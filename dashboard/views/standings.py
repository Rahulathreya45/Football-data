import streamlit as st

from components.ui import render_header
from data.queries import get_seasons, get_standings

seasons_df = get_seasons()
query_season = st.query_params.get("season_id")

selected_season_id = render_header("Standings", seasons_df=seasons_df, selected_season_id=query_season)
st.query_params["season_id"] = str(selected_season_id)

table_type = st.selectbox("Split", ["TOTAL", "HOME", "AWAY"], width=200)

standings_df = get_standings(int(selected_season_id), table_type)

COL_WIDTHS = [0.5, 0.5, 3, 0.6, 0.6, 0.6, 0.6, 0.7, 0.7, 0.7, 0.7]


def _cell(col, value, bold=False):
    with col:
        text = f"<b>{value}</b>" if bold else str(value)
        st.markdown(
            f"<div style='text-align:center;padding-top:8px;'>{text}</div>",
            unsafe_allow_html=True,
        )


if standings_df.empty:
    st.caption("No standings available for this season yet.")
else:
    header_cols = st.columns(COL_WIDTHS)
    for col, label in zip(
        header_cols, ["#", "", "Team", "P", "W", "D", "L", "GF", "GA", "GD", "Pts"]
    ):
        with col:
            st.markdown(
                f"<div style='text-align:center;color:var(--text-muted);font-size:0.78rem;"
                f"font-weight:700;'>{label}</div>",
                unsafe_allow_html=True,
            )
    st.markdown("<hr class='navbar-divider'>", unsafe_allow_html=True)

    for _, row in standings_df.iterrows():
        cols = st.columns(COL_WIDTHS)
        _cell(cols[0], int(row["position"]))
        with cols[1]:
            if row.get("team_crest"):
                st.markdown(
                    f"<img src='{row['team_crest']}' style='width:22px;height:22px;"
                    f"object-fit:contain;margin-top:6px;'>",
                    unsafe_allow_html=True,
                )
        with cols[2]:
            key = f"standings_{row['team_id']}_{selected_season_id}_{table_type}"
            if st.button(row["team_name"], key=key, type="tertiary"):
                st.switch_page(
                    "views/team.py",
                    query_params={"team_id": str(row["team_id"]), "season_id": str(selected_season_id)},
                )
        _cell(cols[3], int(row["played_games"]))
        _cell(cols[4], int(row["won"]))
        _cell(cols[5], int(row["draw"]))
        _cell(cols[6], int(row["lost"]))
        _cell(cols[7], int(row["goals_for"]))
        _cell(cols[8], int(row["goals_against"]))
        _cell(cols[9], int(row["goal_difference"]))
        _cell(cols[10], int(row["points"]), bold=True)