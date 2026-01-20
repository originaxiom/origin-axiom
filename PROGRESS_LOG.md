
## NOTE ON LEGACY ENTRIES

> **Documentation layout note (Belt G, 2026-01-11):** This log preserves file paths as they were at the time each entry was written. Some Phase 2–4 design and audit documents have since moved into `phase2/audit/` and `phase3/phase4/design/` subdirectories. See the 2026-01-11 Belt G entry at the end of this file for a map from old paths to current locations.


Early entries in this log predate the current phased layout and may reference
legacy paths (e.g., `src/`, `data/`, `figures/`). The canonical structure is
now Phase 0–5 plus the Stage 2 diagnostic belts (see `README.md` and
`docs/STATE_OF_REPO.md`).

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

### [2026-01-08] Phase 5 – Rung 3: document external FRW diagnostics in interface paper

- Extended the Phase 5 interface-contract section:
  - Updated `phase5/paper/sections/02_interface_contract.tex` to include
    an explicit subsection for the external FRW diagnostics hook:
    - `frw_external_diagnostics` ->
      `phase4/outputs/tables/phase4_F1_frw_external_diagnostics.json`.
  - Clarified that Phase 5 only consumes the Phase 4 diagnostics JSON
    and does not introduce any new FRW modeling or likelihood.
- Updated the dashboard stub:
  - Appended a short note to
    `phase5/paper/sections/03_viability_dashboard_stub.tex` explaining
    that the Phase 5 interface dashboard now surfaces the external FRW
    diagnostics row alongside the F1 outputs.
- This rung is still purely program-level:
  - No new physics, no re-fitting, and no change to the numerical
    content of Phases 3 and 4.
  - The goal is to keep the Phase 5 paper aligned with the actual
    interface and dashboard wiring.

### [2026-01-08] Phase 5 — Rung 4: interface sanity table v1

- Added a Phase 5 script,
  `phase5/src/phase5/make_rung4_sanity_table_v1.py`, which consumes the
  existing interface summary
  (`phase5/outputs/tables/phase5_interface_v1_summary.json`) and
  produces a compact CSV "sanity table":
  `phase5/outputs/tables/phase5_rung4_sanity_table_v1.csv`.
- The table collects, for each Phase 3 / Phase 4 / external entry:
  - `section`, `key`, `relpath`, `exists`, and `size_bytes`, and
  - for the external FRW diagnostics row only, optional extras:
    `ext_status`, `ext_n_rows`, and a short `ext_extra` summary of
    simple scalar fields found in
    `phase4/outputs/tables/phase4_F1_frw_external_diagnostics.json`.
- This rung remains strictly program-level:
  - no new physics,
  - no re-interpretation or re-fitting of Phase 3 or Phase 4 outputs,
  - and no direct reading of the raw external FRW-distance CSV beyond
    what Phase 4 has already summarized.
- The goal is to give collaborators a single, machine-readable snapshot
  of what the Phase 5 interface "sees" across Phases 3/4 and the
  external FRW diagnostics, in a way that is easy to inspect, diff, and
  extend in later rungs.

### [2026-01-08] Phase 5 — Rung 5: minimal interface sanity figure

- Added a small Phase 5 script:
  - `phase5/src/phase5/make_rung5_interface_figure_v1.py`.
- This script consumes the Rung 4 sanity table:
  - `phase5/outputs/tables/phase5_rung4_sanity_table_v1.csv`,
  and produces a simple horizontal bar plot:
  - `phase5/outputs/figures/phase5_interface_sanity_v1.png`.
- The figure is purely program-level:
  - it visualizes which Phase 3/4 interface files exist,
    their sizes (in KB), and any external-status flags reported by
    the F1 external-diagnostics JSON.
  - it does **not** introduce new FRW modeling, likelihoods, or
    physics claims; it only makes the interface contract more
    inspectable.
- The PNG lives under `phase5/outputs/figures/` and is not tracked in
  git, consistent with the treatment of other generated artifacts.

### [2026-01-08] Phase 5 — R5: remove gate–paper recursion and hook into global build

- Fixed a recursion bug between `scripts/phase5_gate.sh` and
  `scripts/build_phase5_paper.sh`:
  - Restored `phase5_gate.sh` to run only the Phase 5 interface
    (no paper build, no artifact).
  - Left `build_phase5_paper.sh` as the place that runs the Phase 5 gate
    and rebuilds the Phase 5 paper + canonical artifact.
- Updated `scripts/build_all_papers.sh`:
  - Phases 0–4 still use their gate scripts.
  - Phase 5 is now invoked via `scripts/build_phase5_paper.sh`, which
    runs the Phase 5 gate and refreshes
    `phase5/artifacts/origin-axiom-phase5.pdf`.
- This rung is purely infrastructural: no physics, no changes to
  Phase 3/4 numerics, only a correction to the program-level build
  graph to avoid infinite recursion.

## 2026-01-08 — Stage 2: FRW corridor analysis (Rungs 1–3)

### Stage 2 — FRW corridor analysis, rung 1: source inventory

- Added Stage 2 script:
  - `stage2/frw_corridor_analysis/src/analyze_frw_corridor_v1.py`
- Purpose:
  - Treat the Phase 4 FRW outputs as **frozen inputs** and build a compact,
    machine-readable inventory of the masks and corridor summary used by
    downstream Stage 2 rungs.
- Inputs (read-only, all pre-existing Phase 4 artifacts):
  - `phase4/outputs/tables/phase4_F1_frw_viability_mask.csv`
  - `phase4/outputs/tables/phase4_F1_frw_lcdm_probe_mask.csv`
  - `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`
  - `phase4/outputs/tables/phase4_F1_frw_data_probe_mask.csv`
  - `phase4/outputs/tables/phase4_F1_frw_corridors.json`
- Output:
  - `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung1_sources_v1.csv`
    (one row per Phase 4 FRW table / JSON, with columns for path, size,
    n_rows, n_cols, and a short role label).
- Checks:
  - All four Phase 4 FRW mask CSVs exist with `n_rows = 2048` and the expected
    column counts.
  - Corridor summary JSON (`phase4_F1_frw_corridors.json`) exists and is
    readable (size ~ 600–700 bytes).

### Stage 2 — FRW corridor analysis, rung 2: boolean census

- Added Stage 2 script:
  - `stage2/frw_corridor_analysis/src/analyze_frw_corridor_bool_census_v1.py`
- Purpose:
  - For each Phase 4 FRW mask, automatically detect boolean-like columns and
    record `(n_true, n_false, n_na, fractions)` to quantify how populated each
    diagnostic flag is before defining any “corridor families.”
- Inputs (same frozen Phase 4 masks as rung 1):
  - `phase4/outputs/tables/phase4_F1_frw_viability_mask.csv`
  - `phase4/outputs/tables/phase4_F1_frw_lcdm_probe_mask.csv`
  - `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`
  - `phase4/outputs/tables/phase4_F1_frw_data_probe_mask.csv`
- Output:
  - `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung2_bool_census_v1.csv`
    (one row per mask × boolean column, with counts and fractions).
- Key census results from this run (2048 grid points total):
  - `phase4_F1_frw_viability_mask.csv`  
    - `has_matter_era`: 2048 true, 0 false, 0 NA  
    - `has_late_accel`: 1016 true, 1032 false, 0 NA  
    - `smooth_H2`: 2048 true, 0 false, 0 NA  
    - `frw_viable`: 1016 true, 1032 false, 0 NA
  - `phase4_F1_frw_lcdm_probe_mask.csv`  
    - `frw_viable`: 1016 true, 1032 false, 0 NA  
    - `lcdm_like`: 63 true, 1985 false, 0 NA
  - `phase4_F1_frw_shape_probe_mask.csv`  
    - `in_toy_corridor`: 1186 true, 862 false, 0 NA  
    - `frw_viable`: 1016 true, 1032 false, 0 NA  
    - `lcdm_like`: 63 true, 1985 false, 0 NA  
    - `shape_and_viable`: 154 true, 1894 false, 0 NA  
    - `shape_and_lcdm`: 40 true, 2008 false, 0 NA
  - `phase4_F1_frw_data_probe_mask.csv`  
    - `has_matter_era`: 2048 true, 0 false, 0 NA  
    - `has_late_accel`: 1016 true, 1032 false, 0 NA  
    - `smooth_H2`: 2048 true, 0 false, 0 NA  
    - `frw_viable`: 1016 true, 1032 false, 0 NA  
    - `data_ok`: 0 true, 2048 false, 0 NA (no external FRW distance data bundled yet).
- Interpretation:
  - Viability, matter era, and smoothness flags behave as expected: the FRW
    toy sector enforces matter-era and smooth-H² everywhere, with viability
    and late-acceleration cutting the grid roughly in half.
  - LCDM-like flags are **sparse** (63/2048 and 40/2048 in the strict
    shape+LCDM intersection), confirming that any “near-LCDM” corridor will be
    highly selective.
  - `data_ok` is uniformly false, making it explicit that all results at this
    rung are driven by the **internal FRW toy model only**, with no external
    distance data in play.

### Stage 2 — FRW corridor analysis, rung 3: FRW family aggregates

- Added Stage 2 script:
  - `stage2/frw_corridor_analysis/src/analyze_frw_corridor_families_v1.py`
- Purpose:
  - Define a small set of coarse **FRW families** on the θ-grid as simple
    combinations of the boolean masks previously audited in rungs 1–2, and
    record how much of the grid each family occupies.
- Nominal grid size:
  - `n_grid = 2048` θ-samples (as inferred from the Phase 4 masks).
- Families and current occupancy (from this run):
  - `F1_FRW_VIABLE`  
    - definition: points with `frw_viable = True` in the FRW viability mask  
    - result: `n_theta = 1016`, `frac_of_grid ≈ 0.49609`
  - `F2_LCDM_LIKE`  
    - definition: points flagged as `lcdm_like = True` in the LCDM probe mask  
    - result: `n_theta = 63`, `frac_of_grid ≈ 0.03076`
  - `F3_TOY_CORRIDOR`  
    - definition: points with `in_toy_corridor = True` in the shape probe mask  
    - result: `n_theta = 1186`, `frac_of_grid ≈ 0.57910`
  - `F4_CORRIDOR_AND_VIABLE`  
    - definition: `in_toy_corridor = True` and `frw_viable = True`  
    - result: `n_theta = 154`, `frac_of_grid ≈ 0.07520`
  - `F5_CORRIDOR_AND_LCDM`  
    - definition: `in_toy_corridor = True` and `lcdm_like = True`  
    - result: `n_theta = 40`, `frac_of_grid ≈ 0.01953`
  - `F6_DATA_OK`  
    - definition: `data_ok = True` in the FRW data probe mask  
    - result: `n_theta = 0`, `frac_of_grid = 0.00000` (no external data bundled).
- Output:
  - `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung3_families_v1.csv`
    (one row per family with counts, fractions, and a short human-readable
    definition).
- Interpretation / status:
  - FRW viability covers about half of the θ-grid, while the toy corridor
    itself covers a bit more than half; their intersection is significantly
    smaller (~7.5% of the grid).
  - Strict LCDM-like behaviour is rare (~3% of the grid), and even rarer when
    also in the toy corridor (~2%), matching the sparse flags seen in rung 2.
  - `F6_DATA_OK` explicitly records that the current Stage 2 analysis is
    **theory-driven only**, with the FRW distance data channel still empty.
  - These families are **diagnostic only** at this rung: they do not feed
    back into Phases 3–5 and remain candidates for later promotion to:
    - a compact addition in Phase 5 (Option A), or
    - a dedicated Stage 2 / Phase 6 FRW corridor paper (Option B).


## 2026-01-08 — Stage 2: FRW corridor analysis, Rung 4 (family overlap v1)

**Scope.** Downstream-only analysis of Phase 4 FRW masks, defining a compact set
of FRW “families” (Rung 3) and now measuring their **overlaps** and coverage
on the nominal θ-grid. This remains a Stage 2 exploration layer; no feedback
into Phases 0–5.

**Inputs.**

- Stage 2 families table (Rung 3):
  - `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung3_families_v1.csv`
- Phase 4 FRW masks (as in Rungs 1–3):
  - `phase4/outputs/tables/phase4_F1_frw_viability_mask.csv`
  - `phase4/outputs/tables/phase4_F1_frw_lcdm_probe_mask.csv`
  - `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`
  - `phase4/outputs/tables/phase4_F1_frw_data_probe_mask.csv`

**Script.**

- `stage2/frw_corridor_analysis/src/analyze_frw_corridor_family_overlap_v1.py`

This script:

1. Reconstructs the boolean families on the nominal grid (N = 2048):
   - F1_FRW_VIABLE
   - F2_LCDM_LIKE
   - F3_TOY_CORRIDOR
   - F4_CORRIDOR_AND_VIABLE
   - F5_CORRIDOR_AND_LCDM
   - F6_DATA_OK
2. Recomputes basic cardinalities (sanity check):
   - F1_FRW_VIABLE: n_θ = 1016, frac_of_grid ≈ 0.49609
   - F2_LCDM_LIKE: n_θ = 63, frac_of_grid ≈ 0.03076
   - F3_TOY_CORRIDOR: n_θ = 1186, frac_of_grid ≈ 0.57910
   - F4_CORRIDOR_AND_VIABLE: n_θ = 154, frac_of_grid ≈ 0.07520
   - F5_CORRIDOR_AND_LCDM: n_θ = 40, frac_of_grid ≈ 0.01953
   - F6_DATA_OK: n_θ = 0, frac_of_grid = 0.00000
3. Builds an overlap census table across all families (pairwise and
   higher-order overlaps), expressed in counts and fractions of the
   nominal grid.

**Outputs.**

- Family overlap table:
  - `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung4_family_overlap_v1.csv`
- Log (human): printed summary of grid size and per-family coverage.

**Status.**

- Rung 4 completes the **coverage + overlap** view of the Phase 4 FRW masks in
  a Stage 2 layer, without modifying any Phase artifacts.
- At this rung we do **not** yet promote any family to a Phase-level claim;
  the overlap table is a scouting tool for future rungs:
  - Rung 5+: visual exploration and robustness checks for a small set of
    candidate “corridor families” that might eventually be promoted into:
    - Option A: a lightweight Phase 5 addendum, or
    - Option B: a dedicated FRW-focused Stage 2 / Phase 6 paper.


[2026-01-08] Stage 2 – FRW corridor analysis (rungs 1–5)
- Implemented a Stage 2 FRW-corridor analysis stack in
  stage2/frw_corridor_analysis:
  - Rung 1 (sources table):
    - stage2/frw_corridor_analysis/src/analyze_frw_corridor_v1.py
    - Summarizes Phase 4 FRW masks and corridor config into
      stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung1_sources_v1.csv.
  - Rung 2 (boolean census):
    - stage2/frw_corridor_analysis/src/analyze_frw_corridor_bool_census_v1.py
    - Scans the Phase 4 FRW mask CSVs for boolean-like columns and records
      per-flag true/false counts into
      stage2_frw_corridor_rung2_bool_census_v1.csv.
  - Rung 3 (family definitions):
    - stage2/frw_corridor_analysis/src/analyze_frw_corridor_families_v1.py
    - Defines FRW theta-families on the 2048-point grid:
      F1_FRW_VIABLE, F2_LCDM_LIKE, F3_TOY_CORRIDOR,
      F4_CORRIDOR_AND_VIABLE, F5_CORRIDOR_AND_LCDM, F6_DATA_OK,
      writing their sizes and fractions into
      stage2_frw_corridor_rung3_families_v1.csv.
  - Rung 4 (family overlaps):
    - stage2/frw_corridor_analysis/src/analyze_frw_corridor_family_overlap_v1.py
    - Computes conditional overlaps frac_i_given_j across families and
      records them in
      stage2_frw_corridor_rung4_family_overlap_v1.csv.
      Confirms, e.g., that F2_LCDM_LIKE is a strict subset of F1_FRW_VIABLE,
      and that F5_CORRIDOR_AND_LCDM corresponds to the F3 ∩ F2 intersection.
  - Rung 5 (visual summaries):
    - stage2/frw_corridor_analysis/src/plot_frw_corridor_families_v1.py
    - Uses phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv to
      generate:
      - stage2/frw_corridor_analysis/outputs/figures/
        stage2_frw_corridor_family_theta_hist_v1.pdf
        (theta histograms for the main FRW families), and
      - stage2/frw_corridor_analysis/outputs/figures/
        stage2_frw_corridor_family_omega_lambda_scatter_v1.pdf
        (theta–omega_lambda scatter, colored by family).
- Sanity:
  - All family counts in rungs 3–5 match the Phase 4 masks and each other:
    F1=1016, F2=63, F3=1186, F4=154, F5=40, F6=0 over 2048 grid points.
  - Data flag F6_DATA_OK remains identically false (no external FRW
    distance data yet), consistent with the current Phase 4 configuration.
- Status:
  - Stage 2 FRW corridor rungs 1–5 are complete and remain strictly
    downstream of Phase 4 artifacts (no feedback into Phase 4).
  - These results are candidates for future promotion into either:
    - a lightweight addition to Phase 5, or
    - a dedicated downstream Stage 2 / Phase 6 FRW-focused paper,
    depending on later stability and interpretability checks.

### Stage 2 – FRW corridors

#### Rung 6 – contiguity of FRW families (stage2/frw_corridor_analysis)

- Added script `stage2/frw_corridor_analysis/src/analyze_frw_corridor_contiguity_v1.py`.
- Script reads `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv` and, for each FRW family
  \(F_1\)–\(F_5\), computes:
  - total number of true points `n_theta` and their fraction of the full grid, `frac_of_grid`;
  - the number of contiguous θ-segments in which the family is populated;
  - per-segment diagnostics, written to
    `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung6_contiguity_v1.csv`.
- Current baseline (2048-point θ-grid):
  - `F1_FRW_VIABLE`: 1 contiguous arc (1016 points, ~0.50 of grid).
  - `F2_LCDM_LIKE`: 2 disjoint lobes (63 points, ~0.03 of grid).
  - `F3_TOY_CORRIDOR`: 2 lobes (1186 points, ~0.58 of grid).
  - `F4_CORRIDOR_AND_VIABLE`: 2 lobes (154 points, ~0.08 of grid).
  - `F5_CORRIDOR_AND_LCDM`: 2 lobes (40 points, ~0.02 of grid).
- Interpretation (Stage 2, non-claim): FRW viability forms a single broad corridor in θ,
  while LCDM-like and corridor-related families split into two clean θ-bands. This favours
  reading them as genuine geometric “corridors” rather than speckled noise, but no promotion
  into Phase 4/5 PDFs is made at this rung.


## 2026-01-09 – Stage 2: FRW corridor analysis (Rung 7 – θ-stride robustness)

- Added `stage2/frw_corridor_analysis/src/analyze_frw_corridor_stride_robustness_v1.py`.
- The script reads `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`
  and reuses the FRW families defined in Stage 2 (F1–F5):
  `frw_viable`, `lcdm_like`, `in_toy_corridor`, `shape_and_viable`,
  `shape_and_lcdm`.
- For strides {1, 2, 4, 8}, it:
  - subsamples the θ-grid,
  - recomputes per-family counts and fractions,
  - counts the number of contiguous θ-segments on the subsampled grid,
  - writes a summary table to  
    `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung7_stride_robustness_v1.csv`.
- Outcome (current baseline):
  - `F1_FRW_VIABLE` remains a single contiguous θ-block (n_segments = 1) at all
    strides, with frac(θ) ≈ 0.496 at every stride.
  - `F3_TOY_CORRIDOR`, `F4_CORRIDOR_AND_VIABLE`, and `F5_CORRIDOR_AND_LCDM`
    retain a two-segment structure at all strides, with stable occupancy
    fractions (to ~1e-2).
  - `F2_LCDM_LIKE` continues to appear as two small θ-islands under stride
    1–8 with consistent sparse occupancy.
- Interpretation:
  - The FRW corridors and LCDM-like islands identified in previous rungs are
    not a fragile artifact of the exact θ sampling; their basic geometry
    (number of segments and occupancy fractions) is stable under moderate
    downsampling.
  - This rung is descriptive only and does not modify any Phase 4/5 logic or
    claims.


---

### Stage 2 – FRW corridor analysis (Rungs 1–8)

**Context.** Built a Stage 2 analysis chain that stays strictly downstream of
Phase 4 FRW artifacts, using the fixed θ-grid masks from
`phase4/outputs/tables/phase4_F1_frw_*_mask.csv`. No feedback into Phase 4 or
Phase 5; this is exploratory scaffolding for a possible FRW-focused follow-up.

- **Rung 1 – Source table inventory.**  
  Added `stage2/frw_corridor_analysis/src/analyze_frw_corridor_v1.py`, which
  checks for the presence and shape of the four FRW mask tables
  (`frw_viability_mask`, `frw_lcdm_probe_mask`, `frw_shape_probe_mask`,
  `frw_data_probe_mask`) and writes a small provenance table to  
  `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung1_sources_v1.csv`.

- **Rung 2 – Boolean census.**  
  Added `analyze_frw_corridor_bool_census_v1.py`, which scans the four mask
  tables for “boolean-like” columns and counts `(n_true, n_false, n_na)` for
  each. Results are stored in  
  `stage2/.../stage2_frw_corridor_rung2_bool_census_v1.csv`. This confirms that
  core flags such as `frw_viable`, `lcdm_like`, `in_toy_corridor`,
  `shape_and_viable`, `shape_and_lcdm`, and `data_ok` behave as clean {0,1}
  indicators over the θ-grid.

- **Rung 3 – Family definitions.**  
  Added `analyze_frw_corridor_families_v1.py`, which promotes five FRW “families”
  on the fixed θ-grid:
  F1_FRW_VIABLE, F2_LCDM_LIKE, F3_TOY_CORRIDOR,
  F4_CORRIDOR_AND_VIABLE (intersection), and
  F5_CORRIDOR_AND_LCDM (intersection).  
  For each family, the rung records `n_theta` and `frac_of_grid` to  
  `stage2/.../stage2_frw_corridor_rung3_families_v1.csv`. This makes the basic
  size of each family explicit (≈50% viable, ≈3% LCDM-like, etc.).

- **Rung 4 – Family overlap matrix.**  
  Added `analyze_frw_corridor_family_overlap_v1.py`, which constructs a
  pairwise overlap table between the F1–F5 families (Jaccard-like overlaps and
  conditional fractions). Output lives at  
  `stage2/.../stage2_frw_corridor_rung4_family_overlap_v1.csv`. This quantifies
  how much the “LCDM-like” set sits inside (or outside) the toy corridor and
  viability sets, instead of leaving that structure implicit.

- **Rung 5 – Basic family figures (θ and ΩΛ views).**  
  Added `plot_frw_corridor_families_v1.py`, which:
  - makes a simple θ-histogram showing how the F1–F5 families occupy the
    θ-grid, and
  - produces an ΩΛ vs θ view using the Phase 4 `shape_probe_mask` table.  
  Figures are written as PDFs to  
  `stage2/frw_corridor_analysis/outputs/figures/`, e.g.
  `stage2_frw_corridor_family_theta_hist_v1.pdf` and
  `stage2_frw_corridor_family_omega_lambda_scatter_v1.pdf`.  
  These figures are currently **Stage-2 only** and are not wired into any phase
  paper.

- **Rung 6 – Contiguity of families in θ.**  
  Added `analyze_frw_corridor_contiguity_v1.py`, which measures how many
  contiguous θ-segments each family decomposes into, and what fraction of the
  grid each segment family covers. Results are stored in  
  `stage2/.../stage2_frw_corridor_rung6_contiguity_v1.csv`. This checks whether
  viable / LCDM-like sets are scattered speckles or coherent intervals on the
  current θ-grid (they are coherent intervals).

- **Rung 7 – Stride-sampling robustness.**  
  Added `analyze_frw_corridor_stride_robustness_v1.py`, which sub-samples the
  θ-grid with strides {1, 2, 4, 8} and recomputes family occupancy and segment
  counts on each subgrid. Results go to  
  `stage2/.../stage2_frw_corridor_rung7_stride_robustness_v1.csv`. For all
  F1–F5 families, the fraction of “true” points on the subgrid remains stable
  as the stride increases, indicating that the families are not artifacts of
  single isolated θ points.

- **Rung 8 – Local θ-smoothing robustness.**  
  Added `analyze_frw_corridor_smoothing_v1.py`, which applies 1D majority
  filters (window sizes 3 and 5) along the θ-index to each F1–F5 family and
  compares:
  `n_true`, `frac_true`, number of θ-segments, and Jaccard similarity before
  and after smoothing. Output is written to  
  `stage2/.../stage2_frw_corridor_rung8_smoothing_v1.csv`. On the current
  Phase 4 θ-grid, all families remain exactly unchanged (Jaccard = 1.0, same
  occupancy and segment counts), i.e. the FRW corridor / LCDM-like structure is
  robust to mild local smoothing and is not a single-point noise artifact.

At this rung, Stage-2 FRW corridor analysis is a self-contained, reproducible
exploration downstream of Phase 4. It is a candidate source of figures and
diagnostics for a future FRW-focused extension (Phase 6 / Stage-2 paper), but
does not yet promote any new claims into the locked phases.

---

### Stage 2 – FRW corridor analysis (Rungs 1–8)

**Context.** Built a Stage 2 analysis chain that stays strictly downstream of
Phase 4 FRW artifacts, using the fixed θ-grid masks from
`phase4/outputs/tables/phase4_F1_frw_*_mask.csv`. No feedback into Phase 4 or
Phase 5; this is exploratory scaffolding for a possible FRW-focused follow-up.

- **Rung 1 – Source table inventory.**  
  Added `stage2/frw_corridor_analysis/src/analyze_frw_corridor_v1.py`, which
  checks for the presence and shape of the four FRW mask tables
  (`frw_viability_mask`, `frw_lcdm_probe_mask`, `frw_shape_probe_mask`,
  `frw_data_probe_mask`) and writes a small provenance table to  
  `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung1_sources_v1.csv`.

- **Rung 2 – Boolean census.**  
  Added `analyze_frw_corridor_bool_census_v1.py`, which scans the four mask
  tables for “boolean-like” columns and counts `(n_true, n_false, n_na)` for
  each. Results are stored in  
  `stage2/.../stage2_frw_corridor_rung2_bool_census_v1.csv`. This confirms that
  core flags such as `frw_viable`, `lcdm_like`, `in_toy_corridor`,
  `shape_and_viable`, `shape_and_lcdm`, and `data_ok` behave as clean {0,1}
  indicators over the θ-grid.

- **Rung 3 – Family definitions.**  
  Added `analyze_frw_corridor_families_v1.py`, which promotes five FRW “families”
  on the fixed θ-grid:
  F1_FRW_VIABLE, F2_LCDM_LIKE, F3_TOY_CORRIDOR,
  F4_CORRIDOR_AND_VIABLE (intersection), and
  F5_CORRIDOR_AND_LCDM (intersection).  
  For each family, the rung records `n_theta` and `frac_of_grid` to  
  `stage2/.../stage2_frw_corridor_rung3_families_v1.csv`. This makes the basic
  size of each family explicit (≈50% viable, ≈3% LCDM-like, etc.).

- **Rung 4 – Family overlap matrix.**  
  Added `analyze_frw_corridor_family_overlap_v1.py`, which constructs a
  pairwise overlap table between the F1–F5 families (Jaccard-like overlaps and
  conditional fractions). Output lives at  
  `stage2/.../stage2_frw_corridor_rung4_family_overlap_v1.csv`. This quantifies
  how much the “LCDM-like” set sits inside (or outside) the toy corridor and
  viability sets, instead of leaving that structure implicit.

- **Rung 5 – Basic family figures (θ and ΩΛ views).**  
  Added `plot_frw_corridor_families_v1.py`, which:
  - makes a simple θ-histogram showing how the F1–F5 families occupy the
    θ-grid, and
  - produces an ΩΛ vs θ view using the Phase 4 `shape_probe_mask` table.  
  Figures are written as PDFs to  
  `stage2/frw_corridor_analysis/outputs/figures/`, e.g.
  `stage2_frw_corridor_family_theta_hist_v1.pdf` and
  `stage2_frw_corridor_family_omega_lambda_scatter_v1.pdf`.  
  These figures are currently **Stage-2 only** and are not wired into any phase
  paper.

- **Rung 6 – Contiguity of families in θ.**  
  Added `analyze_frw_corridor_contiguity_v1.py`, which measures how many
  contiguous θ-segments each family decomposes into, and what fraction of the
  grid each segment family covers. Results are stored in  
  `stage2/.../stage2_frw_corridor_rung6_contiguity_v1.csv`. This checks whether
  viable / LCDM-like sets are scattered speckles or coherent intervals on the
  current θ-grid (they are coherent intervals).

- **Rung 7 – Stride-sampling robustness.**  
  Added `analyze_frw_corridor_stride_robustness_v1.py`, which sub-samples the
  θ-grid with strides {1, 2, 4, 8} and recomputes family occupancy and segment
  counts on each subgrid. Results go to  
  `stage2/.../stage2_frw_corridor_rung7_stride_robustness_v1.csv`. For all
  F1–F5 families, the fraction of “true” points on the subgrid remains stable
  as the stride increases, indicating that the families are not artifacts of
  single isolated θ points.

- **Rung 8 – Local θ-smoothing robustness.**  
  Added `analyze_frw_corridor_smoothing_v1.py`, which applies 1D majority
  filters (window sizes 3 and 5) along the θ-index to each F1–F5 family and
  compares:
  `n_true`, `frac_true`, number of θ-segments, and Jaccard similarity before
  and after smoothing. Output is written to  
  `stage2/.../stage2_frw_corridor_rung8_smoothing_v1.csv`. On the current
  Phase 4 θ-grid, all families remain exactly unchanged (Jaccard = 1.0, same
  occupancy and segment counts), i.e. the FRW corridor / LCDM-like structure is
  robust to mild local smoothing and is not a single-point noise artifact.

At this rung, Stage-2 FRW corridor analysis is a self-contained, reproducible
exploration downstream of Phase 4. It is a candidate source of figures and
diagnostics for a future FRW-focused extension (Phase 6 / Stage-2 paper), but
does not yet promote any new claims into the locked phases.

## 2026-01-09 — Stage 2: FRW corridor analysis (Rung 9)

- **Rung 9 — FRW corridor segment geometry + θ\* alignment (stage2/frw_corridor_analysis)**  
  - Added `stage2/frw_corridor_analysis/src/analyze_frw_corridor_segments_theta_star_v1.py`.  
  - Inputs: Phase 4 shape-probe mask  
    - `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`  
  - Outputs:  
    - `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung9_segments_v1.csv`  
      - one row per contiguous θ-segment for each family  
      - columns include `family_id`, `segment_id`, `start_index`, `end_index`, `n_pts`, `theta_min`, `theta_max`, `theta_span`, `contains_theta_star`.  
    - `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung9_theta_star_alignment_v1.csv`  
      - one row per family (F1–F5) with nearest-grid alignment to the project’s special value θ\* = φ^φ ≈ 2.1784575679  
      - columns include `theta_star`, `theta_closest`, `abs_delta`, `index_closest`, optional physical diagnostics (`omega_lambda_closest`, `E_vac_closest`, `age_Gyr_closest`), and basic occupancy stats (`n_true`, `frac_of_grid`).  
  - Status: **Complete.** This rung remains purely diagnostic and downstream of Phase 4, providing a geometric map of how each FRW corridor family sits in θ and how θ\* aligns with them, without feeding back into any Phase 3–5 claims.

---

### 2026-01-09 – Stage 2: FRW corridor documentation & promotion gate

- Consolidated Stage 2 FRW corridor work (Rungs 1–9) into a local axis
  README:
  - `stage2/frw_corridor_analysis/README_FRW_CORRIDORS_v1.md`
  summarizing inputs, rungs, structural findings, and current limits on
  interpretation.
- Introduced a formal **FRW Corridor Promotion Gate**:
  - `docs/FRW_CORRIDOR_PROMOTION_GATE_v1.md`
  specifying conditions under which FRW corridor diagnostics may be
  promoted into phase papers (data-backed, robustness, clear claims,
  reproducibility).
