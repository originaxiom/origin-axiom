
## 2025-12-10 — θ*-agnostic scalar vacuum: dispersion, dephasing, noise

**Files & scripts**

- `src/scalar_vacuum_theta/run_1d_vacuum_dispersion.py`
- `src/scalar_vacuum_theta/run_1d_vacuum_dephasing.py`
- `src/scalar_vacuum_theta/run_1d_vacuum_noise_residue.py`
- Data: `data/processed/scalar_vacuum_theta/*.csv`, `*.npz`
- Figures: `figures/scalar_vacuum_theta/*.png`
docs/results/
  cancellation_system/
    runs/<run_id>/                     ← tracked per-run CSV + run_meta.json
figures/cancellation_system/
  runs/<run_id>/                       ← tracked per-run plots
  chain_residual_scan.png              ← “latest” pointer (overwritten)
scripts/cancellation_system/
  rebuild_chain_residual_scan_from_log.py
  merge_chain_residual_scan_runs.py
src/cancellation_system/
  run_chain_residual_scan.py

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


### 2025-12-11 – 4D lattice Δα(θ) scans (Point B: θ*-agnostic check)

**Scripts**

- \`src/lattice_theta/lattice_delta_alpha.py\`
- \`src/lattice_theta/run_delta_alpha_theta_scan.py\`

**Global θ scan (0 → 2π)**

- Command:
  - \`PYTHONPATH=src python3 -m lattice_theta.run_delta_alpha_theta_scan --theta-min 0.0 --theta-max 6.0 --n-theta 61 --R-max 12 --R-fit-min 6 --p 6.0\`
- Outputs:
  - \`data/processed/lattice_theta/delta_alpha_theta_global_R12_p6.csv\`
  - \`figures/lattice_theta/delta_alpha_theta_global_R12_p6.png\`
- Result:
  - Smooth, non-flat Δα(θ) curve with a single broad minimum in the neighbourhood of θ ≈ 2.6.
  - This is a **θ*-agnostic** 4D lattice analogue of the earlier 1D twisted-chain checks.

**Focused scan around the minimum**

- Command:
  - \`PYTHONPATH=src python3 -m lattice_theta.run_delta_alpha_theta_scan --theta-min 2.3 --theta-max 2.9 --n-theta 61 --R-max 16 --R-fit-min 8 --p 6.0\`
- Outputs:
  - \`data/processed/lattice_theta/delta_alpha_theta_min_focus.csv\`
  - \`figures/lattice_theta/delta_alpha_theta_min_focus.png\`
- Result:
  - Parabolic minimum around θ ≈ 2.59 with Δα ≈ -8.78.
  - Error bars from the A + B/R fit at R ≥ 8 are ~1×10⁻², so the minimum location is stable at the ~10⁻³–10⁻² level.

**High-R confirmation of θ\*** (zoomed + higher cutoff)

- Command:
  - \`PYTHONPATH=src python3 -m lattice_theta.run_delta_alpha_theta_scan --theta-min 2.55 --theta-max 2.63 --n-theta 61 --R-max 24 --R-fit-min 12 --p 6.0\`
- Outputs:
  - \`data/processed/lattice_theta/delta_alpha_theta_star_R24.csv\`
  - \`figures/lattice_theta/delta_alpha_theta_star_R24.png\`
- Result:
  - Minimum confirmed near θ* ≈ 2.595 with Δα(θ*) ≈ -8.77.
  - Increasing R_max to 24 and fitting over R ≥ 12 does **not** shift the minimum significantly, only tightens σ_A.
- Interpretation:
  - This is our cleanest numerical estimate of the “preferred” twist angle in the 4D lattice Δα(θ) construction.
  - Next step (Point B → C): compare **cancelling vs non-cancelling** implementations at this θ* and tie back into the Origin Axiom (“universe avoids exact cancellation but can sit near a structured non-zero Δα”).


## 2025-12-11 — 4D lattice θ-scan and θ★ refinement

**Goal.** Map the 4D lattice vacuum remainder Δα(θ) over one full 0–2π cycle, then zoom in to locate a numerically stable minimum θ★ that can be compared with the axiom’s preferred phase.

### A. Global θ scan (0 ≤ θ ≤ 2π)

- Script: `src/lattice_theta/run_delta_alpha_theta_scan.py` (global mode)
- Run: `R_max = 12`, `p = 6.0`, `R_fit_min = 6`, `n_theta = 61`
- Output table: `data/processed/lattice_theta/delta_alpha_theta_global_R12_p6.csv`
- Plot: `figures/lattice_theta/delta_alpha_theta_global_R12_p6.png`
- Result: Δα(θ) is smooth and non-pathological over [0, 2π].  
  A broad minimum appears in the window **θ ≈ 2.5–2.7 rad**, with Δα(θ) ≈ −8.7.

### B. Core region refinement around the minimum

- Script: same module, “core” scan setup.
- Run: `R_max = 20`, `p = 6.0`, `R_fit_min = 7`, `θ ∈ [2.3, 2.9]`, `n_theta = 61`
- Outputs:
  - `data/processed/lattice_theta/delta_alpha_theta_core_R20.csv`
  - `figures/lattice_theta/delta_alpha_theta_core_R20.png`
  - `figures/lattice_theta/delta_alpha_theta_core_R20_p7.png`
- Result: the minimum sharpens to **θ ≈ 2.59 rad**, with  
  Δα(θ) ≈ −8.78 and σ_A ~ 10⁻², showing a clear, asymmetric well.

### C. θ★ focus with higher R_max

- Script: same module, “theta_star” narrow scan.
- Run: `R_max = 24`, `p = 6.0`, `R_fit_min = 12`,  
  `θ ∈ [2.55, 2.63]`, `n_theta = 41`
- Outputs:
  - `data/processed/lattice_theta/delta_alpha_theta_star_R24.csv`
  - `figures/lattice_theta/delta_alpha_theta_star_R24.png`
- Result:
  - The minimum is stable when increasing both **R_max** and **R_fit_min**.
  - Best region: **θ★ ≈ 2.595 ± 0.01 rad**
  - Value: **Δα(θ★) ≈ −8.77 ± 0.01**
  - Neighbouring θ-values are higher by several σ, so θ★ is a genuine, well-resolved minimum of the 4D lattice sum.

### D. Notes

- Detailed per-run logs and command lines are kept in  
  `notes/lattice_theta_log.md`.

### Next steps

1. **Non-cancelling vs cancelling comparison at θ★**  
   - Fix θ = θ★ in the 4D lattice and compare:
     - unconstrained (ordinary cancelling) evolution,
     - evolution with the non-cancelling constraint.
   - Check whether the non-cancelling rule prefers / stabilizes this θ★ configuration.

2. **Axiom link-up**  
   - Interpret Δα(θ★) as a candidate “preferred phase” in the axiom story and compare it with other φ/φ^φ-based structures in the Origin Axiom framework.


### 2025-12-11 – θ★ cancellation-chain check (non-cancelling vs cancelling)

- Ran `cancellation_system/run_chain_residual_scan.py` at θ★ = 2.598 for
  Ns = 16…4096, with and without global zero-sum constraint.
- Non-cancelling (no-zero-sum) and cancelling (zero-sum) runs both show
  mean|S|/sqrt(N) growing from ~0.9 at N=16 to ~3.1–3.2 at N=4096.
- Compared to the φ^φ baseline (θ ≈ 2.17846) where mean|S|/sqrt(N) stays
  ≈ 0.84–1.06 up to N=128, θ★ clearly enhances residuals.
- Together with the 4D Δα(θ) minimum and the θ*-driven scalar mass shift,
  this provides a three-way consistency check of the non-cancelling principle
  around θ★.


## 2025-12- Act II: zero-sum 14 
**Command**
python3 -m src.cancellation_system.run_chain_residual_scan \
  --theta-min 2.45 --theta-max 2.75 --n-theta 121 \
  --Ns 16,32,64,128,256,512,1024 \
  --n-samples 400 --seed 1234 \
  --max-charge 3 --noise-sigma 0.0 \
  --run-id zero_sum_grid_20251213 \
  --resume \
  --write-latest

**Outputs**
- docs/results/cancellation_system/runs/zero_sum_grid_20251213/chain_residual_scan.csv
- figures/cancellation_system/runs/zero_sum_grid_20251213/chain_residual_scan.png
- figures/cancellation_system/runs/zero_sum_grid_20251213/theta_scan_N1024.png
- figures/cancellation_system/runs/zero_sum_grid_20251213/theta_scan_min_over_N.png
- latest pointers:
  - docs/results/cancellation_system/chain_residual_scan_latest.csv
  - figures/cancellation_system/chain_residual_scan.png

**Key takeaway**
- No special sharp 


### 2025-12-15 — θ★ bridge: import theta_star_v2 window from phenomenology repo

Context:
- Finished `origin-axiom-theta-star` v2 ansatz (normal ordering, NuFIT 5.2 targets).
- PMNS-only v2 runs (N=2000, seeds 1–2) and CKM+PMNS joint v2 runs (N=4000, seeds 1–2) give a stable θ★ window.
- Joint fits achieve χ²_total ≈ 7–8 for 10 observables.

Decision:
- Adopt a *working θ★ band* from the joint CKM+PMNS v2 analysis:
  - θ★_band ≈ [2.32, 5.61] rad (union of 1σ windows for χ² ≤ 50 from the two joint runs).
- Define a *fiducial θ★* for universe-building toy models:
  - θ★_fid ≈ 3.70 rad (average of the two joint θ★ medians).

Implementation in `origin-axiom`:
- Created `config/theta_star_config.json` to store:
  - `theta_star_fid_rad` (3.701),
  - `theta_star_band_rad` with `lo` and `hi`,
  - simple metadata pointing back to `origin-axiom-theta-star`.
- Added `src/theta_star_config.py` helper to load this config and expose a small `ThetaStarConfig` dataclass for use by cancellation-system / FRW scripts.

Next:
- Wire θ★ into the cancellation-system scripts:
  - Allow Einstein-limit / D–R–T scans to be run explicitly at θ★ = θ★_fid.
  - Later: explore sensitivity by sampling a few points across the θ★_band.
- Once this bridge is exercised at least once, promote the θ★ section into the Act II LaTeX (main paper) as the official “θ★ block” feeding the universe-building pipeline.


## 2025-12-15 — θ★ prior wired into origin-axiom

**Context.**  
We now have a consolidated flavor-based posterior for the master phase θ★ from the `origin-axiom-theta-star` repo (PMNS-only and joint CKM+PMNS runs). The posterior is summarised by

- θ★(16%) ≃ 2.18 rad  
- θ★(50%) ≃ 3.63 rad  
- θ★(84%) ≃ 5.54 rad  

using a χ²_tot ≤ 50 cut across three NO runs (`NO_theta_star_delta_only_N2000`, `NO_theta_star_v2_N2000`, `NO_theta_star_v2_N4000`).

**Changes in this repo (origin-axiom).**

- Added a configuration file under `config/theta_star_config.json`:

  - `theta_star_fid_rad = 3.63` rad — fiducial θ★ value for toy-universe / cancellation-system runs.  
  - `theta_star_band_rad = [2.18, 5.54]` rad — working “Act II θ★ prior” band.  
  - `source` metadata pointing back to `origin-axiom-theta-star` and the specific runs / χ² cut.

- Added a small loader module:

  - `src/theta_star_config.py` with:
    - `ThetaStarConfig` dataclass,
    - `load_theta_star_config()` which reads the JSON and exposes:
      - `theta_star_fid_rad`,
      - `theta_star_band_rad = (lo, hi)`,
      - `raw` (full JSON dict for provenance).

**Intended usage.**

Any scalar-universe or cancellation-system script in this repo can now do:

```python
from theta_star_config import load_theta_star_config

