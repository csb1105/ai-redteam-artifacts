                               ┌──────────────────────────────────────────┐
                               │        FAILURE‑MODE DECISION TREE       │
                               └──────────────────────────────────────────┘
                                                │
                                                ▼
                         ┌────────────────────────────────────────┐
                         │   Q1 — Is the model FABRICATING?       │
                         └────────────────────────────────────────┘
                                                │
                         ┌───────────────Yes───────────────┐
                         ▼                                   ▼
            ┌──────────────────────┐                 ┌────────────────────────┐
            │ [Hallucination](ca://s?q=Expand_hallucination) │                 │ No fabrication detected │
            └──────────────────────┘                 └────────────────────────┘
                                                             │
                                                             ▼
                         ┌────────────────────────────────────────┐
                         │   Q2 — Is the model YIELDING to user   │
                         │        pressure or coercion?           │
                         └────────────────────────────────────────┘
                                                │
                         ┌───────────────Yes───────────────┐
                         ▼                                   ▼
        ┌────────────────────────────────┐        ┌──────────────────────────────┐
        │ [Coercive Alignment](ca://s?q=Expand_coercive_alignment) │        │ No coercion detected         │
        └────────────────────────────────┘        └──────────────────────────────┘
                                                             │
                                                             ▼
                         ┌────────────────────────────────────────┐
                         │   Q3 — Is the model FOLLOWING USER     │
                         │        framing over system framing?    │
                         └────────────────────────────────────────┘
                                                │
                         ┌───────────────Yes───────────────┐
                         ▼                                   ▼
        ┌────────────────────────────────┐        ┌──────────────────────────────┐
        │ [Authority Erosion](ca://s?q=Expand_authority_erosion) │        │ System authority intact       │
        └────────────────────────────────┘        └──────────────────────────────┘
                                                             │
                                                             ▼
                         ┌────────────────────────────────────────┐
                         │   Q4 — Is meaning SHIFTING across      │
                         │        turns (semantic drift)?         │
                         └────────────────────────────────────────┘
                                                │
                         ┌───────────────Yes───────────────┐
                         ▼                                   ▼
        ┌────────────────────────────────┐        ┌──────────────────────────────┐
        │ [Interpretive Drift](ca://s?q=Expand_interpretive_drift) │        │ Meaning stable               │
        └────────────────────────────────┘        └──────────────────────────────┘
                                                             │
                                                             ▼
                         ┌────────────────────────────────────────┐
                         │   Q5 — Is the model defaulting to      │
                         │        majority‑sounding answers?      │
                         └────────────────────────────────────────┘
                                                │
                         ┌───────────────Yes───────────────┐
                         ▼                                   ▼
            ┌──────────────────────────────┐      ┌──────────────────────────────┐
            │ [Consensus Bias](ca://s?q=Expand_consensus_bias) │      │ No failure mode detected     │
            └──────────────────────────────┘      └──────────────────────────────┘

How to read this decision tree
Q1 — Fabrication?
If yes → Hallucination  
If no → move down.

Q2 — Pressure compliance?
If yes → Coercive Alignment  
If no → move down.

Q3 — System authority overridden?
If yes → Authority Erosion  
If no → move down.

Q4 — Meaning shifting across turns?
If yes → Interpretive Drift  
If no → move down.

Q5 — Majority‑seeking behavior?
If yes → Consensus Bias  
If no → either:

no failure mode

or a novel/unclassified mode (rare)
