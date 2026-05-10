# Analyst Console Specification

## Purpose
Provide a human-in-the-loop interface for reviewing sessions, validating failure modes, adjusting severity, and annotating doctrine-relevant patterns.

## Panels

### 1. Session List
- Columns: session_id, timestamp, model, scenario, S_session, max_severity, modes[]
- Filters: date, model, suite, scenario, severity, modes
- Actions: open session, mark for review, export

### 2. Session Review Panel
- Transcript with turn-level D/C/A/S and failure-mode badges
- Session summary (scores, severity, modes)
- Analyst controls:
  - Override failure modes
  - Adjust severity
  - Add tags
  - Notes

### 3. Annotation Log
- who, when, what changed
- exportable

### 4. Feedback Hooks
- Mark session as:
  - training candidate
  - policy update candidate
  - instrumentation bug
