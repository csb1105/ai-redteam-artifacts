# Reporting Guidelines

All reports must follow a consistent structure to ensure clarity, comparability, and auditability.

## Required Sections

1. **Summary of Findings**  
   - One to three paragraphs describing what was observed and why it matters.

2. **Failure Mode Classification**  
   - Primary failure mode(s) and any secondary modes.  
   - Reference `docs/glossaries/failure_modes.md`.
   - For authority-related failures, reference the Authority Erosion Ladder in docs/diagrams/.
   - Use the Failure‑Mode Decision Tree (docs/diagrams/failure_mode_decision_tree.md) to determine the correct classification.
   - See docs/diagrams/failure_mode_interaction_matrix.md for cross‑mode interactions and escalation pathways.

3. **Evidence**  
   - Transcript excerpts with turn numbers or timestamps.  
   - Enough context to understand the behavior without reading the full session.

4. **Severity Assessment**  
   - Severity level (1–5) with justification.  
   - Note any uncertainty or missing information.
   - Use the Failure‑Mode Severity Escalation Ladder to determine escalation level and risk.

5. **Contributing Factors**  
   - Prompt patterns, user pressure, ambiguity, or model limitations that contributed.
   - Escalation risk should be evaluated using the Escalation‑Chain Propagation diagram.
   - Constraint‑related failures should be evaluated using the System‑Constraint Flow diagram.

6. **Recommended Mitigations**  
   - Model-level, prompt-level, or system-level mitigations.  
   - Indicate which are speculative vs. tested.

7. **Follow-Up Actions**  
   - Retest plans, monitoring, or escalation paths.

8. **Refer to the Red‑Team Cycle Diagram** (docs/diagrams/redteam_cycle_diagram.md) to align reporting with the operational lifecycle.

9. **Metrics**
   - Sessions MAY include an Interpretive Stability Score S as defined in docs/methodology/interpretive_stability_scoring.md.
   - Interpretive Stability Scores MUST conform to schemas/interpretive_stability.schema.json.
   - Interpretive Stability Scores are produced via the pipeline in docs/diagrams/stability_scoring_pipeline.md.


## Evidence Standards

- Do not paraphrase critical evidence; quote directly.  
- Avoid cherry-picking; note counterexamples if they exist.  
- Maintain a clear link between evidence and classification.

- See docs/diagrams/failure_mode_tagging_pipeline.md for the end‑to‑end tagging and reporting pipeline.

