# Stage 2 obstruction: external age + expansion corridors (v1)

Status: Stage 2 diagnostic helper (obstruction-program-v1 branch). This memo documents a first set of sharpened external-style corridors that combine age and expansion filters on top of the static FRW pre-data kernel.

## 1. Scope and inputs

This rung operates entirely within Stage 2. It does not modify any Phase 0–5 contracts, Phase 4 FRW masks, or Stage 2 promotion gates.

Inputs:

- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_static_frw_kernel_v1.csv`  
  (2048-point θ-grid with FRW scalars and masks, plus the pre-data kernel flag used throughout the obstruction stack).

The pre-data kernel is defined as:

- `has_matter_era == 1`,
- `smooth_H2 == 1`,
- `frw_viable == 1`.

In the current snapshot this gives:

- full grid: 2048 points,
- pre-data kernel: 1016 points (about 49.6% of the grid).

Outputs:

- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_age_expansion_corridors_v1.csv`  
  (kernel table augmented with external-style age and expansion flags),
- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_age_expansion_summary_v1.csv`  
  (family counts and fractions for the new flags).

Helper script:

- `stage2/obstruction_tests/src/apply_external_age_expansion_corridors_v1.py`

## 2. Corridor definitions

On top of the static kernel we introduce six boolean flags:

- `age_broad_v1`  
  True where `11.5 <= age_Gyr <= 15.0`. This is a broad, late-time compatible age band, wide enough to contain most of the kernel.

- `age_tight_v1`  
  True where `13.0 <= age_Gyr <= 14.2`. This is a narrower band around a ~14 Gyr universe, meant as a more constraining age corridor.

- `expansion_broad_v1`  
  True where:
  - `0.55 <= omega_lambda <= 0.85`, and
  - `E_vac` lies between the 5th and 95th percentiles of `E_vac` over the pre-data kernel.  
  This selects a broad, non-extreme expansion regime within the kernel.

- `expansion_tight_v1`  
  True where:
  - `0.62 <= omega_lambda <= 0.78`, and
  - `E_vac` lies between the 10th and 90th percentiles of `E_vac` over the pre-data kernel.  
  This is a tighter expansion band meant to act as a more realistic late-time cut.

From these, we define two structure-friendly proxies:

- `struct_proxy_basic_v1`  
  True where the point lies in the pre-data kernel and satisfies `age_broad_v1`. This is a basic proxy for “late-time friendly FRW histories with a matter era and smooth expansion.”

- `struct_proxy_tight_v1`  
  True where the point lies in the pre-data kernel and simultaneously satisfies:
  - `age_tight_v1`, and
  - `expansion_tight_v1`.  
  This is a more stringent proxy for universes with reasonably tuned age and vacuum expansion within the existing toy FRW stack.

## 3. Summary of family sizes

The summary table `stage2_obstruction_external_age_expansion_summary_v1.csv` reports, for each family, the total count and its overlap with the pre-data kernel. In the current snapshot:

- `ALL_GRID`  
  - `n_points = 2048`  
  - `frac_of_grid = 1.0`  
  - `n_points_in_kernel = 1016`  
  - `frac_of_kernel = 1.0`

- `PRE_DATA_KERNEL`  
  - `n_points = 1016`  
  - `frac_of_grid ≈ 0.4961`  
  - `n_points_in_kernel = 1016`  
  - `frac_of_kernel = 1.0`

- `AGE_BROAD_V1`  
  - `n_points = 933`  
  - `frac_of_grid ≈ 0.4556`  
  - `n_points_in_kernel = 931`  
  - `frac_of_kernel ≈ 0.9163`

- `AGE_TIGHT_V1`  
  - `n_points = 126`  
  - `frac_of_grid ≈ 0.0615`  
  - `n_points_in_kernel = 126`  
  - `frac_of_kernel ≈ 0.1240`

- `EXPANSION_BROAD_V1`  
  - `n_points = 94`  
  - `frac_of_grid ≈ 0.0459`  
  - `n_points_in_kernel = 94`  
  - `frac_of_kernel ≈ 0.0925`

- `EXPANSION_TIGHT_V1`  
  - `n_points = 51`  
  - `frac_of_grid ≈ 0.0249`  
  - `n_points_in_kernel = 51`  
  - `frac_of_kernel ≈ 0.0502`

- `STRUCT_PROXY_BASIC_V1`  
  - `n_points = 931`  
  - `frac_of_grid ≈ 0.4546`  
  - `n_points_in_kernel = 931`  
  - `frac_of_kernel ≈ 0.9163`

- `STRUCT_PROXY_TIGHT_V1`  
  - `n_points = 51`  
  - `frac_of_grid ≈ 0.0249`  
  - `n_points_in_kernel = 51`  
  - `frac_of_kernel ≈ 0.0502`

So:

- the broad age band keeps about 93% of the kernel,
- the tight age band selects about 12% of the kernel,
- the tight expansion band selects about 5% of the kernel,
- the tight structure proxy (`struct_proxy_tight_v1`) also selects about 5% of the kernel, by construction.

## 4. Interpretation

At this rung the sharpened corridors are used purely as diagnostic filters on the existing pre-data FRW kernel:

- The broad age band confirms that most of the kernel corresponds to universes with ages in a reasonable late-time range.
- The tight age band and tight expansion band together demonstrate that the kernel contains a non-trivial but modest subset of points with both age and expansion in a narrow late-time window.
- The structure proxies show that it is straightforward to impose more realistic late-time-friendly cuts without collapsing the kernel to zero.

This sets the stage for combining:

- age-based external corridors (v2),
- late-time expansion corridors,
- and simple structure-friendly proxies

into sharpened obstruction tests on θ-corridors and on any sweet subsets.

## 5. Non-claims and next steps

Non-claims:

- None of the bands in this rung are fitted to real data; they are toy external-style corridors anchored only to the current FRW snapshot and simple percentile cuts.
- No claim is made that points satisfying `struct_proxy_tight_v1` are physically preferred; they are used as a testbed for kernel robustness, not as a selection of the real universe.
- No Phase 4 FRW masks, Phase 5 interfaces, or Stage 2 promotion gates are changed by these helpers.

Next steps:

- Combine the age+expansion helpers with:
  - the external age corridor v2,
  - the external late-time expansion corridor v1,
  - the existing toy corridor and LCDM-like band,
  - and θ★-alignment diagnostics,
  to quantify how much of the sweet subset survives under jointly sharpened filters.
- Use these combined filters to refine the obstruction verdict and to decide what kind of external-style corridors would be worthy candidates for eventual promotion into Phase 4/5 narratives, under separate Phase 0 style gates.
