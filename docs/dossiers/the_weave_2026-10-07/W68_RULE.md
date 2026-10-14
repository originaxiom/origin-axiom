# W68 — the rule, recorded before the code

The SM-derivation seat, 2026-10-14. Committed before the code that reads it exists. What the seat worked by hand while
drafting is listed under "Seen before the rule", and the priors were set after that. Nothing here is a result.

## Why this arc

- **W67's verdict.** The weave's own potential fixes τ at ω or at the cusp, and every vacuum it selects has no
  hierarchy. So a hierarchy needs τ displaced from ω, and the question becomes how the masses grow with the
  displacement δ = |τ − ω|.
- **W65 and W66 found one power,** δ², for the weight −½ sections. At one weight every pair grows with the same power,
  and W66 found the three sectors' coefficients within a factor of 2, where the data need 16.
- **This arc asks whether other weights give other powers.** It is the residual-symmetry mechanism of Novichkov, Penedo
  and Petcov (JHEP 04 (2021) 206; read for W64's reading), read on the matter's own representation ρ_R.

## Weave or thread?

- **Weave-type.** It takes every weight in a stated range, every placement of end data whose space is one-dimensional
  (none chosen), and every pair of the resulting sections.
- **The range of weights.** ρ_R is a multiplier system at the weights k ≡ −½ (mod 2). The range runs from −½ to the
  first weight at which the three eigenlines of the stabiliser of ω have all been reached: −½, 3/2 and 7/2. −½ is
  the Higgs's and R's weight (W63–W65), and 3/2 the fermions' (W64).
- **The tags.** Given Λ (GENESIS FK11). Hypotheses: B1644's form (P-108; P-122), H-sec (W65), and **H-pair′ (new,
  extending W66's H-pair):** the Higgs and the coupling are parameter-free sections of any weight in the range. GENESIS
  FK10's unit is a tagged working postulate.

## Seen before the rule (disclosed; by hand, no numerics)

- **The stabiliser of ω.** ST fixes ω, with cω + d = ω + 1 = e^{iπ/3}. So a section f of weight k satisfies
  f(ω) = e^{iπk/3} ρ(ST) f(ω).
  - ρ(ST) = ρ(S)ρ(T) = √−1 · P L⁻¹ = −√−1 · M, where M = −P L⁻¹ is the three-fold rotation e_i ↦ −e_j, e_j ↦ e_k,
    e_k ↦ −e_i.
  - M's eigenlines: the real axis (1, −1, −1) for eigenvalue 1, ℓ_ω = (−ω, 1, ω²) for ω, and ℓ_ω² = (−ω², 1, ω) for
    ω², with ω = e^{2πi/3}. ℓ_ω and ℓ_ω² are 8-orbit lines, exchanged by conjugation.
  - So f(ω) lies on the eigenline whose eigenvalue λ solves −√−1 λ = e^{−iπk/3}. That gives λ = ω at k = −½, λ = 1 at
    k = 3/2 and λ = ω² at k = 7/2, up to one cube root of unity from the metaplectic cocycle, common to all three.
  - W65 found the weight −½ sections on an 8-orbit line at ω, so the cocycle does not move −½ onto the axis.
  - **The prediction:** −½ on ℓ_ω, 3/2 on the real axis and 7/2 on ℓ_ω².
- **The pair at ω.** For Y(a; c) = a cᵀ + c aᵀ − (a·c)𝟙, with a and c on eigenlines of M:
  - **Both on one isotropic line:** a·c = 0, so Y = a cᵀ + c aᵀ is a multiple of a aᵀ: rank one.
  - **On ℓ_ω and ℓ_ω²:** both isotropic with a·c ≠ 0, so Y = n nᵀ/(a·c) with n = a × c along the axis: rank one.
  - **One isotropic, one on the axis:** a·c = 0 and the two are Hermitian-orthogonal, so Y = a cᵀ + c aᵀ. That gives
    two equal singular values and a null vector n: m₁ = 0 and m₂ = m₃.
  - **Both on the axis:** Y = |c|²(2ĉĉᵀ − 𝟙) up to a scalar, a reflection: m₁ = m₂ = m₃.
- **The orders of vanishing at ω.** A product f·g of sections of weights k₁ and k₂ has weight k₁ + k₂ and the multiplier
  of η⁻¹⁸. So η¹⁸ f·g is a level-one form of weight w = k₁ + k₂ + 9. A level-one form of weight w vanishes at ω to an
  order ≡ −w/2 (mod 3): E₄ has order 1, E₆ order 0, E₄² order 2, Δ order 0 and E₄Δ order 1.
  - −½ with −½: weight 8, order ≡ 2. E·E, R·R′, E·R and E·R′ vanish to order 2 (W65's Φ = E₄²/η¹⁸), and R·R and
    R′·R′ vanish identically.
  - −½ with 7/2: weight 12, order ≡ 0, so it can be nonzero at ω.
  - 7/2 with 7/2: weight 16, order ≡ 1.
- **The powers near ω, for a on ℓ_ω (weight −½) and c on ℓ_ω² (weight 7/2).**
  - In the basis {a, c, n}, Y a = (a·a) c, Y c = (c·c) a and Y n = −(a·c) n.
  - With a·c ≠ 0, a·a ∝ u² and c·c ∝ u (u the local coordinate at ω), the singular values go as 1, u and u².
  - So **m₁ : m₂ : m₃ ∝ δ² : δ : 1** when a = E: a full hierarchy from one displacement.
  - When a is R or R′, a·a ≡ 0, so m₁ ≡ 0 and m₂/m₃ ∝ δ.
  - All of this assumes c·c is not identically zero. A weight 7/2 section could be isotropic at every τ, as R and R′
    are at −½.
- **The weight −½ pairs** (W65, W66): the pairs with an isotropic member have m₁ ≡ 0 and m₂/m₃ ∝ δ². EE has
  m₁m₃ = m₂².
- **The data's pattern, for context only (no fit here).** With δ ≈ 0.06, δ ≈ m_μ/m_τ and δ² ≈ m_c/m_t. Powers of one
  small number match almost any ratio within O(1) coefficients, so this arc fits nothing. W69 would fit, rule first.

## The method (fixed here)

- **The dimensions.** W64's collocation (`collocate`, double precision) at k = −½, 3/2 and 7/2 for every u ∈ {0, 1}³,
  with W45's χ + Σu beside it. The parameter-free sections are those of the placements whose space is one-dimensional.
- **The sections.** W65's collocation generalized to weight k, at 40 digits, with 30 coefficients per eigenline and
  120 points.
  - A one-dimensional space's section is normalized by setting one lowest allowed coefficient to 1. Each of the three
    lines is tried, and the solve with the smallest residual is kept; a line whose coefficient vanishes gives an
    inconsistent system.
  - The residual of the kept solve must be below 10⁻²⁰.
- **At ω.** Each section's value against the three eigenlines of M: the sine of the Hermitian angle to each.
- **The pairs.** Every unordered pair (with repetition) of parameter-free sections. A section f is isotropic at every τ
  when |f·f|/|f|² < 10⁻³⁰ at W65's sample.
  - Y's singular values at ω are taken to 40 digits.
  - At τ = ω + √−1 δ for δ = 10⁻⁴, 10⁻³ and 10⁻², the ratios m₁/m₃ and m₂/m₃ are computed. The powers p₁ and p₂ are the
    slopes of their logs against log δ, between 10⁻⁴ and 10⁻³; the slopes between 10⁻³ and 10⁻² are reported.
  - A ratio below 10⁻³⁰ at all three δ is recorded as identically zero.

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **G1, the sections** | At −½ and 3/2 the one-dimensional placements are exactly the three one-unit ones (dimension Σu). At 7/2 at least one placement is one-dimensional. Every kept solve has a residual below 10⁻²⁰. | 80% |
| **G2, the eigenlines at ω** | Every parameter-free section of weight −½ lies at ω on ℓ_ω, every one of weight 3/2 on the real axis (1, −1, −1), and every one of weight 7/2 on ℓ_ω² (sines below 10⁻²⁰ to its line). | 70% |
| **G3, the pairs at ω** | Each pair's singular values at ω follow its two lines: rank one for two isotropic lines (the same or the conjugate pair); m₁ = 0 and m₂ = m₃ for an isotropic line with the axis; m₁ = m₂ = m₃ for two on the axis. All to 10⁻²⁰ relative. | 80% |
| **G4, the powers near ω** | For every pair (a, c) with a of weight −½ and c of weight 7/2 with c·c not identically zero: p₂ = 1, and p₁ = 2 when a = E, or m₁ identically zero when a is R or R′ (powers within 0.05). Every weight −½ pair with exactly one isotropic member (ER, ER′) has m₁ identically zero and p₂ = 2; the pairs of two isotropic members (RR, RR′, R′R′) have m₂ identically zero (W66). | 55% |

**The read-outs (no prior).**
- The dimension table for all 24 (k, u).
- Every pair's (p₁, p₂) at both slope intervals, its singular values at ω, and the coefficients m₂/m₃ ÷ δ^{p₂} and
  m₁/m₃ ÷ δ^{p₁} at δ = 10⁻⁴.
- **The distinct patterns:** the set of (p₁, p₂) that occur, and which pairs give each.

## The reading, written before the run (predicted)

- **The three weights carry the three residual charges at ω.** −½ sits on one isotropic line, 3/2 on the real axis and
  7/2 on the other isotropic line. That is the order-3 stabiliser's three eigenlines, one per weight.
- **The pair of E with a weight 7/2 section gives a full hierarchy from one displacement:** m₁ : m₂ : m₃ ∝ δ² : δ : 1.
  R or R′ with a weight 7/2 section gives 0 : δ : 1, and the weight −½ pairs give 0 : δ² : 1. So different sectors can
  carry different powers of one δ, as residual symmetry allows elsewhere.
- **What it does not show.** Whether one δ, with the parameter-free coefficients, fits the three sectors and the CKM.
  That is W69's question, rule first. The count stays all 19 of the 19 free (18 if I-18 is earned): 0 of 19.

## A correction before the run (disclosed)

- **G4 as first committed** (9942c9d09) said "every weight −½ pair with an isotropic member has m₁ identically zero and
  p₂ = 2". That includes RR, RR′ and R′R′, which W66 found have rank one at every τ, so m₂ ≡ 0 and no power exists.
  This was a drafting slip against a fact already on record. G4 now names the pairs with exactly one isotropic member,
  and states the rank-one pairs' m₂ ≡ 0. The correction was made before any code existed, and the prior is unchanged.

## Discipline

- **The rule is committed before the script, and there is one run.** A failed launch (a crash before the read-out) is
  disclosed and fixed, and does not count.
- **Each cell is recorded as computed.** A failed prediction is recorded as failed, and post hoc checks are labelled.
