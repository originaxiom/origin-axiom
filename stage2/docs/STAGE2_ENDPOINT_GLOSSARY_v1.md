# Stage 2 Endpoint Glossary (v1, 2026-01-13)

This glossary records the **canonical CSV endpoints and column names** used in Stage 2 analyses, so that:

- humans and tools can avoid mistyping or guessing column names;
- joins between tables are unambiguous;
- future scripts can be written against a stable “API surface”.

If a column name or CSV path changes in the future, this file **must** be updated in the same commit.

---

## 0. Conventions and join keys

- **θ-grid size:** all Stage 2 belts referenced here operate on a **2048-point** θ-grid.
- **Primary coordinate columns:**
  - `theta_index` – integer index in the canonical θ-grid, 0…2047.
  - `theta` – floating-point θ value (radians), same across all θ-grid-based tables.
- **Standard join keys:**
  - For θ-grid tables:  
    - preferred join: `theta`  
    - optional join: `theta_index` (used where explicitly noted).
- **Boolean mask convention:**
  - All mask columns are `0/1` or `False/True` and should be treated as booleans in analysis code.

---

## 1. Core θ-grid endpoint

### 1.1 `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv`

One row per θ-point, combining Phase 3 mechanism outputs and Phase 4 FRW toy outputs.

| Column name              | Type    | Meaning |
|--------------------------|---------|---------|
| `theta_index`            | int     | Index of θ in the canonical 2048-point grid. |
| `theta`                  | float   | θ value (radians) for this grid point. |
| `E_vac`                  | float   | Vacuum energy scale from the mechanism side (Phase 3 → Phase 4 bridge). |
| `omega_lambda`           | float   | Effective Ω\_Λ-like parameter in the toy FRW background at this θ. |
| `age_Gyr`                | float   | Toy FRW age of the universe in Gyr (Phase 4 background integrator). |
| `in_toy_corridor`        | bool    | Corridor membership: 1 if θ lies in the FRW “toy corridor” family; 0 otherwise. |
| `frw_viable`             | bool    | FRW viability mask (e.g., Big Bang exists, matter era, late acceleration, sane background). |
| `lcdm_like`              | bool    | Mask for ΛCDM-like subset of FRW outputs. |
| `shape_and_viable`       | bool    | Mask where both “shape” and “viability” criteria hold. |
| `shape_and_lcdm`         | bool    | Mask where both “shape” and “ΛCDM-like” criteria hold. |
| `frw_data_ok`            | bool    | Toy “data_ok” FRW data-probe flag (currently always false across grid in this rung). |
| `mech_baseline_A0`       | float   | Baseline mechanism A-value (A₀) for this θ, before flooring/binding. |
| `mech_baseline_A_floor`  | float   | Floored baseline A-value at this θ. |
| `mech_baseline_bound`    | float   | Baseline bound flag / weight (in current pipelines this is 0 or 1). |
| `mech_binding_A0`        | float   | Binding-mechanism A₀ for this θ (binding scan). |
| `mech_binding_A`         | float   | Binding-mechanism A after any transformation/flooring. |
| `mech_binding_bound`     | float   | Binding-bound flag / weight (0 or 1). |

This table is the **primary join hub** for Stage 2: all subsequent masks and host diagnostics are attached to this grid.

---

## 2. FRW corridor analysis endpoints

These live under `stage2/frw_corridor_analysis/outputs/tables/`. Only key columns are listed; many rungs share the same base columns: `theta_index`, `theta`, FRW masks.

### 2.1 `stage2_frw_corridor_rung1_sources_v1.csv`

Sources and basic metadata for Phase 4 FRW masks.

| Column name   | Type  | Meaning |
|---------------|-------|---------|
| `source_name` | str   | Identifier of source table (e.g. FRW masks). |
| `path`        | str   | Path to the source CSV within the repo. |
| `n_rows`      | int   | Number of rows. |
| `n_cols`      | int   | Number of columns. |
| `note`        | str   | Short description of the source. |

### 2.2 `stage2_frw_corridor_rung2_bool_census_v1.csv`

Boolean census over FRW masks.

| Column name | Type | Meaning |
|-------------|------|---------|
| `mask_name` | str  | Name of boolean mask (e.g. `frw_viable`, `lcdm_like`, etc.). |
| `n_true`    | int  | Number of grid points where mask is true. |
| `n_false`   | int  | Number of grid points where mask is false. |
| `frac_true` | float| Fraction of grid with mask true. |

