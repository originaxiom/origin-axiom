#!/usr/bin/env python3
"""
phase3_mech.measure_v1

Non-binding Phase 3 experiment:
- Study the empirical distribution of the baseline amplitude A0(theta)
  across many random ensembles of phases and windings.
- Quantify how much probability weight lives near A0 ~ 0.

This is a *measure / selection* probe only. It does NOT:
- introduce new claims;
- change the Phase 3 floor definition;
- define a binding theta-filter.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Any

import numpy as np


# ---------------------------------------------------------------------
# Configuration and simple helpers
# ---------------------------------------------------------------------

@dataclass
class MeasureConfig:
    seed: int = 20260107
    n_theta: int = 1024          # number of theta grid points
    n_modes: int = 64            # modes per ensemble
    n_ensembles: int = 256       # how many independent ensembles
    min_winding: int = 1
    max_winding: int = 4
    n_bins: int = 64             # histogram bins for A0
    eps_candidates: tuple = (0.005, 0.01, 0.02, 0.05)


def get_paths() -> Dict[str, Path]:
    """
    Resolve repository root and Phase 3 tables directory.

    Layout assumption:
      repo_root/
        phase3/
          src/phase3_mech/measure_v1.py
          outputs/tables/
    """
    # .../phase3/src/phase3_mech/measure_v1.py
    here = Path(__file__).resolve()
    # parents: [phase3_mech, src, phase3, origin-axiom, ...]
    repo_root = here.parents[3]
    phase3_root = repo_root / "phase3"
    out_dir = phase3_root / "outputs" / "tables"
    out_dir.mkdir(parents=True, exist_ok=True)
    return {
        "repo_root": repo_root,
        "phase3_root": phase3_root,
        "out_dir": out_dir,
        "json_stats": out_dir / "phase3_measure_v1_stats.json",
        "csv_hist": out_dir / "phase3_measure_v1_hist.csv",
    }


def build_theta_grid(n_theta: int) -> np.ndarray:
    # [0, 2pi) uniformly
    return np.linspace(0.0, 2.0 * np.pi, n_theta, endpoint=False)


def sample_ensemble_amplitude(
    rng: np.random.Generator,
    theta_grid: np.ndarray,
    cfg: MeasureConfig,
) -> np.ndarray:
    """
    Sample one random ensemble:
      alpha_k ~ Uniform[0, 2pi)
      sigma_k in {min_winding, ..., max_winding}
    Compute A0(theta) = |mean_k z_k(theta)|.
    Returns A0(theta_grid) as a 1D array of length n_theta.
    """
    n_theta = theta_grid.shape[0]
    n_modes = cfg.n_modes

    # Phases and windings
    alpha = rng.uniform(0.0, 2.0 * np.pi, size=(n_modes,))
    sigma = rng.integers(cfg.min_winding, cfg.max_winding + 1, size=(n_modes,))

    # Broadcast to (n_modes, n_theta)
    theta = theta_grid[None, :]  # (1, n_theta)
    phase = alpha[:, None] + sigma[:, None] * theta  # (n_modes, n_theta)
    z = np.exp(1j * phase)

    # Ensemble mean over modes
    mean_z = np.mean(z, axis=0)  # (n_theta,)
    A0 = np.abs(mean_z)
    return A0


# ---------------------------------------------------------------------
# Main experiment
# ---------------------------------------------------------------------

def main() -> None:
    cfg = MeasureConfig()
    paths = get_paths()

    rng = np.random.default_rng(cfg.seed)
    theta_grid = build_theta_grid(cfg.n_theta)

    # Collect amplitude arrays: shape (n_ensembles, n_theta)
    amplitudes = np.empty((cfg.n_ensembles, cfg.n_theta), dtype=float)

    for i in range(cfg.n_ensembles):
        A0 = sample_ensemble_amplitude(rng, theta_grid, cfg)
        amplitudes[i, :] = A0

    flat = amplitudes.ravel()  # all A0 values across ensembles and theta

    # Basic statistics
    stats: Dict[str, Any] = {
        "config": asdict(cfg),
        "n_samples": int(flat.size),
        "A0_min": float(np.min(flat)),
        "A0_max": float(np.max(flat)),
        "A0_mean": float(np.mean(flat)),
        "A0_std": float(np.std(flat)),
        "A0_p01": float(np.quantile(flat, 0.01)),
        "A0_p05": float(np.quantile(flat, 0.05)),
        "A0_p25": float(np.quantile(flat, 0.25)),
        "A0_p50": float(np.quantile(flat, 0.50)),
        "A0_p75": float(np.quantile(flat, 0.75)),
        "A0_p95": float(np.quantile(flat, 0.95)),
        "A0_p99": float(np.quantile(flat, 0.99)),
    }

    # How much mass lies below some small eps candidates?
    eps_info = {}
    for eps in cfg.eps_candidates:
        frac = float(np.mean(flat < eps))
        eps_info[str(eps)] = {
            "eps": float(eps),
            "fraction_below_eps": frac,
        }
    stats["eps_candidates"] = eps_info

    # Histogram for a coarse view
    hist_counts, bin_edges = np.histogram(
        flat,
        bins=cfg.n_bins,
        range=(0.0, float(flat.max())),
    )

    # Write JSON stats
    with paths["json_stats"].open("w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2, sort_keys=True)

    # Write CSV histogram
    import csv

    with paths["csv_hist"].open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["bin_left", "bin_right", "count"])
        for i in range(len(hist_counts)):
            writer.writerow([
                f"{bin_edges[i]:.8g}",
                f"{bin_edges[i+1]:.8g}",
                int(hist_counts[i]),
            ])

    # Lightweight console summary
    print("[phase3_measure_v1] Repo root:", paths["repo_root"])
    print("[phase3_measure_v1] Phase 3 root:", paths["phase3_root"])
    print("[phase3_measure_v1] Wrote stats JSON to", paths["json_stats"])
    print("[phase3_measure_v1] Wrote histogram CSV to", paths["csv_hist"])
    print("[phase3_measure_v1] A0_min = {0:.6g}, A0_p01 = {1:.6g}".format(
        stats["A0_min"], stats["A0_p01"]
    ))
    for eps, info in eps_info.items():
        print(
            f"  eps = {info['eps']:.4g} -> "
            f"fraction_below_eps = {info['fraction_below_eps']:.6f}"
        )


if __name__ == "__main__":
    main()
