# B54 Findings

> Logged observation, not a claim (`../../GOVERNANCE.md` §5).

## Verdict

```text
PRODUCES-PROOF-MODULE
```

The exchange block-diagonalization of the metallic `SL(3)` fixed-line Jacobian
is not special to the `c=3` representation point: it holds for the entire fixed
line.

## Exact Results

**1. Exchange commutation for all `c`.** With `c` kept symbolic, the `8x8`
fixed-line Jacobian `J(m, c)` commutes with the record-exchange involution `P`
(`x1<->x4, x2<->x5, x3<->x8, x6<->x7`), verified for `m = 1, 2, 3`. The
off-diagonal symmetric/antisymmetric blocks vanish identically in `c`. This
generalizes the B51 result (`c=3` only) to the whole fixed line. The reason is
structural: the trace map is `P`-equivariant and the fixed line is
`P`-invariant.

**2. Twin polynomials at `c=1`.** In the exchange basis at `c=1, m=1`:

```text
symmetric sector  : (t-1)(t+1)(t^2 - t + 1)    Eisenstein, discriminant -3, Phi_6
antisymmetric     : (t-1)(t+1)(t^2 - t - 1)    golden,     discriminant  5, char(M)
```

The Eisenstein and golden quadratics appear simultaneously in the two sectors of
the same Jacobian. Their discriminants `-3` and `5` are the same pair that
factor the figure-eight gluing equation `z^2(z-1)^2 = (z^2-z+1)(z^2-z-1)` (claim
P12, `tests/test_gluing_equation.py`). Recorded as a structural echo.

**3. Cyclotomic sweep (`m=1`).** The symmetric-sector quadratic `t^2 - c t + 1`
runs through:

```text
c = -1 : t^2 + t + 1   = Phi_3
c =  0 : t^2 + 1        = Phi_4
c =  1 : t^2 - t + 1    = Phi_6   (Eisenstein)
c =  2 : t^2 - 2t + 1   = (t-1)^2 (parabolic)
c =  3 : t^2 - 3t + 1   = char(A) (golden, phi^2 / phi^-2)
```

i.e. the symmetric sector sweeps from elliptic (roots on the unit circle) through
the parabolic boundary at `c=2` to the first hyperbolic factorization at `c=3`.

**4. Regression.** At `c=3` the sectors reproduce the B51 factorization
`(t-1)(t+1)(t^2-(m^2+2)t+1)` and `(t^2+mt-1)(t^2-(m^3+3m)t-1)` for `m=1,2,3`.

## Impact On PC12

B54 upgrades PC12's exchange-symmetry block decomposition from a `c=3` statement
to an all-`c` statement, and records the `c=1` twin polynomials and the `m=1`
cyclotomic sweep as exact structural content for the computational note. It
introduces no selector, no physics dictionary, and no new claim. The clean
cyclotomic sweep is `m=1`-specific; the `m`-general facts are the `c=1`
antisymmetric `char(M)` and the `c=3` factorization.
