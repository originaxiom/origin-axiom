#!/usr/bin/env python
"""
Stage 2 – FRW corridor analysis
Rung 8: 1D smoothing / erosion robustness along θ.

This rung asks:
- If we apply simple 1D majority filters along the θ-grid for our
  FRW families (F1–F5), do the corridors/islands remain recognisably
  the same?
- Or are they so fragile that mild smoothing destroys their structure?

Inputs
------
- phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv

Families (re-used from prior rungs)
-----------------------------------
F1_FRW_VIABLE        -> column 'frw_viable'
F2_LCDM_LIKE         -> column 'lcdm_like'
F3_TOY_CORRIDOR      -> column 'in_toy_corridor'
F4_CORRIDOR_AND_VIABLE -> column 'shape_and_viable'
F5_CORRIDOR_AND_LCDM -> column 'shape_and_lcdm'

Outputs
-------
- stage2/frw_corridor_analysis/outputs/tables/
    stage2_frw_corridor_rung8_smoothing_v1.csv

Each row reports, for a given (family, window_size):

- n_theta: nominal grid size
- window: smoothing window (in θ index units)
- n_true_before / n_true_after
- frac_true_before / frac_true_after (of full grid)
- n_segments_before / n_segments_after
- jaccard: |A ∩ B| / |A ∪ B| for {before, after}
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, List

import numpy as np
import pandas as pd
from datetime import datetime, timezone


TAG = "[stage2_frw_corridor_rung8]"


def find_repo_root(start: Path | None = None) -> Path:
    """
    Heuristic: walk upwards from this file location until we find .git.
    Fallback to current working directory.
    """
    if start is None:
        start = Path(__file__).resolve()
    for p in [start, *start.parents]:
        if (p / ".git").exists():
            return p
    return Path.cwd()


def contiguous_segments(mask: np.ndarray) -> int:
    """
    Count number of contiguous True segments in a 1D boolean mask.
    """
    if mask.size == 0:
        return 0
    segs = 0
    prev = False
    for v in mask:
        if v and not prev:
            segs += 1
        prev = v
    return segs


def majority_filter_1d(mask: np.ndarray, window: int) -> np.ndarray:
    """
    Simple 1D majority filter along the θ index.

    - window must be odd
    - for each index i, look at mask[i - k : i + k + 1], where k = window // 2,
      clipped to the valid range.
    - output is True at i if >= 50% of the window entries are True.
    """
    if window <= 1:
        return mask.copy()
    if window % 2 == 0:
        raise ValueError(f"window must be odd, got {window}")

    n = mask.size
    out = np.zeros_like(mask, dtype=bool)
    k = window // 2
    for i in range(n):
        lo = max(0, i - k)
        hi = min(n, i + k + 1)
        window_slice = mask[lo:hi]
        true_count = int(window_slice.sum())
        if true_count * 2 >= (hi - lo):
            out[i] = True
    return out


@dataclass
class SmoothingRow:
    family_id: str
    column: str
    n_theta: int
    window: int
    n_true_before: int
    n_true_after: int
    frac_true_before: float
    frac_true_after: float
    n_segments_before: int
    n_segments_after: int
    jaccard: float


def main() -> None:
    repo_root = find_repo_root()
    print(f"{TAG} Repo root: {repo_root}")

    mask_path = (
        repo_root
        / "phase4"
        / "outputs"
        / "tables"
        / "phase4_F1_frw_shape_probe_mask.csv"
    )
    if not mask_path.exists():
        raise FileNotFoundError(f"{TAG} Missing mask file: {mask_path}")

    df = pd.read_csv(mask_path)
    n_theta = df.shape[0]
    print(f"{TAG} Loaded shape_probe_mask with {n_theta} rows")

    # Families as in previous rungs
    families: Dict[str, str] = {
        "F1_FRW_VIABLE": "frw_viable",
        "F2_LCDM_LIKE": "lcdm_like",
        "F3_TOY_CORRIDOR": "in_toy_corridor",
        "F4_CORRIDOR_AND_VIABLE": "shape_and_viable",
        "F5_CORRIDOR_AND_LCDM": "shape_and_lcdm",
    }

    for fid, col in families.items():
        if col not in df.columns:
            raise KeyError(f"{TAG} Column {col!r} for {fid} not found in {mask_path}")

    windows = [1, 3, 5]  # 1 = identity (sanity), 3 and 5 = mild smoothing

    rows: List[SmoothingRow] = []

    for fid, col in families.items():
        base_mask = df[col].astype(bool).to_numpy()
        n_true_full = int(base_mask.sum())
        frac_full = n_true_full / float(n_theta)
        n_seg_full = contiguous_segments(base_mask)

        print(
            f"{TAG} {fid}: n_true_full={n_true_full}, "
            f"frac_full={frac_full:.5f}, segments_full={n_seg_full}"
        )

        for w in windows:
            if w == 1:
                smoothed = base_mask.copy()
            else:
                smoothed = majority_filter_1d(base_mask, w)

            n_true_s = int(smoothed.sum())
            frac_s = n_true_s / float(n_theta)
            n_seg_s = contiguous_segments(smoothed)

            # Jaccard similarity between base_mask and smoothed
            both_true = np.logical_and(base_mask, smoothed).sum()
            either_true = np.logical_or(base_mask, smoothed).sum()
            jaccard = float(both_true) / float(either_true) if either_true > 0 else 1.0

            print(
                f"{TAG} {fid}, window={w}: "
                f"n_true_before={n_true_full}, n_true_after={n_true_s}, "
                f"frac_before={frac_full:.5f}, frac_after={frac_s:.5f}, "
                f"segments_before={n_seg_full}, segments_after={n_seg_s}, "
                f"jaccard={jaccard:.5f}"
            )

            rows.append(
                SmoothingRow(
                    family_id=fid,
                    column=col,
                    n_theta=n_theta,
                    window=w,
                    n_true_before=n_true_full,
                    n_true_after=n_true_s,
                    frac_true_before=frac_full,
                    frac_true_after=frac_s,
                    n_segments_before=n_seg_full,
                    n_segments_after=n_seg_s,
                    jaccard=jaccard,
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
    out_csv = out_dir / "stage2_frw_corridor_rung8_smoothing_v1.csv"

    df_out = pd.DataFrame([asdict(r) for r in rows])
    df_out.to_csv(out_csv, index=False)

    print(
        f"{TAG} Wrote {out_csv} ({out_csv.stat().st_size} bytes)"
    )
    ts = datetime.now(timezone.utc).isoformat()
    print(f"{TAG} Timestamp UTC: {ts}")


if __name__ == "__main__":
    main()
