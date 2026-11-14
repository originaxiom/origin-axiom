#!/usr/bin/env python3
"""
Standalone Zero-Import Verifier for Card X-CANON (M22 on docs/seats/agy-exp.md):
Independent Computation of Frame C's Whole-Weave Read-Out with the Canonical
Length-2 Horocycle End (P-845, B1667, B1919, B1924, B1927, B1928).

Strict Guardrails & Firewall:
  - Zero imports from the repository (standard library, numpy, scipy.special, mpmath only).
  - Zero empirical / PDG / cosmological values ("0 of 19").
  - Outputs named strictly by (sector, index) positions; zero particle names.
  - All numerical readout values written exclusively to verify_x_canon_out.json;
    stdout prints structural progress, sample counts, and self-audit gate statuses only.
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
OUT_JSON = HERE / "verify_x_canon_out.json"

EULER_GAMMA = 0.57721566490153286060651209008240243104215933593992
NORM_CONST_SHIFT = EULER_GAMMA + math.log(math.pi)
NORM_CONST_2PI = -2.0 * math.pi * NORM_CONST_SHIFT


# ============================================================================
# SECTION 0: HIGH-PRECISION MPMATH + FAST FLOAT64 LAME UNIFORMIZERS (B1667/B1927)
# ============================================================================

def _wp_and_wp_prime_mp(z: mp.mpc, tau: mp.mpc, max_m: int = 120) -> Tuple[mp.mpc, mp.mpc]:
    k_sh = int(round(float(mp.im(z) / mp.im(tau))))
    if k_sh:
        z = z - k_sh * tau
    pi = mp.pi
    s0 = mp.sin(pi * z)
    c0 = mp.cos(pi * z)
    wp = (pi / s0) ** 2 - (pi ** 2) / 3
    wpp = -2 * (pi ** 3) * c0 / (s0 ** 3)
    for m in range(1, max_m + 1):
        zm_p = pi * (z + m * tau)
        zm_m = pi * (z - m * tau)
        m_t = pi * m * tau
        sp, cp = mp.sin(zm_p), mp.cos(zm_p)
        sm, cm = mp.sin(zm_m), mp.cos(zm_m)
        st = mp.sin(m_t)
        term_wp = (pi / sp) ** 2 + (pi / sm) ** 2 - 2 * ((pi / st) ** 2)
        term_wpp = -2 * (pi ** 3) * (cp / (sp ** 3) + cm / (sm ** 3))
        wp += term_wp
        wpp += term_wpp
        if abs(term_wp) < mp.mpf("1e-44") and abs(term_wpp) < mp.mpf("1e-44"):
            break
    return wp, wpp


def _eisenstein_g2_g3_mp(tau: mp.mpc) -> Tuple[mp.mpc, mp.mpc]:
    q = mp.exp(2 * mp.j * mp.pi * tau)
    e4 = mp.mpc(1)
    e6 = mp.mpc(1)
    qn = q
    for n in range(1, 140):
        if abs(qn) < mp.mpf("1e-46"):
            break
        lam = qn / (1 - qn)
        e4 += 240 * (n ** 3) * lam
        e6 -= 504 * (n ** 5) * lam
        qn *= q
    return (4 * (mp.pi ** 4) / 3) * e4, (8 * (mp.pi ** 6) / 27) * e6


def _eisenstein_E2_mp(tau: mp.mpc) -> mp.mpc:
    q = mp.exp(2 * mp.j * mp.pi * tau)
    e2 = mp.mpc(1)
    qn = q
    for n in range(1, 140):
        if abs(qn) < mp.mpf("1e-46"):
            break
        e2 -= 24 * n * (qn / (1 - qn))
        qn *= q
    return e2


def _lame_frob_mp(z: mp.mpc, g2: mp.mpc, g3: mp.mpc, c_acc: mp.mpc, n_terms: int = 40) -> mp.matrix:
    c_wp: Dict[int, mp.mpc] = {1: g2 / 20, 2: g3 / 28}
    for k in range(3, n_terms + 2):
        c_wp[k] = (mp.mpf(3) / ((2 * k + 3) * (k - 2))) * sum(
            c_wp[m] * c_wp[k - 1 - m] for m in range(1, k - 1)
        )
    qcoeffs = [c_acc] + [c_wp[k] / 4 for k in range(1, n_terms + 1)]
    a = [mp.mpc(1)]
    b = [mp.mpc(0)]
    for n in range(1, n_terms):
        an = -sum(qcoeffs[n - 1 - m] * a[m] for m in range(n)) / (4 * n * n)
        bn = -(4 * n * an + sum(qcoeffs[n - 1 - m] * b[m] for m in range(1, n))) / (4 * n * n)
        a.append(an)
        b.append(bn)
    sz = mp.sqrt(z)
    lz = mp.log(z)
    z2 = z * z
    zp = mp.mpc(1)
    s_y1 = mp.mpc(0)
    s_dy1 = mp.mpc(0)
    s_h = mp.mpc(0)
    s_dh = mp.mpc(0)
    for n in range(n_terms):
        exp_n = 2 * n + mp.mpf("0.5")
        s_y1 += a[n] * zp
        s_dy1 += exp_n * a[n] * zp / z
        s_h += b[n] * zp
        s_dh += exp_n * b[n] * zp / z
        zp *= z2
    y1 = sz * s_y1
    dy1 = sz * s_dy1
    h = sz * s_h
    dh = sz * s_dh
    y2 = y1 * lz + h
    dy2 = dy1 * lz + y1 / z + dh
    fac = -mp.j / (2 * mp.pi)
    return mp.matrix([[fac * y2, fac * dy2], [y1, dy1]])


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


def _taylor_prop_mp(
    Y_init: mp.matrix,
    z_start: mp.mpc,
    z_end: mp.mpc,
    tau: mp.mpc,
    g2: mp.mpc,
    c_acc: mp.mpc,
    n_steps: int = 32,
    order: int = 28,
) -> mp.matrix:
    if abs(z_end - z_start) < mp.mpf("1e-40"):
        return Y_init.copy()
    h = (z_end - z_start) / n_steps
    Y = Y_init.copy()
    z = z_start
    half_g2 = g2 / 2
    for _ in range(n_steps):
        p0, p1 = _wp_and_wp_prime_mp(z, tau)
        p = [mp.mpc(0)] * (order + 1)
        p[0] = p0
        p[1] = p1
        p[2] = 3 * p0 * p0 - half_g2 / 2
        for k in range(3, order):
            p[k] = (mp.mpf(6) / (k * (k - 1))) * sum(p[j] * p[k - 2 - j] for j in range(k - 1))
        q = [p[0] / 4 + c_acc] + [p[k] / 4 for k in range(1, order)]
        Y_next = mp.zeros(2, 2)
        for row in range(2):
            u = [mp.mpc(0)] * (order + 1)
            u[0] = Y[row, 0]
            u[1] = Y[row, 1]
            for k in range(2, order + 1):
                u[k] = -sum(q[j] * u[k - 2 - j] for j in range(k - 1)) / (k * (k - 1))
            val = mp.mpc(0)
            dval = mp.mpc(0)
            hp = mp.mpc(1)
            for k in range(order + 1):
                val += u[k] * hp
                if k >= 1:
                    dval += k * u[k] * (hp / h)
                hp *= h
            Y_next[row, 0] = val
            Y_next[row, 1] = dval
        Y = Y_next
        z += h
    return Y


def _prop_const_mp(Y_init: mp.matrix, dz: mp.mpc, q_const: mp.mpc) -> mp.matrix:
    om = mp.sqrt(q_const)
    w = om * dz
    cw = mp.cos(w)
    sw_om = dz if abs(w) < mp.mpf("1e-18") else mp.sin(w) / om
    M_T = mp.matrix([[cw, -q_const * sw_om], [sw_om, cw]])
    return Y_init * M_T


def _lame_mono_mp(tau: mp.mpc, c_acc: mp.mpc) -> Tuple[mp.matrix, mp.matrix]:
    g2, g3 = _eisenstein_g2_g3_mp(tau)
    ty = float(mp.im(tau))
    tx = float(mp.re(tau))
    z0 = (mp.mpf("-0.5") - mp.mpf("0.5") * tau) if ty <= 3.0 else mp.mpc("-0.5", "-1.0")
    min_per = min(abs(m + n * tau) for m in range(-3, 4) for n in range(-3, 4) if (m, n) != (0, 0))
    r_target = min(mp.mpf("0.20") * min_per, mp.mpf("0.45") * abs(z0))
    zf = z0 * (r_target / abs(z0))
    Yf = _lame_frob_mp(zf, g2, g3, c_acc, n_terms=36)
    q_asymp = -(mp.pi ** 2 / 12) * _eisenstein_E2_mp(tau) + c_acc

    def sp_mp(Y_in: mp.matrix, za: mp.mpc, zb: mp.mpc) -> mp.matrix:
        za_f = complex(float(mp.re(za)), float(mp.im(za)))
        zb_f = complex(float(mp.re(zb)), float(mp.im(zb)))
        d_seg = max(1e-4, _seg_lat_dist_f(za_f.real, za_f.imag, zb_f.real, zb_f.imag, tx, ty))
        n_st = max(26, int(math.ceil(float(abs(zb - za)) / (0.055 * d_seg))))
        return _taylor_prop_mp(Y_in, za, zb, tau, g2, c_acc, n_steps=n_st, order=26)

    Y0 = sp_mp(Yf, zf, z0)
    YA = sp_mp(Y0, z0, z0 + 1)
    zb = z0 + tau
    if ty > 20.0:
        za1 = z0 + mp.mpf(2.5 / ty) * tau
        z1 = z0 + mp.mpf(9.5 / ty) * tau
        z2 = z0 + mp.mpf((ty - 7.5) / ty) * tau
        zb1 = z0 + mp.mpf((ty - 0.5) / ty) * tau
        Ym = sp_mp(sp_mp(Y0, z0, za1), za1, z1)
        Ym = _prop_const_mp(Ym, z2 - z1, q_asymp)
        YB = sp_mp(sp_mp(Ym, z2, zb1), zb1, zb)
    elif ty > 4.0:
        za1 = z0 + mp.mpf(2.5 / ty) * tau
        zb1 = z0 + mp.mpf((ty - 0.5) / ty) * tau
        YB = sp_mp(sp_mp(sp_mp(Y0, z0, za1), za1, zb1), zb1, zb)
    else:
        YB = sp_mp(Y0, z0, zb)
    Y0_inv = mp.inverse(Y0)
    return YA * Y0_inv, YB * Y0_inv


def _g4_mp(MA: mp.matrix, MB: mp.matrix) -> List[mp.mpc]:
    MAB = MA * MB
    MABi = MA * mp.inverse(MB)
    return [
        MA[0, 0] + MA[1, 1],
        MB[0, 0] + MB[1, 1],
        MAB[0, 0] + MAB[1, 1],
        MABi[0, 0] + MABi[1, 1],
    ]


def _gn_solve_mp(t_s: mp.mpc, c_init: mp.mpc, eps_fd: mp.mpf) -> mp.mpc:
    """4-trace Fricke-Klein Cauchy-Riemann Gauss-Newton step (full rank on all of H including Re(tau)=0 and 1/2)."""
    c_cur = c_init
    for _ in range(10):
        MA, MB = _lame_mono_mp(t_s, c_cur)
        g0 = _g4_mp(MA, MB)
        r0 = [mp.im(v) for v in g0]
        if max(abs(v) for v in r0) < mp.mpf("1e-30"):
            break
        MA_p, MB_p = _lame_mono_mp(t_s, c_cur + eps_fd)
        gp = _g4_mp(MA_p, MB_p)
        dg = [(gp[k] - g0[k]) / eps_fd for k in range(4)]
        j0 = [mp.im(v) for v in dg]
        j1 = [mp.re(v) for v in dg]
        a00 = sum(j0[k] * j0[k] for k in range(4))
        a01 = sum(j0[k] * j1[k] for k in range(4))
        a11 = sum(j1[k] * j1[k] for k in range(4))
        b0 = -sum(j0[k] * r0[k] for k in range(4))
        b1 = -sum(j1[k] * r0[k] for k in range(4))
        det = a00 * a11 - a01 * a01
        dx = (a11 * b0 - a01 * b1) / det
        dy = (-a01 * b0 + a00 * b1) / det
        c_cur += mp.mpc(dx, dy)
    return c_cur


def _solve_c_f64_homotopy(tau_in: complex) -> complex:
    ty = tau_in.imag
    if abs(tau_in - 1j) < 1e-14 or abs(tau_in - cmath.exp(1j * math.pi / 3.0)) < 1e-14:
        return 0j
    if ty >= 4.0:
        t_anc = complex(tau_in.real, 3.0)
        c_cur = 0j
        for st in range(1, 3):
            c_cur = _gn_solve_f64((1.0 - st / 2.0) * 1j + (st / 2.0) * t_anc, c_cur)
        n_up = max(1, int(math.ceil(math.log(ty / 3.0) / 0.55)))
        for st in range(1, n_up + 1):
            ys = 3.0 * ((ty / 3.0) ** (st / n_up))
            c_cur = _gn_solve_f64(complex(tau_in.real, ys), c_cur)
        return c_cur
    n_h = max(1, min(4, int(math.ceil(abs(tau_in - 1j) / 1.2))))
    c_cur = 0j
    for st in range(1, n_h + 1):
        c_cur = _gn_solve_f64((1.0 - st / n_h) * 1j + (st / n_h) * tau_in, c_cur)
    return c_cur


def uniformize_mp(tau_in: complex, dps: int = 42) -> Dict[str, float]:
    c_f64 = _solve_c_f64_homotopy(tau_in)
    dps_eff = max(dps, 54 if tau_in.imag > 12.0 else 42)
    with mp.workdps(dps_eff):
        tau = mp.mpc(str(tau_in.real), str(tau_in.imag))
        tau_i = mp.mpc(0, 1)
        tau_om6 = mp.exp(mp.j * mp.pi / 3)
        eps_fd = mp.mpf("1e-18")
        if abs(tau - tau_i) < mp.mpf("1e-28") or abs(tau - tau_om6) < mp.mpf("1e-28"):
            c_cur = mp.mpc(0)
        else:
            c_cur = _gn_solve_mp(tau, mp.mpc(repr(c_f64.real), repr(c_f64.imag)), eps_fd)
        MA, MB = _lame_mono_mp(tau, c_cur)
        comm = MA * MB * mp.inverse(MA) * mp.inverse(MB)
        lam = abs(mp.re(comm[0, 1]))
        assert abs(lam - 1) < mp.mpf("1e-20"), f"mp lam residual: {lam}"
        imB_A = -mp.im(MA[0, 0]) / mp.re(MA[1, 0])
        imB_B = -mp.im(MB[0, 0]) / mp.re(MB[1, 0])
        assert abs(imB_A - imB_B) < mp.mpf("1e-20"), f"mp non-Fuchsian branch at {tau_in}: {abs(imB_A - imB_B)}"
        imB = (imB_A + imB_B) / 2
        G = mp.matrix([[1, mp.j * imB], [0, 1]])
        Gi = mp.matrix([[1, -mp.j * imB], [0, 1]])
        RA_c = G * MA * Gi
        RB_c = G * MB * Gi
        RA = mp.matrix([[mp.re(RA_c[0, 0]), mp.re(RA_c[0, 1])], [mp.re(RA_c[1, 0]), mp.re(RA_c[1, 1])]])
        RB = mp.matrix([[mp.re(RB_c[0, 0]), mp.re(RB_c[0, 1])], [mp.re(RB_c[1, 0]), mp.re(RB_c[1, 1])]])
        gens = [("A", RA), ("a", mp.inverse(RA)), ("B", RB), ("b", mp.inverse(RB))]
        inv_t = {"A": "a", "a": "A", "B": "b", "b": "B"}
        min_c = min(abs(RA[1, 0]), abs(RB[1, 0]))
        fr = list(gens)
        for _ in range(5):
            nxt = []
            for ws, mat in fr:
                lc = ws[-1]
                for nm, gm in gens:
                    if nm == inv_t[lc]:
                        continue
                    pr = mat * gm
                    cv = abs(pr[1, 0])
                    if cv > mp.mpf("1e-9") and cv < min_c:
                        min_c = cv
                    if abs(pr[0, 0]) + abs(pr[0, 1]) + abs(pr[1, 0]) + abs(pr[1, 1]) < mp.mpf("1500"):
                        nxt.append((ws + nm, pr))
            fr = nxt
        L_max = (2 * mp.pi / lam) * (1 / min_c - imB)
        L_2 = mp.pi - (2 * mp.pi / lam) * imB
        sh = mp.mpf("0.5") * mp.log(mp.im(tau)) - (mp.euler + mp.log(mp.pi))
        return {
            "L_2": float(L_2),
            "L_max": float(L_max),
            "tilde_L_2": float(L_2 + sh),
            "tilde_L_max": float(L_max + sh),
        }


def omega6_closed_form_audit_mp(dps: int = 42) -> Tuple[float, float]:
    """Audits our mpmath Lame solver at exact omega_6 = exp(i*pi/3) against the closed-form eta^4 period integral in 42-digit arithmetic."""
    with mp.workdps(dps):
        def eta4(w: mp.mpc) -> mp.mpc:
            q = mp.exp(2 * mp.j * mp.pi * w)
            prod = mp.mpc(1)
            qn = q
            for _ in range(120):
                prod *= (1 - qn)
                if abs(qn) < mp.mpf("1e-46"):
                    break
                qn *= q
            return mp.exp(2 * mp.j * mp.pi * w / 6) * (prod ** 4)
        per1 = mp.quad(eta4, [mp.mpc(0, 1), mp.mpc("1.5", "0.5")])
        kappa_abs = 1 / abs(per1)
        imB_cf = mp.log(3 * kappa_abs / mp.pi) / (2 * mp.pi)
        cf_lmax = 2 * mp.pi * (mp.mpf(1) / 6 - imB_cf)
        cf_l2 = mp.pi - 2 * mp.pi * imB_cf

        tau_om6 = mp.exp(mp.j * mp.pi / 3)
        MA, MB = _lame_mono_mp(tau_om6, mp.mpc(0))
        comm = MA * MB * mp.inverse(MA) * mp.inverse(MB)
        lam = abs(mp.re(comm[0, 1]))
        imB = -(mp.im(MA[0, 0]) / mp.re(MA[1, 0]) + mp.im(MB[0, 0]) / mp.re(MB[1, 0])) / 2
        G = mp.matrix([[1, mp.j * imB], [0, 1]])
        Gi = mp.matrix([[1, -mp.j * imB], [0, 1]])
        RA_c = G * MA * Gi
        RB_c = G * MB * Gi
        min_c = min(abs(mp.re(RA_c[1, 0])), abs(mp.re(RB_c[1, 0])))
        l_max = (2 * mp.pi / lam) * (1 / min_c - imB)
        l_2 = mp.pi - (2 * mp.pi / lam) * imB
        return float(abs(l_2 - cf_l2)), float(abs(l_max - cf_lmax))


# Fast scalar float64 Fuchsian uniformizer (for Chebyshev grid construction + high-y fallback)
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
    """4-trace Fricke-Klein Cauchy-Riemann Gauss-Newton step (full rank on all of H including Re(tau)=0 and 1/2)."""
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


def _extract_L2_Lmax_from_mono(tau: complex, c_cur: complex) -> Tuple[float, float]:
    MA, MB = _lame_mono_f64(tau, c_cur)
    comm = MA @ MB @ np.linalg.inv(MA) @ np.linalg.inv(MB)
    lam = abs(comm[0, 1].real)
    assert abs(lam - 1.0) < 1e-9, f"Fast Fuchsian lam={lam} at tau={tau}"
    imB_A = -MA[0, 0].imag / MA[1, 0].real
    imB_B = -MB[0, 0].imag / MB[1, 0].real
    assert abs(imB_A - imB_B) < 1e-10, f"Non-Fuchsian branch at tau={tau}: diff={abs(imB_A - imB_B)}"
    imB = 0.5 * (imB_A + imB_B)
    G = np.array([[1.0, 1j * imB], [0.0, 1.0]])
    Gi = np.array([[1.0, -1j * imB], [0.0, 1.0]])
    RA = (G @ MA @ Gi).real
    RB = (G @ MB @ Gi).real
    RA_i = np.linalg.inv(RA)
    RB_i = np.linalg.inv(RB)
    gens = [("A", RA), ("a", RA_i), ("B", RB), ("b", RB_i)]
    inv_t = {"A": "a", "a": "A", "B": "b", "b": "B"}
    min_c = min(abs(RA[1, 0]), abs(RB[1, 0]))
    fr = list(gens)
    for _ in range(5):
        nxt = []
        for ws, mat in fr:
            lc = ws[-1]
            for nm, gm in gens:
                if nm == inv_t[lc]:
                    continue
                pr = mat @ gm
                cv = abs(pr[1, 0])
                if cv > 1e-9 and cv < min_c:
                    min_c = cv
                if np.sum(np.abs(pr)) < 1500.0:
                    nxt.append((ws + nm, pr))
        fr = nxt
    L_max = (2.0 * math.pi / lam) * (1.0 / min_c - imB)
    L_2 = math.pi - (2.0 * math.pi / lam) * imB
    return L_2, L_max


def uniformize_fast(tau: complex) -> Tuple[float, float]:
    """Returns (tilde_L_2(tau), tilde_L_max(tau)) in float64 via 4-trace Gauss-Newton branch tracking."""
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
    L_2, L_max = _extract_L2_Lmax_from_mono(tau, c_cur)
    sh = 0.5 * math.log(ty) - NORM_CONST_SHIFT
    return L_2 + sh, L_max + sh


def _uniformize_column_fast(args: Tuple[float, List[float]]) -> List[Tuple[float, float]]:
    """
    Warm-starts c_cur continuously along an ascending-y column at fixed x = xv.
    Returns cusp-desingularized pair (L_2(tau), L_max(tau) - (pi/2)*y), which remain bounded and real-analytic
    down to u = 1/y -> 0!
    """
    xv, ys = args
    order = sorted(range(len(ys)), key=lambda idx: ys[idx])
    res: List[Tuple[float, float]] = [(0.0, 0.0)] * len(ys)
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
        L_2, L_max = _extract_L2_Lmax_from_mono(tau, c_cur)
        res[idx] = (L_2, L_max - 0.5 * math.pi * yv)
    return res


# ============================================================================
# SECTION 1: 4-PATCH CHEBYSHEV SPECTRAL EVALUATOR ON F_+ = {0 <= x <= 1/2, |tau| >= 1}
# ============================================================================

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


class CanonicalEndEvaluator:
    """
    Piecewise 2D Chebyshev-Gauss-Lobatto spectral interpolant of cusp-desingularized L_2(tau)
    and L_max(tau) - (pi/2)*Im(tau) on F_+ = {0 <= x <= 0.5, x^2 + y^2 >= 1}, extended to all F
    by mirror symmetry tilde_L(-conj(tau)) = tilde_L(tau).
    """

    def __init__(self, n_workers: int = 10):
        # Patch 1: warped y in [sqrt(1 - x^2), 1.85], 18 x 18
        # Patch 2: rect   y in [1.85, 4.50],          14 x 18
        # Patch 3: rect   y in [4.50, 12.0],          10 x 18
        # Patch 4: inv-y  u=1/y in [1/38.0, 1/12.0],   8 x 16
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
            col_vals = pool.map(_uniformize_column_fast, col_tasks)
        vals = [item for col in col_vals for item in col]

        arr_l2 = np.array([v[0] for v in vals], dtype=np.float64)
        arr_lmax_d = np.array([v[1] for v in vals], dtype=np.float64)

        n1 = self.p1_nx * self.p1_ny
        n2 = self.p2_nx * self.p2_ny
        n3 = self.p3_nx * self.p3_ny
        n4 = self.p4_nx * self.p4_ny

        i0 = 0
        self.v1_l2 = arr_l2[i0:i0 + n1].reshape(self.p1_nx, self.p1_ny)
        self.v1_lm = arr_lmax_d[i0:i0 + n1].reshape(self.p1_nx, self.p1_ny)
        i0 += n1
        self.v2_l2 = arr_l2[i0:i0 + n2].reshape(self.p2_nx, self.p2_ny)
        self.v2_lm = arr_lmax_d[i0:i0 + n2].reshape(self.p2_nx, self.p2_ny)
        i0 += n2
        self.v3_l2 = arr_l2[i0:i0 + n3].reshape(self.p3_nx, self.p3_ny)
        self.v3_lm = arr_lmax_d[i0:i0 + n3].reshape(self.p3_nx, self.p3_ny)
        i0 += n3
        self.v4_l2 = arr_l2[i0:i0 + n4].reshape(self.p4_nx, self.p4_ny)
        self.v4_lm = arr_lmax_d[i0:i0 + n4].reshape(self.p4_nx, self.p4_ny)

    def eval_batch(self, tau_red: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """Evaluate (tilde_L_2, tilde_L_max) on an array of SL(2,Z)-reduced tau in F."""
        xv = np.clip(np.abs(tau_red.real), 0.0, 0.5)
        yv = tau_red.imag
        raw_l2 = np.empty(len(tau_red), dtype=np.float64)
        raw_lm_d = np.empty(len(tau_red), dtype=np.float64)

        m1 = yv <= 1.85
        m2 = (yv > 1.85) & (yv <= 4.50)
        m3 = (yv > 4.50) & (yv <= 12.0)
        m4 = (yv > 12.0) & (yv <= 38.0)
        m5 = yv > 38.0

        if np.any(m1):
            xx = xv[m1]
            yy = yv[m1]
            ylo = np.sqrt(np.maximum(0.0, 1.0 - xx * xx))
            sv = np.clip((yy - ylo) / (1.85 - ylo), 0.0, 1.0)
            bx = _bary_weights_batch(4.0 * xx - 1.0, self.x1, self.wx1)
            by = _bary_weights_batch(2.0 * sv - 1.0, self.y1, self.wy1)
            raw_l2[m1] = np.einsum("ni,ij,nj->n", bx, self.v1_l2, by)
            raw_lm_d[m1] = np.einsum("ni,ij,nj->n", bx, self.v1_lm, by)

        if np.any(m2):
            xx = xv[m2]
            yy = yv[m2]
            bx = _bary_weights_batch(4.0 * xx - 1.0, self.x2, self.wx2)
            by = _bary_weights_batch(2.0 * (yy - 1.85) / (4.50 - 1.85) - 1.0, self.y2, self.wy2)
            raw_l2[m2] = np.einsum("ni,ij,nj->n", bx, self.v2_l2, by)
            raw_lm_d[m2] = np.einsum("ni,ij,nj->n", bx, self.v2_lm, by)

        if np.any(m3):
            xx = xv[m3]
            yy = yv[m3]
            bx = _bary_weights_batch(4.0 * xx - 1.0, self.x3, self.wx3)
            by = _bary_weights_batch(2.0 * (yy - 4.50) / (12.0 - 4.50) - 1.0, self.y3, self.wy3)
            raw_l2[m3] = np.einsum("ni,ij,nj->n", bx, self.v3_l2, by)
            raw_lm_d[m3] = np.einsum("ni,ij,nj->n", bx, self.v3_lm, by)

        if np.any(m4):
            xx = xv[m4]
            inv_y = 1.0 / yv[m4]
            u_lo, u_hi = 1.0 / 38.0, 1.0 / 12.0
            bx = _bary_weights_batch(4.0 * xx - 1.0, self.x4, self.wx4)
            by = _bary_weights_batch(2.0 * (inv_y - u_lo) / (u_hi - u_lo) - 1.0, self.y4, self.wy4)
            raw_l2[m4] = np.einsum("ni,ij,nj->n", bx, self.v4_l2, by)
            raw_lm_d[m4] = np.einsum("ni,ij,nj->n", bx, self.v4_lm, by)

        sh = 0.5 * np.log(yv) - NORM_CONST_SHIFT
        out_l2 = raw_l2 + sh
        out_lm = raw_lm_d + 0.5 * math.pi * yv + sh

        if np.any(m5):
            idxs = np.where(m5)[0]
            for idx in idxs:
                l2_v, lm_v = uniformize_fast(complex(xv[idx], yv[idx]))
                out_l2[idx] = l2_v
                out_lm[idx] = lm_v

        return out_l2, out_lm


# ============================================================================
# SECTION 2: EXACT SERRE q-SERIES, OVERFLOW-FREE RESIDUES, B1919 NORM & T_COUP
# ============================================================================

def _build_serre_B1_coeff_table(max_k: int = 168) -> Tuple[np.ndarray, np.ndarray]:
    """
    Exact Gaussian-rational q^{1/8}-series for B1691's weight-3/2 covariant triplet DR = B[1]
    (where R = (-th2^2, -th4^2, i*th3^2)/(th2*th3*th4) and D_{-1/2} f = q df/dq + (1/24) E2 f).
    Note: overall constant 1/pi on R cancels identically in all singular-value ratios and mixing matrices;
    we include 1/pi as well so Y matches B1691/B1724 normalization literally.
    Returns (powers_int, coeff_3_by_K_complex128).
    """
    N = max_k

    def s_mul(a: Dict[int, Tuple[Fraction, Fraction]], b: Dict[int, Tuple[Fraction, Fraction]]):
        out: Dict[int, Tuple[Fraction, Fraction]] = {}
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

    def s_inv(a: Dict[int, Tuple[Fraction, Fraction]]):
        k0 = min(a)
        r0, i0 = a[k0]
        n2 = r0 * r0 + i0 * i0
        inv0 = (r0 / n2, -i0 / n2)
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
        # D_{-1/2} f = q df/dq - (-1/2 / 12) E2 f = q df/dq + (1/24) E2 f
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
    """
    Constructs the exact (3, 4, 3, 3) bilinear Yukawa coupling tensor T_COUP[alpha, s, a, b]
    directly from the 2x2 quaternion units so that for c3 = (c_i, c_j, c_k) and u4 = (u_1, u_i, u_j, u_k),
    Y = einsum('...a,...s,asrc->...rc', c3, u4, T_COUP) equals b1656_funcs.coupling(S, weighted_M(u)) identically.
    """
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


SERRE_KS, SERRE_MAT = _build_serre_B1_coeff_table(168)
T_COUP = _build_coupling_tensor()

SIX_CHARGES = {
    "up": (1, -4),
    "down": (1, 2),
    "lepton": (-3, 6),
}

# 12 antipodal representatives of the 24 primitive order-5 points P_5 = (Z/5Z)^2 \ {(0,0)}
P5_ALL_24: List[Tuple[float, float]] = [
    (j / 5.0, k / 5.0) for j in range(5) for k in range(5) if (j, k) != (0, 0)
]
P5_HALF_12: List[Tuple[float, float]] = []
_seen_p5 = set()
for _j in range(5):
    for _k in range(5):
        if (_j, _k) == (0, 0):
            continue
        _neg = ((-_j) % 5, (-_k) % 5)
        if (_j, _k) not in _seen_p5 and _neg not in _seen_p5:
            P5_HALF_12.append((_j / 5.0, _k / 5.0))
            _seen_p5.add((_j, _k))
            _seen_p5.add(_neg)
assert len(P5_HALF_12) == 12


def _theta_char_batch(alpha: np.ndarray, beta: np.ndarray, tau: np.ndarray) -> np.ndarray:
    """
    Evaluates Theta_char(alpha, beta | tau) = sum_{n in Z} exp(i*pi*tau*(n + alpha)^2 + 2*pi*i*(n + alpha)*beta)
    for arbitrary real arrays alpha, beta of shape (B,) and reduced tau of shape (B,) (Im(tau) >= 0.86),
    by centering n = k - round(alpha) so |k + alpha_tilde| <= 6.5 -> zero overflow/underflow at ALL Im(tau)!
    """
    a_tilde = alpha - np.rint(alpha)
    ks = np.arange(-6, 7, dtype=np.float64)[None, :]  # (1, 13)
    m = ks + a_tilde[:, None]                         # (B, 13)
    exponent = 1j * math.pi * tau[:, None] * (m * m) + 2j * math.pi * m * beta[:, None]
    return np.sum(np.exp(exponent), axis=1)


def _th1_prime_0_batch(tau: np.ndarray) -> np.ndarray:
    """Evaluates theta_1'(0 | tau) = 2*pi * sum_{k=0}^7 (-1)^k (2k+1) exp(i*pi*tau*(k+1/2)^2)."""
    ks = np.arange(8, dtype=np.float64)[None, :]
    h = ks + 0.5
    signs = ((-1.0) ** ks) * (2.0 * ks + 1.0)
    return 2.0 * math.pi * np.sum(signs * np.exp(1j * math.pi * tau[:, None] * (h * h)), axis=1)


