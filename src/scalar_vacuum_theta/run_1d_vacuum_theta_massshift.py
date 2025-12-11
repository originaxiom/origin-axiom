#!/usr/bin/env python3
"""
1D scalar vacuum dispersion with a θ*-dependent mass shift.

We keep θ* AGNOSTIC here.

We only assume that whatever the non-cancelling mechanism is,
it enters the scalar sector as an additive shift in the mass-squared:

    m_eff^2 = m0_bare^2 + Δm2(θ*)

For this script, Δm2 is just a parameter `delta_m2`.  You can think
of it as "whatever the lattice / holonomy calculation will later
give us for a particular θ*".

This script:

  * takes m0_bare and delta_m2 as CLI arguments,
  * computes m_eff = sqrt(m0_bare^2 + delta_m2) (clipped to ≥ 0),
  * runs the usual 1D dispersion test with m_eff,
  * compares measured ω_k to the analytic ω_th(k; m_eff),
  * saves results + a figure in the usual data/ and figures/ trees.

Usage examples:

  # no twist correction (baseline)
  python3 src/scalar_vacuum_theta/run_1d_vacuum_theta_massshift.py

  # small positive Δm² (heavier effective vacuum)
  python3 src/scalar_vacuum_theta/run_1d_vacuum_theta_massshift.py --delta-m2 2.0

  # small negative Δm² (lighter effective vacuum)
  python3 src/scalar_vacuum_theta/run_1d_vacuum_theta_massshift.py --delta-m2 -5.0
"""

import argparse
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt


def laplacian_periodic(theta: np.ndarray, dx: float) -> np.ndarray:
    """Periodic second-derivative (1D) using centered differences."""
    return (np.roll(theta, -1) - 2.0 * theta + np.roll(theta, 1)) / (dx * dx)


def measure_mode_frequency(
    N: int,
    L: float,
    m_eff: float,
    n_mode: int,
    dt: float,
    total_time: float,
    stride: int = 10,
) -> tuple[float, float]:
    """
    Evolve a single sinusoidal mode in 1D and measure its frequency.

    We solve (periodic BC):

        θ̈ - θ_xx + m_eff^2 θ = 0

    with a simple velocity-Verlet / leapfrog scheme and project the field
    onto sin(kx) to get a(t). The dominant FFT peak in a(t) gives ω_meas.
    """
    dx = L / N
    x = np.linspace(0.0, L, N, endpoint=False)
    k = 2.0 * np.pi * n_mode / L

    # Initial condition: pure sin mode, zero initial velocity
    theta = np.sin(k * x)
    theta_dot = np.zeros_like(theta)

    n_steps = int(total_time / dt)
    n_rec = n_steps // stride
    a = np.zeros(n_rec)

    mode = np.sin(k * x)
    # normalization for projection
    norm = np.sum(mode ** 2) * dx

    rec_idx = 0
    for step in range(n_steps):
        # --- velocity Verlet / leapfrog ---
        lap = laplacian_periodic(theta, dx)
        acc = lap - (m_eff ** 2) * theta

        theta_dot += 0.5 * dt * acc
        theta += dt * theta_dot

        lap = laplacian_periodic(theta, dx)
        acc = lap - (m_eff ** 2) * theta
        theta_dot += 0.5 * dt * acc
        # ----------------------------------

        if step % stride == 0:
            a[rec_idx] = np.dot(theta, mode) * dx / norm
            rec_idx += 1

    # Remove any constant offset and FFT the time series
    dt_eff = dt * stride
    a_centered = a - np.mean(a_centered := a)
    A = np.fft.rfft(a_centered)
    freqs = np.fft.rfftfreq(len(a_centered), dt_eff)

    idx_peak = int(np.argmax(np.abs(A)))
    omega_meas = 2.0 * np.pi * freqs[idx_peak]
    return k, omega_meas


