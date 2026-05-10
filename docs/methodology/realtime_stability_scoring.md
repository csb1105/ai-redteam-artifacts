# Real-Time Interpretive Stability Scoring Specification

## Purpose
Compute D, C, A, S for each turn during an active session and emit streaming metrics for dashboards and logs.

## Inputs
- session_id
- turn_index
- speaker
- text
- timestamp

## Pipeline Per Turn
1. Load session context (weights, initial intent, constraint/authority state).
2. Compute Drift (D) via semantic distance.
3. Compute Constraint Decay (C) via ladder level / 5.
4. Compute Authority Erosion (A) via ladder level / 5.
5. Compute Stability:
   S_turn = 1 − (w_D·D + w_C·C + w_A·A)
6. Detect failure modes.
7. Emit event:
   - session_id
   - turn_index
   - D, C, A, S
   - failure_modes[]

## Outputs
- Streamed turn-level scoring events.
- Later aggregated into session-level JSON.
