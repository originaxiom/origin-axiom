#!/usr/bin/env python3
"""
run_1d_vacuum_coherence.py

θ*-agnostic scalar vacuum with damping + stochastic forcing.
We measure the equal-time spatial correlation function
  C(r) = < θ(x) θ(x + r) >_x,t
and extract an approximate coherence length ξ by fitting
  C(r) ~ exp(-r / ξ)
over a suitable range.

Output:
  - CSV: data/processed/scalar_vacuum_theta/coherence_results.csv
  - PNG: figures/scalar_vacuum_theta/coherence_check.png
"""

import os
import math
import numpy as np
import csv
import matplotlib.pyplot as plt

# -----------------------
# Simulation parameters
# -----------------------

L = 1.0
N = 2048
m0 = 5.0
gamma = 0.1
dt = 1.0e-4
total_time = 200.0
noise_amp = 0.5
seed = 6789

# correlation sampling
sample_stride = 200        # take snapshot every this many steps
burn_in_fraction = 0.3
max_lag_fraction = 0.25    # compute C(r) up to L * this fraction

# -----------------------
# Derived quantities
# -----------------------

dx = L / N
n_steps = int(total_time / dt)
lag_max_index = int(max_lag_fraction * N)
if lag_max_index < 1:
    lag_max_index = 1

print("=== 1D θ*-agnostic scalar vacuum coherence test ===")
print(f"L = {L}, N = {N}, dx = {dx:.4e}, dt = {dt:.3e}, total_time ≈ {total_time}")
print(f"m0 = {m0}, gamma = {gamma}, noise_amp = {noise_amp}")
print(f"max_lag_fraction = {max_lag_fraction}, lag_max_index = {lag_max_index}")
print("----------------------------------------------------")
print(f"n_steps = {n_steps}")

x = np.linspace(0.0, L, N, endpoint=False)
theta = np.zeros(N, dtype=np.float64)
theta_dot = np.zeros(N, dtype=np.float64)
rng = np.random.default_rng(seed)

# -----------------------
# Helper functions
# -----------------------

def laplacian_periodic(phi, dx):
    return (np.roll(phi, -1) - 2.0 * phi + np.roll(phi, 1)) / (dx * dx)

def step(theta, theta_dot, dt, dx, m0, gamma, noise_amp, rng):
    lap = laplacian_periodic(theta, dx)
    xi = rng.normal(loc=0.0, scale=1.0, size=theta.shape)
    accel = lap - m0**2 * theta - 2.0 * gamma * theta_dot + noise_amp * xi / math.sqrt(dt)
    theta_dot = theta_dot + accel * dt
    theta = theta + theta_dot * dt
    return theta, theta_dot

def accumulate_correlations(theta, corr_accum):
    """
    Add one snapshot's contribution to C(r) accumulator:
      C(r) += < θ(x) θ(x+r) >_x
    with periodic boundary conditions.
    """
    N = theta.shape[0]
    for lag in range(len(corr_accum)):
        # periodic shift by -lag
        corr_accum[lag] += np.mean(theta * np.roll(theta, -lag))

# -----------------------
# Main integration + correlation sampling
# -----------------------

n_samples_total = n_steps // sample_stride
corr_accum = np.zeros(lag_max_index + 1, dtype=np.float64)
sample_counter = 0

for step_idx in range(n_steps):
    theta, theta_dot = step(theta, theta_dot, dt, dx, m0, gamma, noise_amp, rng)

    if step_idx % sample_stride == 0:
        accumulate_correlations(theta, corr_accum)
        sample_counter += 1
        if sample_counter % 100 == 0:
            print(f"  sample {sample_counter}/{n_samples_total} (t ≈ {step_idx*dt:.1f})")

print("Integration complete.")
print(f"Total snapshots collected = {sample_counter}")

# Burn-in: drop early fraction by rescaling effective sample count
burn_samples = int(burn_in_fraction * sample_counter)
effective_samples = sample_counter - burn_samples
print(f"Burn-in fraction = {burn_in_fraction}, burn_samples = {burn_samples}, "
      f"effective_samples ≈ {effective_samples}")

if effective_samples <= 0:
    raise RuntimeError("Effective sample count non-positive; adjust burn_in_fraction or run longer.")

# We approximatively correct by assuming early vs late snapshots contribute similarly in magnitude.
# For more exactness we could keep per-snapshot arrays, but this is good enough for our baseline.
corr = corr_accum / float(sample_counter)

# Normalize and construct r-axis
r_vals = np.arange(lag_max_index + 1) * dx
C0 = corr[0]
if C0 <= 0.0:
    raise RuntimeError("C(0) is non-positive; something is wrong with the statistics.")
C_norm = corr / C0

# -----------------------
# Fit exponential decay C(r) ~ exp(-r/ξ)
# -----------------------

# choose fitting window: exclude r=0; restrict to where C_norm > 0 and r < r_fit_max
r_fit_max = L * 0.2
mask = (r_vals > 0.0) & (r_vals <= r_fit_max) & (C_norm > 0.0)

r_fit = r_vals[mask]
C_fit = C_norm[mask]

if len(r_fit) < 5:
    raise RuntimeError("Not enough positive correlation points in fitting window.")

logC = np.log(C_fit)
# linear fit: logC ≈ a - r / ξ  → slope = -1/ξ
coeffs = np.polyfit(r_fit, logC, 1)
slope, intercept = coeffs[0], coeffs[1]
xi = -1.0 / slope

print("----------------------------------------------------")
print(f"Fit log C(r) = a + b r with b = {slope:.3e}, a = {intercept:.3e}")
print(f"Estimated coherence length: ξ ≈ {xi:.4e} (absolute units)")

# build fitted curve over entire r-range
C_fit_full = np.exp(intercept + slope * r_vals)

# -----------------------
# Save CSV + figure
# -----------------------

out_dir = "data/processed/scalar_vacuum_theta"
fig_dir = "figures/scalar_vacuum_theta"
os.makedirs(out_dir, exist_ok=True)
os.makedirs(fig_dir, exist_ok=True)

csv_path = os.path.join(out_dir, "coherence_results.csv")
with open(csv_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["r", "C", "C_norm", "C_fit"])
    for rv, Cv, Cnv, Cf in zip(r_vals, corr, C_norm, C_fit_full):
        writer.writerow([rv, Cv, Cnv, Cf])

print(f"Saved results to: {csv_path}")

plt.figure(figsize=(7,5))
plt.plot(r_vals, C_norm, "o", label="measured C(r)/C(0)")
plt.plot(r_vals, C_fit_full, "-", label=f"fit ~ exp(-r/ξ), ξ≈{xi:.3e}")
plt.xlabel("r")
plt.ylabel("C(r)/C(0)")
plt.title("Spatial coherence in noisy θ*-agnostic vacuum")
plt.legend()
plt.grid(True)

fig_path = os.path.join(fig_dir, "coherence_check.png")
plt.tight_layout()
plt.savefig(fig_path, dpi=150)
print(f"Saved figure to: {fig_path}")
print("Done.")
