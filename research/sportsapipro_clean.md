# sportsapipro.com — API Investigation

## Project Context

- **Focus:** Premier League
- **Season:** 2025/26
- **Purpose:** Investigate API response structures and determine
  which data is useful for the football data pipeline.
- **Raw responses:** Stored separately as JSON files.

This document contains the investigation of multiple endpoints
from `sportsapipro.com`.

---

# Endpoint: `seasons`

## 1. Request

| Property | Value |
|---|---|
| Source | `sportsapipro.com` |
| Endpoint | `seasons` |
| Method | `GET` |
| URL | `https://api.sportsapipro.com/v2/football/api/tournaments/17/seasons` |
| HTTP Status | `200` |
| Captured At | `2026-08-11T12:28:50.097567+00:00` |
| Raw Response | `raw/sportsapipro/seasons/seasons.json` |

### Query Parameters

_No query parameters._

## 2. Response Metadata

_No standard response metadata detected._

---

## 3. Record Counts

- `seasons`: **35 records**

---

## 4. Response Structure

The following structure is automatically derived from the
complete JSON response.

| JSON Path | Type |
|---|---|
| `$.success` | `boolean` |
| `$.source` | `string` |
| `$.tournamentId` | `integer` |
| `$.seasons` | `array` |
| `$.seasons[]` | `object` |
| `$.seasons[].id` | `integer` |
| `$.seasons[].name` | `string` |
| `$.seasons[].year` | `string` |
| `$.seasons[].tournamentId` | `integer` |
| `$.timezone` | `object` |
| `$.timezone.name` | `string` |
| `$.timezone.utcOffset` | `string` |
| `$.timezone.source` | `string` |
| `$.timezone.country` | `string` |

---

## 1. Request

| Property | Value |
|---|---|
| Source | `sportsapipro.com` |
| Endpoint | `seasons/standings` |
| Method | `GET` |
| URL | `https://api.sportsapipro.com/v2/football/tournament/17/season/76986/standings` |
| HTTP Status | `200` |
| Captured At | `2026-08-12T03:55:26.041174+00:00` |
| Raw Response | `raw/sportsapipro/seasons/standings.json` |

### Query Parameters

_No query parameters._

## 2. Response Metadata

_No standard response metadata detected._

---

## 3. Record Counts

- `standings`: **20 records**

---

## 4. Response Structure

The following structure is automatically derived from the
complete JSON response.

| JSON Path | Type |
|---|---|
| `$.success` | `boolean` |
| `$.tournamentId` | `string` |
| `$.seasonId` | `string` |
| `$.totalTeams` | `integer` |
| `$.standings` | `array` |
| `$.standings[]` | `object` |
| `$.standings[].position` | `integer` |
| `$.standings[].teamId` | `integer` |
| `$.standings[].teamName` | `string` |
| `$.standings[].played` | `integer` |
| `$.standings[].won` | `integer` |
| `$.standings[].drawn` | `integer` |
| `$.standings[].lost` | `integer` |
| `$.standings[].goalsFor` | `integer` |
| `$.standings[].goalsAgainst` | `integer` |
| `$.standings[].points` | `integer` |
| `$.source` | `string` |
| `$.timezone` | `object` |
| `$.timezone.name` | `string` |
| `$.timezone.utcOffset` | `string` |
| `$.timezone.source` | `string` |
| `$.timezone.country` | `string` |

---

## 1. Request

| Property | Value |
|---|---|
| Source | `sportsapipro.com` |
| Endpoint | `seasons/events` |
| Method | `GET` |
| URL | `https://api.sportsapipro.com/v2/football/tournament/17/season/76986/events/last/0` |
| HTTP Status | `200` |
| Captured At | `2026-08-12T03:57:29.992187+00:00` |
| Raw Response | `raw/sportsapipro/seasons/events.json` |

### Query Parameters

_No query parameters._

## 2. Response Metadata

_No standard response metadata detected._

---

## 3. Record Counts

_No top-level arrays detected._

---

## 4. Response Structure

The following structure is automatically derived from the
complete JSON response.

| JSON Path | Type |
|---|---|
| `$.success` | `boolean` |
| `$.data` | `object` |
| `$.data.events` | `array` |
| `$.data.events[]` | `object` |
| `$.data.events[].eventState` | `object` |
| `$.data.events[].tournament` | `object` |
| `$.data.events[].tournament.name` | `string` |
| `$.data.events[].tournament.slug` | `string` |
| `$.data.events[].tournament.category` | `object` |
| `$.data.events[].tournament.category.name` | `string` |
| `$.data.events[].tournament.category.slug` | `string` |
| `$.data.events[].tournament.category.sport` | `object` |
| `$.data.events[].tournament.category.sport.name` | `string` |
| `$.data.events[].tournament.category.sport.slug` | `string` |
| `$.data.events[].tournament.category.sport.id` | `integer` |
| `$.data.events[].tournament.category.priority` | `integer` |
| `$.data.events[].tournament.category.country` | `object` |
| `$.data.events[].tournament.category.country.alpha2` | `string` |
| `$.data.events[].tournament.category.country.alpha3` | `string` |
| `$.data.events[].tournament.category.country.name` | `string` |
| `$.data.events[].tournament.category.country.slug` | `string` |
| `$.data.events[].tournament.category.id` | `integer` |
| `$.data.events[].tournament.category.flag` | `string` |
| `$.data.events[].tournament.category.alpha2` | `string` |
| `$.data.events[].tournament.category.fieldTranslations` | `object` |
| `$.data.events[].tournament.category.fieldTranslations.nameTranslation` | `object` |
| `$.data.events[].tournament.category.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.events[].tournament.category.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.events[].tournament.category.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.events[].tournament.category.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.events[].tournament.category.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.events[].tournament.uniqueTournament` | `object` |
| `$.data.events[].tournament.uniqueTournament.name` | `string` |
| `$.data.events[].tournament.uniqueTournament.slug` | `string` |
| `$.data.events[].tournament.uniqueTournament.primaryColorHex` | `string` |
| `$.data.events[].tournament.uniqueTournament.secondaryColorHex` | `string` |
| `$.data.events[].tournament.uniqueTournament.category` | `object` |
| `$.data.events[].tournament.uniqueTournament.category.name` | `string` |
| `$.data.events[].tournament.uniqueTournament.category.slug` | `string` |
| `$.data.events[].tournament.uniqueTournament.category.sport` | `object` |
| `$.data.events[].tournament.uniqueTournament.category.sport.name` | `string` |
| `$.data.events[].tournament.uniqueTournament.category.sport.slug` | `string` |
| `$.data.events[].tournament.uniqueTournament.category.sport.id` | `integer` |
| `$.data.events[].tournament.uniqueTournament.category.priority` | `integer` |
| `$.data.events[].tournament.uniqueTournament.category.country` | `object` |
| `$.data.events[].tournament.uniqueTournament.category.country.alpha2` | `string` |
| `$.data.events[].tournament.uniqueTournament.category.country.alpha3` | `string` |
| `$.data.events[].tournament.uniqueTournament.category.country.name` | `string` |
| `$.data.events[].tournament.uniqueTournament.category.country.slug` | `string` |
| `$.data.events[].tournament.uniqueTournament.category.id` | `integer` |
| `$.data.events[].tournament.uniqueTournament.category.flag` | `string` |
| `$.data.events[].tournament.uniqueTournament.category.alpha2` | `string` |
| `$.data.events[].tournament.uniqueTournament.category.fieldTranslations` | `object` |
| `$.data.events[].tournament.uniqueTournament.category.fieldTranslations.nameTranslation` | `object` |
| `$.data.events[].tournament.uniqueTournament.category.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.events[].tournament.uniqueTournament.category.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.events[].tournament.uniqueTournament.category.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.events[].tournament.uniqueTournament.category.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.events[].tournament.uniqueTournament.category.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.events[].tournament.uniqueTournament.userCount` | `integer` |
| `$.data.events[].tournament.uniqueTournament.hasPerformanceGraphFeature` | `boolean` |
| `$.data.events[].tournament.uniqueTournament.country` | `object` |
| `$.data.events[].tournament.uniqueTournament.id` | `integer` |
| `$.data.events[].tournament.uniqueTournament.hasEventPlayerStatistics` | `boolean` |
| `$.data.events[].tournament.uniqueTournament.displayInverseHomeAwayTeams` | `boolean` |
| `$.data.events[].tournament.uniqueTournament.fieldTranslations` | `object` |
| `$.data.events[].tournament.uniqueTournament.fieldTranslations.nameTranslation` | `object` |
| `$.data.events[].tournament.uniqueTournament.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.events[].tournament.uniqueTournament.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.events[].tournament.uniqueTournament.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.events[].tournament.uniqueTournament.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.events[].tournament.uniqueTournament.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.events[].tournament.priority` | `integer` |
| `$.data.events[].tournament.isGroup` | `boolean` |
| `$.data.events[].tournament.isLive` | `boolean` |
| `$.data.events[].tournament.id` | `integer` |
| `$.data.events[].tournament.fieldTranslations` | `object` |
| `$.data.events[].tournament.fieldTranslations.nameTranslation` | `object` |
| `$.data.events[].tournament.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.events[].tournament.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.events[].tournament.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.events[].tournament.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.events[].tournament.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.events[].season` | `object` |
| `$.data.events[].season.name` | `string` |
| `$.data.events[].season.year` | `string` |
| `$.data.events[].season.editor` | `boolean` |
| `$.data.events[].season.id` | `integer` |
| `$.data.events[].roundInfo` | `object` |
| `$.data.events[].roundInfo.round` | `integer` |
| `$.data.events[].customId` | `string` |
| `$.data.events[].status` | `object` |
| `$.data.events[].status.code` | `integer` |
| `$.data.events[].status.description` | `string` |
| `$.data.events[].status.type` | `string` |
| `$.data.events[].winnerCode` | `integer` |
| `$.data.events[].venue` | `object` |
| `$.data.events[].venue.city` | `object` |
| `$.data.events[].venue.city.name` | `string` |
| `$.data.events[].venue.city.country` | `object` |
| `$.data.events[].venue.city.country.alpha2` | `string` |
| `$.data.events[].venue.city.country.alpha3` | `string` |
| `$.data.events[].venue.city.country.name` | `string` |
| `$.data.events[].venue.city.country.slug` | `string` |
| `$.data.events[].venue.city.id` | `integer` |
| `$.data.events[].venue.venueCoordinates` | `object` |
| `$.data.events[].venue.venueCoordinates.latitude` | `number` |
| `$.data.events[].venue.venueCoordinates.longitude` | `number` |
| `$.data.events[].venue.hidden` | `boolean` |
| `$.data.events[].venue.slug` | `string` |
| `$.data.events[].venue.name` | `string` |
| `$.data.events[].venue.capacity` | `integer` |
| `$.data.events[].venue.country` | `object` |
| `$.data.events[].venue.country.alpha2` | `string` |
| `$.data.events[].venue.country.alpha3` | `string` |
| `$.data.events[].venue.country.name` | `string` |
| `$.data.events[].venue.country.slug` | `string` |
| `$.data.events[].venue.id` | `integer` |
| `$.data.events[].venue.fieldTranslations` | `object` |
| `$.data.events[].venue.fieldTranslations.nameTranslation` | `object` |
| `$.data.events[].venue.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.events[].venue.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.events[].venue.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.events[].venue.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.events[].venue.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.events[].venue.stadium` | `object` |
| `$.data.events[].venue.stadium.name` | `string` |
| `$.data.events[].venue.stadium.capacity` | `integer` |
| `$.data.events[].homeTeam` | `object` |
| `$.data.events[].homeTeam.name` | `string` |
| `$.data.events[].homeTeam.slug` | `string` |
| `$.data.events[].homeTeam.shortName` | `string` |
| `$.data.events[].homeTeam.gender` | `string` |
| `$.data.events[].homeTeam.sport` | `object` |
| `$.data.events[].homeTeam.sport.name` | `string` |
| `$.data.events[].homeTeam.sport.slug` | `string` |
| `$.data.events[].homeTeam.sport.id` | `integer` |
| `$.data.events[].homeTeam.userCount` | `integer` |
| `$.data.events[].homeTeam.nameCode` | `string` |
| `$.data.events[].homeTeam.disabled` | `boolean` |
| `$.data.events[].homeTeam.national` | `boolean` |
| `$.data.events[].homeTeam.type` | `integer` |
| `$.data.events[].homeTeam.country` | `object` |
| `$.data.events[].homeTeam.country.alpha2` | `string` |
| `$.data.events[].homeTeam.country.alpha3` | `string` |
| `$.data.events[].homeTeam.country.name` | `string` |
| `$.data.events[].homeTeam.country.slug` | `string` |
| `$.data.events[].homeTeam.id` | `integer` |
| `$.data.events[].homeTeam.subTeams` | `array` |
| `$.data.events[].homeTeam.teamColors` | `object` |
| `$.data.events[].homeTeam.teamColors.primary` | `string` |
| `$.data.events[].homeTeam.teamColors.secondary` | `string` |
| `$.data.events[].homeTeam.teamColors.text` | `string` |
| `$.data.events[].homeTeam.fieldTranslations` | `object` |
| `$.data.events[].homeTeam.fieldTranslations.nameTranslation` | `object` |
| `$.data.events[].homeTeam.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.events[].homeTeam.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.events[].homeTeam.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.events[].homeTeam.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.events[].homeTeam.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.events[].awayTeam` | `object` |
| `$.data.events[].awayTeam.name` | `string` |
| `$.data.events[].awayTeam.slug` | `string` |
| `$.data.events[].awayTeam.shortName` | `string` |
| `$.data.events[].awayTeam.gender` | `string` |
| `$.data.events[].awayTeam.sport` | `object` |
| `$.data.events[].awayTeam.sport.name` | `string` |
| `$.data.events[].awayTeam.sport.slug` | `string` |
| `$.data.events[].awayTeam.sport.id` | `integer` |
| `$.data.events[].awayTeam.userCount` | `integer` |
| `$.data.events[].awayTeam.nameCode` | `string` |
| `$.data.events[].awayTeam.disabled` | `boolean` |
| `$.data.events[].awayTeam.national` | `boolean` |
| `$.data.events[].awayTeam.type` | `integer` |
| `$.data.events[].awayTeam.country` | `object` |
| `$.data.events[].awayTeam.country.alpha2` | `string` |
| `$.data.events[].awayTeam.country.alpha3` | `string` |
| `$.data.events[].awayTeam.country.name` | `string` |
| `$.data.events[].awayTeam.country.slug` | `string` |
| `$.data.events[].awayTeam.id` | `integer` |
| `$.data.events[].awayTeam.subTeams` | `array` |
| `$.data.events[].awayTeam.teamColors` | `object` |
| `$.data.events[].awayTeam.teamColors.primary` | `string` |
| `$.data.events[].awayTeam.teamColors.secondary` | `string` |
| `$.data.events[].awayTeam.teamColors.text` | `string` |
| `$.data.events[].awayTeam.fieldTranslations` | `object` |
| `$.data.events[].awayTeam.fieldTranslations.nameTranslation` | `object` |
| `$.data.events[].awayTeam.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.events[].awayTeam.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.events[].awayTeam.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.events[].awayTeam.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.events[].awayTeam.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.events[].homeScore` | `object` |
| `$.data.events[].homeScore.current` | `integer` |
| `$.data.events[].homeScore.display` | `integer` |
| `$.data.events[].homeScore.period1` | `integer` |
| `$.data.events[].homeScore.period2` | `integer` |
| `$.data.events[].homeScore.normaltime` | `integer` |
| `$.data.events[].awayScore` | `object` |
| `$.data.events[].awayScore.current` | `integer` |
| `$.data.events[].awayScore.display` | `integer` |
| `$.data.events[].awayScore.period1` | `integer` |
| `$.data.events[].awayScore.period2` | `integer` |
| `$.data.events[].awayScore.normaltime` | `integer` |
| `$.data.events[].time` | `object` |
| `$.data.events[].time.injuryTime1` | `integer` |
| `$.data.events[].time.injuryTime2` | `integer` |
| `$.data.events[].time.currentPeriodStartTimestamp` | `integer` |
| `$.data.events[].changes` | `object` |
| `$.data.events[].changes.changes` | `array` |
| `$.data.events[].changes.changes[]` | `string` |
| `$.data.events[].changes.changeTimestamp` | `integer` |
| `$.data.events[].hasGlobalHighlights` | `boolean` |
| `$.data.events[].hasXg` | `boolean` |
| `$.data.events[].hasEventPlayerStatistics` | `boolean` |
| `$.data.events[].hasEventPlayerHeatMap` | `boolean` |
| `$.data.events[].detailId` | `integer` |
| `$.data.events[].crowdsourcingDataDisplayEnabled` | `boolean` |
| `$.data.events[].correctAiInsight` | `boolean` |
| `$.data.events[].correctHalftimeAiInsight` | `boolean` |
| `$.data.events[].id` | `integer` |
| `$.data.events[].homeRedCards` | `integer` |
| `$.data.events[].awayRedCards` | `integer` |
| `$.data.events[].slug` | `string` |
| `$.data.events[].startTimestamp` | `integer` |
| `$.data.events[].finalResultOnly` | `boolean` |
| `$.data.events[].feedLocked` | `boolean` |
| `$.data.events[].isEditor` | `boolean` |
| `$.data.events[].eventFilters` | `object` |
| `$.data.events[].eventFilters.category` | `array` |
| `$.data.events[].eventFilters.category[]` | `string` |
| `$.data.events[].eventFilters.level` | `array` |
| `$.data.events[].eventFilters.level[]` | `string` |
| `$.data.events[].eventFilters.gender` | `array` |
| `$.data.events[].eventFilters.gender[]` | `string` |
| `$.data.hasNextPage` | `boolean` |
| `$.source` | `string` |
| `$.cacheHit` | `boolean` |
| `$.timezone` | `object` |
| `$.timezone.name` | `string` |
| `$.timezone.utcOffset` | `string` |
| `$.timezone.source` | `string` |
| `$.timezone.country` | `string` |

---

## 1. Request

| Property | Value |
|---|---|
| Source | `sportsapipro.com` |
| Endpoint | `seasons/match` |
| Method | `GET` |
| URL | `https://api.sportsapipro.com/v2/football/match/14023935` |
| HTTP Status | `200` |
| Captured At | `2026-08-12T04:47:55.722403+00:00` |
| Raw Response | `raw/sportsapipro/seasons/match.json` |

### Query Parameters

_No query parameters._

## 2. Response Metadata

_No standard response metadata detected._

---

## 3. Record Counts

_No top-level arrays detected._

---

## 4. Response Structure

The following structure is automatically derived from the
complete JSON response.

