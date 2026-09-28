"""
One-time setup: create the DynamoDB table for live-match state.

Single table, single-table design:
  PK  match_id  (Number)
  SK  sk        (String)   e.g. STATS#home, LINEUP#48#07, INC#GOAL#123, INC#INJURYTIME#45

Run once: python create_tables.py
"""
import os
import boto3
from dotenv import load_dotenv

load_dotenv()

TABLE_NAME = os.getenv("LIVE_MATCH_TABLE", "live_match_state")
REGION = os.getenv("AWS_REGION", "ap-south-1")


def create_live_match_table():
    ddb = boto3.client("dynamodb", region_name=REGION)

    existing = ddb.list_tables()["TableNames"]
    if TABLE_NAME in existing:
        print(f"Table '{TABLE_NAME}' already exists — skipping.")
        return

    ddb.create_table(
        TableName=TABLE_NAME,
        KeySchema=[
            {"AttributeName": "match_id", "KeyType": "HASH"},
            {"AttributeName": "sk", "KeyType": "RANGE"},
        ],
        AttributeDefinitions=[
            {"AttributeName": "match_id", "AttributeType": "N"},
            {"AttributeName": "sk", "AttributeType": "S"},
        ],
        BillingMode="PAY_PER_REQUEST",   # traffic is bursty (live match) then idle — avoid provisioning for peak
    )
    ddb.get_waiter("table_exists").wait(TableName=TABLE_NAME)
    print(f"Created table '{TABLE_NAME}'.")

    # Delta is the permanent record; Dynamo only needs to hold state for a few days
    # after full time, so let old matches expire automatically.
    ddb.update_time_to_live(
        TableName=TABLE_NAME,
        TimeToLiveSpecification={"Enabled": True, "AttributeName": "ttl"},
    )
    print("Enabled TTL on attribute 'ttl'.")


if __name__ == "__main__":
    create_live_match_table()