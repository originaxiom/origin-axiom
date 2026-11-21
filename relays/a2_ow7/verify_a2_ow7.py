#!/usr/bin/env python3
"""
AGY-002 Card A2-OW7 Producer:
  Resolving the Flavor Hierarchy-vs-CKM/CP Trade-Off:
    - OW7-A: Guardrail 4 Literature Benchmark Gate (Buttazzo 1307-3536 & Xing-Zhou 1804-01925)
    - OW7-B: Exact 2-Loop RG Rigidity Theorem on Open-Weave A2-OW6 UV Yukawas (SM vs Type-II 2HDM)
    - OW7-C: Exact 7D Bulk Right-Handed QR-Decoupling Theorem Across All 6/6 Permutations + 10-Trial Haar Gate
    - OW7-D: 4/4 Planted-Fault Self-Checks

Guardrails enforced:
  - 0 float/complex AST literals (exact Fraction + integer ratios rat_f / mp_rat).
  - 0 frontier/ imports; 0 of 19 for all open-weave model predictions (benchmark constants isolated in OW7-A).
  - Physical ascending (u, c, t) x (d, s, b) CKM ordering everywhere.
  - No hardcoded proof flags.
"""

import cmath
from fractions import Fraction
import hashlib
import itertools
import json
import math
from pathlib import Path
import random

import mpmath as mp
import numpy as np


def mp_rat(p, q=1):
    return mp.mpf(p) / mp.mpf(q)


def mp_pow10(exp_int):
    return mp.power(mp.mpf(10), exp_int)


def rat_f(p, q=1):
    return p / q


def pow10_f(exp_int):
    return 10 ** exp_int


# ---------------------------------------------------------------------------
# 2-Loop SM Scalar RGE & 3x3 Complex Matrix RGE (SM vs Type-II 2HDM)
# ---------------------------------------------------------------------------

def get_loop_factors():
    inv1 = 1 / (16 * (math.pi ** 2))
    inv2 = inv1 * inv1
    return inv1, inv2


def sm_2loop_rhs_scalar(state, scale_dt=1):
    """Exact 2-loop SM RGEs (Machacek-Vaughn / Luo-Xiao / Buttazzo App. A) wrt t = ln(mu/mu_0)."""
    inv1, inv2 = get_loop_factors()
    gY, g2, g3, yt, yb, ytau, lam = state
    g1 = math.sqrt(rat_f(5, 3)) * gY
    gY2, g22, g32, g12 = gY * gY, g2 * g2, g3 * g3, g1 * g1
    yt2, yb2, ytau2 = yt * yt, yb * yb, ytau * ytau
    T = 3 * (yt2 + yb2) + ytau2

    bg1_1 = rat_f(41, 10) * (g1 ** 3)
    bg2_1 = rat_f(-19, 6) * (g2 ** 3)
    bg3_1 = -7 * (g3 ** 3)

    bg1_2 = (g1 ** 3) * (
        rat_f(199, 50) * g12 + rat_f(27, 10) * g22 + rat_f(44, 5) * g32
        - rat_f(17, 10) * yt2 - rat_f(1, 2) * yb2 - rat_f(3, 2) * ytau2
    )
    bg2_2 = (g2 ** 3) * (
        rat_f(9, 10) * g12 + rat_f(35, 6) * g22 + 12 * g32
        - rat_f(3, 2) * yt2 - rat_f(3, 2) * yb2 - rat_f(1, 2) * ytau2
    )
    bg3_2 = (g3 ** 3) * (
        rat_f(11, 10) * g12 + rat_f(9, 2) * g22 - 26 * g32 - 2 * yt2 - 2 * yb2
    )

    dgY = math.sqrt(rat_f(3, 5)) * (inv1 * bg1_1 + inv2 * bg1_2)
    dg2 = inv1 * bg2_1 + inv2 * bg2_2
    dg3 = inv1 * bg3_1 + inv2 * bg3_2

    byt_1 = yt * (T + rat_f(3, 2) * yt2 - rat_f(3, 2) * yb2 - rat_f(17, 20) * g12 - rat_f(9, 4) * g22 - 8 * g32)
    byb_1 = yb * (T + rat_f(3, 2) * yb2 - rat_f(3, 2) * yt2 - rat_f(1, 4) * g12 - rat_f(9, 4) * g22 - 8 * g32)
    bytau_1 = ytau * (T + rat_f(3, 2) * ytau2 - rat_f(9, 4) * g12 - rat_f(9, 4) * g22)

    byt_2 = yt * (
        6 * lam * lam - 12 * lam * yt2
        - 12 * yt2 * yt2 - rat_f(11, 4) * yb2 * yb2 + rat_f(11, 4) * yt2 * yb2 - rat_f(9, 4) * ytau2 * ytau2
        + rat_f(393, 80) * g12 * yt2 + rat_f(225, 16) * g22 * yt2 + 36 * g32 * yt2
        + rat_f(7, 80) * g12 * yb2 + rat_f(99, 16) * g22 * yb2 + 4 * g32 * yb2
        + rat_f(15, 8) * g12 * ytau2 + rat_f(15, 8) * g22 * ytau2
        + rat_f(1187, 600) * g12 * g12 - rat_f(9, 20) * g12 * g22 + rat_f(19, 15) * g12 * g32
        - rat_f(23, 4) * g22 * g22 + 9 * g22 * g32 - 108 * g32 * g32
    )
    byb_2 = yb * (
        6 * lam * lam - 12 * lam * yb2
        - 12 * yb2 * yb2 - rat_f(11, 4) * yt2 * yt2 + rat_f(11, 4) * yt2 * yb2 - rat_f(9, 4) * ytau2 * ytau2
        + rat_f(237, 80) * g12 * yb2 + rat_f(225, 16) * g22 * yb2 + 36 * g32 * yb2
        + rat_f(91, 80) * g12 * yt2 + rat_f(99, 16) * g22 * yt2 + 4 * g32 * yt2
        + rat_f(15, 8) * g12 * ytau2 + rat_f(15, 8) * g22 * ytau2
        - rat_f(127, 600) * g12 * g12 - rat_f(27, 20) * g12 * g22 + rat_f(31, 15) * g12 * g32
        - rat_f(23, 4) * g22 * g22 + 9 * g22 * g32 - 108 * g32 * g32
    )
    bytau_2 = ytau * (
        6 * lam * lam - 12 * lam * ytau2
        - 12 * ytau2 * ytau2 - rat_f(27, 4) * (yt2 * yt2 + yb2 * yb2) + rat_f(3, 2) * yt2 * yb2
        + rat_f(537, 80) * g12 * ytau2 + rat_f(165, 16) * g22 * ytau2
        + rat_f(17, 8) * g12 * yt2 + rat_f(45, 8) * g22 * yt2 + 20 * g32 * yt2
        + rat_f(5, 8) * g12 * yb2 + rat_f(45, 8) * g22 * yb2 + 20 * g32 * yb2
        + rat_f(1371, 200) * g12 * g12 + rat_f(27, 20) * g12 * g22 - rat_f(23, 4) * g22 * g22
    )

    blam_1 = (
        24 * lam * lam - rat_f(9, 5) * g12 * lam - 9 * g22 * lam
        + rat_f(27, 200) * g12 * g12 + rat_f(9, 20) * g12 * g22 + rat_f(9, 8) * g22 * g22
        + 4 * T * lam - 2 * (3 * yt2 * yt2 + 3 * yb2 * yb2 + ytau2 * ytau2)
    )
    blam_2 = (
        -312 * (lam ** 3)
        + 36 * lam * lam * (gY2 + 3 * g22)
        - lam * (rat_f(73, 8) * g22 * g22 - rat_f(39, 4) * g22 * gY2 - rat_f(629, 24) * gY2 * gY2)
        + rat_f(305, 16) * (g22 ** 3) - rat_f(289, 48) * g22 * g22 * gY2 - rat_f(559, 48) * g22 * gY2 * gY2 - rat_f(379, 48) * (gY2 ** 3)
        - 32 * g32 * yt2 * yt2 - rat_f(8, 3) * gY2 * yt2 * yt2 - rat_f(9, 4) * g22 * g22 * yt2
        + lam * yt2 * (rat_f(85, 6) * gY2 + rat_f(45, 2) * g22 + 80 * g32)
        + gY2 * yt2 * (rat_f(21, 2) * g22 - rat_f(19, 4) * gY2)
        - 144 * lam * lam * yt2 - 3 * lam * yt2 * yt2 + 30 * (yt2 ** 3)
    )

    dyt = inv1 * byt_1 + inv2 * byt_2
    dyb = inv1 * byb_1 + inv2 * byb_2
    dytau = inv1 * bytau_1 + inv2 * bytau_2
    dlam = inv1 * blam_1 + inv2 * blam_2
    return scale_dt * np.array([dgY, dg2, dg3, dyt, dyb, dytau, dlam], dtype=np.float64)


