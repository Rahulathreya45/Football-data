import pandas as pd
import streamlit as st

from components.ui import render_header, render_pagination, render_match_card
from data.db import DataSourceError
from data.queries import get_seasons, get_matches, get_matches_count, get_season_schedule
from data.live import (
    awaits_batch, feed_score, find_live_match_id, get_live_match_data, get_live_match_map, is_in_play,
    recorded_match_ids,
)
from data.prefetch import prefetch
from config import MATCHES_PER_PAGE
from utils import parse_int

LIVE_REFRESH_SECONDS = 30


def landing_page(season_id: int, live_ids: set[int]) -> int:
    """With no page in the URL, open on the page holding a match in play
    with a live feed, or else the most recent match played (by the batch
    result or, until that arrives, by its live feed)."""
    schedule = get_season_schedule(season_id)
    if schedule.empty:
        return 1
    rows = list(schedule.itertuples(index=False))
    live = [i for i, r in enumerate(rows)
            if r.match_id in live_ids and is_in_play(r.match_date, r.full_time_home_team_score)]
    played = [i for i, r in enumerate(rows) if pd.notna(r.full_time_home_team_score)
              or (r.match_id in live_ids and awaits_batch(r.match_date, r.full_time_home_team_score))]
    index = live[0] if live else (played[-1] if played else 0)
    return index // MATCHES_PER_PAGE + 1


def live_scores(matches_df, live_ids: set[int]) -> dict[int, tuple[int, int]]:
    """Feed score for every listed match with a feed whose batch result
    isn't in yet (best effort)."""
    scores = {}
    for row in matches_df.itertuples(index=False):
        if row.match_id in live_ids and awaits_batch(row.match_date, row.full_time_home_team_score):
            try:
                live_id = find_live_match_id(row.match_id)
                if live_id is not None:
                    scores[row.match_id] = feed_score(get_live_match_data(live_id)["goals"])
            except DataSourceError:
                pass
    return scores


with st.spinner("Loading seasons..."):
    seasons_df = get_seasons()
query_season = st.query_params.get("season_id")

selected_season_id = render_header("Premier League", seasons_df=seasons_df, selected_season_id=query_season)

if seasons_df.empty:
    st.info("No season data available yet.")
    st.stop()

with st.spinner("Loading matches..."):
    prefetch((get_matches_count, selected_season_id), (get_season_schedule, selected_season_id),
             (get_live_match_map,))
    total_matches = get_matches_count(selected_season_id)
    total_pages = max(1, -(-total_matches // MATCHES_PER_PAGE))  # ceil division

    url_page = parse_int(st.query_params.get("page"))
    page = max(1, url_page) if url_page is not None else landing_page(selected_season_id, recorded_match_ids())
    page = min(page, total_pages)

    matches_df = get_matches(selected_season_id, page=page, page_size=MATCHES_PER_PAGE)

st.caption(f"{total_matches} matches this season")

if matches_df.empty:
    st.caption("No matches found for this season.")


def match_cards():
    live_ids = recorded_match_ids()
    scores = live_scores(matches_df, live_ids)
    for _, row in matches_df.iterrows():
        render_match_card(row, season_id=selected_season_id, has_live=row["match_id"] in live_ids,
                          live_score=scores.get(row["match_id"]),
                          live_now=is_in_play(row["match_date"], row["full_time_home_team_score"]))


# While any listed match is in play, only the cards refresh themselves, so live
# scores update and a match picks up its live state once its feed arrives.
if any(is_in_play(r.match_date, r.full_time_home_team_score) for r in matches_df.itertuples(index=False)):
    st.fragment(run_every=LIVE_REFRESH_SECONDS)(match_cards)()
else:
    match_cards()

render_pagination(page, total_pages)
