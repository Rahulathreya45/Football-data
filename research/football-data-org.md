# football-data.org — API Investigation

## Project Context

- **Focus:** Premier League
- **Season:** 2025/26
- **Purpose:** Investigate API response structures and determine
  which data is useful for the football data pipeline.
- **Raw responses:** Stored separately as JSON files.

This document contains the investigation of multiple endpoints
from `football-data.org`.


---

# Endpoint: `competitions`

## 1. Request

| Property | Value |
|---|---|
| Source | `football-data.org` |
| Endpoint | `competitions` |
| Method | `GET` |
| URL | `https://api.football-data.org/v4/competitions/PL` |
| HTTP Status | `200` |
| Captured At | `2026-08-11T08:00:19.143340+00:00` |
| Raw Response | `raw/api-football/fixtures_2025.json` |

### Query Parameters

| Parameter | Value |
|---|---|
| `league` | `39` |
| `season` | `2025` |

### Notes

Premier League 2025/26 season.
Initial investigation of the fixtures endpoint.

---

## 2. Response Metadata

_No standard response metadata detected._

---

## 3. Record Counts

- `seasons`: **128 records**

---

## 4. Response Structure

The following structure is automatically derived from the
complete JSON response.

| JSON Path | Type |
|---|---|
| `$.area` | `object` |
| `$.area.id` | `integer` |
| `$.area.name` | `string` |
| `$.area.code` | `string` |
| `$.area.flag` | `string` |
| `$.id` | `integer` |
| `$.name` | `string` |
| `$.code` | `string` |
| `$.type` | `string` |
| `$.emblem` | `string` |
| `$.currentSeason` | `object` |
| `$.currentSeason.id` | `integer` |
| `$.currentSeason.startDate` | `string` |
| `$.currentSeason.endDate` | `string` |
| `$.currentSeason.currentMatchday` | `integer` |
| `$.currentSeason.winner` | `null` |
| `$.seasons` | `array` |
| `$.seasons[]` | `object` |
| `$.seasons[].id` | `integer` |
| `$.seasons[].startDate` | `string` |
| `$.seasons[].endDate` | `string` |
| `$.seasons[].currentMatchday` | `integer` |
| `$.seasons[].winner` | `null` |
| `$.lastUpdated` | `string` |

---

## 5. Representative Response Examples

### `seasons`

Showing 2 representative record(s).

```json
[
  {
    "id": 2502,
    "startDate": "2026-08-21",
    "endDate": "2027-05-30",
    "currentMatchday": 1,
    "winner": null
  },
  {
    "id": 2403,
    "startDate": "2025-08-15",
    "endDate": "2026-05-24",
    "currentMatchday": 38,
    "winner": null
  }
]
```

---

## 6. Initial Investigation

### Data availability

- [ ] Does this endpoint contain the data we expected?
- [ ] Is the previous Premier League season fully represented?
- [ ] Are there missing or null fields?
- [ ] Is pagination present?
- [ ] Are there API-specific limits?

### Data modelling

- [ ] What are the stable identifiers?
- [ ] Which fields represent entities?
- [ ] Which fields represent relationships?
- [ ] Which nested objects should become separate entities/tables?
- [ ] Which fields overlap with the other API?
- [ ] Which fields are unique to this source?

### Pipeline relevance

- [ ] Is this endpoint required?
- [ ] Is this endpoint a source of truth for any canonical field?
- [ ] Does it need to be called once per season?
- [ ] Does it need to be called once per team?
- [ ] Does it need to be called once per match?
- [ ] How many requests would a complete season require?
- [ ] Can the response be cached and reused?

### Cross-source mapping

- [ ] What provider IDs need canonical mapping?
- [ ] Can entities be matched deterministically?
- [ ] Are there naming differences between providers?
- [ ] Are there provider-specific fields we need to preserve?

### Decisions / observations

_Add conclusions here after inspecting this endpoint._


---

# Endpoint: `competitions/PL/standings`

## 1. Request

| Property | Value |
|---|---|
| Source | `football-data.org` |
| Endpoint | `competitions/PL/standings` |
| Method | `GET` |
| URL | `https://api.football-data.org/v4/competitions/PL/standings/` |
| HTTP Status | `200` |
| Captured At | `2026-08-11T08:07:34.945168+00:00` |
| Raw Response | `raw/football-data/competitions/PL/standings.json` |

### Query Parameters

| Parameter | Value |
|---|---|
| `season` | `2025` |

### Notes

Premier League 2025/26 season.
Initial investigation of the fixtures endpoint.

---

## 2. Response Metadata

_No standard response metadata detected._

---

## 3. Record Counts

- `standings`: **3 records**

---

## 4. Response Structure

The following structure is automatically derived from the
complete JSON response.

| JSON Path | Type |
|---|---|
| `$.filters` | `object` |
| `$.filters.season` | `string` |
| `$.area` | `object` |
| `$.area.id` | `integer` |
| `$.area.name` | `string` |
| `$.area.code` | `string` |
| `$.area.flag` | `string` |
| `$.competition` | `object` |
| `$.competition.id` | `integer` |
| `$.competition.name` | `string` |
| `$.competition.code` | `string` |
| `$.competition.type` | `string` |
| `$.competition.emblem` | `string` |
| `$.season` | `object` |
| `$.season.id` | `integer` |
| `$.season.startDate` | `string` |
| `$.season.endDate` | `string` |
| `$.season.currentMatchday` | `integer` |
| `$.season.winner` | `null` |
| `$.standings` | `array` |
| `$.standings[]` | `object` |
| `$.standings[].stage` | `string` |
| `$.standings[].type` | `string` |
| `$.standings[].group` | `null` |
| `$.standings[].table` | `array` |
| `$.standings[].table[]` | `object` |
| `$.standings[].table[].position` | `integer` |
| `$.standings[].table[].team` | `object` |
| `$.standings[].table[].team.id` | `integer` |
| `$.standings[].table[].team.name` | `string` |
| `$.standings[].table[].team.shortName` | `string` |
| `$.standings[].table[].team.tla` | `string` |
| `$.standings[].table[].team.crest` | `string` |
| `$.standings[].table[].playedGames` | `integer` |
| `$.standings[].table[].form` | `string` |
| `$.standings[].table[].won` | `integer` |
| `$.standings[].table[].draw` | `integer` |
| `$.standings[].table[].lost` | `integer` |
| `$.standings[].table[].points` | `integer` |
| `$.standings[].table[].goalsFor` | `integer` |
| `$.standings[].table[].goalsAgainst` | `integer` |
| `$.standings[].table[].goalDifference` | `integer` |

---

## 5. Representative Response Examples

