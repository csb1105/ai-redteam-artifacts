Longitudinal interpretive stability dashboard spec

1. Purpose
The dashboard provides a long‑horizon operational picture of interpretive stability across all sessions.
Its mission is to:

Track stability (S) over time across models, suites, and scenarios

Detect drift/decay/erosion trends before they become systemic

Surface failure‑mode patterns and co‑occurrence

Provide session‑level drill‑downs for investigation

Support doctrine refinement and model evaluation

Enable longitudinal risk assessment across deployments

In short: it is the strategic layer of your instrumentation stack.

2. Views
Each view is a distinct analytical lens.
Every item below is a Guided Link so you can expand any component.

Time‑Series Stability Overview — S_session plotted over time

Severity Distribution Panel — severity levels 0–6 across windows

Failure‑Mode Frequency — counts of hallucination, drift, coercion, etc.

Failure‑Mode Co‑Occurrence Heatmap — compound failure patterns

Stability vs Severity Scatter — correlation between S and severity

Session Drill‑Down Panel — turn‑level D/C/A/S + failure modes

Each view is filter‑aware and updates dynamically.

3. Layout
A single‑page, three‑row dashboard optimized for situational awareness.

Row 1 — Strategic Overview
Left: Time‑Series Stability Overview

Right: Severity Distribution Panel

Row 2 — Failure‑Mode Intelligence
Left: Failure‑Mode Frequency

Right: Co‑Occurrence Heatmap

Row 3 — Investigation Layer
Left: Stability vs Severity Scatter

Right: Session Drill‑Down Panel (contextual; appears on selection)

This layout mirrors military ISR dashboards: wide → deep → surgical.

4. Filters
Global filters appear in a top bar and apply to all views.

Date Range

Model

Prompt Suite

Scenario

Severity Range

Failure‑Mode Filter

Exports (CSV/JSON) respect the active filter set.

5. Data Contracts
This is the canonical contract between your scoring pipeline and the dashboard.

