# W67 — the rule, recorded before the code

The SM-derivation seat, 2026-10-14. Committed before the code that reads it exists. What the seat worked by hand while
drafting is listed under "Seen before the rule", and the priors were set after that. Nothing here is a result.

## Why this arc

- **The owner's order is "we look what fixes τ then we count free numbers".** W66 found that the data cannot fix τ
  through the parameter-free sections. So this arc asks what fixes τ from the inside: the weave's own potential.
- **The candidate.** W64 found that O keeps exactly three phase-invariant quartics on M: |a|⁴, |a·a|² and
  A = Σ_u |a_u|⁴. Under H-sec (W65) the Higgs's direction is a section a(τ). So the potential's shape
  V̂(τ) = λ₂ q₂(τ) + c q_A(τ), with q₂ = |a·a|²/|a|⁴ and q_A = A/|a|⁴, becomes a function on the modular curve.
- **Why the direction alone.** Write a = φ â(τ) with φ the Higgs's size. Then
  V = φ⁴ (λ₁ + V̂(τ)) − μ² φ² is lowest, over φ, where λ₁ + V̂(τ) is smallest (for λ₁ + V̂ > 0). So V̂ selects τ.

## Weave or thread?

- **Weave-type.** It takes every parameter-free Higgs section (the one-unit sections E, R and R′, none chosen), every
  O-invariant phase-invariant quartic, and τ over the whole fundamental domain.
- **Why only the parameter-free ones.** The three sections span ℂ³ at every τ except i and ω (W65's determinant).
  So a Higgs ranging over their span reaches every direction at almost every τ. It then minimizes V̂ at W64's points
  on the cone at every such τ, and τ stays flat. Only a section with no free coefficient can fix τ.
- **The tags.** Given Λ (GENESIS FK11). Two hypotheses: H-sec (W65), and **H-pot (new)**: the Higgs's potential is the
  weave's O-invariant quartic, evaluated on the section's direction. GENESIS FK10's unit is a tagged working
  postulate.

## Seen before the rule (disclosed; by hand and from W64–W66's committed results)

- **The invariants are functions on the modular curve.** ρ_R is a scalar times a signed permutation, which keeps
  |a·a|, A and |a|². So q₂ and q_A are invariant under SL(2, ℤ).
- **The bounds.**
  - On every nonzero a ∈ ℂ³, q_A ≥ ⅓ by Cauchy–Schwarz, with equality exactly when all |a_u| are equal.
  - q₂ ≥ 0, with equality exactly on the cone.
  - On the cone, the 8-orbit lines have all |a_u| equal, so q_A = ⅓ there, and W64's K7 found ⅓ attained only there.
- **At ω every section lies on one 8-orbit line** (W65's H3). So q₂ = 0 and q_A = ⅓ there: both minima at once.
  Hence, **for λ₂ ≥ 0 and c > 0, τ = ω is a global minimizer of V̂ for every parameter-free section.** It is the
  unique one for R and R′, if their map onto the cone meets the 8-orbit lines only at ω. For E with λ₂ = 0 it can tie
  with a point where all |E_u| are equal on a real-like line.
- **R and R′ are isotropic at every τ** (W65), so q₂ ≡ 0 and V̂ = c q_A. Their values at the special points: ⅓ at ω,
  ⅜ at i (12-orbit lines) and ½ at the cusp (6-orbit lines), from W64's K7.
- **A reading of W65's H3, not used as a premise.** τ ↦ [R(τ)] sends the cusp, i and ω to the 6-, 12- and 8-orbit
  lines. That is the octahedral picture of X(4) ≅ ℙ¹: 6 cusps, 12 points of order 2 and 8 of order 3. If the map has
  degree one, q_A∘R reaches ⅓ only on ω's orbit and ½ only at the cusps.
- **E.** It is isotropic only at ω and at τ₀ and its mirror (j = 1280; W65). It points along the real e_i at the cusp,
  so q₂ → 1 and q_A → 1 there.
- **At ω every pair of parameter-free sections gives a rank-one Yukawa** (W65's H4, W66's C1): masses 0 : 0 : m₃.

## The method (fixed here)

- **The sections:** W65's 40-digit collocation, evaluated in double precision (W66's instrument, checked there to
  10⁻¹⁵).
- **The grid:** the fundamental domain, with x in 81 steps over [−½, ½] and y in 80 geometric steps over [0.866, 8],
  kept where |τ| ≥ 1; plus ω and i exactly.
- **The landscape.** For each section: q₂ and q_A on the grid; the grid's local minima (lower than all eight
  neighbours); and a Nelder–Mead refinement from each.
