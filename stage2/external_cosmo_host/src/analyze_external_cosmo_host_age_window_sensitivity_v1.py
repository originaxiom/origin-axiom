#!/usr/bin/env python

"""
Stage 2 – External cosmology host: host age-window sensitivity (H6).

Goal:
  Starting from the external host background grid and the joint theta grid,
  sweep a handful of age windows around the current host age anchor and
  quantify how many theta points fall into:

    - HOST_WINDOW
    - FRW_VIABLE_AND_HOST_WINDOW
    - CORRIDOR_AND_VIABLE_AND_HOST_WINDOW

  and what their mean ages / omega_lambda look like.

This is a diagnostic rung only – no physics claims.
"""

from __future__ import annotations

from pathlib import Path
from typing import Dict, List

import numpy as np
import pandas as pd


def find_repo_root(start: Path) -> Path:
    """
    Heuristic repo-root finder: walk up until we see 'stage2' and 'phase4'.
    """
    for parent in [start] + list(start.parents):
        if (parent / "stage2").is_dir() and (parent / "phase4").is_dir():
            return parent
    raise RuntimeError("Could not locate repo root (expected 'stage2' and 'phase4').")


def main() -> None:
    here = Path(__file__).resolve()
    repo_root = find_repo_root(here)
    print(f"[external_cosmo_host_H6] Repo root: {repo_root}")

    bg_path = (
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

    if not bg_path.is_file():
        raise FileNotFoundError(f"Background host table not found: {bg_path}")
    if not joint_path.is_file():
        raise FileNotFoundError(f"Joint theta grid not found: {joint_path}")

    print(f"[external_cosmo_host_H6] Host background table: {bg_path}")
    print(f"[external_cosmo_host_H6] Joint theta grid:     {joint_path}")

    df_bg = pd.read_csv(bg_path)
    df_joint = pd.read_csv(joint_path)

    required_bg = ["theta_index", "age_Gyr_host"]
    required_joint = ["theta_index", "age_Gyr", "omega_lambda", "frw_viable", "in_toy_corridor"]

    missing_bg = [c for c in required_bg if c not in df_bg.columns]
    missing_joint = [c for c in required_joint if c not in df_joint.columns]

    if missing_bg:
        raise RuntimeError(f"Missing required columns in host background table: {missing_bg}")
    if missing_joint:
        raise RuntimeError(f"Missing required columns in joint theta grid: {missing_joint}")

    df = pd.merge(
        df_bg[required_bg],
        df_joint[required_joint],
        on="theta_index",
        how="inner",
        validate="one_to_one",
    )

    df = df.rename(
        columns={
            "age_Gyr": "age_Gyr_repo",
            "omega_lambda": "omega_lambda_repo",
        }
    )

    n_total = len(df)
    print(f"[external_cosmo_host_H6] Joined rows: {n_total}")

    # Ensure masks are boolean
    df["frw_viable"] = df["frw_viable"].astype(bool)
    df["in_toy_corridor"] = df["in_toy_corridor"].astype(bool)

    age_host = df["age_Gyr_host"].to_numpy()
    age_repo = df["age_Gyr_repo"].to_numpy()
    omega_repo = df["omega_lambda_repo"].to_numpy()
    mask_frw = df["frw_viable"].to_numpy()
    mask_corr = df["in_toy_corridor"].to_numpy()

    # Base window: [13.3, 14.3] Gyr => center 13.8, half-width 0.5
    base_center = 13.8
    base_half = 0.5

    # Scales: half-width = base_half * scale
    # e.g. 0.5 => very tight, 1.0 => original, 1.5–2.0 => relaxed.
    scales: List[float] = [0.5, 1.0, 1.5, 2.0]

    rows: List[Dict] = []

    def summarize(mask: np.ndarray, set_name: str, scale: float, age_min: float, age_max: float) -> None:
        n_set = int(mask.sum())
        frac = n_set / n_total if n_total > 0 else np.nan

        if n_set == 0:
            row = {
                "scale": scale,
                "age_min_Gyr": age_min,
                "age_max_Gyr": age_max,
                "set": set_name,
                "n_theta": 0,
                "frac_of_grid": 0.0,
                "age_Gyr_host_mean": np.nan,
                "age_Gyr_host_std": np.nan,
                "age_Gyr_repo_mean": np.nan,
                "age_Gyr_repo_std": np.nan,
                "omega_lambda_repo_mean": np.nan,
                "omega_lambda_repo_std": np.nan,
            }
        else:
            ah = age_host[mask]
            ar = age_repo[mask]
            om = omega_repo[mask]
            row = {
                "scale": scale,
                "age_min_Gyr": age_min,
                "age_max_Gyr": age_max,
                "set": set_name,
                "n_theta": n_set,
                "frac_of_grid": frac,
                "age_Gyr_host_mean": float(np.mean(ah)),
                "age_Gyr_host_std": float(np.std(ah, ddof=0)),
                "age_Gyr_repo_mean": float(np.mean(ar)),
                "age_Gyr_repo_std": float(np.std(ar, ddof=0)),
                "omega_lambda_repo_mean": float(np.mean(om)),
                "omega_lambda_repo_std": float(np.std(om, ddof=0)),
            }

        rows.append(row)

    for scale in scales:
        half = base_half * scale
        age_min = base_center - half
        age_max = base_center + half

        mask_window = (age_host >= age_min) & (age_host <= age_max)
        mask_host = mask_window
        mask_frw_host = mask_window & mask_frw
        mask_corr_frw_host = mask_window & mask_frw & mask_corr

        print(
            f"[external_cosmo_host_H6] scale={scale:0.2f} | "
            f"age_window=[{age_min:0.3f}, {age_max:0.3f}] Gyr | "
            f"HOST_WINDOW n={int(mask_host.sum())}, "
            f"FRW∧HOST n={int(mask_frw_host.sum())}, "
            f"CORR∧FRW∧HOST n={int(mask_corr_frw_host.sum())}"
        )

        summarize(mask_host, "HOST_WINDOW", scale, age_min, age_max)
        summarize(mask_frw_host, "FRW_VIABLE_AND_HOST_WINDOW", scale, age_min, age_max)
        summarize(
            mask_corr_frw_host,
            "CORRIDOR_AND_VIABLE_AND_HOST_WINDOW",
            scale,
            age_min,
            age_max,
        )

    out_path = (
        repo_root
        / "stage2"
        / "external_cosmo_host"
        / "outputs"
        / "tables"
        / "stage2_external_cosmo_host_age_window_sensitivity_v1.csv"
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_df = pd.DataFrame(rows)
    out_df.to_csv(out_path, index=False)
    print(f"[external_cosmo_host_H6] Sensitivity summary written: {out_path}")


if __name__ == "__main__":
    main()
