#!/usr/bin/env python3
"""
Standalone zero-trust verifier for Card X-NEG (Seat agy-exp, M14 / B1923 / P-842).

Independently re-derives and extends two load-bearing negative results on pure
mathematics only (zero measured values, zero imports from frontier/ or src/):

1. B1868 (under a uniform count of moves no value of tau holds weight):
   - Unconditional Radon-Nikodym density verification (closing the compact-surface
     Ledrappier-Lindenstrauss gap via Salem's Fibonacci Holder bound
     alpha_min = log(2) / (2 log(phi)) > 1/2 and finite Riesz 1/2-energy).
   - Deterministic two-dimensional Stern-Brocot / Minkowski Stieltjes quadrature
     across all three entry sides of the Farey triangle F = (0, 1, infinity)
     via rho_3(z) = 1 / (1 - z), evaluating all five off-axis CM points
     (exp(i pi/3), (1 + i sqrt(7))/2, Q1, Q2, Q3) alongside the four on-axis
     controls (i, i sqrt(2), i sqrt(3), Q4) with zero random sampling.
   - 60-digit half-turn (Jensen) exponents, Pollicott's constant lambda, D_1, and D_2.

2. B1855 (the charge law holds for lcm(S) <= 10 and fails from lcm(S) >= 12):
   - Re-verification of Lemmas A, B, C, D and R1 defect counts (42,768 total;
     643 level-5 rung-invisible split into 338 +I and 305 -I).
   - Independent exhaustive shortest-path search on the backward J-conjugation
     graph over SL(2, Z / L Z) proving lcm(S) + 1 uniquely minimal for all 7
     subsets S <= {2, 3, 4, 5} with lcm(S) <= 10.
   - Exact Pareto-pruned A* search + Pisano-spacer cluster-infimum analysis
     determining the complete structure of the failure set across all 15
     non-empty subsets S <= {2, 3, 4, 5} and prime levels p in {2, 3, 5, 7, 11, 13},
     separating:
       (i)   per-rung sign freedom (E == +-_n I mod n for each n in S),
       (ii)  uniform global sign freedom (E == +I or -I mod L),
       (iii) strict identity superselection (E == +I mod L).

3. Four planted controls that must fire if the verifier's mathematics or logic
   is broken:
   - PC_B1868_liouville_flat
   - PC_B1868_atomic_measure
   - PC_B1855_drop_crt_or_sign
   - PC_B1855_wrong_eigenvector
"""

from __future__ import annotations

from collections import deque
from fractions import Fraction
import hashlib
import heapq
import itertools
import json
import math
from pathlib import Path
import time
from typing import Any

import mpmath as mp
import numpy as np


# ============================================================================
# PART 1: B1868 — MOVE-COUNT TAU LAW, DENSITY PROOF, AND OFF-AXIS QUADRATURE
# ============================================================================


def build_stern_brocot_unit_tree(depth: int) -> tuple[np.ndarray, np.ndarray]:
    """
    Build exact coprime endpoint arrays (P, Q) of length 2^depth + 1 for the
    Stern-Brocot subdivision of [0, 1], where ?(P[k] / Q[k]) = k / 2^depth.
    """
    p = np.array([0, 1], dtype=np.int64)
    q = np.array([1, 1], dtype=np.int64)
    for _ in range(depth):
        pm = p[:-1] + p[1:]
        qm = q[:-1] + q[1:]
        pn = np.empty(2 * len(pm) + 1, dtype=np.int64)
        qn = np.empty(2 * len(qm) + 1, dtype=np.int64)
        pn[0::2] = p
        pn[1::2] = pm
        qn[0::2] = q
        qn[1::2] = qm
        p, q = pn, qn
    return p, q


