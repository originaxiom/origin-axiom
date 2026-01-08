#!/usr/bin/env python3
"""
run_f1_frw_shape_probe.py

Tie together three Phase 4 diagnostic layers on F1:

  * F1 shape toy corridor mask:
      phase4/outputs/tables/phase4_F1_shape_mask.csv
      columns: theta, E_vac, in_toy_corridor

  * FRW viability mask:
      phase4/outputs/tables/phase4_F1_frw_viability_mask.csv
      columns: theta, E_vac, omega_lambda, age_Gyr,
               has_matter_era, has_late_accel, smooth_H2,
               frw_viable (0/1)

  * ΛCDM-like FRW probe mask:
      phase4/outputs/tables/phase4_F1_frw_lcdm_probe_mask.csv
      same as FRW viability, plus
               lcdm_like (0/1)

The script joins these on the θ-grid (by the 'theta' column treated
as a string key), constructs a unified per-θ mask, and computes
summary fractions and θ-ranges for:

  - in_toy_corridor
  - frw_viable
  - lcdm_like
  - in_toy_corridor ∧ frw_viable
  - in_toy_corridor ∧ lcdm_like

Outputs:

  * phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv
      columns:
        theta, E_vac, omega_lambda, age_Gyr,
        in_toy_corridor, frw_viable, lcdm_like,
        shape_and_viable, shape_and_lcdm

  * phase4/outputs/tables/phase4_F1_frw_shape_probe.json
      JSON diagnostics summary with fractions and θ-ranges.
"""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple


# ---------------------------------------------------------------------
# Path helpers
# ---------------------------------------------------------------------


HERE = Path(__file__).resolve()
# .../origin-axiom/phase4/src/phase4/run_f1_frw_shape_probe.py
PHASE4_ROOT = HERE.parents[2]  # .../origin-axiom/phase4
TABLES_DIR = PHASE4_ROOT / "outputs" / "tables"


SHAPE_MASK_CSV = TABLES_DIR / "phase4_F1_shape_mask.csv"
FRW_VIAB_MASK_CSV = TABLES_DIR / "phase4_F1_frw_viability_mask.csv"
LCDM_MASK_CSV = TABLES_DIR / "phase4_F1_frw_lcdm_probe_mask.csv"

OUT_MASK_CSV = TABLES_DIR / "phase4_F1_frw_shape_probe_mask.csv"
OUT_JSON = TABLES_DIR / "phase4_F1_frw_shape_probe.json"


# ---------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------


@dataclass
class JoinedRow:
    theta: float
    E_vac: float
    omega_lambda: float
    age_Gyr: float
    in_toy_corridor: bool
    frw_viable: bool
    lcdm_like: bool
    shape_and_viable: bool
    shape_and_lcdm: bool


# ---------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------


def require_file(path: Path, label: str) -> None:
    if not path.is_file():
        raise FileNotFoundError(
            f"[F1_FRW_SHAPE_PROBE] Missing {label}: {path}"
        )


def parse_bool_field(row: Dict[str, str], key: str) -> bool:
    """Interpret a CSV field as Boolean via int(field) != 0, default False."""
    val = row.get(key, "").strip()
    if val == "":
        return False
    try:
        return bool(int(val))
    except ValueError:
        return False


def parse_float_field(row: Dict[str, str], key: str) -> float:
    val = row.get(key, "").strip()
    if val == "":
        raise ValueError(f"Missing float field '{key}' in row: {row}")
    return float(val)


def theta_key(row: Dict[str, str]) -> str:
    """Use the raw 'theta' string as a join key (avoid float rounding issues)."""
    val = row.get("theta", "").strip()
    if val == "":
        raise ValueError(f"Missing 'theta' field in row: {row}")
    return val


# ---------------------------------------------------------------------
# Loaders
# ---------------------------------------------------------------------


