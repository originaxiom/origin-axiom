# W148 — a non-authoring review on own code of the audit lane's two P-210 notes: the symmetric state's Green response and its grading (82c772eb5), and the exterior gap and its thresholds (3ee8f33d0) (the rule, committed before the script)

The SM-derivation seat, 2026-10-24. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **The audit lane's relays** (PHYSICAL_TO_MAIN_SM_CHAT1_2026-10-24_P210_GREEN_RESPONSE and
  ..._P210_EXTERIOR_GAP, rowed in RELAY_LEDGER at f0d05a9b4) ask for independent review. Both notes say no code was
  run and name their own verification duties: the null-plane and Cayley identities, the Γ test, the Q8 commutants,
  the projector path, the contraction (9); and (1)–(6) of the exterior note with its wrong-sign controls.
- **This seat reviewed the lane's earlier checkpoints in W144** (every one held on own code).
- **The owner approved this in order** ("lets go for all systematically", 2026-10-24).

## The objects

- **The first note** (SYMMETRIC_STATE_GREEN_RESPONSE_AND_GRADING.md at 82c772eb5), its equations (1)–(9):
  - the Green form G = u†v′ + v†u′ on W ⊕ W, W = ℂ³ ⊗ ℂ²;
  - a = (u + v)/√2 and b = (u − v)/√2;
  - the maximal null planes b = Ua with U ∈ U(6);
  - the Q8 action I₃ ⊗ ρ(h) on both slots, and the commutant C ⊗ I₂;
  - the grading Γ(u, v) = (u, −v), and the plus trace ker(C − I) ⊗ ℂ² with index 2r − 3;
  - the Cayley chart v = iHu, U = (I − iH)(I + iH)⁻¹;
  - H₂(S) = SS† − tr(SS†)I₂/2 and the planes (8);
  - the path S_t = (I₂ + t n·σ)^{1/2} and its projector;
  - the contraction Y_ab = tr(C_aᵀεC_bε) = −2δ_ab with (C₁, C₂, C₃) = (j, i, k).
- **The second note** (P210_EXTERIOR_GAP_AND_THRESHOLD_DUTY.md at 3ee8f33d0), its (1)–(6):
  - D_K = −iσ₁∂_t − σ₂ ⊗ K, with Γ = diag(I₆, −I₆), and its boundary current;
  - the zero-energy solutions u = e^{−tK}u₀ and v = e^{tK}v₀;
  - the L² plane L_ext(K) = E₊(K) ⊕ E₋(K);
  - the Q8-commuting K_* = A_* ⊗ I₂, and Weyl's eigenvalue bound;
  - the comparator K(S) = I₃ ⊗ H₂(S), and the threshold at S = I₂;
  - the far-tail sequence f_L, with ‖f_L‖ = 1 and ‖D₀f_L‖² = L⁻²∫∣χ′∣²;
  - K = ±mI₆ and the two extremes.
- **The own code:** sympy for the identities, and numpy and mpmath for the random and path checks.
  - The quaternion matrices are W144's, i = diag(i, −i), j = [[0, 1], [−1, 0]] and k = ij, with a second basis
    −iσ_x, −iσ_y, −iσ_z.
  - None of the lane's code is run; it has none for these notes.

## Weave or thread

