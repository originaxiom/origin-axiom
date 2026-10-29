# THE CRITICAL LINE (P-441; P-468's form 2) — the rule, committed before the script exists

chat1 (the web seat), 2026-10-29, at main's relay CC_TO_CHAT1_2026-10-29_THE_CRITICAL_LINE_AND_THE_LIMITS (task A), on the
owner's word. Data-free: no height, scale or value is set beside the strip Im τ ≈ 3.03 or any measured number; a scale
that emerges is reported bare. Nothing here is a result. 0 of 19.

## The frame card (the 2026-10-29 rule, item 1)

- **The frame:** the weave's threads, i.e. the primitive positive hyperbolic classes of PSL(2, ℤ) with both letters,
  weighted by Z(β, μ) = Σ exp(−β ℓ − μ n). Here ℓ = 2 arccosh(t/2) is the thread's geodesic length and n its word length
  (the sum of its runs). The family is CHOSEN.
- **Continuous configurations:** (β, μ); on the critical line, β alone.
- **Discrete choices:** none beyond the family. The statistic read is the height marginal of the equilibrium measure,
  taken as each thread's arclength measure (B1813's) on the standard domain, on Im τ ≥ 1.
- **Outputs:** the line μ = P(β); the democratic point β* with P(β*) = β*; the height marginals along the line and
  their monotonicity; their ordering in β; the mean flow time per letter −P′(β); where 2 log φ and B1813's s = 1 sit on
  the line. None of the 19.
- **Conditions built from the object, typed:**
  - the Farey (Series) coding of the threads: canonical construction;
  - the geodesic flow's arclength measure: canonical construction;
  - the line as the abscissa of convergence of Z: variational, FORCED given the family.
