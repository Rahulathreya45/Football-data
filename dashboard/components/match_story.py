import logging

import pandas as pd
import streamlit as st

from data.db import DataSourceError
from data.match_story import StoryError, build_story_facts, facts_to_json, generate_story, story_coverage
from data.queries import get_live_incidents_history

log = logging.getLogger(__name__)

# Section titles per coverage status, in reading order: after full time the
# whole match comes first, mid-match it's the first half then the rest.
_SECTIONS = {
    "full_time": [("The match", "overview"), ("First half", "first_half"), ("Second half", "second_half")],
    "second_half": [("", "overview"), ("Up to half-time", "first_half"), ("Since the break", "second_half")],
    "half_time": [("", "overview"), ("First half", "first_half")],
    "first_half": [("", "overview"), ("So far", "first_half")],
}


def _render_story(story: dict, coverage: dict, facts: dict):
    st.markdown(f"#### {story['headline']}")
    until = "Full time" if coverage["status"] == "full_time" else f"Up to {coverage['label']}"
    st.caption(f"{until} · Written by Gemini from the recorded live feed. It can make mistakes.")

    for title, field in _SECTIONS[coverage["status"]]:
        text = story.get(field, "").strip()
        if not text:
            continue
        if title:
            st.markdown(f"**{title}**")
        st.markdown(text.replace("$", r"\$"))

    with st.expander("Facts the story was written from"):
        st.json(facts, expanded=1)


@st.dialog("Match story", width="large", icon=":material/auto_stories:")
def _story_dialog(match: pd.Series, live_match_id: int, flow: dict, coverage: dict):
    try:
        with st.spinner("Writing the match story..."):
            incidents = get_live_incidents_history(live_match_id)
            facts = build_story_facts(match, flow, incidents, coverage)
            story = generate_story(facts_to_json(facts))
    except DataSourceError:
        st.warning("Couldn't load the match history right now. Please try again in a moment.",
                   icon=":material/cloud_off:")
        return
    except StoryError as e:
        st.warning(str(e), icon=":material/auto_stories:")
        return
    except Exception:
        log.exception("Match story failed for live match %s", live_match_id)
        st.warning("Something went wrong while writing the story. Please try again later.",
                   icon=":material/error:")
        return
    _render_story(story, coverage, facts)


def render_story_button(match: pd.Series, live_match_id: int, flow: dict | None):
    """The "Match story" button; hidden until the recorded history reaches
    STORY_MIN_MINUTE (or when the history couldn't be loaded)."""
    coverage = story_coverage(flow, match)
    if coverage is None:
        return
    if st.button("Match story", icon=":material/auto_stories:", key="match_story_open"):
        _story_dialog(match, live_match_id, flow, coverage)
