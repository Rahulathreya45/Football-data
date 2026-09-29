"""AI match story: a short written summary of a recorded match, generated
by Gemini on demand (the "Match story" button on the Live tab).

The model never sees raw data. `build_story_facts` turns the S3 live
history (data/live_history.py + queries.get_live_incidents_history) into a
small facts dict for the part of the match the feed has recorded, and
Gemini only writes prose from it. Numbers in the reply are checked against
the facts: one retry with the offending numbers named, then any sentence
still carrying an unknown number is dropped.

Stories aren't stored anywhere. `generate_story` is cached on the facts
JSON, so the same match state is written once per server process and a
new state (more of the match recorded) gets a new story.
"""
import json
import logging
import re

import numpy as np
import pandas as pd
import streamlit as st
from pydantic import BaseModel

from config import GEMINI_API_KEY, GEMINI_MODELS, STORY_MIN_MINUTE
from data.live_history import MatchClock, leaderboard, minute_label, momentum, split_halves
from utils import var_label

log = logging.getLogger(__name__)


class StoryError(Exception):
    """A story couldn't be written; the message is safe to show users."""


# ---------------------------------------------------------------- coverage
def story_coverage(flow: dict | None, match: pd.Series) -> dict | None:
    """How far into the match the recorded feed goes, or None when there's
    too little for a story (no history, or under STORY_MIN_MINUTE)."""
    if flow is None or flow["team"].empty:
        return None
    last = flow["team"].sort_values("event_ts").iloc[-1]
    minute, half = float(last["minute"]), int(last["half"])
    if half == 1 and minute < STORY_MIN_MINUTE:
        return None

    clock, has_result = flow["clock"], pd.notna(match.get("full_time_home_team_score"))
    # The clock stops at the end of each half (45/90 + added time), so a
    # snapshot there was sent after the whistle.
    if half == 2 and (minute >= clock.full_time - 0.5 or (minute >= 90 and has_result)):
        status = "full_time"
    elif half == 2:
        status = "second_half"
    elif minute >= clock.first_half_end - 0.5:
        status = "half_time"
    else:
        status = "first_half"
    return {
        "status": status,
        "minute": minute,
        "half": half,
        "label": "full time" if status == "full_time" else minute_label(minute, half),
        # The recording can stop before the end; the results table may still know the score.
        "final_result_known": status != "full_time" and has_result,
    }


# ---------------------------------------------------------------- facts
STORY_STATS = [
    ("possession_pct", "possession", 0),
    ("xg", "xg", 2),
    ("shots", "shots_total", 0),
    ("shots_off_target", "shots_off_target", 0),
    ("big_chances", "big_chances", 0),
    ("touches_in_opposition_box", "touches_opp_box", 0),
    ("passes", "passes", 0),
    ("pass_accuracy_pct", "pass_accuracy", 0),
    ("goalkeeper_saves", "saves", 0),
    ("fouls", "fouls", 0),
]


def _num(value, digits: int):
    if value is None or pd.isna(value):
        return None
    return int(round(float(value))) if digits == 0 else round(float(value), digits)


def _team_stats(stats: pd.DataFrame, names: dict) -> dict:
    """stats indexed by side -> {team name: {stat: value}}."""
    out = {}
    for side in ("home", "away"):
        if side not in stats.index:
            continue
        row = stats.loc[side]
        out[names[side]] = {key: _num(row.get(col), digits) for key, col, digits in STORY_STATS}
    return out


def _latest_stats(team: pd.DataFrame) -> pd.DataFrame:
    latest = team[team["event_ts"] == team["event_ts"].max()]
    return latest.drop_duplicates("side", keep="last").set_index("side")


def _event(row: pd.Series, names: dict, disallowed: dict) -> dict | None:
    minute = f"{int(row['time'])}'"
    team = names.get(row["side"], row["side"])
    kind = row["kind"]
    if kind == "goal":
        event = {"minute": minute, "type": "goal", "team": team, "scorer": row["player"]}
        if pd.notna(row["home_score"]) and pd.notna(row["away_score"]):
            event["score_after"] = f"{int(row['home_score'])}-{int(row['away_score'])}"
        if pd.notna(row["other_player"]):
            event["assist"] = row["other_player"]
        return event
    if kind == "card":
        card = {"yellow": "yellow card", "red": "red card", "yellowRed": "second yellow card, sent off"}
        event = {"minute": minute, "type": card.get(row["incident_class"], "card"), "team": team, "player": row["player"]}
        if pd.notna(row["reason"]) and row["reason"]:
            event["reason"] = row["reason"]
        return event
    if kind == "sub":
        return {"minute": minute, "type": "substitution", "team": team,
                "player_on": row["player"], "player_off": row["other_player"]}
    if kind == "var":
        event = {"minute": minute, "type": "VAR decision", "team": team,
                 "decision": var_label(row["incident_class"], row["confirmed"])}
        # A goal the feed first reported and then removed is the one VAR ruled out.
        scorer = disallowed.pop(int(row["time"]), None)
        if scorer:
            event["goal_ruled_out_scorer"] = scorer
        return event
    return None


