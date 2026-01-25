from __future__ import annotations

import math
from pathlib import Path

import pandas as pd


def find_repo_root(start: Path) -> Path:
    cur = start
    for _ in range(10):
        if (cur / ".git").exists() and (cur / "README.md").exists():
            return cur
        if cur.parent == cur:
            break
        cur = cur.parent
    raise SystemExit("[analyze_planck_like_gap_v1] ERROR: could not find repo root")


def main() -> int:
    here = Path(__file__).resolve()
    repo_root = find_repo_root(here)
    print(f"[analyze_planck_like_gap_v1] repo_root: {repo_root}")

    kernel_path = (
        repo_root
        / "stage2/obstruction_tests/outputs/tables/stage2_obstruction_static_frw_kernel_v1.csv"
    )
    if not kernel_path.exists():
        raise SystemExit(
            f"[analyze_planck_like_gap_v1] ERROR: kernel table not found: {kernel_path}"
        )

    df = pd.read_csv(kernel_path)

    required_cols = {"theta", "age_Gyr", "omega_lambda", "in_pre_data_kernel"}
    missing = required_cols - set(df.columns)
    if missing:
        raise SystemExit(
            "[analyze_planck_like_gap_v1] ERROR: missing required columns: "
            + ", ".join(sorted(missing))
        )

    kernel_mask = df["in_pre_data_kernel"].astype(bool)
    df_k = df.loc[kernel_mask].copy()
    if df_k.empty:
        raise SystemExit("[analyze_planck_like_gap_v1] ERROR: empty pre-data kernel")

    # Planck-like band used in apply_planck_like_frw_corridor_v1
    age_min, age_max = 13.750, 13.850
    ol_min, ol_max = 0.680, 0.700
    age_c = 0.5 * (age_min + age_max)
    ol_c = 0.5 * (ol_min + ol_max)

    print("[analyze_planck_like_gap_v1] Planck-like band (v1):")
    print(f"  age_Gyr in [{age_min:.3f}, {age_max:.3f}]")
    print(f"  omega_lambda in [{ol_min:.3f}, {ol_max:.3f}]")

    # Basic coverage of the kernel
    age_min_k = df_k["age_Gyr"].min()
    age_max_k = df_k["age_Gyr"].max()
    ol_min_k = df_k["omega_lambda"].min()
    ol_max_k = df_k["omega_lambda"].max()

    print("[analyze_planck_like_gap_v1] Kernel coverage:")
    print(f"  age_Gyr in [{age_min_k:.3f}, {age_max_k:.3f}]")
    print(f"  omega_lambda in [{ol_min_k:.3f}, {ol_max_k:.3f}]")

    # Helper to compute distance from the rectangle in (age, omega_lambda)
    def rect_distance(age: float, ol: float) -> tuple[float, float, float]:
        if age_min <= age <= age_max:
            d_age = 0.0
        elif age < age_min:
            d_age = age_min - age
        else:
            d_age = age - age_max

        if ol_min <= ol <= ol_max:
            d_ol = 0.0
        elif ol < ol_min:
            d_ol = ol_min - ol
        else:
            d_ol = ol - ol_max

        d = math.hypot(d_age, d_ol)
        return d_age, d_ol, d

    # Distances for kernel
    d_rows = []
    for idx, row in df_k.iterrows():
        age = float(row["age_Gyr"])
        ol = float(row["omega_lambda"])
        d_age, d_ol, d = rect_distance(age, ol)
        d_rows.append((idx, d_age, d_ol, d))

    best_idx, best_d_age, best_d_ol, best_d = min(d_rows, key=lambda t: t[3])
    best_row = df_k.loc[best_idx]

    print("[analyze_planck_like_gap_v1] Closest kernel point to Planck-like band:")
    print(f"  theta          = {best_row['theta']:.9f}")
    print(f"  age_Gyr        = {best_row['age_Gyr']:.6f}")
    print(f"  omega_lambda   = {best_row['omega_lambda']:.6f}")
    print(f"  d_age_to_band  = {best_d_age:.6f} Gyr")
    print(f"  d_ol_to_band   = {best_d_ol:.6f}")
    print(f"  d_rect         = {best_d:.6f} (Euclidean in age/omega space)")
    print(f"  age_center_off = {best_row['age_Gyr'] - age_c:.6f} Gyr")
    print(f"  ol_center_off  = {best_row['omega_lambda'] - ol_c:.6f}")

    # Optional: do the same restricted to the "sweet subset" if columns exist
    sweet_summary = None
    if {"lcdm_like", "in_toy_corridor"}.issubset(df.columns):
        sweet_mask = (
            df["in_pre_data_kernel"].astype(bool)
            & df["lcdm_like"].astype(bool)
            & df["in_toy_corridor"].astype(bool)
        )
        df_s = df.loc[sweet_mask].copy()
        if not df_s.empty:
            s_rows = []
            for idx, row in df_s.iterrows():
                age = float(row["age_Gyr"])
                ol = float(row["omega_lambda"])
                d_age, d_ol, d = rect_distance(age, ol)
                s_rows.append((idx, d_age, d_ol, d))
            s_best_idx, s_best_d_age, s_best_d_ol, s_best_d = min(
                s_rows, key=lambda t: t[3]
            )
            s_best = df_s.loc[s_best_idx]
            print("[analyze_planck_like_gap_v1] Closest sweet-subset point:")
            print(f"  theta          = {s_best['theta']:.9f}")
            print(f"  age_Gyr        = {s_best['age_Gyr']:.6f}")
            print(f"  omega_lambda   = {s_best['omega_lambda']:.6f}")
            print(f"  d_age_to_band  = {s_best_d_age:.6f} Gyr")
            print(f"  d_ol_to_band   = {s_best_d_ol:.6f}")
            print(f"  d_rect         = {s_best_d:.6f}")
            print(
                f"  age_center_off = {s_best['age_Gyr'] - age_c:.6f} Gyr"
            )
            print(
                f"  ol_center_off  = {s_best['omega_lambda'] - ol_c:.6f}"
            )
            sweet_summary = {
                "theta": float(s_best["theta"]),
                "age_Gyr": float(s_best["age_Gyr"]),
                "omega_lambda": float(s_best["omega_lambda"]),
                "d_age_to_band": s_best_d_age,
                "d_ol_to_band": s_best_d_ol,
                "d_rect": s_best_d,
            }

    # Write a tiny CSV summary so Stage2 docs can quote it if needed
    rows = [
        {
            "family": "KERNEL",
            "theta": float(best_row["theta"]),
            "age_Gyr": float(best_row["age_Gyr"]),
            "omega_lambda": float(best_row["omega_lambda"]),
            "d_age_to_band": best_d_age,
            "d_ol_to_band": best_d_ol,
            "d_rect": best_d,
        }
    ]
    if sweet_summary is not None:
        s = sweet_summary.copy()
        s["family"] = "SWEET_SUBSET"
        rows.append(s)

    out = pd.DataFrame(rows)
    out_path = (
        repo_root
        / "stage2/obstruction_tests/outputs/tables/stage2_obstruction_planck_like_gap_summary_v1.csv"
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(out_path, index=False)
    print(f"[analyze_planck_like_gap_v1] wrote summary: {out_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
