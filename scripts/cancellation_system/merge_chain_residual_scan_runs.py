#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
import numpy as np
import pandas as pd


def theta_grid(theta_min: float, theta_max: float, n_theta: int) -> np.ndarray:
    return np.linspace(theta_min, theta_max, n_theta)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inputs", nargs="+", required=True, help="Input CSVs to merge")
    ap.add_argument("--out", required=True, help="Output CSV")
    ap.add_argument("--theta-min", type=float, required=True)
    ap.add_argument("--theta-max", type=float, required=True)
    ap.add_argument("--n-theta", type=int, required=True)
    ap.add_argument(
        "--theta-tol",
        type=float,
        default=2e-4,
        help="Tolerance for snapping theta to nearest grid point.",
    )
    args = ap.parse_args()

    grid = theta_grid(args.theta_min, args.theta_max, args.n_theta)

    df = pd.concat([pd.read_csv(p) for p in args.inputs], ignore_index=True)
    thetas = df["theta"].astype(float).to_numpy()

    # snap to nearest grid
    idx = np.searchsorted(grid, thetas)
    idx = np.clip(idx, 1, len(grid) - 1)
    left = grid[idx - 1]
    right = grid[idx]
    nearest = np.where(np.abs(thetas - left) <= np.abs(thetas - right), left, right)

    max_err = float(np.max(np.abs(thetas - nearest))) if len(thetas) else 0.0
    if max_err > args.theta_tol:
        bad = df.loc[np.abs(thetas - nearest) > args.theta_tol, ["theta"]].head(20)
        raise SystemExit(
            f"Theta values too far from grid (max_err={max_err}, tol={args.theta_tol}). Example:\n{bad}"
        )

    df["theta"] = nearest

    # drop duplicates by (theta,N)
    df = df.sort_values(["theta", "N"])
    df = df.drop_duplicates(subset=["theta", "N"], keep="first")

    # validate expected grid coverage for the N values present
    Ns = sorted(df["N"].unique())
    expected = set((float(t), int(N)) for t in grid for N in Ns)
    got = set((float(r.theta), int(r.N)) for r in df[["theta", "N"]].itertuples(index=False))

    missing = sorted(expected - got)
    extra = sorted(got - expected)

    if extra:
        raise SystemExit(f"Extra {len(extra)} (theta,N) pairs outside expected grid. First 10: {extra[:10]}")

    # write even if missing, but report missing explicitly
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(args.out, index=False)
    print("[ok] wrote", args.out, "rows:", len(df))
    if missing:
        print(f"[warn] missing {len(missing)} (theta,N) pairs. First 10:", missing[:10])


if __name__ == "__main__":
    main()