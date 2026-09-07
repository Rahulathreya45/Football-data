import pandas as pd
import streamlit as st

from utils import minute_sort_key, format_minute
from components.ui import render_goal_row


def render_card_row(row, align: str = "left"):
    is_second_yellow = bool(row.get("second_yellow"))
    is_red = bool(row.get("red"))

    if is_second_yellow:
        # Two yellows -> red: show both, plus an arrow into the red card.
        icon_html = (
            "<span class='card-icon yellow'></span>"
            "<span class='card-arrow'>→</span>"
            "<span class='card-icon red'></span>"
        )
    elif is_red:
        icon_html = "<span class='card-icon red'></span>"
    else:
        icon_html = "<span class='card-icon yellow'></span>"

    minute_txt = format_minute(row["minute"])
    name = row.get("player_1_name", "")
    text = f"<span class='goal-scorer'>{name} {minute_txt}</span>"

    if align == "left":
        html = f"<div class='goal-row left'>{icon_html}{text}</div>"
    else:
        html = f"<div class='goal-row right'>{text}{icon_html}</div>"
    st.markdown(html, unsafe_allow_html=True)


def render_sub_row(row, align: str = "left"):
    minute_txt = format_minute(row["minute"])
    sub_in = row.get("sub_in", "")
    sub_out = row.get("sub_out", "")

    text = (
        "<div class='goal-text'>"
        f"<span class='sub-in'>→ {sub_in}</span>"
        f"<span class='sub-out'>← {sub_out}</span>"
        "</div>"
    )
    minute_tag = f"<span class='goal-tag'>{minute_txt}</span>"

    if align == "left":
        html = f"<div class='goal-row left'>{text}{minute_tag}</div>"
    else:
        html = f"<div class='goal-row right'>{minute_tag}{text}</div>"
    st.markdown(html, unsafe_allow_html=True)


def render_event_row(row, align: str):
    event_type = row["event_type"]
    if event_type == "goal":
        render_goal_row(row, align=align)
    elif event_type == "card":
        render_card_row(row, align=align)
    elif event_type == "sub":
        render_sub_row(row, align=align)


def render_time_marker(label: str):
    st.markdown(f"<div class='time-marker'><span>{label}</span></div>", unsafe_allow_html=True)


def _render_event_group(events_df: pd.DataFrame, match: pd.Series):
    for _, row in events_df.iterrows():
        is_home = row["team_id"] == match["home_team_id"]
        c1, c2 = st.columns(2)
        with c1:
            if is_home:
                render_event_row(row, align="left")
        with c2:
            if not is_home:
                render_event_row(row, align="right")


def render_events_tab(
    match: pd.Series,
    goals_df: pd.DataFrame,
    cards_df: pd.DataFrame,
    subs_df: pd.DataFrame,
):
    stadium = match.get("stadium")
    referee = match.get("referee")  # ASSUMPTION - confirm actual column name
    meta_bits = [b for b in [f"🏟️ {stadium}" if stadium else None,
                              f"🧑‍⚖️ {referee}" if referee else None] if b]
    if meta_bits:
        st.markdown(
            f"<div class='match-meta' style='margin-bottom:18px;'>{' · '.join(meta_bits)}</div>",
            unsafe_allow_html=True,
        )

    frames = []
    if not goals_df.empty:
        frames.append(goals_df.assign(event_type="goal"))
    if not cards_df.empty:
        frames.append(cards_df.assign(event_type="card"))
    if not subs_df.empty:
        frames.append(subs_df.assign(event_type="sub"))

    if not frames:
        st.caption("No events recorded for this match.")
        return

    combined = pd.concat(frames, ignore_index=True, sort=False)
    combined["_sort_key"] = combined["minute"].map(minute_sort_key)
    combined = combined.sort_values("_sort_key")

    # Three segments: first half (incl. 45+x), second half regulation
    # (46-90), second half stoppage (90+x) - split at clean sort-key
    # boundaries: base<=45 -> <4600, base 46-90 exact -> <=9000, else stoppage.
    first_half = combined[combined["_sort_key"] < 4600]
    second_half_reg = combined[(combined["_sort_key"] >= 4600) & (combined["_sort_key"] <= 9000)]
    second_half_stoppage = combined[combined["_sort_key"] > 9000]

    _render_event_group(first_half, match)

    ht_label = "Half-Time"
    ht_injury = match.get("first_half_injury_time")
    if pd.notna(ht_injury) and ht_injury:
        ht_label += f" · +{int(ht_injury)} min"
    render_time_marker(ht_label)

    _render_event_group(second_half_reg, match)

    ft_injury = match.get("second_half_injury_time")
    if pd.notna(ft_injury) and ft_injury:
        render_time_marker(f"Injury Time · +{int(ft_injury)} min")

    _render_event_group(second_half_stoppage, match)