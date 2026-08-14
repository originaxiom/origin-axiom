# B800 — B685's Habiro integrality leg, recomputed in-sandbox: PARTIAL CONFIRMATION

cc banking seat, 2026-07-29. B799 registered this as the batch's highest-value remaining
recompute: B685 banked *"the Habiro object is integral away from 3 — the (q−1)¹⁰⁰ denominator is
3¹⁴⁶"* by **re-reading GSWZ eq. 2**, not by computing it. This computes it. Mathematics only;
nothing to `CLAIMS.md`.

## The object, built from first principles rather than transcribed

GSWZ's symmetrised series is `Φ(h)Φ(−h)`, with `Φ` the perturbative series of the figure-eight's
state integral at the geometric saddle. Constructed here:

```
V(u)  = Li₂(e^u) − Li₂(e^−u)          V′(u) = −log(2 − e^u − e^−u)
saddle: (1−w)(1−1/w) = 1  ⟺  w² − w + 1 = 0   ⟹  w₀ = (1+√−3)/2   [verified: w₀²−w₀+1 = 0]
```

**The 1-loop invariant is computed, not assumed: `V″(u₀) = w₀ − 1/w₀ = √−3`.** Every higher
derivative is an *integer* multiple of 1 or √−3 — `V⁽³⁾…V⁽⁸⁾ = −2, −2√−3, 10, 22√−3, −182, −602√−3`
— so the whole expansion lives in ℚ(√−3). **This is the mechanism behind "pure being"**, and it is
now derived in-sandbox rather than read.

## What the computation shows

Exact Feynman expansion over ℚ(√−3) (Fraction arithmetic, no floats), symmetrised to h¹⁴:

| n | v₃(den) | non-3 part |
|---|---|---|
| 2 | 3 | 1 |
| 4 | 5 | 5 |
| 6 | 9 | 5 |
| 8 | 12 | 5²·7 |
| 10 | 14 | 5²·7·11 |
| 12 | 17 | 5³·7·11 |
| 14 | 20 | 5²·7²·11·13 |

**Structural checks that passed:** the symmetrised series is **rational** (the √−3 cancels, as the
symmetrisation requires) and **even** — every odd coefficient vanishes.

**The 3-adic content corroborates B685.** `v₃ ≈ 1.428·n`, extrapolating to **3¹⁴³ at n = 100**
against B685's read of **3¹⁴⁶** — the same law, within 2 % on a linear fit from n ≥ 4.

**The "only 3" clause is NOT reproduced under this normalisation.** Denominators also carry
2, 5, 7, 11, 13. But **every non-3 prime is ≤ n+1**, which is the signature of the Gaussian moments
`(2m−1)!!` and the `1/k!`, `1/r!` factors of the Feynman expansion — a property of *expanding in h*,
not of the object. So the non-3 part is a **normalisation artifact**; the 3-part is the arithmetic.

## Verdict — PARTIAL, and the flag stays

- **CONFIRMED in-sandbox:** the mechanism (√−3 as the 1-loop invariant, integer ℚ(√−3) data) and
  the **3-adic growth law**, which lands in the right place for 3¹⁴⁶.
- **NOT reproduced:** the exact "integral away from 3" statement, because pinning the normalisation
  requires GSWZ's eq. 2 — the very source B685 read and this arc set out **not** to re-read.
- **Therefore B685's `fact_computed: false` stays false.** This substantially strengthens the
  claim's foundation without discharging it. Calling it discharged would repeat B685's own error
  one level up: substituting a *nearly* matching computation for the stated one.

## Residual

Reproduce GSWZ's normalisation (their variable and prefactor convention) and re-run; if the
non-3 primes vanish under it, the claim is discharged exactly. That is a bounded, in-sandbox task
and it is **not** `NEEDS-SPECIALIST`.

`habiro.py` (sympy, readable) · `fast_expansion.py` (exact ℚ(√−3), to h¹⁴) · `output.txt`
