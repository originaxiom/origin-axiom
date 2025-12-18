#!/usr/bin/env python3
"""
R21: Effective vacuum energy scale pivot.

Goal:
  Starting from an illustrative flat FRW cosmology with
    H0 = 70 km s^-1 Mpc^-1
    Omega_Lambda,fid = 0.7
  we:
    - compute rho_crit and rho_Lambda in SI units,
    - compare rho_Lambda to the Planck density,
    - convert rho_Lambda into a characteristic energy scale E_Lambda
      defined by rho_Lambda = E_Lambda^4 in units with hbar = c = 1,
    - express E_Lambda in eV and meV,
    - compare E_Lambda to a reference neutrino mass scale ~ 0.05 eV.

This is bookkeeping for the Act VI bridge: it tells us which
microscopic energy scale corresponds to the effective vacuum slice
we matched to Omega_Lambda ~ 0.7 in the FRW toy.
"""

import json
from pathlib import Path

import numpy as np


def compute_scales():
    # ------------------------------------------------------------------
    # Cosmology input (same as in the R19 physical-scales rung)
    # ------------------------------------------------------------------
    H0_km_s_Mpc = 70.0          # km s^-1 Mpc^-1
    Omega_Lambda_fid = 0.7

    # Unit conversions
    Mpc_in_m = 3.0856775814913673e22  # 1 Mpc in meters
    H0_SI = H0_km_s_Mpc * 1000.0 / Mpc_in_m  # s^-1

    # Fundamental constants (CODATA-ish; sufficient for our purposes)
    c = 299792458.0               # m s^-1
    G = 6.67430e-11               # m^3 kg^-1 s^-2
    hbar = 1.054571817e-34        # J s

    # Critical density and Lambda density in SI units
    rho_crit = 3.0 * H0_SI**2 / (8.0 * np.pi * G)   # kg m^-3
    rho_crit_J = rho_crit * c**2                    # J m^-3
    rho_lambda = Omega_Lambda_fid * rho_crit_J      # J m^-3

    # Planck density for comparison
    # rho_Pl ~ c^7 / (hbar G^2) in SI units (J m^-3)
    rho_pl = c**7 / (hbar * G**2)
    rho_lambda_over_rho_pl = rho_lambda / rho_pl

    # ------------------------------------------------------------------
    # Convert rho_Lambda to a natural-units energy scale E_Lambda
    #
    # In units with hbar = c = 1, energy density has dimension [E]^4,
    # so we can define E_Lambda via rho_Lambda = E_Lambda^4.
    #
    # We convert rho_Lambda[J/m^3] -> rho_Lambda[eV^4] using:
    #   1 eV = 1.602176634e-19 J
    #   1 m = 5.06773065e6 eV^-1
    #
    # Then E_Lambda[eV] = (rho_Lambda[eV^4])^(1/4).
    # ------------------------------------------------------------------
    eV_per_J = 1.0 / 1.602176634e-19
    eV_per_inv_m = 1.0 / 5.06773065e6  # 1/m = (1 / 5.0677e6) eV

    rho_lambda_eV4 = rho_lambda * eV_per_J * (eV_per_inv_m**3)
    E_lambda_eV = float(rho_lambda_eV4**0.25)
    E_lambda_meV = 1.0e3 * E_lambda_eV

    # Reference neutrino-mass scale for a rough comparison
    m_nu_ref_eV = 0.05  # ~sqrt(Delta m^2_atm) scale, for orientation
    E_over_m_nu = E_lambda_eV / m_nu_ref_eV

    return {
        "H0_km_s_Mpc": H0_km_s_Mpc,
        "Omega_Lambda_fid": Omega_Lambda_fid,
        "rho_crit_kg_m3": float(rho_crit),
        "rho_crit_J_m3": float(rho_crit_J),
        "rho_lambda_J_m3": float(rho_lambda),
        "rho_pl_J_m3": float(rho_pl),
        "rho_lambda_over_rho_pl": float(rho_lambda_over_rho_pl),
        "E_lambda_eV": E_lambda_eV,
        "E_lambda_meV": E_lambda_meV,
        "m_nu_ref_eV": m_nu_ref_eV,
        "E_over_m_nu_ref": float(E_over_m_nu),
    }


def main():
    results = compute_scales()

    print("=== R21: effective vacuum energy scale pivot ===")
    print()
    print("Assumed cosmology:")
    print(f"  H0                 = {results['H0_km_s_Mpc']:.1f} km s^-1 Mpc^-1")
    print(f"  Omega_Lambda,fid   = {results['Omega_Lambda_fid']:.3f}")
    print()
    print("Critical and Lambda energy densities:")
    print(f"  rho_crit (mass)    = {results['rho_crit_kg_m3']:.6e} kg m^-3")
    print(f"  rho_crit (energy)  = {results['rho_crit_J_m3']:.6e} J  m^-3")
    print(f"  rho_Lambda         = {results['rho_lambda_J_m3']:.6e} J  m^-3")
    print()
    print("Planck-scale comparison:")
    print(f"  rho_Pl             = {results['rho_pl_J_m3']:.6e} J  m^-3")
    print(
        "  rho_Lambda / rho_Pl "
        f"= {results['rho_lambda_over_rho_pl']:.3e}"
    )
    print("  (This is the familiar ~1e-123 hierarchy.)")
    print()
    print("Effective vacuum energy scale (natural units):")
    print(
        "  Define E_Lambda by rho_Lambda = E_Lambda^4 (hbar = c = 1)."
    )
    print(f"  E_Lambda          = {results['E_lambda_eV']:.4e} eV")
    print(f"                    = {results['E_lambda_meV']:.3f} meV")
    print()
    print("Comparison to a reference neutrino mass scale:")
    print(f"  m_nu,ref          = {results['m_nu_ref_eV']:.3f} eV")
    print(
        "  E_Lambda / m_nu,ref "
        f"= {results['E_over_m_nu_ref']:.3f}"
    )
    print()
    print("Interpretation:")
    print(
        "  - The tiny ratio rho_Lambda / rho_Pl ~ 1e-123 is set by "
        "the combination of (H0, G, c, hbar), not by the microcavity."
    )
    print(
        "  - Once we fix Omega_Lambda,fid ~ 0.7, the corresponding "
        "vacuum-energy scale is E_Lambda ~ a few meV."
    )
    print(
        "  - This rung does not claim a prediction for neutrino masses; "
        "it only locates the effective vacuum slice in the landscape of "
        "microscopic energy scales."
    )

    # Also write a small JSON snapshot for later rungs.
    data_dir = Path("data") / "processed"
    data_dir.mkdir(parents=True, exist_ok=True)
    out_path = data_dir / "effective_vacuum_mass_scale_pivot.json"
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, sort_keys=True)

    print()
    print(f"Wrote mass-scale pivot summary to {out_path}")


if __name__ == "__main__":
    main()