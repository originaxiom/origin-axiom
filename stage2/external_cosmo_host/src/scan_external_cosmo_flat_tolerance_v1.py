#!/usr/bin/env python3
"""
Scan how the external-cosmo host flatness subset behaves as we vary |Omega_tot - 1|.
This is a Stage 2 / external_cosmo_host diagnostic; it does not write per-theta masks,
only a compact summary table.

Inputs:
  - stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_age_anchor_mask_v1.csv

Outputs:
  - stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_flat_tolerance_scan_v1.csv
"""

from __future__ import annotations

import math
from pathlib import Path

import pandas as pd


def main() -> None:
    repo_root = Path(__file__).resolve().parents[3]
    print("[external_cosmo_host_flat_scan] Repo root:", repo_root)

    mask_path = (
        repo_root
        / "stage2"
        / "external_cosmo_host"
        / "outputs"
        / "tables"
        / "stage2_external_cosmo_host_age_anchor_mask_v1.csv"
    )
    if not mask_path.exists():
        raise FileNotFoundError(
            f"[external_cosmo_host_flat_scan] Host age-anchor mask table not found: {mask_path}"
        )

    df = pd.read_csv(mask_path)

    required_cols = ["theta_index", "Omega_m", "Omega_lambda", "frw_viable", "in_toy_corridor"]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise RuntimeError(
            f"[external_cosmo_host_flat_scan] Missing required columns in {mask_path}: {missing}"
        )

    if "Omega_tot" not in df.columns:
        df["Omega_tot"] = df["Omega_m"] + df["Omega_lambda"]

    n_grid = len(df)
    print(f"[external_cosmo_host_flat_scan] Joined rows: {n_grid}")

    # Tolerance grid for |Omega_tot - 1|
    tolerances = [0.01, 0.02, 0.03, 0.05, 0.07, 0.10]

    rows = []
    for tol in tolerances:
        mask_near = (df["Omega_tot"] - 1.0).abs() <= tol
        mask_frw = df["frw_viable"] == 1
        mask_corridor = df["in_toy_corridor"] == 1

        subsets = {
            "ALL_GRID": df,
            "HOST_NEAR_FLAT": df[mask_near],
            "HOST_NEAR_FLAT_AND_FRW_VIABLE": df[mask_near & mask_frw],
            "HOST_NEAR_FLAT_AND_CORRIDOR_AND_FRW_VIABLE": df[mask_near & mask_frw & mask_corridor],
        }

        print(f"[external_cosmo_host_flat_scan] tol={tol:.3f}:")
        for set_name, sub in subsets.items():
            n_theta = len(sub)
            frac = n_theta / n_grid if n_grid > 0 else math.nan
            print(f"  {set_name}: n={n_theta}, frac={frac:.6f}")

            if len(sub) > 0:
                omega_tot_mean = sub["Omega_tot"].mean()
                omega_tot_std = sub["Omega_tot"].std()
                omega_tot_min = sub["Omega_tot"].min()
                omega_tot_max = sub["Omega_tot"].max()
            else:
                omega_tot_mean = omega_tot_std = omega_tot_min = omega_tot_max = math.nan

            rows.append(
                {
                    "tolerance": tol,
                    "set": set_name,
                    "n_theta": n_theta,
                    "frac_of_grid": frac,
                    "Omega_tot_mean": omega_tot_mean,
                    "Omega_tot_std": omega_tot_std,
                    "Omega_tot_min": omega_tot_min,
                    "Omega_tot_max": omega_tot_max,
                }
            )

    out_path = (
        repo_root
        / "stage2"
        / "external_cosmo_host"
        / "outputs"
        / "tables"
        / "stage2_external_cosmo_flat_tolerance_scan_v1.csv"
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(out_path, index=False)
    print("[external_cosmo_host_flat_scan] Summary written:", out_path)


if __name__ == "__main__":
    main()
