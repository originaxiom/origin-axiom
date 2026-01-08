#!/usr/bin/env python
"""
Stage 2 – FRW corridor analysis
Rung 6: contiguity of FRW families in theta-space.

Reads the Phase 4 shape_probe_mask table on the nominal theta grid and,
for each family (F1–F5), finds contiguous theta segments where the family
mask is true. Outputs a CSV summarizing segment ranges and coverage.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List

import numpy as np
import pandas as pd


@dataclass
class SegmentRow:
    family_id: str
    segment_id: int
    theta_min: float
    theta_max: float
    n_pts: int
    frac_of_family: float
    frac_of_grid: float


def find_repo_root(start: Path) -> Path:
    """Walk upwards until we find a .git directory, or fall back to parent."""
    here = start.resolve()
    for p in [here] + list(here.parents):
        if (p / ".git").is_dir():
            return p
    # Fallback: assume we are somewhere under repo/src/... and go up a bit
    return here.parents[3]


def load_shape_probe_mask(repo_root: Path) -> pd.DataFrame:
    path = (
        repo_root
        / "phase4"
        / "outputs"
        / "tables"
        / "phase4_F1_frw_shape_probe_mask.csv"
    )
    if not path.is_file():
        raise FileNotFoundError(f"Missing shape_probe_mask at {path}")
    df = pd.read_csv(path)
    if "theta" not in df.columns:
        raise ValueError("Expected a 'theta' column in shape_probe_mask table")
    return df


def build_family_masks(df: pd.DataFrame) -> Dict[str, pd.Series]:
    required_cols = [
        "in_toy_corridor",
        "frw_viable",
        "lcdm_like",
        "shape_and_viable",
        "shape_and_lcdm",
    ]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(f"Missing expected columns in df: {missing}")

    fam_masks: Dict[str, pd.Series] = {
        "F1_FRW_VIABLE": df["frw_viable"].astype(bool),
        "F2_LCDM_LIKE": df["lcdm_like"].astype(bool),
        "F3_TOY_CORRIDOR": df["in_toy_corridor"].astype(bool),
        "F4_CORRIDOR_AND_VIABLE": df["shape_and_viable"].astype(bool),
        "F5_CORRIDOR_AND_LCDM": df["shape_and_lcdm"].astype(bool),
    }
    return fam_masks


def find_segments_for_family(
    theta: np.ndarray,
    mask: np.ndarray,
    family_id: str,
) -> List[SegmentRow]:
    """
    Given theta values and a boolean mask on the same grid, find contiguous
    segments (in index space) where mask is True.
    """
    n_grid = theta.size
    n_family = int(mask.sum())
    rows: List[SegmentRow] = []

    if n_family == 0:
        return rows

    # Work in theta-sorted order for sanity
    order = np.argsort(theta)
    theta_ord = theta[order]
    mask_ord = mask[order]

    # Indices (in the ordered grid) where mask is True
    true_idx = np.nonzero(mask_ord)[0]
    if true_idx.size == 0:
        return rows

    # Split into contiguous runs where index difference is 1
    breaks = np.where(np.diff(true_idx) > 1)[0] + 1
    segments = np.split(true_idx, breaks)

    for seg_id, seg_idx in enumerate(segments, start=1):
        n_pts = int(seg_idx.size)
        theta_min = float(theta_ord[seg_idx[0]])
        theta_max = float(theta_ord[seg_idx[-1]])
        frac_of_family = n_pts / n_family
        frac_of_grid = n_pts / n_grid

        rows.append(
            SegmentRow(
                family_id=family_id,
                segment_id=seg_id,
                theta_min=theta_min,
                theta_max=theta_max,
                n_pts=n_pts,
                frac_of_family=frac_of_family,
                frac_of_grid=frac_of_grid,
            )
        )

    return rows


def main() -> None:
    repo_root = find_repo_root(Path(__file__).parent)
    print(f"[stage2_frw_corridor_rung6] Repo root: {repo_root}")

    df = load_shape_probe_mask(repo_root)
    n_grid = df.shape[0]
    print(f"[stage2_frw_corridor_rung6] Loaded shape_probe_mask with {n_grid} rows")

    fam_masks = build_family_masks(df)
    theta = df["theta"].to_numpy(dtype=float)

    all_rows: List[SegmentRow] = []

    for fid, series in fam_masks.items():
        mask = series.to_numpy(dtype=bool)
        n_true = int(mask.sum())
        frac = n_true / n_grid if n_grid > 0 else 0.0
        print(
            f"[stage2_frw_corridor_rung6] {fid}: "
            f"n_theta={n_true}, frac_of_grid={frac:.5f}"
        )
        seg_rows = find_segments_for_family(theta, mask, fid)
        print(
            f"[stage2_frw_corridor_rung6]   segments: {len(seg_rows)} "
            f"(covering {sum(r.n_pts for r in seg_rows)} points)"
        )
        all_rows.extend(seg_rows)

    out_dir = (
        repo_root
        / "stage2"
        / "frw_corridor_analysis"
        / "outputs"
        / "tables"
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    out_csv = out_dir / "stage2_frw_corridor_rung6_contiguity_v1.csv"

    fieldnames = [
        "family_id",
        "segment_id",
        "theta_min",
        "theta_max",
        "n_pts",
        "frac_of_family",
        "frac_of_grid",
    ]

    df_out = pd.DataFrame([asdict(r) for r in all_rows], columns=fieldnames)
    df_out.to_csv(out_csv, index=False)

    print(
        f"[stage2_frw_corridor_rung6] Wrote {out_csv} "
        f"({out_csv.stat().st_size} bytes)"
    )
    ts = datetime.now(timezone.utc).isoformat()
    print(f"[stage2_frw_corridor_rung6] Timestamp UTC: {ts}")


if __name__ == "__main__":
    main()
