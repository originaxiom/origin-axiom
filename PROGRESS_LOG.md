
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

