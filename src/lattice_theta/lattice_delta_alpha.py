#!/usr/bin/env python3
"""
θ*-agnostic 4D lattice Δα(θ) test.

We define a 4D integer lattice n = (n1,n2,n3,n4) ∈ ℤ⁴, exclude the origin,
and sum over shells |n| ≤ R_max.  For a given (θ, p) we form

    S_R(θ) = ∑_{0 < |n| ≤ R} cos(θ |n|) / |n|^p

We then fit S_R as a function of R to

    S_R ≈ A + B / R

for R ≥ R_fit_min, and interpret A as Δα(θ).
"""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np


def lattice_sum_4d(theta: float, R_max: int, p: float) -> Tuple[np.ndarray, np.ndarray]:
    """
    Compute partial sums S_R(θ) up to R_max on a 4D lattice, along with
    a crude tail bound estimate for each R.

    Returns
    -------
    R_vals : np.ndarray
        Radii 1..R_max as float.
    S_vals : np.ndarray
        Corresponding partial sums S_R.
    """
    R_vals: List[float] = []
    S_vals: List[float] = []

    for R in range(1, R_max + 1):
        R2 = R * R
        S_R = 0.0

        for n1 in range(-R, R + 1):
            n1_sq = n1 * n1
            for n2 in range(-R, R + 1):
                n2_sq = n2 * n2
                for n3 in range(-R, R + 1):
                    n3_sq = n3 * n3
                    for n4 in range(-R, R + 1):
                        # skip origin
                        if n1 == 0 and n2 == 0 and n3 == 0 and n4 == 0:
                            continue

                        n4_sq = n4 * n4
                        r2 = n1_sq + n2_sq + n3_sq + n4_sq
                        if r2 == 0 or r2 > R2:
                            continue

                        r = math.sqrt(r2)
                        S_R += math.cos(theta * r) / (r**p)

        R_vals.append(float(R))
        S_vals.append(S_R)

        # crude analytic tail bound using 4D shell measure 2π² r³
        # ∫_R^∞ 2π² r³ dr / r^p = 2π² R^{4-p} / (p - 4),  p > 4
        if p > 4.0:
            tail = (2.0 * math.pi**2) * (R ** (4.0 - p)) / (p - 4.0)
        else:
            tail = float("nan")

        print(f"  R={R:2d}: S_R={S_R:+.8f}, tail_bound~ {tail: .3e}")

    return np.array(R_vals, dtype=float), np.array(S_vals, dtype=float)


def fit_delta_alpha(
    R_vals: np.ndarray,
    S_vals: np.ndarray,
    R_fit_min: int,
) -> Tuple[float, float, float]:
    """
    Fit S_R ≈ A + B/R over R >= R_fit_min.

    Returns
    -------
    A : float
        Intercept, interpreted as Δα(θ).
    B : float
        Coefficient of 1/R.
    sigma_A : float
        Naive uncertainty estimate for A.
    """
    mask = R_vals >= float(R_fit_min)
    R_fit = R_vals[mask]
    S_fit = S_vals[mask]

    # Design matrix for [A, B]
    X = np.column_stack(
        [
            np.ones_like(R_fit),
            1.0 / R_fit,
        ]
    )

    # Least-squares fit
    params, *_ = np.linalg.lstsq(X, S_fit, rcond=None)
    A, B = params

    # Naive covariance estimate
    residuals = S_fit - X @ params
    dof = max(len(S_fit) - 2, 1)
    s2 = float(np.sum(residuals**2) / dof)
    XT_X_inv = np.linalg.inv(X.T @ X)
    sigma_A = math.sqrt(XT_X_inv[0, 0] * s2)

    return A, B, sigma_A


