#!/usr/bin/env python3
"""
Phase 4: FRW-inspired toy diagnostics on the F1 mapping.

This script:

  - Reads the F1 sanity curve from
      phase4/outputs/tables/phase4_F1_sanity_curve.csv
    (theta, E_vac).

  - Rescales E_vac(theta) into a dimensionless Omega_Lambda(theta)
    with mean ~0.7.

  - Evaluates a toy FRW-like quantity
        H^2(a; theta) = Omega_r a^{-4} + Omega_m a^{-3} + Omega_Lambda(theta)
    on a *late-time* scale-factor grid a in [0.5, 1].

  - Applies a simple sanity criterion:
      * H^2(a; theta) > 0 for all a in the grid; and
      * max(H^2) / min(H^2) <= frw_sanity_ratio_max.

  - Writes:
      * a JSON diagnostics file with global extrema and moments; and
      * a per-theta CSV mask indicating which thetas pass the toy FRW
        sanity test.

This is deliberately non-binding and toy-level: it does not fix a
physical model, does not define a Phase 4 theta-filter, and is used
only as a structural sanity probe for the F1 mapping.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Tuple

import numpy as np


REPO_ROOT = Path(__file__).resolve().parents[3]


def load_f1_sanity_curve() -> Tuple[np.ndarray, np.ndarray]:
    """
    Load the F1 sanity curve from the Phase 4 outputs.

    Returns
    -------
    thetas : np.ndarray
        Theta grid (radians).
    evac : np.ndarray
        E_vac(theta) values from the F1 mapping.
    """
    curve_path = (
        REPO_ROOT
        / "phase4"
        / "outputs"
        / "tables"
        / "phase4_F1_sanity_curve.csv"
    )

    if not curve_path.is_file():
        raise FileNotFoundError(
            f"F1 sanity curve not found at {curve_path}. "
            "Run phase4/src/phase4/run_f1_sanity.py first."
        )

    thetas = []
    evac = []
    with curve_path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            thetas.append(float(row["theta"]))
            evac.append(float(row["E_vac"]))

    return np.asarray(thetas, dtype=float), np.asarray(evac, dtype=float)


def main() -> None:
    # ------------------------------------------------------------------
    # 1. Load F1 sanity curve
    # ------------------------------------------------------------------
    thetas, evac = load_f1_sanity_curve()

    evac_min = float(np.min(evac))
    evac_max = float(np.max(evac))
    evac_mean = float(np.mean(evac))

    # ------------------------------------------------------------------
    # 2. Rescale to a dimensionless Omega_Lambda(theta)
    # ------------------------------------------------------------------
    omega_lambda_mean_target = 0.7  # toy target mean, non-physical
    evac_norm = evac / evac_mean
    scale = omega_lambda_mean_target / float(np.mean(evac_norm))
    omega_lambda_theta = scale * evac_norm

    omega_lambda_min = float(np.min(omega_lambda_theta))
    omega_lambda_max = float(np.max(omega_lambda_theta))
    omega_lambda_mean = float(np.mean(omega_lambda_theta))

    # ------------------------------------------------------------------
    # 3. FRW-like toy parameters and late-time scale-factor grid
    # ------------------------------------------------------------------
    omega_m = 0.3
    omega_r = 0.0

    # Late-time window only: toy choice, non-binding.
    a_min = 0.5
    a_max = 1.0
    n_a = 128
    a_grid = np.linspace(a_min, a_max, n_a)

    frw_sanity_ratio_max = 10.0  # bound on max(H^2)/min(H^2) per theta

    sane_mask = []
    H2_min_global = float("inf")
    H2_max_global = float("-inf")

    for omega_L in omega_lambda_theta:
        H2 = omega_r * a_grid**-4 + omega_m * a_grid**-3 + omega_L

        H2_min = float(np.min(H2))
        H2_max = float(np.max(H2))

        if H2_min < H2_min_global:
            H2_min_global = H2_min
        if H2_max > H2_max_global:
            H2_max_global = H2_max

        if H2_min <= 0.0:
            sane = False
        else:
            ratio = H2_max / H2_min
            sane = ratio <= frw_sanity_ratio_max

        sane_mask.append(sane)

    sane_arr = np.asarray(sane_mask, dtype=bool)
    frac_sane = float(np.mean(sane_arr))

    # ------------------------------------------------------------------
    # 4. Write diagnostics and per-theta mask
    # ------------------------------------------------------------------
    out_dir = REPO_ROOT / "phase4" / "outputs" / "tables"
    out_dir.mkdir(parents=True, exist_ok=True)

    diag_path = out_dir / "phase4_F1_frw_toy_diagnostics.json"
    mask_path = out_dir / "phase4_F1_frw_toy_mask.csv"

    diagnostics = {
        "mapping_family": "F1",
        "source_curve": str(
            REPO_ROOT
            / "phase4"
            / "outputs"
            / "tables"
            / "phase4_F1_sanity_curve.csv"
        ),
        "omega_m": omega_m,
        "omega_r": omega_r,
        "omega_lambda_mean_target": omega_lambda_mean_target,
        "evac_min": evac_min,
        "evac_max": evac_max,
        "evac_mean": evac_mean,
        "omega_lambda_min": omega_lambda_min,
        "omega_lambda_max": omega_lambda_max,
        "omega_lambda_mean": omega_lambda_mean,
        "a_min": a_min,
        "a_max": a_max,
        "n_a": int(n_a),
        "frw_sanity_ratio_max": frw_sanity_ratio_max,
        "frac_sane": frac_sane,
        "H2_min_global": H2_min_global,
        "H2_max_global": H2_max_global,
    }

    with diag_path.open("w", encoding="utf-8") as f:
        json.dump(diagnostics, f, indent=2, sort_keys=True)

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
