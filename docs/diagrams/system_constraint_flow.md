                           ┌──────────────────────────────────────────┐
                           │        SYSTEM–CONSTRAINT FLOW            │
                           │ (Origin → Propagation → Degradation)     │
                           └──────────────────────────────────────────┘
                                            │
                                            ▼
        ┌──────────────────────────────────────────────────────────────────────────┐
        │   LAYER 0 — ORIGIN: SYSTEM‑LEVEL CONSTRAINTS                             │
        └──────────────────────────────────────────────────────────────────────────┘
                                            │
                                            ▼
    • Hard constraints (safety, policy, architecture)
    • Developer‑defined rules + system messages
    • Non‑negotiable boundaries
    r₀: Full integrity
                                            │
                                            ▼
        ┌──────────────────────────────────────────────────────────────────────────┐
        │   LAYER 1 — INTERPRETATION: MODEL INTERNALIZATION                        │
        └──────────────────────────────────────────────────────────────────────────┘
                                            │
                                            ▼
    • Model interprets system constraints
    • Converts them into latent behavioral priors
    • Vulnerable to ambiguity + misinterpretation
    r: Integrity depends on clarity + consistency
                                            │
                                            ▼
        ┌──────────────────────────────────────────────────────────────────────────┐
        │   LAYER 2 — POLICY APPLICATION: TURN‑LEVEL EXECUTION                     │
        └──────────────────────────────────────────────────────────────────────────┘
                                            │
                                            ▼
    • Constraints applied to each turn
    • Safety checks, refusal logic, guardrails
    • First point where user pressure interacts
    r: Begins to weaken under adversarial load
                                            │
                                            ▼
        ┌──────────────────────────────────────────────────────────────────────────┐
        │   LAYER 3 — USER INTERACTION: PRESSURE + FRAMING                         │
        └──────────────────────────────────────────────────────────────────────────┘
                                            │
                                            ▼
    • User framing competes with system framing
    • Pressure, coercion, ambiguity, repetition
    • Constraint decay begins (softening, hedging)
    r: Split state (system vs. user authority)
                                            │
                                            ▼
        ┌──────────────────────────────────────────────────────────────────────────┐
        │   LAYER 4 — DRIFT + DECAY: CROSS‑TURN PROPAGATION                        │
        └──────────────────────────────────────────────────────────────────────────┘
                                            │
                                            ▼
    • Interpretive drift compounds
    • Constraint reminders become formulaic
    • Model begins answering “around” rules
    r: Functionally degraded
                                            │
                                            ▼
        ┌──────────────────────────────────────────────────────────────────────────┐
        │   LAYER 5 — FAILURE: AUTHORITY COLLAPSE                                  │
        └──────────────────────────────────────────────────────────────────────────┘
                                            │
                                            ▼
    • System constraints no longer shape behavior
    • User intent fully replaces system intent
    • Unsafe or misaligned outputs become possible
    r: Non‑functional (collapse)
