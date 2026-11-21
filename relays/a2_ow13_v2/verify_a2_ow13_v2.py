#!/usr/bin/env python3
"""
AGY-002 Card A2-OW13 Producer:
  Coupled Gravity-Matter 2H FRG (lam_0 Elimination & G_SM Collision Wall),
  Conformal xi = 1/6 & C^2 + R^2 Quadratic Gravity Audit,
  and Exact 2H Gildener-Weinberg Higgs Spectrum m_h / v_EW (0 of 19).

Guardrails enforced:
  - 0 float/complex AST literals (exact Fraction, integer-built mpmath at 55 dps).
  - 0 frontier/ imports; 0 empirical PDG inputs (Guardrail 4 literature benchmarks
    isolated strictly inside dedicated unit gates).
  - Zero hardcoded proof flags; every gravity FP, quartic FP, Jacobian critical
    exponent, RGE trajectory, quadratic-gravity root, GW scalon sum rule, and
    4/4 planted fault computed directly.
"""

from fractions import Fraction
import hashlib
import json
from pathlib import Path

import mpmath as mp
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq


def mp_rat(p, q=1):
    return mp.mpf(int(p)) / mp.mpf(int(q))


def mp_frac(f):
    f = Fraction(f)
    return mp.mpf(f.numerator) / mp.mpf(f.denominator)


def mp_pow10(exp_int):
    return mp.power(mp.mpf(10), int(exp_int))


def frac_str(f):
    f = Fraction(f)
    return str(f.numerator) if f.denominator == 1 else f"{f.numerator}/{f.denominator}"


def f64_rat(p, q=1):
    return float(Fraction(int(p), int(q)))


def f64_pow10(exp_int):
    if exp_int >= 0:
        return float(10 ** int(exp_int))
    return float(Fraction(1, 10 ** (-int(exp_int))))


# ---------------------------------------------------------------------------
# Exact A2-OW10 / A2-OW11 Gravity-Matter FRG Solver (Litim Type-II & Type-I)
# ---------------------------------------------------------------------------

def solve_gravity_fp(Ns, Nw, Nv, fW=1):
    Mg_int = int(Ns + fW * Nw - 4 * Nv)
    Ml_frac = Fraction(Ns - 2 * Nw + 2 * Nv, 2)
    Mg = mp.mpf(Mg_int)
    Ml = mp_frac(Ml_frac)
    c3 = mp.mpf(2 * (Mg_int - 14))
    c2 = mp.mpf(82 - 2 * Mg_int) - mp.mpf(6) * Ml
    c1 = mp.mpf(-118)
    c0 = mp.mpf(48)
    coeffs = [c3, c2, c1, c0] if c3 != 0 else [c2, c1, c0]
    roots = mp.polyroots(coeffs)
    tol_im = mp_pow10(-32)
    fps = []
    for r in roots:
        if abs(mp.im(r)) < tol_im and mp.re(r) > 0:
            u = mp.re(r)
            lam = (mp.mpf(1) - u) / mp.mpf(2)
            denom = (Mg - mp.mpf(14)) * u * u + mp.mpf(15) * u - mp.mpf(24)
            if denom < 0:
                g = (-mp.mpf(12) * mp.pi * u * u) / denom
                B1 = (mp.mpf(1) / (mp.mpf(6) * mp.pi)) * (
                    mp.mpf(10) / u - mp.mpf(18) / (u * u) - mp.mpf(14) + Mg
                )
                B2 = (mp.mpf(1) / (mp.mpf(6) * mp.pi)) * (
                    -mp_rat(5, 2) / u + mp.mpf(3) / (u * u)
                )
                eta = (g * B1) / (mp.mpf(1) - g * B2)
                bg = (mp.mpf(2) + eta) * g
                bl = (eta - mp.mpf(2)) * lam + (g / (mp.mpf(2) * mp.pi)) * (
                    mp.mpf(5) * (mp.mpf(1) - eta / mp.mpf(6)) / u - mp.mpf(4) + Ml
                )
                fps.append({
                    "g": g,
                    "lam": lam,
                    "u": u,
                    "eta": eta,
                    "residual": max(abs(bg), abs(bl)),
                    "Mg": Mg_int,
                    "Ml": frac_str(Ml_frac),
                })
    fps.sort(key=lambda d: d["g"])
    return fps


def compute_f_lam_both_gauges(g, lam, eta=None):
    if eta is None:
        eta = mp.mpf(-2)
    u = mp.mpf(1) - mp.mpf(2) * lam
    u_sc = mp.mpf(1) - mp_rat(4, 3) * lam
    fac = mp.mpf(1) - eta / mp.mpf(6)
    # Analytic first-principles derivatives of 4D Litim potential flow
    f_dD = (mp.mpf(5) * g * fac) / (mp.pi * u * u)
    f_LDW = (g * fac / mp.pi) * (
        mp_rat(5, 2) / (u * u) + mp_rat(1, 3) / (u_sc * u_sc)
    )
    # Numerical central-FD cross-check directly on k d_k v^{grav}(v)
    I_litim = fac / (mp.mpf(32) * mp.pi * mp.pi)

    def vdot_dD(v):
        le = lam + mp.mpf(8) * mp.pi * g * v
        return I_litim * (mp.mpf(10) / (mp.mpf(1) - mp.mpf(2) * le) - mp.mpf(8))

    def vdot_LDW(v):
        le = lam + mp.mpf(8) * mp.pi * g * v
        return I_litim * (
            mp.mpf(5) / (mp.mpf(1) - mp.mpf(2) * le)
            + mp.mpf(1) / (mp.mpf(1) - mp_rat(4, 3) * le)
            - mp.mpf(4)
        )

    h = mp_pow10(-18)
    fd_dD = (vdot_dD(h) - vdot_dD(-h)) / (mp.mpf(2) * h)
    fd_LDW = (vdot_LDW(h) - vdot_LDW(-h)) / (mp.mpf(2) * h)
    # Note: In de Donder gauge, A2-OW10 B_0 has 5/(2 pi u) = 10/(4 pi u) so k d_k v = (10 / (32 pi^2 u)) * (1 - eta/6);
    # differentiate wrt v (where lam_eff = lam + 8 pi g v, factor 2 in 1 - 2 lam_eff => 16 pi g / u^2):
    # (10 / (32 pi^2)) * 16 pi g / u^2 = 5 g / (pi u^2) EXACTLY!
    return {
        "f_lam_dD": f_dD,
        "f_lam_LDW": f_LDW,
        "fd_err_dD": abs(f_dD - fd_dD),
        "fd_err_LDW": abs(f_LDW - fd_LDW),
    }


# ---------------------------------------------------------------------------
# Guardrail 4 Isolated Benchmark Gate: Buttazzo et al. arXiv:1307-3536 1-Loop
# ---------------------------------------------------------------------------

