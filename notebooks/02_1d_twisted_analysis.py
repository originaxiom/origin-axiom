"""
File: notebooks/02_1d_twisted_analysis.py
Purpose: Analyse the 1D twisted vacuum scan (no defect) and produce
  E0(theta_star) vs theta_star plots.
Axiom link: Serves as a null test for exotic twist/phase dependence in the
  vacuum energy. Confirms that the twisted boundary condition alone does not
  induce nontrivial theta_star structure.
Inputs:
  - data/processed/twisted_1d_vacuum_scan.npz
Outputs:
  - data/processed/twisted_1d_E0_vs_theta.png
  - data/processed/twisted_1d_deltaE_vs_theta.png
"""

import numpy as np
import matplotlib.pyplot as plt

def main():
    data_path = "data/processed/twisted_1d_vacuum_scan.npz"
    print(f"Loading twisted 1D vacuum scan from {data_path}")
    d = np.load(data_path, allow_pickle=True)

    theta_list = d["theta_list"]
    E0 = d["E0"]
    deltaE = d["deltaE"]
    params = d["params"].item() if isinstance(d["params"], np.ndarray) else d["params"]

    print("Scan parameters:")
    for k, v in params.items():
        print(f"  {k}: {v}")

    print(f"  min(E0) = {E0.min():.6e}")
    print(f"  max(E0) = {E0.max():.6e}")

    # Plot E0(theta) vs theta
    out_png_E0 = "data/processed/twisted_1d_E0_vs_theta.png"
    fig, ax = plt.subplots()
    ax.plot(theta_list, E0)
    ax.set_xlabel("theta_*")
    ax.set_ylabel("E0(theta_*)")
    ax.set_title("1D twisted scalar: vacuum energy vs twist")
    fig.tight_layout()
    fig.savefig(out_png_E0)
    plt.close(fig)
    print(f"Saved plot: {out_png_E0}")

    # Plot deltaE(theta) vs theta
    out_png_dE = "data/processed/twisted_1d_deltaE_vs_theta.png"
    fig, ax = plt.subplots()
    ax.plot(theta_list, deltaE)
    ax.set_xlabel("theta_*")
    ax.set_ylabel("DeltaE(theta_*)")
    ax.set_title("1D twisted scalar: vacuum energy shift vs twist")
    fig.tight_layout()
    fig.savefig(out_png_dE)
    plt.close(fig)
    print(f"Saved plot: {out_png_dE}")

if __name__ == "__main__":
    main()
