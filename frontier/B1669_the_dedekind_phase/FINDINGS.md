# B1669 — THE DEDEKIND PHASE: the weave's parameter-free Yukawa sector has no hierarchy (m₂/m₁ ≥ ½ for every τ, from B1636's sum rule) and no Cabibbo angle, and on the ruled branch the strong CP angle is π·Re τ (the determinant of every T⊗T coupling is η⁶ times a level-one form)

**Verdict: PROVED as sealed, a census informed by its own draft.** Every cell C0, N8a, N8b, N10a, N10b, N10c held; every
threshold had been set after the referee's own computations and one smoke test of the sealed instrument (§0b), so the
seal certifies the statements and identities as asserted, not a blind prediction. The referee lane, 2026-10-17.
- Sealed `20ed2c300` (instrument sha256 in `ARTIFACT_HASHES.txt`) before the run; the output committed unread; the
  instrument unchanged since the seal. **0 of 19.** POINT_REGISTER P-192.
- **What is B1636's and what is new.** The sum rule m₁ = m₂ + m₃ for every off-diagonal coupling is B1636's theorem;
  this arc proves it symbolically (e₁² = 4e₂ for the eigenvalues of YY†, every complex a, b, c) and draws the corollary
  that no parameter-free sector of the triplet has a hierarchy at any τ. The determinant identities and the phase law
  (N10) are new to the record. The dimension table reproduces B1635's by piece.

## 0. Seen first

`VERDICT topic-sweep /weight[- ]1\b|weight one|zero diagonal|zero-diagonal|half floor|dedekind phase|det(erminant)? of the (yukawa|coupling)|strong cp|theta.bar|vector-valued modular|theta multiplier|M_k\(/: 11 of 1440 arcs on main match (NEGATIVE 1, PROVED 10)`
— B1634 (the weave's lift is the multiplier of η²¹(θ₂², θ₃², θ₄²); χ_{3/2} = 0), B1635 (the dimension table by piece
for k = 1..11; the lowest coupling golden at i; the free-number count), B1636 (the golden spectrum on the tick's
geodesic; m₁ = m₂ + m₃ for every off-diagonal coupling; the weight-1 coupling is the three theta constants placed
off-diagonal), B1640 (the record's hand allows the symmetric weight-1 coupling, the conjugate hand does not; T̄⊗T not
degenerate at ω), B1660 (one Higgs at ω excluded on 54 cells), B1246 (I-18: the type dictionary reaches θ, not θ̄).
**Literature:** Feruglio, Parriciatu, Strumia, Titov 2024 (arXiv:2406.01689) and Penedo, Petcov 2024 (arXiv:2404.08032)
— θ̄ = 0 from modular invariance needs determinants of weight zero, hence reducible representations with unequal
weights; the Zee texture and its exclusion by θ₁₃; the Dedekind η multiplier (12·arg η(x+iy) = πx + O(|q|)).

## 0b. Disclosed

Every number was computed by the referee before the preregistration (`reports/referee_lane_2026-10-17/`, scripts
check5–check7 and check10) and the sealed instrument was smoke-tested once with 160 fit starts
(`before_the_seal/smoke_run.txt`); the sealed run uses 100 starts with the same seed and the same deterministic
identities. No cell is blind. The fits use Huang–Zhou's M_Z masses, not B1668's PDG-2024 running; the floors are three
orders of magnitude above any difference that could make. The referee's first proof of the floor (a Perron-root
argument) is replaced by the corollary of B1636's sum rule.

## 1. The sealed run (`verification/the_dedekind_phase.py`, unchanged; `.json`, `_run.txt`)

| cell | prediction | result |
|---|---|---|
| **C0** plumbing | image order 96, s² = (st)³, s⁴ = −1, exponents (1/8, 3/8, 7/8); B1635's table by piece; B1636's golden spectrum at i | **HOLDS**: 96; true; true; (0.125, 0.375, 0.875); D 0,0,1,1,2,2 / O+ 1,1,2,2,3,3 / O− 0,1,1,2,2,3 for k = 1..11 exactly; (φ⁻¹, φ⁻²) at i to 10⁻⁹ |
| **N8a** the sum rule and the floor | e₁² − 4e₂ = 0 symbolically; random and grid floors ≥ ½; (½, ½) at ω; the closed form | **HOLDS**: symbolic 0; max |s₁−s₂−s₃|/s₁ = 1.2·10⁻¹⁵ and min s₂/s₁ = 0.5006 on 200 000 random matrices; grid min 0.5124 (the grid misses ω by 0.03); at ω (0.500000000, 0.500000000); closed form to 1.7·10⁻¹⁴ |
| **N8b** one form per sector | dim M₁(ρ̄⊗ρ̄) = 1; dim M₀(ρ̄⊗ρ) = 1 and the identity | **HOLDS**: 1; 1, identity to 4·10⁻¹⁶ |
| **N10a** the determinants | det Y₁/η⁶, det(Y_s + rY_a)/(η⁶E₆), det(A + rB)/E₆ constant over five τ to 10⁻⁷ | **HOLDS**: spreads 4.8·10⁻⁹, 1.4·10⁻⁹, 3.8·10⁻¹⁵ |
| **N10b** the phase law | |12·arg η − πx| < 10⁻⁴ for Im τ ≥ 2.5; |arg E₆| < 10⁻⁹ for Im τ ≥ 4.5 | **HOLDS**: 1.8·10⁻⁶; 2.6·10⁻¹⁰ |
| **N10c** the lowest fittable models | χ² > 500 for T⊗T at weight 3, T̄⊗T at weight 2, and the latter with Im τ ≥ 4.5 (100 starts each) | **HOLDS**: 4.2·10³, 3.4·10⁴, 3.4·10⁴ (the values are in the JSON) |

