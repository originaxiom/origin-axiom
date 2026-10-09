# B1628 — PREREGISTRATION: THE DATA AND THE WEAVE'S TWO TRIMAXIMAL RELATIONS — do the measured mixing angles prefer TM1 (the T̄ ⊗ T reading) over TM2 (the T ⊗ T reading)?

cc (main), 2026-10-09, after S106, on the owner's "go" to the outline's item 2a. **Sealed before any data named here is
read, and before `two_relations.py` runs.** 0 of 19.

**Why it matters.** In the frame where all of the weave's group is flavour (B1620, corrected at B1625 with the SM seat's
W43), the leptons' mixing reduces to two parameters as **TM1 under T̄ ⊗ T** (P10) and as **TM2 under T ⊗ T**, the
tensor the SM seat reads given Λ (W39). Under Sym² T it does not reduce at all. TM1 predicts sin²θ₁₂ = 1 − 2/(3 cos²θ₁₃)
≈ 0.318 and TM2 predicts sin²θ₁₂ = 1/(3 cos²θ₁₃) ≈ 0.341. The open tensor choice (GENESIS FK11, given Λ) therefore makes
a measurable difference, and this arc asks whether present primary data already see it.

## Seen first

`VERDICT topic-sweep /TM1|TM2|trimaximal|sin²θ₁₂|theta12|solar angle|NuFIT/: 15 of 1399 arcs on main match (NEGATIVE 7, PROVED 8)`:
- B1612 (the TM columns; data.json, NuFIT 6.0's 3σ |U| ranges), B1613 (P10), B1620 and B1625 (TM1 under T̄ ⊗ T, TM2
  under T ⊗ T), the SM seat's W43 and W44;
- B1066's log (NuFIT 6.1 from a secondary source).

**Literature:** the TM1/TM2 sum rules (Albright–Rodejohann 2008; Xing–Zhou); NuFIT 6.0 (Esteban, Gonzalez-Garcia,
Maltoni, Martinez-Soler, Pinheiro, Schwetz, arXiv:2410.05380).

## Disclosed

- **Not blind.** B1612's post-seal check (`post_seal_tm_sum_rules.json`) graded TM1 at 1.49σ and TM2 at 4.93σ against
  NuFIT 6.1 as recorded from a secondary source (arXiv:2604.04585, Table 1). Main also recalls NuFIT 6.0's sin²θ₁₂ best
  fit as near 0.307 with σ ≈ 0.012, which would put TM2 near 2.8σ. The seal fixes the data rule and the method, not
  ignorance of the outcome.
- **The data rule, fixed here.**
  - **(1)** NuFIT 6.0, arXiv:2410.05380, the global fit's table: best fit, ±1σ and 3σ range of sin²θ₁₂ and sin²θ₁₃,
    normal and inverted ordering, the variant with Super-Kamiokande atmospheric data, which is B1612's variant.
  - **(2)** The newest NuFIT release on nu-fit.org (6.1 or later), if its primary table is reachable on the day; if not,
    that is recorded and only (1) is graded.
  - **(3)** A primary collaboration measurement of sin²θ₁₂ newer than (2), if one is found by a search after this seal
    (for example a reactor experiment's first result), is reported beside them but not graded, since a single
    experiment's θ₁₂ and a global fit are different kinds.
  - The verdict is taken on the newest of (1) and (2) that is reachable; both are reported.
- 1D pulls with the asymmetric error on the prediction's side; θ₁₃'s uncertainty propagated by the prediction's spread
  over sin²θ₁₃'s 1σ interval, added in quadrature. Correlations between θ₁₂ and θ₁₃ in the global fit are neglected
  (they are small, and the θ₁₃ spread is about 4 × 10⁻⁴).

## Cells, predictions, priors

| | prediction | prior |
|---|---|---|
| **R1** | TM1 predicts sin²θ₁₂ ≈ 0.318 and TM2 ≈ 0.341 at the measured θ₁₃, each with a θ₁₃ spread below 10⁻³ | 97% |
| **R2** | on the graded table TM1 lies within 2σ of the best fit (normal ordering) | 85% |
| **R3** | on the graded table TM2 lies beyond 3σ (normal ordering) | 60% |
| **R4** | TM2 lies outside the graded table's 3σ range of sin²θ₁₂ | 55% |

**The reading, written before the run (the cells can only lower it).** If R2 and R3 hold, the present data prefer TM1
to TM2. In the frame where all of G is flavour, the two-parameter lepton reduction then survives only under T̄ ⊗ T, and
under T ⊗ T, the tensor read given Λ, the leptons need the full four mixing parameters. It also survives where c is gauge
(W44), where TM1 returns under T ⊗ T. **The data would then constrain the open choice of tensor and frame (FK11)**, not
exclude the weave. Since a failed relation removes a reduction rather than refuting the structure, the 13 and 0 of 19
are unchanged. If R3 fails, the data do not yet discriminate, and a sharper θ₁₂ measurement will. TM2 would be entered
in FALSIFIER_REGISTER either way as P10′, the T ⊗ T relation.

## Instruments

`verification/two_relations.py` (reads `verification/data.json`, transcribed after the seal); hashes in
`ARTIFACT_HASHES.txt`.
