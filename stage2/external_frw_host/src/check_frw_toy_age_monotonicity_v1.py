#!/usr/bin/env python3
"""
stage2/external_frw_host/src/check_frw_toy_age_monotonicity_v1.py

Diagnostic: how does the Phase 4 FRW toy age behave as a function of omega_lambda,
especially on the FRW-viable set?

- Reads: phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv
- Restricts to frw_viable == 1
- Sorts by omega_lambda
- Computes finite-difference gradients of age_Gyr vs omega_lambda
- Summarises sign structure and magnitudes
- Writes: stage2/external_frw_host/outputs/tables/stage2_external_frw_rung5_toy_age_monotonicity_v1.csv
"""

import sys
from pathlib import Path

import numpy as np
import pandas as pd


def find_repo_root() -> Path:
    """
    Infer repo root from this file location by walking up the parents
    until we find something that looks like the origin-axiom root
    (e.g. containing 'phase4' and 'stage2').
    """
    here = Path(__file__).resolve()
    for p in here.parents:
        if (p / "phase4").is_dir() and (p / "stage2").is_dir():
            return p
    raise RuntimeError("Could not locate repo root from script location.")


def main() -> None:
    repo_root = find_repo_root()
    frw_table = repo_root / "phase4" / "outputs" / "tables" / "phase4_F1_frw_shape_probe_mask.csv"
    out_dir = repo_root / "stage2" / "external_frw_host" / "outputs" / "tables"
    out_path = out_dir / "stage2_external_frw_rung5_toy_age_monotonicity_v1.csv"

    print("[external_frw_host_rung5_age_monotonicity]")
    print(f"  Repo root: {repo_root}")
    print(f"  FRW toy table: {frw_table}")

    if not frw_table.exists():
        raise FileNotFoundError(f"FRW toy table not found: {frw_table}")

    df = pd.read_csv(frw_table)

    # We only need these columns for the diagnostic
    required_cols = ["theta", "omega_lambda", "age_Gyr", "frw_viable"]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise RuntimeError(f"Missing required columns in FRW toy table: {missing}")

    n_total = len(df)
    print(f"  Total rows: {n_total}")

    # Restrict to FRW-viable set for the main monotonicity check
    df_v = df[df["frw_viable"] == 1].copy()
    n_viable = len(df_v)
    print(f"  FRW-viable rows: {n_viable}")

    if n_viable < 3:
        raise RuntimeError("Not enough FRW-viable points to assess monotonicity.")

    # Sort by omega_lambda
    df_v = df_v.sort_values("omega_lambda").reset_index(drop=True)

    omega = df_v["omega_lambda"].to_numpy()
    age = df_v["age_Gyr"].to_numpy()

    # Finite-difference gradients: d(age)/d(omega) with simple forward differences
    d_omega = np.diff(omega)
    d_age = np.diff(age)

    # To avoid division by tiny numbers, only keep steps where |d_omega| is > eps
    eps = 1e-10
    mask_step = np.abs(d_omega) > eps
    if not np.any(mask_step):
        raise RuntimeError("All omega_lambda steps are effectively zero; cannot assess monotonicity.")

    d_omega_eff = d_omega[mask_step]
    d_age_eff = d_age[mask_step]
    grad = d_age_eff / d_omega_eff

    # Sign structure
    signs = np.sign(grad)
    n_pos = int(np.sum(signs > 0))
    n_neg = int(np.sum(signs < 0))
    n_zero = int(np.sum(signs == 0))

    # Basic stats
    grad_mean = float(np.mean(grad))
    grad_std = float(np.std(grad))
    grad_min = float(np.min(grad))
    grad_max = float(np.max(grad))

    abs_grad = np.abs(grad)
    abs_grad_mean = float(np.mean(abs_grad))
    abs_grad_p95 = float(np.percentile(abs_grad, 95.0))
    abs_grad_max = float(np.max(abs_grad))

    print("  Monotonicity summary on FRW-viable set (sorted by omega_lambda):")
    print(f"    steps used: {len(grad)} (out of {len(d_omega)})")
    print(f"    n_pos: {n_pos}, n_neg: {n_neg}, n_zero: {n_zero}")
    print(f"    grad_mean: {grad_mean:.6e}, grad_std: {grad_std:.6e}")
    print(f"    grad_min: {grad_min:.6e}, grad_max: {grad_max:.6e}")
    print(f"    abs_grad_mean: {abs_grad_mean:.6e}, abs_grad_p95: {abs_grad_p95:.6e}, abs_grad_max: {abs_grad_max:.6e}")

    # Build a one-row summary table so Stage 2 can consume this in a reproducible way
    row = {
        "set": "FRW_VIABLE_sorted_by_omega_lambda",
        "n_theta": n_viable,
        "n_steps": len(grad),
        "n_pos": n_pos,
        "n_neg": n_neg,
        "n_zero": n_zero,
        "grad_mean": grad_mean,
        "grad_std": grad_std,
        "grad_min": grad_min,
        "grad_max": grad_max,
        "abs_grad_mean": abs_grad_mean,
        "abs_grad_p95": abs_grad_p95,
        "abs_grad_max": abs_grad_max,
        "omega_lambda_min": float(omega.min()),
        "omega_lambda_max": float(omega.max()),
        "age_Gyr_min": float(age.min()),
        "age_Gyr_max": float(age.max()),
    }

    out_dir.mkdir(parents=True, exist_ok=True)
    pd.DataFrame([row]).to_csv(out_path, index=False)
    print(f"  Summary written: {out_path}")


if __name__ == "__main__":
    main()
