# Stage 2 – Omega Naming & Endpoint Map (v1)

This document is a a small contract for how **omega-like columns** are named and used
in Stage 2, so that FRW toy, host cosmologies, and masks stay consistent and
scripts stop guessing.

It is not a physics claim; it is a **schema + discipline contract**.

---

## 1. Naming Conventions

### 1.1 FRW toy / repo-side parameters

- **`omega_lambda`**
  - Meaning: FRW toy \(\Omega_\Lambda\) on the **repo / Phase 4 FRW grid**.
  - Typical home:
    - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv`
      (alongside `theta_index`, `theta`, `age_Gyr`, `frw_viable`, `in_toy_corridor`, and mechanism columns).
  - Usage rule:
    - Use this name only where the table is **natively** Phase-4 / FRW-toy derived.

- **`omega_lambda_repo`**
  - Meaning: the **same FRW toy \(\Omega_\Lambda\)** value, but carried into host-side
    tables and masks.
  - Typical homes:
    - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_params_grid_v1.csv`
    - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_rung3_age_contrast_v1.csv`
    - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_flat_subset_mask_v1.csv`
    - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_age_anchor_corridor_kernel_v1.csv`
  - Usage rule:
    - When a table is primarily a **host / Stage 2** table but needs the FRW toy
      \(\Omega_\Lambda\) for reference, use `omega_lambda_repo`, not bare `omega_lambda`.
    - New Stage 2 tables **should prefer** `omega_lambda_repo` for FRW toy values.

### 1.2 External FRW / ΛCDM host parameters

These are **external background cosmologies** that are not defined by the Phase-4 FRW toy.

- **`Omega_m`**
  - Meaning: host matter density parameter \(\Omega_m\).
  - Home: external host background grids.
- **`Omega_lambda`**
  - Meaning: host cosmological constant parameter \(\Omega_\Lambda\).
- **`H0_km_s_Mpc`**
  - Meaning: host Hubble constant \(H_0\) in km/s/Mpc.
- **`age_Gyr_host`**
  - Meaning: cosmological age of the Universe predicted by the **host** cosmology
    (FRW host or cosmo host) on that row, in Gyr.
- **`age_Gyr_repo`**
  - Meaning: Phase-4 / FRW toy age carried into a host-context table, in Gyr.

Usage rule:

- Treat `(Omega_m, Omega_lambda, H0_km_s_Mpc)` as a **separate parameter triplet**
  from any `omega_lambda_repo` value.
- If both host and repo omegas appear in the same table, they **must** be
  distinguished by suffix:
  - host: `Omega_lambda` or `Omega_lambda_host`
  - repo (FRW toy): `omega_lambda_repo`

### 1.3 Masks and flags

Common boolean columns and their meaning:

- **`frw_viable`** – row passes the FRW viability filter on the Phase-4 FRW toy.
- **`in_toy_corridor`** – row is inside the Phase-4 toy FRW corridor.
- **`is_near_flat`** – row belongs to the near-flat host subset:
  \(|\Omega_\text{tot} - 1| \le 0.05\).
- **`in_host_age_anchor_box`** (FRW host side) – host age lies in the chosen
  observational age window.
- **`in_host_empirical_anchor_box`** (FRW host side, empirical anchor) – host FRW
  point lies inside the empirical anchor box derived from FRW data probes.

*Rule:*  
Any mask table that will be used in scripts that reason about \(\Omega\) **must**
retain enough columns to reconstruct whatever omega quantity those scripts need
(e.g. `omega_lambda_repo` or `Omega_lambda`), or be explicitly re-joined with a
background grid that carries those columns.

---

## 2. Omega Map: Which Tables Have Which Omega Columns?

This section is purely descriptive of the Stage 2 tables as currently used.

### 2.1 Joint FRW + mechanism grid

- **File**
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv`
- **Relevant columns (partial):**
  - `theta_index`, `theta`
  - `omega_lambda`              – FRW toy \(\Omega_\Lambda\) (native Phase-4 grid)
  - `age_Gyr`                   – FRW toy age in Gyr
  - `frw_viable`, `in_toy_corridor`
  - `mech_baseline_*`, `mech_binding_*`, `*_bound` – mechanism measures

**Contract:** In Stage 2 scripts, this file is the **source of truth** for the FRW
toy `omega_lambda` and `age_Gyr` on the joint θ-grid.

---

### 2.2 External cosmo host – params grid

- **File**
  - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_params_grid_v1.csv`
- **Relevant columns (partial):**
  - `theta_index`, `theta`
  - `omega_lambda_repo`, `age_Gyr_repo`   – FRW toy values carried into host context
  - `Omega_m`, `Omega_lambda`, `H0_km_s_Mpc`

**Contract:**

- Use `omega_lambda_repo` + `age_Gyr_repo` for all **FRW-toy-side comparisons**.
- Use `(Omega_m, Omega_lambda, H0_km_s_Mpc)` to compute host ages and flatness.

---

### 2.3 External cosmo host – background age grid

- **File**
  - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_background_grid_v1.csv`