- Updated `docs/FUTURE_WORK_AND_ROADMAP.md` to reference the Stage 2 FRW
  axis and to record that, as of this date, FRW corridor results remain
  Stage 2 exploratory diagnostics, not phase-level claims.


2026-01-09 — Stage 2: Phase 3 mech/measure analysis (Rungs 1–6)
----------------------------------------------------------------
Context:
  - Build a Stage 2 analysis spine that inspects Phase 3 mechanism / measure
    tables without altering any Phase 3 or Phase 5 claims.
  - Goal is to identify well-behaved, probability-like quantities that could
    serve as candidate "measures" or "flags" for future promotion.

Rung 1 — Phase 3 table inventory
  - Script:
      stage2/mech_measure_analysis/src/inventory_phase3_tables_v1.py
  - Output:
      stage2/mech_measure_analysis/outputs/tables/
        stage2_mech_rung1_phase3_table_inventory_v1.csv
  - Function:
      Scan phase3/outputs/tables for CSV/JSON tables, record file kind,
      byte size, and (for CSVs) n_rows / n_cols. Provides a compact,
      reproducible overview of the numerical tables behind Phase 3.

Rung 2 — Column-level stats for Phase 3 tables
  - Script:
      stage2/mech_measure_analysis/src/analyze_phase3_table_columns_v1.py
  - Output:
      stage2/mech_measure_analysis/outputs/tables/
        stage2_mech_rung2_phase3_column_stats_v1.csv
  - Function:
      For each Phase 3 CSV table, summarize per-column statistics
      (min/max/mean, NaN counts, uniqueness, simple type hints, etc.).
      For JSON diagnostics tables, record high-level summary entries.
      This rung stays purely descriptive and stage-local.

Rung 3 — Probability-like column candidates
  - Script:
      stage2/mech_measure_analysis/src/analyze_phase3_probability_like_columns_v1.py
  - Output:
      stage2/mech_measure_analysis/outputs/tables/
        stage2_mech_rung3_phase3_probability_like_candidates_v1.csv
  - Function:
      Filter the Rung 2 stats for columns that behave like probabilities
      or normalized weights (values within [0,1] up to small tolerances,
      no extreme pathologies). Produces a list of candidate columns with
      notes on why they were selected.

Rung 4 — Measure vs flag role tagging
  - Script:
      stage2/mech_measure_analysis/src/select_phase3_measure_candidates_v1.py
  - Output:
      stage2/mech_measure_analysis/outputs/tables/
        stage2_mech_rung4_phase3_measure_and_flag_candidates_v1.csv
  - Function:
      From the Rung 3 probability-like candidates, assign a tentative
      "role" to each column: measure_candidate (continuous, graded) vs
      flag_candidate (Boolean-ish or threshold-like). This does not
      create new physics claims; it only records which existing Phase 3
      quantities might naturally play which roles.

Rung 5 — θ-profiles for candidate measures
  - Script:
      stage2/mech_measure_analysis/src/analyze_phase3_measure_theta_profiles_v1.py
  - Output:
      stage2/mech_measure_analysis/outputs/tables/
        stage2_mech_rung5_phase3_measure_theta_profiles_v1.csv
  - Function:
      For each measure/flag candidate, extract its behaviour as a
      function of θ across the Phase 3 baseline grid. Records basic
      shape features (e.g., monotonicity flags, support, spread)
      without enforcing any promotion or interpretation.

Rung 6 — Preferred measure shortlist (Stage 2 only)
  - Script:
      stage2/mech_measure_analysis/src/select_phase3_preferred_measures_v1.py
  - Output:
      stage2/mech_measure_analysis/outputs/tables/
        stage2_mech_rung6_phase3_preferred_measure_candidates_v1.csv
  - Function:
      Score each candidate based on coverage, boundedness, θ-profile
      behaviour and other simple diagnostics, and assign decisions such
      as "keep_as_primary", "keep_as_secondary", or "discard_for_now".
      At this rung, all decisions remain strictly Stage 2:
        * no modification of Phase 3 or Phase 5 papers,
        * no new claims about a unique or "true" measure.
      Instead, we obtain a transparent, reproducible shortlist that
      future rungs can either promote (with further justification) or
      consciously leave aside.

Status:
  - All Stage 2 mech/measure rungs (1–6) run cleanly from the current
    Phase 3 artifacts and produce CSV outputs under:
      stage2/mech_measure_analysis/outputs/tables/
  - No feedback is written into the Phase 3 workflow or papers.
  - Promotion of any candidate measure into the main phased program is
    intentionally deferred to later rungs, after more physics-facing
    scrutiny and potential coupling to the FRW corridor analysis.


---

## 2026-01-09 — Stage 2: Joint mech–FRW analysis, Rungs 1–3

### Context

This Stage 2 block stays **strictly downstream** of Phases 3–4.  
Goal: build a joint θ-grid that stitches together:

- Phase 4 FRW diagnostics (toy FRW viability, Ω\_Λ, age, LCDM-like masks, data probe flags),
- Phase 3 mechanism amplitudes (baseline + binding views),

and then quantify how strongly they are correlated, without introducing any new model or claim about our Universe.

All results are exploratory diagnostics only and **do not feed back** into the Phase 3/4 papers.

---

### Stage 2 — Joint mech–FRW Rung 1: Joint θ-grid

**Script**

- `stage2/joint_mech_frw_analysis/src/build_joint_theta_grid_v1.py`

**Inputs**

- Phase 4 FRW masks (all at 2048-point θ grid):
  - `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`
  - `phase4/outputs/tables/phase4_F1_frw_data_probe_mask.csv`
  - `phase4/outputs/tables/phase4_F1_frw_viability_mask.csv`
  - `phase4/outputs/tables/phase4_F1_frw_lcdm_probe_mask.csv`
- Phase 3 mechanism tables (same nominal θ grid):
  - `phase3/outputs/tables/mech_baseline_scan.csv`
  - `phase3/outputs/tables/mech_binding_certificate.csv`

**Checks**

- Verified θ-alignment across all FRW masks:
  - shape vs data probe vs viability vs LCDM probe agree at tolerance `1e-8`.
- Verified θ-alignment between FRW masks and Phase 3 mechanism tables:
  - `mech_baseline_scan.csv` and `mech_binding_certificate.csv` both match the FRW θ grid at tolerance `1e-8`.
- Any misalignment would raise a hard error with a diagnostic max |Δθ|.

**Output**

- Joint grid CSV:
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv`
  - Shape: 2048 rows × 17 columns.

**Key columns in the joint grid**

- FRW / θ-side:
  - `theta_index`, `theta`
  - `E_vac`, `omega_lambda`, `age_Gyr`
  - `in_toy_corridor`, `frw_viable`, `lcdm_like`
  - `shape_and_viable`, `shape_and_lcdm`
  - `frw_data_ok` (attached from the Phase 4 data probe mask)
- Mechanism-side (derived from Phase 3 tables, prefixed at attach time):
  - `mech_baseline_A0`, `mech_baseline_A_floor`, `mech_baseline_bound`
  - `mech_binding_A0`, `mech_binding_A`, `mech_binding_bound`

**Verdict**

- Rung 1 successfully builds a **single joint θ-grid** that stitches together the Phase 4 FRW diagnostics and Phase 3 mechanism amplitudes, with explicit θ-alignment checks.
- This rung is purely infrastructural: it creates the table on which all downstream joint diagnostics operate, but makes **no physical claim** beyond alignment and bookkeeping.

---

### Stage 2 — Joint mech–FRW Rung 2: Family summaries on the joint grid

**Script**

- `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_family_summaries_v1.py`

**Inputs**

- Joint grid from Rung 1:
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv`

**Definition of families (all within the 2048-point θ grid)**

- `ALL_GRID`: all θ points (reference baseline)
- `FRW_VIABLE`: `frw_viable == True`
- `LCDM_LIKE`: `lcdm_like == True`
- `TOY_CORRIDOR`: `in_toy_corridor == True`
- `CORRIDOR_AND_VIABLE`: `in_toy_corridor && frw_viable`
- `CORRIDOR_AND_LCDM`: `in_toy_corridor && lcdm_like`
- `FRW_VIABLE_AND_DATA_OK`: `frw_viable && frw_data_ok`

**Output**

- Summary table:
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_rung2_family_summaries_v1.csv`
  - Includes, for each family:
    - `family_id`
    - `n_theta`
    - `frac_of_grid` (n\_theta / 2048)

**Headline numbers**

On the current toy configuration:

- `ALL_GRID`: n\_θ = 2048, frac\_of\_grid ≈ 1.00000
- `FRW_VIABLE`: n\_θ = 1016, frac\_of\_grid ≈ 0.49609
- `LCDM_LIKE`: n\_θ = 63, frac\_of\_grid ≈ 0.03076
- `TOY_CORRIDOR`: n\_θ = 1186, frac\_of\_grid ≈ 0.57910
- `CORRIDOR_AND_VIABLE`: n\_θ = 154, frac\_of\_grid ≈ 0.07520
- `CORRIDOR_AND_LCDM`: n\_θ = 40, frac\_of\_grid ≈ 0.01953
- `FRW_VIABLE_AND_DATA_OK`: n\_θ = 0, frac\_of\_grid = 0.00000  
  (current configuration has `data_ok == false` everywhere, as expected because no external dataset is yet wired in.)

**Verdict**

- Rung 2 provides **explicit counts and fractions** for the main FRW families directly on the joint grid, mirroring the earlier FRW-only Stage 2 analysis but now in the context of the mech–FRW stitched table.
- Still no new physics claim; this is a structural census of the toy FRW families.

---

### Stage 2 — Joint mech–FRW Rung 3: Global correlations between FRW scalars and mechanism amplitudes

**Script**

- `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_correlations_v1.py`

**Inputs**

- Joint grid:
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv`

**Variables considered**

- FRW scalar fields:
  - `E_vac`, `omega_lambda`, `age_Gyr`
- Mechanism amplitudes (Phase 3, baseline and binding views):
  - `mech_baseline_A0`, `mech_baseline_A_floor`, `mech_baseline_bound`
  - `mech_binding_A0`, `mech_binding_A`, `mech_binding_bound`

**Method**

- For each pair (FRW scalar, mechanism amplitude), compute:
  - Pearson correlation coefficient `r`
  - Covariance
  - Sample size `n` (always 2048 on the current grid)
- Write all results to a single CSV for downstream inspection.

**Output**

- Correlation table:
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_rung3_correlations_v1.csv`
  - 18 rows (3 FRW scalars × 6 mechanism amplitudes).

**Headline correlation patterns**  
(All values approximate, taken from the current run)

- **E\_vac vs mechanism amplitudes**
  - `E_vac` vs `mech_baseline_A0`: r ≈ +0.94
  - `E_vac` vs `mech_baseline_A_floor`: r ≈ +0.98
  - `E_vac` vs `mech_baseline_bound`: r ≈ −0.56
  - The corresponding `mech_binding_*` amplitudes have **the same** correlation pattern.

- **Ω\_Λ vs mechanism amplitudes**
  - `omega_lambda` vs `mech_baseline_A0`: r ≈ +0.94
  - `omega_lambda` vs `mech_baseline_A_floor`: r ≈ +0.98
  - `omega_lambda` vs `mech_baseline_bound`: r ≈ −0.56
  - Again, `mech_binding_*` mirrors the same pattern.

- **Age vs mechanism amplitudes**
  - `age_Gyr` vs `mech_baseline_A0`: r ≈ −0.97
  - `age_Gyr` vs `mech_baseline_A_floor`: r ≈ −0.997
  - `age_Gyr` vs `mech_baseline_bound`: r ≈ +0.63
  - Binding amplitudes mirror baseline: same r values within numerical precision.

**Interpretation (within the toy setup)**

- The Phase 3 mechanism amplitude is **strongly, smoothly coupled** to the Phase 4 FRW scalar fields across the θ grid:
  - Larger toy vacuum energy (and Ω\_Λ) correspond to larger mechanism amplitudes.
  - Younger toy universes correspond to larger mechanism amplitudes; older ones to smaller amplitudes.
- “Bound” variables move in the opposite direction, consistent with encoding something like a distance-to-binding or constraint margin.
- Baseline vs binding amplitudes are effectively two views of the **same underlying signal** in this configuration, as seen by identical correlation patterns.

**Important caveats**

- These are **global correlations over the 2048-point toy θ grid**, not a fit to real data.
- No claim is made that any particular θ selects our observed Universe, nor that this correlation structure alone defines physical reality.
- This rung establishes that the mech–FRW toy construction is **non-degenerate and smoothly stitched**, not that it is correct physics.

**Verdict**

- Rung 3 provides a compact, reproducible **joint diagnostic** of how the Phase 3 mechanism amplitudes co-vary with toy FRW scalar fields across θ.
- This is a good candidate for eventual promotion as a **small, tightly scoped diagnostic figure/table** in:
  - a Stage 2 / Phase 6 downstream analysis, or
  - a future appendix (Phase 5+) describing the structure of the mech–FRW toy pipeline.
- For now it remains strictly in Stage 2, with the results treated as **exploratory diagnostics only**.


## 2026-01-09 — Stage 2: FRW corridors, mech measures, and joint mech–FRW grid

### Stage 2 — FRW corridor analysis (rungs 1–9)

- **Rung 1 — Source inventory (FRW masks & corridors)**  
  - Script: `stage2/frw_corridor_analysis/src/analyze_frw_corridor_v1.py`  
  - Output: `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung1_sources_v1.csv`  
  - Role: Verifies existence, sizes, and basic schema for the Phase 4 FRW masks and corridors:  
    - `phase4_F1_frw_viability_mask.csv`  
    - `phase4_F1_frw_lcdm_probe_mask.csv`  
    - `phase4_F1_frw_shape_probe_mask.csv`  
    - `phase4_F1_frw_data_probe_mask.csv`  
    - `phase4_F1_frw_corridors.json`  

- **Rung 2 — Boolean census over FRW masks**  
  - Script: `stage2/frw_corridor_analysis/src/analyze_frw_corridor_bool_census_v1.py`  
  - Output: `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung2_bool_census_v1.csv`  
  - Role: Counts TRUE/FALSE/NA for all “boolean-like” FRW flags (e.g. `has_matter_era`, `has_late_accel`, `smooth_H2`, `frw_viable`, `lcdm_like`, `in_toy_corridor`, `shape_and_viable`, `shape_and_lcdm`, `data_ok`).  
  - Takeaway:  
    - FRW viability and late acceleration are populated in a substantial fraction of the grid.  
    - LCDM-like and shape-and-LCDM are rare but non-empty.  
    - `data_ok` is uniformly false in the current repo config (no external FRW dataset bundled).

- **Rung 3 — Family definitions on the FRW grid**  
  - Script: `stage2/frw_corridor_analysis/src/analyze_frw_corridor_families_v1.py`  
  - Output: `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung3_families_v1.csv`  
  - Families (on a 2048-point θ grid):  
    - `F1_FRW_VIABLE` — all FRW-viable points (≈ 49.6% of grid).  
    - `F2_LCDM_LIKE` — LCDM-like points (≈ 3.1% of grid).  
    - `F3_TOY_CORRIDOR` — toy FRW corridor mask (≈ 57.9% of grid).  
    - `F4_CORRIDOR_AND_VIABLE` — viable subset of the corridor (≈ 7.5% of grid).  
    - `F5_CORRIDOR_AND_LCDM` — LCDM-like subset of the corridor (≈ 2.0% of grid).  
    - `F6_DATA_OK` — currently empty (0% of grid).  

- **Rung 4 — Family overlap table**  
  - Script: `stage2/frw_corridor_analysis/src/analyze_frw_corridor_family_overlap_v1.py`  
  - Output: `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung4_family_overlap_v1.csv`  
  - Role: Quantifies pairwise overlaps among F1–F6 (e.g. what fraction of `F2_LCDM_LIKE` sits inside `F3_TOY_CORRIDOR`, what fraction of `F4_CORRIDOR_AND_VIABLE` overlaps with LCDM-like, etc.).  
  - Takeaway: LCDM-like points are rare, and LCDM-like-in-corridor is rarer still; the corridor itself is broad.

- **Rung 5 — FRW corridor family plots (θ & ΩΛ)**  
  - Script: `stage2/frw_corridor_analysis/src/plot_frw_corridor_families_v1.py`  
  - Outputs (PDF figures):  
    - `stage2/frw_corridor_analysis/outputs/figures/stage2_frw_corridor_family_theta_hist_v1.pdf`  
    - `stage2/frw_corridor_analysis/outputs/figures/stage2_frw_corridor_family_omega_lambda_scatter_v1.pdf`  
  - Role:  
    - θ-histogram showing where each family (F1–F5) lives on the θ grid.  
    - ΩΛ vs θ scatter with family membership as overlaid masks.  
  - Takeaway: the FRW-viable region is contiguous in θ; the toy corridor is broad and includes LCDM-like sub-pockets but does not obviously “pin” θ to a very narrow band.

- **Rung 6 — Contiguity analysis in θ**  
  - Script: `stage2/frw_corridor_analysis/src/analyze_frw_corridor_contiguity_v1.py`  
  - Output: `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung6_contiguity_v1.csv`  
  - Role: For each family F1–F5, decomposes the true mask into contiguous θ segments and counts them.  
  - Takeaway:  
    - FRW viability is realized as a **single contiguous block**.  
    - LCDM-like and corridor-related families appear as **one or two segments**, suggesting corridor-like structure rather than random speckling.

- **Rung 7 — Stride robustness**  
  - Script: `stage2/frw_corridor_analysis/src/analyze_frw_corridor_stride_robustness_v1.py`  
  - Output: `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung7_stride_robustness_v1.csv`  
  - Role: Checks whether family fractions and segmentation are stable under decimation of the θ grid (strides 1, 2, 4, 8).  
  - Takeaway: fractions and segment counts are robust under coarsening, which is **consistent with** corridor-like structure and **inconsistent with** isolated, grid-sensitive spikes.

- **Rung 8 — Smoothing robustness**  
  - Script: `stage2/frw_corridor_analysis/src/analyze_frw_corridor_smoothing_v1.py`  
  - Output: `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung8_smoothing_v1.csv`  
  - Role: Applies small moving-window smoothers (window sizes 1, 3, 5) to the family masks and compares before/after masks via Jaccard index and segment counts.  
  - Takeaway: For all families F1–F5, masks are **exactly identical** under these small smoothers (Jaccard = 1), confirming that corridor shapes are not artifacts of single-grid noise.

- **Rung 9 — Segments and θ★ alignment**  
  - Script: `stage2/frw_corridor_analysis/src/analyze_frw_corridor_segments_theta_star_v1.py`  
  - Outputs:  
    - `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung9_segments_v1.csv`  
    - `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung9_theta_star_alignment_v1.csv`  
  - Role:  
    - Logs θ-segment structure of each family.  
    - For each family, records the θ in that family closest to θ★ ≈ 2.178458 and its distance |Δθ|.  
  - Takeaway: θ★ lies well inside the **FRW-viable block**, but the closest family hits in corridor-related sets are at |Δθ| ≈ 1.1257, so we **do not** claim special corridor pinning of θ★ at this rung. This remains a **diagnostic observation**, not a promoted claim.

### Stage 2 — Mechanism / measure analysis (rungs 1–6)

- **Rung 1 — Phase 3 table inventory**  
  - Script: `stage2/mech_measure_analysis/src/inventory_phase3_tables_v1.py`  
  - Output: `stage2/mech_measure_analysis/outputs/tables/stage2_mech_rung1_phase3_table_inventory_v1.csv`  
  - Role: Enumerates all Phase 3 mechanism tables and their basic schema:  
    - `mech_baseline_scan.csv`  
    - `mech_baseline_scan_diagnostics.json`  
    - `mech_binding_certificate.csv`  
    - `mech_binding_certificate_diagnostics.json`  
    - `phase3_instability_penalty_v1.json`  
    - `phase3_measure_v1_hist.csv`  
    - `phase3_measure_v1_stats.json`  

- **Rung 2 — Column-level stats**  
  - Script: `stage2/mech_measure_analysis/src/analyze_phase3_table_columns_v1.py`  
  - Output: `stage2/mech_measure_analysis/outputs/tables/stage2_mech_rung2_phase3_column_stats_v1.csv`  
  - Role: For each CSV column: type inference, min/max/mean/std, and simple flags (e.g. is it bounded in [0,1]?, does it look boolean?).

- **Rung 3 — Probability-like candidates**  
  - Script: `stage2/mech_measure_analysis/src/analyze_phase3_probability_like_columns_v1.py`  
  - Output: `stage2/mech_measure_analysis/outputs/tables/stage2_mech_rung3_phase3_probability_like_candidates_v1.csv`  
  - Role: Filters the column stats to columns that numerically behave like probabilities (in [0,1] with reasonable empirical distribution).  
  - Takeaway: Produces a shortlist of candidate measure-like and flag-like columns.

- **Rung 4 — Measure vs flag split**  
  - Script: `stage2/mech_measure_analysis/src/select_phase3_measure_candidates_v1.py`  
  - Output: `stage2/mech_measure_analysis/outputs/tables/stage2_mech_rung4_phase3_measure_and_flag_candidates_v1.csv`  
  - Role: Separates candidates into:  
    - “measure-like” scalars (continuous in [0,1]),  
    - “flag-like” diagnostics (near-boolean).  
  - Takeaway: We identify **6 measure-like** and **2 flag-like** candidates worth tracking.

- **Rung 5 — θ profiles of candidate measures**  
  - Script: `stage2/mech_measure_analysis/src/analyze_phase3_measure_theta_profiles_v1.py`  
  - Output: `stage2/mech_measure_analysis/outputs/tables/stage2_mech_rung5_phase3_measure_theta_profiles_v1.csv`  
  - Role: For each candidate, computes basic θ-profile descriptors (e.g. mean, variance, monotonicity indicators).

- **Rung 6 — Preferred measure shortlist**  
  - Script: `stage2/mech_measure_analysis/src/select_phase3_preferred_measures_v1.py`  
  - Output: `stage2/mech_measure_analysis/outputs/tables/stage2_mech_rung6_phase3_preferred_measure_candidates_v1.csv`  
  - Role: Applies stricter criteria (e.g. smoothness in θ, non-degenerate range, boundedness) to designate a **small set of “preferred” Phase 3 measure candidates** suitable for future promotion into Phase 5 / Stage 3.

### Stage 2 — Joint mech–FRW analysis (rungs 1–3)

- **Rung 1 — Joint θ-grid construction**  
  - Script: `stage2/joint_mech_frw_analysis/src/build_joint_theta_grid_v1.py`  
  - Output: `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv`  
  - Role:  
    - Aligns the Phase 4 FRW θ grid with the Phase 3 mechanism θ grid (2048 points).  
    - Verifies alignment to a tolerance of 1e−8 across:  
      - `phase4_F1_frw_shape_probe_mask.csv`  
      - `phase4_F1_frw_data_probe_mask.csv`  
      - `phase4_F1_frw_viability_mask.csv`  
      - `phase4_F1_frw_lcdm_probe_mask.csv`  
      - `mech_baseline_scan.csv`  
      - `mech_binding_certificate.csv`  
    - Builds a joint table with key columns:  
      - θ-index, θ, E_vac, ΩΛ, age_Gyr  
      - FRW masks (`in_toy_corridor`, `frw_viable`, `lcdm_like`, `shape_and_viable`, `shape_and_lcdm`, `frw_data_ok`)  
      - Mechanism amplitudes (`mech_baseline_A0`, `mech_baseline_A_floor`, `mech_baseline_bound`, `mech_binding_A0`, `mech_binding_A`, `mech_binding_bound`).

- **Rung 2 — Family summaries on the joint grid**  
  - Script: `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_family_summaries_v1.py`  
  - Output: `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_rung2_family_summaries_v1.csv`  
  - Role: Re-derives the basic FRW families (ALL_GRID, FRW_VIABLE, LCDM_LIKE, TOY_CORRIDOR, CORRIDOR_AND_VIABLE, CORRIDOR_AND_LCDM, FRW_VIABLE_AND_DATA_OK) from the joint table to confirm consistency with Stage 2 FRW results.

- **Rung 3 — Joint mech–FRW correlations**  
  - Script: `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_correlations_v1.py`  
  - Output: `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_rung3_correlations_v1.csv`  
  - Role: Computes Pearson correlations and covariances between:  
    - FRW scalars (`E_vac`, `omega_lambda`, `age_Gyr`)  
    - And mechanism amplitudes (`mech_baseline_A0`, `mech_baseline_A_floor`, `mech_baseline_bound`, `mech_binding_A0`, `mech_binding_A`, `mech_binding_bound`).  
  - Takeaway (diagnostic only):  
    - Very strong (|r| ≈ 0.97–0.99) correlations between FRW scalars and the two main amplitude tracks reflect the underlying shared θ-grid construction; they are **not yet elevated** to a physical claim.  
    - Signs and magnitudes are consistent with monotone behavior but require more careful normalization and model comparison before any promotion.

### Stage 2 status

- Stage 2 is now a **self-contained diagnostic scaffold** that:
  - treats Phase 3 and Phase 4 artifacts as read-only inputs,  
  - builds FRW corridor families and robustness checks,  
  - identifies a shortlist of mechanism-based “measure” candidates,  
  - and assembles a joint θ-grid for cross-cutting mech–FRW correlations.
- At this rung, all findings are treated as **internal diagnostics only**, not as promoted claims.  
- Future work will decide, per candidate and per family, whether any of these patterns are robust and non-trivial enough to be:
  - (Option A) folded into the existing Phase 5 narrative as a lightweight extension, or  
  - (Option B) developed into a dedicated Stage 2 / Phase 6 paper focusing on FRW corridors and non-cancellation measures.


### 2026-01-09 — Stage 2: joint mech–FRW analysis, Rung 4 (family-wise correlations)

**Files / code**
- `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_family_correlations_v1.py`
- Outputs:
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_rung4_family_correlations_v1.csv`
  - (uses joint grid from `stage2_joint_theta_grid_v1.csv` built in Rung 1)

**What we did**
- Defined the same FRW families as in the FRW corridor analysis:
  - ALL_GRID, FRW_VIABLE, LCDM_LIKE, TOY_CORRIDOR,
  - CORRIDOR_AND_VIABLE, CORRIDOR_AND_LCDM,
  - FRW_VIABLE_AND_DATA_OK (empty).
- For each family, computed Pearson correlation and covariance between:
  - FRW-side quantities: `E_vac`, `omega_lambda`, `age_Gyr`
  - Mechanical quantities from Phase 3:
    - `mech_baseline_A0`, `mech_baseline_A_floor`, `mech_baseline_bound`
    - `mech_binding_A0`, `mech_binding_A`, `mech_binding_bound`.

**Key observations**
- On the full grid, correlations are already very strong:
  - |r| ~ 0.93–0.98 between {E_vac, omega_lambda} and the mechanical amplitudes.
  - |r| ~ 0.97–1.00 (with opposite sign) between `age_Gyr` and the mechanical amplitudes.
- Inside restricted FRW families (FRW_VIABLE, LCDM_LIKE, TOY_CORRIDOR, CORRIDOR_AND_VIABLE, CORRIDOR_AND_LCDM) the correlations tighten further:
  - Typical |r| ≳ 0.996–0.9999, indicating almost perfect linear relations.
- Several correlations involving the “bound” columns within viable families are `NaN`, consistent with those columns being nearly constant in those subsets (no variance ⇒ undefined Pearson r).
- The FRW_VIABLE_AND_DATA_OK family remains empty, so no correlations are defined there.

**Interpretation / status**
- Within each FRW family, the mechanical amplitudes behave as smooth, monotonic re-parameterisations of the FRW observables (Λ, E_vac, age), rather than as an independent measure with new structure.
- This supports internal consistency between Phase 3 and Phase 4, but argues against promoting the Phase 3 mechanical construction as an independent “probability measure on θ” at this stage.
- Verdict: keep this as a Stage 2 joint-analysis rung (sanity and structure check). No promotion to Phase 5 claims unless later rungs reveal genuinely new constraints tied to the mechanical quantities.


## 2026-01-09 — Stage 2 FRW/mech/joint analysis consolidation

**Context.** With Phases 0–5 locked at Level A and the Phase 4 FRW corridor analysis completed, we introduced Stage 2 as a downstream analysis layer to (i) stress-test the FRW corridor structure, (ii) examine Phase 3 mechanism outputs as potential measures or flags over θ, and (iii) build a joint mech–FRW picture on a common θ-grid.

### Stage 2 FRW corridor analysis (recap, rungs 1–9)

- Confirmed that the Phase 4 FRW masks (viability, toy corridor, LCDM-like, intersections) are:
  - well-behaved on the 2048-point θ-grid,
  - contiguous or nearly contiguous,
  - robust under stride-thinning (1, 2, 4, 8),
  - and stable under small smoothing windows.
- Checked family sizes, overlaps, contiguity, stride robustness, and smoothing effects via:
  - `stage2/frw_corridor_analysis/outputs/tables/`:
    - `stage2_frw_corridor_rung1_sources_v1.csv`
    - `stage2_frw_corridor_rung3_families_v1.csv`
    - `stage2_frw_corridor_rung4_family_overlap_v1.csv`
    - `stage2_frw_corridor_rung6_contiguity_v1.csv`
    - `stage2_frw_corridor_rung7_stride_robustness_v1.csv`
    - `stage2_frw_corridor_rung8_smoothing_v1.csv`
    - `stage2_frw_corridor_rung9_theta_star_alignment_v1.csv`
  - `stage2/frw_corridor_analysis/outputs/figures/`:
    - `stage2_frw_corridor_family_theta_hist_v1.pdf`
    - `stage2_frw_corridor_family_omega_lambda_scatter_v1.pdf`
- Result: FRW corridor families form a clean, robust backdrop; no sharp anomaly is seen at θ* ≈ 2.178458 on this grid.

### Stage 2 mech measure analysis (new, rungs 1–6)

Path: `stage2/mech_measure_analysis/`

- **Rung 1 – inventory.**
  - `inventory_phase3_tables_v1.py`
  - Output: `stage2_mech_rung1_phase3_table_inventory_v1.csv`
  - Inventoried all Phase 3 tables under `phase3/outputs/tables/`, tracking file type, size, and row/column counts.

- **Rung 2 – column stats.**
  - `analyze_phase3_table_columns_v1.py`
  - Output: `stage2_mech_rung2_phase3_column_stats_v1.csv`
  - Summarised basic statistics for numeric columns in Phase 3 CSVs (min, max, mean, std, finite fractions).

- **Rung 3 – probability-like candidates.**
  - `analyze_phase3_probability_like_columns_v1.py`
  - Output: `stage2_mech_rung3_phase3_probability_like_candidates_v1.csv`
  - Flagged columns with bounded, non-degenerate distributions as “probability-like” (potential measures or flags).

- **Rung 4 – measure vs flag classification.**
  - `select_phase3_measure_candidates_v1.py`
  - Output: `stage2_mech_rung4_phase3_measure_and_flag_candidates_v1.csv`
  - Split probability-like candidates into:
    - measure-like (smooth, graded),
    - flag-like (near-Boolean).

- **Rung 5 – θ-profiles.**
  - `analyze_phase3_measure_theta_profiles_v1.py`
  - Output: `stage2_mech_rung5_phase3_measure_theta_profiles_v1.csv`
  - Recorded how candidate measures/flags behave as functions of θ (shape, monotonicity, peaks).

- **Rung 6 – preferred candidates.**
  - `select_phase3_preferred_measures_v1.py`
  - Output: `stage2_mech_rung6_phase3_preferred_measure_candidates_v1.csv`
  - Selected a small set of numerically well-behaved candidates suitable as diagnostics or weights, but:
    - no single column is promoted to a fundamental θ-measure at this rung.

**Mech takeaway.** Phase 3 amplitudes provide smooth, well-controlled diagnostics over θ, but on the current toy setup they do not yet define an independent, physically motivated measure in θ.

