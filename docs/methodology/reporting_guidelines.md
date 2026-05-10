# Reporting Guidelines

All reports must follow a consistent structure to ensure clarity, comparability, and auditability.

## Required Sections

1. **Summary of Findings**  
   - One to three paragraphs describing what was observed and why it matters.

2. **Failure Mode Classification**  
   - Primary failure mode(s) and any secondary modes.  
   - Reference `docs/glossaries/failure_modes.md`.

3. **Evidence**  
   - Transcript excerpts with turn numbers or timestamps.  
   - Enough context to understand the behavior without reading the full session.

4. **Severity Assessment**  
   - Severity level (1–5) with justification.  
   - Note any uncertainty or missing information.

5. **Contributing Factors**  
   - Prompt patterns, user pressure, ambiguity, or model limitations that contributed.

6. **Recommended Mitigations**  
   - Model-level, prompt-level, or system-level mitigations.  
   - Indicate which are speculative vs. tested.

7. **Follow-Up Actions**  
   - Retest plans, monitoring, or escalation paths.

## Evidence Standards

- Do not paraphrase critical evidence; quote directly.  
- Avoid cherry-picking; note counterexamples if they exist.  
- Maintain a clear link between evidence and classification.
