# B995 — the separating-and-rare census: SEALED OUTCOME A, and the instrument VOIDED by its own control

**Date:** 2026-08-09 · **Seat:** cc (banking) · Gate 5 untouched.
**Prereg sealed and PUSHED before compute:** `a356e98706e5e3034657f56a31f9243db7ff707b6066ad10e306da9ae4597c88`
**Declared prior, in the seal: OUTCOME B expected.**

**Both results are reported. Outcome A is NOT converted to B by fiat.**

---

## The sealed run

**Separation** against B855's two rows (m003, m206 | m136, m129, m135) — separates iff m004 differs
from **all five**. Six of eight fail: `h1_torsion` and `h1_divisors` on **m129**; `isom_order` = 8
for four of the five; `alex_degree`, `systole`, `cover2_torsions`. **Two separate:**

| | m004 | base rate (first 1000 one-cusped, **0 skipped**) |
|---|---|---|
| **alex_coeffs** | **(1, −3, 1)** | **1/1000 = 0.10%** → RARE |
| **cover3_torsions** | **(16,)** | **44/1000 = 4.40%** → RARE |

> ### SEALED VERDICT: **OUTCOME A** — two invariants both separating and rare, **against the
> declared prior**.

## THE CONTROL THE PREREG DID NOT CONTAIN — and it voids the instrument

An unexpected positive against a declared negative prior is exactly when to be most suspicious. The
MB12 question — *can the criterion fail?* — was not built into the seal. Run immediately:

### Flaw 1 — RARE and SEPARATING are not independent

The separation set has **five** members. For an invariant whose value has population rate *r*, the
chance all five differ is ≈ **(1−r)⁵**:

| invariant | r | **P(separates by chance)** |
|---|---|---|
| alex_coeffs | 0.10% | **99.5%** |
| cover3_torsions | 4.40% | **79.9%** |

> **Rarity makes separation nearly automatic against a five-element set.** Both survivors pass the
> conjunction **for the same reason they pass one half of it.**

### Flaw 2 — the rarity measure asked the wrong question

**19.3%** of the 1000 manifolds are **unique** in their Alexander polynomial (290 distinct values,
193 occurring once). m004's value occurs once — itself.

> **The sealed measure asked "how many share m004's VALUE" (one) when the informative question is
> "how surprising is uniqueness AT ALL" — a 1-in-5 event, not 1-in-1000.** A sufficiently fine
> invariant separates everything and is rare for everyone.

*(Same shape for `cover3_torsions`: 17.6% of manifolds are unique in it, and m004 is not even unique
there — it shares (16,) with 43 others.)*

## Adjudication

**Sealed outcome: A. Adjudicated finding: the instrument is non-discriminating.** Both stand,
because converting A to B by fiat would be the post-hoc rescue the seal exists to prevent, in the
mirror direction.

**NOT established:** that no separating-and-rare invariant exists. The *instrument* failed; the
*question* is untouched.

**ESTABLISHED, and worth more than the sealed outcome:**

> **A conjunction of "separates from a small set" AND "rare in the population" is ILL-POSED, because
> rarity implies separation.** Any future object-specificity test must **(i)** measure separation
> against a set large enough to have power at the invariant's own rate, and **(ii)** price rarity
> against **the base rate of BEING UNIQUE**, not the frequency of one value.

## Sensitivity note (not a change)

The seal fixed all five relatives including **m129**, which has **two cusps** — and m129 is why
`h1_torsion` failed to separate. cc3 excluded m129 on the stated ground that torsion-freeness carries
no information for a two-cusped manifold; **this seal did not adopt that exclusion.** Had it,
`h1_torsion` would have separated (1 vs 5, 5, 4, 8) — and would then have been killed anyway by its
**60.8% base rate** (B985). Verdict unaffected; the design choice recorded.

---

**Verdict: ran as sealed, returned A; its own control shows A carries no information. The Tier-2
question stands open, with a design constraint the next attempt must satisfy.**
