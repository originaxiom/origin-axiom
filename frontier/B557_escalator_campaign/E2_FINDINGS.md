# B557 E2 — Rule uniqueness: the escalator is FORCED at rung 1, CHOSEN above

The honesty crux of the escalator hypothesis (B556): is (C,D)=(M,M²) forced
or a choice? Computed exactly.

## Setup
By B517, coupling blocks must intertwine the base (CM=MC, DM=MD) ⟹ C=p(M),
D=q(M) are polynomials in M. The coupled top eigenvalue is λ + √(p(λ)q(λ)).
Field-doubling (a genuine new field / irreducible tower) requires √(p(λ)q(λ))
∉ ℚ(λ), i.e. **p+q ODD** (√(λ^k) is irrational over ℚ(λ) iff k odd).

## Results (rung 0 → 1, base F)
| coupling (C,D) | rung-1 charpoly deg | irreducible | Perron | = M₄? |
|---|---|---|---|---|
| (M, M²) | 4 | yes | 3.6762 | **YES** |
| (M², M) | 4 | yes | 3.6762 | **YES** (C↔D swap) |
| (I, M) | 4 | yes | 2.8901 | no (a DIFFERENT doubler) |
| (M, I) | 4 | yes | 2.8901 | no |
| (I, M²),(M,M),(M²,M²) | 4 | **no** (reducible) | — | no |

- **(F, F²) uniquely reproduces M₄** (up to the C↔D swap) — B517's uniqueness,
  confirmed. Other couplings give different matrices, not the object.
- **Multiple field-doubling functors exist:** (M,M²) [p+q=3] and (I,M) [p+q=1]
  both double and give irreducible Pisot towers — with DIFFERENT λ-laws
  (λ+λ√λ vs λ+√λ). So (M,M²) is NOT the only doubler.

## Verdict
The escalator (M,M²) is **FORCED at rung 1** (it alone gives M₄, B517) and is
the **unique SELF-SIMILAR iteration** — the same (X,X²) rule at every rung,
literally the a→a·a² origin gesture. But at rung ≥ 2 it is a **CHOICE**: other
intertwining couplings (e.g. (I,M)) also generate irreducible field-doubling
Pisot towers. **The "canonical but chosen" boundary of B556 HOLDS** — the
falsifier ("(M,M²) is the only doubler ⟹ forced") did NOT fire. The tower's
self-similarity is what singles out (M,M²), not a forcing theorem. Honest and
intact. Locks: tests/test_b557_e2.py.
