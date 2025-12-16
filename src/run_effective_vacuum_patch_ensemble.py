"""
R5: Effective vacuum patch ensemble

Given the band-scan Omega_Lambda(theta_star) from:
    data/processed/effective_vacuum_band_scan.npz

we:
  - sample many theta_star values in the allowed band,
  - map each to Omega_Lambda(theta_star) via linear interpolation,
  - estimate the fraction of patches that land in a narrow window
    around the observed Omega_Lambda ~ 0.7.

Outputs:
  data/processed/effective_vacuum_patch_ensemble.npz
"""

from __future__ import annotations

import numpy as np
from pathlib import Path


def load_band_scan(path: Path = Path("data/processed/effective_vacuum_band_scan.npz")):
    d = np.load(path)
    theta_band = np.asarray(d["theta_band"], dtype=float)
    omega_band = np.asarray(d["omega_lambda_band"], dtype=float)
    theta_fid = float(d["theta_fid"])
    k_scale = float(d["k_scale"])
    omega_lambda_target = float(d["omega_lambda_target"])
    return theta_band, omega_band, theta_fid, k_scale, omega_lambda_target


def build_interp(theta_grid: np.ndarray, omega_grid: np.ndarray):
    """
    Return a simple 1D linear interpolator Omega_Lambda(theta),
    wrapping numpy.interp on a sorted theta grid.
    """
    idx = np.argsort(theta_grid)
    t_sorted = theta_grid[idx]
    o_sorted = omega_grid[idx]

    def omega_of_theta(theta: np.ndarray | float) -> np.ndarray | float:
        return np.interp(theta, t_sorted, o_sorted,
                         left=o_sorted[0], right=o_sorted[-1])

    return omega_of_theta


def main():
    theta_grid, omega_grid, theta_fid, k_scale, omega_target = load_band_scan()
    omega_target = float(omega_target)

    # Build interpolator ΩΛ(θ★)
    omega_of_theta = build_interp(theta_grid, omega_grid)

    # Patch ensemble: many theta★ values in the band
    theta_min = float(theta_grid.min())
    theta_max = float(theta_grid.max())

    rng = np.random.default_rng(12345)
    n_patches = 1000  # can increase later if needed

    theta_samples = rng.uniform(theta_min, theta_max, size=n_patches)
    omega_samples = omega_of_theta(theta_samples)

    # Selection window around the observed ΩΛ ≃ 0.7
    tol = 0.05
    mask_ok = np.abs(omega_samples - omega_target) <= tol
    frac_ok = float(mask_ok.mean())

    # Persist result for later plotting / analysis
    out_path = Path("data/processed/effective_vacuum_patch_ensemble.npz")
    out_path.parent.mkdir(exist_ok=True)
    np.savez(
        out_path,
        theta_samples=theta_samples,
        omega_samples=omega_samples,
        theta_min=theta_min,
        theta_max=theta_max,
        omega_target=omega_target,
        tol=tol,
        theta_fid=theta_fid,
        k_scale=k_scale,
    )

    print("=== R5: effective vacuum patch ensemble ===")
    print(f"  n_patches           = {n_patches}")
    print(f"  theta range [rad]   = {theta_min:.3f} → {theta_max:.3f}")
    print(f"  Omega_Lambda range  = {omega_samples.min():.3f} → {omega_samples.max():.3f}")
    print(f"  target ΩΛ           = {omega_target:.3f} ± {tol:.3f}")
    print(f"  # patches in window = {mask_ok.sum()}  ({frac_ok*100.0:.1f}%)")
    print()
    print(f"Saved ensemble to {out_path}")


if __name__ == "__main__":
    main()