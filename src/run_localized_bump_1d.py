"""
File: src/run_localized_bump_1d.py
Purpose: Evolve a localized bump in a 1D scalar lattice with and without a
  simple global non-cancelling constraint on the mean field.
Axiom link: Tests whether the non-cancelling rule affects the stability and
  dispersion of localized structures (proto-particles) in a minimal 1D model.
Inputs:
  - Command-line arguments (see below).
Outputs:
  - data/processed/localized_bump_1d.npz
    Contains snapshots of the field for free and constrained runs.
Usage:
  - python3 src/run_localized_bump_1d.py --steps 2000 --snapshot-stride 20
"""

import argparse
import os
from pathlib import Path

import numpy as np


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="1D localized bump with/without non-cancelling constraint."
    )
    parser.add_argument(
        "--N",
        type=int,
        default=512,
        help="Number of lattice sites (default: 512).",
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
        default=2000,
        help="Number of time steps to evolve (default: 2000).",
    )
    parser.add_argument(
        "--m0",
        type=float,
        default=0.1,
        help="Mass parameter m0 (default: 0.1).",
    )
    parser.add_argument(
        "--amplitude",
        type=float,
        default=0.1,
        help="Initial bump amplitude (default: 0.1).",
    )
    parser.add_argument(
        "--width",
        type=float,
        default=10.0,
        help="Initial bump width (Gaussian sigma, default: 10.0).",
    )
    parser.add_argument(
        "--epsilon",
        type=float,
        default=1e-3,
        help="Non-cancellation scale epsilon for the constrained run "
             "(default: 1e-3).",
    )
    parser.add_argument(
        "--snapshot-stride",
        type=int,
        default=20,
        help="Store a snapshot every this many steps (default: 20).",
    )
    return parser.parse_args(argv)


def laplacian_1d(phi):
    """Periodic 1D discrete Laplacian with lattice spacing a=1."""
    return np.roll(phi, 1) + np.roll(phi, -1) - 2.0 * phi


def init_gaussian_bump(N, amplitude, width):
    """
    Initialise a Gaussian bump centered at N/2 on a periodic 1D lattice.
    """
    x = np.arange(N)
    x0 = N / 2.0
    return amplitude * np.exp(-0.5 * ((x - x0) / width) ** 2)


def evolve_bump(N, dt, steps, m0, amplitude, width, epsilon, use_constraint, snapshot_stride):
    """
    Evolve a 1D real scalar field with an initial Gaussian bump and optional
    non-cancelling constraint on the global mean field A(t) = <phi>.
    Returns snapshot times and field snapshots.
    """
    phi = init_gaussian_bump(N, amplitude, width)
    pi = np.zeros(N, dtype=float)

    n_snapshots = steps // snapshot_stride + 1
    snapshots = np.zeros((n_snapshots, N), dtype=float)
    t_snap = np.zeros(n_snapshots, dtype=float)

    # Store initial configuration
    snap_idx = 0
    snapshots[snap_idx] = phi.copy()
    t_snap[snap_idx] = 0.0
    snap_idx += 1

    # First half-step for pi
    pi += 0.5 * dt * (laplacian_1d(phi) - (m0 ** 2) * phi)

    t = 0.0
    for n in range(1, steps + 1):
        # Optional non-cancelling constraint on mean field
        if use_constraint:
            A = phi.mean()
            if abs(A) < epsilon:
                sign = 1.0 if A >= 0.0 else -1.0
                shift = sign * (epsilon - abs(A))
                phi += shift

        # Full step for phi
        phi += dt * pi
        # Full step for pi
        pi += dt * (laplacian_1d(phi) - (m0 ** 2) * phi)

        t += dt

        if n % snapshot_stride == 0 and snap_idx < n_snapshots:
            snapshots[snap_idx] = phi.copy()
            t_snap[snap_idx] = t
            snap_idx += 1

    # Trim in case of rounding
    snapshots = snapshots[:snap_idx]
    t_snap = t_snap[:snap_idx]

    return t_snap, snapshots


def main(argv=None):
    args = parse_args(argv)

    N = args.N
    dt = args.dt
    steps = args.steps
    m0 = args.m0
    amplitude = args.amplitude
    width = args.width
    epsilon = args.epsilon
    snapshot_stride = args.snapshot_stride

    print("=== 1D localized bump run ===")
    print(f"N = {N}, dt = {dt}, steps = {steps}, m0 = {m0}")
    print(f"amplitude = {amplitude}, width = {width}, epsilon = {epsilon}")
    print(f"snapshot_stride = {snapshot_stride}")

    print("\nRunning free (unconstrained) evolution...")
    t_free, snaps_free = evolve_bump(
        N=N,
        dt=dt,
        steps=steps,
        m0=m0,
        amplitude=amplitude,
        width=width,
        epsilon=epsilon,
        use_constraint=False,
        snapshot_stride=snapshot_stride,
    )

    print("Running constrained evolution (with non-cancelling rule)...")
    t_con, snaps_con = evolve_bump(
        N=N,
        dt=dt,
        steps=steps,
        m0=m0,
        amplitude=amplitude,
        width=width,
        epsilon=epsilon,
        use_constraint=True,
        snapshot_stride=snapshot_stride,
    )

    if not np.allclose(t_free, t_con):
        raise RuntimeError("Snapshot time arrays differ between runs.")

    out_dir = Path("data") / "processed"
    os.makedirs(out_dir, exist_ok=True)
    out_path = out_dir / "localized_bump_1d.npz"

    params = dict(
        N=N,
        dt=dt,
        steps=steps,
        m0=m0,
        amplitude=amplitude,
        width=width,
        epsilon=epsilon,
        snapshot_stride=snapshot_stride,
        description="1D Gaussian bump with/without non-cancelling constraint",
    )

    np.savez(
        out_path,
        t_snap=t_free,
        snaps_free=snaps_free,
        snaps_constrained=snaps_con,
        params=params,
    )

    print(f"\nSaved localized bump data to {out_path}")


if __name__ == "__main__":
    main()
