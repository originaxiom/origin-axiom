#!/usr/bin/env python3
"""
Standalone Zero-Import Verifier for Card X-SURVIVAL:
What Survives Cancellation — Testing Four Pre-Registered Falsifiers (S1-S4)
and Four Planted Negative Controls (PC_SURV_1-PC_SURV_4).

Strict Guardrails & Firewall:
  - Zero imports from the repository (standard library, numpy, scipy.special, mpmath only).
  - Zero empirical / PDG / cosmological values ("0 of 19").
  - Outputs named strictly by (sector, index) positions; zero particle names.
  - All numerical values written exclusively to verify_x_survival_out.json;
    stdout prints structural progress, integer counts, and gate statuses only.
"""

from __future__ import annotations

import cmath
import hashlib
import json
import math
import os
import pathlib
import random
import time
from fractions import Fraction
from multiprocessing import Pool
from typing import Any, Dict, List, Optional, Tuple

import mpmath as mp
import numpy as np
from scipy.special import digamma

HERE = pathlib.Path(__file__).resolve().parent
OUT_JSON = HERE / "verify_x_survival_out.json"

EULER_GAMMA = 0.57721566490153286060651209008240243104215933593992
NORM_CONST_SHIFT = EULER_GAMMA + math.log(math.pi)


# ============================================================================
# SECTION 0: PUNCTURED-TORUS FUCHSIAN UNIFORMIZER & 4-PATCH CHEBYSHEV EVALUATOR
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
    m_max = max(1, int(math.ceil(6.8 / ty)) + 1)
    for m in range(1, m_max + 1):
        mt = m * tau
        zm_p = pi * (z + mt)
        zm_m = pi * (z - mt)
        m_t = pi * mt
        sp, cp = cmath.sin(zm_p), cmath.cos(zm_p)
        sm, cm = cmath.sin(zm_m), cmath.cos(zm_m)
        st = cmath.sin(m_t)
        isp2 = 1.0 / (sp * sp)
        ism2 = 1.0 / (sm * sm)
        ist2 = 1.0 / (st * st)
        wp += pi2 * (isp2 + ism2 - 2.0 * ist2)
        wpp += -2.0 * pi3 * (cp * isp2 / sp + cm * ism2 / sm)
    return wp, wpp


def _eisenstein_g2_g3_E2_f64(tau: complex) -> Tuple[complex, complex, complex]:
    q = cmath.exp(2j * math.pi * tau)
    E2 = 1.0 + 0j
    E4 = 1.0 + 0j
    E6 = 1.0 + 0j
    qn = q
    for n in range(1, 18):
        if abs(qn) < 1e-18:
            break
        lam = qn / (1.0 - qn)
        n2 = n * n
        n3 = n2 * n
        E2 -= 24.0 * n * lam
        E4 += 240.0 * n3 * lam
        E6 -= 504.0 * (n3 * n2) * lam
        qn *= q
    pi2 = math.pi * math.pi
    pi4 = pi2 * pi2
    return (4.0 * pi4 / 3.0) * E4, (8.0 * pi4 * pi2 / 27.0) * E6, E2


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
    b = [0j]
    for n in range(1, n_terms):
        an = -sum(qcoeffs[n - 1 - m] * a[m] for m in range(n)) / (4.0 * n * n)
        bn = -(4.0 * n * an + sum(qcoeffs[n - 1 - m] * b[m] for m in range(1, n))) / (4.0 * n * n)
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
    if abs(z_end - z_start) < 1e-15:
        return Y_init.copy()
    h = (z_end - z_start) / n_steps
    z = z_start
    y00, y01 = Y_init[0, 0], Y_init[0, 1]
    y10, y11 = Y_init[1, 0], Y_init[1, 1]
    p = [0j] * (order + 1)
    q = [0j] * order
    u0 = [0j] * (order + 1)
    u1 = [0j] * (order + 1)
    g2_q = g2 / 4.0
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
    M_T = np.array([[cw, -q_const * sw_om], [sw_om, cw]], dtype=np.complex128)
    return Y_init @ M_T


def _lame_mono_f64(tau: complex, c_acc: complex) -> Tuple[np.ndarray, np.ndarray]:
    g2, g3, E2 = _eisenstein_g2_g3_E2_f64(tau)
    z0 = -0.5 - 0.5 * tau
    tx, ty = tau.real, tau.imag
    min_per = min(abs(m + n * tau) for m in range(-2, 3) for n in range(-2, 3) if (m, n) != (0, 0))
    r_target = min(0.20 * min_per, 0.45 * abs(z0))
    zf = z0 * (r_target / abs(z0))
    Yf = _lame_frob_f64(zf, g2, g3, c_acc, n_terms=24)
    q_asymp = -(math.pi ** 2 / 12.0) * E2 + c_acc

    def smart_prop(Y_in: np.ndarray, za: complex, zb: complex) -> np.ndarray:
        if ty > 14.0 and abs(zb.imag - za.imag) > 12.5:
            ka = round(za.imag / ty)
            kb = round(zb.imag / ty)
            if ka != kb:
                sgn = 1.0 if (zb.imag > za.imag) else -1.0
                dy = zb.imag - za.imag
                t1 = (ka * ty + sgn * 6.2 - za.imag) / dy
                t2 = (kb * ty - sgn * 6.2 - za.imag) / dy
                if 0.0 < t1 < t2 < 1.0:
                    z1 = za + t1 * (zb - za)
                    z2 = za + t2 * (zb - za)
                    d1 = max(1e-4, _seg_lat_dist_f(za.real, za.imag, z1.real, z1.imag, tx, ty))
                    d2 = max(1e-4, _seg_lat_dist_f(z2.real, z2.imag, zb.real, zb.imag, tx, ty))
                    n1 = max(24, int(math.ceil(abs(z1 - za) / (0.065 * d1))))
                    n2 = max(24, int(math.ceil(abs(zb - z2) / (0.065 * d2))))
                    Ym1 = _taylor_prop_f64(Y_in, za, z1, tau, g2, c_acc, n_steps=n1, order=18)
                    Ym2 = _prop_const_f64(Ym1, z2 - z1, q_asymp)
                    return _taylor_prop_f64(Ym2, z2, zb, tau, g2, c_acc, n_steps=n2, order=18)
        d_seg = max(1e-4, _seg_lat_dist_f(za.real, za.imag, zb.real, zb.imag, tx, ty))
        n_st = max(22, int(math.ceil(abs(zb - za) / (0.065 * d_seg))))
        return _taylor_prop_f64(Y_in, za, zb, tau, g2, c_acc, n_steps=n_st, order=18)

    Y0 = smart_prop(Yf, zf, z0)
    YA = smart_prop(Y0, z0, z0 + 1.0)
    YB = smart_prop(Y0, z0, z0 + tau)
    return YA @ np.linalg.inv(Y0), YB @ np.linalg.inv(Y0)


