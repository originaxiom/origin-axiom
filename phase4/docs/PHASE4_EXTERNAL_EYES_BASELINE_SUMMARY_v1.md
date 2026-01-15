# Phase 4 external-eyes baseline summary (FRW F1 + Stage 2 host kernel)

**Tag:** `stage2_phase4_F1_FRW_baseline_checkpoint_2026-01-15`  
**Scope:** External-eyes narrative of what is *actually computed* in the current
Phase 4 F1 FRW mapping and its Stage 2 external-cosmo host bridge. No new
numerics are introduced here; everything is a paraphrase or re-grouping of
existing tables, scripts, and artifacts in the repo.

This document is meant to be readable on its own by a careful external reader
who has the actual repository. It stays within the Phase 0 contract:
- No claims beyond what is explicitly computed in the repo.
- No uniqueness or discovery claims about a specific value of \(\theta_\star\).
- No probabilistic / statistical weighting of different \(\theta\)-regions.
It is *only* a structural summary of the current baseline F1 configuration.

---

## 0. Objects in play

This summary is about the interaction of three components:

1. **Phase 4 F1 FRW backbone (toy cosmology)**
   - F1 vacuum mapping and FRW backbone:
     - `phase4/src/phase4/run_f1_sanity.py`
     - `phase4/outputs/tables/phase4_F1_sanity_curve.csv`
   - FRW age and viability diagnostics:
     - `phase4/src/phase4/run_f1_frw_toy_diagnostics.py`
     - `phase4/outputs/tables/phase4_F1_frw_toy_diagnostics.json`
     - `phase4/outputs/tables/phase4_F1_frw_viability_mask.csv`
     - `phase4/outputs/tables/phase4_F1_frw_viability_diagnostics.json`
   - FRW shape corridor (E\_vac corridor):
     - `phase4/src/phase4/run_f1_shape_diagnostics.py`
     - `phase4/outputs/tables/phase4_F1_shape_mask.csv`
     - `phase4/outputs/tables/phase4_F1_shape_diagnostics.json`
   - FRW \(\Lambda\)CDM-like probe:
     - `phase4/src/phase4/run_f1_frw_lcdm_probe.py`
     - `phase4/outputs/tables/phase4_F1_frw_lcdm_probe_mask.csv`
     - `phase4/outputs/tables/phase4_F1_frw_lcdm_probe.json`
   - Phase 4 paper + artifact:
     - `phase4/paper/main.tex`
     - `phase4/outputs/paper/phase4_paper.pdf`
     - `phase4/artifacts/origin-axiom-phase4.pdf`
     - top-level copy: `artifacts/origin-axiom-phase4.pdf`

2. **Stage 2 external-cosmo host kernel**
   - Joint grid and external host backgrounds:
     - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv`
     - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_params_grid_v1.csv`
     - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_background_grid_v1.csv`
   - Near-flat subset (host-side \(|\Omega_{\mathrm{tot}} - 1| \le 0.05\)):
     - `stage2/external_cosmo_host/src/flag_external_cosmo_flat_subset_v1.py`
     - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_flat_subset_mask_v1.csv`
     - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_flat_subset_summary_v1.csv`
   - Age-anchored corridor kernel (12-point external host kernel for Phase 4):
     - `stage2/external_cosmo_host/src/build_external_cosmo_host_age_anchor_corridor_kernel_v1.py`
     - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_age_anchor_corridor_kernel_v1.csv`
   - Kernel cross-checks:
     - `stage2/external_cosmo_host/src/check_external_cosmo_host_kernel_consistency_v1.py`
     - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_kernel_consistency_v1.csv`
     - `stage2/external_cosmo_host/src/build_external_cosmo_host_phase4_constraints_v1.py`
     - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_phase4_constraints_v1.csv`
   - Omega naming + near-flat + H\(_0\) bands:
     - `stage2/external_cosmo_host/src/scan_external_host_omega_naming_v1.py`
     - `stage2/external_cosmo_host/outputs/tables/stage2_external_host_omega_naming_scan_v1.csv`
     - `stage2/docs/STAGE2_OMEGA_NAMING_AND_MAP_v1.md`
     - `stage2/external_cosmo_host/src/build_external_cosmo_host_kernel_H0_band_v1.py`
     - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_kernel_H0_band_v1.csv`
     - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_kernel_H0_band_summary_v1.csv`

