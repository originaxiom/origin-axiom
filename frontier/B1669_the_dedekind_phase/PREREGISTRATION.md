# B1669 — THE DEDEKIND PHASE (the parameter-free Yukawa sector of the weave's triplet has no hierarchy and no Cabibbo angle for any τ, and on the ruled branch the strong CP angle is the phase of the modulus): preregistration

The referee lane, 2026-10-17. POINT_REGISTER P-192. 0 of 19.

- **The question.** B1635 counted the couplings of the triplet T on the ruled branch under the holomorphic modular
  ansatz (forms for ρ̄⊗ρ̄ and ρ̄⊗ρ, by piece and weight), B1636 found the lowest symmetric coupling's golden spectrum on
  the tick's geodesic and proved that every off-diagonal coupling obeys m₁ = m₂ + m₃, and B1660 excluded one Higgs at
  τ = ω against the data. Two statements about the same objects remain to be made and banked: (N8) for *every* τ the
  parameter-free sector — one form at weight 1 for T⊗T, one at weight 0 for T̄⊗T — has m₂/m₁ ≥ ½ and no Cabibbo angle,
  so B1660's negative at ω is one point of a theorem; and (N10) the determinant of every T⊗T Yukawa form is η⁶ times a
  level-one form, so that with CP-real coefficients θ̄ = π·Re τ on the ruled branch: the strong CP angle is the Dedekind
  phase of the modulus, and θ̄ < 10⁻¹⁰ puts τ on the CP-conserving axis where δ_CKM = 0. For T̄⊗T the determinant is a
  level-one form (∝ E₆ at weight 2), exponentially real toward the cusp, but the same limit degenerates the masses.
- **The frame.** The paper's convention (Theorem 9; B1634's hand): ρ = χ_η²¹ ⊗ ρ_u on (θ₂², θ₃², θ₄²); couplings
  L^T Y R with L, R ∈ T are forms for ρ̄⊗ρ̄ (weight k odd), with R ∈ T̄ for ρ̄⊗ρ (k even); the Higgs a singlet of the
  modular group; the dictionary of I-33 (singular values = masses, U_u†U_d = V_CKM) *assumed*, as in B1635 and B1660.
  Nothing here is a value; the arc's content is what the ansatz cannot do.

## 0. Seen first

`VERDICT topic-sweep /weight[- ]1\b|weight one|zero diagonal|zero-diagonal|half floor|dedekind phase|det(erminant)? of the (yukawa|coupling)|strong cp|theta.bar|vector-valued modular|theta multiplier|M_k\(/: 11 of 1440 arcs on main match (NEGATIVE 1, PROVED 10)`
— read in full: B1634 (the multiplier of η²¹(θ₂², θ₃², θ₄²) as the weave's lift; χ_{3/2} = 0), B1635 (the dimension
table by piece D, O+, O− for k = 1..11: 0,0,1,1,2,2 / 1,1,2,2,3,3 / 0,1,1,2,2,3; the lowest coupling at i golden; the
count 2 + Σ(2d−1)), B1636 (the golden spectrum on the tick's geodesic; m₁ = m₂ + m₃ for every off-diagonal coupling,
"a theorem"; post seal: the weight-1 coupling is the three theta constants placed off-diagonal), B1640 (the frame
audit: the record's hand allows the symmetric weight-1 coupling, the conjugate hand does not; T̄⊗T non-degenerate at
ω), B1660 (the one-Higgs census at ω: excluded on 54 cells), B1246 (I-18: the type dictionary reaches θ, not θ̄). **What
is new here:** the half floor as a corollary of B1636's sum rule, proved symbolically and holding for every τ (B1635 and
B1636 found the spectrum at ω, at i and on one geodesic); the vanishing Cabibbo angle of the parameter-free sector;
the determinant identities and the phase law (N10), which no arc states; and the χ² floors of the lowest fittable
models with τ free (B1660 fixed τ = ω and the eighteen flat lines). **Literature:** the strong CP solution by modular
invariance with determinants of weight zero — Feruglio, Parriciatu, Strumia, Titov 2024 (arXiv:2406.01689) and
Penedo, Petcov 2024 (arXiv:2404.08032), whose escape needs reducible representations with unequal weights; the Zee
texture (zero-diagonal Majorana matrix; bimaximal mixing) and its exclusion by θ₁₃; Dedekind's η multiplier and the
Rademacher function (the phase 12·arg η(τ) ≡ π·Re τ + O(|q|)).

## 0b. Disclosed

- **The referee computed every number below before this preregistration** (reports 01 and 03 of
  `reports/referee_lane_2026-10-17/`, scripts `check5`–`check7`, `check10`), and **the sealed instrument was smoke-tested
  once** (`before_the_seal/smoke_run.txt`); the instrument is deterministic (fixed seeds), so the sealed run reproduces
  the smoke test. Every threshold is set after seeing. **No cell is blind**; the verdict is graded as a *census informed
  by its own draft* and says so. What the seal protects: the statements, the identities asserted, the thresholds.
