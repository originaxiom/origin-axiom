#!/usr/bin/env python3
"""
Standalone Zero-Import Verifier for Card X-MEASURE (with M23 Area Readout & M24 B1936 Audit)
============================================================================================
Seat: agy-exp
Pre-registered expectations commit: 2a67770de
  (relays/cards/AGY-EXP_X-MEASURE_measure-from-principle-and-area-readout.md)

Computes from scratch (zero imports from main; B1932's area_measure.json untouched):
  1. Exact Hyperbolic Poincare Area-Measure Readout on F = {|tau| >= 1, |Re tau| <= 1/2}
     with explicit cusp compactification u = 1/y in (0, 1/sqrt(1 - x^2)] and precision split:
       - Bulk y <= 5 (u >= 1/5): float64 Gauss-Legendre quadrature (coarse vs fine grid).
       - Mid-cusp 5 < y <= 55 (1/55 <= u < 1/5): arbitrary-precision mpmath SVD (dps=150)
         eliminating IEEE float64 singular-subspace underflow on mixing moduli |V_{ij}|.
       - Deep-cusp y > 55 (0 < u < 1/55): arbitrary-precision mpmath SVD (dps=300) + exact
         rational cusp limit verification at y = 80.
     Evaluated across all 4 combinations: (W_-, W_+) x (exact Theorem 90 weight, old weight),
     plus hard cusp-cutoff bias sweep Y_cut in {3, 5, 10, 20, infty} and naive float64 control.
  2. M25 Candidate 1 (Maximal Entropy / Abramov Formula):
     Mean hyperbolic step length <ell_step> on {L, R}^+ and geodesic-flow entropy
     h_flow(mu_move) = ln(2) / <ell_step> < 1 = h_flow(mu_area).
  3. M25 Candidate 2 (Invariance Under Refining the Level 5 -> 10 -> 15):
     Exact Markov spectral gaps on SL(2, Z/NZ) for N in {5, 10, 15} and paired/independent
     ergodic move-count trajectories conditioned on level-5, level-10, and level-15 admissibility.
  4. M25 Candidate 3 (Pairs Rule P-Q7 Generator Rewriting & Same-Monoid Dual Filtration):
     - Literal <J, K> dihedral trap check (PC_MEAS_3).
     - Generator rewriting test (PC_MEAS_4): {L, R}^+ vs tick-and-swap {J, J^{-1}, P} (even #P)
       vs undoing-symmetrized {L, R, L^{-1}, R^{-1}} at word length n = 28 via 60-digit mpmath
       geodesic reduction.
     - Exhaustive trace-monotone enumeration of primitive Lyndon geodesics in the SAME {L, R}^+
       allowed monoid filtered by hyperbolic geodesic length ell(W) <= L_0 (tr(W) <= 15, 35, 75),
       demonstrating convergence from mu_move toward mu_area under proper-length filtration.
  5. M24 Cold Read Algebraic Verification of B1936:
     Exhaustive test of all 4 multipliers m in (Z/5Z)^x and both Z_2 parity-to-holomorphy rules
     (spinor same-parity Pi_+ vs super-graded fundamental-vector opposite-parity Pi_-).

Strict Firewall & Mask Hygiene:
  - 0 of 19: zero measured/PDG numbers anywhere.
  - Zero decimal floats or scientific notation printed to stdout; values in JSON only.
  - Strictly position-indexed (sector, index) names; zero particle names anywhere.
"""

from __future__ import annotations

import cmath
import hashlib
import json
import math
import pathlib
import random
import time
from fractions import Fraction
from multiprocessing import Pool
from typing import Any, Dict, List, Optional, Tuple

import mpmath as mp
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import eigs as sparse_eigs
from scipy.special import digamma, roots_legendre

HERE = pathlib.Path(__file__).resolve().parent
OUT_JSON = HERE / "verify_x_measure_out.json"

EULER_GAMMA = 0.5772156649015328606065120900824024310421
NORM_CONST_SHIFT = EULER_GAMMA + math.log(math.pi)


# ============================================================================
# SECTION 1: PUNCTURED-TORUS CANONICAL END L_2(tau) (4-TRACE GAUSS-NEWTON + CHEBYSHEV)
# ============================================================================

def _seg_lat_dist_f(ax: float, ay: float, bx: float, by: float, tx: float, ty: float) -> float:
    dx, dy = bx - ax, by - ay
    sl2 = dx * dx + dy * dy
    dmin = 1e9
    for m in range(-3, 4):
        for n in range(-3, 4):
            px, py = m + n * tx, n * ty
            tcl = max(0.0, min(1.0, ((px - ax) * dx + (py - ay) * dy) / sl2)) if sl2 > 1e-30 else 0.0
            d = math.hypot(px - (ax + tcl * dx), py - (ay + tcl * dy))
            if d < dmin:
                dmin = d
    return dmin


def _wp_and_wp_prime_f64(z: complex, tau: complex) -> Tuple[complex, complex]:
    pi = math.pi
    pi2 = pi * pi
    pi3 = pi2 * pi
    k_sh = round(z.imag / tau.imag)
    if k_sh:
        z = z - k_sh * tau
    s0 = cmath.sin(pi * z)
    c0 = cmath.cos(pi * z)
    invs0 = 1.0 / s0
    invs0_2 = invs0 * invs0
    wp = pi2 * invs0_2 - pi2 / 3.0
    wpp = -2.0 * pi3 * c0 * invs0_2 * invs0
    ty = tau.imag
    m_max = 0 if ty > 14.0 else (int(math.ceil(6.8 / ty)) + 1)
    for m in range(1, m_max + 1):
        mt = m * tau
        zm_p = pi * (z + mt)
        zm_m = pi * (z - mt)
        p_mt = pi * mt
        sp, cp = cmath.sin(zm_p), cmath.cos(zm_p)
        sm, cm = cmath.sin(zm_m), cmath.cos(zm_m)
        st = cmath.sin(p_mt)
        isp2 = 1.0 / (sp * sp)
        ism2 = 1.0 / (sm * sm)
        ist2 = 1.0 / (st * st)
        wp += pi2 * (isp2 + ism2 - 2.0 * ist2)
        wpp += -2.0 * pi3 * (cp * isp2 / sp + cm * ism2 / sm)
    return wp, wpp


def _eisenstein_g2_g3_E2_f64(tau: complex) -> Tuple[complex, complex, complex]:
    q = cmath.exp(2j * math.pi * tau)
    e2 = 1.0 + 0j
    e4 = 1.0 + 0j
    e6 = 1.0 + 0j
    qn = q
    for n in range(1, 80):
        if abs(qn) < 1e-18:
            break
        lam = qn / (1.0 - qn)
        e2 -= 24.0 * n * lam
        e4 += 240.0 * (n ** 3) * lam
        e6 -= 504.0 * (n ** 5) * lam
        qn *= q
    pi = math.pi
    return (4.0 * (pi ** 4) / 3.0) * e4, (8.0 * (pi ** 6) / 27.0) * e6, e2


def _lame_frob_f64(z: complex, g2: complex, g3: complex, c_acc: complex, n_terms: int = 24) -> np.ndarray:
    c_wp = [0j] * (n_terms + 2)
    c_wp[1] = g2 / 20.0
    c_wp[2] = g3 / 28.0
    for k in range(3, n_terms + 2):
        s = 0j
        for m in range(1, k - 1):
            s += c_wp[m] * c_wp[k - 1 - m]
        c_wp[k] = (3.0 / ((2 * k + 3) * (k - 2))) * s
    qcoeffs = [c_acc] + [c_wp[k] / 4.0 for k in range(1, n_terms + 1)]
    a = [1.0 + 0j]
    b = [0.0 + 0j]
    for n in range(1, n_terms):
        sa = 0j
        for m in range(n):
            sa += qcoeffs[n - 1 - m] * a[m]
        an = -sa / (4.0 * n * n)
        sb = 0j
        for m in range(1, n):
            sb += qcoeffs[n - 1 - m] * b[m]
        bn = -(4.0 * n * an + sb) / (4.0 * n * n)
        a.append(an)
        b.append(bn)
    sz = cmath.sqrt(z)
    lz = cmath.log(z)
    z2 = z * z
    zp = 1.0 + 0j
    s_y1 = s_dy1 = s_h = s_dh = 0j
    for n in range(n_terms):
        en = 2.0 * n + 0.5
        s_y1 += a[n] * zp
        s_dy1 += en * a[n] * zp / z
        s_h += b[n] * zp
        s_dh += en * b[n] * zp / z
        zp *= z2
    y1 = sz * s_y1
    dy1 = sz * s_dy1
    h = sz * s_h
    dh = sz * s_dh
    y2 = y1 * lz + h
    dy2 = dy1 * lz + y1 / z + dh
    fac = -1j / (2.0 * math.pi)
    return np.array([[fac * y2, fac * dy2], [y1, dy1]], dtype=np.complex128)


def _taylor_prop_f64(
    Y_init: np.ndarray,
    z_start: complex,
    z_end: complex,
    tau: complex,
    g2: complex,
    c_acc: complex,
    n_steps: int = 24,
    order: int = 18,
) -> np.ndarray:
    if abs(z_end - z_start) < 1e-16:
        return Y_init.copy()
    h = (z_end - z_start) / n_steps
    y00, y01 = complex(Y_init[0, 0]), complex(Y_init[0, 1])
    y10, y11 = complex(Y_init[1, 0]), complex(Y_init[1, 1])
    z = z_start
    g2_q = 0.25 * g2
    p = [0j] * (order + 1)
    q = [0j] * order
    u0 = [0j] * (order + 1)
    u1 = [0j] * (order + 1)
    for _ in range(n_steps):
        p0, p1 = _wp_and_wp_prime_f64(z, tau)
        p[0], p[1] = p0, p1
        p[2] = 3.0 * p0 * p0 - g2_q
        for k in range(3, order):
            s = 0j
            for j in range(k - 1):
                s += p[j] * p[k - 2 - j]
            p[k] = (6.0 / (k * (k - 1))) * s
        q[0] = p0 / 4.0 + c_acc
        for k in range(1, order):
            q[k] = p[k] / 4.0
        u0[0], u0[1] = y00, y01
        u1[0], u1[1] = y10, y11
        for k in range(2, order + 1):
            inv = -1.0 / (k * (k - 1))
            s0 = s1 = 0j
            for j in range(k - 1):
                qj = q[j]
                s0 += qj * u0[k - 2 - j]
                s1 += qj * u1[k - 2 - j]
            u0[k] = inv * s0
            u1[k] = inv * s1
        v0 = u0[order]
        v1 = u1[order]
        dv0 = order * u0[order]
        dv1 = order * u1[order]
        for k in range(order - 1, 0, -1):
            v0 = v0 * h + u0[k]
            v1 = v1 * h + u1[k]
            dv0 = dv0 * h + k * u0[k]
            dv1 = dv1 * h + k * u1[k]
        y00 = v0 * h + u0[0]
        y10 = v1 * h + u1[0]
        y01 = dv0
        y11 = dv1
        z += h
    return np.array([[y00, y01], [y10, y11]], dtype=np.complex128)


def _prop_const_f64(Y_init: np.ndarray, dz: complex, q_const: complex) -> np.ndarray:
    om = cmath.sqrt(q_const)
    w = om * dz
    cw = cmath.cos(w)
    sw_om = dz if abs(w) < 1e-8 else cmath.sin(w) / om
    mat_prop_t = np.array([[cw, -q_const * sw_om], [sw_om, cw]], dtype=np.complex128)
    return Y_init @ mat_prop_t


def _lame_mono_f64(tau: complex, c_acc: complex) -> Tuple[np.ndarray, np.ndarray]:
    g2, g3, E2 = _eisenstein_g2_g3_E2_f64(tau)
    tx, ty = tau.real, tau.imag
    z0 = (-0.5 - 0.5 * tau) if ty <= 3.0 else (-0.5 - 1.0j)
    min_per = min(abs(m + n * tau) for m in range(-2, 3) for n in range(-2, 3) if (m, n) != (0, 0))
    r_target = min(0.20 * min_per, 0.45 * abs(z0))
    zf = z0 * (r_target / abs(z0))
    Yf = _lame_frob_f64(zf, g2, g3, c_acc, n_terms=24)
    q_asymp = -(math.pi ** 2 / 12.0) * E2 + c_acc

    def sp_f64(Y_in: np.ndarray, za: complex, zb: complex) -> np.ndarray:
        d_seg = max(1e-4, _seg_lat_dist_f(za.real, za.imag, zb.real, zb.imag, tx, ty))
        n_st = max(24, int(math.ceil(abs(zb - za) / (0.06 * d_seg))))
        return _taylor_prop_f64(Y_in, za, zb, tau, g2, c_acc, n_steps=n_st, order=18)

    Y0 = sp_f64(Yf, zf, z0)
    YA = sp_f64(Y0, z0, z0 + 1.0)
    zb = z0 + tau
    if ty > 14.0:
        za1 = z0 + (2.5 / ty) * tau
        z1 = z0 + (6.8 / ty) * tau
        z2 = z0 + ((ty - 5.8) / ty) * tau
        zb1 = z0 + ((ty - 0.5) / ty) * tau
        Ym = sp_f64(sp_f64(Y0, z0, za1), za1, z1)
        Ym = _prop_const_f64(Ym, z2 - z1, q_asymp)
        YB = sp_f64(sp_f64(Ym, z2, zb1), zb1, zb)
    elif ty > 4.0:
        za1 = z0 + (2.5 / ty) * tau
        zb1 = z0 + ((ty - 0.5) / ty) * tau
        YB = sp_f64(sp_f64(sp_f64(Y0, z0, za1), za1, zb1), zb1, zb)
    else:
        YB = sp_f64(Y0, z0, zb)
    return YA @ np.linalg.inv(Y0), YB @ np.linalg.inv(Y0)


