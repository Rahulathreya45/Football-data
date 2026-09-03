import streamlit as st

from components.styling import load_css

st.set_page_config(
    page_title="Premier League Analytics",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed",
)

load_css()

matches_page = st.Page("views/home_matches.py", title="Matches", icon="⚽", default=True)
match_detail_page = st.Page("views/match_detail.py", title="Match Detail", icon="📋")
team_page = st.Page("views/team.py", title="Team", icon="🏟️")
standings_page = st.Page("views/standings.py", title="Standings", icon="🏆")

pg = st.navigation(
    [matches_page, standings_page, match_detail_page, team_page],
    position="hidden",
)

pg.run()