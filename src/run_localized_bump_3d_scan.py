"""
File: src/run_localized_bump_3d_scan.py
Purpose: Scan over parameters of a 3D localized bump (amplitude, width,
  quartic coupling lambda4, and non-cancelling scale epsilon) and measure
  localization fractions over time for free and constrained runs.
Axiom link: Searches for regions in parameter space where the non-cancelling
  constraint plus self-interaction support longer-lived localized structures
  (oscillon-like lumps), as a step toward identifying proto-particles.
Inputs:
  - Command-line arguments to set scan ranges (see below).
Outputs:
  - data/processed/localized_bump_3d_scan.npz
    Contains parameter grids, snapshot times, and localization fractions for
    each parameter combination, for both free and constrained runs.
Usage:
  - python3 src/run_localized_bump_3d_scan.py
"""

import argparse
import os
from itertools import product
from pathlib import Path

import numpy as np


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="3D localized bump parameter scan with/without constraint."
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
        default=600,
        help="Number of time steps to evolve (default: 600).",
    )
    parser.add_argument(
        "--snapshot-stride",
        type=int,
        default=20,
        help="Store a snapshot every this many steps (default: 20).",
    )
    parser.add_argument(
        "--m0",
        type=float,
        default=0.5,
        help="Mass parameter m0 (default: 0.5).",
    )
    # Simple fixed grids; can be overridden via CLI if needed
    parser.add_argument(
        "--amplitudes",
        type=float,
        nargs="+",
        default=[0.2, 0.3],
        help="List of initial bump amplitudes to scan (default: 0.2 0.3).",
    )
    parser.add_argument(
        "--widths",
        type=float,
        nargs="+",
        default=[3.0, 5.0],
        help="List of bump widths (Gaussian sigma) to scan (default: 3.0 5.0).",
    )
    parser.add_argument(
        "--lambda4s",
        type=float,
        nargs="+",
        default=[0.5, 1.0],
        help="List of quartic couplings lambda4 to scan (default: 0.5 1.0).",
    )
    parser.add_argument(
        "--epsilons",
        type=float,
        nargs="+",
        default=[1e-3, 5e-3],
        help="List of non-cancellation scales epsilon to scan "
             "(default: 1e-3 5e-3).",
    )
    return parser.parse_args(argv)


def laplacian_3d(phi):
    return (
        np.roll(phi, 1, axis=0) + np.roll(phi, -1, axis=0)
        + np.roll(phi, 1, axis=1) + np.roll(phi, -1, axis=1)
        + np.roll(phi, 1, axis=2) + np.roll(phi, -1, axis=2)
        - 6.0 * phi
    )


def init_gaussian_bump_3d(N, amplitude, width):
    coords = np.arange(N)
    x, y, z = np.meshgrid(coords, coords, coords, indexing="ij")
    x0 = N / 2.0
    y0 = N / 2.0
    z0 = N / 2.0
    r2 = (x - x0) ** 2 + (y - y0) ** 2 + (z - z0) ** 2
    return amplitude * np.exp(-0.5 * r2 / (width ** 2))


def compute_localization_fraction(phi, center, radius):
    N = phi.shape[0]
    coords = np.arange(N)
    x, y, z = np.meshgrid(coords, coords, coords, indexing="ij")
    cx, cy, cz = center

    dx = np.minimum(np.abs(x - cx), N - np.abs(x - cx))
    dy = np.minimum(np.abs(y - cy), N - np.abs(y - cy))
    dz = np.minimum(np.abs(z - cz), N - np.abs(z - cz))
    r2 = dx**2 + dy**2 + dz**2
    mask = r2 <= radius**2

    total = np.sum(phi**2)
    if total <= 0.0:
        return 0.0
    local = np.sum((phi[mask])**2)
    return float(local / total)