- **Hypotheses:**
  - (H1) the line's equilibrium state at β is the n → ∞ limit of B1813's fixed-n family tilted by e^(−β ℓ) (equivalence
    of ensembles; standard thermodynamic formalism, stated here, not proved);
  - (H2) the cusp excursions above height 1 correspond one to one to the coding's runs, the k-th reaching apex
    R_k = (a_k + x_k′ + y_k)/2, with x_k′ = [0; a_(k+1), a_(k+2), …] and y_k = [0; a_(k−1), a_(k−2), …] (the Series coding;
    B1720's apex Im τ = Lagrange/2 is its maximum), and the horoball {Im τ > 1} is embedded;
  - (H3) the flow time of the k-th run is r_k = 2 log(a_k + x_k′), which sums exactly to each closed thread's length
    (main's briefing table).
- **The null:** none. No positive is claimed and no datum is read.

## The method (fixed now)

**M1, the line.** The induced (Gauss) transfer operator L_(β,μ) f(x) = Σ_(k≥1) e^(−μk) (k + x)^(−2β) f(1/(k + x)) on
[0, 1], by barycentric Chebyshev collocation (B852's method).
- The sum over k is direct to K₀, with the tail from the interpolant's Taylor terms at 0 against the integrals
  ∫ e^(−μt) (t + x)^(−s) dt.
- P(β) is the μ at which the spectral radius is 1 (bracketed root).
- The grid: β = −8, −4, −2, −1, −0.5, then 0 to 1 in steps of 0.05, with 0.98, 0.99, and β*.
- Convergence is checked in the node count N and in K₀.

**M2.** β* solves P(β) = β.

**M3, the equilibrium's heights.** At β ∈ {0, 0.1, 0.2, β*, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 1}:
- Sample the equilibrium state by its backward chain, which is a rejection sampler of
  p(k | x) = e^(−μk) (k + x)^(−2β) h(1/(k + x)) / h(x), with h the operator's eigenfunction. This gives two-sided run
  sequences.
- Each run k gives its apex R_k (H2) and its flow time r_k (H3).
- The tail is T_β(y) = Σ_k 2 arccosh(R_k / y)₊ / Σ_k r_k, the flow-time fraction above height y. This is exact given the
  sample.
- The y-grid has steps of 0.01 on [1, 2], 0.02 on [2, 4] and 0.1 on [4, 8].
- Standard errors come from independent blocks of chains.

**M4, monotonicity.** The density on a bin is its mass over its width. A member is "monotone on [1, Y]" if no density
rises from one bin to a later bin by more than 3 standard errors. The resolution and the largest standardised rise are
reported.
- **Two exact lemmas, to be stated and proved in the result:**
  - **(L1)** on y ≥ 1, ρ(y) = ∫ 2R / (y √(R² − y²)) 1(R > y) N(dR), with N the apex intensity per unit flow time;
  - **(L2)** if N has a non-increasing density on [1, ∞), then ρ is non-increasing there.

**M5, the order in β.** Is T_β(y) non-decreasing in β at every grid y in [1, 8], within 3 standard errors?

**M6, the mean flow time per letter.**
- Computed two ways, as the sample's Σ r / Σ a and as −P′(β) by central differences of P.
- Whether it reaches 2 log φ = 0.962424 anywhere on β ∈ [0, 1].
- The slope −P(β)/β as β → −∞.

## The controls (each must hold before anything is read; a failure is disclosed and nothing is read until it is resolved, post hoc and labelled)

| control | statement | prior |
|---|---|---|
| C1 | P(0) = log 2 to 10⁻⁹ (at β = 0 the weights are 2^(−k), h ≡ 1) | 97% |
| C2 | at β = 1, μ = 0 the spectral radius is 1 to 10⁻⁸ (the Gauss operator) | 95% |
| C3 | B852's Farey pressures: P(0.2) = 0.53660, P(0.5) = 0.31124, P(0.8) = 0.10570, each to 5 × 10⁻⁵ | 90% |
| C4 | −P′(0) = 0.7924 to 10⁻³ (B1813's mean geodesic length per move) | 90% |
| C5 | at β = 1, T(y) = 3/(πy) on [1, 6] within 3 standard errors at every grid point | 85% |
| C6 | at β = 0, T(1.5), T(2), T(3) = 0.3829, 0.1676, 0.03462 (B1813's limit) within 3 standard errors | 85% |

## The cells, with priors

| cell | statement | prior |
|---|---|---|
| A1 | β* ∈ (0.35, 0.45) | 70% |
| A2 | every member on the β grid is monotone on [1, 6] (M4) | 50% |
| A3 | the height tails are ordered in β: T_β(y) non-decreasing in β at every grid y in [1, 8] (M5) | 80% |
| A4 | the mean flow time per letter stays below 2 log φ on all of [0, 1] | 90% |
| A5 | −P(β)/β at β = −8 is within 2% of 2 log φ (the golden thread's flow time per letter, the top of the Farey Lyapunov spectrum) | 80% |
| A6 | P is real-analytic at β = 2 log φ: the second differences of P show no kink there (B852's test) | 95% |

## What the outcomes mean (fixed now)

- **A2 holds.** No point of the line picks a height. Any characteristic height is a chosen statistic (a quantile, or the
  run cutoff 1/μ), and is reported as such.
- **A2 fails.** Some member's density rises somewhere on [1, 6]. Its location is reported bare, with the bin where the
  rise sits. It is then checked against (L1)–(L2) and against the apex intensity N, to say whether the rise comes from N
  (the coding) or from the excursion kernel. No height is set beside any datum.
- **A3** says whether moving along the line moves weight monotonically into the cusp.
- **A4 and A5** together say whether 2 log φ is a point of the line on [0, 1], or its far end (β → −∞, the golden
  thread). A6 says whether anything happens at β = 2 log φ.
- **β* (A1)** is reported as a value. It is distinguished by the democratic condition, which is CHOSEN as a principle.

## Discipline

- The script `critical_line.py` is committed before its one run.
- Its output is committed unread.
- Any later check is labelled post hoc. A failed launch is kept and disclosed.
- A read-only referee reads the result before it is pushed.

0 of 19.
