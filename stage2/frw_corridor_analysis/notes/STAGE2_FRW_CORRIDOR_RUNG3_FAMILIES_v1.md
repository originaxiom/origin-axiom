# Stage 2 — FRW Corridor Analysis (Rung 3: Family Definitions)

**Rung ID:** stage2_frw_corridor_rung3_families  
**Status:** ACTIVE — descriptive FRW families  
**Scope level:** Stage 2 only (no changes to Phase 0–5)

## 1. Intent

This rung turns the boolean census from Rung 2 into a small set of
named **FRW families** with:

- clearly defined source masks and columns,
- counts of theta grid points in each family,
- fractions of the full grid they occupy.

It is **descriptive only** and does not introduce new physics claims.
Any promotion into the main phased program will be decided in later rungs.

## 2. Inputs

- `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung2_bool_census_v1.csv`

Rung 2 is assumed to be up-to-date relative to Phase 4 masks.

## 3. Outputs

- `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung3_families_v1.csv`

Each row describes one FRW family:

- `family_id`      — stable identifier (e.g. `F1_FRW_VIABLE`)
- `label`          — human-readable description
- `section`        — census section (for traceability)
- `source_key`     — which Phase 4 mask the family comes from
- `col_name`       — exact boolean column used
- `n_theta`        — number of theta points in this family
- `frac_of_grid`   — fraction of the total theta grid
- `n_rows_source`  — rows in the source mask (sanity; should be grid size)
- `notes`          — informal notes about interpretation

## 4. Family definitions (current)

The current family set is:

1. `F1_FRW_VIABLE`  
   - Source: `phase4/outputs/tables/phase4_F1_frw_viability_mask.csv`, column `frw_viable`  
   - Description: Baseline FRW-viable slice in Phase 4.

2. `F2_LCDM_LIKE`  
   - Source: `phase4/outputs/tables/phase4_F1_frw_lcdm_probe_mask.csv`, column `lcdm_like`  
   - Description: Points flagged as LCDM-like in Phase 4.

3. `F3_TOY_CORRIDOR`  
   - Source: `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`, column `in_toy_corridor`  
   - Description: Theta points in the toy corridor band.

4. `F4_CORRIDOR_AND_VIABLE`  
   - Source: `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`, column `shape_and_viable`  
   - Description: Intersection of the toy corridor band with FRW-viable flag.

5. `F5_CORRIDOR_AND_LCDM`  
   - Source: `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`, column `shape_and_lcdm`  
   - Description: Intersection of the toy corridor band with LCDM-like flag.

6. `F6_DATA_OK`  
   - Source: `phase4/outputs/tables/phase4_F1_frw_data_probe_mask.csv`, column `data_ok`  
   - Description: Points passing the external data filter; currently empty in the baseline repo since no data are attached.

## 5. How to run

From the repo root:

```bash
python stage2/frw_corridor_analysis/src/analyze_frw_corridor_families_v1.py
```

Then inspect:

```text
stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung3_families_v1.csv
```

## 6. Role in the broader roadmap

This rung bridges between:

- **Phase 4**: which already constructed FRW masks and toy corridors, and  
- **Later Stage 2 rungs**: where we will examine the parameter-space
  properties of these families (e.g. distributions of theta, E_vac, omega_lambda).

In the larger roadmap:

- Rung 2 told us *how strongly populated* each boolean flag is.
- Rung 3 gives each meaningful slice a **name**, **size**, and **fraction**.
- Rung 4+ can examine whether any family (especially candidates like
  `F4_CORRIDOR_AND_VIABLE` or `F5_CORRIDOR_AND_LCDM`) is stable, interpretable,
  and closely enough tied to the non-cancellation mechanism to justify:

  - **Option A:** lightweight mention or figure in Phase 5, or
  - **Option B:** a dedicated FRW-focused continuation (Phase 6 paper under
    the staged program).

No such promotion is implied here; this rung only prepares structured,
reproducible summaries for later scientific judgment.
