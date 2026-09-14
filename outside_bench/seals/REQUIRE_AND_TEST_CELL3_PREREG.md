# PREREGISTRATION — CELL 3: requirement 1 (matter), the count of three

*Outside bench, 2026-09-14. Written and hashed BEFORE the certificate runs. Gate 5 untouched.*

## R — the requirement, verbatim (`docs/TOE_REQUIREMENTS_LEDGER.md` §A row 1)

> the SM's algebra, matter content, hypercharges, **three generations**

## P — the predicate

In the frame the record actually uses — Pantev–Wijnholt's localized count, as
`frontier/B1321_l205_the_siblings_localized_count` computes it — the count at a fixed cusp is the
fixed-point count of an orientation-preserving cusp-fixing isometry, equal to **|det(A − I)|** for A the
cusp map. B1321, verbatim: *"in PW's frame the localized count on a fixed cusp is the fixed-point count
of the rotation, and every isolated fixed point of an orientation-preserving map of the torus has index
+1 — so the three signs are forced, not chosen."*

**P₃ = the object has an orientation-preserving cusp-fixing isometry with |det(A − I)| = 3.**

## T — m004 against P₃

The record says *"the object counts 2 at every fixed locus"*. Recomputed here, not cited: m004's full
multiset of |det(A − I)| over orientation-preserving cusp-fixing isometries is printed.

## B — what is new here

B1321 asked **which** manifolds have 3, over two-cusped census members to nine tetrahedra, and found
**six** of 61 911. It did **not** ask the distribution — how many objects supply 2, how many supply 3,
how many supply anything. Require-and-test needs the distribution, because "m004 supplies 2" is only
information against how many objects supply what.

**The sweep:** `snappy.OrientableCuspedCensus` in census order, **all cusp numbers**, population
**N = 4000**, fixed now. For each manifold the full multiset of |det(A − I)| over orientation-preserving
cusp-fixing self-isometries, and the maximum. The population is printed before any rate.

## THE TWO OUTCOMES

- **OUTCOME A — the 3 is RARE** (< 1 % of the population attains 3): requirement "three generations"
  does real selecting work; m004 fails it and a rare few pass.
- **OUTCOME B — the 3 is COMMON** (≥ 1 %): it selects little, exactly as Cell 2 found for the 2T door.

## THE SECOND QUESTION, PREREGISTERED SO IT CANNOT BE ADDED AFTERWARDS

Is **2** itself distinguished, or is m004's 2 simply the commonest value? Report the **full
distribution** of the maximum attained count, not only the rate at 3. If 2 is the modal value, then
*"the object counts 2 at every fixed locus"* is a statement about tori, not about m004.

## CONTROLS

| # | control | catches |
|---|---|---|
| L1 | m004's own multiset is computed and printed; it must contain 2 | instrument not wired to the object |
| L2 | **m202 must return 3**, reproducing B1321 on its own witness | an instrument that cannot see a 3 at all — which would make OUTCOME A vacuous |
| L3 | every recorded isometry has cusp-map determinant +1 (orientation-preserving), asserted not assumed | reading orientation-reversing isometries as rotations |
| L4 | population asserted > 0 and printed before any rate; manifolds whose isometry group is unavailable are counted as SKIPPED, never as 0 | the B1197 vacuity trap, and a silent undercount reading as rarity |

## WHAT THIS CELL MAY NOT CONCLUDE

Nothing about generations as physics: the identification h¹ ↔ 4d generations is **I-26, a declared
input** (`TOE_REQUIREMENTS_LEDGER` §E row 4, *"the dimension gap not exhibited"*), and this cell does
not earn it. The count here is a fixed-point count on a torus, and it is reported as one. No value.
