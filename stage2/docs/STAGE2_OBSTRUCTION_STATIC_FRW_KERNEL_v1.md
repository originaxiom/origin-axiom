# Stage 2 obstruction static FRW kernel (v1)

Status.  
This memo documents a small Stage 2 helper script for the obstruction program. It does not change any Phase contracts or Stage 2 core belts; it only packages existing FRW masks into a single table for static θ analysis.

Definition.  
The script `stage2/obstruction_tests/src/build_static_frw_kernel_v1.py` reads the Phase 4 FRW mask tables

- `phase4/outputs/tables/phase4_F1_frw_data_probe_mask.csv`
- `phase4/outputs/tables/phase4_F1_frw_viability_mask.csv`
- `phase4/outputs/tables/phase4_F1_frw_lcdm_probe_mask.csv`
- `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`

joins them on θ, and writes

- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_static_frw_kernel_v1.csv`.

Each row of the output table carries

- FRW scalars: `theta`, `E_vac`, `omega_lambda`, `age_Gyr`,
- basic masks: `has_matter_era`, `has_late_accel`, `smooth_H2`, `frw_viable`, `data_ok`,
- corridor flags: `lcdm_like`, `in_toy_corridor`, `shape_and_viable`, `shape_and_lcdm`,
- and a derived flag `in_pre_data_kernel` recording whether the point lies in the current pre-data FRW kernel.

In this first version the pre-data kernel is defined as the set of θ points with `frw_viable = 1` (the always-true sanity checks are implicitly enforced by the inputs). The kernel should be read as a convenience packaging of existing Stage 2 masks for static obstruction-program analysis, not as a new data-driven corridor or a promoted result.

Usage.  
From the repo root:

- run `python stage2/obstruction_tests/src/build_static_frw_kernel_v1.py` to regenerate the kernel table,
- then inspect the resulting CSV under `stage2/obstruction_tests/outputs/tables/` in any preferred analysis environment.

All interpretation of this kernel is governed by the existing Stage 2 FRW and data-probe docs and by the obstruction-program memos. This helper table is purely diagnostic and downstream-only.