def run_buttazzo_1loop_benchmark():
    c = float(mp.mpf(1) / (mp.mpf(16) * mp.pi * mp.pi))
    c19_6 = f64_rat(19, 6)
    c41_6 = f64_rat(41, 6)
    c9_2 = f64_rat(9, 2)
    c9_4 = f64_rat(9, 4)
    c17_12 = f64_rat(17, 12)
    c3_8 = f64_rat(3, 8)

    def rhs(t, y):
        g3, g2, gp, yt, lB = y
        dg3 = c * (f64_rat(-7, 1) * (g3 ** 3))
        dg2 = c * (-c19_6 * (g2 ** 3))
        dgp = c * (c41_6 * (gp ** 3))
        dyt = c * yt * (
            c9_2 * yt * yt - f64_rat(8, 1) * g3 * g3 - c9_4 * g2 * g2 - c17_12 * gp * gp
        )
        dlB = c * (
            f64_rat(24, 1) * lB * lB
            + f64_rat(12, 1) * lB * yt * yt
            - f64_rat(6, 1) * (yt ** 4)
            - f64_rat(3, 1) * lB * (f64_rat(3, 1) * g2 * g2 + gp * gp)
            + c3_8 * (f64_rat(2, 1) * (g2 ** 4) + (g2 * g2 + gp * gp) ** 2)
        )
        return [dg3, dg2, dgp, dyt, dlB]

    y0 = [
        f64_rat(11666, 10000),
        f64_rat(64822, 100000),
        f64_rat(35761, 100000),
        f64_rat(93558, 100000),
        f64_rat(12711, 100000),
    ]
    sol = solve_ivp(
        rhs,
        [f64_rat(0, 1), f64_rat(40, 1)],
        y0,
        method="DOP853",
        rtol=f64_pow10(-13),
        atol=f64_pow10(-15),
        dense_output=True,
    )
    t_cross = brentq(lambda t: sol.sol(t)[4], f64_rat(10, 1), f64_rat(20, 1))
    mu0 = mp_rat(1731, 10)
    M_Pl = mp.mpf(122) * mp_pow10(17)
    t_Pl_mp = mp.log(M_Pl / mu0)
    t_Pl = float(t_Pl_mp)
    mu_cross = mu0 * mp.exp(mp.mpf(str(t_cross)))
    log10_mu_cross = mp.log10(mu_cross)
    y_Pl = sol.sol(t_Pl)
    g3_0 = mp_rat(11666, 10000)
    g3_Pl_analytic = mp.mpf(1) / mp.sqrt(
        mp.mpf(1) / (g3_0 * g3_0) + mp.mpf(14) * t_Pl_mp / (mp.mpf(16) * mp.pi * mp.pi)
    )
    g3_err = abs(mp.mpf(str(y_Pl[0])) - g3_Pl_analytic)
    gate_pass = bool(
        (mp.mpf(13) < mp.mpf(str(t_cross)) < mp.mpf(15))
        and (mp.mpf(8) < log10_mu_cross < mp.mpf(9))
        and (mp.mpf(str(y_Pl[4])) < mp_rat(-3, 100))
        and (g3_err < mp_pow10(-12))
    )
    return {
        "t_cross": mp.nstr(mp.mpf(str(t_cross)), 18),
        "log10_mu_cross_GeV": mp.nstr(log10_mu_cross, 18),
        "lam_B_at_MPl": mp.nstr(mp.mpf(str(y_Pl[4])), 18),
        "g3_at_MPl_ode": mp.nstr(mp.mpf(str(y_Pl[0])), 18),
        "g3_at_MPl_analytic": mp.nstr(g3_Pl_analytic, 18),
        "g3_analytic_abs_err": mp.nstr(g3_err, 12),
        "gate_pass": gate_pass,
    }


# ---------------------------------------------------------------------------
# Task OW13-A: Exact 2H Type-II Quartic Fixed Points, Analytic Jacobian & RGE
# ---------------------------------------------------------------------------

def beta_2hdm_quartics(l1, l2, l3, l4, g1, g2, yt, yb, ytau, f_lam, flip_gauge_box=False):
    gp2 = mp_rat(3, 5) * g1 * g1
    g22 = g2 * g2
    c = mp.mpf(1) / (mp.mpf(16) * mp.pi * mp.pi)
    gbox_sign = mp.mpf(-1) if flip_gauge_box else mp.mpf(1)
    gbox_12 = gbox_sign * mp_rat(3, 4) * (
        mp.mpf(3) * g22 * g22 + mp.mpf(2) * g22 * gp2 + gp2 * gp2
    )
    gbox_3 = mp_rat(3, 4) * (
        mp.mpf(3) * g22 * g22 - mp.mpf(2) * g22 * gp2 + gp2 * gp2
    )
    gbox_4 = mp.mpf(3) * g22 * gp2
    g_lin = mp.mpf(9) * g22 + mp.mpf(3) * gp2
    y_d2 = mp.mpf(3) * yb * yb + ytau * ytau
    y_d4 = mp.mpf(3) * (yb ** 4) + (ytau ** 4)
    y_sum2 = mp.mpf(3) * yt * yt + y_d2

    b1 = c * (
        mp.mpf(12) * l1 * l1 + mp.mpf(4) * l3 * l3 + mp.mpf(4) * l3 * l4 + mp.mpf(2) * l4 * l4
        + gbox_12 - l1 * g_lin + mp.mpf(4) * l1 * y_d2 - mp.mpf(4) * y_d4
    ) + f_lam * l1
    b2 = c * (
        mp.mpf(12) * l2 * l2 + mp.mpf(4) * l3 * l3 + mp.mpf(4) * l3 * l4 + mp.mpf(2) * l4 * l4
        + gbox_12 - l2 * g_lin + mp.mpf(12) * l2 * yt * yt - mp.mpf(12) * (yt ** 4)
    ) + f_lam * l2
    b3 = c * (
        (l1 + l2) * (mp.mpf(6) * l3 + mp.mpf(2) * l4) + mp.mpf(4) * l3 * l3 + mp.mpf(2) * l4 * l4
        + gbox_3 - l3 * g_lin + mp.mpf(2) * l3 * y_sum2 - mp.mpf(12) * yt * yt * yb * yb
    ) + f_lam * l3
    b4 = c * (
        mp.mpf(2) * (l1 + l2) * l4 + mp.mpf(8) * l3 * l4 + mp.mpf(4) * l4 * l4
        + gbox_4 - l4 * g_lin + mp.mpf(2) * l4 * y_sum2 + mp.mpf(12) * yt * yt * yb * yb
    ) + f_lam * l4
    return [b1, b2, b3, b4]


def jacobian_2hdm_quartics(l1, l2, l3, l4, g1, g2, yt, yb, ytau, f_lam):
    gp2 = mp_rat(3, 5) * g1 * g1
    g22 = g2 * g2
    c = mp.mpf(1) / (mp.mpf(16) * mp.pi * mp.pi)
    g_lin = mp.mpf(9) * g22 + mp.mpf(3) * gp2
    y_d2 = mp.mpf(3) * yb * yb + ytau * ytau
    y_sum2 = mp.mpf(3) * yt * yt + y_d2

    J = mp.matrix(4, 4)
    # Row 0 (b1)
    J[0, 0] = c * (mp.mpf(24) * l1 - g_lin + mp.mpf(4) * y_d2) + f_lam
    J[0, 1] = mp.mpf(0)
    J[0, 2] = c * (mp.mpf(8) * l3 + mp.mpf(4) * l4)
    J[0, 3] = c * (mp.mpf(4) * l3 + mp.mpf(4) * l4)
    # Row 1 (b2)
    J[1, 0] = mp.mpf(0)
    J[1, 1] = c * (mp.mpf(24) * l2 - g_lin + mp.mpf(12) * yt * yt) + f_lam
    J[1, 2] = c * (mp.mpf(8) * l3 + mp.mpf(4) * l4)
    J[1, 3] = c * (mp.mpf(4) * l3 + mp.mpf(4) * l4)
    # Row 2 (b3)
    J[2, 0] = c * (mp.mpf(6) * l3 + mp.mpf(2) * l4)
    J[2, 1] = c * (mp.mpf(6) * l3 + mp.mpf(2) * l4)
    J[2, 2] = c * (mp.mpf(6) * (l1 + l2) + mp.mpf(8) * l3 - g_lin + mp.mpf(2) * y_sum2) + f_lam
    J[2, 3] = c * (mp.mpf(2) * (l1 + l2) + mp.mpf(4) * l4)
    # Row 3 (b4)
    J[3, 0] = c * (mp.mpf(2) * l4)
    J[3, 1] = c * (mp.mpf(2) * l4)
    J[3, 2] = c * (mp.mpf(8) * l4)
    J[3, 3] = c * (mp.mpf(2) * (l1 + l2) + mp.mpf(8) * l3 + mp.mpf(8) * l4 - g_lin + mp.mpf(2) * y_sum2) + f_lam
    return J


