# B2008 — Listening 23: the charged pair is locked by the whole's mirror — the swap of the two readings reverses ω's charge, exchanges L with R, commutes with the unfolding, and is not one of the moves; with it, ω's order-3 charge is gone

**Verdict: PROVED (exact: sympy; integer permutation matrices; GAP membership through sage).** Main, 2026-11-26, in the
author's /loop "continue the listening line". Data-free. Register rows P-882 and P-374. **0 of 19.**

## Seen first

- **B2001 to B2003:** the two charged sectors have identical spectra at every level. Their polynomial is a perfect square.
- **B1983:** the swap changes no orbit.
- **B2004:** σ = RC⁻¹, and the whole acts through ⟨C⟩ * ⟨σ⟩.
- **agy-exp's NI-4** (harvest row 2009; registered, not checked here): "orientation-reversing reflection P locks
  G₊₁ ≡ G₋₁" on X_ω.
- **The record's chirality bit** (the main goal's masterplan; P-374 types it as a convention, two 𝔽₂ bits of which the
  arrow is forced and the chirality a convention): the two orientations are exchanged by the mirror.
- **Swept:** `VERDICT topic-sweep /swap of the two readings|the swap|mirror locks|orientation-reversing|chirality bit/: 52 of 1749 arcs on main match (NEGATIVE 5, OPEN 2, PROVED 45); 19 register rows match (DONE 10`.
- **The literature (standard):** PGL(2, ℤ) = PSL(2, ℤ) ⋊ ⟨an orientation-reversing involution⟩, which inverts the order-3
  generator. Its abelianisation is ℤ₂ × ℤ₂.

## Custody

**Disclosed:** τCτ = C⁻¹ and τστ = σ were reasoned by hand before the card.

## The results (`verification/mirror.py`, `mirror_run.txt`; `mirror_gap.py` through sage, `mirror_gap_run.txt`)

- **P1 holds** (sympy): τ = (x, y, z) ↦ (y, x, z) satisfies τCτ = C⁻¹ and τστ = σ. It permutes the six moves: L ↔ R,
  L⁻¹ ↔ R⁻¹, X ↔ X⁻¹.
- **P2 holds:** at mod 27, 81 and 243 (the orbit of (3,3,3)) and on the leaf mod 5 and 7:
  - τ is an involution preserving the orbit;
  - [P_τ, W] = 0 exactly;
  - P_τ Π₁ = Π₂ P_τ to 3 × 10⁻¹⁶, so the swap carries charge q = 1 onto q = 2.
- **P3 holds:**

  | level | τ in G_k | \|⟨G_k, τ⟩\| | its abelianisation |
  |---|---|---|---|
  | mod 27 | no | 432 = 2 · 216 | ℤ₂ × ℤ₂ |
  | mod 81 | no | 3,888 = 2 · 1,944 | ℤ₂ × ℤ₂ |
  | mod 243 | no | 104,976 = 2 · 52,488 | ℤ₂ × ℤ₂ |

- **As the card said it must, the 3-part is gone** once the swap is added. ℤ₂ × ℤ₂ is the image of PGL(2, ℤ)'s own
  abelianisation.

## What the whole does, read in its own terms

- **The two charged members are kept equal by the whole's mirror:** the swap of the two readings, which exchanges the two moves
  L and R.
  - It reverses ω's charge.
  - It commutes with every move taken together, so with the unfolding.
  - It is not itself a move. The moves realise only the orientation-preserving modular group.
- **The whole with its mirror cannot carry ω's charge** at the three levels run. Adding the swap leaves only ℤ₂ × ℤ₂: the sign of S₄ and the sign of
  orientation (the ℤ₂ × ℤ₂ is computed; naming its factors so is a reading, not computed; Review 87).
  - So the charge, and with it the halving's tie (B2005, B2006), lives in the orientation-preserving part.
  - The charged pair is locked by the orientation-reversing part.
- **Read in the record's own terms:**
  - **The split so far:** 3 → 1 + 2 is native (B2000, B2001).
  - **The last split:** 2 → 1 + 1 needs an ingredient that tells the two orientations apart, a handedness that picks L over R.
    The whole, taken with all its symmetries, does not supply one. This is the chirality bit, met from the unfolding [Review 87, 2026-11-26: a reading in the record's vocabulary; the fact is only that a symmetry which is not a move locks the pair].
  - **agy-exp's synthesis:** this is the whole's own form of its statement that the last split needs a P-breaking asymmetry.
- **No Standard Model shape was asked for, and nothing is compared with data.**

## What is open

- **What could pick an orientation** without being chosen: a sourced handedness (the record's chirality-bit line), read
  against this lock.
- **agy-exp's NI-4 checked on main:** the same lock on the analytic side, on X_ω.
