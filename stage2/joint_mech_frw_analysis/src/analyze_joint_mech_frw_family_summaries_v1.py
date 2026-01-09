from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List

import numpy as np
import pandas as pd


TAG = "[stage2_joint_mech_frw_rung2]"


@dataclass
class FamilySummary:
    family_id: str
    n_theta: int
    frac_of_grid: float
    # we will dynamically attach mech stats as extra fields,
    # but for the CSV we just collect dicts from asdict().


def get_repo_root() -> Path:
    # Script lives at: repo_root/stage2/joint_mech_frw_analysis/src/...
    # parents[0] = src
    # parents[1] = joint_mech_frw_analysis
    # parents[2] = stage2
    # parents[3] = repo_root
    return Path(__file__).resolve().parents[3]


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
    print(f"{TAG} Loaded joint grid: {path} (rows={len(df)}, cols={len(df.columns)})")
    return df


def build_families(df: pd.DataFrame) -> Dict[str, pd.Series]:
    n = len(df)
    fam: Dict[str, pd.Series] = {}

    fam["ALL_GRID"] = pd.Series(True, index=df.index)

    if "frw_viable" in df.columns:
        fam["FRW_VIABLE"] = df["frw_viable"].astype(bool)
    if "lcdm_like" in df.columns:
        fam["LCDM_LIKE"] = df["lcdm_like"].astype(bool)
    if "in_toy_corridor" in df.columns:
        fam["TOY_CORRIDOR"] = df["in_toy_corridor"].astype(bool)
    if "shape_and_viable" in df.columns:
        fam["CORRIDOR_AND_VIABLE"] = df["shape_and_viable"].astype(bool)
    if "shape_and_lcdm" in df.columns:
        fam["CORRIDOR_AND_LCDM"] = df["shape_and_lcdm"].astype(bool)

    # Optional: FRW viable AND data_ok
    if "frw_viable" in df.columns and "frw_data_ok" in df.columns:
        fam["FRW_VIABLE_AND_DATA_OK"] = (
            df["frw_viable"].astype(bool) & df["frw_data_ok"].astype(bool)
        )

    print(f"{TAG} Defined {len(fam)} families on grid of size {n}")
    for fid, mask in fam.items():
        n_theta = int(mask.sum())
        frac = n_theta / float(n) if n > 0 else 0.0
        print(f"{TAG}   {fid}: n_theta={n_theta}, frac_of_grid={frac:.5f}")

    return fam


def summarize_family(
    df: pd.DataFrame,
    fam_id: str,
    mask: pd.Series,
    mech_cols: List[str],
) -> dict:
    n_total = len(df)
    n_theta = int(mask.sum())
    frac = n_theta / float(n_total) if n_total > 0 else 0.0

    base = FamilySummary(
        family_id=fam_id,
        n_theta=n_theta,
        frac_of_grid=frac,
    )
    out = asdict(base)

    if n_theta == 0:
        for col in mech_cols:
            out[f"{col}__mean"] = np.nan
            out[f"{col}__std"] = np.nan
            out[f"{col}__min"] = np.nan
            out[f"{col}__max"] = np.nan
        return out

    sub = df.loc[mask, mech_cols].copy()

    for col in mech_cols:
        if col not in sub.columns:
            out[f"{col}__mean"] = np.nan
            out[f"{col}__std"] = np.nan
            out[f"{col}__min"] = np.nan
            out[f"{col}__max"] = np.nan
            continue

        series = pd.to_numeric(sub[col], errors="coerce").dropna()
        if series.empty:
            out[f"{col}__mean"] = np.nan
            out[f"{col}__std"] = np.nan
            out[f"{col}__min"] = np.nan
            out[f"{col}__max"] = np.nan
            continue

        out[f"{col}__mean"] = float(series.mean())
        out[f"{col}__std"] = float(series.std(ddof=1)) if len(series) > 1 else 0.0
        out[f"{col}__min"] = float(series.min())
        out[f"{col}__max"] = float(series.max())

    return out


def main() -> None:
    repo_root = get_repo_root()
    print(f"{TAG} Repo root: {repo_root}")

    df = load_joint_grid(repo_root)

    required_cols = [
        "theta",
        "E_vac",
        "omega_lambda",
        "age_Gyr",
    ]
    for col in required_cols:
        if col not in df.columns:
            raise KeyError(f"{TAG} Missing required column in joint grid: {col}")

    mech_cols = [
        "mech_baseline_A0",
        "mech_baseline_A_floor",
        "mech_baseline_bound",
        "mech_binding_A0",
        "mech_binding_A",
        "mech_binding_bound",
    ]
    for col in mech_cols:
        if col not in df.columns:
            print(f"{TAG} WARNING: mech column {col} not found in joint grid")

    families = build_families(df)

    rows: List[dict] = []
    for fam_id, mask in families.items():
        row = summarize_family(df, fam_id, mask, mech_cols)
        rows.append(row)

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
        / "stage2_joint_mech_frw_rung2_family_summaries_v1.csv"
    )

    df_out = pd.DataFrame(rows)
    df_out.to_csv(out_csv, index=False)

    print(
        f"{TAG} Wrote family summaries: {out_csv} "
        f"({out_csv.stat().st_size} bytes; rows={len(df_out)})"
    )
    ts = datetime.now(timezone.utc).isoformat()
    print(f"{TAG} Timestamp UTC: {ts}")


if __name__ == "__main__":
    main()
