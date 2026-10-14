# W77 — the rule, recorded before the code

The SM-derivation seat, 2026-10-14. Committed before the code that reads it exists. What the seat worked by hand while
drafting is listed under "Seen before the rule", and the priors were set after that. Nothing here is a result.

## Why this arc

- **The audit lane asked for it.** Its relay `PHYSICAL_TO_GENESIS_MAIN_SM_2026-10-14_ODD_DOMAIN_FORM.md` (on
  `audit/physical-bridge-2026-09-05` @ 3d7933bec) is addressed to main and to this seat. It reports a conditional odd
  complementary form estimate and says: "An independent analytic review is required before treating this as more
  than authored research grade. Sender relay OPEN pending actual receiving read/reproduction."
  - The seat's ledger row for that push said "No relay file to this seat". That was wrong, and is corrected with a
    dated note in this arc's record.
- **The estimate is on the path to the four-dimensional index,** the duty W71 left to the lane. In the lane's own
  words it is a conditional path to Fredholmness at 0, not an index or a count.
- **The owner's rule is to verify load-bearing mathematics with the seat's own code.**

## Weave or thread?

- **Neither: a review of another seat's analytic estimate.** The operator is the lane's, on its supplied semi-flat
  cusp metric, with zero scalar background, either extreme puncture law and the flat retained E₈ coefficient. Those
  hypotheses are the lane's, and the review inherits them. No claim here is a weave result.

## Seen before the rule (disclosed)

- **Read before this rule:** the relay, `PROOF.md`, `DESIGN.md`, `INPUTS.json` and `reference.py` of
  `surface_odd_form_2026_10_14`, and the frame code `upstream_total_metric.py` of `surface_parent_dictionary_2026_10_13`
  (its metric, coframe, gamma matrices and expected brackets).
- **The lane's setting, as read.**
  - The metric is g = ℓ²(dx² + dy²)/y² + (A/y)(du + x dv)² + A y dv².
  - The coframe is e¹ = (ℓ/y)dx, e² = (ℓ/y)dy, e³ = (A/y)^{½}(du + x dv) and e⁴ = (Ay)^{½}dv.
  - The stated brackets are [E₁, E₂] = −E₁/ℓ, [E₂, E₃] = E₃/(2ℓ), [E₁, E₄] = −E₃/ℓ and [E₂, E₄] = −E₄/(2ℓ).
  - V = c₃E₃ + c₄E₄ and H = c₁E₁ + c₂(E₂ − 1/(2ℓ)) + c₁c₃c₄/(4ℓ) + iβc₁/ℓ, with c_j² = −1.
- **Worked by hand.**
  - **The cross form.** {c_aE_a, c_bE_b} = c_a c_b [E_a, E_b] for a vertical and b horizontal. Constants times c₂ or
    c₁ anticommute with c_aE_a. {c₃, c₁c₃c₄} = 2c₁c₄ and {c₄, c₁c₃c₄} = −2c₁c₃ (c² = −1).
    - So the E₃ coefficient is −c₁c₄/ℓ + c₂c₃/(2ℓ) + c₁c₄/(2ℓ) = K₃, and the E₄ coefficient is
      −c₂c₄/(2ℓ) − c₁c₃/(2ℓ) = K₄, as stated.
  - **The cubic spin term.** The Koszul formula gives the totally antisymmetric part Γ_[134] = 1/(6ℓ) from
    C₁₄₃ = −1/ℓ, so the cubic term is ¼ · 6 · Γ_[134] c₁c₃c₄ = c₁c₃c₄/(4ℓ), as stated.
  - **The density.** In the physical norm ∫|ψ|² √g, with √g = ℓ²A/y², div E₂ = −1/ℓ and div E₁ = 0. So c₂(E₂ − 1/(2ℓ))
    is symmetric. c₁c₃c₄ and iβc₁ are Hermitian. In the lane's convention the spin connection's linear part is
    +½ Σ (div E_j) c_j = −c₂/(2ℓ): the density term is the trace part of the spin connection.
  - **The norms.** (2ℓK₃)² = −2 − 2c₁c₂c₃c₄, so K₃†K₃ has eigenvalues 1/ℓ² and 0, each twice. K₄ is the same.
  - **The chain.** |⟨ψ, Fψ⟩| ≤ 2(‖E₃ψ₋‖ + ‖E₄ψ₋‖)‖ψ₊‖/ℓ ≤ (2√2/ℓ)‖D_Vψ₋‖‖ψ‖. Then 2√2ab ≤ a²/2 + 4b², with
    equality at a = 2√2b, gives inequality (1).
  - **The domain argument, read.** Every cross pairing couples ψ₊ to ψ₋. On the core ψ₋ vanishes near the puncture
    section, and H keeps that, since horizontal fields are tangent to the section. So no boundary term arises there.
    The seat found no gap in this step as written.
- **Nothing has been computed by script.**

## The method (fixed here)

- **R1, the brackets, by a second route (exact, sympy).** Use the structure equations de^k = −½ C_ij^k e^i ∧ e^j from
  the coframe, rather than commutators of vector fields. Compare all 64 C_ij^k with the four stated brackets and
  their antisymmetric partners.