### 2.3 `stage2_frw_corridor_rung3_families_v1.csv`

Family definitions for FRW masks (F1, F2, …).

| Column name | Type | Meaning |
|-------------|------|---------|
| `family`    | str  | Family label (e.g. `F1_FRW_VIABLE`, `F2_LCDM_LIKE`, `F3_TOY_CORRIDOR`, etc.). |
| `mask_expr` | str  | Boolean expression used to define the family. |
| `n_theta`   | int  | Number of θ-grid points in this family. |
| `frac_of_grid` | float | n\_theta / 2048. |

### 2.4 `stage2_frw_corridor_rung4_family_overlap_v1.csv`

Overlap matrix between FRW families.

| Column name | Type | Meaning |
|-------------|------|---------|
| `family_A`  | str  | First family. |
| `family_B`  | str  | Second family. |
| `n_overlap` | int  | Size of intersection A ∧ B. |
| `frac_of_grid` | float | n\_overlap / 2048. |

### 2.5 Contiguity / stride / smoothing / segments

- `stage2_frw_corridor_rung6_contiguity_v1.csv`  
- `stage2_frw_corridor_rung7_stride_robustness_v1.csv`  
- `stage2_frw_corridor_rung8_smoothing_v1.csv`  
- `stage2_frw_corridor_rung9_segments_v1.csv`  
- `stage2_frw_corridor_rung9_theta_star_alignment_v1.csv`

These tables capture contiguity in θ, segment lengths, and how corridor membership behaves under stride/smoothing and θ★ alignment.

Common columns:

| Column name   | Type   | Meaning |
|---------------|--------|---------|
| `theta_index` | int    | θ-grid index. |
| `theta`       | float  | θ value (radians). |
| `set`         | str    | Name of the set/family under study. |
| `segment_id`  | int    | Segment index for contiguous blocks (when present). |
| `segment_size`| int    | Number of θ points in the segment. |
| `contains_theta_star` | bool | 1 if this segment contains θ★, 0 otherwise. |
| `min_abs_theta_minus_theta_star` | float | Minimal |θ − θ★| in the segment (when present). |

---

## 3. FRW data-probe & empirical anchor endpoints

These live under `stage2/frw_data_probe_analysis/`.

### 3.1 `outputs/tables/phase4_F1_frw_data_probe_mask.csv` (Phase 4 → Stage 2 source)

Phase 4 data-probe mask; consumed by Stage 2. Columns include:

| Column name      | Type  | Meaning |
|------------------|-------|---------|
| `theta_index`    | int   | θ-grid index. |
| `theta`          | float | θ value. |
| `has_matter_era` | bool  | FRW background has a matter-dominated era. |
| `has_late_accel` | bool  | FRW background has late-time acceleration. |
| `smooth_H2`      | bool  | H²(a) behaviour passes smoothness criteria. |
| `frw_viable`     | bool  | Viability mask (often equivalent to combination of above flags). |
| `data_ok`        | bool  | Toy data-probe flag (currently always false in the grid in this rung). |

### 3.2 `outputs/tables/stage2_frw_data_probe_rung1_column_stats_v1.csv`

Simple boolean census over the data-probe flags.

| Column name | Type  | Meaning |
|-------------|-------|---------|
| `column`    | str   | Name of probe column (e.g. `has_matter_era`, `frw_viable`, `data_ok`). |
| `n_true`    | int   | Count of true values. |
| `n_false`   | int   | Count of false values. |
| `frac_true` | float | Fraction true. |
| `note`      | str   | Optional note (e.g. `always_true`, `always_false`). |

### 3.3 Empirical FRW anchor mask

#### `outputs/tables/stage2_frw_empirical_anchor_mask_v1.csv`

Toy FRW empirical anchor defined via a 2D box in (Ω\_Λ, age\_Gyr).

| Column name              | Type   | Meaning |
|--------------------------|--------|---------|
| `theta`                  | float  | θ value (radians). |
| `omega_lambda`           | float  | FRW Ω\_Λ at θ (from Phase 4). |
| `age_Gyr`                | float  | FRW age at θ (Gyr). |
| `frw_viable`             | bool   | FRW viability mask (copied from FRW table). |
| `in_empirical_anchor_box`| bool   | 1 if (Ω\_Λ, age\_Gyr) lies inside the empirical FRW anchor box; 0 otherwise. |

The empirical anchor box is configured in:

- `config/empirical_anchor_box_v1.json`

with fields like:

