# Phase 3 (Mechanism) — Progress Log

## 2026-01-06 — Rung 0: Mechanism contract + flavor-v1 archival

- Created `phase3/MECHANISM_CONTRACT.md` defining the role of Phase 3 (Mechanism),
  required artifacts, theta-filter schema, run-id layout, reproducibility levels,
  and claims / non-claims, in a way that is compatible with the Phase 0 contract.
- Archived the previous flavor-sector exploratory Phase 3 under
  `experiments/phase3_flavor_v1/`, including its paper, claims, code, and gate scripts,
  so its negative result remains fully reproducible but no longer part of the
  canonical corridor.
- Removed the old Phase 3 theta filter from `phase0/phase_outputs/`, so the Phase 0
  corridor now aggregates only Phases 0–2 until a new mechanism-based
  `phase_03_theta_filter.json` is implemented.