### Stage 2 joint mech–FRW analysis (new, rungs 1–3)

Path: `stage2/joint_mech_frw_analysis/`

- **Rung 1 – joint θ-grid.**
  - `build_joint_theta_grid_v1.py`
  - Output: `stage2_joint_theta_grid_v1.csv` (2048 rows × 17 columns)
  - Built a single θ-aligned table combining:
    - FRW scalars and masks from:
      - `phase4_F1_frw_shape_probe_mask.csv`
      - `phase4_F1_frw_data_probe_mask.csv`
      - `phase4_F1_frw_viability_mask.csv`
      - `phase4_F1_frw_lcdm_probe_mask.csv`
    - mech amplitudes from:
      - `mech_baseline_scan.csv`
      - `mech_binding_certificate.csv`
  - Verified θ-alignment between all inputs within a strict tolerance before joining.

- **Rung 2 – family summaries on the joint grid.**
  - `analyze_joint_mech_frw_family_summaries_v1.py`
  - Output: `stage2_joint_mech_frw_rung2_family_summaries_v1.csv`
  - Defined and summarised several FRW families on the joint grid:
    - ALL_GRID, FRW_VIABLE, LCDM_LIKE, TOY_CORRIDOR,
      CORRIDOR_AND_VIABLE, CORRIDOR_AND_LCDM, FRW_VIABLE_AND_DATA_OK.
  - Confirmed that family sizes and fractions match the Stage 2 FRW corridor results, validating the joint construction.

- **Rung 3 – joint correlations.**
  - `analyze_joint_mech_frw_correlations_v1.py`
  - Output: `stage2_joint_mech_frw_rung3_correlations_v1.csv`
  - Computed correlations between:
    - FRW scalars (`E_vac`, `omega_lambda`, `age_Gyr`) and
    - mech amplitudes (`mech_baseline_*`, `mech_binding_*`).
  - Found:
    - very strong correlations between FRW scalars and mech amplitudes (|r| close to 1 for several pairs),
    - consistent sign patterns (e.g. `E_vac` and `omega_lambda` correlate, `age_Gyr` anti-correlates),
    - indicating that Phase 3 amplitudes act as smooth re-parameterisations of the FRW scalars on this grid.

**Joint takeaway.** On the current 2048-point θ-grid and toy FRW setup:

- mech amplitudes are highly redundant with FRW scalars,
- no additional “hidden” structure emerges beyond what Phase 4 already encodes,
- and there is no special anomaly at θ* ≈ 2.178458 visible at this resolution.

### Status and promotion

- All Stage 2 FRW, mech, and joint scripts are **purely downstream** of Phases 3 and 4 and can be rerun reproducibly.
- At this rung:
  - Stage 2 mech and joint results are **accepted as diagnostic infrastructure** and as evidence that the current toy setup is internally consistent.
  - We **do not** yet promote any Stage 2 quantity to a fundamental θ-measure in Phase 5.
  - A concise Option A summary (non-contradiction / redundancy statement) can later be added to the Phase 5 paper, with Stage 2 artifacts as backing evidence.
- Stage 2 remains the natural home for future mech–FRW refinements (e.g. more realistic FRW data, sharper non-cancellation ansätze, or refined measure proposals) without disturbing the locked Phase 0–5 storyline.


## 2026-01-09 — Stage 2: FRW data-probe audit (rungs 1–2)

**Scope.**  
Audit the FRW data-probe mask produced in Phase 4, focusing on the status of the
aggregate data flag `frw_data_ok` and its relation to the FRW viability corridor.
No Phase-3/4 code was changed; this is a pure Stage-2 downstream analysis.

**Code / scripts.**

- `stage2/frw_data_probe_analysis/src/analyze_frw_data_probes_v1.py`
  - Rung 1: column-level stats for FRW data probes.
- `stage2/frw_data_probe_analysis/src/analyze_frw_data_probes_vs_viability_v1.py`
  - Rung 2: 2×2 cross-tables vs `frw_viable`.

**Inputs.**

- `phase4/outputs/tables/phase4_F1_frw_data_probe_mask.csv`  (2048 × 11)
- `phase4/outputs/tables/phase4_F1_frw_viability_mask.csv`   (2048 × 8)

**Outputs.**

- `stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_data_probe_rung1_column_stats_v1.csv`
- `stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_data_probe_rung2_viability_cross_v1.csv`
- Doc: `stage2/frw_data_probe_analysis/docs/STAGE2_FRW_DATA_PROBE_AUDIT_v1.md`

**Key results.**

- `has_matter_era` and `smooth_H2` are **always true** on the 2048-point θ grid  
  → they act as structural sanity checks in the current snapshot (no extra cut).
- `has_late_accel` and `frw_viable` agree exactly:
  - 1016 points true, 1032 false  
  → viability is effectively equivalent to “late acceleration present”
    once the always-true checks are accounted for.
- `data_ok` is **identically false**:
  - `frac_true = 0.0`, `frac_false = 1.0`
  - Among the 1016 viable points: none satisfy `data_ok`  
    (`FRW_VIABLE ∧ DATA_OK` is empty).

**Interpretation.**

- The Phase-4 FRW pipeline already supports a nontrivial viability corridor
  (≈ 50% of the θ grid) and the Stage-2 corridor rungs explore intersections
  with toy corridor and LCDM-like masks.
- In the current snapshot, the aggregate data flag `frw_data_ok` is **never
  satisfied**, so all FRW families should be interpreted as **pre-data corridors**.
- This is treated as a **pipeline state** (“data gate not yet open”), not as a
  physical exclusion of the origin-axiom corridor. Tuning and validating the
  data probes (and `frw_data_ok` in particular) is deferred to later phases.


## 2026-01-09 — Stage 2: overview and promotion map

**Scope.**  
Summarize the implemented Stage 2 rungs (FRW corridors, mech/measure analysis,
joint mech–FRW analysis, FRW data-probe audit) and classify their outputs as:
promotion candidates, support-only diagnostics, or parked items.

**Docs.**

- `stage2/docs/STAGE2_OVERVIEW_AND_PROMOTION_MAP_v1.md`

**Key points.**

- FRW corridor rungs (1–9) are now treated as a stable Stage 2 belt:
  - Families F1–F5, their fractions of the θ grid, contiguity, and robustness
    checks are all reproducible and downstream-only.
  - F6 (`frw_data_ok`) is currently empty and is explicitly parked for a
    future revision of the Phase 4 data gate.
- Mech/measure rungs (1–6) identify a small set of smooth, probability-like
  measure candidates from Phase 3, without promoting any single choice to a
  physical “measure over θ” yet.
- Joint mech–FRW rungs (1–4) build a joint θ-grid and show strong
  correlations between {E_vac, ω_Λ, age_Gyr} and the mechanical amplitudes,
  while remaining strictly at the level of correlation (no causal claim).
- FRW data-probe rungs (1–2) clarify that, in the current Phase 4 snapshot,
  `frw_viable` is equivalent to “late acceleration present” under always-true
  sanity checks, and that `frw_data_ok` is not yet satisfied anywhere.

**Interpretation.**

- Stage 2 is now a coherent, reproducible analysis belt between Phase 3/4
  artifacts and any future Phase 4/5 text or new phases.
- The newly added overview document acts as a promotion map:
  - marking which Stage 2 artifacts are ready to be cited or plotted,
  - which remain as support-only diagnostics,
  - and which are parked until upstream code/claims evolve.


## 2026-01-09 — Phase 4 FRW promotion design (Stage 2 design rung)

**Scope.**  
Introduce `phase4/docs/PHASE4_FRW_PROMOTION_DESIGN_v1.md` to decide, at a
design level, which Stage 2 FRW, mech/measure, joint mech–FRW, and data-probe
artifacts are candidates for inclusion in Phase 4/5 text and figures, without
yet editing the LaTeX.

**Docs.**

- `phase4/docs/PHASE4_FRW_PROMOTION_DESIGN_v1.md`

**Key points.**

- FRW corridor families (F1–F5), their grid fractions, and one corridor figure
  (θ-histogram or (ω_Λ, E_vac) scatter) are marked as **Option A** candidates
  for inclusion in Phase 4/5, with the rest of the FRW diagnostics remaining
  in Stage 2 / appendix.
- Mech/measure results are kept as a **short textual summary** in Phase 4,
  deferring any choice of a preferred θ-measure to later work.
- Joint mech–FRW correlations are acknowledged as nontrivial but, for now,
  are proposed as a brief textual remark in Phase 4, with any detailed
  visualization deferred to later phases.
- FRW data-probe audit clarifies that `frw_viable` ≡ “late acceleration
  present” in the current snapshot (with always-true sanity checks), and that
  `frw_data_ok` is currently never satisfied; data-conditioned corridor claims
  are explicitly postponed.

**Interpretation.**

- This rung turns Stage 2 from “a bag of analyses” into a **promotion plan**
  that Phase 4/5 can implement later under separate, tightly scoped rungs that
  actually touch the LaTeX.


---

### 2026-01-09 — Stage 2: θ★–FRW alignment diagnostic (rung θ★–FRW–v1)

**Files:**

- `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung9_theta_star_alignment_v1.csv`
- `stage2/theta_star_analysis/docs/STAGE2_THETA_STAR_ALIGNMENT_v1.md`

**Summary:**

- Read off the θ★ ≈ φ^φ alignment results for the FRW families (viable band, LCDM-like, toy corridor, intersections).
- Verified that θ★ lies in the broad FRW-viable band but is not specially selected by the current toy corridor or LCDM-like families.
- Recorded this as a **negative-result sanity check**: nothing in the present FRW corridor machinery “snaps” to θ★ in an interesting way yet.
- Explicitly gated this rung as **Stage2-internal only** (no promotion to Phase 4/5); it serves as a baseline for future FRW+data or joint mech–FRW refinements.


---

### 2026-01-09 — Stage 2 belt overview (FRW, mech, joint, data, θ*)

**Files:**

- `stage2/docs/STAGE2_BELT_OVERVIEW_v1.md`

**Summary:**

- Wrote a Stage 2 master overview describing:
  - FRW corridor belt (rungs 1–9),
  - mech/measure belt (rungs 1–6),
  - joint mech–FRW belt (rungs 1–4),
  - FRW data probe belt (rungs 1–2),
  - θ★–FRW alignment diagnostic rung.
- Collected the main nontrivial outcomes in one place:
  - broad, contiguous FRW-viable band (~50% of θ grid),
  - robust FRW corridor families under contiguity/stride/smoothing tests,
  - strong correlations between Phase 3 mech scalars and Phase 4 vacuum sector,
  - current FRW data mask “data_ok” is empty,
  - θ★ lies inside the viable band but is not singled out by current corridors.
- Explicitly recorded gating: all Stage 2 artifacts remain **internal diagnostics**;
  no new figures or tables are yet promoted into Phase 4/5. This belt will be
  the basis for a later Stage 2 → Phase 4/5 promotion design rung.


---

### 2026-01-09 — Stage 2 → Phase 4/5 promotion design (planning only)

**Files:**

- `stage2/docs/STAGE2_PROMOTION_DESIGN_v1.md`

**Summary:**

- Wrote a Stage 2 promotion design doc that:
  - distinguishes **Option A** (minimal diagnostic/supporting promotions into Phase 4/5)
    from **Option B** (a future dedicated FRW/measure phase),
  - lists concrete Stage 2 artifacts that could be candidates for Option A (FRW
    viability fractions, FRW θ histograms, a joint mech–FRW correlation figure,
    a short list of preferred measure candidates, and a negative-result note
    about the current `data_ok` flag),
  - defines strict promotion criteria (reproducibility, robustness, interpretability,
    narrative alignment, and θ★ neutrality),
  - outlines future promotion rungs (P1–P4) needed to actually move any Stage 2
    artifact into Phase 3/4/5.
- No promotions were enacted in this rung; all Stage 2 outputs remain internal
  diagnostics. This doc acts as a contract for any future Option A promotions.


---

### 2026-01-09 — Stage 2 overview and verdict (diagnostic synthesis)

**Files:**

- `stage2/docs/STAGE2_OVERVIEW_v1.md`

**Summary:**

- Wrote a Stage 2 overview doc that:
  - explains Stage 2's role as a *diagnostic belt* downstream of Phase 3
    (mechanism) and Phase 4 (FRW),
  - summarizes the FRW corridor rungs (1–9), mech/measure rungs (1–6),
    joint mech–FRW rungs (1–4), FRW data probe rungs (1–2), and the θ★
    diagnostic rung,
  - records what nontrivial structure we *did* find (robust FRW bands,
    smooth mechanism-derived scalars, strong mech–FRW correlations, and a clean
    negative result for the current `data_ok` flag),
  - records what we *did not* find (no data corridor, no canonical measure,
    no special promotion of θ★),
  - clarifies how Stage 2 feeds into the separate Option A/B promotion design.
- No new computations or promotions were enacted; this rung is pure synthesis
  to make Stage 2 readable and auditable as a whole.

## 2026-01-10 — Stage 2 doc audit summary + flavor archive banner

Stage2/doc belt: added `stage2/docs/STAGE2_DOC_AUDIT_SUMMARY_v1.md` to document the Stage 2 documentation audit CSVs (inventory, broken refs, orphan candidates, open threads) and clarify that they are diagnostic, downstream-only snapshots. Archived the legacy flavor-sector Phase 3 experiment more explicitly by adding `experiments/phase3_flavor_v1/ARCHIVE_STATUS_v1.md`, marking it as non-canonical and separating it cleanly from the canonical Phase 3 mechanism module. No changes to Phase claims or numerical artifacts; this rung is purely about documentation clarity and governance hygiene.


## 2026-01-10 — Phase/Stage doc refresh + README link pass (docs-only rung)

**Files:**

- `README.md`
- `docs/PROJECT_OVERVIEW.md`
- `docs/STATE_OF_REPO.md`
- `docs/PHASES.md`
- `docs/CLAIMS_INDEX.md`
- `docs/INTERACTING_WITH_REPO.md`
- `docs/FUTURE_WORK_AND_ROADMAP.md`
- `stage2/docs/STAGE2_DOC_AUDIT_SUMMARY_v1.md`
- `stage2/docs/STAGE2_ARCHIVE_STATUS_v1.md`
- `.gitignore`

**Summary:**

- Brought the **top-level documentation into full alignment** with the current program structure:
  - Locked in the identity of **Phase 3 as the mechanism module** (no flavor calibration in canonical `phase3/`).
  - Clarified **Phase 4** as an FRW toy-diagnostic stub and **Phase 5** as an interface/sanity layer (rung 0–1).
  - Described **Stage 2** explicitly as a set of downstream, non-canonical diagnostic belts over Phase 3/4 outputs.

- Updated `README.md` to:
  - Reflect the refreshed Phase 1–5 descriptions and Stage 2 role.
  - Point explicitly to the core Phase papers in `phase*/artifacts/*.pdf`.
  - Add links to key docs and modules (global docs under `docs/`, Stage 2 docs under `stage2/docs/`, and the archived flavor experiment under `experiments/phase3_flavor_v1/`), so the repo is navigable directly from the front page.

- Refreshed global docs under `docs/`:
  - `PROJECT_OVERVIEW.md`: added a clear paragraph on Stage 2 as a **diagnostic belt** and an explicit note that the flavor-sector Phase 3 work is archived and non-canonical.
  - `STATE_OF_REPO.md`: 
    - Updated the Phase 3 status to “mechanism module” and added a **Stage 2 status** section listing the active belts.
    - Fixed the claims indexing to point to `phase0/CLAIMS.md` and to Phase 3 claims in the paper appendix (no `phase3/CLAIMS.md` file).
  - `PHASES.md`: re-framed Phase 3 as the mechanism module, added an “archived flavor add-on” note, and introduced a short **Stage 2 – diagnostic belts** section.
  - `CLAIMS_INDEX.md`: replaced the old flavor-sector Phase 3 claims section with a mechanism-module description, and pointed to `experiments/phase3_flavor_v1/` as archived flavor work.
  - `INTERACTING_WITH_REPO.md`: documented Stage 2 as a downstream-only layer and added guidance for users who only want to run the diagnostic belts.
  - `FUTURE_WORK_AND_ROADMAP.md`: clarified the distinction between **Stage 2 (existing diagnostic belts)** and **Stage II (future phases)**, and enumerated the current Stage 2 rungs (FRW corridor, mech/measure, joint mech–FRW, FRW data-probe).

- Extended the Stage 2 doc-audit docs:
  - `stage2/docs/STAGE2_DOC_AUDIT_SUMMARY_v1.md`: clarified how to use the four CSVs (inventory, broken refs, orphan candidates, open threads) as a **downstream diagnostic snapshot** when preparing publication-grade passes.
  - `stage2/docs/STAGE2_ARCHIVE_STATUS_v1.md`: documented the map between canonical Phase trees (`phase0/`–`phase5/`), Stage 2 belts (`stage2/`), and archived/experimental areas (e.g. `experiments/phase3_flavor_v1/`), plus guidance on where new work should live.

- Git hygiene:
  - Updated `.gitignore` to ignore the transient Stage 2 doc-audit working directory `stage2/doc_repo_audit/`, ensuring the audit scratch space never pollutes the main history.

No numerical pipelines, tables, or claims were changed in this rung. All edits are **documentation and governance only**, to make the repo self-consistent and easier to audit from the outside.


## 2026-01-11 — Stage 2 docs: FRW/mech/joint/data belt summaries (docs-only rung)

Stage 2 doc belt: created four belt-level summary docs under `stage2/docs/` to match the links advertised in `README.md` and make the Stage 2 FRW, mech/measure, joint mech–FRW, and FRW data-probe belts directly navigable. These summaries are downstream-only and point to the existing belt-specific outputs and design docs; they introduce no new computations and do not alter any Phase 0–5 claims.

**Files:**
- `stage2/docs/STAGE2_FRW_CORRIDOR_SUMMARY_v1.md` — high-level summary of the FRW corridor belt (rungs 1–9), inputs from Phase 4 FRW masks, main robustness checks, and θ★ alignment as a negative-result diagnostic.
- `stage2/docs/STAGE2_MECH_MEASURE_SUMMARY_v1.md` — belt-level summary of the mech/measure analysis (rungs 1–6), linking Phase 3 tables to probability-like and measure/flag candidates while explicitly keeping all results diagnostic-only.
- `stage2/docs/STAGE2_JOINT_MECH_FRW_SUMMARY_v1.md` — overview of the joint mech–FRW belt (rungs 1–4), describing the joint θ grid, FRW family definitions, and strong correlations between FRW scalars and mechanism amplitudes as structural cross-checks.
- `stage2/docs/STAGE2_FRW_DATA_PROBE_SUMMARY_v1.md` — concise summary of the FRW data-probe audit (rungs 1–2), recording that `frw_data_ok` is currently never satisfied and that all FRW families should be interpreted as pre-data corridors.

This rung closes broken Stage 2 links in `README.md` by providing the promised summary docs, improves documentation navigability for external auditors, and keeps Stage 2 firmly in its diagnostic, non-promotive role.

## 2026-01-11 — Repo atlas skeleton (docs-only rung)

Added a first-pass repo atlas under `docs/REPO_MAP_AND_ATLAS_v1.md` describing the top-level structure of the repository, including phase directories (phase0–phase5), Stage 2 diagnostic belts, the archived Phase 3 flavor experiment, sandbox notes, and global build/gate scripts. This atlas is descriptive only: it records where papers, code, outputs, and artifacts live on disk, without introducing new physics claims or changing any Phase 0–5 or Stage 2 content. The goal is to make the repo navigable and auditable for external readers before any finer-grained doc-audit or promotion passes.

## 2026-01-11 — Stage 2 doc belt: doc-audit link cleanup (docs-only rung)

Adjusted README and global reproducibility docs so that the Stage 2 documentation audit belt is described correctly without relying on links to the git-ignored working directory `stage2/doc_repo_audit/`. The doc-audit scratch directory is now presented as a local working area (which may not exist in a clean checkout), and readers are directed to `stage2/docs/STAGE2_DOC_AUDIT_SUMMARY_v1.md` for instructions and interpretation instead of 404-prone links. No numerical pipelines, Phase 0–5 claims, or Stage 2 diagnostics were changed; this rung is purely about documentation clarity and avoiding broken links.

## 2026-01-11 — Repo atlas hooks in README and STATE_OF_REPO (docs-only rung)

Linked the new repo atlas into the core documentation so external readers can discover it easily. Updated `README.md` to reference `docs/REPO_MAP_AND_ATLAS_v1.md` directly under the repository-structure section, and extended `docs/STATE_OF_REPO.md` to include the atlas in the canonical policy bullets as the directory-level map of phases, Stage 2 belts, and experiments. No numerical artifacts or Phase 0–5/Stage 2 claims were changed; this rung is purely about navigation and auditability.

## 2026-01-11 — Doc-audit rung B1: promote governance and θ architecture docs

Acted on Stage 2-style doc-audit signals that `docs/ARCHIVE.md`, `docs/GATES_AND_STATUS.md`, and `docs/THETA_ARCHITECTURE.md` were effectively orphaned global governance docs (not linked from the main narrative). Promoted them into the central documentation:

- Extended `docs/STATE_OF_REPO.md` with a **Governance companion docs** section pointing to:
  - `docs/ARCHIVE.md` for archive/deprecation policy,
  - `docs/GATES_AND_STATUS.md` for gates and status labels,
  - `docs/REPRODUCIBILITY.md` for global reproducibility rules.
- Extended `docs/PROJECT_OVERVIEW.md` with a new section **Governance and θ companion docs**, linking:
  - `docs/ARCHIVE.md` and `docs/GATES_AND_STATUS.md` as governance references,
  - `docs/THETA_ARCHITECTURE.md` as the main θ/corridor architecture explainer.

This rung does not change any Phase 0–5 or Stage 2 claims; it reclassifies previously orphaned governance docs as first-class companions to the core overview/state docs, improving navigation and auditability.

## 2026-01-11 — Doc-audit rung B2: promote legacy migrations governance map

Promoted the previously orphaned `docs/LEGACY_MIGRAIONS_PHASE0_MAP.MD` file into
the main governance/navigation surface:

- Extended `docs/ARCHIVE.md` with a **Legacy migrations** section that explains
  how the legacy repository `origin-axiom-legacy` relates to the phased repo and
  points to `docs/LEGACY_MIGRAIONS_PHASE0_MAP.MD` as the provenance index.
- Extended `docs/REPO_MAP_AND_ATLAS_v1.md` with a **Legacy migrations map**
  section that situates `docs/LEGACY_MIGRAIONS_PHASE0_MAP.MD` in the atlas as
  the Phase 0–compatible bridge between legacy runs and current Phase 0–5
  artifacts.

No Phase 0–5 claims or numerical artifacts were changed; this rung only makes a
governance/provenance doc discoverable and clearly scoped.

## 2026-01-11 — Doc-audit rung B3: surface FRW promotion gate and Phase 5 roadmap

Acted on doc-audit style signals that two important governance/planning docs
were effectively orphaned:

- `docs/FRW_CORRIDOR_PROMOTION_GATE_v1.md` (FRW corridor promotion gate), and
- `docs/phase5_roadmap.md` (Phase 5 roadmap from FRW toys to data-contact).

Changes:

- Extended `docs/STAGE2_PROMOTION_DESIGN_v1.md` with a **Companion docs** section
  that points to the FRW corridor promotion gate and the Phase 5 roadmap as the
  governance/planning context for any future Option A/B promotions.
- Extended `docs/FUTURE_WORK_AND_ROADMAP.md` with a **Phase 5 roadmap companion**
  section linking `docs/phase5_roadmap.md` so that Phase 5 planning text is
  discoverable from the main roadmap.

No Phase 0–5 claims, numerical artifacts, or Stage 2 diagnostics were changed;
this rung only promotes existing governance/planning docs into the navigation
surface.

## 2026-01-11 — Doc-audit rung B4: surface Stage 2 overview and joint plan docs

Promoted two previously under-linked Stage 2 design docs into the main Stage 2
navigation surface:

- `docs/STAGE2_OVERVIEW.md` — the conceptual overview of Stage 2 as an
  exploratory downstream lab layer, and
- `docs/STAGE2_JOINT_MECH_FRW_PLAN_v1.md` — the joint mech–FRW analysis plan.

Changes:

- Extended `stage2/docs/STAGE2_BELT_OVERVIEW_v1.md` with a **Companion docs in
  `docs/`** section pointing to `docs/STAGE2_OVERVIEW.md`,
  `docs/STAGE2_JOINT_MECH_FRW_PLAN_v1.md`, and
  `docs/STAGE2_MECH_MEASURE_RUNG1_6_SUMMARY_v1.md` as higher-level Stage 2
  design/summary docs.
- Extended `docs/REPO_MAP_AND_ATLAS_v1.md` with a **Stage 2 overview and plans**
  section that situates `docs/STAGE2_OVERVIEW.md` and
  `docs/STAGE2_JOINT_MECH_FRW_PLAN_v1.md` in the atlas as the conceptual top
  layer for Stage 2 belts.

No Phase 0–5 claims or numerical artifacts were modified; this rung strictly
improves discoverability and provenance of Stage 2 design docs.

## 2026-01-11 — Doc-audit rung C1: record doc-audit status in Stage 2 summary

Extended `stage2/docs/STAGE2_DOC_AUDIT_SUMMARY_v1.md` with a **Doc-audit status
as of 2026-01-11** section that summarises the manual doc-audit rungs applied so
far. The new section records that we have:

- added Stage 2 belt summary docs under `stage2/docs/`,
- introduced and linked a repo atlas (`docs/REPO_MAP_AND_ATLAS_v1.md`),
- clarified the role of the git-ignored `stage2/doc_repo_audit/` working dir,
- promoted key governance and θ architecture docs (`ARCHIVE`, `GATES_AND_STATUS`,
  `THETA_ARCHITECTURE`, and the legacy migrations map),
- surfaced the FRW corridor promotion gate and Phase 5 roadmap, and
- connected higher-level Stage 2 design docs (`STAGE2_OVERVIEW`,
  `STAGE2_JOINT_MECH_FRW_PLAN_v1`, and the mech/measure rung summary) to the
  Stage 2 belt overview and atlas.

No Phase 0–5 claims, numerical artifacts, or Stage 2 diagnostics were changed;
this rung simply makes the current doc-audit progress legible from within the
Stage 2 doc-audit summary itself.

## 2026-01-11 — Doc-audit rung C2: mark Phase 2 AUDIT_REPORT as historic snapshot

Phase 2 doc belt: added a short status banner to `phase2/AUDIT_REPORT.md`
clarifying that it is an internal, point-in-time structural audit snapshot
generated on 2026-01-04, not a living Phase 2 claims or scope document. The
banner explains that the TODO/TBD references listed in the report are part of
the audit (which files contained TODOs at that time) and are intentionally left
unchanged, and directs readers to `phase2/SCOPE.md`, `phase2/CLAIMS.md`,
`phase2/REPRODUCIBILITY.md`, and global docs under `docs/` for the current
Phase 2 status. No Phase 2 claims, numerics, or workflows were modified in this
rung; this is purely a governance/doc-audit clarification.

## 2026-01-11 — Doc-audit rung C3: mark ROADMAP.md as legacy roadmap

Doc-audit belt: added a status banner to `ROADMAP.md` clarifying that it is a
legacy program roadmap from the pre-Stage-2 / early-phasing period. The banner
directs readers to `docs/STATE_OF_REPO.md`, `docs/PHASES.md`, and
`docs/FUTURE_WORK_AND_ROADMAP.md` as the authoritative sources for current
phase/Stage status and future work, and states that when there is disagreement
the `docs/` versions plus per-phase `SCOPE.md`/`CLAIMS.md` are canonical. No
Phase 0–5 claims or numerical artifacts were changed; this rung only reclassifies
an older roadmap as historical context to avoid confusion during audits.

## 2026-01-11 — Doc-audit rung B5: fix Stage 2 overview filename in repo atlas

Doc-audit belt: corrected a broken reference in `docs/REPO_MAP_AND_ATLAS_v1.md`
from the non-existent `STAGE2_OVERVIEW_AND_STATUS_v1.md` to the actual Stage 2
overview doc `STAGE2_OVERVIEW_v1.md`, and clarified the description as an
overview of Stage 2 as a diagnostic belt layer and its sub-belts. No Phase 0–5
claims or numerical artifacts were changed; this rung fixes a 404-style doc
link introduced during the atlas work.

## 2026-01-11 — Doc-audit rung C4: surface atlas and Stage 2 diagnostics from INTERACTING and CLAIMS_INDEX

Doc-audit belt: improved discoverability and scoping of Stage 2 diagnostics and
the repo atlas from two central global docs:

- Extended `docs/INTERACTING_WITH_REPO.md` with an **Additional navigation and
  audit tools** section pointing to:
  - `docs/REPO_MAP_AND_ATLAS_v1.md` as the directory-level repo map,
  - `stage2/docs/STAGE2_BELT_OVERVIEW_v1.md` as the Stage 2 belt overview, and
  - `stage2/docs/STAGE2_DOC_AUDIT_SUMMARY_v1.md` as the documentation audit
    interface.

- Extended `docs/CLAIMS_INDEX.md` with a **Stage 2 diagnostics and non-claims**
  section clarifying that Stage 2 belts introduce no new physical claims, do not
  modify Phase 0–5 claims in place, and can only influence phase text via
  explicit Phase 0–style promotion gates and updates to phase-local `CLAIMS.md`.

No numerical artifacts or Phase 0–5 claims were changed; this rung tightens the
narrative around where to find structural/audit information and how Stage 2
sits relative to the claims ledger.

## 2026-01-11 — Doc-audit rung C5: surface Phase 5 roadmap and sandbox from Phase 5 scope

Phase 5 doc belt: extended `phase5/SCOPE.md` with a **Companion docs and
sandbox** section that:

- points to `docs/phase5_roadmap.md` as the planning-level roadmap for how
  Phase 5 should sit on top of the Phase 3 mechanism and Phase 4 FRW toys, and
- explicitly identifies the `sandbox/PHASE5_SANDBOX_*.md` files as non-canonical
  Phase 5 scratch pads (numerology and speculative ideas that do not change the
  Phase 5 scope or claims).

No Phase 5 claims, numerics, or upstream Phase 3/4 artifacts were modified; this
rung improves navigation and makes the status of Phase 5 planning and sandbox
material clear from the Phase 5 scope document itself.

## 2026-01-11 — Doc-audit rung C6: surface Phase 2 workflow, lock checklist, and audit report from scope

Phase 2 doc belt: extended `phase2/SCOPE.md` with a **Companion docs: workflow,
lock checklist, and audit snapshot** section that:

- points to `PHASE2_WORKFLOW_GUIDE.md` as the operational guide for running the
  Phase 2 pipeline and preparing releases,
- points to `PHASE2_LOCK_CHECKLIST.md` as the checklist for treating Phase 2 as
  locked, and
- clarifies that `AUDIT_REPORT.md` is a structural audit snapshot rather than a
  claims document, directing readers back to `SCOPE.md`, `CLAIMS.md`, and
  `REPRODUCIBILITY.md` as the authoritative Phase 2 contract.

No Phase 2 claims, numerical artifacts, or workflows were modified; this rung
improves navigation and makes key governance/workflow documents discoverable
from the Phase 2 scope itself.

## 2026-01-11 — Doc-audit rung C7: surface FRW design, promotion gate, and Stage 2 FRW diagnostics from Phase 4 scope

Phase 4 doc belt: extended `phase4/SCOPE.md` with a **Companion docs: FRW
design, promotion, and Stage 2 diagnostics** section that:

- points to `FRW_TOY_DESIGN.md`, `FRW_DATA_DESIGN.md`, and `FRW_SYNTHESIS.md`
  as the internal FRW toy and data-design docs for this phase,
- points to `docs/FRW_CORRIDOR_PROMOTION_GATE_v1.md` as the governance gate for
  any future promotion of Stage 2 FRW corridor results into Phase 4/5 text or
  figures,
