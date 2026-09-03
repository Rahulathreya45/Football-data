import streamlit as st

from components.ui import render_header, render_pagination, render_match_card
from data.queries import get_seasons, get_matches, get_matches_count
from config import MATCHES_PER_PAGE

seasons_df = get_seasons()
query_season = st.query_params.get("season_id")

selected_season_id = render_header("Premier League", seasons_df=seasons_df, selected_season_id=query_season)
st.query_params["season_id"] = str(selected_season_id)

page = int(st.query_params.get("page", 1))
total_matches = get_matches_count(selected_season_id)
total_pages = max(1, -(-total_matches // MATCHES_PER_PAGE))  # ceil division
page = min(page, total_pages)

matches_df = get_matches(selected_season_id, page=page, page_size=MATCHES_PER_PAGE)

st.caption(f"{total_matches} matches this season")

for _, row in matches_df.iterrows():
    render_match_card(row, season_id=selected_season_id)

render_pagination(page, total_pages)