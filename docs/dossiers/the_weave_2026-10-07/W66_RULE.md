# W66 — the rule, recorded before the code

The SM-derivation seat, 2026-10-14. Committed before the code that reads it exists. What the seat worked by hand while
drafting is listed under "Seen before the rule", and the priors were set after that. Nothing here is a result.

## Why this arc

- **W65 made the second generation's mass a function of τ.** Read as a section of the matter's bundle (H-sec), the
  Higgs's direction is fixed by end data. For the one-unit placements the section space is one-dimensional, so these
  sections carry no free coefficient at all.
- **The owner's order is "we look what fixes τ then we count free numbers".** This arc counts. Take B1644's Yukawa form
  Y(a; c) = a cᵀ + c aᵀ − (a·c)𝟙 with both the Higgs a and the coupling c among the parameter-free sections. Then every
  sector's Yukawa depends on τ alone, up to its overall scale. If one τ fits more observables than its two real
  numbers, the count drops.

## Weave or thread?

- **Weave-type.** It takes every assignment of the parameter-free pairs to the three charged sectors (none chosen),
  and τ over the whole fundamental domain.
- **The tags.** Given Λ (GENESIS FK11). Three hypotheses, stated:
  - B1644's form at the puncture (P-108's parent map owed; Review 63's P-122 scopes its base);
  - H-sec (W65): the Higgs's direction is a section of weight −½ in ρ_R at the vacuum's τ;
  - **H-pair (new):** the coupling c is also a one-unit section, not only main's R.
  GENESIS FK10's unit is a tagged working postulate.

## The objects (fixed here)

- **The parameter-free sections** are W65's one-unit sections E, R and R′, each the unique section of its placement up
  to scale.
- **A pair** {a, c} gives Y(a; c), symmetric in a and c. There are six pairs: EE, ER, ER′, RR, RR′ and R′R′.
- **An assignment** gives one pair to each of the up, down and charged-lepton sectors: 6³ = 216 assignments.
- **The neutrinos are not in scope.**

## Seen before the rule (disclosed; by hand and from W65's committed read-outs)

- **Rank.**
  - If a and c are both isotropic, Y has rank one: Y = n nᵀ/(a·c) with n = a × c, or 2aaᵀ when a = c. So RR, R′R′ and
    RR′ give m₂ = 0 at every τ.
  - If exactly one of them is isotropic, Y has rank two, with null vector the isotropic one. So ER has m₁ = 0 with null
    vector R, and ER′ has m₁ = 0 with null vector R′.
  - EE is Y = (E·E)(2ÊÊᵀ − 𝟙), and 2ÊÊᵀ − 𝟙 is complex orthogonal. Its singular values are (σ, 1, 1/σ), so
    **m₁m₃ = m₂² exactly** for EE.
- **Where they vanish.** At ω all three sections are parallel (W65), so every pair has rank one there.
  - ER and ER′ also have m₂ = 0 where E·E = 0 (τ₀, j = 1280); W65 found that for ER.
  - EE has rank one at τ₀.
- **Which assignments are live.** The data's three m₂/m₃ are distinct by factors of 3 to 16.
  - An assignment with a rank-one pair has m₂ = 0 in that sector.
  - Two sectors sharing a pair have equal m₂/m₃ at every τ, beyond the allowance.
  - If up and down share a pair, V is the identity and |V_us| = 0.
  - So only the six permutations of (EE, ER, ER′) over (up, down, leptons) can pass.
- **W65's arc read-outs, seen.** On the arc near ω, m_E reaches the up sector's 0.0037 near
  τ = e^{iθ} with θ ≈ π/2 + 38.8 (π/240). There R and R′ overlap at about 0.992 (Hermitian, normalized). If one sector's
  massless state were R̄ and the other's R̄′, the Cabibbo element would be about √(1 − 0.992²) ≈ 0.13, not 0.225. This
  is a rough estimate only: the full V is computed here.
- **The data**, as in W53:
  - masses at M_Z from Huang and Zhou 2021 (`received/HZ2021_running_masses_MZ.json`): m_c/m_t = 3.685 × 10⁻³ (2.8%),
    m_s/m_b = 1.872 × 10⁻² (8.7%) and m_μ/m_τ = 5.887 × 10⁻² (0.03%);
  - the CKM from PDG 2025 (`received/B1612_data.json`): |V_us| = 0.22501 (0.30%) and |V_cb| = 0.04183 (1.9%).

