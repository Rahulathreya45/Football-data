import pandas as pd
import streamlit as st

from components.ui import render_header, render_score_header, render_goals_section, render_invalid_link
from components.lineups import render_lineups_tab
from components.events import render_events_tab
from components.stats import render_stats_tab
from components.live import render_live_tab
from data.queries import (
    get_match,
    get_match_goals,
    get_match_lineups,
    get_match_cards,
    get_match_subs,
    get_player_match_performance,
    get_team_match_performance,
)
from data.db import DataSourceError
from data.live import find_live_match_id, get_live_match_data, get_live_match_map
from data.live_history import get_match_flow, history_loaders
from data.prefetch import prefetch
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
    # Everything below except the live feed depends only on match_id, so load
    # it all at once instead of tab by tab (data/prefetch.py).
    prefetch(
        (get_match, match_id), (get_match_goals, match_id), (get_match_lineups, match_id),
        (get_match_cards, match_id), (get_match_subs, match_id),
        (get_team_match_performance, match_id), (get_player_match_performance, match_id),
        (get_live_match_map,),
    )
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

# The Live tab only appears for matches whose live feed was recorded. If
# DynamoDB can't be reached we can't tell, so show the tab with the error
# rather than fail the whole page.
live_match_id, live_error = None, None
try:
    with st.spinner("Checking for a live feed..."):
        live_match_id = find_live_match_id(match_id)
except DataSourceError as e:
    live_error = e
show_live = live_match_id is not None or live_error is not None

tab_labels = ["Lineups", "Events", "Stats"] + (["Live"] if show_live else [])
tab_lineups, tab_events, tab_stats, *tab_live = st.tabs(tab_labels)

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

if show_live:
    with tab_live[0]:
        live = None
        if live_error is None:
            try:
                with st.spinner("Loading live feed..."):
                    prefetch((get_live_match_data, live_match_id), *history_loaders(live_match_id))
                    live = get_live_match_data(live_match_id)
            except DataSourceError as e:
                live_error = e
        if live is not None:
            # History for Match flow / Leaderboard / halves lives in S3; if it
            # can't be read, only those parts of the tab show an error.
            flow, flow_error = None, None
            try:
                with st.spinner("Loading match history..."):
                    flow = get_match_flow(live_match_id, match["match_date"])
            except DataSourceError as e:
                flow_error = e
            render_live_tab(match, live_match_id, live, flow, flow_error)
        else:
            st.warning(
                "Couldn't load the live feed right now. The live data store may be "
                "unreachable - please try again in a moment.",
                icon=":material/cloud_off:",
            )
            with st.expander("Error details"):
                st.exception(live_error)
