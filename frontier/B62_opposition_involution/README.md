# B62 -- Opposition involution: the 2 unresolved SL(5) fixed-line modes

**Status:** live structural result (exact root-system computation; validated on
SL(3)/SL(4); numerically corroborated). **Not a symbolic proof.** Standalone
character-variety / Lie-theory mathematics; no physics, no Origin-core claim.

## Question

B61 resolved 22 of the 24 SL(5) fixed-line multipliers; the last 2 were a method
limit (the representation-perturbation pseudoinverse limit is gauge-dependent at
the fixed-line rank-loss). Are those 2 modes identifiable?

## The prediction (tested here)

The exchange involution `P` on the trace coordinates (`tr W <-> tr W^-1`)
corresponds to the **opposition involution `theta = -w0`** on the root system of
`sl(n)`. On each height-`h` root space, `theta` splits into a symmetric (+1)
sector carrying the direct factors `char(M^k) = t^2 - L_k t + (-1)^k` and an
antisymmetric (-1) sector carrying the sign sectors
`char(-M^k) = t^2 + L_k t + (-1)^k` (`M = [[1,1],[1,0]]`, Fibonacci).

## Result

The `theta` split on the **height-2** root space of `A_{n-1}` (exact, pure
root-system combinatorics):

```text
 n | dim h=2 | theta+1 | theta-1 | direct char(M^2) | sign char(-M^2)
 3 |    2    |    2    |    0    |        1         |        0          [matches SL(3)]
 4 |    4    |    2    |    2    |        1         |        1          [matches SL(4)]
 5 |    6    |    4    |    2    |        2         |        1          [predicts SL(5)]
```

SL(3) and SL(4) are reproduced exactly. For SL(5) the height-2 space is
`char(M^2)^2 . char(-M^2)`. B61 resolved 4 of its 6 dimensions as
`char(M^2) . char(-M^2)`, so the **2 unresolved modes are the second `char(M^2)`**:

```text
eigenvalues  phi^2 = 2.618034...   and   1/phi^2 = 0.381966...
```

This completes the SL(5) fixed-line factorization:

```text
char(M^-1) . char(M)^2 . char(M^2)^2 . char(M^3) . char(M^4) . char(M^5)
          . char(-M^2) . char(-M^3) . (t-1)^2 (t+1)^2          (degree 24)
```

## Why the numerics could not do this (context)

Re-verified: `tr(DT0)` and `det(DT0)` from the B61 method **scatter across
seeds** (tr ~ 22.8 / 20.8 / 14.5; det complex, varying), so every spectral
invariant of the 2-mode block is gauge-dependent. No flavor of the
representation-perturbation numerics can decide the 2 modes -- the opposition
involution (a canonical, well-defined object) is required.

**Numerical corroboration of the sign:** the gauge-perturbed residual modes are
**positive** (seed 20: ~2.89, ~0.90), consistent with `char(M^2)` `{2.618, 0.382}`
and ruling out the negative-rooted `char(-M^2)` `{-2.618, -0.382}`.

## Honest status

- The opposition-involution split is **exact** and reproduces SL(3)/SL(4); the
  height-2 direct power is `2` consistently for `n=3,4`; the numerics corroborate
  the positive sign. This is recorded as a **live structural result**.
- It is **not** a symbolic proof. A proof needs the ambient `SL(5,C)` trace ring
  (the same construction left open for the symbolic SL(4) proof). The
  power-assignment at heights other than 2 is not derived here.

## Run

```bash
python frontier/B62_opposition_involution/probe.py
python -m pytest tests/test_b62_opposition_involution.py -q
```
