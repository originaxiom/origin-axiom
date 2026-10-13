# W54 — the rule, recorded before the read-out

The SM-derivation seat, 2026-10-09. Committed before the code that reads it exists. The predictions below were derived
by hand before this was written. Nothing here is a result.

## Why this arc

- **The owner's choice (2026-10-09), after W53:** "Test the rank-13 structures."
- **What is left.** In the record's two frames, at weights 1, 3, 5 and 7:
  - every structure with a sector whose coupling is O₊ alone fails m₃ = m₁ + m₂ (W52);
  - the three structures with rank 11, T ⊗ T at (3, 3, k_e), fail the fit (W53 and its post hoc);
  - every other structure has rank 13: as many free numbers as flavour numbers, so it predicts no relation.
- **The question.** Does any rank-13 structure fit the data at all?
  - If one does, the count of 13 is realised.
  - If none does, the weave's modular structure is excluded as the Yukawas' source on the ruled branch, given Λ.
- **The set, 32 structures:**
  - T ⊗ T with every k_s ∈ {3, 5, 7} and (k_u, k_d) ≠ (3, 3): 24 assignments;
  - Sym² T with every k_s ∈ {5, 7}: 8 assignments.

## Weave or thread?

- The forms are the weave's: equivariant under its whole group, built from ρ_T (W50). τ is a state of the weave (W51).
- The claim is about every structure in the set at once, under a stated rule. Weave-type.
- The tags: on the ruled branch; given Λ (GENESIS FK11); couplings in τ alone, holomorphic, with one flavour-blind
  Higgs per sector.

## The data

W53's, unchanged:
- the masses from `received/HZ2021_running_masses_MZ.json`;
- the CKM's |V_us|, |V_cb|, |V_ub| and |V_td| from `received/B1612_data.json`.

## The model and the fit

- **A sector's Yukawa:** Y_s = Σ_i α_{s,i} F̂_i(τ).
  - The sum runs over W52's basis of the coupling space at weight k_s in the frame: D, O₊ and O₋ in T ⊗ T; D and O₊ in
    Sym² T.
  - F̂ = F/‖F‖ (Frobenius) at τ, and α_s ∈ ℂ^{d(k_s)}.
  - The scale and one phase of α_s are redundant: the scale is profiled, and the phase drops out of every observable.
- **The observables, the tolerance and χ²** are W53's: the nine log masses and four log |V|, with
  σ_i = √(δ_i² + a²) and a = 0.10.
- **The parameters.** P = 2 + Σ_s (2 d(k_s) − 1) ≥ 13, rank 13 (W52), so no degree of freedom is left.
- **A structure fits if χ²_min ≤ 5.99**, W53's threshold. Here that is a lenient test, since nothing is predicted. It
  fits exactly if χ²_min ≤ 0.01.
- **The domain** is W53's: the fundamental domain with y ≤ 6, a trial τ reduced into it before evaluation.
- **The decomposition.** At a fixed τ the quark observables depend only on α_u and α_d, and the lepton masses only
  on α_e. So χ²(τ) = Q_{k_u k_d}(τ) + E_{k_e}(τ), each minimised on its own.
- **The search, fixed here.**
  1. **A grid of τ:** x in 11 steps over [−½, ½] and y in 16 geometric steps over [0.87, 6], kept where |τ| ≥ 1.
  2. **At each grid τ:**
     - Q for each quark weight pair of each frame (8 in T ⊗ T, 4 in Sym² T), from 16 random starts;
     - E for each lepton weight of each frame (3 and 2), from 8 random starts;
     - both by trust-region least squares, with seeds drawn from (5400, the pair's or weight's index, the grid
       index).
  3. **Each assignment's grid values** are Q + E.
  4. **A joint refinement for each of the 32:** bounded least squares over τ and every α, from the assignment's 8
     best grid points.
  5. **χ²_min** is the lowest value found.
- **The rank-one test (H1).** For each weight k ∈ {3, 5, 7} in T ⊗ T, at three random τ (seed 5401) in
  x ∈ [−0.4, 0.4], y ∈ [1.05, 2]:
  - minimise the 2 × 2 minors of Y/‖Y‖ over α, from 20 starts;
  - μ_k(τ) is m₂/m₃ at the minimum, the span's closest approach to rank one.

## The facts by hand

1. **Sym² T sits inside T ⊗ T at the same weights.** Its forms are the same D and O₊ forms, with O₋'s coefficients set
   to zero. So a Sym² T structure's χ²_min is at least its T ⊗ T counterpart's.
