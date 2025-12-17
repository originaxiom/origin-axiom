#!/usr/bin/env python3
"""
R15: theta_star linear growth scan over effective vacuum band.

We take the FRW theta* scan from:
  data/processed/effective_vacuum_theta_frw_scan.npz

For each sample (Omega_m(theta), Omega_Lambda(theta)) we compute the
linear growth factor D(a) at a=1 using the standard integral formula
for a flat Omega_m–Omega_Lambda cosmology:

  D(a) ∝ H(a) ∫_0^a da' / (a'^3 H(a')^3)

with H(a) = H0 * sqrt(Omega_m / a^3 + Omega_Lambda).

We then normalise D(a=1) to an Einstein–de Sitter reference model
(Omega_m=1, Omega_Lambda=0) evaluated with the same numerical scheme.

We also intersect the results with the observable corridor defined in
data/processed/theta_star_observable_corridor.json (R13), if present.

Outputs:
  - Console summary of global and corridor growth ranges.
  - NPZ file:
      data/processed/effective_vacuum_theta_growth_scan.npz
    containing theta, Omega_m, Omega_Lambda, t0, q0, D, D_rel, etc.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Optional, Tuple

import numpy as np


SCAN_PATH = Path("data/processed/effective_vacuum_theta_frw_scan.npz")
CORRIDOR_PATH = Path("data/processed/theta_star_observable_corridor.json")
OUT_PATH = Path("data/processed/effective_vacuum_theta_growth_scan.npz")


def growth_factor_a1(
    omega_m: float,
    omega_lambda: float,
    a_min: float = 1.0e-3,
    n_steps: int = 2000,
) -> float:
    """
    Compute the (unnormalised) linear growth factor D(a=1) for a flat
    Omega_m–Omega_Lambda cosmology, using the standard integral formula

      D(a) ∝ H(a) ∫_0^a da' / (a'^3 H(a')^3),

    evaluated at a=1. The overall normalisation is left arbitrary; we
    later divide by the EdS value to get a dimensionless suppression
    factor D_rel.

    Parameters
    ----------
    omega_m : float
        Matter density parameter Omega_m.
    omega_lambda : float
        Vacuum density parameter Omega_Lambda.
    a_min : float, optional
        Lower bound for the scale factor integration (avoids a=0).
    n_steps : int, optional
        Number of grid points between a_min and 1.

    Returns
    -------
    float
        Unnormalised D(a=1) value.
    """
    if omega_m < 0.0 or omega_lambda < 0.0:
        raise ValueError("Growth factor formula assumes non-negative Omega_m, Omega_Lambda.")

    a_grid = np.linspace(a_min, 1.0, n_steps)
    # E(a) = H(a)/H0
    E = np.sqrt(omega_m / a_grid**3 + omega_lambda)
    integrand = 1.0 / (a_grid**3 * E**3)
    integral = np.trapz(integrand, a_grid)

    # Standard prefactor: (5/2) * Omega_m * E(a) evaluated at a=1
    prefac = 2.5 * omega_m * E[-1]
    D = prefac * integral
    return float(D)


def load_corridor_bounds(path: Path) -> Optional[Tuple[float, float]]:
    """
    Load theta* corridor bounds [min, max] from the selection JSON created in R13.
    Returns None if the file is missing or does not contain the expected keys.
    """
    if not path.exists():
        return None

    try:
        with path.open("r") as f:
            data: Dict = json.load(f)
        theta_corr = data.get("theta_corridor", {})
        tmin = float(theta_corr.get("min_rad"))
        tmax = float(theta_corr.get("max_rad"))
        return tmin, tmax
    except Exception:
        return None


def main() -> None:
    print("=== R15: theta_star linear growth scan ===")

    if not SCAN_PATH.exists():
        raise FileNotFoundError(f"FRW scan file not found: {SCAN_PATH}")

    scan = np.load(SCAN_PATH)

    theta = scan["theta_scan"]
    omega_m = scan["omega_m_scan"]
    omega_lambda = scan["omega_lambda_scan"]
    t0_gyr = scan["t0_gyr_scan"]
    q0 = scan["q0_scan"]

    theta_min_band = float(scan["theta_min_band"])
    theta_max_band = float(scan["theta_max_band"])
    H0_km_s_Mpc = float(scan["H0_KM_S_MPC"])
    theta_fid = float(scan["theta_fid"])
    omega_target = float(scan["omega_target"])

    print(f"Loaded FRW scan from {SCAN_PATH}")
    print(f"  theta range        : {theta_min_band:.3f} -> {theta_max_band:.3f} rad")
    print(f"  Omega_Lambda range : {omega_lambda.min():.3f} -> {omega_lambda.max():.3f}")
    print(f"  t0 range           : {t0_gyr.min():.2f} -> {t0_gyr.max():.2f} Gyr")
    print(f"  q0 range           : {q0.min():.3f} -> {q0.max():.3f}")
    print(f"  H0                 : {H0_km_s_Mpc:.1f} km/s/Mpc")
    print(f"  omega_target       : {omega_target:.3f}")
    print(f"  theta_fid          : {theta_fid:.3f} rad")

    # Compute EdS baseline once
    D_EdS = growth_factor_a1(omega_m=1.0, omega_lambda=0.0)
    print(f"\nEdS reference growth (Omega_m=1, Omega_Lambda=0): D_EdS(a=1) = {D_EdS:.4f}")

    # Growth factor for each theta* sample
    D_a1 = np.empty_like(theta)
    for i, (Om, Ol) in enumerate(zip(omega_m, omega_lambda)):
        D_a1[i] = growth_factor_a1(Om, Ol)

    D_rel = D_a1 / D_EdS

    print("\nGlobal growth over theta* band:")
    print(f"  D_rel(a=1) min / max : {D_rel.min():.3f} / {D_rel.max():.3f}")

    # Corridor stats, if available
    corridor_bounds = load_corridor_bounds(CORRIDOR_PATH)
    theta_corr_min = None
    theta_corr_max = None

    if corridor_bounds is not None:
        theta_corr_min, theta_corr_max = corridor_bounds
        mask_corridor = (theta >= theta_corr_min) & (theta <= theta_corr_max)
        n_corr = int(mask_corridor.sum())

        print("\nObservable corridor (from R13):")
        print(f"  theta_corridor      : {theta_corr_min:.3f} -> {theta_corr_max:.3f} rad")
        print(f"  N_corridor samples  : {n_corr} / {theta.size}")

        if n_corr > 0:
            D_corr = D_rel[mask_corridor]
            Om_corr = omega_m[mask_corridor]
            Ol_corr = omega_lambda[mask_corridor]

            print("  Omega_m range       : "
                  f"{Om_corr.min():.3f} -> {Om_corr.max():.3f}")
            print("  Omega_Lambda range  : "
                  f"{Ol_corr.min():.3f} -> {Ol_corr.max():.3f}")
            print("  D_rel range         : "
                  f"{D_corr.min():.3f} -> {D_corr.max():.3f}")
            print(f"  mean(D_rel)         : {D_corr.mean():.3f}")
        else:
            print("  WARNING: no samples found inside corridor mask.")
    else:
        print("\nNo observable corridor JSON found; skipping corridor-specific stats.")

    # Fiducial theta* growth
    idx_fid = int(np.argmin(np.abs(theta - theta_fid)))
    D_rel_fid = float(D_rel[idx_fid])
    Om_fid = float(omega_m[idx_fid])
    Ol_fid = float(omega_lambda[idx_fid])
    t0_fid = float(t0_gyr[idx_fid])
    q0_fid = float(q0[idx_fid])

    print("\nFiducial theta* sample (closest to theta_fid):")
    print(f"  theta_fid_eff   = {theta[idx_fid]:.3f} rad")
    print(f"  Omega_m         = {Om_fid:.3f}")
    print(f"  Omega_Lambda    = {Ol_fid:.3f}")
    print(f"  t0              = {t0_fid:.2f} Gyr")
    print(f"  q0              = {q0_fid:.3f}")
    print(f"  D_rel(a=1)      = {D_rel_fid:.3f}")

    # Save everything to NPZ
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    np.savez(
        OUT_PATH,
        theta_scan=theta,
        omega_m_scan=omega_m,
        omega_lambda_scan=omega_lambda,
        t0_gyr_scan=t0_gyr,
        q0_scan=q0,
        D_a1_scan=D_a1,
        D_rel_scan=D_rel,
        D_EdS=D_EdS,
        theta_min_band=theta_min_band,
        theta_max_band=theta_max_band,
        H0_KM_S_MPC=H0_km_s_Mpc,
        theta_fid=theta_fid,
        omega_target=omega_target,
        theta_corridor_min=theta_corr_min,
        theta_corridor_max=theta_corr_max,
    )

    print(f"\nSaved growth scan to {OUT_PATH}")


if __name__ == "__main__":
    main()