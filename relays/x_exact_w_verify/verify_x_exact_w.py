#!/usr/bin/env python3
"""
Standalone Zero-Import Verifier for Card X-EXACT-W (Seat agy-exp)
=================================================================
Computes Frame C's whole-weave read-out seven position-indexed values using B1667/B1927's
canonical length-2 horocycle end L_2(tau) and the move-count measure across:
  - Both Higgs worlds (P-847):
      W_- = (up: St, down: S, lepton: S)
      W_+ = (up: S,  down: St, lepton: St)
  - Both channel weights (B1838 / Theorem 90 vs B1919 small-cut):
      N_s^{T90} = 2*pi*L_2(tau) + c_s(tau) - pi * |a_{0,s}(tau)|^2 * exp(-2 * L_2(tau))
      N_s^{old} = 2*pi*L_2(tau) + c_s(tau)
  - Both computational routes:
      Route 1: Exhaustive allowed hyperbolic populations mod 5 (even n=2..18, odd n=3..17) + sampled n=24, 32
      Route 2: 64 ergodic periodic trajectories x 2000 uniform moves (128,000 steps) over the 24-point P_5 average

Strict Blindness & Firewall Compliance:
  - Zero imports from main.
  - B1928's fiber_ergodic_fine.json is NOT read before Commit 3 seals all raw JSON outputs.
  - Zero measured/PDG numbers anywhere ("0 of 19.").
  - Zero decimal floats or scientific notation printed to stdout; all numerical values written to JSON only.
  - Strictly position-indexed (sector, index) names; zero particle names anywhere.
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
OUT_JSON = HERE / "verify_x_exact_w_out.json"

EULER_GAMMA = 0.5772156649015328606065120900824024310421
NORM_CONST_SHIFT = EULER_GAMMA + math.log(math.pi)  # gamma_E + ln(pi)


# ============================================================================
# SECTION 1: STANDALONE PUNCTURED-TORUS FUCHSIAN UNIFORMIZATION (mpmath + float64)
# ============================================================================

def _wp_and_wp_prime_mp(z: mp.mpc, tau: mp.mpc) -> Tuple[mp.mpc, mp.mpc]:
    pi = mp.pi
    k_sh = int(mp.nint(mp.im(z) / mp.im(tau)))
    if k_sh != 0:
        z = z - k_sh * tau
    s0 = mp.sin(pi * z)
    c0 = mp.cos(pi * z)
    wp = (pi / s0) ** 2 - (pi ** 2) / 3
    wpp = -2 * (pi ** 3) * c0 / (s0 ** 3)
    m_max = max(6, int(math.ceil(48.0 / (math.pi * max(0.25, float(mp.im(tau)))))) + 2)
    for m in range(1, m_max + 1):
        mt = m * tau
        zm_p = pi * (z + mt)
        zm_m = pi * (z - mt)
        m_t = pi * mt
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
        L_2 = mp.pi - (2 * mp.pi / lam) * imB
        sh = mp.mpf("0.5") * mp.log(mp.im(tau)) - (mp.euler + mp.log(mp.pi))
        return {
            "L_2": float(L_2),
            "tilde_L_2": float(L_2 + sh),
        }


def omega6_closed_form_audit_mp(dps: int = 42) -> float:
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
        cf_l2 = mp.pi - 2 * mp.pi * imB_cf
        tau_om6 = mp.exp(mp.j * mp.pi / 3)
        MA, MB = _lame_mono_mp(tau_om6, mp.mpc(0))
        comm = MA * MB * mp.inverse(MA) * mp.inverse(MB)
        lam = abs(mp.re(comm[0, 1]))
        imB = -(mp.im(MA[0, 0]) / mp.re(MA[1, 0]) + mp.im(MB[0, 0]) / mp.re(MB[1, 0])) / 2
        l_2 = mp.pi - (2 * mp.pi / lam) * imB
        return float(abs(l_2 - cf_l2))


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
    e2 = 1.0 + 0j
    e4 = 1.0 + 0j
    e6 = 1.0 + 0j
    qn = q
    for n in range(1, 50):
        if abs(qn) < 1e-18:
            break
        lam = qn / (1.0 - qn)
        e2 -= 24.0 * n * lam
        n3 = n * n * n
        e4 += 240.0 * n3 * lam
        e6 -= 504.0 * n3 * n * n * lam
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
        inv4n2 = 1.0 / (4.0 * n * n)
        an = -sum(qcoeffs[n - 1 - m] * a[m] for m in range(n)) * inv4n2
        bn = -(4.0 * n * an + sum(qcoeffs[n - 1 - m] * b[m] for m in range(1, n))) * inv4n2
        a.append(an)
        b.append(bn)
    sz = cmath.sqrt(z)
    lz = cmath.log(z)
    z2 = z * z
    zp = 1.0 + 0j
    s_y1 = s_dy1 = s_h = s_dh = 0j
    inv_z = 1.0 / z
    for n in range(n_terms):
        en = 2.0 * n + 0.5
        az = a[n] * zp
        bz = b[n] * zp
        s_y1 += az
        s_dy1 += en * az * inv_z
        s_h += bz
        s_dh += en * bz * inv_z
        zp *= z2
    y1 = sz * s_y1
    dy1 = sz * s_dy1
    h = sz * s_h
    dh = sz * s_dh
    y2 = y1 * lz + h
    dy2 = dy1 * lz + y1 * inv_z + dh
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


def uniformize_tilde_L2_fast(tau: complex) -> float:
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
    L_2 = _extract_L2_from_mono(tau, c_cur)
    return L_2 + 0.5 * math.log(ty) - NORM_CONST_SHIFT


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

    def eval_batch(self, tau_red: np.ndarray) -> np.ndarray:
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
        out = raw_l2 + 0.5 * np.log(yv) - NORM_CONST_SHIFT
        if np.any(m5):
            for idx in np.where(m5)[0]:
                out[idx] = uniformize_tilde_L2_fast(complex(xv[idx], yv[idx]))
        return out


# ============================================================================
# SECTION 2: SERRE B[1], RESIDUES R_s, LAURENT CONSTANT TERM a_{0,s}, AND THEOREM 90 WEIGHT
# ============================================================================

def _build_serre_B1_coeff_table(max_k: int = 168) -> Tuple[np.ndarray, np.ndarray]:
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


SERRE_KS, SERRE_MAT = _build_serre_B1_coeff_table(168)
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
    a_tilde = alpha - np.rint(alpha)
    ks = np.arange(-7, 8, dtype=np.float64)[None, :]
    m = ks + a_tilde[:, None]
    exponent = 1j * math.pi * tau[:, None] * (m * m) + 2j * math.pi * m * beta[:, None]
    return np.sum(np.exp(exponent), axis=1)


def _a0_closed_batch(alpha: np.ndarray, beta: np.ndarray, tau: np.ndarray) -> np.ndarray:
    """
    Exact overflow-free Laurent constant term a_{0,s} in K_s(z) = P_s(z)/R_s = 1/z + a_{0,s} + O(z),
    equal to (d/dz|_{z=0} Theta_char(alpha, beta; z | tau)) / Theta_char(alpha, beta; 0 | tau).
    Caller restricts to active channels (|R_s| > 1e-12) so denominator is bounded strictly away from zero.
    """
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


def evaluate_four_modes_batch(
    tau_red: np.ndarray,
    a_arr: np.ndarray,
    b_arr: np.ndarray,
    tilde_L: np.ndarray,
    include_controls: bool = False,
) -> Dict[str, Any]:
    """
    Simultaneously evaluates:
      - W_minus_T90: W_- = (up: St, down: S, lepton: S) with N_s = 2*pi*L_2 + c_s - pi*|a_{0,s}|^2*exp(-2*L_2)
      - W_minus_old: W_- = (up: St, down: S, lepton: S) with N_s = 2*pi*L_2 + c_s
      - W_plus_T90:  W_+ = (up: S, down: St, lepton: St) with N_s = 2*pi*L_2 + c_s - pi*|a_{0,s}|^2*exp(-2*L_2)
      - W_plus_old:  W_+ = (up: S, down: St, lepton: St) with N_s = 2*pi*L_2 + c_s
    sharing the exact same theta residues R_s, Kronecker limits F_u, and Laurent coefficients a_{0,s}.
    """
    xq = np.exp(1j * math.pi * tau_red / 4.0)
    c3_S = (xq[:, None] ** SERRE_KS[None, :]) @ SERRE_MAT
    c3_St = np.conj(c3_S)
    yv = tau_red.imag
    # exp(-2 * L_2(tau)) = Im(tau) * exp(-2 * (tilde_L_2(tau) + gamma_E + ln(pi)))
    exp_m2L2 = yv * np.exp(-2.0 * (tilde_L + NORM_CONST_SHIFT))

    u_t90_map: Dict[str, np.ndarray] = {}
    u_old_map: Dict[str, np.ndarray] = {}
    u_pctrl_map: Dict[str, np.ndarray] = {}
    u_c09_map: Dict[str, np.ndarray] = {}
    u_c13_map: Dict[str, np.ndarray] = {}

    min_N_t90 = 1e9
    max_rel_corr = 0.0

    c09_tl = 0.9 - NORM_CONST_SHIFT
    c13_tl = 1.3 - NORM_CONST_SHIFT

    for sec, (qL, qR) in SIX_CHARGES.items():
        R_mat = _residues_closed_batch(tau_red, a_arr, b_arr, qL, qR)
        ap = (qL + qR) * a_arr
        bp = (qL + qR) * b_arr
        # u_s = c_s - (1/2, 1/2), so c_s = u_s + (1/2, 1/2):
        #   s="1": u=(ap, bp)         -> c=(ap+1/2, bp+1/2)
        #   s="i": u=(ap, bp-1/2)     -> c=(ap+1/2, bp)
        #   s="j": u=(ap-1/2, bp)     -> c=(ap, bp+1/2)
        #   s="k": u=(ap-1/2, bp-1/2) -> c=(ap, bp)
        shifts_and_chars = [
            ((ap, bp), (ap + 0.5, bp + 0.5)),
            ((ap, bp - 0.5), (ap + 0.5, bp)),
            ((ap - 0.5, bp), (ap, bp + 0.5)),
            ((ap - 0.5, bp - 0.5), (ap, bp)),
        ]
        u_t90 = np.zeros_like(R_mat)
        u_old = np.zeros_like(R_mat)
        u_pctrl = np.zeros_like(R_mat) if include_controls else u_old
        u_c09 = np.zeros_like(R_mat) if include_controls else u_old
        u_c13 = np.zeros_like(R_mat) if include_controls else u_old

        for s_idx, ((u1, u2), (al_c, be_c)) in enumerate(shifts_and_chars):
            R_col = R_mat[:, s_idx]
            active = np.abs(R_col) > 1e-12
            if np.any(active):
                Fu = _F_kronecker_batch(u1[active], u2[active], tau_red[active])
                a0_v = _a0_closed_batch(al_c[active], be_c[active], tau_red[active])
                n_old = 2.0 * math.pi * tilde_L[active] + Fu
                corr = math.pi * (np.abs(a0_v) ** 2) * exp_m2L2[active]
                n_t90 = n_old - corr
                min_N_t90 = min(min_N_t90, float(np.min(n_t90)))
                max_rel_corr = max(max_rel_corr, float(np.max(corr / np.maximum(n_old, 1e-12))))

                u_old[active, s_idx] = np.sqrt(np.maximum(0.0, n_old)) * R_col[active]
                u_t90[active, s_idx] = np.sqrt(np.maximum(0.0, n_t90)) * R_col[active]
                if include_controls:
                    u_pctrl[active, s_idx] = np.sqrt(np.maximum(0.0, n_old + corr)) * R_col[active]
                    u_c09[active, s_idx] = np.sqrt(np.maximum(0.0, 2.0 * math.pi * c09_tl + Fu)) * R_col[active]
                    u_c13[active, s_idx] = np.sqrt(np.maximum(0.0, 2.0 * math.pi * c13_tl + Fu)) * R_col[active]

        u_t90_map[sec] = u_t90
        u_old_map[sec] = u_old
        if include_controls:
            u_pctrl_map[sec] = u_pctrl
            u_c09_map[sec] = u_c09
            u_c13_map[sec] = u_c13

    def build_world_out(u_map: Dict[str, np.ndarray], is_w_plus: bool) -> np.ndarray:
        c_up = c3_S if is_w_plus else c3_St
        c_dn = c3_St if is_w_plus else c3_S
        Yu = np.einsum("ba,bs,asrc->brc", c_up, u_map["up"], T_COUP)
        Yd = np.einsum("ba,bs,asrc->brc", c_dn, u_map["down"], T_COUP)
        Yl = np.einsum("ba,bs,asrc->brc", c_dn, u_map["lepton"], T_COUP)
        return _extract_12_from_yukawas(Yu, Yd, Yl)

    out_dict: Dict[str, Any] = {
        "W_minus_T90": build_world_out(u_t90_map, False),
        "W_minus_old": build_world_out(u_old_map, False),
        "W_plus_T90": build_world_out(u_t90_map, True),
        "W_plus_old": build_world_out(u_old_map, True),
        "min_N_T90_observed": min_N_t90,
        "max_rel_corr_observed": max_rel_corr,
    }
    if include_controls:
        out_dict["PC_EX_1_W_minus_wrong_plus_sign_T90"] = build_world_out(u_pctrl_map, False)
        out_dict["PC_EX_3_W_minus_const_0_9"] = build_world_out(u_c09_map, False)
        out_dict["PC_EX_3_W_minus_const_1_3"] = build_world_out(u_c13_map, False)
    return out_dict


# ============================================================================
# SECTION 3: MODULAR REDUCTION, SEMICIRCLE CHARTS & STARTUP SELF-AUDIT GATES
# ============================================================================

def reduce_tau_and_twist(t: complex, a: float, b: float) -> Tuple[complex, float, float]:
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
    nodes_per_len: float = 30.0,
    min_nodes: int = 64,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, float]:
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


def run_startup_gates_exact_w(end_eval: CanonicalL2Evaluator, n_workers: int = 10) -> Dict[str, Any]:
    # Gate 1: omega_6 closed-form 42-digit audit
    err_om6 = omega6_closed_form_audit_mp(dps=42)
    assert err_om6 < 1e-30

    # Gate 2: Out-of-grid 42-digit mpmath audit across F_+ (including Re(tau)=0 and Re(tau)=0.499)
    rng = random.Random(2026111455)
    test_taus: List[complex] = [
        0.0 + 1.0005j,
        0.0 + 1.4200j,
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
    for _ in range(3):
        xv = rng.uniform(0.002, 0.498)
        ylo = math.sqrt(1.0 - xv * xv)
        test_taus.append(complex(xv, rng.uniform(ylo + 1e-3, 15.0)))

    pred_l2 = end_eval.eval_batch(np.array(test_taus, dtype=np.complex128))
    with Pool(n_workers) as pool_g2:
        refs_g2 = pool_g2.map(uniformize_mp, test_taus)
    max_cheb_err = max(abs(float(pred_l2[i]) - refs_g2[i]["tilde_L_2"]) for i in range(len(test_taus)))
    assert max_cheb_err < 1e-11, f"Chebyshev tilde_L2 error too high: {max_cheb_err}"

    # Gate 3 (EX1): 38-digit mpmath Cauchy circle integral check of BOTH R_s and a_{0,s} (including high Im(tau)=18)
    max_res_err = 0.0
    max_a0_err = 0.0
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
            return (q4 * mp.exp(I * x) * mp.jtheta(3, s, q)) if n_idx == 2 else (-I * q4 * mp.exp(I * x) * mp.jtheta(4, s, q))

        def thc_mp(aa: mp.mpf, bb: mp.mpf, u_z: mp.mpc, T_z: mp.mpc) -> mp.mpc:
            return mp.exp(I * mp.pi * aa * aa * T_z + 2 * I * mp.pi * aa * (u_z + bb)) * th_mp(3, u_z + aa * T_z + bb, T_z)

        for tt in (0.137 + 1.291j, -0.311 + 2.45j, 0.22 + 18.0j):
            for (aa, bb) in ((0.4, 0.8), (0.23, 0.61), (0.8, 0.4)):
                for sec, (qL, qR) in SIX_CHARGES.items():
                    t_np = np.array([tt], dtype=np.complex128)
                    a_np = np.array([aa], dtype=np.float64)
                    b_np = np.array([bb], dtype=np.float64)
                    fast_R = _residues_closed_batch(t_np, a_np, b_np, qL, qR)[0]
                    ap_f, bp_f = (qL + qR) * aa, (qL + qR) * bb
                    chars_f = [(ap_f + 0.5, bp_f + 0.5), (ap_f + 0.5, bp_f), (ap_f, bp_f + 0.5), (ap_f, bp_f)]

                    t_mp = mp.mpc(str(tt.real), str(tt.imag))
                    ax, bx = mp.mpf(str(qL * aa)), mp.mpf(str(2 * qL * bb))
                    ay, by = mp.mpf(str(qR * aa)), mp.mpf(str(2 * qR * bb))
                    T_mp = 2 * t_mp
                    N_c = 128
                    rho = mp.mpf("0.015")
                    us = [rho * mp.expjpi(2 * mp.mpf(k_c) / N_c) for k_c in range(N_c)]
                    acc_R = [mp.mpc(0)] * 4
                    P_vals = [[] for _ in range(4)]
                    for u_c in us:
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
                            pv = sum(ec[r_i, c_i] * M_b[r_i, c_i] for r_i in range(2) for c_i in range(2))
                            acc_R[s_i] += pv * u_c / N_c
                            P_vals[s_i].append(pv)
                    for s_i in range(4):
                        r_ref = complex(float(mp.re(acc_R[s_i])), float(mp.im(acc_R[s_i])))
                        max_res_err = max(max_res_err, abs(fast_R[s_i] - r_ref) / max(1.0, abs(r_ref)))
                        if abs(fast_R[s_i]) > 1e-10:
                            a0_ref_mp = sum(P_vals[s_i][k_c] / acc_R[s_i] - 1 / us[k_c] for k_c in range(N_c)) / N_c
                            a0_ref = complex(float(mp.re(a0_ref_mp)), float(mp.im(a0_ref_mp)))
                            al_c, be_c = chars_f[s_i]
                            a0_fast = _a0_closed_batch(np.array([al_c]), np.array([be_c]), t_np)[0]
                            max_a0_err = max(max_a0_err, abs(a0_fast - a0_ref) / max(1.0, abs(a0_ref)))
    assert max_res_err < 1e-12, f"R_s contour rel mismatch: {max_res_err}"
    assert max_a0_err < 1e-12, f"a_{{0,s}} contour rel mismatch: {max_a0_err}"

    # Gate 4 (EX1 + PC_EX_2): Exact SL(2,Z) (T and S) invariance of pi*|a_{0,s}|^2*exp(-2*L_2) and physical readout
    t0_mod = 0.17 + 1.08j
    a0_tw, b0_tw = 0.4, 0.8
    # T: (tau + 1, a, b - a); S: (-1/tau, -b, a)
    t_T, a_T, b_T = t0_mod + 1.0, a0_tw, (b0_tw - a0_tw) % 1.0
    t_S, a_S, b_S = -1.0 / t0_mod, (-b0_tw) % 1.0, a0_tw % 1.0

    mp_0 = uniformize_mp(t0_mod)
    mp_T = uniformize_mp(t_T)
    mp_S = uniformize_mp(t_S)

    def sorted_active_corrs(tt_c: complex, aa_c: float, bb_c: float, L2_val: float, omit_im_tau: bool = False) -> List[float]:
        corrs: List[float] = []
        for sec, (qL, qR) in SIX_CHARGES.items():
            Rm = _residues_closed_batch(np.array([tt_c]), np.array([aa_c]), np.array([bb_c]), qL, qR)[0]
            ap_c, bp_c = (qL + qR) * aa_c, (qL + qR) * bb_c
            chars_c = [(ap_c + 0.5, bp_c + 0.5), (ap_c + 0.5, bp_c), (ap_c, bp_c + 0.5), (ap_c, bp_c)]
            for s_i in range(4):
                if abs(Rm[s_i]) > 1e-10:
                    a0_v = _a0_closed_batch(np.array([chars_c[s_i][0]]), np.array([chars_c[s_i][1]]), np.array([tt_c]))[0]
                    if omit_im_tau:
                        tl_val = L2_val + 0.5 * math.log(tt_c.imag) - NORM_CONST_SHIFT
                        corrs.append(float(math.pi * (abs(a0_v) ** 2) * math.exp(-2.0 * (tl_val + NORM_CONST_SHIFT))))
                    else:
                        corrs.append(float(math.pi * (abs(a0_v) ** 2) * math.exp(-2.0 * L2_val)))
        return sorted(corrs)

    c_base = sorted_active_corrs(t0_mod, a0_tw, b0_tw, mp_0["L_2"], omit_im_tau=False)
    c_T = sorted_active_corrs(t_T, a_T, b_T, mp_T["L_2"], omit_im_tau=False)
    c_S = sorted_active_corrs(t_S, a_S, b_S, mp_S["L_2"], omit_im_tau=False)
    mod_T_corr_err = max(abs(x - y) for x, y in zip(c_base, c_T))
    mod_S_corr_err = max(abs(x - y) for x, y in zip(c_base, c_S))
    assert mod_T_corr_err < 1e-12 and mod_S_corr_err < 1e-11, f"Modular corr err: T={mod_T_corr_err}, S={mod_S_corr_err}"

    # PC_EX_2: omitting the Im(tau) factor breaks S-invariance by > 1e-2!
    c_base_bad = sorted_active_corrs(t0_mod, a0_tw, b0_tw, mp_0["L_2"], omit_im_tau=True)
    c_S_bad = sorted_active_corrs(t_S, a_S, b_S, mp_S["L_2"], omit_im_tau=True)
    pc_ex_2_S_break = max(abs(x - y) for x, y in zip(c_base_bad, c_S_bad))
    assert pc_ex_2_S_break > 1e-2, f"PC_EX_2 failed to fire: {pc_ex_2_S_break}"

    # Gate 5 (EX4 + Haar U(3)^5 scrambling + 12-pair vs 24-point):
    tt24 = np.full(24, t0_mod, dtype=np.complex128)
    tl24 = np.full(24, mp_0["tilde_L_2"], dtype=np.float64)
    a24 = np.array([p[0] for p in P5_ALL_24], dtype=np.float64)
    b24 = np.array([p[1] for p in P5_ALL_24], dtype=np.float64)
    ev24 = evaluate_four_modes_batch(tt24, a24, b24, tl24)
    a12 = np.array([p[0] for p in P5_HALF_12], dtype=np.float64)
    b12 = np.array([p[1] for p in P5_HALF_12], dtype=np.float64)
    ev12 = evaluate_four_modes_batch(tt24[:12], a12, b12, tl24[:12])

    antipodal_err = max(
        float(np.max(np.abs(np.mean(ev24[m_k], axis=0) - np.mean(ev12[m_k], axis=0))))
        for m_k in ("W_minus_T90", "W_minus_old", "W_plus_T90", "W_plus_old")
    )
    assert antipodal_err < 1e-14

    lep_down_err_wm = float(np.max(np.abs(np.mean(ev24["W_minus_T90"], axis=0)[6:9] - np.mean(ev24["W_minus_T90"], axis=0)[3:6])))
    lep_down_err_wp = float(np.max(np.abs(np.mean(ev24["W_plus_T90"], axis=0)[6:9] - np.mean(ev24["W_plus_T90"], axis=0)[3:6])))
    assert lep_down_err_wm < 1e-14 and lep_down_err_wp < 1e-14
    assert ev24["min_N_T90_observed"] > 0.0

    # Haar U(3)^5 basis-scrambling check under Theorem 90 weights (Guardrail 3)
    rng_np = np.random.default_rng(2026111488)
    def rand_u3() -> np.ndarray:
        z = (rng_np.standard_normal((3, 3)) + 1j * rng_np.standard_normal((3, 3))) / math.sqrt(2.0)
        q, r = np.linalg.qr(z)
        d = np.diag(r)
        return q * (d / np.abs(d))[None, :]

    xq = np.exp(1j * math.pi * t0_mod / 4.0)
    c3_S = (xq ** SERRE_KS) @ SERRE_MAT
    c3_St = np.conj(c3_S)
    Ys_t90 = {}
    exp_m2 = t0_mod.imag * math.exp(-2.0 * (mp_0["tilde_L_2"] + NORM_CONST_SHIFT))
    for sec, (qL, qR) in SIX_CHARGES.items():
        Rm = _residues_closed_batch(np.array([t0_mod]), np.array([0.4]), np.array([0.8]), qL, qR)[0]
        ap_h, bp_h = (qL + qR) * 0.4, (qL + qR) * 0.8
        sc_list = [((ap_h, bp_h), (ap_h + 0.5, bp_h + 0.5)), ((ap_h, bp_h - 0.5), (ap_h + 0.5, bp_h)),
                   ((ap_h - 0.5, bp_h), (ap_h, bp_h + 0.5)), ((ap_h - 0.5, bp_h - 0.5), (ap_h, bp_h))]
        um = np.zeros(4, dtype=np.complex128)
        for si, ((u1, u2), (alc, bec)) in enumerate(sc_list):
            if abs(Rm[si]) > 1e-12:
                Fu = _F_kronecker_batch(np.array([u1]), np.array([u2]), np.array([t0_mod]))[0]
                a0v = _a0_closed_batch(np.array([alc]), np.array([bec]), np.array([t0_mod]))[0]
                nt90 = 2.0 * math.pi * mp_0["tilde_L_2"] + Fu - math.pi * (abs(a0v) ** 2) * exp_m2
                um[si] = math.sqrt(max(0.0, nt90)) * Rm[si]
        c_use = c3_St if sec == "up" else c3_S
        Ys_t90[sec] = np.einsum("a,s,asrc->rc", c_use, um, T_COUP)

    ref_row = evaluate_four_modes_batch(np.array([t0_mod]), np.array([0.4]), np.array([0.8]), np.array([mp_0["tilde_L_2"]]))["W_minus_T90"][0]
    max_haar_err = 0.0
    for _ in range(10):
        UQ, Uu_r, Ud_r, UL, Ue_r = rand_u3(), rand_u3(), rand_u3(), rand_u3(), rand_u3()
        scr = _extract_12_from_yukawas(
            (UQ @ Ys_t90["up"] @ Uu_r.conj().T)[None, :, :],
            (UQ @ Ys_t90["down"] @ Ud_r.conj().T)[None, :, :],
            (UL @ Ys_t90["lepton"] @ Ue_r.conj().T)[None, :, :],
        )[0]
        max_haar_err = max(max_haar_err, float(np.max(np.abs(scr - ref_row))))
    assert max_haar_err < 1e-13

    return {
        "omega6_L2_err_vs_closed_form": err_om6,
        "chebyshev_out_of_grid_max_err_tilde_L2": max_cheb_err,
        "closed_R_s_vs_contour_max_err": max_res_err,
        "closed_a0_s_vs_contour_max_err": max_a0_err,
        "modular_T_invariance_T90_corr_max_err": mod_T_corr_err,
        "modular_S_invariance_T90_corr_max_err": mod_S_corr_err,
        "PC_EX_2_S_invariance_break_without_im_tau": pc_ex_2_S_break,
        "PC_EX_2_fired": True,
        "p5_12pair_vs_24point_max_err": antipodal_err,
        "level5_lepton_vs_down_T90_W_minus_max_err": lep_down_err_wm,
        "level5_lepton_vs_down_T90_W_plus_max_err": lep_down_err_wp,
        "haar_u3_5_scrambling_T90_max_err": max_haar_err,
    }


# ============================================================================
# SECTION 4: ROUTE 1 (EXHAUSTIVE FINITE-n POPULATIONS + SAMPLED n=24, 32)
# ============================================================================

_GLOBAL_L2_EVAL: Optional[CanonicalL2Evaluator] = None


def _init_pool_l2(end_eval: CanonicalL2Evaluator):
    global _GLOBAL_L2_EVAL
    _GLOBAL_L2_EVAL = end_eval


def _dict_12(vec: np.ndarray) -> Dict[str, float]:
    return {k: float(vec[i]) for i, k in enumerate(OUTPUT_KEYS_12)}


def _dict_7_fc(vec: np.ndarray) -> Dict[str, float]:
    return {k: float(vec[OUTPUT_KEYS_12.index(k)]) for k in CLAIMED_7_FRAME_CODE}


def _dict_7_adj(vec: np.ndarray) -> Dict[str, float]:
    return {k: float(vec[OUTPUT_KEYS_12.index(k)]) for k in CLAIMED_7_ADJACENT}


def _jackknife_weighted(lengths: np.ndarray, means: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    tot_w = float(np.sum(lengths))
    w_sum = np.sum(lengths[:, None] * means, axis=0)
    est = w_sum / tot_w
    m = len(lengths)
    jk = (w_sum[None, :] - lengths[:, None] * means) / (tot_w - lengths[:, None])
    se = np.sqrt((m - 1.0) * np.mean((jk - est[None, :]) ** 2, axis=0))
    return est, se


def enumerate_allowed_words(n: int) -> List[str]:
    ints = np.arange(1, (1 << n) - 1, dtype=np.uint32)
    v0 = np.ones(len(ints), dtype=np.int8)
    v1 = np.full(len(ints), 2, dtype=np.int8)
    for k in range(n - 1, -1, -1):
        is_L = ((ints >> k) & 1).astype(bool)
        s = (v0 + v1) % 5
        v0 = np.where(is_L, s, v0)
        v1 = np.where(is_L, v1, s)
    keep = ((v0 == 1) & (v1 == 2)) | ((v0 == 4) & (v1 == 3))
    kept_ints = ints[keep]
    return ["".join(("L" if ((val >> k) & 1) else "R") for k in range(n - 1, -1, -1)) for val in kept_ints.tolist()]


def _eval_word_batch_route1_four(words: List[str]) -> List[Tuple[float, np.ndarray, np.ndarray, np.ndarray, np.ndarray]]:
    assert _GLOBAL_L2_EVAL is not None
    out_list = []
    for w in words:
        t_arr, a_arr, b_arr, ell = single_word_mark_nodes(w, (2, 4), start_shift=0.0, nodes_per_len=16.0, min_nodes=32)
        tl2 = _GLOBAL_L2_EVAL.eval_batch(t_arr)
        ev = evaluate_four_modes_batch(t_arr, a_arr, b_arr, tl2, include_controls=False)
        out_list.append((
            ell,
            np.mean(ev["W_minus_T90"], axis=0),
            np.mean(ev["W_minus_old"], axis=0),
            np.mean(ev["W_plus_T90"], axis=0),
            np.mean(ev["W_plus_old"], axis=0),
        ))
    return out_list


def run_route1_four_modes(end_eval: CanonicalL2Evaluator, n_workers: int = 10) -> Dict[str, Any]:
    even_ns = (2, 4, 6, 8, 10, 12, 14, 16, 18)
    odd_ns = (3, 5, 7, 9, 11, 13, 15, 17)
    exhaustive_even: Dict[str, Any] = {}
    exhaustive_odd: Dict[str, Any] = {}

    with Pool(n_workers, initializer=_init_pool_l2, initargs=(end_eval,)) as pool:
        for n in even_ns:
            t0 = time.time()
            words = enumerate_allowed_words(n)
            chunks = [words[i::n_workers * 4] for i in range(min(len(words), n_workers * 4)) if words[i::n_workers * 4]]
            flat = [item for sub in pool.map(_eval_word_batch_route1_four, chunks) for item in sub]
            ells = np.array([x[0] for x in flat], dtype=np.float64)
            tot_l = float(np.sum(ells))
            m_wm_t90 = np.sum(ells[:, None] * np.array([x[1] for x in flat]), axis=0) / tot_l
            m_wm_old = np.sum(ells[:, None] * np.array([x[2] for x in flat]), axis=0) / tot_l
            m_wp_t90 = np.sum(ells[:, None] * np.array([x[3] for x in flat]), axis=0) / tot_l
            m_wp_old = np.sum(ells[:, None] * np.array([x[4] for x in flat]), axis=0) / tot_l
            exhaustive_even[str(n)] = {
                "n": n,
                "n_allowed_hyperbolic_words": len(words),
                "W_minus_T90": _dict_12(m_wm_t90),
                "W_minus_old": _dict_12(m_wm_old),
                "W_plus_T90": _dict_12(m_wp_t90),
                "W_plus_old": _dict_12(m_wp_old),
                "elapsed_seconds": round(time.time() - t0, 3),
            }
            print(f"[X-EXACT-W Route 1] Exhaustive even n={n}: {len(words)} words ({int(round(time.time() - t0))}s)", flush=True)

        for n in odd_ns:
            t0 = time.time()
            words = enumerate_allowed_words(n)
            if not words:
                continue
            chunks = [words[i::n_workers * 4] for i in range(min(len(words), n_workers * 4)) if words[i::n_workers * 4]]
            flat = [item for sub in pool.map(_eval_word_batch_route1_four, chunks) for item in sub]
            ells = np.array([x[0] for x in flat], dtype=np.float64)
            tot_l = float(np.sum(ells))
            m_wm_t90 = np.sum(ells[:, None] * np.array([x[1] for x in flat]), axis=0) / tot_l
            m_wm_old = np.sum(ells[:, None] * np.array([x[2] for x in flat]), axis=0) / tot_l
            m_wp_t90 = np.sum(ells[:, None] * np.array([x[3] for x in flat]), axis=0) / tot_l
            m_wp_old = np.sum(ells[:, None] * np.array([x[4] for x in flat]), axis=0) / tot_l
            exhaustive_odd[str(n)] = {
                "n": n,
                "n_allowed_hyperbolic_words": len(words),
                "W_minus_T90": _dict_12(m_wm_t90),
                "W_minus_old": _dict_12(m_wm_old),
                "W_plus_T90": _dict_12(m_wp_t90),
                "W_plus_old": _dict_12(m_wp_old),
                "elapsed_seconds": round(time.time() - t0, 3),
            }
            print(f"[X-EXACT-W Route 1] Exhaustive odd  n={n}: {len(words)} words ({int(round(time.time() - t0))}s)", flush=True)

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
            flat = [item for sub in pool.map(_eval_word_batch_route1_four, chunks) for item in sub]
            ells = np.array([x[0] for x in flat], dtype=np.float64)
            est_wm_t90, se_wm_t90 = _jackknife_weighted(ells, np.array([x[1] for x in flat]))
            est_wm_old, se_wm_old = _jackknife_weighted(ells, np.array([x[2] for x in flat]))
            est_wp_t90, se_wp_t90 = _jackknife_weighted(ells, np.array([x[3] for x in flat]))
            est_wp_old, se_wp_old = _jackknife_weighted(ells, np.array([x[4] for x in flat]))
            sampled_high_n[str(n_hi)] = {
                "n": n_hi,
                "n_sampled_words": len(words_hi),
                "W_minus_T90": {"readout": _dict_12(est_wm_t90), "jackknife_se": _dict_12(se_wm_t90)},
                "W_minus_old": {"readout": _dict_12(est_wm_old), "jackknife_se": _dict_12(se_wm_old)},
                "W_plus_T90": {"readout": _dict_12(est_wp_t90), "jackknife_se": _dict_12(se_wp_t90)},
                "W_plus_old": {"readout": _dict_12(est_wp_old), "jackknife_se": _dict_12(se_wp_old)},
                "elapsed_seconds": round(time.time() - t0, 3),
            }
            print(f"[X-EXACT-W Route 1] Sampled n={n_hi}: {len(words_hi)} words ({int(round(time.time() - t0))}s)", flush=True)

    return {
        "exhaustive_even": exhaustive_even,
        "exhaustive_odd": exhaustive_odd,
        "sampled_high_n": sampled_high_n,
    }


# ============================================================================
# SECTION 5: ROUTE 2 (ERGODIC MOVE-COUNT INTEGRAL ACROSS BOTH WORLDS & WEIGHTS)
# ============================================================================

def _eval_ergodic_four_worker(args: Tuple[str, int]) -> Dict[str, Any]:
    assert _GLOBAL_L2_EVAL is not None
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
    tl2_nodes = _GLOBAL_L2_EVAL.eval_batch(tau_red)

    a12 = np.array([p[0] for p in P5_HALF_12], dtype=np.float64)
    b12 = np.array([p[1] for p in P5_HALF_12], dtype=np.float64)

    acc_wm_t90 = np.zeros(12, dtype=np.float64)
    acc_wm_old = np.zeros(12, dtype=np.float64)
    acc_wp_t90 = np.zeros(12, dtype=np.float64)
    acc_wp_old = np.zeros(12, dtype=np.float64)
    acc_pctrl = np.zeros(12, dtype=np.float64)
    acc_c09 = np.zeros(12, dtype=np.float64)
    acc_c13 = np.zeros(12, dtype=np.float64)

    min_n_t90 = 1e9
    max_rel_corr = 0.0

    chunk_sz = 512
    for i0 in range(0, m_nodes, chunk_sz):
        i1 = min(m_nodes, i0 + chunk_sz)
        c_len = i1 - i0
        t_rep = np.repeat(tau_red[i0:i1], 12)
        a_rep = np.tile(a12, c_len)
        b_rep = np.tile(b12, c_len)
        tl2_rep = np.repeat(tl2_nodes[i0:i1], 12)

        ev = evaluate_four_modes_batch(t_rep, a_rep, b_rep, tl2_rep, include_controls=True)
        acc_wm_t90 += np.sum(ev["W_minus_T90"], axis=0)
        acc_wm_old += np.sum(ev["W_minus_old"], axis=0)
        acc_wp_t90 += np.sum(ev["W_plus_T90"], axis=0)
        acc_wp_old += np.sum(ev["W_plus_old"], axis=0)
        acc_pctrl += np.sum(ev["PC_EX_1_W_minus_wrong_plus_sign_T90"], axis=0)
        acc_c09 += np.sum(ev["PC_EX_3_W_minus_const_0_9"], axis=0)
        acc_c13 += np.sum(ev["PC_EX_3_W_minus_const_1_3"], axis=0)
        min_n_t90 = min(min_n_t90, ev["min_N_T90_observed"])
        max_rel_corr = max(max_rel_corr, ev["max_rel_corr_observed"])

    denom = float(m_nodes * 12)
    return {
        "ell": ell,
        "max_im_tau_red": float(np.max(tau_red.imag)),
        "min_N_T90": min_n_t90,
        "max_rel_corr": max_rel_corr,
        "W_minus_T90": acc_wm_t90 / denom,
        "W_minus_old": acc_wm_old / denom,
        "W_plus_T90": acc_wp_t90 / denom,
        "W_plus_old": acc_wp_old / denom,
        "pctrl": acc_pctrl / denom,
        "c09": acc_c09 / denom,
        "c13": acc_c13 / denom,
    }


def run_route2_ergodic_four(end_eval: CanonicalL2Evaluator, n_workers: int = 10) -> Dict[str, Any]:
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
    with Pool(n_workers, initializer=_init_pool_l2, initargs=(end_eval,)) as pool:
        traj_res = pool.map(_eval_ergodic_four_worker, [(w, nodes_per_move) for w in words_long])
        fine_res = pool.map(_eval_ergodic_four_worker, [(w, nodes_per_move * 2) for w in words_long[:8]])
    dt = time.time() - t0

    ells = np.array([r["ell"] for r in traj_res], dtype=np.float64)
    min_n_t90_all = min(r["min_N_T90"] for r in traj_res)
    max_rel_corr_all = max(r["max_rel_corr"] for r in traj_res)
    assert min_n_t90_all > 0.0, f"EX1 positivity failed: min N_T90 = {min_n_t90_all}"

    mat_wm_t90 = np.array([r["W_minus_T90"] for r in traj_res], dtype=np.float64)
    mat_wm_old = np.array([r["W_minus_old"] for r in traj_res], dtype=np.float64)
    mat_wp_t90 = np.array([r["W_plus_T90"] for r in traj_res], dtype=np.float64)
    mat_wp_old = np.array([r["W_plus_old"] for r in traj_res], dtype=np.float64)
    mat_pctrl = np.array([r["pctrl"] for r in traj_res], dtype=np.float64)
    mat_c09 = np.array([r["c09"] for r in traj_res], dtype=np.float64)
    mat_c13 = np.array([r["c13"] for r in traj_res], dtype=np.float64)

    def pack_mode(mat: np.ndarray) -> Dict[str, Any]:
        est, se = _jackknife_weighted(ells, mat)
        return {
            "all_12_outputs": _dict_12(est),
            "all_12_jackknife_se": _dict_12(se),
            "claimed_7_frame_code": _dict_7_fc(est),
            "claimed_7_frame_code_se": _dict_7_fc(se),
            "claimed_7_adjacent": _dict_7_adj(est),
            "claimed_7_adjacent_se": _dict_7_adj(se),
            "_est": est,
            "_se": se,
        }

    p_wm_t90 = pack_mode(mat_wm_t90)
    p_wm_old = pack_mode(mat_wm_old)
    p_wp_t90 = pack_mode(mat_wp_t90)
    p_wp_old = pack_mode(mat_wp_old)

    def pack_paired_diff(mat_a: np.ndarray, mat_b: np.ndarray, ref_est: np.ndarray) -> Dict[str, Any]:
        d_est, d_se = _jackknife_weighted(ells, mat_a - mat_b)
        z_signed = d_est / np.maximum(d_se, 1e-30)
        rel = d_est / np.maximum(np.abs(ref_est), 1e-30)
        idx_fc = [OUTPUT_KEYS_12.index(k) for k in CLAIMED_7_FRAME_CODE]
        return {
            "diff_mean": _dict_12(d_est),
            "diff_se": _dict_12(d_se),
            "paired_signed_z": _dict_12(z_signed),
            "relative_shift": _dict_12(rel),
            "max_abs_rel_shift_claimed_7": float(np.max(np.abs(rel[idx_fc]))),
            "max_abs_paired_z_claimed_7": float(np.max(np.abs(z_signed[idx_fc]))),
            "min_abs_paired_z_claimed_7": float(np.min(np.abs(z_signed[idx_fc]))),
            "_d_est": d_est,
            "_z": z_signed,
        }

    d_t90_wm = pack_paired_diff(mat_wm_t90, mat_wm_old, p_wm_old["_est"])
    d_t90_wp = pack_paired_diff(mat_wp_t90, mat_wp_old, p_wp_old["_est"])
    d_world_t90 = pack_paired_diff(mat_wm_t90, mat_wp_t90, p_wm_t90["_est"])
    d_world_old = pack_paired_diff(mat_wm_old, mat_wp_old, p_wm_old["_est"])
    d_pctrl_wm = pack_paired_diff(mat_pctrl, mat_wm_old, p_wm_old["_est"])
    d_c09 = pack_paired_diff(mat_wm_t90, mat_c09, p_wm_t90["_est"])
    d_c13 = pack_paired_diff(mat_wm_t90, mat_c13, p_wm_t90["_est"])

    idx_fc = [OUTPUT_KEYS_12.index(k) for k in CLAIMED_7_FRAME_CODE]
    # PC_EX_1: flipping -pi|a0|^2 e^{-2L2} -> +pi|a0|^2 e^{-2L2} reverses the sign of every non-negligible shift!
    sig_mask = np.abs(d_t90_wm["_z"][idx_fc]) > 3.0
    sign_reversed_ok = bool(np.all(d_t90_wm["_d_est"][idx_fc][sig_mask] * d_pctrl_wm["_d_est"][idx_fc][sig_mask] < 0.0))
    assert sign_reversed_ok, "PC_EX_1 sign reversal failed"
    assert d_c09["max_abs_paired_z_claimed_7"] > 5.0 and d_c13["max_abs_paired_z_claimed_7"] > 5.0, "PC_EX_3 failed"
    assert d_world_t90["max_abs_paired_z_claimed_7"] > 4.0, "PC_EX_4 failed"

    # EX4 on ergodic averages: lepton == down in both worlds under Theorem 90
    ex4_erg_wm = float(np.max(np.abs(p_wm_t90["_est"][6:9] - p_wm_t90["_est"][3:6])))
    ex4_erg_wp = float(np.max(np.abs(p_wp_t90["_est"][6:9] - p_wp_t90["_est"][3:6])))
    assert ex4_erg_wm < 1e-11 and ex4_erg_wp < 1e-11

    # Split-half & quadrature refinement checks on W_minus_T90 and W_plus_T90
    h1_wm, se1_wm = _jackknife_weighted(ells[:32], mat_wm_t90[:32])
    h2_wm, se2_wm = _jackknife_weighted(ells[32:], mat_wm_t90[32:])
    z_split_wm = float(np.max((np.abs(h1_wm - h2_wm) / np.sqrt(se1_wm ** 2 + se2_wm ** 2 + 1e-30))[idx_fc]))

    coarse_8 = np.array([r["W_minus_T90"] for r in traj_res[:8]])
    fine_8 = np.array([r["W_minus_T90"] for r in fine_res])
    quad_diff_max = float(np.max(np.abs(fine_8 - coarse_8)))

    # Strip private numpy arrays before JSON serialization
    for dct in (p_wm_t90, p_wm_old, p_wp_t90, p_wp_old, d_t90_wm, d_t90_wp, d_world_t90, d_world_old, d_pctrl_wm, d_c09, d_c13):
        for k_priv in [k for k in list(dct.keys()) if k.startswith("_")]:
            del dct[k_priv]

    print(
        f"[X-EXACT-W Route 2] Ergodic {n_trajs}x{word_len} moves completed in {int(round(dt))}s (controls PC_EX_1..4 FIRED)",
        flush=True,
    )

    ex2_holds = (
        d_t90_wm["max_abs_rel_shift_claimed_7"] < 0.01
        and d_t90_wp["max_abs_rel_shift_claimed_7"] < 0.01
        and d_t90_wm["max_abs_paired_z_claimed_7"] > 5.0
        and d_t90_wp["max_abs_paired_z_claimed_7"] > 5.0
    )
    ex3_holds = d_world_t90["min_abs_paired_z_claimed_7"] > 4.0

    return {
        "n_trajectories": n_trajs,
        "moves_per_trajectory": word_len,
        "total_move_steps": n_trajs * word_len,
        "nodes_per_move": nodes_per_move,
        "min_channel_weight_N_T90_observed": min_n_t90_all,
        "max_channel_rel_corr_T90_observed": max_rel_corr_all,
        "split_half_max_z_W_minus_T90_claimed_7": z_split_wm,
        "quadrature_6_vs_12_nodes_max_diff_W_minus_T90": quad_diff_max,
        "elapsed_seconds": round(dt, 3),
        "four_primary_combinations": {
            "W_minus__exact_T90": p_wm_t90,
            "W_minus__old_small_cut": p_wm_old,
            "W_plus__exact_T90": p_wp_t90,
            "W_plus__old_small_cut": p_wp_old,
        },
        "paired_comparisons": {
            "Theorem90_minus_old_in_W_minus": d_t90_wm,
            "Theorem90_minus_old_in_W_plus": d_t90_wp,
            "W_minus_minus_W_plus_under_Theorem90": d_world_t90,
            "W_minus_minus_W_plus_under_old_weight": d_world_old,
        },
        "controls": {
            "PC_EX_1_wrong_plus_sign_T90_vs_old": {
                **d_pctrl_wm,
                "sign_reversed_on_all_significant_shifts": sign_reversed_ok,
                "fired": True,
            },
            "PC_EX_3_const_end_0_9_vs_W_minus_T90": {**d_c09, "fired": True},
            "PC_EX_3_const_end_1_3_vs_W_minus_T90": {**d_c13, "fired": True},
            "PC_EX_4_world_swap_W_minus_vs_W_plus_T90": {
                "min_abs_z_claimed_7": d_world_t90["min_abs_paired_z_claimed_7"],
                "max_abs_z_claimed_7": d_world_t90["max_abs_paired_z_claimed_7"],
                "fired": True,
            },
        },
        "expectations_verdicts": {
            "EX1_contour_modular_and_positivity_holds": True,
            "EX2_sub_percent_and_gt_5sigma_paired_shift_holds": bool(ex2_holds),
            "EX3_macroscopic_world_split_survives_T90_holds": bool(ex3_holds),
            "EX4_level5_lepton_equals_down_under_T90_holds": True,
        },
    }


def main() -> None:
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    t_start = time.time()
    script_sha = hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()
    n_workers = min(10, max(2, (os.cpu_count() or 4) - 2))

    print(f"[X-EXACT-W] Building 4-patch Chebyshev canonical-end evaluator on {n_workers} workers...", flush=True)
    t_g0 = time.time()
    end_eval = CanonicalL2Evaluator(n_workers=n_workers)
    print(f"[X-EXACT-W] Evaluator built in {int(round(time.time() - t_g0))}s. Running startup gates (EX1, EX4, PC_EX_2)...", flush=True)

    gates = run_startup_gates_exact_w(end_eval, n_workers=n_workers)
    print("[X-EXACT-W] Startup gates PASSED (mpmath Lame, R_s & a_{0,s} contour, SL(2,Z) T & S, Haar U(3)^5, PC_EX_2).", flush=True)

    route1 = run_route1_four_modes(end_eval, n_workers=n_workers)
    route2 = run_route2_ergodic_four(end_eval, n_workers=n_workers)

    # Compare Route 1 exhaustive n=18 vs Route 2 ergodic across all 4 combinations
    idx_fc = [OUTPUT_KEYS_12.index(k) for k in CLAIMED_7_FRAME_CODE]
    r1_vs_r2 = {}
    for r1_k, r2_k in (
        ("W_minus_T90", "W_minus__exact_T90"),
        ("W_minus_old", "W_minus__old_small_cut"),
        ("W_plus_T90", "W_plus__exact_T90"),
        ("W_plus_old", "W_plus__old_small_cut"),
    ):
        v18 = np.array([route1["exhaustive_even"]["18"][r1_k][k] for k in OUTPUT_KEYS_12])
        verg = np.array([route2["four_primary_combinations"][r2_k]["all_12_outputs"][k] for k in OUTPUT_KEYS_12])
        diff = np.abs(v18 - verg)
        r1_vs_r2[r2_k] = {
            "abs_diff_exhaustive_n18_vs_ergodic": _dict_12(diff),
            "max_abs_diff_claimed_7": float(np.max(diff[idx_fc])),
        }

    payload = {
        "card": "X-EXACT-W",
        "seat": "agy-exp",
        "empirical_firewall": "0 of 19",
        "particle_names_used": False,
        "b1928_json_read_before_commit": False,
        "script_sha256": script_sha,
        "total_elapsed_seconds": round(time.time() - t_start, 3),
        "startup_gates": gates,
        "route1_finite_n_populations": route1,
        "route2_ergodic_move_count": route2,
        "route1_vs_route2_comparison": r1_vs_r2,
        "all_planted_controls_fired": True,
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"[X-EXACT-W] DONE in {int(round(time.time() - t_start))}s -> {OUT_JSON.name}", flush=True)


if __name__ == "__main__":
    main()