### `standings`

Showing 2 representative record(s).

```json
[
  {
    "stage": "REGULAR_SEASON",
    "type": "TOTAL",
    "group": null,
    "table": [
      {
        "position": 1,
        "team": {
          "id": 57,
          "name": "Arsenal FC",
          "shortName": "Arsenal",
          "tla": "ARS",
          "crest": "https://crests.football-data.org/57.png"
        },
        "playedGames": 38,
        "form": "W,W,W,W,W",
        "won": 26,
        "draw": 7,
        "lost": 5,
        "points": 85,
        "goalsFor": 71,
        "goalsAgainst": 27,
        "goalDifference": 44
      },
      {
        "position": 2,
        "team": {
          "id": 65,
          "name": "Manchester City FC",
          "shortName": "Man City",
          "tla": "MCI",
          "crest": "https://crests.football-data.org/65.png"
        },
        "playedGames": 38,
        "form": "L,D,W,W,D",
        "won": 23,
        "draw": 9,
        "lost": 6,
        "points": 78,
        "goalsFor": 77,
        "goalsAgainst": 35,
        "goalDifference": 42
      },
      {
        "position": 3,
        "team": {
          "id": 66,
          "name": "Manchester United FC",
          "shortName": "Man United",
          "tla": "MUN",
          "crest": "https://crests.football-data.org/66.png"
        },
        "playedGames": 38,
        "form": "W,W,D,W,W",
        "won": 20,
        "draw": 11,
        "lost": 7,
        "points": 71,
        "goalsFor": 69,
        "goalsAgainst": 50,
        "goalDifference": 19
      },
      {
        "position": 4,
        "team": {
          "id": 58,
          "name": "Aston Villa FC",
          "shortName": "Aston Villa",
          "tla": "AVL",
          "crest": "https://crests.football-data.org/58.png"
        },
        "playedGames": 38,
        "form": "W,W,D,L,L",
        "won": 19,
        "draw": 8,
        "lost": 11,
        "points": 65,
        "goalsFor": 56,
        "goalsAgainst": 49,
        "goalDifference": 7
      },
      {
        "position": 5,
        "team": {
          "id": 64,
          "name": "Liverpool FC",
          "shortName": "Liverpool",
          "tla": "LIV",
          "crest": "https://crests.football-data.org/64.png"
        },
        "playedGames": 38,
        "form": "D,L,D,L,W",
        "won": 17,
        "draw": 9,
        "lost": 12,
        "points": 60,
        "goalsFor": 63,
        "goalsAgainst": 53,
        "goalDifference": 10
      },
      {
        "position": 6,
        "team": {
          "id": 1044,
          "name": "AFC Bournemouth",
          "shortName": "Bournemouth",
          "tla": "BOU",
          "crest": "https://crests.football-data.org/bournemouth.png"
        },
        "playedGames": 38,
        "form": "D,D,W,W,D",
        "won": 13,
        "draw": 18,
        "lost": 7,
        "points": 57,
        "goalsFor": 58,
        "goalsAgainst": 54,
        "goalDifference": 4
      },
      {
        "position": 7,
        "team": {
          "id": 71,
          "name": "Sunderland AFC",
          "shortName": "Sunderland",
          "tla": "SUN",
          "crest": "https://crests.football-data.org/71.png"
        },
        "playedGames": 38,
        "form": "W,W,D,D,L",
        "won": 14,
        "draw": 12,
        "lost": 12,
        "points": 54,
        "goalsFor": 42,
        "goalsAgainst": 48,
        "goalDifference": -6
      },
      {
        "position": 8,
        "team": {
          "id": 397,
          "name": "Brighton & Hove Albion FC",
          "shortName": "Brighton Hove",
          "tla": "BHA",
          "crest": "https://crests.football-data.org/397.png"
        },
        "playedGames": 38,
        "form": "L,L,W,L,W",
        "won": 14,
        "draw": 11,
        "lost": 13,
        "points": 53,
        "goalsFor": 52,
        "goalsAgainst": 46,
        "goalDifference": 6
      },
      {
        "position": 9,
        "team": {
          "id": 402,
          "name": "Brentford FC",
          "shortName": "Brentford",
          "tla": "BRE",
          "crest": "https://crests.football-data.org/402.png"
        },
        "playedGames": 38,
        "form": "D,D,L,W,L",
        "won": 14,
        "draw": 11,
        "lost": 13,
        "points": 53,
        "goalsFor": 55,
        "goalsAgainst": 52,
        "goalDifference": 3
      },
      {
        "position": 10,
        "team": {
          "id": 61,
          "name": "Chelsea FC",
          "shortName": "Chelsea",
          "tla": "CHE",
          "crest": "https://crests.football-data.org/61.png"
        },
        "playedGames": 38,
        "form": "L,W,D,L,L",
        "won": 14,
        "draw": 10,
        "lost": 14,
        "points": 52,
        "goalsFor": 58,
        "goalsAgainst": 52,
        "goalDifference": 6
      },
      {
        "position": 11,
        "team": {
          "id": 63,
          "name": "Fulham FC",
          "shortName": "Fulham",
          "tla": "FUL",
          "crest": "https://crests.football-data.org/63.png"
        },
        "playedGames": 38,
        "form": "W,D,L,L,W",
        "won": 15,
        "draw": 7,
        "lost": 16,
        "points": 52,
        "goalsFor": 47,
        "goalsAgainst": 51,
        "goalDifference": -4
      },
      {
        "position": 12,
        "team": {
          "id": 67,
          "name": "Newcastle United FC",
          "shortName": "Newcastle",
          "tla": "NEW",
          "crest": "https://crests.football-data.org/67.png"
        },
        "playedGames": 38,
        "form": "L,W,D,W,L",
        "won": 14,
        "draw": 7,
        "lost": 17,
        "points": 49,
        "goalsFor": 53,
        "goalsAgainst": 55,
        "goalDifference": -2
      },
      {
        "position": 13,
        "team": {
          "id": 62,
          "name": "Everton FC",
          "shortName": "Everton",
          "tla": "EVE",
          "crest": "https://crests.football-data.org/62.png"
        },
        "playedGames": 38,
        "form": "L,L,D,D,L",
        "won": 13,
        "draw": 10,
        "lost": 15,
        "points": 49,
        "goalsFor": 47,
        "goalsAgainst": 50,
        "goalDifference": -3
      },
      {
        "position": 14,
        "team": {
          "id": 341,
          "name": "Leeds United FC",
          "shortName": "Leeds United",
          "tla": "LEE",
          "crest": "https://crests.football-data.org/341.png"
        },
        "playedGames": 38,
        "form": "L,W,D,W,D",
        "won": 11,
        "draw": 14,
        "lost": 13,
        "points": 47,
        "goalsFor": 49,
        "goalsAgainst": 56,
        "goalDifference": -7
      },
      {
        "position": 15,
        "team": {
          "id": 354,
          "name": "Crystal Palace FC",
          "shortName": "Crystal Palace",
          "tla": "CRY",
          "crest": "https://crests.football-data.org/354.png"
        },
        "playedGames": 38,
        "form": "L,D,L,D,L",
        "won": 11,
        "draw": 12,
        "lost": 15,
        "points": 45,
        "goalsFor": 41,
        "goalsAgainst": 51,
        "goalDifference": -10
      },
      {
        "position": 16,
        "team": {
          "id": 351,
          "name": "Nottingham Forest FC",
          "shortName": "Nottingham",
          "tla": "NOT",
          "crest": "https://crests.football-data.org/351.png"
        },
        "playedGames": 38,
        "form": "D,L,D,W,W",
        "won": 11,
        "draw": 11,
        "lost": 16,
        "points": 44,
        "goalsFor": 48,
        "goalsAgainst": 51,
        "goalDifference": -3
      },
      {
        "position": 17,
        "team": {
          "id": 73,
          "name": "Tottenham Hotspur FC",
          "shortName": "Tottenham",
          "tla": "TOT",
          "crest": "https://crests.football-data.org/73.png"
        },
        "playedGames": 38,
        "form": "W,L,D,W,W",
        "won": 10,
        "draw": 11,
        "lost": 17,
        "points": 41,
        "goalsFor": 48,
        "goalsAgainst": 57,
        "goalDifference": -9
      },
      {
        "position": 18,
        "team": {
          "id": 563,
          "name": "West Ham United FC",
          "shortName": "West Ham",
          "tla": "WHU",
          "crest": "https://crests.football-data.org/563.png"
        },
        "playedGames": 38,
        "form": "W,L,L,L,W",
        "won": 10,
        "draw": 9,
        "lost": 19,
        "points": 39,
        "goalsFor": 46,
        "goalsAgainst": 65,
        "goalDifference": -19
      },
      {
        "position": 19,
        "team": {
          "id": 328,
          "name": "Burnley FC",
          "shortName": "Burnley",
          "tla": "BUR",
          "crest": "https://crests.football-data.org/328.png"
        },
        "playedGames": 38,
        "form": "D,L,D,L,L",
        "won": 4,
        "draw": 10,
        "lost": 24,
        "points": 22,
        "goalsFor": 38,
        "goalsAgainst": 75,
        "goalDifference": -37
      },
      {
        "position": 20,
        "team": {
          "id": 76,
          "name": "Wolverhampton Wanderers FC",
          "shortName": "Wolverhampton",
          "tla": "WOL",
          "crest": "https://crests.football-data.org/76.png"
        },
        "playedGames": 38,
        "form": "D,D,L,D,L",
        "won": 3,
        "draw": 11,
        "lost": 24,
        "points": 20,
        "goalsFor": 27,
        "goalsAgainst": 68,
        "goalDifference": -41
      }
    ]
  },
  {
    "stage": "REGULAR_SEASON",
    "type": "HOME",
    "group": null,
    "table": [
      {
        "position": 1,
        "team": {
          "id": 57,
          "name": "Arsenal FC",
          "shortName": "Arsenal",
          "tla": "ARS",
          "crest": "https://crests.football-data.org/57.png"
        },
        "playedGames": 19,
        "form": "",
        "won": 15,
        "draw": 2,
        "lost": 2,
        "points": 47,
        "goalsFor": 41,
        "goalsAgainst": 11,
        "goalDifference": 30
      },
      {
        "position": 2,
        "team": {
          "id": 65,
          "name": "Manchester City FC",
          "shortName": "Man City",
          "tla": "MCI",
          "crest": "https://crests.football-data.org/65.png"
        },
        "playedGames": 19,
        "form": "",
        "won": 14,
        "draw": 3,
        "lost": 2,
        "points": 45,
        "goalsFor": 45,
        "goalsAgainst": 14,
        "goalDifference": 31
      },
      {
        "position": 3,
        "team": {
          "id": 66,
          "name": "Manchester United FC",
          "shortName": "Man United",
          "tla": "MUN",
          "crest": "https://crests.football-data.org/66.png"
        },
        "playedGames": 19,
        "form": "",
        "won": 13,
        "draw": 3,
        "lost": 3,
        "points": 42,
        "goalsFor": 39,
        "goalsAgainst": 24,
        "goalDifference": 15
      },
      {
        "position": 4,
        "team": {
          "id": 58,
          "name": "Aston Villa FC",
          "shortName": "Aston Villa",
          "tla": "AVL",
          "crest": "https://crests.football-data.org/58.png"
        },
        "playedGames": 19,
        "form": "",
        "won": 12,
        "draw": 2,
        "lost": 5,
        "points": 38,
        "goalsFor": 32,
        "goalsAgainst": 22,
        "goalDifference": 10
      },
      {
        "position": 5,
        "team": {
          "id": 64,
          "name": "Liverpool FC",
          "shortName": "Liverpool",
          "tla": "LIV",
          "crest": "https://crests.football-data.org/64.png"
        },
        "playedGames": 19,
        "form": "",
        "won": 10,
        "draw": 6,
        "lost": 3,
        "points": 36,
        "goalsFor": 34,
        "goalsAgainst": 20,
        "goalDifference": 14
      },
      {
        "position": 6,
        "team": {
          "id": 63,
          "name": "Fulham FC",
          "shortName": "Fulham",
          "tla": "FUL",
          "crest": "https://crests.football-data.org/63.png"
        },
        "playedGames": 19,
        "form": "",
        "won": 11,
        "draw": 2,
        "lost": 6,
        "points": 35,
        "goalsFor": 30,
        "goalsAgainst": 20,
        "goalDifference": 10
      },
      {
        "position": 7,
        "team": {
          "id": 397,
          "name": "Brighton & Hove Albion FC",
          "shortName": "Brighton Hove",
          "tla": "BHA",
          "crest": "https://crests.football-data.org/397.png"
        },
        "playedGames": 19,
        "form": "",
        "won": 9,
        "draw": 6,
        "lost": 4,
        "points": 33,
        "goalsFor": 30,
        "goalsAgainst": 20,
        "goalDifference": 10
      },
      {
        "position": 8,
        "team": {
          "id": 71,
          "name": "Sunderland AFC",
          "shortName": "Sunderland",
          "tla": "SUN",
          "crest": "https://crests.football-data.org/71.png"
        },
        "playedGames": 19,
        "form": "",
        "won": 9,
        "draw": 6,
        "lost": 4,
        "points": 33,
        "goalsFor": 25,
        "goalsAgainst": 20,
        "goalDifference": 5
      },
      {
        "position": 9,
        "team": {
          "id": 402,
          "name": "Brentford FC",
          "shortName": "Brentford",
          "tla": "BRE",
          "crest": "https://crests.football-data.org/402.png"
        },
        "playedGames": 19,
        "form": "",
        "won": 8,
        "draw": 8,
        "lost": 3,
        "points": 32,
        "goalsFor": 33,
        "goalsAgainst": 21,
        "goalDifference": 12
      },
      {
        "position": 10,
        "team": {
          "id": 341,
          "name": "Leeds United FC",
          "shortName": "Leeds United",
          "tla": "LEE",
          "crest": "https://crests.football-data.org/341.png"
        },
        "playedGames": 19,
        "form": "",
        "won": 9,
        "draw": 5,
        "lost": 5,
        "points": 32,
        "goalsFor": 29,
        "goalsAgainst": 21,
        "goalDifference": 8
      },
      {
        "position": 11,
        "team": {
          "id": 67,
          "name": "Newcastle United FC",
          "shortName": "Newcastle",
          "tla": "NEW",
          "crest": "https://crests.football-data.org/67.png"
        },
        "playedGames": 19,
        "form": "",
        "won": 10,
        "draw": 2,
        "lost": 7,
        "points": 32,
        "goalsFor": 36,
        "goalsAgainst": 30,
        "goalDifference": 6
      },
      {
        "position": 12,
        "team": {
          "id": 1044,
          "name": "AFC Bournemouth",
          "shortName": "Bournemouth",
          "tla": "BOU",
          "crest": "https://crests.football-data.org/bournemouth.png"
        },
        "playedGames": 19,
        "form": "",
        "won": 7,
        "draw": 10,
        "lost": 2,
        "points": 31,
        "goalsFor": 29,
        "goalsAgainst": 20,
        "goalDifference": 9
      },
      {
        "position": 13,
        "team": {
          "id": 61,
          "name": "Chelsea FC",
          "shortName": "Chelsea",
          "tla": "CHE",
          "crest": "https://crests.football-data.org/61.png"
        },
        "playedGames": 19,
        "form": "",
        "won": 7,
        "draw": 5,
        "lost": 7,
        "points": 26,
        "goalsFor": 26,
        "goalsAgainst": 25,
        "goalDifference": 1
      },
      {
        "position": 14,
        "team": {
          "id": 62,
          "name": "Everton FC",
          "shortName": "Everton",
          "tla": "EVE",
          "crest": "https://crests.football-data.org/62.png"
        },
        "playedGames": 19,
        "form": "",
        "won": 6,
        "draw": 5,
        "lost": 8,
        "points": 23,
        "goalsFor": 26,
        "goalsAgainst": 27,
        "goalDifference": -1
      },
      {
        "position": 15,
        "team": {
          "id": 563,
          "name": "West Ham United FC",
          "shortName": "West Ham",
          "tla": "WHU",
          "crest": "https://crests.football-data.org/563.png"
        },
        "playedGames": 19,
        "form": "",
        "won": 6,
        "draw": 4,
        "lost": 9,
        "points": 22,
        "goalsFor": 27,
        "goalsAgainst": 30,
        "goalDifference": -3
      },
      {
        "position": 16,
        "team": {
          "id": 354,
          "name": "Crystal Palace FC",
          "shortName": "Crystal Palace",
          "tla": "CRY",
          "crest": "https://crests.football-data.org/354.png"
        },
        "playedGames": 19,
        "form": "",
        "won": 4,
        "draw": 9,
        "lost": 6,
        "points": 21,
        "goalsFor": 19,
        "goalsAgainst": 23,
        "goalDifference": -4
      },
      {
        "position": 17,
        "team": {
          "id": 351,
          "name": "Nottingham Forest FC",
          "shortName": "Nottingham",
          "tla": "NOT",
          "crest": "https://crests.football-data.org/351.png"
        },
        "playedGames": 19,
        "form": "",
        "won": 4,
        "draw": 8,
        "lost": 7,
        "points": 20,
        "goalsFor": 20,
        "goalsAgainst": 23,
        "goalDifference": -3
      },
      {
        "position": 18,
        "team": {
          "id": 73,
          "name": "Tottenham Hotspur FC",
          "shortName": "Tottenham",
          "tla": "TOT",
          "crest": "https://crests.football-data.org/73.png"
        },
        "playedGames": 19,
        "form": "",
        "won": 3,
        "draw": 6,
        "lost": 10,
        "points": 15,
        "goalsFor": 22,
        "goalsAgainst": 31,
        "goalDifference": -9
      },
      {
        "position": 19,
        "team": {
          "id": 76,
          "name": "Wolverhampton Wanderers FC",
          "shortName": "Wolverhampton",
          "tla": "WOL",
          "crest": "https://crests.football-data.org/76.png"
        },
        "playedGames": 19,
        "form": "",
        "won": 3,
        "draw": 5,
        "lost": 11,
        "points": 14,
        "goalsFor": 19,
        "goalsAgainst": 34,
        "goalDifference": -15
      },
      {
        "position": 20,
        "team": {
          "id": 328,
          "name": "Burnley FC",
          "shortName": "Burnley",
          "tla": "BUR",
          "crest": "https://crests.football-data.org/328.png"
        },
        "playedGames": 19,
        "form": "",
        "won": 2,
        "draw": 7,
        "lost": 10,
        "points": 13,
        "goalsFor": 18,
        "goalsAgainst": 29,
        "goalDifference": -11
      }
    ]
  }
]
```

