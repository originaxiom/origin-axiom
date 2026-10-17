# W101 — the rule, recorded before the code (the weave's anomaly: the moves acting on the Standard Model's fermions)

The SM-derivation seat, 2026-10-17. Committed before the script that reads it exists. Nothing here is a result.

## Why this arc

- **The referee lane's N10** (its B1669 on its branch, which main will re-bank under P-192) found that on the ruled
  branch θ̄ = π·Re τ for the triplet's T⊗T couplings.
- **This seat's read** (the handoff `docs/handoffs/SM_TO_REFEREE_LANE_2026-10-17_THE_REFEREE_READ.md`, relay §153)
  reads that phase as the moves' mixed anomaly with QCD.
- **The owner's word (2026-10-17).** "agreed": compute the weave's anomaly first.
- **Why it matters.**
  - Anomaly cancellation is a consistency condition, not an identification. It is how the Standard Model's
    hypercharges are fixed.
  - If the moves are an exact symmetry, it constrains the dictionary (which multiplets carry T and which T̄), and the
    dictionary is the open gap.

## Weave or thread?

**WEAVE.**
1. **Every thread, every assignment.** The anomaly is a character of the whole group the moves generate, Mp₂(ℤ) acting
   through ρ: every word, every thread. Every dictionary assignment under the stated rule is taken, none hand-picked:
   each of Q, u^c, d^c, L, e^c and ν^c in T or T̄, 2⁶ = 64.
2. **A joint quantity.** The anomaly is a character of the group; a single thread carries only its value.
3. **A claim about all threads.** The anomaly vanishes on every thread exactly when the character is trivial.

## Hypotheses (stated, not derived)

- **H-T (the triplet postulate, the dictionary open).** Each fermion multiplet carries three generations in T, through
  ρ = χ_η²¹ ⊗ ρ_u, or in T̄, through ρ̄.
- **H-W (the weights).**
  - Under γ = (a b; c d), a multiplet's canonically normalised field rotates by ρ_f(γ) and by the phase
    ((cτ + d)/|cτ + d|)^(−k_f), where k_f is its weight.
  - The record fixes no weight for a triplet field. W41's −¾ belongs to the zero-mode doublet. So the results are
    stated as conditions on the weights.
- **H-H (the Higgs).** Higgs fields are scalars, with no anomaly. For the ruled-branch read-outs: one singlet Higgs of
  weight 0, so a sector's coupling weight is k = k_L + k_R. (A Higgs's weight drops out of θ̄. It is kept at 0 so that
  coupling weights and fermion weights coincide.)
- **H-θ (the QCD angle).** It is constant unless a counterterm θ(τ) = N·arg η(τ) is added (N an integer): the Dedekind
  counterterm.

## The quantities

- **The character layer.**
  - det ρ = χ_η^e, with e predicted to be 9.
  - For a gauge factor G and an assignment s (s_f = +1 for T, −1 for T̄), the character exponent is
    n_G(s) = e·Σ_f w_G(f)·s_f (mod 24).
  - w_G(f) is twice the Dynkin index of f's G-representation times its dimension under the other factors:
    - **SU(3)²:** Q 2, u^c 1, d^c 1;
    - **SU(2)²:** Q 3, L 1;
    - **gravity²:** Q 6, u^c 3, d^c 3, L 2, e^c 1, ν^c 1;
    - **U(1)_Y²** is a read-out only, since U(1) conditions on discrete anomalies depend on normalisation.
- **The coupling layer (QCD, the ruled branch).**
  - A coupling sector with fields in s_L and s_R has a determinant of weight 3k with character
    (det ρ_L · det ρ_R)^(−1).
  - det(Y_u Y_d) then has weight 3K, where K = k_u + k_d, and character χ_η^m, where m = −e(2s_Q + s_u + s_d) (mod 24).
  - θ̄ = θ − arg det(M_u M_d), so a move shifts θ̄ by the phase of that multiplier.
  - **Anomaly-free:** m ≡ 0 (mod 24) and K = 0.
  - **Dedekind-cancellable:** m ≡ 6K (mod 24). The counterterm is then ∝ 6K·arg η, and det(Y_u Y_d)/η^(6K) is a modular
    function.
- **The residual.** With the counterterm, θ̄ − θ = −arg g(τ), where g = det(Y_u Y_d)/η^(6K).

## The cells (predictions, with priors)

- **C0. The representation** (exact where stated; 30 digits otherwise). Prior 99%. Not blind: e = 9 was computed in
  the referee read's checks (R8).
  - ρ is reconstructed from its formula with the classical theta and η laws, as W99 did.
  - Checks: s² = (st)³, s⁸ = 1, s⁴ = −1, an image of order 96, and t-exponents {⅛, ⅜, ⅞}.
  - Then det ρ(t) = χ_η(t)^e and det ρ(s) = χ_η(s)^e with e = 9.
- **C1. The control that fixes every sign.** Prior 95%.
  - For the weight-1 coupling Y₁ (the theta constants off the diagonal), det Y₁(γτ) / ((cτ + d)³ det Y₁(τ)) is measured
    at three generic τ.
  - The words are t, s, the hyperbolic words LR, L²R and LRLLR, and their inverses. (R = s t⁻¹ s⁻¹ on the matrix side.)
  - It is compared with det ρ(γ)^(−2) from the matrices.
  - The cell holds if the two agree to 10⁻²⁰ for every word and τ. This ties the character layer to the measured
    coupling.
