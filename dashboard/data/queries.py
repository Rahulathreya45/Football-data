import pandas as pd

from config import TABLES, LIVE_DELTA_TS_ZONE
from data.db import run_query

def get_seasons() -> pd.DataFrame:
    sql = f"""
        SELECT DISTINCT season_id, season_name
        FROM delta_scan('{TABLES["fact_match_summary"]}')
        ORDER BY season_id DESC
    """
    return run_query(sql)
 
 
def get_matches(season_id: int, page: int = 1, page_size: int = 10) -> pd.DataFrame:
    offset = (page - 1) * page_size
    sql = f"""
        SELECT
            match_id,
            gameweek,
            match_date,
            home_team_id,
            home_team_name,
            home_team_tla,
            home_team_crest,
            full_time_home_team_score,
            home_team_red_cards,
            away_team_id,
            away_team_name,
            away_team_tla,
            away_team_crest,
            full_time_away_team_score,
            away_team_red_cards,
            winner
        FROM delta_scan('{TABLES["fact_match_summary"]}')
        WHERE season_id = ?
        ORDER BY match_date
        LIMIT ? OFFSET ?
    """
    return run_query(sql, (season_id, page_size, offset))
 
 
def get_matches_count(season_id: int) -> int:
    sql = f"""
        SELECT COUNT(*) AS cnt
        FROM delta_scan('{TABLES["fact_match_summary"]}')
        WHERE season_id = ?
    """
    df = run_query(sql, (season_id,))
    return int(df["cnt"].iloc[0])

def get_match(match_id: int):
    """Single match row (all columns) for the Match Detail page, or None
    if the id doesn't exist."""
    sql = f"""
        SELECT *
        FROM delta_scan('{TABLES["fact_match_summary"]}')
        WHERE match_id = ?
    """
    df = run_query(sql, (match_id,))
    return None if df.empty else df.iloc[0]
 
 
def get_match_goals(match_id: int) -> pd.DataFrame:
    sql = f"""
        SELECT *
        FROM delta_scan('{TABLES["fact_goals"]}')
        WHERE match_id = ?
    """
    return run_query(sql, (match_id,))

def get_match_cards(match_id: int) -> pd.DataFrame:
    sql = f"""
        SELECT *
        FROM delta_scan('{TABLES["fact_card"]}')
        WHERE match_id = ?
    """
    return run_query(sql, (match_id,))
 
 
def get_match_subs(match_id: int) -> pd.DataFrame:
    sql = f"""
        SELECT *
        FROM delta_scan('{TABLES["fact_subs"]}')
        WHERE match_id = ?
    """
    return run_query(sql, (match_id,))

def get_team_match_performance(match_id: int) -> pd.DataFrame:
    sql = f"""
        SELECT *
        FROM delta_scan('{TABLES["fact_team_match_performance"]}')
        WHERE match_id = ?
    """
    return run_query(sql, (match_id,))

def get_player_match_performance(match_id: int) -> pd.DataFrame:
    sql = f"""
        SELECT *
        FROM delta_scan('{TABLES["fact_player_match_performance"]}')
        WHERE match_id = ?
    """
    return run_query(sql, (match_id,))
 
 
def get_goalkeeper_match_performance(match_id: int) -> pd.DataFrame:
    sql = f"""
        SELECT *
        FROM delta_scan('{TABLES["fact_goal_keeper_match_performance"]}')
        WHERE match_id = ?
    """
    return run_query(sql, (match_id,))

def get_standings(season_id: int, table_type: str = "TOTAL") -> pd.DataFrame:
    sql = f"""
        SELECT *
        FROM delta_scan('{TABLES["fact_table"]}')
        WHERE season_id = ? AND type = ?
        ORDER BY position
    """
    return run_query(sql, (season_id, table_type))

def get_team(team_id: int):
    """Single dim_team row (name/venue/crest/tla) for the Team page header."""
    sql = f"""
        SELECT *
        FROM delta_scan('{TABLES["dim_team"]}')
        WHERE team_id = ?
    """
    df = run_query(sql, (team_id,))
    return None if df.empty else df.iloc[0]
 
 
def get_teams_by_season(season_id: int) -> pd.DataFrame:
    """Teams that actually appeared in this season's standings, joined to
    dim_team for name/venue/crest - used by the Teams listing grid.
    """
    sql = f"""
        SELECT DISTINCT
            t.team_id,
            t.team_name,
            t.team_venue,
            t.team_crest,
            t.team_tla
        FROM delta_scan('{TABLES["fact_table"]}') f
        JOIN delta_scan('{TABLES["dim_team"]}') t ON t.team_id = f.team_id
        WHERE f.season_id = ?
        ORDER BY t.team_name
    """
    return run_query(sql, (season_id,))
 
 
def get_team_matches(team_id: int, season_id: int, page: int = 1, page_size: int = 10) -> pd.DataFrame:
    offset = (page - 1) * page_size
    sql = f"""
        SELECT
            match_id, gameweek, match_date,
            home_team_id, home_team_name, home_team_tla, home_team_crest,
            full_time_home_team_score, home_team_red_cards,
            away_team_id, away_team_name, away_team_tla, away_team_crest,
            full_time_away_team_score, away_team_red_cards,
            winner
        FROM delta_scan('{TABLES["fact_match_summary"]}')
        WHERE season_id = ? AND (home_team_id = ? OR away_team_id = ?)
        ORDER BY match_date
        LIMIT ? OFFSET ?
    """
    return run_query(sql, (season_id, team_id, team_id, page_size, offset))
 
 