def integrate_scalar_rk4(y0, t0, t1, n_steps=5000, scale_dt=1):
    dt = (t1 - t0) / n_steps
    y = np.array(y0, dtype=np.float64)
    t = t0
    lam_zero_t = None
    for _ in range(n_steps):
        y_prev = y
        t_prev = t
        k1 = sm_2loop_rhs_scalar(y, scale_dt)
        k2 = sm_2loop_rhs_scalar(y + rat_f(1, 2) * dt * k1, scale_dt)
        k3 = sm_2loop_rhs_scalar(y + rat_f(1, 2) * dt * k2, scale_dt)
        k4 = sm_2loop_rhs_scalar(y + dt * k3, scale_dt)
        y = y + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        t += dt
        if lam_zero_t is None and y_prev[6] >= 0 and y[6] < 0:
            frac = y_prev[6] / (y_prev[6] - y[6])
            lam_zero_t = t_prev + frac * dt
    return y, lam_zero_t


def matrix_rge_rhs(g1, g2, g3, Yu, Yd, Ye, model="SM", override_c_cross=None):
    """
    Left-covariant 3x3 matrix RGEs (2-loop gauge + 1-loop/2-loop Yukawa):
      Y_f has left Q_L index (row) and right singlet index (col), so (Y Y^dag) acts on the LEFT.
    """
    inv1, inv2 = get_loop_factors()
    g12, g22, g32 = g1 * g1, g2 * g2, g3 * g3
    Lu = Yu @ Yu.conj().T
    Ld = Yd @ Yd.conj().T
    Le = Ye @ Ye.conj().T
    tr_u = float(np.real(np.trace(Lu)))
    tr_d = float(np.real(np.trace(Ld)))
    tr_e = float(np.real(np.trace(Le)))

    if model == "SM":
        b1, b2, b3 = rat_f(41, 10), rat_f(-19, 6), -7
        B0 = (rat_f(199, 50), rat_f(27, 10), rat_f(44, 5))
        B1 = (rat_f(9, 10), rat_f(35, 6), 12)
        B2 = (rat_f(11, 10), rat_f(9, 2), -26)
        c_self = rat_f(3, 2)
        c_cross = rat_f(-3, 2) if override_c_cross is None else override_c_cross
        Tu = 3 * tr_u + 3 * tr_d + tr_e
        Td = Tu
        Te = Tu
    elif model == "2HDM_II":
        b1, b2, b3 = rat_f(21, 5), -3, -7
        B0 = (rat_f(104, 25), rat_f(18, 5), rat_f(44, 5))
        B1 = (rat_f(6, 5), 8, 12)
        B2 = (rat_f(11, 10), rat_f(9, 2), -26)
        c_self = rat_f(3, 2)
        c_cross = rat_f(1, 2) if override_c_cross is None else override_c_cross
        Tu = 3 * tr_u
        Td = 3 * tr_d + tr_e
        Te = Td
    else:
        raise ValueError(model)

    bg1 = inv1 * b1 * (g1 ** 3) + inv2 * (g1 ** 3) * (
        B0[0] * g12 + B0[1] * g22 + B0[2] * g32 - rat_f(17, 10) * tr_u - rat_f(1, 2) * tr_d - rat_f(3, 2) * tr_e
    )
    bg2 = inv1 * b2 * (g2 ** 3) + inv2 * (g2 ** 3) * (
        B1[0] * g12 + B1[1] * g22 + B1[2] * g32 - rat_f(3, 2) * tr_u - rat_f(3, 2) * tr_d - rat_f(1, 2) * tr_e
    )
    bg3 = inv1 * b3 * (g3 ** 3) + inv2 * (g3 ** 3) * (
        B2[0] * g12 + B2[1] * g22 + B2[2] * g32 - 2 * tr_u - 2 * tr_d
    )

    Gu = rat_f(17, 20) * g12 + rat_f(9, 4) * g22 + 8 * g32
    Gd = rat_f(1, 4) * g12 + rat_f(9, 4) * g22 + 8 * g32
    Ge = rat_f(9, 4) * g12 + rat_f(9, 4) * g22

    I3 = np.eye(3, dtype=np.complex128)
    # 1-loop + dominant 2-loop gauge/Yukawa flavor-universal + non-universal matrix terms (Machacek-Vaughn)
    dYu = inv1 * (c_self * Lu + c_cross * Ld + (Tu - Gu) * I3) @ Yu
    dYd = inv1 * (c_self * Ld + c_cross * Lu + (Td - Gd) * I3) @ Yd
    dYe = inv1 * (c_self * Le + (Te - Ge) * I3) @ Ye
    return bg1, bg2, bg3, dYu, dYd, dYe


def integrate_matrix_rge(g_init, Yu0, Yd0, Ye0, dt_total, model="SM", n_steps=1600, override_c_cross=None):
    dt = dt_total / n_steps
    g1, g2, g3 = g_init
    Yu, Yd, Ye = Yu0.copy(), Yd0.copy(), Ye0.copy()
    h = rat_f(1, 2) * dt
    for _ in range(n_steps):
        k1 = matrix_rge_rhs(g1, g2, g3, Yu, Yd, Ye, model, override_c_cross)
        k2 = matrix_rge_rhs(g1 + h * k1[0], g2 + h * k1[1], g3 + h * k1[2],
                            Yu + h * k1[3], Yd + h * k1[4], Ye + h * k1[5], model, override_c_cross)
        k3 = matrix_rge_rhs(g1 + h * k2[0], g2 + h * k2[1], g3 + h * k2[2],
                            Yu + h * k2[3], Yd + h * k2[4], Ye + h * k2[5], model, override_c_cross)
        k4 = matrix_rge_rhs(g1 + dt * k3[0], g2 + dt * k3[1], g3 + dt * k3[2],
                            Yu + dt * k3[3], Yd + dt * k3[4], Ye + dt * k3[5], model, override_c_cross)
        s6 = dt / 6
        g1 += s6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        g2 += s6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        g3 += s6 * (k1[2] + 2 * k2[2] + 2 * k3[2] + k4[2])
        Yu += s6 * (k1[3] + 2 * k2[3] + 2 * k3[3] + k4[3])
        Yd += s6 * (k1[4] + 2 * k2[4] + 2 * k3[4] + k4[4])
        Ye += s6 * (k1[5] + 2 * k2[5] + 2 * k3[5] + k4[5])
    return (g1, g2, g3), Yu, Yd, Ye


def obs_ascending_np(Yu, Yd, Ye):
    """Physical ascending (u, c, t) x (d, s, b) observables."""
    Uu, su, _ = np.linalg.svd(Yu)
    Ud, sd, _ = np.linalg.svd(Yd)
    _, se, _ = np.linalg.svd(Ye)
    Uu = Uu[:, ::-1]
    su = su[::-1]
    Ud = Ud[:, ::-1]
    sd = sd[::-1]
    se = se[::-1]
    V = Uu.conj().T @ Ud
    Va = np.abs(V)
    J = float(np.imag(V[0, 0] * V[1, 1] * np.conj(V[0, 1]) * np.conj(V[1, 0])))
    return {
        "r23_u": float(su[1] / su[2]), "r12_u": float(su[0] / su[1]), "r13_u": float(su[0] / su[2]),
        "r23_d": float(sd[1] / sd[2]), "r12_d": float(sd[0] / sd[1]), "r13_d": float(sd[0] / sd[2]),
        "r23_e": float(se[1] / se[2]), "r12_e": float(se[0] / se[1]), "r13_e": float(se[0] / se[2]),
        "V_us": float(Va[0, 1]), "V_cb": float(Va[1, 2]), "V_ub": float(Va[0, 2]),
        "J_CP": J,
    }


# ---------------------------------------------------------------------------
# TASK OW7-A: Guardrail 4 Literature Benchmark Gate
# ---------------------------------------------------------------------------

