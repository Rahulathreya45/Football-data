# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Working conventions

- Don't read `*.csv`, `*.json`, `*.jsonl` files or anything under `research/` unless explicitly
  asked — they're large/scratch data, not something to load into context by default
  (`.claude/settings.json` prompts before Read on these). `app.ipynb` is exempt (it's `.ipynb`,
  not `.json`).
- Don't read files covered by `.gitignore` (caches, `.env`, `downloaded_files/`, etc.) unless
  asked.
- Keep this file under 200 lines. When the user makes a decision that changes how this repo
  should be worked in, update this file rather than just answering in chat.

## What this project is

A data engineering portfolio project, topic: football data pipeline/analytics. `README.md` is the
public overview (architecture, what it demonstrates, how to run/deploy); the day-by-day dev log is
`devlog.md`, local only and gitignored (the user keeps it for a portfolio site). Built in two versions:

**v1 (done)** — batch pipeline, Streamlit dashboard:

```
raw APIs/websocket  -->  raw JSON on S3  -->  silver Delta tables  -->  gold Delta tables  -->  Streamlit + DuckDB
(football-data.org,      raw/<year>/...        dim_season             fact_match_summary
 sportsapipro,                                 dim_team               fact_goals / fact_card / fact_subs
 soccerdata/fbref)                             dim_players            fact_table (standings)
                                                                       fact_team_season_stats / fact_players_season_stats
                                                                       fact_match_lineups
                                                                       fact_team_match_performance / fact_player_match_performance
                                                                       fact_goal_keeper_match_performance
```

Sources are landed raw (bronze) in S3, then Databricks builds silver and gold as Delta tables
in S3, queried straight from S3 by DuckDB in the Streamlit dashboard — no warehouse in between.

**v2 (in progress)** — live streaming, being added alongside v1 rather than replacing it:

```
websocket/API (sportsapipro)  -->  Kafka (raw.sportsapipro-events)  -->  DynamoDB (single-row live updates)
                                                                     \->  S3 raw message log  -->  Databricks (Delta)  -->  live tab
```

Match days run live: producer + both consumers during matches (consumers default to live mode;
`--once` is the build-time bounded replay). Built: producer (`live/producer/ws_to_kafka.py`), DynamoDB consumer
(`live/consumer/kafka_to_dynamo.py` + `dynamo_sink.py`, table from `live/data/create_tables.py`),
S3 raw loader (`live/consumer/kafka_to_s3.py`), Databricks jobs `football-live` (file arrival on
`live/raw/`) and `football-batch` (nightly), and the dashboard's Live tab (`dashboard/data/live.py`).

Delta layout (`s3://<bucket>/live/live_delta/`): flat per-message event logs `live_goals`,
`live_cards`, `live_subs`, `live_var_decisions`, `live_injury_time`, `live_lineups`,
`live_team_stats` (every row carries `kafka_partition`, `kafka_offset`, `match_id`, `msg_type`,
`event_ts`). Two facts about the source data:
- Stats, lineups and incidents messages carry full state, so the newest message per match is
  the current state. The base `match:<id>` channel sends only changed fields, with flat dotted
  keys (`"homeScore.current"`), so its state is the newest non-null value per field.
- Match and team ids in live data are sportsapipro's, not football-data.org's ids used by v1
  and the dashboard. The live tab needs a mapping between the two.

S3 raw log contract (`kafka_to_s3.py`), which the Databricks job depends on:
- Path: `s3://<bucket>/live/raw/date=YYYY-MM-DD/part-<partition>-<first offset>-<last offset>.jsonl`
  (own prefix: new files there trigger the Databricks `football-live` job),
  day = UTC date of the Kafka message timestamp. Grouped by day because the producer finds
  matches through the per-day `/today` API.
- Files are never rewritten; each run only adds new ones (S3 can't append, and Auto Loader
  expects immutable files). Don't switch to one mutable file per day.
- One line per message: `kafka_partition`, `kafka_offset`, `kafka_timestamp_ms`, `key`
  (match id or `unkeyed`), `value` (the raw frame as a string, parse with `from_json`).
- At-least-once: offsets are committed after upload (live mode flushes each partition every
  `FLUSH_INTERVAL_SECONDS`, 60, or at 5,000 records), so a crash can re-upload a range.
  Dedupe on `(kafka_partition, kafka_offset)` downstream.

## Repository layout

- `app.ipynb` — the actual ETL/ingestion code lives here, as a sequence of mostly-independent
  cells rather than importable modules. Each markdown cell names the data source/endpoint
  (e.g. "Football-data.org / Standings", "SoccerData-FBRef / Players Season Stats - Shooting");
  the code cell below it fetches from the source API, writes a local copy under `raw/`, and
  uploads the same payload to S3 (`raw/<key>`). Later cells (from "Day 17" onward per the
  README) build the silver/gold Delta tables from this raw data and, at the end, contain the
  Kafka producer (websocket -> Kafka) and consumer/replay (Kafka -> pandas) code for live data.
  When asked to change ingestion or ETL logic, look here first — there is no separate `src/`
  or `etl/` package.