3. **Bridging docs and Phase 4 paper wiring**
   - External host kernel bridge:
     - `phase4/docs/PHASE4_EXTERNAL_HOST_KERNEL_BRIDGE_v1.md`
   - F1 FRW baseline checkpoint:
     - `phase4/docs/PHASE4_FRW_F1_BASELINE_CHECKPOINT_v1.md`
   - Stage 2 / Phase 4 FRW + host summary:
     - `stage2/docs/STAGE2_PHASE4_FRW_HOST_SUMMARY_v1.md`
   - External host kernel paper table:
     - `phase4/src/build_phase4_external_host_kernel_table_v1.py`
     - `phase4/outputs/tables/phase4_external_host_kernel_constraints_v1.tex`
   - Global tag capturing this configuration:
     - `stage2_phase4_F1_FRW_baseline_checkpoint_2026-01-15`

Everything below is a prose summary of what these pieces jointly say.

---

## 1. FRW-only story (Phase 4 F1 baseline)

### 1.1 F1 vacuum mapping and FRW viability

The F1 baseline mapping takes the Phase 3 mechanism table
(`phase3/outputs/tables/mech_baseline_scan_diagnostics.json`) and defines a
vacuum curve \(E_{\mathrm{vac}}(\theta)\) on a 2048-point grid in \(\theta\) with
\(\theta \in [0, 2\pi)\).

From `phase4_F1_sanity_curve.csv` and `phase4_F1_frw_toy_diagnostics.json`:

- Grid:
  - \(n_{\theta} = 2048\).
  - \(\theta_{\min} = 0\), \(\theta_{\max} \approx 6.2801\).
- E\_vac summary:
  - \(E_{\mathrm{vac}, \min} \approx 4.0 \times 10^{-7}\).
  - \(E_{\mathrm{vac}, \max} \approx 1.1 \times 10^{-5}\).
  - \(E_{\mathrm{vac}, \mathrm{mean}} \approx 4.6 \times 10^{-6}\).

The FRW backbone uses a fixed toy matter budget:

- \(\Omega_m = 0.3\),
- \(\Omega_r = 0\),
- and assigns \(\Omega_\Lambda(\theta)\) from the F1 mapping, so that
  \(\Omega_\Lambda\) ranges from about \(0.06\) up to about \(1.69\) across the grid,
  with mean \(0.7\) (as encoded in the diagnostics).

The FRW viability diagnostics (`phase4_F1_frw_viability_mask.csv` and
`phase4_F1_frw_viability_diagnostics.json`) report:

- Fraction FRW-viable:
  - `frac_viable` = 0.49609375, i.e. about 50% of the \(\theta\)-grid.
- Age range over the full grid:
  - `age_Gyr_min` ≈ 11.46 Gyr,
  - `age_Gyr_max` ≈ 16.48 Gyr,
  - `age_Gyr_mean` ≈ 14.20 Gyr.
- Additional Boolean flags (matter era, late acceleration, smooth \(H^2\))
  are all satisfied in the viable set for the baseline configuration.

The FRW viability mask also encodes a *single continuous* viable corridor:

- `theta_min_global` = 0.0,
- `theta_max_global` ≈ 6.2801 (full grid),
- principal FRW corridor (from the dedicated corridor diagnostic):
  - `theta_min` ≈ 0.4264,
  - `theta_max` ≈ 3.5404,
  - `n_points` = 1016 (matching the number of viable grid points).

So, **FRW-only takeaway:** about half of the \(\theta\)-grid is FRW-viable in this
baseline, forming one long corridor from \(\theta \approx 0.43\) to
\(\theta \approx 3.54\), with ages spanning ≈ 11.5–16.5 Gyr and
\(\Omega_\Lambda(\theta)\) spanning ≈ 0.06–1.69.

### 1.2 Shape corridor (E\_vac-based)

The shape corridor is a toy, non-binding diagnostic combining \(E_{\mathrm{vac}}(\theta)\)
with a simple “one sigma above the global minimum” rule:

