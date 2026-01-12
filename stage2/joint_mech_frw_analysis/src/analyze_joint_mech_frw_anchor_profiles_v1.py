#!/usr/bin/env python3

"""
Stage 2 — Joint mech–FRW empirical anchor profiles (v1, robust join)

On the joint theta grid, compute summary statistics for FRW + mechanism
columns across several sets:

- ALL_GRID
- FRW_VIABLE
- TOY_CORRIDOR
- EMPIRICAL_ANCHOR
- FRW_VIABLE_AND_ANCHOR
- CORRIDOR_AND_ANCHOR
- CORRIDOR_AND_VIABLE_AND_ANCHOR

This is a diagnostic rung only. No promotion or physical claims.
"""

from pathlib import Path
import pandas as pd

# Paths
HERE = Path(__file__).resolve()
REPO_ROOT = HERE.parents[3]

JOINT_TABLE = REPO_ROOT / "stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv"
ANCHOR_TABLE = REPO_ROOT / "stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_empirical_anchor_mask_v1.csv"
OUT_DIR = REPO_ROOT / "stage2/joint_mech_frw_analysis/outputs/tables"
OUT_TABLE = OUT_DIR / "stage2_joint_mech_frw_anchor_profiles_v1.csv"


def load_joint_grid() -> pd.DataFrame:
    if not JOINT_TABLE.is_file():
        raise FileNotFoundError(f"Joint theta grid not found: {JOINT_TABLE}")
    df = pd.read_csv(JOINT_TABLE)
    # We allow either 'theta_index' or 'theta' as join keys; checks happen later.
    return df


def load_anchor_mask() -> tuple[pd.DataFrame, str, str]:
    """
    Load the empirical anchor mask table and infer:
    - join_key: 'theta_index' if present, otherwise 'theta'
    - anchor_col: the boolean/integer anchor mask column
    """
    if not ANCHOR_TABLE.is_file():
        raise FileNotFoundError(f"Empirical anchor mask table not found: {ANCHOR_TABLE}")
    df = pd.read_csv(ANCHOR_TABLE)
    cols = list(df.columns)

    # Decide join key
    if "theta_index" in cols:
        join_key = "theta_index"
    elif "theta" in cols:
        join_key = "theta"
    else:
        raise RuntimeError(
            f"Anchor mask table must contain either 'theta_index' or 'theta' as a join key; got columns: {cols}"
        )

    # Choose anchor column (anything that's not the join key; prefer names containing 'anchor')
    candidate_cols = [c for c in cols if c != join_key]
    if not candidate_cols:
        raise RuntimeError(
            f"No candidate anchor-mask column found in anchor table (join key={join_key}, columns={cols})."
        )

    anchor_col = None
    for c in candidate_cols:
        if "anchor" in c.lower():
            anchor_col = c
            break
    if anchor_col is None:
        anchor_col = candidate_cols[0]

    return df[[join_key, anchor_col]].copy(), anchor_col, join_key


def get_corridor_col(df: pd.DataFrame) -> str:
    # Support both 'in_toy_corridor' and 'toy_corridor' naming.
    if "in_toy_corridor" in df.columns:
        return "in_toy_corridor"
    if "toy_corridor" in df.columns:
        return "toy_corridor"
    raise RuntimeError("No toy-corridor column found (expected 'in_toy_corridor' or 'toy_corridor').")


def summarize_sets(df: pd.DataFrame, anchor_col: str) -> pd.DataFrame:
    n_total = len(df)
    if n_total == 0:
        raise RuntimeError("Joint grid is empty.")

    corr_col = get_corridor_col(df)

    mask_all = pd.Series(True, index=df.index)
    mask_frw = df["frw_viable"].astype(bool)
    mask_corr = df[corr_col].astype(bool)
    mask_anchor = df[anchor_col].astype(bool)
    mask_kernel = mask_frw & mask_corr & mask_anchor

    set_masks = {
        "ALL_GRID": mask_all,
        "FRW_VIABLE": mask_frw,
        "TOY_CORRIDOR": mask_corr,
        "EMPIRICAL_ANCHOR": mask_anchor,
        "FRW_VIABLE_AND_ANCHOR": (mask_frw & mask_anchor),
        "CORRIDOR_AND_ANCHOR": (mask_corr & mask_anchor),
        "CORRIDOR_AND_VIABLE_AND_ANCHOR": mask_kernel,
    }

    # Numeric columns we care about; only keep those that actually exist.
    preferred_numeric = [
        "E_vac",
        "omega_lambda",
        "age_Gyr",
        "mech_baseline_A0",
        "mech_baseline_A_floor",
        "mech_baseline_bound",
        "mech_binding_A0",
        "mech_binding_A",
        "mech_binding_bound",
    ]
    numeric_cols = [c for c in preferred_numeric if c in df.columns]

    rows = []
    for name, m in set_masks.items():
        idx = df.index[m]
        n = len(idx)
        frac = n / n_total if n_total > 0 else 0.0

        row = {
            "set": name,
            "n_theta": n,
            "frac_of_grid": frac,
        }

        if n > 0 and numeric_cols:
            sub = df.loc[idx, numeric_cols]
            for col in numeric_cols:
                s = sub[col]
                row[f"{col}__mean"] = float(s.mean())
                row[f"{col}__std"] = float(s.std(ddof=0))
                row[f"{col}__min"] = float(s.min())
                row[f"{col}__max"] = float(s.max())
        else:
            for col in numeric_cols:
                row[f"{col}__mean"] = float("nan")
                row[f"{col}__std"] = float("nan")
                row[f"{col}__min"] = float("nan")
                row[f"{col}__max"] = float("nan")

        rows.append(row)

    return pd.DataFrame(rows)


def main() -> None:
    df_joint = load_joint_grid()
    df_anchor, anchor_col, join_key = load_anchor_mask()

    if join_key not in df_joint.columns:
        raise RuntimeError(
            f"Join key '{join_key}' found in anchor table is not present in joint grid columns: {list(df_joint.columns)}"
        )

    # Join anchor mask onto joint grid.
    df = df_joint.merge(df_anchor, on=join_key, how="left")
    # Treat missing as False.
    df[anchor_col] = df[anchor_col].fillna(False).astype(bool)

    df_out = summarize_sets(df, anchor_col)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    df_out.to_csv(OUT_TABLE, index=False)

    print("[stage2_anchor_profiles_rungA6]")
    print(f"  Joint grid rows: {len(df)}")
    print(f"  Anchor column: {anchor_col}")
    print(f"  Join key: {join_key}")
    print(f"  Output written: {OUT_TABLE}")
    for _, r in df_out.iterrows():
        print(
            f"  {r['set']}: n={int(r['n_theta'])}, "
            f"frac={r['frac_of_grid']:.6f}"
        )


if __name__ == "__main__":
    main()
