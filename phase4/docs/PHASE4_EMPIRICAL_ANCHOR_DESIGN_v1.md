# Phase 4 – Empirical Anchor Design (Draft, non-binding)

Status: **DRAFT – design note, non-binding**  
Scope: document how Phase 4 exposes a small, background-only “empirical anchor” hook via the FRW toy pipeline and Stage 2 belts, without changing any Phase-level claims.

---

## 1. Purpose and scope

This note records:

- which FRW-facing quantities in Phase 4 are used as **anchor observables**,  
- how a small **empirical box** is defined in Stage 2, and  
- how the associated Stage 2 belts interrogate that box relative to:
  - FRW viability,
  - the Phase 4 toy corridor, and
  - the non-cancelling mechanism.

This is **not** a data–fit or likelihood engine. It is a controlled way to ask:

> “Given our current θ-grid, FRW toy background, and mechanism measure, does there exist any θ-region that looks vaguely compatible with a simple background cosmology box?”

All contact with real cosmological constraints remains **Stage 2 diagnostic** and lives under explicit Stage 2 docs.

---

## 2. Anchor observables and FRW columns

Phase 4 already exposes a θ-grid with FRW-like background quantities in

- `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`

The relevant columns for the anchor design are:

- `theta` – the θ coordinate on the grid,
- `omega_lambda` – the effective vacuum-density fraction used in the FRW toy,
- `age_Gyr` – the Phase 4 FRW toy age of the Universe in Gyr,
- Boolean masks such as:
  - `has_matter_era`,
  - `has_late_accel`,
  - `smooth_H2`,
  - `frw_viable`.

**Anchor observables**:

- An **effective vacuum fraction**: `omega_lambda`,
- A **background age**: `age_Gyr`.

No perturbation-level observables (Cℓ, P(k), etc.) are used here.

---

## 3. Empirical anchor box (Stage 2 config)

The actual numerical specification of the “empirical box” lives in Stage 2 as a small config file:

- `stage2/frw_data_probe_analysis/config/empirical_anchor_box_v1.json`

Conceptually this config encodes:

- a 1D allowed band for `omega_lambda`, and
- a 1D allowed band for `age_Gyr`,

and defines a Boolean **anchor mask**:

- `in_empirical_anchor_box = 1` if and only if
  - `omega_lambda` lies inside the configured ΩΛ-band, and
  - `age_Gyr` lies inside the configured age band.

The JSON file is the **single source of truth** for the numerical limits.  
This design note only fixes the *shape* of the construction, not the precise numbers.

---

## 4. Stage 2 belts that use the anchor

The anchor box itself is applied and studied in Stage 2, using the Phase 4 FRW tables and the joint mech–FRW grid.

### 4.1. FRW-anchor mask

Module:

- `stage2/frw_data_probe_analysis/src/analyze_frw_empirical_anchor_v1.py`

Responsibilities:

- Reads:
  - `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`,
  - `stage2/frw_data_probe_analysis/config/empirical_anchor_box_v1.json`.
- Computes:
  - `in_empirical_anchor_box` for each θ on the FRW grid.
- Writes:
  - `stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_empirical_anchor_mask_v1.csv`
    with `theta`, `omega_lambda`, `age_Gyr`, and the anchor mask.

This belt is **purely diagnostic**: it marks where the toy FRW background falls inside the chosen ΩΛ–age box.

### 4.2. Joint mech–FRW anchor intersections

Module:

- `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_intersections_v1.py`

Responsibilities:

