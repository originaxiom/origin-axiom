#!/usr/bin/env python3

"""
Stage 2 — Joint mech–FRW empirical anchor sensitivity (v1)

Starting from:
- the joint theta grid
- the existing empirical anchor mask

we:

1. Infer a baseline bounding box in (omega_lambda, age_Gyr) that contains
   all currently anchored points.

2. Define scaled boxes by multiplying the half-widths by factors in
   SCALE_FACTORS.

3. For each scale, count:
   - how many theta lie in the scaled box,
   - how many are FRW_VIABLE,
   - how many are in the TOY_CORRIDOR,
   - how many are in FRW_VIABLE ∧ TOY_CORRIDOR.

This is a pure diagnostic rung (Stage 2). No claims or promotions.
"""

from pathlib import Path
import math
import pandas as pd

HERE = Path(__file__).resolve()
REPO_ROOT = HERE.parents[3]

JOINT_TABLE = REPO_ROOT / "stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv"
ANCHOR_TABLE = REPO_ROOT / "stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_empirical_anchor_mask_v1.csv"
OUT_DIR = REPO_ROOT / "stage2/joint_mech_frw_analysis/outputs/tables"
OUT_TABLE = OUT_DIR / "stage2_joint_mech_frw_anchor_sensitivity_v1.csv"

SCALE_FACTORS = [0.5, 1.0, 1.5]


def get_corridor_col(df: pd.DataFrame) -> str:
    if "in_toy_corridor" in df.columns:
        return "in_toy_corridor"
    if "toy_corridor" in df.columns:
        return "toy_corridor"
    raise RuntimeError("No toy corridor column found (expected 'in_toy_corridor' or 'toy_corridor').")


def load_joint_grid() -> pd.DataFrame:
    if not JOINT_TABLE.is_file():
        raise FileNotFoundError(f"Joint theta grid not found: {JOINT_TABLE}")
    df = pd.read_csv(JOINT_TABLE)
    for c in ["theta", "omega_lambda", "age_Gyr", "frw_viable"]:
        if c not in df.columns:
            raise RuntimeError(f"Missing required column '{c}' in joint grid.")
    return df


def load_anchor_mask() -> tuple[pd.DataFrame, str, str]:
    if not ANCHOR_TABLE.is_file():
        raise FileNotFoundError(f"Anchor mask table not found: {ANCHOR_TABLE}")
    df = pd.read_csv(ANCHOR_TABLE)
    cols = list(df.columns)

    # Decide join key
    if "theta" in cols:
        join_key = "theta"
    elif "theta_index" in cols:
        join_key = "theta_index"
    else:
        raise RuntimeError(
            f"Anchor mask table must contain 'theta' or 'theta_index' as join key; got columns: {cols}"
        )

    # Choose anchor column
    candidate_cols = [c for c in cols if c != join_key]
    if not candidate_cols:
        raise RuntimeError(
            f"No candidate anchor column found in anchor table (join key={join_key}, columns={cols})."
        )

    anchor_col = None
    for c in candidate_cols:
        if "anchor" in c.lower():
            anchor_col = c
            break
    if anchor_col is None:
        anchor_col = candidate_cols[0]

    return df[[join_key, anchor_col]].copy(), anchor_col, join_key


def infer_baseline_box(df: pd.DataFrame, anchor_col: str) -> tuple[float, float, float, float]:
    mask_anchor = df[anchor_col].astype(bool)
    if not mask_anchor.any():
        raise RuntimeError("No rows are marked as in the empirical anchor box.")

    sub = df.loc[mask_anchor, ["omega_lambda", "age_Gyr"]]
    omega_min = float(sub["omega_lambda"].min())
    omega_max = float(sub["omega_lambda"].max())
    age_min = float(sub["age_Gyr"].min())
    age_max = float(sub["age_Gyr"].max())

    omega_center = 0.5 * (omega_min + omega_max)
    age_center = 0.5 * (age_min + age_max)

    omega_half = 0.5 * (omega_max - omega_min)
    age_half = 0.5 * (age_max - age_min)

    # Avoid pathological zero-width boxes
    if omega_half == 0.0:
        omega_half = 1e-6
    if age_half == 0.0:
        age_half = 1e-6

    return omega_center, omega_half, age_center, age_half


def analyze_sensitivity(df: pd.DataFrame, anchor_col: str) -> pd.DataFrame:
    n_total = len(df)
    corridor_col = get_corridor_col(df)

    omega_center, omega_half_base, age_center, age_half_base = infer_baseline_box(df, anchor_col)

    rows = []
    for scale in SCALE_FACTORS:
        omega_half = omega_half_base * scale
        age_half = age_half_base * scale

        in_box = (
            (df["omega_lambda"].between(omega_center - omega_half, omega_center + omega_half))
            &
            (df["age_Gyr"].between(age_center - age_half, age_center + age_half))
        )

        mask_frw = df["frw_viable"].astype(bool)
        mask_corr = df[corridor_col].astype(bool)

        mask_box = in_box
        mask_box_frw = in_box & mask_frw
        mask_box_corr = in_box & mask_corr
        mask_box_corr_frw = in_box & mask_frw & mask_corr

        def frac(count: int) -> float:
            return count / n_total if n_total > 0 else math.nan

        n_box = int(mask_box.sum())
        n_frw = int(mask_box_frw.sum())
        n_corr = int(mask_box_corr.sum())
        n_corr_frw = int(mask_box_corr_frw.sum())

        rows.append(
            {
                "scale_factor": scale,
                "omega_center": omega_center,
                "age_center": age_center,
                "omega_half_base": omega_half_base,
                "age_half_base": age_half_base,
                "omega_half_scaled": omega_half,
                "age_half_scaled": age_half,
                "n_in_box": n_box,
                "frac_in_box": frac(n_box),
                "n_in_box_and_frw_viable": n_frw,
                "frac_in_box_and_frw_viable": frac(n_frw),
                "n_in_box_and_corridor": n_corr,
                "frac_in_box_and_corridor": frac(n_corr),
                "n_in_box_and_corridor_and_frw": n_corr_frw,
                "frac_in_box_and_corridor_and_frw": frac(n_corr_frw),
            }
        )

    return pd.DataFrame(rows)


def main() -> None:
    df_joint = load_joint_grid()
    df_anchor, anchor_col, join_key = load_anchor_mask()

    if join_key not in df_joint.columns:
        raise RuntimeError(
            f"Join key '{join_key}' from anchor table not present in joint grid columns: {list(df_joint.columns)}"
        )

    df = df_joint.merge(df_anchor, on=join_key, how="left")
    df[anchor_col] = df[anchor_col].fillna(False).astype(bool)

    df_out = analyze_sensitivity(df, anchor_col)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    df_out.to_csv(OUT_TABLE, index=False)

    print("[stage2_anchor_sensitivity_rungA7]")
    print(f"  Joint grid rows: {len(df)}")
    print(f"  Anchor column: {anchor_col}")
    print(f"  Join key: {join_key}")
    print(f"  Baseline half-widths and scaled counts written to: {OUT_TABLE}")
    for _, r in df_out.iterrows():
        print(
            f"  scale={r['scale_factor']:.2f} | "
            f"n_in_box={int(r['n_in_box'])}, "
            f"n_box∧FRW={int(r['n_in_box_and_frw_viable'])}, "
            f"n_box∧corr={int(r['n_in_box_and_corridor'])}, "
            f"n_box∧corr∧FRW={int(r['n_in_box_and_corridor_and_frw'])}"
        )


if __name__ == "__main__":
    main()
