# Stage 2: Phase 3 mech/measure analysis (Rungs 1–6)

This document summarises a Stage 2 analysis spine that inspects the numerical
tables behind Phase 3 without modifying any Phase 3 or Phase 5 claims.

The goal is to identify well-behaved, probability-like quantities that might
later serve as candidate "measures" or "flags" for the non-cancellation
mechanism, while keeping all decisions strictly downstream and reversible.

## Rung 1 — Phase 3 table inventory

- Script:
  - `stage2/mech_measure_analysis/src/inventory_phase3_tables_v1.py`
- Output:
  - `stage2/mech_measure_analysis/outputs/tables/stage2_mech_rung1_phase3_table_inventory_v1.csv`
- Role:
  - Enumerates all CSV/JSON tables in `phase3/outputs/tables`, recording
    file type, byte size, and, for CSVs, `(n_rows, n_cols)`. This provides
    a reproducible snapshot of the numerical Phase 3 landscape on which
    later rungs operate.

## Rung 2 — Column-level stats

- Script:
  - `stage2/mech_measure_analysis/src/analyze_phase3_table_columns_v1.py`
- Output:
  - `stage2/mech_measure_analysis/outputs/tables/stage2_mech_rung2_phase3_column_stats_v1.csv`
- Role:
  - For each Phase 3 CSV table, record simple per-column statistics
    (min/max/mean, uniqueness, NaN counts, coarse type hints, etc.).
  - For JSON diagnostics tables, store a compact summary.
  - This rung is purely descriptive and defines the feature space used
    in Rungs 3–6.

## Rung 3 — Probability-like candidates

- Script:
  - `stage2/mech_measure_analysis/src/analyze_phase3_probability_like_columns_v1.py`
- Output:
  - `stage2/mech_measure_analysis/outputs/tables/stage2_mech_rung3_phase3_probability_like_candidates_v1.csv`
- Role:
  - Filter the Rung 2 stats to columns whose values look probability-like
    (roughly within `[0, 1]` with mild tolerances and no obvious pathologies).
  - Attach notes explaining why each column was selected.
  - This produces a first list of plausible measure-or-weight-like quantities.

## Rung 4 — Measure vs flag role tagging

- Script:
  - `stage2/mech_measure_analysis/src/select_phase3_measure_candidates_v1.py`
- Output:
  - `stage2/mech_measure_analysis/outputs/tables/stage2_mech_rung4_phase3_measure_and_flag_candidates_v1.csv`
- Role:
  - Assign a tentative semantic role to each probability-like candidate:
    - `measure_candidate`: continuous or graded quantities,
    - `flag_candidate`: Boolean-like or thresholded columns.
  - No new physics is asserted; the rung just records which existing
    Phase 3 quantities could naturally play which roles in later work.

## Rung 5 — θ-profiles for candidates

- Script:
  - `stage2/mech_measure_analysis/src/analyze_phase3_measure_theta_profiles_v1.py`
- Output:
  - `stage2/mech_measure_analysis/outputs/tables/stage2_mech_rung5_phase3_measure_theta_profiles_v1.csv`
- Role:
  - For each candidate, extract its behaviour as a function of θ across
    the Phase 3 baseline grid.
  - Record simple shape diagnostics (e.g., approximate monotonicity,
    support, spread) that inform whether a column might be a stable,
    interpretable measure.

## Rung 6 — Preferred candidates (Stage 2 shortlist)

- Script:
  - `stage2/mech_measure_analysis/src/select_phase3_preferred_measures_v1.py`
- Output:
  - `stage2/mech_measure_analysis/outputs/tables/stage2_mech_rung6_phase3_preferred_measure_candidates_v1.csv`
- Role:
  - Combine Rung 5 shape information with basic diagnostics (boundedness,
    coverage, etc.) to assign scores and decisions such as
    `keep_as_primary`, `keep_as_secondary`, or `discard_for_now`.
  - At this stage, all decisions remain strictly Stage 2:
    - no changes to Phase 3 or Phase 5 papers,
    - no claim that any candidate is the unique or final "measure".
  - The output is a transparent shortlist for future physics-facing
    scrutiny and potential coupling to the FRW corridor analysis.

## Status and future use

- All Rungs 1–6 run cleanly from the current Phase 3 artifacts and
  populate CSVs under:
  - `stage2/mech_measure_analysis/outputs/tables/`
- The Stage 2 mech/measure spine is downstream-only and reversible.
- Promotion of any candidate into the main phased program will be
  decided in future rungs, potentially in concert with Stage 2 FRW
  corridor analysis and Phase 5 summary considerations.

