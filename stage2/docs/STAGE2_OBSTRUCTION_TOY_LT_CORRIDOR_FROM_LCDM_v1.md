# Stage 2 obstruction: toy late-time corridor from LCDM box (v1)

Status.  
This memo documents a toy late-time corridor derived purely from the existing LCDM-like band in the Phase 4 FRW masks. It is an internal Stage 2 construct implemented on top of the static FRW kernel; it is not tied to any specific external dataset and does not modify Phase 0–5 contracts or Stage 2 promotion gates.

## 1. Definition

Helper script:

- `stage2/obstruction_tests/src/build_toy_lt_corridor_from_lcdm_box_v1.py`

Input:

- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_static_frw_kernel_v1.csv`

Outputs:

- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_toy_lt_corridor_from_lcdm_box_v1.csv` – static kernel table augmented with a toy late-time corridor flag.
- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_toy_lt_corridor_from_lcdm_box_summary_v1.csv` – small summary of family sizes and fractions.

The script:

- identifies the LCDM-like subset using the existing `lcdm_like` flag in the kernel table,
- computes the minimal enclosing box in the plane \((E_{\mathrm{vac}}, \omega_{\Lambda})\) over these LCDM-like points,
- defines a toy late-time corridor flag `lt_corridor_box_from_lcdm` which is 1 precisely when a θ point lies inside this box,
- records summary counts for:
  - `ALL_GRID`,
  - `PRE_DATA_KERNEL`,
  - `TOY_LT_BOX_FROM_LCDM`,
  - `KERNEL_AND_TOY_LT_BOX_FROM_LCDM`,
  - `LCDM_AND_TOY_LT_BOX_FROM_LCDM`,
  - `TOY_CORRIDOR_AND_TOY_LT_BOX_FROM_LCDM`.

## 2. Interpretation

This toy corridor is intended as an internal exercise of the external-style corridor machinery:

- It behaves like a late-time expansion band because it is defined in terms of vacuum-sector scalars `(E_vac, omega_lambda)` and can be viewed as a simple box in that space.
- It is entirely derived from the existing LCDM-like mask; no new observational input or external numerical thresholds are introduced.
- The resulting flag `lt_corridor_box_from_lcdm` can be intersected with the pre-data kernel and other families in the same way as the Stage 2 FRW corridor masks, providing a testbed for future external-style corridors.

From an obstruction perspective:

- The box tests how sensitive the pre-data kernel and the 40-point sweet-spot region are to a simple, LCDM-based shaping of the vacuum sector.
- Because the box is derived from the current LCDM-like band, it is closer to a sanity-check corridor than to a genuine external constraint; future rungs must take care not to over-interpret it.

## 3. Non-claims and next steps

Non-claims:

- This toy corridor is not a fit to any particular dataset and is not a substitute for a genuine late-time expansion constraint.
- It does not introduce or promote any special θ value; it only reshapes the existing FRW scalar space.
- No phase-level claims, FRW masks, or promotion gates are altered by this construction.

Next steps:

- Use the summary table to compare:
  - how many points in the pre-data kernel fall inside the toy box,
  - how the box overlaps with the LCDM-like band and the toy FRW corridor,
  - whether the 40-point triple intersection region is robust under this reshaping.
- In future, introduce genuinely external-style corridors as separate helpers and compare their behaviour to this internally derived toy corridor under explicit Phase 0–style gates.
