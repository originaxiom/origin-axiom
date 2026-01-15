
# Stage 2 ↔ Phase 4 FRW–Host Summary (F1 baseline checkpoint)

**Status:** cross-phase summary, read-only.  
**Checkpoint tag:** `stage2_phase4_F1_FRW_baseline_checkpoint_2026-01-15`.

This document explains how the Stage 2 external-cosmo host machinery and the
Phase 4 F1 FRW backbone are wired together at the current baseline checkpoint.
It does **not** introduce new physics assumptions; it only summarizes what the
existing tables and scripts already encode.

---

## 1. What Stage 2 external-cosmo hosts do

The Stage 2 `external_cosmo_host` rung builds a grid of flat-ΛCDM
backgrounds and measures how “Universe-like” each one is in age and density:

- Parameter grid:
  - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_params_grid_v1.csv`
    with columns
    `theta_index, theta, omega_lambda_repo, age_Gyr_repo, Omega_m, Omega_lambda, H0_km_s_Mpc`.

- External host background:
  - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_background_grid_v1.csv`
    with `theta_index, theta, Omega_m, Omega_lambda, H0_km_s_Mpc, age_Gyr_host`
    evaluated by an external flat-ΛCDM calculator.

- Near-flat subset:
  - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_flat_subset_mask_v1.csv`
  - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_flat_subset_summary_v1.csv`

  The near-flat mask uses

  \[
  \Omega_\mathrm{tot} = \Omega_m + \Omega_\Lambda
  \]

  and selects points with

  \[
  \lvert\Omega_\mathrm{tot} - 1\rvert \le 0.05,
  \]

  then records how large this subset is and its age / density statistics.

All of these tables are **host-side**: they know nothing about the Phase 4 F1
mapping except for the shared `theta_index` / `theta` and
`omega_lambda_repo` (= \(\Omega_\Lambda\) from the repo’s FRW toy).

---

## 2. The 12-point external host kernel

To connect to Phase 4, Stage 2 defines a stricter **host kernel**:

- Kernel mask and kernel table:
  - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_age_anchor_mask_v1.csv`
  - `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_age_anchor_corridor_kernel_v1.csv`

The kernel keeps only those near-flat host points that:

1. are FRW-viable under the Phase 4 toy mapping (via `frw_viable`);
2. lie inside the Phase 4 internal corridor (`in_toy_corridor`);
3. assign a “Universe-like” age (host age anchor window).

At the F1 baseline checkpoint this produces **12 grid points**, summarized by

- `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_phase4_constraints_v1.csv`

with:

- \(\theta\) range: roughly \(0.64 \le \theta \le 3.32\),
- \(\Omega_\Lambda\) band: about \(0.689 \lesssim \Omega_\Lambda \lesssim 0.723\),
- toy ages: \(\sim 13.40–13.50~\mathrm{Gyr}\),
- host ages: \(\sim 13.33–13.77~\mathrm{Gyr}\),
- mechanism amplitude band: a narrow range in `mech_baseline_A0`.

This 12-point kernel is the **Stage 2 view** of the same region that Phase 4
uses as its “external host alignment” subset.

---

## 3. Phase 4 F1 FRW backbone (very short recap)

Phase 4 builds an FRW backbone on top of the Phase 3 baseline mechanism using
an F1 mapping with

- `alpha = 1.0`, `beta = 4.0`,
- matter and vacuum fractions chosen so that the *mean* \(\Omega_\Lambda\)
  over the F1 curve is 0.7.

Key Phase 4 F1 products:

- FRW viability diagnostics + mask:
  - `phase4/outputs/tables/phase4_F1_frw_viability_diagnostics.json`
  - `phase4/outputs/tables/phase4_F1_frw_viability_mask.csv`
- ΛCDM-like window:
  - `phase4/outputs/tables/phase4_F1_frw_lcdm_probe.json`
  - `phase4/outputs/tables/phase4_F1_frw_lcdm_probe_mask.csv`
- Shape-probe overlap summary:
  - `phase4/outputs/tables/phase4_F1_frw_shape_probe.json`

At the checkpoint:

- about half the grid is FRW-viable,
- about 3% of the grid is ΛCDM-like in age and \(\Omega_\Lambda\),
- these ΛCDM-like points sit in a connected \(\theta\) interval that overlaps
  strongly with the 12 host-kernel points.

The Phase 4 docs

- `phase4/docs/PHASE4_EXTERNAL_HOST_KERNEL_BRIDGE_v1.md`
- `phase4/docs/PHASE4_FRW_F1_BASELINE_CHECKPOINT_v1.md`

give a Phase 4-centric account of the same story.

---

## 4. How Stage 2 and Phase 4 meet

At this checkpoint the FRW toy, the host backgrounds, and the mechanism
baseline are aligned as follows:

- Stage 2 provides:
  - a joint grid over \(\theta\) with \(\Omega_m, \Omega_\Lambda\) and host ages,
  - a near-flat subset,
  - a 12-point age-corridor kernel that is near-flat, FRW-viable, and aligned
    with the Phase 4 toy corridor.

- Phase 4 provides:
  - the F1 FRW viability mask and ΛCDM-like probe on the same \(\theta\) grid,
  - diagnostics that quantify how much of the FRW-viable band is ΛCDM-like,
  - a LaTeX table
    `phase4/outputs/tables/phase4_external_host_kernel_constraints_v1.tex`
    that reports the 12-point kernel as seen from the paper’s side.

The comparison table

- `stage2/external_cosmo_host/outputs/tables/stage2_external_host_kernel_comparison_v1.csv`

confirms that, for these 12 points, the repository’s FRW \(\Omega_\Lambda\)
matches the external host’s \(\Omega_\Lambda\) exactly, and the ages agree
within a few tenths of a Gyr.

From the Stage 2 perspective, this means:

> There exists a **small near-flat host subset** whose age and density bands
> are simultaneously:
> - consistent with the F1 FRW ΛCDM-like window, and  
> - consistent with the Phase 3 baseline mechanism amplitudes.

This is a *statement about overlap of bands*, not a uniqueness claim.

---

## 5. How Phase 5 is expected to consume this

The Phase 5 “FRW–host dashboard” sketch lives in:

- `phase5/docs/PHASE5_FRW_HOST_DASHBOARD_SKETCH_v1.md`

From Stage 2’s side, the intended role is:

- provide the *host* panels for a Phase 5 dashboard:
  - near-flat subset view,
  - 12-point kernel,
  - host vs repo age and \(\Omega_\Lambda\) bands;
- expose hooks where real external data (e.g. binned FRW distance
  measurements) can be added later without changing Stage 2 logic.

Any Phase 5 code that consumes Stage 2 host tables must:

1. treat the files listed above as read-only;
2. state explicitly which subset (near-flat, kernel, etc.) it is using;
3. document any extra priors or likelihoods on top of this baseline.

---

## 6. Reproducibility expectations from a Stage 2 viewpoint

To reuse this alignment in future work:

1. **Check out the tagged checkpoint**

   Ensure you are on or derived from

   ```bash
   git checkout stage2_phase4_F1_FRW_baseline_checkpoint_2026-01-15
   ```

   or document any deviations in `PROGRESS_LOG.md`.

2. **Rebuild the external host tables**

   Run the Stage 2 external host scripts as documented in

   - `stage2/docs/STAGE2_EXTERNAL_COSMO_HOSTS_DESIGN_v1.md`
   - `phase4/docs/PHASE4_EXTERNAL_HOST_KERNEL_BRIDGE_v1.md`

   and confirm that the 12-point kernel and its bands reproduce
   `stage2_external_cosmo_host_phase4_constraints_v1.csv`.

3. **Rebuild the Phase 4 F1 FRW diagnostics**

   Run:

   ```bash
   oa && python phase4/src/phase4/run_f1_sanity.py
   oa && python phase4/src/phase4/run_f1_shape_diagnostics.py
   oa && python phase4/src/phase4/run_f1_frw_toy_diagnostics.py
   oa && python phase4/src/phase4/run_f1_frw_corridors.py
   oa && python phase4/src/phase4/run_f1_frw_lcdm_probe.py
   oa && python phase4/src/phase4/run_f1_frw_data_probe.py
   ```

   and verify that the key JSON summaries match the checkpointed values to
   within numerical tolerance.

If these checks pass, the Stage 2 external host machinery and the Phase 4 F1
FRW backbone are considered aligned at this checkpoint.
