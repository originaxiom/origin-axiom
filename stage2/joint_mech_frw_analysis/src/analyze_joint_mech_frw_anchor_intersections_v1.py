#!/usr/bin/env python3

"""
Stage 2 — Joint mech–FRW empirical anchor intersections (v1)

Computes geometric intersections between:
- FRW viability,
- toy corridor (in_toy_corridor),
- and the empirical anchor box.

Diagnostic only. No promotion or physical claims.
"""

from pathlib import Path
import pandas as pd

# Resolve repo root (origin-axiom/)
REPO_ROOT = Path(__file__).resolve().parents[3]

JOINT_GRID = REPO_ROOT / "stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv"
ANCHOR_MASK = REPO_ROOT / "stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_empirical_anchor_mask_v1.csv"

OUT_DIR = REPO_ROOT / "stage2/joint_mech_frw_analysis/outputs/tables"
OUT_TABLE = OUT_DIR / "stage2_joint_mech_frw_anchor_intersections_v1.csv"


def detect_anchor_mask_column(df_anchor: pd.DataFrame) -> str:
    """
    Try to find the empirical-anchor mask column in df_anchor.

    Priority:
    1. Known names we are likely to have used.
    2. Any boolean / {0,1}-like column != 'theta'.
    """
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

    # Heuristic: boolean-like columns other than 'theta'
    bool_like = []
    for c in df_anchor.columns:
        if c == "theta":
            continue
        series = df_anchor[c].dropna()
        if series.empty:
            continue
        # treat as mask if values are all in {0,1,True,False}
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


def main() -> None:
    # Load joint grid (mechanism + FRW + corridor flags)
    df_joint = pd.read_csv(JOINT_GRID)

    required_joint = ["theta", "in_toy_corridor", "frw_viable"]
    for c in required_joint:
        if c not in df_joint.columns:
            raise RuntimeError(f"Missing column in joint grid: {c}")

    # Load empirical anchor mask table
    df_anchor = pd.read_csv(ANCHOR_MASK)

    if "theta" not in df_anchor.columns:
        raise RuntimeError("Anchor mask table must contain a 'theta' column")

    anchor_mask_col = detect_anchor_mask_column(df_anchor)

    # Merge only theta + mask to avoid clobbering FRW scalars
    df = df_joint.merge(
        df_anchor[["theta", anchor_mask_col]],
        on="theta",
        how="left",
        validate="one_to_one",
    )

    if anchor_mask_col not in df.columns:
        cols = ", ".join(df.columns)
        raise RuntimeError(
            f"After merge, anchor mask column '{anchor_mask_col}' is missing. "
            f"Available columns: {cols}"
        )

    # Missing mask entries are treated as False
    df[anchor_mask_col] = df[anchor_mask_col].fillna(False)

    # Boolean masks
    mask_anchor = df[anchor_mask_col].astype(bool)
    mask_corridor = df["in_toy_corridor"].astype(bool)
    mask_viable = df["frw_viable"].astype(bool)

    n_total = len(df)

    rows = []

    def add_row(name: str, idx) -> None:
        n = int(len(idx))
        frac = float(n / n_total) if n_total > 0 else 0.0
        rows.append(
            {
                "set": name,
                "n_theta": n,
                "frac_of_grid": frac,
            }
        )

    # Basic sets
    add_row("ALL_GRID", df.index)
    add_row("FRW_VIABLE", df.index[mask_viable])
    add_row("TOY_CORRIDOR", df.index[mask_corridor])
    add_row("EMPIRICAL_ANCHOR", df.index[mask_anchor])

    # Intersections
    add_row("FRW_VIABLE_AND_ANCHOR", df.index[mask_viable & mask_anchor])
    add_row("CORRIDOR_AND_ANCHOR", df.index[mask_corridor & mask_anchor])
    add_row(
        "CORRIDOR_AND_VIABLE_AND_ANCHOR",
        df.index[mask_corridor & mask_viable & mask_anchor],
    )

    df_out = pd.DataFrame(rows)

    # Write
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    df_out.to_csv(OUT_TABLE, index=False)

    print("[stage2_anchor_intersections_rung4]")
    print(f"  Joint grid rows: {n_total}")
    print(f"  Output written: {OUT_TABLE}")
    for _, r in df_out.iterrows():
        print(f"  {r['set']}: n={int(r['n_theta'])}, frac={r['frac_of_grid']:.6f}")


if __name__ == "__main__":
    main()