- `databricks/` — `Football_data_pipeline.ipynb` (silver/gold), `live_pipeline.ipynb` (raw log ->
  `live_delta`, param `days_back`, default 1 = today + yesterday, `all` = rebuild) and
  `maintenance.ipynb` (OPTIMIZE + VACUUM of every silver/gold/live_delta table; the dashboard
  pays one S3 request per file, so small files make it slow). Synced through a Databricks Git folder
  (`/Users/<user>/Football-data`): edits made here reach Databricks after a push and a pull in
  the Git folder, and edits made in Databricks need Commit & Push there, then `git pull` here.
  Databricks CLI (default profile) is set up; use `databricks workspace export` / `jobs` /
  `api` for reads, and ask before anything that writes or runs in the workspace.
- `dashboard/` — the Streamlit app that reads the **gold** Delta layer via DuckDB. This is a
  normal importable Python package (see Architecture below).
- `live/` — v2 streaming scripts (`producer/`, `consumer/`, `data/`), run as plain scripts
  (`python live/consumer/kafka_to_s3.py`), configured through env vars with defaults.
- `raw/` — local mirror of what's uploaded to S3 under `raw/`, partitioned by year and source
  (`football_data_org`, `soccerdata_fbref`, `sports_api_pro`), plus a legacy
  `raw/football-data/{competitions,matches,teams}` layout from early in the project.
- `learning/` — the user's Kafka lessons (gitignored, not project code); only touch it when teaching.

## Architecture of `dashboard/`

- `dashboard/config.py` — the only place table locations are defined. `TABLES` maps logical
  names (`fact_match_summary`, `dim_team`, ...) to `s3://<bucket>/silver|gold/<table>` Delta
  paths. Add new tables here, not inline in query code.
- `dashboard/data/db.py` — owns the single cached DuckDB connection (`get_connection`, via
  `st.cache_resource`) with `httpfs`/`aws`/`delta` extensions loaded, and `run_query(sql, params)`
  (`st.cache_data`, 6 h: batch tables only change nightly; `run_live_query` is the 2-min twin for
  `live_delta`). `data/prefetch.py` runs a page's loaders in parallel threads before the page calls
  them (cold pages are S3-latency-bound) and warms common queries on first visit. AWS auth is two-path:
  deployed (Streamlit Cloud) reads `st.secrets["aws"]`, local reads an AWS SSO profile
  (`AWS_PROFILE` env var) via `boto3`. `run_query` uses a cursor per query because the cached
  connection is shared across session threads; DuckDB/credential failures surface as
  `DataSourceError`, which the error boundary around `pg.run()` in `app.py` renders nicely.
- Browser history: `components/styling.py:fix_history_navigation` works around Streamlit's
  multipage back-button bugs (stale query params, duplicate history entries). Don't write
  `st.query_params` on every run — only on a user action — or back navigation breaks again.
- `dashboard/data/queries.py` — all SQL lives here as small functions returning
  `pandas.DataFrame` (or a single `pd.Series`/`None` for single-row lookups), each querying one
  or two `delta_scan('<TABLES[...]>')` tables directly (no ORM). This is the layer to extend
  when a view needs new data — never build SQL inline inside a view/component.
  Data gotcha: soccerdata caches FBref pages with no expiry, so the season-level ingestion
  cells in `app.ipynb` pass `no_cache=is_latest` (else the live season's stats freeze at the
  first download). `dim_players` is built from lineups (everyone in a matchday squad) + season
  stats (details only); built from season stats alone, it missed unused subs and late debutants,
  and every name join downstream silently dropped them.
  Data gotcha: the raw FBref team-match CSVs have an empty `team` column, so the silver
  `fact_team_match_*` cells take `team_id` from `venue` + `fact_match` home/away ids. Don't
  join `dim_team` on `opponent` — that put every team's stats on the opponent's row.
- `dashboard/data/live.py` — the v2 Live tab's data, read from DynamoDB (`live_match_state`,
  `LIVE_MATCH_TABLE`/`AWS_REGION` env vars) through `db.get_aws_session()`, not from `live_delta`.
  A capture is mapped to a dashboard match by (home team, away team) via
  `dim_team.sports_api_pro_team_id` plus kickoff within 3 days of the last message, so no
  sportsapipro match id needs ingesting. The Live tab (`components/live.py`) only appears for
  mapped matches; match cards get a "Live feed" badge. DynamoDB failures never break a page.
