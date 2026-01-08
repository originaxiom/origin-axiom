# Stage 2 — FRW Corridor Analysis (Rung 1)

**Rung ID:** stage2_frw_corridor_rung1  
**Status:** ACTIVE — schema + sanity introspection  
**Scope level:** Stage 2 only (no changes to Phase 0–5)  

## 1. Intent

This rung performs a **read-only sanity pass** over the Phase 4 FRW-related
tables, to understand:

- which FRW masks and corridor summaries are present,
- their basic shapes (rows, columns),
- key boolean / diagnostic columns that future rungs will use.

It does **not** modify any Phase 4 or Phase 5 artifacts. It only writes under:

- `stage2/frw_corridor_analysis/outputs/tables/`

## 2. Inputs (expected from Stage 1 / Phase 4)

Read-only files, relative to repo root:

- `phase4/outputs/tables/phase4_F1_frw_viability_mask.csv`
- `phase4/outputs/tables/phase4_F1_frw_lcdm_probe_mask.csv`
- `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`
- `phase4/outputs/tables/phase4_F1_frw_data_probe_mask.csv`
- `phase4/outputs/tables/phase4_F1_frw_corridors.json`

These are assumed to be produced by the Phase 4 gate and treated as
canonical Stage 1 artifacts.

## 3. Outputs (Stage 2 only)

- `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung1_sources_v1.csv`

This table records, per source file:

- section, key, and relative path
- existence + size
- row / column counts (for CSV sources)
- column names (CSV)
- a short semantic note where possible (e.g., presence of `theta`, `frw_viable`, etc.)

## 4. How to run

From the repo root:

\`\`\`bash
python stage2/frw_corridor_analysis/src/analyze_frw_corridor_v1.py
\`\`\`

After running, inspect:

- the terminal summary, and
- the CSV at:

\`\`\`text
stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung1_sources_v1.csv
\`\`\`

## 5. Relation to Stage 1 (Phases 0–5)

- **One-way dependency**: this rung **reads** Phase 4 FRW tables but does **not**
  alter any Phase 0–5 artifacts.
- It is a preparation step toward defining **FRW corridor families** and
  eventual **promotion** into either:
  - (Option A) a small, well-scoped addition to Phase 5, or
  - (Option B) a dedicated Stage 2 / Phase 6 paper focused on FRW structure.

The promotion choice will be made **per rung / claim**, based on weight and clarity.

## 6. Next rungs (sketched, not yet active)

- **Rung 2 – Corridor tagging**
  - Define operative masks/labels for "FRW corridor" membership, using the
    existing viability + LCDM-like + shape probe structure.
- **Rung 3 – Corridor families**
  - Cluster or otherwise stratify FRW-viable θ regions into interpretable
    families, tied back to the non-cancellation mechanism.
- **Rung 4+ – Promotion candidates**
  - Identify robust, low-regret claims that could be promoted into
    Phase 5 or a dedicated FRW paper.

