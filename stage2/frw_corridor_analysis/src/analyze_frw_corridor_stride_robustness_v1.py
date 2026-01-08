#!/usr/bin/env python3
"""
Stage 2 – FRW corridor analysis
Rung 7: θ-stride robustness of FRW families.

This script:
  - loads phase4_F1_frw_shape_probe_mask.csv
  - defines families F1–F5 in terms of boolean columns,
  - for strides {1, 2, 4, 8}:
      * subsamples the θ-grid by that stride,
      * counts how many points are true for each family,
      * computes fractions wrt the subgrid and full grid,
      * counts how many contiguous θ-segments are present.
  - writes a summary CSV:
      stage2/frw_corridor_analysis/outputs/tables/
          stage2_frw_corridor_rung7_stride_robustness_v1.csv

This is a Stage 2 descriptive rung only; it does not feed back into
any Phase-4/5 logic or PDFs.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List

import pandas as pd


@dataclass
class StrideResult:
    family_id: str
    stride: int
    nominal_n_theta: int
    effective_n_theta: int
    n_true: int
    frac_of_subgrid: float
    frac_of_fullgrid: float
    n_segments: int


FAMILY_DEFS: Dict[str, str] = {
    "F1_FRW_VIABLE": "frw_viable",
    "F2_LCDM_LIKE": "lcdm_like",
    "F3_TOY_CORRIDOR": "in_toy_corridor",
    "F4_CORRIDOR_AND_VIABLE": "shape_and_viable",
    "F5_CORRIDOR_AND_LCDM": "shape_and_lcdm",
    # F6_DATA_OK exists but is identically false in the current baseline,
    # so we skip it for this robustness rung.
}


def find_segments(mask: pd.Series) -> int:
    """
    Count contiguous True segments in a 1D boolean mask.

    The grid is treated as non-periodic here (no wrap-around).
    """
    if mask.empty:
        return 0

    # ensure boolean Series
    m = mask.astype(bool).values
    n = m.shape[0]
    if n == 0:
        return 0

    segments = 0
    in_seg = False
    for val in m:
        if val and not in_seg:
            segments += 1
            in_seg = True
        elif not val and in_seg:
            in_seg = False
    return segments


def main() -> None:
    repo_root = Path(__file__).resolve().parents[3]
    print(f"[stage2_frw_corridor_rung7] Repo root: {repo_root}")

    shape_mask_path = (
        repo_root
        / "phase4"
        / "outputs"
        / "tables"
        / "phase4_F1_frw_shape_probe_mask.csv"
    )
    if not shape_mask_path.is_file():
        raise FileNotFoundError(f"Missing shape_probe_mask CSV: {shape_mask_path}")

    df = pd.read_csv(shape_mask_path)
    nominal_n_theta = df.shape[0]
    print(
        f"[stage2_frw_corridor_rung7] Loaded shape_probe_mask: "
        f"{shape_mask_path} (rows={nominal_n_theta})"
    )

    strides = [1, 2, 4, 8]
    results: List[StrideResult] = []

    for family_id, col in FAMILY_DEFS.items():
        if col not in df.columns:
            raise KeyError(
                f"Expected column '{col}' for {family_id} not found in "
                f"{shape_mask_path}"
            )

        full_mask = df[col].astype(bool)
        print(
            f"[stage2_frw_corridor_rung7] {family_id}: "
            f"nominal_n_theta={nominal_n_theta}, n_true_full={full_mask.sum()}"
        )

        for stride in strides:
            sub_mask = full_mask.iloc[::stride].reset_index(drop=True)
            effective_n_theta = sub_mask.shape[0]
            n_true = int(sub_mask.sum())

            frac_sub = float(n_true) / float(effective_n_theta) if effective_n_theta > 0 else 0.0
            frac_full = float(n_true) / float(nominal_n_theta) if nominal_n_theta > 0 else 0.0

            n_segments = find_segments(sub_mask)

            print(
                f"[stage2_frw_corridor_rung7] {family_id}, stride={stride}: "
                f"effective_n_theta={effective_n_theta}, "
                f"n_true={n_true}, "
                f"frac_of_subgrid={frac_sub:.5f}, "
                f"frac_of_fullgrid={frac_full:.5f}, "
                f"n_segments={n_segments}"
            )

            results.append(
                StrideResult(
                    family_id=family_id,
                    stride=stride,
                    nominal_n_theta=nominal_n_theta,
                    effective_n_theta=effective_n_theta,
                    n_true=n_true,
                    frac_of_subgrid=frac_sub,
                    frac_of_fullgrid=frac_full,
                    n_segments=n_segments,
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
    out_csv = out_dir / "stage2_frw_corridor_rung7_stride_robustness_v1.csv"

    fieldnames = [
        "family_id",
        "stride",
        "nominal_n_theta",
        "effective_n_theta",
        "n_true",
        "frac_of_subgrid",
        "frac_of_fullgrid",
        "n_segments",
    ]
    df_out = pd.DataFrame([asdict(r) for r in results], columns=fieldnames)
    df_out.to_csv(out_csv, index=False)

    print(
        f"[stage2_frw_corridor_rung7] Wrote {out_csv} "
        f"({out_csv.stat().st_size} bytes)"
    )
    ts = datetime.now(timezone.utc).isoformat()
    print(f"[stage2_frw_corridor_rung7] Timestamp: {ts}")


if __name__ == "__main__":
    main()