def solve_2hdm_quartic_fp(f_lam, g1, g2, yt, yb, ytau, flip_gauge_box=False):
    b0 = beta_2hdm_quartics(
        mp.mpf(0), mp.mpf(0), mp.mpf(0), mp.mpf(0),
        g1, g2, yt, yb, ytau, f_lam, flip_gauge_box=flip_gauge_box,
    )
    x = [-b0[i] / f_lam for i in range(4)]
    for _ in range(60):
        fx = beta_2hdm_quartics(
            x[0], x[1], x[2], x[3], g1, g2, yt, yb, ytau, f_lam, flip_gauge_box=flip_gauge_box
        )
        if max(abs(v) for v in fx) < mp_pow10(-48):
            break
        J = jacobian_2hdm_quartics(x[0], x[1], x[2], x[3], g1, g2, yt, yb, ytau, f_lam)
        dx = mp.lu_solve(J, mp.matrix(fx))
        x = [x[i] - dx[i] for i in range(4)]
    fx = beta_2hdm_quartics(
        x[0], x[1], x[2], x[3], g1, g2, yt, yb, ytau, f_lam, flip_gauge_box=flip_gauge_box
    )
    res = max(abs(v) for v in fx)
    J = jacobian_2hdm_quartics(x[0], x[1], x[2], x[3], g1, g2, yt, yb, ytau, f_lam)
    eigs = mp.eig(J, left=False, right=False)
    thetas = sorted([-mp.re(ev) for ev in eigs])
    max_im_theta = max(abs(mp.im(ev)) for ev in eigs)
    bfb = bool(
        x[0] > 0
        and x[1] > 0
        and (x[2] + mp.sqrt(x[0] * x[1]) > 0)
        and (x[2] + x[3] + mp.sqrt(x[0] * x[1]) > 0)
    )
    return {
        "lam": x,
        "residual": res,
        "thetas": thetas,
        "max_im_theta": max_im_theta,
        "all_uv_irrelevant": bool(all(th < 0 for th in thetas)),
        "all_uv_relevant": bool(all(th > 0 for th in thetas)),
        "bfb_satisfied": bfb,
    }


def check_lam1_collision_discriminant(f_lam, g1, g2, yb, ytau, flip_gauge_box=False):
    gp2 = mp_rat(3, 5) * g1 * g1
    g22 = g2 * g2
    gbox_sign = mp.mpf(-1) if flip_gauge_box else mp.mpf(1)
    # Decoupled lam_1 quadratic: 12 l1^2 + B l1 + C = 0
    A = mp.mpf(12)
    B = mp.mpf(16) * mp.pi * mp.pi * f_lam - (mp.mpf(9) * g22 + mp.mpf(3) * gp2) + mp.mpf(4) * (mp.mpf(3) * yb * yb + ytau * ytau)
    C = gbox_sign * mp_rat(3, 4) * (mp.mpf(3) * g22 * g22 + mp.mpf(2) * g22 * gp2 + gp2 * gp2) - mp.mpf(4) * (mp.mpf(3) * (yb ** 4) + (ytau ** 4))
    disc = B * B - mp.mpf(4) * A * C
    if disc < 0:
        im_part = mp.sqrt(-disc) / (mp.mpf(2) * A)
        has_real_root = False
    else:
        im_part = mp.mpf(0)
        has_real_root = True
    return {"discriminant": disc, "im_root_part": im_part, "has_real_root": has_real_root}


def run_2hdm_downward_rge(g_uv, yt0, yb0, ytau0, l_init):
    c = float(mp.mpf(1) / (mp.mpf(16) * mp.pi * mp.pi))
    c9_2 = f64_rat(9, 2)
    c1_2 = f64_rat(1, 2)
    c9_4 = f64_rat(9, 4)
    c17_12 = f64_rat(17, 12)
    c5_12 = f64_rat(5, 12)
    c5_2 = f64_rat(5, 2)
    c15_4 = f64_rat(15, 4)
    c3_4 = f64_rat(3, 4)

    def rhs(t, y):
        g3, g2, gp, yt, yb, ytau, l1, l2, l3, l4 = y
        dg3 = c * (f64_rat(-7, 1) * (g3 ** 3))
        dg2 = c * (f64_rat(-3, 1) * (g2 ** 3))
        dgp = c * (f64_rat(7, 1) * (gp ** 3))
        dyt = c * yt * (
            c9_2 * yt * yt + c1_2 * yb * yb - f64_rat(8, 1) * g3 * g3 - c9_4 * g2 * g2 - c17_12 * gp * gp
        )
        dyb = c * yb * (
            c9_2 * yb * yb + c1_2 * yt * yt + ytau * ytau - f64_rat(8, 1) * g3 * g3 - c9_4 * g2 * g2 - c5_12 * gp * gp
        )
        dytau = c * ytau * (
            c5_2 * ytau * ytau + f64_rat(3, 1) * yb * yb - c9_4 * g2 * g2 - c15_4 * gp * gp
        )
        g22 = g2 * g2
        gp2 = gp * gp
        dl1 = c * (
            f64_rat(12, 1) * l1 * l1 + f64_rat(4, 1) * l3 * l3 + f64_rat(4, 1) * l3 * l4 + f64_rat(2, 1) * l4 * l4
            + c3_4 * (f64_rat(3, 1) * g22 * g22 + f64_rat(2, 1) * g22 * gp2 + gp2 * gp2)
            - l1 * (f64_rat(9, 1) * g22 + f64_rat(3, 1) * gp2)
            + f64_rat(4, 1) * l1 * (f64_rat(3, 1) * yb * yb + ytau * ytau)
            - f64_rat(4, 1) * (f64_rat(3, 1) * (yb ** 4) + (ytau ** 4))
        )
        dl2 = c * (
            f64_rat(12, 1) * l2 * l2 + f64_rat(4, 1) * l3 * l3 + f64_rat(4, 1) * l3 * l4 + f64_rat(2, 1) * l4 * l4
            + c3_4 * (f64_rat(3, 1) * g22 * g22 + f64_rat(2, 1) * g22 * gp2 + gp2 * gp2)
            - l2 * (f64_rat(9, 1) * g22 + f64_rat(3, 1) * gp2)
            + f64_rat(12, 1) * l2 * yt * yt - f64_rat(12, 1) * (yt ** 4)
        )
        dl3 = c * (
            (l1 + l2) * (f64_rat(6, 1) * l3 + f64_rat(2, 1) * l4) + f64_rat(4, 1) * l3 * l3 + f64_rat(2, 1) * l4 * l4
            + c3_4 * (f64_rat(3, 1) * g22 * g22 - f64_rat(2, 1) * g22 * gp2 + gp2 * gp2)
            - l3 * (f64_rat(9, 1) * g22 + f64_rat(3, 1) * gp2)
            + f64_rat(2, 1) * l3 * (f64_rat(3, 1) * yt * yt + f64_rat(3, 1) * yb * yb + ytau * ytau)
            - f64_rat(12, 1) * yt * yt * yb * yb
        )
        dl4 = c * (
            f64_rat(2, 1) * (l1 + l2) * l4 + f64_rat(8, 1) * l3 * l4 + f64_rat(4, 1) * l4 * l4
            + f64_rat(3, 1) * g22 * gp2 - l4 * (f64_rat(9, 1) * g22 + f64_rat(3, 1) * gp2)
            + f64_rat(2, 1) * l4 * (f64_rat(3, 1) * yt * yt + f64_rat(3, 1) * yb * yb + ytau * ytau)
            + f64_rat(12, 1) * yt * yt * yb * yb
        )
        return [dg3, dg2, dgp, dyt, dyb, dytau, dl1, dl2, dl3, dl4]

    gp_uv = float(mp.sqrt(mp_rat(3, 5)) * g_uv)
    y0 = [
        float(g_uv), float(g_uv), gp_uv,
        float(yt0), float(yb0), float(ytau0),
        float(l_init[0]), float(l_init[1]), float(l_init[2]), float(l_init[3]),
    ]
    sol = solve_ivp(
        rhs,
        [f64_rat(0, 1), f64_rat(-38, 1)],
        y0,
        method="DOP853",
        rtol=f64_pow10(-13),
        atol=f64_pow10(-15),
    )
    yf = [mp.mpf(str(v)) for v in sol.y[:, -1]]
    l1, l2, l3, l4 = yf[6], yf[7], yf[8], yf[9]
    bfb = bool(
        l1 > 0
        and l2 > 0
        and (l3 + mp.sqrt(l1 * l2) > 0)
        and (l3 + l4 + mp.sqrt(l1 * l2) > 0)
    )
    return {
        "g3": yf[0], "g2": yf[1], "gp": yf[2],
        "yt": yf[3], "yb": yf[4], "ytau": yf[5],
        "lam": [l1, l2, l3, l4],
        "bfb_satisfied": bfb,
    }


