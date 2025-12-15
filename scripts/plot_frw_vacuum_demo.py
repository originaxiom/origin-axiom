#!/usr/bin/env python3
"""
plot_frw_vacuum_demo.py

Plot the FRW toy-universe results saved by src/run_frw_vacuum_demo.py.

The NPZ file contains separate time + a(t) arrays for each cosmology:
  - t_matter_only, a_matter_only
  - t_lambda_30,  a_lambda_30
  - t_lambda_70,  a_lambda_70
We assume all three time grids are identical (and check this).
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt


def main() -> None:
    data_path = Path("data/processed/frw_vacuum_demo.npz")
    if not data_path.exists():
        raise FileNotFoundError(
            f"Could not find {data_path}. "
            "Run `PYTHONPATH=src python3 src/run_frw_vacuum_demo.py` first."
        )

    data = np.load(data_path)
    print(f"Loaded {data_path}")
    print("Available arrays:", data.files)

    # Extract arrays using the actual keys in your file
    t_m = data["t_matter_only"]
    a_m = data["a_matter_only"]

    t_30 = data["t_lambda_30"]
    a_30 = data["a_lambda_30"]

    t_70 = data["t_lambda_70"]
    a_70 = data["a_lambda_70"]

    # Sanity check: time grids should be identical
    if not (np.allclose(t_m, t_30) and np.allclose(t_m, t_70)):
        raise ValueError(
            "Time grids for the three cosmologies differ; "
            "cannot safely plot on a single shared t axis."
        )

    t = t_m  # common time grid

    fig, ax = plt.subplots()

    ax.plot(t, a_m, label=r"$\Omega_m=1, \Omega_\Lambda=0$ (matter only)")
    ax.plot(t, a_30, label=r"$\Omega_m=0.7, \Omega_\Lambda=0.3$")
    ax.plot(t, a_70, label=r"$\Omega_m=0.3, \Omega_\Lambda=0.7$")

    ax.set_xlabel(r"time $t$ (in $H_0^{-1}$ units)")
    ax.set_ylabel(r"scale factor $a(t)$")
    ax.set_title("FRW toy universe: matter vs vacuum-dominated cases")
    ax.legend()
    ax.grid(True, alpha=0.3)

    out_dir = Path("data/processed/figures")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "frw_vacuum_demo_a_of_t.png"
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close(fig)

    print(f"Wrote figure to {out_path}")


if __name__ == "__main__":
    main()