"""Land every raw Kafka message in S3 (live/date=YYYY-MM-DD/) as the bronze log for the live pipeline."""
import datetime as dt
import json
import os

import boto3
from confluent_kafka import OFFSET_INVALID, Consumer, TopicPartition
from dotenv import load_dotenv

load_dotenv()

BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
TOPIC = os.getenv("KAFKA_TOPIC", "raw.sportsapipro-events")
S3_BUCKET = os.getenv("S3_BUCKET")
# Its own prefix (not live/, which also holds live_delta): the Databricks football-live job
# is triggered by new files under it.
S3_PREFIX = os.getenv("LIVE_S3_PREFIX", "live/raw")
REGION = os.getenv("AWS_REGION", "ap-south-1")
GROUP_ID = os.getenv("S3_LOADER_GROUP_ID", "s3-raw-loader-v1")
MAX_RECORDS_PER_FILE = int(os.getenv("MAX_RECORDS_PER_FILE", "5000"))


def to_record(msg):
    return {
        "kafka_partition": msg.partition(),
        "kafka_offset": msg.offset(),
        "kafka_timestamp_ms": msg.timestamp()[1],
        "key": msg.key().decode("utf-8") if msg.key() else None,
        "value": msg.value().decode("utf-8") if msg.value() else None,
    }


def utc_day(ts_ms):
    return dt.datetime.fromtimestamp(ts_ms / 1000, tz=dt.timezone.utc).date().isoformat()


def flush(s3, consumer, partition, records):
    by_day = {}
    for r in records:
        by_day.setdefault(utc_day(r["kafka_timestamp_ms"]), []).append(r)

    for day, rows in by_day.items():
        key = (f"{S3_PREFIX}/date={day}/"
               f"part-{partition:02d}-{rows[0]['kafka_offset']:012d}-{rows[-1]['kafka_offset']:012d}.jsonl")
        body = "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows)
        s3.put_object(Bucket=S3_BUCKET, Key=key, Body=body.encode("utf-8"), ContentType="application/x-ndjson")
        print(f"uploaded {len(rows)} messages -> s3://{S3_BUCKET}/{key}")

    # commit only once every file of the batch is in S3, so a failed upload is retried on the next run
    consumer.commit(offsets=[TopicPartition(TOPIC, partition, records[-1]["kafka_offset"] + 1)], asynchronous=False)


def main():
    s3 = boto3.client("s3", region_name=REGION)
    consumer = Consumer({
        "bootstrap.servers": BOOTSTRAP_SERVERS,
        "group.id": GROUP_ID,
        "enable.auto.commit": False,
        "auto.offset.reset": "earliest",
    })

    partitions = sorted(consumer.list_topics(TOPIC, timeout=10).topics[TOPIC].partitions)
    committed = {tp.partition: tp.offset
                 for tp in consumer.committed([TopicPartition(TOPIC, p) for p in partitions], timeout=10)}

    start, end = {}, {}
    for p in partitions:
        low, high = consumer.get_watermark_offsets(TopicPartition(TOPIC, p), timeout=10, cached=False)
        start[p] = low if committed[p] == OFFSET_INVALID else max(committed[p], low)
        end[p] = high
        print(f"partition {p}: {start[p]} -> {end[p]} ({end[p] - start[p]} new)")

    pending = {p for p in partitions if start[p] < end[p]}
    if not pending:
        print("Nothing new to load.")
        consumer.close()
        return

    consumer.assign([TopicPartition(TOPIC, p, start[p]) for p in pending])
    buffers = {p: [] for p in pending}

    while pending:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print(f"Kafka error: {msg.error()}")
            continue

        p, offset = msg.partition(), msg.offset()
        if offset >= end[p]:
            continue                  # produced after startup; picked up by the next run

        buffers[p].append(to_record(msg))
        if len(buffers[p]) >= MAX_RECORDS_PER_FILE:
            flush(s3, consumer, p, buffers[p])
            buffers[p] = []
        if offset >= end[p] - 1:
            pending.discard(p)

    for p, records in buffers.items():
        if records:
            flush(s3, consumer, p, records)

    consumer.close()
    print("Done.")


if __name__ == "__main__":
    main()
