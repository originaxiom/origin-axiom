# Stage 2: Archive and Canonical Status Map (2026-01-09)

## Purpose

This document provides a quick map of which parts of the repository are canonical, which are archived or experimental, and which are scratch or sandbox areas. The goal is that a new collaborator, or a future version of us, can answer a simple question:

> “If I read or change something here, am I touching the canonical phased program, a Stage 2 diagnostic belt, or a non-canonical experiment?”

It is a Stage 2 diagnostic document: it does not itself create or remove claims, but it describes the intended status of each top-level area.

## Canonical phased program

These directories define the core Origin-Axiom program as it currently stands:

- `phase0/` – Governance and specification layer.
  - Claims, contracts, and method rules live here.
  - Source of truth for what counts as a claim and how evidence must be presented.
- `phase1/` – Toy ensembles (locked).
  - Canonical toy-domain existence / robustness / scaling claims.
  - Paper and figures are considered stable at this rung.
- `phase2/` – Mode-sum model + bounded FRW diagnostics (under audit).
  - Implements the residue in a stricter mode-sum toy model.
  - FRW-style viability language, deliberately kept diagnostic.
- `phase3/` – Mechanism module (active).
  - Baseline non-cancellation floor on a global amplitude.
  - Binding-style diagnostics and mechanism-level tables.
  - No flavor calibration in canonical `phase3/`.
- `phase4/` – FRW toy diagnostics (stub).
  - Maps Phase 3 outputs into FRW-style backgrounds and viability masks.
  - Provides hooks for data probes without claiming real-data fits.
- `phase5/` – Interface and sanity layer (early rungs).
  - Reads locked Phase 3/4 outputs and emits interface summaries and sanity tables.
  - No new mechanism or cosmology claims.

All physics claims, when referenced from global indexes, should ultimately anchor back to artifacts and papers in these phase directories.

## Stage 2 diagnostic belts (non-canonical, downstream)

Stage 2 lives under `stage2/` and is explicitly **non-canonical**. It is downstream of Phase 3/4 and may be promoted later on a per-rung basis.

Current belts include:

- `stage2/frw_corridor_analysis/`
  - FRW corridor and family analysis rungs (R1–R9, plus doc rung).
- `stage2/mech_measure_analysis/`
  - Mechanism and measure diagnostics over Phase 3 tables.
- `stage2/joint_mech_frw_analysis/`
  - Joint diagnostics on a shared θ-grid between Phase 3 mechanism outputs and Phase 4 FRW masks.
- `stage2/frw_data_probe_analysis/`
  - Audit of FRW data-probe hooks without promoting any data-driven claims.
- `stage2/docs/`
  - Stage 2 documentation, including this archive map and the doc-audit summary.

Stage 2 modules are allowed to be exploratory and may be revised more aggressively, as long as they remain downstream and do not silently change Phase 0–5 claims.

## Archived and experimental areas

These areas are **not canonical**. They may contain ideas, scripts, or results that informed the current program, but they do not carry claims by default.

- `experiments/phase3_flavor_v1/`
  - Archived flavor-sector calibration add-on.
  - Contains CKM/PMNS-based θ-filter work that has been explicitly demoted to a non-canonical experiment.
  - Any future resurrection of this line must go through a fresh, gated Phase or Stage design with clear claims and evidence.
- `experiments/` (other subdirectories)
  - By default, anything under `experiments/` is exploratory.
  - Promotion requires:
    - a short migration note under `docs/` or `phase0/`,
    - a clear target phase,
    - and a gate-checked implementation in that phase or in Stage 2.
- `sandbox/`, `notes/`, or similar scratch areas
  - Used for local sketches, one-off checks, or ad-hoc scripts.
  - Nothing here should be cited as evidence in a canonical claim without being migrated into a proper phase or Stage 2 module.

## Retired or demoted content

Some ideas, constants, or ansätze have been tried and explicitly retired or demoted. When they are kept in the repo:

- They should be clearly labeled as **retired**, **legacy**, or **demoted** in the relevant file headers or README.
- They must not be referenced as if they were part of the current phased program, except in the context of historical notes.

If you encounter a directory or file that appears to carry claims but is not clearly in `phase0/`–`phase5/` or Stage 2, it should either:

1. Be marked as retired/legacy and moved under an experiments or legacy area, or
2. Be properly migrated into a phase or Stage 2 with a clear scope and gate.

## How to use this map

- When adding new work:
  - Decide whether it is canonical (belongs in `phase0/`–`phase5/`), diagnostic (belongs in `stage2/`), or experimental (belongs under `experiments/` or scratch).
  - Reflect that status in the local README and, if relevant, in `docs/PHASES.md` or other global docs.
- When reading or reviewing:
  - Use this file plus `docs/STATE_OF_REPO.md` to orient yourself before trusting any claim or diagram.
  - Treat anything outside the canonical tree as suggestive, not binding.

This document should be updated whenever a major directory changes status (for example, when a Stage 2 belt is promoted into a Phase, or when a large experiment is formally archived).
