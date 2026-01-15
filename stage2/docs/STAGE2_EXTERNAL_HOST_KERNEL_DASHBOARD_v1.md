# Stage 2 – External Host Kernel Dashboard (FRW toy, FRW host, cosmo host)

This document collects, in one place, the **small θ–regions (“kernels”)** where:

1. The Phase 4 FRW toy is FRW-viable.
2. The Phase 4 toy sits inside its own **corridor**.
3. One or more external FRW / cosmological “hosts” assign **Universe-like ages**.
4. The Stage 2 mechanism behaves **smoothly and non-pathologically**.

The point is not to claim “this is the real Universe”, but to provide a **compact, inspectable object** that Phase 4/5 can reference as “first contact” between the internal θ-grid and external FRW / cosmology.

---

## 1. Kernel objects in play

We track three sets:

1. **FRW_TOY_ANCHOR_KERNEL** (internal Phase-4 toy only)
2. **EXTERNAL_FRW_HOST_AGE_ANCHOR** (Phase-4 toy + external FRW host)
3. **EXTERNAL_COSMO_HOST_AGE_CORRIDOR_KERNEL** (Phase-4 toy + external cosmology host + corridor)

All three are derived from the **same 2048-point θ-grid** and its Phase-4 FRW masks.

### 1.1 FRW toy anchor kernel (internal)

Source: Phase-4 FRW toy anchor kernel table (2-point subset).

- Set name: `FRW_TOY_ANCHOR_KERNEL`
- Size: `n_theta = 2`
- Definition (schematic):

  - FRW-viable in the Phase-4 toy.
  - Inside the toy **empirical anchor box**.
  - Inside the Phase-4 **toy corridor**.

The kernel is defined and documented in Phase-4 FRW toy / anchor docs; here we only treat it as the **internal reference kernel** that the hosts will later be compared to.

> For now, this dashboard does **not** repeat its numerical θ / Ω_Λ values; Phase-4 remains the source of truth for those.

---

### 1.2 External FRW host – age anchor subset

Source tables:

- `stage2/external_frw_host/outputs/tables/stage2_external_frw_host_age_anchor_mask_v1.csv`
- `stage2/external_frw_host/outputs/tables/stage2_external_frw_host_age_anchor_profiles_v1.csv`
- Aggregated in:
  - `stage2/external_cosmo_host/outputs/tables/stage2_external_host_kernel_comparison_v1.csv`

**Definition**

The **external FRW host age-anchor subset** is:

- `EXTERNAL_FRW_HOST_AGE_ANCHOR`  
- Built from the **external FRW host** age table cross-matched against the **Phase-4 FRW empirical anchor box** in (Ω_Λ, age) space.
- On the Stage-2 θ-grid this corresponds to points that:

  1. Are FRW-viable in the host table.
  2. Fall inside the **empirical FRW anchor box** (host coordinates).
  3. Are joined back onto the joint θ-grid via `theta_index`.

**Key numbers (from the current run)**

- Size:  
  - `n_theta = 34`
- θ-range:
  - `theta_min ≈ 0.7885`
  - `theta_max ≈ 3.1723`
- Host FRW Ω_Λ (host side – not the Phase-4 toy Ω_Λ):

  - `Omega_lambda_host_mean ≈ 1.0533`
  - `Omega_lambda_host_min ≈ 1.0015`
  - `Omega_lambda_host_max ≈ 1.1047`

- Host ages (FRW host, in Gyr):

  - `age_Gyr_host_mean ≈ 13.60`
  - `age_Gyr_host_min  ≈ 13.31`
  - `age_Gyr_host_max  ≈ 13.90`

- Mechanism summary:

  - Stage-2 mechanism columns are **not** yet wired into this subset summary; at this point the goal is to understand **where** the external FRW host aligns with the internal FRW anchor box, not to over-interpret mechanism behavior.

Interpretation:

- This set shows that, relative to an external FRW age calculation tied to the **FRW empirical anchor box**, there exists a **34-point θ-band** on the Stage-2 grid with **Universe-like FRW ages**.
- It is deliberately larger than the eventual **corridor kernel** (next section) and does *not* yet enforce the Phase-4 **corridor** or mechanism smoothness.

---

