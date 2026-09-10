import pandas as pd

from config import TABLES
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