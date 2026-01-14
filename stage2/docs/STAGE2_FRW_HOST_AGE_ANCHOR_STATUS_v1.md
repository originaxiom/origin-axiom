# Stage 2 – FRW host age anchor status (v1)

**Scope.** This note records what we actually learned from the first FRW-host age anchor experiments in Stage 2, without over-claiming. It is a status + interpretation document, not a claims register.

---

## 1. Objects in play

We are comparing three ingredients:

1. **FRW toy background** (Phase 4)
   - Source: `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`
   - Columns of interest:
     - `theta` – the θ-grid (2048 points)
     - `omega_lambda` – toy vacuum fraction
     - `age_Gyr` – toy FRW age in Gyr
     - `frw_viable` – coarse “FRW background sane?” mask

2. **Analytic FRW host background** (Stage 2 external host)
   - Table: `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung1_age_crosscheck_v1.csv`
   - Built by `stage2/external_frw_host/src/compute_analytic_frw_ages_v1.py`
   - Columns of interest:
     - `theta_index`, `theta`
     - `omega_lambda`
     - `age_Gyr`       – toy FRW age (Phase 4)
     - `age_Gyr_host`  – analytic FRW host age for the same `omega_lambda`
     - `age_Gyr_diff`  – `age_Gyr_host - age_Gyr`
     - `age_Gyr_rel_diff` – relative difference
     - `frw_viable`

3. **Host background bridge + age-anchor masks**
   - Bridge table:
     - `stage2/external_frw_host/outputs/tables/stage2_external_frw_background_bridge_v1.csv`
     - Built by:
       - `stage2/external_frw_host/src/build_frw_background_bridge_v1.py`
     - Role: single table joining `theta`, `omega_lambda`, `age_Gyr` (toy), `age_Gyr_host` (host), and `frw_viable`.
   - Age-window summary:
     - `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung4_age_window_summary_v1.csv`
     - Built by:
       - `stage2/external_frw_host/src/analyze_external_frw_age_window_v1.py`
   - Host age-anchor mask:
     - Mask table:
       - `stage2/external_frw_host/outputs/tables/stage2_external_frw_host_age_anchor_mask_v1.csv`
     - Summary:
       - `stage2/external_frw_host/outputs/tables/stage2_external_frw_host_age_anchor_summary_v1.csv`
     - Built by:
       - `stage2/external_frw_host/src/flag_external_frw_host_age_anchor_v1.py`

The host age anchor is defined as the subset of θ where the **analytic FRW host** age lies in a small window around the observed Universe age:

- Host age window (Gyr):  
  \[
    t_0^\text{host} \in [13.3, 14.3]~\text{Gyr}.
  \]

This is *only* applied on the host side; the toy side is read but not used in the definition of the anchor.

---

## 2. Key numeric facts

### 2.1 Host age anchor and basic counts

From `stage2/external_frw_host/outputs/tables/stage2_external_frw_host_age_anchor_summary_v1.csv`:

- Grid size:
  - `ALL_GRID`: **2048** θ-points (100% of the grid)
- FRW viability:
  - `FRW_VIABLE`: **1016** / 2048 ≈ **0.496** of the grid
- Host age anchor:
  - `HOST_AGE_ANCHOR`: **34** / 2048 ≈ **0.0166** of the grid
  - `FRW_VIABLE_AND_HOST_AGE_ANCHOR`: **34** / 2048 ≈ **0.0166**
    - i.e. *all* host age-anchor points are already FRW-viable in the toy mask.
- Toy age window (for comparison only):
  - `TOY_AGE_WINDOW`: **100** / 2048 ≈ **0.0488**
  - `FRW_VIABLE_AND_TOY_AGE_WINDOW`: **100** / 2048 ≈ **0.0488**
    - These are θ where the **toy** age is near the observed value, regardless of host age.

Intersections with the θ-corridor (from `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_host_age_anchor_intersections_v1.csv`):

- `TOY_CORRIDOR`: **1186** / 2048 ≈ **0.5791**
- `HOST_AGE_ANCHOR`: **34** / 2048 ≈ **0.0166**
- `CORRIDOR_AND_HOST_AGE_ANCHOR`: **0**
- `CORRIDOR_AND_VIABLE_AND_HOST_AGE_ANCHOR`: **0**

> **Takeaway:**  
> The host age anchor is non-empty and lies entirely within the FRW-viable region, but it has **zero overlap** with the current θ-corridor carved out by the original FRW toy + mechanism pipeline.

### 2.2 Host vs toy ages inside the host age anchor

From `stage2/external_frw_host/outputs/tables/stage2_external_frw_host_age_anchor_profiles_v1.csv`:

- Number of θ in host age-anchor:
  - `n_theta = 34`
- θ-range in the host age anchor:
  - `theta_min ≈ 0.7885`
  - `theta_max ≈ 3.1723`
- Vacuum fraction:
  - `omega_lambda_mean ≈ 1.0533`
  - `omega_lambda_std ≈ 0.0317`
  - `omega_lambda_min ≈ 1.0015`
  - `omega_lambda_max ≈ 1.1047`
