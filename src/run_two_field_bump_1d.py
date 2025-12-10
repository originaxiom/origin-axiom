"""
File: src/run_two_field_bump_1d.py
Purpose: Evolve a localized bump in a 1D two-field scalar lattice (phi, chi)
  with linear coupling and optional non-cancelling constraint on the combined
  mean amplitude.
Axiom link: Tests whether interaction between two fields plus the global
  non-cancelling rule can help sustain localized composite structures
  (proto-bound objects) beyond the single-field case.
Inputs:
  - Command-line arguments (see below).
Outputs:
  - data/processed/two_field_bump_1d.npz
Usage:
  - python3 src/run_two_field_bump_1d.py --steps 2000 --snapshot-stride 20 --g 0.02
"""

import argparse
import os
from pathlib import Path

import numpy as np


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="1D two-field localized bump with/without constraint."
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
        "--m1",
        type=float,
        default=0.2,
        help="Mass of phi field (default: 0.2).",
    )
    parser.add_argument(
        "--m2",
        type=float,
        default=0.3,
        help="Mass of chi field (default: 0.3).",
    )
    parser.add_argument(
        "--g",
        type=float,
        default=0.02,
        help="Linear coupling strength g * phi * chi (default: 0.02, stable).",
    )
    parser.add_argument(
        "--epsilon",
        type=float,
        default=1e-3,
        help="Non-cancellation scale epsilon for combined mean (default: 1e-3).",
    )
    parser.add_argument(
        "--phi-amplitude",
        type=float,
        default=0.1,
        help="Initial Gaussian bump amplitude for phi (default: 0.1).",
    )
    parser.add_argument(
        "--phi-width",
        type=float,
        default=10.0,
        help="Initial Gaussian width (sigma) for phi (default: 10.0).",
    )
    parser.add_argument(
        "--snapshot-stride",
        type=int,
        default=20,
        help="Store a snapshot every this many steps (default: 20).",
    )
    return parser.parse_args(argv)


def laplacian_1d(field):
    """Periodic 1D discrete Laplacian with lattice spacing a=1."""
    return np.roll(field, 1) + np.roll(field, -1) - 2.0 * field


def init_gaussian_bump_1d(N, amplitude, width):
    x = np.arange(N)
    x0 = N / 2.0
    return amplitude * np.exp(-0.5 * ((x - x0) / width) ** 2)


def apply_combined_constraint(phi, chi, epsilon):
    """
    Apply non-cancelling constraint to combined mean vector A = (<phi>, <chi>).
    If |A| < epsilon, shift (phi, chi) uniformly along A (or along phi if A=0)
    so that the new |A| is >= epsilon.
    """
    mean_phi = phi.mean()
    mean_chi = chi.mean()
    A_mag = np.sqrt(mean_phi**2 + mean_chi**2)

    if A_mag >= epsilon:
        return

    if A_mag == 0.0:
        shift_phi = epsilon
        shift_chi = 0.0
    else:
        u_phi = mean_phi / A_mag
        u_chi = mean_chi / A_mag
        shift_mag = epsilon - A_mag
        shift_phi = u_phi * shift_mag
        shift_chi = u_chi * shift_mag

    phi += shift_phi
    chi += shift_chi


def compute_localization(phi, chi, center, window_radius):
    """
    Fraction of total density |phi|^2 + |chi|^2 lying in a window around center.
    """
    N = phi.size
    idx = np.arange(N)
    dist = np.minimum(np.abs(idx - center), N - np.abs(idx - center))
    mask = dist <= window_radius

    dens = phi**2 + chi**2
    total = np.sum(dens)
    if total <= 0.0:
        return 0.0
    local = np.sum(dens[mask])
    return float(local / total)