---

## 6. Initial Investigation

### Data availability

- [ ] Does this endpoint contain the data we expected?
- [ ] Is the previous Premier League season fully represented?
- [ ] Are there missing or null fields?
- [ ] Is pagination present?
- [ ] Are there API-specific limits?

### Data modelling

- [ ] What are the stable identifiers?
- [ ] Which fields represent entities?
- [ ] Which fields represent relationships?
- [ ] Which nested objects should become separate entities/tables?
- [ ] Which fields overlap with the other API?
- [ ] Which fields are unique to this source?

### Pipeline relevance

- [ ] Is this endpoint required?
- [ ] Is this endpoint a source of truth for any canonical field?
- [ ] Does it need to be called once per season?
- [ ] Does it need to be called once per team?
- [ ] Does it need to be called once per match?
- [ ] How many requests would a complete season require?
- [ ] Can the response be cached and reused?

### Cross-source mapping

- [ ] What provider IDs need canonical mapping?
- [ ] Can entities be matched deterministically?
- [ ] Are there naming differences between providers?
- [ ] Are there provider-specific fields we need to preserve?

### Decisions / observations

_Add conclusions here after inspecting this endpoint._


---

# Endpoint: `competitions/PL/scorers`

## 1. Request

| Property | Value |
|---|---|
| Source | `football-data.org` |
| Endpoint | `competitions/PL/scorers` |
| Method | `GET` |
| URL | `https://api.football-data.org/v4/competitions/PL/scorers/` |
| HTTP Status | `200` |
| Captured At | `2026-08-11T08:19:14.768299+00:00` |
| Raw Response | `raw/football-data/competitions/PL/scorers.json` |