def _events(incidents: pd.DataFrame, names: dict) -> list[dict]:
    """Incidents still in the feed's final list, in order. Goals that were
    reported and later removed are folded into the VAR decision at the same
    minute, or listed as ruled out."""
    if incidents.empty:
        return []
    removed_goals = incidents[(incidents["kind"] == "goal") & ~incidents["in_final"].astype(bool)]
    disallowed = {int(g["time"]): g["player"] for _, g in removed_goals.iterrows()}
    # Allow a minute's slack between the goal and the VAR decision.
    for minute, scorer in list(disallowed.items()):
        for near in (minute - 1, minute + 1):
            disallowed.setdefault(near, scorer)

    kept = incidents[incidents["in_final"].astype(bool)]
    events = [e for e in (_event(row, names, disallowed) for _, row in kept.iterrows()) if e]
    shown = {e.get("goal_ruled_out_scorer") for e in events}
    for _, g in removed_goals.iterrows():
        if g["player"] not in shown:
            events.append({"minute": f"{int(g['time'])}'", "type": "goal ruled out",
                           "team": names.get(g["side"], g["side"]), "scorer": g["player"]})
    return sorted(events, key=lambda e: int(e["minute"].rstrip("'")))


def _dominant_spells(team: pd.DataFrame, clock: MatchClock, names: dict) -> list[dict]:
    """Stretches of 5-minute windows where one side had at least 70% of the
    touches in the opposition box, merged when back to back."""
    touches = momentum(team, clock, "touches_opp_box")
    if touches.empty:
        return []
    xg = momentum(team, clock, "xg")
    wide = touches.pivot_table(index=["half", "start", "end", "label"], columns="side", values="value", fill_value=0).reset_index()
    xg_wide = xg.pivot_table(index=["half", "start"], columns="side", values="value", fill_value=0)

    spells, current = [], None
    for _, w in wide.iterrows():
        home, away = w.get("home", 0.0), w.get("away", 0.0)
        total = home + away
        leader = "home" if home >= 0.7 * total else "away" if away >= 0.7 * total else None
        if total < 3 or leader is None:
            current = None
            continue
        xg_row = xg_wide.loc[(w["half"], w["start"])] if (w["half"], w["start"]) in xg_wide.index else {}
        if current and current["side"] == leader and current["half"] == w["half"] and current["end"] == w["start"]:
            current.update(end=w["end"], last_label=w["label"])
        else:
            current = {"side": leader, "half": w["half"], "start": w["start"], "end": w["end"],
                       "last_label": w["label"], "touches": {"home": 0.0, "away": 0.0}, "xg": {"home": 0.0, "away": 0.0}}
            spells.append(current)
        for side, value in (("home", home), ("away", away)):
            current["touches"][side] += value
            current["xg"][side] += float(xg_row.get(side, 0.0)) if len(xg_row) else 0.0

    out = []
    for s in spells:
        lead, other = s["side"], "away" if s["side"] == "home" else "home"
        end = s["last_label"].split("–")[1]
        out.append({
            "half": int(s["half"]),
            "minutes": f"{int(s['start'])}-{end}",
            "team_on_top": names[lead],
            "touches_in_opposition_box": f"{round(s['touches'][lead])} vs {round(s['touches'][other])}",
            "xg_in_spell": f"{s['xg'][lead]:.2f} vs {s['xg'][other]:.2f}",
        })
    return out


def _top_players(players: pd.DataFrame, names: dict) -> list[dict]:
    board = leaderboard(players, "Goal threat (xG + xA)", top=3)
    latest = players.sort_values("event_ts").groupby(["side", "player_name"]).tail(1).set_index(["side", "player_name"])
    out = []
    for _, p in board.iterrows():
        row = latest.loc[(p["side"], p["player_name"])]
        out.append({
            "player": p["player_name"], "team": names[p["side"]],
            "xg": _num(row["xg"], 2) or 0, "xa": _num(row["xa"], 2) or 0,
            "shots": _num(row["shots"], 0) or 0, "touches": _num(row["touches"], 0) or 0,
        })
    return out


