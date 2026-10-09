# B1628 — THE DATA AND THE WEAVE'S TWO TRIMAXIMAL RELATIONS: TM1 (T̄ ⊗ T) sits 0.85σ from the measured solar angle and TM2 (T ⊗ T, where all of G is flavour) 2.74σ on NuFIT 6.0 — the data prefer TM1 but do not yet exclude TM2 at 3σ on the global fit; JUNO's first measurement, reported beside it, puts TM2 at 3.64σ

**Verdict: NEGATIVE as sealed** (R1 and R2 hold; R3 and R4 fail). cc (main), 2026-10-09. Sealed `c395a2cd5` before any
data was read (its push carried a PRACTICES currency commit, `05c848381`, disclosed). Value contact under the owner's
reopening; not blind (§3). **0 of 19.**

## 0. Seen first

As sealed: `VERDICT topic-sweep /TM1|TM2|trimaximal|sin²θ₁₂|theta12|solar angle|NuFIT/: 15 of 1399 arcs on main match (NEGATIVE 7, PROVED 8)`
— B1612, B1613 (P10), B1620, B1625 and the SM seat's W43–W44. **Literature:** the TM sum rules (Albright–Rodejohann;
Xing–Zhou); NuFIT 6.0 (arXiv:2410.05380). After the seal: the JUNO Collaboration's first result (arXiv:2511.14593), and
a paper on discrete flavour symmetries after it (arXiv:2511.19408), seen in the search, not read.

## 1. The data, read after the seal by the sealed rule

- **(1) graded:** NuFIT 6.0, Table 1, with SK atmospheric data:
  - normal ordering: sin²θ₁₂ = 0.308 (+0.012 / −0.011), 3σ range 0.275–0.345, and sin²θ₁₃ = 0.02215 (+0.00056 / −0.00058);
  - inverted ordering: the same θ₁₂, and sin²θ₁₃ = 0.02231 ± 0.00056.
- **(2) unreachable:** nu-fit.org on 2026-10-09 still failed on an expired TLS certificate, as for B1612. The newer
  release (6.1) is not graded.
- **(3) reported, not graded:** JUNO, first measurement (59.1 days, 2025-11-18), sin²θ₁₂ = 0.3092 ± 0.0087 (normal
  ordering). Its 3σ range is derived as ±3σ; θ₁₃ is taken from NuFIT 6.0.

## 2. The computation (`two_relations.py`, sealed, unchanged; `two_relations.json`)

| | sealed prediction | prior | result |
|---|---|---|---|
| **R1** | TM1 ≈ 0.318, TM2 ≈ 0.341 at the measured θ₁₃, spreads below 10⁻³ | 97% | **HOLDS** — 0.3182 and 0.3409 (θ₁₃ spreads 4 × 10⁻⁴ and 2 × 10⁻⁴) |
| **R2** | TM1 within 2σ (graded table) | 85% | **HOLDS** — 0.85σ (normal), 0.84σ (inverted) |
| **R3** | TM2 beyond 3σ (graded table) | 60% | **FAILS** — **2.74σ** (both orderings) |
| **R4** | TM2 outside the graded 3σ range | 55% | **FAILS** — 0.3409 is inside 0.275–0.345 |
| JUNO (reported) | — | — | TM1 1.04σ; **TM2 3.64σ, outside JUNO's 3σ** |

## 3. What it says

**The data prefer TM1 to TM2, at 2.7σ on the global fit and 3.6σ on JUNO's first result alone, but the sealed
3σ bar on the graded global fit is not met.**
- The weave's lepton reduction is TM1 under T̄ ⊗ T, or under T ⊗ T where c is gauge (W44). It is TM2 under T ⊗ T in
  B1620's frame.
- So the open choice of tensor and frame, GENESIS FK11 given Λ, is close to being constrained by measurement: the
  reading "T ⊗ T, all of G flavour" keeps a lepton relation only if θ₁₂ moves up.
- A global fit that includes JUNO, or JUNO's fuller data, decides it.
- Either way the 13 and 0 of 19 are unchanged: a failed relation removes a reduction, it does not refute the structure.
- **P10′ (TM2) is entered in FALSIFIER_REGISTER** beside P10.

**Disclosed.** B1612's post-seal check had graded TM2 at 4.93σ against NuFIT 6.1 from a secondary source. That number is
not reproduced on primary NuFIT 6.0 (2.74σ). A plausible reading is that 6.1 includes JUNO's first data, which would
tighten θ₁₂; it is not checked, because 6.1's primary table was unreachable. Pulls are one-dimensional, θ₁₃'s
correlation with θ₁₂ is neglected, and main recalled NuFIT 6.0's central value before the seal (stated there).

## 4. Files

`verification/two_relations.py` (sealed, unchanged), `data.json` (transcribed after the seal), `two_relations.json`,
`two_relations_run.txt`. Kill-graph entry B1628. Test: `tests/test_b1628_the_data_and_the_two_trimaximal_relations.py`.
