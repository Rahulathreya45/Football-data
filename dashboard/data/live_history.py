"""Match-flow analytics from the live feed's full message history (the S3
Delta tables, read through queries.get_live_*). DynamoDB (data/live.py) only
keeps each match's latest state, so everything "over time" comes from here.

The feed stamps messages with clock time, not match minutes. Minutes are
estimated per half from anchors the feed pins to a minute: when an incident
(goal/card/sub/VAR) or an added-time board first reached it. A late message
can only make an anchor look *later* than it happened, so each half's
kickoff is the earliest one its anchors imply. Incidents that were already
in the first message (the capture started after them) aren't anchors.
Without usable anchors the scheduled kickoff and a 15-minute break are used.
"""
from dataclasses import dataclass

import numpy as np
import pandas as pd
import streamlit as st

from data.queries import (
    get_live_incident_first_seen,
    get_live_player_stats_history,
    get_live_team_stats_history,
)

HALF_TIME_BREAK = pd.Timedelta(minutes=15)
MOMENTUM_WINDOW = 5          # minutes

# Stats that are percentages of the whole match so far - they can't be
# split into halves by subtraction.
PERCENT_STATS = {"possession", "duels_won_pct", "pass_accuracy"}


@dataclass(frozen=True)
class MatchClock:
    h1_zero: pd.Timestamp          # clock time of minute 0
    h2_zero: pd.Timestamp          # 2nd-half kickoff minus 45' (so minute = now - h2_zero)
    first_half_end: float          # 45 + added time
    full_time: float               # 90 + added time

    @property
    def second_half_kickoff(self) -> pd.Timestamp:
        return self.h2_zero + pd.Timedelta(minutes=45)

    def minutes(self, ts: pd.Series) -> pd.DataFrame:
        """Estimated match minute, half (1/2) and play time for each clock time."""
        in_second = ts >= self.second_half_kickoff
        m1 = ((ts - self.h1_zero) / pd.Timedelta(minutes=1)).clip(0, self.first_half_end)
        m2 = ((ts - self.h2_zero) / pd.Timedelta(minutes=1)).clip(45, self.full_time)
        out = pd.DataFrame({"minute": np.where(in_second, m2, m1), "half": np.where(in_second, 2, 1)}, index=ts.index)
        out["play"] = self.play(out["minute"], out["half"])
        return out

    def play(self, minute, half):
        """Continuous play time: the 2nd half starts where the 1st (with its
        added time) ended, so 45+2' and 46' don't overlap on a chart axis."""
        return np.where(np.asarray(half) == 1, minute, self.first_half_end + np.asarray(minute) - 45)


def minute_label(minute: float, half: int) -> str:
    """41.3 -> "42'", 1st-half 46.2 -> "45+2'", 92.5 -> "90+3'"."""
    whole = int(np.ceil(minute)) if minute > 0 else 0
    cap = 45 if half == 1 else 90
    return f"{cap}+{whole - cap}'" if whole > cap else f"{whole}'"


def _added_time(anchors: pd.DataFrame, minute: int) -> float:
    boards = anchors[(anchors["kind"] == "injury") & (anchors["time"] == minute)]
    return float(boards["length"].iloc[0]) if not boards.empty and pd.notna(boards["length"].iloc[0]) else 0.0


def build_clock(anchors: pd.DataFrame, kickoff: pd.Timestamp) -> MatchClock:
    added_1, added_2 = _added_time(anchors, 45), _added_time(anchors, 90)
    anchors = anchors[anchors["time"] >= 1]

    h1_zero = h2_zero = None
    if not anchors.empty:
        first_message = anchors["first_seen"].min()
        live = anchors[(anchors["first_seen"] - first_message) > pd.Timedelta(seconds=2)]
        # An incident at minute t happened during (t-1, t]; a board goes up at 45/90.
        elapsed = np.where(live["kind"] == "injury", live["time"], live["time"] - 0.5)
        implied = live["first_seen"] - pd.to_timedelta(elapsed, unit="min")
        is_h1 = (live["time"] <= 44) | ((live["kind"] == "injury") & (live["time"] == 45))
        is_h2 = live["time"].between(46, 89) | ((live["kind"] == "injury") & (live["time"] == 90))
        h1_zero = implied[is_h1].min() if is_h1.any() else None
        h2_zero = implied[is_h2].min() if is_h2.any() else None

    h1_zero = h1_zero if h1_zero is not None and pd.notna(h1_zero) else kickoff
    fallback_h2 = h1_zero + pd.Timedelta(minutes=added_1) + HALF_TIME_BREAK
    # The 2nd half can't start before the 1st ends.
    if h2_zero is None or pd.isna(h2_zero) or h2_zero < h1_zero + pd.Timedelta(minutes=added_1):
        h2_zero = fallback_h2
    return MatchClock(h1_zero, h2_zero, 45 + added_1, 90 + added_2)


