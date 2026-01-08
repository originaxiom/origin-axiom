# Legacy Migrations (Origin Axiom)

Purpose
This document records legacy runs, artifacts, and logs in
`../origin-axiom-legacy` that are candidates for migration into the phased
repository under Phase 0 contract rules. It is a governance and provenance map,
not a claim document.

Scope (Phase 0 compatible)
- In scope: provenance, evidence pointers, reproducibility status, and proposed
  phase ownership for legacy runs.
- Out of scope: asserting physics claims or endorsing a specific theta_star.
- This file does not create new claims. All future claims must be registered in
  the phase-local `CLAIMS.md` and `docs/CLAIMS_INDEX.md`.

Source repositories
- Current phased repo: `/Users/dri/Documents/Projects/origin-axiom`
- Legacy repo: `/Users/dri/Documents/Projects/origin-axiom-legacy`

Phase 0 contract alignment
- P0-C01 (schema-governed artifacts): legacy artifacts are not corridor or
  filter JSONs, so no schema claims are made here.
- P0-C02 (corridor history): this doc does not alter corridor history.
- P0-C03 (claims taxonomy): proposed claim types are noted, but no claims are
  created here.
- P0-C04 (reproducibility): each candidate includes a reproducibility status
  and migration steps needed to become canonical.
- P0-C05 (provenance logs): every candidate points to legacy logs/notes.
- P0-C06 (archive policy): legacy content remains in the archive until promoted.
- P0-C07 (Phase 0 paper): no changes; this is a supporting governance index.

Migration candidates (with evidence pointers)

1) Theta-agnostic scalar vacuum sanity checks
- Summary: Validate linear dispersion, damping dephasing, and noise/coherence in
  a 1D Klein-Gordon vacuum prior to introducing any theta-dependent twist.
- Legacy scripts:
  - `../origin-axiom-legacy/src/scalar_vacuum_theta/run_1d_vacuum_dispersion.py`
  - `../origin-axiom-legacy/src/scalar_vacuum_theta/run_1d_vacuum_dephasing.py`
  - `../origin-axiom-legacy/src/scalar_vacuum_theta/run_1d_vacuum_noise_residue.py`
- Legacy outputs:
  - `../origin-axiom-legacy/data/processed/scalar_vacuum_theta/`
  - `../origin-axiom-legacy/figures/scalar_vacuum_theta/`
- Evidence logs:
  - `../origin-axiom-legacy/PROGRESS_LOG.md`
  - `../origin-axiom-legacy/verification_notes.md`
- Proposed phase: Phase 1 (toy-domain existence/robustness).
- Proposed claim type: existence/robustness of baseline dynamics only.
- Non-claim boundary: no theta_star inference, no cosmology/FRW claims.
- Reproducibility status: scripts are runnable; no Snakemake pipeline yet.
- Migration steps:
  1) Port scripts to a phase module (likely `phase1/src/`).
  2) Add a minimal pipeline step and canonical figures under
     `phase1/outputs/figures/`.
  3) Register a Phase 1 claim or non-claim note with evidence pointers.

2) 4D lattice delta_alpha(theta) scans
- Summary: theta-agnostic lattice sum scan showing a smooth curve and a
  numerically stable minimum near theta_star.
- Legacy scripts:
  - `../origin-axiom-legacy/src/lattice_theta/lattice_delta_alpha.py`
  - `../origin-axiom-legacy/src/lattice_theta/run_delta_alpha_theta_scan.py`
- Legacy outputs:
  - `../origin-axiom-legacy/data/processed/lattice_theta/`
  - `../origin-axiom-legacy/figures/lattice_theta/`
- Evidence logs:
  - `../origin-axiom-legacy/notes/lattice_theta_log.md`
  - `../origin-axiom-legacy/PROGRESS_LOG.md`
- Proposed phase: Phase 1 (toy-domain structural scan).
- Proposed claim type: existence of a smooth theta-dependent residue in a toy
  lattice sum.
- Non-claim boundary: no privileged physical theta_star, no global corridor
  update without Phase 0 ledger integration.
- Reproducibility status: scripts runnable; outputs not part of a phase pipeline.
- Migration steps:
  1) Port scripts and parameter sets into a phase pipeline.
  2) Promote selected figures to `phase1/outputs/figures/` with run metadata.
  3) Add a Phase 1 claim or documented non-claim depending on stability.

3) Cancellation chain residual scans (theta_star vs baseline and grids)
- Summary: residual scaling scans in a discrete cancellation chain toy model,
  including a theta_star run and a broader zero-sum grid.
- Legacy scripts:
  - `../origin-axiom-legacy/src/cancellation_system/run_chain_residual_scan.py`
  - `../origin-axiom-legacy/scripts/cancellation_system/`
- Legacy outputs:
  - `../origin-axiom-legacy/docs/results/cancellation_system/`
  - `../origin-axiom-legacy/figures/cancellation_system/`
