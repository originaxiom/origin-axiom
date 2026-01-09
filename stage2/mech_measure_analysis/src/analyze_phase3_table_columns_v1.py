#!/usr/bin/env python3
"""
Stage 2: Mechanism / measure axis
Rung 2: Column-level stats for Phase 3 tables

For each file in phase3/outputs/tables:

- If CSV:
    * compute per-column stats for numeric columns:
      - n_non_null, n_null
      - min, max, mean, std
- If JSON:
    * record top-level type and a short key summary.

Outputs:
  stage2/mech_measure_analysis/outputs/tables/
    stage2_mech_rung2_phase3_column_stats_v1.csv
"""

from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd

TAG = "[stage2_mech_rung2]"


@dataclass
class ColumnStat:
    file_name: str
    rel_path: str
    kind: str            # "csv" / "json"
    column_name: str     # for JSON: pseudo-column name
    dtype: str
    n_non_null: Optional[int]
    n_null: Optional[int]
    v_min: Optional[float]
    v_max: Optional[float]
    v_mean: Optional[float]
    v_std: Optional[float]
    note: str


def find_repo_root(this_file: Path) -> Path:
    return this_file.resolve().parents[3]


def analyze_csv(path: Path, rel_path: str) -> list[ColumnStat]:
    try:
        df = pd.read_csv(path)
    except Exception as e:  # noqa: BLE001
        return [
            ColumnStat(
                file_name=path.name,
                rel_path=rel_path,
                kind="csv",
                column_name="__FILE__",
                dtype="",
                n_non_null=None,
                n_null=None,
                v_min=None,
                v_max=None,
                v_mean=None,
                v_std=None,
                note=f"error reading CSV: {type(e).__name__}: {e}",
            )
        ]

    rows: list[ColumnStat] = []
    for col in df.columns:
        s = df[col]
        n_non_null = int(s.notna().sum())
        n_null = int(s.isna().sum())
        dtype = str(s.dtype)

        if np.issubdtype(s.dtype, np.number):
            v_min = float(s.min())
            v_max = float(s.max())
            v_mean = float(s.mean())
            v_std = float(s.std(ddof=1)) if n_non_null > 1 else 0.0
            note = "numeric"
        else:
            v_min = v_max = v_mean = v_std = None
            note = "non-numeric"

        rows.append(
            ColumnStat(
                file_name=path.name,
                rel_path=rel_path,
                kind="csv",
                column_name=str(col),
                dtype=dtype,
                n_non_null=n_non_null,
                n_null=n_null,
                v_min=v_min,
                v_max=v_max,
                v_mean=v_mean,
                v_std=v_std,
                note=note,
            )
        )

    return rows


def analyze_json(path: Path, rel_path: str) -> list[ColumnStat]:
    try:
        with path.open("r", encoding="utf-8") as f:
            obj = json.load(f)
    except Exception as e:  # noqa: BLE001
        return [
            ColumnStat(
                file_name=path.name,
                rel_path=rel_path,
                kind="json",
                column_name="__FILE__",
                dtype="",
                n_non_null=None,
                n_null=None,
                v_min=None,
                v_max=None,
                v_mean=None,
                v_std=None,
                note=f"error reading JSON: {type(e).__name__}: {e}",
            )
        ]

    if isinstance(obj, dict):
        keys = sorted(obj.keys())
        hint = ", ".join(keys[:10]) + (", ..." if len(keys) > 10 else "")
        note = f"top-level dict keys: {hint}"
    elif isinstance(obj, list):
        if not obj:
            note = "top-level list (empty)"
        else:
            first = obj[0]
            if isinstance(first, dict):
                keys = sorted(first.keys())
                hint = ", ".join(keys[:10]) + (", ..." if len(keys) > 10 else "")
                note = f"top-level list of dicts; first keys: {hint}"
            else:
                note = f"top-level list; first element type: {type(first).__name__}"
    else:
        note = f"top-level type: {type(obj).__name__}"

    return [
        ColumnStat(
            file_name=path.name,
            rel_path=rel_path,
            kind="json",
            column_name="__STRUCTURE__",
            dtype="",
            n_non_null=None,
            n_null=None,
            v_min=None,
            v_max=None,
            v_mean=None,
            v_std=None,
            note=note,
        )
    ]


def main() -> None:
    this_file = Path(__file__)
    repo_root = find_repo_root(this_file)
    print(f"{TAG} Repo root: {repo_root}")

    tables_dir = repo_root / "phase3" / "outputs" / "tables"
    if not tables_dir.is_dir():
        raise SystemExit(f"{TAG} ERROR: {tables_dir} is not a directory")

    rows: list[ColumnStat] = []

    for path in sorted(tables_dir.iterdir()):
        if not path.is_file():
            continue

        rel_path = path.relative_to(repo_root).as_posix()
        suffix = path.suffix.lower()

        if suffix == ".csv":
            print(f"{TAG} Analyzing CSV: {rel_path}")
            rows.extend(analyze_csv(path, rel_path))
        elif suffix == ".json":
            print(f"{TAG} Summarizing JSON: {rel_path}")
            rows.extend(analyze_json(path, rel_path))
        else:
            print(f"{TAG} Skipping non-csv/json: {rel_path}")
            continue

    out_dir = (
        repo_root
        / "stage2"
        / "mech_measure_analysis"
        / "outputs"
        / "tables"
    )
    out_dir.mkdir(parents=True, exist_ok=True)

    out_csv = out_dir / "stage2_mech_rung2_phase3_column_stats_v1.csv"
    df_out = pd.DataFrame([asdict(r) for r in rows])
    df_out.to_csv(out_csv, index=False)

    print(
        f"{TAG} Wrote column stats: {out_csv} "
        f"({out_csv.stat().st_size} bytes)"
    )


if __name__ == "__main__":
    main()
