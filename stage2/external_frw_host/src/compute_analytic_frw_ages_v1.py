#!/usr/bin/env python3
"""
Stage 2 – External FRW host belt (Rung X1):
Analytic flat-FRW age cross-check against the Phase 4 / Stage 2 joint theta grid.

- Input:
    stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv

- Output:
    stage2/external_frw_host/outputs/tables/stage2_external_frw_rung1_age_crosscheck_v1.csv

This script:
  * treats the 'omega_lambda' column as an effective Ω_Λ in a flat FRW background,
  * assumes Ω_m = 1 - Ω_Λ and neglects radiation,
  * computes a dimensionless age t0_dimless(Ω_Λ) via a simple numerical integral,
  * calibrates a single global scale factor so that t0_dimless matches 'age_Gyr'
    on average over the FRW-viable subset, and
  * compares the calibrated analytic ages to the repo ages row-by-row.

All results are Stage 2 diagnostics only; no claims are promoted upstream.
"""

from pathlib import Path

import numpy as np
import pandas as pd


def get_repo_root() -> Path:
    """Resolve repo root from this file location."""
    here = Path(__file__).resolve()
    # .../origin-axiom/stage2/external_frw_host/src/compute_analytic_frw_ages_v1.py
    # parents[0] = src
    # parents[1] = external_frw_host
    # parents[2] = stage2
    # parents[3] = origin-axiom  <-- repo root
    return here.parents[3]


def _trapz_like(y: np.ndarray, x: np.ndarray) -> float:
    """
    Small helper to integrate y(x) with a trapezoidal rule that works across
    NumPy versions. Prefer np.trapezoid if available, otherwise fall back to
    np.trapz.
    """
    if hasattr(np, "trapezoid"):
        return float(np.trapezoid(y, x))
    # Fallback for older NumPy
    if hasattr(np, "trapz"):
        return float(np.trapz(y, x))
    # Extremely defensive: manual trapezoid rule
    dx = np.diff(x)
    avg = 0.5 * (y[:-1] + y[1:])
    return float(np.sum(dx * avg))


def frw_age_dimless_flat(omega_lambda: float, n_a: int = 400) -> float:
    """
    Compute dimensionless FRW age t0 * H0 for a flat background with
      Omega_m = 1 - Omega_lambda, Omega_lambda = omega_lambda,
    ignoring radiation, via:
      t0 * H0 = ∫_0^1 da / (a * sqrt(Ω_m a^{-3} + Ω_Λ)).

    We integrate from a_min to 1 with a simple trapezoidal rule.
    """
    # Guard against pathological inputs
    if omega_lambda < 0.0:
        omega_lambda = 0.0
    if omega_lambda > 1.5:
        omega_lambda = 1.5

    omega_m = max(1.0 - omega_lambda, 1e-6)

    # Avoid a=0 exactly; start at a_min.
    a_min = 1e-4
    a_max = 1.0
    a = np.linspace(a_min, a_max, n_a)

    # H(a)/H0 = sqrt(Ω_m a^{-3} + Ω_Λ)
    Ha_over_H0 = np.sqrt(omega_m * a**-3 + omega_lambda)

    integrand = 1.0 / (a * Ha_over_H0)

    t0_dimless = _trapz_like(integrand, a)
    return float(t0_dimless)


def main() -> None:
    repo_root = get_repo_root()
    joint_grid_path = repo_root / "stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv"
    out_path = repo_root / "stage2/external_frw_host/outputs/tables/stage2_external_frw_rung1_age_crosscheck_v1.csv"

    print("[external_frw_host_rungX1] Repo root:", repo_root)
    print("[external_frw_host_rungX1] Joint grid:", joint_grid_path)

    if not joint_grid_path.exists():
        raise FileNotFoundError(f"Joint grid not found at {joint_grid_path}")

    df = pd.read_csv(joint_grid_path)

    required_cols = ["theta_index", "theta", "omega_lambda", "age_Gyr", "frw_viable"]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise RuntimeError(f"Missing required columns in joint grid: {missing}")

    # Compute dimensionless ages for each row
    omega_lambda_arr = df["omega_lambda"].to_numpy()
    t0_dimless = np.array([frw_age_dimless_flat(ol) for ol in omega_lambda_arr])

    df["age_dimless_host"] = t0_dimless

    # Use the FRW-viable subset to calibrate a single global scale factor
    mask_viable = df["frw_viable"].astype(bool)
    if not mask_viable.any():
        raise RuntimeError("No FRW-viable points found in joint grid for calibration.")

    age_repo_viable = df.loc[mask_viable, "age_Gyr"].to_numpy()
    age_dimless_viable = df.loc[mask_viable, "age_dimless_host"].to_numpy()

    # Guard against zeros in the denominator
    positive_mask = age_dimless_viable > 0
    if not positive_mask.any():
        raise RuntimeError("All dimensionless ages are non-positive; check FRW integrator.")

    scale = np.median(age_repo_viable[positive_mask] / age_dimless_viable[positive_mask])
    df["age_Gyr_host"] = df["age_dimless_host"] * scale

    # Differences and relative differences (on the repo age scale)
    df["age_Gyr_diff"] = df["age_Gyr_host"] - df["age_Gyr"]
    df["age_Gyr_rel_diff"] = df["age_Gyr_diff"] / df["age_Gyr"].where(df["age_Gyr"] != 0, np.nan)

    # Summary statistics (focus on FRW-viable region)
    age_diff_viable = df.loc[mask_viable, "age_Gyr_diff"].to_numpy()
    age_rel_viable = df.loc[mask_viable, "age_Gyr_rel_diff"].to_numpy()

    mean_abs_diff = float(np.nanmean(np.abs(age_diff_viable)))
    max_abs_diff = float(np.nanmax(np.abs(age_diff_viable)))
    mean_abs_rel = float(np.nanmean(np.abs(age_rel_viable)))

    print("[external_frw_host_rungX1] Calibrated scale factor (Gyr / dimless):", scale)
    print("[external_frw_host_rungX1] FRW-viable subset size:", mask_viable.sum())
    print("[external_frw_host_rungX1] Mean |age_host - age_repo| on viable set [Gyr]:", mean_abs_diff)
    print("[external_frw_host_rungX1] Max  |age_host - age_repo| on viable set [Gyr]:", max_abs_diff)
    print("[external_frw_host_rungX1] Mean |relative diff| on viable set:", mean_abs_rel)

    # Prepare a compact output table
    cols_out = [
        "theta_index",
        "theta",
        "omega_lambda",
        "age_Gyr",
        "age_Gyr_host",
        "age_Gyr_diff",
        "age_Gyr_rel_diff",
        "frw_viable",
    ]
    df_out = df[cols_out].copy()

    out_path.parent.mkdir(parents=True, exist_ok=True)
    df_out.to_csv(out_path, index=False)

    print("[external_frw_host_rungX1] Wrote:", out_path)
    print("[external_frw_host_rungX1] Rows:", len(df_out))


if __name__ == "__main__":
    main()
