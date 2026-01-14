#!/usr/bin/env python3
"""
Stage 2: external cosmology host belt, H2 background rung.

This script takes the cosmological parameter grid produced by
`oa_theta_to_cosmo_params_v1.py` and computes a flat-FRW background age
using an analytic integral, treating (Omega_m, Omega_lambda, H0) as a toy
parameterisation of a ΛCDM-like background.

- Input:
    stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_params_grid_v1.csv

- Output:
    stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_background_grid_v1.csv

At v1, the "host" is an internal analytic FRW integrator. Later this can be
replaced by CLASS/CCL/PyCosmo without changing the I/O contract.
"""

from pathlib import Path
import numpy as np
import pandas as pd


def get_repo_root() -> Path:
    # repo_root/stage2/external_cosmo_host/src/this_script.py
    return Path(__file__).resolve().parents[3]


def load_params_grid(repo_root: Path) -> pd.DataFrame:
    path = (
        repo_root
        / "stage2"
        / "external_cosmo_host"
        / "outputs"
        / "tables"
        / "stage2_external_cosmo_params_grid_v1.csv"
    )
    if not path.exists():
        raise FileNotFoundError(f"Cosmo params grid not found: {path}")
    df = pd.read_csv(path)
    required = ["theta_index", "theta", "Omega_m", "Omega_lambda", "H0_km_s_Mpc"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise RuntimeError(f"Missing required columns in cosmo params grid: {missing}")
    return df


def frw_age_dimless_flat(Omega_lambda: float, n_steps: int = 10000) -> float:
    """
    Dimensionless age t0 * H0 for a flat Universe with matter + Lambda.

    This uses a simple trapezoidal integral over scale factor a in (0, 1].
    Implemented manually (no reliance on numpy.trapz for compatibility).
    """
    Omega_m = max(0.0, 1.0 - Omega_lambda)
    # Avoid degenerate cases
    if Omega_m <= 0 and Omega_lambda <= 0:
        return float("nan")

    a_min = 1e-4
    a_max = 1.0
    a = np.linspace(a_min, a_max, n_steps)
    a3 = a * a * a
    E = np.sqrt(Omega_m / a3 + Omega_lambda)
    integrand = 1.0 / (a * E)

    # Manual trapezoidal rule:
    # integral ≈ h * [0.5*f0 + f1 + ... + f_{N-2} + 0.5*f_{N-1}]
    h = (a_max - a_min) / (n_steps - 1)
    t0_dimless = h * (
        0.5 * integrand[0]
        + integrand[1:-1].sum()
        + 0.5 * integrand[-1]
    )
    return float(t0_dimless)


def dimless_to_Gyr(t0_dimless: np.ndarray, H0_km_s_Mpc: np.ndarray) -> np.ndarray:
    """
    Convert dimensionless age t0*H0^(-1) to Gyr given H0 in km/s/Mpc.

    t0_dimless is t0 * H0 (unitless). We convert:
        t0 = t0_dimless / H0   (in 1/H0 units),
    and then 1/H0 to Gyr via the usual factor.
    """
    # 1 / H0 [s] = (1 Mpc in km) / (H0 km/s)
    Mpc_in_km = 3.085677581e19  # km
    seconds_per_year = 3.15576e7
    factor = Mpc_in_km / seconds_per_year / 1e9  # (1/H0 in Gyr) when H0 in km/s/Mpc

    H0 = H0_km_s_Mpc
    with np.errstate(divide="ignore", invalid="ignore"):
        t0_Gyr = t0_dimless * factor / H0
    return t0_Gyr


def main() -> None:
    repo_root = get_repo_root()
    print(f"[external_cosmo_host_H2] Repo root: {repo_root}")

    df_params = load_params_grid(repo_root)
    n = len(df_params)
    print(f"[external_cosmo_host_H2] Params grid rows: {n}")

    Omega_lambda = df_params["Omega_lambda"].to_numpy(dtype=float)
    H0 = df_params["H0_km_s_Mpc"].to_numpy(dtype=float)

    t0_dimless = np.array([frw_age_dimless_flat(ol) for ol in Omega_lambda])
    age_Gyr_host = dimless_to_Gyr(t0_dimless, H0)

    out = pd.DataFrame(
        {
            "theta_index": df_params["theta_index"].astype(int),
            "theta": df_params["theta"].astype(float),
            "Omega_m": df_params["Omega_m"].astype(float),
            "Omega_lambda": df_params["Omega_lambda"].astype(float),
            "H0_km_s_Mpc": df_params["H0_km_s_Mpc"].astype(float),
            "age_Gyr_host": age_Gyr_host,
        }
    )

    out_path = (
        repo_root
        / "stage2"
        / "external_cosmo_host"
        / "outputs"
        / "tables"
        / "stage2_external_cosmo_host_background_grid_v1.csv"
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(out_path, index=False)

    finite_mask = np.isfinite(age_Gyr_host)
    n_finite = int(finite_mask.sum())
    print(f"[external_cosmo_host_H2] Wrote: {out_path}")
    print(f"[external_cosmo_host_H2] Rows with finite host age: {n_finite}/{n}")
    if n_finite > 0:
        print(
            f"[external_cosmo_host_H2] Host age stats (finite only): "
            f"min={np.nanmin(age_Gyr_host):.3f} Gyr, "
            f"max={np.nanmax(age_Gyr_host):.3f} Gyr"
        )


if __name__ == "__main__":
    main()