- Corridor definition:
  - \(E_{\mathrm{vac}}(\theta) \le E_{\mathrm{vac}, \min} + k_\sigma \sigma\),
  - with `k_sigma = 1.0` in the baseline.
- Diagnostics (`phase4_F1_shape_diagnostics.json`):
  - `corridor_fraction` = 0.5791015625 (about 58% of grid).
  - `corridor_theta_min` = 0.0,
  - `corridor_theta_max` ≈ 6.2801.

Thus the *shape*-based corridor is wide and basically covers a large fraction of
the circle; it is not, by itself, the “selection”. The FRW viability and
external host constraints do the narrowing.

### 1.3 ΛCDM-like window

The ΛCDM-like probe (`phase4_F1_frw_lcdm_probe.json` and mask) is defined by:

- FRW viability (must be in the FRW-viable set).
- Target cosmology:
  - `omega_lambda_target` = 0.7, tolerance ±0.1.
  - `age_target_Gyr` = 13.8 Gyr, tolerance ±1 Gyr.

Diagnostics report:

- `n_grid` = 2048 (full grid),
- `n_frw_viable` = 1016,
- `n_lcdm_like` = 63,
- `lcdm_like_fraction` ≈ 0.03076 (≈ 3.1% of the full grid),
- \(\theta\) range of ΛCDM-like subset:
  - `theta_min_lcdm` ≈ 0.5983,
  - `theta_max_lcdm` ≈ 3.3625.
- Ω\(_\Lambda\) range within ΛCDM-like subset:
  - `omega_lambda_min_lcdm` ≈ 0.6031,
  - `omega_lambda_max_lcdm` ≈ 0.7982.
- Age range within ΛCDM-like subset:
  - `age_Gyr_min_lcdm` ≈ 13.19 Gyr,
  - `age_Gyr_max_lcdm` ≈ 13.77 Gyr.

So the ΛCDM-like *window* is a proper subset of the FRW corridor:

- Still continuous in \(\theta\),
- Nested inside the FRW-viable band,
- Occupying about 3% of the full grid.

### 1.4 Shape + FRW + ΛCDM overlap

The combined probe (`phase4_F1_frw_shape_probe.json`) summarizes overlaps of:

- FRW viability mask,
- Shape corridor mask,
- ΛCDM-like mask.

Key reported fractions (relative to the full 2048-point grid):

- `frac_frw_viable` = 0.49609375 (≈ 49.6%),
- `frac_in_toy_corridor` = 0.5791015625 (≈ 57.9%),
- `frac_lcdm_like` = 0.03076171875 (≈ 3.1%),
- `frac_shape_and_viable` = 0.0751953125 (≈ 7.5%),
- `frac_shape_and_lcdm` = 0.01953125 (≈ 2.0%).

\(\theta\)-ranges:

- FRW-viable:
  - `theta_range_frw_viable` ≈ [0.4264, 3.5404].
- ΛCDM-like:
  - `theta_range_lcdm_like` ≈ [0.5983, 3.3625].
- Shape ∩ ΛCDM:
  - `theta_range_shape_and_lcdm` is the same [0.5983, 3.3625] in the
    baseline run.
- Shape ∩ FRW-viable:
  - `theta_range_shape_and_viable` ≈ [0.4264, 3.5404].

This already tells us, strictly within FRW + toy shape diagnostics:

> There is a non-trivial band of \(\theta\) where the F1 mapping yields a FRW-
> viable background, lies in a simple E\_vac shape corridor, and reproduces a
> flat-\(\Lambda\)CDM-like age and \(\Omega_\Lambda\) band at the toy level.

No claim is made here about **uniqueness** or about **probability**; the corridor
and window are **subsets**, not favored points.

---

## 2. Stage 2 external-cosmo host kernel

### 2.1 Near-flat subset and FRW viability

On the Stage 2 side, the joint grid and host background tables define:

- A 2048-point \(\theta\)-grid shared with the Phase 3/4 machinery.
- For each point, external host parameters:
  - \(\Omega_m\),
  - \(\Omega_\Lambda\),
  - \(H_0\) (in `H0_km_s_Mpc`),
  - host age \(t_{\mathrm{host}}(\theta)\).

The near-flat subset is defined as:

