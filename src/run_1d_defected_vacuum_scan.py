"""
Scan vacuum energy E0(θ*) for a 1D defected scalar chain.

This complements the uniform-ring scan in run_1d_twisted_vacuum_scan.py.
Here we break translation invariance with a single defect bond, making the
global twist θ* physically nontrivial.
"""

import numpy as np
from pathlib import Path

from toy_universe_1d.defected_chain import defected_vacuum_energy


def main():
    N = 256
    c = 1.0
    m0 = 0.1
    defect_strength = 0.5  # weaker bond on the twisted edge

    n_theta = 181
    theta_list = np.linspace(0.0, 2.0 * np.pi, n_theta)

    E0_list = np.zeros_like(theta_list)

    for i, th in enumerate(theta_list):
        E0 = defected_vacuum_energy(
            N,
            c,
            m0,
            th,
            defect_strength=defect_strength,
        )
        E0_list[i] = E0
        if i % 30 == 0 or i == n_theta - 1:
            print(f"θ* = {th:.3f} rad, E0(θ*) = {E0:.6e}")

    E0_ref = float(E0_list[0])
    print(
        "\nReference vacuum energy:\n"
        f"  E0(θ*=0) = {E0_ref:.6e}"
    )

    out_dir = Path("data/processed")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "defected_1d_vacuum_scan.npz"

    np.savez(
        out_path,
        theta_list=theta_list,
        E0_list=E0_list,
        params=dict(
            N=N,
            c=c,
            m0=m0,
            defect_strength=defect_strength,
            n_theta=n_theta,
            E0_ref=E0_ref,
        ),
    )

    print(
        f"Saved defected 1D vacuum scan to {out_path}\n"
        f"E0(θ*=0) = {E0_ref:.6e}"
    )


if __name__ == "__main__":
    main()
