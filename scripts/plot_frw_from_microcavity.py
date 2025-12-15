#!/usr/bin/env python3
"""
plot_frw_from_microcavity.py

Visualize the FRW histories produced by src/run_frw_from_microcavity.py:

- Matter-only (Ω_m = 1, Ω_Λ = 0)
- Microcavity-derived vacuum (Ω_m, Ω_Λ) from ΔE(θ★_fid)

Input:
  data/processed/frw_from_microcavity.npz

Output figure:
  data/processed/figures/frw_from_microcavity_a_of_t.png
"""

from __future__ import annotations

import numpy as np
from pathlib import Path

import matplotlib.pyplot as plt


def main() -> None:
    base = Path("data/processed")
    npz_path = base / "frw_from_microcavity.npz"

    if not npz_path.exists():
        raise FileNotFoundError(
            f"Could not find {npz_path}. "
            "Run `PYTHONPATH=src python3 src/run_frw_from_microcavity.py` first."
        )

    data = np.load(npz_path)

    # Extract FRW histories
    t_matter = data["t_matter_only"]
    a_matter = data["a_matter_only"]

    t_micro = data["t_microcavity"]
    a_micro = data["a_microcavity"]

    # Optional metadata for annotation
    theta_fid = float(data["theta_fid"])
    theta_band = data["theta_band"]
    omega_lambda_fid = float(data["omega_lambda_fid"])
    omega_m_fid = float(data["omega_m_fid"])

    # Ensure figures directory exists
    fig_dir = base / "figures"
    fig_dir.mkdir(parents=True, exist_ok=True)
    out_path = fig_dir / "frw_from_microcavity_a_of_t.png"

    # ------------------------------------------------------------------
    # Plot a(t) vs t
    # ------------------------------------------------------------------
    fig, ax = plt.subplots()

    ax.plot(t_matter, a_matter, label=r"matter-only: $\Omega_m = 1, \Omega_\Lambda = 0$")
    ax.plot(
        t_micro,
        a_micro,
        linestyle="--",
        label=(
            r"microcavity: "
            rf"$\Omega_m \approx {omega_m_fid:.2f}, "
            rf"\Omega_\Lambda \approx {omega_lambda_fid:.2f}$"
        ),
    )

    ax.set_xlabel(r"dimensionless time $t H_0$")
    ax.set_ylabel(r"scale factor $a(t)$")
    ax.set_title(
        "FRW expansion histories: matter-only vs microcavity-derived vacuum\n"
        rf"(Act II $\theta^\star_\mathrm{{fid}} \approx {theta_fid:.3f}\,\mathrm{{rad}}, "
        rf"band $\approx [{theta_band[0]:.3f}, {theta_band[1]:.3f}]$)"
    )

    ax.legend()
    ax.grid(True)

    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()