| JSON Path | Type |
|---|---|
| `$.success` | `boolean` |
| `$.matchId` | `integer` |
| `$.source` | `string` |
| `$.match` | `object` |
| `$.match.eventState` | `object` |
| `$.match.tournament` | `object` |
| `$.match.tournament.name` | `string` |
| `$.match.tournament.slug` | `string` |
| `$.match.tournament.category` | `object` |
| `$.match.tournament.category.name` | `string` |
| `$.match.tournament.category.slug` | `string` |
| `$.match.tournament.category.sport` | `object` |
| `$.match.tournament.category.sport.name` | `string` |
| `$.match.tournament.category.sport.slug` | `string` |
| `$.match.tournament.category.sport.id` | `integer` |
| `$.match.tournament.category.priority` | `integer` |
| `$.match.tournament.category.country` | `object` |
| `$.match.tournament.category.country.alpha2` | `string` |
| `$.match.tournament.category.country.alpha3` | `string` |
| `$.match.tournament.category.country.name` | `string` |
| `$.match.tournament.category.country.slug` | `string` |
| `$.match.tournament.category.id` | `integer` |
| `$.match.tournament.category.flag` | `string` |
| `$.match.tournament.category.alpha2` | `string` |
| `$.match.tournament.category.fieldTranslations` | `object` |
| `$.match.tournament.category.fieldTranslations.nameTranslation` | `object` |
| `$.match.tournament.category.fieldTranslations.nameTranslation.ar` | `string` |
| `$.match.tournament.category.fieldTranslations.nameTranslation.hi` | `string` |
| `$.match.tournament.category.fieldTranslations.nameTranslation.bn` | `string` |
| `$.match.tournament.category.fieldTranslations.nameTranslation.ru` | `string` |
| `$.match.tournament.category.fieldTranslations.shortNameTranslation` | `object` |
| `$.match.tournament.uniqueTournament` | `object` |
| `$.match.tournament.uniqueTournament.name` | `string` |
| `$.match.tournament.uniqueTournament.slug` | `string` |
| `$.match.tournament.uniqueTournament.primaryColorHex` | `string` |
| `$.match.tournament.uniqueTournament.secondaryColorHex` | `string` |
| `$.match.tournament.uniqueTournament.category` | `object` |
| `$.match.tournament.uniqueTournament.category.name` | `string` |
| `$.match.tournament.uniqueTournament.category.slug` | `string` |
| `$.match.tournament.uniqueTournament.category.sport` | `object` |
| `$.match.tournament.uniqueTournament.category.sport.name` | `string` |
| `$.match.tournament.uniqueTournament.category.sport.slug` | `string` |
| `$.match.tournament.uniqueTournament.category.sport.id` | `integer` |
| `$.match.tournament.uniqueTournament.category.priority` | `integer` |
| `$.match.tournament.uniqueTournament.category.country` | `object` |
| `$.match.tournament.uniqueTournament.category.country.alpha2` | `string` |
| `$.match.tournament.uniqueTournament.category.country.alpha3` | `string` |
| `$.match.tournament.uniqueTournament.category.country.name` | `string` |
| `$.match.tournament.uniqueTournament.category.country.slug` | `string` |
| `$.match.tournament.uniqueTournament.category.id` | `integer` |
| `$.match.tournament.uniqueTournament.category.flag` | `string` |
| `$.match.tournament.uniqueTournament.category.alpha2` | `string` |
| `$.match.tournament.uniqueTournament.category.fieldTranslations` | `object` |
| `$.match.tournament.uniqueTournament.category.fieldTranslations.nameTranslation` | `object` |
| `$.match.tournament.uniqueTournament.category.fieldTranslations.nameTranslation.ar` | `string` |
| `$.match.tournament.uniqueTournament.category.fieldTranslations.nameTranslation.hi` | `string` |
| `$.match.tournament.uniqueTournament.category.fieldTranslations.nameTranslation.bn` | `string` |
| `$.match.tournament.uniqueTournament.category.fieldTranslations.nameTranslation.ru` | `string` |
| `$.match.tournament.uniqueTournament.category.fieldTranslations.shortNameTranslation` | `object` |
| `$.match.tournament.uniqueTournament.userCount` | `integer` |
| `$.match.tournament.uniqueTournament.hasRounds` | `boolean` |
| `$.match.tournament.uniqueTournament.hasPerformanceGraphFeature` | `boolean` |
| `$.match.tournament.uniqueTournament.country` | `object` |
| `$.match.tournament.uniqueTournament.id` | `integer` |
| `$.match.tournament.uniqueTournament.hasEventPlayerStatistics` | `boolean` |
| `$.match.tournament.uniqueTournament.displayInverseHomeAwayTeams` | `boolean` |
| `$.match.tournament.uniqueTournament.fieldTranslations` | `object` |
| `$.match.tournament.uniqueTournament.fieldTranslations.nameTranslation` | `object` |
| `$.match.tournament.uniqueTournament.fieldTranslations.nameTranslation.ar` | `string` |
| `$.match.tournament.uniqueTournament.fieldTranslations.nameTranslation.hi` | `string` |
| `$.match.tournament.uniqueTournament.fieldTranslations.nameTranslation.bn` | `string` |
| `$.match.tournament.uniqueTournament.fieldTranslations.nameTranslation.ru` | `string` |
| `$.match.tournament.uniqueTournament.fieldTranslations.shortNameTranslation` | `object` |
| `$.match.tournament.priority` | `integer` |
| `$.match.tournament.isGroup` | `boolean` |
| `$.match.tournament.competitionType` | `integer` |
| `$.match.tournament.isLive` | `boolean` |
| `$.match.tournament.id` | `integer` |
| `$.match.tournament.fieldTranslations` | `object` |
| `$.match.tournament.fieldTranslations.nameTranslation` | `object` |
| `$.match.tournament.fieldTranslations.nameTranslation.hi` | `string` |
| `$.match.tournament.fieldTranslations.nameTranslation.ar` | `string` |
| `$.match.tournament.fieldTranslations.nameTranslation.bn` | `string` |
| `$.match.tournament.fieldTranslations.nameTranslation.ru` | `string` |
| `$.match.tournament.fieldTranslations.shortNameTranslation` | `object` |
| `$.match.season` | `object` |
| `$.match.season.name` | `string` |
| `$.match.season.year` | `string` |
| `$.match.season.editor` | `boolean` |
| `$.match.season.id` | `integer` |
| `$.match.roundInfo` | `object` |
| `$.match.roundInfo.round` | `integer` |
| `$.match.customId` | `string` |
| `$.match.status` | `object` |
| `$.match.status.code` | `integer` |
| `$.match.status.description` | `string` |
| `$.match.status.type` | `string` |
| `$.match.winnerCode` | `integer` |
| `$.match.attendance` | `integer` |
| `$.match.venue` | `object` |
| `$.match.venue.city` | `object` |
| `$.match.venue.city.name` | `string` |
| `$.match.venue.city.country` | `object` |
| `$.match.venue.city.country.alpha2` | `string` |
| `$.match.venue.city.country.alpha3` | `string` |
| `$.match.venue.city.country.name` | `string` |
| `$.match.venue.city.country.slug` | `string` |
| `$.match.venue.city.id` | `integer` |
| `$.match.venue.hidden` | `boolean` |
| `$.match.venue.slug` | `string` |
| `$.match.venue.name` | `string` |
| `$.match.venue.capacity` | `integer` |
| `$.match.venue.country` | `object` |
| `$.match.venue.country.alpha2` | `string` |
| `$.match.venue.country.alpha3` | `string` |
| `$.match.venue.country.name` | `string` |
| `$.match.venue.country.slug` | `string` |
| `$.match.venue.id` | `integer` |
| `$.match.venue.fieldTranslations` | `object` |
| `$.match.venue.fieldTranslations.nameTranslation` | `object` |
| `$.match.venue.fieldTranslations.nameTranslation.ar` | `string` |
| `$.match.venue.fieldTranslations.nameTranslation.hi` | `string` |
| `$.match.venue.fieldTranslations.nameTranslation.bn` | `string` |
| `$.match.venue.fieldTranslations.nameTranslation.ru` | `string` |
| `$.match.venue.fieldTranslations.shortNameTranslation` | `object` |
| `$.match.venue.stadium` | `object` |
| `$.match.venue.stadium.name` | `string` |
| `$.match.venue.stadium.capacity` | `integer` |
| `$.match.referee` | `object` |
| `$.match.referee.name` | `string` |
| `$.match.referee.slug` | `string` |
| `$.match.referee.yellowCards` | `integer` |
| `$.match.referee.redCards` | `integer` |
| `$.match.referee.yellowRedCards` | `integer` |
| `$.match.referee.games` | `integer` |
| `$.match.referee.sport` | `object` |
| `$.match.referee.sport.id` | `integer` |
| `$.match.referee.sport.slug` | `string` |
| `$.match.referee.sport.name` | `string` |
| `$.match.referee.country` | `object` |
| `$.match.referee.country.alpha2` | `string` |
| `$.match.referee.country.alpha3` | `string` |
| `$.match.referee.country.name` | `string` |
| `$.match.referee.country.slug` | `string` |
| `$.match.referee.id` | `integer` |
| `$.match.referee.fieldTranslations` | `object` |
| `$.match.referee.fieldTranslations.nameTranslation` | `object` |
| `$.match.referee.fieldTranslations.nameTranslation.ar` | `string` |
| `$.match.referee.fieldTranslations.nameTranslation.bn` | `string` |
| `$.match.referee.fieldTranslations.nameTranslation.hi` | `string` |
| `$.match.referee.fieldTranslations.nameTranslation.ru` | `string` |
| `$.match.referee.fieldTranslations.shortNameTranslation` | `object` |
| `$.match.homeTeam` | `object` |
| `$.match.homeTeam.name` | `string` |
| `$.match.homeTeam.slug` | `string` |
| `$.match.homeTeam.shortName` | `string` |
| `$.match.homeTeam.gender` | `string` |
| `$.match.homeTeam.sport` | `object` |
| `$.match.homeTeam.sport.name` | `string` |
| `$.match.homeTeam.sport.slug` | `string` |
| `$.match.homeTeam.sport.id` | `integer` |
| `$.match.homeTeam.userCount` | `integer` |
| `$.match.homeTeam.manager` | `object` |
| `$.match.homeTeam.manager.name` | `string` |
| `$.match.homeTeam.manager.slug` | `string` |
| `$.match.homeTeam.manager.shortName` | `string` |
| `$.match.homeTeam.manager.country` | `object` |
| `$.match.homeTeam.manager.country.alpha2` | `string` |
| `$.match.homeTeam.manager.country.alpha3` | `string` |
| `$.match.homeTeam.manager.country.name` | `string` |
| `$.match.homeTeam.manager.country.slug` | `string` |
| `$.match.homeTeam.manager.id` | `integer` |
| `$.match.homeTeam.manager.fieldTranslations` | `object` |
| `$.match.homeTeam.manager.fieldTranslations.nameTranslation` | `object` |
| `$.match.homeTeam.manager.fieldTranslations.nameTranslation.ar` | `string` |
| `$.match.homeTeam.manager.fieldTranslations.nameTranslation.ru` | `string` |
| `$.match.homeTeam.manager.fieldTranslations.shortNameTranslation` | `object` |
| `$.match.homeTeam.manager.fieldTranslations.shortNameTranslation.ar` | `string` |
| `$.match.homeTeam.manager.fieldTranslations.shortNameTranslation.ru` | `string` |
| `$.match.homeTeam.venue` | `object` |
| `$.match.homeTeam.venue.city` | `object` |
| `$.match.homeTeam.venue.city.name` | `string` |
| `$.match.homeTeam.venue.city.country` | `object` |
| `$.match.homeTeam.venue.city.country.alpha2` | `string` |
| `$.match.homeTeam.venue.city.country.alpha3` | `string` |
| `$.match.homeTeam.venue.city.country.name` | `string` |
| `$.match.homeTeam.venue.city.country.slug` | `string` |
| `$.match.homeTeam.venue.city.id` | `integer` |
| `$.match.homeTeam.venue.hidden` | `boolean` |
| `$.match.homeTeam.venue.slug` | `string` |
| `$.match.homeTeam.venue.name` | `string` |
| `$.match.homeTeam.venue.capacity` | `integer` |
| `$.match.homeTeam.venue.country` | `object` |
| `$.match.homeTeam.venue.country.alpha2` | `string` |
| `$.match.homeTeam.venue.country.alpha3` | `string` |
| `$.match.homeTeam.venue.country.name` | `string` |
| `$.match.homeTeam.venue.country.slug` | `string` |
| `$.match.homeTeam.venue.id` | `integer` |
| `$.match.homeTeam.venue.fieldTranslations` | `object` |
| `$.match.homeTeam.venue.fieldTranslations.nameTranslation` | `object` |
| `$.match.homeTeam.venue.fieldTranslations.nameTranslation.ar` | `string` |
| `$.match.homeTeam.venue.fieldTranslations.nameTranslation.hi` | `string` |
| `$.match.homeTeam.venue.fieldTranslations.nameTranslation.bn` | `string` |
| `$.match.homeTeam.venue.fieldTranslations.nameTranslation.ru` | `string` |
| `$.match.homeTeam.venue.fieldTranslations.shortNameTranslation` | `object` |
| `$.match.homeTeam.venue.stadium` | `object` |
| `$.match.homeTeam.venue.stadium.name` | `string` |
| `$.match.homeTeam.venue.stadium.capacity` | `integer` |
| `$.match.homeTeam.nameCode` | `string` |
| `$.match.homeTeam.class` | `integer` |
| `$.match.homeTeam.disabled` | `boolean` |
| `$.match.homeTeam.national` | `boolean` |
| `$.match.homeTeam.type` | `integer` |
| `$.match.homeTeam.country` | `object` |
| `$.match.homeTeam.country.alpha2` | `string` |
| `$.match.homeTeam.country.alpha3` | `string` |
| `$.match.homeTeam.country.name` | `string` |
| `$.match.homeTeam.country.slug` | `string` |
| `$.match.homeTeam.id` | `integer` |
| `$.match.homeTeam.fullName` | `string` |
| `$.match.homeTeam.subTeams` | `array` |
| `$.match.homeTeam.teamColors` | `object` |
| `$.match.homeTeam.teamColors.primary` | `string` |
| `$.match.homeTeam.teamColors.secondary` | `string` |
| `$.match.homeTeam.teamColors.text` | `string` |
| `$.match.homeTeam.foundationDateTimestamp` | `integer` |
| `$.match.homeTeam.fieldTranslations` | `object` |
| `$.match.homeTeam.fieldTranslations.nameTranslation` | `object` |
| `$.match.homeTeam.fieldTranslations.nameTranslation.ar` | `string` |
| `$.match.homeTeam.fieldTranslations.nameTranslation.hi` | `string` |
| `$.match.homeTeam.fieldTranslations.nameTranslation.ru` | `string` |
| `$.match.homeTeam.fieldTranslations.shortNameTranslation` | `object` |
| `$.match.homeTeam.fieldTranslations.shortNameTranslation.ar` | `string` |
| `$.match.homeTeam.fieldTranslations.shortNameTranslation.bn` | `string` |
| `$.match.homeTeam.fieldTranslations.shortNameTranslation.hi` | `string` |
| `$.match.homeTeam.timeActive` | `array` |
| `$.match.awayTeam` | `object` |
| `$.match.awayTeam.name` | `string` |
| `$.match.awayTeam.slug` | `string` |
| `$.match.awayTeam.shortName` | `string` |
| `$.match.awayTeam.gender` | `string` |
| `$.match.awayTeam.sport` | `object` |
| `$.match.awayTeam.sport.name` | `string` |
| `$.match.awayTeam.sport.slug` | `string` |
| `$.match.awayTeam.sport.id` | `integer` |
| `$.match.awayTeam.userCount` | `integer` |
| `$.match.awayTeam.manager` | `object` |
| `$.match.awayTeam.manager.name` | `string` |
| `$.match.awayTeam.manager.slug` | `string` |
| `$.match.awayTeam.manager.shortName` | `string` |
| `$.match.awayTeam.manager.country` | `object` |
| `$.match.awayTeam.manager.country.alpha2` | `string` |
| `$.match.awayTeam.manager.country.alpha3` | `string` |
| `$.match.awayTeam.manager.country.name` | `string` |
| `$.match.awayTeam.manager.country.slug` | `string` |
| `$.match.awayTeam.manager.id` | `integer` |
| `$.match.awayTeam.manager.fieldTranslations` | `object` |
| `$.match.awayTeam.manager.fieldTranslations.nameTranslation` | `object` |
| `$.match.awayTeam.manager.fieldTranslations.nameTranslation.ar` | `string` |
| `$.match.awayTeam.manager.fieldTranslations.nameTranslation.ru` | `string` |
| `$.match.awayTeam.manager.fieldTranslations.shortNameTranslation` | `object` |
| `$.match.awayTeam.manager.fieldTranslations.shortNameTranslation.ar` | `string` |
| `$.match.awayTeam.manager.fieldTranslations.shortNameTranslation.ru` | `string` |
| `$.match.awayTeam.venue` | `object` |
| `$.match.awayTeam.venue.city` | `object` |
| `$.match.awayTeam.venue.city.name` | `string` |
| `$.match.awayTeam.venue.city.country` | `object` |
| `$.match.awayTeam.venue.city.country.alpha2` | `string` |
| `$.match.awayTeam.venue.city.country.alpha3` | `string` |
| `$.match.awayTeam.venue.city.country.name` | `string` |
| `$.match.awayTeam.venue.city.country.slug` | `string` |
| `$.match.awayTeam.venue.city.id` | `integer` |
| `$.match.awayTeam.venue.venueCoordinates` | `object` |
| `$.match.awayTeam.venue.venueCoordinates.latitude` | `number` |
| `$.match.awayTeam.venue.venueCoordinates.longitude` | `number` |
| `$.match.awayTeam.venue.hidden` | `boolean` |
| `$.match.awayTeam.venue.slug` | `string` |
| `$.match.awayTeam.venue.name` | `string` |
| `$.match.awayTeam.venue.capacity` | `integer` |
| `$.match.awayTeam.venue.country` | `object` |
| `$.match.awayTeam.venue.country.alpha2` | `string` |
| `$.match.awayTeam.venue.country.alpha3` | `string` |
| `$.match.awayTeam.venue.country.name` | `string` |
| `$.match.awayTeam.venue.country.slug` | `string` |
| `$.match.awayTeam.venue.id` | `integer` |
| `$.match.awayTeam.venue.fieldTranslations` | `object` |
| `$.match.awayTeam.venue.fieldTranslations.nameTranslation` | `object` |
| `$.match.awayTeam.venue.fieldTranslations.nameTranslation.ar` | `string` |
| `$.match.awayTeam.venue.fieldTranslations.nameTranslation.hi` | `string` |
| `$.match.awayTeam.venue.fieldTranslations.nameTranslation.bn` | `string` |
| `$.match.awayTeam.venue.fieldTranslations.nameTranslation.ru` | `string` |
| `$.match.awayTeam.venue.fieldTranslations.shortNameTranslation` | `object` |
| `$.match.awayTeam.venue.stadium` | `object` |
| `$.match.awayTeam.venue.stadium.name` | `string` |
| `$.match.awayTeam.venue.stadium.capacity` | `integer` |
| `$.match.awayTeam.nameCode` | `string` |
| `$.match.awayTeam.class` | `integer` |
| `$.match.awayTeam.disabled` | `boolean` |
| `$.match.awayTeam.national` | `boolean` |
| `$.match.awayTeam.type` | `integer` |
| `$.match.awayTeam.country` | `object` |
| `$.match.awayTeam.country.alpha2` | `string` |
| `$.match.awayTeam.country.alpha3` | `string` |
| `$.match.awayTeam.country.name` | `string` |
| `$.match.awayTeam.country.slug` | `string` |
| `$.match.awayTeam.id` | `integer` |
| `$.match.awayTeam.fullName` | `string` |
| `$.match.awayTeam.subTeams` | `array` |
| `$.match.awayTeam.teamColors` | `object` |
| `$.match.awayTeam.teamColors.primary` | `string` |
| `$.match.awayTeam.teamColors.secondary` | `string` |
| `$.match.awayTeam.teamColors.text` | `string` |
| `$.match.awayTeam.foundationDateTimestamp` | `integer` |
| `$.match.awayTeam.fieldTranslations` | `object` |
| `$.match.awayTeam.fieldTranslations.nameTranslation` | `object` |
| `$.match.awayTeam.fieldTranslations.nameTranslation.ar` | `string` |
| `$.match.awayTeam.fieldTranslations.nameTranslation.ru` | `string` |
| `$.match.awayTeam.fieldTranslations.shortNameTranslation` | `object` |
| `$.match.awayTeam.fieldTranslations.shortNameTranslation.ar` | `string` |
| `$.match.awayTeam.fieldTranslations.shortNameTranslation.bn` | `string` |
| `$.match.awayTeam.fieldTranslations.shortNameTranslation.hi` | `string` |
| `$.match.awayTeam.timeActive` | `array` |
| `$.match.homeScore` | `object` |
| `$.match.homeScore.current` | `integer` |
| `$.match.homeScore.display` | `integer` |
| `$.match.homeScore.period1` | `integer` |
| `$.match.homeScore.period2` | `integer` |
| `$.match.homeScore.normaltime` | `integer` |
| `$.match.awayScore` | `object` |
| `$.match.awayScore.current` | `integer` |
| `$.match.awayScore.display` | `integer` |
| `$.match.awayScore.period1` | `integer` |
| `$.match.awayScore.period2` | `integer` |
| `$.match.awayScore.normaltime` | `integer` |
| `$.match.time` | `object` |
| `$.match.time.injuryTime1` | `integer` |
| `$.match.time.injuryTime2` | `integer` |
| `$.match.time.currentPeriodStartTimestamp` | `integer` |
| `$.match.changes` | `object` |
| `$.match.changes.changes` | `array` |
| `$.match.changes.changes[]` | `string` |
| `$.match.changes.changeTimestamp` | `integer` |
| `$.match.hasGlobalHighlights` | `boolean` |
| `$.match.hasXg` | `boolean` |
| `$.match.hasEventPlayerStatistics` | `boolean` |
| `$.match.hasEventPlayerHeatMap` | `boolean` |
| `$.match.detailId` | `integer` |
| `$.match.crowdsourcingDataDisplayEnabled` | `boolean` |
| `$.match.correctAiInsight` | `boolean` |
| `$.match.correctHalftimeAiInsight` | `boolean` |
| `$.match.id` | `integer` |
| `$.match.defaultPeriodCount` | `integer` |
| `$.match.defaultPeriodLength` | `integer` |
| `$.match.defaultOvertimeLength` | `integer` |
| `$.match.slug` | `string` |
| `$.match.currentPeriodStartTimestamp` | `integer` |
| `$.match.startTimestamp` | `integer` |
| `$.match.finalResultOnly` | `boolean` |
| `$.match.feedLocked` | `boolean` |
| `$.match.seasonStatisticsType` | `string` |
| `$.match.showTotoPromo` | `boolean` |
| `$.match.isEditor` | `boolean` |
| `$.match.eventFilters` | `object` |
| `$.match.eventFilters.category` | `array` |
| `$.match.eventFilters.category[]` | `string` |
| `$.match.eventFilters.level` | `array` |
| `$.match.eventFilters.level[]` | `string` |
| `$.match.eventFilters.gender` | `array` |
| `$.match.eventFilters.gender[]` | `string` |
| `$.data` | `object` |
| `$.data.event` | `object` |
| `$.data.event.eventState` | `object` |
| `$.data.event.tournament` | `object` |
| `$.data.event.tournament.name` | `string` |
| `$.data.event.tournament.slug` | `string` |
| `$.data.event.tournament.category` | `object` |
| `$.data.event.tournament.category.name` | `string` |
| `$.data.event.tournament.category.slug` | `string` |
| `$.data.event.tournament.category.sport` | `object` |
| `$.data.event.tournament.category.sport.name` | `string` |
| `$.data.event.tournament.category.sport.slug` | `string` |
| `$.data.event.tournament.category.sport.id` | `integer` |
| `$.data.event.tournament.category.priority` | `integer` |
| `$.data.event.tournament.category.country` | `object` |
| `$.data.event.tournament.category.country.alpha2` | `string` |
| `$.data.event.tournament.category.country.alpha3` | `string` |
| `$.data.event.tournament.category.country.name` | `string` |
| `$.data.event.tournament.category.country.slug` | `string` |
| `$.data.event.tournament.category.id` | `integer` |
| `$.data.event.tournament.category.flag` | `string` |
| `$.data.event.tournament.category.alpha2` | `string` |
| `$.data.event.tournament.category.fieldTranslations` | `object` |
| `$.data.event.tournament.category.fieldTranslations.nameTranslation` | `object` |
| `$.data.event.tournament.category.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.event.tournament.category.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.event.tournament.category.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.event.tournament.category.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.event.tournament.category.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.event.tournament.uniqueTournament` | `object` |
| `$.data.event.tournament.uniqueTournament.name` | `string` |
| `$.data.event.tournament.uniqueTournament.slug` | `string` |
| `$.data.event.tournament.uniqueTournament.primaryColorHex` | `string` |
| `$.data.event.tournament.uniqueTournament.secondaryColorHex` | `string` |
| `$.data.event.tournament.uniqueTournament.category` | `object` |
| `$.data.event.tournament.uniqueTournament.category.name` | `string` |
| `$.data.event.tournament.uniqueTournament.category.slug` | `string` |
| `$.data.event.tournament.uniqueTournament.category.sport` | `object` |
| `$.data.event.tournament.uniqueTournament.category.sport.name` | `string` |
| `$.data.event.tournament.uniqueTournament.category.sport.slug` | `string` |
| `$.data.event.tournament.uniqueTournament.category.sport.id` | `integer` |
| `$.data.event.tournament.uniqueTournament.category.priority` | `integer` |
| `$.data.event.tournament.uniqueTournament.category.country` | `object` |
| `$.data.event.tournament.uniqueTournament.category.country.alpha2` | `string` |
| `$.data.event.tournament.uniqueTournament.category.country.alpha3` | `string` |
| `$.data.event.tournament.uniqueTournament.category.country.name` | `string` |
| `$.data.event.tournament.uniqueTournament.category.country.slug` | `string` |
| `$.data.event.tournament.uniqueTournament.category.id` | `integer` |
| `$.data.event.tournament.uniqueTournament.category.flag` | `string` |
| `$.data.event.tournament.uniqueTournament.category.alpha2` | `string` |
| `$.data.event.tournament.uniqueTournament.category.fieldTranslations` | `object` |
| `$.data.event.tournament.uniqueTournament.category.fieldTranslations.nameTranslation` | `object` |
| `$.data.event.tournament.uniqueTournament.category.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.event.tournament.uniqueTournament.category.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.event.tournament.uniqueTournament.category.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.event.tournament.uniqueTournament.category.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.event.tournament.uniqueTournament.category.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.event.tournament.uniqueTournament.userCount` | `integer` |
| `$.data.event.tournament.uniqueTournament.hasRounds` | `boolean` |
| `$.data.event.tournament.uniqueTournament.hasPerformanceGraphFeature` | `boolean` |
| `$.data.event.tournament.uniqueTournament.country` | `object` |
| `$.data.event.tournament.uniqueTournament.id` | `integer` |
| `$.data.event.tournament.uniqueTournament.hasEventPlayerStatistics` | `boolean` |
| `$.data.event.tournament.uniqueTournament.displayInverseHomeAwayTeams` | `boolean` |
| `$.data.event.tournament.uniqueTournament.fieldTranslations` | `object` |
| `$.data.event.tournament.uniqueTournament.fieldTranslations.nameTranslation` | `object` |
| `$.data.event.tournament.uniqueTournament.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.event.tournament.uniqueTournament.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.event.tournament.uniqueTournament.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.event.tournament.uniqueTournament.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.event.tournament.uniqueTournament.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.event.tournament.priority` | `integer` |
| `$.data.event.tournament.isGroup` | `boolean` |
| `$.data.event.tournament.competitionType` | `integer` |
| `$.data.event.tournament.isLive` | `boolean` |
| `$.data.event.tournament.id` | `integer` |
| `$.data.event.tournament.fieldTranslations` | `object` |
| `$.data.event.tournament.fieldTranslations.nameTranslation` | `object` |
| `$.data.event.tournament.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.event.tournament.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.event.tournament.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.event.tournament.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.event.tournament.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.event.season` | `object` |
| `$.data.event.season.name` | `string` |
| `$.data.event.season.year` | `string` |
| `$.data.event.season.editor` | `boolean` |
| `$.data.event.season.id` | `integer` |
| `$.data.event.roundInfo` | `object` |
| `$.data.event.roundInfo.round` | `integer` |
| `$.data.event.customId` | `string` |
| `$.data.event.status` | `object` |
| `$.data.event.status.code` | `integer` |
| `$.data.event.status.description` | `string` |
| `$.data.event.status.type` | `string` |
| `$.data.event.winnerCode` | `integer` |
| `$.data.event.attendance` | `integer` |
| `$.data.event.venue` | `object` |
| `$.data.event.venue.city` | `object` |
| `$.data.event.venue.city.name` | `string` |
| `$.data.event.venue.city.country` | `object` |
| `$.data.event.venue.city.country.alpha2` | `string` |
| `$.data.event.venue.city.country.alpha3` | `string` |
| `$.data.event.venue.city.country.name` | `string` |
| `$.data.event.venue.city.country.slug` | `string` |
| `$.data.event.venue.city.id` | `integer` |
| `$.data.event.venue.hidden` | `boolean` |
| `$.data.event.venue.slug` | `string` |
| `$.data.event.venue.name` | `string` |
| `$.data.event.venue.capacity` | `integer` |
| `$.data.event.venue.country` | `object` |
| `$.data.event.venue.country.alpha2` | `string` |
| `$.data.event.venue.country.alpha3` | `string` |
| `$.data.event.venue.country.name` | `string` |
| `$.data.event.venue.country.slug` | `string` |
| `$.data.event.venue.id` | `integer` |
| `$.data.event.venue.fieldTranslations` | `object` |
| `$.data.event.venue.fieldTranslations.nameTranslation` | `object` |
| `$.data.event.venue.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.event.venue.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.event.venue.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.event.venue.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.event.venue.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.event.venue.stadium` | `object` |
| `$.data.event.venue.stadium.name` | `string` |
| `$.data.event.venue.stadium.capacity` | `integer` |
| `$.data.event.referee` | `object` |
| `$.data.event.referee.name` | `string` |
| `$.data.event.referee.slug` | `string` |
| `$.data.event.referee.yellowCards` | `integer` |
| `$.data.event.referee.redCards` | `integer` |
| `$.data.event.referee.yellowRedCards` | `integer` |
| `$.data.event.referee.games` | `integer` |
| `$.data.event.referee.sport` | `object` |
| `$.data.event.referee.sport.id` | `integer` |
| `$.data.event.referee.sport.slug` | `string` |
| `$.data.event.referee.sport.name` | `string` |
| `$.data.event.referee.country` | `object` |
| `$.data.event.referee.country.alpha2` | `string` |
| `$.data.event.referee.country.alpha3` | `string` |
| `$.data.event.referee.country.name` | `string` |
| `$.data.event.referee.country.slug` | `string` |
| `$.data.event.referee.id` | `integer` |
| `$.data.event.referee.fieldTranslations` | `object` |
| `$.data.event.referee.fieldTranslations.nameTranslation` | `object` |
| `$.data.event.referee.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.event.referee.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.event.referee.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.event.referee.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.event.referee.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.event.homeTeam` | `object` |
| `$.data.event.homeTeam.name` | `string` |
| `$.data.event.homeTeam.slug` | `string` |
| `$.data.event.homeTeam.shortName` | `string` |
| `$.data.event.homeTeam.gender` | `string` |
| `$.data.event.homeTeam.sport` | `object` |
| `$.data.event.homeTeam.sport.name` | `string` |
| `$.data.event.homeTeam.sport.slug` | `string` |
| `$.data.event.homeTeam.sport.id` | `integer` |
| `$.data.event.homeTeam.userCount` | `integer` |
| `$.data.event.homeTeam.manager` | `object` |
| `$.data.event.homeTeam.manager.name` | `string` |
| `$.data.event.homeTeam.manager.slug` | `string` |
| `$.data.event.homeTeam.manager.shortName` | `string` |
| `$.data.event.homeTeam.manager.country` | `object` |
| `$.data.event.homeTeam.manager.country.alpha2` | `string` |
| `$.data.event.homeTeam.manager.country.alpha3` | `string` |
| `$.data.event.homeTeam.manager.country.name` | `string` |
| `$.data.event.homeTeam.manager.country.slug` | `string` |
| `$.data.event.homeTeam.manager.id` | `integer` |
| `$.data.event.homeTeam.manager.fieldTranslations` | `object` |
| `$.data.event.homeTeam.manager.fieldTranslations.nameTranslation` | `object` |
| `$.data.event.homeTeam.manager.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.event.homeTeam.manager.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.event.homeTeam.manager.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.event.homeTeam.manager.fieldTranslations.shortNameTranslation.ar` | `string` |
| `$.data.event.homeTeam.manager.fieldTranslations.shortNameTranslation.ru` | `string` |
| `$.data.event.homeTeam.venue` | `object` |
| `$.data.event.homeTeam.venue.city` | `object` |
| `$.data.event.homeTeam.venue.city.name` | `string` |
| `$.data.event.homeTeam.venue.city.country` | `object` |
| `$.data.event.homeTeam.venue.city.country.alpha2` | `string` |
| `$.data.event.homeTeam.venue.city.country.alpha3` | `string` |
| `$.data.event.homeTeam.venue.city.country.name` | `string` |
| `$.data.event.homeTeam.venue.city.country.slug` | `string` |
| `$.data.event.homeTeam.venue.city.id` | `integer` |
| `$.data.event.homeTeam.venue.hidden` | `boolean` |
| `$.data.event.homeTeam.venue.slug` | `string` |
| `$.data.event.homeTeam.venue.name` | `string` |
| `$.data.event.homeTeam.venue.capacity` | `integer` |
| `$.data.event.homeTeam.venue.country` | `object` |
| `$.data.event.homeTeam.venue.country.alpha2` | `string` |
| `$.data.event.homeTeam.venue.country.alpha3` | `string` |
| `$.data.event.homeTeam.venue.country.name` | `string` |
| `$.data.event.homeTeam.venue.country.slug` | `string` |
| `$.data.event.homeTeam.venue.id` | `integer` |
| `$.data.event.homeTeam.venue.fieldTranslations` | `object` |
| `$.data.event.homeTeam.venue.fieldTranslations.nameTranslation` | `object` |
| `$.data.event.homeTeam.venue.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.event.homeTeam.venue.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.event.homeTeam.venue.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.event.homeTeam.venue.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.event.homeTeam.venue.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.event.homeTeam.venue.stadium` | `object` |
| `$.data.event.homeTeam.venue.stadium.name` | `string` |
| `$.data.event.homeTeam.venue.stadium.capacity` | `integer` |
| `$.data.event.homeTeam.nameCode` | `string` |
| `$.data.event.homeTeam.class` | `integer` |
| `$.data.event.homeTeam.disabled` | `boolean` |
| `$.data.event.homeTeam.national` | `boolean` |
| `$.data.event.homeTeam.type` | `integer` |
| `$.data.event.homeTeam.country` | `object` |
| `$.data.event.homeTeam.country.alpha2` | `string` |
| `$.data.event.homeTeam.country.alpha3` | `string` |
| `$.data.event.homeTeam.country.name` | `string` |
| `$.data.event.homeTeam.country.slug` | `string` |
| `$.data.event.homeTeam.id` | `integer` |
| `$.data.event.homeTeam.fullName` | `string` |
| `$.data.event.homeTeam.subTeams` | `array` |
| `$.data.event.homeTeam.teamColors` | `object` |
| `$.data.event.homeTeam.teamColors.primary` | `string` |
| `$.data.event.homeTeam.teamColors.secondary` | `string` |
| `$.data.event.homeTeam.teamColors.text` | `string` |
| `$.data.event.homeTeam.foundationDateTimestamp` | `integer` |
| `$.data.event.homeTeam.fieldTranslations` | `object` |
| `$.data.event.homeTeam.fieldTranslations.nameTranslation` | `object` |
| `$.data.event.homeTeam.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.event.homeTeam.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.event.homeTeam.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.event.homeTeam.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.event.homeTeam.fieldTranslations.shortNameTranslation.ar` | `string` |
| `$.data.event.homeTeam.fieldTranslations.shortNameTranslation.bn` | `string` |
| `$.data.event.homeTeam.fieldTranslations.shortNameTranslation.hi` | `string` |
| `$.data.event.homeTeam.timeActive` | `array` |
| `$.data.event.awayTeam` | `object` |
| `$.data.event.awayTeam.name` | `string` |
| `$.data.event.awayTeam.slug` | `string` |
| `$.data.event.awayTeam.shortName` | `string` |
| `$.data.event.awayTeam.gender` | `string` |
| `$.data.event.awayTeam.sport` | `object` |
| `$.data.event.awayTeam.sport.name` | `string` |
| `$.data.event.awayTeam.sport.slug` | `string` |
| `$.data.event.awayTeam.sport.id` | `integer` |
| `$.data.event.awayTeam.userCount` | `integer` |
| `$.data.event.awayTeam.manager` | `object` |
| `$.data.event.awayTeam.manager.name` | `string` |
| `$.data.event.awayTeam.manager.slug` | `string` |
| `$.data.event.awayTeam.manager.shortName` | `string` |
| `$.data.event.awayTeam.manager.country` | `object` |
| `$.data.event.awayTeam.manager.country.alpha2` | `string` |
| `$.data.event.awayTeam.manager.country.alpha3` | `string` |
| `$.data.event.awayTeam.manager.country.name` | `string` |
| `$.data.event.awayTeam.manager.country.slug` | `string` |
| `$.data.event.awayTeam.manager.id` | `integer` |
| `$.data.event.awayTeam.manager.fieldTranslations` | `object` |
| `$.data.event.awayTeam.manager.fieldTranslations.nameTranslation` | `object` |
| `$.data.event.awayTeam.manager.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.event.awayTeam.manager.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.event.awayTeam.manager.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.event.awayTeam.manager.fieldTranslations.shortNameTranslation.ar` | `string` |
| `$.data.event.awayTeam.manager.fieldTranslations.shortNameTranslation.ru` | `string` |
| `$.data.event.awayTeam.venue` | `object` |
| `$.data.event.awayTeam.venue.city` | `object` |
| `$.data.event.awayTeam.venue.city.name` | `string` |
| `$.data.event.awayTeam.venue.city.country` | `object` |
| `$.data.event.awayTeam.venue.city.country.alpha2` | `string` |
| `$.data.event.awayTeam.venue.city.country.alpha3` | `string` |
| `$.data.event.awayTeam.venue.city.country.name` | `string` |
| `$.data.event.awayTeam.venue.city.country.slug` | `string` |
| `$.data.event.awayTeam.venue.city.id` | `integer` |
| `$.data.event.awayTeam.venue.venueCoordinates` | `object` |
| `$.data.event.awayTeam.venue.venueCoordinates.latitude` | `number` |
| `$.data.event.awayTeam.venue.venueCoordinates.longitude` | `number` |
| `$.data.event.awayTeam.venue.hidden` | `boolean` |
| `$.data.event.awayTeam.venue.slug` | `string` |
| `$.data.event.awayTeam.venue.name` | `string` |
| `$.data.event.awayTeam.venue.capacity` | `integer` |
| `$.data.event.awayTeam.venue.country` | `object` |
| `$.data.event.awayTeam.venue.country.alpha2` | `string` |
| `$.data.event.awayTeam.venue.country.alpha3` | `string` |
| `$.data.event.awayTeam.venue.country.name` | `string` |
| `$.data.event.awayTeam.venue.country.slug` | `string` |
| `$.data.event.awayTeam.venue.id` | `integer` |
| `$.data.event.awayTeam.venue.fieldTranslations` | `object` |
| `$.data.event.awayTeam.venue.fieldTranslations.nameTranslation` | `object` |
| `$.data.event.awayTeam.venue.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.event.awayTeam.venue.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.event.awayTeam.venue.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.event.awayTeam.venue.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.event.awayTeam.venue.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.event.awayTeam.venue.stadium` | `object` |
| `$.data.event.awayTeam.venue.stadium.name` | `string` |
| `$.data.event.awayTeam.venue.stadium.capacity` | `integer` |
| `$.data.event.awayTeam.nameCode` | `string` |
| `$.data.event.awayTeam.class` | `integer` |
| `$.data.event.awayTeam.disabled` | `boolean` |
| `$.data.event.awayTeam.national` | `boolean` |
| `$.data.event.awayTeam.type` | `integer` |
| `$.data.event.awayTeam.country` | `object` |
| `$.data.event.awayTeam.country.alpha2` | `string` |
| `$.data.event.awayTeam.country.alpha3` | `string` |
| `$.data.event.awayTeam.country.name` | `string` |
| `$.data.event.awayTeam.country.slug` | `string` |
| `$.data.event.awayTeam.id` | `integer` |
| `$.data.event.awayTeam.fullName` | `string` |
| `$.data.event.awayTeam.subTeams` | `array` |
| `$.data.event.awayTeam.teamColors` | `object` |
| `$.data.event.awayTeam.teamColors.primary` | `string` |
| `$.data.event.awayTeam.teamColors.secondary` | `string` |
| `$.data.event.awayTeam.teamColors.text` | `string` |
| `$.data.event.awayTeam.foundationDateTimestamp` | `integer` |
| `$.data.event.awayTeam.fieldTranslations` | `object` |
| `$.data.event.awayTeam.fieldTranslations.nameTranslation` | `object` |
| `$.data.event.awayTeam.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.event.awayTeam.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.event.awayTeam.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.event.awayTeam.fieldTranslations.shortNameTranslation.ar` | `string` |
| `$.data.event.awayTeam.fieldTranslations.shortNameTranslation.bn` | `string` |
| `$.data.event.awayTeam.fieldTranslations.shortNameTranslation.hi` | `string` |
| `$.data.event.awayTeam.timeActive` | `array` |
| `$.data.event.homeScore` | `object` |
| `$.data.event.homeScore.current` | `integer` |
| `$.data.event.homeScore.display` | `integer` |
| `$.data.event.homeScore.period1` | `integer` |
| `$.data.event.homeScore.period2` | `integer` |
| `$.data.event.homeScore.normaltime` | `integer` |
| `$.data.event.awayScore` | `object` |
| `$.data.event.awayScore.current` | `integer` |
| `$.data.event.awayScore.display` | `integer` |
| `$.data.event.awayScore.period1` | `integer` |
| `$.data.event.awayScore.period2` | `integer` |
| `$.data.event.awayScore.normaltime` | `integer` |
| `$.data.event.time` | `object` |
| `$.data.event.time.injuryTime1` | `integer` |
| `$.data.event.time.injuryTime2` | `integer` |
| `$.data.event.time.currentPeriodStartTimestamp` | `integer` |
| `$.data.event.changes` | `object` |
| `$.data.event.changes.changes` | `array` |
| `$.data.event.changes.changes[]` | `string` |
| `$.data.event.changes.changeTimestamp` | `integer` |
| `$.data.event.hasGlobalHighlights` | `boolean` |
| `$.data.event.hasXg` | `boolean` |
| `$.data.event.hasEventPlayerStatistics` | `boolean` |
| `$.data.event.hasEventPlayerHeatMap` | `boolean` |
| `$.data.event.detailId` | `integer` |
| `$.data.event.crowdsourcingDataDisplayEnabled` | `boolean` |
| `$.data.event.correctAiInsight` | `boolean` |
| `$.data.event.correctHalftimeAiInsight` | `boolean` |
| `$.data.event.id` | `integer` |
| `$.data.event.defaultPeriodCount` | `integer` |
| `$.data.event.defaultPeriodLength` | `integer` |
| `$.data.event.defaultOvertimeLength` | `integer` |
| `$.data.event.slug` | `string` |
| `$.data.event.currentPeriodStartTimestamp` | `integer` |
| `$.data.event.startTimestamp` | `integer` |
| `$.data.event.finalResultOnly` | `boolean` |
| `$.data.event.feedLocked` | `boolean` |
| `$.data.event.seasonStatisticsType` | `string` |
| `$.data.event.showTotoPromo` | `boolean` |
| `$.data.event.isEditor` | `boolean` |
| `$.data.event.eventFilters` | `object` |
| `$.data.event.eventFilters.category` | `array` |
| `$.data.event.eventFilters.category[]` | `string` |
| `$.data.event.eventFilters.level` | `array` |
| `$.data.event.eventFilters.level[]` | `string` |
| `$.data.event.eventFilters.gender` | `array` |
| `$.data.event.eventFilters.gender[]` | `string` |
| `$.startTime` | `string` |
| `$.timezone` | `object` |
| `$.timezone.name` | `string` |
| `$.timezone.utcOffset` | `string` |
| `$.timezone.source` | `string` |
| `$.timezone.country` | `string` |