- **A1. The character layer: exact, all 64 assignments.**
  - **SU(3)²:** n = 0 exactly when s_u = s_d = −s_Q, which is 16 of the 64 (2 of the 8 quark assignments). Prior 97%.
  - **SU(2)²:** n ≠ 0 for every assignment, with n ∈ {6, 12, 18}. Prior 97%.
  - **gravity²:** among the SU(3)²-free assignments, n = 0 exactly when s_e = s_ν = −s_L. Without ν^c, no assignment is
    free. Prior 90%.
  - **No assignment** is free in SU(3)², SU(2)² and gravity² at once. Prior 97%.
  - **Read-outs:** U(1)_Y²'s exponent for every assignment.
- **A2. The coupling layer (QCD): exact.**
  - Take every quark assignment and coupling weights 0 ≤ k ≤ 7 that the representation allows: odd k for a sector with
    both fields in the same representation, even k otherwise.
  - The set of (k_u, k_d) that are Dedekind-cancellable is predicted to be 6K ≡ −9(2s_Q + s_u + s_d) (mod 24).
  - **All in T:** K ≡ 2 (mod 4). **s_u = s_d = −s_Q:** K ≡ 0 (mod 4). **The mixed assignments:** K ≡ 1 or 3 (mod 4) by
    the hand.
  - Prior 95%. The risk is the sign, which C1 fixes.
- **A3. θ̄ on the ruled branch** (mpmath at 30 digits; the referee lane's determinant identities, with weight 3 also
  forced by dim M₆(SL(2, ℤ)) = 1; c real, sign free).
  - **A3a.** Weight 1, all in T, no counterterm: θ̄ − θ ≡ −12·arg η (mod π).
    - It is π/2 exactly on Re τ = ½, at five values of y. Prior 99%.
    - Its zero set in the fundamental domain, sampled on the grid below, is the imaginary axis alone. Prior 95%.
  - **A3b.** Weight 3, all in T, no counterterm: the zero set of sin(12·arg η + 2·arg E₆) on the grid.
    - **POST HOC.** The interior curve was found in this seat's scratch and in the referee read's checks (R9). It is
      stated here, not predicted.
    - The script reports every bracketed crossing with |Re τ| ≥ 0.05.
  - **A3c.** With the counterterm:
    - weight 1, all in T: g is constant to 10⁻²⁰ at five τ. Prior 99%.
    - weight 3, all in T, and weight 2, s_u = s_d = −s_Q: g ∝ j − 1728 to 10⁻²⁰ at five τ, with the coupling
      determinants taken as c·η⁶E₆ and c·E₆, as the identities give. Prior 97%.
    - On the grid, and at three added points of |τ| = 1 (arguments 65°, 75° and 85°), arg(j − 1728) is a multiple of π
      exactly on Re τ = 0, Re τ = ½ and |τ| = 1, to 10⁻¹², and nowhere else. Prior 97%.
- **A4. The verdict** (predicted).
  - The moves' QCD anomaly vanishes at the level of the character only when the up and down antiquarks carry the
    conjugate of the doublet's representation.
  - It can be cancelled by a Dedekind counterterm exactly when the coupling weights satisfy A2's congruence.
  - So, if the moves are an exact symmetry, consistency constrains the dictionary and the weights. Its price: either
    the weights cancel, or a τ-dependent θ term couples Re τ to GG̃, an axion-like input.
  - SU(2)² is never free at the level of the character. Gravity² needs ν^c. Both matter only if the moves are gauged.
    SU(2)'s angle is unphysical in the Standard Model.
  - **N10's exclusivity, read through the anomaly:** exact at weights 2 and 3 with the counterterm; void at weight 1
    with the counterterm; without it, true at weight 1 and near the cusp, not at weight 3 at moderate Im τ (post hoc).
  - **It cannot show:** that the moves are an exact symmetry; that τ is a field; any value of the nineteen. 0 of 19.

## The grid and the precision

- **The grid.** x ∈ {0, 0.05, 0.10, …, 0.50} and y ∈ {0.90, 0.95, …, 2.50}, kept where |τ| ≥ 1.
  - Zeros are bracketed by sign changes of sin(phase) between neighbours in x, refined by bisection to 10⁻¹².
  - A disc |τ − i| < 0.03 is excluded, where E₆ = 0.
  - Mirror symmetry (x → −x) is a check, not assumed: three mirrored points are evaluated.
- **Arithmetic.** A1 and A2 use exact integers mod 24.
- **Precision.** C0, C1 and A3 use mpmath at 30 digits, with ρ's matrices in floating point.
  - C1's tolerance, 10⁻²⁰, is set by mpmath's 30-digit η.
  - The five τ for A3c are 0.137 + 1.291i, −0.284 + 2.173i, 0.41 + 0.95i, 0.05 + 1.7i and −0.33 + 1.02i.

## Discipline

- **Order.** This rule, then the script (committed before its single run), then one run with its output committed
  unread, then the record.
- **Failures.** A failed launch is disclosed, with its log kept and redacted. A cell that fails is recorded as failed.
  Post hoc work is labelled.
