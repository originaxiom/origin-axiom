"""
File: src/run_two_field_coupling_1d.py
Purpose: 1D two-field scalar lattice (phi, chi) with linear coupling and
  optional non-cancelling constraint on the combined mean amplitude.
Axiom link: Models a minimal "two-sector" universe where the Origin Axiom
  acts on the global mean vector A = (<phi>, <chi>). We compare how energy
  and amplitude exchange between fields with and without the constraint.
Inputs:
  - Command-line arguments (see below).
Outputs:
  - data/processed/two_field_coupling_1d.npz
Usage:
  - python3 src/run_two_field_coupling_1d.py --steps 4000 --g 0.1
"""

import argparse
import os
from pathlib import Path

import numpy as np


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="1D two-field coupling test with non-cancelling constraint."
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
        default=4000,
        help="Number of time steps to evolve (default: 4000).",
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
        default=0.1,
        help="Linear coupling strength g * phi * chi (default: 0.1).",
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
        help="Initial cosine amplitude for phi (default: 0.1).",
    )
    parser.add_argument(
        "--chi-amplitude",
        type=float,
        default=0.0,
        help="Initial cosine amplitude for chi (default: 0.0).",
    )
    return parser.parse_args(argv)


def laplacian_1d(field):
    """Periodic 1D discrete Laplacian with lattice spacing a=1."""
    return np.roll(field, 1) + np.roll(field, -1) - 2.0 * field


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
        # If both means are zero, choose a simple direction along phi.
        shift_phi = epsilon
        shift_chi = 0.0
    else:
        # Unit vector along current mean
        u_phi = mean_phi / A_mag
        u_chi = mean_chi / A_mag
        shift_mag = epsilon - A_mag
        shift_phi = u_phi * shift_mag
        shift_chi = u_chi * shift_mag

    phi += shift_phi
    chi += shift_chi


def compute_energies(phi, chi, pi_phi, pi_chi, m1, m2, g):
    """
    Compute total energy and per-field pieces on a 1D lattice.
    """
    # Kinetic
    T_phi = 0.5 * np.sum(pi_phi**2)
    T_chi = 0.5 * np.sum(pi_chi**2)

    # Gradient terms (nearest-neighbour)
    grad_phi = np.roll(phi, -1) - phi
    grad_chi = np.roll(chi, -1) - chi
    G_phi = 0.5 * np.sum(grad_phi**2)
    G_chi = 0.5 * np.sum(grad_chi**2)

    # Mass terms
    V_phi_mass = 0.5 * m1**2 * np.sum(phi**2)
    V_chi_mass = 0.5 * m2**2 * np.sum(chi**2)

    # Coupling term
    V_coup = g * np.sum(phi * chi)

    E_phi = T_phi + G_phi + V_phi_mass
    E_chi = T_chi + G_chi + V_chi_mass
    E_total = E_phi + E_chi + V_coup

    return E_total, E_phi, E_chi, V_coup


