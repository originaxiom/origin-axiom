# Phase 5 FRW–Host Dashboard Sketch (F1 baseline, Stage 2 / Phase 4 bridge)

**Status:** design-only sketch, no Phase 5 code yet.  
**Scope:** describe the panels and inputs that a Phase 5 “FRW–host dashboard” would assemble from the *current* Stage 2 and Phase 4 artifacts, using the tagged checkpoint  
`stage2_phase4_F1_FRW_baseline_checkpoint_2026-01-15`.

This is intentionally conservative: it does **not** assume that Phase 5 will
succeed or that θ★ is unique. It only specifies how Phase 5 should *read and
display* the information that is already locked in at this checkpoint.

---

## 1. Inputs from Phase 4 (F1 baseline)

Phase 5 should treat the following Phase 4 products as **read-only inputs**:

- FRW F1 sanity curve:
  - `phase4/outputs/tables/phase4_F1_sanity_curve.csv`
- FRW viability diagnostics + mask:
  - `phase4/outputs/tables/phase4_F1_frw_viability_diagnostics.json`
  - `phase4/outputs/tables/phase4_F1_frw_viability_mask.csv`
- FRW shape corridor diagnostics + mask:
  - `phase4/outputs/tables/phase4_F1_shape_diagnostics.json`
  - `phase4/outputs/tables/phase4_F1_shape_mask.csv`
- ΛCDM-like FRW probe:
  - `phase4/outputs/tables/phase4_F1_frw_lcdm_probe.json`
  - `phase4/outputs/tables/phase4_F1_frw_lcdm_probe_mask.csv`
- FRW data-probe stub (presently “no data”):
  - `phase4/outputs/tables/phase4_F1_frw_data_probe.json`
  - `phase4/outputs/tables/phase4_F1_frw_data_probe_mask.csv`
- Phase 4 external host kernel table (paper-ready):
  - `phase4/outputs/tables/phase4_external_host_kernel_constraints_v1.tex`
- Phase 4 documentation:
  - `phase4/docs/PHASE4_EXTERNAL_HOST_KERNEL_BRIDGE_v1.md`
  - `phase4/docs/PHASE4_FRW_F1_BASELINE_CHECKPOINT_v1.md`

Phase 5 is **not** allowed to silently change these; it can only re-read them,
replot them, or derive *explicitly logged* secondary summaries.

---

## 2. Inputs from Stage 2 external host analysis

Phase 5 also needs the Stage 2 external-host outputs that were used to build
the Phase 4 host kernel:

- External-cosmo host parameter grid:
  - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_params_grid_v1.csv`
- External host FRW-age background grid:
  - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_background_grid_v1.csv`
- External host age-anchor + corridor kernel:
  - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_age_anchor_corridor_kernel_v1.csv`
- Near-flat subset mask + summary:
  - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_flat_subset_mask_v1.csv`
  - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_flat_subset_summary_v1.csv`
- FRW vs host kernel comparison:
  - `stage2/external_cosmo_host/outputs/tables/stage2_external_host_kernel_comparison_v1.csv`
- External-host Phase 4 constraints (12-point kernel summary):
  - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_phase4_constraints_v1.csv`
- Omega-naming sanity scan (for future robustness):
  - `stage2/external_cosmo_host/outputs/tables/stage2_external_host_omega_naming_scan_v1.csv`

Again, Phase 5 may *consume* these tables but not overwrite them.

---

## 3. Dashboard concept: panels and questions

The Phase 5 FRW–host dashboard is meant as a **single place** where we can see:

- how the F1 FRW viability band behaves across θ,
- how the FRW ΛCDM-like window sits inside that viability band,
- how the external host kernel (12-point corridor) threads through both,
- how much of the *near-flat* external host subset actually participates,
- and where future real data (FRW distances, host catalogs) would plug in.

A minimal dashboard should have **four conceptual panels**:

1. **Panel A: FRW viability + ΛCDM-like window (Phase 4 only)**  
   - x-axis: θ.  
   - overplot:
     - FRW viability band (mask from `phase4_F1_frw_viability_mask.csv`),
     - ΛCDM-like subset (mask from `phase4_F1_frw_lcdm_probe_mask.csv`),
     - optional shading for the F1 shape corridor (`phase4_F1_shape_mask.csv`).  
   - Question it answers:  
     “For this F1 mapping, where in θ do we have a smooth matter era,
      late acceleration, and a ΛCDM-like age/ΩΛ window?”

