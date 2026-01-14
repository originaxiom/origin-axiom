# STAGE 2 – Empirical Anchor Status (v1)

**Document scope.** This note summarizes the current status of the Stage 2 empirical–anchor rungs that sit on top of:

- the Phase 3 mechanism module (θ → vacuum-side outputs),
- the Phase 4 FRW toy module (vacuum → toy FRW backgrounds),
- and the Stage 2 FRW / joint belts.

It is *not* making new physical claims. It:

- records **what the current code actually does**,
- describes **where the θ-corridors and empirical boxes intersect (or fail to)**,
- and highlights the main tensions that any future “real physics” contact will have to resolve.

---

## 0. Quick map of the main ingredients

### 0.1. Core tables

- **FRW toy shape mask (Phase 4):**  
  `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`  
  Contains:
  - `theta_index`, `theta`
  - `E_vac`, `omega_lambda`, `age_Gyr`
  - FRW diagnostic flags such as `has_matter_era`, `has_late_accel`, `smooth_H2`, `frw_viable`, etc.

- **FRW empirical anchor mask (Stage 2):**  
  `stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_empirical_anchor_mask_v1.csv`  
  - Same θ-grid; adds `in_empirical_anchor_box` column (Boolean).
  - This is defined by an “empirical box” in (`omega_lambda`, `age_Gyr`) taken from
    `stage2/frw_data_probe_analysis/config/empirical_anchor_box_v1.json`.

- **Joint mechanism–FRW grid (Stage 2):**  
  `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv`  
  - Merges Phase 3 mechanism outputs and Phase 4 FRW toy outputs on the same θ-grid.
  - Key columns:
    - `theta_index`, `theta`
    - FRW side: `E_vac`, `omega_lambda`, `age_Gyr`
    - FRW masks: `in_toy_corridor` (F1 corridor), `frw_viable`, `lcdm_like`, `shape_and_viable`, `shape_and_lcdm`, `frw_data_ok`
    - Mechanism side: `mech_baseline_A0`, `mech_baseline_A_floor`, `mech_baseline_bound`, `mech_binding_A0`, `mech_binding_A`, `mech_binding_bound`

- **External FRW host bridge (Stage 2):**  
  `stage2/external_frw_host/outputs/tables/stage2_external_frw_background_bridge_v1.csv`  
  - Built from an analytic flat-FRW “host” calculation at fixed `omega_lambda`:
    - host age: `age_Gyr_host`
    - toy age (copied from Phase 4): `age_Gyr_toy`
  - plus `theta_index`, `theta`, `omega_lambda`, `frw_viable`.

These are the main endpoints; everything below is built on top of them.

---

## 1. FRW empirical anchor on the toy side

### 1.1. Defining the FRW empirical box

**Design doc:** `phase4/docs/PHASE4_EMPIRICAL_ANCHOR_DESIGN_v1.md`  
**Stage 2 script:** `stage2/frw_data_probe_analysis/src/analyze_frw_empirical_anchor_v1.py`

- Reads the FRW toy table:
  - `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`
- Reads the empirical box config:
  - `stage2/frw_data_probe_analysis/config/empirical_anchor_box_v1.json`
    - Contains central values and half-widths for:
      - `omega_lambda`
      - `age_Gyr`

From this, it defines a Boolean mask:

- `in_empirical_anchor_box = 1` iff:
  - `omega_lambda` lies inside the specified Λ-band, and
  - `age_Gyr` lies inside the specified age band.

**Current outcome (rung A3):**

- Grid size: `2048` θ-points.
- Size of empirical box (toy side):
  - `n_in_anchor_box = 18`  
    → ~0.87% of the total grid.
- These 18 points are a *thin sliver* in θ-space where the toy FRW background matches both:
  - an internally chosen Λ-like band,
  - and an internally chosen toy-age band.

### 1.2. Intersection with corridor and viability

**Script:** `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_intersections_v1.py`  
**Output:** `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_intersections_v1.csv`

This takes:

