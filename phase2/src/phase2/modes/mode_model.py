from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Any, Dict

import numpy as np

from phase2.modes.constraints import ConstraintActivity, enforce_global_floor

# ============================================================
# Origin Axiom — Phase 2
# Mode-sum (QFT-inspired) toy model
#
# This module intentionally keeps the "physics" minimal:
# - Paired contributions that would cancel in an idealized limit
# - A generic interference phase that prevents perfect cancellation
# - A global non-cancellation floor enforced by the Origin Axiom
#
# All quantities here are in *code units*. Any mapping to physical
# units must happen explicitly in calibration/cosmology layers.
# ============================================================


# ============================================================
# Data structures
# ============================================================

@dataclass(frozen=True)
class ModeSumInputs:
    seed: int
    n_modes: int
    cutoff_value: float
    cutoff_type: str
    epsilon: float
    phase_type: str
    phase_value: str


@dataclass(frozen=True)
class ModeSumResult:
    inputs: ModeSumInputs

    # Raw global amplitude (pre-constraint) and corrected amplitude (post-constraint)
    amplitude_raw: complex
    amplitude_constrained: complex
    constraint: ConstraintActivity

    # Proxy residual in code units (conservative choice: |A|)
    residual_raw: float
    residual_constrained: float

    # Diagnostics: fraction of "would-be large" scale remaining after cancellation
    cancellation_ratio_raw: float
    cancellation_ratio_constrained: float


# ============================================================
# Phase parameterization
# ============================================================

def _phi_from_label(label: str) -> float:
    """
    Convert a symbolic phase label to a numeric angle (radians).
    This mapping is *explicitly a model choice* and must be documented.

    Supported labels:
      - golden_ratio
      - sqrt2
      - numeric strings (interpreted as radians, reduced mod 2π)
    """
    if label == "golden_ratio":
        gr = (1.0 + math.sqrt(5.0)) / 2.0
        return float((2.0 * math.pi) * (gr % 1.0))
    if label == "sqrt2":
        return float((2.0 * math.pi) * ((math.sqrt(2.0)) % 1.0))

    # Allow numeric strings like "1.2345"
    try:
        x = float(label)
        return float(x % (2.0 * math.pi))
    except Exception as e:
        raise ValueError(f"Unknown phase label/value: {label}") from e


def get_phase_angle(*, phase_type: str, phase_value: str, rng: np.random.Generator) -> float:
    """
    Produce a phase angle φ in radians.

    phase.type:
      - "irrational_fixed": uses a label mapping (golden_ratio, sqrt2, etc.)
      - "rational": expects "p/q" (integers); uses 2π * (p/q mod 1)
      - "random": uniform φ ~ U(0, 2π)

    Note: In Phase 2 we do not claim a microscopic origin for φ.
    """
    if phase_type == "irrational_fixed":
        return _phi_from_label(phase_value)

    if phase_type == "rational":
        if "/" in phase_value:
            p, q = phase_value.split("/", 1)
            p_i = int(p.strip())
            q_i = int(q.strip())
            if q_i == 0:
                raise ValueError("rational phase q cannot be 0")
            frac = (p_i / q_i) % 1.0
            return float(2.0 * math.pi * frac)
        # also allow numeric radians here
        return float(float(phase_value) % (2.0 * math.pi))

    if phase_type == "random":
        return float(rng.uniform(0.0, 2.0 * math.pi))

    raise ValueError(f"Unsupported phase.type: {phase_type}")


# ============================================================
# Cutoff weighting
# ============================================================

def cutoff_weights(k: np.ndarray, cutoff_value: float, cutoff_type: str) -> np.ndarray:
    """
    UV cutoff envelope over mode index k (proxy momentum/frequency index).

    cutoff.type:
      - "sharp": w = 1 for k <= Λ, else 0
      - "smooth": w = exp(-(k/Λ)^2)

    NOTE: cutoff_value is expressed in the same units as k (here: mode index).
    """
    if cutoff_value <= 0.0 or not np.isfinite(cutoff_value):
        raise ValueError(f"cutoff_value must be positive finite, got {cutoff_value}")

    x = k / cutoff_value

    if cutoff_type == "sharp":
        return (x <= 1.0).astype(np.float64)

    if cutoff_type == "smooth":
        return np.exp(-(x ** 2))

    raise ValueError(f"Unsupported cutoff.type: {cutoff_type}")


# ============================================================
# Core model
# ============================================================

