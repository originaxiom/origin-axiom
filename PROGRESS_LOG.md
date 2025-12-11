
## 2025-12-10 — θ*-agnostic scalar vacuum: dispersion, dephasing, noise

**Files & scripts**

- `src/scalar_vacuum_theta/run_1d_vacuum_dispersion.py`
- `src/scalar_vacuum_theta/run_1d_vacuum_dephasing.py`
- `src/scalar_vacuum_theta/run_1d_vacuum_noise_residue.py`
- Data: `data/processed/scalar_vacuum_theta/*.csv`, `*.npz`
- Figures: `figures/scalar_vacuum_theta/*.png`

**Results**

1. **Dispersion (linear vacuum, no damping/noise)**  
   - Model: 1D Klein–Gordon, `m0 = 5`.  
   - Measured frequencies for modes n=1..8 agree with theory  
     `ω_th = sqrt(k^2 + m0^2)` at relative error ~10^-3.  
   - Confirms that the θ*-agnostic scalar vacuum is numerically a clean KG field.

2. **Dephasing with linear damping**  
   - Added homogeneous damping `gamma = 0.1`.  
   - For modes n=1..5, extracted dephasing rates `eta_meas` from envelope fits.  
   - All `eta_meas` match analytic `eta_th = gamma / 2 = 0.05` (or the chosen convention) at ~10^-3 relative level with R^2 ≈ 0.95.  
   - Confirms that damping is implemented correctly and does not distort dispersion.

3. **Noise, residue, and spatial coherence**  
   - Added white noise forcing with amplitude `noise_amp = 0.5`, integrated for total time ~200 with 20k samples and 6k burn-in.  
   - Mode variances roughly follow `Var(k) ~ const / ω(k)^2`; the product `Var * ω^2` is approximately flat across k with 10–30% scatter.  
   - Spatial correlation function C(r)/C(0) is well fitted by an exponential `exp(-r/ξ)` with coherence length `ξ ≈ 0.176` (in box units).  
   - The θ*-agnostic vacuum behaves as a healthy noisy medium with finite coherence length and no numerical pathologies.

**Status**

- Stage-1 θ*-agnostic scalar vacuum block is validated:
  - Correct dispersion,
  - Correct dephasing under linear damping,
  - Reasonable fluctuation spectrum and finite spatial coherence under noise.
- No φ or φ^φ entered any of these scripts; this is a pure, clean baseline vacuum ready for later insertion of a non-cancelling twist (θ*).


## 2025-12-11 — θ*-agnostic vacuum + cancellation chains

- Added θ*-agnostic scalar vacuum module (`src/scalar_vacuum_theta/`) and verified:
  - 1D dispersion matches ω² = k² + m₀² with rel. errors ~10⁻³.
  - Damped modes obey ηₖ ≈ γ (k-independent) as a clean dephasing sanity check.
  - Noisy vacuum shows Var(θₖ) ~ C/ωₖ² and an exponential spatial coherence C(r) ~ exp(-r/ξ).
- Introduced θ*-agnostic 4D lattice Δα(θ) calculator (`src/lattice_theta/lattice_delta_alpha.py`) and verified it converges for generic θ (example: θ = 2 gives Δα ≈ -7.25 with 1/R tail fit).
- Implemented discrete cancellation-chain toy model (`src/cancellation_system/`) and ran residual scans with enforced zero-sum charges:
  - Explored several θ values, including “nice” numbers (1, 1.5, 2, π) and irrational candidates (φ, φ^φ).
  - Observed mean|S|/√N grows with N for all tested θ; no special suppression for φ or φ^φ — important to keep us θ-agnostic going forward.
- Decision: keep the non-cancelling principle θ*-agnostic in all write-ups. φ and φ^φ remain hypotheses for later testing, not built-in assumptions.

---

## 2025-12-11 — Phase θ-Agnostic-0

- Consolidated a **θ\*-agnostic verification layer** across:
  - `scalar_vacuum_theta/` (dispersion, dephasing, noise residue),
  - `lattice_theta/` (4D Δα(θ) fits for several sample θ),
  - `cancellation_system/` (chain residual scaling for multiple θ).
- Logged summary in `verification_notes.md` under
  **"Phase θ-Agnostic-0: Verification Layer (2025-12-11)"**.
- Added `docs/THETA_AGNOSTIC_PROGRAM.md` to clearly state the
  non-cancelling principle, the θ-agnostic stance, and the near-term roadmap.

