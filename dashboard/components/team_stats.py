import pandas as pd
import streamlit as st

from utils import humanize_column
from data.queries import get_team_season_stats, get_team_players_season_stats

# (label, column, format) per section. "no charts" - just st.metric grids.
STANDARD_STATS = [
    ("Players Used", "standard_players_used", "{:.0f}"),
    ("Avg Age", "standard_avg_age", "{:.1f}"),
    ("Possession %", "standard_possession_pct", "{:.1f}%"),
    ("Goals", "standard_goals", "{:.0f}"),
    ("Assists", "standard_assists", "{:.0f}"),
    ("G+A", "standard_goals_plus_assists", "{:.0f}"),
    ("Non-Penalty Goals", "standard_non_penalty_goals", "{:.0f}"),
    ("Penalty Goals", "standard_penalty_goals", "{:.0f}"),
    ("Penalty Attempts", "standard_penalty_attempts", "{:.0f}"),
    ("Yellow Cards", "standard_yellow_cards", "{:.0f}"),
    ("Red Cards", "standard_red_cards", "{:.0f}"),
    ("Goals/90", "standard_goals_per90", "{:.2f}"),
    ("Assists/90", "standard_assists_per90", "{:.2f}"),
    ("G+A/90", "standard_goals_plus_assists_per90", "{:.2f}"),
    ("NPG/90", "standard_non_penalty_goals_per90", "{:.2f}"),
    ("NPG+A/90", "standard_non_penalty_goals_plus_assists_per90", "{:.2f}"),
]

SHOOTING_STATS = [
    ("Players Used", "shooting_players_used", "{:.0f}"),
    ("Goals", "shooting_goals", "{:.0f}"),
    ("Shots", "shooting_shots", "{:.0f}"),
    ("Shots on Target", "shooting_shots_on_target", "{:.0f}"),
    ("Shots on Target %", "shooting_shots_on_target_pct", "{:.1f}%"),
    ("Shots/90", "shooting_shots_per90", "{:.2f}"),
    ("SoT/90", "shooting_shots_on_target_per90", "{:.2f}"),
    ("Goals/Shot", "shooting_goals_per_shot", "{:.2f}"),
    ("Goals/SoT", "shooting_goals_per_shot_on_target", "{:.2f}"),
    ("Penalty Goals", "shooting_penalty_goals", "{:.0f}"),
    ("Penalty Attempts", "shooting_penalty_attempts", "{:.0f}"),
]

GOALKEEPING_STATS = [
    ("Players Used", "gk_players_used", "{:.0f}"),
    ("Shots on Target Against", "gk_shots_on_target_against", "{:.0f}"),
    ("Saves", "gk_saves", "{:.0f}"),
    ("Save %", "gk_save_pct", "{:.1f}%"),
    ("Wins", "gk_wins", "{:.0f}"),
    ("Draws", "gk_draws", "{:.0f}"),
    ("Losses", "gk_losses", "{:.0f}"),
    ("Clean Sheets", "gk_clean_sheets", "{:.0f}"),
    ("Clean Sheet %", "gk_clean_sheet_pct", "{:.1f}%"),
    ("Penalties Faced", "gk_penalty_kicks_faced", "{:.0f}"),
    ("Penalties Allowed", "gk_penalty_kicks_allowed", "{:.0f}"),
    ("Penalties Saved", "gk_penalty_kicks_saved", "{:.0f}"),
    ("Penalties Missed", "gk_penalty_kicks_missed", "{:.0f}"),
    ("Penalty Save %", "gk_penalty_save_pct", "{:.1f}%"),
]

DISCIPLINE_STATS = [
    ("Second Yellows", "misc_second_yellow_cards", "{:.0f}"),
    ("Fouls Committed", "misc_fouls_committed", "{:.0f}"),
    ("Fouls Drawn", "misc_fouls_drawn", "{:.0f}"),
    ("Offsides", "misc_offsides", "{:.0f}"),
    ("Crosses", "misc_crosses", "{:.0f}"),
    ("Interceptions", "misc_interceptions", "{:.0f}"),
    ("Tackles Won", "misc_tackles_won", "{:.0f}"),
    ("Own Goals", "misc_own_goals", "{:.0f}"),
]

