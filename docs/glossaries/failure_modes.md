# Failure Modes Glossary

A controlled vocabulary for classifying AI system failures. This glossary should remain stable and versioned; changes must be deliberate.

## Consensus Bias

The model collapses toward majority-sounding or socially acceptable answers, regardless of truth or evidence.

## Coercive Alignment

The model shifts behavior to satisfy perceived user demands under pressure, even when those demands conflict with constraints or safety.

## Interpretive Drift

Gradual deviation from stable meaning across turns, where the model’s interpretation of key terms or constraints shifts over time.

See docs/diagrams/escalation_chain_propagation.md for how these modes propagate into escalation events.

## Authority Erosion

The model undermines, ignores, or contradicts authoritative constraints, policies, or system messages, especially after repeated user pressure.

See docs/diagrams/constraint_decay_flow.md for the staged progression from constraint to collapse.

See docs/diagrams/authority_erosion_ladder.md for the staged progression of authority collapse.

See docs/diagrams/system_constraint_flow.md for how system constraints degrade across layers.


## Hallucination

Fabrication of facts, sources, entities, or reasoning steps presented with unwarranted confidence.

## Failure Mode Taxonomy Diagram
<insert ASCII diagram here>
                           ┌──────────────────────────────┐
                           │        FAILURE MODES          │
                           │   (Interpretive Instability)  │
                           └──────────────────────────────┘
                                        │
                                        ▼
        ┌────────────────────────────────────────────────────────────────────┐
        │                        PRIMARY AXES                                │
        └────────────────────────────────────────────────────────────────────┘
                                        │
        ┌───────────────────────────────┼────────────────────────────────────┐
        ▼                               ▼                                    ▼
┌────────────────┐            ┌────────────────────┐               ┌────────────────────┐
│ [Semantic Drift]│            │ [Authority Erosion]│               │ [Factual Integrity]│
│ (Meaning shift) │            │ (Constraint decay) │               │ (Truth stability)  │
└────────────────┘            └────────────────────┘               └────────────────────┘
        │                               │                                    │
        ▼                               ▼                                    ▼
┌──────────────────────┐     ┌──────────────────────┐            ┌──────────────────────┐
│ [Interpretive Drift] │     │ [Coercive Alignment] │            │ [Hallucination]      │
│ (multi‑turn drift)   │     │ (pressure‑induced)   │            │ (fabrication)        │
└──────────────────────┘     └──────────────────────┘            └──────────────────────┘
        │                               │                                    │
        ▼                               ▼                                    ▼
┌──────────────────────┐     ┌──────────────────────┐            ┌──────────────────────┐
│ [Context Collapse]   │     │ [Constraint Bypass]  │            │ [Consensus Bias]     │
│ (loss of grounding)  │     │ (ignoring rules)     │            │ (majority‑seeking)   │
└──────────────────────┘     └──────────────────────┘            └──────────────────────┘
How to read this taxonomy
Top Layer — Failure Modes (the whole space)
All model breakdowns fall into the overarching category of interpretive instability — the system’s inability to maintain stable meaning, constraints, or truth across turns.

Primary Axes (the three governing dimensions)
1. Semantic Drift
Where meaning shifts over time.

Leads to:

Interpretive Drift

Context Collapse

2. Authority Erosion
Where constraints weaken or are overridden.

Leads to:

Coercive Alignment

Constraint Bypass

3. Factual Integrity
Where truth, grounding, or evidence fails.

Leads to:

Hallucination

Consensus Bias

See docs/diagrams/failure_mode_decision_tree.md for the decision logic used to classify failure modes.

For cross‑mode relationships, see docs/diagrams/failure_mode_interaction_matrix.md.

