# B2006 — Listening card 21: the whole's small group at its prime is a 3-adic layer over the cube group — G_k maps onto S₄ by reduction mod 9, its kernel is a 3-group, and the halving's character splits as S₄'s sign times an order-3 character carried by the kernel

Written 2026-11-25, before any run, in the author's /loop "continue the listening line". Data-free. 0 of 19.

## Why

- **B2005:** on ω's orbit mod 3ᵏ the whole acts through a small group G_k: of order 24 at k = 2 (the cube group S₄, B1984), and
  of order 216, 1,944 and 52,488 at k = 3, 4 and 5.
- **The halving holds exactly where G_k keeps ℤ₆,** so that the modular group's order-6 character ρ factors through it.
- **Reduction mod 9** should map each orbit onto the 8-point orbit at mod 9. That makes G_k an extension of S₄ by a kernel K_k
  of order |G_k|/24: 9, 81 and 2,187.
- **What follows from S₄ having only the sign character** (stated here, not tested: it cannot fail once T1 holds): the order-3
  part of ρ must be non-trivial on K_k. The questions are what the order-2 part is, and what K_k is.

## The checks

- **T1:** reduction mod 9 is a C- and σ-equivariant map of the orbit mod 3ᵏ onto the orbit mod 9, for k = 3, 4, 5. The induced
  map G_k → G₂ is onto, and its kernel K_k has the order |G_k|/24. The fibres all have the same size.
- **T2:** the order-2 part ρ³ is trivial on K_k, so it is S₄'s sign character pulled back.
- **T3:** whether K_k is abelian, its exponent, and whether it is elementary abelian.

## Expectations, with priors

| id | expectation | prior |
|---|---|---|
| T1 | reduction mod 9 is equivariant and onto at k = 3, 4, 5; G_k → S₄ is onto, with kernel of order 9, 81 and 2,187, a 3-group | 0.8 |
| T2 | ρ³ is trivial on the kernel at k = 3, 4, 5 | 0.7 |
| T3 | K_3 is elementary abelian of order 9 (ℤ₃²) | 0.5 |

## What it means

- **If T1 and T2 hold:** the whole at its prime is the cube group S₄ (the common point's group, the three in its S₃) with a
  3-adic layer on top.
  - S₄'s sign carries ρ's order-2 half.
  - The layer, which does not exist at mod 9, carries the order-3 half, ω's charge.
  - The halving appears exactly when the layer appears.
- **Nothing is compared with data.**
