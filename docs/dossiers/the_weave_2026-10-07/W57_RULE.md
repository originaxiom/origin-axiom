# W57 — the rule, recorded before the read-out

The SM-derivation seat, 2026-10-13. Committed before the code that reads it exists. The predictions below were derived
by hand before this was written. Nothing here is a result.

## Why this arc

- **The owner's framing (2026-10-13).** "Could it be that the field is the opposite maybe, a field of maximality
  compared to the seed of minimality. A sea of potential where anything is allowed." The dossier's "Reading: the seed of
  minimality and the field of maximality" records it. The owner agreed that a typicality test should follow, rule
  first.
- **The question.** Is the world a typical draw from the seed's own measure? The hypothesis H_max:
  - the seed fixes the shapes, meaning the forms and the placements it allows;
  - the field takes every state the seed allows, distributed by the seed's own invariant measure;
  - the observed flavour numbers are a typical draw from it.
- **The owner's further question** (how can we be sure we expect the right numbers?) is answered by three guards:
  - **ratios at a stated scale, repeated at a second scale.** Two mass tables at different scales, from one source;
  - **the analyst's bias.** The rule comes first and there is one run;
  - **observer selection.** A conditioned version is reported, labelled and separate. It never rescues the main test.

## Weave or thread?

- **Weave-type.**
  - The measures are invariant under the weave's whole group.
  - The placements are every one the seed supplies at the geometry's weight (W56), none hand-picked.
  - The claims concern the measure as a whole.
- **The tags.** On the ruled branch; given Λ (GENESIS FK11); the Standard Model frame; couplings holomorphic in τ.

## The field's states and the seed's measures