- **R2, the spin connection (exact).** Use the Koszul formula Γ_ijk = ½(C_ijk − C_jki + C_kij) from R1's constants,
  and the Dirac term Σ_i c_i ω_i with ω_i = ¼ Σ_jk Γ_ijk c_j c_k. Then:
  - read its cubic part (the c₁c₃c₄ coefficient) and its linear part (the c₂ coefficient);
  - check that the linear part equals +½ Σ_j (div E_j) c_j, with div computed from √g. This is the lane's sign
    convention (ω_i = +¼ Σ Γ_ijk c_j c_k), the one its Lichnerowicz check uses.
- **R3, the cross form (exact).** Use a different gamma representation from the lane's: the chiral one, with
  c₁ = iγ₄, c₂ = iγ₁, c₃ = iγ₂, c₄ = iγ₃, where γ₁,₂,₃ = [[0, −iσ_j], [iσ_j, 0]] and γ₄ = [[0, 1], [1, 0]].
  - Represent V and H as first-order operators: matrix coefficients times the E_i, plus a matrix constant.
  - Compute {V, H} by the bracket rule, reducing products E_aE_b − E_bE_a to R1's brackets.
  - Read the coefficients of every E_i and of the constant, and of any second-order term. β is a symbol.
- **R4, the coefficients (exact).** K₃ and K₄ in the same representation: skew-Hermitian; anticommuting with
  Γ_V = ic₃c₄; K†K with eigenvalues {1/ℓ², 1/ℓ², 0, 0}.
- **R5, the identity and the inequality on test sections (numerical; ℓ = 1, A = 1).**
  - Take sections ψ = Σ f_s(x, y) e^{2πi(m_s u + n_s v)} χ_s: two or three Fourier modes with (m, n) ∈ {−2..2}², random
    constant spinors χ_s, and f_s Gaussian bumps of width 0.12 centred in [−0.5, 0.5] × [1.5, 3]. They are smooth and
    supported away from the box edges; this is the puncture-free part of the core.
  - Integrate over x ∈ [−1, 1] and y ∈ [1, 4] with the density ℓ²A/y², on a 500 × 500 grid (Simpson), for 20 random
    sections (seed 75077) and β ∈ {0, ¾}.
  - Compute ‖Dψ‖², ‖Vψ‖², ‖Hψ‖², ⟨ψ, Fψ⟩ and ‖ψ‖².
  - **The identity:** ‖Dψ‖² − ‖Vψ‖² − ‖Hψ‖² − ⟨ψ, Fψ⟩ = 0, to 10⁻⁶ relative to ‖Dψ‖².
  - **The inequality (1):** ‖Dψ‖² − ‖Vψ‖²/2 − ‖Hψ‖² + 4‖ψ‖² ≥ 0 on every section.
  - **The cross bound:** |⟨ψ, Fψ⟩| ≤ 2√2 ‖ψ‖ ‖Vψ‖.

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **R1, the brackets** | The structure equations give exactly the four stated brackets and their partners, and no other nonzero C_ij^k. | 95% |
| **R2, the spin connection** | The cubic part of Σ c_i ω_i is c₁c₃c₄/(4ℓ). Its linear part is +½ Σ (div E_j) c_j, equal to −c₂/(2ℓ) here: H's density term is the spin connection's trace part. It makes c₂(E₂ − 1/(2ℓ)) symmetric in the physical norm. | 85% |
| **R3, the cross form** | In the chiral representation {V, H} = K₃E₃ + K₄E₄ exactly, with K₃ = (c₂c₃ − c₁c₄)/(2ℓ) and K₄ = −(c₂c₄ + c₁c₃)/(2ℓ). There is no second-order term, no E₁ or E₂ term and no constant, for every β. | 92% |
| **R4, the coefficients** | K₃ and K₄ are skew-Hermitian, anticommute with Γ_V, and K†K has eigenvalues {1/ℓ², 1/ℓ², 0, 0}. | 92% |
| **R5, the test sections** | The identity holds to 10⁻⁶ relative on all 40 (section, β) pairs. Inequality (1) and the cross bound hold on all 40. | 85% |

**The read-outs (no prior).**
- The smallest margin of (1) over the 40 pairs, relative to ‖ψ‖².
- The largest |⟨ψ, Fψ⟩|/(2√2‖ψ‖‖Vψ‖).

## What a result means, fenced

- **If R1 to R5 hold:** the lane's algebra (the brackets, the cubic spin term, the cross form, the coefficient norms)
  and its inequality chain are reproduced on this seat's instruments. The identity is also checked numerically on
  smooth sections in the physical norm.
- **What this review does not cover.**
  - The domain claims: the core's density in the extreme domains, the critical profiles, and the graph closure. They
    were read and no gap was found, but nothing here tests them.
  - The upstream inputs: the vertical gap constant c, the bound on [D, P] and the compactness.
  - The global pointed bundle.
  - The test sections avoid the puncture, so the half-pole component is not exercised numerically.
- **It is not an index, a kernel or a count,** as the lane says. **0 of 19.**

## Discipline

- **The rule is committed before the script, and there is one run.** A failed launch (a crash before the read-out) is
  disclosed and fixed, and does not count.
- **Each cell is recorded as computed.** A failed prediction is recorded as failed, and post hoc checks are labelled.
