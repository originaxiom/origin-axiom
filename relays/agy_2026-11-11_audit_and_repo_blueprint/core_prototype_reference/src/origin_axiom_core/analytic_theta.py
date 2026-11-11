"""Holomorphic Jacobi Theta Functions on the Upper Half-Plane (P-670 Closure).

Standard nome-based implementations (such as `mpmath.jtheta(n, z, exp(i*pi*tau))`)
pass `q = exp(i*pi*tau)` by value and internally evaluate `q ** (1/4) = exp(log(q)/4)`
for odd/spinor theta functions (`n = 1, 2`), introducing artificial branch cuts across
every vertical line `Re(tau) = 2k + 1` (`k in Z`, `k != 0`).

`analytic_jtheta(n, z, tau)` evaluates the bilateral series directly from the
quarter-nome `q_4 = exp(i*pi*tau / 4)` and `w = exp(i*z)`, preserving holomorphicity,
modular `T`-covariance (`tau -> tau + 1`), and quasi-periodicity across all `tau in H`.
"""

from __future__ import annotations

from typing import Tuple

import mpmath as mp

from .guardrail_dsl import producer


@producer
def analytic_jtheta(n: int, z: complex | mp.mpc, tau: complex | mp.mpc, derivative: int = 0, n_terms: int = 45) -> mp.mpc:
    """Evaluates holomorphic Jacobi theta_n^(d)(z | tau) for n in {1, 2, 3, 4} across all Im(tau) > 0."""
    if n not in (1, 2, 3, 4):
        raise ValueError(f"Jacobi index n must be in {{1, 2, 3, 4}}, got {n}")
    if derivative < 0:
        raise ValueError(f"derivative order must be >= 0, got {derivative}")
    t = mp.mpc(tau)
    if mp.im(t) <= 0:
        raise ValueError(f"tau must lie in the upper half-plane Im(tau) > 0, got {t}")
    zv = mp.mpc(z)
    q4 = mp.exp(1j * mp.pi * t / 4)
    q = q4 ** 4  # exp(i * pi * tau)
    acc = mp.mpc(0, 0)

    if n in (1, 2):
        for m in range(-n_terms, n_terms + 1):
            exp_4 = (2 * m + 1) ** 2
            q_pow = q4 ** exp_4
            freq = mp.mpf(2 * m + 1)
            if n == 1:
                sign = -1 if (m % 2 != 0) else 1
                # d^k/dz^k sin((2m+1)z): k=0->sin, 1->cos, 2->-sin, 3->-cos
                mod4 = derivative % 4
                if mod4 == 0:
                    trig = mp.sin(freq * zv)
                elif mod4 == 1:
                    trig = mp.cos(freq * zv)
                elif mod4 == 2:
                    trig = -mp.sin(freq * zv)
                else:
                    trig = -mp.cos(freq * zv)
                acc += sign * q_pow * (freq ** derivative) * trig
            else:
                mod4 = derivative % 4
                if mod4 == 0:
                    trig = mp.cos(freq * zv)
                elif mod4 == 1:
                    trig = -mp.sin(freq * zv)
                elif mod4 == 2:
                    trig = -mp.cos(freq * zv)
                else:
                    trig = mp.sin(freq * zv)
                acc += q_pow * (freq ** derivative) * trig
        return acc

    # n in (3, 4)
    if derivative == 0:
        acc = mp.mpc(1, 0)
    for m in range(1, n_terms + 1):
        q_pow = q ** (m * m)
        freq = mp.mpf(2 * m)
        sign = (-1 if (m % 2 != 0) else 1) if n == 4 else 1
        mod4 = derivative % 4
        if mod4 == 0:
            trig = mp.cos(freq * zv)
        elif mod4 == 1:
            trig = -mp.sin(freq * zv)
        elif mod4 == 2:
            trig = -mp.cos(freq * zv)
        else:
            trig = mp.sin(freq * zv)
        acc += 2 * sign * q_pow * (freq ** derivative) * trig
    return acc


@producer
def dedekind_eta_holomorphic(tau: complex | mp.mpc, n_terms: int = 60) -> mp.mpc:
    """Evaluates holomorphic Dedekind eta(tau) = exp(i*pi*tau/12) * prod_{m>=1}(1 - exp(2*pi*i*m*tau))."""
    t = mp.mpc(tau)
    if mp.im(t) <= 0:
        raise ValueError(f"tau must lie in H, got {t}")
    q2 = mp.exp(2j * mp.pi * t)
    prod = mp.mpc(1, 0)
    qm = q2
    for _ in range(n_terms):
        prod *= 1 - qm
        qm *= q2
    return mp.exp(1j * mp.pi * t / 12) * prod


@producer
def theta_triplet_weight_minus_half(tau: complex | mp.mpc, n_terms: int = 50) -> Tuple[mp.mpc, mp.mpc, mp.mpc]:
    """Evaluates the 3D holomorphic weight-(-1/2) weave triplet (theta_2^2, theta_3^2, theta_4^2) / eta^3."""
    t = mp.mpc(tau)
    et3 = dedekind_eta_holomorphic(t, n_terms=n_terms) ** 3
    th2 = analytic_jtheta(2, 0, t, n_terms=n_terms)
    th3 = analytic_jtheta(3, 0, t, n_terms=n_terms)
    th4 = analytic_jtheta(4, 0, t, n_terms=n_terms)
    return (th2 * th2) / et3, (th3 * th3) / et3, (th4 * th4) / et3
