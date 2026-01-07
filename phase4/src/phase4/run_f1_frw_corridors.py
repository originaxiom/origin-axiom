#!/usr/bin/env python3
"""
Phase 4: post-process F1 FRW viability mask into contiguous theta-corridors.

- Input:
    phase4/outputs/tables/phase4_F1_frw_viability_mask.csv

  This is assumed to have at least:
    - "theta" (float, radians)
    - a viability column, either "viable" or "frw_viable" (0/1)

  It may also contain additional columns (e.g. "omega_lambda", "age_Gyr",
  "has_matter_era", "has_late_accel", "smooth_H2", etc.), which we leave
  untouched.

- Outputs:
    phase4/outputs/tables/phase4_F1_frw_corridors.json
    phase4/outputs/tables/phase4_F1_frw_corridors.csv

  A "corridor" is defined here as a contiguous run of grid points with
  viable == 1 on the theta grid used in the F1 sanity curve / FRW modules.

This is a diagnostic helper only; the resulting corridors are explicitly
non-binding and are NOT promoted to a canonical theta-filter.
"""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, List, Optional, Sequence


@dataclass
class Corridor:
    theta_min: float
    theta_max: float
    n_points: int
    omega_lambda_mean: Optional[float] = None


def _repo_root() -> Path:
    # .../phase4/src/phase4/run_f1_frw_corridors.py -> repo root is parents[3]
    return Path(__file__).resolve().parents[3]


def _paths() -> Dict[str, Path]:
    root = _repo_root()
    tables = root / "phase4" / "outputs" / "tables"
    return {
        "mask": tables / "phase4_F1_frw_viability_mask.csv",
        "corridors_json": tables / "phase4_F1_frw_corridors.json",
        "corridors_csv": tables / "phase4_F1_frw_corridors.csv",
    }


def load_mask(mask_path: Path) -> List[Dict[str, object]]:
    """
    Load the FRW viability mask CSV.

    Accepts either:
      - "viable" column, or
      - "frw_viable" column

    and normalises to a Boolean row["viable"] field.
    """
    rows: List[Dict[str, object]] = []
    with mask_path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise RuntimeError("[F1_FRW_CORRIDORS] Mask CSV has no header")

        fieldnames = list(reader.fieldnames)
        has_omega = "omega_lambda" in fieldnames

        # Choose which column carries the viability flag
        if "viable" in fieldnames:
            viability_field = "viable"
        elif "frw_viable" in fieldnames:
            viability_field = "frw_viable"
        else:
            raise RuntimeError(
                "[F1_FRW_CORRIDORS] Expected a 'viable' or 'frw_viable' "
                f"column in {mask_path}, found {fieldnames}"
            )

        for row in reader:
            # Always parse theta
            row["theta"] = float(row["theta"])  # type: ignore[index]

            # Optional omega_lambda
            if has_omega and row.get("omega_lambda", "") != "":
                row["omega_lambda"] = float(row["omega_lambda"])  # type: ignore[index]

            # Normalise viability flag to row["viable"] as bool
            raw_flag = row.get(viability_field, "0")
            row["viable"] = bool(int(raw_flag))  # type: ignore[index]

            rows.append(row)

    rows.sort(key=lambda r: float(r["theta"]))  # type: ignore[index]
    return rows


def estimate_max_gap(thetas: Sequence[float]) -> float:
    if len(thetas) < 2:
        return 0.0
    diffs = [
        t2 - t1
        for t1, t2 in zip(thetas[:-1], thetas[1:])
        if t2 > t1
    ]
    if not diffs:
        return 0.0
    dt_min = min(diffs)
    # Slight inflation to be robust to FP noise
    return 1.5 * dt_min


def extract_corridors(
    rows: Sequence[Dict[str, object]],
    max_gap: Optional[float] = None,
) -> List[Corridor]:
    if not rows:
        return []

    thetas = [float(r["theta"]) for r in rows]  # type: ignore[index]
    if max_gap is None:
        max_gap = estimate_max_gap(thetas)

    corridors: List[Corridor] = []
    current: Optional[Corridor] = None
    has_omega = "omega_lambda" in rows[0]

    for r in rows:
        th = float(r["theta"])  # type: ignore[index]
        viable = bool(r["viable"])  # type: ignore[index]
        omega = (
            float(r["omega_lambda"])
            if has_omega and r.get("omega_lambda", "") != ""
            else None
        )  # type: ignore[index]

        if not viable:
            if current is not None:
                corridors.append(current)
                current = None
            continue

        if current is None:
            current = Corridor(theta_min=th, theta_max=th, n_points=1)
            if omega is not None:
                current.omega_lambda_mean = omega
            continue

        gap = th - current.theta_max
        if gap <= max_gap:
            # Extend existing corridor
            current.theta_max = th
            current.n_points += 1
            if omega is not None:
                if current.omega_lambda_mean is None:
                    current.omega_lambda_mean = omega
                else:
                    # Online mean update
                    n = current.n_points
                    mu_old = current.omega_lambda_mean
                    current.omega_lambda_mean = mu_old + (omega - mu_old) / n
        else:
            corridors.append(current)
            current = Corridor(theta_min=th, theta_max=th, n_points=1)
            if omega is not None:
                current.omega_lambda_mean = omega

    if current is not None:
        corridors.append(current)

    return corridors


def main() -> None:
    paths = _paths()
    mask_path = paths["mask"]
    out_json = paths["corridors_json"]
    out_csv = paths["corridors_csv"]

    print("[F1_FRW_CORRIDORS] Using mask:", mask_path)

    if not mask_path.exists():
        raise SystemExit(
            f"[F1_FRW_CORRIDORS] Mask file does not exist: {mask_path}"
        )

    rows = load_mask(mask_path)
    if not rows:
        raise SystemExit("[F1_FRW_CORRIDORS] No rows in mask; nothing to do.")

    total_points = len(rows)
    viable_points = sum(1 for r in rows if bool(r["viable"]))  # type: ignore[index]
    viable_fraction = viable_points / total_points if total_points else 0.0

    corridors = extract_corridors(rows)
    n_corridors = len(corridors)

    principal_corridor = None
    if corridors:
        # Choose principal corridor as the one with the largest n_points
        principal_index = max(
            range(len(corridors)), key=lambda i: corridors[i].n_points
        )
        principal_corridor = asdict(corridors[principal_index])
        principal_corridor["index"] = principal_index

    meta = {
        "mapping_family": "F1",
        "source_mask": str(mask_path),
        "n_grid": total_points,
        "n_viable": viable_points,
        "viable_fraction": viable_fraction,
        "n_corridors": n_corridors,
        "principal_corridor": principal_corridor,
    }

    diagnostics = {
        "meta": meta,
        "corridors": [asdict(c) for c in corridors],
    }

    out_json.parent.mkdir(parents=True, exist_ok=True)
    with out_json.open("w", encoding="utf-8") as f:
        json.dump(diagnostics, f, indent=2, sort_keys=True)

    with out_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["index", "theta_min", "theta_max", "n_points", "omega_lambda_mean"])
        for i, c in enumerate(corridors):
            writer.writerow([
                i,
                c.theta_min,
                c.theta_max,
                c.n_points,
                "" if c.omega_lambda_mean is None else c.omega_lambda_mean,
            ])

    print("[F1_FRW_CORRIDORS] Wrote diagnostics JSON to", out_json)
    print("[F1_FRW_CORRIDORS] Wrote corridors CSV to", out_csv)
    print("[F1_FRW_CORRIDORS] Meta:")
    for k, v in meta.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
