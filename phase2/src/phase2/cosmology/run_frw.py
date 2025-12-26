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
from phase2.modes.mode_model import run_mode_sum


# ============================================================
# Origin Axiom — Phase 2
# FRW wrapper (Figure E): interpret OA residual as effective ΩΛ and compare expansion.
#
# Produces (per-run):
#   outputs/runs/<run_id>/
#     meta.json, params.json, summary.json, pip_freeze.txt
#     raw/frw_timeseries.npz
#     figures/frw_comparison.pdf
#
# Canonical figure is copied by Snakemake into outputs/figures/figE_frw_comparison.pdf
# ============================================================


def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Phase 2 FRW wrapper (Fig E).")
    p.add_argument("--config", required=True, help="Path to config/phase2.yaml")
    p.add_argument("--run-id", required=True, help="Run ID: figE_frw_comparison_YYYYMMDDTHHMMSSZ")
    return p.parse_args()


def _E_of_a(a: np.ndarray, Om: float, Or: float, Ol: float) -> np.ndarray:
    # Flat FRW: E(a) = H/H0 = sqrt(Ωm a^-3 + Ωr a^-4 + ΩΛ)
    return np.sqrt(Om * a ** (-3) + Or * a ** (-4) + Ol)


def _q_of_a(a: np.ndarray, Om: float, Or: float, Ol: float) -> np.ndarray:
    """
    Deceleration parameter q(a) = - (a \ddot{a}) / \dot{a}^2 for flat FRW with:
      matter (w=0), radiation (w=1/3), vacuum (w=-1)

      q(a) = [ 0.5 Ωm a^-3 + 1.0 Ωr a^-4 - 1.0 ΩΛ ] / E(a)^2
    """
    E2 = Om * a ** (-3) + Or * a ** (-4) + Ol
    num = 0.5 * Om * a ** (-3) + 1.0 * Or * a ** (-4) - 1.0 * Ol
    return num / E2


def _integrate_tau(a_grid: np.ndarray, Om: float, Or: float, Ol: float) -> np.ndarray:
    """
    Dimensionless time τ = H0 t:
      dτ/da = 1 / (a E(a))
    """
    E = _E_of_a(a_grid, Om, Or, Ol)
    if not np.all(np.isfinite(E)) or np.any(E <= 0.0):
        raise ValueError("E(a) must be finite and positive on the integration grid.")

    dtau_da = 1.0 / (a_grid * E)

    tau = np.zeros_like(a_grid)
    da = np.diff(a_grid)
    tau[1:] = np.cumsum(0.5 * (dtau_da[:-1] + dtau_da[1:]) * da)
    return tau


