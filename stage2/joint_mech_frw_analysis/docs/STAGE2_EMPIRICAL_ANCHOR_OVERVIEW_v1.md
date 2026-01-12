# Stage 2 – Empirical anchor overview (FRW background + mechanism)

Status: Stage 2 diagnostic belt (A1–A8), downstream of Phase 3 and Phase 4. No Phase-level promotions; all results are internal diagnostics unless explicitly gated later.

This document summarises the empirical anchor belt that sits on top of the existing Stage 2 FRW corridor and joint mech–FRW analysis. The belt defines a simple background-cosmology anchor box in terms of the toy FRW quantities computed in Phase 4 and studies how this box intersects the toy corridor and the FRW viability band.

## A1 – Anchor design and scope

The anchor is defined at the level of background FRW diagnostics only. It uses:

- the toy FRW outputs from Phase 4:
  - `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv` (columns: `theta`, `E_vac`, `omega_lambda`, `age_Gyr`, shape flags),
- a small empirical box in the plane
  - `(omega_lambda, age_Gyr)`,

interpreted as a coarse stand-in for “ΛCDM-like vacuum fraction and age”. The exact numerical bounds live in:

- `stage2/frw_data_probe_analysis/config/empirical_anchor_box_v1.json`.

Scope and non-claims:

- This belt does **not** implement real Planck/BAO/SN likelihoods.
- The anchor box is a coarse, illustrative region; it is **not** a full data analysis.
- All results here are Stage 2 diagnostics: they inform future Phase 4/5 design, but do not change any Phase claims.

## A2 – Empirical anchor mask on the FRW grid

Script:

- `stage2/frw_data_probe_analysis/src/analyze_frw_empirical_anchor_v1.py`

Inputs:

- `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`
- `stage2/frw_data_probe_analysis/config/empirical_anchor_box_v1.json`

Output:

- `stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_empirical_anchor_mask_v1.csv` with a boolean column:
  - `in_empirical_anchor_box`: `True` for θ-points inside the anchor box.

Result:

- On the 2048-point θ grid, the anchor box selects:
  - `n_anchor = 18` points (`frac ≈ 0.0088` of the grid).

## A3 – Anchor intersections on the joint mech–FRW grid

Script:

- `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_intersections_v1.py`

Inputs:

- Joint grid: `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv`
- Anchor mask: `stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_empirical_anchor_mask_v1.csv`

Output:

- `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_intersections_v1.csv`

Key sets and sizes (n out of 2048):

- `FRW_VIABLE`: 1016 (`frac ≈ 0.4961`)
- `TOY_CORRIDOR`: 1186 (`frac ≈ 0.5791`)
- `EMPIRICAL_ANCHOR`: 18 (`frac ≈ 0.0088`)
- `FRW_VIABLE ∧ EMPIRICAL_ANCHOR`: 18 (`frac ≈ 0.0088`)
- `TOY_CORRIDOR ∧ EMPIRICAL_ANCHOR`: 18 (`frac ≈ 0.0088`)
- `FRW_VIABLE ∧ TOY_CORRIDOR ∧ EMPIRICAL_ANCHOR`: 18 (`frac ≈ 0.0088`)

Interpretation:

- Every anchored θ-point is simultaneously:
  - FRW-viable, and
  - inside the toy corridor.
- The empirical box carves out a small, non-empty kernel inside the intersection of FRW viability and the toy corridor.

## A4 – Anchor kernel structure in θ

Script:

- `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_kernel_v1.py`

Output:

- `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_kernel_v1.csv`

Key findings:

- The 18-point kernel splits into two contiguous θ-segments:
  - Segment 1: `theta_index[205–213]`, `n = 9`, `theta ∈ [0.6289, 0.6535]`
  - Segment 2: `theta_index[1078–1086]`, `n = 9`, `theta ∈ [3.3073, 3.3318]`
- The distinguished angle `theta_star ≈ 2.178458` does **not** lie in either segment.
- For each segment the minimum distance to `theta_star` is of order unity in θ.

Interpretation:

- The anchor kernel is not a single isolated needle; it appears as two small, well-separated θ-bands.
- On the present toy setup, nothing in the empirical anchor singles out `theta_star`; the anchor lives in different parts of the θ-grid.

## A5 – Anchor profiles in FRW and mechanism variables

Script:

- `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_profiles_v1.py`

Output:

- `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_profiles_v1.csv`

Selected summaries (means and ranges):