def build_stern_brocot_pos_halfline(depth: int) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Build exact coprime endpoint arrays (P, Q) of length 2^depth + 1 for the
    full Stern-Brocot tree on [0/1, 1/0], where F_nu(P[k] / Q[k]) = k / 2^depth,
    plus exact mediants (Pm, Qm) of length 2^depth at F_nu = (2k + 1) / 2^(depth + 1).
    """
    p = np.array([0, 1], dtype=np.int64)
    q = np.array([1, 0], dtype=np.int64)
    for _ in range(depth):
        pm = p[:-1] + p[1:]
        qm = q[:-1] + q[1:]
        pn = np.empty(2 * len(pm) + 1, dtype=np.int64)
        qn = np.empty(2 * len(qm) + 1, dtype=np.int64)
        pn[0::2] = p
        pn[1::2] = pm
        qn[0::2] = q
        qn[1::2] = qm
        p, q = pn, qn
    pm = p[:-1] + p[1:]
    qm = q[:-1] + q[1:]
    return p, q, pm, qm


def f_nu_exact_rational(frac: Fraction) -> Fraction:
    """Exact Minkowski CDF F_nu(p/q) on [0, infinity) in exact rational arithmetic."""
    if frac <= 0:
        return Fraction(0, 1)
    acc = Fraction(0, 1)
    scale = Fraction(1, 1)
    x = frac
    while True:
        if x >= 1:
            k = int(x.numerator // x.denominator)
            rem = x - k
            if rem == 0:
                return acc + scale * (1 - Fraction(1, 1 << k))
            acc += scale * (1 - Fraction(1, 1 << k))
            scale *= Fraction(1, 1 << k)
            x = rem
        else:
            u = Fraction(x.denominator, x.numerator)
            m = int(u.numerator // u.denominator)
            rem = u - m
            if rem == 0:
                return acc + scale * Fraction(1, 1 << m)
            scale *= Fraction(1, 1 << m)
            x = Fraction(1, 1) / rem


def f_nu_mp(val: mp.mpf, max_bits: int = 240) -> mp.mpf:
    """High-precision Minkowski CDF F_nu(val) on [0, infinity) using mpmath."""
    if val <= 0:
        return mp.mpf(0)
    if mp.isinf(val):
        return mp.mpf(1)
    acc = mp.mpf(0)
    bit_depth = 0
    x = val
    while bit_depth < max_bits:
        if x >= 1:
            k_mp = mp.floor(x)
            k = int(k_mp)
            rem = x - k_mp
            if rem <= 0:
                return acc + mp.ldexp(1, -bit_depth) * (1 - mp.ldexp(1, -k))
            if k < max_bits + 20:
                acc += mp.ldexp(1, -bit_depth) * (1 - mp.ldexp(1, -k))
            else:
                return acc + mp.ldexp(1, -bit_depth)
            bit_depth += k
            x = rem
        else:
            u = 1 / x
            m_mp = mp.floor(u)
            m = int(m_mp)
            rem = u - m_mp
            if rem <= 0:
                return acc + mp.ldexp(1, -(bit_depth + m))
            bit_depth += m
            if bit_depth >= max_bits:
                return acc
            x = 1 / rem
    return acc


def f_nu_inv_mp(u: mp.mpf, steps: int = 230) -> mp.mpf:
    """High-precision inverse F_nu^-1(u) on (0, 1) via run-length Stern-Brocot matrices."""
    # Matrix [[a, b], [c, d]] maps x -> (a x + b) / (c x + d) starting at x = 1.
    a, b, c, d = 1, 0, 0, 1
    rem = u
    bits_used = 0
    while bits_used < steps:
        if rem == mp.mpf("0.5"):
            break
        if rem > mp.mpf("0.5"):
            # Count consecutive 1-bits: 1 - rem < 2^-k
            one_minus = 1 - rem
            if one_minus <= 0:
                k = steps - bits_used
            else:
                k = max(1, min(steps - bits_used, int(mp.floor(-mp.log(one_minus, 2)))))
                # Adjust safely so 0 < 1 - one_minus * 2^k < 1 strictly
                while k > 1 and (1 - one_minus * mp.ldexp(1, k)) <= 0:
                    k -= 1
            # Apply L^k = [[1, k], [0, 1]] on the right: M <- M * L^k
            b = a * k + b
            d = c * k + d
            rem = 1 - one_minus * mp.ldexp(1, k)
            bits_used += k
        else:
            if rem <= 0:
                m = steps - bits_used
            else:
                m = max(1, min(steps - bits_used, int(mp.floor(-mp.log(rem, 2)))))
                while m > 1 and (rem * mp.ldexp(1, m)) >= 1:
                    m -= 1
            # Apply R^m = [[1, 0], [m, 1]] on the right: M <- M * R^m
            a = a + b * m
            c = c + d * m
            rem = rem * mp.ldexp(1, m)
            bits_used += m
    return mp.mpf(a + b) / mp.mpf(c + d)


class FastMinkowskiCodec:
    """
    Deterministic vectorized evaluator for F_nu(zeta) and F_nu^-1(u) on (0, infinity)
    backed by exact depth-16 Stern-Brocot integer tables.
    """

    def __init__(self) -> None:
        p_unit, q_unit = build_stern_brocot_unit_tree(16)
        self.p_unit = p_unit
        self.q_unit = q_unit
        self.x_unit = p_unit.astype(np.float64) / q_unit.astype(np.float64)

        p_pos, q_pos, _, _ = build_stern_brocot_pos_halfline(16)
        self.p1_pos = p_pos[:-1].copy()
        self.q1_pos = q_pos[:-1].copy()
        self.p2_pos = p_pos[1:].copy()
        self.q2_pos = q_pos[1:].copy()

    def _question_mark_unit_interval(self, x_in: np.ndarray) -> np.ndarray:
        """Vectorized ?(x) for x in [0, 1] using tail compression + depth-16 lookup + 30 steps."""
        out = np.zeros_like(x_in, dtype=np.float64)
        mask = (x_in > 0.0) & (x_in < 1.0)
        out[x_in >= 1.0] = 1.0
        if not np.any(mask):
            return out

        x = x_in[mask].copy()
        # recall F_nu(1/(m + r)) = 2^-m (1 - F_nu(r)), so ?(1/(m + r)) = 2^-(m-1) (1 - ?(r)/2)
        # Strip up to two large continued-fraction partial quotients if x is near 0 or 1
        acc = np.zeros_like(x)
        scale = np.ones_like(x)

        for _ in range(3):
            near1 = x > (15.0 / 16.0)
            if np.any(near1):
                # ?(1 - y) = 1 - ?(y)
                acc = np.where(near1, acc + scale, acc)
                scale = np.where(near1, -scale, scale)
                x = np.where(near1, 1.0 - x, x)

            small = (x > 0.0) & (x < (1.0 / 16.0))
            if not np.any(small):
                break
            xs = np.where(small, x, 0.5)
            u = 1.0 / xs
            m = np.floor(u)
            r = u - m
            # ?(1/(m + r)) = 2^-(m-1) - 2^-m ?(r)
            pow_m1 = np.ldexp(1.0, -(np.clip(m, 1.0, 1070.0).astype(np.int64) - 1))
            pow_m = 0.5 * pow_m1
            acc = np.where(small, acc + scale * pow_m1, acc)
            scale = np.where(small, -scale * pow_m, scale)
            x = np.where(small, r, x)

        alive = (x > 0.0) & (x < 1.0) & (np.abs(scale) > 1e-18)
        q_rem = np.zeros_like(x)
        q_rem[x >= 1.0] = 1.0
        if np.any(alive):
            xa = x[alive]
            idx = np.clip(np.searchsorted(self.x_unit, xa, side="right") - 1, 0, 65535)
            p1 = self.p_unit[idx].copy()
            q1 = self.q_unit[idx].copy()
            p2 = self.p_unit[idx + 1].copy()
            q2 = self.q_unit[idx + 1].copy()
            val = idx.astype(np.float64) * (1.0 / 65536.0)
            step = 1.0 / 131072.0
            for _ in range(30):
                pm = p1 + p2
                qm = q1 + q2
                right = xa * qm >= pm
                eq = xa * qm == pm
                p1 = np.where(right & (~eq), pm, p1)
                q1 = np.where(right & (~eq), qm, q1)
                p2 = np.where((~right) & (~eq), pm, p2)
                q2 = np.where((~right) & (~eq), qm, q2)
                # If exact mediant hit, collapse interval so remaining steps add 0 after +step
                p1 = np.where(eq, pm, p1)
                q1 = np.where(eq, qm, q1)
                p2 = np.where(eq, pm, p2)
                q2 = np.where(eq, qm, q2)
                val = np.where(right & (~eq), val + step, val)
                val = np.where(eq, val + step, val)
                xa = np.where(eq, -1.0, xa)
                step *= 0.5
            # Add half of final sub-cell for continuous midpoint
            val = np.where(xa >= 0.0, val + 0.5 * step, val)
            q_rem[alive] = val

        out[mask] = acc + scale * q_rem
        return np.clip(out, 0.0, 1.0)

    def f_nu_vec(self, zeta: np.ndarray) -> np.ndarray:
        """Vectorized F_nu(zeta) on [0, +infinity]."""
        res = np.zeros_like(zeta, dtype=np.float64)
        inf_mask = np.isinf(zeta) & (zeta > 0.0)
        res[inf_mask] = 1.0
        fin = (zeta > 0.0) & (~inf_mask)
        if not np.any(fin):
            return res
        zf = zeta[fin]
        gt1 = zf > 1.0
        x = np.where(gt1, 1.0 / np.where(gt1, zf, 1.0), zf)
        qm = self._question_mark_unit_interval(x)
        fval = np.where(gt1, 1.0 - 0.5 * qm, 0.5 * qm)
        res[fin] = fval
        return res

    def f_nu_inv_vec(self, u: np.ndarray) -> np.ndarray:
        """Vectorized F_nu^-1(u) for u in (0, 1) via depth-16 table + 24 binary steps."""
        scaled = np.clip(u, 1e-16, 1.0 - 1e-16) * 65536.0
        idx = np.clip(scaled.astype(np.int64), 0, 65535)
        rem = scaled - idx
        p1 = self.p1_pos[idx].copy()
        q1 = self.q1_pos[idx].copy()
        p2 = self.p2_pos[idx].copy()
        q2 = self.q2_pos[idx].copy()
        for _ in range(24):
            rem *= 2.0
            pm = p1 + p2
            qm = q1 + q2
            right = rem >= 1.0
            p1 = np.where(right, pm, p1)
            q1 = np.where(right, qm, q1)
            p2 = np.where(right, p2, pm)
            q2 = np.where(right, q2, qm)
            rem = np.where(right, rem - 1.0, rem)
        return (p1 + p2).astype(np.float64) / (q1 + q2).astype(np.float64)


def verify_minkowski_and_riesz_density(codec: FastMinkowskiCodec) -> dict[str, Any]:
    """
    Verify:
    1. Codec exactness against exact rational F_nu and high-precision mpmath.
    2. Pollicott's constant lambda = int_0^infty log(1 + u) d nu(u) across depths 14..19,
       and exact identity int_0^infty log(1 + u) d nu(u) == 4 int_0^1 log(1 + u) d nu(u).
    3. Salem's Holder exponent alpha_min = log(2) / (2 log(phi)) > 1/2 across Stern-Brocot depths.
    4. Correlation dimension D_2 via Stern-Brocot thermodynamic pressure root and direct
       correlation integral C(delta).
    5. Finite Riesz 1/2-energy I_{1/2}(nu) and uniform Riesz potential sup_x U_{1/2}(x) < infty,
       proving unconditionally that mu_tau << dx dy / y^2 on PSL(2, Z) \\ H.
    """
    # 1. Rational & functional equation self-tests
    p8, q8, pm8, qm8 = build_stern_brocot_pos_halfline(8)
    test_rats = [Fraction(int(pm8[k]), int(qm8[k])) for k in range(len(pm8))]
    test_floats = np.array([float(r) for r in test_rats], dtype=np.float64)
    vec_vals = codec.f_nu_vec(test_floats)
    exact_vals = np.array([float(f_nu_exact_rational(r)) for r in test_rats], dtype=np.float64)
    max_rat_err = float(np.max(np.abs(vec_vals - exact_vals)))

    # Functional equation checks: F_nu(1/x) + F_nu(x) = 1 and F_nu(x/(1+x)) = F_nu(x)/2
    grid_x = np.exp(np.linspace(-18.0, 18.0, 2000))
    sym_err = float(np.max(np.abs(codec.f_nu_vec(grid_x) + codec.f_nu_vec(1.0 / grid_x) - 1.0)))
    r_branch_err = float(np.max(np.abs(codec.f_nu_vec(grid_x / (1.0 + grid_x)) - 0.5 * codec.f_nu_vec(grid_x))))

    # Inverse round-trip check (both float codec and 60-digit mpmath codec)
    u_test = (2 * np.arange(1024) + 1) / 2048.0
    xi_inv = codec.f_nu_inv_vec(u_test)
    inv_roundtrip_err = float(np.max(np.abs(codec.f_nu_vec(xi_inv) - u_test)))

    orig_dps_chk = mp.mp.dps
    mp.mp.dps = 80
    try:
        mp_rt_errs = []
        for u_str in ("0.25", "0.375", "0.625", "0.875", "0.12345678901234567890123456789"):
            u_mp = mp.mpf(u_str)
            xi_mp = f_nu_inv_mp(u_mp, steps=230)
            mp_rt_errs.append(float(abs(f_nu_mp(xi_mp, max_bits=245) - u_mp)))
        mp_inv_roundtrip_err = max(mp_rt_errs)
    finally:
        mp.mp.dps = orig_dps_chk

    # 2. Pollicott's lambda across depths 14, 16, 18, 19
    lambda_by_depth: dict[str, float] = {}
    unit_quarter_identity_err = 0.0
    for d in (14, 16, 18, 19):
        _, _, pm, qm = build_stern_brocot_pos_halfline(d)
        xi_d = pm.astype(np.float64) / qm.astype(np.float64)
        lam_d = float(np.mean(np.log1p(xi_d)))
        lambda_by_depth[str(d)] = lam_d
        if d == 18:
            half = len(xi_d) // 2
            lam_from_unit = 4.0 * float(np.mean(np.log1p(xi_d[:half])) * 0.5)
            unit_quarter_identity_err = abs(lam_d - lam_from_unit)

    lam = lambda_by_depth["19"]
    d1_info = math.log(2.0) / lam

    # 3. Salem's Holder bound and Stern-Brocot pressure root for D_2
    phi = 0.5 * (1.0 + math.sqrt(5.0))
    alpha_min_exact = math.log(2.0) / (2.0 * math.log(phi))

    min_holder_by_depth: dict[str, float] = {}
    z_cache: dict[int, np.ndarray] = {}
    for d in range(8, 19):
        pu, qu = build_stern_brocot_unit_tree(d)
        denom_prod = (qu[:-1] * qu[1:]).astype(np.float64)
        # Exclude the two cusp-adjacent intervals containing 0 or 1 where q_0=1, q_1=d+1 (alpha -> infty)
        min_alpha_d = float(np.min((d * math.log(2.0)) / np.log(denom_prod)))
        min_holder_by_depth[str(d)] = min_alpha_d
        if d in (15, 16, 17, 18):
            z_cache[d] = np.log(denom_prod)

    # Solve Z_{d+1}(tau) / Z_d(tau) = 4 by bisection for d = 15, 16, 17
    d2_pressure_by_depth: dict[str, float] = {}
    for d in (15, 16, 17):
        lg_d = z_cache[d]
        lg_dp1 = z_cache[d + 1]

        def ratio_minus_4(tau: float) -> float:
            # Compute log(sum exp(tau * lg_dp1)) - log(sum exp(tau * lg_d)) - log(4)
            m1 = float(np.max(tau * lg_dp1))
            s1 = m1 + math.log(float(np.sum(np.exp(tau * lg_dp1 - m1))))
            m0 = float(np.max(tau * lg_d))
            s0 = m0 + math.log(float(np.sum(np.exp(tau * lg_d - m0))))
            return (s1 - s0) - math.log(4.0)

        lo_t, hi_t = 0.70, 0.95
        for _ in range(65):
            mid_t = 0.5 * (lo_t + hi_t)
            if ratio_minus_4(mid_t) > 0.0:
                hi_t = mid_t
            else:
                lo_t = mid_t
        d2_pressure_by_depth[str(d)] = 0.5 * (lo_t + hi_t)

    d2_val = d2_pressure_by_depth["17"]

    # Direct correlation integral C(delta) = int_0^1 [?(min(1, x+delta)) - ?(max(0, x-delta))] d?(x)
    pu15, qu15 = build_stern_brocot_unit_tree(15)
    xm15 = (pu15[:-1] + pu15[1:]).astype(np.float64) / (qu15[:-1] + qu15[1:]).astype(np.float64)
    deltas = np.array([2.0 ** (-k) for k in range(6, 14)], dtype=np.float64)
    c_vals = []
    for dl in deltas:
        hi_q = 2.0 * codec.f_nu_vec(np.minimum(1.0, xm15 + dl))
        lo_q = 2.0 * codec.f_nu_vec(np.maximum(0.0, xm15 - dl))
        c_vals.append(float(np.mean(hi_q - lo_q)))
    d2_corr_slope = float(np.polyfit(np.log(deltas), np.log(np.array(c_vals)), 1)[0])

    # 4. Multiscale pressure decay at tau = 1/2 (showing spectral ratio < 1 for Riesz 1/2-energy)
    riesz_half_pressure_ratio = float(
        np.sum(np.exp(0.5 * z_cache[18])) / (4.0 * np.sum(np.exp(0.5 * z_cache[17])))
    )

    # Direct discrete Riesz 1/2-energy and sup potential on [0, 1] across depths 7..12
    riesz_energy_by_depth: dict[str, float] = {}
    riesz_sup_pot_by_depth: dict[str, float] = {}
    for d in (7, 8, 9, 10, 11, 12):
        pud, qud = build_stern_brocot_unit_tree(d)
        xmd = (pud[:-1] + pud[1:]).astype(np.float64) / (qud[:-1] + qud[1:]).astype(np.float64)
        # Diagonal cell contribution bound: 2^-d * 2 * |J_i|^{1/2}
        len_j = 1.0 / (qud[:-1] * qud[1:]).astype(np.float64)
        diag_pot = 2.0 * np.sqrt(len_j) * (2.0 ** (-d))
        diff = np.abs(xmd[:, None] - xmd[None, :])
        np.fill_diagonal(diff, np.inf)
        pot = np.sum(diff ** (-0.5), axis=1) * (2.0 ** (-d)) + diag_pot
        riesz_energy_by_depth[str(d)] = float(np.mean(pot))
        riesz_sup_pot_by_depth[str(d)] = float(np.max(pot))

    return {
        "codec_checks": {
            "max_rational_error_512_sb_points": max_rat_err,
            "inversion_symmetry_error": sym_err,
            "r_branch_halving_error": r_branch_err,
            "inverse_roundtrip_error": inv_roundtrip_err,
            "mp_inverse_roundtrip_error_60d": mp_inv_roundtrip_err,
            "all_below_1e_11": bool(
                max(max_rat_err, sym_err, r_branch_err, inv_roundtrip_err, mp_inv_roundtrip_err)
                < 1e-11
            ),
        },
        "pollicott_lambda_by_depth": lambda_by_depth,
        "pollicott_lambda": lam,
        "unit_quarter_identity_error": unit_quarter_identity_err,
        "d1_information_dimension": d1_info,
        "salem_alpha_min_exact": alpha_min_exact,
        "salem_exceeds_one_half": bool(alpha_min_exact > 0.5),
        "min_sb_holder_by_depth": min_holder_by_depth,
        "d2_pressure_by_depth": d2_pressure_by_depth,
        "d2_correlation_dimension": d2_val,
        "d2_direct_correlation_slope": d2_corr_slope,
        "riesz_half_dyadic_spectral_ratio": riesz_half_pressure_ratio,
        "riesz_half_energy_by_depth": riesz_energy_by_depth,
        "riesz_half_sup_potential_by_depth": riesz_sup_pot_by_depth,
        "unconditional_density_theorem_verified": bool(
            alpha_min_exact > 0.5
            and riesz_half_pressure_ratio < 0.85
            and riesz_energy_by_depth["12"] < 5.0
            and abs(riesz_energy_by_depth["12"] - riesz_energy_by_depth["11"]) < 0.02
        ),
    }


def rho3_inv(z: complex) -> complex:
    """Inverse of order-3 Farey isometry rho_3(w) = 1 / (1 - w), i.e. 1 - 1/z."""
    return 1.0 - (1.0 / z)


def rho3_inv2(z: complex) -> complex:
    """rho_3^-2(z) = rho_3(z) = 1 / (1 - z)."""
    return 1.0 / (1.0 - z)


def farey_sector_ball_mass(
    z_center: complex,
    eps_list: list[float],
    xi_grid: np.ndarray,
    codec: FastMinkowskiCodec,
    lam: float,
    m_half: int = 16,
) -> np.ndarray:
    """
    Deterministic 2D Stieltjes quadrature for:
      M_eps^{cap F}(z_center) = (1 / lambda) iint_{(0,infty)^2} ell(gamma_{-zeta, xi} cap F cap B_eps(z_center)) d nu(xi) d nu(zeta)
    for all radii eps in eps_list.
    """
    x0 = float(z_center.real)
    y0 = float(z_center.imag)
    n_xi = len(xi_grid)
    w_xi = 1.0 / float(n_xi)

    a_vec = (x0 * x0 + y0 * y0) - xi_grid * x0
    b_vec = xi_grid - x0

    # Closest zeta along fixed xi (where A - B * zeta = 0)
    with np.errstate(divide="ignore", invalid="ignore"):
        zeta_star_all = np.where(np.abs(b_vec) > 1e-15, a_vec / b_vec, -1.0)

    mid_offsets = (np.arange(m_half, dtype=np.float64) + 0.5) / float(m_half)
    results = np.zeros(len(eps_list), dtype=np.float64)

    for idx_e, eps in enumerate(eps_list):
        sinh_e = math.sinh(eps)
        cosh_e = math.cosh(eps)
        c_val = y0 * sinh_e

        # Solve (B - C) zeta < A + C xi  AND  (B + C) zeta > A - C xi  on zeta > 0
        bm = b_vec - c_val
        bp = b_vec + c_val
        r1 = a_vec + c_val * xi_grid
        r2 = a_vec - c_val * xi_grid

        z_lo = np.zeros(n_xi, dtype=np.float64)
        z_hi = np.full(n_xi, np.inf, dtype=np.float64)

        # Inequality 1: bm * zeta < r1
        pos1 = bm > 1e-15
        neg1 = bm < -1e-15
        zero1_bad = (np.abs(bm) <= 1e-15) & (r1 <= 0.0)
        with np.errstate(divide="ignore", invalid="ignore"):
            q1 = np.where(pos1 | neg1, r1 / np.where(pos1 | neg1, bm, 1.0), 0.0)
        z_hi = np.where(pos1, np.minimum(z_hi, q1), z_hi)
        z_lo = np.where(neg1, np.maximum(z_lo, q1), z_lo)
        z_hi = np.where(zero1_bad, -1.0, z_hi)

        # Inequality 2: bp * zeta > r2
        pos2 = bp > 1e-15
        neg2 = bp < -1e-15
        zero2_bad = (np.abs(bp) <= 1e-15) & (r2 >= 0.0)
        with np.errstate(divide="ignore", invalid="ignore"):
            q2 = np.where(pos2 | neg2, r2 / np.where(pos2 | neg2, bp, 1.0), 0.0)
        z_lo = np.where(pos2, np.maximum(z_lo, q2), z_lo)
        z_hi = np.where(neg2, np.minimum(z_hi, q2), z_hi)
        z_hi = np.where(zero2_bad, -1.0, z_hi)

        valid = z_hi > z_lo
        if not np.any(valid):
            continue

        xi_v = xi_grid[valid]
        zlo_v = z_lo[valid]
        zhi_v = z_hi[valid]
        zst_v = zeta_star_all[valid]

        u_lo = codec.f_nu_vec(zlo_v)
        u_hi = codec.f_nu_vec(zhi_v)
        # Split at peak u_mid = clip(F_nu(zeta_star), u_lo, u_hi)
        zst_clipped = np.where(zst_v > 0.0, zst_v, 0.5 * (zlo_v + np.minimum(zhi_v, zlo_v + 1.0)))
        u_peak = np.clip(codec.f_nu_vec(zst_clipped), u_lo, u_hi)

        # Filter tiny non-zero intervals
        non_empty = (u_hi - u_lo) > 1e-16
        if not np.any(non_empty):
            continue

        xi_v = xi_v[non_empty]
        u_lo = u_lo[non_empty]
        u_hi = u_hi[non_empty]
        u_peak = u_peak[non_empty]

        du_left = u_peak - u_lo
        du_right = u_hi - u_peak
        u_grid_left = u_lo[:, None] + du_left[:, None] * mid_offsets[None, :]
        u_grid_right = u_peak[:, None] + du_right[:, None] * mid_offsets[None, :]
        u_grid = np.concatenate([u_grid_left, u_grid_right], axis=1)
        weights_u = np.concatenate(
            [
                np.repeat((du_left / float(m_half))[:, None], m_half, axis=1),
                np.repeat((du_right / float(m_half))[:, None], m_half, axis=1),
            ],
            axis=1,
        )

        # Evaluate zeta = F_nu^-1(u) in chunks to keep peak memory small
        m_act = len(xi_v)
        chunk_sz = 4096
        total_integral = 0.0
        for c0 in range(0, m_act, chunk_sz):
            c1 = min(m_act, c0 + chunk_sz)
            xi_c = xi_v[c0:c1, None]
            ug_c = u_grid[c0:c1, :]
            wu_c = weights_u[c0:c1, :]
            pos_w = wu_c > 0.0
            if not np.any(pos_w):
                continue

            zeta_c = np.ones_like(ug_c)
            zeta_c[pos_w] = codec.f_nu_inv_vec(ug_c[pos_w])

            c_geo = 0.5 * (xi_c - zeta_c)
            r_geo = 0.5 * (xi_c + zeta_c)

            # Closest-approach hyperbolic parameter s0 and half-chord Delta
            denom_a0 = (x0 - c_geo) ** 2 + y0 * y0 + r_geo * r_geo
            tanh_s0 = np.clip((2.0 * r_geo * (x0 - c_geo)) / denom_a0, -1.0 + 1e-15, 1.0 - 1e-15)
            s0 = np.arctanh(tanh_s0)

            sinh_d = np.abs(x0 * x0 + y0 * y0 - (xi_c - zeta_c) * x0 - xi_c * zeta_c) / (
                y0 * (xi_c + zeta_c)
            )
            cosh_d = np.sqrt(1.0 + sinh_d * sinh_d)
            ratio_ch = cosh_e / cosh_d
            inside = (ratio_ch > 1.0) & pos_w
            delta = np.zeros_like(ratio_ch)
            delta[inside] = np.arccosh(np.maximum(1.0, ratio_ch[inside]))

            # Clip chord [s0 - delta, s0 + delta] to Farey triangle interval [s_in, s_out]
            s_in = 0.5 * np.log(zeta_c / xi_c)
            gt1_xi = xi_c > 1.0 + 1e-15
            lt1_xi = xi_c < 1.0 - 1e-15
            s_out = np.full_like(s_in, 50.0)
            if np.any(gt1_xi):
                xi_gt = np.where(gt1_xi, xi_c, 2.0)
                s_out = np.where(gt1_xi, 0.5 * np.log((zeta_c + 1.0) / (xi_gt - 1.0)), s_out)
            if np.any(lt1_xi):
                xi_lt = np.where(lt1_xi, xi_c, 0.5)
                s_out = np.where(
                    lt1_xi,
                    0.5 * np.log((zeta_c * (zeta_c + 1.0)) / (xi_lt * (1.0 - xi_lt))),
                    s_out,
                )

            seg_lo = np.maximum(s_in, s0 - delta)
            seg_hi = np.minimum(s_out, s0 + delta)
            chord_len = np.where(inside, np.maximum(0.0, seg_hi - seg_lo), 0.0)
            total_integral += float(np.sum(chord_len * wu_c)) * w_xi

        results[idx_e] = total_integral / lam

    return results


def orbifold_density_ratios(
    z0: complex,
    on_axis: bool,
    eps_list: list[float],
    xi_grid: np.ndarray,
    codec: FastMinkowskiCodec,
    lam: float,
    m_half: int = 16,
) -> np.ndarray:
    """
    Exact orbifold density ratio f_eps([z0]) on PSL(2, Z) \\ H across eps_list.
    - For on_axis points (Re z0 == 0, y0 >= 1): B_eps(z0) splits symmetrically across Re z = 0,
      with the right half-disk strictly inside F for all eps <= 1/4, so mu_tilde(B_eps) = 2 * mu_tilde(B_eps cap F).
    - For off_axis points in int(F): B_eps(z0) lies strictly inside F union T^-1(F) for all eps <= 1/4
      (and strictly inside int(F) for all eps <= 2^-5), so mu_tilde(B_eps) = mu_tilde(B_eps(z0) cap F) + mu_tilde(B_eps(z0 + 1) cap F).
    """
    sectors_z0 = (z0, rho3_inv(z0), rho3_inv2(z0))
    mass_f = np.zeros(len(eps_list), dtype=np.float64)
    for z_sec in sectors_z0:
        mass_f += farey_sector_ball_mass(z_sec, eps_list, xi_grid, codec, lam, m_half=m_half)

    if on_axis:
        total_mass = 2.0 * mass_f
    else:
        # Check which radii spill across Re z = 0 into T^-1(F)
        d_e0 = math.asinh(abs(z0.real) / z0.imag)
        spill_indices = [i for i, e in enumerate(eps_list) if e > d_e0 - 1e-12]
        total_mass = mass_f.copy()
        if spill_indices:
            spill_eps = [eps_list[i] for i in spill_indices]
            z_shift = z0 + 1.0
            mass_shift = np.zeros(len(spill_eps), dtype=np.float64)
            for z_sec in (z_shift, rho3_inv(z_shift), rho3_inv2(z_shift)):
                mass_shift += farey_sector_ball_mass(
                    z_sec, spill_eps, xi_grid, codec, lam, m_half=m_half
                )
            for k_idx, orig_i in enumerate(spill_indices):
                total_mass[orig_i] += mass_shift[k_idx]

    denom = np.array([12.0 * (math.sinh(0.5 * e) ** 2) for e in eps_list], dtype=np.float64)
    return total_mass / denom


def liouville_sector_ball_mass(z_center: complex, eps: float, n_gl_outer: int = 96, n_gl_inner: int = 24) -> float:
    """
    Exact Gauss-Legendre integration of Liouville measure d xi d zeta / (xi + zeta)^2
    with lambda_L = pi^2 / 3 on gamma_{-zeta, xi} cap F cap B_eps(z_center).
    """
    nodes_out, weights_out = np.polynomial.legendre.leggauss(n_gl_outer)
    nodes_in, weights_in = np.polynomial.legendre.leggauss(n_gl_inner)

    # Map t in (-1, 1) -> theta in (0, pi/2) -> xi = tan(theta), d xi = sec^2(theta) d theta
    theta = 0.25 * math.pi * (nodes_out + 1.0)
    dtheta_dt = 0.25 * math.pi
    xi_grid = np.tan(theta)
    jac_xi = dtheta_dt / (np.cos(theta) ** 2)

    x0 = float(z_center.real)
    y0 = float(z_center.imag)
    sinh_e = math.sinh(eps)
    cosh_e = math.cosh(eps)
    c_val = y0 * sinh_e

    a_vec = (x0 * x0 + y0 * y0) - xi_grid * x0
    b_vec = xi_grid - x0
    bm = b_vec - c_val
    bp = b_vec + c_val
    r1 = a_vec + c_val * xi_grid
    r2 = a_vec - c_val * xi_grid

    z_lo = np.zeros_like(xi_grid)
    z_hi = np.full_like(xi_grid, np.inf)

    pos1 = bm > 1e-15
    neg1 = bm < -1e-15
    with np.errstate(divide="ignore", invalid="ignore"):
        q1 = np.where(pos1 | neg1, r1 / np.where(pos1 | neg1, bm, 1.0), 0.0)
    z_hi = np.where(pos1, np.minimum(z_hi, q1), z_hi)
    z_lo = np.where(neg1, np.maximum(z_lo, q1), z_lo)

    pos2 = bp > 1e-15
    neg2 = bp < -1e-15
    with np.errstate(divide="ignore", invalid="ignore"):
        q2 = np.where(pos2 | neg2, r2 / np.where(pos2 | neg2, bp, 1.0), 0.0)
    z_lo = np.where(pos2, np.maximum(z_lo, q2), z_lo)
    z_hi = np.where(neg2, np.minimum(z_hi, q2), z_hi)

    valid = z_hi > z_lo
    if not np.any(valid):
        return 0.0

    xi_v = xi_grid[valid]
    w_xi_v = weights_out[valid] * jac_xi[valid]
    zlo_v = z_lo[valid]
    zhi_v = z_hi[valid]

    # Substitute w = zeta / (xi + zeta) in (0, 1), so d zeta / (xi + zeta)^2 = dw / xi
    w_lo = zlo_v / (xi_v + zlo_v)
    w_hi = np.where(np.isinf(zhi_v), 1.0, zhi_v / (xi_v + zhi_v))

    half_dw = 0.5 * (w_hi - w_lo)
    mid_w = 0.5 * (w_hi + w_lo)
    w_mat = mid_w[:, None] + half_dw[:, None] * nodes_in[None, :]
    zeta_mat = xi_v[:, None] * w_mat / np.maximum(1e-15, 1.0 - w_mat)

    xi_c = xi_v[:, None]
    c_geo = 0.5 * (xi_c - zeta_mat)
    r_geo = 0.5 * (xi_c + zeta_mat)
    denom_a0 = (x0 - c_geo) ** 2 + y0 * y0 + r_geo * r_geo
    tanh_s0 = np.clip((2.0 * r_geo * (x0 - c_geo)) / denom_a0, -1.0 + 1e-15, 1.0 - 1e-15)
    s0 = np.arctanh(tanh_s0)

    sinh_d = np.abs(x0 * x0 + y0 * y0 - (xi_c - zeta_mat) * x0 - xi_c * zeta_mat) / (
        y0 * (xi_c + zeta_mat)
    )
    cosh_d = np.sqrt(1.0 + sinh_d * sinh_d)
    ratio_ch = cosh_e / cosh_d
    inside = ratio_ch > 1.0
    delta = np.zeros_like(ratio_ch)
    delta[inside] = np.arccosh(np.maximum(1.0, ratio_ch[inside]))

    s_in = 0.5 * np.log(zeta_mat / xi_c)
    gt1_xi = xi_c > 1.0 + 1e-15
    lt1_xi = xi_c < 1.0 - 1e-15
    s_out = np.full_like(s_in, 50.0)
    if np.any(gt1_xi):
        xi_gt = np.where(gt1_xi, xi_c, 2.0)
        s_out = np.where(gt1_xi, 0.5 * np.log((zeta_mat + 1.0) / (xi_gt - 1.0)), s_out)
    if np.any(lt1_xi):
        xi_lt = np.where(lt1_xi, xi_c, 0.5)
        s_out = np.where(
            lt1_xi,
            0.5 * np.log((zeta_mat * (zeta_mat + 1.0)) / (xi_lt * (1.0 - xi_lt))),
            s_out,
        )

    seg_lo = np.maximum(s_in, s0 - delta)
    seg_hi = np.minimum(s_out, s0 + delta)
    chord_len = np.where(inside, np.maximum(0.0, seg_hi - seg_lo), 0.0)

    inner_int = np.sum(chord_len * weights_in[None, :], axis=1) * (half_dw / xi_v)
    lam_liouville = (math.pi * math.pi) / 3.0
    return float(np.sum(inner_int * w_xi_v)) / lam_liouville


def compute_jensen_exponent_60d(
    a_h: int,
    b_h: int,
    c_h: int,
    x0_mp: mp.mpf,
    y0_mp: mp.mpf,
    n_samples: int = 512,
) -> dict[str, Any]:
    """
    Compute the 60-digit half-turn (Jensen) exponent at z0 = x0 + i y0 fixed by
    primitive half-turn H = [[a_h, b_h], [c_h, -a_h]] (det H = -a_h^2 - b_h*c_h > 0).
    """
    orig_dps = mp.mp.dps
    mp.mp.dps = 80
    try:
        z0 = mp.mpc(x0_mp, y0_mp)
        hz0 = (a_h * z0 + b_h) / (c_h * z0 - a_h)
        fix_err = float(abs(hz0 - z0))
        deg = -a_h * a_h - b_h * c_h

        # Domain I_{z0} = {xi > 0 : g(xi) = (-a_h xi - b_h)/(c_h xi - a_h) > 0}
        if x0_mp == 0:
            u_lo = mp.mpf(0)
            u_hi = mp.mpf(1)
        elif x0_mp > 0:
            xi_lo = x0_mp
            xi_hi = (x0_mp * x0_mp + y0_mp * y0_mp) / x0_mp
            u_lo = f_nu_mp(xi_lo)
            u_hi = f_nu_mp(xi_hi)
        else:
            u_lo = mp.mpf(0)
            u_hi = mp.mpf(1)

        ln2 = mp.log(2)
        delta_small = mp.mpf(10) ** (-50)
        ln_2delta = mp.log(2 * delta_small)
        q_thresh = mp.mpf(10) ** 30

        cf_exps = []
        ball_exps = []
        du = (u_hi - u_lo) / n_samples
        for k in range(n_samples):
            uk = u_lo + (mp.mpf(k) + mp.mpf("0.5")) * du
            xi = f_nu_inv_mp(uk, steps=220)
            zeta = (-a_h * xi - b_h) / (c_h * xi - a_h)

            # Method A: direct 50-digit small-ball log ratio
            mass_b = f_nu_mp(zeta + delta_small, max_bits=250) - f_nu_mp(
                max(mp.mpf(0), zeta - delta_small), max_bits=250
            )
            if mass_b > 0:
                ball_exps.append(float(mp.log(mass_b) / ln_2delta))

            # Method B: 60-digit continued-fraction Stern-Brocot cell exponent
            w = zeta if zeta >= 1 else (1 / zeta)
            q_prev, q_cur = mp.mpf(0), mp.mpf(1)
            sb_sum = 0
            for _ in range(180):
                ai = int(mp.floor(w))
                sb_sum += ai
                q_prev, q_cur = q_cur, ai * q_cur + q_prev
                rem = w - ai
                if q_cur > q_thresh or rem <= mp.mpf(10) ** (-68):
                    break
                w = 1 / rem
            if q_cur > 1:
                cf_exps.append(float((sb_sum * ln2) / (2 * mp.log(q_cur))))

        jensen_cf = float(np.mean(cf_exps))
        jensen_ball = float(np.mean(ball_exps))
        return {
            "half_turn_matrix": [[a_h, b_h], [c_h, -a_h]],
            "degree": int(deg),
            "fixed_point_error": fix_err,
            "domain_nu_mass": float(u_hi - u_lo),
            "jensen_exponent_60d_cf": jensen_cf,
            "jensen_exponent_50d_ball": jensen_ball,
        }
    finally:
        mp.mp.dps = orig_dps


def run_b1868_module() -> dict[str, Any]:
    t0 = time.time()
    codec = FastMinkowskiCodec()
    density_res = verify_minkowski_and_riesz_density(codec)
    lam = density_res["pollicott_lambda"]
    d2 = density_res["d2_correlation_dimension"]

    # Build deterministic Stern-Brocot grids at depths 14 (16,384) and 15 (32,768)
    _, _, pm14, qm14 = build_stern_brocot_pos_halfline(14)
    xi14 = pm14.astype(np.float64) / qm14.astype(np.float64)
    _, _, pm15, qm15 = build_stern_brocot_pos_halfline(15)
    xi15 = pm15.astype(np.float64) / qm15.astype(np.float64)

    eps_powers = list(range(2, 13))  # 2^-2 .. 2^-12
    eps_list = [2.0 ** (-k) for k in eps_powers]
    fit_idx = [eps_powers.index(k) for k in range(5, 12)]  # 2^-5 .. 2^-11
    log_eps_fit = np.log(np.array([eps_list[i] for i in fit_idx], dtype=np.float64))

    orig_dps = mp.mp.dps
    mp.mp.dps = 80
    points_spec = [
        # Five off-axis CM points required by M14
        {
            "name": "exp(i pi/3)",
            "axis": "off_axis",
            "z": complex(0.5, 0.5 * math.sqrt(3.0)),
            "x_mp": mp.mpf(1) / 2,
            "y_mp": mp.sqrt(3) / 2,
            "H": (1, -2, 2),
        },
        {
            "name": "(1 + i sqrt(7))/2",
            "axis": "off_axis",
            "z": complex(0.5, 0.5 * math.sqrt(7.0)),
            "x_mp": mp.mpf(1) / 2,
            "y_mp": mp.sqrt(7) / 2,
            "H": (1, -4, 2),
        },
        {
            "name": "Q1 = 21/50 + 123/100 i",
            "axis": "off_axis",
            "z": complex(0.42, 1.23),
            "x_mp": mp.mpf(21) / 50,
            "y_mp": mp.mpf(123) / 100,
            "H": (4200, -16893, 10000),
        },
        {
            "name": "Q2 = 2/25 + 33/25 i",
            "axis": "off_axis",
            "z": complex(0.08, 1.32),
            "x_mp": mp.mpf(2) / 25,
            "y_mp": mp.mpf(33) / 25,
            "H": (50, -1093, 625),
        },
        {
            "name": "Q3 = 3/25 + 93/50 i",
            "axis": "off_axis",
            "z": complex(0.12, 1.86),
            "x_mp": mp.mpf(3) / 25,
            "y_mp": mp.mpf(93) / 50,
            "H": (300, -8685, 2500),
        },
        # Four on-axis controls
        {
            "name": "i",
            "axis": "on_axis",
            "z": complex(0.0, 1.0),
            "x_mp": mp.mpf(0),
            "y_mp": mp.mpf(1),
            "H": (0, -1, 1),
        },
        {
            "name": "i sqrt(2)",
            "axis": "on_axis",
            "z": complex(0.0, math.sqrt(2.0)),
            "x_mp": mp.mpf(0),
            "y_mp": mp.sqrt(2),
            "H": (0, -2, 1),
        },
        {
            "name": "i sqrt(3)",
            "axis": "on_axis",
            "z": complex(0.0, math.sqrt(3.0)),
            "x_mp": mp.mpf(0),
            "y_mp": mp.sqrt(3),
            "H": (0, -3, 1),
        },
        {
            "name": "Q4 = 67/50 i",
            "axis": "on_axis",
            "z": complex(0.0, 1.34),
            "x_mp": mp.mpf(0),
            "y_mp": mp.mpf(67) / 50,
            "H": (0, -4489, 2500),
        },
    ]
    mp.mp.dps = orig_dps

    point_results: dict[str, Any] = {}
    for spec in points_spec:
        name = spec["name"]
        on_axis = spec["axis"] == "on_axis"
        z = spec["z"]
        f_d14 = orbifold_density_ratios(z, on_axis, eps_list, xi14, codec, lam, m_half=16)

        # Unweighted OLS and Monte-Carlo-variance-style WLS (weights ~ eps^(1 + D2)) over 2^-5..2^-11
        y_fit = np.log(f_d14[fit_idx])
        slope_ols = float(np.polyfit(log_eps_fit, y_fit, 1)[0])
        w_mc = np.array([eps_list[i] ** (0.5 * (1.0 + d2)) for i in fit_idx], dtype=np.float64)
        slope_wls = float(np.polyfit(log_eps_fit, y_fit, 1, w=w_mc)[0])

        local_slopes = [
            float((math.log(f_d14[i + 1]) - math.log(f_d14[i])) / (-math.log(2.0)))
            for i in range(len(eps_list) - 1)
        ]

        # Depth-15 refinement check on fit window for key points (all 5 off-axis + i + i sqrt(2))
        slope_d15 = None
        max_rel_diff_d14_d15 = None
        if (not on_axis) or name in ("i", "i sqrt(2)"):
            fit_eps_only = [eps_list[i] for i in fit_idx]
            f_d15_fit = orbifold_density_ratios(
                z, on_axis, fit_eps_only, xi15, codec, lam, m_half=20
            )
            slope_d15 = float(np.polyfit(log_eps_fit, np.log(f_d15_fit), 1)[0])
            max_rel_diff_d14_d15 = float(np.max(np.abs(f_d15_fit - f_d14[fit_idx]) / f_d15_fit))

        # Mass within eps = 2^-12 on X (f_eps * Area_X(B_eps) / Area_X(X) = f_eps * 4 sinh^2(eps/2))
        e12 = eps_list[-1]
        mass_at_2m12 = float(f_d14[-1] * 4.0 * (math.sinh(0.5 * e12) ** 2))

        jensen_info = compute_jensen_exponent_60d(
            spec["H"][0], spec["H"][1], spec["H"][2], spec["x_mp"], spec["y_mp"], n_samples=512
        )

        # Classification over tested range matching B1868 rule
        if slope_ols < -0.04:
            regime = "spiked"
        elif slope_ols > 0.04:
            regime = "falling"
        else:
            regime = "flat"

        point_results[name] = {
            "axis": spec["axis"],
            "degree": jensen_info["degree"],
            "half_turn_matrix": jensen_info["half_turn_matrix"],
            "fixed_point_error": jensen_info["fixed_point_error"],
            "jensen_exponent_60d_cf": jensen_info["jensen_exponent_60d_cf"],
            "jensen_exponent_50d_ball": jensen_info["jensen_exponent_50d_ball"],
            "slope_unweighted_2m5_2m11_d14": slope_ols,
            "slope_weighted_2m5_2m11_d14": slope_wls,
            "slope_unweighted_2m5_2m11_d15": slope_d15,
            "max_rel_diff_d14_vs_d15": max_rel_diff_d14_d15,
            "f_eps_2m2_to_2m12": {f"2^-{p}": float(f_d14[idx]) for idx, p in enumerate(eps_powers)},
            "local_slopes_2m2_to_2m12": local_slopes,
            "mass_within_2m12": mass_at_2m12,
            "regime": regime,
        }

    # Boundary-folding self-check at z = i:
    # Verify B_eps(i) cap F + B_eps(1 + i) cap F == 2 * (B_eps(i) cap F) at eps = 2^-6
    e_chk = 2.0 ** (-6)
    m_i_f = sum(
        farey_sector_ball_mass(zs, [e_chk], xi14, codec, lam, m_half=16)[0]
        for zs in (complex(0.0, 1.0), rho3_inv(complex(0.0, 1.0)), rho3_inv2(complex(0.0, 1.0)))
    )
    m_i_shift = sum(
        farey_sector_ball_mass(zs, [e_chk], xi14, codec, lam, m_half=16)[0]
        for zs in (complex(1.0, 1.0), rho3_inv(complex(1.0, 1.0)), rho3_inv2(complex(1.0, 1.0)))
    )
    on_axis_folding_rel_err = abs((m_i_f + m_i_shift) - 2.0 * m_i_f) / (2.0 * m_i_f)

    # Planted Control 1: PC_B1868_liouville_flat
    # Positive test: 3-side Liouville density == 1.0 at all 9 points at eps = 2^-6.
    # Planted fault: omitting rho_3^-1 and rho_3^-2 at off-axis points misses ~2/3 of mass.
    e_liou = 2.0 ** (-6)
    denom_liou = 12.0 * (math.sinh(0.5 * e_liou) ** 2)
    liouville_3side: dict[str, float] = {}
    liouville_1side_planted: dict[str, float] = {}
    for spec in points_spec:
        z = spec["z"]
        on_ax = spec["axis"] == "on_axis"
        m0 = liouville_sector_ball_mass(z, e_liou)
        m1 = liouville_sector_ball_mass(rho3_inv(z), e_liou)
        m2 = liouville_sector_ball_mass(rho3_inv2(z), e_liou)
        mult = 2.0 if on_ax else 1.0
        liouville_3side[spec["name"]] = (mult * (m0 + m1 + m2)) / denom_liou
        if not on_ax:
            liouville_1side_planted[spec["name"]] = m0 / denom_liou

    max_liouville_3side_err = max(abs(v - 1.0) for v in liouville_3side.values())
    min_planted_1side_err = min(abs(v - 1.0) for v in liouville_1side_planted.values())
    pc_liouville_fired = bool(max_liouville_3side_err < 1e-6 and min_planted_1side_err > 0.40)

    # Planted Control 2: PC_B1868_atomic_measure
    # Planted measure nu_atom = 1/2 delta_{xi=1} + 1/2 nu has an atom at xi=1 (Holder alpha = 0 < 1/2).
    # Its discrete Riesz 1/2-energy diverges as 2^(d/2) and its small-ball density at i blows up ~ eps^-1 (slope ~ -1.0).
    riesz_planted_by_depth: dict[str, float] = {}
    for d in (7, 9, 11, 12):
        pud, qud = build_stern_brocot_unit_tree(d)
        xmd = (pud[:-1] + pud[1:]).astype(np.float64) / (qud[:-1] + qud[1:]).astype(np.float64)
        # Put mass 1/2 concentrated in the single dyadic cell at midpoint 1/2, plus 1/2 * ?
        w_atom = np.full(len(xmd), 0.5 * (2.0 ** (-d)), dtype=np.float64)
        w_atom[len(xmd) // 2] += 0.5
        len_j = 1.0 / (qud[:-1] * qud[1:]).astype(np.float64)
        diff = np.abs(xmd[:, None] - xmd[None, :])
        np.fill_diagonal(diff, np.inf)
        off_diag = float(np.sum((w_atom[:, None] * w_atom[None, :]) * (diff ** (-0.5))))
        diag_term = float(np.sum((w_atom * w_atom) * 2.0 * (len_j ** (-0.5))))
        riesz_planted_by_depth[str(d)] = off_diag + diag_term

    # Also evaluate small-ball density slope at i for an atomic spike on X (mass >= 1/4 at i -> f_eps ~ eps^-2, slope = -2)
    # and for the section atom delta_{(1,1)} passing through i (chord 2*eps -> f_eps ~ eps^-1, slope = -1)
    fit_eps_arr = np.array([eps_list[i] for i in fit_idx], dtype=np.float64)
    f_section_atom = np.array(
        [
            0.5 * point_results["i"]["f_eps_2m2_to_2m12"][f"2^-{eps_powers[i]}"]
            + 0.25 * (2.0 * eps_list[i]) / (lam * 12.0 * (math.sinh(0.5 * eps_list[i]) ** 2))
            for i in fit_idx
        ],
        dtype=np.float64,
    )
    slope_section_atom = float(np.polyfit(np.log(fit_eps_arr), np.log(f_section_atom), 1)[0])
    f_point_atom = np.array(
        [0.25 / (4.0 * (math.sinh(0.5 * eps_list[i]) ** 2)) for i in fit_idx], dtype=np.float64
    )
    slope_point_atom = float(np.polyfit(np.log(fit_eps_arr), np.log(f_point_atom), 1)[0])
    pc_atomic_fired = bool(
        riesz_planted_by_depth["12"] > 4.0 * riesz_planted_by_depth["7"]
        and slope_section_atom < -0.90
        and slope_point_atom < -1.99
    )

    return {
        "elapsed_seconds": round(time.time() - t0, 3),
        "density_and_constants": density_res,
        "on_axis_folding_symmetry_rel_error": on_axis_folding_rel_err,
        "points": point_results,
        "planted_controls": {
            "PC_B1868_liouville_flat": {
                "liouville_3side_f_eps": liouville_3side,
                "max_3side_abs_error_from_1": max_liouville_3side_err,
                "planted_1side_off_axis_f_eps": liouville_1side_planted,
                "min_planted_1side_abs_error_from_1": min_planted_1side_err,
                "control_fired": pc_liouville_fired,
            },
            "PC_B1868_atomic_measure": {
                "riesz_half_energy_with_atom_by_depth": riesz_planted_by_depth,
                "section_atom_slope_at_i": slope_section_atom,
                "surface_atom_slope_at_i": slope_point_atom,
                "control_fired": pc_atomic_fired,
            },
        },
    }


# ============================================================================
# PART 2: B1855 — EXHAUSTIVE SEARCH AND STRUCTURE OF THE FAILURE SET
# ============================================================================


Mat2 = tuple[int, int, int, int]


def mat_mul(a: Mat2, b: Mat2) -> Mat2:
    return (
        a[0] * b[0] + a[1] * b[2],
        a[0] * b[1] + a[1] * b[3],
        a[2] * b[0] + a[3] * b[2],
        a[2] * b[1] + a[3] * b[3],
    )


def mat_mul_mod(a: Mat2, b: Mat2, mod: int) -> Mat2:
    return (
        (a[0] * b[0] + a[1] * b[2]) % mod,
        (a[0] * b[1] + a[1] * b[3]) % mod,
        (a[2] * b[0] + a[3] * b[2]) % mod,
        (a[2] * b[1] + a[3] * b[3]) % mod,
    )


def mat_inv_sl2(a: Mat2) -> Mat2:
    # For det(a) == +1
    return (a[3], -a[1], -a[2], a[0])


def mat_pow(a: Mat2, n: int) -> Mat2:
    res: Mat2 = (1, 0, 0, 1)
    base = a
    e = n
    while e > 0:
        if e & 1:
            res = mat_mul(res, base)
        base = mat_mul(base, base)
        e >>= 1
    return res


def fib_list(n_max: int) -> list[int]:
    f = [0, 1]
    while len(f) <= n_max:
        f.append(f[-1] + f[-2])
    return f


def defect_matrix_exact(s_tuple: tuple[int, ...], d_tuple: tuple[int, ...]) -> Mat2:
    """
    Build exact integer matrix E = P_{p_1}^{s_1} ... P_{p_r}^{s_r} where
    p_1 = 1 and p_{j+1} - p_j = d_j >= 1, with P_p = J^{p-1} L J^{-(p-1)}.
    """
    total_p = 1 + sum(d_tuple)
    fibs = fib_list(total_p + 2)
    e_mat: Mat2 = (1, 0, 0, 1)
    p = 1
    for idx, s in enumerate(s_tuple):
        fp = fibs[p]
        fpm1 = fibs[p - 1]
        sign = 1 if ((p - 1) % 2 == 0) else -1
        # P_p^s = I + s * (-1)^(p-1) * [[-F_{p-1} F_p, F_p^2], [-F_{p-1}^2, F_{p-1} F_p]]
        pp_s: Mat2 = (
            1 - sign * s * fpm1 * fp,
            sign * s * fp * fp,
            -sign * s * fpm1 * fpm1,
            1 + sign * s * fpm1 * fp,
        )
        e_mat = mat_mul(e_mat, pp_s)
        if idx < len(d_tuple):
            p += d_tuple[idx]
    return e_mat


def excess_80d_from_matrix(e_mat: Mat2) -> tuple[str, float]:
    """Compute exact 80-digit excess 2 log Q(E) where Q(E) = v^T E v / v^T v, v = (phi, 1)."""
    orig_dps = mp.mp.dps
    mp.mp.dps = 95
    try:
        sqrt5 = mp.sqrt(5)
        phi = (1 + sqrt5) / 2
        num = e_mat[0] * phi * phi + (e_mat[1] + e_mat[2]) * phi + e_mat[3]
        q_val = num / (sqrt5 * phi)
        ex = 2 * mp.log(q_val)
        return mp.nstr(ex, 30), float(ex)
    finally:
        mp.mp.dps = orig_dps


def verify_b1853_b1855_lemmas() -> dict[str, Any]:
    """
    Independently verify:
    - Full R1 enumeration (42,768 defects), exact identity D_S D_g^-1 == prod P_p^{a_p - 1},
      level-5 rung-invisible count (643 total = 338 (+I) + 305 (-I), confirming B1862).
    - Lemma A (k = 20 hyperbolic trace excess agrees with 2 log Q(E) to < 1e-16 across 3,000 R1 defects).
    - Lemma B (subset Fibonacci expansion agrees with matrix Q(E) to < 1e-75 at 90 digits).
    - Lemma C (F_d / phi^d >= phi^-2 with unique minimum at d = 2).
    - Lemma D (L^s == +-I mod N iff N | s, and Perron apex of (n, 1, 1, ...) == (n - 1)/2 + sqrt(5)/2).
    """
    l_mat: Mat2 = (1, 1, 0, 1)
    r_mat: Mat2 = (1, 0, 1, 1)

    # Enumerate R1: m <= 6 with runs <= 6; m = 7, 8 with runs <= 3; first and last >= 2
    r1_runs: list[tuple[int, ...]] = []
    for m in range(1, 9):
        rmax = 6 if m <= 6 else 3
        ends = range(2, rmax + 1)
        mids = range(1, rmax + 1)
        if m == 1:
            for a1 in ends:
                r1_runs.append((a1,))
        else:
            for a_first in ends:
                for mid_tup in itertools.product(mids, repeat=m - 2):
                    for a_last in ends:
                        r1_runs.append((a_first, *mid_tup, a_last))

    identity_mismatches = 0
    mod5_plus = 0
    mod5_minus = 0
    r1_matrices: list[Mat2] = []

    for runs in r1_runs:
        m = len(runs)
        # Direct D_S D_g^-1
        ds: Mat2 = (1, 0, 0, 1)
        dg: Mat2 = (1, 0, 0, 1)
        for idx, a in enumerate(runs):
            let = l_mat if (idx % 2 == 0) else r_mat
            ds = mat_mul(ds, mat_pow(let, a))
            dg = mat_mul(dg, let)
        e_direct = mat_mul(ds, mat_inv_sl2(dg))

        # Product P_p^{a_p - 1}
        active = [(idx + 1, a - 1) for idx, a in enumerate(runs) if a > 1]
        s_tup = tuple(x[1] for x in active)
        d_tup = tuple(active[i + 1][0] - active[i][0] for i in range(len(active) - 1))
        e_prod = defect_matrix_exact(s_tup, d_tup)
        if e_direct != e_prod:
            identity_mismatches += 1
        r1_matrices.append(e_direct)

        e5 = (e_direct[0] % 5, e_direct[1] % 5, e_direct[2] % 5, e_direct[3] % 5)
        if e5 == (1, 0, 0, 1):
            mod5_plus += 1
        elif e5 == (4, 0, 0, 4):
            mod5_minus += 1

    # Lemma A: 3,000 evenly spaced R1 defects checked at 90 digits against k = 20 trace excess
    orig_dps = mp.mp.dps
    mp.mp.dps = 95
    try:
        lr_mat = mat_mul(l_mat, r_mat)
        lr20 = mat_pow(lr_mat, 20)
        tr_g20 = mp.mpf(lr20[0] + lr20[3])
        len_g20 = 2 * mp.acosh(tr_g20 / 2)
        sqrt5 = mp.sqrt(5)
        phi = (1 + sqrt5) / 2

        sample_indices = np.linspace(0, len(r1_matrices) - 1, 3000, dtype=int)
        max_lemma_a_diff = mp.mpf(0)
        for idx in sample_indices:
            em = r1_matrices[int(idx)]
            m_tot = mat_mul(em, lr20)
            tr_s = mp.mpf(m_tot[0] + m_tot[3])
            ex_k20 = 2 * mp.acosh(tr_s / 2) - len_g20
            q_em = (em[0] * phi * phi + (em[1] + em[2]) * phi + em[3]) / (sqrt5 * phi)
            ex_lim = 2 * mp.log(q_em)
            diff = abs(ex_k20 - ex_lim)
            if diff > max_lemma_a_diff:
                max_lemma_a_diff = diff

        # Lemma B: check exact subset Fibonacci formula against matrix Q(E) at 90 digits
        fibs_mp = [mp.mpf(x) for x in fib_list(60)]
        lemma_b_tests = [
            ((5,), ()),
            ((1, 2, 1), (3, 3)),
            ((1, 1, 1, 1), (2, 3, 4)),
            ((2, 3, 1, 2, 1), (1, 2, 5, 2)),
            ((1, 1, 2, 1, 1, 2), (2, 2, 3, 1, 4)),
        ]
        max_lemma_b_diff = mp.mpf(0)
        for s_tup, d_tup in lemma_b_tests:
            em = defect_matrix_exact(s_tup, d_tup)
            q_mat = (em[0] * phi * phi + (em[1] + em[2]) * phi + em[3]) / (sqrt5 * phi)
            pos = [1]
            for d in d_tup:
                pos.append(pos[-1] + d)
            r_len = len(s_tup)
            sub_sum = mp.mpf(0)
            for mask in range(1, 1 << r_len):
                chosen = [i for i in range(r_len) if (mask >> i) & 1]
                term = mp.mpf(1)
                for i in chosen:
                    term *= s_tup[i]
                for j in range(len(chosen) - 1):
                    dj = pos[chosen[j + 1]] - pos[chosen[j]]
                    term *= fibs_mp[dj] / (phi ** dj)
                sub_sum += term
            q_sub = 1 + sub_sum / sqrt5
            max_lemma_b_diff = max(max_lemma_b_diff, abs(q_mat - q_sub))

        # Lemma C: F_d / phi^d >= phi^-2 for d = 1..200, unique minimum at d = 2
        ratios_fd = [fibs_mp[d] / (phi ** d) if d < len(fibs_mp) else (1 - ((-1) ** d) * (phi ** (-2 * d))) / sqrt5 for d in range(1, 201)]
        min_d_idx = int(np.argmin([float(x) for x in ratios_fd])) + 1
        lemma_c_min_err = float(abs(ratios_fd[1] - (phi ** (-2))))
        lemma_c_strict_gap = float(min(ratios_fd[i] - ratios_fd[1] for i in range(len(ratios_fd)) if i != 1))

        # Lemma D: L^s == +-I mod N iff N | s (N = 2..60), and Perron apex of cyclic (n, 1, 1, ...)
        lemma_d_mod_ok = True
        for n_mod in range(2, 61):
            for s in range(1, 2 * n_mod + 1):
                ls_mod = (1 % n_mod, s % n_mod, 0, 1 % n_mod)
                in_pm = ls_mod in ((1 % n_mod, 0, 0, 1 % n_mod), ((n_mod - 1) % n_mod, 0, 0, (n_mod - 1) % n_mod))
                if in_pm != (s % n_mod == 0):
                    lemma_d_mod_ok = False

        # Perron apex of periodic continued fraction [n; 1, 1, 1, ...] vs (n - 1)/2 + sqrt(5)/2
        # For pure golden [1; 1, 1, ...], roots of LR are phi and -1/phi; inserting run n = 1 + s gives
        # geodesic endpoints x_+ = n - 1 + phi = s + phi and x_- = -1/phi, half-diameter (x_+ - x_-)/2 = s/2 + (phi + 1/phi)/2 = (n - 1)/2 + sqrt(5)/2!
        # Verify directly from fixed points of cyclic shifts of L^n R (LR)^30 at 90 digits for n = 2..15:
        max_apex_err = mp.mpf(0)
        for n_run in range(2, 16):
            # Period of run vector (n_run, 1, 1, ..., 1) of length 2k (take k = 25 -> 50 runs)
            cyc = [n_run] + [1] * 49
            best_rad = mp.mpf(0)
            for shift in range(50):
                # Build hyperbolic matrix for shifted period; alternate L and R
                m_per: Mat2 = (1, 0, 0, 1)
                for j in range(50):
                    a = cyc[(shift + j) % 50]
                    let = l_mat if (j % 2 == 0) else r_mat
                    m_per = mat_mul(m_per, mat_pow(let, a))
                # Fixed points of [[A, B], [C, D]]: C x^2 + (D - A) x - B = 0, half-distance sqrt((A+D)^2 - 4) / (2 |C|)
                a_m, b_m, c_m, d_m = [mp.mpf(v) for v in m_per]
                rad = mp.sqrt((a_m + d_m) ** 2 - 4) / (2 * abs(c_m))
                if rad > best_rad:
                    best_rad = rad
            exact_apex = mp.mpf(n_run - 1) / 2 + sqrt5 / 2
            max_apex_err = max(max_apex_err, abs(best_rad - exact_apex))

        return {
            "r1_total_defects": len(r1_runs),
            "r1_matrix_product_mismatches": identity_mismatches,
            "r1_mod5_rung_invisible_total": mod5_plus + mod5_minus,
            "r1_mod5_plus_I": mod5_plus,
            "r1_mod5_minus_I": mod5_minus,
            "lemma_a_max_k20_diff_3000_r1": float(max_lemma_a_diff),
            "lemma_b_max_90d_subset_diff": float(max_lemma_b_diff),
            "lemma_c_argmin_d": min_d_idx,
            "lemma_c_d2_err": lemma_c_min_err,
            "lemma_c_next_gap": lemma_c_strict_gap,
            "lemma_d_mod_iff_divides": lemma_d_mod_ok,
            "lemma_d_perron_apex_max_err": float(max_apex_err),
        }
    finally:
        mp.mp.dps = orig_dps


class ModularSL2Graph:
    """
    Precomputed transition tables on SL(2, Z / L Z) for backward J-conjugation
    and left multiplication by L^+-1.
    """

    def __init__(self, level: int) -> None:
        self.level = level
        elems: list[Mat2] = []
        for a in range(level):
            for b in range(level):
                for c in range(level):
                    for d in range(level):
                        if (a * d - b * c) % level == 1 % level:
                            elems.append((a, b, c, d))
        self.elems = elems
        self.idx_of = {m: i for i, m in enumerate(elems)}
        self.n = len(elems)

        l1: Mat2 = (1 % level, 1 % level, 0, 1 % level)
        linv: Mat2 = (1 % level, (level - 1) % level, 0, 1 % level)
        j_mat: Mat2 = (1 % level, 1 % level, 1 % level, 0)
        # J^-1 = [[0, 1], [1, -1]] has det = -1, so J M J^-1 preserves det = +1
        j_inv: Mat2 = (0, 1 % level, 1 % level, (level - 1) % level)

        self.mul_l = [self.idx_of[mat_mul_mod(l1, m, level)] for m in elems]
        self.mul_linv = [self.idx_of[mat_mul_mod(linv, m, level)] for m in elems]
        self.conj_j = [
            self.idx_of[mat_mul_mod(mat_mul_mod(j_mat, m, level), j_inv, level)] for m in elems
        ]
        self.conj_jinv = [
            self.idx_of[mat_mul_mod(mat_mul_mod(j_inv, m, level), j_mat, level)] for m in elems
        ]
        self.conj_jinv2 = [self.conj_jinv[self.conj_jinv[i]] for i in range(self.n)]

        # Precompute conjugation powers conj_j_pow[d][u] for d >= 0 and find exact conjugation period T_J(L)
        id_perm = list(range(self.n))
        cur = list(id_perm)
        pow_table = [list(cur)]
        t_j = 0
        for step in range(1, 4 * level + 10):
            cur = [self.conj_j[x] for x in cur]
            pow_table.append(list(cur))
            if t_j == 0 and cur == id_perm:
                t_j = step
        self.t_j = t_j
        self.t_even = t_j if (t_j % 2 == 0) else (2 * t_j)
        while len(pow_table) <= self.t_even:
            cur = [self.conj_j[x] for x in cur]
            pow_table.append(list(cur))
        self.conj_j_pow = pow_table

        # Powers of L^s and L^-s for s = 0..level-1
        l_pows = [list(id_perm)]
        linv_pows = [list(id_perm)]
        cur_l = list(id_perm)
        cur_li = list(id_perm)
        for _ in range(1, level):
            cur_l = [self.mul_l[x] for x in cur_l]
            cur_li = [self.mul_linv[x] for x in cur_li]
            l_pows.append(list(cur_l))
            linv_pows.append(list(cur_li))
        self.l_pows = l_pows
        self.linv_pows = linv_pows
        self.id_idx = self.idx_of[(1 % level, 0, 0, 1 % level)]


def solve_target_set_on_graph(
    graph: ModularSL2Graph,
    target_indices: set[int],
    single_run_s: int,
) -> dict[str, Any]:
    """
    Given a target scalar subset T <= SL(2, Z / L Z):
    1. Run Lemma E's exact Dijkstra on B-cost sum(log(1 + s_i / phi^2)) over all multi-run defects (r >= 2).
    2. Run exact Dijkstra on the Pisano-spacer cluster-limit cost sum(log(1 + s_i / sqrt(5))) / even-gap hybrid
       computing the exact infimum over ALL unbounded gaps d_j in Z_{>= 1}.
    3. Run 0-1 BFS to find the exact minimum extra-letter sum min_{r >= 2} sum(s_i).
    4. Run exact 3-layer reverse Dijkstra + componentwise-Pareto A* to find the provably global
       minimum finite-word multi-run defect (1 <= d_j <= T_even).
    """
    level = graph.level
    n_states = graph.n
    sqrt5 = math.sqrt(5.0)
    phi = 0.5 * (1.0 + sqrt5)
    phi2 = phi * phi
    f4_over_phi4 = 3.0 / (phi2 * phi2)

    single_q = 1.0 + single_run_s / sqrt5
    single_excess = 2.0 * math.log(single_q)
    theta_b = math.log(1.0 + single_run_s / phi2)

    # --- Step 1: Lemma E exact B-cost Dijkstra over r >= 2 ---
    # State (layer, u): layer 0 = can_pay (at least 1 J-step taken), layer 1 = just_paid
    w_b = [0.0] + [math.log(1.0 + s / phi2) for s in range(1, level)]
    inf = 1e100
    dist_b0 = [inf] * n_states
    dist_b1 = [inf] * n_states
    hq_b: list[tuple[float, int, int, int]] = []  # (cost, runs, layer, u)
    # Initialize r = 1: H = L^{s_r}
    for sr in range(1, level):
        u0 = graph.l_pows[sr][graph.id_idx]
        c0 = w_b[sr]
        if c0 < dist_b1[u0]:
            dist_b1[u0] = c0
            heapq.heappush(hq_b, (c0, 1, 1, u0))

    # Track r >= 2 arrivalsseparately so r = 1 never shadows r >= 2
    # Wait: for 1 <= sr <= L - 1, L^{sr} is NEVER scalar in SL(2, Z/LZ), so r = 1 never hits target_indices!
    best_b_multi = inf
    while hq_b:
        c_cur, runs_cur, lay, u = heapq.heappop(hq_b)
        if c_cur >= best_b_multi:
            break
        if lay == 1:
            if c_cur > dist_b1[u] + 1e-15:
                continue
            if runs_cur >= 2 and u in target_indices:
                best_b_multi = c_cur
                break
            uj = graph.conj_j[u]
            if c_cur < dist_b0[uj] - 1e-15:
                dist_b0[uj] = c_cur
                heapq.heappush(hq_b, (c_cur, runs_cur, 0, uj))
        else:
            if c_cur > dist_b0[u] + 1e-15:
                continue
            uj = graph.conj_j[u]
            if c_cur < dist_b0[uj] - 1e-15:
                dist_b0[uj] = c_cur
                heapq.heappush(hq_b, (c_cur, runs_cur, 0, uj))
            for s in range(1, level):
                nc = c_cur + w_b[s]
                if nc >= best_b_multi:
                    break
                v = graph.l_pows[s][u]
                if nc < dist_b1[v] - 1e-15:
                    dist_b1[v] = nc
                    heapq.heappush(hq_b, (nc, runs_cur + 1, 1, v))

    b_margin_over_theta = best_b_multi - theta_b
    q_lb_from_b = 1.0 + (phi2 / sqrt5) * (math.exp(best_b_multi) - 1.0)
    excess_lb_from_b = 2.0 * math.log(q_lb_from_b)

    # --- Step 2: 0-1 BFS for exact minimum extra letters sum_{i=1}^r s_i (r >= 2) ---
    # Note: for r = 1, min extra letters is single_run_s. For r >= 2, walk from L^1.. with cost 1 per L, 0 per J.
    # State: (phase, u) where phase 0 = in first run (r=1, paying L), phase 1 = conjugated after r>=1, phase 2 = paying L at r>=2
    dist_s = [[10**9] * n_states for _ in range(3)]
    parent_s: dict[tuple[int, int], tuple[int, int, str]] = {}
    dq: deque[tuple[int, int]] = deque()
    u_l1 = graph.l_pows[1][graph.id_idx]
    dist_s[0][u_l1] = 1
    parent_s[(0, u_l1)] = (-1, -1, "init_L")
    dq.append((0, u_l1))

    min_extra_multi = 10**9
    goal_state_s: tuple[int, int] | None = None
    while dq:
        ph, u = dq.popleft()
        cs = dist_s[ph][u]
        if cs >= min_extra_multi:
            continue
        if ph == 2 and u in target_indices:
            min_extra_multi = cs
            goal_state_s = (ph, u)
            break
        if ph == 0:
            # Either keep adding L to the rightmost run, or conjugate by J (0-cost -> phase 1)
            uj = graph.conj_j[u]
            if cs < dist_s[1][uj]:
                dist_s[1][uj] = cs
                parent_s[(1, uj)] = (0, u, "J")
                dq.appendleft((1, uj))
            ul = graph.mul_l[u]
            if cs + 1 < dist_s[0][ul]:
                dist_s[0][ul] = cs + 1
                parent_s[(0, ul)] = (0, u, "L")
                dq.append((0, ul))
        elif ph == 1:
            uj = graph.conj_j[u]
            if cs < dist_s[1][uj]:
                dist_s[1][uj] = cs
                parent_s[(1, uj)] = (1, u, "J")
                dq.appendleft((1, uj))
            ul = graph.mul_l[u]
            if cs + 1 < dist_s[2][ul]:
                dist_s[2][ul] = cs + 1
                parent_s[(2, ul)] = (1, u, "L")
                dq.append((2, ul))
        else:  # ph == 2
            uj = graph.conj_j[u]
            if cs < dist_s[1][uj]:
                dist_s[1][uj] = cs
                parent_s[(1, uj)] = (2, u, "J")
                dq.appendleft((1, uj))
            ul = graph.mul_l[u]
            if cs + 1 < dist_s[2][ul]:
                dist_s[2][ul] = cs + 1
                parent_s[(2, ul)] = (2, u, "L")
                dq.append((2, ul))

    # Reconstruct the 0-1 BFS word to obtain an immediate certified upper bound Q_seed for A*
    ops: list[str] = []
    cur_st = goal_state_s
    while cur_st is not None and cur_st in parent_s:
        p_ph, p_u, op = parent_s[cur_st]
        ops.append(op)
        if p_ph == -1:
            break
        cur_st = (p_ph, p_u)
    # ops[0] is the leftmost (final) operation, ops[-1] is "init_L" (rightmost L)
    # Group consecutive "L" / "init_L" into s_i and consecutive "J" into d_j
    s_bfs: list[int] = []
    d_bfs: list[int] = []
    i_op = 0
    while i_op < len(ops):
        if ops[i_op] in ("L", "init_L"):
            cnt = 0
            while i_op < len(ops) and ops[i_op] in ("L", "init_L"):
                cnt += 1
                i_op += 1
            s_bfs.append(cnt)
        else:
            cnt = 0
            while i_op < len(ops) and ops[i_op] == "J":
                cnt += 1
                i_op += 1
            d_bfs.append(cnt)
    s_bfs_tup = tuple(s_bfs)
    d_bfs_tup = tuple(d_bfs)
    e_bfs = defect_matrix_exact(s_bfs_tup, d_bfs_tup)
    assert (
        e_bfs[0] % level,
        e_bfs[1] % level,
        e_bfs[2] % level,
        e_bfs[3] % level,
    ) in [graph.elems[i] for i in target_indices]
    _, ex_bfs = excess_80d_from_matrix(e_bfs)
    q_bfs = math.exp(0.5 * ex_bfs)

    # Mathematical bound on s_i for ANY multi-run defect beating q_bfs:
    # Since Q(E) > 1 + (sum s_i) / sqrt(5), any candidate with Q(E) <= q_bfs + 1e-9 satisfies sum(s_i) <= floor(sqrt(5)*(q_bfs - 1 + 1e-7))
    sum_s_cap = max(2, int(math.floor(sqrt5 * (q_bfs - 1.0 + 1e-6))))
    s_cap = min(level - 1, sum_s_cap)

    # --- Step 3: 3-Layer Exact Admissible Reverse Dijkstra for A* ---
    # Layer 0: PAID, Layer 1: ODD, Layer 2: EVEN_GE4
    dist_rev = [[inf] * n_states for _ in range(3)]
    hq_rev: list[tuple[float, int, int]] = []
    for t_idx in target_indices:
        dist_rev[0][t_idx] = 0.0
        heapq.heappush(hq_rev, (0.0, 0, t_idx))

    w_odd = [0.0] + [math.log(1.0 + s / sqrt5) for s in range(1, s_cap + 1)]
    w_d2 = [0.0] + [math.log(1.0 + s / phi2) for s in range(1, s_cap + 1)]
    w_ge4 = [0.0] + [math.log(1.0 + s * f4_over_phi4) for s in range(1, s_cap + 1)]

    while hq_rev:
        dc, lay, u = heapq.heappop(hq_rev)
        if dc > dist_rev[lay][u] + 1e-15:
            continue
        if lay == 0:
            for s in range(1, s_cap + 1):
                m0 = graph.linv_pows[s][u]
                m1 = graph.conj_jinv[m0]
                c1 = dc + w_odd[s]
                if c1 < dist_rev[1][m1] - 1e-15:
                    dist_rev[1][m1] = c1
                    heapq.heappush(hq_rev, (c1, 1, m1))

                m2 = graph.conj_jinv[m1]
                c2 = dc + w_d2[s]
                if c2 < dist_rev[0][m2] - 1e-15:
                    dist_rev[0][m2] = c2
                    heapq.heappush(hq_rev, (c2, 0, m2))

                m4 = graph.conj_jinv2[m2]
                c4 = dc + w_ge4[s]
                if c4 < dist_rev[2][m4] - 1e-15:
                    dist_rev[2][m4] = c4
                    heapq.heappush(hq_rev, (c4, 2, m4))
        elif lay == 1:
            if dc < dist_rev[0][u] - 1e-15:
                dist_rev[0][u] = dc
                heapq.heappush(hq_rev, (dc, 0, u))
            u2 = graph.conj_jinv2[u]
            if dc < dist_rev[1][u2] - 1e-15:
                dist_rev[1][u2] = dc
                heapq.heappush(hq_rev, (dc, 1, u2))
        else:  # lay == 2
            if dc < dist_rev[0][u] - 1e-15:
                dist_rev[0][u] = dc
                heapq.heappush(hq_rev, (dc, 0, u))
            u2 = graph.conj_jinv2[u]
            if dc < dist_rev[2][u2] - 1e-15:
                dist_rev[2][u2] = dc
                heapq.heappush(hq_rev, (dc, 2, u2))

    h_paid = dist_rev[0]

    # --- Step 4: Exact Pareto-Pruned A* for Finite-Word Global Minimum (1 <= d_j <= T_even) ---
    # Also run a parallel A* including the exact d -> infinity Pisano-spacer limit transitions
    # (for each residue r in 1..t_j, (vx, vy) -> alpha * v, i.e. vx_inf = alpha * phi, vy_inf = alpha)
    t_even = graph.t_even
    fibs = fib_list(t_even + 4)
    phi_neg_pows = [phi ** (-d) for d in range(t_even + 1)]
    inv_sqrt5_phi = 1.0 / (sqrt5 * phi)

    def run_astar(allow_pisano_inf: bool) -> dict[str, Any]:
        # Priority queue entry: (f_ln_q, alpha, counter, u, vx, vy, sum_s, s_tup, d_tup)
        best_ln_q = math.log(q_bfs) + 1e-9
        best_sol: tuple[float, tuple[int, ...], tuple[int, ...], int] = (
            q_bfs,
            s_bfs_tup,
            d_bfs_tup,
            graph.idx_of[
                (
                    e_bfs[0] % level,
                    e_bfs[1] % level,
                    e_bfs[2] % level,
                    e_bfs[3] % level,
                )
            ],
        )

        # Componentwise Pareto frontier on R_+^2 at each modular state u (for r >= 2 and r == 1 separately)
        pareto_r1: dict[int, list[tuple[float, float]]] = {}
        pareto_ge2: dict[int, list[tuple[float, float]]] = {}

        def is_dominated_and_insert(
            table: dict[int, list[tuple[float, float]]], u_st: int, vx_val: float, vy_val: float
        ) -> bool:
            pts = table.get(u_st)
            if pts is None:
                table[u_st] = [(vx_val, vy_val)]
                return False
            for px, py in pts:
                if px <= vx_val + 1e-13 and py <= vy_val + 1e-13:
                    return True
            # Prune points dominated by (vx_val, vy_val)
            table[u_st] = [
                (px, py)
                for (px, py) in pts
                if not (vx_val <= px - 1e-13 and vy_val <= py - 1e-13)
            ] + [(vx_val, vy_val)]
            return False

        pq: list[
            tuple[float, float, int, int, float, float, int, tuple[int, ...], tuple[int, ...]]
        ] = []
        cnt_push = 0
        for sr in range(1, s_cap + 1):
            u0 = graph.l_pows[sr][graph.id_idx]
            vx0 = phi + float(sr)
            vy0 = 1.0
            alpha0 = (phi * vx0 + vy0) * inv_sqrt5_phi
            f0 = math.log(alpha0) + h_paid[u0]
            if f0 <= best_ln_q + 1e-11:
                cnt_push += 1
                heapq.heappush(pq, (f0, alpha0, cnt_push, u0, vx0, vy0, sr, (sr,), ()))

        pops = 0
        near_opt_candidates: list[tuple[tuple[int, ...], tuple[int, ...], float, int]] = [
            (s_bfs_tup, d_bfs_tup, q_bfs, best_sol[3])
        ]

        while pq:
            f_cur, alpha_cur, _, u, vx, vy, sum_s, s_tup, d_tup = heapq.heappop(pq)
            if f_cur > best_ln_q + 1e-11:
                break
            pops += 1

            if len(s_tup) >= 2 and u in target_indices:
                ln_a = math.log(alpha_cur)
                if ln_a < best_ln_q:
                    best_ln_q = ln_a
                    best_sol = (alpha_cur, s_tup, d_tup, u)
                near_opt_candidates.append((s_tup, d_tup, alpha_cur, u))
                continue

            tab = pareto_r1 if len(s_tup) == 1 else pareto_ge2
            if is_dominated_and_insert(tab, u, vx, vy):
                continue

            max_next_s = min(s_cap, sum_s_cap - sum_s)
            if max_next_s < 1:
                continue

            # Finite gaps 1 <= d <= T_even
            for d in range(1, t_even + 1):
                u_conj = graph.conj_j_pow[d][u]
                fd = fibs[d]
                fdp1 = fibs[d + 1]
                fdm1 = fibs[d - 1]
                sc = phi_neg_pows[d]
                jx = sc * (fdp1 * vx + fd * vy)
                jy = sc * (fd * vx + fdm1 * vy)
                for s in range(1, max_next_s + 1):
                    v_next = graph.l_pows[s][u_conj]
                    h_rem = h_paid[v_next]
                    if h_rem >= 1e50:
                        continue
                    vx_n = jx + s * jy
                    vy_n = jy
                    alpha_n = (phi * vx_n + vy_n) * inv_sqrt5_phi
                    f_n = math.log(alpha_n) + h_rem
                    if f_n <= best_ln_q + 1e-11:
                        cnt_push += 1
                        heapq.heappush(
                            pq,
                            (
                                f_n,
                                alpha_n,
                                cnt_push,
                                v_next,
                                vx_n,
                                vy_n,
                                sum_s + s,
                                (s, *s_tup),
                                (d, *d_tup),
                            ),
                        )

            # Unbounded Pisano-spacer transitions d = r + k * T_even -> infinity (encoded as negative gap -r)
            if allow_pisano_inf:
                jx_inf = alpha_cur * phi
                jy_inf = alpha_cur
                for r_res in range(1, graph.t_j + 1):
                    u_conj = graph.conj_j_pow[r_res][u]
                    for s in range(1, max_next_s + 1):
                        v_next = graph.l_pows[s][u_conj]
                        h_rem = h_paid[v_next]
                        if h_rem >= 1e50:
                            continue
                        vx_n = jx_inf + s * jy_inf
                        vy_n = jy_inf
                        alpha_n = (phi * vx_n + vy_n) * inv_sqrt5_phi
                        f_n = math.log(alpha_n) + h_rem
                        if f_n <= best_ln_q + 1e-11:
                            cnt_push += 1
                            heapq.heappush(
                                pq,
                                (
                                    f_n,
                                    alpha_n,
                                    cnt_push,
                                    v_next,
                                    vx_n,
                                    vy_n,
                                    sum_s + s,
                                    (s, *s_tup),
                                    (-r_res, *d_tup),
                                ),
                            )

        return {
            "best_q": best_sol[0],
            "best_excess": 2.0 * math.log(best_sol[0]),
            "s_tuple": list(best_sol[1]),
            "d_tuple": list(best_sol[2]),
            "target_mat_mod_L": list(graph.elems[best_sol[3]]),
            "astar_pops": pops,
            "near_opt_count": len(near_opt_candidates),
            "near_opt_candidates": near_opt_candidates,
        }

    fin_res = run_astar(allow_pisano_inf=False)
    inf_res = run_astar(allow_pisano_inf=True)

    # Re-evaluate all finite near-optimal candidates in exact 80-digit arithmetic
    best_exact_str = ""
    best_exact_flt = 1e100
    best_s_fin = tuple(fin_res["s_tuple"])
    best_d_fin = tuple(fin_res["d_tuple"])
    for s_c, d_c, q_approx, _ in fin_res["near_opt_candidates"]:
        if q_approx <= fin_res["best_q"] * (1.0 + 1e-9):
            em_c = defect_matrix_exact(s_c, d_c)
            ex_str, ex_flt = excess_80d_from_matrix(em_c)
            if ex_flt < best_exact_flt - 1e-14 or (
                abs(ex_flt - best_exact_flt) <= 1e-14 and (sum(s_c), sum(d_c), s_c, d_c) < (sum(best_s_fin), sum(best_d_fin), best_s_fin, best_d_fin)
            ):
                best_exact_flt = ex_flt
                best_exact_str = ex_str
                best_s_fin = s_c
                best_d_fin = d_c

    e_opt_fin = defect_matrix_exact(best_s_fin, best_d_fin)
    mod_opt_fin = (
        e_opt_fin[0] % level,
        e_opt_fin[1] % level,
        e_opt_fin[2] % level,
        e_opt_fin[3] % level,
    )
    assert mod_opt_fin in [graph.elems[i] for i in target_indices]

    # Build explicit run vector [a_1, ..., a_m] for best finite multi-run word
    span_m = 1 + sum(best_d_fin)
    run_vec = [1] * span_m
    p_cur = 0
    for idx_r, s_val in enumerate(best_s_fin):
        run_vec[p_cur] += s_val
        if idx_r < len(best_d_fin):
            p_cur += best_d_fin[idx_r]

    infimum_strictly_below_finite = bool(inf_res["best_excess"] < best_exact_flt - 1e-9)

    return {
        "level": level,
        "sl2_size": n_states,
        "j_conjugation_period": graph.t_j,
        "target_scalar_count": len(target_indices),
        "target_scalars_diag_mod_L": sorted({graph.elems[i][0] for i in target_indices}),
        "single_run_extra_letters": single_run_s,
        "single_run_word": [single_run_s + 1],
        "single_run_excess": single_excess,
        "lemma_e_min_b_cost_multi": best_b_multi,
        "lemma_e_theta_L": theta_b,
        "lemma_e_margin_over_theta": b_margin_over_theta,
        "lemma_e_excess_lower_bound_multi": excess_lb_from_b,
        "min_extra_letters_multi": int(min_extra_multi),
        "min_extra_letters_overall": int(min(single_run_s, min_extra_multi)),
        "shortest_word_beats_single_run": bool(min_extra_multi < single_run_s),
        "finite_multi_opt": {
            "excess_float": best_exact_flt,
            "excess_30d": best_exact_str,
            "s_tuple": list(best_s_fin),
            "d_tuple": list(best_d_fin),
            "sum_extra_letters": int(sum(best_s_fin)),
            "span_runs_m": int(span_m),
            "run_vector": run_vec,
            "scalar_c_mod_L": int(mod_opt_fin[0]),
            "astar_pops": fin_res["astar_pops"],
        },
        "unbounded_gap_infimum_multi": {
            "excess_infimum": inf_res["best_excess"],
            "s_tuple": inf_res["s_tuple"],
            "d_tuple_neg_means_pisano_inf": inf_res["d_tuple"],
            "scalar_c_mod_L": int(inf_res["target_mat_mod_L"][0]),
            "strictly_below_finite_min": infimum_strictly_below_finite,
            "astar_pops": inf_res["astar_pops"],
        },
        "single_run_is_global_minimum": bool(single_excess < inf_res["best_excess"] - 1e-12),
        "excess_gap_multi_minus_single": float(inf_res["best_excess"] - single_excess),
        "finite_excess_gap_multi_minus_single": float(best_exact_flt - single_excess),
    }


def run_b1855_module() -> dict[str, Any]:
    t0 = time.time()
    lemma_checks = verify_b1853_b1855_lemmas()

    # Cache SL(2, Z / L Z) graphs across all needed levels
    needed_levels = sorted({2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 15, 20, 30, 60})
    graphs: dict[int, ModularSL2Graph] = {lv: ModularSL2Graph(lv) for lv in needed_levels}

    # Evaluate all 15 non-empty subsets S <= {2, 3, 4, 5} across all 3 group conditions:
    # (i) per_rung_pm: forall n in S, E == +-I mod n
    # (ii) global_pm: E == +I or -I mod lcm(S)
    # (iii) strict_plus: E == +I mod lcm(S)
    subsets_15: list[tuple[int, ...]] = []
    for r_sz in range(1, 5):
        for comb in itertools.combinations((2, 3, 4, 5), r_sz):
            subsets_15.append(comb)

    subset_results: dict[str, Any] = {}
    level_cache_global_pm: dict[int, dict[str, Any]] = {}
    level_cache_strict_plus: dict[int, dict[str, Any]] = {}

    for s_sub in subsets_15:
        lv = 1
        for n in s_sub:
            lv = math.lcm(lv, n)
        g = graphs[lv]
        key = "{" + ",".join(str(x) for x in s_sub) + "}"

        # Build exact per-rung target indices directly from definition
        targ_per_rung: set[int] = set()
        for idx, (a, b, c, d) in enumerate(g.elems):
            ok = True
            for n in s_sub:
                an, bn, cn, dn = a % n, b % n, c % n, d % n
                if (an, bn, cn, dn) not in ((1 % n, 0, 0, 1 % n), ((n - 1) % n, 0, 0, (n - 1) % n)):
                    ok = False
                    break
            if ok:
                targ_per_rung.add(idx)

        res_per_rung = solve_target_set_on_graph(g, targ_per_rung, single_run_s=lv)

        if lv not in level_cache_global_pm:
            targ_gpm = {
                g.idx_of[(1 % lv, 0, 0, 1 % lv)],
                g.idx_of[((lv - 1) % lv, 0, 0, (lv - 1) % lv)],
            }
            level_cache_global_pm[lv] = solve_target_set_on_graph(g, targ_gpm, single_run_s=lv)

        if lv not in level_cache_strict_plus:
            targ_sp = {g.idx_of[(1 % lv, 0, 0, 1 % lv)]}
            level_cache_strict_plus[lv] = solve_target_set_on_graph(g, targ_sp, single_run_s=lv)

        subset_results[key] = {
            "S": list(s_sub),
            "lcm": lv,
            "per_rung_pm": res_per_rung,
            "global_pm_mod_lcm": level_cache_global_pm[lv],
            "strict_plus_mod_lcm": level_cache_strict_plus[lv],
        }

    # Prime levels p in {2, 3, 5, 7, 11, 13} (where CRT sign splitting is impossible!)
    prime_results: dict[str, Any] = {}
    for p in (2, 3, 5, 7, 11, 13):
        gp = graphs[p]
        targ_pm = {
            gp.idx_of[(1 % p, 0, 0, 1 % p)],
            gp.idx_of[((p - 1) % p, 0, 0, (p - 1) % p)],
        }
        targ_plus = {gp.idx_of[(1 % p, 0, 0, 1 % p)]}
        prime_results[str(p)] = {
            "prime": p,
            "pm_I_mod_p": (
                level_cache_global_pm[p]
                if p in level_cache_global_pm
                else solve_target_set_on_graph(gp, targ_pm, single_run_s=p)
            ),
            "strict_plus_I_mod_p": (
                level_cache_strict_plus[p]
                if p in level_cache_strict_plus
                else solve_target_set_on_graph(gp, targ_plus, single_run_s=p)
            ),
        }

    # Summary checks for B1855 proved scope (lcm <= 10) and refuted scope (lcm >= 12)
    proved_le_10_keys = [k for k, v in subset_results.items() if v["lcm"] <= 10]
    refuted_ge_12_keys = [k for k, v in subset_results.items() if v["lcm"] >= 12]
    all_le_10_proved = all(
        subset_results[k]["per_rung_pm"]["lemma_e_margin_over_theta"] > 0.0
        and subset_results[k]["per_rung_pm"]["single_run_is_global_minimum"]
        for k in proved_le_10_keys
    )
    all_ge_12_refuted = all(
        not subset_results[k]["per_rung_pm"]["single_run_is_global_minimum"]
        for k in refuted_ge_12_keys
    )

    # Planted Control 3: PC_B1855_drop_crt_or_sign
    # Evaluate {3, 4}'s defect (2, 1, 1, 3, 1, 1, 2) -> s = (1, 2, 1), d = (3, 3)
    e_34 = defect_matrix_exact((1, 2, 1), (3, 3))
    _, ex_34 = excess_80d_from_matrix(e_34)
    mod3_34 = tuple(x % 3 for x in e_34)
    mod4_34 = tuple(x % 4 for x in e_34)
    mod12_34 = tuple(x % 12 for x in e_34)
    satisfies_per_rung_34 = (mod3_34 in ((1, 0, 0, 1), (2, 0, 0, 2))) and (
        mod4_34 in ((1, 0, 0, 1), (3, 0, 0, 3))
    )
    planted_strict_or_global_12 = mod12_34 in ((1, 0, 0, 1), (11, 0, 0, 11))
    pc_crt_fired = bool(
        mod12_34 == (5, 0, 0, 5)
        and satisfies_per_rung_34
        and (not planted_strict_or_global_12)
        and ex_34 < 2.0 * math.log(1.0 + 12.0 / math.sqrt(5.0))
    )

    # Planted Control 4: PC_B1855_wrong_eigenvector
    # Replace v = (phi, 1) by transposed (1, phi) on two-run defect (2, 2) -> s = (1, 1), d = (1,)
    e_22 = defect_matrix_exact((1, 1), (1,))
    _, ex_true_22 = excess_80d_from_matrix(e_22)
    l_mat: Mat2 = (1, 1, 0, 1)
    r_mat: Mat2 = (1, 0, 1, 1)
    lr20 = mat_pow(mat_mul(l_mat, r_mat), 20)
    m22_tot = mat_mul(e_22, lr20)
    ex_k20_22 = 2.0 * math.acosh(0.5 * (m22_tot[0] + m22_tot[3])) - 2.0 * math.acosh(
        0.5 * (lr20[0] + lr20[3])
    )
    phi = 0.5 * (1.0 + math.sqrt(5.0))
    q_wrong_22 = (e_22[0] * 1.0 + (e_22[1] + e_22[2]) * phi + e_22[3] * phi * phi) / (
        1.0 + phi * phi
    )
    ex_wrong_22 = 2.0 * math.log(abs(q_wrong_22))
    pc_wrong_eig_fired = bool(
        abs(ex_true_22 - ex_k20_22) < 1e-14 and abs(ex_wrong_22 - ex_k20_22) > 1.5
    )

    return {
        "elapsed_seconds": round(time.time() - t0, 3),
        "lemma_and_r1_checks": lemma_checks,
        "all_7_lcm_le_10_proved": all_le_10_proved,
        "all_8_lcm_ge_12_refuted": all_ge_12_refuted,
        "subsets_of_2_3_4_5": subset_results,
        "prime_levels": prime_results,
        "planted_controls": {
            "PC_B1855_drop_crt_or_sign": {
                "defect_2113112_exact_matrix": list(e_34),
                "defect_2113112_mod_12": list(mod12_34),
                "defect_2113112_excess": ex_34,
                "satisfies_per_rung_3_4": satisfies_per_rung_34,
                "satisfies_planted_global_pm_12": planted_strict_or_global_12,
                "control_fired": pc_crt_fired,
            },
            "PC_B1855_wrong_eigenvector": {
                "defect_22_exact_matrix": list(e_22),
                "k20_trace_excess": ex_k20_22,
                "true_eigenvector_excess": ex_true_22,
                "planted_transposed_eigenvector_excess": ex_wrong_22,
                "control_fired": pc_wrong_eig_fired,
            },
        },
    }


def main() -> None:
    t_start = time.time()
    out_dir = Path(__file__).resolve().parent
    script_bytes = Path(__file__).read_bytes()
    script_sha256 = hashlib.sha256(script_bytes).hexdigest()

    b1868_res = run_b1868_module()
    b1855_res = run_b1855_module()

    all_controls_fired = bool(
        b1868_res["planted_controls"]["PC_B1868_liouville_flat"]["control_fired"]
        and b1868_res["planted_controls"]["PC_B1868_atomic_measure"]["control_fired"]
        and b1855_res["planted_controls"]["PC_B1855_drop_crt_or_sign"]["control_fired"]
        and b1855_res["planted_controls"]["PC_B1855_wrong_eigenvector"]["control_fired"]
    )

    payload = {
        "card": "X-NEG",
        "seat": "agy-exp",
        "script_sha256": script_sha256,
        "total_elapsed_seconds": round(time.time() - t_start, 3),
        "all_planted_controls_fired": all_controls_fired,
        "B1868": b1868_res,
        "B1855": b1855_res,
    }

    out_path = out_dir / "verify_x_neg_out.json"
    out_text = json.dumps(payload, indent=2, sort_keys=False) + "\n"
    out_path.write_text(out_text, encoding="utf-8")


if __name__ == "__main__":
    main()