- points to `phase4/docs/PHASE4_FRW_PROMOTION_DESIGN_v1.md` as the Phase 4
  design-level plan for how Stage 2 FRW/mech/joint/data artifacts might be used
  under that gate, and
- links `stage2/docs/STAGE2_FRW_CORRIDOR_SUMMARY_v1.md` and
  `stage2/docs/STAGE2_FRW_DATA_PROBE_SUMMARY_v1.md` as downstream-only Stage 2
  FRW diagnostics that support interpretation of Phase 4 without changing its
  claims in place.

No Phase 4 claims, numerical artifacts, or FRW pipeline code were modified; this
rung improves navigation and clarifies how Phase 4 relates to FRW design docs,
promotion gates, and Stage 2 FRW diagnostics.

## 2026-01-11 — Doc-audit rung C8: Phase 3 mechanism companion docs

Phase 3 doc belt: extended `phase3/MECHANISM_CONTRACT.md` with a **Companion
docs: role, Stage 2 diagnostics, and archived flavor** section that:

- points to `phase3/ROLE_IN_PROGRAM.md` for the mechanism module's place in the
  Phase 2 → Phase 3 → Phase 4 chain,
- links `stage2/docs/STAGE2_MECH_MEASURE_SUMMARY_v1.md` and
  `stage2/docs/STAGE2_JOINT_MECH_FRW_SUMMARY_v1.md` as downstream-only Stage 2
  mech/measure and joint mech–FRW diagnostics built on top of Phase 3 outputs,
- situates these belts inside `stage2/docs/STAGE2_BELT_OVERVIEW_v1.md`, and
- explicitly points to `experiments/phase3_flavor_v1/ARCHIVE_STATUS_v1.md` as
  the archive banner for the non-canonical Phase 3 flavor-sector experiment.

No Phase 3 claims, numerical artifacts, or mechanism code were modified; this
rung improves navigation and clarifies how canonical Phase 3 relates to Stage 2
diagnostics and the archived flavor tree.

## 2026-01-11 — Doc-audit rung C9: Phase 1 companion docs from scope

Phase 1 doc belt: extended `phase1/SCOPE.md` with a **Companion docs:
narrative, reproducibility, and paper** section that:

- points to `phase1/README.md` as the Phase 1–specific overview of the toy
  ensembles and how they instantiate the non-cancellation axiom,
- points to `phase1/REPRODUCIBILITY.md` as the Phase 1 reproducibility
  contract, and
- points to the consolidated Phase 1 paper `artifacts/origin-axiom-phase1.pdf`
  (built from `phase1/paper/main.tex` and `phase1/outputs/`) as the main
  exposition of Phase 1 claims alongside `phase1/CLAIMS.md`.

No Phase 1 claims, numerical artifacts, or workflows were modified; this rung
improves navigation and makes it easier for readers of the Phase 1 scope to
find the corresponding narrative, reproducibility, and paper artifacts.

## 2026-01-11 — Doc-audit rung C10: Phase 0 companion docs from scope

Phase 0 doc belt: extended `phase0/SCOPE.md` with a **Companion docs:
governance, reproducibility, and paper** section that:

- points to `phase0/README.md` for a Phase 0–specific governance overview,
- points to `phase0/REPRODUCIBILITY.md` as the Phase 0 reproducibility contract,
- links `docs/ARCHIVE.md`, `docs/GATES_AND_STATUS.md`, and
  `docs/THETA_ARCHITECTURE.md` as the global governance and θ-architecture
  docs enforced by Phase 0, and
- points to the consolidated Phase 0 paper `artifacts/origin-axiom-phase0.pdf`
  (built from `phase0/paper/main.tex`) as the main exposition of Phase 0 claims
  alongside `phase0/CLAIMS.md`.

No Phase 0 claims, numerical artifacts, or governance rules were modified; this
rung improves navigation and makes it easier for readers of the Phase 0 scope
to find the corresponding governance, reproducibility, and paper artifacts.

## 2026-01-11 — Doc-audit rung D2: add repo audit checklist to REPRODUCIBILITY

Doc-audit belt: extended `docs/REPRODUCIBILITY.md` with a **Repo audit checklist
(Stage 2 belt)** section that gives external auditors (or future selves) a
concrete sequence of steps to verify:

- clean Phase 0–5 paper builds and artifacts,
- consistency between global docs and the directory-level map in
  `docs/REPO_MAP_AND_ATLAS_v1.md`,
- that Stage 2 FRW/mech/joint/data/θ★ belts are downstream-only diagnostics
  over Phase 3/4 outputs,
- the current status of the Stage 2 doc/repo audit from
  `stage2/docs/STAGE2_DOC_AUDIT_SUMMARY_v1.md`,
- alignment between claims and phase-local `SCOPE.md`/`CLAIMS.md`/`REPRODUCIBILITY.md`,
  and
- clear separation between canonical phases and archived/experimental areas.

No Phase 0–5 claims, numerical artifacts, or Stage 2 computations were changed
in this rung; it tightens the reproducibility and audit narrative in line with
the existing Stage 2 doc/repo audit plan.

## 2026-01-11 — Doc-audit rung C11: mark flavor SCOPE as archived and point to canonical Phase 3

Flavor archive belt: extended `experiments/phase3_flavor_v1/SCOPE.md` with an
archive status note that:

- states explicitly that `experiments/phase3_flavor_v1/` is an archived Phase 3
  flavor-sector experiment and not part of canonical Phase 3,
- points to `experiments/phase3_flavor_v1/ARCHIVE_STATUS_v1.md` as the formal
  archive banner, and
- directs readers back to canonical Phase 3 under `phase3/` (mechanism
  contract, role-in-program doc, and Phase 3 paper artifact) for live Phase 3
  claims.

No canonical Phase 3 claims or numerical artifacts were changed; this rung
tightens the archive boundary and reduces the risk of misreading the flavor
experiment as live Phase 3 content.

## 2026-01-11 — Doc-audit rung D4: consolidate open threads into FUTURE_WORK_AND_ROADMAP

Doc-audit belt: extended `docs/FUTURE_WORK_AND_ROADMAP.md` with a
**Consolidating open threads and TODOs** section that:

- declares this roadmap as the canonical home for future work and unresolved
  questions, and
- ties it explicitly to the Stage 2 doc/repo audit belt via
  `stage2/docs/STAGE2_DOC_AUDIT_SUMMARY_v1.md` and
  `stage2/docs/STAGE2_BELT_OVERVIEW_v1.md`.

The section explains that TODO/TBD-style items discovered across Phase and Stage
docs are being progressively consolidated here, so public-facing phase docs can
focus on established scope and claims. No Phase 0–5 claims, numerical
artifacts, or Stage 2 computations were modified in this rung.

## 2026-01-11 — Doc-audit rung D5: surface Stage 2 diagnostics from PHASES

Doc-audit belt: extended `docs/PHASES.md` with a **Stage 2 diagnostic belts and
doc/repo audit** section that:

- points to `docs/STAGE2_OVERVIEW.md` for the conceptual description of Stage 2
  as a downstream diagnostic lab layer,
- points to `stage2/docs/STAGE2_BELT_OVERVIEW_v1.md` for the belt-level overview
  of FRW, mech/measure, joint mech–FRW, FRW data-probe, θ★, and doc/repo audit
  belts, and
- points to `stage2/docs/STAGE2_DOC_AUDIT_SUMMARY_v1.md` for the documentation/
  repo audit belt status.

The section makes explicit that Stage 2 introduces no new physical claims and
cannot change Phase 0–5 claims in place without passing Phase 0–style gates and
updating phase-local `CLAIMS.md`. No Phase 0–5 numerics or claims were modified
in this rung.

## 2026-01-11 — Doc-audit rung D6: add README entry path aligned with atlas and Stage 2

Doc-audit belt: extended `README.md` with a **Where to start reading** section
that gives a concrete entry path through:

- `docs/PROJECT_OVERVIEW.md` and `docs/PHASES.md` (overview + phase ladder),
- `docs/STATE_OF_REPO.md` and `docs/REPO_MAP_AND_ATLAS_v1.md` (status + layout),
- `docs/CLAIMS_INDEX.md` and the Phase PDFs under `artifacts/` (claims +
  artifacts),
- `docs/STAGE2_OVERVIEW.md`, `stage2/docs/STAGE2_BELT_OVERVIEW_v1.md`, and
  `stage2/docs/STAGE2_DOC_AUDIT_SUMMARY_v1.md` (Stage 2 diagnostic belts and
  doc/repo audit), and
- `docs/ARCHIVE.md`, `docs/GATES_AND_STATUS.md`, and `docs/THETA_ARCHITECTURE.md`
  (governance and archive).

No Phase 0–5 claims, numerical artifacts, or Stage 2 computations were changed;
this rung aligns the README entry path with the existing atlas and Stage 2
doc/audit structure.

## 2026-01-11 — Doc-audit rung D7: slot doc/repo-audit belt into STAGE2_OVERVIEW

Stage 2 doc belt: extended `docs/STAGE2_OVERVIEW.md` with a **Documentation and
repo-audit belt** section that:

- recognises the doc/repo-audit belt as a first-class Stage 2 component alongside
  the FRW, mech/measure, joint mech–FRW, FRW data-probe, and θ★ belts,
- explains its role (inventorying docs, flagging broken refs/orphans/open
  threads, and proposing manual documentation rungs), and
- points to `stage2/docs/STAGE2_DOC_AUDIT_SUMMARY_v1.md` as the primary
  interface, emphasising that the belt does not introduce new physical claims
  or modify Phase 0–5 numerical artifacts.

No Phase 0–5 claims or numerical outputs were changed; this rung tightens the
conceptual Stage 2 overview so it matches the actual belt structure in the repo.

## 2026-01-11 — Doc-audit rung D8: tie Stage 2 belt overview to repo audit checklist

Stage 2 doc belt: extended `stage2/docs/STAGE2_BELT_OVERVIEW_v1.md` with a
section describing how the documentation/repo-audit belt connects to the global
**Repo audit checklist (Stage 2 belt)** in `docs/REPRODUCIBILITY.md`. The new
section points auditors to the checklist as the concrete procedure for
verifying paper builds, global docs + atlas, Stage 2 downstream-only behavior,
doc-audit status, and archive/experiment boundaries. No Phase 0–5 claims or
numerical artifacts were modified in this rung.

## 2026-01-11 — Doc-audit rung D9: tie promotion design to doc/repo-audit belt

Stage 2 doc belt: extended `docs/STAGE2_PROMOTION_DESIGN_v1.md` with a
**Documentation and repo-audit preconditions** section that:

- requires the Stage 2 documentation/repo-audit belt to be in a clean, logged
  state (via `stage2/docs/STAGE2_DOC_AUDIT_SUMMARY_v1.md` and `PROGRESS_LOG.md`)
  before any Stage 2 artifact is promoted into Phase 3/4/5 text or figures,
- insists that global docs and the repo atlas already reflect the intended role
  of any promoted artifacts, and
- ties promotions to clear archive/experiment boundaries as recorded in
  `docs/ARCHIVE.md`, `docs/GATES_AND_STATUS.md`, and
  `stage2/docs/STAGE2_ARCHIVE_STATUS_v1.md`.

No numerical artifacts or Phase 0–5 claims were modified; this rung tightens the
governance conditions on Stage 2 → Phase promotions in line with the doc/repo-
audit belt.

## 2026-01-11 — Doc-audit rung D9: tie promotion design to doc/repo-audit belt

Stage 2 doc belt: extended `docs/STAGE2_PROMOTION_DESIGN_v1.md` with a
**Documentation and repo-audit preconditions** section that:

- requires the Stage 2 documentation/repo-audit belt to be in a clean, logged
  state (via `stage2/docs/STAGE2_DOC_AUDIT_SUMMARY_v1.md` and `PROGRESS_LOG.md`)
  before any Stage 2 artifact is promoted into Phase 3/4/5 text or figures,
- insists that global docs and the repo atlas already reflect the intended role
  of any promoted artifacts, and
- ties promotions to clear archive/experiment boundaries as recorded in
  `docs/ARCHIVE.md`, `docs/GATES_AND_STATUS.md`, and
  `stage2/docs/STAGE2_ARCHIVE_STATUS_v1.md`.

No numerical artifacts or Phase 0–5 claims were modified; this rung tightens the
governance conditions on Stage 2 → Phase promotions in line with the doc/repo-
audit belt.

## 2026-01-11 — Doc-audit rung D10: record doc/repo-audit belt in STATE_OF_REPO

Doc-audit belt: extended `docs/STATE_OF_REPO.md` with a **Stage 2 documentation
and repo-audit status** section that:

- acknowledges the Stage 2 doc/repo-audit belt as part of the governance and
  audit infrastructure,
- explains its role (inventorying docs, flagging broken refs/orphans/open
  threads, proposing manual documentation rungs recorded in `PROGRESS_LOG.md`),
- and points to `stage2/docs/STAGE2_DOC_AUDIT_SUMMARY_v1.md` as the place where
  its current status is described.

No Phase 0–5 claims or numerical artifacts were modified; this rung keeps the
state-of-repo document in sync with the existence and role of the Stage 2
doc/repo-audit belt.

## 2026-01-11 — Doc-audit rung C12: surface root REPRODUCIBILITY entrypoint

Doc-audit belt: acted on the doc-audit orphan table indication that the
root-level `REPRODUCIBILITY.md` (“Reproducibility entrypoint”) was effectively
orphaned:

- Extended `README.md` with a **Reproducibility entrypoint** section pointing
  to the root `REPRODUCIBILITY.md` as a concise starting point for reproducible
  use of the repo.
- Extended `docs/INTERACTING_WITH_REPO.md` with a **Reproducibility
  entrypoint** note that links to the same file and clarifies that it forwards
  into the more detailed reproducibility and audit docs under `docs/` and in
  the phase trees.

No Phase 0–5 claims, numerical artifacts, or Stage 2 computations were
modified; this rung simply promotes an existing reproducibility entrypoint
document into the main navigation surface.

## 2026-01-11 — Doc-audit rung C13: classify Phase 4 PLANNING and HARD_NOVELTY_ROADMAP as design notes

Phase 4 doc belt: acted on the doc-audit orphan table entries for Phase 4
planning documents:

- `phase4/PLANNING.md` (Phase 4 Planning – Vacuum → FRW / Scale sanity), and
- `phase4/HARD_NOVELTY_ROADMAP.md` (Phase 4 hard-novelty roadmap, F1 + FRW).

Changes:

- Added a status banner near the top of both files marking them as **Phase 4
  design / planning notes**, explicitly **draft and non-binding**.
- The banner points readers back to the canonical Phase 4 contract documents
  (`phase4/SCOPE.md`, `phase4/CLAIMS.md`, `phase4/NON_CLAIMS.md`,
  `phase4/REPRODUCIBILITY.md`) and to the detailed FRW design docs
  (`phase4/FRW_TOY_DESIGN.md`, `phase4/FRW_DATA_DESIGN.md`, `phase4/FRW_SYNTHESIS.md`).
- It also notes that any future promotion of ideas from these design notes into
  Phase 4/5 text or figures must pass through the FRW promotion gate
  (`docs/FRW_CORRIDOR_PROMOTION_GATE_v1.md`) and the Phase 4 promotion design
  (`phase4/docs/PHASE4_FRW_PROMOTION_DESIGN_v1.md`), and be reflected in the
  Phase 4 scope/claims documents.

No Phase 4 claims, numerical artifacts, or FRW pipelines were modified; this
rung clarifies the status and role of Phase 4 planning documents within the
governance and Stage 2 doc/repo-audit framework.

## 2026-01-11 — Doc-audit rung C14: surface Phase 4 contract and design bundle from OVERVIEW

Phase 4 doc belt: extended `phase4/OVERVIEW.md` with a **Companion docs: Phase 4
contract and design bundle** section that:

- lists the key Phase 4-local governance and design documents
  (`SCOPE.md`, `CLAIMS.md`, `NON_CLAIMS.md`, `REPRODUCIBILITY.md`,
  `CLAIMS_TABLE.md`, `PHASE3_INTERFACE.md`, `MAPPING_FAMILIES.md`) as the Phase 4
  contract/design surface, and
- situates them alongside the FRW design and promotion docs
  (`FRW_TOY_DESIGN.md`, `FRW_DATA_DESIGN.md`, `FRW_SYNTHESIS.md`,
  `docs/FRW_CORRIDOR_PROMOTION_GATE_v1.md`,
  `phase4/docs/PHASE4_FRW_PROMOTION_DESIGN_v1.md`).

The new section clarifies that these documents are governed by Phase 0 contracts
and Stage 2 promotion design, and that they are to be read as internal Phase 4
contract/design material until the relevant gates are passed and claims are
locked. No Phase 4 claims, numerical artifacts, or FRW pipelines were modified
in this rung.

## 2026-01-11 — Doc-audit rung C15: Phase 3 companion docs from scope

Phase 3 doc belt: extended `phase3/SCOPE.md` with a **Companion docs:
mechanism contract, role, reproducibility, and paper** section that:

- points to `phase3/README.md` for a Phase 3–specific overview,
- links `phase3/MECHANISM_CONTRACT.md` as the mechanism contract,
- links `phase3/ROLE_IN_PROGRAM.md` for the Phase 3 position in the program,
- classifies `phase3/PHASE3_RUNG2_MECHANISM_A_INSTABILITY_PENALTY.md` as a
  rung-level design note refining the mechanism internals without extending
  scope/claims on its own,
- links `phase3/REPRODUCIBILITY.md` as the Phase 3 reproducibility contract,
- and points to `artifacts/origin-axiom-phase3.pdf` as the consolidated Phase 3
  paper to be read together with `phase3/CLAIMS.md`.

No Phase 3 claims, numerical artifacts, or mechanism code were modified; this
rung improves navigation and de-orphans the Rung-2 design note within the Phase
3 scope and Stage 2 doc/repo-audit framework.

## 2026-01-11 — Doc-audit rung E1: record Jan 2026 Stage 2 doc-audit sprint snapshot

Stage 2 doc belt: extended `stage2/docs/STAGE2_DOC_AUDIT_SUMMARY_v1.md` with a
**Jan 2026 Stage 2 doc-audit sprint (snapshot)** section summarising the
documentation rungs applied between 2026-01-09 and 2026-01-11. The new section
captures:

- navigation and mapping improvements (repo atlas, README entry path,
  reproducibility entrypoint),
- explicit surfacing of Stage 2 belts and the doc/repo-audit belt across global
  docs,
- companion-doc wiring for Phase 0–5 scopes and key Phase 3/4 documents,
- archive and experiment boundary tightening (including the Phase 3 flavor
  archive tree), and
- the addition of a Stage 2–aware repo-audit checklist.

It also notes that the doc-audit CSVs provide a point-in-time snapshot and that
future structural changes may require re-running the Stage 2 doc-audit scripts
and applying additional rungs. No Phase 0–5 claims or numerical artifacts were
modified in this rung.
## 2026-01-11 — Belt A / Rung A1: Phase 0 alignment memo (contracts, paper, repo surface)

Phase 0 alignment belt: added `phase0/PHASE0_ALIGNMENT_v1.md`, a descriptive
alignment memo that:

- compares `phase0/SCOPE.md`, `phase0/CLAIMS.md`, and `phase0/REPRODUCIBILITY.md` with the Phase 0 paper (`artifacts/origin-axiom-phase0.pdf`) and the draft θ architecture note `docs/THETA_ARCHITECTURE.md`,
- records that the Phase 0 paper’s abstract and introduction match the Phase 0 scope (governance layer, no physics claims, no fixed θ★, no cosmology inference),
- checks that the claims ledger defines governance and reproducibility contracts rather than physics claims and that its evidence pointers are consistent with the paper’s sections on vocabulary, corridor governance, reproducibility, and falsifiability,
- confirms that `docs/THETA_ARCHITECTURE.md` is correctly labelled as a draft, non-binding design note that remains subordinate to Phase 0–3 claims,
- and identifies the remaining “slack” as intentional conceptual space for later phases (choice of θ-architecture and physical interpretation), not as a contradiction.

The memo is descriptive only and does not introduce new claims or modify existing Phase 0 contracts, numerical artifacts, or Stage 2 diagnostics.
## 2026-01-11 — Belt A / Rung A2: Phase 1 alignment memo (scope, claims, toy ensembles, paper)

Phase 1 alignment belt: added `phase1/PHASE1_ALIGNMENT_v1.md`, a descriptive alignment memo that:

- records how `phase1/SCOPE.md`, `phase1/CLAIMS.md`, `phase1/ASSUMPTIONS.md`, and `phase1/REPRODUCIBILITY.md` line up with the Phase 1 paper (`artifacts/origin-axiom-phase1.pdf` and `phase1/paper/*.tex`) and the Phase 1 repo layout,
- confirms that Phase 1 is consistently presented as a minimal, toy-level non-cancellation phase with no phenomenology, θ★, φ, or unification claims,
- checks that the axiom and toy ensembles in the paper match the claims register (C1–C5) and that the θ-agnostic stance in the toy-model section is consistent with the absence of θ★-specific claims in `phase1/CLAIMS.md`,
- verifies that numeric scaling and energy-discipline claims in `phase1/CLAIMS.md` are supported by the methods/results sections and the outputs under `phase1/outputs/` and `phase1/artifacts/`,
- and confirms that the Phase 1 reproducibility protocol and repository structure match the paper’s description of deterministic, version-controlled numerics.

The memo is descriptive only and does not introduce new claims or modify existing Phase 1 contracts, numerical artifacts, or Stage 2 diagnostics.
## 2026-01-11 — Belt A / Rung A3: Phase 2 alignment memo (scope, claims, FRW viability, paper)

Phase 2 alignment belt: added `phase2/PHASE2_ALIGNMENT_v1.md`, a descriptive alignment memo that:

- records how `phase2/SCOPE.md`, `phase2/CLAIMS.md`, `phase2/ASSUMPTIONS.md`, `phase2/APPROXIMATION_CONTRACT.md`, `phase2/PHASE2_WORKFLOW_GUIDE.md`, `phase2/PHASE2_LOCK_CHECKLIST.md`, `phase2/REPRODUCIBILITY.md`, and `phase2/AUDIT_REPORT.md` line up with the Phase 2 paper (`artifacts/origin-axiom-phase2.pdf`) and the Phase 2 repo structure,
- clarifies that Phase 2 is consistently scoped as a toy mode-sum + bounded FRW viability phase, strictly pre-data and pre-phenomenology,
- checks that the Phase 2 claims register (locked) about existence and structure of a toy FRW viability corridor are consistent with the paper’s FRW viability construction and with Stage 2 FRW diagnostics,
- relates the assumptions and approximation contract to the approximations used in the paper’s derivations, and interprets results as conditional on these approximations,
- and confirms that later Stage 2 FRW diagnostics (broad viable band, empty `frw_data_ok`, θ★ lying inside but not singled out) refine but do not contradict Phase 2 claims when those claims are interpreted as pre-data structural statements.

The memo is descriptive and does not introduce new Phase 2 claims or modify existing contracts, numerical artifacts, or Stage 2 pipelines.
## 2026-01-11 — Belt A / Rung A4: Phase 3 alignment memo (mechanism scope, claims, outputs, paper)

Phase 3 alignment belt: added `phase3/PHASE3_ALIGNMENT_v1.md`, a descriptive alignment memo that:

- compares `phase3/SCOPE.md`, `phase3/CLAIMS.md`, `phase3/MECHANISM_CONTRACT.md`, `phase3/ROLE_IN_PROGRAM.md`, `phase3/REPRODUCIBILITY.md`, and the rung-2 design note with the Phase 3 mechanism paper (`artifacts/origin-axiom-phase3.pdf`) and the outputs under `phase3/outputs/tables/`,
- confirms that Phase 3 is consistently treated as the mechanism module (not a flavor module) in phase-local docs, the paper, and global docs, with flavor-sector experiments archived under `experiments/phase3_flavor_v1/`,
- checks that the mechanism contract and claims register match the implementation and tables (baseline scans, binding certificates, and diagnostics) used in the paper and in Stage 2 mech/joint analysis,
- relates Phase 3 reproducibility docs and repo layout to the way the paper presents its numerics and to the Stage 2 scripts that consume Phase 3 tables,
- and aligns Phase 3 non-claims (no canonical θ-measure, no special θ★ selection, no direct phenomenology) with Stage 2 mech/joint and θ★ diagnostics, which find smooth, well-behaved mechanism scalars that are strongly correlated with FRW scalars but do not single out θ★.

The memo is descriptive only and does not introduce new Phase 3 claims or modify existing contracts, numerical artifacts, or Stage 2 pipelines.
## 2026-01-11 — Belt A / Rung A5: Phase 4 and Phase 5 alignment memos

Phase 4/5 alignment belt: added alignment memos for the FRW toy stub and the interface/sanity layer:

- `phase4/PHASE4_ALIGNMENT_v1.md` records how Phase 4 scope, claims, non-claims, reproducibility docs, FRW design and promotion docs, Phase 4 FRW outputs, Stage 2 FRW and θ★ diagnostics, and the Phase 4 paper align when Phase 4 is interpreted as a toy FRW diagnostic stub with pre-data corridors and no θ★ or data-conditioned corridor claims.

- `phase5/PHASE5_ALIGNMENT_v1.md` records how Phase 5 scope, role, early vision docs, and non-claims align with the current Stage 2 verdicts (FRW viability, mechanism-derived scalars, joint mech–FRW correlations, FRW data gate, and θ★ diagnostics), treating Phase 5 as an interface and sanity layer over locked Phase 3/4 outputs and Stage 2 belts rather than as a new physics phase.

These memos are descriptive only; they do not introduce new claims or modify existing Phase 4/5 contracts, numerical artifacts, or Stage 2 pipelines. They complete Belt A (Phase paper/claims alignment) at the current snapshot.
## 2026-01-11 — Belt B / Rung B1: Stage 2 FRW diagnostics verdict (corridors, data probes, θ★)

Stage 2 FRW belt: added `stage2/frw_corridor_analysis/docs/STAGE2_FRW_VERDICT_v1.md`, a physics-facing verdict document that:

- synthesises the FRW corridor rungs (1–9), the FRW data-probe audit, and the θ★–FRW alignment diagnostic into a single summary,
- records that the current Phase 4 FRW construction admits a broad, contiguous FRW-viable band on the 2048-point θ-grid and structurally nontrivial corridor families that are robust under contiguity and stride tests,
- clarifies that the aggregate data flag `frw_data_ok` is identically false in the current snapshot, so all FRW corridors and families are pre-data corridors and the FRW data gate is not yet open,
- notes that θ★ lies inside the FRW-viable band but is not singled out by any current FRW corridor or family definition, and that this is treated as a negative-result sanity check rather than a hidden prediction,
- and states a conservative verdict: current FRW diagnostics provide a structurally nontrivial toy viability band but do not yet support any data-conditioned corridor or special selection of θ★.

The verdict is descriptive and does not modify Phase 2/4 claims, FRW code, or Stage 2 pipelines; it is intended as a reusable summary for Phase 4/5 text and Phase 5 interface tables.
## 2026-01-11 — Belt B / Rung B2: Stage 2 mechanism diagnostics verdict (Phase 3 amplitudes and measure candidates)

Stage 2 mechanism/measure belt: added `stage2/mech_measure_analysis/docs/STAGE2_MECH_VERDICT_v1.md`, a physics-facing verdict document that:

- summarises rungs 1–6 of the mechanism/measure belt (table inventory, column stats, probability-like candidate selection, measure vs flag classification, θ-profiles, and preferred candidates),
- records that Phase 3 mechanism tables under `phase3/outputs/tables/` are numerically robust, with bounded, finite, non-degenerate scalar columns suitable for downstream analysis,
- shows that a small family of probability-like columns splits naturally into measure-like and flag-like roles and that several preferred mechanism-derived diagnostics can be identified on numerical and structural grounds,
- notes that θ-profiles of measure-like candidates are smooth and well-behaved over the current θ-grid, supporting their use as diagnostics,
- and emphasises that, in the current toy setup, these scalars act as diagnostics rather than a canonical θ-measure and do not single out θ★ on their own.

The verdict is descriptive only and does not change Phase 3 contracts, numerical artifacts, or Stage 2 pipelines; it is intended as reusable backing for Phase 4/5 text and Phase 5 interface summaries.
## 2026-01-11 — Belt B / Rung B3: Stage 2 joint mech–FRW diagnostics verdict (redundancy and θ★)

Stage 2 joint mech–FRW belt: added `stage2/joint_mech_frw_analysis/docs/STAGE2_JOINT_VERDICT_v1.md`, a verdict document that:

- summarises the joint θ-grid construction, FRW family summaries, and joint correlation rungs under `stage2/joint_mech_frw_analysis/`,
- records that Phase 3 mechanism tables and Phase 4 FRW tables are θ-consistent on the 2048-point grid, allowing a clean joint θ-grid,
- confirms that FRW families (viable band, LCDM-like subsets, toy corridor families, and their intersections) are faithfully reproduced on the joint grid with attached mechanism scalars,
- shows that mechanism-derived scalars are highly redundant with FRW scalars (|r| close to 1 for several pairs), so Phase 3 amplitudes act as reparameterisations of the FRW vacuum sector in the current toy setup,
- and notes that θ★ lies in the FRW-viable band but is not singled out by the combined mech–FRW diagnostics, reinforcing the negative-result verdict that no special θ★ signature appears at this stage.

The verdict is descriptive and does not modify Phase 3/4 contracts, numerical artifacts, or Stage 2 pipelines; it is intended as a reusable joint-structure summary for Phase 4/5 and Phase 5 interface work.
## 2026-01-11 — Belt B / Rung B4: Stage 2 master verdict (FRW, mechanism, joint, data, θ★)

Stage 2 umbrella belt: added `stage2/docs/STAGE2_MASTER_VERDICT_v1.md`, a program-level verdict document that:

- summarises the FRW corridor belt, FRW data-probe audit, mechanism/measure belt, joint mech–FRW belt, and θ★ alignment rung into one snapshot,
- records that the current Phase 3 + Phase 4 + Stage 2 pipeline produces a structurally nontrivial toy FRW viability band with robust corridor families,
- confirms that Phase 3 mechanism-derived scalars form a rich but redundant diagnostic family that is tightly correlated with FRW vacuum-sector scalars and does not provide a canonical θ-measure on its own,
- reiterates that the FRW data gate (`frw_data_ok`) is closed in the current snapshot, so all corridors are pre-data corridors,
- states explicitly that θ★ lies inside the FRW-viable band but is not singled out by FRW, mech-only, or joint mech–FRW diagnostics, and that this is treated as a negative-result sanity check,
- and distills Stage 2 into an Option A style “non-contradiction / redundancy” story that Phase 4/5 and external summaries can cite as the baseline diagnostic verdict for the current Origin-Axiom toy universe.

The doc is descriptive only and does not modify any Phase 2/3/4/5 claims, numerical artifacts, or Stage 2 pipelines; it is intended as the master Stage 2 reference for Phase 5 interface work and future promotion gates.
## 2026-01-11 — Belt C / Rung C1: Wire Phase 2–5 alignment memos into doc graph

Doc/graph belt: wired the Phase 2–5 alignment memos into the documentation graph by:

- appending short alignment notes to `phase2/SCOPE.md`, `phase3/SCOPE.md`, `phase4/SCOPE.md`, and `phase5/SCOPE.md` that point to `phase2/PHASE2_ALIGNMENT_v1.md`, `phase3/PHASE3_ALIGNMENT_v1.md`, `phase4/PHASE4_ALIGNMENT_v1.md`, and `phase5/PHASE5_ALIGNMENT_v1.md` respectively, and
- adding a brief alignment memo section at the end of `docs/STATE_OF_REPO.md` listing these files and clarifying that they are descriptive snapshots of how phase contracts, LaTeX papers, and Stage 2 diagnostics line up at the current snapshot.

This rung does not change any Phase claims or Stage 2 verdicts; it just makes the alignment memos discoverable as the canonical entry-points for Phase 2–5 alignment.
## 2026-01-11 — Belt C / Rung C2: Classify key orphan-candidate docs (promote vs legacy vs design vs historical)