---

## 1. Request

| Property | Value |
|---|---|
| Source | `sportsapipro.com` |
| Endpoint | `seasons/match/lineups` |
| Method | `GET` |
| URL | `https://api.sportsapipro.com/v2/football/match/14023935/lineups` |
| HTTP Status | `200` |
| Captured At | `2026-08-12T04:54:07.294154+00:00` |
| Raw Response | `raw/sportsapipro/seasons/match/lineups.json` |

### Query Parameters

_No query parameters._

## 2. Response Metadata

_No standard response metadata detected._

---

## 3. Record Counts

_No top-level arrays detected._

---

## 4. Response Structure

The following structure is automatically derived from the
complete JSON response.

| JSON Path | Type |
|---|---|
| `$.success` | `boolean` |
| `$.matchId` | `integer` |
| `$.endpoint` | `string` |
| `$.data` | `object` |
| `$.data.confirmed` | `boolean` |
| `$.data.home` | `object` |
| `$.data.home.players` | `array` |
| `$.data.home.players[]` | `object` |
| `$.data.home.players[].player` | `object` |
| `$.data.home.players[].player.name` | `string` |
| `$.data.home.players[].player.slug` | `string` |
| `$.data.home.players[].player.shortName` | `string` |
| `$.data.home.players[].player.position` | `string` |
| `$.data.home.players[].player.jerseyNumber` | `string` |
| `$.data.home.players[].player.height` | `integer` |
| `$.data.home.players[].player.userCount` | `integer` |
| `$.data.home.players[].player.gender` | `string` |
| `$.data.home.players[].player.country` | `object` |
| `$.data.home.players[].player.country.alpha2` | `string` |
| `$.data.home.players[].player.country.alpha3` | `string` |
| `$.data.home.players[].player.country.name` | `string` |
| `$.data.home.players[].player.country.slug` | `string` |
| `$.data.home.players[].player.id` | `integer` |
| `$.data.home.players[].player.marketValueCurrency` | `string` |
| `$.data.home.players[].player.dateOfBirthTimestamp` | `integer` |
| `$.data.home.players[].player.proposedMarketValueRaw` | `object` |
| `$.data.home.players[].player.proposedMarketValueRaw.value` | `integer` |
| `$.data.home.players[].player.proposedMarketValueRaw.currency` | `string` |
| `$.data.home.players[].player.fieldTranslations` | `object` |
| `$.data.home.players[].player.fieldTranslations.nameTranslation` | `object` |
| `$.data.home.players[].player.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.home.players[].player.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.home.players[].player.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.home.players[].player.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.home.players[].player.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.home.players[].player.fieldTranslations.shortNameTranslation.ar` | `string` |
| `$.data.home.players[].player.fieldTranslations.shortNameTranslation.bn` | `string` |
| `$.data.home.players[].player.fieldTranslations.shortNameTranslation.hi` | `string` |
| `$.data.home.players[].player.fieldTranslations.shortNameTranslation.ru` | `string` |
| `$.data.home.players[].teamId` | `integer` |
| `$.data.home.players[].shirtNumber` | `integer` |
| `$.data.home.players[].jerseyNumber` | `string` |
| `$.data.home.players[].position` | `string` |
| `$.data.home.players[].substitute` | `boolean` |
| `$.data.home.players[].statistics` | `object` |
| `$.data.home.players[].statistics.totalPass` | `integer` |
| `$.data.home.players[].statistics.accuratePass` | `integer` |
| `$.data.home.players[].statistics.totalLongBalls` | `integer` |
| `$.data.home.players[].statistics.accurateLongBalls` | `integer` |
| `$.data.home.players[].statistics.goalAssist` | `integer` |
| `$.data.home.players[].statistics.accurateOwnHalfPasses` | `integer` |
| `$.data.home.players[].statistics.totalOwnHalfPasses` | `integer` |
| `$.data.home.players[].statistics.accurateOppositionHalfPasses` | `integer` |
| `$.data.home.players[].statistics.totalOppositionHalfPasses` | `integer` |
| `$.data.home.players[].statistics.ballRecovery` | `integer` |
| `$.data.home.players[].statistics.goodHighClaim` | `integer` |
| `$.data.home.players[].statistics.savedShotsFromInsideTheBox` | `integer` |
| `$.data.home.players[].statistics.saves` | `integer` |
| `$.data.home.players[].statistics.totalKeeperSweeper` | `integer` |
| `$.data.home.players[].statistics.accurateKeeperSweeper` | `integer` |
| `$.data.home.players[].statistics.minutesPlayed` | `integer` |
| `$.data.home.players[].statistics.touches` | `integer` |
| `$.data.home.players[].statistics.rating` | `integer` |
| `$.data.home.players[].statistics.possessionLostCtrl` | `integer` |
| `$.data.home.players[].statistics.expectedAssists` | `number` |
| `$.data.home.players[].statistics.totalBallCarriesDistance` | `number` |
| `$.data.home.players[].statistics.ballCarriesCount` | `integer` |
| `$.data.home.players[].statistics.totalProgression` | `number` |
| `$.data.home.players[].statistics.progressiveBallCarriesCount` | `integer` |
| `$.data.home.players[].statistics.keeperSaveValue` | `number` |
| `$.data.home.players[].statistics.ratingVersions` | `object` |
| `$.data.home.players[].statistics.ratingVersions.original` | `integer` |
| `$.data.home.players[].statistics.ratingVersions.alternative` | `number` |
| `$.data.home.players[].statistics.totalShots` | `integer` |
| `$.data.home.players[].statistics.goalsPrevented` | `number` |
| `$.data.home.players[].statistics.passValueNormalized` | `number` |
| `$.data.home.players[].statistics.dribbleValueNormalized` | `integer` |
| `$.data.home.players[].statistics.defensiveValueNormalized` | `number` |
| `$.data.home.players[].statistics.goalkeeperValueNormalized` | `number` |
| `$.data.home.players[].statistics.statisticsType` | `object` |
| `$.data.home.players[].statistics.statisticsType.sportSlug` | `string` |
| `$.data.home.players[].statistics.statisticsType.statisticsType` | `string` |
| `$.data.home.players[].minutesPlayed` | `integer` |
| `$.data.home.players[].played` | `boolean` |
| `$.data.home.supportStaff` | `array` |
| `$.data.home.formation` | `string` |
| `$.data.home.playerColor` | `object` |
| `$.data.home.playerColor.primary` | `string` |
| `$.data.home.playerColor.number` | `string` |
| `$.data.home.playerColor.outline` | `string` |
| `$.data.home.playerColor.fancyNumber` | `string` |
| `$.data.home.goalkeeperColor` | `object` |
| `$.data.home.goalkeeperColor.primary` | `string` |
| `$.data.home.goalkeeperColor.number` | `string` |
| `$.data.home.goalkeeperColor.outline` | `string` |
| `$.data.home.goalkeeperColor.fancyNumber` | `string` |
| `$.data.home.missingPlayers` | `array` |
| `$.data.home.missingPlayers[]` | `object` |
| `$.data.home.missingPlayers[].player` | `object` |
| `$.data.home.missingPlayers[].player.name` | `string` |
| `$.data.home.missingPlayers[].player.firstName` | `string` |
| `$.data.home.missingPlayers[].player.lastName` | `string` |
| `$.data.home.missingPlayers[].player.slug` | `string` |
| `$.data.home.missingPlayers[].player.shortName` | `string` |
| `$.data.home.missingPlayers[].player.position` | `string` |
| `$.data.home.missingPlayers[].player.height` | `integer` |
| `$.data.home.missingPlayers[].player.userCount` | `integer` |
| `$.data.home.missingPlayers[].player.gender` | `string` |
| `$.data.home.missingPlayers[].player.country` | `object` |
| `$.data.home.missingPlayers[].player.country.alpha2` | `string` |
| `$.data.home.missingPlayers[].player.country.alpha3` | `string` |
| `$.data.home.missingPlayers[].player.country.name` | `string` |
| `$.data.home.missingPlayers[].player.country.slug` | `string` |
| `$.data.home.missingPlayers[].player.id` | `integer` |
| `$.data.home.missingPlayers[].player.marketValueCurrency` | `string` |
| `$.data.home.missingPlayers[].player.dateOfBirthTimestamp` | `integer` |
| `$.data.home.missingPlayers[].player.proposedMarketValueRaw` | `object` |
| `$.data.home.missingPlayers[].player.proposedMarketValueRaw.value` | `integer` |
| `$.data.home.missingPlayers[].player.proposedMarketValueRaw.currency` | `string` |
| `$.data.home.missingPlayers[].player.fieldTranslations` | `object` |
| `$.data.home.missingPlayers[].player.fieldTranslations.nameTranslation` | `object` |
| `$.data.home.missingPlayers[].player.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.home.missingPlayers[].player.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.home.missingPlayers[].player.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.home.missingPlayers[].player.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.home.missingPlayers[].player.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.home.missingPlayers[].player.fieldTranslations.shortNameTranslation.ar` | `string` |
| `$.data.home.missingPlayers[].player.fieldTranslations.shortNameTranslation.bn` | `string` |
| `$.data.home.missingPlayers[].player.fieldTranslations.shortNameTranslation.hi` | `string` |
| `$.data.home.missingPlayers[].player.fieldTranslations.shortNameTranslation.ru` | `string` |
| `$.data.home.missingPlayers[].type` | `string` |
| `$.data.home.missingPlayers[].reason` | `integer` |
| `$.data.home.missingPlayers[].description` | `string` |
| `$.data.home.missingPlayers[].externalType` | `integer` |
| `$.data.home.missingPlayers[].expectedEndDate` | `string` |
| `$.data.away` | `object` |
| `$.data.away.players` | `array` |
| `$.data.away.players[]` | `object` |
| `$.data.away.players[].player` | `object` |
| `$.data.away.players[].player.name` | `string` |
| `$.data.away.players[].player.firstName` | `string` |
| `$.data.away.players[].player.lastName` | `string` |
| `$.data.away.players[].player.slug` | `string` |
| `$.data.away.players[].player.shortName` | `string` |
| `$.data.away.players[].player.position` | `string` |
| `$.data.away.players[].player.jerseyNumber` | `string` |
| `$.data.away.players[].player.height` | `integer` |
| `$.data.away.players[].player.userCount` | `integer` |
| `$.data.away.players[].player.gender` | `string` |
| `$.data.away.players[].player.country` | `object` |
| `$.data.away.players[].player.country.alpha2` | `string` |
| `$.data.away.players[].player.country.alpha3` | `string` |
| `$.data.away.players[].player.country.name` | `string` |
| `$.data.away.players[].player.country.slug` | `string` |
| `$.data.away.players[].player.id` | `integer` |
| `$.data.away.players[].player.marketValueCurrency` | `string` |
| `$.data.away.players[].player.dateOfBirthTimestamp` | `integer` |
| `$.data.away.players[].player.proposedMarketValueRaw` | `object` |
| `$.data.away.players[].player.proposedMarketValueRaw.value` | `integer` |
| `$.data.away.players[].player.proposedMarketValueRaw.currency` | `string` |
| `$.data.away.players[].player.fieldTranslations` | `object` |
| `$.data.away.players[].player.fieldTranslations.nameTranslation` | `object` |
| `$.data.away.players[].player.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.away.players[].player.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.away.players[].player.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.away.players[].player.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.away.players[].player.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.away.players[].player.fieldTranslations.shortNameTranslation.ar` | `string` |
| `$.data.away.players[].player.fieldTranslations.shortNameTranslation.bn` | `string` |
| `$.data.away.players[].player.fieldTranslations.shortNameTranslation.hi` | `string` |
| `$.data.away.players[].player.fieldTranslations.shortNameTranslation.ru` | `string` |
| `$.data.away.players[].teamId` | `integer` |
| `$.data.away.players[].shirtNumber` | `integer` |
| `$.data.away.players[].jerseyNumber` | `string` |
| `$.data.away.players[].position` | `string` |
| `$.data.away.players[].substitute` | `boolean` |
| `$.data.away.players[].statistics` | `object` |
| `$.data.away.players[].statistics.totalPass` | `integer` |
| `$.data.away.players[].statistics.accuratePass` | `integer` |
| `$.data.away.players[].statistics.totalLongBalls` | `integer` |
| `$.data.away.players[].statistics.accurateLongBalls` | `integer` |
| `$.data.away.players[].statistics.goalAssist` | `integer` |
| `$.data.away.players[].statistics.accurateOwnHalfPasses` | `integer` |
| `$.data.away.players[].statistics.totalOwnHalfPasses` | `integer` |
| `$.data.away.players[].statistics.accurateOppositionHalfPasses` | `integer` |
| `$.data.away.players[].statistics.totalOppositionHalfPasses` | `integer` |
| `$.data.away.players[].statistics.aerialWon` | `integer` |
| `$.data.away.players[].statistics.duelWon` | `integer` |
| `$.data.away.players[].statistics.totalClearance` | `integer` |
| `$.data.away.players[].statistics.ballRecovery` | `integer` |
| `$.data.away.players[].statistics.wasFouled` | `integer` |
| `$.data.away.players[].statistics.goodHighClaim` | `integer` |
| `$.data.away.players[].statistics.savedShotsFromInsideTheBox` | `integer` |
| `$.data.away.players[].statistics.saves` | `integer` |
| `$.data.away.players[].statistics.punches` | `integer` |
| `$.data.away.players[].statistics.minutesPlayed` | `integer` |
| `$.data.away.players[].statistics.touches` | `integer` |
| `$.data.away.players[].statistics.rating` | `number` |
| `$.data.away.players[].statistics.possessionLostCtrl` | `integer` |
| `$.data.away.players[].statistics.expectedAssists` | `number` |
| `$.data.away.players[].statistics.topSpeed` | `number` |
| `$.data.away.players[].statistics.kilometersCovered` | `number` |
| `$.data.away.players[].statistics.numberOfSprints` | `integer` |
| `$.data.away.players[].statistics.totalBallCarriesDistance` | `number` |
| `$.data.away.players[].statistics.ballCarriesCount` | `integer` |
| `$.data.away.players[].statistics.totalProgression` | `number` |
| `$.data.away.players[].statistics.progressiveBallCarriesCount` | `integer` |
| `$.data.away.players[].statistics.keeperSaveValue` | `number` |
| `$.data.away.players[].statistics.ratingVersions` | `object` |
| `$.data.away.players[].statistics.ratingVersions.original` | `number` |
| `$.data.away.players[].statistics.ratingVersions.alternative` | `number` |
| `$.data.away.players[].statistics.totalShots` | `integer` |
| `$.data.away.players[].statistics.goalsPrevented` | `number` |
| `$.data.away.players[].statistics.passValueNormalized` | `number` |
| `$.data.away.players[].statistics.dribbleValueNormalized` | `number` |
| `$.data.away.players[].statistics.defensiveValueNormalized` | `integer` |
| `$.data.away.players[].statistics.goalkeeperValueNormalized` | `number` |
| `$.data.away.players[].statistics.metersCoveredRunningKm` | `number` |
| `$.data.away.players[].statistics.metersCoveredHighSpeedRunningKm` | `number` |
| `$.data.away.players[].statistics.metersCoveredSprintingKm` | `integer` |
| `$.data.away.players[].statistics.statisticsType` | `object` |
| `$.data.away.players[].statistics.statisticsType.sportSlug` | `string` |
| `$.data.away.players[].statistics.statisticsType.statisticsType` | `string` |
| `$.data.away.players[].minutesPlayed` | `integer` |
| `$.data.away.players[].played` | `boolean` |
| `$.data.away.supportStaff` | `array` |
| `$.data.away.formation` | `string` |
| `$.data.away.playerColor` | `object` |
| `$.data.away.playerColor.primary` | `string` |
| `$.data.away.playerColor.number` | `string` |
| `$.data.away.playerColor.outline` | `string` |
| `$.data.away.playerColor.fancyNumber` | `string` |
| `$.data.away.goalkeeperColor` | `object` |
| `$.data.away.goalkeeperColor.primary` | `string` |
| `$.data.away.goalkeeperColor.number` | `string` |
| `$.data.away.goalkeeperColor.outline` | `string` |
| `$.data.away.goalkeeperColor.fancyNumber` | `string` |
| `$.data.away.missingPlayers` | `array` |
| `$.data.away.missingPlayers[]` | `object` |
| `$.data.away.missingPlayers[].player` | `object` |
| `$.data.away.missingPlayers[].player.name` | `string` |
| `$.data.away.missingPlayers[].player.firstName` | `string` |
| `$.data.away.missingPlayers[].player.slug` | `string` |
| `$.data.away.missingPlayers[].player.shortName` | `string` |
| `$.data.away.missingPlayers[].player.position` | `string` |
| `$.data.away.missingPlayers[].player.jerseyNumber` | `string` |
| `$.data.away.missingPlayers[].player.height` | `integer` |
| `$.data.away.missingPlayers[].player.userCount` | `integer` |
| `$.data.away.missingPlayers[].player.gender` | `string` |
| `$.data.away.missingPlayers[].player.country` | `object` |
| `$.data.away.missingPlayers[].player.country.alpha2` | `string` |
| `$.data.away.missingPlayers[].player.country.alpha3` | `string` |
| `$.data.away.missingPlayers[].player.country.name` | `string` |
| `$.data.away.missingPlayers[].player.country.slug` | `string` |
| `$.data.away.missingPlayers[].player.id` | `integer` |
| `$.data.away.missingPlayers[].player.marketValueCurrency` | `string` |
| `$.data.away.missingPlayers[].player.dateOfBirthTimestamp` | `integer` |
| `$.data.away.missingPlayers[].player.proposedMarketValueRaw` | `object` |
| `$.data.away.missingPlayers[].player.proposedMarketValueRaw.value` | `integer` |
| `$.data.away.missingPlayers[].player.proposedMarketValueRaw.currency` | `string` |
| `$.data.away.missingPlayers[].player.fieldTranslations` | `object` |
| `$.data.away.missingPlayers[].player.fieldTranslations.nameTranslation` | `object` |
| `$.data.away.missingPlayers[].player.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.away.missingPlayers[].player.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.away.missingPlayers[].player.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.away.missingPlayers[].player.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.away.missingPlayers[].player.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.away.missingPlayers[].player.fieldTranslations.shortNameTranslation.ar` | `string` |
| `$.data.away.missingPlayers[].player.fieldTranslations.shortNameTranslation.bn` | `string` |
| `$.data.away.missingPlayers[].player.fieldTranslations.shortNameTranslation.hi` | `string` |
| `$.data.away.missingPlayers[].player.fieldTranslations.shortNameTranslation.ru` | `string` |
| `$.data.away.missingPlayers[].type` | `string` |
| `$.data.away.missingPlayers[].reason` | `integer` |
| `$.data.away.missingPlayers[].description` | `string` |
| `$.data.away.missingPlayers[].externalType` | `integer` |
| `$.data.away.missingPlayers[].expectedEndDate` | `string` |
| `$.source` | `string` |
| `$.cacheHit` | `boolean` |
| `$.timezone` | `object` |
| `$.timezone.name` | `string` |
| `$.timezone.utcOffset` | `string` |
| `$.timezone.source` | `string` |
| `$.timezone.country` | `string` |