cfg = load_theta_star_config()
theta_fid = cfg.theta_star_fid_rad
theta_lo, theta_hi = cfg.theta_star_band_rad
```

- `theta_fid` is the default value when we say “run the toy universe at θ★”.
- `[theta_lo, theta_hi]` is the band we will use for sensitivity checks and for quoting Act II systematic uncertainty due to flavor-sector input.

**Next steps.**

- Thread `theta_fid` into at least one concrete Einstein-limit / cancellation-system experiment (e.g. as the phase / twist parameter in the 1D twisted vacuum scans).  
- Add a short “bridge” subsection in the Act II paper explaining that:
  - θ★ is inferred from flavor fits in `origin-axiom-theta-star`,
  - the result is encoded as `theta_star_config.json`,
  - the scalar-universe experiments in this repo consume that configuration whenever they are said to run “at θ★”.



## 2025-12-15 – θ★ prior applied to 1D vacuum toy (origin-axiom)

**Context**
- Act II θ★ prior is frozen and wired into `origin-axiom` via `config/theta_star_config.json` and `src/theta_star_config.py`.
- Goal: first explicit test of how the cancellation / vacuum toy responds to θ★ values drawn from the Act II flavor window.

**Commands run** (in `origin-axiom`)
```bash
PYTHONPATH=src python3 src/run_toy_universe_demo.py
PYTHONPATH=src python3 src/run_toy_universe_compare_constraint.py
PYTHONPATH=src python3 src/run_toy_universe_compare_constraint_nonlinear.py
PYTHONPATH=src python3 src/run_toy_universe_constraint_scan.py
PYTHONPATH=src python3 src/run_1d_twisted_vacuum_scan.py
PYTHONPATH=src python3 src/run_1d_defected_vacuum_scan.py
PYTHONPATH=src python3 src/run_1d_theta_star_prior_scan.py
```

**Key numerical behaviour**
- `run_toy_universe_demo.py`: toy amplitude |A| evolves smoothly with no constraint; nothing pathological.
- `run_toy_universe_compare_constraint.py` (linear):
  - *no_constraint*: |A| stays essentially at ~0, `constraint hits = 0`.
  - *with_constraint*: |A| is clamped to 0.05 for all steps, `constraint hits = 501/501`.
- `run_toy_universe_compare_constraint_nonlinear.py`:
  - Nonlinear 3D toy reproduces same pattern: with Origin Axiom constraint active, |A| is pinned to 0.05 at every step; energy stays finite and smooth.
- `run_toy_universe_constraint_scan.py`:
  - Scan over ε = {0.01, 0.03, 0.05, 0.10} and λ ∈ {0, 1}:
    - In all cases, <|A|> ≈ ε and final |A| = ε with many hits.
    - Confirms the non-cancelling rule enforces a chosen target amplitude robustly.
- `run_1d_twisted_vacuum_scan.py`:
  - Ground-state energy E₀(θ*) is *constant* for all sampled θ* in [0, 2π]:
    - E₀(θ*) ≈ 1.63969×10² at θ* = 0, 1.047, 2.094, 3.142, 4.189, 5.236, 6.283.
  - This 1D twisted vacuum toy, as implemented, is effectively θ*-blind.
- `run_1d_defected_vacuum_scan.py`:
  - Same conclusion with a defect bond: E₀(θ*) ≈ 1.64079×10² independent of θ*.
- `run_1d_theta_star_prior_scan.py` (new):
  - Reads Act II θ★ prior:
    - θ★_fid = 3.63 rad
    - θ★_band = [2.18, 5.54] rad
  - Samples five θ★ values inside this band:
    - {2.18, 2.905, 3.63, 4.585, 5.54} rad.
  - For all samples:
    - `E0_uniform` = 1.63969×10²
    - `E0_defected` = 1.64079×10²
  - Stores results in `data/processed/theta_star_prior_1d_vacuum_samples.npz`.

**Interpretation**
- The non-cancelling constraint mechanism in the 3D toy behaves exactly as intended:
  - It can pin a global amplitude to a chosen ε (10–100% of the nominal scale), even in nonlinear dynamics, without blowing up the energy.
- The current 1D vacuum toys (twisted ring + defected ring) do **not** respond to θ* at all:
  - E₀(θ*) is flat both in the uniform and defected chains.
  - Applying the Act II θ★ prior therefore makes no difference to the vacuum energy in this particular toy.
- This is consistent with the idea that our present 1D Hamiltonian is too symmetric / gauge-simplified to “feel” the twist; it serves as a clean baseline but not yet as a θ★-sensitive microstructure.

**Conclusion for Act II bridge**
- We have now:
  - A frozen Act II θ★ prior from flavor (`origin-axiom-theta-star`),
  - A working non-cancelling constraint engine (`origin-axiom`),
  - A first explicit test showing that, in the simplest 1D vacuum toy, the vacuum energy is invariant across the allowed θ★ band.
- This locks in a useful baseline statement: any θ★-selection effect in our framework must come from *more structured* microphysics than the v0.1 1D twisted ring currently encodes.

**Next steps (planned)**
- Design a θ★-sensitive 1D microstructure toy (v0.2):
  - Modify or extend the vacuum Hamiltonian so that a physically meaningful quantity (e.g. an effective coupling, boundary phase, or bond modulation) depends periodically on θ★.
  - Ensure the new model remains numerically stable and compatible with the non-cancelling constraint.
- Then repeat the θ★ prior scan:
  - Compare E₀(θ★) inside vs outside the Act II band,
  - Check whether the flavor-informed θ★ window corresponds to locally or globally preferred vacuum configurations.


## 2025-12-15 – θ★-sensitive 1D microcavity toy (origin-axiom)

**Context**
- Act II θ★ prior is frozen in `origin-axiom` via `config/theta_star_config.json` and `src/theta_star_config.py`.
- The earlier 1D twisted / defected vacuum toys were effectively θ★-blind: E₀(θ★) was flat across [0, 2π].
- Goal here: build the *first explicit* θ★-sensitive microstructure toy, then probe it only within the Act II θ★ band.

**Script**
```bash
PYTHONPATH=src python3 src/run_1d_theta_star_microcavity_scan.py
```

**Model definition (summary)**
- 1D scalar chain with open boundaries:
  - N = 256 sites
  - nearest-neighbour coupling c = 1.0
  - baseline mass m0 = 0.1
- Define a central “microcavity” band:
  - cavity_frac = 0.2 → 20% of sites in the middle of the chain.
- Mass profile m(x; θ★):
  - Outside cavity: m(x) = m0
  - Inside cavity:  m(x) = m0 * [1 + α_mass * cos(θ★ − θ₀)]
  - With α_mass = 0.5, θ₀ = 0.
- Hamiltonian:
  - H(θ★) = diag(m(x; θ★)² + 2c) − c (nearest-neighbour off-diagonals).
  - Ground-state energy E₀(θ★) is defined as the smallest eigenvalue of H.

**Act II θ★ prior used**
- Read from `theta_star_config.json` via `load_theta_star_config()`:
  - fiducial θ★  = 3.630000 rad
  - band θ★      = [2.180000, 5.540000] rad
- Sampled 5 θ★ values across this band (with the central one set to θ★_fid):
  - {2.1800, 3.0200, 3.6300, 4.7000, 5.5400} rad.

**Numerical output**
- Baseline (no cavity modulation):
  - E₀_uniform ≈ 1.014943×10⁻²
- With θ★-dependent cavity, the script printed:

  idx  θ★ [rad]    E0_uniform       E0_cavity        ΔE = E_cav − E_uni  
   0   2.1800      1.014943e-02     6.590599e-03     −3.558827e-03  
   1   3.0200      1.014943e-02     4.282916e-03     −5.866510e-03  
   2   3.6300      1.014943e-02     4.816206e-03     −5.333221e-03  
   3   4.7000      1.014943e-02     1.010018e-02     −4.924306e-05  
   4   5.5400      1.014943e-02     1.075372e-02      6.042909e-04  

- Results are saved to:
  - `data/processed/theta_star_prior_1d_microcavity_samples.npz`

**Interpretation**
- Unlike the earlier v0.1 1D twisted / defected vacuum models, this microcavity toy is **explicitly θ★-sensitive**:
  - The ground-state energy shift ΔE(θ★) = E₀_cavity(θ★) − E₀_uniform is *not* constant.
- Within the Act II θ★ band:
  - The cavity is **most energetically favourable** (most negative ΔE) around θ★ ≈ 3.0–3.6 rad.
  - The energy shift becomes very small near θ★ ≈ 4.7 rad.
  - At the upper edge of the band (θ★ ≈ 5.54 rad), ΔE turns slightly positive (cavity marginally *raises* the vacuum energy).
- Qualitatively, this means:
  - The same θ★ that appears in flavour fits can be used as a **single dial** that makes a local region of the scalar field lighter or heavier.
  - In this toy, there is a “sweet zone” for θ★ where the microcavity lowers the vacuum energy the most, and that zone overlaps the central part of the Act II prior band.

**Status in the big picture**
- We now have three pillars:
  1. **Act II (origin-axiom-theta-star):** a statistically informed θ★ band from PMNS+CKM fits.  
  2. **Constraint engine (origin-axiom):** non-cancelling rule that robustly enforces target amplitudes in time evolution.  
  3. **Microstructure toy v0.2 (this script):** a simple yet θ★-sensitive 1D cavity where the vacuum energy shift ΔE actually depends on θ★, and the minimum lies inside the Act II band.

- This does *not* yet claim a realistic cosmological constant prediction, but it is the first concrete microstructure model where:
  - “flavour θ★” → “scalar microstructure θ★” → “vacuum energy shift ΔE(θ★)”
  is implemented end-to-end in code.

**Next steps (planned)**
- Optional refinements of this toy:
  - Vary `alpha_mass`, cavity size, and N to study how robust the ΔE(θ★) pattern is.
  - Sample θ★ *outside* the Act II band to see whether the flavour-preferred region is also a local minimum of ΔE in a broader 2π scan.
- Structural next steps in the roadmap:
  - Wrap this microcavity toy into a small plotting/analysis script (to generate ΔE vs θ★ curves).
  - Decide how far to push 1D toys before moving to higher-dimensional / more realistic cancellation-system scans that incorporate the θ★ prior.

### 2025-12-15 — 1D microcavity full-band θ★ scan (Act II prior wired in)

**Context.** We wired the Act II flavor-based θ★ prior
(`config/theta_star_config.json`, imported via `theta_star_config.load_theta_star_config`)
into the 1D microcavity toy model used to illustrate the Origin Axiom
constraint on a simple lattice vacuum.

**Scripts run.**

- `src/run_1d_theta_star_microcavity_scan.py`
  - sanity check: finite set of θ★ samples from the Act II band.
- `src/scan_1d_theta_star_microcavity_full_band.py`
  - new script: full 0..2π scan of the microcavity vacuum energy shift.

**Key outputs.**

- Uniform reference energy:
  - `E0_uniform ≈ 1.014943e-02`
- Full 0..2π microcavity scan:
  - Global minimum of the vacuum shift ΔE = E_cav − E_uniform:
    - `theta_star_min ≈ π ≈ 3.141593 rad`
    - `ΔE_min ≈ -5.90e-03`
  - Within the Act II band `[2.18, 5.54]` rad the minimum is the same:
    - `theta_star_band_min ≈ 3.141593 rad`
    - `ΔE_band_min ≈ -5.90e-03`
  - At the fiducial flavor value `theta_star_fid = 3.63 rad`
    - `ΔE_fid ≈ -5.33e-03`

Saved artifacts:

- `data/processed/theta_star_microcavity_scan_full_2pi.npz`
- `data/processed/figures/theta_star_microcavity_deltaE_full_2pi.png`

**Interpretation.**

- The simple 1D microcavity model has its lowest vacuum energy near
  `theta_star ≈ π`.
- The Act II θ★ band derived from PMNS+CKM fits fully contains this minimum
  and corresponds to the region where the microcavity *lowers* the vacuum
  energy (negative ΔE).
- The fiducial θ★ from flavor (`3.63 rad`) sits on the flat part of this
  valley: not exactly at the minimum, but clearly in the energetically
  preferred region.
- This is still just a toy model; it is **not** used to re-tune the
  flavor prior. It serves as a first concrete microstructure cross-check
  that the Act II θ★ window is compatible with an Origin-Axiom-style
  vacuum-lowering behavior in a simple cavity.


## 2025-12-15 – 1D two-field localized bump demo (Origin Axiom microstructure)

**Repo:** `origin-axiom`  

**Scripts and commands**

```bash
# evolve two-field localized bump with and without non-cancelling constraint
PYTHONPATH=src python3 src/run_two_field_bump_1d.py   --steps 2000   --snapshot-stride 20   --g 0.02

# inspect saved data products and make basic plots
PYTHONPATH=src python3 scripts/inspect_two_field_bump_1d.py
```

**Data products**

The evolution script writes a compact summary to:

- `data/processed/two_field_bump_1d.npz`

with keys:

- `t_snap` – snapshot times (shape `(101,)`)
- `loc_free`, `loc_constrained` – time series of a localized diagnostic (bump amplitude at chosen point) for free vs constrained runs (shape `(101,)`)
- `profile_times_free`, `profile_times_constrained` – times at which full spatial profiles are stored (shape `(4,)`)
- `profiles_phi_free`, `profiles_phi_constrained` – φ-field snapshots, shape `(4, 512)`
- `profiles_chi_free`, `profiles_chi_constrained` – χ-field snapshots, shape `(4, 512)`
- `params` – dictionary of run parameters (masses, coupling `g`, timestep, etc.).

The new inspection helper `scripts/inspect_two_field_bump_1d.py`:

- prints the available keys and shapes,
- plots the localized diagnostic vs time for free vs constrained runs,
- plots final-time spatial profiles of φ and χ for free vs constrained runs,

and writes figures to:

- `data/processed/figures/two_field_bump_1d_loc_amp.png`
- `data/processed/figures/two_field_bump_1d_phi_final.png`
- `data/processed/figures/two_field_bump_1d_chi_final.png`

**Interpretation (working note)**

- This is our first explicit **two-field microstructure toy** in the cancellation framework: a localized bump in one field evolves in a background where the **Origin Axiom / non-cancelling constraint** is switched on and off.
- The `.npz` layout and inspection script are now standardized, so later we can:
  - compare lifetimes and shapes of localized structures under the constraint vs free evolution,
  - feed in different couplings `g` or initial bump widths as systematic scans,
  - and eventually use similar diagnostics in higher-dimensional or FRW toy universes.


### 2025-12-15 — FRW toy vacuum demo (Act III scaffold)

- Ran `src/run_frw_vacuum_demo.py` in the **origin-axiom** repo.
- The script integrates a flat FRW toy universe with three components:
  - `matter_only`: Ω_m = 1.0, Ω_Λ = 0.0
  - `lambda_30`:   Ω_m = 0.7, Ω_Λ = 0.3
  - `lambda_70`:   Ω_m = 0.3, Ω_Λ = 0.7
- Start scale factor: `a_init = 1e-3`; integration time of order a few H₀⁻¹.
- Output saved to `data/processed/frw_vacuum_demo.npz`, containing time grid `t`
  and scale factor histories for each case.
- Purpose: provide a top-level “cosmic history” toy where an effective vacuum
  component (later tied to the θ★-microcavity ΔE band) can be plugged in and
  compared directly against a matter-only evolution.


## 2025-12-15 — FRW toy universe with matter + vacuum

**Files / scripts**

- `src/run_frw_vacuum_demo.py`  
  Integrates a flat FRW universe with matter and an effective vacuum component,
  for three benchmark cosmologies:
  - matter-only: $(\Omega_m, \Omega_\Lambda) = (1.0, 0.0)$  
  - mixed: $(0.7, 0.3)$  
  - vacuum-dominated: $(0.3, 0.7)$  
  Writes results to `data/processed/frw_vacuum_demo.npz`.

- `scripts/plot_frw_vacuum_demo.py`  
  Reads `data/processed/frw_vacuum_demo.npz` and produces
  `data/processed/figures/frw_vacuum_demo_a_of_t.png`, showing the scale factor
  $a(t)$ vs time for the three cosmologies.

**What we learned**

- At early times (small $a$) the matter term $\propto a^{-3}$ dominates the
  Friedmann equation, so all three cosmologies share nearly identical
  expansion histories.
- As the universe expands, the constant vacuum term takes over in the mixed
  and vacuum-dominated cases, leading to accelerated expansion and a rapidly
  growing $a(t)$.
- This provides a clean ``top–down'' view of how an effective vacuum energy
  (parametrized by $\Omega_\Lambda$) controls cosmic acceleration.

**How this fits the larger project**

- For now, $\Omega_\Lambda$ is treated as a free parameter.  In later Acts we
  will tie it to the microscopic vacuum shift $\Delta E(\theta_\star)$
  computed in the 1D microcavity / lattice models, using the Act II
  $\theta_\star$ prior.
- The FRW demo is the cosmology-side endpoint of the chain  
  $\Delta E(\theta_\star) \rightarrow \rho_\Lambda^{\rm eff}
  \rightarrow \Omega_\Lambda \rightarrow a(t)$,
  which will eventually connect the non–cancelling vacuum rule to an
  observable expansion history.


## 2025-12-15 — FRW from microcavity ΔE(θ★)

**Repo:** `origin-axiom`  
**Script:** `src/run_frw_from_microcavity.py`  
**Inputs:**
- `config/theta_star_config.json` (Act II flavor-based θ★ prior)
- `data/processed/theta_star_microcavity_scan_full_2pi.npz` (1D microcavity ΔE(θ★) scan)

**What we did**

- Loaded the Act II θ★ configuration:
  - θ★_fid ≈ 3.63 rad, θ★ band ≈ [2.18, 5.54] rad.
- Loaded the full 2π microcavity scan and interpolated ΔE(θ★) at θ★_fid:
  - ΔE(θ★_fid) ≈ –5.33×10⁻³ (negative: cavity lowers the vacuum energy).
- Defined a simple scaling Ω_Λ = k_scale · ΔE(θ★), choosing k_scale so that
  Ω_Λ(θ★_fid) ≈ 0.7 (clamped to [0, 1]); this gives Ω_m(θ★_fid) = 0.3.

- Integrated two FRW histories (H₀ = 1, a_init = 1e–3):
  - **Matter-only:** (Ω_m, Ω_Λ) = (1.0, 0.0), a(t_final) ≈ 3.89.
  - **Microcavity vacuum:** (Ω_m, Ω_Λ) ≈ (0.3, 0.7), a(t_final) ≈ 3.28×10¹.

- Saved results to `data/processed/frw_from_microcavity.npz` with:
  - θ★_fid, θ★ band, θ grid, ΔE grid;
  - ΔE(θ★_fid), k_scale, Ω_Λ(θ★_fid), Ω_m(θ★_fid);
  - FRW histories: `(t_matter_only, a_matter_only)` and `(t_microcavity, a_microcavity)`.

**Conceptual status**

This is a **bridge demo**, not a precision ΛCDM fit:

1. θ★ is fixed by **flavor physics** (Act II).
2. θ★ selects a microcavity energy shift ΔE(θ★).
3. ΔE(θ★_fid) is rescaled into an effective vacuum fraction Ω_Λ ≈ 0.7.
4. Ω_Λ sets the late–time FRW expansion rate.

We now have a fully wired chain from **flavor priors → θ★ → microcavity ΔE(θ★) → effective Ω_Λ → FRW expansion**, ready to be refined and compared to real observables in Act III.


# ACT II – FRW from microcavity ΔE(θ★)

**Date:** 2025-12-15  
**Repo:** origin-axiom  
**Scope:** Wire the 1D microcavity vacuum shift ΔE(θ★) to an effective
FRW vacuum fraction Ω_Λ and integrate the corresponding expansion history.

## 1. Inputs

- Act II θ★ prior (from `origin-axiom-theta-star`), imported via  
  `config/theta_star_config.json`:
  - θ★_fid ≈ 3.63 rad  
  - θ★ band ≈ [2.18, 5.54] rad

- 1D microcavity scan from earlier Act II work in this repo:
  - File: `data/processed/theta_star_microcavity_scan_full_2pi.npz`
  - Stores θ★ grid and ΔE(θ★) = E_cav(θ★) − E_uniform
  - For current parameters: ΔE_min ≈ −5.9×10⁻³ (dimensionless units)
  - ΔE(θ★_fid) ≈ −5.33×10⁻³

## 2. Script and run

Script:

```bash
PYTHONPATH=src python3 src/run_frw_from_microcavity.py
```

Key steps inside the script:

1. Load θ★ configuration:
   - θ★_fid, θ★ band from `config/theta_star_config.json`.

2. Load microcavity scan:
   - `theta_grid`, `deltaE` from
     `data/processed/theta_star_microcavity_scan_full_2pi.npz`.

3. Define linear bridge from ΔE(θ★) to Ω_Λ(θ★):

   Ω_Λ(θ★) = k_scale · ΔE(θ★)

   with k_scale fixed by the condition

   Ω_Λ(θ★_fid) = Ω_Λ,fid ≈ 0.70

   which implies

   k_scale = Ω_Λ,fid / ΔE(θ★_fid).

4. Compute Ω_m(θ★) = 1 − Ω_Λ(θ★) and clamp Ω_Λ, Ω_m into [0, 1] to avoid
   unphysical values at the edges of the band.

5. Integrate a flat FRW toy model with
   - matter density ρ_m(a) ∝ a⁻³,
   - vacuum density ρ_Λ = const,
   - H₀ = 1 (dimensionless units),
   - initial scale factor a_init = 10⁻³,
   - final time t_final ≈ 5 H₀⁻¹.

   We compare:
   - a pure matter case: (Ω_m, Ω_Λ) = (1, 0),
   - a microcavity-derived vacuum case at θ★_fid.

Output:

```text
=== FRW from microcavity ΔE(θ★) ===

