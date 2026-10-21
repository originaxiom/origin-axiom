# W113 — the strong angle at every τ: which quark assignments make θ̄ constant without tuning, and does the CKM phase survive there? (the rule, committed before the code)

The SM-derivation seat, 2026-10-21. Committed before the script that reads it exists. Nothing here is a result.

## Why

- **Stage 2 of the project goal** (`THE_SKELETON_AND_THE_FLESH.md`; relay §171). Stage 1, W112, was a clean
  negative. The goal page names the next stage: θ̄, the record's W105.
- **The reason.** A symmetric principle fixes zeros. Among the nineteen, the one value nature puts at zero is θ̄
  (|θ̄| < 10⁻¹⁰). Main's B1670 finds that each mechanism in the literature buys θ̄ = 0 "by construction".
- **What the record has** (W101, banked by main as B1674; B1671):
  - With the Dedekind counterterm that the moves' anomaly needs, θ̄ is constant at weight 1 with every quark in T, so
    it is 0 by CP at every τ. But weight 1 carries no hierarchy (B1636's sum rule; B1671).
  - At weights 2 and 3, θ̄ = −arg(j − 1728), which is zero only where δ_CKM is.
- **What it left open:** the other hands, and mixed weights across the sectors (W105).

## Weave or thread

**WEAVE-type, given the frame below.**
1. **Every assignment.** Every quark hand (s_Q, s_u, s_d) ∈ {±1}³ (W101's eight), every coupling weight, and every
   coupling in the whole space its representation allows. None is hand-picked.
   - W50 found that at a generic τ the moves leave only scalars, so no piece (D, O⁺, O⁻) is protected by a symmetry.
     Restricting a sector to a piece would be a hand choice, so pieces enter only as read-outs.
2. **A joint quantity.** θ̄ with the counterterm. The counterterm's coefficient is the moves' anomaly, a character of
   the whole group the moves generate (W101).
3. **A claim about every τ and every assignment at once.**
- **The fit** (cell C6) is a read-out on the assignment the census leaves, selected by the rule below, not by hand.

## The frame (stated, not derived)

- **W101's hypotheses.**
  - H-T: each multiplet's three generations are in T, through ρ, or in T̄, through ρ̄.
  - H-W: the weights.
  - H-H: one Higgs of weight 0, so a sector's coupling weight is k = k_L + k_R.
  - H-θ: the Dedekind counterterm θ(τ) = N·arg η(τ).
- **H-CP, CP as a symmetry of the law.** This is §158's level 4, the swap in the law (GENESIS GM5c, OPEN).
  - In the theta basis u = (θ₂², θ₃², θ₄²), u(−τ̄) is the complex conjugate of u(τ). The multiplier of u obeys
    A(γ′) = conj A(γ), with γ′ = diag(1, −1) γ diag(1, −1).
  - So CP acts with X = 1 in that basis. The law is CP-symmetric when every coupling's coefficients are real in a
    real basis of its space, and θ₀ ∈ {0, π}.
  - The CKM phase must then come from τ (the owner's ruling of 2026-10-08, read at level 4).
- **Scope.** Tree level; the ruled branch's holomorphic couplings; the quark sector only. Nothing here says that the
  moves are an exact symmetry, that τ is a field, or that the counterterm exists.

## The construction (the script's, written after this rule)

- **A sector.** Its fields have hands s_L (the doublet Q) and s_R (u^c or d^c). Its coupling transforms as
  Y(γτ) = (cτ + d)^k R_L Y R_Rᵀ, with R = ρ̄ for a field in T and R = ρ for a field in T̄.
- **Three types.**
  - T⊗T: s_L = s_R = +1 (main's branch).
  - T̄⊗T̄: both −1.
  - Mixed: s_L ≠ s_R, in both orders.
- **Polynomials.** W = η^m Y is a 3 × 3 matrix of polynomials of degree k + m/2 in u, modulo θ₃⁴ = θ₂⁴ + θ₄⁴.
  - It obeys W(A u) = A_L W A_Rᵀ for A = A_S and A_T, where A_L = conj A for a field in T and A for a field in T̄.
  - m = 18 for T⊗T, 6 for T̄⊗T̄ and 0 for mixed.
  - Every entry of W vanishes at the cusp to order q^{m/24}, read from exact integer q-series.
- **Exact arithmetic.** The equivariant spaces are solved exactly over ℚ(i). Main's B1635 builds T⊗T and the mixed
  type this way; this seat's code is its own.

## The lemma, by hand (to be checked)

- **The character.** det ρ = χ_η⁹ (W101 C0). So a sector's determinant has weight 3k and character χ_η^a, with a = 6
  for T⊗T, 18 for T̄⊗T̄ and 0 for mixed.
- **So det Y = η^a · g,** with g a level-one modular form of weight w = 3k − a/2.
  - g is holomorphic on H, since η has no zeros there.
  - It is holomorphic at the cusp: det Y is, and its exponents are ≡ a/24 (mod 1), so none is below a/24.
- **θ̄ with the counterterm.** If det(Y_u Y_d) = c·η^{6K} with K = k_u + k_d, the counterterm N = 6K cancels the η
  phase exactly, and θ̄ = θ₀ − arg c. W101 A2's congruence is then met automatically.
- **θ̄ is constant for every coupling in a space exactly when g is constant for every member.** A level-one form is
  zero-free on H only if it is cΔ^n, so w must be 12n.
  - **Automatic** (every member): w = 0. That is k = 1 for T⊗T, k = 3 for T̄⊗T̄ and k = 0 for mixed: one weight per
    type, among all weights, not only up to 7.
  - **det ≡ 0:** w < 0, which happens only for T̄⊗T̄ at k = 1. That gives a massless quark.
  - **Tuned** (a sub-variety of the coefficients): w = 12n with n ≥ 1. Up to weight 7, that is k = 5 for T⊗T, k = 7
    for T̄⊗T̄ and k = 4 for mixed. The space then holds E₄ times a lower-weight member, so purity costs one condition,
    real for real coefficients. At higher weights it costs n conditions.
  - **Impossible** (except det ≡ 0): every other weight.
- **The forced pairs.** A quark hand fixes both sectors' types, and the automatic weights then give eight assignments.
  - T⊗T at k = 1 is one-dimensional (O⁺, B1635), so two such sectors are proportional and V = 1.
  - Mixed at k = 0 is the identity, so its masses are degenerate.
  - **So, if dim M₃(T̄⊗T̄) ≥ 2 and its generic determinant is not zero, exactly one assignment is automatic, and
    non-degenerate and non-proportional in both sectors: every quark field in T̄, at coupling weight 3 in both.**
  - It is the hand opposite to the record's (B1640). Its anomaly is cancellable (W101 A2, with K = 6).
- **The dimensions, by hand** (Skoruppa's formula, with tr ρ(S) = e^{−23πi/4} and tr ρ(ST) = 0):
  - T̄⊗T̄ at k = 3, 5 and 7: 3, 4 and 6;
  - at k = 3 the split is 2 symmetric and 1 antisymmetric (Λ²ρ ≅ ρ̄ ⊗ χ_η⁹);
  - at k = 1 the formula gives 1, but at weight one it carries a correction, so that dimension is a read-out.

## The selection rule (fixed now)

- An assignment is **viable** if:
  - neither quark sector is degenerate (three equal masses);
  - neither has a massless quark;
  - and V ≠ 1.
- These are three qualitative facts of the data; m_u ≠ 0 rests on lattice QCD (FLAG). No value is fitted here.

## The cells, with predictions and priors

**Layer F, the census (exact where stated).**

| cell | prediction | prior |
| --- | --- | --- |
| F0 | the control: this seat's construction gives main's dimensions, T⊗T 1, 2, 4, 5 at k = 1, 3, 5, 7 and the mixed type 1, 2, 4, 5 at k = 0, 2, 4, 6 in both orders; the k = 1 T⊗T member is the zero-diagonal theta matrix up to scale, with det ∝ η⁶ (B1671's 8η⁶) | 95% |
| F1 | T̄⊗T̄: dimensions 3, 4, 6 at k = 3, 5, 7; at k = 3, 2 symmetric and 1 antisymmetric | 80% |
| F2 | the determinant layer, for every type and k ≤ 7, on random members at six τ (mpmath, 30 digits): det Y/η^a lies in level-one M_w; it is a constant at w = 0, in ℂE₆ at w = 6, in span{E₄³, Δ} at w = 12 with both components non-zero for a generic member, in E₆·span{E₄³, Δ} at w = 18, and 0 at w < 0 | 90% |
| F3 | at T̄⊗T̄, k = 3, exactly: det W = κ(c)·(θ₂θ₃θ₄)¹² as polynomials modulo Jacobi's relation, with κ a non-zero cubic form in the coefficients, so det Y = 4096κ·η¹⁸ for every member | 85% |
| F4 | the forced pairs: of the eight hands at their automatic weights, exactly one is viable, every quark in T̄ at k = 3 | 80% |

**Layer C, the candidate** (F4's assignment if F4 holds; otherwise every viable automatic one).

| cell | prediction | prior |
| --- | --- | --- |
| C1 | the space is closed under conjugating coefficients, so it has a real basis; for real coefficients Y(−τ̄) = conj Y(τ) to 10⁻²⁰ at three τ (mpmath, 30 digits) | 95% |
| C2 | with real coefficients and the counterterm, det(Y_u)·det(Y_d)/η³⁶ is real to 10⁻¹² for 200 random pairs at 30 random τ in F, so θ̄ ∈ {0, π} at every τ; without the counterterm θ̄ ≡ −36·arg η (mod π) | 95% |
| C3 | the CKM phase survives: at five generic τ, for 100 random real pairs, \|J\| > 10⁻⁸ in at least 95; and \|J\| < 10⁻¹³ at points on Re τ = 0, Re τ = ½ and \|τ\| = 1 | 85% |
| C4 | a hierarchy is available: some real coefficients and some τ in F with Im τ ≤ 6 give m₂/m₁ ≤ 0.1 and m₃/m₂ ≤ 0.1 in both sectors at once (masses m₁ ≥ m₂ ≥ m₃) | 80% |
| C5 | the fit's control: data generated by the model at a random point (fixed seed) is fitted back by the same search to χ² ≤ 0.01 | 85% |
| C6 | **the fit:** χ²_min ≤ 5.99 for the eight quark observables, with six parameters (2 degrees of freedom) | 5% |

**Layer T, the tuned assignments** (k ≤ 7; one tuned condition per tuned sector).

| cell | prediction | prior |
| --- | --- | --- |
| T1 | each tuned variety (T⊗T at 5, T̄⊗T̄ at 7, mixed at 4 in both orders) has non-degenerate real points: along 50 random real lines, the real roots give det Y/η^{6k} constant across three τ to 10⁻¹², and non-zero | 90% |
| T2 | each of the 16 viable tuned assignments has \|J\| > 10⁻⁸ at a generic τ for at least one of 20 sampled real pairs | 85% |
| T3 | read-out only: the smallest hierarchy measure, max over sectors of max(m₂/m₁, m₃/m₂), over the sampled pairs and 20 τ, per assignment | — |

## The fit (fixed now)

- **Observables (8):** m_u/m_c, m_c/m_t, m_d/m_s, m_s/m_b, |V_us|, |V_cb|, |V_ub| and |V_td|.
  - The masses are HZ2021's at M_Z, and the CKM magnitudes are B1612's (PDG 2025), both as W66 reads them
    (`received/HZ2021_running_masses_MZ.json`, `received/B1612_data.json`).
  - The relative errors are combined in quadrature, as W66 forms them.
- **χ²** = Σ ((ln obs − ln data) / hypot(rel, a))², with a = 0.10 (W66's allowance), and read-outs at a = 0.05 and
  0.20. A value below 10⁻¹² scores ∞.
- **The parameters (6).**
  - τ, mapped to F, since the observables are invariant under SL(2, ℤ).
  - Each sector's real coefficients modulo scale, as a point on S². The masses' scales are not fitted.
- **The pass mark:** 5.99, the 95% point of χ² with 2 degrees of freedom.
- **The search** (fixed seed 113):
  - 100 000 random points: τ uniform in F with Im τ ≤ 6, and the coefficients uniform on S²;
  - Nelder–Mead from the best 200, then again from the best 10;
  - a point whose image in F has Im τ > 8 scores ∞.
- **Read-outs:**
  - the best point, with its δ to the nearest elliptic point;
  - its observables, J, and the first generation's values;
  - θ̄ ∈ {0, π} there, by the sign of c_u c_d.
- **The sign of θ̄.** Changing c to −c in one sector flips θ̄ between 0 and π and changes no mass or mixing.
  - So the frame fixes θ̄ to {0, π}, and the choice between them is one bit, chosen like the hand.
  - Whether QCD's vacuum excludes θ̄ = π is not this arc's question.

## What the outcomes mean (fixed now)

- **F4, C2, C3 and C6 hold.** In this frame θ̄ ∈ {0, π} is forced, with no tuning, for the one viable assignment, and
  that assignment fits the quark sector with two degrees of freedom to spare.
  - θ̄'s real value would then be predicted, not fitted, given the frame's inputs: a candidate for the first of the
    nineteen.
  - It goes to main for an independent check, and the count stays 0 until main banks it.
- **F4, C2 and C3 hold, but C6 fails.** θ̄ = 0 and the CKM phase are compatible without tuning in exactly one
  assignment, but that assignment does not fit the data. N10's exclusivity is broken structurally, not physically.
- **C3 fails.** In the forced layer, θ̄ = 0 without tuning and CP violation exclude each other.
- **F4 fails** (no viable automatic assignment, or more than one). The reduction is recorded as it comes out.
- **The tuned layer** gives θ̄ = 0 at every τ at the cost of one tuned coefficient per tuned sector. That trades one
  real number for another, so it cannot lower the count, whatever T1–T3 give.
- **Nothing here lowers the count by itself.** 0 of 19.

## Seen before the rule (disclosed)

- **The record:**
  - W101 (A2's congruences; A3's phases at weights 1, 2 and 3);
  - B1671 (det Y₁ = 8η⁶; the weight-3 and weight-5 T⊗T determinants; the weight-2 mixed one);
  - B1635's dimension table, B1674, B1670's price list, and W50's residual.
- **This seat, by hand, before the rule:**
  - the lemma above, the dimension formula for T̄⊗T̄ (3, 4 and 6), and the cusp exponents of each type's entries;
  - one call of the exact solver's library on a 2 × 2 toy matrix, to learn its interface.
  - No code has been run on T̄⊗T̄, or on any candidate's spectrum, J or fit.
- **Literature.** The mechanism's shape is the modular strong-CP models' (Feruglio, Strumia and Titov 2023; Feruglio,
  Parriciatu, Strumia and Titov 2024; Penedo and Petcov 2024, as main's B1674 lists them): θ̄ = 0 from a determinant
  with no τ-dependent phase, while τ breaks CP. The counterterm route and the census over the record's dictionary are
  this arc's.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read.
- A failed launch is disclosed, with its log kept. Any failed prediction is recorded as failed, and any later check is
  labelled post hoc.

0 of 19.
