# Stage 2 Endpoint Tables – Glossary v1

This document lists the main Stage 2 CSV endpoints (under `stage2/*/outputs/tables/`),
with their paths and column schemas.

Descriptions are intentionally minimal and **auto-inferred from filenames only**;
they are not new claims, just orientation. For precise semantics, the source
scripts in `stage2/*/src/` remain the ground truth.

---

## Module: `external_frw_host`

### `stage2/external_frw_host/outputs/tables/stage2_external_frw_host_age_anchor_mask_v1.csv`
- **Role (heuristic):** Auto-inferred from filename: stage2 external frw host age anchor mask v1
- **Columns (in order):**
  - `theta_index`, `theta`, `omega_lambda`, `age_Gyr_host`, `age_Gyr`, `frw_viable`, `in_host_age_anchor_window`

### `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung1_age_crosscheck_v1.csv`
- **Role (heuristic):** Auto-inferred from filename: external frw rung1 age crosscheck v1
- **Columns (in order):**
  - `theta_index`, `theta`, `omega_lambda`, `age_Gyr`, `age_Gyr_host`, `age_Gyr_diff`, `age_Gyr_rel_diff`, `frw_viable`

### `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung2_age_contrast_v1.csv`
- **Role (heuristic):** Auto-inferred from filename: external frw rung2 age contrast v1
- **Columns (in order):**
  - `set`, `n_theta`, `frac_of_grid`, `age_Gyr_diff_mean`, `age_Gyr_diff_std`, `age_Gyr_diff_min`, `age_Gyr_diff_max`, `age_Gyr_rel_diff_mean`, `age_Gyr_rel_diff_std`, `age_Gyr_rel_diff_min`, `age_Gyr_rel_diff_max`

### `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung3_age_consistency_mask_v1.csv`
- **Role (heuristic):** Auto-inferred from filename: external frw rung3 age consistency mask v1
- **Columns (in order):**
  - `theta_index`, `theta`, `omega_lambda`, `age_Gyr`, `age_Gyr_host`, `frw_viable`, `age_Gyr_rel_diff`, `age_consistent_rel_le_20pct`

### `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung4_age_window_summary_v1.csv`
- **Role (heuristic):** Auto-inferred from filename: external frw rung4 age window summary v1
- **Columns (in order):**
  - `set`, `n_theta`, `frac_of_grid`, `age_Gyr_host_mean`, `age_Gyr_host_std`, `age_Gyr_host_min`, `age_Gyr_host_max`, `age_Gyr_toy_mean`, `age_Gyr_toy_std`, `age_Gyr_toy_min`, `age_Gyr_toy_max`

### `stage2/external_frw_host/outputs/tables/stage2_external_frw_background_bridge_v1.csv`
- **Role (heuristic):** Auto-inferred from filename: external frw background bridge v1
- **Columns (in order):**
  - `theta_index`, `theta`, `omega_lambda`, `age_Gyr_host`, `age_Gyr_toy`, `frw_viable`

### `stage2/external_frw_host/outputs/tables/stage2_external_frw_host_anchor_mask_v1.csv`
- **Role (heuristic):** Auto-inferred from filename: external frw host anchor mask v1
- **Columns (in order):**
  - `theta_index`, `theta`, `omega_lambda`, `age_Gyr`, `age_Gyr_host`, `frw_viable`, `in_host_empirical_anchor_box`

### `stage2/external_frw_host/outputs/tables/stage2_external_frw_host_anchor_profiles_v1.csv`
- **Role (heuristic):** Auto-inferred from filename: external frw host anchor profiles v1
- **Columns (in order):**
  - `n_theta`, `theta_min`, `theta_max`, `omega_lambda_mean`, `omega_lambda_std`, `omega_lambda_min`, `omega_lambda_max`, `age_Gyr_host_mean`, `age_Gyr_host_std`, `age_Gyr_host_min`, `age_Gyr_host_max`, `age_Gyr_toy_mean`, `age_Gyr_toy_std`, `age_Gyr_toy_min`, `age_Gyr_toy_max`, `mech_baseline_A0_mean`, `mech_baseline_A0_std`, `mech_baseline_A0_min`, `mech_baseline_A0_max`, `mech_baseline_A_floor_mean`, `mech_baseline_A_floor_std`, `mech_baseline_A_floor_min`, `mech_baseline_A_floor_max`, `mech_binding_A0_mean`, `mech_binding_A0_std`, `mech_binding_A0_min`, `mech_binding_A0_max`, `mech_binding_A_mean`, `mech_binding_A_std`, `mech_binding_A_min`, `mech_binding_A_max`, `frac_in_toy_corridor`

