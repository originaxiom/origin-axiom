"""
Compare 3D scalar toy universe with and without Origin Axiom constraint
in the presence of a nonlinear self-coupling (lambda != 0).

- Same random initial field for both runs, mean-subtracted so A(0) ~ 0.
- Nonlinear coupling lam = 1.0.
- epsilon = 0.05, theta_star = pi.
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
    seed: int = 42,
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
    with_constraint: bool,
    epsilon: float,
    n_steps: int = 500,
):
    """Run one universe (with or without the global Origin Axiom constraint)."""

    nx = ny = nz = 16
    c = 1.0
    m = 0.1
    lam = 1.0   # nonzero self-interaction
    dt = 0.005  # smaller dt for stability with lambda != 0

    uni = ScalarToyUniverse(nx=nx, ny=ny, nz=nz, c=c, m=m, lam=lam, dt=dt)

    phi0 = make_initial_field_mean_subtracted(nx, ny, nz, amplitude=1e-2, seed=42)
    uni.set_initial_conditions(phi0)

    theta_star = float(np.pi)
    A_ref = 0.0

    if with_constraint:
        uni.constraint_hits = 0
        constraint = hard_constraint_factory(theta_star=theta_star, epsilon=epsilon, A_ref=A_ref)
    else:
        uni.constraint_hits = 0
        constraint = None

    t_list = []
    A_list = []
    E_list = []

    for step in range(n_steps + 1):
        t = step * dt
        A = uni.global_amplitude()
        E = uni.energy()

        t_list.append(t)
        A_list.append(A)
        E_list.append(E)

        if step % 50 == 0:
            label = "with_constraint" if with_constraint else "no_constraint"
            hits_info = f", hits={uni.constraint_hits}" if with_constraint else ""
            print(
                f"[{label}] step {step:4d}: t = {t:5.3f}, "
                f"|A| = {abs(A):.6e}, E = {E:.6e}{hits_info}"
            )

        if step < n_steps:
            if constraint is None:
                uni.step()
            else:
                uni.step(constraint)

    result = dict(
        t=np.array(t_list),
        A=np.array(A_list),
        E=np.array(E_list),
        params=dict(
            nx=nx,
            ny=ny,
            nz=nz,
            c=c,
            m=m,
            lam=lam,
            dt=dt,
            n_steps=n_steps,
            theta_star=theta_star,
            epsilon=epsilon,
            A_ref=A_ref,
            seed=42,
            with_constraint=with_constraint,
            constraint_hits=getattr(uni, "constraint_hits", 0),
            mean_subtracted=True,
        ),
    )

    return result


def main():
    epsilon = 0.05
    n_steps = 500

    print("=== Nonlinear 3D toy universe: no constraint ===")
    res0 = run_single(with_constraint=False, epsilon=epsilon, n_steps=n_steps)

    print("\n=== Nonlinear 3D toy universe: with Origin Axiom constraint ===")
    res1 = run_single(with_constraint=True, epsilon=epsilon, n_steps=n_steps)

    out_dir = Path("data/processed")
    out_dir.mkdir(parents=True, exist_ok=True)

    path0 = out_dir / "toy_v0_1_nonlinear_no_constraint_epsilon005_meanzero.npz"
    path1 = out_dir / "toy_v0_1_nonlinear_with_constraint_epsilon005_meanzero.npz"

    np.savez(path0, **res0)
    np.savez(path1, **res1)

    print("Saved nonlinear comparison runs to:")
    print(f"  {path0}")
    print(f"  {path1}")


if __name__ == "__main__":
    main()
