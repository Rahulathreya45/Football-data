"""Live-feed data (v2): the DynamoDB table filled by the Kafka consumer
(live/consumer/kafka_to_dynamo.py + dynamo_sink.py).

Single-table design: PK match_id = sportsapipro's match id, SK one of
STATS#home|away, LINEUP#<team>#<shirt>, INC#GOAL|CARD|SUB|VAR#<id>,
INC#INJURYTIME#<minute>. Items carry sportsapipro team ids.

The feed knows nothing about football-data.org ids, so a captured match is
mapped onto a dashboard match by its (home team, away team) - through
dim_team.sports_api_pro_team_id - plus the kickoff date. That needs no
sportsapipro match id to be ingested ahead of the match.
"""
import logging
from decimal import Decimal

import pandas as pd
import streamlit as st
from boto3.dynamodb.conditions import Key
from botocore.exceptions import BotoCoreError, ClientError

from config import LIVE_MATCH_TABLE, LIVE_REGION
from data.db import DataSourceError, get_aws_session
from data.queries import get_match_keys, get_team_sports_api_ids

# Item event_ts is the last message's time, i.e. match day (or shortly after
# for a late replay). The same fixture from another season is months away.
MATCH_DATE_TOLERANCE = pd.Timedelta(days=3)

_ITEM_KINDS = {
    "STATS": "stats", "LINEUP": "lineups",
    "INC#GOAL": "goals", "INC#CARD": "cards", "INC#SUB": "subs",
    "INC#VAR": "var", "INC#INJURYTIME": "injury_time",
}


@st.cache_resource(show_spinner=False)
def _table():
    return get_aws_session().resource("dynamodb", region_name=LIVE_REGION).Table(LIVE_MATCH_TABLE)


def _plain(value):
    """DynamoDB hands numbers back as Decimal: int when whole, else float."""
    if isinstance(value, Decimal):
        return int(value) if value == value.to_integral_value() else float(value)
    return value


def _read_all(operation, **kwargs) -> list[dict]:
    """Run a paginated scan/query and return every item as plain Python."""
    items = []
    try:
        while True:
            resp = operation(**kwargs)
            items.extend({k: _plain(v) for k, v in item.items()} for item in resp["Items"])
            if "LastEvaluatedKey" not in resp:
                return items
            kwargs["ExclusiveStartKey"] = resp["LastEvaluatedKey"]
    except (BotoCoreError, ClientError) as e:
        raise DataSourceError(f"Couldn't read the live table '{LIVE_MATCH_TABLE}': {e}") from e


@st.cache_data(ttl=300, show_spinner=False)
def _recorded_matches() -> pd.DataFrame:
    """One row per captured match: live_match_id, each side's sportsapipro
    team id, and the last message time. A full scan, but with a narrow
    projection, and the table only holds a handful of matches."""
    items = _read_all(_table().scan, ProjectionExpression="match_id, sk, side, team_id, event_ts")
    columns = ["live_match_id", "home_sap_team_id", "away_sap_team_id", "last_event_ts"]
    df = pd.DataFrame(items).reindex(columns=["match_id", "sk", "side", "team_id", "event_ts"])
    if df.empty:
        return pd.DataFrame(columns=columns)

    # Lineup/incident items carry `side`; team stats keep it in the sort key.
    df["side"] = df["side"].fillna(df["sk"].str.extract(r"^STATS#(\w+)$")[0])
    sides = (
        df.dropna(subset=["side", "team_id"])
        .groupby(["match_id", "side"])["team_id"]
        .agg(lambda s: s.mode().iloc[0])
        .unstack()
        .reindex(columns=["home", "away"])
    )
    last_ts = pd.to_datetime(df["event_ts"], utc=True, format="ISO8601").groupby(df["match_id"]).max()

    out = pd.DataFrame({"last_event_ts": last_ts}).join(sides)
    out = out.rename(columns={"home": "home_sap_team_id", "away": "away_sap_team_id"})
    return out.rename_axis("live_match_id").reset_index()[columns]


@st.cache_data(ttl=300, show_spinner=False)
def get_live_match_map() -> pd.DataFrame:
    """match_id (dashboard) -> live_match_id for every capture that maps onto
    a known fixture. Captures from other competitions, or without lineups
    (so no team ids), don't map and are left out."""
    columns = ["match_id", "live_match_id", "last_event_ts"]
    recorded = _recorded_matches().dropna(subset=["home_sap_team_id", "away_sap_team_id"])

    teams = get_team_sports_api_ids()
    sap_to_team = dict(zip(teams["sports_api_pro_team_id"].astype("int64"), teams["team_id"]))
    recorded = recorded.assign(
        home_team_id=recorded["home_sap_team_id"].astype("int64").map(sap_to_team),
        away_team_id=recorded["away_sap_team_id"].astype("int64").map(sap_to_team),
    ).dropna(subset=["home_team_id", "away_team_id"])
    if recorded.empty:
        return pd.DataFrame(columns=columns)

    recorded = recorded.astype({"home_team_id": "int64", "away_team_id": "int64"})
    fixtures = get_match_keys().astype({"home_team_id": "int64", "away_team_id": "int64"})
    candidates = recorded.merge(fixtures, on=["home_team_id", "away_team_id"])
    candidates["gap"] = (
        pd.to_datetime(candidates["match_date"], utc=True) - candidates["last_event_ts"]
    ).abs()
    candidates = candidates[candidates["gap"] <= MATCH_DATE_TOLERANCE]

    # Nearest fixture per capture, then the latest capture per fixture.
    candidates = (
        candidates.sort_values("gap").drop_duplicates("live_match_id")
        .sort_values("last_event_ts", ascending=False).drop_duplicates("match_id")
    )
    return candidates[columns].reset_index(drop=True)


def find_live_match_id(match_id: int) -> int | None:
    """The live feed's match id for a dashboard match, or None if the feed
    wasn't recorded for it. Raises DataSourceError if DynamoDB is unreachable."""
    live_map = get_live_match_map()
    hit = live_map[live_map["match_id"] == match_id]
    return None if hit.empty else int(hit["live_match_id"].iloc[0])


def recorded_match_ids() -> set[int]:
    """Dashboard match ids that have a live feed. Best effort - only drives
    the "Live feed" badges on match cards, so a DynamoDB failure just hides
    the badges instead of breaking the page."""
    try:
        return set(get_live_match_map()["match_id"].astype(int))
    except DataSourceError:
        logging.getLogger(__name__).warning("Live feed lookup failed", exc_info=True)
        return set()


@st.cache_data(ttl=60, show_spinner=False)
def get_live_match_data(live_match_id: int) -> dict[str, pd.DataFrame]:
    """Every item for one captured match, split by kind: stats, lineups,
    goals, cards, subs, var, injury_time (one DataFrame each, possibly empty)."""
    items = _read_all(_table().query, KeyConditionExpression=Key("match_id").eq(live_match_id))
    df = pd.DataFrame(items)
    if df.empty:
        return {name: pd.DataFrame() for name in _ITEM_KINDS.values()}

    prefix = df["sk"].str.extract(r"^(STATS|LINEUP|INC#[A-Z]+)")[0]
    data = {
        name: df[prefix == key].dropna(axis=1, how="all").reset_index(drop=True)
        for key, name in _ITEM_KINDS.items()
    }
    if not data["stats"].empty:
        data["stats"]["side"] = data["stats"]["sk"].str.split("#").str[1]
    return data