- \(|\Omega_{\mathrm{tot}}(\theta) - 1| \le 0.05\),
- where \(\Omega_{\mathrm{tot}} = \Omega_m + \Omega_\Lambda\).

From `stage2_external_cosmo_flat_subset_summary_v1.csv`:

- Whole grid:
  - `ALL_GRID`:
    - `n_theta` = 2048,
    - `Omega_tot_mean` ≈ 1.19,
    - `Omega_tot_min` ≈ 1.00,
    - `Omega_tot_max` ≈ 1.69.
- Near-flat host set:
  - `HOST_NEAR_FLAT`:
    - `n_theta` = 1286,
    - fraction ≈ 0.628 of the grid,
    - `Omega_tot_mean` ≈ 1.0003,
    - `Omega_tot_min` ≈ 1.0,
    - `Omega_tot_max` ≈ 1.047.
- Near-flat + FRW-viable:
  - `HOST_NEAR_FLAT_AND_FRW_VIABLE`:
    - `n_theta` = 254,
    - fraction ≈ 0.124,
    - `Omega_tot_mean` ≈ 1.0015.
- Near-flat + FRW-viable + toy-corridor:
  - `HOST_NEAR_FLAT_AND_CORRIDOR_AND_FRW_VIABLE`:
    - `n_theta` = 154,
    - fraction ≈ 0.0752,
    - `Omega_tot_mean` = 1.0 (to numerical precision).

So purely from the host + FRW side (before age/matching), about 7.5% of the grid
meets **all three** conditions:

- FRW-viable in the Phase 4 F1 sense.
- Inside the Phase 4 shape corridor.
- Host \(\Omega_{\mathrm{tot}}\) near 1 within ±0.05.

### 2.2 12-point age-anchored corridor kernel

The 12-point external host kernel is a *further* refinement of the joint set.

From `stage2_external_cosmo_host_phase4_constraints_v1.csv` and
`stage2_external_cosmo_host_age_anchor_corridor_kernel_v1.csv`, the kernel is:

- Name:
  - `EXTERNAL_COSMO_HOST_AGE_CORRIDOR_KERNEL`.
- Size:
  - `n_theta` = 12.
- \(\theta\) span:
  - `theta_min` ≈ 0.6412,
  - `theta_max` ≈ 3.3195.

On this kernel:

- Repo-side \(\Omega_\Lambda\) (Phase 4 F1 toy):
  - `omega_lambda_repo_min` ≈ 0.6892,
  - `omega_lambda_repo_max` ≈ 0.7230,
  - `omega_lambda_repo_mean` ≈ 0.7060.
- Host-side \(\Omega_\Lambda\):
  - `Omega_lambda_host_min` ≈ 0.6892,
  - `Omega_lambda_host_max` ≈ 0.7230,
  - `Omega_lambda_host_mean` ≈ 0.7060.

Age ranges:

- Repo FRW age (toy):
  - `age_Gyr_repo_min` ≈ 13.402,
  - `age_Gyr_repo_max` ≈ 13.502,
  - `age_Gyr_repo_mean` ≈ 13.452.
- Host age:
  - `age_Gyr_host_min` ≈ 13.334,
  - `age_Gyr_host_max` ≈ 13.768,
  - `age_Gyr_host_mean` ≈ 13.546.

Mechanism band (from Stage 3 baseline table carried through):

- `mech_baseline_A0_min` ≈ 0.04610,
- `mech_baseline_A0_max` ≈ 0.04665,
- `mech_baseline_A0_mean` ≈ 0.04638.

The consistency checker `check_external_cosmo_host_kernel_consistency_v1.py`
confirms that for these 12 points:

- All are FRW-viable in the Phase 4 sense (`n_frw_viable` = 12).
- All lie in the Phase 4 toy corridor (`n_in_corridor` = 12).
- All are classified as near-flat on the host side (`n_near_flat` = 12).
- Repo vs host \(\Omega_\Lambda\) differences:
  - Mean difference = 0, min = 0, max = 0 (to numerical precision).