def _residues_closed_batch(
    tau: np.ndarray,
    a: np.ndarray,
    b: np.ndarray,
    qL: int,
    qR: int,
) -> np.ndarray:
    """
    Overflow-free exact closed-form residues R_s (shape (B, 4) in order ["1", "i", "j", "k"])
    for B1656's level-2 theta bilinear at w = a*tau + b (real twist doubled: bx = 2*q*b).
    Because 2*(qL^2 + qR^2) - (qL + qR)^2 - (qL - qR)^2 == 0 identically, G_char cancels
    the Gaussian prefactors of theta_s(ubar) * theta_s(delta) identically!
    """
    ap = (qL + qR) * a
    bp = (qL + qR) * b
    am = (qL - qR) * a
    bm = (qL - qR) * b
    th1p0 = _th1_prime_0_batch(tau)

    # s = "1" and s = "j" both shift beta by +1/2, contributing e^{-i*pi*(ap+am)} = e^{-2*pi*i*qL*a}
    phase_1 = np.exp(-1j * math.pi * (ap + am))  # = exp(-2*pi*i*qL*a)
    R_1 = (-1j) * phase_1 * _theta_char_batch(ap + 0.5, bp + 0.5, tau) * _theta_char_batch(am + 0.5, bm + 0.5, tau) / th1p0
    R_i = (-1.0) * _theta_char_batch(ap + 0.5, bp, tau) * _theta_char_batch(am + 0.5, bm, tau) / th1p0
    R_j = (-1.0) * phase_1 * _theta_char_batch(ap, bp + 0.5, tau) * _theta_char_batch(am, bm + 0.5, tau) / th1p0
    R_k = (+1j) * _theta_char_batch(ap, bp, tau) * _theta_char_batch(am, bm, tau) / th1p0
    return np.stack([R_1, R_i, R_j, R_k], axis=1)


