from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict

import numpy as np
import pandas as pd


@dataclass
class FamilyDef:
    family_id: str
    label: str
    notes: str


def find_repo_root(start: Path) -> Path:
    """
    Walk upwards until we find a .git directory.
    Fall back to parent[3] heuristic if not found.
    """
    for p in [start] + list(start.parents):
        if (p / ".git").is_dir():
            return p
    # Heuristic: .../origin-axiom/stage2/frw_corridor_analysis/src/this_file.py
    # parents[3] -> repo root
    return start.parents[3]


def load_masks(repo_root: Path) -> Dict[str, pd.DataFrame]:
    base = repo_root / "phase4" / "outputs" / "tables"
    paths = {
        "shape": base / "phase4_F1_frw_shape_probe_mask.csv",
        "data": base / "phase4_F1_frw_data_probe_mask.csv",
    }

    dfs: Dict[str, pd.DataFrame] = {}
    for key, path in paths.items():
        if not path.is_file():
            raise FileNotFoundError(f"Expected mask at {path} (key={key})")
        df = pd.read_csv(path)
        dfs[key] = df
    return dfs


def build_family_series(
    shape_df: pd.DataFrame, data_df: pd.DataFrame
) -> Dict[str, pd.Series]:
    """
    Build boolean series for each family on the common theta grid.

    We align data_df to shape_df via theta and require 1-1 mapping.
    """
    n_grid = len(shape_df)
    if len(data_df) != n_grid:
        raise ValueError(
            f"Shape and data probe masks differ in length: "
            f"{n_grid} vs {len(data_df)}"
        )

    # Align by theta explicitly (not just relying on row order)
    merged = pd.merge(
        shape_df,
        data_df[["theta", "data_ok"]],
        on="theta",
        how="inner",
        suffixes=("", "_data"),
    )
    if len(merged) != n_grid:
        raise ValueError(
            "Theta alignment between shape and data probe masks "
            f"changed grid size: {n_grid} -> {len(merged)}"
        )

    fam: Dict[str, pd.Series] = {}

    # These columns are known from Rung 2 logs
    fam["F1_FRW_VIABLE"] = merged["frw_viable"].astype(bool)
    fam["F2_LCDM_LIKE"] = merged["lcdm_like"].astype(bool)
    fam["F3_TOY_CORRIDOR"] = merged["in_toy_corridor"].astype(bool)
    fam["F4_CORRIDOR_AND_VIABLE"] = merged["shape_and_viable"].astype(bool)
    fam["F5_CORRIDOR_AND_LCDM"] = merged["shape_and_lcdm"].astype(bool)
    fam["F6_DATA_OK"] = merged["data_ok"].astype(bool)

    return fam


def family_defs() -> Dict[str, FamilyDef]:
    return {
        "F1_FRW_VIABLE": FamilyDef(
            family_id="F1_FRW_VIABLE",
            label="FRW-viable baseline",
            notes=(
                "theta grid points that satisfy the FRW viability mask "
                "(has_matter_era & has_late_accel & smooth_H2)."
            ),
        ),
        "F2_LCDM_LIKE": FamilyDef(
            family_id="F2_LCDM_LIKE",
            label="LCDM-like FRW",
            notes=(
                "subset of the grid that passes both FRW viability and the "
                "LCDM-like diagnostic (lcdm_like == True)."
            ),
        ),
        "F3_TOY_CORRIDOR": FamilyDef(
            family_id="F3_TOY_CORRIDOR",
            label="Toy corridor",
            notes=(
                "theta grid points inside the toy-theory FRW corridor "
                "defined in Phase 4 (in_toy_corridor == True)."
            ),
        ),
        "F4_CORRIDOR_AND_VIABLE": FamilyDef(
            family_id="F4_CORRIDOR_AND_VIABLE",
            label="Toy corridor ∩ FRW-viable",
            notes=(
                "intersection of the toy corridor and FRW viability "
                "(shape_and_viable == True)."
            ),
        ),
        "F5_CORRIDOR_AND_LCDM": FamilyDef(
            family_id="F5_CORRIDOR_AND_LCDM",
            label="Toy corridor ∩ LCDM-like",
            notes=(
                "intersection of the toy corridor and LCDM-like mask "
                "(shape_and_lcdm == True)."
            ),
        ),
        "F6_DATA_OK": FamilyDef(
            family_id="F6_DATA_OK",
            label="External data-compatible",
            notes=(
                "theta grid points that would pass the external data "
                "mask (data_ok == True) once data is populated."
            ),
        ),
    }


def compute_overlap(
    fam_series: Dict[str, pd.Series], defs: Dict[str, FamilyDef]
) -> pd.DataFrame:
    ids = list(fam_series.keys())
    n_grid = len(next(iter(fam_series.values())))

    rows = []
    for i in ids:
        a = fam_series[i].to_numpy()
        n_i = int(a.sum())
        frac_i = n_i / n_grid if n_grid > 0 else float("nan")

        for j in ids:
            b = fam_series[j].to_numpy()
            n_j = int(b.sum())
            frac_j = n_j / n_grid if n_grid > 0 else float("nan")

            inter = int(np.logical_and(a, b).sum())
            union = int(np.logical_or(a, b).sum())

            frac_inter = inter / n_grid if n_grid > 0 else float("nan")
            frac_cond_i = inter / n_i if n_i > 0 else float("nan")
            frac_cond_j = inter / n_j if n_j > 0 else float("nan")
            jaccard = inter / union if union > 0 else float("nan")

            rows.append(
                {
                    "family_i": i,
                    "family_j": j,
                    "label_i": defs[i].label,
                    "label_j": defs[j].label,
                    "n_grid": n_grid,
                    "n_i": n_i,
                    "n_j": n_j,
                    "frac_i": frac_i,
                    "frac_j": frac_j,
                    "n_intersect": inter,
                    "frac_intersect": frac_inter,
                    "frac_j_given_i": frac_cond_i,
                    "frac_i_given_j": frac_cond_j,
                    "jaccard": jaccard,
                }
            )

    return pd.DataFrame(rows)


def main() -> None:
    here = Path(__file__).resolve()
    repo_root = find_repo_root(here)
    print(f"[stage2_frw_corridor_rung4] Repo root: {repo_root}")

    dfs = load_masks(repo_root)
    shape_df = dfs["shape"]
    data_df = dfs["data"]

    fam_series = build_family_series(shape_df, data_df)
    defs = family_defs()

    # Quick cardinality summary (should echo Rung 3 counts)
    n_grid = len(next(iter(fam_series.values())))
    print(f"[stage2_frw_corridor_rung4] Nominal grid size: {n_grid}")
    for fid, s in fam_series.items():
        n_true = int(s.sum())
        frac = n_true / n_grid if n_grid > 0 else float("nan")
        print(
            f"[stage2_frw_corridor_rung4] {fid}: "
            f"n_theta={n_true}, frac_of_grid={frac:.5f}"
        )

    overlaps = compute_overlap(fam_series, defs)

    out_dir = repo_root / "stage2" / "frw_corridor_analysis" / "outputs" / "tables"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_csv = out_dir / "stage2_frw_corridor_rung4_family_overlap_v1.csv"

    overlaps.to_csv(out_csv, index=False)
    print(
        f"[stage2_frw_corridor_rung4] Wrote {out_csv} "
        f"({out_csv.stat().st_size} bytes)"
    )
    ts = datetime.now(timezone.utc).isoformat()
    print(f"[stage2_frw_corridor_rung4] Timestamp UTC: {ts}")


if __name__ == "__main__":
    main()
