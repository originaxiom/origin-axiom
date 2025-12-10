"""
File: notebooks/09_localized_bump_scan_analysis_3d.py
Purpose: Analyse the 3D localized bump parameter scan. For each parameter
  combination, compares localization fractions over time for free and
  constrained runs and builds summary plots.
Axiom link: Identifies regions in (amplitude, width, lambda4, epsilon) space
  where the non-cancelling constraint appears to enhance or suppress the
  longevity of localized lumps.
Inputs:
  - data/processed/localized_bump_3d_scan.npz
Outputs:
  - data/processed/localized_bump_3d_scan_final_loc.png
  - data/processed/localized_bump_3d_scan_time_slice.png
"""

import numpy as np
import matplotlib.pyplot as plt


def main():
    data_path = "data/processed/localized_bump_3d_scan.npz"
    print(f"Loading 3D localized bump scan from {data_path}")
    d = np.load(data_path, allow_pickle=True)

    t_snap = d["t_snap"]
    loc_free = d["loc_free"]
    loc_con = d["loc_constrained"]
    params = d["params"].item() if isinstance(d["params"], np.ndarray) else d["params"]

    amplitudes = params["amplitudes"]
    widths = params["widths"]
    lambda4s = params["lambda4s"]
    epsilons = params["epsilons"]

    print("Scan parameter grids:")
    print(f"  amplitudes: {amplitudes}")
    print(f"  widths: {widths}")
    print(f"  lambda4s: {lambda4s}")
    print(f"  epsilons: {epsilons}")
    print(f"  number of time snapshots: {t_snap.size}")

    # For simplicity, we will fix lambda4 and epsilon indices and plot a 2D map
    # over (amplitude, width) of the localization at final time.
    il = 0  # first lambda4
    ie = 0  # first epsilon

    final_loc_free = loc_free[:, :, il, ie, -1]
    final_loc_con = loc_con[:, :, il, ie, -1]

    out_final = "data/processed/localized_bump_3d_scan_final_loc.png"
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    im0 = axes[0].imshow(
        final_loc_free,
        origin="lower",
        extent=[widths[0], widths[-1], amplitudes[0], amplitudes[-1]],
        aspect="auto",
    )
    axes[0].set_title("final localization (free)")
    axes[0].set_xlabel("width")
    axes[0].set_ylabel("amplitude")
    fig.colorbar(im0, ax=axes[0])

    im1 = axes[1].imshow(
        final_loc_con,
        origin="lower",
        extent=[widths[0], widths[-1], amplitudes[0], amplitudes[-1]],
        aspect="auto",
    )
    axes[1].set_title("final localization (constrained)")
    axes[1].set_xlabel("width")
    axes[1].set_ylabel("amplitude")
    fig.colorbar(im1, ax=axes[1])

    fig.suptitle(
        f"3D bump scan: final localization (lambda4={lambda4s[il]}, epsilon={epsilons[ie]})"
    )
    fig.tight_layout()
    fig.savefig(out_final)
    plt.close(fig)
    print(f"Saved final localization map: {out_final}")

    # Also plot localization vs time for a representative configuration
    ia = 0  # first amplitude
    iw = 0  # first width

    out_ts = "data/processed/localized_bump_3d_scan_time_slice.png"
    fig, ax = plt.subplots()
    ax.plot(t_snap, loc_free[ia, iw, il, ie, :], label="free")
    ax.plot(t_snap, loc_con[ia, iw, il, ie, :], label="constrained")
    ax.set_xlabel("t")
    ax.set_ylabel("localization fraction")
    ax.set_title(
        f"Localization vs time for a sample config\n"
        f"(A={amplitudes[ia]}, W={widths[iw]}, lambda4={lambda4s[il]}, epsilon={epsilons[ie]})"
    )
    ax.legend()
    fig.tight_layout()
    fig.savefig(out_ts)
    plt.close(fig)
    print(f"Saved time-slice plot: {out_ts}")


if __name__ == "__main__":
    main()