PLAYING_TIME_STATS = [
    ("Avg Min/Start", "pt_avg_minutes_per_start", "{:.1f}"),
    ("Complete Matches", "pt_complete_matches", "{:.0f}"),
    ("Sub Appearances", "pt_sub_appearances", "{:.0f}"),
    ("Avg Min/Sub", "pt_avg_minutes_per_sub", "{:.1f}"),
    ("Unused Sub Appearances", "pt_unused_sub_appearances", "{:.0f}"),
    ("Points/Match", "pt_points_per_match", "{:.2f}"),
    ("Goals Scored On Pitch", "pt_goals_scored_on_pitch", "{:.0f}"),
    ("Goals Conceded On Pitch", "pt_goals_conceded_on_pitch", "{:.0f}"),
    ("+/-", "pt_plus_minus", "{:.0f}"),
    ("+/- per90", "pt_plus_minus_per90", "{:.2f}"),
]

PLAYER_SEASON_COLUMNS = [
    "player_name", "position",
    "standard_matches_played", "standard_starts", "standard_minutes_played",
    "standard_goals", "standard_assists", "standard_goals_plus_assists",
    "standard_non_penalty_goals", "standard_penalty_goals", "standard_penalty_attempts",
    "standard_yellow_cards", "standard_red_cards",
    "standard_goals_per90", "standard_assists_per90",
    "shooting_total_shots", "shooting_shots_on_target", "shooting_shots_on_target_pct",
    "shooting_goals_per_shot", "shooting_goals_per_shot_on_target",
    "misc_fouls_committed", "misc_fouls_drawn", "misc_offsides",
    "misc_crosses", "misc_interceptions", "misc_tackles_won", "misc_own_goals",
]

GOALKEEPER_SEASON_COLUMNS = [
    "player_name",
    "standard_matches_played", "standard_minutes_played",
    "gk_goals_against", "gk_goals_against_per90",
    "gk_shots_on_target_against", "gk_saves", "gk_save_pct",
    "gk_wins", "gk_draws", "gk_losses",
    "gk_clean_sheets", "gk_clean_sheet_pct",
    "gk_penalty_kicks_faced", "gk_penalty_kicks_allowed",
    "gk_penalty_kicks_saved", "gk_penalty_kicks_missed", "gk_penalty_save_pct",
]


def _fmt(val, fmt: str) -> str:
    if pd.isna(val):
        return "-"
    return fmt.format(val)


def _render_metric_section(title: str, stats: list, row: pd.Series, per_row: int = 4):
    st.markdown(f"<div class='section-header'>{title}</div>", unsafe_allow_html=True)
    for i in range(0, len(stats), per_row):
        chunk = stats[i:i + per_row]
        cols = st.columns(len(chunk))
        for col, (label, col_name, fmt) in zip(cols, chunk):
            with col:
                st.metric(label, _fmt(row.get(col_name), fmt))


def render_team_season_stats_tab(team_id: int, season_id: int):
    row = get_team_season_stats(team_id, season_id)
    if row is None:
        st.caption("Team stats aren't available for this season yet.")
        return

    _render_metric_section("Standard", STANDARD_STATS, row)
    _render_metric_section("Shooting", SHOOTING_STATS, row)
    _render_metric_section("Goalkeeping", GOALKEEPING_STATS, row)
    _render_metric_section("Discipline", DISCIPLINE_STATS, row)
    _render_metric_section("Playing Time", PLAYING_TIME_STATS, row)


def render_team_players_season_tab(team_id: int, season_id: int):
    df = get_team_players_season_stats(team_id, season_id)
    if df.empty:
        st.caption("Player stats aren't available for this season yet.")
        return

    view = st.selectbox("Show", ["Players", "Goalkeepers"], width=200, key="team_players_season_view")

    is_gk = df["position"].fillna("").str.upper().str.contains("GK")
    if view == "Goalkeepers":
        filtered, columns = df[is_gk], GOALKEEPER_SEASON_COLUMNS
    else:
        filtered, columns = df[~is_gk], PLAYER_SEASON_COLUMNS

    if filtered.empty:
        st.caption(f"No {view.lower()} found.")
        return

    display_df = filtered[columns].copy()
    display_df.columns = [humanize_column(c) for c in display_df.columns]
    st.dataframe(display_df, hide_index=True, use_container_width=True)