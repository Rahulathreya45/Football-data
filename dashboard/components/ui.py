import pandas as pd
import streamlit as st


def render_header(title: str, seasons_df: pd.DataFrame = None, selected_season_id=None):
    """Single header row: title (+ optional season dropdown) on the left,
    nav links pinned to the right. Pass seasons_df only on pages that need
    the season picker (currently just the Matches/home page).

    Returns the selected season_id if seasons_df was passed, else None.
    """
    c_title, c_dropdown, c_spacer, c_nav1, c_nav2 = st.columns([2, 2, 4, 1, 1])

    new_season_id = selected_season_id

    with c_title:
        st.markdown(
            f"""
            <div class="page-title">
                <span class="page-title-icon">⚽</span>
                <span>{title}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c_dropdown:
        if seasons_df is not None:
            options = dict(zip(seasons_df["season_name"], seasons_df["season_id"]))
            names = list(options.keys())
            default_index = 0
            if selected_season_id:
                for i, sid in enumerate(options.values()):
                    if str(sid) == str(selected_season_id):
                        default_index = i
                        break
            chosen_name = st.selectbox(
                "Season", names, index=default_index, label_visibility="collapsed",
            )
            new_season_id = options[chosen_name]

    with c_nav1:
        st.page_link("views/home_matches.py", label="Matches", icon="⚽")
    with c_nav2:
        st.page_link("views/standings.py", label="Standings", icon="🏆")

    st.markdown("<hr class='navbar-divider'>", unsafe_allow_html=True)

    return new_season_id


def format_match_date(raw) -> str:
    """'2026-08-21T19:00:00Z' -> 'Fri, 21 Aug 2026 · 07:00 PM'"""
    if pd.isna(raw):
        return ""
    ts = pd.to_datetime(raw)
    return ts.strftime("%a, %d %b %Y · %I:%M %p")


def render_pagination(current_page: int, total_pages: int):
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if current_page > 1 and st.button("← Previous", use_container_width=True):
            st.query_params["page"] = str(current_page - 1)
            st.rerun()
    with col2:
        st.markdown(
            f"<div style='text-align:center;padding-top:8px;color:var(--text-muted);'>"
            f"Page {current_page} of {total_pages}</div>",
            unsafe_allow_html=True,
        )
    with col3:
        if current_page < total_pages and st.button("Next →", use_container_width=True):
            st.query_params["page"] = str(current_page + 1)
            st.rerun()


def render_match_card(row, season_id):
    with st.container(border=True):
        c1, c2, c3, c4 = st.columns([4, 2, 4, 2])

        played = pd.notna(row["full_time_home_team_score"])
        winner = row.get("winner")

        with c1:
            _render_team(
                row["home_team_crest"], row["home_team_name"], align="right",
                is_winner=(winner == "HOME_TEAM"),
            )

        with c2:
            if played:
                score = f"{int(row['full_time_home_team_score'])} - {int(row['full_time_away_team_score'])}"
            else:
                score = "vs"
            st.markdown(f"<div class='score-pill'>{score}</div>", unsafe_allow_html=True)

        with c3:
            _render_team(
                row["away_team_crest"], row["away_team_name"], align="left",
                is_winner=(winner == "AWAY_TEAM"),
            )

        with c4:
            if played:
                if st.button("Details →", key=f"match_{row['match_id']}", use_container_width=True):
                    st.switch_page(
                        "views/match_detail.py",
                        query_params={"match_id": str(row["match_id"]), "season_id": str(season_id)},
                    )
            else:
                st.button(
                    "Scheduled", key=f"match_{row['match_id']}",
                    use_container_width=True, disabled=True,
                )

        gw = row.get("gameweek")
        gw_txt = f" · Gameweek {int(gw)}" if pd.notna(gw) else ""
        st.caption(f"📅 {format_match_date(row['match_date'])}{gw_txt}")


def _render_team(crest_url, name, align, is_winner=False):
    crest_html = (
        f"<img src='{crest_url}' width='22' style='vertical-align:middle;margin:0 6px;'>"
        if crest_url else ""
    )
    winner_class = " winner" if is_winner else ""
    if align == "right":
        html = f"<div class='team-name right{winner_class}'>{name}{crest_html}</div>"
    else:
        html = f"<div class='team-name left{winner_class}'>{crest_html}{name}</div>"
    st.markdown(html, unsafe_allow_html=True)