import asyncio, json, os, re, time
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
# Match discovery. The sportsapipro key allows 100 REST calls a day in total (resets 00:00 UTC), /today
# lists only matches already in progress, and live-scores:football pushes no score updates on
# WebSocket v3.2. So the fixture list is read a few times a day and each match is subscribed on a
# timer around its kick-off - never by polling.
FOOTBALL_BASE = REST_BASE.rsplit("/api", 1)[0]                 # .../v2/football (fixture endpoints)
SEASON_ID = os.getenv("SPORTSAPIPRO_SEASON_ID")                # optional; else resolved via /seasons
FIXTURE_REFRESH_SECONDS = int(os.getenv("FIXTURE_REFRESH_SECONDS", str(6 * 3600)))
SUBSCRIBE_BEFORE_KICKOFF = 15 * 60                             # lineups arrive before kick-off
UNSUBSCRIBE_AFTER_KICKOFF = 3 * 3600
# Manual override, e.g. MATCH_IDS=16363879 when the REST quota is used up: subscribed while running.
MATCH_IDS = {int(m) for m in os.getenv("MATCH_IDS", "").split(",") if m.strip()}

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


def rest_get(url):
    resp = requests.get(url, headers={"x-api-key": API_KEY}, timeout=30)
    if resp.status_code == 429:
        raise RuntimeError(f"REST quota used up ({resp.headers.get('x-ratelimit-limit')}/day, "
                           f"resets {resp.headers.get('x-ratelimit-reset')})")
    return resp


def _label(e):
    return f"{(e.get('homeTeam') or {}).get('name')} v {(e.get('awayTeam') or {}).get('name')}"


def get_live_now():
    """Tracked matches already in progress (/today lists only live matches) -> {id: (kickoff, label)}. 1 call."""
    resp = rest_get(f"{REST_BASE}/today")
    resp.raise_for_status()
    return {e["id"]: (e["startTimestamp"], _label(e)) for e in resp.json()["events"]
            if is_tracked_tournament(e.get("tournament"))}


def get_upcoming_fixtures():
    """The tracked tournament's next fixtures -> {id: (kickoff, label)}. 1-3 calls."""
    season_id = SEASON_ID
    if not season_id:
        resp = rest_get(f"{REST_BASE}/tournaments/{TOURNAMENT_ID}/seasons")
        resp.raise_for_status()
        season_id = resp.json()["seasons"][0]["id"]
    fixtures = {}
    for page in range(2):
        resp = rest_get(f"{FOOTBALL_BASE}/tournament/{TOURNAMENT_ID}/season/{season_id}/events/next/{page}")
        if resp.status_code == 404:
            break
        resp.raise_for_status()
        data = resp.json()
        for e in data.get("events", []):
            fixtures[e["id"]] = (e["startTimestamp"], _label(e))
        if not data.get("hasNextPage"):
            break
    return fixtures


def load_schedule(include_live_now):
    """Fixtures to subscribe around kick-off. Each source is best effort: a failed call (quota,
    network) is logged and the producer keeps running with whatever it already has."""
    schedule = {}
    sources = [("upcoming fixtures", get_upcoming_fixtures)]
    if include_live_now:
        sources.append(("in progress now", get_live_now))
    for name, fetch in sources:
        try:
            found = fetch()
            schedule.update(found)
            print(f"{name}: {len(found)} tracked")
        except Exception as e:
            print(f"{name}: lookup failed ({e})")
    for mid, (kickoff, label) in sorted(schedule.items(), key=lambda kv: kv[1][0]):
        when = time.strftime("%a %H:%M UTC", time.gmtime(kickoff))
        print(f"tracking: id={mid} {label} kick-off {when}")
    return schedule


async def apply_schedule(ws, schedule, subscribed):
    """Every 30 s: subscribe from SUBSCRIBE_BEFORE_KICKOFF before kick-off until
    UNSUBSCRIBE_AFTER_KICKOFF after; MATCH_IDS stay subscribed. No REST calls."""
    while True:
        now = time.time()
        for mid in MATCH_IDS:
            await subscribe_match(ws, mid, subscribed)
        for mid, (kickoff, _) in list(schedule.items()):
            if mid in MATCH_IDS:
                continue
            if kickoff - SUBSCRIBE_BEFORE_KICKOFF <= now <= kickoff + UNSUBSCRIBE_AFTER_KICKOFF:
                await subscribe_match(ws, mid, subscribed)
            else:
                await unsubscribe_match(ws, mid, subscribed)
        await asyncio.sleep(30)


async def refresh_schedule(schedule):
    while True:
        await asyncio.sleep(FIXTURE_REFRESH_SECONDS)
        schedule.update(await asyncio.to_thread(load_schedule, False))


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
    schedule = load_schedule(include_live_now=True)      # {match id: (kick-off ts, label)}
    if MATCH_IDS:
        print(f"MATCH_IDS override: {sorted(MATCH_IDS)}")
    refresh_task = asyncio.create_task(refresh_schedule(schedule))
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

                    ping_task = asyncio.create_task(keepalive(ws))
                    schedule_task = asyncio.create_task(apply_schedule(ws, schedule, subscribed))
                    try:
                        async for message in ws:
                            kafka_send(message, f)
                            try:
                                frame = json.loads(message)
                            except json.JSONDecodeError:
                                print(f"non-JSON frame (still saved raw): {message[:100]}")
                                continue

                            print(f"\u2192 {frame.get('channel')} [{frame.get('type')}]")

                            # Older feed versions push live scores here; if any arrive, a tracked match
                            # missing from the schedule is added from its kick-off time.
                            if frame.get("channel") == "live-scores:football":
                                for game in frame.get("data", {}).get("games", []):
                                    if is_tracked_tournament(game.get("tournament")) and game["id"] not in schedule:
                                        schedule[game["id"]] = (game.get("startTimestamp") or time.time(), _label(game))
                    finally:
                        ping_task.cancel()
                        schedule_task.cancel()

            except (websockets.exceptions.ConnectionClosed, OSError) as e:
                print(f"disconnected ({e}) - retrying in {backoff}s")
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