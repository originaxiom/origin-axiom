# Stage 2 obstruction: kernel with Phase 3 mech amplitudes (v1)

## 1. Purpose and scope

This helper constructs a joined table that carries, for each point on the Phase 4 FRW grid, both the obstruction kernel flags and the Phase 3 mechanism amplitudes. It is the bridge between the pre data FRW kernel and the Phase 3 non cancellation diagnostics, and it is used downstream to ask whether a non cancellation floor can be maintained once external style corridors are applied.

The helper is strictly Stage 2: it reads from Phase 3 and Phase 4 outputs and Stage 2 joint mech FRW tables, and writes its own outputs under stage2. It does not modify any Phase contracts, FRW masks or promotion gates.

## 2. Inputs and outputs

Inputs:

- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_static_frw_kernel_v1.csv` (FRW kernel table with pre data flags on the Phase 4 grid).
- `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv` (joint mech FRW table with FRW scalars, masks and Phase 3 amplitudes on the same θ grid).

Outputs:

- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_kernel_with_mech_v1.csv`

The output table carries, for each θ on the Phase 4 grid:

- the FRW kernel and mask information from the static kernel table, including the pre data kernel flag,
- the Phase 4 scalar background quantities and corridor flags as in the joint mech FRW table,
- the Phase 3 mechanism amplitudes, currently:

  - `mech_baseline_A0`
  - `mech_baseline_A_floor`
  - `mech_baseline_bound`
  - `mech_binding_A0`
  - `mech_binding_A`
  - `mech_binding_bound`

This makes it possible to condition simultaneously on FRW viability, pre data kernel membership, external style corridors and mechanism amplitude thresholds in later obstruction rungs.

## 3. Alignment logic

Both input tables live on the same nominal θ grid with 2048 points. To avoid dropping points because of tiny floating point differences in θ, the helper:

- loads both tables and checks that they have the same number of rows,
- sorts each table by `theta` and compares the sorted θ columns,
- if the maximum absolute difference is below a tolerance (currently 1e-10), treats the two tables as index aligned and copies the mechanism amplitude columns into the kernel table by index,
- otherwise falls back to an inner merge on `theta`.

In the current snapshot the sorted θ grids agree within tolerance, so the helper uses the index aligned path. The resulting table retains all grid points and simply augments the FRW kernel with the Phase 3 amplitudes.

## 4. Role in the obstruction program

Within the obstruction program this helper provides the baseline object for tests of the form:

- start from the pre data FRW kernel,
- apply one or more external style corridors (age bands, late time expansion boxes, simple structure proxies),
- and inspect how the surviving set sits with respect to the mechanism amplitudes, including any attempted non cancellation floor.

It is also the object to use when evaluating special points such as θ⋆ on the same footing as kernel and external corridor membership.

The helper is diagnostic only. It does not define or promote a preferred mechanism measure, and it does not change any Phase 0–5 claims. Any promotion of obstruction flavoured statements into phase papers will require separate, tightly scoped rungs and Phase 0 style gates.
