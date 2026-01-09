#!/usr/bin/env python
from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List

import numpy as np
import pandas as pd

TAG = "[stage2_frw_data_probe_rung1]"


@dataclass
class ProbeColumnSummary:
    column: str
    dtype: str
    n_rows: int
    n_na: int
    n_true: int
    n_false: int
    frac_true: float
    frac_false: float
    note: str


def find_repo_root(start: Path | None = None) -> Path:
    here = (start or Path(__file__)).resolve()
    for p in [here] + list(here.parents):
        if (p / ".git").is_dir():
            return p
    raise RuntimeError(f"{TAG} Could not find repo root (.git not found)")


def is_bool_like(s: pd.Series) -> bool:
    """Heuristic: True if dtype is bool or values subset of {0,1} (ignoring NaN)."""
    if s.dtype == bool:
        return True
    vals = pd.unique(s.dropna())
    if len(vals) == 0:
        return False
    try:
        arr = np.asarray(vals, dtype=float)
    except Exception:
        return False
    return set(np.unique(arr)).issubset({0.0, 1.0})


def main() -> None:
    repo_root = find_repo_root()
    print(f"{TAG} Repo root: {repo_root}")

    data_path = (
        repo_root
        / "phase4"
        / "outputs"
        / "tables"
        / "phase4_F1_frw_data_probe_mask.csv"
    )
    if not data_path.is_file():
        raise FileNotFoundError(f"{TAG} Data probe mask not found at {data_path}")

    df = pd.read_csv(data_path)
    print(f"{TAG} Loaded {data_path} with shape {df.shape}")

    rows: List[ProbeColumnSummary] = []

    for col in df.columns:
        if col.lower().startswith("theta"):
            # skip theta / theta_index
            continue

        s = df[col]
        if not is_bool_like(s):
            # only interested in boolean-like probes here
            continue

        n_rows = len(s)
        n_na = int(s.isna().sum())

        # Treat non-zero as True for numeric, or cast for bool.
        if s.dtype == bool:
            mask_true = s.fillna(False)
        else:
            mask_true = (s != 0).fillna(False)

        n_true = int(mask_true.sum())
        n_false = n_rows - n_true - n_na

        frac_true = n_true / n_rows if n_rows > 0 else 0.0
        frac_false = n_false / n_rows if n_rows > 0 else 0.0

        note = ""
        if n_true == 0:
            note = "always_false"
        elif n_false == 0:
            note = "always_true"

        rows.append(
            ProbeColumnSummary(
                column=col,
                dtype=str(s.dtype),
                n_rows=n_rows,
                n_na=n_na,
                n_true=n_true,
                n_false=n_false,
                frac_true=frac_true,
                frac_false=frac_false,
                note=note,
            )
        )
        print(
            f"{TAG} {col}: n_true={n_true}, n_false={n_false}, "
            f"frac_true={frac_true:.5f}, frac_false={frac_false:.5f}, note={note}"
        )

    out_dir = (
        repo_root
        / "stage2"
        / "frw_data_probe_analysis"
        / "outputs"
        / "tables"
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    out_csv = out_dir / "stage2_frw_data_probe_rung1_column_stats_v1.csv"

    df_out = pd.DataFrame([asdict(r) for r in rows])
    df_out.to_csv(out_csv, index=False)

    print(
        f"{TAG} Wrote column stats: {out_csv} "
        f"({out_csv.stat().st_size} bytes; rows={len(df_out)})"
    )


if __name__ == "__main__":
    main()