- Reads the joint θ-grid:

  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv`

  which already contains:

  - FRW-side columns: `omega_lambda`, `age_Gyr`, `frw_viable`,
  - mechanism-side columns: `mech_baseline_*`, `mech_binding_*`,
  - corridor masks: `in_toy_corridor`, `shape_and_viable`, etc.

- Joins in the anchor mask from:

  - `stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_empirical_anchor_mask_v1.csv`.

- Constructs and counts the sets:

  - `ALL_GRID`,
  - `FRW_VIABLE`,
  - `TOY_CORRIDOR`,
  - `EMPIRICAL_ANCHOR` (the anchor box),
  - `FRW_VIABLE_AND_ANCHOR`,
  - `CORRIDOR_AND_ANCHOR`,
  - `CORRIDOR_AND_VIABLE_AND_ANCHOR`.

Result:

- A table  
  `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_intersections_v1.csv`  
  showing that the empirical box is small (18 θ points, ≈ 0.9% of the grid) and entirely contained in
  - FRW-viable, and
  - the toy corridor.

### 4.3. Kernel structure and sensitivity

Additional Stage 2 scripts study:

- **Kernel structure**  
  (`analyze_joint_mech_frw_anchor_kernel_v1.py`):
  - identifies contiguous θ-segments within  
    `CORRIDOR_AND_VIABLE_AND_ANCHOR`,
  - finds two disjoint 9-point segments, neither containing θ★,
  - records their θ-ranges and distances to θ★.

- **Anchor profiles**  
  (`analyze_joint_mech_frw_anchor_profiles_v1.py`):
  - computes mean/min/max of FRW quantities and mechanism measures across:
    - ALL_GRID,
    - FRW_VIABLE,
    - TOY_CORRIDOR,
    - EMPIRICAL_ANCHOR,
    - CORRIDOR_AND_VIABLE_AND_ANCHOR.

- **Sensitivity to box width**  
  (`analyze_joint_mech_frw_anchor_sensitivity_v1.py`):
  - scales the half-widths of the anchor box by factors (e.g. 0.5, 1.0, 1.5),
  - measures how the size of the anchor set and its intersections change,
  - confirming that the 18-point kernel is small but not a single-θ needle.

- **Mechanism contrast**  
  (`analyze_joint_mech_frw_anchor_mech_contrast_v1.py`):
  - compares mechanism measures (e.g. `mech_baseline_A0`, `mech_binding_A`) on:
    - the corridor ∧ viable set,
    - the corridor ∧ viable ∧ anchor kernel,
    - the complementary corridor ∧ viable \ anchor set.

All of these are **Stage 2**, **diagnostic** and live under Stage 2 documentation.

---

## 5. Interpretation and guardrails

### 5.1. What the anchor is allowed to say

Within Phase 4, the empirical anchor is only allowed to support statements of the form:

- “Relative to our current FRW toy background and θ-grid, there exists a **small** set of θ points (the 18-point kernel) where:
  - the FRW toy background passes our internal viability checks,
  - the θ-points lie inside a simple ΩΛ–age box drawn from background cosmology,
  - and the mechanism measure is within a narrow band.”

or

- “This small kernel splits into two disconnected segments in θ, neither of which contains θ★; any future θ★-locking would have to reconcile with this structure.”

These are **shape and structure statements** about the toy environment and masks, not claims of “fitting the Universe”.

### 5.2. What the anchor is not allowed to claim

The anchor **does not**:

- give θ★ a measured value,
- declare that the current implementation of the axiom “explains” ΩΛ or the age of the Universe,
- serve as a likelihood or posterior over θ,
- justify promoting any θ-region to a Phase 4 or Phase 5 claim about real cosmology.

Any serious, data-level contact (CMB, BAO, SN, growth, etc.) belongs in a **separate Stage II pipeline** (e.g. based on CLASS/CCL/Cobaya/CosmoSIS), with its own gates and contracts.

---

## 6. Forward-looking notes

This anchor design is deliberately minimal and conservative. It prepares the ground for two future directions:

1. **Internal refinement** (inside the current program):
   - refine the toy FRW integrator and viability masks,
   - study how stable the 18-point kernel is under:
     - improved FRW modelling,
     - different θ-grids,
     - alternate approximate empirical boxes.

2. **External host / Stage II contact**:
   - use external FRW hosts to calibrate the toy ages and ΩΛ mapping (cf. `stage2/external_frw_host/*`),
   - eventually, if desired, introduce a genuinely data-calibrated anchor box in a Stage II pipeline.

Until then, this document acts as a **design fence**: it keeps the empirical anchor concept visible and well documented, while preventing it from being over-interpreted in the Phase 3/4/5 narrative.

