# Stage 2 – Mechanism/measure belt summary (Phase 3 tables, rungs 1–6, v1)

**Scope.**  
Summarise the Stage 2 mech/measure analysis that inspects Phase 3 numerical tables and identifies well-behaved, probability-like quantities. All work is downstream of Phase 3 and Phase 5 and does not change any canonical claims; it provides diagnostics and candidate measures/flags only.

**Status.**  
Diagnostic-only. No single column is promoted to a fundamental θ-measure at this rung.

For a detailed rung-by-rung description, see:

- `docs/STAGE2_MECH_MEASURE_RUNG1_6_SUMMARY_v1.md`

---

## 1. Inputs and outputs

Inputs:

- All Phase 3 tables under `phase3/outputs/tables/`, including:
  - `mech_baseline_scan.csv`
  - `mech_binding_certificate.csv`
  - other mechanism diagnostic tables produced by the Phase 3 pipeline.

Outputs (representative):

- `stage2_mech_rung1_phase3_table_inventory_v1.csv`
- `stage2_mech_rung2_phase3_column_stats_v1.csv`
- `stage2_mech_rung3_phase3_probability_like_candidates_v1.csv`
- `stage2_mech_rung4_phase3_measure_and_flag_candidates_v1.csv`
- `stage2_mech_rung5_phase3_measure_theta_profiles_v1.csv`
- `stage2_mech_rung6_phase3_preferred_measure_candidates_v1.csv`

All of these live under:

- `stage2/mech_measure_analysis/outputs/tables/`

---

## 2. Rungs 1–6 at a glance

- **Rung 1 – Inventory of Phase 3 tables.**  
  Enumerates all CSV and JSON tables in `phase3/outputs/tables/` and records basic metadata (file type, byte size, row and column counts). Establishes a reproducible snapshot of the Phase 3 numerical landscape.

- **Rung 2 – Column-level stats.**  
  For each numeric column in the Phase 3 CSV tables, records simple statistics (min, max, mean, standard deviation, fraction of finite entries). Identifies columns that are numerically well-behaved.

- **Rung 3 – Probability-like candidates.**  
  Flags columns whose values are bounded, non-degenerate, and live on a compact support (for example roughly in [0,1]) as “probability-like” candidates that might later serve as measures or flags.

- **Rung 4 – Measure vs flag classification.**  
  Splits probability-like candidates into:
  - **measure-like** (smooth, graded distributions), and
  - **flag-like** (near-Boolean, with values concentrated near 0 and 1).

- **Rung 5 – θ-profiles.**  
  Studies how candidate measures and flags behave as functions of θ, recording monotonicity, peaks, and simple shape descriptors on the θ grid.

- **Rung 6 – Preferred candidates.**  
  Selects a small set of numerically well-behaved candidate measures and flags suitable for use as Stage 2 diagnostics or weights, while explicitly avoiding the declaration of a single “canonical” θ-measure.

---

## 3. Takeaways

- Phase 3 already provides smooth, well-controlled scalar diagnostics over θ that can be treated as probability-like quantities.
- These diagnostics are redundant with the underlying mechanism; they do not yet define an independently motivated measure on θ.
- Stage 2 mech/measure results are accepted as diagnostic infrastructure only. Any promotion of a particular column to a canonical θ-measure would require a separate, Phase 0–style gate and updates to Phase 3/5 text.
