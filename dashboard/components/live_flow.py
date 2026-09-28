"""Match flow and Leaderboard sub-tabs of the Live tab: charts over the live
feed's message history (data/live_history.py get_match_flow)."""
import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

from data.live_history import LEADERBOARD_METRICS, leaderboard, minute_label, momentum

# Team colours: the stat bars' hues (#00d26a / #58a6ff) stepped into the
# dark-mode lightness band for chart marks - checked with the dataviz palette
# validator against both the page and card surfaces (CVD ΔE 23.6).
HOME_COLOR, AWAY_COLOR = "#00ab57", "#4b8ff0"
TEXT, MUTED, GRID, SURFACE = "#e6edf3", "#8b949e", "#262d38", "#0d1117"
FONT = "Source Sans Pro, sans-serif"

# Extra stats a viewer can add under the xG chart: label -> (column, d3 format).
TREND_STATS = {
    "Possession %": ("possession", ".0f"),
    "Shots": ("shots_total", ".0f"),
    "Big chances": ("big_chances", ".0f"),
    "Touches in opp. box": ("touches_opp_box", ".0f"),
    "Final third entries": ("final_third_entries", ".0f"),
    "Pass accuracy %": ("pass_accuracy", ".0f"),
    "Duels won %": ("duels_won_pct", ".0f"),
    "Tackles": ("tackles", ".0f"),
    "Saves": ("saves", ".0f"),
}

MOMENTUM_METRICS = {
    "Touches in opp. box": "touches_opp_box",
    "Shots": "shots_total",
    "xG": "xg",
    "Final third entries": "final_third_entries",
}


# ---------------------------------------------------------------- shared chart pieces
def _style(chart: alt.TopLevelMixin, height: int) -> alt.TopLevelMixin:
    return (
        chart.properties(height=height, width="container")
        .configure(background="transparent", font=FONT)
        .configure_view(stroke=None)
        .configure_axis(
            labelColor=MUTED, titleColor=MUTED, labelFontSize=12, titleFontSize=12,
            titleFontWeight="normal", gridColor=GRID, gridWidth=1, domain=False,
            tickColor=GRID, labelPadding=6,
        )
        .configure_legend(
            orient="top", direction="horizontal", title=None, labelColor=TEXT,
            labelFontSize=12, symbolStrokeWidth=2, padding=0, offset=6,
        )
    )


def _x(clock, **kwargs) -> alt.X:
    """Shared match-minute axis over play time: 0'...45' | HT | 60'...90'."""
    h1 = clock.first_half_end
    ticks = [0, 15, 30, 45] + [float(clock.play(m, 2)) for m in (60, 75, 90)]
    label = f"(datum.value > {h1:.3f} ? round(datum.value - {h1 - 45:.3f}) : round(datum.value)) + \"′\""
    return alt.X(
        kwargs.pop("field", "play:Q"),
        scale=alt.Scale(domain=[0, float(clock.play(clock.full_time, 2))], nice=False),
        axis=alt.Axis(values=ticks, labelExpr=label, grid=False, title=None),
        **kwargs,
    )


def _half_time_rule(clock) -> alt.LayerChart:
    df = pd.DataFrame({"play": [clock.first_half_end], "label": ["HT"]})
    rule = alt.Chart(df).mark_rule(color=GRID, strokeWidth=1).encode(x=_x(clock))
    text = alt.Chart(df).mark_text(color=MUTED, fontSize=11, align="left", dx=4, baseline="top").encode(
        x=_x(clock), y=alt.value(0), text="label:N"
    )
    return rule + text


def _team_scale(names: dict) -> alt.Scale:
    return alt.Scale(domain=[names["home"], names["away"]], range=[HOME_COLOR, AWAY_COLOR])


def _series(team: pd.DataFrame, col: str, names: dict) -> pd.DataFrame:
    d = team[["side", "play", "minute", "half", col]].dropna(subset=[col])
    d = d.sort_values("play").groupby(["side", "play"], as_index=False).last()
    d["team"] = d["side"].map(names)
    d["when"] = [minute_label(m, h) for m, h in zip(d["minute"], d["half"])]
    return d.rename(columns={col: "value"})


