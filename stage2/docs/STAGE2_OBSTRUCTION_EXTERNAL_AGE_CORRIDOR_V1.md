# Stage 2 obstruction: toy external-style age corridor (v1)

Status.  This memo documents a first toy external-style corridor implemented on top of the static FRW kernel. The corridor is defined as an age band in gigayears and is intended purely as an internal test of the obstruction machinery. The numerical bounds are placeholders and do not represent a tuned fit to any particular dataset.

## 1. Definition

Helper script:

- `stage2/obstruction_tests/src/apply_external_age_corridor_v1.py`

Input:

- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_static_frw_kernel_v1.csv`

Outputs:

- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_age_corridor_v1.csv` – static kernel table augmented with `external_age_corridor_v1`.
- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_age_corridor_summary_v1.csv` – summary of family sizes and fractions.

The script:

- reads the static kernel table with columns including `theta`, `age_Gyr`, `in_pre_data_kernel`, `lcdm_like`, and `in_toy_corridor`,
- defines a toy age band in gigayears:
  - `AGE_MIN_GYR = 10.0`,
  - `AGE_MAX_GYR = 20.0`,
  with the understanding that these are conservative placeholder values to be revised in future design rungs,
- sets `external_age_corridor_v1 = 1` for all θ points whose `age_Gyr` lies in this band,
- records family counts for:
  - `ALL_GRID`,
  - `PRE_DATA_KERNEL`,
  - `EXTERNAL_AGE_CORRIDOR_V1`,
  - `KERNEL_AND_EXTERNAL_AGE_V1`,
  - `LCDM_AND_EXTERNAL_AGE_V1`,
  - `TOY_CORRIDOR_AND_EXTERNAL_AGE_V1`,
  - `KERNEL_LCDM_TOY_AND_EXTERNAL_AGE_V1`.

In the current snapshot, the summary helper shows that `EXTERNAL_AGE_CORRIDOR_V1` is true for all 2048 grid points, with 1016 of them in the pre-data kernel. The age band is therefore effectively a no-op filter on this grid: it preserves the kernel and all previously defined internal families, including the 40-point sweet subset.

## 2. Interpretation

Purpose.

- This age corridor is the first explicit example of an external-style filter in the obstruction program:
  - it takes a simple scalar that would naturally be constrained by observations (cosmic age),
  - builds a band in that scalar space,
  - and checks how the pre-data kernel and existing families respond.

Internal role.

- Because the numerical bounds are deliberately broad, the corridor is designed more as a structural test than as a sharp constraint:
  - it preserves the pre-data kernel (all 1016 kernel points satisfy the band),
  - it preserves the LCDM-like band (63 kernel points),
  - it preserves the FRW toy corridor (1186 grid points),
  - and the 40-point sweet subset where kernel, LCDM-like band, and toy corridor coincide remains unchanged.
- The families summary makes it easy to see:
  - that no part of the kernel lies outside the toy age band at this stage,
  - how the age band overlaps the LCDM-like band and the FRW toy corridor,
  - and that the obstruction machinery for defining and intersecting external-style flags behaves as expected.

## 3. Non-claims and future tightening

Non-claims.

- `external_age_corridor_v1` is not a fit to a specific dataset or a calibrated cosmological age bound.
- The chosen band `[10, 20]` Gyr is a placeholder, deliberately wide so the current toy FRW setup is not artificially over-constrained.
- No phase-level contracts, FRW masks, or Stage 2 promotion gates are changed by this construction.

Future tightening.

- In future rungs, the age band can be tightened or replaced by a more realistic age corridor, guided by:
  - external cosmological constraints,
  - Stage II host scenarios, or
  - more refined FRW diagnostics in Phase 4.
- Any such tightening will be introduced as a separate design rung with explicit justification and a clear record of how the new band interacts with the kernel and the existing families.

From an obstruction perspective, this toy age corridor is a first scaffolding step: it shows how external-style questions can be phrased and intersected with the static kernel without yet committing to specific observational thresholds. The fact that it currently acts as a no-op filter is useful: it confirms that the corridor machinery is correctly wired before any aggressive external cuts are introduced.
