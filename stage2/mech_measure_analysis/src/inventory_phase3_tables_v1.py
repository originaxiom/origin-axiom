#!/usr/bin/env python3
"""
Stage 2: Mechanism / measure axis
Rung 1: Inventory of Phase 3 tables

This script:

- Locates the repo root from its own path.
- Lists all files in phase3/outputs/tables/.
- For each CSV or JSON file, records:
  - file name, relative path, suffix
  - file size (bytes)
  - for CSV: n_rows, n_cols, a sample of column names
  - for JSON: top-level type and a sample of keys (if dict)

Outputs:
  stage2/mech_measure_analysis/outputs/tables/
    stage2_mech_rung1_phase3_table_inventory_v1.csv
"""

from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Optional

import pandas as pd

TAG = "[stage2_mech_rung1]"


@dataclass
class TableInfo:
    file_name: str
    rel_path: str
    suffix: str
    size_bytes: int
    kind: str  # "csv" / "json" / "other"
    n_rows: Optional[int]
    n_cols: Optional[int]
    schema_hint: str


def find_repo_root(this_file: Path) -> Path:
    # This file lives at: repo_root/stage2/mech_measure_analysis/src/...
    return this_file.resolve().parents[3]


def analyze_csv(path: Path) -> tuple[int, int, str]:
    try:
        df = pd.read_csv(path)
        n_rows, n_cols = df.shape
        cols = list(df.columns)
        if len(cols) > 8:
            hint = ", ".join(cols[:8]) + ", ..."
        else:
            hint = ", ".join(cols)
        return n_rows, n_cols, f"columns: {hint}"
    except Exception as e:  # noqa: BLE001
        return -1, -1, f"error reading CSV: {type(e).__name__}: {e}"


def analyze_json(path: Path) -> tuple[Optional[int], Optional[int], str]:
    try:
        with path.open("r", encoding="utf-8") as f:
            obj = json.load(f)
    except Exception as e:  # noqa: BLE001
        return None, None, f"error reading JSON: {type(e).__name__}: {e}"

    if isinstance(obj, dict):
        keys = list(obj.keys())
        if len(keys) > 10:
            hint = ", ".join(sorted(keys)[:10]) + ", ..."
        else:
            hint = ", ".join(sorted(keys))
        return None, None, f"top-level dict keys: {hint}"
    elif isinstance(obj, list):
        # try to inspect first element
        if not obj:
            return None, None, "top-level list (empty)"
        first = obj[0]
        if isinstance(first, dict):
            keys = list(first.keys())
            if len(keys) > 10:
                hint = ", ".join(sorted(keys)[:10]) + ", ..."
            else:
                hint = ", ".join(sorted(keys))
            return None, None, f"top-level list of dicts; first keys: {hint}"
        else:
            return None, None, f"top-level list; first element type: {type(first).__name__}"
    else:
        return None, None, f"top-level type: {type(obj).__name__}"


def main() -> None:
    this_file = Path(__file__)
    repo_root = find_repo_root(this_file)
    print(f"{TAG} Repo root: {repo_root}")

    tables_dir = repo_root / "phase3" / "outputs" / "tables"
    if not tables_dir.is_dir():
        raise SystemExit(f"{TAG} ERROR: {tables_dir} does not exist or is not a directory")

    print(f"{TAG} Scanning {tables_dir} ...")

    rows: list[TableInfo] = []

    for path in sorted(tables_dir.iterdir()):
        if not path.is_file():
            continue

        rel_path = path.relative_to(repo_root).as_posix()
        suffix = path.suffix.lower()
        size_bytes = path.stat().st_size

        if suffix == ".csv":
            kind = "csv"
            n_rows, n_cols, schema_hint = analyze_csv(path)
        elif suffix == ".json":
            kind = "json"
            n_rows, n_cols, schema_hint = analyze_json(path)
        else:
            kind = "other"
            n_rows, n_cols, schema_hint = None, None, "not inspected (non-csv/json)"

        info = TableInfo(
            file_name=path.name,
            rel_path=rel_path,
            suffix=suffix,
            size_bytes=size_bytes,
            kind=kind,
            n_rows=n_rows,
            n_cols=n_cols,
            schema_hint=schema_hint,
        )
        rows.append(info)

        print(
            f"{TAG} {rel_path} | kind={kind} | size={size_bytes} | "
            f"n_rows={n_rows} | n_cols={n_cols}"
        )

    out_dir = (
        repo_root
        / "stage2"
        / "mech_measure_analysis"
        / "outputs"
        / "tables"
    )
    out_dir.mkdir(parents=True, exist_ok=True)

    out_csv = out_dir / "stage2_mech_rung1_phase3_table_inventory_v1.csv"
    df_out = pd.DataFrame([asdict(r) for r in rows])
    df_out.to_csv(out_csv, index=False)

    print(
        f"{TAG} Wrote inventory: {out_csv} ({out_csv.stat().st_size} bytes)"
    )


if __name__ == "__main__":
    main()