### Query Parameters

| Parameter | Value |
|---|---|
| `season` | `2025` |

### Notes

Premier League 2025/26 season.
Initial investigation of the fixtures endpoint.

---

## 2. Response Metadata

- **Count:** `10`

---

## 3. Record Counts

- `scorers`: **10 records**

---

## 4. Response Structure

The following structure is automatically derived from the
complete JSON response.

| JSON Path | Type |
|---|---|
| `$.count` | `integer` |
| `$.filters` | `object` |
| `$.filters.season` | `integer` |
| `$.filters.limit` | `integer` |
| `$.competition` | `object` |
| `$.competition.id` | `integer` |
| `$.competition.name` | `string` |
| `$.competition.code` | `string` |
| `$.competition.type` | `string` |
| `$.competition.emblem` | `string` |
| `$.season` | `object` |
| `$.season.id` | `integer` |
| `$.season.startDate` | `string` |
| `$.season.endDate` | `string` |
| `$.season.currentMatchday` | `integer` |
| `$.season.winner` | `null` |
| `$.scorers` | `array` |
| `$.scorers[]` | `object` |
| `$.scorers[].player` | `object` |
| `$.scorers[].player.id` | `integer` |
| `$.scorers[].player.name` | `string` |
| `$.scorers[].player.firstName` | `string` |
| `$.scorers[].player.lastName` | `string` |
| `$.scorers[].player.dateOfBirth` | `string` |
| `$.scorers[].player.nationality` | `string` |
| `$.scorers[].player.section` | `string` |
| `$.scorers[].player.position` | `null` |
| `$.scorers[].player.shirtNumber` | `null` |
| `$.scorers[].player.lastUpdated` | `string` |
| `$.scorers[].team` | `object` |
| `$.scorers[].team.id` | `integer` |
| `$.scorers[].team.name` | `string` |
| `$.scorers[].team.shortName` | `string` |
| `$.scorers[].team.tla` | `string` |
| `$.scorers[].team.crest` | `string` |
| `$.scorers[].team.address` | `string` |
| `$.scorers[].team.website` | `string` |
| `$.scorers[].team.founded` | `integer` |
| `$.scorers[].team.clubColors` | `string` |
| `$.scorers[].team.venue` | `string` |
| `$.scorers[].team.lastUpdated` | `string` |
| `$.scorers[].playedMatches` | `integer` |
| `$.scorers[].goals` | `integer` |
| `$.scorers[].assists` | `integer` |
| `$.scorers[].penalties` | `integer` |

