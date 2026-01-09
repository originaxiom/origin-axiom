from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Tuple

import numpy as np
import pandas as pd


TAG = "[stage2_joint_mech_frw_rung1]"


@dataclass
class TableMeta:
    rel_path: str
    n_rows: int
    n_cols: int


def find_repo_root(start: Optional[Path] = None) -> Path:
    here = (start or Path(__file__).resolve()).absolute()
    for parent in [here] + list(here.parents):
        if (parent / ".git").is_dir():
            return parent
    raise RuntimeError(f"{TAG} Could not find repo root (.git)")


def load_csv(repo_root: Path, rel_path: str) -> Tuple[pd.DataFrame, TableMeta]:
    path = repo_root / rel_path
    if not path.is_file():
        raise FileNotFoundError(f"{TAG} Missing expected CSV: {rel_path}")
    df = pd.read_csv(path)
    meta = TableMeta(
        rel_path=rel_path,
        n_rows=len(df),
        n_cols=df.shape[1],
    )
    print(
        f"{TAG} Loaded {rel_path} "
        f"(n_rows={meta.n_rows}, n_cols={meta.n_cols})"
    )
    return df, meta


def assert_theta_align(
    base: pd.DataFrame,
    other: pd.DataFrame,
    base_name: str,
    other_name: str,
    tol: float = 1e-8,
) -> None:
    if "theta" not in base.columns:
        raise ValueError(f"{TAG} {base_name} has no 'theta' column")
    if "theta" not in other.columns:
        raise ValueError(f"{TAG} {other_name} has no 'theta' column")

    if len(base) != len(other):
        raise ValueError(
            f"{TAG} Theta mismatch: {base_name} has {len(base)} rows, "
            f"{other_name} has {len(other)} rows"
        )

    theta_base = np.asarray(base["theta"].values, dtype=float)
    theta_other = np.asarray(other["theta"].values, dtype=float)

    if not np.allclose(theta_base, theta_other, atol=tol, rtol=0.0):
        max_diff = float(np.max(np.abs(theta_base - theta_other)))
        raise ValueError(
            f"{TAG} Theta values differ between {base_name} and {other_name} "
            f"(max |Δθ| ≈ {max_diff:.3e})"
        )

    print(
        f"{TAG} Theta alignment OK between {base_name} and {other_name} "
        f"(n={len(theta_base)}, tol={tol:g})"
    )


def main() -> None:
    repo_root = find_repo_root()
    print(f"{TAG} Repo root: {repo_root}")

    # -----------------------------
    # 1. Load FRW shape probe mask
    # -----------------------------
    frw_shape_rel = "phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv"
    frw_shape_df, frw_shape_meta = load_csv(repo_root, frw_shape_rel)

    if "theta" not in frw_shape_df.columns:
        raise ValueError(f"{TAG} {frw_shape_rel} has no 'theta' column")

    n_grid = len(frw_shape_df)
    print(f"{TAG} Nominal theta grid size: {n_grid}")

    # Standardize base grid: add an explicit index column
    df_joint = frw_shape_df.copy()
    if "theta_index" not in df_joint.columns:
        df_joint.insert(0, "theta_index", np.arange(n_grid, dtype=int))

    # --------------------------------------
    # 2. Optionally attach data_ok and checks
    # --------------------------------------
    frw_data_rel = "phase4/outputs/tables/phase4_F1_frw_data_probe_mask.csv"
    try:
        frw_data_df, _ = load_csv(repo_root, frw_data_rel)
        assert_theta_align(
            frw_shape_df,
            frw_data_df,
            base_name="frw_shape_probe_mask",
            other_name="frw_data_probe_mask",
        )
        # We expect a boolean-like 'data_ok' column there
        if "data_ok" in frw_data_df.columns:
            df_joint["frw_data_ok"] = frw_data_df["data_ok"].astype(bool)
            print(f"{TAG} Attached frw_data_ok from {frw_data_rel}")
        else:
            print(
                f"{TAG} WARNING: {frw_data_rel} has no 'data_ok' column; "
                "skipping attachment"
            )
    except FileNotFoundError as e:
        print(f"{TAG} WARNING: {e}; continuing without data_ok")

    # Light consistency checks with viability / LCDM masks
    frw_viability_rel = "phase4/outputs/tables/phase4_F1_frw_viability_mask.csv"
    frw_lcdm_rel = "phase4/outputs/tables/phase4_F1_frw_lcdm_probe_mask.csv"

    for rel in [frw_viability_rel, frw_lcdm_rel]:
        try:
            df_tmp, _ = load_csv(repo_root, rel)
            assert_theta_align(
                frw_shape_df,
                df_tmp,
                base_name="frw_shape_probe_mask",
                other_name=rel,
            )
        except FileNotFoundError as e:
            print(f"{TAG} WARNING: {e}; skipping alignment check for {rel}")

    # ------------------------------------------------
    # 3. Attach Phase 3 per-theta mechanism quantities
    # ------------------------------------------------
    # We treat these as pure per-theta tables, aligned to the same grid.
    phase3_tables = [
        ("phase3/outputs/tables/mech_baseline_scan.csv", "mech_baseline_"),
        ("phase3/outputs/tables/mech_binding_certificate.csv", "mech_binding_"),
    ]

    for rel, prefix in phase3_tables:
        try:
            df_p3, meta = load_csv(repo_root, rel)
        except FileNotFoundError as e:
            print(f"{TAG} WARNING: {e}; skipping {rel}")
            continue

        assert_theta_align(
            frw_shape_df,
            df_p3,
            base_name="frw_shape_probe_mask",
            other_name=rel,
        )

        # Attach all non-theta columns with a clear prefix
        for col in df_p3.columns:
            if col == "theta":
                continue
            new_col = f"{prefix}{col}"
            if new_col in df_joint.columns:
                print(
                    f"{TAG} WARNING: column {new_col} already in joint grid; "
                    f"overwriting with values from {rel}"
                )
            df_joint[new_col] = df_p3[col].values

        print(
            f"{TAG} Attached {meta.n_cols - 1} columns from {rel} "
            f"with prefix '{prefix}'"
        )

    # ------------------------------------------------
    # 4. Final bookkeeping and write output
    # ------------------------------------------------
    out_dir = (
        repo_root
        / "stage2"
        / "joint_mech_frw_analysis"
        / "outputs"
        / "tables"
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    out_csv = out_dir / "stage2_joint_theta_grid_v1.csv"

    df_joint.to_csv(out_csv, index=False)
    print(
        f"{TAG} Wrote joint theta grid: {out_csv} "
        f"(n_rows={len(df_joint)}, n_cols={df_joint.shape[1]}, "
        f"size_bytes={out_csv.stat().st_size})"
    )

    # Brief summary of key columns
    key_cols = [
        c
        for c in df_joint.columns
        if c in {
            "theta_index",
            "theta",
            "E_vac",
            "omega_lambda",
            "age_Gyr",
            "frw_viable",
            "lcdm_like",
            "in_toy_corridor",
            "shape_and_viable",
            "shape_and_lcdm",
            "frw_data_ok",
        }
        or c.startswith("mech_baseline_")
        or c.startswith("mech_binding_")
    ]
    print(f"{TAG} Key columns in joint grid:")
    for c in key_cols:
        print(f"{TAG}   - {c}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{TAG} ERROR: {e}", file=sys.stderr)
        raise