def get_team_matches_count(team_id: int, season_id: int) -> int:
    sql = f"""
        SELECT COUNT(*) AS cnt
        FROM delta_scan('{TABLES["fact_match_summary"]}')
        WHERE season_id = ? AND (home_team_id = ? OR away_team_id = ?)
    """
    df = run_query(sql, (season_id, team_id, team_id))
    return int(df["cnt"].iloc[0])

def get_team_season_stats(team_id: int, season_id: int):
    sql = f"""
        SELECT *
        FROM delta_scan('{TABLES["fact_team_season_stats"]}')
        WHERE team_id = ? AND season_id = ?
    """
    df = run_query(sql, (team_id, season_id))
    return None if df.empty else df.iloc[0]
 
 
def get_team_players_season_stats(team_id: int, season_id: int) -> pd.DataFrame:
    sql = f"""
        SELECT p.player_name, s.*
        FROM delta_scan('{TABLES["fact_players_season_stats"]}') s
        JOIN delta_scan('{TABLES["dim_player"]}') p ON p.player_id = s.player_id
        WHERE s.team_id = ? AND s.season_id = ?
    """
    return run_query(sql, (team_id, season_id))

def get_match_lineups(match_id: int) -> pd.DataFrame:
    """fact_match_lineups joined to dim_player for the display name.
    ASSUMPTION: dim_player has player_id + player_name (full name) -
    unconfirmed, matching the pattern dim_team uses (team_id/team_name).
    Fix the join/column below if your actual schema differs.
    """
    sql = f"""
        SELECT
            l.jersey_number,
            l.position,
            l.is_starter,
            l.minutes_played,
            l.team_id,
            l.player_id,
            l.team_formation,
            p.player_name
        FROM delta_scan('{TABLES["fact_match_lineups"]}') l
        JOIN delta_scan('{TABLES["dim_player"]}') p ON p.player_id = l.player_id
        WHERE l.match_id = ?
    """
    return run_query(sql, (match_id,))

def get_team_sports_api_ids() -> pd.DataFrame:
    """dim_team's team_id <-> sportsapipro team id, for mapping the live feed
    (which only knows sportsapipro ids) onto dashboard teams."""
    sql = f"""
        SELECT team_id, sports_api_pro_team_id
        FROM delta_scan('{TABLES["dim_team"]}')
        WHERE sports_api_pro_team_id IS NOT NULL
    """
    return run_query(sql)


def get_match_keys() -> pd.DataFrame:
    """Every match's teams and kickoff, all seasons - the live-feed mapping
    finds a dashboard match by (home team, away team, date)."""
    sql = f"""
        SELECT match_id, home_team_id, away_team_id, match_date
        FROM delta_scan('{TABLES["fact_match_summary"]}')
    """
    return run_query(sql)


# ---------------------------------------------------------------- live feed history (S3 Delta)
# event_ts in live_delta is the feed's UTC clock stored as LIVE_DELTA_TS_ZONE
# time; reading it back as that zone's wall clock and re-labelling it UTC
# gives the real instant.
_LIVE_TS = f"timezone('UTC', timezone('{LIVE_DELTA_TS_ZONE}', event_ts))"


def get_live_team_stats_history(live_match_id: int) -> pd.DataFrame:
    """Every team-stats snapshot the live feed sent for a match (cumulative,
    full-match values), one row per side per message."""
    sql = f"""
        SELECT side, {_LIVE_TS} AS event_ts, kafka_offset,
               possession, xg, big_chances, shots_total, shots_off_target, saves,
               passes, passes_accurate, fouls, tackles, interceptions, clearances,
               recoveries, touches_opp_box, final_third_entries, duels_won_pct
        FROM delta_scan('{TABLES["live_team_stats"]}')
        WHERE match_id = ?
        ORDER BY event_ts, side
    """
    return run_query(sql, (live_match_id,))


def get_live_player_stats_history(live_match_id: int) -> pd.DataFrame:
    """Every lineup snapshot for a match: each player's cumulative stats per message."""
    sql = f"""
        SELECT side, player_name, shirt_number, is_sub, position,
               {_LIVE_TS} AS event_ts, kafka_offset,
               minutes, touches, passes, passes_accurate, shots, xg, xa,
               duels_won, duels_lost, recoveries, clearances
        FROM delta_scan('{TABLES["live_lineups"]}')
        WHERE match_id = ?
        ORDER BY event_ts
    """
    return run_query(sql, (live_match_id,))


def get_live_incident_first_seen(live_match_id: int) -> pd.DataFrame:
    """When each incident (and each added-time board, with its length) first
    reached the feed, with its match minute - the anchors for turning clock
    time into match minutes."""
    sql = f"""
        SELECT 'goal' AS kind, id, time, NULL AS length, min({_LIVE_TS}) AS first_seen FROM delta_scan('{TABLES["live_goals"]}') WHERE match_id = ? GROUP BY ALL
        UNION ALL
        SELECT 'card', id, time, NULL, min({_LIVE_TS}) FROM delta_scan('{TABLES["live_cards"]}') WHERE match_id = ? GROUP BY ALL
        UNION ALL
        SELECT 'sub', id, time, NULL, min({_LIVE_TS}) FROM delta_scan('{TABLES["live_subs"]}') WHERE match_id = ? GROUP BY ALL
        UNION ALL
        SELECT 'var', id, time, NULL, min({_LIVE_TS}) FROM delta_scan('{TABLES["live_var_decisions"]}') WHERE match_id = ? GROUP BY ALL
        UNION ALL
        SELECT 'injury', NULL, time, max(length), min({_LIVE_TS}) FROM delta_scan('{TABLES["live_injury_time"]}') WHERE match_id = ? GROUP BY time
    """
    return run_query(sql, (live_match_id,) * 5)
