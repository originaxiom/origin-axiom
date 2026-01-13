# Stage 2 – Empirical FRW Anchor Belt (v1)

Status: **diagnostic / non-canonical**  
Date: 2026-01-12

This document summarises the Stage 2 **empirical FRW anchor belt**:
a downstream diagnostic that tests whether the existing Phase 3
mechanism + Phase 4 FRW toy corridor can pass through a small,
data-shaped box in \((\omega_\Lambda, t_0)\) space.

All anchor logic lives in Stage 2. Phase 4 only provides the FRW
background columns and masks; any empirical interpretation remains
downstream and non-binding.

See also:

- Phase-4 design stub: `phase4/docs/PHASE4_EMPIRICAL_ANCHOR_DESIGN_v1.md`
- FRW corridor belt: `stage2/frw_corridor_analysis/docs/STAGE2_FRW_CORRIDOR_OVERVIEW_v1.md`
- Joint mech–FRW belt: `stage2/joint_mech_frw_analysis/docs/STAGE2_JOINT_MECH_FRW_OVERVIEW_v1.md`
- Mech/measure belt: `stage2/mech_measure_analysis/docs/STAGE2_MECH_MEASURE_OVERVIEW_v1.md`

---

## 1. Anchor definition and inputs

### 1.1 FRW background source

The anchor uses the Phase 4 FRW shape/mask table:

- `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`

Key columns:

- `theta` – θ coordinate on the 2048-point grid  
- `E_vac` – vacuum scale inherited from Phase 3  
- `omega_lambda` – effective toy dark-energy fraction  
- `age_Gyr` – toy FRW background age in Gyr  
- FRW masks:
  - `frw_viable`
  - `has_matter_era`
  - `has_late_accel`
  - `smooth_H2`

These semantics are documented on the Phase-4 side in:

- `phase4/docs/PHASE4_EMPIRICAL_ANCHOR_DESIGN_v1.md`

### 1.2 Empirical box (Stage-2 config)

The empirical anchor box is defined by a small JSON config:

- `stage2/frw_data_probe_analysis/config/empirical_anchor_box_v1.json`

This file specifies:

- a central value and half-width for `omega_lambda`,
- a central value and half-width for `age_Gyr`,
- and a choice of whether both conditions must be satisfied
  simultaneously (AND) or not.

**Convention (v1):**

- The box is interpreted as a **toy “data-like” region** in
  \((\omega_\Lambda, t_0)\) space.
- The exact numerical values live in the JSON file; Stage 2 code only
  reads and applies them. No hard-coded anchors appear in Python.

---

## 2. Anchor belt rungs (code + outputs)

### 2.1 Rung A3 – FRW anchor mask

Script:

- `stage2/frw_data_probe_analysis/src/analyze_frw_empirical_anchor_v1.py`

Behaviour:

- Reads:
  - `phase4_F1_frw_shape_probe_mask.csv`
  - `empirical_anchor_box_v1.json`
- Constructs a Boolean column:
  - `in_empirical_anchor_box` (per θ)
- Writes:

  - `stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_empirical_anchor_mask_v1.csv`

Key facts (current snapshot):

- Grid size: 2048 θ-points.
- `in_empirical_anchor_box` true at **18** points (~0.88% of grid).

This rung defines the “anchor mask” that later rungs combine with FRW
viability and the toy corridor.

---

### 2.2 Rung A4 – Joint mech–FRW intersections

Script:

- `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_intersections_v1.py`

Inputs:

- Joint θ-grid:

  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv`

  containing:
  - Phase-4 FRW columns:
    - `omega_lambda`, `age_Gyr`
    - `frw_viable`, `in_toy_corridor`, etc.
  - Phase-3 mech scalars:
    - `mech_baseline_*`, `mech_binding_*`

- Anchor mask:

  - `stage2_frw_empirical_anchor_mask_v1.csv`

Outputs:

- `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_intersections_v1.csv`

Key counts (current snapshot):

- `ALL_GRID`: n = 2048 (1.000000)
- `FRW_VIABLE`: n = 1016 (0.496094)
- `TOY_CORRIDOR`: n = 1186 (0.579102)
- `EMPIRICAL_ANCHOR`: n = 18 (0.008789)
- `FRW_VIABLE_AND_ANCHOR`: n = 18
- `CORRIDOR_AND_ANCHOR`: n = 18
- `CORRIDOR_AND_VIABLE_AND_ANCHOR`: n = 18

So, in this snapshot:

> Every anchor point is simultaneously FRW-viable *and* inside the
> pre-existing toy corridor.

---

### 2.3 Rung A5b – Anchor kernel geometry

Script:

- `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_kernel_v1.py`

Behaviour:

- Restricts to the kernel:
  - `FRW_VIABLE ∧ in_toy_corridor ∧ in_empirical_anchor_box`
- Segments this set into **contiguous θ-index intervals**.
- Computes basic geometry for each segment.

Output:

- `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_kernel_v1.csv`
- PNG overview:

  - `stage2/joint_mech_frw_analysis/outputs/figures/stage2_joint_mech_frw_anchor_overview_v1.png`

Current kernel (2048-point grid):

- Total kernel size: n = 18
- Number of contiguous segments: 2

Segments:

1. Segment 1
   - `theta_index[205–213]`, n = 9
   - `theta ∈ [0.6289, 0.6535]` (approx; see CSV for exact values)
   - `contains_theta_star = False`
2. Segment 2
   - `theta_index[1078–1086]`, n = 9
   - `theta ∈ [3.3073, 3.3318]` (approx)
   - `contains_theta_star = False`

Both segments live **inside** the toy corridor, and both are FRW-viable.

---

### 2.4 Rung A6 – Kernel profiles

Script:

- `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_profiles_v1.py`

Behaviour:

- Joins the joint θ-grid with the anchor mask (by `theta`).
- For each of the following sets:

  - `ALL_GRID`
  - `FRW_VIABLE`
  - `TOY_CORRIDOR`
  - `EMPIRICAL_ANCHOR`
  - `FRW_VIABLE_AND_ANCHOR`
  - `CORRIDOR_AND_ANCHOR`
  - `CORRIDOR_AND_VIABLE_AND_ANCHOR`

  computes summary stats for:

  - `E_vac`, `omega_lambda`, `age_Gyr`
  - all mech scalars:
    - `mech_baseline_A0`, `mech_baseline_A_floor`,
      `mech_baseline_bound`,
    - `mech_binding_A0`, `mech_binding_A`,
      `mech_binding_bound`.

Output:

- `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_profiles_v1.csv`

Headline observation (current snapshot):

- In the `CORRIDOR_AND_VIABLE_AND_ANCHOR` set (n = 18):

  - `omega_lambda` has small spread around the anchor values,
  - `age_Gyr` has small spread,
  - the mech amplitudes form a **narrow sub-band** inside their
    corridor ranges, indicating that the anchor kernel corresponds
    to a fairly tight region in both FRW and mech space.

---

### 2.5 Rung A7 – Anchor sensitivity

Script:

- `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_sensitivity_v1.py`

Behaviour:

- Treats the anchor box half-widths as baseline and explores scaled
  variants:

  - e.g. scale factors 0.5, 1.0, 1.5

- For each scale, recomputes:

  - `n_in_box`
  - `n_box ∧ FRW_VIABLE`
  - `n_box ∧ in_toy_corridor`
  - `n_box ∧ FRW_VIABLE ∧ in_toy_corridor`

Output:

- `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_sensitivity_v1.csv`

Current snapshot (selected):

- scale = 0.50:
  - `n_in_box = 8`, all 8 FRW-viable, all 8 in corridor.
- scale = 1.00:
  - `n_in_box = 18`, all 18 FRW-viable, all 18 in corridor.
- scale = 1.50:
  - `n_in_box = 26`, all 26 FRW-viable, 24 of 26 in corridor.

Interpretation:

> The anchor kernel sits in a region where a moderate tightening or
> loosening of the empirical box still leaves a **non-empty, FRW-viable,
> corridor-compatible region**, but the counts are small and move
> discretely as the box expands.

---

### 2.6 Rung A8 – Mechanism contrasts

Script:

- `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_mech_contrast_v1.py`

Behaviour:

- Compares mech amplitudes across four sets:

  - `ALL_GRID`
  - `FRW_VIABLE`
  - `CORRIDOR_AND_VIABLE`
  - `CORRIDOR_AND_VIABLE_AND_ANCHOR`

- For each mech column, records:

  - `n_theta`, `frac_of_grid`, `mean`, `std`, `min`, `max`.

Output:

- `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_mech_contrast_v1.csv`

Qualitative picture (current snapshot):

- Going from `ALL_GRID` → `FRW_VIABLE` dramatically narrows the
  mech range.
- Restricting further to `CORRIDOR_AND_VIABLE` tightens the band again.
- The `CORRIDOR_AND_VIABLE_AND_ANCHOR` set is a **very narrow strip**
  in mech space, with small `std` and min/max tightly clustered.

This reinforces the view that:

> the empirical anchor picks out a small, structured patch of the
> mech-FRW landscape, rather than a random dusting of grid points.

---

### 2.7 Mech gradients (Stage 2 mech rung 7)

Script:

- `stage2/mech_measure_analysis/src/analyze_mech_theta_gradients_v1.py`

Behaviour:

- Uses the joint θ-grid and anchor mask to estimate finite-difference
  gradients of mech amplitudes with respect to θ:

  - across:
    - `ALL_GRID`
    - `FRW_VIABLE`
    - `TOY_CORRIDOR`
    - `CORRIDOR_AND_VIABLE`
    - `CORRIDOR_AND_VIABLE_AND_ANCHOR`

- Summarises `grad_mean`, `grad_std`, and several norms of the
  gradient (`abs_grad_mean`, `abs_grad_p95`, `abs_grad_max`).

Output:

- `stage2/mech_measure_analysis/outputs/tables/stage2_mech_rung7_theta_gradients_v1.csv`

Current snapshot:

- Gradients inside the anchor kernel are **non-zero and comparable
  in magnitude** to those in the surrounding corridor, i.e. the anchor
  does not sit in a perfectly flat region of mech space.

---

### 2.8 External FRW host cross-check (optional belt)

Script:

- `stage2/external_frw_host/src/compute_analytic_frw_ages_v1.py`

Behaviour:

- Uses a simple analytic flat-FRW integral to compute
  `age_Gyr_host(omega_lambda)` on the same θ-grid.
- Calibrates a global scale factor to relate the host’s dimensionless
  age to Gyr.
- Compares `age_Gyr_host` to the repo’s `age_Gyr` (Phase 4) on the
  FRW-viable subset.

Output:

- `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung1_age_crosscheck_v1.csv`

Current snapshot:

- Mean |age_host − age_repo| on FRW-viable set:
  - ~2.7 Gyr
- Max |age_host − age_repo|:
  - ~12.9 Gyr
- Mean relative difference:
  - ~0.20

Interpretation:

> The simple analytic host is **not** a calibrated model of the
> repo’s FRW toy; it serves here as a coarse, negative-result
> cross-check only. No promotion or empirical claim is made from
> this comparison.

---

## 3. Synthesis: what the anchor belt currently says (and does not say)

### 3.1 What it *does* say

On the current 2048-point θ-grid with the present empirical box:

- There exists a **small but non-empty kernel** of θ values (18 points)
  that satisfies:

  - Phase 4 FRW viability (`frw_viable = True`),
  - membership in the toy θ-corridor (`in_toy_corridor = True`),
  - and being inside the empirical \((\omega_\Lambda, t_0)\) box.

- This kernel consists of **two contiguous segments** in θ; both lie
  well away from θ★ (φ^φ) in the current grid.
- Within this kernel:
  - FRW quantities (`omega_lambda`, `age_Gyr`) show small spread,
  - mech amplitudes form a narrow sub-band,
  - gradients are non-zero but not pathological.

So, as a diagnostic statement:

> The current non-cancelling mechanism + FRW toy + empirical box do
> not immediately rule each other out; there is a small, structured
> region of θ where all three filters agree.

### 3.2 What it *does not* say

The anchor belt **does not** claim that:

- the empirical box is a faithful representation of real cosmological
  constraints,
- the surviving kernel is statistically preferred by real data,
- θ★ is selected, preferred, or singled out in any way,
- the current FRW toy is calibrated against external FRW codes or
  likelihood pipelines.

All such claims would require:

1. A dedicated FRW empirical anchor promotion gate (Phase 4/5 level),
2. Independent replication / cross-checks,
3. A much more careful data and host-physics design.

Until then, this belt remains a **Stage 2 diagnostic**: a structured
sanity check that the current machinery admits at least one small
region where:

- mechanism corridor,
- FRW viability,
- and a toy data-shaped box

can coexist without obvious fine-tuning.

---

## 4. Future work (anchor belt)

Potential future rungs include:

- refining the empirical box (or replacing it with multiple boxes),
- cross-checking FRW backgrounds against a more realistic external host,
- exploring whether the anchor kernel remains non-empty under:
  - grid refinement,
  - alternative θ-corridor definitions,
  - modest changes in the mechanism or FRW mapping,
- and, only under a dedicated promotion gate, deciding which parts of
  this belt (if any) should be mentioned in Phase 4/5 narrative.

For now, the empirical anchor belt is **accepted as Stage 2 diagnostic
infrastructure only**, with all promotion and physical interpretation
explicitly deferred.

