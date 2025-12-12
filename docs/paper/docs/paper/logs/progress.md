# Origin Axiom — Paper Progress Log

## 2025-12-12 — Act II compiles + figures wired
- Built a minimal `docs/paper/main.tex` that inputs Act II sections.
- Fixed missing `sections/*.tex` includes by moving all `act2_*.tex` into `docs/paper/sections/`.
- Verified figure assets exist under repo root:
  - figures/lattice_theta/delta_alpha_theta_global_R12_p6.png
  - figures/lattice_theta/delta_alpha_theta_min_focus.png
  - figures/lattice_theta/delta_alpha_theta_star_R24.png
  - figures/scalar_vacuum_theta/dispersion_theta_massshift_check.png
  - figures/cancellation_system/chain_residual_scan.png
- Produced `docs/paper/main.pdf` containing the Act II theta scan result:
  - theta-star minimum around θ⋆ ≃ 2.598 and Δα(θ⋆) ≃ −8.77.
- Next: normalize build entrypoint + clean folder structure (single paper root, one build command),
  then proceed to the next Act / results integration.

## 2025-12-12 — Act II findings (θ⋆ stability zone)

### Core empirical observation
- A pronounced stability/minimum appears in the θ landscape near
  \[
    \theta_\star \approx 2.598 \quad (\text{close to } \varphi^2 = 2.618...)
  \]
- At this point the observed extremum depth is approximately
  \[
    \Delta\alpha(\theta_\star) \simeq -8.77.
  \]

### Interpretation (current)
- The “θ⋆ zone” behaves like a *preferred holonomy / phase-lock point* where the cancellation system becomes least able to fully cancel (or equivalently where the residual becomes structurally stable).
- The proximity of θ⋆ to \varphi^2 suggests the golden-ratio family may be acting as an attractor in the scan, but we treat this as a hypothesis until we stress-test sensitivity.

### What is *not* yet proven
- Whether θ⋆ is invariant under:
  - scan resolution / step size,
  - cutoff radius R / lattice size,
  - boundary conditions,
  - alternative definitions of Δα / residual metric.
- Whether the depth (-8.77) is a meaningful physical invariant or a scale artifact.

### Immediate falsification / robustness checklist
1) Re-run the θ scan at multiple resolutions (coarse → fine) and verify θ⋆ converges.
2) Re-run at multiple cutoffs (e.g. R=12, 18, 24, 30) and check if θ⋆ drifts.
3) Swap residual metric (L2 vs L∞ vs signed sum) and check if θ⋆ persists.
4) Bootstrap / jitter initial conditions and verify the minimum is not a numerical coincidence.

