# STAGE2_EXTERNAL_COSMO_HOST_DESIGN_v1

Status: draft design (Stage 2 belt, not yet promoted)  
Owner: Origin-Axiom Stage 2 (FRW + mechanism)  
Scope: external cosmology host for background-only diagnostics

---

## 0. Purpose and Phase 0 constraints

This document defines a Stage 2 belt that connects the Origin-Axiom θ-grid to an
external cosmology “host” (analytic FRW, CLASS/CCL, etc.) in a way that:

- **Respects Phase 0 discipline:**
  - external codes are used as diagnostic hosts, not oracles,
  - no new physical claims are made at Phase 2/3/4 without explicit gates;
- **Re-uses the existing Stage 2 infrastructure:**
  - joint θ-grid from `stage2/joint_mech_frw_analysis`,
  - FRW masks and empirical anchors from the FRW toy and host belts;
- **Prepares for Stage II:**
  - the interfaces are designed so that, later, CLASS/CCL/Cobaya/CosmoSIS can
    be plugged in without changing the Stage 2 contract.

The belt is **background-only** at v1: it computes FRW background quantities like
age, H(z), and distances. No likelihoods and no perturbation observables (C_ℓ, P(k))
are touched in this first version.

---

## 1. Inputs and outputs

### 1.1 Canonical inputs

The external cosmology host belt consumes:

- Joint θ-grid (from Stage 2 mech–FRW belt):

  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv`

  Expected columns (current baseline):

  - `theta_index`
  - `theta`
  - `E_vac`
  - `omega_lambda`
  - `age_Gyr` (Phase 4 FRW toy age)
  - `in_toy_corridor`
  - `frw_viable`
  - `lcdm_like`
  - `shape_and_viable`
  - `shape_and_lcdm`
  - `frw_data_ok`
  - `mech_baseline_A0`
  - `mech_baseline_A_floor`
  - `mech_baseline_bound`
  - `mech_binding_A0`
  - `mech_binding_A`
  - `mech_binding_bound`

- FRW empirical anchor mask:

  - `stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_empirical_anchor_mask_v1.csv`

  Expected columns (current baseline):

  - `theta`
  - `in_empirical_anchor_box` (bool)

- External FRW host bridge table (v0 analytic host):

  - `stage2/external_frw_host/outputs/tables/stage2_external_frw_background_bridge_v1.csv`

  Expected columns (current baseline):

  - `theta_index`
  - `theta`
  - `omega_lambda`
  - `age_Gyr_toy`   (Phase 4 FRW toy age)
  - `age_Gyr_host`  (analytic flat–ΛCDM host age)
  - `frw_viable`

### 1.2 New outputs (this belt)

At v1, the external cosmology host belt will produce:

- Cosmological-parameter grid:

  - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_params_grid_v1.csv`

  Columns (v1, background-only):

  - `theta_index`
  - `theta`
  - `omega_lambda_repo`   (from joint θ-grid)
  - `age_Gyr_repo`        (FRW toy age from joint θ-grid)
  - `Omega_m`             (toy mapping, see §2)
  - `Omega_lambda`        (toy mapping, see §2)
  - `H0_km_s_Mpc`         (fixed or θ-dependent toy choice, v1 fixed)
  - optionally `w0`, `wa` (defaulting to -1, 0 for ΛCDM-like mapping)

