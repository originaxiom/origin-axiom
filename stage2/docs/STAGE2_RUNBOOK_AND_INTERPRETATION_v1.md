# Stage 2 – Runbook and Interpretation (v1)

This document is the **human + AI runbook for Stage 2**.

- It tells you **what to run**, **in what order**, and **where to look**.
- It explains how to interpret Stage 2 outputs without over-claiming or drifting beyond Phase 0–4 contracts.
- It is meant to be read alongside:
  - `stage2/docs/STAGE2_CODE_AUDIT_AND_HEALTHCHECK_v1.md`
  - `stage2/docs/STAGE2_ENDPOINTS_AND_TABLES_MAP_v1.md`
  - The Phase docs (`phase3/PHASE3_ALIGNMENT_v1.md`, `phase4/PHASE4_ALIGNMENT_v1.md`, `phase5/PHASE5_ALIGNMENT_v1.md` when present).

Stage 2 remains a **diagnostic layer**: it *interrogates* the mechanism + FRW toy implementations and their contact with a simple empirical anchor. It does **not** introduce new physical claims on its own.

---

## 0. Pre-requisites

Before running Stage 2, the following should hold:

1. **Repo state**
   - Phase 0–2 papers build cleanly via:
     - `scripts/build_papers.sh`
     - `scripts/check_papers_clean.sh`
   - Phase 3 mechanism pipeline is up-to-date and builds via Snakemake:
     - `snakemake -s phase3/workflow/Snakefile -j 4` (or similar).
   - Phase 4 FRW toy outputs and masks exist under:
     - `phase4/outputs/tables/`

