#!/usr/bin/env python3
"""
R23: theta_star observable corridor and ΛCDM background residuals plot.

This script:
  - Loads the FRW scan over theta_star from
      data/processed/effective_vacuum_theta_frw_scan.npz
  - Reconstructs a simple ΛCDM backbone with (Omega_m, Omega_Lambda) = (0.3, 0.7)
    and the same H0 as the scan.
  - Computes fractional residuals in luminosity distance at z = 0.3, 0.5, 1.0
    between each theta_star slice and the ΛCDM backbone.
  - Applies the observable-corridor cuts used in R13/R22:
        0.60 <= Omega_Lambda <= 0.80
        12.0 <= t0 (Gyr) <= 15.0
        q0 < 0
  - Builds a two-panel figure:
      * Top: Omega_Lambda(theta_star) with the corridor and band indicated.
      * Bottom: fractional distance residuals vs theta_star for the three
        redshifts, with the corridor highlighted and fiducial / best slices
        marked.
  - Saves:
      figures/theta_star_lcdm_background_corridor.png
      figures/theta_star_lcdm_background_corridor.pdf
      data/processed/theta_star_lcdm_background_corridor_plot_summary.json

This serves as the main visual hook for Act VI background-level discussion.
"""

from __future__ import annotations

import json
import math
import pathlib
from dataclasses import dataclass
from typing import Dict, Tuple

import numpy as np
import matplotlib.pyplot as plt


DATA_DIR = pathlib.Path("data/processed")
FIG_DIR = pathlib.Path("figures")

FRW_SCAN_PATH = DATA_DIR / "effective_vacuum_theta_frw_scan.npz"
PLOT_SUMMARY_PATH = DATA_DIR / "theta_star_lcdm_background_corridor_plot_summary.json"


@dataclass
class FRWScan:
    theta: np.ndarray
    omega_lambda: np.ndarray
    omega_m: np.ndarray
    t0_gyr: np.ndarray
    q0: np.ndarray
    dL_z03: np.ndarray
    dL_z05: np.ndarray
    dL_z10: np.ndarray
    theta_min_band: float
    theta_max_band: float
    H0_km_s_Mpc: float
    theta_fid: float
    delta_E_fid: float
    k_scale: float
    omega_target: float


def load_frw_scan(path: pathlib.Path) -> FRWScan:
    print(f"Loading FRW scan from: {path}")
    with np.load(path, allow_pickle=True) as f:
        keys = list(f.keys())
        print(f"  Available keys: {keys}")

        theta = f["theta_scan"]
        omega_lambda = f["omega_lambda_scan"]
        omega_m = f["omega_m_scan"]
        t0_gyr = f["t0_gyr_scan"]
        q0 = f["q0_scan"]
        dL_z03 = f["dL_z03_scan"]
        dL_z05 = f["dL_z05_scan"]
        dL_z10 = f["dL_z10_scan"]

        theta_min_band = float(f["theta_min_band"])
        theta_max_band = float(f["theta_max_band"])
        H0_km_s_Mpc = float(f["H0_KM_S_MPC"])
        theta_fid = float(f["theta_fid"])
        delta_E_fid = float(f["delta_E_fid"])
        k_scale = float(f["k_scale"])
        omega_target = float(f["omega_target"])

    return FRWScan(
        theta=theta,
        omega_lambda=omega_lambda,
        omega_m=omega_m,
        t0_gyr=t0_gyr,
        q0=q0,
        dL_z03=dL_z03,
        dL_z05=dL_z05,
        dL_z10=dL_z10,
        theta_min_band=theta_min_band,
        theta_max_band=theta_max_band,
        H0_km_s_Mpc=H0_km_s_Mpc,
        theta_fid=theta_fid,
        delta_E_fid=delta_E_fid,
        k_scale=k_scale,
        omega_target=omega_target,
    )


