from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict

import numpy as np

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from phase2.utils_meta import setup_run, write_json
from phase2.modes.mode_model import run_mode_sum, to_summary_dict


# ============================================================
# Origin Axiom — Phase 2
# Runner for Figure A (mode-sum residual)
#
# Produces:
#   outputs/runs/<run_id>/
#     meta.json, params.json, summary.json, pip_freeze.txt
#     raw/mode_sum_outputs.npz
#     figures/residual.pdf
#
# The canonical figure is copied by Snakemake into outputs/figures/.
# ============================================================


def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Phase 2 mode-sum runner (Figure A).")
    p.add_argument("--config", required=True, help="Path to config/phase2.yaml")
    p.add_argument("--task", required=True, choices=["residual"], help="Task selector (currently only 'residual').")
    p.add_argument("--run-id", required=True, help="Run ID: figA_mode_sum_residual_YYYYMMDDTHHMMSSZ")
    return p.parse_args()


def _save_pdf(fig: plt.Figure, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(str(path), format="pdf", bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    args = _parse_args()
    config_path = Path(args.config).resolve()
    run_id = str(args.run_id)

    # Setup run dir + provenance
    cfg_raw, paths, meta, repo_root = setup_run(
        config_path=config_path,
        run_id=run_id,
        task=args.task,
    )

    # Reload resolved config snapshot (ensures run uses recorded params)
    with paths.params_json.open("r", encoding="utf-8") as f:
        cfg_resolved: Dict[str, Any] = json.load(f)

    # Run the model
    res = run_mode_sum(cfg_resolved)

    # Save raw outputs
    paths.raw_dir.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(
        paths.raw_dir / "mode_sum_outputs.npz",
        amplitude_raw=np.array([res.amplitude_raw.real, res.amplitude_raw.imag], dtype=np.float64),
        amplitude_constrained=np.array([res.amplitude_constrained.real, res.amplitude_constrained.imag], dtype=np.float64),
        residual_raw=np.float64(res.residual_raw),
        residual_constrained=np.float64(res.residual_constrained),
        cancellation_ratio_raw=np.float64(res.cancellation_ratio_raw),
        cancellation_ratio_constrained=np.float64(res.cancellation_ratio_constrained),
        epsilon=np.float64(res.inputs.epsilon),
        n_modes=np.int64(res.inputs.n_modes),
        cutoff_value=np.float64(res.inputs.cutoff_value),
        phase_type=np.array([res.inputs.phase_type]),
        phase_value=np.array([res.inputs.phase_value]),
    )

    # Plot residual figure (single panel)
    fig = plt.figure(figsize=(6.2, 3.6))
    ax = fig.add_subplot(1, 1, 1)

    bars = ["raw", "constrained"]
    vals = [res.residual_raw, res.residual_constrained]
    ax.bar(bars, vals)

    ax.set_ylabel(r"Residual proxy $|A|$ (code units)")
    ax.set_title("Mode-sum residual under global non-cancellation constraint")

    # Annotate with metadata (Phase-1 style)
    txt = (
        f"n_modes={res.inputs.n_modes}\n"
        f"cutoff=({res.inputs.cutoff_type}, {res.inputs.cutoff_value})\n"
        f"phase=({res.inputs.phase_type}, {res.inputs.phase_value})\n"
        f"epsilon={res.inputs.epsilon:.3e}\n"
        f"constraint_applied={bool(res.constraint.applied)}"
    )
    ax.text(
        1.02, 0.5, txt,
        transform=ax.transAxes,
        va="center", ha="left", fontsize=9
    )

    out_fig = paths.fig_dir / "residual.pdf"
    _save_pdf(fig, out_fig)

    # Summary JSON (stable schema)
    summary = to_summary_dict(res)
    summary["output_files"] = {
        "figure": "figures/residual.pdf",
        "raw": "raw/mode_sum_outputs.npz",
    }
    write_json(paths.summary_json, summary)


if __name__ == "__main__":
    main()