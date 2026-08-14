# B839 — B685's non-3 denominator is an EXPANSION artifact: `(2n)!` clears it exactly

cc banking seat, 2026-07-30. **Prereg `0bbdc9f5fcf96cb2`, sealed before computing.** Gate 5
absolute — arithmetic only, nothing to `CLAIMS.md`.

## Verdict: ARTIFACT CONFIRMED

**`(2n)!` absorbs the entire non-3 denominator at every computed order**, and **no other member of
the sealed family does**:

| n | non-3 denominator | factorisation |
|---|---|---|
| 2 | 4 | 2² |
| 4 | 320 | 2⁶·5 |
| 6 | 2 560 | 2⁹·5 |
| 8 | 2 867 200 | 2¹⁴·5²·7 |
| 10 | 252 313 600 | 2¹⁷·5²·7·11 |
| 12 | 20 185 088 000 | 2²¹·5³·7·11 |
| 14 | 2 938 948 812 800 | 2²⁴·5²·7²·11·13 |

| normalisation | clears every n? |
|---|---|
| **`(2n)!`** | **YES** |
| `n!`, `(n+1)!`, `n!!`, `(n+1)!!`, `(2n−1)!!`, `(n/2)!` | no — fail at **n = 2** |
| `2ⁿ·(n/2)!`, `4ⁿ·(n/2)!` | no — fail at **n = 4** |

**The criterion could fail and eight of nine family members did fail** — six at the first non-trivial
order. This is not a normalisation fitted to the data; it is the one member of a fixed family that
survives.

> **B800's diagnosis is verified: the non-3 content belongs to the h-expansion, not to the object.**

## My mechanism prediction was wrong, and precisely how

The prereg said I expected a **double factorial**, reasoning that repeated small odd primes
(5²·7²·11·13) are double-factorial shape, and required that a different winner be reported as a
mechanism error even with the verdict right.

**The winner is `(2n)!` — a single factorial.** And the identity

```
(2n)! = 2ⁿ · n! · (2n−1)!!          (verified n = 1..7)
```

shows exactly what I got wrong: **the double factorial is one of three factors and is insufficient
alone.** `(2n−1)!!` fails at n = 2 because it carries no 2-part, and the denominators are
overwhelmingly 2-adic (2²⁴ by n = 14). **I named the odd-prime factor and missed that the 2-part
dominates** — visible in B800's own table, which printed `v2` beside `v3` all along.

## What is discharged, and what is emphatically not

**Discharged — the ARITHMETIC.** That the Habiro series' denominator is a pure power of 3 under a
natural expansion normalisation is now an **in-repo, re-runnable computation**, built from B800's
own verified components (its `phihat` and `K`, symmetrised exactly as its `main()` does — the banked
artifact was not modified).

**NOT discharged — the CONVENTION.** That **GSWZ's eq. (2) uses this normalisation** remains
**cited, not read.** B800 declined to re-read the paper and so does this arc.

> **`B685.fact_computed` stays FALSE** — but its residue is now one literature line rather than a
> whole computation. **Calling it discharged would repeat B685's original error one level up:
> substituting a nearly-matching computation for the stated one.**

**What would flip it:** read GSWZ eq. (2) and confirm the prefactor convention is `(2n)!` or
equivalent. **One line, and the claim is fully computed.**

## Also corroborated

B800's 3-adic law is untouched and stands: `v₃ ≈ 1.428·n` → **3¹⁴³ at n = 100** against B685's
**3¹⁴⁶** — the same law within 2 %.

`tests/test_b839_residue.py`
