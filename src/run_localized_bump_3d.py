"""
File: src/run_localized_bump_3d.py
Purpose: Evolve a localized bump in a 3D scalar lattice with and without a
  simple global non-cancelling constraint on the mean field, including a
  quartic self-interaction.
Axiom link: Tests whether the non-cancelling rule, combined with a
  self-interacting scalar field, can support long-lived localized structures
  (proto-oscillons) in 3D.
Inputs:
  - Command-line arguments (see below).
Outputs:
  - data/processed/localized_bump_3d.npz
    Contains snapshot times and field snapshots for free and constrained runs.
Usage:
  - python3 src/run_localized_bump_3d.py --steps 800 --snapshot-stride 20
"""

import argparse
import os
from pathlib import Path

import numpy as np


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="3D localized bump with/without non-cancelling constraint."
    )
    parser.add_argument(
        "--N",
        type=int,
        default=40,
        help="Linear lattice size N (total sites N^3, default: 40).",
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
        default=800,
        help="Number of time steps to evolve (default: 800).",
    )
    parser.add_argument(
        "--m0",
        type=float,
        default=0.5,
        help="Mass parameter m0 (default: 0.5).",
    )
    parser.add_argument(
        "--lambda4",
        type=float,
        default=1.0,
        help="Quartic self-interaction coupling lambda (default: 1.0).",
    )
    parser.add_argument(
        "--amplitude",
        type=float,
        default=0.3,
        help="Initial bump amplitude (default: 0.3).",
    )
    parser.add_argument(
        "--width",
        type=float,
        default=4.0,
        help="Initial bump width (Gaussian sigma in lattice units, default: 4.0).",
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


def laplacian_3d(phi):
    """
    Periodic 3D discrete Laplacian with lattice spacing a = 1.
    phi has shape (N, N, N).
    """
    return (
        np.roll(phi, 1, axis=0) + np.roll(phi, -1, axis=0)
        + np.roll(phi, 1, axis=1) + np.roll(phi, -1, axis=1)
        + np.roll(phi, 1, axis=2) + np.roll(phi, -1, axis=2)
        - 6.0 * phi
    )


def init_gaussian_bump_3d(N, amplitude, width):
    """
    Initialise a 3D Gaussian bump centered at (N/2, N/2, N/2) on a periodic
    cubic lattice.
    """
    coords = np.arange(N)
    x, y, z = np.meshgrid(coords, coords, coords, indexing="ij")
    x0 = N / 2.0
    y0 = N / 2.0
    z0 = N / 2.0
    r2 = (x - x0) ** 2 + (y - y0) ** 2 + (z - z0) ** 2
    return amplitude * np.exp(-0.5 * r2 / (width ** 2))


def evolve_bump_3d(N, dt, steps, m0, lambda4, amplitude, width,
                   epsilon, use_constraint, snapshot_stride):
    """
    Evolve a 3D real scalar field with an initial Gaussian bump, quartic
    self-interaction, and optional non-cancelling constraint on the global
    mean field A(t) = <phi>.
    Returns snapshot times and field snapshots.
    """
    phi = init_gaussian_bump_3d(N, amplitude, width)
    pi = np.zeros_like(phi)

    n_snapshots = steps // snapshot_stride + 1
    snapshots = np.zeros((n_snapshots, N, N, N), dtype=float)
    t_snap = np.zeros(n_snapshots, dtype=float)

    # Store initial configuration
    snap_idx = 0
    snapshots[snap_idx] = phi.copy()
    t_snap[snap_idx] = 0.0
    snap_idx += 1

    # First half-step for pi: pi_{1/2} = pi_0 + dt/2 * (laplacian - dV/dphi)
    pi += 0.5 * dt * (laplacian_3d(phi) - (m0 ** 2) * phi - lambda4 * (phi ** 3))

    t = 0.0
    for n in range(1, steps + 1):
        # Optional non-cancelling constraint on global mean
        if use_constraint:
            A = phi.mean()
            if abs(A) < epsilon:
                sign = 1.0 if A >= 0.0 else -1.0
                shift = sign * (epsilon - abs(A))
                phi += shift

        # Full step for phi
        phi += dt * pi
        # Full step for pi
        pi += dt * (laplacian_3d(phi) - (m0 ** 2) * phi - lambda4 * (phi ** 3))

        t += dt

        if n % snapshot_stride == 0 and snap_idx < n_snapshots:
            snapshots[snap_idx] = phi.copy()
            t_snap[snap_idx] = t
            snap_idx += 1

    snapshots = snapshots[:snap_idx]
    t_snap = t_snap[:snap_idx]

    return t_snap, snapshots


def main(argv=None):
    args = parse_args(argv)

    N = args.N
    dt = args.dt
    steps = args.steps
    m0 = args.m0
    lambda4 = args.lambda4
    amplitude = args.amplitude
    width = args.width
    epsilon = args.epsilon
    snapshot_stride = args.snapshot_stride

    print("=== 3D localized bump run ===")
    print(f"N = {N}, dt = {dt}, steps = {steps}")
    print(f"m0 = {m0}, lambda4 = {lambda4}")
    print(f"amplitude = {amplitude}, width = {width}, epsilon = {epsilon}")
    print(f"snapshot_stride = {snapshot_stride}")

    print("\nRunning free (unconstrained) evolution...")
    t_free, snaps_free = evolve_bump_3d(
        N=N,
        dt=dt,
        steps=steps,
        m0=m0,
        lambda4=lambda4,
        amplitude=amplitude,
        width=width,
        epsilon=epsilon,
        use_constraint=False,
        snapshot_stride=snapshot_stride,
    )

    print("Running constrained evolution (with non-cancelling rule)...")
    t_con, snaps_con = evolve_bump_3d(
        N=N,
        dt=dt,
        steps=steps,
        m0=m0,
        lambda4=lambda4,
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
    out_path = out_dir / "localized_bump_3d.npz"

    params = dict(
        N=N,
        dt=dt,
        steps=steps,
        m0=m0,
        lambda4=lambda4,
        amplitude=amplitude,
        width=width,
        epsilon=epsilon,
        snapshot_stride=snapshot_stride,
        description="3D Gaussian bump with quartic self-interaction "
                    "with/without non-cancelling constraint",
    )

    np.savez(
        out_path,
        t_snap=t_free,
        snaps_free=snaps_free,
        snaps_constrained=snaps_con,
        params=params,
    )

    print(f"\nSaved 3D localized bump data to {out_path}")


if __name__ == "__main__":
    main()
