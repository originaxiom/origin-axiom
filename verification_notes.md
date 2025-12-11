
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
