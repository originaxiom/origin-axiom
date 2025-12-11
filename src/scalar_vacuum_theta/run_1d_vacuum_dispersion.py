#!/usr/bin/env python3
"""
run_1d_vacuum_dispersion.py

θ*-agnostic 1D scalar vacuum dispersion test.

Evolves a real scalar field θ(x,t) on a 1D periodic lattice with equation:

    θ_tt = θ_xx - m0^2 θ

(in units where c = 1),

excites a few Fourier modes, measures their oscillation frequencies from
time series, and compares to the theoretical dispersion:

    ω_k^2 = k^2 + m0^2,

with k_n = 2π n / L.

Outputs:
  - data/processed/scalar_vacuum_theta/dispersion_results.npz
  - data/processed/scalar_vacuum_theta/dispersion_results.csv
  - figures/scalar_vacuum_theta/dispersion_check.png (if matplotlib available)
"""

import os
import math
import csv
from dataclasses import dataclass, asdict
from typing import List

import numpy as np


@dataclass
class DispersionResult:
    mode_index: int
    k: float
    omega_theory: float
    omega_measured: float
    rel_error: float


def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def leapfrog_step(theta, theta_dot, m0, dx, dt):
    """
    One leapfrog step for θ_tt = θ_xx - m0^2 θ on a periodic 1D lattice.
    Uses second-order central differences and periodic boundary conditions.
    """
    # Compute spatial second derivative with periodic BC
    theta_xx = (np.roll(theta, -1) - 2.0 * theta + np.roll(theta, 1)) / (dx * dx)
    # Acceleration
    theta_tt = theta_xx - (m0 * m0) * theta
    # Half-step velocity
    theta_dot_half = theta_dot + 0.5 * dt * theta_tt
    # Full-step position
    theta_new = theta + dt * theta_dot_half
    # Recompute acceleration at new position
    theta_xx_new = (np.roll(theta_new, -1) - 2.0 * theta_new + np.roll(theta_new, 1)) / (dx * dx)
    theta_tt_new = theta_xx_new - (m0 * m0) * theta_new
    # Full-step velocity
    theta_dot_new = theta_dot_half + 0.5 * dt * theta_tt_new
    return theta_new, theta_dot_new


def project_mode(theta_series, x, k):
    """
    Project θ(x,t) onto cos(kx) mode over space, for each time slice.

    theta_series: array of shape (T, N)
    x: spatial grid (N,)
    k: wavenumber
    """
    cos_kx = np.cos(k * x)
    # Normalize so that a pure cos(kx) with amplitude A gives projection ~ A
    norm = np.sum(cos_kx**2)
    proj = theta_series @ cos_kx / norm
    return proj


def measure_frequency_from_fft(time, signal):
    """
    Given time grid and real signal(t), compute dominant frequency via FFT.
    Returns angular frequency ω (rad/time).
    """
    T = time[-1] - time[0]
    n = len(time)
    # Assume uniform spacing
    dt = time[1] - time[0]

    # Remove mean to avoid zero-frequency dominance
    signal = signal - np.mean(signal)

    # FFT
    fft_vals = np.fft.rfft(signal)
    freqs = np.fft.rfftfreq(n, d=dt)  # cycles per unit time
    power = np.abs(fft_vals)**2

    # Ignore zero-frequency bin
    if len(power) > 1:
        power[0] = 0.0

    idx = np.argmax(power)
    f_peak = freqs[idx]          # cycles / time
    omega_peak = 2.0 * math.pi * f_peak  # rad / time
    return omega_peak


