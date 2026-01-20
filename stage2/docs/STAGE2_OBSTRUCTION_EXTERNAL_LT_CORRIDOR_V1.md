# Stage 2 obstruction – external late-time corridor (v1)

Status.  This memo documents the first external-style late-time expansion corridor helper in the obstruction program on branch `obstruction-program-v1`. It acts on the static FRW kernel table and defines a boolean flag `external_lt_corridor_v1` together with a small family summary. The construction is Stage 2–internal and does not alter any Phase 0–5 contracts, FRW masks, or promotion gates.

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
  - `stage2/obstruction_tests/src/apply_external_lt_corridor_v1.py`
- Outputs:
  - `stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_lt_corridor_v1.csv`:
    - copy of the static kernel table with an added column `external_lt_corridor_v1` (0/1).
  - `stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_lt_corridor_summary_v1.csv`:
    - summary over families:
      - `ALL_GRID`,
      - `PRE_DATA_KERNEL`,
      - `EXTERNAL_LT_CORRIDOR_V1`,
      - `KERNEL_AND_EXTERNAL_LT_V1`,
      - `LCDM_AND_EXTERNAL_LT_V1`,
      - `TOY_CORRIDOR_AND_EXTERNAL_LT_V1`,
      - `KERNEL_LCDM_TOY_AND_EXTERNAL_LT_V1`,
    - with counts and fractions relative to the full grid and to the pre-data kernel.

Construction (v1, LCDM-derived box).

- The script:
  - loads the static kernel table and identifies:
    - the pre-data kernel (`in_pre_data_kernel = 1`),
    - the LCDM-like subset (`lcdm_like = 1`),
  - derives a minimal axis-aligned box in the \((E_{\text{vac}}, \omega_\Lambda)\) plane enclosing the LCDM-like points:
    - `E_vac_min = min(E_vac | lcdm_like = 1)`,
    - `E_vac_max = max(E_vac | lcdm_like = 1)`,
    - `omega_min = min(omega_lambda | lcdm_like = 1)`,
    - `omega_max = max(omega_lambda | lcdm_like = 1)`,
  - defines `external_lt_corridor_v1 = 1` exactly on points inside this box, and `0` otherwise.
- If, in some future snapshot, the LCDM-like band were empty, the script falls back to a trivial box covering the full span of `E_vac` and `omega_lambda` in the static table and emits a warning; in this case the corridor is explicitly marked as degenerate.

Interpretation.

- In v1 the external late-time corridor is deliberately *aligned* with the existing LCDM-like island:
  - it reproduces the same box that already encloses the LCDM-like band in the static FRW kernel,
  - it is meant as a baseline external-style helper that can later be tightened or reshaped by genuine external arguments.
- The family summary table shows, for this snapshot:
  - how much of the pre-data kernel lies inside the corridor,
  - how the corridor overlaps with the LCDM-like band and the FRW toy corridor,
  - whether the 40-point sweet subset (kernel ∧ LCDM-like ∧ toy corridor) is preserved.

## 2. Relation to the toy LCDM box corridor

The obstruction belt already includes an internal **toy late-time corridor** derived from the LCDM box:

- Construction:
  - `stage2/obstruction_tests/src/build_toy_lt_corridor_from_lcdm_box_v1.py`
  - tables:
    - `stage2_obstruction_toy_lt_corridor_from_lcdm_box_v1.csv`,
    - `stage2_obstruction_toy_lt_corridor_from_lcdm_box_summary_v1.csv`.
- That helper interprets the LCDM bounding box as an internal reshaping of the vacuum scalar space and studies its overlap with the pre-data kernel and the toy FRW corridor.

The new external-style helper differs mainly in interpretation and gating:

- `external_lt_corridor_v1` is treated as a **mock external-style corridor**:
  - it uses the same geometric box in \((E_{\text{vac}}, \omega_\Lambda)\) as a baseline,
  - but is explicitly framed as something that future rungs may tighten or perturb based on genuine external considerations.
- Subsequent design rungs will:
  - either adjust the box boundaries away from the exact LCDM-derived limits, or
  - replace them with bands informed by explicit late-time expansion criteria,
  - and record the impact on the pre-data kernel and sweet subset in updated summary tables and verdicts.

## 3. Non-claims and future work

Non-claims.

- `external_lt_corridor_v1` does not represent a fit to data or a realistic constraint on late-time expansion; it is a structured placeholder that mirrors the current LCDM-like island.
- No Phase 4 FRW masks or Stage 2 promotion gates are changed by this helper.
- No claim is made that the surviving θ region is physically preferred; this remains a diagnostic question.

Future work.

- Later external-style rungs will:
  - introduce age and expansion bands with thresholds motivated by external arguments rather than by the internal LCDM-like band,
  - introduce structure-friendly proxies, and
  - study whether the pre-data kernel and the 40-point sweet subset survive under these sharpened corridors.
- The Stage 2 obstruction verdict will be updated only when such sharpened corridors are in place and have been tested; until then, `external_lt_corridor_v1` is part of the internal obstruction toolkit, not a final constraint.
