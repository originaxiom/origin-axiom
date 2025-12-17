#!/usr/bin/env python3
"""
R14: Plot theta_star observable corridor across the effective vacuum band.

Inputs:
  - data/processed/effective_vacuum_theta_frw_scan.npz

This file is produced by scripts/scan_theta_star_frw_observables.py (R12) and
contains:
  - theta_scan          : sampled theta_star values [rad]
  - omega_lambda_scan   : Omega_Lambda(theta_star)
  - t0_gyr_scan         : age t0(theta_star) in Gyr (for H0 ~ 70 km/s/Mpc)
  - q0_scan             : deceleration parameter q0(theta_star)
  - plus some metadata (theta_min_band, theta_max_band, etc.)

We:
  - reload the scan data,
  - apply the same observable cuts as in R13:
      0.60 <= Omega_Lambda <= 0.80
      12.0 <= t0 <= 15.0  Gyr
      q0 < 0  (accelerating today)
  - identify the surviving theta_star "observable corridor",
  - and plot Omega_Lambda(theta_star), t0(theta_star), q0(theta_star)
    with the corridor highlighted.

Outputs:
  - figures/theta_star_observable_corridor.png
  - figures/theta_star_observable_corridor.pdf
  - data/processed/theta_star_observable_corridor_plot_summary.json
"""

from __future__ import annotations

from pathlib import Path
import json

import numpy as np
import matplotlib.pyplot as plt


SCAN_PATH = Path("data/processed/effective_vacuum_theta_frw_scan.npz")
FIG_DIR = Path("figures")
FIG_DIR.mkdir(parents=True, exist_ok=True)

# Selection cuts (same as R13)
OMEGA_MIN = 0.60
OMEGA_MAX = 0.80
T0_MIN_GYR = 12.0
T0_MAX_GYR = 15.0
Q0_MAX = 0.0   # require q0 < 0 (accelerating)


def load_scan(path: Path):
    d = np.load(path)
    theta = np.asarray(d["theta_scan"], dtype=float)
    omega = np.asarray(d["omega_lambda_scan"], dtype=float)
    t0_gyr = np.asarray(d["t0_gyr_scan"], dtype=float)
    q0 = np.asarray(d["q0_scan"], dtype=float)

    theta_min_band = float(d["theta_min_band"])
    theta_max_band = float(d["theta_max_band"])
    H0_km_s_Mpc = float(d["H0_KM_S_MPC"])

    return {
        "theta": theta,
        "omega": omega,
        "t0_gyr": t0_gyr,
        "q0": q0,
        "theta_min_band": theta_min_band,
        "theta_max_band": theta_max_band,
        "H0_km_s_Mpc": H0_km_s_Mpc,
    }


def build_observable_mask(theta, omega, t0_gyr, q0):
    """Return boolean mask for points satisfying the observable cuts."""
    return (
        (omega >= OMEGA_MIN)
        & (omega <= OMEGA_MAX)
        & (t0_gyr >= T0_MIN_GYR)
        & (t0_gyr <= T0_MAX_GYR)
        & (q0 < Q0_MAX)
    )


def plot_corridor(theta, omega, t0_gyr, q0, mask, theta_min_band, theta_max_band):
    """Make the 3-panel corridor plot and return (theta_corridor_min, theta_corridor_max)."""
    if np.any(mask):
        theta_sel = theta[mask]
        corridor_min = float(theta_sel.min())
        corridor_max = float(theta_sel.max())
    else:
        corridor_min = None
        corridor_max = None
        print("Warning: no points satisfy the observable cuts; no corridor to shade.")

    fig, axes = plt.subplots(3, 1, sharex=True, figsize=(6.0, 8.0))

    # Panel 1: Omega_Lambda(theta)
    ax = axes[0]
    ax.plot(theta, omega, marker="o")
    ax.set_ylabel(r"$\Omega_\Lambda(\theta_\star)$")
    ax.set_xlim(theta_min_band, theta_max_band)
    ax.grid(True, linestyle=":")

    if corridor_min is not None:
        ax.axvspan(corridor_min, corridor_max, alpha=0.1)
        ax.axhline(0.7, linestyle="--")
        ax.text(
            0.02,
            0.95,
            r"$0.60 \leq \Omega_\Lambda \leq 0.80$",
            transform=ax.transAxes,
            va="top",
            ha="left",
        )

    # Panel 2: t0(theta) in Gyr
    ax = axes[1]
    ax.plot(theta, t0_gyr, marker="o")
    ax.set_ylabel(r"$t_0(\theta_\star)\,[\mathrm{Gyr}]$")
    ax.grid(True, linestyle=":")
    if corridor_min is not None:
        ax.axvspan(corridor_min, corridor_max, alpha=0.1)
        ax.text(
            0.02,
            0.95,
            r"$12 \leq t_0 \leq 15~\mathrm{Gyr}$",
            transform=ax.transAxes,
            va="top",
            ha="left",
        )

    # Panel 3: q0(theta)
    ax = axes[2]
    ax.plot(theta, q0, marker="o")
    ax.set_ylabel(r"$q_0(\theta_\star)$")
    ax.set_xlabel(r"$\theta_\star~[\mathrm{rad}]$")
    ax.grid(True, linestyle=":")
    ax.axhline(0.0, linestyle="--")
    if corridor_min is not None:
        ax.axvspan(corridor_min, corridor_max, alpha=0.1)
        ax.text(
            0.02,
            0.95,
            r"$q_0 < 0$ (accelerating)",
            transform=ax.transAxes,
            va="top",
            ha="left",
        )

    fig.suptitle(
        r"Observable corridor in $\theta_\star$: "
        r"$\Omega_\Lambda(\theta_\star)$, $t_0(\theta_\star)$, $q_0(\theta_\star)$"
    )
    fig.tight_layout(rect=[0, 0, 1, 0.96])

    out_png = FIG_DIR / "theta_star_observable_corridor.png"
    out_pdf = FIG_DIR / "theta_star_observable_corridor.pdf"
    fig.savefig(out_png, dpi=300)
    fig.savefig(out_pdf)
    plt.close(fig)

    print(f"Wrote {out_png}")
    print(f"Wrote {out_pdf}")

    return corridor_min, corridor_max


