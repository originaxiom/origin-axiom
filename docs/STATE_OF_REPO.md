# Repository State (Single Source of Truth)

This document summarizes the current phase status, canonical artifacts, and reproducibility entry points for the origin-axiom program.

## Canonical policy

- Canonical PDFs live in `phase*/artifacts/`.
- Canonical figures live in `phase*/outputs/figures/`.
- Ephemeral runs are not tracked (for example, `**/outputs/runs/`, `.snakemake/`).
- Stage 2 diagnostics live under `stage2/` and remain non-canonical until explicitly promoted into a Phase.
- For a directory-level view of phases, Stage 2 belts, and experiments, see [`REPO_MAP_AND_ATLAS_v1.md`](REPO_MAP_AND_ATLAS_v1.md).

## Phase status (high-level)

- **Phase 0**: governance and specification layer (no physics claims).
- **Phase 1**: toy-domain existence, robustness, and scaling claims (locked).
- **Phase 2**: mode-sum model plus bounded FRW-style viability checks (under audit).
- **Phase 3**: mechanism module (toy non-cancellation floor plus binding-style diagnostics; no flavor calibration in canonical `phase3/`).
- **Phase 4**: FRW toy diagnostics stub (downstream mapping of Phase 3 outputs into toy FRW backgrounds; no real-data claims).
- **Phase 5**: interface and sanity layer (reads locked Phase 3/4 artifacts and emits summaries and sanity tables; no new mechanism or cosmology claims).
- **Stage 2**: diagnostic belts over Phase 3/4 outputs (`frw_corridor_analysis`, `mech_measure_analysis`, `joint_mech_frw_analysis`, `frw_data_probe_analysis`, and documentation audit tools). All Stage 2 work is strictly downstream and non-canonical.

## Reproducibility entry points

These are the canonical entry points for reproducing phase-level artifacts. When in doubt, prefer the per-phase reproducibility notes or local READMEs over ad-hoc scripts.

- **Phase 0**: compile the paper in `phase0/paper/` (see `phase0/REPRODUCIBILITY.md` if present).
- **Phase 1**: `cd phase1 && snakemake -c 1 all`
- **Phase 2**: `cd phase2 && snakemake -c 1 all`
- **Phase 3**: see `phase3/ROLE_IN_PROGRAM.md` and the Phase 3 paper appendices for the current gate and run instructions.
- **Phase 4**: see `phase4/OVERVIEW.md` and the Phase 4 paper notes for FRW toy-diagnostic reproducibility.
- **Phase 5**: see `phase5/SCOPE.md` and the Phase 5 paper notes for interface-layer entry points.
- **Stage 2**: see `stage2/docs/STAGE2_OVERVIEW_v1.md` and the local docs under each Stage 2 module for belt-specific entry points.

## Claims indexing

- Global claims map: `docs/CLAIMS_INDEX.md`.
- Phase 0 method claims: `phase0/CLAIMS.md`.
- Phase 1 physics claims: `phase1/CLAIMS.md`.
- Phase 2 physics claims: `phase2/CLAIMS.md`.
- Phase 3 physics claims: recorded in the Phase 3 paper appendix (`phase3/paper/appendix/`) and `phase3/ROLE_IN_PROGRAM.md` (there is no standalone `phase3/CLAIMS.md` at this rung).
- Stage 2 diagnostic belts do not carry independent claims; they are downstream views of Phase 3/4 artifacts.
## Governance companion docs

For more detailed governance and structural guidance, see:

- `docs/ARCHIVE.md` – archive and deprecation policy (how exploratory work is retired or migrated).
- `docs/GATES_AND_STATUS.md` – central index of gates, status labels, and canonical vs downstream layers.
- `docs/REPRODUCIBILITY.md` – global reproducibility and gate rules.

## Stage 2 documentation and repo-audit status

Stage 2 includes a documentation and repo-audit belt that keeps the written
surface of the repository aligned with the actual Phase/Stage artifacts and
Phase 0 contracts. Its role is to:

- inventory documentation and structural files,
- flag broken references, orphaned docs, and open TODO/TBD-style threads, and
- propose small, manually applied documentation rungs (navigation fixes,
  archive labels, companion-doc links, etc.), recorded in `PROGRESS_LOG.md`.

The current status of this belt, including which manual rungs have been applied
so far, is described in:

- `stage2/docs/STAGE2_DOC_AUDIT_SUMMARY_v1.md`

This belt introduces no new physical claims and does not modify Phase 0–5
numerical artifacts; it is part of the governance and audit infrastructure
of the project.

---

Alignment memos (Phase 2–5): For phase-local alignment between scope/claims/contracts, LaTeX papers, and Stage 2 diagnostics, see:

- `phase2/PHASE2_ALIGNMENT_v1.md`
- `phase3/PHASE3_ALIGNMENT_v1.md`
- `phase4/PHASE4_ALIGNMENT_v1.md`
- `phase5/PHASE5_ALIGNMENT_v1.md`

These memos are descriptive snapshots and do not introduce new claims; they record how the current papers and Stage 2 belts line up with each phase’s contracts and reproducibility docs.