- the joint θ-grid table,
- the FRW empirical-anchor mask,

and constructs several subsets:

- `ALL_GRID`
- `FRW_VIABLE`
- `TOY_CORRIDOR` (Phase 4 F1 corridor on the toy side)
- `EMPIRICAL_ANCHOR` (`in_empirical_anchor_box == 1`)
- and the intersections:
  - `FRW_VIABLE_AND_ANCHOR`
  - `CORRIDOR_AND_ANCHOR`
  - `CORRIDOR_AND_VIABLE_AND_ANCHOR`

**Current counts (rung A4):**

- `ALL_GRID`: 2048 / 2048 (100%)
- `FRW_VIABLE`: 1016 / 2048 (~49.6%)
- `TOY_CORRIDOR`: 1186 / 2048 (~57.9%)
- `EMPIRICAL_ANCHOR`: 18 / 2048 (~0.9%)
- `FRW_VIABLE_AND_ANCHOR`: 18 / 2048 (~0.9%)
- `CORRIDOR_AND_ANCHOR`: 18 / 2048 (~0.9%)
- `CORRIDOR_AND_VIABLE_AND_ANCHOR`: 18 / 2048 (~0.9%)

So at this rung, **all 18 anchor points**:

- are FRW-viable, and
- lie inside the Phase 4 toy corridor.

This is the “anchor kernel” inside the F1 corridor.

### 1.3. Kernel structure in θ

**Script:** `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_kernel_v1.py`  
**Output:** `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_kernel_v1.csv`

This script:

- Takes the `CORRIDOR_AND_VIABLE_AND_ANCHOR` mask,
- Finds contiguous **θ-index segments** inside that set,
- For each segment, reports:
  - θ-index range,
  - θ-range (`theta_min`, `theta_max`),
  - whether the segment contains θ★ (as currently defined in config),
  - minimal distance |θ − θ★| within the segment.

**Current outcome (rung A5b):**

- Kernel size: 18 θ-points.
- Segments (2 equal-size clusters):
  1. `theta_index[205–213]`, 9 points,
     - `theta ∈ [0.6289, 0.6535]`,
     - does *not* contain θ★,
     - closest distance to θ★ ≈ 1.52.
  2. `theta_index[1078–1086]`, 9 points,
     - `theta ∈ [3.3073, 3.3318]`,
     - does *not* contain θ★,
     - closest distance to θ★ ≈ 1.13.

This yields a clean picture:

- The **toy-corridor+FRW-viable+empirical-box kernel** is:
  - **small** (18 / 2048 θ’s),
  - **clustered** into two short θ-intervals,
  - and **well-separated** from the current θ★ choice.

### 1.4. Profiles and sensitivity

**Profiles script:**  
`stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_profiles_v1.py`  
**Output:**  
`stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_profiles_v1.csv`

This builds simple profiles of:

- `E_vac`, `omega_lambda`, `age_Gyr`
- and mechanism columns `mech_*`

over the sets:

- `ALL_GRID`
- `FRW_VIABLE`
- `TOY_CORRIDOR`
- `EMPIRICAL_ANCHOR`
- `FRW_VIABLE_AND_ANCHOR`
- `CORRIDOR_AND_ANCHOR`
- `CORRIDOR_AND_VIABLE_AND_ANCHOR`

Key facts for the anchor kernel:

- `n_theta = 18` (≈0.9% of grid).
- FRW side:
  - `omega_lambda` is tightly clustered:
    - mean ≈ 0.69,
    - σ ≈ 0.016,
    - range ≈ [0.664, 0.717].
  - `age_Gyr`:
    - mean ≈ 13.50 Gyr,
    - σ ≈ 0.049 Gyr,
    - range ≈ [13.42, 13.58] Gyr.
- Mechanism side:
  - `mech_baseline_A0` and `mech_binding_A0`:
    - mean ≈ 0.0461,
    - σ ≈ 2.7×10⁻⁴,
    - range ≈ [0.0457, 0.0465].
  - So both mechanism variants essentially pick out **the same narrow amplitude band** on the anchor kernel.

