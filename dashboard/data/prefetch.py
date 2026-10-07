"""Load a page's independent data at the same time.

Pages are latency-bound: each query is a chain of small S3 requests (the
Delta log, then each data file), and the app runs in the US while the bucket
is in ap-south-1. Streamlit runs a page top to bottom, so a cold match page
used to wait for about ten queries one after another.

prefetch() runs the cached loaders a page is about to call in parallel
threads; when the page then calls them in its usual order they're cache
hits. Errors are swallowed here: the page's own call raises them again,
inside its normal error handling.
"""
import logging
import threading
from concurrent.futures import ThreadPoolExecutor

import streamlit as st
from streamlit.runtime.scriptrunner import add_script_run_ctx, get_script_run_ctx

from data.db import BATCH_TTL, get_connection

log = logging.getLogger(__name__)
_pool = ThreadPoolExecutor(max_workers=8, thread_name_prefix="prefetch")


def _run(ctx, fn, args):
    add_script_run_ctx(threading.current_thread(), ctx)
    try:
        fn(*args)
    except Exception as e:
        log.debug("prefetch of %s failed: %s", getattr(fn, "__name__", fn), e)


def prefetch(*calls, wait: bool = True):
    """Run (fn, *args) calls in parallel. With wait=False it returns at once."""
    try:
        get_connection()      # connect (and show its spinner) on the page's own thread
    except Exception:
        return                # the page's own calls will show the error
    ctx = get_script_run_ctx()
    futures = [_pool.submit(_run, ctx, call[0], call[1:]) for call in calls]
    if wait:
        for future in futures:
            future.result()


@st.cache_resource(ttl=BATCH_TTL, show_spinner=False)
def warm_cache():
    """Once per server (and again after BATCH_TTL), load what most visits
    start with in the background: the latest season's first match page,
    standings and clubs, and the live-feed map behind the match badges."""
    from config import MATCHES_PER_PAGE
    from data.live import get_live_match_map
    from data.queries import get_matches, get_matches_count, get_seasons, get_standings, get_teams_by_season

    def warm():
        try:
            seasons = get_seasons()
            if seasons.empty:
                return
            season_id = int(seasons["season_id"].iloc[0])
            prefetch((get_matches_count, season_id), (get_matches, season_id, 1, MATCHES_PER_PAGE),
                     (get_standings, season_id, "TOTAL"), (get_teams_by_season, season_id),
                     (get_live_match_map,))
        except Exception as e:
            log.debug("cache warm-up failed: %s", e)

    thread = threading.Thread(target=warm, name="warm-cache", daemon=True)
    add_script_run_ctx(thread, get_script_run_ctx())
    thread.start()
    return True
