#!/usr/bin/env python

from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List

import pandas as pd
import numpy as np


TAG = "[stage2_frw_corridor_rung9]"

# Project's special theta* (phi^phi) value
THETA_STAR = 2.1784575679


@dataclass
class SegmentRow:
    family_id: str
    segment_id: int
    start_index: int
    end_index: int
    n_pts: int
    theta_min: float
    theta_max: float
    theta_span: float
    contains_theta_star: bool


@dataclass
class ThetaStarAlignmentRow:
    family_id: str
    theta_star: float
    theta_closest: float
    abs_delta: float
    index_closest: int
    omega_lambda_closest: float | None
    E_vac_closest: float | None
    age_Gyr_closest: float | None
    n_true: int
    frac_of_grid: float


def find_repo_root() -> Path:
    """
    Infer repo root assuming this file lives at:
      <repo>/stage2/frw_corridor_analysis/src/...
    """
    here = Path(__file__).resolve()
    return here.parents[3]


def compute_segments(mask: pd.Series, theta: pd.Series, family_id: str) -> List[SegmentRow]:
    """
    Given a boolean mask over the theta grid, return contiguous segments
    in index space with basic theta geometry.
    """
    idx_true = np.flatnonzero(mask.to_numpy())
    rows: List[SegmentRow] = []

    if idx_true.size == 0:
        return rows

    seg_id = 0
    seg_start = idx_true[0]
    prev = idx_true[0]

    for i in idx_true[1:]:
        if i != prev + 1:
            # close previous segment
            seg_end = prev
            seg_id += 1

            theta_slice = theta.iloc[seg_start : seg_end + 1]
            theta_min = float(theta_slice.min())
            theta_max = float(theta_slice.max())
            theta_span = theta_max - theta_min
            contains_star = (theta_min <= THETA_STAR <= theta_max)

            rows.append(
                SegmentRow(
                    family_id=family_id,
                    segment_id=seg_id,
                    start_index=int(seg_start),
                    end_index=int(seg_end),
                    n_pts=int(seg_end - seg_start + 1),
                    theta_min=theta_min,
                    theta_max=theta_max,
                    theta_span=theta_span,
                    contains_theta_star=contains_star,
                )
            )

            # start new
            seg_start = i

        prev = i

    # close last segment
    seg_end = prev
    seg_id += 1
    theta_slice = theta.iloc[seg_start : seg_end + 1]
    theta_min = float(theta_slice.min())
    theta_max = float(theta_slice.max())
    theta_span = theta_max - theta_min
    contains_star = (theta_min <= THETA_STAR <= theta_max)

    rows.append(
        SegmentRow(
            family_id=family_id,
            segment_id=seg_id,
            start_index=int(seg_start),
            end_index=int(seg_end),
            n_pts=int(seg_end - seg_start + 1),
            theta_min=theta_min,
            theta_max=theta_max,
            theta_span=theta_span,
            contains_theta_star=contains_star,
        )
    )

    return rows


