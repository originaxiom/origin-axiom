#!/usr/bin/env python3
"""
R4: Effective vacuum band scan

Goal
-----
Take the microcavity-backed effective vacuum we already calibrated
(theta_star_microcavity_scan_full_2pi + theta_star_microcavity_core_summary),
and scan a band of theta_star values to see how Omega_Lambda(theta_star)
varies.

This does *not* integrate FRW again. It just quantifies how sensitive the
effective vacuum is to small shifts in theta_star under the same k_scale.

Inputs
------
- data/processed/theta_star_microcavity_scan_full_2pi.npz
    keys: theta_grid, delta_E, E0_uniform, E0_cavity, ...

- data/processed/theta_star_microcavity_core_summary.json
    keys: theta_fid_nominal, theta_fid_grid, delta_E_fid,
          omega_lambda_target, k_scale

Outputs
-------
- data/processed/effective_vacuum_band_scan.npz
    theta_band:        1D array of sampled theta values (rad)
    deltaE_band:       1D array of interpolated ΔE(theta)
    omega_lambda_band: 1D array of Omega_Lambda(theta)
    theta_fid:         scalar (rad)
    k_scale:           scalar
    omega_lambda_target: scalar (fiducial ΩΛ)

Plus a short printed summary to stdout.
"""

import json
from pathlib import Path

import numpy as np


DATA_DIR = Path("data/processed")
SCAN_NPZ = DATA_DIR / "theta_star_microcavity_scan_full_2pi.npz"
CORE_JSON = DATA_DIR / "theta_star_microcavity_core_summary.json"
OUT_NPZ  = DATA_DIR / "effective_vacuum_band_scan.npz"


def load_microcavity_scan():
    if not SCAN_NPZ.exists():
        raise FileNotFoundError(f"Missing microcavity scan NPZ: {SCAN_NPZ}")
    arr = np.load(SCAN_NPZ)
    required = {"theta_grid", "delta_E"}
    if not required.issubset(arr.files):
        raise KeyError(f"{SCAN_NPZ} missing keys {required - set(arr.files)}")
    theta = np.asarray(arr["theta_grid"], dtype=float)
    delta_E = np.asarray(arr["delta_E"], dtype=float)
    return theta, delta_E


def load_core_summary():
    if not CORE_JSON.exists():
        raise FileNotFoundError(f"Missing core summary JSON: {CORE_JSON}")
    data = json.loads(CORE_JSON.read_text())
    theta_fid = float(data["theta_fid_nominal"])
    k_scale = float(data["k_scale"])
    omega_lambda_target = float(data["omega_lambda_target"])
    return theta_fid, k_scale, omega_lambda_target


def clamp(x, lo=0.0, hi=0.999):
    return np.clip(x, lo, hi)


def main():
    print("=== R4: Effective vacuum θ★-band scan ===\n")

    theta_grid, delta_E_grid = load_microcavity_scan()
    theta_fid, k_scale, omega_lambda_target = load_core_summary()

    print("Loaded microcavity scan:")
    print(f"  theta_grid: N = {theta_grid.size}, "
          f"min = {theta_grid.min():.6f}, max = {theta_grid.max():.6f}")
    print(f"  delta_E:    min = {delta_E_grid.min(): .6e}, "
          f"max = {delta_E_grid.max(): .6e}\n")

    print("Loaded core summary:")
    print(f"  theta_fid_nominal   = {theta_fid:.6f} rad")
    print(f"  omega_lambda_target = {omega_lambda_target:.3f}")
    print(f"  k_scale             = {k_scale: .6e}\n")

    # Define a theta band. For now, reuse the band we used in R3:
    #   [2.18, 5.54] rad  (roughly centered around pi)
    theta_min = 2.18
    theta_max = 5.54
    n_samples = 41  # ~0.086 rad spacing; fine for structure

    theta_band = np.linspace(theta_min, theta_max, n_samples)

    # Interpolate delta_E(theta) on this band.
    # theta_grid is already dense; simple 1D interpolation is enough.
    deltaE_band = np.interp(theta_band, theta_grid, delta_E_grid)

    # Map to Omega_Lambda via our existing k_scale, with clamping.
    omega_lambda_raw = k_scale * deltaE_band
    omega_lambda_band = clamp(omega_lambda_raw, 0.0, 0.999)

    # Basic stats
    ol_min = float(omega_lambda_band.min())
    ol_max = float(omega_lambda_band.max())

    print("=== Band scan summary ===")
    print(f"  theta_band range [rad]: {theta_min:.3f} → {theta_max:.3f}")
    print(f"  # samples              : {n_samples}")
    print(f"  Omega_Lambda(theta)    : min = {ol_min:.3f}, "
          f"max = {ol_max:.3f}")

    # Find where Omega_Lambda is "near" observational value, say within ±0.05
    tol = 0.05
    mask_near = np.abs(omega_lambda_band - omega_lambda_target) <= tol
    n_near = int(mask_near.sum())

    print(f"\n  Points with |ΩΛ - {omega_lambda_target:.3f}| ≤ {tol:.3f}: {n_near}")
    if n_near > 0:
        th_near = theta_band[mask_near]
        ol_near = omega_lambda_band[mask_near]
        print("  Representative subset (up to 5 points):")
        for t, ol in list(zip(th_near, ol_near))[:5]:
            print(f"    theta = {t:.6f} rad,  ΩΛ(theta) = {ol:.3f}")
    else:
        print("  (None within this tolerance.)")

    # Save results
    np.savez(
        OUT_NPZ,
        theta_band=theta_band,
        deltaE_band=deltaE_band,
        omega_lambda_band=omega_lambda_band,
        theta_fid=theta_fid,
        k_scale=k_scale,
        omega_lambda_target=omega_lambda_target,
    )

    print(f"\nSaved band scan to {OUT_NPZ}")


if __name__ == "__main__":
    main()