def load_shape_mask(path: Path) -> Dict[str, Dict[str, str]]:
    require_file(path, "shape mask")
    out: Dict[str, Dict[str, str]] = {}
    with path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        expected_cols = {"theta", "E_vac", "in_toy_corridor"}
        missing = expected_cols - set(reader.fieldnames or [])
        if missing:
            raise RuntimeError(
                f"[F1_FRW_SHAPE_PROBE] Shape mask {path} is missing columns: {missing}"
            )
        for row in reader:
            key = theta_key(row)
            out[key] = row
    return out


def load_viability_mask(path: Path) -> Dict[str, Dict[str, str]]:
    require_file(path, "FRW viability mask")
    out: Dict[str, Dict[str, str]] = {}
    with path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        expected_cols = {
            "theta",
            "E_vac",
            "omega_lambda",
            "age_Gyr",
            "has_matter_era",
            "has_late_accel",
            "smooth_H2",
            "frw_viable",
        }
        missing = expected_cols - set(reader.fieldnames or [])
        if missing:
            raise RuntimeError(
                f"[F1_FRW_SHAPE_PROBE] FRW viability mask {path} is missing columns: {missing}"
            )
        for row in reader:
            key = theta_key(row)
            out[key] = row
    return out


def load_lcdm_mask(path: Path) -> Dict[str, Dict[str, str]]:
    require_file(path, "ΛCDM-like mask")
    out: Dict[str, Dict[str, str]] = {}
    with path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        expected_cols = {
            "theta",
            "E_vac",
            "omega_lambda",
            "age_Gyr",
            "frw_viable",
            "lcdm_like",
        }
        missing = expected_cols - set(reader.fieldnames or [])
        if missing:
            raise RuntimeError(
                f"[F1_FRW_SHAPE_PROBE] ΛCDM-like mask {path} is missing columns: {missing}"
            )
        for row in reader:
            key = theta_key(row)
            out[key] = row
    return out


# ---------------------------------------------------------------------
# Join & diagnostics
# ---------------------------------------------------------------------


def join_masks(
    shape_mask: Dict[str, Dict[str, str]],
    frw_mask: Dict[str, Dict[str, str]],
    lcdm_mask: Dict[str, Dict[str, str]],
) -> List[JoinedRow]:
    """
    Join the three masks by θ. We iterate over the FRW viability mask,
    assuming it defines the canonical θ-grid for Phase 4 FRW-facing diagnostics.
    """
    joined: List[JoinedRow] = []

    for theta_str, frw_row in sorted(frw_mask.items(), key=lambda kv: float(kv[0])):
        shape_row = shape_mask.get(theta_str)
        lcdm_row = lcdm_mask.get(theta_str)

        in_toy_corridor = False
        if shape_row is not None:
            in_toy_corridor = parse_bool_field(shape_row, "in_toy_corridor")

        frw_viable = parse_bool_field(frw_row, "frw_viable")

        lcdm_like = False
        if lcdm_row is not None:
            lcdm_like = parse_bool_field(lcdm_row, "lcdm_like")

        theta_val = float(theta_str)
        E_vac = parse_float_field(frw_row, "E_vac")
        omega_lambda = parse_float_field(frw_row, "omega_lambda")
        age_Gyr = parse_float_field(frw_row, "age_Gyr")

        shape_and_viable = in_toy_corridor and frw_viable
        shape_and_lcdm = in_toy_corridor and lcdm_like

        joined.append(
            JoinedRow(
                theta=theta_val,
                E_vac=E_vac,
                omega_lambda=omega_lambda,
                age_Gyr=age_Gyr,
                in_toy_corridor=in_toy_corridor,
                frw_viable=frw_viable,
                lcdm_like=lcdm_like,
                shape_and_viable=shape_and_viable,
                shape_and_lcdm=shape_and_lcdm,
            )
        )

    return joined


def frac(condition_flags: List[bool]) -> float:
    if not condition_flags:
        return 0.0
    return sum(1 for x in condition_flags if x) / float(len(condition_flags))


def theta_range(values: List[float], mask: List[bool]) -> Optional[Tuple[float, float]]:
    selected = [v for v, m in zip(values, mask) if m]
    if not selected:
        return None
    return min(selected), max(selected)