- Host background grid (v1 analytic host wrapper):

  - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_background_grid_v1.csv`

  Columns (v1):

  - `theta_index`
  - `theta`
  - `Omega_m`
  - `Omega_lambda`
  - `H0_km_s_Mpc`
  - `age_Gyr_host`      (from external host)
  - optionally: `age_rel_diff_vs_repo`, `age_diff_vs_repo`
  - optionally: simple distances (comoving distance to z=1, etc.) in future rungs.

These outputs are designed so that:

- Stage 2 can compare **repo toy age** vs **host age** vs **empirical-age window**;
- later, a CLASS/CCL/Cobaya host can compute richer observables without changing
  the columns carrying `theta`, `Omega_m`, `Omega_lambda`, `H0_km_s_Mpc`.

---

## 2. θ → cosmological parameters mapping layer

The mapping layer is defined by:

- `stage2/external_cosmo_host/src/oa_theta_to_cosmo_params_v1.py`

Contract:

- Reads the joint θ-grid;
- For each θ-row, emits a corresponding cosmology parameter row:

  - `Omega_lambda` is a function of the repo’s `omega_lambda` column
    (v1: simply copy it; later: more refined mapping is allowed but must be
    fully documented);
  - `Omega_m` is set such that spatial curvature is zero at v1:

    - v1 toy choice: `Omega_m = max(0, 1 - Omega_lambda)` ignoring radiation;
    - later versions may add Ω_r, Ω_k with explicit documentation;

  - `H0_km_s_Mpc` is a fixed reference value at v1:

    - v1 toy choice: 70 km/s/Mpc (exact value not a claim, just a reference scale);

  - optional `w0`, `wa` can be set to (-1, 0) at v1.

Non-claims:

- This mapping is a **toy projection** of Origin-Axiom θ onto a standard FRW
  parameter slice, not a derived prediction for the real Universe.
- All θ → params relations are subject to change under explicit, gated design updates.

---

## 3. Host background layer (analytic host at v1)

The host background script at v1:

- `stage2/external_cosmo_host/src/run_cosmo_host_background_grid_v1.py`

Contract:

- Reads `stage2_external_cosmo_params_grid_v1.csv`;
- For each row, computes the FRW background age for a flat Universe with:
  - given `Omega_m`, `Omega_lambda`, `H0_km_s_Mpc`,
  - standard FRW integral for t₀, optionally ignoring radiation;
- Writes `stage2_external_cosmo_host_background_grid_v1.csv` with host ages.

At v1, the “host” implementation is allowed to reuse the same analytic FRW
integrator already used in the `stage2/external_frw_host` belt. The important part
is **interface and table structure**, not physical sophistication.

Later:

- The implementation inside `run_cosmo_host_background_grid_v1.py` can be swapped
  to call CCL, CLASS, PyCosmo, etc. as long as:
  - the input columns (`theta`, `Omega_m`, `Omega_lambda`, `H0_km_s_Mpc`) are
    preserved;
  - the output contract (per-θ background quantities) is preserved.

---

## 4. Rungs for this belt (v1)

We define the following rungs for the external cosmology host belt:

- **H1 – Mapping rung (θ → params)**

  - Script: `oa_theta_to_cosmo_params_v1.py`
  - Output: `stage2_external_cosmo_params_grid_v1.csv`
  - Checks:
    - number of rows matches joint θ-grid,
    - `Omega_m + Omega_lambda` is close to 1 on the FRW-viable set,
    - no negative `Omega_m` or `Omega_lambda`.

- **H2 – Background host rung (params → age)**

  - Script: `run_cosmo_host_background_grid_v1.py`
  - Output: `stage2_external_cosmo_host_background_grid_v1.csv`
  - Checks:
    - number of rows matches mapping grid,
    - ages are finite and positive for all FRW-viable rows,
    - qualitative trend: age_host increases with Omega_lambda on the viable set.

- **H3 – Comparison rung (repo vs host vs anchors)**

  - Script: to be defined (future)
  - Input:
    - joint θ-grid,
    - FRW empirical anchor mask,
    - host background grid.
  - Output:
    - a table summarising:
      - overlaps between:
        - FRW-viable set,
        - toy corridor,
        - repo empirical age box,
        - host age box around the observed Universe age.
  - This rung is where we re-ask, with a better host, whether any θ interval
    can simultaneously satisfy:
    - mechanism corridor,
    - FRW viability,
    - empirical age constraints.

At v1 we will implement H1 and H2 fully, and stub H3 as a design placeholder.

---

## 5. Phase 0 and promotion / non-promotion

- The external cosmology host belt is **Stage 2 only** at v1.
- No new claims about “fitting ΛCDM” or “predicting Ω\_Λ, H₀” are allowed.
- Any plot or number extracted from this belt must be framed as:
  - “Given this θ → params mapping and this external FRW host, the following
    θ-rows produce FRW backgrounds that do / do not lie in a specified box.”

Promotion to Stage II:

- Only after:
  - the mapping layer stabilises (explicit versioning),
  - the host implementation moves from analytic toy to a validated library
    (CLASS/CCL/PyCosmo),
  - and an explicit Stage II gate document is added (likelihoods, data-contact).