def _save_pdf(fig: plt.Figure, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(str(path), format="pdf", bbox_inches="tight")
    plt.close(fig)


def _clamp(x: float, lo: float, hi: float) -> float:
    return float(min(max(x, lo), hi))


def main() -> None:
    args = _parse_args()
    config_path = Path(args.config).resolve()
    run_id = str(args.run_id)

    # Setup run dir + provenance
    cfg_raw, paths, meta, repo_root = setup_run(
        config_path=config_path,
        run_id=run_id,
        task="frw_comparison",
    )

    # Reload resolved config snapshot (ensures run uses recorded params)
    with paths.params_json.open("r", encoding="utf-8") as f:
        cfg: Dict[str, Any] = json.load(f)

    # ------------------------------------------------------------
    # Step 1: compute OA residual (self-contained, baseline uses mode_sum)
    # ------------------------------------------------------------
    if not cfg.get("mode_sum", {}).get("enabled", True):
        raise ValueError("FRW runner expects mode_sum.enabled=true for Phase 2 baseline.")

    res = run_mode_sum(cfg)
    residual = float(res.residual_constrained)

    # ------------------------------------------------------------
    # Step 2: map residual -> ΩΛ,eff (explicit knob, no hidden calibration)
    # ------------------------------------------------------------
    cosmo = cfg.get("cosmology", {})
    params = cosmo.get("parameters", {})
    interp = cosmo.get("interpretation", {})

    Om = float(params.get("Omega_m", 0.3))
    Or = float(params.get("Omega_r", 0.0))

    # Optional external comparison curve ("ΛCDM-like") via ΩΛ,obs
    comp = cosmo.get("comparison", {})
    Ol_obs = comp.get("Omega_L_obs", None)
    if Ol_obs is None:
        # If not provided, default to flat closure (clamped for safety)
        Ol_obs_val = _clamp(1.0 - Om - Or, 0.0, 2.0)
    else:
        Ol_obs_val = _clamp(float(Ol_obs), 0.0, 2.0)

    # OA mapping knob (dimensionless): ΩΛ,eff = factor * residual
    factor = float(interp.get("residual_to_omega_lambda", 0.01))
    if factor < 0.0 or not np.isfinite(factor):
        raise ValueError("cosmology.interpretation.residual_to_omega_lambda must be finite and >= 0")

    Ol_eff = _clamp(factor * residual, 0.0, 2.0)

    # Baseline: matter+radiation only (ΩΛ=0) to show acceleration clearly
    Ol_base = 0.0

    # ------------------------------------------------------------
    # Step 3: compute FRW curves on an a-grid
    # ------------------------------------------------------------
    a_min = float(interp.get("a_min", 1e-3))
    a_max = float(interp.get("a_max", 1.0))
    n_grid = int(interp.get("n_grid", 2000))

    if not (0.0 < a_min < a_max):
        raise ValueError("Invalid a-grid: require 0 < a_min < a_max")
    if n_grid < 50:
        raise ValueError("n_grid too small; require >= 50")

    a = np.geomspace(a_min, a_max, n_grid)

    E_base = _E_of_a(a, Om, Or, Ol_base)
    E_eff = _E_of_a(a, Om, Or, Ol_eff)
    E_obs = _E_of_a(a, Om, Or, Ol_obs_val)

    q_base = _q_of_a(a, Om, Or, Ol_base)
    q_eff = _q_of_a(a, Om, Or, Ol_eff)
    q_obs = _q_of_a(a, Om, Or, Ol_obs_val)

    tau_base = _integrate_tau(a, Om, Or, Ol_base)
    tau_eff = _integrate_tau(a, Om, Or, Ol_eff)
    tau_obs = _integrate_tau(a, Om, Or, Ol_obs_val)

    # ------------------------------------------------------------
    # Step 4: save raw time series (audit)
    # ------------------------------------------------------------
    paths.raw_dir.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(
        paths.raw_dir / "frw_timeseries.npz",
        a=a,
        E_base=E_base,
        E_eff=E_eff,
        E_obs=E_obs,
        q_base=q_base,
        q_eff=q_eff,
        q_obs=q_obs,
        tau_base=tau_base,
        tau_eff=tau_eff,
        tau_obs=tau_obs,
        Omega_m=np.float64(Om),
        Omega_r=np.float64(Or),
        Omega_L_base=np.float64(Ol_base),
        Omega_L_eff=np.float64(Ol_eff),
        Omega_L_obs=np.float64(Ol_obs_val),
        residual_constrained=np.float64(residual),
        residual_to_omega_lambda=np.float64(factor),
        constraint_applied=np.bool_(res.constraint.applied),
    )

    # ------------------------------------------------------------
    # Step 5: plot Fig E (single PDF, 2 panels; reviewer-friendly)
    # ------------------------------------------------------------
    fig, axes = plt.subplots(2, 1, figsize=(7.2, 7.2), sharex=True)

    # Panel 1: H/H0 = E(a)
    axes[0].plot(a, E_base, label="baseline (ΩΛ=0)")
    axes[0].plot(a, E_eff, label="OA residual → ΩΛ,eff")
    axes[0].plot(a, E_obs, label="reference ΩΛ,obs")
    axes[0].set_ylabel("H/H0")
    axes[0].set_title("FRW response to OA residual (flat FRW; explicit code-unit mapping)")
    axes[0].grid(True, alpha=0.3)
    axes[0].legend(loc="best")

    # Panel 2: q(a)
    axes[1].plot(a, q_base, label="baseline (ΩΛ=0)")
    axes[1].plot(a, q_eff, label="OA residual → ΩΛ,eff")
    axes[1].plot(a, q_obs, label="reference ΩΛ,obs")
    axes[1].axhline(0.0, linewidth=1.0)
    axes[1].set_ylabel("q(a)")
    axes[1].set_xlabel("scale factor a")
    axes[1].set_xscale("log")
    axes[1].grid(True, alpha=0.3)
    axes[1].legend(loc="best")

    # Metadata block (Phase-1 style)
    meta_txt = (
        f"Ωm={Om:.3f}, Ωr={Or:.3f}\n"
        f"residual_constrained={residual:.6g}\n"
        f"factor(residual→ΩΛ)={factor:.6g}\n"
        f"ΩΛ,eff={Ol_eff:.6g}\n"
        f"ΩΛ,obs={Ol_obs_val:.6g}\n"
        f"constraint_applied={bool(res.constraint.applied)}"
    )
    axes[0].text(
        1.02, 0.5, meta_txt,
        transform=axes[0].transAxes,
        va="center", ha="left", fontsize=9
    )

    out_fig = paths.fig_dir / "frw_comparison.pdf"
    _save_pdf(fig, out_fig)

    # ------------------------------------------------------------
    # Step 6: summary.json (stable + explicit mapping)
    # ------------------------------------------------------------
    summary = {
        "residual_constrained": residual,
        "constraint_applied": bool(res.constraint.applied),
        "Omega_m": Om,
        "Omega_r": Or,
        "Omega_L_eff": Ol_eff,
        "Omega_L_obs": Ol_obs_val,
        "Omega_L_base": Ol_base,
        "residual_to_omega_lambda": factor,
        "a_grid": {"a_min": a_min, "a_max": a_max, "n_grid": n_grid},
        "output_files": {
            "figure": "figures/frw_comparison.pdf",
            "raw": "raw/frw_timeseries.npz",
        },
    }
    write_json(paths.summary_json, summary)


if __name__ == "__main__":
    main()