- All-grid (2048 points):
  - `omega_lambda`: mean ≈ 0.70, std ≈ 0.66, range ≈ [0.06, 1.69]
  - `age_Gyr`: mean ≈ 14.20, std ≈ 2.09, range ≈ [11.46, 16.48]
- FRW-viable band (1016 points):
  - `omega_lambda`: mean ≈ 1.30, range ≈ [0.30, 1.69]
  - `age_Gyr`: mean ≈ 12.22, range ≈ [11.46, 14.97]
- Toy corridor (1186 points):
  - `omega_lambda`: mean ≈ 0.16, range ≈ [0.06, 0.72]
  - `age_Gyr`: mean ≈ 15.89, range ≈ [13.40, 16.48]
- Empirical anchor kernel (18 points; same for all four anchor-intersection sets):
  - `omega_lambda`: mean ≈ 0.690, std ≈ 0.016, range ≈ [0.664, 0.717]
  - `age_Gyr`: mean ≈ 13.50, std ≈ 0.049, range ≈ [13.42, 13.58]
  - `E_vac`: mean ≈ 4.5×10⁻⁶ with very small scatter
  - Mechanism amplitudes (`mech_baseline_A0`, `mech_binding_A0`, etc.) lie in narrow interior bands; the kernel does not sit on any hard numerical bound.

Interpretation:

- The toy corridor by itself prefers low `omega_lambda` and large `age_Gyr`.
- The FRW-viable band prefers higher `omega_lambda` and lower `age_Gyr`.
- The empirical anchor kernel is a small intersection where:
  - `omega_lambda` is close to the data-inspired value (~0.69),
  - `age_Gyr` is close to the data-inspired value (~13.5 Gyr),
  - θ lies both in the toy corridor and in the FRW-viable band,
  - and the mechanism amplitudes are smooth and interior (no fine-tuning on numeric bounds).

## A6 – Sensitivity of the kernel to the anchor box

Script:

- `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_sensitivity_v1.py`

Output:

- `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_sensitivity_v1.csv`

Method:

- Infer a baseline bounding box in (`omega_lambda`, `age_Gyr`) that contains all anchored points.
- Define scaled boxes by multiplying the half-widths by scale factors `s ∈ {0.5, 1.0, 1.5}`.
- For each scale, count:
  - `n_in_box`
  - `n_in_box_and_frw_viable`
  - `n_in_box_and_corridor`
  - `n_in_box_and_corridor_and_frw_viable`.

Results (n out of 2048):

- `s = 0.5` (box shrunk by 2×):
  - `n_in_box = 8`
  - `n_box∧FRW = 8`
  - `n_box∧corridor = 8`
  - `n_box∧corridor∧FRW = 8`
- `s = 1.0` (baseline box):
  - `n_in_box = 18`
  - `n_box∧FRW = 18`
  - `n_box∧corridor = 18`
  - `n_box∧corridor∧FRW = 18`
- `s = 1.5` (box widened by 1.5×):
  - `n_in_box = 26`
  - `n_box∧FRW = 26`
  - `n_box∧corridor = 24`
  - `n_box∧corridor∧FRW = 24`

Interpretation:

- The empirical anchor kernel is **not** a single fine-tuned needle:
  - a 2× shrink in box size retains a compact 8-point core that is still FRW-viable and inside the toy corridor.
- The kernel does **not** immediately blow up into the whole corridor:
  - even at 1.5× box size, only 24 corridor points (out of 1186) lie in the scaled box and in the FRW-viable band.
- For all three scales, the anchored points remain strongly aligned with:
  - FRW viability, and
  - the toy corridor.

## A7 – Verdict and gating

On the current Phase 3 mechanism and Phase 4 toy FRW setup:

- The empirical anchor belt finds a **small but robust** intersection between:
  - the mechanism-preferred toy corridor,
  - the FRW-viable band, and
  - a simple background-cosmology–inspired box in `(omega_lambda, age_Gyr)`.
- This intersection appears as two short θ-bands, well separated from `theta_star`, with:
  - tight ranges in `omega_lambda`, `age_Gyr`, and mechanism amplitudes,
  - stability under moderate tightening/loosening of the anchor box.

Gating:

- These results remain **Stage 2 diagnostics only**.
- No new claims are added to Phase 3, Phase 4, or Phase 5.
- Any future use of this kernel in Phase text (e.g. Phase 4/5 figures or Phase 5 interface summaries) must pass through a separate promotion gate and be logged explicitly in `PROGRESS_LOG.md`.