**Sensitivity script:**  
`stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_sensitivity_v1.py`  
**Output:**  
`stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_sensitivity_v1.csv`

This:

- rescales the empirical box half-widths by factors (0.5, 1.0, 1.5),
- recomputes how many θ’s fall into the rescaled box,
- and tracks overlaps with `FRW_VIABLE` and `TOY_CORRIDOR`.

Summary:

- At 0.5× width:
  - `n_in_box = 8`, all in `FRW_VIABLE` and `TOY_CORRIDOR`.
- At 1.0× width:
  - `n_in_box = 18` (the baseline kernel).
- At 1.5× width:
  - `n_in_box = 26`, with:
    - 26 FRW-viable,
    - 24 also in the toy corridor.

So the **anchor kernel is robust** to modest widening of the empirical box; it does not explode into a broad, noisy region.

---

## 2. External FRW host and age alignment

This belt checks how the Phase 4 FRW toy backgrounds compare to a **simple analytic flat-FRW host** that uses the same `omega_lambda` but computes age via a standard FRW integral.

### 2.1. External host ages and cross-check

**Host age script:**  
`stage2/external_frw_host/src/compute_analytic_frw_ages_v1.py`  
**Host cross-check table:**  
`stage2/external_frw_host/outputs/tables/stage2_external_frw_rung1_age_crosscheck_v1.csv`

- For each θ:
  - Takes `omega_lambda` from the FRW toy table / joint grid.
  - Computes a dimensionless FRW age for a flat universe with matter + Λ.
  - Calibrates a global scale factor so that:
    - the host ages roughly match the toy ages on the FRW-viable set in a mean-squared sense.
  - Outputs:
    - `theta_index`, `theta`, `omega_lambda`,
    - `age_Gyr` (toy, copied from Phase 4),
    - `age_Gyr_host` (analytic host),
    - `age_Gyr_diff = age_Gyr_host - age_Gyr`,
    - `age_Gyr_rel_diff = (age_Gyr_host - age_Gyr) / age_Gyr`,
    - `frw_viable`.

**Contrast script:**  
`stage2/external_frw_host/src/analyze_external_frw_age_contrast_v1.py`  
**Output:**  
`stage2/external_frw_host/outputs/tables/stage2_external_frw_rung2_age_contrast_v1.csv`

Key summary:

- `ALL_GRID` (2048 pts):
  - ⟨Δage⟩ ≈ -8.41 Gyr,
  - ⟨|Δage|/age_toy⟩ ≈ 0.53.
- `FRW_VIABLE` (1016 pts):
  - ⟨Δage⟩ ≈ -2.49 Gyr,
  - ⟨|Δage|/age_toy⟩ ≈ 0.18.
- `CORRIDOR_AND_VIABLE` (154 pts):
  - ⟨Δage⟩ ≈ -11.86 Gyr,
  - ⟨|Δage|/age_toy⟩ ≈ 0.84.
- `CORRIDOR_AND_VIABLE_AND_ANCHOR` (18 pts):
  - ⟨Δage⟩ ≈ -10.87 Gyr,
  - ⟨|Δage|/age_toy⟩ ≈ 0.81.

So:

- On the FRW-viable band as a whole, the host provides a **reasonable but loose** age cross-check (∼20% level).
- On the *corridor+empirical-anchor kernel*, the host says:
  - “these toy universes are ~11 Gyr *older* than my own age.”

This is an important tension: the anchor kernel that looks nice inside the toy itself is **not** age-compatible with the simple external FRW host.

### 2.2. Age-consistency mask (host vs toy)

**Script:**  
`stage2/external_frw_host/src/flag_age_consistent_subset_v1.py`  
**Output:**  
`stage2/external_frw_host/outputs/tables/stage2_external_frw_rung3_age_consistency_mask_v1.csv`

This:

- Reads the host cross-check table,
- Defines a **relative-age consistency mask**:
  - `age_consistent_rel_le_20pct = 1` iff |age_host − age_toy| / age_toy ≤ 0.2 (20%),
- Joins in the FRW empirical anchor mask to see where consistency overlaps with both viability and the toy anchor.

Current summary:

- `ALL_GRID`: 778 / 2048 θ’s (∼38%) are within 20% age consistency.
- `FRW_VIABLE`: same 778 / 2048 (all age-consistent points are FRW-viable).
- `CORRIDOR_AND_VIABLE`:
  - 0 θ’s satisfy the 20% age-consistency cut.
- `CORRIDOR_AND_VIABLE_AND_ANCHOR`:
  - 0 θ’s satisfy the 20% age-consistency cut.

So:

- There *exist* θ’s where host and toy agree reasonably on age,
- but **none of these lie in the current F1 toy corridor** or in the toy empirical-anchor kernel.

### 2.3. Host-age window around the observed age

**Age-window diagnostics:**  
- `stage2/external_frw_host/src/analyze_external_frw_age_window_v1.py`  
- `stage2/external_frw_host/src/flag_external_frw_host_age_anchor_v1.py`

**Outputs:**

- `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung4_age_window_summary_v1.csv`
- `stage2/external_frw_host/outputs/tables/stage2_external_frw_host_age_anchor_mask_v1.csv`
- `stage2/external_frw_host/outputs/tables/stage2_external_frw_host_age_anchor_summary_v1.csv`
- `stage2/external_frw_host/outputs/tables/stage2_external_frw_host_age_anchor_profiles_v1.csv`

Design choice:

- Introduce a **host-age anchor window**:
  - host age in [13.3, 14.3] Gyr (a ±0.5 Gyr band around the observed ≈13.8 Gyr).

Key results:

- `HOST_AGE_ANCHOR` (host ages in [13.3, 14.3] Gyr and FRW-viable):
  - 34 / 2048 θ’s (~1.66% of grid).
  - On this set:
    - `omega_lambda` clusters around ≈ 1.05,
    - `age_Gyr_host`:
      - mean ≈ 13.60 Gyr,
      - σ ≈ 0.18 Gyr,
      - range ≈ [13.31, 13.90] Gyr,
    - `age_Gyr_toy`:
      - mean ≈ 12.58 Gyr,
      - σ ≈ 0.07 Gyr,
      - range ≈ [12.47, 12.69] Gyr,
    - mechanism amplitudes:
      - `mech_baseline_A0` and `mech_binding_A0` ≈ 0.0513 with very small spread.
- Intersection with the toy corridor:
  - Script: `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_host_age_anchor_intersections_v1.py`
  - Output: `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_host_age_anchor_intersections_v1.csv`
  - `CORRIDOR_AND_VIABLE_AND_HOST_AGE_ANCHOR` is **empty**.

So the picture is:

- There is a narrow θ-band where an external FRW host gives a Universe-like age.
- The toy FRW age at those θ’s is ~1 Gyr younger than the host.
- None of those θ’s live inside the current toy corridor.

### 2.4. Host anchor mirroring of the toy empirical box

For completeness, there is also a **host-side mirror** of the toy empirical box:

- `stage2/external_frw_host/src/analyze_external_frw_host_anchor_v1.py`
- `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_host_anchor_intersections_v1.py`

These scripts:

- Infer a host-side (`omega_lambda`, `age_Gyr_host`) box from the toy empirical-anchor set,
- flag `in_host_empirical_anchor_box`,
- and measure overlaps with:
  - `FRW_VIABLE`,
  - `TOY_CORRIDOR`,
  - and the joint corridor+viable set.

Current status is consistent with the story above:

- The same 18 θ’s that form the toy empirical-anchor kernel are also flagged as a host-side mirror,
- but their **host ages are far from Universe-like**, and their **toy ages are far from the host-age window**.

---

## 3. FRW toy age monotonicity (sanity of the toy itself)

