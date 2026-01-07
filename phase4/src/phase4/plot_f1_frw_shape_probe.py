#!/usr/bin/env python3
"""
Phase 4: F1/FRW shape-probe summary figure.

Reads the joined mask
  phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv
and produces a θ vs Ω_Λ scatter plot highlighting:
- all grid points;
- FRW-viable points;
- ΛCDM-like points;
- points that are both in the toy F1 corridor and ΛCDM-like.

Outputs a PNG into:
  phase4/outputs/figures/phase4_F1_frw_shape_probe_omega_lambda_vs_theta.png
"""

import csv
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def get_phase4_root() -> Path:
    # This file lives in phase4/src/phase4/, so parents[2] = phase4/
    return Path(__file__).resolve().parents[2]


def load_shape_probe_mask(path: Path):
    rows = []
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(r)

    if not rows:
        raise RuntimeError(f"[plot_f1_frw_shape_probe] No rows found in {path}")

    theta = np.array([float(r["theta"]) for r in rows])
    omega_lambda = np.array([float(r["omega_lambda"]) for r in rows])

    def to_bool_array(col: str):
        return np.array([bool(int(r[col])) for r in rows], dtype=bool)

    in_toy_corridor = to_bool_array("in_toy_corridor")
    frw_viable = to_bool_array("frw_viable")
    lcdm_like = to_bool_array("lcdm_like")

    # Composite sets (should match the columns in the CSV, but we recompute for safety)
    shape_and_viable = in_toy_corridor & frw_viable
    shape_and_lcdm = in_toy_corridor & lcdm_like

    return {
        "theta": theta,
        "omega_lambda": omega_lambda,
        "in_toy_corridor": in_toy_corridor,
        "frw_viable": frw_viable,
        "lcdm_like": lcdm_like,
        "shape_and_viable": shape_and_viable,
        "shape_and_lcdm": shape_and_lcdm,
    }


def main():
    phase4_root = get_phase4_root()
    tables_dir = phase4_root / "outputs" / "tables"
    fig_dir = phase4_root / "outputs" / "figures"
    fig_dir.mkdir(parents=True, exist_ok=True)

    mask_path = tables_dir / "phase4_F1_frw_shape_probe_mask.csv"
    if not mask_path.is_file():
        raise FileNotFoundError(
            f"[plot_f1_frw_shape_probe] Missing joined mask: {mask_path}"
        )

    data = load_shape_probe_mask(mask_path)
    theta = data["theta"]
    omega_lambda = data["omega_lambda"]
    frw_viable = data["frw_viable"]
    lcdm_like = data["lcdm_like"]
    shape_and_lcdm = data["shape_and_lcdm"]

    plt.figure(figsize=(7, 4))

    # All points (faint background)
    plt.scatter(theta, omega_lambda, s=6, alpha=0.15, label="all grid points")

    # FRW-viable
    plt.scatter(
        theta[frw_viable],
        omega_lambda[frw_viable],
        s=8,
        alpha=0.4,
        label="FRW-viable",
    )

    # ΛCDM-like (subset of FRW-viable)
    plt.scatter(
        theta[lcdm_like],
        omega_lambda[lcdm_like],
        s=18,
        alpha=0.9,
        label=r"$\Lambda$CDM-like",
    )

    # Intersection: toy corridor ∧ ΛCDM-like
    if np.any(shape_and_lcdm):
        plt.scatter(
            theta[shape_and_lcdm],
            omega_lambda[shape_and_lcdm],
            s=40,
            facecolors="none",
            edgecolors="k",
            linewidths=1.0,
            label=r"F1-corridor $\cap$ $\Lambda$CDM-like",
        )

    plt.xlabel(r"$\theta$")
    plt.ylabel(r"$\Omega_\Lambda(\theta)$ (toy units)")
    plt.title("Phase 4 F1/FRW shape-probe: $\Omega_\Lambda(\\theta)$ vs $\\theta$")
    plt.grid(True, alpha=0.2)
    plt.legend(loc="best", fontsize=8)

    out_path = fig_dir / "phase4_F1_frw_shape_probe_omega_lambda_vs_theta.png"
    plt.tight_layout()
    plt.savefig(out_path, dpi=200)
    plt.close()

    print("[plot_f1_frw_shape_probe] Wrote figure to", out_path)


if __name__ == "__main__":
    main()