2. **Core outputs available**
   - Mechanism tables:
     - `phase3/outputs/tables/mech_baseline_scan.csv`
     - `phase3/outputs/tables/mech_baseline_scan_diagnostics.json`
     - `phase3/outputs/tables/mech_binding_certificate.csv`
     - `phase3/outputs/tables/mech_binding_certificate_diagnostics.json`
     - `phase3/outputs/tables/phase3_measure_v1_hist.csv`
     - `phase3/outputs/tables/phase3_measure_v1_stats.json`
   - FRW toy tables:
     - `phase4/outputs/tables/phase4_F1_frw_viability_mask.csv`
     - `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`
     - `phase4/outputs/tables/phase4_F1_frw_data_probe_mask.csv`
   - Joint grid:
     - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv`

   All of these can be rebuilt using the scripts referenced in  
   `STAGE2_CODE_AUDIT_AND_HEALTHCHECK_v1.md` and  
   `STAGE2_ENDPOINTS_AND_TABLES_MAP_v1.md`.

3. **Environment**
   - Python environment that runs all Stage 2 scripts (see healthcheck doc).
   - No uncommitted hacks to Stage 2 scripts unless clearly logged in the main `PROGRESS_LOG.md` and/or Stage 2 docs.

---

## 1. Standard Stage 2 run sequence

This is the **canonical Stage 2 ladder** at the current repository state.  
Exact filenames and arguments are catalogued in `STAGE2_ENDPOINTS_AND_TABLES_MAP_v1.md`; here we focus on logic and interpretation.

### 1.1 Phase 4 FRW corridor analysis

**Goal:** Understand the structure of FRW toy viability and θ-corridors.

Core scripts (FRW corridor belt):

- `stage2/frw_corridor_analysis/src/analyze_frw_corridor_rung1_sources_v1.py`
- `stage2/frw_corridor_analysis/src/analyze_frw_corridor_rung2_bool_census_v1.py`
- `stage2/frw_corridor_analysis/src/analyze_frw_corridor_rung3_families_v1.py`
- `stage2/frw_corridor_analysis/src/analyze_frw_corridor_rung4_family_overlap_v1.py`
- `stage2/frw_corridor_analysis/src/analyze_frw_corridor_rung6_contiguity_v1.py`
- `stage2/frw_corridor_analysis/src/analyze_frw_corridor_rung7_stride_robustness_v1.py`
- `stage2/frw_corridor_analysis/src/analyze_frw_corridor_rung8_smoothing_v1.py`
- `stage2/frw_corridor_analysis/src/analyze_frw_corridor_rung9_segments_v1.py`
- `stage2/frw_corridor_analysis/src/analyze_frw_corridor_rung9_theta_star_alignment_v1.py`

**Outputs (examples):**

- `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung3_families_v1.csv`
- `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung6_contiguity_v1.csv`
- `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung9_segments_v1.csv`
- `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung9_theta_star_alignment_v1.csv`

**How to read:**

- These tables answer:
  - Do we have extended θ-corridors, or isolated viable θ-points?
  - How many segments, how wide, and how stable under stride/smoothing?
  - Where is θ★ relative to each segment (inside / outside / distance)?

This belt is **purely internal geometry** of the FRW toy universe. No empirical data yet.

---

### 1.2 FRW data probes and empirical anchor

**Goal:** Define and examine a **simple empirical anchor** in FRW toy space.

Config:

- `stage2/frw_data_probe_analysis/config/empirical_anchor_box_v1.json`
  - Defines a 2D box in `(omega_lambda, age_Gyr)` that stands in for a toy “observationally allowed” region.

Core scripts:

- `stage2/frw_data_probe_analysis/src/analyze_frw_data_probes_v1.py`
  - Column-level stats for FRW data probes (e.g. `has_matter_era`, `has_late_accel`, `smooth_H2`, `frw_viable`, `data_ok`).
- `stage2/frw_data_probe_analysis/src/analyze_frw_empirical_anchor_v1.py`
  - Produces:
    - `stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_empirical_anchor_mask_v1.csv`
    - with column `in_empirical_anchor_box`.

**How to read:**

- `analyze_frw_data_probes_v1.py` tells you what the FRW toy filters are actually doing (what fraction pass basic probes).
- `analyze_frw_empirical_anchor_v1.py` identifies the subset of θ where the FRW toy background falls inside the empirical box.

At this point, you have:

- `frw_viable` mask (FRW toy internal viability),
- `in_toy_corridor` mask,
- `in_empirical_anchor_box` mask (FRW toy + simple anchor).

---

### 1.3 Mechanism + joint FRW/mechanism belts

**Goal:** Put the mechanism and FRW toy on a shared θ-grid and quantify their relationship.

Central object:

- `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv`

This table carries, per θ-index:

- θ, E_vac, omega_lambda, age_Gyr
- FRW masks (`frw_viable`, `lcdm_like`, `shape_and_viable`, `shape_and_lcdm`, `frw_data_ok`)
- Corridor flags (`in_toy_corridor`)
- Mechanism-side amplitudes and bounds:
  - `mech_baseline_A0`, `mech_baseline_A_floor`, `mech_baseline_bound`
  - `mech_binding_A0`, `mech_binding_A`, `mech_binding_bound`

Mechanism-side belt:

- `stage2/mech_measure_analysis/src/inventory_phase3_tables_v1.py`
  - Inventories Phase 3 tables and sizes.
- `stage2/mech_measure_analysis/src/analyze_mech_theta_gradients_v1.py`
  - Produces:
    - `stage2/mech_measure_analysis/outputs/tables/stage2_mech_rung7_theta_gradients_v1.csv`
  - Summarises θ-gradients of mechanism amplitudes across:
    - ALL_GRID
    - FRW_VIABLE
    - TOY_CORRIDOR
    - CORRIDOR_AND_VIABLE
    - CORRIDOR_AND_VIABLE_AND_ANCHOR

Anchor intersections on the joint grid:

- `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_intersections_v1.py`
  - Uses `in_empirical_anchor_box` to measure:
    - `EMPIRICAL_ANCHOR`
    - `FRW_VIABLE_AND_ANCHOR`
    - `CORRIDOR_AND_ANCHOR`
    - `CORRIDOR_AND_VIABLE_AND_ANCHOR`
- `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_kernel_v1.py`
  - Identifies contiguous θ-index segments inside:
    - FRW_VIABLE ∧ TOY_CORRIDOR ∧ ANCHOR
  - Outputs:
    - counts, segment ranges, and distances to θ★.
- `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_profiles_v1.py`
  - Produces set-wise averages and spreads for mechanism and FRW quantities:
    - `stage2_joint_mech_frw_anchor_profiles_v1.csv`
- `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_sensitivity_v1.py`
  - Varies the empirical box width and reports:
    - how `n_in_box` and overlaps change with scale.
- `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_mech_contrast_v1.py`
  - Compares mechanism amplitudes between:
    - CORRIDOR_AND_VIABLE_AND_ANCHOR vs CORRIDOR_AND_VIABLE_NOT_ANCHOR.

**How to read:**

- Intersections + kernel:
  - Answer: *Does the internal FRW corridor actually hit the empirical box at all? If yes, is that region fragmented or corridor-like?*
- Profiles:
  - Answer: *How special are the θ-points that survive all three filters, as seen from the mechanism side?*
- Sensitivity:
  - Answer: *Does the picture collapse if you shrink or expand the empirical box slightly?*
- Gradients:
  - Answer: *Are mechanism amplitudes smooth or wild across θ, especially within the triple-intersection region?*

These are **still diagnostic**: they clarify geometry and mechanism behaviour near the empirical anchor.

---

### 1.4 External FRW host cross-checks

**Goal:** Compare the Phase 4 FRW toy ages to a simple analytic FRW host, and define a “host-calibrated” consistency subset.

Core scripts:

- `stage2/external_frw_host/src/compute_analytic_frw_ages_v1.py`
  - Uses ω_Λ from the joint grid and an analytic flat FRW integrator to compute:
    - `age_Gyr_host`
  - Produces:
    - `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung1_age_crosscheck_v1.csv`
- `stage2/external_frw_host/src/analyze_external_frw_age_contrast_v1.py`
  - Summarises:
    - `age_Gyr_diff = age_host - age_repo`
    - `age_Gyr_rel_diff = (age_host - age_repo) / age_repo`
  - Over sets:
    - ALL_GRID, FRW_VIABLE, CORRIDOR_AND_VIABLE, CORRIDOR_AND_VIABLE_AND_ANCHOR
- `stage2/external_frw_host/src/flag_age_consistent_subset_v1.py`
  - Flags θ where:
    - `|age_host - age_repo| / age_repo ≤ threshold` (e.g. 20%)
  - Produces:
    - `stage2_external_frw_rung3_age_consistency_mask_v1.csv`
  - And reports:
    - How many θ are “host-consistent” in ALL_GRID, FRW_VIABLE, CORRIDOR_AND_VIABLE, etc.

**How to read:**

- Cross-check:
  - If FRW toy ages disagree violently with the simple FRW host, the toy’s age column is not trustworthy as an anchor coordinate.
- Consistency mask:
  - Defines a **host-calibrated corridor**: places where Phase 4’s toy ages can be read as reasonable FRW ages.

---

### 1.5 Host-calibrated corridor and host anchor

**Goal:** Combine host age consistency with the empirical anchor and FRW/mechanism structure.

Core scripts:

- `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_host_corridor_v1.py`
  - Uses:
    - Joint grid
    - Age consistency mask (`age_consistent_rel_le_20pct`)
    - Anchor mask (`in_empirical_anchor_box`)
  - Defines and summarises:
    - `HOST_CALIBRATED_CORRIDOR` (age-consistent set)
    - Intersections with FRW_VIABLE, TOY_CORRIDOR, ANCHOR.
- `stage2/external_frw_host/src/analyze_external_frw_host_anchor_v1.py`
  - Infers a host-based empirical anchor box from the FRW anchor (same ω_Λ range, mapped age range in `age_Gyr_host`).
  - Produces:
    - `stage2_external_frw_host_anchor_mask_v1.csv`
    - with `in_host_empirical_anchor_box`.
- `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_host_anchor_intersections_v1.py`
  - Intersections between:
    - HOST_ANCHOR
    - FRW_VIABLE
    - TOY_CORRIDOR
    - CORRIDOR_AND_VIABLE_AND_HOST_ANCHOR

**How to read:**

- `HOST_CALIBRATED_CORRIDOR`:
  - Where FRW toy ages agree with an analytic host to within the chosen tolerance.
- Host anchor:
  - The “same” empirical anchor, but expressed in host-age space.
- Intersections:
  - A stricter sanity slice:
    - FRW_VIABLE ∧ TOY_CORRIDOR ∧ HOST_ANCHOR (and optionally age-consistent).

At the current state, the key fact is that the original triple-intersection
(CORRIDOR ∧ FRW_VIABLE ∧ ANCHOR) lives far outside the host age-consistent region, which is itself a concrete diagnostic result.

---

### 1.6 Visuals and summaries

Some Stage 2 scripts produce diagnostic plots under:

- `stage2/joint_mech_frw_analysis/outputs/figures/`
  - e.g. `stage2_joint_mech_frw_anchor_overview_v1.png`

These show:

- θ vs E_vac, θ vs age_Gyr, θ vs mechanism amplitudes,
- with FRW viability / corridor / anchor / host masks overlaid.

Screenshots or exports of these plots are **allowed as visual aids**, but do not carry additional claims beyond what the tables already encode.

---

## 2. Sanity checks before trusting a Stage 2 result

Before using Stage 2 outputs in any narrative (Phase 4/5 text, talks, etc.), perform at least:

1. **Regenerate key tables**
   - Re-run the relevant Stage 2 scripts from a clean state.
   - Confirm that:
     - `stage2_joint_theta_grid_v1.csv` row count and columns match expectations.
     - FRW tables in Phase 4 have not changed silently.

2. **Check joins and keys**
   - Ensure that **all** Stage 2 joins use:
     - either `theta_index` or `theta` as documented,
     - never a mixture of mismatched keys.
   - If any Stage 2 script shows a warning about missing join keys or drops rows, treat that as a potential bug.

3. **Row counts across belts**
   - For a fixed grid size (currently 2048 θ-values):
     - ALL_GRID should always report `n_theta = 2048`.
     - FRW_VIABLE, TOY_CORRIDOR, EMPIRICAL_ANCHOR, HOST_ANCHOR, etc., should give **sensible fractions** that match the values printed at runtime.

4. **Cross-check endpoints**
   - Use `STAGE2_ENDPOINTS_AND_TABLES_MAP_v1.md` as the canonical reference for:
     - expected filenames,
     - column names,
     - and interpretations.
   - Avoid ad hoc string-typing of column names in new scripts: copy from the map.

5. **Spot-check slices**
   - For any striking Stage 2 result (e.g. “18 θ-points survive all filters”), spot-check:
     - the corresponding rows in the joint grid,
     - their FRW and mechanism values,
   - to ensure they genuinely satisfy the boolean masks.

---

## 3. How to talk about Stage 2 results (without over-claiming)

Stage 2 results are allowed to support **shapes of claims** like:

- “On the current θ-grid, FRW viability occupies ~50% of points, while the toy corridor occupies ~58%.”
- “The intersection of toy corridor, FRW viability, and the empirical anchor contains 18 out of 2048 grid points (≈0.9%), arranged in two short θ-segments.”
- “Within that triple-intersection, mechanism amplitudes are smooth in θ and occupy a narrow sub-range of the global amplitude distribution.”
- “When we require the toy FRW ages to agree with a simple analytic FRW host to within 20%, the previously identified triple-intersection completely disappears.”

Stage 2 results are **not** allowed to support claims like:

- “We have predicted the observed value of Λ (or H₀) from first principles.”
- “The axiom is confirmed by cosmological data.”
- “This model is empirically ruled in/out by Planck/BAO/SN.”

Those would require:

- a fully defined mapping to standard cosmological parameters,
- a real data likelihood pipeline (Cobaya/CosmoSIS-style),
- a new Phase/Stage with explicit data-contact gates.

---

## 4. Extension slots – how to add new belts safely

When adding new Stage 2 analyses:

1. **Create a dedicated submodule**
   - e.g. `stage2/external_cosmo_hosts/`, `stage2/flavour_probe_analysis/`, etc.
   - Mirror the current style:
     - `src/` for scripts,
     - `config/` for parameters,
     - `outputs/tables/` and `outputs/figures/` for results.

2. **Define endpoints first**
   - Update:
     - `stage2/docs/STAGE2_ENDPOINTS_AND_TABLES_MAP_v1.md`
   - Add:
     - new table names,
     - column names,
     - a short description of what each column means,
     - and which upstream tables it depends on.

3. **Keep data contact gated**
   - Any script that touches external data or sophisticated cosmology codes (CLASS, CCL, Cobaya, CosmoSIS, etc.) must:
     - live in a clearly marked Stage 2/Stage II submodule,
     - have its own “scope and non-claims” header at the top of the doc.

4. **Log promotions explicitly**
   - If any Stage 2 diagnostic is to be promoted into a Phase-level narrative (e.g. Phase 4 or 5 text), this must be:
     - logged in `PROGRESS_LOG.md`,
     - tied to a specific commit and Stage 2 rung,
     - and reflected in the relevant Phase alignment doc.

---

## 5. Current “big picture” from Stage 2

At the time of this document (see `PROGRESS_LOG.md` for exact dates / commits), Stage 2 tells a **consistent but deliberately modest story**:

- There **is** a non-trivial FRW toy corridor in θ-space.
- The empirical anchor box in `(omega_lambda, age_Gyr)` carves out a **small, structured subset** of that corridor (two short segments, 18/2048 θ-points).
- Mechanism amplitudes in that subset are:
  - smooth in θ,
  - and occupy a narrow slice of the global mechanism range.
- However, when we:
  - cross-check FRW ages against an analytic FRW host,
  - and require ≤20% relative age agreement,
  the triple-intersection between corridor, FRW viability, and the empirical anchor disappears.

Interpretation:

- The **current toy implementation** can produce:
  - FRW-like corridors,
  - and small anchor-overlaps *within its own internal age definition*,
- but these overlaps do **not** survive a simple external FRW age calibration.

This is already a meaningful outcome:

- It **does not** kill the axiom,
- It **does** put pressure on:
  - the FRW toy mapping,
  - the choice of empirical anchor box,
  - and the corridor construction.

Stage 2’s next role is to guide:

- **targeted refinements** (better FRW toy, alternative anchors, refined mechanism corridors),
- without breaking Phase 0 governance or over-claiming.

