#!/usr/bin/env python3
"""
R6: Plot residence-time statistics for the theta_star random-walk ensemble.

Input:
  data/processed/theta_star_random_walk_residence.npz

Output:
  figures/theta_star_random_walk_residence.png
  figures/theta_star_random_walk_residence.pdf
"""

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt


DATA_PATH = Path("data/processed/theta_star_random_walk_residence.npz")
FIG_DIR = Path("figures")


def load_residence(path: Path):
    d = np.load(path)

    theta_traj = d["theta_traj"]      # shape (N_traj, N_steps+1)
    omega_traj = d["omega_traj"]      # shape (N_traj, N_steps+1)
    theta_min = float(d["theta_min"])
    theta_max = float(d["theta_max"])
    omega_target = float(d["omega_target"])
    tol_list = np.array(d["tol_list"], dtype=float)
    k_scale = float(d["k_scale"])
    theta_fid = float(d["theta_fid"])

    n_traj, n_steps_plus1 = omega_traj.shape
    return (
        theta_traj,
        omega_traj,
        theta_min,
        theta_max,
        omega_target,
        tol_list,
        k_scale,
        theta_fid,
        n_traj,
        n_steps_plus1,
    )


def main():
    (
        theta_traj,
        omega_traj,
        theta_min,
        theta_max,
        omega_target,
        tol_list,
        k_scale,
        theta_fid,
        n_traj,
        n_steps_plus1,
    ) = load_residence(DATA_PATH)

    omega_flat = omega_traj.ravel()
    Ntot = omega_flat.size

    print("Loaded:", DATA_PATH)
    print("  shape(theta_traj) =", theta_traj.shape)
    print("  shape(omega_traj) =", omega_traj.shape)
    print("  theta range [rad]: {:.3f} -> {:.3f}".format(theta_min, theta_max))
    print("  Omega_Lambda min/max: {:.3f} -> {:.3f}".format(omega_flat.min(), omega_flat.max()))
    print("  theta_fid:", theta_fid)
    print("  k_scale:", k_scale)
    print("  target ΩΛ:", omega_target)
    print("  tol_list:", tol_list)

    for tol in tol_list:
        in_win = np.abs(omega_flat - omega_target) <= tol
        n_in = int(in_win.sum())
        frac = 100.0 * n_in / Ntot
        print(
            "Window |ΩΛ - {:.3f}| ≤ {:.3f}: {:6d} / {:6d} ({:4.1f}%)".format(
                omega_target, tol, n_in, Ntot, frac
            )
        )

    FIG_DIR.mkdir(exist_ok=True)

    fig, ax = plt.subplots(figsize=(6, 4))

    ax.hist(
        omega_flat,
        bins=40,
        density=True,
        alpha=0.7,
    )

    # Highlight the broadest tolerance band (typically 0.05)
    tol0 = float(tol_list[0])
    ax.axvline(omega_target, linestyle="--", linewidth=1.5)
    ax.axvspan(
        omega_target - tol0,
        omega_target + tol0,
        alpha=0.2,
    )

    ax.set_xlabel(r"$\Omega_\Lambda$")
    ax.set_ylabel("Residence time density")
    ax.set_title(r"Random-walk residence of $\theta_\star$ in $\Omega_\Lambda$ space")

    for ext in ("png", "pdf"):
        out = FIG_DIR / f"theta_star_random_walk_residence.{ext}"
        fig.savefig(out, bbox_inches="tight")
        print("  wrote", out)

    plt.close(fig)


if __name__ == "__main__":
    main()