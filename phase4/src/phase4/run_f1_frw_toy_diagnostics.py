#!/usr/bin/env python3
"""
Phase 4: FRW-inspired toy diagnostics for the F1 mapping.

This script:
  - reads the F1 vacuum-energy-like curve E_vac(theta) from
    phase4/outputs/tables/phase4_F1_sanity_curve.csv;
  - rescales it to a toy Omega_Lambda(theta) field with mean ~0.7;
  - evaluates a simple FRW-like H^2(a; theta) over a scale-factor grid;
  - constructs a Boolean "FRW-sane" mask per theta based on positivity
    and a bounded variation criterion; and
  - writes JSON summary diagnostics and a per-theta CSV mask.

All quantities are dimensionless and explicitly non-physical; this is
a structural sanity check, not a cosmological fit.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Tuple, List

import numpy as np

# Repo root (…/origin-axiom)
REPO_ROOT = Path(__file__).resolve().parents[3]


def load_f1_curve(path: Path) -> Tuple[np.ndarray, np.ndarray]:
    """Load theta and E_vac(theta) from the F1 sanity curve CSV."""
    if not path.is_file():
        raise SystemExit(
            f"[F1_FRW] ERROR: sanity curve not found at {path}. "
            "Run phase4/src/phase4/run_f1_sanity.py first."
        )

    thetas: List[float] = []
    evac: List[float] = []

    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if "theta" not in reader.fieldnames or "E_vac" not in reader.fieldnames:
            raise SystemExit(
                "[F1_FRW] ERROR: expected columns 'theta' and 'E_vac' "
                f"in {path}, got {reader.fieldnames}"
            )
        for row in reader:
            thetas.append(float(row["theta"]))
            evac.append(float(row["E_vac"]))

    thetas_arr = np.asarray(thetas, dtype=float)
    evac_arr = np.asarray(evac, dtype=float)

    return thetas_arr, evac_arr


def main() -> None:
    curve_path = REPO_ROOT / "phase4" / "outputs" / "tables" / "phase4_F1_sanity_curve.csv"
    thetas, evac = load_f1_curve(curve_path)

    if evac.size == 0:
        raise SystemExit("[F1_FRW] ERROR: empty E_vac(theta) array")

    evac_mean = float(np.mean(evac))
    if evac_mean <= 0.0:
        raise SystemExit(
            f"[F1_FRW] ERROR: non-positive mean E_vac(theta) = {evac_mean}"
        )

    # Dimensionless normalisation of E_vac(theta)
    evac_dimless = evac / evac_mean  # mean ~ 1

    # Toy FRW parameters (dimensionless, non-physical)
    omega_m = 0.3
    omega_r = 0.0
    omega_lambda_mean_target = 0.7

    # Scale evac_dimless so that <Omega_Lambda(theta)> ~= omega_lambda_mean_target
    scale = omega_lambda_mean_target / float(np.mean(evac_dimless))
    omega_lambda_theta = scale * evac_dimless

    # Scale-factor grid for toy FRW evaluation
    a_grid = np.linspace(0.1, 1.0, 64, dtype=float)

    # Base H^2(a) contribution from matter + radiation only
    H2_base = omega_r * a_grid**-4 + omega_m * a_grid**-3

    H2_min_list: List[float] = []
    H2_max_list: List[float] = []
    sane_mask: List[bool] = []

    ratio_max = 10.0  # toy bound on H^2 variation over the a-grid

    for omega_L in omega_lambda_theta:
        H2_theta = H2_base + omega_L
        h2_min = float(np.min(H2_theta))
        h2_max = float(np.max(H2_theta))
        H2_min_list.append(h2_min)
        H2_max_list.append(h2_max)

        ratio = h2_max / h2_min if h2_min > 0.0 else np.inf
        sane = (h2_min > 0.0) and (ratio <= ratio_max)
        sane_mask.append(bool(sane))

    H2_min_arr = np.asarray(H2_min_list, dtype=float)
    H2_max_arr = np.asarray(H2_max_list, dtype=float)
    sane_arr = np.asarray(sane_mask, dtype=bool)

    frac_sane = float(np.mean(sane_arr.astype(float)))

    diagnostics = {
        "mapping_family": "F1",
        "source_curve": str(curve_path),
        "omega_m": omega_m,
        "omega_r": omega_r,
        "omega_lambda_mean_target": omega_lambda_mean_target,
        "evac_min": float(np.min(evac)),
        "evac_max": float(np.max(evac)),
        "evac_mean": evac_mean,
        "omega_lambda_min": float(np.min(omega_lambda_theta)),
        "omega_lambda_max": float(np.max(omega_lambda_theta)),
        "omega_lambda_mean": float(np.mean(omega_lambda_theta)),
        "a_min": float(a_grid[0]),
        "a_max": float(a_grid[-1]),
        "frw_sanity_ratio_max": ratio_max,
        "frac_sane": frac_sane,
        "H2_min_global": float(np.min(H2_min_arr)),
        "H2_max_global": float(np.max(H2_max_arr)),
    }

    out_dir = REPO_ROOT / "phase4" / "outputs" / "tables"
    out_dir.mkdir(parents=True, exist_ok=True)
    diag_path = out_dir / "phase4_F1_frw_toy_diagnostics.json"
    mask_path = out_dir / "phase4_F1_frw_toy_mask.csv"

    # Write JSON diagnostics
    with diag_path.open("w", encoding="utf-8") as f:
        json.dump(diagnostics, f, indent=2, sort_keys=True)

    # Per-theta CSV mask
    with mask_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["theta", "omega_lambda", "frw_sane"])
        for th, omega_L, sane in zip(thetas, omega_lambda_theta, sane_arr):
            writer.writerow([float(th), float(omega_L), int(bool(sane))])

    print("[F1_FRW] Wrote diagnostics to", diag_path)
    print("[F1_FRW] Wrote per-theta mask CSV to", mask_path)
    print("[F1_FRW] Summary:")
    for k, v in diagnostics.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