---

## 1. Request

| Property | Value |
|---|---|
| Source | `sportsapipro.com` |
| Endpoint | `seasons/match/statistics` |
| Method | `GET` |
| URL | `https://api.sportsapipro.com/v2/football/match/14023935/statistics` |
| HTTP Status | `200` |
| Captured At | `2026-08-12T04:57:48.690055+00:00` |
| Raw Response | `raw/sportsapipro/seasons/match/statistics.json` |

### Query Parameters

_No query parameters._

## 2. Response Metadata

_No standard response metadata detected._

---

## 3. Record Counts

_No top-level arrays detected._

---

## 4. Response Structure

The following structure is automatically derived from the
complete JSON response.

| JSON Path | Type |
|---|---|
| `$.success` | `boolean` |
| `$.matchId` | `integer` |
| `$.endpoint` | `string` |
| `$.data` | `object` |
| `$.data.statistics` | `array` |
| `$.data.statistics[]` | `object` |
| `$.data.statistics[].period` | `string` |
| `$.data.statistics[].groups` | `array` |
| `$.data.statistics[].groups[]` | `object` |
| `$.data.statistics[].groups[].groupName` | `string` |
| `$.data.statistics[].groups[].statisticsItems` | `array` |
| `$.data.statistics[].groups[].statisticsItems[]` | `object` |
| `$.data.statistics[].groups[].statisticsItems[].name` | `string` |
| `$.data.statistics[].groups[].statisticsItems[].home` | `string` |
| `$.data.statistics[].groups[].statisticsItems[].away` | `string` |
| `$.data.statistics[].groups[].statisticsItems[].compareCode` | `integer` |
| `$.data.statistics[].groups[].statisticsItems[].statisticsType` | `string` |
| `$.data.statistics[].groups[].statisticsItems[].valueType` | `string` |
| `$.data.statistics[].groups[].statisticsItems[].homeValue` | `integer` |
| `$.data.statistics[].groups[].statisticsItems[].awayValue` | `integer` |
| `$.data.statistics[].groups[].statisticsItems[].renderType` | `integer` |
| `$.data.statistics[].groups[].statisticsItems[].key` | `string` |
| `$.source` | `string` |
| `$.cacheHit` | `boolean` |
| `$.timezone` | `object` |
| `$.timezone.name` | `string` |
| `$.timezone.utcOffset` | `string` |
| `$.timezone.source` | `string` |
| `$.timezone.country` | `string` |