2. **Panel B: External host kernel vs FRW bands**  
   - x-axis: θ (restricted to the 12-point host kernel).  
   - overplot:
     - host kernel θ positions (from `stage2_external_cosmo_host_age_anchor_corridor_kernel_v1.csv`),
     - FRW ΛCDM-like mask at those θ values (join with `phase4_F1_frw_lcdm_probe_mask.csv`),
     - markers or bars showing host vs repo age ranges and ΩΛ bands
       (from `stage2_external_cosmo_host_phase4_constraints_v1.csv`).  
   - Question it answers:  
     “Does the external host corridor sit *inside* the FRW ΛCDM-like window,
      and if so, how tightly in θ and in age?”

3. **Panel C: Near-flat external host subset**  
   - x-axis: Ω_tot or ΩΛ_host; y-axis: age or θ.  
   - uses:
     - `stage2_external_cosmo_flat_subset_mask_v1.csv`,
     - `stage2_external_cosmo_flat_subset_summary_v1.csv`.  
   - overlay the 12 host-kernel points and highlight which of them are FRW-viable
     and ΛCDM-like.  
   - Question it answers:  
     “Within all near-flat external cosmologies, how special is the corridor
      that participates in the FRW + F1 + host kernel intersection?”

4. **Panel D: Data-probe slot (currently stubbed)**  
   - present, but clearly labeled as a **placeholder** until a real binned FRW
     distance dataset is provided at  
     `phase4/data/external/frw_distance_binned.csv`.  
   - dashboard should read `phase4_F1_frw_data_probe.json` and explicitly show:
     - `data_available = false`,
     - `n_data_points = 0`,
     - `n_data_ok = 0`.  
   - Question it answers (in future):  
     “When real FRW distance data is provided, does the F1 FRW + host kernel
      intersection survive χ² constraints?”

---

## 4. Reuse protocol for this checkpoint (Phase 5 view)

For any future Phase 5 experiment that starts from this checkpoint, the minimum
**reproducibility contract** is:

1. **Rebuild the Phase 4 F1 baseline**  
   - Run the full F1 FRW pipeline:
     - `oa && python phase4/src/phase4/run_f1_sanity.py`
     - `oa && python phase4/src/phase4/run_f1_shape_diagnostics.py`
     - `oa && python phase4/src/phase4/run_f1_frw_toy_diagnostics.py`
     - `oa && python phase4/src/phase4/run_f1_frw_corridors.py`
     - `oa && python phase4/src/phase4/run_f1_frw_lcdm_probe.py`
     - `oa && python phase4/src/phase4/run_f1_frw_data_probe.py`
   - Confirm that the key JSON diagnostics
     (`phase4_F1_frw_viability_diagnostics.json`,
      `phase4_F1_frw_lcdm_probe.json`,
      `phase4_F1_frw_shape_probe.json`) match the checkpointed bands
     within numerical tolerance.

2. **Rebuild the Stage 2 external host kernel**  
   - Re-run the relevant Stage 2 scripts (exact commands are documented in  
     `stage2/docs/STAGE2_EXTERNAL_COSMO_HOSTS_DESIGN_v1.md` and
     `phase4/docs/PHASE4_EXTERNAL_HOST_KERNEL_BRIDGE_v1.md`), ending with:
     - `stage2_external_cosmo_host_age_anchor_corridor_kernel_v1.csv`
     - `stage2_external_cosmo_host_phase4_constraints_v1.csv`
     - `stage2_external_cosmo_flat_subset_mask_v1.csv`
     - `stage2_external_cosmo_flat_subset_summary_v1.csv`
     - `stage2_external_host_kernel_comparison_v1.csv`
   - Check that the 12-point kernel and its ΩΛ/age bands agree with the
     checkpointed values.

3. **Confirm the tagged baseline**  
   - Verify that the repo is at (or derived from) tag  
     `stage2_phase4_F1_FRW_baseline_checkpoint_2026-01-15`, or that any
     deviations are explicitly logged in `PROGRESS_LOG.md`.

Only after these checks pass should Phase 5 be allowed to ingest the inputs and
construct additional statistics or visualizations.

---

## 5. Out-of-scope for this sketch

This document intentionally does **not**:

- define a Phase 5 claim about uniqueness or existence of θ★,
- introduce any new priors, likelihoods, or data beyond the existing stubs,
- modify Stage 2 or Phase 4 artifacts,
- promise that the host kernel or FRW window will survive stricter probes.

Its only role is to give Phase 5 a clean, contract-respecting *view* of what
has already been established by Stage 2 and Phase 4 at this checkpoint.
