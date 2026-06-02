# B61 -- SL(5) fixed-line factorization via a stable high-precision SVD pinv

**Status:** numerical, high-precision; validated on SL(3)/SL(4). **Not a
symbolic proof.** Standalone trace-map mathematics; no physics, no Origin-core
claim.

## What this probe does

B60 generalized the fixed-line factorization method to arbitrary `n` and built
the cross-`n` structure map for `n = 3, 4`, but reported **SL(5) as blocked by a
conditioning wall** (`cond(Dx) ~ 1e11`). B61 re-examines SL(5) at high working
precision (mpmath, default 60 digits) with an SVD-based pseudoinverse, and finds
that the "wall" was a **misdiagnosis**:

- B60's SL(5) coordinate words used only **forward** letters (`A, B` powers and
  `A^i B^j`). At high precision the smallest singular value of `Dx` is the
  dps-floor (`~1e-40`) -- a **true null direction**: that 24-word set is
  **rank 23**, not 24. Double precision mis-read the rounding floor as
  `cond ~ 1e11`.
- Switching to a coordinate set with **inverse letters** (`A, B, A^{-1}, B^{-1}`,
  length `<= 4`) gives a genuine **rank-24** system at `cond ~ 4e3` (`eps=0.2`)
  to `~2e5` (`eps=0.05`). The barrier was a bad coordinate choice, not a
  precision limit.

With the inverse-word coordinates + mpmath SVD-pinv at small `eps`, **22 of the
24 SL(5) multipliers resolve** to the Cayley-Hamilton catalog. The remaining 2
are a characterized **method limit** (see FINDINGS).

## Method (mpmath port of B59/B60)

`DT(eps) = DX . svd_pinv(Dx)` at `A = exp(eps P), B = exp(eps Q)` for a small-eps
ladder, extrapolated entrywise to `eps -> 0`; eigenvalues matched to
`char(M^k) = t^2 - L_k t + (-1)^k`, sign sectors `char(-M^k) = t^2 + L_k t +
(-1)^k`, and parity `(t-1)^a (t+1)^b`.

Key pieces in `probe.py`:

- `svd_pinv` -- stable pinv via SVD of the **tall** orientation
  (`pinv(A) = V^H diag(1/S) U^H`; wide `A` handled by `pinv(A^H)^H`). Loses only
  `~log10(cond)` digits, vs `2 log10(cond)` for normal equations.
- `expm_mp` -- scaling-and-squaring + Taylor matrix exponential.
- `SL5_WORDS` -- the rank-24 inverse-word coordinate set.
- `fixed_line_spectrum`, `_extrap0` (Vandermonde least-squares to `eps=0`),
  `_catalog` / `identify` / `compute_sl5`.

## Results

| n | resolved factorization | powers | sign sectors | parity |
|---|---|---|---|---|
| 3 | `char(M^-1)·char(M^2)·char(M^3)·(t-1)(t+1)` | {-1,2,3} | none | deg 2 |
| 4 | `char(M^-1)·char(M)·char(M^2)·char(M^3)·char(M^4)·char(-M^2)·(t-1)^2(t+1)` | {-1,1,2,3,4} | {-2} | deg 3 |
| 5 | `char(M^-1)·char(M)^2·char(M^2)·char(M^3)·char(M^4)·char(M^5)·char(-M^2)·char(-M^3)·(t-1)^2(t+1)^2` **+ 2 method-limited** | {-1,1,1,2,3,4,5} | {-2,-3} | deg 4 |

Validation (this method, high precision): SL(3) reproduces B55 c=3 to
**~4e-14**; SL(4) reproduces B59 to **~3e-9** (vs B60's `~1e-3` double-precision
floor).

## Run

```bash
python frontier/B61_sl5_high_precision/probe.py   # SL(3)+SL(4) gates, then SL(5) (~2-3 min)
python -m pytest tests/test_b61_sl5.py -q          # fast checks (~10s)
```
