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