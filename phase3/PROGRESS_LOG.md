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

## 2026-01-06 — Rung 1: Phase 3 mechanism skeleton + gate

- Created a fresh Phase 3 mechanism namespace under `phase3/` (paper,
  src, outputs, artifacts, workflow) distinct from the archived
  `experiments/phase3_flavor_v1/` flavor-calibration experiment.
- Added a Rung-1 skeleton paper (`phase3/paper/main.tex`) with
  introduction, mechanism-design placeholder, baseline-experiments
  placeholder, limitations, and reproducibility appendices, aligned
  with the Phase 0 contract and Phase 3 mechanism contract.
- Implemented a minimal Snakemake workflow in
  `phase3/workflow/Snakefile` that builds the Phase 3 paper and exports
  the canonical artifact `phase3/artifacts/origin-axiom-phase3.pdf`.
- Added `scripts/phase3_gate.sh` so that `bash scripts/phase3_gate.sh
  --level A|B` from repo root regenerates the Phase 3 artifact in a
  clean repository.
- No physical mechanism, numerical experiments, or theta-filter
  artifacts are defined at this rung; the skeleton only prepares the
  structure for later rungs.
