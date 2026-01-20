# Stage 2 obstruction static FRW kernel families (v1)

Status.  
This memo documents a Stage 2 obstruction helper that summarises how the static FRW pre-data kernel sits inside the existing FRW corridor structure. It is diagnostic-only and downstream of the Phase 4 and Stage 2 FRW belts.

Definition.  
The script `stage2/obstruction_tests/src/analyze_static_frw_kernel_families_v1.py` reads

- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_static_frw_kernel_v1.csv`

and computes counts and fractions for several θ-families, writing

- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_static_frw_kernel_families_v1.csv`.

For each family it records

- `family_name` – label for the family,
- `n_points` – number of θ points in the family,
- `frac_of_grid` – fraction of the full 2048-point grid,
- `frac_of_kernel` – fraction of the pre-data kernel (where applicable),
- `note` – short description where useful.

Families.  
The current version includes:

- `ALL_GRID` – all θ points on the Phase 4 FRW grid.
- `PRE_DATA_KERNEL` – points with `in_pre_data_kernel = 1` (currently defined by `frw_viable = 1` with always-true sanity checks inherited from Phase 4).
- `LCDM_LIKE` – points flagged as LCDM-like by the Phase 4 FRW LCDM probe mask.
- `TOY_CORRIDOR` – points in the Phase 4 toy FRW corridor.
- `KERNEL_AND_LCDM` – intersection of the pre-data kernel with the LCDM-like set.
- `KERNEL_AND_TOY` – intersection of the pre-data kernel with the toy corridor.
- `LCDM_AND_TOY` – intersection of LCDM-like points with the toy corridor.
- `KERNEL_AND_LCDM_AND_TOY` – triple intersection of kernel, LCDM-like, and toy corridor.
- `SHAPE_AND_VIABLE` – points flagged as both shape-selected and FRW-viable in the shape probe mask.
- `SHAPE_AND_LCDM` – points flagged as both shape-selected and LCDM-like.

Interpretation.  
This helper is intended to make it easier to see how the pre-data FRW kernel decomposes across the existing Stage 2 FRW families, and to provide a compact input for later obstruction-program rungs (for example robustness checks or external-style corridor tests). It does not introduce new thresholds, mappings, or claims about the real universe. All interpretation remains governed by the Phase 4 FRW docs, the Stage 2 FRW and corridor summaries, and the obstruction-program memos.
