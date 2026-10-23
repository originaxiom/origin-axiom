# W144 — the audit lane's five unreviewed checkpoints (its relay at 17cdad33a): a proof review on own code of the joint root action, the puncture connecting map, the transported principal parts, projective regularity and the full-gauge kernel (the rule, committed before the script)

The SM-derivation seat, 2026-10-23. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **The audit lane's relay** (`PHYSICAL_TO_MAIN_SM_CHAT1_2026-10-20_UNREVIEWED_ROOT_AND_END_LAW.md`, 17cdad33a on
  `audit/physical-bridge-2026-09-05`) asks main, this seat and the web seat for a non-authoring review of five
  checkpoints:
  - 8c82671fc, the joint theta-root action and its combined automorphy (with the root cover of 94613bc41 it corrects);
  - 91398366d, the puncture's connecting map and both kernel dimensions;
  - 64e1f24a2, the transported principal parts, normal frame and Green form;
  - 93138ceca, projective regularity at d = 0 or 6;
  - 799c45cbf, the full E₈ transport and its central kernel.
- **The owner said "doit"** (2026-10-23) to taking it up.
- **The relay separates proof review from execution approval.** The lane's 18 sealed tests (444648150) stay unrun
  here. This arc imports and executes none of the lane's code; every check is on code written here.

## The objects

- **The definitions are the lane's**, read from its committed notes (`COHERENT_WORD_LIFTS_AND_LOCAL_BOUNDARY.md`,
  `GEOMETRIC_THETA_REGISTER.md`, `THETA_ROOT_COVER_AND_GLOBAL_SCOPE.md`):
  - F₂ = ⟨a, b⟩; L: b ↦ ab and R: a ↦ ab, the rightmost map acting first; c = ab⁻¹a⁻¹b and Δ = LR⁻¹L;
  - ρ(a) = i = diag(i, −i), ρ(b) = j = [[0, 1], [−1, 0]]; g_L = (1 + i)/√2, g_R = (1 − j)/√2; J_h = (I_h, ρ(h)) and
    ε = (id, −1);
  - μ(l) = e^{πi/4}, μ(s) = e^{−3πi/4}, μ(J_h) = 1; j_l = 1, j_s = √τ, j_{J_h} = 1;
  - theta arguments with periods 1 and τ, so θ_n(z|τ) is mpmath's jtheta(n, πz, e^{πiτ}).
- **The root cover:** w² = θ₁(z|τ), with the maps C, A, B, K₁, K₂, the modular root maps L, S and the field
  F = N/w, N = (iθ₂(z|2τ), θ₃(z|2τ)).
- **The puncture:** b = v/√d with v = N(0) and d = θ₁′(0|τ). The transported data at a lift z_y ∈ ℤ + τℤ are
  n_y = N(z_y) and d_y = θ₁′(z_y|τ).
- **E₈:** its 240 roots in the standard coordinates, the A₅ + A₂ + A₁ subsystem from the extended diagram, and the
  central elements as exponentials of fundamental coweights.

## Weave or thread

**Neither, strictly: a proof review of another seat's checkpoints.** Part A acts with the whole lifted group E of all
the moves (weave-type). Parts B to D sit on one fixed fibre with a supplied coefficient, which is the lane's own
stated scope. Part E is group theory.

## The audit by reading (stated now, before any run)

- **The five notes were read in full**, with the definitions in the two notes above. No error was found by reading
  in their derivations, given their stated hypotheses.
- **Checked by hand:**
  - AB = CBA, A² = CK₁ and B² = CK₂, from t(z)t(z + τ) = e^{−2πiτ−2πiz};
  - LK₂ = K₂′K₁′⁻¹L;
  - S² = (τ, −z, −iw), since arg τ + arg(−1/τ) = π;
  - the corrected s⁴ = εJ_c⁻¹, by inverting Δ⁴ = εJ_c;
  - F(Ax) = iF and F(Bx) = jF, from the half-period laws;
  - F(P_l x) = e^{πi/8}g_l F;
  - D_c = ABA⁻¹B⁻¹ = C;
  - the transport identities (9) and (11) of 64e1f24a2, which are algebraic once its (2) holds;
  - R⁰ = (d/6)I − P_Λ;
  - the E₈ characters (−1)^{a+c}, z₃^{a−b} and z₆^a z₃^b (−1)^c.
- **What computation cannot check here, read only:**
  - the finite-distance Fredholm application that supplies the index d − 3;
  - the subharmonic argument for H⁰(E₀) = 0 and the Serre-duality normalisation;
  - whether the same action requires projective regularity.
  The first is cited by the lane as awaiting specialist acceptance, and this arc does not change that.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| A1 | **The root cover** (40 digits, four τ, three z each). C, A, B, K₁ and K₂ preserve w² = θ₁; C² = 1, AB = CBA, A² = CK₁, B² = CK₂; F is K₁- and K₂-invariant; F(Ax) = iF, F(Bx) = jF, F(Cx) = −F | 95% |