def evolve_and_localization(N, dt, steps, m0, lambda4,
                            amplitude, width, epsilon, snapshot_stride,
                            use_constraint):
    """
    Evolve a 3D bump and return times + localization fractions over time.
    We do not store full fields, only the localization measure.
    """
    phi = init_gaussian_bump_3d(N, amplitude, width)
    pi = np.zeros_like(phi)

    center = (N // 2, N // 2, N // 2)
    radius = int(width * 1.5)

    n_snapshots = steps // snapshot_stride + 1
    t_snap = np.zeros(n_snapshots, dtype=float)
    loc = np.zeros(n_snapshots, dtype=float)

    # initial snapshot
    snap_idx = 0
    t_snap[snap_idx] = 0.0
    loc[snap_idx] = compute_localization_fraction(phi, center, radius)
    snap_idx += 1

    # first half-step for pi
    pi += 0.5 * dt * (laplacian_3d(phi) - (m0 ** 2) * phi - lambda4 * (phi ** 3))

    t = 0.0
    for n in range(1, steps + 1):
        if use_constraint:
            A = phi.mean()
            if abs(A) < epsilon:
                sign = 1.0 if A >= 0.0 else -1.0
                shift = sign * (epsilon - abs(A))
                phi += shift

        phi += dt * pi
        pi += dt * (laplacian_3d(phi) - (m0 ** 2) * phi - lambda4 * (phi ** 3))

        t += dt

        if n % snapshot_stride == 0 and snap_idx < n_snapshots:
            t_snap[snap_idx] = t
            loc[snap_idx] = compute_localization_fraction(phi, center, radius)
            snap_idx += 1

    t_snap = t_snap[:snap_idx]
    loc = loc[:snap_idx]
    return t_snap, loc


def main(argv=None):
    args = parse_args(argv)

    N = args.N
    dt = args.dt
    steps = args.steps
    snapshot_stride = args.snapshot_stride
    m0 = args.m0
    amplitudes = args.amplitudes
    widths = args.widths
    lambda4s = args.lambda4s
    epsilons = args.epsilons

    print("=== 3D localized bump parameter scan ===")
    print(f"N = {N}, dt = {dt}, steps = {steps}, snapshot_stride = {snapshot_stride}")
    print(f"m0 = {m0}")
    print(f"amplitudes = {amplitudes}")
    print(f"widths = {widths}")
    print(f"lambda4s = {lambda4s}")
    print(f"epsilons = {epsilons}")

    # Reference time grid (will be same for all configs)
    n_snapshots = steps // snapshot_stride + 1
    t_snap = dt * snapshot_stride * np.arange(n_snapshots, dtype=float)

    shape = (
        len(amplitudes),
        len(widths),
        len(lambda4s),
        len(epsilons),
        n_snapshots,
    )

    loc_free = np.zeros(shape, dtype=float)
    loc_con = np.zeros(shape, dtype=float)

    for ia, A in enumerate(amplitudes):
        for iw, W in enumerate(widths):
            for il, L4 in enumerate(lambda4s):
                for ie, eps in enumerate(epsilons):
                    print(
                        f"\nConfig: amplitude={A}, width={W}, lambda4={L4}, epsilon={eps}"
                    )

                    t_f, loc_f = evolve_and_localization(
                        N=N,
                        dt=dt,
                        steps=steps,
                        m0=m0,
                        lambda4=L4,
                        amplitude=A,
                        width=W,
                        epsilon=eps,
                        snapshot_stride=snapshot_stride,
                        use_constraint=False,
                    )
                    t_c, loc_c = evolve_and_localization(
                        N=N,
                        dt=dt,
                        steps=steps,
                        m0=m0,
                        lambda4=L4,
                        amplitude=A,
                        width=W,
                        epsilon=eps,
                        snapshot_stride=snapshot_stride,
                        use_constraint=True,
                    )

                    # Sanity: time grids must match the reference
                    if not np.allclose(t_f, t_snap[: t_f.size]):
                        raise RuntimeError("Time grid mismatch in free run.")
                    if not np.allclose(t_c, t_snap[: t_c.size]):
                        raise RuntimeError("Time grid mismatch in constrained run.")

                    loc_free[ia, iw, il, ie, : t_f.size] = loc_f
                    loc_con[ia, iw, il, ie, : t_c.size] = loc_c

    out_dir = Path("data") / "processed"
    os.makedirs(out_dir, exist_ok=True)
    out_path = out_dir / "localized_bump_3d_scan.npz"

    params = dict(
        N=N,
        dt=dt,
        steps=steps,
        snapshot_stride=snapshot_stride,
        m0=m0,
        amplitudes=np.array(amplitudes, dtype=float),
        widths=np.array(widths, dtype=float),
        lambda4s=np.array(lambda4s, dtype=float),
        epsilons=np.array(epsilons, dtype=float),
        description="3D Gaussian bump scan: localization fraction vs time "
                    "for free and constrained runs.",
    )

    np.savez(
        out_path,
        t_snap=t_snap,
        loc_free=loc_free,
        loc_constrained=loc_con,
        params=params,
    )

    print(f"\nSaved 3D localized bump scan to {out_path}")


if __name__ == "__main__":
    main()
