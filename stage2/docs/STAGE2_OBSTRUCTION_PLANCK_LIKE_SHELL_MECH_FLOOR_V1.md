# Stage 2 / Obstruction: Planck-like FRW shell vs mechanism and floor (v1)

## 1. Purpose and scope

This helper sits in the D-batch of Stage 2 obstruction diagnostics. Its role is
to probe how the pre-data FRW kernel and the Phase 3 mechanism amplitudes behave
in a small neighbourhood of a realistic late-time FRW band inspired by Planck
constraints, without promoting any new empirical claim.

It **does not**:

- change any Phase 0–5 contracts,
- modify the FRW viability masks,
- or define a preferred theta or mechanism-based measure.

It is a Stage 2 diagnostic only.

## 2. Construction

We start from the Planck-like toy box already used in
`STAGE2_OBSTRUCTION_PLANCK_LIKE_CORRIDOR_V1` and
`analyze_planck_like_gap_v1.py`:

- age_Gyr in [13.750, 13.850],
- omega_lambda in [0.680, 0.700].

In the current static FRW kernel this box is empty: no point of the 2048-point
theta grid, and no point of the pre-data kernel or the 40-point sweet subset,
lies inside it.

To get a more informative picture we define a **Planck-near shell (v1)** in
(age_Gyr, omega_lambda) space around the same centre (13.8 Gyr, 0.69), with
modest rectangular tolerances:

- age_Gyr in [13.6, 14.0]  (±0.2 Gyr),
- omega_lambda in [0.60, 0.78] (±0.09).

These numbers are chosen to:

- comfortably include the closest kernel / sweet-subset point identified by the
  gap analysis, and
- span a small but non-trivial neighbourhood in FRW space,

without claiming to be a data-fitted corridor. They are explicitly labelled as a
Stage 2 diagnostic shell, not as a promoted cosmological constraint.

On top of this we reuse the non-cancellation floor threshold introduced earlier
for the binding amplitude:

- floor threshold: mech_binding_A0 >= 0.045.

Given the Stage 2 obstruction kernel with mechanism amplitudes
`stage2_obstruction_kernel_with_mech_v1.csv`, we define:

- `IN_KERNEL`:
    `in_pre_data_kernel == True`.

- `IN_PLANCK_NEAR_SHELL_V1`:
    `IN_KERNEL` and
    `13.6 <= age_Gyr <= 14.0` and
    `0.60 <= omega_lambda <= 0.78`.

- `IN_FLOOR_V1`:
    `IN_KERNEL` and `mech_binding_A0 >= 0.045`.

- `IN_SHELL_AND_FLOOR_V1`:
    `IN_PLANCK_NEAR_SHELL_V1 and IN_FLOOR_V1`.

For each of the families

- `PRE_DATA_KERNEL`,
- `PLANCK_NEAR_SHELL_V1`,
- `PLANCK_NEAR_SHELL_AND_FLOOR_V1`,

we summarise:

- `n_points`, `frac_of_grid`,
- `n_points_in_kernel`, `frac_of_kernel`,
- min / max / mean of the six Phase 3 amplitudes
  (`mech_baseline_A0`, `mech_baseline_A_floor`, `mech_baseline_bound`,
   `mech_binding_A0`, `mech_binding_A`, `mech_binding_bound`).

The results are written to

- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_planck_like_shell_mech_floor_summary_v1.csv`.

## 3. Interpretation (v1)

In this first snapshot the Planck-like toy box itself is empty, and the D3 gap
analysis already shows that the closest kernel / sweet-subset point sits *near*
but outside that band. The shell helper makes this precise by asking:

1. How many kernel points live in a small FRW neighbourhood around a realistic
   Planck-like centre?
2. Among those, how many also satisfy the non-cancellation floor on the binding
   amplitude?
3. Do the mechanism amplitudes in that shell look qualitatively similar to the
   broader kernel, or do they show a different pattern?

This is still a **static** diagnostic: we are not yet evolving theta(t) or the
floor. The outcome feeds directly into the later dynamic-theta and frustrated
floor rungs: if a reasonably populated shell exists and is floor-friendly, it
suggests that an evolving theta(t) + floor mechanism might be able to visit a
Planck-like late-time regime without destroying the obstruction picture. If the
shell is empty or floor-hostile, that will be an explicit obstacle for the
dynamic strand to address.

No stronger statement is made at this stage.
