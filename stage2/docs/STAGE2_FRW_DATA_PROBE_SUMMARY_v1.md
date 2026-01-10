# Stage 2 – FRW data-probe belt summary (rungs 1–2, v1)

**Scope.**  
Summarise the Stage 2 FRW data-probe audit that inspects the Phase 4 FRW “data probe” mask. The belt does not change any Phase 3/4 code; it clarifies how the aggregate data flag `frw_data_ok` behaves relative to the FRW viability corridor on the current θ grid.

**Status.**  
Diagnostic-only. As of the current snapshot, `frw_data_ok` is never satisfied; all FRW families are interpreted as pre-data corridors.

For detailed methods and tables, see:

- `stage2/frw_data_probe_analysis/docs/STAGE2_FRW_DATA_PROBE_AUDIT_v1.md`

---

## 1. Inputs and outputs

Inputs:

- `phase4/outputs/tables/phase4_F1_frw_data_probe_mask.csv`  (2048 × 11)
- `phase4/outputs/tables/phase4_F1_frw_viability_mask.csv`   (2048 × 8)

Outputs:

- `stage2_frw_data_probe_rung1_column_stats_v1.csv`
- `stage2_frw_data_probe_rung2_viability_cross_v1.csv`

All outputs live under:

- `stage2/frw_data_probe_analysis/outputs/tables/`

---

## 2. Rungs 1–2 at a glance

- **Rung 1 – Column stats for data probes.**  
  Records basic counts and fractions for boolean-like data-probe columns (`has_matter_era`, `smooth_H2`, `has_late_accel`, `data_ok`, and related fields) on the 2048-point θ grid.

- **Rung 2 – Cross tables vs FRW viability.**  
  Builds 2×2 cross tables between each data probe and the FRW viability mask `frw_viable`, focusing in particular on the aggregate flag `frw_data_ok`.

---

## 3. Takeaways

On the current Phase 4 snapshot:

- `has_matter_era` and `smooth_H2` are always true, so they act as structural sanity checks rather than additional cuts.
- `has_late_accel` and `frw_viable` agree exactly (1016 grid points true, 1032 false), so FRW viability is effectively equivalent to “late acceleration present” once the always-true checks are accounted for.
- `frw_data_ok` is identically false on the 2048-point grid, including on all FRW-viable points; the intersection FRW_VIABLE ∧ DATA_OK is empty.

Interpretation:

- The Phase 4 FRW pipeline already supports a nontrivial viability corridor, and the Stage 2 corridor rungs analyse its structure and intersections with toy corridor and LCDM-like masks.
- In the current snapshot, the aggregate data flag is effectively a parked gate: no θ values pass, so all FRW families should be interpreted as pre-data corridors.
- Tuning and validating the data probes, and opening the data gate in a controlled way, is deferred to future work; this belt records the present state so it is auditable.
