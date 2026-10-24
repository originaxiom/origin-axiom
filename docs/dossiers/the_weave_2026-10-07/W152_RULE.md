# W152 — the Higgs as a qubit state: R is the square of the theta qubit, the modular group moves it by the weave's Clifford gates, the cone's special lines are the stabilizer and magic states, and every direction is a squared qubit plus its weighted antipode with I = 2r/(1 + r²) (the rule, committed before the script)

The SM-derivation seat, 2026-10-24. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **W151** named "the squared spinor" as the next candidate, from its cone-tracking reading: following the cone needs
  the coefficients' quadratic relation, the structure of a square h = ψ ⊗ ψ.
- **The owner's word** (2026-10-24): "check answers and start next candidate whenever the right moment". The answers
  are collected in relay §260.
- **What the hand work found while writing this rule, and why the arc is reframed.** The squared spinor is not a
  special candidate. Every direction h ∈ M is a squared qubit state plus its antipode's square at a smaller weight:
  the Takagi factorization of a 2 × 2 complex symmetric matrix. So "the square" is a coordinate system on M. W152
  sets it up exactly, reads the record and the target in it, and leaves the question it sharpens: what fixes the
  qubit state and its mixing.

## The objects

- **The theta qubit:** ψ₀(τ) = (ε, θ) with ε = Θ₂(2τ) = Σ e^{2πiτ(n+½)²} and θ = Θ₃(2τ) = Σ e^{2πiτn²}, direct sums.
- **M as the qubit's symmetric square.** In W146's lines (l1 = x, l3 = y − iz, l7 = y + iz), write
  S_h = [[l3, −l1], [−l1, −l7]].
  - For ψ = (a, b), ψψᵀ is the S_h of (l1, l3, l7) = (−ab, a², −b²): this is Sym²ψ.
  - det S_h = −h·h, and ‖S_h‖² = 2|h|² (the Frobenius norm and W146's norm).
  - g ∈ GL(2) acts by S_h ↦ g S_h gᵀ.
- **The qubit's modular action** (by hand, from θ₂(−1/τ) = √(−iτ) θ₄(τ), θ₃(−1/τ) = √(−iτ) θ₃(τ), θ₃(τ/2) = θ + ε
  and θ₄(τ/2) = θ − ε):
  - ψ₀(τ + 1) = g_T ψ₀(τ), with g_T = diag(i, 1), the phase gate;
  - ψ₀(−1/τ) = √(−iτ) g_S ψ₀(τ), with g_S = [[−1, 1], [1, 1]]/√2 = −ZHZ, a Hadamard-type reflection.
- **W28's lifts of the weave's moves on the common point's qubit:** L ↦ e^{iπZ/4} and R ↦ e^{−iπY/4}, with L ↔ T and
  R ↔ S T⁻¹ S⁻¹ (W28, I2 and I3).
- **The Bloch sphere's special states under the Clifford group:** the 6 stabilizer states (the Pauli eigenstates),
  the 8 F-type magic states (Bloch vectors (±1, ±1, ±1)/√3) and the 12 H-type magic states (the 12 edge midpoints).
- **The Takagi coordinates of a direction:** S_h = σ₁ u₁u₁ᵀ + σ₂ u₂u₂ᵀ with σ₁ ≥ σ₂ ≥ 0, u₁ and u₂ orthonormal. Then
  u₁ is the direction's qubit state, u₂ = j ū₁ is its antipode, and r = σ₂/σ₁ ∈ [0, 1] is its mixing.

## Weave or thread

**K2 and K3 are weave-type:** they concern the moves' group on the common point's qubit (W28) and every special line
(W149). **K4** is exact for every direction. **K5** is a census over every form in W146's record list and its
conjugate, with none hand-picked. **The read-outs** use a fitted target.

## The cells, with predictions, priors and pre-mortems

