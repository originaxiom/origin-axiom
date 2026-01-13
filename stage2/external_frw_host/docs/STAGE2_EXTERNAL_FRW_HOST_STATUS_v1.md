# Stage 2 – External FRW host status (v1)

Status: **diagnostic / non-claiming**. This note records Stage 2 rungs that
compare the Phase 4 FRW toy outputs to a simple external FRW "host" model.

The goal is not to promote new claims, but to document where the current FRW toy
corridor and empirical anchor sit relative to a standard flat-FRW age
calibration.

---

## Rung X1 – Analytic flat-FRW ages on the joint θ-grid

Script:
- `stage2/external_frw_host/src/compute_analytic_frw_ages_v1.py`

Inputs:
- Joint mech–FRW grid:
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv`
- Uses the Phase 4 `omega_lambda` column as the FRW dark-energy density parameter.

Method:
- Define a standard flat FRW background with matter + Λ.
- Compute a dimensionless age integral for each `omega_lambda` on the θ-grid.
- Calibrate a single multiplicative scale factor so that the external host age
  matches (in the least-squares sense) the Phase 4 toy age on the FRW-viable
  subset.
- Record, for each θ:
  - `age_Gyr` (Phase 4 toy),
  - `age_Gyr_host` (analytic host),
  - `age_Gyr_diff = age_Gyr_host - age_Gyr`,
  - `age_Gyr_rel_diff = age_Gyr_diff / age_Gyr`,
  - `frw_viable` flag from the joint grid.

Outputs:
- Table:
  - `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung1_age_crosscheck_v1.csv`
- Diagnostics (illustrative values for this repo state):
  - FRW-viable subset size: ~1000 points.
  - Typical absolute relative difference on the FRW-viable subset is O(0.2):
    the FRW toy ages are in the right order of magnitude but not tightly
    calibrated.

Interpretation:
- The Phase 4 toy FRW ages are broadly consistent in *scale* with a simple
  flat-FRW host once a global scale factor is applied, but individual θ-points
  can differ by O(10%)–O(100%) depending on the region of θ-space.

---

## Rung X2 – Age contrast across key θ-families

Script:
- `stage2/external_frw_host/src/analyze_external_frw_age_contrast_v1.py`

Inputs:
- `stage2_external_frw_rung1_age_crosscheck_v1.csv`

Method:
- Group rows into:
  - `ALL_GRID`,
  - `FRW_VIABLE`,
  - `CORRIDOR_AND_VIABLE`,
  - `CORRIDOR_AND_VIABLE_AND_ANCHOR`
  (where the last two use the existing Stage 2 families:
   toy corridor, FRW viability, and empirical anchor kernel).
- For each group, compute:
  - mean and std of `age_Gyr_diff`,
  - mean and std of `age_Gyr_rel_diff`,
  - min / max of `age_Gyr_diff` and `age_Gyr_rel_diff`.

Outputs:
- `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung2_age_contrast_v1.csv`
- For the current repo state (illustrative numbers):
  - ALL_GRID:   ⟨Δage⟩ ~ -8.4 Gyr, ⟨|Δage| / age_repo⟩ ~ 0.53
  - FRW_VIABLE: ⟨Δage⟩ ~ -2.5 Gyr, ⟨|Δage| / age_repo⟩ ~ 0.18
  - CORRIDOR_AND_VIABLE:
      large negative age differences, typical relative mismatch ≳ 0.8
  - CORRIDOR_AND_VIABLE_AND_ANCHOR:
      similarly large negative mismatch (repo ages much larger than host).

Interpretation:
- Within the FRW-viable set as a whole, the toy ages are within ~20% of the
  analytic host on average.
- However, the *specific* corridor that is both FRW-viable and inside the toy
  corridor lives in a region where the Phase 4 toy ages are systematically much
  larger than the host ages (by ~80% on average).
- The empirical anchor kernel (corridor ∧ FRW-viable ∧ data-box) sits in the
  same mis-calibrated region.

---

## Rung X3 – Age-consistency mask (20% threshold)

Script:
- `stage2/external_frw_host/src/flag_age_consistent_subset_v1.py`

Inputs:
- Joint grid:
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv`
- Host ages:
  - `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung1_age_crosscheck_v1.csv`
- Empirical anchor mask:
  - `stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_empirical_anchor_mask_v1.csv`

Method:
- Join the three tables on `(theta_index, theta)`.
- Define:
  - `age_rel_err_abs = |age_Gyr_rel_diff|`.
  - `age_consistent_rel_le_20pct = (age_rel_err_abs <= 0.20)`.
- For each of the sets
  - `ALL_GRID`,
  - `FRW_VIABLE`,
  - `CORRIDOR_AND_VIABLE`,
  - `CORRIDOR_AND_VIABLE_AND_ANCHOR`,
  compute how many θ-points satisfy the 20% age-consistency criterion.

Outputs:
- Row-level table:
  - `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung3_age_consistency_mask_v1.csv`
- Summary for current repo state:
  - Total grid: 2048 points.
  - Age-consistent (≤20%):
    - ALL_GRID:                778 points (~0.38 of grid).
    - FRW_VIABLE:              778 points (~0.38 of grid).
    - CORRIDOR_AND_VIABLE:       0 points.
    - CORRIDOR_AND_VIABLE_AND_ANCHOR: 0 points.

Interpretation:
- There is a substantial band of θ-values where the Phase 4 toy ages are
  consistent with a simple flat-FRW host at the 20% level, and all of these
  points are FRW-viable.
- None of these age-consistent points lie inside the current toy corridor
  (FRW-viable ∧ in_toy_corridor), and none lie inside the empirical anchor
  kernel (corridor ∧ FRW-viable ∧ data-box).
- In other words, the existing toy corridor and its empirical anchor kernel
  occupy a region of θ-space where the Phase 4 ages are systematically
  mis-calibrated relative to a standard FRW age, even though many other
  FRW-viable θ-points *are* well-calibrated.

---

## Working interpretation for Stage 2

- The external FRW host rungs do **not** overturn the axiom or the mechanism,
  but they do show that:
  - The current toy corridor is not aligned with the simplest FRW age
    calibration, even though FRW-viable, age-consistent θ-points exist.
- For future work:
  - The present corridor should be treated as a *historical toy corridor* whose
    FRW age scale is known to be off.
  - Any future “host-calibrated corridor” should be introduced as a **separate
    Stage 2 object**, defined transparently in terms of:
    - FRW viability,
    - toy corridor membership (if retained),
    - age-consistency with an external FRW host,
    - and any empirical anchor boxes applied.

