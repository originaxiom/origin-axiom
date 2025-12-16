#!/usr/bin/env python3
"""
Refresh data/processed/microcavity_sweep_summary.json by actually
reading the per-configuration microcavity NPZ scans and computing stats.

Assumptions:
  - Summary JSON already exists and has the structure:
      {
        "theta_fid_nominal": ...,
        "results": {
          "N256_mc0.150_w8.0": {...},
          ...
        }
      }
  - For each label L in results, there is a corresponding NPZ file:
      data/processed/microcavity_sweep_<L>.npz
  - Each NPZ file contains:
      theta_grid  (1D array)
      delta_E     (1D array; same length as theta_grid)
"""

import json
from pathlib import Path

import numpy as np


def main():
    base = Path(__file__).resolve().parents[1]  # repo root
    summary_path = base / "data" / "processed" / "microcavity_sweep_summary.json"

    if not summary_path.exists():
        raise FileNotFoundError(f"Cannot find summary JSON at {summary_path}")

    summary = json.loads(summary_path.read_text())

    theta_fid_nominal = float(summary.get("theta_fid_nominal", 3.63))
    results = summary.get("results", {})

    print(f"Using theta_fid_nominal = {theta_fid_nominal:.6f} rad")

    updated = 0
    skipped = 0

    for label, info in results.items():
        # Example: label = "N512_mc0.200_w8.0"
        npz_name = f"microcavity_sweep_{label}.npz"
        npz_path = base / "data" / "processed" / npz_name

        if not npz_path.exists():
            print(f"[WARN] Missing NPZ for {label}: {npz_path} (skipping)")
            skipped += 1
            continue

        data = np.load(npz_path)

        if "theta_grid" not in data or "delta_E" not in data:
            print(f"[WARN] NPZ {npz_path} lacks theta_grid or delta_E (skipping)")
            skipped += 1
            continue

        theta_grid = np.asarray(data["theta_grid"], dtype=float)
        delta_E = np.asarray(data["delta_E"], dtype=float)

        if theta_grid.shape != delta_E.shape:
            print(f"[WARN] Shape mismatch in {npz_path}: "
                  f"theta_grid {theta_grid.shape}, delta_E {delta_E.shape}")
            skipped += 1
            continue

        # Global min / max
        i_min = int(np.argmin(delta_E))
        i_max = int(np.argmax(delta_E))

        theta_min = float(theta_grid[i_min])
        theta_max = float(theta_grid[i_max])
        deltaE_min = float(delta_E[i_min])
        deltaE_max = float(delta_E[i_max])

        # Value at fiducial theta (nearest grid point)
        i_fid = int(np.argmin(np.abs(theta_grid - theta_fid_nominal)))
        theta_fid = float(theta_grid[i_fid])
        deltaE_fid = float(delta_E[i_fid])

        # Simple sign descriptor
        if deltaE_min < 0.0 and abs(deltaE_min) > 1e-8:
            sign_pattern = "vacuum-lowering-well"
        elif deltaE_max > 0.0 and abs(deltaE_max) > 1e-8:
            sign_pattern = "vacuum-raising-hump"
        else:
            sign_pattern = "flat-or-numerically-zero"

        info.update(
            theta_fid=theta_fid,
            deltaE_fid=deltaE_fid,
            theta_min=theta_min,
            theta_max=theta_max,
            deltaE_min=deltaE_min,
            deltaE_max=deltaE_max,
            sign_pattern=sign_pattern,
        )

        updated += 1
        print(
            f"[OK] {label:22} "
            f"ΔE_fid={deltaE_fid:+.3e}, "
            f"ΔE_min={deltaE_min:+.3e}, "
            f"ΔE_max={deltaE_max:+.3e}"
        )

    print(f"\nUpdated {updated} entries, skipped {skipped}.")

    # Write back, nicely formatted
    summary["results"] = results
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True))
    print(f"Wrote updated summary to {summary_path}")


if __name__ == "__main__":
    main()