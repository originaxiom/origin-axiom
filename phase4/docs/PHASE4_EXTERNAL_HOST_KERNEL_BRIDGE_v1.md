# Phase 4 External Host Kernel Bridge (F1 / Stage 2)

This note summarizes how the 12-point **external-cosmo host kernel** from Stage 2 is wired into the Phase 4 F1 FRW diagnostics. It is purely a **diagnostic bridge**: it documents where the Phase 4 internal FRW toy, its corridor, and an external flat-\LambdaCDM host happen to agree, without promoting any cosmological claim.

The goal is that a reader can start from this file, locate the exact CSV tables and scripts, and reconstruct the Stage 2 \(\leftrightarrow\) Phase 4 interface deterministically.

---

## 1. Main inputs and tables

The bridge uses the following Stage 2 and Phase 4 artifacts:

- **Stage 2 / external-cosmo host**
  - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_params_grid_v1.csv`  
    Per-\(\theta\) toy FRW background: \(\theta\), \(\omega_{\Lambda,\mathrm{repo}}\), age\(_\mathrm{repo}\), and derived \(\Omega_m, \Omega_\Lambda\) used for the host construction.
  - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_background_grid_v1.csv`  
    External flat-\(\Lambda\)CDM host background grid: \(\theta\), \(\Omega_m\), \(\Omega_\Lambda\), \(H_0\), age\(_\mathrm{host}\).
  - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_flat_subset_mask_v1.csv`  
    Per-\(\theta\) **near-flat host mask**, including  
    `Omega_m`, `Omega_lambda`, `Omega_tot`, `omega_lambda_repo`, `age_Gyr_repo`, `age_Gyr_host`, `frw_viable`, `in_toy_corridor`, and `is_near_flat`.  
    The near-flat definition is  
    \[
      |\Omega_\mathrm{tot} - 1| \le 0.05,
    \]
    giving \(n = 1286\) out of 2048 grid points (\(\approx 0.628\)).
  - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_age_anchor_corridor_kernel_v1.csv`  
    The **12-point kernel** where:
    - the Phase 4 FRW toy is FRW-viable,  
    - the toy lies inside its internal corridor, and  
    - the external flat-\(\Lambda\)CDM host assigns a Universe-like age near the Phase 2 / Phase 4 anchor.
  - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_phase4_constraints_v1.csv`  
    A compact constraints summary (one row) extracted from the 12-point kernel, used as the direct input for the Phase 4 LaTeX table.

- **Phase 4 / F1 FRW diagnostics**
  - `phase4/outputs/tables/phase4_F1_sanity_curve.csv`  
    Baseline F1 mapping curve, giving \(E_\mathrm{vac}(\theta)\) on the 2048-point grid.
  - `phase4/outputs/tables/phase4_F1_frw_viability_mask.csv`  
    Per-\(\theta\) FRW viability mask derived from the F1 curve:
    `theta`, `E_vac`, `omega_lambda`, `age_Gyr`, and Boolean flags including `has_matter_era`, `has_late_accel`, `frw_viable`.
  - `phase4/outputs/tables/phase4_F1_frw_lcdm_probe.json`  
    Internal **\(\Lambda\)CDM-like FRW probe** summary:
    - \(n_\mathrm{grid} = 2048\),  
    - \(n_\mathrm{frw\_viable} = 1016\),  
    - \(n_\mathrm{lcdm\_like} = 63\)  
      (\(\mathrm{lcdm\_like\_fraction} \approx 0.0308\)),  
    - \(\theta \in [0.5983, 3.3625]\) for the LCDM-like subset,  
    - \(\omega_\Lambda \in [0.6031, 0.7982]\),  
    - ages in \([13.19, 13.77]~\mathrm{Gyr}\) for the LCDM-like subset.
  - `phase4/outputs/tables/phase4_F1_frw_shape_probe.json`  
    Joint overlaps between:
    - FRW-viable set,  
    - toy-corridor set,  
    - LCDM-like probe.  
    For example,
    - \(\mathrm{frac\_frw\_viable} = 0.4961\),  
    - \(\mathrm{frac\_in\_toy\_corridor} = 0.5791\),  
    - \(\mathrm{frac\_lcdm\_like} = 0.0308\),  
    - \(\mathrm{frac\_shape\_and\_viable} = 0.0752\),  
    - \(\mathrm{frac\_shape\_and\_lcdm} = 0.0195\).

- **Bridge table inside the Phase 4 paper**
  - Builder script:  
    `phase4/src/build_phase4_external_host_kernel_table_v1.py`
  - LaTeX table output:  
    `phase4/outputs/tables/phase4_external_host_kernel_constraints_v1.tex`  
    which is included in the Phase 4 paper as the external-host kernel table (see `\label{tab:external_host_kernel}`).

For naming conventions across these files (e.g. `omega_lambda` vs `omega_lambda_repo` vs `Omega_lambda`), see also  
`STAGE2_OMEGA_NAMING_AND_MAP_v1.md` and the scan script  
`stage2/external_cosmo_host/src/scan_external_host_omega_naming_v1.py`.

---

## 2. Definition of the 12-point external-cosmo host kernel

The Stage 2 kernel table  
`stage2_external_cosmo_host_age_anchor_corridor_kernel_v1.csv` is constructed by:

1. Starting from the Stage 2 **joint \(\theta\) grid** (the same 2048-point grid used by Phase 3 and Phase 4).
2. Joining to:
   - the external-cosmo host background grid, and  
   - the near-flat host mask (`is_near_flat`) derived from \(\Omega_\mathrm{tot}\).
3. Intersecting the following Boolean conditions:
   - `frw_viable = True` (FRW-viable toy, using the Phase 4 FRW backbone),  
   - `in_toy_corridor = True` (inside the Phase 4 internal toy corridor),  
   - `is_near_flat = True` (external host lies in the near-flat subset),  
   - host age in a **Universe-like window** around the Phase 2 / Phase 4 age anchor.

The result is a **12-point kernel**:
- `n_theta = 12`, drawn from the 2048-point joint grid.
- Each row carries:
  - `theta_index`, `theta`,  
  - `omega_lambda_repo`, `age_Gyr_repo` (toy),  
  - `Omega_m`, `Omega_lambda`, `age_Gyr_host` (host),  
  - and the mechanism diagnostics  
    `mech_baseline_A0`, `mech_baseline_A_floor`, `mech_baseline_bound`,  
    `mech_binding_A0`, `mech_binding_A`, `mech_binding_bound`.

A separate consistency check  
`stage2/external_cosmo_host/src/check_external_cosmo_host_kernel_consistency_v1.py` writes  
`stage2_external_cosmo_host_kernel_consistency_v1.csv` and confirms that, on this 12-point kernel,

- all points are FRW-viable (`all_frw_viable = True`),  
- all lie inside the toy corridor (`all_in_corridor = True`),  
- all lie in the near-flat host subset (`all_near_flat = True`), and  
- the host and toy ages are close:
  - age difference (host − repo) [Gyr]:  
    mean \(\approx 0.094\), min \(\approx -0.167\), max \(\approx 0.366\),  
  - absolute age difference [Gyr]:  
    mean \(\approx 0.164\), min \(\approx 0.026\), max \(\approx 0.366\).

These numbers are **diagnostic of the chosen toy and host configurations** and are not promoted as cosmological measurements.

---

## 3. Numerical summary of the kernel band

The Phase 4–ready constraints table  
`stage2_external_cosmo_host_phase4_constraints_v1.csv` condenses the 12-point kernel into a single row with the following bands (all computed directly from the kernel CSV):

- **\(\theta\) support**
  - \(n_\theta = 12\),
  - \(\theta \in [0.6412039693, 3.3195344249]\).

- **Toy and host \(\Omega_\Lambda\) bands**
  - Toy: `omega_lambda_repo`  
    \[
      \omega_{\Lambda,\mathrm{repo}} \in [0.6892324577, 0.7229500555],
    \]
  - Host: `Omega_lambda`  
    \[
      \Omega_{\Lambda,\mathrm{host}} \in [0.6892324577, 0.7229500555].
    \]
  Within the kernel, the host and toy \(\Lambda\) fractions match numerically by construction, but are still tracked separately in the CSV for clarity.

- **Toy and host age bands**
  - Toy ages:
    \[
      \mathrm{age}_\mathrm{repo} \in [13.4024883, 13.5019605]~\mathrm{Gyr},
    \]
  - Host ages:
    \[
      \mathrm{age}_\mathrm{host} \in [13.3344618, 13.7681294]~\mathrm{Gyr}.
    \]

- **Mechanism band (baseline A0)**
  - `mech_baseline_A0` values across the kernel satisfy
    \[
      0.04609937555 \;\lesssim\; \mathrm{mech\_baseline\_A0} \;\lesssim\; 0.04665311924.
    \]
  This is the mechanism band quoted in the Phase 4 table as the \(\theta\)-space band on which the external host and internal FRW toy jointly satisfy the kernel conditions.

The Phase 4 LaTeX table  
`phase4/outputs/tables/phase4_external_host_kernel_constraints_v1.tex` is a direct formatting of these bands, and is the only place where they are used in the Phase 4 paper.

---

## 4. Relation to internal F1 FRW probes

On the **internal** side, the Phase 4 F1 diagnostics establish:

- The FRW-viable fraction of the grid is \(\approx 0.50\)  
  (`frac_viable = 0.49609375` in `phase4_F1_frw_viability_diagnostics.json`).
- The toy shape corridor (non-binding diagnostic) covers \(\approx 0.58\) of the grid  
  (`corridor_fraction = 0.5791015625` in `phase4_F1_shape_diagnostics.json`).
- The internal \(\Lambda\)CDM-like probe picks out \(\approx 3.1\%\) of the grid inside the FRW-viable set  
  (`lcdm_like_fraction = 0.03076171875` in `phase4_F1_frw_lcdm_probe.json`).

The **12-point external host kernel** is more restrictive: it sits at the intersection of

- FRW-viable toy,  
- toy-corridor membership,  
- near-flat external host, and  
- host age close to the Phase 2 / Phase 4 age anchor.

This kernel is not used to define a new corridor or constraint; instead, it is:

- a **Stage 2 / Phase 4 alignment check**, and  
- a compact region where the **external host and internal FRW toy** share:
  - a narrow \(\theta\) band,  
  - a narrow \(\Omega_\Lambda\) band,  
  - and closely matching age bands,  
  while remaining FRW-viable and near-flat.

All statements above are strictly about the **diagnostic behavior of the current toy and host construction**. No extrapolation to real data or cosmological inference is made at the Phase 4 level.

---

## 5. Reproduction checklist

To fully reproduce the bridge on a clean clone of the repository:

1. **External-cosmo host pipeline (Stage 2)**
   - Generate or refresh the external host background grid and near-flat subset.  
   - Run the scripts that produce:
     - `stage2_external_cosmo_host_background_grid_v1.csv`,  
     - `stage2_external_cosmo_flat_subset_mask_v1.csv`,  
     - `stage2_external_cosmo_host_age_anchor_corridor_kernel_v1.csv`,  
     - `stage2_external_cosmo_host_phase4_constraints_v1.csv`.

2. **Phase 4 F1 FRW diagnostics**
   - Run the F1 FRW pipeline:
     - `phase4/src/phase4/run_f1_sanity.py`  
     - `phase4/src/phase4/run_f1_shape_diagnostics.py`  
     - `phase4/src/phase4/run_f1_frw_toy_diagnostics.py`  
     - `phase4/src/phase4/run_f1_frw_corridors.py`  
     - `phase4/src/phase4/run_f1_frw_lcdm_probe.py`  
     - `phase4/src/phase4/run_f1_frw_data_probe.py`  
   - Confirm that `phase4_F1_frw_viability_diagnostics.json`,  
     `phase4_F1_frw_lcdm_probe.json`, and `phase4_F1_frw_shape_probe.json` match the
     fractions and bands summarized above.

3. **Bridge table for the Phase 4 paper**
   - Run  
     `phase4/src/build_phase4_external_host_kernel_table_v1.py`  
     to regenerate  
     `phase4/outputs/tables/phase4_external_host_kernel_constraints_v1.tex`.
   - Rebuild the Phase 4 paper:
     - `cd phase4/paper`  
     - `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`.

If all scripts complete without error and the quoted bands match, the Stage 2 / Phase 4 external-host bridge is reproducibly aligned with the rest of the repository.
