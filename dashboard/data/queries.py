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