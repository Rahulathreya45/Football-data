import streamlit as st

from components.ui import render_header, render_team_grid_card
from data.queries import get_seasons, get_teams_by_season

seasons_df = get_seasons()
query_season = st.query_params.get("season_id")

selected_season_id = render_header("Teams", seasons_df=seasons_df, selected_season_id=query_season)
st.query_params["season_id"] = str(selected_season_id)

teams_df = get_teams_by_season(int(selected_season_id))

if teams_df.empty:
    st.caption("No teams found for this season.")
else:
    teams = list(teams_df.iterrows())
    for i in range(0, len(teams), 5):
        chunk = teams[i:i + 5]
        cols = st.columns(5)
        for col, (_, trow) in zip(cols, chunk):
            with col:
                render_team_grid_card(trow, selected_season_id)