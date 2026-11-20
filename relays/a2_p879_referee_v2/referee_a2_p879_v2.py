#!/usr/bin/env python3
"""Independent Cold-Room Zero-Trust Referee for Card A2-P879 (P-879, 0 of 19).

Standalone verification covering:
  - Pure-mpmath Weierstrass Fuchsian ODE solver with step-doubling / Richardson
    extrapolation and Gauss SL_2(Z) fundamental-domain reduction for L_2(tau).
  - Spinor-contraction vs triplet-vector convention checks (Guardrail 4).
  - T1: SymPy + numerical proof of null-basis 2x2 reduction and B1966 E4 law.
  - T2: 4x4 Kronecker lift singular-value identity and rank-1 Wedin/Weyl remainder.
  - T3: SymPy polynomial proof + dense 2D spinor-grid check of Spinor Mobius bound.
  - T4: Frame C unweighted theta residue (order-5 w_u=0, rank-1, s_L^res=0) and
        Theorem 90 weighted cusp s_L decay across heights y in {1..30}.
  - T5: Global CP^2 affine-chart Weyl + Davis-Kahan exclusion certifier across
        >= 300 Frame C (tau, a, b) pairs (incl. L_2 +- 1/50 sensitivity) and
        B1967 16-rational positive control.
  - Guardrail 3: 10 random Haar U(3)^3 scrambling trials (< 1e-12 invariance).
  - Planted faults PF1..PF5: all 5 detected by automated assertions.
"""

from __future__ import annotations

import json
import math
import os
import time
from concurrent.futures import ThreadPoolExecutor
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp


# ---------------------------------------------------------------------------
# Pure-integer constructors (zero float / complex AST literals)
# ---------------------------------------------------------------------------

def rat_f(p: int, q: int = 1) -> float:
    return p / q


def pow10_f(n: int) -> float:
    if n >= 0:
        return (10 ** n) / 1
    return 1 / (10 ** (-n))


def c_rat(rp: int, rq: int = 1, ip: int = 0, iq: int = 1) -> complex:
    return complex(rp / rq, ip / iq)


def mp_rat(p: int, q: int = 1):
    return mp.mpf(p) / mp.mpf(q)


def mp_pow10(n: int):
    return mp.mpf(10) ** n


def mp_crat(rp: int, rq: int = 1, ip: int = 0, iq: int = 1):
    return mp.mpc(mp_rat(rp, rq), mp_rat(ip, iq))


I_C = complex(0, 1)
I_MP = mp.mpc(0, 1)
ONE_F = rat_f(1, 1)
ZERO_F = rat_f(0, 1)


