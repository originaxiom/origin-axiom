"""
File: notebooks/08_localized_bump_analysis_3d.py
Purpose: Analyse the 3D localized bump evolution with and without the
  non-cancelling constraint. Looks at central slices and a localization
  measure over time.
Axiom link: Probes whether the non-cancelling rule plus self-interaction
  can support more stable, localized 3D lumps (proto-oscillons).
Inputs:
  - data/processed/localized_bump_3d.npz
Outputs:
  - data/processed/localized_bump_3d_slices.png
  - data/processed/localized_bump_3d_localization.png
"""

import numpy as np
import matplotlib.pyplot as plt


def compute_localization_fraction(phi, center, radius):
    """
    Fraction of |phi|^2 contained in a sphere of given radius around center,
    on a periodic cubic lattice.
    """
    N = phi.shape[0]
    coords = np.arange(N)
    x, y, z = np.meshgrid(coords, coords, coords, indexing="ij")
    cx, cy, cz = center

    dx = np.minimum(np.abs(x - cx), N - np.abs(x - cx))
    dy = np.minimum(np.abs(y - cy), N - np.abs(y - cy))
    dz = np.minimum(np.abs(z - cz), N - np.abs(z - cz))
    r2 = dx**2 + dy**2 + dz**2

    mask = r2 <= radius**2

    total = np.sum(phi**2)
    if total <= 0.0:
        return 0.0
    local = np.sum((phi[mask])**2)
    return float(local / total)


def main():
    data_path = "data/processed/localized_bump_3d.npz"
    print(f"Loading 3D localized bump data from {data_path}")
    d = np.load(data_path, allow_pickle=True)

    t_snap = d["t_snap"]
    snaps_free = d["snaps_free"]
    snaps_constrained = d["snaps_constrained"]
    params = d["params"].item() if isinstance(d["params"], np.ndarray) else d["params"]

    N = params["N"]
    dt = params["dt"]
    steps = params["steps"]
    m0 = params["m0"]
    lambda4 = params["lambda4"]
    amplitude = params["amplitude"]
    width = params["width"]
    epsilon = params["epsilon"]
    snapshot_stride = params["snapshot_stride"]

    print("Run parameters:")
    for k, v in params.items():
        print(f"  {k}: {v}")

    center = (N // 2, N // 2, N // 2)
    radius = int(width * 1.5)

    # Compute localization fractions
    loc_free = []
    loc_con = []
    for phi_f, phi_c in zip(snaps_free, snaps_constrained):
        loc_free.append(compute_localization_fraction(phi_f, center, radius))
        loc_con.append(compute_localization_fraction(phi_c, center, radius))

    loc_free = np.array(loc_free)
    loc_con = np.array(loc_con)

    # Plot central slices at selected times (z = center plane)
    out_slices = "data/processed/localized_bump_3d_slices.png"
    zc = center[2]
    num_snaps = len(t_snap)
    indices = [0, min(num_snaps // 4, num_snaps - 1),
               min(num_snaps // 2, num_snaps - 1),
               num_snaps - 1]
    indices = sorted(set(indices))

    fig, axes = plt.subplots(2, len(indices), figsize=(4 * len(indices), 6))
    for j, idx in enumerate(indices):
        im0 = axes[0, j].imshow(snaps_free[idx][:, :, zc], origin="lower")
        axes[0, j].set_title(f"free t={t_snap[idx]:.1f}")
        axes[0, j].set_xticks([])
        axes[0, j].set_yticks([])
        fig.colorbar(im0, ax=axes[0, j], fraction=0.046, pad=0.04)

        im1 = axes[1, j].imshow(snaps_constrained[idx][:, :, zc], origin="lower")
        axes[1, j].set_title(f"constrained t={t_snap[idx]:.1f}")
        axes[1, j].set_xticks([])
        axes[1, j].set_yticks([])
        fig.colorbar(im1, ax=axes[1, j], fraction=0.046, pad=0.04)

    axes[0, 0].set_ylabel("y")
    axes[1, 0].set_ylabel("y")
    fig.suptitle("3D localized bump: central z-slices (free vs constrained)")
    fig.tight_layout()
    fig.savefig(out_slices)
    plt.close(fig)
    print(f"Saved slices plot: {out_slices}")

    # Plot localization vs time
    out_loc = "data/processed/localized_bump_3d_localization.png"
    fig, ax = plt.subplots()
    ax.plot(t_snap, loc_free, label="free")
    ax.plot(t_snap, loc_con, label="constrained")
    ax.set_xlabel("t")
    ax.set_ylabel("localization fraction")
    ax.set_title("3D localization vs time (fraction of |phi|^2 in central sphere)")
    ax.legend()
    fig.tight_layout()
    fig.savefig(out_loc)
    plt.close(fig)
    print(f"Saved localization plot: {out_loc}")


if __name__ == "__main__":
    main()
