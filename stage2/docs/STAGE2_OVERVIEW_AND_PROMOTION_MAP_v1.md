# Stage 2 overview and promotion map (v1)

**Date:** 2026-01-09  
**Scope:** Summarize the Stage 2 “analysis belt” as implemented so far, and
classify which Stage 2 results are (a) promotion candidates for Phase 4/5 text,
(b) support-only diagnostics, or (c) parked items for later work.

Stage 2 is deliberately *downstream-only*: it never mutates Phase-3/4 code or
claims. It takes the existing artifacts (Phase 3 measures, Phase 4 FRW masks,
etc.) and asks:

> “Given what Phase 3/4 already produced, what structure can we see in θ,
>  and which pieces look robust and scientifically ‘claimable’ if we ever
>  decide to promote them into the main line of the program?”

---

## 1. FRW corridor analysis (stage2/frw_corridor_analysis)

**Rungs implemented:**

- Rung 1 – Source inventory
  - CSV/boolean mask inventory from Phase 4:
    - `phase4_F1_frw_viability_mask.csv`
    - `phase4_F1_frw_lcdm_probe_mask.csv`
    - `phase4_F1_frw_shape_probe_mask.csv`
    - `phase4_F1_frw_data_probe_mask.csv`
- Rung 2 – Boolean census
  - Counts of `True`/`False` per boolean-like column.
- Rung 3 – FRW family definitions
  - Families on a 2048-point θ grid:
    - **F1_FRW_VIABLE**: `frw_viable`
    - **F2_LCDM_LIKE**: `lcdm_like`
    - **F3_TOY_CORRIDOR**: `in_toy_corridor`
    - **F4_CORRIDOR_AND_VIABLE**: `in_toy_corridor ∧ frw_viable`
    - **F5_CORRIDOR_AND_LCDM**: `in_toy_corridor ∧ lcdm_like`
    - **F6_DATA_OK**: `data_ok`
  - Fractions of the grid (≈, from the Phase 4 snapshot):
    - F1: 1016 / 2048 ≈ 0.496
    - F2: 63 / 2048 ≈ 0.031
    - F3: 1186 / 2048 ≈ 0.579
    - F4: 154 / 2048 ≈ 0.075
    - F5: 40 / 2048 ≈ 0.020
    - F6: 0 / 2048 = 0.0
- Rung 4 – Family overlap table
  - Pairwise intersections of {F1,…,F6}.
- Rung 5 – θ-histogram and (ω_Λ, E_vac) scatter **(PDF)**
  - For all families, using the Phase 4 shape-probe table:
    - `stage2_frw_corridor_family_theta_hist_v1.pdf`
    - `stage2_frw_corridor_family_omega_lambda_scatter_v1.pdf`
- Rung 6 – Contiguity analysis
  - For each family, decompose `θ`-support into contiguous segments.
  - Snapshot:
    - F1 has **1** contiguous block (1016 points).
    - F2–F5 have **2** segments each.
- Rung 7 – Stride-robustness
  - Re-sample families with strides {1, 2, 4, 8} in index space.
  - For each stride, record:
    - effective grid size,
    - number of `True` points,
    - fraction of subgrid / full grid,
    - number of segments.
  - Fractions of subgrid remain stable across strides, segments counts are
    stable for this snapshot.
- Rung 8 – Smoothing robustness
  - Apply simple 1D smoothing in θ (window sizes 1, 3, 5).
  - For each family, record:
    - pre/post `True` counts,
    - segment counts,
    - Jaccard similarity of the masks.
  - In this snapshot, Jaccard ≈ 1.0 for all tested windows: smoothing does
    not change the masks, which is a nontrivial sanity check on
    discretization artifacts.
- Rung 9 – Segment geometry and θ* alignment
  - For each family, record segment geometry (start/end/length).
  - Compute the point in each family closest to
    θ⋆ ≈ φ^φ ≈ 2.178458 on the 2048-point grid.
  - In the current Phase 4 snapshot:
    - **F1_FRW_VIABLE** has a point at θ ≈ 2.178253 (|Δ| ≈ 2.0×10⁻⁴).
    - The more constrained families (F4, F5) typically align closest to a
      different peak near θ ≈ 3.30.

### 1.1 FRW corridor — promotion assessment

- **Promotion candidates (text/figures):**
  - The **family definitions** `{F1,…,F5}` and their fractions of the θ grid.
  - The **θ-histogram** and **(ω_Λ, E_vac)-scatter** figures (Rung 5) as
    candidates for:
    - Option A: a compact corridor subsection in Phase 4/5 text.
    - Option B: a dedicated FRW/corridor-focused Stage/Phase later on.
  - The **contiguity profile** (one long FRW-viable band with embedded
    subsets) is a conceptually clear story and could be safely referenced
    once we decide how much FRW content belongs in the main line.
