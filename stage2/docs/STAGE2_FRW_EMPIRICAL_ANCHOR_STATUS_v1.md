# Stage 2 – FRW empirical anchor belt (status v1)

**File:** `stage2/docs/STAGE2_FRW_EMPIRICAL_ANCHOR_STATUS_v1.md`  
**Scope:** Document the Stage 2 “empirical anchor” belt that links the Phase 4 FRW toy grid,
a simple \((\Omega_\Lambda, t_0)\) anchor box, the Phase 3 mechanism scalars, and an external
flat–FRW host age calculation. All results here are **diagnostic only**, downstream of
Phases 3–4.

---

## 1. Inputs and location in the program

**Upstream artifacts**

- Phase 3 mechanism outputs:
  - `phase3/outputs/tables/mech_baseline_scan.csv`
  - `phase3/outputs/tables/mech_binding_certificate.csv`
- Phase 4 FRW toy outputs:
  - `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`
  - `phase4/outputs/tables/phase4_F1_frw_viability_mask.csv`

**Joint grid and Stage 2 belts**

- Joint mech–FRW θ-grid:
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv`
- Stage 2 FRW corridor belt:
  - `stage2/frw_corridor_analysis/` (rungs 1–9; viability, LCDM-like, toy corridor, etc.)
- Stage 2 mech/measure belt:
  - `stage2/mech_measure_analysis/` (rungs 1–7; inventories, measure candidates, gradients)

**New empirical-anchor and host artifacts**

- FRW empirical anchor mask:
  - `stage2/frw_data_probe_analysis/config/empirical_anchor_box_v1.json`
  - `stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_empirical_anchor_mask_v1.csv`
- Joint anchor intersections, kernel, profiles, sensitivity, mech contrast:
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_intersections_v1.csv`
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_kernel_v1.csv`
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_profiles_v1.csv`
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_sensitivity_v1.csv`
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_mech_contrast_v1.csv`
  - `stage2/joint_mech_frw_analysis/outputs/figures/stage2_joint_mech_frw_anchor_overview_v1.png`
- External flat–FRW host cross-check:
  - `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung1_age_crosscheck_v1.csv`
  - `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung2_age_contrast_v1.csv`

**Program role**

This belt sits between:

- Phase 3 mechanism scalars (θ → vacuum-side amplitudes),
- Phase 4 FRW toy background (vacuum scale → \(\Omega_\Lambda\), `age_Gyr`, viability flags),
- and a simple external flat–FRW age calculation.

Its job is **not** to claim “we fit ΛCDM”, but to:

1. Define a small empirical “anchor box” in \((\Omega_\Lambda, t_0)\)-space.
2. See whether the existing toy corridor and FRW-viable sets intersect that box.
3. Inspect what the Phase 3 mechanism is doing on that kernel.
4. Cross-check the Phase 4 `age_Gyr` against a standard flat–FRW host.

---

## 2. Empirical anchor box and mask

The anchor is defined via:

- Config: `stage2/frw_data_probe_analysis/config/empirical_anchor_box_v1.json`

This JSON specifies:

- central values for an \(\Omega_\Lambda\)-like column and an age-like column (Gyr),
- symmetric half-widths around those central values,
- the column names to use from the Phase 4 FRW toy table.

Using this config, we run:

- `stage2/frw_data_probe_analysis/src/analyze_frw_empirical_anchor_v1.py`

This produces:

- `stage2_frw_empirical_anchor_mask_v1.csv` with columns:
  - `theta`, `theta_index`
  - `omega_lambda`, `age_Gyr` (copied from Phase 4 FRW toy grid)
  - `in_empirical_anchor_box` (Boolean)

On the 2048-point θ-grid:

- `in_empirical_anchor_box` is **true for 18 points**  
  → about **0.88%** of the grid.

By construction this mask is purely **Stage 2 diagnostic**:

- it does **not** alter any Phase 4 table,
- it reads Phase 4 outputs plus a small config box and emits a downstream Boolean column.

---

## 3. Intersections with FRW viability and toy corridor

We combine the anchor mask with:

- FRW viability and LCDM-like masks from Phase 4,
- the Stage 2 toy corridor families.

Using:

- `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_intersections_v1.py`

on the joint grid
`stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv` we obtain:

- `stage2_joint_mech_frw_anchor_intersections_v1.csv`

Key counts (from the logged run):

- `ALL_GRID`:
  - 2048 / 2048 (by definition).
- `FRW_VIABLE`:
  - 1016 / 2048 ≈ **0.496** of the grid.
- `TOY_CORRIDOR`:
  - 1186 / 2048 ≈ **0.579** of the grid.
- `EMPIRICAL_ANCHOR` (`in_empirical_anchor_box`):
  - 18 / 2048 ≈ **0.0088** of the grid.
- Intersections:
  - `FRW_VIABLE ∧ ANCHOR`: 18 / 2048
  - `CORRIDOR ∧ ANCHOR`: 18 / 2048
  - `CORRIDOR ∧ FRW_VIABLE ∧ ANCHOR`: 18 / 2048

