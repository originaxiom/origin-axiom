#!/usr/bin/env python3
"""
100% Blind Disjoint Cold-Room Zero-Trust Referee for Card AGY-002_A2-P629-VEFF-MODULUS.

Strictly 0 of 19 (ZERO empirical PDG/NuFIT/Planck/DESI/CODATA constants anywhere).
Pure Python stdlib + mpmath + sympy ONLY; python3 -I; 0 AST float/complex literals or casts;
0 JSON floats.

Disjoint numerical algorithms (Guardrail 6):
  - RP1: Dedekind eta via Euler's pentagonal number theorem; E2 via exact logarithmic
         derivative (12 / (i*pi)) * eta'/eta of the pentagonal series; E(tau, s) via
         Chowla-Selberg cross-checked against direct N=40 square-box lattice sum.
  - RP2: Weierstrass wp(z)/4 via exact Jacobi theta_1 log-derivative; Fuchsian L2(tau)
         via hybrid explicit 6th-order Yoshida Solution A (from exact BCH equations)
         + implicit 5-stage GL10 / 6-stage GL12 symplectic polish (exact Legendre roots,
         det = 1 to machine precision); Hermitian spectra & Autonne-Takagi via 6x6
         real-split symmetric mp.eigsy.
  - RP3: Curved spin-1/2 Dirac Kahler metric G_{s=1/2} via corner-split Clenshaw-Curtis
         polar quadrature + Forest-Ruth symplectic radial propagation; Piece 2 coupled
         2-loop Type-II 2HDM + 1-loop D-term quartics + 3x3 Hermitian soft-mass RGEs via
         implicit 2-stage 4th-order Gauss-Legendre (GL4); Dynamic V4 on S^5 x S^5 via
         multi-start Riemannian Armijo descent; Guardrail 3 via 10-trial Cayley-transform
         Haar U(3)^5 x U(3)_{nu_R} scrambling U = (I - i A)(I + i A)^{-1}.
  - RP4: All 6/6 planted negative controls (RPF1-RPF6) & 6/6 Referee gates (RG1-RG6).
"""

import hashlib
import json
import math
import os
import random
import sys
import time
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import sympy as sp

# ---------------------------------------------------------------------------
# Basic exact-rational / mpmath helpers (ZERO float/complex literals or casts)
# ---------------------------------------------------------------------------

def M(num, den=1):
    return mp.mpf(num) / mp.mpf(den)


def POW10(exp_int):
    return mp.mpf(10) ** exp_int


def IU():
    return mp.mpc(0, 1)


def fmt_r(val, digits=25):
    return mp.nstr(mp.mpf(mp.re(val)), digits)


def fmt_c(val, digits=25):
    return {"re": mp.nstr(mp.re(val), digits), "im": mp.nstr(mp.im(val), digits)}


def fmt_list_r(vals, digits=20):
    return [fmt_r(v, digits) for v in vals]


def assert_zero_json_floats(obj, path="$"):
    if isinstance(obj, (bool, type(None), int, str)):
        return
    if isinstance(obj, list):
        for idx, item in enumerate(obj):
            assert_zero_json_floats(item, f"{path}[{idx}]")
        return
    if isinstance(obj, dict):
        for k, v in obj.items():
            assert_zero_json_floats(v, f"{path}.{k}")
        return
    raise AssertionError(f"Forbidden JSON type at {path}: {type(obj).__name__}")


# ---------------------------------------------------------------------------
# Disjoint Modular Functions (Euler Pentagonal Theorem & Log-Derivative E2)
# ---------------------------------------------------------------------------

def eta_and_E2_pentagonal(tau):
    """
    Compute Dedekind eta(tau) via Euler's pentagonal number theorem:
        eta(tau) = exp(i*pi*tau/12) * sum_{k=-inf}^{inf} (-1)^k q^{k(3k-1)/2}
    and quasi-modular E2(tau) from the exact logarithmic derivative:
        E2(tau) = (12 / (i*pi)) * eta'(tau)/eta(tau) = 1 + 24 * (q P'(q)) / P(q).
    """
    I = IU()
    q = mp.exp(2 * I * mp.pi * tau)
    tol = POW10(-(mp.mp.dps + 8))
    P = mp.mpc(1)
    qP = mp.mpc(0)
    k = 1
    while True:
        e1 = (k * (3 * k - 1)) // 2
        e2 = (k * (3 * k + 1)) // 2
        sgn = -1 if (k % 2 == 1) else 1
        t1 = sgn * (q ** e1)
        t2 = sgn * (q ** e2)
        P += t1 + t2
        qP += e1 * t1 + e2 * t2
        if abs(t1) < tol and abs(t2) < tol:
            break
        k += 1
        if k > 2000:
            break
    eta = mp.exp(I * mp.pi * tau / 12) * P
    E2 = 1 + 24 * (qP / P)
    return eta, E2


def E2_hat(tau):
    eta, E2 = eta_and_E2_pentagonal(tau)
    y = mp.im(tau)
    return eta, E2, E2 - M(3) / (mp.pi * y)


def V_RS(tau):
    eta, _ = eta_and_E2_pentagonal(tau)
    y = mp.im(tau)
    return -mp.log(y * (abs(eta) ** 4))


def V_FILQ(tau, n, drop_nonholo=False):
    eta, E2, E2h = E2_hat(tau)
    y = mp.im(tau)
    e2_use = E2 if drop_nonholo else E2h
    pref = ((2 * y) ** (-3 * n)) * (abs(eta) ** (-12 * n))
    bracket = (mp.mpf(n) * (mp.pi ** 2) * (y ** 2) / 3) * (abs(e2_use) ** 2) - 3
    return pref * bracket


def E_chowla_selberg(tau, s, N_max=None):
    """Non-holomorphic Eisenstein series E(tau, s) = sum' y^s |m*tau+n|^{-2s}."""
    x = mp.re(tau)
    y = mp.im(tau)
    s_mp = mp.mpf(s)
    term0 = 2 * mp.zeta(2 * s_mp) * (y ** s_mp)
    term1 = (
        2
        * mp.sqrt(mp.pi)
        * (mp.gamma(s_mp - M(1, 2)) / mp.gamma(s_mp))
        * mp.zeta(2 * s_mp - 1)
        * (y ** (1 - s_mp))
    )
    pref = 8 * (mp.pi ** s_mp) * mp.sqrt(y) / mp.gamma(s_mp)
    tol = POW10(-(mp.mp.dps + 8))
    if N_max is None:
        N_max = max(40, int(mp.ceil((mp.mp.dps + 12) * mp.log(10) / (2 * mp.pi * y))) + 10)
    tot = mp.mpf(0)
    nu = s_mp - M(1, 2)
    exp_d = 1 - 2 * s_mp
    for N in range(1, N_max + 1):
        sig = mp.mpf(0)
        r_lim = int(math.isqrt(N))
        for d in range(1, r_lim + 1):
            if N % d == 0:
                sig += mp.mpf(d) ** exp_d
                q_d = N // d
                if q_d != d:
                    sig += mp.mpf(q_d) ** exp_d
        t = (mp.mpf(N) ** nu) * sig * mp.besselk(nu, 2 * mp.pi * N * y) * mp.cos(2 * mp.pi * N * x)
        tot += t
        if abs(pref * t) < tol and N > 5:
            break
    return term0 + term1 + pref * tot


def E_lattice_box(tau, s, N_box=40):
    """Direct square-box lattice sum over [-N_box, N_box]^2 \\ {(0, 0)}."""
    y = mp.im(tau)
    ys = y ** s
    s_int = int(s)
    tot = mp.mpf(0)
    for m in range(-N_box, N_box + 1):
        for n in range(-N_box, N_box + 1):
            if m == 0 and n == 0:
                continue
            z = m * tau + n
            norm2 = mp.re(z) ** 2 + mp.im(z) ** 2
            tot += ys / (norm2 ** s_int)
    return tot


def E_half_period_lattice_box(tau, s, N_box=40):
    """
    Sum of the 3 nontrivial half-period character Eisenstein sums on [-N_box, N_box]^2:
        sum_{(a,b) in {(1/2,0),(0,1/2),(1/2,1/2)}} sum' (-1)^{2am+2bn} y^s |m*tau+n|^{-2s}
    Note: sum_{(a,b)!=0} (-1)^{2am+2bn} = +3 if (m,n) both even else -1.
    """
    y = mp.im(tau)
    ys = y ** s
    s_int = int(s)
    tot_char = mp.mpf(0)
    tot_full = mp.mpf(0)
    for m in range(-N_box, N_box + 1):
        for n in range(-N_box, N_box + 1):
            if m == 0 and n == 0:
                continue
            z = m * tau + n
            norm2 = mp.re(z) ** 2 + mp.im(z) ** 2
            term = ys / (norm2 ** s_int)
            tot_full += term
            wt = 3 if (m % 2 == 0 and n % 2 == 0) else -1
            tot_char += wt * term
    return tot_char, tot_full


def grad_hess_2d(fn, x0, y0, hx, hy=None):
    """4th-order central finite-difference gradient and 2D Hessian."""
    if hy is None:
        hy = hx
    f0 = fn(x0, y0)
    fxp1 = fn(x0 + hx, y0)
    fxm1 = fn(x0 - hx, y0)
    fxp2 = fn(x0 + 2 * hx, y0)
    fxm2 = fn(x0 - 2 * hx, y0)
    fyp1 = fn(x0, y0 + hy)
    fym1 = fn(x0, y0 - hy)
    fyp2 = fn(x0, y0 + 2 * hy)
    fym2 = fn(x0, y0 - 2 * hy)
    fpp = fn(x0 + hx, y0 + hy)
    fpm = fn(x0 + hx, y0 - hy)
    fmp = fn(x0 - hx, y0 + hy)
    fmm = fn(x0 - hx, y0 - hy)
    gx = (-fxp2 + 8 * fxp1 - 8 * fxm1 + fxm2) / (12 * hx)
    gy = (-fyp2 + 8 * fyp1 - 8 * fym1 + fym2) / (12 * hy)
    hxx = (-fxp2 + 16 * fxp1 - 30 * f0 + 16 * fxm1 - fxm2) / (12 * hx * hx)
    hyy = (-fyp2 + 16 * fyp1 - 30 * f0 + 16 * fym1 - fym2) / (12 * hy * hy)
    hxy = (fpp - fpm - fmp + fmm) / (4 * hx * hy)
    tr = hxx + hyy
    disc = mp.sqrt((hxx - hyy) ** 2 + 4 * hxy * hxy)
    lam1 = (tr - disc) / 2
    lam2 = (tr + disc) / 2
    return f0, gx, gy, hxx, hyy, hxy, lam1, lam2


def newton_2d_min(fn, x_init, y_init, h_step, tol_grad, max_iter=25):
    """2D Newton minimization with backtracking, zero hardcoded target coordinates."""
    x, y = mp.mpf(x_init), mp.mpf(y_init)
    for it in range(max_iter):
        f0, gx, gy, hxx, hyy, hxy, lam1, lam2 = grad_hess_2d(fn, x, y, h_step)
        gnorm = mp.sqrt(gx * gx + gy * gy)
        if gnorm < tol_grad:
            return x, y, f0, gx, gy, hxx, hyy, hxy, lam1, lam2, it
        det = hxx * hyy - hxy * hxy
        if det <= 0 or hxx <= 0:
            # fallback gradient step
            step = M(1, 20)
            dx = -step * gx / (gnorm + 1)
            dy = -step * gy / (gnorm + 1)
        else:
            dx = -(hyy * gx - hxy * gy) / det
            dy = -(-hxy * gx + hxx * gy) / det
        # Backtrack to stay in upper half-plane and decrease |grad| or f
        alpha = mp.mpf(1)
        while alpha > POW10(-12):
            xn = x + alpha * dx
            yn = y + alpha * dy
            if yn > M(1, 2):
                fn_val = fn(xn, yn)
                if fn_val <= f0 + POW10(-25):
                    x, y = xn, yn
                    break
            alpha /= 2
        else:
            x = x + alpha * dx
            y = y + alpha * dy
    f0, gx, gy, hxx, hyy, hxy, lam1, lam2 = grad_hess_2d(fn, x, y, h_step)
    return x, y, f0, gx, gy, hxx, hyy, hxy, lam1, lam2, max_iter


# ---------------------------------------------------------------------------
# Module RP1 — Pure Bosonic Modular Potentials & FILQ (1990) Benchmarks
# ---------------------------------------------------------------------------

def elapsed_sec_str(t0_ns):
    dt_ms = (time.monotonic_ns() - t0_ns) // 1000000
    return fmt_r(M(dt_ms, 1000), 6)


def run_RP1():
    t0_ns = time.monotonic_ns()
    mp.mp.dps = 50
    I = IU()
    tau_gen = M(137, 1000) + I * M(1213, 1000)
    tau_i = I
    tau_w = M(1, 2) + I * mp.sqrt(3) / 2

    # 1. T and S invariance of E3, E2, V_RS at tau_gen
    ts_checks = {}
    for name, fn in [
        ("E3", lambda t: E_chowla_selberg(t, 3)),
        ("E2", lambda t: E_chowla_selberg(t, 2)),
        ("V_RS", V_RS),
    ]:
        v0 = fn(tau_gen)
        vT = fn(tau_gen + 1)
        vS = fn(-1 / tau_gen)
        err_T = abs(vT - v0) / (abs(v0) + 1)
        err_S = abs(vS - v0) / (abs(v0) + 1)
        ts_checks[name] = {
            "val": fmt_r(v0, 30),
            "T_rel_err": fmt_r(err_T, 10),
            "S_rel_err": fmt_r(err_S, 10),
            "pass": bool(err_T < POW10(-30) and err_S < POW10(-30)),
        }

    # 2. Chowla-Selberg vs direct N=40 square-box lattice sum at s=3
    E3_cs_gen = E_chowla_selberg(tau_gen, 3)
    E3_lat_gen = E_lattice_box(tau_gen, 3, N_box=40)
    lat_rel_err = abs(E3_lat_gen - E3_cs_gen) / abs(E3_cs_gen)

    # 3. Exact -15/16 half-period spin-structure sum (exact Fraction proof + N=40 lattice check)
    # Algebraic proof: sum_{(a,b) in {(1/2,0),(0,1/2),(1/2,1/2)}} (-1)^{2am+2bn}
    #   = +3 for (m,n) in 2Z^2, -1 otherwise -> 4 * 2^{-2s} - 1 = 2^{2-2s} - 1.
    # For s = 3: Fraction(4, 2**6) - Fraction(1, 1) = Fraction(-15, 16).
    exact_half_period_frac = Fraction(4, 2 ** 6) - Fraction(1, 1)
    assert exact_half_period_frac == Fraction(-15, 16)
    char_sum_40, full_sum_40 = E_half_period_lattice_box(tau_gen, 3, N_box=40)
    # Exact finite-box identity: char_sum(N=40) == (4/64)*E_lat(N=20) - E_lat(N=40)
    full_sum_20 = E_lattice_box(tau_gen, 3, N_box=20)
    finite_box_id_err = abs(char_sum_40 - (M(1, 16) * full_sum_20 - full_sum_40))
    lattice_ratio = char_sum_40 / full_sum_40
    ratio_err_vs_minus15_16 = abs(lattice_ratio - M(-15, 16))

    # 4. Kronecker first limit formula at i, omega_+, tau_gen
    # lim_{s->1} (E(tau, s) - pi/(s-1)) = pi*V_RS(tau) + 2*pi*(gamma - ln 2)
    # Use symmetric Richardson extrapolation at eps and eps/2 for exact limit to < 1e-22!
    kronecker = {}
    eps1 = POW10(-10)
    eps2 = eps1 / 2
    for lbl, tpt in [("i", tau_i), ("omega", tau_w), ("tau_gen", tau_gen)]:
        rhs = mp.pi * V_RS(tpt) + 2 * mp.pi * (mp.euler - mp.log(2))
        f_p1 = E_chowla_selberg(tpt, 1 + eps1) - mp.pi / eps1
        f_m1 = E_chowla_selberg(tpt, 1 - eps1) + mp.pi / eps1
        lim1 = (f_p1 + f_m1) / 2
        f_p2 = E_chowla_selberg(tpt, 1 + eps2) - mp.pi / eps2
        f_m2 = E_chowla_selberg(tpt, 1 - eps2) + mp.pi / eps2
        lim2 = (f_p2 + f_m2) / 2
        lhs_rich = (4 * lim2 - lim1) / 3
        err = abs(lhs_rich - rhs)
        kronecker[lbl] = {
            "lhs_extrap": fmt_r(lhs_rich, 25),
            "rhs_exact": fmt_r(rhs, 25),
            "abs_err": fmt_r(err, 10),
            "pass": bool(err < POW10(-16)),
        }

    # 5. Critical points & Hessian classification of E3, E2, V_RS at i (saddle) and omega_+ (min)
    bosonic_crit = {}
    h_fd = POW10(-6)
    for name, fn in [
        ("E3", lambda x, y: E_chowla_selberg(x + I * y, 3)),
        ("E2", lambda x, y: E_chowla_selberg(x + I * y, 2)),
        ("V_RS", lambda x, y: V_RS(x + I * y)),
    ]:
        fi, gxi, gyi, hxxi, hyyi, hxyi, l1i, l2i = grad_hess_2d(fn, M(0), M(1), h_fd)
        fw, gxw, gyw, hxxw, hyyw, hxyw, l1w, l2w = grad_hess_2d(fn, M(1, 2), mp.sqrt(3) / 2, h_fd)
        f2i = fn(M(0), M(2))
        f4i = fn(M(0), M(4))
        gn_i = mp.sqrt(gxi ** 2 + gyi ** 2)
        gn_w = mp.sqrt(gxw ** 2 + gyw ** 2)
        iso_w = abs(l1w - l2w) / (abs(l2w) + 1)
        saddle_i = bool(gn_i < POW10(-15) and l1i < 0 and l2i > 0)
        min_w = bool(gn_w < POW10(-15) and l1w > 0 and l2w > 0 and iso_w < POW10(-12))
        cusp_mono = bool(fw < fi < f2i < f4i)
        bosonic_crit[name] = {
            "val_omega": fmt_r(fw, 25),
            "val_i": fmt_r(fi, 25),
            "val_2i": fmt_r(f2i, 25),
            "val_4i": fmt_r(f4i, 25),
            "i_grad_norm": fmt_r(gn_i, 10),
            "i_eigs": [fmt_r(l1i, 18), fmt_r(l2i, 18)],
            "i_is_saddle": saddle_i,
            "omega_grad_norm": fmt_r(gn_w, 10),
            "omega_eigs": [fmt_r(l1w, 18), fmt_r(l2w, 18)],
            "omega_isotropy_rel": fmt_r(iso_w, 10),
            "omega_is_min": min_w,
            "cusp_monotone": cusp_mono,
        }

    # 6. FILQ (1990) zero-parameter N=1 SUGRA modular potentials V_{FILQ, n}, n = 1, 2, 3
    filq_res = {}
    for n in (1, 2, 3):
        v0 = V_FILQ(tau_gen, n)
        vT = V_FILQ(tau_gen + 1, n)
        vS = V_FILQ(-1 / tau_gen, n)
        err_T = abs(vT - v0) / (abs(v0) + 1)
        err_S = abs(vS - v0) / (abs(v0) + 1)

        fn_n = lambda x, y, nn=n: V_FILQ(x + I * y, nn)
        # Neutral start (0, 3/2) — Guardrail 1: zero target coordinates baked in!
        xs, ys, Vs, gxs, gys, hxxs, hyys, hxys, l1s, l2s, n_it = newton_2d_min(
            fn_n, M(0), M(3, 2), POW10(-7), POW10(-25), max_iter=40
        )
        gn = mp.sqrt(gxs ** 2 + gys ** 2)
        Vi = fn_n(M(0), M(1))
        Vw = fn_n(M(1, 2), mp.sqrt(3) / 2)
        V2i = fn_n(M(0), M(2))
        V4i = fn_n(M(0), M(4))
        filq_res[f"n={n}"] = {
            "T_rel_err": fmt_r(err_T, 10),
            "S_rel_err": fmt_r(err_S, 10),
            "x_star": fmt_r(xs, 25),
            "y_star": fmt_r(ys, 25),
            "V_star": fmt_r(Vs, 25),
            "grad_norm": fmt_r(gn, 10),
            "V_xx": fmt_r(hxxs, 20),
            "V_yy": fmt_r(hyys, 20),
            "V_xy": fmt_r(hxys, 15),
            "hess_eigs": [fmt_r(l1s, 20), fmt_r(l2s, 20)],
            "V_i": fmt_r(Vi, 22),
            "V_omega": fmt_r(Vw, 22),
            "V_2i": fmt_r(V2i, 22),
            "V_4i": fmt_r(V4i, 22),
            "iters": int(n_it),
            "pass": bool(
                err_T < POW10(-30)
                and err_S < POW10(-30)
                and gn < POW10(-20)
                and hxxs > 0
                and hyys > 0
                and l1s > 0
                and Vs < Vi < Vw
                and 0 < V2i < V4i
            ),
        }

    rp1_pass = bool(
        all(v["pass"] for v in ts_checks.values())
        and lat_rel_err < POW10(-5)
        and exact_half_period_frac == Fraction(-15, 16)
        and finite_box_id_err < POW10(-40)
        and ratio_err_vs_minus15_16 < POW10(-5)
        and all(v["pass"] for v in kronecker.values())
        and all(
            v["i_is_saddle"] and v["omega_is_min"] and v["cusp_monotone"]
            for v in bosonic_crit.values()
        )
        and all(v["pass"] for v in filq_res.values())
    )

    return {
        "ts_invariance": ts_checks,
        "E3_lattice_vs_cs_N40": {
            "E3_cs": fmt_r(E3_cs_gen, 25),
            "E3_lat_N40": fmt_r(E3_lat_gen, 25),
            "rel_err": fmt_r(lat_rel_err, 10),
        },
        "half_period_spin_sum_s3": {
            "exact_fraction": f"{exact_half_period_frac.numerator}/{exact_half_period_frac.denominator}",
            "lattice_N40_ratio": fmt_r(lattice_ratio, 20),
            "abs_err_vs_minus15_16": fmt_r(ratio_err_vs_minus15_16, 10),
            "finite_box_identity_err": fmt_r(finite_box_id_err, 10),
        },
        "kronecker_first_limit": kronecker,
        "bosonic_critical_points": bosonic_crit,
        "FILQ_1990": filq_res,
        "pass": rp1_pass,
        "elapsed_sec": elapsed_sec_str(t0_ns),
    }, {
        "y_filq1": mp.mpf(filq_res["n=1"]["y_star"]),
        "y_filq3": mp.mpf(filq_res["n=3"]["y_star"]),
    }


