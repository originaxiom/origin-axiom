# B578-D5 — the Kubota–Leopoldt identification: RETRACTION FIRED (and a gift)

**Date:** 2026-07-14 (rerun cell; the exact B525 error class, finally swept).
**Lock:** `tests/test_b578_kubota_retraction.py`.

**The retraction.** B519 cell A2 closed with "the tower measure IS the known
Kubota–Leopoldt 3-adic L-function" — asserted, never computed. Computed now, two
independent methods (from-scratch Bernoulli-polynomial sums in exact cyclotomic
arithmetic; Sage `DirichletCharacter.bernoulli`): **refuted.** B413's banked values
are (now exactly) the classical Gauss sums τ(χ), τ̄(χ) of the order-3 character mod 9
(12·L(χ₁,μ) = 3ζ₉ = τ(χ) exact; |τ|² = 9); the genuine KL value for the same
character is L₃(−1,χ) = −B_{2,χ}/2 = −(2/3)ζ₃ − 4/3 — living in ℚ(ζ₃) (degree 2, vs
degree 6), norm² 16/3 (vs 9), and **ℚ-linearly independent of B413's values (rank 4)**.
The field mismatch is structural (ℚ(ζ₃) ∩ ℚ(ζ₉)⁺ = ℚ, coprime Galois subgroups); a
second character (χ₋₃) confirms it is not character-choice. Additionally B519's
closing citation ("the ℚ(√−15) landscape") belonged to sibling cell A1. **B519 cell
A2's closure is retracted; the correction note is appended to its VERDICT.**

**What survives, sharpened:** B413's "reducible to a classical Gauss sum" language is
upgraded to a checked exact identity — its measure IS the τ(χ)-triple, a clean
classical object.

**The gift (H132 answered):** the two ζ₉ apparitions ARE connected —
> **L(χ₁,μ) + L(χ₂,μ) = c₀/4 = (ζ₉+ζ₉⁻¹)/4 = 432·e₃, exactly** —
the sum of the tower measure's two nontrivial Fourier coefficients is 432 times the
B578-D4 jewel. The mechanism is elementary cyclotomic trace algebra (e₃ lies on the
real subfield; the coefficients' sum projects onto it), NOT Iwasawa theory. H132:
connected, mundanely, exactly.

Firewalled. Nothing to CLAIMS.md.
