# The SM seat's check of the physical lane's four-form register: every finite claim holds

*The SM seat, 2026-11-18. The source is reports/physical_bridge_2026_09_05/four_form_register_2026_11_17/ on
audit/physical-bridge-2026-09-05 at 798281903 (PHYSICAL-C7). Read in full: README.md, REVIEW_AND_DISCRIMINATORS.md,
FOUR_FORM_QUOTIENT_AND_CONNECTION.md, BASED_REGISTER_AND_RELATIONAL_REFERENCE.md,
INTERNAL_COMPOSITE_REGISTER_AND_WORD_ACTION.md, CONSTRAINED_PHASE_RESPONSE_FROM_SAME_KINETIC_ACTION.md,
NONLINEAR_FAMILY_AND_COMPLETE_DOMAIN.md and FULL_E8_LIFT_AND_PHYSICAL_END_DUTY.md. The packet's review brief asks for
an independent check, and this is it, run on this seat's own code while that lane is not running:
`relays/sm_physical_check/check_four_form_register.py`, output in
`relays/sm_physical_check/check_four_form_register.json`. Nothing of the lane's is imported or run. No data.*

The script makes 79 checks: 68 claims and 11 plants that must fail. All 79 come out as expected, in about 5 seconds.
"rnd n" means n seeded random points, and the residual is the largest seen. Numbers like (5) are the equation numbers
of the note concerned. "Item" means a numbered duty in REVIEW_AND_DISCRIMINATORS.md.

## Quotient, Gauss connection, primitive period (items 1 to 3)

| claim | check | result |
|---|---|---|
| (3) invariants of charges (+,+,−,−) are the Z_ij; det Z = 0 is the only relation | Groebner elimination | holds |
| same: invariant and C[Z]/(det) Hilbert functions agree, (d+1)² | degrees 1 to 6 | holds |
| a rank-one Z has a balanced factorization, \|λ\|⁴ = ‖R‖²/‖P‖², unique up to the circle | rnd 200 | 3e-15 |
| smooth part of complex dimension 3; vertex only from P = R = 0 | ∇det, rnd 20; vertex by hand | holds |
| plant: a rank-two point, or the truncation (P₁, R₁), gives the same quotient | det(PRᵗ) ≡ 0; dim 1 | **fails** |
| (4)-(6) N b² − 2bJ + K; b = J/N; metric ‖dP‖² + ‖dR‖² − J²/N | symbolic | exact |
| plant: a plus sign on the negative charge in J | another minimiser | **fails** |
| A → A + dφ under a local phase; the metric is unchanged | rnd 50 | 2e-14 |
| nonorthonormal coordinates with Grams transported: the same A | rnd 50 | 2e-16 |
| plant: the same coordinates without the Grams | off by 1.46 | **fails** |
| (7) A₀ = (a_u − a_v)/2 and ds² = 2dt² + t²[\|du\|² + \|dv\|² − (a_u − a_v)²/2] | rnd 200 | 1e-14 |
| plant: (7) without the radial 2dt² | off by 19 | **fails** |
| (9) Kähler potential 2√tr(ZZ†), in the \|dP\|² convention | complex Hessian, rnd 20 | 2e-15 |
| plant: the Ricci-flat (tr ZZ†)^(2/3) gives the same metric up to a constant | ratio spread 0.75 | **fails** |
| (10) on v = ū: a_ū = −a_u, A_N = sin²(θ/2)dφ, F = ½ sin θ dθ∧dφ, ∫F/2π = 1 | symbolic | exact |
| A_S = A_N − dφ regular at θ = π; the transition winds once; Z = t²uu† | symbolic | exact |
| plant: one Hopf term, A = a_u/2, has period 1 | gives ½ | **fails** |
| (11) latitude holonomy exp[−iπ(1 − cos θ₀)], varying continuously | symbolic | exact |
| (13) E ≥ length²/L, with equality at constant speed | one discretised path | 2e-9 |

## Based register and reference (BASED_REGISTER_AND_RELATIONAL_REFERENCE.md)