- `omega_lambda_center`, `omega_lambda_half_width`
- `age_Gyr_center`, `age_Gyr_half_width`

---

## 4. Joint mech–FRW anchor endpoints

These live under `stage2/joint_mech_frw_analysis/outputs/tables/`.

### 4.1 Intersection counts

#### `stage2_joint_mech_frw_anchor_intersections_v1.csv`

Set sizes and fractions for FRW anchor and its intersections on the joint grid.

| Column name    | Type  | Meaning |
|----------------|-------|---------|
| `set`          | str   | Set label (see Section 7). |
| `n_theta`      | int   | Number of θ points in this set. |
| `frac_of_grid` | float | n\_theta / 2048. |

Standard set labels include:

- `ALL_GRID`
- `FRW_VIABLE`
- `TOY_CORRIDOR`
- `EMPIRICAL_ANCHOR`
- `FRW_VIABLE_AND_ANCHOR`
- `CORRIDOR_AND_ANCHOR`
- `CORRIDOR_AND_VIABLE_AND_ANCHOR`

### 4.2 Anchor kernel segments

#### `stage2_joint_mech_frw_anchor_kernel_v1.csv`

Contiguous θ-segments where the triple intersection holds:

- FRW viable ∧ in toy corridor ∧ in empirical anchor box.

| Column name                      | Type   | Meaning |
|----------------------------------|--------|---------|
| `segment_id`                     | int    | Segment index. |
| `n_theta`                        | int    | Number of θ points in the segment. |
| `theta_index_min`               | int    | Smallest θ-index in the segment. |
| `theta_index_max`               | int    | Largest θ-index in the segment. |
| `theta_min`                      | float  | Minimal θ value in the segment. |
| `theta_max`                      | float  | Maximal θ value in the segment. |
| `contains_theta_star`           | bool   | 1 if θ★ lies in this segment; 0 otherwise. |
| `min_abs_theta_minus_theta_star`| float  | Minimal |θ − θ★| within the segment. |

### 4.3 Profiles over sets

#### `stage2_joint_mech_frw_anchor_profiles_v1.csv`

Per-set means / std / min / max over FRW and mech columns.

| Column name                      | Type   | Meaning |
|----------------------------------|--------|---------|
| `set`                            | str    | Set label (Section 7). |
| `n_theta`                        | int    | Count of θ in set. |
| `frac_of_grid`                   | float  | n\_theta / 2048. |
| `E_vac__mean` / `E_vac__std` / `E_vac__min` / `E_vac__max` | float | Stats for `E_vac`. |
| `omega_lambda__mean/std/min/max` | float  | Stats for Ω\_Λ. |
| `age_Gyr__mean/std/min/max`      | float  | Stats for toy FRW age. |
| `mech_baseline_A0__*`            | float  | Stats for `mech_baseline_A0`. |
| `mech_baseline_A_floor__*`       | float  | Stats for `mech_baseline_A_floor`. |
| `mech_baseline_bound__*`         | float  | Stats for `mech_baseline_bound`. |
| `mech_binding_A0__*`             | float  | Stats for `mech_binding_A0`. |
| `mech_binding_A__*`              | float  | Stats for `mech_binding_A`. |
| `mech_binding_bound__*`          | float  | Stats for `mech_binding_bound`. |

### 4.4 Anchor sensitivity

#### `stage2_joint_mech_frw_anchor_sensitivity_v1.csv`

How set sizes change as the empirical anchor box is scaled.

| Column name                         | Type   | Meaning |
|-------------------------------------|--------|---------|
| `scale`                             | float  | Multiplicative factor on box half-widths (e.g. 0.5, 1.0, 1.5). |
| `n_in_box`                          | int    | θ points in scaled anchor box. |
| `n_box_and_frw_viable`             | int    | Count of points in scaled box ∧ FRW viable. |
| `n_box_and_corridor`               | int    | Count of points in scaled box ∧ toy corridor. |
| `n_box_and_corridor_and_frw_viable`| int    | Count of points in scaled box ∧ corridor ∧ FRW viable. |

### 4.5 Mechanism contrast across sets

#### `stage2_joint_mech_frw_anchor_mech_contrast_v1.csv`

Mechanism statistics across key sets.

| Column name      | Type  | Meaning |
|------------------|-------|---------|
| `set`            | str   | Set label. |
| `mech_column`    | str   | One of the mechanism columns (baseline/binding A / bound). |
| `n_theta`        | int   | θ count in set. |
| `frac_of_grid`   | float | n\_theta / 2048. |
| `mean`           | float | Mean over set. |
| `std`            | float | Standard deviation over set. |
| `min` / `max`    | float | Min / max over set. |