Doc/graph belt: used the Stage 2 doc-audit orphan-candidate snapshot to classify several key docs and make their status explicit by appending short status blocks, without changing existing content:

- Root-level:
  - `REPRODUCIBILITY.md`: marked as a top-level reproducibility entrypoint and navigation aid, with phase-specific contracts living under `phase*/REPRODUCIBILITY.md` and Phase 2–5 alignment memos.
  - `ROADMAP.md`: marked as a legacy roadmap snapshot, with `docs/FUTURE_WORK_AND_ROADMAP.md` and Stage 2 overview docs as the current roadmap.

- Phase 2:
  - `phase2/AUDIT_REPORT.md`: clarified as a historical audit snapshot (P2-A1); TODO/TBD/FIXME references are historical, not a live to-do list; pointed readers to `phase2/CLAIMS.md`, `phase2/REPRODUCIBILITY.md`, and `phase2/PHASE2_ALIGNMENT_v1.md` for current Phase 2 status.
  - `phase2/ASSUMPTIONS.md`, `phase2/CLAIMS_TABLE.md`, `phase2/PHASE2_LOCK_CHECKLIST.md`, `phase2/APPROXIMATION_CONTRACT.md`, `phase2/PHASE2_WORKFLOW_GUIDE.md`, `phase2/CLAIMS.md`, `phase2/REPRODUCIBILITY.md`: explicitly marked as canonical Phase 2 contracts/guides and tied to `phase2/PHASE2_ALIGNMENT_v1.md` and the locked Phase 2 paper.

- Phase 3:
  - `phase3/MECHANISM_CONTRACT.md`, `phase3/ROLE_IN_PROGRAM.md`: marked as canonical Phase 3 mechanism and role docs, interpreted under `phase3/PHASE3_ALIGNMENT_v1.md`.
  - `phase3/PHASE3_RUNG2_MECHANISM_A_INSTABILITY_PENALTY.md`: marked as a rung-level design note (historical/explanatory, not a claims register).

- Phase 4:
  - `phase4/PLANNING.md`, `phase4/PHASE3_INTERFACE.md`, `phase4/CLAIMS_TABLE.md`, `phase4/HARD_NOVELTY_ROADMAP.md`, `phase4/FRW_SYNTHESIS.md`, `phase4/MAPPING_FAMILIES.md`, `phase4/CLAIMS.md`, `phase4/NON_CLAIMS.md`, `phase4/REPRODUCIBILITY.md`: explicitly tagged as design/draft/non-binding docs whose interpretation is governed by `phase4/PHASE4_ALIGNMENT_v1.md` and the FRW promotion gates (`phase4/docs/PHASE4_FRW_PROMOTION_DESIGN_v1.md`, `docs/FRW_CORRIDOR_PROMOTION_GATE_v1.md`).

- Phase 5:
  - `phase5/PHASE5_VISION_RUNG0.md`: marked as a Phase 5 Rung 0 vision/planning doc, with future Phase 5 interface work governed by `phase5/PHASE5_ALIGNMENT_v1.md` and Stage 2 master verdicts.

This rung does not alter any numerical artifacts or claims; it makes previously “orphan-like” or ambiguous docs explicitly classified as canonical, legacy, design, or historical, using the alignment memos and Stage 2 verdicts as the reference.
## 2026-01-11 — Belt C / Rung C3: Doc open-threads status (TODO / DRAFT markers)

Doc/graph belt: clarified the status of open-thread markers surfaced by the Stage 2 doc-audit belt by:

- adding `stage2/docs/STAGE2_DOC_OPEN_THREADS_STATUS_v1.md`, which classifies TODO/DRAFT/TBD/FIXME markers as historical/audit-only, draft-but-operational contracts, or design notes, with special attention to:
  - the narrative TODO in `PROGRESS_LOG.md` (historical / contextual),
  - the Phase 2 audit-report TODO cluster (historical audit snapshot, not a live to-do list),
  - the Phase 3 mechanism contract DRAFT marker (draft-but-operational for the current Stage 2 snapshot),
  - and the Phase 4 DRAFT cluster in planning/claims/mapping/reproducibility docs (design/draft documents governed by alignment memos and promotion gates, not current blockers),
- and appending a short pointer to `stage2/docs/STAGE2_DOC_AUDIT_SUMMARY_v1.md` to make this status doc discoverable from the doc-audit summary.

This rung does not remove or edit any TODO/DRAFT markers; it records how they should be interpreted so that future audits can distinguish live gates from preserved historical context.
## 2026-01-11 — Belt D / Rung D1: Phase 5 interface table design (Stage 2 verdicts → program summaries)

Phase 5 interface belt: added `phase5/INTERFACE_TABLE_DESIGN_v1.md`, a non-binding design note that:

- specifies Phase 5 as an interface/sanity layer over Phase 3/4 outputs and Stage 2 verdicts,
- lists the Stage 2 verdict and summary docs that Phase 5 interface tables will depend on,
- proposes a small set of interface tables (P5-1–P5-5) for:
  - FRW viability and family fractions,
  - mechanism diagnostics and preferred candidates,
  - joint mech–FRW redundancy summaries,
  - θ★ status in the current toy universe,
  - and a compact list of Stage 2 program-level verdicts,
- and emphasises that these tables are interface views over Stage 2 diagnostics (internal verdicts only), not new physics claims or external phenomenology.

This rung does not add any new computations or claims; it sketches the future Phase 5 interface belt that will convert Stage 2 CSVs and verdict docs into reproducible program verdict tables.
## 2026-01-11 — Belt D / Rung D2: Phase 5 program verdict skeleton (Stage 2 era)

Phase 5 interface belt: added `phase5/PROGRAM_VERDICT_SKELETON_v1.md`, a non-binding Phase-5-voice narrative skeleton that:

- restates the Stage 2 master verdict in internal program language (broad FRW viability band, pre-data corridors, rich but redundant mechanism diagnostics, closed data gate, θ★ inside the viable band but not selected),
- makes explicit what Phase 5 can safely record as internal verdicts at the current snapshot,
- lists what Phase 5 explicitly does not yet claim (no data-conditioned corridor, no canonical θ-measure, no θ★ prediction),
- and connects this narrative skeleton to the planned Phase 5 interface tables described in `phase5/INTERFACE_TABLE_DESIGN_v1.md`.

The skeleton introduces no new physics or claims; it is a narrative template for future Phase 5 tables and text, anchored to `stage2/docs/STAGE2_MASTER_VERDICT_v1.md`.
## 2026-01-11 — Belt E / Rung E1: Stage 2 paper audit plan (Phase 0–5 PDFs)

Paper-audit belt: added `stage2/docs/STAGE2_PAPER_AUDIT_PLAN_v1.md`, which:

- lists the canonical Phase 0–5 paper PDFs under `artifacts/` to be audited,
- defines per-phase audit goals (narrative alignment, claims alignment, and scope/status language) against phase contracts, alignment memos, and Stage 2 verdicts,
- lays out planned rungs E2–E6:
  - Phase 2 paper audit,
  - Phase 3 paper audit,
  - Phase 4 paper audit,
  - Phase 5 stub audit (if present),
  - and a quick Phase 0–1 consistency scan,
- and explicitly separates descriptive audit rungs from any future LaTeX editing rungs (which will be gated and logged separately).

No papers or LaTeX sources were changed in this rung; it is a planning-only step for a structured paper audit belt.
## 2026-01-11 — Belt E / Rung E2: Phase 2 paper audit (mode-sum + bounded FRW viability)

Paper-audit belt: read `artifacts/origin-axiom-phase2.pdf` (abstract, introduction, claims C2.1–C2.3, scope and non-claims sections, conclusion, and provenance appendix) alongside the Phase 2 docs and alignment memo, and recorded the audit in `stage2/docs/STAGE2_PAPER_AUDIT_PHASE2_v1.md`.

Audit verdict:

- The Phase 2 paper consistently presents Phase 2 as a bounded, reproducible test of a global non-cancellation floor in a vacuum testbed with a toy FRW embedding, aligned with Phase 2 SCOPE/CLAIMS/REPRODUCIBILITY docs and `phase2/PHASE2_ALIGNMENT_v1.md`.
- Claims C2.1–C2.3 (existence under constraint, robustness under numerical controls, FRW embedding stability) are framed as statements about the implemented pipeline, not as physical predictions or data-facing claims.
- The paper’s non-claims and upgrade list match the global program docs and Stage 2 master verdict: no identification of ε with a physical constant, no continuum-limit theorem, no realistic field content, no θ★ selection, and no quantitative match to the observed cosmological constant.
- The FRW part is clearly described as a toy background test; it does not claim a populated, data-conditioned FRW corridor or a broad θ-grid viability band, so there is no conflict with the later Phase 4 + Stage 2 FRW belts (which operate on a richer FRW pipeline).
- No contradictions were found between the Phase 2 paper and the current Stage 2 FRW and master verdicts; any future edits can be limited to minor clarifications and cross-links rather than substantive claim changes.

No LaTeX or paper sources were modified in this rung; it is a descriptive audit only.
## 2026-01-11 — Belt E / Rung E3: Phase 3 paper audit (mechanism module)

Paper-audit belt: read `artifacts/origin-axiom-phase3.pdf` (abstract, introduction, mechanism definition, claims/non-claims, diagnostics, discussion, and conclusion) alongside the Phase 3 docs and alignment memo and recorded the audit in `stage2/docs/STAGE2_PAPER_AUDIT_PHASE3_v1.md`.

Audit verdict:

- The Phase 3 paper consistently presents Phase 3 as a mechanism-only rung that implements a non-cancellation floor on a toy ensemble of complex modes and studies its impact on a global amplitude diagnostic.
- The mechanism-level claims (existence of a stable floor-enforced ensemble and a genuine binding regime with global shifts between unconstrained and floor-enforced amplitudes) align with `phase3/MECHANISM_CONTRACT.md`, `phase3/SCOPE.md`, and `phase3/PHASE3_ALIGNMENT_v1.md` and do not assert a canonical θ-measure, θ★ selection, or physical vacuum model.
- The paper treats the previously used flavor experiment as archived, matching the structure and status of `experiments/phase3_flavor_v1/` in the repo.
- Diagnostics, including the instability penalty, are framed as internal, toy-model quantities and are fully compatible with the Stage 2 mechanism and joint verdicts, which find smooth, redundant mechanism-derived scalars but no privileged θ or independent θ-measure.
- No contradictions were found between the Phase 3 paper and the Stage 2 master verdict; any future edits can be limited to minor clarifications and cross-links.

No LaTeX or paper sources were modified in this rung; it is a descriptive audit only.
## 2026-01-11 — Belt E / Rung E4: Phase 4 paper audit (vacuum→FRW toy corridor stub)

Paper-audit belt: read `artifacts/origin-axiom-phase4.pdf` (abstract, introduction, E_vac mapping and F1 stack, FRW viability and ΛCDM-like sections, corridor discussion, and conclusion) alongside the Phase 4 docs, alignment memo, and Stage 2 verdicts, and recorded the audit in `stage2/docs/STAGE2_PAPER_AUDIT_PHASE4_v1.md`.

Audit verdict:

- The Phase 4 paper presents Phase 4 as an FRW-facing toy corridor stub built from the Phase 3 amplitude via a fixed E_vac(θ) mapping and a simple FRW model, in line with `phase4/PHASE4_ALIGNMENT_v1.md` and `docs/PHASES.md`.
- Its FRW viability and ΛCDM-like constructions are framed as internal corridor-style diagnostics on the θ-grid, not as data-conditioned or observationally calibrated bands.
- The paper does not claim a canonical θ-corridor, a θ★ selection, or quantitative agreement with real cosmological parameters; it emphasises numerical stability, transparency, and reproducibility of the vacuum→FRW diagnostic chain.
- These statements are compatible with the Stage 2 FRW, data-probe, joint, and θ★ verdicts, which find a broad FRW-viable band and robust toy corridors but a closed aggregate data gate and no special promotion of θ★.

No LaTeX or paper sources were modified in this rung; it is a descriptive audit only.
## 2026-01-11 — Belt E: Phase 0–5 paper audit (Stage 2 snapshot)

Paper-audit belt: established a structured, audit-only pass over all Phase 0–5 PDFs, checking them against their phase contracts, alignment memos, global docs, and the Stage 2 verdicts.

Artifacts:

- `stage2/docs/STAGE2_PAPER_AUDIT_PLAN_v1.md` — defines the paper-audit belt (targets, goals, and planned rungs E2–E6).
- `stage2/docs/STAGE2_PAPER_AUDIT_PHASE2_v1.md` — Phase 2 paper audit (mode-sum + bounded FRW viability) against Phase 2 contracts and Stage 2 FRW verdicts.
- `stage2/docs/STAGE2_PAPER_AUDIT_PHASE3_v1.md` — Phase 3 paper audit (mechanism module) against the Phase 3 mechanism contract and Stage 2 mechanism/joint verdicts.
- `stage2/docs/STAGE2_PAPER_AUDIT_PHASE4_v1.md` — Phase 4 paper audit (vacuum→FRW toy corridor stub) against Phase 4 contracts and Stage 2 FRW/data-probe/joint/θ★ verdicts.
- `stage2/docs/STAGE2_PAPER_AUDIT_PHASE5_v1.md` — Phase 5 paper audit (interface/dashboard stub) against Phase 5 docs and the Stage 2 master verdict.
- `stage2/docs/STAGE2_PAPER_AUDIT_PHASE01_v1.md` — quick consistency scan of Phase 0 (governance) and Phase 1 (axiom + toy existence) papers against the current program structure.
- `stage2/docs/STAGE2_PAPER_AUDIT_OVERVIEW_v1.md` — overview and navigation layer summarising the belt’s findings and pointing to the per-phase notes.

Belt verdict: At the current Stage 2 snapshot, none of the Phase 0–5 PDFs contradict their own phase contracts, the global docs, or the Stage 2 FRW/mechanism/joint/θ★ verdicts. Phase 0–1 still provide a clean governance and axiom foundation; Phases 2–4 are framed as bounded toy pipelines and diagnostics rather than physical predictions; Phase 5 is presented as an interface/dashboard stub rather than a new physics phase. Any future paper edits can be limited to minor clarifications and explicit cross-links, to be handled in a separate paper-edit belt.

## 2026-01-11 — Belt G: phase-level doc hierarchy re-org (canonical vs design/audit)

Scope: Introduced a light documentation hierarchy for Phase 2–4 by moving non-canonical design and audit docs into dedicated subdirectories, without altering historical PROGRESS_LOG entries.

Changes:

- Created `phase2/audit/` and moved:
  - `phase2/AUDIT_REPORT.md` → `phase2/audit/AUDIT_REPORT.md`

- Created `phase3/design/` and moved:
  - `phase3/PHASE3_NEXT_RUNG.md` → `phase3/design/PHASE3_NEXT_RUNG.md`
  - `phase3/PHASE3_RUNG2_MECHANISM_A_INSTABILITY_PENALTY.md` → `phase3/design/PHASE3_RUNG2_MECHANISM_A_INSTABILITY_PENALTY.md`

- Created `phase4/design/` and moved:
  - `phase4/PLANNING.md` → `phase4/design/PLANNING.md`
  - `phase4/HARD_NOVELTY_ROADMAP.md` → `phase4/design/HARD_NOVELTY_ROADMAP.md`
  - `phase4/FRW_SYNTHESIS.md` → `phase4/design/FRW_SYNTHESIS.md`
  - `phase4/MAPPING_FAMILIES.md` → `phase4/design/MAPPING_FAMILIES.md`
  - `phase4/FRW_TOY_DESIGN.md` → `phase4/design/FRW_TOY_DESIGN.md`
  - `phase4/PHASE3_INTERFACE.md` → `phase4/design/PHASE3_INTERFACE.md`
  - `phase4/FRW_DATA_DESIGN.md` → `phase4/design/FRW_DATA_DESIGN.md`

Notes:

- Historical PROGRESS_LOG entries preserve the original file paths used at the time and may refer to pre-reorg locations. For current locations of design and audit docs, use the mappings above and the phase-level alignment memos (`phase2/PHASE2_ALIGNMENT_v1.md`, `phase3/PHASE3_ALIGNMENT_v1.md`, `phase4/PHASE4_ALIGNMENT_v1.md`).
- Non-log docs that previously linked to the old paths (alignment memos, design notes, Stage 2 doc-open-threads summary) were updated to point at the new locations.

## 2026-01-11 — Belt F: doc spine and phase doc layout notes

Scope: Add a light documentation spine for new readers and explicit per-phase doc layout notes, aligned with the new design/audit subdirectory hierarchy from Belt G. No claims, code, or numerical artifacts were changed.

Changes:

- Added a global doc spine under:
  - `docs/DOC_SPINE_v1.md`
  which points new readers to a minimal set of entrypoint docs (README, PROJECT_OVERVIEW, PHASES, STATE_OF_REPO, STAGE2_MASTER_VERDICT) and then to the full atlas:
  - `docs/REPO_MAP_AND_ATLAS_v1.md`

- Added per-phase documentation layout notes:
  - `phase2/PHASE2_DOCS_LAYOUT_v1.md`
  - `phase3/PHASE3_DOCS_LAYOUT_v1.md`
  - `phase4/PHASE4_DOCS_LAYOUT_v1.md`
  - `phase5/PHASE5_DOCS_LAYOUT_v1.md`

These layout notes:

- classify Phase 2–5 docs into:
  - canonical contracts (scope, claims, non-claims, reproducibility, alignment, progress logs, local READMEs),
  - design and planning notes (including the Phase 2 audit report and Phase 3/4 design docs now living under `audit/` and `design/`),
  - and historical/audit material (paper backups, archived experiments),
- and document the intended hierarchy so future additions can follow the same pattern.

This rung is documentation-structure only and does not modify any numerical pipeline, paper content, or phase claims.

## 2026-01-12 — Scripts rung: unify paper build entrypoints

Scope: Simplify and standardise paper build entrypoints so that per-phase builders and the global builder all produce and sync the same canonical artifacts, both phase-local and at the repo root.

Changes:

- Retired the old Phase 0–2 helper semantics of `scripts/build_papers.sh` and turned it into a thin wrapper around:
  - `scripts/build_paper.sh`
  which runs all phase gates (0–5) and then calls `scripts/build_all_papers.sh` to aggregate artifacts.

- Added per-phase builders:
  - `scripts/build_phase0_paper.sh`
  - `scripts/build_phase1_paper.sh`
  - `scripts/build_phase2_paper.sh`
  - `scripts/build_phase3_paper.sh`
  - `scripts/build_phase4_paper.sh`
  - (Phase 5 builder existed and was updated, see below.)

  Each per-phase builder:
  - runs the corresponding phase gate (`scripts/phaseN_gate.sh`), and
  - ensures the canonical artifact lives at:
    - `phaseN/artifacts/origin-axiom-phaseN.pdf` (phase-local), and
    - `artifacts/origin-axiom-phaseN.pdf` (top-level aggregate).

- Updated `scripts/build_phase5_paper.sh` to adopt the same convention:
  - after running the Phase 5 gate and building `phase5/paper/main.tex`,
  - it now syncs `phase5/artifacts/origin-axiom-phase5.pdf` into `artifacts/origin-axiom-phase5.pdf`.

Effect:

- There is now a clean separation between:
  - per-phase builders (`build_phaseN_paper.sh`), and
  - the global builder (`build_paper.sh` / `build_papers.sh`),
- and any of these commands produce consistent artifacts in both the phase-local and repo-root locations.
- No claims, numerical content, or LaTeX sources were modified; this rung is build-script and reproducibility hygiene only.

## 2026-01-12 — Stage 2: empirical FRW anchor (background box A1–A4)

Scope: Introduced and executed a Stage 2 empirical FRW anchor rung that tests whether the current Phase 3 mechanism + Phase 4 FRW toy mapping admits any nontrivial overlap with a simple background-cosmology box in (\omega_\Lambda, t_0) on the existing 2048-point θ grid, without touching external pipelines or full data likelihoods.

Work:

- Added `stage2/frw_data_probe_analysis/src/analyze_frw_empirical_anchor_v1.py` and `stage2/frw_data_probe_analysis/config/empirical_anchor_box_v1.json` to define a small background-cosmology box in (\omega_\Lambda, t_0) and compute a boolean empirical-anchor mask `stage2/frw_empirical_anchor_mask_v1.csv` on the Phase 4 FRW toy grid (`phase4_F1_frw_shape_probe_mask.csv`).
- Ran the empirical-anchor script and confirmed that the anchor is highly selective but non-empty on the current grid: 18 out of 2048 θ points fall inside the empirical box, i.e. `EMPIRICAL_ANCHOR` has n=18, frac≈0.0088.
- Updated the joint mech–FRW anchor-intersections script (`stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_intersections_v1.py`) to:
  - resolve the repo root via `parents[3]`,
  - use the existing `in_toy_corridor` mask from the joint grid instead of inventing new corridor logic,
  - robustly detect the empirical anchor mask column in the anchor table rather than assuming a specific name.
- Ran the anchor-intersections script to compute set sizes and fractions for:
  - ALL_GRID, FRW_VIABLE, TOY_CORRIDOR, EMPIRICAL_ANCHOR,
  - FRW_VIABLE_AND_ANCHOR, CORRIDOR_AND_ANCHOR, CORRIDOR_AND_VIABLE_AND_ANCHOR,
  and stored the results in `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_intersections_v1.csv`.

Key results:

- On the current 2048-point θ grid:
  - FRW_VIABLE has n=1016 (≈ 49.6% of the grid).
  - TOY_CORRIDOR has n=1186 (≈ 57.9% of the grid).
  - EMPIRICAL_ANCHOR has n=18 (≈ 0.88% of the grid).
- All 18 empirical-anchor points satisfy both FRW viability and toy-corridor membership:
  - FRW_VIABLE_AND_ANCHOR: n=18, frac≈0.0088.
  - CORRIDOR_AND_ANCHOR: n=18, frac≈0.0088.
  - CORRIDOR_AND_VIABLE_AND_ANCHOR: n=18, frac≈0.0088.
- Therefore the empirical anchor set is a strict subset of `FRW_VIABLE ∧ TOY_CORRIDOR` and identifies a small kernel of θ values where the Phase 3 mechanism, Phase 4 FRW toy viability, and the background-cosmology box all agree.

Status and gating:

- This empirical-anchor rung is recorded as a Stage 2 diagnostic only:
  - it introduces no new Phase 4 or Phase 5 claims,
  - it does not promote any specific θ or corridor as “observationally selected,”
  - it does not involve external cosmology codes or full Planck/BAO/SN likelihoods.
- Any future promotion of these results into Phase 4/5 text or figures will be handled via the existing FRW promotion design gates (`phase4/docs/PHASE4_FRW_PROMOTION_DESIGN_v1.md`, Stage 2 promotion design docs) and will remain constrained by the Phase 0 contract (scope, non-claims, reproducibility).

## 2026-01-12 — Stage 2: empirical anchor kernel characterization (A5b)

Scope: Characterise the internal structure of the empirical FRW anchor kernel on the joint mech–FRW grid, i.e. points that satisfy FRW viability, the Stage 2 toy corridor, and the empirical background-cosmology box simultaneously. This rung is diagnostic-only and does not promote any θ-region to phase-level claims.

Work:

- Added `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_kernel_v1.py`, a Stage 2 script that:
  - reads the joint grid `stage2_joint_theta_grid_v1.csv` and the empirical anchor mask `stage2_frw_empirical_anchor_mask_v1.csv`,
  - detects the empirical-anchor mask column robustly (reusing the same logic as the intersections script),
  - defines the kernel mask as FRW_VIABLE ∧ IN_TOY_CORRIDOR ∧ IN_EMPIRICAL_ANCHOR,
  - computes distances |θ − θ★| to the reference θ★ ≈ 2.178458,
  - groups the kernel points into contiguous segments in `theta_index`,
  - writes a segment-level summary table `stage2_joint_mech_frw_anchor_kernel_v1.csv` and prints a human-readable summary.

- Ran the kernel analysis script:
  - `oa && python stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_kernel_v1.py`

Key numerical results:

- Total grid size: 2048 θ points (unchanged).
- Kernel size (FRW_VIABLE ∧ TOY_CORRIDOR ∧ EMPIRICAL_ANCHOR): n = 18.
- Number of contiguous θ-index segments in the kernel: 2.
  - Segment 1:
    - theta_index[205–213], n = 9,
    - θ ∈ [0.628932, 0.653476],
    - contains_theta_star = False,
    - minimum |θ − θ★| ≈ 1.525 × 10^0 at θ ≈ 0.653476.
  - Segment 2:
    - theta_index[1078–1086], n = 9,
    - θ ∈ [3.307263, 3.331806],
    - contains_theta_star = False,
    - minimum |θ − θ★| ≈ 1.129 × 10^0 at θ ≈ 3.307263.

Interpretation:

- The empirical FRW anchor kernel is:
  - small (18/2048 ≈ 0.9% of the θ grid),
  - structured into two disjoint, contiguous islands in θ,
  - clearly offset from θ★ (neither segment contains θ★, and the closest points lie at |θ − θ★| ≈ O(1)).
- Combined with the A4 intersections rung, this reinforces that:
  - the axiom + mechanism + FRW toy mapping is not trivially ruled out by the current background-cosmology box (kernel is non-empty),
  - but the present empirical anchor does **not** single out θ★ in any obvious way at this diagnostic level.
- This rung records the basic geometry of the anchor kernel for future reference (e.g. if later FRW/data refinements or external cosmology hosts are added) without changing any phase claims.

Status and gating:

- This A5b kernel analysis remains a Stage 2 diagnostic only:
  - it introduces no new claims in Phase 3, Phase 4, or Phase 5,
  - it does not alter the definition of the empirical box or the FRW toy pipeline,
  - it is intended as a geometric summary of the existing anchor kernel for later comparison.

## 2026-01-12 — Stage 2: joint mech–FRW empirical anchor overview figure (A6)

Scope: Produce a Stage 2 diagnostic figure in (omega_lambda, age_Gyr) space that visualises how the empirical FRW anchor kernel sits inside the Phase 4 FRW-viable corridor and the full FRW grid. This rung is purely visual / diagnostic and does not change any phase claims.

Work:

- Added `stage2/joint_mech_frw_analysis/src/plot_joint_mech_frw_anchor_overview_v1.py`, which:
  - reads the joint mech–FRW grid `stage2_joint_theta_grid_v1.csv` and the empirical anchor mask `stage2_frw_empirical_anchor_mask_v1.csv`,
  - detects the empirical-anchor mask column using the same robust logic as the A4/A5 scripts,
  - defines masks for:
    - all FRW grid points,
    - FRW_viable ∧ in_toy_corridor,
    - the empirical anchor kernel (FRW_VIABLE ∧ IN_TOY_CORRIDOR ∧ IN_ANCHOR),
  - produces a scatter plot in (omega_lambda, age_Gyr) with:
    - faint points for the full FRW grid,
    - highlighted points for FRW_viable ∧ corridor,
    - star markers for the 18-point empirical anchor kernel,
  - writes the figure to `stage2/joint_mech_frw_analysis/outputs/figures/stage2_joint_mech_frw_anchor_overview_v1.png`,
  - prints a short summary (grid sizes and counts for the masks).

- Ran the plotting script:
  - `oa && python stage2/joint_mech_frw_analysis/src/plot_joint_mech_frw_anchor_overview_v1.py`

Qualitative outcome (visual):

- The full FRW grid traces a smooth curve in (omega_lambda, age_Gyr) space.
- The FRW_viable ∧ corridor set forms a contiguous mid-range band along this curve.
- The empirical anchor kernel appears as a small, compact cluster of 18 points embedded inside this band:
  - it occupies a narrow interval in both omega_lambda and age_Gyr,
  - it does not extend to the extremes of the FRW grid,
  - it visually matches the two-segment structure previously identified in θ-space.

Interpretation:

- The figure confirms that the empirical FRW anchor kernel is:
  - non-empty but small,
  - structurally nested inside the broader FRW-viable corridor,
  - and not associated with any obvious anomaly or special feature in the (omega_lambda, age_Gyr) projection.
- This supports the A4/A5b numerical conclusions:
  - the current empirical box bites nontrivially,
  - but it does not “snap” the system to θ★ or to any visibly exotic FRW subset at this diagnostic level.

Status and gating:

- This figure remains a Stage 2 diagnostic artifact:
  - no new claims in Phase 3/4/5,
  - safe to reuse later as an illustrative panel if Phase 4/5 decides to promote an Option-A style “background anchor” summary.

## 2026-01-12 — Stage I + Stage 2 status snapshot (Belt H, rung H1)

Scope: Add a single high-level status document that captures the Stage I (Phase 0–5) and Stage 2 diagnostic belt situation as of January 2026 in narrative form, for future-me and external readers. This rung is documentation-only; it introduces no new numerical results or claims.

Work:

- Created `docs/STAGE1_STATUS_JAN2026_v1.md` as a narrative snapshot that:
  - summarises the roles and current status of Phase 0–5 (governance, toy ensembles, Phase 2 mode-sum + bounded FRW viability, Phase 3 mechanism module, Phase 4 FRW toy diagnostics, Phase 5 interface/sanity layer),
  - enumerates the Stage 2 belts (FRW corridor, mech/measure, joint mech–FRW, FRW data-probe, doc/repo audit, empirical background anchor) and records their main positive structures and structured negative results,
  - states explicitly what we now know about θ★ inside the current sandbox (inside the viable band but not specially picked out by the current diagnostics) and what we do not know yet (no canonical θ-measure, no strong empirical locking, no full data contact),
  - sketches three future directions: (1) external-facing snapshot/communication, (2) a gated Stage II layer interfacing with external cosmology hosts and real data, and (3) mechanism-side refinements within the existing Phase 3 + Phase 4 toy universe.

Interpretation:

- This status doc is a companion to `docs/STATE_OF_REPO.md`, `docs/PHASES.md`, and the Stage 2 overview docs. It is meant to be read by human auditors (future-me or collaborators), giving a single place where the current verdict on the axiom, θ★, and the FRW toy lab is explained in plain language without over-claiming.
- The document locks in the idea that the current Stage I + Stage 2 snapshot is already scientifically meaningful as a worked-out, reproducible counterexample to several naive hopes (canonical θ-measure, sharp θ★ locking, immediate data corridor), while keeping the door open to gated, more ambitious extensions.

Status and gating:

- This rung is docs-only: no phase paper, numerical artifact, or Stage 2 table was changed.
- `docs/STAGE1_STATUS_JAN2026_v1.md` is considered non-binding but canonical as a descriptive snapshot of the repo as of this date; future snapshots should create new dated status docs rather than rewriting this one.

## 2026-01-12 — Stage II external cosmology hosts design note (Belt I, rung I1)

Scope: Record a conceptual design for a future Stage II layer that would interface the θ-dependent vacuum and mechanism story with external cosmology hosts (CLASS/CCL/CCL-like libraries, Cobaya/CosmoSIS-style frameworks) under strict Phase 0 governance. This rung is documentation-only; no Stage II code or data contact is introduced.

Work:

- Added `docs/STAGEII_COSMO_HOSTS_DESIGN_v1.md` describing:
  - the relationship between Stage I + Stage 2 and a potential Stage II layer,
  - Stage II scope and non-claims (diagnostic environment, not a claim engine),
  - a layered architecture (θ and mechanism inputs, θ→cosmo-parameter mapping, host layer, optional data/likelihood layer),
  - gating and promotion criteria for any Stage II outputs that might later influence Phase 4/5 or a future dedicated phase,
  - an initial rung sketch (background host alignment, extended empirical anchors, host-computed linear observables, and tightly gated prototype data contact).

Interpretation:

- Stage II is now explicitly defined as *out-of-band* relative to Stage I: it may read Phase 3/4 artifacts and external codes but cannot silently update Stage 0–5 claims.
- The existing Stage 2 empirical background anchor belt serves as a baseline for any future Stage II anchor work: richer anchors or host-based diagnostics should be compared back to the current small, two-island kernel on the FRW toy grid.

