# Stage 2 obstruction: external corridors status snapshot (v1)

Status: Stage 2 diagnostic overview (obstruction-program-v1 branch). This memo summarises the current set of external-style corridors and helpers used in the obstruction program and records what they do to the static FRW pre-data kernel and to the existing sweet subsets. It does not change any Phase 0–5 contracts, FRW masks, or Stage 2 promotion gates.

## 1. Context and inputs

All constructions in this memo are downstream of the Phase 4 FRW toy stack and its masks:

- `phase4_F1_frw_data_probe_mask.csv`
- `phase4_F1_frw_viability_mask.csv`
- `phase4_F1_frw_lcdm_probe_mask.csv`
- `phase4_F1_frw_shape_probe_mask.csv`

The common starting point is the static FRW kernel:

- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_static_frw_kernel_v1.csv` (2048-point θ-grid).

Pre-data kernel definition (reused everywhere):

- `has_matter_era == 1`
- `smooth_H2 == 1`
- `frw_viable == 1`

In the current snapshot:

- full grid: 2048 θ-points
- pre-data kernel: 1016 points (≈ 49.6% of the grid)

All external-style corridors and helpers in this memo act as *additional filters* on this static kernel.

## 2. Internal/toy late-time corridors in vacuum space

### 2.1 Toy late-time corridor from LCDM box

Helper script and docs:

- `stage2/obstruction_tests/src/build_toy_lt_corridor_from_lcdm_box_v1.py`
- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_toy_lt_corridor_from_lcdm_box_v1.csv`
- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_toy_lt_corridor_from_lcdm_box_summary_v1.csv`
- `stage2/docs/STAGE2_OBSTRUCTION_TOY_LT_CORRIDOR_FROM_LCDM_v1.md`

Definition (internal, FRW-space only):

- Derives a late-time corridor box in the (`E_vac`, `omega_lambda`) plane from the current LCDM-like band.
- Marks a flag `toy_lt_corridor_from_lcdm` (naming internal to the helper) for points in the static kernel that lie in that box.

Key features (from the summary and docs):

- LCDM-like band size: 63 points in the grid.
- The toy late-time box is chosen so that the LCDM-like island sits well inside it.
- There is a 40-point “sweet region” where:
  - the point lies in the pre-data kernel,
  - lies in the LCDM-like band,
  - lies in the original toy FRW corridor,
  - lies inside the derived LCDM-based late-time box.

Interpretation:

- This helper reshapes the vacuum sector around the LCDM-like island without killing the kernel or the 40-point sweet subset.
- It remains an *internal* late-time corridor: no direct external data is used, just the current FRW toy/LCDM masks.

### 2.2 External late-time corridor helper (v1)

Helper script and docs:

- `stage2/obstruction_tests/src/apply_external_lt_corridor_v1.py`
- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_lt_corridor_v1.csv`
- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_lt_corridor_summary_v1.csv`
- `stage2/docs/STAGE2_OBSTRUCTION_EXTERNAL_LT_CORRIDOR_V1.md`

Definition:

- Uses the same LCDM-derived (`E_vac`, `omega_lambda`) box as the toy corridor helper, but treats it explicitly as an “external-style” late-time corridor flag (`external_lt_corridor_v1`).
- Summarises families such as:
  - `KERNEL_AND_EXTERNAL_LT_V1`
  - `LCDM_AND_EXTERNAL_LT_V1`
  - `TOY_CORRIDOR_AND_EXTERNAL_LT_V1`
  - `KERNEL_LCDM_TOY_AND_EXTERNAL_LT_V1`

Key features:

- The corridor is tightly aligned with the LCDM-like island and preserves the same 40-point sweet subset:
  - `KERNEL_LCDM_TOY_AND_EXTERNAL_LT_V1` contains the same 40 points already identified by the internal LCDM-based box.
- No additional cuts in age are imposed in this helper; it is purely a vacuum-sector late-time corridor.

Interpretation:

- This is a structured placeholder for a late-time external-style constraint that mirrors the present LCDM-like behaviour of the stack.
- It confirms that the static kernel plus toy corridors admit a meaningful late-time-friendly subset without declaring it physically preferred.

## 3. External age corridors

### 3.1 External age corridor v2 (non-trivial band)

Helper script and docs:

- `stage2/obstruction_tests/src/apply_external_age_corridor_v2.py`
- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_age_corridor_v2.csv`
- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_age_corridor_summary_v2.csv`
- `stage2/docs/STAGE2_OBSTRUCTION_EXTERNAL_AGE_CORRIDOR_V2.md`

Definition:

- Defines a toy external-style age corridor:
  - `12.0 <= age_Gyr <= 15.0` (v2 band),
  - flagging points with `external_age_corridor_v2 == True`.
- Summarises families:
  - `EXTERNAL_AGE_CORRIDOR_V2`
  - `KERNEL_AND_EXTERNAL_AGE_V2`
  - `LCDM_AND_EXTERNAL_AGE_V2`
  - `TOY_CORRIDOR_AND_EXTERNAL_AGE_V2`
  - `KERNEL_LCDM_TOY_AND_EXTERNAL_AGE_V2` (sweet subset under the age band).

Key numbers (from the v2 summary):

- `EXTERNAL_AGE_CORRIDOR_V2`: 358 grid points (≈ 17.5%), of which 356 lie in the kernel (≈ 35.0% of kernel).
- `KERNEL_AND_EXTERNAL_AGE_V2`: 356 points (≈ 35.0% of kernel).
- `KERNEL_LCDM_TOY_AND_EXTERNAL_AGE_V2`: 40 points, i.e. the same 40-point sweet subset survives the age band v2.

Interpretation:

- A non-trivial age band can be imposed on the kernel without killing:
  - the overall kernel (≈ one third of kernel survives), or
  - the 40-point sweet subset (all 40 survive this toy age corridor).
- The age band is still toy-level and not fitted to data, but it already acts as a meaningful obstruction test: the sweet subset is not obviously ruled out by basic age considerations.

## 4. External age + expansion corridors (v1)

Helper script and docs:

- `stage2/obstruction_tests/src/apply_external_age_expansion_corridors_v1.py`
- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_age_expansion_corridors_v1.csv`
- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_age_expansion_summary_v1.csv`
- `stage2/docs/STAGE2_OBSTRUCTION_EXTERNAL_AGE_EXPANSION_CORRIDORS_V1.md`

Definitions (flags added on top of the static kernel):

- `age_broad_v1`: `11.5 <= age_Gyr <= 15.0`.
- `age_tight_v1`: `13.0 <= age_Gyr <= 14.2`.
- `expansion_broad_v1`:
  - `0.55 <= omega_lambda <= 0.85`, and
  - `E_vac` between the 5th and 95th percentiles of `E_vac` over the kernel.
- `expansion_tight_v1`:
  - `0.62 <= omega_lambda <= 0.78`, and
  - `E_vac` between the 10th and 90th percentiles of `E_vac` over the kernel.
- Structure proxies:
  - `struct_proxy_basic_v1` = kernel ∧ `age_broad_v1`.
  - `struct_proxy_tight_v1` = kernel ∧ `age_tight_v1` ∧ `expansion_tight_v1`.

Summary (from `stage2_obstruction_external_age_expansion_summary_v1.csv`):

Relative to the 2048-point grid and 1016-point kernel:

- `AGE_BROAD_V1`:
  - 933 points (≈ 45.6% of grid),
  - 931 in kernel (≈ 91.6% of kernel).
- `AGE_TIGHT_V1`:
  - 126 points (≈ 6.2% of grid),
  - 126 in kernel (≈ 12.4% of kernel).
- `EXPANSION_BROAD_V1`:
  - 94 points (≈ 4.6% of grid),
  - 94 in kernel (≈ 9.3% of kernel).
- `EXPANSION_TIGHT_V1`:
  - 51 points (≈ 2.5% of grid),
  - 51 in kernel (≈ 5.0% of kernel).
- `STRUCT_PROXY_BASIC_V1`:
  - 931 points (≈ 45.5% of grid),
  - 931 in kernel (≈ 91.6% of kernel).
- `STRUCT_PROXY_TIGHT_V1`:
  - 51 points (≈ 2.5% of grid),
  - 51 in kernel (≈ 5.0% of kernel).

Interpretation:

- Broad age + expansion cuts keep most of the kernel (structure-friendly, “late-time compatible” universes are plentiful in the toy stack).
- Tight age + expansion cuts select a modest but nontrivial subset (~5% of the kernel), suggesting that the kernel is not artificially fine-tuned: even relatively strict late-time-friendly filters do not empty it.
- These bands are still toy external-style corridors (based on simple windows and percentiles), but they are now strong enough to be meaningful obstruction probes.

## 5. Qualitative obstruction status (v1, external-corridor layer)

At this stage, combining the results from:

- the static FRW kernel and toy FRW corridor,
- the LCDM-like band and internal LCDM-based late-time corridor,
- the external late-time helper,
- the external age corridor v2,
- the age+expansion helpers,

we have:

- A robust pre-data kernel (~50% of the θ-grid) that survives all internal sanity checks.
- A 40-point sweet subset that:
  - lies in the kernel,
  - lies in the toy FRW corridor,
  - lies in the LCDM-like band,
  - survives the toy and external late-time corridors,
  - survives the non-trivial external age corridor v2.
- Sharpened age+expansion corridors that:
  - keep most of the kernel under broad bands,
  - still leave ~5% of the kernel under tight late-time-friendly bands.

Obstruction verdict at this layer (v1):

- On the *current* toy FRW + mechanism stack, and under the *current* choice of toy/external corridors, there is no sign that the θ-corridors and sweet subsets are trivial or catastrophically obstructed:
  - the kernel is large and internally consistent,
  - non-trivial subsets survive increasingly sharpened corridors.
- At the same time, no special θ* selection has emerged from these corridors alone; the sweet subset is non-empty but not yet a unique or obviously preferred θ region.

This memo is therefore a **status snapshot**, not a final obstruction verdict. It records that:

- the obstruction program has moved from “only internal FRW corridors” to “a first family of external-style age and expansion corridors,”
- these sharpened corridors do not kill the kernel or the current sweet subset,
- but they have not yet produced an obstruction or a compelling selection of θ*.

## 6. Non-claims and forward plan

Non-claims:

- None of the age or expansion bands here are fitted to real data or formal observational bounds; they are toy external-style corridors chosen for structure and interpretability.
- No Phase 4 FRW masks, Phase 5 interfaces, or Stage 2 promotion gates were changed by this rung; all new flags live entirely inside Stage 2.
- No claim is made that any surviving subset (including the 40-point sweet set) is physically realised; they are candidate regions for further tests, not “the universe”.

Forward plan (obstruction layer):

- Combine the external-style corridors with θ*-alignment diagnostics and the mechanism scalars to check whether:
  - θ-corridors and sweet subsets remain non-trivial under sharpened filters, and
  - any robust, θ*-sensitive structures emerge.
- Design a small set of more realistic external corridors (age + expansion + simple structure proxies) guided by external literature and fit them into the obstruction vocabulary and Phase 0 gates.
- Once a stable family of such corridors exists, update `STAGE2_MASTER_VERDICT_v1.md` (or a later version) with a refined obstruction verdict that integrates both the internal corridors and these external-style tests.
