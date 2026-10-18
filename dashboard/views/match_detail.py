import pandas as pd
import streamlit as st

from components.ui import render_header, render_score_header, render_goals_section, render_invalid_link
from components.lineups import render_lineups_tab
from components.events import render_events_tab
from components.stats import render_stats_tab
from components.live import render_live_tab
from components.match_story import render_story_button
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
from data.live import (
    awaits_batch, feed_score, find_live_match_id, get_live_match_data, get_live_match_map, is_in_play,
)
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

LIVE_REFRESH_SECONDS = 30

# The Live tab / live view only appears for matches whose live feed was
# recorded. If DynamoDB can't be reached we can't tell, so show it with the
# error rather than fail the whole page.
live_match_id, live_error = None, None
try:
    with st.spinner("Checking for a live feed..."):
        live_match_id = find_live_match_id(match_id)
except DataSourceError as e:
    live_error = e
in_play = is_in_play(match["match_date"], match.get("full_time_home_team_score"))
# Past the in-play window but the batch result isn't in: the feed is all we
# have, so the page stays live-only (without refreshing) until it arrives.
feed_only = (not in_play and live_match_id is not None
             and awaits_batch(match["match_date"], match.get("full_time_home_team_score")))


def _load_flow(live_id):
    """History for Match flow / Leaderboard / halves (S3); if it can't be read,
    only those parts of the tab show an error."""
    try:
        with st.spinner("Loading match history..."):
            return get_match_flow(live_id, match["match_date"]), None
    except DataSourceError as e:
        return None, e


def _load_live():
    """(live feed id, DynamoDB state, error). While in play the feed id is
    looked up again on each refresh, so a feed that starts after the page
    opened is picked up."""
    live_id, error = live_match_id, live_error
    if live_id is None and error is None and in_play:
        try:
            live_id = find_live_match_id(match_id)
        except DataSourceError as e:
            error = e
    if live_id is None or error is not None:
        return live_id, None, error
    try:
        with st.spinner("Loading live feed..."):
            prefetch((get_live_match_data, live_id), *history_loaders(live_id))
            return live_id, get_live_match_data(live_id), None
    except DataSourceError as e:
        return live_id, None, e


def _render_live_view(live_id, live, error):
    if live_id is None and error is None:
        st.info("Waiting for the live feed. This page updates by itself once the match data "
                "starts arriving.", icon=":material/sensors:")
        return
    if live is None:
        st.warning(
            "Couldn't load the live feed right now. The live data store may be "
            "unreachable - please try again in a moment.",
            icon=":material/cloud_off:",
        )
        with st.expander("Error details"):
            st.exception(error)
        return
    flow, flow_error = _load_flow(live_id)
    # In play, the story button lives outside the refreshing fragment, so a
    # refresh doesn't close an open story or regenerate it every 30 s.
    render_live_tab(match, live_id, live, flow, flow_error, show_story=not in_play)


def _live_page():
    """Live state: the feed's score in the header and only the live view (the
    batch tabs and goals fill in after the match). Runs as a fragment every
    LIVE_REFRESH_SECONDS; DynamoDB state is cached 15 s, the S3 history 2 min."""
    live_id, live, error = _load_live()
    score = feed_score(live["goals"]) if live is not None else None
    render_score_header(match, season_id=season_id, live_score=score, live_now=in_play)
    _render_live_view(live_id, live, error)


if in_play:
    with st.container(horizontal=True, vertical_alignment="center", horizontal_alignment="distribute"):
        st.caption(f":red-badge[:material/sensors: Live] Updates every {LIVE_REFRESH_SECONDS} seconds")
        if live_match_id is not None:
            render_story_button(match, live_match_id, _load_flow(live_match_id)[0])
    st.fragment(run_every=LIVE_REFRESH_SECONDS)(_live_page)()
    st.stop()
if feed_only:
    _live_page()
    st.stop()

render_score_header(match, season_id=season_id)

with st.spinner("Loading goals..."):
    goals_df = get_match_goals(match_id)
render_goals_section(match, goals_df)

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
        _render_live_view(*_load_live())
