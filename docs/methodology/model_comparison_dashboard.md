# Model Comparison Dashboard Specification

## Purpose
Compare interpretive stability and failure-mode profiles across models.

## Views

### 1. Model Stability Comparison
- Bar/boxplot per model
- Mean/median S_session
- Distribution (IQR)

### 2. Model Severity Profile
- Stacked bars per model
- Proportion of sessions at each severity level

### 3. Failure-Mode Profile
- Heatmap: models × failure modes
- Cell = % of sessions with mode

### 4. Delta View
- Select two models
- Show deltas in:
  - mean S
  - severity distribution
  - mode frequencies

## Data
- stability_sessions
- stability_turns