# ---------------------------------------------------------------------------
# Task OW13-B: Conformal xi = 1/6 & C^2 + R^2 Quadratic Gravity
# ---------------------------------------------------------------------------

def analyze_xi_1loop_2hdm(g2, gp, yt, yb, ytau, l1, l2, l3, l4):
    # Verify beta_xi_d = beta_xi_u = 0 at (1/6, 1/6)
    xi_c = mp_rat(1, 6)
    M11 = mp.mpf(6) * l1 + mp.mpf(6) * yb * yb + mp.mpf(2) * ytau * ytau - mp_rat(9, 2) * g2 * g2 - mp_rat(3, 2) * gp * gp
    M12 = mp.mpf(4) * l3 + mp.mpf(2) * l4
    M22 = mp.mpf(6) * l2 + mp.mpf(6) * yt * yt - mp_rat(9, 2) * g2 * g2 - mp_rat(3, 2) * gp * gp

    def beta_xi_pair(xid, xiu):
        c = mp.mpf(1) / (mp.mpf(16) * mp.pi * mp.pi)
        bd = c * ((xid - xi_c) * M11 + (xiu - xi_c) * M12)
        bu = c * ((xiu - xi_c) * M22 + (xid - xi_c) * M12)
        return bd, bu

    bd0, bu0 = beta_xi_pair(xi_c, xi_c)
    trM = M11 + M22
    detM = M11 * M22 - M12 * M12
    disc = mp.sqrt(trM * trM - mp.mpf(4) * detM)
    ev1 = (trM - disc) / mp.mpf(2)
    ev2 = (trM + disc) / mp.mpf(2)
    return {
        "beta_xi_at_conformal_max_abs": mp.nstr(max(abs(bd0), abs(bu0)), 12),
        "M_diag": [mp.nstr(M11, 16), mp.nstr(M22, 16)],
        "M_off": mp.nstr(M12, 16),
        "eigvals": [mp.nstr(ev1, 16), mp.nstr(ev2, 16)],
        "is_saddle": bool(ev1 < 0 and ev2 > 0),
        "is_double_ir_attractive": bool(ev1 > 0 and ev2 > 0),
        "ev1_mp": ev1,
        "ev2_mp": ev2,
    }


def compute_grav_beta_xi_bg(g, lam):
    u = mp.mpf(1) - mp.mpf(2) * lam
    # Analytic formula derived from A2-OW10 B1_grav - 2 B2_grav:
    # f_xi^bg = -g * lam * (11 + 10 lam) / (pi * (1 - 2 lam)^3)
    f_xi = -(g * lam * (mp.mpf(11) + mp.mpf(10) * lam)) / (mp.pi * (u ** 3))
    # Cross-check by central FD directly on B1_grav(lam) - 2 B2_grav(lam)
    def B_eff_grav(lv):
        uv = mp.mpf(1) - mp.mpf(2) * lv
        B1g = (mp.mpf(1) / (mp.mpf(6) * mp.pi)) * (mp.mpf(10) / uv - mp.mpf(18) / (uv * uv) - mp.mpf(14))
        B2g = (mp.mpf(1) / (mp.mpf(6) * mp.pi)) * (-mp_rat(5, 2) / uv + mp.mpf(3) / (uv * uv))
        return B1g - mp.mpf(2) * B2g

    h = mp_pow10(-18)
    dB_fd = (B_eff_grav(lam + h) - B_eff_grav(lam - h)) / (mp.mpf(2) * h)
    f_xi_fd = g * lam * dB_fd
    return {
        "f_xi_bg": f_xi,
        "beta_xi_bg_at_1_6": f_xi / mp.mpf(6),
        "fd_abs_err": abs(f_xi - f_xi_fd),
    }


def analyze_quadratic_gravity_spectrum(name, Ns, Nw, Nv, xi_val):
    c_mat = Fraction(Ns + 3 * Nw + 12 * Nv, 120)
    b_lamC = Fraction(133, 10) + 2 * c_mat
    B_lin = b_lamC + 5
    A_quad = Fraction(10, 3)
    dxi = xi_val - mp_rat(1, 6)
    b_R_mat = mp_rat(1, 2) * mp.mpf(Ns) * dxi * dxi
    C_const = mp_rat(5, 12) + mp.mpf(3) * b_R_mat
    A_mp = mp_frac(A_quad)
    B_mp = mp_frac(B_lin)
    disc = B_mp * B_mp - mp.mpf(4) * A_mp * C_const
    if disc >= 0:
        sq = mp.sqrt(disc)
        w_plus = (-B_mp + sq) / (mp.mpf(2) * A_mp)
        w_minus = (-B_mp - sq) / (mp.mpf(2) * A_mp)
        # Slope d(beta_omega / lam_C) / d omega = -(2 A omega + B):
        # Negative slope means UV-attractive as t -> +infty (for lam_C > 0)!
        slope_plus = -(mp.mpf(2) * A_mp * w_plus + B_mp)
        slope_minus = -(mp.mpf(2) * A_mp * w_minus + B_mp)
        real_fps = True
    else:
        w_plus = None
        w_minus = None
        slope_plus = None
        slope_minus = None
        real_fps = False
    if Ns > 0:
        dxi_crit = mp.sqrt((B_mp * B_mp - mp_rat(50, 9)) / (mp.mpf(20) * mp.mpf(Ns)))
    else:
        dxi_crit = None
    return {
        "name": name,
        "Ns": Ns,
        "Nw": Nw,
        "Nv": Nv,
        "c_mat": frac_str(c_mat),
        "b_lamC_coeff": frac_str(b_lamC),
        "b_R_mat": mp.nstr(b_R_mat, 16),
        "discriminant": mp.nstr(disc, 20),
        "discriminant_mp": disc,
        "real_fps_exist": real_fps,
        "omega_plus": mp.nstr(w_plus, 20) if w_plus is not None else None,
        "omega_minus": mp.nstr(w_minus, 20) if w_minus is not None else None,
        "omega_plus_mp": w_plus,
        "omega_minus_mp": w_minus,
        "omega_plus_uv_attractive": bool(slope_plus < 0) if slope_plus is not None else False,
        "omega_minus_uv_repulsive": bool(slope_minus > 0) if slope_minus is not None else False,
        "dxi_crit": mp.nstr(dxi_crit, 18) if dxi_crit is not None else "infinity",
        "dxi_crit_mp": dxi_crit,
    }