def _score(events: list[dict], upto: int | None = None) -> str:
    goals = [e for e in events if e["type"] == "goal" and (upto is None or int(e["minute"].rstrip("'")) <= upto)]
    scores = [g["score_after"] for g in goals if "score_after" in g]
    return scores[-1] if scores else "0-0"


def _result(score: str, names: dict, finished: bool) -> str:
    """'2-3' -> 'Aston Villa FC won 3-2' (or 'lead 3-2' mid-match)."""
    home, away = (int(n) for n in score.split("-"))
    if home == away:
        return f"draw {home}-{away}" if finished else f"level at {home}-{away}"
    winner, high, low = (names["home"], home, away) if home > away else (names["away"], away, home)
    return f"{winner} {'won' if finished else 'lead'} {high}-{low}"


def build_story_facts(match: pd.Series, flow: dict, incidents: pd.DataFrame, coverage: dict) -> dict:
    """Everything the story may say, for the part of the match recorded."""
    names = {"home": match["home_team_name"], "away": match["away_team_name"]}
    team, clock = flow["team"], flow["clock"]
    events = _events(incidents, names)
    spells = _dominant_spells(team, clock, names)
    status = coverage["status"]

    facts = {
        "match": {
            "competition": "Premier League",
            "date": pd.to_datetime(match["match_date"]).strftime("%d %B %Y"),
            "home_team": names["home"],
            "away_team": names["away"],
        },
        "status": status,
        "recorded_until": coverage["label"],
        "score": f"{names['home']} {_score(events)} {names['away']}",
        "result_so_far": _result(_score(events), names, status == "full_time"),
    }
    if coverage["final_result_known"]:
        facts["final_result"] = (f"{names['home']} {int(match['full_time_home_team_score'])}-"
                                 f"{int(match['full_time_away_team_score'])} {names['away']}")

    first_events = [e for e in events if int(e["minute"].rstrip("'")) <= 45]
    second_events = [e for e in events if int(e["minute"].rstrip("'")) > 45]
    halves = split_halves(flow) if status in ("second_half", "full_time") else None

    facts["first_half"] = {"events": first_events, "spells_on_top": [s for s in spells if s["half"] == 1]}
    if status == "first_half":
        facts["first_half"]["team_stats_so_far"] = _team_stats(_latest_stats(team), names)
    elif halves is not None:
        facts["first_half"]["team_stats"] = _team_stats(halves["1st"], names)

    if status in ("half_time", "second_half", "full_time"):
        facts["half_time_score"] = f"{names['home']} {_score(events, 45)} {names['away']}"
        if status == "half_time":
            facts["first_half"]["team_stats"] = _team_stats(_latest_stats(team), names)

    if status in ("second_half", "full_time"):
        facts["second_half"] = {"events": second_events, "spells_on_top": [s for s in spells if s["half"] == 2]}
        if halves is not None:
            facts["second_half"]["team_stats"] = _team_stats(halves["2nd"], names)
        facts["whole_match_team_stats"] = _team_stats(_latest_stats(team), names)

    if not flow["players"].empty:
        facts["top_players_by_xg_plus_xa"] = _top_players(flow["players"], names)
    return facts


# ---------------------------------------------------------------- generation
class MatchStory(BaseModel):
    headline: str
    overview: str
    first_half: str
    second_half: str


