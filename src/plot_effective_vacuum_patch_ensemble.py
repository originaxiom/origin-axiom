#!/usr/bin/env python3
"""
R5: Plot effective vacuum patch ensemble

Loads:
  data/processed/effective_vacuum_patch_ensemble.npz

and produces:
  figures/effective_vacuum_patch_ensemble.png
  figures/effective_vacuum_patch_ensemble.pdf
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


DATA_PATH = Path("data/processed/effective_vacuum_patch_ensemble.npz")
FIG_DIR = Path("figures")


def load_ensemble(path: Path):
    d = np.load(path)
    print("Loaded:", path)
    print("  keys:", d.files)

    # Our actual keys in this run:
    #   theta_samples, omega_samples, theta_min, theta_max,
    #   omega_target, tol, theta_fid, k_scale
    theta = d["theta_samples"]
    omega = d["omega_samples"]

    theta_min = float(d["theta_min"])
    theta_max = float(d["theta_max"])
    theta_band = np.array([theta_min, theta_max], dtype=float)

    omega_target = float(d["omega_target"])
    omega_tol = float(d["tol"])

    return theta, omega, theta_band, omega_target, omega_tol


def main():
    theta, omega, theta_band, omega_target, omega_tol = load_ensemble(DATA_PATH)

    print()
    print("Ensemble summary:")
    print("  theta range [rad]:", float(theta.min()), "->", float(theta.max()))
    print(
        "  Omega_Lambda range:",
        float(omega.min()),
        "->",
        float(omega.max()),
    )
    print(
        "  target Omega_Lambda:",
        omega_target,
        "+/-",
        omega_tol,
    )

    # Selection window
    mask = np.abs(omega - omega_target) <= omega_tol
    frac = mask.mean()
    print(f"  # patches in window: {mask.sum()} / {len(omega)} "
          f"({100.0 * frac:.1f}%)")

    FIG_DIR.mkdir(exist_ok=True)

    fig, ax = plt.subplots(figsize=(6, 4))

    # Histogram of Omega_Lambda across patches
    ax.hist(omega, bins=40, density=True, alpha=0.6, label="patch ensemble")

    # Highlight the target band
    ax.axvspan(
        omega_target - omega_tol,
        omega_target + omega_tol,
        alpha=0.2,
        label=r"$\Omega_\Lambda = 0.7 \pm 0.05$",
    )
    ax.axvline(omega_target, linestyle="--", label="target")

    ax.set_xlabel(r"$\Omega_\Lambda$")
    ax.set_ylabel("normalized count")
    ax.set_title("Effective vacuum patch ensemble")

    ax.legend()

    for ext in ("png", "pdf"):
        out = FIG_DIR / f"effective_vacuum_patch_ensemble.{ext}"
        fig.savefig(out, bbox_inches="tight")
        print("  wrote", out)

    plt.close(fig)


if __name__ == "__main__":
    main()