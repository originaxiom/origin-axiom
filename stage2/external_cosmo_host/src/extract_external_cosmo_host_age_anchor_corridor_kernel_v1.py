#!/usr/bin/env python3
"""
H5: Extract external-cosmo host age-anchor corridor kernel

Goal:
  - Take the external-cosmo host age-anchor mask (H4) and the joint theta grid.
  - Identify the triple-overlap:
        HOST_AGE_ANCHOR ∧ FRW_VIABLE ∧ TOY_CORRIDOR
    which H4 found to be ~12 points.
  - Write those points to a dedicated kernel table with FRW + host + mech columns.
  - Print a compact summary (theta range, omega_lambda ranges, ages, mech means).

We DO NOT assume specific column names for the host-anchor flag anymore.
Instead, we reconstruct the host age-anchor as:
    13.3 Gyr <= age_Gyr_host <= 14.3 Gyr
using the same window as H4.
"""

from pathlib import Path
import pandas as pd
import numpy as np


# Host age-anchor window [Gyr] (must match H4)
HOST_AGE_MIN = 13.3
HOST_AGE_MAX = 14.3


def main() -> None:
    here = Path(__file__).resolve()
    repo_root = here.parents[3]

    joint_path = (
        repo_root
        / "stage2"
        / "joint_mech_frw_analysis"
        / "outputs"
        / "tables"
        / "stage2_joint_theta_grid_v1.csv"
    )
    host_mask_path = (
        repo_root
        / "stage2"
        / "external_cosmo_host"
        / "outputs"
        / "tables"
        / "stage2_external_cosmo_host_age_anchor_mask_v1.csv"
    )
    out_path = (
        repo_root
        / "stage2"
        / "external_cosmo_host"
        / "outputs"
        / "tables"
        / "stage2_external_cosmo_host_age_anchor_corridor_kernel_v1.csv"
    )

    print("[external_cosmo_host_H5] Repo root:", repo_root)
    print("[external_cosmo_host_H5] Joint grid:", joint_path)
    print("[external_cosmo_host_H5] Host age-anchor mask:", host_mask_path)

    if not joint_path.is_file():
        raise FileNotFoundError(f"Joint theta grid not found: {joint_path}")
    if not host_mask_path.is_file():
        raise FileNotFoundError(f"Host age-anchor mask not found: {host_mask_path}")

    df_joint = pd.read_csv(joint_path)
    df_host = pd.read_csv(host_mask_path)

    # --- Required columns on host side (keep this minimal & robust) ---
    required_host = [
        "theta_index",
        "theta",
        "omega_lambda_repo",
        "age_Gyr_repo",
        "age_Gyr_host",
        "frw_viable",
        "in_toy_corridor",
    ]
    missing_host = [c for c in required_host if c not in df_host.columns]
    if missing_host:
        raise RuntimeError(
            f"[external_cosmo_host_H5] Missing required columns in host mask: {missing_host}"
        )

    # Optional: if Omega_lambda_host exists, we’ll include it later
    has_Omega_lambda_host = "Omega_lambda_host" in df_host.columns

    # --- Required columns on joint grid (mechanism + FRW toy) ---
    required_joint = [
        "theta_index",
        "theta",
        "omega_lambda",
        "age_Gyr",
        "mech_baseline_A0",
        "mech_baseline_A_floor",
        "mech_baseline_bound",
        "mech_binding_A0",
        "mech_binding_A",
        "mech_binding_bound",
    ]
    missing_joint = [c for c in required_joint if c not in df_joint.columns]
    if missing_joint:
        raise RuntimeError(
            f"[external_cosmo_host_H5] Missing required columns in joint grid: {missing_joint}"
        )

    # --- Merge host + joint on theta_index ---
    df = pd.merge(
        df_host,
        df_joint,
        on="theta_index",
        how="inner",
        suffixes=("", "_joint"),
    )

    n_total = len(df)
    print(f"[external_cosmo_host_H5] Joined rows: {n_total}")

    # --- Reconstruct masks ---
    # Host age-anchor flag based ONLY on age_Gyr_host and the known window
    age_host = df["age_Gyr_host"].astype(float)
    mask_host_anchor = (age_host >= HOST_AGE_MIN) & (age_host <= HOST_AGE_MAX)

    # FRW viability + corridor flags come directly from the host mask columns
    mask_viable = df["frw_viable"].astype(bool)
    mask_corr = df["in_toy_corridor"].astype(bool)

    mask_kernel = mask_host_anchor & mask_viable & mask_corr
    df_kernel = df.loc[mask_kernel].copy()
    n_kernel = len(df_kernel)
    print(
        "[external_cosmo_host_H5] Kernel size "
        "(HOST_AGE_ANCHOR ∧ FRW_VIABLE ∧ TOY_CORRIDOR): "
        f"n={n_kernel}"
    )

    if n_kernel == 0:
        print("[external_cosmo_host_H5] WARNING: kernel is empty; nothing to write.")
        return

    # Sort by theta_index for readability
    df_kernel.sort_values("theta_index", inplace=True)

    # --- Columns to keep in kernel table ---
    keep_cols = [
        "theta_index",
        "theta",  # host-side theta (should match joint)
        "omega_lambda_repo",
        "age_Gyr_repo",
        "age_Gyr_host",
        "omega_lambda",      # repo FRW toy
        "age_Gyr",           # repo FRW toy
        "frw_viable",
        "in_toy_corridor",
        "mech_baseline_A0",
        "mech_baseline_A_floor",
        "mech_baseline_bound",
        "mech_binding_A0",
        "mech_binding_A",
        "mech_binding_bound",
    ]

    if has_Omega_lambda_host:
        keep_cols.insert(3, "Omega_lambda_host")  # place it near omega_lambda_repo

    missing_keep = [c for c in keep_cols if c not in df_kernel.columns]
    if missing_keep:
        raise RuntimeError(
            f"[external_cosmo_host_H5] Kernel is missing expected columns: {missing_keep}"
        )

    out_path.parent.mkdir(parents=True, exist_ok=True)
    df_kernel[keep_cols].to_csv(out_path, index=False)
    print(f"[external_cosmo_host_H5] Kernel table written:", out_path)

    # --- Compact summary over the kernel ---
    theta_min = float(df_kernel["theta"].min())
    theta_max = float(df_kernel["theta"].max())

    omega_repo_min = float(df_kernel["omega_lambda_repo"].min())
    omega_repo_max = float(df_kernel["omega_lambda_repo"].max())

    if has_Omega_lambda_host:
        omega_host_min = float(df_kernel["Omega_lambda_host"].min())
        omega_host_max = float(df_kernel["Omega_lambda_host"].max())
    else:
        omega_host_min = np.nan
        omega_host_max = np.nan

    age_repo_mean = float(df_kernel["age_Gyr_repo"].mean())
    age_repo_std = float(df_kernel["age_Gyr_repo"].std(ddof=0))
    age_host_mean = float(df_kernel["age_Gyr_host"].mean())
    age_host_std = float(df_kernel["age_Gyr_host"].std(ddof=0))

    mech_cols = [
        "mech_baseline_A0",
        "mech_baseline_A_floor",
        "mech_baseline_bound",
        "mech_binding_A0",
        "mech_binding_A",
        "mech_binding_bound",
    ]

    print(
        "[external_cosmo_host_H5] Kernel theta-range: "
        f"[{theta_min:.6f}, {theta_max:.6f}] (n={n_kernel})"
    )
    print(
        "[external_cosmo_host_H5] Kernel omega_lambda (repo) range: "
        f"[{omega_repo_min:.6f}, {omega_repo_max:.6f}]"
    )
    if has_Omega_lambda_host:
        print(
            "[external_cosmo_host_H5] Kernel Omega_lambda (host) range: "
            f"[{omega_host_min:.6f}, {omega_host_max:.6f}]"
        )
    else:
        print("[external_cosmo_host_H5] Kernel Omega_lambda (host): not available in mask")

    print("[external_cosmo_host_H5] Kernel ages:")
    print(f"  repo toy age:  mean={age_repo_mean:.3f} Gyr, std={age_repo_std:.3f} Gyr")
    print(f"  host age:      mean={age_host_mean:.3f} Gyr, std={age_host_std:.3f} Gyr")

    print("[external_cosmo_host_H5] Kernel mechanism profiles:")
    for col in mech_cols:
        mean = float(df_kernel[col].mean())
        std = float(df_kernel[col].std(ddof=0))
        col_min = float(df_kernel[col].min())
        col_max = float(df_kernel[col].max())
        print(
            f"  {col}: mean={mean:.9f}, std={std:.9f}, "
            f"min={col_min:.9f}, max={col_max:.9f}"
        )


if __name__ == "__main__":
    main()
