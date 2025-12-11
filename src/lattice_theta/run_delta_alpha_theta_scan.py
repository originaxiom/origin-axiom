"""
Theta-grid scan for the 4D lattice vacuum shift Δα(θ).

This script:
- Imports the single-θ evaluator from lattice_delta_alpha.py
- Samples θ on a uniform grid
- Calls compute_delta_alpha_theta(θ, ...)
- Saves a CSV with θ, Δα(θ), σ_A and settings
- Produces a basic θ vs Δα(θ) plot
"""

import argparse
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

from lattice_theta.lattice_delta_alpha import compute_delta_alpha_theta


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Scan Δα(θ) on a θ-grid using the 4D lattice sum."
    )
    parser.add_argument(
        "--theta-min",
        type=float,
        default=0.5,
        help="Minimum θ value (inclusive).",
    )
    parser.add_argument(
        "--theta-max",
        type=float,
        default=3.5,
        help="Maximum θ value (inclusive).",
    )
    parser.add_argument(
        "--n-theta",
        type=int,
        default=16,
        help="Number of θ points in the grid.",
    )
    parser.add_argument(
        "--R-max",
        type=int,
        default=12,
        help="Maximum 4D radius R for the lattice sum.",
    )
    parser.add_argument(
        "--R-fit-min",
        type=int,
        default=6,
        help="Minimum R used in the A + B/R fit.",
    )
    parser.add_argument(
        "--p",
        type=float,
        default=6.0,
        help="Power p in the radial decay (same as in lattice_delta_alpha).",
    )
    parser.add_argument(
        "--out-tag",
        type=str,
        default="theta_grid",
        help="Tag to include in output filenames.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    thetas = np.linspace(args.theta_min, args.theta_max, args.n_theta)

    print("=== θ-grid scan for Δα(θ) ===")
    print(f"θ range     : [{args.theta_min:.6f}, {args.theta_max:.6f}]")
    print(f"n_theta     : {args.n_theta}")
    print(f"R_max       : {args.R_max}")
    print(f"R_fit_min   : {args.R_fit_min}")
    print(f"p           : {args.p}")
    print("----------------------------------------")

    rows = []

    for i, theta in enumerate(thetas, start=1):
        print(f"[{i:03d}/{len(thetas):03d}] θ = {theta:.9f}")
        result = compute_delta_alpha_theta(
            theta=theta,
            R_max=args.R_max,
            p=args.p,
            R_fit_min=args.R_fit_min,
        )
        A = result["A"]
        sigma_A = result["sigma_A"]
        rows.append(
            {
                "theta": theta,
                "delta_alpha": A,
                "sigma_A": sigma_A,
                "R_max": args.R_max,
                "R_fit_min": args.R_fit_min,
                "p": args.p,
            }
        )
        print(f"  Δα(θ) ≈ {A:+.6f} ± {sigma_A:.3e}")

    out_dir_data = Path("data/processed/lattice_theta")
    out_dir_fig = Path("figures/lattice_theta")
    out_dir_data.mkdir(parents=True, exist_ok=True)
    out_dir_fig.mkdir(parents=True, exist_ok=True)

    csv_path = out_dir_data / f"delta_alpha_{args.out_tag}.csv"
    import csv

    fieldnames = ["theta", "delta_alpha", "sigma_A", "R_max", "R_fit_min", "p"]
    with csv_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    thetas_arr = np.array([r["theta"] for r in rows])
    dalpha_arr = np.array([r["delta_alpha"] for r in rows])
    sigma_arr = np.array([r["sigma_A"] for r in rows])

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.errorbar(
        thetas_arr,
        dalpha_arr,
        yerr=sigma_arr,
        fmt="o-",
        capsize=3,
    )
    ax.set_xlabel("theta")
    ax.set_ylabel("delta_alpha(theta)")
    ax.set_title(
        f"Delta alpha(theta) scan, R_max={args.R_max}, "
        f"R_fit>={args.R_fit_min}, p={args.p}"
    )
    ax.grid(True, alpha=0.3)

    fig_path = out_dir_fig / f"delta_alpha_{args.out_tag}.png"
    fig.tight_layout()
    fig.savefig(fig_path, dpi=200)

    print("----------------------------------------")
    print("Saved theta-grid scan to:")
    print(f"  {csv_path}")
    print(f"  {fig_path}")
    print("Done.")


if __name__ == "__main__":
    main()
