# Stage 2 Table Endpoints & Glossary (v1)

This atlas is a **map of Stage 2 table endpoints** and the boolean sets / masks they define.

It is meant to:
- Prevent name drift and typos (for humans and AI collaborators),
- Clarify how tables depend on each other,
- Make it easy to see where each “corridor / anchor / host-consistency” statement really lives.

Stage 2 follows the Phase 0 contract: these tables are *diagnostic instruments*, not new physics claims.

---

## 0. Core θ–grid

### `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv`

**Role:** Canonical joint θ–grid for Stage 2. Everything that needs both mechanism and FRW lives here.

**Upstream:**
- Phase 3 mechanism tables (vacuum / measure),
- Phase 4 FRW toy outputs and masks.

**Key columns:**

- `theta_index`  
  Integer index on the θ–grid (0 … N−1). Used for contiguity, segments, and as a join key in some Stage 2 rungs.

- `theta`  
  The actual θ value (float). Used as the primary join key between different Stage 2 tables.

- `E_vac`  
  Vacuum-scale proxy from mechanism → FRW bridge.

- `omega_lambda`  
  Effective Λ-like parameter used by the FRW toy.

- `age_Gyr`  
  FRW toy age in Gyr, as produced by Phase 4.

- `in_toy_corridor`  
  Boolean: 1 if θ is in the Phase 4 toy FRW corridor; 0 otherwise.

- `frw_viable`  
  Boolean: 1 if θ passes internal FRW viability checks (e.g. reasonable expansion history); 0 otherwise.

- `lcdm_like`  
  Boolean: 1 if θ looks ΛCDM-like under internal Phase 4 diagnostics; 0 otherwise.

- `shape_and_viable`, `shape_and_lcdm`  
  Boolean composites used in corridor / family rungs.

- `frw_data_ok`  
  Boolean: 1 if θ passes the current FRW “data probe” definition; currently always false in the present toy.

- `mech_baseline_A0`, `mech_baseline_A_floor`, `mech_baseline_bound`  
  Mechanism-side baseline amplitude and bound columns.

- `mech_binding_A0`, `mech_binding_A`, `mech_binding_bound`  
  Mechanism-side binding amplitude and bound columns.

These are the **canonical** mechanism columns; other Stage 2 tables should avoid inventing their own names for the same quantities.

---

## 1. FRW corridor analysis belt

Directory: `stage2/frw_corridor_analysis/outputs/tables/`

These tables interrogate the **Phase 4 FRW masks** and build the “corridor” picture. They do *not* touch mechanism directly.

### 1.1 `stage2_frw_corridor_rung1_sources_v1.csv`

**Role:** Inventory of upstream FRW tables and masks used for corridor analysis.

**Notes:**
- Lists source tables (e.g. Phase 4 FRW masks),
- Records kind (csv/json), number of rows / columns, and basic sanity metadata.

### 1.2 `stage2_frw_corridor_rung2_bool_census_v1.csv`

**Role:** Census of boolean FRW masks on the grid (how many points satisfy each mask).

**Notes:**
- Gives “how many 1’s / 0’s” for each FRW boolean column.
- Useful for quickly seeing whether masks are trivial (all true or all false).

### 1.3 `stage2_frw_corridor_rung3_families_v1.csv`

**Role:** Defines FRW “families” such as:

- F1: FRW_VIABLE,
- F2: LCDM_LIKE,
- F3: TOY_CORRIDOR,
- F4/F5: intersections of corridor with viable / LCDM-like,
- F6: FRW_DATA_OK, etc.

**Notes:**
- Each row is a family name plus counts and fractions of the grid.
- These family names are reused in later rungs (corridor overlap, contiguity, etc.).

### 1.4 `stage2_frw_corridor_rung4_family_overlap_v1.csv`

**Role:** Overlap matrix between the FRW families.

**Notes:**
- Quantifies how much, for example, FRW_VIABLE overlaps TOY_CORRIDOR or LCDM_LIKE.
- Helps identify whether a “corridor” is special or just duplicating another mask.

### 1.5 `stage2_frw_corridor_rung6_contiguity_v1.csv`

**Role:** Contiguity diagnostics of FRW families along θ.

**Notes:**
- Uses `theta_index` to see whether a family is made of:
  - one contiguous corridor,
  - or many split segments.
- Outputs segment counts and basic segment statistics.

### 1.6 `stage2_frw_corridor_rung7_stride_robustness_v1.csv`

**Role:** Downsampling (stride) robustness tests.

**Notes:**
- Re-computes contiguity with coarser sampling,
- Checks whether corridors and families survive or fracture under striding.

