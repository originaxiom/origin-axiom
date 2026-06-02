# B60 Findings

> Logged observation, not a claim (`../../GOVERNANCE.md` §5).

## Verdict

```text
PRODUCES-RESULT (numerical) for n=3,4 cross-n map; SL(5) UNRESOLVED (conditioning barrier).
```

## The corrected cross-n tower (n=3,4)

```text
n   char(M^k) powers      sign sectors   parity block          degree
3   {-1, 2, 3}            none           (t-1)(t+1)             2     (2 + 3*2 = 8)
4   {-1, 1, 2, 3, 4}      char(-M^2)     (t-1)^2 (t+1)          3     (3 + 5*2 + 2 = 15)
5   {-1,1,1,2,3,4,5}      -M^2, -M^3     (t-1)^2 (t+1)^2        4     [B61, 22 of 24]
```

The `n=5` row is from **B61** (22 of 24 multipliers; see below).

Three trends from `n=3` to `n=4`:

1. **Powers climb and densify:** `{-1, 2, 3}` becomes `{-1, 1, 2, 3, 4}` (gains
   `M`, `M^4`). Higher rank reaches higher `M`-powers and fills in the gap at `1`.
2. **A sign sector appears:** `char(-M^2) = t^2+3t+1` (eigenvalues `-phi^2,
   -phi^-2`) is present at `n=4`, absent at `n=3`.
3. **The parity block grows:** `(t-1)(t+1)` (degree 2) becomes `(t-1)^2(t+1)`
   (degree 3).

This is the empirical replacement for the refuted `(n^2-1-parity)/2`
all-`char(M^k)` conjecture (B59). It is computed by the B59 extrapolation method,
validated on SL(3) ground truth to `max match 0.0000`; SL(4) reproduces B59 to
`max match 0.0101`.

## The SL(5) barrier (honest negative)

SL(5) (24-dim) does not resolve at double precision: `cond(Dx) ~ 1e11`. Five
attempts failed to extract a clean spectrum: double-precision finite-difference
extrapolation (`max|imag| ~ 18`), coordinate row-balancing, exact analytic
differentials at double precision (`max|imag| ~ 2-3`), `mpmath` single-`eps`
normal-equations pinv (not the `eps->0` limit), and `mpmath` multi-`eps`
extrapolation (normal-equations squared the conditioning to `~1e22` and the
inverse went numerically singular at `dps=45`).

The required next step is a **stable high-precision solver** -- SVD-based
pseudo-inverse at high working precision with multi-`eps` extrapolation -- or the
**symbolic ambient SL(5,C) trace ring**. Recorded so the barrier is not
re-encountered blindly.

> **Update (B61):** the SVD pinv at dps=60 shows this "`cond ~ 1e11` barrier" was
> a **misdiagnosis** -- B60's forward-only word set is **rank 23** (its 24th
> singular value is the dps zero-floor, mis-read in double precision as
> `cond ~ 1e11`). With inverse-word coordinates (`A,B,A^{-1},B^{-1}`, rank 24,
> `cond ~ 1e4`), **22 of 24** SL(5) multipliers resolve to the catalog (the
> `n=5` row above). The last 2 are a method limit (fixed-line rank-loss makes the
> pinv `eps->0` limit gauge-dependent). See `../B61_sl5_high_precision/`.

## Status

Numerical, method-validated for `n=3,4`; SL(5) unresolved. The cross-n map is an
empirical structure, not a symbolic theorem. No physics, no Origin-core claim;
proven ledger unchanged.
