# Stage 2 – External FRW Host Sanity Belt (X1–X3)

Status: **diagnostic-only**, Stage 2 belt.  
Scope: sanity-check the Phase 4 FRW toy background against a simple analytic flat–ΛCDM host and record the outcome as **non-promoted** infrastructure. No Phase-level claims change.

---

## 1. Scope and guards

This belt introduces an **external FRW host** as a comparison tool for the Phase 4 FRW toy background:

- It treats the Phase 4 FRW outputs as a **toy background**, not as a calibrated cosmology engine.
- It uses a minimal analytic **flat ΛCDM age formula** as a host:
  - input: an effective \(\Omega_\Lambda\) from the Phase 4 grid,
  - output: a host-predicted age \(t_{0,\mathrm{host}}\) (dimensionless and then scaled to Gyr).
- It is explicitly **Stage 2 diagnostic infrastructure**:
  - downstream of Phase 3/4,
  - no change to the Phase 0–5 claims or contracts,
  - no promotion to paper figures or tables.

Any future contact with full cosmology pipelines (CLASS/CCL/Cobaya, real data likelihoods, etc.) must live in a **separate, gated Stage II pipeline**, not in this belt.

---

## 2. Inputs and methods

### 2.1. Inputs

- Joint θ-grid from the Stage 2 joint mech–FRW belt:
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv`
  - columns used here:
    - `theta_index`, `theta`,
    - `omega_lambda`,
    - `age_Gyr` (Phase 4 FRW toy age),
    - `frw_viable`,
    - `corridor_and_viable`,
    - `corridor_and_viable_and_anchor` (18-point empirical kernel).
- Empirical anchor belt:
  - `stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_empirical_anchor_mask_v1.csv`
  - provides the `in_empirical_anchor_box` mask and feeds the 18-point kernel definition.

### 2.2. External FRW host

The host is implemented as a simple analytic **flat–ΛCDM background age**:

\[
t_0(\Omega_\Lambda) \;=\; \int_0^1 \frac{da}{a\,H(a;\Omega_\Lambda)} \quad,\quad
H^2(a) = H_0^2\left[ \Omega_m a^{-3} + \Omega_\Lambda \right],
\]

with \(\Omega_m = 1 - \Omega_\Lambda\) and a fixed \(H_0\) scaling. In practice:

1. For each row in the joint grid, we take the Phase 4 `omega_lambda` as \(\Omega_\Lambda\).
2. We numerically integrate the **dimensionless** age \(t_{0,\mathrm{dimless}}(\Omega_\Lambda)\) on a fixed \(a\)-grid.
3. We calibrate a single global scale factor \(s\) (Gyr per dimensionless unit) on the **FRW-viable subset** by a simple least-squares fit:

   - choose \(s\) that minimises the squared difference between
     - `age_Gyr` (Phase 4 toy age), and
     - \(t_{0,\mathrm{host}} = s \, t_{0,\mathrm{dimless}}\).

4. We then apply this fixed calibration to **all** θ points to get `age_Gyr_host`.

This is intentionally a **minimal**, background-only host:
- no radiation, no curvature,
- no perturbations or CMB,
- no sharp data constraints.

### 2.3. Scripts and outputs

- X1 – host ages and pointwise differences:
  - Script:
    - `stage2/external_frw_host/src/compute_analytic_frw_ages_v1.py`
  - Output:
    - `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung1_age_crosscheck_v1.csv`
      - columns: `theta_index`, `theta`, `omega_lambda`, `age_Gyr`, `age_Gyr_host`,
        `age_Gyr_diff = age_Gyr - age_Gyr_host`, `age_Gyr_rel_diff`, `frw_viable`.

- X2 – set-wise contrasts:
  - Script:
    - `stage2/external_frw_host/src/analyze_external_frw_age_contrast_v1.py`
  - Output:
    - `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung2_age_contrast_v1.csv`
      - aggregated over the sets:
        - `ALL_GRID`,
        - `FRW_VIABLE`,
        - `CORRIDOR_AND_VIABLE`,
        - `CORRIDOR_AND_VIABLE_AND_ANCHOR`.

---

## 3. Key numerical findings

### 3.1. Global picture (ALL_GRID)

- Set: **ALL_GRID** (2048 θ points, full grid).
- On average, the Phase 4 FRW toy ages are **older** than the analytic host prediction:
  - \(\langle \Delta t_0 \rangle \approx -8.4 \,\mathrm{Gyr}\),
  - mean relative difference \(\langle \Delta t_0 / t_{0,\mathrm{repo}} \rangle \approx -0.53\).
- Interpretation:
  - Across the full θ-grid, the toy FRW pipeline is **not calibrated** to the analytic flat–ΛCDM age; it systematically produces larger ages.

### 3.2. FRW-viable subset

- Set: **FRW_VIABLE** (about half the grid, 1016 points).
- After restricting to `frw_viable == True`:
  - mean age difference is smaller in magnitude:
    - \(\langle \Delta t_0 \rangle \approx -2.5 \,\mathrm{Gyr}\),
    - mean relative difference \(\approx -0.18\).
- Interpretation:
  - The **FRW viability mask** is at least loosely aligned with the analytic host:
    - viable points are, on average, **less badly** mismatched in age than the full grid.
  - But the mismatch is still at the \(\mathcal{O}(10\%)\)–\(\mathcal{O}(20\%)\) level, so this is not a calibrated match.

### 3.3. Corridor and empirical kernel

- Set: **CORRIDOR_AND_VIABLE** (toy corridor ∧ FRW viable).
  - mean age difference:
    - \(\langle \Delta t_0 \rangle \approx -11.9 \,\mathrm{Gyr}\),
    - mean relative difference \(\approx -0.84\).
- Set: **CORRIDOR_AND_VIABLE_AND_ANCHOR** (18-point empirical kernel).
  - mean age difference:
    - \(\langle \Delta t_0 \rangle \approx -10.9 \,\mathrm{Gyr}\),
    - mean relative difference \(\approx -0.81\).

Interpretation:

- The **toy corridor ∧ FRW viable** region is, in fact, **worse** than a generic FRW-viable point in terms of alignment with the analytic host:
  - it prefers θ-patches where the toy FRW age is almost a factor of 2 larger than the host prediction.
- The 18-point **empirical kernel** is slightly less extreme than the broader corridor, but:
  - still shows \(\sim 80\%\) relative mismatch,
  - is **not** a special pocket where the toy FRW ages secretly match a standard flat–ΛCDM background.

---

## 4. Interpretation and gate

### 4.1. What this *does* tell us

- The external analytic FRW host acts as a **sanity comparator**:
  - it confirms that the Phase 4 FRW toy ages are **rough diagnostic quantities**, not calibrated cosmological ages;
  - it shows that the FRW viability mask nudges the grid towards somewhat more reasonable ages, but not enough to claim “alignment with ΛCDM”.
- The **empirical kernel** (18 points) is:
  - internal to the current anchor design,
  - not singled out by the host as a particularly well-calibrated region,
  - therefore interpretable only as an **internal** intersection of:
    - FRW viability,
    - toy corridor,
    - chosen empirical box.

### 4.2. What this *does not* claim

This belt **does not**:

- promote any θ-region to a **data-calibrated** corridor,
- claim that the current implementation of the axiom is compatible or incompatible with real cosmological age measurements,
- serve as a likelihood evaluation, constraint, or fit to Planck/BAO/SN or any real dataset.

The mismatch magnitudes here are treated as a **diagnostic snapshot** of:
- how far the Phase 4 FRW toy pipeline is from a simple flat–ΛCDM age calculation, and
- how the internal masks (FRW viability, corridor, anchor kernel) sit within that mismatch landscape.

### 4.3. Forward path

- Any serious contact with **real FRW background constraints** (e.g. precise age, \(H_0\), \(\Omega_\Lambda\) boxes from data) belongs in a **future Stage II pipeline**:
  - hosted e.g. on CLASS/CCL/ Cobaya / CosmoSIS,
  - with explicit Phase-0-style contracts and promotion gates.

- The current external FRW host belt (X1–X3):
  - remains **Stage 2 diagnostic infrastructure**,
  - can be cited in future design documents as evidence that:
    - Phase 4 FRW ages are toy-level,
    - the empirical kernel is internal and not yet data-calibrated,
  - but is **not** used to modify or strengthen any Phase 3/4/5 claims.

