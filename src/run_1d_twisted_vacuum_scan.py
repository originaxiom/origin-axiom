import numpy as np
from pathlib import Path
from toy_universe_1d import vacuum_energy_1d

def main():
    # 1D lattice parameters
    N = 256     # number of sites (large enough to approximate continuum a bit)
    c = 1.0
    m0 = 0.1    # small but nonzero mass

    # Scan θ* across [0, 2π]
    n_theta = 181
    theta_list = np.linspace(0.0, 2.0 * np.pi, n_theta)

    E0 = np.zeros_like(theta_list)
    for i, th in enumerate(theta_list):
        E0[i] = vacuum_energy_1d(N, c, m0, th)
        if i % 30 == 0:
            print(f"θ* = {th:.3f} rad, E0(θ*) = {E0[i]:.6e}")

    # Subtract θ* = 0 baseline to highlight twist effect
    E0_0 = E0[0]
    deltaE = E0 - E0_0

    out_dir = Path("data/processed")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "twisted_1d_vacuum_scan.npz"

    np.savez(
        out_path,
        theta_list=theta_list,
        E0=E0,
        deltaE=deltaE,
        params=dict(
            N=int(N),
            c=float(c),
            m0=float(m0),
            n_theta=int(n_theta),
            E0_ref=float(E0_0),
        ),
    )

    print(f"\nSaved 1D twisted vacuum scan to {out_path}")
    print(f"E0(θ*=0) = {E0_0:.6e}")

if __name__ == "__main__":
    main()
