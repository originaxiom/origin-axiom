from __future__ import annotations

from pathlib import Path

import numpy as np

from two_field_lattice import TwoFieldParams, TwoFieldToyUniverse


def main() -> None:
    base = Path("data/processed")
    base.mkdir(parents=True, exist_ok=True)

    # --- Define parameters for this experiment ---
    params = TwoFieldParams(
        nx=16,
        ny=16,
        nz=16,
        c=1.0,
        m_phi=0.1,
        m_chi=0.1,
        lam_phi=1.0,
        lam_chi=1.0,
        g=0.0,         # set >0 later if you want explicit cross-coupling
        dt=0.005,
        n_steps=500,
        epsilon=0.05,
        A_ref=0.0,
        seed=42,
        mean_subtracted=True,
    )

    # Shared initial conditions for both runs
    rng = np.random.default_rng(params.seed)
    shape = (params.nx, params.ny, params.nz)

    phi0 = 1e-3 * (rng.standard_normal(shape) + 1j * rng.standard_normal(shape))
    chi0 = 1e-3 * (rng.standard_normal(shape) + 1j * rng.standard_normal(shape))

    # Run both cases
    run_case(params, phi0, chi0, use_constraint=False, label="no_constraint", out_dir=base)
    run_case(params, phi0, chi0, use_constraint=True, label="with_constraint", out_dir=base)


def run_case(
    params: TwoFieldParams,
    phi0: np.ndarray,
    chi0: np.ndarray,
    use_constraint: bool,
    label: str,
    out_dir: Path,
) -> None:
    """
    Run one two-field simulation with or without the Origin Axiom constraint.
    """
    uni = TwoFieldToyUniverse(params, use_constraint=use_constraint)
    uni.set_initial_conditions(phi0, chi0)

    n_steps = params.n_steps
    dt = params.dt

    t_list = []
    A_phi_list = []
    A_chi_list = []
    A_psi_list = []
    E_list = []

    print(f"=== Two-field run: {label} ===")
    print(
        f"N={params.nx}, lam_phi={params.lam_phi}, lam_chi={params.lam_chi}, "
        f"g={params.g}, eps={params.epsilon}, dt={dt}, n_steps={n_steps}"
    )

    for step in range(n_steps + 1):
        # Record diagnostics BEFORE the step (t = step * dt)
        t_list.append(uni.t)
        A_phi_list.append(uni.global_amplitude_phi())
        A_chi_list.append(uni.global_amplitude_chi())
        A_psi_list.append(uni.global_amplitude_psi())
        E_list.append(uni.total_energy())

        if step % 50 == 0:
            print(
                f"[{label}] step {step:4d}: t = {uni.t:6.3f}, "
                f"|A_psi| = {abs(A_psi_list[-1]):.6e}, "
                f"E = {E_list[-1]:.6e}, "
                f"hits_psi = {uni.constraint_hits_psi}"
            )

        if step < n_steps:
            uni.step()

    t_arr = np.array(t_list)
    A_phi = np.array(A_phi_list)
    A_chi = np.array(A_chi_list)
    A_psi = np.array(A_psi_list)
    E = np.array(E_list)

    eps = params.epsilon
    fname = f"two_field_compare_{label}_eps{eps:0.3f}.npz"
    out_path = out_dir / fname

    np.savez(
        out_path,
        t=t_arr,
        A_phi=A_phi,
        A_chi=A_chi,
        A_psi=A_psi,
        E=E,
        constraint_hits_psi=uni.constraint_hits_psi,
        params=params.__dict__,
        epsilon=params.epsilon,
        lam_phi=params.lam_phi,
        lam_chi=params.lam_chi,
        g=params.g,
    )

    print(f"Saved {label} run to {out_path}")
    print(f"Total psi-constraint hits: {uni.constraint_hits_psi}")


if __name__ == "__main__":
    main()
