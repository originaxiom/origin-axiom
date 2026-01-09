from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import List

import numpy as np
import pandas as pd


TAG = "[stage2_joint_mech_frw_rung3]"


@dataclass
class CorrelationRow:
    frw_scalar: str
    mech_var: str
    pearson_r: float
    covariance: float
    n_points: int


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


def compute_correlations(
    df: pd.DataFrame,
    frw_scalars: List[str],
    mech_vars: List[str],
) -> List[CorrelationRow]:
    rows: List[CorrelationRow] = []

    for fs in frw_scalars:
        if fs not in df.columns:
            print(f"{TAG} WARNING: FRW scalar {fs} not found in joint grid; skipping")
            continue

        x_raw = pd.to_numeric(df[fs], errors="coerce")

        for mv in mech_vars:
            if mv not in df.columns:
                print(f"{TAG} WARNING: mech var {mv} not found in joint grid; skipping")
                continue

            y_raw = pd.to_numeric(df[mv], errors="coerce")

            # Drop rows where either side is NaN
            mask = x_raw.notna() & y_raw.notna()
            x = x_raw[mask]
            y = y_raw[mask]
            n = int(mask.sum())

            if n < 2:
                print(
                    f"{TAG} WARNING: not enough points for correlation "
                    f"({fs} vs {mv}); n={n}"
                )
                rows.append(
                    CorrelationRow(
                        frw_scalar=fs,
                        mech_var=mv,
                        pearson_r=float("nan"),
                        covariance=float("nan"),
                        n_points=n,
                    )
                )
                continue

            # Pearson correlation
            pearson_r = float(x.corr(y))

            # Sample covariance
            covariance = float(np.cov(x.to_numpy(), y.to_numpy(), ddof=1)[0, 1])

            rows.append(
                CorrelationRow(
                    frw_scalar=fs,
                    mech_var=mv,
                    pearson_r=pearson_r,
                    covariance=covariance,
                    n_points=n,
                )
            )

            print(
                f"{TAG} {fs} vs {mv}: n={n}, "
                f"pearson_r={pearson_r:.6f}, cov={covariance:.6e}"
            )

    return rows


def main() -> None:
    repo_root = get_repo_root()
    print(f"{TAG} Repo root: {repo_root}")

    df = load_joint_grid(repo_root)

    frw_scalars = ["E_vac", "omega_lambda", "age_Gyr"]
    mech_vars = [
        "mech_baseline_A0",
        "mech_baseline_A_floor",
        "mech_baseline_bound",
        "mech_binding_A0",
        "mech_binding_A",
        "mech_binding_bound",
    ]

    for col in frw_scalars + mech_vars:
        if col not in df.columns:
            print(f"{TAG} WARNING: column {col} missing from joint grid")

    rows = compute_correlations(df, frw_scalars, mech_vars)

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
        / "stage2_joint_mech_frw_rung3_correlations_v1.csv"
    )

    df_out = pd.DataFrame([asdict(r) for r in rows])
    df_out.to_csv(out_csv, index=False)

    print(
        f"{TAG} Wrote correlations: {out_csv} "
        f"({out_csv.stat().st_size} bytes; rows={len(df_out)})"
    )
    ts = datetime.now(timezone.utc).isoformat()
    print(f"{TAG} Timestamp UTC: {ts}")


if __name__ == "__main__":
    main()
