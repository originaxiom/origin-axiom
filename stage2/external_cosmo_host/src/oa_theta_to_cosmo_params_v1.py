#!/usr/bin/env python3
"""
Stage 2: external cosmology host belt, H1 mapping rung.

This script maps the Stage 2 joint theta grid onto a simple FRW parameter
slice (Omega_m, Omega_lambda, H0) in a toy, flat-Universe way.

- Input:
    stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv

- Output:
    stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_params_grid_v1.csv

Contract:
- We do *not* claim these parameters are the true cosmological parameters of
  our Universe. They are a convenient projection of the Origin-Axiom theta
  axis into a familiar FRW parameter space, suitable for driving an external
  FRW host (analytic or CLASS/CCL/PyCosmo).
"""

from pathlib import Path
import pandas as pd
import numpy as np


def get_repo_root() -> Path:
    # This script lives at: repo_root/stage2/external_cosmo_host/src/....
    return Path(__file__).resolve().parents[3]


def load_joint_grid(repo_root: Path) -> pd.DataFrame:
    path = repo_root / "stage2" / "joint_mech_frw_analysis" / "outputs" / "tables" / "stage2_joint_theta_grid_v1.csv"
    if not path.exists():
        raise FileNotFoundError(f"Joint theta grid not found: {path}")
    df = pd.read_csv(path)
    required = ["theta_index", "theta", "omega_lambda", "age_Gyr"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise RuntimeError(f"Missing required columns in joint grid: {missing}")
    return df


def build_cosmo_params(df: pd.DataFrame) -> pd.DataFrame:
    # Toy mapping v1:
    # - Use repo omega_lambda directly as Omega_lambda.
    # - Impose flatness at v1 by Omega_m = max(0, 1 - Omega_lambda).
    # - Fix H0 to 70 km/s/Mpc as a reference value (not a claim).
    omega_lambda = df["omega_lambda"].to_numpy()
    omega_lambda = np.clip(omega_lambda, 0.0, 2.0)  # mild sanity guard

    omega_m = 1.0 - omega_lambda
    omega_m = np.clip(omega_m, 0.0, 2.0)

    H0 = np.full_like(omega_lambda, 70.0, dtype=float)

    out = pd.DataFrame(
        {
            "theta_index": df["theta_index"].astype(int),
            "theta": df["theta"].astype(float),
            "omega_lambda_repo": df["omega_lambda"].astype(float),
            "age_Gyr_repo": df["age_Gyr"].astype(float),
            "Omega_m": omega_m,
            "Omega_lambda": omega_lambda,
            "H0_km_s_Mpc": H0,
        }
    )

    return out


def main() -> None:
    repo_root = get_repo_root()
    print(f"[external_cosmo_host_H1] Repo root: {repo_root}")

    df_joint = load_joint_grid(repo_root)
    print(f"[external_cosmo_host_H1] Joint grid rows: {len(df_joint)}")

    df_params = build_cosmo_params(df_joint)
    out_path = (
        repo_root
        / "stage2"
        / "external_cosmo_host"
        / "outputs"
        / "tables"
        / "stage2_external_cosmo_params_grid_v1.csv"
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df_params.to_csv(out_path, index=False)

    n = len(df_params)
    omega_m = df_params["Omega_m"].to_numpy()
    omega_l = df_params["Omega_lambda"].to_numpy()

    print(f"[external_cosmo_host_H1] Wrote: {out_path}")
    print(f"[external_cosmo_host_H1] Rows: {n}")
    print(
        f"[external_cosmo_host_H1] On this grid: "
        f"min(Omega_m+Omega_lambda)={np.min(omega_m + omega_l):.3f}, "
        f"max(Omega_m+Omega_lambda)={np.max(omega_m + omega_l):.3f}"
    )


if __name__ == "__main__":
    main()
