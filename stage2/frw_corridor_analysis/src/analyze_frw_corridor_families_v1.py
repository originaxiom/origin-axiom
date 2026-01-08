#!/usr/bin/env python
"""
Stage 2 — FRW corridor analysis, Rung 3 (family definitions).

Goal:
    Using the boolean census from Rung 2, define a small set of named
    FRW "families" (sets of theta points) and summarize their sizes and
    fractions of the total grid.

Scope:
    - Stage 2 only: does NOT modify Phase 0–5.
    - Reads the Rung 2 census CSV as its only input.
    - Produces a compact families table.

Inputs:
    - stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung2_bool_census_v1.csv

Outputs:
    - stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung3_families_v1.csv

Notes:
    This rung is descriptive only. It does NOT add new physics claims.
    Any promotion into Phase 5 (Option A) or a FRW-specific Phase 6 (Option B)
    will be decided in later rungs.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import math
import pandas as pd


@dataclass
class FamilySummary:
    family_id: str
    label: str
    section: str
    source_key: str
    col_name: str
    n_theta: int
    frac_of_grid: Optional[float]
    n_rows_source: int
    notes: str


def find_repo_root(start: Optional[Path] = None) -> Path:
    if start is None:
        start = Path(__file__).resolve().parent

    current = start
    while True:
        git_dir = current / ".git"
        stage2_dir = current / "stage2"
        if git_dir.is_dir() or stage2_dir.is_dir():
            return current
        if current.parent == current:
            return start
        current = current.parent


def load_bool_census(repo_root: Path) -> pd.DataFrame:
    path = (
        repo_root
        / "stage2"
        / "frw_corridor_analysis"
        / "outputs"
        / "tables"
        / "stage2_frw_corridor_rung2_bool_census_v1.csv"
    )
    if not path.exists():
        raise FileNotFoundError(
            f"Rung 2 census not found: {path}. "
            "Run analyze_frw_corridor_bool_census_v1.py first."
        )
    df = pd.read_csv(path)
    # basic sanity
    required_cols = {
        "section",
        "source_key",
        "col_name",
        "n_rows",
        "n_true",
        "n_false",
    }
    missing = required_cols - set(df.columns)
    if missing:
        raise ValueError(f"Census file missing columns: {sorted(missing)}")
    return df


def define_family_specs() -> List[Dict[str, str]]:
    """
    Logical family definitions in terms of (section, source_key, col_name).

    These are descriptive labels, not physics claims.
    """
    specs: List[Dict[str, str]] = []

    # 1) All FRW-viable points in the baseline mask
    specs.append(
        dict(
            family_id="F1_FRW_VIABLE",
            section="phase4_frw_masks",
            source_key="frw_viability_mask",
            col_name="frw_viable",
            label="FRW-viable points (Phase 4 viability mask)",
            notes="Baseline FRW viability slice (late acceleration + matter era + smooth H2).",
        )
    )

    # 2) LCDM-like subset of FRW-viable points
    specs.append(
        dict(
            family_id="F2_LCDM_LIKE",
            section="phase4_frw_masks",
            source_key="frw_lcdm_probe_mask",
            col_name="lcdm_like",
            label="LCDM-like FRW points (Phase 4 LCDM probe)",
            notes="Points flagged as LCDM-like in the Phase 4 LCDM probe mask.",
        )
    )

    # 3) Points inside the toy corridor band
    specs.append(
        dict(
            family_id="F3_TOY_CORRIDOR",
            section="phase4_frw_masks",
            source_key="frw_shape_probe_mask",
            col_name="in_toy_corridor",
            label="Toy-corridor band (Phase 4 shape probe)",
            notes="Theta points that fall inside the Phase 4 toy corridor band.",
        )
    )

    # 4) Corridor ∩ FRW-viable (Phase 4 combined flag)
    specs.append(
        dict(
            family_id="F4_CORRIDOR_AND_VIABLE",
            section="phase4_frw_masks",
            source_key="frw_shape_probe_mask",
            col_name="shape_and_viable",
            label="Corridor ∩ FRW-viable (Phase 4 shape probe)",
            notes="Intersection of toy corridor band with FRW-viable flag.",
        )
    )

    # 5) Corridor ∩ LCDM-like (Phase 4 combined flag)
    specs.append(
        dict(
            family_id="F5_CORRIDOR_AND_LCDM",
            section="phase4_frw_masks",
            source_key="frw_shape_probe_mask",
            col_name="shape_and_lcdm",
            label="Corridor ∩ LCDM-like (Phase 4 shape probe)",
            notes="Intersection of toy corridor band with LCDM-like flag.",
        )
    )

    # 6) Data-ok slice (currently empty but explicit)
    specs.append(
        dict(
            family_id="F6_DATA_OK",
            section="phase4_frw_masks",
            source_key="frw_data_probe_mask",
            col_name="data_ok",
            label="Data-compatible slice (Phase 4 data probe)",
            notes="Points passing the external data filter; currently empty since no data are attached.",
        )
    )

    return specs


def main() -> None:
    repo_root = find_repo_root()
    print(f"[stage2_frw_corridor_rung3] Repo root: {repo_root}")

    df = load_bool_census(repo_root)
    specs = define_family_specs()

    total_grid: Optional[int] = None
    if not df.empty:
        # use the first n_rows as a proxy for grid size (should be 2048)
        total_grid = int(df["n_rows"].iloc[0])
        print(f"[stage2_frw_corridor_rung3] Detected nominal grid size: {total_grid}")

    summaries: List[FamilySummary] = []

    # lookup key for fast access
    # (section, source_key, col_name) -> row
    key_cols = ["section", "source_key", "col_name"]
    df_keyed = df.set_index(key_cols)

    for spec in specs:
        key = (
            spec["section"],
            spec["source_key"],
            spec["col_name"],
        )
        family_id = spec["family_id"]
        label = spec["label"]
        notes = spec["notes"]

        if key not in df_keyed.index:
            print(f"[stage2_frw_corridor_rung3] WARNING: census row not found for {family_id}: {key}")
            continue

        row = df_keyed.loc[key]
        n_rows = int(row["n_rows"])
        n_true = int(row["n_true"])
        frac = None
        if total_grid is not None and total_grid > 0:
            frac = float(n_true) / float(total_grid)

        summaries.append(
            FamilySummary(
                family_id=family_id,
                label=label,
                section=spec["section"],
                source_key=spec["source_key"],
                col_name=spec["col_name"],
                n_theta=n_true,
                frac_of_grid=frac,
                n_rows_source=n_rows,
                notes=notes,
            )
        )

        print(
            f"[stage2_frw_corridor_rung3] {family_id}: n_theta={n_true}, "
            f"frac_of_grid={frac:.5f}" if (frac is not None) else
            f"[stage2_frw_corridor_rung3] {family_id}: n_theta={n_true}, frac_of_grid=UNKNOWN"
        )

    if not summaries:
        print("[stage2_frw_corridor_rung3] No families summarized; nothing to write.")
        return

    out_dir = (
        repo_root
        / "stage2"
        / "frw_corridor_analysis"
        / "outputs"
        / "tables"
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    out_csv = out_dir / "stage2_frw_corridor_rung3_families_v1.csv"

    fieldnames = [
        "family_id",
        "label",
        "section",
        "source_key",
        "col_name",
        "n_theta",
        "frac_of_grid",
        "n_rows_source",
        "notes",
    ]

    with out_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for s in summaries:
            writer.writerow(asdict(s))

    print(
        f"[stage2_frw_corridor_rung3] Wrote {out_csv} "
        f"({out_csv.stat().st_size} bytes)"
    )
    ts = datetime.now(timezone.utc).isoformat()
    print(f"[stage2_frw_corridor_rung3] Timestamp UTC: {ts}")


if __name__ == "__main__":
    main()