### 1.3 External cosmology host – age∧corridor kernel

Source tables:

- `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_age_anchor_mask_v1.csv`
- `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_age_anchor_corridor_kernel_v1.csv`
- Aggregated in:
  - `stage2/external_cosmo_host/outputs/tables/stage2_external_host_kernel_comparison_v1.csv`

**Definition**

The **cosmo-host age∧corridor kernel** is:

- `EXTERNAL_COSMO_HOST_AGE_CORRIDOR_KERNEL`
- Built from the external cosmology host chain by:

  1. Mapping θ → `(Omega_m, Omega_lambda, H0)` with `oa_theta_to_cosmo_params_v1.py`.
  2. Computing **host FRW ages** on this parameter grid (`run_cosmo_host_background_grid_v1.py`).
  3. Selecting points where host age lies in a **Universe-like window** around ~13.8 Gyr (the “host age anchor”).
  4. Intersecting with:
     - Phase-4 `frw_viable == True`,
     - Phase-4 `in_toy_corridor == True`.

The result is a **12-point kernel** where the Phase-4 FRW toy, the external cosmology host, and the Stage-2 mechanism all overlap in a controlled way.

**Key numbers (current run)**

From `stage2_external_cosmo_host_age_anchor_corridor_kernel_v1.csv`:

- Size:

  - `n_theta = 12`

- θ-range on the joint grid:

  - `theta_min ≈ 0.6412`
  - `theta_max ≈ 3.3195`

- Phase-4 toy Ω_Λ (repo side):

  - `omega_lambda_repo_mean ≈ 0.7060`
  - `omega_lambda_repo_min  ≈ 0.6892`
  - `omega_lambda_repo_max  ≈ 0.7230`

- Ages (Gyr):

  - **Phase-4 FRW toy ages** (repo):

    - `age_Gyr_repo_mean ≈ 13.452`
    - `age_Gyr_repo_min  ≈ 13.402`
    - `age_Gyr_repo_max  ≈ 13.502`

  - **External cosmo-host ages**:

    - `age_Gyr_host_mean ≈ 13.546`
    - `age_Gyr_host_min  ≈ 13.334`
    - `age_Gyr_host_max  ≈ 13.768`

- Mechanism behavior (Stage-2 baseline measure):

  - Column: `mech_baseline_A0` (and likewise `mech_binding_A0`)
  - On the 12-point kernel:

    - `mech_baseline_A0_mean ≈ 0.04638`
    - `mech_baseline_A0_min  ≈ 0.04610`
    - `mech_baseline_A0_max  ≈ 0.04665`

  - The corresponding `*_bound` flags are exactly zero throughout the kernel in the current run.

**Interpretation**

On the current Stage-2 grid, **there exists a narrow θ-band with 12 points such that**:

1. The Phase-4 FRW toy is **FRW-viable** and inside its **corridor**.
2. An external flat-ΛCDM cosmology host with fixed mapping θ → `(Omega_m, Omega_lambda, H0)` yields **Universe-like ages** in the 13–14 Gyr range.
3. The Stage-2 mechanism (`mech_baseline_A0` and its variants) is **smooth and tightly banded** across these 12 points, with no pathological spikes or sign flips.

This does **not** say “the real Universe is one of these 12 θ values”. It says:

> Given the present θ-grid and host mapping, there is a small, inspectable region where **internal FRW**, **external cosmology**, and the **mechanism** are mutually compatible in age and remain mathematically well-behaved.

---

## 2. Sensitivity and robustness hooks

The kernel is not a single magic point; it lives inside a **family of nearby host windows and priors** that have already been partially explored.

### 2.1 Host age window sensitivity

Source:  
`stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_age_window_sensitivity_v1.csv`

For different scale factors on the age window around ~13.8 Gyr:

- `scale = 0.5` → window `[13.55, 14.05]` Gyr:
  - HOST_WINDOW: 12 points
  - FRW_VIABLE ∧ HOST_WINDOW: 12
  - CORRIDOR ∧ FRW_VIABLE ∧ HOST_WINDOW: 6

- `scale = 1.0` → window `[13.30, 14.30]` Gyr:
  - HOST_WINDOW: 22
  - FRW_VIABLE ∧ HOST_WINDOW: 22
  - CORRIDOR ∧ FRW_VIABLE ∧ HOST_WINDOW: 12