def evolve_two_field_bump(
    N, dt, steps, m1, m2, g, epsilon, phi_amp, phi_width, snapshot_stride,
    use_constraint
):
    """
    Evolve two coupled fields starting from a localized bump in phi
    (chi initially zero). Return snapshot times, localization vs time, and
    a few representative profiles.
    """
    # Initial fields
    phi = init_gaussian_bump_1d(N, phi_amp, phi_width)
    chi = np.zeros(N, dtype=float)

    pi_phi = np.zeros_like(phi)
    pi_chi = np.zeros_like(chi)

    center = N // 2
    window_radius = int(1.5 * phi_width)

    n_snapshots = steps // snapshot_stride + 1
    t_snap = np.zeros(n_snapshots, dtype=float)
    loc_snap = np.zeros(n_snapshots, dtype=float)

    # also store a small number of full profiles for plotting (start, mid, end)
    profile_indices = [0, steps // 4, steps // 2, steps]
    profile_indices = sorted(set(profile_indices))
    profile_times = []
    profiles_phi = []
    profiles_chi = []

    # Initial snapshot
    snap_idx = 0
    t_snap[snap_idx] = 0.0
    loc_snap[snap_idx] = compute_localization(phi, chi, center, window_radius)
    snap_idx += 1

    # Record initial profiles if requested
    if 0 in profile_indices:
        profile_times.append(0.0)
        profiles_phi.append(phi.copy())
        profiles_chi.append(chi.copy())

    # initial half-step for momenta
    lap_phi = laplacian_1d(phi)
    lap_chi = laplacian_1d(chi)
    pi_phi += 0.5 * dt * (lap_phi - m1**2 * phi - g * chi)
    pi_chi += 0.5 * dt * (lap_chi - m2**2 * chi - g * phi)

    t = 0.0
    for n in range(1, steps + 1):
        if use_constraint:
            apply_combined_constraint(phi, chi, epsilon)

        # full step for fields
        phi += dt * pi_phi
        chi += dt * pi_chi

        # full step for momenta
        lap_phi = laplacian_1d(phi)
        lap_chi = laplacian_1d(chi)
        pi_phi += dt * (lap_phi - m1**2 * phi - g * chi)
        pi_chi += dt * (lap_chi - m2**2 * chi - g * phi)

        t += dt

        # localization snapshot
        if n % snapshot_stride == 0 and snap_idx < n_snapshots:
            t_snap[snap_idx] = t
            loc_snap[snap_idx] = compute_localization(phi, chi, center, window_radius)
            snap_idx += 1

        # store profiles at selected times
        if n in profile_indices:
            profile_times.append(t)
            profiles_phi.append(phi.copy())
            profiles_chi.append(chi.copy())

    t_snap = t_snap[:snap_idx]
    loc_snap = loc_snap[:snap_idx]

    profiles_phi = np.array(profiles_phi)
    profiles_chi = np.array(profiles_chi)
    profile_times = np.array(profile_times)

    return t_snap, loc_snap, profile_times, profiles_phi, profiles_chi


def main(argv=None):
    args = parse_args(argv)

    N = args.N
    dt = args.dt
    steps = args.steps
    m1 = args.m1
    m2 = args.m2
    g = args.g
    epsilon = args.epsilon
    phi_amp = args.phi_amplitude
    phi_width = args.phi_width
    snapshot_stride = args.snapshot_stride

    print("=== 1D two-field localized bump run ===")
    print(f"N = {N}, dt = {dt}, steps = {steps}")
    print(f"m1 = {m1}, m2 = {m2}, g = {g}, epsilon = {epsilon}")
    print(f"phi_amp = {phi_amp}, phi_width = {phi_width}")
    print(f"snapshot_stride = {snapshot_stride}")

    print("\nRunning free (no constraint) evolution...")
    t_free, loc_free, pt_free, prof_phi_free, prof_chi_free = evolve_two_field_bump(
        N=N,
        dt=dt,
        steps=steps,
        m1=m1,
        m2=m2,
        g=g,
        epsilon=epsilon,
        phi_amp=phi_amp,
        phi_width=phi_width,
        snapshot_stride=snapshot_stride,
        use_constraint=False,
    )

    print("Running constrained evolution (with non-cancelling rule)...")
    t_con, loc_con, pt_con, prof_phi_con, prof_chi_con = evolve_two_field_bump(
        N=N,
        dt=dt,
        steps=steps,
        m1=m1,
        m2=m2,
        g=g,
        epsilon=epsilon,
        phi_amp=phi_amp,
        phi_width=phi_width,
        snapshot_stride=snapshot_stride,
        use_constraint=True,
    )

    if not np.allclose(t_free, t_con):
        raise RuntimeError("Snapshot time arrays differ between free and constrained runs.")

    out_dir = Path("data") / "processed"
    os.makedirs(out_dir, exist_ok=True)
    out_path = out_dir / "two_field_bump_1d.npz"

    params = dict(
        N=N,
        dt=dt,
        steps=steps,
        m1=m1,
        m2=m2,
        g=g,
        epsilon=epsilon,
        phi_amp=phi_amp,
        phi_width=phi_width,
        snapshot_stride=snapshot_stride,
        description="1D two-field localized bump with/without non-cancelling constraint",
    )

    np.savez(
        out_path,
        t_snap=t_free,
        loc_free=loc_free,
        loc_constrained=loc_con,
        profile_times_free=pt_free,
        profiles_phi_free=prof_phi_free,
        profiles_chi_free=prof_chi_free,
        profile_times_constrained=pt_con,
        profiles_phi_constrained=prof_phi_con,
        profiles_chi_constrained=prof_chi_con,
        params=params,
    )

    print(f"\nSaved two-field bump data to {out_path}")


if __name__ == "__main__":
    main()
