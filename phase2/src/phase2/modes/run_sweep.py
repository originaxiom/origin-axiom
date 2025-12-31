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


def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
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


def _apply_sweep_value(cfg: Dict[str, Any], *, sweep_name: str, val: float) -> None:
    """Patch a *resolved* config dict in-place for a single sweep value.

    IMPORTANT: Patch the same keys that the model reads.
    See: phase2.modes.mode_model.run_mode_sum()
    """
    if sweep_name == "epsilon":
        # Model reads: model.epsilon.value
        model = cfg.setdefault("model", {})
        eps_block = model.get("epsilon", {})
        if isinstance(eps_block, dict):
            eps_block["value"] = float(val)
            model["epsilon"] = eps_block
        else:
            model["epsilon"] = float(val)

    elif sweep_name == "cutoff":
        # Model reads: mode_sum.cutoff.value
        ms = cfg.setdefault("mode_sum", {})
        cutoff = ms.setdefault("cutoff", {})
        cutoff["value"] = float(val)
        ms["cutoff"] = cutoff

    elif sweep_name == "n_modes":
        # Model reads: mode_sum.n_modes
        ms = cfg.setdefault("mode_sum", {})
        ms["n_modes"] = int(val)

    else:
        raise ValueError(f"Unknown sweep_name: {sweep_name!r}")


def main() -> None:
    args = _parse_args()
    sweep_name = args.sweep
    run_id = str(args.run_id)
    config_path = Path(args.config).resolve()

    # Setup run + provenance
    cfg_raw, paths, meta, repo_root = setup_run(
        config_path=config_path,
        run_id=run_id,
        task=f"sweep_{sweep_name}",
    )

    # Reload frozen config snapshot (resolved, reference-free)
    with paths.params_json.open("r", encoding="utf-8") as f:
        cfg: Dict[str, Any] = json.load(f)

    # Resolve sweep definition
    sweep_cfg = _get_sweep_cfg(cfg, sweep_name)
    sweep_values: List[float] = list(sweep_cfg["values"])

    # Execute sweep
    x_vals: List[float] = []
    y_vals: List[float] = []
    summaries: List[Dict[str, Any]] = []

    for val in sweep_values:
        cfg_local = json.loads(json.dumps(cfg))
        _apply_sweep_value(cfg_local, sweep_name=sweep_name, val=float(val))

        res = run_mode_sum(cfg_local)

        x_vals.append(float(val))
        y_vals.append(float(res.residual_constrained))
        summaries.append(summarize_result(res))

    # Ensure figures/ exists
    paths.fig_dir.mkdir(parents=True, exist_ok=True)

    # Determine canonical filename + labels
    if sweep_name == "epsilon":
        fname = "scaling_epsilon.pdf"
        xlabel = "epsilon (ε)"
        xscale = "log"
    elif sweep_name == "cutoff":
        fname = "scaling_cutoff.pdf"
        xlabel = "cutoff"
        xscale = "linear"
    else:
        fname = "scaling_modes.pdf"
        xlabel = "n_modes"
        xscale = "linear"

    # Plot
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

    # Save raw + summary
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