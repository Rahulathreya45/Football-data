import pandas as pd
import streamlit as st

from utils import humanize_column
from data.queries import (
    get_team_match_performance,
    get_player_match_performance,
    get_goalkeeper_match_performance,
)

PLAYER_COLUMNS = [
    "player_name", "jersey_number", "position", "minutes_played",
    "goals", "assists", "shots", "shots_on_target",
    "penalty_goals", "penalty_attempts",
    "yellow_cards", "red_cards",
    "fouls_committed", "fouls_drawn", "offsides",
    "crosses", "tackles_won", "interceptions", "own_goals",
]

GOALKEEPER_COLUMNS = [
    "player_name", "minutes_played",
    "gk_shots_on_target_against", "gk_goals_against", "gk_saves", "gk_save_pct",
]


def _fmt(val, fmt: str) -> str:
    if pd.isna(val):
        return "-"
    return fmt.format(val)


def _split_pct(home_val, away_val):
    h = home_val if pd.notna(home_val) else 0
    a = away_val if pd.notna(away_val) else 0
    total = h + a
    if total <= 0:
        return 50.0, 50.0
    return h / total * 100, a / total * 100


def render_stat_bar(label: str, home_val, away_val, fmt: str = "{:.0f}"):
    home_pct, away_pct = _split_pct(home_val, away_val)
    home_txt = _fmt(home_val, fmt)
    away_txt = _fmt(away_val, fmt)

    html = (
        "<div class='stat-bar-block'>"
        f"<div class='stat-bar-label'>{label}</div>"
        "<div class='stat-bar-row'>"
        f"<span class='stat-bar-value left'>{home_txt}</span>"
        "<div class='stat-bar-track'>"
        f"<div class='stat-bar-fill home' style='width:{home_pct:.1f}%'></div>"
        f"<div class='stat-bar-fill away' style='width:{away_pct:.1f}%'></div>"
        "</div>"
        f"<span class='stat-bar-value right'>{away_txt}</span>"
        "</div>"
        "</div>"
    )
    st.markdown(html, unsafe_allow_html=True)


def render_stat_row(label: str, home_val, away_val, fmt: str = "{:.0f}"):
    home_txt = _fmt(home_val, fmt)
    away_txt = _fmt(away_val, fmt)
    st.markdown(
        "<div class='stat-row'>"
        f"<span class='stat-row-value'>{home_txt}</span>"
        f"<span class='stat-row-label'>{label}</span>"
        f"<span class='stat-row-value'>{away_txt}</span>"
        "</div>",
        unsafe_allow_html=True,
    )


def _render_clean_sheet_row(home_val, away_val):
    home_txt = "✅ Clean sheet" if home_val == 1 else "—"
    away_txt = "✅ Clean sheet" if away_val == 1 else "—"
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"<div style='text-align:center;'>{home_txt}</div>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div style='text-align:center;'>{away_txt}</div>", unsafe_allow_html=True)


def _render_team_meta(home: pd.Series, away: pd.Series, match: pd.Series):
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            f"<div class='formation-label'>{match['home_team_name']} · {home.get('team_formation', '')}</div>",
            unsafe_allow_html=True,
        )
        st.caption(f"Captain: {home.get('captain_name') or '-'}")
    with c2:
        st.markdown(
            f"<div class='formation-label'>{match['away_team_name']} · {away.get('team_formation', '')}</div>",
            unsafe_allow_html=True,
        )
        st.caption(f"Captain: {away.get('captain_name') or '-'}")


