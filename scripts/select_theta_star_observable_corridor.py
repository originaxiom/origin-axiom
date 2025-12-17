#!/usr/bin/env python3
"""
R13: Select a theta_star corridor that yields observationally acceptable FRW universes.

Criteria (hard-coded for now):
  - 0.6 <= Omega_Lambda <= 0.8
  - 12.0 <= t0 <= 15.0 Gyr
  - q0 < 0  (accelerating today)

Reads:
  data/processed/effective_vacuum_theta_frw_scan.npz

Writes:
  data/processed/theta_star_observable_corridor.json
"""

import json
from pathlib import Path

import numpy as np

SCAN_PATH = Path("data/processed/effective_vacuum_theta_frw_scan.npz")
OUT_PATH = Path("data/processed/theta_star_observable_corridor.json")


def main() -> None:
    print("=== R13: theta_star observable corridor selection ===")

    if not SCAN_PATH.exists():
        raise FileNotFoundError(f"Scan file not found: {SCAN_PATH}")

    data = np.load(SCAN_PATH)
    keys = list(data.files)

    print("Loaded FRW scan:", SCAN_PATH)
    print("Available keys:", keys)

    # --- Locate core arrays using actual key names from the scan file ---

    # theta grid
    if "theta_scan" in data:
        theta = np.asarray(data["theta_scan"], dtype=float)
    elif "theta_grid" in data:
        theta = np.asarray(data["theta_grid"], dtype=float)
    elif "theta" in data:
        theta = np.asarray(data["theta"], dtype=float)
    else:
        raise KeyError(
            "Could not find theta grid in scan file. "
            "Expected one of: 'theta_scan', 'theta_grid', 'theta'."
        )

    # Omega_Lambda
    if "omega_lambda_scan" in data:
        omega_lambda = np.asarray(data["omega_lambda_scan"], dtype=float)
    elif "omega_lambda" in data:
        omega_lambda = np.asarray(data["omega_lambda"], dtype=float)
    elif "Omega_Lambda" in data:
        omega_lambda = np.asarray(data["Omega_Lambda"], dtype=float)
    else:
        raise KeyError(
            "Could not find Omega_Lambda array in scan file. "
            "Expected one of: 'omega_lambda_scan', 'omega_lambda', 'Omega_Lambda'."
        )

    # Age in Gyr
    if "t0_gyr_scan" in data:
        t0_Gyr = np.asarray(data["t0_gyr_scan"], dtype=float)
    elif "t0_Gyr" in data:
        t0_Gyr = np.asarray(data["t0_Gyr"], dtype=float)
    else:
        raise KeyError(
            "Could not find age array in scan file. "
            "Expected one of: 't0_gyr_scan', 't0_Gyr'."
        )

    # Deceleration parameter
    if "q0_scan" in data:
        q0 = np.asarray(data["q0_scan"], dtype=float)
    elif "q0" in data:
        q0 = np.asarray(data["q0"], dtype=float)
    else:
        raise KeyError(
            "Could not find q0 array in scan file. "
            "Expected one of: 'q0_scan', 'q0'."
        )

    # --- Sanity check shapes ---

    if not (
        theta.shape == omega_lambda.shape == t0_Gyr.shape == q0.shape
    ):
        raise ValueError(
            "Shape mismatch between arrays:\n"
            f"  theta        : {theta.shape}\n"
            f"  omega_lambda : {omega_lambda.shape}\n"
            f"  t0_Gyr       : {t0_Gyr.shape}\n"
            f"  q0           : {q0.shape}"
        )

    print()
    print("Global ranges over theta_star band:")
    print(f"  theta range        : {theta.min():.3f} -> {theta.max():.3f} rad")
    print(f"  Omega_Lambda range : {omega_lambda.min():.3f} -> {omega_lambda.max():.3f}")
    print(f"  t0 range           : {t0_Gyr.min():.2f} -> {t0_Gyr.max():.2f} Gyr")
    print(f"  q0 range           : {q0.min():.3f} -> {q0.max():.3f}")

    # --- Selection cuts (crude observational window) ---

    OMEGA_MIN = 0.60
    OMEGA_MAX = 0.80
    T0_MIN = 12.0
    T0_MAX = 15.0

    mask = (
        (omega_lambda >= OMEGA_MIN)
        & (omega_lambda <= OMEGA_MAX)
        & (t0_Gyr >= T0_MIN)
        & (t0_Gyr <= T0_MAX)
        & (q0 < 0.0)
    )

    idx = np.where(mask)[0]
    n_tot = theta.size
    n_sel = idx.size

    print()
    print("Selection criteria:")
    print(f"  {OMEGA_MIN:.2f} <= Omega_Lambda <= {OMEGA_MAX:.2f}")
    print(f"  {T0_MIN:.2f} <= t0 <= {T0_MAX:.2f} Gyr")
    print("  q0 < 0 (accelerating)")
    print()
    frac = 100.0 * n_sel / float(n_tot) if n_tot > 0 else 0.0
    print(f"Selected {n_sel} / {n_tot} samples ({frac:.1f}%)")

    if n_sel == 0:
        print()
        print("No samples passed the selection cuts; nothing to save.")
        return

    theta_sel = theta[idx]
    omega_sel = omega_lambda[idx]
    t0_sel = t0_Gyr[idx]
    q0_sel = q0[idx]

    print()
    print("theta_star corridor (selected region):")
    print(f"  theta range        : {theta_sel.min():.3f} -> {theta_sel.max():.3f} rad")
    print(f"  Omega_Lambda range : {omega_sel.min():.3f} -> {omega_sel.max():.3f}")
    print(f"  t0 range           : {t0_sel.min():.2f} -> {t0_sel.max():.2f} Gyr")
    print(f"  q0 range           : {q0_sel.min():.3f} -> {q0_sel.max():.3f}")

    print()
    print("Accepted samples (theta, Omega_Lambda, t0[Gyr], q0):")
    for i in idx:
        print(
            f"  {theta[i]:6.3f}  {omega_lambda[i]:6.3f}  "
            f"{t0_Gyr[i]:6.2f}  {q0[i]:7.3f}"
        )

    # --- Save compact JSON summary ---

    summary = {
        "scan_file": str(SCAN_PATH),
        "selection_cuts": {
            "Omega_Lambda_min": OMEGA_MIN,
            "Omega_Lambda_max": OMEGA_MAX,
            "t0_min_Gyr": T0_MIN,
            "t0_max_Gyr": T0_MAX,
            "q0_condition": "< 0",
        },
        "n_total": int(n_tot),
        "n_selected": int(n_sel),
        "fraction_selected": float(n_sel) / float(n_tot) if n_tot > 0 else 0.0,
        "theta_corridor": {
            "min_rad": float(theta_sel.min()),
            "max_rad": float(theta_sel.max()),
        },
        "Omega_Lambda_selected": {
            "min": float(omega_sel.min()),
            "max": float(omega_sel.max()),
        },
        "t0_selected_Gyr": {
            "min": float(t0_sel.min()),
            "max": float(t0_sel.max()),
        },
        "q0_selected": {
            "min": float(q0_sel.min()),
            "max": float(q0_sel.max()),
        },
    }

    OUT_PATH.write_text(json.dumps(summary, indent=2))
    print()
    print("Wrote selection summary to", OUT_PATH)


if __name__ == "__main__":
    main()