def compute_delta_alpha_theta(
    theta: float,
    R_max: int,
    R_fit_min: int,
    p: float,
) -> Dict[str, float]:
    """
    High-level driver: compute S_R(θ), fit Δα(θ), and print a summary.
    """
    print("=== θ*-agnostic 4D lattice Δα(θ) test ===")
    print(f"theta = {theta:.6f}")
    print(f"R_max = {R_max}, p = {p}, R_fit_min = {R_fit_min}")
    print("----------------------------------------------------")
    print(f"Computing 4D lattice partial sums up to R_max={R_max}...")

    R_vals, S_vals = lattice_sum_4d(theta, R_max, p)

    print("----------------------------------------------------")
    print(f"Fit S_R ~ A + B/R for R >= {R_fit_min}:")

    A, B, sigma_A = fit_delta_alpha(R_vals, S_vals, R_fit_min)

    print(f"  A ≈ {A:+.8f}  (interpreted as Δα(θ))")
    print(f"  B ≈ {B:+.8f}")
    print(f"  naive σ_A ≈ {sigma_A: .3e}")
    print(f"  Δα(θ) ≈ {A:+.6f} ± {sigma_A: .3e}")

    return {
        "theta": theta,
        "R_max": R_max,
        "R_fit_min": R_fit_min,
        "p": p,
        "delta_alpha": A,
        "sigma_A": sigma_A,
        "B": B,
        "A": A,
        "A_err": sigma_A,
    }


def save_delta_alpha_results(
    res: Dict[str, float],
    R_vals: np.ndarray,
    S_vals: np.ndarray,
    out_tag: str,
) -> None:
    """
    Save detailed results (R, S_R) plus fit parameters to .npz/.csv,
    and a quick R→S_R plot.
    """
    out_dir_data = Path("data/processed/lattice_theta")
    out_dir_fig = Path("figures/lattice_theta")
    out_dir_data.mkdir(parents=True, exist_ok=True)
    out_dir_fig.mkdir(parents=True, exist_ok=True)

    theta = res["theta"]
    R_max = int(res["R_max"])

    base = f"delta_alpha_theta_R{R_max}_theta{theta:.3f}"
    npz_path = out_dir_data / f"{base}.npz"
    csv_path = out_dir_data / f"{base}.csv"

    np.savez(
        npz_path,
        theta=theta,
        R=R_vals,
        S_R=S_vals,
        delta_alpha=res["delta_alpha"],
        sigma_A=res["sigma_A"],
        B=res["B"],
        R_max=res["R_max"],
        R_fit_min=res["R_fit_min"],
        p=res["p"],
    )

    with csv_path.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            ["theta", "R", "S_R", "delta_alpha", "sigma_A", "B", "R_max", "R_fit_min", "p"]
        )
        for R, S in zip(R_vals, S_vals):
            writer.writerow(
                [
                    theta,
                    int(R),
                    S,
                    res["delta_alpha"],
                    res["sigma_A"],
                    res["B"],
                    res["R_max"],
                    res["R_fit_min"],
                    res["p"],
                ]
            )

    # simple R-plot
    try:
        import matplotlib.pyplot as plt  # type: ignore

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(R_vals, S_vals, "o-")
        ax.set_xlabel("R")
        ax.set_ylabel("S_R(theta)")
        ax.set_title(
            rf"4D lattice S_R, θ={theta:.6f}, R_max={R_max}, "
            rf"R_{{fit}}\ge {res['R_fit_min']}, p={res['p']}"
        )
        ax.grid(True, alpha=0.3)
        fig.tight_layout()

        fig_path = out_dir_fig / f"{base}.png"
        fig.savefig(fig_path, dpi=200)
    except Exception as exc:  # plotting not critical
        print("Warning: failed to make R-plot:", exc)

    print("Saved results to:")
    print(f"  {npz_path}")
    print(f"  {csv_path}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="θ*-agnostic 4D lattice Δα(θ) test (single θ)."
    )
    parser.add_argument(
        "--theta",
        type=float,
        required=True,
        help="theta value to test",
    )
    parser.add_argument(
        "--R-max",
        type=int,
        required=True,
        help="maximum lattice radius R_max",
    )
    parser.add_argument(
        "--R-fit-min",
        type=int,
        required=True,
        help="minimum R used in the A + B/R fit",
    )
    parser.add_argument(
        "--p",
        type=float,
        default=6.0,
        help="power p in the 1/|n|^p weight (default 6.0)",
    )
    args = parser.parse_args()

    res = compute_delta_alpha_theta(
        theta=args.theta,
        R_max=args.R_max,
        R_fit_min=args.R_fit_min,
        p=args.p,
    )

    # Recompute S_R / R_vals for saving (compute_delta_alpha_theta prints only)
    R_vals, S_vals = lattice_sum_4d(args.theta, args.R_max, args.p)
    save_delta_alpha_results(res, R_vals, S_vals, out_tag=f"theta_R{args.R_max}")