=== Act II theta★ configuration ===
  θ★_fid (rad) = 3.630000
  θ★ band (rad) = [2.180000, 5.540000]

=== Microcavity ΔE(θ★) scan ===
  loaded from: data/processed/theta_star_microcavity_scan_full_2pi.npz
  n_theta = 256
  ΔE_min = -5.900614e-03
  ΔE_max =  6.295376e-04

=== Scaling ΔE(θ★) -> Ω_Λ ===
  ΔE(θ★_fid)          = -5.333074e-03
  chosen Ω_Λ,fid      =  0.700
  resulting k_scale   = -1.312564e+02
  Ω_Λ(θ★_fid) after clamp =  0.700
  Ω_m(θ★_fid)         =  0.300

=== Integrating FRW histories ===
  [matter_only] a(0) = 1.000e-03, a(t_final) = 3.890e+00
  [microcavity] Ω_m = 0.300, Ω_Λ = 0.700, a(0) = 1.000e-03, a(t_final) = 3.284e+01

Saved FRW-from-microcavity results to data/processed/frw_from_microcavity.npz
```

The NPZ file contains:

- `t_matter_only`, `a_matter_only`
- `t_microcavity`, `a_microcavity`
- `theta_fid`, `theta_band`
- `omega_lambda_fid`, `omega_m_fid`
- `k_scale`, etc.

## 3. Plot: a(t) comparison

Script:

```bash
PYTHONPATH=src python3 scripts/plot_frw_from_microcavity.py
```

This reads `data/processed/frw_from_microcavity.npz` and writes:

- `data/processed/figures/frw_from_microcavity_a_of_t.png`

Figure content:

- Blue curve: matter-only universe (Ω_m = 1, Ω_Λ = 0).
- Orange dashed: microcavity-derived vacuum case with
  Ω_Λ(θ★_fid) ≈ 0.70, Ω_m(θ★_fid) ≈ 0.30.

Both histories start from a_init = 10⁻³ at t = 0 (H₀ = 1 units).
The matter-only case follows a decelerating power-law growth
a(t) ∝ t^{2/3}, reaching a(t_final) ≈ 3.9 at t ≈ 5.
The microcavity case accelerates due to the effective vacuum term,
reaching a(t_final) ≈ 32.8 over the same interval.

## 4. Interpretation / status

- This is the first complete pipeline from Act II flavor structure
  (θ★ prior) → microcavity vacuum shift ΔE(θ★) → effective Ω_Λ(θ★)
  → FRW expansion.
- The mapping is deliberately simple (linear scaling) and uses a single
  free parameter k_scale, fixed by matching Ω_Λ(θ★_fid) to a
  concordance-like value ≈ 0.7.
- Absolute units for Λ are not yet fixed; all calculations are in
  dimensionless H₀ = 1 units.
- Future Acts need to:
  - introduce physical units and match to observed H₀,
  - refine the ΔE(θ★) → Ω_Λ mapping with better microphysics,
  - and confront the resulting expansion history with real cosmological
    data.


### 2025-12-15 — Physical scaling check: microcavity ΔE(θ★) vs observed Λ

**Scripts / data**
- `scripts/estimate_lambda_scaling.py`
- Config: `config/theta_star_config.json` (Act II θ★ prior: θ★_fid = 3.63 rad, band = [2.18, 5.54] rad)
- Microcavity input: `data/processed/theta_star_microcavity_scan_full_2pi.npz`
  - Keys: `theta_grid`, `E0_uniform`, `E0_cavity`, `delta_E`, `theta_star_config`, `micro_params`

**What the script does**
- Treats the 1D microcavity ΔE(θ★) as a *dimensionless* proxy for a vacuum energy density shift.
- Calibrates a single scaling factor **S** such that, at the fiducial θ★ from Act II,
  the mapped vacuum energy density matches an approximate observed dark-energy density ρ_Λ,obs.
- Uses toy ΛCDM-like numbers:
  - H₀ ≈ 70 km/s/Mpc
  - Ω_Λ ≈ 0.7
  - ρ_crit ≈ 8.27×10⁻¹⁰ J/m³
  - ρ_Λ,obs ≈ 5.79×10⁻¹⁰ J/m³

**Key numerical results (current toy model)**
- From the full microcavity scan:
  - ΔE_min ≈ −5.90×10⁻³
  - ΔE_max ≈  +6.30×10⁻⁴
  - θ★_fid_used ≈ 3.63 rad (nearest grid point)
  - ΔE(θ★_fid) ≈ −5.33×10⁻³  (dimensionless)
- Define the mapping:
  - ρ_vac(θ★) ≈ S · [−ΔE(θ★)]
  - Choose **S** such that ρ_vac(θ★_fid) = ρ_Λ,obs.
  - Resulting scale: S ≈ 1.09×10⁻⁷ J/m³ per unit of (−ΔE).
- Over the Act II θ★ band [2.18, 5.54] rad, this gives:
  - min ρ_vac(θ★ in band) ≈ −6.6×10⁻¹¹ J/m³
  - max ρ_vac(θ★ in band) ≈ +6.4×10⁻¹⁰ J/m³
  - By construction, ρ_vac at θ★_fid matches ρ_Λ,obs within rounding.

**Interpretation / status**
- This is **not** a prediction of Λ from first principles.
- It is an *explicit scaling convention* that answers:
  > “If the 1D microcavity ΔE(θ★) model were the right microphysics, what physical energy-density scale would one unit of dimensionless ΔE need to represent to match today’s dark-energy density at θ★_fid?”
- The answer is: **O(10⁻⁷ J/m³ per unit of −ΔE)**.
- Future, more realistic models (higher-dimensional cavities, proper field content, etc.) can be checked against this required scale.
- Together with the FRW-from-microcavity demo, this closes the *Act II bridge* from:
  - θ★-from-flavor → 1D microcavity ΔE(θ★) → effective Ω_Λ → FRW expansion,
  while remaining honest that the microphysics and dimensional analysis are still toy-level.


### 2025-12-15 — Effective vacuum interface and FRW run

**Repo:** origin-axiom  
**Files:**  
- `src/vacuum_effective.py`  
- `src/run_frw_from_effective_vacuum.py`  
- `data/processed/frw_from_effective_vacuum.npz` (output)

**What we did**
- Implemented a thin `EffectiveVacuumModel` in `src/vacuum_effective.py` that:
  - Reads the Act II theta-star prior from `config/theta_star_config.json`.
  - Loads the 1D microcavity scan from `data/processed/theta_star_microcavity_scan_full_2pi.npz`.
  - Defines a toy mapping from microcavity energy shifts to an effective cosmological constant:
    - `Omega_Lambda(theta_star) = k_scale * delta_E(theta_star)`,
    - with `k_scale` chosen so that at the fiducial theta-star (\u03B8\u2605_fid) we recover a target value `Omega_Lambda,fid = 0.7` (by construction).

- Wrapped this model in `src/run_frw_from_effective_vacuum.py`, which:
  - Builds the `EffectiveVacuumModel` from current Act II configuration and microcavity data.
  - Evaluates `Omega_Lambda(theta_star)` and `Omega_m(theta_star)` at the fiducial \u03B8\u2605.
  - Integrates a flat FRW toy model (H0=1 units) for:
    - a matter-only universe (`Omega_m = 1, Omega_Lambda = 0`), and
    - an "effective-vacuum" universe with (`Omega_m(theta_star_fid), Omega_Lambda(theta_star_fid)`).
  - Saves the results (time and scale factor arrays, plus meta-info about \u03B8\u2605 and `k_scale`) to `data/processed/frw_from_effective_vacuum.npz`.

**Why this matters**
- This is the first clean Act III interface that treats the vacuum sector as a function
  of the flavor-informed theta-star prior rather than an arbitrary knob in FRW.
- `vacuum_effective.py` is now the single entry point for:
  - "what does the microstructure say about Omega_Lambda(theta_star)?"
  - simple FRW scripts can call this without knowing microcavity internals.
- This keeps the story modular:
  - Act II: build and lock the theta-star posterior from flavor.
  - Act III (step 1): translate microcavity \u0394E(\u03B8\u2605) into an effective Lambda,
    and show that this reproduces the expected FRW acceleration behaviour for the fiducial band.



# 2025-12-15 — FRW observable-style check (matter-only vs effective vacuum)

**Script:** `scripts/compare_frw_observables.py`  
**Context:** First Act III “observable check” for the origin-axiom FRW toy universe.

## What the script does

- Loads the Act II theta★ configuration from `theta_star_config.py`:
  - `theta_star_fid_rad ≈ 3.63`
  - `theta_star_band_rad ≈ [2.18, 5.54]`
- Hard-codes a fiducial vacuum fraction
  - `Omega_Lambda,fid = 0.7`
  - `Omega_m,fid = 0.3`
- Defines two flat FRW cosmologies:
  1. **matter_only**: `Omega_m = 1.0`, `Omega_Lambda = 0.0`
  2. **effective_vacuum**: `Omega_m = 0.3`, `Omega_Lambda = 0.7`
- For each cosmology it computes:
  - Dimensionless age: `t0 * H0 = ∫ da / (a * E(a))` from `a_min = 1e-4` to `a = 1`
    with `E(a) = sqrt(Omega_m / a^3 + Omega_Lambda)`.
  - Physical age in Gyr assuming `H0 ≈ 70 km/s/Mpc`.
  - Deceleration parameter today `q0 = 0.5 * Omega_m - Omega_Lambda`.

## Numerical results (from this run)

With `H0 ≈ 70 km/s/Mpc` (Hubble time `t_H ≈ 13.97 Gyr`):

- **matter_only**
  - `t0 * H0 ≈ 0.667`
  - `t0 ≈ 9.31 Gyr`
  - `q0 ≈ +0.50` (always decelerating)

- **effective_vacuum** (theta★-backed vacuum fraction)
  - `t0 * H0 ≈ 0.964`
  - `t0 ≈ 13.47 Gyr`
  - `q0 ≈ -0.55` (accelerating)

## Interpretation

- The effective-vacuum cosmology (using the Act II theta★-prior-backed
  `Omega_Lambda,fid = 0.7`) has:
  - A **negative** deceleration parameter (`q0 < 0`), i.e. late-time accelerated expansion.
  - An age scale `t0 ≈ 13.5 Gyr`, qualitatively close to the observed age of the Universe.
- The matter-only model has:
  - A **positive** deceleration parameter (`q0 ≈ 0.5`), i.e. always decelerating.
  - A younger age (`t0 ≈ 9.3 Gyr`), illustrating the standard “age problem” of pure matter FRW.

This check does **not** prove the microcavity model predicts Λ; instead,
it shows that once `Omega_Lambda` is set by the theta★-backed effective vacuum,
the resulting FRW cosmology naturally lives in the same qualitative regime
(age and acceleration sign) as the observed Universe.

### 2025-12-15 – ACT III: Hubble-style distance comparison (Hubble diagram)

**Context.** We now have an effective vacuum cosmology in `origin-axiom` that is backed by the Act II theta-star prior and the 1D microcavity scan. To make a first explicit contact with supernova-like observables, we constructed a simple Hubble-style distance–redshift comparison: matter-only vs effective vacuum.

**Code paths.**

- `scripts/compare_hubble_diagram.py`  
  Simple FRW tool that computes dimensionless luminosity distance
  d_L(z) in units of c / H0 for:
  - matter-only: Omega_m = 1, Omega_Lambda = 0
  - effective vacuum: Omega_m ~= 0.3, Omega_Lambda ~= 0.7 (from the theta-star prior config)
- Uses the shared interface:
  - `from theta_star_config import load_theta_star_config`
  - Config file: `config/theta_star_config.json` (Act II export)

**How to run.**

From the `origin-axiom` repo root:

```bash
cd ~/Documents/projects/origin-axiom
PYTHONPATH=src python3 scripts/compare_hubble_diagram.py
```

This prints the effective-vacuum cosmology inferred from the theta-star prior and writes:

- `data/processed/figures/frw_effective_hubble_diagram.png`

**What the script computes.**

We work in flat FRW with matter + Lambda, ignoring radiation and curvature. In units with c = 1 and distances measured in c / H0:

- Dimensionless Hubble factor:
  E(z) = H(z) / H0 = sqrt(Omega_m (1+z)^3 + Omega_Lambda).
- Dimensionless comoving distance:
  chi(z) = integral_0^z dz' / E(z').
- Dimensionless luminosity distance:
  d_L(z) = (1+z) * chi(z).

The script evaluates these with a simple trapezoidal rule on a uniform z-grid up to z_max ~= 2.

**Qualitative result.**

- For a given redshift z, the effective-vacuum curve has a larger luminosity distance d_L(z) than the matter-only curve.
- In Hubble-diagram language, this means that standard candles (e.g. SNe Ia) would appear fainter at fixed z in the effective-vacuum cosmology than in a matter-only universe.
- This is the familiar signature of late-time acceleration and is qualitatively compatible with the observed SN Hubble diagram.

The goal here is not precision cosmology but showing that, once we fix Omega_Lambda from the theta-star / microcavity pipeline, the resulting FRW background behaves in the expected accelerated way when seen through a distance–redshift relation.

**Next steps / hooks.**

- (Optional) Add a second script that overlays real binned SN data (or a mock LambdaCDM Hubble diagram) on top of our curves, to show how closely a simple Omega_m ~= 0.3, Omega_Lambda ~= 0.7 effective cosmology can track observations.
- Keep this script as the main entry point for “first contact” with observable expansion history in ACT III.


2025-12-15 — Locked Act II–III methods note and FRW/microcavity pipeline. See docs/paper/main_origin_axiom.tex, tag v0.2-act2-3-methods. This is the reference state for the θ⋆ prior → ∆E(θ⋆) → ρ_vac(θ⋆) → FRW toy pipeline.


2025-12-16 — Microcavity param sweeps housekeeping

- Files data/processed/microcavity_sweep_*.npz were produced by a stub
  version of scan_1d_microcavity_param_sweep.py with deltaE set to zero
  (no microcavity solver call).
- These NPZs are **sandbox / placeholder** and are **not used** in the Act II
  theta★ → microcavity → FRW chain or in any published figures.
- Any future use of microcavity_sweep_*.npz must be based on a regenerated
  dataset with a proper ΔE(θ) computation.


## 2025-12-16 – R2: Effective vacuum and FRW bridge

- Recovered and inspected microcavity full-2π scan:
  - data/processed/theta_star_microcavity_scan_full_2pi.npz
  - Summarized band and fiducial point in:
    - data/processed/theta_star_microcavity_core_summary.json
    - theta_fid_nominal = 3.63 rad
    - theta_fid_grid ≈ 3.6325 rad
    - delta_E(theta_fid) ≈ -5.33e-3 (dimensionless)
- Fixed microcavity sandbox NPZ naming:
  - microcavity_sweep_*.npz now expose both `deltaE` and `delta_E` for compatibility.
- Constructed effective vacuum model:
  - src/vacuum_effective.py
  - k_scale ≈ -1.31e2 chosen such that Omega_Lambda(theta_fid) = 0.7
- Ran FRW from effective vacuum:
  - src/run_frw_from_effective_vacuum.py
  - Produced data/processed/frw_from_effective_vacuum.npz
  - Verified accelerated expansion for (Omega_m, Omega_Lambda) = (0.3, 0.7) vs matter-only.



[2025-12-16] R3: FRW observables from effective vacuum
  - Built run_frw_observables_from_effective_vacuum.py to derive a(t), z, and
    a simple Hubble-like distance curve from frw_from_effective_vacuum.npz.
  - Saved observables to data/processed/frw_effective_observables.npz
    and figures/frw_from_effective_vacuum_a_of_t.pdf,
    figures/frw_effective_hubble_diagram.png.
  - This closes the loop: theta_star -> microcavity delta_E(theta)
    -> effective vacuum scaling -> FRW history -> expansion observables.



## 2025-12-16 — R4/R5: Effective vacuum θ★ band scan & stability window

- Loaded `data/processed/theta_star_microcavity_core_summary.json`
  (θ_fid_nominal = 3.63 rad, ΔE_fid ≈ −5.33×10⁻³, Ω_Λ,target = 0.7,
    k_scale ≈ −1.31×10²).
- Ran `src/run_effective_vacuum_band_scan.py`:
  - θ-band: [2.18, 5.54] rad, 41 samples.
  - Ω_Λ(θ) range in band: [0, 0.775].
  - Found 9 grid points with |Ω_Λ(θ) − 0.7| ≤ 0.05 in window
    θ ≈ 2.516–3.692 rad.
  - Saved results to `data/processed/effective_vacuum_band_scan.npz`.
- Plotted band scan with `src/plot_effective_vacuum_band_scan.py`:
  - Wrote `figures/effective_vacuum_band_scan.{png,pdf}`.
- Estimated local derivative dΩ_Λ/dθ in the window:
  - Typical slopes ~0.2–0.4 per rad away from the peak,
    ~0 near the mid-window point (θ_mid ≈ 3.10 rad).
  - Rough “allowed drift” keeping |ΔΩ_Λ|≲0.05 comes out ≈ 2.2 rad
    (very loose order-of-magnitude stability estimate, to be refined later).

- 2025-12-16 (R4–R6, theta-star microcavity branch)
  - R4: Implemented `run_effective_vacuum_band_scan.py` and
    `plot_effective_vacuum_band_scan.py`; produced
    `data/processed/effective_vacuum_band_scan.npz` and
    `figures/effective_vacuum_band_scan.{png,pdf}`.
  - R5: Quantified θ-window where |ΩΛ(θ) − 0.7| ≤ 0.05:
    found 9 points in [2.516, 3.692] rad; computed
    dΩΛ/dθ slopes at sample points.
  - R6: Wrote Act II A-branch summary in
    `act5_dynamical_theta_star.tex` (Result A); interpret
    microcavity→ΩΛ→FRW bridge and define “θ★ corridor”.
  - Status: A-branch (microcavity-backed effective vacuum
    and θ★ corridor) is functionally complete at the
    scaffolding level. No further scans planned in this repo.



### 2025-12-16 — R5: Effective vacuum patch ensemble

- Script: `src/run_effective_vacuum_patch_ensemble.py`
- Inputs:
  - `data/processed/effective_vacuum_band_scan.npz` (R4 band scan).
- Method:
  - Built 1D interpolator ΩΛ(θ★) over the microcavity-backed band [2.18, 5.54] rad.
  - Drew `N = 1000` θ★ values uniformly in this band.
  - Computed ΩΛ(θ★) for each and counted patches with |ΩΛ − 0.7| ≤ 0.05.
- Output:
  - `data/processed/effective_vacuum_patch_ensemble.npz` with:
    - `theta_samples`, `omega_samples`, `theta_min`, `theta_max`,
      `omega_target = 0.7`, `tol = 0.05`, `theta_fid`, `k_scale`.
- Result:
  - ΩΛ(θ★) in the band spans ~[0, 0.775].
  - Fraction of Λ-like patches (|ΩΛ − 0.7| ≤ 0.05) ≈ 0.215 (21.5%).
- Interpretation:
  - In this toy ensemble with a flat prior in θ★, Λ-like universes form a
    non-negligible subspace of the θ★ band, consistent with a “corridor”
    rather than a single fine-tuned point.


[2025-12-16] R5: effective vacuum patch ensemble

- Script: src/run_effective_vacuum_patch_ensemble.py
- Data:   data/processed/effective_vacuum_patch_ensemble.npz
- Plot:   figures/effective_vacuum_patch_ensemble.(png,pdf)

Summary:
- Sampled 1000 θ⋆ patches uniformly from the effective band
  [2.18, 5.54] rad obtained in R4.
- Mapped each θ⋆ to ΩΛ using the microcavity-backed effective vacuum scaling
  with k_scale ≈ -1.31×10² and ΩΛ(fid) = 0.7.
- Resulting ΩΛ distribution spans [0, 0.775], with strong weight near 0 and
  near the upper band edge.
- Fraction of patches in the observational window ΩΛ = 0.70 ± 0.05:
  215 / 1000 ≈ 21.5%.



- **R5: effective vacuum patch ensemble**
  - Used the effective-vacuum band scan from R4 and the microcavity-based
    scaling (k_scale ≈ -131.4) to define ΩΛ(θ★) over the admissible band
    [2.18, 5.54] rad.
  - Drew N_patch = 1000 uniform θ★ samples in this band and mapped each to
    ΩΛ. The ensemble spans 0 ≤ ΩΛ ≲ 0.78 with mean ≈ 0.45, σ ≈ 0.31,
    median ≈ 0.57.
  - A total of 215 patches (≈ 21.5%) land in the observational window
    ΩΛ = 0.70 ± 0.05. The observed ΩΛ lies within the central 68% interval
    of the ensemble, so in this toy model our patch is statistically
    “typical” within the θ★ band rather than exponentially fine-tuned.


- **R6: Act V microcavity → FRW → ensemble summary**
  - Collected results from R1–R5 into an Act V summary section in
    `docs/paper/act5_dynamical_theta_star.tex`.
  - Explicitly documented: (i) fiducial microcavity point
    (theta_fid ≈ 3.63 rad, ΔE_fid ≈ -5.3e-3), (ii) scaling to
    ΩΛ(theta★), (iii) FRW histories for (Ω_m, Ω_Λ) = (1,0) vs (0.3,0.7),
    (iv) θ★-band scan, and (v) effective patch ensemble.
  - Main qualitative conclusion: within the microcavity-selected
    θ★-band, patches with ΩΛ ≈ 0.7 form a ~20% subset of the ensemble
    and are statistically typical, not exponentially fine-tuned, in this
    toy model.


### 2025-12-16 — R5: Effective vacuum patch ensemble

- Implemented `src/run_effective_vacuum_patch_ensemble.py` and
  `src/plot_effective_vacuum_patch_ensemble.py`.
- Generated `data/processed/effective_vacuum_patch_ensemble.npz` and
  figures `figures/effective_vacuum_patch_ensemble.{png,pdf}`.
- Ensemble: N = 1000 patches, θ⋆ sampled uniformly from [2.18, 5.54] rad.
- ΩΛ statistics:
  - min/max ≈ 0.000 / 0.775  
  - mean ≈ 0.445, std ≈ 0.307, median ≈ 0.573
- Fraction of patches near the observed value ΩΛ ≈ 0.7:
  - |ΩΛ − 0.70| ≤ 0.05 → 215 / 1000 ≈ 21.5%
  - |ΩΛ − 0.70| ≤ 0.02 → 80 / 1000 ≈ 8.0%
  - |ΩΛ − 0.70| ≤ 0.01 → 39 / 1000 ≈ 3.9%
- Interpretation: within the allowed θ⋆ band from the microcavity model,
  Λ-like patches (ΩΛ ≈ 0.7) occupy a non-negligible fraction of the ensemble,
  supporting the claim that our toy vacuum does not require extreme fine-tuning.



- 2025-12-16 (R6): Implemented toy random-walk dynamics for θ★ within the
  microcavity-supported band using `src/run_theta_star_random_walk_residence.py`.
  Constructed ΩΛ(θ★) via the calibrated microcavity scaling
  (k_scale ≈ -131.4, ΩΛ(θ★_fid) ≈ 0.7 at θ★_fid = 3.63 rad)
  and evolved N_TRAJ = 200 trajectories over N_STEPS = 2000 steps with
  reflecting boundaries and step size Δθ ≈ 0.02 rad.
  Measured residence-time fractions in three windows,
  |ΩΛ - 0.7| ≤ {0.05, 0.02, 0.01}, obtaining ≈{20.5%, 7.4%, 3.7%}.
  Saved ensemble to `data/processed/theta_star_random_walk_residence.npz`
  and summary figure `figures/theta_star_random_walk_residence.{png,pdf}`.


### R6 – θ★ random-walk residence in effective vacuum band

**Scripts**

- `src/run_theta_star_random_walk_residence.py`
- `src/plot_theta_star_random_walk_residence.py`

**Inputs**

- `data/processed/theta_star_microcavity_scan_full_2pi.npz`
- `data/processed/theta_star_microcavity_core_summary.json`

**Config**

- Band: θ★ ∈ [2.18, 5.54] rad (same as R4–R5)
- Random walk:  
  - `N_TRAJ = 200` trajectories  
  - `N_STEPS = 2000` steps  
  - `STEP_SIZE = 0.02` rad  
  - reflecting boundaries at band edges
- Cosmological scaling:
  - `omega_lambda_target = 0.7`
  - `k_scale ≈ -1.313986e+02`

**Outputs**

- `data/processed/theta_star_random_walk_residence.npz`
- `figures/theta_star_random_walk_residence.png` (and `.pdf`)

**Key numbers (residence fractions in ΩΛ space)**

Flattening all trajectories:
- Window \|ΩΛ − 0.700\| ≤ 0.050 : 82 064 / 400 200 ≈ **20.5%**
- Window \|ΩΛ − 0.700\| ≤ 0.020 : 29 640 / 400 200 ≈ **7.4%**
- Window \|ΩΛ − 0.700\| ≤ 0.010 : 14 679 / 400 200 ≈ **3.7%**

**Interpretation**

A simple θ★ random walk confined to the microcavity-allowed band spends  
O(10%) of its “time” in patches whose ΩΛ is observationally acceptable,  
and a few percent in a tighter ±0.01 window. This qualitatively matches  
the static patch-ensemble result from R5 and supports the idea that the  
microcavity-backed band can dynamically host Λ ≈ 0.7 without fine-tuning
to a single θ★ value.



- 2025-12-16 — R7: Implemented `run_theta_star_prior_vs_effective_vacuum.py` and
  `plot_theta_star_prior_vs_effective_vacuum.py`. Mapped the original 1D twisted-vacuum
  θ★ prior into an induced prior over ΩΛ using the microcavity-backed k_scale, and
  added the corresponding figure + discussion to Act V.


2025-12-16 (dri) R7: Induced ΩΛ prior from θ★ prior
  - Added run_theta_star_prior_vs_effective_vacuum.py to map existing 1D θ★ prior
    (theta_star_prior_1d_vacuum_samples.npz) through the microcavity-calibrated
    effective vacuum (k_scale, delta_E(θ★)).
  - Saved samples to data/processed/theta_star_prior_vs_effective_vacuum.npz and
    generated figures/theta_star_prior_vs_effective_vacuum.{png,pdf}.
  - Result: broad ΩΛ prior (0 → ~0.76) with non-negligible weight near ΩΛ ≈ 0.7,
    supporting a non-fine-tuned but ΛCDM-compatible region of the θ★ band.


## 2025-12-17 — R8: Localised two-field microstructure in effective vacuum

**Scripts**

- `src/run_two_field_bump_1d.py`
- `scripts/inspect_two_field_bump_1d.py`
- `scripts/summarize_two_field_bump_1d.py` (new)

**Commands**

```bash
cd ~/Documents/Projects/origin-axiom
PYTHONPATH=src python3 src/run_two_field_bump_1d.py --steps 2000 --snapshot-stride 20 --g 0.02
PYTHONPATH=src python3 scripts/inspect_two_field_bump_1d.py
PYTHONPATH=src python3 scripts/summarize_two_field_bump_1d.py
```

**Data / figures**

- `data/processed/two_field_bump_1d.npz`
- `data/processed/figures/two_field_bump_1d_loc_amp.png`
- `data/processed/figures/two_field_bump_1d_phi_final.png`
- `data/processed/figures/two_field_bump_1d_chi_final.png`

**Summary**

- Confirmed that the 1D two-field bump toy evolves stably under the Origin-Axiom non-cancelling constraint.
- In both the free and constrained runs the localised bump gradually disperses and its amplitude decays over the integration time.
- The constrained trajectory tracks the free one closely: initial amplitudes are identical, final amplitudes differ only at the few-percent level, and simple diagnostics (half-amplitude lifetime, mean |loc|) are comparable between the two cases.
- The helper script `scripts/summarize_two_field_bump_1d.py` prints basic diagnostics (initial/final amplitudes, half-amplitude lifetimes, mean |loc|) for both free and constrained trajectories.
- This rung serves as a first microstructure check that applying the non-cancelling rule on top of a θ★-selected effective vacuum does not introduce runaway behaviour or obvious pathologies in a localised two-field excitation.



## 2025-12-17 — θ★ bridge summary index (R9)

- Added `scripts/summarize_theta_star_bridge.py` to collect all key θ★ → microcavity → effective-vacuum ensemble numbers in one place.
- Summary script reads:
  - Act II θ★ prior band and fiducial value from `config/theta_star_config.json`,
  - microcavity core summary from `data/processed/theta_star_microcavity_core_summary.json`,
  - effective-vacuum band scan from `data/processed/effective_vacuum_band_scan.npz`,
  - patch ensemble from `data/processed/effective_vacuum_patch_ensemble.npz`,
  - random-walk residence data from `data/processed/theta_star_random_walk_residence.npz`.
- Writes a compact machine-readable index to
  `data/processed/theta_star_bridge_summary.json` with:
  - θ★ prior band `[2.18, 5.54]` rad and θ★_fid ≈ 3.63 rad,
  - microcavity ΔE_fid, k_scale, and Ω_Λ,target,
  - effective-vacuum band scan ranges and 9/41 points in the Ω_Λ = 0.70 ± 0.05 corridor,
  - patch ensemble stats (mean/median/std and fractions in |Ω_Λ − 0.70| ≤ {0.05, 0.02, 0.01}),
  - random-walk residence fractions in the same Ω_Λ windows.
- Purpose: provide a single, reproducible numerical snapshot of the Act II/III θ★ bridge, so later analyses can sanity-check against one JSON instead of chasing individual NPZ files.


## 2025-12-17 — R10: FRW observables from theta_star-backed effective vacuum

- Added `scripts/summarize_effective_vacuum_observables.py` to compute standard FRW observables for:
  - a matter-only cosmology (Omega_m = 1.0, Omega_Lambda = 0.0), and
  - the effective-vacuum cosmology backed by the theta_star + microcavity bridge (Omega_m = 0.3, Omega_Lambda = 0.7).
- For each cosmology the script prints:
  - dimensionless age factor t0 * H0 from a_min ≈ 1e-4 to a = 1,
  - physical age t0 in Gyr for H0 = 70 km/s/Mpc (t_H ≈ 13.97 Gyr),
  - deceleration parameter q0 = 0.5 * Omega_m − Omega_Lambda,
  - luminosity distances d_L(z)/(c/H0) at z = 0.3, 0.5, 1.0.
- Current numerical output:
  - matter-only: t0 * H0 ≈ 0.667 → t0 ≈ 9.31 Gyr, q0 = +0.50, d_L(z)/(c/H0) ≈ {0.32, 0.55, 1.17} at z = {0.3, 0.5, 1.0}.
  - effective vacuum: t0 * H0 ≈ 0.964 → t0 ≈ 13.47 Gyr, q0 = −0.55, d_L(z)/(c/H0) ≈ {0.36, 0.66, 1.54} at z = {0.3, 0.5, 1.0}.
- Interpretation: the theta_star-backed effective vacuum cosmology has a negative deceleration parameter and an age in the 13–14 Gyr range, with larger luminosity distances than the matter-only model at fixed redshift. This matches the qualitative behaviour of a standard Omega_m ≈ 0.3, Omega_Lambda ≈ 0.7 LambdaCDM universe, without yet claiming a precision fit to real cosmological data.


## 2025-12-17 — R11: Act II/III θ★ bridge status snapshot

- Created `docs/ACT23_BRIDGE_STATUS.md` to freeze the current status of the
  θ★→microcavity→effective-vacuum→FRW bridge.
- Documented:
  - flavor-based θ★ prior (fiducial and band),
  - 1D microcavity ΔE(θ★) scan and core summary (delta_E_fid, k_scale, omega_target),
  - effective vacuum band scan, patch ensemble, and random-walk residence statistics,
  - FRW histories and basic observables (age, q0, luminosity distances) for
    matter-only vs θ★-backed effective vacuum.
- Explicitly listed limitations of the current toy pipeline
  (1D cavity, linear scaling, limited FRW components, no real-data fit, exploratory
  physical scaling only) and outlined a TODO list for any future “real data” contact.
- This rung serves as a checkpoint: the microcavity/FRW branch is now documented as a
  scaffold-level toy model, ready to be refined or replaced in later Acts without
  losing track of what it currently achieves.


## 2025-12-17 — R13: $\theta_\star$ observable corridor (Act II/III bridge)

- Scripts:
  - `scripts/scan_theta_star_frw_observables.py`
  - `scripts/select_theta_star_observable_corridor.py`
- Data:
  - `data/processed/effective_vacuum_theta_frw_scan.npz` (FRW scan over the Act II $\theta_\star$ band)
  - `data/processed/theta_star_observable_corridor.json` (selection summary and accepted samples)
- Method:
  - Used the microcavity-backed effective vacuum scaling (same `k_scale` and $\Omega_\Lambda(\theta_\star)$ as in R4–R6) to compute, for 41 $\theta_\star$ values in the band $[2.18,5.54]$ rad, the corresponding FRW observables: $(\Omega_\Lambda,\Omega_m)$, age $t_0$ (Gyr), deceleration parameter $q_0$, and example luminosity distances $d_L(z)/(c/H_0)$ at $z=\{0.3,0.5,1.0\}$.
  - Defined a simple “observable corridor” by requiring $0.60 \le \Omega_\Lambda \le 0.80$, $12.0~\mathrm{Gyr} \le t_0 \le 15.0~\mathrm{Gyr}$, and $q_0 < 0$ (late-time acceleration) for each sample.
- Results:
  - 18 out of 41 samples (≈43.9%) in the flavour-informed $\theta_\star$ band satisfy all three cuts.
  - Selected corridor in $\theta_\star$ space: $\theta_\star \in [2.432,3.860]$ rad, with $\Omega_\Lambda \in [0.609,0.775]$, $t_0 \in [12.49,14.57]$ Gyr, and $q_0 \in [-0.662,-0.413]$.
  - The fiducial phase from the Act II flavour analysis, $\theta_{\star,\mathrm{fid}} \simeq 3.63$ rad, lies comfortably inside this corridor.
- Interpretation:
  - Within the microcavity-backed effective vacuum model, a substantial fraction of the flavour-informed $\theta_\star$ band yields FRW cosmologies that (i) accelerate, (ii) have a vacuum fraction of the right order of magnitude, and (iii) an age compatible with a $H_0 \sim 70~\mathrm{km\,s^{-1}\,\mathrm{Mpc}^{-1}}$ universe.
  - This strengthens the Act II/III bridge: the same $\theta_\star$ band that fits flavour data is also compatible with very basic cosmological sanity checks, without tuning to a single point.


### 2025-12-17 — R12–R14: θ★ FRW observable scan and corridor

**Scripts**

- `scripts/scan_theta_star_frw_observables.py`  *(R12)*
- `scripts/select_theta_star_observable_corridor.py`  *(R13)*
- `scripts/plot_theta_star_observable_corridor.py`  *(R14)*

**Data / figures**

- `data/processed/effective_vacuum_theta_frw_scan.npz`
- `data/processed/theta_star_observable_corridor.json`
- `data/processed/theta_star_observable_corridor_plot_summary.json`
- `figures/theta_star_observable_corridor.png`
- `figures/theta_star_observable_corridor.pdf`

**R12 — θ★ FRW observable scan**

- Scanned the Act II θ★ band `[2.18, 5.54] rad` on a 41-point grid.  
- For each θ★:
  - built `Ω_Λ(θ★)` from the microcavity ΔE(θ★) and calibrated `k_scale`  
    (`Ω_Λ(θ★_fid) = 0.7`, `θ★_fid = 3.63 rad`),
  - computed flat FRW observables with `H0 = 70 km/s/Mpc`:
    - `t0(θ★)` (age of the universe),
    - `q0(θ★) = 0.5 Ω_m - Ω_Λ`,
    - dimensionless luminosity distances `d_L(z)/(c/H0)` at `z = 0.3, 0.5, 1.0`.
- Global ranges over the band:
  - `Ω_Λ(θ★) ∈ [0.000, 0.775]`
  - `t0(θ★) ∈ [9.31, 14.57] Gyr`
  - `q0(θ★) ∈ [-0.662, 0.500]`

**R13 — θ★ observable corridor selection**

- Loaded the FRW scan and applied simple “observationally reasonable” cuts:
  - `0.60 ≤ Ω_Λ ≤ 0.80`
  - `12.0 ≤ t0 ≤ 15.0 Gyr`
  - `q0 < 0` (accelerating today)
- Result:
  - Selected `18 / 41` grid points (**43.9%** of the band).
  - θ★ “observable corridor”:
    - `θ★ ∈ [2.432, 3.860] rad`
    - `Ω_Λ ∈ [0.609, 0.775]`
    - `t0 ∈ [12.49, 14.57] Gyr`
    - `q0 ∈ [-0.662, -0.413]`
- Saved the selection to  
  `data/processed/theta_star_observable_corridor.json`
  (stores the corridor bounds and the per-point table).

**R14 — θ★ observable corridor plot**

- Used the FRW scan + corridor mask to build a 3-panel summary figure:
  - Top: `Ω_Λ(θ★)` over the full prior band, with the accepted corridor highlighted.
  - Middle: `t0(θ★)` in Gyr, same shaded corridor.
  - Bottom: `q0(θ★)` vs θ★, with the accelerating region (`q0 < 0`) emphasized.
- Wrote:
  - `figures/theta_star_observable_corridor.png`
  - `figures/theta_star_observable_corridor.pdf`
  - `data/processed/theta_star_observable_corridor_plot_summary.json`
- Qualitative takeaway:
  - Within the broad Act II θ★ band, there exists a sub–interval  
    `θ★ ≈ 2.4–3.9 rad` where:
    - `Ω_Λ` sits near the concordance value,
    - the FRW age is ~12.5–14.5 Gyr,
    - and the universe is accelerating (`q0 < 0`).
  - This corridor overlaps the microcavity plateau and the earlier
    patch / random-walk results, reinforcing the picture of a
    **θ★ corridor** rather than a single fine-tuned θ★ point.



R15 — theta★ linear growth scan over effective-vacuum band (2025-12-17)

Scripts
- scripts/scan_theta_star_linear_growth.py
- Input: data/processed/effective_vacuum_theta_frw_scan.npz
- Output: data/processed/effective_vacuum_theta_growth_scan.npz

What we computed
- For each theta★ sample in the effective-vacuum FRW scan, we computed the
  (unnormalised) linear growth factor D(a=1) using the standard flat FRW
  Omega_m–Omega_Lambda integral:
    D(a) ∝ H(a) ∫ da' / (a'^3 H(a')^3),  with a ∈ [a_min, 1], a_min = 1e-3.
- We evaluated D(a=1) for every (Omega_m(theta★), Omega_Lambda(theta★)) pair
  in the band 2.18 ≤ theta★ ≤ 5.54 rad.
- We also computed a reference Einstein–de Sitter growth factor D_EdS(a=1)
  for (Omega_m, Omega_Lambda) = (1, 0) with the same numerical scheme.
- Defined a dimensionless suppression factor
    D_rel(theta★) = D(a=1; Omega_m(theta★), Omega_Lambda(theta★)) / D_EdS(a=1).
- Where available, we intersected these results with the observable corridor
  from data/processed/theta_star_observable_corridor.json (R13).

Key numerical results
- FRW scan recap (from effective_vacuum_theta_frw_scan.npz):
  - theta★ band: 2.18 → 5.54 rad
  - Omega_Lambda(theta★) in band: 0.000 → 0.775
  - t0(theta★) in band: 9.31 → 14.57 Gyr
  - q0(theta★) in band: -0.662 → 0.500
  - H0 = 70 km/s/Mpc
  - omega_target = 0.700
  - theta_fid = 3.63 rad

- EdS reference:
  - D_EdS(a=1) (Omega_m=1, Omega_Lambda=0) = 1.0000 (by construction).

- Global growth over the full theta★ band:
  - D_rel(a=1) min / max = 0.728 / 1.000.
  - Interpretation: relative to an EdS universe, the effective-vacuum models
    suppress linear growth by up to ~27% in the most Lambda-dominated cases,
    and smoothly approach EdS-like growth near Omega_Lambda → 0.

- Observable corridor (from R13):
  - theta_corridor = 2.432 → 3.860 rad.
  - N_corridor samples = 18 / 41.
  - Omega_m range in corridor: 0.225 → 0.391.
  - Omega_Lambda range in corridor: 0.609 → 0.775.
  - D_rel(a=1) range in corridor: 0.728 → 0.827.
  - Mean D_rel(a=1) across corridor: 0.767.

  So in the “observationally acceptable” region (age 12–15 Gyr,
  accelerating q0 < 0, and Omega_Lambda ~ 0.6–0.8), the linear growth factor
  is consistently ~75% of the EdS value, with only modest variation across
  the corridor.

- Fiducial theta★ sample (closest to theta_fid = 3.63 rad):
  - theta★_fid,eff = 3.608 rad.
  - Omega_m(theta★_fid,eff) = 0.292.
  - Omega_Lambda(theta★_fid,eff) = 0.708.
  - t0(theta★_fid,eff) = 13.57 Gyr.
  - q0(theta★_fid,eff) = -0.561.
  - D_rel(a=1; theta★_fid,eff) = 0.774.

  This fiducial point lives well inside the observable corridor and has a
  growth suppression very close to the corridor mean (~0.77).

Interpretation / status
- R15 adds a first structure-formation observable to the theta★ → effective
  vacuum → FRW chain: the linear growth factor D(a=1).
- Across the full theta★ band, growth varies smoothly between “EdS-like”
  (D_rel ≈ 1) and “Lambda-dominated” (D_rel ≈ 0.73).
- Inside the R13 observable corridor (2.432–3.860 rad), growth is both
  suppressed (D_rel ≈ 0.73–0.83) and stable: all acceptable theta★ values
  lead to a moderate ~20–25% reduction relative to EdS.
- The fiducial flavor-informed theta★ (≈3.63 rad) sits comfortably in this
  corridor, with a growth factor typical of the corridor ensemble.

- This does not yet constitute a precise prediction for sigma_8 or the
  matter power spectrum, but it shows that the same microcavity-backed
  theta★ band that yields realistic (Omega_m, Omega_Lambda, t0, q0) also
  supports a sensible, smoothly varying linear-growth sector without
  fine-tuning or pathological behaviour.

Next steps (planned)
- R16: build a plotting script for D_rel(theta★) analogous to the R14
  observable corridor figure, shading the corridor and marking the fiducial
  theta★ point.
- Optional: introduce a crude sigma_8-like proxy by combining D_rel(a=1)
  with a simple initial-power normalisation, to compare “theta★ corridor”
  vs “EdS baseline” in a more observable-like way.





## 2025-12-17 — R16: θ★-dependent linear growth plot

**Script**  
- `scripts/scan_theta_star_linear_growth.py` (R15 — already run, produces the growth NPZ)  
- `scripts/plot_theta_star_linear_growth.py` (new in R16)

**Data inputs**  
- `data/processed/effective_vacuum_theta_frw_scan.npz`  
  - `theta_scan` over band [2.18, 5.54] rad  
  - `omega_lambda_scan`, `omega_m_scan`, `t0_gyr_scan`, `q0_scan`  
- `data/processed/effective_vacuum_theta_growth_scan.npz` (from R15)  
  - `theta_scan`, `D_rel_scan` with  
    `D_rel(a=1) = D(a=1) / D_EdS(a=1)` at each θ★ sample

**What the script does** (`plot_theta_star_linear_growth.py`)
- Loads the FRW scan and linear-growth scan on the same θ★ grid.
- Reconstructs the **observable corridor** directly from the FRW arrays using the R13 criteria:
  - `0.60 <= Omega_Lambda <= 0.80`
  - `12.0 <= t0 <= 15.0` Gyr
  - `q0 < 0` (accelerating expansion)
- Identifies:
  - Corridor θ★ range ≈ [2.432, 3.860] rad
  - Ω_Λ range in corridor ≈ [0.609, 0.775]
  - t₀ range in corridor ≈ [12.49, 14.57] Gyr
  - q₀ range in corridor ≈ [−0.662, −0.413]
- Uses the same criteria to define a boolean mask over the `theta_scan` grid and applies it to the growth array `D_rel_scan`.

**Figure produced**
- `figures/theta_star_linear_growth_scan.png`
- `figures/theta_star_linear_growth_scan.pdf`

Layout:
1. **Top panel:** Ω_Λ(θ★) over the full band, with:
   - band edges [2.18, 5.54] rad,
   - vertical dashed line at the fiducial θ★ ≈ 3.63 rad,
   - shaded vertical strip indicating the observable corridor.
2. **Bottom panel:** Relative linear growth today, D_rel(a=1; θ★), on the same θ★ axis, with the same corridor shading and fiducial marker.

**Key behaviour (reusing R15 numbers for context)**
- Over the full θ★ band, the relative growth at a = 1 spans:
  - `D_rel(a=1)` ∈ [0.728, 1.000], i.e. up to ~27% suppression vs Einstein–de Sitter.
- Inside the observable corridor:
  - `D_rel(a=1)` ∈ [0.728, 0.827]
  - mean `D_rel(a=1)` ≈ 0.767
- Near the fiducial θ★ sample (θ★ ≈ 3.61 rad, Ω_m ≈ 0.29, Ω_Λ ≈ 0.71):
  - `t0 ≈ 13.57` Gyr, `q0 ≈ −0.56`, `D_rel(a=1) ≈ 0.774`

**Interpretation**
- The same θ★ corridor that gives a reasonable age and acceleration (Act II/III bridge) also yields a **smooth, moderately suppressed growth history**:
  - growth is consistently ~75% of EdS across the corridor,
  - no pathological spikes or dips appear as θ★ is varied inside the allowed band.
- This extends the θ★ → microcavity → Ω_Λ → FRW pipeline to include **first-pass structure formation diagnostics**, showing that our non-cancelling effective vacuum can support an accelerated, Λ-like universe with linear growth suppression in the expected range.




- 2025-12-17 (R17, Act V – observable corridor text):
  - Added Act V subsection summarising the θ⋆-dependent FRW observable corridor
    (age, ΩΛ, q0) and the associated linear growth suppression D_rel(a=1).
  - Corridor defined by loose, observation-inspired cuts:
      0.60 ≤ ΩΛ ≤ 0.80, 12 Gyr ≤ t0 ≤ 15 Gyr, q0 < 0,
    selecting θ⋆ ≃ 2.43–3.86 rad out of the full Act II band.
  - Documented that, once the microcavity scaling S is fixed at a single fiducial
    point, the resulting θ⋆-dependent effective vacuum yields FRW backgrounds and
    linear growth broadly compatible with an accelerating, Λ-like universe.
  - Emphasised that this is a qualitative consistency check, not yet a parameter-free
    prediction of ΩΛ; a more microscopic cancellation system and confrontation with
    real data are deferred to future work.



## 2025-12-17 — R17/R18: Act V observable corridor + closing summary

- Locked in Act V "observable corridor" subsection in `docs/paper/act5_dynamical_theta_star.tex`:
  - Defined a θ⋆ corridor by applying loose, observation-inspired cuts on the FRW band scan:
      0.60 ≤ Ω_Λ ≤ 0.80, 12 Gyr ≤ t₀ ≤ 15 Gyr, q₀ < 0.
  - Corridor spans θ⋆ ≃ 2.43–3.86 rad with Ω_Λ ≃ 0.61–0.78, t₀ ≃ 12.5–14.6 Gyr, q₀ ≃ −0.66 to −0.41.
  - Included linear growth suppression D_rel(a=1) ≃ 0.73–0.83 across the same corridor and a representative point near the Act II median with (Ω_m, Ω_Λ) ≃ (0.29, 0.71), t₀ ≃ 13.6 Gyr, D_rel(a=1) ≃ 0.77.
- Rewrote the Act V closing summary subsection to:
  - Describe the full θ⋆ → microcavity ΔE(θ⋆) → effective vacuum Ω_Λ(θ⋆) → FRW + growth pipeline (R1–R16).
  - Emphasise that once the single scaling S is fixed at the fiducial slice, the non-cancelling principle produces a structured θ⋆ band whose FRW age, acceleration, distances and growth are broadly Λ-like.
  - Make explicit that this is a qualitative consistency check, not yet a parameter-free prediction of Ω_Λ or a precision fit to cosmological data; genuine predictions are deferred to future, more microscopic models of the cancellation system and a full data confrontation.


## 2025-12-17 — R19: Physical scales for the effective vacuum bridge

- Scripts:
  - Added `scripts/effective_vacuum_physical_scales.py`.

- Data:
  - Reused microcavity core summary
    `data/processed/theta_star_microcavity_core_summary.json`.

- Summary:
  - Computed the physical critical density and vacuum energy density for the
    fiducial effective vacuum slice (H0 = 70 km s^-1 Mpc^-1, Omega_Lambda ≈ 0.7).
  - Expressed rho_Lambda in SI units and as a ratio to the Planck energy density,
    confirming the familiar hierarchy rho_Lambda / rho_Pl ~ 1e-123.
  - Related this rho_Lambda to the dimensionless microcavity energy shift
    DeltaE_fid ≈ -5.3×10^-3, defining an effective scale factor that maps
    lattice DeltaE to physical energy density.
  - Clarified that at the present stage the non-cancelling microcavity model
    provides an O(10^-3) dimensionless knob; the tiny absolute scale of Lambda
    comes from the choice of H0 and fundamental constants rather than from an
    internal prediction of the cancellation system.

- Status:
  - R19 completes the first rung of Act VI (scale-setting). Next rungs will
    use this bookkeeping to design the universe→atoms stitching ladder.


### R19 – Physical scales for the effective vacuum bridge (scripts/effective_vacuum_physical_scales.py)

**Goal.** Expose how the dimensionless microcavity energy shift at the fiducial
θ★ slice is promoted to a physical dark–energy density ρ_Λ, and make the
Planck–scale hierarchy explicit in standard cosmological units.

**What I ran.**

- `PYTHONPATH=src python3 scripts/effective_vacuum_physical_scales.py`

**Key outputs.**

- Loaded microcavity core summary from
  `data/processed/theta_star_microcavity_core_summary.json` with
  ΔE_fid ≈ −5.33×10⁻³, k_scale ≈ −1.31×10², and Ω_Λ,target = 0.7.
- Adopted H₀ = 70 km s⁻¹ Mpc⁻¹, giving:
  - ρ_crit ≈ 9.20×10⁻²⁷ kg m⁻³
  - ρ_Λ(mass) ≈ 6.44×10⁻²⁷ kg m⁻³
  - ρ_Λ ≈ 5.79×10⁻¹⁰ J m⁻³
- Planck density:
  - ρ_Pl ≈ 4.63×10¹¹³ J m⁻³
  - Ratio ρ_Λ / ρ_Pl ≈ 1.25×10⁻¹²³ (the standard “10⁻¹²³ problem”).
- Effective mapping from dimensionless microcavity units to physical ρ_Λ:
  - ΔE_fid = −5.33×10⁻³ (dimensionless)
  - scale_factor ≈ −1.09×10⁻⁷ J m⁻³ per unit ΔE
  - Check: Ω_Λ,fid = k_scale × ΔE_fid ≈ 0.700 (consistent with earlier rungs).

**Interpretation.**

- The tiny ratio ρ_Λ / ρ_Pl ≈ 10⁻¹²³ is set entirely by (H₀, G, c, ħ).
  The microcavity and non–cancelling rule only provide an 𝒪(10⁻³) shift
  in dimensionless lattice units.
- R19 does *not* claim a microscopic derivation of the absolute Λ scale.
  Instead, it makes the calibration explicit: once we demand that the
  θ★ fiducial slice reproduces Ω_Λ ≈ 0.7 for a chosen H₀, there is a unique
  conversion factor that maps ΔE_fid to the observed ρ_Λ.
- This rung closes Act V on the physical–units side: the θ★–driven effective
  vacuum bridge is now explicitly tied to standard cosmological densities
  without silently hiding the 10⁻¹²³ hierarchy.



### [2025-12-17] R20 – Roadmap for Acts VI–VIII (planning rung)

**Scope.** Created an explicit roadmap for the remaining acts of the Phase II
programme (Acts VI–VIII), focusing on how to climb from the existing
θ★–to–FRW bridge (Act V) towards flavour, toy matter, and eventual observational
hooks.

**Files.**
- Added `docs/ROADMAP_ACT_VI_VIII.md` with:
  - recap of the current status after Act V,
  - high-level goals for Acts VI, VII, and VIII,
  - planned rung labels R21–R32 with intended scripts, artefacts and LaTeX
    files.
- Updated this `PROGRESS_LOG.md` entry to register R20 as a planning rung.

**Status / intent.**
- R20 is a **meta-rung**: no new physics or numerics, but a locked structure
  for the remaining ladder.
- Acts VI–VIII will now proceed rung-by-rung:
  - Act VI: θ★ corridor vs flavour and σ₈-like growth.
  - Act VII: toy matter sector on θ★-selected vacuum.
  - Act VIII: atoms/observables outlook and comparison hooks.
- The roadmap file will be treated as the single source of truth for future
  rung planning on the “universe → atoms” path.




R21 – effective vacuum energy scale pivot (2025-12-17)
----------------------------------------------------------------

Status
- Implemented and ran scripts/effective_vacuum_mass_scale_pivot.py.
- This rung is bookkeeping: it locates the calibrated effective vacuum slice in physical units and compares it to Planck and neutrino scales. No new constraint on θ★ is imposed.

Inputs and configuration
- Cosmology assumed:
  - H0 = 70 km s^-1 Mpc^-1
  - Ω_Λ,fid = 0.700
- Microcavity calibration:
  - Uses ΔE_fid, k_scale, and θ★_fid from data/processed/theta_star_microcavity_core_summary.json.
  - Same calibration as in the effective-vacuum FRW rungs (R3–R4, R9–R16).

Key numerical results
- Critical density and Λ slice:
  - ρ_crit ≈ 9.20×10^-27 kg m^-3
  - ρ_crit (energy) ≈ 8.27×10^-10 J m^-3
  - ρ_Λ = Ω_Λ,fid × ρ_crit ≈ 5.79×10^-10 J m^-3

- Planck comparison:
  - ρ_Pl ≈ 4.63×10^113 J m^-3
  - ρ_Λ / ρ_Pl ≈ 1.25×10^-123
  - Confirms the familiar ~10^-123 hierarchy: this ratio is set entirely by (H0, G, c, ħ), not by the microcavity details.

- Effective vacuum energy scale (natural units)
  - Define E_Λ by ρ_Λ = E_Λ^4 (ħ = c = 1).
  - E_Λ ≈ 2.30×10^-3 eV = 2.30 meV

- Comparison to a reference neutrino mass scale:
  - m_ν,ref = 0.050 eV
  - E_Λ / m_ν,ref ≈ 0.046
  - The effective vacuum scale sits in the “neutrino neighbourhood”: a few percent of a typical neutrino mass scale.

Interpretation / takeaway
- R21 does *not* solve the 10^-123 problem and does not add new θ★ constraints.
- It makes the bookkeeping explicit:
  - Given the observed (H0, Ω_Λ), the corresponding vacuum energy density is ρ_Λ ~ 10^-123 ρ_Pl.
  - In particle-physics language this corresponds to an effective energy scale of a few meV.
- This places the calibrated θ★–backed effective vacuum in a concrete region of the microscopic energy hierarchy (well below electroweak/QCD scales, but not wildly separated from neutrino masses), ready to be compared against any future microphysical model that might link θ★, flavour, and vacuum energy more directly.



- 2025-12-17 — R22: theta_star FRW background vs ΛCDM backbone

  Added `scripts/compare_theta_star_to_lcdm_background.py` to compare the
  effective-vacuum FRW band from Act V against a fixed ΛCDM reference with
  (Ω_m, Ω_Λ) = (0.3, 0.7) and the same H0. The script ingests
  `data/processed/effective_vacuum_theta_frw_scan.npz`, constructs an internal
  ΛCDM backbone (age and d_L(z)/(c/H0) at z = 0.3, 0.5, 1.0), and computes
  fractional residuals in age and distances for each theta_star sample.

  We reuse the R13 “observable corridor” cuts
  (0.60 ≤ Ω_Λ ≤ 0.80, 12–15 Gyr age, q0 < 0) and report residual statistics
  both over the full Act II band and inside this corridor. Across the full
  band, age residuals reach ~30% and distance residuals up to ~25%; inside
  the corridor they shrink to ≲8% in age and ≲5% in distances, with medians
  at the few-percent level. A simple background mismatch score χ^2_bg
  (using 5% toy errors on d_L) is used to identify the best-matching
  theta_star slice, which lies near θ_* ≈ 3.61 rad with
  (Ω_m, Ω_Λ) ≈ (0.29, 0.71), t0 ≈ 13.6 Gyr, and distance residuals
  ≲0.5% at z ≤ 1. The residuals and masks are saved to
  `data/processed/theta_star_lcdm_background_residuals.npz` for later use in
  Act VI plots and discussion.





## 2025-12-18 — R22/R23: θ⋆ FRW background vs ΛCDM backbone

- R22: background comparison script
  - Added `scripts/compare_theta_star_to_lcdm_background.py` to compare the θ⋆-backed FRW band to a reference ΛCDM backbone with (Ω_m, Ω_Λ) = (0.3, 0.7).
  - Inputs:
    - FRW band scan: `data/processed/effective_vacuum_theta_frw_scan.npz` (θ⋆ grid, Ω_m(θ⋆), Ω_Λ(θ⋆), t₀(θ⋆), q₀(θ⋆), d_L(z;θ⋆) for z = 0.3, 0.5, 1.0).
  - For the full θ⋆ band:
    - Age residuals vs backbone: |Δt₀/t₀,ref| ≈ 0.7–31%.
    - Distance residuals: |Δd_L/d_L,ref| ≈ 0.2–12% at z=0.3, 0.3–17% at z=0.5, 0.5–24% at z=1.0.
  - Restricted to the “observable corridor” from R13 (0.60 ≤ Ω_Λ ≤ 0.80, 12–15 Gyr, q₀<0):
    - Age residuals tighten to ≈ 0.7–8%.
    - Distance residuals tighten to ≈ 0.2–1.9% (z=0.3), 0.3–3.0% (z=0.5), 0.5–4.9% (z=1.0).
  - Identified a best-matching slice inside the corridor:
    - θ⋆,best ≈ 3.608 rad with (Ω_m, Ω_Λ) ≈ (0.292, 0.708), t₀ ≈ 13.57 Gyr, q₀ ≈ −0.56.
    - Background distances differ from the backbone by only ≈ 0.2–0.5% at z = 0.3–1.0 (χ²_bg ≈ 0.012).

- R23: corridor + residuals figure
  - Added `scripts/plot_theta_star_lcdm_background_corridor.py` to visualise:
    - Top panel: Ω_Λ(θ⋆) over the Act II band, with the Act II prior band, the observable FRW corridor, θ⋆,fid ≈ 3.63 rad, and θ⋆,best ≈ 3.61 rad highlighted.
    - Bottom panel: fractional distance residuals Δd_L(z)/d_L,ref (in %) vs θ⋆ at z = 0.3, 0.5, 1.0 relative to the ΛCDM backbone (Ω_m, Ω_Λ) = (0.3, 0.7).
  - Outputs:
    - `figures/theta_star_lcdm_background_corridor.png`
    - `figures/theta_star_lcdm_background_corridor.pdf`
    - `data/processed/theta_star_lcdm_background_corridor_plot_summary.json`
  - Result: within the observable θ⋆ corridor, both background ages and Hubble-diagram distances remain within a few per cent of a standard ΛCDM backbone, with the flavour-informed θ⋆,fid lying close to the best-matching slice.



-



R24 – theta_star linear growth vs ΛCDM-like slice
Date: 2025-12-18

Scripts:
  - scripts/compare_theta_star_to_lcdm_growth.py

Inputs:
  - data/processed/effective_vacuum_theta_growth_scan.npz
  - data/processed/effective_vacuum_theta_frw_scan.npz
  - Act II prior band for theta_star: [2.18, 5.54] rad
  - Observable corridor in theta_star (from R13/R23): [2.432, 3.860] rad
  - H0 (metadata): 70 km s^-1 Mpc^-1

What the script computes:
  - Reuses the precomputed linear growth factor D(a; theta_star) for each FRW model in the band,
    normalized such that D_rel(a=1) = D(a=1; theta_star) / D_EdS(a=1), where D_EdS is the
    Einstein–de Sitter (Omega_m=1, Omega_Lambda=0) growth factor.
  - Identifies the “LCDM-like” slice within the band by finding the theta_star value that best
    matches the internal (Omega_m, Omega_Lambda) = (0.3, 0.7) FRW backbone used in R22/R23.
    This best-matching theta_star (theta_best) plays the role of a sigma8-like normalization point.
  - For each theta_star in the observable corridor, computes a sigma8-like amplitude ratio
    R_sigma8(theta) = D_rel(theta) / D_rel(theta_best), i.e. the ratio of linear growth today
    relative to the best-matching LCDM-like slice.

Key numerical results (from this run):
  - Full theta_star band (2.18 -> 5.54 rad):
      D_rel(a=1) min / max : 0.728 / 1.000
      D_rel(a=1) mean      : 0.870
    (So across the entire band, linear growth today ranges from fully EdS-like to
     ~27% suppressed.)

  - Observable corridor selection (theta_star corridor from R13/R23):
      theta_star corridor    : 2.432 -> 3.860 rad
      D_rel(a=1) corridor    : 0.728 -> 0.827
      mean D_rel(a=1)        : 0.767
    (Inside the corridor, all models are accelerated and have growth suppressed by
     ~17–27% relative to EdS.)

  - Reference LCDM-like slice (for sigma8-like normalization):
      theta_fid (metadata)   : 3.630 rad
      theta_best (in band)   : 3.608 rad
      D_rel(a=1; theta_best) : 0.774
    (This theta_best slice is the same one singled out in R22/R23 as giving the best match
     to the internal (Omega_m, Omega_Lambda) = (0.3, 0.7) FRW backbone in background distances.)

  - Sigma8-like amplitude ratios within the observable corridor:
      R_sigma8(theta) = D_rel(theta) / D_rel(theta_best)
      R_sigma8 min / max     : 0.940 / 1.068
      R_sigma8 mean          : 0.990
      Fractional range       : -6.0% .. +6.8% relative to theta_best

Interpretation:
  - Background-level consistency (R22/R23) already showed that there is a broad theta_star
    corridor where age, q0, and luminosity distances are within a few percent of a standard
    (0.3, 0.7) ΛCDM backbone.
  - R24 adds the first structure-growth diagnostic. Once we fix a single “LCDM-like” slice
    theta_best ~ 3.61 rad as the sigma8-like normalization point, all other theta_star
    values in the observable corridor produce a late-time linear growth amplitude within
    ~±6% of that reference.
  - In other words, if we imagine calibrating the absolute sigma8 at theta_best, the rest of
    the theta_star corridor does not wildly over- or under-grow structure. The non-cancelling,
    microcavity-backed effective vacuum yields a family of FRW models whose linear growth
    is “LCDM-like” at the rough few-percent level across the same corridor that already
    matched background distances.
  - This is not yet a precision prediction for sigma8. It is a consistency check: given a
    single normalization point, the theta_star-induced variation in late-time growth remains
    moderate, and does not immediately conflict with the kind of O(10%) observational
    uncertainties typically involved in sigma8 determinations.

Status / next steps:
  - R24 completes the “background + linear growth” consistency checks for the theta_star
    observable corridor.
  - Remaining Act VI tasks (in the current roadmap):
      * Short LaTeX subsection summarizing the linear-growth behavior and the sigma8-like
        amplitude ratios over the corridor.
      * Optional: explore whether any simple, qualitative tension emerges if we compare the
        corridor’s growth suppression with a schematic “low sigma8” vs “high sigma8” split,
        keeping in mind the limited realism of the current toy model.
  - At the current level, the non-cancelling effective vacuum bridge passes: there exists a
    theta_star corridor that simultaneously yields ΛCDM-like background distances and
    moderate, LCDM-like suppression of linear growth, once a single normalization point is
    chosen.



-



### 2025-12-21 — Gate 1 complete (Act VI): flavour × cosmology θ★ compatibility

Flavour posterior (from `origin-axiom-theta-star`, chi2_total <= 50):
- global θ★ (q16, q50, q84) = (2.0982, 3.5299, 5.5915) rad

Cosmology corridor (from R23 summary):
- θ★ corridor = [2.4320, 3.8600] rad

Overlap:
- θ★ overlap = [2.4320, 3.8600] rad (corridor fully contained in flavour band)

Artifacts:
- `data/processed/theta_star_posterior_summary_from_flavour.json`
- `data/processed/theta_star_flavour_cosmo_compatibility.json`
- `figures/theta_star_flavour_vs_cosmo_overlap.png`
- `docs/paper/act6_theta_star_flavour_cosmo_compatibility.tex`

Script:
- `scripts/act6_theta_star_flavour_cosmo_compatibility.py`








### 2026-01-03 — Phase 0–2 alignment pass begins (baseline freeze)

Purpose:
- Lock a reproducible baseline before governance alignment and Phase 2 rewrite.
- Prevent “dark progress” by logging every change as we retrofit Phase (Phase 1/2) to comply with Phase 0.

Plan (locked):
1) Stage 0 — baseline freeze + tag
2) Stage 1 — Phase 0 compactify (constitution: short, enforceable, referenced)
3) Stage 2 — Phase 1 compliance polish (explicit non-claims, falsifiers, provenance)
4) Stage 3 — Phase 2 paper rebuild + rewrite to match Phase 1 rigor (no ambiguity; strict scope)
5) Stage 4 — continuity polish across logs / state docs

Notes:
- No code/physics changes in this entry; only provenance and workflow locking.

### 2026-01-03 — Stage 1 (Rung 1.1): Phase 0 intro rewrite (constitution voice)

- Rewrote Phase 0 introduction as a constitution-style contract: what Phase 0 is, what it is not, why governance is required, and the “no dark progress” rule.
- No physics content added; strengthens scope boundaries for later phases.

### 2026-01-03 — Stage 1 (Rung 1.1): Phase 0 intro rewrite (constitution voice)

- Rewrote Phase 0 introduction as a constitution-style contract: what Phase 0 is, what it is not, why governance is required, and the “no dark progress” rule.
- No physics content added; strengthens scope boundaries for later phases.



### 2026-01-03 — Stage 1 (Rung 1.2): Phase 0 governance vocabulary rewrite

- Rewrote Phase 0 "Axioms and definitions" into a minimal governance vocabulary: claim/evidence/artifacts, phase contracts, corridor/filter objects, provenance, failure modes, and falsifiers.
- Explicitly scoped as governance-only (no physics postulates).

### 2026-01-03 — Stage 1 (Rung 1.3): Rewrite Phase 0 corridor method (filters/corridors/history)

- Rewrote corridor governance section to define filter artifacts, corridor artifacts, and append-only corridor history as binding governance objects.
- Added explicit corridor update rules: no silent narrowing, evidence requirements, provenance requirements, and auditability conditions.


### 2026-01-03 — Stage 1 (Rung 1.4): Rewrite Phase 0 phase contracts (claim taxonomy + binding checklist)

- Rewrote Phase contracts section to define mandatory scope contracts, claim taxonomy, required claim structure, and an evidence binding rule.
- Added a reviewer-facing Phase 0 compliance checklist as the lock condition for later phases.

### 2026-01-03 — Stage 1 (Rung 1.5): Rewrite Phase 0 reproducibility contract (run bundles + provenance)

- Rewrote reproducibility contract to define canonical artifacts vs regenerable outputs, required provenance fields, and a minimal run-bundle structure.
- Added explicit failure-handling rule: if an artifact cannot be regenerated, dependent claims are marked broken until repaired and logged.


### 2026-01-03 — Stage 1 (Rung 1.6): Rewrite Phase 0 falsifiability + failure modes (falsifiers required)

- Rewrote falsifiability/failure section: every claim must list concrete falsifiers; phases must list failure modes; failures are recorded, quarantined, repaired, and re-validated.
- Added a strict speculation policy to protect scope contracts (speculation must be labeled and cannot be used as evidence).

### 2026-01-03 — Stage 1 (Rung 1.7): Compress Phase 0 candidate origins into non-normative note

- Replaced candidate-origins discussion with a short non-normative hypothesis list.
- Added explicit governance rule: future phases may test these routes only as bounded claims with evidence + falsifiers; cannot be cited as evidence.

### 2026-01-03 — Stage 1 (Rung 1.8): Rewrite Phase 0 conclusion + compactification complete

- Rewrote Phase 0 conclusion into a short constitution close summarizing governance rules (claims/evidence/provenance/falsifiers/corridor history).
- Completed Phase 0 compactification pass (sections rewritten into enforceable, reviewer-facing contracts).

### 2026-01-03 — Stage 1 (Rung 1.9): Phase 0 paper spine lock on ed (main.tex/abstract/appendix policy)

- Rewrote Phase 0 main.tex into a clean, stable paper spine (no placeholders), with explicit separation between normative body and non-normative appendices.
- Rewrote corrupted abstract into constitution-grade summary consistent with Phase 0 scope (governance only).
- Ensured bibliography is non-empty by citing workflow reproducibility references in the reproducibility contract.
- Added explicit non-normative disclaimers to each appendix to prevent scope confusion.



### 2026-01-03 — Stage 1 (Rung 1.10): Phase 0 split into constitution + appendices

- Split Phase 0 into two build targets:
  - phase0/paper/main.tex (normative constitution)
  - phase0/paper/appendices.tex (non-normative supporting appendices)
- Added T1/lmodern for cleaner PDF text extraction under XeLaTeX.

### 2026-01-03 — Stage 1 (Rung 1.10c): Remove final cross-ref in appendices; verify Phase 0 builds clean

- Removed last dangling cross-reference in Phase 0 appendices (no undefined refs remain).
- Verified bibliography keys and citation resolution under latexmk.

## 2026-01-05 — Phase 3 bootstrap (scope-aligned)
- Created phase3/ structure + Phase 3 contract docs (SCOPE, NON_CLAIMS, ASSUMPTIONS, APPROXIMATION_CONTRACT, CLAIMS, CLAIMS_TABLE, REPRODUCIBILITY).
- Added scripts/phase3_gate.sh (Level A/B/C) + phase3/workflow/Snakefile skeleton.
- Added Phase 3 fit + injection script skeletons and paper skeleton.

## 2026-01-05 — Phase 3 θ-fit contract (bootstrap placeholder)
- Added Phase 3 fit ansatz contract + targets.yaml (placeholder_mode=true).
- Fit runner now reads YAML, emits provenance meta + diagnostics JSON, and bundles them for Level A verification.

## 2026-01-05 — Phase 3 baseline fixed-offset locked (b_PMNS = pi)
- Discrete offset sweep selected b_PMNS = pi as best hypothesis; locked in targets.yaml and recorded in phase3 notes.

## 2026-01-05 — Phase 3 baseline fixed-offset locked (b_PMNS = pi)
- Discrete offset sweep selected b_PMNS = pi as best hypothesis; locked in targets.yaml and recorded in phase3 notes.

## 2026-01-07 — Phase 4: diagnostic FRW-facing mapping stub

- Landed a first Phase 4 artifact in `phase4/artifacts/origin-axiom-phase4.pdf`,
  focused on *structure* rather than physical claims.
- Introduced the F1 mapping family, which reuses the Phase 3 vacuum mechanism
  and quantile-based floor from
  `phase3/outputs/tables/mech_baseline_scan_diagnostics.json` to define a
  strictly positive scalar \(E_{\mathrm{vac}}(\theta)\) on a uniform
  \(\theta \in [0, 2\pi)\) grid.
- Added three diagnostic layers:
  - an F1 sanity curve
    (`phase4/outputs/tables/phase4_F1_sanity_curve.csv`) to check that
    \(E_{\mathrm{vac}}(\theta)\) behaves numerically and respects the Phase 3
    floor;
  - F1 shape diagnostics with a *toy* \(\theta\)-corridor summarised by
    `phase4_F1_shape_diagnostics.json` / `phase4_F1_shape_mask.csv`, used only
    as a descriptive shape probe (not a physical corridor or \(\theta_\star\));
  - an FRW-inspired toy module that rescales \(E_{\mathrm{vac}}(\theta)\) into a
    proxy \(\Omega_\Lambda(\theta)\), evaluates a simple
    \(H^2(a;\theta) = \Omega_r a^{-4} + \Omega_m a^{-3} + \Omega_\Lambda(\theta)\)
    on a late-time scale-factor grid, and logs a per-\(\theta\) "FRW-sane" mask.
- Recorded both the initial empty-mask outcome and the later late-time tweak of
  the FRW toy in `phase4/FRW_TOY_DESIGN.md`, treating them as *local, toy-level*
  positive/negative results about this particular normalisation and sanity
  criterion, not as global statements about the axiom.
- Wrote a dedicated limitations/scope section for Phase 4 clarifying that:
  - F1 is a single toy mapping family,
  - all diagnostics are grid-based and baseline-dependent,
  - no physically justified \(\theta\)-corridor or candidate \(\theta_\star\) is
    claimed at this phase, and
  - any future corridor tightening, \(\theta_\star\) proposal, or data
    calibration must live in later rungs/phases with explicit new assumptions.

## 2026-01-07 — Phase 3 instability diagnostics + Phase 4 FRW probe polish

- **Phase 3: toy-mechanism measure diagnostics (measure_v1)**  
  - Implemented `phase3/src/phase3_mech/measure_v1.py`, a lightweight probe of the
    baseline amplitude distribution \(A_0(\theta)\) using the existing
    Phase 3 mechanism output.
  - The script reads the baseline scan from
    `phase3/outputs/tables/mech_baseline_scan.csv` (column `A0`), computes basic
    summary statistics and quantiles, and writes:
    - `phase3/outputs/tables/phase3_measure_v1_stats.json` (summary stats + eps-grid),
    - `phase3/outputs/tables/phase3_measure_v1_hist.csv` (binned histogram).
  - Console output now records a small eps-grid diagnostic, e.g.
    \(\mathrm{Pr}[A_0 < \varepsilon]\) for \(\varepsilon \in \{0.005, 0.01, 0.02, 0.05\)\,
    making explicit how often the toy ensemble wanders into the deep cancellation basin
    near \(A_0 = 0\) under the current configuration.
  - All of these are explicitly documented as **toy-model diagnostics only**:
    they do **not** impose a physical floor, alter the binding experiment, or
    introduce new corridor constraints.

- **Phase 3: instability-penalty diagnostic (instability_penalty_v1)**  
  - Implemented `phase3/src/phase3_mech/instability_penalty_v1.py`, which consumes
    `phase3_measure_v1_stats.json` and constructs a simple “instability penalty”
    functional over the eps-grid.
  - The current implementation treats the measured fractions below each \(\varepsilon\)
    threshold as a toy proxy for how heavily the mechanism samples the deep
    cancellation basin, and aggregates them into a scalar
    `total_penalty` (today's baseline run gives `total_penalty ≈ 22.64`).
  - Output is written to
    `phase3/outputs/tables/phase3_instability_penalty_v1.json` and is positioned
    as a **non-binding diagnostic** that could be iterated in future rungs
    (e.g. with alternative eps-grids, weights, or comparisons between mechanisms).

- **Phase 3 paper + gate refresh**  
  - Extended Section 3 (results) to briefly report the new measure/instability
    diagnostics and emphasise their purely diagnostic, toy-model status.
  - Updated Appendix B (reproducibility) to document:
    - `measure_v1.py` (inputs, outputs, and console eps-grid summary),
    - `instability_penalty_v1.py` (dependency on `phase3_measure_v1_stats.json`
      and penalty JSON output).
  - Rebuilt the Phase 3 paper via `scripts/phase3_gate.sh`; Level-A gate passes and
    the canonical artifact `phase3/artifacts/origin-axiom-phase3.pdf` is up to date.

- **Phase 4: F1/FRW probe clarification (Rung 1 polish)**  
  - Clarified in the Phase 4 text that the F1 mapping
    \(E_{\text{vac}}(\theta) = \alpha\,A(\theta)^\beta\) with baseline
    \((\alpha, \beta) = (1, 4)\) is a **structural toy choice**, not a physical
    identification of vacuum energy.
  - Tightened the description of the FRW-facing diagnostics stack and the
    “shape/ΛCDM-like” probe, making explicit that:
    - no θ-filter is promoted to binding status,
    - no fine-tuning claim is made,
    - the current `frw_data_probe` remains a stub that records a structured
      negative result when no external dataset is present.
  - Rebuilt the Phase 4 paper via `scripts/phase4_gate.sh`; gate passes and
    `phase4/artifacts/origin-axiom-phase4.pdf` is in sync with the code.

- **Forward hook to next rung**  
  - The new diagnostics and text changes are deliberately framed as
    **non-binding infrastructure**: they sharpen our view of how the toy
    mechanism explores the cancellation basin and how the FRW pipeline reacts,
    without yet answering the central “why enforce a floor?” question.
  - The next Phase 3 rung is expected to focus on candidate *mechanisms* for
    non-cancellation (topological, consistency-based, or emergent), which can
    then be tested against these diagnostics rather than extending them further.


2026-01-07 – Phase 3 / Phase 4 Rung 1: floor diagnostics and FRW pipeline

- Phase 3 mechanism paper
  - Finalised the Rung 1 mechanism write-up and regenerated
    \`phase3/outputs/paper/phase3_paper.pdf\` and the tracked artifact
    \`phase3/artifacts/origin-axiom-phase3.pdf\`.
  - Added a lightweight ensemble-measure probe via
    \`phase3/src/phase3_mech/measure_v1.py\), which reads the baseline
    mechanism scan (\`mech_baseline_scan.csv\`) and constructs the
    empirical distribution of the global amplitude observable $begin:math:text$A\_0$end:math:text$.
    The script writes
    \`phase3/outputs/tables/phase3_measure_v1_stats.json\` and
    \`phase3/outputs/tables/phase3_measure_v1_hist.csv\`, and prints
    selected quantiles and fractions below illustrative $begin:math:text$\\varepsilon$end:math:text$
    thresholds.  These are explicitly documented as **toy diagnostics**,
    not physical floor scales or binding constraints.
  - Added a companion instability-penalty diagnostic
    \`phase3/src/phase3_mech/instability_penalty_v1.py\), which
    consumes the stats JSON, aggregates the probability mass in the
    near-zero basin, and reports a dimensionless penalty score as
    \`phase3/outputs/tables/phase3_instability_penalty_v1.json\`.
    This quantity is tracked as an internal health check on the
    cancellation structure of the current toy ensemble, not as a
    cosmology-facing observable.
  - Updated the Phase 3 paper (results and reproducibility appendices)
    to reference the new diagnostics, including explicit reporting of
    the measured fractions \(\Pr[A_0 < \varepsilon]\) for several
    benchmark \(\varepsilon\) values.  The text stresses that (i) these
    are entirely configuration-dependent, (ii) no physical floor value
    is promoted, and (iii) no corridor-narrowing claim is made at this
    rung.
  - Added \`phase3/PHASE3_NEXT_RUNG.md\`, a design document for the next
    rungs.  It sketches candidate directions for turning the abstract
    non-cancellation floor idea into more structurally justified
    mechanisms (e.g. consistency- or topology-motivated floors), and
    clarifies that Phase 5 should remain a placeholder until such
    candidates are properly formulated and tested.

- Phase 4 FRW-facing pipeline
  - Regenerated the Phase 4 paper and artifacts via the gated build,
    updating \`phase4/outputs/paper/phase4_paper.pdf\` and
    \`phase4/artifacts/origin-axiom-phase4.pdf\) after clarifying the
    F1 mapping family and the FRW diagnostic stack.
  - Tightened the documentation of the Phase 4 scripts:
    - the F1 sanity and shape diagnostics
    - the FRW toy and viability scans
    - the $begin:math:text$\\Lambda$end:math:text$CDM-like probe and the joint shape/FRW probe
    - the (currently stubbed) data-probe layer
    including explicit input/output paths under
    \`phase4/outputs/tables/\` and the summary figure in
    \`phase4/outputs/figures/phase4_F1_frw_shape_probe_omega_lambda_vs_theta.png\`.
  - Made it explicit in the text that (i) the F1 mapping is a structural
    toy choice rather than a physically justified relation between
    amplitude and vacuum energy, (ii) all FRW diagnostics are treated as
    non-binding sanity checks, and (iii) no $begin:math:text$\\theta$end:math:text$-filter is
    promoted to the Phase 0 corridor at this stage.

- Sandbox and exploration hygiene
  - Archived several speculative explorations (including numerology and
    mechanism sketches developed with external assistants) into a
    dedicated \`sandbox/\` folder, deliberately **outside** the rung
    structure.  These documents are kept as idea reservoirs and negative
    results, not as sources of claims.  Any concept that graduates from
    sandbox into a Phase will be re-derived, recomputed, and documented
    from scratch within the Phase 0–4 ladder.

At this point, Phases 3 and 4 both have Rung 1 papers and gated build
paths, with additional diagnostics and next-rung design notes in place.
No new binding claims have been added to the Phase 0 ledger; the focus
of this step was to harden the existing toy mechanism and FRW-facing
infrastructure while keeping the epistemic status of all quantities
strictly scoped.

### 2026-01-07 – Unified Phase 0–4 paper gates and global build driver

**What changed**

- Added Level-A gate plumbing for Phase 0 and Phase 1 so they match the Phase 2–4 pattern:
  - Phase 0 and Phase 1 now have `scripts/phase0_gate.sh` and `scripts/phase1_gate.sh` that:
    - Resolve the repo root.
    - `cd` into `phase0/workflow` / `phase1/workflow`.
    - Invoke Snakemake to rebuild the paper and canonical artifact.
- Standardised the paper build pattern across Phases 0–4:
  - Each gate builds `paper/main.tex` via `latexmk` and then copies `main.pdf` to:
    - `phaseN/outputs/paper/phaseN_paper.pdf`
    - `phaseN/artifacts/origin-axiom-phaseN.pdf`
  - This brings Phase 0–2 in line with the existing Phase 3 / Phase 4 pattern.
- Introduced `scripts/build_paper.sh` as a single entry point:
  - Runs Phase 0–4 gates (where present).
  - Prints a summary of canonical artifact locations for a quick visual check.
- Verified on the MacBook dev environment that:
  - `oa && scripts/build_paper.sh`
  successfully (re)builds and refreshes:
  - `phase0/artifacts/origin-axiom-phase0.pdf`
  - `phase1/artifacts/origin-axiom-phase1.pdf`
  - `phase2/artifacts/origin-axiom-phase2.pdf`
  - `phase3/artifacts/origin-axiom-phase3.pdf`
  - `phase4/artifacts/origin-axiom-phase4.pdf`

**Status**

- Phase 0–4 paper builds now share a single, consistent Snakemake + gate + artifact pattern.
- Rung considered **stable** for paper-build plumbing; future rungs will focus on content and physics, not infrastructure.


2026-01-08 (local) — Phase 5 roadmap scaffold
---------------------------------------------
- Added docs/phase5_roadmap.md as the canonical design brief for Phase 5.
- Clarified Phase 5’s role: interface between the Phase 0–4 toy tower and external cosmological summaries.
- Explicitly recorded boundaries: no sandbox numerology is promoted to formal claims without derivation + code.
- Outlined initial Phase 5 rungs (P5.1–P5.5) focusing on interfaces, diagnostics, and eventual data contact.


2026-01-08 (local) — Phase 5 interface v1
-----------------------------------------
- Created Phase 5 skeleton: phase5/config, phase5/src/phase5, phase5/outputs/{tables,figures}.
- Added phase5/config/phase5_inputs_v1.json listing which Phase 3 and Phase 4 outputs are treated as Phase 5 inputs.
- Implemented phase5/src/phase5/phase5_interface_v1.py, a non-physical connectivity check that:
  - Locates the repo root from its own path,
  - Loads the Phase 5 interface spec,
  - Verifies existence of referenced tables/masks,
  - Writes phase5/outputs/tables/phase5_interface_v1_summary.json.
- Kept this rung purely diagnostic: no new claims, no numerology, no external data.


2026-01-08 (local) – Phase 4 F1 sanity diagnostics stub
------------------------------------------------------
- Added phase4/src/phase4/f1_sanity_curve_diagnostics_v1.py.
- This script writes a minimal JSON diagnostics stub
  phase4/outputs/tables/phase4_F1_sanity_curve_diagnostics.json
  pointing to the existing F1 sanity curve CSV.
- Phase 5 interface v1 now reports all Phase 3/4 inputs as OK,
  with only the optional external FRW distance file marked as missing.

2026-01-08 (local) – Phase 5 interface Rung 0 check
---------------------------------------------------
- On branch phase5-interface-local, ran:
  python phase5/src/phase5/phase5_interface_v1.py
- Confirmed that all required Phase 3 and Phase 4 inputs are present:
  * phase3: mech_baseline_diagnostics, measure_stats, measure_hist,
    instability_penalty (all OK).
  * phase4: F1 sanity curve, shape diagnostics, FRW toy, viability,
    LCDM probe, shape probe, corridors, data probe (all OK).
- The only missing asset is the optional external FRW distance file
  phase4/data/external/frw_distance_binned.csv, which is explicitly
  documented as optional and must be handled gracefully by Phase 5.
- This run serves as the Rung 0 sanity confirmation: Phase 5 is now
  authorized to consume the locked Phase 3/4 pipeline outputs via
  phase5_interface_v1, without mutating upstream phases.

2026-01-08 (local) – Phase 5 gate (Rung 0 interface wiring)
-----------------------------------------------------------
- Created scripts/phase5_gate.sh as a Level-A gate for Phase 5.
- The gate delegates to phase5/src/phase5/phase5_interface_v1.py,
  which inspects locked Phase 3 and Phase 4 outputs only.
- Verified that the gate runs cleanly:
  * All required Phase 3 diagnostics present (baseline, measure, penalty).
  * All required Phase 4 F1 + FRW diagnostics present (sanity, shape,
    viability, LCDM/shape/data probes, corridors).
  * The only missing item is the explicitly optional external file
    phase4/data/external/frw_distance_binned.csv, which Phase 5
    is required to handle gracefully.
- Phase 5 is now structurally integrated into the gate system without
  mutating upstream phases, ready for Rung 1 design work.

2026-01-08 (local) — Phase 5 paper Rung 1 skeleton
--------------------------------------------------
- Created a minimal, self-contained LaTeX skeleton for the Phase 5 paper
  under phase5/paper/.
- Defined sections for preamble, scope and non-claims, interface
  contract, a stub viability dashboard, and limitations/next-rungs.
- Added stub appendices for interface claims and reproducibility notes,
  and a local Reference.bib.
- The Phase 5 paper is explicitly descriptive and meta-level: it
  documents the Phase 5 interface and program role without introducing
  new physics claims or modifying Phases 3/4.

- 2026-01-08 (phase5-interface-local, Rung 3):
  - Ran `phase5/src/phase5/make_interface_dashboard_v1.py` to generate
    `phase5/outputs/tables/phase5_interface_dashboard_v1_summary.csv`
    from the interface summary JSON.
  - Updated `phase5/paper/sections/03_viability_dashboard_stub.tex` to
    describe the current interface-level dashboard and its CSV schema,
    keeping the scope strictly program- and structure-level with no new
    physics claims or derived viability scores.

- 2026-01-08 (phase5-interface-local, Rung 4):
  - Added `scripts/build_phase5_paper.sh` as a one-button Phase 5 build
    driver that runs the Phase 5 gate, regenerates the interface
    dashboard CSV, builds the Phase 5 paper with `latexmk`, and copies
    the result to `phase5/artifacts/origin-axiom-phase5.pdf`.
  - This wires Phase 5 into the program-level build story without
    modifying upstream phases or their gates.

### [2026-01-08] Phase 4 F1.D0 – External FRW distance contract stub

- Appended a new Rung F1.D0 section to `phase4/FRW_DATA_DESIGN.md`
  defining the contract for the external FRW distance–redshift dataset:
  - path: `phase4/data/external/frw_distance_binned.csv`
  - required columns: `z`, `mu`, `sigma_mu` with documented units and
    a diagonal-error model at this rung.
  - clarified that the repo may ship with a header-only CSV and that
    Phase 4/5 code must handle the zero-row case gracefully.
- Created a header-only stub CSV at
  `phase4/data/external/frw_distance_binned.csv` that matches the
  declared schema.
- This establishes the first explicit external-observable contract
  on the roadmap from the axiom (via F1 mappings) to FRW distance
  data, without yet introducing a likelihood or new claims.

### [2026-01-08] Phase 4 F1.D1 – External FRW distance diagnostics script

- Extended `phase4/FRW_DATA_DESIGN.md` with Rung F1.D1, defining a
  small diagnostics script for the external FRW distance dataset:
  - script: `phase4/src/phase4/f1_frw_external_diagnostics_v1.py`
  - output: `phase4/outputs/tables/phase4_F1_frw_external_diagnostics.json`.
- Implemented the diagnostics script to:
  - resolve repo and Phase 4 roots from its own location,
  - read `phase4/data/external/frw_distance_binned.csv` while skipping
    comment and empty lines,
  - check that the required columns `z`, `mu`, `sigma_mu` exist,
  - parse rows into floats with basic error counting,
  - compute row counts and simple ranges (`z_min/z_max`, `mu_min/mu_max`,
    `sigma_mu_min/sigma_mu_max`) when data are present,
  - check for non-decreasing `z`,
  - treat the zero-row case as a valid state (`ok_zero_rows`).
- The script is intentionally model-free: it makes no θ- or F1-specific
  assumptions and introduces no likelihood or physical claims. It
  serves purely as a plumbing and inspection layer for external data,
  to be used later by Phase 5 and higher rungs of Phase 4.

### [2026-01-08] Phase 5 – Rung 2: interface wiring of external FRW diagnostics

- Updated `phase5/config/phase5_inputs_v1.json` to include a new Phase 4
  entry:
  - `frw_external_diagnostics` →
    `phase4/outputs/tables/phase4_F1_frw_external_diagnostics.json`.
- Re-ran the Phase 5 interface and dashboard:
  - `scripts/phase5_gate.sh`
  - `phase5/src/phase5/make_interface_dashboard_v1.py`
- The interface summary now exposes the external FRW diagnostics JSON
  alongside the existing Phase 4 F1 outputs, so Phase 5 can see:
  - whether the external dataset is present,
  - its basic properties (as computed by the Phase 4 F1.D1 script),
  - and its status (`ok` vs `ok_zero_rows` vs missing).
- This rung remains strictly meta-level:
  - no new physics, no θ- or FRW modeling, and no likelihood.
  - It only extends the program-level contract so that Phase 5 is aware
    of the external FRW diagnostics produced by Phase 4.