| claim | check | result |
|---|---|---|
| (1) U(u) ∈ SU2, U(e^{iφ}u) = U(u)D_φ; i = U(i,0), j = U(0,1) are quaternions | rnd 50 | 6e-16 |
| (2)-(3) A_φ = −sin φ + i cos φ, B_φ = j cos φ + k sin φ | 13 values of φ | 2e-16 |
| same: tr[A_φ, B_φ] = 2 − 4cos²φ (−2 at 0, 2 at π/2); Z unchanged | 13 values of φ | 2e-16 |
| (4)-(5) A_reg, B_reg invariant with ζ carried; they are U(ζ⁻¹u), U(ζv) | rnd 50 | 4e-16 |
| plant: an untransformed reference leaves A_reg invariant | off by 1.97 | **fails** |
| (6)-(6a) b = (J + ν²dχ)/(N + ν²); g_quot + [Nν²/(N + ν²)](dχ − A)²; limits 0, N | symbolic | exact |
| (7) F_{N_d} ∋ λ₋R_cS and F_{N_c} ∋ λ₊P_cT for the stated W₃ | symbolic | holds |
| (8) the shear's derivative at (I, I) is (X, Y) → (X, X + Y) | central difference, rnd 20 | 2e-9 |
| (8) every invariant symmetric form is degenerate; the n-th power is (X, nX) | invariance equations | holds |
| § 6 control: ‖Y − τX‖²/Im τ is invariant under τ → τ + 1, Y → X + Y | symbolic | exact |

## Internal composite (INTERNAL_COMPOSITE_REGISTER_AND_WORD_ACTION.md, items 9 to 11)

| claim | check | result |
|---|---|---|
| (1) A = UJU⁻¹ and W = UC⁻¹ are gauge-invariant; A² = −I, tr A = 0, W ∈ SU2 | rnd 100 | 1e-15 |
| (2) any lift of A, with C = W⁻¹U, returns (u, v) up to the opposite phase | rnd 100 | 6e-16 |
| § 2 identity: \|α\|² + \|α − β\|² − (2α₃ − β₃)²/2 = 2\|α⊥ − β⊥/2\|² + \|β\|²/2 | symbolic | exact |
| § 2 intermediates: a_u = α₃, a_v = β₃ − α₃, ⟨A, k⟩ = β₃, ‖DA‖² = 4\|α⊥ − β⊥/2\|² | rnd 200 | 1e-14 |
| (4) ds² = 2dt² + (t²/2)(‖DA‖² + ‖k‖²); (5) A_phase = a_u − ⟨A, k⟩/2 | rnd 200, vs. the source | 3e-14 |
| plant: the product metric without the cross term (dA for DA) | off by 44 | **fails** |
| on v = ū, W = I and tr[A, W] = 2 | rnd 20 | 5e-16 |
| (8) tr[A, W] = 2 − 4(\|w\|² − (n·w)²), within [−2, 2] | rnd 500 | 2e-15 |
| (9)-(10) v → iv gives (A, AW) and keeps metric and connection; T⁴ = id, T² ≠ id | rnd 100 | 1e-15 |
| W = −A: the other move sends A to I, of trace 2 | direct | holds |
| (11) G = cos θ + sin θ A, θ = 2 arctan(t/t₀), inverted; (G, B) → (G, GB) is v → e^{iθ}v | rnd 100 | 9e-15 |
| (13) Δg = t²θ′dt(a_u + a_v) + (t²/2)θ′²dt²; a pure radial tangent detects it | rnd 100 and one case | 9e-15 |

## Constrained phase, nonlinear leading terms, E8 centre (items 12, 4, 7, 8)

