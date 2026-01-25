# Stage 2 – Planck-like FRW corridor helper (v1)

This memo records a simple, external-style FRW corridor used as a **diagnostic helper** in the obstruction program. It does not introduce any new Phase-level claims or modify existing FRW masks; it provides a more realistic late-time band against which to test the Stage 2 obstruction stack.

## 1. Definition

We start from the static FRW kernel table

- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_static_frw_kernel_v1.csv`,

which contains, on a common θ grid,

- background scalars `E_vac`, `omega_lambda`, `age_Gyr`,
- FRW viability flags (including the pre-data kernel flag),
- LCDM-like and toy-corridor flags from existing Stage 2 helpers.

On this table we define a **Planck-like external corridor** by placing a rectangular band in the `(age_Gyr, omega_lambda)` plane, inspired by Planck ΛCDM constraints:

- `age_Gyr` in `[13.75, 13.85]` Gyr (a narrow band around a ~13.8 Gyr universe),
- `omega_lambda` in `[0.68, 0.70]` (a narrow band around Ω_Λ ≈ 0.69).

We then define a boolean flag

- `in_planck_like_corridor_v1`,

which is `True` for rows whose `age_Gyr` and `omega_lambda` both lie inside this box, and `False` otherwise.

## 2. Implementation and outputs

The helper is implemented by

- `stage2/obstruction_tests/src/apply_planck_like_frw_corridor_v1.py`, which
  - reads the static FRW kernel table,
  - attaches the `in_planck_like_corridor_v1` flag,
  - and writes:

    - an augmented table  
      `stage2/obstruction_tests/outputs/tables/stage2_obstruction_planck_like_corridor_v1.csv`,
    - and a summary table  
      `stage2/obstruction_tests/outputs/tables/stage2_obstruction_planck_like_corridor_summary_v1.csv`.

The summary table reports, for several diagnostic families,

- `ALL_GRID`,
- `PRE_DATA_KERNEL`,
- `PLANCK_LIKE_V1`,
- `KERNEL_AND_PLANCK_LIKE_V1`,
- `LCDM_AND_PLANCK_LIKE_V1`,
- `TOY_CORRIDOR_AND_PLANCK_LIKE_V1`,
- `KERNEL_LCDM_TOY_AND_PLANCK_LIKE_V1`,

their sizes and fractions relative to the full θ grid and to the pre-data kernel.

This places the Planck-like corridor on the same footing as our earlier late-time and age corridors and toy LT boxes.

## 3. Role in the obstruction program

Within the obstruction program this helper plays a **purely diagnostic** role:

- It provides a first, sharpened external-style late-time corridor tied to a realistic age and dark-energy density band, rather than to broad toy intervals.
- It allows us to ask whether:
  - the pre-data kernel remains comfortably populated,
  - the 40-point “sweet subset” remains non-empty,
  - and how those sets intersect with a Planck-like `(age_Gyr, omega_lambda)` box.

In later rungs we will overlay this Planck-like corridor with:

- the Phase 3 mechanism amplitudes (via the `kernel_with_mech` table),
- the existing non-cancellation floor diagnostics,
- and any dynamic θ or stochastic-drive toy models that approximate the obstructed-cancellation picture.

At this stage **no** Phase 0–5 claims, FRW masks, or Stage 2 promotion gates are modified. `in_planck_like_corridor_v1` is a helper flag for obstruction diagnostics, not a promoted cosmological constraint or a new empirical claim.