### 1.7 `stage2_frw_corridor_rung8_smoothing_v1.csv`

**Role:** Smoothing robustness tests.

**Notes:**
- Applies simple smoothing kernels to FRW masks,
- Checks whether families / corridors are robust to small local changes.

### 1.8 `stage2_frw_corridor_rung9_segments_v1.csv`

**Role:** Final corridor segmentation summary.

**Notes:**
- Lists each contiguous θ segment for chosen families (e.g. FRW_VIABLE, TOY_CORRIDOR),
- Records start/end `theta_index` and θ-range.

### 1.9 `stage2_frw_corridor_rung9_theta_star_alignment_v1.csv`

**Role:** Alignment of θ★ with FRW corridor segments.

**Notes:**
- For each segment, records:
  - whether it contains θ★,
  - minimum |θ − θ★| distance to the segment,
  - and alignment diagnostics.

---

## 2. FRW data probes & empirical anchor

Directory: `stage2/frw_data_probe_analysis/`

### 2.1 `outputs/tables/stage2_frw_data_probe_rung1_column_stats_v1.csv`

**Role:** Statistics of FRW data-probe booleans.

**Columns (conceptual):**
- Set name (e.g. ALL_GRID),
- For each probe (e.g. `has_matter_era`, `has_late_accel`, `smooth_H2`, `frw_viable`, `data_ok`):
  - counts, fractions, and “always_true / always_false” flags.

**Usage:**
- Confirms, for example, that `data_ok` is currently nowhere true.

### 2.2 `outputs/tables/stage2_frw_empirical_anchor_mask_v1.csv`

**Role:** Defines the **FRW-side empirical anchor box** in (ΩΛ, age_Gyr).

**Upstream:**
- FRW shape-probe mask table:  
  `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`
- Anchor config:  
  `stage2/frw_data_probe_analysis/config/empirical_anchor_box_v1.json`

**Expected columns:**

- `theta` – join key.
- `in_empirical_anchor_box` – boolean; 1 if θ lies inside the chosen ΩΛ–age box.

Additional pass-through columns (e.g. `omega_lambda`, `age_Gyr`, FRW masks) may be present depending on implementation, but `theta` and `in_empirical_anchor_box` are the canonical ones.

**Canonical set name:**
- `EMPIRICAL_ANCHOR` := `{ θ | in_empirical_anchor_box == 1 }`  
  (18 points in the current toy grid).

---

## 3. Joint mech–FRW anchor and corridor analysis

Directory: `stage2/joint_mech_frw_analysis/outputs/tables/`

### 3.1 `stage2_joint_theta_grid_v1.csv`

Already described in §0. This is the **primary joint endpoint**.

---

### 3.2 `stage2_joint_mech_frw_anchor_intersections_v1.csv`

**Role:** Set census for intersections of:

- FRW viability,
- Toy corridor,
- Empirical anchor.

**Key set names and meanings:**

- `ALL_GRID`  
  The full θ-grid (size N = 2048).

- `FRW_VIABLE`  
  `{ θ | frw_viable == 1 }` (size = 1016).

- `TOY_CORRIDOR`  
  `{ θ | in_toy_corridor == 1 }` (size = 1186).

- `EMPIRICAL_ANCHOR`  
  `{ θ | in_empirical_anchor_box == 1 }` (size = 18).

Intersections:

- `FRW_VIABLE_AND_ANCHOR`  
  `FRW_VIABLE ∧ EMPIRICAL_ANCHOR`.

- `CORRIDOR_AND_ANCHOR`  
  `TOY_CORRIDOR ∧ EMPIRICAL_ANCHOR`.

- `CORRIDOR_AND_VIABLE_AND_ANCHOR`  
  `TOY_CORRIDOR ∧ FRW_VIABLE ∧ EMPIRICAL_ANCHOR`  
  (18 points in the current toy).

Each row contains:
- `set`, `n_theta`, `frac_of_grid`.

---

### 3.3 `stage2_joint_mech_frw_anchor_kernel_v1.csv`

**Role:** Identifies the **anchor kernel segments** along θ.

**Notes:**
- Uses `theta_index` over the set `CORRIDOR_AND_VIABLE_AND_ANCHOR`.
- Returns:

  - Number of segments,
  - For each segment:
    - start/end `theta_index`,
    - θ-range `[theta_min, theta_max]`,
    - whether segment contains θ★,
    - minimum |θ − θ★| within the segment.

**Interpretation in the current toy:**
- Finds **two 9-point segments** in θ, neither containing θ★.

---

### 3.4 `stage2_joint_mech_frw_anchor_profiles_v1.csv`