**A review of another seat's algebra at one fixed state.** Neither a weave result nor a thread result: the claims are
about the two notes' statements.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| G1 | **The Green form and its null planes.** G = a†a′ − b†b′ (sympy, exact). On 200 random U ∈ U(6) the graph b = Ua is null to 10⁻¹² and its projection to a has rank 6. On 200 random null six-planes given by a random non-orthonormal basis (P; Q) with P†P = Q†Q, the projection to a is injective and QP⁻¹ is unitary to 10⁻¹². Each such plane is its own G-orthogonal complement (dimension 6), so no null plane is larger | 97% |
| G2 | **The Q8 commutant.** In both bases the commutant of I₃ ⊗ i and I₃ ⊗ j in M₆(ℂ) is exactly M₃(ℂ) ⊗ I₂ (dimension 9, exact rank). A Q8-invariant graph has U = C ⊗ I₂ with C ∈ U(3) | 99% |
| G3 | **The grading.** Γ exchanges a and b. On 200 random C ∈ U(3) that are not involutions, the graph of C ⊗ I₂ is not Γ-invariant (by at least 10⁻³). On the Hermitian involutions of each rank r = 0, 1, 2, 3 it is, its plus trace has dimension 2r, and 2r − 3 runs over {−3, −1, +1, +3} | 98% |
| G4 | **The Cayley chart.** On 200 random Hermitian H on W, v = iHu is null to 10⁻¹², U = (I − iH)(I + iH)⁻¹ is unitary, and its graph is the same plane. Q8-covariant H are exactly A ⊗ I₂. H = hI₆ gives a one-parameter family through v = 0, and U = −I lies outside the chart | 98% |
| G5 | **The projector path and the planes (8).** H₂(S_t) = t n·σ (sympy, symbolic t and unit n). The projectors I₃ ⊗ (I₂ ± n·σ)/2 for n and −n are orthogonal, with operator-norm distance 1, at every t. The planes (8) tend to v = 0 and to u = 0 as t → 0. They are covariant under S ↦ gS and under S ↦ gSg† for random g ∈ U(2). Off S = I₂, with η ≠ 0, they are not Γ-invariant (their Cayley U has U² ≠ I) | 95% |
| G6 | **The contraction (9).** C_aᵀε = −εC_a, (ε⁻¹)ᵀ = ε, and Y_ab = Σ_mn (C_aᵀεC_b)_mn(ε⁻¹)_mn = tr(C_aC_b) = −2δ_ab, exactly in both bases (sympy) | 95% |
| E1 | **The constant-tail operator.** With ∂_t replaced by a symbol, D_K equals the block form (1) exactly. Γ anticommutes with it. For random Hermitian K and smooth test spinors on [0, T], ⟨ψ, D_Kψ′⟩ − ⟨D_Kψ, ψ′⟩ = i[u†v′ + v†u′](0) − i[u†v′ + v†u′](T) for polynomial test spinors, to 10⁻¹⁰ (Gauss–Legendre, exact for their degree) | 95% |
| E2 | **The zero modes and the L² plane.** For 200 random invertible Hermitian K, e^{−tK}u₀ and e^{tK}v₀ solve D_Kψ = 0 to 10⁻¹⁰. The decaying ones are exactly u₀ ∈ E₊ and v₀ ∈ E₋. L_ext = E₊ ⊕ E₋ is six-dimensional, G-null to 10⁻¹² and Γ-invariant | 97% |
| E3 | **The stabilizer and the gap.** A Q8-commuting invertible K_* = A ⊗ I₂ has a positive eigenspace of even dimension. Weyl's bound holds on 2 000 random pairs of Hermitian matrices to 10⁻¹². On 200 random continuous paths K(s) with K(0) = K_* and ‖K(s) − K(0)‖ < δ/2, where δ = min∣eig(K_*)∣, the number of positive eigenvalues is constant | 98% |
| E4 | **The threshold comparator.** K(S_s) = s I₃ ⊗ n·σ, and its positive eigenspace is the range of I₃ ⊗ (I₂ + n·σ)/2, of rank 3, for 0 < s < 1. The tail threshold s² → 0, and both decay lengths are 1/s | 98% |
| E5 | **The far-tail sequence.** For a smooth bump χ on (0, 1) normalised to ∫∣χ∣² = 1, ‖f_L‖ = 1 and ‖D₀f_L‖² = L⁻²∫∣χ′∣², to 10⁻⁸ at L ∈ {1, 10, 100} (quadrature) | 97% |
| E6 | **The extremes and the controls.** K = mI₆ gives v = 0 (plus rank 6, index +3) for m > 0, and u = 0 (rank 0, index −3) for m < 0. The controls fail as they should: with a wrong Green sign (u†v′ − v†u′) the planes of G1 and E2 are not null; with the decay orientation reversed the selected plane is E₋ ⊕ E₊, still null; with the MINUS slot omitted the plane E₊ ⊕ 0 has dimension below 6 unless K > 0, so it is not maximal | 95% |

## What the outcomes mean (fixed now)

- **G1–G6 hold.** The first note's classification is correct as stated. At the symmetric state, the Q8-invariant
  maximal null planes form a U(3) family. The grading cuts it to the even ranks, with index in {−3, −1, +1, +3}. The
  coupling (9) does not supply a boundary normal map.
- **E1–E6 hold.** The second note's constant-tail control is correct as stated. A uniformly gapped Q8 tail gives even
  plus rank, and three needs a threshold, a changed stabilizer, a changed grading or another tail.
- **Neither closes P-210,** as both notes say. This seat's review certifies the algebra, not the physical end, the
  exterior's existence or any index of the programme.
- **Any cell fails:** the failure is the finding. It is diagnosed (the lane's statement, or this seat's code) before
  anything else is said, and reported to the lane as found.

## What stays out

- The finite-distance Fredholm application; the source notes the two cite; the eighteen-test proposal; any physical
  claim. Main's B1678 check is not rerun.

## Seen before the rule (disclosed)

- **Read:** both notes in full, and their relays when they were rowed (f0d05a9b4). Main's B1678 FINDINGS were not
  read for this rule.
- **By hand:** every equation (1)–(9) of the first note and (1)–(6) of the second, while reading. Each appeared
  correct.
- **Not run:** no script exists.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read.
- A failed launch is disclosed, with its log kept. Any failed prediction is recorded as failed, and any later check is
  labelled post hoc.

0 of 19.
