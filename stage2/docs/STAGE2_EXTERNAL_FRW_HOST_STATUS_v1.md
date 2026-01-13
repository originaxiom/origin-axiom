# Stage 2 – External flat–FRW host (status v1)

**File:** `stage2/docs/STAGE2_EXTERNAL_FRW_HOST_STATUS_v1.md`  
**Scope:** Document the Stage 2 “external FRW host” belt that compares the Phase 4 FRW toy
age column (`age_Gyr`) to a simple external flat–FRW age calculation
\(t_0^{\text{(host)}}(\Omega_\Lambda)\). All results here are **diagnostic only** and do not
modify Phase 3 or Phase 4 claims.

---

## 1. Inputs, scripts, and outputs

**Upstream inputs**

- Joint mech–FRW θ-grid:
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv`
    - contains:
      - `theta_index`, `theta`
      - `omega_lambda`, `age_Gyr`, `frw_viable`
      - mechanism scalars (`mech_*` columns)
      - corridor / viability / LCDM-like masks

**External host scripts**

- `stage2/external_frw_host/src/compute_analytic_frw_ages_v1.py`
  - constructs a simple flat–FRW host age for each row of the joint grid.
- `stage2/external_frw_host/src/analyze_external_frw_age_contrast_v1.py`
  - summarises age differences between:
    - Phase 4 FRW toy age (`age_Gyr`),
    - external host age (`age_Gyr_host`),
    - across several θ-subsets.

**Outputs**

- Age cross-check table:
  - `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung1_age_crosscheck_v1.csv`
    - columns:
      - `theta_index`, `theta`
      - `omega_lambda`
      - `age_Gyr` (Phase 4 toy age)
      - `age_Gyr_host` (external flat–FRW host age, in Gyr)
      - `age_Gyr_diff = age_Gyr_host - age_Gyr`
      - `age_Gyr_rel_diff = age_Gyr_diff / age_Gyr`
      - `frw_viable` (Boolean mask copied from Phase 4)
- Age contrast summary:
  - `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung2_age_contrast_v1.csv`
    - per set:
      - `set`, `n_theta`, `frac_of_grid`
      - `age_Gyr_diff_mean`, `age_Gyr_diff_std`, `age_Gyr_diff_min`, `age_Gyr_diff_max`
      - `age_Gyr_rel_diff_mean`, `age_Gyr_rel_diff_std`,
        `age_Gyr_rel_diff_min`, `age_Gyr_rel_diff_max`

---

## 2. Host model definition (conceptual)

The “host” used here is a very simple flat–FRW toy:

- Interprets the Phase 4 `omega_lambda` column as:
  - \(\Omega_\Lambda\) in a flat \(\Omega_m + \Omega_\Lambda = 1\) background.
- For each \(\Omega_\Lambda\), defines:
  - \(\Omega_m = 1 - \Omega_\Lambda\)
- Computes a **dimensionless** age for a flat FRW model:
  \[
  t_0^{\text{(dimless)}}(\Omega_\Lambda) =
  \int_0^{1} \frac{da}{a \sqrt{\Omega_m a^{-3} + \Omega_\Lambda}}.
  \]
- Converts this to Gyr by calibrating a **single global scale factor**
  (Gyr per dimensionless time) so that the host ages broadly match the Phase 4
  `age_Gyr` over the grid.

Thus:

- The host is neither a full Boltzmann code nor a full ΛCDM pipeline.
- It is a **sanity-check FRW background calculator** that:
  - uses the same \(\Omega_\Lambda\)-like column as Phase 4,
  - constructs a standard flat–FRW age from it,
  - compares that age to the Phase 4 `age_Gyr` toy mapping.

---

## 3. Rung X1 – Age cross-check construction

Script:

- `stage2/external_frw_host/src/compute_analytic_frw_ages_v1.py`

Steps (high level):

1. **Load joint grid**:
   - `stage2_joint_theta_grid_v1.csv`
   - extract `theta_index`, `theta`, `omega_lambda`, `age_Gyr`, `frw_viable`.
2. **Compute dimensionless host age**:
   - for each row, integrate a flat–FRW age integral
     \(t_0^{\text{(dimless)}}(\Omega_\Lambda)\).
3. **Calibrate Gyr scale factor**:
   - choose a single multiplicative factor so that host ages roughly agree with
     toy `age_Gyr` on the grid (internal least-squares-style calibration).
   - The logged run reports:
     - calibrated scale factor ≈ **2.75 Gyr per dimensionless unit**.
4. **Compute differences**:
   - `age_Gyr_host` = dimless_age × calibrated_scale
   - `age_Gyr_diff`  = `age_Gyr_host - age_Gyr`
   - `age_Gyr_rel_diff` = `age_Gyr_diff / age_Gyr`
5. **Write table**:
   - `stage2_external_frw_rung1_age_crosscheck_v1.csv`
   - 2048 rows (one per θ grid point).

Key diagnostic from the logged run:

- On the FRW-viable subset (1016 points), the script reports:
  - mean \(|age_{\text{host}} - age_{\text{toy}}|\) ≈ **2.7 Gyr**,
  - max \(|age_{\text{host}} - age_{\text{toy}}|\) ≈ **12.9 Gyr**,
  - mean \(|\text{relative diff}|\) ≈ **0.20**.

Interpretation:

- Even after a global calibration, the toy `age_Gyr` column is only
  **moderately aligned** with a standard flat–FRW age:
  - good enough to treat as a coarse background-age proxy,
  - not good enough to treat as “physically calibrated” without caveats.

---

## 4. Rung X2 – Age contrast across sets

Script:

- `stage2/external_frw_host/src/analyze_external_frw_age_contrast_v1.py`

Input:

- `stage2_external_frw_rung1_age_crosscheck_v1.csv`

Sets analysed:

- `ALL_GRID`: all θ points (2048).
- `FRW_VIABLE`: rows with `frw_viable = 1` (1016).
- `CORRIDOR_AND_VIABLE`: rows where both:
  - `frw_viable = 1` and `in_toy_corridor = 1`.
- `CORRIDOR_AND_VIABLE_AND_ANCHOR`:
  - the 18-point **anchor kernel**:
    - FRW-viable,
    - in the Stage 2 toy corridor,
    - in the empirical \((\Omega_\Lambda, t_0)\) anchor box.

The summary table is written to:

- `stage2_external_frw_rung2_age_contrast_v1.csv`.

Representative numbers from the logged run:

- **ALL_GRID** (2048 points):
  - ⟨Δage⟩ ≈ **−8.41 Gyr**  
    (host younger than toy, on average).
  - ⟨|Δage| / age_toy⟩ ≈ **0.53**.
- **FRW_VIABLE** (1016 points):
  - ⟨Δage⟩ ≈ **−2.49 Gyr**.
  - ⟨|Δage| / age_toy⟩ ≈ **0.18**.
- **CORRIDOR_AND_VIABLE** (154 points):
  - ⟨Δage⟩ ≈ **−11.86 Gyr**.
  - ⟨|Δage| / age_toy⟩ ≈ **0.84**.
- **CORRIDOR_AND_VIABLE_AND_ANCHOR** (18 points):
  - ⟨Δage⟩ ≈ **−10.87 Gyr**.
  - ⟨|Δage| / age_toy⟩ ≈ **0.81**.

So:

- The toy age and host age agree *best* on the FRW-viable subset as a whole.
- Inside the toy corridor and empirical anchor kernel, the host age is
  systematically **much younger** than the toy age (large negative Δage, large
  relative error).

---

## 5. Interpretation and non-claims

**What this belt *does* say**

- The Phase 4 `age_Gyr` column is:
  - derived from an internal toy-FRW mapping,
  - only loosely aligned with a standard flat–FRW age, even after global calibration.
- On FRW-viable points:
  - the mismatch is ~20% on average, with tails larger than that.
- On the toy corridor and empirical anchor kernel:
  - the mismatch is much larger (~80% relative error on average),
  - indicating that the age scale in those regions is **not** reliably calibrated.

As a result:

- Any future empirical contact that leans on “age of the Universe” should:
  - either refine the Phase 4 toy mapping,
  - or treat the external host as the **primary** age diagnostic,
  - or both.

**What this belt *does not* claim**

- We do **not** claim that:
  - the current FRW toy reproduces ΛCDM background ages,
  - the external host is a complete or final cosmology model,
  - the age mismatch rules out or validates the axiom or mechanism.
- We do **not** use:
  - Planck/BAO/SN likelihoods,
  - any real-data pipeline beyond the schematic background-age box
    used in the separate empirical-anchor belt.

Everything in this file is strictly **Stage 2 diagnostic**:

- It reads Phase 4 outputs (plus masks) and compares them to a simple host model.
- It informs how seriously we should treat `age_Gyr` as a calibrated quantity in later work.

---

## 6. Future directions (out of scope for this doc)

The external host belt suggests several follow-ups, which must each be gated and
scoped separately:

1. **Toy age refinement (Phase 4–adjacent):**
   - adjust the Phase 4 FRW toy mapping so that:
     - `age_Gyr` better tracks a standard flat–FRW age for FRW-viable points,
     - or introduce a “host-calibrated” age column as a first-class diagnostic.
2. **Richer external cosmology host (Stage II-style):**
   - define a Stage 2/Stage II belt where:
     - θ → effective cosmological parameters,
     - parameters → external library (e.g. CLASS/CCL/PyCosmo),
     - outputs → background observables (H(z), distances, etc.).
   - keep these under Phase 0 governance with explicit scope and non-claims.
3. **Empirical anchor promotion gates:**
   - if and when the toy/host age alignment is improved, define the conditions
     under which:
     - the empirical anchor kernel can be cited in Phase 4 or Phase 5 narrative,
     - without over-claiming beyond what these diagnostics actually show.

Until such rungs exist and pass their own checks, this document should be read as
a **status snapshot of a diagnostic external-host belt**, not as a physics result.

