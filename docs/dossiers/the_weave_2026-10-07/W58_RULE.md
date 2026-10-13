# W58 — the rule, recorded before the code

The SM-derivation seat, 2026-10-13. Committed before the code that reads it exists. What the seat saw before writing it
is listed under "Seen before the rule", and the priors of the cells it touches are set after that look. Nothing here is
a result.

## Why this arc

- **The owner approved the seat's plan (2026-10-13).** Its step A3: check a level-four modular-symmetry preprint with
  the record's own code, and grade it.
- **The preprint.** Barger, "Level-Four Modular Symmetry Selected by the Harmonic Pattern of Quark and Lepton Masses",
  arXiv:2609.09262v1 (8 Sep 2026). The PDF's sha256, its Table I and the printed claims are in
  `received/B2026_level_four_claims.json`.
- **What it claims.**
  - The quark and lepton masses at M_Z show a two-to-one pattern of logarithmic steps, mirrored between the up–down and
    down–lepton comparisons. Read as charges on a ℤ_N clock, it selects level four: Γ₄ ≅ S₄, the generations in a
    triplet at T-charges (3, 1, 0), the mirror the sign singlet.
  - The lepton masses fix ε = 14/75 and τ = (2i/π) ln(1/ε) = 1.0685 i.
  - Eight postulates (theta-constant insertions with unit coefficients, one adopted empirical relation) then give the six
    quark masses, the CKM matrix and the neutrino sector "with no continuous parameter".
- **Why it matters to the record.** The record's triplet T is an S₄ triplet twisted by a character (W21, W38, W50), and
  its components are the even theta constants of the records' torus, T = η²¹·(θ₄², θ₂², θ₃²) (W50). An independent
  route from the data lands on the same kind of object. So the record must check two things: whether it is the same
  representation, and whether the claimed numbers stand.
- **The owner's rule (B1517): repo first, then literature, and verify load-bearing math even when published.**

## Weave or thread?

- **K1 and K2 concern T, the weave's triplet** (a WEAVE object, W21). They compare it with the preprint's triplet.
- **K3 to K7 check an outside claim.** They are neither a weave nor a thread result. Nothing in them is the record's
  derivation.
- **The tags.** On the ruled branch; given Λ (GENESIS FK11) for any reading of T as the generations.

## Seen before the rule (disclosed)

- **ρ_T's matrices** (W56's module, the code convention F(−1/τ) = τ^k ρ(S) F(τ)), in the basis of the parity lines.
  - T is monomial: it fixes the second line and exchanges the first and third.
  - S fixes the third line and exchanges the first two.
  - Untwisted by e^{−2πi/8} on T and e^{3πi/4} on S, they satisfy S² = (ST)³ = T⁴ = 1, with traces −1, 1, 0 at S, T and
    ST. That is one case of K1, checked interactively.
- **The selection theorem at N = 4,** worked by hand: the shifts c = 2 and c = 3 both solve it (K3).
- **The double ratio:** 2/ε = 10.714 by hand (K5).
- **The record's own data.**
  - At M_Z: m_b, m_c, m_s, m_d and m_u from the preprint's relations, by hand on Huang and Zhou's values, each within
    1σ (K7a).
  - At 10¹² GeV (`received/HZ2021_running_masses_1e12.json`): m_b/m_τ = 0.689 and the double ratio 10.55 (K7b).
- **W51's critical points** (i, ω, 1.551i, ½ + 2.224i, 2.226i), quoted in the reading.

## The constants

- **ε and τ.** ε = 14/75 and τ_B = (2i/π) ln(75/14). The theta constants are θ₂ = Σ e^{iπτ(n+½)²},
  θ₃ = Σ e^{iπτn²} and θ₄ = Σ (−1)ⁿ e^{iπτn²}.