**Role:** Mechanism and FRW profiles over key sets.

**Key columns include:**

- `set` – one of:
  - `ALL_GRID`, `FRW_VIABLE`, `TOY_CORRIDOR`,
  - `EMPIRICAL_ANCHOR`,
  - `FRW_VIABLE_AND_ANCHOR`,
  - `CORRIDOR_AND_ANCHOR`,
  - `CORRIDOR_AND_VIABLE_AND_ANCHOR`.

- `n_theta`, `frac_of_grid`.

For each scalar column from the joint grid (e.g. `E_vac`, `omega_lambda`, `age_Gyr`, `mech_*`), summary stats:

- `<col>__mean`, `<col>__std`, `<col>__min`, `<col>__max`.

This is the main source for statements like:

- “In the empirical anchor kernel, mech amplitude is ≈ 0.0461 with tiny spread.”

---

### 3.5 `stage2_joint_mech_frw_anchor_sensitivity_v1.csv`

**Role:** Sensitivity of the empirical anchor to widening/narrowing the ΩΛ–age box.

**Columns (conceptual):**

- `scale` – multiplicative factor on half-widths (e.g. 0.50, 1.00, 1.50).
- For each scale:
  - `n_in_box` – points in the scaled box.
  - `n_box∧FRW`, `n_box∧corr`, `n_box∧corr∧FRW` – intersection counts with FRW viability and toy corridor.

---

### 3.6 `stage2_joint_mech_frw_anchor_mech_contrast_v1.csv`

**Role:** Mechanism amplitude contrast across sets.

**Key columns:**

- `set` – same set names as in the profiles file, but focusing on:
  - `ALL_GRID`, `FRW_VIABLE`,
  - `CORRIDOR_AND_VIABLE`,
  - `CORRIDOR_AND_VIABLE_AND_ANCHOR`.

- `mech_column` – one of:
  - `mech_baseline_A0`, `mech_baseline_A_floor`, `mech_baseline_bound`,
  - `mech_binding_A0`, `mech_binding_A`, `mech_binding_bound`.

- `n_theta`, `frac_of_grid`, `mean`, `std`, `min`, `max`.

This table is where statements like:

- “In the anchored corridor, mech amplitude sits on a narrow plateau compared to the full FRW-viable set”

are grounded.

---

### 3.7 `stage2_joint_mech_frw_host_corridor_summary_v1.csv`

**Role:** Host-calibrated FRW age consistency vs corridor and anchor.

**Upstream:**

- Joint grid,
- Age-consistency mask:  
  `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung3_age_consistency_mask_v1.csv`,
- Empirical anchor mask.

**Sets:**

- `ALL_GRID`
- `FRW_VIABLE`
- `TOY_CORRIDOR`
- `HOST_CALIBRATED_CORRIDOR`  
  `{ θ | age_consistent_rel_le_20pct == 1 }` (with current 20% threshold).
- `HOST_CORRIDOR_AND_ANCHOR`  
  `HOST_CALIBRATED_CORRIDOR ∧ EMPIRICAL_ANCHOR`.

In the current toy:
- `HOST_CALIBRATED_CORRIDOR` has 778 points,
- `HOST_CORRIDOR_AND_ANCHOR` is empty.

---

### 3.8 `stage2_joint_mech_frw_host_anchor_intersections_v1.csv`

**Role:** Host-space analogue of the FRW anchor intersections.

**Upstream:**

- Joint grid,
- Host anchor mask:  
  `stage2/external_frw_host/outputs/tables/stage2_external_frw_host_anchor_mask_v1.csv`.

**Sets:**

- `ALL_GRID`
- `FRW_VIABLE`
- `TOY_CORRIDOR`
- `HOST_ANCHOR`
- `FRW_VIABLE_AND_HOST_ANCHOR`
- `CORRIDOR_AND_HOST_ANCHOR`
- `CORRIDOR_AND_VIABLE_AND_HOST_ANCHOR`

Currently, the host anchor picks the same 18 θ-points as the FRW anchor, just viewed in host-age space.

---

## 4. Mech measure analysis belt

Directory: `stage2/mech_measure_analysis/outputs/tables/`

### 4.1 `stage2_mech_rung1_phase3_table_inventory_v1.csv`

**Role:** Inventory of Phase 3 mechanism tables.

**Notes:**
- Lists each Phase 3 output table under `phase3/outputs/tables`,
- Records kind (csv/json), size, row/column counts,
- Provides a quick view of what mechanism-side tables exist.

---

### 4.2 `stage2_mech_rung7_theta_gradients_v1.csv`