---

## 1. Request

| Property | Value |
|---|---|
| Source | `sportsapipro.com` |
| Endpoint | `seasons/match/incidents` |
| Method | `GET` |
| URL | `https://api.sportsapipro.com/v2/football/match/14023935/incidents` |
| HTTP Status | `200` |
| Captured At | `2026-08-12T05:05:47.123448+00:00` |
| Raw Response | `raw/sportsapipro/seasons/match/incidents.json` |

### Query Parameters

_No query parameters._

## 2. Response Metadata

_No standard response metadata detected._

---

## 3. Record Counts

_No top-level arrays detected._

---

## 4. Response Structure

The following structure is automatically derived from the
complete JSON response.

| JSON Path | Type |
|---|---|
| `$.success` | `boolean` |
| `$.matchId` | `integer` |
| `$.endpoint` | `string` |
| `$.data` | `object` |
| `$.data.incidents` | `array` |
| `$.data.incidents[]` | `object` |
| `$.data.incidents[].text` | `string` |
| `$.data.incidents[].homeScore` | `integer` |
| `$.data.incidents[].awayScore` | `integer` |
| `$.data.incidents[].isLive` | `boolean` |
| `$.data.incidents[].time` | `integer` |
| `$.data.incidents[].addedTime` | `integer` |
| `$.data.incidents[].timeSeconds` | `integer` |
| `$.data.incidents[].incidentType` | `string` |
| `$.data.incidents[].reversedPeriodTime` | `integer` |
| `$.data.incidents[].reversedPeriodTimeSeconds` | `integer` |
| `$.data.incidents[].periodTimeSeconds` | `integer` |
| `$.data.home` | `object` |
| `$.data.home.goalkeeperColor` | `object` |
| `$.data.home.goalkeeperColor.primary` | `string` |
| `$.data.home.goalkeeperColor.number` | `string` |
| `$.data.home.goalkeeperColor.outline` | `string` |
| `$.data.home.goalkeeperColor.fancyNumber` | `string` |
| `$.data.home.playerColor` | `object` |
| `$.data.home.playerColor.primary` | `string` |
| `$.data.home.playerColor.number` | `string` |
| `$.data.home.playerColor.outline` | `string` |
| `$.data.home.playerColor.fancyNumber` | `string` |
| `$.data.away` | `object` |
| `$.data.away.goalkeeperColor` | `object` |
| `$.data.away.goalkeeperColor.primary` | `string` |
| `$.data.away.goalkeeperColor.number` | `string` |
| `$.data.away.goalkeeperColor.outline` | `string` |
| `$.data.away.goalkeeperColor.fancyNumber` | `string` |
| `$.data.away.playerColor` | `object` |
| `$.data.away.playerColor.primary` | `string` |
| `$.data.away.playerColor.number` | `string` |
| `$.data.away.playerColor.outline` | `string` |
| `$.data.away.playerColor.fancyNumber` | `string` |
| `$.source` | `string` |
| `$.cacheHit` | `boolean` |
| `$.timezone` | `object` |
| `$.timezone.name` | `string` |
| `$.timezone.utcOffset` | `string` |
| `$.timezone.source` | `string` |
| `$.timezone.country` | `string` |

---

## 1. Request

| Property | Value |
|---|---|
| Source | `sportsapipro.com` |
| Endpoint | `seasons/match/shotmap` |
| Method | `GET` |
| URL | `https://api.sportsapipro.com/v2/football/match/14023935/shotmap` |
| HTTP Status | `200` |
| Captured At | `2026-08-12T05:08:39.274792+00:00` |
| Raw Response | `raw/sportsapipro/seasons/match/shotmap.json` |

### Query Parameters

_No query parameters._

## 2. Response Metadata

_No standard response metadata detected._

---

## 3. Record Counts

_No top-level arrays detected._

---

## 4. Response Structure

The following structure is automatically derived from the
complete JSON response.

| JSON Path | Type |
|---|---|
| `$.success` | `boolean` |
| `$.matchId` | `integer` |
| `$.endpoint` | `string` |
| `$.data` | `object` |
| `$.data.shotmap` | `array` |
| `$.data.shotmap[]` | `object` |
| `$.data.shotmap[].player` | `object` |
| `$.data.shotmap[].player.name` | `string` |
| `$.data.shotmap[].player.firstName` | `string` |
| `$.data.shotmap[].player.lastName` | `string` |
| `$.data.shotmap[].player.slug` | `string` |
| `$.data.shotmap[].player.shortName` | `string` |
| `$.data.shotmap[].player.position` | `string` |
| `$.data.shotmap[].player.jerseyNumber` | `string` |
| `$.data.shotmap[].player.userCount` | `integer` |
| `$.data.shotmap[].player.gender` | `string` |
| `$.data.shotmap[].player.id` | `integer` |
| `$.data.shotmap[].player.fieldTranslations` | `object` |
| `$.data.shotmap[].player.fieldTranslations.nameTranslation` | `object` |
| `$.data.shotmap[].player.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.shotmap[].player.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.shotmap[].player.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.shotmap[].player.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.shotmap[].player.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.shotmap[].player.fieldTranslations.shortNameTranslation.ar` | `string` |
| `$.data.shotmap[].player.fieldTranslations.shortNameTranslation.bn` | `string` |
| `$.data.shotmap[].player.fieldTranslations.shortNameTranslation.hi` | `string` |
| `$.data.shotmap[].player.fieldTranslations.shortNameTranslation.ru` | `string` |
| `$.data.shotmap[].isHome` | `boolean` |
| `$.data.shotmap[].shotType` | `string` |
| `$.data.shotmap[].situation` | `string` |
| `$.data.shotmap[].playerCoordinates` | `object` |
| `$.data.shotmap[].playerCoordinates.x` | `number` |
| `$.data.shotmap[].playerCoordinates.y` | `number` |
| `$.data.shotmap[].playerCoordinates.z` | `integer` |
| `$.data.shotmap[].bodyPart` | `string` |
| `$.data.shotmap[].goalMouthLocation` | `string` |
| `$.data.shotmap[].goalMouthCoordinates` | `object` |
| `$.data.shotmap[].goalMouthCoordinates.x` | `integer` |
| `$.data.shotmap[].goalMouthCoordinates.y` | `number` |
| `$.data.shotmap[].goalMouthCoordinates.z` | `number` |
| `$.data.shotmap[].xg` | `number` |
| `$.data.shotmap[].xgot` | `integer` |
| `$.data.shotmap[].goalkeeper` | `object` |
| `$.data.shotmap[].goalkeeper.name` | `string` |
| `$.data.shotmap[].goalkeeper.slug` | `string` |
| `$.data.shotmap[].goalkeeper.shortName` | `string` |
| `$.data.shotmap[].goalkeeper.position` | `string` |
| `$.data.shotmap[].goalkeeper.jerseyNumber` | `string` |
| `$.data.shotmap[].goalkeeper.userCount` | `integer` |
| `$.data.shotmap[].goalkeeper.gender` | `string` |
| `$.data.shotmap[].goalkeeper.id` | `integer` |
| `$.data.shotmap[].goalkeeper.fieldTranslations` | `object` |
| `$.data.shotmap[].goalkeeper.fieldTranslations.nameTranslation` | `object` |
| `$.data.shotmap[].goalkeeper.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.shotmap[].goalkeeper.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.shotmap[].goalkeeper.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.shotmap[].goalkeeper.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.shotmap[].goalkeeper.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.shotmap[].goalkeeper.fieldTranslations.shortNameTranslation.ar` | `string` |
| `$.data.shotmap[].goalkeeper.fieldTranslations.shortNameTranslation.bn` | `string` |
| `$.data.shotmap[].goalkeeper.fieldTranslations.shortNameTranslation.hi` | `string` |
| `$.data.shotmap[].goalkeeper.fieldTranslations.shortNameTranslation.ru` | `string` |
| `$.data.shotmap[].id` | `integer` |
| `$.data.shotmap[].time` | `integer` |
| `$.data.shotmap[].addedTime` | `integer` |
| `$.data.shotmap[].timeSeconds` | `integer` |
| `$.data.shotmap[].draw` | `object` |
| `$.data.shotmap[].draw.start` | `object` |
| `$.data.shotmap[].draw.start.x` | `number` |
| `$.data.shotmap[].draw.start.y` | `number` |
| `$.data.shotmap[].draw.end` | `object` |
| `$.data.shotmap[].draw.end.x` | `number` |
| `$.data.shotmap[].draw.end.y` | `integer` |
| `$.data.shotmap[].draw.goal` | `object` |
| `$.data.shotmap[].draw.goal.x` | `number` |
| `$.data.shotmap[].draw.goal.y` | `number` |
| `$.data.shotmap[].incidentType` | `string` |
| `$.data.shotmap[].reversedPeriodTime` | `integer` |
| `$.data.shotmap[].reversedPeriodTimeSeconds` | `integer` |
| `$.data.shotmap[].periodTimeSeconds` | `integer` |
| `$.source` | `string` |
| `$.cacheHit` | `boolean` |
| `$.timezone` | `object` |
| `$.timezone.name` | `string` |
| `$.timezone.utcOffset` | `string` |
| `$.timezone.source` | `string` |
| `$.timezone.country` | `string` |

---

## 1. Request

| Property | Value |
|---|---|
| Source | `sportsapipro.com` |
| Endpoint | `seasons/match/graph` |
| Method | `GET` |
| URL | `https://api.sportsapipro.com/v2/football/match/14023935/graph` |
| HTTP Status | `200` |
| Captured At | `2026-08-12T05:09:35.079576+00:00` |
| Raw Response | `raw/sportsapipro/seasons/match/graph.json` |

### Query Parameters

_No query parameters._

## 2. Response Metadata

_No standard response metadata detected._

---

## 3. Record Counts

_No top-level arrays detected._

---

## 4. Response Structure

The following structure is automatically derived from the
complete JSON response.

| JSON Path | Type |
|---|---|
| `$.success` | `boolean` |
| `$.matchId` | `integer` |
| `$.endpoint` | `string` |
| `$.data` | `object` |
| `$.data.graphPoints` | `array` |
| `$.data.graphPoints[]` | `object` |
| `$.data.graphPoints[].minute` | `integer` |
| `$.data.graphPoints[].value` | `integer` |
| `$.data.graphPointsV2` | `array` |
| `$.data.periodTime` | `integer` |
| `$.data.overtimeLength` | `integer` |
| `$.data.periodCount` | `integer` |
| `$.source` | `string` |
| `$.cacheHit` | `boolean` |
| `$.timezone` | `object` |
| `$.timezone.name` | `string` |
| `$.timezone.utcOffset` | `string` |
| `$.timezone.source` | `string` |
| `$.timezone.country` | `string` |

---

## 1. Request

| Property | Value |
|---|---|
| Source | `sportsapipro.com` |
| Endpoint | `seasons/match/average-positions` |
| Method | `GET` |
| URL | `https://api.sportsapipro.com/v2/football/match/14023935/average-positions` |
| HTTP Status | `200` |
| Captured At | `2026-08-12T05:10:03.080800+00:00` |
| Raw Response | `raw/sportsapipro/seasons/match/average-positions.json` |

### Query Parameters

_No query parameters._

## 2. Response Metadata

_No standard response metadata detected._

---

## 3. Record Counts

_No top-level arrays detected._

---

## 4. Response Structure

The following structure is automatically derived from the
complete JSON response.

| JSON Path | Type |
|---|---|
| `$.success` | `boolean` |
| `$.matchId` | `integer` |
| `$.endpoint` | `string` |
| `$.data` | `object` |
| `$.data.home` | `array` |
| `$.data.home[]` | `object` |
| `$.data.home[].player` | `object` |
| `$.data.home[].player.name` | `string` |
| `$.data.home[].player.firstName` | `string` |
| `$.data.home[].player.slug` | `string` |
| `$.data.home[].player.shortName` | `string` |
| `$.data.home[].player.position` | `string` |
| `$.data.home[].player.jerseyNumber` | `string` |
| `$.data.home[].player.userCount` | `integer` |
| `$.data.home[].player.gender` | `string` |
| `$.data.home[].player.id` | `integer` |
| `$.data.home[].player.fieldTranslations` | `object` |
| `$.data.home[].player.fieldTranslations.nameTranslation` | `object` |
| `$.data.home[].player.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.home[].player.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.home[].player.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.home[].player.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.home[].player.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.home[].player.fieldTranslations.shortNameTranslation.ar` | `string` |
| `$.data.home[].player.fieldTranslations.shortNameTranslation.bn` | `string` |
| `$.data.home[].player.fieldTranslations.shortNameTranslation.hi` | `string` |
| `$.data.home[].player.fieldTranslations.shortNameTranslation.ru` | `string` |
| `$.data.home[].averageX` | `integer` |
| `$.data.home[].averageY` | `number` |
| `$.data.home[].pointsCount` | `integer` |
| `$.data.away` | `array` |
| `$.data.away[]` | `object` |
| `$.data.away[].player` | `object` |
| `$.data.away[].player.name` | `string` |
| `$.data.away[].player.firstName` | `string` |
| `$.data.away[].player.lastName` | `string` |
| `$.data.away[].player.slug` | `string` |
| `$.data.away[].player.shortName` | `string` |
| `$.data.away[].player.position` | `string` |
| `$.data.away[].player.jerseyNumber` | `string` |
| `$.data.away[].player.userCount` | `integer` |
| `$.data.away[].player.gender` | `string` |
| `$.data.away[].player.id` | `integer` |
| `$.data.away[].player.fieldTranslations` | `object` |
| `$.data.away[].player.fieldTranslations.nameTranslation` | `object` |
| `$.data.away[].player.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.away[].player.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.away[].player.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.away[].player.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.away[].player.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.away[].player.fieldTranslations.shortNameTranslation.ar` | `string` |
| `$.data.away[].player.fieldTranslations.shortNameTranslation.bn` | `string` |
| `$.data.away[].player.fieldTranslations.shortNameTranslation.hi` | `string` |
| `$.data.away[].player.fieldTranslations.shortNameTranslation.ru` | `string` |
| `$.data.away[].averageX` | `number` |
| `$.data.away[].averageY` | `number` |
| `$.data.away[].pointsCount` | `integer` |
| `$.data.substitutions` | `array` |
| `$.data.substitutions[]` | `object` |
| `$.data.substitutions[].playerIn` | `object` |
| `$.data.substitutions[].playerIn.name` | `string` |
| `$.data.substitutions[].playerIn.slug` | `string` |
| `$.data.substitutions[].playerIn.shortName` | `string` |
| `$.data.substitutions[].playerIn.position` | `string` |
| `$.data.substitutions[].playerIn.jerseyNumber` | `string` |
| `$.data.substitutions[].playerIn.userCount` | `integer` |
| `$.data.substitutions[].playerIn.gender` | `string` |
| `$.data.substitutions[].playerIn.id` | `integer` |
| `$.data.substitutions[].playerIn.fieldTranslations` | `object` |
| `$.data.substitutions[].playerIn.fieldTranslations.nameTranslation` | `object` |
| `$.data.substitutions[].playerIn.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.substitutions[].playerIn.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.substitutions[].playerIn.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.substitutions[].playerIn.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.substitutions[].playerIn.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.substitutions[].playerIn.fieldTranslations.shortNameTranslation.ar` | `string` |
| `$.data.substitutions[].playerIn.fieldTranslations.shortNameTranslation.bn` | `string` |
| `$.data.substitutions[].playerIn.fieldTranslations.shortNameTranslation.hi` | `string` |
| `$.data.substitutions[].playerIn.fieldTranslations.shortNameTranslation.ru` | `string` |
| `$.data.substitutions[].playerOut` | `object` |
| `$.data.substitutions[].playerOut.name` | `string` |
| `$.data.substitutions[].playerOut.firstName` | `string` |
| `$.data.substitutions[].playerOut.lastName` | `string` |
| `$.data.substitutions[].playerOut.slug` | `string` |
| `$.data.substitutions[].playerOut.shortName` | `string` |
| `$.data.substitutions[].playerOut.position` | `string` |
| `$.data.substitutions[].playerOut.jerseyNumber` | `string` |
| `$.data.substitutions[].playerOut.userCount` | `integer` |
| `$.data.substitutions[].playerOut.gender` | `string` |
| `$.data.substitutions[].playerOut.id` | `integer` |
| `$.data.substitutions[].playerOut.fieldTranslations` | `object` |
| `$.data.substitutions[].playerOut.fieldTranslations.nameTranslation` | `object` |
| `$.data.substitutions[].playerOut.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.substitutions[].playerOut.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.substitutions[].playerOut.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.substitutions[].playerOut.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.substitutions[].playerOut.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.substitutions[].playerOut.fieldTranslations.shortNameTranslation.ar` | `string` |
| `$.data.substitutions[].playerOut.fieldTranslations.shortNameTranslation.bn` | `string` |
| `$.data.substitutions[].playerOut.fieldTranslations.shortNameTranslation.hi` | `string` |
| `$.data.substitutions[].playerOut.fieldTranslations.shortNameTranslation.ru` | `string` |
| `$.data.substitutions[].id` | `integer` |
| `$.data.substitutions[].time` | `integer` |
| `$.data.substitutions[].injury` | `boolean` |
| `$.data.substitutions[].isHome` | `boolean` |
| `$.data.substitutions[].incidentClass` | `string` |
| `$.data.substitutions[].incidentType` | `string` |
| `$.data.substitutions[].reversedPeriodTime` | `integer` |
| `$.source` | `string` |
| `$.cacheHit` | `boolean` |
| `$.timezone` | `object` |
| `$.timezone.name` | `string` |
| `$.timezone.utcOffset` | `string` |
| `$.timezone.source` | `string` |
| `$.timezone.country` | `string` |

---

## 1. Request

