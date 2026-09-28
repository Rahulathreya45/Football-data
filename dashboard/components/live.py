import re

import pandas as pd
import streamlit as st

from components.events import render_card_row, render_sub_row, render_time_marker
from components.lineups import render_team_lineup
from components.stats import render_stat_bar
from components.ui import render_goal_row
from utils import format_minute

# sportsapipro positions are just G/D/M/F; the shared lineup renderer
# expects FBref-style codes.
_POSITION_CODES = {"G": "GK", "D": "DF", "M": "MF", "F": "FW"}

# Same-minute events: goals first, then VAR, cards, subs.
_KIND_ORDER = {"goal": 0, "var": 1, "card": 2, "sub": 3}

TEAM_STAT_SECTIONS = [
    ("Attack", [
        ("Possession", "possession", "{:.0f}%"),
        ("Expected Goals (xG)", "xg", "{:.2f}"),
        ("Big Chances", "big_chances", "{:.0f}"),
        ("Shots", "shots_total", "{:.0f}"),
        ("Shots off Target", "shots_off_target", "{:.0f}"),
        ("Touches in Opposition Box", "touches_opp_box", "{:.0f}"),
        ("Final Third Entries", "final_third_entries", "{:.0f}"),
    ]),
    ("Passing", [
        ("Passes", "passes", "{:.0f}"),
        ("Accurate Passes", "passes_accurate", "{:.0f}"),
        ("Pass Accuracy", "pass_accuracy", "{:.0f}%"),
    ]),
    ("Defending", [
        ("Tackles", "tackles", "{:.0f}"),
        ("Interceptions", "interceptions", "{:.0f}"),
        ("Clearances", "clearances", "{:.0f}"),
        ("Ball Recoveries", "recoveries", "{:.0f}"),
        ("Goalkeeper Saves", "saves", "{:.0f}"),
        ("Fouls", "fouls", "{:.0f}"),
        ("Duels Won", "duels_won_pct", "{:.0f}%"),
    ]),
]

PLAYER_COLUMNS = {
    "shirt_number": st.column_config.NumberColumn("#", format="%d", width="small"),
    "player_name": st.column_config.TextColumn("Player"),
    "position": st.column_config.TextColumn("Pos", width="small"),
    "minutes": st.column_config.NumberColumn("Min", format="%d"),
    "touches": st.column_config.NumberColumn("Touches", format="%d"),
    "passes": st.column_config.NumberColumn("Passes", format="%d"),
    "pass_accuracy": st.column_config.ProgressColumn("Pass %", format="%.0f%%", min_value=0, max_value=100),
    "shots": st.column_config.NumberColumn("Shots", format="%d"),
    "shots_off_target": st.column_config.NumberColumn("Off target", format="%d"),
    "xg": st.column_config.NumberColumn("xG", format="%.2f"),
    "xa": st.column_config.NumberColumn("xA", format="%.2f"),
    "duels_won": st.column_config.NumberColumn("Duels won", format="%d"),
    "duels_lost": st.column_config.NumberColumn("Duels lost", format="%d"),
    "fouls": st.column_config.NumberColumn("Fouls", format="%d"),
    "was_fouled": st.column_config.NumberColumn("Fouled", format="%d"),
    "clearances": st.column_config.NumberColumn("Clearances", format="%d"),
    "recoveries": st.column_config.NumberColumn("Recoveries", format="%d"),
}


def _pct(part, whole):
    return part / whole * 100 if pd.notna(part) and pd.notna(whole) and whole else None


def _minute(value):
    """Incident minute as an int. DynamoDB items of every kind share one
    DataFrame upstream, so whole numbers can come through as floats."""
    return int(value) if pd.notna(value) else None


def _humanize_class(value) -> str:
    """'goalAwarded' -> 'Goal awarded'."""
    words = re.sub(r"(?<!^)(?=[A-Z])", " ", str(value or "")).lower()
    return words.capitalize()


def _feed_score(goals: pd.DataFrame) -> tuple[int, int]:
    """Score after the last goal the feed recorded (goal items carry the
    running score)."""
    if goals.empty or "home_score" not in goals:
        return 0, 0
    last = goals.sort_values(["time", "id"]).iloc[-1]
    return int(last["home_score"]), int(last["away_score"])


def _side_stats(stats: pd.DataFrame, side: str) -> pd.Series:
    rows = stats[stats["side"] == side] if not stats.empty else stats
    if rows.empty:
        return pd.Series(dtype=object)
    row = rows.iloc[0].copy()
    row["pass_accuracy"] = _pct(row.get("passes_accurate"), row.get("passes"))
    return row