def evolve_two_field_system(
    N, dt, steps, m1, m2, g, epsilon, phi_amp, chi_amp, use_constraint
):
    """
    Evolve two coupled 1D fields with optional non-cancelling constraint.
    Returns time array and time series for mean fields and energies.
    """
    x = np.arange(N)
    mode = 1
    theta = 2.0 * np.pi * mode * x / float(N)

    phi = phi_amp * np.cos(theta)
    chi = chi_amp * np.cos(theta)

    pi_phi = np.zeros_like(phi)
    pi_chi = np.zeros_like(chi)

    t_arr = dt * np.arange(steps, dtype=float)
    mean_phi_arr = np.zeros(steps, dtype=float)
    mean_chi_arr = np.zeros(steps, dtype=float)
    E_total_arr = np.zeros(steps, dtype=float)
    E_phi_arr = np.zeros(steps, dtype=float)
    E_chi_arr = np.zeros(steps, dtype=float)
    V_coup_arr = np.zeros(steps, dtype=float)

    # Initial half-step for momenta
    lap_phi = laplacian_1d(phi)
    lap_chi = laplacian_1d(chi)
    pi_phi += 0.5 * dt * (lap_phi - m1**2 * phi - g * chi)
    pi_chi += 0.5 * dt * (lap_chi - m2**2 * chi - g * phi)

    for n in range(steps):
        # Optional constraint
        if use_constraint:
            apply_combined_constraint(phi, chi, epsilon)

        # Full step for fields
        phi += dt * pi_phi
        chi += dt * pi_chi

        # Full step for momenta
        lap_phi = laplacian_1d(phi)
        lap_chi = laplacian_1d(chi)
        pi_phi += dt * (lap_phi - m1**2 * phi - g * chi)
        pi_chi += dt * (lap_chi - m2**2 * chi - g * phi)

        # Record observables
        mean_phi_arr[n] = phi.mean()
        mean_chi_arr[n] = chi.mean()
        E_total, E_phi, E_chi, V_coup = compute_energies(phi, chi, pi_phi, pi_chi, m1, m2, g)
        E_total_arr[n] = E_total
        E_phi_arr[n] = E_phi
        E_chi_arr[n] = E_chi
        V_coup_arr[n] = V_coup

    return t_arr, mean_phi_arr, mean_chi_arr, E_total_arr, E_phi_arr, E_chi_arr, V_coup_arr


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
    chi_amp = args.chi_amplitude

    print("=== 1D two-field coupling run ===")
    print(f"N = {N}, dt = {dt}, steps = {steps}")
    print(f"m1 = {m1}, m2 = {m2}, g = {g}, epsilon = {epsilon}")
    print(f"phi_amp = {phi_amp}, chi_amp = {chi_amp}")

    print("\nRunning free (no constraint) evolution...")
    t_free, mphi_free, mchi_free, E_free, Ephi_free, Echi_free, Vc_free = (
        evolve_two_field_system(
            N=N,
            dt=dt,
            steps=steps,
            m1=m1,
            m2=m2,
            g=g,
            epsilon=epsilon,
            phi_amp=phi_amp,
            chi_amp=chi_amp,
            use_constraint=False,
        )
    )

    print("Running constrained evolution (with non-cancelling rule)...")
    t_con, mphi_con, mchi_con, E_con, Ephi_con, Echi_con, Vc_con = (
        evolve_two_field_system(
            N=N,
            dt=dt,
            steps=steps,
            m1=m1,
            m2=m2,
            g=g,
            epsilon=epsilon,
            phi_amp=phi_amp,
            chi_amp=chi_amp,
            use_constraint=True,
        )
    )

    if not np.allclose(t_free, t_con):
        raise RuntimeError("Time arrays do not match between free and constrained runs.")

    out_dir = Path("data") / "processed"
    os.makedirs(out_dir, exist_ok=True)
    out_path = out_dir / "two_field_coupling_1d.npz"

    params = dict(
        N=N,
        dt=dt,
        steps=steps,
        m1=m1,
        m2=m2,
        g=g,
        epsilon=epsilon,
        phi_amp=phi_amp,
        chi_amp=chi_amp,
        description="1D two-field lattice with coupling and optional "
                    "non-cancelling constraint on combined mean.",
    )

    np.savez(
        out_path,
        t=t_free,
        mean_phi_free=mphi_free,
        mean_chi_free=mchi_free,
        mean_phi_constrained=mphi_con,
        mean_chi_constrained=mchi_con,
        E_total_free=E_free,
        E_phi_free=Ephi_free,
        E_chi_free=Echi_free,
        V_coup_free=Vc_free,
        E_total_constrained=E_con,
        E_phi_constrained=Ephi_con,
        E_chi_constrained=Echi_con,
        V_coup_constrained=Vc_con,
        params=params,
    )

    print(f"\nSaved two-field coupling data to {out_path}")


if __name__ == "__main__":
    main()