def _line_chart(team, clock, col, names, fmt, height, goals=None, area=False):
    """Line per team over the match with a crosshair tooltip; optional goal
    markers (xG chart). Linear between snapshots: the feed sends stats in
    batches, and a step line would pile each batch onto the minute it arrived."""
    d = _series(team, col, names)
    if d.empty:
        return None
    scale = _team_scale(names)
    color = alt.Color("team:N", scale=scale, legend=alt.Legend(symbolType="stroke"))
    no_legend = alt.Color("team:N", scale=scale, legend=None)
    y = alt.Y("value:Q", title=None, axis=alt.Axis(format=fmt, tickCount=4))

    line = alt.Chart(d).mark_line(
        interpolate="linear", strokeWidth=2, strokeCap="round", strokeJoin="round"
    ).encode(x=_x(clock), y=y, color=color)

    last = d.groupby("side").tail(1)
    end_dot = alt.Chart(last).mark_circle(size=70, opacity=1, stroke=SURFACE, strokeWidth=2).encode(
        x=_x(clock), y=y, color=no_legend
    )
    end_label = alt.Chart(last).mark_text(align="left", dx=8, color=TEXT, fontSize=12).encode(
        x=_x(clock), y=y, text=alt.Text("value:Q", format=fmt)
    )

    # Crosshair: one row per snapshot time with both teams' latest values.
    wide = (
        d.pivot_table(index=["play", "when"], columns="side", values="value", aggfunc="last")
        .reset_index().sort_values("play").ffill()
    )
    for side in ("home", "away"):
        if side not in wide:
            wide[side] = np.nan
    nearest = alt.selection_point(nearest=True, on="pointermove", fields=["play"], empty=False, clear="pointerout")
    tooltip = [
        alt.Tooltip("when:N", title="Minute"),
        alt.Tooltip("home:Q", title=names["home"], format=fmt),
        alt.Tooltip("away:Q", title=names["away"], format=fmt),
    ]
    hover = alt.Chart(wide).mark_point(opacity=0, size=400).encode(x=_x(clock), tooltip=tooltip).add_params(nearest)
    crosshair = alt.Chart(wide).mark_rule(color=MUTED, strokeWidth=1).encode(x=_x(clock)).transform_filter(nearest)

    layers = [_half_time_rule(clock), line, crosshair, end_dot, end_label, hover]
    if area:
        # A 10% wash under each line; stack=None so the teams overlap from 0
        # instead of stacking on top of each other.
        wash = alt.Chart(d).mark_area(interpolate="linear", opacity=0.1).encode(
            x=_x(clock), y=alt.Y("value:Q", stack=None), color=no_legend
        )
        layers.insert(1, wash)

    if goals is not None and not goals.empty and col == "xg":
        g = goals.copy()
        g["half"] = np.where(g["time"] <= 45, 1, 2)
        g["play"] = clock.play(g["time"], g["half"])
        g["team"] = g["side"].map(names)
        g["when"] = [minute_label(m, h) for m, h in zip(g["time"], g["half"])]
        # Goals before the stats capture began have no line to sit on (they're
        # still in the Timeline tab).
        g = g[g["play"] >= d["play"].min()]
        # Sit each goal on its team's line.
        g["value"] = [
            float(np.interp(p, d.loc[d["side"] == s, "play"], d.loc[d["side"] == s, "value"]))
            if (d["side"] == s).any() else 0.0
            for s, p in zip(g["side"], g["play"])
        ]
        g["score"] = g["home_score"].astype("Int64").astype(str) + "-" + g["away_score"].astype("Int64").astype(str)
        layers.append(
            alt.Chart(g).mark_point(shape="circle", filled=True, size=130, opacity=1, stroke=SURFACE, strokeWidth=2)
            .encode(
                x=_x(clock), y=y, color=no_legend,
                tooltip=[
                    alt.Tooltip("scorer_name:N", title="Goal"),
                    alt.Tooltip("when:N", title="Minute"),
                    alt.Tooltip("score:N", title="Score"),
                ],
            )
        )
    return _style(alt.layer(*layers), height)


def goals_before_capture(team: pd.DataFrame, goals: pd.DataFrame | None, clock) -> int:
    """Goals the xG chart leaves out because they came before the first stats snapshot."""
    if goals is None or goals.empty or team.empty:
        return 0
    play = clock.play(goals["time"], np.where(goals["time"] <= 45, 1, 2))
    return int((play < team["play"].min()).sum())


def _momentum_chart(team, clock, col, names, height):
    m = momentum(team, clock, col)
    if m.empty:
        return None, m
    m["team"] = m["side"].map(names)
    m["center"] = [float(clock.play((s + e) / 2, h)) for s, e, h in zip(m["start"], m["end"], m["half"])]
    m["x0"], m["x1"] = m["center"] - 1.3, m["center"] + 1.3
    m["signed"] = np.where(m["side"] == "home", m["value"], -m["value"])
    fmt = ".2f" if col == "xg" else ".1f"
    limit = max(float(m["value"].max()), 0.1) * 1.1

    color = alt.Color("team:N", scale=_team_scale(names), legend=alt.Legend(symbolType="square"))
    base = alt.Chart(m).encode(
        x=_x(clock, field="x0:Q"), x2="x1:Q",
        # Symmetric so neither team's bars look bigger by scale alone.
        y=alt.Y(
            "signed:Q", title=None, axis=alt.Axis(labelExpr="abs(datum.value)", tickCount=4),
            scale=alt.Scale(domain=[-limit, limit], nice=False),
        ),
        y2=alt.datum(0),          # grow from the zero line (x + x2 alone makes Vega-Lite draw horizontal ranges)
        color=color,
        tooltip=[
            alt.Tooltip("label:N", title="Minutes"),
            alt.Tooltip("team:N", title="Team"),
            alt.Tooltip("value:Q", title="Added", format=fmt),
        ],
    )
    # Rounded at the data end, square at the baseline (above for home, below for away).
    home = base.transform_filter(alt.datum.side == "home").mark_bar(cornerRadiusTopLeft=4, cornerRadiusTopRight=4)
    away = base.transform_filter(alt.datum.side == "away").mark_bar(cornerRadiusBottomLeft=4, cornerRadiusBottomRight=4)
    zero = alt.Chart(pd.DataFrame({"y": [0]})).mark_rule(color=MUTED, strokeWidth=1).encode(y="y:Q")
    return _style(alt.layer(_half_time_rule(clock), home, away, zero), height), m