def _last_update(live: dict):
    stamps = [pd.to_datetime(df["event_ts"], utc=True, format="ISO8601").max()
              for df in live.values() if not df.empty and "event_ts" in df]
    return max(stamps) if stamps else pd.NaT


def _render_summary(live: dict):
    home_score, away_score = _feed_score(live["goals"])
    home, away = _side_stats(live["stats"], "home"), _side_stats(live["stats"], "away")

    with st.container(horizontal=True):
        st.metric("Score (live feed)", f"{home_score} - {away_score}", border=True)
        if not home.empty and not away.empty:
            st.metric("xG", f"{home.get('xg', 0):.2f} - {away.get('xg', 0):.2f}", border=True)
            st.metric("Possession", f"{home.get('possession', 0):.0f}% - {away.get('possession', 0):.0f}%", border=True)
            st.metric("Shots", f"{home.get('shots_total', 0):.0f} - {away.get('shots_total', 0):.0f}", border=True)

    last_update = _last_update(live)
    updated = last_update.strftime("%d %b %Y · %H:%M UTC") if pd.notna(last_update) else "unknown"
    st.caption(f"Last updated {updated}")


# ---------------------------------------------------------------- timeline
def _timeline_events(live: dict) -> list[dict]:
    events = []
    for _, g in live["goals"].iterrows():
        events.append(dict(
            kind="goal", time=_minute(g.get("time")), id=g.get("id"), side=g.get("side"),
            minute=_minute(g.get("time")), scorer=g.get("scorer_name", ""), assist=g.get("assist_name"),
        ))
    for _, c in live["cards"].iterrows():
        card_class = c.get("incident_class")
        events.append(dict(
            kind="card", time=_minute(c.get("time")), id=c.get("id"), side=c.get("side"),
            minute=_minute(c.get("time")), player_1_name=c.get("player_name", ""),
            second_yellow=card_class == "yellowRed", red=card_class == "red",
        ))
    for _, s in live["subs"].iterrows():
        events.append(dict(
            kind="sub", time=_minute(s.get("time")), id=s.get("id"), side=s.get("side"),
            minute=_minute(s.get("time")), sub_in=s.get("player_in_name", ""), sub_out=s.get("player_out_name", ""),
        ))
    for _, v in live["var"].iterrows():
        events.append(dict(
            kind="var", time=_minute(v.get("time")), id=v.get("id"), side=v.get("side"),
            minute=_minute(v.get("time")), label=_humanize_class(v.get("incident_class")),
        ))
    return sorted(events, key=lambda e: (e["time"] or 0, _KIND_ORDER[e["kind"]], e["id"] or 0))


def _render_var_row(event: dict, align: str):
    badge = "<span class='event-badge sub'>VAR</span>"
    text = f"<span class='goal-scorer'>{event['label']} {format_minute(event['minute'])}</span>"
    inner = f"{badge}{text}" if align == "left" else f"{text}{badge}"
    st.markdown(f"<div class='goal-row {align}'>{inner}</div>", unsafe_allow_html=True)


def _render_event(event: dict):
    c1, c2 = st.columns(2)
    align = "left" if event["side"] == "home" else "right"
    with c1 if align == "left" else c2:
        if event["kind"] == "goal":
            render_goal_row(event, align=align)
        elif event["kind"] == "card":
            render_card_row(event, align=align)
        elif event["kind"] == "sub":
            render_sub_row(event, align=align)
        else:
            _render_var_row(event, align)


def _added_time(injury: pd.DataFrame, minute: int) -> str:
    if injury.empty or "time" not in injury:
        return ""
    rows = injury[injury["time"] == minute]
    if rows.empty or pd.isna(rows["length"].iloc[0]):
        return ""
    return f" · +{int(rows['length'].iloc[0])} min"


def _score_at(goals: pd.DataFrame, minute: int) -> str:
    before = goals[goals["time"] <= minute] if not goals.empty else goals
    home, away = _feed_score(before)
    return f"{home} - {away}"


def _render_timeline(live: dict):
    events = _timeline_events(live)
    if not events:
        st.caption("No goals, cards or substitutions in the live feed for this match.")
        return

    goals, injury = live["goals"], live["injury_time"]
    for event in (e for e in events if (e["time"] or 0) <= 45):
        _render_event(event)
    render_time_marker(f"Half-time · {_score_at(goals, 45)}{_added_time(injury, 45)}")
    for event in (e for e in events if (e["time"] or 0) > 45):
        _render_event(event)
    render_time_marker(f"Full-time · {_score_at(goals, 999)}{_added_time(injury, 90)}")