def _F_kronecker_batch(u1: np.ndarray, u2: np.ndarray, tau: np.ndarray) -> np.ndarray:
    """
    Vectorized B1919 shifted Kronecker limit function F_u(tau) for arrays u1, u2, tau of shape (B,)
    with Im(tau) >= 0.86. Caller masks out exact (0, 0) mod 1 singularities where R_s == 0.
    """
    x = tau.real
    y = tau.imag
    a = np.mod(u1, 1.0)
    b = np.mod(u2, 1.0)
    # Snap near-0 or near-1 fractional parts cleanly
    a_zero = (a < 1e-12) | (a > 1.0 - 1e-12)
    a_safe = np.where(a_zero, 0.5, a)
    b_zero = (b < 1e-12) | (b > 1.0 - 1e-12)
    b_safe = np.where(b_zero, 0.5, b)

    first_nz = -math.pi * (2.0 * math.log(2.0) + np.log(y) + digamma(a_safe) + digamma(1.0 - a_safe))
    first_z = math.pi * (2.0 * EULER_GAMMA - 2.0 * math.log(2.0) - np.log(y))
    zero_row_z = np.where(b_zero, 0.0, y * (math.pi ** 2) / (np.sin(math.pi * b_safe) ** 2))
    base = np.where(a_zero, first_z + zero_row_z, first_nz)

    # For y >= 0.86, K = 11 gives exp(-2*pi*10*0.86) = 3.4e-24 < float64 machine epsilon!
    ks = np.arange(-11, 12, dtype=np.float64)[None, :]
    a_eff = np.where(a_zero, 0.0, a)[:, None]
    m = ks + a_eff                                   # (B, 23)
    m_nz = np.abs(m) > 1e-12
    m_safe = np.where(m_nz, m, 1.0)
    w = np.exp(-2.0 * math.pi * np.abs(m_safe) * y[:, None] + 2j * math.pi * (m_safe * x[:, None] + u2[:, None]))
    term = np.where(m_nz, (2.0 * math.pi / np.abs(m_safe)) * np.real(w / (1.0 - w)), 0.0)
    return base + np.sum(term, axis=1)


