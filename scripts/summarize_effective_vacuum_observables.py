#!/usr/bin/env python3
"""
R10: FRW observables for theta_star-backed effective vacuum.

This script computes a few standard FRW observables for two cosmologies:

  1) matter_only:
       Omega_m = 1.0
       Omega_Lambda = 0.0

  2) effective_vacuum:
       Omega_m = 0.3
       Omega_Lambda = 0.7

The second set of parameters is the same pair used in the
theta_star -> microcavity -> effective vacuum bridge:
  - Omega_Lambda(theta_star_fid) ~ 0.7
  - Omega_m(theta_star_fid) ~ 0.3

For each cosmology we compute:
  - t0 * H0  (dimensionless age factor)
  - t0 in Gyr for a fiducial H0 = 70 km/s/Mpc
  - deceleration parameter q0 = 0.5 * Omega_m - Omega_Lambda
  - luminosity distance d_L(z) / (c / H0) for a few redshifts z

This is a sanity rung: we only check that the effective_vacuum
cosmology lives in the same ballpark as standard LambdaCDM
(age ~ 13-14 Gyr, q0 < 0, SN-like Hubble diagram behavior).
"""

from __future__ import annotations

import numpy as np


# ----------------------------------------------------------------------
# Basic FRW helpers
# ----------------------------------------------------------------------


def E_of_a(a: np.ndarray, omega_m: float, omega_lambda: float) -> np.ndarray:
    """
    Dimensionless Hubble factor E(a) = H(a) / H0 for flat FRW with
    matter + Lambda (no radiation, no curvature).

    E(a) = sqrt( Omega_m / a^3 + Omega_Lambda )
    """
    return np.sqrt(omega_m / a**3 + omega_lambda)


def age_factor(omega_m: float, omega_lambda: float,
               a_min: float = 1.0e-4, n_steps: int = 20000) -> float:
    """
    Compute t0 * H0 = int_{a_min}^1 da / (a * E(a)) with a simple
    trapezoidal rule.

    a_min is a small starting scale factor representing "early times".
    """
    a = np.linspace(a_min, 1.0, n_steps + 1)
    E = E_of_a(a, omega_m, omega_lambda)
    integrand = 1.0 / (a * E)
    t0_H0 = np.trapz(integrand, a)
    return float(t0_H0)


def hubble_time_Gyr(H0_km_s_Mpc: float = 70.0) -> float:
    """
    Return the Hubble time t_H = 1 / H0 in Gyr for a given H0 in km/s/Mpc.

    Uses:
      1 Mpc = 3.085677581491367e22 m
      1 Gyr = 1e9 * 365.25 * 24 * 3600 s
    """
    Mpc_in_m = 3.085677581491367e22
    H0_SI = H0_km_s_Mpc * 1.0e3 / Mpc_in_m  # s^-1
    t_H0_sec = 1.0 / H0_SI
    sec_per_Gyr = 1.0e9 * 365.25 * 24.0 * 3600.0
    return t_H0_sec / sec_per_Gyr


def comoving_distance(z: float, omega_m: float, omega_lambda: float,
                      n_steps: int = 2000) -> float:
    """
    Dimensionless comoving distance chi(z) in units of c/H0:

      chi(z) = int_0^z dz' / E(z')

    where E(z) = sqrt( Omega_m (1+z)^3 + Omega_Lambda ).
    """
    if z <= 0.0:
        return 0.0
    z_grid = np.linspace(0.0, z, n_steps + 1)
    E = np.sqrt(omega_m * (1.0 + z_grid)**3 + omega_lambda)
    integrand = 1.0 / E
    chi = np.trapz(integrand, z_grid)
    return float(chi)


def luminosity_distance(z: float, omega_m: float, omega_lambda: float,
                        n_steps: int = 2000) -> float:
    """
    Dimensionless luminosity distance d_L(z) / (c/H0):

      d_L(z) = (1+z) * chi(z).
    """
    chi = comoving_distance(z, omega_m, omega_lambda, n_steps=n_steps)
    return (1.0 + z) * chi


def deceleration_parameter(omega_m: float, omega_lambda: float) -> float:
    """
    q0 = 0.5 * Omega_m - Omega_Lambda
    for matter + Lambda in flat FRW.
    """
    return 0.5 * omega_m - omega_lambda


# ----------------------------------------------------------------------
# Main R10 summary
# ----------------------------------------------------------------------


def summarize_cosmology(label: str,
                        omega_m: float,
                        omega_lambda: float,
                        H0_km_s_Mpc: float = 70.0,
                        z_list: list[float] | None = None) -> None:
    """
    Print FRW observables for a given (Omega_m, Omega_Lambda).
    """
    if z_list is None:
        z_list = [0.3, 0.5, 1.0]

    print(f"--- {label} ---")
    print(f"Omega_m      = {omega_m:.3f}")
    print(f"Omega_Lambda = {omega_lambda:.3f}")
    print(f"H0           = {H0_km_s_Mpc:.1f} km/s/Mpc")

    # Age factor t0 * H0
    t0_H0 = age_factor(omega_m, omega_lambda)
    t_H0_Gyr = hubble_time_Gyr(H0_km_s_Mpc=H0_km_s_Mpc)
    t0_Gyr = t0_H0 * t_H0_Gyr

    # Deceleration parameter
    q0 = deceleration_parameter(omega_m, omega_lambda)

    print()
    print(f"t0 * H0      = {t0_H0:.3f}")
    print(f"Hubble time  = {t_H0_Gyr:.2f} Gyr")
    print(f"t0           = {t0_Gyr:.2f} Gyr")
    print(f"q0           = {q0:.3f}")
    print()

    # Hubble-diagram style distances
    print("z    d_L(z)/(c/H0)")
    for z in z_list:
        dL = luminosity_distance(z, omega_m, omega_lambda)
        print(f"{z:3.1f}  {dL:8.4f}")
    print()


def main() -> None:
    print("=== R10: FRW observables for theta_star-backed effective vacuum ===")
    print()

    # Baseline cosmologies:
    # 1) pure matter
    omega_m_matter = 1.0
    omega_l_matter = 0.0

    # 2) effective vacuum (theta_star + microcavity backed)
    #    This pair (0.3, 0.7) is the same one used in the
    #    FRW-from-effective-vacuum rung built from the microcavity
    #    DeltaE(theta_star_fid) with k_scale tuned to Omega_Lambda ~ 0.7.
    omega_m_eff = 0.3
    omega_l_eff = 0.7

    H0 = 70.0

    print(f"Assumed H0 = {H0:.1f} km/s/Mpc")
    print()

    summarize_cosmology(
        label="matter_only",
        omega_m=omega_m_matter,
        omega_lambda=omega_l_matter,
        H0_km_s_Mpc=H0,
        z_list=[0.3, 0.5, 1.0],
    )

    summarize_cosmology(
        label="effective_vacuum (theta_star-backed)",
        omega_m=omega_m_eff,
        omega_lambda=omega_l_eff,
        H0_km_s_Mpc=H0,
        z_list=[0.3, 0.5, 1.0],
    )


if __name__ == "__main__":
    main()