**Script:**  
`stage2/external_frw_host/src/check_frw_toy_age_monotonicity_v1.py`  
**Output:**  
`stage2/external_frw_host/outputs/tables/stage2_external_frw_rung5_toy_age_monotonicity_v1.csv`

Goal:

- Ensure that, at least on the FRW-viable band, the toy FRW age behaves **monotonically** as a function of `omega_lambda`, so that joint boxes in (`omega_lambda`, `age_Gyr`) are not artifacts of numerical wiggles.

Procedure:

- Load `phase4_F1_frw_shape_probe_mask.csv`.
- Restrict to `frw_viable == 1` (1016 θ-points).
- Sort by `omega_lambda`.
- Compute finite-difference gradients:
  - `grad = Δ(age_Gyr) / Δ(omega_lambda)`.

Result:

- `n_theta = 1016`, `n_steps = 1015`.
- Sign structure:
  - `n_pos = 0`, `n_neg = 1015`, `n_zero = 0`.
- So on the FRW-viable band,
  - `age_Gyr` is **strictly decreasing** as `omega_lambda` increases.
- Value ranges:
  - `omega_lambda ∈ [0.3027, 1.6898]`,
  - `age_Gyr ∈ [11.46, 14.97]` Gyr.

Interpretation:

- The toy FRW age vs `omega_lambda` relation is **smooth and strictly monotone** on the FRW-viable subset.
- This justifies treating boxes in (`omega_lambda`, `age_Gyr`) as selecting genuine slices of a smooth FRW trade-off curve, not numerical noise.

---

## 4. Where the Stage 2 anchor story stands (v1)

Putting all of this together:

1. **Inside the toy itself** (Phase 4 + Stage 2 FRW belts):
   - There exists a small but robust θ-region (18 points, 2 short intervals) where:
     - the toy FRW background is viable,
     - the θ lies inside the Phase 4 F1 corridor,
     - and (`omega_lambda`, `age_Gyr`) fall inside an empirical box.
   - Mechanism amplitudes on this kernel are very tightly clustered around A ≈ 0.046.

2. **Relative to a simple external FRW host:**
   - On the FRW-viable band as a whole, host ages and toy ages agree at the ∼20% level, which is acceptable for a diagnostic host.
   - On the toy empirical-anchor kernel, the host ages differ from the toy ages by ≈ 10–11 Gyr (~80% relative difference).
   - There is a separate narrow θ-band (34 points) where the host age is Universe-like (~13.3–14.3 Gyr), but:
     - the toy age there is ~12.6 Gyr,
     - none of those θ’s are in the current toy corridor.

3. **Relative-age consistency:**
   - There are 778 θ-points where host and toy ages agree within 20%,
     all of them FRW-viable.
   - None of these lie in the current **corridor+anchor** kernel.

4. **Toy FRW behavior:**
   - The toy age is strictly monotone in `omega_lambda` on the FRW-viable band, so the observed tensions are not artifacts of local numerical glitches.

**Conclusion at this rung.**

- The current implementation of the axiom + Phase 3 mechanism + Phase 4 FRW toy + Stage 2 corridors **does produce a small, well-structured θ-kernel** that looks reasonable *internally* to the toy.
- However, when this kernel is confronted with:
  - a simple external FRW age calculation, and
  - a broad Universe-age window,
  the kernel sits in a **host-disfavored region**:
  - toy ages and host ages do not align,
  - and the host-age anchor lies outside the toy corridor.

This is not a failure of the program; it is a **diagnostic result**:

- At this rung, the current toy implementation of the axiom **does not support a θ-corridor that is simultaneously**:
  - Phase 4 corridor-preferred,
  - FRW-viable,
  - inside the toy empirical anchor box,
  - and host-age compatible with the observed Universe.

Future rungs (beyond v1 of this document) will have to decide whether to:

- treat this as evidence *against* the current implementation of the toy/FRW link,
- or to adjust:
  - the FRW toy mapping,
  - the empirical box definition,
  - or the mechanism–FRW coupling,
under Phase 0 governance and with explicit promotion gates.

