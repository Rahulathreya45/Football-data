"""
Keep each match's current state in DynamoDB, from the raw Kafka topic.

Live (default): run during the match alongside the producer. Starts from the
oldest message Kafka still holds and keeps reading new ones until Ctrl+C.
--once: the build-time bounded replay - read up to the end offsets seen at
startup, then exit.

It never commits offsets: every start replays the retained topic. That's safe
because writes are idempotent (put_latest ignores messages older than the row
it would overwrite), and it's required: team ids come from each match's first
lineups message, which a resumed consumer would have skipped.
"""
import argparse
import json
import os
from collections import Counter, defaultdict

import boto3
from confluent_kafka import Consumer, TopicPartition
from dotenv import load_dotenv

from dynamo_sink import write_team_stats, write_lineups, write_incidents

load_dotenv()

BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP", "localhost:9092")
TOPIC = os.getenv("KAFKA_TOPIC", "raw.sportsapipro-events")
TABLE_NAME = os.getenv("LIVE_MATCH_TABLE", "live_match_state")
REGION = os.getenv("AWS_REGION", "ap-south-1")

GROUP_ID = "dynamo-sink-v1"
KEEP_TYPES = {"snapshot", "update"}


def parse_channel(channel):
    parts = (channel or "").split(":")
    return parts[2] if len(parts) > 2 else ("match" if len(parts) == 2 else None)


def main(once: bool):
    table = boto3.resource("dynamodb", region_name=REGION).Table(TABLE_NAME)
    team_ids_by_match = defaultdict(dict)   # match_id -> {"home": id, "away": id}, from that match's first lineups message
    counts = defaultdict(Counter)

    consumer = Consumer({
        "bootstrap.servers": BOOTSTRAP_SERVERS,
        "group.id": GROUP_ID,
        "enable.auto.commit": False,
        "auto.offset.reset": "earliest",
    })

    metadata = consumer.list_topics(TOPIC, timeout=10)
    partitions = sorted(metadata.topics[TOPIC].partitions.keys())

    start_offsets, end_offsets = {}, {}
    for partition in partitions:
        low, high = consumer.get_watermark_offsets(TopicPartition(TOPIC, partition), timeout=10, cached=False)
        start_offsets[partition] = low
        end_offsets[partition] = high

    backlog = sum(end_offsets[p] - start_offsets[p] for p in partitions)
    print(f"Topic: {TOPIC} | partitions: {partitions} | messages so far: {backlog} | mode: {'once' if once else 'live'}")

    # Live mode reads every partition, including empty ones, since new messages can land anywhere.
    pending = {p for p in partitions if start_offsets[p] < end_offsets[p]} if once else set(partitions)
    if not pending:
        print("Topic is empty.")
        consumer.close()
        return

    consumer.assign([TopicPartition(TOPIC, p, start_offsets[p]) for p in pending])

    try:
        while pending:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                print(f"Kafka error: {msg.error()}")
                continue

            partition, offset = msg.partition(), msg.offset()
            if once and offset >= end_offsets[partition]:
                continue                   # produced after startup; picked up by the next run

            key = msg.key().decode("utf-8") if msg.key() else None
            if key and key.isdigit():      # match channels are keyed by match id; everything else is "unkeyed"
                match_id = int(key)
                team_ids = team_ids_by_match[match_id]
                try:
                    env = json.loads(msg.value().decode("utf-8"))
                except json.JSONDecodeError:
                    print(f"Invalid JSON: partition={partition}, offset={offset}")
                else:
                    kind = parse_channel(env.get("channel"))
                    if env.get("type") in KEEP_TYPES and kind == "stats":
                        write_team_stats(table, match_id, env, team_ids, offset)
                        counts[match_id]["stats"] += 1
                    elif env.get("type") in KEEP_TYPES and kind == "lineups":
                        write_lineups(table, match_id, env, team_ids, offset)
                        counts[match_id]["lineups"] += 1
                    elif env.get("type") in KEEP_TYPES and kind == "incidents":
                        write_incidents(table, match_id, env, team_ids, offset)
                        counts[match_id]["incidents"] += 1
                    else:
                        counts[match_id]["skipped"] += 1   # odds, heartbeats, base match channel, non-snapshot/update types

            if once and offset >= end_offsets[partition] - 1:
                pending.discard(partition)
    except KeyboardInterrupt:
        print("Stopping (Ctrl+C).")
    finally:
        consumer.close()

    print(f"Done. {len(counts)} matches written:")
    for match_id, c in sorted(counts.items()):
        print(f"  {match_id}: {dict(c)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--once", action="store_true", help="replay up to the current end of the topic, then exit")
    main(once=parser.parse_args().once)