# ---------------------------------------------------------------------------
# Disjoint Fuchsian Solver: Theta_1 Log-Deriv wp(z) + Yoshida 6A + GL10/GL12
# ---------------------------------------------------------------------------

def build_yoshida_6a():
    """
    Derive Yoshida (1990) 6th-order Solution A symmetric splitting weights from
    the exact 3 BCH equations (sum w^3 = 0, sum w^5 = 0, sum w^3 P^2 = 0) at
    current mp.mp.dps — ZERO float literals.
    """
    w1, w2, w3 = sp.symbols("w1 w2 w3")
    w0 = 1 - 2 * (w1 + w2 + w3)
    ws = [w3, w2, w1, w0, w1, w2, w3]
    P = []
    cum = sp.Integer(0)
    for w in ws:
        P.append(cum + w / 2 - sp.Rational(1, 2))
        cum += w
    f1 = sp.expand(sum(w ** 3 for w in ws))
    f2 = sp.expand(sum(w ** 5 for w in ws))
    f3 = sp.expand(sum((w ** 3) * (p ** 2) for w, p in zip(ws, P)))
    F1 = sp.lambdify((w1, w2, w3), f1)
    F2 = sp.lambdify((w1, w2, w3), f2)
    F3 = sp.lambdify((w1, w2, w3), f3)
    sol = mp.findroot([F1, F2, F3], (M(-6, 5), M(1, 4), M(4, 5)))
    w1v, w2v, w3v = mp.re(sol[0]), mp.re(sol[1]), mp.re(sol[2])
    w0v = 1 - 2 * (w1v + w2v + w3v)
    return [w3v, w2v, w1v, w0v, w1v, w2v, w3v]


def build_gl_tableau(stages):
    """
    Exact s-stage Gauss-Legendre symplectic Runge-Kutta tableau (order 2s)
    from exact integer Legendre polynomial P_s(t) = 0 — ZERO float literals.
    Supports stages = 2 (GL4), 5 (GL10), 6 (GL12).
    """
    if stages == 2:
        r = mp.sqrt(3) / 3
        c_gl = [(1 - r) / 2, (1 + r) / 2]
    elif stages == 5:
        s70 = mp.sqrt(70)
        r1 = mp.sqrt((35 + 2 * s70) / 63)
        r2 = mp.sqrt((35 - 2 * s70) / 63)
        c_gl = [(1 - r1) / 2, (1 - r2) / 2, M(1, 2), (1 + r2) / 2, (1 + r1) / 2]
    elif stages == 6:
        # P_6(t) = (231 t^6 - 315 t^4 + 105 t^2 - 5)/16 = 0 -> cubic in u = t^2
        u_roots = sorted(
            [mp.re(r) for r in mp.polyroots([mp.mpf(231), mp.mpf(-315), mp.mpf(105), mp.mpf(-5)])]
        )
        t_pos = [mp.sqrt(u) for u in u_roots]
        c_gl = [
            (1 - t_pos[2]) / 2,
            (1 - t_pos[1]) / 2,
            (1 - t_pos[0]) / 2,
            (1 + t_pos[0]) / 2,
            (1 + t_pos[1]) / 2,
            (1 + t_pos[2]) / 2,
        ]
    else:
        raise ValueError(f"Unsupported GL stages: {stages}")

    s = len(c_gl)
    V_mat = mp.matrix([[c_gl[j] ** k for j in range(s)] for k in range(s)])
    b_gl = mp.lu_solve(V_mat, mp.matrix([M(1, k + 1) for k in range(s)]))
    A_gl = mp.matrix(s, s)
    for i in range(s):
        row = mp.lu_solve(V_mat, mp.matrix([(c_gl[i] ** (k + 1)) / (k + 1) for k in range(s)]))
        for j in range(s):
            A_gl[i, j] = row[j]
    A2_gl = A_gl * A_gl
    b1mc = [b_gl[j] * (1 - c_gl[j]) for j in range(s)]
    return c_gl, [b_gl[j] for j in range(s)], A_gl, A2_gl, b1mc