def main():
    print("=== R14: theta_star observable corridor plot ===")
    if not SCAN_PATH.exists():
        raise SystemExit(
            f"Scan file not found: {SCAN_PATH}\n"
            "Run scripts/scan_theta_star_frw_observables.py first."
        )

    meta = load_scan(SCAN_PATH)
    theta = meta["theta"]
    omega = meta["omega"]
    t0_gyr = meta["t0_gyr"]
    q0 = meta["q0"]
    theta_min_band = meta["theta_min_band"]
    theta_max_band = meta["theta_max_band"]

    print(f"Loaded FRW scan from {SCAN_PATH}")
    print(f"  theta range        : {theta.min():.3f} -> {theta.max():.3f} rad")
    print(f"  Omega_Lambda range : {omega.min():.3f} -> {omega.max():.3f}")
    print(f"  t0 range           : {t0_gyr.min():.2f} -> {t0_gyr.max():.2f} Gyr")
    print(f"  q0 range           : {q0.min():.3f} -> {q0.max():.3f}")
    print()
    print("Selection criteria:")
    print(f"  {OMEGA_MIN:.2f} <= Omega_Lambda <= {OMEGA_MAX:.2f}")
    print(f"  {T0_MIN_GYR:.2f} <= t0 <= {T0_MAX_GYR:.2f} Gyr")
    print(f"  q0 < {Q0_MAX:.1f}")
    print()

    mask = build_observable_mask(theta, omega, t0_gyr, q0)
    n_total = theta.size
    n_sel = int(mask.sum())
    frac = 100.0 * n_sel / n_total

    if n_sel == 0:
        print(f"No samples satisfy the observable cuts ({n_sel} / {n_total}).")
    else:
        theta_sel = theta[mask]
        omega_sel = omega[mask]
        t0_sel = t0_gyr[mask]
        q0_sel = q0[mask]

        corr_min = float(theta_sel.min())
        corr_max = float(theta_sel.max())

        print(f"Selected {n_sel} / {n_total} samples ({frac:.1f}%)")
        print("theta_star corridor (selected region):")
        print(f"  theta range        : {corr_min:.3f} -> {corr_max:.3f} rad")
        print(f"  Omega_Lambda range : {omega_sel.min():.3f} -> {omega_sel.max():.3f}")
        print(f"  t0 range           : {t0_sel.min():.2f} -> {t0_sel.max():.2f} Gyr")
        print(f"  q0 range           : {q0_sel.min():.3f} -> {q0_sel.max():.3f}")
        print()
        print("Accepted samples (theta, Omega_Lambda, t0[Gyr], q0):")
        for th, om, t0_i, q0_i in zip(theta_sel, omega_sel, t0_sel, q0_sel):
            print(f"  {th:6.3f}  {om:6.3f}  {t0_i:6.2f}  {q0_i:7.3f}")
        print()

    # Plot, with shading if any points survive
    corr_min, corr_max = plot_corridor(
        theta, omega, t0_gyr, q0, mask, theta_min_band, theta_max_band
    )

    summary = {
        "theta_min_band": float(theta_min_band),
        "theta_max_band": float(theta_max_band),
        "H0_KM_S_MPC": float(meta["H0_km_s_Mpc"]),
        "n_total": int(n_total),
        "n_selected": int(n_sel),
        "fraction_selected_percent": frac,
        "theta_corridor_min": corr_min,
        "theta_corridor_max": corr_max,
    }
    out_json = Path("data/processed/theta_star_observable_corridor_plot_summary.json")
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(summary, indent=2))
    print(f"Wrote corridor plot summary to {out_json}")


if __name__ == "__main__":
    main()