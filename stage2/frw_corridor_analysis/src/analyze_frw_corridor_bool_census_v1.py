#!/usr/bin/env python
"""
Stage 2 — FRW corridor analysis, Rung 2 (boolean census).

Goal:
    For each Phase 4 FRW mask table, detect boolean-like columns and compute
    true/false counts and fractions. This is a preparatory rung to understand
    how strongly populated different FRW conditions are (viability, LCDM-like,
    corridor membership, etc.).

Scope:
    - READ-ONLY with respect to Phase folders.
    - Only writes under stage2/frw_corridor_analysis/outputs/tables/.

Inputs (relative to repo root, expected from Phase 4 gate / Stage 1):
    - phase4/outputs/tables/phase4_F1_frw_viability_mask.csv
    - phase4/outputs/tables/phase4_F1_frw_lcdm_probe_mask.csv
    - phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv
    - phase4/outputs/tables/phase4_F1_frw_data_probe_mask.csv

Outputs:
    - stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung2_bool_census_v1.csv
"""

from __future__ import annotations

import csv
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pandas as pd


@dataclass
class BoolColSummary:
    section: str
    source_key: str
    relpath: str
    col_name: str
    dtype: str
    n_rows: int
    n_true: int
    n_false: int
    n_na: int
    frac_true: Optional[float]
    frac_false: Optional[float]
    notes: str


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
            return start
        current = current.parent


def is_bool_like_series(series: pd.Series) -> bool:
    """
    Heuristic: consider a column boolean-like if, after dropping NA and
    mapping string/int/bool representations, its unique set is a subset
    of {0, 1, True, False}.
    """
    s = series.dropna()

    if s.empty:
        return False

    # Normalize values
    def normalize(x):
        if isinstance(x, bool):
            return x
        if isinstance(x, (int, float)):
            if x in (0, 1):
                return int(x)
        if isinstance(x, str):
            t = x.strip().lower()
            if t in ("true", "t", "yes", "y", "1"):
                return True
            if t in ("false", "f", "no", "n", "0"):
                return False
        return "__OTHER__"

    normalized = s.map(normalize)
    unique_vals = set(normalized.unique())

    allowed = {0, 1, True, False}
    # If we see any "__OTHER__", it's not a clean boolean-like column
    if "__OTHER__" in unique_vals:
        return False

    return unique_vals.issubset(allowed)


def summarize_bool_columns(
    df: pd.DataFrame,
    relpath: str,
    section: str,
    source_key: str,
) -> List[BoolColSummary]:
    n_rows = len(df)
    rows: List[BoolColSummary] = []

    for col in df.columns:
        if not is_bool_like_series(df[col]):
            continue

        s = df[col]
        # Normalize again for counts
        def to_bool(x) -> Optional[bool]:
            if isinstance(x, bool):
                return x
            if isinstance(x, (int, float)):
                if x == 1:
                    return True
                if x == 0:
                    return False
            if isinstance(x, str):
                t = x.strip().lower()
                if t in ("true", "t", "yes", "y", "1"):
                    return True
                if t in ("false", "f", "no", "n", "0"):
                    return False
            return None

        mapped = s.map(to_bool)
        n_na = mapped.isna().sum()
        n_true = int((mapped == True).sum())   # noqa: E712
        n_false = int((mapped == False).sum()) # noqa: E712

        denom = n_true + n_false
        frac_true = float(n_true) / denom if denom > 0 else None
        frac_false = float(n_false) / denom if denom > 0 else None

        notes_parts: List[str] = []
        col_lower = col.lower()
        if "viab" in col_lower:
            notes_parts.append("viability-related")
        if "lcdm" in col_lower:
            notes_parts.append("LCDM-like related")
        if "corridor" in col_lower or "corr" in col_lower:
            notes_parts.append("corridor-related")
        if "shape" in col_lower:
            notes_parts.append("shape-related")
        if "data" in col_lower:
            notes_parts.append("data-probe-related")

        notes = ", ".join(notes_parts)

        rows.append(
            BoolColSummary(
                section=section,
                source_key=source_key,
                relpath=relpath,
                col_name=col,
                dtype=str(df[col].dtype),
                n_rows=n_rows,
                n_true=n_true,
                n_false=n_false,
                n_na=int(n_na),
                frac_true=frac_true,
                frac_false=frac_false,
                notes=notes,
            )
        )

    return rows


def main() -> None:
    repo_root = find_repo_root()
    print(f"[stage2_frw_corridor_rung2] Repo root: {repo_root}")

    sources: Dict[str, Dict[str, str]] = {
        "phase4_frw_masks": {
            "frw_viability_mask": "phase4/outputs/tables/phase4_F1_frw_viability_mask.csv",
            "frw_lcdm_probe_mask": "phase4/outputs/tables/phase4_F1_frw_lcdm_probe_mask.csv",
            "frw_shape_probe_mask": "phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv",
            "frw_data_probe_mask": "phase4/outputs/tables/phase4_F1_frw_data_probe_mask.csv",
        },
    }

    out_dir = repo_root / "stage2" / "frw_corridor_analysis" / "outputs" / "tables"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_csv = out_dir / "stage2_frw_corridor_rung2_bool_census_v1.csv"

    all_rows: List[BoolColSummary] = []

    for section, items in sources.items():
        print(f"[stage2_frw_corridor_rung2] Section: {section}")
        for key, rel in items.items():
            path = repo_root / rel
            relpath = path.as_posix()
            if not path.exists():
                print(f"  - {key}: MISSING ({relpath})")
                continue

            print(f"  - {key}: reading {relpath}")
            try:
                df = pd.read_csv(path)
            except Exception as e:
                print(f"    ERROR reading {relpath}: {type(e).__name__}: {e}")
                continue

            bool_rows = summarize_bool_columns(df, relpath=relpath, section=section, source_key=key)
            if not bool_rows:
                print(f"    No boolean-like columns detected.")
            else:
                print(f"    Detected {len(bool_rows)} boolean-like columns:")
                for br in bool_rows:
                    print(
                        f"      * {br.col_name}: "
                        f"n_true={br.n_true}, n_false={br.n_false}, n_na={br.n_na}"
                    )
            all_rows.extend(bool_rows)

    if not all_rows:
        print("[stage2_frw_corridor_rung2] WARNING: no boolean-like columns found; nothing to write.")
        return

    fieldnames = [
        "section",
        "source_key",
        "relpath",
        "col_name",
        "dtype",
        "n_rows",
        "n_true",
        "n_false",
        "n_na",
        "frac_true",
        "frac_false",
        "notes",
    ]

    with out_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in all_rows:
            d = asdict(r)
            writer.writerow(d)

    print(
        f"[stage2_frw_corridor_rung2] Wrote {out_csv} "
        f"({out_csv.stat().st_size} bytes)"
    )
    ts = datetime.now(timezone.utc).isoformat()
    print(f"[stage2_frw_corridor_rung2] Timestamp UTC: {ts}")


if __name__ == "__main__":
    main()
