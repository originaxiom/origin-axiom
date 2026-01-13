# Stage 2 – FRW Empirical Anchor and External FRW Host Status (v1)

**Status:** Diagnostic Stage 2 belt (A1–A8, HX1–X3). Non-claim, non-binding.  
**Scope:** Map and interrogate a small FRW/age “empirical anchor” region for the current Phase 3–4 toy pipeline, and quantify how badly (or well) it survives contact with a simple external FRW host.

---

## 1. Scope and non-claims

This belt does **not**:

- Claim that the current toy FRW implementation matches real cosmological data.
- Claim a precise prediction for \(\Omega_\Lambda\), \(H_0\), or the age of the Universe.
- Promote any Stage 2 diagnostic into Phase-level claims.

It **does**:

- Define a concrete FRW/age “empirical anchor box” in the current Phase 4 toy space.
- Track the corresponding \(\theta\)-points through the joint mechanism–FRW grid.
- Compare toy FRW ages to a simple external FRW background host.
- Make explicit where the current toy FRW ages are *in tension* with a calibrated FRW background.

All results are **diagnostic only** and live entirely inside Stage 2.

---

## 2. Inputs, scripts, and tables

### 2.1 FRW toy anchor (A1–A4/A6/A7/A8)

**Inputs**

- Phase 4 FRW toy table:
  - `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`
    - Contains: \(\theta\), `E_vac`, `omega_lambda`, `age_Gyr`, and FRW-shape/viability flags.

**Scripts**

- `stage2/frw_data_probe_analysis/src/analyze_frw_empirical_anchor_v1.py`
  - Reads the Phase 4 FRW table and applies a small box in \((\omega_\Lambda, \text{age}_\mathrm{Gyr})\).
  - Config: `stage2/frw_data_probe_analysis/config/empirical_anchor_box_v1.json`.
- `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_intersections_v1.py`
- `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_kernel_v1.py`
- `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_profiles_v1.py`
- `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_sensitivity_v1.py`
- `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_mech_contrast_v1.py`
- `stage2/mech_measure_analysis/src/analyze_mech_theta_gradients_v1.py`

**Outputs (key tables)**

- FRW anchor mask:
  - `stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_empirical_anchor_mask_v1.csv`
    - Columns include: `theta_index`, `theta`, `omega_lambda`, `age_Gyr`, `frw_viable`, `in_empirical_anchor_box`.
    - Size: 2048 rows; **18** rows with `in_empirical_anchor_box = True` (~0.0088 of the grid).
- Joint intersections:
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_intersections_v1.csv`
    - Confirms:
      - `FRW_VIABLE`: 1016/2048 (~0.496)
      - `TOY_CORRIDOR`: 1186/2048 (~0.579)
      - `EMPIRICAL_ANCHOR`: 18/2048 (~0.0088)
      - All anchor points lie in `FRW_VIABLE ∧ TOY_CORRIDOR`.
- Anchor kernel (segments in \(\theta\)):
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_kernel_v1.csv`
    - Finds 2 contiguous 9-point segments in \(\theta\):
      - Segment 1: \(\theta \in [0.6289, 0.6535]\) (index 205–213).
      - Segment 2: \(\theta \in [3.3073, 3.3318]\) (index 1078–1086).
      - Neither segment contains \(\theta_\star\); both sit \(O(1)\) radians away from it.
- Anchor profiles:
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_profiles_v1.csv`
    - Summaries for:
      - `ALL_GRID`, `FRW_VIABLE`, `TOY_CORRIDOR`,
      - `EMPIRICAL_ANCHOR`,
      - `FRW_VIABLE_AND_ANCHOR`,
      - `CORRIDOR_AND_ANCHOR`,
      - `CORRIDOR_AND_VIABLE_AND_ANCHOR`.
    - For the 18-point anchor (and its intersections) we get:
      - \(\omega_\Lambda\) tightly clustered near ~0.69 (std ≈ 0.016).
      - Toy `age_Gyr` tightly clustered near ~13.50 Gyr (std ≈ 0.05 Gyr).
      - Mechanism measure (`mech_*` columns) in a narrow band around ~0.046 with small scatter.
- Anchor sensitivity:
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_sensitivity_v1.csv`
    - Varies the anchor half-widths by factors 0.5, 1.0, 1.5.
    - Counts:
      - scale = 0.50 → 8 points survive all filters.
      - scale = 1.00 → 18 points.
      - scale = 1.50 → 26 points in the box, of which 24 lie in `FRW_VIABLE ∧ TOY_CORRIDOR`.
