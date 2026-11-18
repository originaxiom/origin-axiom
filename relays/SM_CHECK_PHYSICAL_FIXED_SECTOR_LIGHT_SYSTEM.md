# The SM seat's check of the fixed-sector light system: every finite step holds

The analytic core is not checked here.

*The SM seat, 2026-11-18. The packet is reports/physical_bridge_2026_09_05/fixed_sector_light_system_2026_11_16/ on
audit/physical-bridge-2026-09-05 at 798281903. Read in full: REVIEW_BRIEF.md,
COMPLETE_PHYSICAL_KERNEL_AND_CORE_CHARACTERS.md, COMPLETE_CUBIC_AND_GLOBAL_PAIRING_RANKS.md,
BALANCED_FORM_TANGENTS_AND_ACTUAL_MOMENT_CORRECTION.md, CUSP_GAUGE_INVERSE_AND_LOCAL_STATIONARY_BRANCH.md and
NEUTRAL_STATIONARY_FAMILY_AND_FULL_E8_PENCIL.md, with FINDINGS.md for context. This seat's own code, built from
scratch with nothing imported from the lane: `relays/sm_physical_check/check_fixed_sector_light_system.py`, output
`relays/sm_physical_check/check_fixed_sector_light_system.json` (41 checks, about 25 s). Its model is the principal
sl2 in so5, so5 + so5 in so10 in so16, and the 248 as the so16 adjoint plus a Clifford chiral spinor. No data; no
physical value.*

## The finite steps, checked

| | claim (packet) | check (this seat) | result |
|---|---|---|---|
| K1 | E^j ∈ so5 (j = 1, 3); T₍₃₎ ∝ (E†)³ lowest j = 3 | invariant form; E² ∉ so5; ad(J_z) = −3 | **holds** |
| K2 | A = (−iN)e^(−iπH/4): phase i at m = 2; Ad_A = i^(−m) swap | explicit 10 × 10 A, weights −3..3 | **holds** |
| K3 | (1): A_(±j) = i^(1∓j) σ_x | = Ad_A phase at m = w − 1 | **holds** (consistency) |
| K4 | j = 1: opposite phases; exponents 0, 2; no mode | characters with β₁ = −1; Riemann–Roch | **holds** |
| K5 | j = 3: w = +3 none; w = −3 two modes N_± | β₃ = +1; one pole, one section each | **holds** |
| K6 | (2,2) form: w = 4, S⁶L⁻¹, two poles, two sections | strict pole rule; Riemann–Roch | **holds** |
| K7 | charged forms: dim H⁰(S⁵L⁻¹(2p)) = 2; S¹ no pole | same | **holds** |
| K8 | cross element v₁∧v₂ has A-phase +1 | explicit wedge in Λ²(C¹⁰) | **holds** |
| K9 | 5 + 3 + 3 + 1 = 12; misaligned 9 + 1 | arithmetic | **holds** |
| C1 | only A S T, P N T, R N S; B pairs with nothing | enumerate weight 0, charge 0; pair sums 0, −3, −6 | **holds** |
| C2 | N·ψ_T lands in the two-pole P target | (1 − w₁) + (1 − w₂) = w + 2; 1 + 0 ≤ 2 | **holds** |
| C3 | (3): only N_(δ₊) couples P to T; α₋δ₋ = η | all sign cases of η, α₊ | **holds** |
| C4 | j = 3 element: one extreme entry on V_(3/2) | (E†)³ ∈ sp4; sole entry ⟨−3/2\|·\|3/2⟩ = 6 | **holds** |
| M1 | Y1 rank 2; values \|tλ₊ν_c\|, \|tλ₋ν_d\|; null pair | Y1 = ∂²W3 at A = 0, N = tν; null (P_s, R_s) | **holds** |
| M2 | S = T = N = 0: W3 is cubic-flat | symbolic gradient | **holds** |
| M3 | A, S, T only: y A S T | symbolic | **holds** |
| M4 | ∂_ρ h/t² = −2e_Q; m_Q² = 4e_Q²t² | symbolic | **holds** |
| T1 | (2): −i[a_x, a_y] = [a, a†]/2 | random Hermitian matrices | **holds** |
| T2 | (4): δA = (−D_yψ, D_xψ) gives δF = (D_x² + D_y²)ψ | symbolic, nonabelian 2 × 2 fields | **holds** |
| T3 | (4): spin part is −(ad_q†ad_q + ad_q ad_q†)ψ ≤ 0 | random q, Hermitian ψ | **holds** |
| G1 | exponents (1 ± √(1 + 4ℓ²c))/2 = −β_c, 1 + β_c | symbolic roots | **holds** |
| G2 | e^(−t)dt keeps 1, e^(−βt); drops e^t, e^((1+β)t) | integrals | **holds** |
| G3 | δ < β_c avoids resonance | resonance iff δ = β_c; none at c = 0 | **holds** |
| P1 | pencil ranks 180 (kernel 68), 148 (kernel 100) | numerical ranks on 120 + 128; sl2 counts | **holds** |
| E1 | roster 10 + 11·5 + 32·4 + 55·1 = 248 | E8 weights on the so5 Cartan | **holds** |
| E2 | at μ = iλ: Tr₁₀ X⁸ = 68, Tr₅ = 4, Tr₄ = 1/4 (·λ⁸) | symbolic | **holds** |
| E3 | Tr₂₄₈(ad X)⁸ = (15/2)(Tr₅X⁴)²; quartic trace 0 | symbolic; also modulo Tr₅X² | **holds** |
| E4 | Tr₅X² = 0, Tr₅X⁴ = 4a³b Tr(E³T₍₃₎) > 0 | char. poly x⁵ − (Tr₅X⁴/4)x; Tr = 288 | **holds** |
| E5 | (3) on actual matrices; b = 0 nilpotent | 248 matrices: 4877107.2 both sides | **holds** |
| E6 | complex-gauge response keeps trace and class | complex orthogonal conjugation | **holds** |
| N1 | [q₀′, v] = [r₀′, u] = [u, v] = 0; linear moment 0 | explicit so16 blocks | **holds** |
| N2 | D5 kernel 0; E6 centralizer is Q alone | so10: 0; chiral 16: 0; one triple: 10 | **holds** |

