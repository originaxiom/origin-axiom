#!/usr/bin/env python3

"""
Stage 2 — Joint mech–FRW empirical anchor kernel analysis (A5b, v1)

Takes:
- the joint mech–FRW grid, and
- the empirical FRW anchor mask,

and characterizes the kernel:
- points with FRW viability,
- inside the Stage 2 toy corridor,
- inside the empirical background-cosmology box.

Outputs:
- a segment-level CSV with θ ranges and distances to θ★,
- a short printed summary.

Diagnostic only. No promotion or physical claims.
"""

from pathlib import Path
import math
import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[3]

JOINT_GRID = REPO_ROOT / "stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv"
ANCHOR_MASK = REPO_ROOT / "stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_empirical_anchor_mask_v1.csv"

OUT_DIR = REPO_ROOT / "stage2/joint_mech_frw_analysis/outputs/tables"
OUT_TABLE = OUT_DIR / "stage2_joint_mech_frw_anchor_kernel_v1.csv"

# Reference theta_star (φ^φ-style value used elsewhere in the project)
THETA_STAR = 2.178458


def detect_anchor_mask_column(df_anchor: pd.DataFrame) -> str:
    known_candidates = [
        "in_empirical_anchor",
        "in_anchor",
        "empirical_anchor_mask",
        "in_empirical_box",
        "in_data_box",
    ]
    for name in known_candidates:
        if name in df_anchor.columns:
            return name

    bool_like = []
    for c in df_anchor.columns:
        if c == "theta":
            continue
        series = df_anchor[c].dropna()
        if series.empty:
            continue
        if series.isin([0, 1, True, False]).all():
            bool_like.append(c)

    if len(bool_like) == 1:
        return bool_like[0]

    cols = ", ".join(df_anchor.columns)
    bool_cols = ", ".join(bool_like) if bool_like else "(none)"
    raise RuntimeError(
        "Could not unambiguously detect empirical anchor mask column.\n"
        f"  Anchor table columns: {cols}\n"
        f"  Boolean-like candidates (excluding 'theta'): {bool_cols}\n"
        "Please ensure there is a dedicated mask column (e.g. 'in_empirical_anchor' or 'in_anchor')."
    )


def find_segments(theta_idx: pd.Series) -> list[tuple[int, int]]:
    """Given a series of integer indices, return contiguous [start, end] segments."""
    idx_sorted = sorted(int(i) for i in theta_idx)
    if not idx_sorted:
        return []

    segments = []
    start = idx_sorted[0]
    prev = idx_sorted[0]

    for k in idx_sorted[1:]:
        if k == prev + 1:
            prev = k
            continue
        # end of segment
        segments.append((start, prev))
        start = k
        prev = k

    segments.append((start, prev))
    return segments


def main() -> None:
    # Load joint grid
    df_joint = pd.read_csv(JOINT_GRID)

    required = ["theta_index", "theta", "frw_viable", "in_toy_corridor"]
    for c in required:
        if c not in df_joint.columns:
            raise RuntimeError(f"Missing column in joint grid: {c}")

    # Load anchor mask
    df_anchor = pd.read_csv(ANCHOR_MASK)
    if "theta" not in df_anchor.columns:
        raise RuntimeError("Anchor mask table must contain a 'theta' column")

    anchor_mask_col = detect_anchor_mask_column(df_anchor)

    # Merge to get anchor mask on joint grid
    df = df_joint.merge(
        df_anchor[["theta", anchor_mask_col]],
        on="theta",
        how="left",
        validate="one_to_one",
    )

    df[anchor_mask_col] = df[anchor_mask_col].fillna(False)

    mask_anchor = df[anchor_mask_col].astype(bool)
    mask_viable = df["frw_viable"].astype(bool)
    mask_corridor = df["in_toy_corridor"].astype(bool)

    kernel_mask = mask_anchor & mask_viable & mask_corridor
    df_kernel = df.loc[kernel_mask].copy()

    n_total = len(df)
    n_kernel = len(df_kernel)

    # Compute theta-star distances
    df_kernel["theta_star_distance"] = (df_kernel["theta"] - THETA_STAR).abs()

    # Segment structure by theta_index
    segments_idx = find_segments(df_kernel["theta_index"])
    rows = []
    for seg_id, (start_idx, end_idx) in enumerate(segments_idx, start=1):
        seg = df_kernel[(df_kernel["theta_index"] >= start_idx) & (df_kernel["theta_index"] <= end_idx)]
        theta_min = seg["theta"].min()
        theta_max = seg["theta"].max()
        n_seg = len(seg)
        dist_min = seg["theta_star_distance"].min()
        dist_at_min = float(
            seg.loc[seg["theta_star_distance"].idxmin(), "theta"]
        ) if n_seg > 0 else math.nan
        contains_theta_star = bool((theta_min <= THETA_STAR) and (THETA_STAR <= theta_max))

        rows.append(
            {
                "segment_id": seg_id,
                "theta_index_start": start_idx,
                "theta_index_end": end_idx,
                "n_theta_segment": n_seg,
                "theta_min": float(theta_min),
                "theta_max": float(theta_max),
                "contains_theta_star": contains_theta_star,
                "min_theta_star_distance": float(dist_min),
                "theta_at_min_distance": dist_at_min,
            }
        )

    df_out = pd.DataFrame(rows)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    df_out.to_csv(OUT_TABLE, index=False)

    # Print summary
    print("[stage2_anchor_kernel_rung5b]")
    print(f"  Total grid rows: {n_total}")
    print(f"  Kernel size (FRW_VIABLE ∧ TOY_CORRIDOR ∧ ANCHOR): n={n_kernel}")

    if n_kernel == 0:
        print("  Kernel is empty; nothing further to characterize.")
        return

    print(f"  Number of contiguous theta-index segments: {len(segments_idx)}")
    for r in rows:
        print(
            f"  Segment {r['segment_id']}: "
            f"theta_index[{r['theta_index_start']}–{r['theta_index_end']}], "
            f"n={r['n_theta_segment']}, "
            f"theta∈[{r['theta_min']:.6f}, {r['theta_max']:.6f}], "
            f"contains_theta_star={r['contains_theta_star']}, "
            f"min|theta-θ*|={r['min_theta_star_distance']:.6e} "
            f"at theta={r['theta_at_min_distance']:.6f}"
        )

    print(f"  Output written: {OUT_TABLE}")


if __name__ == "__main__":
    main()
