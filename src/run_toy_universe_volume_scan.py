#!/usr/bin/env python3
"""
run_toy_universe_volume_scan.py

Goal:
    For a few lattice sizes N, compare the time-averaged energy density
    with and without the Origin Axiom constraint, and see how the
    difference Δρ depends on volume.

Output:
    For each (N, lambda, epsilon) we write a single .npz file under
    data/processed/, containing:
        - t : time array
        - A_no,  E_no,  rho_no  (no constraint)
        - A_with, E_with, rho_with (with constraint)
        - meta: dict of parameters and summary statistics (JSON string)
"""

import json
from pathlib import Path

import numpy as np

from toy_universe_lattice import ScalarToyUniverse


def run_single_case(
    N: int,
    lam: float,
    epsilon: float,
    n_steps: int = 500,
    dt: float = 0.005,
    m: float = 0.1,
    c: float = 1.0,
    a: float = 1.0,
    theta_star: float = np.pi,  # bookkeeping only
    seed: int = 42,
) -> dict:
    """
    Run a pair of simulations (no constraint, with constraint) for a given
    lattice size N and parameters (lam, epsilon), and return all data
    in a dictionary ready to save.

    We use mean-subtracted small random initial conditions so that the
    unconstrained run naturally explores near A ≈ 0, while the constrained
    run is forced to respect |A| >= epsilon.
    """
    rng = np.random.default_rng(seed)

    # --- helper: set up initial field ---
    def make_initial_field(nx, ny, nz):
        phi0 = 1e-3 * (
            rng.standard_normal((nx, ny, nz)) +
            1j * rng.standard_normal((nx, ny, nz))
        )
        # mean-subtract to start near A ≈ 0
        phi0 -= phi0.mean()
        return phi0

    volume = (N * a) ** 3
    t_arr = np.arange(n_steps + 1) * dt

    # --- run without constraint ---
    uni_no = ScalarToyUniverse(
        nx=N,
        ny=N,
        nz=N,
        c=c,
        m=m,
        lam=lam,
        dt=dt,
    )
    # explicitly disable Origin Axiom constraint if available
    if hasattr(uni_no, "set_origin_axiom_constraint"):
        uni_no.set_origin_axiom_constraint(
            theta_star=theta_star,
            epsilon=epsilon,
            A_ref=0.0,
            use_constraint=False,
        )

    phi0 = make_initial_field(N, N, N)
    uni_no.set_initial_conditions(phi0)

    A_no = []
    E_no = []

    for step in range(n_steps + 1):
        A_no.append(uni_no.global_amplitude())
        E_no.append(uni_no.energy())
        if step < n_steps:
            uni_no.step()

    A_no = np.array(A_no)
    E_no = np.array(E_no)
    rho_no = E_no / volume
    hits_no = getattr(uni_no, "constraint_hits", 0)

    # --- run with constraint ---
    uni_with = ScalarToyUniverse(
        nx=N,
        ny=N,
        nz=N,
        c=c,
        m=m,
        lam=lam,
        dt=dt,
    )
    if hasattr(uni_with, "set_origin_axiom_constraint"):
        uni_with.set_origin_axiom_constraint(
            theta_star=theta_star,
            epsilon=epsilon,
            A_ref=0.0,
            use_constraint=True,
        )

    phi0 = make_initial_field(N, N, N)
    uni_with.set_initial_conditions(phi0)

    A_with = []
    E_with = []

    for step in range(n_steps + 1):
        A_with.append(uni_with.global_amplitude())
        E_with.append(uni_with.energy())
        if step < n_steps:
            uni_with.step()

    A_with = np.array(A_with)
    E_with = np.array(E_with)
    rho_with = E_with / volume
    hits_with = getattr(uni_with, "constraint_hits", 0)

    # --- summaries ---
    rho_no_mean = float(rho_no.mean())
    rho_with_mean = float(rho_with.mean())
    delta_rho = rho_with_mean - rho_no_mean

    meta = {
        "N": N,
        "a": a,
        "volume": volume,
        "lam": lam,
        "epsilon": epsilon,
        "m": m,
        "c": c,
        "dt": dt,
        "n_steps": n_steps,
        "theta_star": theta_star,
        "seed": seed,
        "rho_no_mean": rho_no_mean,
        "rho_with_mean": rho_with_mean,
        "delta_rho": delta_rho,
        "constraint_hits_no": int(hits_no),
        "constraint_hits_with": int(hits_with),
    }

    return {
        "t": t_arr,
        "A_no": A_no,
        "E_no": E_no,
        "rho_no": rho_no,
        "A_with": A_with,
        "E_with": E_with,
        "rho_with": rho_with,
        "meta_json": json.dumps(meta),
    }


def main():
    base = Path("data/processed")
    base.mkdir(parents=True, exist_ok=True)

    # Lattice sizes and parameters to scan.
    N_list = [16, 24, 32]
    lam_list = [0.0, 1.0]
    epsilon = 0.05

    for lam in lam_list:
        for N in N_list:
            print(
                f"=== Volume scan: N = {N}, lambda = {lam:.2f}, "
                f"epsilon = {epsilon:.3f} ==="
            )
            out = run_single_case(N=N, lam=lam, epsilon=epsilon)

            fname = base / f"volume_scan_N{N}_lam{lam:.2f}_eps{epsilon:.3f}.npz"
            np.savez_compressed(fname, **out)

            meta = json.loads(out["meta_json"])
            print(
                "Summary:"
                f"  delta_rho = {meta['delta_rho']:.6e},"
                f"  rho_no = {meta['rho_no_mean']:.6e},"
                f"  rho_with = {meta['rho_with_mean']:.6e},"
                f"  hits_with = {meta['constraint_hits_with']}"
            )
            print(f"Saved: {fname}")
            print()

    print("Volume scan completed.")


if __name__ == "__main__":
    main()