def uniformize_tilde_L2_fast(tau: complex) -> float:
    if abs(tau - 1j) < 1e-14 or abs(tau - cmath.exp(1j * math.pi / 3.0)) < 1e-14:
        c_cur = 0j
    else:
        n_h = max(1, min(6, int(math.ceil(abs(tau - 1j) / 2.0))))
        c_cur = 0j
        eps = 1e-8
        for st in range(1, n_h + 1):
            ts = (1.0 - st / n_h) * 1j + (st / n_h) * tau
            for _ in range(8):
                MA, MB = _lame_mono_f64(ts, c_cur)
                fA = (MA[0, 0] + MA[1, 1]).imag
                fB = (MB[0, 0] + MB[1, 1]).imag
                if max(abs(fA), abs(fB)) < 1e-13:
                    break
                MA_p, MB_p = _lame_mono_f64(ts, c_cur + eps)
                dA = ((MA_p[0, 0] + MA_p[1, 1]) - (MA[0, 0] + MA[1, 1])) / eps
                dB = ((MB_p[0, 0] + MB_p[1, 1]) - (MB[0, 0] + MB[1, 1])) / eps
                det = dA.imag * dB.real - dA.real * dB.imag
                dx = -(dB.real * fA - dA.real * fB) / det
                dy = -(-dB.imag * fA + dA.imag * fB) / det
                c_cur += complex(dx, dy)
    MA, MB = _lame_mono_f64(tau, c_cur)
    comm = MA @ MB @ np.linalg.inv(MA) @ np.linalg.inv(MB)
    lam = abs(comm[0, 1].real)
    assert abs(lam - 1.0) < 1e-9
    imB = -0.5 * (MA[0, 0].imag / MA[1, 0].real + MB[0, 0].imag / MB[1, 0].real)
    L_2 = math.pi - (2.0 * math.pi / lam) * imB
    return L_2 + 0.5 * math.log(tau.imag) - NORM_CONST_SHIFT


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
        self.p1_nx, self.p1_ny = 16, 16
        self.p2_nx, self.p2_ny = 12, 16
        self.p3_nx, self.p3_ny = 8, 16
        self.p4_nx, self.p4_ny = 6, 14

        self.x1, self.wx1 = _cheb_nodes_weights(self.p1_nx)
        self.y1, self.wy1 = _cheb_nodes_weights(self.p1_ny)
        self.x2, self.wx2 = _cheb_nodes_weights(self.p2_nx)
        self.y2, self.wy2 = _cheb_nodes_weights(self.p2_ny)
        self.x3, self.wx3 = _cheb_nodes_weights(self.p3_nx)
        self.y3, self.wy3 = _cheb_nodes_weights(self.p3_ny)
        self.x4, self.wx4 = _cheb_nodes_weights(self.p4_nx)
        self.y4, self.wy4 = _cheb_nodes_weights(self.p4_ny)

        tasks: List[complex] = []
        for u_x in self.x1:
            xv = 0.25 * (u_x + 1.0)
            ylo = math.sqrt(max(0.0, 1.0 - xv * xv))
            for u_y in self.y1:
                yv = ylo + (1.85 - ylo) * 0.5 * (u_y + 1.0)
                tasks.append(complex(xv, yv))
        for u_x in self.x2:
            xv = 0.25 * (u_x + 1.0)
            for u_y in self.y2:
                yv = 1.85 + (4.50 - 1.85) * 0.5 * (u_y + 1.0)
                tasks.append(complex(xv, yv))
        for u_x in self.x3:
            xv = 0.25 * (u_x + 1.0)
            for u_y in self.y3:
                yv = 4.50 + (12.0 - 4.50) * 0.5 * (u_y + 1.0)
                tasks.append(complex(xv, yv))
        u_lo, u_hi = 1.0 / 36.0, 1.0 / 12.0
        for u_x in self.x4:
            xv = 0.25 * (u_x + 1.0)
            for u_y in self.y4:
                inv_y = u_lo + (u_hi - u_lo) * 0.5 * (u_y + 1.0)
                tasks.append(complex(xv, 1.0 / inv_y))

        with Pool(n_workers) as pool:
            arr = np.array(pool.map(uniformize_tilde_L2_fast, tasks), dtype=np.float64)

        n1 = self.p1_nx * self.p1_ny
        n2 = self.p2_nx * self.p2_ny
        n3 = self.p3_nx * self.p3_ny
        n4 = self.p4_nx * self.p4_ny
        i0 = 0
        self.v1 = arr[i0:i0 + n1].reshape(self.p1_nx, self.p1_ny); i0 += n1
        self.v2 = arr[i0:i0 + n2].reshape(self.p2_nx, self.p2_ny); i0 += n2
        self.v3 = arr[i0:i0 + n3].reshape(self.p3_nx, self.p3_ny); i0 += n3
        self.v4 = arr[i0:i0 + n4].reshape(self.p4_nx, self.p4_ny)

    def eval_batch(self, tau_red: np.ndarray) -> np.ndarray:
        xv = np.clip(np.abs(tau_red.real), 0.0, 0.5)
        yv = tau_red.imag
        out = np.empty(len(tau_red), dtype=np.float64)
        m1 = yv <= 1.85
        m2 = (yv > 1.85) & (yv <= 4.50)
        m3 = (yv > 4.50) & (yv <= 12.0)
        m4 = (yv > 12.0) & (yv <= 36.0)
        m5 = yv > 36.0
        if np.any(m1):
            xx, yy = xv[m1], yv[m1]
            ylo = np.sqrt(np.maximum(0.0, 1.0 - xx * xx))
            sv = np.clip((yy - ylo) / (1.85 - ylo), 0.0, 1.0)
            bx = _bary_weights_batch(4.0 * xx - 1.0, self.x1, self.wx1)
            by = _bary_weights_batch(2.0 * sv - 1.0, self.y1, self.wy1)
            out[m1] = np.einsum("ni,ij,nj->n", bx, self.v1, by)
        if np.any(m2):
            xx, yy = xv[m2], yv[m2]
            bx = _bary_weights_batch(4.0 * xx - 1.0, self.x2, self.wx2)
            by = _bary_weights_batch(2.0 * (yy - 1.85) / (4.50 - 1.85) - 1.0, self.y2, self.wy2)
            out[m2] = np.einsum("ni,ij,nj->n", bx, self.v2, by)
        if np.any(m3):
            xx, yy = xv[m3], yv[m3]
            bx = _bary_weights_batch(4.0 * xx - 1.0, self.x3, self.wx3)
            by = _bary_weights_batch(2.0 * (yy - 4.50) / (12.0 - 4.50) - 1.0, self.y3, self.wy3)
            out[m3] = np.einsum("ni,ij,nj->n", bx, self.v3, by)
        if np.any(m4):
            xx, inv_y = xv[m4], 1.0 / yv[m4]
            u_lo, u_hi = 1.0 / 36.0, 1.0 / 12.0
            bx = _bary_weights_batch(4.0 * xx - 1.0, self.x4, self.wx4)
            by = _bary_weights_batch(2.0 * (inv_y - u_lo) / (u_hi - u_lo) - 1.0, self.y4, self.wy4)
            out[m4] = np.einsum("ni,ij,nj->n", bx, self.v4, by)
        if np.any(m5):
            for idx in np.where(m5)[0]:
                out[idx] = uniformize_tilde_L2_fast(complex(xv[idx], yv[idx]))
        return out


# ============================================================================
# SECTION 1: SERRE WEIGHT-3/2 TRIPLET, YUKAWA TENSOR, RESIDUES & NORM
# ============================================================================

