# W55 — the rule, recorded before the read-out

The SM-derivation seat, 2026-10-13. Committed before the code that reads it exists. The predictions below were derived
by hand before this was written. Nothing here is a result.

## Why this arc

- **The owner's choice (2026-10-13), after "Reading W49–W54 together":** (a), does the gauge side on record tell the
  sectors apart?
- **The reading's point 3.** All fields in T and one τ give the up quarks, down quarks and charged leptons one
  hierarchy (W53). The data give them three. The fits that work give the sectors different weights (W54), which the
  weave does not supply.
- **The question.** Does the gauge side on record supply what tells the sectors apart, in a way that fixes numbers?
  - The frames: F-MC's E₆ cubic (THE_CLAIM §1: matter mass in the cubic 27³ ⊃ 16·16·10, the doublet in the 10 ⊂ 27),
    SO(10)'s 16·16·10 and minimal SU(5) (both inside it), and the Standard Model frame of W52 to W54.
  - If the answer is yes, the weights or the coefficients stop being free.

## Weave or thread?

- Each claim is about every structure a frame allows, at every weight and every τ. Weave-type for the weave's part;
  the gauge frames are the record's, cited.
- The tags: on the ruled branch; given Λ (GENESIS FK11), so every left-handed field of a generation is in T at the
  geometry's weight 3/2 (W45); couplings holomorphic in τ.

## The facts by hand

1. **Where the Higgs sits decides what the gauge side can tell apart.**
   - **The E₆ cubic with every vacuum value in flavour-blind 27s** (the Higgs doublets, and F-MC's rank-closing ⟨1⟩
     and ⟨ν^c⟩):
     - one flavour matrix λ (in T ⊗ T, symmetric) serves every coupling, each with its own E₆ Clebsch–Gordan number
       and vacuum value;
     - the down-type mass matrix on (d, D) × (d^c, D^c) is then P ⊗ λ, with P = [[v_d, 0], [n, s]] (v_d, n and s
       carrying the Clebsch numbers);
     - the singular values of P ⊗ λ are the products σ_a(P)·σ_i(λ): two branches, σ_min(P) and σ_max(P) times λ's
       singular values. The down quarks are the lighter branch, so their masses are σ_min(P) times λ's, exactly;
     - the same holds for the charged leptons, on (e, e′) × (e^c, e′^c) with P′ = [[v_d, n], [0, s]]: the doublet L
       mixes with the 10's L′^c through ⟨ν^c⟩, and L′ L′^c takes ⟨1⟩.
     - So the light down quarks and charged leptons have **equal in-sector ratios**, those of λ, whatever the vacuum
       values. The up quarks share them too, with V a phase matrix, unless H_u and H_d sit in different 27s.
   - **SO(10) with one 10_H** gives Y_u = Y_d = Y_e up to scale. **Minimal SU(5)** (one 5̄_H) gives Y_e = Y_dᵀ, with
     the same singular values.
   - **A Higgs in T** (the generations' own 27s, or vacuum values with flavour directions) can split the down quarks
     from the leptons. But the directions are new free numbers, four reals per vacuum value: nothing on record fixes
     them.
   - **The Standard Model frame** (separate doublets, not in T): with every matter field at 3/2, a sector's weight is
     3 plus its Higgs's. The down quarks and leptons share H_d, so k_d = k_e. That is the only tie, and the Higgs
     weights stay free.
2. **The tie is measurable.** Equal in-sector ratios for the down quarks and the leptons must meet both data sets.
   - m_d/m_b = 9.4 × 10⁻⁴ against m_e/m_τ = 2.8 × 10⁻⁴ (×3.4), and m_s/m_b = 0.019 against m_μ/m_τ = 0.059 (×3.1).
   - With W53's tolerance (a = 0.10) the two log ratios cost about (ln 3.4)²/0.045 ≈ 33 and (ln 3.1)²/0.048 ≈ 28. So
     χ² ≳ 60, in the six masses alone, for every structure with the tie, at any weight and any τ.
   - This is the classic down–lepton mismatch of unified theories, met here inside the record's own frame.
3. **What the Standard Model frame's tie leaves.** Of W54's fits, those with k_d = k_e are (5, 5, 5), (5, 7, 7) and,
   by W54's post hoc, (7, 7, 7). They have P = 23, 27 and 29, so the tie reduces no free number.

## The computation

- **K1, the tie's bound.** The minimum, over two shared log ratios (ρ₁, ρ₂) and the two sectors' scales, of the χ² of
  the six down and lepton log masses with in-sector ratios (ρ₁, ρ₂, 0). This is a linear least-squares problem,
  solved exactly at a = 0.05, 0.10 and 0.20. Also the allowance a* at which the bound falls to 5.99.
- **K2, the Kronecker lemma.** For 200 random complex symmetric λ and random complex (v_d, n, s): the six singular
  values of P ⊗ λ equal the six products σ_a(P)·σ_i(λ), to 10⁻¹⁰ relative; the same for the leptons' P′ = Pᵀ.
- **K3, the Standard Model frame's tie**, read from W54's recorded JSON and its post hoc: the fitting structures with
  k_d = k_e, and their P.

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **K1** | The tie's bound at a = 0.10 is at least 50. The tie is excluded in every frame that imposes it, at every weight and τ. | 90% |
| **K2** | The Kronecker lemma holds on all 200 samples. | 97% |
| **K3** | In the Standard Model frame the fitting structures with k_d = k_e are exactly (5, 5, 5), (5, 7, 7) and (7, 7, 7), with P ≥ 23 each. | 95% |
| **K4** | The allowance a* at which the tie's bound reaches 5.99 is above 0.25: only a running allowance of more than 25% would admit it. | 80% |

## The reading, written before the run

- **If K1 to K3 hold, the answer to (a) is no.**
  - The gauge side on record either ties the sectors together, and the data exclude the tie: the down quarks with the
    leptons in F-MC's cubic, SO(10) and minimal SU(5), all three sectors with one flavour-blind 27.
  - Or it tells them apart only through Higgs content that carries new free numbers: flavour directions in T, or the
    separate doublets' weights in the Standard Model frame.
  - So nothing on record tells the sectors apart in a way that fixes a number. The count stays W54's: all 19 of the 19
    free on the ruled branch, given Λ (18 if I-18 is earned).
- **What it locates.** The missing ingredient is the Higgs sector's flavour structure (where the Higgs sits relative
  to T, and with what weight). That is a dictionary datum (GENESIS FK11), not something the weave or F-MC supplies.
- **If K1 fails** (the bound below 50), the tie is less costly than the hand estimate says. The bound is reported,
  and the frames that impose the tie are graded by it.

## Discipline

- One run. A failed launch (a crash before the read-out) is disclosed and fixed, and does not count as a run.
- Each cell is recorded as computed, and a failed prediction is recorded as failed.
- Post-hoc checks are labelled.
