from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict

import numpy as np

from phase2.utils_meta import setup_run, write_json
from phase2.modes.mode_model import run_mode_sum, to_summary_dict
from phase2.observables import plot_mode_sum_residual


# ============================================================
# Origin Axiom — Phase 2
# Figure A runner (Claim 2.1): mode-sum residual demonstration
#
# Canonical outputs (per-run):
#   outputs/runs/<run_id>/
#     raw/mode_sum_outputs.npz
#     figures/residual.pdf
#     summary.json
#
# This script is intended to be called by Snakemake.
# Direct invocation is allowed for debugging, but canonical artifacts
# are produced only through Snakemake.
# ============================================================


def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Phase 2 mode-sum runner (Fig A).")
    p.add_argument("--config", required=True, help="Path to config/phase2.yaml")
    p.add_argument(
        "--task",
        required=True,
        choices=["residual"],
        help="Which output to generate (Phase 2 currently uses only 'residual').",
    )
    p.add_argument("--run-id", required=True, help="Run ID (used for outputs/runs/<run_id>/)")
    return p.parse_args()


def main() -> None:
    args = _parse_args()
    config_path = Path(args.config).resolve()
    run_id = str(args.run_id)

    # ------------------------------------------------------------
    # Setup run directory + write params.json/meta.json/pip_freeze.txt
    # ------------------------------------------------------------
    _cfg_raw, paths, _meta, _repo_root = setup_run(
        config_path=config_path,
        run_id=run_id,
        task=f"mode_sum_{args.task}",
    )

    # Reload resolved snapshot so the run uses what is recorded
    with paths.params_json.open("r", encoding="utf-8") as f:
        cfg: Dict[str, Any] = json.load(f)

    # ------------------------------------------------------------
    # Execute model
    # ------------------------------------------------------------
    res = run_mode_sum(cfg)

    # ------------------------------------------------------------
    # Save raw arrays (minimal, but sufficient for audit)
    # ------------------------------------------------------------
    paths.raw_dir.mkdir(parents=True, exist_ok=True)

    np.savez_compressed(
        paths.raw_dir / "mode_sum_outputs.npz",
        amplitude_raw=np.array([res.amplitude_raw.real, res.amplitude_raw.imag], dtype=np.float64),
        amplitude_constrained=np.array([res.amplitude_constrained.real, res.amplitude_constrained.imag], dtype=np.float64),
        residual_raw=np.float64(res.residual_raw),
        residual_constrained=np.float64(res.residual_constrained),
        cancellation_ratio_raw=np.float64(res.cancellation_ratio_raw),
        cancellation_ratio_constrained=np.float64(res.cancellation_ratio_constrained),
        constraint_applied=np.bool_(res.constraint.applied),
        epsilon=np.float64(res.inputs.epsilon),
        n_modes=np.int64(res.inputs.n_modes),
        cutoff_value=np.float64(res.inputs.cutoff_value),
        cutoff_type=np.array([res.inputs.cutoff_type]),
        phase_type=np.array([res.inputs.phase_type]),
        phase_value=np.array([res.inputs.phase_value]),
        seed=np.int64(res.inputs.seed),
    )

    # ------------------------------------------------------------
    # Plot (per-run)
    # ------------------------------------------------------------
    plot_mode_sum_residual(res, paths.fig_dir)

    # ------------------------------------------------------------
    # Write summary.json used by CLAIMS.md + paper
    # ------------------------------------------------------------
    summary = to_summary_dict(res)
    summary["output_files"] = {
        "figure": "figures/residual.pdf",
        "raw": "raw/mode_sum_outputs.npz",
    }
    write_json(paths.summary_json, summary)


if __name__ == "__main__":
    main()