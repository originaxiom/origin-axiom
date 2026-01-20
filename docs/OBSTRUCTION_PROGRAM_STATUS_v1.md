# Obstruction program status (v1, static FRW kernel)

Status.  
This memo records the status of the obstruction program as implemented on branch `obstruction-program-v1` in January 2026. It is an interpretive overlay on top of the locked Phase 0–5 stack and the existing Stage 2 belts. No Phase contracts, promotion gates, or numerical pipelines are changed here; all obstruction statements remain diagnostic-only and downstream of the canonical program.

## 1. Inputs and spine

The obstruction program in this branch stands on:

- Phase 0–5 stack:
  - Phase 0 governance and contracts (`phase0/`),
  - Phase 1 toy ensembles (`phase1/`),
  - Phase 2 mode-sum and bounded FRW viability (`phase2/`),
  - Phase 3 mechanism module (`phase3/`),
  - Phase 4 FRW toy diagnostics and masks (`phase4/`),
  - Phase 5 interface and sanity layer (`phase5/`).
- Stage 2 diagnostic belts:
  - FRW corridor analysis (`stage2/frw_corridor_analysis/`),
  - mech/measure analysis (`stage2/mech_measure_analysis/`),
  - joint mech–FRW analysis (`stage2/joint_mech_frw_analysis/`),
  - FRW data-probe audit (`stage2/frw_data_probe_analysis/`),
  - θ★–FRW alignment diagnostic,
  - doc and archive audit belt (`stage2/doc_repo_audit/`).

The obstruction program uses these as its diagnostic spine, with design-level guidance recorded in:

- `docs/OBSTRUCTION_EMPIRICAL_PROGRAM_v1.md` – empirical scope and standards for obstruction tests, with emphasis on static θ corridors, pre-data FRW kernels, and Phase 0 governance.
- `stage2/docs/STAGE2_OBSTRUCTION_TESTING_SPINE_v1.md` – how the Stage 2 belts (FRW corridors, mech/measure, joint mech–FRW, FRW data probes, θ★ diagnostic) function collectively as an obstruction-testing spine.
- `stage2/docs/STAGE2_EXTERNAL_CONSTRAINTS_DESIGN_v1.md` – design-only memo for future external-style constraints (late-time expansion, early-structure-friendly, and host-consistency filters), not yet implemented in code.
- `docs/STAGEII_COSMO_HOSTS_DESIGN_v1.md` – design notes for Stage II cosmology hosts and host-style questions about corridor survival and kernel structure.

## 2. Constructs added in obstruction-program-v1

On top of the existing stack, this branch adds three concrete constructs.

### 2.1 Static FRW pre-data kernel

Helper script:

- `stage2/obstruction_tests/src/build_static_frw_kernel_v1.py`

Input FRW masks:

- `phase4/outputs/tables/phase4_F1_frw_data_probe_mask.csv`
- `phase4/outputs/tables/phase4_F1_frw_viability_mask.csv`
- `phase4/outputs/tables/phase4_F1_frw_lcdm_probe_mask.csv`
- `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`

Output helper table:

- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_static_frw_kernel_v1.csv`

The helper joins the FRW masks on θ and records, for each grid point:

- FRW scalars: `theta`, `E_vac`, `omega_lambda`, `age_Gyr`,
- FRW masks: `has_matter_era`, `has_late_accel`, `smooth_H2`, `frw_viable`, `data_ok`,
- corridor flags: `lcdm_like`, `in_toy_corridor`, `shape_and_viable`, `shape_and_lcdm`,
- derived flag: `in_pre_data_kernel`, currently defined by `frw_viable = 1` with always-true sanity checks inherited from Phase 4.

On the current snapshot:

- grid size: 2048 θ points,
- pre-data kernel size: 1016 points with `in_pre_data_kernel = 1` (~49.6% of the grid).

The construct is documented in:

- `stage2/docs/STAGE2_OBSTRUCTION_STATIC_FRW_KERNEL_v1.md`.

### 2.2 Kernel family decomposition

Helper script:

- `stage2/obstruction_tests/src/analyze_static_frw_kernel_families_v1.py`

Input:

- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_static_frw_kernel_v1.csv`

Output family table:

- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_static_frw_kernel_families_v1.csv`

For each θ-family it records:

- `family_name`,
- `n_points`,
- `frac_of_grid`,
- `frac_of_kernel` (where applicable),
- `note`.

Families include:

- `ALL_GRID` – all 2048 θ points,
- `PRE_DATA_KERNEL` – `in_pre_data_kernel = 1` (1016 points),
- `LCDM_LIKE` – LCDM-like set from the FRW LCDM probe mask,
- `TOY_CORRIDOR` – toy FRW corridor from Phase 4,
- `KERNEL_AND_LCDM` – pre-data kernel ∩ LCDM-like,
- `KERNEL_AND_TOY` – pre-data kernel ∩ toy corridor,
- `LCDM_AND_TOY` – LCDM-like ∩ toy corridor,
- `KERNEL_AND_LCDM_AND_TOY` – triple intersection of kernel, LCDM-like, and toy corridor,
- `SHAPE_AND_VIABLE` – shape-selected and FRW-viable points,
- `SHAPE_AND_LCDM` – shape-selected and LCDM-like points.

This is documented in:

- `stage2/docs/STAGE2_OBSTRUCTION_STATIC_FRW_KERNEL_FAMILIES_v1.md`.

### 2.3 Minimal robustness note

Interpretive memo:

- `stage2/docs/STAGE2_OBSTRUCTION_STATIC_FRW_KERNEL_ROBUSTNESS_v1.md`

This memo reads the helper counts as a minimal robustness poke on the static kernel. In the current snapshot:

- Grid and kernel:
  - `ALL_GRID`: 2048 points,
  - `PRE_DATA_KERNEL`: 1016 points (~49.6% of grid).
- Basic families:
  - `LCDM_LIKE`: 63 points (~3.1% of grid, ~6.2% of kernel),
  - `TOY_CORRIDOR`: 1186 points (~57.9% of grid, ~1.17 × kernel size).
- Intersections:
  - `KERNEL_AND_TOY`: 154 points (~7.5% of grid, ~15.2% of kernel),
  - `LCDM_AND_TOY`: 40 points (~2.0% of grid, ~3.9% of kernel),
  - `KERNEL_AND_LCDM_AND_TOY`: 40 points (~2.0% of grid, ~3.9% of kernel),
  - `SHAPE_AND_VIABLE`: 154 points (matches `KERNEL_AND_TOY`),
  - `SHAPE_AND_LCDM`: 40 points (matches `LCDM_AND_TOY`).

From an obstruction perspective this shows:

- the pre-data kernel is non-trivial and retains O(10^2) points under multiple independent intersections,
- the toy corridor is strictly larger than the kernel (the kernel is not defined by the corridor),
- there is a non-empty “sweet spot” region (40 points) where FRW viability, LCDM-likeness, and toy-corridor membership coincide.

## 3. Verdict and roadmap

Verdict for obstruction-program-v1 (static, internal):

- The program now has a concrete static FRW kernel and a quantified corridor structure on which to test obstruction-flavoured ideas.
- The pre-data kernel is neither empty nor full; it sits in a regime where non-trivial intersections with independent FRW families leave O(10^2) points, including a 40-point triple intersection region.
- All constructs are downstream of locked Phase 3/4 outputs and Stage 2 FRW machinery; no new physics assumptions, external data, or θ-selection criteria have been introduced.

Non-claims:

- No external-style corridors (late-time expansion boxes, early-age bounds, or host metrics) are implemented in code yet; they exist only as design notes.
- No θ value, special or otherwise, is singled out or promoted by obstruction-program-v1.
- No change is made to Phase 0–5 claims, the Stage 2 promotion map, or the interpretation of existing FRW masks.

Forward roadmap (beyond v1):

- External-style corridors:
  - encode simple external-style filters (for example effective expansion boxes or early-age-inspired cuts) as separate Stage 2 helpers over the static kernel,
  - treat them as design experiments first, promoted only via explicit Phase 0–style gates.
- Host-style questions:
  - use the static FRW kernel and its families as inputs to Stage II host diagnostics, where host scenarios and obstruction questions are formulated at the level of “which θ-regions survive which host patterns”.
- Dynamic or higher-resolution probes:
  - if warranted by static results, explore whether any putative θ regions identified in the static kernel survive under refined FRW pipelines, host constraints, or more realistic data probes.

This memo freezes obstruction-program-v1 as a static, internal, Stage 2–compatible overlay. Future obstruction work should build on these constructs via new, tightly scoped rungs and explicit gates rather than by retroactively changing the v1 status.
