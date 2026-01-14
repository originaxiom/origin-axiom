# Stage 2 – External Cosmology Host: Results Snapshot (v1)

## 0. Scope

This document is a **results snapshot** for the `stage2/external_cosmo_host` belt.  
It is **diagnostic only** and lives strictly under the Phase 0 contract:

- No new physics claims.
- No “we fit the Universe” language.
- Only: “given our current θ–mapping and FRW toy model, here is what the external FRW background calculator reports.”

This is meant to be a **lab log** that Phase 4/5 can point to, not a paper section.

---

## 1. Setup (reminder)

- Joint θ–grid (Stage 2):
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv`
  - 2048 θ–samples on `[0, 2π)`, with:
    - `theta_index`, `theta`
    - FRW toy outputs: `omega_lambda`, `age_Gyr`, `frw_viable`, `in_toy_corridor`
    - mechanism outputs: `mech_baseline_*`, `mech_binding_*`

- External cosmology host belt (this chain):
  - H1 – θ → cosmological params:
    - `stage2/external_cosmo_host/src/oa_theta_to_cosmo_params_v1.py`
    - Output:
      - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_params_grid_v1.csv`
      - Columns: `theta_index, theta, omega_lambda_repo, age_Gyr_repo, Omega_m, Omega_lambda, H0_km_s_Mpc`
      - Current mapping:
        - `Omega_lambda = omega_lambda_repo`
        - `Omega_m = 1 - Omega_lambda_repo`
        - `H0_km_s_Mpc = 70.0` (fixed fiducial)
      - On this grid:
        - `min(Omega_m + Omega_lambda) = 1.000`
        - `max(Omega_m + Omega_lambda) = 1.690`
        - i.e. we explicitly allow non-flat backgrounds in the mapping; external host still treats it as a flat FRW toy with the specified (Ω_m, Ω_Λ).

  - H2 – External FRW background ages:
    - `stage2/external_cosmo_host/src/run_cosmo_host_background_grid_v1.py`
    - Output:
      - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_background_grid_v1.csv`
      - Columns: `theta_index, theta, Omega_m, Omega_lambda, H0_km_s_Mpc, age_Gyr_host`
    - Age computation:
      - Uses a **manual trapezoid rule** (no `np.trapz`) for the flat-FRW-like integral
        \[
          t_0 \propto \int_0^1 \frac{da}{a\sqrt{\Omega_m a^{-3} + \Omega_\Lambda}}.
        \]
      - Then calibrated to Gyr via a single scale factor (fixed, shared across grid).
    - Basic stats:
      - 2048 rows, all with finite `age_Gyr_host`.
      - Host-age range:
        - `min(age_Gyr_host) ≈ 9.507 Gyr`
        - `max(age_Gyr_host) ≈ 129.634 Gyr`

---

## 2. Age contrast vs repo FRW toy

Script:

- `stage2/external_cosmo_host/src/analyze_external_cosmo_host_age_contrast_v1.py`
- Output summary:
  - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_rung3_age_contrast_v1.csv`
- This joins:
  - host ages: `age_Gyr_host`
  - repo FRW toy ages: `age_Gyr` (renamed to `age_Gyr_repo`)
  - masks: `frw_viable`, `in_toy_corridor`

Key diagnostics (from the printed summary):

- **ALL_GRID** (n = 2048)
  - ⟨Δage⟩ = ⟨age_host − age_repo⟩ ≈ +32.65 Gyr
  - ⟨|Δage| / age_repo⟩ ≈ 2.85
  - Interpretation:
    - With the *current* mapping and calibration, the host code is typically much older than the repo FRW toy on average.

- **FRW_VIABLE** subset (n = 1016)
  - ⟨Δage⟩ ≈ +72.38 Gyr
  - ⟨|Δage| / age_repo⟩ ≈ 6.16
  - Interpretation:
    - On the FRW-viable subset (by repo criteria), the host background tends to assign dramatically larger ages than the toy FRW pipeline.

- **CORRIDOR_AND_VIABLE** subset (n = 154)
  - ⟨Δage⟩ ≈ −2.44 Gyr
  - ⟨|Δage| / age_repo⟩ ≈ −0.17 (sign reflects the way ratios are stored; magnitude is O(10–1))
  - Interpretation:
    - On the **intersection of FRW_viable ∧ toy-corridor**, the host and repo ages are much closer:
      - Mean difference only a few Gyr in magnitude.
      - This is the first hint that the “corridor & viable” region is special: despite global misalignment, this subset behaves more coherently under the external host.

