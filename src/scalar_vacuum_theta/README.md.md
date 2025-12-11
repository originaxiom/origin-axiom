# Scalar vacuum sector (θ*-agnostic)

This module isolates the **1D scalar vacuum** as a clean playground for the
non-cancelling axiom, but with **θ*** kept **agnostic**.

The idea is:

- We study a simple Klein–Gordon–like field in 1D,
- With mass parameter `m0`,
- And verify that our numerics are clean *before* we attach any specific
  φ or φ^φ choice.
- Later, a θ*-dependent mass shift Δm²(θ*) can be plugged into the same
  structure.

---

## 1. `run_1d_vacuum_dispersion.py`

**Goal:** Check that the discrete evolution of a free scalar field reproduces

\[
\omega_k^2 = k^2 + m_0^2
\]

to high precision.

- Excites several Fourier modes in a 1D box (periodic),
- Evolves them in time with a second-order integrator,
- Extracts ω from the time series via FFT,
- Compares with the analytic dispersion.

**Run:**

```bash
python3 src/scalar_vacuum_theta/run_1d_vacuum_dispersion.py
```

Outputs:

- `data/processed/scalar_vacuum_theta/dispersion_results.csv`
- `figures/scalar_vacuum_theta/dispersion_check.png`

---

## 2. `run_1d_vacuum_dephasing.py`

**Goal:** Add a uniform damping `gamma` and verify that the **mode envelope**
decays with the expected dephasing rate.

For a simple damped KG mode with small damping, the envelope decays roughly as

\[
A_k(t) \sim e^{-\eta t}, \quad \eta \approx \gamma
\]

In this θ*-agnostic check we:

- Launch a single mode,
- Integrate with damping γ,
- Fit the log-envelope to extract η_meas,
- Compare to η_th = γ.

**Run:**

```bash
python3 src/scalar_vacuum_theta/run_1d_vacuum_dephasing.py
```

Outputs:

- `data/processed/scalar_vacuum_theta/dephasing_results.csv`
- `figures/scalar_vacuum_theta/dephasing_check.png`

---

## 3. `run_1d_vacuum_noise_residue.py`

**Goal:** Add additive noise and probe the **steady-state fluctuations** and
**spatial coherence** of the field.

We evolve

\[
\ddot\theta - \theta_{xx} + m_0^2 \theta + \gamma \dot\theta = \sigma\,\xi(x,t)
\]

where ξ is Gaussian white noise, and measure:

### (a) Mode variances  
\[
\mathrm{Var}[\theta_k] \sim \frac{C}{\omega_k^2}
\]

### (b) Spatial coherence  
- Compute C(r) = ⟨θ(x) θ(x+r)⟩,  
- Fit C(r)/C(0) ~ exp(−r/ξ),  
- Extract coherence length ξ.

**Run:**

```bash
python3 src/scalar_vacuum_theta/run_1d_vacuum_noise_residue.py
```

Outputs:

- `data/processed/scalar_vacuum_theta/noise_residue_results.csv`
- `data/processed/scalar_vacuum_theta/coherence_results.csv`
- `figures/scalar_vacuum_theta/noise_residue_check.png`
- `figures/scalar_vacuum_theta/coherence_check.png`

---

## 4. `run_1d_vacuum_theta_massshift.py` (θ*-parametric extension)

This script treats the **twist** as a parametric mass shift

\[
m_{\text{eff}}^2 = m_0^2 + \Delta m^2(\theta_\star)
\]

without committing to any particular θ*. It:

- Takes `m0_bare` and `delta_m2` as inputs,
- Computes `m_eff = sqrt(m0_bare^2 + delta_m2)`,
- Re-runs the dispersion test with `m_eff`,
- And outputs tables/plots showing how ω_k changes with the shift.

**Run:**

```bash
python3 src/scalar_vacuum_theta/run_1d_vacuum_theta_massshift.py
```

This is the bridge between:

- The θ*-agnostic vacuum sector, and  
- Any future lattice / holonomy calculation that produces a concrete Δm²(θ*).