def wp_theta1(z, tau, E2_val):
    """
    Weierstrass wp(z; tau) via exact Jacobi theta_1 logarithmic derivative:
        wp(z) = -d^2/dz^2 ln theta_1(pi*z, tau) - (pi^2 / 3) * E2(tau).
    Reduces z mod Z*tau + Z first for uniform super-exponential convergence at all y.
    """
    I = IU()
    y = mp.im(tau)
    m = mp.nint(mp.im(z) / y)
    z = z - m * tau
    n = mp.nint(mp.re(z))
    z = z - n
    v = mp.pi * z
    q = mp.exp(2 * I * mp.pi * tau)
    tol = POW10(-(mp.mp.dps + 8))
    s0 = mp.mpc(0)
    s1 = mp.mpc(0)
    s2 = mp.mpc(0)
    k = 0
    while True:
        sgn = -1 if (k % 2 == 1) else 1
        qn = sgn * (q ** ((k * (k + 1)) // 2))
        mo = 2 * k + 1
        sv = mp.sin(mo * v)
        cv = mp.cos(mo * v)
        t0 = qn * sv
        s0 += t0
        s1 += qn * mo * cv
        s2 -= qn * (mo * mo) * sv
        if abs(t0) < tol and k > 2:
            break
        k += 1
        if k > 400:
            break
    d2log = (mp.pi ** 2) * (s2 * s0 - s1 * s1) / (s0 * s0)
    return -d2log - (mp.pi ** 2 / 3) * E2_val


def precomp_y6a(zs, ze, tau, E2_val, ns, y6_weights):
    dz = (ze - zs) / ns
    items = []
    z = zs
    for _ in range(ns):
        for w in y6_weights:
            h = w * dz
            h2 = h / 2
            V0 = wp_theta1(z + h2, tau, E2_val) / 4
            items.append((h, h2, V0))
            z += h
    return items


def prop_y6a(items, c):
    m00 = mp.mpc(1)
    m01 = mp.mpc(0)
    m10 = mp.mpc(0)
    m11 = mp.mpc(1)
    for (h, h2, V0) in items:
        m00 += h2 * m10
        m01 += h2 * m11
        hV = h * (V0 + c)
        m10 -= hV * m00
        m11 -= hV * m01
        m00 += h2 * m10
        m01 += h2 * m11
    return mp.matrix([[m00, m01], [m10, m11]])


def precomp_gl(zs, ze, tau, E2_val, ns, gl_tab):
    c_gl = gl_tab[0]
    s = len(c_gl)
    h = (ze - zs) / ns
    steps = []
    for step in range(ns):
        zb = zs + step * h
        V0 = [wp_theta1(zb + c_gl[i] * h, tau, E2_val) / 4 for i in range(s)]
        steps.append((h, V0))
    return steps


def prop_gl(steps, c, gl_tab):
    c_gl, b_gl, _, A2_gl, b1mc = gl_tab
    s = len(c_gl)
    Mmat = mp.matrix([[mp.mpc(1), mp.mpc(0)], [mp.mpc(0), mp.mpc(1)]])
    for (h, V0) in steps:
        h2 = h * h
        Vs = [v + c for v in V0]
        S = mp.matrix(s, s)
        for i in range(s):
            vh2 = Vs[i] * h2
            for j in range(s):
                S[i, j] = (mp.mpc(1) if i == j else mp.mpc(0)) + vh2 * A2_gl[i, j]
        Sinv = S ** (-1)
        Mn = mp.matrix(2, 2)
        for col in range(2):
            u0 = Mmat[0, col]
            p0 = Mmat[1, col]
            rhs = [-Vs[i] * (u0 + h * c_gl[i] * p0) for i in range(s)]
            L = [sum(Sinv[i, j] * rhs[j] for j in range(s)) for i in range(s)]
            Mn[0, col] = u0 + h * p0 + h2 * sum(b1mc[j] * L[j] for j in range(s))
            Mn[1, col] = p0 + h * sum(b_gl[i] * L[i] for i in range(s))
        Mmat = Mn
    return Mmat


def frobenius_series_wp(tau, E2_val, c_acc, N_frob=28, M_pts=36):
    """Laurent expansion of wp(z)/4 + c around z=0 and exact Frobenius recurrence."""
    I = IU()
    y = mp.im(tau)
    rad = min(M(1, 10), y / 10)
    p = [mp.mpc(0)] * N_frob
    for j in range(M_pts):
        ang = 2 * mp.pi * j / M_pts
        zj = rad * mp.exp(I * ang)
        fj = wp_theta1(zj, tau, E2_val) / 4 - M(1, 4) / (zj * zj) + c_acc
        for k in range(0, N_frob, 2):
            p[k] += fj * mp.exp(-I * k * ang) / (M_pts * (rad ** k))
    a = [mp.mpc(0)] * (N_frob + 2)
    a[0] = mp.mpc(1)
    for n in range(2, N_frob + 2, 2):
        s_val = mp.mpc(0)
        for m in range(0, n - 1, 2):
            s_val += p[n - 2 - m] * a[m]
        a[n] = -s_val / (n * n)
    b = [mp.mpc(0)] * (N_frob + 2)
    for n in range(2, N_frob + 2, 2):
        s_val = 2 * n * a[n]
        for m in range(2, n - 1, 2):
            s_val += p[n - 2 - m] * b[m]
        b[n] = -s_val / (n * n)
    return a, b, rad


def eval_frobenius_W(zs, a, b):
    sq = mp.sqrt(zs)
    lz = mp.log(zs)
    ur = mp.mpc(0)
    dur = mp.mpc(0)
    ul = mp.mpc(0)
    dul = mp.mpc(0)
    for n in range(0, len(a), 2):
        zn = zs ** n
        ur += a[n] * sq * zn
        dur += a[n] * (n + M(1, 2)) * (sq / zs) * zn
        ul += b[n] * sq * zn
        dul += b[n] * (n + M(1, 2)) * (sq / zs) * zn
    return mp.matrix([[ur, ur * lz + ul], [dur, dur * lz + ur / zs + dul]])


def solve_fuchsian_L2(tau, hi_prec=False):
    """
    Disjoint Fuchsian solver for length-2 horocycle L2(tau) and accessory parameter c(tau):
      Stage 1: Explicit 6th-order Yoshida Solution A with precomputed wp(z)/4 to converge
               c(tau) rapidly via holomorphic Gauss-Newton (ZERO matrix inversions).
      Stage 2: Implicit symplectic GL10 (normal) or GL12 (hi_prec) polish + geometrically
               graded ray Frobenius extraction of A(tau) -> L2(tau) = pi - A(tau)/2.
    """
    I = IU()
    old_dps = mp.mp.dps
    y_in = mp.im(mp.mpc(tau))
    work_dps = 46 if hi_prec else (36 if y_in > 3 else 32)
    mp.mp.dps = work_dps
    tau = mp.mpc(tau)
    x = mp.re(tau)
    y = mp.im(tau)
    _, E2_val = eta_and_E2_pentagonal(tau)
    z0 = M(1, 2) + tau / 2

    # Stage 1: Yoshida 6A fast solve for c(tau)
    y6w = build_yoshida_6a()
    ns_a1 = 22 if y >= 1 else 28
    it_a1 = precomp_y6a(z0, z0 + 1, tau, E2_val, ns_a1, y6w)
    if y > M(3, 2):
        f = min(M(1, 3), 1 / y)
        zm = z0 + tau / 2
        w1 = zm - f * tau
        w2 = zm + f * tau
        it_b1 = (
            precomp_y6a(z0, w1, tau, E2_val, 14, y6w)
            + precomp_y6a(w1, w2, tau, E2_val, 22, y6w)
            + precomp_y6a(w2, z0 + tau, tau, E2_val, 14, y6w)
        )
    else:
        it_b1 = precomp_y6a(z0, z0 + tau, tau, E2_val, 24, y6w)

    def eval_y6(c_val):
        Ta = prop_y6a(it_a1, c_val)
        Tb = prop_y6a(it_b1, c_val)
        Tab = Tb * Ta
        return Ta[0, 0] + Ta[1, 1], Tb[0, 0] + Tb[1, 1], Tab[0, 0] + Tab[1, 1]

    c = (mp.pi ** 2 / 12) * (E2_val - M(3) / (mp.pi * y))
    eps1 = POW10(-11)
    for _ in range(10):
        tra, trb, trab = eval_y6(c)
        r = [mp.im(tra), mp.im(trb), mp.im(trab)]
        res1 = mp.sqrt(r[0] ** 2 + r[1] ** 2 + r[2] ** 2) / (abs(trb) + 1)
        if res1 < POW10(-10):
            break
        tra_p, trb_p, trab_p = eval_y6(c + eps1)
        dta = (tra_p - tra) / eps1
        dtb = (trb_p - trb) / eps1
        dtab = (trab_p - trab) / eps1
        J = mp.matrix([
            [mp.im(dta), mp.re(dta)],
            [mp.im(dtb), mp.re(dtb)],
            [mp.im(dtab), mp.re(dtab)],
        ])
        dc = mp.lu_solve(J.T * J, -(J.T * mp.matrix(r)))
        c = c + dc[0] + I * dc[1]

    # Stage 2: High-order symplectic GL10 / GL12 polish
    gl_stages = 6 if hi_prec else 5
    gl_tab = build_gl_tableau(gl_stages)
    if hi_prec:
        ns_a2 = 56 if y >= 1 else 68
        ns_b_mid = 56
        ns_b_end = 28
        ns_b_plain = 64
        N_frob, M_pts, ns_ray = 38, 48, 22
        tol_res = POW10(-34)
        eps2 = POW10(-17)
    else:
        ns_a2 = 34 if y >= 1 else 42
        ns_b_mid = 34
        ns_b_end = 18
        ns_b_plain = 38
        N_frob, M_pts, ns_ray = 28, 36, 18
        tol_res = POW10(-22)
        eps2 = POW10(-13)

    st_a = precomp_gl(z0, z0 + 1, tau, E2_val, ns_a2, gl_tab)
    if y > M(3, 2):
        f = min(M(1, 3), 1 / y)
        zm = z0 + tau / 2
        w1 = zm - f * tau
        w2 = zm + f * tau
        st_b = (
            precomp_gl(z0, w1, tau, E2_val, ns_b_end, gl_tab)
            + precomp_gl(w1, w2, tau, E2_val, ns_b_mid, gl_tab)
            + precomp_gl(w2, z0 + tau, tau, E2_val, ns_b_end, gl_tab)
        )
    else:
        st_b = precomp_gl(z0, z0 + tau, tau, E2_val, ns_b_plain, gl_tab)

    def eval_gl(c_val):
        Ta = prop_gl(st_a, c_val, gl_tab)
        Tb = prop_gl(st_b, c_val, gl_tab)
        Tab = Tb * Ta
        return Ta, Tb, Ta[0, 0] + Ta[1, 1], Tb[0, 0] + Tb[1, 1], Tab[0, 0] + Tab[1, 1]

    Ta = Tb = None
    res = mp.mpf(1)
    for _ in range(5):
        Ta, Tb, tra, trb, trab = eval_gl(c)
        r = [mp.im(tra), mp.im(trb), mp.im(trab)]
        res = mp.sqrt(r[0] ** 2 + r[1] ** 2 + r[2] ** 2) / (abs(trb) + 1)
        if res < tol_res:
            break
        _, _, tra_p, trb_p, trab_p = eval_gl(c + eps2)
        dta = (tra_p - tra) / eps2
        dtb = (trb_p - trb) / eps2
        dtab = (trab_p - trab) / eps2
        J = mp.matrix([
            [mp.im(dta), mp.re(dta)],
            [mp.im(dtb), mp.re(dtb)],
            [mp.im(dtab), mp.re(dtab)],
        ])
        dc = mp.lu_solve(J.T * J, -(J.T * mp.matrix(r)))
        c = c + dc[0] + I * dc[1]
    Ta, Tb, tra, trb, trab = eval_gl(c)
    res = mp.sqrt(mp.im(tra) ** 2 + mp.im(trb) ** 2 + mp.im(trab) ** 2) / (abs(trb) + 1)
    det_err = max(
        abs(Ta[0, 0] * Ta[1, 1] - Ta[0, 1] * Ta[1, 0] - 1),
        abs(Tb[0, 0] * Tb[1, 1] - Tb[0, 1] * Tb[1, 0] - 1),
    )

    # Frobenius extraction along geometrically graded inward ray
    a_coef, b_coef, rad = frobenius_series_wp(tau, E2_val, c, N_frob=N_frob, M_pts=M_pts)
    z_near = M(1, 2) + I * min(y / 2, M(1, 2))
    zs = (rad / 2) * (z_near / abs(z_near))
    Wf = eval_frobenius_W(zs, a_coef, b_coef)
    way = [zs, 2 * zs, 4 * zs, z_near]
    if abs(z_near - z0) > M(1, 100):
        way.append(z0)
    st_r = []
    for k in range(len(way) - 1):
        st_r += precomp_gl(way[k], way[k + 1], tau, E2_val, ns_ray, gl_tab)
    P_in = prop_gl(st_r, c, gl_tab)
    Wz0 = P_in * Wf
    Wi = mp.matrix([[Wz0[1, 1], -Wz0[0, 1]], [-Wz0[1, 0], Wz0[0, 0]]])
    Ma = (Wi * Ta * Wz0).T
    Mb = (Wi * Tb * Wz0).T
    Aa = 2 * mp.re(mp.conj(Ma[0, 1]) * Ma[1, 1]) / (abs(Ma[0, 1]) ** 2)
    Ab = 2 * mp.re(mp.conj(Mb[0, 1]) * Mb[1, 1]) / (abs(Mb[0, 1]) ** 2)
    L2 = mp.pi - Aa / 2
    diff_A = abs(Aa - Ab)

    mp.mp.dps = old_dps
    return {
        "c": c,
        "L2": L2,
        "A": Aa,
        "Aa_Ab_diff": diff_A,
        "trace_res": res,
        "det_err": det_err,
    }


# ---------------------------------------------------------------------------
# Frame C Exact Construction & Disjoint 6x6 Real-Split Linear Algebra
# ---------------------------------------------------------------------------

def build_frame_C_constants():
    I = IU()
    I2 = mp.matrix([[1, 0], [0, 1]])
    QI = mp.matrix([[I, 0], [0, -I]])
    QJ = mp.matrix([[0, 1], [-1, 0]])
    QK = QI * QJ
    EPS = QJ
    BL = [QJ, QI, QK]
    U_list = [("1", I2), ("i", QI), ("j", QJ), ("k", QK)]
    Gmat = mp.matrix(4, 4)
    for a_idx, (_, ua) in enumerate(U_list):
        EU = EPS * ua
        for idx_mn, (m, n) in enumerate([(0, 0), (0, 1), (1, 0), (1, 1)]):
            Gmat[a_idx, idx_mn] = EU[m, n]
    Ginv = Gmat ** (-1)
    edual = {
        name: mp.matrix([[Ginv[0, b_idx], Ginv[1, b_idx]], [Ginv[2, b_idx], Ginv[3, b_idx]]])
        for b_idx, (name, _) in enumerate(U_list)
    }
    Q_basis = [QI, QJ, QK]
    T_qs = []
    for Q in Q_basis:
        d_s = {}
        for s_name, E in edual.items():
            M3 = mp.matrix(3, 3)
            for ra in range(3):
                for rb in range(3):
                    B = BL[ra].T * EPS * Q * BL[rb]
                    M3[ra, rb] = (
                        B[0, 0] * E[0, 0]
                        + B[0, 1] * E[0, 1]
                        + B[1, 0] * E[1, 0]
                        + B[1, 1] * E[1, 1]
                    )
            d_s[s_name] = M3
        T_qs.append(d_s)

    # 288 primitive pairs of E[30]_{prim} / +-
    pts = []
    seen = set()
    for a in range(30):
        for b in range(30):
            if math.gcd(math.gcd(a, b), 30) == 1:
                key = min((a, b), ((-a) % 30, (-b) % 30))
                if key not in seen:
                    seen.add(key)
                    pts.append(key)
    assert len(pts) == 288
    return T_qs, pts


def theta_char(ca, cb, tau):
    I = IU()
    k0 = int(mp.floor(ca + M(1, 2)))
    ca0 = ca - k0
    tol = POW10(-(mp.mp.dps + 8))
    s = mp.mpc(0)
    n = 0
    while True:
        if n == 0:
            nc = ca0
            t = mp.exp(I * mp.pi * tau * (nc * nc) + 2 * I * mp.pi * nc * cb)
            s += t
        else:
            nc1 = n + ca0
            nc2 = -n + ca0
            t1 = mp.exp(I * mp.pi * tau * (nc1 * nc1) + 2 * I * mp.pi * nc1 * cb)
            t2 = mp.exp(I * mp.pi * tau * (nc2 * nc2) + 2 * I * mp.pi * nc2 * cb)
            s += t1 + t2
            if abs(t1) < tol and abs(t2) < tol and n > 3:
                break
        n += 1
        if n > 200:
            break
    return s


def theta1_dlog(z, tau):
    """Exact d/dz ln theta_1(pi*z, tau) = pi * theta_1'(pi*z)/theta_1(pi*z)."""
    I = IU()
    y = mp.im(tau)
    m = mp.nint(mp.im(z) / y)
    z_red = z - m * tau
    n = mp.nint(mp.re(z_red))
    z_red = z_red - n
    v = mp.pi * z_red
    q = mp.exp(2 * I * mp.pi * tau)
    tol = POW10(-(mp.mp.dps + 8))
    s0 = mp.mpc(0)
    s1 = mp.mpc(0)
    k = 0
    while True:
        sgn = -1 if (k % 2 == 1) else 1
        qn = sgn * (q ** ((k * (k + 1)) // 2))
        mo = 2 * k + 1
        t0 = qn * mp.sin(mo * v)
        s0 += t0
        s1 += qn * mo * mp.cos(mo * v)
        if abs(t0) < tol and k > 2:
            break
        k += 1
        if k > 400:
            break
    return mp.pi * (s1 / s0) - 2 * mp.pi * I * m


def Fu_kronecker(al, be, tau):
    """Regularized Kronecker/digamma sum F_u(alpha, beta; tau)."""
    I = IU()
    x = mp.re(tau)
    y = mp.im(tau)
    al = al - mp.floor(al)
    be = be - mp.floor(be)
    tol = POW10(-(mp.mp.dps + 8))
    if abs(al) < POW10(-25):
        s = mp.pi * (2 * mp.euler - 2 * mp.log(2) - mp.log(y)) + (mp.pi ** 2 * y) / (
            mp.sin(mp.pi * be) ** 2
        )
        k = 1
        while True:
            w1 = mp.exp(-2 * mp.pi * k * y + 2 * mp.pi * I * (k * x + be))
            w2 = mp.exp(-2 * mp.pi * k * y + 2 * mp.pi * I * (-k * x + be))
            t = (2 * mp.pi / k) * (mp.re(w1 / (1 - w1)) + mp.re(w2 / (1 - w2)))
            s += t
            if abs(t) < tol and k > 4:
                break
            k += 1
            if k > 500:
                break
        return s
    else:
        s = -mp.pi * (2 * mp.log(2) + mp.log(y) + mp.psi(0, al) + mp.psi(0, 1 - al))
        # k = 0 term
        w0 = mp.exp(-2 * mp.pi * al * y + 2 * mp.pi * I * (al * x + be))
        s += (2 * mp.pi / al) * mp.re(w0 / (1 - w0))
        k = 1
        while True:
            ak1 = al + k
            ak2 = al - k
            w1 = mp.exp(-2 * mp.pi * abs(ak1) * y + 2 * mp.pi * I * (ak1 * x + be))
            w2 = mp.exp(-2 * mp.pi * abs(ak2) * y + 2 * mp.pi * I * (ak2 * x + be))
            t1 = (2 * mp.pi / abs(ak1)) * mp.re(w1 / (1 - w1))
            t2 = (2 * mp.pi / abs(ak2)) * mp.re(w2 / (1 - w2))
            s += t1 + t2
            if abs(t1) < tol and abs(t2) < tol and k > 4:
                break
            k += 1
            if k > 500:
                break
        return s


def eig_herm3_realsplit(H):
    """
    Disjoint Hermitian 3x3 eigendecomposition via 6x6 real-split symmetric mp.eigsy:
        R = [[Re H, -Im H], [Im H, Re H]].
    Returns (sorted_evals[3], unitary_U[3x3]) with H * U = U * diag(evals).
    """
    I = IU()
    R = mp.matrix(6, 6)
    for r in range(3):
        for c in range(3):
            re_v = mp.re(H[r, c])
            im_v = mp.im(H[r, c])
            R[r, c] = re_v
            R[r + 3, c + 3] = re_v
            R[r, c + 3] = -im_v
            R[r + 3, c] = im_v
    evals, evecs = mp.eigsy(R)
    idx = sorted(range(6), key=lambda k: evals[k])
    vals = []
    vecs = []
    for pair in ((idx[0], idx[1]), (idx[2], idx[3]), (idx[4], idx[5])):
        vals.append(evals[pair[0]])
        picked = None
        for k in pair:
            v = [evecs[r, k] + I * evecs[r + 3, k] for r in range(3)]
            for vp in vecs:
                proj = sum(mp.conj(vp[r]) * v[r] for r in range(3))
                v = [v[r] - proj * vp[r] for r in range(3)]
            nrm = mp.sqrt(sum(abs(z) ** 2 for z in v))
            if nrm > POW10(-8):
                picked = [z / nrm for z in v]
                break
        vecs.append(picked)
    U = mp.matrix(3, 3)
    for c in range(3):
        for r in range(3):
            U[r, c] = vecs[c][r]
    return vals, U


def eigvals_herm3_realsplit(H):
    """Fast eigenvalue-only 6x6 real-split symmetric mp.eigsy."""
    R = mp.matrix(6, 6)
    for r in range(3):
        for c in range(3):
            re_v = mp.re(H[r, c])
            im_v = mp.im(H[r, c])
            R[r, c] = re_v
            R[r + 3, c + 3] = re_v
            R[r, c + 3] = -im_v
            R[r + 3, c] = im_v
    evals = mp.eigsy(R, eigvals_only=True)
    ev = sorted([evals[k] for k in range(6)])
    return [ev[0], ev[2], ev[4]]


def takagi_3x3_realsplit(K):
    """
    Disjoint Autonne-Takagi decomposition K = U * diag(s1, s2, s3) * U^T
    for complex symmetric 3x3 K = A + i B via 6x6 real-symmetric mp.eigsy on
        M = [[A, B], [B, -A]].
    Positive-eigenvalue eigenvectors (x, y) give v = x + i y satisfying K v* = s v!
    """
    I = IU()
    Ks = (K + K.T) / 2
    M6 = mp.matrix(6, 6)
    for r in range(3):
        for c in range(3):
            a_rc = mp.re(Ks[r, c])
            b_rc = mp.im(Ks[r, c])
            M6[r, c] = a_rc
            M6[r, c + 3] = b_rc
            M6[r + 3, c] = b_rc
            M6[r + 3, c + 3] = -a_rc
    evals, evecs = mp.eigsy(M6)
    # Sort ascending: indices 3, 4, 5 are the 3 non-negative singular values s1 <= s2 <= s3!
    idx = sorted(range(6), key=lambda k: evals[k])
    pos_idx = idx[3:]
    svals = [max(mp.mpf(0), evals[k]) for k in pos_idx]
    vecs = []
    for k in pos_idx:
        v = [evecs[r, k] + I * evecs[r + 3, k] for r in range(3)]
        # Re-orthogonalize in C^3 in case of exact/near degeneracy (e.g. RPF4 K = I_3!)
        for vp in vecs:
            proj = sum(mp.conj(vp[r]) * v[r] for r in range(3))
            v = [v[r] - proj * vp[r] for r in range(3)]
        nrm = mp.sqrt(sum(abs(z) ** 2 for z in v))
        if nrm < POW10(-10):
            # Fallback orthogonal vector in C^3
            for basis_i in range(3):
                cand = [mp.mpc(1) if r == basis_i else mp.mpc(0) for r in range(3)]
                for vp in vecs:
                    proj = sum(mp.conj(vp[r]) * cand[r] for r in range(3))
                    cand = [cand[r] - proj * vp[r] for r in range(3)]
                nrm = mp.sqrt(sum(abs(z) ** 2 for z in cand))
                if nrm > POW10(-5):
                    v = cand
                    break
        v = [z / nrm for z in v]
        vecs.append(v)
    U = mp.matrix(3, 3)
    for c in range(3):
        for r in range(3):
            U[r, c] = vecs[c][r]
    return svals, U


def get_S_vec_tau(tau):
    I = IU()
    eta, _ = eta_and_E2_pentagonal(tau)
    t2 = theta_char(M(1, 2), M(0), tau)
    t3 = theta_char(M(0), M(0), tau)
    t4 = theta_char(M(0), M(1, 2), tau)
    c0 = -(t2 ** 2) * (t3 ** 4 + t4 ** 4) / (24 * (eta ** 3))
    c1 = (t4 ** 2) * (t2 ** 4 + t3 ** 4) / (24 * (eta ** 3))
    c2 = I * (t3 ** 2) * (t2 ** 4 - t4 ** 4) / (24 * (eta ** 3))
    return [c0, c1, c2], eta


def eval_frameC_all288(tau, L2_val, T_qs, pts):
    """Evaluate all-288 level-30 fermion potentials Tr2, V4, V_CW(1), V_CW^(tr)."""
    I = IU()
    y = mp.im(tau)
    S_vec, eta = get_S_vec_tau(tau)
    denom_R = 2 * mp.pi * (eta ** 3)

    # Pre-contract S(tau) with T_qs -> 4 matrices T_S[s_name]
    T_S = {}
    for nm in ("1", "i", "j", "k"):
        T_S[nm] = S_vec[0] * T_qs[0][nm] + S_vec[1] * T_qs[1][nm] + S_vec[2] * T_qs[2][nm]

    th_cache = {}
    wt_cache = {}

    def get_th(na, nb):
        # theta[ca, cb + m] = exp(2*pi*i*ca*m) * theta[ca, cb]
        na_m = na % 60
        nb_m = nb % 60
        shift_b = (nb - nb_m) // 60
        key = (na_m, nb_m)
        if key not in th_cache:
            th_cache[key] = theta_char(M(na_m, 60), M(nb_m, 60), tau)
        val = th_cache[key]
        if shift_b != 0 and na_m != 0:
            val = val * mp.exp(2 * I * mp.pi * M(na_m * shift_b, 60))
        return val

    def get_wt(na, nb):
        aa = (na - 30) % 60
        bb = (nb - 30) % 60
        key = (aa, bb)
        if key not in wt_cache:
            if aa == 0 and bb == 0:
                wt_cache[key] = mp.mpf(0)
            else:
                al = M(aa, 60)
                be = M(bb, 60)
                fu = Fu_kronecker(al, be, tau)
                a0 = 2 * mp.pi * I * al + theta1_dlog(al * tau + be, tau)
                c_val = (
                    fu
                    + mp.pi * mp.log(y)
                    - 2 * mp.pi * (mp.euler + mp.log(mp.pi))
                    - mp.pi * (abs(a0) ** 2) * mp.exp(-2 * L2_val)
                )
                val = 2 * mp.pi * L2_val + c_val
                wt_cache[key] = mp.sqrt(val) if val > 0 else mp.mpf(0)
        return wt_cache[key]

    sectors = [("u", 1, -4, 3), ("d", 1, 2, 3), ("e", -3, 6, 1)]
    Tr2 = mp.mpf(0)
    V4 = mp.mpf(0)
    VCW1 = mp.mpf(0)
    lams_all = []
    inv_64pi2 = M(1) / (64 * mp.pi ** 2)

    for (a_int, b_int) in pts:
        for (_, qL, qR, Nc) in sectors:
            x0_60 = 2 * qL * a_int
            y0_60 = 2 * qR * a_int
            ap_60 = x0_60 + y0_60
            am_60 = x0_60 - y0_60
            bp_60 = 2 * (qL + qR) * b_int
            bm_60 = 2 * (qL - qR) * b_int
            ef = mp.exp(-2 * I * mp.pi * M(x0_60, 60))
            kappas = {"1": -I * ef, "i": mp.mpc(-1), "j": -ef, "k": I}
            cs_list = [
                ("1", ap_60 + 30, bp_60 + 30, am_60 + 30, bm_60 + 30),
                ("i", ap_60 + 30, bp_60, am_60 + 30, bm_60),
                ("j", ap_60, bp_60 + 30, am_60, bm_60 + 30),
                ("k", ap_60, bp_60, am_60, bm_60),
            ]
            Y = mp.matrix(3, 3)
            for (nm, ca, cb, da, db) in cs_list:
                if (ca % 60 == 30 and cb % 60 == 30) or (da % 60 == 30 and db % 60 == 30):
                    continue
                Rs = kappas[nm] * get_th(ca, cb) * get_th(da, db) / denom_R
                wt = get_wt(ca, cb)
                coeff = wt * Rs
                if coeff != 0:
                    Y += coeff * T_S[nm]
            H = y * (Y.T.conjugate() * Y)
            evs = eigvals_herm3_realsplit(H)
            for lam in evs:
                if lam < 0:
                    lam = mp.mpf(0)
                Tr2 += Nc * lam
                V4 -= Nc * (lam * lam)
                if lam > 0:
                    VCW1 -= Nc * (lam * lam) * (mp.log(lam) - M(3, 2)) * inv_64pi2
                lams_all.append((Nc, lam))

    VCW_tr = mp.mpf(0)
    for (Nc, lam) in lams_all:
        if lam > 0:
            VCW_tr -= Nc * (lam * lam) * (mp.log(lam / Tr2) - M(3, 2)) * inv_64pi2
    return {"Tr2": Tr2, "V4": V4, "VCW1": VCW1, "VCW_tr": VCW_tr}


def eval_mark_basis(a_int, b_int, tau, L2_val, T_qs):
    """Build weight-0 Y_bas[sec][q_idx] at a single mark (a_int/30, b_int/30) for u, d, e, nu."""
    I = IU()
    y = mp.im(tau)
    S_vec, eta = get_S_vec_tau(tau)
    denom_R = 2 * mp.pi * (eta ** 3)
    sq_y = mp.sqrt(y)

    Y_bas = {}
    for sec, qL, qR in [("u", 1, -4), ("d", 1, 2), ("e", -3, 6), ("nu", -3, 0)]:
        x0_60 = 2 * qL * a_int
        y0_60 = 2 * qR * a_int
        ap_60 = x0_60 + y0_60
        am_60 = x0_60 - y0_60
        bp_60 = 2 * (qL + qR) * b_int
        bm_60 = 2 * (qL - qR) * b_int
        ef = mp.exp(-2 * I * mp.pi * M(x0_60, 60))
        kappas = {"1": -I * ef, "i": mp.mpc(-1), "j": -ef, "k": I}
        cs_list = [
            ("1", ap_60 + 30, bp_60 + 30, am_60 + 30, bm_60 + 30),
            ("i", ap_60 + 30, bp_60, am_60 + 30, bm_60),
            ("j", ap_60, bp_60 + 30, am_60, bm_60 + 30),
            ("k", ap_60, bp_60, am_60, bm_60),
        ]
        comps = {}
        for (nm, ca, cb, da, db) in cs_list:
            if (ca % 60 == 30 and cb % 60 == 30) or (da % 60 == 30 and db % 60 == 30):
                comps[nm] = mp.mpc(0)
                continue
            th1 = theta_char(M(ca, 60), M(cb, 60), tau)
            th2 = theta_char(M(da, 60), M(db, 60), tau)
            Rs = kappas[nm] * th1 * th2 / denom_R
            aa = (ca - 30) % 60
            bb = (cb - 30) % 60
            if aa == 0 and bb == 0:
                wt = mp.mpf(0)
            else:
                al = M(aa, 60)
                be = M(bb, 60)
                fu = Fu_kronecker(al, be, tau)
                a0 = 2 * mp.pi * I * al + theta1_dlog(al * tau + be, tau)
                c_val = (
                    fu
                    + mp.pi * mp.log(y)
                    - 2 * mp.pi * (mp.euler + mp.log(mp.pi))
                    - mp.pi * (abs(a0) ** 2) * mp.exp(-2 * L2_val)
                )
                val = 2 * mp.pi * L2_val + c_val
                wt = mp.sqrt(val) if val > 0 else mp.mpf(0)
            comps[nm] = sq_y * wt * Rs
        Y_bas[sec] = [
            sum(comps[nm] * T_qs[qi][nm] for nm in ("1", "i", "j", "k")) for qi in range(3)
        ]
    return Y_bas, S_vec


# ---------------------------------------------------------------------------
# Module RP2 — Full Fundamental-Domain Boson + Fermion Phase Diagram
# ---------------------------------------------------------------------------

def run_RP2(T_qs, pts, rp1_cache):
    t0_ns = time.monotonic_ns()
    I = IU()
    mp.mp.dps = 30
    fuch_cache = {}
    all288_cache = {}

    def get_point(tau, hi_prec=False):
        key = (fmt_r(mp.re(tau), 18), fmt_r(mp.im(tau), 18), bool(hi_prec))
        if key not in all288_cache:
            old_dps = mp.mp.dps
            mp.mp.dps = 45 if hi_prec else 28
            tau_w = mp.mpc(tau)
            fres = solve_fuchsian_L2(tau_w, hi_prec=hi_prec)
            fuch_cache[key] = fres
            a288 = eval_frameC_all288(tau_w, fres["L2"], T_qs, pts)
            all288_cache[key] = (fres, a288)
            mp.mp.dps = old_dps
        return all288_cache[key]

    # 1. Exact T and S invariance at tau_mod = 1/4 + 6/5 i (< 1e-25)
    mp.mp.dps = 45
    tau_mod = M(1, 4) + I * M(6, 5)
    f0, a0 = get_point(tau_mod, hi_prec=True)
    fT, aT = get_point(tau_mod + 1, hi_prec=True)
    fS, aS = get_point(-1 / tau_mod, hi_prec=True)
    L2_T_err = abs(fT["L2"] - f0["L2"])
    L2_S_err = abs(fS["L2"] - (f0["L2"] + mp.log(abs(tau_mod))))
    ts_fermion = {
        "L2_T_err": fmt_r(L2_T_err, 10),
        "L2_S_err": fmt_r(L2_S_err, 10),
    }
    ts_fermion_ok = bool(L2_T_err < POW10(-25) and L2_S_err < POW10(-25))
    for kname in ("Tr2", "V4", "VCW1", "VCW_tr"):
        eT = abs(aT[kname] - a0[kname]) / (abs(a0[kname]) + 1)
        eS = abs(aS[kname] - a0[kname]) / (abs(a0[kname]) + 1)
        ok = bool(eT < POW10(-25) and eS < POW10(-25))
        ts_fermion_ok = ts_fermion_ok and ok
        ts_fermion[kname] = {
            "val": fmt_r(a0[kname], 28),
            "T_rel_err": fmt_r(eT, 10),
            "S_rel_err": fmt_r(eS, 10),
            "pass": ok,
        }

    # 2. Orbifolds & arc (P2-A & P2-B)
    mp.mp.dps = 30
    tau_w = M(1, 2) + I * mp.sqrt(3) / 2
    tau_arc = mp.exp(I * 5 * mp.pi / 12)
    tau_i = I
    fw, aw = get_point(tau_w, hi_prec=False)
    fa, aa = get_point(tau_arc, hi_prec=False)
    fi, ai = get_point(tau_i, hi_prec=False)
    f2i, a2i = get_point(2 * I, hi_prec=False)
    f4i, a4i = get_point(4 * I, hi_prec=False)
    f_h4i, a_h4i = get_point(M(1, 2) + 4 * I, hi_prec=False)
    f_h5i, a_h5i = get_point(M(1, 2) + 5 * I, hi_prec=False)

    E3_i = E_chowla_selberg(tau_i, 3)
    E3_w = E_chowla_selberg(tau_w, 3)
    E3_4i = E_chowla_selberg(4 * I, 3)
    cB_crit = (aw["VCW1"] - ai["VCW1"]) / (E3_i - E3_w)
    casimir_4i = a4i["VCW1"] + 100 * E3_4i

    p2a_ok = bool(
        ai["VCW_tr"] > 0
        and aw["VCW_tr"] > 0
        and aa["VCW_tr"] > 0
        and ai["VCW_tr"] < aw["VCW_tr"] < aa["VCW_tr"]
        and aa["VCW_tr"] < a2i["VCW_tr"] < a4i["VCW_tr"]
        and aa["V4"] < min(ai["V4"], aw["V4"])
    )
    p2b_ok = bool(cB_crit > 0 and casimir_4i < -POW10(8))

    # 3. P2-C: Coupled potential V_tot(tau; c_F) = V_{FILQ, 3}(tau) + c_F * V_CW^(all-288)(1; tau)
    def V_tot(tau, cF):
        _, a288 = get_point(tau, hi_prec=False)
        return V_FILQ(tau, 3) + cF * a288["VCW1"]

    # Coarse scan along x = 1/2 to bracket minimum cleanly (Guardrail 1: no baked-in y*!)
    scan_half = {}
    y_grid_num = [1, M(3, 2), 2, M(5, 2), 3, M(7, 2), 4]
    y_vals_70 = []
    for yg in y_grid_num:
        t_pt = M(1, 2) + I * yg
        _, a_pt = get_point(t_pt, hi_prec=False)
        vf3 = V_FILQ(t_pt, 3)
        vt70 = vf3 + 70 * a_pt["VCW1"]
        y_vals_70.append((yg, vt70))
        scan_half[fmt_r(yg, 6)] = {
            "V_FILQ3": fmt_r(vf3, 18),
            "VCW1": fmt_r(a_pt["VCW1"], 18),
            "VCW_tr": fmt_r(a_pt["VCW_tr"], 18),
            "V_tot_70": fmt_r(vt70, 18),
        }

    # Find bracket around lowest grid point on x = 1/2
    best_idx = min(range(len(y_vals_70)), key=lambda idx: y_vals_70[idx][1])
    y_lo = y_vals_70[max(0, best_idx - 1)][0]
    y_hi = y_vals_70[min(len(y_vals_70) - 1, best_idx + 1)][0]

    # Golden-section bracket shrink (5 steps -> width ~ 0.1) + rapid 1D Newton polish on x = 1/2
    phi_inv = (mp.sqrt(5) - 1) / 2
    a_b, b_b = y_lo, y_hi
    c_b = b_b - phi_inv * (b_b - a_b)
    d_b = a_b + phi_inv * (b_b - a_b)
    fc_b = V_tot(M(1, 2) + I * c_b, 70)
    fd_b = V_tot(M(1, 2) + I * d_b, 70)
    for _ in range(5):
        if fc_b < fd_b:
            b_b = d_b
            d_b = c_b
            fd_b = fc_b
            c_b = b_b - phi_inv * (b_b - a_b)
            fc_b = V_tot(M(1, 2) + I * c_b, 70)
        else:
            a_b = c_b
            c_b = d_b
            fc_b = fd_b
            d_b = a_b + phi_inv * (b_b - a_b)
            fd_b = V_tot(M(1, 2) + I * d_b, 70)
    y_cur = (a_b + b_b) / 2

    # 1D Newton polish on dV/dy = 0 along x = 1/2 with fine step hy_fd = 10^-6
    hy_fd = POW10(-6)
    for _ in range(6):
        v0 = V_tot(M(1, 2) + I * y_cur, 70)
        vp = V_tot(M(1, 2) + I * (y_cur + hy_fd), 70)
        vm = V_tot(M(1, 2) + I * (y_cur - hy_fd), 70)
        gy_c = (vp - vm) / (2 * hy_fd)
        hyy_c = (vp - 2 * v0 + vm) / (hy_fd * hy_fd)
        dy = -gy_c / hyy_c
        # Clamp single step to stay inside bracket
        if abs(dy) > M(1, 5):
            dy = M(1, 5) if dy > 0 else M(-1, 5)
        y_cur = y_cur + dy
        if abs(dy) < POW10(-9):
            break
    y_star = y_cur
    tau_tot_star = M(1, 2) + I * y_star

    # 2D gradient, Hessian, and T-reflection check at (1/2, y_star) with h_x = 1/50, h_y = 10^-6
    hx = M(1, 50)
    hy = POW10(-6)
    f_star, a_star = get_point(tau_tot_star, hi_prec=False)
    V_star = V_FILQ(tau_tot_star, 3) + 70 * a_star["VCW1"]

    f_xp, a_xp = get_point(M(1, 2) + hx + I * y_star, hi_prec=False)
    f_xm, a_xm = get_point(M(1, 2) - hx + I * y_star, hi_prec=False)
    V_xp = V_FILQ(M(1, 2) + hx + I * y_star, 3) + 70 * a_xp["VCW1"]
    V_xm = V_FILQ(M(1, 2) - hx + I * y_star, 3) + 70 * a_xm["VCW1"]
    T_refl_L2_err = abs(f_xp["L2"] - f_xm["L2"])
    gx_half = (V_xp - V_xm) / (2 * hx)
    Vxx_half = (V_xp - 2 * V_star + V_xm) / (hx * hx)

    V_yp = V_tot(M(1, 2) + I * (y_star + hy), 70)
    V_ym = V_tot(M(1, 2) + I * (y_star - hy), 70)
    gy_half = (V_yp - V_ym) / (2 * hy)
    Vyy_half = (V_yp - 2 * V_star + V_ym) / (hy * hy)

    # Compare against (0, y_star) saddle!
    V_0y = V_tot(I * y_star, 70)
    V_0y_xp = V_tot(hx + I * y_star, 70)
    V_0y_xm = V_tot(-hx + I * y_star, 70)
    Vxx_zero = (V_0y_xp - 2 * V_0y + V_0y_xm) / (hx * hx)

    # Check V_tot(tau_FILQ3*; 70), V_tot(1/2 + 4i; 70), c_F^crit, and c_F = 100 well!
    tau_filq3 = I * rp1_cache["y_filq3"]
    _, a_f3 = get_point(tau_filq3, hi_prec=False)
    Vf3_at_f3 = V_FILQ(tau_filq3, 3)
    V_tot_at_f3_70 = Vf3_at_f3 + 70 * a_f3["VCW1"]
    # First-order c_F^crit where V_tot(1/2 + i y*; c_F) == V_tot(tau_FILQ3*; c_F)
    cF_crit_est = (V_FILQ(tau_tot_star, 3) - Vf3_at_f3) / (a_f3["VCW1"] - a_star["VCW1"])

    V_tot_h4i_70 = V_FILQ(M(1, 2) + 4 * I, 3) + 70 * a_h4i["VCW1"]
    V_tot_h4i_100 = V_FILQ(M(1, 2) + 4 * I, 3) + 100 * a_h4i["VCW1"]
    V_tot_h5i_100 = V_FILQ(M(1, 2) + 5 * I, 3) + 100 * a_h5i["VCW1"]

    p2c_ok = bool(
        T_refl_L2_err < POW10(-12)
        and abs(gx_half) < POW10(-4)
        and abs(gy_half) / (abs(Vyy_half) + 1) < POW10(-8)
        and Vxx_half > 0
        and Vyy_half > 0
        and Vxx_zero < 0
        and V_star < V_0y
        and V_star < -6 * POW10(6)
        and V_tot_at_f3_70 > 0
        and V_tot_h4i_70 > 4 * POW10(9)
        and V_tot_h4i_100 < 0
        and V_tot_h5i_100 > POW10(12)
    )

    out = {
        "ts_invariance_all288": ts_fermion,
        "ts_invariance_pass": ts_fermion_ok,
        "orbifolds_and_cusp": {
            "omega": {k: fmt_r(v, 20) for k, v in aw.items()} | {"L2": fmt_r(fw["L2"], 22)},
            "arc_5pi12": {k: fmt_r(v, 20) for k, v in aa.items()} | {"L2": fmt_r(fa["L2"], 22)},
            "i": {k: fmt_r(v, 20) for k, v in ai.items()} | {"L2": fmt_r(fi["L2"], 22)},
            "2i": {k: fmt_r(v, 20) for k, v in a2i.items()} | {"L2": fmt_r(f2i["L2"], 22)},
            "4i": {k: fmt_r(v, 20) for k, v in a4i.items()} | {"L2": fmt_r(f4i["L2"], 22)},
        },
        "P2_A_trace_scale": {
            "pass": p2a_ok,
            "VCW_tr_i": fmt_r(ai["VCW_tr"], 20),
            "VCW_tr_omega": fmt_r(aw["VCW_tr"], 20),
            "VCW_tr_arc": fmt_r(aa["VCW_tr"], 20),
            "V4_arc_below_orbifolds": bool(aa["V4"] < min(ai["V4"], aw["V4"])),
        },
        "P2_B_casimir_nogo": {
            "pass": p2b_ok,
            "cB_crit": fmt_r(cB_crit, 20),
            "VCW1_plus_100E3_at_4i": fmt_r(casimir_4i, 20),
        },
        "P2_C_coupled_vacuum": {
            "pass": p2c_ok,
            "scan_x_half": scan_half,
            "y_star": fmt_r(y_star, 20),
            "L2_star": fmt_r(f_star["L2"], 22),
            "c_acc_star": fmt_c(f_star["c"], 20),
            "V_star": fmt_r(V_star, 20),
            "g_x_half": fmt_r(gx_half, 12),
            "g_y_half": fmt_r(gy_half, 12),
            "V_xx_half": fmt_r(Vxx_half, 20),
            "V_yy_half": fmt_r(Vyy_half, 20),
            "T_refl_L2_err": fmt_r(T_refl_L2_err, 10),
            "V_at_0_ystar": fmt_r(V_0y, 20),
            "V_xx_zero": fmt_r(Vxx_zero, 20),
            "V_tot_at_FILQ3_star_70": fmt_r(V_tot_at_f3_70, 20),
            "cF_crit_est": fmt_r(cF_crit_est, 15),
            "V_tot_half_4i_70": fmt_r(V_tot_h4i_70, 20),
            "V_tot_half_4i_100": fmt_r(V_tot_h4i_100, 20),
            "V_tot_half_5i_100": fmt_r(V_tot_h5i_100, 20),
        },
        "elapsed_sec": elapsed_sec_str(t0_ns),
    }
    cache = {
        "tau_w": tau_w,
        "f_w": fw,
        "tau_tot_star": tau_tot_star,
        "f_tot_star": f_star,
        "a_h4i": a_h4i,
    }
    return out, cache


# ---------------------------------------------------------------------------
# Curved Spin-1/2 Dirac Kahler Metric G_{s=1/2} (Corner-Split CC Polar Quad)
# ---------------------------------------------------------------------------

def cc_nodes_weights(N):
    xs = [mp.cos(k * mp.pi / N) for k in range(N + 1)]
    ws = []
    for k in range(N + 1):
        c_k = mp.mpf(1) if (k == 0 or k == N) else mp.mpf(2)
        s = mp.mpf(0)
        for j in range(1, N // 2 + 1):
            b_j = mp.mpf(1) if (2 * j == N) else mp.mpf(2)
            s += b_j * mp.cos(2 * j * k * mp.pi / N) / (4 * j * j - 1)
        ws.append((c_k / N) * (1 - s))
    return list(reversed(xs)), list(reversed(ws))


def theta_nu_z(nu, z, tau):
    I = IU()
    ca = M(1, 2) if nu == 2 else M(0)
    cb = M(1, 2) if nu == 4 else M(0)
    tol = POW10(-(mp.mp.dps + 6))
    s = mp.mpc(0)
    n = 0
    while True:
        if n == 0:
            nc = ca
            s += mp.exp(I * mp.pi * tau * (nc * nc) + 2 * I * mp.pi * nc * (z + cb))
        else:
            nc1 = n + ca
            nc2 = -n + ca
            t1 = mp.exp(I * mp.pi * tau * (nc1 * nc1) + 2 * I * mp.pi * nc1 * (z + cb))
            t2 = mp.exp(I * mp.pi * tau * (nc2 * nc2) + 2 * I * mp.pi * nc2 * (z + cb))
            s += t1 + t2
            if abs(t1) < tol and abs(t2) < tol and n > 3:
                break
        n += 1
        if n > 100:
            break
    return s


def compute_curved_dirac_G_s12(tau, f_sol):
    """
    Corner-split Clenshaw-Curtis polar quadrature + Forest-Ruth symplectic radial
    propagation for Gauss-Bonnet Area = int e^{2 phi} d^2 z and spin-1/2 Dirac
    Kahler metric G_j = int |psi_j(z)|^2 e^{+phi(z)} d^2 z, ordered as [QJ, QI, QK]
    = [theta_4, theta_2, theta_3].
    """
    I = IU()
    old_dps = mp.mp.dps
    mp.mp.dps = 26
    tau = mp.mpc(tau)
    x = mp.re(tau)
    y = mp.im(tau)
    _, E2_val = eta_and_E2_pentagonal(tau)
    c_acc = mp.mpc(f_sol["c"])
    A_val = mp.mpf(f_sol["A"])

    a_coef, b_coef, _ = frobenius_series_wp(tau, E2_val, c_acc, N_frob=14, M_pts=20)
    cbrt2 = mp.root(2, 3)
    d_FR = [1 / (2 - cbrt2), -cbrt2 / (2 - cbrt2), 1 / (2 - cbrt2)]

    def step_ray(z1, z2, v_mat, nsub=2):
        dz = (z2 - z1) / nsub
        u0, u1 = v_mat[0, 0], v_mat[0, 1]
        p0, p1 = v_mat[1, 0], v_mat[1, 1]
        z = z1
        for _ in range(nsub):
            for w in d_FR:
                h = w * dz
                h2 = h / 2
                u0 += h2 * p0
                u1 += h2 * p1
                V = wp_theta1(z + h2, tau, E2_val) / 4 + c_acc
                p0 -= h * V * u0
                p1 -= h * V * u1
                u0 += h2 * p0
                u1 += h2 * p1
                z += h
        return mp.matrix([[u0, u1], [p0, p1]])

    alpha1 = mp.arg(1 + tau)
    alpha2 = mp.arg(-1 + tau)
    if y > M(3, 2):
        segs = [(alpha2 - mp.pi, M(0)), (M(0), alpha1), (alpha1, alpha2)]
        N_th_seg = 10
        N_r = 22
        eps_z = M(1, 40)
    else:
        segs = [(alpha2 - mp.pi, alpha1), (alpha1, alpha2)]
        N_th_seg = 12
        N_r = 20
        eps_z = M(1, 30)

    xs_th, ws_th = cc_nodes_weights(N_th_seg)
    xs_r, ws_r = cc_nodes_weights(N_r)

    # Exact analytic inner disk |z| < eps_z
    t_in = A_val / 2 - mp.log(eps_z)
    Area_tot = 2 * mp.pi / t_in
    rad_in = 2 * mp.pi * mp.exp(A_val / 2) * mp.e1(t_in)
    G_tot = {nu: (abs(theta_nu_z(nu, mp.mpc(0), tau)) ** 2) * rad_in for nu in (4, 2, 3)}

    for (a_lo, a_hi) in segs:
        mid_a = (a_lo + a_hi) / 2
        half_da = (a_hi - a_lo) / 2
        for j in range(N_th_seg + 1):
            alpha = mid_a + half_da * xs_th[j]
            w_th = half_da * ws_th[j]
            ca = mp.cos(alpha)
            sa = mp.sin(alpha)
            eia = ca + I * sa
            R_max = M(1) / (2 * max(abs(sa / y), abs(ca - (x / y) * sa)))
            s_min = mp.log(eps_z)
            s_max = mp.log(R_max)
            half_ds = (s_max - s_min) / 2
            mid_s = (s_max + s_min) / 2
            zs = eps_z * eia
            v_mat = eval_frobenius_W(zs, a_coef, b_coef)
            z_prev = zs
            for k in range(N_r + 1):
                rho_k = mp.exp(mid_s + half_ds * xs_r[k])
                z_k = rho_k * eia
                if k > 0:
                    v_mat = step_ray(z_prev, z_k, v_mat, nsub=2)
                    z_prev = z_k
                u_r = v_mat[0, 0]
                u_l = v_mat[0, 1]
                ephi = 2 / (A_val * (abs(u_r) ** 2) - 2 * mp.re(mp.conj(u_r) * u_l))
                w_meas = 2 * w_th * half_ds * ws_r[k] * (rho_k * rho_k)
                Area_tot += w_meas * (ephi * ephi)
                gauss = mp.exp(-2 * mp.pi * (mp.im(z_k) ** 2) / y)
                for nu in (4, 2, 3):
                    G_tot[nu] += w_meas * gauss * (abs(theta_nu_z(nu, z_k, tau)) ** 2) * ephi

    gb_err = abs(Area_tot / (2 * mp.pi) - 1)
    G_raw = [G_tot[4], G_tot[2], G_tot[3]]
    mean_G = (G_raw[0] + G_raw[1] + G_raw[2]) / 3
    gmean_G = (G_raw[0] * G_raw[1] * G_raw[2]) ** M(1, 3)
    G_am = [v / mean_G for v in G_raw]
    G_gm = [v / gmean_G for v in G_raw]
    iso_err = max(abs(v - 1) for v in G_am)

    mp.mp.dps = old_dps
    return {
        "Area": Area_tot,
        "gb_err": gb_err,
        "G_raw": G_raw,
        "G_am": G_am,
        "G_gm": G_gm,
        "iso_err": iso_err,
    }


# ---------------------------------------------------------------------------
# 2-Loop Type-II 2HDM + 1-Loop D-Term Quartics + 3x3 Hermitian Soft-Mass RGEs
# ---------------------------------------------------------------------------

def mat_tr(A):
    return A[0, 0] + A[1, 1] + A[2, 2]


def mat_herm(A):
    return (A + A.T.conjugate()) / 2


def rge_rhs_2hdm_ii(state, include_lam_in_betaY=True, mode_1hdm=False):
    """
    Exact coupled 2-loop Type-II 2HDM Gauge + Yukawa (Chowdhury-Eberhardt 1503.08216 &
    Luo-Wang-Xiao hep-ph/0211440) + 1-loop Gauge-Higgs D-term quartics (lambda_1, lambda_2
    without 1/2 in V, so lam_CE = 2*lam_D) + 3x3 Hermitian Martin (hep-ph/9709356) soft-mass
    RGEs (M_a = A_0 = 0), with t = ln(mu / mu_UV).
    """
    g1, g2, g3, Yu, Yd, Ye, l1, l2, l3, l4, mHu2, mHd2, MQ2, Mu2, Md2, ML2, Me2 = state
    I3 = mp.eye(3)
    inv_16pi2 = M(1) / (16 * mp.pi ** 2)
    inv_16pi2_sq = inv_16pi2 * inv_16pi2

    g1s = g1 * g1
    g2s = g2 * g2
    g3s = g3 * g3
    gp2 = M(3, 5) * g1s  # g'^2 = (3/5) g1^2

    Hu = Yu * Yu.T.conjugate()
    Hd = Yd * Yd.T.conjugate()
    He = Ye * Ye.T.conjugate()
    Tu = mp.re(mat_tr(Hu))
    Td = mp.re(mat_tr(Hd))
    Te = mp.re(mat_tr(He))
    Tuu = mp.re(mat_tr(Hu * Hu))
    Tdd = mp.re(mat_tr(Hd * Hd))
    Tee = mp.re(mat_tr(He * He))
    Tud = mp.re(mat_tr(Hu * Hd))

    # CE convention quartics (V = (1/2) l1_ce |Phi1|^4 + (1/2) l2_ce |Phi2|^4 + ...)
    l1_ce = 2 * l1
    l2_ce = 2 * l2

    # 1. Gauge beta functions (1-loop + 2-loop)
    if mode_1hdm:
        b1, b2, b3 = M(41, 10), M(-19, 6), M(-7)
        B = [
            [M(199, 50), M(27, 10), M(44, 5)],
            [M(9, 10), M(35, 6), M(12)],
            [M(11, 10), M(9, 2), M(-26)],
        ]
    else:
        b1, b2, b3 = M(21, 5), M(-3), M(-7)
        B = [
            [M(104, 25), M(18, 5), M(44, 5)],
            [M(6, 5), M(8), M(12)],
            [M(11, 10), M(9, 2), M(-26)],
        ]
    dg1 = inv_16pi2 * (b1 * g1 ** 3) + inv_16pi2_sq * (g1 ** 3) * (
        B[0][0] * g1s + B[0][1] * g2s + B[0][2] * g3s - M(17, 10) * Tu - M(1, 2) * Td - M(3, 2) * Te
    )
    dg2 = inv_16pi2 * (b2 * g2 ** 3) + inv_16pi2_sq * (g2 ** 3) * (
        B[1][0] * g1s + B[1][1] * g2s + B[1][2] * g3s - M(3, 2) * Tu - M(3, 2) * Td - M(1, 2) * Te
    )
    dg3 = inv_16pi2 * (b3 * g3 ** 3) + inv_16pi2_sq * (g3 ** 3) * (
        B[2][0] * g1s + B[2][1] * g2s + B[2][2] * g3s - 2 * Tu - 2 * Td
    )

    # 2. Yukawa beta functions (1-loop + 2-loop)
    if mode_1hdm:
        # 1HDM (SM) 1-loop for Xing-Zhou sign benchmark
        bYu1 = (M(3, 2) * Hu - M(3, 2) * Hd + (3 * Tu + 3 * Td + Te - M(17, 20) * g1s - M(9, 4) * g2s - 8 * g3s) * I3) * Yu
        bYd1 = (M(3, 2) * Hd - M(3, 2) * Hu + (3 * Tu + 3 * Td + Te - M(1, 4) * g1s - M(9, 4) * g2s - 8 * g3s) * I3) * Yd
        bYe1 = (M(3, 2) * He + (3 * Tu + 3 * Td + Te - M(9, 4) * g1s - M(9, 4) * g2s) * I3) * Ye
        dYu = inv_16pi2 * bYu1
        dYd = inv_16pi2 * bYd1
        dYe = inv_16pi2 * bYe1
    else:
        # Type-II 2HDM 1-loop
        bYu1 = (M(3, 2) * Hu + M(1, 2) * Hd + (3 * Tu - M(17, 20) * g1s - M(9, 4) * g2s - 8 * g3s) * I3) * Yu
        bYd1 = (M(3, 2) * Hd + M(1, 2) * Hu + (3 * Td + Te - M(1, 4) * g1s - M(9, 4) * g2s - 8 * g3s) * I3) * Yd
        bYe1 = (M(3, 2) * He + (3 * Td + Te - M(9, 4) * g1s - M(9, 4) * g2s) * I3) * Ye

        # Type-II 2HDM 2-loop (exact Chowdhury-Eberhardt 1503.08216 + Luo-Wang-Xiao matrix order)
        g4_u = (
            M(1267, 600) * g1s * g1s
            - M(9, 20) * g1s * g2s
            + M(19, 15) * g1s * g3s
            - M(21, 4) * g2s * g2s
            + 9 * g2s * g3s
            - 108 * g3s * g3s
        )
        g4_d = (
            M(-113, 600) * g1s * g1s
            - M(27, 20) * g1s * g2s
            + M(31, 15) * g1s * g3s
            - M(21, 4) * g2s * g2s
            + 9 * g2s * g3s
            - 108 * g3s * g3s
        )
        g4_e = M(1449, 200) * g1s * g1s + M(27, 20) * g1s * g2s - M(21, 4) * g2s * g2s

        lam_u_sc = M(3, 2) * l2_ce * l2_ce + l3 * l3 + l3 * l4 + l4 * l4 if include_lam_in_betaY else M(0)
        lam_d_sc = M(3, 2) * l1_ce * l1_ce + l3 * l3 + l3 * l4 + l4 * l4 if include_lam_in_betaY else M(0)
        lam_Hu_u = -6 * l2_ce if include_lam_in_betaY else M(0)
        lam_Hd_u = (-2 * l3 + 2 * l4) if include_lam_in_betaY else M(0)
        lam_Hd_d = -6 * l1_ce if include_lam_in_betaY else M(0)
        lam_Hu_d = (-2 * l3 + 2 * l4) if include_lam_in_betaY else M(0)
        lam_He_e = -6 * l1_ce if include_lam_in_betaY else M(0)

        sc_u = (
            g4_u
            + lam_u_sc
            + (M(17, 8) * g1s + M(45, 8) * g2s + 20 * g3s) * Tu
            - M(27, 4) * Tuu
            - M(9, 4) * Tud
        )
        bYu2 = (
            M(3, 2) * (Hu * Hu)
            - M(1, 4) * (Hu * Hd)
            - M(1, 4) * (Hd * Hd)
            + (M(223, 80) * g1s + M(135, 16) * g2s + 16 * g3s - M(27, 4) * Tu + lam_Hu_u) * Hu
            + (M(-41, 240) * g1s + M(33, 16) * g2s + M(16, 3) * g3s - M(3, 4) * (3 * Td + Te) + lam_Hd_u) * Hd
            + sc_u * I3
        ) * Yu

        sc_d = (
            g4_d
            + lam_d_sc
            + (M(5, 8) * g1s + M(45, 8) * g2s + 20 * g3s) * Td
            + (M(15, 8) * g1s + M(15, 8) * g2s) * Te
            - M(27, 4) * Tdd
            - M(9, 4) * Tee
            - M(9, 4) * Tud
        )
        bYd2 = (
            M(3, 2) * (Hd * Hd)
            - M(1, 4) * (Hd * Hu)
            - M(1, 4) * (Hu * Hu)
            + (M(187, 80) * g1s + M(135, 16) * g2s + 16 * g3s - M(9, 4) * (3 * Td + Te) + lam_Hd_d) * Hd
            + (M(-53, 240) * g1s + M(33, 16) * g2s + M(16, 3) * g3s - M(9, 4) * Tu + lam_Hu_d) * Hu
            + sc_d * I3
        ) * Yd

        sc_e = (
            g4_e
            + lam_d_sc
            + (M(5, 8) * g1s + M(45, 8) * g2s + 20 * g3s) * Td
            + (M(15, 8) * g1s + M(15, 8) * g2s) * Te
            - M(27, 4) * Tdd
            - M(9, 4) * Tee
            - M(9, 4) * Tud
        )
        bYe2 = (
            M(3, 2) * (He * He)
            + (M(387, 80) * g1s + M(135, 16) * g2s - M(9, 4) * (3 * Td + Te) + lam_He_e) * He
            + sc_e * I3
        ) * Ye

        dYu = inv_16pi2 * bYu1 + inv_16pi2_sq * bYu2
        dYd = inv_16pi2 * bYd1 + inv_16pi2_sq * bYd2
        dYe = inv_16pi2 * bYe1 + inv_16pi2_sq * bYe2

    # 3. 1-loop 2HDM-II scalar quartics (l1 = l1_ce/2, l2 = l2_ce/2, l5 = 0)
    g4_diag = M(3, 4) * (3 * g2s * g2s + 2 * g2s * gp2 + gp2 * gp2)
    g4_l3 = M(3, 4) * (3 * g2s * g2s - 2 * g2s * gp2 + gp2 * gp2)
    g2_lin = 9 * g2s + 3 * gp2
    dl1_ce = (
        12 * l1_ce * l1_ce + 4 * l3 * l3 + 4 * l3 * l4 + 2 * l4 * l4
        + g4_diag - l1_ce * g2_lin + 4 * l1_ce * (3 * Td + Te) - 4 * (3 * Tdd + Tee)
    )
    dl2_ce = (
        12 * l2_ce * l2_ce + 4 * l3 * l3 + 4 * l3 * l4 + 2 * l4 * l4
        + g4_diag - l2_ce * g2_lin + 4 * l2_ce * (3 * Tu) - 4 * (3 * Tuu)
    )
    dl1 = inv_16pi2 * (dl1_ce / 2)
    dl2 = inv_16pi2 * (dl2_ce / 2)
    dl3 = inv_16pi2 * (
        (l1_ce + l2_ce) * (6 * l3 + 2 * l4) + 4 * l3 * l3 + 2 * l4 * l4
        + g4_l3 - l3 * g2_lin + 2 * l3 * (3 * Tu + 3 * Td + Te) - 12 * Tud
    )
    dl4 = inv_16pi2 * (
        2 * (l1_ce + l2_ce) * l4 + 8 * l3 * l4 + 4 * l4 * l4
        + 3 * g2s * gp2 - l4 * g2_lin + 2 * l4 * (3 * Tu + 3 * Td + Te) + 12 * Tud
    )

    # 4. 1-loop 3x3 Hermitian soft scalar mass RGEs (Martin hep-ph/9709356, M_a = A_0 = 0)
    S_tr = mHu2 - mHd2 + mp.re(mat_tr(MQ2 - ML2 - 2 * Mu2 + Md2 + Me2))
    YuH = Yu.T.conjugate()
    YdH = Yd.T.conjugate()
    YeH = Ye.T.conjugate()
    Hu_R = YuH * Yu
    Hd_R = YdH * Yd
    He_R = YeH * Ye

    dmHu2 = inv_16pi2 * (
        6 * mp.re(mat_tr((mHu2 * I3 + MQ2) * Hu + Yu * Mu2 * YuH)) + M(3, 5) * g1s * S_tr
    )
    dmHd2 = inv_16pi2 * (
        6 * mp.re(mat_tr((mHd2 * I3 + MQ2) * Hd + Yd * Md2 * YdH))
        + 2 * mp.re(mat_tr((mHd2 * I3 + ML2) * He + Ye * Me2 * YeH))
        - M(3, 5) * g1s * S_tr
    )
    dMQ2 = inv_16pi2 * mat_herm(
        (MQ2 + 2 * mHu2 * I3) * Hu + Hu * MQ2 + 2 * Yu * Mu2 * YuH
        + (MQ2 + 2 * mHd2 * I3) * Hd + Hd * MQ2 + 2 * Yd * Md2 * YdH
        + M(1, 5) * g1s * S_tr * I3
    )
    dMu2 = inv_16pi2 * mat_herm(
        2 * (Mu2 + 2 * mHu2 * I3) * Hu_R + 2 * Hu_R * Mu2 + 4 * YuH * MQ2 * Yu
        - M(4, 5) * g1s * S_tr * I3
    )
    dMd2 = inv_16pi2 * mat_herm(
        2 * (Md2 + 2 * mHd2 * I3) * Hd_R + 2 * Hd_R * Md2 + 4 * YdH * MQ2 * Yd
        + M(2, 5) * g1s * S_tr * I3
    )
    dML2 = inv_16pi2 * mat_herm(
        (ML2 + 2 * mHd2 * I3) * He + He * ML2 + 2 * Ye * Me2 * YeH
        - M(3, 5) * g1s * S_tr * I3
    )
    dMe2 = inv_16pi2 * mat_herm(
        2 * (Me2 + 2 * mHd2 * I3) * He_R + 2 * He_R * Me2 + 4 * YeH * ML2 * Ye
        + M(6, 5) * g1s * S_tr * I3
    )

    return (
        dg1, dg2, dg3, dYu, dYd, dYe, dl1, dl2, dl3, dl4,
        dmHu2, dmHd2, dMQ2, dMu2, dMd2, dML2, dMe2,
    )


def state_axpy(s0, a1, k1, a2=None, k2=None):
    if a2 is None:
        return tuple(s0[i] + a1 * k1[i] for i in range(len(s0)))
    return tuple(s0[i] + a1 * k1[i] + a2 * k2[i] for i in range(len(s0)))


def state_diff_norm(ka, kb):
    mx = mp.mpf(0)
    for x, y in zip(ka, kb):
        if isinstance(x, mp.matrix):
            for r in range(x.rows):
                for c in range(x.cols):
                    d = abs(x[r, c] - y[r, c])
                    if d > mx:
                        mx = d
        else:
            d = abs(x - y)
            if d > mx:
                mx = d
    return mx


def hermite_zero_crossing(t0, t1, f0, f1, d0, d1):
    """Exact cubic Hermite root in [t1, t0] (t1 < t0) when f0 > 0 >= f1."""
    dt = t1 - t0  # negative
    # u in [0, 1], t(u) = t0 + u*dt
    # H(u) = (2u^3 - 3u^2 + 1) f0 + (u^3 - 2u^2 + u) (dt*d0) + (-2u^3 + 3u^2) f1 + (u^3 - u^2) (dt*d1)
    m0 = dt * d0
    m1 = dt * d1

    def H(u):
        u2 = u * u
        u3 = u2 * u
        return (2 * u3 - 3 * u2 + 1) * f0 + (u3 - 2 * u2 + u) * m0 + (-2 * u3 + 3 * u2) * f1 + (u3 - u2) * m1

    lo, hi = mp.mpf(0), mp.mpf(1)
    for _ in range(50):
        mid = (lo + hi) / 2
        if H(mid) > 0:
            lo = mid
        else:
            hi = mid
    return t0 + ((lo + hi) / 2) * dt


def integrate_gl4(state0, t_end, n_steps, include_lam_in_betaY=True, mode_1hdm=False):
    """
    Disjoint 2-stage 4th-order Implicit Gauss-Legendre (GL4) ODE integrator (NOT RK4!).
    Tracks exact EWSB zero crossings t_EWSB^(u) and t_EWSB^(d) via cubic Hermite roots,
    and checks all 4 vacuum stability inequalities at every step.
    """
    s3_6 = mp.sqrt(3) / 6
    a11 = M(1, 4)
    a22 = M(1, 4)
    a12 = M(1, 4) - s3_6
    a21 = M(1, 4) + s3_6
    h = mp.mpf(t_end) / n_steps
    tol_fp = POW10(-(mp.mp.dps - 4))

    state = state0
    t_cur = mp.mpf(0)
    t_ewsb_u = None
    t_ewsb_d = None
    all_stab = True

    def check_stab(st):
        l1, l2, l3, l4 = st[6], st[7], st[8], st[9]
        if l1 <= 0 or l2 <= 0:
            return False
        s12 = 2 * mp.sqrt(l1 * l2)
        # At t = 0 exact D-term saturates l3 + l4 + 2*sqrt(l1*l2) = 0; allow -1e-25 roundoff
        return bool(l3 + s12 > -POW10(-25) and l3 + l4 + s12 > -POW10(-25))

    all_stab = all_stab and check_stab(state)

    for step in range(n_steps):
        k0 = rge_rhs_2hdm_ii(state, include_lam_in_betaY=include_lam_in_betaY, mode_1hdm=mode_1hdm)
        k1 = k0
        k2 = k0
        for _ in range(25):
            y1 = state_axpy(state, h * a11, k1, h * a12, k2)
            y2 = state_axpy(state, h * a21, k1, h * a22, k2)
            k1_n = rge_rhs_2hdm_ii(y1, include_lam_in_betaY=include_lam_in_betaY, mode_1hdm=mode_1hdm)
            k2_n = rge_rhs_2hdm_ii(y2, include_lam_in_betaY=include_lam_in_betaY, mode_1hdm=mode_1hdm)
            err = max(state_diff_norm(k1_n, k1), state_diff_norm(k2_n, k2))
            k1, k2 = k1_n, k2_n
            if err < tol_fp:
                break
        state_next = state_axpy(state, h / 2, k1, h / 2, k2)
        t_next = t_cur + h
        k_next = rge_rhs_2hdm_ii(state_next, include_lam_in_betaY=include_lam_in_betaY, mode_1hdm=mode_1hdm)

        # Check EWSB crossings
        if t_ewsb_u is None and state[10] > 0 and state_next[10] <= 0:
            t_ewsb_u = hermite_zero_crossing(t_cur, t_next, state[10], state_next[10], k0[10], k_next[10])
        if t_ewsb_d is None and state[11] > 0 and state_next[11] <= 0:
            t_ewsb_d = hermite_zero_crossing(t_cur, t_next, state[11], state_next[11], k0[11], k_next[11])

        state = state_next
        t_cur = t_next
        all_stab = all_stab and check_stab(state)

    return state, t_ewsb_u, t_ewsb_d, all_stab


def make_initial_state(Yu, Yd, Ye, soft_rots=None):
    g1 = M(1, 2)
    g2 = M(1, 2)
    g3 = M(1, 2)
    gp2 = M(3, 5) * g1 * g1
    l1 = (g2 * g2 + gp2) / 8
    l2 = l1
    l3 = (g2 * g2 - gp2) / 4
    l4 = -(g2 * g2) / 2
    I3 = mp.eye(3)
    MQ2 = I3
    Mu2 = I3
    Md2 = I3
    ML2 = I3
    Me2 = I3
    if soft_rots is not None:
        UQ, Uu, Ud, UL, Ue = soft_rots
        MQ2 = UQ * MQ2 * UQ.T.conjugate()
        Mu2 = Uu * Mu2 * Uu.T.conjugate()
        Md2 = Ud * Md2 * Ud.T.conjugate()
        ML2 = UL * ML2 * UL.T.conjugate()
        Me2 = Ue * Me2 * Ue.T.conjugate()
    return (g1, g2, g3, Yu, Yd, Ye, l1, l2, l3, l4, mp.mpf(1), mp.mpf(1), MQ2, Mu2, Md2, ML2, Me2)


def extract_piece2_observables(st, t_ewsb_u, t_ewsb_d, all_stab):
    g1, g2, g3, Yu, Yd, Ye, l1, l2, l3, l4, mHu2, mHd2, MQ2, Mu2, Md2, ML2, Me2 = st
    eu, Uu = eig_herm3_realsplit(Yu * Yu.T.conjugate())
    ed, Ud = eig_herm3_realsplit(Yd * Yd.T.conjugate())
    ee, Ue = eig_herm3_realsplit(Ye * Ye.T.conjugate())
    su = [mp.sqrt(max(mp.mpf(0), v)) for v in eu]
    sd = [mp.sqrt(max(mp.mpf(0), v)) for v in ed]
    se = [mp.sqrt(max(mp.mpf(0), v)) for v in ee]
    V = Uu.T.conjugate() * Ud
    V12 = abs(V[0, 1])
    V23 = abs(V[1, 2])
    V13 = abs(V[0, 2])
    Jcp = mp.im(V[0, 1] * V[1, 2] * mp.conj(V[0, 2]) * mp.conj(V[1, 1]))
    std_ckm = bool(V12 > V23 > V13)

    # Sfermion minimum squared mass & S-trace
    sf_eigs = []
    for Msf in (MQ2, Mu2, Md2, ML2, Me2):
        sf_eigs.extend(eigvals_herm3_realsplit(Msf))
    min_sf = min(sf_eigs)
    S_ir = mHu2 - mHd2 + mp.re(mat_tr(MQ2 - ML2 - 2 * Mu2 + Md2 + Me2))
    s12 = 2 * mp.sqrt(max(mp.mpf(0), l1 * l2))
    stab_ir = bool(l1 > 0 and l2 > 0 and (l3 + s12) > 0 and (l3 + l4 + s12) > 0)

    return {
        "g1": g1,
        "g2": g2,
        "g3": g3,
        "yt_over_g3": su[2] / g3,
        "mb_over_mtau": sd[2] / se[2] if se[2] > 0 else mp.mpf(0),
        "u23": su[1] / su[2] if su[2] > 0 else mp.mpf(0),
        "u13": su[0] / su[2] if su[2] > 0 else mp.mpf(0),
        "d23": sd[1] / sd[2] if sd[2] > 0 else mp.mpf(0),
        "d13": sd[0] / sd[2] if sd[2] > 0 else mp.mpf(0),
        "e23": se[1] / se[2] if se[2] > 0 else mp.mpf(0),
        "e13": se[0] / se[2] if se[2] > 0 else mp.mpf(0),
        "V12": V12,
        "V23": V23,
        "V13": V13,
        "Jcp": Jcp,
        "abs_Jcp": abs(Jcp),
        "std_ckm": std_ckm,
        "l1": l1,
        "l2": l2,
        "l3": l3,
        "l4": l4,
        "stab_margin": l3 + l4 + s12,
        "stab_all": bool(all_stab and stab_ir),
        "mHu2_IR": mHu2,
        "mHd2_IR": mHd2,
        "t_EWSB_u": t_ewsb_u,
        "t_EWSB_d": t_ewsb_d,
        "min_sf": min_sf,
        "S_IR": S_ir,
        "Ue": Ue,
        "su": su,
        "sd": sd,
        "se": se,
    }


def serialize_piece2(obs):
    keys_r = [
        "g1", "g2", "g3", "yt_over_g3", "mb_over_mtau",
        "u23", "u13", "d23", "d13", "e23", "e13",
        "V12", "V23", "V13", "Jcp", "l1", "l2", "l3", "l4",
        "stab_margin", "mHu2_IR", "mHd2_IR", "min_sf", "S_IR",
    ]
    d = {k: fmt_r(obs[k], 18) for k in keys_r}
    d["std_ckm"] = bool(obs["std_ckm"])
    d["stab_all"] = bool(obs["stab_all"])
    d["t_EWSB_u"] = fmt_r(obs["t_EWSB_u"], 16) if obs["t_EWSB_u"] is not None else None
    d["t_EWSB_d"] = fmt_r(obs["t_EWSB_d"], 16) if obs["t_EWSB_d"] is not None else None
    d["ewsb_u_first"] = bool(
        obs["t_EWSB_u"] is not None
        and (obs["t_EWSB_d"] is None or obs["t_EWSB_u"] > obs["t_EWSB_d"])
    )
    return d


def extract_pmns(Ye, Ynu, MR):
    """
    True U(3)_L-covariant Weinberg operator kappa_nu = Y_nu M_R^{-1} Y_nu^T
    diagonalized via disjoint 6x6 real-split Autonne-Takagi.
    """
    _, Ue = eig_herm3_realsplit(Ye * Ye.T.conjugate())
    kappa = Ynu * (MR ** (-1)) * Ynu.T
    svals, Unu = takagi_3x3_realsplit(kappa)
    # Check Takagi residual ||U_nu^H kappa U_nu^* - diag(s)||_F
    diag_chk = Unu.T.conjugate() * kappa * Unu.conjugate()
    tak_err = mp.mpf(0)
    for r in range(3):
        for c in range(3):
            tgt = svals[r] if r == c else mp.mpc(0)
            tak_err += abs(diag_chk[r, c] - tgt) ** 2
    tak_err = mp.sqrt(tak_err)

    U = Ue.T.conjugate() * Unu
    s13_sq = abs(U[0, 2]) ** 2
    c13_sq = max(POW10(-35), 1 - s13_sq)
    s12_sq = (abs(U[0, 1]) ** 2) / c13_sq
    s23_sq = (abs(U[1, 2]) ** 2) / c13_sq
    J_pmns = mp.im(U[0, 1] * U[1, 2] * mp.conj(U[0, 2]) * mp.conj(U[1, 1]))
    dm21 = svals[1] ** 2 - svals[0] ** 2
    dm31 = svals[2] ** 2 - svals[0] ** 2
    r_dm = dm21 / dm31 if dm31 > POW10(-35) else mp.mpf(0)
    return {
        "s12_sq": s12_sq,
        "s23_sq": s23_sq,
        "s13_sq": s13_sq,
        "J_pmns": J_pmns,
        "abs_J_pmns": abs(J_pmns),
        "dm21_over_dm31": r_dm,
        "svals": svals,
        "takagi_err": tak_err,
    }


def serialize_pmns(p):
    return {
        "s12_sq": fmt_r(p["s12_sq"], 18),
        "s23_sq": fmt_r(p["s23_sq"], 18),
        "s13_sq": fmt_r(p["s13_sq"], 18),
        "J_pmns": fmt_r(p["J_pmns"], 18),
        "dm21_over_dm31": fmt_r(p["dm21_over_dm31"], 18),
        "svals": fmt_list_r(p["svals"], 18),
        "takagi_err": fmt_r(p["takagi_err"], 10),
    }


def minimize_dynamic_V4_S5xS5(A_bas, S_hat, lam3=M(-1, 4)):
    """
    Disjoint multi-start Riemannian Armijo gradient descent on S^5 x S^5 minimizing:
        F(h_u, h_d) = V_4(h_u, h_d) + lam3 * |V_4(S_hat)| * |h_u^H h_d|^2.
    """
    def Y_of(sec, h):
        return h[0] * A_bas[sec][0] + h[1] * A_bas[sec][1] + h[2] * A_bas[sec][2]

    def tr_H2(Mat):
        H = Mat.T.conjugate() * Mat
        H2 = H * H
        return mp.re(mat_tr(H2))

    def norm_vec(v):
        n = mp.sqrt(sum(abs(z) ** 2 for z in v))
        return [z / n for z in v]

    V4_S_abs = abs(-3 * tr_H2(Y_of("u", S_hat)) - 3 * tr_H2(Y_of("d", S_hat)) - tr_H2(Y_of("e", S_hat)))

    def obj_grad(hu, hd):
        Yu = Y_of("u", hu)
        Yd = Y_of("d", hd)
        Ye = Y_of("e", hd)
        Hu = Yu * (Yu.T.conjugate() * Yu)
        Hd = Yd * (Yd.T.conjugate() * Yd)
        He = Ye * (Ye.T.conjugate() * Ye)
        ov = sum(mp.conj(hu[k]) * hd[k] for k in range(3))
        val = -3 * tr_H2(Yu) - 3 * tr_H2(Yd) - tr_H2(Ye) + lam3 * V4_S_abs * (abs(ov) ** 2)
        gu = [mp.mpc(0)] * 3
        gd = [mp.mpc(0)] * 3
        for k in range(3):
            AuH = A_bas["u"][k].T.conjugate()
            AdH = A_bas["d"][k].T.conjugate()
            AeH = A_bas["e"][k].T.conjugate()
            tu = sum(AuH[r, c] * Hu[c, r] for r in range(3) for c in range(3))
            td = sum(AdH[r, c] * Hd[c, r] for r in range(3) for c in range(3))
            te = sum(AeH[r, c] * He[c, r] for r in range(3) for c in range(3))
            gu[k] = -6 * tu + lam3 * V4_S_abs * hd[k] * mp.conj(ov)
            gd[k] = -6 * td - 2 * te + lam3 * V4_S_abs * hu[k] * ov
        pu = mp.re(sum(mp.conj(hu[k]) * gu[k] for k in range(3)))
        pd = mp.re(sum(mp.conj(hd[k]) * gd[k] for k in range(3)))
        gu = [gu[k] - pu * hu[k] for k in range(3)]
        gd = [gd[k] - pd * hd[k] for k in range(3)]
        return val, gu, gd

    I = IU()
    s3i = M(1) / mp.sqrt(3)
    starts = [
        (S_hat, S_hat),
        ([mp.mpc(1), mp.mpc(0), mp.mpc(0)], [mp.mpc(1), mp.mpc(0), mp.mpc(0)]),
        ([mp.mpc(0), mp.mpc(1), mp.mpc(0)], [mp.mpc(0), mp.mpc(1), mp.mpc(0)]),
        ([mp.mpc(0), mp.mpc(0), mp.mpc(1)], [mp.mpc(0), mp.mpc(0), mp.mpc(1)]),
        ([s3i, s3i, s3i], [s3i, s3i, s3i]),
        (norm_vec([mp.mpc(1), I, mp.mpc(-1)]), norm_vec([mp.mpc(1), -I, mp.mpc(1)])),
    ]
    best = None
    for (hu0, hd0) in starts:
        hu = list(hu0)
        hd = list(hd0)
        step = M(1) / (V4_S_abs + 1)
        for _ in range(180):
            val, gu, gd = obj_grad(hu, hd)
            gn2 = sum(abs(z) ** 2 for z in gu) + sum(abs(z) ** 2 for z in gd)
            if gn2 < POW10(-30) * (V4_S_abs ** 2 + 1):
                break
            alpha = step * 2
            while alpha > POW10(-22):
                hu_n = norm_vec([hu[k] - alpha * gu[k] for k in range(3)])
                hd_n = norm_vec([hd[k] - alpha * gd[k] for k in range(3)])
                v_n, _, _ = obj_grad(hu_n, hd_n)
                if v_n <= val - M(1, 10) * alpha * 2 * gn2:
                    hu, hd = hu_n, hd_n
                    step = alpha
                    break
                alpha /= 2
            else:
                break
        val, gu, gd = obj_grad(hu, hd)
        gn = mp.sqrt(sum(abs(z) ** 2 for z in gu) + sum(abs(z) ** 2 for z in gd))
        if best is None or val < best[0]:
            best = (val, hu, hd, gn)
    val, hu, hd, gn = best
    ov = abs(sum(mp.conj(hu[k]) * hd[k] for k in range(3)))
    return val, hu, hd, gn, ov


def random_cayley_unitary(rng):
    """
    Disjoint random Haar-like U(3) matrix via Cayley transform U = (I - i A)(I + i A)^{-1}
    of a random rational Hermitian matrix A (NOT Box-Muller QR!).
    """
    I = IU()
    A = mp.matrix(3, 3)
    for r in range(3):
        A[r, r] = M(rng.randint(-1500, 1500), 1000)
        for c in range(r + 1, 3):
            re_v = M(rng.randint(-1500, 1500), 1000)
            im_v = M(rng.randint(-1500, 1500), 1000)
            A[r, c] = re_v + I * im_v
            A[c, r] = re_v - I * im_v
    I3 = mp.eye(3)
    U = (I3 - I * A) * ((I3 + I * A) ** (-1))
    return U


# ---------------------------------------------------------------------------
# Module RP3 — Guardrail 4 Benchmarks, Curved Dirac G_{s=1/2}, Pieces 2 & 3, G3
# ---------------------------------------------------------------------------

def run_RP3(T_qs, rp1_cache, rp2_cache):
    t0_ns = time.monotonic_ns()
    mp.mp.dps = 45
    I = IU()

    # 1. Guardrail 4 Benchmarks
    # 1a. Chowdhury-Eberhardt (arXiv:1503.08216) 2-loop Type-II 2HDM beta_{y_t} (all terms!)
    g1_b = M(47, 100)
    g2_b = M(63, 100)
    g3_b = M(117, 100)
    yt_b = M(93, 100)
    yb_b = M(37, 100)
    ytau_b = M(21, 100)
    l1_b = M(11, 100)
    l2_b = M(13, 100)
    l3_b = M(7, 100)
    l4_b = M(-9, 100)
    Yu_b = mp.matrix([[0, 0, 0], [0, 0, 0], [0, 0, yt_b]])
    Yd_b = mp.matrix([[0, 0, 0], [0, 0, 0], [0, 0, yb_b]])
    Ye_b = mp.matrix([[0, 0, 0], [0, 0, 0], [0, 0, ytau_b]])
    I3 = mp.eye(3)
    st_b = (g1_b, g2_b, g3_b, Yu_b, Yd_b, Ye_b, l1_b, l2_b, l3_b, l4_b, M(1), M(1), I3, I3, I3, I3, I3)
    rhs_b = rge_rhs_2hdm_ii(st_b, include_lam_in_betaY=True)
    # Independent Chowdhury-Eberhardt 1-gen formula directly in CE g'^2 = (3/5) g1^2, l_CE = 2*l_D:
    gp2_b = M(3, 5) * g1_b * g1_b
    g2s_b = g2_b * g2_b
    g3s_b = g3_b * g3_b
    yt2, yb2, ytau2 = yt_b ** 2, yb_b ** 2, ytau_b ** 2
    l1c, l2c = 2 * l1_b, 2 * l2_b
    ce_lo = (M(9, 2) * yt2 + M(1, 2) * yb2 - M(17, 12) * gp2_b - M(9, 4) * g2s_b - 8 * g3s_b) * yt_b
    ce_nlo_b = (
        M(1267, 216) * gp2_b ** 2
        - M(3, 4) * gp2_b * g2s_b
        + M(19, 9) * gp2_b * g3s_b
        - M(21, 4) * g2s_b ** 2
        + 9 * g2s_b * g3s_b
        - 108 * g3s_b ** 2
        + M(3, 2) * l2c ** 2 + l3_b ** 2 + l3_b * l4_b + l4_b ** 2
    ) * yt_b
    ce_nlo_ii = (
        gp2_b * (M(-41, 144) * yb2 + M(131, 16) * yt2)
        + g2s_b * (M(33, 16) * yb2 + M(225, 16) * yt2)
        + g3s_b * (M(16, 3) * yb2 + 36 * yt2)
        - M(5, 2) * yb2 ** 2 - M(5, 2) * yb2 * yt2 - M(3, 4) * yb2 * ytau2 - 12 * yt2 ** 2
        - 2 * yb2 * l3_b + 2 * yb2 * l4_b - 6 * yt2 * l2c
    ) * yt_b
    inv16 = M(1) / (16 * mp.pi ** 2)
    ce_ref = inv16 * ce_lo + (inv16 ** 2) * (ce_nlo_b + ce_nlo_ii)
    ce_err = abs(rhs_b[3][2, 2] - ce_ref)

    # Also verify CE 1-gen beta_{y_b} and beta_{y_tau}!
    ce_yb_lo = (M(9, 2) * yb2 + M(1, 2) * yt2 + ytau2 - M(5, 12) * gp2_b - M(9, 4) * g2s_b - 8 * g3s_b) * yb_b
    ce_yb_nlo = (
        M(-113, 216) * gp2_b ** 2 - M(9, 4) * gp2_b * g2s_b + M(31, 9) * gp2_b * g3s_b
        - M(21, 4) * g2s_b ** 2 + 9 * g2s_b * g3s_b - 108 * g3s_b ** 2
        + M(3, 2) * l1c ** 2 + l3_b ** 2 + l3_b * l4_b + l4_b ** 2
        + gp2_b * (M(79, 16) * yb2 - M(53, 144) * yt2 + M(25, 8) * ytau2)
        + g2s_b * (M(225, 16) * yb2 + M(33, 16) * yt2 + M(15, 8) * ytau2)
        + g3s_b * (36 * yb2 + M(16, 3) * yt2)
        - 12 * yb2 ** 2 - M(5, 2) * yb2 * yt2 - M(9, 4) * yb2 * ytau2 - M(5, 2) * yt2 ** 2 - M(9, 4) * ytau2 ** 2
        - 6 * yb2 * l1c - 2 * yt2 * l3_b + 2 * yt2 * l4_b
    ) * yb_b
    ce_yb_err = abs(rhs_b[4][2, 2] - (inv16 * ce_yb_lo + (inv16 ** 2) * ce_yb_nlo))

    ce_ytau_lo = (M(5, 2) * ytau2 + 3 * yb2 - M(15, 4) * gp2_b - M(9, 4) * g2s_b) * ytau_b
    ce_ytau_nlo = (
        M(161, 8) * gp2_b ** 2 + M(9, 4) * gp2_b * g2s_b - M(21, 4) * g2s_b ** 2
        + M(3, 2) * l1c ** 2 + l3_b ** 2 + l3_b * l4_b + l4_b ** 2
        + gp2_b * (M(25, 24) * yb2 + M(179, 16) * ytau2)
        + g2s_b * (M(45, 8) * yb2 + M(165, 16) * ytau2)
        + 20 * g3s_b * yb2
        - M(27, 4) * yb2 ** 2 - M(9, 4) * yb2 * yt2 - M(27, 4) * yb2 * ytau2 - 3 * ytau2 ** 2
        - 6 * ytau2 * l1c
    ) * ytau_b
    ce_ytau_err = abs(rhs_b[5][2, 2] - (inv16 * ce_ytau_lo + (inv16 ** 2) * ce_ytau_nlo))

    # 1b. Martin (hep-ph/9709356) Eqs. 6.5.24-6.5.30 7-equation soft-mass benchmark (non-universal S != 0!)
    mHu_m, mHd_m = M(11, 10), M(17, 10)
    mQ_m, mu_m, md_m, mL_m, me_m = M(13, 10), M(19, 10), M(23, 10), M(29, 10), M(31, 10)
    st_m = (
        g1_b, g2_b, g3_b, Yu_b, Yd_b, Ye_b, l1_b, l2_b, l3_b, l4_b,
        mHu_m, mHd_m, mQ_m * I3, mu_m * I3, md_m * I3, mL_m * I3, me_m * I3,
    )
    rhs_m = rge_rhs_2hdm_ii(st_m, include_lam_in_betaY=True)
    Xt = 2 * yt2 * (mHu_m + mQ_m + mu_m)
    Xb = 2 * yb2 * (mHd_m + mQ_m + md_m)
    Xtau = 2 * ytau2 * (mHd_m + mL_m + me_m)
    S_m = mHu_m - mHd_m + 3 * (mQ_m - mL_m - 2 * mu_m + md_m + me_m)
    g1s_b = g1_b * g1_b
    martin_refs = [
        inv16 * (3 * Xt + M(3, 5) * g1s_b * S_m),
        inv16 * (3 * Xb + Xtau - M(3, 5) * g1s_b * S_m),
        inv16 * (Xt + Xb + M(1, 5) * g1s_b * S_m),
        inv16 * (2 * Xt - M(4, 5) * g1s_b * S_m),
        inv16 * (2 * Xb + M(2, 5) * g1s_b * S_m),
        inv16 * (Xtau - M(3, 5) * g1s_b * S_m),
        inv16 * (2 * Xtau + M(6, 5) * g1s_b * S_m),
    ]
    martin_vals = [
        rhs_m[10], rhs_m[11], rhs_m[12][2, 2], rhs_m[13][2, 2],
        rhs_m[14][2, 2], rhs_m[15][2, 2], rhs_m[16][2, 2],
    ]
    martin_max_err = max(abs(a - b) for a, b in zip(martin_vals, martin_refs))

    # 1c. Xing-Zhou opposite d|V_cb|/dt sign in 2HDM-II vs 1HDM
    th = M(1, 20)
    V_rot = mp.matrix([[1, 0, 0], [0, mp.cos(th), mp.sin(th)], [0, -mp.sin(th), mp.cos(th)]])
    Yu_xz = mp.matrix([[M(1, 1000), 0, 0], [0, M(1, 100), 0], [0, 0, M(9, 10)]])
    Yd_xz = V_rot * mp.matrix([[M(1, 1000), 0, 0], [0, M(1, 100), 0], [0, 0, M(3, 10)]])
    Ye_xz = mp.matrix([[M(1, 1000), 0, 0], [0, M(1, 100), 0], [0, 0, M(1, 10)]])
    st_xz = make_initial_state(Yu_xz, Yd_xz, Ye_xz)
    st_2hdm_dn, _, _, _ = integrate_gl4(st_xz, M(-2), 10, include_lam_in_betaY=True, mode_1hdm=False)
    st_1hdm_dn, _, _, _ = integrate_gl4(st_xz, M(-2), 10, include_lam_in_betaY=True, mode_1hdm=True)

    def get_Vcb(st_v):
        _, Uu_v = eig_herm3_realsplit(st_v[3] * st_v[3].T.conjugate())
        _, Ud_v = eig_herm3_realsplit(st_v[4] * st_v[4].T.conjugate())
        return abs((Uu_v.T.conjugate() * Ud_v)[1, 2])

    vcb_0 = get_Vcb(st_xz)
    vcb_2hdm = get_Vcb(st_2hdm_dn)
    vcb_1hdm = get_Vcb(st_1hdm_dn)
    # Running DOWN (dt < 0): in 2HDM-II d|V_cb|/dt < 0 => |V_cb| INCREASES; in 1HDM d|V_cb|/dt > 0 => DECREASES!
    dVcb_dt_2hdm = (vcb_2hdm - vcb_0) / M(-2)
    dVcb_dt_1hdm = (vcb_1hdm - vcb_0) / M(-2)
    xz_opposite_sign = bool(dVcb_dt_2hdm < 0 and dVcb_dt_1hdm > 0)

    g4_benchmarks = {
        "CE_2loop_yt_abs_err": fmt_r(ce_err, 10),
        "CE_2loop_yb_abs_err": fmt_r(ce_yb_err, 10),
        "CE_2loop_ytau_abs_err": fmt_r(ce_ytau_err, 10),
        "Martin_7eq_max_err": fmt_r(martin_max_err, 10),
        "XZ_dVcb_dt_2HDM_II": fmt_r(dVcb_dt_2hdm, 14),
        "XZ_dVcb_dt_1HDM": fmt_r(dVcb_dt_1hdm, 14),
        "XZ_opposite_sign": xz_opposite_sign,
        "pass": bool(
            ce_err < POW10(-38)
            and ce_yb_err < POW10(-38)
            and ce_ytau_err < POW10(-38)
            and martin_max_err < POW10(-38)
            and xz_opposite_sign
        ),
    }

    # 2. All 3 canonical vacua: tau_omega, tau_FILQ1*, tau_tot*(70)
    mp.mp.dps = 36
    tau_filq1 = I * rp1_cache["y_filq1"]
    f_filq1 = solve_fuchsian_L2(tau_filq1, hi_prec=False)
    vacua = [
        ("omega", rp2_cache["tau_w"], rp2_cache["f_w"]),
        ("FILQ1_star", tau_filq1, f_filq1),
        ("tot_star_70", rp2_cache["tau_tot_star"], rp2_cache["f_tot_star"]),
    ]

    curved_G_out = {}
    vacua_results = {}
    haar_seed_state = None  # store (Yu, Yd, Ye, Ynu_w, MR_2w) at tot_star_70 DynamicV4 for Guardrail 3!
    rpf456_cache = None

    for vname, tau_v, f_v in vacua:
        # 2a. Curved spin-1/2 Dirac G_{s=1/2}
        G_info = compute_curved_dirac_G_s12(tau_v, f_v)
        curved_G_out[vname] = {
            "tau": fmt_c(tau_v, 20),
            "L2": fmt_r(f_v["L2"], 20),
            "Area_over_2pi_minus_1": fmt_r(G_info["Area"] / (2 * mp.pi) - 1, 10),
            "gb_err": fmt_r(G_info["gb_err"], 10),
            "G_raw_423": fmt_list_r(G_info["G_raw"], 16),
            "G_am_423": fmt_list_r(G_info["G_am"], 16),
            "G_gm_423": fmt_list_r(G_info["G_gm"], 16),
            "isotropy_err": fmt_r(G_info["iso_err"], 10),
            "gb_pass": bool(G_info["gb_err"] < POW10(-3)),
        }

        # 2b. Build mark w = (4/15, 1/30) => (8, 1) and doubled mark 2w = (8/15, 1/15) => (16, 2)
        Y_bas_w, S_vec = eval_mark_basis(8, 1, tau_v, f_v["L2"], T_qs)
        Y_bas_2w, _ = eval_mark_basis(16, 2, tau_v, f_v["L2"], T_qs)
        nrm_S = mp.sqrt(sum(abs(z) ** 2 for z in S_vec))
        S_hat = [z / nrm_S for z in S_vec]

        G_am = G_info["G_am"]
        Gih = mp.matrix([
            [1 / mp.sqrt(G_am[0]), 0, 0],
            [0, 1 / mp.sqrt(G_am[1]), 0],
            [0, 0, 1 / mp.sqrt(G_am[2])],
        ])
        A_bas_curv_w = {
            sec: [Gih * Y_bas_w[sec][qi] * Gih for qi in range(3)]
            for sec in ("u", "d", "e", "nu")
        }
        A_bas_curv_2w = {
            sec: [Gih * Y_bas_2w[sec][qi] * Gih for qi in range(3)]
            for sec in ("nu",)
        }

        # Dynamic V4 minimization on S^5 x S^5 (curved basis)
        val_dyn, hu_dyn, hd_dyn, gn_dyn, ov_dyn = minimize_dynamic_V4_S5xS5(
            A_bas_curv_w, S_hat, lam3=M(-1, 4)
        )

        branches = [
            ("Static_FLAT", Y_bas_w, Y_bas_2w, S_hat, S_hat),
            ("Static_CURVED_s12", A_bas_curv_w, A_bas_curv_2w, S_hat, S_hat),
            ("DynamicV4_ferro_CURVED_s12", A_bas_curv_w, A_bas_curv_2w, hu_dyn, hd_dyn),
        ]

        br_out = {}
        for bname, bas_w, bas_2w, hu_v, hd_v in branches:
            Yu_raw = hu_v[0] * bas_w["u"][0] + hu_v[1] * bas_w["u"][1] + hu_v[2] * bas_w["u"][2]
            Yd_raw = hd_v[0] * bas_w["d"][0] + hd_v[1] * bas_w["d"][1] + hd_v[2] * bas_w["d"][2]
            Ye_raw = hd_v[0] * bas_w["e"][0] + hd_v[1] * bas_w["e"][1] + hd_v[2] * bas_w["e"][2]
            Ynu_w_raw = hu_v[0] * bas_w["nu"][0] + hu_v[1] * bas_w["nu"][1] + hu_v[2] * bas_w["nu"][2]
            Ynu_2w_raw = hu_v[0] * bas_2w["nu"][0] + hu_v[1] * bas_2w["nu"][1] + hu_v[2] * bas_2w["nu"][2]

            # Single overall normalization max_f sigma_3(Y_f) = 1 across {u, d, e}
            s3_u = mp.sqrt(max(mp.mpf(0), eigvals_herm3_realsplit(Yu_raw * Yu_raw.T.conjugate())[2]))
            s3_d = mp.sqrt(max(mp.mpf(0), eigvals_herm3_realsplit(Yd_raw * Yd_raw.T.conjugate())[2]))
            s3_e = mp.sqrt(max(mp.mpf(0), eigvals_herm3_realsplit(Ye_raw * Ye_raw.T.conjugate())[2]))
            scale_all = max(s3_u, s3_d, s3_e)
            Yu0 = Yu_raw / scale_all
            Yd0 = Yd_raw / scale_all
            Ye0 = Ye_raw / scale_all
            Ynu_w = Ynu_w_raw / scale_all
            Ynu_2w = Ynu_2w_raw / scale_all

            # UV observables
            st0 = make_initial_state(Yu0, Yd0, Ye0)
            uv_obs = extract_piece2_observables(st0, None, None, True)

            # Piece 2: GL4 integration t = 0 -> -35 (n=80 AND n=160 step-halving check!)
            st80, tu80, td80, stab80 = integrate_gl4(st0, M(-35), 80, include_lam_in_betaY=True)
            st160, tu160, td160, stab160 = integrate_gl4(st0, M(-35), 160, include_lam_in_betaY=True)
            ir80 = extract_piece2_observables(st80, tu80, td80, stab80)
            ir160 = extract_piece2_observables(st160, tu160, td160, stab160)

            step_half_err = max(
                abs(ir80[k] - ir160[k]) / (abs(ir160[k]) + 1)
                for k in ("yt_over_g3", "mb_over_mtau", "V12", "V23", "V13", "mHu2_IR", "mHd2_IR", "min_sf")
            )

            # Diagnostic sensitivity: decoupled lambda=0 in beta_Y^(2) (n=80)
            st_nolam, tu_nl, td_nl, stab_nl = integrate_gl4(st0, M(-35), 80, include_lam_in_betaY=False)
            ir_nl = extract_piece2_observables(st_nolam, tu_nl, td_nl, stab_nl)

            # Piece 3: Majorana PMNS at UV (Ye0) and IR (st160[5]) for M_R in {I_3, 1w, 2w}
            MR_1w = (Ynu_w + Ynu_w.T) / 2
            MR_2w = (Ynu_2w + Ynu_2w.T) / 2
            pmns_uv = {}
            pmns_ir = {}
            for mlabel, MR_mat in [("I3", I3), ("sym_1w", MR_1w), ("sym_2w", MR_2w)]:
                pmns_uv[mlabel] = serialize_pmns(extract_pmns(Ye0, Ynu_w, MR_mat))
                pmns_ir[mlabel] = serialize_pmns(extract_pmns(st160[5], Ynu_w, MR_mat))

            br_entry = {
                "UV": serialize_piece2(uv_obs),
                "IR_n160": serialize_piece2(ir160),
                "IR_n80_vs_n160_rel_err": fmt_r(step_half_err, 10),
                "IR_nolam_betaY_diag": {
                    "yt_over_g3": fmt_r(ir_nl["yt_over_g3"], 14),
                    "mb_over_mtau": fmt_r(ir_nl["mb_over_mtau"], 14),
                    "V12": fmt_r(ir_nl["V12"], 14),
                    "V23": fmt_r(ir_nl["V23"], 14),
                    "V13": fmt_r(ir_nl["V13"], 14),
                    "mHu2_IR": fmt_r(ir_nl["mHu2_IR"], 14),
                    "mHd2_IR": fmt_r(ir_nl["mHd2_IR"], 14),
                },
                "Piece3_PMNS_UV": pmns_uv,
                "Piece3_PMNS_IR": pmns_ir,
            }
            if bname == "DynamicV4_ferro_CURVED_s12":
                br_entry["dynamic_V4_min"] = {
                    "V_obj": fmt_r(val_dyn, 18),
                    "grad_norm": fmt_r(gn_dyn, 10),
                    "overlap_hu_hd": fmt_r(ov_dyn, 16),
                }
            br_out[bname] = br_entry

            if vname == "tot_star_70" and bname == "DynamicV4_ferro_CURVED_s12":
                haar_seed_state = (Yu0, Yd0, Ye0, Ynu_w, MR_2w, ir80, extract_pmns(st80[5], Ynu_w, MR_2w))
                rpf456_cache = (Ye0, Ynu_w, MR_2w)

        vacua_results[vname] = br_out

    # 3. Guardrail 3: 10-trial Cayley-transform Haar U(3)^5 x U(3)_{nu_R} scrambling
    # Test through FULL coupled 2-loop Yukawa + quartics + 3x3 soft-mass EWSB + Majorana PMNS!
    mp.mp.dps = 38
    Yu_ref, Yd_ref, Ye_ref, Ynu_ref, MR_ref, _, _ = haar_seed_state
    st_ref0 = make_initial_state(Yu_ref, Yd_ref, Ye_ref)
    st_ref80, tu_ref, td_ref, stab_ref = integrate_gl4(st_ref0, M(-35), 80, include_lam_in_betaY=True)
    ir_ref = extract_piece2_observables(st_ref80, tu_ref, td_ref, stab_ref)
    pmns_ref = extract_pmns(st_ref80[5], Ynu_ref, MR_ref)
    rng = random.Random(20261126)
    max_unitarity_err = mp.mpf(0)
    max_drift_all = mp.mpf(0)
    trial_drifts = []
    obs_keys = [
        "yt_over_g3", "mb_over_mtau", "u23", "d23", "e23",
        "V12", "V23", "V13", "abs_Jcp", "l1", "l2", "l3", "l4",
        "mHu2_IR", "mHd2_IR", "min_sf", "S_IR",
    ]
    pmns_keys = ["s12_sq", "s23_sq", "s13_sq", "abs_J_pmns", "dm21_over_dm31"]

    for tr in range(10):
        UQ = random_cayley_unitary(rng)
        Uu = random_cayley_unitary(rng)
        Ud = random_cayley_unitary(rng)
        UL = random_cayley_unitary(rng)
        Ue = random_cayley_unitary(rng)
        UnuR = random_cayley_unitary(rng)
        for Umat in (UQ, Uu, Ud, UL, Ue, UnuR):
            diff_u = Umat.T.conjugate() * Umat - I3
            u_err = mp.sqrt(sum(abs(diff_u[r, c]) ** 2 for r in range(3) for c in range(3)))
            if u_err > max_unitarity_err:
                max_unitarity_err = u_err

        Yu_s = UQ * Yu_ref * Uu.T.conjugate()
        Yd_s = UQ * Yd_ref * Ud.T.conjugate()
        Ye_s = UL * Ye_ref * Ue.T.conjugate()
        Ynu_s = UL * Ynu_ref * UnuR.T.conjugate()
        MR_s = UnuR.conjugate() * MR_ref * UnuR.T.conjugate()

        st_s0 = make_initial_state(Yu_s, Yd_s, Ye_s, soft_rots=(UQ, Uu, Ud, UL, Ue))
        st_s80, tu_s, td_s, stab_s = integrate_gl4(st_s0, M(-35), 80, include_lam_in_betaY=True)
        ir_s = extract_piece2_observables(st_s80, tu_s, td_s, stab_s)
        pmns_s = extract_pmns(st_s80[5], Ynu_s, MR_s)

        tdrift = mp.mpf(0)
        for k in obs_keys:
            d = abs(ir_s[k] - ir_ref[k]) / (abs(ir_ref[k]) + 1)
            if d > tdrift:
                tdrift = d
        if ir_ref["t_EWSB_u"] is not None and ir_s["t_EWSB_u"] is not None:
            d = abs(ir_s["t_EWSB_u"] - ir_ref["t_EWSB_u"]) / (abs(ir_ref["t_EWSB_u"]) + 1)
            if d > tdrift:
                tdrift = d
        for k in pmns_keys:
            d = abs(pmns_s[k] - pmns_ref[k]) / (abs(pmns_ref[k]) + 1)
            if d > tdrift:
                tdrift = d
        trial_drifts.append(fmt_r(tdrift, 10))
        if tdrift > max_drift_all:
            max_drift_all = tdrift

    haar_out = {
        "n_trials": 10,
        "generator": "Cayley transform U = (I - i A)(I + i A)^{-1}",
        "max_unitarity_err": fmt_r(max_unitarity_err, 10),
        "max_observable_drift": fmt_r(max_drift_all, 10),
        "trial_drifts": trial_drifts,
        "pass": bool(max_unitarity_err < POW10(-30) and max_drift_all < POW10(-25)),
    }

    # Check RG4 & RG5 criteria
    gb_all_ok = all(v["gb_pass"] for v in curved_G_out.values())
    w_iso_ok = bool(mp.mpf(curved_G_out["omega"]["isotropy_err"]) < POW10(-3))
    step_half_ok = True
    ewsb_stab_ok = True
    s_ir_ok = True
    for vname in vacua_results:
        for bname, bres in vacua_results[vname].items():
            if mp.mpf(bres["IR_n80_vs_n160_rel_err"]) >= POW10(-6):
                step_half_ok = False
            ir = bres["IR_n160"]
            if not ir["stab_all"]:
                ewsb_stab_ok = False
            if not (mp.mpf(ir["mHu2_IR"]) < 0 and mp.mpf(ir["min_sf"]) > 0):
                ewsb_stab_ok = False
            if abs(mp.mpf(ir["S_IR"])) >= POW10(-25):
                s_ir_ok = False

    takagi_all_ok = True
    for vname in vacua_results:
        for bname, bres in vacua_results[vname].items():
            for sec_k in ("Piece3_PMNS_UV", "Piece3_PMNS_IR"):
                for mk, pval in bres[sec_k].items():
                    if mp.mpf(pval["takagi_err"]) >= POW10(-25):
                        takagi_all_ok = False
    rg4_pass = bool(g4_benchmarks["pass"] and gb_all_ok and w_iso_ok and step_half_ok and ewsb_stab_ok and s_ir_ok)
    rg5_pass = bool(haar_out["pass"] and takagi_all_ok)

    return {
        "guardrail4_benchmarks": g4_benchmarks,
        "curved_dirac_G_s12": curved_G_out,
        "vacua_unfolding": vacua_results,
        "guardrail3_haar_10trials": haar_out,
        "RG4_pass": rg4_pass,
        "RG5_pass": rg5_pass,
        "elapsed_sec": elapsed_sec_str(t0_ns),
    }, rpf456_cache


# ---------------------------------------------------------------------------
# Module RP4 — All 6/6 Planted Negative Controls (RPF1-RPF6) & 6/6 Gates
# ---------------------------------------------------------------------------

def run_RP4(rp1_cache, rp2_cache, rpf456_cache):
    t0_ns = time.monotonic_ns()
    mp.mp.dps = 38
    I = IU()
    I3 = mp.eye(3)

    # RPF1: Drop -3/(pi*y) from E2_hat -> breaks S-invariance of V_{FILQ, 1} (> 0.1)
    tau_gen = M(137, 1000) + I * M(1213, 1000)
    v_bad = V_FILQ(tau_gen, 1, drop_nonholo=True)
    v_bad_S = V_FILQ(-1 / tau_gen, 1, drop_nonholo=True)
    rpf1_err = abs(v_bad_S - v_bad) / (abs(v_bad) + 1)
    rpf1_ok = bool(rpf1_err > M(1, 10))

    # RPF2: Sub-critical V_{FILQ, 1} + 70 * V_CW(1) at 1/2 + 4i -> < -1e9 cusp runaway
    tau_h4i = M(1, 2) + 4 * I
    v_subcrit = V_FILQ(tau_h4i, 1) + 70 * rp2_cache["a_h4i"]["VCW1"]
    rpf2_ok = bool(v_subcrit < -POW10(9))

    # RPF3: Shift off tau_{FILQ, 1}^* by (+1/10, +1/10) -> dV > 0.01, |grad V| > 0.5
    y_f1 = rp1_cache["y_filq1"]
    fn_f1 = lambda x, y: V_FILQ(x + I * y, 1)
    V_opt = fn_f1(M(0), y_f1)
    V_sh, gx_sh, gy_sh, _, _, _, _, _ = grad_hess_2d(fn_f1, M(1, 10), y_f1 + M(1, 10), POW10(-6))
    dV_sh = V_sh - V_opt
    gn_sh = mp.sqrt(gx_sh ** 2 + gy_sh ** 2)
    rpf3_ok = bool(dV_sh > M(1, 100) and gn_sh > M(1, 2))

    # RPF4: Degenerate M_R = Y_nu^T Y_nu -> exact kappa_nu = I_3
    Ye0, Ynu_w, MR_2w = rpf456_cache
    MR_deg = Ynu_w.T * Ynu_w
    kappa_deg = Ynu_w * (MR_deg ** (-1)) * Ynu_w.T
    frob_err = mp.sqrt(sum(abs(kappa_deg[r, c] - (1 if r == c else 0)) ** 2 for r in range(3) for c in range(3)))
    s_deg, _ = takagi_3x3_realsplit(kappa_deg)
    spread_deg = (s_deg[2] - s_deg[0]) / s_deg[2]
    rpf4_ok = bool(frob_err < POW10(-25) and spread_deg < POW10(-25))

    # RPF5: Broken contraction Y_nu^T M_R^{-1} Y_nu under Cayley Haar -> fails U(3)_L (> 0.5)
    rng = random.Random(999123)
    kappa_brk0 = Ynu_w.T * (MR_2w ** (-1)) * Ynu_w
    s_brk0, _ = takagi_3x3_realsplit(kappa_brk0)
    max_brk_drift = mp.mpf(0)
    for _ in range(5):
        UL = random_cayley_unitary(rng)
        UnuR = random_cayley_unitary(rng)
        Ynu_r = UL * Ynu_w * UnuR.T.conjugate()
        MR_r = UnuR.conjugate() * MR_2w * UnuR.T.conjugate()
        kappa_brkr = Ynu_r.T * (MR_r ** (-1)) * Ynu_r
        s_brkr, _ = takagi_3x3_realsplit(kappa_brkr)
        d = max(abs(s_brkr[k] - s_brk0[k]) / (abs(s_brk0[k]) + POW10(-30)) for k in range(3))
        if d > max_brk_drift:
            max_brk_drift = d
    rpf5_ok = bool(max_brk_drift > M(1, 2))

    # RPF6: Zeroing Yukawas -> kills radiative EWSB (m_{H_u}^2 = m_{H_d}^2 = +1, no zero crossing)
    Z3 = mp.zeros(3)
    st_z0 = make_initial_state(Z3, Z3, Z3)
    st_zIR, tu_z, td_z, _ = integrate_gl4(st_z0, M(-35), 80, include_lam_in_betaY=True)
    err_mHu = abs(st_zIR[10] - 1)
    err_mHd = abs(st_zIR[11] - 1)
    rpf6_ok = bool(err_mHu < POW10(-30) and err_mHd < POW10(-30) and tu_z is None and td_z is None)

    controls = {
        "RPF1_drop_nonholo_E2": {
            "S_rel_err": fmt_r(rpf1_err, 14),
            "triggered": rpf1_ok,
        },
        "RPF2_subcritical_FILQ1_cusp": {
            "V_at_half_4i": fmt_r(v_subcrit, 18),
            "triggered": rpf2_ok,
        },
        "RPF3_off_minimum_shift": {
            "dV": fmt_r(dV_sh, 16),
            "grad_norm": fmt_r(gn_sh, 16),
            "triggered": rpf3_ok,
        },
        "RPF4_degenerate_MR_YnuTYnu": {
            "frob_kappa_minus_I3": fmt_r(frob_err, 10),
            "spectral_spread": fmt_r(spread_deg, 10),
            "triggered": rpf4_ok,
        },
        "RPF5_broken_contraction_Haar": {
            "max_rel_drift": fmt_r(max_brk_drift, 14),
            "triggered": rpf5_ok,
        },
        "RPF6_zero_yukawas_no_ewsb": {
            "mHu2_IR": fmt_r(st_zIR[10], 20),
            "mHd2_IR": fmt_r(st_zIR[11], 20),
            "t_EWSB_u": None if tu_z is None else fmt_r(tu_z, 10),
            "t_EWSB_d": None if td_z is None else fmt_r(td_z, 10),
            "triggered": rpf6_ok,
        },
    }
    n_trig = sum(1 for v in controls.values() if v["triggered"])
    return {
        "planted_controls": controls,
        "triggered_count": int(n_trig),
        "total_count": 6,
        "pass": bool(n_trig == 6),
        "elapsed_sec": elapsed_sec_str(t0_ns),
    }


# ---------------------------------------------------------------------------
# Main Entrypoint
# ---------------------------------------------------------------------------

def main():
    t_start_ns = time.monotonic_ns()
    out_dir = Path(__file__).resolve().parent
    out_json = out_dir / "referee_a2_p629_veff_modulus_out.json"
    out_sha = out_dir / "OUTPUT_SHA256.txt"

    T_qs, pts = build_frame_C_constants()

    rp1_out, rp1_cache = run_RP1()
    rp2_out, rp2_cache = run_RP2(T_qs, pts, rp1_cache)
    rp3_out, rpf456_cache = run_RP3(T_qs, rp1_cache, rp2_cache)
    rp4_out = run_RP4(rp1_cache, rp2_cache, rpf456_cache)

    gates = {
        "RG1_RP1_bosonic_and_FILQ": bool(rp1_out["pass"]),
        "RG2_RP2_P2A_P2B_and_TS_inv": bool(
            rp2_out["ts_invariance_pass"]
            and rp2_out["P2_A_trace_scale"]["pass"]
            and rp2_out["P2_B_casimir_nogo"]["pass"]
        ),
        "RG3_RP2_P2C_coupled_vacuum": bool(rp2_out["P2_C_coupled_vacuum"]["pass"]),
        "RG4_RP3_G4_curved_Dirac_Piece2": bool(rp3_out["RG4_pass"]),
        "RG5_RP3_Piece3_and_Haar_G3": bool(rp3_out["RG5_pass"]),
        "RG6_RP4_planted_controls_6of6": bool(rp4_out["pass"]),
    }
    gates_passed = sum(1 for v in gates.values() if v)
    all_pass = bool(gates_passed == 6)

    payload = {
        "card_id": "AGY-002_A2-P629-VEFF-MODULUS",
        "role": "100% Blind Disjoint Cold-Room Zero-Trust Referee",
        "empirical_inputs_used": "0 of 19",
        "python_version": sys.version.split()[0],
        "mpmath_version": mp.__version__,
        "sympy_version": sp.__version__,
        "disjoint_algorithms": {
            "RP1_eta_E2": "Euler pentagonal theorem + exact logarithmic derivative E2 = 1 + 24*q*P'/P",
            "RP1_Eisenstein": "Chowla-Selberg + direct N=40 square-box lattice sum",
            "RP2_wp": "Exact Jacobi theta_1 logarithmic derivative",
            "RP2_Fuchsian_L2": "Hybrid explicit 6th-order Yoshida Solution A (exact BCH) + implicit GL10/GL12 symplectic polish",
            "RP2_RP3_linalg": "6x6 real-split symmetric mp.eigsy for Hermitian spectra and Autonne-Takagi",
            "RP3_curved_Dirac_G": "Corner-split Clenshaw-Curtis polar quadrature + Forest-Ruth symplectic radial ray",
            "RP3_RGE_integrator": "2-stage 4th-order implicit Gauss-Legendre (GL4) with cubic Hermite EWSB roots",
            "RP3_dynamic_V4": "Multi-start Riemannian Armijo gradient descent on S^5 x S^5",
            "RP3_Haar_G3": "10-trial Cayley-transform U = (I - i A)(I + i A)^{-1} over U(3)^5 x U(3)_{nu_R}",
        },
        "RP1": rp1_out,
        "RP2": rp2_out,
        "RP3": rp3_out,
        "RP4": rp4_out,
        "referee_gates": gates,
        "gates_passed": int(gates_passed),
        "gates_total": 6,
        "all_pass": all_pass,
        "total_elapsed_sec": elapsed_sec_str(t_start_ns),
    }

    assert_zero_json_floats(payload)
    json_bytes = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")
    out_json.write_bytes(json_bytes)
    digest = hashlib.sha256(json_bytes).hexdigest()
    out_sha.write_text(f"{digest}  {out_json.name}\n", encoding="utf-8")
    print(f"WROTE {out_json.name} ({len(json_bytes)} bytes) sha256={digest}")
    print(f"GATES: {gates_passed}/6  ALL_PASS={all_pass}  ELAPSED={payload['total_elapsed_sec']}s")


if __name__ == "__main__":
    main()
