"""
File: src/run_mode_spectrum_with_constraint.py
Purpose: Probe the mode spectrum (omega(k)) of a 1D scalar lattice with and
  without a simple global non-cancelling constraint.
Axiom link: Models a minimal version of the Origin Axiom by enforcing that the
  global mean field A(t) = <phi> never falls below a small scale epsilon in
  magnitude. Compares how this constraint affects the oscillation frequency
  of a chosen Fourier mode.
Inputs:
  - Command-line arguments (see below).
Outputs:
  - data/processed/mode_spectrum_1d.npz
    Contains time series and parameters for both constrained and unconstrained
    runs.
Usage:
  - python3 src/run_mode_spectrum_with_constraint.py --steps 4096 --k-index 1
"""

import argparse
import os
from pathlib import Path

import numpy as np


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="1D scalar mode spectrum with/without non-cancelling constraint."
    )
    parser.add_argument(
        "--N",
        type=int,
        default=256,
        help="Number of lattice sites (default: 256).",
    )
    parser.add_argument(
        "--dt",
        type=float,
        default=0.05,
        help="Time step (default: 0.05).",
    )
    parser.add_argument(
        "--steps",
        type=int,
        default=4096,
        help="Number of time steps to evolve (default: 4096).",
    )
    parser.add_argument(
        "--m0",
        type=float,
        default=0.1,
        help="Mass parameter m0 (default: 0.1).",
    )
    parser.add_argument(
        "--k-index",
        type=int,
        default=1,
        help="Integer mode index k (0 <= k < N). Default: 1.",
    )
    parser.add_argument(
        "--epsilon",
        type=float,
        default=1e-3,
        help="Non-cancellation scale epsilon for the constrained run "
             "(default: 1e-3).",
    )
    parser.add_argument(
        "--amplitude",
        type=float,
        default=1e-3,
        help="Initial cosine-mode amplitude (default: 1e-3).",
    )
    return parser.parse_args(argv)


def laplacian_1d(phi):
    """Periodic 1D discrete Laplacian with lattice spacing a=1."""
    return np.roll(phi, 1) + np.roll(phi, -1) - 2.0 * phi


def project_mode(phi, k_index):
    """
    Project the field onto a cosine mode with integer index k_index.
    This is a simple real-valued projection used as the observable.
    """
    N = phi.size
    x = np.arange(N)
    theta = 2.0 * np.pi * k_index * x / float(N)
    basis = np.cos(theta)
    return (phi * basis).mean()


def evolve_mode_spectrum(N, dt, steps, m0, k_index, amplitude, epsilon, use_constraint):
    """
    Evolve a 1D real scalar field with initial cosine mode and optional
    non-cancelling constraint on the global mean field A(t) = <phi>.
    Returns time array and projected mode time series.
    """
    # Field and conjugate momentum
    phi = np.zeros(N, dtype=float)
    pi = np.zeros(N, dtype=float)

    # Initial cosine mode
    x = np.arange(N)
    theta = 2.0 * np.pi * k_index * x / float(N)
    phi[:] = amplitude * np.cos(theta)
    # pi already zero

    # Time array and observable storage
    t_arr = dt * np.arange(steps, dtype=float)
    mode_vals = np.zeros(steps, dtype=float)

    # Leapfrog-like update
    # First half-step for pi
    pi += 0.5 * dt * (laplacian_1d(phi) - (m0 ** 2) * phi)

    for n in range(steps):
        # Optional global non-cancelling constraint on the mean field
        if use_constraint:
            A = phi.mean()
            if abs(A) < epsilon:
                # Shift phi uniformly so that |<phi>| >= epsilon.
                # Keep the sign of A if nonzero, otherwise pick +1.
                sign = 1.0 if A >= 0.0 else -1.0
                shift = sign * (epsilon - abs(A))
                phi += shift

        # Full step for phi
        phi += dt * pi

        # Full step for pi (kick)
        pi += dt * (laplacian_1d(phi) - (m0 ** 2) * phi)

        # Record projected mode
        mode_vals[n] = project_mode(phi, k_index)

    return t_arr, mode_vals


def main(argv=None):
    args = parse_args(argv)

    N = args.N
    dt = args.dt
    steps = args.steps
    m0 = args.m0
    k_index = args.k_index
    amplitude = args.amplitude
    epsilon = args.epsilon

    if k_index < 0 or k_index >= N:
        raise ValueError(f"k-index must satisfy 0 <= k-index < N (got {k_index}, N={N})")

    print("=== 1D mode spectrum run ===")
    print(f"N = {N}, dt = {dt}, steps = {steps}, m0 = {m0}")
    print(f"k_index = {k_index}, amplitude = {amplitude}, epsilon = {epsilon}")

    # Unconstrained run
    print("\nRunning unconstrained evolution...")
    t_free, mode_free = evolve_mode_spectrum(
        N=N,
        dt=dt,
        steps=steps,
        m0=m0,
        k_index=k_index,
        amplitude=amplitude,
        epsilon=epsilon,
        use_constraint=False,
    )

    # Constrained run
    print("\nRunning constrained evolution (with non-cancelling rule)...")
    t_con, mode_con = evolve_mode_spectrum(
        N=N,
        dt=dt,
        steps=steps,
        m0=m0,
        k_index=k_index,
        amplitude=amplitude,
        epsilon=epsilon,
        use_constraint=True,
    )

    # Sanity check on time arrays
    if not np.allclose(t_free, t_con):
        raise RuntimeError("Time arrays for constrained and unconstrained runs differ.")

    # Prepare output directory
    out_dir = Path("data") / "processed"
    os.makedirs(out_dir, exist_ok=True)
    out_path = out_dir / "mode_spectrum_1d.npz"

    params = dict(
        N=N,
        dt=dt,
        steps=steps,
        m0=m0,
        k_index=k_index,
        amplitude=amplitude,
        epsilon=epsilon,
        description="1D scalar mode spectrum with/without non-cancelling constraint",
    )

    np.savez(
        out_path,
        t=t_free,
        mode_free=mode_free,
        mode_constrained=mode_con,
        params=params,
    )

    print(f"\nSaved mode spectrum data to {out_path}")


if __name__ == "__main__":
    main()