## The fit (fixed here)

- **The observables (five, at leading order).**
  - The three log(m₂/m₃).
  - log|V_us| and log|V_cb|, from V = U_u^† U_d, with U the left singular vectors in ascending order (W52's and W53's
    convention): V_us = V₁₂ and V_cb = V₂₃.

  The first generation is massless in the rank-two pairs, so m₁/m₃, |V_ub| and |V_td| are read out, not fitted.
- **The tolerance (W53's).** z_i = (log O_i − log O_i^data)/σ_i with σ_i = √(δ_i² + a²). Here δ_i is the datum's
  relative error, and a is the running allowance: a = 0.10 for the verdict, with 0.05 and 0.20 reported.
- **χ² = Σ z_i²**, with five observables against τ's two real numbers: 3 degrees of freedom. **An assignment passes if
  χ²_min ≤ 7.81** (p ≥ 0.05). A zero mass or a zero |V| scores χ² = ∞.
- **The domain.** The observables are invariant under SL(2, ℤ). The pairs have weight −1 in ρ_R ⊗ ρ_R, and ρ_R is a
  scalar times a signed permutation. So τ ranges over the fundamental domain |x| ≤ ½, |τ| ≥ 1, y ≤ 6.
- **The search.**
  - A grid: x in 41 steps over [−½, ½] and y in 40 geometric steps over [0.87, 6], kept where |τ| ≥ 1.
  - For each of the 216 assignments, a Nelder–Mead refinement in (x, y) from its 10 best grid points. Trial points
    outside the domain are mapped in.
- **The instrument.** W65's sections, solved again by its 40-digit collocation (W65's `solve_section`), then
  evaluated in double precision from their q-expansions. The check: at W65's sample, the double-precision values
  agree with the 40-digit ones to 10⁻¹⁰ relative.

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **C1, the rank** | At W65's twenty sample points, away from ω and τ₀ by 0.05: RR, R′R′ and RR′ have m₂/m₃ < 10⁻¹². ER and ER′ have m₁/m₃ < 10⁻¹², with null vectors R and R′ (sine below 10⁻¹⁰), and m₂/m₃ > 10⁻⁹. EE has \|m₁m₃/m₂² − 1\| < 10⁻¹⁰. | 95% |
| **C2, the live assignments** | Every assignment that is not a permutation of (EE, ER, ER′) has χ²_min > 7.81 at a = 0.10. | 90% |
| **C3, the verdict** | No assignment passes: χ²_min > 7.81 for all 216 at a = 0.10. | 80% |

**The read-outs (no prior).**
- For each of the six permutations: χ²_min, τ_min, the five observables and their z at the minimum, and how many of the
  ten refinements reach it (within Δχ² < 0.1).
- At each permutation's minimum: m₁/m₃ for its EE sector (m₁m₃ = m₂²), |V_ub| and |V_td|.
- The best χ² at a = 0.05 and a = 0.20.
- **Two at a time.** For the permutation with up = ER: the smallest z(m_c/m_t)² + z(V_us)² over τ. This asks whether the
  up ratio and the Cabibbo angle can both be met at one τ.

## The reading, written before the run (predicted)

- **Only three of the six pairs give a second generation at all,** and only their six permutations can fit. The
  rank-one pairs (both sections isotropic) give one heavy generation per sector.
- **No assignment fits.**
  - The three ratios are functions of one τ that all vanish together at ω and grow from there.
  - The Cabibbo angle needs the massless states R̄ and R̄′ to separate, which happens away from ω.
  - Near ω the ratios are small enough, but the overlap is too close to 1.
- **So the parameter-free sections do not fix τ by the data, and the count stays all 19 of the 19 free** (18 if I-18 is
  earned). 0 of 19. Under H-sec and H-pair, the second generation needs a two-unit Higgs (W65), whose free |α/β| per
  sector keeps the count where it is.
- **If an assignment passes,** τ is fixed by two observables, and the other three are predictions given the three
  hypotheses. That would be the first drop in the count.

## Discipline

- **The rule is committed before the script, and there is one run.** A failed launch (a crash before the read-out) is
  disclosed and fixed, and does not count.
- **Each cell is recorded as computed.** A failed prediction is recorded as failed, and post hoc checks are labelled.
