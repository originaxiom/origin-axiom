# B557 — the rung-2 carriers (tower-probe campaign, verified 2026-07-13)

Two escalator-campaign cells, adversarially verified and re-checked in-sandbox
(`tests/test_b557_carriers.py`). Firewalled: pure combinatorics / spectral number
theory, no Standard-Model claim. Lit-gates UNCLEAR → no novelty claim.

## E1 — the explicit 8-letter carrier σ₈ (closes B557-E1 / FL3)

The escalator image T(M₄) = [[M₄,M₄],[M₄²,M₄]] is a non-negative integer 8×8 matrix,
hence the incidence matrix of a substitution on 8 letters. Reading column j as the
Parikh vector of letter j's image gives an **explicit primitive σ₈** (image lengths
23,14,18,11,10,6,8,4):

```
1 -> 1 2 3 3 4 5 5 5 5 5 6 6 6 7 7 7 7 7 7 8 8 8 8
2 -> 1 3 4 5 5 5 6 6 7 7 7 7 8 8
3 -> 1 2 3 4 5 5 5 5 6 6 7 7 7 7 7 8 8 8
4 -> 1 3 5 5 6 6 7 7 7 8 8
5 -> 1 2 3 3 4 5 6 7 7 8
6 -> 1 3 4 5 7 8
7 -> 1 2 3 4 5 6 7 8
8 -> 1 3 5 7
```

Verified: incidence(σ₈) = T(M₄) exactly; σ₈ **primitive** (incidence² > 0, so k=2);
and the **quine seed-invariant LIFTS** — because row 1 of T(M₄) is all-ones (M₄'s row a
is all-ones, T stacks [M₄|M₄] on top), letter 1 occurs exactly once in each image, and
ordering it first makes it appear once at **position 0** in all 8 images — the same
signature the seed a has in σ₄. So rung 2 is **built, not just posited**, and the
seed-invariant is a tower invariant (lifts at every rung Tⁿ). Only the Parikh columns
are matrix-forced; intra-image letter order is a gauge, and seed-first is the
representative realizing the invariant.

## T-1 — the rung-2 gap-label module (the next prediction after B555)

The rung-2 matrix T(M₄) (8×8) has:
- **charpoly** x⁸−4x⁷−56x⁶−152x⁵−205x⁴−192x³−134x²−56x−11, **irreducible over ℚ**;
- **Perron** λ₂ = 10.724751771861389…, satisfying the λ-law λ₂ = λ₁(1+√λ₁);
- **field** K = ℚ(λ₂): degree 8, signature (2 real, 3 complex pairs) — NOT totally real,
  NOT Galois; a **golden octic tower** ℚ ⊂ ℚ(√5) ⊂ ℚ(√5,√φ) ⊂ K (degrees 2,4,8), with
  polynomial discriminant −2¹⁶·5⁴·59²·12641²;
- **letter frequencies** = normalized right Perron eigenvector; scaled to comp0=1 it is
  (1, 1/φ, √φ, √φ/φ, 1.9173…, 1.1850…, 2.4389…, 1.5073…) with entry-sum λ₂, so the first
  letter's frequency is exactly **f₀ = 1/λ₂**.

**Predicted rung-2 gap labels** (gap-labeling theorem): the IDS values lie in the
ℤ-module ⟨f₀,…,f₇⟩ mod 1 (ℤ-rank 8, dense, only low-height relation Σfᵢ=1). Simplest
candidate labels: 1/λ₂ = 0.09324, f₁ = 0.05763, f₆ = 0.22741, f₀+f₁ = 0.15087. This is
the **degree-8 successor** to B555's degree-4 rung-1 prediction — computed from the
matrix alone (the explicit chain via σ₈ above is the natural continuation). Open riders:
the octic Galois group is unresolved; the chain-to-IDS-plateau check is not yet run.
