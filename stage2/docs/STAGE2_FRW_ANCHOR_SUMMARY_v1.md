# Stage 2 – FRW Empirical Anchor Summary (Draft, diagnostic only)

Status: **Stage 2 diagnostic – non-canonical, non-binding**  
Scope: summarise the Stage 2 “empirical anchor” belt built on top of the Phase 4 FRW toy, the joint mech–FRW grid, and the external FRW host cross-check. This document records *structure and diagnostics only* and is **not** a Phase 3/4/5 claim.

---

## 1. Inputs and configuration

This belt sits downstream of the canonical Phase 3 mechanism and Phase 4 FRW toy pipelines.

**Core inputs**

- Phase 4 FRW toy table:
  - `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`
  - columns: `theta`, `E_vac`, `omega_lambda`, `age_Gyr`, FRW shape and viability flags.
- Stage 2 joint θ-grid:
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv`
  - columns:
    - FRW side: `theta_index`, `theta`, `E_vac`, `omega_lambda`, `age_Gyr`,
      `frw_viable`, `lcdm_like`, `shape_and_viable`, `shape_and_lcdm`,
      `frw_data_ok`,
    - mechanism side: `mech_baseline_*`, `mech_binding_*`,
    - corridor mask: `in_toy_corridor`.

**Anchor configuration**

- Empirical box config:
  - `stage2/frw_data_probe_analysis/config/empirical_anchor_box_v1.json`
- Defines 1D bands in:
  - `omega_lambda` (Ω_Λ-like),
  - `age_Gyr` (FRW toy age),
- and the Boolean mask:
  - `in_empirical_anchor_box`.

All numerical limits live in the JSON config; this doc only records the *shape* of the construction and the observed outcomes.

---

## 2. Anchor masks and intersections

### 2.1 FRW anchor mask

Script:

- `stage2/frw_data_probe_analysis/src/analyze_frw_empirical_anchor_v1.py`

Outputs:

- `stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_empirical_anchor_mask_v1.csv`

Key counts on the 2048-point θ-grid:

- `ALL_GRID`: n = 2048, frac = 1.0
- `FRW_VIABLE`: n = 1016, frac ≈ 0.496
- `TOY_CORRIDOR`: n = 1186, frac ≈ 0.579
- `EMPIRICAL_ANCHOR` (`in_empirical_anchor_box`): n = 18, frac ≈ 0.0088

Already at this stage the anchor band is a **small** subset of the θ-grid (~0.9% of points).

### 2.2 Joint mech–FRW anchor intersections

Script:

- `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_intersections_v1.py`

Outputs:

- `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_intersections_v1.csv`

Using the joint grid and joining in the anchor mask, we count:

- `ALL_GRID`: n = 2048, frac = 1.000000
- `FRW_VIABLE`: n = 1016, frac ≈ 0.496094
- `TOY_CORRIDOR`: n = 1186, frac ≈ 0.579102
- `EMPIRICAL_ANCHOR`: n = 18, frac ≈ 0.008789
- `FRW_VIABLE_AND_ANCHOR`: n = 18, frac ≈ 0.008789
- `CORRIDOR_AND_ANCHOR`: n = 18, frac ≈ 0.008789
- `CORRIDOR_AND_VIABLE_AND_ANCHOR`: n = 18, frac ≈ 0.008789

Thus, in the current snapshot:

- the 18-point empirical-anchor band is **entirely contained** in both
  - the FRW viability region, and
  - the Phase 4 toy corridor,
- the intersection
  - `CORRIDOR_AND_VIABLE_AND_ANCHOR`
  is exactly the 18-point anchor set.

---

## 3. Kernel structure and sensitivity

### 3.1 Kernel segments in θ

Script:

- `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_kernel_v1.py`

Output:

- `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_kernel_v1.csv`

On `CORRIDOR_AND_VIABLE_AND_ANCHOR` (18 points), the code finds two contiguous θ-segments:

- Segment 1:
  - `theta_index` ∈ [205, 213] (9 points),
  - `theta` ∈ [0.628932, 0.653476],
  - contains θ★? **False**,
  - min |θ − θ★| ≈ 1.525 at θ ≈ 0.6535.
- Segment 2:
  - `theta_index` ∈ [1078, 1086] (9 points),
  - `theta` ∈ [3.307263, 3.331806],
  - contains θ★? **False**,
  - min |θ − θ★| ≈ 1.129 at θ ≈ 3.3073.

So the anchor kernel is:

- **disconnected** in θ (two 9-point blocks),
- **not** snapping onto θ★ in this FRW toy + anchor configuration.

A corresponding diagnostic figure lives at:

- `stage2/joint_mech_frw_analysis/outputs/figures/stage2_joint_mech_frw_anchor_overview_v1.png`

(showing θ vs `omega_lambda` and `age_Gyr`, with corridor, viability, anchor box, and kernel overlayed).

### 3.2 Sensitivity to box width

Script:

- `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_sensitivity_v1.py`

Output:

- `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_sensitivity_v1.csv`

For a set of scaling factors applied to the empirical box half-widths:

- scale = 0.50:
  - `n_in_box` = 8
  - `n_box ∧ FRW_VIABLE` = 8
  - `n_box ∧ CORRIDOR` = 8
  - `n_box ∧ CORRIDOR ∧ FRW_VIABLE` = 8
- scale = 1.00:
  - `n_in_box` = 18
  - `n_box ∧ FRW_VIABLE` = 18
  - `n_box ∧ CORRIDOR` = 18
  - `n_box ∧ CORRIDOR ∧ FRW_VIABLE` = 18
- scale = 1.50:
  - `n_in_box` = 26
  - `n_box ∧ FRW_VIABLE` = 26
  - `n_box ∧ CORRIDOR` = 24
  - `n_box ∧ CORRIDOR ∧ FRW_VIABLE` = 24

Interpretation:

- the anchor kernel is **not** a single-θ needle; it remains a **small band** even when the box is widened,
- however, the intersection remains a tiny fraction of the θ-grid (from 8 to 26 points out of 2048).

---

## 4. Mechanism-side profiles and contrast

### 4.1 Anchor profiles across FRW/mech sets

Script:

- `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_profiles_v1.py`

Output:

- `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_profiles_v1.csv`

For each set (ALL_GRID, FRW_VIABLE, TOY_CORRIDOR, EMPIRICAL_ANCHOR, CORRIDOR_AND_VIABLE_AND_ANCHOR), the table reports means and spreads of:

- FRW quantities: `E_vac`, `omega_lambda`, `age_Gyr`,
- mechanism quantities: `mech_baseline_A0`, `mech_baseline_A_floor`,
  `mech_baseline_bound`, `mech_binding_A0`, `mech_binding_A`, `mech_binding_bound`.

Illustrative numbers (rounded):

- `ALL_GRID`:
  - ⟨`omega_lambda`⟩ ≈ 0.663, std ≈ 0.061
  - ⟨`age_Gyr`⟩ ≈ 14.20, std ≈ 2.09
  - ⟨`mech_baseline_A0`⟩ ≈ 0.0388
- `FRW_VIABLE`:
  - ⟨`omega_lambda`⟩ ≈ 1.30, std ≈ 0.41
  - ⟨`age_Gyr`⟩ ≈ 12.22, std ≈ 0.95
  - ⟨`mech_baseline_A0`⟩ ≈ 0.0533
- `TOY_CORRIDOR`:
  - ⟨`omega_lambda`⟩ ≈ 0.160, std ≈ 0.151
  - ⟨`age_Gyr`⟩ ≈ 15.89, std ≈ 0.79
  - ⟨`mech_baseline_A0`⟩ ≈ 0.0269
- `EMPIRICAL_ANCHOR` (18 points):
  - ⟨`omega_lambda`⟩ ≈ 0.690, std ≈ 0.016
  - ⟨`age_Gyr`⟩ ≈ 13.50, std ≈ 0.049
  - ⟨`mech_baseline_A0`⟩ ≈ 0.0461, std ≈ 0.00027
- `CORRIDOR_AND_VIABLE_AND_ANCHOR` = same 18 points as above.

This shows:

- the anchor kernel picks out a **narrow Ω_Λ band** and a **narrow age band**,
- mechanism amplitudes on the kernel are **internally very tight**, but sit between:
  - the lower amplitudes typical of the full corridor, and
  - the higher amplitudes of the full FRW-viable band.

### 4.2 Mechanism contrast within the corridor

Script:

- `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_mech_contrast_v1.py`

Output:

- `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_mech_contrast_v1.csv`

Comparing mechanism statistics across:

- `ALL_GRID`,
- `FRW_VIABLE`,
- `CORRIDOR_AND_VIABLE` (154 points),
- `CORRIDOR_AND_VIABLE_AND_ANCHOR` (18 points).

Example for `mech_baseline_A0` (rounded):

- `ALL_GRID`: ⟨A0⟩ ≈ 0.0388
- `FRW_VIABLE`: ⟨A0⟩ ≈ 0.0533
- `CORRIDOR_AND_VIABLE`: ⟨A0⟩ ≈ 0.0423
- `CORRIDOR_AND_VIABLE_AND_ANCHOR`: ⟨A0⟩ ≈ 0.0461

So:

- FRW viability alone pushes A0 up,
- the corridor alone prefers lower A0,
- the anchor kernel sits as a **narrow interior slice** in A0 between the viable band and the broad corridor.

This is a structural, not causal, statement: the anchor kernel is a sharp subset where FRW viability, corridor membership, and mechanism amplitude all meet in a tight range.

---

## 5. External FRW host cross-check

To get a sense of how the FRW toy ages compare to a simple analytic FRW host, Stage 2 uses an external host belt.

### 5.1 Host ages and calibration

Script:

- `stage2/external_frw_host/src/compute_analytic_frw_ages_v1.py`

Output:

- `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung1_age_crosscheck_v1.csv`

This script:

- computes an analytic FRW age for flat matter+Λ models as a function of `omega_lambda`,
- calibrates a global scale factor so that one representative configuration matches the toy age in Gyr,
- compares **host** ages (`age_Gyr_host`) to **repo** ages (`age_Gyr`).

### 5.2 Age contrast across sets

Script:

- `stage2/external_frw_host/src/analyze_external_frw_age_contrast_v1.py`

Output:

- `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung2_age_contrast_v1.csv`

Key summary (rounded):

- `ALL_GRID` (2048 points):
  - ⟨Δage⟩ ≈ −8.41 Gyr,
  - ⟨|Δage|/age_repo⟩ ≈ 0.53.
- `FRW_VIABLE` (1016 points):
  - ⟨Δage⟩ ≈ −2.49 Gyr,
  - ⟨|Δage|/age_repo⟩ ≈ 0.18.
- `CORRIDOR_AND_VIABLE` (154 points):
  - ⟨Δage⟩ ≈ −11.86 Gyr,
  - ⟨|Δage|/age_repo⟩ ≈ 0.84.
- `CORRIDOR_AND_VIABLE_AND_ANCHOR` (18 points):
  - ⟨Δage⟩ ≈ −10.87 Gyr,
  - ⟨|Δage|/age_repo⟩ ≈ 0.81.

Interpretation:

- There is a **significant systematic mismatch** between the current FRW toy ages and the simple analytic host,
- especially on the corridor and anchor sets (relative differences ≳ 80%),
- the anchor kernel is **not** specially picked out by the host: it behaves similarly to the broader corridor∧viable set.

This is read as a **modeling/normalisation issue** in the present FRW toy and mapping, not as a physical exclusion of the axiom.

---

## 6. Interpretation and non-claims

At this Stage 2 rung, we record the following as **diagnostic outcomes**, *not* Phase-level claims:

1. **Small structured kernel**

   - A small (18-point) kernel exists where:
     - FRW toy is viable,
     - the Phase 4 toy corridor holds,
     - and the Ω_Λ–age pair lies inside a simple empirical box.
   - This kernel is disconnected in θ and does **not** contain θ★.

2. **Mechanism–FRW interplay**

   - Mechanism amplitudes on the kernel form a tight interior band compared to:
     - the broader FRW-viable region, and
     - the broader corridor region.
   - This shows **nontrivial structure**, but falls short of a canonical measure or θ-selection principle.

3. **Host mismatch**

   - External host ages disagree substantially with the FRW toy ages, particularly on the corridor and anchor sets.
   - Any future attempt to promote an “empirical anchor” into Phase 4/5 must first address this FRW toy vs host mismatch.

**Non-claims:**

- No claim is made that the current implementation of the axiom “predicts” Ω_Λ, the age of the Universe, or any cosmological observable.
- No claim is made that θ★ is selected or singled out by the anchor kernel.
- No likelihoods, posteriors, or parameter constraints are derived.

All anchor-related scripts and tables remain **Stage 2 diagnostics**. Any future promotion into Phase 4/5 text must pass through explicit promotion gates and updated alignment docs, and may require a more realistic FRW/cosmology host.

---

## 7. Pointers and navigation

Anchor and kernel belt:

- Config:
  - `stage2/frw_data_probe_analysis/config/empirical_anchor_box_v1.json`
- Tables:
  - `stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_empirical_anchor_mask_v1.csv`
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_intersections_v1.csv`
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_kernel_v1.csv`
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_profiles_v1.csv`
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_sensitivity_v1.csv`
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_mech_contrast_v1.csv`
- Figure:
  - `stage2/joint_mech_frw_analysis/outputs/figures/stage2_joint_mech_frw_anchor_overview_v1.png`

External FRW host belt:

- `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung1_age_crosscheck_v1.csv`
- `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung2_age_contrast_v1.csv`

Phase 4 design note:

- `phase4/docs/PHASE4_EMPIRICAL_ANCHOR_DESIGN_v1.md` – defines the Phase 4-facing interface and guardrails for any use of the anchor in Phase text.

