# Card W-F19: a proof attempt for the class index at odd levels (W-F12's open item)

**Seat:** the web seat (chat1). **Kind:** `result:` (data-free), a proof attempt with a sealed check. **Committed before
the work**, except step 1's formula, which was derived while this card was drafted (disclosed).

## The claim

At every odd level of a metallic tick, every doublet V has class index zero:
- I_w(V) = n(V) − n(V* ⊗ w) = 0;
- V is any non-split extension 0 → α → V → β → 0 of characters, as in W-F12;
- w is the orientation character, and n is the dimension of the interior classes.

W-F12 computed this on 51,506 doublets at golden levels 1, 3, 5 and 7, and found no proof.

## The route

1. **A formula valid at every level.** For any finite-dimensional module V of a one-cusped mapping torus with peripheral
   group P:

   I_w(V) = h⁰(P; V* ⊗ w) + h⁰(G; V) − h⁰(G; V* ⊗ w) − r¹(V),

   where r¹(V) is the rank of the restriction H¹(G; V) → H¹(P; V). It follows from:
   - twisted Poincaré–Lefschetz duality;
   - the half-lives-half-dies count on the cusp;
   - Euler characteristic zero for G and for P.
2. **Odd levels.** At an odd level, P is a Klein bottle group (μλμ⁻¹ = λ⁻¹) and w(μ) = −1. Each term is computed for a
   doublet from:
   - W-F6's laws for characters on G;
   - the Klein bottle's cohomology of characters (done by hand);
   - the long exact sequences of 0 → α → V → β → 0 on G and on P;
   - the snake lemma for the restriction.

   The cases are the types of α, β and ℓ = α/β. Here ℓ = 1, or ℓ is non-trivial on the fibre with ℓ(μ) = −1.
3. **The deliverable.** Either a proof that the four terms cancel in every case, or the exact case where the argument
   needs a cup product that the laws do not decide. That case is named, and its count is checked against W-F12's
   n = 1 doublets (6, 90 and 756 at levels 3, 5 and 7).

## The sealed check (expectations in the script's header before the run)

- **The formula.** Step 1's formula, term by term, on every doublet at golden levels 3 and 5, and on every record module
  at golden level 4 (an even level, where I can be ±1).
- **New odd levels.** Bronze levels 1 and 3, and silver (m = 2) levels 1 and 3. There the claim is a prediction: the
  class index is zero on every doublet.
- **A plant.** w left out of the formula fails at some odd level.

## What would refute the claim

A doublet at an odd level with a non-zero class index, at any m. A proof that holds only for golden would be reported
as such.