def main() -> None:
    parser = argparse.ArgumentParser(
        description="1D scalar vacuum dispersion with θ*-parametric mass shift"
    )
    parser.add_argument(
        "--m0-bare",
        type=float,
        default=5.0,
        help="Bare mass parameter m0_bare (default: 5.0)",
    )
    parser.add_argument(
        "--delta-m2",
        type=float,
        default=0.0,
        help="Mass-squared shift Δm²(θ*) (default: 0.0). "
             "Interpret as coming from the non-cancelling twist.",
    )
    parser.add_argument(
        "--n-max",
        type=int,
        default=8,
        help="Maximum Fourier mode index to test (default: 8)",
    )
    parser.add_argument(
        "--L",
        type=float,
        default=1.0,
        help="Domain length (default: 1.0)",
    )
    parser.add_argument(
        "--N",
        type=int,
        default=2048,
        help="Number of grid points (default: 2048)",
    )
    parser.add_argument(
        "--dt",
        type=float,
        default=1.0e-4,
        help="Time step (default: 1e-4)",
    )
    parser.add_argument(
        "--T",
        type=float,
        default=200.0,
        help="Total evolution time (default: 200.0)",
    )
    args = parser.parse_args()

    m0_bare = float(args.m0_bare)
    delta_m2 = float(args.delta_m2)

    # Ensure the effective mass squared is non-negative
    m2_eff = max(m0_bare ** 2 + delta_m2, 0.0)
    m_eff = np.sqrt(m2_eff)

    print("=== 1D scalar vacuum dispersion with θ*-parametric mass shift ===")
    print(f"L = {args.L}, N = {args.N}")
    print(f"dx = {args.L / args.N:.4e}, dt = {args.dt:.4e}, total_time ≈ {args.T:.1f}")
    print(f"m0_bare = {m0_bare}, delta_m2 = {delta_m2}, m_eff = {m_eff}")
    print("----------------------------------------------------")

    ks = []
    omega_th_list = []
    omega_meas_list = []
    rel_errs = []

    for n in range(1, args.n_max + 1):
        k, omega_meas = measure_mode_frequency(
            N=args.N,
            L=args.L,
            m_eff=m_eff,
            n_mode=n,
            dt=args.dt,
            total_time=args.T,
            stride=10,
        )
        omega_th = np.sqrt(k * k + m_eff ** 2)
        rel_err = (omega_meas - omega_th) / omega_th

        print(
            f"Mode n={n:2d} (k={k:7.4f}): "
            f"ω_meas={omega_meas:9.6f}, ω_th={omega_th:9.6f}, "
            f"rel_err={rel_err:+.3e}"
        )

        ks.append(k)
        omega_th_list.append(omega_th)
        omega_meas_list.append(omega_meas)
        rel_errs.append(rel_err)

    ks = np.array(ks)
    omega_th_arr = np.array(omega_th_list)
    omega_meas_arr = np.array(omega_meas_list)
    rel_errs = np.array(rel_errs)

    # Prepare output directories
    data_dir = Path("data/processed/scalar_vacuum_theta")
    fig_dir = Path("figures/scalar_vacuum_theta")
    data_dir.mkdir(parents=True, exist_ok=True)
    fig_dir.mkdir(parents=True, exist_ok=True)

    # Save CSV
    csv_path = data_dir / "dispersion_theta_massshift_results.csv"
    header = (
        "n,k,omega_th,omega_meas,rel_err,"
        "m0_bare,delta_m2,m_eff"
    )
    n_indices = np.arange(1, args.n_max + 1, dtype=int)
    arr = np.column_stack(
        [n_indices, ks, omega_th_arr, omega_meas_arr, rel_errs]
    )
    # we will append the same m0/Δm²/m_eff info as extra columns per row
    extra_cols = np.column_stack(
        [
            np.full_like(ks, m0_bare),
            np.full_like(ks, delta_m2),
            np.full_like(ks, m_eff),
        ]
    )
    arr_full = np.column_stack([arr, extra_cols])
    np.savetxt(csv_path, arr_full, delimiter=",", header=header, comments="")
    print(f"Saved results to: {csv_path}")

    # Plot: theory vs measured
    plt.figure(figsize=(7, 5))
    plt.plot(ks, omega_th_arr, "o-", label="theory: sqrt(k^2 + m_eff^2)")
    plt.plot(ks, omega_meas_arr, "s--", label="measured")
    plt.xlabel("k")
    plt.ylabel("ω")
    plt.title(
        "1D scalar vacuum dispersion with θ*-parametric mass shift\n"
        f"(m0_bare={m0_bare}, Δm²={delta_m2}, m_eff={m_eff:.3f})"
    )
    plt.legend()
    plt.grid(True)
    fig_path = fig_dir / "dispersion_theta_massshift_check.png"
    plt.tight_layout()
    plt.savefig(fig_path, dpi=150)
    plt.close()
    print(f"Saved figure to: {fig_path}")

    print("Done.")


if __name__ == "__main__":
    main()
