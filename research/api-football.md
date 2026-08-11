# api-football.com — API Investigation

## Project Context

- **Focus:** Premier League
- **Season:** 2025/26
- **Purpose:** Investigate API response structures and determine
  which data is useful for the football data pipeline.
- **Raw responses:** Stored separately as JSON files.

This document contains the investigation of multiple endpoints
from `api-football.com`.


---

# Endpoint: `teams`

## 1. Request

| Property | Value |
|---|---|
| Source | `api-football.com` |
| Endpoint | `teams` |
| Method | `GET` |
| URL | `https://v3.football.api-sports.io/teams` |
| HTTP Status | `200` |
| Captured At | `2026-08-11T10:42:07.019701+00:00` |
| Raw Response | `raw/api-football/teams/teams.json` |

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

- **API endpoint reported:** `teams`
- **Results:** `0`
- **Paging:**
```json
{
  "current": 1,
  "total": 1
}
```
- **Errors:**
```json
{
  "plan": "Free plans do not have access to this season, try from 2022 to 2024."
}
```

---

## 3. Record Counts

- `response`: **0 records**

---

## 4. Response Structure

The following structure is automatically derived from the
complete JSON response.

| JSON Path | Type |
|---|---|
| `$.get` | `string` |
| `$.parameters` | `object` |
| `$.parameters.league` | `string` |
| `$.parameters.season` | `string` |
| `$.errors` | `object` |
| `$.errors.plan` | `string` |
| `$.results` | `integer` |
| `$.paging` | `object` |
| `$.paging.current` | `integer` |
| `$.paging.total` | `integer` |
| `$.response` | `array` |

---

## 5. Representative Response Examples

_No top-level record array detected._

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

