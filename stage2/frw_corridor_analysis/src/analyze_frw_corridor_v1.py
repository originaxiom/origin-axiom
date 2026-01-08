#!/usr/bin/env python
"""
Stage 2 — FRW corridor analysis, Rung 1 (sanity + schema introspection).

Goal:
    Read key Phase 4 FRW tables (viability & probe masks, corridors summary),
    check their existence, basic shape, and column schema, and write a small
    Stage 2 sanity table that we can build subsequent rungs on.

This script is READ-ONLY with respect to Phase folders. It only writes under:
    stage2/frw_corridor_analysis/outputs/

Inputs (relative to repo root, expected to exist from Phase 4 gate):
    - phase4/outputs/tables/phase4_F1_frw_viability_mask.csv
    - phase4/outputs/tables/phase4_F1_frw_lcdm_probe_mask.csv
    - phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv
    - phase4/outputs/tables/phase4_F1_frw_data_probe_mask.csv
    - phase4/outputs/tables/phase4_F1_frw_corridors.json

Outputs:
    - stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung1_sources_v1.csv
"""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional

import pandas as pd


@dataclass
class SourceSummary:
    section: str
    key: str
    relpath: str
    exists: bool
    size_bytes: Optional[int]
    n_rows: Optional[int]
    n_cols: Optional[int]
    columns: str
    ext_status: str
    ext_extra: str


def find_repo_root(start: Optional[Path] = None) -> Path:
    """
    Walk upwards until we find a directory that looks like the repo root,
    identified by the presence of `.git` or `phase4/` folder.
    """
    if start is None:
        start = Path(__file__).resolve().parent

    current = start
    while True:
        git_dir = current / ".git"
        phase4_dir = current / "phase4"
        if git_dir.is_dir() or phase4_dir.is_dir():
            return current
        if current.parent == current:
            # Fallback: just return where we started if nothing better is found
            return start
        current = current.parent


def summarize_csv(path: Path, section: str, key: str) -> SourceSummary:
    relpath = path.as_posix()
    if not path.exists():
        return SourceSummary(
            section=section,
            key=key,
            relpath=relpath,
            exists=False,
            size_bytes=None,
            n_rows=None,
            n_cols=None,
            columns="",
            ext_status="MISSING",
            ext_extra="file does not exist",
        )

    size_bytes = path.stat().st_size

    try:
        df = pd.read_csv(path)
        n_rows, n_cols = df.shape
        cols = list(df.columns)
        columns_str = ", ".join(cols)

        # Try to detect some semantic columns we care about
        bool_like = [c for c in cols if c.lower().startswith("has_")
                     or c.lower().endswith("_ok")
                     or c.lower().endswith("_viable")
                     or c.lower().endswith("_like")]
        notes = []
        if bool_like:
            notes.append(f"bool-like columns: {', '.join(bool_like)}")
        if "theta" in df.columns:
            notes.append("has theta column")
        if "E_vac" in df.columns or "E[vac]" in df.columns:
            notes.append("has E_vac-like column")
        ext_extra = "; ".join(notes) if notes else ""

        return SourceSummary(
            section=section,
            key=key,
            relpath=relpath,
            exists=True,
            size_bytes=size_bytes,
            n_rows=int(n_rows),
            n_cols=int(n_cols),
            columns=columns_str,
            ext_status="OK",
            ext_extra=ext_extra,
        )
    except Exception as e:
        return SourceSummary(
            section=section,
            key=key,
            relpath=relpath,
            exists=True,
            size_bytes=size_bytes,
            n_rows=None,
            n_cols=None,
            columns="",
            ext_status="ERROR_READ",
            ext_extra=f"{type(e).__name__}: {e}",
        )


def summarize_json(path: Path, section: str, key: str) -> SourceSummary:
    relpath = path.as_posix()
    if not path.exists():
        return SourceSummary(
            section=section,
            key=key,
            relpath=relpath,
            exists=False,
            size_bytes=None,
            n_rows=None,
            n_cols=None,
            columns="",
            ext_status="MISSING",
            ext_extra="file does not exist",
        )

    size_bytes = path.stat().st_size

    try:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        # We do not try to deeply interpret the JSON here; just basic shape
        if isinstance(data, dict):
            top_keys = ", ".join(sorted(data.keys()))
            extra = f"top-level keys: {top_keys}"
        else:
            extra = f"top-level type: {type(data).__name__}"

        return SourceSummary(
            section=section,
            key=key,
            relpath=relpath,
            exists=True,
            size_bytes=size_bytes,
            n_rows=None,
            n_cols=None,
            columns="",
            ext_status="OK",
            ext_extra=extra,
        )
    except Exception as e:
        return SourceSummary(
            section=section,
            key=key,
            relpath=relpath,
            exists=True,
            size_bytes=size_bytes,
            n_rows=None,
            n_cols=None,
            columns="",
            ext_status="ERROR_READ",
            ext_extra=f"{type(e).__name__}: {e}",
        )


def main() -> None:
    repo_root = find_repo_root()
    print(f"[stage2_frw_corridor_rung1] Repo root: {repo_root}")

    # Define the Phase 4 FRW sources we care about in this rung
    sources: Dict[str, Dict[str, str]] = {
        "phase4_frw_masks": {
            "frw_viability_mask": "phase4/outputs/tables/phase4_F1_frw_viability_mask.csv",
            "frw_lcdm_probe_mask": "phase4/outputs/tables/phase4_F1_frw_lcdm_probe_mask.csv",
            "frw_shape_probe_mask": "phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv",
            "frw_data_probe_mask": "phase4/outputs/tables/phase4_F1_frw_data_probe_mask.csv",
        },
        "phase4_frw_corridors": {
            "frw_corridors": "phase4/outputs/tables/phase4_F1_frw_corridors.json",
        },
    }

    out_dir = repo_root / "stage2" / "frw_corridor_analysis" / "outputs" / "tables"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_csv = out_dir / "stage2_frw_corridor_rung1_sources_v1.csv"

    rows: List[SourceSummary] = []

    for section, items in sources.items():
        print(f"[stage2_frw_corridor_rung1] Section: {section}")
        for key, rel in items.items():
            path = repo_root / rel
            if rel.endswith(".csv"):
                summary = summarize_csv(path, section=section, key=key)
            else:
                summary = summarize_json(path, section=section, key=key)

            rows.append(summary)

            status = "OK" if summary.exists and summary.ext_status == "OK" else summary.ext_status
            print(
                f"  - {key}: {status}, exists={summary.exists}, "
                f"size={summary.size_bytes}, n_rows={summary.n_rows}, "
                f"n_cols={summary.n_cols}"
            )

    # Write CSV summary
    fieldnames = [
        "section",
        "key",
        "relpath",
        "exists",
        "size_bytes",
        "n_rows",
        "n_cols",
        "columns",
        "ext_status",
        "ext_extra",
    ]

    with out_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in rows:
            d = asdict(r)
            # normalize bool -> int for CSV if desired; keep as bool for now
            writer.writerow(d)

    print(
        f"[stage2_frw_corridor_rung1] Wrote {out_csv} "
        f"({out_csv.stat().st_size} bytes)"
    )
    ts = datetime.now(timezone.utc).isoformat()
    print(f"[stage2_frw_corridor_rung1] Timestamp UTC: {ts}")


if __name__ == "__main__":
    main()