- **Support-only diagnostics:**
  - Detailed overlap tables, stride robustness, smoothing robustness, and
    segment geometries are **support** for “this is not a grid artifact”
    and can stay in Stage 2 / appendix-like locations.
- **Parked items:**
  - **F6_DATA_OK** is currently empty (no θ passes `frw_data_ok`), so any
    data-conditioned corridor story is explicitly **parked** until we
    re-open and tune the Phase 4 data gate.

---

## 2. Mech/measure analysis (stage2/mech_measure_analysis)

**Rungs implemented:**

- Rung 1 – Phase 3 table inventory
  - Catalogued:
    - `mech_baseline_scan.csv` (+ diagnostics JSON),
    - `mech_binding_certificate.csv` (+ diagnostics JSON),
    - `phase3_measure_v1_hist.csv`,
    - `phase3_measure_v1_stats.json`.
- Rung 2 – Column stats
  - For each numeric column: min, max, mean, std, approximate support.
  - For JSON stats: reduced to synthetic scalar summaries.
- Rung 3 – Probability-like candidate detection
  - From the column stats, identified **11** probability-like candidates
    (roughly “in [0,1] and non-degenerate”).
- Rung 4 – Measure vs flag split
  - Split probability-like candidates into:
    - **6 scalar measure candidates** (continuous-ish),
    - **2 flag candidates** (essentially boolean).
- Rung 5 – θ-profiles for candidate measures
  - For each of the 8 candidates:
    - sample the measure vs θ on the 2048-point Phase 3 grid,
    - record basic shape descriptors (e.g. monotonic, peaked, flat).
- Rung 6 – Preferred measure set
  - From Rung 5 shapes, select a **small preferred set** of measure
    candidates that:
    - behave smoothly in θ,
    - are not trivially flat or binary,
    - preserve the intended “probability-like” range.

### 2.1 Mech/measure — promotion assessment

- **Promotion candidates:**
  - The existence of a **shortlist of smooth, probability-like
    measure candidates** rooted in Phase 3 runs is a robust Stage 2 result.
  - These can become:
    - inputs to joint mech–FRW constructions,
    - eventual “measure on θ-space” building blocks in later phases.
- **Support-only diagnostics:**
  - Full column-by-column stats and raw probability-like candidate lists.
  - These remain in Stage 2 as forensic/diagnostics artifacts.
- **Parked items:**
  - We **do not yet interpret** any particular measure candidate as “the”
    measure or prior over θ. At Stage 2 we only say:
    > “Phase 3 contains several well-behaved, probability-like scalars that
    >  are compatible with being interpreted *as* measures in principle.”
  - The promotion of a particular candidate to a *claim* (e.g. “this is the
    preferred measure”) is explicitly deferred to later phases, after more
    physics and consistency checks.

---

## 3. Joint mech–FRW analysis (stage2/joint_mech_frw_analysis)

**Rungs implemented:**

