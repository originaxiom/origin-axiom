#!/usr/bin/env python3
"""
R12: Scan FRW observables over the theta_star band.

We:
  - Load the 1D microcavity scan delta_E(theta) from
      data/processed/theta_star_microcavity_scan_full_2pi.npz
  - Load the core summary (theta_fid, k_scale, omega_lambda_target) from
      data/processed/theta_star_microcavity_core_summary.json
  - Define Omega_Lambda(theta) = clip(k_scale * delta_E(theta), 0, 0.999)
  - Restrict to the Act II theta_star band [2.18, 5.54] rad
  - For a grid of theta values in this band, compute:
      * Omega_Lambda(theta), Omega_m(theta) = 1 - Omega_Lambda(theta)
      * FRW age t0_H0 = ∫ da / (a E(a)) from a_min to 1
      * Age in Gyr for H0 = 70 km/s/Mpc
      * Deceleration parameter q0 = 0.5 * Omega_m - Omega_Lambda
      * Dimensionless luminosity distances d_L(z)/(c/H0) at z = 0.3, 0.5, 1.0
  - Save results to:
      data/processed/effective_vacuum_theta_frw_scan.npz

This is a diagnostic rung: we are not fitting real data, only mapping how
our theta_star-backed effective vacuum would populate basic FRW observables
across the allowed theta_star band.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


MICROCAVITY_SCAN_PATH = Path("data/processed/theta_star_microcavity_scan_full_2pi.npz")
CORE_SUMMARY_PATH = Path("data/processed/theta_star_microcavity_core_summary.json")

# Act II theta_star band (rad), as used in previous rungs
THETA_MIN_BAND = 2.18
THETA_MAX_BAND = 5.54
N_THETA_SAMPLES = 41  # same density as effective_vacuum_band_scan

# Cosmology settings
H0_KM_S_MPC = 70.0  # km/s/Mpc
A_MIN = 1.0e-4      # starting scale factor for age integral


def load_microcavity_scan(path: Path):
    data = np.load(path)
    theta_grid = np.asarray(data["theta_grid"], dtype=float)
    delta_E = np.asarray(data["delta_E"], dtype=float)

    # sort by theta to make interpolation robust
    order = np.argsort(theta_grid)
    theta_sorted = theta_grid[order]
    delta_sorted = delta_E[order]
    return theta_sorted, delta_sorted


def load_core_summary(path: Path):
    data = json.loads(path.read_text())
    theta_fid = float(data["theta_fid_nominal"])
    delta_E_fid = float(data["delta_E_fid"])
    k_scale = float(data["k_scale"])
    omega_target = float(data.get("omega_lambda_target", 0.7))
    return theta_fid, delta_E_fid, k_scale, omega_target


def make_deltaE_interp(theta_grid: np.ndarray, delta_E_grid: np.ndarray):
    def deltaE(theta: np.ndarray) -> np.ndarray:
        return np.interp(theta, theta_grid, delta_E_grid)
    return deltaE


def omega_lambda_from_deltaE(delta_E: np.ndarray, k_scale: float) -> np.ndarray:
    omega = k_scale * delta_E
    return np.clip(omega, 0.0, 0.999)


def hubble_time_gyr(H0_km_s_Mpc: float) -> float:
    """
    Hubble time t_H in Gyr for a given H0 in km/s/Mpc.

    Uses t_H = 9.78e9 / h Gyr with h = H0 / 100 km/s/Mpc, which is the
    standard cosmology back-of-the-envelope relation.
    """
    h = H0_km_s_Mpc / 100.0
    return 9.78e9 / h / 1.0e9  # Gyr


def frw_age_H0(omega_m: float, omega_lambda: float, a_min: float = A_MIN) -> float:
    """
    Dimensionless age t0 * H0 = ∫_{a_min}^{1} da / (a E(a))
    with E(a) = sqrt(omega_m / a^3 + omega_lambda) in a flat FRW (no radiation).
    """
    if omega_m < 0 or omega_lambda < 0:
        return np.nan
    if omega_m + omega_lambda <= 0:
        return np.nan

    a = np.linspace(a_min, 1.0, 2000)
    E = np.sqrt(omega_m / a**3 + omega_lambda)
    integrand = 1.0 / (a * E)
    # np.trapz is deprecated alias; use trapezoid
    t0_H0 = np.trapezoid(integrand, a)
    return float(t0_H0)


def frw_luminosity_distance(omega_m: float, omega_lambda: float, z: float) -> float:
    """
    Dimensionless luminosity distance d_L(z)/(c/H0) in flat FRW:
      d_L = (1+z) * ∫_0^z dz' / E(z'),   E(z') = sqrt(omega_m (1+z')^3 + omega_lambda).
    """
    if omega_m < 0 or omega_lambda < 0:
        return np.nan
    if omega_m + omega_lambda <= 0:
        return np.nan

    z_grid = np.linspace(0.0, z, 2000)
    E = np.sqrt(omega_m * (1.0 + z_grid) ** 3 + omega_lambda)
    integrand = 1.0 / E
    chi = np.trapezoid(integrand, z_grid)
    d_L = (1.0 + z) * chi
    return float(d_L)


def main():
    print("=== R12: theta_star FRW observable scan over effective vacuum band ===")

    theta_grid_mc, delta_E_grid = load_microcavity_scan(MICROCAVITY_SCAN_PATH)
    theta_fid, delta_E_fid, k_scale, omega_target = load_core_summary(CORE_SUMMARY_PATH)

    print("Microcavity scan:")
    print(f"  theta_grid: N = {theta_grid_mc.size}, min = {theta_grid_mc.min():.6f}, "
          f"max = {theta_grid_mc.max():.6f}")
    print(f"  delta_E:    min = {delta_E_grid.min(): .6e}, "
          f"max = {delta_E_grid.max(): .6e}")
    print()
    print("Core summary:")
    print(f"  theta_fid_nominal   = {theta_fid:.3f} rad")
    print(f"  delta_E_fid         = {delta_E_fid: .6e}")
    print(f"  omega_lambda_target = {omega_target:.3f}")
    print(f"  k_scale             = {k_scale: .6e}")
    print()

    deltaE = make_deltaE_interp(theta_grid_mc, delta_E_grid)
    t_H_gyr = hubble_time_gyr(H0_KM_S_MPC)

    theta_scan = np.linspace(THETA_MIN_BAND, THETA_MAX_BAND, N_THETA_SAMPLES)
    omega_lambda_scan = omega_lambda_from_deltaE(deltaE(theta_scan), k_scale)
    omega_m_scan = 1.0 - omega_lambda_scan

    t0_H0_scan = np.zeros_like(theta_scan)
    t0_gyr_scan = np.zeros_like(theta_scan)
    q0_scan = np.zeros_like(theta_scan)
    dL_z03_scan = np.zeros_like(theta_scan)
    dL_z05_scan = np.zeros_like(theta_scan)
    dL_z10_scan = np.zeros_like(theta_scan)

    for i, (theta, omega_l) in enumerate(zip(theta_scan, omega_lambda_scan)):
        omega_m = omega_m_scan[i]
        t0_H0 = frw_age_H0(omega_m, omega_l, a_min=A_MIN)
        t0_gyr = t0_H0 * t_H_gyr
        q0 = 0.5 * omega_m - omega_l

        dL_z03 = frw_luminosity_distance(omega_m, omega_l, 0.3)
        dL_z05 = frw_luminosity_distance(omega_m, omega_l, 0.5)
        dL_z10 = frw_luminosity_distance(omega_m, omega_l, 1.0)

        t0_H0_scan[i] = t0_H0
        t0_gyr_scan[i] = t0_gyr
        q0_scan[i] = q0
        dL_z03_scan[i] = dL_z03
        dL_z05_scan[i] = dL_z05
        dL_z10_scan[i] = dL_z10

    # Basic summary
    print(f"theta* band for scan: [{THETA_MIN_BAND:.3f}, {THETA_MAX_BAND:.3f}] rad")
    print(f"N_theta samples      : {N_THETA_SAMPLES}")
    print()
    print("Omega_Lambda(theta) over band:")
    print(f"  min / max = {omega_lambda_scan.min():.3f} / {omega_lambda_scan.max():.3f}")
    print()
    print("FRW age t0 (Gyr) over band:")
    print(f"  min / max = {t0_gyr_scan.min():.2f} / {t0_gyr_scan.max():.2f}")
    print()
    print("Deceleration parameter q0 over band:")
    print(f"  min / max = {q0_scan.min():.3f} / {q0_scan.max():.3f}")
    print()
    print("Example distances d_L(z)/(c/H0):")
    idx_mid = len(theta_scan) // 2
    print(f"  at theta_mid ≈ {theta_scan[idx_mid]:.3f} rad:")
    print(f"    Omega_m      = {omega_m_scan[idx_mid]:.3f}")
    print(f"    Omega_Lambda = {omega_lambda_scan[idx_mid]:.3f}")
    print(f"    t0           = {t0_gyr_scan[idx_mid]:.2f} Gyr")
    print(f"    q0           = {q0_scan[idx_mid]:.3f}")
    print(f"    d_L(0.3)     = {dL_z03_scan[idx_mid]:.4f} (c/H0)")
    print(f"    d_L(0.5)     = {dL_z05_scan[idx_mid]:.4f} (c/H0)")
    print(f"    d_L(1.0)     = {dL_z10_scan[idx_mid]:.4f} (c/H0)")

    out_path = Path("data/processed/effective_vacuum_theta_frw_scan.npz")
    np.savez(
        out_path,
        theta_scan=theta_scan,
        omega_lambda_scan=omega_lambda_scan,
        omega_m_scan=omega_m_scan,
        t0_H0_scan=t0_H0_scan,
        t0_gyr_scan=t0_gyr_scan,
        q0_scan=q0_scan,
        dL_z03_scan=dL_z03_scan,
        dL_z05_scan=dL_z05_scan,
        dL_z10_scan=dL_z10_scan,
        theta_min_band=THETA_MIN_BAND,
        theta_max_band=THETA_MAX_BAND,
        H0_KM_S_MPC=H0_KM_S_MPC,
        theta_fid=theta_fid,
        delta_E_fid=delta_E_fid,
        k_scale=k_scale,
        omega_target=omega_target,
    )
    print()
    print(f"Saved theta* FRW scan to {out_path}")


if __name__ == "__main__":
    main()