---

## 5. Representative Response Examples

### `scorers`

Showing 2 representative record(s).

```json
[
  {
    "player": {
      "id": 38101,
      "name": "Erling Haaland",
      "firstName": "Erling",
      "lastName": "Haaland",
      "dateOfBirth": "2000-07-21",
      "nationality": "Norway",
      "section": "Offence",
      "position": null,
      "shirtNumber": null,
      "lastUpdated": "2026-06-01T11:16:30Z"
    },
    "team": {
      "id": 65,
      "name": "Manchester City FC",
      "shortName": "Man City",
      "tla": "MCI",
      "crest": "https://crests.football-data.org/65.png",
      "address": "SportCity Manchester M11 3FF",
      "website": "https://www.mancity.com",
      "founded": 1880,
      "clubColors": "Sky Blue / White",
      "venue": "Etihad Stadium",
      "lastUpdated": "2022-02-10T19:48:37Z"
    },
    "playedMatches": 36,
    "goals": 27,
    "assists": 8,
    "penalties": 3
  },
  {
    "player": {
      "id": 138230,
      "name": "Thiago",
      "firstName": "Igor Thiago",
      "lastName": "Thiago",
      "dateOfBirth": "2001-06-26",
      "nationality": "Brazil",
      "section": "Offence",
      "position": null,
      "shirtNumber": null,
      "lastUpdated": "2026-06-14T00:10:45Z"
    },
    "team": {
      "id": 402,
      "name": "Brentford FC",
      "shortName": "Brentford",
      "tla": "BRE",
      "crest": "https://crests.football-data.org/402.png",
      "address": "Braemar Road Brentford TW8 0NT",
      "website": "http://www.brentfordfc.co.uk",
      "founded": 1889,
      "clubColors": "Red / White / Black",
      "venue": "Griffin Park",
      "lastUpdated": "2022-04-03T16:24:00Z"
    },
    "playedMatches": 38,
    "goals": 22,
    "assists": 1,
    "penalties": 8
  }
]
```

---

## 6. Initial Investigation

### Data availability

- [ ] Does this endpoint contain the data we expected?
- [ ] Is the previous Premier League season fully represented?
- [ ] Are there missing or null fields?
- [ ] Is pagination present?
- [ ] Are there API-specific limits?

### Data modelling

- [ ] What are the stable identifiers?
- [ ] Which fields represent entities?
- [ ] Which fields represent relationships?
- [ ] Which nested objects should become separate entities/tables?
- [ ] Which fields overlap with the other API?
- [ ] Which fields are unique to this source?

### Pipeline relevance

- [ ] Is this endpoint required?
- [ ] Is this endpoint a source of truth for any canonical field?
- [ ] Does it need to be called once per season?
- [ ] Does it need to be called once per team?
- [ ] Does it need to be called once per match?
- [ ] How many requests would a complete season require?
- [ ] Can the response be cached and reused?

### Cross-source mapping

- [ ] What provider IDs need canonical mapping?
- [ ] Can entities be matched deterministically?
- [ ] Are there naming differences between providers?
- [ ] Are there provider-specific fields we need to preserve?

### Decisions / observations

_Add conclusions here after inspecting this endpoint._


---

# Endpoint: `competitions/PL/matches`

## 1. Request