# ---------------------------------------------------------------------------
# Task OW13-C: Exact 1-Loop 2H Gildener-Weinberg Scalon Spectrum
# ---------------------------------------------------------------------------

def analyze_gw_spectrum(g2, gp, l3_test, l4_test, yb_test, ytau_test, couple_top_yt=None):
    # Direct Coleman-Weinberg / GW formula along H_d:
    # m_W/v = g2/2, m_Z/v = sqrt(g2^2 + gp^2)/2,
    # m_{H+-}^2/v^2 = l3/2, m_H^2/v^2 = m_A^2/v^2 = (l3 + l4)/2,
    # m_b/v = yb/sqrt(2), m_tau/v = ytau/sqrt(2)
    mW4 = (g2 / mp.mpf(2)) ** 4
    mZ4 = ((g2 * g2 + gp * gp) / mp.mpf(4)) ** 2
    mHp4 = (l3_test / mp.mpf(2)) ** 2
    mHA4 = ((l3_test + l4_test) / mp.mpf(2)) ** 2
    mb4 = (yb_test * yb_test / mp.mpf(2)) ** 2
    mtau4 = (ytau_test * ytau_test / mp.mpf(2)) ** 2
    mt4 = ((couple_top_yt * couple_top_yt / mp.mpf(2)) ** 2) if couple_top_yt is not None else mp.mpf(0)

    B_gw = (
        mp.mpf(6) * mW4 + mp.mpf(3) * mZ4 + mp.mpf(2) * mHA4 + mp.mpf(2) * mHp4
        - mp.mpf(12) * mb4 - mp.mpf(4) * mtau4 - mp.mpf(12) * mt4
    ) / (mp.mpf(64) * mp.pi * mp.pi)
    mh2_over_v2 = mp.mpf(8) * B_gw

    # Cross-check exact identity 8 B_gw == (1/2) * beta_{lam_1}(lam_1 = 0) (when top decoupled)
    g1_eq = mp.sqrt(mp_rat(5, 3)) * gp
    b_lam1_zero = beta_2hdm_quartics(
        mp.mpf(0), mp.mpf(0), l3_test, l4_test, g1_eq, g2, mp.mpf(0), yb_test, ytau_test, mp.mpf(0)
    )[0]
    id_err = abs(mh2_over_v2 - mp_rat(1, 2) * b_lam1_zero) if couple_top_yt is None else None

    # Pure-gauge floor (l3=l4=yb=ytau=0)
    B_gauge = (mp.mpf(6) * mW4 + mp.mpf(3) * mZ4) / (mp.mpf(64) * mp.pi * mp.pi)
    mh_floor = mp.sqrt(mp.mpf(8) * B_gauge)
    # 1H SM top-tachyon threshold: 12 (yt^2/2)^2 = 6 mW4 + 3 mZ4
    yt_crit = ((mp.mpf(6) * mW4 + mp.mpf(3) * mZ4) / mp.mpf(3)) ** mp_rat(1, 4)
    # Collider sum rule for m_h / v = 1/2:
    # 1/4 = 8 B_gauge + (4 / (8 pi^2)) * (M_heavy / v)^4
    M_heavy_deg = ((mp_rat(1, 4) - mp.mpf(8) * B_gauge) * mp.mpf(2) * mp.pi * mp.pi) ** mp_rat(1, 4)
    S4_quarter = (mp.mpf(4) ** mp_rat(1, 4)) * M_heavy_deg
    lam_eff_req = mp.mpf(2) * M_heavy_deg * M_heavy_deg

    return {
        "B_gw": mp.nstr(B_gw, 20),
        "mh2_over_v2": mp.nstr(mh2_over_v2, 20),
        "B_gw_mp": B_gw,
        "identity_abs_err": mp.nstr(id_err, 12) if id_err is not None else None,
        "identity_err_mp": id_err,
        "pure_gauge_mh_over_v": mp.nstr(mh_floor, 18),
        "mh_floor_mp": mh_floor,
        "sm_1h_yt_tachyon_crit": mp.nstr(yt_crit, 18),
        "yt_crit_mp": yt_crit,
        "M_heavy_deg_for_mh_half": mp.nstr(M_heavy_deg, 18),
        "M_heavy_mp": M_heavy_deg,
        "S4_fourth_root_over_v": mp.nstr(S4_quarter, 18),
        "S4_mp": S4_quarter,
        "lam_eff_portal_required": mp.nstr(lam_eff_req, 18),
        "lam_eff_mp": lam_eff_req,
    }


