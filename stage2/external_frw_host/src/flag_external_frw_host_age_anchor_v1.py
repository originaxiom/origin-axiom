from pathlib import Path
import pandas as pd
import numpy as np


def main() -> None:
    # Resolve repo root (…/origin-axiom)
    repo_root = Path(__file__).resolve().parents[3]
    bridge_table = repo_root / "stage2/external_frw_host/outputs/tables/stage2_external_frw_background_bridge_v1.csv"
    out_table = repo_root / "stage2/external_frw_host/outputs/tables/stage2_external_frw_host_age_anchor_mask_v1.csv"

    print("[external_frw_host_age_anchor_v1]")
    print(f"  Repo root:   {repo_root}")
    print(f"  Bridge table:{bridge_table}")

    if not bridge_table.is_file():
        raise FileNotFoundError(f"Bridge table not found: {bridge_table}")

    df = pd.read_csv(bridge_table)

    required_cols = [
        "theta_index",
        "theta",
        "omega_lambda",
        "age_Gyr_host",
        "age_Gyr_toy",
        "frw_viable",
    ]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise RuntimeError(f"Missing expected columns in bridge table: {missing}")

    n_total = len(df)
    print(f"  Rows:       {n_total}")

    # --- Define host-age anchor window (Universe-like ages) ---
    AGE_MIN = 13.3
    AGE_MAX = 14.3
    print(f"  Host age anchor window [Gyr]: [{AGE_MIN:.3f}, {AGE_MAX:.3f}]")

    age_host = df["age_Gyr_host"].astype(float)
    age_toy = df["age_Gyr_toy"].astype(float)
    frw_viable = df["frw_viable"].astype(bool)

    mask_host_anchor = (age_host >= AGE_MIN) & (age_host <= AGE_MAX)

    # Optional: toy-age window for comparison (same numeric window)
    mask_toy_window = (age_toy >= AGE_MIN) & (age_toy <= AGE_MAX)

    df["in_host_age_anchor_window"] = mask_host_anchor

    # --- Summaries ---
    def count_frac(mask: pd.Series | np.ndarray) -> tuple[int, float]:
        m = np.asarray(mask, dtype=bool)
        n = int(m.sum())
        frac = float(n) / n_total if n_total > 0 else np.nan
        return n, frac

    sets = {
        "ALL_GRID": np.ones(n_total, dtype=bool),
        "FRW_VIABLE": frw_viable,
        "HOST_AGE_ANCHOR": mask_host_anchor,
        "FRW_VIABLE_AND_HOST_AGE_ANCHOR": frw_viable & mask_host_anchor,
        "TOY_AGE_WINDOW": mask_toy_window,
        "FRW_VIABLE_AND_TOY_AGE_WINDOW": frw_viable & mask_toy_window,
    }

    rows = []
    for name, m in sets.items():
        n, frac = count_frac(m)
        if n > 0:
            mean_age_host = float(age_host[m].mean())
            mean_age_toy = float(age_toy[m].mean())
        else:
            mean_age_host = float("nan")
            mean_age_toy = float("nan")
        print(
            f"  {name:28s} n={n:4d}, frac={frac:0.6f}, "
            f"<age_host>={mean_age_host:0.3f}, <age_toy>={mean_age_toy:0.3f}"
        )
        rows.append(
            {
                "set": name,
                "n_theta": n,
                "frac_of_grid": frac,
                "age_Gyr_host_mean": mean_age_host,
                "age_Gyr_toy_mean": mean_age_toy,
            }
        )

    summary_df = pd.DataFrame(
        rows,
        columns=[
            "set",
            "n_theta",
            "frac_of_grid",
            "age_Gyr_host_mean",
            "age_Gyr_toy_mean",
        ],
    )

    # --- Write per-theta mask table ---
    out_table.parent.mkdir(parents=True, exist_ok=True)

    out_cols = [
        "theta_index",
        "theta",
        "omega_lambda",
        "age_Gyr_host",
        "age_Gyr_toy",
        "frw_viable",
        "in_host_age_anchor_window",
    ]
    for c in out_cols:
        if c not in df.columns:
            raise RuntimeError(f"Expected column missing before write: {c}")

    df[out_cols].to_csv(out_table, index=False)
    print(f"  Host-age anchor mask written: {out_table}")

    # Also write a tiny summary table next to it
    summary_path = out_table.with_name("stage2_external_frw_host_age_anchor_summary_v1.csv")
    summary_df.to_csv(summary_path, index=False)
    print(f"  Summary written:              {summary_path}")


if __name__ == "__main__":
    main()