### `stage2/external_frw_host/outputs/tables/stage2_external_frw_host_age_anchor_profiles_v1.csv`
- **Role (heuristic):** Auto-inferred from filename: external frw host age anchor profiles v1
- **Columns (in order):**
  - `n_theta`, `theta_min`, `theta_max`, `omega_lambda_mean`, `omega_lambda_std`, `omega_lambda_min`, `omega_lambda_max`, `age_Gyr_host_mean`, `age_Gyr_host_std`, `age_Gyr_host_min`, `age_Gyr_host_max`, `age_Gyr_toy_mean`, `age_Gyr_toy_std`, `age_Gyr_toy_min`, `age_Gyr_toy_max`, `mech_baseline_A0_mean`, `mech_baseline_A0_std`, `mech_baseline_A0_min`, `mech_baseline_A0_max`, `mech_baseline_A_floor_mean`, `mech_baseline_A_floor_std`, `mech_baseline_A_floor_min`, `mech_baseline_A_floor_max`, `mech_binding_A0_mean`, `mech_binding_A0_std`, `mech_binding_A0_min`, `mech_binding_A0_max`, `mech_binding_A_mean`, `mech_binding_A_std`, `mech_binding_A_min`, `mech_binding_A_max`, `frac_in_toy_corridor`

---

## Module: `frw_corridor_analysis`

### `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung1_sources_v1.csv`
- **Role (heuristic):** Auto-inferred from filename: frw corridor rung1 sources v1
- **Columns (in order):**
  - `section`, `path`, `kind`, `size_bytes`, `n_rows`, `n_cols`

### `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung2_bool_census_v1.csv`
- **Role (heuristic):** Auto-inferred from filename: frw corridor rung2 bool census v1
- **Columns (in order):**
  - `column`, `n_true`, `n_false`, `frac_true`, `frac_false`

### `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung3_families_v1.csv`
- **Role (heuristic):** Auto-inferred from filename: frw corridor rung3 families v1
- **Columns (in order):**
  - `family`, `mask_expr`, `n_theta`, `frac_of_grid`

### `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung4_family_overlap_v1.csv`
- **Role (heuristic):** Auto-inferred from filename: frw corridor rung4 family overlap v1
- **Columns (in order):**
  - `set`, `n_theta`, `frac_of_grid`

### `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung6_contiguity_v1.csv`
- **Role (heuristic):** Auto-inferred from filename: frw corridor rung6 contiguity v1
- **Columns (in order):**
  - `set`, `n_theta`, `frac_of_grid`, `n_segments`, `segment_lengths`, `theta_min`, `theta_max`

### `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung7_stride_robustness_v1.csv`
- **Role (heuristic):** Auto-inferred from filename: frw corridor rung7 stride robustness v1
- **Columns (in order):**
  - `set`, `stride`, `n_theta`, `frac_of_grid`, `n_segments`, `segment_lengths`, `theta_min`, `theta_max`

### `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung8_smoothing_v1.csv`
- **Role (heuristic):** Auto-inferred from filename: frw corridor rung8 smoothing v1
- **Columns (in order):**
  - `set`, `window`, `n_theta`, `frac_of_grid`, `n_segments`, `segment_lengths`, `theta_min`, `theta_max`

### `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung9_segments_v1.csv`
- **Role (heuristic):** Auto-inferred from filename: frw corridor rung9 segments v1
- **Columns (in order):**
  - `segment_id`, `theta_index_start`, `theta_index_end`, `n_theta`, `theta_min`, `theta_max`

### `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung9_theta_star_alignment_v1.csv`
- **Role (heuristic):** Auto-inferred from filename: frw corridor rung9 theta star alignment v1
- **Columns (in order):**
  - `segment_id`, `theta_index_start`, `theta_index_end`, `n_theta`, `theta_min`, `theta_max`, `contains_theta_star`, `theta_star`, `min_abs_delta`, `theta_at_min_abs_delta`

---

## Module: `frw_data_probe_analysis`

### `stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_data_probe_rung1_column_stats_v1.csv`
- **Role (heuristic):** Auto-inferred from filename: frw data probe rung1 column stats v1
- **Columns (in order):**
  - `column`, `n_true`, `n_false`, `frac_true`, `frac_false`, `note`

### `stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_empirical_anchor_mask_v1.csv`
- **Role (heuristic):** Auto-inferred from filename: frw empirical anchor mask v1
- **Columns (in order):**
  - `theta_index`, `theta`, `omega_lambda`, `age_Gyr`, `in_empirical_anchor_box`

---

## Module: `joint_mech_frw_analysis`

### `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv`
- **Role (heuristic):** Auto-inferred from filename: joint theta grid v1
- **Columns (in order):**
  - `theta_index`, `theta`, `E_vac`, `omega_lambda`, `age_Gyr`, `in_toy_corridor`, `frw_viable`, `lcdm_like`, `shape_and_viable`, `shape_and_lcdm`, `frw_data_ok`, `mech_baseline_A0`, `mech_baseline_A_floor`, `mech_baseline_bound`, `mech_binding_A0`, `mech_binding_A`, `mech_binding_bound`

### `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_intersections_v1.csv`
- **Role (heuristic):** Auto-inferred from filename: joint mech frw anchor intersections v1
- **Columns (in order):**
  - `set`, `n_theta`, `frac_of_grid`

### `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_kernel_v1.csv`
- **Role (heuristic):** Auto-inferred from filename: joint mech frw anchor kernel v1
- **Columns (in order):**
  - `segment_id`, `theta_index_start`, `theta_index_end`, `n_theta`, `theta_min`, `theta_max`, `contains_theta_star`, `theta_star`, `min_abs_delta`, `theta_at_min_abs_delta`