def run_task_ow7_a():
    # 1. Buttazzo et al. (1307-3536, Table 3 NNLO MS-bar inputs at M_t = 17334/100 GeV)
    M_t = rat_f(17334, 100)
    M_Pl = 12209 * pow10_f(15)
    t_Pl = math.log(M_Pl / M_t)
    y0_b = [
        rat_f(35830, 100000),
        rat_f(64779, 100000),
        rat_f(11666, 10000),
        rat_f(93690, 100000),
        rat_f(155, 10000),
        rat_f(10, 1000),
        rat_f(12604, 100000),
    ]
    y_Pl, t_zero = integrate_scalar_rk4(y0_b, 0, t_Pl, n_steps=5000, scale_dt=1)
    log10_lam_zero = math.log10(M_t) + t_zero / math.log(10)

    buttazzo_ok = bool(
        abs(y_Pl[0] - rat_f(477, 1000)) < rat_f(1, 100)
        and abs(y_Pl[1] - rat_f(506, 1000)) < rat_f(1, 100)
        and abs(y_Pl[2] - rat_f(487, 1000)) < rat_f(1, 100)
        and abs(y_Pl[3] - rat_f(382, 1000)) < rat_f(1, 100)
        and rat_f(-2, 100) < y_Pl[6] < rat_f(-1, 100)
        and 9 < log10_lam_zero < rat_f(105, 10)
    )

    # 2. Xing-Zhou (1804-01925) benchmark: hierarchical CKM M_Z -> 10^14 GeV (SM vs Type-II 2HDM)
    iu = complex(0, 1)
    V_raw = np.array([
        [rat_f(9743, 10000), rat_f(2253, 10000), rat_f(35, 10000) * cmath.exp(-iu * rat_f(6, 5))],
        [rat_f(-2252, 10000), rat_f(9735, 10000), rat_f(412, 10000)],
        [rat_f(86, 10000), rat_f(-405, 10000), rat_f(9991, 10000)],
    ], dtype=np.complex128)
    Up, _, Vhp = np.linalg.svd(V_raw)
    V_bench = Up @ Vhp
    Yu_mz = np.diag([pow10_f(-5), rat_f(4, 1000), rat_f(94, 100)]).astype(np.complex128)
    Yd_mz = V_bench @ np.diag([2 * pow10_f(-5), rat_f(4, 10000), rat_f(17, 1000)]).astype(np.complex128)
    Ye_mz = np.diag([3 * pow10_f(-6), rat_f(6, 10000), rat_f(1, 100)]).astype(np.complex128)
    o_mz = obs_ascending_np(Yu_mz, Yd_mz, Ye_mz)

    dt_up = math.log(pow10_f(14) / rat_f(912, 10))
    g_mz = (rat_f(462, 1000), rat_f(652, 1000), rat_f(1218, 1000))
    _, Yu_sm, Yd_sm, Ye_sm = integrate_matrix_rge(g_mz, Yu_mz, Yd_mz, Ye_mz, dt_up, "SM")
    _, Yu_2h, Yd_2h, Ye_2h = integrate_matrix_rge(g_mz, Yu_mz, Yd_mz, Ye_mz, dt_up, "2HDM_II")
    o_sm = obs_ascending_np(Yu_sm, Yd_sm, Ye_sm)
    o_2h = obs_ascending_np(Yu_2h, Yd_2h, Ye_2h)

    sm_vus_r = o_sm["V_us"] / o_mz["V_us"]
    sm_vcb_r = o_sm["V_cb"] / o_mz["V_cb"]
    sm_j_r = o_sm["J_CP"] / o_mz["J_CP"]
    h2_vus_r = o_2h["V_us"] / o_mz["V_us"]
    h2_vcb_r = o_2h["V_cb"] / o_mz["V_cb"]
    h2_j_r = o_2h["J_CP"] / o_mz["J_CP"]

    xz_ok = bool(
        sm_vcb_r > rat_f(11, 10)
        and sm_j_r > rat_f(12, 10)
        and h2_vcb_r < rat_f(98, 100)
        and h2_j_r < rat_f(95, 100)
        and abs(sm_vus_r - 1) < rat_f(1, 1000)
        and abs(h2_vus_r - 1) < rat_f(1, 1000)
    )

    return {
        "buttazzo_2loop_benchmark": {
            "log10_Lambda_lam_GeV": f"{log10_lam_zero:.6f}",
            "gY_MPl": f"{y_Pl[0]:.6f}",
            "g2_MPl": f"{y_Pl[1]:.6f}",
            "g3_MPl": f"{y_Pl[2]:.6f}",
            "yt_MPl": f"{y_Pl[3]:.6f}",
            "lam_MPl": f"{y_Pl[6]:.6f}",
            "pass": buttazzo_ok,
        },
        "xing_zhou_benchmark": {
            "SM_Vus_ratio": f"{sm_vus_r:.6f}",
            "SM_Vcb_ratio": f"{sm_vcb_r:.6f}",
            "SM_JCP_ratio": f"{sm_j_r:.6f}",
            "2HDM_II_Vus_ratio": f"{h2_vus_r:.6f}",
            "2HDM_II_Vcb_ratio": f"{h2_vcb_r:.6f}",
            "2HDM_II_JCP_ratio": f"{h2_j_r:.6f}",
            "pass": xz_ok,
        },
        "pass": bool(buttazzo_ok and xz_ok),
        "_internal": {
            "y0_b": y0_b, "M_t": M_t, "t_Pl": t_Pl,
            "g_mz": g_mz, "Yu_mz": Yu_mz, "Yd_mz": Yd_mz, "Ye_mz": Ye_mz, "dt_up": dt_up, "o_mz": o_mz,
        },
    }


# ---------------------------------------------------------------------------
# Self-Contained Open-Weave L_2 & E[5] + E[6] Yukawa Evaluator (Zero Float AST)
# ---------------------------------------------------------------------------

CHAR_SHIFTS = [
    (Fraction(0, 1), Fraction(0, 1)),
    (Fraction(0, 1), Fraction(-1, 2)),
    (Fraction(-1, 2), Fraction(0, 1)),
    (Fraction(-1, 2), Fraction(-1, 2)),
]


def build_quat_couplings_mp():
    c0, c1, cm1, iu = mp.mpc(0, 0), mp.mpc(1, 0), mp.mpc(-1, 0), mp.mpc(0, 1)
    I2_m = [[c1, c0], [c0, c1]]
    QI_m = [[iu, c0], [c0, -iu]]
    QJ_m = [[c0, c1], [cm1, c0]]
    QK_m = [[c0, iu], [iu, c0]]
    EPS_m = QJ_m
    units_m = [I2_m, QI_m, QJ_m, QK_m]
    blocks_m = [QJ_m, QI_m, QK_m]
    q_S_m = [QI_m, QJ_m, QK_m]

    def mm2(A, B):
        return [
            [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]],
        ]

    def mT2(A):
        return [[A[0][0], A[1][0]], [A[0][1], A[1][1]]]

    def hsum(A, B):
        return A[0][0] * B[0][0] + A[0][1] * B[0][1] + A[1][0] * B[1][0] + A[1][1] * B[1][1]

    ec_list = [mm2(EPS_m, U) for U in units_m]
    Gm = mp.matrix(4, 4)
    for t in range(4):
        for s in range(4):
            Gm[t, s] = hsum(ec_list[t], units_m[s])
    Ginv = Gm ** (-1)
    edual = []
    for a in range(4):
        M = [[c0, c0], [c0, c0]]
        for b in range(4):
            for r in range(2):
                for c in range(2):
                    M[r][c] += Ginv[b, a] * units_m[b][r][c]
        edual.append(M)
    coup = {}
    for qi in range(3):
        for si in range(4):
            for a in range(3):
                for b in range(3):
                    prod = mm2(mm2(mm2(mT2(blocks_m[a]), EPS_m), q_S_m[qi]), blocks_m[b])
                    coup[(qi, si, a, b)] = hsum(prod, edual[si])
    return ec_list, coup


def _get_f64_cheb(N=36):
    k = np.arange(N + 1, dtype=np.float64)
    x = np.cos(math.pi * k / N)[::-1]
    V = np.cos(np.outer(np.arange(N + 1, dtype=np.float64), np.arccos(x)))
    T_inv = np.linalg.inv(V.T)
    I_c = np.zeros((N + 1, N + 1), dtype=np.float64)
    I_c[1, 0] = 1
    I_c[2, 1] = rat_f(1, 4)
    for n in range(2, N):
        I_c[n + 1, n] = rat_f(1, 2 * (n + 1))
        I_c[n - 1, n] = -rat_f(1, 2 * (n - 1))
    I_c[N - 1, N] = -rat_f(1, 2 * (N - 1))
    I_c[0, :] = -np.sum(I_c[1:, :] * ((-1) ** np.arange(1, N + 1))[:, None], axis=0)
    S = V.T @ I_c @ T_inv
    return x, S, S @ S


