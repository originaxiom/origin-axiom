import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def main():
    data_path = Path("data/processed/twisted_1d_vacuum_scan.npz")
    if not data_path.exists():
        raise FileNotFoundError(f"Data file not found: {data_path}")

    npz = np.load(data_path, allow_pickle=True)
    theta_list = npz["theta_list"]
    E0 = npz["E0"]
    deltaE = npz["deltaE"]
    params = npz["params"].item()

    print("Loaded 1D twisted vacuum scan with params:")
    for k, v in params.items():
        print(f"  {k}: {v}")

    # Plot absolute E0(θ*)
    plt.figure()
    plt.plot(theta_list, E0)
    plt.xlabel(r"$\theta_\ast$")
    plt.ylabel(r"$E_0(\theta_\ast)$")
    plt.title("1D twisted scalar: vacuum energy vs twist")
    plt.grid(True)
    plt.tight_layout()
    out_abs = Path("data/processed/twisted_1d_E0_vs_theta.png")
    plt.savefig(out_abs)

    # Plot deltaE(θ*) = E0(θ*) - E0(0)
    plt.figure()
    plt.plot(theta_list, deltaE)
    plt.axhline(0.0, linestyle="--")
    plt.xlabel(r"$\theta_\ast$")
    plt.ylabel(r"$\Delta E_0(\theta_\ast) = E_0(\theta_\ast) - E_0(0)$")
    plt.title("1D twisted scalar: vacuum energy shift vs twist")
    plt.grid(True)
    plt.tight_layout()
    out_delta = Path("data/processed/twisted_1d_deltaE_vs_theta.png")
    plt.savefig(out_delta)

    print("Saved plots:")
    print(f"  {out_abs}")
    print(f"  {out_delta}")

if __name__ == "__main__":
    main()
