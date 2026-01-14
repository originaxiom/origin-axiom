#!/usr/bin/env python3
"""
Stage2 / external_cosmo_host / H8:
Flag a near-flat subset in the external-cosmo host background grid and
summarize overlaps with FRW_viable and the FRW toy corridor.

Definition here:
    Omega_tot = Omega_m + Omega_lambda
    near-flat if |Omega_tot - 1| <= tol

Outputs:
    - mask table: stage2_external_cosmo_flat_subset_mask_v1.csv
    - summary:    stage2_external_cosmo_flat_subset_summary_v1.csv
"""

from pathlib import Path
import numpy as np
import pandas as pd


def get_repo_root() -> Path:
    # Same pattern as other Stage2 scripts
    return Path(__file__).resolve().parents[3]


def summarize(df: pd.DataFrame, mask: pd.Series, name: str, n_total: int) -> dict:
    n = int(mask.sum())
    frac = n / float(n_total) if n_total > 0 else np.nan
    sub = df[mask]

    def m(col):
        return float(sub[col].mean()) if n > 0 else np.nan

    def s(col):
        return float(sub[col].std()) if n > 0 else np.nan

    def mn(col):
        return float(sub[col].min()) if n > 0 else np.nan

    def mx(col):
        return float(sub[col].max()) if n > 0 else np.nan

    return {
        "set": name,
        "n_theta": n,
        "frac_of_grid": frac,
        "Omega_tot_mean": m("Omega_tot"),
        "Omega_tot_std": s("Omega_tot"),
        "Omega_tot_min": mn("Omega_tot"),
        "Omega_tot_max": mx("Omega_tot"),
        "age_Gyr_host_mean": m("age_Gyr_host"),
        "age_Gyr_host_std": s("age_Gyr_host"),
        "age_Gyr_host_min": mn("age_Gyr_host"),
        "age_Gyr_host_max": mx("age_Gyr_host"),
        "age_Gyr_repo_mean": m("age_Gyr_repo"),
        "age_Gyr_repo_std": s("age_Gyr_repo"),
        "age_Gyr_repo_min": mn("age_Gyr_repo"),
        "age_Gyr_repo_max": mx("age_Gyr_repo"),
        "omega_lambda_repo_mean": m("omega_lambda_repo"),
        "omega_lambda_repo_std": s("omega_lambda_repo"),
        "omega_lambda_repo_min": mn("omega_lambda_repo"),
        "omega_lambda_repo_max": mx("omega_lambda_repo"),
    }


def main() -> None:
    repo_root = get_repo_root()
    print("[external_cosmo_host_H8] Repo root:", repo_root)

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
    mask_out_path = (
        repo_root
        / "stage2"
        / "external_cosmo_host"
        / "outputs"
        / "tables"
        / "stage2_external_cosmo_flat_subset_mask_v1.csv"
    )
    summary_out_path = (
        repo_root
        / "stage2"
        / "external_cosmo_host"
        / "outputs"
        / "tables"
        / "stage2_external_cosmo_flat_subset_summary_v1.csv"
    )

    if not host_path.is_file():
        raise FileNotFoundError(f"[external_cosmo_host_H8] Host background table not found: {host_path}")
    if not joint_path.is_file():
        raise FileNotFoundError(f"[external_cosmo_host_H8] Joint theta grid not found: {joint_path}")

    # Load host background (Omega_m, Omega_lambda, age_Gyr_host)
    host_df = pd.read_csv(host_path)
    required_host_cols = ["theta_index", "Omega_m", "Omega_lambda", "age_Gyr_host"]
    missing_host = [c for c in required_host_cols if c not in host_df.columns]
    if missing_host:
        raise RuntimeError(f"[external_cosmo_host_H8] Missing columns in host background table: {missing_host}")

    # Compute Omega_tot
    host_df["Omega_tot"] = host_df["Omega_m"] + host_df["Omega_lambda"]

    # Load joint theta grid for repo age and toy corridor info
    joint_df = pd.read_csv(joint_path)
    required_joint_cols = ["theta_index", "omega_lambda", "age_Gyr", "frw_viable", "in_toy_corridor"]
    missing_joint = [c for c in required_joint_cols if c not in joint_df.columns]
    if missing_joint:
        raise RuntimeError(f"[external_cosmo_host_H8] Missing columns in joint grid table: {missing_joint}")

    # Join on theta_index
    df = pd.merge(
        host_df,
        joint_df[["theta_index", "omega_lambda", "age_Gyr", "frw_viable", "in_toy_corridor"]],
        on="theta_index",
        how="inner",
        validate="one_to_one",
    ).rename(
        columns={
            "omega_lambda": "omega_lambda_repo",
            "age_Gyr": "age_Gyr_repo",
        }
    )

    n_total = len(df)
    print(f"[external_cosmo_host_H8] Joined rows: {n_total}")

    # Define near-flat mask
    tol = 0.05  # |Omega_tot - 1| <= 0.05
    df["is_near_flat"] = np.abs(df["Omega_tot"] - 1.0) <= tol
    n_flat = int(df["is_near_flat"].sum())
    print(
        f"[external_cosmo_host_H8] Near-flat definition: |Omega_tot - 1| <= {tol:.3f} "
        f"=> n={n_flat}, frac={n_flat / n_total:.6f}"
    )

    # Build masks for subsets
    mask_all = np.ones(n_total, dtype=bool)
    mask_flat = df["is_near_flat"]
    mask_frw = df["frw_viable"].fillna(False)
    mask_corr = df["in_toy_corridor"].fillna(False)

    mask_flat_frw = mask_flat & mask_frw
    mask_flat_frw_corr = mask_flat & mask_frw & mask_corr

    # Summaries
    rows = []
    rows.append(summarize(df, mask_all, "ALL_GRID", n_total))
    rows.append(summarize(df, mask_flat, "HOST_NEAR_FLAT", n_total))
    rows.append(summarize(df, mask_flat_frw, "HOST_NEAR_FLAT_AND_FRW_VIABLE", n_total))
    rows.append(
        summarize(
            df,
            mask_flat_frw_corr,
            "HOST_NEAR_FLAT_AND_CORRIDOR_AND_FRW_VIABLE",
            n_total,
        )
    )

    summary_df = pd.DataFrame(rows)
    summary_out_path.parent.mkdir(parents=True, exist_ok=True)
    summary_df.to_csv(summary_out_path, index=False)
    print(f"[external_cosmo_host_H8] Summary written:", summary_out_path)

    # Mask table (one row per theta_index with the key flags)
    mask_df = df[
        [
            "theta_index",
            "Omega_m",
            "Omega_lambda",
            "Omega_tot",
            "omega_lambda_repo",
            "age_Gyr_repo",
            "age_Gyr_host",
            "frw_viable",
            "in_toy_corridor",
            "is_near_flat",
        ]
    ].copy()
    mask_out_path.parent.mkdir(parents=True, exist_ok=True)
    mask_df.to_csv(mask_out_path, index=False)
    print(f"[external_cosmo_host_H8] Mask table written:", mask_out_path)


if __name__ == "__main__":
    main()