def _g4_f64(MA: np.ndarray, MB: np.ndarray) -> np.ndarray:
    MAB = MA @ MB
    MABi = MA @ np.linalg.inv(MB)
    return np.array(
        [
            MA[0, 0] + MA[1, 1],
            MB[0, 0] + MB[1, 1],
            MAB[0, 0] + MAB[1, 1],
            MABi[0, 0] + MABi[1, 1],
        ],
        dtype=np.complex128,
    )


def _gn_solve_f64(ts: complex, c_init: complex, eps: float = 1e-8) -> complex:
    c_cur = c_init
    for _ in range(10):
        MA, MB = _lame_mono_f64(ts, c_cur)
        g0 = _g4_f64(MA, MB)
        r0 = g0.imag
        if np.max(np.abs(r0)) < 1e-13:
            break
        MA_p, MB_p = _lame_mono_f64(ts, c_cur + eps)
        dg = (_g4_f64(MA_p, MB_p) - g0) / eps
        J = np.column_stack([dg.imag, dg.real])
        dc = np.linalg.solve(J.T @ J, J.T @ (-r0))
        c_cur += complex(float(dc[0]), float(dc[1]))
    return c_cur


def _extract_L2_from_mono(tau: complex, c_cur: complex) -> float:
    MA, MB = _lame_mono_f64(tau, c_cur)
    comm = MA @ MB @ np.linalg.inv(MA) @ np.linalg.inv(MB)
    lam = abs(comm[0, 1].real)
    assert abs(lam - 1.0) < 1e-9
    imB_A = -MA[0, 0].imag / MA[1, 0].real
    imB_B = -MB[0, 0].imag / MB[1, 0].real
    assert abs(imB_A - imB_B) < 1e-10
    imB = 0.5 * (imB_A + imB_B)
    return math.pi - (2.0 * math.pi / lam) * imB


def uniformize_L2_raw_fast(tau: complex) -> float:
    ty = tau.imag
    if abs(tau - 1j) < 1e-14 or abs(tau - cmath.exp(1j * math.pi / 3.0)) < 1e-14:
        c_cur = 0j
    elif ty >= 4.0:
        t_anc = complex(tau.real, 3.0)
        c_cur = 0j
        for st in range(1, 3):
            c_cur = _gn_solve_f64((1.0 - st / 2.0) * 1j + (st / 2.0) * t_anc, c_cur)
        n_up = max(1, int(math.ceil(math.log(ty / 3.0) / 0.55)))
        for st in range(1, n_up + 1):
            ys = 3.0 * ((ty / 3.0) ** (st / n_up))
            c_cur = _gn_solve_f64(complex(tau.real, ys), c_cur)
    else:
        n_h = max(1, min(4, int(math.ceil(abs(tau - 1j) / 1.2))))
        c_cur = 0j
        for st in range(1, n_h + 1):
            c_cur = _gn_solve_f64((1.0 - st / n_h) * 1j + (st / n_h) * tau, c_cur)
    return _extract_L2_from_mono(tau, c_cur)


def _uniformize_column_L2_fast(args: Tuple[float, List[float]]) -> List[float]:
    xv, ys = args
    order = sorted(range(len(ys)), key=lambda idx: ys[idx])
    res: List[float] = [0.0] * len(ys)
    c_prev: Optional[complex] = None
    y_prev: float = 1.0
    for idx in order:
        yv = ys[idx]
        tau = complex(xv, yv)
        if abs(tau - 1j) < 1e-14 or abs(tau - cmath.exp(1j * math.pi / 3.0)) < 1e-14:
            c_cur = 0j
        elif c_prev is None:
            if yv >= 4.0:
                t_anc = complex(xv, 3.0)
                c_cur = 0j
                for st in range(1, 3):
                    c_cur = _gn_solve_f64((1.0 - st / 2.0) * 1j + (st / 2.0) * t_anc, c_cur)
                n_up = max(1, int(math.ceil(math.log(yv / 3.0) / 0.55)))
                for st in range(1, n_up + 1):
                    ys_s = 3.0 * ((yv / 3.0) ** (st / n_up))
                    c_cur = _gn_solve_f64(complex(xv, ys_s), c_cur)
            else:
                n_h = max(1, min(4, int(math.ceil(abs(tau - 1j) / 1.2))))
                c_cur = 0j
                for st in range(1, n_h + 1):
                    c_cur = _gn_solve_f64((1.0 - st / n_h) * 1j + (st / n_h) * tau, c_cur)
        else:
            c_cur = c_prev
            n_up = max(1, int(math.ceil(abs(math.log(yv / y_prev)) / 0.55)))
            for st in range(1, n_up + 1):
                ys_s = y_prev * ((yv / y_prev) ** (st / n_up))
                c_cur = _gn_solve_f64(complex(xv, ys_s), c_cur)
        c_prev = c_cur
        y_prev = yv
        res[idx] = _extract_L2_from_mono(tau, c_cur)
    return res


def _cheb_nodes_weights(n: int) -> Tuple[np.ndarray, np.ndarray]:
    j = np.arange(n, dtype=np.float64)
    nodes = -np.cos(math.pi * j / (n - 1))
    w = ((-1.0) ** j) * np.ones(n, dtype=np.float64)
    w[0] *= 0.5
    w[-1] *= 0.5
    return nodes, w


def _bary_weights_batch(u: np.ndarray, nodes: np.ndarray, w: np.ndarray) -> np.ndarray:
    diff = u[:, None] - nodes[None, :]
    exact = np.abs(diff) < 1e-14
    diff_safe = np.where(exact, 1.0, diff)
    ker = w[None, :] / diff_safe
    mat = ker / np.sum(ker, axis=1, keepdims=True)
    if np.any(exact):
        rows, cols = np.where(exact)
        mat[rows, :] = 0.0
        mat[rows, cols] = 1.0
    return mat


class CanonicalL2Evaluator:
    def __init__(self, n_workers: int = 10):
        self.p1_nx, self.p1_ny = 18, 18
        self.p2_nx, self.p2_ny = 14, 18
        self.p3_nx, self.p3_ny = 10, 18
        self.p4_nx, self.p4_ny = 8, 16

        self.x1, self.wx1 = _cheb_nodes_weights(self.p1_nx)
        self.y1, self.wy1 = _cheb_nodes_weights(self.p1_ny)
        self.x2, self.wx2 = _cheb_nodes_weights(self.p2_nx)
        self.y2, self.wy2 = _cheb_nodes_weights(self.p2_ny)
        self.x3, self.wx3 = _cheb_nodes_weights(self.p3_nx)
        self.y3, self.wy3 = _cheb_nodes_weights(self.p3_ny)
        self.x4, self.wx4 = _cheb_nodes_weights(self.p4_nx)
        self.y4, self.wy4 = _cheb_nodes_weights(self.p4_ny)

        col_tasks: List[Tuple[float, List[float]]] = []
        for u_x in self.x1:
            xv = 0.25 * (u_x + 1.0)
            ylo = math.sqrt(max(0.0, 1.0 - xv * xv))
            col_tasks.append((xv, [ylo + (1.85 - ylo) * 0.5 * (u_y + 1.0) for u_y in self.y1]))
        for u_x in self.x2:
            xv = 0.25 * (u_x + 1.0)
            col_tasks.append((xv, [1.85 + (4.50 - 1.85) * 0.5 * (u_y + 1.0) for u_y in self.y2]))
        for u_x in self.x3:
            xv = 0.25 * (u_x + 1.0)
            col_tasks.append((xv, [4.50 + (12.0 - 4.50) * 0.5 * (u_y + 1.0) for u_y in self.y3]))
        u_lo, u_hi = 1.0 / 38.0, 1.0 / 12.0
        for u_x in self.x4:
            xv = 0.25 * (u_x + 1.0)
            col_tasks.append((xv, [1.0 / (u_lo + (u_hi - u_lo) * 0.5 * (u_y + 1.0)) for u_y in self.y4]))

        with Pool(n_workers) as pool:
            col_vals = pool.map(_uniformize_column_L2_fast, col_tasks)
        arr = np.array([item for col in col_vals for item in col], dtype=np.float64)

        n1 = self.p1_nx * self.p1_ny
        n2 = self.p2_nx * self.p2_ny
        n3 = self.p3_nx * self.p3_ny
        n4 = self.p4_nx * self.p4_ny
        i0 = 0
        self.v1 = arr[i0:i0 + n1].reshape(self.p1_nx, self.p1_ny); i0 += n1
        self.v2 = arr[i0:i0 + n2].reshape(self.p2_nx, self.p2_ny); i0 += n2
        self.v3 = arr[i0:i0 + n3].reshape(self.p3_nx, self.p3_ny); i0 += n3
        self.v4 = arr[i0:i0 + n4].reshape(self.p4_nx, self.p4_ny)

        # Fit exact cusp spine L_2(i*y) = L2_inf + c1*(1/y^2) + c2*(1/y^4) on y = 18, 26, 36
        spine_ys = [18.0, 26.0, 36.0]
        spine_l2 = [uniformize_L2_raw_fast(complex(0.0, yv)) for yv in spine_ys]
        A_sp = np.array([[1.0, 1.0 / (yv * yv), 1.0 / (yv ** 4)] for yv in spine_ys], dtype=np.float64)
        self.cusp_poly = np.linalg.solve(A_sp, np.array(spine_l2, dtype=np.float64))
        self.L2_cusp_inf = float(self.cusp_poly[0])

    def eval_L2_raw_batch(self, tau_red: np.ndarray) -> np.ndarray:
        xv = np.clip(np.abs(tau_red.real), 0.0, 0.5)
        yv = tau_red.imag
        raw_l2 = np.empty(len(tau_red), dtype=np.float64)
        m1 = yv <= 1.85
        m2 = (yv > 1.85) & (yv <= 4.50)
        m3 = (yv > 4.50) & (yv <= 12.0)
        m4 = (yv > 12.0) & (yv <= 38.0)
        m5 = yv > 38.0
        if np.any(m1):
            xx, yy = xv[m1], yv[m1]
            ylo = np.sqrt(np.maximum(0.0, 1.0 - xx * xx))
            sv = np.clip((yy - ylo) / (1.85 - ylo), 0.0, 1.0)
            bx = _bary_weights_batch(4.0 * xx - 1.0, self.x1, self.wx1)
            by = _bary_weights_batch(2.0 * sv - 1.0, self.y1, self.wy1)
            raw_l2[m1] = np.einsum("ni,ij,nj->n", bx, self.v1, by)
        if np.any(m2):
            xx, yy = xv[m2], yv[m2]
            bx = _bary_weights_batch(4.0 * xx - 1.0, self.x2, self.wx2)
            by = _bary_weights_batch(2.0 * (yy - 1.85) / (4.50 - 1.85) - 1.0, self.y2, self.wy2)
            raw_l2[m2] = np.einsum("ni,ij,nj->n", bx, self.v2, by)
        if np.any(m3):
            xx, yy = xv[m3], yv[m3]
            bx = _bary_weights_batch(4.0 * xx - 1.0, self.x3, self.wx3)
            by = _bary_weights_batch(2.0 * (yy - 4.50) / (12.0 - 4.50) - 1.0, self.y3, self.wy3)
            raw_l2[m3] = np.einsum("ni,ij,nj->n", bx, self.v3, by)
        if np.any(m4):
            xx, inv_y = xv[m4], 1.0 / yv[m4]
            u_lo, u_hi = 1.0 / 38.0, 1.0 / 12.0
            bx = _bary_weights_batch(4.0 * xx - 1.0, self.x4, self.wx4)
            by = _bary_weights_batch(2.0 * (inv_y - u_lo) / (u_hi - u_lo) - 1.0, self.y4, self.wy4)
            raw_l2[m4] = np.einsum("ni,ij,nj->n", bx, self.v4, by)
        if np.any(m5):
            inv_y2 = 1.0 / (yv[m5] * yv[m5])
            raw_l2[m5] = self.cusp_poly[0] + self.cusp_poly[1] * inv_y2 + self.cusp_poly[2] * (inv_y2 * inv_y2)
        return raw_l2

    def eval_tilde_L2_batch(self, tau_red: np.ndarray) -> np.ndarray:
        raw_l2 = self.eval_L2_raw_batch(tau_red)
        return raw_l2 + 0.5 * np.log(tau_red.imag) - NORM_CONST_SHIFT


# ============================================================================
# SECTION 2: EXACT RATIONAL SERRE B[1], FLOAT64 & ARBITRARY-PRECISION MPMATH FRAME C
# ============================================================================

