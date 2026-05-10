# Red-Team Cycle

This document defines the operational cycle for AI red‑team evaluations.

## 1. Preparation
- Define threat model
- Select adversarial prompt suite
- Establish evaluation criteria and severity scale
- See docs/diagrams/system_constraint_flow.md for the full constraint‑origin and propagation model.


## 2. Execution
- Run multi‑turn adversarial sessions
- Capture transcripts and metadata
- Log deviations, drift, and failure signatures
- Authority degradation should be evaluated using the Authority Erosion Ladder (docs/diagrams/authority_erosion_ladder.md).
- See docs/diagrams/escalation_chain_propagation.md for the propagation model from drift to escalation.


## 3. Classification
- Map behaviors to failure modes
- Assign severity and confidence
- Update machine‑readable catalogs
- Analysts should reference the Failure‑Mode Decision Tree when mapping behaviors to failure modes.
- Analysts should consult the Failure‑Mode Interaction Matrix to identify compound or cascading failures.
- Severity progression should be evaluated using the Failure‑Mode Severity Escalation Ladder.

## 4. Reporting
- Generate failure‑mode reports
- Produce synthesis documents
- Feed findings back into doctrine

## 5. Iteration
- Expand prompt suite
- Refine methodology
- Re-run sessions for longitudinal tracking

## Constraint Decay Flow
See docs/diagrams/constraint_decay_flow.md for the staged model of constraint degradation.

## Red‑Team Cycle Diagram
See docs/diagrams/redteam_cycle_diagram.md for the visual representation of the operational cycle.


