# The twisted-units comparison: a design draft (unsealed; fixed before the units exist; refereed twice)

chat1 (the web seat), 2026-10-15. **This is not a seal.** It fixes the comparison's shape before the SM seat's units
exist, so that nothing about the units can shape it. The seal will repeat this design. Any change after this draft will
be listed in the seal with its reason. Nothing here is a result.

## Why this arc

- **The owner's ruling, as chat1 reports it** (received 15:19 by this seat's clock: "continue as u recomend", on
  chat1's recommendation at `818db8b8d`):
  - **the SM seat builds the twisted matter units:** ρ_R sections with characteristic, per field, if ρ_R admits them.
    That is the 15:17 addendum's question, and the SM seat's to answer;
  - **chat1 carries them along the threads** and seals the comparison at N = 9, 11 and 12;
  - **the SM seat checks it blind** after the seal, before reading chat1's run.
- **Why the units must be twisted.** In the minimal reading (only the coupling vector twisted), the deep-cusp
  exponents are W84's in every sector (the 15:17 addendum). That comparison is already scored: §117, W88's Q6,
  Σz² = 57. Sector-dependent exponents need sector-dependent units (W84, §106 item 4).

## The question

With matter units carrying their own characteristic, do the thread frame's cells, on the threads where an order-N
hypercharge line closes (N = 9, 11, 12), give per-sector mass ratios that meet the data under W66's predicate?

## Premises (named)

- **H-thread:** couplings are cycle integrals along the vacuum's closed geodesic (W72, chat1's thread frame).
- **The vacuum's thread is one on which the line closes all three sectors.** Two thread families are scored apart.
  Neither is picked.
  - **T-tower:** the least-volume candidates, the family the record's action would favour if volume dominates (the
    13:43 addendum). These are L·Rⁿ of either sign with n ≤ 3N², admitted only if they close.
  - **T-low:** closing threads of height at most 3, with words up to length 12.
    - They are enumerated by script before any unit is evaluated.
    - They are scored only if the SM seat supplies the units' multiplier for the reduction, or series long enough for
      the period's lowest point, y ≈ 1/|C|. Otherwise they are excluded, with that reason.
- **The units, the coupling vector, the Higgs modes and the completions are as the SM seat delivers them,** at a stated
  commit.
  - Any choice inside them is the SM seat's, and is cited, not made here.
  - THETA2's β = (−224, −4, −112) and the ORTH construction were built for untwisted units. They are used only as
    delivered or re-derived for the twisted units. Otherwise those cells are excluded, with that reason.

## Admissibility (no mass computed)

- **Closure.** The instrument's closure test is run on the delivered units, coupling vector and Higgs modes, on every
  candidate thread at N = 9, 11 and 12.
  - The minimal reading's law only proposes the candidates. Only threads that close are admitted.
- **Lines.** Every order-N line the thread fixes counts, up to sign.

## What is computed (one run)

- **A configuration is (thread, line, cell).**
  - The cells are C1, C2/{E4, THETA2, ORTH} and C3/{E4, THETA2, ORTH}, built as the 15:17 addendum's instrument builds
    them, with the delivered units.
  - All three sectors and the CKM are computed in the same configuration. Q's units are shared by up and down.
- **Per sector:** R₂ = m₂/m₃ and R₁ = m₁/m₃, from the singular values of K_L^(−½) Y K_R^(−½ᵀ).
- **CKM moduli:** |V_us|, |V_cb| and |V_ub|, from V = U_upᴴ U_down, with U the left singular vectors.
- **The instrument's own error, r_calc:** the larger relative change of each quantity between two comparisons:
  - Npts against 1.25·Npts;
  - the full coefficients against the coefficients rounded to 53 bits.
- **Failures count; nothing is dropped.** A configuration fails, and is counted, if it has a zero singular value or
  cannot be computed to the stated bound.
  - T-tower at k = 3 reaches y ≈ 120–220. That needs roughly 2,500–3,500 bits and about 10⁴ points; the cost is
    measured before the seal.

## The scoring: W66's predicate as W88 used it (a = 0.10), extended to k = 6

- **Data:** at M_Z, as W88 used them.
  - Masses: the SM seat's `received/HZ2021_running_masses_MZ.json`.
  - CKM: `received/B1612_data.json`.
  - Any other scale is a read-out only.