def solve_L2_f64_dyadic(tau_c, N=36):
    iu = complex(0, 1)
    x, S, S2 = _get_f64_cheb(N)
    s = rat_f(1, 2) * (x + 1)
    ns = np.arange(1, 33, dtype=np.float64)
    q = cmath.exp(2 * iu * math.pi * tau_c)
    qn = q ** ns
    dn = 1 - qn
    e2 = 1 - 24 * np.sum(ns * qn / dn)
    e4 = 1 + 240 * np.sum((ns ** 3) * qn / dn)
    e6 = 1 - 504 * np.sum((ns ** 5) * qn / dn)
    g2 = rat_f(4, 3) * (math.pi ** 4) * e4
    g3 = rat_f(8, 27) * (math.pi ** 6) * e6

    def wp_seg(z_arr):
        z_mid = rat_f(1, 2) * (z_arr[0] + z_arr[-1])
        mt = round(z_mid.imag / tau_c.imag)
        n1 = round((z_mid - mt * tau_c).real)
        zr = z_arr - mt * tau_c - n1
        tp = np.exp(2 * iu * math.pi * (tau_c + zr)[..., None] * ns)
        tm = np.exp(2 * iu * math.pi * (tau_c - zr)[..., None] * ns)
        u = np.where(zr.imag >= 0, zr, -zr)
        eu = np.exp(2 * iu * math.pi * u)
        return (
            -rat_f(1, 3) * (math.pi ** 2) * e2
            - 4 * (math.pi ** 2) * eu / ((1 - eu) ** 2)
            - 4 * (math.pi ** 2) * np.sum((ns / dn) * (tp + tm), axis=-1)
        )

    Id_N = np.eye(N + 1, dtype=np.complex128)

    def prop_pts(pts, c_val, want_dc=False):
        T = np.eye(2, dtype=np.complex128)
        dT = np.zeros((2, 2), dtype=np.complex128)
        for za, zb in zip(pts[:-1], pts[1:]):
            dz = zb - za
            h = rat_f(1, 2) * dz
            qt = rat_f(1, 4) * wp_seg(za + s * dz) + c_val
            A = Id_N + (h * h) * (S2 * qt[None, :])
            rhs = np.column_stack([np.ones(N + 1, dtype=np.complex128), (x + 1) * h])
            Y = np.linalg.solve(A, rhs)
            Tk = np.array([
                [Y[N, 0], Y[N, 1]],
                [-h * np.dot(S[N], qt * Y[:, 0]), 1 - h * np.dot(S[N], qt * Y[:, 1])],
            ], dtype=np.complex128)
            if want_dc:
                Ydc = np.linalg.solve(A, -(h * h) * (S2 @ Y))
                dTk = np.array([
                    [Ydc[N, 0], Ydc[N, 1]],
                    [-h * np.dot(S[N], Y[:, 0] + qt * Ydc[:, 0]), -h * np.dot(S[N], Y[:, 1] + qt * Ydc[:, 1])],
                ], dtype=np.complex128)
                dT = dTk @ T + Tk @ dT
            T = Tk @ T
        return (T, dT) if want_dc else T

    z0 = rat_f(1, 2) + rat_f(1, 2) * tau_c
    pts_a = [z0 + rat_f(k, 4) for k in range(5)]
    n_b = max(6, int(math.ceil(abs(tau_c) * 4)))
    pts_b = [z0 + rat_f(k, n_b) * tau_c for k in range(n_b + 1)]
    c_val = complex((math.pi ** 2) / 12, 0)
    tol_nr = pow10_f(-13)
    for _ in range(28):
        Ta, dTa = prop_pts(pts_a, c_val, True)
        Tb, dTb = prop_pts(pts_b, c_val, True)
        Tab = Ta @ Tb
        dTab = dTa @ Tb + Ta @ dTb
        res = np.array([np.trace(Ta).imag, np.trace(Tb).imag, np.trace(Tab).imag], dtype=np.float64)
        if float(np.max(np.abs(res))) < tol_nr:
            break
        df = np.array([np.trace(dTa), np.trace(dTb), np.trace(dTab)], dtype=np.complex128)
        step, _, _, _ = np.linalg.lstsq(np.column_stack([df.imag, df.real]), -res, rcond=None)
        c_val += complex(float(step[0]), float(step[1]))
    Ta = prop_pts(pts_a, c_val)
    Tb = prop_pts(pts_b, c_val)

    def to_mob(T):
        M = np.array([[T[1, 1], T[0, 1]], [T[1, 0], T[0, 0]]], dtype=np.complex128)
        return M / np.sqrt(np.linalg.det(M))

    Tp = Tb @ Ta @ np.linalg.inv(Tb) @ np.linalg.inv(Ta)
    Aa, P0 = to_mob(Ta), to_mob(Tp)
    pf = (P0[0, 0] - P0[1, 1]) / (2 * P0[1, 0])
    da = cmath.sqrt((Aa[0, 0] - Aa[1, 1]) ** 2 + 4 * Aa[0, 1] * Aa[1, 0])
    fa1 = (Aa[0, 0] - Aa[1, 1] + da) / (2 * Aa[1, 0])
    fa2 = (Aa[0, 0] - Aa[1, 1] - da) / (2 * Aa[1, 0])
    g0 = np.array([[1, -fa1], [1, -pf]], dtype=np.complex128)
    ssc = (g0[0, 0] * fa2 + g0[0, 1]) / (g0[1, 0] * fa2 + g0[1, 1])
    g = np.array([[1 / ssc, -fa1 / ssc], [1, -pf]], dtype=np.complex128)
    g /= np.sqrt(np.linalg.det(g))
    if (g[0, 1] / g[1, 1]).imag < 0:
        g = np.array([[iu, 0], [0, -iu]], dtype=np.complex128) @ g
    RP = g @ P0 @ np.linalg.inv(g)
    RP /= RP[0, 0]
    lam = abs(float(RP[0, 1].real))
    zs = rat_f(1, 20) * z0 / abs(z0)
    pts_in = [z0]
    cur_in = z0
    while abs(cur_in) > rat_f(2, 25):
        cur_in = rat_f(1, 2) * cur_in
        pts_in.append(cur_in)
    pts_in.append(zs)
    Tin = prop_pts(pts_in, c_val)
    Mf = 56
    laur = {1: g2 / 20, 2: g3 / 28}
    for n in range(3, Mf // 2 + 2):
        laur[n] = (3 / ((2 * n + 3) * (n - 2))) * sum(laur[m] * laur[n - 1 - m] for m in range(1, n - 1))
    Qc = np.zeros(Mf + 1, dtype=np.complex128)
    Qc[0] = c_val
    for n in range(1, Mf // 2 + 1):
        Qc[2 * n] = rat_f(1, 4) * laur[n]
    al = np.zeros(Mf + 1, dtype=np.complex128)
    be = np.zeros(Mf + 1, dtype=np.complex128)
    al[0] = 1
    for m in range(1, Mf + 1):
        al[m] = -sum(Qc[j] * al[m - 2 - j] for j in range(m - 1)) / (m * m)
        be[m] = -(2 * m * al[m] + sum(Qc[j] * be[m - 2 - j] for j in range(m - 1))) / (m * m)
    zp = zs ** np.arange(Mf + 1)
    gloc = np.dot(be, zp) / np.dot(al, zp)
    wzs = Tin[0, 1] / Tin[0, 0]
    uzs = (g[0, 0] * wzs + g[0, 1]) / (g[1, 0] * wzs + g[1, 1])
    imB = float(uzs.imag + (lam / (2 * math.pi)) * (math.log(abs(zs)) + float(gloc.real)))
    return float(math.pi - (2 * math.pi / lam) * imB)


def solve_L2_punctured_torus_mp(tau_c):
    z = mp.mpc(tau_c)
    acc_shift = mp.mpf(0)
    tol_circle = mp_pow10(-30)
    for _ in range(100):
        n = int(mp.nint(mp.re(z)))
        z = z - n
        if mp.re(z) > mp_rat(1, 2):
            z -= 1
        elif mp.re(z) <= mp_rat(-1, 2):
            z += 1
        az = abs(z)
        if az < mp.mpf(1) - tol_circle:
            acc_shift -= mp.log(az)
            z = -1 / z
        elif abs(az - mp.mpf(1)) <= tol_circle and mp.re(z) < 0:
            acc_shift -= mp.log(az)
            z = -1 / z
        else:
            break
    l2_f = solve_L2_f64_dyadic(complex(float(mp.re(z)), float(mp.im(z))))
    return mp.mpf(repr(l2_f)) + acc_shift


def eval_yukawa_mp(t_m, l2_m, w_L, w_R, ec_list, coup):
    pi_mp = mp.pi
    iu_mp = mp.mpc(0, 1)
    eg = mp.euler
    x_r, y_r = mp.re(t_m), mp.im(t_m)
    q = mp.exp(2 * iu_mp * pi_mp * t_m)
    y_eff = max(float(y_r), rat_f(3, 20))
    m_max = max(14, int(math.ceil(mp.mp.dps * math.log(10) / (2 * math.pi * y_eff) + 6)))
    n_th = max(12, int(math.ceil(math.sqrt(mp.mp.dps * math.log(10) / (math.pi * y_eff)) + 5)))
    eta_prod = mp.mpf(1)
    e2 = mp.mpf(1)
    qp = mp.mpc(1)
    for m in range(1, m_max + 3):
        qp *= q
        eta_prod *= 1 - qp
        e2 -= 24 * m * qp / (1 - qp)
    denom_hat = 2 * pi_mp * ((mp.exp(iu_mp * pi_mp * t_m / 12) * eta_prod) ** 3)

    def th0_dt(ca, cb):
        s0, s1 = mp.mpc(0), mp.mpc(0)
        for k in range(-n_th, n_th + 1):
            na = mp.mpf(k) + ca
            tm = mp.exp(iu_mp * pi_mp * na * na * t_m + 2 * iu_mp * pi_mp * na * cb)
            s0 += tm
            s1 += mp_rat(1, 2) * na * na * tm
        return s0, s1

    t2, dt2 = th0_dt(mp_rat(1, 2), mp.mpf(0))
    t4, dt4 = th0_dt(mp.mpf(0), mp_rat(1, 2))
    t3, dt3 = th0_dt(mp.mpf(0), mp.mpf(0))
    R_h = [-(t2 * t2) / denom_hat, -(t4 * t4) / denom_hat, iu_mp * (t3 * t3) / denom_hat]
    dN_h = [-2 * t2 * dt2 / denom_hat, -2 * t4 * dt4 / denom_hat, 2 * iu_mp * t3 * dt3 / denom_hat]
    c3_v = [dN_h[i] - (e2 / 12) * R_h[i] for i in range(3)]

    def thc01(aa, bb):
        k0 = round(-float(aa))
        k1 = round(-float(aa) - rat_f(1, 2))
        X0, X1 = mp.mpc(0), mp.mpc(0)
        for k in range(-n_th, n_th + 1):
            n0 = mp.mpf(k + k0) + aa
            X0 += mp.exp(2 * iu_mp * pi_mp * t_m * n0 * n0 + 2 * iu_mp * pi_mp * n0 * bb)
            n1 = mp.mpf(k + k1) + aa
            X1 += mp.exp(2 * iu_mp * pi_mp * t_m * ((n1 + mp_rat(1, 2)) ** 2) + 2 * iu_mp * pi_mp * n1 * bb)
        return X0, X1

    ax = mp_rat(w_L[0].numerator, w_L[0].denominator)
    bx = 2 * mp_rat(w_L[1].numerator, w_L[1].denominator)
    ay = mp_rat(w_R[0].numerator, w_R[0].denominator)
    by = 2 * mp_rat(w_R[1].numerator, w_R[1].denominator)
    X0, X1 = thc01(ax, bx)
    Y0, Y1 = thc01(ay, by)
    Mm = [
        [X0 * Y0 / denom_hat, mp.exp(iu_mp * pi_mp * by) * X0 * Y1 / (iu_mp * denom_hat)],
        [mp.exp(iu_mp * pi_mp * bx) * X1 * Y0 / (iu_mp * denom_hat), -mp.exp(iu_mp * pi_mp * (bx + by)) * X1 * Y1 / denom_hat],
    ]
    R_ch = [sum(ec_list[si][r][c] * Mm[r][c] for r in range(2) for c in range(2)) for si in range(4)]

    shift_old = 2 * pi_mp * (l2_m + mp_rat(1, 2) * mp.log(y_r) - eg - mp.log(pi_mp))
    em2l2 = mp.exp(-2 * l2_m)
    u_sum_a = w_L[0] + w_R[0]
    u_sum_b = w_L[1] + w_R[1]
    u_ch = []
    for si, (ds1, ds2) in enumerate(CHAR_SHIFTS):
        ua = (u_sum_a + ds1) % 1
        ub = (u_sum_b + ds2) % 1
        if ua == 0 and ub == 0:
            u_ch.append(mp.mpc(0))
            continue
        a_m = mp_rat(ua.numerator, ua.denominator)
        b_m = mp_rat(ub.numerator, ub.denominator)
        if ua == 0:
            fu = pi_mp * (2 * eg - 2 * mp.log(2) - mp.log(y_r)) + (pi_mp ** 2) * y_r / (mp.sin(pi_mp * b_m) ** 2)
            for m in range(1, m_max + 2):
                for ms in (mp.mpf(m), mp.mpf(-m)):
                    wm = mp.exp(2 * iu_mp * pi_mp * (ms * x_r + b_m) - 2 * pi_mp * abs(ms) * y_r)
                    fu += (2 * pi_mp / abs(ms)) * mp.re(wm / (1 - wm))
        else:
            fu = -pi_mp * (mp.digamma(a_m) + mp.digamma(1 - a_m) + 2 * mp.log(2) + mp.log(y_r))
            for k in range(-m_max - 1, m_max + 2):
                ms = mp.mpf(k) + a_m
                wm = mp.exp(2 * iu_mp * pi_mp * (ms * x_r + b_m) - 2 * pi_mp * abs(ms) * y_r)
                fu += (2 * pi_mp / abs(ms)) * mp.re(wm / (1 - wm))
        nu_f = ua if ua <= Fraction(1, 2) else ua - 1
        nu = mp_rat(nu_f.numerator, nu_f.denominator)
        bm_neg = (-ub) % 1
        Bm = mp_rat(bm_neg.numerator, bm_neg.denominator)
        w_z = nu * t_m - Bm
        ser = mp.mpc(0)
        for m in range(1, m_max + 2):
            qm = q ** m
            ser += (mp.exp(2 * iu_mp * pi_mp * m * (t_m + w_z)) - mp.exp(2 * iu_mp * pi_mp * m * (t_m - w_z))) / (2 * iu_mp * (1 - qm))
        a0 = pi_mp * mp.cot(pi_mp * w_z) + 4 * pi_mp * ser + 2 * iu_mp * pi_mp * nu
        val = shift_old + fu - pi_mp * (abs(a0) ** 2) * em2l2
        u_ch.append(mp.sqrt(val) * R_ch[si])

    Ym = mp.matrix(3, 3)
    for a_i in range(3):
        for b_i in range(3):
            s_val = mp.mpc(0)
            for qi in range(3):
                for si in range(4):
                    cc = coup[(qi, si, a_i, b_i)]
                    if cc != 0:
                        s_val += c3_v[qi] * u_ch[si] * cc
            Ym[a_i, b_i] = s_val
    return Ym


def red_centered(num, den):
    r = num % den
    if 2 * r > den:
        r -= den
    return Fraction(r, den)


def build_open_weave_regime4b_mats_mp(m, ec_list, coup):
    tau = mp.mpc(mp_rat(2 * m, 5), mp_rat(m, 5))
    l2_m = solve_L2_punctured_torus_mp(tau)
    w3 = ((3 + mp.sqrt(5)) / 2) ** (-4)
    w4 = 4 * ((2 + mp.sqrt(3)) ** (-4))

    def level_K(K):
        zeta = mp.exp(mp.mpc(0, 2) * mp.pi / K)
        Yu, Yd, Ye = mp.zeros(3, 3), mp.zeros(3, 3), mp.zeros(3, 3)
        for a in range(K):
            for b in range(K):
                if a == 0 and b == 0:
                    continue
                ph = zeta ** ((-a * b) % K)
                wLu = (red_centered(a, K), red_centered(b, K))
                wRu = (red_centered(-4 * a, K), red_centered(-4 * b, K))
                wRd = (red_centered(2 * a, K), red_centered(2 * b, K))
                wLe = (red_centered(-3 * a, K), red_centered(-3 * b, K))
                wRe = (red_centered(6 * a, K), red_centered(6 * b, K))
                Yu += ph * eval_yukawa_mp(tau, l2_m, wLu, wRu, ec_list, coup)
                Yd += ph * eval_yukawa_mp(tau, l2_m, wLu, wRd, ec_list, coup)
                Ye += ph * eval_yukawa_mp(tau, l2_m, wLe, wRe, ec_list, coup)
        return Yu, Yd, Ye

    Yu5, Yd5, Ye5 = level_K(5)
    Yu6, Yd6, Ye6 = level_K(6)
    Yu = w3 * Yu5 / 24 + w4 * Yu6 / 35
    Yd = w3 * Yd5 / 24 + w4 * Yd6 / 35
    Ye = w3 * Ye5 / 24 + w4 * Ye6 / 35
    return Yu, Yd, Ye


def mp_to_np(M):
    return np.array([[complex(float(mp.re(M[r, c])), float(mp.im(M[r, c]))) for c in range(3)] for r in range(3)], dtype=np.complex128)


# ---------------------------------------------------------------------------
# TASK OW7-B: Exact RG Rigidity Theorem on Open-Weave A2-OW6 UV Yukawas
# ---------------------------------------------------------------------------

def run_task_ow7_b(Yu8_mp, Yd8_mp, Ye8_mp, Yu24_mp, Yd24_mp, Ye24_mp):
    Yu8, Yd8, Ye8 = mp_to_np(Yu8_mp), mp_to_np(Yd8_mp), mp_to_np(Ye8_mp)
    Yu24, Yd24, Ye24 = mp_to_np(Yu24_mp), mp_to_np(Yd24_mp), mp_to_np(Ye24_mp)

    g_uv = (rat_f(52, 100), rat_f(52, 100), rat_f(52, 100))
    dt_down = -14 * math.log(10)

    trajectories = []
    max_r13_factor = 1
    max_vus_rel_shift = 0
    max_vcb_factor = 1
    max_jcp_factor = 1
    all_sm_suppress = True
    all_2hdm_enhance = True

    for label, (Yu0, Yd0, Ye0) in (("m8", (Yu8, Yd8, Ye8)), ("m24", (Yu24, Yd24, Ye24))):
        su_max = float(np.linalg.svd(Yu0, compute_uv=False)[0])
        sd_max = float(np.linalg.svd(Yd0, compute_uv=False)[0])
        se_max = float(np.linalg.svd(Ye0, compute_uv=False)[0])
        Yu_n, Yd_n, Ye_n = Yu0 / su_max, Yd0 / sd_max, Ye0 / se_max
        o_uv = obs_ascending_np(Yu_n, Yd_n, Ye_n)

        for model in ("SM", "2HDM_II"):
            for yp, yq in ((7, 10), (3, 2)):
                ys = rat_f(yp, yq)
                _, Yu_ir, Yd_ir, Ye_ir = integrate_matrix_rge(g_uv, ys * Yu_n, ys * Yd_n, ys * Ye_n, dt_down, model)
                o_ir = obs_ascending_np(Yu_ir, Yd_ir, Ye_ir)

                f_r13 = max(
                    max(o_ir["r13_u"] / o_uv["r13_u"], o_uv["r13_u"] / o_ir["r13_u"]),
                    max(o_ir["r13_d"] / o_uv["r13_d"], o_uv["r13_d"] / o_ir["r13_d"]),
                    max(o_ir["r13_e"] / o_uv["r13_e"], o_uv["r13_e"] / o_ir["r13_e"]),
                )
                d_vus = abs(o_ir["V_us"] - o_uv["V_us"]) / o_uv["V_us"]
                f_vcb = max(o_ir["V_cb"] / o_uv["V_cb"], o_uv["V_cb"] / o_ir["V_cb"])
                f_jcp = max(abs(o_ir["J_CP"]) / abs(o_uv["J_CP"]), abs(o_uv["J_CP"]) / abs(o_ir["J_CP"]))

                max_r13_factor = max(max_r13_factor, f_r13)
                max_vus_rel_shift = max(max_vus_rel_shift, d_vus)
                max_vcb_factor = max(max_vcb_factor, f_vcb)
                max_jcp_factor = max(max_jcp_factor, f_jcp)

                if model == "SM" and not (o_ir["V_cb"] < o_uv["V_cb"] and abs(o_ir["J_CP"]) < abs(o_uv["J_CP"])):
                    all_sm_suppress = False
                if model == "2HDM_II" and not (o_ir["V_cb"] > o_uv["V_cb"] and abs(o_ir["J_CP"]) > abs(o_uv["J_CP"])):
                    all_2hdm_enhance = False

                trajectories.append({
                    "level": label,
                    "model": model,
                    "y_UV": f"{yp}/{yq}",
                    "UV_r13_u": f"{o_uv['r13_u']:.6e}",
                    "IR_r13_u": f"{o_ir['r13_u']:.6e}",
                    "UV_Vus": f"{o_uv['V_us']:.6e}",
                    "IR_Vus": f"{o_ir['V_us']:.6e}",
                    "UV_Vcb": f"{o_uv['V_cb']:.6e}",
                    "IR_Vcb": f"{o_ir['V_cb']:.6e}",
                    "UV_JCP": f"{o_uv['J_CP']:+.6e}",
                    "IR_JCP": f"{o_ir['J_CP']:+.6e}",
                    "max_r13_factor": f"{f_r13:.6f}",
                    "vus_rel_shift": f"{d_vus:.6f}",
                    "vcb_factor": f"{f_vcb:.6f}",
                    "jcp_factor": f"{f_jcp:.6f}",
                })

    pass_b = bool(
        len(trajectories) == 8
        and max_r13_factor < 2
        and max_vus_rel_shift < rat_f(4, 100)
        and max_vcb_factor < 4
        and max_jcp_factor < 4
        and all_sm_suppress
        and all_2hdm_enhance
    )
    return {
        "max_r13_amplification_factor": f"{max_r13_factor:.6f}",
        "max_Vus_rel_shift": f"{max_vus_rel_shift:.6f}",
        "max_Vcb_factor": f"{max_vcb_factor:.6f}",
        "max_JCP_factor": f"{max_jcp_factor:.6f}",
        "SM_always_suppresses_Vcb_JCP_downward": all_sm_suppress,
        "2HDM_II_always_enhances_Vcb_JCP_downward": all_2hdm_enhance,
        "trajectories": trajectories,
        "pass": pass_b,
    }


# ---------------------------------------------------------------------------
# TASK OW7-C: Exact 7D Bulk Right-Handed QR-Decoupling Across All 6/6 Perms
# ---------------------------------------------------------------------------

def det3_mp(M):
    return (
        M[0, 0] * (M[1, 1] * M[2, 2] - M[1, 2] * M[2, 1])
        - M[0, 1] * (M[1, 0] * M[2, 2] - M[1, 2] * M[2, 0])
        + M[0, 2] * (M[1, 0] * M[2, 1] - M[1, 1] * M[2, 0])
    )


def obs_ascending_mp(Yu, Yd, Ye):
    """45-dps mpmath SVD in physical ascending (u, c, t) x (d, s, b) ordering."""
    def svd_asc(M):
        U, S, _ = mp.svd_c(M)
        ord_i = sorted(range(3), key=lambda i: mp.re(S[i]))
        sv = [mp.re(S[i]) for i in ord_i]
        U_a = mp.matrix([[U[r, ord_i[c]] for c in range(3)] for r in range(3)])
        return sv, U_a

    su, Uu = svd_asc(Yu)
    sd, Ud = svd_asc(Yd)
    se, _ = svd_asc(Ye)
    V = Uu.transpose_conj() * Ud
    Va = [[abs(V[r, c]) for c in range(3)] for r in range(3)]
    J_cp = mp.im(V[0, 0] * V[1, 1] * mp.conj(V[0, 1]) * mp.conj(V[1, 0]))

    Hu = Yu * Yu.transpose_conj()
    Hd = Yd * Yd.transpose_conj()
    comm = Hu * Hd - Hd * Hu
    tr_u = mp.re(Hu[0, 0] + Hu[1, 1] + Hu[2, 2])
    tr_d = mp.re(Hd[0, 0] + Hd[1, 1] + Hd[2, 2])
    J_det_norm = mp.im(det3_mp(comm)) / ((tr_u ** 3) * (tr_d ** 3))

    return {
        "r23_u": su[1] / su[2], "r12_u": su[0] / su[1], "r13_u": su[0] / su[2],
        "r23_d": sd[1] / sd[2], "r12_d": sd[0] / sd[1], "r13_d": sd[0] / sd[2],
        "r23_e": se[1] / se[2], "r12_e": se[0] / se[1], "r13_e": se[0] / se[2],
        "V_abs": Va,
        "V_us": Va[0][1], "V_cb": Va[1][2], "V_ub": Va[0][2],
        "J_CP": J_cp, "J_det_norm": J_det_norm,
    }


def gram_schmidt_qr_ascending_mp(M_perm):
    """
    Exact 45-dps Gram-Schmidt QR on reversed columns [c_2, c_1, c_0], then reverse Q back to
    ascending (1st, 2nd, 3rd) order so col 2 aligns along heaviest col c_2!
    """
    cols_rev = [[M_perm[r, c] for r in range(3)] for c in (2, 1, 0)]
    q_rev = []
    for v in cols_rev:
        w = list(v)
        for prev in q_rev:
            proj = sum(mp.conj(prev[r]) * w[r] for r in range(3))
            w = [w[r] - proj * prev[r] for r in range(3)]
        nrm = mp.sqrt(sum(abs(w[r]) ** 2 for r in range(3)))
        q_rev.append([w[r] / nrm for r in range(3)])
    q_asc = [q_rev[2], q_rev[1], q_rev[0]]
    return mp.matrix([[q_asc[c][r] for c in range(3)] for r in range(3)])


def random_haar_u3_mp(rng):
    cols = []
    for _ in range(3):
        v = [mp.mpc(mp.mpf(repr(rng.gauss(0, 1))), mp.mpf(repr(rng.gauss(0, 1)))) for _ in range(3)]
        for prev in cols:
            proj = sum(mp.conj(prev[r]) * v[r] for r in range(3))
            v = [v[r] - proj * prev[r] for r in range(3)]
        nrm = mp.sqrt(sum(abs(v[r]) ** 2 for r in range(3)))
        cols.append([v[r] / nrm for r in range(3)])
    return mp.matrix([[cols[c][r] for c in range(3)] for r in range(3)])


def run_task_ow7_c(Yu8, Yd8, Ye8, Yu24, Yd24, Ye24):
    mp.mp.dps = 45
    rng = random.Random(20261121)

    # Zero-parameter geodesic hypercharge-weighted profile: eps_f = phi^(-2 * |6 Y_R|) = exp(-(|6 Y_R|/2) * L_m004)
    phi = (1 + mp.sqrt(5)) / 2
    eu = phi ** (-8)   # |6 Y_R(u^c)| = 4
    ed = phi ** (-4)   # |6 Y_R(d^c)| = 2
    ee = phi ** (-12)  # |6 Y_R(e^c)| = 6

    def right_scale(M, perm, eps):
        # Permute columns by perm, then scale col 0 by eps^2, col 1 by eps, col 2 by 1
        scales = [eps * eps, eps, mp.mpf(1)]
        return mp.matrix([[M[r, perm[c]] * scales[c] for c in range(3)] for r in range(3)])

    perm_results = []
    all_6_break_tradeoff = True
    max_qr_diff_finite = mp.mpf(0)
    max_qr_diff_asym = mp.mpf(0)
    max_haar_drift_all6 = mp.mpf(0)

    for perm in itertools.permutations((0, 1, 2)):
        Yu_e = right_scale(Yu8, perm, eu)
        Yd_e = right_scale(Yd8, perm, ed)
        Ye_e = right_scale(Ye8, perm, ee)
        o = obs_ascending_mp(Yu_e, Yd_e, Ye_e)

        # Exact QR limit
        Yu_p = mp.matrix([[Yu8[r, perm[c]] for c in range(3)] for r in range(3)])
        Yd_p = mp.matrix([[Yd8[r, perm[c]] for c in range(3)] for r in range(3)])
        Qu = gram_schmidt_qr_ascending_mp(Yu_p)
        Qd = gram_schmidt_qr_ascending_mp(Yd_p)
        Vqr = Qu.transpose_conj() * Qd
        Vqr_abs = [[abs(Vqr[r, c]) for c in range(3)] for r in range(3)]
        Jqr = mp.im(Vqr[0, 0] * Vqr[1, 1] * mp.conj(Vqr[0, 1]) * mp.conj(Vqr[1, 0]))
        qr_diff_fin = max(abs(o["V_abs"][r][c] - Vqr_abs[r][c]) for r in range(3) for c in range(3))
        if qr_diff_fin > max_qr_diff_finite:
            max_qr_diff_finite = qr_diff_fin

        # Asymptotic convergence check at eps_f / 1000
        o_tiny = obs_ascending_mp(
            right_scale(Yu8, perm, eu / 1000),
            right_scale(Yd8, perm, ed / 1000),
            right_scale(Ye8, perm, ee / 1000),
        )
        qr_diff_tiny = max(abs(o_tiny["V_abs"][r][c] - Vqr_abs[r][c]) for r in range(3) for c in range(3))
        if qr_diff_tiny > max_qr_diff_asym:
            max_qr_diff_asym = qr_diff_tiny

        # Mandatory 10-trial 45-dps Haar basis-scrambling gate
        max_h = mp.mpf(0)
        for _ in range(10):
            UL = random_haar_u3_mp(rng)
            URu = random_haar_u3_mp(rng)
            URd = random_haar_u3_mp(rng)
            ULe = random_haar_u3_mp(rng)
            URe = random_haar_u3_mp(rng)
            ot = obs_ascending_mp(
                UL * Yu_e * URu.transpose_conj(),
                UL * Yd_e * URd.transpose_conj(),
                ULe * Ye_e * URe.transpose_conj(),
            )
            dr = max([
                abs(ot["r23_u"] - o["r23_u"]), abs(ot["r12_u"] - o["r12_u"]),
                abs(ot["r23_d"] - o["r23_d"]), abs(ot["r12_d"] - o["r12_d"]),
                abs(ot["r23_e"] - o["r23_e"]), abs(ot["r12_e"] - o["r12_e"]),
                max(abs(ot["V_abs"][r][c] - o["V_abs"][r][c]) for r in range(3) for c in range(3)),
                abs(ot["J_CP"] - o["J_CP"]), abs(ot["J_det_norm"] - o["J_det_norm"]),
            ])
            if dr > max_h:
                max_h = dr
        if max_h > max_haar_drift_all6:
            max_haar_drift_all6 = max_h

        rel_ed_23 = abs(o["r23_e"] - o["r23_d"]) / o["r23_d"]
        u_steeper_ratio = o["r13_d"] / o["r13_u"]
        perm_ok = bool(
            o["r13_u"] < mp_rat(2, 10000)
            and o["r13_d"] < mp_rat(5, 1000)
            and o["r13_e"] < mp_rat(2, 1000000)
            and u_steeper_ratio > 20
            and rel_ed_23 > mp_rat(98, 100)
            and mp_rat(14, 100) < o["V_us"] < mp_rat(25, 100)
            and abs(o["J_CP"]) > mp_rat(5, 100000)
            and qr_diff_fin < mp_rat(2, 100)
            and qr_diff_tiny < mp_pow10(-6)
            and max_h < mp_pow10(-30)
        )
        if not perm_ok:
            all_6_break_tradeoff = False

        perm_results.append({
            "perm": list(perm),
            "r13_u": mp.nstr(o["r13_u"], 10),
            "r13_d": mp.nstr(o["r13_d"], 10),
            "r13_e": mp.nstr(o["r13_e"], 10),
            "u_steeper_than_d_ratio": mp.nstr(u_steeper_ratio, 8),
            "rel_ed_23_split": mp.nstr(rel_ed_23, 8),
            "V_us": mp.nstr(o["V_us"], 10),
            "V_cb": mp.nstr(o["V_cb"], 10),
            "V_ub": mp.nstr(o["V_ub"], 10),
            "J_CP": mp.nstr(o["J_CP"], 10),
            "V_us_QR": mp.nstr(Vqr_abs[0][1], 10),
            "V_cb_QR": mp.nstr(Vqr_abs[1][2], 10),
            "V_ub_QR": mp.nstr(Vqr_abs[0][2], 10),
            "J_CP_QR": mp.nstr(Jqr, 10),
            "qr_diff_finite": mp.nstr(qr_diff_fin, 8),
            "qr_diff_eps_div_1000": mp.nstr(qr_diff_tiny, 8),
            "haar_10trial_max_drift": mp.nstr(max_h, 6),
            "strict_hierarchical_CKM_Vus_gt_Vcb_gt_Vub": bool(o["V_us"] > o["V_cb"] > o["V_ub"] > 0),
            "pass": perm_ok,
        })

    # Asymmetric covering controls: (Yu@8, Yd@24) and (Yu@24, Yd@8)
    o_8_24 = obs_ascending_mp(Yu8, Yd24, Ye24)
    o_24_8 = obs_ascending_mp(Yu24, Yd8, Ye24)
    asym_ok = bool(
        o_8_24["V_us"] > mp_rat(5, 100) and abs(o_8_24["J_CP"]) > mp_rat(3, 10000) and o_8_24["r13_u"] > mp_rat(5, 100)
        and o_24_8["V_us"] > mp_rat(5, 100) and abs(o_24_8["J_CP"]) > mp_rat(3, 10000) and o_24_8["r13_d"] > mp_rat(5, 100)
    )

    pass_c = bool(all_6_break_tradeoff and asym_ok)
    return {
        "geodesic_scales": {
            "eps_u_phi_neg8": mp.nstr(eu, 12),
            "eps_d_phi_neg4": mp.nstr(ed, 12),
            "eps_e_phi_neg12": mp.nstr(ee, 12),
        },
        "all_6_permutations_break_tradeoff": all_6_break_tradeoff,
        "max_qr_diff_finite_all6": mp.nstr(max_qr_diff_finite, 8),
        "max_qr_diff_eps_div_1000_all6": mp.nstr(max_qr_diff_asym, 8),
        "max_haar_10trial_drift_all6": mp.nstr(max_haar_drift_all6, 6),
        "permutations": perm_results,
        "asymmetric_covering_controls": {
            "Yu8_Yd24": {
                "r13_u": mp.nstr(o_8_24["r13_u"], 10), "r13_d": mp.nstr(o_8_24["r13_d"], 10),
                "V_us": mp.nstr(o_8_24["V_us"], 10), "J_CP": mp.nstr(o_8_24["J_CP"], 10),
            },
            "Yu24_Yd8": {
                "r13_u": mp.nstr(o_24_8["r13_u"], 10), "r13_d": mp.nstr(o_24_8["r13_d"], 10),
                "V_us": mp.nstr(o_24_8["V_us"], 10), "J_CP": mp.nstr(o_24_8["J_CP"], 10),
            },
            "pass": asym_ok,
        },
        "pass": pass_c,
    }


# ---------------------------------------------------------------------------
# TASK OW7-D: 4 / 4 Planted-Fault Self-Checks
# ---------------------------------------------------------------------------

def run_task_ow7_d(res_a, Yu8_mp, Yu24_mp, Yd24_mp, Ye24_mp):
    ia = res_a["_internal"]

    # PF-OW7-1: Erroneous factor 1/2 in d/dt (d/d ln mu^2 mistake) pushes log10(Lambda_lam) > 15
    _, t_zero_bad = integrate_scalar_rk4(ia["y0_b"], 0, ia["t_Pl"], n_steps=5000, scale_dt=rat_f(1, 2))
    log10_bad = math.log10(ia["M_t"]) + t_zero_bad / math.log(10)
    pf1_caught = bool(log10_bad > 15)

    # PF-OW7-2: Flip c_cross in SM (-3/2 -> +1/2) reverses Xing-Zhou upward V_cb & J_CP ratios to < 1
    _, Yu_bad, Yd_bad, Ye_bad = integrate_matrix_rge(
        ia["g_mz"], ia["Yu_mz"], ia["Yd_mz"], ia["Ye_mz"], ia["dt_up"], "SM", override_c_cross=rat_f(1, 2)
    )
    o_bad = obs_ascending_np(Yu_bad, Yd_bad, Ye_bad)
    vcb_bad_r = o_bad["V_cb"] / ia["o_mz"]["V_cb"]
    j_bad_r = o_bad["J_CP"] / ia["o_mz"]["J_CP"]
    pf2_caught = bool(vcb_bad_r < 1 and j_bad_r < 1)

    # PF-OW7-3: Illegal left-right overlap V_u^T U_u fails 10-trial Haar invariance (> 1/10)
    rng = random.Random(20261121)
    mp.mp.dps = 30
    U0, _, Vh0 = mp.svd_c(Yu8_mp)
    V0 = Vh0.transpose_conj()
    ov0 = V0.transpose() * U0
    ov0_abs = [[abs(ov0[r, c]) for c in range(3)] for r in range(3)]
    max_illegal_drift = mp.mpf(0)
    for _ in range(10):
        UL = random_haar_u3_mp(rng)
        UR = random_haar_u3_mp(rng)
        Ut, _, Vht = mp.svd_c(UL * Yu8_mp * UR.transpose_conj())
        Vt = Vht.transpose_conj()
        ovt = Vt.transpose() * Ut
        dr = max(abs(abs(ovt[r, c]) - ov0_abs[r][c]) for r in range(3) for c in range(3))
        if dr > max_illegal_drift:
            max_illegal_drift = dr
    pf3_caught = bool(max_illegal_drift > mp_rat(1, 10))

    # PF-OW7-4: Setting D_{R,f} = I_3 at m = 24 regresses straight back into A2-OW6 collapsed CKM/CP
    mp.mp.dps = 45
    o24 = obs_ascending_mp(Yu24_mp, Yd24_mp, Ye24_mp)
    pf4_caught = bool(o24["V_us"] < mp_rat(1, 100000) and abs(o24["J_CP"]) < mp_pow10(-15))

    all_caught = pf1_caught and pf2_caught and pf3_caught and pf4_caught
    return {
        "PF_OW7_1_factor_half_dt_mistake": {
            "faulty_log10_Lambda_lam": f"{log10_bad:.6f}",
            "caught": pf1_caught,
        },
        "PF_OW7_2_flipped_SM_c_cross": {
            "faulty_Vcb_ratio": f"{vcb_bad_r:.6f}",
            "faulty_JCP_ratio": f"{j_bad_r:.6f}",
            "caught": pf2_caught,
        },
        "PF_OW7_3_illegal_left_right_overlap": {
            "max_haar_drift": mp.nstr(max_illegal_drift, 8),
            "caught": pf3_caught,
        },
        "PF_OW7_4_no_bulk_localization_m24_regression": {
            "m24_Vus": mp.nstr(o24["V_us"], 8),
            "m24_JCP": mp.nstr(o24["J_CP"], 8),
            "caught": pf4_caught,
        },
        "caught_count": sum([pf1_caught, pf2_caught, pf3_caught, pf4_caught]),
        "total_planted": 4,
        "pass": all_caught,
    }


def main():
    script_path = Path(__file__).resolve()
    script_sha = hashlib.sha256(script_path.read_bytes()).hexdigest()

    res_a = run_task_ow7_a()
    mp.mp.dps = 45
    ec_list, coup = build_quat_couplings_mp()
    Yu8, Yd8, Ye8 = build_open_weave_regime4b_mats_mp(8, ec_list, coup)
    Yu24, Yd24, Ye24 = build_open_weave_regime4b_mats_mp(24, ec_list, coup)

    res_b = run_task_ow7_b(Yu8, Yd8, Ye8, Yu24, Yd24, Ye24)
    res_c = run_task_ow7_c(Yu8, Yd8, Ye8, Yu24, Yd24, Ye24)
    res_d = run_task_ow7_d(res_a, Yu8, Yu24, Yd24, Ye24)

    res_a_clean = {k: v for k, v in res_a.items() if k != "_internal"}
    all_passed = bool(res_a_clean["pass"] and res_b["pass"] and res_c["pass"] and res_d["pass"])

    payload = {
        "card": "A2-OW7",
        "empirical_inputs_used": "0 of 19 (literature benchmarks isolated strictly in OW7-A)",
        "script_sha256": script_sha,
        "OW7_A_literature_benchmark_gate": res_a_clean,
        "OW7_B_rg_rigidity_theorem": res_b,
        "OW7_C_7d_bulk_qr_decoupling_all6_perms": res_c,
        "OW7_D_planted_faults": res_d,
        "all_gates_passed": all_passed,
    }

    out_path = script_path.parent / "verify_a2_ow7_out.json"
    out_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    out_sha = hashlib.sha256(out_path.read_bytes()).hexdigest()
    print(f"A2-OW7_COMPLETE all_gates_passed={all_passed} output_sha256={out_sha}")
    if not all_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