So *all* anchor points lie simultaneously in:

- the FRW-viable set and
- the Stage 2 toy corridor.

We refer to this 18-point set as the **anchor kernel**.

---

## 4. Anchor kernel structure in θ

The kernel’s θ-structure is resolved by:

- `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_kernel_v1.py`
- Output: `stage2_joint_mech_frw_anchor_kernel_v1.csv`

Result:

- Total kernel size: 18 θ-points.
- They form **two contiguous θ-index segments** of length 9 each:
  - Segment 1: `theta_index[205–213]`,  
    `theta ∈ [0.6289, 0.6535]` (approx; from the run log),
  - Segment 2: `theta_index[1078–1086]`,  
    `theta ∈ [3.3073, 3.3318]` (approx).

Both segments:

- lie inside the FRW-viable band,
- lie inside the toy corridor,
- do **not** currently include \(\theta^\star\); the minimal distance of θ in the kernel to
  the current \(\theta^\star\) value is \(\mathcal{O}(1)\) in θ units.

The high-level picture:

- The anchor kernel is a **thin but non-needle** structure:
  - not just a single isolated θ,
  - but also not a broad band – two short, disjoint segments.

A visual overview is saved in:

- `stage2/joint_mech_frw_analysis/outputs/figures/stage2_joint_mech_frw_anchor_overview_v1.png`

---

## 5. Profiles and sensitivity

### 5.1. Scalar profiles over the anchor

Using:

- `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_profiles_v1.py`
- Output: `stage2_joint_mech_frw_anchor_profiles_v1.csv`

we summarise, for each set:

- `ALL_GRID`
- `FRW_VIABLE`
- `TOY_CORRIDOR`
- `EMPIRICAL_ANCHOR`
- `FRW_VIABLE ∧ ANCHOR`
- `CORRIDOR ∧ ANCHOR`
- `CORRIDOR ∧ FRW_VIABLE ∧ ANCHOR`

the mean, standard deviation, min, max of:

- Phase 4 scalars: `E_vac`, `omega_lambda`, `age_Gyr`
- Phase 3 mechanism scalars:
  - `mech_baseline_A0`, `mech_baseline_A_floor`, `mech_baseline_bound`
  - `mech_binding_A0`, `mech_binding_A`, `mech_binding_bound`

Diagnostics:

- The anchor kernel is tightly clustered in:
  - `omega_lambda` and `age_Gyr`, consistent with the small anchor box.
- The mechanism amplitudes on the kernel:
  - occupy a narrower band than on `ALL_GRID`,
  - but remain compatible with the overall FRW-viable and corridor ranges.
- No single mechanism scalar is promoted to a canonical “measure over θ” at this rung;
  this belt remains diagnostic.

### 5.2. Sensitivity to anchor box size

Using:

- `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_sensitivity_v1.py`
- Output: `stage2_joint_mech_frw_anchor_sensitivity_v1.csv`

we scale the anchor half-widths by:

- \(s = 0.5, 1.0, 1.5\)

and record:

- `n_in_box` (points in the scaled box),
- `n_box∧FRW`, `n_box∧corr`, `n_box∧corr∧FRW`.

From the logged run:

- \(s = 0.5\):
  - `n_in_box = 8`, all within FRW-viable and the toy corridor.
- \(s = 1.0\) (baseline):
  - `n_in_box = 18` (the kernel).
- \(s = 1.5\):
  - `n_in_box = 26`, with 24 points in `FRW_VIABLE ∧ TOY_CORRIDOR`.

Interpretation:

- The anchor kernel is **stable under modest box rescaling**:
  - shrinking the box picks out the “core” of the two segments,
  - enlarging it grows the segments but does not suddenly grab the whole corridor.

---

## 6. Mechanism contrast inside vs outside the anchor

Using:

- `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_mech_contrast_v1.py`
- Output: `stage2_joint_mech_frw_anchor_mech_contrast_v1.csv`

we compare the mechanism scalars across:

- `ALL_GRID`
- `FRW_VIABLE`
- `CORRIDOR ∧ FRW_VIABLE`
- `CORRIDOR ∧ FRW_VIABLE ∧ ANCHOR`
- `CORRIDOR ∧ FRW_VIABLE ∧ ¬ANCHOR`

The anchor kernel:

- has mechanism amplitudes that are:
  - more tightly distributed than on `ALL_GRID`,
  - somewhat narrower than on `CORRIDOR ∧ FRW_VIABLE` as a whole.
- However, the contrast between **inside** vs **outside** the anchor within
  the corridor+viable set is still **modest**:
  - this is a nontrivial diagnostic structure,
  - but not yet a clean “mechanism picks the anchor” signature.

At this rung we treat this as:

- evidence that the mechanism is **compatible** with the empirical box,
- but **not yet compelling evidence** that it *selects* that box.

---

## 7. External flat–FRW host age cross-check

### 7.1. Host construction

We introduce a simple external flat–FRW host belt:

- `stage2/external_frw_host/src/compute_analytic_frw_ages_v1.py`

This script:

1. Takes the joint grid:
   - `stage2_joint_theta_grid_v1.csv` (with `omega_lambda`, `age_Gyr`, `frw_viable`).
2. Interprets `omega_lambda` as a flat \(\Omega_\Lambda\).
3. For each \(\Omega_\Lambda\), numerically integrates a standard flat–FRW age
   \(t_0^{\text{(host)}}(\Omega_\Lambda)\) (dimensionless).
4. Calibrates a single Gyr scale factor so that host ages roughly align with toy ages over
   the grid.
5. Writes:
   - `stage2_external_frw_rung1_age_crosscheck_v1.csv` with columns:
     - `theta_index`, `theta`, `omega_lambda`
     - `age_Gyr` (Phase 4 toy)
     - `age_Gyr_host` (external host)
     - `age_Gyr_diff = age_Gyr_host - age_Gyr`
     - `age_Gyr_rel_diff = age_Gyr_diff / age_Gyr`
     - `frw_viable` (mask)

### 7.2. Contrast by sets

Using:

- `stage2/external_frw_host/src/analyze_external_frw_age_contrast_v1.py`
- Output:
  - `stage2_external_frw_rung2_age_contrast_v1.csv`

we summarise mean and dispersion of `age_Gyr_diff` and `age_Gyr_rel_diff` for:

- `ALL_GRID`
- `FRW_VIABLE`
- `CORRIDOR ∧ FRW_VIABLE`
- `CORRIDOR ∧ FRW_VIABLE ∧ ANCHOR`

Representative diagnostics from the logged run:

- `ALL_GRID` (2048 points):
  - ⟨Δage⟩ ≈ −8.4 Gyr,
  - ⟨|Δage| / age_toy⟩ ≈ 0.53.
- `FRW_VIABLE` (1016 points):
  - ⟨Δage⟩ ≈ −2.5 Gyr,
  - ⟨|Δage| / age_toy⟩ ≈ 0.18.
- `CORRIDOR ∧ FRW_VIABLE` (154 points):
  - ⟨Δage⟩ ≈ −11.9 Gyr,
  - ⟨|Δage| / age_toy⟩ ≈ 0.84.
- `CORRIDOR ∧ FRW_VIABLE ∧ ANCHOR` (18 points):
  - ⟨Δage⟩ ≈ −10.9 Gyr,
  - ⟨|Δage| / age_toy⟩ ≈ 0.80.

Interpretation:

- The Phase 4 FRW toy age is:
  - loosely calibrated to a standard flat–FRW age on the grid as a whole,
  - somewhat better-behaved on the FRW-viable subset,
  - significantly misaligned (large negative Δage, large relative error) inside the toy
    corridor and anchor kernel.
- For now, we treat this as:
  - a **warning light** for interpreting `age_Gyr` as a physically calibrated age,
  - an indication that any future empirical contact should either:
    - improve the Phase 4 toy mapping, or
    - lean more heavily on the external host for age-like diagnostics.

No changes are made to Phase 4 code at this rung.

---

## 8. Gating, non-claims, and future directions

**Gating status**

- All scripts and tables in this belt live under `stage2/` and are explicitly
  **non-canonical diagnostics**.
- No Phase 3 or Phase 4 claims are modified.
- No direct cosmology data likelihoods (Planck, BAO, SN, etc.) are used:
  - the “empirical anchor box” is a schematic background-cosmology box in
    \((\Omega_\Lambda, t_0)\)-space, not a full data pipeline.

**Non-claims**

At this rung we explicitly **do not claim**:

- that the axiom or its mechanism “predicts” the observed \(\Omega_\Lambda\) or age,
- that the anchor kernel is unique, optimal, or selected by the mechanism,
- that the FRW toy mapping is a faithful representation of ΛCDM background cosmology.

Instead, we record:

- there **exists** a small θ-kernel where:
  - the Phase 3 mechanism amplitudes,
  - the Phase 4 FRW toy outputs,
  - and a simple empirical background-cosmology box all intersect without contradiction;
- the FRW toy age is only loosely compatible with a standard flat–FRW host, especially in
  the corridor and anchor region.

**Future directions (outside this doc’s scope)**

Possible next rungs, to be designed and gated separately:

1. **FRW toy refinement:**
   - tighten the Phase 4 toy mapping so `age_Gyr` is better calibrated against the host
     on FRW-viable sets;
   - or introduce a “host-calibrated” age column as a first-class diagnostic.
2. **External cosmology host belt (Stage II-style):**
   - connect θ → effective cosmological parameters → CCL/CLASS-style background or
     linear observables, still under strict Phase 0 governance.
3. **Data-contact gates:**
   - define clear criteria for when, if ever, these diagnostics may be promoted into
     Phase 4 or Phase 5 narrative as a bona fide “empirical anchor”.

Until those rungs exist and pass their own gates, this document should be read as a
diagnostic snapshot only.

