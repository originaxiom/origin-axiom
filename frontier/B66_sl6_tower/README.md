# B66 -- The SL(6) numerical fixed-line tower (35 dimensions)

**Status:** the `n=6` row of the metallic trace-map tower, computed numerically
at high precision. Extends the inverse-word method (B61, SL(5)) to the 35-dim
`SL(6,C)` character variety. Standalone trace-map mathematics; no physics, no
Origin-core claim. **Numerical, not a symbolic proof.**

## What it settles

The campaign's open multiplicity question -- does the odd-`k` degree-3 factor
multiplicity follow `max(n-d,1)` (=> **3** at `n=6`) or saturate at **2**?
**SL(6) is the smallest `n` that distinguishes them.**

```text
|k|=3 multiplicity (char(M^3)+char(-M^3)) = 2      ->  max(n-d,1)=3 REFUTED
theta-split sectors  9 odd-k + 6 even-k + 5 parity = 35   CONFIRMED (exact)
```

The `|k|=3` quadratics resolve cleanly (all four roots `+-4.236, -+0.236` on the
catalog); there is no clean third factor. See `FINDINGS.md` for the full spectrum,
the 26/35 resolved profile, and the 9 gauge-corrupted modes.

## Method

1. **Coordinates.** `SL6_WORDS` -- a rank-35 set of words in `{A,B,A^-1,B^-1}`
   (length <= 5), QR-pivot-selected at a near-fixed-line representation. Inverse
   words are essential: forward-only sets undercount the rank near the fixed line
   (the B60->B61 lesson).
2. **Ambient fixed-line Jacobian.** `DT(eps) = DX . pinv(Dx)` at `A=exp(eps P)`,
   `B=exp(eps Q)`, with a stable mpmath SVD pinv (dps 60), extrapolated `eps->0`
   over a tight 8-point ladder (`0.006..0.027`, degree-7 Richardson).
3. **Identification.** The 35 multipliers are matched against the Dickson catalog
   `char(M^k)=t^2-L_k t+(-1)^k`, sign sectors `char(-M^k)`, and parity `t-+1`,
   with `L_k=tr(M^k)`, `M=[[1,1],[1,0]]` (Fibonacci, `m=1`). The `|k|=3`
   multiplicity is counted by direct root matching (avoids the
   `char(-M^k)=char(M^-k)` label aliasing).

## The theta-split (exact, fast)

`theta_split(n,h)` / `sector_prediction(n)` give the opposition-involution
(`theta=-w_0`) eigenspace split on the height-`h` root space of `A_{n-1}` (B62/B64).
This fixes the *sector dimensions* exactly:

```text
sector_prediction(6) = (9, 6, 5)  ->  2*(9+6)+5 = 35
  validated: SL(3)=8, SL(4)=15, SL(5)=24
```

It does **not** fix the per-`k` multiplicities -- those are what the numerics
measure, and why the `|k|=3` test needed this run.

## Honest limit

The SL(6) fixed-line rank-loss is severe: 9 of 35 modes are gauge-corrupted (the
B62 mechanism amplified from SL(5)'s 2 modes). The full 15-quadratic profile is
not completely resolved, but the `|k|=3` quadratics have *moderate* roots, resolve
cleanly, and number exactly 2 -- which is the test. A symbolic proof for `n>=5`
needs the ambient `SL(n,C)` Procesi trace ring (B58, open).

## Files

- `probe.py` -- the SL(6) probe: coordinates, mpmath SVD-pinv pipeline, Dickson
  identification, `theta_split`/`sector_prediction`, `factor_profile`. `main()`
  prints the full spectrum, the resolved profile, the gauge modes, and the `|k|=3`
  count (~30 min).
- `FINDINGS.md` -- the result, the full spectrum, the method limit.
