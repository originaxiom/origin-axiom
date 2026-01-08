# Phase 3 — Discrete Offset Model Selection (b_PMNS)

We tested discrete fixed hypotheses for the PMNS offset b_PMNS in:
  delta_PMNS(theta) = (theta + b_PMNS) mod 2π
with delta_CKM(theta) = theta (baseline b_CKM = 0),
and targets (CKM δ, PMNS δ_CP) frozen in phase3/fit/data_frozen/.

Evidence artifact:
- phase3/outputs/tables/theta_offset_sweep.csv

Result summary (lowest χ² wins):
- b_PMNS = π: χ² = 0.675474 (best), θ* ≈ 1.146367 rad, 68% ≈ [1.120292, 1.172128]
- b_PMNS = π/2: χ² = 1.881895 (Δχ² ≈ 1.206)
- b_PMNS = -π/2: χ² = 9.093410
- b_PMNS = 0: χ² = 12.712767

Decision:
- Lock Phase 3 baseline hypothesis to b_PMNS = π (fixed; not fit).