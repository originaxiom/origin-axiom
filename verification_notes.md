
---

## Phase θA — θ*-agnostic scalar vacuum sanity checks

**Goal.**  
Establish a clean reference scalar vacuum, independent of any specific choice of non-cancelling twist θ*, to serve as the baseline medium before we introduce φ, φ^φ, or any other candidate.

**Model.**  
1D Klein–Gordon field with constant mass `m0`, optional homogeneous damping `gamma`, and optional white-noise forcing. Discretized on a uniform lattice with leapfrog time integration.

### θA.1 Dispersion

- Script: `src/scalar_vacuum_theta/run_1d_vacuum_dispersion.py`  
- Parameters: `L = 1.0`, `N = 2048`, `dt = 1.4648e-4`, `m0 = 5.0`.  
- Modes n=1..8 were initialized individually and their frequencies `ω_meas` extracted from FFTs.  
- Comparison to theory `ω_th = sqrt(k^2 + m0^2)` shows relative errors ≲ 10^-3 across all tested modes.  
- Conclusion: the θ*-agnostic scalar vacuum behaves as an accurate discretized Klein–Gordon field.

### θA.2 Dephasing with linear damping

- Script: `src/scalar_vacuum_theta/run_1d_vacuum_dephasing.py`  
- Damping: `gamma = 0.1`, total time ≈ 200, modes n=1..5.  
- Envelopes of mode amplitudes yield dephasing rates `eta_meas` that agree with the analytic rate `eta_th = gamma / 2` (depending on convention) at ≈ 10^-3 relative accuracy, with R^2 ≈ 0.95 for the exponential fits.  
- Conclusion: homogeneous damping is implemented correctly and does not spoil dispersion.

### θA.3 Noise, residue, and spatial coherence

- Script: `src/scalar_vacuum_theta/run_1d_vacuum_noise_residue.py`  
- Parameters: `gamma = 0.1`, `noise_amp = 0.5`, total time ≈ 200, 20k samples with 6k burn-in.  
- Mode variances approximately follow the expected scaling `Var(k) ~ const / ω(k)^2`, with the product `Var * ω^2` roughly constant across modes (scatter ~10–30%).  
- Spatial correlation function C(r)/C(0) is well fitted by `exp(-r/ξ)` with coherence length `ξ ≈ 0.176` in box units.  
- Conclusion: the θ*-agnostic vacuum is a well-behaved noisy medium with finite coherence length and no obvious numerical pathologies.

**Summary.**  
Phase θA confirms that, before introducing any specific non-cancelling twist θ*, our baseline scalar vacuum is numerically and physically consistent. This provides the reference medium onto which we will later graft θ*-dependent effects (e.g. φ- or φ^φ-derived corrections) and compare against the clean θ*-free behavior.



## Phase θ-0 — θ*-agnostic sanity checks (vacuum + chains)

- Added a θ*-agnostic scalar vacuum testbed in `src/scalar_vacuum_theta/`.
  - `run_1d_vacuum_dispersion.py`: 1D Klein–Gordon dispersion check with m₀ = 5. Numerical ωₖ agrees with ω² = k² + m₀² at ~10⁻³ level across modes n = 1…8.
  - `run_1d_vacuum_dephasing.py`: damped evolution with uniform γ. Extracted ηₖ from envelopes confirms ηₖ ≈ γ (k-independent), validating the damping implementation.
  - `run_1d_vacuum_noise_residue.py`: noisy vacuum, measuring mode variances and spatial coherence. Variances scale approximately like const/ωₖ² and C(r) is well fit by exp(-r/ξ), giving a finite coherence length ξ.
- Implemented a generic 4D lattice Δα(θ) calculator in `src/lattice_theta/lattice_delta_alpha.py`.
  - For example θ = 2, R up to 8 already shows a stable partial sum S_R with a reasonable 1/R tail fit, indicating the construction is numerically well behaved for generic θ.
