# Stage 2 obstruction: static FRW kernel robustness (v1)

Status.  
This memo records a minimal robustness check on the static FRW pre-data kernel used in the obstruction program. It is diagnostic-only and downstream of the Phase 4 FRW masks and Stage 2 FRW belt; no Phase 0–5 contracts, promotion gates, or numerical pipelines are changed.

Inputs.  
The analysis is based on the helper tables

- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_static_frw_kernel_v1.csv`
- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_static_frw_kernel_families_v1.csv`

constructed from the Phase 4 FRW masks:

- `phase4_F1_frw_data_probe_mask.csv`
- `phase4_F1_frw_viability_mask.csv`
- `phase4_F1_frw_lcdm_probe_mask.csv`
- `phase4_F1_frw_shape_probe_mask.csv`.

Pre-data kernel.  
The static pre-data kernel is defined by

- `in_pre_data_kernel = 1`, which in this snapshot is equivalent to `frw_viable = 1` with always-true sanity checks (`has_matter_era = 1`, `smooth_H2 = 1`) inherited from Phase 4.

On the current 2048-point θ grid the helper reports

- `ALL_GRID`: 2048 points (100% of the grid),
- `PRE_DATA_KERNEL`: 1016 points (≈ 49.6% of the grid, by construction 100% of the kernel).

Intersections with existing FRW families.  
Using the same helper, we record how the kernel sits inside the existing FRW families:

- `LCDM_LIKE`: 63 points
  - ≈ 3.1% of the grid,
  - ≈ 6.2% of the kernel (`KERNEL_AND_LCDM` has the same size).
- `TOY_CORRIDOR`: 1186 points
  - ≈ 57.9% of the grid,
  - ≈ 1.17 × the kernel size (the toy corridor extends beyond the kernel).
- `KERNEL_AND_TOY`: 154 points
  - ≈ 7.5% of the grid,
  - ≈ 15.2% of the kernel.
- `LCDM_AND_TOY`: 40 points
  - ≈ 2.0% of the grid,
  - ≈ 3.9% of the kernel.
- `KERNEL_AND_LCDM_AND_TOY`: 40 points
  - ≈ 2.0% of the grid,
  - ≈ 3.9% of the kernel
  - (triple intersection kernel ∩ LCDM-like ∩ toy corridor).
- `SHAPE_AND_VIABLE`: 154 points
  - matches `KERNEL_AND_TOY` in this snapshot.
- `SHAPE_AND_LCDM`: 40 points
  - matches `LCDM_AND_TOY`.

Robustness reading.  

- The pre-data kernel is not a single thin sliver: it contains 1016 out of 2048 θ points and retains \`O(10^2)\` points even when simultaneously intersected with independent corridor-style flags (`lcdm_like`, `in_toy_corridor`, shape-selected subsets).
- The non-empty triple intersection (`KERNEL_AND_LCDM_AND_TOY` with 40 points) shows that there is a region of θ that:
  - passes the current FRW viability gate,
  - is marked LCDM-like by the dedicated mask,
  - and lies inside the toy FRW corridor / shape-selected region.
- At the same time, the toy corridor is strictly larger than the kernel (1186 vs 1016 points), confirming that the kernel is acting as a non-trivial gate rather than being defined by the toy corridor itself.

From the obstruction-program perspective, this constitutes a minimal robustness poke: the kernel survives intersection with several independent Stage 2 FRW families in a way that leaves non-empty, non-negligible subsets. It does not demonstrate optimality or uniqueness, but it shows that the current pre-data kernel is not an artefact of a single mask.

Non-claims and future work.  

- No new thresholds or external corridors are introduced here; all families are inherited from existing Stage 2 FRW machinery.
- These numbers are specific to the current Phase 4 snapshot and may change under future refinements to FRW masks or data probes.
- Future obstruction rungs can:
  - compare this kernel to stricter or looser derived kernels,
  - study how candidate θ values behave under external-style corridors or host-style constraints,
  - and test whether any putative special θ survives such tightening.
