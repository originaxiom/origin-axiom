"""
Analysis and plots for the 1D defected twisted scalar model.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


def main():
    base = Path("data/processed")
    path = base / "defected_1d_vacuum_scan.npz"
    if not path.exists():
        raise FileNotFoundError(
            f"{path} not found. Run src/run_1d_defected_vacuum_scan.py first."
        )

    npz = np.load(path, allow_pickle=True)
    theta_list = npz["theta_list"]
    E0_list = npz["E0_list"]
    params = npz["params"].item()

    E0_ref = params.get("E0_ref", float(E0_list[0]))
    deltaE = E0_list - E0_ref

    print("Loaded defected 1D twisted vacuum scan with params:")
    for k, v in params.items():
        print(f"  {k}: {v}")
    print(f"  min(E0) = {E0_list.min():.6e}")
    print(f"  max(E0) = {E0_list.max():.6e}")

    base.mkdir(parents=True, exist_ok=True)

    # Plot absolute E0(θ*)
    plt.figure()
    plt.plot(theta_list, E0_list)
    plt.xlabel(r"$\theta_\ast$")
    plt.ylabel(r"$E_0(\theta_\ast)$")
    plt.title("1D defected scalar: vacuum energy vs twist")
    plt.grid(True)
    plt.tight_layout()
    out_abs = base / "defected_1d_E0_vs_theta.png"
    plt.savefig(out_abs)

    # Plot deltaE(θ*) = E0(θ*) - E0(0)
    plt.figure()
    plt.plot(theta_list, deltaE)
    plt.axhline(0.0, linestyle="--")
    plt.xlabel(r"$\theta_\ast$")
    plt.ylabel(r"$\Delta E_0(\theta_\ast)$")
    plt.title("1D defected scalar: vacuum energy shift vs twist")
    plt.grid(True)
    plt.tight_layout()
    out_delta = base / "defected_1d_deltaE_vs_theta.png"
    plt.savefig(out_delta)

    print("Saved plots:")
    print(f"  {out_abs}")
    print(f"  {out_delta}")


if __name__ == "__main__":
    main()