def main():
    mp.mp.dps = 55
    out = {}

    # ------------------------------------------------------------------
    # OW13-A: Benchmarks, f_lam, 2H Quartic FPs, Downward RGE, f_g
    # ------------------------------------------------------------------
    bench_sm = run_buttazzo_1loop_benchmark()

    gravity_specs = [
        ("pure_gravity_T2",    0,  0,  0, 1),
        ("spin10_real10_T2",  10, 48, 45, 1),
        ("spin10_real10_T1",  10, 48, 45, 2),
        ("ps_412_T2",         16, 48, 21, 1),
        ("gsm_2h_T2",          8, 48, 12, 1),
    ]
    grav_fps = {}
    for label, ns, nw, nv, fw in gravity_specs:
        fps = solve_gravity_fp(ns, nw, nv, fW=fw)
        assert len(fps) == 1, f"Expected unique FP for {label}, got {len(fps)}"
        fp = fps[0]
        fl = compute_f_lam_both_gauges(fp["g"], fp["lam"], fp["eta"])
        grav_fps[label] = {
            "Ns": ns, "Nw": nw, "Nv": nv, "fW": fw,
            "g_star": mp.nstr(fp["g"], 20),
            "lam_star": mp.nstr(fp["lam"], 20),
            "fp_residual": mp.nstr(fp["residual"], 12),
            "f_lam_dD": mp.nstr(fl["f_lam_dD"], 20),
            "f_lam_LDW": mp.nstr(fl["f_lam_LDW"], 20),
            "fd_err_dD": mp.nstr(fl["fd_err_dD"], 12),
            "fd_err_LDW": mp.nstr(fl["fd_err_LDW"], 12),
            "_g": fp["g"],
            "_lam": fp["lam"],
            "_f_dD": fl["f_lam_dD"],
            "_f_LDW": fl["f_lam_LDW"],
            "_fd_max": max(fl["fd_err_dD"], fl["fd_err_LDW"]),
        }

    # Exact analytic collision threshold at g_UV = 13/25
    g_uv = mp_rat(13, 25)
    yt_uv = mp_rat(11, 20)
    yb_low = mp_rat(1, 100)
    yb_high = mp_rat(9, 20)
    f_crit_ratio = (mp.mpf(54) + mp.mpf(6) * mp.sqrt(mp.mpf(114))) / (mp.mpf(80) * mp.pi * mp.pi)
    f_crit = f_crit_ratio * g_uv * g_uv
    yb_crit = (mp_rat(171, 600) ** mp_rat(1, 4)) * g_uv

    # Collision check for G_SM 2H at yb = 1/100 (both dD and LDW)
    gsm_coll_dD = check_lam1_collision_discriminant(grav_fps["gsm_2h_T2"]["_f_dD"], g_uv, g_uv, yb_low, yb_low)
    gsm_coll_LDW = check_lam1_collision_discriminant(grav_fps["gsm_2h_T2"]["_f_LDW"], g_uv, g_uv, yb_low, yb_low)

    # Full 4-coupling 2H quartic FPs for Spin(10) T2 (dD & LDW, low & high yb), Spin(10) T1 (dD), PS(4,1,2) T2 (dD)
    quartic_cases = [
        ("spin10_T2_dD_yb_low",   grav_fps["spin10_real10_T2"]["_f_dD"],  yb_low),
        ("spin10_T2_LDW_yb_low",  grav_fps["spin10_real10_T2"]["_f_LDW"], yb_low),
        ("spin10_T2_dD_yb_high",  grav_fps["spin10_real10_T2"]["_f_dD"],  yb_high),
        ("spin10_T2_LDW_yb_high", grav_fps["spin10_real10_T2"]["_f_LDW"], yb_high),
        ("spin10_T1_dD_yb_low",   grav_fps["spin10_real10_T1"]["_f_dD"],  yb_low),
        ("ps412_T2_dD_yb_low",    grav_fps["ps_412_T2"]["_f_dD"],         yb_low),
    ]
    quartic_fps = {}
    for label, fl_val, ybv in quartic_cases:
        res = solve_2hdm_quartic_fp(fl_val, g_uv, g_uv, yt_uv, ybv, ybv)
        quartic_fps[label] = {
            "f_lam": mp.nstr(fl_val, 18),
            "yb": mp.nstr(ybv, 10),
            "lam_star": [mp.nstr(v, 18) for v in res["lam"]],
            "max_abs_lam": mp.nstr(max(abs(v) for v in res["lam"]), 16),
            "residual": mp.nstr(res["residual"], 12),
            "thetas": [mp.nstr(th, 16) for th in res["thetas"]],
            "max_im_theta": mp.nstr(res["max_im_theta"], 12),
            "all_uv_irrelevant": res["all_uv_irrelevant"],
            "bfb_satisfied": res["bfb_satisfied"],
            "_res_mp": res["residual"],
            "_max_lam_mp": max(abs(v) for v in res["lam"]),
            "_lam_mp": res["lam"],
        }

    # Downward 1-loop 2H Type-II RGE (t = 0 -> -38)
    rge_high_grav = run_2hdm_downward_rge(g_uv, yt_uv, yb_high, yb_high, quartic_fps["spin10_T2_dD_yb_high"]["_lam_mp"])
    rge_high_zero = run_2hdm_downward_rge(g_uv, yt_uv, yb_high, yb_high, [mp.mpf(0)] * 4)
    ir_diff_high = max(abs(rge_high_grav["lam"][i] - rge_high_zero["lam"][i]) for i in range(4))

    rge_low_grav = run_2hdm_downward_rge(g_uv, yt_uv, yb_low, yb_low, quartic_fps["spin10_T2_dD_yb_low"]["_lam_mp"])
    rge_low_zero = run_2hdm_downward_rge(g_uv, yt_uv, yb_low, yb_low, [mp.mpf(0)] * 4)

    # Exact f_g > 0 structural theorem (Spin(10) vs U(1)_Y)
    T_adj_so10 = Fraction(8, 1)
    T_16_so10 = Fraction(2, 1)
    T_vec10_so10 = Fraction(1, 1)
    b_so10_real10 = Fraction(-11, 3) * T_adj_so10 + Fraction(2, 3) * (3 * T_16_so10) + Fraction(1, 6) * T_vec10_so10
    b_so10_comp10 = Fraction(-11, 3) * T_adj_so10 + Fraction(2, 3) * (3 * T_16_so10) + Fraction(1, 3) * T_vec10_so10
    b_u1y_2h = Fraction(21, 5)

    def check_fg_sector(b_frac, fg_sample):
        b_mp = mp_frac(b_frac)
        # beta_g = -fg * g + (b / (16 pi^2)) * g^3
        # Gaussian FP g = 0: theta_0 = -d(beta_g)/dg|_0 = +fg
        theta_gauss = fg_sample
        ratio = (mp.mpf(16) * mp.pi * mp.pi * fg_sample) / b_mp
        if ratio > 0:
            g_int = mp.sqrt(ratio)
            # d(beta_g)/dg|_{g_int} = -fg + 3*(b/(16 pi^2))*g_int^2 = -fg + 3 fg = +2 fg => theta_int = -2 fg
            theta_int = -(-fg_sample + mp.mpf(3) * (b_mp / (mp.mpf(16) * mp.pi * mp.pi)) * g_int * g_int)
            has_interactive = True
        else:
            g_int = None
            theta_int = None
            has_interactive = False
        return {
            "b_1loop": frac_str(b_frac),
            "asymptotically_free": bool(b_frac < 0),
            "theta_gaussian": mp.nstr(theta_gauss, 12),
            "has_interactive_uv_fp": has_interactive,
            "g_interactive_at_fg_1e_2": mp.nstr(g_int, 16) if g_int is not None else None,
            "theta_interactive": mp.nstr(theta_int, 12) if theta_int is not None else None,
        }

    fg_sample = mp_rat(1, 100)
    fg_theorem = {
        "fg_sample": "1/100",
        "spin10_real10": check_fg_sector(b_so10_real10, fg_sample),
        "spin10_complex10": check_fg_sector(b_so10_comp10, fg_sample),
        "u1y_2h": check_fg_sector(b_u1y_2h, fg_sample),
    }

    ow13_a_pass = bool(
        bench_sm["gate_pass"]
        and all(grav_fps[k]["_f_dD"] > 0 and grav_fps[k]["_f_LDW"] > 0 and grav_fps[k]["_fd_max"] < mp_pow10(-15) for k in grav_fps)
        and (mp_rat(4, 100) < f_crit < mp_rat(41, 1000))
        and (grav_fps["gsm_2h_T2"]["_f_dD"] < mp_rat(34, 1000))
        and (grav_fps["gsm_2h_T2"]["_f_dD"] < f_crit)
        and (grav_fps["gsm_2h_T2"]["_f_LDW"] < mp_rat(22, 1000))
        and (grav_fps["gsm_2h_T2"]["_f_LDW"] < f_crit)
        and (not gsm_coll_dD["has_real_root"])
        and (not gsm_coll_LDW["has_real_root"])
        and (grav_fps["spin10_real10_T2"]["_f_dD"] > mp_rat(67, 100))
        and (grav_fps["spin10_real10_T2"]["_f_LDW"] > mp_rat(37, 100))
        and all(
            quartic_fps[k]["_res_mp"] < mp_pow10(-40)
            and quartic_fps[k]["all_uv_irrelevant"]
            and quartic_fps[k]["_max_lam_mp"] < mp_rat(3, 100)
            for k in quartic_fps
        )
        and quartic_fps["spin10_T2_dD_yb_high"]["bfb_satisfied"]
        and quartic_fps["spin10_T2_LDW_yb_high"]["bfb_satisfied"]
        and rge_high_grav["bfb_satisfied"]
        and rge_high_zero["bfb_satisfied"]
        and (ir_diff_high < mp_rat(5, 1000))
        and (rge_low_grav["lam"][0] < mp_rat(-1, 10))
        and (rge_low_grav["lam"][1] > mp_rat(7, 10))
        and (b_so10_real10 == Fraction(-151, 6))
        and (b_so10_comp10 == Fraction(-25, 1))
        and (not fg_theorem["spin10_real10"]["has_interactive_uv_fp"])
        and fg_theorem["u1y_2h"]["has_interactive_uv_fp"]
    )

    # ------------------------------------------------------------------
    # OW13-B: Conformal xi = 1/6 & C^2 + R^2 Quadratic Gravity
    # ------------------------------------------------------------------
    gp_uv_mp = mp.sqrt(mp_rat(3, 5)) * g_uv
    l_low = quartic_fps["spin10_T2_dD_yb_low"]["_lam_mp"]
    l_high = quartic_fps["spin10_T2_dD_yb_high"]["_lam_mp"]
    xi_uv_low = analyze_xi_1loop_2hdm(g_uv, gp_uv_mp, yt_uv, yb_low, yb_low, l_low[0], l_low[1], l_low[2], l_low[3])
    xi_uv_high = analyze_xi_1loop_2hdm(g_uv, gp_uv_mp, yt_uv, yb_high, yb_high, l_high[0], l_high[1], l_high[2], l_high[3])
    xi_ir_high = analyze_xi_1loop_2hdm(
        rge_high_grav["g2"], rge_high_grav["gp"],
        rge_high_grav["yt"], rge_high_grav["yb"], rge_high_grav["ytau"],
        rge_high_grav["lam"][0], rge_high_grav["lam"][1], rge_high_grav["lam"][2], rge_high_grav["lam"][3],
    )

    grav_xi_bg = {}
    for label in ("pure_gravity_T2", "spin10_real10_T2", "spin10_real10_T1", "ps_412_T2", "gsm_2h_T2"):
        res_xi = compute_grav_beta_xi_bg(grav_fps[label]["_g"], grav_fps[label]["_lam"])
        grav_xi_bg[label] = {
            "f_xi_bg": mp.nstr(res_xi["f_xi_bg"], 18),
            "beta_xi_bg_at_1_6": mp.nstr(res_xi["beta_xi_bg_at_1_6"], 18),
            "fd_abs_err": mp.nstr(res_xi["fd_abs_err"], 12),
            "_f_mp": res_xi["f_xi_bg"],
            "_fd_mp": res_xi["fd_abs_err"],
        }
    unimod_xi = compute_grav_beta_xi_bg(mp.mpf(4) * mp.pi / mp.mpf(5), mp.mpf(0))
    grav_xi_bg["unimodular_lam0_2h"] = {
        "f_xi_bg": mp.nstr(unimod_xi["f_xi_bg"], 18),
        "beta_xi_bg_at_1_6": mp.nstr(unimod_xi["beta_xi_bg_at_1_6"], 18),
        "fd_abs_err": mp.nstr(unimod_xi["fd_abs_err"], 12),
        "_f_mp": unimod_xi["f_xi_bg"],
        "_fd_mp": unimod_xi["fd_abs_err"],
    }

    quad_specs = [
        ("pure_gravity",     0,  0,  0),
        ("gsm_2h",           8, 48, 12),
        ("ps_412",          16, 48, 21),
        ("spin10_real10",   10, 48, 45),
        ("spin10_complex10",20, 48, 45),
    ]
    quad_results = {}
    for name, ns, nw, nv in quad_specs:
        quad_results[name] = analyze_quadratic_gravity_spectrum(name, ns, nw, nv, mp_rat(1, 6))

    disc_pure = quad_results["pure_gravity"]["discriminant_mp"]
    ow13_b_pass = bool(
        (mp.mpf(xi_uv_low["beta_xi_at_conformal_max_abs"]) < mp_pow10(-45))
        and (mp.mpf(xi_uv_high["beta_xi_at_conformal_max_abs"]) < mp_pow10(-45))
        and (mp.mpf(xi_ir_high["beta_xi_at_conformal_max_abs"]) < mp_pow10(-45))
        and xi_uv_low["is_saddle"]
        and xi_uv_high["is_double_ir_attractive"]
        and xi_ir_high["is_double_ir_attractive"]
        and (xi_ir_high["ev1_mp"] > mp.mpf(9))
        and (xi_ir_high["ev2_mp"] > mp.mpf(13))
        and all(grav_xi_bg[k]["_fd_mp"] < mp_pow10(-15) for k in grav_xi_bg)
        and (mp_rat(-8, 100) < grav_xi_bg["spin10_real10_T2"]["_f_mp"] < mp_rat(-7, 100))
        and (mp_rat(16, 1000) < grav_xi_bg["ps_412_T2"]["_f_mp"] < mp_rat(17, 1000))
        and (mp_rat(-22, 100) < grav_xi_bg["gsm_2h_T2"]["_f_mp"] < mp_rat(-21, 100))
        and (grav_xi_bg["unimodular_lam0_2h"]["_f_mp"] == mp.mpf(0))
        and (mp_rat(-23, 1000) < quad_results["pure_gravity"]["omega_plus_mp"] < mp_rat(-22, 1000))
        and (mp_rat(-55, 10) < quad_results["pure_gravity"]["omega_minus_mp"] < mp_rat(-54, 10))
        and all(
            quad_results[k]["real_fps_exist"]
            and quad_results[k]["omega_plus_uv_attractive"]
            and quad_results[k]["omega_minus_uv_repulsive"]
            and (mp.mpf(quad_results[k]["b_R_mat"]) == mp.mpf(0))
            for k in quad_results
        )
        and all(quad_results[k]["discriminant_mp"] > disc_pure for k in ("gsm_2h", "ps_412", "spin10_real10", "spin10_complex10"))
        and (quad_results["spin10_real10"]["dxi_crit_mp"] < mp_rat(22, 10))
        and (quad_results["gsm_2h"]["dxi_crit_mp"] < mp_rat(19, 10))
        and (quad_results["ps_412"]["dxi_crit_mp"] < mp_rat(15, 10))
        and (quad_results["spin10_complex10"]["dxi_crit_mp"] < mp_rat(15, 10))
    )

    # ------------------------------------------------------------------
    # OW13-C: Exact 2H Gildener-Weinberg Scalon Spectrum
    # ------------------------------------------------------------------
    gw_ew = analyze_gw_spectrum(mp_rat(13, 20), mp_rat(9, 25), mp_rat(3, 10), mp_rat(-1, 5), mp_rat(1, 50), mp_rat(1, 100))
    gw_gut = analyze_gw_spectrum(g_uv, gp_uv_mp, mp_rat(7, 25), mp_rat(-3, 20), mp_rat(1, 100), mp_rat(1, 100))

    ow13_c_pass = bool(
        (gw_ew["identity_err_mp"] < mp_pow10(-45))
        and (gw_gut["identity_err_mp"] < mp_pow10(-45))
        and (mp_rat(45, 100) < gw_ew["yt_crit_mp"] < mp_rat(46, 100))
        and (mp_rat(37, 100) < gw_gut["yt_crit_mp"] < mp_rat(38, 100))
        and (gw_ew["B_gw_mp"] > 0)
        and (gw_gut["B_gw_mp"] > 0)
        and (mp_rat(39, 1000) < gw_ew["mh_floor_mp"] < mp_rat(40, 1000))
        and (mp_rat(28, 1000) < gw_gut["mh_floor_mp"] < mp_rat(29, 1000))
        and (mp_rat(148, 100) < gw_ew["M_heavy_mp"] < mp_rat(150, 100))
        and (mp_rat(210, 100) < gw_ew["S4_mp"] < mp_rat(211, 100))
        and (gw_ew["lam_eff_mp"] > mp_rat(44, 10))
    )

    # ------------------------------------------------------------------
    # OW13-D: 4 / 4 Planted Fault Controls (PF-OW13-1..4)
    # ------------------------------------------------------------------
    pf1 = solve_2hdm_quartic_fp(-grav_fps["spin10_real10_T2"]["_f_dD"], g_uv, g_uv, yt_uv, yb_low, yb_low)
    pf1_pass = bool(pf1["residual"] < mp_pow10(-40) and pf1["all_uv_relevant"])

    pf2 = check_lam1_collision_discriminant(
        grav_fps["gsm_2h_T2"]["_f_dD"], g_uv, g_uv, yb_low, yb_low, flip_gauge_box=True
    )
    pf2_pass = bool(pf2["has_real_root"] and pf2["discriminant"] > 0)

    pf3 = analyze_quadratic_gravity_spectrum("spin10_real10_nonconf", 10, 48, 45, mp.mpf(5))
    pf3_pass = bool((not pf3["real_fps_exist"]) and pf3["discriminant_mp"] < 0)

    pf4 = analyze_gw_spectrum(
        mp_rat(13, 20), mp_rat(9, 25), mp.mpf(0), mp.mpf(0), mp.mpf(0), mp.mpf(0), couple_top_yt=mp_rat(94, 100)
    )
    pf4_pass = bool(pf4["B_gw_mp"] < 0)

    ow13_d_pass = bool(pf1_pass and pf2_pass and pf3_pass and pf4_pass)
    all_gates_passed = bool(ow13_a_pass and ow13_b_pass and ow13_c_pass and ow13_d_pass)

    # Strip private mpmath helper keys before JSON serialization
    def clean_dict(d):
        if isinstance(d, dict):
            return {k: clean_dict(v) for k, v in d.items() if not k.startswith("_") and not k.endswith("_mp")}
        if isinstance(d, list):
            return [clean_dict(v) for v in d]
        return d

    out = {
        "card_id": "A2-OW13",
        "seat": "AGY-002",
        "empirical_inputs": "0 of 19",
        "ow13_a": {
            "guardrail4_buttazzo_1loop_benchmark": bench_sm,
            "gravity_fixed_points_and_f_lam": clean_dict(grav_fps),
            "collision_wall": {
                "g_uv": "13/25",
                "f_crit_over_g2": mp.nstr(f_crit_ratio, 18),
                "f_crit": mp.nstr(f_crit, 18),
                "yb_crit": mp.nstr(yb_crit, 18),
                "gsm_2h_dD_discriminant": mp.nstr(gsm_coll_dD["discriminant"], 18),
                "gsm_2h_dD_im_root": mp.nstr(gsm_coll_dD["im_root_part"], 18),
                "gsm_2h_dD_has_real_root": gsm_coll_dD["has_real_root"],
                "gsm_2h_LDW_discriminant": mp.nstr(gsm_coll_LDW["discriminant"], 18),
                "gsm_2h_LDW_im_root": mp.nstr(gsm_coll_LDW["im_root_part"], 18),
                "gsm_2h_LDW_has_real_root": gsm_coll_LDW["has_real_root"],
            },
            "quartic_fixed_points": clean_dict(quartic_fps),
            "downward_rge_t_0_to_neg38": {
                "yb_high_grav_fixed": {
                    "g_ir": [mp.nstr(rge_high_grav["g3"], 16), mp.nstr(rge_high_grav["g2"], 16), mp.nstr(rge_high_grav["gp"], 16)],
                    "y_ir": [mp.nstr(rge_high_grav["yt"], 16), mp.nstr(rge_high_grav["yb"], 16), mp.nstr(rge_high_grav["ytau"], 16)],
                    "lam_ir": [mp.nstr(v, 16) for v in rge_high_grav["lam"]],
                    "bfb_satisfied": rge_high_grav["bfb_satisfied"],
                },
                "yb_high_zero_boundary": {
                    "lam_ir": [mp.nstr(v, 16) for v in rge_high_zero["lam"]],
                    "bfb_satisfied": rge_high_zero["bfb_satisfied"],
                },
                "yb_high_max_ir_quartic_diff": mp.nstr(ir_diff_high, 16),
                "yb_low_grav_fixed": {
                    "lam_ir": [mp.nstr(v, 16) for v in rge_low_grav["lam"]],
                    "bfb_satisfied": rge_low_grav["bfb_satisfied"],
                },
                "yb_low_zero_boundary": {
                    "lam_ir": [mp.nstr(v, 16) for v in rge_low_zero["lam"]],
                    "bfb_satisfied": rge_low_zero["bfb_satisfied"],
                },
            },
            "fg_structural_theorem": fg_theorem,
            "gate_pass": ow13_a_pass,
        },
        "ow13_b": {
            "xi_1loop_2hdm": {
                "uv_spin10_yb_low": clean_dict(xi_uv_low),
                "uv_spin10_yb_high": clean_dict(xi_uv_high),
                "ir_t_neg38_yb_high": clean_dict(xi_ir_high),
            },
            "grav_beta_xi_bg": clean_dict(grav_xi_bg),
            "quadratic_gravity_c2_r2": clean_dict(quad_results),
            "gate_pass": ow13_b_pass,
        },
        "ow13_c": {
            "gw_ew_benchmark": clean_dict(gw_ew),
            "gw_gut_benchmark": clean_dict(gw_gut),
            "gate_pass": ow13_c_pass,
        },
        "ow13_d": {
            "pf_ow13_1_flip_f_lam": {
                "thetas": [mp.nstr(th, 14) for th in pf1["thetas"]],
                "all_uv_relevant": pf1["all_uv_relevant"],
                "detected": pf1_pass,
            },
            "pf_ow13_2_flip_gauge_box": {
                "discriminant": mp.nstr(pf2["discriminant"], 16),
                "has_real_root": pf2["has_real_root"],
                "detected": pf2_pass,
            },
            "pf_ow13_3_nonconformal_xi5": {
                "discriminant": pf3["discriminant"],
                "real_fps_exist": pf3["real_fps_exist"],
                "detected": pf3_pass,
            },
            "pf_ow13_4_couple_top_to_Hd": {
                "B_gw": pf4["B_gw"],
                "mh2_over_v2": pf4["mh2_over_v2"],
                "detected": pf4_pass,
            },
            "planted_faults_detected": int(pf1_pass) + int(pf2_pass) + int(pf3_pass) + int(pf4_pass),
            "gate_pass": ow13_d_pass,
        },
        "all_gates_passed": all_gates_passed,
    }

    out_path = Path(__file__).resolve().parent / "a2_ow13_v2_results.json"
    out_text = json.dumps(out, indent=2, sort_keys=True) + "\n"
    out_path.write_text(out_text, encoding="utf-8")
    digest = hashlib.sha256(out_text.encode("utf-8")).hexdigest()
    print(f"Wrote {out_path} (SHA-256={digest}) all_gates_passed={all_gates_passed}")
    if not all_gates_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
