#!/usr/bin/env python3

"""
Stage 2 — Joint mech–FRW empirical anchor overview plot (A6, v1)

Produces a diagnostic scatter plot in (omega_lambda, age_Gyr) space, showing:
- all FRW grid points,
- FRW-viable points inside the toy corridor,
- the empirical anchor kernel (FRW_VIABLE ∧ IN_TOY_CORRIDOR ∧ IN_ANCHOR).

This is a Stage 2 visualization only (no new claims).
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

REPO_ROOT = Path(__file__).resolve().parents[3]

JOINT_GRID = REPO_ROOT / "stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv"
ANCHOR_MASK = REPO_ROOT / "stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_empirical_anchor_mask_v1.csv"

OUT_DIR = REPO_ROOT / "stage2/joint_mech_frw_analysis/outputs/figures"
OUT_FIG = OUT_DIR / "stage2_joint_mech_frw_anchor_overview_v1.png"


def detect_anchor_mask_column(df_anchor: pd.DataFrame) -> str:
    candidates = [
        "in_empirical_anchor",
        "in_anchor",
        "empirical_anchor_mask",
        "in_empirical_box",
        "in_data_box",
    ]
    for name in candidates:
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


def main() -> None:
    df_joint = pd.read_csv(JOINT_GRID)

    required = ["theta", "omega_lambda", "age_Gyr", "frw_viable", "in_toy_corridor"]
    for c in required:
        if c not in df_joint.columns:
            raise RuntimeError(f"Missing column in joint grid: {c}")

    df_anchor = pd.read_csv(ANCHOR_MASK)
    if "theta" not in df_anchor.columns:
        raise RuntimeError("Anchor mask table must contain a 'theta' column")

    anchor_mask_col = detect_anchor_mask_column(df_anchor)

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

    mask_viable_corridor = mask_viable & mask_corridor
    mask_kernel = mask_viable_corridor & mask_anchor

    n_total = len(df)
    n_viable_corridor = int(mask_viable_corridor.sum())
    n_kernel = int(mask_kernel.sum())

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(6, 5))

    # Background: all grid points
    ax.scatter(
        df["omega_lambda"],
        df["age_Gyr"],
        s=6,
        alpha=0.15,
        label="All FRW grid points",
    )

    # FRW-viable corridor points (excluding anchor kernel)
    if n_viable_corridor > 0:
        mask_viable_corridor_only = mask_viable_corridor & ~mask_kernel
        ax.scatter(
            df.loc[mask_viable_corridor_only, "omega_lambda"],
            df.loc[mask_viable_corridor_only, "age_Gyr"],
            s=10,
            alpha=0.5,
            label="FRW_viable ∧ corridor",
        )

    # Anchor kernel points
    if n_kernel > 0:
        ax.scatter(
            df.loc[mask_kernel, "omega_lambda"],
            df.loc[mask_kernel, "age_Gyr"],
            s=40,
            marker="*",
            label="Empirical anchor kernel",
        )

    ax.set_xlabel("omega_lambda (toy FRW)")
    ax.set_ylabel("age_Gyr (toy FRW)")
    ax.set_title("Stage 2: joint mech–FRW empirical anchor overview (v1)")

    ax.legend(loc="best")
    ax.grid(True)
    fig.tight_layout()

    fig.savefig(OUT_FIG, dpi=200)

    print("[stage2_anchor_plot_rung6]")
    print(f"  Total FRW grid rows: {n_total}")
    print(f"  FRW_viable ∧ corridor points: {n_viable_corridor}")
    print(f"  Empirical anchor kernel points: {n_kernel}")
    print(f"  Figure written to: {OUT_FIG}")


if __name__ == "__main__":
    main()
