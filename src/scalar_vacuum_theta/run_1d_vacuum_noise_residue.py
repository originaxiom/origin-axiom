#!/usr/bin/env python3
"""
run_1d_vacuum_noise_residue.py

θ*-agnostic scalar vacuum with damping + stochastic forcing.
We measure the steady-state variance of a few Fourier modes and check whether
it is approximately compatible with a simple scaling Var[|θ_k|] ∝ 1 / ω_k^2.

This is *not* claiming a fully rigorous FDT normalization; it is a practical
baseline test: the damped, noisy vacuum reaches a stationary state, and the
mode variances follow a simple, controlled pattern.

Output:
  - CSV: data/processed/scalar_vacuum_theta/noise_residue_results.csv
  - PNG: figures/scalar_vacuum_theta/noise_residue_check.png
"""

import os
import math
import numpy as np
import csv
import matplotlib.pyplot as plt

# -----------------------
# Simulation parameters
# -----------------------

L = 1.0          # system length
N = 2048         # number of grid points
m0 = 5.0         # mass parameter
gamma = 0.1      # damping coefficient
dt = 1.0e-4      # time step
total_time = 200.0   # total physical time
noise_amp = 0.5      # stochastic acceleration amplitude per sqrt(dt)
seed = 12345

# modes to monitor (Fourier indices)
mode_indices = [1, 2, 3, 4, 5]

# sampling / burn-in
sample_stride = 100        # take a sample every this many steps
burn_in_fraction = 0.3     # drop this fraction of earliest samples

# -----------------------
# Derived quantities
# -----------------------

dx = L / N
n_steps = int(total_time / dt)
n_samples = n_steps // sample_stride

print("=== 1D θ*-agnostic scalar vacuum with noise ===")
print(f"L = {L}, N = {N}, dx = {dx:.4e}, dt = {dt:.3e}, total_time ≈ {total_time}")
print(f"m0 = {m0}, gamma = {gamma}, noise_amp = {noise_amp}")
print("----------------------------------------------------")
print(f"n_steps = {n_steps}, n_samples (before burn-in) ≈ {n_samples}")

# spatial grid and fields
x = np.linspace(0.0, L, N, endpoint=False)
theta = np.zeros(N, dtype=np.float64)
theta_dot = np.zeros(N, dtype=np.float64)

rng = np.random.default_rng(seed)

# -----------------------
# Helper functions
# -----------------------

def laplacian_periodic(phi, dx):
    """Simple second-derivative with periodic boundary conditions."""
    return (np.roll(phi, -1) - 2.0 * phi + np.roll(phi, 1)) / (dx * dx)

def step(theta, theta_dot, dt, dx, m0, gamma, noise_amp, rng):
    """
    One leapfrog-like update with damping and stochastic forcing.
    Noise is approximate white noise in acceleration: noise_amp * N(0,1) / sqrt(dt).
    """
    lap = laplacian_periodic(theta, dx)
    # white noise in acceleration; scaling 1/sqrt(dt) approximates δ-correlated noise
    xi = rng.normal(loc=0.0, scale=1.0, size=theta.shape)
    accel = lap - m0**2 * theta - 2.0 * gamma * theta_dot + noise_amp * xi / math.sqrt(dt)

    theta_dot = theta_dot + accel * dt
    theta = theta + theta_dot * dt
    return theta, theta_dot

def measure_mode_amplitudes(theta, mode_indices):
    """
    Compute absolute value of Fourier coefficients for selected modes.
    Using rFFT (periodic domain). Mode index n corresponds to k = 2π n / L.
    """
    theta_k = np.fft.rfft(theta)
    amps = {}
    for n in mode_indices:
        if n < len(theta_k):
            amps[n] = np.abs(theta_k[n])
        else:
            amps[n] = np.nan
    return amps

# -----------------------
# Main time integration
# -----------------------

# store samples for each mode
samples = {n: np.zeros(n_samples, dtype=np.float64) for n in mode_indices}
sample_counter = 0

