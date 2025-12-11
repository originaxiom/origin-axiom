#!/usr/bin/env python3
"""
??*-agnostic 4D lattice ????(??) test.

We define a 4D integer lattice m = (n1, n2, n3, n4) ??? Z^4 \ {0},
and compute a phase-weighted sum inside a spherical cutoff |m| <= R:

  S_R(??) = sum_{m != 0, |m| <= R} cos(?? * |m|) / |m|^p

for some p > 4 (we use p = 6 by default so the sum is absolutely convergent).

We then:
  * compute S_R for R = 1..R_max,
  * estimate a tail bound using a continuum approximation,
  * fit S_R ??? A + B / R for R >= R_fit_min,
  * interpret A as ????(??).

Outputs:
  * data/processed/lattice_theta/delta_alpha_theta_R{R_max}_theta{theta:.3f}.csv
  * data/processed/lattice_theta/delta_alpha_theta_R{R_max}_theta{theta:.3f}.npz
  * figures/lattice_theta/delta_alpha_theta_R{R_max}_theta{theta:.3f}.png
"""

import argparse
import csv
import math
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt


def lattice_sum_4d(R: int, theta: float, p: float) -> float:
    """
    Brute-force 4D lattice sum:

      S_R = sum_{m in Z^4 \ {0}, |m| <= R} cos(theta * |m|) / |m|^p

    where |m| = sqrt(n1^2 + n2^2 + n3^2 + n4^2).

    Parameters
    ----------
    R : int
        Spherical cutoff radius in lattice units (integer).
    theta : float
        Phase parameter ??.
    p : float
        Power in the denominator (must be > 4 for absolute convergence).

    Returns
    -------
    float
        Partial sum S_R.
    """
    R2 = R * R
    S = 0.0

    for n1 in range(-R, R + 1):
        n1_sq = n1 * n1
        for n2 in range(-R, R + 1):
            n2_sq = n2 * n2
            for n3 in range(-R, R + 1):
                n3_sq = n3 * n3
                for n4 in range(-R, R + 1):
                    n4_sq = n4 * n4
                    # skip origin
                    if n1 == 0 and n2 == 0 and n3 == 0 and n4 == 0:
                        continue

                    r2 = n1_sq + n2_sq + n3_sq + n4_sq
                    if r2 > R2:
                        continue

                    r = math.sqrt(r2)
                    S += math.cos(theta * r) / (r ** p)

    return S


def tail_bound_4d(R: float, p: float) -> float:
    """
    Rough continuum tail bound for the sum over |m| > R.

    We approximate the shell measure in 4D:

      dN ~ S_3 * r^3 dr,  with S_3 = 2??^2  (surface area of the unit 3-sphere).

    Then for p > 4:

      |tail| ~ ???_R^??? S_3 * r^3 * (1 / r^p) dr
              = S_3 * ???_R^??? r^{3-p} dr
              = S_3 * [ r^{4-p} / (4 - p) ]_R^???
              = S_3 * (R^{4-p}) / (p - 4)

    We take the absolute value as an upper bound.

    Parameters
    ----------
    R : float
        Radius beyond which we approximate the tail.
    p : float
        Power in the denominator (> 4).

    Returns
    -------
    float
        Tail bound estimate.
    """
    if p <= 4.0:
        return float("inf")
    S3 = 2.0 * math.pi ** 2
    return S3 * (R ** (4.0 - p)) / (p - 4.0)


def compute_delta_alpha_theta(theta: float,
                              R_max: int,
                              p: float,
                              R_fit_min: int):
    """
    Compute S_R(??) up to R_max, estimate tail bounds, and fit S_R ??? A + B / R.

    Parameters
    ----------
    theta : float
        Phase parameter ??.
    R_max : int
        Maximum spherical cutoff radius.
    p : float
        Power in the denominator for the lattice sum.
    R_fit_min : int
        Minimum R to include in the A + B/R fit.

    Returns
    -------
    dict
        {
          "R_values": np.ndarray,
          "S_values": np.ndarray,
          "tail_bounds": np.ndarray,
          "theta": float,
          "p": float,
          "R_fit_min": int,
          "A": float,     # fitted ????(??)
          "B": float,
          "A_err": float, # naive standard error on A
        }
    """
    Rs = np.arange(1, R_max + 1, dtype=int)
    S_values = []
    tail_bounds = []

    print("Computing 4D lattice partial sums up to R_max={}...".format(R_max))
    for R in Rs:
        S_R = lattice_sum_4d(int(R), theta, p)
        tb = tail_bound_4d(float(R), p)
        S_values.append(S_R)
        tail_bounds.append(tb)
        print(f"  R={R:2d}: S_R={S_R:+.8f}, tail_bound???{tb:.3e}")

    S_values = np.array(S_values, dtype=float)
    tail_bounds = np.array(tail_bounds, dtype=float)

    # Fit S_R ??? A + B / R for R >= R_fit_min
    mask = Rs >= R_fit_min
    if np.count_nonzero(mask) < 2:
        raise ValueError("Not enough R values ??? R_fit_min for a linear fit.")

    x = 1.0 / Rs[mask]
    y = S_values[mask]

    coeffs, cov = np.polyfit(x, y, 1, cov=True)
    B, A = coeffs  # y ??? B*x + A
    # naive errors from covariance
    A_err = float(np.sqrt(cov[1, 1])) if cov.size == 4 else float("nan")

    print("----------------------------------------------------")
    print("Fit S_R ??? A + B/R for R ??? {}:".format(R_fit_min))
    print(f"  A ??? {A:+.8f}  (interpreted as ????(??))")
    print(f"  B ??? {B:+.8f}")
    print(f"  naive ??_A ??? {A_err:.3e}")

    return {
        "R_values": Rs,
        "S_values": S_values,
        "tail_bounds": tail_bounds,
        "theta": float(theta),
        "p": float(p),
        "R_fit_min": int(R_fit_min),
        "A": float(A),
        "B": float(B),
        "A_err": float(A_err),
    }