def run_dispersion_test():
    # -----------------------------
    # Simulation parameters
    # -----------------------------
    L = 1.0              # domain length
    N = 2048             # number of spatial points
    m0 = 5.0             # mass term (sets ω0 ~ m0 for k=0)
    c = 1.0              # wave speed (kept as 1 for now)

    # CFL condition for leapfrog (rough guideline)
    dx = L / N
    cfl = 0.3
    dt = cfl * dx / c

    total_time = 200.0   # total simulated time
    n_steps = int(total_time / dt)

    # How often to sample for Fourier analysis
    sample_stride = 10
    n_samples = n_steps // sample_stride + 1

    # Modes to test (k_n = 2π n / L)
    mode_indices = [1, 2, 3, 4, 5, 6, 7, 8]

    # -----------------------------
    # Output setup
    # -----------------------------
    out_dir = os.path.join("data", "processed", "scalar_vacuum_theta")
    fig_dir = os.path.join("figures", "scalar_vacuum_theta")
    ensure_dir(out_dir)
    ensure_dir(fig_dir)

    # Spatial grid
    x = np.linspace(0.0, L, N, endpoint=False)

    results: List[DispersionResult] = []

    # For diagnostic storage (optional, only first mode to avoid giant files)
    store_timeseries = True
    stored = {}

    print("=== 1D θ*-agnostic scalar vacuum dispersion test ===")
    print(f"L = {L}, N = {N}, dx = {dx:.4e}, dt = {dt:.4e}, total_time ≈ {total_time}")
    print(f"m0 = {m0}")
    print("----------------------------------------------------")

    for n in mode_indices:
        k_n = 2.0 * math.pi * n / L
        omega_theory = math.sqrt(k_n * k_n + m0 * m0)

        print(f"Running mode n={n} (k={k_n:.4f}, ω_th={omega_theory:.4f}) ...")

        # Initial conditions: θ(x,0) = A cos(k_n x), θ_t(x,0) = 0
        A = 1.0
        theta = A * np.cos(k_n * x)
        theta_dot = np.zeros_like(theta)

        # Time series for projection
        proj_series = np.zeros(n_samples, dtype=np.float64)
        time_series = np.zeros(n_samples, dtype=np.float64)

        s_idx = 0
        proj_series[s_idx] = np.sum(theta * np.cos(k_n * x)) / np.sum(np.cos(k_n * x)**2)
        time_series[s_idx] = 0.0
        s_idx += 1

        # Main time loop
        for step in range(1, n_steps + 1):
            theta, theta_dot = leapfrog_step(theta, theta_dot, m0, dx, dt)

            if step % sample_stride == 0:
                t = step * dt
                time_series[s_idx] = t
                proj_series[s_idx] = np.sum(theta * np.cos(k_n * x)) / np.sum(np.cos(k_n * x)**2)
                s_idx += 1

        # Truncate in case we didn't fill exactly
        time_used = time_series[:s_idx]
        proj_used = proj_series[:s_idx]

        # Measure frequency
        omega_meas = measure_frequency_from_fft(time_used, proj_used)
        rel_err = (omega_meas - omega_theory) / omega_theory

        results.append(DispersionResult(
            mode_index=n,
            k=k_n,
            omega_theory=omega_theory,
            omega_measured=omega_meas,
            rel_error=rel_err
        ))

        print(f"  ω_meas = {omega_meas:.6f}, rel_err = {rel_err:.3e}")

        if store_timeseries and n == mode_indices[0]:
            stored["time"] = time_used
            stored["proj_n1"] = proj_used

    # -----------------------------
    # Save numeric results
    # -----------------------------
    # npz
    npz_path = os.path.join(out_dir, "dispersion_results.npz")
    np.savez(
        npz_path,
        mode_indices=np.array([r.mode_index for r in results]),
        k=np.array([r.k for r in results]),
        omega_theory=np.array([r.omega_theory for r in results]),
        omega_measured=np.array([r.omega_measured for r in results]),
        rel_error=np.array([r.rel_error for r in results]),
        **stored
    )

    # csv
    csv_path = os.path.join(out_dir, "dispersion_results.csv")
    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["mode_index", "k", "omega_theory", "omega_measured", "rel_error"])
        for r in results:
            writer.writerow([r.mode_index, r.k, r.omega_theory, r.omega_measured, r.rel_error])

    print("----------------------------------------------------")
    print(f"Saved results to:")
    print(f"  {npz_path}")
    print(f"  {csv_path}")

    # -----------------------------
    # Optional plot
    # -----------------------------
    try:
        import matplotlib.pyplot as plt

        ks = np.array([r.k for r in results])
        w_th = np.array([r.omega_theory for r in results])
        w_me = np.array([r.omega_measured for r in results])

        plt.figure()
        plt.plot(ks, w_th, "o-", label="theory: sqrt(k^2 + m0^2)")
        plt.plot(ks, w_me, "s--", label="measured")
        plt.xlabel("k")
        plt.ylabel("ω")
        plt.title("1D scalar vacuum dispersion (θ*-agnostic)")
        plt.legend()
        plt.grid(True)

        fig_path = os.path.join(fig_dir, "dispersion_check.png")
        plt.savefig(fig_path, dpi=200, bbox_inches="tight")
        plt.close()
        print(f"Saved figure to: {fig_path}")
    except Exception as e:
        print("Could not create plot (matplotlib missing or error):", e)

    print("Done.")


if __name__ == "__main__":
    run_dispersion_test()
