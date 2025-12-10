"""
File: notebooks/10_two_field_coupling_analysis_1d.py
Purpose: Analyse the 1D two-field coupling test. Compares mean fields and
  energy behaviour with and without the non-cancelling constraint.
Axiom link: Checks whether the constraint meaningfully alters energy exchange
  between two coupled sectors, as a proto-picture of "bound" structures.
Inputs:
  - data/processed/two_field_coupling_1d.npz
Outputs:
  - data/processed/two_field_coupling_means.png
  - data/processed/two_field_coupling_energy.png
"""

import numpy as np
import matplotlib.pyplot as plt


def main():
    data_path = "data/processed/two_field_coupling_1d.npz"
    print(f"Loading two-field coupling data from {data_path}")
    d = np.load(data_path, allow_pickle=True)

    t = d["t"]
    mphi_free = d["mean_phi_free"]
    mchi_free = d["mean_chi_free"]
    mphi_con = d["mean_phi_constrained"]
    mchi_con = d["mean_chi_constrained"]

    E_free = d["E_total_free"]
    E_con = d["E_total_constrained"]

    params = d["params"].item() if isinstance(d["params"], np.ndarray) else d["params"]

    print("Run parameters:")
    for k, v in params.items():
        print(f"  {k}: {v}")

    # Plot mean fields vs time
    out_means = "data/processed/two_field_coupling_means.png"
    fig, ax = plt.subplots()
    ax.plot(t, mphi_free, label="phi free")
    ax.plot(t, mchi_free, label="chi free")
    ax.plot(t, mphi_con, "--", label="phi constrained")
    ax.plot(t, mchi_con, "--", label="chi constrained")
    ax.set_xlabel("t")
    ax.set_ylabel("mean field")
    ax.set_title("Two-field coupling: mean fields vs time")
    ax.legend()
    fig.tight_layout()
    fig.savefig(out_means)
    plt.close(fig)
    print(f"Saved mean-fields plot: {out_means}")

    # Plot total energy vs time
    out_energy = "data/processed/two_field_coupling_energy.png"
    fig, ax = plt.subplots()
    ax.plot(t, E_free, label="E total free")
    ax.plot(t, E_con, label="E total constrained")
    ax.set_xlabel("t")
    ax.set_ylabel("E total")
    ax.set_title("Two-field coupling: total energy vs time")
    ax.legend()
    fig.tight_layout()
    fig.savefig(out_energy)
    plt.close(fig)
    print(f"Saved energy plot: {out_energy}")


if __name__ == "__main__":
    main()
