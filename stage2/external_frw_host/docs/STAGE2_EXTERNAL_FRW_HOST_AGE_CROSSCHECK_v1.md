# Stage 2 — External FRW Host Age Cross-Check (Rung X1)

**Status:** Diagnostic, Stage 2 only.  
**Scope:** Compare the Phase 4 FRW toy age column against an external, analytic flat-FRW host to check whether the Phase 4 quantities can be treated as literal ΛCDM parameters.

---

## 1) Code and inputs

This rung is implemented by:

- `stage2/external_frw_host/src/compute_analytic_frw_ages_v1.py`

It reads:

- Joint θ-grid (Phase 4 + mechanism):
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv`

and uses the columns:

- `theta_index`, `theta`
- `omega_lambda`          (Phase 4 FRW toy vacuum fraction)
- `age_Gyr`               (Phase 4 FRW toy age in Gyr)
- `frw_viable`            (Phase 4 FRW background viability mask)

The script writes:

- `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung1_age_crosscheck_v1.csv`

Each row of this table contains:

- `theta_index`, `theta`
- `omega_lambda`
- `age_Gyr`       – age from the Phase 4 FRW toy pipeline
- `age_Gyr_host`  – age from the external analytic FRW host
- `age_Gyr_diff`  – `age_Gyr_host - age_Gyr`
- `age_Gyr_rel_diff` – relative difference, `(age_Gyr_host - age_Gyr) / age_Gyr`
- `frw_viable`    – Phase 4 viability flag

---

## 2) External FRW host model

The external host uses a simple flat-FRW background:

- Universe assumed spatially flat with:
  - \\\( \Omega_\Lambda = \texttt{omega\_lambda} \\\)
  - \\\( \Omega_m = 1 - \Omega_\Lambda \\\)
  - radiation neglected at late times.

The dimensionless age is computed as:

\\[
t_0 H_0 \;=\; \int_{a_\text{min}}^1 \frac{da}{a \sqrt{\Omega_m a^{-3} + \Omega_\Lambda}}\,,
\\]

where:

- \\\( a_\text{min} \\\) is a small scale factor cutoff to avoid the Big Bang singularity in the integrand,
- the integral is evaluated numerically for each \\\( \Omega_\Lambda \\\).

The resulting dimensionless ages are then converted to Gyr by fitting a **single global scale factor** so that the host ages best match the Phase 4 ages on the FRW-viable subset:

- `age_Gyr_host = scale_factor * t0_dimless`.

This is intentionally minimal:

- it does not model radiation, curvature, or any perturbation physics,
- it treats `omega_lambda` purely as a background vacuum fraction in a vanilla flat-FRW toy.

---

## 3) Summary of results

For the current snapshot (2048-point θ-grid):

- FRW-viable subset:
  - `frw_viable == 1` for 1016 out of 2048 points (≈ 49.6% of the grid).

On this subset, the script finds:

- Fitted global scale factor:
  - \\\( \texttt{scale\_factor} \approx 2.75 \\\) Gyr per unit of dimensionless age.
- Age comparison on the FRW-viable set:
  - Mean absolute difference:
    - \\\( \langle |t_{\text{host}} - t_{\text{repo}}| \rangle \approx 2.7 \\\) Gyr
  - Maximum absolute difference:
    - \\\( \max |t_{\text{host}} - t_{\text{repo}}| \approx 12.9 \\\) Gyr
  - Mean absolute relative difference:
    - \\\( \langle |(t_{\text{host}} - t_{\text{repo}}) / t_{\text{repo}}| \rangle \approx 0.20 \\\)

At the low-\\( \Omega_\Lambda \\\) end of the grid, the mismatch can be very large. For example:

- For \\\( \Omega_\Lambda \approx 0.0605 \\\):
  - Phase 4 toy age: \\\( t_{\text{repo}} \approx 16.48 \\\) Gyr
  - Host age: \\\( t_{\text{host}} \approx 1.87 \\\) Gyr (after applying the fitted scale)
  - Difference: \\\( t_{\text{host}} - t_{\text{repo}} \approx -14.6 \\\) Gyr

This illustrates that the Phase 4 `age_Gyr` column is not simply the age of a flat-FRW model with \\\( \Omega_m = 1 - \Omega_\Lambda \\\) and fixed \\\( H_0 \\\).

---

## 4) Interpretation

This rung is a **cross-check**, not a replacement for Phase 4:

- It confirms that:
  - Phase 4 FRW quantities (`omega_lambda`, `age_Gyr`) are **FRW-inspired toy diagnostics**, not literal ΛCDM parameters wired into a standard background solver.
  - A very simple external flat-FRW host, even after a global rescaling, only matches the Phase 4 ages at the ~20% level on average, and can deviate far more in some regions.

As a result:

- We should **not** silently treat:
  - `omega_lambda` as a direct proxy for the cosmological constant density fraction in a standard ΛCDM model, or
  - `age_Gyr` as the true ΛCDM age of the Universe,
  without an explicit mapping layer and a dedicated gate.

Within the program:

- Phase 4 remains a **toy FRW diagnostic stub** with its own internal mapping from mechanism outputs to FRW-like quantities.
- Stage 2’s external FRW host is a **downstream diagnostic only**, used to:
  - sanity-check shapes and scales,
  - prevent accidental over-interpretation of the Phase 4 columns,
  - and inform any future design of a more realistic host (e.g. CLASS/CCL-based) under a new gate.

---

## 5) Relation to empirical anchors

This rung is related to, but distinct from, the empirical anchor belt:

- The **empirical anchor** belt defines a tiny “background data box” in the Phase 4 FRW space and asks whether any \\\( \theta \\\) survive the intersection of:
  - mechanism corridor,
  - FRW viability,
  - and this data-like box.
- The **external FRW host** rung instead asks:
  - “If we try to view Phase 4’s `omega_lambda` and `age_Gyr` through the lens of a simple flat-FRW background with \\\( \Omega_m = 1 - \Omega_\Lambda \\\), how far off are we?”

Both rungs support the same governance point:

- Any future move toward **real** cosmological data contact must introduce:
  - an explicit mapping layer from \\\( \theta \\\) to standard cosmological parameters,
  - a clear Phase 0 gate,
  - and careful documentation of which quantities are toy diagnostics and which are being treated as data-facing.