- Rung 1 – Joint θ-grid assembly
  - Constructed a **joint 2048-point θ grid** that aligns:
    - Phase 4 FRW tables:
      - `frw_shape_probe_mask`,
      - `frw_data_probe_mask`,
      - `frw_viability_mask`,
      - `frw_lcdm_probe_mask`;
    - Phase 3 mechanical tables:
      - `mech_baseline_scan.csv`,
      - `mech_binding_certificate.csv`.
  - Verified θ-alignment to within a numerical tolerance (≈ 10⁻⁸) across
    all sources.
  - Built a single table:
    - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv`
    - 2048 rows, 17 columns, including:
      - `theta_index`, `theta`, `E_vac`, `omega_lambda`, `age_Gyr`,
      - FRW flags: `in_toy_corridor`, `frw_viable`, `lcdm_like`,
        `shape_and_viable`, `shape_and_lcdm`, `frw_data_ok`,
      - mechanical amplitudes: `mech_baseline_A0`, `mech_baseline_A_floor`,
        `mech_baseline_bound`, `mech_binding_A0`, `mech_binding_A`,
        `mech_binding_bound`.
- Rung 2 – FRW family summaries on the joint grid
  - Reconstructed the same families {ALL_GRID, FRW_VIABLE, LCDM_LIKE,
    TOY_CORRIDOR, CORRIDOR_AND_VIABLE, CORRIDOR_AND_LCDM,
    FRW_VIABLE_AND_DATA_OK} on the joint grid and verified their fractions
    match the Stage 2 FRW corridor analysis.
- Rung 3 – Global correlations
  - Computed Pearson correlations (and covariances) between:
    - `{E_vac, omega_lambda, age_Gyr}` and
    - `{mech_baseline_A0, mech_baseline_A_floor, mech_baseline_bound,
       mech_binding_A0, mech_binding_A, mech_binding_bound}`.
  - Snapshot behavior:
    - **Strong positive correlation** between `E_vac`, `omega_lambda` and
      the “A0/A_floor” amplitudes (r ≈ 0.94–0.98).
    - **Strong negative correlation** between these cosmological scalars
      and “bound”-type columns (r ≈ -0.56 globally).
    - **Age_Gyr** shows the corresponding opposite sign correlations
      (older universes where Λ is smaller correlate with smaller A0/A_floor
      and larger bound, etc.).
- Rung 4 – Family-conditioned correlations
  - Same correlation machinery, but restricted to FRW families (e.g.
    FRW_VIABLE, TOY_CORRIDOR, CORRIDOR_AND_VIABLE, CORRIDOR_AND_LCDM).
  - This checks whether the global correlations survive inside the more
    constrained subsets.

### 3.1 Joint mech–FRW — promotion assessment

- **Promotion candidates:**
  - The existence of a *joint θ-grid* where FRW scalars and mechanical
    amplitudes are consistently aligned is a robust infrastructural result.
  - The fact that there are **strong, coherent correlations** between
    `{E_vac, ω_Λ, age_Gyr}` and mechanical amplitudes is nontrivial and may
    warrant:
    - a figure or brief subsection in Phase 4/5 (Option A), or
    - a dedicated future Stage/Phase focusing on the “mech ⇔ geometry”
      relation (Option B).
  - At Stage 2, we stop at *correlation*; no causal or interpretative claim.
- **Support-only diagnostics:**
  - Detailed per-family correlation tables.
- **Parked items:**
  - Any narrative like “mechanics explains Λ” is **explicitly not claimed**
    at Stage 2; these correlations are *candidates for future explanation*,
    not explanations themselves.

---

## 4. FRW data-probe audit (stage2/frw_data_probe_analysis)

**Rungs implemented:**

- Rung 1 – Column stats
  - Stats for:
    - `has_matter_era`,
    - `has_late_accel`,
    - `smooth_H2`,
    - `frw_viable`,
    - `data_ok`.
- Rung 2 – Viability cross-tables
  - For each probe column, built the 2×2 table with `frw_viable`.
  - Snapshot:
    - `has_matter_era` and `smooth_H2` are **always true**.
    - `has_late_accel` and `frw_viable` are identical in this snapshot:
      - 1016 points true, 1032 false.
    - `data_ok` is **always false**:
      - `FRW_VIABLE ∧ DATA_OK` is empty.

### 4.1 FRW data probes — promotion assessment

- **Promotion candidates:**
  - Text-level statement that:
    > In the current Phase 4 snapshot, the FRW viability mask is equivalent
    >  to “late acceleration present,” under the always-true matter-era and
    >  smoothness sanity checks.
- **Support-only diagnostics:**
  - Exact 2×2 tables, raw CSVs.
- **Parked items:**
  - Any data-conditioned corridor (`frw_data_ok = True`) is **not yet
    available**: the aggregate data flag is currently never satisfied.
  - The tuning and interpretation of `data_ok` is explicitly deferred to a
    future revision of Phase 4.

---

## 5. Stage 2 as a whole — status and role

**Status:**

- Stage 2 has been implemented for the main Phase 3/4 artifacts that matter
  for θ-space structure:
  - FRW corridors,
  - mechanical/measure candidates,
  - joint mech–FRW alignment,
  - FRW data-probe status.
- All rungs are:
  - downstream-only,
  - reproducible by single-script calls,
  - logged in `PROGRESS_LOG.md`,
  - producing explicit CSV/PDF artifacts.

**Role in the larger phased program:**

- Stage 2 is now a **living but coherent belt** between:
  - the existing Phase 3/4 numerical pipeline, and
  - future Phase 4/5 text and any new phases (measure, data, mech–FRW, etc.).
- It provides:
  - A **corridor vocabulary** (F1–F5 families and their grid fractions).
  - A **mech/measure candidate set** (well-behaved probability-like columns).
  - A **joint θ-grid** with strong correlations between geometry and mech
    amplitudes.
  - A **clear statement of the data gate** (`frw_data_ok` currently closed).

**Promotion map summary (v1):**

- **Safe to promote as text/figures (Option A candidates):**
  - FRW families and their fractions, plus the Stage 2 FRW corridor figures.
  - The existence of smooth probability-like measure candidates from Phase 3
    (without choosing a “winner” yet).
  - The existence of strong correlations between cosmological scalars and
    mechanical amplitudes on the joint grid.
  - The statement about `frw_viable` ≈ “late acceleration present” in the
    current Phase 4 snapshot.
- **Support-only / appendix-level:**
  - Detailed overlap/robustness/segment tables.
  - Full column inventories and raw candidate listings.
  - Per-family correlation tables.
- **Parked for future phases:**
  - Any definitive choice of a single “preferred” measure over θ.
  - Any data-conditioned corridor (requires `frw_data_ok` > 0).
  - Any mechanistic explanation of Λ or FRW structure derived from the
    joint correlations.

This document should be read as a **map of what Stage 2 actually did**, not
a promise that all of it will be promoted. Future rungs and phases can move
items between “support,” “promotion,” and “parked” as the program evolves.