- Repo vs host age differences:
  - `age_diff_Gyr_mean` ≈ +0.094 Gyr (host minus repo),
  - `age_diff_Gyr_min` ≈ −0.167 Gyr,
  - `age_diff_Gyr_max` ≈ +0.366 Gyr,
  - `age_abs_diff_Gyr_mean` ≈ 0.164 Gyr,
  - `age_abs_diff_Gyr_max` ≈ 0.366 Gyr.

So within this 12-point kernel:

> The Phase 4 FRW toy and the external flat-\(\Lambda\)CDM host agree on
> \(\Omega_\Lambda\) exactly (by construction) and on age to within a few tenths of
> a Gyr, while sharing FRW viability, shape corridor membership, and near-flat
> host curvature.

### 2.3 H\(_0\) and host bands

The H\(_0\)-band summary table
`stage2_external_cosmo_host_kernel_H0_band_summary_v1.csv` records, for this 12-
point kernel, the range of host-side \((\Omega_m, \Omega_\Lambda, H_0)\) that is
actually being used as external “eyeglasses” in the baseline.

We do not reinterpret or marginalize over those values here; we only note:

- The external host kernel is **not** a general cosmological fit.
- It is a *particular* band in \((\Omega_m, \Omega_\Lambda, H_0)\) space that
  (a) lies on the Stage 2 grid, and (b) is consistent with the FRW + corridor
  conditions described above, and (c) yields the near-flat, age-anchored
  12-point kernel used in Phase 4.

---

## 3. Intersection story: what this baseline says (and does not say)

### 3.1 Positive structural content

Taken together, the current baseline configuration supports the following
**positive but modest** statements:

1. **Non-empty structural overlap**
   - There exists a **non-empty, finite-measure band** of \(\theta\) for which:
     - Phase 4 FRW toy backgrounds are viable under the chosen F1 mapping.
     - The toy FRW ages and \(\Omega_\Lambda\) values sit inside a simple ΛCDM-like
       window (13.8 ± 1 Gyr, 0.7 ± 0.1).
     - A flat-\(\Lambda\)CDM external host with fixed \((\Omega_m, \Omega_\Lambda, H_0)\)
       grid assignments yields:
       - near-flat \(\Omega_{\mathrm{tot}}\) (|Ω\(_{\mathrm{tot}}\)−1| ≤ 0.05),
       - ages within a few tenths of a Gyr of the toy FRW ages,
       - exactly matching \(\Omega_\Lambda\) on the 12-point kernel.

2. **Corridor-within-corridor structure**
   - The 12-point kernel lives inside:
     - The FRW-viable corridor (≈ 50% of the grid),
     - A ΛCDM-like window (≈ 3% of the grid),
     - The near-flat host subset (≈ 63% of the grid),
     - The joint near-flat + FRW-viable + corridor set (≈ 7.5% of the grid).
   - This nested structure is *explicitly encoded* in the masks and summary tables;
     there is no hidden weighting or tuning beyond the mechanical rules already
     written in the scripts.

3. **Reproducible numeric bands**
   - All key numerical ranges (θ spans, Ω\(_\Lambda\) bands, age bands, mechanism band)
     are reproducibly stored in:
     - `phase4_F1_frw_viability_diagnostics.json`,
     - `phase4_F1_frw_lcdm_probe.json`,
     - `phase4_F1_frw_shape_probe.json`,
     - `stage2_external_cosmo_host_phase4_constraints_v1.csv`,
     - `stage2_external_cosmo_host_kernel_H0_band_summary_v1.csv`,
     - and are reflected in the Phase 4 paper table
       `phase4_external_host_kernel_constraints_v1.tex`.

### 3.2 Explicit non-claims

Equally important are the things this configuration **does not** claim:

- **No uniqueness of \(\theta_\star\):**
  - The corridor and kernel are *bands* in \(\theta\), not picks of a unique value.
  - There is no statistical or Bayesian preference implemented in this baseline.

- **No full-precision cosmological fit:**
  - The external host is a controlled flat-\(\Lambda\)CDM background *sampled on a grid*,
    not a global MCMC or parameter estimation pipeline.
  - The alignment is a structurally interesting overlap, not a best-fit claim.

