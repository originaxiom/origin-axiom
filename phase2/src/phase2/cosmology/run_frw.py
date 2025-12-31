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


def _req(cfg: Dict[str, Any], path: str) -> Any:
    cur: Any = cfg
    for part in path.split("."):
        if not isinstance(cur, dict) or part not in cur:
            raise ValueError(f"Missing required config key: '{path}'")
        cur = cur[part]
    return cur


def _req_float(cfg: Dict[str, Any], path: str) -> float:
    v = _req(cfg, path)
    try:
        x = float(v)
    except Exception as e:
        raise ValueError(f"Config key '{path}' must be float-like, got {v!r}") from e
    if not np.isfinite(x):
        raise ValueError(f"Config key '{path}' must be finite, got {x}")
    return x


def _req_int(cfg: Dict[str, Any], path: str) -> int:
    v = _req(cfg, path)
    try:
        x = int(v)
    except Exception as e:
        raise ValueError(f"Config key '{path}' must be int-like, got {v!r}") from e
    return x


def _req_str(cfg: Dict[str, Any], path: str) -> str:
    v = _req(cfg, path)
    if v is None:
        raise ValueError(f"Config key '{path}' must be a string, got None")
    return str(v)


def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Phase 2 FRW wrapper (Fig E).")
    p.add_argument("--config", required=True, help="Path to config/phase2.yaml")
    p.add_argument("--run-id", required=True, help="Run ID (used for outputs/runs/<run_id>/)")
    return p.parse_args()


def _frw_E2(a: np.ndarray, Om: float, Or: float, Ol: float) -> np.ndarray:
    # Flat FRW: E(a)^2 = Ωm a^-3 + Ωr a^-4 + ΩΛ
    return Om * a ** (-3) + Or * a ** (-4) + Ol


def _frw_E(a: np.ndarray, Om: float, Or: float, Ol: float) -> np.ndarray:
    E2 = _frw_E2(a, Om, Or, Ol)
    if not np.all(np.isfinite(E2)) or np.any(E2 <= 0.0):
        raise ValueError("Non-positive or non-finite E(a)^2 encountered; check Ω parameters and a-grid.")
    return np.sqrt(E2)


def _frw_q(a: np.ndarray, Om: float, Or: float, Ol: float) -> np.ndarray:
    # q(a) = (1/(2E^2)) [3Ωm a^-3 + 4Ωr a^-4] - 1
    E2 = _frw_E2(a, Om, Or, Ol)
    num = 0.5 * (3.0 * Om * a ** (-3) + 4.0 * Or * a ** (-4))
    return num / E2 - 1.0


def _integrate_tau(a: np.ndarray, Om: float, Or: float, Ol: float) -> np.ndarray:
    # dτ/da = 1/(aE(a)) ; τ = H0 t (dimensionless)
    E = _frw_E(a, Om, Or, Ol)
    integrand = 1.0 / (a * E)
    tau = np.zeros_like(a, dtype=np.float64)
    for i in range(1, len(a)):
        da = a[i] - a[i - 1]
        tau[i] = tau[i - 1] + 0.5 * da * (integrand[i] + integrand[i - 1])
    return tau


def _save_pdf(fig: plt.Figure, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)


def _flat_closure_check(label: str, Om: float, Or: float, Ol: float, tol: float) -> None:
    s = Om + Or + Ol
    if abs(s - 1.0) > tol:
        raise ValueError(
            f"Flat-FRW closure failed for '{label}': Ωm+Ωr+ΩΛ = {s:.12g} (tol={tol})."
        )


def _first_crossing_a(a: np.ndarray, q: np.ndarray, threshold: float = 0.0) -> float | None:
    """
    Return the first a where q(a) < threshold (strict).
    If no crossing exists, return None.
    """
    mask = np.isfinite(q) & (q < threshold)
    if not np.any(mask):
        return None
    return float(a[np.argmax(mask)])


