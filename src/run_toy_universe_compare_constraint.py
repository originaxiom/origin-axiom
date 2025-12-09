import numpy as np
from pathlib import Path

from toy_universe_lattice import ScalarToyUniverse
from toy_universe_lattice.origin_axiom_constraint import hard_constraint_factory

def run_once(with_constraint: bool, seed: int = 42):
    # Lattice + model parameters
    nx = ny = nz = 16
    c = 1.0
    m = 0.1
    lam = 0.0
    dt = 0.01
    n_steps = 500

    # Constraint params: larger epsilon so the region is significant
    theta_star = np.pi
    epsilon = 5e-2   # 0.05
    A_ref = 0.0

    if with_constraint:
        constraint = hard_constraint_factory(theta_star, epsilon, A_ref=A_ref)
        label = "with_constraint"
    else:
        constraint = None
        label = "no_constraint"

    uni = ScalarToyUniverse(nx=nx, ny=ny, nz=nz, c=c, m=m, lam=lam, dt=dt)

    rng = np.random.default_rng(seed)
    phi0 = 1e-3 * (rng.standard_normal(uni.lat.shape) + 1j * rng.standard_normal(uni.lat.shape))

    # Subtract the mean so that A(0) ≈ 0 (strongly cancelling configuration)
    phi0 -= phi0.mean()
    uni.set_initial_conditions(phi0)

    # If we have a constraint, enforce it once at t=0 as well
    if constraint is not None:
        constraint(uni)

    times = np.zeros(n_steps + 1)
    A_mod = np.zeros(n_steps + 1)
    energies = np.zeros(n_steps + 1)

    t = 0.0
    times[0] = t
    A_mod[0] = np.abs(uni.global_amplitude())
    energies[0] = uni.energy()

    print(f"[{label}] step 0: t = {t:.3f}, |A| = {A_mod[0]:.5e}, E = {energies[0]:.5e}")

    for i in range(1, n_steps + 1):
        uni.step(constraint=constraint)
        t = i * dt
        times[i] = t
        A_mod[i] = np.abs(uni.global_amplitude())
        energies[i] = uni.energy()

        if i % 50 == 0:
            print(f"[{label}] step {i:4d}: t = {t:.3f}, |A| = {A_mod[i]:.5e}, E = {energies[i]:.5e}")

    print(f"[{label}] constraint hits: {uni.constraint_hits}")

    out_dir = Path("data/processed")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"toy_v0_1_{label}_epsilon005_meanzero.npz"

    np.savez(
        out_path,
        times=times,
        A_mod=A_mod,
        energies=energies,
        params=dict(
            nx=nx, ny=ny, nz=nz,
            c=c, m=m, lam=lam, dt=dt,
            n_steps=n_steps,
            theta_star=float(theta_star),
            epsilon=float(epsilon),
            A_ref=float(A_ref),
            seed=int(seed),
            with_constraint=with_constraint,
            constraint_hits=int(uni.constraint_hits),
            mean_subtracted=True,
        ),
    )

    print(f"[{label}] saved to {out_path}")

def main():
    # Same seed so we compare exactly the same initial condition
    run_once(with_constraint=False, seed=42)
    run_once(with_constraint=True, seed=42)

if __name__ == "__main__":
    main()
