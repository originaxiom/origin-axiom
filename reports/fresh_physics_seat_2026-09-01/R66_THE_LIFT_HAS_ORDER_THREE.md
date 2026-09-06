# R66 — THE LIFT HAS ORDER THREE: w₃'s Tits lift in the exact e₆ is of order 3 with Ad-multiplicities (24, 27, 27) — the A₂³ class, no assumption left

**Seat:** fresh physics seat (fc) · **Date:** 2026-09-06 · **Status:** seat report, not banked. Exact (Fractions on B351's 78-dimensional Chevalley e₆, re-run on this bench in R60); script `computations/r66_tits_lift.py`. Removes the "order-3 lift" caveat of R64 §0 and R65 for the E₆ statement.

## What was done

1. The icosian E₆ = {1, g}^⊥ of R64 is given a positive system by a generic functional; its six simple roots have the E₆ Cartan matrix and are matched to Bourbaki's labelling by a permutation. Every one of its 72 roots is then an integer combination of them, and the set of coordinate vectors equals B351's root list exactly.
2. w₃ = w_{A₂}⁻¹·L_g becomes a 6 × 6 integer matrix on simple-root coordinates, and a breadth-first search over W(E₆) (45,649 elements visited) returns a word of length 24:
   `w₃ = s₆ s₂ s₄ s₅ s₃ s₄ s₁ s₃ s₂ s₄ s₅ s₆ s₂ s₄ s₅ s₃ s₄ s₁ s₃ s₂ s₄ s₅ s₃ s₄`.
3. Each simple reflection is lifted as nᵢ = exp(ad eᵢ)·exp(ad e₋ᵢ)·exp(ad eᵢ) on the 78 (with B351's convention [e_α, e_{−α}] = −h_α, so fᵢ = −e₋ᵢ); ad eᵢ is checked nilpotent of degree 3, and each nᵢ is checked to act on the Cartan as sᵢ. The lift ŵ₃ is the product in the word's order; its Cartan action is checked to reproduce the Weyl matrix of step 2.

## Result

| | |
|---|---|
| ŵ₃³ on the 78 | **= identity** |
| Ad-eigenvalue 1 multiplicity | **24** |
| ω + ω̄ multiplicities | **54** (= 27 + 27) |
| class | **A₂ × A₂ × A₂** (centralizer dim 24) — the trinification element; the D₄ × T² class would read (30, 24 + 24) |

So the founding ratio's E₆ factor lifts to an element of order 3 in the adjoint group of E₆ whose centralizer is SU(3)³. R65's "the object's element selects the A₂³ class and rejects the D₄ class (85 → 40)" now rests on a computed lift, not on a cycle-count argument.

## What remains a caveat

R64 §4's placement of L_g, w_{A₂}, w₃ into the three order-3 classes of **E₈** used the same cycle-count argument at the E₈ level; the E₈ lifts were not built (no exact e₈ on this bench). The E₆ half of that table is now settled by this report; the E₈ half is still stated for order-3 lifts.

*Sweep: no Tits lift or Weyl word for an order-3 element appears in B1256, B1257, B1264, B1274, B1275 or the SM-derivation branch's B1268–B1271.*
