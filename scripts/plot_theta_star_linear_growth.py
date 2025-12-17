#!/usr/bin/env python3
"""
R16: theta_star linear growth vs effective vacuum band

This script visualises how the linear growth factor D(a=1) responds to
theta_star within the microcavity-backed effective vacuum band.

Inputs
------
- data/processed/effective_vacuum_theta_frw_scan.npz
    theta_scan          : theta_star samples over [theta_min_band, theta_max_band]
    omega_lambda_scan   : Omega_Lambda(theta)
    omega_m_scan        : Omega_m(theta)
    t0_gyr_scan         : age of universe in Gyr
    q0_scan             : deceleration parameter today
    theta_min_band      : lower edge of theta band
    theta_max_band      : upper edge of theta band
    H0_KM_S_MPC         : H0 used in the FRW scan
    theta_fid           : fiducial theta_star from Act II prior
    omega_target        : target Omega_Lambda at theta_fid (≈ 0.7)

- data/processed/effective_vacuum_theta_growth_scan.npz (from R15)
    theta_scan          : same theta grid as FRW scan
    D_rel_scan          : D(a=1) / D_EdS(a=1) at each theta

What it does
------------
- Reconstructs the "observable corridor" using the same criteria as R13:
    0.60 <= Omega_Lambda <= 0.80
    12.0 <= t0 <= 15.0 Gyr
    q0 < 0    (accelerating)
- Computes a boolean mask for points in the corridor.
- Plots:
    Panel 1: Omega_Lambda(theta) with the corridor shaded
    Panel 2: D_rel(a=1; theta) with the corridor shaded

Outputs
-------
- figures/theta_star_linear_growth_scan.png
- figures/theta_star_linear_growth_scan.pdf

This is a visual companion to R15, showing that the same theta_star
corridor which yields a good age + acceleration also gives a smooth,
moderately suppressed linear growth history.
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


FRW_SCAN_PATH = Path("data/processed/effective_vacuum_theta_frw_scan.npz")
GROWTH_SCAN_PATH = Path("data/processed/effective_vacuum_theta_growth_scan.npz")


def load_frw_scan(path: Path):
    data = np.load(path)
    files = set(data.files)

    for key in ("theta_scan", "theta", "theta_grid"):
        if key in files:
            theta = np.asarray(data[key], dtype=float)
            break
    else:
        raise KeyError(f"Could not find theta array in {path}: {files}")

    omega_lambda = np.asarray(data["omega_lambda_scan"], dtype=float)
    omega_m = np.asarray(data["omega_m_scan"], dtype=float)
    t0_gyr = np.asarray(data["t0_gyr_scan"], dtype=float)
    q0 = np.asarray(data["q0_scan"], dtype=float)

    theta_min_band = float(data["theta_min_band"])
    theta_max_band = float(data["theta_max_band"])
    H0_km_s_MPC = float(data["H0_KM_S_MPC"])
    theta_fid = float(data["theta_fid"])
    omega_target = float(data["omega_target"])

    return {
        "theta": theta,
        "omega_lambda": omega_lambda,
        "omega_m": omega_m,
        "t0_gyr": t0_gyr,
        "q0": q0,
        "theta_min_band": theta_min_band,
        "theta_max_band": theta_max_band,
        "H0_km_s_MPC": H0_km_s_MPC,
        "theta_fid": theta_fid,
        "omega_target": omega_target,
    }


def load_growth_scan(path: Path, theta_ref: np.ndarray):
    data = np.load(path)
    files = set(data.files)

    for key in ("theta_scan", "theta", "theta_grid"):
        if key in files:
            theta = np.asarray(data[key], dtype=float)
            break
    else:
        raise KeyError(f"Could not find theta array in {path}: {files}")

    for key in ("D_rel_scan", "D_rel", "D_rel_a1"):
        if key in files:
            D_rel = np.asarray(data[key], dtype=float)
            break
    else:
        raise KeyError(f"Could not find D_rel array in {path}: {files}")

    if theta.shape != theta_ref.shape or not np.allclose(theta, theta_ref, rtol=0, atol=1e-6):
        raise ValueError(
            "Theta grid in growth scan does not match FRW scan.\n"
            f"  FRW theta shape: {theta_ref.shape}\n"
            f"  growth theta shape: {theta.shape}"
        )

    return {
        "theta": theta,
        "D_rel": D_rel,
    }


def select_corridor(omega_lambda: np.ndarray, t0_gyr: np.ndarray, q0: np.ndarray):
    mask = (
        (omega_lambda >= 0.60)
        & (omega_lambda <= 0.80)
        & (t0_gyr >= 12.0)
        & (t0_gyr <= 15.0)
        & (q0 < 0.0)
    )
    return mask


def plot_theta_star_linear_growth(frw, growth, mask):
    theta = frw["theta"]
    omega_lambda = frw["omega_lambda"]
    t0_gyr = frw["t0_gyr"]
    q0 = frw["q0"]
    D_rel = growth["D_rel"]

    theta_min_band = frw["theta_min_band"]
    theta_max_band = frw["theta_max_band"]
    theta_fid = frw["theta_fid"]

    theta_corridor = theta[mask]
    if theta_corridor.size > 0:
        theta_corr_min = float(theta_corridor.min())
        theta_corr_max = float(theta_corridor.max())
    else:
        theta_corr_min = np.nan
        theta_corr_max = np.nan

    D_corridor = D_rel[mask]
    D_min = float(D_rel.min())
    D_max = float(D_rel.max())
    D_corr_min = float(D_corridor.min()) if D_corridor.size > 0 else np.nan
    D_corr_max = float(D_corridor.max()) if D_corridor.size > 0 else np.nan
    D_corr_mean = float(D_corridor.mean()) if D_corridor.size > 0 else np.nan

    t0_corridor = t0_gyr[mask]
    omega_corridor = omega_lambda[mask]
    q0_corridor = q0[mask]

    fig, axes = plt.subplots(2, 1, figsize=(6.0, 7.0), sharex=True)
    ax1, ax2 = axes

    # Panel 1: Omega_Lambda(theta)
    ax1.plot(theta, omega_lambda, "-", lw=1.8, label=r"$\Omega_\Lambda(\theta_\star)$")

    if theta_corridor.size > 0:
        ax1.axvspan(theta_corr_min, theta_corr_max, alpha=0.15, label="Observable corridor")

    ax1.axvline(theta_min_band, color="k", ls=":", lw=1.0)
    ax1.axvline(theta_max_band, color="k", ls=":", lw=1.0)

    ax1.axvline(theta_fid, color="k", ls="--", lw=1.2, label=r"fiducial $\theta_\star$")

    ax1.set_ylabel(r"$\Omega_\Lambda$")
    ax1.set_xlim(theta_min_band, theta_max_band)
    ax1.set_ylim(0.0, max(0.82, omega_lambda.max() * 1.05))
    ax1.grid(True, alpha=0.3)
    ax1.legend(loc="best", fontsize=8)

    # Panel 2: D_rel(theta)
    ax2.plot(theta, D_rel, "-", lw=1.8, label=r"$D(a=1)/D_{\rm EdS}(a=1)$")

    if theta_corridor.size > 0:
        ax2.axvspan(theta_corr_min, theta_corr_max, alpha=0.15, label="Observable corridor")

    ax2.axvline(theta_min_band, color="k", ls=":", lw=1.0)
    ax2.axvline(theta_max_band, color="k", ls=":", lw=1.0)
    ax2.axvline(theta_fid, color="k", ls="--", lw=1.2, label=r"fiducial $\theta_\star$")

    ax2.set_xlabel(r"$\theta_\star\ {\rm [rad]}$")
    ax2.set_ylabel(r"$D(a=1)/D_{\rm EdS}(a=1)$")
    ax2.set_xlim(theta_min_band, theta_max_band)
    ax2.set_ylim(max(0.6, D_min * 0.95), min(1.05, D_max * 1.05))
    ax2.grid(True, alpha=0.3)
    ax2.legend(loc="best", fontsize=8)

    fig.suptitle(
        r"$\theta_\star$-dependent effective vacuum and linear growth",
        fontsize=11,
    )
    fig.tight_layout(rect=[0.0, 0.0, 1.0, 0.96])

    out_png = Path("figures/theta_star_linear_growth_scan.png")
    out_pdf = Path("figures/theta_star_linear_growth_scan.pdf")
    out_png.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_png, dpi=200)
    fig.savefig(out_pdf)
    plt.close(fig)

    summary = {
        "theta_min_band": float(theta_min_band),
        "theta_max_band": float(theta_max_band),
        "theta_corr_min": theta_corr_min,
        "theta_corr_max": theta_corr_max,
        "N_total": int(theta.size),
        "N_corridor": int(mask.sum()),
        "omega_lambda_min": float(omega_lambda.min()),
        "omega_lambda_max": float(omega_lambda.max()),
        "omega_lambda_corr_min": float(omega_corridor.min()) if omega_corridor.size > 0 else float("nan"),
        "omega_lambda_corr_max": float(omega_corridor.max()) if omega_corridor.size > 0 else float("nan"),
        "t0_min_gyr": float(t0_gyr.min()),
        "t0_max_gyr": float(t0_gyr.max()),
        "t0_corr_min_gyr": float(t0_corridor.min()) if t0_corridor.size > 0 else float("nan"),
        "t0_corr_max_gyr": float(t0_corridor.max()) if t0_corridor.size > 0 else float("nan"),
        "q0_min": float(q0.min()),
        "q0_max": float(q0.max()),
        "q0_corr_min": float(q0_corridor.min()) if q0_corridor.size > 0 else float("nan"),
        "q0_corr_max": float(q0_corridor.max()) if q0_corridor.size > 0 else float("nan"),
        "D_rel_min": D_min,
        "D_rel_max": D_max,
        "D_rel_corr_min": D_corr_min,
        "D_rel_corr_max": D_corr_max,
        "D_rel_corr_mean": D_corr_mean,
        "selection_criteria": {
            "omega_lambda_min": 0.60,
            "omega_lambda_max": 0.80,
            "t0_min_gyr": 12.0,
            "t0_max_gyr": 15.0,
            "q0_max": 0.0,
        },
    }

    summary_path = Path("data/processed/theta_star_linear_growth_plot_summary.json")
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    with summary_path.open("w") as f:
        json.dump(summary, f, indent=2)

    print()
    print("=== R16: theta_star linear growth plot ===")
    print(f"theta band        : {theta_min_band:.3f} -> {theta_max_band:.3f} rad")
    print(f"Omega_Lambda band : {omega_lambda.min():.3f} -> {omega_lambda.max():.3f}")
    print(f"t0 band           : {t0_gyr.min():.2f} -> {t0_gyr.max():.2f} Gyr")
    print(f"q0 band           : {q0.min():.3f} -> {q0.max():.3f}")
    print()
    print("Selection criteria:")
    print("  0.60 <= Omega_Lambda <= 0.80")
    print("  12.0 <= t0 <= 15.0 Gyr")
    print("  q0 < 0")
    print()
    print(f"Selected {int(mask.sum())} / {theta.size} samples "
          f"({100.0 * mask.mean():.1f}%) in the observable corridor.")
    if theta_corridor.size > 0:
        print("theta* corridor (selected region):")
        print(f"  theta range        : {theta_corr_min:.3f} -> {theta_corr_max:.3f} rad")
        print(f"  D_rel(a=1) range   : {D_corr_min:.3f} -> {D_corr_max:.3f}")
        print(f"  mean D_rel(a=1)    : {D_corr_mean:.3f}")
    print()
    print(f"Wrote {out_png}")
    print(f"Wrote {out_pdf}")
    print(f"Wrote growth plot summary to {summary_path}")


def main():
    frw = load_frw_scan(FRW_SCAN_PATH)
    growth = load_growth_scan(GROWTH_SCAN_PATH, frw["theta"])
    mask = select_corridor(frw["omega_lambda"], frw["t0_gyr"], frw["q0"])
    plot_theta_star_linear_growth(frw, growth, mask)


if __name__ == "__main__":
    main()