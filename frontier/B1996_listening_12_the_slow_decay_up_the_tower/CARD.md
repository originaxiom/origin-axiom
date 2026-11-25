# B1996 card — listening 12: the slow decay of the whole's largest orbits up the tower; does it settle to a limit?

Written 2026-11-25, before the run, in the author's /loop "continue the listening line". Data-free. 0 of 19.

## Why

- **B1987:** over the common point, the cube's structures decay at 1/√2 per move at every level, while the large orbits
  that grow along the tangent cone decay more slowly, and differently at each level: 0.707 (mod 27), 0.958 (mod 81),
  0.839 (mod 125), 0.928 (mod 343).
- **B1992:** what the whole selects by finitely many conditions is algebraic. A limit over the whole tower is not such a
  selection. If the slow decay settles to a limit, that would be a number the whole fixes that need not be algebraic.
- **The question:** does the slowest decay on the largest orbits settle as the level grows, at p = 3 and at p = 5?

## The system (nothing chosen)

- **The moves L and R** on the points over the common point on the cusp's leaf, mod 3^k for k = 3, 4, 5 (27, 81, 243)
  and mod 5^k for k = 3, 4 (125, 625).
- **On the largest orbit at each level:**
  - W₊ = P_L + P_R: its largest eigenvalues by modulus, by sparse Arnoldi (scipy);
  - W± = W₊ + W₊ᵀ: its largest eigenvalues (scipy's eigsh).
- **Read:** the largest modulus of W₊ below 2 (the slowest decay, as a ratio to 2), and W±'s gap below its top.
- **Control:** at mod 27, 81 and 125 the run reproduces B1987's values (0.7071, 0.9576, 0.8389).

## Expectations, with priors

| id | expectation | prior |
|---|---|---|
| D1 | the control reproduces B1987 within 1e-3 | 0.95 |
| D2 | along each tower the slowest-decay ratio rises towards 1, so no limit below 1 is seen | 0.55 |
| D3 | none: the table of ratios and gaps by level is the result | — |

## What it means

- **A ratio that settles below 1 across levels** would be a number the whole fixes as a limit, the first candidate value
  not bound by B1992's algebraic constraint.
- **A ratio rising to 1** means the whole forgets ever more slowly as it unfolds outward, with no scale.
- **Either outcome is described, not read as physical.** Nothing is compared with data.