def compute_lcdm_backbone(H0_km_s_Mpc: float,
                          Omega_m: float = 0.3,
                          Omega_Lambda: float = 0.7) -> Dict[str, float]:
    """
    Construct a simple flat ΛCDM backbone with (Omega_m, Omega_Lambda) and
    given H0, and compute t0 and dL(z)/(c/H0) at z = 0.3, 0.5, 1.0.

    We work in dimensionless units where H0 = 1 for the integrations and
    convert back to Gyr using the usual conversion factor at the end.
    """
    print("Constructing ΛCDM backbone with (Omega_m, Omega_Lambda) = "
          f"({Omega_m:.3f}, {Omega_Lambda:.3f})")

    # Dimensionless H(a): H(a)/H0
    def E(a: np.ndarray) -> np.ndarray:
        return np.sqrt(Omega_m * a ** -3 + Omega_Lambda)

    # Age t0 * H0 = ∫ da / (a E(a)) from a_min to 1
    a_min = 1e-4
    a_grid = np.linspace(a_min, 1.0, 2000)
    integrand_age = 1.0 / (a_grid * E(a_grid))
    t0_H0 = np.trapz(integrand_age, a_grid)

    # Convert dimensionless t0 * H0 to Gyr for the given H0
    # H0 [km/s/Mpc] -> H0 [s^-1]:
    H0_SI = H0_km_s_Mpc * 1000.0 / (3.0856775814913673e22)
    # Hubble time [s] = 1 / H0
    tH_s = 1.0 / H0_SI
    # Convert to Gyr
    sec_per_yr = 31557600.0
    tH_Gyr = tH_s / (1e9 * sec_per_yr)
    t0_Gyr = t0_H0 * tH_Gyr

    # Luminosity distance d_L(z)/(c/H0) in units of c/H0
    def E_z(z: np.ndarray) -> np.ndarray:
        return np.sqrt(Omega_m * (1 + z) ** 3 + Omega_Lambda)

    z_samples = [0.3, 0.5, 1.0]
    dL_over_cH0 = {}
    for z in z_samples:
        z_grid = np.linspace(0.0, z, 2000)
        integrand = 1.0 / E_z(z_grid)
        chi = np.trapz(integrand, z_grid)  # comoving distance in c/H0 units
        dL = (1 + z) * chi
        dL_over_cH0[f"z{z:.1f}"] = dL

    print(f"  t0_ref = {t0_Gyr:.3f} Gyr")
    for z, dL in dL_over_cH0.items():
        print(f"  dL_ref({z})/(c/H0) = {dL:.4f}")

    return {
        "t0_Gyr": t0_Gyr,
        "dL_z03": dL_over_cH0["z0.3"],
        "dL_z05": dL_over_cH0["z0.5"],
        "dL_z10": dL_over_cH0["z1.0"],
    }


def observable_corridor_mask(scan: FRWScan) -> np.ndarray:
    """
    Apply the same observable-corridor cuts as in R13/R22:
      0.60 <= Omega_Lambda <= 0.80
      12.0 <= t0 <= 15.0 Gyr
      q0 < 0
    """
    m1 = (scan.omega_lambda >= 0.60) & (scan.omega_lambda <= 0.80)
    m2 = (scan.t0_gyr >= 12.0) & (scan.t0_gyr <= 15.0)
    m3 = scan.q0 < 0.0
    mask = m1 & m2 & m3
    print(f"Observable corridor: selected {mask.sum()} / {mask.size} samples.")
    return mask


def compute_residuals(scan: FRWScan,
                      backbone: Dict[str, float]) -> Dict[str, np.ndarray]:
    """
    Compute fractional residuals vs the reference ΛCDM backbone:
      Δt0/t0_ref (not used in plot, but stored),
      ΔdL(z)/dL_ref(z) for z=0.3,0.5,1.0.
    """
    t0_ref = backbone["t0_Gyr"]
    dL_ref_z03 = backbone["dL_z03"]
    dL_ref_z05 = backbone["dL_z05"]
    dL_ref_z10 = backbone["dL_z10"]

    dt0_frac = (scan.t0_gyr - t0_ref) / t0_ref
    ddL_z03_frac = (scan.dL_z03 - dL_ref_z03) / dL_ref_z03
    ddL_z05_frac = (scan.dL_z05 - dL_ref_z05) / dL_ref_z05
    ddL_z10_frac = (scan.dL_z10 - dL_ref_z10) / dL_ref_z10

    print("Residuals vs backbone (absolute, in %):")
    for label, arr in [
        ("|Δt0/t0_ref|", dt0_frac),
        ("|ΔdL(z=0.3)|", ddL_z03_frac),
        ("|ΔdL(z=0.5)|", ddL_z05_frac),
        ("|ΔdL(z=1.0)|", ddL_z10_frac),
    ]:
        vals = np.abs(arr) * 100.0
        print(f"  {label}: min/med/max = "
              f"{vals.min():.2f} / {np.median(vals):.2f} / {vals.max():.2f}")

    return {
        "dt0_frac": dt0_frac,
        "ddL_z03_frac": ddL_z03_frac,
        "ddL_z05_frac": ddL_z05_frac,
        "ddL_z10_frac": ddL_z10_frac,
    }


