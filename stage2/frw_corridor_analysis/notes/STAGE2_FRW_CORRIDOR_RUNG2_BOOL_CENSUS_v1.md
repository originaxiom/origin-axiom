# Stage 2 — FRW Corridor Analysis (Rung 2: Boolean Census)

**Rung ID:** stage2_frw_corridor_rung2_bool_census  
**Status:** ACTIVE — boolean census over FRW masks  
**Scope level:** Stage 2 only (no changes to Phase 0–5)

## 1. Intent

This rung performs a **boolean census** of FRW-related mask tables from Phase 4.
It answers questions like:

- How many θ grid points are FRW-viable?
- How many are LCDM-like?
- How many lie in any "corridor" or shape-filter region?
- How much of the θ-grid is screened out by existing flags?

The logic is intentionally generic: it identifies boolean-like columns by their
value patterns, rather than assuming specific column names, to stay robust to
future refinements.

## 2. Inputs (read-only Phase 4 artifacts)

Relative to repo root:

- `phase4/outputs/tables/phase4_F1_frw_viability_mask.csv`
- `phase4/outputs/tables/phase4_F1_frw_lcdm_probe_mask.csv`
- `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`
- `phase4/outputs/tables/phase4_F1_frw_data_probe_mask.csv`

These are treated as **Stage 1 canon** and must not be modified here.

## 3. Outputs (Stage 2 only)

- `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung2_bool_census_v1.csv`

Each row of this table summarizes one boolean-like column:

- `section`      — logical grouping (currently `phase4_frw_masks`)
- `source_key`   — which mask (viability/lcdm/shape/data)
- `relpath`      — source file path
- `col_name`     — column name in the CSV
- `dtype`        — pandas dtype
- `n_rows`       — total rows
- `n_true`       — count of true values
- `n_false`      — count of false values
- `n_na`         — count of non-boolean / missing entries
- `frac_true`    — n_true / (n_true + n_false), if defined
- `frac_false`   — n_false / (n_true + n_false), if defined
- `notes`        — heuristic notes (e.g. "viability-related", "LCDM-like related")

## 4. How to run

From the repo root:

\`\`\`bash
python stage2/frw_corridor_analysis/src/analyze_frw_corridor_bool_census_v1.py
\`\`\`

Then inspect:

\`\`\`text
stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung2_bool_census_v1.csv
\`\`\`

## 5. Role in the broader roadmap

This rung:

- stays **fully downstream** of Phase 4 artifacts (no feedback into phases),
- prepares a compact view of which FRW flags are populated and how strongly,
- lays the groundwork for:

  - Rung 3: defining FRW **corridor families** (e.g., intersection of
    viability, LCDM-like, and corridor/shape flags),
  - Rung 4+: exploring whether any such families are robust enough to
    become candidates for promotion into:

    - **Option A:** a lightweight addition to Phase 5, or
    - **Option B:** a dedicated Stage 2 / Phase 6 FRW-focused paper.

Promotion decisions will be made per rung / claim, based on stability,
interpretability, and relevance to the core non-cancellation mechanism.
