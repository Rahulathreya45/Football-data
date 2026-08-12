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
