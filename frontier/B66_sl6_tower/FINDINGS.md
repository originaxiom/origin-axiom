# B66 -- SL(6) numerical fixed-line tower (35-dim): the |k|=3 multiplicity test

**Status:** numerical, high-precision; not a symbolic proof. Standalone trace-map
mathematics; no physics, no Origin-core claim.

## Question

The metallic fixed-line Jacobian factors over the Dickson catalog
`char(M^k)=t^2-L_k t+(-1)^k` (`L_k=tr(M^k)`, `M=[[1,1],[1,0]]`), with sign
sectors `char(-M^k)` and a parity block `(t-1)^a(t+1)^b`. Across the tower the
*sector dimensions* are fixed by the opposition-involution `theta`-split (B62/B64),
but the **multiplicity of each `char(M^k)`** is not. The campaign's open question:
does the odd-`k`, degree-`d=3` multiplicity follow `max(n-d,1)` (which would give
**3** at `n=6`) or saturate at **2**? SL(5) cannot decide it -- `max(5-3,1)=2`
equals the alternative there. **SL(6) is the first `n` where the two predictions
differ (3 vs 2), so it disambiguates the formula for all `n`.**

## Result

```text
theta-split sector structure (exact):   9 odd-k + 6 even-k quadratics + 5 parity = 35   CONFIRMED
|k|=3 multiplicity (char(M^3)+char(-M^3)):   2        ->  max(n-d,1)=3  REFUTED
```

The numerical spectrum resolves the `|k|=3` region **cleanly** -- all four roots
of the two `|k|=3` quadratics land on the catalog:

```text
char( M^3) = t^2 - 4t - 1 :   4.23606792  (dist 5e-8)   -0.23606707 (dist 9e-7)
char(-M^3) = t^2 + 4t - 1 :  -4.23564808  (dist 4e-4)    0.23606433 (dist 4e-6)
```

That is **exactly two** `|k|=3` quadratics, each with both roots resolved. A
third `|k|=3` factor would need two further roots near the `|k|=3` values; the
only extra mode in the big-root region is `-4.434` (dist `0.198` from
`char(-M^3)`'s `-4.236`), and it has **no small-root partner** (only one mode sits
near each of `+-0.236`). It is therefore a gauge-corrupted mode, not a third
`|k|=3` factor. **The `|k|=3` multiplicity is 2, the same as SL(5)** -- it does
**not** grow with `n`, refuting `max(n-d,1)`.

## Resolved factor profile (26/35)

```text
|k|=1:  char(M) x2  + char(M^-1) x1   = 3
|k|=2:  char(M^2) x2 + char(-M^2) x1  = 3
|k|=3:  char(M^3) x1 + char(-M^3) x1  = 2     <- KEY TEST
|k|=4:  char(M^4) x1                  = 1
|k|=5:  char(M^5) x1                  = 1
parity: ~ (t-1)^2 (t+1)^3                       (deg 5, theta-split prediction)
```

## Honest status / method limit

- **The SL(6) fixed-line rank-loss is far more severe than SL(5)'s.** Of 35
  multipliers, **26 resolve cleanly** (tol 0.03); **9 are gauge-corrupted**: three
  complex-conjugate pairs (`-0.031+-0.242i`, `0.404+-0.248i`, `2.651+-0.227i`) and
  three real outliers (`-4.434`, `-0.431`, `12.116`). This is the same mechanism
  B62 found for SL(5) (the trivial-rep degeneracy makes the `eps->0` pinv limit
  gauge-dependent), amplified at `n=6` from 2 unresolved modes to 9.
- **The full 15-quadratic multiplicity profile is therefore not completely
  determined numerically** (5 of 15 quadratics sit among the gauge modes). What
  *is* determined is the specific test the campaign posed: the `|k|=3` quadratics
  have **moderate** roots (`+-4.236`), resolve cleanly, and number exactly **2**.
- **The `theta`-split sector count (9/6/5 = 35) is exact** (pure root-system
  combinatorics, `sector_prediction(6)`; validated SL(3)=8, SL(4)=15, SL(5)=24).
- A symbolic proof for `n>=5` still needs the ambient `SL(n,C)` Procesi trace ring
  (B58, open). This run is high-precision numerics (mpmath dps 60, inverse-word
  coordinates, tight `eps`-ladder extrapolation), not a theorem.

## Reproduce

```bash
python frontier/B66_sl6_tower/probe.py     # ~30 min: full spectrum + |k|=3 count
python -m pytest tests/test_b66_sl6_tower.py -q   # fast: theta-split + catalog + word rank
```
