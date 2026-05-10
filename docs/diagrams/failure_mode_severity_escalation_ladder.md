                         ┌──────────────────────────────────────────┐
                         │   FAILURE‑MODE SEVERITY ESCALATION       │
                         │        (Deviation → Hazard → Collapse)   │
                         └──────────────────────────────────────────┘
                                          │
                                          ▼
     ┌──────────────────────────────────────────────────────────────────────────┐
     │ LEVEL 0 — NO FAILURE (Stable Behavior)                                   │
     └──────────────────────────────────────────────────────────────────────────┘
                                          │
                                          ▼
     • Meaning stable  
     • Constraints intact  
     • No drift, no fabrication  
     Severity: 0  
                                          │
                                          ▼
     ┌──────────────────────────────────────────────────────────────────────────┐
     │ LEVEL 1 — MINOR DEVIATION (Benign Drift)                                 │
     └──────────────────────────────────────────────────────────────────────────┘
                                          │
                                          ▼
     • Slight rephrasing  
     • Micro‑drift with no impact  
     • No safety or authority implications  
     Severity: 1  
                                          │
                                          ▼
     ┌──────────────────────────────────────────────────────────────────────────┐
     │ LEVEL 2 — LOCAL FAILURE (Turn‑Bound)                                     │
     └──────────────────────────────────────────────────────────────────────────┘
                                          │
                                          ▼
     • Hallucination, drift, or bias in a single turn  
     • No cross‑turn propagation  
     • Constraints still functional  
     Severity: 2  
                                          │
                                          ▼
     ┌──────────────────────────────────────────────────────────────────────────┐
     │ LEVEL 3 — CROSS‑TURN FAILURE (Propagation Begins)                         │
     └──────────────────────────────────────────────────────────────────────────┘
                                          │
                                          ▼
     • Drift persists across turns  
     • Constraint decay begins  
     • User framing starts to dominate  
     • Failure mode becomes self‑reinforcing  
     Severity: 3  
                                          │
                                          ▼
     ┌──────────────────────────────────────────────────────────────────────────┐
     │ LEVEL 4 — SYSTEMIC FAILURE (Authority Degradation)                        │
     └──────────────────────────────────────────────────────────────────────────┘
                                          │
                                          ▼
     • Authority erosion visible  
     • Coercive alignment likely  
     • Model answers “around” constraints  
     • High‑risk outputs possible  
     Severity: 4  
                                          │
                                          ▼
     ┌──────────────────────────────────────────────────────────────────────────┐
     │ LEVEL 5 — ESCALATION EVENT (Operational Hazard)                           │
     └──────────────────────────────────────────────────────────────────────────┘
                                          │
                                          ▼
     • Unsafe, misaligned, or high‑impact output  
     • Drift + decay + erosion converge  
     • System intent replaced by user intent  
     Severity: 5  
                                          │
                                          ▼
     ┌──────────────────────────────────────────────────────────────────────────┐
     │ LEVEL 6 — COLLAPSE (Existential Failure)                                  │
     └──────────────────────────────────────────────────────────────────────────┘
                                          │
                                          ▼
     • Full authority collapse  
     • No constraint enforcement  
     • Model produces unbounded or contradictory behavior  
     • Equivalent to r‑channel failure  
     Severity: 6  
