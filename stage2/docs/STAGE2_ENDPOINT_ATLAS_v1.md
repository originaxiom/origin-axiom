# Stage 2 Endpoint Atlas (v1)

This atlas lists the main **Stage 2 CSV endpoints** and the scripts that produce them, so humans (and tools) can quickly see:

- where key tables live,
- which script regenerates them,
- what the primary join keys are,
- and which masks / columns matter for interpretation.

It is **descriptive only** and does not introduce new claims. For exact column names and types, always defer to the CSV header and producing script.

---

## 0. Conventions

- **Repo root:** assumed to be the top-level `origin-axiom` directory.
- All paths below are **relative to repo root**.
- “Primary keys” = columns you can reliably use to join / align tables.
- “Mask columns” = boolean columns used for defining subsets / families.

---

## 1. Documentation / repo audit endpoints

### 1.1 Broken refs table

- **Path:**  
  `stage2/doc_repo_audit/outputs/tables/stage2_doc_broken_refs_v1.csv`
- **Producer:**  
  `stage2/doc_repo_audit/src/analyze_doc_links_v1.py`
- **Primary keys (typical):**
  - `source_rel_path` – Markdown file containing the broken link
  - `line_no` – line of the offending link
- **Key columns (examples):**
  - `link_text` – the bracket text
  - `link_target` – raw Markdown target
  - `resolved_rel_path` – where the link resolver *thinks* it points
  - `exists` – boolean, whether the resolved path exists
- **Role:**  
  Registry of broken or suspicious Markdown links across the repo. Used for doc belts and for keeping the repo navigable.

---

### 1.2 Orphan candidates table

- **Path:**  
  `stage2/doc_repo_audit/outputs/tables/stage2_doc_orphan_candidates_v1.csv`
- **Producer:**  
  `stage2/doc_repo_audit/src/analyze_doc_links_v1.py`
- **Primary keys (typical):**
  - `rel_path` – path of the Markdown file
- **Key columns (examples):**
  - `kind` – e.g. `md`, `pdf`, etc.
  - `location` – e.g. `root`, `phase`, etc.
  - `size_bytes`
  - `title`
  - `referenced_by` – semicolon-separated list of referrers
  - `is_orphan_candidate` – boolean flag
  - various `has_todo` / `has_draft` / `has_deprecated` flags
- **Role:**  
  Helps find documentation that may be unreferenced (“orphaned”) or legacy, so it can be either adopted, archived, or clearly labeled.

---

### 1.3 Open threads table

- **Path:**  
  `stage2/doc_repo_audit/outputs/tables/stage2_doc_open_threads_v1.csv`
- **Producer:**  
  `stage2/doc_repo_audit/src/scan_doc_open_threads_v1.py`
- **Primary keys (typical):**
  - `rel_path`
  - `line_no`
- **Key columns (examples):**
  - `pattern` – the matched tag, e.g. `TODO`, `DRAFT`, `FIXME`
  - `line_snippet` – local context line
- **Role:**  
  “Open threads” radar for TODO/DRAFT/FIXME-style markers. Used to keep track of non-locked areas without polluting phase claims.

---

## 2. FRW corridor analysis endpoints

All of these live under:

- `stage2/frw_corridor_analysis/outputs/tables/`

They interrogate the **Phase 4 FRW masks** and build families, overlaps, contiguity, etc.

### 2.1 Source inventory

- **Path:**  
  `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung1_sources_v1.csv`
- **Producer:**  
  `stage2/frw_corridor_analysis/src/inventory_frw_sources_v1.py`
- **Primary keys (typical):**
  - a per-source identifier (see CSV header)
- **Key columns (examples):**
  - file paths for FRW masks (viability, LCDM-like, toy corridor)
  - `kind` / `n_rows` / `n_cols`
- **Role:**  
  Lightweight inventory of which FRW mask tables exist and their basic shapes.

---

### 2.2 Boolean census

- **Path:**  
  `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung2_bool_census_v1.csv`
- **Producer:**  
  `stage2/frw_corridor_analysis/src/analyze_frw_bool_census_v1.py`
- **Primary keys:**
  - one row per boolean column / mask
- **Key columns (examples):**
  - `mask_name`
  - `n_true`, `n_false`
  - `frac_true`, `frac_false`
- **Role:**  
  Sanity overview of how often each FRW mask is true/false across the θ-grid.

---

### 2.3 Families and overlaps

- **Paths:**
  - `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung3_families_v1.csv`
  - `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung4_family_overlap_v1.csv`
- **Producers:**  
  `analyze_frw_families_v1.py`, `analyze_frw_family_overlap_v1.py`
- **Primary keys:**
  - `family` / `set`
- **Key columns (examples):**
  - `n_theta`, `frac_of_grid`
  - for overlaps: pairwise intersections and their fractions
