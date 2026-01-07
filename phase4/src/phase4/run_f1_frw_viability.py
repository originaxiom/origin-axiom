#!/usr/bin/env python
"""
Phase 4 – F1 FRW viability diagnostic.

This script reads the F1 sanity curve CSV, maps E_vac(theta) to a toy
Omega_Lambda(theta) with <Omega_Lambda> ~ 0.7, and then applies a set
of minimally physical FRW-style viability checks:

- Dimensionless age integral t0 * H0, converted to an approximate age
  in Gyr (using H0 ~ 70 km/s/Mpc).
- Existence of a matter-dominated era at a ~ 0.3 (Omega_m a^-3 >
  Omega_Lambda).
- Late-time acceleration at a ~ 1 (Omega_Lambda dominates over matter
  and radiation).
- A smooth, positive H^2(a; theta) over a late-time window with a
  bounded variation factor.

The result is a per-theta mask flagging "FRW viable" theta values and
a summary diagnostics JSON recording global fractions and extrema.

All thresholds are deliberately loose and are documented in the Phase 4
paper; they define a *minimal viability corridor*, not a precise fit
to data.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Tuple, Dict, Any

import numpy as np


# Repo root inferred from this file location:
#   origin-axiom/phase4/src/phase4/run_f1_frw_viability.py
REPO_ROOT = Path(__file__).resolve().parents[3]


def load_f1_sanity_curve(path: Path) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    """
    Load the F1 sanity curve from CSV.

    The expected header is at least:
      theta, E_vac

    Any additional columns are ignored here. The metadata dict is kept
    minimal; richer metadata lives in the Phase 4 logs and paper.
    """
    thetas = []
    evac = []
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            thetas.append(float(row["theta"]))
            evac.append(float(row["E_vac"]))

    thetas_arr = np.asarray(thetas, dtype=float)
    evac_arr = np.asarray(evac, dtype=float)
    meta: Dict[str, Any] = {
        "n_grid": int(thetas_arr.size),
        "theta_min": float(thetas_arr.min()) if thetas_arr.size else None,
        "theta_max": float(thetas_arr.max()) if thetas_arr.size else None,
    }
    return thetas_arr, evac_arr, meta


def compute_age_Gyr_for_omega_lambda(
    omega_lambda: float,
    omega_m: float,
    omega_r: float,
    H0_km_s_Mpc: float = 70.0,
    a_min: float = 1.0e-4,
    a_max: float = 1.0,
    n_a: int = 4096,
) -> float:
    """
    Compute the FRW age of the universe in Gyr for a flat model with
    (Omega_r, Omega_m, Omega_lambda) and H0.

    Uses the standard dimensionless age integral

      t0 * H0 = ∫_0^1 da / (a * E(a)),

    with E(a) = sqrt(Omega_r a^-4 + Omega_m a^-3 + Omega_lambda).
    The integral is evaluated numerically on [a_min, a_max]; the
    contribution from [0, a_min] is negligible for our purposes.

    Conversion to Gyr uses the classic approximation

      1 / H0 ≈ 9.78 / h  Gyr,  with  h = H0 / 100.
    """
    a = np.linspace(a_min, a_max, n_a, dtype=float)
    H2 = omega_r / a**4 + omega_m / a**3 + omega_lambda
    E = np.sqrt(H2)
    integrand = 1.0 / (a * E)
    t0_H0 = float(np.trapezoid(integrand, a))  # dimensionless t0 * H0

    h = H0_km_s_Mpc / 100.0
    H0_inv_Gyr = 9.78 / h  # standard cosmology textbook approximation
    return t0_H0 * H0_inv_Gyr


def main() -> None:
    repo_root = REPO_ROOT

    curve_path = repo_root / "phase4" / "outputs" / "tables" / "phase4_F1_sanity_curve.csv"
    diag_path = repo_root / "phase4" / "outputs" / "tables" / "phase4_F1_frw_viability_diagnostics.json"
    mask_path = repo_root / "phase4" / "outputs" / "tables" / "phase4_F1_frw_viability_mask.csv"

    diag_path.parent.mkdir(parents=True, exist_ok=True)

    thetas, evac, _meta = load_f1_sanity_curve(curve_path)
    thetas_arr = np.asarray(thetas, dtype=float)
    evac_arr = np.asarray(evac, dtype=float)

    # FRW and mapping parameters (kept in spirit with the FRW toy script)
    omega_m = 0.3
    omega_r = 0.0
    omega_lambda_mean_target = 0.7
    H0_km_s_Mpc = 70.0

    # Age viability window (broad, centred near ~13.8 Gyr)
    age_min_Gyr = 10.0
    age_max_Gyr = 20.0

    # Late-time smoothness window for H^2
    a_min_sanity = 0.5
    a_max_sanity = 1.0
    n_a_sanity = 256
    frw_sanity_ratio_max = 10.0

    # Map E_vac(theta) to Omega_Lambda(theta) by rescaling to match
    # the target mean, mirroring the FRW toy behaviour.
    evac_mean = float(evac_arr.mean())
    if evac_mean <= 0.0:
        raise RuntimeError("Non-positive mean E_vac; cannot define Omega_Lambda(theta).")

    scale = omega_lambda_mean_target / evac_mean
    omega_lambda_theta = scale * evac_arr

    # Precompute grids
    a_sanity = np.linspace(a_min_sanity, a_max_sanity, n_a_sanity, dtype=float)

    ages_Gyr = []
    has_matter_era = []
    has_late_accel = []
    has_smooth_H2 = []

    for omega_L in omega_lambda_theta:
        # Age in Gyr
        age_Gyr = compute_age_Gyr_for_omega_lambda(
            omega_lambda=omega_L,
            omega_m=omega_m,
            omega_r=omega_r,
            H0_km_s_Mpc=H0_km_s_Mpc,
        )
        ages_Gyr.append(age_Gyr)

        # Matter-dominated era at a ~ 0.3: require matter to dominate
        # over Lambda at that scale factor.
        a_m = 0.3
        rho_m_m = omega_m / a_m**3
        rho_L_m = omega_L
        has_matter_era.append(rho_m_m > rho_L_m)

        # Late-time acceleration at a ~ 1: require Lambda to dominate
        # over matter + radiation.
        a_late = 1.0
        rho_m_late = omega_m / a_late**3
        rho_r_late = omega_r / a_late**4
        has_late_accel.append(omega_L > (rho_m_late + rho_r_late))

        # Smooth, positive H^2 over late-time window
        H2_sanity = omega_r / a_sanity**4 + omega_m / a_sanity**3 + omega_L
        H2_min = float(H2_sanity.min())
        H2_max = float(H2_sanity.max())
        if H2_min <= 0.0:
            has_smooth_H2.append(False)
        else:
            has_smooth_H2.append((H2_max / H2_min) <= frw_sanity_ratio_max)

    ages_Gyr_arr = np.asarray(ages_Gyr, dtype=float)
    has_matter_arr = np.asarray(has_matter_era, dtype=bool)
    has_late_arr = np.asarray(has_late_accel, dtype=bool)
    smooth_arr = np.asarray(has_smooth_H2, dtype=bool)

    age_window_ok = (ages_Gyr_arr >= age_min_Gyr) & (ages_Gyr_arr <= age_max_Gyr)
    viable_arr = age_window_ok & has_matter_arr & has_late_arr & smooth_arr

    diagnostics = {
        "mapping_family": "F1",
        "source_curve": str(curve_path),
        "omega_m": float(omega_m),
        "omega_r": float(omega_r),
        "omega_lambda_mean_target": float(omega_lambda_mean_target),
        "H0_km_s_Mpc": float(H0_km_s_Mpc),
        "age_window_Gyr": [float(age_min_Gyr), float(age_max_Gyr)],
        "age_Gyr_min": float(ages_Gyr_arr.min()),
        "age_Gyr_max": float(ages_Gyr_arr.max()),
        "age_Gyr_mean": float(ages_Gyr_arr.mean()),
        "frac_has_matter_era": float(has_matter_arr.mean()),
        "frac_has_late_accel": float(has_late_arr.mean()),
        "frac_smooth_H2": float(smooth_arr.mean()),
        "frac_age_window_ok": float(age_window_ok.mean()),
        "frac_viable": float(viable_arr.mean()),
        "theta_min_global": float(thetas_arr.min()),
        "theta_max_global": float(thetas_arr.max()),
    }

    with diag_path.open("w", encoding="utf-8") as f:
        json.dump(diagnostics, f, indent=2, sort_keys=True)

    with mask_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "theta",
                "E_vac",
                "omega_lambda",
                "age_Gyr",
                "has_matter_era",
                "has_late_accel",
                "smooth_H2",
                "frw_viable",
            ]
        )
        for th, ev, omega_L, age_Gyr, hm, hl, sm, ok in zip(
            thetas_arr,
            evac_arr,
            omega_lambda_theta,
            ages_Gyr_arr,
            has_matter_arr,
            has_late_arr,
            smooth_arr,
            viable_arr,
        ):
            writer.writerow(
                [
                    float(th),
                    float(ev),
                    float(omega_L),
                    float(age_Gyr),
                    int(bool(hm)),
                    int(bool(hl)),
                    int(bool(sm)),
                    int(bool(ok)),
                ]
            )

    print("[F1_FRW_VIABILITY] Wrote diagnostics to", diag_path)
    print("[F1_FRW_VIABILITY] Wrote per-theta mask CSV to", mask_path)
    print("[F1_FRW_VIABILITY] Summary:")
    for k, v in diagnostics.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
