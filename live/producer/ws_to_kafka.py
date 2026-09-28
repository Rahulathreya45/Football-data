import asyncio, json, os, re
import requests
import websockets
from confluent_kafka import Producer
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_FOOTBALL_KEY")
KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
TOPIC = os.getenv("KAFKA_TOPIC", "raw.sportsapipro-events")
WS_URL = os.getenv("SPORTSAPIPRO_WS_URL", "wss://api.sportsapipro.com/v2/football/ws")
REST_BASE = os.getenv("SPORTSAPIPRO_REST_BASE", "https://api.sportsapipro.com/v2/football/api")
TOURNAMENT_ID = int(os.getenv("TOURNAMENT_ID", "17"))
TOURNAMENT_SLUG = os.getenv("TOURNAMENT_SLUG", "premier-league")
TOURNAMENT_CATEGORY_SLUG = os.getenv("TOURNAMENT_CATEGORY_SLUG", "england")
RAW_LOG_FILE = os.getenv("RAW_LOG_FILE", "sportsapipro_raw.jsonl")

MATCH_CHANNEL_SUFFIXES = ("", ":incidents", ":stats", ":lineups", ":odds")
ACTIVE_STATUSES = ("notstarted", "inprogress")

producer = Producer({
    "bootstrap.servers": KAFKA_BOOTSTRAP_SERVERS,
    "acks": "all",
    "enable.idempotence": True,
})


def delivery_report(err, msg):
    if err is not None:
        print(f"KAFKA DELIVERY FAILED: {err}")


def describe_tournament(tournament: dict) -> str:
    tournament = tournament or {}
    unique_id = (tournament.get("uniqueTournament") or {}).get("id")
    category = (tournament.get("category") or {}).get("slug")
    return f"{tournament.get('name')} (uniqueTournament={unique_id}, slug={tournament.get('slug')}, category={category})"


def is_tracked_tournament(tournament: dict) -> bool:
    """uniqueTournament.id decides when present; the slug fallback (pre-game fixtures may lack it)
    also checks the country, because other countries' leagues use the slug "premier-league" too."""
    tournament = tournament or {}
    unique_id = (tournament.get("uniqueTournament") or {}).get("id")
    if unique_id is not None:
        return unique_id == TOURNAMENT_ID
    category = (tournament.get("category") or {}).get("slug")
    return tournament.get("slug") == TOURNAMENT_SLUG and category == TOURNAMENT_CATEGORY_SLUG


def get_todays_matches():
    """One-off REST call at startup — seeds any tracked matches already live/upcoming today."""
    resp = requests.get(f"{REST_BASE}/today", headers={"x-api-key": API_KEY})
    resp.raise_for_status()
    events = resp.json()["events"]

    matches = {}
    for e in events:
        if is_tracked_tournament(e.get("tournament")):
            matches[e["id"]] = e["status"]["type"]
            print(f"tracking: id={e['id']} {describe_tournament(e.get('tournament'))}")
        else:
            print(f"skipped (not tracked): id={e.get('id')} {describe_tournament(e.get('tournament'))}")
    return matches


match_key_re = re.compile(r"match:(\d+)")


def kafka_send(raw_message: str, f):
    f.write(raw_message + "\n")
    f.flush()
    m = match_key_re.search(raw_message)
    key = m.group(1) if m else "unkeyed"
    while True:
        try:
            producer.produce(TOPIC, key=key, value=raw_message, callback=delivery_report)
            break
        except BufferError:
            producer.poll(0.1)
    producer.poll(0)


async def subscribe_match(ws, match_id, subscribed):
    for suffix in MATCH_CHANNEL_SUFFIXES:
        ch = f"match:{match_id}{suffix}"
        if ch not in subscribed:
            await ws.send(json.dumps({"action": "subscribe", "channel": ch}))
            subscribed.add(ch)
            print(f"subscribed: {ch}")


async def unsubscribe_match(ws, match_id, subscribed):
    for suffix in MATCH_CHANNEL_SUFFIXES:
        ch = f"match:{match_id}{suffix}"
        if ch in subscribed:
            await ws.send(json.dumps({"action": "unsubscribe", "channel": ch}))
            subscribed.discard(ch)
            print(f"unsubscribed: {ch}")


async def keepalive(ws):
    while True:
        await asyncio.sleep(30)
        await ws.send(json.dumps({"action": "ping", "channel": "live-scores"}))


async def watch():
    uri = f"{WS_URL}?x-api-key={API_KEY}"
    live_matches = get_todays_matches()
    backoff = 1

    with open(RAW_LOG_FILE, "a", encoding="utf-8") as f:
        while True:
            subscribed = set()
            try:
                async with websockets.connect(uri) as ws:
                    backoff = 1

                    await ws.send(json.dumps({"action": "subscribe", "channel": "live-scores:football"}))
                    subscribed.add("live-scores:football")
                    print("subscribed: live-scores:football")

                    for mid, status in list(live_matches.items()):
                        if status in ACTIVE_STATUSES:
                            await subscribe_match(ws, mid, subscribed)

                    ping_task = asyncio.create_task(keepalive(ws))
                    try:
                        async for message in ws:
                            kafka_send(message, f)
                            try:
                                frame = json.loads(message)
                            except json.JSONDecodeError:
                                print(f"non-JSON frame (still saved raw): {message[:100]}")
                                continue

                            print(f"→ {frame.get('channel')} [{frame.get('type')}]")

                            if frame.get("channel") == "live-scores:football":
                                for game in frame.get("data", {}).get("games", []):
                                    mid = game["id"]
                                    if not is_tracked_tournament(game.get("tournament")):
                                        continue
                                    status = game["status"]["type"]
                                    prev = live_matches.get(mid)
                                    live_matches[mid] = status
                                    if status == "inprogress" and prev != "inprogress":
                                        await subscribe_match(ws, mid, subscribed)
                                    elif status == "finished" and prev == "inprogress":
                                        await unsubscribe_match(ws, mid, subscribed)
                    finally:
                        ping_task.cancel()

            except (websockets.exceptions.ConnectionClosed, OSError) as e:
                print(f"disconnected ({e}) — retrying in {backoff}s")
                await asyncio.sleep(backoff)
                backoff = min(backoff * 2, 30)


async def main():
    try:
        await watch()
    finally:
        print("flushing producer — waiting for any pending messages to be delivered...")
        producer.flush(timeout=10)


if __name__ == "__main__":
    os.makedirs(os.path.dirname(RAW_LOG_FILE) or ".", exist_ok=True)
    asyncio.run(main())