- **Two routes:** W51's `thetas` (the record's series) and mpmath's `jtheta` at 30 digits. They must agree to 10⁻¹².
- **Masses** are the preprint's Table I, with v = 248.40 GeV, except in K7.

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **K1** | Of the 24 characters χ_η^k of the metaplectic group (χ_η the multiplier of η, computed from η itself in the code convention), exactly two untwist ρ_T to a representation of Γ₄ ≅ S₄ (S′² = (S′T′)³ = T′⁴ = 1): k = 3 and k = 15. They give the triplets with T-charges {0, 1, 3} (traces −1, 1, 0 at S, T, ST: the cube's rotations, the preprint's 3) and {1, 2, 3} (the preprint's 3′). | 97% (one case seen) |
| **K2** | The preprint's generation lines are the T′-eigenlines (charges 0, 1, 3 for its generations 3, 2, 1). In the record's basis exactly one of them is a parity line: the one carrying θ₂², the preprint's third generation. Its first and second generations are (e₁ ± ζe₃)/√2, for one phase ζ: mixtures of the parity lines carrying θ₄² and θ₃². So no permutation of the three alike parity lines gives the preprint's basis. | 97% (the matrices seen) |
| **K3** | Under the stated hypotheses, scanning 3 ≤ N ≤ 12, solutions exist only at N = 4. The hypotheses: one charge vector a in [0, N)³ with integer steps (2, 1), and b = (a + c) mod N with steps (−2, +1). At N = 4 the solutions are a = (0, 2, 3) with c ∈ {2, 3}. Only c = 2 shifts the T-charges by a character of S₄ (1′, charge 2). | 95% (worked by hand) |
| **K4** | At τ_B the seat's code gives θ₂, θ₃, θ₄ = 0.86515, 1.06969, 0.93031 and Im τ = 1.0685. Every printed claim in the data file with a printed value reproduces from its stated formula to the printed digits (at most one unit in the last printed digit). The claims: Eqs. 21, 22, 25, 26, 28 to 34, 40, 43, 44, 46 and 49; P4; Table VII's six masses; Tables VIII and IX; Sec. III C and III D. | 80% |
| **K5** | The preprint's P5 gives the double ratio (y_μ y_d)/(y_s y_e) = 2/ε = 10.714 exactly. It lies within 2σ of the target recorded after W57, 10.58 ± 0.11 (`received/AHS2026_double_ratio.json`). Its Georgi–Jarlskog plaquette (2/(ε Im τ))^{1/2} = 3.167 lies within 2σ of the record's own value at M_Z (Huang and Zhou). | 95% (the first part by hand) |
| **K6** | The look-elsewhere. (a) Recomputed on the paper's own definitions, Table XIV's coverages for the anchor, P1, P2 and P4 reproduce on both dictionaries: within a factor 1.5 where printed below 50%, within 0.1 where printed above. (b) The anchor's dressing (2θ₃)⁴ = 2^{8/2} θ₃⁴ lies outside the paper's form-value box. On the smallest box of the same shape that holds it (\|k\| ≤ 8, 0 ≤ b ≤ 4, c ∈ {0, 1}, w ∈ {−1, 0, 1}), its coverage at 0.02% is at least 10%. (c) The product of the four coverages, taking the form-value family for P1, P2, P4 and (b)'s box for the anchor, is at least 1%. The text's 10⁻⁶ uses the declared family. | 70% |
| **K7** | The record's own data (Huang and Zhou 2021, PDG 2020 inputs, independent of the preprint's Ref. [4]), with ε and τ re-derived from those lepton masses by the preprint's Eqs. 23–24. (a) At M_Z, full SM: the anchor m_τ/m_μ = ε^{−7/2}/(2θ₃)⁴ holds within 2σ. The six quark relations each hold within 2σ, with y_t = √2 m_t/v_F, v_F = 246 GeV, in place of m_t. (b) At 10¹² GeV: P1 (m_b/m_τ = (2ε)^{−1/2}) fails by more than 5σ, while the double ratio 2/ε holds within 2σ. | 90% (part seen) |

**The definitions behind K4 and K6.**
- **The CKM** is in the standard parametrization: s₁₂ = |V_us|, s₂₃ = |V_cb|, s₁₃ = |V_ub| and δ from Eq. 33.
  - J = c₁₂c₂₃c₁₃² s₁₂s₂₃s₁₃ sin δ.
  - R_b and R_t come from the matrix, and the angles from Eq. 37.
- **The coverage of a target t with relative uncertainty σ.**
  - x is log-uniform on [t e⁻³, t e³].
  - It lands if |ln x − ln f| ≤ σ for some element f, on half-integer rungs ε^{n/2} over every n that reaches the range.
  - The coverage is the measure of the union of those windows, computed exactly, not sampled.
- **A hit** is an element f with |ln t − ln f| ≤ σ.

**The reading, written before the run (predicted).**
- **The structure is shared.**
  - An independent route from the data lands on the record's T: the same level-four triplet, up to η³'s multiplier.
  - Its couplings are theta constants of the same torus.
- **The basis is not.**
  - The preprint's generations are the eigenlines of T, the basis that the cusp's residual ℤ₄ singles out.
  - The record's three are the parity lines, alike under the moves.
  - In the record's terms, the preprint's generations are the three after a state of the field has broken the weave's
    group toward the cusp. That is W50's "the modulus is the state that breaks the weave's group", taken at one
    particular τ.
- **The numbers stand as arithmetic,** and the relations hold at M_Z on the record's own data too.
- **The significance does not.**
  - The coefficients are selections from a family that covers every number at percent precision.
  - The anchor is one landing in a family of several hundred prefactors.
  - The relations that are not double ratios hold at one chosen scale.
- **What the record takes from it.** No derivation. What it offers:
  - a candidate state τ = 1.0685 i, near i, which is no critical point of any functional on record (W51);
  - two numbers for C1 to aim at: the double ratio 2/ε and the plaquette (2/(ε Im τ))^{1/2}.
- **The count stays all 19 of the 19 free** (18 if I-18 is earned). 0 of 19.

## Discipline

- **The rule and the data file are committed before the script.**
- **One run.** A failed launch (a crash before the read-out) is disclosed and fixed, and does not count as a run.
- **Each cell is recorded as computed.** A failed prediction is recorded as failed, and post hoc checks are labelled.
- **The preprint's PDF is not added to the repository.** Its sha256 and the transcribed numbers are.