**Role:** θ-derivative statistics of mechanism amplitudes over key sets.

**Sets:**
- `ALL_GRID`
- `FRW_VIABLE`
- `TOY_CORRIDOR`
- `CORRIDOR_AND_VIABLE`
- `CORRIDOR_AND_VIABLE_AND_ANCHOR`

**Columns:**

- `set`
- `mech_column` – same six canonical mechanism columns as above.
- `n_theta`, `frac_of_grid`
- `grad_mean`, `grad_std`, `grad_min`, `grad_max`
- `abs_grad_mean`, `abs_grad_p95`, `abs_grad_max`

Used to quantify how “flat” or “steep” the mechanism is in the anchor kernel vs broader sets.

---

## 5. External FRW host belt

Directory: `stage2/external_frw_host/outputs/tables/`

### 5.1 `stage2_external_frw_rung1_age_crosscheck_v1.csv`

**Role:** Analytic FRW-host age comparison.

**Columns (key):**

- `theta_index`, `theta`
- `omega_lambda`
- `age_Gyr` – repo FRW toy age
- `age_Gyr_host` – host analytic FRW age (after single-scale calibration)
- `age_Gyr_diff` – host − repo
- `age_Gyr_rel_diff` – (host − repo) / repo
- `frw_viable` – pass-through from joint grid

---

### 5.2 `stage2_external_frw_rung2_age_contrast_v1.csv`

**Role:** Age-difference summary per set.

**Sets (rows):**

- `ALL_GRID`
- `FRW_VIABLE`
- `CORRIDOR_AND_VIABLE`
- `CORRIDOR_AND_VIABLE_AND_ANCHOR`

**Columns (key):**

- `n_theta`, `frac_of_grid`
- `age_Gyr_diff_mean`, `age_Gyr_diff_std`, `age_Gyr_diff_min`, `age_Gyr_diff_max`
- `age_Gyr_rel_diff_mean`, `age_Gyr_rel_diff_std`, `age_Gyr_rel_diff_min`, `age_Gyr_rel_diff_max`

This is where the “~80% relative age mismatch in the anchored corridor” is quantified.

---

### 5.3 `stage2_external_frw_rung3_age_consistency_mask_v1.csv`

**Role:** Age-consistency mask relative to the host under a chosen threshold.

**Columns (key):**

- `theta_index`, `theta`
- `age_Gyr_rel_diff` – from the cross-check table
- `age_consistent_rel_le_20pct` – boolean: 1 if |rel diff| ≤ 0.2, else 0

**Sets derived:**

- `HOST_CALIBRATED_CORRIDOR` := `{ θ | frw_viable ∧ age_consistent_rel_le_20pct }`

In current config, this set has 778 points and intersects the toy corridor but *not* the empirical anchor.

---

### 5.4 `stage2_external_frw_host_anchor_mask_v1.csv`

**Role:** Host-space empirical anchor definition.

**Upstream:**

- `stage2_external_frw_rung1_age_crosscheck_v1.csv` (host ages),
- `stage2_frw_empirical_anchor_mask_v1.csv` (FRW anchor).

**Columns (key):**

- `theta_index`, `theta`
- `omega_lambda`
- `age_Gyr` – repo FRW age
- `age_Gyr_host` – host FRW age
- `frw_viable`
- `in_host_empirical_anchor_box` – boolean: 1 if θ lies inside the **host** ΩΛ–age_host box inferred from the FRW anchor.

By design, this currently selects the same 18 θ-points as the FRW empirical anchor, just measured in host-age coordinates.

---

## 6. Naming discipline and future use

- **Canonical join keys:**  
  - Use `theta` for cross-belt joins unless a script explicitly requires `theta_index`.
- **Canonical mechanism columns:**  
  - Always reuse `mech_baseline_A0`, `mech_baseline_A_floor`, `mech_baseline_bound`,  
    `mech_binding_A0`, `mech_binding_A`, `mech_binding_bound`.
- **Canonical sets:**  
  - `ALL_GRID`, `FRW_VIABLE`, `TOY_CORRIDOR`, `EMPIRICAL_ANCHOR`,  
    `FRW_VIABLE_AND_ANCHOR`, `CORRIDOR_AND_ANCHOR`, `CORRIDOR_AND_VIABLE_AND_ANCHOR`,  
    `HOST_CALIBRATED_CORRIDOR`, `HOST_CORRIDOR_AND_ANCHOR`, `HOST_ANCHOR`.

Any new Stage 2 rung or external host module should:

1. Reuse these names wherever the concept is the same.
2. Add new names only when the concept is genuinely new, and log them here.