def _with_minutes(df: pd.DataFrame, clock: MatchClock) -> pd.DataFrame:
    if df.empty:
        return df.assign(minute=pd.Series(dtype=float), half=pd.Series(dtype=int))
    df = df.copy()
    df["event_ts"] = pd.to_datetime(df["event_ts"], utc=True)
    return df.join(clock.minutes(df["event_ts"]))


@st.cache_data(ttl=300, show_spinner=False)
def get_match_flow(live_match_id: int, kickoff) -> dict:
    """Team and player stat histories with estimated match minutes, plus the
    clock used. `kickoff` is the scheduled kickoff (fallback anchor)."""
    anchors = get_live_incident_first_seen(live_match_id)
    anchors["first_seen"] = pd.to_datetime(anchors["first_seen"], utc=True)
    clock = build_clock(anchors, pd.to_datetime(kickoff, utc=True))

    team = _with_minutes(get_live_team_stats_history(live_match_id), clock)
    if not team.empty:
        team["pass_accuracy"] = team["passes_accurate"] / team["passes"].where(team["passes"] > 0) * 100
    players = _with_minutes(get_live_player_stats_history(live_match_id), clock)
    return {"clock": clock, "team": team, "players": players}


# ---------------------------------------------------------------- momentum
def _half_windows(start: float, end: float) -> list[tuple[float, float]]:
    """5-minute windows over one half; the last one absorbs added time."""
    edges = list(np.arange(start, start + 45, MOMENTUM_WINDOW)) + [end]
    return list(zip(edges[:-1], edges[1:]))


def momentum(team: pd.DataFrame, clock: MatchClock, metric: str) -> pd.DataFrame:
    """How much of `metric` each side added in each 5-minute window.

    sportsapipro updates team stats in batches (gaps of up to ~15 minutes),
    so the running totals are interpolated linearly between snapshots before
    differencing - a batch is spread over the minutes it covers instead of
    landing as one spike. Windows before the capture started, or after the
    latest snapshot, are left out."""
    columns = ["half", "start", "end", "label", "side", "value"]
    if team.empty:
        return pd.DataFrame(columns=columns)

    series = {}
    for side in ("home", "away"):
        s = team[team["side"] == side].sort_values("play")
        s = s.assign(v=s[metric].fillna(0)).groupby("play", as_index=False)["v"].last()
        series[side] = (s["play"].to_numpy(), s["v"].to_numpy())
    first_play = max(x[0] for x, _ in series.values())
    last_play = min(x[-1] for x, _ in series.values())

    rows = []
    for half, (h_start, h_end) in ((1, (0, clock.first_half_end)), (2, (45, clock.full_time))):
        for start, end in _half_windows(h_start, h_end):
            p_start, p_end = (float(clock.play(m, half)) for m in (start, end))
            if p_start < first_play or p_start >= last_play:
                continue
            p_end = min(p_end, last_play)
            is_last = end == h_end and end > h_start + 45
            label = f"{int(start)}–{int(h_start + 45)}+" if is_last else f"{int(start)}–{int(round(end))}"
            for side, (x, y) in series.items():
                value = np.interp(p_end, x, y) - np.interp(p_start, x, y)
                rows.append((half, start, end, label, side, max(float(value), 0.0)))
    return pd.DataFrame(rows, columns=columns)


