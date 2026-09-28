import streamlit as st

from components.ui import render_header, render_pagination, render_match_card
from data.queries import get_seasons, get_matches, get_matches_count
from data.live import recorded_match_ids
from config import MATCHES_PER_PAGE
from utils import parse_int

with st.spinner("Loading seasons..."):
    seasons_df = get_seasons()
query_season = st.query_params.get("season_id")

selected_season_id = render_header("Premier League", seasons_df=seasons_df, selected_season_id=query_season)

if seasons_df.empty:
    st.info("No season data available yet.")
    st.stop()

with st.spinner("Loading matches..."):
    page = max(1, parse_int(st.query_params.get("page"), 1))
    total_matches = get_matches_count(selected_season_id)
    total_pages = max(1, -(-total_matches // MATCHES_PER_PAGE))  # ceil division
    page = min(page, total_pages)

    matches_df = get_matches(selected_season_id, page=page, page_size=MATCHES_PER_PAGE)
    live_ids = recorded_match_ids()

st.caption(f"{total_matches} matches this season")

if matches_df.empty:
    st.caption("No matches found for this season.")

for _, row in matches_df.iterrows():
    render_match_card(row, season_id=selected_season_id, has_live=row["match_id"] in live_ids)

render_pagination(page, total_pages)
