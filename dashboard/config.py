import os
from dotenv import load_dotenv
load_dotenv()
S3_BUCKET = os.getenv("S3_BUCKET")
S3_REGION = "ap-south-1"

AWS_PROFILE = os.getenv("AWS_PROFILE")

GOLD_BASE = f"s3://{S3_BUCKET}/gold"
SIlVER_BASE = f"s3://{S3_BUCKET}/silver"
LIVE_DELTA_BASE = f"s3://{S3_BUCKET}/live/live_delta"

# The Databricks live job stores the feed's UTC clock time as if it were in
# this zone (pandas -> spark.createDataFrame under an IST session), so every
# live_delta event_ts is 5h30m early. Queries undo it on read instead of
# changing the Databricks job.
LIVE_DELTA_TS_ZONE = "Asia/Kolkata"

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
    # v2 live feed history (every message), written by the Databricks live cells
    "live_team_stats": f"{LIVE_DELTA_BASE}/live_team_stats",
    "live_lineups": f"{LIVE_DELTA_BASE}/live_lineups",
    "live_goals": f"{LIVE_DELTA_BASE}/live_goals",
    "live_cards": f"{LIVE_DELTA_BASE}/live_cards",
    "live_subs": f"{LIVE_DELTA_BASE}/live_subs",
    "live_var_decisions": f"{LIVE_DELTA_BASE}/live_var_decisions",
    "live_injury_time": f"{LIVE_DELTA_BASE}/live_injury_time",
}

MATCHES_PER_PAGE = 10

# v2 live feed: DynamoDB table written by live/consumer/kafka_to_dynamo.py
# (same env vars as the live/ scripts).
LIVE_MATCH_TABLE = os.getenv("LIVE_MATCH_TABLE", "live_match_state")
LIVE_REGION = os.getenv("AWS_REGION", S3_REGION)
