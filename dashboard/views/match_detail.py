import pandas as pd
import streamlit as st

from components.ui import render_header, render_score_header, render_goals_section, render_invalid_link
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
from utils import parse_int

BACK_PAGE, BACK_LABEL = "views/home_matches.py", "Back to matches"

raw_match_id = st.query_params.get("match_id")

render_header("Match Detail")

if not raw_match_id:
    render_invalid_link("No match selected.", BACK_PAGE, BACK_LABEL)

match_id = parse_int(raw_match_id)
if match_id is None:
    render_invalid_link("Invalid match link.", BACK_PAGE, BACK_LABEL)

with st.spinner("Loading match..."):
    match = get_match(match_id)

if match is None:
    render_invalid_link("Match not found.", BACK_PAGE, BACK_LABEL)

season_id = parse_int(st.query_params.get("season_id"))
if season_id is None and pd.notna(match.get("season_id")):
    season_id = int(match["season_id"])

st.page_link(BACK_PAGE, label=BACK_LABEL, icon=":material/arrow_back:")

render_score_header(match, season_id=season_id)

with st.spinner("Loading goals..."):
    goals_df = get_match_goals(match_id)
render_goals_section(match, goals_df)

tab_lineups, tab_events, tab_stats = st.tabs(["Lineups", "Events", "Stats"])

with tab_lineups:
    with st.spinner("Loading lineups..."):
        lineups_df = get_match_lineups(match_id)
    render_lineups_tab(match, lineups_df)

with tab_events:
    with st.spinner("Loading events..."):
        cards_df = get_match_cards(match_id)
        subs_df = get_match_subs(match_id)
    render_events_tab(match, goals_df, cards_df, subs_df)

with tab_stats:
    render_stats_tab(match)
