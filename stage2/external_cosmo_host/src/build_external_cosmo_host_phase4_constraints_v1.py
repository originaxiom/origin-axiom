#!/usr/bin/env python3
"""
Stage 2 / external_cosmo_host
H10: Build a tiny Phase-4-ready constraints table from the cosmo-host kernel.

Input:
  - stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_age_anchor_corridor_kernel_v1.csv
    (12-point kernel: HOST_AGE_ANCHOR ∧ FRW_VIABLE ∧ TOY_CORRIDOR)

  - stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_background_grid_v1.csv
    (full external ΛCDM background grid with Omega_m, Omega_lambda, age_Gyr_host)

Output:
  - stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_phase4_constraints_v1.csv

This is a *one-row* summary of the kernel:
  - θ-range
  - toy Ω_Λ (repo) range
  - host Ω_Λ range
  - toy age range
  - host age range
  - mechanism band (mech_baseline_A0)
"""

from __future__ import annotations

import pandas as pd
from pathlib import Path


def _stats(series: pd.Series):
    """Return (mean, min, max) as plain floats."""
    s = pd.Series(series).astype(float)
    return float(s.mean()), float(s.min()), float(s.max())


def main() -> None:
    repo_root = Path(__file__).resolve().parents[3]

    kernel_path = (
        repo_root
        / "stage2"
        / "external_cosmo_host"
        / "outputs"
        / "tables"
        / "stage2_external_cosmo_host_age_anchor_corridor_kernel_v1.csv"
    )
    bg_path = (
        repo_root
        / "stage2"
        / "external_cosmo_host"
        / "outputs"
        / "tables"
        / "stage2_external_cosmo_host_background_grid_v1.csv"
    )
    out_path = (
        repo_root
        / "stage2"
        / "external_cosmo_host"
        / "outputs"
        / "tables"
        / "stage2_external_cosmo_host_phase4_constraints_v1.csv"
    )

    print("[external_cosmo_host_H10] Repo root:", repo_root)
    print("[external_cosmo_host_H10] Kernel table:", kernel_path)
    print("[external_cosmo_host_H10] Background grid:", bg_path)

    if not kernel_path.is_file():
        raise FileNotFoundError(
            f"[external_cosmo_host_H10] Kernel table not found: {kernel_path}"
        )
    if not bg_path.is_file():
        raise FileNotFoundError(
            f"[external_cosmo_host_H10] Background grid not found: {bg_path}"
        )

    kernel = pd.read_csv(kernel_path)
    bg = pd.read_csv(bg_path)

    # Sanity checks on expected columns
    required_kernel_cols = [
        "theta_index",
        "theta",
        "omega_lambda_repo",
        "age_Gyr_repo",
        "age_Gyr_host",
        "mech_baseline_A0",
    ]
    missing_kernel = [c for c in required_kernel_cols if c not in kernel.columns]
    if missing_kernel:
        raise RuntimeError(
            f"[external_cosmo_host_H10] Missing required columns in kernel table: "
            f"{missing_kernel}"
        )

    required_bg_cols = ["theta_index", "Omega_lambda"]
    missing_bg = [c for c in required_bg_cols if c not in bg.columns]
    if missing_bg:
        raise RuntimeError(
            f"[external_cosmo_host_H10] Missing required columns in background grid: "
            f"{missing_bg}"
        )

    n_kernel = len(kernel)
    print(f"[external_cosmo_host_H10] Kernel rows: {n_kernel}")
    if n_kernel == 0:
        raise RuntimeError("[external_cosmo_host_H10] Kernel is empty; nothing to summarize.")

    # Join in host Omega_lambda via theta_index
    bg_small = bg[["theta_index", "Omega_lambda"]].copy()
    merged = kernel.merge(
        bg_small,
        on="theta_index",
        how="left",
        validate="one_to_one",
    )

    if merged["Omega_lambda"].isna().any():
        n_na = int(merged["Omega_lambda"].isna().sum())
        raise RuntimeError(
            f"[external_cosmo_host_H10] Missing Omega_lambda for {n_na} kernel rows after join."
        )

    # Basic θ range
    theta_min = float(merged["theta"].min())
    theta_max = float(merged["theta"].max())

    # Toy / repo Ω_Λ stats
    omega_repo_mean, omega_repo_min, omega_repo_max = _stats(merged["omega_lambda_repo"])

    # Host Ω_Λ stats
    Omega_host_mean, Omega_host_min, Omega_host_max = _stats(merged["Omega_lambda"])

    # Toy age stats
    age_repo_mean, age_repo_min, age_repo_max = _stats(merged["age_Gyr_repo"])

    # Host age stats
    age_host_mean, age_host_min, age_host_max = _stats(merged["age_Gyr_host"])

    # Mechanism band stats
    mech_mean, mech_min, mech_max = _stats(merged["mech_baseline_A0"])

    row = {
        "kernel_name": "EXTERNAL_COSMO_HOST_AGE_CORRIDOR_KERNEL",
        "n_theta": int(n_kernel),
        "theta_min": theta_min,
        "theta_max": theta_max,
        "omega_lambda_repo_mean": omega_repo_mean,
        "omega_lambda_repo_min": omega_repo_min,
        "omega_lambda_repo_max": omega_repo_max,
        "Omega_lambda_host_mean": Omega_host_mean,
        "Omega_lambda_host_min": Omega_host_min,
        "Omega_lambda_host_max": Omega_host_max,
        "age_Gyr_repo_mean": age_repo_mean,
        "age_Gyr_repo_min": age_repo_min,
        "age_Gyr_repo_max": age_repo_max,
        "age_Gyr_host_mean": age_host_mean,
        "age_Gyr_host_min": age_host_min,
        "age_Gyr_host_max": age_host_max,
        "mech_baseline_A0_mean": mech_mean,
        "mech_baseline_A0_min": mech_min,
        "mech_baseline_A0_max": mech_max,
    }

    out_df = pd.DataFrame([row])
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_df.to_csv(out_path, index=False)

    print(f"[external_cosmo_host_H10] Constraints table written: {out_path}")
    print("[external_cosmo_host_H10] Row summary:")
    for k, v in row.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