| Property | Value |
|---|---|
| Source | `football-data.org` |
| Endpoint | `competitions/PL/matches` |
| Method | `GET` |
| URL | `https://api.football-data.org/v4/competitions/PL/matches/` |
| HTTP Status | `200` |
| Captured At | `2026-08-11T08:24:44.185925+00:00` |
| Raw Response | `raw/football-data/competitions/PL/matches.json` |

### Query Parameters

| Parameter | Value |
|---|---|
| `season` | `2025` |
| `matchday` | `38` |
| `status` | `FINISHED` |

### Notes

Premier League 2025/26 season.
Initial investigation of the fixtures endpoint.

---

## 2. Response Metadata

_No standard response metadata detected._

---

## 3. Record Counts

- `matches`: **10 records**

---

## 4. Response Structure

The following structure is automatically derived from the
complete JSON response.

| JSON Path | Type |
|---|---|
| `$.filters` | `object` |
| `$.filters.season` | `integer` |
| `$.filters.status` | `array` |
| `$.filters.status[]` | `string` |
| `$.filters.matchday` | `string` |
| `$.resultSet` | `object` |
| `$.resultSet.count` | `integer` |
| `$.resultSet.first` | `string` |
| `$.resultSet.last` | `string` |
| `$.resultSet.played` | `integer` |
| `$.competition` | `object` |
| `$.competition.id` | `integer` |
| `$.competition.name` | `string` |
| `$.competition.code` | `string` |
| `$.competition.type` | `string` |
| `$.competition.emblem` | `string` |
| `$.matches` | `array` |
| `$.matches[]` | `object` |
| `$.matches[].area` | `object` |
| `$.matches[].area.id` | `integer` |
| `$.matches[].area.name` | `string` |
| `$.matches[].area.code` | `string` |
| `$.matches[].area.flag` | `string` |
| `$.matches[].competition` | `object` |
| `$.matches[].competition.id` | `integer` |
| `$.matches[].competition.name` | `string` |
| `$.matches[].competition.code` | `string` |
| `$.matches[].competition.type` | `string` |
| `$.matches[].competition.emblem` | `string` |
| `$.matches[].season` | `object` |
| `$.matches[].season.id` | `integer` |
| `$.matches[].season.startDate` | `string` |
| `$.matches[].season.endDate` | `string` |
| `$.matches[].season.currentMatchday` | `integer` |
| `$.matches[].season.winner` | `null` |
| `$.matches[].id` | `integer` |
| `$.matches[].utcDate` | `string` |
| `$.matches[].status` | `string` |
| `$.matches[].matchday` | `integer` |
| `$.matches[].stage` | `string` |
| `$.matches[].group` | `null` |
| `$.matches[].lastUpdated` | `string` |
| `$.matches[].homeTeam` | `object` |
| `$.matches[].homeTeam.id` | `integer` |
| `$.matches[].homeTeam.name` | `string` |
| `$.matches[].homeTeam.shortName` | `string` |
| `$.matches[].homeTeam.tla` | `string` |
| `$.matches[].homeTeam.crest` | `string` |
| `$.matches[].awayTeam` | `object` |
| `$.matches[].awayTeam.id` | `integer` |
| `$.matches[].awayTeam.name` | `string` |
| `$.matches[].awayTeam.shortName` | `string` |
| `$.matches[].awayTeam.tla` | `string` |
| `$.matches[].awayTeam.crest` | `string` |
| `$.matches[].score` | `object` |
| `$.matches[].score.winner` | `string` |
| `$.matches[].score.duration` | `string` |
| `$.matches[].score.fullTime` | `object` |
| `$.matches[].score.fullTime.home` | `integer` |
| `$.matches[].score.fullTime.away` | `integer` |
| `$.matches[].score.halfTime` | `object` |
| `$.matches[].score.halfTime.home` | `integer` |
| `$.matches[].score.halfTime.away` | `integer` |
| `$.matches[].odds` | `object` |
| `$.matches[].odds.msg` | `string` |
| `$.matches[].referees` | `array` |
| `$.matches[].referees[]` | `object` |
| `$.matches[].referees[].id` | `integer` |
| `$.matches[].referees[].name` | `string` |
| `$.matches[].referees[].type` | `string` |
| `$.matches[].referees[].nationality` | `string` |

---

## 5. Representative Response Examples

### `matches`

Showing 2 representative record(s).

```json
[
  {
    "area": {
      "id": 2072,
      "name": "England",
      "code": "ENG",
      "flag": "https://crests.football-data.org/770.svg"
    },
    "competition": {
      "id": 2021,
      "name": "Premier League",
      "code": "PL",
      "type": "LEAGUE",
      "emblem": "https://crests.football-data.org/PL.png"
    },
    "season": {
      "id": 2403,
      "startDate": "2025-08-15",
      "endDate": "2026-05-24",
      "currentMatchday": 38,
      "winner": null
    },
    "id": 538155,
    "utcDate": "2026-05-24T15:00:00Z",
    "status": "FINISHED",
    "matchday": 38,
    "stage": "REGULAR_SEASON",
    "group": null,
    "lastUpdated": "2026-06-07T20:20:25Z",
    "homeTeam": {
      "id": 71,
      "name": "Sunderland AFC",
      "shortName": "Sunderland",
      "tla": "SUN",
      "crest": "https://crests.football-data.org/71.png"
    },
    "awayTeam": {
      "id": 61,
      "name": "Chelsea FC",
      "shortName": "Chelsea",
      "tla": "CHE",
      "crest": "https://crests.football-data.org/61.png"
    },
    "score": {
      "winner": "HOME_TEAM",
      "duration": "REGULAR",
      "fullTime": {
        "home": 2,
        "away": 1
      },
      "halfTime": {
        "home": 1,
        "away": 0
      }
    },
    "odds": {
      "msg": "Activate Odds-Package in User-Panel to retrieve odds."
    },
    "referees": [
      {
        "id": 11443,
        "name": "Chris Kavanagh",
        "type": "REFEREE",
        "nationality": "England"
      }
    ]
  },
  {
    "area": {
      "id": 2072,
      "name": "England",
      "code": "ENG",
      "flag": "https://crests.football-data.org/770.svg"
    },
    "competition": {
      "id": 2021,
      "name": "Premier League",
      "code": "PL",
      "type": "LEAGUE",
      "emblem": "https://crests.football-data.org/PL.png"
    },
    "season": {
      "id": 2403,
      "startDate": "2025-08-15",
      "endDate": "2026-05-24",
      "currentMatchday": 38,
      "winner": null
    },
    "id": 538156,
    "utcDate": "2026-05-24T15:00:00Z",
    "status": "FINISHED",
    "matchday": 38,
    "stage": "REGULAR_SEASON",
    "group": null,
    "lastUpdated": "2026-06-07T20:20:25Z",
    "homeTeam": {
      "id": 397,
      "name": "Brighton & Hove Albion FC",
      "shortName": "Brighton Hove",
      "tla": "BHA",
      "crest": "https://crests.football-data.org/397.png"
    },
    "awayTeam": {
      "id": 66,
      "name": "Manchester United FC",
      "shortName": "Man United",
      "tla": "MUN",
      "crest": "https://crests.football-data.org/66.png"
    },
    "score": {
      "winner": "AWAY_TEAM",
      "duration": "REGULAR",
      "fullTime": {
        "home": 0,
        "away": 3
      },
      "halfTime": {
        "home": 0,
        "away": 2
      }
    },
    "odds": {
      "msg": "Activate Odds-Package in User-Panel to retrieve odds."
    },
    "referees": [
      {
        "id": 213813,
        "name": "Sam Barrott",
        "type": "REFEREE",
        "nationality": "England"
      }
    ]
  }
]
```