- **Role:**  
  Encodes FRW “families” such as FRW_VIABLE, TOY_CORRIDOR, LCDM_LIKE, and their overlaps.

---

### 2.4 Contiguity, stride robustness, smoothing, segments

- **Paths:**
  - `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung6_contiguity_v1.csv`
  - `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung7_stride_robustness_v1.csv`
  - `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung8_smoothing_v1.csv`
  - `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung9_segments_v1.csv`
  - `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung9_theta_star_alignment_v1.csv`
- **Producers:**  
  corresponding `analyze_frw_*_v1.py` scripts under `stage2/frw_corridor_analysis/src/`.
- **Primary keys:**
  - usually `family` plus segment IDs or stride parameters
- **Key columns (examples):**
  - number and length of contiguous segments in θ
  - stride / smoothing parameters and how they affect corridor stability
  - distances from segments to θ\*
- **Role:**  
  Quantifies whether FRW corridors are “fat and contiguous” or “needle-like”, and how robust they are to sampling tricks.

---

## 3. FRW data-probe + empirical anchor endpoints

### 3.1 FRW data-probe diagnostics

- **Path:**  
  `stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_data_probe_rung1_column_stats_v1.csv`
- **Producer:**  
  `stage2/frw_data_probe_analysis/src/analyze_frw_data_probes_v1.py`
- **Primary keys:**
  - `column` – name of boolean probe column
- **Key columns (examples):**
  - `n_true`, `n_false`
  - `frac_true`, `frac_false`
  - optional `note` (e.g. “always_true”, “always_false”)
- **Role:**  
  Census of FRW probe flags such as `has_matter_era`, `has_late_accel`, `smooth_H2`, `frw_viable`, `data_ok`.

---

### 3.2 Empirical anchor mask

- **Path:**  
  `stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_empirical_anchor_mask_v1.csv`
- **Producer:**  
  `stage2/frw_data_probe_analysis/src/analyze_frw_empirical_anchor_v1.py`
- **Primary keys:**
  - `theta` (one row per θ-grid point)
- **Key columns (examples):**
  - columns inherited from the Phase 4 FRW shape table, such as:
    - `theta`, `E_vac`, `omega_lambda`, `age_Gyr`
  - `in_empirical_anchor_box` – boolean: whether the point lies in the chosen (Ω_Λ, age) box.
- **Role:**  
  Defines the first empirical anchor subset: FRW points whose (Ω_Λ-like, age_Gyr) lie in a small “data-inspired” box.

---

## 4. Joint mech–FRW endpoints (θ-grid bridge)

All of these live under:

- `stage2/joint_mech_frw_analysis/outputs/tables/`

They are built on the shared grid:

### 4.1 Joint θ grid

- **Path:**  
  `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv`
- **Producer:**  
  `stage2/joint_mech_frw_analysis/src/build_joint_theta_grid_v1.py`
- **Primary keys:**
  - `theta_index`
  - `theta`
- **Key columns (from header):**
  - Mechanism/FRW shared:
    - `theta_index`, `theta`, `E_vac`, `omega_lambda`, `age_Gyr`
  - FRW masks:
    - `in_toy_corridor`, `frw_viable`, `lcdm_like`,  
      `shape_and_viable`, `shape_and_lcdm`, `frw_data_ok`
  - Mechanism measure columns:
    - `mech_baseline_A0`, `mech_baseline_A_floor`, `mech_baseline_bound`
    - `mech_binding_A0`, `mech_binding_A`, `mech_binding_bound`
- **Role:**  
  The **main bridge table** aligning θ, vacuum/FRW quantities, and mechanism measures. Most Stage 2 analyses join against this.

---

### 4.2 Anchor intersections

- **Path:**  
  `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_intersections_v1.csv`
- **Producer:**  
  `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_intersections_v1.py`
- **Primary keys:**
  - `set` – name of subset
- **Key columns (examples):**
  - `set` – one of:
    - `ALL_GRID`
    - `FRW_VIABLE`
    - `TOY_CORRIDOR`
    - `EMPIRICAL_ANCHOR`
    - `FRW_VIABLE_AND_ANCHOR`
    - `CORRIDOR_AND_ANCHOR`
    - `CORRIDOR_AND_VIABLE_AND_ANCHOR`
  - `n_theta`, `frac_of_grid`
- **Role:**  
  Counts and fractions for intersections of FRW viability, toy corridor, and the empirical anchor.

---

### 4.3 Anchor kernel (contiguity in θ)

- **Path:**  
  `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_kernel_v1.csv`
- **Producer:**  
  `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_kernel_v1.py`
- **Primary keys:**
  - segment identifiers (see header)
