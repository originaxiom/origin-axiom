#!/usr/bin/env python3
"""
R24: theta_star linear growth vs LCDM-like slice

This script compares the sigma8-like linear growth factor today,
D_rel(a=1; theta_star), across the effective-vacuum theta_star band and,
in particular, within the "observable corridor" defined in R13:

  0.60 <= Omega_Lambda <= 0.80
  12.0 <= t0 [Gyr]     <= 15.0
  q0 < 0

Inputs:
  - data/processed/effective_vacuum_theta_growth_scan.npz
      (from scan_theta_star_linear_growth.py, R15)
  - data/processed/effective_vacuum_theta_frw_scan.npz
      (from scan_theta_star_frw_observables.py, R12/R13)

Output:
  - Console summary of D_rel statistics and sigma8-like ratios
  - data/processed/theta_star_lcdm_growth_comparison.json
"""

import json
from pathlib import Path

import numpy as np


GROWTH_PATH = Path("data/processed/effective_vacuum_theta_growth_scan.npz")
FRW_PATH = Path("data/processed/effective_vacuum_theta_frw_scan.npz")
OUT_JSON = Path("data/processed/theta_star_lcdm_growth_comparison.json")


def load_growth_and_frw(growth_path: Path, frw_path: Path):
    """Load growth and FRW band scans and enforce basic consistency."""
    growth_data = np.load(growth_path)
    frw_data = np.load(frw_path)

    # Required keys (growth)
    try:
        theta_g = growth_data["theta_scan"]
        D_rel = growth_data["D_rel_scan"]
    except KeyError as exc:
        raise KeyError(
            "Growth scan file is missing required keys "
            "'theta_scan' and/or 'D_rel_scan'."
        ) from exc

    # Required keys (FRW)
    try:
        theta_f = frw_data["theta_scan"]
        omega_lambda = frw_data["omega_lambda_scan"]
        t0_gyr = frw_data["t0_gyr_scan"]
        q0 = frw_data["q0_scan"]
        theta_min_band = float(frw_data["theta_min_band"])
        theta_max_band = float(frw_data["theta_max_band"])
        theta_fid = float(frw_data["theta_fid"])
    except KeyError as exc:
        raise KeyError(
            "FRW scan file is missing one of the required keys: "
            "'theta_scan', 'omega_lambda_scan', 't0_gyr_scan', "
            "'q0_scan', 'theta_min_band', 'theta_max_band', 'theta_fid'."
        ) from exc

    # H0 metadata is nice-to-have only
    try:
        H0 = float(frw_data["H0_KM_S_MPC"])
    except KeyError:
        H0 = 70.0

    # Sanity check: theta grids should match
    if theta_g.shape != theta_f.shape or not np.allclose(theta_g, theta_f):
        raise RuntimeError(
            "Theta grids in growth and FRW scans do not match. "
            "Check that both NPZ files were produced with the same band "
            "and sampling."
        )

    return {
        "theta": theta_g,
        "D_rel": D_rel,
        "omega_lambda": omega_lambda,
        "t0_gyr": t0_gyr,
        "q0": q0,
        "theta_min_band": theta_min_band,
        "theta_max_band": theta_max_band,
        "theta_fid": theta_fid,
        "H0": H0,
    }


