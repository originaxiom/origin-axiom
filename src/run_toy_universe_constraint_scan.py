"""
Scan how the Origin Axiom constraint behaves for different (epsilon, lambda)
in the 3D scalar toy universe.

- 16^3 lattice, periodic.
- c = 1.0, m = 0.1.
- lambda in {0.0 (linear), 1.0 (nonlinear)}.
- epsilon in {0.01, 0.03, 0.05, 0.10}.
- Same mean-subtracted random initial field for all runs (fixed seed).

For each (lambda, epsilon) we record:
- constraint_hits
- mean and std of |A(t)|
- final |A(t_final)|
- mean and std of E(t)
"""

import numpy as np
from pathlib import Path

from toy_universe_lattice import ScalarToyUniverse
from toy_universe_lattice.origin_axiom_constraint import hard_constraint_factory


def make_initial_field_mean_subtracted(
    nx: int,
    ny: int,
    nz: int,
    amplitude: float = 1e-2,
    seed: int = 1234,
) -> np.ndarray:
    """Small random complex field with mean subtraction so A(0) ≈ 0."""
    rng = np.random.default_rng(seed)
    shape = (nx, ny, nz)
    phi = amplitude * (
        rng.standard_normal(shape) + 1j * rng.standard_normal(shape)
    )
    mean = np.mean(phi)
    phi -= mean
    return phi


def run_single(
    lam: float,
    epsilon: float,
    n_steps: int = 300,
) -> dict:
    """Run one universe with given lambda and epsilon, return summary stats."""

    nx = ny = nz = 16
    c = 1.0
    m = 0.1
    dt = 0.005  # safe for both linear and nonlinear

    uni = ScalarToyUniverse(nx=nx, ny=ny, nz=nz, c=c, m=m, lam=lam, dt=dt)

    phi0 = make_initial_field_mean_subtracted(nx, ny, nz, amplitude=1e-2, seed=1234)
    uni.set_initial_conditions(phi0)

    theta_star = float(np.pi)
    A_ref = 0.0

    uni.constraint_hits = 0
    constraint = hard_constraint_factory(theta_star=theta_star, epsilon=epsilon, A_ref=A_ref)

    A_abs_list = []
    E_list = []

    for step in range(n_steps + 1):
        A = uni.global_amplitude()
        E = uni.energy()

        A_abs_list.append(abs(A))
        E_list.append(E)

        if step % 50 == 0:
            print(
                f"[lam={lam:.2f}, eps={epsilon:.3f}] "
                f"step {step:4d}: |A| = {abs(A):.6e}, "
                f"E = {E:.6e}, hits={uni.constraint_hits}"
            )

        if step < n_steps:
            uni.step(constraint)

    A_abs_arr = np.asarray(A_abs_list)
    E_arr = np.asarray(E_list)

    summary = dict(
        lam=lam,
        epsilon=epsilon,
        n_steps=n_steps,
        A_abs_mean=float(A_abs_arr.mean()),
        A_abs_std=float(A_abs_arr.std()),
        A_abs_final=float(A_abs_arr[-1]),
        E_mean=float(E_arr.mean()),
        E_std=float(E_arr.std()),
        constraint_hits=int(getattr(uni, "constraint_hits", 0)),
        nx=nx,
        ny=ny,
        nz=nz,
        c=c,
        m=m,
        dt=dt,
        theta_star=theta_star,
        A_ref=A_ref,
        seed=1234,
    )

    return summary


def main():
    lam_list = [0.0, 1.0]
    eps_list = [0.01, 0.03, 0.05, 0.10]
    n_steps = 300

    results = []

    for lam in lam_list:
        for eps in eps_list:
            print("\n=== Running scan case: "
                  f"lambda = {lam:.2f}, epsilon = {eps:.3f} ===")
            summary = run_single(lam=lam, epsilon=eps, n_steps=n_steps)
            results.append(summary)
            print(
                "Summary: "
                f"hits = {summary['constraint_hits']}, "
                f"<|A|> = {summary['A_abs_mean']:.4e}, "
                f"final |A| = {summary['A_abs_final']:.4e}"
            )

    # Pack results into arrays/tables
    lam_vals = np.array([r["lam"] for r in results])
    eps_vals = np.array([r["epsilon"] for r in results])
    hits = np.array([r["constraint_hits"] for r in results])
    A_mean = np.array([r["A_abs_mean"] for r in results])
    A_final = np.array([r["A_abs_final"] for r in results])
    E_mean = np.array([r["E_mean"] for r in results])
    E_std = np.array([r["E_std"] for r in results])

    out_dir = Path("data/processed")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "constraint_scan_eps_lambda.npz"

    np.savez(
        out_path,
        lam_vals=lam_vals,
        eps_vals=eps_vals,
        hits=hits,
        A_mean=A_mean,
        A_final=A_final,
        E_mean=E_mean,
        E_std=E_std,
        meta=dict(
            lam_list=lam_list,
            eps_list=eps_list,
            n_steps=n_steps,
            nx=16,
            ny=16,
            nz=16,
            c=1.0,
            m=0.1,
            dt=0.005,
            seed=1234,
        ),
    )

    print("\nSaved constraint scan to", out_path)


if __name__ == "__main__":
    main()
