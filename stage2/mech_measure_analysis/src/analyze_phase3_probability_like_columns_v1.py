#!/usr/bin/env python3
"""
Stage 2: Mechanism / measure axis
Rung 3: Identify probability-like / flag-like columns in Phase 3 tables.

Inputs:
  - stage2/mech_measure_analysis/outputs/tables/
      stage2_mech_rung2_phase3_column_stats_v1.csv

For each numeric CSV column recorded there, we classify:

  - is_01_bounded:   v_min >= -eps and v_max <= 1 + eps
  - approx_binary:   is_01_bounded and (v_min >= -eps) and (v_max <= 1 + eps)
                     and (v_min <= 0.1) and (v_max >= 0.9)
                     (i.e. column actually uses both ends of [0,1])
  - approx_probability_like:
                     is_01_bounded and not approx_binary
                     (i.e. lives in [0,1], but not obviously a hard flag)

Outputs:
  - stage2/mech_measure_analysis/outputs/tables/
      stage2_mech_rung3_phase3_probability_like_candidates_v1.csv
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd

TAG = "[stage2_mech_rung3]"


@dataclass
class ProbLikeRow:
    file_name: str
    rel_path: str
    column_name: str
    dtype: str
    v_min: Optional[float]
    v_max: Optional[float]
    v_mean: Optional[float]
    v_std: Optional[float]
    is_01_bounded: bool
    approx_binary: bool
    approx_probability_like: bool
    note: str


def find_repo_root(this_file: Path) -> Path:
    # this_file = stage2/mech_measure_analysis/src/analyze_phase3_probability_like_columns_v1.py
    #   src        ^1  ^2                      ^3
    return this_file.resolve().parents[3]


def main() -> None:
    this_file = Path(__file__)
    repo_root = find_repo_root(this_file)
    print(f"{TAG} Repo root: {repo_root}")

    stats_csv = (
        repo_root
        / "stage2"
        / "mech_measure_analysis"
        / "outputs"
        / "tables"
        / "stage2_mech_rung2_phase3_column_stats_v1.csv"
    )
    if not stats_csv.is_file():
        raise SystemExit(f"{TAG} ERROR: stats CSV not found: {stats_csv}")

    df = pd.read_csv(stats_csv)
    print(f"{TAG} Loaded stats table with {len(df)} rows")

    rows: list[ProbLikeRow] = []

    eps = 1e-9

    for _, r in df.iterrows():
        kind = str(r.get("kind", ""))
        if kind != "csv":
            continue

        dtype = str(r.get("dtype", ""))
        # Heuristic: only consider numeric dtypes
        if not any(k in dtype for k in ("int", "float", "complex")):
            continue

        v_min = r.get("v_min")
        v_max = r.get("v_max")
        v_mean = r.get("v_mean")
        v_std = r.get("v_std")

        # Guard against NaNs
        if isinstance(v_min, float) and np.isnan(v_min):
            v_min = None
        if isinstance(v_max, float) and np.isnan(v_max):
            v_max = None

        is_01_bounded = False
        approx_binary = False
        approx_prob_like = False
        note_parts: list[str] = []

        if v_min is not None and v_max is not None:
            if v_min >= -eps and v_max <= 1.0 + eps:
                is_01_bounded = True
                note_parts.append("in_[0,1]_up_to_eps")

                # Binary-ish: uses both ends of [0,1] substantially
                if (v_min <= 0.1) and (v_max >= 0.9):
                    approx_binary = True
                    note_parts.append("approx_binary_flag")
                else:
                    approx_prob_like = True
                    note_parts.append("approx_probability_like")
            else:
                note_parts.append("outside_[0,1]")

        note = "; ".join(note_parts) if note_parts else ""

        rows.append(
            ProbLikeRow(
                file_name=str(r.get("file_name", "")),
                rel_path=str(r.get("rel_path", "")),
                column_name=str(r.get("column_name", "")),
                dtype=dtype,
                v_min=float(v_min) if v_min is not None else None,
                v_max=float(v_max) if v_max is not None else None,
                v_mean=float(v_mean) if not pd.isna(v_mean) else None,
                v_std=float(v_std) if not pd.isna(v_std) else None,
                is_01_bounded=is_01_bounded,
                approx_binary=approx_binary,
                approx_probability_like=approx_prob_like,
                note=note,
            )
        )

    out_dir = (
        repo_root
        / "stage2"
        / "mech_measure_analysis"
        / "outputs"
        / "tables"
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    out_csv = out_dir / "stage2_mech_rung3_phase3_probability_like_candidates_v1.csv"

    df_out = pd.DataFrame([asdict(r) for r in rows])
    df_out.to_csv(out_csv, index=False)

    print(
        f"{TAG} Wrote probability-like candidates: {out_csv} "
        f"({out_csv.stat().st_size} bytes)"
    )


if __name__ == "__main__":
    main()