- **The placements** are W56's four at the geometry's weight:
  - (H_u, H_d) ∈ {(B, B), (B, D), (D, B), (D, D)};
  - B is flavour-blind (W53's two forms at k = 3);
  - D is the dual triplet (R_D's 8 forms at 9/2);
  - **S_mix**, the main model, gives each placement the same weight;
  - each placement alone is a read-out.
- **τ follows the hyperbolic measure** dx dy / y² on the whole fundamental domain, the cusp included. It is the only
  measure the moves keep. It is sampled exactly:
  - θ uniform on [−π/6, π/6], and x = sin θ;
  - y = cos θ / U, with U uniform on (0, 1].
- **At each τ the couplings follow the invariant Gaussian on the space the seed allows there.**
  - **A B sector:** the 2-dimensional span of W53's forms at τ, in ℂ^{3×3} with the Frobenius metric. Y = Σ β_b E_b,
    with E an orthonormal basis of the span and β standard complex Gaussian.
  - **A D sector:** W = Σ γ_c Q_c over an orthonormal basis Q of the 8-dimensional span of R_D's forms at τ in ℂ²⁷,
    with γ standard complex Gaussian. h is standard complex Gaussian in ℂ³, and Y_ij = Σ_k W_ijk h_k.
  - d and e share h_d, and their W's are independent.
  - These are unitarily invariant, so under the moves the measure is invariant: nothing is added.
- **The null, anarchy.** Each Y_s is an independent standard complex Gaussian 3 × 3 matrix, with no τ and no seed
  structure.

## The observables and the data

- **The ten shape numbers.**
  - The log mass ratios log(m₁/m₃) and log(m₂/m₃) in each sector.
  - log |V_us|, log |V_cb|, log |V_ub| and log |V_td|, with V = U_uᴴ U_d from the left singular vectors in ascending
    order (W53's convention).
  - The scales carry no shape, and are dropped.
  - Logs below log 10⁻¹⁶ are set to that value: numerical floor, far below every datum.
- **The data at M_Z** are W53's: `received/HZ2021_running_masses_MZ.json` and `received/B1612_data.json`. The ten
  values, by hand: u (−11.83, −5.60), d (−6.97, −3.98), e (−8.18, −2.83); the CKM (−1.49, −3.17, −5.59, −4.76).
- **The data at 10¹² GeV**, the robustness scale: `received/HZ2021_running_masses_1e12.json` (same paper, same PDF,
  Table 2 and Table 3's row at 10¹² GeV). The CKM is kept at its low-scale values.
- **The tolerance** σ_i = √(δ_i² + a²), with a = 0.10 (W53).
  - δ_i is the relative error, combined in quadrature over the two masses of a ratio.
  - For a |V| it is the relative error of that |V|.

## The test

- **The draws.**
  - 250 000 per placement, so S_mix has 10⁶. The seeds come from (5700, the placement's index, the batch index).
  - 10⁶ for anarchy (seed 5701).
  - 200 pseudo-data from S_mix: a uniform placement, then a draw, from an independent stream (seed 5702).
- **The distance** from a draw x to a target t: d(x, t) = max_i |x_i − t_i| / σ_i.
- **The acceptance** A(ε) is the fraction of a model's draws with d ≤ ε, on the ladder ε ∈ {2, 4, 8, 16, 32, 64}.
- **ε\*** is the smallest rung at which S_mix accepts at least 20 draws around the data at M_Z.
- **T1, the seed against anarchy.**
  - R = A_S(ε\*) / A_A(ε\*), at ε\*.
  - If anarchy accepts no draw, A_A is replaced by its 95% upper bound 3/N.
- **T2, typicality under the seed.**
  - For each pseudo-datum, count S_mix's draws within ε\* of it. Do the same for the data.
  - p = (1 + #{pseudo-data whose count ≤ the data's}) / 201.
- **T3, the marginals.** For each of the ten numbers, the two-sided empirical p of the datum under S_mix:
  2 min(F, 1 − F), with F the empirical CDF with one count added at each end.
- **T4, the control.** The same marginal under anarchy for log(m_u/m_t).

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **T1** | R ≥ 10: the seed's measure makes the data at least ten times as probable as anarchy does, at ε\*. | 85% |
| **T2** | p < 0.05: the data are not a typical draw from S_mix at ε\*. | 70% |
| **T3** | Each of the ten numbers alone is typical under S_mix: every two-sided p ≥ 0.01. | 60% |
| **T4** | Anarchy fails the up quarks' hierarchy: two-sided p < 0.001 for log(m_u/m_t). | 95% |

**The hand reasons.**
- **T1.**
  - Under anarchy, the smallest singular value of a complex Gaussian matrix makes P(m₁/m₃ < x) of order x².
  - Combined over the three sectors and the small CKM, the data's neighbourhood at ε ≤ 16 has probability below
    10⁻¹⁰, so no anarchy draw is accepted and the bound 3 × 10⁻⁶ applies.
  - The seed reaches hierarchies through the cusp, where P(y > Y) ≈ 0.9/Y: a heavy tail. Its acceptance at ε\* should
    be 10⁻⁵ to 10⁻⁴.
- **T2.**
  - The data need deep hierarchies, at different depths in each sector. W53's F1 put the flavour-blind sectors at
    y ≈ 8.2 for u, 5.1 for d and 5.9 for e.
  - A typical draw sits at y around 1 to 2, with weak hierarchies and large mixings, where the draws are densest.
  - So the data's neighbourhood should be sparse compared with a typical draw's.
- **T3.** Each number alone is reachable through the cusp's heavy tail.
- **T4.** P(m_u/m_t < 7 × 10⁻⁶) is of order 10⁻¹⁰ under anarchy.

**The read-outs (no prior).**
- **For each placement:** its acceptances on the ladder, its T2 p, and its marginals.
- **The robustness scale (10¹² GeV).** T1, T2 and T3 again, with the same draws.
- **The observer-conditioned version (labelled; it cannot rescue T2).**
  - Keep only draws whose three lightest-to-heaviest ratios are all below 10⁻², a crude proxy for a light first
    generation. The pseudo-data are taken from the conditioned S_mix.
  - Recompute R and p.

## The reading, written before the run

- **If T1 holds and T2 goes as predicted:**
  - the seed's structure helps: it makes hierarchies cheap where anarchy cannot;
  - but the world is not a typical draw from the seed's own measure at the geometry's weight;
  - so the field of maximality, in its simplest form (the seed's measure, every placement at the geometry's weight), is
    excluded. Something selects within the sea: a measure that is not the seed's own, or the selection the record
    keeps looking for (GENESIS FK9).
  - The observer-conditioned read-out then says whether the atypicality is the observer's own selection. It is
    reported, not used to rescue.
- **If T2 fails (the data are typical):** the owner's hypothesis survives its first test. The flavour numbers look like
  a typical draw. "Deriving them" becomes deriving the measure, and the next test is a sharper statistic.
- **If T1 fails:** the seed's forms add nothing statistically over anarchy at this resolution.
- **If the robustness scale agrees,** the verdict does not hinge on the scale of comparison.
- **Either way the count stays all 19 of the 19 free as numbers** (18 if I-18 is earned). What changes is whether the
  record can speak of their distribution.

## Discipline

- One run. A failed launch (a crash before the read-out) is disclosed and fixed, and does not count as a run.
- Each cell is recorded as computed, and a failed prediction is recorded as failed.
- Post-hoc checks are labelled.
