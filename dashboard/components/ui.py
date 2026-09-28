import pandas as pd
import streamlit as st

from data.db import DataSourceError
from utils import minute_sort_key, format_minute, asset_data_uri


def render_header(title: str, seasons_df: pd.DataFrame = None, selected_season_id=None):
    """Single header row: title (+ optional season dropdown) on the left,
    nav links pinned to the right. Pass seasons_df only on pages that need
    the season picker (currently just the Matches/home page).

    Returns the selected season_id if seasons_df was passed, else None.
    The season is kept in the season_id query param only once the user
    changes it; without one the latest season is shown.
    """
    c_title, c_dropdown, c_spacer, c_nav1, c_nav2, c_nav3 = st.columns([2, 2, 3, 1, 1, 1])

    new_season_id = selected_season_id

    with c_title:
        st.markdown(f"<div class='page-title'>{title}</div>", unsafe_allow_html=True)

    with c_dropdown:
        if seasons_df is not None and not seasons_df.empty:
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
            # Only write the URL when the user picks a different season:
            # rewriting it on every run adds a browser-history entry each
            # time and breaks the back button (see fix_history_navigation).
            if new_season_id != list(options.values())[default_index]:
                st.query_params["season_id"] = str(new_season_id)

    with c_nav1:
        st.page_link("views/home_matches.py", label="Matches", icon="⚽")
    with c_nav2:
        st.page_link("views/teams_list.py", label="Teams", icon="🏟️")
    with c_nav3:
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
        if current_page > 1 and st.button("← Previous", width="stretch"):
            st.query_params["page"] = str(current_page - 1)
            st.rerun()
    with col2:
        st.markdown(
            f"<div style='text-align:center;padding-top:8px;color:var(--text-muted);'>"
            f"Page {current_page} of {total_pages}</div>",
            unsafe_allow_html=True,
        )
    with col3:
        if current_page < total_pages and st.button("Next →", width="stretch"):
            st.query_params["page"] = str(current_page + 1)
            st.rerun()


def render_match_card(row, season_id, has_live=False):
    """The whole card is clickable: an invisible button (key matchopen_*) is
    stretched over the bordered container by the rules in theme.css and
    opens Match Detail - for scheduled matches too. has_live adds a badge
    for matches whose v2 live feed was recorded."""
    match_id = row["match_id"]
    played = pd.notna(row["full_time_home_team_score"])

    with st.container(border=True, key=f"matchcard_{match_id}"):
        c1, c2, c3 = st.columns([4, 2, 4], vertical_alignment="center")

        with c1:
            _render_team(row["home_team_crest"], row["home_team_name"], side="home")

        with c2:
            if played:
                score = f"{int(row['full_time_home_team_score'])} - {int(row['full_time_away_team_score'])}"
            else:
                score = "vs"
            st.markdown(f"<div class='score-pill'>{score}</div>", unsafe_allow_html=True)

        with c3:
            _render_team(row["away_team_crest"], row["away_team_name"], side="away")

        gw = row.get("gameweek")
        gw_txt = f" · Gameweek {int(gw)}" if pd.notna(gw) else ""
        status = "Full time" if played else "Scheduled"
        live_txt = " · :red-badge[:material/sensors: Live feed]" if has_live else ""
        st.caption(f"📅 {format_match_date(row['match_date'])}{gw_txt} · {status}{live_txt}")

        if st.button("Open match", key=f"matchopen_{match_id}"):
            st.switch_page(
                "views/match_detail.py",
                query_params={"match_id": str(match_id), "season_id": str(season_id)},
            )


def _render_team(crest_url, name, side):
    crest = f"<img src='{crest_url}' class='match-card-crest'>" if crest_url else ""
    if side == "home":
        inner = f"<span>{name}</span>{crest}"
    else:
        inner = f"{crest}<span>{name}</span>"
    st.markdown(
        f"<div class='match-card-team {side}'>{inner}</div>",
        unsafe_allow_html=True,
    )


def render_team_grid_card(row, season_id):
    with st.container(border=True):
        st.markdown(
            "<div style='text-align:center;'>"
            f"<img src='{row.get('team_crest', '')}' style='width:52px;height:52px;object-fit:contain;'>"
            f"<div style='font-weight:700;margin-top:8px;font-size:0.88rem;'>{row['team_name']}</div>"
            "</div>",
            unsafe_allow_html=True,
        )
        if st.button("View", key=f"teamcard_{row['team_id']}", width="stretch"):
            st.switch_page(
                "views/team.py",
                query_params={"team_id": str(row["team_id"]), "season_id": str(season_id)},
            )