| cell | prediction | prior |
| --- | --- | --- |
| K1 | **R is the square of the theta qubit (exact; main's B1746 formula and the web seat's dictionary entry, reproduced).** In W146's lines, (l1, l3, l7)(R) = η⁻³(−εθ, ε², −θ²), at 20 random τ with Im τ ∈ [0.9, 4], each to 10⁻²⁵ of \|R\| (40 digits) | 98% |
| K2 | **The qubit's modular action is the weave's.** ψ₀(τ + 1) = g_T ψ₀(τ) and ψ₀(−1/τ) = √(−iτ) g_S ψ₀(τ) at the same 20 τ, to 10⁻²⁵. The projective group ⟨g_T, g_S⟩ has order 24. Sym² carries g_T and g_S to ρ(T) and ρ(S) (W134's `rho_exact`, in W146's lines) projectively, to 10⁻²⁵. The unitary U = e^{iπZ/4} carries (g_T, g_S g_T⁻¹ g_S⁻¹) to W28's (e^{iπZ/4}, e^{−iπY/4}) projectively, exactly (sympy). By hand, g_S g_T⁻¹ g_S⁻¹ ∝ e^{iπX/4} | 92% |
| K3 | **The cone's special lines are the stabilizer and magic states (exact).** Under ψ ↦ Sym²ψ, the 6 stabilizer states map onto W149's six ℤ₄-lines, (1, 0) onto h₀ and (0, 1) onto h̄₀. The 8 F-type magic states map onto the eight ℤ₃-lines, and the 12 H-type ones onto the twelve ℤ₂-lines. Each is matched one to one, projectively to 10⁻⁴⁰ (wedge at 50 digits, through W146's lines), against W149's 26 lines (its `group_O`, `isotropic_lines_of` and `stabilizer`, exact) | 95% |
| K4 | **Every direction is a squared qubit plus its weighted antipode (exact).** det S_h = −h·h and ‖S_h‖² = 2\|h\|² (sympy). So I = 2r/(1 + r²) for every h, with r the Takagi ratio. On 2 000 random h: I against 2r/(1 + r²) to 10⁻²⁵; u₂ ⊥ u₁; and under each of the 24 projective elements, u₁ moves by the element and r is unchanged, both to 10⁻²⁵ (40 digits) | 97% |
| K5 | **The record's forms as qubit states: W146's dichotomy restated.** Along τ = iy, y ∈ [4, 8], for the 24 objects: R, F₂ and their conjugates are pure, r below 10⁻²⁵. The other null-led objects have ln r falling at slope −π (r ~ \|q\|^{½}) to 10⁻³, and 1 − \|⟨u₁, s⟩\| below 10⁻⁶ at y = 8, with s the stabilizer state of their lead line: (1, 0) for an l3 lead, (0, 1) for an l7 lead. The e₁-led objects tend to the maximally mixed state, with 1 − r below 10⁻³ at y = 8 | 90% |
| R | **Read-outs** (no prediction): on B1743's ten rows (W146's sha-checked target), r from I and u₁'s Bloch angle from the stabilizer state (1, 0) (h₀); across the L₂ rows, the slopes of ln r and of the angle; the special state nearest u₁ on each row and its angle; and R's own Bloch angle at the rows' Im τ, beside the target's | — |

**Pre-mortems** (how each cell could fail for a reason that is not the finding):
- **K1.**
  - ε's q^{¼} must come from the direct sum, not from a principal nome root (W144's lesson; the web seat's e13
    found mpmath's branch off by −i for Re τ > ½).
  - η⁻³ is W146's `eta_pow`.
- **K2.**
  - √(−iτ) is the principal root, which is right for Im τ > 0.
  - ρ(S) and ρ(T) carry their own scalars (z = e^{iπ/4}) and η⁻³ its multiplier, so the comparison is projective.
  - U is predicted by hand. A different conjugating unitary would mean a hand slip in the basis, not a failure of the
    group statement. The group statement is the cell's substance.
- **K3.** W149's lines come from its numerical eigenlines at 50 digits. A match at 10⁻⁴⁰ is projective, by the wedge
  of the two vectors.
