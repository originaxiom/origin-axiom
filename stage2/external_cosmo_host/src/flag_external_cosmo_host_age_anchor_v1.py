#!/usr/bin/env python3
"""
Stage 2 / external_cosmo_host – H4: host age anchor window on external cosmology host.

Goal:
  - Take the external-cosmo host background grid (theta -> Omega_m, Omega_lambda, H0, age_host),
  - Join it with the joint theta grid (repo FRW quantities + corridor/viability masks),
  - Flag a host-age "anchor window" around the observed Universe age,
  - Summarise overlaps with FRW_VIABLE and TOY_CORRIDOR.

This stays strictly in the toy/host-diagnostic lane:
  - No new data ingestion here beyond the chosen age window.
  - No Phase-level claims; this is a Stage 2 diagnostic rung.

Outputs:
  - Mask table:
      stage2/external_cosmo_host/outputs/tables/
        stage2_external_cosmo_host_age_anchor_mask_v1.csv
  - Summary table:
      stage2/external_cosmo_host/outputs/tables/
        stage2_external_cosmo_host_age_anchor_summary_v1.csv
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np
import pandas as pd


def main() -> None:
    # Repo root (origin-axiom)
    repo_root = Path(__file__).resolve().parents[3]

    host_path = (
        repo_root
        / "stage2"
        / "external_cosmo_host"
        / "outputs"
        / "tables"
        / "stage2_external_cosmo_host_background_grid_v1.csv"
    )

    joint_path = (
        repo_root
        / "stage2"
        / "joint_mech_frw_analysis"
        / "outputs"
        / "tables"
        / "stage2_joint_theta_grid_v1.csv"
    )

    mask_out = (
        repo_root
        / "stage2"
        / "external_cosmo_host"
        / "outputs"
        / "tables"
        / "stage2_external_cosmo_host_age_anchor_mask_v1.csv"
    )

    summary_out = (
        repo_root
        / "stage2"
        / "external_cosmo_host"
        / "outputs"
        / "tables"
        / "stage2_external_cosmo_host_age_anchor_summary_v1.csv"
    )

    print("[external_cosmo_host_H4] Repo root:", repo_root)
    print("[external_cosmo_host_H4] Host background table:", host_path)
    print("[external_cosmo_host_H4] Joint theta grid:", joint_path)

    if not host_path.is_file():
        raise FileNotFoundError(f"Host background grid not found: {host_path}")
    if not joint_path.is_file():
        raise FileNotFoundError(f"Joint theta grid not found: {joint_path}")

    df_host = pd.read_csv(host_path)
    df_joint = pd.read_csv(joint_path)

    required_host_cols = [
        "theta_index",
        "theta",
        "Omega_m",
        "Omega_lambda",
        "H0_km_s_Mpc",
        "age_Gyr_host",
    ]
    missing_host = [c for c in required_host_cols if c not in df_host.columns]
    if missing_host:
        raise RuntimeError(f"Missing required columns in host background grid: {missing_host}")

    required_joint_cols = [
        "theta_index",
        "omega_lambda",
        "age_Gyr",
        "in_toy_corridor",
        "frw_viable",
    ]
    missing_joint = [c for c in required_joint_cols if c not in df_joint.columns]
    if missing_joint:
        raise RuntimeError(f"Missing required columns in joint grid: {missing_joint}")

    # Join on theta_index
    df = df_host.merge(
        df_joint[required_joint_cols],
        on="theta_index",
        how="left",
        suffixes=("_host", "_repo"),
    )

    n_total = len(df)
    print(f"[external_cosmo_host_H4] Joined rows: {n_total}")

    if n_total == 0:
        raise RuntimeError("Joined host/joint table is empty.")

    # Normalise booleans
    df["frw_viable"] = df["frw_viable"].astype(bool)
    df["in_toy_corridor"] = df["in_toy_corridor"].astype(bool)

    # Host age anchor window (same window we used elsewhere)
    age_min = 13.3
    age_max = 14.3
    df["in_host_age_anchor_window"] = (df["age_Gyr_host"] >= age_min) & (
        df["age_Gyr_host"] <= age_max
    )

    print(
        f"[external_cosmo_host_H4] Host age anchor window [Gyr]: "
        f"[{age_min:.3f}, {age_max:.3f}]"
    )

    # Define masks
    mask_all = np.ones(n_total, dtype=bool)
    mask_frw = df["frw_viable"].to_numpy()
    mask_corr = df["in_toy_corridor"].to_numpy()
    mask_anchor = df["in_host_age_anchor_window"].to_numpy()

    sets = {
        "ALL_GRID": mask_all,
        "FRW_VIABLE": mask_frw,
        "TOY_CORRIDOR": mask_corr,
        "HOST_AGE_ANCHOR": mask_anchor,
        "FRW_VIABLE_AND_HOST_AGE_ANCHOR": mask_frw & mask_anchor,
        "CORRIDOR_AND_HOST_AGE_ANCHOR": mask_corr & mask_anchor,
        "CORRIDOR_AND_VIABLE_AND_HOST_AGE_ANCHOR": mask_corr & mask_frw & mask_anchor,
    }

    def summarise(mask: np.ndarray, name: str) -> dict:
        if mask is None:
            sub = df
        else:
            sub = df[mask]

        n = len(sub)
        frac = float(n) / float(n_total) if n_total > 0 else math.nan

        def stats(col: str):
            if n == 0:
                return (math.nan, math.nan, math.nan, math.nan)
            arr = sub[col].to_numpy(dtype=float)
            return (
                float(np.nanmean(arr)),
                float(np.nanstd(arr)),
                float(np.nanmin(arr)),
                float(np.nanmax(arr)),
            )

        age_host_mean, age_host_std, age_host_min, age_host_max = stats("age_Gyr_host")
        age_repo_mean, age_repo_std, age_repo_min, age_repo_max = stats("age_Gyr")
        om_repo_mean, om_repo_std, om_repo_min, om_repo_max = stats("omega_lambda")
        om_host_mean, om_host_std, om_host_min, om_host_max = stats("Omega_lambda")

        print(
            f"[external_cosmo_host_H4] {name:32s} n={n:4d}, frac={frac:0.6f}, "
            f"<age_host>={age_host_mean:0.3f} Gyr, <age_repo>={age_repo_mean:0.3f} Gyr"
        )

        return {
            "set": name,
            "n_theta": n,
            "frac_of_grid": frac,
            "age_Gyr_host_mean": age_host_mean,
            "age_Gyr_host_std": age_host_std,
            "age_Gyr_host_min": age_host_min,
            "age_Gyr_host_max": age_host_max,
            "age_Gyr_repo_mean": age_repo_mean,
            "age_Gyr_repo_std": age_repo_std,
            "age_Gyr_repo_min": age_repo_min,
            "age_Gyr_repo_max": age_repo_max,
            "omega_lambda_repo_mean": om_repo_mean,
            "omega_lambda_repo_std": om_repo_std,
            "omega_lambda_repo_min": om_repo_min,
            "omega_lambda_repo_max": om_repo_max,
            "Omega_lambda_host_mean": om_host_mean,
            "Omega_lambda_host_std": om_host_std,
            "Omega_lambda_host_min": om_host_min,
            "Omega_lambda_host_max": om_host_max,
        }

    rows = [summarise(m, name) for name, m in sets.items()]

    # Save summary table
    summary_out.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(summary_out, index=False)
    print(f"[external_cosmo_host_H4] Summary written:", summary_out)

    # Save mask table for downstream rungs
    mask_cols = [
        "theta_index",
        "theta",
        "Omega_m",
        "Omega_lambda",
        "H0_km_s_Mpc",
        "age_Gyr_host",
        "omega_lambda",
        "age_Gyr",
        "frw_viable",
        "in_toy_corridor",
        "in_host_age_anchor_window",
    ]
    missing_mask_cols = [c for c in mask_cols if c not in df.columns]
    if missing_mask_cols:
        raise RuntimeError(f"Missing expected columns for mask table: {missing_mask_cols}")

    mask_df = df[mask_cols].rename(
        columns={
            "omega_lambda": "omega_lambda_repo",
            "age_Gyr": "age_Gyr_repo",
        }
    )
    mask_out.parent.mkdir(parents=True, exist_ok=True)
    mask_df.to_csv(mask_out, index=False)
    print(f"[external_cosmo_host_H4] Host age-anchor mask written:", mask_out)


if __name__ == "__main__":
    main()