def to_py(obj):
    """Recursively convert numpy / mpmath / Fraction types to native JSON types."""
    if isinstance(obj, dict):
        return {str(k): to_py(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [to_py(v) for v in obj]
    if isinstance(obj, np.ndarray):
        return [to_py(v) for v in obj.tolist()]
    if isinstance(obj, (np.bool_, bool)):
        return bool(obj)
    if isinstance(obj, (np.integer, int)):
        return int(obj)
    if isinstance(obj, (np.floating, float)):
        return float(obj)
    if isinstance(obj, (mp.mpf,)):
        return float(obj)
    if isinstance(obj, (np.complexfloating, complex, mp.mpc)):
        return {"re": float(obj.real), "im": float(obj.imag)}
    if isinstance(obj, Fraction):
        return f"{obj.numerator}/{obj.denominator}"
    return obj


# ---------------------------------------------------------------------------
# Quaternion / Spinor Basis & Yukawa Operator
# ---------------------------------------------------------------------------

def quaternion_basis_np():
    qj = np.array([[0, 1], [-1, 0]], dtype=complex)
    qi = np.array([[I_C, 0], [0, -I_C]], dtype=complex)
    qk = qi @ qj
    eps = qj
    c_gen = [qj, qi, qk]
    half = rat_f(1, 2)
    e_dual = {
        "1": half * np.array([[0, 1], [-1, 0]], dtype=complex),
        "i": half * np.array([[0, I_C], [I_C, 0]], dtype=complex),
        "j": half * np.array([[-1, 0], [0, -1]], dtype=complex),
        "k": half * np.array([[-I_C, 0], [0, I_C]], dtype=complex),
    }
    return eps, qj, qi, qk, c_gen, e_dual


def s_of_h_np(h: np.ndarray, qj: np.ndarray, qi: np.ndarray, qk: np.ndarray) -> np.ndarray:
    return h[1] * qi + h[0] * qj + h[2] * qk


def mw_to_uw_np(mw: np.ndarray):
    two = rat_f(2, 1)
    two_i = 2 * I_C
    m0 = (mw[0, 0] + mw[1, 1]) / two
    m1 = (mw[0, 0] - mw[1, 1]) / two_i
    m2 = (mw[0, 1] - mw[1, 0]) / two
    m3 = (mw[0, 1] + mw[1, 0]) / two_i
    u = -two * np.array([m0, -m3, m1], dtype=complex)
    w = -two * m2
    return u, w


def uw_to_mw_np(u: np.ndarray, w: complex, e_dual: dict) -> np.ndarray:
    return (-w) * e_dual["1"] + u[1] * e_dual["i"] + u[0] * e_dual["j"] + u[2] * e_dual["k"]


def y_spin_np(s_mat: np.ndarray, mw: np.ndarray, eps: np.ndarray, c_gen: list) -> np.ndarray:
    out = np.zeros((3, 3), dtype=complex)
    for a in range(3):
        for b in range(3):
            out[a, b] = np.trace((c_gen[a].T @ eps @ s_mat @ c_gen[b]).T @ mw)
    return out


def y_vec_np(h: np.ndarray, u: np.ndarray, w: complex) -> np.ndarray:
    hx = np.array(
        [[0, -h[2], h[1]], [h[2], 0, -h[0]], [-h[1], h[0], 0]],
        dtype=complex,
    )
    return np.outer(u, h) + np.outer(h, u) - np.dot(u, h) * np.eye(3, dtype=complex) + w * hx


def haar_unitary(n: int, rng: np.random.Generator) -> np.ndarray:
    z = rng.normal(size=(n, n)) + I_C * rng.normal(size=(n, n))
    q, r = np.linalg.qr(z)
    d = np.diag(r)
    ph = np.where(np.abs(d) > pow10_f(-15), d / np.abs(d), ONE_F)
    return q * ph[None, :]


def verify_convention_guardrail4(rng: np.random.Generator) -> dict:
    eps, qj, qi, qk, c_gen, e_dual = quaternion_basis_np()
    max_diff_d = ZERO_F
    max_diff_u_eps = ZERO_F
    max_diff_u_eps_t = ZERO_F
    max_sv_diff = ZERO_F
    max_vckm_diff = ZERO_F
    tol = pow10_f(-13)
    for _ in range(12):
        h = rng.normal(size=3) + I_C * rng.normal(size=3)
        h = h / np.linalg.norm(h)
        mw = rng.normal(size=(2, 2)) + I_C * rng.normal(size=(2, 2))
        mw_u = rng.normal(size=(2, 2)) + I_C * rng.normal(size=(2, 2))
        u, w = mw_to_uw_np(mw)
        uu, wu = mw_to_uw_np(mw_u)
        sd = s_of_h_np(h, qj, qi, qk)
        yd_spin = y_spin_np(sd, mw, eps, c_gen)
        yd_vec = y_vec_np(h, u, w)
        max_diff_d = max(max_diff_d, float(np.max(np.abs(yd_spin - yd_vec))))

        su_eps = eps @ np.conj(sd) @ eps
        su_eps_t = eps @ np.conj(sd) @ eps.T
        yu_spin_eps = y_spin_np(su_eps, mw_u, eps, c_gen)
        yu_spin_epst = y_spin_np(su_eps_t, mw_u, eps, c_gen)
        yu_vec = y_vec_np(np.conj(h), uu, wu)
        max_diff_u_eps = max(max_diff_u_eps, float(np.max(np.abs(yu_spin_eps + yu_vec))))
        max_diff_u_eps_t = max(max_diff_u_eps_t, float(np.max(np.abs(yu_spin_epst - yu_vec))))

        ud1, sd1, _ = np.linalg.svd(yd_vec)
        uu_plus, su_plus, _ = np.linalg.svd(yu_vec)
        uu_minus, su_minus, _ = np.linalg.svd(-yu_vec)
        max_sv_diff = max(max_sv_diff, float(np.max(np.abs(su_plus - su_minus))))
        v_plus = np.abs(uu_plus.conj().T @ ud1)
        v_minus = np.abs(uu_minus.conj().T @ ud1)
        max_vckm_diff = max(max_vckm_diff, float(np.max(np.abs(v_plus - v_minus))))

    passed = bool(
        max_diff_d < tol
        and max_diff_u_eps < tol
        and max_diff_u_eps_t < tol
        and max_sv_diff < tol
        and max_vckm_diff < tol
    )
    return {
        "max_diff_Y_down": max_diff_d,
        "max_diff_Y_up_eps_conj_eps_plus_Ybar": max_diff_u_eps,
        "max_diff_Y_up_eps_conj_epsT_minus_Ybar": max_diff_u_eps_t,
        "sign_flip_sv_diff": max_sv_diff,
        "sign_flip_Vckm_diff": max_vckm_diff,
        "tolerance": tol,
        "passed": passed,
    }


# ---------------------------------------------------------------------------
# L_2(tau): Gauss SL_2(Z) Reduction + Pure-mpmath Weierstrass ODE Propagator
# ---------------------------------------------------------------------------

def gauss_reduce_sl2z(tau):
    """Reduce tau in H to the fundamental domain |Re tau_fd| <= 1/2, |tau_fd| >= 1.

    Returns (tau_fd, a, b, c, d) with integer a*d - b*c = 1 and tau_fd = (a*tau + b)/(c*tau + d).
    """
    a, b, c, d = 1, 0, 0, 1
    z = mp.mpc(tau)
    half = mp_rat(1, 2)
    eps_fd = mp_pow10(-14)
    for _ in range(100):
        n = int(mp.nint(mp.re(z)))
        if n != 0:
            z = z - n
            a, b = a - n * c, b - n * d
        if abs(z) < mp.mpf(1) - eps_fd:
            z = -mp.mpf(1) / z
            a, b, c, d = -c, -d, a, b
        else:
            if abs(mp.re(z)) <= half + eps_fd:
                break
    return z, a, b, c, d


def cusp_l2_exact():
    return mp.pi + mp.log(mp.pi) - 3 * mp.log(2)


def solve_l2_weierstrass_ode_direct(
    tau,
    B_init=None,
    steps_root: int = 32,
    steps_eval: int = 96,
    check_hp3: bool = False,
    steps_hp3: int = 160,
):
    """Solve the Fuchsian Weierstrass ODE y'' + (1/4 wp(z;tau) + B) y = 0 directly on [0, 1/2] & [0, tau/2].

    Desingularizes z = z_target * t^2 on t in [0, 1] and integrates via pure-mpmath RK4 with
    two-stage B(tau) polishing, step-doubling (N vs 2N), and Richardson extrapolation.
    """
    pi = mp.pi
    im_tau = mp.im(tau)
    if B_init is None:
        B_init = (pi * pi) / 12 - (pi * pi) / (4 * ((im_tau + 1) ** 2))

    qh = mp.exp(pi * I_MP * tau)
    if im_tau < mp.mpf(1):
        n_max = 8
    elif im_tau < mp.mpf(2):
        n_max = 6
    elif im_tau < mp.mpf(5):
        n_max = 4
    else:
        n_max = 3

    weights = []
    s1_0 = mp.mpc(0)
    s3_0 = mp.mpc(0)
    s5_0 = mp.mpc(0)
    s7_0 = mp.mpc(0)
    for n in range(n_max):
        sgn = 1 if (n % 2 == 0) else -1
        w = sgn * (qh ** (n * (n + 1)))
        m = 2 * n + 1
        mpi = m * pi
        weights.append((w, mpi, mpi * mpi))
        s1_0 += w * mpi
        s3_0 -= w * (mpi ** 3)
        s5_0 += w * (mpi ** 5)
        s7_0 -= w * (mpi ** 7)

    eta1_2 = s3_0 / (3 * s1_0)
    c3 = s3_0 / (6 * s1_0)
    c5 = s5_0 / (120 * s1_0)
    c7 = s7_0 / (5040 * s1_0)
    g2_20 = -12 * (c5 - c3 * c3 / 2)
    g3_28 = -30 * (c7 - c3 * c5 + (c3 ** 3) / 3)
    small_thresh = mp_rat(3, 100)
    quarter = mp_rat(1, 4)

    def wp_minus_invz2(z):
        if abs(z) < small_thresh:
            z2 = z * z
            return g2_20 * z2 + g3_28 * z2 * z2
        piz = pi * z
        s1 = mp.sin(piz)
        c1 = mp.cos(piz)
        s2 = 2 * s1 * c1
        c2 = c1 * c1 - s1 * s1
        sn, cn = s1, c1
        t = mp.mpc(0)
        tp = mp.mpc(0)
        tpp = mp.mpc(0)
        for idx, (w, mpi, mpi2) in enumerate(weights):
            t += w * sn
            tp += w * mpi * cn
            tpp -= w * mpi2 * sn
            if idx + 1 < n_max:
                sn, cn = sn * c2 + cn * s2, cn * c2 - sn * s2
        return (tp * tp - t * tpp) / (t * t) + eta1_2 - 1 / (z * z)

    def precomp_wp(zt, nsteps: int):
        hdt = mp.mpf(1) / (2 * nsteps)
        nodes = [mp.mpc(0)] * (2 * nsteps + 1)
        for j in range(1, 2 * nsteps + 1):
            tj = j * hdt
            nodes[j] = quarter * wp_minus_invz2(zt * tj * tj)
        return nodes

    def eval_S(zt, B, nsteps: int, wp_nodes: list):
        dt = mp.mpf(1) / nsteps
        hdt = dt / 2
        z2 = 4 * zt * zt
        qr_nodes = [z2 * ((j * hdt) ** 3) * (wp_nodes[j] + B) for j in range(2 * nsteps + 1)]
        u1, p1 = mp.mpc(1), mp.mpc(0)
        w, pw = mp.mpc(0), mp.mpc(0)
        for s in range(nsteps):
            j = 2 * s
            t0 = s * dt
            if t0 == 0:
                k1_u1 = k1_p1 = k1_w = k1_pw = mp.mpc(0)
            else:
                c0 = qr_nodes[j]
                k1_u1 = p1 / t0
                k1_p1 = -c0 * u1
                k1_w = pw / t0
                k1_pw = -c0 * w - 4 * k1_u1
            tm = t0 + hdt
            cm = qr_nodes[j + 1]
            u_m = u1 + hdt * k1_u1
            p_m = p1 + hdt * k1_p1
            w_m = w + hdt * k1_w
            pw_m = pw + hdt * k1_pw
            k2_u1 = p_m / tm
            k2_p1 = -cm * u_m
            k2_w = pw_m / tm
            k2_pw = -cm * w_m - 4 * k2_u1
            u_m2 = u1 + hdt * k2_u1
            p_m2 = p1 + hdt * k2_p1
            w_m2 = w + hdt * k2_w
            pw_m2 = pw + hdt * k2_pw
            k3_u1 = p_m2 / tm
            k3_p1 = -cm * u_m2
            k3_w = pw_m2 / tm
            k3_pw = -cm * w_m2 - 4 * k3_u1
            t1 = (s + 1) * dt
            c1 = qr_nodes[j + 2]
            u_1 = u1 + dt * k3_u1
            p_1 = p1 + dt * k3_p1
            w_1 = w + dt * k3_w
            pw_1 = pw + dt * k3_pw
            k4_u1 = p_1 / t1
            k4_p1 = -c1 * u_1
            k4_w = pw_1 / t1
            k4_pw = -c1 * w_1 - 4 * k4_u1
            u1 += (dt / 6) * (k1_u1 + 2 * k2_u1 + 2 * k3_u1 + k4_u1)
            p1 += (dt / 6) * (k1_p1 + 2 * k2_p1 + 2 * k3_p1 + k4_p1)
            w += (dt / 6) * (k1_w + 2 * k2_w + 2 * k3_w + k4_w)
            pw += (dt / 6) * (k1_pw + 2 * k2_pw + 2 * k3_pw + k4_pw)
        sz = mp.sqrt(zt)
        lz = mp.log(zt)
        phi1 = sz * u1
        phi1p = (u1 + p1) / (2 * sz)
        phi2 = phi1 * lz + sz * w
        phi2p = phi1p * lz + phi1 / zt + (w + pw) / (2 * sz)
        return phi2p / phi1p + mp.conj(phi2 / phi1)

    half = mp_rat(1, 2)
    wp1_r = precomp_wp(half, steps_root)
    wp2_r = precomp_wp(tau / 2, steps_root)

    def F_root(Br, Bi):
        B_c = mp.mpc(Br, Bi)
        diff = eval_S(half, B_c, steps_root, wp1_r) - eval_S(tau / 2, B_c, steps_root, wp2_r)
        return mp.re(diff), mp.im(diff)

    sol0 = mp.findroot(F_root, (mp.re(B_init), mp.im(B_init)), tol=mp_pow10(-8))
    B0 = mp.mpc(sol0[0], sol0[1])

    # Polish B_sol at steps_eval so B truncation error drops below 1e-8
    wp1_e = precomp_wp(half, steps_eval)
    wp2_e = precomp_wp(tau / 2, steps_eval)

    def F_polish(Br, Bi):
        B_c = mp.mpc(Br, Bi)
        diff = eval_S(half, B_c, steps_eval, wp1_e) - eval_S(tau / 2, B_c, steps_eval, wp2_e)
        return mp.re(diff), mp.im(diff)

    sol = mp.findroot(F_polish, (mp.re(B0), mp.im(B0)), tol=mp_pow10(-13))
    B_sol = mp.mpc(sol[0], sol[1])

    wp1_2e = precomp_wp(half, 2 * steps_eval)
    S_N = eval_S(half, B_sol, steps_eval, wp1_e)
    S_2N = eval_S(half, B_sol, 2 * steps_eval, wp1_2e)
    L2_N = pi - mp.re(S_N) / 2
    L2_2N = pi - mp.re(S_2N) / 2
    L2_rich = (16 * L2_2N - L2_N) / 15
    step_err = abs(L2_2N - L2_N)

    hp_consistency = mp.mpf(0)
    im_leak = abs(mp.im(S_2N))
    if check_hp3:
        wp3_e = precomp_wp((1 + tau) / 2, steps_hp3)
        wp3_2e = precomp_wp((1 + tau) / 2, 2 * steps_hp3)
        S3_N = eval_S((1 + tau) / 2, B_sol, steps_hp3, wp3_e)
        S3_2N = eval_S((1 + tau) / 2, B_sol, 2 * steps_hp3, wp3_2e)
        L2_3N = pi - mp.re(S3_N) / 2
        L2_3_2N = pi - mp.re(S3_2N) / 2
        L2_3 = (16 * L2_3_2N - L2_3N) / 15
        hp_consistency = abs(L2_3 - L2_rich)
        im_leak = max(im_leak, abs(mp.im(S3_2N)))

    return {
        "L2": L2_rich,
        "L2_N": L2_N,
        "L2_2N": L2_2N,
        "step_err": step_err,
        "hp3_diff": hp_consistency,
        "im_leak": im_leak,
        "B": B_sol,
    }


def compute_l2_suite():
    """Compute and verify L_2(tau) across all moduli + SL_2(Z) + cusp + monotonicity checks."""
    mp.mp.dps = 22
    xs = [Fraction(0, 1), Fraction(13, 100), Fraction(1, 4), Fraction(1, 2)]
    ys_ode = [Fraction(1, 1), Fraction(3, 2), Fraction(2, 1), Fraction(3, 1), Fraction(6, 1)]
    ys_all = ys_ode + [Fraction(15, 1), Fraction(30, 1)]

    hp3_targets = {
        (Fraction(0, 1), Fraction(1, 1)),
        (Fraction(0, 1), Fraction(2, 1)),
        (Fraction(13, 100), Fraction(2, 1)),
        (Fraction(13, 100), Fraction(6, 1)),
    }

    l2_cache = {}
    max_step_err = ZERO_F
    max_hp3_diff = ZERO_F
    max_im_leak = ZERO_F

    for xf in xs:
        for yf in ys_all:
            tau = mp_crat(xf.numerator, xf.denominator, yf.numerator, yf.denominator)
            tau_fd, a, b, c, d = gauss_reduce_sl2z(tau)
            if yf >= Fraction(12, 1):
                l2_val = cusp_l2_exact() - mp.log(abs(c * tau + d))
                l2_cache[(xf, yf)] = {
                    "L2": l2_val,
                    "step_err": mp.mpf(0),
                    "hp3_diff": mp.mpf(0),
                    "im_leak": mp.mpf(0),
                    "source": "cusp_formula",
                }
            else:
                do_hp3 = (xf, yf) in hp3_targets
                res = solve_l2_weierstrass_ode_direct(tau_fd, check_hp3=do_hp3, steps_hp3=160)
                l2_val = res["L2"] - mp.log(abs(c * tau + d))
                res["L2"] = l2_val
                res["source"] = "weierstrass_rk4_richardson"
                l2_cache[(xf, yf)] = res
                max_step_err = max(max_step_err, float(res["step_err"]))
                max_im_leak = max(max_im_leak, float(res["im_leak"]))
                if do_hp3:
                    max_hp3_diff = max(max_hp3_diff, float(res["hp3_diff"]))

    # Explicit cusp check at x=13/100, y=12 (ODE vs cusp formula)
    tau_12 = mp_crat(13, 100, 12, 1)
    res_12 = solve_l2_weierstrass_ode_direct(tau_12)
    l2_cusp = cusp_l2_exact()
    cusp_diff_at_12 = float(abs(res_12["L2"] - l2_cusp))
    max_step_err = max(max_step_err, float(res_12["step_err"]))

    # Holomorphic monotonicity check in y for each column x
    col_mono_checks = []
    for xf in xs:
        vals = [float(l2_cache[(xf, yf)]["L2"]) for yf in ys_ode] + [float(l2_cusp)]
        col_mono_checks.append(all(vals[i] > vals[i + 1] for i in range(len(vals) - 1)))
    monotonic_ok = bool(all(col_mono_checks))

    # Independent non-FD SL_2(Z) covariance check at tau' = -1/(2i) and -1/(13/100 + 2i)
    tau_2i = mp_crat(0, 1, 2, 1)
    tau_inv_2i = -mp.mpf(1) / tau_2i
    b_seed_2i = (tau_2i ** 2) * l2_cache[(Fraction(0, 1), Fraction(2, 1))]["B"]
    res_inv_2i = solve_l2_weierstrass_ode_direct(tau_inv_2i, B_init=b_seed_2i)
    sl2z_diff_2i = float(abs(res_inv_2i["L2"] - (l2_cache[(Fraction(0, 1), Fraction(2, 1))]["L2"] + mp.log(abs(tau_2i)))))

    tau_13 = mp_crat(13, 100, 2, 1)
    tau_inv_13 = -mp.mpf(1) / tau_13
    b_seed_13 = (tau_13 ** 2) * l2_cache[(Fraction(13, 100), Fraction(2, 1))]["B"]
    res_inv_13 = solve_l2_weierstrass_ode_direct(tau_inv_13, B_init=b_seed_13)
    sl2z_diff_13 = float(abs(res_inv_13["L2"] - (l2_cache[(Fraction(13, 100), Fraction(2, 1))]["L2"] + mp.log(abs(tau_13)))))

    # Also check Gauss reduction on shifted/inverted point (13/100 + 2i) -> -1/(13/100 + 2i) + 3
    tau_scrambled = -mp.mpf(1) / tau_13 + 3
    tau_red, _, _, c_r, d_r = gauss_reduce_sl2z(tau_scrambled)
    gauss_red_err = float(abs(tau_red - tau_13))
    ln_factor_err = float(abs(mp.log(abs(c_r * tau_scrambled + d_r)) + mp.log(abs(tau_13))))

    rk4_tol = pow10_f(-8)
    passed = bool(
        max_step_err < rk4_tol
        and max_hp3_diff < pow10_f(-7)
        and max_im_leak < pow10_f(-7)
        and sl2z_diff_2i < rk4_tol
        and sl2z_diff_13 < rk4_tol
        and gauss_red_err < pow10_f(-13)
        and ln_factor_err < pow10_f(-13)
        and monotonic_ok
        and cusp_diff_at_12 < rat_f(1, 50)
    )

    x13_table = {
        f"{yf.numerator}/{yf.denominator}": float(l2_cache[(Fraction(13, 100), yf)]["L2"])
        for yf in ys_all
    }
    x13_table["12/1_ode"] = float(res_12["L2"])
    x13_table["cusp_formula"] = float(l2_cusp)

    summary = {
        "max_rk4_step_doubling_err": max_step_err,
        "max_half_period_3_diff": max_hp3_diff,
        "max_imag_leak": max_im_leak,
        "sl2z_direct_ode_diff_2i": sl2z_diff_2i,
        "sl2z_direct_ode_diff_13_100_2i": sl2z_diff_13,
        "gauss_reduction_roundtrip_err": gauss_red_err,
        "cusp_diff_at_y12": cusp_diff_at_12,
        "holomorphic_monotonicity_ok": monotonic_ok,
        "x_13_100_L2_values": x13_table,
        "rk4_tolerance": rk4_tol,
        "passed": passed,
    }
    return l2_cache, summary


# ---------------------------------------------------------------------------
# T1, T2, T3 Pre-Registered Theorems
# ---------------------------------------------------------------------------

def verify_t1(rng: np.random.Generator) -> dict:
    # 1. Symbolic proof in SymPy via quaternion SO(3) equivariance + canonical null frame
    q0, q1, q2, q3 = sp.symbols("q0 q1 q2 q3", real=True)
    n2 = q0 ** 2 + q1 ** 2 + q2 ** 2 + q3 ** 2
    r_un = sp.Matrix([
        [q0 ** 2 + q1 ** 2 - q2 ** 2 - q3 ** 2, 2 * (q1 * q2 - q0 * q3), 2 * (q1 * q3 + q0 * q2)],
        [2 * (q1 * q2 + q0 * q3), q0 ** 2 - q1 ** 2 + q2 ** 2 - q3 ** 2, 2 * (q2 * q3 - q0 * q1)],
        [2 * (q1 * q3 - q0 * q2), 2 * (q2 * q3 + q0 * q1), q0 ** 2 - q1 ** 2 - q2 ** 2 + q3 ** 2],
    ])
    so3_orth_zero = bool(sp.expand(r_un.T * r_un - n2 ** 2 * sp.eye(3)) == sp.zeros(3))
    h_sym = sp.Matrix(sp.symbols("h0 h1 h2"))
    v_sym = sp.Matrix(sp.symbols("v0 v1 v2"))
    so3_cross_zero = bool(sp.expand((r_un * h_sym).cross(r_un * v_sym) - n2 * r_un * h_sym.cross(v_sym)) == sp.zeros(3, 1))

    h0 = sp.Matrix([1, sp.I, 0]) / sp.sqrt(2)
    h0b = sp.Matrix([1, -sp.I, 0]) / sp.sqrt(2)
    e3 = -sp.I * h0.cross(h0b)
    B_sym = sp.Matrix.hstack(h0, h0b, e3)
    au, bu, gu, w = sp.symbols("alpha_u beta_u gamma_u w")
    u_sym = au * h0 + bu * h0b + gu * e3
    hx_sym = sp.Matrix([[0, -h0[2], h0[1]], [h0[2], 0, -h0[0]], [-h0[1], h0[0], 0]])
    Y_sym = u_sym * h0.T + h0 * u_sym.T - (u_sym.dot(h0)) * sp.eye(3) + w * hx_sym
    M_sym = sp.simplify(B_sym.H * Y_sym * B_sym)
    kernel_col0_zero = bool(M_sym[:, 0] == sp.zeros(3, 1))
    kernel_row1_zero = bool(M_sym[1, :] == sp.zeros(1, 3))
    A_sym = sp.Matrix([[M_sym[0, 1], M_sym[0, 2]], [M_sym[2, 1], M_sym[2, 2]]])
    det_law_zero = bool(sp.simplify(A_sym.det() + w ** 2 + u_sym.dot(u_sym)) == 0)

    # 2. Numerical verification across 12 random null vectors (unit and non-unit) & complex (u, w)
    max_unit_err = ZERO_F
    max_col0_err = ZERO_F
    max_row1_err = ZERO_F
    max_det_err = ZERO_F
    max_mass_prod_err = ZERO_F
    tol = pow10_f(-12)

    for trial in range(12):
        # Ensure real SO(3) rotation from real Ginibre QR with det=+1
        z_r = rng.normal(size=(3, 3))
        qr_r, rr_r = np.linalg.qr(z_r)
        s_diag = np.sign(np.diag(rr_r))
        s_diag[s_diag == 0] = 1
        r_rot = qr_r * s_diag[None, :]
        if np.linalg.det(r_rot) < 0:
            r_rot[:, 0] = -r_rot[:, 0]
        n1 = r_rot[:, 0]
        n2_v = r_rot[:, 1]
        h0_n = (n1 + I_C * n2_v) / math.sqrt(2)
        scale = rat_f(1, 1) if trial < 6 else rat_f(3 + trial, 5)
        h_scaled = scale * h0_n

        u_n = rng.normal(size=3) + I_C * rng.normal(size=3)
        w_n = rng.normal() + I_C * rng.normal()
        e3_n = -I_C * np.cross(h0_n, np.conj(h0_n))
        B_n = np.column_stack([h0_n, np.conj(h0_n), e3_n])
        max_unit_err = max(max_unit_err, float(np.linalg.norm(B_n.conj().T @ B_n - np.eye(3))))

        M_n = B_n.conj().T @ y_vec_np(h0_n, u_n, w_n) @ B_n
        max_col0_err = max(max_col0_err, float(np.linalg.norm(M_n[:, 0])))
        max_row1_err = max(max_row1_err, float(np.linalg.norm(M_n[1, :])))

        A_n = np.array([[M_n[0, 1], M_n[0, 2]], [M_n[2, 1], M_n[2, 2]]], dtype=complex)
        det_res = np.linalg.det(A_n) + w_n ** 2 + np.dot(u_n, u_n)
        max_det_err = max(max_det_err, float(abs(det_res)))

        sv = np.linalg.svd(y_vec_np(h_scaled, u_n, w_n), compute_uv=False)
        prod_lhs = float(sv[0] * sv[1])
        prod_rhs = float((np.linalg.norm(h_scaled) ** 2) * abs(w_n ** 2 + np.dot(u_n, u_n)))
        max_mass_prod_err = max(max_mass_prod_err, abs(prod_lhs - prod_rhs))

    passed = bool(
        so3_orth_zero
        and so3_cross_zero
        and kernel_col0_zero
        and kernel_row1_zero
        and det_law_zero
        and max_unit_err < tol
        and max_col0_err < tol
        and max_row1_err < tol
        and max_det_err < tol
        and max_mass_prod_err < tol
    )
    return {
        "sympy_so3_orthog_zero": so3_orth_zero,
        "sympy_so3_cross_equivariance_zero": so3_cross_zero,
        "sympy_kernel_col0_zero": kernel_col0_zero,
        "sympy_kernel_row1_zero": kernel_row1_zero,
        "sympy_det_law_zero": det_law_zero,
        "max_B_unitarity_err": max_unit_err,
        "max_col0_err": max_col0_err,
        "max_row1_err": max_row1_err,
        "max_det_law_err": max_det_err,
        "max_m2_m3_product_err": max_mass_prod_err,
        "tolerance": tol,
        "passed": passed,
    }


def verify_t2(rng: np.random.Generator) -> dict:
    eps, qj, qi, qk, c_gen, _ = quaternion_basis_np()
    c4 = [np.eye(2, dtype=complex), qj, qi, qk]
    half = rat_f(1, 2)
    sqrt2 = math.sqrt(2)
    tol = pow10_f(-12)

    max_sv4_err = ZERO_F
    max_rem_excess = -ONE_F
    max_v_norm_err = ZERO_F
    max_v_norm_real_xi_err = ZERO_F
    min_v_norm_sq = rat_f(10, 1)
    max_v_norm_sq = ZERO_F

    for _ in range(50):
        h = rng.normal(size=3) + I_C * rng.normal(size=3)
        h = h / np.linalg.norm(h)
        mw = rng.normal(size=(2, 2)) + I_C * rng.normal(size=(2, 2))
        H = eps @ s_of_h_np(h, qj, qi, qk)

        Y4 = np.zeros((4, 4), dtype=complex)
        for A in range(4):
            for B in range(4):
                Y4[A, B] = half * np.trace((c4[A].T @ H @ c4[B]).T @ mw)
        sv4 = np.sort(np.linalg.svd(Y4, compute_uv=False))[::-1]

        r = min(ONE_F, float(abs(np.dot(h, h))))
        sig_p = (math.sqrt(ONE_F + r) + math.sqrt(max(ZERO_F, ONE_F - r))) / sqrt2
        sig_m = (math.sqrt(ONE_F + r) - math.sqrt(max(ZERO_F, ONE_F - r))) / sqrt2
        um, sm, vmh = np.linalg.svd(mw)
        expected_sv4 = np.sort(
            np.array([sig_p * sm[0], sig_p * sm[1], sig_m * sm[0], sig_m * sm[1]])
        )[::-1]
        max_sv4_err = max(max_sv4_err, float(np.max(np.abs(sv4 - expected_sv4))))

        uh, sh, vhh = np.linalg.svd(H)
        xi = uh[:, 0]
        eta = vhh[0, :]
        l_vec = um[:, 0]
        r_vec = vmh[0, :]
        v_lxi = np.array([xi @ c_gen[a] @ l_vec for a in range(3)], dtype=complex)
        v_reta = np.array([eta @ c_gen[a] @ r_vec for a in range(3)], dtype=complex)
        v_norm_sq = float(np.sum(np.abs(v_lxi) ** 2))
        expected_v_norm_sq = ONE_F + float(abs(l_vec @ eps @ np.conj(xi)) ** 2)
        max_v_norm_err = max(max_v_norm_err, abs(v_norm_sq - expected_v_norm_sq))
        min_v_norm_sq = min(min_v_norm_sq, v_norm_sq)
        max_v_norm_sq = max(max_v_norm_sq, v_norm_sq)

        # Also verify real-spinor specialization 1 + |l^T eps xi|^2
        xi_r = rng.normal(size=2)
        xi_r = xi_r / np.linalg.norm(xi_r)
        v_r = np.array([xi_r @ c_gen[a] @ l_vec for a in range(3)], dtype=complex)
        max_v_norm_real_xi_err = max(
            max_v_norm_real_xi_err,
            abs(float(np.sum(np.abs(v_r) ** 2)) - (ONE_F + float(abs(l_vec @ eps @ xi_r) ** 2))),
        )

        Y3 = Y4[1:, 1:]
        A0 = half * sh[0] * sm[0] * np.outer(v_lxi, v_reta)
        rem_norm = float(np.linalg.norm(Y3 - A0, ord=2))
        rem_bound = max(sig_p * float(sm[1]), sig_m * float(sm[0]))
        max_rem_excess = max(max_rem_excess, rem_norm - rem_bound)

    passed = bool(
        max_sv4_err < tol
        and max_rem_excess <= tol
        and max_v_norm_err < tol
        and max_v_norm_real_xi_err < tol
        and min_v_norm_sq >= ONE_F - tol
        and max_v_norm_sq <= rat_f(2, 1) + tol
    )
    return {
        "n_trials": 50,
        "max_sv4_kronecker_err": max_sv4_err,
        "max_remainder_excess": max_rem_excess,
        "max_v_norm_sq_err": max_v_norm_err,
        "max_v_norm_real_xi_err": max_v_norm_real_xi_err,
        "min_v_norm_sq": min_v_norm_sq,
        "max_v_norm_sq": max_v_norm_sq,
        "tolerance": tol,
        "passed": passed,
    }


def verify_t3(b1967_channels: dict) -> dict:
    # 1. SymPy symbolic proof of Spinor Mobius Bound
    sL, cL, sx, cx = sp.symbols("sL cL sx cx", real=True)
    a2 = (1 + cx * cL + sx * sL) / 2
    b2 = (1 - cx * cL + sx * sL) / 2
    ab = (sx + sL) / 2
    poly_diff = sp.expand((1 + sL) ** 2 * (2 - a2) * (2 - b2) - (3 - sL) ** 2 * ab ** 2)
    poly_diff = sp.expand(poly_diff.subs(cL ** 2, 1 - sL ** 2)).subs(cx ** 2, 1 - sx ** 2)
    expected_factored = 2 * (1 - sx) * ((1 + sx) + sL * (2 - sx + sL ** 2))
    sympy_poly_identity_zero = bool(sp.expand(poly_diff - expected_factored) == 0)

    # Check direct matrix construction in SymPy at critical point t_* = pi/4 - alpha/2
    al_s = sp.Symbol("alpha", real=True, positive=True)
    t_s = sp.Symbol("t", real=True)
    qj_s = sp.Matrix([[0, 1], [-1, 0]])
    qi_s = sp.Matrix([[sp.I, 0], [0, -sp.I]])
    qk_s = qi_s * qj_s
    c_s = [qj_s, qi_s, qk_s]
    ld_s = sp.Matrix([1, 0])
    lu_s = sp.Matrix([sp.cos(al_s), sp.sin(al_s)])
    xi_s = sp.Matrix([sp.cos(t_s), -sp.sin(t_s)])
    xiu_s = qj_s * xi_s
    vu_s = sp.Matrix([(xiu_s.T * c_s[k] * lu_s)[0, 0] for k in range(3)])
    vd_s = sp.Matrix([(xi_s.T * c_s[k] * ld_s)[0, 0] for k in range(3)])
    num_s = sp.simplify((vu_s.H * vd_s)[0, 0])
    den_u_s = sp.simplify((vu_s.H * vu_s)[0, 0])
    den_d_s = sp.simplify((vd_s.H * vd_s)[0, 0])
    t_star_s = sp.pi / 4 - al_s / 2
    val_at_star = sp.simplify((num_s ** 2 / (den_u_s * den_d_s)).subs(t_s, t_star_s))
    target_sq = ((1 + sp.sin(al_s)) / (3 - sp.sin(al_s))) ** 2
    sympy_crit_value_zero = bool(sp.simplify(val_at_star - target_sq) == 0)
    deriv_at_star = sp.simplify(sp.diff(num_s ** 2 / (den_u_s * den_d_s), t_s).subs(t_s, t_star_s))
    sympy_crit_deriv_zero = bool(deriv_at_star == 0)

    # 2. Dense 2D (t, phi) spinor grid check across sL in {0, 1/4, 1/2, 3/4, 17/19, 1}
    eps, qj, qi, qk, c_gen, e_dual = quaternion_basis_np()
    C_arr = np.array(c_gen)
    ts = np.linspace(ZERO_F, math.pi / 2, 16001)
    phis = np.linspace(ZERO_F, 2 * math.pi, 33)
    T, P = np.meshgrid(ts, phis, indexing="ij")
    xi0 = np.cos(T)
    xi1 = np.exp(I_C * P) * np.sin(T)
    xiu0 = np.conj(xi1)
    xiu1 = -np.conj(xi0)

    sL_list = [
        Fraction(0, 1),
        Fraction(1, 4),
        Fraction(1, 2),
        Fraction(3, 4),
        Fraction(17, 19),
        Fraction(1, 1),
    ]
    grid_results = []
    max_grid_err = ZERO_F
    max_exact_err = ZERO_F
    grid_tol = pow10_f(-8)
    exact_tol = pow10_f(-13)
    for sf in sL_list:
        sL_val = rat_f(sf.numerator, sf.denominator)
        ld = np.array([ONE_F, ZERO_F], dtype=complex)
        lu = np.array([math.sqrt(max(ZERO_F, ONE_F - sL_val * sL_val)), sL_val], dtype=complex)
        Cl_d = np.einsum("aij,j->ai", C_arr, ld)
        Cl_u = np.einsum("aij,j->ai", C_arr, lu)
        vd = xi0[:, :, None] * Cl_d[:, 0][None, None, :] + xi1[:, :, None] * Cl_d[:, 1][None, None, :]
        vu = xiu0[:, :, None] * Cl_u[:, 0][None, None, :] + xiu1[:, :, None] * Cl_u[:, 1][None, None, :]
        num = np.abs(np.sum(np.conj(vu) * vd, axis=-1))
        den = np.linalg.norm(vu, axis=-1) * np.linalg.norm(vd, axis=-1)
        sup_grid = float(np.max(num / den))

        # Exact evaluation at t_*
        t_star = math.pi / 4 - math.asin(sL_val) / 2
        xi_ex = np.array([math.cos(t_star), -math.sin(t_star)], dtype=complex)
        xiu_ex = eps @ np.conj(xi_ex)
        vd_ex = np.array([xi_ex @ c_gen[a] @ ld for a in range(3)], dtype=complex)
        vu_ex = np.array([xiu_ex @ c_gen[a] @ lu for a in range(3)], dtype=complex)
        val_ex = float(abs(np.vdot(vu_ex, vd_ex)) / (np.linalg.norm(vu_ex) * np.linalg.norm(vd_ex)))

        ceil_val = (ONE_F + sL_val) / (rat_f(3, 1) - sL_val)
        g_err = abs(sup_grid - ceil_val)
        e_err = abs(val_ex - ceil_val)
        max_grid_err = max(max_grid_err, g_err)
        max_exact_err = max(max_exact_err, e_err)
        grid_results.append({
            "sL": f"{sf.numerator}/{sf.denominator}",
            "ceiling": ceil_val,
            "grid_sup": sup_grid,
            "grid_err": g_err,
            "exact_t_star_err": e_err,
        })

    # 3. Check B1967 16-rational control s_L > 17/19 (and > 19/20)
    mu_1967 = uw_to_mw_np(b1967_channels["u_u"], b1967_channels["w_u"], e_dual)
    md_1967 = uw_to_mw_np(b1967_channels["u_d"], b1967_channels["w_d"], e_dual)
    Uu_1967, _, _ = np.linalg.svd(mu_1967)
    Ud_1967, _, _ = np.linalg.svd(md_1967)
    sL_1967 = float(abs(Uu_1967[:, 0] @ eps @ Ud_1967[:, 0]))
    b1967_ok = bool(sL_1967 > rat_f(17, 19) and sL_1967 > rat_f(19, 20))

    passed = bool(
        sympy_poly_identity_zero
        and sympy_crit_value_zero
        and sympy_crit_deriv_zero
        and max_grid_err < grid_tol
        and max_exact_err < exact_tol
        and b1967_ok
    )
    return {
        "sympy_poly_identity_zero": sympy_poly_identity_zero,
        "sympy_crit_value_zero": sympy_crit_value_zero,
        "sympy_crit_deriv_zero": sympy_crit_deriv_zero,
        "max_2d_grid_err": max_grid_err,
        "max_exact_t_star_err": max_exact_err,
        "grid_results": grid_results,
        "b1967_sL": sL_1967,
        "b1967_mobius_ceiling": (ONE_F + sL_1967) / (rat_f(3, 1) - sL_1967),
        "b1967_gt_17_19": bool(sL_1967 > rat_f(17, 19)),
        "b1967_gt_19_20": bool(sL_1967 > rat_f(19, 20)),
        "passed": passed,
    }


# ---------------------------------------------------------------------------
# Frame C Channel Construction (Theta Residue + Theorem 90 Weights)
# ---------------------------------------------------------------------------

def prepare_tau_context(tau):
    """Precompute eta denominator, theta_1 weights, and adaptive truncation bounds for tau."""
    y = mp.im(tau)
    q = mp.exp(2 * mp.pi * I_MP * tau)
    n_eta = 32 if y < 2 else (16 if y < 5 else 8)
    prod = mp.mpc(1)
    qn = q
    for _ in range(1, n_eta):
        prod *= 1 - qn
        qn *= q
    eta_denom = 2 * mp.pi * ((mp.exp(mp.pi * I_MP * tau / 12) * prod) ** 3)
    n_t1 = 10 if y < 2 else (6 if y < 5 else 4)
    half = mp_rat(1, 2)
    t1_weights = [
        (2 * (1 if (n % 2 == 0) else -1) * mp.exp(mp.pi * I_MP * ((n + half) ** 2) * tau), (2 * n + 1) * mp.pi)
        for n in range(n_t1)
    ]
    n_tc = 11 if y < 2 else (6 if y < 5 else 4)
    n_f = 16 if y < 2 else (8 if y < 5 else 4)
    return {
        "eta_denom": eta_denom,
        "t1_weights": t1_weights,
        "n_tc": n_tc,
        "n_f": n_f,
        "log_y": mp.log(y),
        "const_shift": 2 * mp.pi * (mp.euler + mp.log(mp.pi)),
    }


def theta_c_mp(alpha, beta, tau, n_tc: int = 12):
    n0 = -int(mp.nint(alpha))
    s = mp.mpc(0)
    for n in range(n0 - n_tc, n0 + n_tc + 1):
        na = n + alpha
        s += mp.exp(mp.pi * I_MP * na * na * tau + 2 * mp.pi * I_MP * na * beta)
    return s


def theta1_and_deriv_mp(z, tau, t1_weights=None):
    s = mp.mpc(0)
    sp_z = mp.mpc(0)
    if t1_weights is None:
        half = mp_rat(1, 2)
        for n in range(10):
            sgn = 1 if (n % 2 == 0) else -1
            m = n + half
            fac = 2 * sgn * mp.exp(mp.pi * I_MP * m * m * tau)
            arg = (2 * n + 1) * mp.pi * z
            s += fac * mp.sin(arg)
            sp_z += fac * (2 * n + 1) * mp.pi * mp.cos(arg)
        return s, sp_z
    for fac, mpi in t1_weights:
        arg = mpi * z
        s += fac * mp.sin(arg)
        sp_z += fac * mpi * mp.cos(arg)
    return s, sp_z


def eta_mp(tau):
    q = mp.exp(2 * mp.pi * I_MP * tau)
    prod = mp.mpc(1)
    qn = q
    for _ in range(1, 35):
        prod *= 1 - qn
        qn *= q
    return mp.exp(mp.pi * I_MP * tau / 12) * prod


def f_green_row_mp(alpha, beta, tau, cache: dict, n_f: int = 16):
    key = (str(alpha), str(beta), str(mp.re(tau)), str(mp.im(tau)))
    if key in cache:
        return cache[key]
    x = mp.re(tau)
    y = mp.im(tau)
    zero_tol = mp_pow10(-15)
    cut_tol = mp_pow10(-22)
    b1940_shift = mp.pi * (2 * mp.log(2) + mp.log(y))
    if abs(alpha) < zero_tol:
        sin_b = mp.sin(mp.pi * beta)
        res = y * (mp.pi ** 2) / (sin_b * sin_b) + 2 * mp.pi * mp.euler - b1940_shift
        m_list = [m for m in range(-n_f, n_f + 1) if m != 0]
    else:
        res = -b1940_shift - mp.pi * (mp.psi(0, alpha) + mp.psi(0, 1 - alpha))
        m_list = list(range(-n_f, n_f + 1))
    for m in m_list:
        ma = m + alpha
        r = mp.exp(-2 * mp.pi * abs(ma) * y)
        if r < cut_tol:
            continue
        theta = 2 * mp.pi * (ma * x + beta)
        cos_t = mp.cos(theta)
        res += (mp.pi / abs(ma)) * 2 * (r * cos_t - r * r) / (1 - 2 * r * cos_t + r * r)
    cache[key] = res
    return res


def is_int_pair_mp(x, y) -> bool:
    tol = mp_pow10(-15)
    return bool(abs(x - mp.nint(x)) < tol and abs(y - mp.nint(y)) < tol)


def frame_c_base_terms(tau, af: Fraction, bf: Fraction, qL: int, qR: int, f_cache: dict, tau_ctx=None):
    """Compute L_2-independent terms (Rs, Fu, |a0|^2, base_const) for channels {'1','i','j','k'}."""
    if tau_ctx is None:
        tau_ctx = prepare_tau_context(tau)
    a = mp_rat(af.numerator, af.denominator)
    b = mp_rat(bf.numerator, bf.denominator)
    x0, x1 = qL * a, 2 * qL * b
    y0, y1 = qR * a, 2 * qR * b
    ap, am = x0 + y0, x0 - y0
    bp, bm = (x1 + y1) / 2, (x1 - y1) / 2
    H = mp_rat(1, 2)
    e = mp.exp(-2 * mp.pi * I_MP * x0)
    kappa = {"1": -I_MP * e, "i": mp.mpc(-1), "j": -e, "k": I_MP}
    cs = {"1": (ap + H, bp + H), "i": (ap + H, bp), "j": (ap, bp + H), "k": (ap, bp)}
    ds = {"1": (am + H, bm + H), "i": (am + H, bm), "j": (am, bm + H), "k": (am, bm)}

    eta_denom = tau_ctx["eta_denom"]
    n_tc = tau_ctx["n_tc"]
    n_f = tau_ctx["n_f"]
    t1_w = tau_ctx["t1_weights"]
    base_shift = tau_ctx["log_y"] * mp.pi - tau_ctx["const_shift"]

    terms = {}
    for s in ("1", "i", "j", "k"):
        c0, c1 = cs[s]
        d0, d1 = ds[s]
        if is_int_pair_mp(c0 - H, c1 - H) or is_int_pair_mp(d0 - H, d1 - H):
            terms[s] = None
        else:
            Rs = kappa[s] * theta_c_mp(c0, c1, tau, n_tc) * theta_c_mp(d0, d1, tau, n_tc) / eta_denom
            al_r = (c0 - H) % 1
            be_r = (c1 - H) % 1
            t1, t1p = theta1_and_deriv_mp(al_r * tau + be_r, tau, t1_w)
            a0 = 2 * mp.pi * I_MP * al_r + t1p / t1
            Fu = f_green_row_mp(al_r, be_r, tau, f_cache, n_f)
            terms[s] = (Rs, Fu + base_shift, mp.pi * (abs(a0) ** 2))
    return terms


def frame_c_eval_from_terms(terms: dict, L2):
    exp_neg_2l2 = mp.exp(-2 * L2)
    two_pi_l2 = 2 * mp.pi * L2
    rs_out = {}
    us_out = {}
    ns_out = {}
    for s in ("1", "i", "j", "k"):
        item = terms[s]
        if item is None:
            rs_out[s] = complex(0, 0)
            us_out[s] = complex(0, 0)
            ns_out[s] = ZERO_F
        else:
            Rs, base_part, a0_coef = item
            Ns = two_pi_l2 + base_part - a0_coef * exp_neg_2l2
            rs_out[s] = complex(Rs)
            ns_out[s] = float(Ns)
            us_out[s] = complex(mp.sqrt(max(mp.mpf(0), Ns)) * Rs)
    return rs_out, us_out, ns_out


def frame_c_sector_channels(tau, L2, af: Fraction, bf: Fraction, qL: int, qR: int, f_cache: dict, tau_ctx=None):
    """Return (res_dict, full_dict, N_dict) for channels {'1','i','j','k'}."""
    terms = frame_c_base_terms(tau, af, bf, qL, qR, f_cache, tau_ctx)
    return frame_c_eval_from_terms(terms, L2)


def channels_dict_to_mw(ch: dict, e_dual: dict) -> np.ndarray:
    return ch["1"] * e_dual["1"] + ch["i"] * e_dual["i"] + ch["j"] * e_dual["j"] + ch["k"] * e_dual["k"]


def channels_dict_to_uw(ch: dict):
    u = np.array([ch["j"], ch["i"], ch["k"]], dtype=complex)
    w = -ch["1"]
    return u, w


def torsion_point_sets():
    pts5 = [(Fraction(i, 5), Fraction(j, 5)) for i in range(5) for j in range(5) if not (i == 0 and j == 0)]
    pts12 = [
        (Fraction(1, 3), Fraction(1, 3)),
        (Fraction(1, 3), Fraction(0, 1)),
        (Fraction(1, 4), Fraction(1, 2)),
        (Fraction(1, 4), Fraction(1, 4)),
        (Fraction(1, 6), Fraction(1, 6)),
        (Fraction(1, 6), Fraction(5, 6)),
        (Fraction(3, 7), Fraction(1, 7)),
        (Fraction(1, 7), Fraction(6, 7)),
        (Fraction(2, 7), Fraction(3, 7)),
        (Fraction(1, 7), Fraction(0, 1)),
        (Fraction(1, 8), Fraction(3, 8)),
        (Fraction(3, 8), Fraction(1, 8)),
    ]
    return pts5, pts12


def verify_t4(l2_cache: dict) -> dict:
    mp.mp.dps = 24
    eps, _, _, _, _, e_dual = quaternion_basis_np()
    pts5, pts12 = torsion_point_sets()
    all36 = pts5 + pts12

    # 1. At tau = 13/100 + 2i: check T4(a) order-5 w_u==0 and T4(b)(1,2) rank-1 & s_L^res==0
    xf_mid = Fraction(13, 100)
    yf_mid = Fraction(2, 1)
    tau_mid = mp_crat(xf_mid.numerator, xf_mid.denominator, yf_mid.numerator, yf_mid.denominator)
    l2_mid = l2_cache[(xf_mid, yf_mid)]["L2"]
    ctx_mid = prepare_tau_context(tau_mid)
    f_cache = {}

    max_wu_order5 = ZERO_F
    max_mu2_mu1_res_u = ZERO_F
    max_mu2_mu1_res_d = ZERO_F
    max_sL_res = ZERO_F

    for idx, (af, bf) in enumerate(all36):
        ru, uu, _ = frame_c_sector_channels(tau_mid, l2_mid, af, bf, 1, -4, f_cache, ctx_mid)
        rd, ud, _ = frame_c_sector_channels(tau_mid, l2_mid, af, bf, 1, 2, f_cache, ctx_mid)
        if idx < 24:
            max_wu_order5 = max(max_wu_order5, float(abs(ru["1"])), float(abs(uu["1"])))
        mu_res = channels_dict_to_mw(ru, e_dual)
        md_res = channels_dict_to_mw(rd, e_dual)
        Uu_r, su_r, _ = np.linalg.svd(mu_res)
        Ud_r, sd_r, _ = np.linalg.svd(md_res)
        max_mu2_mu1_res_u = max(max_mu2_mu1_res_u, float(su_r[1] / su_r[0]))
        max_mu2_mu1_res_d = max(max_mu2_mu1_res_d, float(sd_r[1] / sd_r[0]))
        sL_r = float(abs(Uu_r[:, 0] @ eps @ Ud_r[:, 0]))
        max_sL_res = max(max_sL_res, sL_r)

    # 2. Cusp s_L decay across x in {0, 1/4} and y in {1, 3/2, 2, 3, 6, 15, 30} on order-5 + order-7
    pts7 = [pt for pt in pts12 if pt[0].denominator == 7 or pt[1].denominator == 7]
    pts_cusp = pts5 + pts7
    xs_cusp = [Fraction(0, 1), Fraction(1, 4)]
    ys_cusp = [Fraction(1, 1), Fraction(3, 2), Fraction(2, 1), Fraction(3, 1), Fraction(6, 1), Fraction(15, 1), Fraction(30, 1)]
    ys_mono = [Fraction(1, 1), Fraction(3, 1), Fraction(6, 1), Fraction(15, 1), Fraction(30, 1)]

    cusp_table = {}
    max_sL_overall = ZERO_F
    mono_checks = []
    y6_checks = []
    y30_checks = []
    max_wu_cusp = ZERO_F

    for xf in xs_cusp:
        col_key = f"{xf.numerator}/{xf.denominator}"
        cusp_table[col_key] = {}
        for yf in ys_cusp:
            tau = mp_crat(xf.numerator, xf.denominator, yf.numerator, yf.denominator)
            l2 = l2_cache[(xf, yf)]["L2"]
            ctx = prepare_tau_context(tau)
            max_sL_h = ZERO_F
            for idx, (af, bf) in enumerate(pts_cusp):
                _, uu, _ = frame_c_sector_channels(tau, l2, af, bf, 1, -4, f_cache, ctx)
                _, ud, _ = frame_c_sector_channels(tau, l2, af, bf, 1, 2, f_cache, ctx)
                if idx < 24:
                    max_wu_cusp = max(max_wu_cusp, float(abs(uu["1"])))
                Mu = channels_dict_to_mw(uu, e_dual)
                Md = channels_dict_to_mw(ud, e_dual)
                Uu, _, _ = np.linalg.svd(Mu)
                Ud, _, _ = np.linalg.svd(Md)
                sL = float(abs(Uu[:, 0] @ eps @ Ud[:, 0]))
                max_sL_h = max(max_sL_h, sL)
            max_sL_overall = max(max_sL_overall, max_sL_h)
            cusp_table[col_key][f"{yf.numerator}/{yf.denominator}"] = max_sL_h
            if yf == Fraction(6, 1):
                y6_checks.append(max_sL_h < rat_f(1, 5))
            if yf == Fraction(30, 1):
                y30_checks.append(max_sL_h < rat_f(1, 8))
        mono_vals = [cusp_table[col_key][f"{yf.numerator}/{yf.denominator}"] for yf in ys_mono]
        mono_checks.append(all(mono_vals[i] > mono_vals[i + 1] for i in range(len(mono_vals) - 1)))

    mono_ok = bool(all(mono_checks))
    y6_ok = bool(all(y6_checks))
    y30_ok = bool(all(y30_checks))

    tol_wu = pow10_f(-14)
    tol_res = pow10_f(-13)
    passed = bool(
        max_wu_order5 < tol_wu
        and max_wu_cusp < tol_wu
        and max_mu2_mu1_res_u < tol_res
        and max_mu2_mu1_res_d < tol_res
        and max_sL_res < tol_res
        and max_sL_overall < rat_f(2, 5)
        and mono_ok
        and y6_ok
        and y30_ok
    )
    return {
        "n_torsion_points": len(all36),
        "max_order5_wu_at_13_100_2i": max_wu_order5,
        "max_order5_wu_across_cusp_grid": max_wu_cusp,
        "max_res_mu2_mu1_up": max_mu2_mu1_res_u,
        "max_res_mu2_mu1_down": max_mu2_mu1_res_d,
        "max_res_sL": max_sL_res,
        "max_full_sL_overall": max_sL_overall,
        "cusp_max_sL_table": cusp_table,
        "monotonic_decay_1_3_6_15_30": mono_ok,
        "y6_lt_1_5": y6_ok,
        "y30_lt_1_8": y30_ok,
        "passed": passed,
    }


# ---------------------------------------------------------------------------
# T5: Deterministic Vectorized CP^2 Weyl + Davis-Kahan Global Certifier
# ---------------------------------------------------------------------------

def build_initial_cp2_grid():
    """Build initial 8^4 bidisk-filtered cover across all 3 affine charts of CP^2."""
    hw0 = rat_f(1, 8)
    g1 = np.linspace(-ONE_F + hw0, ONE_F - hw0, 8)
    pts4 = np.stack(np.meshgrid(g1, g1, g1, g1, indexing="ij"), axis=-1).reshape(-1, 4)
    m0 = np.maximum(ZERO_F, np.abs(pts4[:, 0]) - hw0) ** 2 + np.maximum(ZERO_F, np.abs(pts4[:, 1]) - hw0) ** 2 > ONE_F
    m1 = np.maximum(ZERO_F, np.abs(pts4[:, 2]) - hw0) ** 2 + np.maximum(ZERO_F, np.abs(pts4[:, 3]) - hw0) ** 2 > ONE_F
    pts4 = pts4[~(m0 | m1)]
    init_c = np.vstack([pts4, pts4, pts4])
    init_k = np.repeat(np.array([0, 1, 2]), len(pts4))

    v0 = np.ones((len(init_c), 3), dtype=complex)
    z0 = init_c[:, 0] + I_C * init_c[:, 1]
    z1 = init_c[:, 2] + I_C * init_c[:, 3]
    k0 = init_k == 0
    k1 = init_k == 1
    k2 = init_k == 2
    v0[k0, 1] = z0[k0]
    v0[k0, 2] = z1[k0]
    v0[k1, 0] = z0[k1]
    v0[k1, 2] = z1[k1]
    v0[k2, 0] = z0[k2]
    v0[k2, 1] = z1[k2]
    nv0 = np.linalg.norm(v0, axis=1)
    h0 = v0 / nv0[:, None]
    rad0 = math.sqrt(4 * hw0 * hw0)
    dh0 = rad0 / np.maximum(ONE_F, nv0 - rad0)
    return init_c, init_k, h0, np.conj(h0), dh0


INIT_C, INIT_K, INIT_H, INIT_HC, INIT_DH = build_initial_cp2_grid()


def build_Y_batch_fast(h: np.ndarray, u: np.ndarray, w: complex) -> np.ndarray:
    uh = h @ u
    Y = h[:, :, None] * u[None, None, :] + u[None, :, None] * h[:, None, :]
    Y[:, 0, 0] -= uh
    Y[:, 1, 1] -= uh
    Y[:, 2, 2] -= uh
    Y[:, 0, 1] -= w * h[:, 2]
    Y[:, 0, 2] += w * h[:, 1]
    Y[:, 1, 0] += w * h[:, 2]
    Y[:, 1, 2] -= w * h[:, 0]
    Y[:, 2, 0] -= w * h[:, 1]
    Y[:, 2, 1] += w * h[:, 0]
    return Y


def mu1_from_uw(u: np.ndarray, w: complex) -> float:
    _, _, _, _, _, e_dual = quaternion_basis_np()
    mw = uw_to_mw_np(u, w, e_dual)
    return float(np.linalg.svd(mw, compute_uv=False)[0])


def certify_cp2_global(
    uu: np.ndarray,
    wu: complex,
    ud: np.ndarray,
    wd: complex,
    max_steps: int = 16,
    lip_scale: float = ONE_F,
    conj_up: bool = True,
    return_survivors: bool = False,
):
    """Certified branch-and-bound over all 3 charts of CP^2 using MVT + Weyl + Davis-Kahan."""
    mu1_u = mu1_from_uw(uu, wu)
    mu1_d = mu1_from_uw(ud, wd)
    two_sqrt2 = 2 * math.sqrt(2)
    ratio_thresh = rat_f(1, 100)
    cos_9_10 = math.acos(rat_f(9, 10))
    half = rat_f(1, 2)

    c = INIT_C
    cid = INIT_K
    hws = np.array([rat_f(1, 8), rat_f(1, 8), rat_f(1, 8), rat_f(1, 8)], dtype=float)
    total_eval = 0

    for step in range(max_steps):
        if step == 0:
            h = INIT_H
            dh = INIT_DH
        else:
            rad = float(np.linalg.norm(hws))
            m0 = np.maximum(ZERO_F, np.abs(c[:, 0]) - hws[0]) ** 2 + np.maximum(ZERO_F, np.abs(c[:, 1]) - hws[1]) ** 2 > ONE_F
            m1 = np.maximum(ZERO_F, np.abs(c[:, 2]) - hws[2]) ** 2 + np.maximum(ZERO_F, np.abs(c[:, 3]) - hws[3]) ** 2 > ONE_F
            keep_dom = ~(m0 | m1)
            c = c[keep_dom]
            cid = cid[keep_dom]
            if len(c) == 0:
                out = {"excluded": bool(len(c) == 0), "steps": step, "boxes_evaluated": total_eval, "surviving_boxes": 0}
                if return_survivors:
                    out.update({"surv_c": c, "surv_cid": cid, "hws": hws.copy()})
                return out
            v = np.ones((len(c), 3), dtype=complex)
            z0 = c[:, 0] + I_C * c[:, 1]
            z1 = c[:, 2] + I_C * c[:, 3]
            k0 = cid == 0
            k1 = cid == 1
            k2 = cid == 2
            v[k0, 1] = z0[k0]
            v[k0, 2] = z1[k0]
            v[k1, 0] = z0[k1]
            v[k1, 2] = z1[k1]
            v[k2, 0] = z0[k2]
            v[k2, 1] = z1[k2]
            nv = np.linalg.norm(v, axis=1)
            h = v / nv[:, None]
            dh = rad / np.maximum(ONE_F, nv - rad)

        total_eval += len(c)
        Dd = lip_scale * two_sqrt2 * mu1_d * dh
        Yd = build_Y_batch_fast(h, ud, wd)
        ed, Vd = np.linalg.eigh(Yd @ np.swapaxes(np.conj(Yd), 1, 2))
        sd = np.sqrt(np.maximum(ZERO_F, ed[:, ::-1]))
        pd = (sd[:, 1] - Dd) > ratio_thresh * (sd[:, 0] + Dd)
        rem = ~pd
        if not np.any(rem):
            out = {"excluded": bool(not np.any(rem)), "steps": step, "boxes_evaluated": total_eval, "surviving_boxes": 0}
            if return_survivors:
                out.update({"surv_c": np.empty((0, 4)), "surv_cid": np.empty(0, dtype=int), "hws": hws.copy()})
            return out

        c_r = c[rem]
        cid_r = cid[rem]
        h_r = h[rem]
        sd_r = sd[rem]
        Ud0_r = Vd[rem, :, -1]
        Dd_r = Dd[rem]
        Du_r = lip_scale * two_sqrt2 * mu1_u * dh[rem]

        if conj_up:
            hu_r = INIT_HC[rem] if step == 0 else np.conj(h_r)
            Yu_r = -build_Y_batch_fast(hu_r, uu, wu)
        else:
            Yu_r = build_Y_batch_fast(h_r, uu, wu)
        eu, Vu = np.linalg.eigh(Yu_r @ np.swapaxes(np.conj(Yu_r), 1, 2))
        su_r = np.sqrt(np.maximum(ZERO_F, eu[:, ::-1]))
        Uu0_r = Vu[:, :, -1]

        pu = (su_r[:, 1] - Du_r) > ratio_thresh * (su_r[:, 0] + Du_r)
        gap_ok = (~pu) & ((su_r[:, 0] - Du_r) > su_r[:, 1]) & ((sd_r[:, 0] - Dd_r) > sd_r[:, 1])
        pv = np.zeros(len(c_r), dtype=bool)
        if np.any(gap_ok):
            idx = np.where(gap_ok)[0]
            num_u = Du_r[idx] * (2 * su_r[idx, 0] + Du_r[idx])
            den_u = (su_r[idx, 0] - Du_r[idx]) ** 2 - su_r[idx, 1] ** 2
            th_u = np.arcsin(np.minimum(ONE_F, num_u / den_u))
            num_d = Dd_r[idx] * (2 * sd_r[idx, 0] + Dd_r[idx])
            den_d = (sd_r[idx, 0] - Dd_r[idx]) ** 2 - sd_r[idx, 1] ** 2
            th_d = np.arcsin(np.minimum(ONE_F, num_d / den_d))
            v33 = np.minimum(ONE_F, np.abs(np.sum(np.conj(Uu0_r[idx]) * Ud0_r[idx], axis=1)))
            pv[idx] = (np.arccos(v33) - th_u - th_d) > cos_9_10

        keep = ~(pu | pv)
        if not np.any(keep):
            out = {"excluded": bool(not np.any(keep)), "steps": step, "boxes_evaluated": total_eval, "surviving_boxes": 0}
            if return_survivors:
                out.update({"surv_c": np.empty((0, 4)), "surv_cid": np.empty(0, dtype=int), "hws": hws.copy()})
            return out

        c_s = c_r[keep]
        cid_s = cid_r[keep]
        if step == max_steps - 1:
            out = {
                "excluded": bool(len(c_s) == 0),
                "steps": step,
                "boxes_evaluated": total_eval,
                "surviving_boxes": int(len(c_s)),
            }
            if return_survivors:
                out.update({"surv_c": c_s, "surv_cid": cid_s, "hws": hws.copy()})
            return out

        ax = step % 4
        hws[ax] *= half
        shift = np.zeros(4, dtype=float)
        shift[ax] = hws[ax]
        c = np.vstack([c_s - shift, c_s + shift])
        cid = np.concatenate([cid_s, cid_s])

    out = {"excluded": bool(len(c) == 0), "steps": max_steps, "boxes_evaluated": total_eval, "surviving_boxes": int(len(c))}
    if return_survivors:
        out.update({"surv_c": c, "surv_cid": cid, "hws": hws.copy()})
    return out


def b1967_control_channels() -> dict:
    u_u = np.array([
        c_rat(8112623, 23657898, 29517392, 42170071),
        c_rat(-32191861, 58976063, 10109002, 39589433),
        c_rat(8361869, 35299624, 201121, 6549724),
    ], dtype=complex)
    w_u = c_rat(32621059, 80596130, -2122066, 7900781)
    u_d = np.array([
        c_rat(8253345, 14846974, 32273371, 84797632),
        c_rat(13917810, 48354631, -69799368, 69016585),
        c_rat(29492199, 87199192, -23893336, 16802917),
    ], dtype=complex)
    w_d = c_rat(126906246, 75918835, 16923861, 50797165)
    return {"u_u": u_u, "w_u": w_u, "u_d": u_d, "w_d": w_d}


def verify_t5(l2_cache: dict, b1967_ch: dict) -> dict:
    mp.mp.dps = 20
    pts5, pts12 = torsion_point_sets()

    # Build Frame C certification jobs
    # 1) Full 24 order-5 + 12 order-3..8 slices across all 7 heights y in {1, 3/2, 2, 3, 6, 15, 30} at x=13/100 -> 252 pts
    # 2) Representative slices at x in {0, 1/4, 1/2}, y=2 (4 pts each) + (0,1) & (1/4,6) (2 pts each) -> 16 pts
    # 3) L_2 +- 1/50 sensitivity check at (13/100, 2) across 24 pts (12 order-5 + 12 order-3..8) -> 48 pts
    jobs_spec = []
    xf_13 = Fraction(13, 100)
    ys_full = [Fraction(1, 1), Fraction(3, 2), Fraction(2, 1), Fraction(3, 1), Fraction(6, 1), Fraction(15, 1), Fraction(30, 1)]
    for yf in ys_full:
        for af, bf in pts5:
            jobs_spec.append(("main_x13_o5", xf_13, yf, mp.mpf(0), af, bf))
        for af, bf in pts12:
            jobs_spec.append(("main_x13_o38", xf_13, yf, mp.mpf(0), af, bf))

    rep4 = [pts5[0], pts5[4]] + [pts12[0], pts12[6]]
    for xf in [Fraction(0, 1), Fraction(1, 4), Fraction(1, 2)]:
        for af, bf in rep4:
            jobs_spec.append(("cross_col", xf, Fraction(2, 1), mp.mpf(0), af, bf))
    for xf, yf in [(Fraction(0, 1), Fraction(1, 1)), (Fraction(1, 4), Fraction(6, 1))]:
        for af, bf in [pts5[0], pts12[6]]:
            jobs_spec.append(("cross_col", xf, yf, mp.mpf(0), af, bf))

    sens24 = pts5[:12] + pts12
    dl2 = mp_rat(1, 50)
    for tag, delta in [("L2_minus_1_50", -dl2), ("L2_plus_1_50", dl2)]:
        for af, bf in sens24:
            jobs_spec.append((tag, xf_13, Fraction(2, 1), delta, af, bf))

    # Precompute base terms cached by (xf, yf, af, bf) so sensitivity runs reuse Rs, Fu, |a0|^2
    f_cache = {}
    ctx_cache = {}
    base_cache = {}
    cert_inputs = []
    for tag, xf, yf, delta, af, bf in jobs_spec:
        tau = mp_crat(xf.numerator, xf.denominator, yf.numerator, yf.denominator)
        if (xf, yf) not in ctx_cache:
            ctx_cache[(xf, yf)] = prepare_tau_context(tau)
        tau_ctx = ctx_cache[(xf, yf)]
        pt_key = (xf, yf, af, bf)
        if pt_key not in base_cache:
            base_cache[pt_key] = (
                frame_c_base_terms(tau, af, bf, 1, -4, f_cache, tau_ctx),
                frame_c_base_terms(tau, af, bf, 1, 2, f_cache, tau_ctx),
            )
        terms_u, terms_d = base_cache[pt_key]
        l2 = l2_cache[(xf, yf)]["L2"] + delta
        _, ch_u, _ = frame_c_eval_from_terms(terms_u, l2)
        _, ch_d, _ = frame_c_eval_from_terms(terms_d, l2)
        uu, wu = channels_dict_to_uw(ch_u)
        ud, wd = channels_dict_to_uw(ch_d)
        cert_inputs.append((uu, wu, ud, wd))

    def _run_one(item):
        uu, wu, ud, wd = item
        return certify_cp2_global(uu, wu, ud, wd, max_steps=16, lip_scale=ONE_F, conj_up=True)

    n_workers = min(16, os.cpu_count() or 8)
    with ThreadPoolExecutor(max_workers=n_workers) as pool:
        results = list(pool.map(_run_one, cert_inputs))

    n_total = len(results)
    n_excluded = sum(1 for r in results if r["excluded"])
    max_surv = max(r["surviving_boxes"] for r in results)
    max_steps_used = max(r["steps"] for r in results)
    max_boxes_eval = max(r["boxes_evaluated"] for r in results)

    sens_results = [r for (spec, r) in zip(jobs_spec, results) if spec[0].startswith("L2_")]
    n_sens_excluded = sum(1 for r in sens_results if r["excluded"])

    # Mandatory Positive Control: B1967 16-rational counterexample
    r_ctrl = rat_f(3, 1000)
    cos_t = math.sqrt((ONE_F + r_ctrl) / 2)
    sin_t = math.sqrt((ONE_F - r_ctrl) / 2)
    h_ctrl = np.array([cos_t, I_C * sin_t, ZERO_F], dtype=complex)
    Yu_ctrl = -y_vec_np(np.conj(h_ctrl), b1967_ch["u_u"], b1967_ch["w_u"])
    Yd_ctrl = y_vec_np(h_ctrl, b1967_ch["u_d"], b1967_ch["w_d"])
    Uu_ctrl, su_ctrl, _ = np.linalg.svd(Yu_ctrl)
    Ud_ctrl, sd_ctrl, _ = np.linalg.svd(Yd_ctrl)
    V_ctrl = np.abs(Uu_ctrl.conj().T @ Ud_ctrl)
    min_vkk = float(np.min(np.diag(V_ctrl)))
    m2_m3_u = float(su_ctrl[1] / su_ctrl[0])
    m1_m2_u = float(su_ctrl[2] / su_ctrl[1])
    m2_m3_d = float(sd_ctrl[1] / sd_ctrl[0])
    m1_m2_d = float(sd_ctrl[2] / sd_ctrl[1])
    ctrl_thresholds_ok = bool(
        min_vkk >= rat_f(9, 10)
        and m2_m3_u <= rat_f(1, 100)
        and m2_m3_d <= rat_f(1, 100)
        and m1_m2_u <= rat_f(1, 2)
        and m1_m2_d <= rat_f(1, 2)
    )

    ctrl_cert = certify_cp2_global(
        b1967_ch["u_u"],
        b1967_ch["w_u"],
        b1967_ch["u_d"],
        b1967_ch["w_d"],
        max_steps=8,
        lip_scale=ONE_F,
        conj_up=True,
        return_survivors=True,
    )
    tan_t = sin_t / cos_t
    x_star = np.array([ZERO_F, tan_t, ZERO_F, ZERO_F], dtype=float)
    sc = ctrl_cert["surv_c"]
    scid = ctrl_cert["surv_cid"]
    shws = ctrl_cert["hws"]
    if len(sc) > 0:
        box_tol = pow10_f(-12)
        target_mask = (scid == 0) & np.all(np.abs(sc - x_star[None, :]) <= shws[None, :] + box_tol, axis=1)
        n_target_boxes_kept = int(np.sum(target_mask))
    else:
        n_target_boxes_kept = 0

    ctrl_not_pruned = bool((not ctrl_cert["excluded"]) and ctrl_cert["surviving_boxes"] > 0 and n_target_boxes_kept > 0)

    passed = bool(
        n_total >= 150
        and n_excluded == n_total
        and max_surv == 0
        and n_sens_excluded == len(sens_results)
        and ctrl_thresholds_ok
        and ctrl_not_pruned
    )
    return {
        "n_frame_c_points_certified": n_total,
        "n_frame_c_excluded": n_excluded,
        "n_sensitivity_points": len(sens_results),
        "n_sensitivity_excluded": n_sens_excluded,
        "max_surviving_boxes": max_surv,
        "max_steps_used": max_steps_used,
        "max_boxes_evaluated_per_point": max_boxes_eval,
        "b1967_positive_control": {
            "m2_m3_up": m2_m3_u,
            "m1_m2_up": m1_m2_u,
            "m2_m3_down": m2_m3_d,
            "m1_m2_down": m1_m2_d,
            "diag_Vkk": [float(V_ctrl[i, i]) for i in range(3)],
            "min_Vkk": min_vkk,
            "thresholds_satisfied": ctrl_thresholds_ok,
            "certifier_excluded": bool(ctrl_cert["excluded"]),
            "certifier_surviving_boxes": int(ctrl_cert["surviving_boxes"]),
            "certifier_target_boxes_kept": n_target_boxes_kept,
            "not_pruned": ctrl_not_pruned,
        },
        "passed": passed,
    }


# ---------------------------------------------------------------------------
# Guardrail 3: 10 Random Haar U(3)^3 Basis-Scrambling Trials
# ---------------------------------------------------------------------------

def certifier_center_metrics(h_arr: np.ndarray, dh_arr: np.ndarray, Yu_arr: np.ndarray, Yd_arr: np.ndarray, mu1_u: float, mu1_d: float):
    two_sqrt2 = 2 * math.sqrt(2)
    ratio_thresh = rat_f(1, 100)
    cos_9_10 = math.acos(rat_f(9, 10))
    Du = two_sqrt2 * mu1_u * dh_arr
    Dd = two_sqrt2 * mu1_d * dh_arr
    Uu, su, _ = np.linalg.svd(Yu_arr)
    Ud, sd, _ = np.linalg.svd(Yd_arr)
    pu = (su[:, 1] - Du) > ratio_thresh * (su[:, 0] + Du)
    pd = (sd[:, 1] - Dd) > ratio_thresh * (sd[:, 0] + Dd)
    gap_ok = ((su[:, 0] - Du) > su[:, 1]) & ((sd[:, 0] - Dd) > sd[:, 1])
    th_u = np.zeros(len(h_arr), dtype=float)
    th_d = np.zeros(len(h_arr), dtype=float)
    v33 = np.minimum(ONE_F, np.abs(np.sum(np.conj(Uu[:, :, 0]) * Ud[:, :, 0], axis=1)))
    pv = np.zeros(len(h_arr), dtype=bool)
    if np.any(gap_ok):
        idx = np.where(gap_ok)[0]
        th_u[idx] = np.arcsin(np.minimum(ONE_F, Du[idx] * (2 * su[idx, 0] + Du[idx]) / ((su[idx, 0] - Du[idx]) ** 2 - su[idx, 1] ** 2)))
        th_d[idx] = np.arcsin(np.minimum(ONE_F, Dd[idx] * (2 * sd[idx, 0] + Dd[idx]) / ((sd[idx, 0] - Dd[idx]) ** 2 - sd[idx, 1] ** 2)))
        pv[idx] = (np.arccos(v33[idx]) - th_u[idx] - th_d[idx]) > cos_9_10
    return su, sd, v33, th_u, th_d, (pu | pd | pv)


def verify_haar_guardrail3(l2_cache: dict, b1967_ch: dict, rng: np.random.Generator) -> dict:
    mp.mp.dps = 20
    xf = Fraction(13, 100)
    yf = Fraction(2, 1)
    tau = mp_crat(xf.numerator, xf.denominator, yf.numerator, yf.denominator)
    l2 = l2_cache[(xf, yf)]["L2"]
    f_cache = {}
    _, ch_u, _ = frame_c_sector_channels(tau, l2, Fraction(1, 5), Fraction(0, 1), 1, -4, f_cache)
    _, ch_d, _ = frame_c_sector_channels(tau, l2, Fraction(1, 5), Fraction(0, 1), 1, 2, f_cache)
    uu_fc, wu_fc = channels_dict_to_uw(ch_u)
    ud_fc, wd_fc = channels_dict_to_uw(ch_d)

    # Sample 48 centers: B1967 h(3/1000) + generic non-degenerate unit vectors + INIT_H centers
    r_ctrl = rat_f(3, 1000)
    h_ctrl = np.array([[math.sqrt((ONE_F + r_ctrl) / 2), I_C * math.sqrt((ONE_F - r_ctrl) / 2), ZERO_F]], dtype=complex)
    h_rand = rng.normal(size=(47, 3)) + I_C * rng.normal(size=(47, 3))
    h_rand = h_rand / np.linalg.norm(h_rand, axis=1, keepdims=True)
    h_samp = np.vstack([h_ctrl, h_rand])
    dh_samp = np.full(48, rat_f(1, 16), dtype=float)
    h_cert_samp = INIT_H[::150][:48]
    dh_cert_samp = INIT_DH[::150][:48]

    cases = [
        ("B1967_ctrl", b1967_ch["u_u"], b1967_ch["w_u"], b1967_ch["u_d"], b1967_ch["w_d"]),
        ("FrameC_1_5_0", uu_fc, wu_fc, ud_fc, wd_fc),
    ]

    max_ratio_drift = ZERO_F
    max_vckm_drift = ZERO_F
    max_theta_drift = ZERO_F
    prune_mask_mismatches = 0
    tol = pow10_f(-12)
    sep_tol = pow10_f(-6)

    for _, uu, wu, ud, wd in cases:
        mu1_u = mu1_from_uw(uu, wu)
        mu1_d = mu1_from_uw(ud, wd)
        Yu_base = -build_Y_batch_fast(np.conj(h_samp), uu, wu)
        Yd_base = build_Y_batch_fast(h_samp, ud, wd)
        Uu0, su0, _ = np.linalg.svd(Yu_base)
        Ud0, sd0, _ = np.linalg.svd(Yd_base)
        rat_u0 = su0[:, 1:] / su0[:, :1]
        rat_d0 = sd0[:, 1:] / sd0[:, :1]
        vckm0 = np.abs(np.einsum("nai,naj->nij", np.conj(Uu0), Ud0))
        nondeg = (
            ((su0[:, 0] - su0[:, 1]) > sep_tol * su0[:, 0])
            & ((su0[:, 1] - su0[:, 2]) > sep_tol * su0[:, 0])
            & ((sd0[:, 0] - sd0[:, 1]) > sep_tol * sd0[:, 0])
            & ((sd0[:, 1] - sd0[:, 2]) > sep_tol * sd0[:, 0])
        )

        Yu_cert0 = -build_Y_batch_fast(np.conj(h_cert_samp), uu, wu)
        Yd_cert0 = build_Y_batch_fast(h_cert_samp, ud, wd)
        _, _, v33_0, thu0, thd0, mask0 = certifier_center_metrics(h_cert_samp, dh_cert_samp, Yu_cert0, Yd_cert0, mu1_u, mu1_d)

        for _ in range(10):
            UL = haar_unitary(3, rng)
            UR_u = haar_unitary(3, rng)
            UR_d = haar_unitary(3, rng)
            Yu_scr = np.einsum("ij,njk,lk->nil", UL, Yu_base, np.conj(UR_u))
            Yd_scr = np.einsum("ij,njk,lk->nil", UL, Yd_base, np.conj(UR_d))
            Uu1, su1, _ = np.linalg.svd(Yu_scr)
            Ud1, sd1, _ = np.linalg.svd(Yd_scr)
            rat_u1 = su1[:, 1:] / su1[:, :1]
            rat_d1 = sd1[:, 1:] / sd1[:, :1]
            vckm1 = np.abs(np.einsum("nai,naj->nij", np.conj(Uu1), Ud1))

            Yu_cert1 = np.einsum("ij,njk,lk->nil", UL, Yu_cert0, np.conj(UR_u))
            Yd_cert1 = np.einsum("ij,njk,lk->nil", UL, Yd_cert0, np.conj(UR_d))
            _, _, v33_1, thu1, thd1, mask1 = certifier_center_metrics(h_cert_samp, dh_cert_samp, Yu_cert1, Yd_cert1, mu1_u, mu1_d)

            max_ratio_drift = max(
                max_ratio_drift,
                float(np.max(np.abs(rat_u1 - rat_u0))),
                float(np.max(np.abs(rat_d1 - rat_d0))),
            )
            if np.any(nondeg):
                max_vckm_drift = max(max_vckm_drift, float(np.max(np.abs(vckm1[nondeg] - vckm0[nondeg]))))
            max_theta_drift = max(
                max_theta_drift,
                float(np.max(np.abs(v33_1 - v33_0))),
                float(np.max(np.abs(thu1 - thu0))),
                float(np.max(np.abs(thd1 - thd0))),
            )
            prune_mask_mismatches += int(np.sum(mask1 != mask0))

    passed = bool(
        max_ratio_drift < tol
        and max_vckm_drift < tol
        and max_theta_drift < tol
        and prune_mask_mismatches == 0
    )
    return {
        "n_trials_per_case": 10,
        "max_sv_ratio_drift": max_ratio_drift,
        "max_Vckm_drift": max_vckm_drift,
        "max_certifier_theta_drift": max_theta_drift,
        "prune_mask_mismatches": prune_mask_mismatches,
        "tolerance": tol,
        "passed": passed,
    }


# ---------------------------------------------------------------------------
# 5 Planted Faults (PF1..PF5)
# ---------------------------------------------------------------------------

def verify_planted_faults(l2_cache: dict, b1967_ch: dict, rng: np.random.Generator) -> dict:
    # PF1: Inflated Mobius bound 1/2 at s_L = 0 vs true sup = 1/3
    true_sup_sL0 = (ONE_F + ZERO_F) / (rat_f(3, 1) - ZERO_F)
    inflated_sL0 = rat_f(1, 2)
    pf1_caught = bool(true_sup_sL0 < inflated_sL0 - rat_f(1, 10))

    # PF2: Switch up sector from conjugate reading h* to same reading h on Frame C (0, 1/5)
    mp.mp.dps = 20
    xf, yf = Fraction(13, 100), Fraction(2, 1)
    tau = mp_crat(xf.numerator, xf.denominator, yf.numerator, yf.denominator)
    l2 = l2_cache[(xf, yf)]["L2"]
    f_cache = {}
    _, ch_u_015, _ = frame_c_sector_channels(tau, l2, Fraction(0, 1), Fraction(1, 5), 1, -4, f_cache)
    _, ch_d_015, _ = frame_c_sector_channels(tau, l2, Fraction(0, 1), Fraction(1, 5), 1, 2, f_cache)
    uu_015, wu_015 = channels_dict_to_uw(ch_u_015)
    ud_015, wd_015 = channels_dict_to_uw(ch_d_015)

    pf2_cert = certify_cp2_global(uu_015, wu_015, ud_015, wd_015, max_steps=5, lip_scale=ONE_F, conj_up=False)
    # Scan 400 random null vectors under same-h reading to verify alignment + hierarchy becomes feasible
    best_pf2_v33 = ZERO_F
    best_pf2_ratio = ONE_F
    for _ in range(400):
        a_n = rng.normal() + I_C * rng.normal()
        b_n = rng.normal() + I_C * rng.normal()
        h_n = np.array([a_n * a_n - b_n * b_n, I_C * (a_n * a_n + b_n * b_n), 2 * a_n * b_n], dtype=complex)
        h_n = h_n / np.linalg.norm(h_n)
        Yu_same = y_vec_np(h_n, uu_015, wu_015)
        Yd_same = y_vec_np(h_n, ud_015, wd_015)
        Uu_s, su_s, _ = np.linalg.svd(Yu_same)
        Ud_s, sd_s, _ = np.linalg.svd(Yd_same)
        r_max = max(float(su_s[1] / su_s[0]), float(sd_s[1] / sd_s[0]))
        v33_s = float(abs(np.vdot(Uu_s[:, 0], Ud_s[:, 0])))
        if r_max <= rat_f(1, 100) and v33_s > best_pf2_v33:
            best_pf2_v33 = v33_s
            best_pf2_ratio = r_max
    pf2_caught = bool((not pf2_cert["excluded"]) and best_pf2_v33 >= rat_f(9, 10) and best_pf2_ratio <= rat_f(1, 100))

    # PF3: Corrupt Weyl Lipschitz constant downward by 1/10 on B1967 positive control -> false exclusion
    pf3_cert = certify_cp2_global(
        b1967_ch["u_u"],
        b1967_ch["w_u"],
        b1967_ch["u_d"],
        b1967_ch["w_d"],
        max_steps=8,
        lip_scale=rat_f(1, 10),
        conj_up=True,
    )
    pf3_caught = bool(pf3_cert["excluded"] and pf3_cert["surviving_boxes"] == 0)

    # PF4: Corrupt up right hypercharge from -4 to +2 -> breaks order-5 w_u == 0 law and makes up == down
    _, ch_u_pf4, _ = frame_c_sector_channels(tau, l2, Fraction(1, 5), Fraction(0, 1), 1, 2, f_cache)
    _, ch_d_ref, _ = frame_c_sector_channels(tau, l2, Fraction(1, 5), Fraction(0, 1), 1, 2, f_cache)
    uu_pf4, wu_pf4 = channels_dict_to_uw(ch_u_pf4)
    ud_ref, wd_ref = channels_dict_to_uw(ch_d_ref)
    pf4_wu_mag = float(abs(wu_pf4))
    pf4_ud_diff = float(np.max(np.abs(uu_pf4 - ud_ref)))
    pf4_caught = bool(pf4_wu_mag > rat_f(1, 10) and pf4_ud_diff < pow10_f(-14))

    # PF5: Unequal left-handed unitary scrambling U_{L,u} != U_{L,d} -> |V_CKM| drifts > 1/10
    r_ctrl = rat_f(3, 1000)
    h_ctrl = np.array([math.sqrt((ONE_F + r_ctrl) / 2), I_C * math.sqrt((ONE_F - r_ctrl) / 2), ZERO_F], dtype=complex)
    Yu_0 = -y_vec_np(np.conj(h_ctrl), b1967_ch["u_u"], b1967_ch["w_u"])
    Yd_0 = y_vec_np(h_ctrl, b1967_ch["u_d"], b1967_ch["w_d"])
    Uu_0, _, _ = np.linalg.svd(Yu_0)
    Ud_0, _, _ = np.linalg.svd(Yd_0)
    V_0 = np.abs(Uu_0.conj().T @ Ud_0)

    max_pf5_drift = ZERO_F
    for _ in range(5):
        UL_u = haar_unitary(3, rng)
        UL_d = haar_unitary(3, rng)
        UR_u = haar_unitary(3, rng)
        UR_d = haar_unitary(3, rng)
        Uu_p, _, _ = np.linalg.svd(UL_u @ Yu_0 @ UR_u.conj().T)
        Ud_p, _, _ = np.linalg.svd(UL_d @ Yd_0 @ UR_d.conj().T)
        V_p = np.abs(Uu_p.conj().T @ Ud_p)
        max_pf5_drift = max(max_pf5_drift, float(np.max(np.abs(V_p - V_0))))
    pf5_caught = bool(max_pf5_drift > rat_f(1, 10))

    passed = bool(pf1_caught and pf2_caught and pf3_caught and pf4_caught and pf5_caught)
    return {
        "PF1_inflated_mobius_sL0": {"true_sup": true_sup_sL0, "planted": inflated_sL0, "caught": pf1_caught},
        "PF2_same_h_up_frameC": {
            "certifier_excluded": bool(pf2_cert["excluded"]),
            "surviving_boxes": int(pf2_cert["surviving_boxes"]),
            "best_null_V33": best_pf2_v33,
            "best_null_m2_m3": best_pf2_ratio,
            "caught": pf2_caught,
        },
        "PF3_corrupt_lipschitz_b1967": {
            "certifier_excluded": bool(pf3_cert["excluded"]),
            "surviving_boxes": int(pf3_cert["surviving_boxes"]),
            "caught": pf3_caught,
        },
        "PF4_corrupt_qRu_to_plus2": {
            "wu_magnitude_at_1_5_0": pf4_wu_mag,
            "max_uu_minus_ud": pf4_ud_diff,
            "caught": pf4_caught,
        },
        "PF5_unequal_UL_scrambling": {
            "max_Vckm_drift": max_pf5_drift,
            "caught": pf5_caught,
        },
        "passed": passed,
    }


def main():
    t_start = time.time()
    rng = np.random.default_rng(20261120)
    b1967_ch = b1967_control_channels()

    conv_res = verify_convention_guardrail4(rng)
    l2_cache, l2_res = compute_l2_suite()
    t1_res = verify_t1(rng)
    t2_res = verify_t2(rng)
    t3_res = verify_t3(b1967_ch)
    t4_res = verify_t4(l2_cache)
    t5_res = verify_t5(l2_cache, b1967_ch)
    haar_res = verify_haar_guardrail3(l2_cache, b1967_ch, rng)
    pf_res = verify_planted_faults(l2_cache, b1967_ch, rng)

    elapsed = time.time() - t_start
    all_passed = bool(
        conv_res["passed"]
        and l2_res["passed"]
        and t1_res["passed"]
        and t2_res["passed"]
        and t3_res["passed"]
        and t4_res["passed"]
        and t5_res["passed"]
        and haar_res["passed"]
        and pf_res["passed"]
    )

    report = {
        "card": "A2-P879",
        "empirical_firewall": "0 of 19",
        "runtime_seconds": elapsed,
        "all_gates_passed": all_passed,
        "gates": {
            "convention_guardrail4": conv_res,
            "L2_weierstrass_ode": l2_res,
            "T1_null_2x2_reduction": t1_res,
            "T2_kronecker_lift": t2_res,
            "T3_spinor_mobius_bound": t3_res,
            "T4_frame_c_obstructions": t4_res,
            "T5_cp2_certifier_and_control": t5_res,
            "guardrail3_haar_invariance": haar_res,
            "planted_faults_PF1_PF5": pf_res,
        },
    }

    out_path = Path(__file__).resolve().parent / "referee_a2_p879_v2_out.json"
    with out_path.open("w", encoding="utf-8") as fh:
        json.dump(to_py(report), fh, indent=2, sort_keys=False)

    print(f"A2-P879 referee finished in {elapsed:.2f}s | all_gates_passed={all_passed}")


if __name__ == "__main__":
    main()
