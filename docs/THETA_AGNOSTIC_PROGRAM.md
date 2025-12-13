# Origin Axiom — θ\*-Agnostic Program

_Last updated: 2025-12-11_

This document states the **neutral, θ\*-agnostic program** of the Origin Axiom project.

We assume only:

1. **Non-cancelling principle**  
   - Absolute “nothing” (no space, no time, no laws, no fields, no possibilities) is not a coherent state.  
   - Reality is modeled as a complex system of modes whose phases **cannot cancel to a strict global zero**.

2. **Global twist parameter θ\***  
   - There exists a **dimensionless twist parameter θ\*** (a phase, holonomy or topological angle) that characterizes how far the system is from exact cancellation.  
   - At this stage, **θ\*** is a free parameter.  
   - Numbers like φ, φ², φ^φ, π, etc. are treated as **test samples**, not built-in truths.

The goal of the project is to see whether such a θ\*-based non-cancelling principle can be turned into a mathematically consistent, physically meaningful framework that connects to known physics.

We explicitly **avoid** assuming from the outset that θ\* = φ or θ\* = φ^φ.


---

## 2. Verification Layer (Phase θ-Agnostic-0)

We currently have three independent, θ-agnostic verification pillars:

1. **1D scalar vacuum (free, dissipative, noisy)**  
   Module: `src/scalar_vacuum_theta/`  
   - `run_1d_vacuum_dispersion.py`  
     - Confirms ω² = k² + m₀² with relative errors ~10⁻³ across modes.  
   - `run_1d_vacuum_dephasing.py`  
     - Confirms ηₖ ≈ γ with relative error ~10⁻³ and R² ≈ 0.95 for the exponential envelope fits.  
   - `run_1d_vacuum_noise_residue.py`  
     - Confirms Var(k) ∝ 1/ωₖ² up to O(10–20%) deviations.  
   These tests validate the numerical implementation of the scalar vacuum, independently of any θ\*.

2. **4D lattice Δα(θ) (vacuum self-energy shift)**  
   Module: `src/lattice_theta/`  
   - `lattice_delta_alpha.py`  
     - Computes a 4D integer-lattice sum S_R(θ) with spherical cutoff |n| ≤ R.  
     - Fits S_R ≈ A(θ) + B(θ)/R for R ≥ R_fit_min, interpreting A(θ) as Δα(θ).  
   - Current test set (R_max = 12, R_fit_min = 6) includes:
     - θ = 1.0  
     - θ = 1.6180339887… (φ)  
     - θ = 2.1784575679… (φ^φ)  
     - θ = 2.0  
     - θ = 3.1415926535… (π)  
   - For each θ, results are saved to:
     - `data/processed/lattice_theta/delta_alpha_theta_R12_theta*.csv/.npz`  
     - `figures/lattice_theta/delta_alpha_theta_R12_theta*.png`  

   **Important:**  
   - These θ values are treated as **sample points** on a continuous Δα(θ) curve.  
   - No special status is assigned to any specific value; they are simply probes.

3. **Cancellation system: discrete non-cancellation testbed**  
   Module: `src/cancellation_system/`  
   - `run_chain_residual_scan.py`  
     - Tests residual sums S(N, θ) for chains of length N with integer “charges” up to max_q.  
     - For each (N, θ), measures mean|S|, rms|S| and mean|S|/√N.  
   - Runs performed so far include:
     - θ sets such as {1.0, 1.5, 1.618…, 2.0, 2.5, π} and {φ, φ^φ, 2.0, π}.  
     - N in {8, 16, 32, 64, 128}, max_q = 5, n_samples = 500.  
   - Results saved to:
     - `docs/results/cancellation_system/chain_residual_scan_latest.csv`  
     - `figures/cancellation_system/chain_residual_scan.png`

   **Key observation:**  
   - All tested θ show mean|S|/√N ≈ O(1).  
   - No strong evidence for a “magic” angle that suppresses residuals emerges in this simple 1D model.  
   - This is **useful**: it prevents us from prematurely over-interpreting φ or φ^φ as special based on this toy system.


A concise summary of these results lives in:  
`verification_notes.md` under **"Phase θ-Agnostic-0: Verification Layer (2025-12-11)"**.


---

## 3. Program Structure (θ-Agnostic Roadmap)

We separate three layers:

1. **Axiom level (philosophical / conceptual)**  
   - Non-cancelling principle (no absolute nothingness, global twist θ\*).  
   - This gives us *motivation* but not yet equations of motion.

2. **Mathematical structure level**  
   - How θ\* can enter:
     - As a phase in a lattice sum → Δα(θ).  
     - As a holonomy / boundary condition in field configurations.  
     - As a parameter in a cancellation functional or partition function.  
   - Here we define sums, limits, PDEs, and stochastic equations **without** assuming the value of θ\*.

3. **Model / phenomenology level**  
   - Concrete simulations (scalar vacuum, 4D lattice, cancellation system).  
   - Later: coupling to geometry, higher dimensions, flavour structure, cosmology, etc.  
   - Only at this level do we connect to data or specific scales.


---

## 4. Near-Term Tasks (Next Phases)

### Phase 1 — Refine Δα(θ) as a function

**Goal:** move from a handful of θ samples to a more resolved θ → Δα(θ) map.

Tasks:
1. Increase R_max (e.g. 16, 20, maybe 24) while monitoring CPU time.  
2. Sample θ on a **uniform grid** (e.g. 0 < θ < 2π, or 0 < θ < 3) instead of named constants.  
3. Fit Δα(θ) with:
   - Smooth interpolants (splines or low-order Fourier expansion),  
   - Error estimates from the (A, σ_A) fits.  
4. Store results in:
   - `data/processed/lattice_theta/delta_alpha_scan_theta_grid.csv`  

This will tell us whether Δα(θ) has any **non-trivial structure** (minima, maxima, inflection points) that could later motivate candidate θ\* values.

---

### Phase 2 — θ-Dependent Scalar Vacuum

**Goal:** introduce θ-dependence into the scalar vacuum sector, but only via a θ-parametrized mass term or coupling that is explicitly derived from Δα(θ) or a similar structural object.

Example directions:
- Define an effective mass:
  - m_eff²(θ) = m_base² + c · Δα(θ),  
  then study how dispersion, dephasing, and noise behave as θ varies.
- Or, introduce θ as a **boundary phase** or twist in mode expansion.

Key constraint:
- The θ-dependence must be **explicitly traceable** to a structural rule (lattice sum, holonomy, boundary condition), not hand-tuned.

---

### Phase 3 — Richer Non-Cancellation Structures

**Goal:** go beyond 1D, uncorrelated chains.

Candidates:
- 2D or 3D cancellation systems with:
  - local constraints (e.g. divergence-free, loop closures),  
  - quasi-crystal-like patterns, or  
  - random graphs with cycle constraints.
- Study how residual “non-cancellation” scales with system size and topology.

Again, θ remains a parameter; the question is whether any **emergent structure** appears for particular θ in richer geometries.

---

## 5. Neutrality and Avoiding φ-Bias

Going forward:

- φ and φ^φ are allowed in the code and notes **only** as:
  - Sample test values in θ scans,
  - Historical references to earlier explorations.

- They should **not** be presented as:
  - Assumed truths,
  - Predetermined “destinations” of the program.

Any future claim like “θ\* ≈ φ^φ” must arise from:

1. A **clearly defined structural mechanism**, and  
2. A **quantitative, falsifiable link** to either:
   - Simulation results (e.g. extremal behaviour of a functional), or  
   - Observed data (cosmology, spectra, mixing, etc.).

Until then, θ\* is deliberately **agnostic**.