- **For each equality:** z = (ln X − ln Y)/√(r_calc² + r_data² + a²).
- **S-mass:** the six equalities (R₁ and R₂ in three sectors) in one configuration. It passes if Σz² ≤ 12.59, the 95%
  point for 6 degrees of freedom.
- **S-shape:** W88's Q6 form with the computed ratio, z = ln(ρ_calc/ρ_data)/√(r_calc² + r_s² + a²), where
  ρ = ln R₁ / ln R₂. There are three equalities; it passes if Σz² ≤ 7.81.
- **S-ckm:** three equalities. It passes if Σz² ≤ 7.81.

## The base rate and the one primary claim (fixed now)

- **The null:** other hypercharge-like charge assignments, put through the same configurations.
  - These are integer 6Y charges (q_Q, q_u, q_d, q_L, q_e, q_H) with the three vertices neutral: Q·u^c·H, Q·d^c·H̄ and
    L·e^c·H̄.
  - The box is |q| ≤ 12. The SM's assignment and its negative are excluded.
  - M of them are drawn with a fixed seed. M is at least 99, and is set in the seal from the measured cost.
    - If the cost allows M ≥ 99 only on part of T-tower, the seal restricts the primary claim to that part, before the
      run.
  - The same integer assignment is used at every N, reduced mod N.
  - **Eligibility.** A null assignment counts only if it is eligible at all of N = 9, 11 and 12, on the SM's terms
    there:
    - the three sectors' coupling vectors split, with no coincidence up to sign;
    - no sector is untwisted, so (ū, δ) are not both in Λ.
    - Draws ineligible at any of the three are replaced by further draws with the same seed.
  - **Draws ≡ k·SM mod N,** for k a unit mod N, at any of the three N, are excluded, and their number is reported. They
    relabel the SM's lines.
  - **The SM's null leptons at N = 9 are not matched in the null.** That is stated, and the null's patterns are
    reported.
- **Why not the field permutations.** Permuting the five fields' charges breaks the vertices' neutrality. Its six or
  120 cases would also limit p to 1/6 or 1/120.
- **The primary claim:** S-mass on T-tower, pooled over N and lines on one configuration set for every assignment.
  - **The set:** the lines with N² | Q_γ(w), where closure does not depend on the charges.
  - Closure with the delivered units is still checked there for each assignment. If any assignment fails to close
    somewhere in the set, the statistic becomes that assignment's pass fraction over its admitted configurations, and
    the admitted counts are reported.
  - **It is earned if p ≤ 0.05, one-sided,** with p = (1 + #{null assignments scoring at least the SM's})/(M + 1).
- **Everything else is a read-out:** S-shape, S-ckm, T-low and each N alone. These carry a Bonferroni correction over
  the number of such claims, which is fixed in the seal.
- **The untwisted units are a sanity control,** not a base rate.

## Controls the instrument must pass first (on the delivered units; no N = 9, 11 or 12 mass)

- With the units untwisted, it reproduces `818db8b8d`'s numbers on its towers.
- **The excluded-order coincidences**, with units twisted by charges reduced mod N:
  - at N = 3, up = down in every cell, and the leptons are untwisted;
  - at N = 5, down = leptons, and at N = 7, up = leptons, in C1 only. In C1 the left and right units share a weight;
    elsewhere the pairs swap sides.
- Closure on every admitted thread, and quadrature convergence, both to stated bounds.

## Seen before this draft (disclosed)

- The data's log-ratios, 2.11, 1.75 and 2.89 (§117), and the masses' sizes.
- The minimal reading on the excluded-order towers (`818db8b8d`).
- No twisted unit exists yet. Nothing at N = 9, 11 or 12 has been computed.

## What the outcomes would mean (fixed with priors in the seal)

- **The primary claim is earned.** That family, with the SM seat's units, would give a candidate fit with every discrete
  choice (family, N, line, cell) counted. It would go to main as a candidate, not as a relation with no free size.
- **Nothing passes.** That excludes the fuller reading with these units on that family, and nothing wider.
- **Passes at the null's rate.** That is look-elsewhere, not evidence.

chat1, 2026-10-15. 0 of 19.
