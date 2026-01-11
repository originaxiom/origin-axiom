# Phase 5 – Scope

This document defines what Phase 5 is allowed to do, and what it is not
allowed to do, in the context of the Origin Axiom multi-phase program.

Phase 5 is a **meta-phase**. It does not introduce a new microscopic
mechanism or a new θ-model. Instead, it:

1. **Consumes locked upstream artifacts**
   - Reads Phase 3 vacuum-mechanism outputs:
     - `phase3/outputs/tables/mech_baseline_scan_diagnostics.json`
     - `phase3/outputs/tables/phase3_measure_v1_stats.json`
     - `phase3/outputs/tables/phase3_measure_v1_hist.csv`
     - `phase3/outputs/tables/phase3_instability_penalty_v1.json`
   - Reads Phase 4 FRW mapping + diagnostics outputs:
     - All Phase 4 F1 / FRW diagnostics listed in
       `phase5/config/phase5_inputs_v1.json`.

2. **Defines a stable “interface layer”**
   - Provides a single, programmatic view over these upstream outputs via:
     - `phase5/src/phase5/phase5_interface_v1.py`
     - `phase5/outputs/tables/phase5_interface_v1_summary.json`
   - Treats upstream artifacts as **read-only** and **locked** for the
     purpose of Phase 5 work (Rung 0–1).

3. **Prepares for external-facing synthesis (later rungs)**
   - Phase 5 will eventually host:
     - A public-facing Phase 5 paper (cosmology-facing synthesis),
     - Bundles that package selected upstream artifacts and derived
       summaries for readers and collaborators.
   - Phase 5 may integrate **optional external datasets**, such as
     FRW distance compilations, *without* changing the upstream pipeline.

4. **Acts as a gatekeeper for program-level claims**
   - No new fundamental physics mechanism is introduced here.
   - Instead, Phase 5 will:
     - Check that upstream claims are internally consistent,
     - Prepare pathways to confront them with data in a controlled way,
       without over-claiming.

---

## In-scope for Rung 0–1

For the current work (Rung 0 and Rung 1), Phase 5 is limited to:

1. **Interface sanity and wiring**
   - Ensure `phase5_interface_v1` locates all required upstream files.
   - Distinguish required vs. optional assets:
     - Required: Phase 3 and Phase 4 tables specified in
       `phase5_inputs_v1.json`.
     - Optional: `phase4/data/external/frw_distance_binned.csv`, and any
       similar future external datasets, documented as optional.

2. **Metadata + documentation**
   - Define:
     - `phase5/SCOPE.md` (this document),
     - `phase5/NON_CLAIMS.md`,
     - `phase5/ROLE_IN_PROGRAM.md`,
     - `phase5/PROGRESS_LOG.md` (Phase 5–specific chronology).
   - Keep these aligned with `docs/CLAIMS_INDEX.md` and the existing
     Phase 3 / Phase 4 documentation style.

3. **Gate integration**
   - Provide a Phase 5 gate script:
     - `scripts/phase5_gate.sh`
   - Gate behavior (Level A):
     - Run `phase5_interface_v1`,
     - Exit successfully if all required inputs exist,
     - Treat missing optional external data as a non-fatal condition.

---

## Out of scope (Rung 0–1)

At this stage, Phase 5 explicitly does **not**:

1. Produce a new cosmological parameter fit (e.g. \(H_0\), \(\Omega_\Lambda\)).
2. Claim to resolve tensions (Hubble tension, \(S_8\) tension, etc.).
3. Introduce new θ-parameter families or new mapping mechanisms.
4. Modify upstream pipelines in `phase3/` or `phase4/`.
5. Commit to a final public narrative about the real universe; this is
   preparatory work only.

Later rungs (Rung 2+) may extend the scope, but must do so by updating
this document and `phase5/NON_CLAIMS.md` accordingly.


---

## Companion docs and sandbox

For readers who want more detail on how Phase 5 is intended to sit on top of
the Phase 3 mechanism and Phase 4 FRW toys, and where exploratory ideas live:

- `docs/phase5_roadmap.md` sketches a roadmap for Phase 5 as an interface and
  sanity layer moving from toy FRW corridors toward data-contact. It is
  planning text, not a binding claims document, and must be read together with
  this scope and `phase5/NON_CLAIMS.md`.

- `sandbox/PHASE5_SANDBOX_*.md` files (for example,
  `sandbox/PHASE5_SANDBOX_GENERATION_NUMEROLOGY.md`,
  `sandbox/PHASE5_SANDBOX_H0_MPL_SCALING_IDEAS.md`, and
  `sandbox/PHASE5_SANDBOX_PHI_PHI_LAMBDA_NUMEROLOGY.md`) are explicitly
  non-canonical scratch pads. They are allowed to explore numerology and
  speculative ideas but do not alter the Phase 5 scope or claims.
