# W53 — the rule, recorded before the read-out

The SM-derivation seat, 2026-10-09. Committed with its data file, before the code that reads them exists. The
predictions below were derived by hand before this was written. Nothing here is a result.

## Why this arc

- **The owner's order (2026-10-09):** "we look what fixes τ then we count free numbers."
  - W51 found τ free.
  - W52 counted. At the geometry's weight (k = 3 in every sector), the Standard Model frame T ⊗ T leaves 11 of the
    13 flavour numbers free and predicts two relations, both in the quark sector: eight quark shape numbers (four mass
    ratios and the CKM's four) come from six parameters (τ and two complex coefficients).
  - Whether that structure fits the data was left to a fit.
- **The owner's choice for the fit (2026-10-09): common-scale masses.** "Quark masses run to one scale (M_Z) from a
  cited table, added to the record with its source. The CKM comes from the PDG 2025 data already in the record. The
  tolerance is the data errors plus a stated running uncertainty."
- **Why this one fit decides the count.** By W52's scan and its post-hoc P1, every other weight assignment in either
  frame (weights 1, 3, 5, 7) does one of two things:
  - it has a sector whose coupling is O₊ alone, which forces m₃ = m₁ + m₂ in that sector. Every charged sector
    violates that many times over: ×136, ×43 and ×17 (B1273, B1276 in
    `docs/THE_DESTINATION_LEDGER_2026-09-06.md`, rows 6–14);
  - or it has rank 13 and predicts no relation.

  So T ⊗ T at (3, 3, 3) is the only structure on record that could both fit and predict.

## Weave or thread?

- **The forms are the weave's.** They are equivariant under its whole group (every word in L and R) and built from
  ρ_T, the joint action on the shared records (W50). τ is a state of the weave (W51). The structure is W52's.
- **The claim is about the structure, not about any thread.** The fit asks whether that joint structure meets the
  world's 13 flavour numbers. Weave-type.
- **The tags:**
  - on the ruled branch;
  - given Λ (GENESIS FK11);
  - couplings in τ alone, holomorphic, with one flavour-blind Higgs per sector;
  - weight 3 in every sector (W45's reading).

## The data

- **Masses: Huang and Zhou 2021,** "Precise values of running quark and lepton masses in the Standard Model",
  Phys. Rev. D 103, 016010, arXiv:2009.04851v2.
  - The source: Table 2 (quarks) and Table 3 (charged leptons), the row "M_Z, Full SM".
  - What they are: MS-bar running masses at μ = M_Z = 91.1876 GeV, defined there as m_f = y_f v_F/√2 with
    v_F = 246 GeV. Their inputs are PDG 2020.
  - Transcribed to `received/HZ2021_running_masses_MZ.json` with the PDF's sha256.
  - The values, in GeV:

    | sector | m₁ | m₂ | m₃ |
    |---|---|---|---|
    | up | 0.00123 ± 0.00021 | 0.620 ± 0.017 | 168.26 ± 0.75 |
    | down | 0.00267 ± 0.00019 | 0.05316 ± 0.00461 | 2.839 ± 0.026 |
    | charged leptons | 0.00048307 ± 0.00000045 | 0.101766 ± 0.000023 | 1.72856 ± 0.00028 |
- **CKM: PDG 2025** (eq. 12.27, the global fit), as transcribed in `received/B1612_data.json` (W44):
  - |V_us| = 0.22501 ± 0.00068, |V_cb| = 0.04183 ± 0.00079, |V_ub| = 0.003732 ± 0.000090 and
    |V_td| = 0.00858 ± 0.00019.
  - |V_td| stands in for J. With the three angles it fixes cos δ, and it does not depend on the hand, since J's sign
    is a convention (the reading of W24–W29).
- **Both are taken at M_Z.** The CKM's running below M_Z is negligible at this precision.

## The model and the fit

- **The structure (W52).** At k = 3 the T ⊗ T coupling space has two forms: F₊ in O₊ (symmetric, zero diagonal) and
  F₋ in O₋ (antisymmetric). D has none at k = 3.
- **A sector's Yukawa:** Y_s = e^{c_s}(F̂₊(τ) + ρ_s F̂₋(τ)) for s ∈ {u, d, e}.
  - F̂ = F/‖F‖ (Frobenius) at τ, and ρ_s = exp(u_s + i v_s).
  - This is W52's parametrization rescaled: 11 real parameters (τ, three scales and three complex ρ).
- **The observables (13).**
  - The nine log singular values of the Y_s, ascending in each sector (m₁ < m₂ < m₃).
  - log|V_us|, log|V_cb|, log|V_ub| and log|V_td|, from V = U_u^† U_d, with U_s the left singular vectors in
    ascending order (W52's convention): V_us = V₁₂, V_cb = V₂₃, V_ub = V₁₃, V_td = V₃₁.
- **The tolerance.** Each observable is compared in logs: z_i = (log O_i − log O_i^data)/σ_i, with
  σ_i = √(δ_i² + a²).
  - δ_i is the datum's relative error, and a the running allowance.
  - a = 0.10 for the verdict. a = 0.05 and 0.20 are reported.
  - **Why 10%.** The structure holds at an unknown scale. Between M_Z and a high scale, Standard Model running changes
    the in-sector ratios m_c/m_t and m_s/m_b, and |V_cb|, |V_ub| and |V_td|, by roughly 10 to 20%, and the others by
    less. The cross-sector ratios (m_b/m_τ and the like) run more, but the free scales absorb them.
- **χ² = Σ z_i².**
  - The three scales are profiled analytically (each sector's weighted mean).
  - 13 observables against 11 parameters leaves 2 degrees of freedom.
  - **The fit passes if χ²_min ≤ 5.99** (p ≥ 0.05).
- **The domain.** The observables are invariant under the modular group:
  - ρ_T is unitary in the t basis (W50), and the pieces are invariant;
  - Y(γτ) = (cτ + d)³ ρ̄(γ) Y(τ) ρ̄(γ)^T, so the masses scale together and V is unchanged.

  So τ ranges over the fundamental domain |x| ≤ ½, |τ| ≥ 1, with y ≤ 6. A trial point with |τ| < 1 is mapped in by
  τ → −1/τ and a shift before evaluation, so the q-series are only evaluated at y ≥ √3/2.
- **The search, fixed here.**
  1. **A grid of τ:** x in 21 steps over [−½, ½] and y in 28 geometric steps over [0.87, 6], kept where |τ| ≥ 1.
  2. **Per sector at each grid τ:** ρ_s is fitted to the sector's two log mass ratios (Levenberg–Marquardt) from 72
     starts (|ρ| = 10⁻² to 10² in 9 steps, and 8 phases). The best three distinct minima are kept.
  3. **At each grid τ:** the χ² of the best of the 27 combinations.
  4. **The joint refinement:** all eight shape parameters (bounded least squares, scales profiled), from the 60 best
     grid points and 200 random starts (seed 5300).
  5. **The other objectives:** the same refinement for the masses-only objective (the nine log masses), and at
     a = 0.05 and 0.20.
  6. **For F1:** each sector's own two ratios, refined over (τ, ρ_s) from that sector's 30 best grid points.
- **The global minimum** is the lowest χ² found. The number of starts that reach it (within Δχ² < 0.1) is reported.

## The facts by hand

1. **The cusp's exponents.**
   - ρ_T(T) has eigen-turns ⅛, ⅜ and ⅞ (W45, W50).
   - By W50's N6 these belong to θ₂² (the parity (0, ½), the middle index of t), θ₃² − θ₄² and θ₃² + θ₄².
   - A coupling in ρ_T^∨ ⊗ ρ_T^∨ has q-exponents −(a + b) mod 1. So:
     - the entries joining the middle parity to the outer two, in their combination with θ₃² + θ₄², have exponent 0,
       the constant term;
     - O₊'s (1, 3) entry has exponent ¼, and O₋'s has ¾;
     - the other combination of the middle row and column has ½.
2. **The k = 3 forms have constant terms.**
   - O₊'s generators sit at weights 1, 3 and 5, with Σk = 12·(0 + ¼ + ½) = 9, as W52's dimensions 1, 1, 2, 2 show.
   - The weight-3 space is one-dimensional, so its form is the Serre derivative D of the weight-1 form F₁. Its
     leading coefficients are (λ − 1/12) times F₁'s.
   - With F₁, DF₁ and D²F₁ generating, their Wronskian is a multiple of η¹⁸. So every leading coefficient of F₁ is
     nonzero, and so is every one of DF₁'s.
   - W52's profiles agree. At y = 3 the smallest singular value over the largest is 0.0251 at k = 1 and 0.0495 at
     k = 3. The ratio is 1.97, against the 2 the derivative predicts (|¼ − 1/12| over |0 − 1/12|).
3. **Near the cusp, at leading order.**
   - Y_s is close to its constant term, which lives in the middle row and column. That term has two entries,
     α_s = c₀ + ρ_s d₀ and β_s = c₀ − ρ_s d₀ (up to normalization), and singular values √2|α_s|, √2|β_s| and 0.
   - O₊'s (1, 3) term lifts the zero at q^{1/4}, and that first-order value does not depend on ρ_s.
   - **Regime A** (q^{1/4} ≪ m₂/m₃ ≪ 1): m₁/m₃ ≈ κ q^{1/4}, the same in every such sector. κ ≈ 2.8: half of W52's
     k = 3 ratio at y = 3 (0.0495, where α = β), divided by q^{1/4} = e^{−3π/2}.
   - **Regime B** (β_s ≲ q^{1/4}): here m₂/m₃ equals κ q^{1/4}, and β_s tunes m₁.
   - The left singular vectors are fixed at leading order, the same in every sector: the middle parity, and a phased
     sum and difference of the outer two.
4. **The sectors want different τ.** With q^{1/4} = e^{−πy/2} and κ = 2.8, the data need:
   - u: y ≈ 4.2 (regime B, m_c/m_t = κ q^{1/4}). Regime A needs y ≈ 8.2, outside the domain.
   - d: y ≈ 5.1 (A) or 3.2 (B).
   - e: y ≈ 5.85 (A) or 2.45 (B).

   No y serves all three. By this estimate the best common compromise costs χ² ≈ 190 in the masses alone
   (a = 0.10).
5. **Away from the cusp the hierarchies are hard to reach.**
   - A zero-diagonal 3 × 3 matrix is near rank one only near a single row or column, that is, with four entries
     small. Two complex parameters (τ and ρ) do not reach that generically.
   - At i and ω the couplings have degenerate pairs or zeros (W50).
   - So m_c/m_t ≈ 0.004 needs the cusp, unless a special point the hand analysis misses supports it.
6. **The CKM near the cusp** is close to a permutation (fact 3's fixed vectors), and |V_us| = 0.225 is hard to reach.
   That adds to the χ², but the verdict does not need it if fact 4 holds.

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **M0** | The controls. (a) At k = 3 there is one form in O₊ and one in O₋, symmetric and antisymmetric, with zero diagonal. (b) ρ_T(S) and ρ_T(T) are unitary in the t basis. (c) The ten shape observables (six log ratios, four log \|V\|) are unchanged under τ → τ + 1 and τ → −1/τ at five random points, to 10⁻⁸. (d) The 13 × 11 Jacobian has rank 11 at three random points. (e) In W52's recorded scan every assignment without an O₊-alone sector has rank 13, except T ⊗ T at (3, 3, 3), with 11. | 97% |
| **F1** | Each sector alone is reachable. For each of u, d and e, some τ in the domain and some ρ_s reproduce the sector's two log mass ratios to 10⁻⁶. | 85% |
| **F2** | The masses alone cannot all be fit at one τ. The masses-only χ²_min (nine log masses, eleven parameters, a = 0.10) exceeds 5.99. | 70% |
| **F3** | The fit, the arc's question: χ²_min ≤ 5.99 at a = 0.10, with 13 observables and 11 parameters. | 10% |
| **F4** | The cusp's universality. At τ = 5i, take a grid of ρ (\|ρ\| = 10⁻³ to 10³ in 601 steps, 1440 phases). Every point with m₂/m₃ ∈ [0.005, 0.05] has m₁/m₃ ∈ [0.95, 1.20] × 10⁻³ (κ q^{1/4} = 1.07 × 10⁻³), and at least 20 points fall in the window. | 75% |

F2 and F3 are tied: if F2 holds, F3 fails.

**Extra read-outs (no prior).**
- χ²_min at a = 0.05 and at a = 0.20.
- The best fit: τ (and its distance from i and ω), the three ρ_s, and the thirteen pulls.
- The τ of the masses-only best fit.
- Where each sector alone is reachable (F1's τ).
- The grid's best χ² in bands of y.
- The number of starts that reach the global minimum.

## The reading, written before the run

- **If F3 holds,** the weave's modular structure at the geometry's weight fits the 13 flavour numbers with 11.
  - It predicts two quark relations.
  - τ is the fit's own; W51 found nothing canonical that fixes it.
  - The tally stays W52's: at most 17 of the 19 free on the ruled branch, given Λ.
- **If F3 fails,** that structure is excluded at the stated allowance. By M0(e) and W52's P1, no structure on record
  both fits the data and predicts a flavour relation. Then:
  - the weave's modular structure predicts no flavour relation that the data allow;
  - its free flavour numbers are 13 if some structure with P ≥ 13 fits. That is not tested here; it is a later arc.
    The tally is then at most 19 of the 19, or 18 if I-18 is earned;
  - if no structure fits at any weight, the modular structure is excluded as the Yukawas' source on the ruled branch.
- **If F2 holds,** the failure is in the masses, before the CKM. The three sectors' hierarchies need three different
  τ (facts 3 and 4, and F4 if it holds).
- **If F3 fails at a = 0.10 but passes at a = 0.20,** it is recorded as failed, and the a = 0.20 read-out is reported
  as a weaker reading.
- **If F2 fails,** some point the hand analysis missed carries the hierarchies. Its τ is reported.

## Discipline

- The data file and this rule are committed together, before the code. Nothing was computed for this arc before the
  commit. W52's recorded profiles and W50's recorded N6 were read, not recomputed.
- One run. A failed launch (a crash before the read-out) is disclosed and fixed, and does not count as a run.
- Each cell is recorded as computed, and a failed prediction is recorded as failed.
- Post-hoc checks are labelled.
