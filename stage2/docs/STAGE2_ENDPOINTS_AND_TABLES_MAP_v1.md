# Stage 2 – Endpoints and Tables Map (v1)

This memo is a **glossary of Stage 2 endpoints**: key CSV tables, their locations, and their roles.  
Goal: make it easy for humans (and AI) to navigate the Stage 2 layer without guessing filenames or column names.

It focuses on:

- FRW corridor analysis
- FRW data probes and empirical anchor
- Mechanism / measure analysis
- Joint mech–FRW grid and intersections
- External FRW host cross-checks

Phase-level contracts (Phase 0–4) and the Stage 2 code audit / design memos remain the **source of truth** for scope and claims.

---

## 1. FRW corridor analysis

**Folder:**  
`stage2/frw_corridor_analysis/outputs/tables/`

These tables start from Phase 4 FRW masks and build structured θ-families and corridors.

- `stage2_frw_corridor_rung1_sources_v1.csv`
  - **Role:** Inventory of FRW source tables and basic metadata.
  - **Key columns:**
    - `source_name` – e.g. `frw_viability_mask`, `frw_shape_probe_mask`, ...
    - `path` – path to the Phase 4 input table.
    - `n_rows`, `n_cols`, `size_bytes`.
  - **Use:** sanity check that Phase 4 FRW sources exist and have expected shapes.

- `stage2_frw_corridor_rung2_bool_census_v1.csv`
  - **Role:** Census of boolean FRW masks over the θ grid.
  - **Key columns:**
    - `mask_name` – e.g. `frw_viable`, `lcdm_like`, `toy_corridor`, ...
    - `n_true`, `n_false`, `frac_true`, `frac_false`.
  - **Use:** quick overview of how restrictive each FRW mask is.

- `stage2_frw_corridor_rung3_families_v1.csv`
  - **Role:** Definition of **families** of θ based on masks.
  - **Key columns:**
    - `family` – e.g. `ALL_GRID`, `FRW_VIABLE`, `LCDM_LIKE`, `TOY_CORRIDOR`, ...
    - `n_theta`, `frac_of_grid`.
  - **Use:** canonical labels for θ-families used across Stage 2.

- `stage2_frw_corridor_rung4_family_overlap_v1.csv`
  - **Role:** Overlaps between families.
  - **Key columns:**
    - `family_A`, `family_B`
    - `n_overlap`, `frac_of_grid`.
  - **Use:** see how FRW_viable, toy corridor, etc., intersect.

- `stage2_frw_corridor_rung6_contiguity_v1.csv`
  - **Role:** Contiguity diagnostics.
  - **Key columns:**
    - `family`
    - `n_segments` – number of contiguous θ-index segments.
    - `segment_lengths_stats` (aggregated).
  - **Use:** distinguish corridors from isolated “needles” in θ.

- `stage2_frw_corridor_rung7_stride_robustness_v1.csv`
  - **Role:** Downsampling robustness (stride tests).
  - **Key columns:**
    - `family`, `stride`
    - `n_theta`, `n_segments`, `frac_of_grid`.
  - **Use:** stability of corridors under coarser sampling.

- `stage2_frw_corridor_rung8_smoothing_v1.csv`
  - **Role:** Smoothing robustness.
  - **Key columns:**
    - `family`, `window_size`
    - `smoothed_n_theta`, `smoothed_n_segments`.
  - **Use:** check whether corridors survive simple smoothing.

- `stage2_frw_corridor_rung9_segments_v1.csv`
  - **Role:** Explicit corridor segments.
  - **Key columns:**
    - `family`
    - `segment_id`
    - `theta_index_start`, `theta_index_end`
    - `theta_min`, `theta_max`
    - `n_theta`.
  - **Use:** concrete segments for downstream analysis.

- `stage2_frw_corridor_rung9_theta_star_alignment_v1.csv`
  - **Role:** Alignment of θ★ with each family’s segments.
  - **Key columns:**
    - `family`, `segment_id`
    - `contains_theta_star` (bool)
    - `min_abs_delta_theta_star` – distance from θ★ to closest point in segment.
  - **Use:** quantify how θ★ sits relative to corridors.

---

## 2. FRW data probes + empirical anchor

**Folder:**  
`stage2/frw_data_probe_analysis/`

### 2.1 Config

- `config/empirical_anchor_box_v1.json`
  - **Role:** Definition of the empirical anchor box in FRW toy space.
  - **Typical keys:**
    - `omega_lambda_center`, `omega_lambda_half_width`
    - `age_Gyr_center`, `age_Gyr_half_width`
  - **Use:** defines a small 2D box in (ω_Λ, age_Gyr) used as the **empirical anchor** in FRW toy space.

### 2.2 Outputs

- `outputs/tables/stage2_frw_data_probe_rung1_column_stats_v1.csv`
  - **Role:** Stats over FRW data-probe masks (from Phase 4).
  - **Key columns:**
    - `column` – `has_matter_era`, `has_late_accel`, `smooth_H2`, `frw_viable`, `data_ok`, ...
    - `n_true`, `n_false`, `frac_true`, `frac_false`, `note`.
  - **Use:** check which probes bite and how strongly.

