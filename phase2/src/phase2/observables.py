from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Optional

import matplotlib
matplotlib.use("Agg")  # headless / CI-safe
import matplotlib.pyplot as plt
import numpy as np

from phase2.modes.mode_model import ModeSumResult

# ============================================================
# Origin Axiom — Phase 2
# Observables + plotting helpers (per-run artifacts)
#
# Design rules:
# - Pure summarization helpers return JSON-serializable dicts.
# - Plotting helpers ONLY write into the per-run figures/ directory.
# - Canonical figures in outputs/figures/ are produced by Snakemake
#   as copies from per-run figures (reproducibility contract).
# ============================================================


def _save_pdf(fig: plt.Figure, path: Path) -> None:
    """Save a matplotlib Figure to PDF and close it."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(str(path), format="pdf", bbox_inches="tight")
    plt.close(fig)


def plot_mode_sum_residual(res: ModeSumResult, run_fig_dir: Path) -> Dict[str, str]:
    """
    FIGURE (per-run): residual before/after constraint, plus cancellation ratios.

    Writes:
      <run>/figures/residual.pdf

    Returns:
      {"residual": "residual.pdf"}  (relative to run_fig_dir)
    """
    run_fig_dir.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(6.2, 3.6))

    labels = ["raw", "constrained"]
    vals = [float(res.residual_raw), float(res.residual_constrained)]

    ax.bar(labels, vals)
    ax.set_title("Mode-sum residual (code units)")
    ax.set_ylabel("|A| (proxy residual)")
    ax.grid(True, axis="y", alpha=0.3)

    # Phase-1 style metadata block
    meta_txt = (
        f"n_modes={res.inputs.n_modes}\n"
        f"cutoff={res.inputs.cutoff_type}:{res.inputs.cutoff_value}\n"
        f"epsilon={res.inputs.epsilon:.3e}\n"
        f"phase={res.inputs.phase_type}:{res.inputs.phase_value}\n"
        f"cancel_ratio_raw={res.cancellation_ratio_raw:.3e}\n"
        f"cancel_ratio_con={res.cancellation_ratio_constrained:.3e}\n"
        f"constraint_applied={bool(res.constraint.applied)}"
    )
    ax.text(
        1.02, 0.5, meta_txt,
        transform=ax.transAxes,
        va="center",
        ha="left",
        fontsize=9,
    )

    out = run_fig_dir / "residual.pdf"
    _save_pdf(fig, out)
    return {"residual": "residual.pdf"}


def plot_scaling_curve(
    *,
    x: List[float],
    y: List[float],
    xlabel: str,
    ylabel: str,
    title: str,
    run_fig_dir: Path,
    filename: str,
    xscale: Optional[str] = None,
    yscale: Optional[str] = None,
    annotate: Optional[str] = None,
) -> Dict[str, str]:
    """
    Generic scaling plot for sweeps.

    Parameters:
      x, y: lists of numeric values (same length)
      xlabel, ylabel, title: axis/title strings
      run_fig_dir: per-run figures dir
      filename: output PDF filename (e.g., "scaling_cutoff.pdf")
      xscale/yscale: "linear" or "log" (or None to leave default)
      annotate: optional text block drawn to the right (Phase-1 style)

    Writes:
      <run>/figures/<filename>

    Returns:
      {"scaling": "<filename>"}  (relative to run_fig_dir)
    """
    if len(x) != len(y):
        raise ValueError(f"x and y must have the same length (got {len(x)} vs {len(y)})")
    if len(x) < 2:
        raise RuntimeError(f"Not enough valid sweep points to plot (valid={len(x)})")

    run_fig_dir.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(6.2, 3.6))
    ax.plot(x, y, marker="o", linestyle="-")

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True, alpha=0.3)

    if xscale is not None:
        ax.set_xscale(xscale)
    if yscale is not None:
        ax.set_yscale(yscale)

    if annotate:
        ax.text(
            1.02, 0.5, annotate,
            transform=ax.transAxes,
            va="center",
            ha="left",
            fontsize=9,
        )

    out = run_fig_dir / filename
    _save_pdf(fig, out)
    return {"scaling": filename}


def summarize_result(res: ModeSumResult) -> Dict[str, Any]:
    """
    Flatten key fields for table-like export / summaries.

    Contract:
      - JSON-serializable
      - stable keys (avoid churn)
      - no I/O
    """
    # Use np.real/np.imag to be robust if amplitude becomes np.complex types.
    return {
        "n_modes": int(res.inputs.n_modes),
        "cutoff_type": str(res.inputs.cutoff_type),
        "cutoff_value": float(res.inputs.cutoff_value),
        "epsilon": float(res.inputs.epsilon),
        "phase_type": str(res.inputs.phase_type),
        "phase_value": str(res.inputs.phase_value),
        "constraint_applied": bool(res.constraint.applied),
        "residual_raw": float(res.residual_raw),
        "residual_constrained": float(res.residual_constrained),
        "cancellation_ratio_raw": float(res.cancellation_ratio_raw),
        "cancellation_ratio_constrained": float(res.cancellation_ratio_constrained),
        "amplitude_raw_re": float(np.real(res.amplitude_raw)),
        "amplitude_raw_im": float(np.imag(res.amplitude_raw)),
        "amplitude_con_re": float(np.real(res.amplitude_constrained)),
        "amplitude_con_im": float(np.imag(res.amplitude_constrained)),
    }