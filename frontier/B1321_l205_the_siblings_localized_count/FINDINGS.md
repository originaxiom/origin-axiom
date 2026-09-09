# B1321 — L205, THE SIBLING'S LOCALIZED COUNT: m202's order-3 rotation gives Pantev–Wijnholt's count 3 on BOTH of its cusps, the signs are forced (one identification row, I-30, not two), and the three-line class of the census to nine tetrahedra has exactly six members — m202, s959, v3461, v3551, o9_40999, o9_43931 — none of which keeps the golden face; the price of the 3 is the golden polynomial throughout the class the census can see

**Date:** 2026-09-09 · **Seat:** cc (main) · **Plan:** the owner's D3 decision of 2026-09-08, L205 · **DESIGN sealed** `9b82d2e2…` before the runs ·
**Status:** **PROVED** (both computations finite, controls live; the pre-registered FAIL branch of the search at prior 0.75) · **Price:** one identification
row, **I-30**, UNEARNED at registration · **Credit:** fc R72b/R72d (the order-3 isometry and the census menu), the audit seat (R15/R18, the three arcs),
sm:B1282 and B1302 (the flat sector vector-like; the golden face absent; the two named choices), B1320 (the frame and the control).

## 1. (a) m202's localized count (`verification/b1321_m202_count.py`)

m202 has 6 isometries, none swaps the cusps; on **each** cusp the orientation-preserving cusp-fixing isometries take |det(A − I)| ∈ {0, 1, 3, 4}, with the
order-3 rotation (A = [[−1, −1],[1, 0]]) giving **3** on cusp 0 and on cusp 1 alike. In PW's frame the localized count on a fixed cusp is the fixed-point
count of the rotation, and every isolated fixed point of an orientation-preserving map of the torus has index +1 — so **the three signs are forced, not
chosen**: fc's second choice ("equal signs on the three lines") is a theorem in this frame, and the price is one row: **I-30 — the closing's charge locus ≡
a cusp of m202 fixed by its order-3 rotation** (which of the two cusps, and m202 itself within its class — both closer's choices; the object supplies the
rotation and the count, not the locus). Registered UNEARNED; the baseline migrates from 12 to 13 with this reason dated.

## 2. (b) the three-line class to nine tetrahedra (`verification/b1321_class_search.py`, 18 s)

All 61 911 manifolds of SnapPy's orientable cusped census (the bench's limit is nine tetrahedra; the plan wrote twelve), 2 750 of them two-cusped; **six**
have an orientation-preserving isometry fixing a cusp with |det(A − I)| = 3:

| member | tetrahedra | H₁ | cusps carrying the 3 | Alexander test | golden specialisations |
|---|---|---|---|---|---|
| **m202** | 4 | ℤ ⊕ ℤ | both | two-generator (∂R/∂a = (t₂ − 1)Δ; seven ±1 monomials = B1302's) | **0 of 48** |
| s959 | 6 | ℤ/3 ⊕ ℤ ⊕ ℤ | both | rank-3 presentation, gcd of the 2-minors | 0 of 48 |
| v3461 | 7 | ℤ ⊕ ℤ | both | two-generator | 0 of 48 |
| v3551 | 7 | ℤ/2 ⊕ ℤ ⊕ ℤ | both | rank-3, minors' gcd | 0 of 48 |
| o9_40999 | 9 | ℤ/4 ⊕ ℤ ⊕ ℤ | both | rank-3, minors' gcd | 0 of 48 |
| o9_43931 | 9 | ℤ/5 ⊕ ℤ ⊕ ℤ | both | rank-3, minors' gcd | 0 of 48 |

No presentation was left untested. **Controls:** m202 is in the class with 0 golden specialisations (B1302's number, reproduced by main's own re-implementation
of its test); a planted factor t₁² − 3t₁ + 1 on m202's Δ is detected by the same test. **FAIL branch, as pre-registered: no member of the three-line class
through nine tetrahedra keeps the golden face.**

## 3. What this settles

The owner's bounded arc closes D3 as a **priced door**: the object's own family reaches a localized 3 only on manifolds that have lost the golden
polynomial — the fibre monodromy that makes m004 the object — and reaching it costs one identification row on top. Nothing in the census to nine
tetrahedra offers a 3 and the golden face together. What would reopen it: the census beyond nine tetrahedra (not on this bench), or a member of the class
found by construction rather than by census (a Dehn filling of a three-cusped manifold, say) — recorded as the remaining question on L205, which moves
from OPEN to PRICED.

## Receipts, lock

`verification/b1321_m202_count.{py,out,json}`, `b1321_class_search.{py,out,json}`, `already_banked_at_seal.txt`; `tests/test_b1321_l205_the_siblings_localized_count.py`.
