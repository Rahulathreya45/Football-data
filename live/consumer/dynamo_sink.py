"""
Shared helpers for writing flattened live-match data into DynamoDB.
Single table design: PK = match_id (Number), SK = item type (String).
"""
import math
import datetime as dt
from decimal import Decimal

import numpy as np
import pandas as pd
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

TEAM_STATS = {                        # api key -> column
    "ballPossession": "possession", "expectedGoals": "xg", "bigChanceCreated": "big_chances",
    "totalShotsOnGoal": "shots_total", "shotsOffGoal": "shots_off_target", "goalkeeperSaves": "saves",
    "passes": "passes", "accuratePasses": "passes_accurate", "fouls": "fouls", "totalTackle": "tackles",
    "interceptionWon": "interceptions", "totalClearance": "clearances", "ballRecovery": "recoveries",
    "touchesInOppBox": "touches_opp_box", "finalThirdEntries": "final_third_entries", "duelWonPercent": "duels_won_pct",
}

PLAYER_STATS = {
    "minutesPlayed": "minutes", "touches": "touches", "totalPass": "passes", "accuratePass": "passes_accurate",
    "totalShots": "shots", "shotOffTarget": "shots_off_target", "expectedGoals": "xg", "expectedAssists": "xa",
    "duelWon": "duels_won", "duelLost": "duels_lost", "fouls": "fouls", "wasFouled": "was_fouled",
    "totalClearance": "clearances", "ballRecovery": "recoveries",
}

INCIDENT_TYPE_PREFIX = {"goal": "GOAL", "card": "CARD", "substitution": "SUB", "varDecision": "VAR"}


def _r3(v):
    return round(v, 3) if isinstance(v, (int, float)) and not (isinstance(v, float) and math.isnan(v)) else v


def to_item(row):
    """dict -> DynamoDB-safe dict: drop NaN/None, numpy -> python, float -> Decimal, timestamp -> ISO string."""
    out = {}
    for k, v in row.items():
        if v is None or (isinstance(v, float) and math.isnan(v)) or v is pd.NaT:
            continue
        if isinstance(v, np.generic):
            v = v.item()
        if isinstance(v, float):
            v = Decimal(str(v))
        elif isinstance(v, (pd.Timestamp, dt.datetime)):
            v = v.isoformat()
        out[k] = v
    return out


def put_latest(table, match_id, sk, row):
    """Full-state message (stats/lineups): overwrite, but never let a late/out-of-order
    Kafka message with an older offset clobber a newer one."""
    item = {**to_item(row), "match_id": match_id, "sk": sk}
    try:
        table.put_item(
            Item=item,
            ConditionExpression="attribute_not_exists(#o) OR #o < :o",
            ExpressionAttributeNames={"#o": "offset"},
            ExpressionAttributeValues={":o": item["offset"]},
        )
    except ClientError as e:
        if e.response["Error"]["Code"] != "ConditionalCheckFailedException":
            raise            # a failed condition just means a stale message; anything else is real


def put_incident(table, match_id, sk, row):
    """Incidents (goal/card/sub/var/injuryTime): each is its own event, so a
    plain overwrite by id is enough — no offset race to guard against."""
    table.put_item(Item={**to_item(row), "match_id": match_id, "sk": sk})


def reconcile_goals(table, match_id, current_goal_ids):
    """Goals are the one incident type that can be retracted (VAR overturn): the
    disallowed goal simply stops appearing in later messages, no flag flips.
    Delete anything previously stored that's no longer in the latest message."""
    resp = table.query(KeyConditionExpression=Key("match_id").eq(match_id) & Key("sk").begins_with("INC#GOAL#"))
    stored_ids = {int(i["sk"].rsplit("#", 1)[-1]) for i in resp["Items"]}
    for stale_id in stored_ids - set(current_goal_ids):
        table.delete_item(Key={"match_id": match_id, "sk": f"INC#GOAL#{stale_id}"})


# ---------------------------------------------------------------- team stats
def write_team_stats(table, match_id, env, team_ids, offset):
    p = env["data"]
    if "error" in p:                       # snapshot before stats exist -> 404 payload
        return
    ts = pd.to_datetime(env["timestamp"], unit="ms", utc=True)
    for block in p.get("statistics", []):
        if block["period"] != "ALL":
            continue
        for side in ("home", "away"):
            row = {"team_id": team_ids.get(side), "offset": offset, "event_ts": ts}
            row.update({col: None for col in TEAM_STATS.values()})
            for g in block["groups"]:
                for it in g["statisticsItems"]:
                    col = TEAM_STATS.get(it["key"])
                    if col and row[col] is None:      # same key repeats across groups -> first wins
                        row[col] = it[f"{side}Value"]
            put_latest(table, match_id, f"STATS#{side}", row)


