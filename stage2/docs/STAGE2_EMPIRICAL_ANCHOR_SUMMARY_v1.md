# Stage 2 – Empirical FRW anchor (background cosmology box, v1)

Status: Stage 2 diagnostic rung (A1–A4); downstream-only; no promotion to phase claims.

## Scope

This Stage 2 rung introduces a simple empirical FRW anchor on the existing Phase 4 FRW toy grid and joint mech–FRW grid and asks whether there is any nontrivial overlap between:
- the FRW-viable band produced by the Phase 4 FRW toy pipeline,
- the Stage 2 toy θ-corridor, and
- a small “background cosmology” box in \\\( (\omega_\Lambda, t_0) \\\).

The goal is to test whether the current axiom + mechanism + FRW mapping is immediately incompatible with basic background cosmology, or whether a non-empty but constrained overlap exists, without touching real likelihoods or external cosmology codes.

## Inputs

- Phase 4 FRW toy grid (2048-point θ grid):
  - `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv` (columns include `theta`, `E_vac`, `omega_lambda`, `age_Gyr`, shape flags)
- Stage 2 FRW corridor masks:
  - `stage2/frw_corridor_analysis/` outputs (in particular the `in_toy_corridor` mask that is already carried into the joint grid)
- Stage 2 joint mech–FRW grid:
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv` (columns include `theta`, `E_vac`, `omega_lambda`, `age_Gyr`, `in_toy_corridor`, `frw_viable`, `lcdm_like`, FRW shape flags, and mechanism amplitudes)
- Anchor configuration:
  - `stage2/frw_data_probe_analysis/config/empirical_anchor_box_v1.json` (defines a small box in \\\( (\omega_\Lambda, t_0) \\\), treated as a proxy for a background-cosmology consistency region)
- Stage 2 empirical anchor mask table:
  - `stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_empirical_anchor_mask_v1.csv` (boolean mask on the 2048-point θ grid)

## Method (A1–A4)

1. **A1 – Define empirical FRW anchor.**  
   Chose a small box in \\\( (\omega_\Lambda, t_0) \\\) based on background-cosmology plausibility (central values and tolerances encoded in `empirical_anchor_box_v1.json`). This is treated as a toy background-cosmology region, not as a full likelihood or Planck-level constraint.

2. **A2 – Compute empirical anchor mask on the FRW grid.**  
   `stage2/frw_data_probe_analysis/src/analyze_frw_empirical_anchor_v1.py`:
   - Reads the FRW toy table `phase4_F1_frw_shape_probe_mask.csv`.
   - Applies the empirical box cuts in \\\( (\omega_\Lambda, t_0) \\\).
   - Writes `stage2_frw_empirical_anchor_mask_v1.csv` with a boolean mask on the 2048-point θ grid.

3. **A3 – Count empirical-anchor survivors.**  
   The A2 script reports:
   - grid size: 2048 θ values,
   - empirical anchor survivors: 18,
   - `in_anchor` fraction ≈ 0.0088.  
   At this stage we already know that the anchor box is non-empty but highly selective.

4. **A4 – Intersect empirical anchor with FRW viability and the toy corridor on the joint grid.**  
   `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_intersections_v1.py`:
   - Reads the joint grid `stage2_joint_theta_grid_v1.csv` (2048 rows).
   - Merges the empirical anchor mask from `stage2_frw_empirical_anchor_mask_v1.csv` by θ.
   - Uses three boolean masks on the joint grid:
     - `frw_viable` (Phase 4 FRW viability flag),
     - `in_toy_corridor` (Stage 2 FRW corridor membership),
     - empirical anchor mask (auto-detected from the anchor table).
   - Computes cardinalities and fractions for:
     - ALL_GRID,
     - FRW_VIABLE,
     - TOY_CORRIDOR,
     - EMPIRICAL_ANCHOR,
     - FRW_VIABLE_AND_ANCHOR,
     - CORRIDOR_AND_ANCHOR,
     - CORRIDOR_AND_VIABLE_AND_ANCHOR.
   - Writes `stage2_joint_mech_frw_anchor_intersections_v1.csv`.

## Numerical results (A4)

On the current 2048-point θ grid:

- ALL_GRID:  
  - n = 2048  
  - frac_of_grid = 1.000000

- FRW_VIABLE:  
  - n = 1016  
  - frac_of_grid ≈ 0.4961

- TOY_CORRIDOR (`in_toy_corridor`):  
  - n = 1186  
  - frac_of_grid ≈ 0.5791

- EMPIRICAL_ANCHOR (background-cosmology box):  
  - n = 18  
  - frac_of_grid ≈ 0.0088

- FRW_VIABLE_AND_ANCHOR:  
  - n = 18  
  - frac_of_grid ≈ 0.0088

- CORRIDOR_AND_ANCHOR:  
  - n = 18  
  - frac_of_grid ≈ 0.0088

- CORRIDOR_AND_VIABLE_AND_ANCHOR:  
  - n = 18  
  - frac_of_grid ≈ 0.0088

In other words, on this grid and for this empirical box:

- every empirical-anchor point is FRW-viable (`FRW_VIABLE_AND_ANCHOR` = 18), and
- every empirical-anchor point lies inside the Stage 2 toy θ-corridor (`CORRIDOR_AND_ANCHOR` = 18),
- so the empirical anchor set is a strict subset of `FRW_VIABLE ∩ TOY_CORRIDOR` with 18 θ values out of 2048.

## Interpretation

Within the current toy FRW and corridor setup:

- The empirical FRW anchor box is **highly selective** but **non-empty**:
  - only ≈ 0.9% of the θ grid survive the background-cosmology box;
  - the axiom + mechanism + FRW mapping is not “automatically” compatible with background cosmology but is also not immediately ruled out.
- The empirical anchor does **not** pull the model outside its own FRW-viable band or outside the toy θ-corridor:
  - all anchor-compatible θ lie in `FRW_VIABLE ∧ TOY_CORRIDOR`.
- This rung therefore identifies a **small kernel** of θ values where:
  - the Phase 3 mechanism,
  - the Phase 4 FRW toy viability,
  - and a simple background-cosmology box all agree.

This is precisely the regime where further questions about fine-tuning, measure assignment over θ, and potential extensions (e.g. more realistic FRW data probes or external cosmology hosts) become scientifically meaningful, because the joint filters are neither trivially empty nor trivially full.

## Status and gating

- This empirical anchor rung is a **Stage 2 diagnostic only**:
  - it does not promote any particular θ value or corridor to a Phase 4 or Phase 5 claim;
  - it does not involve external cosmology pipelines (CLASS, CCL, Cobaya, etc);
  - it does not use full Planck/BAO/SN likelihoods, only a toy background box.
- Any future promotion of these results into:
  - Phase 4 text or figures, or
  - Phase 5 interface summaries,
  will require a separate, explicitly gated promotion rung (e.g. via `phase4/docs/PHASE4_FRW_PROMOTION_DESIGN_v1.md` and Stage 2 promotion design docs) and will remain subject to the Phase 0 contract (scope, non-claims, and reproducibility requirements).