def render_score_header(match: pd.Series, season_id=None):
    played = pd.notna(match.get("full_time_home_team_score"))

    with st.container(border=True):
        c1, c2, c3 = st.columns([4, 3, 4])

        with c1:
            _render_score_team(match, "home", season_id)

        with c2:
            if played:
                score_txt = (
                    f"{int(match['full_time_home_team_score'])} - "
                    f"{int(match['full_time_away_team_score'])}"
                )
            else:
                score_txt = "vs"
            st.markdown(f"<div class='big-score'>{score_txt}</div>", unsafe_allow_html=True)

            ht_home = match.get("half_time_home_team_score")
            ht_away = match.get("half_time_away_team_score")
            if pd.notna(ht_home) and pd.notna(ht_away):
                st.markdown(
                    f"<div class='ht-score'>HT {int(ht_home)} - {int(ht_away)}</div>",
                    unsafe_allow_html=True,
                )

        with c3:
            _render_score_team(match, "away", season_id)

        meta_bits = [format_match_date(match["match_date"])]
        if match.get("stadium"):
            meta_bits.append(match["stadium"])
        if match.get("match_referee"):
            meta_bits.append(f"Referee: {match['match_referee']}")
        st.markdown(
            f"<div class='match-meta'>{' · '.join(meta_bits)}</div>",
            unsafe_allow_html=True,
        )


def _render_score_team(match: pd.Series, side: str, season_id):
    """Crest + team name; clicking either opens the team page (the link is
    stretched over the whole keyed container by theme.css). The match
    winner's name is highlighted via the _win key suffix."""
    query_params = {"team_id": str(int(match[f"{side}_team_id"]))}
    if season_id is not None:
        query_params["season_id"] = str(season_id)
    is_winner = match.get("winner") == match.get(f"{side}_team_tla")
    key = f"scoreteam_{side}_win" if is_winner else f"scoreteam_{side}"
    with st.container(key=key):
        st.markdown(
            f"<div class='score-team'>"
            f"<img src='{match.get(f'{side}_team_crest', '')}' class='score-crest'>"
            f"</div>",
            unsafe_allow_html=True,
        )
        st.page_link(
            "views/team.py",
            label=match[f"{side}_team_name"],
            query_params=query_params,
            width="stretch",
        )


def render_error(error: Exception):
    """Friendly error message used by the error boundary in app.py."""
    if isinstance(error, DataSourceError):
        st.error(
            "Couldn't load data right now. The data store may be unreachable "
            "- please try again in a moment.",
            icon=":material/cloud_off:",
        )
    else:
        st.error(
            "An unexpected error happened while loading this page.",
            icon=":material/error:",
        )
    with st.expander("Error details"):
        st.exception(error)
    st.page_link("views/home_matches.py", label="Back to matches", icon=":material/arrow_back:")


def render_invalid_link(message: str, back_page: str, back_label: str):
    """Guard for missing/invalid/unknown ids in the query string."""
    st.error(message, icon=":material/link_off:")
    st.page_link(back_page, label=back_label, icon=":material/arrow_back:")
    st.stop()


def _goal_icon_info(row) -> tuple:
    """(icon_filename, badge_color, tag_text) based on the fact_goals
    booleans - own goal / missed penalty render red, everything else green.
    """
    if row.get("is_own_goal"):
        return "goal.png", "red", "OG"
    if row.get("is_penalty_miss"):
        return "penalty-kick.png", "red", "missed pen"
    if row.get("is_penalty"):
        return "penalty-kick.png", "green", "pen"
    return "goal.png", "green", ""


def render_goal_row(row, align: str = "left"):
    icon_file, color, tag = _goal_icon_info(row)
    icon_uri = asset_data_uri(icon_file)
    fallback = "🎯" if "penalty" in icon_file else "⚽"
    icon_html = f"<img src='{icon_uri}'>" if icon_uri else fallback

    minute_txt = format_minute(row["minute"])
    scorer = row["scorer"] if pd.notna(row["scorer"]) and str(row["scorer"]).strip() else "Unknown player"
    tag_html = f" <span class='goal-tag'>({tag})</span>" if tag else ""

    assist = row.get("assist")
    assist_html = ""
    if pd.notna(assist) and str(assist).strip():
        assist_html = f"<div class='goal-assist'>Assisted by {assist}</div>"

    badge = f"<span class='goal-icon-badge {color}'>{icon_html}</span>"
    text = (
        f"<div class='goal-text'>"
        f"<span class='goal-scorer'>{scorer}{tag_html} {minute_txt}</span>"
        f"{assist_html}"
        f"</div>"
    )

    if align == "left":
        html = f"<div class='goal-row left'>{badge}{text}</div>"
    else:
        html = f"<div class='goal-row right'>{text}{badge}</div>"

    st.markdown(html, unsafe_allow_html=True)


def render_goals_section(match: pd.Series, goals_df: pd.DataFrame):
    st.markdown("<div class='section-header'>Goals</div>", unsafe_allow_html=True)

    if goals_df.empty:
        if pd.notna(match.get("full_time_home_team_score")):
            st.caption("No goals in this match.")
        else:
            st.caption("This match hasn't been played yet.")
        return

    goals_df = goals_df.copy()
    goals_df["_sort_key"] = goals_df["minute"].map(minute_sort_key)
    goals_df = goals_df.sort_values("_sort_key")

    for _, row in goals_df.iterrows():
        is_home = row["team_id"] == match["home_team_id"]
        c1, c2 = st.columns(2)
        with c1:
            if is_home:
                render_goal_row(row, align="left")
        with c2:
            if not is_home:
                render_goal_row(row, align="right")