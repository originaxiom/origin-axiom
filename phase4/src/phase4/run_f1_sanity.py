#!/usr/bin/env python3
"""
Phase 4 F1 sanity script.

This script:
  - loads the Phase 3 baseline vacuum configuration;
  - reads the canonical epsfloor from the baseline diagnostics;
  - computes the F1 mapping E_vac(theta) = alpha * A(theta)**beta; and
  - prints simple summary diagnostics and writes a CSV for later plots.
"""

from __future__ import annotations

import csv
import pathlib
import sys

import numpy as np

# Compute repository root from this file's location.
# File is:   <repo>/phase4/src/phase4/run_f1_sanity.py
# parents[0] = <repo>/phase4/src/phase4
# parents[1] = <repo>/phase4/src
# parents[2] = <repo>/phase4
# parents[3] = <repo>
THIS_FILE = pathlib.Path(__file__).resolve()
REPO_ROOT = THIS_FILE.parents[3]

# Ensure Phase 3 and Phase 4 src directories are importable.
PHASE3_SRC = REPO_ROOT / "phase3" / "src"
PHASE4_SRC = REPO_ROOT / "phase4" / "src"

sys.path.insert(0, str(PHASE3_SRC))
sys.path.insert(0, str(PHASE4_SRC))

from phase4 import (  # type: ignore[import]
    build_default_f1_config,
    compute_f1_vacuum_curve,
)


def main() -> None:
    cfg = build_default_f1_config()
    thetas, evac, meta = compute_f1_vacuum_curve(cfg)

    out_dir = REPO_ROOT / "phase4" / "outputs" / "tables"
    out_dir.mkdir(parents=True, exist_ok=True)
    csv_path = out_dir / "phase4_F1_sanity_curve.csv"

    # Write per-theta CSV for later figures.
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["theta", "E_vac"])
        for th, ev in zip(thetas, evac):
            writer.writerow([float(th), float(ev)])

    print("[F1_sanity] Wrote curve to", csv_path)
    print("[F1_sanity] Mapping metadata:")
    for k, v in meta.items():
        print(f"  {k}: {v}")

    print("[F1_sanity] E_vac(theta) summary:")
    print("  min:", float(np.min(evac)))
    print("  max:", float(np.max(evac)))
    print("  mean:", float(np.mean(evac)))


if __name__ == "__main__":
    main()