---

## 5. Mechanism measure analysis endpoints

### 5.1 `stage2/mech_measure_analysis/outputs/tables/stage2_mech_rung1_phase3_table_inventory_v1.csv`

Inventory of Phase 3 mechanism tables and diagnostics.

| Column name | Type  | Meaning |
|-------------|-------|---------|
| `path`      | str   | Table path under repo root. |
| `kind`      | str   | File type (`csv` or `json`). |
| `size`      | int   | File size in bytes. |
| `n_rows`    | int   | Number of rows (if applicable). |
| `n_cols`    | int   | Number of columns (if applicable). |

### 5.2 `stage2_mech_rung7_theta_gradients_v1.csv`

θ-derivative statistics for mechanism columns across sets.

| Column name     | Type   | Meaning |
|-----------------|--------|---------|
| `set`           | str    | Set label (as before: ALL\_GRID, FRW\_VIABLE, TOY\_CORRIDOR, CORRIDOR\_AND\_VIABLE, CORRIDOR\_AND\_VIABLE\_AND\_ANCHOR). |
| `mech_column`   | str    | Mechanism column whose θ-gradient is being summarized. |
| `n_theta`       | int    | Count of θ used (taking finite differences). |
| `frac_of_grid`  | float  | n\_theta / 2048. |
| `grad_mean`     | float  | Mean gradient dA/dθ over the set. |
| `grad_std`      | float  | Standard deviation of gradients. |
| `grad_min`      | float  | Minimum gradient over the set. |
| `grad_max`      | float  | Maximum gradient over the set. |
| `abs_grad_mean` | float  | Mean absolute gradient. |
| `abs_grad_p95`  | float  | 95th percentile of |grad|. |
| `abs_grad_max`  | float  | Maximum |grad|. |

---

## 6. External FRW host endpoints

These live under `stage2/external_frw_host/outputs/tables/`.

### 6.1 Analytic FRW age cross-check

#### `stage2_external_frw_rung1_age_crosscheck_v1.csv`

Analytic FRW host ages vs toy FRW ages (joined on θ).

| Column name     | Type   | Meaning |
|-----------------|--------|---------|
| `theta_index`   | int    | θ-grid index. |
| `theta`         | float  | θ value. |
| `omega_lambda`  | float  | Ω\_Λ from joint grid. |
| `age_Gyr`       | float  | Toy FRW age from joint grid. |
| `age_Gyr_host`  | float  | Age from analytic FRW host (after global calibration). |
| `age_Gyr_diff`  | float  | `age_Gyr_host - age_Gyr`. |
| `age_Gyr_rel_diff` | float | Relative difference, typically `(age_host - age_repo) / age_repo`. |
| `frw_viable`    | bool   | FRW viability mask (copied through). |

### 6.2 Age contrast summaries

#### `stage2_external_frw_rung2_age_contrast_v1.csv`

Per-set summaries of FRW age differences.

| Column name          | Type   | Meaning |
|----------------------|--------|---------|
| `set`                | str    | Set label. |
| `n_theta`            | int    | Count. |
| `frac_of_grid`       | float  | n\_theta / 2048. |
| `age_Gyr_diff_mean`  | float  | Mean age difference (host − toy). |
| `age_Gyr_diff_std`   | float  | Std of age differences. |
| `age_Gyr_diff_min`   | float  | Min age difference. |
| `age_Gyr_diff_max`   | float  | Max age difference. |
| `age_Gyr_rel_diff_mean` | float | Mean relative difference. |
| `age_Gyr_rel_diff_std`  | float | Std of relative difference. |
| `age_Gyr_rel_diff_min`  | float | Min relative difference. |
| `age_Gyr_rel_diff_max`  | float | Max relative difference. |

### 6.3 Age-consistency mask

#### `stage2_external_frw_rung3_age_consistency_mask_v1.csv`

Mask for age-consistent subset w.r.t host FRW ages.

| Column name                  | Type   | Meaning |
|------------------------------|--------|---------|
| `theta_index`                | int    | θ-grid index. |
| `theta`                      | float  | θ value. |
| `age_Gyr_rel_diff`           | float  | Relative age difference (copied from cross-check table). |
| `age_consistent_rel_le_20pct`| bool   | 1 if |Δage| / age\_repo ≤ 0.2; 0 otherwise. |