- **Relevant columns (partial):**
  - `theta_index`, `theta`
  - `Omega_m`, `Omega_lambda`, `H0_km_s_Mpc`
  - `age_Gyr_host`            – host cosmology age in Gyr

**Contract:** This is the **host-side age oracle**. If a mask or kernel needs host
ages or host \(\Omega\) but doesn’t carry them, it should re-join to this table
on `theta_index`.

---

### 2.4 External cosmo host – flat subset mask

- **File**
  - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_flat_subset_mask_v1.csv`
- **Relevant columns (partial):**
  - `theta_index`
  - `Omega_m`, `Omega_lambda`, `Omega_tot`
  - `omega_lambda_repo`, `age_Gyr_repo`, `age_Gyr_host`
  - `frw_viable`, `in_toy_corridor`, `is_near_flat`

**Contract:**

- `is_near_flat` encodes the near-flat selection \(|\Omega_\text{tot}-1| \le 0.05\).
- FRW toy vs host roles:
  - FRW toy: `omega_lambda_repo`, `age_Gyr_repo`
  - host: `Omega_m`, `Omega_lambda`, `Omega_tot`, `age_Gyr_host`
- Scripts that need to know whether a row is near-flat should look only at
  `is_near_flat` (not rederive the condition ad hoc).

---

### 2.5 External cosmo host – host age anchor kernel

- **File**
  - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_age_anchor_corridor_kernel_v1.csv`
- **Relevant columns (partial):**
  - `theta_index`, `theta`
  - `omega_lambda_repo`        – FRW toy \(\Omega_\Lambda\) (repo naming)
  - `age_Gyr_repo`             – FRW toy age
  - `age_Gyr_host`             – host-age in Gyr
  - `omega_lambda` (duplicate FRW toy \(\Omega_\Lambda\) via join)
  - `age_Gyr`     (duplicate FRW toy age via join)
  - `frw_viable`, `in_toy_corridor`
  - `mech_baseline_*`, `mech_binding_*`, `*_bound`

**Contract:**

- Within this kernel, `omega_lambda` and `omega_lambda_repo` refer to the same
  FRW toy parameter; for new scripts we should prefer **one canonical name**:
  `omega_lambda_repo`.
- Physics comparisons inside the kernel should be explicit about which age is
  used:
  - FRW toy age: `age_Gyr_repo`
  - host age: `age_Gyr_host`.

---

### 2.6 External cosmo host – age contrast and window sensitivity

- **Age contrast**
  - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_rung3_age_contrast_v1.csv`
  - Contains summary statistics of `age_Gyr_host` vs `age_Gyr_repo` for various sets:
    `ALL_GRID`, `FRW_VIABLE`, `CORRIDOR_AND_VIABLE`.
- **Age window sensitivity**
  - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_age_window_sensitivity_v1.csv`
  - Contains age-window selections and counts as a function of:
    - `scale`, `(age_min_Gyr, age_max_Gyr)`
    - subset labels: `HOST_WINDOW`, `FRW_VIABLE_AND_HOST_WINDOW`,
      `CORRIDOR_AND_VIABLE_AND_HOST_WINDOW`
  - Uses:
    - `age_Gyr_host_mean/std`
    - `age_Gyr_repo_mean/std`
    - `omega_lambda_repo_mean/std`.

**Contract:**

- These tables are **summaries**, not sources of raw omega values.
- Scripts must not assume they can recover per-θ omega from them; they must
  re-join to raw grids/masks instead.

---

## 3. Coding Discipline for New Stage 2 Scripts

Going forward, any new Stage 2 script that touches omega columns must:

1. **Declare its expectations** at the top (conceptually or in comments), e.g.:

   > “This script expects `omega_lambda_repo`, `age_Gyr_repo` from
   >  `stage2_external_cosmo_params_grid_v1.csv` and `Omega_m`, `Omega_lambda`,
   >  `age_Gyr_host` from the background grid.”

2. **Check columns explicitly**, e.g.:

   ```python
   def require_columns(df, cols, context=""):
       missing = [c for c in cols if c not in df.columns]
       if missing:
           raise RuntimeError(f"[{context}] Missing required columns: {missing}")
   ```

   And then:

   ```python
   require_columns(
       df_kernel,
       ["theta_index", "omega_lambda_repo", "age_Gyr_repo", "age_Gyr_host"],
       context="H9 kernel check",
   )
   ```

3. **Never assume** that a mask table contains `theta` or `omega_lambda` unless
   the header has been checked. If needed, re-join with:

   - the joint θ-grid for FRW toy values, or
   - the host background grid for `(Omega_m, Omega_lambda, age_Gyr_host)`.

4. When both host and repo omegas are present, suffixes are mandatory:

   - `omega_lambda_repo` – FRW toy
   - `Omega_lambda` or `Omega_lambda_host` – host cosmology.

---

## 4. Why This Doc Exists

This file is here so that:

- Humans and AIs can quickly see **which table carries which omega**, and
- Future scripts have a **single source of truth** for naming conventions.

If a future change introduces a new omega-bearing table or renames a column,
this document should be updated in the same commit.