- **No external dataset constraint yet:**
  - The Phase 4 FRW data probe is a **stub**:
    - `phase4_F1_frw_data_probe.json` reports `data_available = false`
      and `n_data_points = 0`.
    - No external distance-binned dataset is shipped in the repo at this tag.
  - Therefore there is no actual data-driven likelihood or chi-square evaluation
    restricting the host band beyond the grid + logic described above.

- **No extrapolation beyond the encoded grids:**
  - All conclusions are limited to the specific θ grid and parameter grids used
    in Stage 2 and Phase 4. There is no extrapolation to continuous parameter
    space beyond what the grids and masks already encode.

---

## 4. How an external reader can re-check this configuration

The minimal “external-eyes” rerun plan, assuming the repo is at the above tag:

1. **Check out the tagged baseline**
   - `git checkout stage2_phase4_F1_FRW_baseline_checkpoint_2026-01-15`

2. **Rebuild Stage 2 external host pieces**
   - `oa && python stage2/external_cosmo_host/src/flag_external_cosmo_flat_subset_v1.py`
   - `oa && python stage2/external_cosmo_host/src/build_external_cosmo_host_age_anchor_corridor_kernel_v1.py`
   - `oa && python stage2/external_cosmo_host/src/check_external_cosmo_host_kernel_consistency_v1.py`
   - `oa && python stage2/external_cosmo_host/src/build_external_cosmo_host_phase4_constraints_v1.py`
   - `oa && python stage2/external_cosmo_host/src/build_external_cosmo_host_kernel_H0_band_v1.py`

3. **Rebuild Phase 4 F1 FRW pipeline**
   - `oa && python phase4/src/phase4/run_f1_sanity.py`
   - `oa && python phase4/src/phase4/run_f1_shape_diagnostics.py`
   - `oa && python phase4/src/phase4/run_f1_frw_toy_diagnostics.py`
   - `oa && python phase4/src/phase4/run_f1_frw_corridors.py`
   - `oa && python phase4/src/phase4/run_f1_frw_lcdm_probe.py`
   - `oa && python phase4/src/phase4/run_f1_frw_data_probe.py`

4. **Rebuild Phase 4 paper and artifacts**
   - `oa && scripts/build_phase4_paper.sh`

5. **Confirm key bands in the resulting files**
   - From `phase4_F1_frw_viability_diagnostics.json`:
     - `frac_viable`, age range, and global θ range.
   - From `phase4_F1_frw_lcdm_probe.json`:
     - `lcdm_like_fraction`, θ, Ω\(_\Lambda\), and age ranges.
   - From `phase4_F1_frw_shape_probe.json`:
     - Overlap fractions and θ ranges for FRW-viable, corridor, and ΛCDM-like sets.
   - From `stage2_external_cosmo_host_phase4_constraints_v1.csv`:
     - 12-point kernel θ span, Ω\(_\Lambda\) bands, age bands, and A\(_0\) band.
   - From `stage2_external_cosmo_host_kernel_H0_band_summary_v1.csv`:
     - Host-side H\(_0\) and density bands used on the kernel.
   - From `phase4/outputs/paper/phase4_paper.pdf`:
     - The host kernel table and text statements that reference these bands.

If all of these values match the ranges summarized in this document, then the
external reader has independently confirmed the current baseline configuration
without relying on any unstated interpretation.

---

## 5. Position of this baseline in the broader Phase ladder

Within the multi-phase Origin Axiom ladder, this configuration is best read as:

- **Phase 3** provides a baseline mechanism table and vacuum energy curve.
- **Phase 4 (F1 baseline)** checks whether a simple, disciplined mapping from
  that mechanism into FRW backgrounds:
  - produces large, coherent FRW-viable corridors in \(\theta\),
  - admits an internal ΛCDM-like window with a reasonable age band,
  - and can structurally coexist with a flat-\(\Lambda\)CDM external host band
    without contradiction on age and \(\Omega_\Lambda\).

This is *not* yet a discovery claim. It is a **checkpoint**: the combination of
Phase 4 F1 FRW baseline and Stage 2 external host kernel forms a tightly
specified, reproducible “external-eyes” configuration that can be:

- Rebuilt from scratch by any careful reader,
- Critiqued in detail,
- And extended in future rungs (e.g. alternative mappings, richer host models,
  explicit data integration) without sacrificing the current clarity.
