import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def main():
    data_path = Path("data/processed/effective_vacuum_band_scan.npz")
    data = np.load(data_path)

    theta = data["theta_band"]
    omega = data["omega_lambda_band"]
    theta_fid = float(data["theta_fid"])
    omega_target = float(data["omega_lambda_target"])
    k_scale = float(data["k_scale"])

    print("Loaded:", data_path)
    print("  theta range          :", float(theta.min()), "->", float(theta.max()))
    print("  Omega_Lambda range   :", float(omega.min()), "->", float(omega.max()))
    print("  theta_fid            :", theta_fid)
    print("  omega_lambda_target  :", omega_target)
    print("  k_scale              :", k_scale)

    fig, ax = plt.subplots()

    ax.plot(theta, omega, label=r"$\Omega_\Lambda(\theta_\star)$")
    ax.axhline(omega_target, linestyle="--", linewidth=1,
               label=rf"target $\Omega_\Lambda = {omega_target:.2f}$")

    ax.set_xlabel(r"$\theta_\star\ \mathrm{[rad]}$")
    ax.set_ylabel(r"$\Omega_\Lambda(\theta_\star)$")
    ax.set_xlim(theta.min(), theta.max())
    ax.legend(loc="best")

    fig_dir = Path("figures")
    fig_dir.mkdir(exist_ok=True)

    for ext in ("png", "pdf"):
        out = fig_dir / f"effective_vacuum_band_scan.{ext}"
        fig.savefig(out, bbox_inches="tight")
        print("  wrote", out)

    plt.close(fig)

if __name__ == "__main__":
    main()