# Stability Ingestion Service Specification

## Purpose
Automate ingestion of `data/stability/*.json` into structured tables (`stability_sessions`, `stability_turns`) after validating against `schemas/interpretive_stability.schema.json`.

## Responsibilities
- Watch `data/stability/` for new or updated JSON files.
- Validate each file against the schema.
- Transform JSON into relational rows.
- Upsert into database tables.
- Track ingestion state and errors.

## Pipeline
1. File watcher detects new/changed file.
2. JSON loaded and validated.
3. Transform:
   - stability_sessions: session-level metadata + D/C/A/S
   - stability_turns: turn-level D/C/A/S + failure modes
4. Upsert logic:
   - Replace existing session if session_id matches.
5. Log ingestion events and errors.

## Tables
### stability_sessions
- session_id
- timestamp
- model
- prompt_suite?
- scenario?
- D_session, C_session, A_session, S_session
- max_severity

### stability_turns
- session_id
- turn_index
- speaker
- D, C, A, S
- failure_modes (JSON array)

## Configuration
- INGEST_ROOT = data/stability/
- DB_URL
- POLL_INTERVAL_MS