- Ages:
  - Host age:
    - `age_Gyr_host_mean ≈ 13.599`
    - `age_Gyr_host_std  ≈ 0.179`
    - `age_Gyr_host_min  ≈ 13.315`
    - `age_Gyr_host_max  ≈ 13.897`
  - Toy age at the same θ:
    - `age_Gyr_toy_mean ≈ 12.577`
    - `age_Gyr_toy_std  ≈ 0.069`
    - `age_Gyr_toy_min  ≈ 12.467`
    - `age_Gyr_toy_max  ≈ 12.691`
- Mechanism amplitudes in this band:
  - `mech_baseline_A0_mean ≈ 0.05125` with very small spread
  - `mech_baseline_A_floor_mean ≈ 0.05125` (same)
  - `mech_binding_A0_mean ≈ 0.05125`
  - `mech_binding_A_mean ≈ 0.05125`
  - `frac_in_toy_corridor = 0.0`

> **Takeaway (ages):**
> - Where the **host** FRW background says “this θ gives a universe with age ≈ 13.6 Gyr”,  
>   the **toy** FRW background at the same θ is sitting around ≈ 12.58 Gyr.
> - This is a **~1 Gyr systematic offset** in the age, *within* the small host age window.

> **Takeaway (corridor):**
> - None of these 34 host age-anchor θ-points lie in the existing **toy corridor**, even though they are FRW-viable and have well-behaved mechanism amplitudes.

---

## 3. What this *does* and *does not* say

### 3.1 What we can safely say

1. **Host age anchor is non-empty.**
   - There exist θ where the analytic FRW host background (given our ωΛ mapping) produces ages in the observational window \([13.3, 14.3]\) Gyr.

2. **These host age-anchor points are FRW-viable in the toy mask.**
   - The `FRW_VIABLE` mask does *not* rule them out; they pass the coarse FRW toy sanity checks.

3. **The toy FRW background is internally consistent but age-misaligned.**
   - At those same θ, the toy FRW age is systematically lower (≈ 12.6 Gyr) than the host age (≈ 13.6 Gyr).
   - This confirms that the toy FRW age calibration is **not** tuned to match a standard FRW background at ωΛ ≈ 1.05.

4. **The current toy corridor is not host-age anchored.**
   - The θ-corridor singled out by our original Phase 4 + Stage 2 FRW diagnostics does **not** intersect the host age anchor at all.
   - Any future corridor we call “empirically anchored” would have to:
     - either move towards this host age-anchor band,
     - or use a different observable / mapping as its anchor.

### 3.2 What we explicitly do *not* claim

- We do **not** claim that:
  - the present toy FRW age is “wrong” in an absolute sense,
  - the host age-anchor band is uniquely preferred,
  - θ-values outside this band are empirically ruled out.
- We also do **not** claim:
  - any full ΛCDM fit,
  - any confrontation with CMB/BAO/SN data,
  - or any prediction of exact cosmological parameters.

This is strictly a **background-age comparison** between:
- a toy FRW implementation baked into Phase 4, and
- a simple analytic FRW host model at the same ωΛ.

---

## 4. How this informs next steps

Given these results, the natural follow-ups (outside this document) are:

1. **FRW toy tightening (Phase 4 design docs + code):**
   - Make explicit in Phase 4 docs that the current FRW toy age is not calibrated to standard FRW at ωΛ ≈ 1.
   - Decide whether we want to:
     - (A) keep the toy as-is and treat host-age comparisons as a diagnostic only, or
     - (B) introduce a mild recalibration so that the toy’s FRW age converges towards the analytic host age in some region (e.g. near the host age anchor).

2. **Corridor re-interpretation (Stage 2 belts):**
   - Be explicit in Stage 2 runbooks that:
     - the original θ-corridor is a **toy FRW corridor**,  
     - not yet an “empirically age-anchored” corridor.
   - If we later define an “empirically anchored corridor”, it will have to use:
     - the host age-anchor mask, and/or
     - additional external constraints.

3. **Mechanism-side reflection:**
   - Note that mechanism amplitudes in the host age-anchor band cluster around ≈ 0.05125 with tiny spread.
   - This gives a concrete target region (in θ and in mechanism amplitude space) for any future mechanism refinements that might aim to cohabit with the host age-anchor.

---

## 5. Reproducibility checklist (for this status)

To reproduce the numbers referenced here:

1. Build the analytic FRW host ages and cross-check:
   - `python stage2/external_frw_host/src/compute_analytic_frw_ages_v1.py`

2. Build the background bridge:
   - `python stage2/external_frw_host/src/build_frw_background_bridge_v1.py`

3. Construct the host age anchor + summary:
   - `python stage2/external_frw_host/src/flag_external_frw_host_age_anchor_v1.py`

4. Build host age-anchor intersections with the joint θ-grid:
   - `python stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_host_age_anchor_intersections_v1.py`

5. Build the host age-anchor profiles:
   - `python stage2/external_frw_host/src/analyze_external_frw_host_age_anchor_profiles_v1.py`

All paths and counts in this note come directly from the outputs of those scripts as run on the current repo state.

