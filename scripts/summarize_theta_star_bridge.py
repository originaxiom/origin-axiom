#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from theta_star_config import load_theta_star_config


DATA_DIR = Path("data/processed")


def frac_window(arr: np.ndarray, target: float, width: float) -> tuple[int, float]:
    """Return (count, percentage) of entries with |arr - target| <= width."""
    if arr.size == 0:
        return 0, 0.0
    mask = (arr >= target - width) & (arr <= target + width)
    count = int(mask.sum())
    frac_pct = float(100.0 * count / arr.size)
    return count, frac_pct


def main() -> None:
    print("=== theta_star bridge summary ===")

    # 1) Act II theta* prior (from config)
    cfg = load_theta_star_config()
    theta_fid = float(cfg.theta_star_fid_rad)
    theta_lo, theta_hi = map(float, cfg.theta_star_band_rad)

    print("theta* prior band (from config): [{:.3f}, {:.3f}] rad".format(theta_lo, theta_hi))
    print("theta* fiducial: {:.3f} rad".format(theta_fid))
    print()

    # 2) Microcavity core summary
    core_path = DATA_DIR / "theta_star_microcavity_core_summary.json"
    core_data = json.loads(core_path.read_text())

    delta_E_fid = float(core_data["delta_E_fid"])
    k_scale = float(core_data["k_scale"])
    omega_target = float(core_data.get("omega_lambda_target", 0.7))

    print("Microcavity core:")
    print("  file         : {}".format(core_path))
    print("  delta_E_fid  = {: .6e}".format(delta_E_fid))
    print("  k_scale      = {: .6e}".format(k_scale))
    print("  omega_target = {:.3f}".format(omega_target))
    print()

    # 3) Effective vacuum band scan
    band_path = DATA_DIR / "effective_vacuum_band_scan.npz"
    band = np.load(band_path)

    theta_band = np.asarray(band["theta_band"], dtype=float)
    omega_band = np.asarray(band["omega_lambda_band"], dtype=float)

    theta_band_min = float(theta_band.min())
    theta_band_max = float(theta_band.max())
    omega_band_min = float(omega_band.min())
    omega_band_max = float(omega_band.max())

    tol_corridor = 0.05
    mask_corridor = (omega_band >= omega_target - tol_corridor) & (
        omega_band <= omega_target + tol_corridor
    )
    n_corridor = int(mask_corridor.sum())

    if n_corridor > 0:
        theta_corridor_lo = float(theta_band[mask_corridor].min())
        theta_corridor_hi = float(theta_band[mask_corridor].max())
    else:
        theta_corridor_lo = None
        theta_corridor_hi = None

    print("Effective vacuum band scan:")
    print("  file              : {}".format(band_path))
    print("  theta_band range  : {:.3f} -> {:.3f} rad".format(theta_band_min, theta_band_max))
    print("  Omega_Lambda range: {:.3f} -> {:.3f}".format(omega_band_min, omega_band_max))
    print("  N_grid            : {}".format(theta_band.size))
    if n_corridor > 0:
        print(
            "  corridor |Omega-0.7| <= {:.3f}: {} / {} points".format(
                tol_corridor, n_corridor, theta_band.size
            )
        )
        print(
            "  theta_corridor     : [{:.3f}, {:.3f}] rad".format(
                theta_corridor_lo, theta_corridor_hi
            )
        )
    else:
        print("  corridor |Omega-0.7| <= {:.3f}: no grid points".format(tol_corridor))
    print()

    # 4) Patch ensemble summary
    patch_path = DATA_DIR / "effective_vacuum_patch_ensemble.npz"
    p = np.load(patch_path)

    omega_p = np.asarray(p["omega_samples"], dtype=float)
    n_patches = int(omega_p.size)

    omega_p_min = float(omega_p.min())
    omega_p_max = float(omega_p.max())
    omega_p_mean = float(omega_p.mean())
    omega_p_median = float(np.median(omega_p))
    omega_p_std = float(omega_p.std())

    p_005_n, p_005_pct = frac_window(omega_p, omega_target, 0.05)
    p_002_n, p_002_pct = frac_window(omega_p, omega_target, 0.02)
    p_001_n, p_001_pct = frac_window(omega_p, omega_target, 0.01)

    print("Patch ensemble (effective_vacuum_patch_ensemble.npz):")
    print("  file              : {}".format(patch_path))
    print("  N_patches         : {}".format(n_patches))
    print(
        "  Omega range       : {:.3f} -> {:.3f}".format(
            omega_p_min, omega_p_max
        )
    )
    print(
        "  mean/median/std   : {:.3f} / {:.3f} / {:.3f}".format(
            omega_p_mean, omega_p_median, omega_p_std
        )
    )
    print(
        "  |Omega-0.7|<=0.05 : {} / {} ({:.1f}%)".format(
            p_005_n, n_patches, p_005_pct
        )
    )
    print(
        "  |Omega-0.7|<=0.02 : {} / {} ({:.1f}%)".format(
            p_002_n, n_patches, p_002_pct
        )
    )
    print(
        "  |Omega-0.7|<=0.01 : {} / {} ({:.1f}%)".format(
            p_001_n, n_patches, p_001_pct
        )
    )
    print()

    # 5) Random-walk residence summary
    rw_path = DATA_DIR / "theta_star_random_walk_residence.npz"
    r = np.load(rw_path)

    omega_rw = np.asarray(r["omega_traj"], dtype=float).ravel()
    n_rw_points = int(omega_rw.size)

    omega_rw_min = float(omega_rw.min())
    omega_rw_max = float(omega_rw.max())

    rw_005_n, rw_005_pct = frac_window(omega_rw, omega_target, 0.05)
    rw_002_n, rw_002_pct = frac_window(omega_rw, omega_target, 0.02)
    rw_001_n, rw_001_pct = frac_window(omega_rw, omega_target, 0.01)

    print("Random-walk residence (theta_star_random_walk_residence.npz):")
    print("  file              : {}".format(rw_path))
    print("  N_points          : {}".format(n_rw_points))
    print(
        "  Omega range       : {:.3f} -> {:.3f}".format(
            omega_rw_min, omega_rw_max
        )
    )
    print(
        "  |Omega-0.7|<=0.05 : {} / {} ({:.1f}%)".format(
            rw_005_n, n_rw_points, rw_005_pct
        )
    )
    print(
        "  |Omega-0.7|<=0.02 : {} / {} ({:.1f}%)".format(
            rw_002_n, n_rw_points, rw_002_pct
        )
    )
    print(
        "  |Omega-0.7|<=0.01 : {} / {} ({:.1f}%)".format(
            rw_001_n, n_rw_points, rw_001_pct
        )
    )
    print()

    # 6) Machine-readable JSON summary
    summary = {
        "theta_star_prior_band": {"lo": theta_lo, "hi": theta_hi},
        "theta_star_fiducial": theta_fid,
        "microcavity_core": {
            "delta_E_fid": delta_E_fid,
            "k_scale": k_scale,
            "omega_lambda_target": omega_target,
        },
        "effective_vacuum_band_scan": {
            "theta_band_min": theta_band_min,
            "theta_band_max": theta_band_max,
            "omega_lambda_min": omega_band_min,
            "omega_lambda_max": omega_band_max,
            "n_points": int(theta_band.size),
            "tol_corridor": tol_corridor,
            "n_points_in_corridor": n_corridor,
            "theta_corridor_lo": theta_corridor_lo,
            "theta_corridor_hi": theta_corridor_hi,
        },
        "patch_ensemble": {
            "n_patches": n_patches,
            "omega_lambda_min": omega_p_min,
            "omega_lambda_max": omega_p_max,
            "omega_lambda_mean": omega_p_mean,
            "omega_lambda_median": omega_p_median,
            "omega_lambda_std": omega_p_std,
            "fractions_in_windows": {
                "0.05": {"count": p_005_n, "percent": p_005_pct},
                "0.02": {"count": p_002_n, "percent": p_002_pct},
                "0.01": {"count": p_001_n, "percent": p_001_pct},
            },
        },
        "random_walk_residence": {
            "n_points": n_rw_points,
            "omega_lambda_min": omega_rw_min,
            "omega_lambda_max": omega_rw_max,
            "fractions_in_windows": {
                "0.05": {"count": rw_005_n, "percent": rw_005_pct},
                "0.02": {"count": rw_002_n, "percent": rw_002_pct},
                "0.01": {"count": rw_001_n, "percent": rw_001_pct},
            },
        },
    }

    out_path = DATA_DIR / "theta_star_bridge_summary.json"
    out_path.write_text(json.dumps(summary, indent=2))
    print("Wrote summary JSON to {}".format(out_path))


if __name__ == "__main__":
    main()