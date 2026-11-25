# B1997 — listening card 13 — the exact identity of λ*, the whole's settled rate at its own prime

Written 2026-11-25, before the run, in the author's /loop "continue the listening line". Data-free. 0 of 19.

## Why

- **B1996:** on the tower of the whole's own prime 3, the unfolding's slowest non-undamped decay settles at λ*/2 per
  move, with λ* = 1.915298…, at mod 81, 243 and 729. λ* is algebraic (an integer matrix's eigenvalue) but unidentified:
  double precision could not support a polynomial search.
- **The question:** what number is it, exactly?

## The check (exact)

- **I1:** W₊ = P_L + P_R on the largest orbit over the common point mod 81 (648 points), as an integer matrix. Its
  characteristic polynomial is computed exactly (FLINT, fmpz_mat.charpoly) and factored over ℤ (fmpz_poly.factor).
- **I2:** the irreducible factor with a root at 1.915298…: its degree, its coefficients, its roots, and the field.
- **I3, consistency:** that factor evaluated at the sparse eigenvalues found at mod 243 and mod 729, to double
  precision.

## Expectations, with priors

| id | expectation | prior |
|---|---|---|
| J1 | λ* is a root of an irreducible integer factor of degree at most 12 | 0.4 |
| J2 | λ*² generates a smaller field (the ± pair), its minimal polynomial of degree at most 6 | 0.4 |
| J3 | none: the factor and its field are the result | — |

## What it means

- **The exact number the whole fixes at its own prime, and the field it lives in.** Whether that field is one already on
  record (ℚ(√5), ℚ(√−3), ℚ(√−7)) or a new one is itself information. Nothing is read as physical, and nothing is
  compared with data.
