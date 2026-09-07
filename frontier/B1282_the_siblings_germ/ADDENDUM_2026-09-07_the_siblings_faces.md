# B1282 — addendum (2026-09-07): the sibling's faces — m202 keeps the object's arithmetic face and not its golden one

L208 (iii) asked whether the E₆ chain of B1270 (the two faces: the icosian E₈ of the golden monodromy, the Eisenstein plane
of ℚ(√−3)) transports to the two-cusped sibling. The arithmetic face does: m202 is cusped arithmetic over ℚ(√−3) and keeps
2T (96 surjections; B1292, re-run in B1281). **The golden face does not appear in m202's Alexander module**
(`verification/siblings_faces.py`, `SELFTEST: PASS`, run record `siblings_faces_run.txt`):

- From the Fox derivatives of the relator aabbAbAABBaB (a ↦ t₁, b ↦ t₂; H₁ = ℤ²), with the fundamental formula
  ∂R/∂a = (t₂ − 1)Δ, ∂R/∂b = −(t₁ − 1)Δ checked to agree: **Δ_{m202}(t₁, t₂) ≐ t₁t₂ + t₁ + t₂² + t₂ + 1 + t₂²/t₁ + t₂/t₁**,
  a Newton polygon with seven monomials and every coefficient ±1 (so every face of the Thurston norm ball is a candidate
  fibered face).
- Over the 96 primitive classes (p, q) with |p|, |q| ≤ 6, the specialisation Δ(t^p, t^q) — the characteristic polynomial
  of the monodromy on the fibre's H₁ when (p, q) is fibered — is monic 90 times, always with cyclotomic-type factors
  (Φ₇, Φ₁₂, t⁴ + 2t³ + t² + 2t + 1, …), and **t² − 3t + 1 divides none of them**: no fibration of m202 has the object's
  golden monodromy, so B1270's E₈ face (the icosian lattice from ⟨R, L⟩ mod 5) is not carried by the sibling's
  Alexander module.
- The diagonal specialisation Δ(t, t) = −(2t² + 3t + 2) is not monic (the class (1, 1) is not fibered) and has the roots
  **(−3 ± i√7)/4** — on the unit circle with cos θ = −3/4 — which are exactly the μ-spectrum of B1280's case B on the
  object's elliptic components (tr μ = −1/2), the ℚ(√−7) of the heartbeat's period-4 field (B448, B316). Recorded as a
  coincidence of numbers; not identified.

So "leave the knot, keep the field" (main B1291, fc R72) keeps E₆'s arithmetic face and loses its golden one: on m202 the
E₆ would have to come from ℚ(√−3) and 2T alone (B727's route), without the icosian E₈ and its family triplet (B1270,
B1271). L208 (iii) is answered negatively for the Alexander-module route; L208 (iv), the price of a sibling, is sharpened:
it costs the E₈ face.
