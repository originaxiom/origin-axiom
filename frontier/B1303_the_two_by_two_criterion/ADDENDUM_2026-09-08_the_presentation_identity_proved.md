# B1303 addendum (2026-09-08, later) — the presentation identity, proved; the three presentations agree on every character

B1303 wrote π₁(Y_n) = ⟨a, b | φⁿ(a) = a, φⁿ(b) = b⟩ with φ: a ↦ a²b, b ↦ ab and validated it by homomorphism counts
(n = 2 … 5) and by the Reidemeister–Schreier Fox calculus (n ≤ 13). The identity is now **proved**
(`frontier/B1304_the_two_adic_tower/ADDENDUM_2026-09-08_the_positive_half_proved.md` §2(1)): φ = c_a∘φ′ where φ′ fixes
the boundary commutator, and a = b⁻¹ φ′(b⁻¹)⁻¹ is a Reidemeister coboundary, so killing (a t)ⁿ = b⁻¹ tⁿ b in the
mapping-torus group is killing tⁿ — the branched cover's relation. The same holds for the half-deck presentation
⟨a, b | h^{2n}(x) = x⟩, h: a ↦ ab, b ↦ a (h² = c_{aba}∘φ′, aba = (a⁻¹b⁻¹) φ′(a⁻¹b⁻¹)⁻¹).

`verification/presentations_h1_all_characters.py` (record `presentations_h1_all_characters_run.txt`): the three Fox
matrices give the same h¹ on **every** character of H₁(Y_n) for n = 2 … 9, exactly modulo two primes ≈ 10⁹ — counts 0, 3, 0,
20, 27, 56, 0, 147, equal to B1301's exact supports. (A first run with one prime ≈ 60 over-counted Y₇ by 28 and Y₉ by 36:
a rank read modulo one small prime can vanish accidentally. The criterion's two-prime rule is not optional.)

**Two benches (2026-09-09).** Main's B1306 slice A re-derived the criterion independently — the full Fox Jacobian on the explicit words
φⁿ(a), φⁿ(b) at every non-trivial character of Y₃ … Y₉, two primes — and found the same supports 3, 0, 20, 27, 56, 0, 147, rank J ≤ 1
everywhere, this branch's factorised product equal to J + I at every character, det(J + I) = 1 at all 9 324 characters, Y₂₀'s 41-part
empty and Y₂₄'s 2-primary support equal to Y₁₂'s. It also met the one-prime false zeros (84 at Y₇, 183 at Y₉) before applying two primes.
