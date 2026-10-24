# W150 — the frame's heavy states as τ's holder: Higaki, Kawamura and Kobayashi's one-loop mechanism on every singlet form of the joint family group, where it holds Im τ, and what it leaves free (the rule, committed before the script)

The SM-derivation seat, 2026-10-24. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **The breaking chain** (`THE_BREAKING_CHAIN_2026-10-24.md`, sections 9a and 11) named one finite-Im τ mechanism from
  the literature that the record has never tried. Higaki, Kawamura and Kobayashi (arXiv:2402.02071) hold Im τ with a
  one-loop potential from a heavy vector-like pair whose mass is a modular form with a T-charge.
- **The owner approved it** ("yes i agree thank you, do them", 2026-10-24).
- **The question:** in the record's frame, where does this mechanism hold τ, and is the place fixed by the frame's
  integers, or by something the frame leaves free?

## The objects

- **The mechanism, as the paper states it** (its eqs. 3.2–3.5): supersymmetry with a τ-independent soft mass m₀ for
  the scalar partners; one vector-like pair whose supersymmetric mass is m_Q²(τ) = M_Q² (2 Im τ)^k |Y(τ)|², with Y a
  singlet form of weight k. At leading order in m₀²,

  V(τ) = (m₀²/16π²) f(m_Q²(τ)), with f(u) = u (log(u/μ²) − 1),

  and μ the renormalization scale. M̃ = |c₀| M_Q, with c₀ the leading q-coefficient of Y.
- **The frame's singlet forms** (W136's census of the joint family group Γ₄):
  - **1′:** η¹²·g for g in the level-1 ring; weights 6, 10, 12, 14, 16 (η¹², η¹²E₄, η¹²E₆, η¹²E₄², η¹²E₄E₆);
  - **1:** the level-1 forms E₄, E₆, E₄², E₄E₆, E₄³, E₆² and Δ, at weights 4 to 12.
  The 2 and the triplets are left out (see below).
- **The fits' band:** Im τ ∈ [2.0, 3.6] (the breaking chain, section 3).

## Weave or thread

**A census of one chosen mechanism over every singlet form of the frame.** The forms are the joint family group's.
The mechanism itself (supersymmetry, one heavy pair, a soft mass) is the literature's input, chosen. **Not a weave
result.**

## The cells, with predictions, priors and pre-mortems

| cell | prediction | prior |
| --- | --- | --- |
| H1 | **The minimum is where the heavy mass meets μ (exact).** f′(u) = log(u/μ²) (sympy). So every critical point of V has ∇m_Q² = 0 or m_Q(τ) = μ, and V ≥ −(m₀²/16π²) μ², with equality exactly on the level set {m_Q(τ) = μ} | 99% |
| H2 | **The paper's numbers reproduced.** With the leading term m_Q² = M̃² x^k e^{−px}, x = 2 Im τ and μ = M̃, the root of x^k e^{−px} = 1 beyond x = k/p is, at p = 2π/3, x₀ = 3.9, 7.9, 12 and 16 for k = 6, 8, 10 and 12 (the paper's eq. 3.7 values, rounded as it prints them). The root equals −(k/p) W₋₁(−p/k) to 10⁻¹⁰ | 95% |
| H3 | **The frame's singlet T-charges.** Along τ = iy, y ∈ [3, 6], the slope of ln\|Y(iy)\| is −π (to 10⁻³) for every 1′ form: the leading exponent is ½, a T-charge of 2 at level 4. It is 0 for every level-1 form other than Δ, and −2π for Δ | 98% |
| H4 | **The frame's holders at μ = M̃, with the exact forms along τ = iy, y ∈ [1, 8].** Every crossing of m_Q = μ is a minimum (H1). **On the cusp side** (beyond the maximum of m_Q²), crossings exist for the 1′ forms of weights 10, 12, 14 and 16, at Im τ₀ = 2.66, 3.95, 5.23 and 6.55 (each to ±0.02), and for none at weight 6. Of these only weight 10 lies in the band. No level-1 form has a cusp-side crossing. **Next to i:** the forms with a factor E₆ (the 1′ forms of weights 12 and 16; E₆, E₄E₆ and E₆²) vanish at i and have one more crossing in y ∈ (1, 1.3). No other form has a crossing in y ∈ [1, 1.3] | 90% |
| H5 | **Re τ is flat exactly.** V depends on τ only through m_Q². So on the level curve through τ₀ (weight 10, μ = M̃) V is constant. The curve crosses every Re τ ∈ [−½, ½] (21 points) within 3 × 10⁻⁵ of Im τ₀, and V there equals −(m₀²/16π²) μ² to 10⁻²⁰ relative | 95% |
| H6 | **The height is set by μ/M̃.** A cusp-side minimum exists only for μ/M̃ ≤ (k/(πe))^{k/2}: 2.20 at weight 10 and 7.70 at weight 12. The cusp-side Im τ₀ lies in the band exactly when μ/M̃ ∈ [0.237, 1.91] at weight 10 and [1.71, 7.65] at weight 12, each to 1% (by hand from the leading term). Across that window τ₀ moves through the whole band, about a factor 8 in μ/M̃ at either weight | 90% |
| R | **Read-outs** (no prediction): the weight-10 curve's Im τ₀ beside main's S215, the heavy observables at Im τ 2.6–2.7. S215 was seen before this rule, so this is no test and no trial. Also, by hand: the second derivative of V across the curve at τ₀ | — |