def main() -> None:
    repo_root = find_repo_root()
    print(f"{TAG} Repo root: {repo_root}")

    shape_mask_path = (
        repo_root
        / "phase4"
        / "outputs"
        / "tables"
        / "phase4_F1_frw_shape_probe_mask.csv"
    )
    if not shape_mask_path.exists():
        raise FileNotFoundError(f"Missing shape_probe_mask at {shape_mask_path}")

    df = pd.read_csv(shape_mask_path)
    print(f"{TAG} Loaded shape_probe_mask: {shape_mask_path} (rows={len(df)})")

    if "theta" not in df.columns:
        raise KeyError("Expected column 'theta' in shape_probe_mask table")

    theta = df["theta"].astype(float)

    # Optional physical columns, if present
    col_E_vac = "E_vac" if "E_vac" in df.columns else None
    col_omega_lambda = "omega_lambda" if "omega_lambda" in df.columns else None
    col_age_Gyr = "age_Gyr" if "age_Gyr" in df.columns else None

    required_flags = [
        "frw_viable",
        "lcdm_like",
        "in_toy_corridor",
        "shape_and_viable",
        "shape_and_lcdm",
    ]
    for flag in required_flags:
        if flag not in df.columns:
            raise KeyError(f"Expected boolean flag column '{flag}' in shape_probe_mask")

    family_defs: Dict[str, pd.Series] = {
        "F1_FRW_VIABLE": df["frw_viable"].astype(bool),
        "F2_LCDM_LIKE": df["lcdm_like"].astype(bool),
        "F3_TOY_CORRIDOR": df["in_toy_corridor"].astype(bool),
        "F4_CORRIDOR_AND_VIABLE": df["shape_and_viable"].astype(bool),
        "F5_CORRIDOR_AND_LCDM": df["shape_and_lcdm"].astype(bool),
    }

    n_grid = len(df)
    print(f"{TAG} Nominal grid size: {n_grid}")

    all_segments: List[SegmentRow] = []
    theta_star_rows: List[ThetaStarAlignmentRow] = []

    for fid, mask in family_defs.items():
        n_true = int(mask.sum())
        frac = n_true / n_grid if n_grid > 0 else 0.0
        print(f"{TAG} {fid}: n_true={n_true}, frac_of_grid={frac:.5f}")

        if n_true == 0:
            # still record empty alignment row
            theta_star_rows.append(
                ThetaStarAlignmentRow(
                    family_id=fid,
                    theta_star=THETA_STAR,
                    theta_closest=float("nan"),
                    abs_delta=float("nan"),
                    index_closest=-1,
                    omega_lambda_closest=None,
                    E_vac_closest=None,
                    age_Gyr_closest=None,
                    n_true=n_true,
                    frac_of_grid=frac,
                )
            )
            continue

        seg_rows = compute_segments(mask, theta, fid)
        all_segments.extend(seg_rows)

        # Closest point to theta*
        theta_true = theta[mask].to_numpy()
        idx_true = np.flatnonzero(mask.to_numpy())
        deltas = np.abs(theta_true - THETA_STAR)
        j = int(np.argmin(deltas))
        idx_closest = int(idx_true[j])
        theta_closest = float(theta_true[j])
        abs_delta = float(deltas[j])

        omega_val = None
        E_val = None
        age_val = None

        if col_omega_lambda is not None:
            omega_val = float(df.loc[idx_closest, col_omega_lambda])
        if col_E_vac is not None:
            E_val = float(df.loc[idx_closest, col_E_vac])
        if col_age_Gyr is not None:
            age_val = float(df.loc[idx_closest, col_age_Gyr])

        print(
            f"{TAG} {fid}: closest to theta*={THETA_STAR:.6f} "
            f"is theta={theta_closest:.6f} at index={idx_closest}, "
            f"|Δ|={abs_delta:.6e}"
        )

        theta_star_rows.append(
            ThetaStarAlignmentRow(
                family_id=fid,
                theta_star=THETA_STAR,
                theta_closest=theta_closest,
                abs_delta=abs_delta,
                index_closest=idx_closest,
                omega_lambda_closest=omega_val,
                E_vac_closest=E_val,
                age_Gyr_closest=age_val,
                n_true=n_true,
                frac_of_grid=frac,
            )
        )

    out_dir = (
        repo_root
        / "stage2"
        / "frw_corridor_analysis"
        / "outputs"
        / "tables"
    )
    out_dir.mkdir(parents=True, exist_ok=True)

    segments_csv = out_dir / "stage2_frw_corridor_rung9_segments_v1.csv"
    theta_star_csv = out_dir / "stage2_frw_corridor_rung9_theta_star_alignment_v1.csv"

    if all_segments:
        df_segments = pd.DataFrame([asdict(r) for r in all_segments])
        df_segments.to_csv(segments_csv, index=False)
        print(
            f"{TAG} Wrote segments table: {segments_csv} "
            f"({segments_csv.stat().st_size} bytes)"
        )
    else:
        print(f"{TAG} No segments to write (all families empty?)")

    df_theta_star = pd.DataFrame([asdict(r) for r in theta_star_rows])
    df_theta_star.to_csv(theta_star_csv, index=False)
    print(
        f"{TAG} Wrote theta* alignment table: {theta_star_csv} "
        f"({theta_star_csv.stat().st_size} bytes)"
    )

    ts = datetime.now(timezone.utc).isoformat()
    print(f"{TAG} Timestamp UTC: {ts}")


if __name__ == "__main__":
    main()