- **The potential's census.** For each section and each (λ₂, c) in {0, 0.1, 1, 10} × {−1, −0.1, 0.1, 1}: the
  global minimum of V̂ over the grid, refined by Nelder–Mead from the 10 best grid points. A minimum at y > 7 is
  recorded as "runs to the cusp".

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **F1, R and R′** | q₂ < 10⁻¹² everywhere on the grid. q_A(ω) = ⅓ and q_A(i) = ⅜ to 10⁻¹². On the grid, ⅓ < q_A < ½ at least 10⁻³ away from ω and ω + 1 (the same point of the modular curve), and q_A exceeds 0.499 at 8i. Every refined local minimum of q_A is at ω or ω + 1. | 85% |
| **F2, E** | q₂ is below 10⁻¹² at ω and at τ₀ and its mirror, and above 10⁻¹⁰ at every grid point at least 0.02 from them and from ω + 1. q_A(E(ω)) = ⅓ to 10⁻¹². q₂ and q_A exceed 0.99 at 8i. | 85% |
| **F3, what fixes τ** | With c > 0, the global minimum of V̂ is at ω or ω + 1 (within 10⁻⁴): for R and R′ at every λ₂, and for E at every λ₂ > 0. For R and R′ with c < 0, the minimum runs to the cusp. | 85% |

**The read-outs (no prior).**
- For E with c < 0, and with λ₂ = 0 and c > 0: where the minimum of V̂ sits (ω, τ₀, the cusp, or elsewhere). With
  λ₂ = 0, E may tie with ω wherever all three |E_u| are equal on a non-isotropic line, where q_A is also ⅓.
- The τ in the fundamental domain where all three |E_u| are equal, if any.
- q_A(E(τ₀)), and E's q₂ and q_A along τ = iy and along the arc from i to ω.
- Every refined local minimum and its value, for q_A∘R, q_A∘R′, q₂∘E and q_A∘E.
- The masses at each fixed point: m₂/m₃ for the pairs ER, ER′ and EE, which are rank one at ω (W66's C1).

## The reading, written before the run (predicted)

- **The weave's own potential fixes τ.** With c > 0, the anisotropy evaluated on the Higgs's section is lowest at ω, on
  every parameter-free section and for every λ₂ ≥ 0. With c < 0, R and R′ run to the cusp. So τ is either ω or the
  cusp, by the sign of one coefficient, as W64's K7 found the Higgs's direction on M to be.
- **But where it fixes τ, the second generation is massless.** At ω every Yukawa built from these sections has rank one
  (W65, W66): masses 0 : 0 : m₃. At the cusp the rank-one pairs stay rank one.
- **So the weave gives a vacuum with one heavy generation and τ fixed.** The second generation's mass needs a
  displacement of τ from ω (m ∝ |τ − ω|², W65), and nothing computed supplies its size.
- **The count stays all 19 of the 19 free** (18 if I-18 is earned). 0 of 19. τ would be fixed (given H-sec and H-pot),
  but no observable of the 19 is then fitted.

## Discipline

- **The rule is committed before the script, and there is one run.** A failed launch (a crash before the read-out) is
  disclosed and fixed, and does not count.
- **Each cell is recorded as computed.** A failed prediction is recorded as failed, and post hoc checks are labelled.
