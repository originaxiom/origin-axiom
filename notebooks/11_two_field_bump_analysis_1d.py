"""
File: notebooks/11_two_field_bump_analysis_1d.py
Purpose: Analyse the 1D two-field localized bump evolution with and without
  the non-cancelling constraint. Compares localization vs time and how the
  bump splits between phi and chi.
Axiom link: Checks whether two-field interactions plus the global rule lead
  to any enhanced localization compared to the single-field case.
Inputs:
  - data/processed/two_field_bump_1d.npz
Outputs:
  - data/processed/two_field_bump_localization.png
  - data/processed/two_field_bump_profiles.png
"""

import numpy as np
import matplotlib.pyplot as plt


def main():
    data_path = "data/processed/two_field_bump_1d.npz"
    print(f"Loading two-field bump data from {data_path}")
    d = np.load(data_path, allow_pickle=True)

    t_snap = d["t_snap"]
    loc_free = d["loc_free"]
    loc_con = d["loc_constrained"]

    pt_free = d["profile_times_free"]
    phi_free = d["profiles_phi_free"]
    chi_free = d["profiles_chi_free"]

    pt_con = d["profile_times_constrained"]
    phi_con = d["profiles_phi_constrained"]
    chi_con = d["profiles_chi_constrained"]

    params = d["params"].item() if isinstance(d["params"], np.ndarray) else d["params"]

    N = params["N"]
    phi_amp = params["phi_amp"]
    phi_width = params["phi_width"]
    g = params["g"]
    epsilon = params["epsilon"]

    print("Run parameters:")
    for k, v in params.items():
        print(f"  {k}: {v}")

    # Localization vs time
    out_loc = "data/processed/two_field_bump_localization.png"
    fig, ax = plt.subplots()
    ax.plot(t_snap, loc_free, label="free")
    ax.plot(t_snap, loc_con, label="constrained")
    ax.set_xlabel("t")
    ax.set_ylabel("localization fraction")
    ax.set_title("Two-field localized bump: localization vs time")
    ax.legend()
    fig.tight_layout()
    fig.savefig(out_loc)
    plt.close(fig)
    print(f"Saved localization plot: {out_loc}")

    # Profiles plot: overlay phi and chi for a few times, free vs constrained
    out_prof = "data/processed/two_field_bump_profiles.png"
    fig, axes = plt.subplots(2, phi_free.shape[0], figsize=(4 * phi_free.shape[0], 6))
    x = np.arange(N)

    for j in range(phi_free.shape[0]):
        # free
        ax0 = axes[0, j]
        ax0.plot(x, phi_free[j], label="phi")
        ax0.plot(x, chi_free[j], label="chi")
        ax0.set_title(f"free t={pt_free[j]:.1f}")
        ax0.set_xlabel("site")
        ax0.set_ylabel("field")
        if j == 0:
            ax0.legend()

        # constrained
        ax1 = axes[1, j]
        ax1.plot(x, phi_con[j], label="phi")
        ax1.plot(x, chi_con[j], label="chi")
        ax1.set_title(f"constrained t={pt_con[j]:.1f}")
        ax1.set_xlabel("site")
        ax1.set_ylabel("field")
        if j == 0:
            ax1.legend()

    fig.suptitle(
        f"Two-field localized bump (phi_amp={phi_amp}, width={phi_width}, g={g}, epsilon={epsilon})"
    )
    fig.tight_layout()
    fig.savefig(out_prof)
    plt.close(fig)
    print(f"Saved profiles plot: {out_prof}")


if __name__ == "__main__":
    main()
