# B60 -- SL(n) Tower: cross-n structure map (n=3,4) + SL(5) barrier

## Question

Extend B59's SL(4) computation: build the corrected cross-n structure map by the
same (validated) method, and push to SL(5).

## Status

```text
FRONTIER EVIDENCE (numerical, method-validated for n=3,4)
PC12 SUPPORT
NO CLAIM PROMOTION
```

## Run

```bash
python frontier/B60_sln_tower/probe.py
```

## Result -- corrected cross-n structure map

The fixed-line factorization, computed by the B59 extrapolation method
(validated on SL(3) ground truth, `max match 0.0000`):

```text
n   char(M^k) powers      sign sectors   parity block        (degree check)
3   {-1, 2, 3}            none           (t-1)(t+1)   [2]    2 + 3*2 = 8  = n^2-1
4   {-1, 1, 2, 3, 4}      char(-M^2)     (t-1)^2(t+1) [3]    3 + 5*2 + 2 = 15 = n^2-1
5   {-1,1,1,2,3,4,5}      -M^2, -M^3     (t-1)^2(t+1)^2 [4]  [B61: 22 of 24 resolved]
```

The `n=5` row is resolved by **B61** (`../B61_sl5_high_precision/`); the "barrier"
below was a rank-deficient word set, not conditioning.

Trend `n=3 -> 4`: the `char(M^k)` powers **climb and densify** (`{-1,2,3}` ->
`{-1,1,2,3,4}`), a **sign sector** appears (`char(-M^2)`, none at n=3), and the
**parity block grows** (degree 2 -> 3). This empirical map is the actual
structure; it is **not** the naive `(n^2-1-parity)/2` all-`char(M^k)` count,
which B59 refuted.

## The SL(5) barrier

SL(5) (24-dim) does **not** resolve at double precision. The trace-coordinate
differential `Dx` has condition number `~1e11` at the relevant scale (the
probe reports `~3.5e10` at `eps=0.1`; it worsens as `eps->0` like `eps^-2`), so
the extrapolated Jacobian is dominated by numerical noise. Verified attempts that
did **not** crack it: double-precision finite-difference and exact-differential
extrapolation, coordinate row-balancing, and `mpmath` normal-equations pinv
(which squares the conditioning to `~1e22` and goes numerically singular).

A clean SL(5) factorization needs **either** a stable high-precision solver
(SVD-based pseudo-inverse at high working precision with multi-`eps`
extrapolation) **or** the symbolic ambient SL(5,C) trace ring. Neither is built
here; the barrier is documented as a reproducible conditioning fact.

> **Resolved by B61.** The stable SVD pinv at dps=60 shows the `~1e11` was the
> double-precision *rounding floor* hiding a **rank-23** word set (forward-only
> letters). Inverse-word coordinates restore rank 24 at `cond ~ 1e4`, and **22 of
> 24** multipliers resolve to the catalog (the `n=5` row). The remaining 2 are a
> method limit (fixed-line rank-loss). See `../B61_sl5_high_precision/`.

## Verdict

Cross-n structure map established for **n=3,4** (numerical, method-validated) --
the corrected tower replacing the refuted conjecture. **SL(5) unresolved**
(conditioning barrier), with the required next step identified. Standalone
trace-map math; no claim promoted.
