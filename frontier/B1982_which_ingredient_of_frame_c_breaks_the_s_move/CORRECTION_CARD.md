# B1982 correction card — the S move with the record's own end law (B1667, B1724, B1921)

Written 2026-11-25, before the run, after main read B1921 and B1724 (found by the sweep for B1982's page, before B1982
landed). Data-free. 0 of 19.

## The fault

- **The record's end law under S** (B1667, tested in B1724, derived in B1921): L(−1/τ) = L(τ) + log|τ|. The invariant
  combination is L̃ = L + ½ log Im τ − (γ + log π). B1724 found B1656's frame SL(2, ℤ)-covariant with this law, to
  1.5e-9.
- **B1980's runs did not use it.** The first run read the end's table outside its domain. The correction read
  L(τ_FD) with no shift. On the axis the law gives L(i/y) = L(iy) + log y; the correction gave L(iy).
- **B1982's variants V0, V3, V4 and V6,** which keep the norm, carried the same error.
- **V1, V2 and V5 drop the norm, so they do not use the end.** Their failure stands.

## The run (`verification/s_endlaw.py`)

- **The frame.** Frame C, through B1980's `duality_cov.parts_L`, which reproduces `determinant_law.parts` exactly given
  the end.
- **The end.** At the source height y ≥ 1 it is read on the axis, in the table's domain, as in every run. At the
  partner height 1/y it is L(iy) + log y.
- **The test.** The S move at 1.25 against 0.8, 1.5 against 2/3, and 2.5 against 0.4. B1976's 96 points against all
  899 nonzero points of E[30], under any bijection, with sectors and reading fixed.
- **Also:** B1982's V3 (a₀ dropped) under the same law, and the residue core V1 again as a control (it does not use L).

## Expectations, with priors

| id | expectation | prior |
|---|---|---|
| L1 | frame C passes S with the record's end law (largest d < 1e-8 at all three pairs) | 0.55 |
| L2 | V1 (no norm) fails as before (0.09 and 0.15) | 0.95 |

## What each outcome means

- **L1 holds:** frame C is SL(2, ℤ)-covariant when its end is transformed by its own law, as B1724 found for B1656's
  frame.
  - B1980's "frame C fails S" and B1982's ablations of the norm are then artefacts of main's wrong end law.
  - P-882's premise as worded is wrong, and P-882 is restated: what remains one-hole is how the frame is used (read at
    one cusp, one height, one point), not the frame's form.
  - V1's failure then says that the norm is needed for covariance, which B1921 already implies.
- **L1 fails:** frame C differs from B1656's frame in its covariance, and the breaker is found with the correct law.
- **Nothing is compared with data.**