def find_best_theta(scan: FRWScan, residuals: Dict[str, np.ndarray],
                    mask: np.ndarray) -> Tuple[int, float]:
    """
    Within the observable corridor (mask), find the theta_star index that
    best matches the reference backbone using a simple chi^2 over the three
    distance residuals, assuming 5% fractional errors on each point.
    """
    dd03 = residuals["ddL_z03_frac"]
    dd05 = residuals["ddL_z05_frac"]
    dd10 = residuals["ddL_z10_frac"]

    sigma = 0.05  # 5% toy error
    chi2 = ((dd03 / sigma) ** 2 +
            (dd05 / sigma) ** 2 +
            (dd10 / sigma) ** 2)

    chi2_corridor = np.where(mask, chi2, np.inf)
    idx_best = int(np.argmin(chi2_corridor))
    theta_best = float(scan.theta[idx_best])

    print(f"Best-matching theta_star inside corridor:")
    print(f"  idx_best     = {idx_best}")
    print(f"  theta_best   = {theta_best:.3f} rad")
    print(f"  Omega_m      = {scan.omega_m[idx_best]:.3f}")
    print(f"  Omega_Lambda = {scan.omega_lambda[idx_best]:.3f}")
    print(f"  t0           = {scan.t0_gyr[idx_best]:.3f} Gyr")
    print(f"  q0           = {scan.q0[idx_best]:.3f}")
    print(f"  chi2_bg      = {chi2[idx_best]:.3f}")

    return idx_best, theta_best


def make_plot(scan: FRWScan,
              residuals: Dict[str, np.ndarray],
              mask: np.ndarray,
              theta_best: float) -> None:
    """
    Build and save the two-panel figure:
      - top: Omega_Lambda(theta_star) with band/corridor and fid/best markers,
      - bottom: fractional distance residuals vs theta_star at z=0.3,0.5,1.0.
    """
    FIG_DIR.mkdir(exist_ok=True)

    theta = scan.theta
    omega_L = scan.omega_lambda

    dt0_frac = residuals["dt0_frac"]
    dd03 = residuals["ddL_z03_frac"]
    dd05 = residuals["ddL_z05_frac"]
    dd10 = residuals["ddL_z10_frac"]

    theta_band_min = scan.theta_min_band
    theta_band_max = scan.theta_max_band
    theta_fid = scan.theta_fid

    theta_corr = theta[mask]
    omega_corr = omega_L[mask]

    # For corridor edges, just take min/max of theta over mask
    theta_corr_min = float(theta_corr.min()) if mask.any() else math.nan
    theta_corr_max = float(theta_corr.max()) if mask.any() else math.nan

    fig, (ax_top, ax_bot) = plt.subplots(2, 1, figsize=(7.0, 8.0), sharex=True)

    # --- Top panel: Omega_Lambda(theta_star) ---
    ax_top.plot(theta, omega_L, label=r"$\Omega_\Lambda(\theta_\star)$")
    if mask.any():
        ax_top.fill_between(theta_corr, omega_corr,
                            alpha=0.3,
                            label="Observable corridor")
    ax_top.axvspan(theta_band_min, theta_band_max,
                   alpha=0.05, label="Act II prior band")

    # Vertical lines for fiducial and best
    ax_top.axvline(theta_fid, linestyle="--",
                   label=rf"$\theta_{{\star,\mathrm{{fid}}}} \approx {theta_fid:.2f}$")
    ax_top.axvline(theta_best, linestyle=":",
                   label=rf"$\theta_{{\star,\mathrm{{best}}}} \approx {theta_best:.2f}$")

    ax_top.set_ylabel(r"$\Omega_\Lambda(\theta_\star)$")
    ax_top.set_title(r"Effective vacuum band and observable corridor in $\theta_\star$")
    ax_top.set_xlim(theta_band_min, theta_band_max)
    ax_top.set_ylim(0.0, max(omega_L.max(), 0.8) * 1.05)
    ax_top.legend(loc="best", fontsize=9)

    # --- Bottom panel: fractional distance residuals vs theta_star ---
    # Convert to percent for nicer y-axis numbers
    ax_bot.plot(theta, dd03 * 100.0, label=r"$\Delta d_L(z=0.3)/d_{L,\mathrm{ref}}$ [%]")
    ax_bot.plot(theta, dd05 * 100.0, label=r"$\Delta d_L(z=0.5)/d_{L,\mathrm{ref}}$ [%]")
    ax_bot.plot(theta, dd10 * 100.0, label=r"$\Delta d_L(z=1.0)/d_{L,\mathrm{ref}}$ [%]")

    # Highlight corridor points with thicker markers
    if mask.any():
        ax_bot.plot(theta_corr, dd03[mask] * 100.0, "o", markersize=4)
        ax_bot.plot(theta_corr, dd05[mask] * 100.0, "o", markersize=4)
        ax_bot.plot(theta_corr, dd10[mask] * 100.0, "o", markersize=4)

    # Vertical lines as above
    ax_bot.axvline(theta_fid, linestyle="--",
                   label=rf"$\theta_{{\star,\mathrm{{fid}}}}$")
    ax_bot.axvline(theta_best, linestyle=":",
                   label=rf"$\theta_{{\star,\mathrm{{best}}}}$")

    ax_bot.axhline(0.0, linestyle="-", linewidth=0.8)
    ax_bot.set_xlabel(r"$\theta_\star \;[\mathrm{rad}]$")
    ax_bot.set_ylabel(r"$\Delta d_L / d_{L,\mathrm{ref}} \;[\%]$")
    ax_bot.set_xlim(theta_band_min, theta_band_max)

    # Set a sensible y-range based on percent residuals
    all_resid_percent = np.concatenate(
        [dd03, dd05, dd10]
    ) * 100.0
    max_abs = max(5.0, np.nanmax(np.abs(all_resid_percent)) * 1.1)
    ax_bot.set_ylim(-max_abs, max_abs)

    ax_bot.set_title(r"Fractional distance residuals vs $\theta_\star$ "
                     r"relative to $(\Omega_m,\Omega_\Lambda)=(0.3,0.7)$")
    ax_bot.legend(loc="best", fontsize=9)

    fig.tight_layout(rect=[0, 0, 1, 0.97])
    fig.suptitle(r"R23: $\theta_\star$ observable corridor vs ΛCDM backbone",
                 y=0.995, fontsize=12)

    png_path = FIG_DIR / "theta_star_lcdm_background_corridor.png"
    pdf_path = FIG_DIR / "theta_star_lcdm_background_corridor.pdf"

    fig.savefig(png_path, dpi=200)
    fig.savefig(pdf_path)
    plt.close(fig)

    print(f"Wrote {png_path}")
    print(f"Wrote {pdf_path}")

    # Store corridor edges on the scan object for summary
    scan.theta_corr_min = theta_corr_min
    scan.theta_corr_max = theta_corr_max


