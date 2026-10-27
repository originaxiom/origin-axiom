# B1756 — JUNO'S SECOND RELEASE AND THE WEAVE'S TWO TRIMAXIMAL RELATIONS: P10′ (TM2 under T ⊗ T, all of G flavour) IS FALSIFIED BY THE REGISTER'S OWN WORDING — 5.82σ FROM JUNO'S sin²θ₁₂ = 0.3036 ± 0.0064; P10 (a) (TM1) STANDS AT 2.28σ, BELOW ITS 3σ KILL LINE

**Verdict: PROVED (a grading by the falsifier register's fixed wording; B1628's sealed instrument unchanged).** cc (main),
2026-10-24 (P-388, P-273). **0 of 19** — a failed relation removes a reduction; it gives no parameter.

## 1. The data

JUNO's second release (arXiv:2609.37895 v1, 2026-09-29; 207.2 live days), read by main on arXiv's abstract page on
2026-10-24 after the web seat named it (its relay of 2026-10-24, harvest row 1399): sin²θ₁₂ = 0.3036 ± 0.0064,
Δm²₂₁ = (7.388 ± 0.078) × 10⁻⁵ eV², normal ordering favoured. θ₁₃ from NuFIT 6.0 (normal ordering), as B1628.

## 2. The grading (`verification/grade.py` → `two_relations.json`, `grade.json`, `grade_run.txt`)

B1628's `two_relations.py` (sealed 2026-10-09) is loaded unchanged, its sha256 asserted, and pointed at this arc's
`data.json`; it adds θ₁₃'s spread in quadrature, as sealed.

| data | TM1 (P10 (a)): 1 − 2/(3 cos²θ₁₃) = 0.3182 | TM2 (P10′): 1/(3 cos²θ₁₃) = 0.3409 |
|---|---|---|
| JUNO, second release (0.3036 ± 0.0064) | **2.28σ** — stands (the kill line is 3σ) | **5.82σ — falsified** |
| JUNO, first result (0.3092 ± 0.0087; B1628's transcription) | 1.04σ | 3.64σ |

**The register's wordings, fixed before this release:** P10 (a) dies on "a θ₁₂ measurement more than 3σ from
1 − 2/(3 cos²θ₁₃)"; P10′ on "a global fit or a single precision measurement placing 0.341 beyond 3σ". JUNO's second
release is a single precision measurement placing 0.341 at 5.82σ.

## 3. What it means

- **P10′ is falsified: the TM2 reading is dead.** In the frame where all of the weave's group is flavour and the mass tensor is
  T ⊗ T (B1620, B1625; the SM seat's W43), the weave's lepton reduction is TM2, and the data exclude it. As the register
  says, this kills that reading, not the weave: under that tensor and frame the leptons keep the full four mixing
  parameters. The open choice of tensor and frame (GENESIS FK11, given Λ) is now constrained by measurement: "T ⊗ T, all of
  G flavour" carries no surviving lepton relation.
- **P10 (a) stands, under pressure:** TM1 (T̄ ⊗ T; or T ⊗ T where c is gauge, W44) sits 2.28σ from JUNO's value; it was
  0.85σ on NuFIT 6.0 and 1.04σ on JUNO's first result. A JUNO value 0.0046 lower (0.2990), or the same central value with an
  error near 0.0049, would cross its 3σ line. P10 (b) (δ_CP) is untouched.
- **P10's scope notes stand:** it is a flavon-frame reading; on the ruled branch one τ cannot give its residual pair
  (B1640). So a survival of TM1 does not count for the ruled branch either.

## 4. Disclosed

- The data were read before this arc (by the web seat and by main); this is not a sealed test. What makes it a grading
  rather than a look is that both criteria were fixed in the register on 2026-10-08 and 2026-10-09, before either JUNO
  number, and are applied here as worded with B1628's sealed instrument.
- **By the register's own wording P10′ had already met its kill criterion on JUNO's first result** (3.64σ, 2025-11-18).
  B1628's sealed rule graded the global fit only and reported single experiments without grading them, so the register
  left P10′ open; the second release removes any doubt. The status cell is corrected with that history.
- One-dimensional pulls; θ₁₃'s correlation with θ₁₂ neglected, as in B1628; JUNO's θ₁₂ is nearly independent of θ₁₃.

## Seen first

`VERDICT topic-sweep /TM1|TM2|trimaximal|sin²θ₁₂|theta12|solar angle|JUNO/ (full text): 45 of 1528 arcs on main match (NEGATIVE 17, OPEN 1, PROVED 26, no verdict file 1)`
— among them B1612, B1613, B1620, B1625, B1628, B1640, B1655. **The register:** P-273 (JUNO's figures pinned), P-388, P-005 (P10's scope note). **Literature:** JUNO
(arXiv:2511.14593, 2609.37895); NuFIT 6.0 (arXiv:2410.05380).

## Files

`verification/data.json`, `verification/grade.py` → `two_relations.json`, `grade.json`, `grade_run.txt`. The lock:
`tests/test_b1756_junos_second_release.py`.