- `dashboard/data/live_history.py` — the Live tab's over-time views (Match flow, Leaderboard,
  1st/2nd-half filter) from the S3 `live_delta` history via `queries.get_live_*`. Delta
  `event_ts` is 5h30m early (Databricks stored UTC clock as IST); queries fix it on read with
  `LIVE_DELTA_TS_ZONE` - the user doesn't want the Databricks job changed for this. Match
  minutes are estimated per half from when incidents/added-time boards first reached the feed;
  stats arrive in batches, so running totals are interpolated between snapshots. Halves are
  estimated from the last first-half snapshot (checked against the feed's own 1ST/2ND blocks:
  counts exact, % within ~1.5 pts).
- `dashboard/data/match_story.py` — AI match story (Live tab "Match story" button → dialog,
  `components/match_story.py`), Gemini free tier via `google-genai` (`GEMINI_API_KEY`,
  `GEMINI_MODELS` fallback list in `config.py`). Built from the S3 history, not DynamoDB: a
  facts dict for the recorded part of the match (hidden before `STORY_MIN_MINUTE`), Gemini
  writes prose only from it, and numbers not in the facts are retried once then dropped.
  Stories aren't persisted (user's choice); `generate_story` is `st.cache_data`'d on the facts JSON.
- `dashboard/views/*.py` — one file per page, registered as `st.Page` entries in
  `dashboard/app.py` and wired into `st.navigation(...)`. Pages read `st.query_params` for
  IDs (`match_id`, `team_id`, `season_id`), fetch via `data/queries.py`, and delegate rendering
  to `dashboard/components/*.py`. Follow the existing `match_detail.py` pattern (guard on
  missing/invalid id -> `st.error`/`st.stop()` -> render) for new pages.
- `dashboard/components/*.py` — presentation-only helper functions (`render_*`) that take
  DataFrames/rows and draw Streamlit UI; grouped by page section (`lineups.py`, `events.py`,
  `stats.py`, `team_stats.py`, `ui.py`) plus `styling.py` for CSS injection.
- `dashboard/utils.py` — small pure helpers shared across components (minute sorting/formatting,
  column-name humanizing, name abbreviation, base64-encoding local assets for inline HTML).
- `dashboard/assets/` — static images/icons and `theme.css`, loaded by `components/styling.py`.

## Running the dashboard

```
streamlit run dashboard/app.py
```

Requires `.env` (loaded via `python-dotenv`) with at minimum `S3_BUCKET` and `AWS_PROFILE`, and
a logged-in AWS SSO session for that profile (`aws sso login --profile "<AWS_PROFILE>"`) — the
app raises a `DataSourceError` at connection time if credentials can't be obtained. There is no
local/offline mode: every page reads Delta tables straight from S3 via DuckDB.

Deployment (Streamlit Community Cloud, entry point `dashboard/app.py`): auth is the read-only IAM
user `football-dashboard-reader` (inline policy `football-dashboard-read-only`: S3 List + Get on
`silver/`, `gold/`, `live/live_delta/` only; DynamoDB Scan/Query/GetItem/DescribeTable on
`live_match_state`). Its secrets live in the gitignored root `.streamlit/secrets.toml` (top-level
`S3_BUCKET`, `GEMINI_API_KEY`, plus `[aws]`), which is what gets pasted into Cloud. Streamlit turns
top-level secrets into env vars at server start. While that file exists, local runs from the repo
root also use those keys instead of SSO. If the dashboard starts reading a new S3 prefix or AWS
service, extend that policy too.

## Working in `app.ipynb`

- Dependencies: `requirements-pipeline.txt` (notebook + `live/`) and `dashboard/requirements.txt`
  (dashboard only; Streamlit Community Cloud installs this one). Keep them in sync with imports.
- Ingestion cells follow a copy-paste pattern: set `URL`/`HEADERS`/`PARAMS`, fetch, write to a
  local `OUTPUT_PATH` under `raw/`, then `put_object` the same bytes to S3 at the matching key.
  When adding a new source/endpoint, match this pattern rather than introducing a shared fetch
  helper (the notebook intentionally keeps each cell runnable independently, top to bottom).
  API keys are read from env vars (`FOOTBALL_DATA_ORG_API_KEY`, `API_FOOTBALL_KEY`, etc.) via
  `.env`.
- The live-data cells at the end are the prototypes of the `live/` scripts (which are now the
  source of truth). They need Kafka at `localhost:9092`, topic `raw.sportsapipro-events`. The
  producer subscribes to Premier League match channels (`match:<id>`, `:incidents`, `:stats`,
  `:lineups`, `:odds`) and forwards every raw frame keyed by match id (non-match frames get
  `unkeyed`). Match/team IDs here (`TOURNAMENT_ID = 17` = Premier League) are sportsapipro's own
  IDs, not football-data.org's.