def _build_serre_B1_exact(max_k: int = 168) -> Tuple[np.ndarray, np.ndarray, List[Tuple[int, List[Tuple[Fraction, Fraction]]]]]:
    N = max_k

    def s_mul(a: Dict[int, Tuple[Fraction, Fraction]], b: Dict[int, Tuple[Fraction, Fraction]]):
        out: Dict[int, Tuple[Fraction, Fraction]] = {}
        for ka, (ar, ai) in a.items():
            for kb, (br, bi) in b.items():
                k = ka + kb
                if k <= N:
                    pr, pi_ = out.get(k, (Fraction(0), Fraction(0)))
                    out[k] = (pr + ar * br - ai * bi, pi_ + ar * bi + ai * br)
        return {k: v for k, v in out.items() if v[0] or v[1]}

    def s_inv(a: Dict[int, Tuple[Fraction, Fraction]]):
        k0 = min(a)
        c0r, c0i = a[k0]
        d = c0r * c0r + c0i * c0i
        inv0 = (c0r / d, -c0i / d)
        M = N + k0
        sj = [a.get(k0 + j, (Fraction(0), Fraction(0))) for j in range(M + 1)]
        t: List[Tuple[Fraction, Fraction]] = [inv0]
        for m in range(1, M + 1):
            ar, ai = Fraction(0), Fraction(0)
            for j in range(1, m + 1):
                sr, si = sj[j]
                if sr or si:
                    tr, ti = t[m - j]
                    ar += sr * tr - si * ti
                    ai += sr * ti + si * tr
            t.append((-(inv0[0] * ar - inv0[1] * ai), -(inv0[0] * ai + inv0[1] * ar)))
        return {m - k0: t[m] for m in range(M + 1) if m - k0 <= N and (t[m][0] or t[m][1])}

    th2: Dict[int, Tuple[Fraction, Fraction]] = {}
    n = 0
    while (2 * n + 1) ** 2 <= N:
        th2[(2 * n + 1) ** 2] = (Fraction(2), Fraction(0))
        n += 1
    th3: Dict[int, Tuple[Fraction, Fraction]] = {0: (Fraction(1), Fraction(0))}
    th4: Dict[int, Tuple[Fraction, Fraction]] = {0: (Fraction(1), Fraction(0))}
    n = 1
    while 4 * n * n <= N:
        th3[4 * n * n] = (Fraction(2), Fraction(0))
        th4[4 * n * n] = (Fraction(2 * ((-1) ** n)), Fraction(0))
        n += 1

    e2: Dict[int, Tuple[Fraction, Fraction]] = {0: (Fraction(1), Fraction(0))}
    for m in range(1, N // 8 + 1):
        sig1 = sum(d for d in range(1, m + 1) if m % d == 0)
        e2[8 * m] = (Fraction(-24 * sig1), Fraction(0))

    di = s_inv(s_mul(s_mul(th2, th3), th4))
    R0 = {k: (-v[0], -v[1]) for k, v in s_mul(s_mul(th2, th2), di).items()}
    R1 = {k: (-v[0], -v[1]) for k, v in s_mul(s_mul(th4, th4), di).items()}
    R2 = s_mul(s_mul(s_mul(th3, th3), {0: (Fraction(0), Fraction(1))}), di)

    def serre_mhalf(f: Dict[int, Tuple[Fraction, Fraction]]):
        qdf = {k: (v[0] * Fraction(k, 8), v[1] * Fraction(k, 8)) for k, v in f.items() if k != 0}
        e2f = s_mul(e2, f)
        out = dict(qdf)
        for k, (r, im) in e2f.items():
            pr, pi_ = out.get(k, (Fraction(0), Fraction(0)))
            out[k] = (pr + r * Fraction(1, 24), pi_ + im * Fraction(1, 24))
        return out

    B1 = [serre_mhalf(R0), serre_mhalf(R1), serre_mhalf(R2)]
    all_ks = sorted(set().union(*(d.keys() for d in B1)))
    ks_arr = np.array(all_ks, dtype=np.int64)
    mat = np.zeros((len(all_ks), 3), dtype=np.complex128)
    exact_rows: List[Tuple[int, List[Tuple[Fraction, Fraction]]]] = []
    for row, k in enumerate(all_ks):
        cols_frac = []
        for col, d in enumerate(B1):
            fr, fi = d.get(k, (Fraction(0), Fraction(0)))
            cols_frac.append((fr, fi))
            if fr or fi:
                mat[row, col] = complex(float(fr), float(fi))
        exact_rows.append((k, cols_frac))
    return ks_arr, mat, exact_rows


def _build_coupling_tensor() -> np.ndarray:
    i2 = np.eye(2, dtype=np.complex128)
    qi = np.array([[1j, 0.0], [0.0, -1j]], dtype=np.complex128)
    qj = np.array([[0.0, 1.0], [-1.0, 0.0]], dtype=np.complex128)
    qk = qi @ qj
    eps = qj
    units = [i2, qi, qj, qk]
    ec = [eps @ u for u in units]
    G = np.array([[np.sum(ec[t] * units[s]) for s in range(4)] for t in range(4)], dtype=np.complex128)
    Gi = np.linalg.inv(G)
    edual = [sum(Gi[b, a] * units[b] for b in range(4)) for a in range(4)]
    blocks = [qj, qi, qk]
    higgs_units = [qi, qj, qk]
    T = np.zeros((3, 4, 3, 3), dtype=np.complex128)
    for alpha in range(3):
        S_unit = higgs_units[alpha]
        for s_idx in range(4):
            M_unit = edual[s_idx]
            for ra in range(3):
                for cb in range(3):
                    T[alpha, s_idx, ra, cb] = np.sum((blocks[ra].T @ eps @ S_unit @ blocks[cb]) * M_unit)
    return T


SERRE_KS, SERRE_MAT, SERRE_EXACT_ROWS = _build_serre_B1_exact(168)
T_COUP = _build_coupling_tensor()
# Nonzero entries of T_COUP as exact half-integers (real*2, imag*2)
T_COUP_NZ: List[Tuple[int, int, int, int, int, int]] = []
for _al in range(3):
    for _si in range(4):
        for _ra in range(3):
            for _cb in range(3):
                _v = T_COUP[_al, _si, _ra, _cb]
                if abs(_v) > 1e-14:
                    _tr2 = int(round(_v.real * 2.0))
                    _ti2 = int(round(_v.imag * 2.0))
                    assert abs(_v - complex(_tr2 / 2.0, _ti2 / 2.0)) < 1e-14
                    T_COUP_NZ.append((_al, _si, _ra, _cb, _tr2, _ti2))

SIX_CHARGES = {
    "up": (1, -4),
    "down": (1, 2),
    "lepton": (-3, 6),
}

P5_HALF_12_INT: List[Tuple[int, int]] = []
_seen_p5 = set()
for _j in range(5):
    for _k in range(5):
        if (_j, _k) == (0, 0):
            continue
        _neg = ((-_j) % 5, (-_k) % 5)
        if (_j, _k) not in _seen_p5 and _neg not in _seen_p5:
            P5_HALF_12_INT.append((_j, _k))
            _seen_p5.add((_j, _k))
            _seen_p5.add(_neg)
assert len(P5_HALF_12_INT) == 12
P5_HALF_12: List[Tuple[float, float]] = [(j / 5.0, k / 5.0) for (j, k) in P5_HALF_12_INT]

OUTPUT_KEYS_12 = (
    "up__2_over_3",
    "up__1_over_3",
    "up__1_over_2",
    "down__2_over_3",
    "down__1_over_3",
    "down__1_over_2",
    "lepton__2_over_3",
    "lepton__1_over_3",
    "lepton__1_over_2",
    "mixing__1_2",
    "mixing__2_3",
    "mixing__1_3",
)

CLAIMED_7_FRAME_CODE = (
    "up__2_over_3",
    "up__1_over_3",
    "down__2_over_3",
    "down__1_over_3",
    "mixing__1_2",
    "mixing__2_3",
    "mixing__1_3",
)

CLAIMED_7_ADJACENT = (
    "up__1_over_2",
    "up__2_over_3",
    "down__1_over_2",
    "down__2_over_3",
    "mixing__1_2",
    "mixing__2_3",
    "mixing__1_3",
)


def _theta_char_batch(alpha: np.ndarray, beta: np.ndarray, tau: np.ndarray) -> np.ndarray:
    a_tilde = alpha - np.rint(alpha)
    ks = np.arange(-7, 8, dtype=np.float64)[None, :]
    m = ks + a_tilde[:, None]
    exponent = 1j * math.pi * tau[:, None] * (m * m) + 2j * math.pi * m * beta[:, None]
    return np.sum(np.exp(exponent), axis=1)


def _a0_closed_batch(alpha: np.ndarray, beta: np.ndarray, tau: np.ndarray) -> np.ndarray:
    a_tilde = alpha - np.rint(alpha)
    ks = np.arange(-7, 8, dtype=np.float64)[None, :]
    m = ks + a_tilde[:, None]
    terms = np.exp(1j * math.pi * tau[:, None] * (m * m) + 2j * math.pi * m * beta[:, None])
    denom = np.sum(terms, axis=1)
    numer = 2j * math.pi * np.sum(m * terms, axis=1)
    return numer / denom


def _th1_prime_0_batch(tau: np.ndarray) -> np.ndarray:
    ks = np.arange(8, dtype=np.float64)[None, :]
    h = ks + 0.5
    signs = ((-1.0) ** ks) * (2.0 * ks + 1.0)
    return 2.0 * math.pi * np.sum(signs * np.exp(1j * math.pi * tau[:, None] * (h * h)), axis=1)


def _residues_closed_batch(tau: np.ndarray, a: np.ndarray, b: np.ndarray, qL: int, qR: int) -> np.ndarray:
    ap = (qL + qR) * a
    bp = (qL + qR) * b
    am = (qL - qR) * a
    bm = (qL - qR) * b
    th1p0 = _th1_prime_0_batch(tau)

    phase_1 = np.exp(-1j * math.pi * (ap + am))
    R_1 = (-1j) * phase_1 * _theta_char_batch(ap + 0.5, bp + 0.5, tau) * _theta_char_batch(am + 0.5, bm + 0.5, tau) / th1p0
    R_i = (-1.0) * _theta_char_batch(ap + 0.5, bp, tau) * _theta_char_batch(am + 0.5, bm, tau) / th1p0
    R_j = (-1.0) * phase_1 * _theta_char_batch(ap, bp + 0.5, tau) * _theta_char_batch(am, bm + 0.5, tau) / th1p0
    R_k = (+1j) * _theta_char_batch(ap, bp, tau) * _theta_char_batch(am, bm, tau) / th1p0
    return np.stack([R_1, R_i, R_j, R_k], axis=1)


def _F_kronecker_batch(u1: np.ndarray, u2: np.ndarray, tau: np.ndarray) -> np.ndarray:
    x = tau.real
    y = tau.imag
    a = np.mod(u1, 1.0)
    b = np.mod(u2, 1.0)
    a_zero = (a < 1e-12) | (a > 1.0 - 1e-12)
    a_safe = np.where(a_zero, 0.5, a)
    b_zero = (b < 1e-12) | (b > 1.0 - 1e-12)
    b_safe = np.where(b_zero, 0.5, b)

    first_nz = -math.pi * (2.0 * math.log(2.0) + np.log(y) + digamma(a_safe) + digamma(1.0 - a_safe))
    first_z = math.pi * (2.0 * EULER_GAMMA - 2.0 * math.log(2.0) - np.log(y))
    zero_row_z = np.where(b_zero, 0.0, y * (math.pi ** 2) / (np.sin(math.pi * b_safe) ** 2))
    base = np.where(a_zero, first_z + zero_row_z, first_nz)

    ks = np.arange(-12, 13, dtype=np.float64)[None, :]
    a_eff = np.where(a_zero, 0.0, a)[:, None]
    m = ks + a_eff
    m_nz = np.abs(m) > 1e-12
    m_safe = np.where(m_nz, m, 1.0)
    w = np.exp(-2.0 * math.pi * np.abs(m_safe) * y[:, None] + 2j * math.pi * (m_safe * x[:, None] + u2[:, None]))
    term = np.where(m_nz, (2.0 * math.pi / np.abs(m_safe)) * np.real(w / (1.0 - w)), 0.0)
    return base + np.sum(term, axis=1)


def _extract_12_from_yukawas(Y_up: np.ndarray, Y_down: np.ndarray, Y_lep: np.ndarray) -> np.ndarray:
    B = len(Y_up)
    out = np.empty((B, 12), dtype=np.float64)
    Uu_desc, sv_u, _ = np.linalg.svd(Y_up)
    Ud_desc, sv_d, _ = np.linalg.svd(Y_down)
    sv_l = np.linalg.svd(Y_lep, compute_uv=False)

    out[:, 0] = sv_u[:, 1] / sv_u[:, 0]
    out[:, 1] = sv_u[:, 2] / sv_u[:, 0]
    out[:, 2] = sv_u[:, 2] / sv_u[:, 1]

    out[:, 3] = sv_d[:, 1] / sv_d[:, 0]
    out[:, 4] = sv_d[:, 2] / sv_d[:, 0]
    out[:, 5] = sv_d[:, 2] / sv_d[:, 1]

    out[:, 6] = sv_l[:, 1] / sv_l[:, 0]
    out[:, 7] = sv_l[:, 2] / sv_l[:, 0]
    out[:, 8] = sv_l[:, 2] / sv_l[:, 1]

    Uu_asc = Uu_desc[:, :, ::-1]
    Ud_asc = Ud_desc[:, :, ::-1]
    V = np.einsum("aji,ajk->aik", np.conj(Uu_asc), Ud_asc)
    out[:, 9] = np.abs(V[:, 0, 1])
    out[:, 10] = np.abs(V[:, 1, 2])
    out[:, 11] = np.abs(V[:, 0, 2])
    return out


def evaluate_four_modes_f64_batch(
    tau_red: np.ndarray,
    a_arr: np.ndarray,
    b_arr: np.ndarray,
    tilde_L: np.ndarray,
) -> Dict[str, np.ndarray]:
    xq = np.exp(1j * math.pi * tau_red / 4.0)
    c3_S = (xq[:, None] ** SERRE_KS[None, :]) @ SERRE_MAT
    c3_St = np.conj(c3_S)
    yv = tau_red.imag
    exp_m2L2 = yv * np.exp(-2.0 * (tilde_L + NORM_CONST_SHIFT))

    u_t90_map: Dict[str, np.ndarray] = {}
    u_old_map: Dict[str, np.ndarray] = {}

    for sec, (qL, qR) in SIX_CHARGES.items():
        R_mat = _residues_closed_batch(tau_red, a_arr, b_arr, qL, qR)
        ap = (qL + qR) * a_arr
        bp = (qL + qR) * b_arr
        shifts_and_chars = [
            ((ap, bp), (ap + 0.5, bp + 0.5)),
            ((ap, bp - 0.5), (ap + 0.5, bp)),
            ((ap - 0.5, bp), (ap, bp + 0.5)),
            ((ap - 0.5, bp - 0.5), (ap, bp)),
        ]
        u_t90 = np.zeros_like(R_mat)
        u_old = np.zeros_like(R_mat)
        for s_idx, ((u1, u2), (al_c, be_c)) in enumerate(shifts_and_chars):
            R_col = R_mat[:, s_idx]
            active = np.abs(R_col) > 1e-14
            if np.any(active):
                Fu = _F_kronecker_batch(u1[active], u2[active], tau_red[active])
                a0_v = _a0_closed_batch(al_c[active], be_c[active], tau_red[active])
                n_old = 2.0 * math.pi * tilde_L[active] + Fu
                corr = math.pi * (np.abs(a0_v) ** 2) * exp_m2L2[active]
                n_t90 = n_old - corr
                u_old[active, s_idx] = np.sqrt(np.maximum(0.0, n_old)) * R_col[active]
                u_t90[active, s_idx] = np.sqrt(np.maximum(0.0, n_t90)) * R_col[active]
        u_t90_map[sec] = u_t90
        u_old_map[sec] = u_old

    def build_world_out(u_map: Dict[str, np.ndarray], is_w_plus: bool) -> np.ndarray:
        c_up = c3_S if is_w_plus else c3_St
        c_dn = c3_St if is_w_plus else c3_S
        Yu = np.einsum("ba,bs,asrc->brc", c_up, u_map["up"], T_COUP)
        Yd = np.einsum("ba,bs,asrc->brc", c_dn, u_map["down"], T_COUP)
        Yl = np.einsum("ba,bs,asrc->brc", c_dn, u_map["lepton"], T_COUP)
        return _extract_12_from_yukawas(Yu, Yd, Yl)

    return {
        "W_minus_T90": build_world_out(u_t90_map, False),
        "W_minus_old": build_world_out(u_old_map, False),
        "W_plus_T90": build_world_out(u_t90_map, True),
        "W_plus_old": build_world_out(u_old_map, True),
    }


def eval_p5_avg_four_modes_mp(x_val: float, y_val: float, L2_raw_val: float, dps: int = 150) -> Dict[str, np.ndarray]:
    """
    Arbitrary-precision mpmath evaluation of the P_5-averaged 12 outputs across all 4 modes
    at tau = x_val + i * y_val with canonical raw end L_2(tau) = L2_raw_val.
    Eliminates IEEE float64 SVD singular-subspace underflow in the cusp y > 5.
    """
    with mp.workdps(dps):
        tau = mp.mpc(mp.mpf(repr(x_val)), mp.mpf(repr(y_val)))
        yv = mp.im(tau)
        L2 = mp.mpf(repr(L2_raw_val))
        tl2 = L2 + mp.mpf("0.5") * mp.log(yv) - (mp.euler + mp.log(mp.pi))
        exp_m2L2 = mp.exp(-2 * L2)

        xq = mp.exp(mp.j * mp.pi * tau / 4)
        c3_S = [mp.mpc(0), mp.mpc(0), mp.mpc(0)]
        cutoff_serre = mp.mpf(10) ** (-(dps + 10))
        for k_int, cols_frac in SERRE_EXACT_ROWS:
            pw = xq ** k_int
            if abs(pw) < cutoff_serre and k_int > 8:
                break
            for col_j in range(3):
                fr, fi = cols_frac[col_j]
                if fr or fi:
                    c_mp = mp.mpc(mp.mpf(fr.numerator) / fr.denominator, mp.mpf(fi.numerator) / fi.denominator)
                    c3_S[col_j] += pw * c_mp
        c3_St = [mp.conj(z) for z in c3_S]

        def th_char(al: mp.mpf, be: mp.mpf) -> mp.mpc:
            at = al - mp.nint(al)
            s = mp.mpc(0)
            for k in range(-9, 10):
                m = mp.mpf(k) + at
                s += mp.exp(mp.j * mp.pi * tau * m * m + 2 * mp.j * mp.pi * m * be)
            return s

        def a0_char(al: mp.mpf, be: mp.mpf) -> mp.mpc:
            at = al - mp.nint(al)
            num = mp.mpc(0)
            den = mp.mpc(0)
            for k in range(-9, 10):
                m = mp.mpf(k) + at
                t = mp.exp(mp.j * mp.pi * tau * m * m + 2 * mp.j * mp.pi * m * be)
                den += t
                num += 2 * mp.j * mp.pi * m * t
            return num / den

        th1p0 = mp.mpc(0)
        for k in range(10):
            h = mp.mpf(k) + mp.mpf("0.5")
            th1p0 += ((-1) ** k) * (2 * k + 1) * mp.exp(mp.j * mp.pi * tau * h * h)
        th1p0 *= 2 * mp.pi

        def F_kron(u1: mp.mpf, u2: mp.mpf) -> mp.mpf:
            a = u1 - mp.floor(u1)
            b = u2 - mp.floor(u2)
            az = (abs(a) < mp.mpf("1e-35")) or (abs(a - 1) < mp.mpf("1e-35"))
            bz = (abs(b) < mp.mpf("1e-35")) or (abs(b - 1) < mp.mpf("1e-35"))
            if az:
                base = mp.pi * (2 * mp.euler - 2 * mp.log(2) - mp.log(yv))
                if not bz:
                    base += yv * (mp.pi ** 2) / (mp.sin(mp.pi * b) ** 2)
                a_eff = mp.mpf(0)
            else:
                base = -mp.pi * (2 * mp.log(2) + mp.log(yv) + mp.digamma(a) + mp.digamma(1 - a))
                a_eff = a
            tot = base
            for k in range(-14, 15):
                m = mp.mpf(k) + a_eff
                if abs(m) > mp.mpf("1e-35"):
                    w = mp.exp(-2 * mp.pi * abs(m) * yv + 2 * mp.j * mp.pi * (m * mp.re(tau) + u2))
                    if abs(w) > cutoff_serre:
                        tot += (2 * mp.pi / abs(m)) * mp.re(w / (1 - w))
            return tot

        accs = {
            "W_minus_T90": np.zeros(12, dtype=np.float64),
            "W_minus_old": np.zeros(12, dtype=np.float64),
            "W_plus_T90": np.zeros(12, dtype=np.float64),
            "W_plus_old": np.zeros(12, dtype=np.float64),
        }
        half = mp.mpf("0.5")
        zero_thr = mp.mpf(10) ** (-dps + 20)

        for ja, jb in P5_HALF_12_INT:
            a_p = mp.mpf(ja) / 5
            b_p = mp.mpf(jb) / 5
            u_t90_sec: Dict[str, List[mp.mpc]] = {}
            u_old_sec: Dict[str, List[mp.mpc]] = {}
            # Notice lepton mod 5 has exact transposed spectrum of down; compute up, down, lepton explicitly!
            for sec, (qL, qR) in SIX_CHARGES.items():
                ap = (qL + qR) * a_p
                bp = (qL + qR) * b_p
                am = (qL - qR) * a_p
                bm = (qL - qR) * b_p
                ph1 = mp.exp(-mp.j * mp.pi * (ap + am))
                R_1 = (-mp.j) * ph1 * th_char(ap + half, bp + half) * th_char(am + half, bm + half) / th1p0
                R_i = (-1) * th_char(ap + half, bp) * th_char(am + half, bm) / th1p0
                R_j = (-1) * ph1 * th_char(ap, bp + half) * th_char(am, bm + half) / th1p0
                R_k = (+mp.j) * th_char(ap, bp) * th_char(am, bm) / th1p0
                Rs = [R_1, R_i, R_j, R_k]
                sh = [
                    ((ap, bp), (ap + half, bp + half)),
                    ((ap, bp - half), (ap + half, bp)),
                    ((ap - half, bp), (ap, bp + half)),
                    ((ap - half, bp - half), (ap, bp)),
                ]
                vt90 = [mp.mpc(0)] * 4
                vold = [mp.mpc(0)] * 4
                for s_i in range(4):
                    if abs(Rs[s_i]) > zero_thr:
                        Fu = F_kron(sh[s_i][0][0], sh[s_i][0][1])
                        a0v = a0_char(sh[s_i][1][0], sh[s_i][1][1])
                        n_old = 2 * mp.pi * tl2 + Fu
                        corr = mp.pi * (abs(a0v) ** 2) * exp_m2L2
                        vold[s_i] = mp.sqrt(n_old) * Rs[s_i]
                        vt90[s_i] = mp.sqrt(n_old - corr) * Rs[s_i]
                u_t90_sec[sec] = vt90
                u_old_sec[sec] = vold

            def make_Y(c_vec: List[mp.mpc], u_v: List[mp.mpc]) -> mp.matrix:
                Y = mp.zeros(3, 3)
                for al_i, s_i, ra, cb, tr2, ti2 in T_COUP_NZ:
                    Y[ra, cb] += c_vec[al_i] * u_v[s_i] * mp.mpc(tr2, ti2) * half
                return Y

            def extract_12_mp(u_map: Dict[str, List[mp.mpc]], is_w_plus: bool) -> np.ndarray:
                c_up = c3_S if is_w_plus else c3_St
                c_dn = c3_St if is_w_plus else c3_S
                Yu = make_Y(c_up, u_map["up"])
                Yd = make_Y(c_dn, u_map["down"])
                Yl = make_Y(c_dn, u_map["lepton"])
                Uu, sv_u, _ = mp.svd_c(Yu)
                Ud, sv_d, _ = mp.svd_c(Yd)
                _, sv_l, _ = mp.svd_c(Yl)
                v_arr = np.empty(12, dtype=np.float64)
                v_arr[0] = float(sv_u[1] / sv_u[0])
                v_arr[1] = float(sv_u[2] / sv_u[0])
                v_arr[2] = float(sv_u[2] / sv_u[1])
                v_arr[3] = float(sv_d[1] / sv_d[0])
                v_arr[4] = float(sv_d[2] / sv_d[0])
                v_arr[5] = float(sv_d[2] / sv_d[1])
                v_arr[6] = float(sv_l[1] / sv_l[0])
                v_arr[7] = float(sv_l[2] / sv_l[0])
                v_arr[8] = float(sv_l[2] / sv_l[1])
                for out_idx, (i_asc, j_asc) in ((9, (0, 1)), (10, (1, 2)), (11, (0, 2))):
                    ii = 2 - i_asc
                    jj = 2 - j_asc
                    s_ov = mp.mpc(0)
                    for k_r in range(3):
                        s_ov += mp.conj(Uu[k_r, ii]) * Ud[k_r, jj]
                    v_arr[out_idx] = float(abs(s_ov))
                return v_arr

            accs["W_minus_T90"] += extract_12_mp(u_t90_sec, False) / 12.0
            accs["W_minus_old"] += extract_12_mp(u_old_sec, False) / 12.0
            accs["W_plus_T90"] += extract_12_mp(u_t90_sec, True) / 12.0
            accs["W_plus_old"] += extract_12_mp(u_old_sec, True) / 12.0

        return accs


def _mp_cusp_worker(args: Tuple[float, float, float, int]) -> Dict[str, np.ndarray]:
    xv, yv, l2_raw, dps = args
    return eval_p5_avg_four_modes_mp(xv, yv, l2_raw, dps=dps)


# ============================================================================
# SECTION 3: HYPERBOLIC POINCARE AREA MEASURE & CUSP TREATMENT
# ============================================================================

def _dict_12(arr: np.ndarray) -> Dict[str, float]:
    return {OUTPUT_KEYS_12[i]: float(arr[i]) for i in range(12)}


def _dict_7_fc(arr: np.ndarray) -> Dict[str, float]:
    return {k: float(arr[OUTPUT_KEYS_12.index(k)]) for k in CLAIMED_7_FRAME_CODE}


def _dict_7_adj(arr: np.ndarray) -> Dict[str, float]:
    return {k: float(arr[OUTPUT_KEYS_12.index(k)]) for k in CLAIMED_7_ADJACENT}


def _eval_f64_p5_avg_grid(taus: np.ndarray, end_eval: CanonicalL2Evaluator) -> Dict[str, np.ndarray]:
    n_pts = len(taus)
    tl2 = end_eval.eval_tilde_L2_batch(taus)
    a12 = np.array([p[0] for p in P5_HALF_12], dtype=np.float64)
    b12 = np.array([p[1] for p in P5_HALF_12], dtype=np.float64)
    out = {
        "W_minus_T90": np.empty((n_pts, 12), dtype=np.float64),
        "W_minus_old": np.empty((n_pts, 12), dtype=np.float64),
        "W_plus_T90": np.empty((n_pts, 12), dtype=np.float64),
        "W_plus_old": np.empty((n_pts, 12), dtype=np.float64),
    }
    chunk = 256
    for i0 in range(0, n_pts, chunk):
        i1 = min(n_pts, i0 + chunk)
        cl = i1 - i0
        t_rep = np.repeat(taus[i0:i1], 12)
        a_rep = np.tile(a12, cl)
        b_rep = np.tile(b12, cl)
        tl_rep = np.repeat(tl2[i0:i1], 12)
        ev = evaluate_four_modes_f64_batch(t_rep, a_rep, b_rep, tl_rep)
        for k in out:
            out[k][i0:i1] = np.mean(ev[k].reshape(cl, 12, 12), axis=1)
    return out


def compute_area_measure_with_cusp(end_eval: CanonicalL2Evaluator, n_workers: int = 10) -> Dict[str, Any]:
    """
    Integrates (3 / pi) * dx * du over x in [-1/2, 1/2], u = 1/y in (0, 1/sqrt(1 - x^2)]:
      - Bulk u in [1/5, 1/sqrt(1 - x^2)] (y <= 5): float64 Gauss-Legendre (16x20 vs 24x32).
      - Mid-cusp u in [1/55, 1/5] (5 <= y <= 55): mpmath dps=150 Gauss-Legendre (8x10 vs 12x16).
      - Deep-cusp u in (0, 1/55] (y >= 55): mpmath dps=300 Gauss-Legendre (6x6).
    Also evaluates:
      - PC_MEAS_1: naive float64 SVD vs mpmath SVD in the cusp (y = 22, 28, 35) + naive float64 full integral.
      - PC_MEAS_2: renormalized hard cusp-cutoff integrals at Y_cut in {3, 5, 10, 20}.
    """
    t0 = time.time()
    norm_prefac = 3.0 / math.pi

    def integrate_bulk_f64(nx: int, nu: int, u_low: float) -> Tuple[Dict[str, np.ndarray], float]:
        gx, wx = roots_legendre(nx)
        gu, wu = roots_legendre(nu)
        xs = 0.5 * gx  # [-1/2, 1/2], jacobian 0.5
        wx_s = 0.5 * wx
        taus_list = []
        weights_list = []
        for ix, xv in enumerate(xs):
            u_top = 1.0 / math.sqrt(1.0 - xv * xv)
            if u_top <= u_low:
                continue
            half_du = 0.5 * (u_top - u_low)
            mid_u = 0.5 * (u_top + u_low)
            for iu, uv_ref in enumerate(gu):
                u_val = mid_u + half_du * uv_ref
                y_val = 1.0 / u_val
                taus_list.append(complex(xv, y_val))
                weights_list.append(norm_prefac * wx_s[ix] * half_du * wu[iu])
        taus_arr = np.array(taus_list, dtype=np.complex128)
        w_arr = np.array(weights_list, dtype=np.float64)
        vals = _eval_f64_p5_avg_grid(taus_arr, end_eval)
        res = {k: np.sum(w_arr[:, None] * vals[k], axis=0) for k in vals}
        return res, float(np.sum(w_arr))

    bulk_coarse, mass_bulk_c = integrate_bulk_f64(16, 20, 0.2)
    bulk_fine, mass_bulk_f = integrate_bulk_f64(24, 32, 0.2)

    def integrate_strip_mp(nx: int, nu: int, u_a: float, u_b: float, dps: int, pool: Pool) -> Tuple[Dict[str, np.ndarray], float]:
        gx, wx = roots_legendre(nx)
        gu, wu = roots_legendre(nu)
        xs = 0.5 * gx
        wx_s = 0.5 * wx
        half_du = 0.5 * (u_b - u_a)
        mid_u = 0.5 * (u_b + u_a)
        us = mid_u + half_du * gu
        wu_s = half_du * wu

        pts_tau = []
        pts_xy = []
        w_list = []
        for ix, xv in enumerate(xs):
            for iu, uv in enumerate(us):
                yv = 1.0 / float(uv)
                pts_tau.append(complex(float(xv), yv))
                pts_xy.append((float(xv), yv))
                w_list.append(norm_prefac * float(wx_s[ix]) * float(wu_s[iu]))
        l2_raw = end_eval.eval_L2_raw_batch(np.array(pts_tau, dtype=np.complex128))
        tasks = [(pts_xy[i][0], pts_xy[i][1], float(l2_raw[i]), dps) for i in range(len(pts_xy))]
        evals = pool.map(_mp_cusp_worker, tasks)
        w_arr = np.array(w_list, dtype=np.float64)
        res = {}
        for mode_k in ("W_minus_T90", "W_minus_old", "W_plus_T90", "W_plus_old"):
            mat = np.array([e[mode_k] for e in evals], dtype=np.float64)
            res[mode_k] = np.sum(w_arr[:, None] * mat, axis=0)
        return res, float(np.sum(w_arr)), pts_xy, evals, w_arr

    with Pool(n_workers) as pool:
        mid_coarse, _, _, _, _ = integrate_strip_mp(8, 10, 1.0 / 55.0, 0.2, 150, pool)
        mid_fine, mass_mid_f, mid_pts_xy, mid_evals, mid_w = integrate_strip_mp(12, 16, 1.0 / 55.0, 0.2, 150, pool)
        deep_fine, mass_deep_f, _, _, _ = integrate_strip_mp(6, 6, 0.0, 1.0 / 55.0, 300, pool)

        # Verify exact rational cusp limit (0, 0, 0, 0, 0, 0, 0, 0, 0, 5/12, 5/12, 7/12) at y = 80
        cusp_y80 = pool.map(_mp_cusp_worker, [(-0.23, 80.0, end_eval.L2_cusp_inf, 260), (0.31, 80.0, end_eval.L2_cusp_inf, 260)])

        # Planted Control PC_MEAS_1: compare float64 SVD vs mpmath SVD at y = 22, 28, 35
        pc1_ys = [22.0, 28.0, 35.0]
        pc1_taus = np.array([complex(0.17, yv) for yv in pc1_ys], dtype=np.complex128)
        pc1_l2 = end_eval.eval_L2_raw_batch(pc1_taus)
        pc1_mp = pool.map(_mp_cusp_worker, [(0.17, pc1_ys[i], float(pc1_l2[i]), 160) for i in range(3)])
        pc1_f64 = _eval_f64_p5_avg_grid(pc1_taus, end_eval)

    total_mass = mass_bulk_f + mass_mid_f + mass_deep_f
    assert abs(total_mass - 1.0) < 1e-12, f"Poincare area normalization error: {total_mass}"

    exact_area: Dict[str, np.ndarray] = {}
    coarse_area: Dict[str, np.ndarray] = {}
    quad_err: Dict[str, np.ndarray] = {}
    for k in ("W_minus_T90", "W_minus_old", "W_plus_T90", "W_plus_old"):
        exact_area[k] = bulk_fine[k] + mid_fine[k] + deep_fine[k]
        coarse_area[k] = bulk_coarse[k] + mid_coarse[k] + deep_fine[k]
        quad_err[k] = np.abs(exact_area[k] - coarse_area[k])

    # Naive float64 integral over the entire u in (0, 1/sqrt(1-x^2)] (showing float64 SVD cusp corruption)
    naive_f64_full, _ = integrate_bulk_f64(24, 48, 0.0)
    pc1_pointwise_max_err = max(
        float(np.max(np.abs(pc1_f64["W_minus_T90"][i] - pc1_mp[i]["W_minus_T90"])))
        for i in range(3)
    )
    pc1_integral_bias_mixing = float(np.max(np.abs(naive_f64_full["W_minus_T90"][9:12] - exact_area["W_minus_T90"][9:12])))
    pc1_fired = bool(pc1_pointwise_max_err > 0.20 and pc1_integral_bias_mixing > 1e-3)

    # Cusp cutoff study PC_MEAS_2: renormalized integrals on y <= Y_cut for Y_cut in {3, 5, 10, 20}
    idx_fc7 = [OUTPUT_KEYS_12.index(k) for k in CLAIMED_7_FRAME_CODE]
    exact_fc7 = exact_area["W_minus_T90"][idx_fc7]
    cutoff_table: Dict[str, Any] = {}
    for y_cut in (3.0, 5.0):
        sub_int, sub_mass = integrate_bulk_f64(24, 28, 1.0 / y_cut)
        renorm = sub_int["W_minus_T90"] / sub_mass
        diff_fc7 = np.abs(renorm[idx_fc7] - exact_fc7)
        cutoff_table[str(int(y_cut))] = {
            "Y_cut": int(y_cut),
            "retained_area_fraction": sub_mass,
            "W_minus_T90_renormalized_claimed_7": _dict_7_fc(renorm),
            "max_abs_bias_vs_full_claimed_7": float(np.max(diff_fc7)),
            "max_rel_bias_vs_full_claimed_7": float(np.max(diff_fc7 / exact_fc7)),
        }

    # For Y_cut = 10 and 20, combine bulk_fine (y <= 5) with mpmath strip [1/Y_cut, 1/5]
    with Pool(n_workers) as pool:
        for y_cut in (10, 20):
            st_int, st_mass, _, _, _ = integrate_strip_mp(10, 12, 1.0 / float(y_cut), 0.2, 150, pool)
            tot_m = mass_bulk_f + st_mass
            renorm = (bulk_fine["W_minus_T90"] + st_int["W_minus_T90"]) / tot_m
            diff_fc7 = np.abs(renorm[idx_fc7] - exact_fc7)
            cutoff_table[str(y_cut)] = {
                "Y_cut": y_cut,
                "retained_area_fraction": tot_m,
                "W_minus_T90_renormalized_claimed_7": _dict_7_fc(renorm),
                "max_abs_bias_vs_full_claimed_7": float(np.max(diff_fc7)),
                "max_rel_bias_vs_full_claimed_7": float(np.max(diff_fc7 / exact_fc7)),
            }

    r3 = cutoff_table["3"]["max_rel_bias_vs_full_claimed_7"]
    r5 = cutoff_table["5"]["max_rel_bias_vs_full_claimed_7"]
    r10 = cutoff_table["10"]["max_rel_bias_vs_full_claimed_7"]
    r20 = cutoff_table["20"]["max_rel_bias_vs_full_claimed_7"]
    pc2_fired = bool(r5 > 0.10 and (r3 > r5 > r10 > r20 > 0.0))

    target_cusp_limit = np.array([0.0] * 9 + [5.0 / 12.0, 5.0 / 12.0, 7.0 / 12.0], dtype=np.float64)
    y80_err_vs_rational = max(
        float(np.max(np.abs(cusp_y80[0]["W_minus_T90"] - target_cusp_limit))),
        float(np.max(np.abs(cusp_y80[1]["W_minus_T90"] - target_cusp_limit))),
    )
    assert y80_err_vs_rational < 1e-9, f"Cusp y=80 limit mismatch: {y80_err_vs_rational}"

    four_combos_out = {}
    for k_json, k_int in (
        ("W_minus__exact_T90", "W_minus_T90"),
        ("W_minus__old_small_cut", "W_minus_old"),
        ("W_plus__exact_T90", "W_plus_T90"),
        ("W_plus__old_small_cut", "W_plus_old"),
    ):
        four_combos_out[k_json] = {
            "all_12_outputs": _dict_12(exact_area[k_int]),
            "all_12_quadrature_err": _dict_12(quad_err[k_int]),
            "claimed_7_frame_code": _dict_7_fc(exact_area[k_int]),
            "claimed_7_frame_code_quad_err": _dict_7_fc(quad_err[k_int]),
            "claimed_7_adjacent": _dict_7_adj(exact_area[k_int]),
            "claimed_7_adjacent_quad_err": _dict_7_adj(quad_err[k_int]),
        }

    print(f"[X-MEASURE Area] Completed hybrid Poincare area integral ({int(round(time.time() - t0))}s)", flush=True)
    return {
        "cusp_treatment": {
            "compactification": "u = 1/y on (0, 1/sqrt(1 - x^2)] with constant Jacobian (3/pi) dx du",
            "bulk_region": "y <= 5 (float64 24x32 Gauss-Legendre, area fraction ~ 81%)",
            "mid_cusp_region": "5 < y <= 55 (mpmath dps=150 12x16 Gauss-Legendre, area fraction ~ 17%)",
            "deep_cusp_region": "y > 55 (mpmath dps=300 6x6 Gauss-Legendre, area fraction ~ 2%)",
            "L2_cusp_limit_inf": end_eval.L2_cusp_inf,
            "total_normalized_area_check": total_mass,
            "exact_cusp_rational_limit_12": _dict_12(target_cusp_limit),
            "y80_max_err_vs_exact_rational_cusp_limit": y80_err_vs_rational,
            "max_quadrature_refinement_err_W_minus_T90": float(np.max(quad_err["W_minus_T90"])),
        },
        "PC_MEAS_1_float64_cusp_svd_underflow": {
            "pointwise_max_err_y22_28_35": pc1_pointwise_max_err,
            "naive_float64_full_area_mixing_bias": pc1_integral_bias_mixing,
            "naive_float64_full_area_W_minus_T90_claimed_7": _dict_7_fc(naive_f64_full["W_minus_T90"]),
            "fired": pc1_fired,
        },
        "PC_MEAS_2_hard_cusp_cutoff_bias": {
            "cutoffs": cutoff_table,
            "fired": pc2_fired,
        },
        "four_primary_combinations": four_combos_out,
        "_raw_arrays": exact_area,
    }


# ============================================================================
# SECTION 4: GENERAL HYPERBOLIC GEODESIC EVALUATOR (60-DIGIT MPMATH REDUCTION + HYBRID SVD)
# ============================================================================

_GLOBAL_END: Optional[CanonicalL2Evaluator] = None


def _init_pool_end(ev: CanonicalL2Evaluator) -> None:
    global _GLOBAL_END
    _GLOBAL_END = ev


def reduce_tau_only_f64(t: complex) -> complex:
    for _ in range(250):
        m = round(t.real)
        if m:
            t = t - m
        if abs(t) < 1.0 - 1e-12:
            t = -1.0 / t
        else:
            return t
    raise RuntimeError("SL(2,Z) reduction exceeded 250 steps")


def local_semicircle_charts(w: str) -> Tuple[List[str], List[float], List[float], List[float], float]:
    n = len(w)
    gs = [("R" if w[n - 1 - k] == "L" else "L") for k in range(n)]
    n_warm = max(2, int(math.ceil(160.0 / n)))
    x = 1.0
    for _ in range(n_warm):
        for k in range(n - 1, -1, -1):
            x = (x + 1.0) if gs[k] == "L" else (x / (x + 1.0))
    betas = [0.0] * n
    betas[0] = x
    for k in range(n - 1, 0, -1):
        x = (x + 1.0) if gs[k] == "L" else (x / (x + 1.0))
        betas[k] = x
    y = -1.0
    for _ in range(n_warm):
        for k in range(n):
            y = (y - 1.0) if gs[k] == "L" else (y / (1.0 - y))
    betaps = [0.0] * n
    betaps[0] = y
    for k in range(n - 1):
        y = (y - 1.0) if gs[k] == "L" else (y / (1.0 - y))
        betaps[k + 1] = y
    ds_list: List[float] = []
    for k in range(n):
        kp = (k + 1) % n
        zk1 = 0.5 * (betas[kp] + betaps[kp]) + 0.5j * (betas[kp] - betaps[kp])
        gk_zk1 = (zk1 + 1.0) if gs[k] == "L" else (zk1 / (zk1 + 1.0))
        ratio = (gk_zk1 - betaps[k]) / (betas[k] - gk_zk1)
        ds_list.append(math.log(ratio.imag))
    return gs, betas, betaps, ds_list, sum(ds_list)


def _eval_reduced_taus_hybrid(taus_red: np.ndarray, end_eval: CanonicalL2Evaluator) -> Dict[str, np.ndarray]:
    """Evaluates P_5-averaged 4 modes along reduced taus, routing y > 5.5 through mpmath SVD."""
    low_mask = taus_red.imag <= 5.5
    n_tot = len(taus_red)
    res = {k: np.empty((n_tot, 12), dtype=np.float64) for k in ("W_minus_T90", "W_minus_old", "W_plus_T90", "W_plus_old")}
    if np.any(low_mask):
        sub = _eval_f64_p5_avg_grid(taus_red[low_mask], end_eval)
        for k in res:
            res[k][low_mask] = sub[k]
    if np.any(~low_mask):
        hi_idxs = np.where(~low_mask)[0]
        l2_hi = end_eval.eval_L2_raw_batch(taus_red[hi_idxs])
        for loc_i, idx in enumerate(hi_idxs):
            yv = float(taus_red[idx].imag)
            dps = 150 if yv <= 55.0 else 280
            ev_mp = eval_p5_avg_four_modes_mp(float(taus_red[idx].real), yv, float(l2_hi[loc_i]), dps=dps)
            for k in res:
                res[k][idx] = ev_mp[k]
    return {k: np.mean(res[k], axis=0) for k in res}


def _geodesic_taus_from_matrix_mp(M: Tuple[int, int, int, int], m_nodes: int = 96) -> Tuple[np.ndarray, float]:
    """
    Given hyperbolic M = (a, b, c, d) in SL(2, Z) with |a + d| > 2, computes its closed geodesic
    on PSL(2, Z) \\ H in 70-digit mpmath and returns (taus_red_in_F, ell).
    """
    a, b, c, d = M
    if a + d < 0:
        a, b, c, d = -a, -b, -c, -d
    assert a * d - b * c == 1 and a + d > 2
    # If c == 0, conjugate into c != 0 via S (none of our hyperbolic axes is infinity, since tr > 2 => a != 1)
    if c == 0:
        # M = [[a, b], [0, d]] with a*d=1, a>0 => a=d=1 (parabolic), excluded by a+d > 2!
        raise ValueError("Parabolic matrix passed to hyperbolic geodesic solver")
    with mp.workdps(70):
        tr = mp.mpf(a + d)
        disc = mp.sqrt(tr * tr - 4)
        lam_plus = (tr + disc) / 2
        ell_mp = 2 * mp.log(lam_plus)
        # Fixed points of (a z + b) / (c z + d) = z => c z^2 + (d - a) z - b = 0
        beta_plus = (mp.mpf(a - d) + disc) / (2 * mp.mpf(c))
        beta_minus = (mp.mpf(a - d) - disc) / (2 * mp.mpf(c))
        b_hi = max(beta_plus, beta_minus)
        b_lo = min(beta_plus, beta_minus)

        taus_red = np.empty(m_nodes, dtype=np.complex128)
        for j in range(m_nodes):
            s_val = (mp.mpf(j) + mp.mpf("0.5")) * (ell_mp / m_nodes)
            ies = mp.j * mp.exp(s_val)
            zt = (b_hi * ies + b_lo) / (ies + 1)
            # SL(2, Z) reduction in 70-digit mpmath
            for _ in range(400):
                m_sh = mp.nint(mp.re(zt))
                if m_sh != 0:
                    zt = zt - m_sh
                if abs(zt) < mp.mpf("1") - mp.mpf("1e-30"):
                    zt = -1 / zt
                else:
                    break
            taus_red[j] = complex(float(mp.re(zt)), float(mp.im(zt)))
        return taus_red, float(ell_mp)


def _eval_matrix_geodesic_worker(args: Tuple[Tuple[int, int, int, int], int]) -> Tuple[float, Dict[str, np.ndarray]]:
    assert _GLOBAL_END is not None
    M, m_nodes = args
    taus_red, ell = _geodesic_taus_from_matrix_mp(M, m_nodes=m_nodes)
    means = _eval_reduced_taus_hybrid(taus_red, _GLOBAL_END)
    return ell, means


def _eval_lr_ergodic_worker(args: Tuple[str, int]) -> Dict[str, Any]:
    assert _GLOBAL_END is not None
    w, nodes_per_move = args
    _, betas, betaps, ds_list, ell = local_semicircle_charts(w)
    n_moves = len(w)
    m_nodes = max(256, n_moves * nodes_per_move)
    cum = np.empty(n_moves + 1, dtype=np.float64)
    cum[0] = 0.0
    cum[1:] = np.cumsum(ds_list)
    s_grid = (np.arange(m_nodes, dtype=np.float64) + 0.5) * (ell / m_nodes)
    k_idxs = np.clip(np.searchsorted(cum, s_grid, side="right") - 1, 0, n_moves - 1)
    s_locs = s_grid - cum[k_idxs]
    betas_arr = np.asarray(betas, dtype=np.float64)[k_idxs]
    betaps_arr = np.asarray(betaps, dtype=np.float64)[k_idxs]
    ies = 1j * np.exp(s_locs)
    zt_arr = (betas_arr * ies + betaps_arr) / (ies + 1.0)
    tau_red = np.array([reduce_tau_only_f64(complex(z)) for z in zt_arr], dtype=np.complex128)
    means = _eval_reduced_taus_hybrid(tau_red, _GLOBAL_END)
    return {"ell": ell, "means": means}


def _jackknife_weighted(lengths: np.ndarray, mat: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    tot_w = float(np.sum(lengths))
    w_sum = np.sum(lengths[:, None] * mat, axis=0)
    est = w_sum / tot_w
    m = len(lengths)
    jk = (w_sum[None, :] - lengths[:, None] * mat) / (tot_w - lengths[:, None])
    se = np.sqrt((m - 1.0) * np.mean((jk - est[None, :]) ** 2, axis=0))
    return est, se


# ============================================================================
# SECTION 5: M25 CANDIDATES 1, 2, 3 AND M24 COLD-READ ALGEBRAIC VERIFICATION
# ============================================================================

def _mat_mul_mod(A: Tuple[int, int, int, int], B: Tuple[int, int, int, int], mod: int) -> Tuple[int, int, int, int]:
    return (
        (A[0] * B[0] + A[1] * B[2]) % mod,
        (A[0] * B[1] + A[1] * B[3]) % mod,
        (A[2] * B[0] + A[3] * B[2]) % mod,
        (A[2] * B[1] + A[3] * B[3]) % mod,
    )


def _mat_mul_int(A: Tuple[int, int, int, int], B: Tuple[int, int, int, int]) -> Tuple[int, int, int, int]:
    return (
        A[0] * B[0] + A[1] * B[2],
        A[0] * B[1] + A[1] * B[3],
        A[2] * B[0] + A[3] * B[2],
        A[2] * B[1] + A[3] * B[3],
    )


def _is_allowed_at_level(M: Tuple[int, int, int, int], level: int) -> bool:
    det_m_i = (M[0] - 1) * (M[3] - 1) - M[1] * M[2]
    return math.gcd(det_m_i % level, level) == 1


def _sl2_markov_gap(level: int) -> Tuple[int, float]:
    L_m = (1, 1, 0, 1)
    R_m = (1, 0, 1, 1)
    elems = []
    idx_map = {}
    for a in range(level):
        for b in range(level):
            for c in range(level):
                for d in range(level):
                    if (a * d - b * c) % level == 1:
                        g = (a, b, c, d)
                        idx_map[g] = len(elems)
                        elems.append(g)
    n = len(elems)
    rows_sp = []
    cols_sp = []
    vals_sp = []
    for i, g in enumerate(elems):
        rows_sp.append(i); cols_sp.append(idx_map[_mat_mul_mod(g, L_m, level)]); vals_sp.append(0.5)
        rows_sp.append(i); cols_sp.append(idx_map[_mat_mul_mod(g, R_m, level)]); vals_sp.append(0.5)
    P_sp = csr_matrix((vals_sp, (rows_sp, cols_sp)), shape=(n, n))
    evals_sp = sparse_eigs(P_sp, k=6, which="LM", return_eigenvectors=False)
    mags = np.sort(np.abs(evals_sp))[::-1]
    return n, float(1.0 - mags[1])


def _sample_closed_lr_trajectory(rng: random.Random, target_len: int, level: int) -> str:
    L_m = (1, 1, 0, 1)
    R_m = (1, 0, 1, 1)
    n_pre = target_len - 10
    while True:
        pre_chars = [rng.choice("LR") for _ in range(n_pre)]
        if "L" not in pre_chars or "R" not in pre_chars:
            continue
        cur = (1, 0, 0, 1)
        for ch in pre_chars:
            cur = _mat_mul_mod(cur, L_m if ch == "L" else R_m, level)
        # Find random 10-letter suffix making total product allowed mod level
        cands = list(range(1024))
        rng.shuffle(cands)
        for bits in cands[:128]:
            suf = "".join("L" if ((bits >> k) & 1) else "R" for k in range(9, -1, -1))
            tot = cur
            for ch in suf:
                tot = _mat_mul_mod(tot, L_m if ch == "L" else R_m, level)
            if _is_allowed_at_level(tot, level):
                return "".join(pre_chars) + suf


def _is_lyndon_word(w: str) -> bool:
    n = len(w)
    for k in range(1, n):
        if w[k:] + w[:k] <= w:
            return False
    return True


def enumerate_lr_lyndon_by_trace_bound(t_max: int, level: int = 5) -> List[Tuple[str, Tuple[int, int, int, int]]]:
    """
    Exhaustively enumerates ALL primitive closed geodesics (Lyndon words W in {L, R}^+)
    satisfying tr(W) <= t_max and level-5 admissibility det(W - I) = 2 - tr(W) != 0 mod 5,
    exploiting strict trace monotonicity and Lyndon prefix pruning (every prefix of a Lyndon
    word is a prefix of a Lyndon word, so w[0] == 'L' and no prefix can exceed lexicographically).
    """
    L_i = (1, 1, 0, 1)
    R_i = (1, 0, 1, 1)
    results: List[Tuple[str, Tuple[int, int, int, int]]] = []
    # Every Lyndon word containing both L and R starts with 'L'!
    stack: List[Tuple[str, Tuple[int, int, int, int], bool]] = [("L", L_i, False)]
    while stack:
        w, M, hR = stack.pop()
        if hR:
            tr = M[0] + M[3]
            if tr > 2 and _is_allowed_at_level(M, level) and _is_lyndon_word(w):
                results.append((w, M))
        for ch, G, nhR in (("L", L_i, hR), ("R", R_i, True)):
            Mn = _mat_mul_int(M, G)
            trn = Mn[0] + Mn[3]
            if trn <= t_max:
                if not nhR and Mn[1] > t_max - 2:
                    continue
                stack.append((w + ch, Mn, nhR))
    return results


def audit_b1936_algebra() -> Dict[str, Any]:
    Y6_weyl = {"ten_1": 1, "ten_2": -4, "fivebar_1": 2, "fivebar_2": -3, "ten_3": 6}
    sectors = {"up": ("ten_1", "ten_2"), "down": ("ten_1", "fivebar_1"), "lepton": ("fivebar_2", "ten_3")}
    dirac_frame_c = {"up": (1, 4), "down": (1, -2), "lepton": (-3, -6)}

    multiplier_scan = {}
    single_parity_multipliers = []
    for m in (1, 2, 3, 4):
        degs = {f: (m * y) % 5 for f, y in Y6_weyl.items()}
        pars = sorted(set(v % 2 for v in degs.values()))
        is_single = len(pars) == 1
        if is_single:
            single_parity_multipliers.append(m)
        multiplier_scan[str(m)] = {
            "degrees_mod5": degs,
            "parities": pars,
            "single_parity_class": is_single,
        }

    # Evaluate both Rule Pi_+ (same parity: kh % 2 == mp) and Rule Pi_- (super-graded opposite parity: kh % 2 != mp)
    rule_results = {"Pi_plus_same_parity": {}, "Pi_minus_super_graded_opposite_parity": {}}
    for sign in (+1, -1):
        m_eff = (2 * sign) % 5
        degs = {f: (m_eff * y) % 5 for f, y in Y6_weyl.items()}
        mp_par = next(iter(set(v % 2 for v in degs.values())))
        w_same = {}
        w_opp = {}
        for sec, (fa, fb) in sectors.items():
            kh = (-(degs[fa] + degs[fb])) % 5
            w_same[sec] = "S" if (kh % 2 == mp_par) else "St"
            w_opp[sec] = "S" if (kh % 2 != mp_par) else "St"
        rule_results["Pi_plus_same_parity"][f"sign_{sign:+d}"] = w_same
        rule_results["Pi_minus_super_graded_opposite_parity"][f"sign_{sign:+d}"] = w_opp

    # Check Frame C's Dirac pairs (q_L, q_R) under k = 2*q mod 5
    dirac_degrees = {
        sec: {"deg_qL": (2 * qL) % 5, "deg_qR": (2 * qR) % 5, "parities": ((2 * qL) % 5 % 2, (2 * qR) % 5 % 2)}
        for sec, (qL, qR) in dirac_frame_c.items()
    }

    m5_holds = (
        single_parity_multipliers == [2, 3]
        and all(v == {"up": "St", "down": "S", "lepton": "S"} for v in rule_results["Pi_plus_same_parity"].values())
        and all(v == {"up": "S", "down": "St", "lepton": "St"} for v in rule_results["Pi_minus_super_graded_opposite_parity"].values())
    )
    return {
        "single_parity_multipliers_in_Z5_star": single_parity_multipliers,
        "multiplier_scan": multiplier_scan,
        "grading_rules_by_hypercharge_sign": rule_results,
        "frame_c_dirac_kernel_degrees": dirac_degrees,
        "M5_holds": m5_holds,
    }


def _random_haar_u3(rng_np: np.random.Generator) -> np.ndarray:
    z = (rng_np.standard_normal((3, 3)) + 1j * rng_np.standard_normal((3, 3))) / math.sqrt(2.0)
    q, r = np.linalg.qr(z)
    d = np.diag(r)
    ph = d / np.abs(d)
    return q * ph[None, :]


def main() -> None:
    t_start = time.time()
    # Startup Gate 0 (Guardrail 3): Unitary Haar basis-scrambling invariance on physical observables
    rng_haar = np.random.default_rng(2026111400)
    yu_test = rng_haar.standard_normal((16, 3, 3)) + 1j * rng_haar.standard_normal((16, 3, 3))
    yd_test = rng_haar.standard_normal((16, 3, 3)) + 1j * rng_haar.standard_normal((16, 3, 3))
    yl_test = rng_haar.standard_normal((16, 3, 3)) + 1j * rng_haar.standard_normal((16, 3, 3))
    base_obs = _extract_12_from_yukawas(yu_test, yd_test, yl_test)
    yu_rot = np.empty_like(yu_test)
    yd_rot = np.empty_like(yd_test)
    yl_rot = np.empty_like(yl_test)
    for b_i in range(16):
        u_lq = _random_haar_u3(rng_haar)
        v_ru = _random_haar_u3(rng_haar)
        v_rd = _random_haar_u3(rng_haar)
        u_ll = _random_haar_u3(rng_haar)
        v_rl = _random_haar_u3(rng_haar)
        yu_rot[b_i] = u_lq @ yu_test[b_i] @ v_ru.conj().T
        yd_rot[b_i] = u_lq @ yd_test[b_i] @ v_rd.conj().T
        yl_rot[b_i] = u_ll @ yl_test[b_i] @ v_rl.conj().T
    haar_err = float(np.max(np.abs(_extract_12_from_yukawas(yu_rot, yd_rot, yl_rot) - base_obs)))
    assert haar_err < 1e-12, f"Haar basis-scrambling invariance violated: {haar_err}"

    print("[X-MEASURE] Building 4-patch Chebyshev + cusp-spine canonical L_2 evaluator...", flush=True)
    end_eval = CanonicalL2Evaluator(n_workers=10)
    print(f"[X-MEASURE] L_2 evaluator ready ({int(round(time.time() - t_start))}s)", flush=True)

    # Startup Gate 1: stitching accuracy between float64 and mpmath at y = 5.0
    t_stitch = np.array([complex(-0.31, 5.0), complex(0.17, 5.0)], dtype=np.complex128)
    f64_st = _eval_f64_p5_avg_grid(t_stitch, end_eval)
    l2_st = end_eval.eval_L2_raw_batch(t_stitch)
    mp_st0 = eval_p5_avg_four_modes_mp(-0.31, 5.0, float(l2_st[0]), dps=120)
    mp_st1 = eval_p5_avg_four_modes_mp(0.17, 5.0, float(l2_st[1]), dps=120)
    stitch_err = max(
        float(np.max(np.abs(f64_st["W_minus_T90"][0] - mp_st0["W_minus_T90"]))),
        float(np.max(np.abs(f64_st["W_minus_T90"][1] - mp_st1["W_minus_T90"]))),
        float(np.max(np.abs(f64_st["W_plus_T90"][0] - mp_st0["W_plus_T90"]))),
    )
    assert stitch_err < 1e-8, f"Stitching mismatch at y=5.0: {stitch_err}"

    # Startup Gate 2: verify matrix-geodesic mpmath integrator matches local_semicircle_charts on {L, R}^+ words
    probe_words = ["LLR", "LLLRR", "LRLRLLRR", "LLLLRRRRLLR"]
    max_mat_vs_chart_err = 0.0
    n_gate2 = 1024
    for pw in probe_words:
        M_pw = (1, 0, 0, 1)
        for ch in pw:
            M_pw = _mat_mul_int(M_pw, (1, 1, 0, 1) if ch == "L" else (1, 0, 1, 1))
        taus_m, ell_m = _geodesic_taus_from_matrix_mp(M_pw, m_nodes=n_gate2)
        ev_m = _eval_reduced_taus_hybrid(taus_m, end_eval)

        _, betas, betaps, ds_l, ell_c = local_semicircle_charts(pw)
        cum = np.cumsum([0.0] + ds_l)
        sg = (np.arange(n_gate2, dtype=np.float64) + 0.5) * (ell_c / n_gate2)
        ki = np.clip(np.searchsorted(cum, sg, side="right") - 1, 0, len(pw) - 1)
        ies = 1j * np.exp(sg - cum[ki])
        zt = (np.asarray(betas)[ki] * ies + np.asarray(betaps)[ki]) / (ies + 1.0)
        tr_c = np.array([reduce_tau_only_f64(complex(z)) for z in zt], dtype=np.complex128)
        ev_c = _eval_reduced_taus_hybrid(tr_c, end_eval)
        assert abs(ell_m - ell_c) < 1e-12
        max_mat_vs_chart_err = max(max_mat_vs_chart_err, float(np.max(np.abs(ev_m["W_minus_T90"] - ev_c["W_minus_T90"]))))
    assert max_mat_vs_chart_err < 1e-4, f"Matrix geodesic vs chart mismatch: {max_mat_vs_chart_err}"

    # 1. Exact Area-Measure Readout & Cusp Treatment
    area_res = compute_area_measure_with_cusp(end_eval, n_workers=10)
    area_raw = area_res.pop("_raw_arrays")

    # 2. Candidate 1 & Candidate 2: Ergodic {L, R}^+ trajectories at levels 5, 10, 15 + Abramov entropy
    t_erg = time.time()
    gap5_n, gap5 = _sl2_markov_gap(5)
    gap10_n, gap10 = _sl2_markov_gap(10)
    gap15_n, gap15 = _sl2_markov_gap(15)
    assert gap5 > 0.1 and gap10 > 0.1 and gap15 > 0.1

    rng_lvl = random.Random(2026111499)
    words_lvl5 = [_sample_closed_lr_trajectory(rng_lvl, 1500, 5) for _ in range(32)]
    words_lvl10 = [_sample_closed_lr_trajectory(rng_lvl, 1500, 10) for _ in range(32)]
    words_lvl15 = [_sample_closed_lr_trajectory(rng_lvl, 1500, 15) for _ in range(32)]

    with Pool(10, initializer=_init_pool_end, initargs=(end_eval,)) as pool:
        res_l5 = pool.map(_eval_lr_ergodic_worker, [(w, 5) for w in words_lvl5])
        res_l10 = pool.map(_eval_lr_ergodic_worker, [(w, 5) for w in words_lvl10])
        res_l15 = pool.map(_eval_lr_ergodic_worker, [(w, 5) for w in words_lvl15])

    def summarize_erg(res_list: List[Dict[str, Any]]) -> Dict[str, Any]:
        ells = np.array([r["ell"] for r in res_list], dtype=np.float64)
        out_modes = {}
        for mk in ("W_minus_T90", "W_minus_old", "W_plus_T90", "W_plus_old"):
            mat = np.array([r["means"][mk] for r in res_list], dtype=np.float64)
            est, se = _jackknife_weighted(ells, mat)
            out_modes[mk] = (est, se)
        return {"ells": ells, "modes": out_modes}

    sum_l5 = summarize_erg(res_l5)
    sum_l10 = summarize_erg(res_l10)
    sum_l15 = summarize_erg(res_l15)
    print(f"[X-MEASURE Levels] Completed level 5/10/15 ergodic runs ({int(round(time.time() - t_erg))}s)", flush=True)

    # Abramov geodesic-flow entropy of move-count measure across all 96*1500 = 144,000 steps
    all_ells_per_step = np.concatenate([sum_l5["ells"], sum_l10["ells"], sum_l15["ells"]]) / 1500.0
    mean_ell_step = float(np.mean(all_ells_per_step))
    se_ell_step = float(np.std(all_ells_per_step, ddof=1) / math.sqrt(len(all_ells_per_step)))
    h_flow_move = math.log(2.0) / mean_ell_step
    se_h_flow_move = (math.log(2.0) / (mean_ell_step ** 2)) * se_ell_step
    m2_holds = bool(h_flow_move < 1.0 - 20.0 * se_h_flow_move)
    assert m2_holds, "M2 Abramov entropy bound failed"

    # Level-refinement invariance test (M3)
    est5, se5 = sum_l5["modes"]["W_minus_T90"]
    est10, se10 = sum_l10["modes"]["W_minus_T90"]
    est15, se15 = sum_l15["modes"]["W_minus_T90"]
    z_10_vs_5 = np.abs(est10 - est5) / np.sqrt(se10 ** 2 + se5 ** 2)
    z_15_vs_5 = np.abs(est15 - est5) / np.sqrt(se15 ** 2 + se5 ** 2)
    idx_7 = [OUTPUT_KEYS_12.index(k) for k in CLAIMED_7_FRAME_CODE]
    max_z_lvl10 = float(np.max(z_10_vs_5[idx_7]))
    max_z_lvl15 = float(np.max(z_15_vs_5[idx_7]))
    m3_holds = bool(max_z_lvl10 < 3.5 and max_z_lvl15 < 3.5)

    # Area vs Move-Count comparison (M1)
    area_wm_t90 = area_raw["W_minus_T90"]
    area_wp_t90 = area_raw["W_plus_T90"]
    rel_shift_area_vs_move_wm = (area_wm_t90 - est5) / est5
    z_area_vs_move_wm = (area_wm_t90 - est5) / se5
    rel_shift_area_vs_move_wp = (area_wp_t90 - sum_l5["modes"]["W_plus_T90"][0]) / sum_l5["modes"]["W_plus_T90"][0]
    m1_holds = bool(
        float(np.max(np.abs(rel_shift_area_vs_move_wm[idx_7]))) > 0.25
        and float(np.min(np.abs(z_area_vs_move_wm[idx_7]))) > 10.0
    )

    # 3. Candidate 3: Pairs Rule P-Q7 (Literal <J, K>, Generator Rewriting, & Same-Monoid Dual Filtration)
    t_c3 = time.time()
    # 3a. PC_MEAS_3: Literal <J, K> dihedral trap check
    J_mat = np.array([[1, 1], [1, 0]], dtype=np.int64)
    J_inv = np.array([[0, 1], [1, -1]], dtype=np.int64)
    K_mat = np.array([[0, 1], [-1, 0]], dtype=np.int64)
    K_inv = -K_mat
    assert np.array_equal(K_mat @ J_mat @ K_inv, -J_inv), "K J K^{-1} != -J^{-1}"
    rng_jk = random.Random(2026111501)
    jk_gens = [J_mat, J_inv, K_mat, K_inv]
    all_commute_with_LR_axis = True
    LR_mat = J_mat @ J_mat
    for _ in range(500):
        W = np.eye(2, dtype=np.int64)
        for _ in range(rng_jk.randint(2, 16)):
            W = W @ rng_jk.choice(jk_gens)
        if int(round(np.linalg.det(W))) == 1 and abs(int(W[0, 0] + W[1, 1])) > 2:
            # Must commute with LR up to inverse (same golden axis: W * LR == LR * W)
            if not np.array_equal(W @ LR_mat, LR_mat @ W):
                all_commute_with_LR_axis = False
                break
    assert all_commute_with_LR_axis, "PC_MEAS_3 dihedral trap violated"

    # 3b. PC_MEAS_4: Generator rewriting at n = 28 ({L, R}^+ vs {J, J^{-1}, P} even-#P vs {L, R, L^{-1}, R^{-1}})
    rng_gen = random.Random(2026111502)

    def sample_lr_pos_matrices(n_words: int = 260, word_len: int = 28) -> List[Tuple[int, int, int, int]]:
        L_i, R_i = (1, 1, 0, 1), (1, 0, 1, 1)
        out_m = []
        while len(out_m) < n_words:
            M = (1, 0, 0, 1)
            hL = hR = False
            for _ in range(word_len):
                if rng_gen.random() < 0.5:
                    M = _mat_mul_int(M, L_i); hL = True
                else:
                    M = _mat_mul_int(M, R_i); hR = True
            if hL and hR and abs(M[0] + M[3]) > 2 and _is_allowed_at_level(M, 5):
                out_m.append(M)
        return out_m

    def sample_jp_even_matrices(n_words: int = 260, word_len: int = 28) -> List[Tuple[int, int, int, int]]:
        # Reduced words in {J, J^{-1}, P} with #P even (so det = +1 because det J = -1, det P = -1 => det = (-1)^{word_len} = +1 for even word_len!)
        # Wait: BOTH J = [[1,1],[1,0]] and P = [[0,1],[1,0]] have det = -1!!
        # Therefore ANY word of EVEN total length in {J, J^{-1}, P} has det = (-1)^{even} = +1 automatically!!
        J_t = (1, 1, 1, 0)
        Ji_t = (0, 1, 1, -1)
        P_t = (0, 1, 1, 0)
        alph = [("J", J_t), ("Ji", Ji_t), ("P", P_t)]
        forbid = {"J": "Ji", "Ji": "J", "P": "P"}
        assert word_len % 2 == 0
        out_m = []
        while len(out_m) < n_words:
            M = (1, 0, 0, 1)
            prev = ""
            for _ in range(word_len):
                choices = [x for x in alph if x[0] != forbid.get(prev, "")]
                tag, G = rng_gen.choice(choices)
                M = _mat_mul_int(M, G)
                prev = tag
            assert M[0] * M[3] - M[1] * M[2] == 1
            if abs(M[0] + M[3]) > 2 and M[2] != 0 and _is_allowed_at_level(M, 5):
                out_m.append(M)
        return out_m

    def sample_lr_sym_undoing_matrices(n_words: int = 260, word_len: int = 28) -> List[Tuple[int, int, int, int]]:
        # Reduced words in {L, R, L^{-1}, R^{-1}} obtained by closing {L, R} under undoing K (K L K^{-1} = R^{-1}, K R K^{-1} = L^{-1})
        alph = [
            ("L", (1, 1, 0, 1)),
            ("R", (1, 0, 1, 1)),
            ("Li", (1, -1, 0, 1)),
            ("Ri", (1, 0, -1, 1)),
        ]
        forbid = {"L": "Li", "Li": "L", "R": "Ri", "Ri": "R"}
        out_m = []
        while len(out_m) < n_words:
            M = (1, 0, 0, 1)
            prev = ""
            for _ in range(word_len):
                choices = [x for x in alph if x[0] != forbid.get(prev, "")]
                tag, G = rng_gen.choice(choices)
                M = _mat_mul_int(M, G)
                prev = tag
            if abs(M[0] + M[3]) > 2 and M[2] != 0 and _is_allowed_at_level(M, 5):
                out_m.append(M)
        return out_m

    mats_g0 = sample_lr_pos_matrices(260, 28)
    mats_g1 = sample_jp_even_matrices(260, 28)
    mats_g2 = sample_lr_sym_undoing_matrices(260, 28)

    # 3c. Same-Monoid Dual Filtration on {L, R}^+:
    # Compare exhaustive combinatorial length |w| <= 10 Lyndon geodesics against exhaustive hyperbolic trace cutoffs T_max in {15, 35, 75}
    words_comb_10: List[Tuple[str, Tuple[int, int, int, int]]] = []
    for w_len in range(2, 11):
        for bits in range(1 << (w_len - 1)):
            w_s = "L" + "".join("R" if ((bits >> k) & 1) else "L" for k in range(w_len - 2, -1, -1))
            if "R" not in w_s or not _is_lyndon_word(w_s):
                continue
            mat_comb = (1, 0, 0, 1)
            for ch in w_s:
                mat_comb = _mat_mul_int(mat_comb, (1, 1, 0, 1) if ch == "L" else (1, 0, 1, 1))
            if (mat_comb[0] + mat_comb[3]) > 2 and _is_allowed_at_level(mat_comb, 5):
                words_comb_10.append((w_s, mat_comb))

    trace_cutoffs = (15, 35, 75)
    trace_pop_words = {t_max: enumerate_lr_lyndon_by_trace_bound(t_max, level=5) for t_max in trace_cutoffs}

    with Pool(10, initializer=_init_pool_end, initargs=(end_eval,)) as pool:
        ev_g0 = pool.map(_eval_matrix_geodesic_worker, [(m, 96) for m in mats_g0])
        ev_g1 = pool.map(_eval_matrix_geodesic_worker, [(m, 96) for m in mats_g1])
        ev_g2 = pool.map(_eval_matrix_geodesic_worker, [(m, 96) for m in mats_g2])
        ev_comb10 = pool.map(_eval_matrix_geodesic_worker, [(m, 112) for (_, m) in words_comb_10])

        # Evaluate union of trace_cutoff = 75 primitive Lyndon geodesics once and slice for 15, 35, 75
        words_75 = trace_pop_words[75]
        ev_tr75 = pool.map(_eval_matrix_geodesic_worker, [(m, 112) for (_, m) in words_75])

    def summarize_mat_pop(ev_list: List[Tuple[float, Dict[str, np.ndarray]]]) -> Tuple[np.ndarray, np.ndarray]:
        ells = np.array([x[0] for x in ev_list], dtype=np.float64)
        mat = np.array([x[1]["W_minus_T90"] for x in ev_list], dtype=np.float64)
        return _jackknife_weighted(ells, mat)

    est_g0, se_g0 = summarize_mat_pop(ev_g0)
    est_g1, se_g1 = summarize_mat_pop(ev_g1)
    est_g2, se_g2 = summarize_mat_pop(ev_g2)
    est_comb10, _ = summarize_mat_pop(ev_comb10)

    z_jp_vs_lr = np.abs(est_g1 - est_g0) / np.sqrt(se_g1 ** 2 + se_g0 ** 2)
    z_sym_vs_lr = np.abs(est_g2 - est_g0) / np.sqrt(se_g2 ** 2 + se_g0 ** 2)
    max_z_jp = float(np.max(z_jp_vs_lr[idx_7]))
    max_z_sym = float(np.max(z_sym_vs_lr[idx_7]))
    pc4_fired = bool(max_z_jp > 10.0 and max_z_sym > 10.0)

    trace_filtration_results: Dict[str, Any] = {
        "combinatorial_word_len_le_10": {
            "max_combinatorial_word_length": 10,
            "n_primitive_lyndon_geodesics": len(words_comb_10),
            "W_minus_T90_claimed_7": _dict_7_fc(est_comb10),
            "W_minus_T90_all_12": _dict_12(est_comb10),
        }
    }
    for t_max in trace_cutoffs:
        sub_ev = [
            ev_tr75[i]
            for i, (_, m) in enumerate(words_75)
            if (m[0] + m[3]) <= t_max
        ]
        ells_sub = np.array([x[0] for x in sub_ev], dtype=np.float64)
        mat_sub = np.array([x[1]["W_minus_T90"] for x in sub_ev], dtype=np.float64)
        mean_sub = np.sum(ells_sub[:, None] * mat_sub, axis=0) / float(np.sum(ells_sub))
        max_word_len = max(len(words_75[i][0]) for i, (_, m) in enumerate(words_75) if (m[0] + m[3]) <= t_max)
        trace_filtration_results[str(t_max)] = {
            "trace_bound": t_max,
            "geodesic_length_bound": 2.0 * math.acosh(t_max / 2.0),
            "n_primitive_lyndon_geodesics": len(sub_ev),
            "max_combinatorial_word_length_included": max_word_len,
            "W_minus_T90_claimed_7": _dict_7_fc(mean_sub),
            "W_minus_T90_all_12": _dict_12(mean_sub),
            "_raw": mean_sub,
        }

    # Check that filtering the SAME {L, R}^+ monoid by hyperbolic length shifts all 4 singular-value ratios
    # away from combinatorial move-count toward area measure!
    tr75_raw = trace_filtration_results["75"]["_raw"]
    for t_k in trace_filtration_results.values():
        t_k.pop("_raw", None)
    ratio_idxs = [0, 1, 3, 4]  # up 2/3, up 1/3, down 2/3, down 1/3
    shifts_toward_area_vs_erg = all(
        abs(float(tr75_raw[i] - area_wm_t90[i])) < abs(float(est5[i] - area_wm_t90[i]))
        for i in ratio_idxs
    )
    shifts_toward_area_vs_comb10 = all(
        abs(float(tr75_raw[i] - area_wm_t90[i])) < abs(float(est_comb10[i] - area_wm_t90[i]))
        for i in ratio_idxs
    )
    shifts_toward_area = bool(shifts_toward_area_vs_erg and shifts_toward_area_vs_comb10)
    m4_holds = bool(all_commute_with_LR_axis and pc4_fired and shifts_toward_area)
    print(f"[X-MEASURE Candidate 3] Completed generator & dual-filtration tests ({int(round(time.time() - t_c3))}s)", flush=True)

    # 4. M24 Cold Read Algebraic Verification of B1936
    b1936_audit = audit_b1936_algebra()
    assert b1936_audit["M5_holds"], "B1936 algebraic verification failed"

    out_payload = {
        "card": "X-MEASURE",
        "seat": "agy-exp",
        "messages_covered": ["M23_area_measure", "M24_B1936_cold_read", "M25_X_MEASURE"],
        "expectations_commit": "2a67770de",
        "empirical_firewall": "0 of 19",
        "particle_names_used": False,
        "b1932_area_json_read_before_commit": False,
        "script_sha256": hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
        "total_elapsed_seconds": round(time.time() - t_start, 3),
        "startup_gates": {
            "haar_basis_scrambling_max_err": haar_err,
            "stitching_y5_f64_vs_mpmath_max_err": stitch_err,
            "matrix_geodesic_mp_vs_semicircle_chart_max_err": max_mat_vs_chart_err,
        },
        "expectations_summary": {
            "M1_area_vs_move_and_cusp_holds": m1_holds,
            "M2_abramov_maximal_entropy_dichotomy_holds": m2_holds,
            "M3_level_refinement_invariance_selects_neither_holds": m3_holds,
            "M4_pairs_rule_and_same_monoid_dual_filtration_holds": m4_holds,
            "M5_b1936_cold_read_algebra_holds": b1936_audit["M5_holds"],
            "PC_MEAS_1_float64_cusp_svd_underflow_fired": area_res["PC_MEAS_1_float64_cusp_svd_underflow"]["fired"],
            "PC_MEAS_2_hard_cusp_cutoff_bias_fired": area_res["PC_MEAS_2_hard_cusp_cutoff_bias"]["fired"],
            "PC_MEAS_3_literal_JK_dihedral_trap_fired": all_commute_with_LR_axis,
            "PC_MEAS_4_generator_rewriting_shift_fired": pc4_fired,
        },
        "area_measure_readout": area_res,
        "area_vs_move_count_comparison": {
            "W_minus_T90_relative_shift_area_minus_move": _dict_12(rel_shift_area_vs_move_wm),
            "W_minus_T90_z_vs_move_se": _dict_12(z_area_vs_move_wm),
            "W_plus_T90_relative_shift_area_minus_move": _dict_12(rel_shift_area_vs_move_wp),
        },
        "candidate1_maximal_entropy_abramov": {
            "move_count_symbolic_entropy_per_step": math.log(2.0),
            "mean_hyperbolic_length_per_LR_step": mean_ell_step,
            "mean_hyperbolic_length_per_LR_step_se": se_ell_step,
            "move_count_geodesic_flow_entropy_per_unit_length": h_flow_move,
            "move_count_geodesic_flow_entropy_se": se_h_flow_move,
            "liouville_area_geodesic_flow_entropy_per_unit_length": 1.0,
            "entropy_gap_z_below_liouville": (1.0 - h_flow_move) / se_h_flow_move,
        },
        "candidate2_level_refinement_invariance": {
            "sl2_markov_spectral_gaps": {
                "level_5": {"group_order": gap5_n, "spectral_gap": gap5},
                "level_10": {"group_order": gap10_n, "spectral_gap": gap10},
                "level_15": {"group_order": gap15_n, "spectral_gap": gap15},
            },
            "ergodic_W_minus_T90_by_level": {
                "level_5": {"claimed_7": _dict_7_fc(est5), "se_7": _dict_7_fc(se5)},
                "level_10": {"claimed_7": _dict_7_fc(est10), "se_7": _dict_7_fc(se10), "max_z_vs_level5": max_z_lvl10},
                "level_15": {"claimed_7": _dict_7_fc(est15), "se_7": _dict_7_fc(se15), "max_z_vs_level5": max_z_lvl15},
            },
        },
        "candidate3_pairs_rule_and_dual_filtration": {
            "PC_MEAS_3_literal_JK_commutes_with_golden_axis": all_commute_with_LR_axis,
            "generator_rewriting_n28_W_minus_T90": {
                "G0_LR_positive_monoid": {"claimed_7": _dict_7_fc(est_g0), "se_7": _dict_7_fc(se_g0)},
                "G1_JP_tick_and_swap_even": {"claimed_7": _dict_7_fc(est_g1), "se_7": _dict_7_fc(se_g1), "max_z_vs_LR": max_z_jp},
                "G2_LR_symmetric_with_undoing": {"claimed_7": _dict_7_fc(est_g2), "se_7": _dict_7_fc(se_g2), "max_z_vs_LR": max_z_sym},
            },
            "same_monoid_geodesic_length_filtration_LR_pos": trace_filtration_results,
            "all_four_ratios_shift_from_move_toward_area": shifts_toward_area,
        },
        "m24_b1936_algebraic_audit": b1936_audit,
    }

    OUT_JSON.write_text(json.dumps(out_payload, indent=2) + "\n")
    out_sha = hashlib.sha256(OUT_JSON.read_bytes()).hexdigest()
    (HERE / "OUTPUT_SHA256.txt").write_text(f"{out_sha}  verify_x_measure_out.json\n")
    print(f"[X-MEASURE] Wrote JSON output cleanly in {int(round(time.time() - t_start))}s", flush=True)


if __name__ == "__main__":
    main()
