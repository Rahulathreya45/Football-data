import logging

import streamlit as st

from components.styling import load_css, fix_history_navigation
from components.ui import render_error
from data.prefetch import warm_cache

st.set_page_config(
    page_title="Premier League Analytics",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed",
)

load_css()
fix_history_navigation()

matches_page = st.Page("views/home_matches.py", title="Matches", icon="⚽", default=True)
match_detail_page = st.Page("views/match_detail.py", title="Match Detail", icon="📋")
teams_list_page = st.Page("views/teams_list.py", title="Teams", icon="🏟️")
team_page = st.Page("views/team.py", title="Team", icon="🏟️")
standings_page = st.Page("views/standings.py", title="Standings", icon="🏆")

pg = st.navigation(
    [matches_page, standings_page, match_detail_page, teams_list_page, team_page],
    position="hidden",
)

# Start loading the most common data in the background on the first visit.
try:
    warm_cache()
except Exception:
    logging.getLogger(__name__).exception("Cache warm-up failed to start")

# Error boundary for every page. st.stop / st.switch_page / st.rerun raise
# Streamlit control-flow exceptions that subclass BaseException, so they
# pass through untouched.
try:
    pg.run()
except Exception as e:
    logging.getLogger(__name__).exception("Page %s failed", pg.title)
    render_error(e)