SYSTEM_PROMPT = """You are a football reporter writing short match stories for a Premier League
stats dashboard. You write ONLY from the FACTS JSON you are given.

Rules:
- Never invent players, events, reasons, injuries, quotes, or context that isn't in the facts.
- Only use numbers that appear in the facts (scores, minutes, stats). Don't calculate new
  numbers such as totals, differences or percentages.
- Keep every number in its scope: a first_half stat is not a second_half or whole-match stat,
  and one team's number is never the other team's. Describe the result as in "result_so_far".
- Write like a match report, not a stats sheet: tell what happened and how the game flowed,
  and use only the 2-3 most telling numbers per section. Write expected goals as "xG".
- Use each team's name as given. British English. Plain prose, no markdown, no bullet points.
- "spells_on_top" are periods when one team pinned the other back; use them to describe the flow.
- A "VAR decision" of "Goal disallowed" or a "goal ruled out" is a goal that didn't count.
- Write about the match only up to "recorded_until"; don't guess what happens after it.

Fields:
- headline: one short line that captures the story (not just the score).
- overview: status "full_time" -> 2-3 sentences on the whole match (result, decisive moments,
  which side created more). If "final_result" is present instead, the recording stopped early:
  one sentence saying the recording ends at "recorded_until" and giving the final result.
  Otherwise "".
- first_half: status "first_half" -> 3-5 sentences on the match so far. "half_time" -> 3-5
  sentences on the first half. "second_half" -> 2-3 sentences starting "Up to half-time".
  "full_time" -> 2-4 sentences on the first half.
- second_half: "" unless status is "second_half" (3-4 sentences on the play since the break)
  or "full_time" (2-4 sentences on the second half)."""


_NUMBER = re.compile(r"\d+(?:\.\d+)?")


def _allowed_numbers(facts_json: str) -> set[str]:
    allowed = {_normal(n) for n in _NUMBER.findall(facts_json)}
    return allowed | {str(n) for n in range(11)} | {"45", "90"}


def _normal(number: str) -> str:
    return str(float(number)).rstrip("0").rstrip(".") if "." in number else str(int(number))


def _unknown_numbers(story: MatchStory, allowed: set[str]) -> set[str]:
    text = " ".join([story.headline, story.overview, story.first_half, story.second_half])
    return {n for n in _NUMBER.findall(text) if _normal(n) not in allowed}


def _drop_unverified(text: str, allowed: set[str]) -> str:
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    return " ".join(s for s in sentences if all(_normal(n) in allowed for n in _NUMBER.findall(s)))


@st.cache_resource(show_spinner=False)
def _client():
    from google import genai
    return genai.Client(api_key=_api_key())


def _api_key() -> str | None:
    if GEMINI_API_KEY:
        return GEMINI_API_KEY
    try:
        return st.secrets.get("GEMINI_API_KEY")
    except Exception:
        return None


def _ask(contents: list) -> MatchStory:
    """One call, trying each model in GEMINI_MODELS until one answers."""
    from google.genai import errors, types

    config = types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT,
        temperature=0.2,
        response_mime_type="application/json",
        response_schema=MatchStory,
        automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True),
    )
    last_error = None
    for model in GEMINI_MODELS:
        try:
            response = _client().models.generate_content(model=model, contents=contents, config=config)
        except errors.APIError as e:
            # 429 = free-tier quota used up, 404 = model retired, 5xx = overloaded: try the next.
            log.warning("Gemini %s failed: %s %s", model, e.code, e.message)
            last_error = e
            if e.code in (429, 404) or e.code >= 500:
                continue
            raise StoryError("The AI service rejected the request.") from e
        if response.parsed is None:
            last_error = ValueError(f"{model} returned no parsable story")
            continue
        return response.parsed

    if isinstance(last_error, errors.APIError) and last_error.code == 429:
        raise StoryError("The free AI quota is used up for now. Please try again later.") from last_error
    raise StoryError("Couldn't reach the AI service right now. Please try again in a moment.") from last_error


@st.cache_data(show_spinner=False, max_entries=200)
def generate_story(facts_json: str) -> dict:
    """The story for one match state, as a dict of MatchStory fields."""
    if not _api_key():
        raise StoryError("Match stories aren't set up: GEMINI_API_KEY is missing.")

    prompt = f"FACTS:\n{facts_json}"
    allowed = _allowed_numbers(facts_json)
    story = _ask([prompt])
    unknown = _unknown_numbers(story, allowed)
    if unknown:
        log.info("Story used numbers not in the facts (%s); retrying", sorted(unknown))
        story = _ask([prompt, f"Your previous story used numbers that aren't in the facts: "
                              f"{', '.join(sorted(unknown))}. Rewrite it using only numbers from the facts."])
    fields = story.model_dump()
    if _unknown_numbers(story, allowed):
        fields = {k: _drop_unverified(v, allowed) for k, v in fields.items()}
    return fields


def facts_to_json(facts: dict) -> str:
    """Stable JSON (the cache key for generate_story)."""
    def default(value):
        if isinstance(value, (np.integer, np.floating)):
            return value.item()
        return str(value)
    return json.dumps(facts, ensure_ascii=False, indent=1, default=default)
