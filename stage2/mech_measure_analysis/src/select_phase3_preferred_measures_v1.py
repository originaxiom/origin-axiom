#!/usr/bin/env python3
"""
Stage 2: Mechanism / measure axis
Rung 6: Select preferred Phase 3 measure / flag candidates.

Inputs:
  - stage2/mech_measure_analysis/outputs/tables/
      stage2_mech_rung5_phase3_measure_theta_profiles_v1.csv

Outputs:
  - stage2/mech_measure_analysis/outputs/tables/
      stage2_mech_rung6_phase3_preferred_measure_candidates_v1.csv

This remains descriptive and downstream-only. It does NOT change any phase
claims; it just ranks candidates based on simple, explicit heuristics.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Literal

import numpy as np
import pandas as pd

TAG = "[stage2_mech_rung6]"

Role = Literal["measure_candidate", "flag_candidate"]


@dataclass
class PreferredRow:
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
    frac_flag_true: float | None

    has_theta: bool
    theta_col: str | None
    pearson_r_theta: float | None
    monotonic_score: float | None

    # Simple heuristic scores
    coverage_score: float
    boundedness_score: float
    monotone_score: float
    theta_score: float
    overall_score: float

    decision: str
    notes: str


def find_repo_root(this_file: Path) -> Path:
    # this_file: stage2/mech_measure_analysis/src/select_phase3_preferred_measures_v1.py
    return this_file.resolve().parents[3]


def safe_float(x) -> float | None:
    try:
        if pd.isna(x):
            return None
        return float(x)
    except Exception:
        return None


def score_row(r: pd.Series) -> tuple[float, float, float, float, float, str]:
    """
    Return (coverage_score, boundedness_score, monotone_score, theta_score, overall_score, decision, notes)
    with explicit, conservative heuristics.
    """
    notes = []

    role = str(r["role"])

    n_total = int(r.get("n_total", 0))
    n_finite = int(r.get("n_finite", 0))
    frac_in_0_1 = safe_float(r.get("frac_in_0_1"))
    monotonic_score = safe_float(r.get("monotonic_score"))
    pearson_r = safe_float(r.get("pearson_r_theta"))
    has_theta = bool(r.get("has_theta", False))

    # Coverage: fraction of finite values
    coverage = 0.0
    if n_total > 0:
        coverage = n_finite / n_total
    coverage_score = coverage
    if coverage < 0.9:
        notes.append(f"low_coverage≈{coverage:.2f}")

    # Boundedness: fraction in [0,1]; if missing, treat as 0
    bounded = frac_in_0_1 if frac_in_0_1 is not None else 0.0
    boundedness_score = bounded
    if bounded < 0.7:
        notes.append(f"weak_[0,1]_boundedness≈{bounded:.2f}")

    # Theta-related scores
    theta_score = 1.0 if has_theta else 0.0
    if not has_theta:
        notes.append("no_theta_column")

    # Monotonicity: prefer monotone-ish behaviour, but don't enforce too hard
    mono = monotonic_score if monotonic_score is not None else 0.0
    monotone_score = mono
    if monotonic_score is None:
        notes.append("no_monotonicity_estimate")

    # For role-dependent adjustments:
    if role == "flag_candidate":
        # Flags: we care less about monotonicity; more about [0,1] behaviour.
        alpha_cov = 0.3
        alpha_bound = 0.5
        alpha_mono = 0.1
        alpha_theta = 0.1
    else:
        # Measures: want coverage, boundedness, monotonicity, and theta.
        alpha_cov = 0.3
        alpha_bound = 0.3
        alpha_mono = 0.2
        alpha_theta = 0.2

    overall = (
        alpha_cov * coverage_score
        + alpha_bound * boundedness_score
        + alpha_mono * monotone_score
        + alpha_theta * theta_score
    )

    # Decision thresholds (conservative)
    if overall >= 0.8 and coverage >= 0.9 and bounded >= 0.8:
        decision = "keep_as_primary"
    elif overall >= 0.6 and coverage >= 0.8 and bounded >= 0.6:
        decision = "keep_as_secondary"
    else:
        decision = "discard_for_now"
        notes.append("below_thresholds")

    # Light-touch note on Pearson r if available
    if pearson_r is not None:
        notes.append(f"pearson_r≈{pearson_r:.2f}")

    return (
        coverage_score,
        boundedness_score,
        monotone_score,
        theta_score,
        overall,
        decision,
        "; ".join(notes),
    )


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
        / "stage2_mech_rung5_phase3_measure_theta_profiles_v1.csv"
    )
    if not in_csv.is_file():
        raise SystemExit(f"{TAG} ERROR: input CSV not found: {in_csv}")

    df = pd.read_csv(in_csv)
    print(f"{TAG} Loaded theta profiles with {len(df)} rows")

    rows: list[PreferredRow] = []

    for _, r in df.iterrows():
        file_name = str(r.get("file_name", ""))
        rel_path = str(r.get("rel_path", ""))
        column_name = str(r.get("column_name", ""))
        role = str(r.get("role", "measure_candidate"))
        dtype = str(r.get("dtype", ""))

        (
            coverage_score,
            boundedness_score,
            monotone_score,
            theta_score,
            overall_score,
            decision,
            notes,
        ) = score_row(r)

        row = PreferredRow(
            file_name=file_name,
            rel_path=rel_path,
            column_name=column_name,
            role=role,  # type: ignore[arg-type]
            dtype=dtype,
            n_total=int(r.get("n_total", 0)),
            n_finite=int(r.get("n_finite", 0)),
            v_min=safe_float(r.get("v_min")),
            v_max=safe_float(r.get("v_max")),
            v_mean=safe_float(r.get("v_mean")),
            v_std=safe_float(r.get("v_std")),
            frac_in_0_1=safe_float(r.get("frac_in_0_1")),
            frac_positive=safe_float(r.get("frac_positive")),
            frac_flag_true=safe_float(r.get("frac_flag_true")),
            has_theta=bool(r.get("has_theta", False)),
            theta_col=str(r.get("theta_col")) if not pd.isna(r.get("theta_col")) else None,
            pearson_r_theta=safe_float(r.get("pearson_r_theta")),
            monotonic_score=safe_float(r.get("monotonic_score")),
            coverage_score=coverage_score,
            boundedness_score=boundedness_score,
            monotone_score=monotone_score,
            theta_score=theta_score,
            overall_score=overall_score,
            decision=decision,
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
    out_csv = (
        out_dir
        / "stage2_mech_rung6_phase3_preferred_measure_candidates_v1.csv"
    )

    if rows:
        df_out = pd.DataFrame([asdict(rr) for rr in rows])
        df_out.to_csv(out_csv, index=False)
        print(
            f"{TAG} Wrote preferred candidates: {out_csv} "
            f"({out_csv.stat().st_size} bytes)"
        )
    else:
        print(f"{TAG} WARNING: no rows produced; nothing written")


if __name__ == "__main__":
    main()
