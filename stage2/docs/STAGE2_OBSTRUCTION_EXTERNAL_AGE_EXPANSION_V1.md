# Stage 2 obstruction program – external age and expansion corridors (v1)

## 1. Scope and role

This memo documents the helper `apply_external_age_expansion_corridors_v1.py` in the Stage 2 obstruction program. The goal is to define simple external-style bands in age and expansion space, plus a basic structure proxy, and to see how they carve the pre-data FRW kernel built from the Phase 4 masks. These corridors are deliberately toy-level and internal. They are not data-fitted constraints and they do not alter any Phase 0–5 contracts or Stage 2 promotion gates.

The helper is part of the O2.x block of the obstruction program, where we systematically test whether the static FRW kernel remains non-empty under increasingly structured external-style filters before we attempt any sharper verdicts in O3.x.

## 2. Inputs and outputs

Code:

- `stage2/obstruction_tests/src/apply_external_age_expansion_corridors_v1.py`

Inputs:

- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_static_frw_kernel_v1.csv`

This input table encodes the 2048-point θ grid with Phase 4 FRW scalars and masks, together with a Boolean flag for the pre-data FRW kernel (points that satisfy the viability and sanity checks used in the obstruction program).

Outputs:

- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_age_expansion_corridors_v1.csv`
- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_age_expansion_summary_v1.csv`

The augmented table adds a set of Boolean flags for the external-style corridors. The summary table reports, for each corridor family, the number of points and fractions relative to the full grid and to the pre-data kernel.

## 3. Definition of the corridors

In the current snapshot `apply_external_age_expansion_corridors_v1.py` defines the following families on the 2048-point θ grid.

Age-based bands (using the Phase 4 scalar `age_Gyr`):

- `AGE_BROAD_V1`: a broad age band intended to represent “old enough to host mature structure” in a very forgiving way. This band keeps most of the pre-data kernel.
- `AGE_TIGHT_V1`: a narrower age band targeting a late-time universe of order fourteen billion years old. This band is closer to what one would expect from a ΛCDM-like host age, but is still a toy choice, not a data-fitted constraint.

Expansion bands (using the Phase 4 vacuum sector scalars):

- `EXPANSION_BROAD_V1`: a broad box in the space of FRW quantities (`E_vac`, `omega_lambda`) that retains a modest fraction of the kernel.
- `EXPANSION_TIGHT_V1`: a tighter box that picks out a smaller subset whose late-time expansion history is closer to the Phase 4 LCDM-like region.

Structure proxies:

- `STRUCT_PROXY_BASIC_V1`: a basic structure-friendly proxy that mirrors `AGE_BROAD_V1` in the current snapshot. It is designed to keep essentially all points that are not obviously too young.
- `STRUCT_PROXY_TIGHT_V1`: a tighter proxy that coincides with `EXPANSION_TIGHT_V1` in the current snapshot and is meant to represent a minimal joint age+expansion condition that could plausibly host familiar structure.

All bands and proxies are defined by explicit numerical thresholds inside the script, derived from the current FRW scalar distributions. They are presented as internal design choices, not as observationally calibrated constraints.

## 4. Current numerical snapshot

For the current run the summary file reports:

- Grid and kernel:
  - `ALL_GRID`: 2048 points (fraction of grid = 1.0), with 1016 points in the pre-data kernel (fraction of kernel = 1.0).
  - `PRE_DATA_KERNEL`: 1016 points (fraction of grid ≈ 0.496), by construction.

- Age bands:
  - `AGE_BROAD_V1`: 933 points on the grid (fraction ≈ 0.456), with 931 in the kernel (fraction of kernel ≈ 0.916).
  - `AGE_TIGHT_V1`: 126 points on the grid (fraction ≈ 0.062), with 126 in the kernel (fraction of kernel ≈ 0.124).

- Expansion bands:
  - `EXPANSION_BROAD_V1`: 94 points on the grid (fraction ≈ 0.046), all 94 in the kernel (fraction of kernel ≈ 0.093).
  - `EXPANSION_TIGHT_V1`: 51 points on the grid (fraction ≈ 0.025), all 51 in the kernel (fraction of kernel ≈ 0.050).

- Structure proxies:
  - `STRUCT_PROXY_BASIC_V1`: 931 points on the grid (fraction ≈ 0.455), with 931 in the kernel (fraction of kernel ≈ 0.916).
  - `STRUCT_PROXY_TIGHT_V1`: 51 points on the grid (fraction ≈ 0.025), with 51 in the kernel (fraction of kernel ≈ 0.050).

In words: the broad age and structure proxies leave most of the kernel intact, while the tight expansion and structure bands pick out a roughly five-percent subset of the kernel. These numbers are specific to the current Phase 4 snapshot and may change as the FRW pipeline is refined.

## 5. Role in the obstruction program

Within the obstruction program this helper provides a small catalogue of external-style cuts that can be combined with:

- the internal LCDM-like and toy FRW corridors,
- the external-style age-only corridors (including the v2 band),
- and the Phase 3 amplitudes attached to the kernel,

to form diagnostic families of the form:

- “kernel and external age v2”,
- “kernel and tight age/expansion/structure band”,
- “kernel ∧ LCDM-like ∧ toy FRW corridor ∧ external age v2”,

and so on. These families are then summarised both in FRW space and in mechanism-amplitude space by `analyze_kernel_mech_vs_external_corridors_v1.py`.

The purpose is to test whether the static FRW kernel and any small “sweet subsets” remain non-empty under increasingly structured external-style demands, and whether any such subsets exhibit pathological or finely tuned behaviour in the Phase 3 amplitudes.

## 6. Non-claims and future work

Non-claims:

- `apply_external_age_expansion_corridors_v1.py` defines toy external-style corridors only. The thresholds are not fitted to data and do not represent precise observational constraints.
- No Phase 4 FRW masks or Phase 3 mechanisms are altered by these helpers. All outputs remain strictly in Stage 2.
- No statement is made that any surviving region is physically preferred or that the tight bands define a canonical host corridor. They are test corridors for the obstruction program, nothing more.

Future work:

- Introduce age and expansion bands whose thresholds are derived from explicit external arguments (for example observational age bounds or simple effective w0–wa boxes) rather than from internal distributions.
- Introduce additional structure-friendly proxies and combine them with the existing age and expansion bands.
- Update the Stage 2 obstruction verdict once a small, well-motivated set of such sharpened external corridors has been applied and their impact on the kernel and any sweet subsets has been summarised.
