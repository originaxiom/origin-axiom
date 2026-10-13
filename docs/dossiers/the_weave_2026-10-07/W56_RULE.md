# W56 — the rule, recorded before the read-out

The SM-derivation seat, 2026-10-13. Committed before the code that reads it exists. The predictions below were derived
by hand before this was written. Nothing here is a result.

## Why this arc

- **The owner's request (2026-10-13).** Look for a field compatible with the seed, by the same minimality as the seed
  ("Reading: the seed and the field"). The owner shared notes of 2025 for this. They were read at the owner's request
  and are not banked. Then: "contemplate once more and do as you recommend".
- **The standard a candidate field must meet** (proposed to the owner on 2026-10-13):
  1. nothing added: the principle generates it, with no new free constant;
  2. shared by every thread, as the two records are;
  3. the seed's own moves act on it;
  4. its interaction with the seed is not flat: it picks τ and the Higgs state (GENESIS FK9);
  5. it yields at least one testable number.
- **What the contemplation found by hand.** These facts are stated here so that the run can check them.
  - **Most of the 19 numbers belong to one field.** 15 of them are couplings of the Higgs: the 13 flavour numbers and
    the 2 of its potential. So the field the record has not built is first of all the Higgs, with τ as its partner
    state.
  - **The Higgs has been flavour-blind so far.** Every arc from W52 to W55 kept it a singlet of the moves. W55 placed
    the missing datum in the Higgs's place relative to T.
  - **The parity of the triplet's multiplier.**
    - In the record's construction ρ_T(S)² = i·1. This was read off W50's matrices before this rule was written; it is
      a convention fact, not a result.
    - A coupling form of weight k in a representation R needs R(S)² = e^{−iπk}.
    - Each generation contributes conj ρ_T: the coupling forms of W50–W54 lie in conj ρ_T ⊗ conj ρ_T, at odd k.
    - **A Higgs that transforms exactly like a generation** (conj ρ_T, at 3/2) gives a triple coupling in
      R_G = (conj ρ_T)^⊗3. That needs (−i)³ = i = e^{−iπk}, so k ≡ 3/2 (mod 2). At the generations' total weight 9/2
      no form exists. **The Higgs cannot be a fourth copy of a generation.**
    - **A Higgs in the dual triplet** (contributing ρ_T) gives R_D = conj ρ_T ⊗ conj ρ_T ⊗ ρ_T. That needs
      (−i)²·i = −i = e^{−iπk}, so k ≡ 1/2 (mod 2), and 9/2 is allowed. **At the geometry's weight, the dual triplet is
      the only placement of generation type.**
  - **The d–e wall: the down quarks and the charged leptons are alike in everything the record supplies.**
    - **The seed and the Standard Model frame.** Under Λ (GENESIS FK11), Q, d^c, L and e^c are all in T at 3/2. In the
      Standard Model frame d and e also share H_d. So their couplings lie in one space, and only free coefficients can
      tell them apart.
    - **F-MC's E₆ cubic (THE_CLAIM §1).** Write the 27 in trinification form, (Q_L, Q_R, L).
      - The down quarks get their masses from tr(Q_L L Q_Rᵀ), through the 2 × 2 neutral block N of ⟨L⟩.
      - The charged leptons get theirs from det L, through N's adjugate.
      - For a 2 × 2 matrix, adj N = J Nᵀ J⁻¹, with one fixed J.
      - The cubic is symmetric, so the flavour tensor is too. Then the 6 × 6 lepton matrix is
        −(1 ⊗ J) M_dᵀ (1 ⊗ J)⁻¹, up to the cubic's normalisation, and its singular values are those of M_d.
      - This holds for any number of Higgs 27s, any flavour structure and any neutral vacuum values. **So in F-MC's
        frame no Higgs content in 27s can tell the down quarks from the charged leptons.**
      - **A correction to W55.** W55's scope remark said further Higgs 27s or flavour directions in T "can split the
        sectors". In the E₆ frame they cannot. Only a Higgs outside the 27 can: W39's 351′, which holds SU(5)'s 45.
    - **The shared fibre's holonomies.** The moves fix a flat U(1) holonomy (y_a, y_b) on the shared fibre only when it
      is trivial: L forces y_a = 1 and R forces y_b = 1 (W31's F4 for hypercharge). So no Wilson line on the fibre can
      split quarks from leptons either.
    - **The data's d–e pattern is the Georgi–Jarlskog one** (W55):
      - m_μ/m_τ is 3.1 times m_s/m_b;
      - m_d/m_b is 3.4 times m_e/m_τ.
- **The question.** Test W55's located datum at the geometry's weight: take every Higgs placement the seed itself
  supplies there, and ask whether any fits and whether any predicts.
  - **(B), flavour-blind at weight 0:** the coupling in T ⊗ T at k = 3 (W53).
  - **(G), like a generation (T at 3/2):** no coupling exists, by the parity above.
  - **(D), in the dual triplet at 3/2:** the coupling in R_D at k = 9/2.
  - In the Standard Model frame H_u and H_d are placed separately. (B, B) is W53's, and it failed. This arc runs
    (D, D), (B, D) and (D, B).
  - This is the bound the seat recommended to the owner. The Higgs's direction is left free, to see whether any
    direction fits at all before asking what selects one.

## Weave or thread?

- **Weave-type.**
  - The forms are the weave's: equivariant under its whole group and built from ρ_T (W50).
  - τ is a state of the weave (W51).
  - The placements are every one the seed supplies at the geometry's weight, under the stated rule, with none
    hand-picked.
  - The claims are about all of them at once, at every τ.
- **The tags.** On the ruled branch; given Λ (GENESIS FK11); couplings holomorphic in τ. The frames are the record's:
  the Standard Model frame of W52–W55, and F-MC's E₆ cubic (THE_CLAIM §1).

## The data

W53's, unchanged:
- the masses from `received/HZ2021_running_masses_MZ.json`;
- the CKM's |V_us|, |V_cb|, |V_ub| and |V_td| from `received/B1612_data.json`.

## The computation

- **K1, the E₆ identity.**
  - **The cubic.** In trinification form, I₃ = det Q_L + det Q_R + det L − tr(Q_L L Q_Rᵀ), with d its polarisation.
  - **The couplings.** W = Σ Y^{(m)}_{ijk} d(Φ_i, Φ_j, H^{(m)}_k), for m = 1, 2 or 3 Higgs 27s. The flavour tensors are
    random complex. The vacuum values are random, in the five neutral components of each L.
  - **The charges.** Q_L's columns carry (2/3, −1/3, −1/3), Q_R's carry (−2/3, 1/3, 1/3), and L's entries carry
    −(q_L(α) + q_R(β)).
  - **M_d** is the Hessian block, for one colour, between Q_L's charge −1/3 triplets (α = 2, 3) and Q_R's charge +1/3
    triplets (β = 2, 3): 6 × 6 with flavour.
  - **M_e** is the block between L's charge −1 entries (L^1_2, L^1_3) and its charge +1 entries (L^2_1, L^3_1): 6 × 6.
  - **The test.** 200 random cases. Predicted: in every case the sorted singular values of M_e are one multiple c of
    M_d's, to 10⁻¹⁰, with the same c in every case.
  - **The control, which must fail.** Repeat with one neutral component's contribution to the lepton block multiplied
    by −3. That is a deformation like Georgi and Jarlskog's, and it is not E₆-invariant. The ratios must then differ
    by more than 10⁻³ in every case.
- **K2, the parity and the dimensions.** Use W50's form solver: the S condition on the arc, with T built into the
  exponents.
  - Compute dim M_k for R_G and R_D at k = 1/2, 3/2, …, 15/2.
  - The control: T ⊗ T at k = 3, 5, 7 gives 2, 4, 5 (W52) with the same routine.
  - n is the dimension of R_D at 9/2.
- **K3, the census.** For (D, D), (B, D) and (D, B):
  - **A sector with a B Higgs:** Y_s = Σ_a α_{s,a} F̂_a(τ), with W53's forms at k = 3 (two of them).
  - **A sector with a D Higgs:** (Y_s)_{ij} = Σ_a α_{s,a} Σ_k F̂_{a,ijk}(τ) h_k.
    - F̂_a runs over R_D's basis at 9/2, each form normalised at τ.
    - h = h_u or h_d ∈ ℂ³ is free, and d and e share h_d.
    - The first index is the left-handed field, the second the right-handed, the third the Higgs's.
  - **The observables, the tolerance (a = 0.10), the threshold (5.99) and the domain** (the fundamental domain with
    y ≤ 6) are W53's.
  - **When a trial τ is mapped into the domain by γ,** h is replaced by conj(ρ_T(γ)) h. That keeps the observables
    continuous, by the forms' equivariance.
  - **The search, fixed here.**
    1. **The grid** is W54's τ grid: x in 11 steps over [−½, ½] and y in 16 geometric steps over [0.87, 6], kept where
       |τ| ≥ 1.
    2. **At each grid τ** the other parameters are fitted by trust-region least squares from 4 random starts. The
       seeds are drawn from (5600, the structure's index, the grid index).
    3. **A joint bounded refinement** over τ and every parameter follows, from each structure's 8 best grid points.
    4. **χ²_min** is the lowest value found.
  - **P, the effective count:** 2 + 4 for each D Higgs + Σ_s (2 d_s − 1), where d_s is 2 for B and n for D.
- **K4, the count.** For each structure, the rank of the 13 × P Jacobian at three random points. The observables are
  the nine log masses, each sector's scale carried in its coefficients, and the four log \|V\|.

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **K1** | The E₆ identity holds on all 200 cases: σ(M_e) = c σ(M_d), with one c, to 10⁻¹⁰. The deformed control breaks it on all 200. | 90% |
| **K2** | R_G has no forms at k ≡ 1/2 (mod 2), so none at 9/2. R_D has none at k ≡ 3/2 (mod 2). R_D at 9/2 has n ≥ 2. The control gives 2, 4, 5. | 90% |
| **K3a** | (D, D) fits. | 80% |
| **K3b** | (B, D) fits. | 70% |
| **K3c** | (D, B) does not fit. | 80% |
| **K4** | Every structure run has rank 13, so none predicts a flavour number. | 90% |

**The hand reasons.**
- **K2.** The free-module estimate is dim ≈ dk/12 − Tr Λ + d/2, where Λ holds the exponents in [0, 1).
  - For T ⊗ T it gives 3, 4.5 and 6 at k = 3, 5 and 7, against W52's 2, 4 and 5: an overshoot of up to one.
  - R_D: Tr Λ = 109/8, giving about 10 at 9/2, so n ≈ 9.
  - R_G: Tr Λ = 111/8, giving about 3 at 3/2.
- **K3a.** P ≈ 2 + 8 + 3(2n − 1) ≈ 60 for 13 numbers. W53's universality pinned the light-to-heavy ratio of every
  k = 3 sector. Here n forms with different leading exponents, and a free direction, remove the pin.
- **K3b.**
  - W53's F1 found the up quarks' two ratios reachable at k = 3 to a residual of 0.036, at τ ≈ −½ + 4.21i.
  - At 9/2, d and e are free enough to follow that τ.
- **K3c.**
  - Here d and e are both at k = 3 and share one τ.
  - In the hierarchical regime both light-to-heavy ratios are pinned to κ q^{1/4} (W53's F4), while the data need them
    3.4 times apart.
  - W53's F1 also put their exact solutions at different τ: d at y ≈ 3.19 or 5.11, e at y ≈ 2.47 or 5.91.
- **K4.** In every structure P is far above 13, and W54 found rank 13 at every P ≥ 23.

**Extra read-outs (no prior).**
- Every dimension of K2.
- For each structure: χ²_min, the τ of its minimum, P, its pulls, and whether the minimum sits on the box's edge.

## The reading, written before the run

- **If K1 holds.** F-MC's cubic, with any Higgs content in 27s, gives the down quarks and the charged leptons one
  spectrum, and the data exclude that (W55's K1: χ² ≥ 106). W55's scope remark is corrected: in F-MC's frame only
  Higgs content beyond the 27 can split them.
- **If K2 holds.** The Higgs cannot transform like a generation at the generations' weight, because no coupling exists
  there. At the geometry's weight the only placement of generation type is the dual triplet.
- **If K3 and K4 go as predicted:**
  - **The Higgs's place was what W53's structure lacked.** The geometry's weight, rejected with a flavour-blind Higgs
    (W53), fits once H_d carries the dual-triplet index.
  - **But it predicts nothing.** It fits with P around 40 to 60 for 13 numbers. The count stays 19 of the 19 free,
    given Λ.
  - **The coefficients carry the freedom, not the direction:** n complex numbers per sector, against 4 reals per
    direction. So a field that only selects the Higgs's direction cannot make this predictive. A principle that fixes
    the couplings themselves is needed.
- **The d–e wall, whatever the run gives.**
  - Nothing the record supplies tells the down quarks from the charged leptons, except free coefficients (the Standard
    Model frame) or a Higgs beyond the 27 (F-MC's frame).
  - The data's d–e pattern is Georgi and Jarlskog's.
  - So a field compatible with the seed must carry the quark–lepton distinction, which the seed and its frames keep
    symmetric.
- **If K3a fails.** Even the dual-triplet Higgs cannot rescue the geometry's weight. The geometry's weight is then
  excluded for every placement the seed supplies there.

## Discipline

- One run. A failed launch (a crash before the read-out) is disclosed and fixed, and does not count as a run.
- Each cell is recorded as computed, and a failed prediction is recorded as failed.
- Post-hoc checks are labelled.
