"""
Stage 2 / obstruction: Planck-like FRW shell vs mechanism amplitudes and floor (v1).

This helper starts from the Stage 2 obstruction kernel with mechanism amplitudes and
defines a simple "Planck-near" FRW shell around a Planck-like age / omega_Lambda
band. It then summarises how many kernel points fall in that shell, how they look
in the six Phase 3 amplitudes, and how many also satisfy the non-cancellation
floor used in earlier diagnostics.

Inputs
------

- stage2/obstruction_tests/outputs/tables/stage2_obstruction_kernel_with_mech_v1.csv

  Expected columns include at least:

    - theta
    - age_Gyr
    - omega_lambda
    - in_pre_data_kernel
    - mech_baseline_A0
    - mech_baseline_A_floor
    - mech_baseline_bound
    - mech_binding_A0
    - mech_binding_A
    - mech_binding_bound

No other Stage 2 tables are required; this helper is self-contained.

Construction
------------

We take as a starting point the Planck-like late-time box used in
`apply_planck_like_frw_corridor_v1.py` and `analyze_planck_like_gap_v1.py`:

    age_Gyr in [13.750, 13.850]
    omega_lambda in [0.680, 0.700]

That box is empty for the static FRW kernel in the current snapshot. To probe the
nearby region without tuning a single point, we define a *shell* around the same
centre (13.8 Gyr, 0.69) with modest rectangular tolerances:

    age_Gyr in [13.6, 14.0]    (±0.2 Gyr around 13.8)
    omega_lambda in [0.60, 0.78] (±0.09 around 0.69)

These numbers are chosen to:

  - comfortably include the closest kernel / sweet-subset point identified by
    `analyze_planck_like_gap_v1.py`, and
  - provide a small but non-trivial neighbourhood in FRW space,

without pretending to be a data-fitted constraint. They are explicitly a Stage 2
diagnostic, not a promoted cosmological corridor.

We then define:

  - `IN_KERNEL`:
      in_pre_data_kernel == True

  - `IN_PLANCK_NEAR_SHELL_V1`:
      IN_KERNEL and
      13.6 <= age_Gyr <= 14.0 and
      0.60 <= omega_lambda <= 0.78

  - `IN_FLOOR_V1`:
      IN_KERNEL and mech_binding_A0 >= 0.045

    (matching the "floor" threshold used in
     `analyze_non_cancellation_floor_vs_corridors_v1.py`.)

  - `IN_SHELL_AND_FLOOR_V1`:
      IN_PLANCK_NEAR_SHELL_V1 and IN_FLOOR_V1

For each of three families:

  - PRE_DATA_KERNEL
  - PLANCK_NEAR_SHELL_V1
  - PLANCK_NEAR_SHELL_AND_FLOOR_V1

we report counts, fractions, and min / max / mean of the six mechanism amplitudes.

Outputs
-------

- stage2/obstruction_tests/outputs/tables/stage2_obstruction_planck_like_shell_mech_floor_summary_v1.csv

This helper is diagnostic only. It does not modify any Phase 0–5 contracts, does
not promote the shell to a physical constraint, and does not define any preferred
theta or mechanism measure. It is intended to inform later dynamic-theta and
frustrated-floor rungs.

"""

from __future__ import annotations

from pathlib import Path
from typing import Dict, List

import pandas as pd


def describe_family(
    df: pd.DataFrame,
    mask: pd.Series,
    family_name: str,
    amp_cols: List[str],
    kernel_mask: pd.Series,
) -> Dict[str, float]:
    total_n = len(df)
    kernel_n = int(kernel_mask.sum())

    sub = df.loc[mask].copy()
    n = len(sub)
    n_in_kernel = int((mask & kernel_mask).sum())

    row: Dict[str, float] = {
        "family_name": family_name,
        "n_points": float(n),
        "frac_of_grid": float(n) / float(total_n) if total_n > 0 else float("nan"),
        "n_points_in_kernel": float(n_in_kernel),
        "frac_of_kernel": float(n_in_kernel) / float(kernel_n) if kernel_n > 0 else float(
            "nan"
        ),
    }

    for col in amp_cols:
        if n == 0:
            row[f"{col}_min"] = float("nan")
            row[f"{col}_max"] = float("nan")
            row[f"{col}_mean"] = float("nan")
        else:
            s = sub[col]
            row[f"{col}_min"] = float(s.min())
            row[f"{col}_max"] = float(s.max())
            row[f"{col}_mean"] = float(s.mean())

    return row


