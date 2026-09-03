import streamlit as st

from components.ui import render_header

render_header("Team")

team_id = st.query_params.get("team_id")
season_id = st.query_params.get("season_id")

if not team_id:
    st.warning("No team selected.")
    st.page_link("views/home_matches.py", label="← Back to Matches")
    st.stop()

st.page_link("views/home_matches.py", label="← Back to Matches")
st.title(f"Team #{team_id}")

st.info(
    "Team season stats / player season stats / fixtures tabs land here next, "
    "once we're on to the team_season_* and player_season_* tables."
)