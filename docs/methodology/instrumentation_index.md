# Instrumentation Index

This index maps every component of the interpretive stability instrumentation suite.

---

## 1. Schemas
- `schemas/interpretive_stability.schema.json`

---

## 2. Diagrams
- `docs/diagrams/stability_scoring_pipeline.md`
- `docs/diagrams/failure_mode_tagging_pipeline.md`

---

## 3. Methodology Specs
- `docs/methodology/interpretive_stability_scoring.md`
- `docs/methodology/stability_ingestion_service.md`
- `docs/methodology/realtime_stability_scoring.md`
- `docs/methodology/longitudinal_stability_dashboard.md`
- `docs/methodology/model_comparison_dashboard.md`
- `docs/methodology/analyst_console.md`

---

## 4. Frontend
- `frontend/types/stabilityApi.ts`
- `frontend/dashboards/longitudinal/`
- `frontend/dashboards/model_comparison/`
- `frontend/analyst_console/`

---

## 5. Backend
- `backend/ingestion/`
- `backend/realtime_scoring/`
- `backend/api/`

---

## 6. Data
- `data/stability/*.json`

---

## 7. Dependency Graph

schemas  
→ ingestion  
→ realtime scoring  
→ data  
→ dashboards  
→ analyst console  
→ doctrine updates

---