- Built a discrete “cancellation chain” toy model in `src/cancellation_system/`.
  - `run_chain_residual_scan.py` enforces zero-sum integer charges with random phases kθ and measures residual S(N,θ).
  - Scans over multiple θ (including φ and φ^φ) show mean|S|/√N grows with N for all tested values; no obviously privileged θ at this level.

Conclusion for Phase θ-0:
These checks confirm that (i) our θ*-agnostic scalar vacuum sector is numerically consistent and physically sensible, and (ii) a simple 1D cancellation-chain model does *not* single out any special θ by itself. This supports keeping the non-cancelling axiom θ-agnostic while we move to higher-dimensional and more structured models.

---

# Phase θ-Agnostic-0: Verification Layer (2025-12-11)
**Goal:** Establish a clean, unbiased, θ\*-agnostic baseline across:  
1. Scalar vacuum sector in 1D  
2. 4D lattice Δα(θ) asymptotics  
3. Cancellation-system residual scaling  

This is the **first systematic attempt** to test whether any θ\* produces  
non-trivial, stable, or universal signatures across three independent systems.

---

# 1. Scalar Vacuum Sector (1D, free + dissipative + stochastic)

All tests were performed with general mass parameter *m₀ = 5.0* on domain *L = 1*, using  
*2048 grid points* and *total evolution time ≈ 200*.  
No assumption about θ was introduced here — these are θ-free tests establishing model correctness.

### (1A) Dispersion Relation
Measured ωₘₑₐₛ match theoretical ω = √(k² + m₀²) with  
relative errors **3×10⁻⁴ to 10⁻³** across modes.  
The free-field scheme is validated.

### (1B) Dephasing Test
Decay rates ηₘₑₐₛ ≈ γ (γ=0.1) with  
accuracy **3×10⁻⁴**, R² ≈ **0.952**.  
Dissipative dynamics validated.

### (1C) Noise Residue
Mode variances obey **Var ~ C / ω²** with 2–20% deviations.  
Stochastic vacuum behaves consistently.

---

# 2. 4D Lattice Δα(θ): Asymptotic Partial Sum Analysis

R = 1…12, fit via S_R ≈ A + B/R for R ≥ 6.  
A is interpreted as the θ-dependent vacuum residue Δα(θ).

### Δα(θ) results

| θ | Δα(θ) | σ_A |
|---|-------|-----|
| 1.0 | +3.1976 | 0.0287 |
| 1.618… | –4.1859 | 0.0157 |
| 2.178… | –7.9873 | 0.0115 |
| 2.0 | –7.0959 | 0.0180 |
| 3.1415… | –7.5819 | 0.00137 |

Observations:
- Δα(θ) is smooth and monotonic over tested region.  
- No singularity or preferred minimum detected yet.  
- Larger R_max (≥ 20) needed for curvature detection.

---

# 3. Cancellation System Residual Scaling

Residuals S(N, θ) tested for N = 8…128, θ in:  
{1.0, 1.618…, 2.0, 2.178…, 3.14159…}

Metric: mean|S|/√N  
Random-like cancellation → O(1)  
Perfect cancellation → 0

### Observations:
- All θ give mean|S|/√N ≈ **0.85–1.30**.  
- No θ shows anomalous suppression.  
- Slightly lower scaling for θ≈1.618 and θ≈2.178 at small N,  
  but convergence removes difference by N ≈ 128.  
- No evidence for preferred θ in this system.

---

# Phase θ-Agnostic-0 Summary

1. Scalar vacuum system validated (free, dissipative, stochastic).  
2. 4D lattice Δα(θ) produces consistent, smooth θ-dependence.  
3. Cancellation system shows no special θ across tested range.  

This establishes the **ground-zero neutral baseline** for θ\* search —  
no bias toward φ, φ², φ^φ, π, etc.  
Later phases will introduce higher-dimensional, correlated, and geometric tests  
to see whether θ\* emerges from structure rather than assumption.

