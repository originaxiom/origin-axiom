# Stage 2 — FRW data-probe audit (rungs 1–2)

**Scope.**  
This Stage-2 module inspects the FRW “data probe” mask produced in Phase 4, without
modifying any Phase-3/4 code. The goal is to understand the status of the aggregate
data flag `frw_data_ok` and its relation to the FRW viability corridor, so that
Phase-4/5 text can describe the current pipeline honestly.

Source tables:

- `phase4/outputs/tables/phase4_F1_frw_data_probe_mask.csv`
- `phase4/outputs/tables/phase4_F1_frw_viability_mask.csv`

All results are produced under:

- `stage2/frw_data_probe_analysis/outputs/tables/`

---

## Rung 1 — Column-level stats

Script:

- `stage2/frw_data_probe_analysis/src/analyze_frw_data_probes_v1.py`

Output:

- `stage2_frw_data_probe_rung1_column_stats_v1.csv`

Method:

- Load `phase4_F1_frw_data_probe_mask.csv` (2048 rows).
- Identify **boolean-like** columns (dtype bool or subset of {0,1}).
- For each, record `n_true`, `n_false`, `n_na`, and fractions.

Key findings on the 2048-point θ-grid:

- `has_matter_era` and `smooth_H2` are **always true**:
  - `frac_true = 1.0`, `frac_false = 0.0`.
- `has_late_accel` and `frw_viable` are **true on exactly 1016 points**, false on 1032.
- `data_ok` is **always false**:
  - `frac_true = 0.0`, `frac_false = 1.0`.

Already at this level we see:

- Two probes (`has_matter_era`, `smooth_H2`) are **structural sanity checks** that do not restrict the grid in this snapshot.
- The “late acceleration” and “viable” flags are tightly coupled.
- The aggregate “data OK” flag is currently **never satisfied**.

---

## Rung 2 — Cross with FRW viability

Script:

- `stage2/frw_data_probe_analysis/src/analyze_frw_data_probes_vs_viability_v1.py`

Output:

- `stage2_frw_data_probe_rung2_viability_cross_v1.csv`

Method:

- Load both masks (data probes + viability).
- Enforce θ-alignment at tolerance 1e-8.
- For each boolean-like probe column, build the 2×2 table:

  - rows: `frw_viable ∈ {False, True}`
  - columns: `probe ∈ {False, True}`

  and compute fractions with respect to the full 2048-point grid.

Summary (n = 2048):

- `has_matter_era`:
  - True everywhere: all 2048 points pass this probe.
  - Does not further restrict the viability corridor.

- `smooth_H2`:
  - Also true everywhere: again, no additional restriction.

- `has_late_accel`:
  - `frw_viable=True` iff `has_late_accel=True`.
  - In this snapshot, **FRW viability is effectively equivalent to “late acceleration present”**, once the always-true checks are accounted for.

- `frw_viable`:
  - Serves as the canonical viability label; consistent with the above.

- `data_ok`:
  - `frac_probe_true = 0.0` (no θ satisfies `data_ok`).
  - Among the 1016 viable points:
    - `n_tt = 0` (no point is both viable and `data_ok`-true),
    - `n_tf = 1016` (all viable points fail `data_ok`).

Thus, in the current Phase-4 snapshot:

> The **FRW viability corridor is non-empty and nontrivial**, but the aggregate
> data flag `frw_data_ok` is identically false, so the intersection
> `FRW_VIABLE ∧ DATA_OK` is empty.

This matches Stage-2 FRW corridor results, where:

- the family `F6_DATA_OK` has `n_theta = 0`, and
- `FRW_VIABLE_AND_DATA_OK` is also empty.

---

## Interpretation and status

- The existing FRW pipeline already supports a **nontrivial viability corridor**
  (roughly half the θ-grid) and interesting intersections with a toy corridor
  and LCDM-like shape probes.

- However, in this snapshot the **data stage has not been tuned/validated**:
  the combined data flag `frw_data_ok` is never satisfied and therefore
  kills the entire viability corridor.

- We treat this as a **pipeline state** (“data gate not yet open”), not as a
  physical exclusion of the origin-axiom corridor:
  further work is required to define, calibrate, and test `frw_data_ok` before
  any observational claims can be made.

**Status:** This Stage-2 audit is complete for the current Phase-4 outputs.
It provides a precise, reproducible statement that future Phase-4/5 text can
quote when describing the status of FRW + data filters.