- `scale = 1.5` → window `[13.05, 14.55]` Gyr:
  - HOST_WINDOW: 34
  - FRW_VIABLE ∧ HOST_WINDOW: 34
  - CORRIDOR ∧ FRW_VIABLE ∧ HOST_WINDOW: 19

- `scale = 2.0` → window `[12.80, 14.80]` Gyr:
  - HOST_WINDOW: 46
  - FRW_VIABLE ∧ HOST_WINDOW: 46
  - CORRIDOR ∧ FRW_VIABLE ∧ HOST_WINDOW: 26

So as the host age window is widened, the **intersection with the toy corridor grows smoothly** (6 → 12 → 19 → 26). There is no sign of a fragile “single-pixel” coincidence; the kernel sits inside a **moderately stable age band**.

### 2.2 Near-flat host subset

Source:

- `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_flat_subset_summary_v1.csv`
- `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_flat_subset_mask_v1.csv`

Definition:

- Near-flat host: \(|\Omega_{\text{tot}} - 1| \le 0.05\).

Key counts:

- `HOST_NEAR_FLAT`: 1286 / 2048 grid points.
- `HOST_NEAR_FLAT_AND_FRW_VIABLE`: 254 points.
- `HOST_NEAR_FLAT_AND_CORRIDOR_AND_FRW_VIABLE`: 154 points.

That last number (154) matches the pure Phase-4 **`CORRIDOR_AND_VIABLE`** set size on the same grid. So the corridor is **compatible with near-flat external cosmology** in a non-trivial way; it’s not being “killed” by the flatness requirement.

---

## 3. How Phase 4 and Phase 5 can use this

This dashboard is designed so that downstream phases can reference **exact, reproducible objects** instead of informal phrases like “a small θ-region where things work”.

### 3.1 Recommended Phase 4 usage

In Phase-4 FRW toy text (and figures), refer to:

- A **FRW toy anchor kernel panel** (2 points, internal only).
- A **host kernel panel** based on the 12-point `EXTERNAL_COSMO_HOST_AGE_CORRIDOR_KERNEL`, with:

  - θ-band and Ω_Λ range,
  - toy vs host ages (means + ranges),
  - mechanism mean band.

Suggested language (scope-safe):

> “On the current θ-grid, there exists a narrow band of 12 points where the Phase-4 FRW toy is FRW-viable and in its corridor, and an external flat-ΛCDM host assigns Universe-like ages. Within this band the Stage-2 mechanism remains smooth and tightly banded. We treat this as a diagnostic `host kernel`, not as a claim that the real Universe selects any specific θ.”

### 3.2 Recommended Phase 5 usage

In Phase-5 “dashboard” / “first real contact” panels:

- Show this 12-point kernel alongside other anchors (mechanism, data probes, etc.).
- Track how:

  - the kernel behaves if the host mapping θ → cosmology is varied,
  - or if the host age window / flatness tolerance are re-tuned.

The kernel is then one of the **stress-test levers** for the entire θ-story: if future adjustments to the framework make it disappear or explode, that behavior becomes part of the Phase-5 narrative.

---

## 4. File and endpoint references

For quick lookup:

- Joint θ-grid (Phase-4, Stage-2 backbone):
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv`
- External FRW host chain:
  - `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung1_age_crosscheck_v1.csv`
  - `stage2/external_frw_host/outputs/tables/stage2_external_frw_host_age_anchor_mask_v1.csv`
  - `stage2/external_frw_host/outputs/tables/stage2_external_frw_host_age_anchor_profiles_v1.csv`
- External cosmology host chain:
  - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_params_grid_v1.csv`
  - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_background_grid_v1.csv`
  - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_rung3_age_contrast_v1.csv`
  - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_age_anchor_mask_v1.csv`
  - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_age_anchor_corridor_kernel_v1.csv`
  - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_age_window_sensitivity_v1.csv`
  - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_flat_subset_mask_v1.csv`
  - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_flat_subset_summary_v1.csv`
- Kernel comparison:
  - `stage2/external_cosmo_host/outputs/tables/stage2_external_host_kernel_comparison_v1.csv`

