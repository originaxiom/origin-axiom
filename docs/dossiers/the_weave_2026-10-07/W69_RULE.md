# W69 — the rule, recorded before the code

The SM-derivation seat, 2026-10-14. Committed before the code that reads it exists. What the seat worked by hand while
drafting is listed under "Seen before the rule", and the priors were set after that. Nothing here is a result.

## Why this arc

- **W68's opening.** The weights −½, 3/2 and 7/2 give seven parameter-free sections. Their pairings make the masses
  grow from ω as different powers of δ = |τ − ω|, so one displacement could give different sectors different
  hierarchies.
- **W66's census used only weight −½** (six pairs, 216 assignments) and found no fit (best χ² 309).
- **This arc runs the same census over all 28 pairs of W68's seven sections:** 28³ = 21 952 assignments of a pair to
  each of the up, down and charged-lepton sectors, each fitted at one τ.
- **What would change the count.** If one τ fits the five observables, two of them fix τ and three become predictions:
  the first drop in the count. The owner's order is "we look what fixes τ then we count free numbers".

## Weave or thread?

- **Weave-type.** It takes every pair of every parameter-free section in W68's range of weights, every assignment to the
  three sectors (none chosen), and τ over the whole fundamental domain.
- **The tags.** Given Λ (GENESIS FK11). The hypotheses are B1644's form (P-108; P-122), H-sec (W65) and H-pair′ (W68).
  GENESIS FK10's unit is a tagged working postulate.

## Seen before the rule (disclosed; all from W66 and W68's committed read-outs)

- **W66's best,** ER′ / ER / EE at 308.6, sits near ω with m₂/m₃ of 0.010, 0.011 and 0.021 against the data's 0.0037,
  0.019 and 0.059.
- **W68's coefficients near ω.**
  - m₂/m₃ = 13.2 δ² for ER and ER′, 26.4 δ² for EE, 1.877 δ for R, R′ or E with the weight 7/2 section G, and 0.939 δ
    for GG.
  - The pairs with a 3/2 section have m₂ ≈ m₃ near ω.
- **A rough estimate near ω, by hand.**
  - If δ is set by the leptons through a δ¹ pairing (1.877 δ = 0.059, so δ = 0.031), the smallest up ratio available
    is ER's 13.2 δ² = 0.013, 3.4 times the data's.
  - If δ is set by the up sector through ER (δ = 0.017), the leptons' best is 1.877 δ = 0.031, 1.9 times too small.
  - So near ω no assignment should fit. Away from ω the ratios are general functions of τ, and only the census can
    say.
- **The first generation is not fitted.** W68 found that every pairing with a full hierarchy fixes m₁m₃/m₂² near ω (at
  15 or 1), against the data's 0.08 to 2.7. So m₁/m₃ is read out, not fitted, as in W66.

## The fit (fixed here; W66's, extended)

- **The sections.** W68's seven:
  - at −½: E, R and R′;
  - at 3/2: the one-unit placements (1, 0, 0), (0, 1, 0) and (0, 0, 1);
  - at 7/2: the placement (0, 0, 0).

  Each is solved again by W68's 40-digit collocation, then evaluated in double precision from its q-expansion. The
  check: at W65's sample, the double-precision values agree with the 40-digit ones to 10⁻¹⁰ relative.
- **A pair** {a, c} gives Y(a; c) = a cᵀ + c aᵀ − (a·c)𝟙, symmetric in a and c: 28 pairs.
- **The observables, data, tolerance and pass mark are W66's.**
  - The observables are the three log(m₂/m₃), log|V_us| and log|V_cb|, with V = U_u^† U_d from left singular vectors
    in ascending order.
  - The data are Huang and Zhou 2021 at M_Z, and PDG 2025.
  - σ_i = √(δ_i² + a²), with a = 0.10 for the verdict, and 0.05 and 0.20 reported.
  - **An assignment passes if χ²_min ≤ 7.81** (3 degrees of freedom). A ratio or |V| below 10⁻¹² scores χ² = ∞.
- **The domain and the grid are W66's:** the fundamental domain with y ≤ 6, and 41 × 40 grid points kept where
  |τ| ≥ 1. The observables are invariant under SL(2, ℤ) at every weight, because ρ_R is a scalar times a signed
  permutation.
- **The search.**
  - On the grid, each sector's log-ratio term and each up–down pair's CKM term are computed once per pair and grid
    point. Every assignment's χ² is then their sum.
  - Every assignment's grid minimum is recorded.
  - A Nelder–Mead refinement in (x, y), from each assignment's 10 best grid points, runs for three sets of
    assignments:
    - the 50 assignments with the lowest grid minimum;
    - every assignment whose grid minimum is below 3 × 7.81;
    - W66's two best (ER′ / ER / EE and ER / ER′ / EE).
- **What a pass would mean.** A pass at a = 0.10 is a candidate, not a derivation, since it is found among 21 952
  assignments. The count drops only if a later arc, rule first, confirms a prediction of the candidate that was not
  fitted: |V_ub|, |V_td| or the first-generation ratios. Those values are read out here and recorded before any such
  test.

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **J1, the instrument** | The double-precision sections agree with the 40-digit ones at W65's sample to 10⁻¹⁰ relative, for all seven. | 95% |
| **J2, W66 inside W69** | W66's best assignment, refined here, reaches χ²_min within 1% of W66's 308.6. | 90% |
| **J3, the verdict** | No assignment passes: every refined χ²_min is above 7.81 at a = 0.10, and every grid minimum of the unrefined assignments is above 3 × 7.81. | 75% |

**The read-outs (no prior).**
- **The ten best assignments at a = 0.10.** For each: χ²_min, τ_min and its distance from ω, the five observables and
  their z, the weights used, and how many refinements reach the minimum.
- **At the best assignment:** m₁/m₃ for each sector, |V_ub| and |V_td|, unfitted.
- **The best χ²_min at a = 0.05 and 0.20,** and the number of assignments passing at each.
- **By weight:** the best χ²_min among the assignments that use only −½, the ones that use a 3/2 section, and the ones
  that use the 7/2 section.

## The reading, written before the run (predicted)

- **The extra weights do not rescue the fit.** Near ω the second-generation ratios differ only by powers and O(1)
  coefficients, and no single δ meets the up sector's 0.0037 and the leptons' 0.059 together. Away from ω the sections
  are generic, and five observables against τ's two numbers is too many.
- **So the data do not fix τ through the parameter-free sections at any weight in the range,** and the count does not
  drop. A fit needs free coefficients per sector, as W65's two-unit Higgs has, and those keep the count where it is.
- **The count stays all 19 of the 19 free** (18 if I-18 is earned). 0 of 19.

## Discipline

- **The rule is committed before the script, and there is one run.** A failed launch (a crash before the read-out) is
  disclosed and fixed, and does not count.
- **Disclosed: the script was drafted before this rule was committed.** It was written after this rule's text, while
  W68's tests ran. It has not been run, and it is committed after this rule.
- **Each cell is recorded as computed.** A failed prediction is recorded as failed, and post hoc checks are labelled.