for step_idx in range(n_steps):
    theta, theta_dot = step(theta, theta_dot, dt, dx, m0, gamma, noise_amp, rng)

    if step_idx % sample_stride == 0:
        amps = measure_mode_amplitudes(theta, mode_indices)
        for n in mode_indices:
            samples[n][sample_counter] = amps[n]
        sample_counter += 1

        if sample_counter % 100 == 0:
            print(f"  sample {sample_counter}/{n_samples} (t ≈ {step_idx*dt:.1f})")

print("Integration complete.")

# adjust sample_counter in case n_steps/sample_stride was not exact
for n in mode_indices:
    samples[n] = samples[n][:sample_counter]
n_samples = sample_counter
print(f"Effective samples = {n_samples}")

# -----------------------
# Compute variances, compare to 1/ω_k^2 scaling
# -----------------------

burn = int(burn_in_fraction * n_samples)
print(f"Burn-in samples: {burn} (out of {n_samples})")

results = []
omega_list = []
var_list = []
scaled_list = []

for n in mode_indices:
    data = samples[n][burn:]
    # variance of amplitude time series
    var_meas = np.var(data)
    # corresponding k and ω_k
    k = 2.0 * math.pi * n / L
    omega_th = math.sqrt(k*k + m0*m0)
    results.append((n, k, omega_th, var_meas))
    omega_list.append(omega_th)
    var_list.append(var_meas)

omega_arr = np.array(omega_list)
var_arr = np.array(var_list)

# Fit simple scaling Var ≈ C / ω^2 → C = mean(Var * ω^2)
C = np.mean(var_arr * omega_arr**2)
var_fit = C / (omega_arr**2)

scaled_constant = var_arr * omega_arr**2   # should cluster around C
scaled_list = scaled_constant.tolist()

print("----------------------------------------------------")
print("Mode variances and scaling check (Var ≈ C / ω^2):")
for (n, k, omega_th, var_meas), vfit, vscaled in zip(results, var_fit, scaled_constant):
    rel_err = (var_meas - vfit) / vfit if vfit != 0 else 0.0
    print(f"  n={n:2d}, k={k:7.3f}, ω={omega_th:7.3f}, Var_meas={var_meas: .3e}, "
          f"Var_fit={vfit: .3e}, (Var*ω^2)={vscaled: .3e}, rel_err={rel_err: .2e}")

# -----------------------
# Save CSV + figure
# -----------------------

out_dir = "data/processed/scalar_vacuum_theta"
fig_dir = "figures/scalar_vacuum_theta"
os.makedirs(out_dir, exist_ok=True)
os.makedirs(fig_dir, exist_ok=True)

csv_path = os.path.join(out_dir, "noise_residue_results.csv")
with open(csv_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["n", "k", "omega", "var_meas", "var_fit", "var_omega2"])
    for (n, k, omega_th, var_meas), vfit, vscaled in zip(results, var_fit, scaled_constant):
        writer.writerow([n, k, omega_th, var_meas, vfit, vscaled])

print(f"Saved results to: {csv_path}")

# Plot: scaled constant vs k (should be ~flat)
plt.figure(figsize=(7,5))
ks = [r[1] for r in results]
plt.axhline(C, linestyle="--", label=f"mean C ≈ {C:.3e}")
plt.plot(ks, scaled_constant, "o-", label=r"$\mathrm{Var}(|\theta_k|)\,\omega_k^2$")
plt.xlabel("k")
plt.ylabel(r"$\mathrm{Var}(|\theta_k|)\,\omega_k^2$")
plt.title("Mode variance scaling in noisy θ*-agnostic vacuum")
plt.legend()
plt.grid(True)

fig_path = os.path.join(fig_dir, "noise_residue_check.png")
plt.tight_layout()
plt.savefig(fig_path, dpi=150)
print(f"Saved figure to: {fig_path}")
print("Done.")
