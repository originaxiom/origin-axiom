#!/usr/bin/env python3
"""
compare_frw_observables.py

Compute simple FRW / LCDM-style observables for two cosmologies:

  (1) Matter-only, flat FRW:
        Omega_m = 1.0
        Omega_Lambda = 0.0

  (2) Effective vacuum model inferred from the theta* prior:
        Omega_Lambda = OMEGA_LAMBDA_FID  (hard-coded here, consistent with
                                          run_frw_from_microcavity.py)
        Omega_m      = 1.0 - Omega_Lambda

We report:
  - dimensionless age t0 * H0 (integral over a from ~0 to 1)
  - physical age in Gyr assuming H0 ~ 70 km/s/Mpc
  - deceleration parameter today, q0 = 0.5 * Omega_m - Omega_Lambda

This is intentionally minimal: the goal is just to show that
the effective-vacuum cosmology has a negative q0 (accelerated
expansion) and a plausible age scale compared to standard LCDM.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np

from theta_star_config import load_theta_star_config


# Keep this in sync with run_frw_from_microcavity.py and run_frw_from_effective_vacuum.py
OMEGA_LAMBDA_FID = 0.7


@dataclass
class Cosmology:
    name: str
    omega_m: float
    omega_lambda: float


def E_of_a(a: np.ndarray, omega_m: float, omega_lambda: float) -> np.ndarray:
    """
    Dimensionless H(a)/H0 for a flat FRW universe with matter + Lambda.

        E(a) = sqrt( Omega_m / a^3 + Omega_Lambda )

    Radiation and curvature are neglected on purpose (toy model).
    """
    return np.sqrt(omega_m / a**3 + omega_lambda)


def age_in_H0_units(cosmo: Cosmology, a_min: float = 1.0e-4, a_max: float = 1.0) -> float:
    """
    Age t0 in units of H0^{-1}:

        t0 * H0 = integral_{a_min}^{1} da / [a * E(a)]

    We use a simple trapezoidal rule on a uniform grid in a.
    """
    a_grid = np.linspace(a_min, a_max, 5000)
    E = E_of_a(a_grid, cosmo.omega_m, cosmo.omega_lambda)
    integrand = 1.0 / (a_grid * E)
    t_dimless = np.trapz(integrand, a_grid)
    return float(t_dimless)


def deceleration_parameter_today(cosmo: Cosmology) -> float:
    """
    For a flat FRW with only matter and Lambda,

        q0 = - (a * a_ddot) / (a_dot^2) at a=1
           = 0.5 * Omega_m - Omega_Lambda
    """
    return 0.5 * cosmo.omega_m - cosmo.omega_lambda


def hubble_time_Gyr(H0_km_s_Mpc: float = 70.0) -> float:
    """
    Convert H0 (in km/s/Mpc) to a Hubble time t_H in Gyr.

        t_H = 1 / H0

    with the usual unit conversions.
    """
    km_to_m = 1000.0
    Mpc_to_m = 3.085677581e22  # meters
    H0_SI = H0_km_s_Mpc * km_to_m / Mpc_to_m  # 1/s

    seconds_per_year = 365.25 * 24.0 * 3600.0
    seconds_per_Gyr = seconds_per_year * 1.0e9

    t_H_seconds = 1.0 / H0_SI
    return t_H_seconds / seconds_per_Gyr


def main() -> None:
    # 1) Load theta* configuration (for documentation / printing)
    cfg = load_theta_star_config()
    theta_fid = float(cfg.theta_star_fid_rad)
    theta_lo, theta_hi = cfg.theta_star_band_rad

    omega_lambda_eff = float(OMEGA_LAMBDA_FID)
    omega_m_eff = 1.0 - omega_lambda_eff

    # 2) Define the two cosmologies we want to compare.
    cosmo_matter_only = Cosmology(
        name="matter_only",
        omega_m=1.0,
        omega_lambda=0.0,
    )

    cosmo_effective = Cosmology(
        name="effective_vacuum",
        omega_m=omega_m_eff,
        omega_lambda=omega_lambda_eff,
    )

    # 3) Print a short banner so it is self-documenting in the terminal.
    print("=== FRW observable-style checks: matter-only vs effective vacuum ===\n")

    print("-> Effective-vacuum cosmology from theta* prior:")
    print(f"   theta_star_fid_rad  = {theta_fid:.6f}")
    print(f"   theta_star_band_rad = [{theta_lo:.6f}, {theta_hi:.6f}]")
    print(f"   omega_lambda_fid    = {omega_lambda_eff:.6f}")
    print(f"   omega_m_fid         = {omega_m_eff:.6f}\n")

    # 4) Compute dimensionless ages and deceleration parameters.
    results = []
    for cosmo in (cosmo_matter_only, cosmo_effective):
        t_dimless = age_in_H0_units(cosmo)
        q0 = deceleration_parameter_today(cosmo)
        results.append((cosmo, t_dimless, q0))

    # 5) Convert to physical ages (in Gyr) using a fiducial H0.
    H0_km_s_Mpc = 70.0
    t_H_Gyr = hubble_time_Gyr(H0_km_s_Mpc=H0_km_s_Mpc)

    print("=== Dimensionless ages (t0 * H0) ===")
    for cosmo, t_dimless, _ in results:
        print(f"  {cosmo.name:15s}: t0 * H0 ≈ {t_dimless:.3f}")
    print()

    print(f"Assuming H0 ≈ {H0_km_s_Mpc:.1f} km/s/Mpc, the Hubble time is:")
    print(f"  t_H ≈ {t_H_Gyr:.3f} Gyr\n")

    print("=== Physical ages (t0) in Gyr ===")
    for cosmo, t_dimless, _ in results:
        age_Gyr = t_dimless * t_H_Gyr
        print(f"  {cosmo.name:15s}: t0 ≈ {age_Gyr:.2f} Gyr")
    print()

    # 6) Deceleration parameters.
    print("=== Deceleration parameter today (q0) ===")
    for cosmo, _, q0 in results:
        print(f"  {cosmo.name:15s}: q0 ≈ {q0:.3f}")
    print()
    print("Interpretation:")
    print("  - matter_only should give q0 ≈ +0.5 (always decelerating).")
    print("  - effective_vacuum should give q0 < 0 (accelerating),")
    print("    qualitatively compatible with the observed late-time universe.")


if __name__ == "__main__":
    main()