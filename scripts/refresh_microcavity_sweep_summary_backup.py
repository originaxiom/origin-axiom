#!/usr/bin/env python3
"""
Refresh microcavity_sweep_summary.json with robust NPZ parsing.

This script:
  • Finds all microcavity_sweep_*.npz files in data/processed/
  • Accepts any historical naming for theta and deltaE arrays
  • Extracts ΔE_min, ΔE_max, ΔE(fid)
  • Saves to JSON in the same structure as before
"""

import json
import numpy as np
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed"
SUMMARY_PATH = DATA / "microcavity_sweep_summary.json"

# --- Fiducial theta★ (from flavour) ---
theta_fid_nominal = 3.63
print(f"Using theta_fid_nominal = {theta_fid_nominal:.6f} rad")

# Keys for compatibility
THETA_KEYS = ["theta_grid", "theta", "theta_vals"]
DELTA_KEYS = ["deltaE", "delta_E", "deltaE_vals", "deltaE_theta", "deltaE_values"]

results = {}

# ---------------------------------------------------------
# Iterate over all NPZ sweep files
# ---------------------------------------------------------
for npz_path in sorted(DATA.glob("microcavity_sweep_*.npz")):
    name = npz_path.stem
    try:
        arr = np.load(npz_path)
        keys = arr.files
    except Exception as e:
        print(f"[ERROR] Could not read {npz_path}: {e}")
        continue

    # -----------------------------------------------------
    # Locate theta array
    # -----------------------------------------------------
    theta_key = None
    for key in THETA_KEYS:
        if key in keys:
            theta_key = key
            break

    if theta_key is None:
        print(f"[WARN] {npz_path} missing theta array (keys={keys}) — skipping")
        continue

    theta = np.asarray(arr[theta_key]).astype(float)

    # -----------------------------------------------------
    # Locate deltaE array
    # -----------------------------------------------------
    delta_key = None
    for key in DELTA_KEYS:
        if key in keys:
            delta_key = key
            break

    if delta_key is None:
        print(f"[WARN] {npz_path} missing deltaE array (keys={keys}) — skipping")
        continue

    deltaE = np.asarray(arr[delta_key]).astype(float)

    # -----------------------------------------------------
    # Sanity checks
    # -----------------------------------------------------
    if theta.shape != deltaE.shape:
        print(f"[WARN] Shape mismatch in {npz_path}: "
              f"theta {theta.shape}, deltaE {deltaE.shape} — skipping")
        continue

    # Parse metadata
    N = int(arr["N"]) if "N" in keys else None
    mc = float(arr["mass_contrast"]) if "mass_contrast" in keys else None
    w = float(arr["cavity_width"]) if "cavity_width" in keys else None

    # Indices
    i_min = int(np.argmin(deltaE))
    i_max = int(np.argmax(deltaE))
    i_fid = int(np.argmin(abs(theta - theta_fid_nominal)))

    # Build entry
    results[name] = {
        "N": N,
        "mass_contrast": mc,
        "cavity_width": w,
        "theta_fid": float(theta[i_fid]),
        "theta_min": float(theta[i_min]),
        "theta_max": float(theta[i_max]),
        "deltaE_fid": float(deltaE[i_fid]),
        "deltaE_min": float(deltaE[i_min]),
        "deltaE_max": float(deltaE[i_max]),
    }

    print(f"[OK] {name}: ΔE(fid)={deltaE[i_fid]:.3e}, "
          f"min={deltaE[i_min]:.3e}, max={deltaE[i_max]:.3e}")

# ---------------------------------------------------------
# Final summary JSON
# ---------------------------------------------------------
summary_data = {
    "theta_fid_nominal": theta_fid_nominal,
    "results": results,
}

SUMMARY_PATH.write_text(json.dumps(summary_data, indent=2))
print(f"\nWrote updated summary to {SUMMARY_PATH}")
print(f"Updated {len(results)} entries, skipped {27 - len(results)}.")