# ---------------------------------------------------------------- half split
def _team_totals(players: pd.DataFrame, upto: pd.Timestamp | None) -> pd.DataFrame:
    """Per side duels won/lost summed over players, from the last lineup
    snapshot at or before `upto` (None = latest)."""
    snaps = players if upto is None else players[players["event_ts"] <= upto]
    if snaps.empty:
        return pd.DataFrame(columns=["duels_won", "duels_lost"])
    last = snaps.sort_values("event_ts").groupby(["side", "player_name"]).tail(1)
    return last.groupby("side")[["duels_won", "duels_lost"]].sum()


def split_halves(flow: dict) -> dict | None:
    """{'1st': stats by side, '2nd': stats by side} estimated from snapshots,
    or None when the capture didn't cover the end of the first half.

    Counts split by subtraction (full match minus the last first-half
    snapshot). Pass accuracy and duels won % are rebuilt from their counts.
    Second-half possession is an estimate: possession is a share of the whole
    match so far, so it's back-solved assuming each half's length in minutes."""
    team, players, clock = flow["team"], flow["players"], flow["clock"]
    if team.empty:
        return None
    first = team[team["half"] == 1]
    if first.empty or first["minute"].max() < 40:
        return None

    ht_ts = first["event_ts"].max()
    ht = first[first["event_ts"] == ht_ts].set_index("side")
    ft = team[team["event_ts"] == team["event_ts"].max()].set_index("side")
    stat_cols = [c for c in team.columns if c not in ("side", "event_ts", "kafka_offset", "minute", "half")]

    h1 = ht[stat_cols].copy()
    h2 = (ft[stat_cols] - ht[stat_cols]).clip(lower=0)

    # Pass accuracy per half from its own passes.
    for half in (h1, h2):
        half["pass_accuracy"] = half["passes_accurate"] / half["passes"].where(half["passes"] > 0) * 100

    # Duels won % per half from player-level duel counts.
    duels_ht, duels_ft = _team_totals(players, ht_ts), _team_totals(players, None)
    if not duels_ft.empty:
        for half, d in ((h1, duels_ht), (h2, (duels_ft - duels_ht.reindex(duels_ft.index, fill_value=0)))):
            total = (d["duels_won"] + d["duels_lost"]).reindex(half.index)
            half["duels_won_pct"] = (d["duels_won"].reindex(half.index) / total.where(total > 0) * 100)

    # Possession: full = (h1 * T1 + h2 * T2) / (T1 + T2)  ->  solve for h2.
    t1, t2 = clock.first_half_end, clock.full_time - 45
    if t2 > 0:
        est = (ft["possession"] * (t1 + t2) - ht["possession"] * t1) / t2
        est = est.clip(0, 100)
        if est.sum() > 0:
            h2["possession"] = est / est.sum() * 100
    return {"1st": h1, "2nd": h2}


# ---------------------------------------------------------------- leaderboard
LEADERBOARD_METRICS = {
    "Goal threat (xG + xA)": lambda df: df["xg"].fillna(0) + df["xa"].fillna(0),
    "Touches": lambda df: df["touches"],
    "Accurate passes": lambda df: df["passes_accurate"],
    "Duels won": lambda df: df["duels_won"],
    "Ball recoveries": lambda df: df["recoveries"],
    "Shots": lambda df: df["shots"],
}


def leaderboard(players: pd.DataFrame, metric: str, top: int = 10) -> pd.DataFrame:
    """Top players so far on `metric`, with the metric's path over the
    match (one value per lineup snapshot) for a sparkline."""
    columns = ["side", "player_name", "shirt_number", "minutes", "value", "trend"]
    if players.empty:
        return pd.DataFrame(columns=columns)
    df = players.sort_values("event_ts").copy()
    df["value"] = LEADERBOARD_METRICS[metric](df).fillna(0)

    grouped = df.groupby(["side", "player_name"], sort=False)
    latest = grouped.tail(1).set_index(["side", "player_name"])
    trend = grouped["value"].agg(list)
    table = latest.assign(trend=trend).reset_index()
    table = table[table["minutes"].fillna(0) > 0]
    return table.sort_values("value", ascending=False).head(top)[columns].reset_index(drop=True)
