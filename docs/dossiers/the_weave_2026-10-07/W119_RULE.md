# W119 — beyond tree level: does a Kähler correction or a loop move θ̄'s structural zero, or carry the first generation's forced coefficients into the data's windows? (the rule, committed before the code)

The SM-derivation seat, 2026-10-21. Committed before the script that reads it exists. Nothing here is a result.

## Why

- **The owner's order** (2026-10-21): three arcs, each done properly, then a pause to consolidate. This is the third:
  a step beyond the holomorphic tree level.
- **What the tree level left.**
  - W113: in one assignment θ̄ ∈ {0, π} at every τ by structure, but that assignment does not fit the quarks.
  - W114: θ̄ = 0 and the quark data coexist only at the Standard Model's own count.
  - W118: the composite field's forced coefficients m₁m₃/m₂² near ω are exact rationals. Two reach the up quarks'
    window and none the down quarks' or the leptons'.
- **The question.** Do the corrections beyond tree level change either result?
  - **Kähler corrections:** the matter fields' metrics, which the holomorphic couplings do not fix.
  - **Loops:** the running of the couplings between the scale where the forced structure holds and M_Z, where the
    data are.
- **Already on record, cited and not redone.** The one-loop potential for τ (W59), and main's B1686 reproducing W60 and
  W62 with "nothing computed holds τ". The departure from the symmetric points is not generated at one loop in the
  record's frames.

## Part K: the Kähler correction and θ̄ (fixed now)

- **By hand (to be checked).** Canonical normalization replaces each Yukawa Y by K_L^{−1/2} Y K_R^{−1/2}, with the
  fields' Kähler metrics K Hermitian and positive.
  - So det Y is multiplied by det(K_L)^{−1/2} det(K_R)^{−1/2}, a positive real number.
  - So arg det(Y_u Y_d), and with it θ̄ (the counterterm's phase is τ's alone), is unchanged by every Kähler metric,
    minimal or not, τ-dependent or not.
  - **W113's structural θ̄ ∈ {0, π} therefore survives every Kähler correction at tree level.**
- **The check.** At W113's forced assignment, at three τ and for 100 random Hermitian positive metrics on each of
  Q, u and d, the change in arg det(Y_u Y_d) is computed.
- **What Kähler corrections do change** (a reading, cited, not computed). Non-minimal Kähler terms allowed by the
  modular symmetry carry their own free coefficients, so they move masses and mixings (Chen, Ramos-Sánchez and Ratz,
  arXiv:1909.06910). The record has no principle that fixes them. Read with W118, the forced rational coefficients are
  predictions only if the Kähler metric is minimal.
- **θ̄ at loop level** (a reading, cited). In the Standard Model, θ̄'s renormalization first appears at high loop order
  and is negligible (Ellis and Gaillard 1979). So a structural zero stays a zero beyond tree level. With CP in the law,
  no soft phase exists in the frame to generate it at one loop.

## Part L: the running of the forced coefficients (fixed now)

- **The quantity.** The double ratio DR = m₁m₃/m₂² = (m₁/m₂)/(m₂/m₃).
  - At one loop with hierarchical Yukawas, the first two generations' ratio m₁/m₂ does not run, up to terms of
    order y₂² and |V_cb|² y₃², which are neglected.
  - m₂/m₃ runs through the third generation's Yukawas. So DR(M_Z) = F · DR(Λ), with
    F = exp(−∫ c(y) dt / 16π²), integrated over t = ln μ from ln M_Z to ln Λ.
- **The coefficients c(y)** (one loop, third generation; from the standard β functions):
  - SM: up (3/2)(y_t² − y_b²); down (3/2)(y_b² − y_t²); leptons (3/2) y_τ².
  - MSSM: up 3y_t² + y_b²; down 3y_b² + y_t²; leptons 3y_τ².
- **The running.**
  - The gauge couplings and (y_t, y_b, y_τ) are integrated at one loop from M_Z, with the SM's or the MSSM's
    coefficients throughout. The MSSM's threshold is taken at M_Z.
  - The Yukawas start from √2 m/v, divided by sin β for the top and by cos β for the bottom and the τ in the MSSM.
    W66's masses at M_Z are used, with no threshold corrections.
  - A point is kept only if every Yukawa stays below √(4π) up to Λ.
- **The scan.**
  - The SM, and the MSSM with tan β = 2, 5, 10, 20, 30, 40 and 50.
  - Λ = 10¹², 10¹⁴ and 10¹⁶ GeV.
- **The forced coefficients** (taken to hold at Λ): W68's 15 and 1, and W118's 15, 735/121, 77/4, 3/5, 5/4, 385/529
  and 1.
- **The windows** are W118's, at M_Z (W66's data and allowance).
- **A coherent point** is a scan point at which every sector has some forced coefficient with F·DR in its window.

## Weave or thread

**WEAVE-type, given the frames.**
- Part K is a statement about every Kähler metric on the weave's matter.
- Part L takes every forced coefficient on record (W68, W118) at every scan point, with none hand-picked.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| B0 | the control: in the MSSM the three gauge couplings meet within 2% at 2 × 10¹⁶ GeV, and in the SM they do not (spread above 5%) | 90% |
| B1 | the Kähler theorem: the change in arg det(Y_u Y_d) under every sampled metric is below 10⁻¹² at all three τ | 99% |
| B2 | the band: at every kept scan point, F lies in [0.4, 2.5] for each sector | 85% |
| B3 | **no coherent point:** no scan point brings forced coefficients into all three windows; in particular no forced coefficient reaches the leptons' window at any point | 95% |
| B4 | read-out: each sector's range of F, and which forced coefficient reaches which window at which points | — |

## What the outcomes mean (fixed now)

- **B1 holds (a theorem, checked).** θ̄'s structural zero cannot be moved by any Kähler correction. A θ̄ that is
  structural at tree level stays structural.
- **B3 holds.** Running between the forced scale and M_Z cannot carry the first generation's forced coefficients into
  all three sectors' data. W118's negative stands beyond tree level, in the SM and the MSSM alike.
- **B3 fails.** Some scan point brings all three sectors into their windows. That is a candidate, with the scan point
  as its one free choice. It goes to main for a full analysis with thresholds and two loops, and the count stays 0.
- **In every case** the departure from the symmetric points stays unexplained at one loop (W59, B1686). Non-minimal
  Kähler terms would add free numbers, so they cannot lower the count.

## Seen before the rule (disclosed)

- **The record's tree-level results:** W113, W114 and W118 in full, and W59 and main's B1686.
- **The β functions and the literature cited,** recalled by this seat and not re-derived here.
- **The rough size of the running,** estimated by hand: F of order exp(±0.5) for perturbative Yukawas, and the
  one-loop gauge couplings meeting near 2 × 10¹⁶ GeV in the MSSM (α⁻¹ ≈ 24.3 for all three) but not in the SM. For the
  leptons, 3/5 → 0.081 would need F ≈ 0.13, far outside that. B3's prior reflects it.
- **No running has been computed** by this seat in this project.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read.
- A failed launch is disclosed, with its log kept. Any failed prediction is recorded as failed, and any later check is
  labelled post hoc.

0 of 19.