# ---------------------------------------------------------------- sub-tabs
def _section(title: str):
    st.markdown(f"<div class='section-header'>{title}</div>", unsafe_allow_html=True)


def render_match_flow(flow: dict, live: dict, match: pd.Series):
    team, clock = flow["team"], flow["clock"]
    if team.empty:
        st.caption("The feed's history for this match isn't in the S3 tables yet.")
        return
    names = {"home": match["home_team_name"], "away": match["away_team_name"]}
    first = team.sort_values("play").iloc[0]
    st.caption(
        f"Minutes are estimated from the live feed · stats from "
        f"{minute_label(first['minute'], first['half'])}"
    )

    _section("Expected goals (xG)")
    chart = _line_chart(team, clock, "xg", names, ".2f", 280, goals=live.get("goals"))
    if chart is None:
        st.caption("No xG in the feed for this match.")
    else:
        st.altair_chart(chart, theme=None, width="stretch")
        early = goals_before_capture(team, live.get("goals"), clock)
        note = f" {early} goal{'s' if early != 1 else ''} came before the stats capture began - see Timeline." if early else ""
        st.caption(f"Dots mark goals.{note}")

    extra = st.pills(
        "Add stats over time", options=list(TREND_STATS), selection_mode="multi",
        default=None, key="live_flow_trends",
    )
    if extra:
        cols = st.columns(2)
        for i, label in enumerate(extra):
            col, fmt = TREND_STATS[label]
            with cols[i % 2]:
                st.markdown(f"**{label}**")
                chart = _line_chart(team, clock, col, names, fmt, 190, area=True)
                if chart is None:
                    st.caption("Not in the feed for this match.")
                else:
                    st.altair_chart(chart, theme=None, width="stretch")

    _section("Momentum")
    metric = st.segmented_control(
        "Momentum metric", options=list(MOMENTUM_METRICS), default="Touches in opp. box",
        key="live_momentum_metric", label_visibility="collapsed",
    ) or "Touches in opp. box"
    chart, windows = _momentum_chart(team, clock, MOMENTUM_METRICS[metric], names, 240)
    if chart is None:
        st.caption("Not enough of the match captured for momentum yet.")
    else:
        st.altair_chart(chart, theme=None, width="stretch")
        st.caption(f"{metric} per 5 minutes")
        with st.expander("View data"):
            table = windows.pivot_table(index=["half", "start", "label"], columns="side", values="value").reset_index()
            table = table.rename(columns={"label": "Minutes", "home": names["home"], "away": names["away"]})
            st.dataframe(table.drop(columns=["half", "start"]).round(3), hide_index=True, width="stretch")


def render_leaderboard(flow: dict, match: pd.Series):
    players = flow["players"]
    if players.empty:
        st.caption("The feed's player history for this match isn't in the S3 tables yet.")
        return
    metric = st.segmented_control(
        "Rank by", options=list(LEADERBOARD_METRICS), default="Goal threat (xG + xA)",
        key="live_leaderboard_metric", label_visibility="collapsed",
    ) or "Goal threat (xG + xA)"
    board = leaderboard(players, metric)
    if board.empty:
        st.caption("No player stats in the feed yet.")
        return

    names = {"home": match["home_team_name"], "away": match["away_team_name"]}
    board = board.assign(
        rank=range(1, len(board) + 1),
        team=board["side"].map(names),
    )[["rank", "player_name", "team", "minutes", "value", "trend"]]
    is_xg = metric.startswith("Goal threat")
    st.dataframe(
        board, hide_index=True, width="stretch",
        column_config={
            "rank": st.column_config.NumberColumn("#", width="small"),
            "player_name": st.column_config.TextColumn("Player"),
            "team": st.column_config.TextColumn("Team"),
            "minutes": st.column_config.NumberColumn("Min", format="%d"),
            "value": st.column_config.NumberColumn(metric, format="%.2f" if is_xg else "%d"),
            "trend": st.column_config.LineChartColumn("Over the match", y_min=0, color=MUTED),
        },
    )
    st.caption("Top 10 players so far, both teams. The line shows how their total built up.")
