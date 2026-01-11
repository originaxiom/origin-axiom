# Stage 2 mechanism diagnostics verdict (Phase 3 amplitudes and measure candidates)

Status (2026-01-11): This document synthesises the Stage 2 mechanism/measure rungs into a compact verdict about Phase 3 mechanism-derived scalars. It is descriptive and diagnostic-only and does not introduce new claims beyond those already present in Phase 3 contracts and Stage 2 docs.

## 1. Inputs and scope

This verdict is based on the Stage 2 mechanism/measure belt under `stage2/mech_measure_analysis/`, in particular:

- `inventory_phase3_tables_v1.py` → `stage2_mech_rung1_phase3_table_inventory_v1.csv` (Rung 1: table inventory).
- `analyze_phase3_table_columns_v1.py` → `stage2_mech_rung2_phase3_column_stats_v1.csv` (Rung 2: column stats).
- `analyze_phase3_probability_like_columns_v1.py` → `stage2_mech_rung3_phase3_probability_like_candidates_v1.csv` (Rung 3: probability-like candidates).
- `select_phase3_measure_candidates_v1.py` → `stage2_mech_rung4_phase3_measure_and_flag_candidates_v1.csv` (Rung 4: measure vs flag classification).
- `analyze_phase3_measure_theta_profiles_v1.py` → `stage2_mech_rung5_phase3_measure_theta_profiles_v1.csv` (Rung 5: θ-profiles).
- `select_phase3_preferred_measures_v1.py` → `stage2_mech_rung6_phase3_preferred_measure_candidates_v1.csv` (Rung 6: preferred candidates).

All of these scripts act on canonical Phase 3 mechanism tables under `phase3/outputs/tables/`, especially `mech_baseline_scan.csv` and `mech_binding_certificate.csv`. They are strictly downstream diagnostics: they do not change Phase 3 tables or claims; they read Phase 3 outputs and emit Stage 2 CSVs and summary docs.

## 2. Inventory and basic column behavior

Rungs 1–2 (`stage2_mech_rung1_phase3_table_inventory_v1.csv` and `stage2_mech_rung2_phase3_column_stats_v1.csv`) establish that:

- The Phase 3 mechanism tables under `phase3/outputs/tables/` form a **small, well-defined set** of CSVs with consistent row counts and dimensions, dominated by:
  - baseline scans (`mech_baseline_scan.csv` and variants),
  - binding certificates (`mech_binding_certificate.csv` and related tables),
  - and auxiliary diagnostics where needed.
- Numeric columns corresponding to mechanism-derived scalars (e.g. baseline amplitudes, penalties, binding indicators, and related quantities) are **finite and bounded** on the sampled θ-grid:
  - no systematic NaN or inf contamination,
  - minima and maxima lie in reasonable ranges set by the mechanism contract,
  - standard deviations and finite fractions are consistent with well-behaved distributions rather than pathological spikes.

At this level, the inventory and column stats confirm that Phase 3 mechanism tables are **numerically sound** and suitable for downstream diagnostics: there is no evidence of broken columns or obvious data pathologies in the mechanism outputs that Stage 2 uses.

## 3. Probability-like columns and measure/flag candidates

Rungs 3–4 (`stage2_mech_rung3_phase3_probability_like_candidates_v1.csv` and `stage2_mech_rung4_phase3_measure_and_flag_candidates_v1.csv`) identify and classify “probability-like” columns:

- A **probability-like** column is defined operationally as a numeric column whose values:
  - are bounded within a closed interval [a, b],
  - have nontrivial spread (i.e. not nearly constant),
  - and avoid degenerate or extreme behavior across the θ-grid.
- Applying this filter to Phase 3 tables yields a **short list** of columns that behave like candidate measures or flags: they are bounded, non-degenerate, and numerically stable.

Stage 2 then splits these candidates into two classes:

- **Measure-like candidates:** columns whose distributions are relatively smooth and graded across θ, varying continuously or at least gradually rather than flipping between extremes. These are natural candidates for diagnostic weights or continuous “importance” scores over θ, in a toy sense.
- **Flag-like candidates:** columns whose distributions are near-Boolean or dominated by two distinct plateaux, behaving more like indicator flags than genuine measures. These are natural candidates for defining masks or binary diagnostics (e.g. binding regimes vs non-binding).