---

## 6. Initial Investigation

### Data availability

- [ ] Does this endpoint contain the data we expected?
- [ ] Is the previous Premier League season fully represented?
- [ ] Are there missing or null fields?
- [ ] Is pagination present?
- [ ] Are there API-specific limits?

### Data modelling

- [ ] What are the stable identifiers?
- [ ] Which fields represent entities?
- [ ] Which fields represent relationships?
- [ ] Which nested objects should become separate entities/tables?
- [ ] Which fields overlap with the other API?
- [ ] Which fields are unique to this source?

### Pipeline relevance

- [ ] Is this endpoint required?
- [ ] Is this endpoint a source of truth for any canonical field?
- [ ] Does it need to be called once per season?
- [ ] Does it need to be called once per team?
- [ ] Does it need to be called once per match?
- [ ] How many requests would a complete season require?
- [ ] Can the response be cached and reused?

### Cross-source mapping

- [ ] What provider IDs need canonical mapping?
- [ ] Can entities be matched deterministically?
- [ ] Are there naming differences between providers?
- [ ] Are there provider-specific fields we need to preserve?

### Decisions / observations

_Add conclusions here after inspecting this endpoint._


---

# Endpoint: `matches`

## 1. Request

| Property | Value |
|---|---|
| Source | `football-data.org` |
| Endpoint | `matches` |
| Method | `GET` |
| URL | `https://api.football-data.org/v4/matches/` |
| HTTP Status | `200` |
| Captured At | `2026-08-11T08:29:23.610744+00:00` |
| Raw Response | `raw/football-data/matches/matches.json` |

### Query Parameters

| Parameter | Value |
|---|---|
| `ids` | `538156` |
| `date` | `2026-05-24` |
| `status` | `FINISHED` |

### Notes

Premier League 2025/26 season.
Initial investigation of the fixtures endpoint.

---

## 2. Response Metadata

_No standard response metadata detected._

---

## 3. Record Counts

- `matches`: **1 records**

---

## 4. Response Structure

The following structure is automatically derived from the
complete JSON response.

| JSON Path | Type |
|---|---|
| `$.filters` | `object` |
| `$.filters.permission` | `string` |
| `$.filters.status` | `array` |
| `$.filters.status[]` | `string` |
| `$.resultSet` | `object` |
| `$.resultSet.count` | `integer` |
| `$.resultSet.competitions` | `string` |
| `$.resultSet.first` | `string` |
| `$.resultSet.last` | `string` |
| `$.resultSet.played` | `integer` |
| `$.matches` | `array` |
| `$.matches[]` | `object` |
| `$.matches[].area` | `object` |
| `$.matches[].area.id` | `integer` |
| `$.matches[].area.name` | `string` |
| `$.matches[].area.code` | `string` |
| `$.matches[].area.flag` | `string` |
| `$.matches[].competition` | `object` |
| `$.matches[].competition.id` | `integer` |
| `$.matches[].competition.name` | `string` |
| `$.matches[].competition.code` | `string` |
| `$.matches[].competition.type` | `string` |
| `$.matches[].competition.emblem` | `string` |
| `$.matches[].season` | `object` |
| `$.matches[].season.id` | `integer` |
| `$.matches[].season.startDate` | `string` |
| `$.matches[].season.endDate` | `string` |
| `$.matches[].season.currentMatchday` | `integer` |
| `$.matches[].season.winner` | `null` |
| `$.matches[].id` | `integer` |
| `$.matches[].utcDate` | `string` |
| `$.matches[].status` | `string` |
| `$.matches[].matchday` | `integer` |
| `$.matches[].stage` | `string` |
| `$.matches[].group` | `null` |
| `$.matches[].lastUpdated` | `string` |
| `$.matches[].homeTeam` | `object` |
| `$.matches[].homeTeam.id` | `integer` |
| `$.matches[].homeTeam.name` | `string` |
| `$.matches[].homeTeam.shortName` | `string` |
| `$.matches[].homeTeam.tla` | `string` |
| `$.matches[].homeTeam.crest` | `string` |
| `$.matches[].awayTeam` | `object` |
| `$.matches[].awayTeam.id` | `integer` |
| `$.matches[].awayTeam.name` | `string` |
| `$.matches[].awayTeam.shortName` | `string` |
| `$.matches[].awayTeam.tla` | `string` |
| `$.matches[].awayTeam.crest` | `string` |
| `$.matches[].score` | `object` |
| `$.matches[].score.winner` | `string` |
| `$.matches[].score.duration` | `string` |
| `$.matches[].score.fullTime` | `object` |
| `$.matches[].score.fullTime.home` | `integer` |
| `$.matches[].score.fullTime.away` | `integer` |
| `$.matches[].score.halfTime` | `object` |
| `$.matches[].score.halfTime.home` | `integer` |
| `$.matches[].score.halfTime.away` | `integer` |
| `$.matches[].odds` | `object` |
| `$.matches[].odds.msg` | `string` |
| `$.matches[].referees` | `array` |
| `$.matches[].referees[]` | `object` |
| `$.matches[].referees[].id` | `integer` |
| `$.matches[].referees[].name` | `string` |
| `$.matches[].referees[].type` | `string` |
| `$.matches[].referees[].nationality` | `string` |

---

## 5. Representative Response Examples

### `matches`

Showing 1 representative record(s).

