"""
model_1d_chain.py

θ*-agnostic 1D "cancellation chain" utilities.

Idea:
- We consider a 1D chain of N "sites".
- Each site carries an integer "charge" q_j in [-max_charge, max_charge].
- We enforce (optionally) a global constraint sum_j q_j = 0
  (so there is no trivial net bias).
- A phase is assigned to each site as

      θ_j = q_j * theta + noise_j,

  where theta is a free parameter (candidate θ*), and noise_j ~ N(0, noise_sigma).

- We define the complex amplitude

      S = Σ_j e^{i θ_j},

  and use |S| as a measure of "how well the chain cancels to zero" given
  this discrete integer structure.

This is meant as a *simple probe* of the non-cancelling principle:
  - For truly random phases (no structure), |S| ~ O(sqrt(N)).
  - For special θ and constrained charges, the scaling and residual pattern
    might deviate from the random baseline.

We deliberately keep this GENERAL and θ-agnostic. No φ is hard-coded.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, asdict
from typing import Dict, Any, Tuple

import numpy as np


@dataclass
class ChainConfig:
    """
    Configuration for a single chain draw.

    Attributes
    ----------
    N : int
        Number of sites in the chain.
    theta : float
        Phase step per unit charge (our candidate θ).
    max_charge : int
        Max |q_j| allowed. Charges live in [-max_charge, +max_charge].
    noise_sigma : float
        Standard deviation of Gaussian phase noise added to each θ_j.
        If 0, phases are perfectly locked to q_j * theta.
    enforce_zero_sum : bool
        If True, construct charges so that sum_j q_j = 0 exactly.
    seed : int | None
        Optional RNG seed for reproducibility.
    """
    N: int = 32
    theta: float = 2.0
    max_charge: int = 5
    noise_sigma: float = 0.0
    enforce_zero_sum: bool = True
    seed: int | None = None


def _make_rng(seed: int | None) -> np.random.Generator:
    if seed is None:
        return np.random.default_rng()
    return np.random.default_rng(seed)


def draw_charges(cfg: ChainConfig) -> np.ndarray:
    """
    Draw an integer charge vector q_j with optional global sum=0 constraint.

    Strategy if enforce_zero_sum=True:
      - Start from q = 0
      - Perform a random walk in charge space by repeatedly choosing (i, j)
        and moving one unit of charge from j to i, respecting bounds.
      - This guarantees sum q_j = 0 at all times.

    This is NOT unique or physically canonical, it's just a simple,
    reproducible way to generate a nontrivial integer structure with sum=0.
    """
    N = cfg.N
    max_q = cfg.max_charge
    rng = _make_rng(cfg.seed)

    if max_q <= 0:
        # Trivial case: all charges zero
        return np.zeros(N, dtype=int)

    if not cfg.enforce_zero_sum:
        # Independent uniform charges in [-max_q, max_q]
        return rng.integers(-max_q, max_q + 1, size=N, dtype=int)

    # Enforce sum_j q_j = 0 with a random walk in charge space
    q = np.zeros(N, dtype=int)
    # Number of random-walk steps: heuristic
    steps = max(N * max_q * 5, 10)

    for _ in range(steps):
        i = rng.integers(0, N)
        j = rng.integers(0, N)
        if i == j:
            continue

        # Decide randomly to move +1 from j to i or -1 from j to i
        direction = rng.choice([-1, 1])

        if direction == 1:
            # q_i += 1, q_j -= 1
            if q[i] >= max_q or q[j] <= -max_q:
                continue
            q[i] += 1
            q[j] -= 1
        else:
            # q_i -= 1, q_j += 1
            if q[i] <= -max_q or q[j] >= max_q:
                continue
            q[i] -= 1
            q[j] += 1

    # Sanity check: enforce zero sum by construction
    # (Should already be zero, but we assert to catch bugs.)
    assert int(q.sum()) == 0, "Charge construction should maintain sum=0"
    return q


def build_phases(cfg: ChainConfig, q: np.ndarray) -> np.ndarray:
    """
    Build phases θ_j = q_j * theta + noise.

    Parameters
    ----------
    cfg : ChainConfig
        Chain configuration.
    q : np.ndarray
        Integer charges, shape (N,).

    Returns
    -------
    phases : np.ndarray
        Real-valued phases θ_j.
    """
    assert len(q) == cfg.N
    base = q.astype(float) * cfg.theta

    if cfg.noise_sigma > 0.0:
        rng = _make_rng(None)  # separate stream for noise
        noise = rng.normal(loc=0.0, scale=cfg.noise_sigma, size=cfg.N)
        return base + noise
    else:
        return base


def chain_sum(phases: np.ndarray) -> complex:
    """
    Compute S = Σ_j e^{i θ_j}.

    Parameters
    ----------
    phases : np.ndarray
        Array of phases θ_j.

    Returns
    -------
    S : complex
        Complex sum of unit phasors.
    """
    return np.exp(1j * phases).sum()


def summarize_chain(cfg: ChainConfig) -> Dict[str, Any]:
    """
    Draw a single chain, compute phases and residual, and return summary dict.

    Returns keys:
      - N, theta, max_charge, noise_sigma
      - sum_q, sum_q_abs
      - S_real, S_imag, S_abs
      - S_abs_over_sqrtN
    """
    q = draw_charges(cfg)
    phases = build_phases(cfg, q)
    S = chain_sum(phases)

    N = cfg.N
    S_abs = abs(S)
    S_abs_over_sqrtN = S_abs / math.sqrt(N)

    out: Dict[str, Any] = {
        "N": N,
        "theta": cfg.theta,
        "max_charge": cfg.max_charge,
        "noise_sigma": cfg.noise_sigma,
        "enforce_zero_sum": cfg.enforce_zero_sum,
        "sum_q": int(q.sum()),
        "sum_q_abs": int(np.abs(q).sum()),
        "S_real": float(S.real),
        "S_imag": float(S.imag),
        "S_abs": float(S_abs),
        "S_abs_over_sqrtN": float(S_abs_over_sqrtN),
    }
    out.update({f"q_{i}": int(v) for i, v in enumerate(q)})
    return out


def summarize_many(cfg: ChainConfig, n_samples: int) -> Dict[str, Any]:
    """
    Run many chains with the same config and accumulate basic statistics.

    Returns keys:
      - N, theta, max_charge, noise_sigma, enforce_zero_sum
      - n_samples
      - mean_S_abs, rms_S_abs
      - mean_S_abs_over_sqrtN, rms_S_abs_over_sqrtN
    """
    N = cfg.N
    S_abs_list = []
    S_scaled_list = []

    for k in range(n_samples):
        local_cfg = cfg
        if cfg.seed is not None:
            # Derive a per-sample seed from the base one
            local_cfg = ChainConfig(
                **{
                    **asdict(cfg),
                    "seed": cfg.seed + k,
                }
            )
        summary = summarize_chain(local_cfg)
        S_abs_list.append(summary["S_abs"])
        S_scaled_list.append(summary["S_abs_over_sqrtN"])

    S_abs_arr = np.array(S_abs_list, dtype=float)
    S_scaled_arr = np.array(S_scaled_list, dtype=float)

    def _rms(x: np.ndarray) -> float:
        return float(np.sqrt(np.mean(x**2)))

    return {
        "N": N,
        "theta": cfg.theta,
        "max_charge": cfg.max_charge,
        "noise_sigma": cfg.noise_sigma,
        "enforce_zero_sum": cfg.enforce_zero_sum,
        "n_samples": int(n_samples),
        "mean_S_abs": float(S_abs_arr.mean()),
        "rms_S_abs": _rms(S_abs_arr),
        "mean_S_abs_over_sqrtN": float(S_scaled_arr.mean()),
        "rms_S_abs_over_sqrtN": _rms(S_scaled_arr),
    }