# ---------------------------------------------------------------- team stats
def _render_team_stats(live: dict, match: pd.Series):
    home, away = _side_stats(live["stats"], "home"), _side_stats(live["stats"], "away")
    if home.empty or away.empty:
        st.caption("The live feed has no team stats for this match.")
        return

    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"<div class='formation-label'>{match['home_team_name']}</div>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div class='formation-label'>{match['away_team_name']}</div>", unsafe_allow_html=True)

    for section, rows in TEAM_STAT_SECTIONS:
        st.markdown(f"<div class='section-header'>{section}</div>", unsafe_allow_html=True)
        for label, col, fmt in rows:
            render_stat_bar(label, home.get(col), away.get(col), fmt=fmt)


# ---------------------------------------------------------------- lineups
def _lineup_frame(lineups: pd.DataFrame, side: str) -> pd.DataFrame:
    team = lineups[lineups["side"] == side]
    return pd.DataFrame({
        "jersey_number": team["shirt_number"],
        "player_name": team["player_name"],
        # Unused subs can lack a position; the lineup renderer needs a string.
        "position": team.get("position", pd.Series(index=team.index, dtype=object)).map(_POSITION_CODES).fillna(""),
        "is_starter": ~team["is_sub"].astype(bool),
        "team_formation": team.get("formation"),
        "is_captain": team.get("is_captain", False),
    })


def _render_lineups(live: dict, match: pd.Series):
    lineups = live["lineups"]
    if lineups.empty:
        st.caption("The live feed has no lineups for this match.")
        return
    if "confirmed" in lineups and not lineups["confirmed"].fillna(False).astype(bool).all():
        st.caption(":material/info: These are predicted lineups; the feed never confirmed them.")

    c1, c2 = st.columns(2)
    for col, side in ((c1, "home"), (c2, "away")):
        team_df = _lineup_frame(lineups, side)
        with col, st.container(border=True):
            render_team_lineup(team_df, match[f"{side}_team_name"], match.get(f"{side}_team_crest", ""))
            captains = team_df.loc[team_df["is_captain"].fillna(False).astype(bool), "player_name"]
            if not captains.empty:
                st.caption(f"**Captain:** {captains.iloc[0]}", text_alignment="center")


# ---------------------------------------------------------------- player stats
def _render_player_stats(live: dict, match: pd.Series):
    lineups = live["lineups"]
    if lineups.empty or "minutes" not in lineups:
        st.caption("The live feed has no player stats for this match.")
        return

    names = {"home": match["home_team_name"], "away": match["away_team_name"]}
    side = st.segmented_control(
        "Team", options=["home", "away"], format_func=names.get,
        default="home", key="live_player_stats_side", label_visibility="collapsed",
    ) or "home"

    players = lineups[(lineups["side"] == side) & lineups["minutes"].notna()].copy()
    if players.empty:
        st.caption("No player stats for this team.")
        return
    players["pass_accuracy"] = [_pct(a, p) for a, p in zip(players.get("passes_accurate"), players.get("passes"))]
    if "position" in players:
        players["position"] = players["position"].map(_POSITION_CODES)
    players = players.sort_values(["is_sub", "shirt_number"]).reindex(columns=list(PLAYER_COLUMNS))
    # The feed leaves a stat out when it's zero; these players were on the pitch.
    counts = [c for c in PLAYER_COLUMNS if c not in ("shirt_number", "player_name", "position", "pass_accuracy")]
    players[counts] = players[counts].fillna(0)

    st.dataframe(players, hide_index=True, column_config=PLAYER_COLUMNS, width="stretch")
    st.caption("Players who got on the pitch. xG/xA: expected goals/assists.")


def render_live_tab(match: pd.Series, live: dict):
    """Live tab on Match Detail: what the v2 live feed captured for this
    match (data/live.py get_live_match_data), in sub-tabs."""
    _render_summary(live)

    tab_timeline, tab_stats, tab_lineups, tab_players = st.tabs(
        ["Timeline", "Team stats", "Lineups", "Player stats"]
    )
    with tab_timeline:
        _render_timeline(live)
    with tab_stats:
        _render_team_stats(live, match)
    with tab_lineups:
        _render_lineups(live, match)
    with tab_players:
        _render_player_stats(live, match)
