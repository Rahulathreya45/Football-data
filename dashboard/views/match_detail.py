import streamlit as st

from components.ui import render_header

render_header("Match Detail")

match_id = st.query_params.get("match_id")
season_id = st.query_params.get("season_id")

if not match_id:
    st.warning("No match selected.")
    st.page_link("views/home_matches.py", label="← Back to Matches")
    st.stop()

st.page_link("views/home_matches.py", label="← Back to Matches")
st.title(f"Match #{match_id}")

st.info(
    "Score header, goal/card/sub timeline, and team + player stat tabs land "
    "here next, once we confirm the fact_goals / fact_card / fact_subs and "
    "team_match_* / player_match_summary column names."
)