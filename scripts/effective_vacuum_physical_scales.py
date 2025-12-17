"""
R19: Physical scales for the effective vacuum bridge

This script takes our calibrated effective vacuum (Omega_Lambda ~ 0.7 at
theta_star ~ 3.63 rad with H0 = 70 km/s/Mpc), computes the corresponding
physical vacuum energy density, and relates it to the dimensionless
microcavity energy shift DeltaE_fid from the core summary.

Goals:
  - Print rho_crit and rho_Lambda in SI units.
  - Compute rho_Lambda / rho_Pl (Planck density) to expose the ~1e-123 hierarchy.
  - Compute the effective scale factor that maps DeltaE_fid -> rho_Lambda.

Inputs:
  - data/processed/theta_star_microcavity_core_summary.json
      (must contain at least: delta_E_fid, omega_target, optionally k_scale)
"""

from __future__ import annotations

import json
import math
from pathlib import Path
import sys


CORE_PATH = Path("data/processed/theta_star_microcavity_core_summary.json")


def load_core_summary():
    if not CORE_PATH.exists():
        print(f"ERROR: {CORE_PATH} not found.")
        print("Run the microcavity summary rung first "
              "(e.g. summarize_theta_star_microcavity_scan.py).")
        sys.exit(1)

    with CORE_PATH.open("r") as f:
        core = json.load(f)

    print(f"Loaded microcavity core summary from: {CORE_PATH}")
    print(f"Available keys: {sorted(core.keys())}")

    # Required: delta_E_fid
    try:
        delta_E_fid = core["delta_E_fid"]
    except KeyError:
        print("ERROR: 'delta_E_fid' key not found in core summary JSON.")
        sys.exit(1)

    # Fiducial theta (optional but nice to print)
    theta_fid = core.get("theta_fid_nominal",
                         core.get("theta_fid",
                                  None))

    # Target Omega_Lambda at the fiducial slice
    omega_target = core.get("omega_target", 0.7)

    # Optional: stored k_scale from previous rungs
    k_scale = core.get("k_scale", None)

    return {
        "delta_E_fid": float(delta_E_fid),
        "theta_fid": float(theta_fid) if theta_fid is not None else None,
        "omega_target": float(omega_target),
        "k_scale": float(k_scale) if k_scale is not None else None,
    }


def main():
    core = load_core_summary()
    delta_E_fid = core["delta_E_fid"]
    theta_fid = core["theta_fid"]
    omega_target = core["omega_target"]
    k_scale = core["k_scale"]

    print()
    print("=== R19: Physical scales for the effective vacuum bridge ===")
    if theta_fid is not None:
        print(f"Fiducial theta_star (from core summary) : {theta_fid:.3f} rad")
    else:
        print("Fiducial theta_star: (not stored in core summary)")
    print(f"DeltaE_fid (dimensionless microcavity shift) : {delta_E_fid:.6e}")
    print(f"Omega_Lambda target at fiducial slice       : {omega_target:.3f}")
    if k_scale is not None:
        print(f"k_scale from core summary                   : {k_scale:.6e}")
    print()

    # --- Physical constants (CODATA-ish, sufficient for our purpose) ---
    # All calculations are approximate at the ~1% level; this is bookkeeping,
    # not precision cosmology.
    G = 6.67430e-11          # m^3 kg^-1 s^-2
    c = 299_792_458.0        # m s^-1
    hbar = 1.054_571_817e-34 # J s

    # H0 in standard cosmology units
    H0_km_s_Mpc = 70.0       # km s^-1 Mpc^-1 (same as in FRW scripts)
    Mpc_in_m = 3.085_677_581_491_367e22  # m

    # Convert H0 to SI (s^-1)
    H0_SI = H0_km_s_Mpc * 1_000.0 / Mpc_in_m

    # Critical density: rho_crit = 3 H0^2 / (8 pi G)
    rho_crit = 3.0 * H0_SI**2 / (8.0 * math.pi * G)  # kg / m^3
    rho_lambda_mass = omega_target * rho_crit        # kg / m^3
    rho_lambda_Jm3 = rho_lambda_mass * c**2          # J / m^3

    # Planck energy density: rho_Pl = c^7 / (hbar * G^2)  [J / m^3]
    rho_Pl_Jm3 = c**7 / (hbar * G**2)
    ratio_lambda_to_Pl = rho_lambda_Jm3 / rho_Pl_Jm3

    # Effective mapping from dimensionless DeltaE_fid to physical rho_Lambda
    # Units: J/m^3 per unit of (dimensionless) DeltaE
    scale_factor = rho_lambda_Jm3 / delta_E_fid

    print("Assumed cosmology:")
    print(f"  H0                = {H0_km_s_Mpc:.1f} km s^-1 Mpc^-1")
    print(f"  rho_crit          = {rho_crit:.6e} kg m^-3")
    print(f"  Omega_Lambda,fid  = {omega_target:.3f}")
    print(f"  rho_Lambda (mass) = {rho_lambda_mass:.6e} kg m^-3")
    print(f"  rho_Lambda        = {rho_lambda_Jm3:.6e} J m^-3")
    print()

    print("Planck-scale comparison:")
    print(f"  rho_Pl            = {rho_Pl_Jm3:.6e} J m^-3")
    print(f"  rho_Lambda / rho_Pl ≈ {ratio_lambda_to_Pl:.3e}")
    print("  (This is the familiar ~1e-123 hierarchy.)")
    print()

    print("Effective microcavity mapping:")
    print(f"  DeltaE_fid                = {delta_E_fid:.6e} (dimensionless)")
    print(f"  scale_factor              = {scale_factor:.6e} J m^-3 per unit DeltaE")
    if k_scale is not None:
        print(f"  Check: Omega_Lambda,fid = k_scale * DeltaE_fid ≈ {k_scale * delta_E_fid:.3f}")
    print()
    print("Interpretation:")
    print("  - The tiny ratio rho_Lambda / rho_Pl ~ 1e-123 is set entirely by")
    print("    the (H0, G, c, hbar) scales, not by the microcavity itself.")
    print("  - The microcavity + non-cancelling rule supply an O(1e-3) shift")
    print("    DeltaE_fid in dimensionless lattice units.")
    print("  - Our calibration chooses the overall scale so that this DeltaE_fid")
    print("    corresponds to the observed Omega_Lambda ~ 0.7 at the fiducial slice.")
    print()
    print("At this rung we are *not* predicting the absolute magnitude of Lambda.")
    print("We are exposing the bookkeeping: how a dimensionless DeltaE_fid is")
    print("promoted to a physical rho_Lambda once H0 and fundamental constants")
    print("are specified.")
    print()


if __name__ == "__main__":
    main()