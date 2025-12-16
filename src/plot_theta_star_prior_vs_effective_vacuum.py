#!/usr/bin/env python3
"""
R7: Plot theta_star prior mapped into Omega_Lambda via microcavity.

Reads:
  data/processed/theta_star_prior_vs_effective_vacuum.npz

Writes:
  figures/theta_star_prior_vs_effective_vacuum.(png|pdf)
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt


DATA_PATH = Path("data/processed/theta_star_prior_vs_effective_vacuum.npz")
FIG_DIR = Path("figures")


def main():
    d = np.load(DATA_PATH)

    theta = d["theta_prior"]
    omega = d["omega_prior"]
    theta_fid = float(d["theta_fid"])
    omega_target = float(d["omega_lambda_target"])

    print(f"Loaded: {DATA_PATH}")
    print("  N prior samples:", theta.size)
    print("  theta range [rad]: {:.3f} -> {:.3f}".format(theta.min(), theta.max()))
    print("  Omega_Lambda range: {:.3f} -> {:.3f}".format(omega.min(), omega.max()))
    print("  mean(Omega_Lambda)   = {:.3f}".format(omega.mean()))
    print("  median(Omega_Lambda) = {:.3f}".format(np.median(omega)))
    print("  std(Omega_Lambda)    = {:.3f}".format(omega.std()))
    print("  target Omega_Lambda  = {:.3f}".format(omega_target))

    FIG_DIR.mkdir(exist_ok=True)

    fig, ax = plt.subplots(figsize=(6, 4))

    # Simple histogram of the induced Omega_Lambda prior
    bins = np.linspace(0.0, 0.8, 9)
    ax.hist(omega, bins=bins, density=True, alpha=0.8, edgecolor="black", label=r"prior")

    # Target line at Omega_Lambda = 0.7
    ax.axvline(omega_target, linestyle="--", label=rf"target $\Omega_\Lambda = {omega_target:.2f}$")

    ax.set_xlabel(r"$\Omega_\Lambda$")
    ax.set_ylabel("normalized count")
    ax.set_title(r"$\theta_\star$ prior mapped into $\Omega_\Lambda$")
    ax.legend(loc="upper left")

    fig.tight_layout()

    for ext in ("png", "pdf"):
        out = FIG_DIR / f"theta_star_prior_vs_effective_vacuum.{ext}"
        fig.savefig(out, bbox_inches="tight")
        print("  wrote", out)

    plt.close(fig)


if __name__ == "__main__":
    main()