**Pre-mortems** (how each cell could fail for a reason that is not the finding):
- **H2.** The paper prints two significant figures; "rounded as it prints them" means agreement at that precision.
  Their p = 2π/3 is level 3, not the record's level 4; the cell checks the instrument, not the frame.
- **H3.** The slopes over [3, 6] carry q-corrections. For E₄ the correction is about 240 e^{−6π}, near 10⁻⁶, well
  inside 10⁻³. Δ's −2π needs its leading coefficient 1, which holds.
- **H4.**
  - "Exact forms" means the q-series to the working precision. A failure of ±0.02 would come from the leading-term
    estimates, which are by hand.
  - The weight-6 1′ form's maximum of x⁶e^{−πx} is about 0.12 < 1, so no root. If the exact form's maximum differs
    enough to reach 1, that is a finding.
  - The level-1 forms without an E₆ factor have m_Q > μ everywhere on y ≥ 1 (E₄(i) ≈ 1.46), or below μ everywhere
    there (Δ, which peaks at y ≈ 0.95). So they have no crossing.
  - The near-i crossings were found by hand while writing this rule, from E₆(i) = 0. Their positions (y ≈ 1.02 for
    E₆, 1.05 to 1.1 for η¹²E₆) are rough, so the cell asks only for (1, 1.3).
  - The near-i crossings of the higher-weight E₆-factor forms sit within 0.01 of y = 1, so the scan steps by 10⁻⁴
    there.
- **H5.** The curve's Re τ-dependence comes from E₄'s 240q and η²⁴'s 48q. That is about (480 + 48) e^{−2π Im τ₀}
  in m_Q², divided by |∂ ln m_Q²/∂ Im τ| ≈ 2.52: about 1.2 × 10⁻⁵ at weight 10. Hence 3 × 10⁻⁵. A first draft said
  10⁻⁶, leaving out the coefficients; corrected before the commit. V's constancy is exact by H1.
- **H6.** The window's ends are from the leading term. The exact forms shift them by far less than 1% in the band.

## What the outcomes mean (fixed now)

- **H1 and H5 hold.** With one heavy pair the mechanism does not fix τ to a point. It fixes a curve, m_Q(τ) = μ, along
  which Re τ is exactly flat. That is the axion the paper wants, and a modulus the record cannot use for a CP phase
  without a second term.
- **The forms that vanish at i** hold a second component of the curve next to i, the symmetric point again (the
  breaking chain, section 2).
- **H4 and H6 hold.** The frame's T-charged singlets (1′, weight 10 and up) can put the curve in the fits' band. Where
  it falls is set by μ/M̃ through log(μ/M̃), across a factor of about 8 per band. So the mechanism turns τ's height
  into one free ratio. That is "forced to choose, not forced which", now with a dynamical reason. The integers k and
  t select only the window.
- **So the literature's "set by integers" holds only once μ/M̃ is fixed.** The paper sets μ = M̃, and its figure uses
  M_Q = 10⁴ μ. The record would need a principle that fixes the ratio, for instance the forced scale (W119) against
  the heavy state's own scale. Nothing on record does.
- **Any cell fails:** the failure is the finding, and it is diagnosed before anything else is said.
- **This is data-free.** The read-out against S215 is a coincidence check, not a test.

## What stays out

- **Supersymmetry beyond the paper's choice:** a τ-dependent soft mass; the supergravity tree potential; the dilaton.
- **Forms beyond singlets.** The 2 and the triplets (ρ′, ρ′ ⊗ sgn) as mass matrices, and the exotics of the 27s with
  their own vev directions: those need a direction in M, the open problem of W149.
- Two heavy pairs, or any sum that could lift the flat direction (the two-object route, next).
- The fundamental domain beyond τ = iy and the level curve through τ₀. Any comparison with data.

## Seen before the rule (disclosed)

- **Read:** the paper's eqs. 3.1–3.7 and its figure caption; the follow-up's (arXiv:2412.18435) eq. 3.9, which states
  the minimum at m_Q² = μ²; W136's census of the 1′ and 1 forms; main's S215 (P-362).
- **By hand:** H1's derivative; the near-i crossings from E₆(i) = 0 and rough q-series values at y = 1.01 to 1.1.
- **With a calculator** (mpmath's Lambert W on the leading term only, not the arc's instrument on the exact forms):
  - the estimates for H2, H4 and H6: 3.896, 7.89, 11.77 and 15.82 at p = 2π/3; Im τ₀ 2.661, 3.945, 5.231 and 6.552
    for the 1′ weights;
  - the weight-6 maximum, 0.120;
  - the bounds 2.202 and 7.699;
  - the window ends 0.237, 1.91, 1.71 and 7.65.
  One by-hand slip was corrected by this: 7.69 for 7.70.
- **Not run:** no script exists.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read.
- A failed launch is disclosed, with its log kept. Any failed prediction is recorded as failed, and any later check is
  labelled post hoc.

0 of 19.
