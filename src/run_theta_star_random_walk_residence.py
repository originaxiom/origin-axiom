#!/usr/bin/env python3
"""
R6: Toy random-walk dynamics for theta_star within the microcavity band.

We:
  - Load the microcavity theta_grid and delta_E(theta) from
    data/processed/theta_star_microcavity_scan_full_2pi.npz
  - Load the calibrated k_scale and omega_lambda_target from
    data/processed/theta_star_microcavity_core_summary.json
  - Define Omega_Lambda(theta) = clip(k_scale * delta_E(theta), 0, 0.999)
  - Evolve many theta_star trajectories as a simple 1D random walk
    within the band [theta_min_band, theta_max_band]
  - Measure the fraction of (trajectory, time) points with
    |Omega_Lambda - omega_target| within several windows.

This is explicitly a toy model for residence-time, not a physical
equation of motion for theta_star.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


# ---------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------

MICROCAVITY_SCAN_PATH = Path("data/processed/theta_star_microcavity_scan_full_2pi.npz")
CORE_SUMMARY_PATH = Path("data/processed/theta_star_microcavity_core_summary.json")

# Band we already used in previous steps (in radians):
THETA_MIN_BAND = 2.18
THETA_MAX_BAND = 5.54

# Random-walk parameters
N_TRAJ = 200          # number of independent universes / patches
N_STEPS = 2000        # time steps per trajectory
STEP_SIZE = 0.02      # typical theta-step per time step (radians)
RNG_SEED = 12345      # for reproducibility

# Omega_Lambda target windows (same center as before, different widths)
TOL_LIST = [0.05, 0.02, 0.01]


# ---------------------------------------------------------------------
# Helpers: load microcavity + core scaling, and build Omega_Lambda(theta)
# ---------------------------------------------------------------------


def load_microcavity_scan(path: Path):
    data = np.load(path)
    theta_grid = np.asarray(data["theta_grid"], dtype=float)
    delta_E = np.asarray(data["delta_E"], dtype=float)

    # Sort by theta so interpolation is well-defined
    order = np.argsort(theta_grid)
    theta_sorted = theta_grid[order]
    delta_sorted = delta_E[order]

    return theta_sorted, delta_sorted


def load_core_summary(path: Path):
    """
    Load theta_fid, k_scale and omega_lambda_target from the core summary.

    If k_scale is missing but delta_E_fid is present, reconstruct:
        k_scale = omega_lambda_target / delta_E_fid
    and write it back into the JSON file.
    """
    data = json.loads(path.read_text())

    theta_fid = float(data["theta_fid_nominal"])
    omega_lambda_target = float(data["omega_lambda_target"])

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
                "delta_E_fid is zero; cannot compute k_scale = omega_lambda_target / delta_E_fid."
            )
        k_scale = omega_lambda_target / delta_E_fid
        data["k_scale"] = k_scale
        path.write_text(json.dumps(data, indent=2))
        print(f"[INFO] Reconstructed missing k_scale in {path}")
        print(f"       delta_E_fid         = {delta_E_fid}")
        print(f"       omega_lambda_target = {omega_lambda_target}")
        print(f"       k_scale             = {k_scale}")

    return theta_fid, k_scale, omega_lambda_target


def make_omega_lambda(theta_grid: np.ndarray, delta_E_grid: np.ndarray, k_scale: float):
    """
    Return a function Omega_Lambda(theta) built from the theta_grid, delta_E_grid
    and the calibrated k_scale.
    """
    def deltaE_of_theta(theta: np.ndarray) -> np.ndarray:
        # 1D linear interpolation in theta
        return np.interp(theta, theta_grid, delta_E_grid)

    def omega_lambda(theta: np.ndarray) -> np.ndarray:
        dE = deltaE_of_theta(theta)
        omega = k_scale * dE
        # Clamp to [0, 0.999] as in the effective-vacuum logic
        return np.clip(omega, 0.0, 0.999)

    return omega_lambda


# ---------------------------------------------------------------------
# Random-walk dynamics in theta_star
# ---------------------------------------------------------------------


def run_theta_star_random_walk(
    omega_lambda_fn,
    theta_min: float,
    theta_max: float,
    n_traj: int,
    n_steps: int,
    step_size: float,
    rng_seed: int,
):
    rng = np.random.default_rng(rng_seed)

    # Initial theta for each trajectory: uniform in the band
    theta0 = rng.uniform(theta_min, theta_max, size=n_traj)

    # Allocate arrays: shape (n_traj, n_steps+1)
    theta_traj = np.zeros((n_traj, n_steps + 1), dtype=float)
    omega_traj = np.zeros_like(theta_traj)

    theta_traj[:, 0] = theta0
    omega_traj[:, 0] = omega_lambda_fn(theta0)

    # Simple Gaussian random-walk with reflecting boundaries
    for t in range(1, n_steps + 1):
        step = step_size * rng.normal(size=n_traj)
        theta_new = theta_traj[:, t - 1] + step

        # Reflect at the boundaries (rather than just clipping)
        over_max = theta_new > theta_max
        under_min = theta_new < theta_min

        theta_new[over_max] = theta_max - (theta_new[over_max] - theta_max)
        theta_new[under_min] = theta_min + (theta_min - theta_new[under_min])

        # A second clip in case the reflection overshoots by a lot (rare)
        theta_new = np.clip(theta_new, theta_min, theta_max)

        theta_traj[:, t] = theta_new
        omega_traj[:, t] = omega_lambda_fn(theta_new)

    return theta_traj, omega_traj


def main():
    print("=== R6: theta_star random-walk residence time ===")

    # 1) Load microcavity scan + core summary
    theta_grid, delta_E_grid = load_microcavity_scan(MICROCAVITY_SCAN_PATH)
    theta_fid, k_scale, omega_target = load_core_summary(CORE_SUMMARY_PATH)

    print("Microcavity scan:")
    print(f"  theta_grid: N = {theta_grid.size}, min = {theta_grid.min():.6f}, "
          f"max = {theta_grid.max():.6f}")
    print(f"  delta_E:    min = {delta_E_grid.min(): .6e}, "
          f"max = {delta_E_grid.max(): .6e}")
    print()
    print("Core summary:")
    print(f"  theta_fid          = {theta_fid:.3f} rad")
    print(f"  omega_lambda_target = {omega_target:.3f}")
    print(f"  k_scale             = {k_scale: .6e}")
    print()
    print(f"Random-walk band: [{THETA_MIN_BAND:.3f}, {THETA_MAX_BAND:.3f}] rad")
    print(f"  N_TRAJ  = {N_TRAJ}")
    print(f"  N_STEPS = {N_STEPS}")
    print(f"  STEP_SIZE = {STEP_SIZE:.3f} rad")
    print()

    omega_lambda = make_omega_lambda(theta_grid, delta_E_grid, k_scale)

    # 2) Run the random-walk
    theta_traj, omega_traj = run_theta_star_random_walk(
        omega_lambda_fn=omega_lambda,
        theta_min=THETA_MIN_BAND,
        theta_max=THETA_MAX_BAND,
        n_traj=N_TRAJ,
        n_steps=N_STEPS,
        step_size=STEP_SIZE,
        rng_seed=RNG_SEED,
    )

    # 3) Measure residence fractions in each window
    omega_flat = omega_traj.ravel()
    total_points = omega_flat.size

    print("Residence statistics (fraction of trajectory-time):")
    for tol in TOL_LIST:
        mask = (omega_flat >= omega_target - tol) & (omega_flat <= omega_target + tol)
        n_in = int(mask.sum())
        frac = 100.0 * n_in / total_points
        print(f"  |Omega_Lambda - {omega_target:.3f}| <= {tol:.3f} : "
              f"{n_in} / {total_points} ({frac:.2f}%)")

    # 4) Save for possible plotting later
    out_path = Path("data/processed/theta_star_random_walk_residence.npz")
    np.savez(
        out_path,
        theta_traj=theta_traj,
        omega_traj=omega_traj,
        theta_min=THETA_MIN_BAND,
        theta_max=THETA_MAX_BAND,
        omega_target=omega_target,
        tol_list=np.array(TOL_LIST, dtype=float),
        k_scale=k_scale,
        theta_fid=theta_fid,
    )
    print()
    print(f"Saved random-walk ensemble to {out_path}")


if __name__ == "__main__":
    main()