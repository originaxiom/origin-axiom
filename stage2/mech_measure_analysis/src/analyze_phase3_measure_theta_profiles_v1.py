#!/usr/bin/env python3
"""
Stage 2: Mechanism / measure axis
Rung 5: Theta-profiles for Phase 3 measure/flag candidates.

Inputs:
  - stage2/mech_measure_analysis/outputs/tables/
      stage2_mech_rung4_phase3_measure_and_flag_candidates_v1.csv

For each candidate:
  - Load its source CSV (rel_path) under repo root.
  - Recompute basic stats for the target column.
  - Estimate fraction of values in [0,1] and (for flags) fraction of "true".
  - If a theta-like column exists, compute:
      * Pearson correlation with theta (if variance > 0)
      * A crude monotonicity score: fraction of same-sign steps along sorted theta.

Outputs:
  - stage2/mech_measure_analysis/outputs/tables/
      stage2_mech_rung5_phase3_measure_theta_profiles_v1.csv

This remains descriptive and downstream-only.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Literal

import numpy as np
import pandas as pd

TAG = "[stage2_mech_rung5]"

Role = Literal["measure_candidate", "flag_candidate"]


@dataclass
class ThetaProfileRow:
    file_name: str
    rel_path: str
    column_name: str
    role: Role
    dtype: str

    n_total: int
    n_finite: int

    v_min: float | None
    v_max: float | None
    v_mean: float | None
    v_std: float | None

    frac_in_0_1: float | None
    frac_positive: float | None
    frac_flag_true: float | None  # only meaningful for flag_candidate

    has_theta: bool
    theta_col: str | None

    pearson_r_theta: float | None
    monotonic_score: float | None  # fraction of same-sign steps along theta

    notes: str


def find_repo_root(this_file: Path) -> Path:
    # this_file: stage2/mech_measure_analysis/src/analyze_phase3_measure_theta_profiles_v1.py
    return this_file.resolve().parents[3]


def find_theta_column(df: pd.DataFrame) -> str | None:
    """
    Heuristic: pick the first column whose name contains 'theta' (case-insensitive).
    """
    for col in df.columns:
        if "theta" in str(col).lower():
            return col
    return None


def safe_pearson(x: np.ndarray, y: np.ndarray) -> float | None:
    if x.size < 2 or y.size < 2:
        return None
    if np.allclose(np.std(x), 0.0) or np.allclose(np.std(y), 0.0):
        return None
    x0 = (x - x.mean()) / x.std()
    y0 = (y - y.mean()) / y.std()
    r = float(np.mean(x0 * y0))
    return r


def monotonicity_score(theta: np.ndarray, vals: np.ndarray) -> float | None:
    """
    Very crude monotonicity proxy:
      - Sort by theta
      - Look at successive differences of vals
      - Score = fraction of non-zero steps that share the majority sign

    Returns None if fewer than 3 finite points.
    """
    if theta.size < 3:
        return None
    order = np.argsort(theta)
    v_sorted = vals[order]
    diffs = np.diff(v_sorted)
    mask = np.isfinite(diffs) & (diffs != 0.0)
    diffs = diffs[mask]
    if diffs.size == 0:
        return 1.0  # perfectly flat => treat as "fully monotone" for this crude metric
    n_pos = np.sum(diffs > 0)
    n_neg = np.sum(diffs < 0)
    majority = max(n_pos, n_neg)
    return float(majority) / float(n_pos + n_neg)


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
        / "stage2_mech_rung4_phase3_measure_and_flag_candidates_v1.csv"
    )
    if not in_csv.is_file():
        raise SystemExit(f"{TAG} ERROR: input CSV not found: {in_csv}")

    df_candidates = pd.read_csv(in_csv)
    print(f"{TAG} Loaded Rung 4 candidates with {len(df_candidates)} rows")

    rows: list[ThetaProfileRow] = []

    for _, r in df_candidates.iterrows():
        rel_path = Path(str(r["rel_path"]))
        file_name = str(r.get("file_name", rel_path.name))
        column_name = str(r["column_name"])
        role = str(r["role"])
        dtype = str(r.get("dtype", ""))

        src_csv = repo_root / rel_path
        if not src_csv.is_file():
            print(f"{TAG} WARNING: missing source CSV: {src_csv}, skipping")
            continue

        df = pd.read_csv(src_csv)
        if column_name not in df.columns:
            print(
                f"{TAG} WARNING: column '{column_name}' not found in {rel_path}, skipping"
            )
            continue

        vals = df[column_name].to_numpy()
        finite_mask = np.isfinite(vals)
        vals_f = vals[finite_mask]

        n_total = int(vals.size)
        n_finite = int(vals_f.size)

        if n_finite == 0:
            v_min = v_max = v_mean = v_std = None
            frac_in_0_1 = frac_positive = frac_flag_true = None
            has_theta = False
            theta_col = None
            pearson_r = None
            mono = None
            notes = "no_finite_values"
        else:
            v_min = float(np.min(vals_f))
            v_max = float(np.max(vals_f))
            v_mean = float(np.mean(vals_f))
            v_std = float(np.std(vals_f))

            in_0_1 = (vals_f >= 0.0) & (vals_f <= 1.0)
            frac_in_0_1 = float(np.mean(in_0_1))

            positive = vals_f > 0.0
            frac_positive = float(np.mean(positive))

            frac_flag_true = None
            notes_list: list[str] = []

            if role == "flag_candidate":
                # Crude "true" definition: val > 0.5 OR, if values are 0/1-ish, val > 0
                # We keep both interpretations in the notes.
                gt_half = vals_f > 0.5
                frac_flag_true = float(np.mean(gt_half))
                notes_list.append("flag_true≈val>0.5")

            # Theta-related diagnostics
            theta_col = find_theta_column(df)
            if theta_col is not None:
                theta_vals = df[theta_col].to_numpy()
                theta_f = theta_vals[finite_mask]
                has_theta = True

                pearson_r = safe_pearson(theta_f, vals_f)
                mono = monotonicity_score(theta_f, vals_f)
            else:
                has_theta = False
                theta_col = None
                pearson_r = None
                mono = None
                notes_list.append("no_theta_column_detected")

            notes = "; ".join(notes_list)

        row = ThetaProfileRow(
            file_name=file_name,
            rel_path=str(rel_path),
            column_name=column_name,
            role=role,  # type: ignore[arg-type]
            dtype=dtype,
            n_total=n_total,
            n_finite=n_finite,
            v_min=v_min,
            v_max=v_max,
            v_mean=v_mean,
            v_std=v_std,
            frac_in_0_1=frac_in_0_1,
            frac_positive=frac_positive,
            frac_flag_true=frac_flag_true,
            has_theta=has_theta,
            theta_col=theta_col,
            pearson_r_theta=pearson_r,
            monotonic_score=mono,
            notes=notes,
        )
        rows.append(row)

    out_dir = (
        repo_root
        / "stage2"
        / "mech_measure_analysis"
        / "outputs"
        / "tables"
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    out_csv = out_dir / "stage2_mech_rung5_phase3_measure_theta_profiles_v1.csv"

    if rows:
        df_out = pd.DataFrame([asdict(r) for r in rows])
        df_out.to_csv(out_csv, index=False)
        print(
            f"{TAG} Wrote theta profiles: {out_csv} "
            f"({out_csv.stat().st_size} bytes)"
        )
    else:
        print(f"{TAG} WARNING: no rows produced; nothing written")


if __name__ == "__main__":
    main()
