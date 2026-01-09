#!/usr/bin/env python3
from __future__ import annotations

import numpy as np
import pandas as pd

from pathlib import Path
from datetime import datetime, timezone
from typing import Dict

TAG = "[stage2_joint_mech_frw_rung4]"


def find_repo_root(start: Path | None = None) -> Path:
    """
    Walk upwards until we find a .git directory.
    Assumes we are somewhere inside the repo.
    """
    if start is None:
        start = Path.cwd().resolve()

    for path in [start, *start.parents]:
        if (path / ".git").is_dir():
            return path

    raise RuntimeError(f"{TAG} Could not find repo root starting from {start}")


def load_joint_grid(repo_root: Path) -> pd.DataFrame:
    path = (
        repo_root
        / "stage2"
        / "joint_mech_frw_analysis"
        / "outputs"
        / "tables"
        / "stage2_joint_theta_grid_v1.csv"
    )
    if not path.exists():
        raise FileNotFoundError(f"{TAG} Joint grid not found at {path}")

    df = pd.read_csv(path)
    print(
        f"{TAG} Loaded joint grid: {path} "
        f"(rows={len(df)}, cols={df.shape[1]})"
    )
    return df


def define_families(df: pd.DataFrame) -> Dict[str, np.ndarray]:
    """
    Rebuild the FRW families on the joint grid, matching rung2.
    """
    def as_bool(col: str) -> np.ndarray:
        if col not in df.columns:
            raise KeyError(f"{TAG} Missing column {col!r} in joint grid")
        return df[col].astype(bool).to_numpy()

    n = len(df)
    families: Dict[str, np.ndarray] = {}

    frw_viable = as_bool("frw_viable")
    lcdm_like = as_bool("lcdm_like")
    corridor = as_bool("in_toy_corridor")
    data_ok = as_bool("frw_data_ok")

    families["ALL_GRID"] = np.ones(n, dtype=bool)
    families["FRW_VIABLE"] = frw_viable
    families["LCDM_LIKE"] = lcdm_like
    families["TOY_CORRIDOR"] = corridor
    families["CORRIDOR_AND_VIABLE"] = corridor & frw_viable
    families["CORRIDOR_AND_LCDM"] = corridor & lcdm_like
    families["FRW_VIABLE_AND_DATA_OK"] = frw_viable & data_ok

    for fid, mask in families.items():
        n_theta = int(mask.sum())
        frac = n_theta / float(n) if n else 0.0
        print(
            f"{TAG} {fid}: n_theta={n_theta}, "
            f"frac_of_grid={frac:.5f}"
        )

    return families


def pearson_and_cov(x: np.ndarray, y: np.ndarray) -> tuple[float, float]:
    """
    Compute Pearson r and covariance with basic safety checks.
    Returns (nan, nan) if variance is zero or too few points.
    """
    if x.size < 2 or y.size < 2:
        return float("nan"), float("nan")

    x = x.astype(float)
    y = y.astype(float)

    if np.allclose(x, x[0]) or np.allclose(y, y[0]):
        return float("nan"), float("nan")

    r = float(np.corrcoef(x, y)[0, 1])
    cov = float(np.cov(x, y, ddof=1)[0, 1])
    return r, cov


def main() -> None:
    repo_root = find_repo_root()
    print(f"{TAG} Repo root: {repo_root}")

    df = load_joint_grid(repo_root)
    n_grid = len(df)

    families = define_families(df)

    frw_cols = ["E_vac", "omega_lambda", "age_Gyr"]
    mech_cols = [
        "mech_baseline_A0",
        "mech_baseline_A_floor",
        "mech_baseline_bound",
        "mech_binding_A0",
        "mech_binding_A",
        "mech_binding_bound",
    ]

    missing = [c for c in frw_cols + mech_cols if c not in df.columns]
    if missing:
        raise KeyError(f"{TAG} Missing columns in joint grid: {missing}")

    rows = []

    for fid, mask in families.items():
        idx = np.nonzero(mask)[0]
        n_theta = int(idx.size)
        if n_theta == 0:
            print(f"{TAG} {fid}: empty family, skipping correlations")
            continue

        frac_of_grid = n_theta / float(n_grid) if n_grid else 0.0

        for frw_col in frw_cols:
            x = df.loc[idx, frw_col].to_numpy()
            for mech_col in mech_cols:
                y = df.loc[idx, mech_col].to_numpy()
                r, cov = pearson_and_cov(x, y)

                rows.append(
                    {
                        "family_id": fid,
                        "frw_col": frw_col,
                        "mech_col": mech_col,
                        "n_theta": n_theta,
                        "frac_of_grid": frac_of_grid,
                        "pearson_r": r,
                        "covariance": cov,
                    }
                )

                print(
                    f"{TAG} {fid} | {frw_col} vs {mech_col}: "
                    f"n={n_theta}, frac_of_grid={frac_of_grid:.5f}, "
                    f"pearson_r={r:.6f}, cov={cov:.3e}"
                )

    out_dir = (
        repo_root
        / "stage2"
        / "joint_mech_frw_analysis"
        / "outputs"
        / "tables"
    )
    out_dir.mkdir(parents=True, exist_ok=True)

    out_csv = (
        out_dir
        / "stage2_joint_mech_frw_rung4_family_correlations_v1.csv"
    )
    df_out = pd.DataFrame(rows)
    df_out.to_csv(out_csv, index=False)

    print(
        f"{TAG} Wrote family correlations: {out_csv} "
        f"({out_csv.stat().st_size} bytes; rows={len(df_out)})"
    )
    ts = datetime.now(timezone.utc).isoformat()
    print(f"{TAG} Timestamp UTC: {ts}")


if __name__ == "__main__":
    main()
