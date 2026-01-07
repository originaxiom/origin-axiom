#!/usr/bin/env python3
"""
Phase 4 - Rung 11: FRW ΛCDM-like probe on the F1 mapping.

This script reads the FRW viability mask produced by
`run_f1_frw_viability.py` and defines a simple "ΛCDM-like" window in
terms of:

- a target vacuum fraction Ω_Λ^target ≈ 0.7 with a tolerance ΔΩ_Λ, and
- a target age t0^target ≈ 13.8 Gyr with a tolerance Δt,

restricted to rows that are already marked as FRW-viable. The result is:

- a JSON diagnostics file summarising the ΛCDM-like subset and its
  θ-extent; and
- a per-grid CSV mask with an added `lcdm_like` column.

This is still a toy diagnostic: it is not a fit to real data, and the
thresholds are intentionally broad. Its role is to demonstrate that
the Phase 3 → Phase 4 pipeline can support FRW histories that are at
least roughly compatible with late-time ΛCDM-like cosmology.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any, Dict, List

import numpy as np

# ----------------------------------------------------------------------
# Local helpers: repo root + outputs/tables directory
# ----------------------------------------------------------------------


def get_repo_root() -> Path:
    """
    Infer the repo root by walking up from this file.

    Assumes the file is located at:
      <repo_root>/phase4/src/phase4/run_f1_frw_lcdm_probe.py
    """
    here = Path(__file__).resolve()
    # .../origin-axiom/phase4/src/phase4/run_f1_frw_lcdm_probe.py
    # parents[0] = .../phase4/src/phase4
    # parents[1] = .../phase4/src
    # parents[2] = .../phase4
    # parents[3] = .../origin-axiom
    return here.parents[3]


def ensure_phase4_outputs_dir(subdir: str) -> Path:
    """
    Ensure phase4/outputs/<subdir>/ exists and return its Path.
    """
    repo_root = get_repo_root()
    base = repo_root / "phase4" / "outputs" / subdir
    base.mkdir(parents=True, exist_ok=True)
    return base


# FRW / ΛCDM-like toy parameters
OMEGA_M: float = 0.3
OMEGA_R: float = 0.0
OMEGA_L_TARGET: float = 0.7
OMEGA_L_TOL: float = 0.1  # |Ω_Λ - Ω_Λ^target| <= 0.1

AGE_TARGET_GYR: float = 13.8
AGE_TOL_GYR: float = 1.0  # |t0 - 13.8 Gyr| <= 1 Gyr

H0_KM_S_MPC: float = 70.0  # kept for documentation only


def load_viability_mask(path: Path) -> List[Dict[str, Any]]:
    """
    Load the FRW viability mask CSV produced by run_f1_frw_viability.py.

    Expected columns:
      theta, E_vac, omega_lambda, age_Gyr,
      has_matter_era, has_late_accel, smooth_H2, frw_viable
    """
    rows: List[Dict[str, Any]] = []
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        expected = {
            "theta",
            "E_vac",
            "omega_lambda",
            "age_Gyr",
            "has_matter_era",
            "has_late_accel",
            "smooth_H2",
            "frw_viable",
        }
        missing = expected.difference(fieldnames)
        if missing:
            raise RuntimeError(
                f"[F1_FRW_LCDM] Expected columns {sorted(expected)}, "
                f"found {sorted(fieldnames)}; missing {sorted(missing)}"
            )

        for row in reader:
            try:
                theta = float(row["theta"])
                evac = float(row["E_vac"])
                omega_lambda = float(row["omega_lambda"])
                age_gyr = float(row["age_Gyr"])
                frw_viable = bool(int(row["frw_viable"]))
            except Exception as e:  # pragma: no cover - defensive
                raise RuntimeError(
                    f"[F1_FRW_LCDM] Failed to parse row {row!r}: {e}"
                ) from e

            rows.append(
                {
                    "theta": theta,
                    "E_vac": evac,
                    "omega_lambda": omega_lambda,
                    "age_Gyr": age_gyr,
                    "frw_viable": frw_viable,
                    # keep the raw flags for potential future use
                    "has_matter_era": bool(int(row["has_matter_era"])),
                    "has_late_accel": bool(int(row["has_late_accel"])),
                    "smooth_H2": bool(int(row["smooth_H2"])),
                }
            )

    return rows


def main() -> None:
    repo_root = get_repo_root()
    tables_dir = ensure_phase4_outputs_dir("tables")

    mask_path = tables_dir / "phase4_F1_frw_viability_mask.csv"
    diag_path = tables_dir / "phase4_F1_frw_lcdm_probe.json"
    lcdm_mask_path = tables_dir / "phase4_F1_frw_lcdm_probe_mask.csv"

    print("[F1_FRW_LCDM] Using viability mask:", mask_path)

    rows = load_viability_mask(mask_path)

    thetas = np.array([r["theta"] for r in rows], dtype=float)
    evac = np.array([r["E_vac"] for r in rows], dtype=float)
    omega_lambda = np.array([r["omega_lambda"] for r in rows], dtype=float)
    age_gyr = np.array([r["age_Gyr"] for r in rows], dtype=float)
    frw_viable = np.array([r["frw_viable"] for r in rows], dtype=bool)

    n_grid = int(thetas.size)
    n_frw_viable = int(frw_viable.sum())

    # Define a simple ΛCDM-like window:
    # - already FRW-viable;
    # - Ω_Λ within OMEGA_L_TARGET ± OMEGA_L_TOL;
    # - age within AGE_TARGET_GYR ± AGE_TOL_GYR.
    cond_omega = np.abs(omega_lambda - OMEGA_L_TARGET) <= OMEGA_L_TOL
    cond_age = np.abs(age_gyr - AGE_TARGET_GYR) <= AGE_TOL_GYR

    lcdm_like = frw_viable & cond_omega & cond_age
    n_lcdm_like = int(lcdm_like.sum())
    frac_lcdm_like = float(n_lcdm_like) / float(n_grid) if n_grid > 0 else 0.0

    diagnostics: Dict[str, Any] = {
        "mapping_family": "F1",
        "source_mask": str(mask_path),
        "omega_m": float(OMEGA_M),
        "omega_r": float(OMEGA_R),
        "H0_km_s_Mpc": float(H0_KM_S_MPC),
        "omega_lambda_target": float(OMEGA_L_TARGET),
        "omega_lambda_tolerance": float(OMEGA_L_TOL),
        "age_target_Gyr": float(AGE_TARGET_GYR),
        "age_tolerance_Gyr": float(AGE_TOL_GYR),
        "n_grid": int(n_grid),
        "n_frw_viable": int(n_frw_viable),
        "n_lcdm_like": int(n_lcdm_like),
        "lcdm_like_fraction": float(frac_lcdm_like),
    }

    if n_lcdm_like > 0:
        theta_l = thetas[lcdm_like]
        omega_l = omega_lambda[lcdm_like]
        age_l = age_gyr[lcdm_like]

        diagnostics.update(
            {
                "theta_min_lcdm": float(theta_l.min()),
                "theta_max_lcdm": float(theta_l.max()),
                "omega_lambda_min_lcdm": float(omega_l.min()),
                "omega_lambda_max_lcdm": float(omega_l.max()),
                "age_Gyr_min_lcdm": float(age_l.min()),
                "age_Gyr_max_lcdm": float(age_l.max()),
            }
        )

    # Write JSON diagnostics
    with diag_path.open("w", encoding="utf-8") as f:
        json.dump(diagnostics, f, indent=2, sort_keys=True)

    # Write per-grid mask CSV
    with lcdm_mask_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "theta",
                "E_vac",
                "omega_lambda",
                "age_Gyr",
                "frw_viable",
                "lcdm_like",
            ]
        )
        for r, is_lcdm in zip(rows, lcdm_like):
            writer.writerow(
                [
                    float(r["theta"]),
                    float(r["E_vac"]),
                    float(r["omega_lambda"]),
                    float(r["age_Gyr"]),
                    int(bool(r["frw_viable"])),
                    int(bool(is_lcdm)),
                ]
            )

    print("[F1_FRW_LCDM] Wrote diagnostics to", diag_path)
    print("[F1_FRW_LCDM] Wrote ΛCDM-like mask to", lcdm_mask_path)
    print("[F1_FRW_LCDM] Summary:")
    for k, v in diagnostics.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