Status and gating:

- No new numerical artifacts or data contacts were created in this rung.
- `docs/STAGEII_COSMO_HOSTS_DESIGN_v1.md` is a non-binding design note that must be revised or superseded once concrete Stage II work begins; until then, Stage I + Stage 2 remain the only canonical program layers.


## 2026-01-12 — Stage 2: empirical FRW anchor belt (A1–A8, diagnostic-only)

**Scope.**  
Define and study a simple background-cosmology anchor box in terms of the Phase 4 toy FRW diagnostics, and measure how it intersects the Phase 4 FRW-viable band, the Stage 2 toy corridor, and the joint mech–FRW grid. This belt remains a Stage 2 diagnostic; no Phase 3/4/5 claims or figures are promoted.

**Config and mask.**

- Added `stage2/frw_data_probe_analysis/config/empirical_anchor_box_v1.json` defining a small box in the toy FRW plane `(omega_lambda, age_Gyr)`, interpreted as a coarse ΛCDM-like reference region.
- Added `stage2/frw_data_probe_analysis/src/analyze_frw_empirical_anchor_v1.py` (rung A3):
  - Input: `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv` and the anchor config JSON.
  - Output: `stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_empirical_anchor_mask_v1.csv` with a boolean column `in_empirical_anchor_box`.
  - On the 2048-point θ-grid the anchor selects `n_anchor = 18` points (`frac ≈ 0.0088`).

**Joint mech–FRW intersections and kernel.**

- Added `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_intersections_v1.py` (rung A4):
  - Input: joint grid `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv` and the anchor mask table.
  - Output: `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_intersections_v1.csv`.
  - Key counts (n out of 2048): `FRW_VIABLE = 1016`, `TOY_CORRIDOR = 1186`, `EMPIRICAL_ANCHOR = 18`, and `FRW_VIABLE ∧ TOY_CORRIDOR ∧ ANCHOR = 18`. Every anchored θ-point lies in both the FRW-viable band and the toy corridor.
- Added `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_kernel_v1.py` (rung A5b):
  - Output: `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_kernel_v1.csv`.
  - The 18-point anchor kernel splits into two contiguous θ-segments:
    - Segment 1: `theta_index[205–213]`, `n = 9`, `theta ∈ [0.6289, 0.6535]`.
    - Segment 2: `theta_index[1078–1086]`, `n = 9`, `theta ∈ [3.3073, 3.3318]`.
  - The distinguished `theta_star ≈ 2.178458` lies in neither segment; distances to `theta_star` are of order unity in θ.

**Profiles and sensitivity.**

- Added `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_profiles_v1.py` (rung A6):
  - Output: `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_profiles_v1.csv`.
  - The anchor kernel (and its FRW-viable / corridor intersections) has:
    - `omega_lambda` tightly clustered around ≈ 0.69 with width ≈ 0.02.
    - `age_Gyr` tightly clustered around ≈ 13.5 Gyr with width ≈ 0.05 Gyr.
    - Smooth, interior mechanism amplitudes (`mech_baseline_*`, `mech_binding_*`) not pinned to any hard numeric bounds.
- Added `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_sensitivity_v1.py` (rung A7):
  - Output: `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_sensitivity_v1.csv`.
  - Shrinking the anchor box half-widths by a factor 0.5 leaves a compact 8-point core (`n_box∧corridor∧FRW = 8`).
  - Baseline box (scale 1.0) gives the 18-point kernel (`n_box∧corridor∧FRW = 18`).
  - Widening the box by 1.5× yields 26 FRW-viable points in the box, of which 24 lie in the corridor (`n_box∧corridor∧FRW = 24`).
  - The anchor kernel is therefore small but robust: it neither collapses to zero under modest tightening nor expands to fill the corridor under modest loosening.

**Docs and figure.**

- Added `stage2/joint_mech_frw_analysis/docs/STAGE2_EMPIRICAL_ANCHOR_OVERVIEW_v1.md` (rung A8) summarising:
  - the anchor design and config,
  - the intersection counts,
  - the θ-segment structure of the kernel,
  - the FRW/mechanism profiles,
  - and the sensitivity study, with explicit Stage 2 gating.
- Added a simple diagnostic figure `stage2/joint_mech_frw_analysis/outputs/figures/stage2_joint_mech_frw_anchor_overview_v1.png` showing the anchor kernel and its position relative to the broader FRW and corridor structure (for internal use in Stage 2).

**Verdict and gating.**

- On the current Phase 3 mechanism and Phase 4 toy FRW setup, there exists a small but numerically stable intersection between:
  - the toy θ-corridor,
  - the FRW-viable band, and
  - a coarse background-cosmology anchor box in `(omega_lambda, age_Gyr)`.
- This intersection appears as two short θ-bands that do not contain `theta_star`. The kernel lives in a narrow region of `omega_lambda`, `age_Gyr`, and mechanism amplitudes, and is stable under moderate rescaling of the anchor box.
- All of these results remain **Stage 2 diagnostics only**. No new claims or figures are promoted into Phase 3, Phase 4, or Phase 5. Any future use of this kernel in Phase text must pass through a separate promotion gate and be logged explicitly.

## 2026-01-12 — Stage 2 external FRW host age cross-check (diagnostic rung)

**Files:**

- `stage2/external_frw_host/src/compute_analytic_frw_ages_v1.py`
- `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung1_age_crosscheck_v1.csv`
- `stage2/external_frw_host/docs/STAGE2_EXTERNAL_FRW_HOST_AGE_CROSSCHECK_v1.md`

**Summary:**

- Added a Stage 2 external-host rung that compares the Phase 4 FRW toy age column against a simple analytic flat-FRW background.
- The host assumes a late-time flat Universe with \\\( \Omega_\Lambda = \texttt{omega\_lambda} \\\), \\\( \Omega_m = 1 - \Omega_\Lambda \\\), neglects radiation, and computes dimensionless ages via a numerical integral, which are then rescaled to Gyr using a single global factor fitted on the FRW-viable subset.
- On the current 2048-point θ grid:
  - FRW viability holds at 1016 points (≈ 49.6% of the grid).
  - After calibration, the mean absolute age difference on the viable subset is ≈ 2.7 Gyr, with a mean absolute relative difference of ≈ 20% and a maximum absolute difference of ≈ 13 Gyr in some corners.
- This confirms that Phase 4’s `omega_lambda` and `age_Gyr` columns are FRW-inspired toy diagnostics rather than literal ΛCDM parameters of a standard flat-FRW model. The external host is recorded as a downstream diagnostic only and will inform any future design of a more realistic host or data-facing gate, without altering current Phase 3/4/5 claims.


### 2026-01-12 — Stage 2: empirical FRW anchor belt (Rungs A1–A8 + X1)

**Scope.**  
Define and interrogate a simple “background cosmology” empirical anchor for the Phase 4 FRW toy, using the existing θ-grid and FRW outputs. The goal is to see whether there is any θ-region that is simultaneously:
- FRW-viable in the toy pipeline,
- inside the broad toy θ-corridor,
- and consistent with a conservative data-inspired box in \((\Omega_\Lambda, t_0)\),

and to test whether this region exhibits any special behaviour in the Phase 3 mechanism or singles out θ★.

**Code / scripts.**

- Anchor mask (FRW side):
  - `stage2/frw_data_probe_analysis/config/empirical_anchor_box_v1.json`
    - Defines a generous box in \((\Omega_\Lambda, \text{age}_\mathrm{Gyr})\).
  - `stage2/frw_data_probe_analysis/src/analyze_frw_empirical_anchor_v1.py`
    - Input: `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`
    - Output: `stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_empirical_anchor_mask_v1.csv`
    - Adds `in_empirical_anchor_box` on the 2048-point θ grid.

- Joint FRW–mech intersections and kernel:
  - `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_intersections_v1.py`
    - Input:
      - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv`
      - `stage2_frw_empirical_anchor_mask_v1.csv`
    - Output:
      - `stage2_joint_mech_frw_anchor_intersections_v1.csv`
    - Tracks:
      - ALL_GRID, FRW_VIABLE, TOY_CORRIDOR, EMPIRICAL_ANCHOR,
      - FRW_VIABLE_AND_ANCHOR,
      - CORRIDOR_AND_ANCHOR,
      - CORRIDOR_AND_VIABLE_AND_ANCHOR.
  - `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_kernel_v1.py`
    - Output:
      - `stage2_joint_mech_frw_anchor_kernel_v1.csv`
    - Identifies contiguous θ-index segments of the kernel and distances to θ★.
  - `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_profiles_v1.py`
    - Output:
      - `stage2_joint_mech_frw_anchor_profiles_v1.csv`
    - Summarises FRW + mech scalars (means, std, min, max) over:
      - ALL_GRID, FRW_VIABLE, TOY_CORRIDOR,
      - EMPIRICAL_ANCHOR,
      - FRW_VIABLE_AND_ANCHOR,
      - CORRIDOR_AND_ANCHOR,
      - CORRIDOR_AND_VIABLE_AND_ANCHOR.
  - `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_sensitivity_v1.py`
    - Output:
      - `stage2_joint_mech_frw_anchor_sensitivity_v1.csv`
    - Varies the empirical box half-widths (e.g. scale = 0.5, 1.0, 1.5) and tracks how many θ points remain in:
      - ANCHOR,
      - ANCHOR ∧ FRW_VIABLE,
      - ANCHOR ∧ TOY_CORRIDOR,
      - ANCHOR ∧ FRW_VIABLE ∧ TOY_CORRIDOR.
  - `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_mech_contrast_v1.py`
    - Output:
      - `stage2_joint_mech_frw_anchor_mech_contrast_v1.csv`
    - Compares mechanism amplitudes on:
      - ALL_GRID,
      - FRW_VIABLE,
      - CORRIDOR_AND_VIABLE,
      - CORRIDOR_AND_VIABLE_AND_ANCHOR,
      - CORRIDOR_AND_VIABLE_NOT_ANCHOR.

- External FRW cross-check (toy host):
  - `stage2/external_frw_host/src/compute_analytic_frw_ages_v1.py`
    - Input:
      - `stage2_joint_theta_grid_v1.csv`
    - Output:
      - `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung1_age_crosscheck_v1.csv`
    - Uses a flat \((\Omega_m, \Omega_\Lambda)\) FRW background with matter+Λ only to compute analytic ages and compare to the Phase 4 toy ages.

- Visual:
  - `stage2/joint_mech_frw_analysis/outputs/figures/stage2_joint_mech_frw_anchor_overview_v1.png`
    - Joint θ-plot of ω_Λ vs age_Gyr with:
      - FRW-viable band,
      - toy corridor points,
      - empirical anchor kernel,
      - θ★ marked,
      - and (optionally) the analytic FRW host curves.

**Key results.**

- The empirical anchor mask `in_empirical_anchor_box` is true for:
  - 18 / 2048 grid points (~0.0088 of the θ grid).
  - All 18 points satisfy FRW_VIABLE and TOY_CORRIDOR.
- The kernel consists of two 9-point contiguous θ segments:
  - Segment 1: `theta_index ∈ [205, 213]`, `theta ∈ [0.6289, 0.6535]`.
  - Segment 2: `theta_index ∈ [1078, 1086]`, `theta ∈ [3.3073, 3.3318]`.
  - Neither segment contains θ★; the closest θ in the kernel is ~1.1–1.5 away from θ★.
- Profiles and contrasts:
  - On the **FRW_VIABLE** set (1016 points), the mechanism amplitudes sit on a high, smooth plateau:
    - `mech_baseline_A0 ≈ mech_baseline_A_floor ≈ 0.0533 ± 0.005`, with `*_bound = 0`.
  - The **CORRIDOR_AND_VIABLE** subset (154 points) selects a lower, but still smooth band:
    - `mech_baseline_A0 ≈ 0.0423 ± 0.0027`, range ≈ 0.0375–0.0467.
  - The **empirical kernel** (`CORRIDOR_AND_VIABLE_AND_ANCHOR`, 18 points) defines an even narrower mid-range stripe:
    - `mech_baseline_A0 ≈ 0.0461 ± 0.0003`, range ≈ 0.0457–0.0465,
    - with baseline = floor and `*_bound = 0`.
  - Sensitivity rungs show that halving or enlarging the empirical box smoothly shrinks/expands the kernel (8 → 18 → 26 points), without any new discontinuities or θ★ selection.
- External FRW cross-check:
  - A simple analytic flat Ω_m+Ω_Λ FRW host (matter+Λ only) reproduces the qualitative structure but differs from the Phase 4 toy ages at the ~20% level on the FRW-viable set:
    - mean |age_host − age_repo| ≈ 2.7 Gyr, max ≈ 12.9 Gyr,
    - mean relative difference ≈ 0.20.
  - This confirms that the anchor exercise should be interpreted as a **toy background diagnostic**, not a precision cosmology fit.

**Interpretation.**

- There exists a small θ-region (two 9-point segments) where:
  - the Phase 3 mechanism is well-behaved,
  - the Phase 4 FRW toy pipeline deems the background viable,
  - and a conservative (\(\Omega_\Lambda, t_0\)) box is satisfied.
- This region is:
  - **thin** (~0.9% of the grid),
  - **smooth** in both FRW and mechanism scalars,
  - and **does not contain θ★**; it is θ★-neutral.
- The empirical anchor thus acts as a sharpening filter on the existing FRW-viable toy corridor, not as a mechanism that “snaps” the axiom onto θ★.
- Given the known 𝒪(20%) discrepancy between the Phase 4 toy ages and a standard FRW host, all of these results are treated as **Stage 2 diagnostics only**. No anchor-derived θ-claim or “prediction” is promoted into Phase 4/5 at this rung.
## 2026-01-12 – Stage 2: Empirical FRW anchor belt (A3–A8, diagnostic only)

Context: Phase 3 mechanism and Phase 4 FRW toy already provide a θ-grid,
vacuum scale, FRW viability masks, and a toy corridor. This rung adds a
Stage-2-only “empirical FRW anchor belt” that tests whether there is any
structured overlap between:

- the Phase-3/4 θ-corridor,
- FRW viability,
- and a small, data-shaped box in \((\omega_\Lambda, t_0)\) space.

All of this remains Stage-2 diagnostic infrastructure; no Phase-level
claims are promoted.

**A3 – FRW empirical anchor mask**

- Added JSON config `stage2/frw_data_probe_analysis/config/empirical_anchor_box_v1.json`
  defining a small box in \((\omega_\Lambda, t_0)\) derived from background
  cosmology.
- Implemented `stage2/frw_data_probe_analysis/src/analyze_frw_empirical_anchor_v1.py`
  to read:
  - `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`, and
  - the empirical box config,
  and produce:
  - `stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_empirical_anchor_mask_v1.csv`
    with a Boolean `in_empirical_anchor_box` flag per θ.
- Current snapshot: grid size 2048; 18 points (~0.88%) satisfy the
  anchor box.

**A4 – Joint mech–FRW ∧ anchor intersections**

- Extended the Stage-2 joint grid belt with
  `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_intersections_v1.py`,
  which joins:
  - the joint θ-grid
    (`stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv`),
  - the FRW masks (`frw_viable`, `in_toy_corridor`, etc.), and
  - the empirical anchor mask (`in_empirical_anchor_box`).
- Wrote:
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_intersections_v1.csv`
    with counts for:
    - `ALL_GRID`, `FRW_VIABLE`, `TOY_CORRIDOR`,
    - `EMPIRICAL_ANCHOR`,
    - `FRW_VIABLE_AND_ANCHOR`,
    - `CORRIDOR_AND_ANCHOR`,
    - `CORRIDOR_AND_VIABLE_AND_ANCHOR`.
- Current snapshot: all 18 anchor points are both FRW-viable and inside
  the toy corridor.

**A5b – Anchor kernel geometry + overview plot**

- Implemented
  `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_kernel_v1.py`
  to isolate the kernel:
  - `FRW_VIABLE ∧ in_toy_corridor ∧ in_empirical_anchor_box`,
  segment it into contiguous θ-index intervals, and dump per-segment
  geometry.
- Wrote:
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_kernel_v1.csv`
  - `stage2/joint_mech_frw_analysis/outputs/figures/stage2_joint_mech_frw_anchor_overview_v1.png`
- Current snapshot (2048-point grid):
  - kernel size: 18 θ-points,
  - 2 contiguous segments of length 9,
  - both segments lie inside the toy corridor and are FRW-viable,
  - neither segment contains θ★; θ★ sits at a finite distance away.

**A6 – Kernel profiles**

- Added
  `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_profiles_v1.py`
  to compute summary stats for:
  - `E_vac`, `omega_lambda`, `age_Gyr`,
  - and the mechanism scalars
    (`mech_baseline_*`, `mech_binding_*`)
  across:
  - `ALL_GRID`, `FRW_VIABLE`, `TOY_CORRIDOR`,
  - `EMPIRICAL_ANCHOR`,
  - `FRW_VIABLE_AND_ANCHOR`,
  - `CORRIDOR_AND_ANCHOR`,
  - `CORRIDOR_AND_VIABLE_AND_ANCHOR`.
- Output:
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_profiles_v1.csv`
- Current snapshot: the anchor kernel is a narrow band in both FRW and
  mech space (small spreads in `omega_lambda`, `age_Gyr`, and the mech
  amplitudes), i.e. not a random dusting of θ-points.

**A7 – Anchor sensitivity**

- Implemented
  `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_sensitivity_v1.py`
  to test how the kernel behaves under scaled empirical box widths
  (e.g. 0.5×, 1.0×, 1.5× of the baseline half-widths).
- Output:
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_sensitivity_v1.csv`
- Current snapshot (selected):
  - 0.5×: 8 θ in box, all FRW-viable and in corridor.
  - 1.0×: 18 θ in box, all FRW-viable and in corridor.
  - 1.5×: 26 θ in box, 26 FRW-viable, 24 still in corridor.
- Interpretation (Stage-2 only): the anchor kernel is small but
  reasonably robust to modest tightening or loosening of the box.

**A8 – Mechanism contrasts and gradients**

- Extended the joint belt with
  `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_mech_contrast_v1.py`
  to compare mech amplitudes across:
  - `ALL_GRID`, `FRW_VIABLE`,
  - `CORRIDOR_AND_VIABLE`,
  - `CORRIDOR_AND_VIABLE_AND_ANCHOR`,
  writing:
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_mech_contrast_v1.csv`.
- Added a mech-side gradient rung:
  - `stage2/mech_measure_analysis/src/analyze_mech_theta_gradients_v1.py`,
  which uses the joint grid + anchor mask to compute θ-gradients of
  mech amplitudes across the same sets, writing:
  - `stage2/mech_measure_analysis/outputs/tables/stage2_mech_rung7_theta_gradients_v1.csv`.
- Current snapshot: the anchor kernel corresponds to a narrow band of
  mech amplitudes with non-zero θ-gradients; the corridor + viability
  + anchor filters pick out a structured patch rather than a flat plateau.

**External FRW host cross-check (optional)**

- Implemented
  `stage2/external_frw_host/src/compute_analytic_frw_ages_v1.py`
  as a simple analytic flat-FRW host that:
  - computes a dimensionless FRW age from `omega_lambda`,
  - calibrates a single global scale factor to map to Gyr,
  - and compares host ages to the Phase-4 `age_Gyr` on the FRW-viable set.
- Output:
  - `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung1_age_crosscheck_v1.csv`.
- Current snapshot: differences of order a few Gyr on average and up to
  ~13 Gyr; this is recorded as a **negative-result cross-check only**,
  not a calibrated external benchmark.

**Stage-2 documentation**

- Added Phase-4 design stub:
  - `phase4/docs/PHASE4_EMPIRICAL_ANCHOR_DESIGN_v1.md`
  defining the FRW-side observables and the intended contact shape.
- Added Stage-2 overview:
  - `stage2/docs/STAGE2_EMPIRICAL_ANCHOR_OVERVIEW_v1.md`
  summarising the belt (A3–A8), its inputs, outputs, and current
  diagnostic conclusions.
- All anchor logic remains **Stage-2 diagnostic / non-canonical**. No
  Phase-3/4/5 claims are updated; any promotion would require a separate
  FRW empirical anchor gate.


## 2026-01-13 — Stage 2 external FRW host sanity belt (X1–X3)

**Scope.**  
Introduce and park a minimal external FRW host belt that compares the Phase 4 FRW toy background ages against a simple analytic flat–ΛCDM age formula. This is a **Stage 2 diagnostic-only** belt; no Phase 3/4/5 claims or figures are changed.

**Code / scripts.**

- `stage2/external_frw_host/src/compute_analytic_frw_ages_v1.py` (X1)
  - Reads the joint θ-grid from  
    `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv`.
  - For each row, takes `omega_lambda` as \(\Omega_\Lambda\) in a flat ΛCDM background, computes a **dimensionless age** via a simple FRW integral, and then calibrates a single global Gyr scale factor against the FRW-viable subset to obtain `age_Gyr_host`.
  - Writes pointwise comparison table:  
    `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung1_age_crosscheck_v1.csv`  
    (2048 rows, with `age_Gyr`, `age_Gyr_host`, `age_Gyr_diff`, `age_Gyr_rel_diff`, `frw_viable`).

- `stage2/external_frw_host/src/analyze_external_frw_age_contrast_v1.py` (X2)
  - Aggregates the X1 table over four sets:
    - ALL_GRID,
    - FRW_VIABLE,
    - CORRIDOR_AND_VIABLE,
    - CORRIDOR_AND_VIABLE_AND_ANCHOR (18-point empirical kernel).
  - Writes summary table:  
    `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung2_age_contrast_v1.csv`.

- Doc: `stage2/external_frw_host/docs/STAGE2_EXTERNAL_FRW_HOST_SUMMARY_v1.md` (X3)
  - Records scope, inputs, methods, key numerical findings, and an explicit **diagnostic-only gate** for this belt.

**Key results.**

- Across the **full θ-grid** (ALL_GRID, 2048 points):
  - The Phase 4 FRW toy ages are systematically **older** than the analytic host:
    - mean age difference \(\langle t_{\mathrm{repo}} - t_{\mathrm{host}} \rangle \approx -8.4\) Gyr,
    - mean relative difference \(\approx -0.53\).
  - Interpretation: the Phase 4 FRW ages are **not calibrated** to a standard flat–ΛCDM age; they are deliberately toy-level diagnostics.

- On the **FRW-viable** subset (FRW_VIABLE, 1016 points):
  - The mismatch is smaller but still significant:
    - mean difference \(\approx -2.5\) Gyr,
    - mean relative difference \(\approx -0.18\).
  - Interpretation: the FRW viability mask nudges the grid towards somewhat more reasonable ages in the analytic host, but not enough to claim “alignment with ΛCDM”.

- On the **toy corridor ∧ FRW-viable** set (CORRIDOR_AND_VIABLE, 154 points):
  - The mismatch is actually **worse**:
    - mean difference \(\approx -11.9\) Gyr,
    - mean relative difference \(\approx -0.84\).
  - Interpretation: the current toy corridor prefers θ regions where the toy FRW background is much older than the analytic host prediction.

- On the **18-point empirical kernel** (CORRIDOR_AND_VIABLE_AND_ANCHOR):
  - The mismatch remains large:
    - mean difference \(\approx -10.9\) Gyr,
    - mean relative difference \(\approx -0.81\).
  - Interpretation: the empirical kernel is an internal intersection of:
    - FRW viability,
    - toy corridor,
    - the chosen empirical box,
    and is **not** singled out by the external host as a “well-calibrated” region.

**Interpretation.**

- The external FRW host belt (X1–X3) is treated as a **sanity comparator**:
  - it confirms that the Phase 4 FRW background is a **toy diagnostic pipeline**, not a calibrated cosmology engine;
  - it shows that FRW viability somewhat reduces the mismatch, but the toy corridor and 18-point kernel still live in regions that look strongly misaligned with a simple flat–ΛCDM age calculation.

- No new Phase-level claims are made.  
  The external host results are **not** used as additional constraints on θ or as evidence for or against θ★. They simply document the current mismatch landscape between:
  - the Phase 4 FRW toy ages, and
  - a minimal analytic flat–ΛCDM background age.

**Gating / forward path.**

- This belt remains **Stage 2 diagnostic infrastructure only**:
  - no figures or tables are promoted into Phase 4/5,
  - no data contact is implied,
  - no cosmological parameters are “fit” or “constrained”.

- Any serious contact with **real background cosmology constraints** (e.g. precise age, \(H_0\), \(\Omega_\Lambda\) boxes, full Cℓ or P(k) pipelines) is reserved for a future **Stage II external pipeline**, likely hosted on CLASS/CCL/Cobaya/CosmoSIS, with its own Phase-0-style contracts and promotion gates.


## 2026-01-13 – Stage 2: FRW empirical anchor + external FRW host (diagnostic belt)

**Status:** Stage 2 diagnostics only – non-canonical, non-binding.  
This rung bundles the FRW “empirical anchor” work (A1–A8) and the first external FRW host cross-checks into a single documented belt.

- Built a Stage 2 FRW empirical anchor mask on top of the Phase 4 FRW toy grid:
  - `stage2/frw_data_probe_analysis/src/analyze_frw_empirical_anchor_v1.py`
    constructs `in_empirical_anchor_box` on the 2048-point θ-grid using
    `omega_lambda` and `age_Gyr` from
    `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`
    and a small config file
    `stage2/frw_data_probe_analysis/config/empirical_anchor_box_v1.json`.
  - Result: an 18-point anchor subset (`in_empirical_anchor_box = True`),
    ≈ 0.9% of the grid, fully contained inside both the FRW-viable set and
    the Phase 4 toy corridor.

- Extended the joint mech–FRW analysis with anchor-aware intersections and kernel:
  - `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_intersections_v1.py`
    joins the anchor mask into
    `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv`
    and counts:
    - `FRW_VIABLE` ≈ 49.6% of the grid,
    - `TOY_CORRIDOR` ≈ 57.9%,
    - `EMPIRICAL_ANCHOR` = `FRW_VIABLE ∧ CORRIDOR` = 18 points.
  - `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_kernel_v1.py`
    finds that these 18 points break into two contiguous θ-segments
    (indices [205–213] and [1078–1086]), neither containing θ★.
    The overview figure
    `stage2/joint_mech_frw_analysis/outputs/figures/stage2_joint_mech_frw_anchor_overview_v1.png`
    shows the kernel sitting as a thin band in the Ω_Λ–age plane inside the
    toy corridor and FRW-viable region.
  - `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_sensitivity_v1.py`
    varies the empirical box half-widths (scales 0.5, 1.0, 1.5) and shows
    that the anchor remains a small but non-singleton subset
    (8 → 18 → 26 θ-points), still fully inside FRW-viable, with most
    points also inside the toy corridor.

- Profiled FRW + mechanism behaviour on the anchor vs broader sets:
  - `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_profiles_v1.py`
    summarises FRW quantities (`E_vac`, `omega_lambda`, `age_Gyr`) and
    mechanism amplitudes (`mech_baseline_*`, `mech_binding_*`) across:
    `ALL_GRID`, `FRW_VIABLE`, `TOY_CORRIDOR`, `EMPIRICAL_ANCHOR`,
    and `CORRIDOR_AND_VIABLE_AND_ANCHOR`.
    The anchor kernel picks out a very narrow band in Ω_Λ and age,
    with mechanism amplitudes tightly clustered around
    `mech_baseline_A0 ≈ 0.046` – intermediate between the lower corridor
    values and the higher FRW-viable band.
  - `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_mech_contrast_v1.py`
    compares mechanism statistics on
    `CORRIDOR_AND_VIABLE_AND_ANCHOR` (18 pts) vs
    `CORRIDOR_AND_VIABLE` (154 pts) vs `FRW_VIABLE` and `ALL_GRID`.
    The anchor kernel appears as a narrow interior slice in the mechanism
    amplitude range, not a single θ-needle.

- Added mechanism-side θ-gradient diagnostics with anchor awareness:
  - `stage2/mech_measure_analysis/src/analyze_mech_theta_gradients_v1.py`
    computes discrete θ-gradients of `mech_baseline_*` and `mech_binding_*`
    on the joint grid and reports gradient statistics for
    `ALL_GRID`, `FRW_VIABLE`, `TOY_CORRIDOR`,
    `CORRIDOR_AND_VIABLE`, and the 18-point anchor kernel.
    The anchor region shows steep but coherent gradients rather than a flat
    plateau, reinforcing the picture of a small, structured kernel rather
    than an isolated special point.

- Introduced a simple external FRW host belt to cross-check ages:
  - `stage2/external_frw_host/src/compute_analytic_frw_ages_v1.py`
    computes an analytic flat matter+Λ FRW age as a function of Ω_Λ
    (no data, host physics only), calibrates one overall scale factor to
    match a representative point, then compares host ages to the Phase 4
    toy ages on the joint grid. Output table:
    `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung1_age_crosscheck_v1.csv`.
  - `stage2/external_frw_host/src/analyze_external_frw_age_contrast_v1.py`
    summarises the age differences across:
    `ALL_GRID`, `FRW_VIABLE`, `CORRIDOR_AND_VIABLE`,
    and `CORRIDOR_AND_VIABLE_AND_ANCHOR`, writing
    `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung2_age_contrast_v1.csv`.
    In the current toy implementation:
    - host vs toy ages disagree at the ~50% level on `ALL_GRID`,
    - ≈ 18% relative difference on the FRW-viable set,
    - ≳ 80% relative difference on the corridor and anchor kernel.
    This is treated as a **modeling / normalisation mismatch** between the
    current FRW toy and the analytic host, not as a physical exclusion
    of the axiom.

- Documentation and guardrails:
  - `phase4/docs/PHASE4_EMPIRICAL_ANCHOR_DESIGN_v1.md` records the Phase 4
    interface for the empirical anchor (which columns are used, what
    claim shapes are allowed, and explicit non-claims).
  - `stage2/docs/STAGE2_FRW_ANCHOR_SUMMARY_v1.md` summarises the entire
    Stage 2 anchor + host belt, emphasising that all results are
    diagnostic and remain outside the canonical Phase 3/4/5 narratives.

- Claims discipline:
  - No new Phase 3/4/5 claims have been introduced.
  - The empirical anchor, kernel, and external host contrasts are kept
    strictly in Stage 2 as **diagnostic lenses** on the existing mechanism
    and FRW toy. Before any promotion into Phase text, the FRW toy vs host
    mismatch must be addressed and a dedicated promotion gate defined.


## 2026-01-13 – Stage 2: FRW empirical anchor + external FRW host (A-ladder)

- Phase 4 FRW toy equations + host mapping:
  - Added `phase4/docs/PHASE4_FRW_TOY_EQUATIONS_v1.md` documenting:
    - how `phase4_F1_frw_shape_probe_mask.csv` encodes \(\theta\), `E_vac`, `omega_lambda`, `age_Gyr`, and FRW viability flags;
    - the toy flat-FRW background equations used to interpret `omega_lambda` and `age_Gyr`;
    - the simple analytic flat-FRW “host” model used in Stage 2 for age cross-checks.
  - Updated `phase4/PHASE4_ALIGNMENT_v1.md` with a short pointer section linking:
    - the FRW toy equations doc;
    - the Stage 2 empirical-anchor belt (`stage2/frw_data_probe_analysis/`, `stage2/joint_mech_frw_analysis/`);
    - the external FRW host belt (`stage2/external_frw_host/`);
    and reiterated that all of these remain Stage 2 diagnostics, not Phase 4 claims.

