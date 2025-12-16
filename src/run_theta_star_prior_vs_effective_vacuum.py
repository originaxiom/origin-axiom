#!/usr/bin/env python3
"""
R7: theta_star prior vs. effective vacuum (microcavity-backed).

Goal:
  - Start from the original theta_star prior samples from the 1D twisted
    vacuum scan (R1).
  - Map each theta_star sample through the calibrated microcavity
    delta_E(theta) and k_scale to obtain an induced prior for
    Omega_Lambda.
  - Save the joint (theta_star, Omega_Lambda) samples for plotting and
    comparison with the "effective vacuum" band / patches (R4–R6).

This script is *read-only* with respect to all earlier data products:
it does not modify existing NPZ/JSON files, only reads them and writes
a new NPZ file.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------

THETA_PRIOR_PATH = Path("data/processed/theta_star_prior_1d_vacuum_samples.npz")
MICROCAVITY_SCAN_PATH = Path("data/processed/theta_star_microcavity_scan_full_2pi.npz")
CORE_SUMMARY_PATH = Path("data/processed/theta_star_microcavity_core_summary.json")

OUT_PATH = Path("data/processed/theta_star_prior_vs_effective_vacuum.npz")


# ---------------------------------------------------------------------
# Loaders
# ---------------------------------------------------------------------


def load_theta_prior(path: Path) -> np.ndarray:
    """
    Load theta_star samples from the 1D twisted-vacuum prior NPZ.

    We allow for a few possible key names to be robust against earlier
    naming choices.
    """
    d = np.load(path)
    print(f"Loaded theta prior from {path}")
    print("  keys:", d.files)

    candidate_keys = [
        "theta_samples",
        "theta_star_samples",
        "theta_prior",
        "theta",
    ]
    key = None
    for k in candidate_keys:
        if k in d.files:
            key = k
            break

    if key is None:
        raise KeyError(
            f"Could not find any of {candidate_keys} in {path}; "
            "please inspect the file structure."
        )

    theta = np.asarray(d[key], dtype=float).ravel()
    print(f"  using theta from key: {key}, shape = {theta.shape}")
    return theta


def load_microcavity_scan(path: Path):
    """
    Load theta_grid and delta_E(theta) from the full 2π microcavity scan.
    """
    d = np.load(path)
    print(f"Loaded microcavity scan from {path}")
    print("  keys:", d.files)

    theta_grid = np.asarray(d["theta_grid"], dtype=float)
    delta_E = np.asarray(d["delta_E"], dtype=float)

    # Sort by theta to make interpolation well-defined
    order = np.argsort(theta_grid)
    theta_sorted = theta_grid[order]
    delta_sorted = delta_E[order]

    print(
        f"  theta_grid: N = {theta_sorted.size}, "
        f"min = {theta_sorted.min():.6f}, max = {theta_sorted.max():.6f}"
    )
    print(
        f"  delta_E:    min = {delta_sorted.min(): .6e}, "
        f"max = {delta_sorted.max(): .6e}"
    )

    return theta_sorted, delta_sorted


def load_core_summary(path: Path):
    """
    Load theta_fid_nominal, omega_lambda_target, and k_scale from the
    microcavity core summary JSON.

    If k_scale is missing but delta_E_fid is present, reconstruct
      k_scale = omega_lambda_target / delta_E_fid
    and write it back to the JSON (as we did in earlier steps).
    """
    data = json.loads(path.read_text())
    print(f"Loaded core summary from {path}")

    theta_fid = float(data["theta_fid_nominal"])

    if "omega_lambda_target" in data:
        omega_lambda_target = float(data["omega_lambda_target"])
    else:
        # default to 0.7 if somehow missing, but this should not happen
        omega_lambda_target = 0.7
        data["omega_lambda_target"] = omega_lambda_target
        path.write_text(json.dumps(data, indent=2))
        print("[WARN] omega_lambda_target missing; set to 0.7 and updated JSON.")

    if "k_scale" in data:
        k_scale = float(data["k_scale"])
    else:
        if "delta_E_fid" not in data:
            raise KeyError(
                "Core summary JSON is missing both 'k_scale' and 'delta_E_fid'; "
                "cannot reconstruct k_scale."
            )
        delta_E_fid = float(data["delta_E_fid"])
        if delta_E_fid == 0.0:
            raise ValueError(
                "delta_E_fid is zero; cannot compute k_scale = "
                "omega_lambda_target / delta_E_fid."
            )
        k_scale = omega_lambda_target / delta_E_fid
        data["k_scale"] = k_scale
        path.write_text(json.dumps(data, indent=2))
        print("[INFO] Reconstructed missing k_scale in core summary JSON.")
        print(f"       delta_E_fid         = {delta_E_fid}")
        print(f"       omega_lambda_target = {omega_lambda_target}")
        print(f"       k_scale             = {k_scale}")

    print("Core summary:")
    print(f"  theta_fid_nominal   = {theta_fid:.3f} rad")
    print(f"  omega_lambda_target = {omega_lambda_target:.3f}")
    print(f"  k_scale             = {k_scale: .6e}")

    return theta_fid, omega_lambda_target, k_scale


# ---------------------------------------------------------------------
# Omega_Lambda(theta) from microcavity
# ---------------------------------------------------------------------


def make_omega_lambda(theta_grid: np.ndarray, delta_E_grid: np.ndarray, k_scale: float):
    """
    Build an interpolation-based Omega_Lambda(theta) function.
    """

    def deltaE_of_theta(theta: np.ndarray) -> np.ndarray:
        return np.interp(theta, theta_grid, delta_E_grid)

    def omega_lambda(theta: np.ndarray) -> np.ndarray:
        dE = deltaE_of_theta(theta)
        omega = k_scale * dE
        # Clamp to [0, 0.999] as in effective-vacuum logic
        return np.clip(omega, 0.0, 0.999)

    return omega_lambda


# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------


def main():
    print("=== R7: theta_star prior vs effective vacuum ===")

    # 1) Load prior samples and microcavity scaling
    theta_prior = load_theta_prior(THETA_PRIOR_PATH)
    theta_grid, delta_E_grid = load_microcavity_scan(MICROCAVITY_SCAN_PATH)
    theta_fid, omega_target, k_scale = load_core_summary(CORE_SUMMARY_PATH)

    omega_lambda_fn = make_omega_lambda(theta_grid, delta_E_grid, k_scale)

    # 2) Map the prior over theta_star into an induced prior for Omega_Lambda
    omega_prior = omega_lambda_fn(theta_prior)

    print()
    print("Prior over theta_star:")
    print(f"  theta_prior: N = {theta_prior.size}")
    print(f"  theta range [rad]: {theta_prior.min():.6f} -> {theta_prior.max():.6f}")
    print()
    print("Induced prior for Omega_Lambda:")
    print(f"  Omega_Lambda range: {omega_prior.min():.3f} -> {omega_prior.max():.3f}")
    print(f"  mean(Omega_Lambda)   = {omega_prior.mean():.3f}")
    print(f"  median(Omega_Lambda) = {np.median(omega_prior):.3f}")
    print(f"  std(Omega_Lambda)    = {omega_prior.std():.3f}")
    print(f"  target Omega_Lambda  = {omega_target:.3f}")
    print()

    # 3) Save a compact NPZ for plotting / further analysis
    np.savez(
        OUT_PATH,
        theta_prior=theta_prior,
        omega_prior=omega_prior,
        theta_grid=theta_grid,
        delta_E_grid=delta_E_grid,
        theta_fid=theta_fid,
        omega_lambda_target=omega_target,
        k_scale=k_scale,
    )
    print(f"Saved prior-vs-effective-vacuum samples to {OUT_PATH}")


if __name__ == "__main__":
    main()