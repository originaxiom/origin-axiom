import numpy as np
from toy_universe_lattice import ScalarToyUniverse
from toy_universe_lattice.origin_axiom_constraint import hard_constraint_factory
from pathlib import Path

def main():
    # Lattice + model parameters
    nx = ny = nz = 16
    c = 1.0
    m = 0.1
    lam = 0.0
    dt = 0.01
    n_steps = 500

    # Origin Axiom constraint parameters
    theta_star = np.pi  # just a test value for now
    epsilon = 1e-2
    A_ref = 0.0         # forbid global cancellation A ≈ 0

    constraint = hard_constraint_factory(theta_star, epsilon, A_ref=A_ref)

    # Initialize universe
    uni = ScalarToyUniverse(nx=nx, ny=ny, nz=nz, c=c, m=m, lam=lam, dt=dt)

    rng = np.random.default_rng(42)
    phi0 = 1e-3 * (rng.standard_normal(uni.lat.shape) + 1j * rng.standard_normal(uni.lat.shape))
    uni.set_initial_conditions(phi0)

    # Storage for diagnostics
    times = np.zeros(n_steps + 1)
    A_mod = np.zeros(n_steps + 1)
    energies = np.zeros(n_steps + 1)

    # Initial state
    t = 0.0
    times[0] = t
    A_mod[0] = np.abs(uni.global_amplitude())
    energies[0] = uni.energy()

    print(f"Step    0: t = {t:.3f}, |A| = {A_mod[0]:.5e}, E = {energies[0]:.5e}")

    # Time evolution
    for i in range(1, n_steps + 1):
        uni.step(constraint=constraint)
        t = i * dt
        times[i] = t
        A_mod[i] = np.abs(uni.global_amplitude())
        energies[i] = uni.energy()

        if i % 50 == 0:
            print(f"Step {i:4d}: t = {t:.3f}, |A| = {A_mod[i]:.5e}, E = {energies[i]:.5e}")

    # Save diagnostics
    out_dir = Path("data/processed")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "toy_v0_1_theta_pi_constraint.npz"

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
        ),
    )

    print(f"Saved diagnostics to {out_path}")

if __name__ == "__main__":
    main()