OUTPUT_KEYS_CANON = (
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


def evaluate_frame_batch(
    tau_red: np.ndarray,
    a_arr: np.ndarray,
    b_arr: np.ndarray,
    tilde_L: np.ndarray,
    global_mirror: bool = False,
) -> np.ndarray:
    """
    Vectorized evaluation of all 12 position-indexed outputs (shape (B, 12), matching OUTPUT_KEYS_CANON)
    at reduced tau_red in F, twist (a_arr, b_arr), and invariant end tilde_L.
    If global_mirror is False: record's charge-consistent reading (up: St, down: S, lepton: S).
    If global_mirror is True:  mirror reading (up: S, down: St, lepton: St) [PC_CANON_2].
    Note: in basis (q_i, q_j, q_k), St = q_j conj(S) q_j^T has components conj(c3)!
    """
    xq = np.exp(1j * math.pi * tau_red / 4.0)
    c3_S = (xq[:, None] ** SERRE_KS[None, :]) @ SERRE_MAT  # (B, 3)
    c3_St = np.conj(c3_S)

    c3_map = {
        "up": c3_S if global_mirror else c3_St,
        "down": c3_St if global_mirror else c3_S,
        "lepton": c3_St if global_mirror else c3_S,
    }

    Y_sec: Dict[str, np.ndarray] = {}
    for sec, (qL, qR) in SIX_CHARGES.items():
        R_mat = _residues_closed_batch(tau_red, a_arr, b_arr, qL, qR)  # (B, 4)
        ap = (qL + qR) * a_arr
        bp = (qL + qR) * b_arr
        shifts = [
            (ap, bp),
            (ap, bp - 0.5),
            (ap - 0.5, bp),
            (ap - 0.5, bp - 0.5),
        ]
        u_mat = np.zeros_like(R_mat)
        for s_idx, (u1, u2) in enumerate(shifts):
            R_col = R_mat[:, s_idx]
            active = np.abs(R_col) > 1e-12
            if np.any(active):
                Fu = _F_kronecker_batch(u1[active], u2[active], tau_red[active])
                w_sq = np.maximum(0.0, 2.0 * math.pi * tilde_L[active] + Fu)
                u_mat[active, s_idx] = np.sqrt(w_sq) * R_col[active]
        Y_sec[sec] = np.einsum("ba,bs,asrc->brc", c3_map[sec], u_mat, T_COUP)

    B = len(tau_red)
    out = np.empty((B, 12), dtype=np.float64)

    # Up SVD (full U needed for mixing; np.linalg.svd returns descending s[:,0] >= s[:,1] >= s[:,2])
    Uu_desc, sv_u, _ = np.linalg.svd(Y_sec["up"])
    Ud_desc, sv_d, _ = np.linalg.svd(Y_sec["down"])
    sv_l = np.linalg.svd(Y_sec["lepton"], compute_uv=False)

    # Ascending labels: sigma_1 = sv[:,2], sigma_2 = sv[:,1], sigma_3 = sv[:,0]
    out[:, 0] = sv_u[:, 1] / sv_u[:, 0]  # up__2_over_3
    out[:, 1] = sv_u[:, 2] / sv_u[:, 0]  # up__1_over_3
    out[:, 2] = sv_u[:, 2] / sv_u[:, 1]  # up__1_over_2

    out[:, 3] = sv_d[:, 1] / sv_d[:, 0]  # down__2_over_3
    out[:, 4] = sv_d[:, 2] / sv_d[:, 0]  # down__1_over_3
    out[:, 5] = sv_d[:, 2] / sv_d[:, 1]  # down__1_over_2

    out[:, 6] = sv_l[:, 1] / sv_l[:, 0]  # lepton__2_over_3
    out[:, 7] = sv_l[:, 2] / sv_l[:, 0]  # lepton__1_over_3
    out[:, 8] = sv_l[:, 2] / sv_l[:, 1]  # lepton__1_over_2

    Uu_asc = Uu_desc[:, :, ::-1]
    Ud_asc = Ud_desc[:, :, ::-1]
    V = np.einsum("aji,ajk->aik", np.conj(Uu_asc), Ud_asc)
    out[:, 9] = np.abs(V[:, 0, 1])       # mixing__1_2
    out[:, 10] = np.abs(V[:, 1, 2])      # mixing__2_3
    out[:, 11] = np.abs(V[:, 0, 2])      # mixing__1_3
    return out


# ============================================================================
# SECTION 3: MODULAR REDUCTION & OVERFLOW-FREE LOCAL SEMICIRCLE GEODESIC CHARTS
# ============================================================================

def reduce_tau_and_twist(t: complex, a: float, b: float) -> Tuple[complex, float, float]:
    """Reduces (tau, a, b) under SL(2, Z) into F = {|Re tau| <= 0.5, |tau| >= 1} preserving w = a*tau + b."""
    for _ in range(250):
        m = round(t.real)
        if m:
            t = t - m
            b = b + m * a
        if abs(t) < 1.0 - 1e-12:
            t, a, b = -1.0 / t, -b, a
        else:
            return t, a % 1.0, b % 1.0
    raise RuntimeError("SL(2,Z) reduction exceeded 250 steps")


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
    """
    Exact overflow-free local semicircle decomposition of the closed geodesic of gamma_w = W(w)^T
    for a hyperbolic word w in {L, R}^n (containing both L and R).
    Returns (gs, betas, betaps, ds_list, total_length).
    """
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


def single_word_mark_nodes(
    w: str,
    mark_int: Tuple[int, int] = (2, 4),
    start_shift: float = 0.0,
    nodes_per_len: float = 32.0,
    min_nodes: int = 64,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, float]:
    """
    Produces reduced (tau_red, a_red, b_red) arrays and exact length ell(w) along one closed period
    of w at the 5-torsion mark (mark_int[0]/5, mark_int[1]/5), supporting arbitrary word length n.
    """
    gs, betas, betaps, ds_list, ell = local_semicircle_charts(w)
    n = len(w)
    m_nodes = max(min_nodes, int(math.ceil(nodes_per_len * ell)))
    cum = [0.0]
    for d in ds_list:
        cum.append(cum[-1] + d)

    marks = [mark_int]
    ja, jb = mark_int
    for k in range(n):
        if gs[k] == "L":
            ja, jb = ja, (ja + jb) % 5
        else:
            ja, jb = (ja + jb) % 5, jb
        marks.append((ja, jb))

    tau_arr = np.empty(m_nodes, dtype=np.complex128)
    a_arr = np.empty(m_nodes, dtype=np.float64)
    b_arr = np.empty(m_nodes, dtype=np.float64)

    for j in range(m_nodes):
        s_glob = ((j / m_nodes + start_shift) % 1.0) * ell
        # Binary search step k
        lo, hi = 0, n - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if cum[mid] <= s_glob:
                lo = mid
            else:
                hi = mid - 1
        k_idx = lo
        s_loc = s_glob - cum[k_idx]
        ies = 1j * math.exp(s_loc)
        zt = (betas[k_idx] * ies + betaps[k_idx]) / (ies + 1.0)
        ma, mb = marks[k_idx]
        tr, ar, br = reduce_tau_and_twist(zt, ma / 5.0, mb / 5.0)
        tau_arr[j] = tr
        a_arr[j] = ar
        b_arr[j] = br
    return tau_arr, a_arr, b_arr, ell


# ============================================================================
# SECTION 4: STARTUP SELF-AUDIT GATES (GATES 1, 2, 3 + HAAR SCRAMBLING)
# ============================================================================

def run_startup_gates(end_eval: CanonicalEndEvaluator) -> Dict[str, Any]:
    # Gate 1: B1667 omega6 closed-form check in 42-digit mpmath arithmetic
    err_om6_l2, err_om6_lmax = omega6_closed_form_audit_mp(dps=42)
    assert err_om6_l2 < 1e-30 and err_om6_lmax < 1e-30

    # Gate 2: Out-of-grid 42-digit mpmath audit of 4-patch Chebyshev evaluator across F_+
    rng = random.Random(2026111401)
    test_taus: List[complex] = [
        0.0 + 1.0005j,
        0.499 + 0.871j,
        0.137 + 1.291j,
        0.312 + 1.849j,
        0.219 + 1.852j,
        0.441 + 3.712j,
        0.083 + 4.505j,
        0.388 + 9.400j,
        0.175 + 18.60j,
        0.412 + 28.50j,
    ]
    for _ in range(4):
        xv = rng.uniform(0.002, 0.498)
        ylo = math.sqrt(1.0 - xv * xv)
        yv = rng.uniform(ylo + 1e-3, 15.0)
        test_taus.append(complex(xv, yv))

    pred_l2, pred_lm = end_eval.eval_batch(np.array(test_taus, dtype=np.complex128))
    with Pool(min(10, max(2, (os.cpu_count() or 4) - 2))) as pool_g2:
        refs_g2 = pool_g2.map(uniformize_mp, test_taus)
    max_cheb_err_l2 = 0.0
    max_cheb_err_lm = 0.0
    for idx, ref in enumerate(refs_g2):
        max_cheb_err_l2 = max(max_cheb_err_l2, abs(float(pred_l2[idx]) - ref["tilde_L_2"]))
        max_cheb_err_lm = max(max_cheb_err_lm, abs(float(pred_lm[idx]) - ref["tilde_L_max"]))
    assert max_cheb_err_l2 < 1e-11, f"Chebyshev tilde_L2 error too high: {max_cheb_err_l2}"
    assert max_cheb_err_lm < 1e-6, f"Chebyshev tilde_Lmax error too high: {max_cheb_err_lm}"

    # Gate 3: Compare overflow-free closed-form residues + frame batch vs mpmath B1656 Cauchy contour integral
    # including high Im(tau) = 18 where naive exp would overflow!
    max_res_err = 0.0
    with mp.workdps(38):
        I = mp.mpc(0, 1)
        qi_m = mp.matrix([[I, 0], [0, -I]])
        qj_m = mp.matrix([[0, 1], [-1, 0]])
        qk_m = qi_m * qj_m
        units_m = [mp.eye(2), qi_m, qj_m, qk_m]

        def th_mp(n_idx: int, u_z: mp.mpc, t_z: mp.mpc) -> mp.mpc:
            q = mp.exp(I * mp.pi * t_z)
            x = mp.pi * u_z
            if n_idx == 3:
                return mp.jtheta(3, x, q)
            if n_idx == 4:
                return mp.jtheta(4, x, q)
            q4 = mp.exp(I * mp.pi * t_z / 4)
            s = x + mp.pi * t_z / 2
            if n_idx == 2:
                return q4 * mp.exp(I * x) * mp.jtheta(3, s, q)
            return -I * q4 * mp.exp(I * x) * mp.jtheta(4, s, q)

        def thc_mp(aa: mp.mpf, bb: mp.mpf, u_z: mp.mpc, T_z: mp.mpc) -> mp.mpc:
            return mp.exp(I * mp.pi * aa * aa * T_z + 2 * I * mp.pi * aa * (u_z + bb)) * th_mp(3, u_z + aa * T_z + bb, T_z)

        for tt in (0.137 + 1.291j, -0.311 + 2.45j, 0.22 + 18.0j):
            for (aa, bb) in ((0.4, 0.8), (0.2, 0.6), (0.8, 0.4)):
                for sec, (qL, qR) in SIX_CHARGES.items():
                    fast_R = _residues_closed_batch(
                        np.array([tt], dtype=np.complex128),
                        np.array([aa], dtype=np.float64),
                        np.array([bb], dtype=np.float64),
                        qL,
                        qR,
                    )[0]
                    t_mp = mp.mpc(str(tt.real), str(tt.imag))
                    ax, bx = mp.mpf(str(qL * aa)), mp.mpf(str(2 * qL * bb))
                    ay, by = mp.mpf(str(qR * aa)), mp.mpf(str(2 * qR * bb))
                    T_mp = 2 * t_mp
                    N_c = 128
                    rho = mp.mpf("0.015")
                    acc = [mp.mpc(0)] * 4
                    for k_c in range(N_c):
                        u_c = rho * mp.expjpi(2 * mp.mpf(k_c) / N_c)
                        t1 = th_mp(1, u_c, t_mp)
                        den = I * mp.exp(-I * mp.pi * t_mp / 2) * mp.exp(-I * mp.pi * u_c) * t1
                        X0 = thc_mp(ax, bx, u_c, T_mp)
                        X1 = thc_mp(ax, bx, u_c + t_mp, T_mp)
                        Y0 = thc_mp(ay, by, u_c, T_mp)
                        Y1 = thc_mp(ay, by, u_c + t_mp, T_mp)
                        M_b = mp.matrix([
                            [X0 * Y0 / t1, mp.exp(I * mp.pi * by) * X0 * Y1 / den],
                            [mp.exp(I * mp.pi * bx) * X1 * Y0 / den, mp.exp(I * mp.pi * (bx + by)) * X1 * Y1 / th_mp(1, u_c + t_mp, t_mp)],
                        ])
                        for s_i in range(4):
                            ec = qj_m * units_m[s_i]
                            p_val = sum(ec[r_i, c_i] * M_b[r_i, c_i] for r_i in range(2) for c_i in range(2))
                            acc[s_i] += p_val * u_c / N_c
                    for s_i in range(4):
                        r_ref = complex(float(mp.re(acc[s_i])), float(mp.im(acc[s_i])))
                        max_res_err = max(max_res_err, abs(fast_R[s_i] - r_ref) / max(1.0, abs(r_ref)))
    assert max_res_err < 1e-12, f"Closed-form residue rel mismatch vs contour integral: {max_res_err}"

    # Gate 4: Antipodal 12-pair vs 24-point exact equality + lepton == down at level 5 + Haar U(3)^5 scrambling!
    tt_arr = np.full(24, 0.213 + 1.417j, dtype=np.complex128)
    tl_val, _ = end_eval.eval_batch(np.array([0.213 + 1.417j], dtype=np.complex128))
    a24 = np.array([p[0] for p in P5_ALL_24], dtype=np.float64)
    b24 = np.array([p[1] for p in P5_ALL_24], dtype=np.float64)
    out24 = np.mean(evaluate_frame_batch(tt_arr, a24, b24, np.full(24, tl_val[0])), axis=0)
    a12 = np.array([p[0] for p in P5_HALF_12], dtype=np.float64)
    b12 = np.array([p[1] for p in P5_HALF_12], dtype=np.float64)
    out12 = np.mean(evaluate_frame_batch(tt_arr[:12], a12, b12, np.full(12, tl_val[0])), axis=0)
    antipodal_diff = float(np.max(np.abs(out24 - out12)))
    lep_down_diff = float(np.max(np.abs(out24[6:9] - out24[3:6])))
    assert antipodal_diff < 1e-14, f"12-pair vs 24-point mismatch: {antipodal_diff}"
    assert lep_down_diff < 1e-14, f"Level-5 lepton vs down mismatch: {lep_down_diff}"

    # Unitary Haar U(3)^5 basis-scrambling check (Guardrail 3)
    rng_np = np.random.default_rng(20261114)
    def rand_u3() -> np.ndarray:
        z = (rng_np.standard_normal((3, 3)) + 1j * rng_np.standard_normal((3, 3))) / math.sqrt(2.0)
        q, r = np.linalg.qr(z)
        d = np.diag(r)
        return q * (d / np.abs(d))[None, :]

    # Extract raw Y_u, Y_d, Y_l at one point and apply U_Q (shared left for up & down), U_u, U_d, U_L, U_e
    xq = np.exp(1j * math.pi * (0.213 + 1.417j) / 4.0)
    c3_S = ((xq ** SERRE_KS) @ SERRE_MAT)
    c3_St = np.conj(c3_S)
    Ys_raw = {}
    for sec, (qL, qR) in SIX_CHARGES.items():
        Rm = _residues_closed_batch(np.array([0.213 + 1.417j]), np.array([0.4]), np.array([0.8]), qL, qR)[0]
        ap, bp = (qL + qR) * 0.4, (qL + qR) * 0.8
        um = np.zeros(4, dtype=np.complex128)
        for si, (u1, u2) in enumerate([(ap, bp), (ap, bp - 0.5), (ap - 0.5, bp), (ap - 0.5, bp - 0.5)]):
            if abs(Rm[si]) > 1e-12:
                Fu = _F_kronecker_batch(np.array([u1]), np.array([u2]), np.array([0.213 + 1.417j]))[0]
                um[si] = math.sqrt(max(0.0, 2.0 * math.pi * tl_val[0] + Fu)) * Rm[si]
        c_use = c3_St if sec == "up" else c3_S
        Ys_raw[sec] = np.einsum("a,s,asrc->rc", c_use, um, T_COUP)

    ref_row = evaluate_frame_batch(np.array([0.213 + 1.417j]), np.array([0.4]), np.array([0.8]), np.array([tl_val[0]]))[0]
    max_haar_err = 0.0
    for _ in range(10):
        UQ, Uu_r, Ud_r, UL, Ue_r = rand_u3(), rand_u3(), rand_u3(), rand_u3(), rand_u3()
        Yu_s = UQ @ Ys_raw["up"] @ Uu_r.conj().T
        Yd_s = UQ @ Ys_raw["down"] @ Ud_r.conj().T
        Yl_s = UL @ Ys_raw["lepton"] @ Ue_r.conj().T
        Uu_d, su, _ = np.linalg.svd(Yu_s)
        Ud_d, sd, _ = np.linalg.svd(Yd_s)
        sl = np.linalg.svd(Yl_s, compute_uv=False)
        V_s = Uu_d[:, ::-1].conj().T @ Ud_d[:, ::-1]
        scr_row = np.array([
            su[1] / su[0], su[2] / su[0], su[2] / su[1],
            sd[1] / sd[0], sd[2] / sd[0], sd[2] / sd[1],
            sl[1] / sl[0], sl[2] / sl[0], sl[2] / sl[1],
            abs(V_s[0, 1]), abs(V_s[1, 2]), abs(V_s[0, 2]),
        ])
        max_haar_err = max(max_haar_err, float(np.max(np.abs(scr_row - ref_row))))
    assert max_haar_err < 1e-13, f"Haar basis-scrambling error: {max_haar_err}"

    # Gate 5 + PC_CANON_4: Allowed word window-shift invariance vs disallowed word window-shift failure
    t_a0, aa0, ba0, _ = single_word_mark_nodes("LLLLLLRLR", (2, 4), start_shift=0.0, nodes_per_len=80.0, min_nodes=320)
    t_a1, aa1, ba1, _ = single_word_mark_nodes("LLLLLLRLR", (2, 4), start_shift=0.37, nodes_per_len=80.0, min_nodes=320)
    tl_a0, _ = end_eval.eval_batch(t_a0)
    tl_a1, _ = end_eval.eval_batch(t_a1)
    m_a0 = np.mean(evaluate_frame_batch(t_a0, aa0, ba0, tl_a0), axis=0)
    m_a1 = np.mean(evaluate_frame_batch(t_a1, aa1, ba1, tl_a1), axis=0)
    allowed_win_spread = float(np.max(np.abs(m_a0 - m_a1)))
    assert allowed_win_spread < 1e-11, f"Allowed word window spread too large: {allowed_win_spread}"

    # Disallowed word w = "LLR": W(LLR) @ [1, 2]^T = [[3,2],[1,1]] @ [1,2] = [7,3] = [2,3] != +-(1,2) mod 5!
    # Evaluate literally along gamma_{LLR} geodesic with fixed unpermuted mark (0.4, 0.8) across two windows:
    _, betas_d, betaps_d, ds_d, ell_d = local_semicircle_charts("LLR")
    # Direct global geodesic of W(LLR)^T = [[3,1],[2,1]] on [betaps_d[0], betas_d[0]]:
    def eval_raw_window(sh: float) -> np.ndarray:
        taus_w, as_w, bs_w = [], [], []
        for j in range(96):
            s_val = (sh + j / 96.0) * ell_d - 0.5 * ell_d
            ies = 1j * math.exp(s_val)
            zt = (betas_d[0] * ies + betaps_d[0]) / (ies + 1.0)
            tr, ar, br = reduce_tau_and_twist(zt, 0.4, 0.8)
            taus_w.append(tr)
            as_w.append(ar)
            bs_w.append(br)
        t_arr = np.array(taus_w, dtype=np.complex128)
        tl_w, _ = end_eval.eval_batch(t_arr)
        return np.mean(evaluate_frame_batch(t_arr, np.array(as_w), np.array(bs_w), tl_w), axis=0)

    disallowed_win_spread = float(np.max(np.abs(eval_raw_window(0.0) - eval_raw_window(0.37))))
    assert disallowed_win_spread > 1e-2, f"PC_CANON_4 failed to fire: {disallowed_win_spread}"

    return {
        "omega6_L2_err_vs_closed_form": err_om6_l2,
        "omega6_Lmax_err_vs_closed_form": err_om6_lmax,
        "chebyshev_out_of_grid_max_err_tilde_L2": max_cheb_err_l2,
        "chebyshev_out_of_grid_max_err_tilde_Lmax": max_cheb_err_lm,
        "closed_residue_vs_contour_max_err": max_res_err,
        "p5_12pair_vs_24point_max_diff": antipodal_diff,
        "level5_lepton_vs_down_max_diff": lep_down_diff,
        "haar_u3_5_scrambling_max_err": max_haar_err,
        "allowed_word_window_spread": allowed_win_spread,
        "PC_CANON_4_disallowed_window_spread": disallowed_win_spread,
        "PC_CANON_4_fired": True,
    }


# ============================================================================
# SECTION 5: ROUTE 1 (EXHAUSTIVE FINITE-n POPULATIONS + SAMPLED n=24, 32)
# ============================================================================

_GLOBAL_END_EVAL: Optional[CanonicalEndEvaluator] = None


def _init_pool_worker(end_eval: CanonicalEndEvaluator):
    global _GLOBAL_END_EVAL
    _GLOBAL_END_EVAL = end_eval


def _eval_word_batch_route1(words: List[str]) -> List[Tuple[float, np.ndarray]]:
    assert _GLOBAL_END_EVAL is not None
    out_list: List[Tuple[float, np.ndarray]] = []
    for w in words:
        t_arr, a_arr, b_arr, ell = single_word_mark_nodes(w, (2, 4), start_shift=0.0, nodes_per_len=16.0, min_nodes=32)
        tl2, _ = _GLOBAL_END_EVAL.eval_batch(t_arr)
        vals = evaluate_frame_batch(t_arr, a_arr, b_arr, tl2, global_mirror=False)
        out_list.append((ell, np.mean(vals, axis=0)))
    return out_list


def enumerate_allowed_words(n: int) -> List[str]:
    """Exact exhaustive enumeration of all hyperbolic words w in {L, R}^n keeping +-(1, 2) mod 5."""
    # Track action mod 5 from right to left or left to right:
    # W(c_0 ... c_{n-1}) @ [1, 2]^T mod 5. Let state at step k be M_prefix mod 5 (2x2 tuple).
    # Even faster: recursive / bitmask! For n <= 18, 2^18 = 262,144 words -> C/numpy vectorized mod 5 takes 0.01s!
    ints = np.arange(1, (1 << n) - 1, dtype=np.uint32)  # excludes 00..0 (R..R) and 11..1 (L..L)!
    # Bit b_k = 1 -> 'L', 0 -> 'R'. Apply from right (k = n-1 down to 0) to vector v = (1, 2) mod 5!
    v0 = np.ones(len(ints), dtype=np.int8)
    v1 = np.full(len(ints), 2, dtype=np.int8)
    for k in range(n - 1, -1, -1):
        is_L = ((ints >> k) & 1).astype(bool)
        # L: (v0 + v1, v1) mod 5; R: (v0, v0 + v1) mod 5
        s = (v0 + v1) % 5
        v0 = np.where(is_L, s, v0)
        v1 = np.where(is_L, v1, s)
    keep = ((v0 == 1) & (v1 == 2)) | ((v0 == 4) & (v1 == 3))
    kept_ints = ints[keep]
    words: List[str] = []
    for val in kept_ints.tolist():
        chars = [("L" if ((val >> k) & 1) else "R") for k in range(n - 1, -1, -1)]
        words.append("".join(chars))
    return words


def _dict_from_vec(vec: np.ndarray) -> Dict[str, float]:
    return {k: float(vec[i]) for i, k in enumerate(OUTPUT_KEYS_CANON)}


def _jackknife_weighted(lengths: np.ndarray, means: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """Delete-1 jackknife mean and standard error for length-weighted trajectory averages."""
    tot_w = float(np.sum(lengths))
    w_sum = np.sum(lengths[:, None] * means, axis=0)
    est = w_sum / tot_w
    m = len(lengths)
    jk = (w_sum[None, :] - lengths[:, None] * means) / (tot_w - lengths[:, None])
    se = np.sqrt((m - 1.0) * np.mean((jk - est[None, :]) ** 2, axis=0))
    return est, se


def run_route1_populations(end_eval: CanonicalEndEvaluator, n_workers: int = 10) -> Dict[str, Any]:
    even_ns = (2, 4, 6, 8, 10, 12, 14, 16, 18)
    odd_ns = (3, 5, 7, 9, 11, 13, 15, 17)
    exhaustive_even: Dict[str, Any] = {}
    exhaustive_odd: Dict[str, Any] = {}

    with Pool(n_workers, initializer=_init_pool_worker, initargs=(end_eval,)) as pool:
        for n in even_ns:
            t0 = time.time()
            words = enumerate_allowed_words(n)
            chunks = [words[i::n_workers * 4] for i in range(min(len(words), n_workers * 4)) if words[i::n_workers * 4]]
            res_Nested = pool.map(_eval_word_batch_route1, chunks)
            flat = [item for sub in res_Nested for item in sub]
            ells = np.array([x[0] for x in flat], dtype=np.float64)
            arrs = np.array([x[1] for x in flat], dtype=np.float64)
            pop_mean = np.sum(ells[:, None] * arrs, axis=0) / np.sum(ells)
            exhaustive_even[str(n)] = {
                "n": n,
                "n_allowed_hyperbolic_words": len(words),
                "mean_geodesic_length": float(np.mean(ells)),
                "readout": _dict_from_vec(pop_mean),
                "elapsed_seconds": round(time.time() - t0, 3),
            }
            print(f"[Route 1] Exhaustive even n={n}: {len(words)} words ({int(round(time.time() - t0))}s)", flush=True)

        for n in odd_ns:
            t0 = time.time()
            words = enumerate_allowed_words(n)
            if not words:
                continue
            chunks = [words[i::n_workers * 4] for i in range(min(len(words), n_workers * 4)) if words[i::n_workers * 4]]
            res_Nested = pool.map(_eval_word_batch_route1, chunks)
            flat = [item for sub in res_Nested for item in sub]
            ells = np.array([x[0] for x in flat], dtype=np.float64)
            arrs = np.array([x[1] for x in flat], dtype=np.float64)
            pop_mean = np.sum(ells[:, None] * arrs, axis=0) / np.sum(ells)
            exhaustive_odd[str(n)] = {
                "n": n,
                "n_allowed_hyperbolic_words": len(words),
                "mean_geodesic_length": float(np.mean(ells)),
                "readout": _dict_from_vec(pop_mean),
                "elapsed_seconds": round(time.time() - t0, 3),
            }
            print(f"[Route 1] Exhaustive odd  n={n}: {len(words)} words ({int(round(time.time() - t0))}s)", flush=True)

        # Sampled populations at n = 24 and n = 32 (300 allowed words each, fixed deterministic seed)
        rng = random.Random(2026111422)
        sampled_high_n: Dict[str, Any] = {}
        for n_hi in (24, 32):
            t0 = time.time()
            words_hi: List[str] = []
            while len(words_hi) < 300:
                w_cand = "".join(rng.choice("LR") for _ in range(n_hi))
                if "L" not in w_cand or "R" not in w_cand:
                    continue
                ja, jb = 1, 2
                for ch in reversed(w_cand):
                    if ch == "L":
                        ja = (ja + jb) % 5
                    else:
                        jb = (ja + jb) % 5
                if (ja, jb) in ((1, 2), (4, 3)):
                    words_hi.append(w_cand)
            chunks = [words_hi[i::n_workers * 3] for i in range(n_workers * 3)]
            res_Nested = pool.map(_eval_word_batch_route1, chunks)
            flat = [item for sub in res_Nested for item in sub]
            ells = np.array([x[0] for x in flat], dtype=np.float64)
            arrs = np.array([x[1] for x in flat], dtype=np.float64)
            est, se = _jackknife_weighted(ells, arrs)
            sampled_high_n[str(n_hi)] = {
                "n": n_hi,
                "n_sampled_words": len(words_hi),
                "n_distinct_words": len(set(words_hi)),
                "readout": _dict_from_vec(est),
                "jackknife_se": _dict_from_vec(se),
                "elapsed_seconds": round(time.time() - t0, 3),
            }
            print(f"[Route 1] Sampled n={n_hi}: {len(words_hi)} words ({int(round(time.time() - t0))}s)", flush=True)

    # Successive population drift from n=14 -> 16 -> 18
    r14 = np.array([exhaustive_even["14"]["readout"][k] for k in OUTPUT_KEYS_CANON])
    r16 = np.array([exhaustive_even["16"]["readout"][k] for k in OUTPUT_KEYS_CANON])
    r18 = np.array([exhaustive_even["18"]["readout"][k] for k in OUTPUT_KEYS_CANON])
    drift_14_16 = float(np.max(np.abs(r16 - r14)))
    drift_16_18 = float(np.max(np.abs(r18 - r16)))

    return {
        "exhaustive_even": exhaustive_even,
        "exhaustive_odd": exhaustive_odd,
        "sampled_high_n": sampled_high_n,
        "max_abs_drift_14_to_16": drift_14_16,
        "max_abs_drift_16_to_18": drift_16_18,
    }


# ============================================================================
# SECTION 6: ROUTE 2 (ERGODIC INTEGRAL OF 24-POINT P_5 AVERAGE ALONG LONG WORDS)
#            + PLANTED CONTROLS PC_CANON_1, PC_CANON_2, PC_CANON_3
# ============================================================================

def _eval_ergodic_word_worker(args: Tuple[str, int]) -> Dict[str, Any]:
    """
    Integrates the 24-point P_5 average (via the 12 exact antipodal representatives) along one
    long periodic random word w in {L, R}^N using exact local semicircle charts, evaluating
    simultaneously:
      - canonical length-2 horocycle end tilde_L_2(tau) [Route 2 main],
      - global Higgs-reading mirror at tilde_L_2(tau)   [PC_CANON_2],
      - kinked maximal-horoball end tilde_L_max(tau)    [PC_CANON_3],
      - constant invariant ends 0.9 - (gamma+ln pi) and 1.3 - (gamma+ln pi) [PC_CANON_1].
    """
    assert _GLOBAL_END_EVAL is not None
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

    tau_red = np.array([reduce_tau_only(complex(z)) for z in zt_arr], dtype=np.complex128)
    tl2_nodes, tlm_nodes = _GLOBAL_END_EVAL.eval_batch(tau_red)

    a12 = np.array([p[0] for p in P5_HALF_12], dtype=np.float64)
    b12 = np.array([p[1] for p in P5_HALF_12], dtype=np.float64)

    # Process in chunks of 512 tau-nodes (512 * 12 = 6144 batch size) for cache-optimal vectorization
    acc_canon = np.zeros(12, dtype=np.float64)
    acc_mirror = np.zeros(12, dtype=np.float64)
    acc_lmax = np.zeros(12, dtype=np.float64)
    acc_c09 = np.zeros(12, dtype=np.float64)
    acc_c13 = np.zeros(12, dtype=np.float64)

    c09_val = 0.9 - NORM_CONST_SHIFT
    c13_val = 1.3 - NORM_CONST_SHIFT

    def _svd_12(Yu: np.ndarray, Yd: np.ndarray, Yl: np.ndarray) -> np.ndarray:
        out = np.empty((len(Yu), 12), dtype=np.float64)
        Uu_d, sv_u, _ = np.linalg.svd(Yu)
        Ud_d, sv_d, _ = np.linalg.svd(Yd)
        sv_l = np.linalg.svd(Yl, compute_uv=False)
        out[:, 0] = sv_u[:, 1] / sv_u[:, 0]
        out[:, 1] = sv_u[:, 2] / sv_u[:, 0]
        out[:, 2] = sv_u[:, 2] / sv_u[:, 1]
        out[:, 3] = sv_d[:, 1] / sv_d[:, 0]
        out[:, 4] = sv_d[:, 2] / sv_d[:, 0]
        out[:, 5] = sv_d[:, 2] / sv_d[:, 1]
        out[:, 6] = sv_l[:, 1] / sv_l[:, 0]
        out[:, 7] = sv_l[:, 2] / sv_l[:, 0]
        out[:, 8] = sv_l[:, 2] / sv_l[:, 1]
        V = np.einsum("aji,ajk->aik", np.conj(Uu_d[:, :, ::-1]), Ud_d[:, :, ::-1])
        out[:, 9] = np.abs(V[:, 0, 1])
        out[:, 10] = np.abs(V[:, 1, 2])
        out[:, 11] = np.abs(V[:, 0, 2])
        return out

    chunk_sz = 512
    for i0 in range(0, m_nodes, chunk_sz):
        i1 = min(m_nodes, i0 + chunk_sz)
        c_len = i1 - i0
        t_rep = np.repeat(tau_red[i0:i1], 12)
        a_rep = np.tile(a12, c_len)
        b_rep = np.tile(b12, c_len)
        tl2_rep = np.repeat(tl2_nodes[i0:i1], 12)
        tlm_rep = np.repeat(tlm_nodes[i0:i1], 12)

        xq = np.exp(1j * math.pi * t_rep / 4.0)
        c3_S = (xq[:, None] ** SERRE_KS[None, :]) @ SERRE_MAT
        c3_St = np.conj(c3_S)

        u_l2: Dict[str, np.ndarray] = {}
        u_lm: Dict[str, np.ndarray] = {}
        u_09: Dict[str, np.ndarray] = {}
        u_13: Dict[str, np.ndarray] = {}
        for sec, (qL, qR) in SIX_CHARGES.items():
            R_mat = _residues_closed_batch(t_rep, a_rep, b_rep, qL, qR)
            ap = (qL + qR) * a_rep
            bp = (qL + qR) * b_rep
            shifts = [(ap, bp), (ap, bp - 0.5), (ap - 0.5, bp), (ap - 0.5, bp - 0.5)]
            m_l2 = np.zeros_like(R_mat)
            m_lm = np.zeros_like(R_mat)
            m_09 = np.zeros_like(R_mat)
            m_13 = np.zeros_like(R_mat)
            for s_idx, (u1, u2) in enumerate(shifts):
                R_col = R_mat[:, s_idx]
                act = np.abs(R_col) > 1e-12
                if np.any(act):
                    Fu = _F_kronecker_batch(u1[act], u2[act], t_rep[act])
                    m_l2[act, s_idx] = np.sqrt(np.maximum(0.0, 2.0 * math.pi * tl2_rep[act] + Fu)) * R_col[act]
                    m_lm[act, s_idx] = np.sqrt(np.maximum(0.0, 2.0 * math.pi * tlm_rep[act] + Fu)) * R_col[act]
                    m_09[act, s_idx] = np.sqrt(np.maximum(0.0, 2.0 * math.pi * c09_val + Fu)) * R_col[act]
                    m_13[act, s_idx] = np.sqrt(np.maximum(0.0, 2.0 * math.pi * c13_val + Fu)) * R_col[act]
            u_l2[sec] = m_l2
            u_lm[sec] = m_lm
            u_09[sec] = m_09
            u_13[sec] = m_13

        acc_canon += np.sum(_svd_12(
            np.einsum("ba,bs,asrc->brc", c3_St, u_l2["up"], T_COUP),
            np.einsum("ba,bs,asrc->brc", c3_S, u_l2["down"], T_COUP),
            np.einsum("ba,bs,asrc->brc", c3_S, u_l2["lepton"], T_COUP),
        ), axis=0)
        acc_mirror += np.sum(_svd_12(
            np.einsum("ba,bs,asrc->brc", c3_S, u_l2["up"], T_COUP),
            np.einsum("ba,bs,asrc->brc", c3_St, u_l2["down"], T_COUP),
            np.einsum("ba,bs,asrc->brc", c3_St, u_l2["lepton"], T_COUP),
        ), axis=0)
        acc_lmax += np.sum(_svd_12(
            np.einsum("ba,bs,asrc->brc", c3_St, u_lm["up"], T_COUP),
            np.einsum("ba,bs,asrc->brc", c3_S, u_lm["down"], T_COUP),
            np.einsum("ba,bs,asrc->brc", c3_S, u_lm["lepton"], T_COUP),
        ), axis=0)
        acc_c09 += np.sum(_svd_12(
            np.einsum("ba,bs,asrc->brc", c3_St, u_09["up"], T_COUP),
            np.einsum("ba,bs,asrc->brc", c3_S, u_09["down"], T_COUP),
            np.einsum("ba,bs,asrc->brc", c3_S, u_09["lepton"], T_COUP),
        ), axis=0)
        acc_c13 += np.sum(_svd_12(
            np.einsum("ba,bs,asrc->brc", c3_St, u_13["up"], T_COUP),
            np.einsum("ba,bs,asrc->brc", c3_S, u_13["down"], T_COUP),
            np.einsum("ba,bs,asrc->brc", c3_S, u_13["lepton"], T_COUP),
        ), axis=0)

    denom = float(m_nodes * 12)
    return {
        "ell": ell,
        "max_im_tau_red": float(np.max(tau_red.imag)),
        "canon": acc_canon / denom,
        "mirror": acc_mirror / denom,
        "lmax": acc_lmax / denom,
        "c09": acc_c09 / denom,
        "c13": acc_c13 / denom,
    }


def run_route2_ergodic(end_eval: CanonicalEndEvaluator, n_workers: int = 10) -> Dict[str, Any]:
    rng = random.Random(2026111499)
    n_trajs = 64
    word_len = 2000
    nodes_per_move = 6
    words_long: List[str] = []
    while len(words_long) < n_trajs:
        w = "".join(rng.choice("LR") for _ in range(word_len))
        if "L" in w and "R" in w:
            words_long.append(w)

    t0 = time.time()
    with Pool(n_workers, initializer=_init_pool_worker, initargs=(end_eval,)) as pool:
        traj_res = pool.map(_eval_ergodic_word_worker, [(w, nodes_per_move) for w in words_long])
        # Quadrature refinement audit: re-evaluate first 8 trajectories at 2x density (12 nodes/move)
        fine_res = pool.map(_eval_ergodic_word_worker, [(w, nodes_per_move * 2) for w in words_long[:8]])
    dt = time.time() - t0

    ells = np.array([r["ell"] for r in traj_res], dtype=np.float64)
    max_y_seen = max(r["max_im_tau_red"] for r in traj_res)

    canon_mat = np.array([r["canon"] for r in traj_res], dtype=np.float64)
    mirror_mat = np.array([r["mirror"] for r in traj_res], dtype=np.float64)
    lmax_mat = np.array([r["lmax"] for r in traj_res], dtype=np.float64)
    c09_mat = np.array([r["c09"] for r in traj_res], dtype=np.float64)
    c13_mat = np.array([r["c13"] for r in traj_res], dtype=np.float64)

    est_canon, se_canon = _jackknife_weighted(ells, canon_mat)
    est_mirror, se_mirror = _jackknife_weighted(ells, mirror_mat)
    est_lmax, se_lmax = _jackknife_weighted(ells, lmax_mat)
    est_c09, se_c09 = _jackknife_weighted(ells, c09_mat)
    est_c13, se_c13 = _jackknife_weighted(ells, c13_mat)

    # Paired jackknife z-scores for PC_CANON_1, PC_CANON_2, PC_CANON_3!
    def paired_z(diff_mat: np.ndarray) -> np.ndarray:
        est_d, se_d = _jackknife_weighted(ells, diff_mat)
        return np.abs(est_d) / np.maximum(se_d, 1e-30)

    z_c09 = paired_z(canon_mat - c09_mat)
    z_c13 = paired_z(canon_mat - c13_mat)
    z_mirror = paired_z(canon_mat - mirror_mat)
    z_lmax = paired_z(canon_mat - lmax_mat)

    idx_claimed = [OUTPUT_KEYS_CANON.index(k) for k in CLAIMED_7_FRAME_CODE]
    max_z_c09 = float(np.max(z_c09[idx_claimed]))
    max_z_c13 = float(np.max(z_c13[idx_claimed]))
    min_z_mirror = float(np.min(z_mirror[idx_claimed]))
    max_z_mirror = float(np.max(z_mirror[idx_claimed]))
    max_z_lmax = float(np.max(z_lmax[idx_claimed]))

    assert max_z_c09 > 5.0 and max_z_c13 > 5.0, f"PC_CANON_1 failed to fire: {max_z_c09}, {max_z_c13}"
    assert max_z_mirror > 4.0, f"PC_CANON_2 failed to fire: {max_z_mirror}"
    assert max_z_lmax > 5.0, f"PC_CANON_3 failed to fire: {max_z_lmax}"

    # Split-half consistency check (first 32 vs second 32 trajectories)
    est_h1, se_h1 = _jackknife_weighted(ells[:32], canon_mat[:32])
    est_h2, se_h2 = _jackknife_weighted(ells[32:], canon_mat[32:])
    z_split = np.abs(est_h1 - est_h2) / np.sqrt(se_h1 ** 2 + se_h2 ** 2 + 1e-30)

    # Quadrature refinement difference (6 vs 12 nodes/move on 8 trajectories)
    coarse_8 = np.array([r["canon"] for r in traj_res[:8]], dtype=np.float64)
    fine_8 = np.array([r["canon"] for r in fine_res], dtype=np.float64)
    quad_refinement_max_diff = float(np.max(np.abs(fine_8 - coarse_8)))

    print(
        f"[Route 2] Ergodic {n_trajs}x{word_len} moves completed in {int(round(dt))}s (controls PC_CANON_1..3 FIRED)",
        flush=True,
    )

    return {
        "n_trajectories": n_trajs,
        "moves_per_trajectory": word_len,
        "total_move_steps": n_trajs * word_len,
        "nodes_per_move": nodes_per_move,
        "max_reduced_im_tau_observed": max_y_seen,
        "elapsed_seconds": round(dt, 3),
        "canonical_L2_readout": _dict_from_vec(est_canon),
        "canonical_L2_jackknife_se": _dict_from_vec(se_canon),
        "claimed_7_frame_code_convention": {k: float(est_canon[OUTPUT_KEYS_CANON.index(k)]) for k in CLAIMED_7_FRAME_CODE},
        "claimed_7_frame_code_se": {k: float(se_canon[OUTPUT_KEYS_CANON.index(k)]) for k in CLAIMED_7_FRAME_CODE},
        "claimed_7_adjacent_convention": {k: float(est_canon[OUTPUT_KEYS_CANON.index(k)]) for k in CLAIMED_7_ADJACENT},
        "claimed_7_adjacent_se": {k: float(se_canon[OUTPUT_KEYS_CANON.index(k)]) for k in CLAIMED_7_ADJACENT},
        "split_half_max_z_claimed_7": float(np.max(z_split[idx_claimed])),
        "split_half_median_z_claimed_7": float(np.median(z_split[idx_claimed])),
        "quadrature_6_vs_12_nodes_max_diff": quad_refinement_max_diff,
        "controls": {
            "PC_CANON_1_constant_end_0_9": {
                "readout": _dict_from_vec(est_c09),
                "jackknife_se": _dict_from_vec(se_c09),
                "paired_z_vs_canonical": _dict_from_vec(z_c09),
                "max_z_claimed_7": max_z_c09,
                "fired": True,
            },
            "PC_CANON_1_constant_end_1_3": {
                "readout": _dict_from_vec(est_c13),
                "jackknife_se": _dict_from_vec(se_c13),
                "paired_z_vs_canonical": _dict_from_vec(z_c13),
                "max_z_claimed_7": max_z_c13,
                "fired": True,
            },
            "PC_CANON_2_global_higgs_mirror": {
                "readout": _dict_from_vec(est_mirror),
                "jackknife_se": _dict_from_vec(se_mirror),
                "paired_z_vs_canonical": _dict_from_vec(z_mirror),
                "min_z_claimed_7": min_z_mirror,
                "max_z_claimed_7": max_z_mirror,
                "fired": True,
            },
            "PC_CANON_3_kinked_L_max_end": {
                "readout": _dict_from_vec(est_lmax),
                "jackknife_se": _dict_from_vec(se_lmax),
                "paired_z_vs_canonical": _dict_from_vec(z_lmax),
                "max_z_claimed_7": max_z_lmax,
                "fired": True,
            },
        },
    }


def main() -> None:
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    t_start = time.time()
    script_sha = hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()
    n_workers = min(10, max(2, (os.cpu_count() or 4) - 2))
    print(f"[X-CANON] Building 4-patch Chebyshev canonical-end evaluator on {n_workers} workers...", flush=True)
    t_grid0 = time.time()
    end_eval = CanonicalEndEvaluator(n_workers=n_workers)
    print(f"[X-CANON] Canonical-end evaluator built in {int(round(time.time() - t_grid0))}s. Running startup self-audit gates...", flush=True)

    gates = run_startup_gates(end_eval)
    print("[X-CANON] Startup self-audit gates PASSED (mpmath Lame, contour residues, Haar U(3)^5, PC_CANON_4).", flush=True)

    route1 = run_route1_populations(end_eval, n_workers=n_workers)
    route2 = run_route2_ergodic(end_eval, n_workers=n_workers)

    # Compare Route 1 (exhaustive n=18 and sampled n=32) against Route 2 ergodic integral
    r1_18 = np.array([route1["exhaustive_even"]["18"]["readout"][k] for k in OUTPUT_KEYS_CANON])
    r1_32 = np.array([route1["sampled_high_n"]["32"]["readout"][k] for k in OUTPUT_KEYS_CANON])
    se_32 = np.array([route1["sampled_high_n"]["32"]["jackknife_se"][k] for k in OUTPUT_KEYS_CANON])
    r2_est = np.array([route2["canonical_L2_readout"][k] for k in OUTPUT_KEYS_CANON])
    se_r2 = np.array([route2["canonical_L2_jackknife_se"][k] for k in OUTPUT_KEYS_CANON])

    diff_18_vs_erg = np.abs(r1_18 - r2_est)
    z_32_vs_erg = np.abs(r1_32 - r2_est) / np.sqrt(se_32 ** 2 + se_r2 ** 2 + 1e-30)
    idx_cl = [OUTPUT_KEYS_CANON.index(k) for k in CLAIMED_7_FRAME_CODE]

    print("[X-CANON] Route 1 and Route 2 complete. Writing all numerical values to JSON only.", flush=True)

    payload = {
        "card": "X-CANON",
        "seat": "agy-exp",
        "empirical_firewall": "0 of 19",
        "particle_names_used": False,
        "b1928_json_read_before_commit": False,
        "script_sha256": script_sha,
        "total_elapsed_seconds": round(time.time() - t_start, 3),
        "startup_gates": gates,
        "route1_finite_n_populations": route1,
        "route2_ergodic_24point_integral": route2,
        "route1_vs_route2_comparison": {
            "abs_diff_exhaustive_n18_vs_ergodic": _dict_from_vec(diff_18_vs_erg),
            "max_abs_diff_n18_vs_ergodic_claimed_7": float(np.max(diff_18_vs_erg[idx_cl])),
            "z_sampled_n32_vs_ergodic": _dict_from_vec(z_32_vs_erg),
            "median_z_n32_vs_ergodic_claimed_7": float(np.median(z_32_vs_erg[idx_cl])),
            "max_z_n32_vs_ergodic_claimed_7": float(np.max(z_32_vs_erg[idx_cl])),
        },
        "all_planted_controls_fired": True,
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"[X-CANON] DONE in {int(round(time.time() - t_start))}s -> {OUT_JSON.name}", flush=True)


if __name__ == "__main__":
    main()
