# B588 — the sector-exchange theorem (L81(a)) — prereg

**Date: 2026-07-14. Preregistered BEFORE the computation. Firewall: nothing to
CLAIMS.md; no SM quantities.**

## The question (L81(a))

B584 observed: the level-rank pair realizes ONE number (−1/φ) in OPPOSITE
parity sectors — all-even on SU(2)₃ (where C = 1), all-odd on SU(3)₂
(where tr_even = 0). Prove the exchange at the parity-projector level.

## The claim (to be established computationally + structurally)

1. **(D_A₁) the rank-1 decomposition identity:** Z(W; SU(2)_k) =
   ½[t₊(κ′) − t₋(κ′)] on ℂ[ℤ_{2κ′}] (κ′ = k+2; the A₁ Weil rep,
   T = e^{πiμ²/(2κ′)}, S = the finite FT with pairing e^{−πiμν/κ′}), with
   t± = tr(ρ_Weil(W)∘P_{±1}) — verified exactly against banked su2 values
   for balanced words across κ′.
2. **The membership fact:** −1 = w₀ ∈ W(A₁) (it IS the reflection; C_stage =
   −w₀ = +1, all reps self-dual) but −1 ∉ W(A₂) (no Weyl element of A₂ is
   −I; C_stage = −w₀ ≠ 1). Hence the parity Gauss term (conductor
   det(A+I)-type) enters the PLAIN Weyl assembly on the A₁ side (the only =
   even sector) and the C-COSET assembly on the A₂ side (the odd sector).
3. **The ingredient identity at κ = κ′ = 5 (the level-rank point):** the A₁
   assembly ½[t₊ − t₋] and the A₂ twelve-term assembly are built from the
   SAME Gauss data (the unit identity term and the √5-family terms), and both
   evaluate to −1/φ: ½(1 − √5) = (1/12)[(1+5) − 6√5]. The sector exchange is
   exactly the migration of the −1 element across the Weyl-group boundary
   under level-rank — B242/B243's "level-rank = conjugation" seen at the
   parity-projector level.

## Falsifiers

- (D_A₁) fails ⇒ the rank-1 factorization is wrong — stop.
- If t₊/t₋ at κ′=5 are not (1, √5)·units, the ingredient identity fails as
  framed — report what they are.

## MB13

B587 (the A₂ machinery — reused), B204/Jeffrey (the SU(2) Gauss framework,
known/cited — (D_A₁) is its restatement in the B587 normalization), B238
(su2 banked values), B242/B243 (level-rank = conjugation), B584 (the sector
observation). No prior parity-projector-level exchange statement found.