def compute_diagnostics(joined: List[JoinedRow]) -> Dict[str, object]:
    if not joined:
        return {
            "n_grid": 0,
            "frac_in_toy_corridor": 0.0,
            "frac_frw_viable": 0.0,
            "frac_lcdm_like": 0.0,
            "frac_shape_and_viable": 0.0,
            "frac_shape_and_lcdm": 0.0,
            "theta_range_in_toy_corridor": None,
            "theta_range_frw_viable": None,
            "theta_range_lcdm_like": None,
            "theta_range_shape_and_viable": None,
            "theta_range_shape_and_lcdm": None,
        }

    n_grid = len(joined)
    thetas = [r.theta for r in joined]

    in_toy_corridor_flags = [r.in_toy_corridor for r in joined]
    frw_viable_flags = [r.frw_viable for r in joined]
    lcdm_like_flags = [r.lcdm_like for r in joined]
    shape_and_viable_flags = [r.shape_and_viable for r in joined]
    shape_and_lcdm_flags = [r.shape_and_lcdm for r in joined]

    diagnostics: Dict[str, object] = {
        "n_grid": n_grid,
        "frac_in_toy_corridor": frac(in_toy_corridor_flags),
        "frac_frw_viable": frac(frw_viable_flags),
        "frac_lcdm_like": frac(lcdm_like_flags),
        "frac_shape_and_viable": frac(shape_and_viable_flags),
        "frac_shape_and_lcdm": frac(shape_and_lcdm_flags),
        "theta_range_in_toy_corridor": theta_range(thetas, in_toy_corridor_flags),
        "theta_range_frw_viable": theta_range(thetas, frw_viable_flags),
        "theta_range_lcdm_like": theta_range(thetas, lcdm_like_flags),
        "theta_range_shape_and_viable": theta_range(thetas, shape_and_viable_flags),
        "theta_range_shape_and_lcdm": theta_range(thetas, shape_and_lcdm_flags),
    }

    return diagnostics


# ---------------------------------------------------------------------
# I/O
# ---------------------------------------------------------------------


def write_mask_csv(path: Path, joined: List[JoinedRow]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "theta",
        "E_vac",
        "omega_lambda",
        "age_Gyr",
        "in_toy_corridor",
        "frw_viable",
        "lcdm_like",
        "shape_and_viable",
        "shape_and_lcdm",
    ]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in joined:
            writer.writerow(
                {
                    "theta": r.theta,
                    "E_vac": r.E_vac,
                    "omega_lambda": r.omega_lambda,
                    "age_Gyr": r.age_Gyr,
                    "in_toy_corridor": int(r.in_toy_corridor),
                    "frw_viable": int(r.frw_viable),
                    "lcdm_like": int(r.lcdm_like),
                    "shape_and_viable": int(r.shape_and_viable),
                    "shape_and_lcdm": int(r.shape_and_lcdm),
                }
            )


def write_diagnostics_json(path: Path, diagnostics: Dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(diagnostics, f, indent=2, sort_keys=True)


# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------


def main() -> None:
    print("[F1_FRW_SHAPE_PROBE] Phase 4 root:", PHASE4_ROOT)
    print("[F1_FRW_SHAPE_PROBE] Tables dir:", TABLES_DIR)

    shape_mask = load_shape_mask(SHAPE_MASK_CSV)
    frw_mask = load_viability_mask(FRW_VIAB_MASK_CSV)
    lcdm_mask = load_lcdm_mask(LCDM_MASK_CSV)

    joined = join_masks(shape_mask, frw_mask, lcdm_mask)
    diagnostics = compute_diagnostics(joined)

    write_mask_csv(OUT_MASK_CSV, joined)
    write_diagnostics_json(OUT_JSON, diagnostics)

    print("[F1_FRW_SHAPE_PROBE] Wrote joined mask CSV to", OUT_MASK_CSV)
    print("[F1_FRW_SHAPE_PROBE] Wrote diagnostics JSON to", OUT_JSON)
    print("[F1_FRW_SHAPE_PROBE] Summary:")
    for k, v in diagnostics.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
