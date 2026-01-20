# Stage 2 obstruction – external age corridor (v2)

Status. This memo documents the first non-trivial age-based external-style corridor helper in the obstruction program on branch `obstruction-program-v1`. It acts on the static FRW kernel table and defines a boolean flag `external_age_corridor_v2` together with a small family summary. The construction is Stage 2–internal and does not alter any Phase 0–5 contracts, FRW masks, or promotion gates.

## 1. Inputs and construction

Inputs.

- Static FRW kernel table:
  - `stage2/obstruction_tests/outputs/tables/stage2_obstruction_static_frw_kernel_v1.csv`
  - Columns used here include:
    - `theta`, `E_vac`, `omega_lambda`, `age_Gyr`,
    - FRW sanity and viability flags,
    - `lcdm_like`,
    - `in_toy_corridor`,
    - `in_pre_data_kernel`.

Helper script and outputs.

- Script:
  - `stage2/obstruction_tests/src/apply_external_age_corridor_v2.py`
- Outputs:
  - `stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_age_corridor_v2.csv`:
    - copy of the static kernel table with an added column `external_age_corridor_v2` (0/1).
  - `stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_age_corridor_summary_v2.csv`:
    - summary over families:
      - `ALL_GRID`,
      - `PRE_DATA_KERNEL`,
      - `EXTERNAL_AGE_CORRIDOR_V2`,
      - `KERNEL_AND_EXTERNAL_AGE_V2`,
      - `LCDM_AND_EXTERNAL_AGE_V2`,
      - `TOY_CORRIDOR_AND_EXTERNAL_AGE_V2`,
      - `KERNEL_LCDM_TOY_AND_EXTERNAL_AGE_V2`,
    - with counts and fractions relative to the full grid and to the pre-data kernel.

Construction (v2 age band).

- The script loads the static kernel table and identifies:
  - the pre-data kernel (`in_pre_data_kernel = 1`),
  - the LCDM-like subset (`lcdm_like = 1` if present),
  - the FRW toy corridor (`in_toy_corridor = 1` if present).
- It then imposes a simple external-style age band on the FRW scalar `age_Gyr`:
  - an age corridor `[12.0, 15.0]` Gyr is selected as a toy late-time band,
  - `external_age_corridor_v2 = 1` exactly on points where `age_Gyr` lies in this interval and `0` otherwise.
- The choice `[12.0, 15.0]` Gyr is deliberately narrow compared to the trivial `[10.0, 20.0]` band used in the v1 machinery test:
  - it is wide enough to be clearly compatible with a late-time universe of order fourteen billion years old,
  - but narrow enough to have a realistic chance of cutting away parts of the pre-data kernel and LCDM-like band.

Interpretation.

- In v2 the age corridor is meant as a genuinely constraining external-style filter:
  - it is not tuned to the existing sweet subset or to any particular θ value,
  - it is narrow enough that whether the pre-data kernel and sweet subset survive is a substantive question rather than a foregone conclusion.
- The family summary table shows, for this snapshot:
  - how much of the pre-data kernel lies inside the age corridor,
  - how it overlaps with the LCDM-like island and the FRW toy corridor,
  - whether the 40-point triple-intersection region remains non-empty.

## 2. Relation to previous age and late-time helpers

Previous helpers in the obstruction belt include:

- The age corridor v1 helper:
  - implemented a very broad band `[10.0, 20.0]` Gyr,
  - served mainly as a machinery test and was effectively non-constraining.
- The late-time corridor helpers in the vacuum sector:
  - the toy late-time corridor from the LCDM box,
  - the external late-time corridor v1 that mirrors the LCDM bounding box in the \((E_{\text{vac}}, \omega_\Lambda)\) plane.

The v2 age corridor complements these by cutting directly on the FRW scalar `age_Gyr` rather than only on vacuum parameters:

- it provides an age-first view on late-time acceptability,
- it can be compared with the vacuum-space corridors to see whether they agree on which parts of the kernel look late-time friendly,
- it is explicitly external-style: motivated by the scale of the late-time universe rather than by internal structure of the FRW masks alone.

## 3. Non-claims and future work

Non-claims.

- `external_age_corridor_v2` is a toy external-style band; it is not claimed to be an optimal or data-fitted age constraint.
- No Phase 4 FRW masks or Stage 2 promotion gates are changed by this helper.
- No statement is made that any surviving θ region is physically preferred; the corridor is used only to test whether the static kernel and the 40-point sweet subset are robust under non-trivial age cuts.

Future work.

- Later external-style rungs may:
  - adjust the age band to match specific observational bounds or redshift-dependent age constraints,
  - combine age cuts with additional background or structure-friendly proxies,
  - and re-evaluate whether the pre-data kernel and sweet subset survive under these sharpened filters.
- The obstruction verdict will only be revised once a small set of such sharpened external-style corridors has been applied and their impact on the kernel and sweet subset has been summarised.