def main() -> None:
    args = _parse_args()
    config_path = Path(args.config).resolve()
    run_id = str(args.run_id)

    _cfg_raw, paths, _meta, _repo_root = setup_run(
        config_path=config_path,
        run_id=run_id,
        task="frw_comparison",
    )

    # Reload resolved snapshot so the run uses what is recorded
    with paths.params_json.open("r", encoding="utf-8") as f:
        cfg: Dict[str, Any] = json.load(f)

    # Required config (no defaults)
    if not bool(_req(cfg, "cosmology.enabled")):
        raise ValueError("cosmology.enabled must be true for Figure E generation.")

    if _req_str(cfg, "cosmology.model") != "FRW_flat":
        raise ValueError("cosmology.model must be 'FRW_flat' for Phase 2 Figure E.")

    # Interpret Omega_m in config as the OBSERVATIONAL reference matter fraction.
    Om_obs = _req_float(cfg, "cosmology.parameters.Omega_m")
    Or = _req_float(cfg, "cosmology.parameters.Omega_r")
    Ol_obs = _req_float(cfg, "cosmology.comparison.Omega_L_obs")

    vac_src = _req_str(cfg, "cosmology.interpretation.vacuum_energy_source")
    if vac_src != "phase2_residual":
        raise ValueError("cosmology.interpretation.vacuum_energy_source must be 'phase2_residual'.")

    factor = _req_float(cfg, "cosmology.interpretation.residual_to_omega_lambda")
    if factor < 0.0:
        raise ValueError("cosmology.interpretation.residual_to_omega_lambda must be >= 0.")

    cap_mode = _req_str(cfg, "cosmology.interpretation.cap_mode")
    if cap_mode not in ("none", "closure"):
        raise ValueError("cosmology.interpretation.cap_mode must be 'none' or 'closure'.")

    closure_tol = _req_float(cfg, "cosmology.interpretation.flat_closure_tol")
    if closure_tol <= 0.0:
        raise ValueError("cosmology.interpretation.flat_closure_tol must be > 0.")

    a_min = _req_float(cfg, "cosmology.interpretation.a_min")
    a_max = _req_float(cfg, "cosmology.interpretation.a_max")
    n_grid = _req_int(cfg, "cosmology.interpretation.n_grid")
    if not (0.0 < a_min < a_max <= 1.0):
        raise ValueError("Require 0 < a_min < a_max <= 1.0")
    if n_grid < 50:
        raise ValueError("cosmology.interpretation.n_grid must be >= 50")

    # Step 1: compute OA residual
    if not bool(cfg.get("mode_sum", {}).get("enabled", True)):
        raise ValueError("FRW runner expects mode_sum.enabled=true (Phase 2 baseline).")
    res = run_mode_sum(cfg)
    residual = float(res.residual_constrained)

    # Step 2: map residual -> ΩΛ,eff (raw)
    Ol_eff_raw = factor * residual
    if not np.isfinite(Ol_eff_raw):
        raise ValueError("Computed ΩΛ,eff is non-finite; check residual and mapping factor.")
    Ol_eff_raw = max(float(Ol_eff_raw), 0.0)

    # If cap_mode='closure', ΩΛ,eff cannot exceed (1-Ωr) to keep Ωm_eff >= 0 under flatness.
    if cap_mode == "closure":
        cap = 1.0 - Or
        if cap < 0.0:
            raise ValueError("Ωr > 1, cannot enforce flat closure.")
        Ol_eff = min(Ol_eff_raw, cap)
    else:
        Ol_eff = Ol_eff_raw

    # IMPORTANT: For a *flat* OA-effective curve, enforce closure by construction:
    # Ωm_eff = 1 - Ωr - ΩΛ_eff
    Om_eff = 1.0 - Or - Ol_eff
    if Om_eff < 0.0:
        raise ValueError(
            f"Computed Ωm_eff < 0 (Ωm_eff={Om_eff}); increase cap_mode='closure' or reduce mapping factor."
        )

    # Baseline flat curve (Λ=0): Ωm_base = 1 - Ωr
    Om_base = 1.0 - Or
    Ol_base = 0.0

    # Reference observational curve uses (Ωm_obs, Ωr, ΩΛ_obs) as given
    # (still requires flatness; if not, config is inconsistent with FRW_flat scope)
    _flat_closure_check("baseline", Om_base, Or, Ol_base, tol=closure_tol)
    _flat_closure_check("OA_eff", Om_eff, Or, Ol_eff, tol=closure_tol)
    _flat_closure_check("obs_ref", Om_obs, Or, Ol_obs, tol=closure_tol)

    # Step 3: compute curves
    a = np.logspace(np.log10(a_min), np.log10(a_max), n_grid)

    E_base = _frw_E(a, Om_base, Or, Ol_base)
    q_base = _frw_q(a, Om_base, Or, Ol_base)
    tau_base = _integrate_tau(a, Om_base, Or, Ol_base)

    E_eff = _frw_E(a, Om_eff, Or, Ol_eff)
    q_eff = _frw_q(a, Om_eff, Or, Ol_eff)
    tau_eff = _integrate_tau(a, Om_eff, Or, Ol_eff)

    E_obs = _frw_E(a, Om_obs, Or, Ol_obs)
    q_obs = _frw_q(a, Om_obs, Or, Ol_obs)
    tau_obs = _integrate_tau(a, Om_obs, Or, Ol_obs)

    # ---- Numerical acceleration markers (drift-free Claim 2.3 checks) ----
    q_at_a_max = {
        "baseline": float(q_base[-1]),
        "OA_eff": float(q_eff[-1]),
        "obs_ref": float(q_obs[-1]),
    }
    a_first_q_lt_0 = {
        "baseline": _first_crossing_a(a, q_base, threshold=0.0),
        "OA_eff": _first_crossing_a(a, q_eff, threshold=0.0),
        "obs_ref": _first_crossing_a(a, q_obs, threshold=0.0),
    }
    accelerates_by_a_max = {
        "baseline": bool(q_base[-1] < 0.0),
        "OA_eff": bool(q_eff[-1] < 0.0),
        "obs_ref": bool(q_obs[-1] < 0.0),
    }

    # Save raw
    paths.raw_dir.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(
        paths.raw_dir / "frw_timeseries.npz",
        a=a,
        E_base=E_base, q_base=q_base, tau_base=tau_base,
        E_eff=E_eff, q_eff=q_eff, tau_eff=tau_eff,
        E_obs=E_obs, q_obs=q_obs, tau_obs=tau_obs,
        residual_constrained=np.float64(residual),
        Omega_r=np.float64(Or),
        Omega_m_obs=np.float64(Om_obs),
        Omega_L_obs=np.float64(Ol_obs),
        Omega_m_eff=np.float64(Om_eff),
        Omega_L_eff=np.float64(Ol_eff),
        Omega_m_base=np.float64(Om_base),
        Omega_L_base=np.float64(Ol_base),
        residual_to_omega_lambda=np.float64(factor),
        cap_mode=np.array([cap_mode]),
        constraint_applied=np.bool_(res.constraint.applied),
        q_at_a_max=json.dumps(q_at_a_max),
        a_first_q_lt_0=json.dumps(a_first_q_lt_0),
        accelerates_by_a_max=json.dumps(accelerates_by_a_max),
    )

    # Plot Fig E
    fig, axes = plt.subplots(2, 1, figsize=(7.2, 7.2), sharex=True)

    axes[0].plot(a, E_base, label="baseline (flat, ΩΛ=0)")
    axes[0].plot(a, E_eff, label="OA residual → ΩΛ,eff (flat closure)")
    axes[0].plot(a, E_obs, label="reference (ΩΛ,obs)")
    axes[0].set_ylabel("H/H0 = E(a)")
    axes[0].set_title("FRW response to OA residual (standard FRW; explicit mapping)")
    axes[0].grid(True, alpha=0.3)
    axes[0].legend(loc="best")

    axes[1].plot(a, q_base, label="baseline (flat, ΩΛ=0)")
    axes[1].plot(a, q_eff, label="OA residual → ΩΛ,eff (flat closure)")
    axes[1].plot(a, q_obs, label="reference (ΩΛ,obs)")
    axes[1].axhline(0.0, linewidth=1.0)
    axes[1].set_ylabel("q(a)")
    axes[1].set_xlabel("scale factor a")
    axes[1].set_xscale("log")
    axes[1].grid(True, alpha=0.3)
    axes[1].legend(loc="best")

    meta_txt = (
        f"Ωr={Or:.6g}\n"
        f"residual_constrained={residual:.6g}\n"
        f"factor(residual→ΩΛ)={factor:.6g}\n"
        f"cap_mode={cap_mode}\n"
        f"ΩΛ,eff={Ol_eff:.6g}\n"
        f"Ωm,eff={Om_eff:.6g}\n"
        f"Ωm,obs={Om_obs:.6g}\n"
        f"ΩΛ,obs={Ol_obs:.6g}\n"
        f"q(a_max) OA_eff={q_at_a_max['OA_eff']:.6g}\n"
        f"constraint_applied={bool(res.constraint.applied)}"
    )
    axes[0].text(1.02, 0.5, meta_txt, transform=axes[0].transAxes, va="center", ha="left", fontsize=9)

    out_fig = paths.fig_dir / "frw_comparison.pdf"
    _save_pdf(fig, out_fig)

    # summary.json
    summary = {
        "residual_constrained": residual,
        "constraint_applied": bool(res.constraint.applied),
        "Omega_r": Or,
        "Omega_m_obs": Om_obs,
        "Omega_L_obs": Ol_obs,
        "Omega_m_eff": Om_eff,
        "Omega_L_eff": Ol_eff,
        "Omega_m_base": Om_base,
        "Omega_L_base": Ol_base,
        "residual_to_omega_lambda": factor,
        "cap_mode": cap_mode,
        "flat_closure_tol": closure_tol,
        "a_grid": {"a_min": a_min, "a_max": a_max, "n_grid": n_grid},
        "q_at_a_max": q_at_a_max,
        "a_first_q_lt_0": a_first_q_lt_0,
        "accelerates_by_a_max": accelerates_by_a_max,
        "output_files": {
            "figure": "figures/frw_comparison.pdf",
            "raw": "raw/frw_timeseries.npz",
        },
    }
    write_json(paths.summary_json, summary)


if __name__ == "__main__":
    main()