- `outputs/tables/stage2_frw_empirical_anchor_mask_v1.csv`
  - **Role:** FRW-side empirical anchor mask table.
  - **Key columns:**
    - `theta`
    - `omega_lambda`
    - `age_Gyr`
    - `in_empirical_anchor_box` – bool, based on the config box.
  - **Use:** identify θ-points inside the FRW empirical anchor box.

---

## 3. Mechanism / measure analysis

**Folder:**  
`stage2/mech_measure_analysis/outputs/tables/`

- `stage2_mech_rung1_phase3_table_inventory_v1.csv`
  - **Role:** Inventory of Phase 3 mechanism tables.
  - **Key columns:**
    - `path`, `kind` (`csv` / `json`), `size_bytes`, `n_rows`, `n_cols`.
  - **Use:** quick overview and health-check of Phase 3 outputs.

- `stage2_mech_rung2_mech_stats_v1.csv`
  - **Role:** Global stats of mechanism measures across the θ grid.
  - **Key columns:**
    - `mech_column` – `mech_baseline_A0`, `mech_baseline_A_floor`, `mech_baseline_bound`, `mech_binding_A0`, `mech_binding_A`, `mech_binding_bound`.
    - `n_theta`, `mean`, `std`, `min`, `max`.
  - **Use:** understand the range and behaviour of mechanism measures.

- `stage2_mech_rung3_mech_vs_frw_corr_v1.csv`
  - **Role:** Correlations between mechanism measures and FRW quantities.
  - **Key columns:**
    - `pair` – e.g. `E_vac_vs_mech_baseline_A0`, `omega_lambda_vs_mech_binding_A`, ...
    - `pearson_r`
    - `subset` – `ALL_GRID`, `FRW_VIABLE`, `TOY_CORRIDOR`, etc.
  - **Use:** quantify alignment/misalignment between mechanism and FRW outputs.

- `stage2_mech_rung7_theta_gradients_v1.csv`
  - **Role:** θ-gradients of mechanism measures on different subsets.
  - **Key columns:**
    - `set` – `ALL_GRID`, `FRW_VIABLE`, `TOY_CORRIDOR`, `CORRIDOR_AND_VIABLE`, `CORRIDOR_AND_VIABLE_AND_ANCHOR`.
    - `mech_column`
    - `n_theta`, `frac_of_grid`
    - `grad_mean`, `grad_std`, `grad_min`, `grad_max`
    - `abs_grad_mean`, `abs_grad_p95`, `abs_grad_max`.
  - **Use:** see how “steep” or flat mechanism measures are across different θ families, especially in the empirical anchor.

---

## 4. Joint mech–FRW grid and intersections

**Folder:**  
`stage2/joint_mech_frw_analysis/outputs/tables/`

### 4.1 Core joint grid

- `stage2_joint_theta_grid_v1.csv`
  - **Role:** Central hub table aligning mechanism and FRW toy outputs.
  - **Key columns (subset):**
    - `theta_index`, `theta`
    - `E_vac`, `omega_lambda`, `age_Gyr`
    - FRW masks: `in_toy_corridor`, `frw_viable`, `lcdm_like`, `shape_and_viable`, `shape_and_lcdm`, `frw_data_ok`
    - Mechanism measures: `mech_baseline_*`, `mech_binding_*`
  - **Use:** everything else in Stage 2 joins back to this grid.

### 4.2 Empirical anchor intersection tables

- `stage2_joint_mech_frw_anchor_intersections_v1.csv`
  - **Role:** Set counts for empirical anchor intersections (FRW toy side).
  - **Key columns:**
    - `set` – `ALL_GRID`, `FRW_VIABLE`, `TOY_CORRIDOR`, `EMPIRICAL_ANCHOR`, `FRW_VIABLE_AND_ANCHOR`, `CORRIDOR_AND_ANCHOR`, `CORRIDOR_AND_VIABLE_AND_ANCHOR`.
    - `n_theta`, `frac_of_grid`.
  - **Use:** global picture of how rare the empirical anchor is, and how it intersects FRW viability and the toy corridor.

- `stage2_joint_mech_frw_anchor_kernel_v1.csv`
  - **Role:** Contiguous segments of the **anchor kernel** (FRW_viable ∧ toy_corridor ∧ empirical_anchor).
  - **Key columns:**
    - `segment_id`
    - `theta_index_start`, `theta_index_end`
    - `theta_min`, `theta_max`
    - `n_theta`
    - `contains_theta_star`
    - `min_abs_delta_theta_star`
  - **Use:** structure of the empirical anchor kernel in θ.

- `stage2_joint_mech_frw_anchor_profiles_v1.csv`
  - **Role:** Aggregate profiles of FRW and mechanism quantities on different sets.
  - **Key columns:**
    - `set` – same labels as above.
    - `n_theta`, `frac_of_grid`
    - `E_vac__mean/std/min/max`
    - `omega_lambda__mean/std/min/max`
    - `age_Gyr__mean/std/min/max`
    - `mech_*__mean/std/min/max` (for each mechanism measure).
  - **Use:** comparative “fingerprints” of the anchor vs corridor vs full grid.

