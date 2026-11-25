# B2006 — Listening 21: the whole's small group at its prime is a 3-adic layer over the cube group — G_k maps onto S₄ by reduction mod 9, its kernel is ℤ₃² at mod 27, ℤ₉² at mod 81 and a non-abelian group of order 3⁷ at mod 243; the halving's order-6 character is S₄'s sign times an order-3 character carried by the layer

**Verdict: PROVED (exact: a walk over every element of G_k, up to 52,488; sympy for the kernels).** Main, 2026-11-25, in the
author's /loop "continue the listening line". Data-free. Register row P-882. **0 of 19.**

## Seen first

- **B2005:** G_k has order 216, 1,944 and 52,488 at mod 27, 81 and 243, with abelianisation ℤ₆, and ρ factors through it. At
  mod 9 it is S₄ with ℤ₂.
- **B1984:** the common point's group is the cube group S₄. Mod 9 the cusp is the cube.
- **B1985:** the 3-tower is self-similar.
- **B1991:** at 2 the linear group is S₃.
- **Swept:** `VERDICT topic-sweep /3-adic layer|reduction mod 9|kernel of order 9|Z3\^?2|cube group S4/: 1 of 1747 arcs on main match (PROVED 1); 1 register rows match (QUEUED 1)`.
- **The literature (standard):** S₄'s only non-trivial linear character is the sign. A group whose order is a power of a prime
  is that prime's p-group.

## The results (`verification/layer.py`, `layer_run.txt`)

| level | reduction mod 9 (equivariant, onto) | fibre size | G_k → S₄ onto | kernel K_k | ρ³ on K_k | ρ² on K_k |
|---|---|---|---|---|---|---|
| mod 27 | yes | 9 | yes | order 9, abelian, all non-identity elements of order 3: **ℤ₃²** | trivial | all of ℤ₃ |
| mod 81 | yes | 81 | yes | order 81, abelian, element orders {1: 1, 3: 8, 9: 72}: **ℤ₉²** | trivial | all of ℤ₃ |
| mod 243 | yes | 729 | yes | order 2,187 = 3⁷, **non-abelian**, exponent 27 | trivial | all of ℤ₃ |

- **T1 holds:** reduction mod 9 is a C- and σ-equivariant map onto the cube's 8 points, with uniform fibres. G_k maps onto S₄
  with a 3-group kernel of order |G_k|/24.
- **T2 holds:** the order-2 half ρ³ is trivial on the kernel, so it is S₄'s sign pulled back.
- **The order-3 half ρ² takes every value on the kernel,** as it must, since S₄ has no order-3 character. It is stated, not
  counted as a test.
- **T3 holds:** K₃ = ℤ₃². Beyond the expectations, K₄ = ℤ₉² (its element orders are those of ℤ₉²), and K₅ is non-abelian of
  order 3⁷. That is the same step at mod 243 that B2005 found in |G₅|.

## What the whole does, read in its own terms

- **At its prime the whole is the cube group with a 3-adic layer.**
  - The cube group S₄ is the common point's group, with the three in its S₃.
  - On it sits a 3-group: ℤ₃², then ℤ₉², then a non-abelian group of order 3⁷.
  - The layer appears at mod 27. At mod 9 there is only the cube.
- **The halving's character splits between the two pieces.** The modular group's order-6 character ρ is S₄'s sign times an
  order-3 character, which is ω's charge, ρ(C) = ω. The charge lives on the layer.
- **So the halving appears exactly when the layer appears.** That ties B2002 to B2005 into one statement: at its prime, the
  whole's 3-adic layer carries ω's charge and makes the charged pair an exact half-scale copy of the neutral member.
- **No rate is read as physical, and nothing is compared with data.**

## What is open

- **The layer's law for every k:** ℤ₃², ℤ₉², and then a non-abelian group of order 3⁷ rather than ℤ₂₇² of order 3⁶. What
  happens at mod 243, and whether the extra factor of 3 recurs.
- **The full derivation of the halving from this structure.** Induce from the stabiliser, twist by the layer's character, and
  read the three left-out modes off S₄ and the stabiliser.