| claim | check | result |
|---|---|---|
| (1) E = E_horizontal + N(b − a)² | symbolic | exact |
| (2)-(4) minimum Δ²/R at b* = a + Δ/(RN); constant current 2Δ/R = dΓ/dβ | KKT, 2000 cells, rnd N | 2e-15 |
| (5) sewing: equal ratios; extra Γ = (β − I₁ − I₂)²/(R₁ + R₂); free β gives 0 | symbolic | exact |
| plant: harmonic weighting (R₁ + R₂)/(R₁R₂) is the minimum | it is not | **fails** |
| nonlinear (3), (5), (10): Z is λ-invariant; ∂_λ(h/t²) = 4e_Q at 0; circle tangent norm 2t² | symbolic | exact |
| E8: 240 roots; Q = (2/3)(e₁ + e₂ + e₃) has charges 0, ±1/3, ±2/3, ±1 **and ±4/3** | enumeration | see reading |
| (1) period 6π; z₃ ≠ 1, z₃³ = 1, z₃ = 1 on ±1; 3Q is in the lattice, Q is not | exact | holds |
| (2) c₁(eff) = 3c₁(full): a c₁ = 1 effective bundle needs full degree 1/3 | winding of θ → 3θ | holds |
| (3)-(5) the four has Q = +1, −1/3 (×3); diag(e^{iφ}, e^{−iφ}, 1, 1) has det 1 and closes | exact | holds |
| plant: the pure-Q transition exp(iφQ) closes at 2π | ends at diag(1, z₃, z₃, z₃) | **fails** |
| § 5: a common scale leaves A; ω = dΘ; Θ(iP, −iR) = 0; Θ = t²(a_u + a_v), 0 on v = ū | symbolic, rnd 100 | 2e-15 |

## Reading

- **No failure.** Every finite identity, dimension, connection, curvature, trace and E8 statement in the seven notes
  holds as written. Each of the brief's rejections is built as a plant that fails in its stated direction:
  - plus sign;
  - half Hopf unit;
  - untransformed reference;
  - missing cross term;
  - wrong sewing weight;
  - pure-Q lift;
  - two-mode truncation;
  - rank-two point.

  This seat added three plants of its own, which also fail:
  - Gram-free coordinates;
  - a dropped radial term;
  - the Ricci-flat potential.
- **One small incompleteness, not an error.** FULL_E8_LIFT_AND_PHYSICAL_END_DUTY.md § 1 says the E8 roster "also
  contains charges +/-1/3 and +/-2/3". The six roots ±(e_i + e_j) with i, j ≤ 3 also carry ±4/3. This changes
  nothing: exp(6πiQ) kills them and z₃ moves them.
- **Conventions are this seat's choices,** and they agree with every displayed formula:
  - the matrix U(u) and the quaternions i = U(i,0), j = U(0,1);
  - the su2 basis, with J = diag(i, −i);
  - the standard even E8 coordinates.
- **One check failed on this seat's side first.** The Nielsen-derivative check first used a forward difference with
  too tight a tolerance, and failed at 1e-5. Rerun as a central difference, it holds at 2e-9. The claim was not at
  fault.

## What is NOT checked

- **Analytic premises,** which the packet takes as given:
  - the P-C3e weighted Banach inverse and its estimates;
  - joint analyticity in (u, v, λ);
  - both implicit-function steps and their uniformity in direction (item 4);
  - the off-Q gap of the full gauge connection, the O(t²) cross block, the O(t⁴) Schur term and A_t = A₀ + O(t).
    Item 5 is checked only at its leading norm 2t²;
  - the fermion domain and the bounded perturbation (13) (item 6);
  - the dual-zero-mode argument that nothing cancels λ₋R_cS.
- **Steps done by hand or quoted:**
  - π₁(Y) = 0, π₂(Y) = Z and H₂ = Z. Only the action's freeness is argued, in one line;
  - the primitivity of v = ū in π₂. Only the winding of its transition is computed;
  - that diag(e^{iφ}, e^{−iφ}) contracts in SU2;
  - that there is no global phase over a c₁ = 1 sphere;
  - that A_t − A₀ is basic and keeps the period (12);
  - the integer (6) for a map f;
  - the radial chart's vertex limits;
  - the change of variables (12).
- **Physical interpretations,** none assessed, and none claimed by the packet:
  - that these four coefficients, kinetic term and charges are the lane's physical form modes;
  - the SU2 coefficient category and the coefficient-to-group frames;
  - native word moves as physical operations;
  - any end map, carrier, index, state selection, history weight, colour flux or three-family statement.
