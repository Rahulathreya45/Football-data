import re

import pandas as pd
import streamlit as st

from utils import asset_data_uri, abbreviate_name

# Rough defense -> attack ordering, used only to sort starters into
# formation rows (not an exact tactical mapping - see render note below).
_POSITION_RANK = {
    "GK": 0,
    "LB": 10, "RB": 10, "WB": 10, "CB": 11, "DF": 11,
    "DM": 20,
    "LM": 30, "RM": 30, "CM": 31, "MF": 31,
    "AM": 40,
    "LW": 50, "RW": 50, "FW": 51, "ST": 51,
}


def _primary_position(position: str) -> str:
    """'DF,MF' -> 'DF' - some players carry a dual-position tag, take the
    first as the primary one for grouping/sorting purposes."""
    if not position:
        return "MF"
    return position.split(",")[0].strip().upper()


def _position_rank(position: str) -> int:
    return _POSITION_RANK.get(_primary_position(position), 31)


def _player_card(row):
    shirt_uri = asset_data_uri("shirt.svg")
    shirt_html = f"<img src='{shirt_uri}' class='shirt-icon'>" if shirt_uri else "👕"

    number = row.get("jersey_number")
    number_txt = str(int(number)) if pd.notna(number) else ""
    name = abbreviate_name(row.get("player_name", ""))

    html = (
        "<div class='player-card'>"
        "<div class='shirt-wrap'>"
        f"{shirt_html}"
        f"<span class='shirt-number'>{number_txt}</span>"
        "</div>"
        f"<div class='player-name'>{name}</div>"
        "</div>"
    )
    st.markdown(html, unsafe_allow_html=True)


def _render_formation_rows(starters: pd.DataFrame, formation: str):
    """Lays starters out in rows: GK on its own row at the top, then rows
    sized off the formation string (e.g. '4-2-3-1' -> [4, 2, 3, 1]),
    defense first. Within each row, players are ordered by a rough
    position rank rather than a real tactical x/y - the data gives us
    jersey/position/formation but not an explicit grid slot per player,
    so this is an approximation, not a pixel-exact tactics board.
    """
    is_gk = starters["position"].apply(lambda p: _primary_position(p) == "GK")
    gk = starters[is_gk]
    outfielders = starters[~is_gk].copy()
    outfielders["_rank"] = outfielders["position"].apply(_position_rank)
    outfielders = outfielders.sort_values("_rank")

    row_sizes = [int(n) for n in re.findall(r"\d+", formation or "")]
    if not row_sizes or sum(row_sizes) != len(outfielders):
        # Formation string doesn't cleanly account for every outfielder
        # (missing data, red card, etc.) - fall back to one row rather
        # than guessing wrong and mis-slicing the list.
        row_sizes = [len(outfielders)] if len(outfielders) else []

    if not gk.empty:
        cols = st.columns(len(gk))
        for col, (_, prow) in zip(cols, gk.iterrows()):
            with col:
                _player_card(prow)

    idx = 0
    for size in row_sizes:
        chunk = outfielders.iloc[idx: idx + size]
        idx += size
        if chunk.empty:
            continue
        cols = st.columns(len(chunk))
        for col, (_, prow) in zip(cols, chunk.iterrows()):
            with col:
                _player_card(prow)


def _render_team_column(team_df: pd.DataFrame, team_name: str, crest_url: str):
    formation = team_df["team_formation"].dropna()
    formation = formation.iloc[0] if not formation.empty else ""

    crest_html = f"<img src='{crest_url}' class='formation-crest'>" if crest_url else ""
    st.markdown(
        f"<div class='formation-label'>{crest_html}{team_name} · {formation}</div>",
        unsafe_allow_html=True,
    )

    starters = team_df[team_df["is_starter"]]
    _render_formation_rows(starters, formation)

    subs = team_df[~team_df["is_starter"]].sort_values("jersey_number")
    if not subs.empty:
        st.markdown("<div class='subs-label'>Substitutes</div>", unsafe_allow_html=True)
        for _, srow in subs.iterrows():
            num = int(srow["jersey_number"]) if pd.notna(srow["jersey_number"]) else "-"
            st.caption(f"{num} · {srow['player_name']} ({_primary_position(srow['position'])})")


def render_lineups_tab(match: pd.Series, lineups_df: pd.DataFrame):
    if lineups_df.empty:
        st.caption("Lineup data isn't available for this match yet.")
        return

    home_df = lineups_df[lineups_df["team_id"] == match["home_team_id"]]
    away_df = lineups_df[lineups_df["team_id"] == match["away_team_id"]]

    c1, c2 = st.columns(2)
    with c1:
        with st.container(border=True):
            _render_team_column(home_df, match["home_team_name"], match.get("home_team_crest", ""))
    with c2:
        with st.container(border=True):
            _render_team_column(away_df, match["away_team_name"], match.get("away_team_crest", ""))