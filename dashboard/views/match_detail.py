import streamlit as st

from components.ui import render_header, render_score_header, render_goals_section
from components.lineups import render_lineups_tab
from components.events import render_events_tab
from components.stats import render_stats_tab
from data.queries import (
    get_match,
    get_match_goals,
    get_match_lineups,
    get_match_cards,
    get_match_subs,
)

raw_match_id = st.query_params.get("match_id")

render_header("Match Detail")

if not raw_match_id:
    st.warning("No match selected.")
    st.page_link("views/home_matches.py", label="← Back to Matches")
    st.stop()

match_id = int(raw_match_id)
match = get_match(match_id)

if match is None:
    st.error("Match not found.")
    st.page_link("views/home_matches.py", label="← Back to Matches")
    st.stop()

st.page_link("views/home_matches.py", label="← Back to Matches")

render_score_header(match)

goals_df = get_match_goals(match_id)
render_goals_section(match, goals_df)

tab_lineups, tab_events, tab_stats = st.tabs(["Lineups", "Events", "Stats"])

with tab_lineups:
    lineups_df = get_match_lineups(match_id)
    render_lineups_tab(match, lineups_df)

with tab_events:
    cards_df = get_match_cards(match_id)
    subs_df = get_match_subs(match_id)
    render_events_tab(match, goals_df, cards_df, subs_df)

with tab_stats:
    render_stats_tab(match)