def render_team_stats_tab(match: pd.Series):
    perf_df = get_team_match_performance(int(match["match_id"]))
    if perf_df.empty:
        st.caption("Team stats aren't available for this match yet.")
        return

    home_rows = perf_df[perf_df["team_id"] == match["home_team_id"]]
    away_rows = perf_df[perf_df["team_id"] == match["away_team_id"]]
    if home_rows.empty or away_rows.empty:
        st.caption("Team stats aren't available for this match yet.")
        return

    home, away = home_rows.iloc[0], away_rows.iloc[0]

    _render_team_meta(home, away, match)

    st.markdown("<div class='section-header'>Possession</div>", unsafe_allow_html=True)
    render_stat_bar("Possession", home.get("possession_pct"), away.get("possession_pct"), fmt="{:.0f}%")

    st.markdown("<div class='section-header'>Shooting</div>", unsafe_allow_html=True)
    render_stat_bar("Goals", home.get("shooting_goals"), away.get("shooting_goals"))
    render_stat_bar("Shots", home.get("shooting_shots"), away.get("shooting_shots"))
    render_stat_bar("Shots on Target", home.get("shooting_shots_on_target"), away.get("shooting_shots_on_target"))
    render_stat_bar(
        "Shots on Target %", home.get("shooting_shots_on_target_pct"),
        away.get("shooting_shots_on_target_pct"), fmt="{:.1f}%",
    )
    render_stat_bar(
        "Goals per Shot", home.get("shooting_goals_per_shot"),
        away.get("shooting_goals_per_shot"), fmt="{:.2f}",
    )
    render_stat_bar(
        "Goals per Shot on Target", home.get("shooting_goals_per_shot_on_target"),
        away.get("shooting_goals_per_shot_on_target"), fmt="{:.2f}",
    )
    render_stat_bar("Penalty Goals", home.get("shooting_penalty_goals"), away.get("shooting_penalty_goals"))
    render_stat_bar("Penalty Attempts", home.get("shooting_penalty_attempts"), away.get("shooting_penalty_attempts"))

    st.markdown("<div class='section-header'>Discipline</div>", unsafe_allow_html=True)
    render_stat_row("Yellow Cards", home.get("misc_yellow_cards"), away.get("misc_yellow_cards"))
    render_stat_row("Red Cards", home.get("misc_red_cards"), away.get("misc_red_cards"))
    render_stat_row("Second Yellows", home.get("misc_second_yellow_cards"), away.get("misc_second_yellow_cards"))
    render_stat_row("Fouls Committed", home.get("misc_fouls_committed"), away.get("misc_fouls_committed"))
    render_stat_row("Fouls Drawn", home.get("misc_fouls_drawn"), away.get("misc_fouls_drawn"))
    render_stat_row("Offsides", home.get("misc_offsides"), away.get("misc_offsides"))
    render_stat_row("Crosses", home.get("misc_crosses"), away.get("misc_crosses"))
    render_stat_row("Interceptions", home.get("misc_interceptions"), away.get("misc_interceptions"))
    render_stat_row("Tackles Won", home.get("misc_tackles_won"), away.get("misc_tackles_won"))
    render_stat_row("Own Goals", home.get("misc_own_goals"), away.get("misc_own_goals"))

    st.markdown("<div class='section-header'>Goalkeeping</div>", unsafe_allow_html=True)
    render_stat_row(
        "Shots on Target Against", home.get("gk_shots_on_target_against"),
        away.get("gk_shots_on_target_against"),
    )
    render_stat_row("Goals Against", home.get("gk_goals_against"), away.get("gk_goals_against"))
    render_stat_row("Saves", home.get("gk_saves"), away.get("gk_saves"))
    render_stat_row("Save %", home.get("gk_save_pct"), away.get("gk_save_pct"), fmt="{:.1f}%")
    _render_clean_sheet_row(home.get("gk_clean_sheet"), away.get("gk_clean_sheet"))
    render_stat_row("Penalties Faced", home.get("gk_penalty_kicks_faced"), away.get("gk_penalty_kicks_faced"))
    render_stat_row("Penalties Allowed", home.get("gk_penalty_kicks_allowed"), away.get("gk_penalty_kicks_allowed"))
    render_stat_row("Penalties Saved", home.get("gk_penalty_kicks_saved"), away.get("gk_penalty_kicks_saved"))
    render_stat_row("Penalties Missed", home.get("gk_penalty_kicks_missed"), away.get("gk_penalty_kicks_missed"))


def _render_team_table(df: pd.DataFrame, team_id: int, columns: list, sort_by: str = None):
    team_df = df[df["team_id"] == team_id]
    if team_df.empty:
        st.caption("No data available.")
        return

    team_df = team_df[columns].copy()
    if sort_by and sort_by in team_df.columns:
        team_df = team_df.sort_values(sort_by)

    team_df.columns = [humanize_column(c) for c in team_df.columns]
    st.dataframe(team_df, hide_index=True, use_container_width=True)


def render_player_stats_tab(match: pd.Series):
    view = st.selectbox("Show", ["Players", "Goalkeepers"], width=200)

    match_id = int(match["match_id"])
    home_id = int(match["home_team_id"])
    away_id = int(match["away_team_id"])

    if view == "Players":
        df = get_player_match_performance(match_id)
        columns, sort_by = PLAYER_COLUMNS, "jersey_number"
    else:
        df = get_goalkeeper_match_performance(match_id)
        columns, sort_by = GOALKEEPER_COLUMNS, None

    if df.empty:
        st.caption(f"{view} stats aren't available for this match yet.")
        return

    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"<div class='formation-label'>{match['home_team_name']}</div>", unsafe_allow_html=True)
        _render_team_table(df, home_id, columns, sort_by)
    with c2:
        st.markdown(f"<div class='formation-label'>{match['away_team_name']}</div>", unsafe_allow_html=True)
        _render_team_table(df, away_id, columns, sort_by)


def render_stats_tab(match: pd.Series):
    tab_teams, tab_players = st.tabs(["Teams", "Players"])
    with tab_teams:
        render_team_stats_tab(match)
    with tab_players:
        render_player_stats_tab(match)