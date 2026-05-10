                     ┌──────────────────────────────────────────┐
                     │     FAILURE‑MODE TAGGING PIPELINE        │
                     │ (Transcript → Tags → Reports → Synthesis)│
                     └──────────────────────────────────────────┘
                                      │
                                      ▼
        ┌────────────────────────────────────────────────────────────┐
        │   STAGE 1 — INGEST: SESSIONS + METADATA                    │
        └────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
        • Input: sessions/<id>/transcript.md  
        • Input: sessions/<id>/metadata.json  
        • Context: model, date, prompt suite, notes  

                                      │
                                      ▼
        ┌────────────────────────────────────────────────────────────┐
        │   STAGE 2 — PREPROCESS: NORMALIZE + SEGMENT                │
        └────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
        • Clean formatting, remove noise  
        • Segment into turns / exchanges  
        • Attach turn‑level metadata (speaker, timestamp, etc.)  

                                      │
                                      ▼
        ┌────────────────────────────────────────────────────────────┐
        │   STAGE 3 — DETECTION: FAILURE SIGNATURE SCAN              │
        └────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
        • Apply heuristics / models to detect:  
          – hallucination  
          – coercive alignment  
          – authority erosion  
          – interpretive drift  
          – consensus bias  
        • Mark candidate spans with provisional labels  

                                      │
                                      ▼
        ┌────────────────────────────────────────────────────────────┐
        │   STAGE 4 — TAGGING: MODE + SEVERITY ASSIGNMENT            │
        └────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
        • Map signatures → canonical failure modes  
        • Assign severity (0–6) using escalation ladder  
        • Store tags in machine‑readable form (e.g., JSON)  

                                      │
                                      ▼
        ┌────────────────────────────────────────────────────────────┐
        │   STAGE 5 — REPORTING: HUMAN‑READABLE ARTIFACTS            │
        └────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
        • Generate failure‑mode reports (reports/failure_mode_reports/)  
        • Include evidence excerpts + tags + severity  
        • Link to diagrams (decision tree, interaction matrix, etc.)  

                                      │
                                      ▼
        ┌────────────────────────────────────────────────────────────┐
        │   STAGE 6 — SYNTHESIS: AGGREGATION + TRENDS                │
        └────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
        • Aggregate tags across sessions  
        • Identify patterns, co‑occurrence, escalation chains  
        • Produce synthesis docs (reports/synthesis/)  

                                      │
                                      ▼
        ┌────────────────────────────────────────────────────────────┐
        │   STAGE 7 — FEEDBACK: DOCTRINE + TOOLING UPDATE            │
        └────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
        • Refine prompt suites, diagrams, and methodology  
        • Update classifiers / heuristics  
        • Close the loop into preparation phase of Red‑Team Cycle  

The scoring stage outputs JSON conforming to schemas/interpretive_stability.schema.json.

The scoring pipeline feeds into the tagging pipeline via schema-compliant JSON outputs.