- **K4.**
  - The Takagi values are the singular values of S_h, and u₁ is its top left singular vector up to a phase.
  - Near r = 1 the vectors are ill-defined, so draws with r > 0.999 are counted and set aside for the u₁ check.
- **K5.**
  - The slope −π comes from W146's K2 (I/(C\|q\|^{½}) → 1), since r ≈ I/2.
  - For the e₁-led objects only r is checked, because their u₁ is ill-defined in the limit.
  - The corrections to I/(C\|q\|^{½}) are of relative order C e^{−πy}, about 10⁻⁴ at y = 4 for the largest C (104),
    so the slope over [4, 8] is inside 10⁻³. A tolerance failure there is diagnosed as such.
  - The measure is 1 − \|⟨u₁, s⟩\|, about \|δ\|²/4, not the distance \|u₁ − s\|, about \|δ\|/√2. For ∂R at y = 8
    the first is near 10⁻¹⁰ and the second near 10⁻⁵.
- **R.** The rows are fitted values; this is a description, not a test.

## What the outcomes mean (fixed now)

- **K1 to K4 hold.** The record's Higgs direction has an exact qubit dictionary:
  - the cone is the set of pure states;
  - the invariant I is the mixing, I = 2r/(1 + r²);
  - the modular group acts on the qubit by the Clifford gates, which are the weave's moves on the common point's
    qubit up to one fixed rotation;
  - the cusp, i and ω go to the stabilizer, H-type magic and F-type magic states.
  "The squared spinor" is then a coordinate system on every direction, not a special candidate.
- **K5 holds.** In qubit language W146's dichotomy says: every single section tends to a pure stabilizer state, or to
  the maximally mixed state. So no single section stays partly mixed near a stabilizer state.
- **What it leaves open, stated as the question for the next arc.** The target, in these coordinates, is a nearly
  pure state, displaced from a stabilizer state (the read-outs give the numbers). What in the joint action fixes a
  qubit state off the stabilizer and magic points, and a constant mixing r? Michel's theorem says an O-invariant
  functional of u₁ alone is extremal at the special orbits (the breaking chain, section 2). So the displacement needs
  the τ-dependence (the modular trajectory) or a second structure. Either way, its coefficients are counted under the
  WEAVE sentence once the owner rules on it.
- **K2's identification is of the group, not of the object.** That the theta qubit and the common point's qubit are
  one object is a reading, not checked here.
- **Any cell fails:** the failure is the finding, and it is diagnosed before anything else is said.
- **This is data-free.** The read-outs use a fitted target; they are a description, not a test.

## What stays out

- Any dynamics for (u₁, r), and any functional of them: magic measures, potentials, the joint (τ, h) potential.
- The metaplectic lift's characters and the qubit sections beyond ψ₀ (the Clifford products of the catalogue with
  ψ₀, and sums of qubit sections).
- The band fits, and any comparison with data beyond the read-outs.
- Whether the theta qubit is the common point's qubit as one object (a reading for later).

## Seen before the rule (disclosed)

- **Read:**
  - main's B1746 formula and the web seat's R_IS_THE_S4PRIME_TRIPLET (the identity of K1);
  - W28's NOTE (the lifts and the Clifford group), W149's C1 lines and its read-out rows, W146's K2 and K6.
- **By hand:**
  - the duplication identities and the S-law of ψ₀;
  - g_T, g_S = −ZHZ, g_S g_T⁻¹ g_S⁻¹ ∝ e^{iπX/4}, and U = e^{iπZ/4};
  - S_h, det S_h = −h·h, ‖S_h‖² = 2|h|², and I = 2r/(1 + r²);
  - the stabilizer and magic correspondence by equivariance;
  - K5's rates, and its measure 1 − |⟨u₁, s⟩| (corrected from a distance while writing the rule);
  - from W149's rows: the target's r ≈ I/2 ≈ 0.009, and an angle of about 25° from tan(angle/2) ≈ \|δ\|/√2.
- **Not run:** no script exists.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read.
- A failed launch is disclosed, with its log kept. Any failed prediction is recorded as failed, and any later check is
  labelled post hoc.

0 of 19.