Read-outs: dim M_k(ρ̄⊗ρ) = 1, 2, 4, 5 at k = 0, 2, 4, 6 (D 1,1,2,2; O+ 0,1,2,3; O− 0,1,2,3); the weight-1 form as a
Majorana texture with the charged leptons diagonal: θ₁₃ = 9·10⁻¹¹ and 8·10⁻⁹ degrees on Re τ = ½ (Im τ = 2.5, 3.5),
6·10⁻⁵ and 9·10⁻⁴ off it; θ₂₃ = 45.0°, θ₁₂ = 44.2–44.8° — the Zee texture, bimaximal, inverted; the floor's maximum
0.99984 toward the cusp (the two heavy masses degenerate there).

## 2. What it means

- **N8.** The two parameter-free sectors of the triplet — the symmetric weight-1 coupling c·[[0, θ₄², θ₃²], [θ₄², 0,
  θ₂²], [θ₃², θ₂², 0]] for L, R ∈ T and the identity for R ∈ T̄ — have m₂/m₁ ≥ ½ for every τ (equality at ω, where
  the spectrum is (1, ½, ½); (1, φ⁻¹, φ⁻²) at i), because m₁ = m₂ + m₃ ≤ 2m₂; and with one form per sector M_u ∝ M_d
  and V = 1. B1660's negative at ω is one point of this theorem. The data need m₂/m₁ ≤ 0.06 and θ_C = 13°. The first
  free numbers enter at weight 3 (one complex ratio per sector, B1635's count) and still miss by three orders of
  magnitude in χ² (N10c); the triplet begins to fit at weight 5 with four coefficients per sector, which is ordinary
  modular model building.
- **N10.** With L, R ∈ T, det(ρ̄Yρ̄ᵀ) = (det ρ̄)² det Y and (det ρ̄)²(t) = e^{−2πi·22/8} = i = χ_η(t)⁶; a character of
  Mp₂(ℤ) is fixed by its value on t, so det Y has character χ_η⁶ and det Y/η⁶ is a level-one form (constant at weight
  1, E₆ at weight 3). Hence θ̄ − θ_QCD = arg(c_u c_d) + 12·arg η(τ) + arg(f_u f_d), and 12·arg η(x+iy) = πx to 10⁻⁵ for
  Im τ ≥ 2.5: **on the ruled branch the strong CP angle is the Dedekind phase of the modulus**, and θ̄ < 10⁻¹⁰ puts τ
  on the imaginary axis to that precision, where every form is real and δ_CKM = 0. With R ∈ T̄ the determinant is a
  level-one form (E₆ at weight 2) whose phase is 504·e^{−2π Im τ} sin 2πx — below 10⁻¹⁰ for Im τ ≳ 4.7 — but the same
  limit makes the weight-2 forms diagonal plus off-diagonal of order e^{−π Im τ/2}, degenerating the masses pairwise
  and sending J to zero (the fit at Im τ ≥ 4.5: χ² = 3.4·10⁴, J ≈ −10⁻¹⁰). The irreducible three cannot have θ̄ = 0
  together with δ_CKM ≠ 0 at tree level on this branch; the literature's escape needs reducible representations with
  unequal weights, i.e. giving up the three. I-18 is sharpened: the ansatz reaches θ̄, as π·Re τ.
- **On the price ledger (B1668)** the weave's structure enters with zero rows bought.
- **What it cannot show:** that the modular ansatz is nature's; that I-33 (singular values = masses) is earned; any value.

## 3. Files

`verification/the_dedekind_phase.py` (sealed 20ed2c300), `.json`, `_run.txt`; `before_the_seal/`; the lock
`tests/test_b1669_the_dedekind_phase.py`.