### 6.4 Host anchor mask

#### `stage2_external_frw_host_anchor_mask_v1.csv`

Host-side empirical anchor inferred from FRW empirical anchor.

| Column name                        | Type   | Meaning |
|------------------------------------|--------|---------|
| `theta_index`                      | int    | θ-grid index. |
| `theta`                            | float  | θ value. |
| `omega_lambda`                     | float  | Ω\_Λ from host table (copied). |
| `age_Gyr`                          | float  | Toy FRW age from host table. |
| `age_Gyr_host`                     | float  | Host FRW age. |
| `frw_viable`                       | bool   | FRW viability flag (copied). |
| `in_host_empirical_anchor_box`     | bool   | 1 if (Ω\_Λ, age\_Gyr_host) lies inside host-inferred empirical anchor box; 0 otherwise. |

Notes:

- The host-anchor box is **inferred** from the FRW empirical anchor mask by mapping the same θ-set into host-age space.

---

## 7. Joint host–anchor intersections

### 7.1 `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_host_anchor_intersections_v1.csv`

Set sizes for host anchor intersections on the joint grid.

| Column name    | Type  | Meaning |
|----------------|-------|---------|
| `set`          | str   | Set label. |
| `n_theta`      | int   | Number of θ. |
| `frac_of_grid` | float | n\_theta / 2048. |

Standard labels here include:

- `ALL_GRID`
- `FRW_VIABLE`
- `TOY_CORRIDOR`
- `HOST_ANCHOR`
- `FRW_VIABLE_AND_HOST_ANCHOR`
- `CORRIDOR_AND_HOST_ANCHOR`
- `CORRIDOR_AND_VIABLE_AND_HOST_ANCHOR`

### 7.2 `stage2_joint_mech_frw_host_corridor_summary_v1.csv`

Summary over host-calibrated corridor masks. **Note:** here the labels `FRW_VIABLE` and `TOY_CORRIDOR` refer to host-side diagnostics and may not match the original Phase 4 FRW masks exactly.

| Column name    | Type  | Meaning |
|----------------|-------|---------|
| `set`          | str   | Host-diagnostic set label (e.g. `ALL_GRID`, `HOST_CALIBRATED_CORRIDOR`, etc.). |
| `n_theta`      | int   | Count. |
| `frac_of_grid` | float | n\_theta / 2048. |

---

## 8. Standard set labels (Stage 2)

Across Stage 2 tables, the following **set labels** are used with consistent semantics unless otherwise documented:

- `ALL_GRID`  
  Entire θ-grid (2048 points).

- `FRW_VIABLE`  
  Points where `frw_viable == 1` in the toy FRW masks.

- `TOY_CORRIDOR`  
  Points where `in_toy_corridor == 1`.

- `EMPIRICAL_ANCHOR`  
  Points where `in_empirical_anchor_box == 1` (FRW toy empirical anchor).

- `FRW_VIABLE_AND_ANCHOR`  
  `frw_viable == 1` ∧ `in_empirical_anchor_box == 1`.

- `CORRIDOR_AND_ANCHOR`  
  `in_toy_corridor == 1` ∧ `in_empirical_anchor_box == 1`.

- `CORRIDOR_AND_VIABLE_AND_ANCHOR`  
  `in_toy_corridor == 1` ∧ `frw_viable == 1` ∧ `in_empirical_anchor_box == 1`.  
  This is the **FRW toy empirical anchor kernel** conditioned on corridor and viability.

- `HOST_CALIBRATED_CORRIDOR`  
  Points selected by host-side age-consistency mask (see host-corridor doc; semantics may differ from Phase 4 toy corridor).

- `HOST_ANCHOR`  
  Points where `in_host_empirical_anchor_box == 1`, i.e. the host-side image of FRW empirical anchor θ-set.

When a table uses any label with **non-standard semantics**, that should be explicitly documented in the corresponding Stage 2 doc (e.g. host-corridor notes).

---

## 9. Maintenance notes

- This glossary is a **living contract** for Stage 2 endpoints.
- When adding a new Stage 2 CSV or renaming any column:
  1. Update the relevant Stage 2 code.
  2. Update this glossary with:
     - path,
     - column list,
     - brief interpretation.
  3. Reference this file from new Stage 2 doc belts as needed.
- Downstream consumers (papers, notebooks, external tools) should read from this glossary rather than inferring column semantics from code.

