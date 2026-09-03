import os
from dotenv import load_dotenv
load_dotenv()
S3_BUCKET = os.getenv("S3_BUCKET")
S3_REGION = "ap-south-1"

AWS_PROFILE = os.getenv("AWS_PROFILE")

GOLD_BASE = f"s3://{S3_BUCKET}/gold"
SIlVER_BASE = f"s3://{S3_BUCKET}/silver"

TABLES = {
    "dim_season": f"{SIlVER_BASE}/dim_season",
    "dim_team": f"{SIlVER_BASE}/dim_team",
    "dim_player": f"{SIlVER_BASE}/dim_players",
    "fact_match_summary": f"{GOLD_BASE}/fact_match_summary",
    "fact_goals": f"{GOLD_BASE}/fact_goals",
    "fact_card": f"{GOLD_BASE}/fact_card",
    "fact_subs": f"{GOLD_BASE}/fact_subs",
    "fact_match_lineups": f"{GOLD_BASE}/fact_match_lineups",
    "fact_team_season_stats": f"{GOLD_BASE}/fact_team_season_stats",
    "fact_players_season_stats": f"{GOLD_BASE}/fact_players_season_stats",
    "fact_table": f"{GOLD_BASE}/fact_table",
    "fact_team_match_performance": f"{GOLD_BASE}/fact_team_match_performance",
    "fact_player_match_performance": f"{GOLD_BASE}/fact_player_match_performance",
    "fact_goal_keeper_match_performance": f"{GOLD_BASE}/fact_goal_keeper_match_performance",
}

MATCHES_PER_PAGE = 10