- `stage2_joint_mech_frw_anchor_sensitivity_v1.csv`
  - **Role:** Sensitivity of anchor counts to scaling the empirical box.
  - **Key columns:**
    - `scale` – e.g. 0.5, 1.0, 1.5
    - `n_in_box`
    - `n_box_and_frw_viable`
    - `n_box_and_corridor`
    - `n_box_and_corridor_and_frw_viable`.
  - **Use:** robustness of the anchor to modest box inflations/shrinkages.

- `stage2_joint_mech_frw_anchor_mech_contrast_v1.csv`
  - **Role:** Mechanism contrasts between anchor and non-anchor regions.
  - **Key columns:**
    - `set` – `ALL_GRID`, `FRW_VIABLE`, `CORRIDOR_AND_VIABLE`, `CORRIDOR_AND_VIABLE_AND_ANCHOR`, `CORRIDOR_AND_VIABLE_NOT_ANCHOR`.
    - `mech_column`
    - `n_theta`, `frac_of_grid`
    - `mean`, `std`, `min`, `max`.
  - **Use:** compare mechanism amplitudes on the anchor vs the surrounding corridor.

### 4.3 Host-guided corridor summary

- `stage2_joint_mech_frw_host_corridor_summary_v1.csv`
  - **Role:** High-level summary of host-calibrated corridor and its intersections.
  - **Key columns:**
    - `set` – `ALL_GRID`, `FRW_VIABLE`, `TOY_CORRIDOR`, `HOST_CALIBRATED_CORRIDOR`, `HOST_CORRIDOR_AND_ANCHOR`, etc.
    - `n_theta`, `frac_of_grid`.
  - **Use:** see how big the host age-consistent corridor is, and whether it intersects the empirical anchor.

- `stage2_joint_mech_frw_host_anchor_intersections_v1.csv`
  - **Role:** Same as anchor intersections, but for the **host-side anchor**.
  - **Key columns:**
    - `set` – `ALL_GRID`, `FRW_VIABLE`, `TOY_CORRIDOR`, `HOST_ANCHOR`, `FRW_VIABLE_AND_HOST_ANCHOR`, `CORRIDOR_AND_HOST_ANCHOR`, `CORRIDOR_AND_VIABLE_AND_HOST_ANCHOR`.
    - `n_theta`, `frac_of_grid`.
  - **Use:** check consistency between FRW toy anchor and host anchor behaviour.

---

## 5. External FRW host cross-checks

**Folder:**  
`stage2/external_frw_host/outputs/tables/`

- `stage2_external_frw_rung1_age_crosscheck_v1.csv`
  - **Role:** Pointwise toy vs host age comparison.
  - **Key columns:**
    - `theta_index`, `theta`
    - `omega_lambda`
    - `age_Gyr` – Phase 4 toy age
    - `age_Gyr_host` – analytic host FRW age
    - `age_Gyr_diff` – host − toy
    - `age_Gyr_rel_diff` – relative difference
    - `frw_viable`.
  - **Use:** raw material for age-contrast diagnostics and age-consistency masks.

- `stage2_external_frw_rung2_age_contrast_v1.csv`
  - **Role:** Aggregate age-contrast stats on key sets.
  - **Key columns:**
    - `set` – `ALL_GRID`, `FRW_VIABLE`, `CORRIDOR_AND_VIABLE`, `CORRIDOR_AND_VIABLE_AND_ANCHOR`.
    - `n_theta`, `frac_of_grid`
    - `age_Gyr_diff_mean/std/min/max`
    - `age_Gyr_rel_diff_mean/std/min/max`.
  - **Use:** how far toy ages are from host ages on each subset.

- `stage2_external_frw_rung3_age_consistency_mask_v1.csv`
  - **Role:** Host age-consistency mask.
  - **Key columns (subset):**
    - `theta_index`, `theta`
    - `omega_lambda`, `age_Gyr`, `age_Gyr_host`
    - `age_Gyr_rel_diff`
    - `age_consistent_rel_le_20pct` – bool.
  - **Use:** define a **host-calibrated corridor**: FRW-viable points with ≤ 20% relative age discrepancy.

- `stage2_external_frw_host_anchor_mask_v1.csv`
  - **Role:** Host-side empirical anchor mask.
  - **Key columns:**
    - `theta_index`, `theta`
    - `omega_lambda`
    - `age_Gyr`, `age_Gyr_host`
    - `frw_viable`
    - `in_host_empirical_anchor_box` – bool.
  - **Use:** mirror of the FRW toy empirical anchor in host coordinates.

---

## 6. How to use this map

- When adding a new Stage 2 table:
  - add a short entry here with:
    - path,
    - role,
    - key columns,
    - intended use.
- When writing new analysis scripts:
  - prefer **re-using** these tables rather than rolling ad hoc CSVs,
  - use the column names spelled exactly as in this map.

This document is allowed to **grow**, but not to silently rename existing endpoints. Any renaming must be:

1. implemented in code,
2. logged in `PROGRESS_LOG.md`, and
3. reflected here with clear “old → new” notes.