def main() -> int:
    repo_root = Path(__file__).resolve().parents[3]
    print("[analyze_planck_like_shell_mech_floor_v1]")
    print(f"  repo_root: {repo_root}")

    kernel_path = (
        repo_root
        / "stage2/obstruction_tests/outputs/tables/stage2_obstruction_kernel_with_mech_v1.csv"
    )
    if not kernel_path.is_file():
        print(f"  ERROR: kernel_with_mech table not found: {kernel_path}")
        return 1

    df = pd.read_csv(kernel_path)
    print(f"  loaded kernel_with_mech table: shape={df.shape}")

    required_cols = [
        "theta",
        "age_Gyr",
        "omega_lambda",
        "in_pre_data_kernel",
        "mech_baseline_A0",
        "mech_baseline_A_floor",
        "mech_baseline_bound",
        "mech_binding_A0",
        "mech_binding_A",
        "mech_binding_bound",
    ]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        print("  ERROR: missing required columns in kernel_with_mech table:")
        for c in missing:
            print(f"    - {c}")
        return 1

    # Basic masks
    kernel_mask = df["in_pre_data_kernel"].astype(bool)

    # Non-cancellation floor as used in earlier obstruction diagnostics
    floor_thresh = 0.045
    floor_mask = kernel_mask & (df["mech_binding_A0"] >= floor_thresh)

    # Planck-like band centre and shell tolerances
    age_c = 13.8
    age_tol = 0.2
    ol_c = 0.69
    ol_tol = 0.09

    shell_mask = (
        kernel_mask
        & (df["age_Gyr"].between(age_c - age_tol, age_c + age_tol))
        & (df["omega_lambda"].between(ol_c - ol_tol, ol_c + ol_tol))
    )

    shell_and_floor_mask = shell_mask & floor_mask

    total_n = len(df)
    kernel_n = int(kernel_mask.sum())
    shell_n = int(shell_mask.sum())
    shell_floor_n = int(shell_and_floor_mask.sum())

    print("  kernel size:", kernel_n, "out of", total_n)
    print(
        "  Planck-near shell (v1): age in"
        f" [{age_c - age_tol:.3f}, {age_c + age_tol:.3f}],"
        f" omega_lambda in [{ol_c - ol_tol:.3f}, {ol_c + ol_tol:.3f}]"
    )
    print(f"    points in shell: {shell_n}")
    print(f"    points in shell ∩ floor (A0 >= {floor_thresh:.3f}): {shell_floor_n}")

    amp_cols = [
        "mech_baseline_A0",
        "mech_baseline_A_floor",
        "mech_baseline_bound",
        "mech_binding_A0",
        "mech_binding_A",
        "mech_binding_bound",
    ]

    rows: List[Dict[str, float]] = []
    rows.append(
        describe_family(
            df=df,
            mask=kernel_mask,
            family_name="PRE_DATA_KERNEL",
            amp_cols=amp_cols,
            kernel_mask=kernel_mask,
        )
    )
    rows.append(
        describe_family(
            df=df,
            mask=shell_mask,
            family_name="PLANCK_NEAR_SHELL_V1",
            amp_cols=amp_cols,
            kernel_mask=kernel_mask,
        )
    )
    rows.append(
        describe_family(
            df=df,
            mask=shell_and_floor_mask,
            family_name="PLANCK_NEAR_SHELL_AND_FLOOR_V1",
            amp_cols=amp_cols,
            kernel_mask=kernel_mask,
        )
    )

    out = pd.DataFrame(rows)
    out_path = (
        repo_root
        / "stage2/obstruction_tests/outputs/tables/stage2_obstruction_planck_like_shell_mech_floor_summary_v1.csv"
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(out_path, index=False)
    print(f"  wrote summary: {out_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
