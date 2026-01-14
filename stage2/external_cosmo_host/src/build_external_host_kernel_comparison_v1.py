#!/usr/bin/env python
"""
Stage2 / external_cosmo_host / H7:
Build a compact comparison table for three kernels:

1) FRW_TOY_ANCHOR_KERNEL
2) EXTERNAL_FRW_HOST_AGE_ANCHOR
3) EXTERNAL_COSMO_HOST_AGE_CORRIDOR_KERNEL
"""

from pathlib import Path
import numpy as np
import pandas as pd


def repo_root_from_file() -> Path:
    return Path(__file__).resolve().parents[3]


def safe_stats(df: pd.DataFrame, col: str | None):
    if col is None or col not in df.columns:
        return (np.nan, np.nan, np.nan)
    s = pd.to_numeric(df[col], errors="coerce")
    s = s.replace([np.inf, -np.inf], np.nan).dropna()
    if s.empty:
        return (np.nan, np.nan, np.nan)
    return (float(s.mean()), float(s.min()), float(s.max()))


def mech_mean(df: pd.DataFrame, col: str) -> float:
    if col not in df.columns:
        return float("nan")
    s = pd.to_numeric(df[col], errors="coerce")
    s = s.replace([np.inf, -np.inf], np.nan).dropna()
    if s.empty:
        return float("nan")
    return float(s.mean())


def summarize_kernel(
    label: str,
    df: pd.DataFrame,
    theta_col: str,
    omega_col: str,
    age_repo_col: str,
    age_host_frw_col: str | None = None,
    age_host_cosmo_col: str | None = None,
):
    n_theta = int(len(df))

    theta_mean, theta_min, theta_max = safe_stats(df, theta_col)
    omega_mean, omega_min, omega_max = safe_stats(df, omega_col)

    age_repo_mean, age_repo_min, age_repo_max = safe_stats(df, age_repo_col)
    age_host_frw_mean, age_host_frw_min, age_host_frw_max = safe_stats(
        df, age_host_frw_col
    )
    age_host_cosmo_mean, age_host_cosmo_min, age_host_cosmo_max = safe_stats(
        df, age_host_cosmo_col
    )

    baseline_mean = mech_mean(df, "mech_baseline_A0")
    binding_mean = mech_mean(df, "mech_binding_A0")

    return {
        "set_name": label,
        "n_theta": n_theta,
        "theta_min": theta_min,
        "theta_max": theta_max,
        "omega_lambda_mean": omega_mean,
        "omega_lambda_min": omega_min,
        "omega_lambda_max": omega_max,
        "age_repo_mean": age_repo_mean,
        "age_repo_min": age_repo_min,
        "age_repo_max": age_repo_max,
        "age_host_frw_mean": age_host_frw_mean,
        "age_host_frw_min": age_host_frw_min,
        "age_host_frw_max": age_host_frw_max,
        "age_host_cosmo_mean": age_host_cosmo_mean,
        "age_host_cosmo_min": age_host_cosmo_min,
        "age_host_cosmo_max": age_host_cosmo_max,
        "mech_baseline_A0_mean": baseline_mean,
        "mech_binding_A0_mean": binding_mean,
    }


def main():
    repo_root = repo_root_from_file()
    print("[external_cosmo_host_H7] Repo root:", repo_root)

    frw_kernel_path = (
        repo_root
        / "stage2"
        / "joint_mech_frw_analysis"
        / "outputs"
        / "tables"
        / "stage2_joint_mech_frw_anchor_kernel_v1.csv"
    )
    frw_host_age_mask_path = (
        repo_root
        / "stage2"
        / "external_frw_host"
        / "outputs"
        / "tables"
        / "stage2_external_frw_host_age_anchor_mask_v1.csv"
    )
    cosmo_kernel_path = (
        repo_root
        / "stage2"
        / "external_cosmo_host"
        / "outputs"
        / "tables"
        / "stage2_external_cosmo_host_age_anchor_corridor_kernel_v1.csv"
    )

    for p in [frw_kernel_path, frw_host_age_mask_path, cosmo_kernel_path]:
        if not p.exists():
            raise FileNotFoundError(f"[external_cosmo_host_H7] Missing expected input: {p}")

    frw_df = pd.read_csv(frw_kernel_path)
    host_frw_df = pd.read_csv(frw_host_age_mask_path)
    cosmo_df = pd.read_csv(cosmo_kernel_path)

    print(
        "[external_cosmo_host_H7] Input sizes:",
        f"FRW kernel: {len(frw_df)} rows,",
        f"FRW host age-anchor mask: {len(host_frw_df)} rows,",
        f"cosmo-host corridor kernel: {len(cosmo_df)} rows",
    )

    rows: list[dict] = []

    # 1) Internal FRW toy anchor kernel
    #    NB: this kernel file is a 2-row segment summary, so many stats will be NaN;
    #    that's acceptable as a placeholder until we add a per-theta kernel table.
    rows.append(
        summarize_kernel(
            label="FRW_TOY_ANCHOR_KERNEL",
            df=frw_df,
            theta_col="theta",          # if missing, stats become NaN
            omega_col="omega_lambda",   # likewise
            age_repo_col="age_Gyr",
            age_host_frw_col=None,
            age_host_cosmo_col=None,
        )
    )

    # 2) External FRW host age-anchor subset only
    anchor_col = "in_host_age_anchor_box"
    if anchor_col not in host_frw_df.columns:
        raise RuntimeError(
            f"[external_cosmo_host_H7] Expected column '{anchor_col}' "
            f"in host age-anchor mask table."
        )
    host_frw_anchor_df = host_frw_df[host_frw_df[anchor_col].astype(bool)].copy()
    print(
        "[external_cosmo_host_H7] FRW host age-anchor subset size:",
        len(host_frw_anchor_df),
    )

    rows.append(
        summarize_kernel(
            label="EXTERNAL_FRW_HOST_AGE_ANCHOR",
            df=host_frw_anchor_df,
            theta_col="theta",
            omega_col="omega_lambda",
            age_repo_col="age_Gyr",        # may be absent; then will show NaN
            age_host_frw_col="age_Gyr_host",
            age_host_cosmo_col=None,
        )
    )

    # 3) External cosmo-host age–corridor kernel (12-point θ band)
    rows.append(
        summarize_kernel(
            label="EXTERNAL_COSMO_HOST_AGE_CORRIDOR_KERNEL",
            df=cosmo_df,
            theta_col="theta",
            omega_col="omega_lambda_repo",
            age_repo_col="age_Gyr_repo",
            age_host_frw_col=None,
            age_host_cosmo_col="age_Gyr_host",
        )
    )

    out_path = (
        repo_root
        / "stage2"
        / "external_cosmo_host"
        / "outputs"
        / "tables"
        / "stage2_external_host_kernel_comparison_v1.csv"
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_df = pd.DataFrame(rows)
    out_df.to_csv(out_path, index=False)

    print("[external_cosmo_host_H7] Comparison table written:", out_path)
    print("[external_cosmo_host_H7] Summary:")
    print(out_df.to_string(index=False))


if __name__ == "__main__":
    main()
