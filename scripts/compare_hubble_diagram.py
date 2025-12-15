#!/usr/bin/env python3
"""
compare_hubble_diagram.py

Toy Hubble diagram-style comparison for the Origin Axiom FRW models:

  - matter-only:       Omega_m = 1.0, Omega_Lambda = 0.0
  - effective vacuum:  Omega_m ~ 0.3, Omega_Lambda ~ 0.7

We compute dimensionless comoving distance chi(z) and luminosity
distance d_L(z) (in units of c / H0), and plot d_L(z) vs z for
both cosmologies.

This script is deliberately simple; it is NOT a precision cosmology
tool, just a way to see that the effective vacuum gives a "more
accelerated" Hubble diagram than matter-only, qualitatively closer
to the observed supernova Hubble diagram.

Usage (from repo root):

  PYTHONPATH=src python3 scripts/compare_hubble_diagram.py
"""

import numpy as np
import matplotlib.pyplot as plt

from theta_star_config import load_theta_star_config


def E_of_z(z, omega_m, omega_lambda):
    """
    Dimensionless H(z)/H0 for a flat FRW with matter + Lambda.

    We ignore radiation and curvature:
      E(z) = sqrt( Omega_m * (1+z)^3 + Omega_Lambda )
    """
    return np.sqrt(omega_m * (1.0 + z) ** 3 + omega_lambda)


def comoving_distance_dimless(z, omega_m, omega_lambda, nz=2000):
    """
    Dimensionless comoving distance chi(z) in units of c/H0:

        chi(z) = integral_0^z dz' / E(z')

    We do a simple trapezoidal integration on a fine z-grid.
    """
    z_grid = np.linspace(0.0, z, nz)
    integrand = 1.0 / E_of_z(z_grid, omega_m, omega_lambda)
    chi = np.trapz(integrand, z_grid)
    return chi


def luminosity_distance_dimless(z, omega_m, omega_lambda, nz=2000):
    """
    Dimensionless luminosity distance d_L(z) in units of c/H0:

        d_L(z) = (1 + z) * chi(z)

    where chi(z) is the comoving distance in c/H0 units.
    """
    chi = comoving_distance_dimless(z, omega_m, omega_lambda, nz=nz)
    return (1.0 + z) * chi


def main():
    # --- 1. Load effective-vacuum cosmology from theta_star config ---
    cfg = load_theta_star_config()
    theta_fid = float(cfg.theta_star_fid_rad)
    theta_lo, theta_hi = cfg.theta_star_band_rad

    # In the current interface, we treat omega_lambda_fid as the
    # effective vacuum density at the fiducial theta_star, and enforce
    # a flat universe:
    omega_lambda_eff = float(getattr(cfg, "omega_lambda_fid", 0.7))
    omega_m_eff = 1.0 - omega_lambda_eff

    print("=== Hubble-diagram-style comparison ===")
    print("Effective-vacuum cosmology from theta_star prior:")
    print(f"  theta_star_fid_rad  = {theta_fid:.6f}")
    print(f"  theta_star_band_rad = [{theta_lo:.6f}, {theta_hi:.6f}]")
    print(f"  omega_lambda_fid    = {omega_lambda_eff:.6f}")
    print(f"  omega_m_fid         = {omega_m_eff:.6f}")
    print()

    # --- 2. Set up redshift grid ---
    # We go up to z ~ 2, where supernova Hubble diagrams are rich.
    z_max = 2.0
    nz = 300
    z_grid = np.linspace(0.0, z_max, nz)

    # Matter-only cosmology
    omega_m_matter = 1.0
    omega_lambda_matter = 0.0

    dL_matter = np.array(
        [luminosity_distance_dimless(z, omega_m_matter, omega_lambda_matter) for z in z_grid]
    )
    dL_eff = np.array(
        [luminosity_distance_dimless(z, omega_m_eff, omega_lambda_eff) for z in z_grid]
    )

    # --- 3. Plot d_L(z) in units of c/H0 ---
    fig, ax = plt.subplots(figsize=(7, 5))

    ax.plot(
        z_grid,
        dL_matter,
        label=r"matter only ($\Omega_m=1,\ \Omega_\Lambda=0$)",
    )
    ax.plot(
        z_grid,
        dL_eff,
        linestyle="--",
        label=r"effective vacuum ($\Omega_m\simeq0.3,\ \Omega_\Lambda\simeq0.7$)",
    )

    ax.set_xlabel("redshift z")
    ax.set_ylabel(r"$d_L(z)$  [in units of $c / H_0$]")
    ax.set_title(
        r"Hubble-style diagram: matter-only vs effective vacuum"
        "\n"
        r"(distances in units of $c / H_0$)"
    )
    ax.legend(loc="upper left")

    ax.grid(True, alpha=0.3)

    outpath = "data/processed/figures/frw_effective_hubble_diagram.png"
    fig.tight_layout()
    fig.savefig(outpath, dpi=150)
    print(f"Saved Hubble-style distance plot to {outpath}")


if __name__ == "__main__":
    main()