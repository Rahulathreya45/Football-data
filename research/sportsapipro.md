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

### Notes

Premier League 2025/26 season.
Initial investigation of the fixtures endpoint.

---

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

## 5. Representative Response Examples

### `seasons`

Showing 2 representative record(s).

```json
[
  {
    "id": 96668,
    "name": "Premier League 26/27",
    "year": "26/27",
    "tournamentId": 17
  },
  {
    "id": 76986,
    "name": "Premier League 25/26",
    "year": "25/26",
    "tournamentId": 17
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

