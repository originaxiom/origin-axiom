"""
run_chain_residual_scan.py

Scan how well 1D integer-structured chains can cancel a complex sum
S = Σ e^{i θ_j} under a θ-agnostic phase rule

    θ_j = q_j * theta + noise_j,

with integer charges q_j ∈ [-max_charge, +max_charge] and optional global
constraint Σ q_j = 0.

For each (theta, N), we draw 'n_samples' independent chains and record:

  - mean |S|
  - rms |S|
  - mean (|S| / sqrt(N))
  - rms (|S| / sqrt(N))

Outputs:
  - CSV:  data/processed/cancellation_system/chain_residual_scan.csv
  - PNG:  figures/cancellation_system/chain_residual_scan.png

This is a *probe* of the non-cancelling principle:
if the system behaved like random phases, |S| ~ O(sqrt(N)).
Deviations in scaling or θ-dependence may signal interesting structure.
"""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path
from typing import List

import numpy as np

try:
    import matplotlib.pyplot as plt
    HAVE_MPL = True
except Exception:
    HAVE_MPL = False

from .model_1d_chain import ChainConfig, summarize_many


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Scan 1D cancellation chains over N and theta."
    )
    p.add_argument(
        "--Ns",
        type=str,
        default="8,16,32,64,128",
        help="Comma-separated list of N values (chain lengths). Default: 8,16,32,64,128",
    )
    p.add_argument(
        "--theta",
        type=float,
        default=2.0,
        help="Single theta value to scan (if --thetas not given). Default: 2.0",
    )
    p.add_argument(
        "--thetas",
        type=str,
        default=None,
        help="Optional comma-separated list of theta values, e.g. '1.5,2.0,2.5'.",
    )
    p.add_argument(
        "--max-charge",
        type=int,
        default=5,
        help="Max |q_j| allowed. Default: 5",
    )
    p.add_argument(
        "--noise-sigma",
        type=float,
        default=0.0,
        help="Std dev of Gaussian phase noise. Default: 0.0 (no noise).",
    )
    p.add_argument(
        "--n-samples",
        type=int,
        default=500,
        help="Number of independent chains per (theta, N). Default: 500",
    )
    p.add_argument(
        "--seed",
        type=int,
        default=1234,
        help="Base RNG seed (for reproducibility). Default: 1234",
    )
    p.add_argument(
        "--no-zero-sum",
        action="store_true",
        help="Disable sum(q_j) = 0 constraint if set.",
    )
    return p.parse_args()


def _parse_float_list(s: str) -> List[float]:
    out: List[float] = []
    for chunk in s.split(","):
        chunk = chunk.strip()
        if not chunk:
            continue
        out.append(float(chunk))
    return out


def main() -> None:
    args = parse_args()

    Ns = [int(x) for x in args.Ns.split(",") if x.strip()]
    if args.thetas is not None:
        thetas = _parse_float_list(args.thetas)
    else:
        thetas = [args.theta]

    enforce_zero_sum = not args.no_zero_sum

    # Output paths
    data_dir = Path("data/processed/cancellation_system")
    fig_dir = Path("figures/cancellation_system")
    data_dir.mkdir(parents=True, exist_ok=True)
    fig_dir.mkdir(parents=True, exist_ok=True)

    out_csv = data_dir / "chain_residual_scan.csv"

    print("=== 1D cancellation chain residual scan ===")
    print(f"Ns      : {Ns}")
    print(f"thetas  : {thetas}")
    print(f"max_q   : {args.max_charge}")
    print(f"noise   : {args.noise_sigma}")
    print(f"n_samples per point: {args.n_samples}")
    print(f"enforce_zero_sum   : {enforce_zero_sum}")
    print("----------------------------------------------------")

    rows: List[dict] = []
    for theta in thetas:
        print(f"\n--- theta = {theta:.6f} ---")
        for N in Ns:
            cfg = ChainConfig(
                N=N,
                theta=theta,
                max_charge=args.max_charge,
                noise_sigma=args.noise_sigma,
                enforce_zero_sum=enforce_zero_sum,
                seed=args.seed,
            )
            stats = summarize_many(cfg, n_samples=args.n_samples)
            rows.append(stats)

            print(
                f"N={N:4d}: "
                f"mean|S|={stats['mean_S_abs']:.3f}, "
                f"rms|S|={stats['rms_S_abs']:.3f}, "
                f"mean|S|/sqrtN={stats['mean_S_abs_over_sqrtN']:.3f}"
            )

    # Write CSV
    if rows:
        fieldnames = list(rows[0].keys())
        with out_csv.open("w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        print(f"\nSaved scan summary to: {out_csv}")

    # Optional plot
    if HAVE_MPL and rows:
        # Group by theta
        rows_arr = rows
        # Unique thetas in insertion order
        unique_thetas: List[float] = []
        for r in rows_arr:
            t = float(r["theta"])
            if t not in unique_thetas:
                unique_thetas.append(t)

        plt.figure()
        for theta in unique_thetas:
            Ns_for_t = sorted({r["N"] for r in rows_arr if float(r["theta"]) == theta})
            means_for_t = []
            for N in Ns_for_t:
                # Find row
                for r in rows_arr:
                    if r["N"] == N and float(r["theta"]) == theta:
                        means_for_t.append(r["mean_S_abs_over_sqrtN"])
                        break
            plt.plot(
                Ns_for_t,
                means_for_t,
                marker="o",
                label=f"theta={theta:g}",
            )

        plt.xscale("log")
        plt.xlabel("N (chain length)")
        plt.ylabel("mean |S| / sqrt(N)")
        plt.title("1D cancellation chain residuals (θ-agnostic)")
        plt.legend()
        plt.grid(True, which="both", linestyle="--", alpha=0.4)

        fig_path = fig_dir / "chain_residual_scan.png"
        plt.tight_layout()
        plt.savefig(fig_path, dpi=150)
        plt.close()
        print(f"Saved figure to: {fig_path}")
    else:
        if not HAVE_MPL:
            print("matplotlib not available; skipping plot.")
        else:
            print("No data rows; nothing to plot.")


if __name__ == "__main__":
    main()
