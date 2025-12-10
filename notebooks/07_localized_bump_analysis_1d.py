"""
File: notebooks/07_localized_bump_analysis_1d.py
Purpose: Analyse the 1D localized bump evolution with and without the
  non-cancelling constraint. Measures how localized the bump remains over
  time and compares free vs constrained runs.
Axiom link: Probes whether the non-cancelling rule helps or hinders the
  stability of localized structures (proto-particles) in a simple 1D model.
Inputs:
  - data/processed/localized_bump_1d.npz
Outputs:
  - data/processed/localized_bump_profiles.png
  - data/processed/localized_bump_localization.png
"""

import numpy as np
import matplotlib.pyplot as plt


def compute_localization_measure(phi, center, window_radius):
    """
    Simple localization measure: fraction of |phi|^2 contained in a window
    around 'center' versus the total.
    """
    N = phi.size
    indices = np.arange(N)
    # Distance on periodic lattice
    dist = np.minimum(np.abs(indices - center), N - np.abs(indices - center))
    mask = dist <= window_radius

    total = np.sum(phi ** 2)
    if total <= 0.0:
        return 0.0

    local = np.sum((phi[mask]) ** 2)
    return float(local / total)


def main():
    data_path = "data/processed/localized_bump_1d.npz"
    print(f"Loading localized bump data from {data_path}")
    d = np.load(data_path, allow_pickle=True)

    t_snap = d["t_snap"]
    snaps_free = d["snaps_free"]
    snaps_constrained = d["snaps_constrained"]
    params = d["params"].item() if isinstance(d["params"], np.ndarray) else d["params"]

    N = params["N"]
    dt = params["dt"]
    steps = params["steps"]
    amplitude = params["amplitude"]
    width = params["width"]
    epsilon = params["epsilon"]
    snapshot_stride = params["snapshot_stride"]

    print("Run parameters:")
    for k, v in params.items():
        print(f"  {k}: {v}")

    # Center of initial bump
    center = int(N // 2)
    window_radius = int(width * 1.5)

    # Compute localization measures over time
    loc_free = []
    loc_con = []
    for phi_f, phi_c in zip(snaps_free, snaps_constrained):
        loc_free.append(compute_localization_measure(phi_f, center, window_radius))
        loc_con.append(compute_localization_measure(phi_c, center, window_radius))

    loc_free = np.array(loc_free)
    loc_con = np.array(loc_con)

    # Plot field profiles at a few snapshot times
    out_profiles = "data/processed/localized_bump_profiles.png"
    fig, ax = plt.subplots()
    x = np.arange(N)

    # pick up to 4 snapshots (start, early, mid, late)
    num_snaps = len(t_snap)
    indices = [0, min(num_snaps // 4, num_snaps - 1),
               min(num_snaps // 2, num_snaps - 1),
               num_snaps - 1]
    indices = sorted(set(indices))

    for idx in indices:
        ax.plot(x, snaps_free[idx], "--", alpha=0.7,
                label=f"free t={t_snap[idx]:.1f}" if idx == indices[0] else None)
        ax.plot(x, snaps_constrained[idx], alpha=0.7,
                label=f"constrained t={t_snap[idx]:.1f}" if idx == indices[0] else None)

    ax.set_xlabel("lattice site")
    ax.set_ylabel("phi")
    ax.set_title("Localized bump evolution (free vs constrained)")
    ax.legend()
    fig.tight_layout()
    fig.savefig(out_profiles)
    plt.close(fig)
    print(f"Saved profiles plot: {out_profiles}")

    # Plot localization measure over time
    out_loc = "data/processed/localized_bump_localization.png"
    fig, ax = plt.subplots()
    ax.plot(t_snap, loc_free, label="free")
    ax.plot(t_snap, loc_con, label="constrained")
    ax.set_xlabel("t")
    ax.set_ylabel("localization fraction")
    ax.set_title("Localization vs time (fraction of |phi|^2 in central window)")
    ax.legend()
    fig.tight_layout()
    fig.savefig(out_loc)
    plt.close(fig)
    print(f"Saved localization plot: {out_loc}")


if __name__ == "__main__":
    main()