- **Key columns (examples):**
  - segment index
  - `theta_index_min`, `theta_index_max`
  - `theta_min`, `theta_max`
  - indicators for whether a segment contains θ\* and its distance from θ\*
- **Role:**  
  Describes the empirical-anchor ∧ FRW-viable ∧ toy-corridor region as **contiguous θ-segments**.

---

### 4.4 Anchor profiles (mean values over sets)

- **Path:**  
  `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_profiles_v1.csv`
- **Producer:**  
  `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_profiles_v1.py`
- **Primary keys:**
  - `set` – same set labels as intersections
- **Key columns (seen in header):**
  - `set`, `n_theta`, `frac_of_grid`
  - For each scalar field (e.g. `E_vac`, `omega_lambda`, `age_Gyr`, `mech_baseline_A0`, …):
    - `<name>__mean`, `<name>__std`, `<name>__min`, `<name>__max`
- **Role:**  
  Summarises the “typical” values of mechanism and FRW quantities over each subset (ALL, FRW_VIABLE, CORRIDOR_AND_VIABLE, EMPIRICAL_ANCHOR, etc.).

---

### 4.5 Anchor sensitivity

- **Path:**  
  `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_sensitivity_v1.csv`
- **Producer:**  
  `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_sensitivity_v1.py`
- **Primary keys:**
  - `scale` – scaling factor for the empirical box widths (e.g. 0.50, 1.00, 1.50)
- **Key columns (examples):**
  - `n_in_box`
  - `n_box_and_frw`
  - `n_box_and_corr`
  - `n_box_and_corr_and_frw`
- **Role:**  
  Checks how the anchor set size and intersections change when the box in (Ω_Λ, age) is shrunk / expanded.

---

### 4.6 Anchor–mechanism contrast

- **Path:**  
  `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_mech_contrast_v1.csv`
- **Producer:**  
  `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_mech_contrast_v1.py`
- **Primary keys:**
  - `set`
  - `mech_column`
- **Key columns (from header):**
  - `set` – e.g. `ALL_GRID`, `FRW_VIABLE`, `CORRIDOR_AND_VIABLE`, `CORRIDOR_AND_VIABLE_AND_ANCHOR`, `CORRIDOR_AND_VIABLE_NOT_ANCHOR`
  - `mech_column` – one of the mechanism measure columns
  - `n_theta`, `frac_of_grid`
  - `mean`, `std`, `min`, `max`
- **Role:**  
  Compares mechanism measure statistics inside vs outside the empirical anchor, and inside vs outside the FRW corridor.

---

### 4.7 Host corridor summary (age-consistent corridor)

- **Path:**  
  `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_host_corridor_summary_v1.csv`
- **Producer:**  
  `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_host_corridor_v1.py`
- **Primary keys:**
  - `set`
- **Key columns (examples):**
  - `set` – e.g. `ALL_GRID`, `FRW_VIABLE`, `TOY_CORRIDOR`, `HOST_CALIBRATED_CORRIDOR`, `HOST_CORRIDOR_AND_ANCHOR`
  - `n_theta`, `frac_of_grid`
- **Role:**  
  Summarises the size of the **host-calibrated FRW age-consistent corridor** and its overlap with the empirical anchor and the toy corridor.

---

## 5. Mechanism measure analysis endpoints

All under:

- `stage2/mech_measure_analysis/outputs/tables/`

### 5.1 Phase 3 tables inventory

- **Path:**  
  `stage2/mech_measure_analysis/outputs/tables/stage2_mech_rung1_phase3_table_inventory_v1.csv`
- **Producer:**  
  `stage2/mech_measure_analysis/src/inventory_phase3_tables_v1.py`
- **Primary keys:**
  - table identifier (see header)
- **Key columns (examples):**
  - file paths for Phase 3 tables
  - `kind` – `csv` or `json`
  - `size`, `n_rows`, `n_cols`
- **Role:**  
  Inventory of Phase 3 mechanism tables before deeper analysis.

---

### 5.2 θ-gradients of mechanism measure

- **Path:**  
  `stage2/mech_measure_analysis/outputs/tables/stage2_mech_rung7_theta_gradients_v1.csv`
- **Producer:**  
  `stage2/mech_measure_analysis/src/analyze_mech_theta_gradients_v1.py`
- **Primary keys:**
  - `set`
  - `mech_column`
- **Key columns (from header):**
  - `set` – e.g. `ALL_GRID`, `FRW_VIABLE`, `TOY_CORRIDOR`, `CORRIDOR_AND_VIABLE`, `CORRIDOR_AND_VIABLE_AND_ANCHOR`
  - `mech_column`
  - `n_theta`, `frac_of_grid`
  - `grad_mean`, `grad_std`, `grad_min`, `grad_max`
  - `abs_grad_mean`, `abs_grad_p95`, `abs_grad_max`