def write_plot_summary(scan: FRWScan,
                       residuals: Dict[str, np.ndarray],
                       mask: np.ndarray,
                       theta_best: float) -> None:
    PLOT_SUMMARY_PATH.parent.mkdir(exist_ok=True)

    dt0 = residuals["dt0_frac"]
    dd03 = residuals["ddL_z03_frac"]
    dd05 = residuals["ddL_z05_frac"]
    dd10 = residuals["ddL_z10_frac"]

    def stats(arr: np.ndarray) -> Dict[str, float]:
        vals = np.abs(arr) * 100.0
        return {
            "min_percent": float(vals.min()),
            "median_percent": float(np.median(vals)),
            "max_percent": float(vals.max()),
        }

    summary = {
        "theta_band": [float(scan.theta_min_band), float(scan.theta_max_band)],
        "theta_corridor": [
            float(getattr(scan, "theta_corr_min", float("nan"))),
            float(getattr(scan, "theta_corr_max", float("nan"))),
        ],
        "theta_fid": float(scan.theta_fid),
        "theta_best": float(theta_best),
        "omega_lambda_stats_full": stats(scan.omega_lambda - 0.7),
        "age_residual_stats_full": stats(dt0),
        "dL_residual_stats_full": {
            "z0.3": stats(dd03),
            "z0.5": stats(dd05),
            "z1.0": stats(dd10),
        },
        "corridor_fraction": float(mask.sum()) / float(mask.size),
    }

    with open(PLOT_SUMMARY_PATH, "w") as f:
        json.dump(summary, f, indent=2)

    print(f"Wrote plot summary to {PLOT_SUMMARY_PATH}")


def main() -> None:
    print("=== R23: theta_star observable corridor vs ΛCDM backbone plot ===")
    scan = load_frw_scan(FRW_SCAN_PATH)

    backbone = compute_lcdm_backbone(
        H0_km_s_Mpc=scan.H0_km_s_Mpc,
        Omega_m=0.3,
        Omega_Lambda=0.7,
    )

    mask = observable_corridor_mask(scan)
    residuals = compute_residuals(scan, backbone)
    idx_best, theta_best = find_best_theta(scan, residuals, mask)

    make_plot(scan, residuals, mask, theta_best)
    write_plot_summary(scan, residuals, mask, theta_best)

    print("R23 complete.")


if __name__ == "__main__":
    main()