2. **Where a span holds a rank-one coupling (a Segre count).**
   - A rank-one matrix a bᵀ has four free numbers, since (a, b) ∈ ℙ² × ℙ².
   - To lie in the span at weight k it must meet three conditions:
     - its diagonal is proportional to D's: 2 conditions with one D form, 3 (a zero diagonal) with none;
     - its symmetric off-diagonal part lies in O₊'s span: 3 − n₊ conditions;
     - its antisymmetric part lies in O₋'s span: 3 − n₋ conditions.
   - **k = 3** (n_D, n₊, n₋ = 0, 1, 1): 3 + 2 + 2 = 7 conditions on 4. No rank-one coupling, except in the limit at
     the cusp (W53).
   - **k = 5** (1, 2, 1): 2 + 1 + 2 = 5 on 4. None at a generic τ; τ (one complex number) supplies the fifth, so
     rank one occurs only at isolated τ.
   - **k = 7** (1, 2, 2): 2 + 1 + 1 = 4 on 4. Finitely many at every τ.
   - **Sym² T at 5 or 7** (a symmetric rank one is a aᵀ, two free numbers): 2 + 1 = 3 on 2. So again rank one only at
     isolated τ.
3. **What it implies for the hierarchies.**
   - A sector at weight 7 reaches any hierarchy at any τ: near a rank-one point of its span, its other coefficients
     set the light 2 × 2 block freely.
   - At weight 5, and in Sym² T, only near isolated τ.
   - At weight 3, only near the cusp, where W53 found the sectors pinned together.
4. **The CKM at weight 7.**
   - If u and d use the same rank-one point a bᵀ, their heaviest left vectors agree at leading order (V_tb ≈ 1).
   - V_us comes from the two light blocks, which are free. V_cb and V_ub come from the heavy vectors' first-order
     shifts, of the light masses' size.
   - Rank 13 says these are not tied, so (7, 7, k_e) should fit.
   - A lepton sector at 3 or 5 restricts τ (W53's curves, or isolated points), but a quark pair at (7, 7) fits at any
     τ.

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **H0** | The controls. (a) The T ⊗ T dimensions at k = 3, 5, 7 are 2, 4, 5, and Sym² T's at 5 and 7 are 3. (b) The ten shape observables of a (5, 7, 5) structure in T ⊗ T at random α are unchanged under τ → τ + 1 and τ → −1/τ at five random points, to 10⁻⁸. (c) The 13 × P Jacobian of (7, 5, 5) in T ⊗ T at a random point has rank 13. | 95% |
| **H1** | The rank-one test, at all three random τ: μ₇ < 10⁻⁶, while μ₅ > 10⁻³ and μ₃ > 10⁻³. | 65% |
| **H2** | The question: at least one of the 32 structures fits (χ²_min ≤ 5.99 at a = 0.10). | 85% |
| **H3** | Every T ⊗ T structure with u and d at weight 7 fits: (7, 7, 3), (7, 7, 5) and (7, 7, 7). | 70% |

**Extra read-outs (no prior).**
- Every structure's χ²_min and the τ of its minimum. For each that fits: P and the pulls.
- Each quark pair's and lepton weight's best grid value (where each part can be fit alone).
- Whether each minimum sits on the box's edge (y = 6, the cusp).

## The reading, written before the run

- **If H2 holds,** the structures that fit are listed.
  - They fit with P ≥ 13 real parameters and rank 13, so they predict nothing. The count of 13 is realised.
  - The tally is all 19 of the 19 free on the ruled branch, given Λ, or 18 if I-18 is earned.
  - The weave's modular structure can carry the Yukawas, but explains none of the 13 numbers. It does so only away
    from the geometry's weight (k = 3, W45's reading).
  - Which weight a sector takes is not forced (W52). Nothing fixes the Higgs's.
- **If H2 fails,** no structure on record fits. The weave's modular structure is then excluded as the Yukawas' source
  on the ruled branch, given Λ. Its scope: couplings holomorphic in τ alone, one flavour-blind Higgs per sector,
  weights up to 7, the record's two frames.
- **H1 carries the reason,** if it holds: only weight 7 holds rank-one couplings at a generic τ.
- **Weights 9 and above are not tested.** There d ≥ 6, so rank one is reached at every τ, and the count stays 13.

## Discipline

- One run. A failed launch (a crash before the read-out) is disclosed and fixed, and does not count as a run.
- Each cell is recorded as computed, and a failed prediction is recorded as failed.
- Post-hoc checks are labelled.