- **Role:**  
  Summarises how “steep” the mechanism measure is as a function of θ over different subsets, and whether gradients look special in the empirical anchor region.

---

## 6. External FRW host endpoints

All under:

- `stage2/external_frw_host/outputs/tables/`

These relate the repo’s FRW toy outputs to a **simple analytic FRW age host**.

### 6.1 Age cross-check table

- **Path:**  
  `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung1_age_crosscheck_v1.csv`
- **Producer:**  
  `stage2/external_frw_host/src/compute_analytic_frw_ages_v1.py`
- **Primary keys:**
  - `theta_index`
  - `theta`
- **Key columns (from header):**
  - `theta_index`, `theta`, `omega_lambda`
  - `age_Gyr` – repo toy FRW age
  - `age_Gyr_host` – analytic host-computed FRW age
  - `age_Gyr_diff` – host minus repo
  - `age_Gyr_rel_diff` – relative difference fraction
  - `frw_viable` – copied mask
- **Role:**  
  Row-by-row comparison of toy FRW ages vs an external analytic FRW age calculation.

---

### 6.2 Age contrast summary

- **Path:**  
  `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung2_age_contrast_v1.csv`
- **Producer:**  
  `stage2/external_frw_host/src/analyze_external_frw_age_contrast_v1.py`
- **Primary keys:**
  - `set`
- **Key columns (from header):**
  - `set` – e.g. `ALL_GRID`, `FRW_VIABLE`, `CORRIDOR_AND_VIABLE`, `CORRIDOR_AND_VIABLE_AND_ANCHOR`
  - `n_theta`, `frac_of_grid`
  - `age_Gyr_diff_mean`, `age_Gyr_diff_std`, `age_Gyr_diff_min`, `age_Gyr_diff_max`
  - `age_Gyr_rel_diff_mean`, `age_Gyr_rel_diff_std`, `age_Gyr_rel_diff_min`, `age_Gyr_rel_diff_max`
- **Role:**  
  Summarises how far the toy FRW ages are from the analytic host, especially inside the corridor and anchor.

---

### 6.3 Age-consistency mask (relative-error filter)

- **Path:**  
  `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung3_age_consistency_mask_v1.csv`
- **Producer:**  
  `stage2/external_frw_host/src/flag_age_consistent_subset_v1.py`
- **Primary keys:**
  - `theta_index`
- **Key columns (examples):**
  - `theta`, `omega_lambda`, `age_Gyr`, `age_Gyr_host`
  - `age_Gyr_rel_diff`
  - `age_consistent_rel_le_20pct` – boolean: host vs repo age consistent at ≤ 20% relative error
- **Role:**  
  Defines the *host-calibrated age-consistent set* used for the host corridor analysis.

---

### 6.4 Host anchor mask (host-side empirical anchor)

- **Path:**  
  `stage2/external_frw_host/outputs/tables/stage2_external_frw_host_anchor_mask_v1.csv`
- **Producer:**  
  `stage2/external_frw_host/src/analyze_external_frw_host_anchor_v1.py`
- **Primary keys:**
  - `theta_index`
  - `theta`
- **Key columns (examples):**
  - `omega_lambda`, `age_Gyr`, `age_Gyr_host`, `frw_viable`
  - `in_host_empirical_anchor_box` – boolean: in host-inferred anchor box
- **Role:**  
  Host-side mirror of the empirical anchor, inferred from the FRW anchor’s Ω_Λ range and mapped onto host age.

---

## 7. Host–anchor intersections (joint mech–FRW)

### 7.1 Host-anchor intersections

- **Path:**  
  `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_host_anchor_intersections_v1.csv`
- **Producer:**  
  `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_host_anchor_intersections_v1.py`
- **Primary keys:**
  - `set`
- **Key columns (examples):**
  - `set` – e.g. `ALL_GRID`, `FRW_VIABLE`, `TOY_CORRIDOR`, `HOST_ANCHOR`, `FRW_VIABLE_AND_HOST_ANCHOR`, `CORRIDOR_AND_HOST_ANCHOR`, `CORRIDOR_AND_VIABLE_AND_HOST_ANCHOR`
  - `n_theta`, `frac_of_grid`
- **Role:**  
  Counts and fractions for intersections between the host empirical anchor, FRW viability, and the toy corridor.

---

## 8. How to use this atlas

- When adding a new Stage 2 table:
  1. Add a row/section here with:
     - path,
     - producer script,
     - primary keys,
     - key columns,
     - 1–2 line description.
  2. Ensure the producing script name and CSV path are stable.
- When writing code or papers:
  - Use this atlas to avoid mistyping paths or guessing column names.
  - Treat the **joint θ grid** and **Phase 2/3/4 alignment docs** as the primary hubs for joins.

