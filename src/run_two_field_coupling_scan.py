from __future__ import annotations

from pathlib import Path
from typing import Tuple

import numpy as np

from two_field_coupled_lattice import TwoFieldCoupledParams, TwoFieldCoupledUniverse


DATA_DIR = Path("data/processed")


def make_initial_fields(
    shape: Tuple[int, int, int],
    seed: int = 42,
    amp: float = 1e-3,
) -> Tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    phi0 = amp * (
        rng.standard_normal(shape) + 1j * rng.standard_normal(shape)
    )
    chi0 = amp * (
        rng.standard_normal(shape) + 1j * rng.standard_normal(shape)
    )
    return phi0, chi0


def run_single_case(g: float, use_constraint: bool, label: str) -> Path:
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    params = TwoFieldCoupledParams(
        nx=16,
        ny=16,
        nz=16,
        c=1.0,
        m_phi=0.1,
        m_chi=0.1,
        lam_phi=1.0,
        lam_chi=1.0,
        g=g,
        dt=0.005,
        n_steps=500,
        epsilon_psi=0.05,
        A_ref_psi=0.0 + 0.0j,
    )

    shape = (params.nx, params.ny, params.nz)
    phi0, chi0 = make_initial_fields(shape=shape, seed=1234)

    uni = TwoFieldCoupledUniverse(params, use_constraint=use_constraint)
    uni.set_initial_conditions(phi0, chi0, mean_subtract=True)

    t_list = []
    Apsi_list = []
    E_list = []

    print(
        f"=== g = {g:.2f}, use_constraint = {use_constraint} "
        f"({label}) ==="
    )

    # record t=0
    diag = uni.diagnostics()
    t_list.append(diag["t"])
    Apsi_list.append(diag["A_psi"])
    E_list.append(diag["E_total"])

    for _ in range(params.n_steps):
        uni.step()
        diag = uni.diagnostics()
        t_list.append(diag["t"])
        Apsi_list.append(diag["A_psi"])
        E_list.append(diag["E_total"])

    Apsi_arr = np.array(Apsi_list)
    E_arr = np.array(E_list)
    t_arr = np.array(t_list)

    hits = diag["constraint_hits"]

    fname = DATA_DIR / f"two_field_coupling_g{g:.2f}_{label}.npz"
    np.savez(
        fname,
        t=t_arr,
        Apsi=Apsi_arr,
        E=E_arr,
        g=g,
        params=params.__dict__,
        use_constraint=use_constraint,
        constraint_hits=hits,
    )

    print(
        f"Saved {fname} | "
        f"hits = {hits}, "
        f"<|A_psi|> = {np.mean(np.abs(Apsi_arr)):.3e}, "
        f"<E> = {np.mean(E_arr):.6e}"
    )

    return fname


def main() -> None:
    g_list = [0.0, 0.1, 0.5, 1.0]

    for g in g_list:
        # no constraint case
        run_single_case(g, use_constraint=False, label="no_constraint")
        # constrained ψ case
        run_single_case(g, use_constraint=True, label="with_constraint")

    print("Two-field coupling scan complete.")


if __name__ == "__main__":
    main()
