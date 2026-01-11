# Phase 5 interface table design (Stage 2 verdicts → program-facing summaries)

Status (2026-01-11): This document is a design note for Phase 5 interface tables. It specifies which Stage 2 verdicts and tables Phase 5 is expected to surface as program-facing summaries, and in what form. It is a planning document (non-binding) and does not introduce new physics claims beyond those already present in Phases 0–4 and Stage 2.

## 1. Scope and role

Phase 5 is defined as an interface and sanity layer over:

- locked Phase 0–3 contracts and papers,
- the Phase 4 FRW toy stub and its FRW tables, and
- Stage 2 diagnostic belts and verdict docs.

Its job is to provide:

- compact **program verdict tables**,
- reader-facing **status summaries**, and
- clear separation between what is **established internally** (toy-universe structure, redundancy, negative results) and what remains **open** (real data, canonical θ-measure, θ★ selection).

Phase 5 does not add new physics pipelines at this rung; it organises and exposes the Stage 2 verdicts.

## 2. Inputs from Stage 2 and phases

Phase 5 interface tables are expected to draw on:

- FRW verdict and diagnostics:
  - `stage2/frw_corridor_analysis/docs/STAGE2_FRW_VERDICT_v1.md`
  - `stage2/frw_corridor_analysis/docs/STAGE2_FRW_CORRIDOR_SUMMARY_v1.md`
  - `stage2/frw_data_probe_analysis/docs/STAGE2_FRW_DATA_PROBE_AUDIT_v1.md`
  - FRW tables under `phase4/outputs/tables/`.
- Mechanism verdict and diagnostics:
  - `stage2/mech_measure_analysis/docs/STAGE2_MECH_VERDICT_v1.md`
  - `stage2/mech_measure_analysis/docs/STAGE2_MECH_MEASURE_SUMMARY_v1.md`
  - mechanism tables under `phase3/outputs/tables/`.
- Joint mech–FRW verdict:
  - `stage2/joint_mech_frw_analysis/docs/STAGE2_JOINT_VERDICT_v1.md`
  - `stage2/joint_mech_frw_analysis/docs/STAGE2_JOINT_MECH_FRW_SUMMARY_v1.md`
  - `stage2_joint_theta_grid_v1.csv` and related outputs.
- θ★ and master verdicts:
  - `stage2/theta_star_analysis/docs/STAGE2_THETA_STAR_ALIGNMENT_v1.md`
  - `stage2/docs/STAGE2_MASTER_VERDICT_v1.md`.
- Phase alignment memos:
  - `phase3/PHASE3_ALIGNMENT_v1.md`
  - `phase4/PHASE4_ALIGNMENT_v1.md`
  - `phase5/PHASE5_ALIGNMENT_v1.md`.

Phase 5 interface work should treat these documents as **inputs and constraints**, not as things to be silently overridden.

## 3. Proposed Phase 5 interface tables

The following tables are proposed as Phase 5 interface artifacts. Names and numbering are placeholders for future LaTeX/CSV implementations.

### Table P5-1: FRW viability and family fractions (toy universe snapshot)

- Purpose: summarise the FRW toy world structure over θ at a glance.
- Content (conceptual):
  - number of grid points and θ-range,
  - fraction of grid in:
    - ALL_GRID,
    - FRW_VIABLE,
    - LCDM_LIKE,
    - TOY_CORRIDOR,
    - CORRIDOR_AND_VIABLE,
    - CORRIDOR_AND_LCDM,
    - FRW_VIABLE_AND_DATA_OK (noting that this is currently empty),
  - notes on contiguity/robustness tests (qualitative).
- Source:
  - Stage 2 FRW verdict and corridor summary,
  - FRW tables and family definitions used in Stage 2.

### Table P5-2: Mechanism diagnostics and preferred candidates

- Purpose: show what the Phase 3 mechanism actually produces as θ-dependent diagnostics.
- Content (conceptual):
  - list of “preferred” mechanism-derived diagnostics (column names),
  - type (measure-like vs flag-like),
  - basic numeric ranges and qualitative θ-profile notes (e.g. smooth / monotone / peaked),
  - statement that none is promoted to a canonical θ-measure.
- Source:
  - Stage 2 mechanism verdict and measure summary,
  - Phase 3 mechanism tables.

### Table P5-3: Joint mech–FRW redundancy summary

- Purpose: quantify how redundant Phase 3 scalars are with Phase 4 FRW scalars.
- Content (conceptual):
  - selected pairs of FRW scalars (E_vac, omega_lambda, age_Gyr) and mechanism scalars,
  - their correlation coefficients (or a qualitative scale: very strong / strong / moderate),
  - short notes on redundancy (e.g. “acts as reparameterisation of E_vac”).
- Source:
  - Stage 2 joint verdict and correlation summary,
  - `stage2_joint_mech_frw_rung3_correlations_v1.csv`.

### Table P5-4: θ★ status in the current toy universe

- Purpose: give a single, auditable view of θ★ in the current snapshot.
- Content (conceptual):
  - whether θ★ is in FRW_VIABLE, LCDM_LIKE, TOY_CORRIDOR, intersections,
  - mechanism diagnostic values at θ★ vs family means,
  - a clear statement that θ★ is inside the viable band but not singled out by any current diagnostic,
  - explicit classification as “negative-result sanity check” for this snapshot.
- Source:
  - θ★ alignment doc,
  - FRW and mechanism verdict docs.

### Table P5-5: Program-level Stage 2 verdicts

- Purpose: record what the program can safely claim at the Stage 2 snapshot.
- Content (conceptual):
  - small set of rows, each with:
    - verdict label (e.g. “FRW viability band exists”, “no canonical θ-measure”, “data gate closed”, “θ★ not selected”),
    - status (true in current snapshot),
    - backing documents (Stage 2 verdicts, alignment memos),
    - comment about future work (e.g. “could change under new belts / data gate revision”).
- Source:
  - Stage 2 master verdict,
  - Phase 5 alignment memo.

These tables are **interface views**: they do not define new quantities, only organise existing Stage 2 verdicts.

## 4. Separation of internal verdicts vs external claims

Phase 5 interface tables should enforce a clear separation between:

- **Internal verdicts**:
  - statements about the behavior of the current toy mechanism+FRW pipeline and Stage 2 diagnostics (e.g. existence of a viability band, redundancy, closed data gate, negative θ★ result).
- **External claims or speculations**:
  - anything that would speak about real cosmological data, observed parameters, or broader phenomenology.

At this design rung:

- only **internal verdicts** are admitted into P5 tables,
- any external-facing interpretation is deferred to future design notes or separate workspaces and must not be silently folded into Phase 5 tables.

## 5. Implementation notes (deferred)

This document defines **what** Phase 5 should eventually expose, not **how** to generate it. A later Phase 5 interface belt is expected to:

- define scripts or notebooks that read Stage 2 CSVs and produce the interface tables as CSV/LaTeX,
- ensure that the resulting tables are fully reproducible from locked Phase 3/4 artifacts and Stage 2 pipelines,
- and tie the generated tables into the Phase 5 paper under its reproducibility contract.

Those steps are explicitly deferred to a future belt and will be recorded in `phase5/PROGRESS_LOG.md` and `PROGRESS_LOG.md` when enacted.