| A2 | **The modular root maps.** L and S preserve the equation. LK₁ = K₁′L, LK₂ = K₂′K₁′⁻¹L, SK₁ = K₂′⁻¹S and SK₂ = K₁′S. S² = (τ, −z, −iw), S⁴ = C, (SL)³ = S². Reversing both root signs keeps (SL)³ = S²; reversing one breaks it by −1 | 90% |
| A3 | **The based words, exact.** Δ(a) = ab⁻¹a⁻¹, Δ(b) = a, Δ⁴ = I_c; RL⁻¹R = Δ⁻¹, with S(a) = b and S(b) = b⁻¹a⁻¹b; (SL)³ = S² in Aut(F₂); I_c ≠ I_c⁻¹. Every generator's lift intertwines ρ; g_Δ = (i + j)/√2; (Δ, g_Δ)⁴ = (I_c, +1) = εJ_c; s⁴ = (I_c⁻¹, +1) = εJ_c⁻¹, not εJ_c | 97% |
| A4 | **The joint action.** D_a = A and D_b = CB⁻¹ satisfy the four conjugations (5) of 8c82671fc, and D_c = C. F(P_l x) = e^{πi/8}g_l F and F(P_s x) = e^{−3πi/8}τ^{1/4}g_s F with g_s = g_R g_L⁻¹ g_R; F(D_h x) = ρ(h)F for h = a, b. k_e² = j_e μ(e) on l, s, J_a, J_b and s⁴; k_{s⁴} = −1, so k_ε = −1. On the relation word (sl)³s⁻² the composed k equals the sign of its g-part | 85% |
| B1 | **The puncture expansion** (four τ). N = v + O(z²) and θ₁/(dz) = 1 + O(z²), so F = z^{−1/2}b(1 + O(z²)) with b ≠ 0 | 95% |
| B2 | **The connecting map.** δ(u)_p = bᵀεu_p has rank 3 and kernel U = ℂ³ ⊗ b, and U⊥ = ℂ³ ⊗ span(εᵀb̄). The kernel pairs are (0, 3), (3, 0), (3, 3) and (0, 0) for Λ = 0, ℂ⁶, U and U⊥. The Green control dim(U⊥ ∩ Λ⊥) = 3 − r_Λ holds on those four and on random Λ of every dimension 0 to 6, where generically r_Λ = min(d, 3) | 95% |
| C1 | **The transported puncture data** at six lifts z_y = m + nτ and four τ. d_{P_e y} = j_e² r_e(y)² d_y and n_{P_e y} = r_e(y)k_e g_e n_y for e = l, s, J_a, J_b. r_l = e^{πi/8}; r_s(y) = e^{−3πi/8}τ^{1/4}e^{πiz_y²/(2τ)}, which differs from k_s off the zero lift. r_ε = 1, r_{J_c} = −1, r_{s⁴} = −1, and r_s(P_s y)r_s(y) = −i | 90% |
| C2 | **The transport maps (9) of 64e1f24a2** at those lifts for e = l, s. At ε, A = C = −I₃ and M = −I₆. At J_c, A = C = I₃ and M = I₆; without r the J_c square fails by −1. The spin maps (10) are trivial at ε, and the Green form (11) is invariant | 90% |
| D1 | **Projective regularity.** R⁰ = (d/6)I − P_Λ vanishes exactly at d ∈ {0, 6}; exp(−2πiR_Λ) = −I₆ at every d; at d = 3 the residue has three eigenvalues each of ±½; deg E_Λ = −tr R_Λ = d − 3. A scalar residue ½ − q gives degree −3 + 6q. The commutant of I₃ ⊗ ρ is M₃ ⊗ 1, three doublet copies | 97% |
| E1 | **The full-gauge kernel, on own E₈ roots.** The central elements of SU(6) × SU(3) × SU(2) acting trivially on all 240 roots form ℤ₆, generated by an element of orders (6, 3, 2). (−I₆, I₃, −I₂) is in it and (−I₆, I₃, I₂) is not; the latter is −1 on exactly 112 roots. The eigenvalue counts give the blocks 35 + 8 + 3 + 40 + 45 + 45 + 36 + 36 | 92% |
| E2 | **The compensation.** U_a and U_b have commutator and squares (−I₆, I₃, −I₂) ∈ K in the product group. On ρ ⊗ ρ, i⊗i and j⊗j commute, square to 1, and with their product have trace 0, so the four characters appear once each. The commutant of {i, j} in M₂ is the scalars | 97% |

## What the outcomes mean (fixed now)

- **Every cell holds.** The load-bearing mathematics of the five checkpoints is confirmed on this seat's own code,
  as a non-authoring review: the identities, the transport and its signs, the connecting map, the kernel table, the
  projective selection and the E₈ kernel. This is proof review only. It certifies no execution of the lane's sealed
  tests, no Fredholm application, and no physical requirement of any end law.
- **A cell fails.** The failure is diagnosed first, as this seat's convention or the lane's statement, before
  anything else is said, and reported to the lane in the relay.
- **The relation to this seat's record is a reading, written after the run.** W28 reached the same ±3 extremes from
  the moves with the flavour group, and from locality. W46 and W47 found that three needs one unit of end data at the
  cusp, and that nothing on the weave's surface forces it.

## What stays out

- **The "compatible same-action response with all compensating fields retained"** that the relay asks next. It is a
  construction, not a review, and is not attempted here.
- The lane's code, tests and frozen proposal; the silver cover; the complete-cusp operator.

## Seen before the rule (disclosed)

- **Read:** the relay; the five checkpoint notes and the root-cover note in full; the opening 150 lines of
  COHERENT_WORD_LIFTS; the definition lines of GEOMETRIC_THETA_REGISTER (by search); 4c4c463ba's message and diff;
  this seat's W28 section.
- **By hand:** the checks listed above.
- **Not run:** no script exists, and no code of the lane's was imported or run.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read.
- A failed launch is disclosed, with its log kept. Any failed prediction is recorded as failed, and any later check is
  labelled post hoc.

0 of 19.
