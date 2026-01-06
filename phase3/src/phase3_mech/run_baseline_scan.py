#!/usr/bin/env python3
"""
Phase 3 mechanism: baseline binding scan.

This script:
  - constructs the baseline_v1 vacuum configuration;
  - scans the unconstrained amplitude A_0(theta) on a uniform grid;
  - chooses epsfloor as the 25th percentile of A_0(theta);
  - rescans with the floor enforced to obtain A(theta) and a binding mask;
  - writes a CSV of (theta, A0, A_floor, bound_flag);
  - writes a JSON diagnostics file with summary statistics.

It is a convenience tool for Rung 4 and later rungs; it does not
change the Phase 3 gate, which still only builds the paper artifact.
"""

from __future__ import annotations

import json
import math
import pathlib
import sys

import numpy as np

# Ensure we can import phase3_mech when this file is run as a script
THIS_FILE = pathlib.Path(__file__).resolve()
SRC_DIR = THIS_FILE.parents[1]  # .../phase3/src
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from phase3_mech import (  # type: ignore  # noqa: E402
    make_vacuum_config,
    scan_amplitude_unconstrained,
    scan_amplitude_with_floor,
)


def main() -> None:
    # Locate the phase3 directory relative to this file.
    phase3_dir = THIS_FILE.parents[2]  # .../phase3

    tables_dir = phase3_dir / "outputs" / "tables"
    tables_dir.mkdir(parents=True, exist_ok=True)

    csv_path = tables_dir / "mech_baseline_scan.csv"
    diag_path = tables_dir / "mech_baseline_scan_diagnostics.json"

    # Baseline configuration and scan settings
    cfg = make_vacuum_config("baseline_v1")
    n_grid = 2048
    theta_min = 0.0
    theta_max = 2.0 * math.pi

    # First: unconstrained scan to see the distribution of A_0(theta)
    thetas, amps0 = scan_amplitude_unconstrained(
        cfg,
        n_grid=n_grid,
        theta_min=theta_min,
        theta_max=theta_max,
    )

    # Choose epsfloor as the 25th percentile of A_0(theta).
    # This ensures a non-zero but non-dominant binding fraction by construction.
    epsfloor = float(np.quantile(amps0, 0.25))

    # Second: scan with the floor enforced using the helper,
    # which recomputes A_0(theta) internally for clarity.
    (
        thetas_floor,
        amps0_floor,
        amps_floor,
        binds,
        diagnostics,
    ) = scan_amplitude_with_floor(
        cfg,
        epsfloor=epsfloor,
        n_grid=n_grid,
        theta_min=theta_min,
        theta_max=theta_max,
    )

    # Sanity checks on alignment
    assert np.allclose(thetas, thetas_floor)
    assert np.allclose(amps0, amps0_floor)

    # Write CSV with per-theta values
    with csv_path.open("w", encoding="utf-8") as f:
        f.write("theta,A0,A_floor,bound\n")
        for t, a0, af, b in zip(thetas, amps0, amps_floor, binds):
            f.write(f"{t:.9f},{a0:.9e},{af:.9e},{int(bool(b))}\n")

    # Enrich diagnostics with grid and quantile information
    diag_full = {
        "epsfloor": float(diagnostics.get("epsfloor", epsfloor)),
        "min_unconstrained": float(
            diagnostics.get("min_unconstrained", float(amps0.min()))
        ),
        "max_unconstrained": float(
            diagnostics.get("max_unconstrained", float(amps0.max()))
        ),
        "frac_bound": float(diagnostics.get("frac_bound", float(binds.mean()))),
        "n_grid": int(n_grid),
        "theta_min": float(theta_min),
        "theta_max": float(theta_max),
        "q25_unconstrained": float(np.quantile(amps0, 0.25)),
        "q50_unconstrained": float(np.quantile(amps0, 0.50)),
        "q75_unconstrained": float(np.quantile(amps0, 0.75)),
    }

    with diag_path.open("w", encoding="utf-8") as f:
        json.dump(diag_full, f, indent=2, sort_keys=True)

    print(f"[baseline_scan] Wrote CSV to {csv_path}")
    print(f"[baseline_scan] Wrote diagnostics to {diag_path}")
    print("[baseline_scan] Summary diagnostics:")
    for k, v in diag_full.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
