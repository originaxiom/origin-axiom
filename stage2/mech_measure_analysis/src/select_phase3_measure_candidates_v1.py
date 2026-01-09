#!/usr/bin/env python3
"""
Stage 2: Mechanism / measure axis
Rung 4: Select Phase 3 measure / flag candidates from Rung 3 output.

Inputs:
  - stage2/mech_measure_analysis/outputs/tables/
      stage2_mech_rung3_phase3_probability_like_candidates_v1.csv

Logic (per row = one CSV column):
  - If approx_binary:
        role = "flag_candidate"
  - Else if approx_probability_like:
        role = "measure_candidate"
  - Else:
        skip

Outputs:
  - stage2/mech_measure_analysis/outputs/tables/
      stage2_mech_rung4_phase3_measure_and_flag_candidates_v1.csv

This is still descriptive: it does not change Phase 3, it just labels
which columns look structurally like flags or measures in [0,1].
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Literal

import pandas as pd

TAG = "[stage2_mech_rung4]"


Role = Literal["measure_candidate", "flag_candidate"]


@dataclass
class CandidateRow:
    file_name: str
    rel_path: str
    column_name: str
    dtype: str
    role: Role
    v_min: float | None
    v_max: float | None
    v_mean: float | None
    v_std: float | None
    note: str


def find_repo_root(this_file: Path) -> Path:
    # this_file: stage2/mech_measure_analysis/src/select_phase3_measure_candidates_v1.py
    return this_file.resolve().parents[3]


def main() -> None:
    this_file = Path(__file__)
    repo_root = find_repo_root(this_file)
    print(f"{TAG} Repo root: {repo_root}")

    in_csv = (
        repo_root
        / "stage2"
        / "mech_measure_analysis"
        / "outputs"
        / "tables"
        / "stage2_mech_rung3_phase3_probability_like_candidates_v1.csv"
    )
    if not in_csv.is_file():
        raise SystemExit(f"{TAG} ERROR: input CSV not found: {in_csv}")

    df = pd.read_csv(in_csv)
    print(f"{TAG} Loaded Rung 3 candidates with {len(df)} rows")

    rows: list[CandidateRow] = []

    n_flag = 0
    n_measure = 0

    for _, r in df.iterrows():
        approx_binary = bool(r.get("approx_binary", False))
        approx_prob = bool(r.get("approx_probability_like", False))

        role: Role | None = None
        notes: list[str] = []

        if approx_binary:
            role = "flag_candidate"
            n_flag += 1
            notes.append("approx_binary_flag_from_rung3")
        elif approx_prob:
            role = "measure_candidate"
            n_measure += 1
            notes.append("approx_probability_like_from_rung3")
        else:
            # Not in [0,1] or otherwise not interesting for this rung
            continue

        note = "; ".join(notes)

        rows.append(
            CandidateRow(
                file_name=str(r.get("file_name", "")),
                rel_path=str(r.get("rel_path", "")),
                column_name=str(r.get("column_name", "")),
                dtype=str(r.get("dtype", "")),
                role=role,
                v_min=float(r["v_min"]) if "v_min" in r and not pd.isna(r["v_min"]) else None,
                v_max=float(r["v_max"]) if "v_max" in r and not pd.isna(r["v_max"]) else None,
                v_mean=float(r["v_mean"]) if "v_mean" in r and not pd.isna(r["v_mean"]) else None,
                v_std=float(r["v_std"]) if "v_std" in r and not pd.isna(r["v_std"]) else None,
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
    out_csv = out_dir / "stage2_mech_rung4_phase3_measure_and_flag_candidates_v1.csv"

    if rows:
        df_out = pd.DataFrame([asdict(r) for r in rows])
        df_out.to_csv(out_csv, index=False)
        print(
            f"{TAG} Wrote measure/flag candidates: {out_csv} "
            f"({out_csv.stat().st_size} bytes)"
        )
    else:
        print(f"{TAG} WARNING: no candidates found; nothing written")

    print(f"{TAG} Summary: measure_candidates={n_measure}, flag_candidates={n_flag}")


if __name__ == "__main__":
    main()