# ---------------------------------------------------------------- lineups
def write_lineups(table, match_id, env, team_ids, offset):
    p = env["data"]
    ts = pd.to_datetime(env["timestamp"], unit="ms", utc=True)
    for side in ("home", "away"):
        team = p.get(side)
        if not team or not team.get("players"):        # error payload / not published yet
            continue
        ids = [x["teamId"] for x in team["players"]]
        side_team_id = max(set(ids), key=ids.count)    # mode: an academy sub can carry a different teamId
        team_ids[side] = side_team_id                   # feeds stats writes that arrive after this message

        for x in team["players"]:
            row = {
                "side": side, "team_id": side_team_id, "shirt_number": x["shirtNumber"],
                "player_name": x["player"]["name"], "position": x.get("position"),   # absent for some unused subs
                "is_sub": x["substitute"], "is_captain": x.get("captain", False),
                "formation": team.get("formation"), "confirmed": p.get("confirmed"),
                "offset": offset, "event_ts": ts,
            }
            s = x.get("statistics", {})
            for k, col in PLAYER_STATS.items():
                v = s.get(k)
                row[col] = _r3(v) if col in ("xg", "xa") else v
            put_latest(table, match_id, f"LINEUP#{side_team_id}#{x['shirtNumber']:02d}", row)


# ---------------------------------------------------------------- incidents
def write_incidents(table, match_id, env, team_ids, offset):
    ts = pd.to_datetime(env["timestamp"], unit="ms", utc=True)
    goal_ids_now = []

    for inc in env["data"].get("incidents", []):
        itype = inc.get("incidentType")

        if itype == "injuryTime":
            put_incident(table, match_id, f"INC#INJURYTIME#{inc.get('time')}",
                         {"time": inc.get("time"), "length": inc.get("length"), "offset": offset, "event_ts": ts})
            continue

        if itype not in INCIDENT_TYPE_PREFIX or inc.get("id") is None:
            continue                       # period / anything unmapped

        prefix = INCIDENT_TYPE_PREFIX[itype]
        side = "home" if inc.get("isHome") else "away"
        row = {"id": inc["id"], "time": inc.get("time"), "side": side,
               "team_id": team_ids.get(side), "offset": offset, "event_ts": ts}

        if itype == "goal":
            row.update(home_score=inc.get("homeScore"), away_score=inc.get("awayScore"),
                       scorer_name=inc.get("player", {}).get("name"),
                       scorer_short_name=inc.get("player", {}).get("shortName"),
                       scorer_position=inc.get("player", {}).get("position"),
                       scorer_jersey_number=inc.get("player", {}).get("jerseyNumber"),
                       assist_name=inc.get("assist1", {}).get("name"),
                       assist_short_name=inc.get("assist1", {}).get("shortName"),
                       assist_position=inc.get("assist1", {}).get("position"),
                       assist_jersey_number=inc.get("assist1", {}).get("jerseyNumber"))
            goal_ids_now.append(inc["id"])
        elif itype == "card":
            row.update(incident_class=inc.get("incidentClass"), player_name=inc.get("playerName"),
                       reason=inc.get("reason"))
        elif itype == "substitution":
            row.update(player_in_name=inc.get("playerIn", {}).get("name"),
                       player_in_short_name=inc.get("playerIn", {}).get("shortName"),
                       player_in_position=inc.get("playerIn", {}).get("position"),
                       player_in_jersey_number=inc.get("playerIn", {}).get("jerseyNumber"),
                       player_out_name=inc.get("playerOut", {}).get("name"),
                       player_out_short_name=inc.get("playerOut", {}).get("shortName"),
                       player_out_position=inc.get("playerOut", {}).get("position"),
                       player_out_jersey_number=inc.get("playerOut", {}).get("jerseyNumber"))
        elif itype == "varDecision":
            row.update(incident_class=inc.get("incidentClass"), confirmed=inc.get("confirmed"))

        put_incident(table, match_id, f"INC#{prefix}#{inc['id']}", row)

    reconcile_goals(table, match_id, goal_ids_now)