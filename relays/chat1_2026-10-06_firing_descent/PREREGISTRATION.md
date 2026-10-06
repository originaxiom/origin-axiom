# Does s961's firing come down to m025? (chat1, 2026-10-06) — sealed before any cell is run

**Question.** s961 (M3, the root's 3-fold cyclic cover, B1432: 72 firing modules, 48 backgrounds) is also tick 6 of the
golden act, i.e. the orientation double cover of m025 = tick 3 (N3). The register lemma (chat1 2026-10-06, 264/264)
says I(M; p*U) = I_w(U) + I_w(U⊗w). If a firing module V (I(V) = ±1, odd) were a pullback p*U, the two register
halves would be forced unequal. Registered open cell from the non-orientable-index relay: do M3's firing modules descend
to N3?

**Seen first.** B1432 (census, conventions: torsion characters trivial on the peripheral group; loci h¹(λ) ≥ 1; 72
firing all on the 12 non-square loci), B1471 (mirror/realness), B1476 (s961 CS 0, 4 of 8 spin structures survive a
mirror), B1477, sm:B1506 (the triplet as a deck orbit on s961), main GENESIS FK2/FK12. No arc asks whether s961's
firing modules are invariant under the orientation-reversing deck of s961 → m025.

**Argument written before running (to be checked, not assumed).** A σ-invariant character χ of M = ker w extends to N
(χ̃(t)² = χ(t²)), so χ restricted to the torsion T_M = (ℤ/4)² factors through H₁(N) torsion = (ℤ/2)²: order ≤ 2, i.e. a
square. A non-split V with α ≠ β has a unique invariant line, so σ*V ≅ V forces σ*α = α, σ*β = β, hence λ a square. All
firing modules sit on non-square λ. Therefore none is σ-fixed and none descends as a 2-dim module.

**Instrument.** chat1's own F_p code (nonor_index.py functions, not B1297's d2lib, not B1432's myindex), s961 presented
as ker w ⊂ π₁(m025) by Reidemeister–Schreier, torus cusp ⟨x, m²⟩. Primes 13, 29, 37 (all ≡ 1 mod 4); a cell counts only
if all three agree. Module = non-split extension with α the sub-character, β = α/λ the quotient; the other stacking
order reported too.

| | prediction | prior | kill |
|---|---|---|---|
| C1 (control) | 16 peripheral-trivial characters; all 16 loci with h¹ = 1; 72 firing of 256 in at least one stacking order, all on 12 non-square loci, 6 each | 75% | any number differs from B1432 → the instrument or the convention is wrong; nothing below is read |
| D1 | σ (conjugation by an orientation-reversing t) fixes exactly the 4 characters of order ≤ 2 | 95% | any order-4 character fixed |
| D2 | σ fixes none of the firing modules; it pairs them, 36 pairs, equal index within a pair | 90% | a firing module σ-fixed, or a pair with different index |
| D3 (Shapiro control) | for every firing V, the 4-dim induced module Ind V on m025 has untwisted class index = I(s961; V) | 85% | any mismatch |

**What a result means, fenced.** D2 holding: the three-fold firing is not visible on the act-alone state as a 2-dim
module; it is visible on m025 only as the induced pair {V, σ*V} (D3). That closes the registered cell negatively for
the register lemma as a selector at this level. It is not a statement about physics, generations or values.
