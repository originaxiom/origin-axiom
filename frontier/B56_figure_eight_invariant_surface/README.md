# B56 -- Figure-Eight Invariant-Surface Negative Control

## Question

Does the figure-eight knot sit on the self-evidencing invariant surface
`I = 1/4` (the `m=1` value of `I = m^2/4`)? I.e., is the `c=1` symmetric-sector
Eisenstein factor (B55) a genuine figure-eight connection, realized on the
invariant surface?

## Status

```text
FRONTIER NEGATIVE CONTROL
NO CLAIM PROMOTION
```

## Run

```bash
python frontier/B56_figure_eight_invariant_surface/probe.py
```

## What It Checks

```text
diagonal locus cubic w^3-2w^2-2w+1 = (w+1)(w^2-3w+1), roots {-1, phi^2, phi^-2}
diagonal Fricke-Vogt invariant I = 3w^2-2w^3-1 in {4, -17/2 +/- 7 sqrt5/2}
  -> NONE equals 1/4
the two irrational I-values multiply to 11 (plain Q(sqrt5) algebra)
figure-eight ideal tetrahedron shape z^2-z+1 = 0 is COMPLEX (disc -3, Q(sqrt-3)),
  disjoint from the real diagonal locus
```

## Verdict

`DEAD` -- for the holonomy-on-`I=1/4` bridge. The diagonal SL(2,C)
representations never meet `I = 1/4`, and the figure-eight's geometric holonomy
lives in `Q(sqrt-3)` (the complex tetrahedron shape), disjoint from the real
diagonal locus. The `c=1` symmetric Eisenstein factor `t^2-t+1` shares its
polynomial with the figure-eight shape only because `Phi_6` is the simplest
discriminant `-3` cyclotomic -- a **cyclotomic coincidence**, not an
invariant-surface connection.

## Scope Guard

This negative control does **not** affect the separate, real statement that the
`c=1` twins' discriminant pair `(-3, 5)` matches the factors of the figure-eight
**gluing equation** `z^2(z-1)^2 = (z^2-z+1)(z^2-z-1)` (claim P12,
`tests/test_gluing_equation.py`). That gluing-equation echo is kept as a
structural observation; it is only the holonomy / `I=1/4` bridge that is dead.

The self-evidencing / `I=1/4` framing is quarantined in
`paths/E21_self_evidencing_closure/`.