def save_results(result: dict,
                 out_root: Path) -> None:
    """
    Save CSV, NPZ, and a simple plot of S_R vs 1/R with fit.

    Parameters
    ----------
    result : dict
        Output from compute_delta_alpha_theta().
    out_root : Path
        Root directory of the project (where data/ and figures/ live).
    """
    theta = result["theta"]
    R_max = int(result["R_values"][-1])

    data_dir = out_root / "data" / "processed" / "lattice_theta"
    fig_dir = out_root / "figures" / "lattice_theta"
    data_dir.mkdir(parents=True, exist_ok=True)
    fig_dir.mkdir(parents=True, exist_ok=True)

    # Filenames keyed by R_max and ?? (rounded for readability)
    tag = f"R{R_max}_theta{theta:.3f}"

    csv_path = data_dir / f"delta_alpha_theta_{tag}.csv"
    npz_path = data_dir / f"delta_alpha_theta_{tag}.npz"
    fig_path = fig_dir / f"delta_alpha_theta_{tag}.png"

    # Save NPZ
    np.savez(
        npz_path,
        R_values=result["R_values"],
        S_values=result["S_values"],
        tail_bounds=result["tail_bounds"],
        theta=result["theta"],
        p=result["p"],
        R_fit_min=result["R_fit_min"],
        A=result["A"],
        B=result["B"],
        A_err=result["A_err"],
    )

    # Save CSV
    with csv_path.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "R",
            "S_R",
            "tail_bound",
            "theta",
            "p",
            "R_fit_min",
            "A_fit",
            "B_fit",
            "A_err",
        ])
        for R, S_R, tb in zip(
            result["R_values"], result["S_values"], result["tail_bounds"]
        ):
            writer.writerow([
                int(R),
                f"{S_R:.10e}",
                f"{tb:.10e}",
                f"{theta:.10e}",
                f"{result['p']:.10e}",
                result["R_fit_min"],
                f"{result['A']:.10e}",
                f"{result['B']:.10e}",
                f"{result['A_err']:.10e}",
            ])

    # Make a simple plot S_R vs 1/R with fitted line
    Rs = result["R_values"]
    S_vals = result["S_values"]
    mask = Rs >= result["R_fit_min"]

    x = 1.0 / Rs
    x_fit = x[mask]
    y_fit = S_vals[mask]

    A = result["A"]
    B = result["B"]
    x_dense = np.linspace(0.0, x_fit.max(), 200)
    y_dense = B * x_dense + A

    plt.figure()
    plt.scatter(x, S_vals, label="S_R data")
    plt.plot(x_dense, y_dense, label="fit A + B/R")
    plt.xlabel("1 / R")
    plt.ylabel("S_R(??)")
    plt.title(f"4D lattice ????(??) vs 1/R (??={theta:.3f}, R_max={R_max})")
    plt.legend()
    plt.tight_layout()
    plt.savefig(fig_path, dpi=200)
    plt.close()

    print("Saved results to:")
    print(f"  {npz_path}")
    print(f"  {csv_path}")
    print(f"Saved figure to:")
    print(f"  {fig_path}")


def main():
    parser = argparse.ArgumentParser(
        description="??*-agnostic 4D lattice ????(??) test (brute-force, no numba)."
    )
    parser.add_argument(
        "--theta",
        type=float,
        required=True,
        help="Phase parameter ??.",
    )
    parser.add_argument(
        "--R-max",
        type=int,
        default=12,
        help="Maximum lattice radius R_max (integer).",
    )
    parser.add_argument(
        "--p",
        type=float,
        default=6.0,
        help="Power p in denominator (must be > 4 for convergence).",
    )
    parser.add_argument(
        "--R-fit-min",
        type=int,
        default=6,
        help="Minimum R to include in linear fit S_R ??? A + B/R.",
    )

    args = parser.parse_args()

    print("=== ??*-agnostic 4D lattice ????(??) test ===")
    print(f"theta = {args.theta:.6f}")
    print(f"R_max = {args.R_max}, p = {args.p}, R_fit_min = {args.R_fit_min}")
    print("----------------------------------------------------")

    out_root = Path(__file__).resolve().parents[2]  # project root (???/origin-axiom)

    result = compute_delta_alpha_theta(
        theta=args.theta,
        R_max=args.R_max,
        p=args.p,
        R_fit_min=args.R_fit_min,
    )

    save_results(result, out_root)


if __name__ == "__main__":
    main()
