from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List

import numpy as np

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from phase2.utils_meta import setup_run, write_json
from phase2.modes.mode_model import run_mode_sum
from phase2.observables import plot_scaling_curve, summarize_result


# ============================================================
# Origin Axiom — Phase 2
# Parameter sweep runner (Figures B, C, D)
#
# Contract (HARD):
# - Always creates <run>/figures/
# - Always writes exactly ONE scaling PDF
# - Filename is deterministic per sweep
# - Raises on invalid or empty sweeps
# ============================================================


def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Phase 2 sweep runner.")
    p.add_argument("--config", required=True, help="Path to config/phase2.yaml")
    p.add_argument(
        "--sweep",
        required=True,
        choices=["epsilon", "cutoff", "n_modes"],
        help="Which parameter to sweep",
    )
    p.add_argument("--run-id", required=True, help="Run ID")
    return p.parse_args()


def _get_sweep_cfg(cfg: Dict[str, Any], name: str) -> Dict[str, Any]:
    sweeps = cfg.get("sweeps", {})
    if name not in sweeps:
        raise ValueError(f"Sweep '{name}' not found in config.sweeps")
    sweep_cfg = sweeps[name]
    if not sweep_cfg.get("enabled", False):
        raise ValueError(f"Sweep '{name}' is disabled in config")
    values = sweep_cfg.get("values", [])
    if not isinstance(values, list) or len(values) < 2:
        raise ValueError(f"Sweep '{name}' must define at least 2 values")
    return sweep_cfg


def main() -> None:
    args = _parse_args()
    sweep_name = args.sweep
    run_id = str(args.run_id)
    config_path = Path(args.config).resolve()

    # ------------------------------------------------------------
    # Setup run + provenance
    # ------------------------------------------------------------
    cfg_raw, paths, meta, repo_root = setup_run(
        config_path=config_path,
        run_id=run_id,
        task=f"sweep_{sweep_name}",
    )

    # Reload frozen config snapshot
    with paths.params_json.open("r", encoding="utf-8") as f:
        cfg: Dict[str, Any] = json.load(f)

    # ------------------------------------------------------------
    # Resolve sweep definition
    # ------------------------------------------------------------
    sweep_cfg = _get_sweep_cfg(cfg, sweep_name)
    sweep_values: List[float] = list(sweep_cfg["values"])

    # ------------------------------------------------------------
    # Execute sweep
    # ------------------------------------------------------------
    x_vals: List[float] = []
    y_vals: List[float] = []
    summaries: List[Dict[str, Any]] = []

    for val in sweep_values:
        # Patch config copy for this run
        cfg_local = json.loads(json.dumps(cfg))  # deep copy

        if sweep_name == "epsilon":
            cfg_local["mode_sum"]["epsilon"] = float(val)
        elif sweep_name == "cutoff":
            cfg_local["mode_sum"]["cutoff_value"] = float(val)
        elif sweep_name == "n_modes":
            cfg_local["mode_sum"]["n_modes"] = int(val)

        res = run_mode_sum(cfg_local)

        x_vals.append(float(val))
        y_vals.append(float(res.residual_constrained))
        summaries.append(summarize_result(res))

    # ------------------------------------------------------------
    # GUARANTEE figures/ exists
    # ------------------------------------------------------------
    paths.fig_dir.mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------
    # Determine canonical filename + labels
    # ------------------------------------------------------------
    if sweep_name == "epsilon":
        fname = "scaling_epsilon.pdf"
        xlabel = "ε"
        xscale = "log"
    elif sweep_name == "cutoff":
        fname = "scaling_cutoff.pdf"
        xlabel = "cutoff"
        xscale = "log"
    elif sweep_name == "n_modes":
        fname = "scaling_modes.pdf"
        xlabel = "number of modes"
        xscale = "log"

    # ------------------------------------------------------------
    # Plot (this MUST happen, no conditionals)
    # ------------------------------------------------------------
    plot_scaling_curve(
        x=x_vals,
        y=y_vals,
        xlabel=xlabel,
        ylabel="residual (constrained)",
        title=f"Residual scaling with {sweep_name}",
        run_fig_dir=paths.fig_dir,
        filename=fname,
        xscale=xscale,
        yscale="log",
    )

    # ------------------------------------------------------------
    # Save raw + summary
    # ------------------------------------------------------------
    paths.raw_dir.mkdir(parents=True, exist_ok=True)

    np.savez_compressed(
        paths.raw_dir / f"sweep_{sweep_name}.npz",
        x=np.array(x_vals),
        y=np.array(y_vals),
    )

    summary = {
        "sweep": sweep_name,
        "values": x_vals,
        "residuals": y_vals,
        "n_points": len(x_vals),
        "output_files": {
            "figure": f"figures/{fname}",
            "raw": f"raw/sweep_{sweep_name}.npz",
        },
    }
    write_json(paths.summary_json, summary)


if __name__ == "__main__":
    main()