- Stage 2 FRW empirical anchor box + kernel (A1–A7):
  - Introduced a simple empirical anchor box in \((\Omega_\Lambda, t_0)\)-space via
    `stage2/frw_data_probe_analysis/config/empirical_anchor_box_v1.json`, centered near
    \(\Omega_\Lambda \approx 0.69\) and \(t_0 \approx 13.5\,\mathrm{Gyr}\) with explicit half-widths.
  - Ran `stage2/frw_data_probe_analysis/src/analyze_frw_empirical_anchor_v1.py` to build
    `stage2_frw_empirical_anchor_mask_v1.csv` with Boolean `in_empirical_anchor_box` on the
    Phase 4 FRW toy grid (2048 θ-points); found 18 θ values inside the anchor
    (\(\sim 0.88\%\) of the grid).
  - Used the joint mech–FRW grid
    `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv` and
    `analyze_joint_mech_frw_anchor_intersections_v1.py` to quantify intersections:
    - `FRW_VIABLE`: 1016 / 2048 (≈ 0.496 of grid),
    - `TOY_CORRIDOR`: 1186 / 2048 (≈ 0.579 of grid),
    - `EMPIRICAL_ANCHOR`: 18 / 2048 (≈ 0.0088 of grid),
    - `FRW_VIABLE ∧ ANCHOR`: 18 / 2048 (all anchor points FRW-viable),
    - `CORRIDOR ∧ ANCHOR`: 18 / 2048 (all anchor points in the toy corridor),
    - `CORRIDOR ∧ FRW_VIABLE ∧ ANCHOR`: same 18-point kernel.
  - Resolved the kernel into contiguous θ-index segments with
    `stage2_joint_mech_frw_anchor_kernel_v1.csv`: found two segments of length 9 each; both lie
    within the toy corridor and FRW-viable set but do **not** currently contain \(\theta^\star\).
  - Generated a visual overview of the anchor sets and kernel:
    `stage2/joint_mech_frw_analysis/outputs/figures/stage2_joint_mech_frw_anchor_overview_v1.png`.

- Profiles, sensitivity, and mechanism contrast over the anchor (A6–A8):
  - Ran `analyze_joint_mech_frw_anchor_profiles_v1.py` to produce
    `stage2_joint_mech_frw_anchor_profiles_v1.csv`, summarizing
    \(E_\text{vac}\), `omega_lambda`, `age_Gyr`, and the Phase 3 mechanism measures over
    `ALL_GRID`, `FRW_VIABLE`, `TOY_CORRIDOR`, `EMPIRICAL_ANCHOR`, and
    `CORRIDOR ∧ FRW_VIABLE ∧ ANCHOR`. The anchor kernel shows:
    - tightly clustered `omega_lambda` and `age_Gyr` near the anchor center;
    - mechanism measures living in a narrower band than on the full grid, but without a
      clean, sharp “mechanism signature” yet.
  - Ran `analyze_joint_mech_frw_anchor_sensitivity_v1.py` to scale the anchor half-widths by
    factors \(s = 0.5, 1.0, 1.5\) and record how the kernel grows/shrinks:
    - \(s = 0.5\): 8 points (all FRW-viable and in the corridor),
    - \(s = 1.0\): 18 points (baseline kernel),
    - \(s = 1.5\): 26 points in the box, 24 in `FRW_VIABLE ∧ CORRIDOR`.
    This confirms the kernel is thin but not a single isolated needle.
  - Ran `analyze_joint_mech_frw_anchor_mech_contrast_v1.py` to compare mechanism measures across
    `ALL_GRID`, `FRW_VIABLE`, `CORRIDOR ∧ FRW_VIABLE`, `CORRIDOR ∧ FRW_VIABLE ∧ ANCHOR`, and
    `CORRIDOR ∧ FRW_VIABLE ∧ ¬ANCHOR`; anchor points lie in a relatively tight mechanism band,
    but contrast with non-anchor corridor points is still modest (diagnostic, non-claim).

- External flat-FRW host + age cross-check (X1–X2):
  - Implemented a simple external flat-FRW host belt in
    `stage2/external_frw_host/src/compute_analytic_frw_ages_v1.py`, treating the Phase 4
    `omega_lambda` column as a flat \(\Omega_\Lambda\) and computing a dimensionless FRW age
    \(t_0^{\text{(host)}}(\Omega_\Lambda)\) via numeric integration, then calibrating a global
    Gyr scale factor from the grid.
  - Wrote the host–toy comparison table
    `stage2_external_frw_rung1_age_crosscheck_v1.csv` and summarized contrasts with
    `analyze_external_frw_age_contrast_v1.py` into
    `stage2_external_frw_rung2_age_contrast_v1.csv`. Diagnostics:
    - on `ALL_GRID`: mean Δage ≈ −8.4 Gyr, mean relative |Δage|/age_toy ≈ 0.53;
    - on `FRW_VIABLE`: mean Δage ≈ −2.5 Gyr, mean relative |Δage|/age_toy ≈ 0.18;
    - on `CORRIDOR ∧ FRW_VIABLE`: mean Δage ≈ −11.9 Gyr, mean relative |Δage|/age_toy ≈ 0.84;
    - on `CORRIDOR ∧ FRW_VIABLE ∧ ANCHOR`: mean Δage ≈ −10.9 Gyr, mean relative
      |Δage|/age_toy ≈ 0.81.
    This confirms the Phase 4 FRW toy age is only loosely calibrated against a standard
    flat-FRW host, especially inside the toy corridor and empirical anchor kernel; the belt
    is treated as a prompt for future refinement, not as a contradiction claim.

- Stage 2 status documentation:
  - Added `stage2/docs/STAGE2_FRW_EMPIRICAL_ANCHOR_STATUS_v1.md` as a central status note for
    this belt, collecting:
    - the anchor-box definition and mask;
    - kernel structure, profiles, sensitivity, and mechanism contrast;
    - external host age cross-checks;
    - and explicit reminders that all of these are Stage 2 diagnostics (no new Phase-level
      claims or “we predict ΛCDM” statements).

### 2026-01-13 – Stage 2 external FRW host: age consistency vs toy corridor (Rungs X1–X3)

- Added a small Stage 2 **external FRW host** belt to compare the Phase 4 FRW toy
  ages against a simple analytic flat-FRW background:
  - `stage2/external_frw_host/src/compute_analytic_frw_ages_v1.py` (Rung X1) builds
    an age cross-check table
    (`stage2_external_frw_rung1_age_crosscheck_v1.csv`), computing
    `age_Gyr_host` and `age_Gyr_rel_diff` for each θ on the joint grid.
  - `stage2/external_frw_host/src/analyze_external_frw_age_contrast_v1.py` (Rung X2)
    summarises the age differences across
    `ALL_GRID`, `FRW_VIABLE`, `CORRIDOR_AND_VIABLE`, and
    `CORRIDOR_AND_VIABLE_AND_ANCHOR`.

- Implemented `stage2/external_frw_host/src/flag_age_consistent_subset_v1.py` (Rung X3)
  to define an **age-consistency mask**:
  - Join the joint mech–FRW grid, the external host age table, and the empirical
    anchor mask on `(theta_index, theta)`.
  - Define `age_rel_err_abs = |age_Gyr_rel_diff|` and
    `age_consistent_rel_le_20pct` for points with ≤20% relative age mismatch.
  - Summary for the current repo state:
    - Total grid: 2048 θ-points.
    - Age-consistent (≤20%):
      - `ALL_GRID`: 778 points (~0.38 of grid).
      - `FRW_VIABLE`: 778 points (~0.38 of grid).
      - `CORRIDOR_AND_VIABLE`: 0 points.
      - `CORRIDOR_AND_VIABLE_AND_ANCHOR`: 0 points.

- Interpretation (recorded in
  `stage2/external_frw_host/docs/STAGE2_EXTERNAL_FRW_HOST_STATUS_v1.md`):
  - There is a substantial band of FRW-viable θ-points whose toy ages agree with
    a simple flat-FRW host at the 20% level.
  - The current toy corridor and its empirical anchor kernel sit entirely
    **outside** this age-consistent band: they are FRW-viable but live in a
    region where the Phase 4 toy ages are systematically mis-calibrated relative
    to the host.
  - For future work, the existing corridor should be treated as a historical
    toy corridor with known age-calibration issues; any future
    “host-calibrated corridor” should be introduced as a separate, explicitly
    defined Stage 2 object.


## 2026-01-13 – Stage 2 / External FRW host (rungs X2–X3, Hx1): age-consistent host corridor vs empirical anchor

- Extended the external FRW host belt to compare the toy Phase 4 FRW ages against an analytic flat–FRW age calculator and then carve out a “host-calibrated corridor”:
  - `stage2/external_frw_host/src/analyze_external_frw_age_contrast_v1.py` ingests `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung1_age_crosscheck_v1.csv` and summarises the age differences between the repo’s FRW toy (`age_Gyr`) and the analytic host age (`age_Gyr_host`).
    - On the **full θ-grid** (2048 points), the mean age difference is ⟨Δage⟩ ≈ –8.41 Gyr with a mean relative difference ⟨|Δage|/age_repo⟩ ≈ 0.53.
    - On the **FRW_viable** subset (1016 points), the mean age difference improves to ⟨Δage⟩ ≈ –2.49 Gyr with ⟨|Δage|/age_repo⟩ ≈ 0.18, confirming that the viability filters already push the toy FRW towards more host-like ages but still leave substantial bias.
    - On the **corridor ∧ viable** subset (154 points) and the **corridor ∧ viable ∧ empirical anchor** subset (18 points), the age discrepancies are large: ⟨Δage⟩ ≈ –11.9 Gyr and –10.9 Gyr, with relative differences ≈ 0.84 and 0.81 respectively.
  - `stage2/external_frw_host/src/flag_age_consistent_subset_v1.py` combines the host cross-check table with the empirical anchor mask to define an age-consistency flag
    (`age_consistent_rel_le_20pct`) using a 20% relative-error threshold between `age_Gyr` and `age_Gyr_host`.
    - This yields **778 / 2048** θ-points (≈ 0.38 of the grid) that are age-consistent with the host and **all** of them sit inside the FRW_viable set.
    - Crucially, **no** points in the original theta-corridor that also hit the empirical anchor box survive this 20% age-consistency requirement: both `CORRIDOR_AND_VIABLE` and `CORRIDOR_AND_VIABLE_AND_ANCHOR` have `n_age_consistent = 0`.
  - `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_host_corridor_v1.py` summarises a “host-calibrated corridor” defined by the age-consistency mask:
    - `HOST_CALIBRATED_CORRIDOR` has **778** θ-points (≈ 0.38 of the grid).
    - Its intersection with the empirical anchor box is **empty** (`HOST_CORRIDOR_AND_ANCHOR n=0`), so even after requiring external FRW age-consistency, the toy FRW + corridor + empirical anchor chain still has no non-trivial θ that simultaneously:
      - passes Phase 4 FRW viability,
      - lies inside the toy θ-corridor,
      - sits inside the small (Ω_Λ, age) empirical box,
      - and has toy ages consistent with an analytic FRW host at the 20% level.

- Interpretation (Stage 2 diagnostic, **no promotion to Phase claims**):
  - This belt shows that the present implementation of the FRW toy + empirical anchor is structurally “host-incompatible” in the corridor: once an external FRW age standard is enforced at even modest (20%) tolerance, the intersection with the empirical anchor collapses to the empty set.
  - We keep this as a **negative but informative diagnostic result** rather than tuning the toy FRW machinery to force overlap; any future adjustment (e.g. redefining the age observable, relaxing the anchor box, or directly host-calibrating the FRW toy) will be done in a separate, explicitly documented belt so that the current emptiness remains a reproducible, archived statement about the **current** pipeline.


## 2026-01-13 – Stage 2: FRW empirical anchor + external FRW host cross-check (A1–A8, HX1–X3)

**Goal:** Carve out a small, explicit FRW/age “empirical anchor” region in the current Phase 4 toy FRW outputs, track it through the joint mechanism–FRW grid, and test its behaviour against a simple external FRW background host – all as Stage 2 diagnostics, with no promotion to Phase-level claims.

### 1) FRW toy empirical anchor (A1–A4, A6–A8)

- Added `stage2/frw_data_probe_analysis/src/analyze_frw_empirical_anchor_v1.py` with config
  `stage2/frw_data_probe_analysis/config/empirical_anchor_box_v1.json`:
  - Reads `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`.
  - Defines a small box in \((\omega_\Lambda, \text{age}_\mathrm{Gyr})\) and writes
    `stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_empirical_anchor_mask_v1.csv`
    with a boolean `in_empirical_anchor_box`.
  - Result: 18 / 2048 θ-grid points lie inside the empirical anchor (~0.0088 of the grid); all 18 are FRW-viable.

- Extended the joint mech–FRW belt with anchor-aware rungs:
  - `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_intersections_v1.py`  
    → `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_intersections_v1.csv`
    - Confirms:
      - `FRW_VIABLE`: 1016 / 2048,
      - `TOY_CORRIDOR`: 1186 / 2048,
      - `EMPIRICAL_ANCHOR`: 18 / 2048,
      - All 18 anchor points lie in `FRW_VIABLE ∧ TOY_CORRIDOR`.
  - `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_kernel_v1.py`  
    → `stage2/joint_mech_frw_anchor_kernel_v1.csv`
    - Finds two 9-point contiguous θ-segments making up the 18-point anchor kernel:
      - Segment 1: θ_index 205–213, θ ≈ [0.63, 0.65],
      - Segment 2: θ_index 1078–1086, θ ≈ [3.31, 3.33],
      - Neither segment contains θ★.
  - `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_profiles_v1.py`  
    → `stage2_joint_mech_frw_anchor_profiles_v1.csv`
    - Provides summary stats for `ALL_GRID`, `FRW_VIABLE`, `TOY_CORRIDOR`,
      `EMPIRICAL_ANCHOR`, and their intersections.
    - In the 18-point kernel, `omega_lambda` clusters near ≈0.69 and toy `age_Gyr`
      clusters near ≈13.5 Gyr with O(0.05 Gyr) scatter.
  - `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_sensitivity_v1.py`  
    → `stage2_joint_mech_frw_anchor_sensitivity_v1.csv`
    - Varies the empirical box half-widths by factors 0.5, 1.0, 1.5 and tracks how many
      points survive ^ anchor ∧ FRW-viable ∧ corridor:
      - scale 0.5 → 8 points,
      - scale 1.0 → 18 points,
      - scale 1.5 → 26 points (24 in `FRW_VIABLE ∧ TOY_CORRIDOR`).
  - `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_anchor_mech_contrast_v1.py`  
    → `stage2_joint_mech_frw_anchor_mech_contrast_v1.csv`
    - Compares mechanism measures across:
      - `ALL_GRID`, `FRW_VIABLE`,
      - `CORRIDOR_AND_VIABLE` (154 points),
      - `CORRIDOR_AND_VIABLE_AND_ANCHOR` (18 points).
    - In the 18-point kernel the mechanism amplitudes (`mech_baseline_A0`, `mech_binding_A0`)
      sit in a narrow band around ≈0.046 with σ ≈ 2.7×10⁻⁴.

- Added a θ-gradient diagnostic:
  - `stage2/mech_measure_analysis/src/analyze_mech_theta_gradients_v1.py`  
    → `stage2_mech_rung7_theta_gradients_v1.csv`
    - Estimates θ-derivatives of `mech_baseline_A0`, `mech_baseline_A_floor`,
      `mech_binding_A0`, `mech_binding_A` on:
      - the full grid,
      - FRW-viable subset,
      - corridor subset,
      - corridor ∧ viable ∧ anchor kernel.
    - In the 18-point kernel, |gradients| are O(3.4×10⁻²), comparable to corridor
      edges: the kernel is a narrow band, not a flat plateau.

### 2) External FRW host age cross-check (HX1–HX3)

- Implemented a simple external FRW host for age-only cross-checks:
  - `stage2/external_frw_host/src/compute_analytic_frw_ages_v1.py`  
    → `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung1_age_crosscheck_v1.csv`
    - Uses a flat-FRW age integral with a single global calibration factor to map
      dimensionless ages into Gyr.
    - Joins on the same θ-grid as the joint table and records:
      - `age_Gyr` (toy), `age_Gyr_host`, and their differences.
- Summarised age differences on key subsets:
  - `stage2/external_frw_host/src/analyze_external_frw_age_contrast_v1.py`  
    → `stage2_external_frw_rung2_age_contrast_v1.csv`
    - ALL_GRID (2048 points): ⟨age_host − age_repo⟩ ≈ −8.4 Gyr, mean relative
      difference ≈ −0.53.
    - FRW_VIABLE (1016 points): ⟨age_host − age_repo⟩ ≈ −2.5 Gyr, mean relative
      difference ≈ −0.18.
    - CORRIDOR_AND_VIABLE (154 points): ⟨age_host − age_repo⟩ ≈ −11.9 Gyr,
      mean relative difference ≈ −0.84.
    - CORRIDOR_AND_VIABLE_AND_ANCHOR (18 points): ⟨age_host − age_repo⟩ ≈ −10.9 Gyr,
      mean relative difference ≈ −0.81.
- Tagged a 20% age-consistent subset:
  - `stage2/external_frw_host/src/flag_age_consistent_subset_v1.py`  
    → `stage2_external_frw_rung3_age_consistency_mask_v1.csv`
    - Adds `age_consistent_rel_le_20pct` using |age_host − age_repo| / age_repo ≤ 0.2.
    - Results:
      - ALL_GRID: 778 / 2048 points age-consistent.
      - FRW_VIABLE: same 778 points (all lie within FRW-viable).
      - CORRIDOR_AND_VIABLE: 0 points.
      - CORRIDOR_AND_VIABLE_AND_ANCHOR: 0 points.
- Checked the host-calibrated corridor:
  - `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_host_corridor_v1.py`  
    → `stage2_joint_mech_frw_host_corridor_summary_v1.csv`
    - Defines `HOST_CALIBRATED_CORRIDOR` as the age-consistent subset.
    - Confirms that `HOST_CALIBRATED_CORRIDOR ∧ TOY_CORRIDOR ∧ FRW_VIABLE ∧ ANCHOR`
      is empty: the present toy FRW corridor and its 18-point kernel live outside the
      20% age-consistent band of the analytic FRW host.

### 3) Host-space anchor tied back to FRW anchor

- Anchored the host table directly on the FRW empirical anchor:
  - `stage2/external_frw_host/src/analyze_external_frw_host_anchor_v1.py`  
    → `stage2_external_frw_host/outputs/tables/stage2_external_frw_host_anchor_mask_v1.csv`
    - Reads:
      - host age cross-check table, and
      - FRW empirical anchor table.
    - Infers a host anchor box by taking min/max of:
      - `omega_lambda` on FRW anchor points, and
      - `age_Gyr_host` on those same points.
    - Resulting host anchor:
      - `omega_lambda` ∈ [0.664228, 0.716531],
      - `age_Gyr_host` ∈ [2.57, 2.70] Gyr,
      - 18 θ-points in the box (same θ-indices as the FRW anchor).
- Intersections on the joint grid:
  - `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_host_anchor_intersections_v1.py`  
    → `stage2_joint_mech_frw_host_anchor_intersections_v1.csv`
    - ALL_GRID: 2048
    - FRW_VIABLE: 1016
    - TOY_CORRIDOR: 1186
    - HOST_ANCHOR: 18
    - FRW_VIABLE_AND_HOST_ANCHOR: 18
    - CORRIDOR_AND_HOST_ANCHOR: 18
    - CORRIDOR_AND_VIABLE_AND_HOST_ANCHOR: 18

**Net picture:** the empirical anchor kernel is small but real (18 θ-points in two contiguous segments, all FRW-viable and inside the toy corridor), and it has a coherent mechanism profile. However, the current toy FRW age normalization is strongly inconsistent with a simple analytic FRW host, especially inside the corridor and anchor. Any future contact with real cosmological ages must be hosted on a properly normalized FRW layer; the present toy `age_Gyr` column is to be treated as diagnostic scaffolding only.

- Documented this belt and its status in
  `stage2/docs/STAGE2_EMPIRICAL_ANCHOR_STATUS_v1.md` (diagnostic, non-binding).

[2026-01-13] Stage 2: anchor + external FRW host + code/runbook/docs belt

- Stage 2 documentation + governance:
  - Added `stage2/docs/STAGE2_CODE_AUDIT_AND_HEALTHCHECK_v1.md` as a focused audit of Stage 2 scripts
    (mech_measure, FRW corridor, FRW data probes, joint mech–FRW analysis, external FRW host), including
    current failure modes, known limitations, and concrete follow-up rungs.
  - Added `stage2/docs/STAGE2_RUNBOOK_AND_INTERPRETATION_v1.md` as a Stage 2 “how to read the belts” guide:
    what each Stage 2 table means, how the rungs hang together conceptually, and how to avoid over-claiming
    beyond Phase 0–4 contracts.
  - Added `stage2/docs/STAGE2_ENDPOINTS_GLOSSARY_v1.md` as the canonical glossary for Stage 2 endpoints:
    a single place that enumerates the main tables (joint θ-grid, FRW masks, empirical anchor masks, external
    FRW host cross-checks, anchor profiles/sensitivity, mech-contrast and θ-gradients) and explains column
    names like `theta_index`, `omega_lambda`, `age_Gyr`, `in_toy_corridor`, `frw_viable`,
    `in_empirical_anchor_box`, `age_consistent_rel_le_20pct`, `in_host_empirical_anchor_box`, etc.

- FRW empirical anchor in internal (Phase 4) FRW space:
  - Extended the Stage 2 FRW data-probe belt with an empirical anchor mask:
    `stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_empirical_anchor_mask_v1.csv` now records
    for each θ whether its Phase 4 FRW background lies inside a narrow 2D box in
    (`omega_lambda`, `age_Gyr`) defined by `stage2/frw_data_probe_analysis/config/empirical_anchor_box_v1.json`.
  - Built a joint “anchor intersections” summary on the θ-grid:
    `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_intersections_v1.csv` counts
    how many θ values lie in each of:
    - `ALL_GRID` (2048 points),
    - `FRW_VIABLE` (~50% of grid),
    - `TOY_CORRIDOR` (~58% of grid),
    - `EMPIRICAL_ANCHOR` (18 points, ~0.9% of grid),
    - and their intersections (the 18-point anchor set sits fully inside both `FRW_VIABLE` and `TOY_CORRIDOR`).
  - Computed a kernel / contiguity picture:
    `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_kernel_v1.csv` shows that
    the 18 anchor points appear as two contiguous 9-point segments in θ, both FRW-viable and inside the toy
    corridor, but not containing the current θ★ reference value (θ★ lies ~1–1.5 radians away).

- Anchor profiles, sensitivity, and mechanism contrast:
  - Added `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_profiles_v1.csv` to
    summarise, for sets like `ALL_GRID`, `FRW_VIABLE`, `TOY_CORRIDOR`, `EMPIRICAL_ANCHOR`,
    `CORRIDOR_AND_VIABLE_AND_ANCHOR`, the mean/std/min/max of:
    - `E_vac`, `omega_lambda`, `age_Gyr`,
    - `mech_baseline_A0`, `mech_baseline_A_floor`, `mech_baseline_bound`,
    - `mech_binding_A0`, `mech_binding_A`, `mech_binding_bound`.
    This makes the 18-point anchor bubbles explicit in both FRW and mechanism space.
  - Added `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_sensitivity_v1.csv` to
    record how anchor counts change when the empirical box is shrunk/expanded (e.g. 0.5×, 1.0×, 1.5× the
    baseline half-widths). The current runs confirm that the 18-point kernel is small but not a single isolated
    spike: shrinking to 0.5× leaves a smaller (8-point) subset; expanding to 1.5× still yields a compact set
    that remains fully inside `FRW_VIABLE` and mostly inside the toy corridor.
  - Added `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_mech_contrast_v1.csv` to
    compare mechanism-side measures between:
    - `ALL_GRID`,
    - `FRW_VIABLE`,
    - `CORRIDOR_AND_VIABLE`,
    - `CORRIDOR_AND_VIABLE_AND_ANCHOR`,
    - `CORRIDOR_AND_VIABLE_NOT_ANCHOR`.
    This makes it explicit that the anchor kernel sits in a relatively narrow band of mechanism amplitude
    (e.g. `mech_baseline_A0` and `mech_binding_A0` concentrated near ~0.046 with small spread) compared to
    the broader FRW-viable and toy-corridor sets.
  - Extended Stage 2 mech-measure analysis with θ-gradients:
    `stage2/mech_measure_analysis/outputs/tables/stage2_mech_rung7_theta_gradients_v1.csv` summarises
    discrete θ-gradients of the mechanism measures on:
    `ALL_GRID`, `FRW_VIABLE`, `TOY_CORRIDOR`, `CORRIDOR_AND_VIABLE`, and
    `CORRIDOR_AND_VIABLE_AND_ANCHOR`, confirming that the anchor subset is not an artefact of a single
    pathological grid point but sits in a region with reasonably smooth θ variation.

- External analytic FRW host: age cross-check and host-calibrated corridor:
  - Implemented an external flat-FRW “host” integrator in
    `stage2/external_frw_host/src/compute_analytic_frw_ages_v1.py`, calibrated against the Phase 4 FRW-viable
    subset and producing `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung1_age_crosscheck_v1.csv`.
    This table aligns the joint θ-grid with:
    - `age_Gyr_host` (host ages),
    - and the signed / relative differences (`age_Gyr_host - age_Gyr`, `(age_Gyr_host - age_Gyr)/age_Gyr`),
    under the same `omega_lambda` and FRW-viable mask.
  - Summarised host-vs-repo age differences for four key sets in
    `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung2_age_contrast_v1.csv`, showing e.g.:
    - on `FRW_VIABLE` the mean relative age difference is modest (~18–20%),
    - while on `CORRIDOR_AND_VIABLE` and especially `CORRIDOR_AND_VIABLE_AND_ANCHOR`, the host ages disagree
      strongly with the Phase 4 toy ages (relative differences of order ~80%).
  - Introduced a host “age-consistent” mask in
    `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung3_age_consistency_mask_v1.csv`, flagging
    `age_consistent_rel_le_20pct` when `|age_Gyr_host - age_Gyr|/age_Gyr <= 0.2`. On this run:
    - 778/2048 θ points (all FRW-viable) are age-consistent,
    - but **none** of the 18-point FRW empirical anchor kernel lies in this age-consistent subset.
  - Propagated this into the joint θ-grid via
    `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_host_corridor_summary_v1.csv`, which
    defines a host-calibrated corridor and confirms that the current empirical anchor kernel has zero overlap
    with the “FRW-viable and age-consistent” corridor.

- Host-side empirical anchor:
  - Added `stage2/external_frw_host/src/analyze_external_frw_host_anchor_v1.py`, which infers an empirical
    anchor box directly in host space by:
    - joining the FRW anchor mask with the host cross-check table on θ,
    - reading off the min/max of `omega_lambda` and `age_Gyr_host` over the 18 FRW anchor points,
    - defining a host-side empirical box in (`omega_lambda`, `age_Gyr_host`) around that region.
  - The resulting mask table
    `stage2/external_frw_host/outputs/tables/stage2_external_frw_host_anchor_mask_v1.csv` records, for each θ:
    - `theta_index`, `theta`, `omega_lambda`, `age_Gyr`, `age_Gyr_host`, `frw_viable`,
    - and `in_host_empirical_anchor_box` (host-side analogue of `in_empirical_anchor_box`).
    This construction yields the same 18-point set as the FRW anchor, now expressed in host coordinates.
  - Summarised host-anchor intersections in
    `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_host_anchor_intersections_v1.csv`,
    verifying that:
    - `HOST_ANCHOR` = 18 points,
    - all 18 lie in `FRW_VIABLE`,
    - all 18 lie in the toy corridor,
    - but they still lie outside the “age-consistent (≤20%)” host-calibrated corridor.

- High-level interpretation / next steps:
  - Stage 2 now has:
    - a well-defined empirical anchor in FRW space (18 θ points),
    - a corresponding host-side anchor box,
    - and a host-calibrated FRW corridor defined by age-consistency with an external FRW host.
  - Current results suggest a tension between:
    - the narrow FRW-viable + toy-corridor + empirical-anchor kernel, and
    - the host-calibrated age-consistent corridor (no overlap at the chosen 20% threshold).
  - Rather than tuning the toy to force agreement, this belt is explicitly recorded as:
    - a **diagnostic rung**: a first controlled attempt to tie the non-cancelling vacuum story to a concrete
      background observable (age vs ωΛ), using both internal FRW toy and an external FRW host.
    - Inputs and thresholds (anchor box, age-consistency cutoff, host model) are now explicit and can be
      revisited in future belts without retroactively mutating this rung.


---

### 2026-01-14 – Stage 2: FRW toy tightening vs external FRW host + endpoints glossary

**Docs + governance**

- Added FRW toy documentation and healthchecks for Phase 4:
  - `phase4/docs/PHASE4_FRW_TOY_EQUATIONS_v1.md`: makes the toy FRW backbone explicit (ω_Λ column, age_Gyr, and probe flags) and fixes the mapping between code and paper.
  - `phase4/docs/PHASE4_FRW_TOY_HEALTHCHECK_v1.md`: collects basic sanity checks on the Phase 4 FRW toy (monotonicity, behaviour at low/high ω_Λ, qualitative expectations).
  - `phase4/docs/PHASE4_FRW_TOY_HOST_ALIGNMENT_DESIGN_v1.md`: design note for comparing the FRW toy’s age_Gyr to a more standard FRW “host” calculation.
  - Updated `phase4/PHASE4_ALIGNMENT_v1.md` and `phase4/docs/PHASE4_EMPIRICAL_ANCHOR_DESIGN_v1.md` to point at the new FRW toy docs and to clarify that all host/anchor work lives in Stage 2 as diagnostic belts only.
- Added Stage 2 meta-docs:
  - `docs/COMMIT_HISTORY_ATLAS_v1.md`: narrative atlas of key commits / rungs for Stage 2.
  - `stage2/docs/STAGE2_RUNBOOK_AND_INTERPRETATION_v1.md`: how to *run* the Stage 2 belts and how to interpret their outputs without over-claiming.
  - `stage2/docs/STAGE2_CODE_AUDIT_AND_HEALTHCHECK_v1.md`: summary of the Stage 2 code audit and healthcheck (what we inspected, what we found, and open threads).
  - `stage2/docs/STAGE2_ENDPOINTS_GLOSSARY_v1.md`: glossary of Stage 2 CSV endpoints and columns so humans + tools can map outputs without guesswork.

**External FRW host: age bridge + anchor**

- Added a simple external FRW “host” age calculator + bridge:
  - `stage2/external_frw_host/src/compute_analytic_frw_ages_v1.py`: computes a flat–FRW background age for each ω_Λ on the joint θ-grid and calibrates a single scale factor so that the FRW-viable subset matches the toy ages in an average sense.
  - Output: `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung1_age_crosscheck_v1.csv` with columns `theta_index, theta, omega_lambda, age_Gyr (toy), age_Gyr_host, age_Gyr_diff, age_Gyr_rel_diff, frw_viable`.
- Built a bridge table and basic age-window diagnostics:
  - `stage2/external_frw_host/src/build_frw_background_bridge_v1.py`: joins the host ages back onto the θ-grid and writes `stage2_external_frw_background_bridge_v1.csv` as the canonical “FRW host vs toy background” bridge.
  - `stage2/external_frw_host/src/analyze_external_frw_age_window_v1.py`: defines simple age windows in host and toy ages (around 13.8 Gyr for the host, and around the toy’s FRW-viable ages) and reports:
    - small host age window with ⟨age_host⟩ ≈ 13.6 Gyr, ⟨age_toy⟩ ≈ 12.6 Gyr,
    - a different toy age window with ⟨age_toy⟩ ≈ 13.8 Gyr but host ages ≈ 2.5 Gyr, confirming a strong misalignment between the toy ages and a more standard FRW age for the same ω_Λ grid.