- Evidence logs:
  - `../origin-axiom-legacy/notes/cancellation_system_log.md`
  - `../origin-axiom-legacy/docs/notes/act2_zero_sum_grid_20251213.md`
  - `../origin-axiom-legacy/PROGRESS_LOG.md`
- Proposed phase: Phase 1 (toy-domain residual scaling).
- Proposed claim type: existence/robustness of non-cancelling residual scaling.
- Non-claim boundary:
  - zero-sum grid indicates theta_star is not the minimizer in this toy model,
    so no uniqueness or preferred-theta claim is allowed here.
- Reproducibility status: per-run CSVs and plots exist; pipeline not integrated.
- Migration steps:
  1) Import both theta_star runs and the zero-sum grid as paired evidence.
  2) Preserve negative/contrast results alongside positive scans.
  3) Add an explicit non-claim note in Phase 1 claims.

4) Toy universe constraint comparisons and epsilon/lambda scan
- Summary: 3D scalar toy universe runs comparing constraint vs no constraint,
  plus epsilon/lambda activity scans.
- Legacy scripts:
  - `../origin-axiom-legacy/src/run_toy_universe_compare_constraint.py`
  - `../origin-axiom-legacy/src/run_toy_universe_compare_constraint_nonlinear.py`
  - `../origin-axiom-legacy/src/run_toy_universe_constraint_scan.py`
- Legacy outputs:
  - `../origin-axiom-legacy/data/processed/`
  - See `../origin-axiom-legacy/docs/REPRODUCING_FIGURES.md`
- Evidence logs:
  - `../origin-axiom-legacy/docs/SIMULATION_LOG.md`
  - `../origin-axiom-legacy/docs/REPRODUCING_FIGURES.md`
- Proposed phase: Phase 1 (toy-domain existence/robustness).
- Proposed claim type: constraint enforces a non-cancellation floor while
  preserving stable energy behavior in toy settings.
- Non-claim boundary: no claims about physical vacuum, cosmology, or theta_star.
- Reproducibility status: scripts and notebooks documented; no Snakemake pipeline.
- Migration steps:
  1) Port scripts/notebooks into phase workflow.
  2) Promote a minimal set of canonical figures.
  3) Register claims with explicit non-claim boundaries.

5) 1D twisted and defected vacuum null tests
- Summary: 1D twisted boundary scans (with and without defect) showing no
  measurable theta dependence in vacuum energy in the tested setup.
- Legacy scripts:
  - `../origin-axiom-legacy/src/run_1d_twisted_vacuum_scan.py`
  - `../origin-axiom-legacy/src/run_1d_defected_vacuum_scan.py`
- Legacy outputs:
  - `../origin-axiom-legacy/data/processed/`
  - `../origin-axiom-legacy/docs/REPRODUCING_FIGURES.md`
- Evidence logs:
  - `../origin-axiom-legacy/docs/SIMULATION_LOG.md`
- Proposed phase: Phase 1 (toy-domain null results).
- Proposed claim type: null result only.
- Non-claim boundary: does not rule out theta dependence in higher dimensions
  or non-quadratic models.
- Reproducibility status: scripts documented; no phase pipeline yet.
- Migration steps:
  1) Port runs into Phase 1 workflow.
  2) Register as a non-claim or negative result in Phase 1 ledger.

Optional, later-phase candidates (if needed)
- Effective vacuum band scan and patch ensemble:
  - `../origin-axiom-legacy/src/run_effective_vacuum_band_scan.py`
  - `../origin-axiom-legacy/src/run_effective_vacuum_patch_ensemble.py`
  - Proposed phase: Phase 2 (bounded viability preparation).
- FRW bridge scripts:
  - `../origin-axiom-legacy/src/run_frw_from_effective_vacuum.py`
  - `../origin-axiom-legacy/src/run_frw_observables_from_effective_vacuum.py`
  - Proposed phase: Phase 2 or Phase 4 depending on current scope.

Reproducibility and artifact policy (Phase 0 compatible)
- Legacy data under `../origin-axiom-legacy/data/processed/` is not canonical.
- Promotion requires:
  1) Canonical outputs under `phaseX/outputs/figures/`.
  2) Evidence pointers in `phaseX/CLAIMS.md` with explicit non-claim boundaries.
  3) A reproducible workflow (Snakemake or equivalent) documented in
     `phaseX/REPRODUCIBILITY.md`.
  4) Update to `docs/CLAIMS_INDEX.md` when claims are formalized.

Known gaps and risks
- Some legacy results rely on ad hoc scripts without pinned run metadata.
- Plots and CSVs are in legacy paths that are not governed by phase contracts.
- Negative results (for example, the zero-sum grid vs theta_star) must be
  explicitly preserved to avoid over-claiming.

Next steps (governance order)
1) Decide which candidates become Phase 1 claims vs Phase 1 non-claims.
2) Port minimal scripts and parameter sets into phase workflows.
3) Promote canonical figures and register evidence pointers.
4) Update phase claims and `docs/CLAIMS_INDEX.md` accordingly.