def run_mode_sum(cfg_resolved: Dict[str, Any]) -> ModeSumResult:
    """
    Mode-sum toy model approximating QFT vacuum energy structure:

      1) Construct a set of mode indices k = 1..n_modes
      2) Assign proxy frequencies ω_k (here: ω_k = k)
      3) Apply a UV envelope w_k via cutoff
      4) Form paired "mismatch" contributions with a phase φ:
            mismatch_k = w_k * ω_k * (1 - e^{iφ})
         so φ -> 0 produces near-cancellation, while generic φ prevents exact cancellation.
      5) Sum to a global complex amplitude:
            A = Σ mismatch_k
      6) Enforce the Origin Axiom global floor:
            |A| >= ε
      7) Report residual proxies:
            residual := |A|
            cancellation_ratio := |A| / Σ |w_k ω_k|

    IMPORTANT:
    - residual_* are in *code units* and represent a conservative proxy.
    - physical mapping is handled elsewhere.
    """
    # -----------------------------
    # Read config (explicit only)
    # -----------------------------
    g = cfg_resolved.get("global", {})
    ms = cfg_resolved.get("mode_sum", {})
    model = cfg_resolved.get("model", {})

    seed = int(g.get("seed", 0))
    rng = np.random.default_rng(seed)

    n_modes = int(ms.get("n_modes", 2048))
    if n_modes <= 0:
        raise ValueError(f"mode_sum.n_modes must be positive, got {n_modes}")

    cutoff = ms.get("cutoff", {})
    cutoff_value = float(cutoff.get("value", 1.0))
    cutoff_type = str(cutoff.get("type", "sharp"))

    # epsilon: prefer model.epsilon.value, fallback to model.epsilon if flattened
    eps_block = model.get("epsilon", {})
    if isinstance(eps_block, dict):
        epsilon = float(eps_block.get("value", 1e-12))
    else:
        epsilon = float(model.get("epsilon", 1e-12))

    if epsilon <= 0.0 or not np.isfinite(epsilon):
        raise ValueError(f"epsilon must be positive finite, got {epsilon}")

    phase = ms.get("phase", {})
    phase_type = str(phase.get("type", "irrational_fixed"))
    phase_value = str(phase.get("value", "golden_ratio"))
    phi = get_phase_angle(phase_type=phase_type, phase_value=phase_value, rng=rng)

    # -----------------------------
    # Build mode sum
    # -----------------------------
    k = np.arange(1, n_modes + 1, dtype=np.float64)
    omega = k  # simple proxy; keep explicit

    w = cutoff_weights(k, cutoff_value=cutoff_value, cutoff_type=cutoff_type)

    # mismatch term: complex, same phase for all modes (minimal baseline)
    mismatch = w * omega * (1.0 - np.exp(1j * phi))

    A_raw = complex(np.sum(mismatch))

    # Apply Origin Axiom global floor (acts on complex amplitude)
    A_con, activity = enforce_global_floor(A_raw, epsilon=epsilon, rng=rng)

    residual_raw = float(abs(A_raw))
    residual_con = float(abs(A_con))

    denom = float(np.sum(np.abs(w * omega)))
    if denom <= 0.0:
        # This is an invalid region (e.g., cutoff_value < 1 for sharp cutoff with k>=1)
        raise ValueError("Cutoff eliminated all modes; denom is 0")

    cancel_ratio_raw = float(residual_raw / denom)
    cancel_ratio_con = float(residual_con / denom)

    inputs = ModeSumInputs(
        seed=seed,
        n_modes=n_modes,
        cutoff_value=cutoff_value,
        cutoff_type=cutoff_type,
        epsilon=epsilon,
        phase_type=phase_type,
        phase_value=phase_value,
    )

    return ModeSumResult(
        inputs=inputs,
        amplitude_raw=A_raw,
        amplitude_constrained=A_con,
        constraint=activity,
        residual_raw=residual_raw,
        residual_constrained=residual_con,
        cancellation_ratio_raw=cancel_ratio_raw,
        cancellation_ratio_constrained=cancel_ratio_con,
    )


# ============================================================
# Serialization
# ============================================================

def to_summary_dict(res: ModeSumResult) -> Dict[str, Any]:
    """
    Minimal machine-readable summary for run summary.json.
    Keep this stable: it is part of the reproducibility contract.
    """
    def _c(z: complex) -> Dict[str, float]:
        return {"re": float(z.real), "im": float(z.imag)}

    return {
        "inputs": {
            "seed": int(res.inputs.seed),
            "n_modes": int(res.inputs.n_modes),
            "cutoff": {"type": str(res.inputs.cutoff_type), "value": float(res.inputs.cutoff_value)},
            "epsilon": float(res.inputs.epsilon),
            "phase": {"type": str(res.inputs.phase_type), "value": str(res.inputs.phase_value)},
        },
        "amplitude": {
            "raw": _c(res.amplitude_raw),
            "constrained": _c(res.amplitude_constrained),
        },
        "constraint": {
            "applied": bool(res.constraint.applied),
            "epsilon": float(res.constraint.epsilon),
            "magnitude_before": float(res.constraint.magnitude_before),
            "magnitude_after": float(res.constraint.magnitude_after),
            "delta_magnitude": float(res.constraint.delta_magnitude),
            "direction_source": str(res.constraint.direction_source),
        },
        "residual": {
            "raw": float(res.residual_raw),
            "constrained": float(res.residual_constrained),
        },
        "cancellation_ratio": {
            "raw": float(res.cancellation_ratio_raw),
            "constrained": float(res.cancellation_ratio_constrained),
        },
    }