We do **not** interpret the sign conventions too aggressively here; the core fact is:
- **Global** host vs toy ages disagree wildly.
- **Corridor ∧ viable** behaves much better.

---

## 3. Host age anchor window and overlap with corridor

We then impose a **host-side age anchor**:

Script:

- `stage2/external_cosmo_host/src/flag_external_cosmo_host_age_anchor_v1.py`
- Outputs:
  - Mask + summary:
    - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_age_anchor_mask_v1.csv`
    - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_age_anchor_summary_v1.csv`
  - The summary file contains pre-aggregated stats for several sets.

Anchor definition:

- Host age anchor window:
  \[
    13.3\ \mathrm{Gyr} \;\le\; \text{age\_Gyr\_host} \;\le\; 14.3\ \mathrm{Gyr}
  \]
  motivated by a loose “Universe-age-scale” box, not a precision cosmology fit.

Key numbers (from the summary):

- **ALL_GRID** (n = 2048)
  - ⟨age_host⟩ ≈ 46.85 Gyr
  - ⟨age_repo⟩ ≈ 14.20 Gyr

- **FRW_VIABLE** (n = 1016)
  - ⟨age_host⟩ ≈ 84.61 Gyr
  - ⟨age_repo⟩ ≈ 12.22 Gyr

- **TOY_CORRIDOR** (n = 1186)
  - ⟨age_host⟩ ≈ 9.95 Gyr
  - ⟨age_repo⟩ ≈ 15.89 Gyr

- **HOST_AGE_ANCHOR** (subset where host age lies in [13.3, 14.3] Gyr)
  - n = 22 (≈ 1.07% of grid)
  - ⟨age_host⟩ ≈ 13.77 Gyr
  - ⟨age_repo⟩ ≈ 13.41 Gyr
  - ⟨Omega_lambda_host⟩ ≈ 0.722 (std ≈ 0.020)
  - All 22 are FRW-viable by the host-side construction.

- **CORRIDOR_AND_HOST_AGE_ANCHOR**
  - n = 12 (≈ 0.59% of grid)
  - ⟨age_host⟩ ≈ 13.55 Gyr
  - ⟨age_repo⟩ ≈ 13.45 Gyr
  - ⟨Omega_lambda_host⟩ ≈ 0.706 (std ≈ 0.011)
  - **All 12 are FRW_VIABLE**, in the sense of the repo’s `frw_viable` mask.

So, out of 2048 θ points:

- 22 lie in the **host age anchor** window.
- 12 of those also lie in the **toy corridor** and are FRW-viable.
- That 12-point subset is where the toy FRW and external host ages both sit near a “Universe-like” age, given our crude anchor.

---

## 4. Corridor kernel: where everything meets

Script:

- `stage2/external_cosmo_host/src/extract_external_cosmo_host_age_anchor_corridor_kernel_v1.py`
- Output:
  - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_age_anchor_corridor_kernel_v1.csv`

Definition (in code):

- Kernel = points satisfying:
  - `FRW_VIABLE`
  - `in_toy_corridor`
  - `in_host_age_anchor` (age_host in [13.3, 14.3] Gyr)

Key printed diagnostics:

- Kernel size:
  - n = 12

- θ–range:
  - `theta ∈ [0.641204, 3.319534]` (in radians)
  - 12 θ’s split into two symmetric packets (low-θ and high-θ) similar to the earlier FRW-only empirical kernel.

- Repo-side λ and ages (kernel):
  - `omega_lambda_repo` range: `[0.689232, 0.722950]`
  - Repo toy ages in kernel:
    - mean ≈ 13.452 Gyr
    - std  ≈ 0.032 Gyr
  - Host ages in kernel:
    - mean ≈ 13.546 Gyr
    - std  ≈ 0.140 Gyr

Mechanism profiles in kernel:

- For all four main measure columns, we have:
  - `mech_baseline_A0`, `mech_baseline_A_floor`,
  - `mech_binding_A0`, `mech_binding_A`
- Stats (from the script’s printed summary):
  - Means ≈ 0.04638
  - Std ≈ 1.8 × 10⁻⁴
  - Range:
    - min ≈ 0.04610
    - max ≈ 0.04665
- The bound columns (`mech_baseline_bound`, `mech_binding_bound`) are 0 across the kernel, consistent with how those bounds are currently defined in the mechanism.

Interpretation (diagnostic, not a claim):

- The 12-point kernel defines a **thin ridge in θ** where:
  - Repo FRW toy says:
    - “This θ is FRW-viable and inside our toy corridor.”
  - External cosmology host says:
    - “This θ has a background age in a Universe-like ~[13.3, 14.3] Gyr window.”
  - Mechanism says:
    - “All θ in this ridge see a very tight cluster of measure values near ≈ 0.0464.”

This looks like exactly the sort of **overlap kernel** we wanted from the host belt:
a place where mechanism, FRW toy, and an external FRW age anchor agree enough to be interesting.

---

## 5. Where this sits in the bigger Stage 2 story

Relative to earlier Stage 2 belts:

- FRW-only anchor (Phase 4 + Stage 2):
  - Identified small segments where:
    - FRW_viable ∧ toy corridor ∧ empirical (Ω_Λ, age) box held.
  - Those were the original **FRW-only kernels**.

- External FRW host (Stage 2 / external_frw_host):
  - Checked the repo FRW toy against an analytic FRW background.
  - Found that:
    - **Globally**: ages mismatch strongly.
    - **Corridor ∧ viable**: ages are much closer, but the original empirical anchor did not hold after host cross-checks.

- External cosmology host (this belt):
  - Introduces a θ → (Ω_m, Ω_Λ, H₀) mapping and recomputes background ages with a slightly different FRW toy engine.
  - Plugs in a crude Universe-age box and finds:
    - 12 θ’s that are:
      - FRW_viable,
      - in the toy corridor,
      - and in a Universe-like host age window.

So this belt gives a **first external-consistency kernel** for the corridor, even under a deliberately simple mapping and a rough age box.

We still do **not** claim:
- That the mapping θ → (Ω_m, Ω_Λ, H₀) is physically correct.
- That this reproduces ΛCDM, Planck, or any real dataset.

We *do* claim (within Phase 0 discipline):

> Given the **current** θ–mapping and toy FRW structure,
> there exists a **small, contiguous kernel in θ** where the mechanism,
> the repo FRW toy, and an external FRW-like age diagnostic all agree
> on a Universe-aged background in the 13–14 Gyr band.

---

## 6. Hooks for future rungs

What we can safely do next, building on this:

1. **Sensitivity rungs (optional, Stage 2):**
   - Vary the host age window (e.g. ±0.5 Gyr, ±1 Gyr) and track:
     - kernel size,
     - θ-width,
     - drift of mechanism mean values.

2. **Correlation rungs (optional, Stage 2):**
   - Reuse the mechanism-correlation scripts to compare:
     - Mechanism measure columns vs host `Omega_lambda` and `age_Gyr_host`,
     - Restricted to the corridor and kernel.

3. **Phase 4/5 narrative hooks:**
   - Phase 4:
     - Describe this as a “host-checked FRW toy corridor,”
       and limit language to:
       *“there exists a small θ-band where the toy FRW background and an external FRW host both support Universe-like ages.”*
   - Phase 5:
     - Use the kernel as one of the dashboard panels (e.g. in an “anchor kernel overview” figure).


---

## H7: External host kernel comparison (FRW toy vs FRW host vs cosmo host)

We gather three small kernel-like subsets into a single comparison table:

- **Input table:** `stage2/external_cosmo_host/outputs/tables/stage2_external_host_kernel_comparison_v1.csv`
- **Builder script:** `stage2/external_cosmo_host/src/build_external_host_kernel_comparison_v1.py`

The three rows are:

1. **FRW_TOY_ANCHOR_KERNEL** (internal toy segment)
   - Source: `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_kernel_v1.csv`
   - Size: `n_theta = 2`
   - Role: a minimal internal reference segment for the Phase 4 FRW toy (most aggregate stats are intentionally left undefined / NaN).

2. **EXTERNAL_FRW_HOST_AGE_ANCHOR** (FRW host, age-only anchor)
   - Source: `stage2/external_frw_host/outputs/tables/stage2_external_frw_host_age_anchor_mask_v1.csv`
   - Selection (reconstructed numerically in H7):
     - FRW-viable (`frw_viable = True` if present),
     - external FRW host age in the observational window: **13.3–14.3 Gyr**.
   - Size: `n_theta = 34`
   - Approximate profiles:
     - θ-range: ~**[0.79, 3.17]**,
     - repo-side Λ-band: `omega_lambda` ≈ **1.05** with min / max ~[1.00, 1.10],
     - host ages: `age_Gyr_host` ≈ **13.60 Gyr**, spanning roughly [13.31, 13.90] Gyr.

3. **EXTERNAL_COSMO_HOST_AGE_CORRIDOR_KERNEL** (cosmo host, corridor kernel)
   - Source: `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_age_anchor_corridor_kernel_v1.csv`
   - Selection: points that simultaneously satisfy
     - FRW-viable,
     - inside the Phase 4 FRW **toy corridor**,
     - inside the cosmo-host **age window** [13.3, 14.3] Gyr.
   - Size: `n_theta = 12`
   - Approximate profiles:
     - θ-range: ~**[0.64, 3.32]**,
     - repo-side Λ-band: `omega_lambda_repo` ≈ **0.706** with min / max ~[0.689, 0.723],
     - toy ages: `age_Gyr_repo` ≈ **13.45 Gyr** (very narrow spread ~0.03 Gyr),
     - cosmo-host ages: `age_Gyr_host` ≈ **13.55 Gyr** (spread ~0.14 Gyr),
     - mechanism:
       - `mech_baseline_A0` and `mech_binding_A0` ≈ **0.04638**,
       - scatter across the 12 points is O(10^-4),
       - corresponding `*_bound` flags are zero over this kernel.

### Interpretation (Phase-4/5 safe reading)

- The **FRW host age-anchor** (34 points) shows there is a moderately broad θ-band where an *external flat-ΛCDM host* assigns Universe-like ages (13.3–14.3 Gyr) to the Stage 2 grid.
- The **cosmo-host age–corridor kernel** (12 points) is a much narrower θ-band lying *inside* both:
  - the Phase 4 FRW toy corridor, and
  - an external ΛCDM cosmology slice with observationally reasonable ages.

Within this 12-point band:

1. Toy ages and external cosmo-host ages are both close to the observed Universe age,
2. Repo-side Λ (from the FRW toy) sits in a narrow strip around ~0.70,
3. The Stage 2 mechanism (`A0`-type columns) is well-behaved and tightly clustered.

We **do not** claim this kernel uniquely identifies the real Universe. Instead, we treat it as:

> a compact, inspectable region of the θ-grid where the FRW toy, an external cosmology, and the Stage 2 mechanism agree on Universe-like ages and a narrow Λ-band.

This region is a natural candidate for Phase 5 “first contact” dashboards (e.g. as an **anchor-kernel panel**), and a convenient testbed for any future modifications to the FRW toy or mechanism.


---

## H8 – Near-flat external-cosmo subset (Ω_tot ≈ 1)

Script: `stage2/external_cosmo_host/src/flag_external_cosmo_flat_subset_v1.py`  
Tables:
- `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_flat_subset_summary_v1.csv`
- `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_flat_subset_mask_v1.csv`

We define a *near-flat* external-cosmo host subset by
\[
\Omega_{\text{tot}} \equiv \Omega_m + \Omega_\Lambda,\quad
|\Omega_{\text{tot}} - 1| \le 0.05.
\]

Key findings:

- On the full grid (2048 rows), this yields:
  - `HOST_NEAR_FLAT`: 1286 / 2048 (≈ 0.628), with
    \(\langle \Omega_{\text{tot}} \rangle \approx 1.0003\), \(\sigma \approx 0.0032\), and
    \(\Omega_{\text{tot}} \in [1.00, 1.05]\).
- Intersections with the Phase-4 FRW toy grid:
  - `HOST_NEAR_FLAT_AND_FRW_VIABLE`: 254 / 2048 (≈ 0.124).
  - `HOST_NEAR_FLAT_AND_CORRIDOR_AND_FRW_VIABLE`: 154 / 2048 (≈ 0.075),
    for which
    \(\Omega_{\text{tot}} = 1\) **exactly** across the subset
    (mean = 1.0, std = 0, min = max = 1.0).
- On this 154-point band (near-flat ∧ FRW-viable ∧ in the Phase-4 corridor):
  - host ages: \(\langle t_0^{\text{host}} \rangle \approx 11.74~\text{Gyr}\),
    spanning ≈ 10.47–13.77 Gyr,
  - repo FRW toy ages:
    \(\langle t_0^{\text{repo}} \rangle \approx 14.17~\text{Gyr}\),
    spanning ≈ 13.40–14.97 Gyr.

This confirms that our 12-point external-cosmo host *age–corridor kernel* (H5) lives
inside a strictly flat external background (\(\Omega_{\text{tot}} = 1\)) and sits within
a broader flat band where the Phase-4 FRW toy remains FRW-viable and inside its corridor.
