import streamlit as st

from components.ui import render_header, render_match_card, render_pagination, render_invalid_link
from components.team_stats import render_team_season_stats_tab, render_team_players_season_tab
from data.queries import get_team, get_seasons, get_team_matches, get_team_matches_count
from data.live import recorded_match_ids
from config import MATCHES_PER_PAGE
from utils import parse_int

BACK_PAGE, BACK_LABEL = "views/teams_list.py", "Back to teams"

render_header("Team")

raw_team_id = st.query_params.get("team_id")

if not raw_team_id:
    render_invalid_link("No team selected.", BACK_PAGE, BACK_LABEL)

team_id = parse_int(raw_team_id)
if team_id is None:
    render_invalid_link("Invalid team link.", BACK_PAGE, BACK_LABEL)

with st.spinner("Loading team..."):
    team = get_team(team_id)

    season_id = parse_int(st.query_params.get("season_id"))
    if season_id is None:
        seasons_df = get_seasons()
        season_id = int(seasons_df["season_id"].iloc[0]) if not seasons_df.empty else None

if team is None:
    render_invalid_link("Team not found.", BACK_PAGE, BACK_LABEL)

st.page_link(BACK_PAGE, label=BACK_LABEL, icon=":material/arrow_back:")

with st.container(border=True):
    st.markdown(
        "<div style='text-align:center;'>"
        f"<img src='{team.get('team_crest', '')}' style='width:64px;height:64px;object-fit:contain;'>"
        f"<div style='font-size:1.4rem;font-weight:800;margin-top:10px;'>"
        f"{team['team_name']} · {team.get('team_tla', '')}</div>"
        f"<div class='match-meta' style='margin-top:4px;'>🏟️ {team.get('team_venue', '-')}</div>"
        "</div>",
        unsafe_allow_html=True,
    )

tab_matches, tab_team_stats, tab_player_stats = st.tabs(["Matches", "Team Stats", "Players Stats"])

with tab_matches:
    if season_id is None:
        st.caption("No season data available.")
    else:
        with st.spinner("Loading matches..."):
            page = max(1, parse_int(st.query_params.get("page"), 1))
            total = get_team_matches_count(team_id, season_id)
            total_pages = max(1, -(-total // MATCHES_PER_PAGE))
            page = min(page, total_pages)

            matches_df = get_team_matches(team_id, season_id, page=page, page_size=MATCHES_PER_PAGE)
            live_ids = recorded_match_ids()
        st.caption(f"{total} matches this season")
        for _, row in matches_df.iterrows():
            render_match_card(row, season_id=season_id, has_live=row["match_id"] in live_ids)
        render_pagination(page, total_pages)

with tab_team_stats:
    if season_id is None:
        st.caption("No season data available.")
    else:
        render_team_season_stats_tab(team_id, season_id)

with tab_player_stats:
    if season_id is None:
        st.caption("No season data available.")
    else:
        render_team_players_season_tab(team_id, season_id)