| Property | Value |
|---|---|
| Source | `sportsapipro.com` |
| Endpoint | `teams/players` |
| Method | `GET` |
| URL | `https://api.sportsapipro.com/v2/football/teams/30/players` |
| HTTP Status | `200` |
| Captured At | `2026-08-12T05:17:49.204578+00:00` |
| Raw Response | `raw/sportsapipro/seasons/match/players.json` |

### Query Parameters

_No query parameters._

## 2. Response Metadata

_No standard response metadata detected._

---

## 3. Record Counts

_No top-level arrays detected._

---

## 4. Response Structure

The following structure is automatically derived from the
complete JSON response.

| JSON Path | Type |
|---|---|
| `$.success` | `boolean` |
| `$.data` | `object` |
| `$.data.players` | `array` |
| `$.data.players[]` | `object` |
| `$.data.players[].player` | `object` |
| `$.data.players[].player.name` | `string` |
| `$.data.players[].player.firstName` | `string` |
| `$.data.players[].player.lastName` | `string` |
| `$.data.players[].player.slug` | `string` |
| `$.data.players[].player.shortName` | `string` |
| `$.data.players[].player.team` | `object` |
| `$.data.players[].player.team.name` | `string` |
| `$.data.players[].player.team.slug` | `string` |
| `$.data.players[].player.team.shortName` | `string` |
| `$.data.players[].player.team.gender` | `string` |
| `$.data.players[].player.team.sport` | `object` |
| `$.data.players[].player.team.sport.name` | `string` |
| `$.data.players[].player.team.sport.slug` | `string` |
| `$.data.players[].player.team.sport.id` | `integer` |
| `$.data.players[].player.team.tournament` | `object` |
| `$.data.players[].player.team.tournament.name` | `string` |
| `$.data.players[].player.team.tournament.slug` | `string` |
| `$.data.players[].player.team.tournament.category` | `object` |
| `$.data.players[].player.team.tournament.category.name` | `string` |
| `$.data.players[].player.team.tournament.category.slug` | `string` |
| `$.data.players[].player.team.tournament.category.sport` | `object` |
| `$.data.players[].player.team.tournament.category.sport.name` | `string` |
| `$.data.players[].player.team.tournament.category.sport.slug` | `string` |
| `$.data.players[].player.team.tournament.category.sport.id` | `integer` |
| `$.data.players[].player.team.tournament.category.priority` | `integer` |
| `$.data.players[].player.team.tournament.category.country` | `object` |
| `$.data.players[].player.team.tournament.category.country.alpha2` | `string` |
| `$.data.players[].player.team.tournament.category.country.alpha3` | `string` |
| `$.data.players[].player.team.tournament.category.country.name` | `string` |
| `$.data.players[].player.team.tournament.category.country.slug` | `string` |
| `$.data.players[].player.team.tournament.category.id` | `integer` |
| `$.data.players[].player.team.tournament.category.flag` | `string` |
| `$.data.players[].player.team.tournament.category.alpha2` | `string` |
| `$.data.players[].player.team.tournament.category.fieldTranslations` | `object` |
| `$.data.players[].player.team.tournament.category.fieldTranslations.nameTranslation` | `object` |
| `$.data.players[].player.team.tournament.category.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.players[].player.team.tournament.category.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.players[].player.team.tournament.category.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.players[].player.team.tournament.category.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.players[].player.team.tournament.category.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.players[].player.team.tournament.uniqueTournament` | `object` |
| `$.data.players[].player.team.tournament.uniqueTournament.name` | `string` |
| `$.data.players[].player.team.tournament.uniqueTournament.slug` | `string` |
| `$.data.players[].player.team.tournament.uniqueTournament.primaryColorHex` | `string` |
| `$.data.players[].player.team.tournament.uniqueTournament.secondaryColorHex` | `string` |
| `$.data.players[].player.team.tournament.uniqueTournament.category` | `object` |
| `$.data.players[].player.team.tournament.uniqueTournament.category.name` | `string` |
| `$.data.players[].player.team.tournament.uniqueTournament.category.slug` | `string` |
| `$.data.players[].player.team.tournament.uniqueTournament.category.sport` | `object` |
| `$.data.players[].player.team.tournament.uniqueTournament.category.sport.name` | `string` |
| `$.data.players[].player.team.tournament.uniqueTournament.category.sport.slug` | `string` |
| `$.data.players[].player.team.tournament.uniqueTournament.category.sport.id` | `integer` |
| `$.data.players[].player.team.tournament.uniqueTournament.category.priority` | `integer` |
| `$.data.players[].player.team.tournament.uniqueTournament.category.country` | `object` |
| `$.data.players[].player.team.tournament.uniqueTournament.category.country.alpha2` | `string` |
| `$.data.players[].player.team.tournament.uniqueTournament.category.country.alpha3` | `string` |
| `$.data.players[].player.team.tournament.uniqueTournament.category.country.name` | `string` |
| `$.data.players[].player.team.tournament.uniqueTournament.category.country.slug` | `string` |
| `$.data.players[].player.team.tournament.uniqueTournament.category.id` | `integer` |
| `$.data.players[].player.team.tournament.uniqueTournament.category.flag` | `string` |
| `$.data.players[].player.team.tournament.uniqueTournament.category.alpha2` | `string` |
| `$.data.players[].player.team.tournament.uniqueTournament.category.fieldTranslations` | `object` |
| `$.data.players[].player.team.tournament.uniqueTournament.category.fieldTranslations.nameTranslation` | `object` |
| `$.data.players[].player.team.tournament.uniqueTournament.category.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.players[].player.team.tournament.uniqueTournament.category.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.players[].player.team.tournament.uniqueTournament.category.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.players[].player.team.tournament.uniqueTournament.category.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.players[].player.team.tournament.uniqueTournament.category.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.players[].player.team.tournament.uniqueTournament.userCount` | `integer` |
| `$.data.players[].player.team.tournament.uniqueTournament.country` | `object` |
| `$.data.players[].player.team.tournament.uniqueTournament.id` | `integer` |
| `$.data.players[].player.team.tournament.uniqueTournament.displayInverseHomeAwayTeams` | `boolean` |
| `$.data.players[].player.team.tournament.uniqueTournament.fieldTranslations` | `object` |
| `$.data.players[].player.team.tournament.uniqueTournament.fieldTranslations.nameTranslation` | `object` |
| `$.data.players[].player.team.tournament.uniqueTournament.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.players[].player.team.tournament.uniqueTournament.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.players[].player.team.tournament.uniqueTournament.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.players[].player.team.tournament.uniqueTournament.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.players[].player.team.tournament.uniqueTournament.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.players[].player.team.tournament.priority` | `integer` |
| `$.data.players[].player.team.tournament.isLive` | `boolean` |
| `$.data.players[].player.team.tournament.id` | `integer` |
| `$.data.players[].player.team.tournament.fieldTranslations` | `object` |
| `$.data.players[].player.team.tournament.fieldTranslations.nameTranslation` | `object` |
| `$.data.players[].player.team.tournament.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.players[].player.team.tournament.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.players[].player.team.tournament.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.players[].player.team.tournament.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.players[].player.team.tournament.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.players[].player.team.primaryUniqueTournament` | `object` |
| `$.data.players[].player.team.primaryUniqueTournament.name` | `string` |
| `$.data.players[].player.team.primaryUniqueTournament.slug` | `string` |
| `$.data.players[].player.team.primaryUniqueTournament.primaryColorHex` | `string` |
| `$.data.players[].player.team.primaryUniqueTournament.secondaryColorHex` | `string` |
| `$.data.players[].player.team.primaryUniqueTournament.category` | `object` |
| `$.data.players[].player.team.primaryUniqueTournament.category.name` | `string` |
| `$.data.players[].player.team.primaryUniqueTournament.category.slug` | `string` |
| `$.data.players[].player.team.primaryUniqueTournament.category.sport` | `object` |
| `$.data.players[].player.team.primaryUniqueTournament.category.sport.name` | `string` |
| `$.data.players[].player.team.primaryUniqueTournament.category.sport.slug` | `string` |
| `$.data.players[].player.team.primaryUniqueTournament.category.sport.id` | `integer` |
| `$.data.players[].player.team.primaryUniqueTournament.category.priority` | `integer` |
| `$.data.players[].player.team.primaryUniqueTournament.category.country` | `object` |
| `$.data.players[].player.team.primaryUniqueTournament.category.country.alpha2` | `string` |
| `$.data.players[].player.team.primaryUniqueTournament.category.country.alpha3` | `string` |
| `$.data.players[].player.team.primaryUniqueTournament.category.country.name` | `string` |
| `$.data.players[].player.team.primaryUniqueTournament.category.country.slug` | `string` |
| `$.data.players[].player.team.primaryUniqueTournament.category.id` | `integer` |
| `$.data.players[].player.team.primaryUniqueTournament.category.flag` | `string` |
| `$.data.players[].player.team.primaryUniqueTournament.category.alpha2` | `string` |
| `$.data.players[].player.team.primaryUniqueTournament.category.fieldTranslations` | `object` |
| `$.data.players[].player.team.primaryUniqueTournament.category.fieldTranslations.nameTranslation` | `object` |
| `$.data.players[].player.team.primaryUniqueTournament.category.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.players[].player.team.primaryUniqueTournament.category.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.players[].player.team.primaryUniqueTournament.category.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.players[].player.team.primaryUniqueTournament.category.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.players[].player.team.primaryUniqueTournament.category.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.players[].player.team.primaryUniqueTournament.userCount` | `integer` |
| `$.data.players[].player.team.primaryUniqueTournament.country` | `object` |
| `$.data.players[].player.team.primaryUniqueTournament.id` | `integer` |
| `$.data.players[].player.team.primaryUniqueTournament.displayInverseHomeAwayTeams` | `boolean` |
| `$.data.players[].player.team.primaryUniqueTournament.fieldTranslations` | `object` |
| `$.data.players[].player.team.primaryUniqueTournament.fieldTranslations.nameTranslation` | `object` |
| `$.data.players[].player.team.primaryUniqueTournament.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.players[].player.team.primaryUniqueTournament.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.players[].player.team.primaryUniqueTournament.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.players[].player.team.primaryUniqueTournament.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.players[].player.team.primaryUniqueTournament.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.players[].player.team.userCount` | `integer` |
| `$.data.players[].player.team.nameCode` | `string` |
| `$.data.players[].player.team.disabled` | `boolean` |
| `$.data.players[].player.team.national` | `boolean` |
| `$.data.players[].player.team.type` | `integer` |
| `$.data.players[].player.team.country` | `object` |
| `$.data.players[].player.team.country.alpha2` | `string` |
| `$.data.players[].player.team.country.alpha3` | `string` |
| `$.data.players[].player.team.country.name` | `string` |
| `$.data.players[].player.team.country.slug` | `string` |
| `$.data.players[].player.team.id` | `integer` |
| `$.data.players[].player.team.teamColors` | `object` |
| `$.data.players[].player.team.teamColors.primary` | `string` |
| `$.data.players[].player.team.teamColors.secondary` | `string` |
| `$.data.players[].player.team.teamColors.text` | `string` |
| `$.data.players[].player.team.fieldTranslations` | `object` |
| `$.data.players[].player.team.fieldTranslations.nameTranslation` | `object` |
| `$.data.players[].player.team.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.players[].player.team.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.players[].player.team.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.players[].player.team.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.players[].player.team.fieldTranslations.shortNameTranslation.ar` | `string` |
| `$.data.players[].player.team.fieldTranslations.shortNameTranslation.bn` | `string` |
| `$.data.players[].player.team.fieldTranslations.shortNameTranslation.hi` | `string` |
| `$.data.players[].player.position` | `string` |
| `$.data.players[].player.positionsDetailed` | `array` |
| `$.data.players[].player.positionsDetailed[]` | `string` |
| `$.data.players[].player.jerseyNumber` | `string` |
| `$.data.players[].player.height` | `integer` |
| `$.data.players[].player.dateOfBirth` | `string` |
| `$.data.players[].player.preferredFoot` | `string` |
| `$.data.players[].player.retired` | `boolean` |
| `$.data.players[].player.userCount` | `integer` |
| `$.data.players[].player.gender` | `string` |
| `$.data.players[].player.injury` | `object` |
| `$.data.players[].player.injury.reason` | `string` |
| `$.data.players[].player.injury.status` | `string` |
| `$.data.players[].player.injury.expectedReturn` | `integer` |
| `$.data.players[].player.injury.id` | `integer` |
| `$.data.players[].player.injury.startDateTimestamp` | `integer` |
| `$.data.players[].player.injury.updateDateTimestamp` | `integer` |
| `$.data.players[].player.injury.endDateTimestamp` | `integer` |
| `$.data.players[].player.injury.expectedReturnDateData` | `object` |
| `$.data.players[].player.injury.expectedReturnDateData.month` | `integer` |
| `$.data.players[].player.injury.expectedReturnDateData.year` | `integer` |
| `$.data.players[].player.country` | `object` |
| `$.data.players[].player.country.alpha2` | `string` |
| `$.data.players[].player.country.alpha3` | `string` |
| `$.data.players[].player.country.name` | `string` |
| `$.data.players[].player.country.slug` | `string` |
| `$.data.players[].player.id` | `integer` |
| `$.data.players[].player.underage` | `boolean` |
| `$.data.players[].player.shirtNumber` | `integer` |
| `$.data.players[].player.dateOfBirthTimestamp` | `integer` |
| `$.data.players[].player.contractUntilTimestamp` | `integer` |
| `$.data.players[].player.proposedMarketValue` | `integer` |
| `$.data.players[].player.proposedMarketValueRaw` | `object` |
| `$.data.players[].player.proposedMarketValueRaw.value` | `integer` |
| `$.data.players[].player.proposedMarketValueRaw.currency` | `string` |
| `$.data.players[].player.fieldTranslations` | `object` |
| `$.data.players[].player.fieldTranslations.nameTranslation` | `object` |
| `$.data.players[].player.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.players[].player.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.players[].player.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.players[].player.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.players[].player.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.players[].player.fieldTranslations.shortNameTranslation.ar` | `string` |
| `$.data.players[].player.fieldTranslations.shortNameTranslation.bn` | `string` |
| `$.data.players[].player.fieldTranslations.shortNameTranslation.hi` | `string` |
| `$.data.players[].player.fieldTranslations.shortNameTranslation.ru` | `string` |
| `$.data.foreignPlayers` | `array` |
| `$.data.foreignPlayers[]` | `object` |
| `$.data.foreignPlayers[].player` | `object` |
| `$.data.foreignPlayers[].player.name` | `string` |
| `$.data.foreignPlayers[].player.firstName` | `string` |
| `$.data.foreignPlayers[].player.lastName` | `string` |
| `$.data.foreignPlayers[].player.slug` | `string` |
| `$.data.foreignPlayers[].player.shortName` | `string` |
| `$.data.foreignPlayers[].player.team` | `object` |
| `$.data.foreignPlayers[].player.team.name` | `string` |
| `$.data.foreignPlayers[].player.team.slug` | `string` |
| `$.data.foreignPlayers[].player.team.shortName` | `string` |
| `$.data.foreignPlayers[].player.team.gender` | `string` |
| `$.data.foreignPlayers[].player.team.sport` | `object` |
| `$.data.foreignPlayers[].player.team.sport.name` | `string` |
| `$.data.foreignPlayers[].player.team.sport.slug` | `string` |
| `$.data.foreignPlayers[].player.team.sport.id` | `integer` |
| `$.data.foreignPlayers[].player.team.tournament` | `object` |
| `$.data.foreignPlayers[].player.team.tournament.name` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.slug` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.category` | `object` |
| `$.data.foreignPlayers[].player.team.tournament.category.name` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.category.slug` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.category.sport` | `object` |
| `$.data.foreignPlayers[].player.team.tournament.category.sport.name` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.category.sport.slug` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.category.sport.id` | `integer` |
| `$.data.foreignPlayers[].player.team.tournament.category.priority` | `integer` |
| `$.data.foreignPlayers[].player.team.tournament.category.country` | `object` |
| `$.data.foreignPlayers[].player.team.tournament.category.country.alpha2` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.category.country.alpha3` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.category.country.name` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.category.country.slug` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.category.id` | `integer` |
| `$.data.foreignPlayers[].player.team.tournament.category.flag` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.category.alpha2` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.category.fieldTranslations` | `object` |
| `$.data.foreignPlayers[].player.team.tournament.category.fieldTranslations.nameTranslation` | `object` |
| `$.data.foreignPlayers[].player.team.tournament.category.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.category.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.category.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.category.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.category.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.foreignPlayers[].player.team.tournament.uniqueTournament` | `object` |
| `$.data.foreignPlayers[].player.team.tournament.uniqueTournament.name` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.uniqueTournament.slug` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.uniqueTournament.primaryColorHex` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.uniqueTournament.secondaryColorHex` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.uniqueTournament.category` | `object` |
| `$.data.foreignPlayers[].player.team.tournament.uniqueTournament.category.name` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.uniqueTournament.category.slug` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.uniqueTournament.category.sport` | `object` |
| `$.data.foreignPlayers[].player.team.tournament.uniqueTournament.category.sport.name` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.uniqueTournament.category.sport.slug` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.uniqueTournament.category.sport.id` | `integer` |
| `$.data.foreignPlayers[].player.team.tournament.uniqueTournament.category.priority` | `integer` |
| `$.data.foreignPlayers[].player.team.tournament.uniqueTournament.category.country` | `object` |
| `$.data.foreignPlayers[].player.team.tournament.uniqueTournament.category.country.alpha2` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.uniqueTournament.category.country.alpha3` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.uniqueTournament.category.country.name` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.uniqueTournament.category.country.slug` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.uniqueTournament.category.id` | `integer` |
| `$.data.foreignPlayers[].player.team.tournament.uniqueTournament.category.flag` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.uniqueTournament.category.alpha2` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.uniqueTournament.category.fieldTranslations` | `object` |
| `$.data.foreignPlayers[].player.team.tournament.uniqueTournament.category.fieldTranslations.nameTranslation` | `object` |
| `$.data.foreignPlayers[].player.team.tournament.uniqueTournament.category.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.uniqueTournament.category.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.uniqueTournament.category.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.uniqueTournament.category.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.uniqueTournament.category.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.foreignPlayers[].player.team.tournament.uniqueTournament.userCount` | `integer` |
| `$.data.foreignPlayers[].player.team.tournament.uniqueTournament.country` | `object` |
| `$.data.foreignPlayers[].player.team.tournament.uniqueTournament.id` | `integer` |
| `$.data.foreignPlayers[].player.team.tournament.uniqueTournament.displayInverseHomeAwayTeams` | `boolean` |
| `$.data.foreignPlayers[].player.team.tournament.uniqueTournament.fieldTranslations` | `object` |
| `$.data.foreignPlayers[].player.team.tournament.uniqueTournament.fieldTranslations.nameTranslation` | `object` |
| `$.data.foreignPlayers[].player.team.tournament.uniqueTournament.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.uniqueTournament.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.uniqueTournament.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.uniqueTournament.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.uniqueTournament.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.foreignPlayers[].player.team.tournament.priority` | `integer` |
| `$.data.foreignPlayers[].player.team.tournament.isLive` | `boolean` |
| `$.data.foreignPlayers[].player.team.tournament.id` | `integer` |
| `$.data.foreignPlayers[].player.team.tournament.fieldTranslations` | `object` |
| `$.data.foreignPlayers[].player.team.tournament.fieldTranslations.nameTranslation` | `object` |
| `$.data.foreignPlayers[].player.team.tournament.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.foreignPlayers[].player.team.tournament.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.foreignPlayers[].player.team.primaryUniqueTournament` | `object` |
| `$.data.foreignPlayers[].player.team.primaryUniqueTournament.name` | `string` |
| `$.data.foreignPlayers[].player.team.primaryUniqueTournament.slug` | `string` |
| `$.data.foreignPlayers[].player.team.primaryUniqueTournament.primaryColorHex` | `string` |
| `$.data.foreignPlayers[].player.team.primaryUniqueTournament.secondaryColorHex` | `string` |
| `$.data.foreignPlayers[].player.team.primaryUniqueTournament.category` | `object` |
| `$.data.foreignPlayers[].player.team.primaryUniqueTournament.category.name` | `string` |
| `$.data.foreignPlayers[].player.team.primaryUniqueTournament.category.slug` | `string` |
| `$.data.foreignPlayers[].player.team.primaryUniqueTournament.category.sport` | `object` |
| `$.data.foreignPlayers[].player.team.primaryUniqueTournament.category.sport.name` | `string` |
| `$.data.foreignPlayers[].player.team.primaryUniqueTournament.category.sport.slug` | `string` |
| `$.data.foreignPlayers[].player.team.primaryUniqueTournament.category.sport.id` | `integer` |
| `$.data.foreignPlayers[].player.team.primaryUniqueTournament.category.priority` | `integer` |
| `$.data.foreignPlayers[].player.team.primaryUniqueTournament.category.country` | `object` |
| `$.data.foreignPlayers[].player.team.primaryUniqueTournament.category.country.alpha2` | `string` |
| `$.data.foreignPlayers[].player.team.primaryUniqueTournament.category.country.alpha3` | `string` |
| `$.data.foreignPlayers[].player.team.primaryUniqueTournament.category.country.name` | `string` |
| `$.data.foreignPlayers[].player.team.primaryUniqueTournament.category.country.slug` | `string` |
| `$.data.foreignPlayers[].player.team.primaryUniqueTournament.category.id` | `integer` |
| `$.data.foreignPlayers[].player.team.primaryUniqueTournament.category.flag` | `string` |
| `$.data.foreignPlayers[].player.team.primaryUniqueTournament.category.alpha2` | `string` |
| `$.data.foreignPlayers[].player.team.primaryUniqueTournament.category.fieldTranslations` | `object` |
| `$.data.foreignPlayers[].player.team.primaryUniqueTournament.category.fieldTranslations.nameTranslation` | `object` |
| `$.data.foreignPlayers[].player.team.primaryUniqueTournament.category.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.foreignPlayers[].player.team.primaryUniqueTournament.category.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.foreignPlayers[].player.team.primaryUniqueTournament.category.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.foreignPlayers[].player.team.primaryUniqueTournament.category.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.foreignPlayers[].player.team.primaryUniqueTournament.category.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.foreignPlayers[].player.team.primaryUniqueTournament.userCount` | `integer` |
| `$.data.foreignPlayers[].player.team.primaryUniqueTournament.country` | `object` |
| `$.data.foreignPlayers[].player.team.primaryUniqueTournament.id` | `integer` |
| `$.data.foreignPlayers[].player.team.primaryUniqueTournament.displayInverseHomeAwayTeams` | `boolean` |
| `$.data.foreignPlayers[].player.team.primaryUniqueTournament.fieldTranslations` | `object` |
| `$.data.foreignPlayers[].player.team.primaryUniqueTournament.fieldTranslations.nameTranslation` | `object` |
| `$.data.foreignPlayers[].player.team.primaryUniqueTournament.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.foreignPlayers[].player.team.primaryUniqueTournament.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.foreignPlayers[].player.team.primaryUniqueTournament.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.foreignPlayers[].player.team.primaryUniqueTournament.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.foreignPlayers[].player.team.primaryUniqueTournament.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.foreignPlayers[].player.team.userCount` | `integer` |
| `$.data.foreignPlayers[].player.team.nameCode` | `string` |
| `$.data.foreignPlayers[].player.team.disabled` | `boolean` |
| `$.data.foreignPlayers[].player.team.national` | `boolean` |
| `$.data.foreignPlayers[].player.team.type` | `integer` |
| `$.data.foreignPlayers[].player.team.country` | `object` |
| `$.data.foreignPlayers[].player.team.country.alpha2` | `string` |
| `$.data.foreignPlayers[].player.team.country.alpha3` | `string` |
| `$.data.foreignPlayers[].player.team.country.name` | `string` |
| `$.data.foreignPlayers[].player.team.country.slug` | `string` |
| `$.data.foreignPlayers[].player.team.id` | `integer` |
| `$.data.foreignPlayers[].player.team.teamColors` | `object` |
| `$.data.foreignPlayers[].player.team.teamColors.primary` | `string` |
| `$.data.foreignPlayers[].player.team.teamColors.secondary` | `string` |
| `$.data.foreignPlayers[].player.team.teamColors.text` | `string` |
| `$.data.foreignPlayers[].player.team.fieldTranslations` | `object` |
| `$.data.foreignPlayers[].player.team.fieldTranslations.nameTranslation` | `object` |
| `$.data.foreignPlayers[].player.team.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.foreignPlayers[].player.team.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.foreignPlayers[].player.team.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.foreignPlayers[].player.team.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.foreignPlayers[].player.team.fieldTranslations.shortNameTranslation.ar` | `string` |
| `$.data.foreignPlayers[].player.team.fieldTranslations.shortNameTranslation.bn` | `string` |
| `$.data.foreignPlayers[].player.team.fieldTranslations.shortNameTranslation.hi` | `string` |
| `$.data.foreignPlayers[].player.position` | `string` |
| `$.data.foreignPlayers[].player.positionsDetailed` | `array` |
| `$.data.foreignPlayers[].player.positionsDetailed[]` | `string` |
| `$.data.foreignPlayers[].player.jerseyNumber` | `string` |
| `$.data.foreignPlayers[].player.height` | `integer` |
| `$.data.foreignPlayers[].player.dateOfBirth` | `string` |
| `$.data.foreignPlayers[].player.preferredFoot` | `string` |
| `$.data.foreignPlayers[].player.userCount` | `integer` |
| `$.data.foreignPlayers[].player.gender` | `string` |
| `$.data.foreignPlayers[].player.country` | `object` |
| `$.data.foreignPlayers[].player.country.alpha2` | `string` |
| `$.data.foreignPlayers[].player.country.alpha3` | `string` |
| `$.data.foreignPlayers[].player.country.name` | `string` |
| `$.data.foreignPlayers[].player.country.slug` | `string` |
| `$.data.foreignPlayers[].player.id` | `integer` |
| `$.data.foreignPlayers[].player.underage` | `boolean` |
| `$.data.foreignPlayers[].player.shirtNumber` | `integer` |
| `$.data.foreignPlayers[].player.dateOfBirthTimestamp` | `integer` |
| `$.data.foreignPlayers[].player.contractUntilTimestamp` | `integer` |
| `$.data.foreignPlayers[].player.proposedMarketValue` | `integer` |
| `$.data.foreignPlayers[].player.proposedMarketValueRaw` | `object` |
| `$.data.foreignPlayers[].player.proposedMarketValueRaw.value` | `integer` |
| `$.data.foreignPlayers[].player.proposedMarketValueRaw.currency` | `string` |
| `$.data.foreignPlayers[].player.fieldTranslations` | `object` |
| `$.data.foreignPlayers[].player.fieldTranslations.nameTranslation` | `object` |
| `$.data.foreignPlayers[].player.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.foreignPlayers[].player.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.foreignPlayers[].player.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.foreignPlayers[].player.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.foreignPlayers[].player.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.foreignPlayers[].player.fieldTranslations.shortNameTranslation.ar` | `string` |
| `$.data.foreignPlayers[].player.fieldTranslations.shortNameTranslation.bn` | `string` |
| `$.data.foreignPlayers[].player.fieldTranslations.shortNameTranslation.hi` | `string` |
| `$.data.foreignPlayers[].player.fieldTranslations.shortNameTranslation.ru` | `string` |
| `$.data.nationalPlayers` | `array` |
| `$.data.nationalPlayers[]` | `object` |
| `$.data.nationalPlayers[].player` | `object` |
| `$.data.nationalPlayers[].player.name` | `string` |
| `$.data.nationalPlayers[].player.slug` | `string` |
| `$.data.nationalPlayers[].player.shortName` | `string` |
| `$.data.nationalPlayers[].player.team` | `object` |
| `$.data.nationalPlayers[].player.team.name` | `string` |
| `$.data.nationalPlayers[].player.team.slug` | `string` |
| `$.data.nationalPlayers[].player.team.shortName` | `string` |
| `$.data.nationalPlayers[].player.team.gender` | `string` |
| `$.data.nationalPlayers[].player.team.sport` | `object` |
| `$.data.nationalPlayers[].player.team.sport.name` | `string` |
| `$.data.nationalPlayers[].player.team.sport.slug` | `string` |
| `$.data.nationalPlayers[].player.team.sport.id` | `integer` |
| `$.data.nationalPlayers[].player.team.tournament` | `object` |
| `$.data.nationalPlayers[].player.team.tournament.name` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.slug` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.category` | `object` |
| `$.data.nationalPlayers[].player.team.tournament.category.name` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.category.slug` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.category.sport` | `object` |
| `$.data.nationalPlayers[].player.team.tournament.category.sport.name` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.category.sport.slug` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.category.sport.id` | `integer` |
| `$.data.nationalPlayers[].player.team.tournament.category.priority` | `integer` |
| `$.data.nationalPlayers[].player.team.tournament.category.country` | `object` |
| `$.data.nationalPlayers[].player.team.tournament.category.country.alpha2` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.category.country.alpha3` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.category.country.name` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.category.country.slug` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.category.id` | `integer` |
| `$.data.nationalPlayers[].player.team.tournament.category.flag` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.category.alpha2` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.category.fieldTranslations` | `object` |
| `$.data.nationalPlayers[].player.team.tournament.category.fieldTranslations.nameTranslation` | `object` |
| `$.data.nationalPlayers[].player.team.tournament.category.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.category.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.category.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.category.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.category.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.nationalPlayers[].player.team.tournament.uniqueTournament` | `object` |
| `$.data.nationalPlayers[].player.team.tournament.uniqueTournament.name` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.uniqueTournament.slug` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.uniqueTournament.primaryColorHex` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.uniqueTournament.secondaryColorHex` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.uniqueTournament.category` | `object` |
| `$.data.nationalPlayers[].player.team.tournament.uniqueTournament.category.name` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.uniqueTournament.category.slug` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.uniqueTournament.category.sport` | `object` |
| `$.data.nationalPlayers[].player.team.tournament.uniqueTournament.category.sport.name` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.uniqueTournament.category.sport.slug` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.uniqueTournament.category.sport.id` | `integer` |
| `$.data.nationalPlayers[].player.team.tournament.uniqueTournament.category.priority` | `integer` |
| `$.data.nationalPlayers[].player.team.tournament.uniqueTournament.category.country` | `object` |
| `$.data.nationalPlayers[].player.team.tournament.uniqueTournament.category.country.alpha2` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.uniqueTournament.category.country.alpha3` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.uniqueTournament.category.country.name` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.uniqueTournament.category.country.slug` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.uniqueTournament.category.id` | `integer` |
| `$.data.nationalPlayers[].player.team.tournament.uniqueTournament.category.flag` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.uniqueTournament.category.alpha2` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.uniqueTournament.category.fieldTranslations` | `object` |
| `$.data.nationalPlayers[].player.team.tournament.uniqueTournament.category.fieldTranslations.nameTranslation` | `object` |
| `$.data.nationalPlayers[].player.team.tournament.uniqueTournament.category.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.uniqueTournament.category.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.uniqueTournament.category.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.uniqueTournament.category.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.uniqueTournament.category.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.nationalPlayers[].player.team.tournament.uniqueTournament.userCount` | `integer` |
| `$.data.nationalPlayers[].player.team.tournament.uniqueTournament.country` | `object` |
| `$.data.nationalPlayers[].player.team.tournament.uniqueTournament.id` | `integer` |
| `$.data.nationalPlayers[].player.team.tournament.uniqueTournament.displayInverseHomeAwayTeams` | `boolean` |
| `$.data.nationalPlayers[].player.team.tournament.uniqueTournament.fieldTranslations` | `object` |
| `$.data.nationalPlayers[].player.team.tournament.uniqueTournament.fieldTranslations.nameTranslation` | `object` |
| `$.data.nationalPlayers[].player.team.tournament.uniqueTournament.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.uniqueTournament.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.uniqueTournament.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.uniqueTournament.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.uniqueTournament.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.nationalPlayers[].player.team.tournament.priority` | `integer` |
| `$.data.nationalPlayers[].player.team.tournament.isLive` | `boolean` |
| `$.data.nationalPlayers[].player.team.tournament.id` | `integer` |
| `$.data.nationalPlayers[].player.team.tournament.fieldTranslations` | `object` |
| `$.data.nationalPlayers[].player.team.tournament.fieldTranslations.nameTranslation` | `object` |
| `$.data.nationalPlayers[].player.team.tournament.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.nationalPlayers[].player.team.tournament.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.nationalPlayers[].player.team.primaryUniqueTournament` | `object` |
| `$.data.nationalPlayers[].player.team.primaryUniqueTournament.name` | `string` |
| `$.data.nationalPlayers[].player.team.primaryUniqueTournament.slug` | `string` |
| `$.data.nationalPlayers[].player.team.primaryUniqueTournament.primaryColorHex` | `string` |
| `$.data.nationalPlayers[].player.team.primaryUniqueTournament.secondaryColorHex` | `string` |
| `$.data.nationalPlayers[].player.team.primaryUniqueTournament.category` | `object` |
| `$.data.nationalPlayers[].player.team.primaryUniqueTournament.category.name` | `string` |
| `$.data.nationalPlayers[].player.team.primaryUniqueTournament.category.slug` | `string` |
| `$.data.nationalPlayers[].player.team.primaryUniqueTournament.category.sport` | `object` |
| `$.data.nationalPlayers[].player.team.primaryUniqueTournament.category.sport.name` | `string` |
| `$.data.nationalPlayers[].player.team.primaryUniqueTournament.category.sport.slug` | `string` |
| `$.data.nationalPlayers[].player.team.primaryUniqueTournament.category.sport.id` | `integer` |
| `$.data.nationalPlayers[].player.team.primaryUniqueTournament.category.priority` | `integer` |
| `$.data.nationalPlayers[].player.team.primaryUniqueTournament.category.country` | `object` |
| `$.data.nationalPlayers[].player.team.primaryUniqueTournament.category.country.alpha2` | `string` |
| `$.data.nationalPlayers[].player.team.primaryUniqueTournament.category.country.alpha3` | `string` |
| `$.data.nationalPlayers[].player.team.primaryUniqueTournament.category.country.name` | `string` |
| `$.data.nationalPlayers[].player.team.primaryUniqueTournament.category.country.slug` | `string` |
| `$.data.nationalPlayers[].player.team.primaryUniqueTournament.category.id` | `integer` |
| `$.data.nationalPlayers[].player.team.primaryUniqueTournament.category.flag` | `string` |
| `$.data.nationalPlayers[].player.team.primaryUniqueTournament.category.alpha2` | `string` |
| `$.data.nationalPlayers[].player.team.primaryUniqueTournament.category.fieldTranslations` | `object` |
| `$.data.nationalPlayers[].player.team.primaryUniqueTournament.category.fieldTranslations.nameTranslation` | `object` |
| `$.data.nationalPlayers[].player.team.primaryUniqueTournament.category.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.nationalPlayers[].player.team.primaryUniqueTournament.category.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.nationalPlayers[].player.team.primaryUniqueTournament.category.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.nationalPlayers[].player.team.primaryUniqueTournament.category.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.nationalPlayers[].player.team.primaryUniqueTournament.category.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.nationalPlayers[].player.team.primaryUniqueTournament.userCount` | `integer` |
| `$.data.nationalPlayers[].player.team.primaryUniqueTournament.country` | `object` |
| `$.data.nationalPlayers[].player.team.primaryUniqueTournament.id` | `integer` |
| `$.data.nationalPlayers[].player.team.primaryUniqueTournament.displayInverseHomeAwayTeams` | `boolean` |
| `$.data.nationalPlayers[].player.team.primaryUniqueTournament.fieldTranslations` | `object` |
| `$.data.nationalPlayers[].player.team.primaryUniqueTournament.fieldTranslations.nameTranslation` | `object` |
| `$.data.nationalPlayers[].player.team.primaryUniqueTournament.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.nationalPlayers[].player.team.primaryUniqueTournament.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.nationalPlayers[].player.team.primaryUniqueTournament.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.nationalPlayers[].player.team.primaryUniqueTournament.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.nationalPlayers[].player.team.primaryUniqueTournament.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.nationalPlayers[].player.team.userCount` | `integer` |
| `$.data.nationalPlayers[].player.team.nameCode` | `string` |
| `$.data.nationalPlayers[].player.team.disabled` | `boolean` |
| `$.data.nationalPlayers[].player.team.national` | `boolean` |
| `$.data.nationalPlayers[].player.team.type` | `integer` |
| `$.data.nationalPlayers[].player.team.country` | `object` |
| `$.data.nationalPlayers[].player.team.country.alpha2` | `string` |
| `$.data.nationalPlayers[].player.team.country.alpha3` | `string` |
| `$.data.nationalPlayers[].player.team.country.name` | `string` |
| `$.data.nationalPlayers[].player.team.country.slug` | `string` |
| `$.data.nationalPlayers[].player.team.id` | `integer` |
| `$.data.nationalPlayers[].player.team.teamColors` | `object` |
| `$.data.nationalPlayers[].player.team.teamColors.primary` | `string` |
| `$.data.nationalPlayers[].player.team.teamColors.secondary` | `string` |
| `$.data.nationalPlayers[].player.team.teamColors.text` | `string` |
| `$.data.nationalPlayers[].player.team.fieldTranslations` | `object` |
| `$.data.nationalPlayers[].player.team.fieldTranslations.nameTranslation` | `object` |
| `$.data.nationalPlayers[].player.team.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.nationalPlayers[].player.team.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.nationalPlayers[].player.team.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.nationalPlayers[].player.team.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.nationalPlayers[].player.team.fieldTranslations.shortNameTranslation.ar` | `string` |
| `$.data.nationalPlayers[].player.team.fieldTranslations.shortNameTranslation.bn` | `string` |
| `$.data.nationalPlayers[].player.team.fieldTranslations.shortNameTranslation.hi` | `string` |
| `$.data.nationalPlayers[].player.position` | `string` |
| `$.data.nationalPlayers[].player.positionsDetailed` | `array` |
| `$.data.nationalPlayers[].player.positionsDetailed[]` | `string` |
| `$.data.nationalPlayers[].player.jerseyNumber` | `string` |
| `$.data.nationalPlayers[].player.height` | `integer` |
| `$.data.nationalPlayers[].player.dateOfBirth` | `string` |
| `$.data.nationalPlayers[].player.preferredFoot` | `string` |
| `$.data.nationalPlayers[].player.userCount` | `integer` |
| `$.data.nationalPlayers[].player.deceased` | `boolean` |
| `$.data.nationalPlayers[].player.gender` | `string` |
| `$.data.nationalPlayers[].player.country` | `object` |
| `$.data.nationalPlayers[].player.country.alpha2` | `string` |
| `$.data.nationalPlayers[].player.country.alpha3` | `string` |
| `$.data.nationalPlayers[].player.country.name` | `string` |
| `$.data.nationalPlayers[].player.country.slug` | `string` |
| `$.data.nationalPlayers[].player.id` | `integer` |
| `$.data.nationalPlayers[].player.underage` | `boolean` |
| `$.data.nationalPlayers[].player.shirtNumber` | `integer` |
| `$.data.nationalPlayers[].player.dateOfBirthTimestamp` | `integer` |
| `$.data.nationalPlayers[].player.contractUntilTimestamp` | `integer` |
| `$.data.nationalPlayers[].player.proposedMarketValue` | `integer` |
| `$.data.nationalPlayers[].player.proposedMarketValueRaw` | `object` |
| `$.data.nationalPlayers[].player.proposedMarketValueRaw.value` | `integer` |
| `$.data.nationalPlayers[].player.proposedMarketValueRaw.currency` | `string` |
| `$.data.nationalPlayers[].player.fieldTranslations` | `object` |
| `$.data.nationalPlayers[].player.fieldTranslations.nameTranslation` | `object` |
| `$.data.nationalPlayers[].player.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.nationalPlayers[].player.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.nationalPlayers[].player.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.nationalPlayers[].player.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.nationalPlayers[].player.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.nationalPlayers[].player.fieldTranslations.shortNameTranslation.ar` | `string` |
| `$.data.nationalPlayers[].player.fieldTranslations.shortNameTranslation.bn` | `string` |
| `$.data.nationalPlayers[].player.fieldTranslations.shortNameTranslation.hi` | `string` |
| `$.data.nationalPlayers[].player.fieldTranslations.shortNameTranslation.ru` | `string` |
| `$.data.supportStaff` | `array` |
| `$.data.playerPreviousTeam` | `array` |
| `$.data.playerPreviousTeam[]` | `object` |
| `$.data.playerPreviousTeam[].player` | `object` |
| `$.data.playerPreviousTeam[].player.name` | `string` |
| `$.data.playerPreviousTeam[].player.slug` | `string` |
| `$.data.playerPreviousTeam[].player.shortName` | `string` |
| `$.data.playerPreviousTeam[].player.team` | `object` |
| `$.data.playerPreviousTeam[].player.team.name` | `string` |
| `$.data.playerPreviousTeam[].player.team.slug` | `string` |
| `$.data.playerPreviousTeam[].player.team.shortName` | `string` |
| `$.data.playerPreviousTeam[].player.team.gender` | `string` |
| `$.data.playerPreviousTeam[].player.team.sport` | `object` |
| `$.data.playerPreviousTeam[].player.team.sport.name` | `string` |
| `$.data.playerPreviousTeam[].player.team.sport.slug` | `string` |
| `$.data.playerPreviousTeam[].player.team.sport.id` | `integer` |
| `$.data.playerPreviousTeam[].player.team.tournament` | `object` |
| `$.data.playerPreviousTeam[].player.team.tournament.name` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.slug` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.category` | `object` |
| `$.data.playerPreviousTeam[].player.team.tournament.category.name` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.category.slug` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.category.sport` | `object` |
| `$.data.playerPreviousTeam[].player.team.tournament.category.sport.name` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.category.sport.slug` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.category.sport.id` | `integer` |
| `$.data.playerPreviousTeam[].player.team.tournament.category.priority` | `integer` |
| `$.data.playerPreviousTeam[].player.team.tournament.category.country` | `object` |
| `$.data.playerPreviousTeam[].player.team.tournament.category.country.alpha2` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.category.country.alpha3` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.category.country.name` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.category.country.slug` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.category.id` | `integer` |
| `$.data.playerPreviousTeam[].player.team.tournament.category.flag` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.category.alpha2` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.category.fieldTranslations` | `object` |
| `$.data.playerPreviousTeam[].player.team.tournament.category.fieldTranslations.nameTranslation` | `object` |
| `$.data.playerPreviousTeam[].player.team.tournament.category.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.category.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.category.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.category.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.category.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.playerPreviousTeam[].player.team.tournament.uniqueTournament` | `object` |
| `$.data.playerPreviousTeam[].player.team.tournament.uniqueTournament.name` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.uniqueTournament.slug` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.uniqueTournament.primaryColorHex` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.uniqueTournament.secondaryColorHex` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.uniqueTournament.category` | `object` |
| `$.data.playerPreviousTeam[].player.team.tournament.uniqueTournament.category.name` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.uniqueTournament.category.slug` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.uniqueTournament.category.sport` | `object` |
| `$.data.playerPreviousTeam[].player.team.tournament.uniqueTournament.category.sport.name` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.uniqueTournament.category.sport.slug` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.uniqueTournament.category.sport.id` | `integer` |
| `$.data.playerPreviousTeam[].player.team.tournament.uniqueTournament.category.priority` | `integer` |
| `$.data.playerPreviousTeam[].player.team.tournament.uniqueTournament.category.country` | `object` |
| `$.data.playerPreviousTeam[].player.team.tournament.uniqueTournament.category.country.alpha2` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.uniqueTournament.category.country.alpha3` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.uniqueTournament.category.country.name` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.uniqueTournament.category.country.slug` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.uniqueTournament.category.id` | `integer` |
| `$.data.playerPreviousTeam[].player.team.tournament.uniqueTournament.category.flag` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.uniqueTournament.category.alpha2` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.uniqueTournament.category.fieldTranslations` | `object` |
| `$.data.playerPreviousTeam[].player.team.tournament.uniqueTournament.category.fieldTranslations.nameTranslation` | `object` |
| `$.data.playerPreviousTeam[].player.team.tournament.uniqueTournament.category.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.uniqueTournament.category.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.uniqueTournament.category.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.uniqueTournament.category.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.uniqueTournament.category.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.playerPreviousTeam[].player.team.tournament.uniqueTournament.userCount` | `integer` |
| `$.data.playerPreviousTeam[].player.team.tournament.uniqueTournament.country` | `object` |
| `$.data.playerPreviousTeam[].player.team.tournament.uniqueTournament.id` | `integer` |
| `$.data.playerPreviousTeam[].player.team.tournament.uniqueTournament.displayInverseHomeAwayTeams` | `boolean` |
| `$.data.playerPreviousTeam[].player.team.tournament.uniqueTournament.fieldTranslations` | `object` |
| `$.data.playerPreviousTeam[].player.team.tournament.uniqueTournament.fieldTranslations.nameTranslation` | `object` |
| `$.data.playerPreviousTeam[].player.team.tournament.uniqueTournament.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.uniqueTournament.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.uniqueTournament.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.uniqueTournament.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.uniqueTournament.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.playerPreviousTeam[].player.team.tournament.priority` | `integer` |
| `$.data.playerPreviousTeam[].player.team.tournament.isLive` | `boolean` |
| `$.data.playerPreviousTeam[].player.team.tournament.id` | `integer` |
| `$.data.playerPreviousTeam[].player.team.tournament.fieldTranslations` | `object` |
| `$.data.playerPreviousTeam[].player.team.tournament.fieldTranslations.nameTranslation` | `object` |
| `$.data.playerPreviousTeam[].player.team.tournament.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.playerPreviousTeam[].player.team.tournament.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.playerPreviousTeam[].player.team.primaryUniqueTournament` | `object` |
| `$.data.playerPreviousTeam[].player.team.primaryUniqueTournament.name` | `string` |
| `$.data.playerPreviousTeam[].player.team.primaryUniqueTournament.slug` | `string` |
| `$.data.playerPreviousTeam[].player.team.primaryUniqueTournament.primaryColorHex` | `string` |
| `$.data.playerPreviousTeam[].player.team.primaryUniqueTournament.secondaryColorHex` | `string` |
| `$.data.playerPreviousTeam[].player.team.primaryUniqueTournament.category` | `object` |
| `$.data.playerPreviousTeam[].player.team.primaryUniqueTournament.category.name` | `string` |
| `$.data.playerPreviousTeam[].player.team.primaryUniqueTournament.category.slug` | `string` |
| `$.data.playerPreviousTeam[].player.team.primaryUniqueTournament.category.sport` | `object` |
| `$.data.playerPreviousTeam[].player.team.primaryUniqueTournament.category.sport.name` | `string` |
| `$.data.playerPreviousTeam[].player.team.primaryUniqueTournament.category.sport.slug` | `string` |
| `$.data.playerPreviousTeam[].player.team.primaryUniqueTournament.category.sport.id` | `integer` |
| `$.data.playerPreviousTeam[].player.team.primaryUniqueTournament.category.priority` | `integer` |
| `$.data.playerPreviousTeam[].player.team.primaryUniqueTournament.category.country` | `object` |
| `$.data.playerPreviousTeam[].player.team.primaryUniqueTournament.category.country.alpha2` | `string` |
| `$.data.playerPreviousTeam[].player.team.primaryUniqueTournament.category.country.alpha3` | `string` |
| `$.data.playerPreviousTeam[].player.team.primaryUniqueTournament.category.country.name` | `string` |
| `$.data.playerPreviousTeam[].player.team.primaryUniqueTournament.category.country.slug` | `string` |
| `$.data.playerPreviousTeam[].player.team.primaryUniqueTournament.category.id` | `integer` |
| `$.data.playerPreviousTeam[].player.team.primaryUniqueTournament.category.flag` | `string` |
| `$.data.playerPreviousTeam[].player.team.primaryUniqueTournament.category.alpha2` | `string` |
| `$.data.playerPreviousTeam[].player.team.primaryUniqueTournament.category.fieldTranslations` | `object` |
| `$.data.playerPreviousTeam[].player.team.primaryUniqueTournament.category.fieldTranslations.nameTranslation` | `object` |
| `$.data.playerPreviousTeam[].player.team.primaryUniqueTournament.category.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.playerPreviousTeam[].player.team.primaryUniqueTournament.category.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.playerPreviousTeam[].player.team.primaryUniqueTournament.category.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.playerPreviousTeam[].player.team.primaryUniqueTournament.category.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.playerPreviousTeam[].player.team.primaryUniqueTournament.category.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.playerPreviousTeam[].player.team.primaryUniqueTournament.userCount` | `integer` |
| `$.data.playerPreviousTeam[].player.team.primaryUniqueTournament.country` | `object` |
| `$.data.playerPreviousTeam[].player.team.primaryUniqueTournament.id` | `integer` |
| `$.data.playerPreviousTeam[].player.team.primaryUniqueTournament.displayInverseHomeAwayTeams` | `boolean` |
| `$.data.playerPreviousTeam[].player.team.primaryUniqueTournament.fieldTranslations` | `object` |
| `$.data.playerPreviousTeam[].player.team.primaryUniqueTournament.fieldTranslations.nameTranslation` | `object` |
| `$.data.playerPreviousTeam[].player.team.primaryUniqueTournament.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.playerPreviousTeam[].player.team.primaryUniqueTournament.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.playerPreviousTeam[].player.team.primaryUniqueTournament.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.playerPreviousTeam[].player.team.primaryUniqueTournament.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.playerPreviousTeam[].player.team.primaryUniqueTournament.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.playerPreviousTeam[].player.team.userCount` | `integer` |
| `$.data.playerPreviousTeam[].player.team.nameCode` | `string` |
| `$.data.playerPreviousTeam[].player.team.disabled` | `boolean` |
| `$.data.playerPreviousTeam[].player.team.national` | `boolean` |
| `$.data.playerPreviousTeam[].player.team.type` | `integer` |
| `$.data.playerPreviousTeam[].player.team.country` | `object` |
| `$.data.playerPreviousTeam[].player.team.country.alpha2` | `string` |
| `$.data.playerPreviousTeam[].player.team.country.alpha3` | `string` |
| `$.data.playerPreviousTeam[].player.team.country.name` | `string` |
| `$.data.playerPreviousTeam[].player.team.country.slug` | `string` |
| `$.data.playerPreviousTeam[].player.team.id` | `integer` |
| `$.data.playerPreviousTeam[].player.team.teamColors` | `object` |
| `$.data.playerPreviousTeam[].player.team.teamColors.primary` | `string` |
| `$.data.playerPreviousTeam[].player.team.teamColors.secondary` | `string` |
| `$.data.playerPreviousTeam[].player.team.teamColors.text` | `string` |
| `$.data.playerPreviousTeam[].player.team.fieldTranslations` | `object` |
| `$.data.playerPreviousTeam[].player.team.fieldTranslations.nameTranslation` | `object` |
| `$.data.playerPreviousTeam[].player.team.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.playerPreviousTeam[].player.team.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.playerPreviousTeam[].player.team.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.playerPreviousTeam[].player.team.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.playerPreviousTeam[].player.team.fieldTranslations.shortNameTranslation.ar` | `string` |
| `$.data.playerPreviousTeam[].player.team.fieldTranslations.shortNameTranslation.bn` | `string` |
| `$.data.playerPreviousTeam[].player.team.fieldTranslations.shortNameTranslation.hi` | `string` |
| `$.data.playerPreviousTeam[].player.position` | `string` |
| `$.data.playerPreviousTeam[].player.positionsDetailed` | `array` |
| `$.data.playerPreviousTeam[].player.positionsDetailed[]` | `string` |
| `$.data.playerPreviousTeam[].player.jerseyNumber` | `string` |
| `$.data.playerPreviousTeam[].player.height` | `integer` |
| `$.data.playerPreviousTeam[].player.dateOfBirth` | `string` |
| `$.data.playerPreviousTeam[].player.preferredFoot` | `string` |
| `$.data.playerPreviousTeam[].player.userCount` | `integer` |
| `$.data.playerPreviousTeam[].player.deceased` | `boolean` |
| `$.data.playerPreviousTeam[].player.gender` | `string` |
| `$.data.playerPreviousTeam[].player.country` | `object` |
| `$.data.playerPreviousTeam[].player.country.alpha2` | `string` |
| `$.data.playerPreviousTeam[].player.country.alpha3` | `string` |
| `$.data.playerPreviousTeam[].player.country.name` | `string` |
| `$.data.playerPreviousTeam[].player.country.slug` | `string` |
| `$.data.playerPreviousTeam[].player.id` | `integer` |
| `$.data.playerPreviousTeam[].player.underage` | `boolean` |
| `$.data.playerPreviousTeam[].player.shirtNumber` | `integer` |
| `$.data.playerPreviousTeam[].player.dateOfBirthTimestamp` | `integer` |
| `$.data.playerPreviousTeam[].player.contractUntilTimestamp` | `integer` |
| `$.data.playerPreviousTeam[].player.proposedMarketValue` | `integer` |
| `$.data.playerPreviousTeam[].player.proposedMarketValueRaw` | `object` |
| `$.data.playerPreviousTeam[].player.proposedMarketValueRaw.value` | `integer` |
| `$.data.playerPreviousTeam[].player.proposedMarketValueRaw.currency` | `string` |
| `$.data.playerPreviousTeam[].player.fieldTranslations` | `object` |
| `$.data.playerPreviousTeam[].player.fieldTranslations.nameTranslation` | `object` |
| `$.data.playerPreviousTeam[].player.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.playerPreviousTeam[].player.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.playerPreviousTeam[].player.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.playerPreviousTeam[].player.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.playerPreviousTeam[].player.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.playerPreviousTeam[].player.fieldTranslations.shortNameTranslation.ar` | `string` |
| `$.data.playerPreviousTeam[].player.fieldTranslations.shortNameTranslation.bn` | `string` |
| `$.data.playerPreviousTeam[].player.fieldTranslations.shortNameTranslation.hi` | `string` |
| `$.data.playerPreviousTeam[].player.fieldTranslations.shortNameTranslation.ru` | `string` |
| `$.data.playerPreviousTeam[].previousTeam` | `object` |
| `$.data.playerPreviousTeam[].previousTeam.name` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.slug` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.shortName` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.gender` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.sport` | `object` |
| `$.data.playerPreviousTeam[].previousTeam.sport.name` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.sport.slug` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.sport.id` | `integer` |
| `$.data.playerPreviousTeam[].previousTeam.tournament` | `object` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.name` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.slug` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.category` | `object` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.category.name` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.category.slug` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.category.sport` | `object` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.category.sport.name` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.category.sport.slug` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.category.sport.id` | `integer` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.category.priority` | `integer` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.category.country` | `object` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.category.country.alpha2` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.category.country.alpha3` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.category.country.name` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.category.country.slug` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.category.id` | `integer` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.category.flag` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.category.alpha2` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.category.fieldTranslations` | `object` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.category.fieldTranslations.nameTranslation` | `object` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.category.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.category.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.category.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.category.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.category.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.uniqueTournament` | `object` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.uniqueTournament.name` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.uniqueTournament.slug` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.uniqueTournament.primaryColorHex` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.uniqueTournament.secondaryColorHex` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.uniqueTournament.category` | `object` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.uniqueTournament.category.name` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.uniqueTournament.category.slug` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.uniqueTournament.category.sport` | `object` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.uniqueTournament.category.sport.name` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.uniqueTournament.category.sport.slug` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.uniqueTournament.category.sport.id` | `integer` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.uniqueTournament.category.priority` | `integer` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.uniqueTournament.category.country` | `object` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.uniqueTournament.category.country.alpha2` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.uniqueTournament.category.country.alpha3` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.uniqueTournament.category.country.name` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.uniqueTournament.category.country.slug` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.uniqueTournament.category.id` | `integer` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.uniqueTournament.category.flag` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.uniqueTournament.category.alpha2` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.uniqueTournament.category.fieldTranslations` | `object` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.uniqueTournament.category.fieldTranslations.nameTranslation` | `object` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.uniqueTournament.category.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.uniqueTournament.category.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.uniqueTournament.category.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.uniqueTournament.category.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.uniqueTournament.category.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.uniqueTournament.userCount` | `integer` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.uniqueTournament.country` | `object` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.uniqueTournament.id` | `integer` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.uniqueTournament.displayInverseHomeAwayTeams` | `boolean` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.uniqueTournament.fieldTranslations` | `object` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.uniqueTournament.fieldTranslations.nameTranslation` | `object` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.uniqueTournament.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.uniqueTournament.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.uniqueTournament.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.uniqueTournament.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.uniqueTournament.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.priority` | `integer` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.isLive` | `boolean` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.id` | `integer` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.fieldTranslations` | `object` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.fieldTranslations.nameTranslation` | `object` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.tournament.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.playerPreviousTeam[].previousTeam.primaryUniqueTournament` | `object` |
| `$.data.playerPreviousTeam[].previousTeam.primaryUniqueTournament.name` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.primaryUniqueTournament.slug` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.primaryUniqueTournament.primaryColorHex` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.primaryUniqueTournament.secondaryColorHex` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.primaryUniqueTournament.category` | `object` |
| `$.data.playerPreviousTeam[].previousTeam.primaryUniqueTournament.category.name` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.primaryUniqueTournament.category.slug` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.primaryUniqueTournament.category.sport` | `object` |
| `$.data.playerPreviousTeam[].previousTeam.primaryUniqueTournament.category.sport.name` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.primaryUniqueTournament.category.sport.slug` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.primaryUniqueTournament.category.sport.id` | `integer` |
| `$.data.playerPreviousTeam[].previousTeam.primaryUniqueTournament.category.priority` | `integer` |
| `$.data.playerPreviousTeam[].previousTeam.primaryUniqueTournament.category.country` | `object` |
| `$.data.playerPreviousTeam[].previousTeam.primaryUniqueTournament.category.country.alpha2` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.primaryUniqueTournament.category.country.alpha3` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.primaryUniqueTournament.category.country.name` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.primaryUniqueTournament.category.country.slug` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.primaryUniqueTournament.category.id` | `integer` |
| `$.data.playerPreviousTeam[].previousTeam.primaryUniqueTournament.category.flag` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.primaryUniqueTournament.category.alpha2` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.primaryUniqueTournament.category.fieldTranslations` | `object` |
| `$.data.playerPreviousTeam[].previousTeam.primaryUniqueTournament.category.fieldTranslations.nameTranslation` | `object` |
| `$.data.playerPreviousTeam[].previousTeam.primaryUniqueTournament.category.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.primaryUniqueTournament.category.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.primaryUniqueTournament.category.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.primaryUniqueTournament.category.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.primaryUniqueTournament.category.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.playerPreviousTeam[].previousTeam.primaryUniqueTournament.userCount` | `integer` |
| `$.data.playerPreviousTeam[].previousTeam.primaryUniqueTournament.country` | `object` |
| `$.data.playerPreviousTeam[].previousTeam.primaryUniqueTournament.id` | `integer` |
| `$.data.playerPreviousTeam[].previousTeam.primaryUniqueTournament.displayInverseHomeAwayTeams` | `boolean` |
| `$.data.playerPreviousTeam[].previousTeam.primaryUniqueTournament.fieldTranslations` | `object` |
| `$.data.playerPreviousTeam[].previousTeam.primaryUniqueTournament.fieldTranslations.nameTranslation` | `object` |
| `$.data.playerPreviousTeam[].previousTeam.primaryUniqueTournament.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.primaryUniqueTournament.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.primaryUniqueTournament.fieldTranslations.nameTranslation.bn` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.primaryUniqueTournament.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.primaryUniqueTournament.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.playerPreviousTeam[].previousTeam.userCount` | `integer` |
| `$.data.playerPreviousTeam[].previousTeam.nameCode` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.disabled` | `boolean` |
| `$.data.playerPreviousTeam[].previousTeam.national` | `boolean` |
| `$.data.playerPreviousTeam[].previousTeam.type` | `integer` |
| `$.data.playerPreviousTeam[].previousTeam.country` | `object` |
| `$.data.playerPreviousTeam[].previousTeam.country.alpha2` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.country.alpha3` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.country.name` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.country.slug` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.id` | `integer` |
| `$.data.playerPreviousTeam[].previousTeam.teamColors` | `object` |
| `$.data.playerPreviousTeam[].previousTeam.teamColors.primary` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.teamColors.secondary` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.teamColors.text` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.fieldTranslations` | `object` |
| `$.data.playerPreviousTeam[].previousTeam.fieldTranslations.nameTranslation` | `object` |
| `$.data.playerPreviousTeam[].previousTeam.fieldTranslations.nameTranslation.ar` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.fieldTranslations.nameTranslation.hi` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.fieldTranslations.nameTranslation.ru` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.fieldTranslations.shortNameTranslation` | `object` |
| `$.data.playerPreviousTeam[].previousTeam.fieldTranslations.shortNameTranslation.ar` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.fieldTranslations.shortNameTranslation.bn` | `string` |
| `$.data.playerPreviousTeam[].previousTeam.fieldTranslations.shortNameTranslation.hi` | `string` |
| `$.data.playerPreviousTeam[].transferDate` | `string` |
| `$.data.nationalTeamPlayerStatistics` | `array` |
| `$.data.teamDepthAssignments` | `null` |
| `$.source` | `string` |
| `$.cacheHit` | `boolean` |
| `$.timezone` | `object` |
| `$.timezone.name` | `string` |
| `$.timezone.utcOffset` | `string` |
| `$.timezone.source` | `string` |
| `$.timezone.country` | `string` |

---
