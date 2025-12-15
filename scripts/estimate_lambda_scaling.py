#!/usr/bin/env python3
"""
Estimate the mapping between the dimensionless microcavity ΔE(θ★)
and the observed vacuum energy density ρ_Λ.

This is a *toy* scaling check:

  - We take a simple ΛCDM-like cosmology with
      H0 ≈ 70 km/s/Mpc, Ω_Λ ≈ 0.7, Ω_m ≈ 0.3.
  - We compute the corresponding critical density ρ_crit and ρ_Λ = Ω_Λ ρ_crit.
  - We load the 1D microcavity scan ΔE(θ★) and look at ΔE at the
    Act II fiducial θ★ (from config/theta_star_config.json).
  - We then solve for a proportionality constant S such that

        ρ_Λ (observed) ≈ S * (-ΔE(θ★_fid))

    i.e. we treat -ΔE as a positive vacuum energy density and
    absorb all microscopic details into S.

This does *not* claim a physical derivation of Λ. It is just a way
to document what energy-density scale our toy ΔE would have to
represent if the θ★-selected vacuum were to match the observed Λ.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


# ---------------------------------------------------------------------
# 1. Cosmology helpers
# ---------------------------------------------------------------------


def compute_rho_lambda_observed(
    H0_km_s_Mpc: float = 70.0,
    omega_lambda: float = 0.7,
) -> tuple[float, float]:
    """
    Compute critical density ρ_crit and vacuum energy density ρ_Λ
    in SI units (J/m^3), for a given H0 and Ω_Λ.

    We use:
        H0_km_s_Mpc: Hubble constant in km/s/Mpc
        omega_lambda: Ω_Λ

    Returns:
        (rho_crit, rho_lambda) in J/m^3
    """
    # Physical constants (CODATA-ish)
    G = 6.67430e-11  # m^3 kg^-1 s^-2
    c = 2.99792458e8  # m/s
    MPC_TO_M = 3.0856775814913673e22  # m

    # Convert H0 to 1/s
    H0 = H0_km_s_Mpc * 1_000.0 / MPC_TO_M  # s^-1

    # Critical density: ρ_crit = 3 H0^2 / (8 π G) (kg/m^3)
    rho_crit_mass = 3.0 * H0**2 / (8.0 * np.pi * G)

    # Convert to energy density via E = ρ c^2
    rho_crit_energy = rho_crit_mass * c**2  # J/m^3

    # Vacuum energy density
    rho_lambda = omega_lambda * rho_crit_energy

    return rho_crit_energy, rho_lambda


# ---------------------------------------------------------------------
# 2. Load theta★ config and microcavity ΔE(θ★)
# ---------------------------------------------------------------------


def load_theta_star_config(
    path: str | Path = "config/theta_star_config.json",
) -> dict:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(
            f"Could not find theta★ config at {p}. "
            "Make sure origin-axiom-theta-star has exported it."
        )
    with p.open("r", encoding="utf-8") as f:
        cfg = json.load(f)
    return cfg


def normalize_band(band_raw) -> tuple[float, float]:
    """
    Accepts either:
      - [lo, hi] (list/tuple)
      - {'lo': ..., 'hi': ...}
      - {'min': ..., 'max': ...}
    and returns (lo, hi) as floats.
    """
    # list or tuple with two entries
    if isinstance(band_raw, (list, tuple)):
        if len(band_raw) != 2:
            raise ValueError(
                f"theta_star_band_rad list/tuple must have length 2, "
                f"got length {len(band_raw)}"
            )
        lo, hi = band_raw
        return float(lo), float(hi)

    # dict-like
    if isinstance(band_raw, dict):
        keys = {k.lower(): k for k in band_raw.keys()}
        if "lo" in keys and "hi" in keys:
            lo = band_raw[keys["lo"]]
            hi = band_raw[keys["hi"]]
        elif "min" in keys and "max" in keys:
            lo = band_raw[keys["min"]]
            hi = band_raw[keys["max"]]
        else:
            # Fallback: sort values
            vals = list(band_raw.values())
            if len(vals) != 2:
                raise ValueError(
                    "theta_star_band_rad dict must have 2 entries "
                    f"(lo/hi or min/max); got keys {list(band_raw.keys())}"
                )
            lo, hi = sorted(vals)
        return float(lo), float(hi)

    raise TypeError(
        "theta_star_band_rad must be list/tuple or dict; "
        f"got type {type(band_raw)}"
    )


def load_microcavity_scan(
    path: str | Path = "data/processed/theta_star_microcavity_scan_full_2pi.npz",
) -> dict:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(
            f"Could not find microcavity scan at {p}. "
            "Run src/scan_1d_theta_star_microcavity_full_band.py first."
        )
    # allow_pickle=True because the .npz contains an object array (metadata)
    data = np.load(p, allow_pickle=True)
    return {k: data[k] for k in data.files}


# ---------------------------------------------------------------------
# 3. Main report
# ---------------------------------------------------------------------


def main() -> None:
    print("=== Physical scaling check: microcavity ΔE(θ★) vs observed Λ ===\n")

    # 1) Observed ρ_Λ (toy ΛCDM numbers)
    rho_crit, rho_lambda = compute_rho_lambda_observed()
    print("-> ΛCDM-like cosmology (toy numbers)")
    print("   H0           ≈ 70 km/s/Mpc")
    print("   Ω_Λ          ≈ 0.7")
    print(f"   ρ_crit       ≈ {rho_crit:.3e} J/m^3")
    print(f"   ρ_Λ,obs      ≈ {rho_lambda:.3e} J/m^3\n")

    # 2) Load theta★ config
    cfg = load_theta_star_config()
    theta_fid = float(cfg["theta_star_fid_rad"])
    band_raw = cfg["theta_star_band_rad"]
    theta_lo, theta_hi = normalize_band(band_raw)

    print("-> Act II theta★ configuration")
    print(f"   θ★_fid       = {theta_fid:.6f} rad")
    print(f"   θ★ band      = [{theta_lo:.6f}, {theta_hi:.6f}] rad\n")

    # 3) Load microcavity scan and find ΔE at θ★_fid
    mc = load_microcavity_scan()
    print("-> Microcavity scan keys:", list(mc.keys()))

    # Try to find the theta array under several plausible names
    theta_key_candidates = ["theta", "theta_vals", "theta_grid", "theta_samples"]
    theta = None
    theta_key_used = None
    for k in theta_key_candidates:
        if k in mc:
            theta = mc[k]
            theta_key_used = k
            break

    if theta is None:
        raise KeyError(
            "Could not find a θ★ array in microcavity scan. "
            f"Available keys: {list(mc.keys())}. "
            "Tried names: " + ", ".join(theta_key_candidates)
        )

    # Try to find the ΔE array under several plausible names
    deltaE_key_candidates = ["deltaE", "deltaE_vals", "deltaE_theta", "DeltaE"]
        # Try to find the ΔE array under several plausible names
    deltaE_key_candidates = ["delta_E", "deltaE", "deltaE_vals", "deltaE_theta", "DeltaE"]
    deltaE = None
    deltaE_key_used = None
    for k in deltaE_key_candidates:
        if k in mc:
            deltaE = mc[k]
            deltaE_key_used = k
            break

    if deltaE is None:
        raise KeyError(
            "Could not find a ΔE(θ★) array in microcavity scan. "
            f"Available keys: {list(mc.keys())}. "
            "Tried names: " + ", ".join(deltaE_key_candidates)
        )

    print(f"   using θ★ key     = {theta_key_used!r}")
    print(f"   using ΔE(θ★) key = {deltaE_key_used!r}\n")

    if deltaE is None:
        raise KeyError(
            "Could not find a ΔE(θ★) array in microcavity scan. "
            f"Available keys: {list(mc.keys())}. "
            "Tried names: " + ", ".join(deltaE_key_candidates)
        )

    print(f"   using θ★ key    = {theta_key_used!r}")
    print(f"   using ΔE(θ★) key = {deltaE_key_used!r}\n")

    # Find the index nearest to θ★_fid
    idx_fid = int(np.argmin(np.abs(theta - theta_fid)))
    theta_fid_used = float(theta[idx_fid])
    deltaE_fid = float(deltaE[idx_fid])

    print("-> Microcavity ΔE(θ★) scan")
    print(f"   scan file    = data/processed/theta_star_microcavity_scan_full_2pi.npz")
    print(f"   n_θ          = {theta.size}")
    print(f"   ΔE_min       = {deltaE.min():.3e}")
    print(f"   ΔE_max       = {deltaE.max():.3e}")
    print(f"   θ★_fid_used  = {theta_fid_used:.6f} rad (nearest grid point)")
    print(f"   ΔE(θ★_fid)   = {deltaE_fid:.3e}  (dimensionless)\n")

    # 4) Toy mapping: ρ_Λ ≈ S * (-ΔE(θ★_fid))
    #    We treat -ΔE as the positive vacuum energy density.
    if deltaE_fid >= 0.0:
        print("WARNING: ΔE(θ★_fid) is non-negative; the simple mapping "
              "ρ_Λ ≈ S * (-ΔE) would be awkward.\n")

    S = rho_lambda / (-deltaE_fid)  # J/m^3 per unit of (-ΔE)
    print("-> Toy scaling factor")
    print("   We define ρ_vac(θ★) ≈ S * (-ΔE(θ★))")
    print(f"   S (scale)    ≈ {S:.3e} J/m^3 per unit of (-ΔE)\n")

    # 5) What does this imply for other θ★ values in the Act II band?
    mask_band = (theta >= theta_lo) & (theta <= theta_hi)
    deltaE_band = deltaE[mask_band]

    rho_vac_band = S * (-deltaE_band)
    rho_vac_min = float(rho_vac_band.min())
    rho_vac_max = float(rho_vac_band.max())

    print("-> Implied ρ_vac across the Act II θ★ band")
    print(f"   min ρ_vac(θ★ in band) ≈ {rho_vac_min:.3e} J/m^3")
    print(f"   max ρ_vac(θ★ in band) ≈ {rho_vac_max:.3e} J/m^3")
    print("   (by construction, ρ_vac at θ★_fid matches ρ_Λ,obs)\n")

    print("Interpretation:")
    print("  This script does *not* prove that the θ★-microcavity model")
    print("  predicts the observed Λ. Instead, it makes the scaling")
    print("  assumption explicit and documents what energy-density scale")
    print("  a unit of dimensionless ΔE would need to represent.")
    print("  Any future, more realistic microphysics can then be checked")
    print("  against this required scale.")


if __name__ == "__main__":
    main()