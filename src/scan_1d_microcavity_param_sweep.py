#!/usr/bin/env python3
"""
Parameter sweep for the 1D microcavity ΔE(θ*) model.

Reads a small grid of (N, mass_contrast, cavity_width) from
config/microcavity_param_sweep.yaml and, for each point, computes ΔE(θ)
on a fixed θ-grid. Outputs:

  - data/processed/microcavity_sweep_*.npz  (raw θ-grid + ΔE)
  - data/processed/microcavity_sweep_summary.json  (aggregated stats)

This is Act IV scaffolding; implementation details live in the existing
1D cavity routines where possible.
"""

import json
import pathlib
from dataclasses import asdict, dataclass
from typing import Dict, Any

import numpy as np
import yaml

# TODO: adjust import to your actual microcavity module
# from cancellation_system.microcavity_1d import compute_deltaE_theta_grid

ROOT = pathlib.Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config" / "microcavity_param_sweep.yaml"
DATA_DIR = ROOT / "data" / "processed"
DATA_DIR.mkdir(parents=True, exist_ok=True)


@dataclass
class SweepResult:
    N: int
    mass_contrast: float
    cavity_width: float
    theta_fid: float
    deltaE_fid: float
    theta_min: float
    deltaE_min: float
    theta_max: float
    deltaE_max: float
    sign_pattern: str  # e.g. "neg_min_pos_tail" or similar


def main() -> None:
    with CONFIG_PATH.open("r") as f:
        cfg = yaml.safe_load(f)

    Ns = cfg["lattice_sizes"]
    mass_contrasts = cfg["mass_contrasts"]
    cavity_widths = cfg["cavity_widths"]
    theta_start = cfg["theta_grid"]["start"]
    theta_stop = cfg["theta_grid"]["stop"]
    theta_num = cfg["theta_grid"]["num"]

    theta_grid = np.linspace(theta_start, theta_stop, theta_num)
    theta_fid = 3.63  # import from theta_star_config.json in a later refinement

    summary: Dict[str, Any] = {}
    results = []

    for N in Ns:
        for mc in mass_contrasts:
            for w in cavity_widths:
                key = f"N{N}_mc{mc:.3f}_w{w:.1f}"
                print(f"=== Running microcavity sweep for {key} ===")

                # TODO: call your existing microcavity routine here:
                # deltaE = compute_deltaE_theta_grid(theta_grid, N=N,
                #                                    mass_contrast=mc,
                #                                    cavity_width=w)
                # Placeholder to keep the script runnable until wired:
                deltaE = np.zeros_like(theta_grid)

                # Find indices and values
                i_min = int(np.argmin(deltaE))
                i_max = int(np.argmax(deltaE))

                # Closest to fiducial θ*
                i_fid = int(np.argmin(np.abs(theta_grid - theta_fid)))

                res = SweepResult(
                    N=N,
                    mass_contrast=mc,
                    cavity_width=w,
                    theta_fid=float(theta_grid[i_fid]),
                    deltaE_fid=float(deltaE[i_fid]),
                    theta_min=float(theta_grid[i_min]),
                    deltaE_min=float(deltaE[i_min]),
                    theta_max=float(theta_grid[i_max]),
                    deltaE_max=float(deltaE[i_max]),
                    sign_pattern="TODO",  # fill based on actual shape later
                )
                results.append(res)

                # Save raw grid for this config
                out_npz = DATA_DIR / f"microcavity_sweep_{key}.npz"
                np.savez_compressed(
                    out_npz,
                    theta_grid=theta_grid,
                    deltaE=deltaE,
                    N=N,
                    mass_contrast=mc,
                    cavity_width=w,
                )
                summary[key] = asdict(res)

    # Save aggregated summary
    out_json = DATA_DIR / "microcavity_sweep_summary.json"
    with out_json.open("w") as f:
        json.dump(
            {
                "theta_fid_nominal": theta_fid,
                "results": summary,
            },
            f,
            indent=2,
        )

    print(f"Wrote summary to {out_json}")


if __name__ == "__main__":
    main()