def _build_serre_B1_coeff_table(max_k: int = 200) -> Tuple[np.ndarray, np.ndarray]:
    N = max_k

    def s_mul(a, b):
        out = {}
        for k1, (r1, i1) in a.items():
            for k2, (r2, i2) in b.items():
                k = k1 + k2
                if k > N:
                    continue
                rr = r1 * r2 - i1 * i2
                ii = r1 * i2 + i1 * r2
                if rr or ii:
                    pr, pi_ = out.get(k, (Fraction(0), Fraction(0)))
                    nr, ni = pr + rr, pi_ + ii
                    if nr or ni:
                        out[k] = (nr, ni)
                    elif k in out:
                        del out[k]
        return out

    def s_inv(a):
        k0 = min(a)
        r0, i0 = a[k0]
        n2 = r0 * r0 + i0 * i0
        inv0 = (r0 / n2, -i0 / n2)
        M = N + k0
        sj = [a.get(k0 + j, (Fraction(0), Fraction(0))) for j in range(M + 1)]
        t = [inv0]
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

    th2 = {}
    n = 0
    while (2 * n + 1) ** 2 <= N:
        th2[(2 * n + 1) ** 2] = (Fraction(2), Fraction(0))
        n += 1
    th3 = {0: (Fraction(1), Fraction(0))}
    th4 = {0: (Fraction(1), Fraction(0))}
    n = 1
    while 4 * n * n <= N:
        th3[4 * n * n] = (Fraction(2), Fraction(0))
        th4[4 * n * n] = (Fraction(2 * ((-1) ** n)), Fraction(0))
        n += 1
    e2 = {0: (Fraction(1), Fraction(0))}
    for m in range(1, N // 8 + 1):
        sig1 = sum(d for d in range(1, m + 1) if m % d == 0)
        e2[8 * m] = (Fraction(-24 * sig1), Fraction(0))

    di = s_inv(s_mul(s_mul(th2, th3), th4))
    R0 = {k: (-v[0], -v[1]) for k, v in s_mul(s_mul(th2, th2), di).items()}
    R1 = {k: (-v[0], -v[1]) for k, v in s_mul(s_mul(th4, th4), di).items()}
    R2 = s_mul(s_mul(s_mul(th3, th3), {0: (Fraction(0), Fraction(1))}), di)

    def serre_mhalf(f):
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
    for col, d in enumerate(B1):
        for row, k in enumerate(all_ks):
            if k in d:
                mat[row, col] = complex(float(d[k][0]), float(d[k][1]))
    return ks_arr, mat


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


SERRE_KS, SERRE_MAT = _build_serre_B1_coeff_table(200)
T_COUP = _build_coupling_tensor()

SIX_CHARGES = {
    "up": (1, -4),
    "down": (1, 2),
    "lepton": (-3, 6),
}

P5_ALL_24: List[Tuple[float, float]] = [
    (j / 5.0, k / 5.0) for j in range(5) for k in range(5) if (j, k) != (0, 0)
]
P5_HALF_12: List[Tuple[float, float]] = []
_seen5 = set()
for _j in range(5):
    for _k in range(5):
        if (_j, _k) == (0, 0):
            continue
        _neg = ((-_j) % 5, (-_k) % 5)
        if (_j, _k) not in _seen5 and _neg not in _seen5:
            P5_HALF_12.append((_j / 5.0, _k / 5.0))
            _seen5.add((_j, _k))
            _seen5.add(_neg)
assert len(P5_HALF_12) == 12

# Primitive order-15 points: gcd(j, k, 15) == 1 (192 points = 96 antipodal pairs)
P15_INT_192: List[Tuple[int, int]] = [
    (j, k) for j in range(15) for k in range(15) if math.gcd(math.gcd(j, k), 15) == 1
]
assert len(P15_INT_192) == 192
P15_HALF_96: List[Tuple[float, float]] = []
_seen15 = set()
for _j, _k in P15_INT_192:
    _neg = ((-_j) % 15, (-_k) % 15)
    if (_j, _k) not in _seen15 and _neg not in _seen15:
        P15_HALF_96.append((_j / 15.0, _k / 15.0))
        _seen15.add((_j, _k))
        _seen15.add(_neg)
assert len(P15_HALF_96) == 96


def eval_B1_vec(tau: complex) -> np.ndarray:
    xq = cmath.exp(1j * math.pi * tau / 4.0)
    return (xq ** SERRE_KS) @ SERRE_MAT


def _theta_char_batch(alpha: np.ndarray, beta: np.ndarray, tau: np.ndarray, half_win: int = 8) -> np.ndarray:
    a_tilde = alpha - np.rint(alpha)
    ks = np.arange(-half_win, half_win + 1, dtype=np.float64)[None, :]
    m = ks + a_tilde[:, None]
    exponent = 1j * math.pi * tau[:, None] * (m * m) + 2j * math.pi * m * beta[:, None]
    return np.sum(np.exp(exponent), axis=1)


def _th1_prime_0_batch(tau: np.ndarray, n_terms: int = 10) -> np.ndarray:
    ks = np.arange(n_terms, dtype=np.float64)[None, :]
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
    R_j = (-1.0) * _theta_char_batch(ap, bp + 0.5, tau) * _theta_char_batch(am, bm + 0.5, tau) / th1p0
    R_k = (+1j) * _theta_char_batch(ap, bp, tau) * _theta_char_batch(am, bm, tau) / th1p0
    return np.stack([R_1, R_i, R_j, R_k], axis=1)


def _F_kronecker_batch(u1: np.ndarray, u2: np.ndarray, tau: np.ndarray, k_max: int = 16) -> np.ndarray:
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

    ks = np.arange(-k_max, k_max + 1, dtype=np.float64)[None, :]
    a_eff = np.where(a_zero, 0.0, a)[:, None]
    m = ks + a_eff
    m_nz = np.abs(m) > 1e-12
    m_safe = np.where(m_nz, m, 1.0)
    w = np.exp(-2.0 * math.pi * np.abs(m_safe) * y[:, None] + 2j * math.pi * (m_safe * x[:, None] + u2[:, None]))
    term = np.where(m_nz, (2.0 * math.pi / np.abs(m_safe)) * np.real(w / (1.0 - w)), 0.0)
    return base + np.sum(term, axis=1)


def build_yukawa_batch(
    tau: np.ndarray,
    a_arr: np.ndarray,
    b_arr: np.ndarray,
    tilde_L: np.ndarray,
) -> Tuple[Dict[str, np.ndarray], Dict[str, np.ndarray]]:
    """
    Returns (Y_W_minus, Y_W_plus) dictionaries mapping sector -> (B, 3, 3) complex Yukawa matrices,
    where W_minus = (up: St, down: S, lepton: S) and W_plus = (up: S, down: St, lepton: St).
    """
    xq = np.exp(1j * math.pi * tau / 4.0)
    c3_S = (xq[:, None] ** SERRE_KS[None, :]) @ SERRE_MAT
    c3_St = np.conj(c3_S)

    Y_minus: Dict[str, np.ndarray] = {}
    Y_plus: Dict[str, np.ndarray] = {}
    for sec, (qL, qR) in SIX_CHARGES.items():
        R_mat = _residues_closed_batch(tau, a_arr, b_arr, qL, qR)
        ap = (qL + qR) * a_arr
        bp = (qL + qR) * b_arr
        shifts = [(ap, bp), (ap, bp - 0.5), (ap - 0.5, bp), (ap - 0.5, bp - 0.5)]
        u_mat = np.zeros_like(R_mat)
        for s_idx, (u1, u2) in enumerate(shifts):
            R_col = R_mat[:, s_idx]
            active = np.abs(R_col) > 1e-12
            if np.any(active):
                Fu = _F_kronecker_batch(u1[active], u2[active], tau[active])
                w_sq = np.maximum(0.0, 2.0 * math.pi * tilde_L[active] + Fu)
                u_mat[active, s_idx] = np.sqrt(w_sq) * R_col[active]
        Y_S = np.einsum("ba,bs,asrc->brc", c3_S, u_mat, T_COUP)
        Y_St = np.einsum("ba,bs,asrc->brc", c3_St, u_mat, T_COUP)
        if sec == "up":
            Y_minus[sec] = Y_St
            Y_plus[sec] = Y_S
        else:
            Y_minus[sec] = Y_S
            Y_plus[sec] = Y_St
    return Y_minus, Y_plus


# ============================================================================
# SECTION 2: TEST S1 — QUANTUM TRACE CANCELLATION OF ODD TICKS ON T (+) T_bar
# ============================================================================

def run_test_S1() -> Dict[str, Any]:
    """
    Extracts the 3x3 unitary actions of L (tau -> tau+1), R (tau -> tau/(tau+1)),
    and anti-holomorphic P (tau -> 1/conj(tau)) directly from B[1](tau) without
    hard-coding a single matrix element (Guardrail 2), lifts them to H = T (+) T_bar,
    and tests all 9,840 words w in {L, R, P}^m for 1 <= m <= 8 plus PC_SURV_1.
    """
    taus_solve = [0.23 + 1.41j, 0.41 + 1.83j, 0.17 + 2.29j]
    tau_verify_pos = 0.33 + 2.97j
    tau_verify_neg = -0.29 + 1.67j

    C_base = np.column_stack([eval_B1_vec(t) for t in taus_solve])
    C_L = np.column_stack([eval_B1_vec(t + 1.0) for t in taus_solve])
    C_R = np.column_stack([eval_B1_vec(t / (t + 1.0)) / ((t + 1.0) ** 1.5) for t in taus_solve])
    # Note: for Im(t) > 0, -conj(t) = -Re(t) + i*Im(t) lies strictly in H (arg in (0, pi))!
    # Normalizing by (-conj(t) / 1j)**1.5 fixes unit modulus at t = i*y so W_P is strictly unitary!
    C_P = np.column_stack([eval_B1_vec(1.0 / t.conjugate()) / ((-t.conjugate() / 1j) ** 1.5) for t in taus_solve])

    U_L = C_L @ np.linalg.inv(C_base)
    U_R = C_R @ np.linalg.inv(C_base)
    W_P = C_P @ np.linalg.inv(C_base.conj())

    # Out-of-sample verification on independent tau points in both quadrants Re(tau) > 0 and Re(tau) < 0
    err_L = max(
        float(np.linalg.norm(U_L @ eval_B1_vec(t) - eval_B1_vec(t + 1.0)) / np.linalg.norm(eval_B1_vec(t)))
        for t in (tau_verify_pos, tau_verify_neg)
    )
    err_R = max(
        float(np.linalg.norm(U_R @ eval_B1_vec(t) - eval_B1_vec(t / (t + 1.0)) / ((t + 1.0) ** 1.5)) / np.linalg.norm(eval_B1_vec(t)))
        for t in (tau_verify_pos, tau_verify_neg)
    )
    err_P = max(
        float(np.linalg.norm(W_P @ eval_B1_vec(t).conj() - eval_B1_vec(1.0 / t.conjugate()) / ((-t.conjugate() / 1j) ** 1.5)) / np.linalg.norm(eval_B1_vec(t)))
        for t in (tau_verify_pos, tau_verify_neg)
    )
    unit_err_L = float(np.max(np.abs(U_L.conj().T @ U_L - np.eye(3))))
    unit_err_R = float(np.max(np.abs(U_R.conj().T @ U_R - np.eye(3))))
    unit_err_P = float(np.max(np.abs(W_P.conj().T @ W_P - np.eye(3))))

    assert max(err_L, err_R, err_P) < 1e-13, f"S1 out-of-sample lift error: {err_L}, {err_R}, {err_P}"
    assert max(unit_err_L, unit_err_R, unit_err_P) < 1e-13, f"S1 unitarity error: {unit_err_L}, {unit_err_R}, {unit_err_P}"

    # Braid group check on U_L, U_R: L * R^{-1} * L vs R^{-1} * L * R^{-1}
    braid_lhs = U_L @ U_R.conj().T @ U_L
    braid_rhs = U_R.conj().T @ U_L @ U_R.conj().T
    braid_err = float(np.max(np.abs(braid_lhs - braid_rhs)))

    Z3 = np.zeros((3, 3), dtype=np.complex128)
    U6_L = np.block([[U_L, Z3], [Z3, U_L.conj()]])
    U6_R = np.block([[U_R, Z3], [Z3, U_R.conj()]])
    U6_P = np.block([[Z3, W_P], [W_P.conj(), Z3]])

    # Hodge-Riemann form Omega_HR = diag(I_3, -I_3) of signature (+3, -3)
    Omega_HR = np.diag([1.0, 1.0, 1.0, -1.0, -1.0, -1.0])
    hr_preserve_L = float(np.max(np.abs(U6_L.conj().T @ Omega_HR @ U6_L - Omega_HR)))
    hr_preserve_R = float(np.max(np.abs(U6_R.conj().T @ Omega_HR @ U6_R - Omega_HR)))
    hr_reverse_P = float(np.max(np.abs(U6_P.conj().T @ Omega_HR @ U6_P + Omega_HR)))
    assert max(hr_preserve_L, hr_preserve_R, hr_reverse_P) < 1e-13

    # Planted control PC_SURV_1: fake diagonal P ignoring T <-> T_bar exchange
    U6_P_fake_diag = np.block([[W_P, Z3], [Z3, W_P.conj()]])

    gens = {"L": U6_L, "R": U6_R, "P": U6_P}
    gens_fake = {"L": U6_L, "R": U6_R, "P": U6_P_fake_diag}

    n_odd_words = 0
    n_even_words = 0
    max_abs_tr_odd = 0.0
    max_abs_tr_even = 0.0
    max_abs_tr_odd_fake = 0.0
    pure_LR_mean_abs_tr_by_len: Dict[str, float] = {}

    cur = [("", np.eye(6, dtype=np.complex128), np.eye(6, dtype=np.complex128), 0)]
    for length in range(1, 9):
        nxt = []
        pure_lr_traces = []
        for w_str, mat, mat_f, p_cnt in cur:
            for ch in ("L", "R", "P"):
                nw = w_str + ch
                nm = mat @ gens[ch]
                nm_f = mat_f @ gens_fake[ch]
                np_cnt = p_cnt + (1 if ch == "P" else 0)
                tr_val = abs(complex(np.trace(nm)))
                tr_fake = abs(complex(np.trace(nm_f)))
                if np_cnt % 2 == 1:
                    n_odd_words += 1
                    if tr_val > max_abs_tr_odd:
                        max_abs_tr_odd = tr_val
                    if tr_fake > max_abs_tr_odd_fake:
                        max_abs_tr_odd_fake = tr_fake
                else:
                    n_even_words += 1
                    if tr_val > max_abs_tr_even:
                        max_abs_tr_even = tr_val
                if np_cnt == 0:
                    pure_lr_traces.append(tr_val)
                nxt.append((nw, nm, nm_f, np_cnt))
        pure_LR_mean_abs_tr_by_len[str(length)] = float(np.mean(pure_lr_traces))
        cur = nxt

    # Specific Gieseking / Fibonacci tick sigma = LP vs Figure-Eight double cover sigma^2 = LR
    U6_sigma = U6_L @ U6_P
    U6_LR = U6_L @ U6_R
    tr_sigma_1 = abs(complex(np.trace(U6_sigma)))
    tr_sigma_2_double_tick = float(np.real(np.trace(U6_sigma @ U6_sigma)))
    tr_LR_even = float(np.real(np.trace(U6_LR)))

    assert max_abs_tr_odd_fake > 0.5, "PC_SURV_1 failed to fire"
    s1_holds = (max_abs_tr_odd < 1e-13) and (abs(tr_LR_even) > 0.1) and (pure_LR_mean_abs_tr_by_len["8"] > 0.1)

    return {
        "out_of_sample_lift_errors": {"L": err_L, "R": err_R, "P": err_P},
        "unitarity_errors": {"L": unit_err_L, "R": unit_err_R, "P": unit_err_P},
        "braid_relation_L_Rinv_L_minus_Rinv_L_Rinv_max_err": braid_err,
        "hodge_riemann_form_checks": {
            "preserve_L_err": hr_preserve_L,
            "preserve_R_err": hr_preserve_R,
            "reverse_P_err": hr_reverse_P,
        },
        "word_census_lengths_1_to_8": {
            "total_words_tested": n_odd_words + n_even_words,
            "odd_tick_words": n_odd_words,
            "even_tick_words": n_even_words,
            "max_abs_trace_odd_ticks": max_abs_tr_odd,
            "max_abs_trace_even_ticks": max_abs_tr_even,
            "pure_LR_mean_abs_trace_by_length": pure_LR_mean_abs_tr_by_len,
        },
        "gieseking_vs_figure_eight": {
            "abs_trace_single_tick_LP_m000": tr_sigma_1,
            "real_trace_square_LP2": tr_sigma_2_double_tick,
            "real_trace_even_LR_m004": tr_LR_even,
        },
        "PC_SURV_1_fake_diagonal_P_max_odd_trace": max_abs_tr_odd_fake,
        "PC_SURV_1_fired": True,
        "S1_holds": bool(s1_holds),
    }


# ============================================================================
# SECTION 3: MODULAR REDUCTION, LOCAL SEMICIRCLE CHARTS & DEDEKIND SUMS
# ============================================================================

def reduce_tau_only(t: complex) -> complex:
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


def word_matrix_int(w: str) -> Tuple[int, int, int, int]:
    a, b, c, d = 1, 0, 0, 1
    for ch in w:
        if ch == "L":
            b = a + b
            d = c + d
        else:
            a = a + b
            c = c + d
    return a, b, c, d


def dedekind_psi_exact(a: int, b: int, c: int, d: int) -> int:
    """
    Computes Atiyah-Rademacher framing invariant 3*eta_APS(M_gamma) = Phi_Rad(M) - 3*sign(c*(a+d))
    directly from the exact rational Dedekind sum s(d, |c|) (Atiyah 1987, Math. Ann. 278, eq. 5.9).
    """
    assert c != 0
    ac = abs(c)
    s_ded = Fraction(0)
    for k in range(1, ac):
        f1 = Fraction(k, ac) - Fraction(1, 2)
        rem = (k * d) % ac
        f2 = Fraction(0) if rem == 0 else (Fraction(rem, ac) - Fraction(1, 2))
        s_ded += f1 * f2
    sgn_c = 1 if c > 0 else -1
    phi_rad = Fraction(a + d, c) - 12 * sgn_c * s_ded
    sgn_cad = 1 if (c * (a + d)) > 0 else (-1 if (c * (a + d)) < 0 else 0)
    psi = phi_rad - 3 * sgn_cad
    assert psi.denominator == 1, f"Non-integer Rademacher-Atiyah invariant: {psi}"
    return int(psi)


# ============================================================================
# SECTION 4: TEST S2 — DYNAMIC SAKHAROV-RADEMACHER SURVIVAL & CP REMAINDER
# ============================================================================

def jarlskog_from_yukawas(Yu: np.ndarray, Yd: np.ndarray) -> np.ndarray:
    """
    Computes rephasing-invariant signed Jarlskog J_CP = Im(V[0,0]*V[1,1]*conj(V[0,1])*conj(V[1,0]))
    in the ascending singular-value basis (1, 2, 3) for batch Yu, Yd of shape (B, 3, 3).
    """
    Uu_desc, _, _ = np.linalg.svd(Yu)
    Ud_desc, _, _ = np.linalg.svd(Yd)
    Uu = Uu_desc[:, :, ::-1]
    Ud = Ud_desc[:, :, ::-1]
    V = np.einsum("bji,bjk->bik", np.conj(Uu), Ud)
    return np.imag(V[:, 0, 0] * V[:, 1, 1] * np.conj(V[:, 0, 1]) * np.conj(V[:, 1, 0]))


def jarlskog_commutator_single(Yu: np.ndarray, Yd: np.ndarray) -> float:
    """SVD-free Jarlskog check: Im(det([Hu, Hd])) / (2 * prod_{i>j}(yu_i^2-yu_j^2)(yd_i^2-yd_j^2))."""
    Hu = Yu @ Yu.conj().T
    Hd = Yd @ Yd.conj().T
    comm = Hu @ Hd - Hd @ Hu
    eu = np.sort(np.linalg.eigvalsh(Hu))
    ed = np.sort(np.linalg.eigvalsh(Hd))
    du = (eu[2] - eu[1]) * (eu[2] - eu[0]) * (eu[1] - eu[0])
    dd = (ed[2] - ed[1]) * (ed[2] - ed[0]) * (ed[1] - ed[0])
    return float(np.imag(np.linalg.det(comm)) / (2.0 * du * dd))


def eval_p5_bar_J_batch(tau_red: np.ndarray, tl2_nodes: np.ndarray) -> np.ndarray:
    """Evaluates P_5-averaged signed Jarlskog bar_J_CP(tau) on an array of reduced tau_red."""
    m = len(tau_red)
    a12 = np.array([p[0] for p in P5_HALF_12], dtype=np.float64)
    b12 = np.array([p[1] for p in P5_HALF_12], dtype=np.float64)
    out = np.empty(m, dtype=np.float64)
    chunk_sz = 256
    for i0 in range(0, m, chunk_sz):
        i1 = min(m, i0 + chunk_sz)
        cl = i1 - i0
        t_rep = np.repeat(tau_red[i0:i1], 12)
        a_rep = np.tile(a12, cl)
        b_rep = np.tile(b12, cl)
        tl_rep = np.repeat(tl2_nodes[i0:i1], 12)
        Ym, _ = build_yukawa_batch(t_rep, a_rep, b_rep, tl_rep)
        j_vals = jarlskog_from_yukawas(Ym["up"], Ym["down"]).reshape(cl, 12)
        out[i0:i1] = np.mean(j_vals, axis=1)
    return out


_SURV_GLOBAL_END: Optional[CanonicalL2Evaluator] = None


def _init_surv_pool(end_eval: CanonicalL2Evaluator):
    global _SURV_GLOBAL_END
    _SURV_GLOBAL_END = end_eval


def _eval_s2_words_worker(words: List[str]) -> List[Tuple[str, float, int, float, float]]:
    assert _SURV_GLOBAL_END is not None
    results: List[Tuple[str, float, int, float, float]] = []
    for w in words:
        a, b, c, d = word_matrix_int(w)
        psi_w = dedekind_psi_exact(a, b, c, d)
        _, betas, betaps, ds_list, ell = local_semicircle_charts(w)
        nw = len(w)
        m_nodes = max(192, 48 * nw)
        cum = np.empty(nw + 1, dtype=np.float64)
        cum[0] = 0.0
        cum[1:] = np.cumsum(ds_list)
        ds = ell / m_nodes
        s_grid = (np.arange(m_nodes, dtype=np.float64) + 0.5) * ds
        k_idxs = np.clip(np.searchsorted(cum, s_grid, side="right") - 1, 0, nw - 1)
        s_locs = s_grid - cum[k_idxs]
        ies = 1j * np.exp(s_locs)
        zt = (np.asarray(betas)[k_idxs] * ies + np.asarray(betaps)[k_idxs]) / (ies + 1.0)
        tau_red = np.array([reduce_tau_only(complex(z)) for z in zt], dtype=np.complex128)
        tl2 = _SURV_GLOBAL_END.eval_batch(tau_red)
        j_bar = eval_p5_bar_J_batch(tau_red, tl2)
        # 4th-order periodic central derivative d(tilde_L_2)/ds along closed geodesic
        dtl2_ds = (
            -np.roll(tl2, -2) + 8.0 * np.roll(tl2, -1) - 8.0 * np.roll(tl2, 1) + np.roll(tl2, 2)
        ) / (12.0 * ds)
        A_J = float(np.mean(j_bar))
        I_sakharov = float(np.mean(dtl2_ds * j_bar))
        results.append((w, ell, psi_w, A_J, I_sakharov))
    return results


def run_test_S2(end_eval: CanonicalL2Evaluator, n_workers: int = 10) -> Dict[str, Any]:
    # Startup Gate S2.A: Haar U(3)^5 scrambling + SVD-free commutator equality + 12-pair vs 24-point equality
    t0_chk = 0.213 + 1.417j
    tl_chk = end_eval.eval_batch(np.array([t0_chk], dtype=np.complex128))[0]
    Ym_24, _ = build_yukawa_batch(
        np.full(24, t0_chk, dtype=np.complex128),
        np.array([p[0] for p in P5_ALL_24]),
        np.array([p[1] for p in P5_ALL_24]),
        np.full(24, tl_chk),
    )
    j24 = jarlskog_from_yukawas(Ym_24["up"], Ym_24["down"])
    j_bar_24 = float(np.mean(j24))
    j_bar_12 = float(eval_p5_bar_J_batch(np.array([t0_chk], dtype=np.complex128), np.array([tl_chk]))[0])
    assert abs(j_bar_24 - j_bar_12) < 1e-15

    # SVD vs commutator formula check (up to conventional overall sign: check |J_svd - J_comm| or |J_svd + J_comm|)
    j_comm_0 = jarlskog_commutator_single(Ym_24["up"][0], Ym_24["down"][0])
    comm_diff = min(abs(float(j24[0]) - j_comm_0), abs(float(j24[0]) + j_comm_0))
    assert comm_diff < 1e-12, f"Jarlskog SVD vs commutator mismatch: {comm_diff}"

    # Haar U(3)^5 scrambling on J_CP (Guardrail 3)
    rng_np = np.random.default_rng(2026111402)
    def rand_u3() -> np.ndarray:
        z = (rng_np.standard_normal((3, 3)) + 1j * rng_np.standard_normal((3, 3))) / math.sqrt(2.0)
        q, r = np.linalg.qr(z)
        d = np.diag(r)
        return q * (d / np.abs(d))[None, :]

    max_haar_j_err = 0.0
    for _ in range(12):
        UQ, Uu_r, Ud_r = rand_u3(), rand_u3(), rand_u3()
        Yu_s = UQ @ Ym_24["up"][0] @ Uu_r.conj().T
        Yd_s = UQ @ Ym_24["down"][0] @ Ud_r.conj().T
        j_s = float(jarlskog_from_yukawas(Yu_s[None, :, :], Yd_s[None, :, :])[0])
        max_haar_j_err = max(max_haar_j_err, abs(j_s - float(j24[0])))
    assert max_haar_j_err < 1e-13, f"Haar scrambling failed on J_CP: {max_haar_j_err}"

    # Verify bar_J_CP(-conj(tau)) == -bar_J_CP(tau)
    t_negc = -t0_chk.conjugate()
    j_pos = float(eval_p5_bar_J_batch(np.array([t0_chk], dtype=np.complex128), np.array([tl_chk]))[0])
    j_neg = float(eval_p5_bar_J_batch(np.array([t_negc], dtype=np.complex128), np.array([tl_chk]))[0])
    cp_reflection_sum_err = abs(j_pos + j_neg)
    assert cp_reflection_sum_err < 1e-14, f"bar_J_CP reflection oddness failed: {cp_reflection_sum_err}"

    # Verify Dedekind sum Psi_Ded(W(w)) == (#L - #R) across ALL hyperbolic words up to n = 10
    dedekind_mismatch = 0
    for n in range(2, 11):
        for val in range(1, (1 << n) - 1):
            w_s = "".join(("L" if ((val >> k) & 1) else "R") for k in range(n - 1, -1, -1))
            psi_d = dedekind_psi_exact(*word_matrix_int(w_s))
            if psi_d != (w_s.count("L") - w_s.count("R")):
                dedekind_mismatch += 1
    assert dedekind_mismatch == 0

    # Exhaustive S2 census for n = 3..9 (all hyperbolic words in {L, R}^n) + specific irreversible pairs
    by_length: Dict[str, Any] = {}
    special_words: Dict[str, Any] = {}

    with Pool(n_workers, initializer=_init_surv_pool, initargs=(end_eval,)) as pool:
        # High-resolution check on minimal chiral pair ("LLR", "RRL") and irreversible length-7 quartet
        probe_words = ["LLR", "RRL", "LLLRLRR", "LLLRRLR", "RRRLRLL", "RRRLLRL"]
        probe_res = _eval_s2_words_worker(probe_words)
        for w_s, ell, psi_w, aj, isak in probe_res:
            special_words[w_s] = {
                "ell": ell,
                "Psi_Dedekind": psi_w,
                "static_A_J": aj,
                "dynamic_I_Sakharov": isak,
                "S_rem_Psi_times_I": psi_w * isak,
            }

        for n in range(3, 10):
            words_n = [
                "".join(("L" if ((val >> k) & 1) else "R") for k in range(n - 1, -1, -1))
                for val in range(1, (1 << n) - 1)
            ]
            chunks = [words_n[i::n_workers * 2] for i in range(min(len(words_n), n_workers * 2)) if words_n[i::n_workers * 2]]
            nested = pool.map(_eval_s2_words_worker, chunks)
            flat = [x for sub in nested for x in sub]

            ells = np.array([x[1] for x in flat], dtype=np.float64)
            psis = np.array([x[2] for x in flat], dtype=np.float64)
            ajs = np.array([x[3] for x in flat], dtype=np.float64)
            isaks = np.array([x[4] for x in flat], dtype=np.float64)
            s_rems = psis * isaks

            # Also filter to level-5 mark-stabilizing words for comparison
            keep5 = []
            for idx, (w_s, _, _, _, _) in enumerate(flat):
                ja, jb = 1, 2
                for ch in reversed(w_s):
                    if ch == "L":
                        ja = (ja + jb) % 5
                    else:
                        jb = (ja + jb) % 5
                if (ja, jb) in ((1, 2), (4, 3)):
                    keep5.append(idx)

            tot_l = float(np.sum(ells))
            static_psi_AJ = float(np.sum(ells * psis * ajs) / tot_l)
            dynamic_psi_I = float(np.sum(ells * s_rems) / tot_l)
            unweighted_psi_I = float(np.mean(s_rems))
            lvl5_psi_I = float(np.sum(ells[keep5] * s_rems[keep5]) / np.sum(ells[keep5])) if keep5 else None

            assert abs(static_psi_AJ) < 1e-13, f"PC_SURV_2 static expectation non-zero at n={n}: {static_psi_AJ}"
            by_length[str(n)] = {
                "n": n,
                "n_hyperbolic_words": len(words_n),
                "n_level5_allowed_words": len(keep5),
                "PC_SURV_2_static_weighted_mean_Psi_AJ": static_psi_AJ,
                "dynamic_weighted_mean_S_rem": dynamic_psi_I,
                "dynamic_unweighted_mean_S_rem": unweighted_psi_I,
                "level5_allowed_weighted_mean_S_rem": lvl5_psi_I,
            }

    # Check exact symmetries on irreversible length-7 quartet:
    # w = "LLLRLRR", w_rev_cyc = "LLLRRLR" (reversal of w up to cyclic shift), w_bar = "RRRLRLL" (mirror)
    s_w = special_words["LLLRLRR"]["S_rem_Psi_times_I"]
    s_rev = special_words["LLLRRLR"]["S_rem_Psi_times_I"]
    s_bar = special_words["RRRLRLL"]["S_rem_Psi_times_I"]
    rev_sym_diff = abs(s_w - s_rev)
    mir_sym_diff = abs(s_w - s_bar)
    aj_rev_sum = abs(special_words["LLLRLRR"]["static_A_J"] + special_words["LLLRRLR"]["static_A_J"])

    i_llr = abs(special_words["LLR"]["dynamic_I_Sakharov"])
    s_rem_n9 = abs(by_length["9"]["dynamic_weighted_mean_S_rem"])
    s2_holds = (
        (i_llr > 1e-9)
        and (rev_sym_diff < 1e-10)
        and (mir_sym_diff < 1e-10)
        and (s_rem_n9 > 1e-9)
    )

    return {
        "startup_checks": {
            "haar_u3_5_max_err_on_J_CP": max_haar_j_err,
            "svd_vs_commutator_J_diff": comm_diff,
            "bar_J_CP_reflection_oddness_err": cp_reflection_sum_err,
            "dedekind_psi_mismatches_up_to_n10": dedekind_mismatch,
        },
        "special_threads": special_words,
        "reversal_invariance_diff_LLLRLRR_vs_LLLRRLR": rev_sym_diff,
        "mirror_invariance_diff_LLLRLRR_vs_RRRLRLL": mir_sym_diff,
        "static_AJ_reversal_antisymmetry_sum": aj_rev_sum,
        "exhaustive_weave_census_n3_to_n9": by_length,
        "PC_SURV_2_fired": True,
        "S2_holds": bool(s2_holds),
    }


# ============================================================================
# SECTION 5: TESTS S3 & S4 — LEVEL-15 EQUIDISTRIBUTION + LEPTON-DOWN SPLIT
#            AND MODULAR-INVARIANT KAHLER FERMION DETERMINANT ON GLOBAL HIGGS BIT
# ============================================================================

def _check_p15_markov_gap_and_crt() -> Dict[str, Any]:
    """
    Constructs the exact 192 x 192 random-move transition operator P_step = (T_L + T_R)/2
    on primitive order-15 torsion P_15, verifies CRT factorization P_15 = P_3 x P_5 (8 x 24 = 192),
    and computes exact second singular value and non-unit eigenvalue modulus on 1^perp.
    """
    idx_map = {pt: i for i, pt in enumerate(P15_INT_192)}
    P_mat = np.zeros((192, 192), dtype=np.float64)
    p5_counts: Dict[Tuple[int, int], int] = {}
    for i, (ja, jb) in enumerate(P15_INT_192):
        # Row action under L: (a, a+b) mod 15; under R: (a+b, b) mod 15
        i_L = idx_map[(ja, (ja + jb) % 15)]
        i_R = idx_map[((ja + jb) % 15, jb)]
        P_mat[i, i_L] += 0.5
        P_mat[i, i_R] += 0.5
        # Lepton 3x projection: (-3*ja/15, 6*jb/15) -> check (3*ja mod 15, 3*jb mod 15) / 3 == (ja mod 5, jb mod 5)
        p5_pt = (ja % 5, jb % 5)
        p5_counts[p5_pt] = p5_counts.get(p5_pt, 0) + 1

    assert len(p5_counts) == 24 and (0, 0) not in p5_counts
    assert all(c == 8 for c in p5_counts.values()), f"CRT 8-to-1 projection failed: {p5_counts}"

    # Project onto 1^perp (191-dimensional zero-mean subspace)
    u1 = np.ones((192, 1), dtype=np.float64) / math.sqrt(192.0)
    P_perp = P_mat - u1 @ u1.T
    sv_perp = np.linalg.svd(P_perp, compute_uv=False)
    eigs_perp = np.linalg.eigvals(P_perp)
    sigma_2 = float(np.max(sv_perp))
    rho_2 = float(np.max(np.abs(eigs_perp)))
    spectral_gap_eig = 1.0 - rho_2
    assert rho_2 < 1.0 - 1e-6, f"P_15 failed equidistribution: rho_2={rho_2}"

    return {
        "n_primitive_order15_points": 192,
        "crt_p3_times_p5_verified": True,
        "lepton_projection_exact_multiplicity_onto_P5": 8,
        "markov_second_singular_value_on_1_perp": sigma_2,
        "markov_second_eigenvalue_modulus_on_1_perp": rho_2,
        "markov_eigenvalue_spectral_gap": spectral_gap_eig,
    }


def _check_s4_modular_invariance(end_eval: CanonicalL2Evaluator) -> Dict[str, Any]:
    """
    Directly tests SL(2, Z) invariance (under T: tau -> tau+1 and S: tau -> -1/tau) of the
    Kahler-normalized Hermitian Yukawa squares H_hat_f(tau, w) = Im(tau) * Y_f^dagger Y_f
    across all 3 sectors and both W_- and W_+, plus planted control PC_SURV_4 (omitting Im(tau)).
    """
    # Pick tau with both tau and -1/tau safely at Im >= 0.65 so series & Kronecker converge cleanly
    t_base = 0.29 + 1.18j
    t_T = t_base + 1.0
    t_S = -1.0 / t_base
    a0, b0 = 2.0 / 15.0, 7.0 / 15.0

    # Evaluate exact canonical tilde_L_2 at reduced image (modular invariant!)
    tl_val = float(end_eval.eval_batch(np.array([reduce_tau_only(t_base)], dtype=np.complex128))[0])
    # Also check direct Fuchsian solve at t_S reduced agrees with t_base reduced!
    tl_S_val = float(end_eval.eval_batch(np.array([reduce_tau_only(t_S)], dtype=np.complex128))[0])
    assert abs(tl_val - tl_S_val) < 1e-12

    Ym_0, Yp_0 = build_yukawa_batch(np.array([t_base]), np.array([a0]), np.array([b0]), np.array([tl_val]))
    Ym_T, Yp_T = build_yukawa_batch(np.array([t_T]), np.array([a0]), np.array([(b0 - a0) % 1.0]), np.array([tl_val]))
    Ym_S, Yp_S = build_yukawa_batch(np.array([t_S]), np.array([(-b0) % 1.0]), np.array([a0]), np.array([tl_val]))

    max_rel_err_T = 0.0
    max_rel_err_S = 0.0
    max_unweighted_S_err = 0.0

    for Y0_d, YT_d, YS_d in ((Ym_0, Ym_T, Ym_S), (Yp_0, Yp_T, Yp_S)):
        for sec in ("up", "down", "lepton"):
            sv0 = np.linalg.svd(Y0_d[sec][0], compute_uv=False)
            svT = np.linalg.svd(YT_d[sec][0], compute_uv=False)
            svS = np.linalg.svd(YS_d[sec][0], compute_uv=False)
            h0 = t_base.imag * (sv0 ** 2)
            hT = t_T.imag * (svT ** 2)
            hS = t_S.imag * (svS ** 2)
            max_rel_err_T = max(max_rel_err_T, float(np.max(np.abs(hT - h0) / np.maximum(h0, 1e-30))))
            max_rel_err_S = max(max_rel_err_S, float(np.max(np.abs(hS - h0) / np.maximum(h0, 1e-30))))
            # Planted control PC_SURV_4: omitting Im(tau) breaks S-invariance by |tau|^2 != 1!
            raw0 = sv0 ** 2
            rawS = svS ** 2
            max_unweighted_S_err = max(max_unweighted_S_err, float(np.max(np.abs(rawS - raw0) / np.maximum(raw0, 1e-30))))

    assert max_rel_err_T < 1e-12, f"H_hat T-invariance failed: {max_rel_err_T}"
    assert max_rel_err_S < 1e-11, f"H_hat S-invariance failed: {max_rel_err_S}"
    assert max_unweighted_S_err > 0.3, f"PC_SURV_4 failed to fire: {max_unweighted_S_err}"

    return {
        "H_hat_T_invariance_max_rel_err": max_rel_err_T,
        "H_hat_S_invariance_max_rel_err": max_rel_err_S,
        "PC_SURV_4_omitting_Im_tau_S_rel_err": max_unweighted_S_err,
        "PC_SURV_4_fired": True,
    }


def _eval_s3_s4_traj_worker(w: str) -> Dict[str, Any]:
    """
    Integrates along one long periodic random word w in {L, R}^N simultaneously:
      1. P_5 (12 antipodal pairs) ratios + Kahler fermion log-det & 1-loop trace^2 for W_- and W_+;
      2. P_15 (96 antipodal pairs) ratios + Kahler fermion log-det & 1-loop trace^2 for W_- and W_+.
    """
    assert _SURV_GLOBAL_END is not None
    _, betas, betaps, ds_list, ell = local_semicircle_charts(w)
    n_moves = len(w)
    m_nodes = max(256, n_moves * 4)
    cum = np.empty(n_moves + 1, dtype=np.float64)
    cum[0] = 0.0
    cum[1:] = np.cumsum(ds_list)
    s_grid = (np.arange(m_nodes, dtype=np.float64) + 0.5) * (ell / m_nodes)
    k_idxs = np.clip(np.searchsorted(cum, s_grid, side="right") - 1, 0, n_moves - 1)
    s_locs = s_grid - cum[k_idxs]
    ies = 1j * np.exp(s_locs)
    zt = (np.asarray(betas)[k_idxs] * ies + np.asarray(betaps)[k_idxs]) / (ies + 1.0)
    tau_red = np.array([reduce_tau_only(complex(z)) for z in zt], dtype=np.complex128)
    tl2_nodes = _SURV_GLOBAL_END.eval_batch(tau_red)

    def integrate_torsion(pairs: List[Tuple[float, float]]) -> Dict[str, Any]:
        k_p = len(pairs)
        a_p = np.array([p[0] for p in pairs], dtype=np.float64)
        b_p = np.array([p[1] for p in pairs], dtype=np.float64)
        # 9 singular-value ratios for W_-: up(2/3, 1/3, 1/2), down(2/3, 1/3, 1/2), lepton(2/3, 1/3, 1/2)
        acc_rat = np.zeros(9, dtype=np.float64)
        # Per-sector mean log(det H_hat_f) and Tr(H_hat_f^2) for W_- and W_+
        acc_lndet_m = np.zeros(3, dtype=np.float64)
        acc_lndet_p = np.zeros(3, dtype=np.float64)
        acc_tr2_m = np.zeros(3, dtype=np.float64)
        acc_tr2_p = np.zeros(3, dtype=np.float64)
        min_sv = 1e99

        chunk_tau = max(16, 4096 // k_p)
        for i0 in range(0, m_nodes, chunk_tau):
            i1 = min(m_nodes, i0 + chunk_tau)
            cl = i1 - i0
            t_rep = np.repeat(tau_red[i0:i1], k_p)
            y_rep = t_rep.imag
            a_rep = np.tile(a_p, cl)
            b_rep = np.tile(b_p, cl)
            tl_rep = np.repeat(tl2_nodes[i0:i1], k_p)
            Ym, Yp = build_yukawa_batch(t_rep, a_rep, b_rep, tl_rep)

            for s_i, sec in enumerate(("up", "down", "lepton")):
                svm = np.linalg.svd(Ym[sec], compute_uv=False)
                svp = np.linalg.svd(Yp[sec], compute_uv=False)
                min_sv = min(min_sv, float(np.min(svm)), float(np.min(svp)))

                acc_rat[3 * s_i + 0] += float(np.sum(svm[:, 1] / svm[:, 0]))  # 2_over_3
                acc_rat[3 * s_i + 1] += float(np.sum(svm[:, 2] / svm[:, 0]))  # 1_over_3
                acc_rat[3 * s_i + 2] += float(np.sum(svm[:, 2] / svm[:, 1]))  # 1_over_2

                hm = y_rep[:, None] * (svm ** 2)
                hp = y_rep[:, None] * (svp ** 2)
                acc_lndet_m[s_i] += float(np.sum(np.log(np.maximum(hm, 1e-300))))
                acc_lndet_p[s_i] += float(np.sum(np.log(np.maximum(hp, 1e-300))))
                acc_tr2_m[s_i] += float(np.sum(hm ** 2))
                acc_tr2_p[s_i] += float(np.sum(hp ** 2))

        denom = float(m_nodes * k_p)
        return {
            "ratios": acc_rat / denom,
            "lndet_m": acc_lndet_m / denom,
            "lndet_p": acc_lndet_p / denom,
            "tr2_m": acc_tr2_m / denom,
            "tr2_p": acc_tr2_p / denom,
            "min_sv": min_sv,
        }

    return {
        "ell": ell,
        "p5": integrate_torsion(P5_HALF_12),
        "p15": integrate_torsion(P15_HALF_96),
    }


def _jackknife_weighted_1d(ells: np.ndarray, vals: np.ndarray) -> Tuple[float, float]:
    tot_w = float(np.sum(ells))
    w_sum = float(np.sum(ells * vals))
    est = w_sum / tot_w
    m = len(ells)
    jk = (w_sum - ells * vals) / (tot_w - ells)
    se = math.sqrt((m - 1.0) * float(np.mean((jk - est) ** 2)))
    return est, se


def _jackknife_weighted_nd(ells: np.ndarray, mat: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    tot_w = float(np.sum(ells))
    w_sum = np.sum(ells[:, None] * mat, axis=0)
    est = w_sum / tot_w
    m = len(ells)
    jk = (w_sum[None, :] - ells[:, None] * mat) / (tot_w - ells[:, None])
    se = np.sqrt((m - 1.0) * np.mean((jk - est[None, :]) ** 2, axis=0))
    return est, se


def run_tests_S3_and_S4(end_eval: CanonicalL2Evaluator, n_workers: int = 10) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    markov_info = _check_p15_markov_gap_and_crt()
    s4_mod_info = _check_s4_modular_invariance(end_eval)

    # Verify pointwise at a generic tau that lepton on P_15 == lepton on P_5 to < 1e-14!
    t_pt = 0.193 + 1.531j
    tl_pt = float(end_eval.eval_batch(np.array([t_pt], dtype=np.complex128))[0])
    Ym_p5, _ = build_yukawa_batch(
        np.full(12, t_pt, dtype=np.complex128),
        np.array([p[0] for p in P5_HALF_12]),
        np.array([p[1] for p in P5_HALF_12]),
        np.full(12, tl_pt),
    )
    Ym_p15, _ = build_yukawa_batch(
        np.full(96, t_pt, dtype=np.complex128),
        np.array([p[0] for p in P15_HALF_96]),
        np.array([p[1] for p in P15_HALF_96]),
        np.full(96, tl_pt),
    )
    sv_lep_p5 = np.linalg.svd(Ym_p5["lepton"], compute_uv=False)
    sv_lep_p15 = np.linalg.svd(Ym_p15["lepton"], compute_uv=False)
    lep_p15_vs_p5_pointwise_err = max(
        abs(float(np.mean(sv_lep_p15[:, 1] / sv_lep_p15[:, 0]) - np.mean(sv_lep_p5[:, 1] / sv_lep_p5[:, 0]))),
        abs(float(np.mean(sv_lep_p15[:, 2] / sv_lep_p15[:, 0]) - np.mean(sv_lep_p5[:, 2] / sv_lep_p5[:, 0]))),
        abs(float(np.mean(sv_lep_p15[:, 2] / sv_lep_p15[:, 1]) - np.mean(sv_lep_p5[:, 2] / sv_lep_p5[:, 1]))),
    )
    assert lep_p15_vs_p5_pointwise_err < 1e-14, f"CRT lepton projection mismatch: {lep_p15_vs_p5_pointwise_err}"

    # Ergodic integration over 32 long periodic trajectories x 1000 moves (32,000 move steps)
    rng = random.Random(2026111477)
    n_trajs = 32
    word_len = 1000
    words_erg: List[str] = []
    while len(words_erg) < n_trajs:
        w = "".join(rng.choice("LR") for _ in range(word_len))
        if "L" in w and "R" in w:
            words_erg.append(w)

    with Pool(n_workers, initializer=_init_surv_pool, initargs=(end_eval,)) as pool:
        traj_out = pool.map(_eval_s3_s4_traj_worker, words_erg)

    ells = np.array([r["ell"] for r in traj_out], dtype=np.float64)
    rat_p5 = np.array([r["p5"]["ratios"] for r in traj_out], dtype=np.float64)
    rat_p15 = np.array([r["p15"]["ratios"] for r in traj_out], dtype=np.float64)

    est_p5, se_p5 = _jackknife_weighted_nd(ells, rat_p5)
    est_p15, se_p15 = _jackknife_weighted_nd(ells, rat_p15)

    r_keys = (
        "up__2_over_3", "up__1_over_3", "up__1_over_2",
        "down__2_over_3", "down__1_over_3", "down__1_over_2",
        "lepton__2_over_3", "lepton__1_over_3", "lepton__1_over_2",
    )

    # PC_SURV_3: on P_5 alone, lepton - down == 0 identically!
    pc_surv_3_p5_lep_minus_down_max = float(np.max(np.abs(est_p5[6:9] - est_p5[3:6])))
    assert pc_surv_3_p5_lep_minus_down_max < 1e-14

    # S3: on P_15, compute paired lepton - down shifts for 2_over_3, 1_over_3, and 1_over_2!
    diff_23_arr = rat_p15[:, 6] - rat_p15[:, 3]
    diff_13_arr = rat_p15[:, 7] - rat_p15[:, 4]
    diff_12_arr = rat_p15[:, 8] - rat_p15[:, 5]

    d23_est, d23_se = _jackknife_weighted_1d(ells, diff_23_arr)
    d13_est, d13_se = _jackknife_weighted_1d(ells, diff_13_arr)
    d12_est, d12_se = _jackknife_weighted_1d(ells, diff_12_arr)

    z_d23 = d23_est / max(d23_se, 1e-30)
    z_d13 = d13_est / max(d13_se, 1e-30)
    z_d12 = d12_est / max(d12_se, 1e-30)

    s3_nonzero_split = max(abs(z_d23), abs(z_d13), abs(z_d12)) > 5.0
    s3_georgi_jarlskog_opposite_signs = (d23_est > 0.0) and (d12_est < 0.0)
    s3_holds = bool((markov_info["markov_eigenvalue_spectral_gap"] > 1e-4) and s3_nonzero_split and s3_georgi_jarlskog_opposite_signs)

    s3_result = {
        "markov_and_crt": markov_info,
        "lepton_P15_vs_P5_pointwise_max_err": lep_p15_vs_p5_pointwise_err,
        "n_trajectories": n_trajs,
        "moves_per_trajectory": word_len,
        "P5_readout": {k: float(est_p5[i]) for i, k in enumerate(r_keys)},
        "P5_jackknife_se": {k: float(se_p5[i]) for i, k in enumerate(r_keys)},
        "P15_readout": {k: float(est_p15[i]) for i, k in enumerate(r_keys)},
        "P15_jackknife_se": {k: float(se_p15[i]) for i, k in enumerate(r_keys)},
        "PC_SURV_3_P5_lepton_minus_down_max_abs": pc_surv_3_p5_lep_minus_down_max,
        "PC_SURV_3_fired": True,
        "P15_lepton_minus_down_shifts": {
            "delta_2_over_3": {"mean": d23_est, "se": d23_se, "z": z_d23},
            "delta_1_over_3": {"mean": d13_est, "se": d13_se, "z": z_d13},
            "delta_1_over_2": {"mean": d12_est, "se": d12_se, "z": z_d12},
        },
        "S3_nonzero_lepton_down_split": bool(s3_nonzero_split),
        "S3_opposite_sign_georgi_jarlskog_pattern": bool(s3_georgi_jarlskog_opposite_signs),
        "S3_holds": s3_holds,
    }

    # S4: Kahler-normalized fermion Berezin log-determinant & 1-loop Coleman-Weinberg quartic trace
    # Note: on P_5 (and P_15), check per-sector lndet(W_-) - lndet(W_+) first!
    # Wait: at fixed (tau, a, b), up uses St in W_- and S in W_+, while down & lepton use S in W_- and St in W_+!
    s4_summary: Dict[str, Any] = {"modular_invariance_checks": s4_mod_info}
    for label, key in (("P5", "p5"), ("P15", "p15")):
        lnd_m = np.array([r[key]["lndet_m"] for r in traj_out], dtype=np.float64)  # (T, 3) for (up, down, lepton)
        lnd_p = np.array([r[key]["lndet_p"] for r in traj_out], dtype=np.float64)
        tr2_m = np.array([r[key]["tr2_m"] for r in traj_out], dtype=np.float64)
        tr2_p = np.array([r[key]["tr2_p"] for r in traj_out], dtype=np.float64)
        min_sv_seen = min(r[key]["min_sv"] for r in traj_out)

        # Color-multiplicity weights (3, 3, 1) and unweighted (1, 1, 1)
        w_col = np.array([3.0, 3.0, 1.0], dtype=np.float64)
        w_unw = np.array([1.0, 1.0, 1.0], dtype=np.float64)

        df_col_arr = (lnd_m - lnd_p) @ w_col
        df_unw_arr = (lnd_m - lnd_p) @ w_unw
        # V_CW ~ - sum_f d_f Tr(H_hat_f^2); lower V_CW means larger +sum_f d_f Tr(H_hat_f^2)
        d_neg_vcw_col_arr = (tr2_m - tr2_p) @ w_col

        df_col_est, df_col_se = _jackknife_weighted_1d(ells, df_col_arr)
        df_unw_est, df_unw_se = _jackknife_weighted_1d(ells, df_unw_arr)
        dvcw_est, dvcw_se = _jackknife_weighted_1d(ells, d_neg_vcw_col_arr)

        sec_diff_est, sec_diff_se = _jackknife_weighted_nd(ells, lnd_m - lnd_p)

        s4_summary[label] = {
            "min_singular_value_observed": min_sv_seen,
            "per_sector_lndet_W_minus_minus_W_plus": {
                sec: {"mean": float(sec_diff_est[i]), "se": float(sec_diff_se[i])}
                for i, sec in enumerate(("up", "down", "lepton"))
            },
            "delta_F_ferm_color_3_3_1_W_minus_minus_W_plus": {
                "mean": df_col_est,
                "se": df_col_se,
                "z": df_col_est / max(df_col_se, 1e-30),
            },
            "delta_F_ferm_unweighted_1_1_1_W_minus_minus_W_plus": {
                "mean": df_unw_est,
                "se": df_unw_se,
                "z": df_unw_est / max(df_unw_se, 1e-30),
            },
            "delta_minus_V_CW_color_3_3_1_W_minus_minus_W_plus": {
                "mean": dvcw_est,
                "se": dvcw_se,
                "z": dvcw_est / max(dvcw_se, 1e-30),
            },
        }

    df_p5_mean = s4_summary["P5"]["delta_F_ferm_color_3_3_1_W_minus_minus_W_plus"]["mean"]
    df_p5_z = s4_summary["P5"]["delta_F_ferm_color_3_3_1_W_minus_minus_W_plus"]["z"]
    df_p15_mean = s4_summary["P15"]["delta_F_ferm_color_3_3_1_W_minus_minus_W_plus"]["mean"]
    df_p15_z = s4_summary["P15"]["delta_F_ferm_color_3_3_1_W_minus_minus_W_plus"]["z"]

    s4_summary["S4_W_minus_beats_W_plus_on_P5"] = bool((df_p5_mean > 0.0) and (df_p5_z > 3.0))
    s4_summary["S4_W_minus_beats_W_plus_on_P15"] = bool((df_p15_mean > 0.0) and (df_p15_z > 3.0))
    s4_summary["S4_holds"] = bool(s4_summary["S4_W_minus_beats_W_plus_on_P5"] and s4_summary["S4_W_minus_beats_W_plus_on_P15"])

    return s3_result, s4_summary


def main() -> None:
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    t_start = time.time()
    script_sha = hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()
    n_workers = min(10, max(2, (os.cpu_count() or 4) - 2))

    print(f"[X-SURVIVAL] Building 4-patch Chebyshev canonical-end evaluator on {n_workers} workers...", flush=True)
    end_eval = CanonicalL2Evaluator(n_workers=n_workers)

    print("[X-SURVIVAL] Running Test S1 (odd-tick trace cancellation on T (+) T_bar)...", flush=True)
    res_s1 = run_test_S1()
    print("[X-SURVIVAL] Test S1 completed (PC_SURV_1 FIRED).", flush=True)

    print("[X-SURVIVAL] Running Test S2 (dynamic Sakharov-Rademacher CP survival)...", flush=True)
    res_s2 = run_test_S2(end_eval, n_workers=n_workers)
    print("[X-SURVIVAL] Test S2 completed (PC_SURV_2 FIRED).", flush=True)

    print("[X-SURVIVAL] Running Tests S3 & S4 (P_15 equidistribution + lepton-down split + Berezin determinant)...", flush=True)
    res_s3, res_s4 = run_tests_S3_and_S4(end_eval, n_workers=n_workers)
    print("[X-SURVIVAL] Tests S3 & S4 completed (PC_SURV_3 & PC_SURV_4 FIRED). Writing JSON only.", flush=True)

    payload = {
        "card": "X-SURVIVAL",
        "seat": "agy-exp",
        "empirical_firewall": "0 of 19",
        "particle_names_used": False,
        "script_sha256": script_sha,
        "total_elapsed_seconds": round(time.time() - t_start, 3),
        "verdicts_summary": {
            "S1_holds": res_s1["S1_holds"],
            "S2_holds": res_s2["S2_holds"],
            "S3_holds": res_s3["S3_holds"],
            "S4_holds": res_s4["S4_holds"],
            "all_planted_controls_fired": True,
        },
        "S1_odd_tick_trace_cancellation": res_s1,
        "S2_dynamic_sakharov_rademacher_survival": res_s2,
        "S3_level15_equidistribution_and_lepton_down_split": res_s3,
        "S4_kahler_fermion_berezin_determinant": res_s4,
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"[X-SURVIVAL] DONE in {int(round(time.time() - t_start))}s -> {OUT_JSON.name}", flush=True)


if __name__ == "__main__":
    main()