- **The sum rule is B1636's theorem, not this arc's**; this arc proves it symbolically (e₁² = 4e₂ for the eigenvalues
  of YY†, every complex a, b, c) and draws the corollary m₂/m₁ ≥ ½. The referee's own first proof (a Perron-root
  argument) is weaker and is not used.
- **The fits use Huang–Zhou's M_Z masses** (as the referee's draft did), not B1668's PDG-2024 running; the floors are
  three orders of magnitude above any difference that could make.

## 1. The cells

| cell | prediction | kind |
|---|---|---|
| **C0**, plumbing | ρ built from the formula has image order 96, s² = (st)³, s⁴ = −1, exponents (1/8, 3/8, 7/8); B1635's dimension table by piece reproduced exactly for k = 1..11; B1636's golden spectrum (1, φ⁻¹, φ⁻²) at i to 10⁻⁹ | gate |
| **N8a**, the sum rule and the half floor | symbolically e₁² − 4e₂ = 0 for the generic zero-diagonal complex symmetric 3×3 matrix; on 200 000 random such matrices max |s₁ − s₂ − s₃|/s₁ < 10⁻¹² and min s₂/s₁ ≥ ½; on a grid over the fundamental domain (81 × 160, Im τ ≤ 6) the weight-1 form's m₂/m₁ ≥ ½; at ω exactly (½, ½); the closed form c·[[0, θ₄², θ₃²], [θ₄², 0, θ₂²], [θ₃², θ₂², 0]] to 10⁻¹⁰ | test (informed) |
| **N8b**, one form per parameter-free sector | dim M₁(ρ̄⊗ρ̄) = 1 and dim M₀(ρ̄⊗ρ) = 1, the latter the identity to 10⁻¹⁰ — hence M_u ∝ M_d and V_CKM = 1 in every parameter-free sector | test (informed) |
| **N10a**, the determinants | det Y₁/η⁶, det(Y_s + rY_a)/(η⁶E₆) for three r, and det(A + rB)/E₆ for the weight-2 Dirac forms are constant over five τ to a relative spread below 10⁻⁷ | test (informed: 5·10⁻⁹, 1.4·10⁻⁹, 4·10⁻¹⁵) |
| **N10b**, the phase law | max over x ∈ [−½, ½], y ∈ {2.5, 3, 4} of |12·arg η(x+iy) − πx| < 10⁻⁴; max |arg E₆| at y ≥ 4.5 < 10⁻⁹ | test (informed: 1.8·10⁻⁶, 2.7·10⁻¹⁰) |
| **N10c**, the lowest fittable models | against the eight quark observables (four mass ratios, |V_us|, |V_cb|, |V_ub|, J; Huang–Zhou masses, PDG 2024 CKM), the best of 100 Nelder–Mead starts has χ² > 500 for each of: T⊗T at weight 3 (one complex coefficient per sector, τ shared), T̄⊗T at weight 2, and T̄⊗T at weight 2 with Im τ ≥ 4.5 | test (informed: 3.8–4.2·10³, 2.9·10⁴, 3.3·10⁴) |
| read-outs | the dimension tables; the weight-1 form's Majorana angles at four τ (θ₁₃ on Re τ = ½, θ₂₃); λ, the fit parameters; the floor's maximum on the grid | — |

**If C0 fails, nothing after it is read as a result.** Verdict rule: PROVED if N8a–N10c hold; NEGATIVE as sealed if any
fails, with the failing cell's reading. The verdict's first line says the cells are informed.

## 2. What it would mean

- **N8:** B1660's "one Higgs at ω is excluded" becomes "every parameter-free sector is excluded at every τ, with a
  floor of ½ on the second-to-third mass ratio and no Cabibbo angle" — a theorem on the ansatz, not a census. The data
  need m₂/m₃ ≤ 0.06 and θ_C = 13°. The first free numbers enter at weight 3, where N10c says the fits still fail by
  three orders of magnitude in χ²; the triplet begins to fit at weight 5 with four coefficients per sector (B1635's
  count), which is ordinary model building.
- **N10:** on the ruled branch the irreducible three cannot have θ̄ = 0 together with δ_CKM ≠ 0 at tree level: with L,
  R ∈ T the strong CP angle is π·Re τ up to the coefficients' phase, and with R ∈ T̄ its suppression toward the cusp is
  the same limit that kills the hierarchy and J. The literature's escape (weight-zero determinants) requires reducible,
  one-dimensional representations with unequal weights — giving up the three. I-18 (the record's type dictionary
  reaches θ, not θ̄) is thereby sharpened: the ansatz does reach θ̄, as a function of the modulus, and the function is
  the wrong one.
- **What it cannot show:** that the modular ansatz is nature's; that the dictionary I-33 is earned; any value.

## 3. Files

`verification/the_dedekind_phase.py` (sealed), with `the_dedekind_phase.json` and `_run.txt` after the run;
`verification/before_the_seal/smoke_run.txt`; the lock `tests/test_b1669_the_dedekind_phase.py`.
