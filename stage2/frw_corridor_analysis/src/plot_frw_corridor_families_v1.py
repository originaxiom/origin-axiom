#!/usr/bin/env python3
"""
Stage 2 – FRW corridor analysis, Rung 5:
Diagnostic plots for FRW families in theta and (theta, omega_lambda) space.

Inputs:
  - phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv

Outputs:
  - stage2/frw_corridor_analysis/outputs/figures/
      stage2_frw_corridor_family_theta_hist_v1.pdf
      stage2_frw_corridor_family_omega_lambda_scatter_v1.pdf
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List

import matplotlib.pyplot as plt
import pandas as pd


@dataclass(frozen=True)
class FamilyDef:
    family_id: str
    column: str
    description: str


FAMILIES: List[FamilyDef] = [
    FamilyDef(
        family_id="F1_FRW_VIABLE",
        column="frw_viable",
        description="FRW viable in Phase 4 viability mask",
    ),
    FamilyDef(
        family_id="F2_LCDM_LIKE",
        column="lcdm_like",
        description="LCDM-like FRW in Phase 4 LCDM probe",
    ),
    FamilyDef(
        family_id="F3_TOY_CORRIDOR",
        column="in_toy_corridor",
        description="Inside toy FRW corridor",
    ),
    FamilyDef(
        family_id="F4_CORRIDOR_AND_VIABLE",
        column="shape_and_viable",
        description="Toy corridor AND FRW viable",
    ),
    FamilyDef(
        family_id="F5_CORRIDOR_AND_LCDM",
        column="shape_and_lcdm",
        description="Toy corridor AND LCDM-like",
    ),
]


def find_repo_root(start: Path | None = None) -> Path:
    """Walk upwards until we find a .git directory."""
    if start is None:
        start = Path(__file__).resolve()
    p = start
    for _ in range(10):
        if (p / ".git").is_dir():
            return p
        if p.parent == p:
            break
        p = p.parent
    raise RuntimeError("Could not find repo root from path: {}".format(start))


def load_shape_probe_mask(repo_root: Path) -> pd.DataFrame:
    path = (
        repo_root
        / "phase4"
        / "outputs"
        / "tables"
        / "phase4_F1_frw_shape_probe_mask.csv"
    )
    if not path.is_file():
        raise FileNotFoundError(f"Missing input CSV: {path}")
    df = pd.read_csv(path)
    print(f"[stage2_frw_corridor_rung5] Loaded shape_probe_mask: {path}")
    print(f"[stage2_frw_corridor_rung5] df shape: {df.shape}")
    return df


def compute_family_masks(df: pd.DataFrame) -> Dict[str, pd.Series]:
    masks: Dict[str, pd.Series] = {}
    for fam in FAMILIES:
        if fam.column not in df.columns:
            raise KeyError(
                f"Expected family column '{fam.column}' "
                f"for {fam.family_id} not found in dataframe"
            )
        col = df[fam.column]
        mask = col.astype(bool)
        n_true = int(mask.sum())
        frac = n_true / len(df) if len(df) else 0.0
        print(
            f"[stage2_frw_corridor_rung5] {fam.family_id}: "
            f"n_theta={n_true}, frac_of_grid={frac:.5f}"
        )
        masks[fam.family_id] = mask
    return masks


def make_theta_hist(
    df: pd.DataFrame,
    masks: Dict[str, pd.Series],
    out_path: Path,
) -> None:
    theta = df["theta"]

    plt.figure(figsize=(8, 5))
    for fam in FAMILIES:
        mask = masks[fam.family_id]
        if mask.any():
            plt.hist(
                theta[mask],
                bins=40,
                histtype="step",
                label=fam.family_id,
                density=True,
            )

    plt.xlabel("theta")
    plt.ylabel("density")
    plt.title("Stage 2 – FRW families: theta distribution")
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()
    print(f"[stage2_frw_corridor_rung5] Wrote theta hist: {out_path}")


def make_omega_lambda_scatter(
    df: pd.DataFrame,
    masks: Dict[str, pd.Series],
    out_path: Path,
) -> None:
    if "omega_lambda" not in df.columns:
        raise KeyError("Expected column 'omega_lambda' in shape_probe_mask")

    theta = df["theta"]
    omega_lambda = df["omega_lambda"]

    plt.figure(figsize=(8, 5))
    for fam in FAMILIES:
        mask = masks[fam.family_id]
        if not mask.any():
            continue
        plt.scatter(
            theta[mask],
            omega_lambda[mask],
            s=6,
            alpha=0.5,
            label=fam.family_id,
        )

    plt.xlabel("theta")
    plt.ylabel("omega_lambda")
    plt.title("Stage 2 – FRW families in (theta, omega_lambda)")
    plt.legend(markerscale=2.0)
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()
    print(f"[stage2_frw_corridor_rung5] Wrote omega_lambda scatter: {out_path}")


def main() -> None:
    repo_root = find_repo_root()
    print(f"[stage2_frw_corridor_rung5] Repo root: {repo_root}")

    df = load_shape_probe_mask(repo_root)
    masks = compute_family_masks(df)

    out_fig_dir = (
        repo_root
        / "stage2"
        / "frw_corridor_analysis"
        / "outputs"
        / "figures"
    )
    out_fig_dir.mkdir(parents=True, exist_ok=True)

    theta_hist_path = (
        out_fig_dir
        / "stage2_frw_corridor_family_theta_hist_v1.pdf"
    )
    omega_lambda_scatter_path = (
        out_fig_dir
        / "stage2_frw_corridor_family_omega_lambda_scatter_v1.pdf"
    )

    make_theta_hist(df, masks, theta_hist_path)
    make_omega_lambda_scatter(df, masks, omega_lambda_scatter_path)

    ts = datetime.now(timezone.utc).isoformat()
    print(f"[stage2_frw_corridor_rung5] Timestamp UTC: {ts}")


if __name__ == "__main__":
    main()