def main():
    if not GROWTH_PATH.exists():
        raise FileNotFoundError(
            f"Could not find growth scan at {GROWTH_PATH}. "
            "Run scan_theta_star_linear_growth.py (R15) first."
        )
    if not FRW_PATH.exists():
        raise FileNotFoundError(
            f"Could not find FRW scan at {FRW_PATH}. "
            "Run scan_theta_star_frw_observables.py (R12) first."
        )

    data = load_growth_and_frw(GROWTH_PATH, FRW_PATH)

    theta = data["theta"]
    D_rel = data["D_rel"]
    omega_lambda = data["omega_lambda"]
    t0_gyr = data["t0_gyr"]
    q0 = data["q0"]
    theta_min_band = data["theta_min_band"]
    theta_max_band = data["theta_max_band"]
    theta_fid = data["theta_fid"]
    H0 = data["H0"]

    print("=== R24: theta_star linear growth vs LCDM-like slice ===")
    print(f"Loaded growth scan from: {GROWTH_PATH}")
    print(f"Loaded FRW scan    from: {FRW_PATH}")
    print(
        f"  theta band        : {theta_min_band:.3f} -> {theta_max_band:.3f} rad"
    )
    print(
        f"  H0 (metadata)     : {H0:.1f} km s^-1 Mpc^-1"
    )

    # Global growth stats over the full theta band
    D_band_min = float(D_rel.min())
    D_band_max = float(D_rel.max())
    D_band_mean = float(D_rel.mean())

    print("\n[Full theta_star band] linear growth today (relative to EdS):")
    print(f"  D_rel(a=1) min / max : {D_band_min:.3f} / {D_band_max:.3f}")
    print(f"  D_rel(a=1) mean      : {D_band_mean:.3f}")

    # Observable corridor mask (same as R13/R23)
    corridor_mask = (
        (omega_lambda >= 0.60)
        & (omega_lambda <= 0.80)
        & (t0_gyr >= 12.0)
        & (t0_gyr <= 15.0)
        & (q0 < 0.0)
    )
    idx_corridor = np.where(corridor_mask)[0]
    N_corridor = idx_corridor.size

    if N_corridor == 0:
        raise RuntimeError(
            "Observable corridor selection is empty. "
            "Check that the FRW scan uses the same cuts as R13."
        )

    # Effective "best" slice: nearest to theta_fid inside the corridor
    # (this matches the slice used in the background comparison scripts).
    abs_diff = np.abs(theta - theta_fid)
    idx_fid_all = int(abs_diff.argmin())

    if corridor_mask[idx_fid_all]:
        idx_best = idx_fid_all
    else:
        # If the exact fiducial grid point is outside the corridor,
        # pick the corridor point closest in theta to theta_fid.
        abs_diff_corr = abs_diff[idx_corridor]
        idx_best = int(idx_corridor[abs_diff_corr.argmin()])

    theta_best = float(theta[idx_best])
    D_ref = float(D_rel[idx_best])

    # Corridor stats
    D_corr = D_rel[idx_corridor]
    D_corr_min = float(D_corr.min())
    D_corr_max = float(D_corr.max())
    D_corr_mean = float(D_corr.mean())

    # Sigma8-like ratios relative to the best slice
    R_sigma8 = D_corr / D_ref
    R_min = float(R_sigma8.min())
    R_max = float(R_sigma8.max())
    R_mean = float(R_sigma8.mean())

    print("\n[Observable corridor selection]")
    print(f"  Number of samples      : {N_corridor} / {theta.size}")
    print(
        f"  theta_star corridor    : {theta[idx_corridor].min():.3f}"
        f" -> {theta[idx_corridor].max():.3f} rad"
    )
    print(
        f"  D_rel(a=1) corridor    : {D_corr_min:.3f} -> {D_corr_max:.3f}"
    )
    print(f"  mean D_rel(a=1)        : {D_corr_mean:.3f}")

    print("\nReference LCDM-like slice (for sigma8-like normalization):")
    print(f"  theta_fid (metadata)   : {theta_fid:.3f} rad")
    print(f"  theta_best (in band)   : {theta_best:.3f} rad")
    print(f"  D_rel(a=1; theta_best) : {D_ref:.3f}")

    print(
        "\nSigma8-like amplitude ratios "
        "R_sigma8(theta) = D_rel(theta) / D_rel(theta_best) "
        "(within corridor):"
    )
    print(
        f"  R_sigma8 min / max     : {R_min:.3f} / {R_max:.3f}"
    )
    print(f"  R_sigma8 mean          : {R_mean:.3f}")
    print(
        f"  Fractional range       : "
        f"{(R_min - 1.0) * 100:.1f}% .. {(R_max - 1.0) * 100:.1f}% "
        f"relative to theta_best"
    )

    # Prepare JSON summary (convert numpy types to built-in Python types)
    theta_corr = theta[idx_corridor]
    omega_lambda_corr = omega_lambda[idx_corridor]
    t0_corr = t0_gyr[idx_corridor]
    q0_corr = q0[idx_corridor]

    summary = {
        "growth_scan_path": str(GROWTH_PATH),
        "frw_scan_path": str(FRW_PATH),
        "H0_km_s_Mpc": H0,
        "theta_min_band": theta_min_band,
        "theta_max_band": theta_max_band,
        "theta_fid": theta_fid,
        "theta_best": theta_best,
        "D_rel_best": D_ref,
        "band_stats": {
            "D_rel_min": D_band_min,
            "D_rel_max": D_band_max,
            "D_rel_mean": D_band_mean,
        },
        "corridor_selection": {
            "N_total": int(theta.size),
            "N_corridor": int(N_corridor),
            "theta_corr_min": float(theta_corr.min()),
            "theta_corr_max": float(theta_corr.max()),
            "D_rel_min": D_corr_min,
            "D_rel_max": D_corr_max,
            "D_rel_mean": D_corr_mean,
            "R_sigma8_min": R_min,
            "R_sigma8_max": R_max,
            "R_sigma8_mean": R_mean,
        },
        "corridor_samples": {
            "theta": theta_corr.tolist(),
            "D_rel": D_corr.tolist(),
            "omega_lambda": omega_lambda_corr.tolist(),
            "t0_gyr": t0_corr.tolist(),
            "q0": q0_corr.tolist(),
            "R_sigma8": R_sigma8.tolist(),
        },
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with OUT_JSON.open("w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, sort_keys=True)

    print(f"\nWrote growth comparison summary to {OUT_JSON}")
    print("R24 complete.")


if __name__ == "__main__":
    main()