- Mechanism contrast and gradients:
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_mech_contrast_v1.csv`
    - Compares mechanism measures across:
      - `ALL_GRID`, `FRW_VIABLE`,
      - `CORRIDOR_AND_VIABLE` (154 points),
      - `CORRIDOR_AND_VIABLE_AND_ANCHOR` (18 points).
    - In the 18-point kernel:
      - `mech_baseline_A0` ≈ `mech_binding_A0` ≈ 0.0461 with σ ≈ 2.7×10⁻⁴, spanning ~[0.0457, 0.0465].
  - `stage2/mech_measure_analysis/outputs/tables/stage2_mech_rung7_theta_gradients_v1.csv`
    - Shows that in the anchor kernel, |θ-gradients of the mechanism measure| are O(0.035), comparable to the corridor edges: the kernel is not a perfectly flat plateau.

---

## 3. External FRW host cross-check (HX1–HX3)

### 3.1 Host age computation

**Scripts**

- `stage2/external_frw_host/src/compute_analytic_frw_ages_v1.py`
  - Computes an analytic flat-FRW age \(t_0(\Omega_\Lambda)\) on the *same* θ-grid as the joint table.
  - Calibrates a single overall scale so that a reference subset matches the toy ages in aggregate.

**Output**

- `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung1_age_crosscheck_v1.csv`
  - Columns: `theta_index`, `theta`, `omega_lambda`, `age_Gyr` (toy), `age_Gyr_host`, `age_Gyr_diff`, `age_Gyr_rel_diff`, `frw_viable`.

On the full grid and main subsets:

- ALL_GRID (2048 points):
  - ⟨age_host − age_repo⟩ ≈ −8.41 Gyr
  - ⟨|Δage| / age_repo⟩ ≈ 0.53
- FRW_VIABLE (1016 points):
  - ⟨age_host − age_repo⟩ ≈ −2.49 Gyr
  - ⟨|Δage| / age_repo⟩ ≈ 0.18
- CORRIDOR_AND_VIABLE (154 points):
  - ⟨age_host − age_repo⟩ ≈ −11.86 Gyr
  - ⟨|Δage| / age_repo⟩ ≈ 0.84
- CORRIDOR_AND_VIABLE_AND_ANCHOR (18 points):
  - ⟨age_host − age_repo⟩ ≈ −10.87 Gyr
  - ⟨|Δage| / age_repo⟩ ≈ 0.81

So: **inside the corridor and especially inside the 18-point kernel, the host FRW ages are systematically much smaller than the toy ages** (by ~11 Gyr).

### 3.2 Age-consistency mask (HX3)

**Script**

- `stage2/external_frw_host/src/flag_age_consistent_subset_v1.py`
  - Adds a boolean `age_consistent_rel_le_20pct` using |age_host − age_repo| / age_repo ≤ 0.2.

**Output**

- `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung3_age_consistency_mask_v1.csv`

Summary:

- ALL_GRID: 778/2048 points (≈ 0.38) are age-consistent at the 20% level.
- FRW_VIABLE: the same 778 points (all lie within the FRW-viable set).
- CORRIDOR_AND_VIABLE: **0** points.
- CORRIDOR_AND_VIABLE_AND_ANCHOR: **0** points.

In other words: **the current toy FRW corridor (and its 18-point kernel) lives entirely outside the 20% age-consistent region** of the analytic FRW host.

### 3.3 Host anchor derived from FRW anchor

**Script**

- `stage2/external_frw_host/src/analyze_external_frw_host_anchor_v1.py`
  - Reads:
    - Host cross-check table: `stage2_external_frw_rung1_age_crosscheck_v1.csv`
    - FRW empirical anchor table: `stage2_frw_empirical_anchor_mask_v1.csv`
  - Infers a **host-space anchor box** by taking the min/max of:
    - `omega_lambda` on the FRW anchor points
    - `age_Gyr_host` on those same points.

**Output**

- `stage2/external_frw_host/outputs/tables/stage2_external_frw_host_anchor_mask_v1.csv`
  - Columns: `theta_index`, `theta`, `omega_lambda`, `age_Gyr`, `age_Gyr_host`, `frw_viable`, `in_host_empirical_anchor_box`.
  - Rows: 2048, with **18** host-anchor points (same θ-indices as the FRW anchor).

Inferred host anchor box:

- \(\omega_\Lambda \in [0.664228, 0.716531]\) — matches the FRW anchor range.
- \(t_{0,\mathrm{host}} \in [2.57, 2.70]\) Gyr — *very different* scale from the toy FRW ages (~13.5 Gyr) on the same θ-points.

Intersections on the joint grid:

- `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_host_anchor_intersections_v1.csv`
  - ALL_GRID: 2048
  - FRW_VIABLE: 1016
  - TOY_CORRIDOR: 1186
  - HOST_ANCHOR: 18
  - FRW_VIABLE_AND_HOST_ANCHOR: 18
  - CORRIDOR_AND_HOST_ANCHOR: 18
  - CORRIDOR_AND_VIABLE_AND_HOST_ANCHOR: 18

So the 18-point FRW anchor kernel maps to **the same 18 points** in the host table, but with host ages near ~2.6 Gyr instead of ~13.5 Gyr.

---

## 4. Interpretation and next steps (diagnostic only)

1. **The FRW empirical anchor exists but is small.**  
   - 18/2048 grid points survive all of:
     - FRW viability,
     - toy corridor membership,
     - and the current \((\omega_\Lambda, \text{age}_\mathrm{Gyr})\) box.
   - These points form two short contiguous θ-segments and exhibit a narrow, non-flat band of mechanism measures.

2. **The analytic FRW host strongly disagrees with the toy ages in the corridor and anchor.**  
   - In the 18-point kernel, host ages are ≈2.6 Gyr, toy ages ≈13.5 Gyr.
   - At the 20% relative level, *no* corridor-and-viable points are age-consistent with the host.

3. **What this does and does not mean.**
   - This is **not** evidence for or against the axiom itself; it is a statement about the current *implementation* and scaling of the Phase 4 FRW toy.
   - It tells us that we cannot treat the current toy `age_Gyr` column as a physically normalized age observable. Any future contact with real cosmological ages must go through a host-normalized layer.

4. **Planned follow-ups (future belts, not yet implemented).**
   - Make the FRW toy → host mismatch explicit in Phase 4 docs (non-claims / reproducibility notes).
   - Introduce a host-native anchor (using realistic ΛCDM-like age/ΩΛ constraints) and treat the toy FRW ages as scaffolding only.
   - Audit FRW toy code for scaling/normalization choices and ensure any future “real data” contact is hosted directly on validated FRW tools, not on toy ages.

This doc is meant as a *snapshot* of where the empirical anchor and external FRW host belt stands as of 2026-01-13. Any promotion of these diagnostics into Phase-level claims must go through the existing Phase 0 governance gates.