```json
[
  {
    "area": {
      "id": 2072,
      "name": "England",
      "code": "ENG",
      "flag": "https://crests.football-data.org/770.svg"
    },
    "competition": {
      "id": 2021,
      "name": "Premier League",
      "code": "PL",
      "type": "LEAGUE",
      "emblem": "https://crests.football-data.org/PL.png"
    },
    "season": {
      "id": 2403,
      "startDate": "2025-08-15",
      "endDate": "2026-05-24",
      "currentMatchday": 38,
      "winner": null
    },
    "id": 538156,
    "utcDate": "2026-05-24T15:00:00Z",
    "status": "FINISHED",
    "matchday": 38,
    "stage": "REGULAR_SEASON",
    "group": null,
    "lastUpdated": "2026-06-07T20:20:25Z",
    "homeTeam": {
      "id": 397,
      "name": "Brighton & Hove Albion FC",
      "shortName": "Brighton Hove",
      "tla": "BHA",
      "crest": "https://crests.football-data.org/397.png"
    },
    "awayTeam": {
      "id": 66,
      "name": "Manchester United FC",
      "shortName": "Man United",
      "tla": "MUN",
      "crest": "https://crests.football-data.org/66.png"
    },
    "score": {
      "winner": "AWAY_TEAM",
      "duration": "REGULAR",
      "fullTime": {
        "home": 0,
        "away": 3
      },
      "halfTime": {
        "home": 0,
        "away": 2
      }
    },
    "odds": {
      "msg": "Activate Odds-Package in User-Panel to retrieve odds."
    },
    "referees": [
      {
        "id": 213813,
        "name": "Sam Barrott",
        "type": "REFEREE",
        "nationality": "England"
      }
    ]
  }
]
```

---

## 6. Initial Investigation

### Data availability

- [ ] Does this endpoint contain the data we expected?
- [ ] Is the previous Premier League season fully represented?
- [ ] Are there missing or null fields?
- [ ] Is pagination present?
- [ ] Are there API-specific limits?

### Data modelling

- [ ] What are the stable identifiers?
- [ ] Which fields represent entities?
- [ ] Which fields represent relationships?
- [ ] Which nested objects should become separate entities/tables?
- [ ] Which fields overlap with the other API?
- [ ] Which fields are unique to this source?

### Pipeline relevance

- [ ] Is this endpoint required?
- [ ] Is this endpoint a source of truth for any canonical field?
- [ ] Does it need to be called once per season?
- [ ] Does it need to be called once per team?
- [ ] Does it need to be called once per match?
- [ ] How many requests would a complete season require?
- [ ] Can the response be cached and reused?

### Cross-source mapping

- [ ] What provider IDs need canonical mapping?
- [ ] Can entities be matched deterministically?
- [ ] Are there naming differences between providers?
- [ ] Are there provider-specific fields we need to preserve?

### Decisions / observations

_Add conclusions here after inspecting this endpoint._


---

# Endpoint: `teams`

## 1. Request

| Property | Value |
|---|---|
| Source | `football-data.org` |
| Endpoint | `teams` |
| Method | `GET` |
| URL | `https://api.football-data.org/v4/teams/66` |
| HTTP Status | `200` |
| Captured At | `2026-08-11T08:37:24.887569+00:00` |
| Raw Response | `raw/football-data/teams/teams.json` |

### Query Parameters

| Parameter | Value |
|---|---|
| `ids` | `538156` |
| `date` | `2026-05-24` |
| `status` | `FINISHED` |

### Notes

Premier League 2025/26 season.
Initial investigation of the fixtures endpoint.

---

## 2. Response Metadata

_No standard response metadata detected._

---

## 3. Record Counts

- `runningCompetitions`: **1 records**
- `squad`: **38 records**
- `staff`: **0 records**

---

## 4. Response Structure

The following structure is automatically derived from the
complete JSON response.

| JSON Path | Type |
|---|---|
| `$.area` | `object` |
| `$.area.id` | `integer` |
| `$.area.name` | `string` |
| `$.area.code` | `string` |
| `$.area.flag` | `string` |
| `$.id` | `integer` |
| `$.name` | `string` |
| `$.shortName` | `string` |
| `$.tla` | `string` |
| `$.crest` | `string` |
| `$.address` | `string` |
| `$.website` | `string` |
| `$.founded` | `integer` |
| `$.clubColors` | `string` |
| `$.venue` | `string` |
| `$.runningCompetitions` | `array` |
| `$.runningCompetitions[]` | `object` |
| `$.runningCompetitions[].id` | `integer` |
| `$.runningCompetitions[].name` | `string` |
| `$.runningCompetitions[].code` | `string` |
| `$.runningCompetitions[].type` | `string` |
| `$.runningCompetitions[].emblem` | `string` |
| `$.coach` | `object` |
| `$.coach.id` | `null` |
| `$.coach.firstName` | `null` |
| `$.coach.lastName` | `null` |
| `$.coach.name` | `null` |
| `$.coach.dateOfBirth` | `null` |
| `$.coach.nationality` | `null` |
| `$.coach.contract` | `object` |
| `$.coach.contract.start` | `null` |
| `$.coach.contract.until` | `null` |
| `$.squad` | `array` |
| `$.squad[]` | `object` |
| `$.squad[].id` | `integer` |
| `$.squad[].name` | `string` |
| `$.squad[].position` | `string` |
| `$.squad[].dateOfBirth` | `string` |
| `$.squad[].nationality` | `string` |
| `$.staff` | `array` |
| `$.lastUpdated` | `string` |

---

## 5. Representative Response Examples

### `runningCompetitions`

Showing 1 representative record(s).

```json
[
  {
    "id": 2021,
    "name": "Premier League",
    "code": "PL",
    "type": "LEAGUE",
    "emblem": "https://crests.football-data.org/PL.png"
  }
]
```

---

## 6. Initial Investigation

### Data availability

- [ ] Does this endpoint contain the data we expected?
- [ ] Is the previous Premier League season fully represented?
- [ ] Are there missing or null fields?
- [ ] Is pagination present?
- [ ] Are there API-specific limits?

### Data modelling

- [ ] What are the stable identifiers?
- [ ] Which fields represent entities?
- [ ] Which fields represent relationships?
- [ ] Which nested objects should become separate entities/tables?
- [ ] Which fields overlap with the other API?
- [ ] Which fields are unique to this source?

### Pipeline relevance

- [ ] Is this endpoint required?
- [ ] Is this endpoint a source of truth for any canonical field?
- [ ] Does it need to be called once per season?
- [ ] Does it need to be called once per team?
- [ ] Does it need to be called once per match?
- [ ] How many requests would a complete season require?
- [ ] Can the response be cached and reused?

### Cross-source mapping

- [ ] What provider IDs need canonical mapping?
- [ ] Can entities be matched deterministically?
- [ ] Are there naming differences between providers?
- [ ] Are there provider-specific fields we need to preserve?

### Decisions / observations

_Add conclusions here after inspecting this endpoint._