The resulting Rung 4 CSV (`stage2_mech_rung4_phase3_measure_and_flag_candidates_v1.csv`) is a map from Phase 3 columns to measure-like vs flag-like roles, grounded in their empirical distributions.

This step supports two conclusions:

- Phase 3 mechanism outputs contain **several well-behaved probability-like scalars** that could, in principle, serve as diagnostic measures or flags.
- There is no need to invent artificial measures at Stage 2; the mechanism itself produces a small family of numerically robust, structurally meaningful scalar diagnostics.

## 4. θ-profiles and preferred mechanisms candidates

Rung 5 (`stage2_mech_rung5_phase3_measure_theta_profiles_v1.csv`) examines the behavior of measure-like candidates as functions of θ. For each candidate, Stage 2 records:

- basic shape features (e.g. monotonicity segments, presence of peaks or plateaux),
- rough gradients and curvature indicators,
- and whether the profile appears noisy, oscillatory, or smooth at the working resolution.

The θ-profiles show that:

- most measure-like candidates are **smooth or gently varying** over θ at the current grid resolution,
- there are no unexpected spikes, discontinuities, or numerically unstable stretches in the profiles,
- and the general behavior is consistent with what one expects from mechanism-derived scalars linked to FRW quantities (e.g. larger amplitudes in regions with stronger effective vacuum contributions).

Rung 6 (`stage2_mech_rung6_phase3_preferred_measure_candidates_v1.csv`) then selects a **small subset of preferred candidates** on the basis of:

- numerical stability (boundedness, absence of pathologies),
- smooth or at least reasonably structured θ-profiles,
- and distinctiveness (avoid redundant clones of the same behavior).

The result is a shortlist of “preferred mechanism-derived diagnostics” that are especially well-behaved over θ and hence particularly suitable as Stage 2 diagnostic weights, colorings, or summary variables.

Crucially, Rung 6 **does not** promote any one of these candidates to a canonical θ-measure; it designates them as **preferred diagnostics** for analysis, not as fundamental measures.

## 5. Mechanism diagnostics verdict (current snapshot)

Putting the mech/measure rungs together, the Stage 2 mechanism belt supports the following verdict for the current Phase 3 mechanism outputs:

- Phase 3 mechanism tables are **numerically robust**: they form a small, well-audited set of CSVs with bounded, finite, and non-degenerate scalar columns that are suitable for downstream use.
- Among these scalars, there exists a **short list of probability-like candidates** that naturally split into measure-like and flag-like roles based on their empirical distributions. This confirms that the mechanism itself provides a useful set of diagnostic scalars without additional ad hoc constructs.
- θ-profiles of measure-like candidates are **smooth and well-behaved** on the current grid, with no evidence of numerical instability or pathological dependence on θ. This supports using them as diagnostic axes or weights in Stage 2 analyses.
- A small set of **preferred mechanism-derived diagnostics** can be identified on purely numerical and structural grounds. These preferred candidates are excellent diagnostic tools for Stage 2 belts and future interface layers (Phase 5).

At the same time:

- The Stage 2 mech/measure belt **does not** identify a unique, physically motivated θ-measure. The preferred candidates are useful diagnostics but are numerically redundant with each other and, as shown by joint mech–FRW analysis, largely reparameterise FRW scalars.
- No special behavior at θ★ emerges from the mech-only diagnostics at this stage beyond what is seen in FRW quantities; any attempt to interpret a mechanism-derived scalar as a fundamental measure over θ would require additional principles and promotion gates.

In short: the mechanism belt shows that Phase 3 provides a rich and well-controlled diagnostic scalar field over θ, but in the current toy setup these scalars function as **diagnostics, not as a canonical measure**, and they do not pick out θ★ in an interesting way on their own.

## 6. Potential future rungs (not executed here)

This verdict suggests, but does not enact, a few future Stage 2 and Phase 5 rungs:

- Mechanism-variation belts that explore alternative non-cancellation implementations and compare how the catalog of probability-like candidates and their θ-profiles change across variants.
- Information-theoretic diagnostics (e.g. entropy and mutual information between mechanism scalars and FRW scalars) to quantify precisely how redundant or compressive the mechanism-derived scalars are relative to FRW quantities.
- Interface-layer rungs in Phase 5 that expose the preferred mechanism-derived diagnostics as part of a human-readable summary of “what the mechanism actually does over θ” without promoting any of them to a canonical measure.

These are left for future work and are not part of this descriptive verdict.