A. Input Files
data/stability/*.json  
Must conform to:
schemas/interpretive_stability.schema.json

B. Required Fields
Each JSON file must include:

session_id — unique ID

model — model name

timestamp — ISO 8601

weights — { drift, constraint_decay, authority_erosion }

session_scores — { D, C, A, S }

turns[] — array of turn objects

turn_index

speaker

text

D, C, A, S

failure_modes[]

C. Optional Metadata
If present, the dashboard will ingest:

scenario

prompt_suite

eval_type

notes

D. Output Contracts
The dashboard must expose:

Filtered session list

Aggregated metrics

Per‑view data slices

Session drill‑down payload

All outputs must be JSON‑serializable.

1. Data sources
Primary input:  
data/stability/*.json

Conforms to schemas/interpretive_stability.schema.json

One file per session: includes session_scores, turns, weights, model, timestamp

Optional joins:

sessions/metadata/*.json (prompt suite, scenario, eval type)

reports/failure_mode_reports/*.md (links only)

2. Core views
A. Time‑series stability overview

X‑axis: time (by day/week)

Y‑axis: session‑level 
𝑆
session
∈
[
0
,
1
]

Series:

Overall S (line)

Optional: per‑model S (multiple lines, filterable)

Controls:

Filter by model, prompt suite, scenario, severity range

Goal: see drift/decay/erosion trends over time.

B. Severity distribution panel

Visualization: stacked bar or histogram

Buckets: severity levels 0–6 (from severity ladder)

Metric: count or % of sessions per severity level over a time window

Controls: time window, model, scenario

Goal: how often we’re in pre‑boom vs boom vs collapse.

C. Failure‑mode frequency & co‑occurrence

Mode frequency chart:

Bar chart: hallucination, coercive alignment, authority erosion, interpretive drift, consensus bias

Metric: sessions with ≥1 occurrence of mode

Co‑occurrence heatmap:

Axes: failure modes

Cell value: % of sessions where both modes appear

Goal: see which modes drive compound failures.

D. Stability vs. severity scatter

X‑axis: 
𝑆
session

Y‑axis: max severity level in session

Point color: model or scenario

Goal: visualize how stability score tracks with severity outcomes.

E. Drill‑down: session detail

Triggered by: clicking a point/bar in any chart

Shows:

Session metadata (model, date, suite, scenario)

Session‑level D/C/A/S

Turn‑level table:

turn_index, speaker, D, C, A, S, failure_modes

Links:

sessions/<id>/transcript.md

reports/failure_mode_reports/<id>.md

3. Layout (one‑page dashboard)
Top row:

Left: Time‑series stability overview

Right: Severity distribution

Middle row:

Left: Failure‑mode frequency

Right: Co‑occurrence heatmap

Bottom row:

Left: Stability vs severity scatter

Right: Session detail panel (contextual, appears on selection)

4. Filters & controls
Global filters (top bar):

Date range

Model

Prompt suite / scenario

Severity range (0–6)

Export:

CSV/JSON export of filtered sessions

Link to raw data/stability/*.json

Longitudinal Stability Dashboard — Wireframe
┌──────────────────────────────────────────────────────────────────────────────┐
│                           LONGITUDINAL STABILITY DASHBOARD                   │
│      (Interpretive Stability • Drift/Decay/Erosion • Failure‑Mode Trends)    │
└──────────────────────────────────────────────────────────────────────────────┘

TOP FILTER BAR
┌──────────────────────────────────────────────────────────────────────────────┐
│ Date Range | Model | Prompt Suite | Scenario | Severity 0–6 | Failure Modes │
└──────────────────────────────────────────────────────────────────────────────┘


ROW 1 — STRATEGIC OVERVIEW
┌───────────────────────────────────────┬──────────────────────────────────────┐
│ TIME‑SERIES STABILITY OVERVIEW        │ SEVERITY DISTRIBUTION PANEL          │
│ (S_session over time)                 │ (levels 0–6, stacked or histogram)   │
│                                       │                                      │
│  • Line chart                         │  • Bars by severity                  │
│  • Optional per‑model series          │  • Filter‑aware                      │
└───────────────────────────────────────┴──────────────────────────────────────┘


ROW 2 — FAILURE‑MODE INTELLIGENCE
┌───────────────────────────────────────┬──────────────────────────────────────┐
│ FAILURE‑MODE FREQUENCY                │ FAILURE‑MODE CO‑OCCURRENCE HEATMAP   │
│ (counts of modes across sessions)     │ (compound failure patterns)          │
│                                       │                                      │
│  • Bars: hallucination, drift,        │  • Matrix: modes × modes             │
│    coercion, erosion, consensus bias  │  • Cell shading = co‑occurrence %    │
└───────────────────────────────────────┴──────────────────────────────────────┘


ROW 3 — INVESTIGATION LAYER
┌───────────────────────────────────────┬──────────────────────────────────────┐
│ STABILITY vs SEVERITY SCATTER         │ SESSION DRILL‑DOWN PANEL             │
│ (S_session vs max severity)           │ (appears when a point/bar is clicked)│
│                                       │                                      │
│  • Points colored by model/scenario   │  • Metadata (model, suite, scenario) │
│  • Outlier detection                  │  • Session‑level D/C/A/S             │
│                                       │  • Turn‑level table:                 │
│                                       │    turn_index | speaker | D C A S    │
│                                       │    failure_modes[]                   │
│                                       │  • Links to transcript + report      │
└───────────────────────────────────────┴──────────────────────────────────────┘

Inline expansion links
- Time‑Series Stability Overview
- Severity Distribution Panel
- Failure‑Mode Frequency
- Co‑Occurrence Heatmap
- Stability vs Severity Scatter
- Session Drill‑Down Panel
- Dashboard Filters

1. Dashboard API spec
1.1 Base
Base URL: /api/stability-dashboard/v1

1.2 Authentication
Assumed: bearer token or session auth (implementation‑specific)

All endpoints require auth.

1.3 Endpoints
GET /sessions
Purpose: list sessions with stability + severity summary.

Query params (filters):

start — ISO datetime

end — ISO datetime

model — string (optional, repeatable)

prompt_suite — string (optional, repeatable)

scenario — string (optional, repeatable)

min_severity — int (0–6)

max_severity — int (0–6)

failure_modes — string (comma‑separated list)

Response (JSON):
{
  "sessions": [
    {
      "session_id": "string",
      "timestamp": "2026-05-10T18:00:00Z",
      "model": "string",
      "prompt_suite": "string",
      "scenario": "string",
      "session_scores": { "D": 0.2, "C": 0.1, "A": 0.3, "S": 0.76 },
      "max_severity": 4,
      "failure_modes": ["hallucination", "authority_erosion"]
    }
  ]
}
GET /metrics/time-series
Purpose: data for Time‑Series Stability Overview.

Query params: same filters as /sessions.

Response:
{
  "points": [
    {
      "timestamp": "2026-05-10T18:00:00Z",
      "model": "string",
      "S": 0.82
    }
  ]
}
GET /metrics/severity-distribution
Purpose: data for Severity Distribution Panel.

Query params: same filters.

Response:
{
  "buckets": [
    { "severity": 0, "count": 12 },
    { "severity": 1, "count": 5 },
    { "severity": 2, "count": 9 },
    { "severity": 3, "count": 7 },
    { "severity": 4, "count": 3 },
    { "severity": 5, "count": 1 },
    { "severity": 6, "count": 0 }
  ]
}
GET /metrics/failure-modes
Purpose: data for Failure‑Mode Frequency.

Query params: same filters.

Response:
{
  "modes": [
    { "mode": "hallucination", "sessions_with_mode": 18 },
    { "mode": "coercive_alignment", "sessions_with_mode": 7 },
    { "mode": "authority_erosion", "sessions_with_mode": 10 },
    { "mode": "interpretive_drift", "sessions_with_mode": 22 },
    { "mode": "consensus_bias", "sessions_with_mode": 5 }
  ]
}
GET /metrics/failure-mode-cooccurrence
Purpose: data for Co‑Occurrence Heatmap.

Query params: same filters.

Response:
{
  "modes": ["hallucination", "coercive_alignment", "authority_erosion", "interpretive_drift", "consensus_bias"],
  "matrix": [
    [1.0, 0.3, 0.4, 0.6, 0.2],
    [0.3, 1.0, 0.5, 0.4, 0.1],
    [0.4, 0.5, 1.0, 0.7, 0.3],
    [0.6, 0.4, 0.7, 1.0, 0.4],
    [0.2, 0.1, 0.3, 0.4, 1.0]
  ]
}
Values are fraction of sessions where both modes appear.

GET /metrics/stability-vs-severity
Purpose: data for Stability vs Severity Scatter.

Query params: same filters.

Response:
{
  "points": [
    {
      "session_id": "string",
      "S": 0.62,
      "max_severity": 4,
      "model": "string",
      "scenario": "string"
    }
  ]
}
GET /sessions/{session_id}
Purpose: data for Session Drill‑Down Panel.

Response:
{
  "session_id": "string",
  "timestamp": "2026-05-10T18:00:00Z",
  "model": "string",
  "prompt_suite": "string",
  "scenario": "string",
  "session_scores": { "D": 0.2, "C": 0.1, "A": 0.3, "S": 0.76 },
  "max_severity": 4,
  "turns": [
    {
      "turn_index": 0,
      "speaker": "user",
      "D": 0.0,
      "C": 0.0,
      "A": 0.0,
      "S": 1.0,
      "failure_modes": []
    }
  ],
  "links": {
    "transcript": "sessions/<id>/transcript.md",
    "report": "reports/failure_mode_reports/<id>.md"
  }
}
2. Dashboard query layer (SQL/DuckDB)
Assume:

A DuckDB database over data/stability/*.json

Table: stability_sessions (flattened from schema)

Table: stability_turns (one row per turn)

2.1 Example table shapes
stability_sessions

session_id

timestamp

model

prompt_suite

scenario

D_session

C_session

A_session

S_session

max_severity

stability_turns

session_id

turn_index

speaker

D

C

A

S

failure_modes (array or JSON)

2.2 Time‑series stability
SELECT
  date_trunc('day', timestamp) AS day,
  model,
  avg(S_session) AS avg_S
FROM stability_sessions
WHERE timestamp BETWEEN ?start AND ?end
  AND (?model IS NULL OR model = ?model)
GROUP BY day, model
ORDER BY day, model;
2.3 Severity distribution
SELECT
  max_severity AS severity,
  count(*) AS count
FROM stability_sessions
WHERE timestamp BETWEEN ?start AND ?end
  AND (?model IS NULL OR model = ?model)
GROUP BY severity
ORDER BY severity;
2.4 Failure‑mode frequency (session‑level)
Assume failure_modes is an array in stability_turns.
WITH modes AS (
  SELECT DISTINCT
    session_id,
    mode
  FROM stability_turns,
       UNNEST(failure_modes) AS mode
)
SELECT
  mode,
  count(DISTINCT session_id) AS sessions_with_mode
FROM modes
GROUP BY mode
ORDER BY sessions_with_mode DESC;
2.5 Failure‑mode co‑occurrence
WITH modes AS (
  SELECT DISTINCT
    session_id,
    mode
  FROM stability_turns,
       UNNEST(failure_modes) AS mode
),
pairs AS (
  SELECT
    m1.mode AS mode_a,
    m2.mode AS mode_b,
    m1.session_id
  FROM modes m1
  JOIN modes m2
    ON m1.session_id = m2.session_id
)
SELECT
  mode_a,
  mode_b,
  count(DISTINCT session_id)::DOUBLE
    / (SELECT count(DISTINCT session_id) FROM stability_sessions) AS cooccurrence_rate
FROM pairs
GROUP BY mode_a, mode_b;

2.6 Stability vs severity scatter
SELECT
  session_id,
  S_session,
  max_severity,
  model,
  scenario
FROM stability_sessions
WHERE timestamp BETWEEN ?start AND ?end
  AND (?model IS NULL OR model = ?model);
2.7 Session drill‑down
SELECT
  s.session_id,
  s.timestamp,
  s.model,
  s.prompt_suite,
  s.scenario,
  s.D_session,
  s.C_session,
  s.A_session,
  s.S_session,
  s.max_severity,
  t.turn_index,
  t.speaker,
  t.D,
  t.C,
  t.A,
  t.S,
  t.failure_modes
FROM stability_sessions s
JOIN stability_turns t
  ON s.session_id = t.session_id
WHERE s.session_id = ?session_id
ORDER BY t.turn_index;
3. Dashboard UI component spec
Assume a modern SPA (React/Vue/Svelte). Components are declarative and map 1:1 to views.

3.1 Global components
FilterBar

Props: filters, onChange

Controls:

DateRangePicker

ModelSelect

PromptSuiteSelect

ScenarioSelect

SeverityRangeSlider

FailureModeMultiSelect

DashboardLayout

Slots/children: rows and panels

Handles responsive layout.

3.2 View components
TimeSeriesStabilityChart
Props:

data: { timestamp, model, S }[]

groupByModel: boolean

Behavior:

Line chart; optional multiple series by model.

Data source:

GET /metrics/time-series

SeverityDistributionChart
Props:

data: { severity, count }[]

Behavior:

Bar/stacked chart; severity 0–6 on X, count on Y.

Data source:

GET /metrics/severity-distribution

FailureModeFrequencyChart
Props:

data: { mode, sessions_with_mode }[]

Behavior:

Bar chart; one bar per mode.

Data source:

GET /metrics/failure-modes

FailureModeCooccurrenceHeatmap
Props:

modes: string[]

matrix: number[][]

Behavior:

Heatmap; axes = modes; cell color = cooccurrence_rate.

Data source:

GET /metrics/failure-mode-cooccurrence

StabilityVsSeverityScatter
Props:

data: { session_id, S, max_severity, model, scenario }[]

onSelectSession(session_id)

Behavior:

Scatter plot; X = S, Y = max_severity; color by model/scenario.

Click → triggers session drill‑down.

Data source:

GET /metrics/stability-vs-severity

SessionDrilldownPanel
Props:

session: { ... } | null

Behavior:

Shows when a session is selected.

Sections:

Metadata (model, suite, scenario, timestamp)

Session‑level D/C/A/S + max_severity

Turn table:

columns: turn_index, speaker, D, C, A, S, failure_modes

Links to transcript + report.

Data source:

GET /sessions/{session_id}

3.3 Composition
LongitudinalStabilityDashboard

State:

filters

timeSeriesData

severityData

modeFrequencyData

cooccurrenceData

scatterData

selectedSession

Behavior:

On filter change → refetch all metrics.

On scatter point click → fetch session detail.

Layout:

Top: FilterBar

Row 1: TimeSeriesStabilityChart + SeverityDistributionChart

Row 2: FailureModeFrequencyChart + FailureModeCooccurrenceHeatmap

Row 3: StabilityVsSeverityScatter + SessionDrilldownPanel