### `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_profiles_v1.csv`
- **Role (heuristic):** Auto-inferred from filename: joint mech frw anchor profiles v1
- **Columns (in order):**
  - `set`, `n_theta`, `frac_of_grid`, `E_vac__mean`, `E_vac__std`, `E_vac__min`, `E_vac__max`, `omega_lambda__mean`, `omega_lambda__std`, `omega_lambda__min`, `omega_lambda__max`, `age_Gyr__mean`, `age_Gyr__std`, `age_Gyr__min`, `age_Gyr__max`, `mech_baseline_A0__mean`, `mech_baseline_A0__std`, `mech_baseline_A0__min`, `mech_baseline_A0__max`, `mech_baseline_A_floor__mean`, `mech_baseline_A_floor__std`, `mech_baseline_A_floor__min`, `mech_baseline_A_floor__max`, `mech_baseline_bound__mean`, `mech_baseline_bound__std`, `mech_baseline_bound__min`, `mech_baseline_bound__max`, `mech_binding_A0__mean`, `mech_binding_A0__std`, `mech_binding_A0__min`, `mech_binding_A0__max`, `mech_binding_A__mean`, `mech_binding_A__std`, `mech_binding_A__min`, `mech_binding_A__max`, `mech_binding_bound__mean`, `mech_binding_bound__std`, `mech_binding_bound__min`, `mech_binding_bound__max`

### `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_sensitivity_v1.csv`
- **Role (heuristic):** Auto-inferred from filename: joint mech frw anchor sensitivity v1
- **Columns (in order):**
  - `scale`, `omega_lambda_min`, `omega_lambda_max`, `age_Gyr_min`, `age_Gyr_max`, `n_in_box`, `n_box_and_frw_viable`, `n_box_and_corridor`, `n_box_and_corridor_and_frw_viable`

### `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_mech_contrast_v1.csv`
- **Role (heuristic):** Auto-inferred from filename: joint mech frw anchor mech contrast v1
- **Columns (in order):**
  - `set`, `mech_column`, `n_theta`, `frac_of_grid`, `mean`, `std`, `min`, `max`

### `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_host_corridor_summary_v1.csv`
- **Role (heuristic):** Auto-inferred from filename: joint mech frw host corridor summary v1
- **Columns (in order):**
  - `set`, `n_theta`, `frac_of_grid`

### `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_host_anchor_intersections_v1.csv`
- **Role (heuristic):** Auto-inferred from filename: joint mech frw host anchor intersections v1
- **Columns (in order):**
  - `set`, `n_theta`, `frac_of_grid`

### `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_host_age_anchor_intersections_v1.csv`
- **Role (heuristic):** Auto-inferred from filename: joint mech frw host age anchor intersections v1
- **Columns (in order):**
  - `set`, `n_theta`, `frac_of_grid`

---

## Module: `mech_measure_analysis`

### `stage2/mech_measure_analysis/outputs/tables/stage2_mech_rung1_phase3_table_inventory_v1.csv`
- **Role (heuristic):** Auto-inferred from filename: mech rung1 phase3 table inventory v1
- **Columns (in order):**
  - `path`, `kind`, `size_bytes`, `n_rows`, `n_cols`

### `stage2/mech_measure_analysis/outputs/tables/stage2_mech_rung2_phase3_measure_summary_v1.csv`
- **Role (heuristic):** Auto-inferred from filename: mech rung2 phase3 measure summary v1
- **Columns (in order):**
  - `column`, `mean`, `std`, `min`, `max`, `p5`, `p50`, `p95`

### `stage2/mech_measure_analysis/outputs/tables/stage2_mech_rung3_mech_vs_vacuum_correlation_v1.csv`
- **Role (heuristic):** Auto-inferred from filename: mech rung3 mech vs vacuum correlation v1
- **Columns (in order):**
  - `subset`, `x_column`, `y_column`, `pearson_r`, `n`, `note`

### `stage2/mech_measure_analysis/outputs/tables/stage2_mech_rung4_mech_vs_frw_correlation_v1.csv`
- **Role (heuristic):** Auto-inferred from filename: mech rung4 mech vs frw correlation v1
- **Columns (in order):**
  - `subset`, `x_column`, `y_column`, `pearson_r`, `n`, `note`

### `stage2/mech_measure_analysis/outputs/tables/stage2_mech_rung5_mech_vs_anchor_correlation_v1.csv`
- **Role (heuristic):** Auto-inferred from filename: mech rung5 mech vs anchor correlation v1
- **Columns (in order):**
  - `subset`, `x_column`, `y_column`, `pearson_r`, `n`, `note`

### `stage2/mech_measure_analysis/outputs/tables/stage2_mech_rung7_theta_gradients_v1.csv`
- **Role (heuristic):** Auto-inferred from filename: mech rung7 theta gradients v1
- **Columns (in order):**
  - `set`, `mech_column`, `n_theta`, `frac_of_grid`, `grad_mean`, `grad_std`, `grad_min`, `grad_max`, `abs_grad_mean`, `abs_grad_p95`, `abs_grad_max`

