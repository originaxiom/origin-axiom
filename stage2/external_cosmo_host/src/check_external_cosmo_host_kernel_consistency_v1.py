#!/usr/bin/env python3
"""
Stage 2 / external_cosmo_host – H9 consistency check for the age∧corridor kernel.

Checks that the 12-point EXTERNAL_COSMO_HOST_AGE_CORRIDOR_KERNEL:

- is entirely FRW-viable in the Phase-4 toy,
- lies inside the Phase-4 toy corridor,
- lies inside the near-flat host subset (|Omega_tot - 1| <= 0.05),
- has small and well-behaved age differences between repo toy ages and host ages,
- has small differences between repo omega_lambda and the kernel (joint-grid) omega_lambda.

Outputs a one-row CSV summary for Phase 4/5 dashboards.
"""

import pathlib
import pandas as pd


def require_columns(df: pd.DataFrame, cols, name: str):
    missing = [c for c in cols if c not in df.columns]
    if missing:
        raise RuntimeError(f"[external_cosmo_host_H9] Missing columns in {name}: {missing}")


def main() -> None:
    # Resolve repo root (…/origin-axiom)
    repo_root = pathlib.Path(__file__).resolve().parents[3]
    print("[external_cosmo_host_H9] Repo root:", repo_root)

    kernel_path = (
        repo_root
        / "stage2"
        / "external_cosmo_host"
        / "outputs"
        / "tables"
        / "stage2_external_cosmo_host_age_anchor_corridor_kernel_v1.csv"
    )
    flat_mask_path = (
        repo_root
        / "stage2"
        / "external_cosmo_host"
        / "outputs"
        / "tables"
        / "stage2_external_cosmo_flat_subset_mask_v1.csv"
    )
    out_path = (
        repo_root
        / "stage2"
        / "external_cosmo_host"
        / "outputs"
        / "tables"
        / "stage2_external_cosmo_host_kernel_consistency_v1.csv"
    )

    print("[external_cosmo_host_H9] Cosmo host kernel:", kernel_path)
    print("[external_cosmo_host_H9] Near-flat mask:", flat_mask_path)

    kernel_df = pd.read_csv(kernel_path)
    flat_df = pd.read_csv(flat_mask_path)

    # Kernel: already carries joint-grid info (omega_lambda, age_Gyr, frw_viable, in_toy_corridor)
    require_columns(
        kernel_df,
        [
            "theta_index",
            "theta",
            "omega_lambda_repo",
            "age_Gyr_repo",
            "age_Gyr_host",
            "omega_lambda",
            "age_Gyr",
            "frw_viable",
            "in_toy_corridor",
        ],
        "cosmo host kernel",
    )

    # Near-flat mask: Omega_tot and near-flat flag
    require_columns(
        flat_df,
        ["theta_index", "Omega_tot", "is_near_flat"],
        "near-flat host mask",
    )

    n_kernel = len(kernel_df)
    print(f"[external_cosmo_host_H9] Kernel size (rows): {n_kernel}")

    # Join kernel with near-flat mask
    flat_cols = ["theta_index", "Omega_tot", "is_near_flat"]
    merged = kernel_df.merge(flat_df[flat_cols], on="theta_index", how="left")

    # Check that every kernel theta_index appears in the near-flat mask
    if merged["Omega_tot"].isna().any() or merged["is_near_flat"].isna().any():
        missing = merged[merged["Omega_tot"].isna() | merged["is_near_flat"].isna()][
            "theta_index"
        ].tolist()
        raise RuntimeError(
            f"[external_cosmo_host_H9] Some kernel theta_index values are missing from near-flat mask: {missing}"
        )

    # Basic counts / logical checks
    n_frw_viable = int(kernel_df["frw_viable"].sum())
    n_in_corridor = int(kernel_df["in_toy_corridor"].sum())
    n_near_flat = int(merged["is_near_flat"].sum())

    all_frw_viable = (n_frw_viable == n_kernel)
    all_in_corridor = (n_in_corridor == n_kernel)
    all_near_flat = (n_near_flat == n_kernel)

    print(
        f"[external_cosmo_host_H9] FRW-viable in kernel: {n_frw_viable}/{n_kernel} "
        f"(all={all_frw_viable})"
    )
    print(
        f"[external_cosmo_host_H9] In toy corridor in kernel: {n_in_corridor}/{n_kernel} "
        f"(all={all_in_corridor})"
    )
    print(
        f"[external_cosmo_host_H9] Near-flat host in kernel: {n_near_flat}/{n_kernel} "
        f"(all={all_near_flat})"
    )

    # Age and omega deltas
    age_diff = merged["age_Gyr_host"] - merged["age_Gyr_repo"]
    age_abs = age_diff.abs()

    omega_diff = merged["omega_lambda_repo"] - merged["omega_lambda"]
    omega_abs = omega_diff.abs()

    def stats(arr: pd.Series, name: str):
        return {
            f"{name}_mean": float(arr.mean()),
            f"{name}_std": float(arr.std(ddof=0)),
            f"{name}_min": float(arr.min()),
            f"{name}_max": float(arr.max()),
        }

    age_stats = stats(age_diff, "age_diff_Gyr")
    age_abs_stats = stats(age_abs, "age_abs_diff_Gyr")
    omega_stats = stats(omega_diff, "omega_lambda_diff")
    omega_abs_stats = stats(omega_abs, "omega_lambda_abs_diff")

    print(
        "[external_cosmo_host_H9] Age differences (host - repo) [Gyr]: "
        f"mean={age_stats['age_diff_Gyr_mean']:.3f}, "
        f"min={age_stats['age_diff_Gyr_min']:.3f}, "
        f"max={age_stats['age_diff_Gyr_max']:.3f}"
    )
    print(
        "[external_cosmo_host_H9] |Age difference| [Gyr]: "
        f"mean={age_abs_stats['age_abs_diff_Gyr_mean']:.3f}, "
        f"min={age_abs_stats['age_abs_diff_Gyr_min']:.3f}, "
        f"max={age_abs_stats['age_abs_diff_Gyr_max']:.3f}"
    )
    print(
        "[external_cosmo_host_H9] Omega_lambda differences (repo - kernel): "
        f"mean={omega_stats['omega_lambda_diff_mean']:.6f}, "
        f"min={omega_stats['omega_lambda_diff_min']:.6f}, "
        f"max={omega_stats['omega_lambda_diff_max']:.6f}"
    )
    print(
        "[external_cosmo_host_H9] |Omega_lambda difference|: "
        f"mean={omega_abs_stats['omega_lambda_abs_diff_mean']:.6f}, "
        f"min={omega_abs_stats['omega_lambda_abs_diff_min']:.6f}, "
        f"max={omega_abs_stats['omega_lambda_abs_diff_max']:.6f}"
    )

    summary = {
        "n_kernel": n_kernel,
        "n_frw_viable": n_frw_viable,
        "n_in_corridor": n_in_corridor,
        "n_near_flat": n_near_flat,
        "all_frw_viable": all_frw_viable,
        "all_in_corridor": all_in_corridor,
        "all_near_flat": all_near_flat,
    }
    summary.update(age_stats)
    summary.update(age_abs_stats)
    summary.update(omega_stats)
    summary.update(omega_abs_stats)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame([summary]).to_csv(out_path, index=False)
    print("[external_cosmo_host_H9] Summary written:", out_path)


if __name__ == "__main__":
    main()
