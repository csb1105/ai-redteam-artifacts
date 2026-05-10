# AI Red Team Artifacts

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
![Status](https://img.shields.io/badge/status-active-green.svg)
![Domain](https://img.shields.io/badge/domain-AI%20Red%20Team-critical.svg)

A doctrine-aligned, evidence-driven repository for AI red-team operations. This repo captures the full lifecycle of adversarial evaluation: prompt design, multi-turn sessions, failure-mode classification, synthesis, and methodological doctrine.

---

## Purpose

This repository is a **living corpus of AI red-team artifacts**. It is designed to:

- **Systematically probe** models for failure modes and interpretive instability  
- **Document evidence** in a structured, auditable way  
- **Classify and track** failure modes over time  
- **Support governance and doctrine** for mission-critical deployments  

The structure reflects a separation of concerns:

- `prompts/` — adversarial and baseline suites  
- `sessions/` — concrete test runs with transcripts and metadata  
- `reports/` — failure-mode reports and synthesis documents  
- `libraries/` — machine-readable catalogs of prompts and failure modes  
- `docs/` — methodology, glossaries, and reporting doctrine  
- `tools/` — parsing and analysis utilities

---

## Repository structure

```text
ai-redteam-artifacts/
├── README.md
├── docs/
│   ├── methodology/
│   ├── glossaries/
├── prompts/
│   ├── adversarial/
│   └── baseline/
├── sessions/
├── reports/
│   ├── failure_mode_reports/
│   └── synthesis/
├── libraries/
└── tools/

## Workflow
- See docs/diagrams/redteam_cycle_diagram.md for the full cycle diagram.
- See docs/diagrams/escalation_chain_propagation.md for the escalation‑chain model.
- See docs/diagrams/authority_erosion_ladder.md for the authority erosion ladder diagram.
- See docs/diagrams/constraint_decay_flow.md for the constraint decay mode diagram. 
- See docs/diagrams/interpretive_drift_timeline.md for the interpretative drift timeline diagram. 
- See docs/diagrams/system_constraint_flow.md for the system constraint flow diagram. 
- See docs/diagrams/failure_mode_decision_tree.md for the classification decision tree.
- See docs/diagrams/failure_mode_tagging_pipeline.md for the transcript → tags → reports → synthesis pipeline.

##Architecture
- See docs/diagrams/system_constraint_flow.md for the system‑constraint flow diagram.

##Doctrine
- See docs/diagrams/failure_mode_interaction_matrix.md for the interaction matrix.
- See docs/diagrams/failure_mode_severity_escalation_ladder.md for the severity escalation ladder.

##Data Structures
- Interpretive Stability Schema: schemas/interpretive_stability.schema.json

## Instrumentation
- Interpretive Stability Scoring Pipeline: docs/diagrams/stability_scoring_pipeline.md
- Longitudinal stability dashboard spec: docs/methodology/longitudinal_stability_dashboard.md




