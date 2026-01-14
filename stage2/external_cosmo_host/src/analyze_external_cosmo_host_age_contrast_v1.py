#!/usr/bin/env python3
"""
Stage 2: external cosmology host belt, H3 age-contrast rung.

Compare the external cosmology host background ages to the repo FRW toy ages
on the common theta-grid, and summarise differences over key subsets.

Inputs:
  - stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv
      (FRW toy + mechanism + masks)
  - stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_background_grid_v1.csv
      (Omega_m, Omega_lambda, H0, age_Gyr_host)

Output:
  - stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_rung3_age_contrast_v1.csv

This is a structural diagnostic only: it checks whether the external host
background age is grossly misaligned with the toy FRW background used in
Phase 4 / Stage 2.
"""

from pathlib import Path
import numpy as np
import pandas as pd


def get_repo_root() -> Path:
    # repo_root/stage2/external_cosmo_host/src/this_script.py
    return Path(__file__).resolve().parents[3]


def load_joint_grid(repo_root: Path) -> pd.DataFrame:
    path = (
        repo_root
        / "stage2"
        / "joint_mech_frw_analysis"
        / "outputs"
        / "tables"
        / "stage2_joint_theta_grid_v1.csv"
    )
    if not path.exists():
        raise FileNotFoundError(f"Joint theta grid not found: {path}")
    df = pd.read_csv(path)
    required = [
        "theta_index",
        "theta",
        "omega_lambda",
        "age_Gyr",
        "frw_viable",
        "in_toy_corridor",
    ]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise RuntimeError(f"Missing required columns in joint grid: {missing}")
    return df


def load_host_background(repo_root: Path) -> pd.DataFrame:
    path = (
        repo_root
        / "stage2"
        / "external_cosmo_host"
        / "outputs"
        / "tables"
        / "stage2_external_cosmo_host_background_grid_v1.csv"
    )
    if not path.exists():
        raise FileNotFoundError(f"Host background grid not found: {path}")
    df = pd.read_csv(path)
    required = [
        "theta_index",
        "theta",
        "Omega_m",
        "Omega_lambda",
        "H0_km_s_Mpc",
        "age_Gyr_host",
    ]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise RuntimeError(f"Missing required columns in host background grid: {missing}")
    return df


def summarize_diff(mask_name: str, df: pd.DataFrame, mask: np.ndarray, n_total: int) -> dict:
    m = mask.astype(bool)
    n = int(m.sum())
    frac = n / float(n_total) if n_total > 0 else np.nan

    if n == 0:
        return {
            "set": mask_name,
            "n_theta": n,
            "frac_of_grid": frac,
            "age_Gyr_diff_mean": np.nan,
            "age_Gyr_diff_std": np.nan,
            "age_Gyr_diff_min": np.nan,
            "age_Gyr_diff_max": np.nan,
            "age_Gyr_rel_diff_mean": np.nan,
            "age_Gyr_rel_diff_std": np.nan,
            "age_Gyr_rel_diff_min": np.nan,
            "age_Gyr_rel_diff_max": np.nan,
        }

    diff = df.loc[m, "age_Gyr_diff"].to_numpy()
    rel = df.loc[m, "age_Gyr_rel_diff"].to_numpy()

    return {
        "set": mask_name,
        "n_theta": n,
        "frac_of_grid": frac,
        "age_Gyr_diff_mean": float(np.nanmean(diff)),
        "age_Gyr_diff_std": float(np.nanstd(diff)),
        "age_Gyr_diff_min": float(np.nanmin(diff)),
        "age_Gyr_diff_max": float(np.nanmax(diff)),
        "age_Gyr_rel_diff_mean": float(np.nanmean(rel)),
        "age_Gyr_rel_diff_std": float(np.nanstd(rel)),
        "age_Gyr_rel_diff_min": float(np.nanmin(rel)),
        "age_Gyr_rel_diff_max": float(np.nanmax(rel)),
    }


def main() -> None:
    repo_root = get_repo_root()
    print(f"[external_cosmo_host_H3] Repo root: {repo_root}")

    df_joint = load_joint_grid(repo_root)
    df_host = load_host_background(repo_root)

    # Join on theta_index; we keep the joint grid as the primary record.
    df = pd.merge(
        df_joint,
        df_host[
            [
                "theta_index",
                "Omega_m",
                "Omega_lambda",
                "H0_km_s_Mpc",
                "age_Gyr_host",
            ]
        ],
        on="theta_index",
        how="inner",
        suffixes=("", "_host"),
    )

    n = len(df)
    if n == 0:
        raise RuntimeError("Join between joint grid and host background produced zero rows.")
    print(f"[external_cosmo_host_H3] Joined rows: {n}")

    # Rename for clarity
    df["age_Gyr_repo"] = df["age_Gyr"].astype(float)
    df["age_Gyr_host"] = df["age_Gyr_host"].astype(float)

    with np.errstate(divide="ignore", invalid="ignore"):
        df["age_Gyr_diff"] = df["age_Gyr_host"] - df["age_Gyr_repo"]
        df["age_Gyr_rel_diff"] = df["age_Gyr_diff"] / df["age_Gyr_repo"]

    # Basic sanity print
    print(
        "[external_cosmo_host_H3] Global diff stats: "
        f"⟨Δage⟩={np.nanmean(df['age_Gyr_diff']):.3f} Gyr, "
        f"⟨Δage/age_repo⟩≈{np.nanmean(np.abs(df['age_Gyr_rel_diff'])):.3f}"
    )

    frw_viable = df["frw_viable"].astype(int) == 1
    in_corr = df["in_toy_corridor"].astype(bool)

    sets = {
        "ALL_GRID": np.ones(n, dtype=bool),
        "FRW_VIABLE": frw_viable,
        "CORRIDOR_AND_VIABLE": frw_viable & in_corr,
    }

    rows = []
    for name, m in sets.items():
        summary = summarize_diff(name, df, m, n)
        rows.append(summary)
        print(
            f"[external_cosmo_host_H3] {name:20s} "
            f"n={summary['n_theta']:4d}, frac={summary['frac_of_grid']:.6f}, "
            f"⟨Δage⟩={summary['age_Gyr_diff_mean']:.3f} Gyr, "
            f"⟨Δage/age_repo⟩≈{summary['age_Gyr_rel_diff_mean']:.3f}"
        )

    out_df = pd.DataFrame(rows)
    out_path = (
        repo_root
        / "stage2"
        / "external_cosmo_host"
        / "outputs"
        / "tables"
        / "stage2_external_cosmo_host_rung3_age_contrast_v1.csv"
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_df.to_csv(out_path, index=False)
    print(f"[external_cosmo_host_H3] Summary written: {out_path}")


if __name__ == "__main__":
    main()