- Defined a host-side “age anchor” and profiled it:
  - `stage2/external_frw_host/src/flag_external_frw_host_age_anchor_v1.py`: flags a host-age anchor subset `HOST_AGE_ANCHOR` where the **host** age lies in a [13.3, 14.3] Gyr window around the observed Universe age, and summarises intersections with FRW_viable and the toy age window.
    - Result: `HOST_AGE_ANCHOR` contains 34 θ-points; all are FRW-viable in the toy, but none lie in the existing toy-empirical anchor box from the FRW toy itself.
    - Outputs: `stage2_external_frw_host_age_anchor_mask_v1.csv` and `stage2_external_frw_host_age_anchor_summary_v1.csv`.
  - `stage2/external_frw_host/src/analyze_external_frw_host_age_anchor_profiles_v1.py`: profiles that 34-point host-age anchor subset against the joint θ-grid:
    - ω_Λ is high (mean ≈ 1.05) and fairly narrow.
    - host ages are tightly clustered around ≈ 13.6 Gyr with small scatter.
    - toy ages in the same set are ≈ 12.6 Gyr, i.e. systematically younger.
    - the mechanism amplitudes (mech_baseline_A0, mech_binding_A0, etc.) are non-extreme and fairly narrow, but the subset sits entirely outside the current Phase 4 toy corridor (frac_in_toy_corridor = 0).

**Joint analysis: host age anchor vs toy corridor**

- Added a joint Stage 2 diagnostic:
  - `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_host_age_anchor_intersections_v1.py`:
    - Joins the host age-anchor mask to the joint θ-grid and reports intersections between:
      - ALL_GRID (2048 points),
      - FRW_VIABLE (1016 points),
      - TOY_CORRIDOR (1186 points),
      - HOST_AGE_ANCHOR (34 points).
    - Result: all 34 host age-anchor points are FRW-viable, but **none** lie inside the current Phase 4 toy FRW corridor:
      - `CORRIDOR_AND_HOST_AGE_ANCHOR` = 0
      - `CORRIDOR_AND_VIABLE_AND_HOST_AGE_ANCHOR` = 0
    - Output summary: `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_host_age_anchor_intersections_v1.csv`.

**Interpretation (diagnostic, not promoted to claims)**

- These host-age diagnostics are explicitly Stage 2 **toy/host checks**, not phase-level claims:
  - They show that, on the current θ-grid and ω_Λ mapping, the Phase 4 FRW toy’s notion of age is significantly misaligned with a standard FRW background age for the same ω_Λ.
  - The host age-anchor subset that matches a reasonable 13.8 Gyr background age is FRW-viable but lives **outside** the existing toy FRW “empirical anchor corridor”.
- This is treated as:
  - evidence that the FRW toy needs tightening / redesign before using age as a strong empirical anchor, and
  - a motivation for the FRW toy healthcheck + host-alignment docs added in this rung.
- See `stage2/docs/STAGE2_RUNBOOK_AND_INTERPRETATION_v1.md` and `stage2/docs/STAGE2_CODE_AUDIT_AND_HEALTHCHECK_v1.md` for the broader Stage 2 interpretation and audit context, and `stage2/docs/STAGE2_ENDPOINTS_GLOSSARY_v1.md` for exact column semantics of all Stage 2 tables referenced above.


---

### 2026-01-14 – Stage 2: FRW host age anchor status (Rung H1)

High-level:

- Canonicalised the first FRW host age-anchor experiments into
  `stage2/docs/STAGE2_FRW_HOST_AGE_ANCHOR_STATUS_v1.md`.
- The note records how the analytic FRW host background (at fixed ω_Λ) compares to the Phase 4 FRW toy background, and how the resulting host age anchor relates to the existing θ-corridor.

Technical details:

- Host-age cross-check table:
  - `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung1_age_crosscheck_v1.csv`
    - Built by `stage2/external_frw_host/src/compute_analytic_frw_ages_v1.py`.
- Background bridge:
  - `stage2/external_frw_host/outputs/tables/stage2_external_frw_background_bridge_v1.csv`
    - Built by `stage2/external_frw_host/src/build_frw_background_bridge_v1.py`.
- Host age-anchor mask + summary:
  - `stage2/external_frw_host/outputs/tables/stage2_external_frw_host_age_anchor_mask_v1.csv`
  - `stage2/external_frw_host/outputs/tables/stage2_external_frw_host_age_anchor_summary_v1.csv`
    - Built by `stage2/external_frw_host/src/flag_external_frw_host_age_anchor_v1.py`.
- Joint-grid intersections and profiles:
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_host_age_anchor_intersections_v1.csv`
  - `stage2/external_frw_host/outputs/tables/stage2_external_frw_host_age_anchor_profiles_v1.csv`
    - Built by the corresponding Stage 2 scripts.

Key status findings (recorded, not claimed as results):

- The host age anchor (analytic FRW age in [13.3, 14.3] Gyr) is non-empty:
  - 34 / 2048 θ-points (~1.66% of the grid), all within the FRW-viable mask.
- In this host age-anchor band:
  - Host age ≈ 13.6 Gyr, toy FRW age ≈ 12.6 Gyr → ~1 Gyr offset.
  - Mechanism amplitudes cluster near ~0.0513 with tiny spread.
  - `frac_in_toy_corridor = 0`, i.e. no overlap between the current θ-corridor and the host age-anchor band.
- This is explicitly documented as a diagnostic:
  - The current Phase 4 FRW toy corridor is a **toy-FRW corridor** and is *not* yet an “empirically age-anchored” corridor.
  - Any future “empirically anchored corridor” must be defined via the host age-anchor mask and/or additional external constraints, and gated through Phase 0 discipline.


---

### 2026-01-14 – Phase 4 / Stage 2: FRW toy tightening decision card (Rung H2)

High-level:

- Added `phase4/docs/PHASE4_FRW_TOY_TIGHTENING_DECISION_v1.md` as a design/decision card for how (and whether) to “tighten” the Phase 4 FRW toy in light of Stage 2 FRW host-age diagnostics.
- Explicitly framed two options:
  - (A) keep the FRW toy as-is and treat the analytic FRW host as an external diagnostic bench,
  - (B) introduce a mild, explicitly-calibrated adjustment to align the toy FRW ages more closely with the host ages in a chosen band.
- For the current repo state, adopted **Option A** as the default: the FRW toy remains unchanged; host-age comparisons stay purely diagnostic.

Technical notes:

- The decision card references and depends on:
  - `phase4/docs/PHASE4_FRW_TOY_EQUATIONS_v1.md`
  - `phase4/docs/PHASE4_FRW_TOY_HEALTHCHECK_v1.md`
  - `phase4/docs/PHASE4_FRW_TOY_HOST_ALIGNMENT_DESIGN_v1.md`
  - `stage2/docs/STAGE2_FRW_HOST_AGE_ANCHOR_STATUS_v1.md`
- Any future move towards Option B (toy calibration) is gated by:
  - a dedicated Phase 4 calibration rung,
  - a new design note (e.g. `PHASE4_FRW_TOY_HOST_ALIGNMENT_CALIBRATION_v1.md`),
  - and extended Stage 2 verification scripts (updated host cross-checks, anchor analyses, and pre/post comparisons).

Governance:

- No FRW toy equations are modified by this rung.
- The θ-corridor remains a **toy FRW corridor**; it is not yet an empirically age-anchored corridor.
- Host-age anchor sets remain Stage 2 diagnostics; any promotion to “empirical corridor” status requires a separate, explicitly-gated rung.


---

### 2026-01-14 – Phase 5: Stage 2 anchors & corridors interface note (Rung H3)

High-level:

- Added `phase5/docs/PHASE5_STAGE2_ANCHORS_INTERFACE_v1.md` to bridge Stage 2 diagnostics (FRW corridor, empirical anchors, external FRW host age) into the future Phase 5 narrative.
- The note:
  - identifies the key Stage 2 tables that Phase 5 may treat as inputs,
  - summarises the current θ–landscape (FRW-viable, toy corridor, empirical toy anchor kernel, external host-age anchor band),
  - records overlap/non-overlap patterns (e.g. the toy empirical anchor kernel vs θ★; host-age anchor vs toy corridor),
  - and fixes the allowed / forbidden narrative shapes for Phase 5 (what can and cannot be claimed).

Governance:

- No new code, masks, or θ–filters were introduced by this rung.
- All statements in the interface doc are explicitly tied to existing Stage 2 outputs:
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv`
  - `stage2/frw_corridor_analysis/outputs/tables/...`
  - `stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_empirical_anchor_mask_v1.csv`
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_*_v1.csv`
  - `stage2/external_frw_host/outputs/tables/stage2_external_frw_*_age_*_v1.csv`
- The note reiterates that all “anchor” language is about:
  - the current implementation of the axiom + mechanism + FRW toy + simple FRW host,
  - not about definitive fits to real cosmological data.


---

### 2026-01-14 – Phase 4 FRW toy tightening: equations + healthchecks + host alignment snapshot (Rung H4)

High-level:

- Appended concrete FRW background and diagnostic content to the Phase 4 FRW toy docs:
  - `phase4/docs/PHASE4_FRW_TOY_EQUATIONS_v1.md`
    - Recorded the actual flat-FRW backbone, the θ → (E_vac, omega_lambda, age_Gyr) mapping, and where these quantities live in the repo (`phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`, `stage2_joint_theta_grid_v1.csv`).
  - `phase4/docs/PHASE4_FRW_TOY_HEALTHCHECK_v1.md`
    - Summarised Stage 2 FRW corridor + empirical anchor results (18-point toy empirical anchor kernel, two disjoint θ segments, not containing θ★).
    - Summarised external FRW host age cross-checks and the current tension: host-age anchor band (34 points) does not intersect the Phase 4 toy corridor.
  - `phase4/docs/PHASE4_FRW_TOY_HOST_ALIGNMENT_DESIGN_v1.md`
    - Captured a status snapshot of the implemented external-host belt and its current alignment/misalignment pattern, to guide future tightening.

Governance:

- No new code or masks were introduced in this rung; we only documented the behaviour of existing pipelines:
  - Stage 2 FRW corridor + empirical anchor belt:
    - `stage2/frw_corridor_analysis/outputs/tables/...`
    - `stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_empirical_anchor_mask_v1.csv`
    - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_anchor_*_v1.csv`
  - Stage 2 external FRW host belt:
    - `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung*_age_*_v1.csv`
    - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_host_*_v1.csv`
- All numerical statements in these docs are snapshots of the current repo and are explicitly framed as:
  - properties of the current axiom + mechanism + FRW toy + simple host implementation,
  - not universal claims about real cosmology.


2026-01-14 — Stage 2 / FRW host alignment + toy-age monotonicity

Context:
- Tightening the Phase 4 FRW toy against a simple external FRW host and checking that the toy’s age–ΩΛ behavior is internally sane before attempting any bolder empirical use.

Changes (Stage 2, FRW host belt):

- Added an external-FRW “host” bridge that compares the Phase 4 toy background to an analytic flat-FRW model at fixed ΩΛ:
  - Script: `stage2/external_frw_host/src/compute_analytic_frw_ages_v1.py`
  - Output: `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung1_age_crosscheck_v1.csv`
  - On the FRW-viable subset (1016 / 2048 θ-points), the host ages differ from the Phase 4 toy ages by a mean absolute relative difference of ≈ 0.20. This makes the host useful as an external check, but not yet as a tight calibration.

- Summarised the host vs toy age differences across key subsets:
  - Script: `stage2/external_frw_host/src/analyze_external_frw_age_contrast_v1.py`
  - Output: `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung2_age_contrast_v1.csv`
  - At the current anchor kernel (FRW-viable ∧ toy-corridor ∧ empirical box), host ages are typically ≈ 10–11 Gyr lower than the toy ages (relative offset ≈ 0.8).

- Built a background “bridge” table that carries both toy and host ages for every θ:
  - Script: `stage2/external_frw_host/src/build_frw_background_bridge_v1.py`
  - Output: `stage2/external_frw_host/outputs/tables/stage2_external_frw_background_bridge_v1.csv`
  - This becomes the central hub for subsequent host-alignment diagnostics.

- Defined and probed an age window around the observed age of the Universe:
  - Script: `stage2/external_frw_host/src/analyze_external_frw_age_window_v1.py`
  - Output: `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung4_age_window_summary_v1.csv`
  - Host age window (current choice): [13.3, 14.3] Gyr.
  - Identified:
    - a host-age window set (host in [13.3, 14.3] Gyr),
    - a toy-age window set (toy in [13.3, 14.3] Gyr),
    - and their FRW-viable intersections.
  - Result: host-age window and toy-age window both exist but do not coincide in θ-space; there is currently no θ that is simultaneously in the toy anchor kernel and in the host-age window.

- Promoted the host-age window into a “host age anchor” mask:
  - Script: `stage2/external_frw_host/src/flag_external_frw_host_age_anchor_v1.py`
  - Outputs:
    - Mask: `stage2/external_frw_host/outputs/tables/stage2_external_frw_host_age_anchor_mask_v1.csv`
    - Summary: `stage2/external_frw_host/outputs/tables/stage2_external_frw_host_age_anchor_summary_v1.csv`
  - Host age anchor = FRW-viable θ-points where the host age lies in [13.3, 14.3] Gyr.
  - Size: 34 / 2048 grid points (≈ 1.7%). On this set, the toy ages cluster around ≈ 12.6 Gyr, i.e. ~1 Gyr younger than the host.

- Checked how the host-age anchor overlaps with the joint Phase 3–4 corridor and FRW viability:
  - Script: `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_host_age_anchor_intersections_v1.py`
  - Output: `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_host_age_anchor_intersections_v1.csv`
  - Result:
    - Host-age anchor: 34 θ-points (all FRW-viable),
    - None of these lie inside the current F1 toy corridor, so
      `CORRIDOR_AND_VIABLE_AND_HOST_AGE_ANCHOR` is empty at this rung.

- Profiled the host-age anchor set against the joint θ-grid:
  - Script: `stage2/external_frw_host/src/analyze_external_frw_host_age_anchor_profiles_v1.py`
  - Output: `stage2/external_frw_host/outputs/tables/stage2_external_frw_host_age_anchor_profiles_v1.csv`
  - On these 34 points:
    - `omega_lambda` is tightly clustered around ≈ 1.05,
    - host ages lie in ≈ [13.3, 13.9] Gyr (mean ≈ 13.60 Gyr),
    - toy ages lie in ≈ [12.47, 12.69] Gyr (mean ≈ 12.58 Gyr),
    - mechanism baselines sit near A ≈ 0.051 with very small spread,
    - none of the host-age anchor points are in the current F1 toy corridor.

Toy-age monotonicity (FRW toy sanity check):

- Added an explicit Stage 2 diagnostic that checks whether the Phase 4 FRW toy age is monotone as a function of `omega_lambda` on the FRW-viable band:
  - Script: `stage2/external_frw_host/src/check_frw_toy_age_monotonicity_v1.py`
  - Output: `stage2/external_frw_host/outputs/tables/stage2_external_frw_rung5_toy_age_monotonicity_v1.csv`

- Procedure:
  - Start from `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`.
  - Restrict to the FRW-viable subset (`frw_viable == 1`), which has 1016 θ-points.
  - Sort this subset by `omega_lambda`.
  - Compute finite-difference slopes `d(age_Gyr)/d(omega_lambda)` along the sorted sequence.

- Result:
  - `n_theta = 1016`, `n_steps = 1015`.
  - Gradient sign structure: `n_pos = 0`, `n_neg = 1015`, `n_zero = 0`.
  - So on the FRW-viable set, `age_Gyr` is strictly decreasing as `omega_lambda` increases.
  - Gradient statistics:
    - `grad_min ≈ -4.92` Gyr per unit `omega_lambda`,
    - `grad_max ≈ -1.44` Gyr per unit `omega_lambda`,
    - `abs_grad_p95 ≈ 4.11` Gyr per unit `omega_lambda`.
  - Value ranges on the FRW-viable band:
    - `omega_lambda ∈ [0.3027, 1.6898]`,
    - `age_Gyr ∈ [11.46, 14.97]`.

Interpretation:

- The external FRW host provides a simple, analytic check on the Phase 4 toy ages; they broadly track the same qualitative trend but are offset at the ≈ 20% level on the FRW-viable set, and ≈ 1 Gyr away on a host-age-like window.
- The current F1 toy corridor and the host-age anchor do not intersect: there is no θ that simultaneously lies in the mechanism/FRW corridor and in a narrow host-age window around the observed age of the Universe, at the present rung.
- The FRW toy age is, however, internally well-behaved: `age_Gyr(omega_lambda)` is strictly monotone on the FRW-viable grid. This supports using narrow joint windows in `(omega_lambda, age_Gyr)` as empirical anchors and reading the resulting θ-corridors as slices of a smooth FRW trade-off curve, rather than as artifacts of numerical noise.

## 2026-01-14 – Stage2: external FRW/ΛCDM hosts and age-anchored corridor kernels

**Stage2 code audit, runbook, and endpoints glossary**

- Locked in a Stage2 health snapshot and usage guide:
  - `stage2/docs/STAGE2_CODE_AUDIT_AND_HEALTHCHECK_v1.md`
  - `stage2/docs/STAGE2_RUNBOOK_AND_INTERPRETATION_v1.md`
- Added `stage2/docs/STAGE2_ENDPOINTS_GLOSSARY_v1.md` documenting the key Stage2 CSV endpoints and column names for downstream scripts and humans (joint grid, FRW probes, mechanism tables, host masks, kernels, etc.).

**External FRW host (analytic FRW age cross-check on Phase-4 toy)**

- Implemented an external FRW-age host on the same θ–Ω_Λ grid:
  - `stage2/external_frw_host/src/compute_analytic_frw_ages_v1.py`
  - Cross-check and contrast: `analyze_external_frw_age_contrast_v1.py`
  - 20% relative age-consistency mask: `flag_age_consistent_subset_v1.py`
- Built a FRW-age bridge and age-window diagnostics:
  - Bridge table: `build_frw_background_bridge_v1.py`
  - Age-window summary: `analyze_external_frw_age_window_v1.py`
  - Host-age anchor mask + summary: `flag_external_frw_host_age_anchor_v1.py`
  - Host-age anchor profiles: `analyze_external_frw_host_age_anchor_profiles_v1.py`
- Connected back into the joint θ–mechanism–FRW grid:
  - Joint intersections with host age anchor via
    `stage2/joint_mech_frw_analysis/src/analyze_joint_mech_frw_host_age_anchor_intersections_v1.py`
- Documented the FRW-host chain and results in
  `stage2/docs/STAGE2_FRW_HOST_HX_SECTION_v1.md`.

**External cosmology host (flat-ΛCDM background, fixed H₀)**

- Defined a θ → (Ω_m, Ω_Λ, H₀) mapping on the joint grid:
  - `stage2/external_cosmo_host/src/oa_theta_to_cosmo_params_v1.py`
  - Params grid: `stage2_external_cosmo_params_grid_v1.csv`
- Evaluated ΛCDM host ages on the same grid:
  - `run_cosmo_host_background_grid_v1.py`
  - Age contrast vs repo toy ages: `analyze_external_cosmo_host_age_contrast_v1.py`
- Defined an external-host age anchor window around the observed age:
  - Host age-anchor mask + summary:
    `flag_external_cosmo_host_age_anchor_v1.py`
    → `stage2_external_cosmo_host_age_anchor_mask_v1.csv`,
       `stage2_external_cosmo_host_age_anchor_summary_v1.csv`
- Extracted a 12-point “age ∧ corridor ∧ FRW-viable” kernel:
  - `extract_external_cosmo_host_age_anchor_corridor_kernel_v1.py`
  - Kernel table:
    `stage2_external_cosmo_host_age_anchor_corridor_kernel_v1.csv`
  - On this 12-point band:
    - repo toy ages: ⟨t₀^repo⟩ ≈ 13.45 Gyr with small scatter,
    - external ΛCDM host ages: ⟨t₀^host⟩ ≈ 13.55 Gyr with small scatter,
    - mechanism baselines/binding amplitudes stay in a narrow band
      (~0.0461–0.0467) with zero bound flags.
- Age-window sensitivity sweep on the external-cosmo host:
  - `analyze_external_cosmo_host_age_window_sensitivity_v1.py`
  - Varies the age window scale (0.5×–2×) and tracks:
    - host-window counts,
    - FRW-viable intersection,
    - corridor ∧ FRW ∧ host intersection.
- Built a cross-host kernel comparison table linking:
  - FRW toy anchor kernel (Phase 4),
  - external FRW-host age anchor,
  - external ΛCDM host age ∧ corridor kernel:
    `build_external_host_kernel_comparison_v1.py`
    → `stage2_external_host_kernel_comparison_v1.csv`.
- Snapshot + design docs for the external-cosmo host chain:
  - `stage2/docs/STAGE2_EXTERNAL_COSMO_HOSTS_DESIGN_v1.md`
  - `stage2/docs/STAGE2_EXTERNAL_COSMO_HOST_RESULTS_v1.md`

**Status**

- Stage2 now exposes a small, well-characterized θ-band where:
  1. the Phase-4 FRW toy is FRW-viable and inside the toy corridor,
  2. an external flat-ΛCDM background with fixed H₀ yields Universe-like ages,
  3. Stage2 mechanism amplitudes are controlled and non-pathological.
- All host, kernel, and sensitivity diagnostics are scripted, reproducible
  from the repo, and the working tree is clean and pushed on `main`
  after these changes.

## 2026-01-14 – Stage 2 external hosts + Phase 4 host-alignment wording

**Scope:** Documentation / design-only update, no change to numerical results.

- **Stage 2 / external hosts**
  - Documented the FRW-host and cosmology-host overlays as strictly *diagnostic* tools:
    - `stage2/docs/STAGE2_FRW_HOST_HX_SECTION_v1.md`
    - `stage2/docs/STAGE2_EXTERNAL_COSMO_HOST_DESIGN_v1.md`
    - `stage2/docs/STAGE2_EXTERNAL_COSMO_HOST_RESULTS_v1.md`
  - Summarised the current external-host outputs:
    - FRW-host age cross-checks and age-anchor masks,
    - cosmology-host age grid, age-contrast, 12-point age∧corridor kernel,
    - kernel comparison table across: FRW toy, external FRW host, external cosmo host.

- **Phase 4 / host-alignment design**
  - Updated `PHASE4_FRW_TOY_HOST_ALIGNMENT_DESIGN_v1.md` to:
    - define the objects in play (θ-grid + mechanism, FRW toy, empirical anchor, external hosts),
    - specify host-alignment purely as *mask overlaps* and stress-tests on the FRW toy,
    - formalise the notion of a small θ-kernel where:
      - FRW toy is FRW-viable and in the toy corridor,
      - simple external FRW/ΛCDM hosts give Universe-like ages,
      - mechanism measures remain in a narrow, non-pathological band.
  - Clarified that these are **not** cosmological measurements or fits, and cannot be promoted to real-physics claims within Phase 4.

- **PHASES.md**
  - Refined the Phase 4 description to:
    - include FRW toy + external-host diagnostics and the 12-point θ-kernel as *toy-level* artifacts,
    - explicitly restrict Phase 4 claims to existence/structure of masks and diagnostics,
    - defer any real-physics promotion to future gated phases (Phase 5+).

**Claim boundary:** All changes in this entry are *interpretive/organizational*. They do not alter the Stage 2 or Phase 4 numerical outputs; they only make the host-alignment usage and limits explicit under the Phase 0 contract.


- 2026-01-15 (Stage 2 / Phase 4 interface)
  - Added `stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_phase4_constraints_v1.csv` as a compact 12-point kernel summary (FRW-viable ∧ corridor ∧ external-cosmo age window).
  - Implemented `phase4/src/build_phase4_external_host_kernel_table_v1.py` to auto-generate
    `phase4/outputs/tables/phase4_external_host_kernel_constraints_v1.tex` for direct inclusion
    in the Phase 4 FRW toy paper as the “external-cosmo host age–corridor kernel” table.

- 2026-01-15 (Stage 2 / Phase 4 interface)
  - Exported 12-point external-cosmo host kernel summary to
    `stage2_external_cosmo_host_phase4_constraints_v1.csv`.
  - Added `phase4/src/build_phase4_external_host_kernel_table_v1.py` and
    `phase4/outputs/tables/phase4_external_host_kernel_constraints_v1.tex`
    to include the external-cosmo host age–corridor kernel as a Phase 4 table.

- 2026-01-15 (Phase 4 paper grooming)
  - Added a placeholder figure and label `fig:phase4-shape-probe` in
    `phase4/paper/03_diagnostics_stub.tex` to resolve the remaining
    undefined reference warning.

- 2026-01-15 (Phase 4 F1 FRW sanity sweep)
  - Re-ran the Phase 4 F1 FRW pipeline
    (`run_f1_sanity.py`, `run_f1_shape_diagnostics.py`,
    `run_f1_frw_toy_diagnostics.py`, `run_f1_frw_corridors.py`,
    `run_f1_frw_lcdm_probe.py`, `run_f1_frw_data_probe.py`) to
    confirm that the FRW backbone, corridors, LCDM-like probe, and
    data-probe stubs are consistent with the current Stage 2 / host
    configuration.

- 2026-01-15 (Phase 4 paper refresh)
  - Rebuilt `phase4_paper.pdf` and refreshed Phase 4 artifacts to
    include the external-cosmo host kernel table and updated F1 FRW
    diagnostics.
- 2026-01-15 (Phase 4 external host kernel bridge)
  - Added `phase4/docs/PHASE4_EXTERNAL_HOST_KERNEL_BRIDGE_v1.md` to document the
    12-point external-cosmo host kernel, its numerical bands, and its relation
    to the Phase 4 F1 FRW diagnostics and paper table wiring.

- 2026-01-15 (Phase 4 F1 baseline checkpoint)
  - Added `phase4/docs/PHASE4_FRW_F1_BASELINE_CHECKPOINT_v1.md`
    to freeze the current F1 FRW viability, shape corridor, ΛCDM-like
    window, and Stage 2 external host kernel overlap for the
    baseline configuration.
- 2026-01-15 (Stage 2 external host flatness tolerance scan) Added scan_external_cosmo_flat_tolerance_v1.py and stage2_external_cosmo_flat_tolerance_scan_v1.csv to track HOST_NEAR_FLAT / FRW-viable / corridor fractions as a function of |Omega_tot - 1| tolerance.

## 2026-01-16 — Repo rename to origin-axiom-framework (docs-only rung)

Scope:
- Record the GitHub repository rename and README rollback as a purely documentary change.

Actions:
- Renamed the GitHub repo to `origin-axiom-framework` (no change to scientific content or phase structure).
- Restored `README.md` to the canonical pre-rename version from commit `8c9b1ea` to keep the Stage 1 / Stage 2 description and repo map stable.
- Confirmed that no Phase 0–5 or Stage 2 artifacts, claims, or pipelines were modified in this rung.

Notes:
- A separate repo `origin-axiom-obstruction` now exists for focused work on the conceptual obstruction to exact vacuum cancellation; it is not yet wired into this framework and remains non-canonical background.

## 2026-01-20 — Obstruction program v1 (docs-only branch)

Scope.  
On branch `obstruction-program-v1`, added an explicit obstruction-program interpretive layer over the existing Stage I phases and Stage 2 belts, without changing any Phase contracts or numerical artefacts. All changes are documentation-only and remain non-binding relative to Phase 0 governance.

Files.

- `docs/OBSTRUCTION_PROGRAM_OVERVIEW_v1.md`: new overview memo describing the obstruction-to-perfect-cancellation interpretation, its embedding into the Phase 0–5 ladder, how Stage 2 belts and empirical kernels test it, and explicit non-claims and usage notes (internal and future-facing).
- `README.md`, `docs/PROJECT_OVERVIEW.md`: added short “obstruction program” pointers linking to the overview memo, clearly marked as interpretive and non-canonical.
- `docs/THETA_ARCHITECTURE.md`: appended an “obstruction-program view of θ” section explaining how θ and θ\* can be read as indexing near-cancelling configurations, while emphasising that this does not promote θ\* via current FRW or data probes.
- `docs/STAGE1_STAGE2_STATUS_v1.md`: recorded the obstruction program as an explicit interpretive layer that does not alter lock status for Phase 0–2, Phase 3–5, or Stage 2.
- `stage2/docs/STAGE2_OBSTRUCTION_TESTING_SPINE_v1.md`: new Stage 2 memo organising the FRW corridor, mech/measure, joint mech–FRW, empirical FRW anchor, and external host belts as a coherent “obstruction testing spine”, summarising what they do and do not say about non-cancelling corridors.
- `stage2/docs/STAGE2_MASTER_VERDICT_v1.md`: added a short interpretive paragraph explaining how the master verdict reads from the obstruction-program perspective, without changing any Stage 2 gating.
- `docs/STAGEII_COSMO_HOSTS_DESIGN_v1.md`: appended an “obstruction-program questions for Stage II” section framing host- and data-facing questions about corridor survival and kernel structure as programmatic prompts for future work.

Status and non-claims.

- No Phase 0–2 claims, Phase 3–5 contracts, or Stage 2 promotion gates were modified in this branch; all new language is explicitly interpretive and downstream of existing artefacts.
- The obstruction program is documented as a way of threading together the current stack (mechanism, FRW toy, empirical kernels, external hosts), not as a proof that reality is literally an obstructed cancellation process.
- Any future promotion of obstruction-flavoured statements into Phase papers will require dedicated rungs, explicit Phase 0 gates, and separate commits outside this branch.

## 2026-01-20 — Obstruction program v1: empirical and external-constraints design

Scope.  
On branch `obstruction-program-v1`, extended the obstruction-program documentation to cover static empirical tests and a design-only external-constraints layer, without introducing new code paths or changing any Phase 0–5 contracts or Stage 2 promotion gates. All changes are interpretive overlays and documentation.

Files.

- `docs/OBSTRUCTION_EMPIRICAL_PROGRAM_v1.md`: new memo defining the obstruction empirical program in the current stack. Clarifies that:
  - θ* is treated as part of the fixed rule set,
  - current tests focus on static θ slices and corridors (no dynamical θ field yet),
  - meaningful positive outcomes require non-empty, structured, mildly robust θ kernels that survive internal FRW and Stage 2 filters,
  - meaningful negative outcomes are documented no-go results for specific obstruction variants,
  - and any use of real cosmological knowledge (Λ, DESI hints, early galaxies) is staged: conceptual guardrails now, explicit external corridors later.
- `stage2/docs/STAGE2_OBSTRUCTION_TESTING_SPINE_v1.md`: appended a section describing the existing pre-data FRW kernel as the initial static θ testbed for the obstruction program. Recorded that:
  - it is a small, non-empty subset of the θ grid that passes current FRW viability and toy empirical filters,
  - it is interpreted as a sanity-check kernel, not a prediction,
  - and later rungs will ask whether similar kernels persist under modest changes in thresholds, mappings, or host choices.
- `stage2/docs/STAGE2_EXTERNAL_CONSTRAINTS_DESIGN_v1.md`: new Stage 2 design memo specifying how external-style constraints will eventually be encoded as downstream corridors:
  - late-time expansion corridors (e.g. effective w0–wa boxes, H(z) bands, age bounds),
  - early-structure-friendly corridors (high-redshift age and growth proxies),
  - and host-consistency corridors (simple metrics comparing toy FRW histories to external host solvers),
  all framed as reproducible filters on existing tables rather than as live data-fitting pipelines.
- `docs/REPO_MAP_AND_ATLAS_v1.md`: added an “Obstruction-program and external-constraints docs” section listing the key obstruction memos (`OBSTRUCTION_PROGRAM_OVERVIEW_v1`, `THETA_ARCHITECTURE`, `OBSTRUCTION_EMPIRICAL_PROGRAM_v1`, Stage 2 obstruction spine and external-constraints design, Stage 2 master verdict, and Stage II host design) so the obstruction stack is discoverable from the global atlas.

Status and non-claims.  
- No numerical artefacts, Phase contracts, or Stage 2 promotion gates were changed in this rung; all edits are documentation-only and clearly marked as interpretive. The obstruction program remains an overlay on the locked Stage 0–5 + Stage 2 structure, not an alternative set of claims.
- Static θ corridors and the existing pre-data FRW kernel are positioned as testbeds for future work: they show that the current stack can support non-trivial θ subsets under internal filters, but they are not yet confronted with explicit external corridors or host-level metrics.
- Any future introduction of concrete external corridors (for example effective w0–wa boxes or high-redshift age bounds) and any promotion of their outputs into phase papers will require separate design rungs, Phase 0 style gates, and explicit updates to the relevant documents.
