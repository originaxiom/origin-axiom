# B839 — PREREGISTRATION: is the non-3 denominator an EXPANSION artifact or the object's arithmetic?

cc banking seat, 2026-07-30. **Sealed before computing.** Gate 5 absolute — arithmetic only, no
physical value, nothing to `CLAIMS.md`.

## The residue, inherited exactly

B685 banked *"the Habiro object is integral away from 3 — the (q−1)¹⁰⁰ denominator is 3¹⁴⁶"* on a
**source re-read**, not an in-repo computation, so its `fact_computed` is **false**. B800 recomputed
the series from first principles and got a **partial** confirmation:

- **CONFIRMED:** the mechanism and the 3-adic growth law — `v₃ ≈ 1.428·n`, extrapolating to **3¹⁴³**
  at n = 100 against B685's **3¹⁴⁶**, the same law within 2 %.
- **NOT reproduced:** *"integral away from 3."* Denominators also carry 2, 5, 7, 11, 13.

B800 diagnosed but did not test: *"every non-3 prime is ≤ n+1, which is the signature of the
Gaussian moments (2m−1)!! and the 1/k!, 1/r! factors of the Feynman expansion — **a property of
expanding in h, not of the object**."* It left the residual as **bounded and explicitly not
NEEDS-SPECIALIST**.

## The test, which does not require re-reading GSWZ

**If the non-3 part is an artifact of expanding in `h`, it must be absorbed by a factorial-type
normalisation** — the expansion's own combinatorial prefactors. So:

> **Search a fixed family of natural normalisations `N(n)` for one where `N(n)·cₙ` has a denominator
> that is a PURE POWER OF 3, for every computed `n`.**

Family, fixed here: `n!`, `(n+1)!`, `(2n)!`, `n!!`, `(n+1)!!`, `(2n−1)!!`, `(n/2)!`, `2ⁿ·(n/2)!`,
`4ⁿ·(n/2)!`, and the products of any one of these with a power of 2.

## Two-outcome, and the kill branch is real

- **ARTIFACT CONFIRMED** — some `N(n)` in the family clears every non-3 prime at every computed `n`.
  Then B800's diagnosis is verified, the non-3 content is the expansion's and not the object's, and
  **B685's "integral away from 3" is discharged CONDITIONAL on GSWZ using that normalisation** —
  which is a statement about their convention, still not read here, and must be labelled so.
- **ARTIFACT REFUTED** — **no** member of the family clears them. Then the non-3 primes are **not** a
  factorial artifact of the h-expansion, B800's stated diagnosis is **wrong**, and **B685's claim is
  in worse shape than "unverified": it would be positively contradicted by the only in-repo
  computation of it.** That outcome is banked as a refutation and B685 is downgraded.

**Non-vacuity check (MB12):** the criterion can fail — `other(n)` grows (1, 1, 5, 5, 175, 1925,
9625, 175175) and a normalisation must divide **all** of them simultaneously. A family member that
works at n = 4 and fails at n = 14 is a fail.

## Pre-stated expectation

**I expect ARTIFACT CONFIRMED, via a double factorial** — the `(2m−1)!!` B800 named. The values
5, 175 = 5²·7, 175175 = 5²·7²·11·13 carry repeated small odd primes, which is double-factorial
shape, not single-factorial. **If a plain `n!` clears it instead, my reading of the mechanism is
wrong even though the verdict is right**, and that distinction gets reported.

## What this cannot do

It cannot verify GSWZ's actual convention — that requires the paper, which B800 deliberately did not
re-read and neither does this. **A CONFIRMED outcome discharges the ARITHMETIC and leaves the
CONVENTION cited.** Calling it fully discharged would repeat B685's original error one level up.