The strict pole rule used for K4–K7 is this seat's own reading of "strict cusp bound". A section of S^e with pole
order m at the cusp is q^(e/2 − m) times a power of Im z in the cusp frame, so it is bounded only for m < e/2 (or
m = e = 0). This gives max pole order ⌈e/2⌉ − 1 for e > 0. It reproduces every degree the packet states (0, 0, −,
1, 2, 2, 0 for e = 0, 2, −2, 4, 5, 6, 1).

## Planted countercontrols (each must fail, and each does)

| | plant | result |
|---|---|---|
| X1 | the cross-module phase with a symmetric product is +1 | **fails** (it is −1) |
| X2 | (3) and the quartic cancellation survive without the 32 spinor fours | **fails** |
| X3 | flipping the sign of ∂_t² gives the same exponents | **fails** |
| X4 | a non-strict pole bound (m ≤ e/2) still gives one section of S⁴L_δ | **fails** (it gives two) |
| X5 | the single-triple pencil kernel is 68 | **fails** (it is 100) |

## Reading

- Every finite statement this seat could compute holds. These are the swapped D5 core phases, the exterior sign,
  the channel selection, the polarization coefficient, the extreme spinor element and the rank-two mass matrix. They
  also include the 248 roster, the eighth-power identity, the quartic cancellation and the 68/100 kernels.
- No claim failed. During development one check (T3) failed because of an elementwise-product bug in this seat's
  own code, not in the packet. After the fix it holds.
- The E8 facts are checked twice: from the weights, and from explicit 248-dimensional matrices.
- K3, K4 and K5 take β_j = (−1)^((j+1)/2) for D = G(Fk) as given. This seat could not derive those phases from the
  stated Fk = diag(i, −i) without the source's slot conventions. The j = 1 "no zero mode" result rests on that
  premise.
- The packet's load-bearing claims are its analytic ones: the weighted cusp inverse (3), the two implicit-function
  steps and the D-flat completions. None is checked here, so the stationary families stay conditional.

## Not checked here

- The β_j values of D = G(Fk), and the Fi/Fk flavour matrices themselves.
- The orthogonal domain reduction, the positive gap of the algebraic complement, and the physical slot densities.
- The source normalizations: y, λ_± as literal integrals, the Ω^(−3/2) representatives, the Hodge density Ω⁻³, the
  one-half connection density and e_Q.
- The equality of the two polarized coefficients C in the cubic. Only the resulting selection (3) is checked.
- The identification L_δ L_η = L_top,+⁻¹ and the top character.
- The E6 kernel claim that P_v = 2k†k has kernel Q. Only the finite centralizer fact behind it is checked.
- The essential-spectrum bound and the closed range of P_v.
- The zero-angular shift w²/(4ℓ²), and the domination of the exp(t) drift by the exp(2t) term.
- The weighted Hölder spaces, the lifted Schauder estimates on the shrinking circle, and the bijection (3) with its
  bounded inverse.
- The real-analyticity of the moment map into Y_δ, the projection (5), both implicit-function theorems and the
  removable t² division.
- The full O(ε³)/O(ε⁶) remainder in (7), global transitions and reflection equivariance of the responses.
- The higher-order coefficient Y2 (V2 and the charged complementary inverse), which the packet itself leaves
  unevaluated.
- Source completeness (SOURCES.json), and every global, external-space, three-family or gravitational statement.
