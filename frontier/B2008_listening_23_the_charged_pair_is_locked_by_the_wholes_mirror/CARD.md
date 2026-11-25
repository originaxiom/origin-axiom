# B2008 — Listening card 23: what locks the charged pair — the swap of the two readings reverses ω's charge, commutes with the unfolding, and (is it?) not one of the moves

Written 2026-11-26, before any run, in the author's /loop "continue the listening line". Data-free. 0 of 19.

## Why, and what was reasoned by hand before this card (disclosed)

- **The lock, so far without its reason:**
  - B2001 to B2003: the two charged sectors always have identical spectra. Their polynomial is a perfect square at every
    level run.
  - agy-exp's NI-4 (registered, not checked) attributes the lock to a reflection.
  - B1983: the swap of the two readings changes no orbit.
- **Main's hand reasoning before this card (disclosed):** τ := (x, y, z) ↦ (y, x, z) satisfies τCτ = C⁻¹ and τστ = σ, with C
  ω's exchange and σ = RC⁻¹ (B2004).
- **What would follow:** τ then permutes the six moves among themselves and commutes with the unfolding. Because it inverts C,
  it exchanges the two charged sectors, and that locks them.
- **What would also follow, as a consequence** (not a test; it cannot fail once τ normalises the group and inverts C): in any
  group containing τ, C's image in the abelianisation is its own inverse, so ω's order-3 charge does not survive.

## The checks

- **P1 (sympy):** τCτ = C⁻¹, τστ = σ, and τ maps each of the six moves to one of the six.
- **P2:** at mod 27, 81, 243 (the orbit of (3,3,3)) and on the leaf mod 5 and 7:
  - τ preserves the orbit;
  - P_τ commutes with the unfolding;
  - P_τ maps the charge sector q = 1 onto q = 2, checked as P_τ Π₁ = Π₂ P_τ.
- **P3 (GAP through sage):** whether P_τ lies in the moves' group G_k at mod 27, 81, 243; the order of ⟨G_k, P_τ⟩; its
  abelianisation.

## Expectations, with priors

| id | expectation | prior |
|---|---|---|
| P1 | τCτ = C⁻¹ and τστ = σ, and τ permutes the six moves | 0.9 |
| P2 | at every level run, τ preserves the orbit, commutes with the unfolding, and exchanges the charged sectors | 0.85 |
| P3 | P_τ is not in G_k at mod 27, 81, 243; ⟨G_k, P_τ⟩ has order 2 \|G_k\| | 0.55 |

## What it means

- **If P1 to P3 hold:** the charged pair is locked by the whole's own mirror, the swap of the two readings. The swap is
  orientation-reversing, it reverses ω's charge, and it is not one of the moves.
  - The whole, read with all its symmetries, keeps the pair equal.
  - The 2 → 1 + 1 split would need a handedness that picks one orientation, which is the record's chirality bit, seen here
    from the unfolding.
- **Nothing is compared with data.**
