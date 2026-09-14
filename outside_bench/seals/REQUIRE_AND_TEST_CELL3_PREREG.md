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

---

# ADDENDUM 1 (2026-09-14) — CONTROL L1 WAS MIS-SPECIFIED BY THIS SEAL, AND THE MIS-SPECIFICATION IS THE FINDING

**The seal above wrote:** *"The record says 'the object counts 2 at every fixed locus'. Recomputed
here: m004's full multiset of |det(A − I)| … is printed"* — and made **L1 = the multiset must contain 2.**

**It does not, and it should not.** The first run returned m004 → **{0: 2, 4: 2}**. The instrument is
correct; the control imported a number from the wrong frame.

**The record uses TWO different counts, and this seal collapsed them into one.**

| # | quantity | on m004 | where |
|---|---|---|---|
| 1 | **\|det(A − I)\|** — the cusp fixed-point count, Pantev–Wijnholt's localized count | **{0, 4}** | `docs/MAIN_GOAL.md` l. 80–84, quoting **B1295 as a banked NEGATIVE**: *"968 isometries, 1,376 cusp-fixing pairs, `\|det(A−I)\| ∈ {0: 882, 4: 494}`"* — over all 87 covers to degree 10 |
| 2 | **χ(Fix g) = 1 − s_μ(g)** — the Euler characteristic of the fixed locus in the 3-manifold | **{0, 2}** | `docs/MAIN_GOAL.md` l. 87: *"On m004 every isometry has `χ(Fix g) = 1 − s_μ(g) ∈ {0, 2}`"* |

**The "2" of "the object counts 2 at every fixed locus" is quantity 2. The "3" of B1321 and of
requirement 1's three generations is quantity 1.** They are not on the same scale, and
`docs/TOE_REQUIREMENTS_LEDGER.md` §C row 2 carries the sentence *"the object counts 2 at every fixed
locus"* with no frame attached — so a reader of the ledger cannot tell that the 2 and the 3 are
different quantities. This is rule #26 in the wild: **a paraphrase is where the hypotheses go missing**,
and it took writing a predicate to expose it, because a predicate must name its quantity.

**CORRECTED CONTROL L1, with its source stated:** in the |det(A − I)| frame, m004 must return
**{0, 4}** — B1295's own banked values. **L2 (m202 → 3) is unchanged and passed on the first run.**

**Not changed:** the sweep, the population, the two outcomes, or the second question. Only the control's
expected value, and only because the seal named the wrong one. The first run's numbers stand and are
reported; nothing was re-aimed after seeing a rate.

**χ is NOT swept across the census.** `χ(Fix g) = 1 − s_μ(g)` is stated in the record **for m004**;
generalising it to arbitrary census manifolds would be the same paraphrase error one level down. It is
printed for m004 and m202 only, from the record, and labelled as cited.
