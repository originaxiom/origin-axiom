#!/usr/bin/env python3
"""
Independent Cold-Room Zero-Trust Referee for AGY-002 Card A2-OW13 (+ Erratum 1).

Strict Cold-Room & Guardrail Compliance:
  - Authored solely from Card A2-OW13, Erratum 1, and Card A2-OW10 prior to Commit 4b.
  - Zero float or complex AST literals anywhere in this script.
  - Zero frontier/ or producer imports.
  - Zero empirical PDG inputs (Guardrail 4 literature benchmarks strictly isolated
    inside dedicated unit-gate functions).
  - Zero hardcoded proof flags: all booleans computed from explicit algebraic,
    symbolic, and high-precision numerical checks at 60 decimal digits.

Disjoint Mathematical & Numerical Methods:
  1. Symbolic derivation of the 4D Litim threshold integral, f_lam^(dD), f_lam^(LDW),
     and beta_xi^(grav, bg) via sympy.integrate and sympy.diff (no finite differences).
  2. Symbolic derivation of the A2-OW10 gravity fixed-point cubic and root finding via
     sympy.real_roots + sympy.Poly.nroots (disjoint from mp.polyroots).
  3. First-principles derivation of 2HDM pure-scalar quartic beta functions from the
     8x8 Hessian Tr(H^2) via sympy.hessian; 4-coupling nonlinear system solved via
     sympy.Matrix.jacobian + mpmath damped Newton; G_SM collision proved via exact
     sympy discriminant, explicit complex roots, and sum-of-squares algebraic identity.
  4. Disjoint ODE integration using BOTH pure mpmath classic RK4 with step-halving
     Richardson extrapolation AND scipy.integrate.solve_ivp(..., method="Radau")
     (disjoint from DOP853).
  5. Symbolic sympy.solve / sympy.diff / sympy.simplify proofs for f_g > 0 theorem,
     1-loop M_xi stability, Avramidi-Barvinsky / Codello-Percacci C^2 + R^2 quadratic
     gravity and |xi - 1/6|_crit bounds, exact 2H Gildener-Weinberg identity, and
     all 4/4 planted fault controls PF-OW13-1..4.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Callable, Dict, List, Tuple

import mpmath as mp
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq


mp.mp.dps = 60


def mp_frac(num: int, den: int = 1) -> mp.mpf:
    """Build exact rational mpmath float from integer numerator/denominator."""
    return mp.mpf(num) / mp.mpf(den)


def sp_to_mp(expr: sp.Expr) -> mp.mpf:
    """Evaluate a real SymPy expression to 60-digit mpmath mpf."""
    return mp.mpf(str(sp.N(expr, 65)))


def to_pair(val: mp.mpf, digits: int = 35) -> Dict[str, Any]:
    """Return both JSON float and high-precision string for exact cross-checks."""
    return {
        "float": float(val),
        "mp_str": mp.nstr(val, digits),
    }


def rk4_mp_step_halving(
    rhs: Callable[[mp.mpf, List[mp.mpf]], List[mp.mpf]],
    t0: mp.mpf,
    t1: mp.mpf,
    y0: List[mp.mpf],
    n_coarse: int,
) -> Tuple[List[mp.mpf], List[mp.mpf], List[mp.mpf], mp.mpf]:
    """
    Classic 4th-order Runge-Kutta in pure mpmath with step-halving Richardson
    extrapolation (n_coarse vs 2*n_coarse).
    Returns (y_coarse, y_fine, y_richardson, max_step_halving_diff).
    """

    def integrate(nsteps: int) -> List[mp.mpf]:
        h = (t1 - t0) / mp.mpf(nsteps)
        half = mp_frac(1, 2)
        sixth = mp_frac(1, 6)
        t = t0
        y = list(y0)
        dim = len(y)
        for _ in range(nsteps):
            k1 = rhs(t, y)
            y2 = [y[i] + h * half * k1[i] for i in range(dim)]
            k2 = rhs(t + h * half, y2)
            y3 = [y[i] + h * half * k2[i] for i in range(dim)]
            k3 = rhs(t + h * half, y3)
            y4 = [y[i] + h * k3[i] for i in range(dim)]
            k4 = rhs(t + h, y4)
            y = [
                y[i] + h * sixth * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i])
                for i in range(dim)
            ]
            t = t + h
        return y

    y_c = integrate(n_coarse)
    y_f = integrate(2 * n_coarse)
    y_r = [(16 * y_f[i] - y_c[i]) / mp.mpf(15) for i in range(len(y0))]
    max_diff = max(abs(y_f[i] - y_c[i]) for i in range(len(y0)))
    return y_c, y_f, y_r, max_diff


# =============================================================================
# TASK OW13-A.1: Isolated Guardrail 4 Buttazzo 1-Loop SM Criticality Benchmark
# =============================================================================
def run_guardrail4_buttazzo_sm() -> Dict[str, Any]:
    """
    Isolated Guardrail 4 unit gate for 1-loop SM criticality
    (Buttazzo et al. arXiv:1307.3536 Table 3 exact rational inputs).
    Strictly isolated: inputs never leave this function.
    """
    mu0 = mp_frac(1731, 10)
    m_pl = mp.mpf(122) * (mp.mpf(10) ** 17)
    t_pl = mp.log(m_pl / mu0)
    t_end = mp.mpf(40)

    y0 = [
        mp_frac(11666, 10**4),   # g_3
        mp_frac(64822, 10**5),   # g_2
        mp_frac(35761, 10**5),   # g'
        mp_frac(93558, 10**5),   # y_t
        mp_frac(12711, 10**5),   # lam_B
    ]

    inv16pi2 = mp.mpf(1) / (mp.mpf(16) * mp.pi**2)
    c_g2 = -mp_frac(19, 6)
    c_gp = mp_frac(41, 6)
    c_yt_self = mp_frac(9, 2)
    c_yt_g2 = -mp_frac(9, 4)
    c_yt_gp = -mp_frac(17, 12)
    c_lam_box = mp_frac(3, 8)

    def sm_rhs_mp(_t: mp.mpf, y: List[mp.mpf]) -> List[mp.mpf]:
        g3, g2, gp, yt, lam_b = y
        dg3 = inv16pi2 * (-mp.mpf(7) * g3**3)
        dg2 = inv16pi2 * (c_g2 * g2**3)
        dgp = inv16pi2 * (c_gp * gp**3)
        dyt = inv16pi2 * yt * (
            c_yt_self * yt**2 - mp.mpf(8) * g3**2 + c_yt_g2 * g2**2 + c_yt_gp * gp**2
        )
        dlam = inv16pi2 * (
            mp.mpf(24) * lam_b**2
            + mp.mpf(12) * lam_b * yt**2
            - mp.mpf(6) * yt**4
            - mp.mpf(3) * lam_b * (mp.mpf(3) * g2**2 + gp**2)
            + c_lam_box * (mp.mpf(2) * g2**4 + (g2**2 + gp**2) ** 2)
        )
        return [dg3, dg2, dgp, dyt, dlam]

    inv16pi2_f = float(inv16pi2)
    c_g2_f = float(Fraction(-19, 6))
    c_gp_f = float(Fraction(41, 6))
    c_yt_self_f = float(Fraction(9, 2))
    c_yt_g2_f = float(Fraction(-9, 4))
    c_yt_gp_f = float(Fraction(-17, 12))
    c_lam_box_f = float(Fraction(3, 8))

    def sm_rhs_f(_t: float, y: List[float]) -> List[float]:
        g3, g2, gp, yt, lam_b = y
        dg3 = inv16pi2_f * (-7 * g3**3)
        dg2 = inv16pi2_f * (c_g2_f * g2**3)
        dgp = inv16pi2_f * (c_gp_f * gp**3)
        dyt = inv16pi2_f * yt * (
            c_yt_self_f * yt**2 - 8 * g3**2 + c_yt_g2_f * g2**2 + c_yt_gp_f * gp**2
        )
        dlam = inv16pi2_f * (
            24 * lam_b**2
            + 12 * lam_b * yt**2
            - 6 * yt**4
            - 3 * lam_b * (3 * g2**2 + gp**2)
            + c_lam_box_f * (2 * g2**4 + (g2**2 + gp**2) ** 2)
        )
        return [dg3, dg2, dgp, dyt, dlam]

    # Disjoint integrator 1: Pure mpmath RK4 + step-halving Richardson (t=0 -> t_Pl -> 40)
    _, _, y_pl_rich, diff_pl_rk4 = rk4_mp_step_halving(sm_rhs_mp, mp.mpf(0), t_pl, y0, 400)
    _, _, y_40_rich, diff_40_rk4 = rk4_mp_step_halving(sm_rhs_mp, t_pl, t_end, y_pl_rich, 40)

    # Find t_cross in pure mpmath by stepping RK4 to locate sign change then bisection
    n_scan = 400
    h_scan = t_end / mp.mpf(n_scan)
    half = mp_frac(1, 2)
    sixth = mp_frac(1, 6)
    t_cur = mp.mpf(0)
    y_cur = list(y0)
    t_lo = mp.mpf(0)
    t_hi = mp.mpf(0)
    y_lo = list(y0)
    found_bracket = False
    for _ in range(n_scan):
        k1 = sm_rhs_mp(t_cur, y_cur)
        k2 = sm_rhs_mp(t_cur + h_scan * half, [y_cur[i] + h_scan * half * k1[i] for i in range(5)])
        k3 = sm_rhs_mp(t_cur + h_scan * half, [y_cur[i] + h_scan * half * k2[i] for i in range(5)])
        k4 = sm_rhs_mp(t_cur + h_scan, [y_cur[i] + h_scan * k3[i] for i in range(5)])
        y_nxt = [
            y_cur[i] + h_scan * sixth * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i])
            for i in range(5)
        ]
        t_nxt = t_cur + h_scan
        if y_cur[4] >= 0 and y_nxt[4] <= 0 and not found_bracket:
            t_lo = t_cur
            t_hi = t_nxt
            y_lo = list(y_cur)
            found_bracket = True
            break
        t_cur = t_nxt
        y_cur = y_nxt

    # Refine t_cross by bisection with Richardson-accurate RK4 from y_lo
    # First get ultra-accurate state at t_lo via RK4 step-halving from 0 -> t_lo
    _, _, y_lo_acc, _ = rk4_mp_step_halving(sm_rhs_mp, mp.mpf(0), t_lo, y0, 300)
    a_t = t_lo
    b_t = t_hi
    for _ in range(60):
        mid_t = (a_t + b_t) * half
        _, _, y_mid, _ = rk4_mp_step_halving(sm_rhs_mp, t_lo, mid_t, y_lo_acc, 4)
        if y_mid[4] > 0:
            a_t = mid_t
        else:
            b_t = mid_t
    t_cross_mp = (a_t + b_t) * half
    mu_cross_mp = mu0 * mp.exp(t_cross_mp)
    log10_mu_cross_mp = mp.log10(mu_cross_mp)

    # Disjoint integrator 2: scipy Radau (implicit stiff solver, NOT DOP853)
    sol_radau = solve_ivp(
        sm_rhs_f,
        [0, 40],
        [float(v) for v in y0],
        method="Radau",
        t_eval=[float(t_pl), 40],
        rtol=float(Fraction(1, 10**13)),
        atol=float(Fraction(1, 10**15)),
        dense_output=True,
    )
    y_pl_radau = [mp.mpf(float(sol_radau.y[i, 0])) for i in range(5)]
    y_40_radau = [mp.mpf(float(sol_radau.y[i, 1])) for i in range(5)]
    t_cross_radau = mp.mpf(
        float(brentq(lambda tv: float(sol_radau.sol(tv)[4]), 10, 20, xtol=float(Fraction(1, 10**14))))
    )
    log10_mu_cross_radau = mp.log10(mu0 * mp.exp(t_cross_radau))

    # Exact analytic 1-loop g_3(M_Pl)
    g3_pl_analytic = (y0[0] ** (-2) + mp.mpf(14) * t_pl * inv16pi2) ** (-half)
    g3_err_rk4 = abs(y_pl_rich[0] - g3_pl_analytic)
    g3_err_radau = abs(y_pl_radau[0] - g3_pl_analytic)
    max_rk4_vs_radau_pl = max(abs(y_pl_rich[i] - y_pl_radau[i]) for i in range(5))
    max_rk4_vs_radau_40 = max(abs(y_40_rich[i] - y_40_radau[i]) for i in range(5))
    t_cross_diff = abs(t_cross_mp - t_cross_radau)

    tol_g3 = mp_frac(1, 10**12)
    tol_ode = mp_frac(1, 10**10)
    passed = bool(
        found_bracket
        and sol_radau.success
        and (mp.mpf(8) < log10_mu_cross_mp < mp.mpf(9))
        and (mp.mpf(13) < t_cross_mp < mp.mpf(15))
        and (y_pl_rich[4] < -mp_frac(3, 100))
        and (g3_err_rk4 < tol_g3)
        and (g3_err_radau < tol_g3)
        and (max_rk4_vs_radau_pl < tol_ode)
        and (max_rk4_vs_radau_40 < tol_ode)
        and (t_cross_diff < tol_ode)
    )

    return {
        "methods": ["mpmath_RK4_Richardson_400_800", "scipy_Radau"],
        "t_Pl": to_pair(t_pl),
        "t_cross_rk4": to_pair(t_cross_mp),
        "t_cross_radau": to_pair(t_cross_radau),
        "t_cross_integrator_diff": to_pair(t_cross_diff),
        "log10_mu_cross_GeV": to_pair(log10_mu_cross_mp),
        "log10_mu_cross_GeV_radau": to_pair(log10_mu_cross_radau),
        "lam_B_at_M_Pl": to_pair(y_pl_rich[4]),
        "lam_B_at_t40": to_pair(y_40_rich[4]),
        "g3_at_M_Pl_rk4": to_pair(y_pl_rich[0]),
        "g3_at_M_Pl_radau": to_pair(y_pl_radau[0]),
        "g3_at_M_Pl_analytic": to_pair(g3_pl_analytic),
        "g3_err_vs_analytic_rk4": to_pair(g3_err_rk4),
        "g3_err_vs_analytic_radau": to_pair(g3_err_radau),
        "rk4_step_halving_diff_M_Pl": to_pair(diff_pl_rk4),
        "rk4_step_halving_diff_t40": to_pair(diff_40_rk4),
        "max_rk4_vs_radau_M_Pl": to_pair(max_rk4_vs_radau_pl),
        "max_rk4_vs_radau_t40": to_pair(max_rk4_vs_radau_40),
        "passed": passed,
    }


# =============================================================================
# TASK OW13-A.2 & B.2: Symbolic Litim f_lam, A2-OW10 Cubic & beta_xi^{grav, bg}
# =============================================================================
def derive_litim_and_solve_gravity_fps() -> Tuple[Dict[str, Any], Dict[str, Any], Dict[str, Any]]:
    """
    Symbolically derive I_litim, f_lam^(dD), f_lam^(LDW), A2-OW10 cubic, and
    beta_xi^(grav, bg) via sympy.integrate & sympy.diff; solve all 5 gravity FPs
    via sympy.real_roots + sympy.Poly.nroots.
    """
    z, eta_N, g, lam, v, u, xi, x = sp.symbols("z eta_N g lam v u xi x", real=True)
    M_g, M_l = sp.symbols("M_g M_l", real=True)

    # 1. Exact 4D Litim threshold integral via sympy.integrate
    I_litim_derived = (
        sp.Rational(1, 2)
        * sp.Rational(1, 16)
        / sp.pi**2
        * sp.integrate(z * (2 - eta_N * (1 - z)), (z, 0, 1))
    )
    I_litim_target = (1 - eta_N / 6) / (32 * sp.pi**2)
    I_litim_exact_zero = sp.simplify(I_litim_derived - I_litim_target) == 0

    # 2. Symbolic derivation of f_lam^(dD) and f_lam^(LDW) via sympy.diff
    lam_eff_v = lam + 8 * sp.pi * g * v
    dv_dD = 10 * I_litim_derived / (1 - 2 * lam_eff_v)
    dv_LDW = I_litim_derived * (
        5 / (1 - 2 * lam_eff_v) + 1 / (1 - sp.Rational(4, 3) * lam_eff_v)
    )
    f_dD_derived = sp.simplify(sp.diff(dv_dD, v).subs(v, 0))
    f_LDW_derived = sp.simplify(sp.diff(dv_LDW, v).subs(v, 0))

    f_dD_target = 5 * g * (1 - eta_N / 6) / (sp.pi * (1 - 2 * lam) ** 2)
    f_dD_eta2_target = 20 * g / (3 * sp.pi * (1 - 2 * lam) ** 2)
    f_LDW_target = (g * (1 - eta_N / 6) / sp.pi) * (
        sp.Rational(5, 2) / (1 - 2 * lam) ** 2
        + sp.Rational(1, 3) / (1 - sp.Rational(4, 3) * lam) ** 2
    )
    f_LDW_eta2_target = (
        10 * g / (3 * sp.pi * (1 - 2 * lam) ** 2)
        + 4 * g / (sp.pi * (3 - 4 * lam) ** 2)
    )

    f_dD_symbolic_match = bool(
        sp.simplify(f_dD_derived - f_dD_target) == 0
        and sp.simplify(f_dD_derived.subs(eta_N, -2) - f_dD_eta2_target) == 0
    )
    f_LDW_symbolic_match = bool(
        sp.simplify(f_LDW_derived - f_LDW_target) == 0
        and sp.simplify(f_LDW_derived.subs(eta_N, -2) - f_LDW_eta2_target) == 0
    )

    f_dD_eta2 = sp.simplify(f_dD_derived.subs(eta_N, -2))
    f_LDW_eta2 = sp.simplify(f_LDW_derived.subs(eta_N, -2))

    # 3. A2-OW10 B_1, B_2, beta_g, beta_lam & symbolic derivation of cubic and beta_xi^{grav, bg}
    u_lam = 1 - 2 * lam
    B1_lam = (1 / (6 * sp.pi)) * (10 / u_lam - 18 / u_lam**2 - 14 + M_g)
    B2_lam = (1 / (6 * sp.pi)) * (-sp.Rational(5, 2) / u_lam + 3 / u_lam**2)
    eta_expr = g * B1_lam / (1 - g * B2_lam)
    beta_g_expr = (2 + eta_expr) * g
    beta_lam_expr = (eta_expr - 2) * lam + (g / (2 * sp.pi)) * (
        5 * (1 - eta_expr / 6) / u_lam - 4 + M_l
    )

    # Derive g*(u) and cubic polynomial in u from beta_g=0 (eta_N=-2), beta_lam=0
    g_fp_sols = sp.solve(sp.Eq(eta_expr, -2), g)
    g_fp_of_lam = sp.simplify(g_fp_sols[0])
    g_fp_of_u = sp.simplify(g_fp_of_lam.subs(lam, (1 - u) / 2))
    g_fp_target_u = -12 * sp.pi * u**2 / ((M_g - 14) * u**2 + 15 * u - 24)
    g_fp_symbolic_match = bool(sp.simplify(g_fp_of_u - g_fp_target_u) == 0)

    eta_at_gfp_is_minus2 = bool(sp.simplify(eta_expr.subs(g, g_fp_of_lam) - (-2)) == 0)
    bl_sub = sp.together(
        sp.simplify(beta_lam_expr.subs(g, g_fp_of_lam)).subs(lam, (1 - u) / 2)
    )
    num_bl, _den_bl = sp.fraction(bl_sub)
    cubic_derived = sp.expand(num_bl)
    cubic_target = 2 * (M_g - 14) * u**3 + (82 - 2 * M_g - 6 * M_l) * u**2 - 118 * u + 48
    # Match up to overall sign/rational scale
    ratio_cubic = sp.simplify(cubic_derived / cubic_target)
    cubic_symbolic_match = bool(eta_at_gfp_is_minus2 and ratio_cubic.is_number and ratio_cubic != 0)

    # Symbolic derivation of beta_xi^{grav, bg} from k d_k Z_N(phi)
    # Z_N(phi) = 1/(16 pi G) - (1/2) xi x (where x = phi^2), lam_eff(x) = lam / (1 - 8 pi g xi x)
    # k d_k Z_N(phi) = -(k^2 / (16 pi)) (B_1(lam_eff) + eta_N B_2(lam_eff))
    # Matching -(1/2) beta_xi x => beta_xi = -2 * d/dx [RHS]|_{x=0}
    lam_eff_x = lam / (1 - 8 * sp.pi * g * xi * x)
    rhs_kdz = -(1 / (16 * sp.pi)) * (
        B1_lam.subs(lam, lam_eff_x) + eta_N * B2_lam.subs(lam, lam_eff_x)
    )
    beta_xi_bg_derived = sp.simplify((-2 * sp.diff(rhs_kdz, x).subs(x, 0)).subs(eta_N, -2))
    beta_xi_bg_target = -g * lam * xi * (11 + 10 * lam) / (sp.pi * (1 - 2 * lam) ** 3)
    beta_xi_bg_symbolic_match = bool(
        sp.simplify(beta_xi_bg_derived - beta_xi_bg_target) == 0
    )
    f_xi_bg_expr = sp.simplify(beta_xi_bg_derived / xi)
    f_xi_bg_at_zero_is_zero = bool(sp.simplify(f_xi_bg_expr.subs(lam, 0)) == 0)

    # Symbolic 2x2 gravity Jacobian for Pure Gravity Litim (2004) benchmark
    J_grav_sym = sp.Matrix([beta_g_expr, beta_lam_expr]).jacobian([g, lam])

    # 4. Solve all 5 gravity fixed points via sympy.real_roots & cross-check sympy.nroots
    spectra = [
        ("pure_gravity_T2", "Pure Gravity T2", 0, 0, 0, 1),
        ("spin10_real10_T2", "Spin(10) real-10 T2", 10, 48, 45, 1),
        ("spin10_real10_T1", "Spin(10) real-10 T1", 10, 48, 45, 2),
        ("ps_412_T2", "PS(4,1,2) T2", 16, 48, 21, 1),
        ("gsm_2h_T2", "G_SM 2H T2", 8, 48, 12, 1),
    ]

    fps_out: Dict[str, Any] = {}
    fps_mp: Dict[str, Dict[str, mp.mpf]] = {}
    all_f_lam_pos = True
    all_residuals_ok = True
    all_unique_phys = True
    all_nroots_agree = True

    for key, label, n_s, n_w, n_v, f_w in spectra:
        mg_val = n_s + f_w * n_w - 4 * n_v
        ml_rat = sp.Rational(n_s - 2 * n_w + 2 * n_v, 2)
        poly_spec = sp.Poly(cubic_target.subs({M_g: mg_val, M_l: ml_rat}), u)

        # Method A: sympy.real_roots (exact isolating intervals -> 65 digits)
        r_roots = sp.real_roots(poly_spec)
        # Method B: sympy.Poly.nroots (all complex roots at 65 digits)
        n_roots = poly_spec.nroots(n=65, maxsteps=200)
        real_nroots = [
            mp.mpf(str(sp.re(nr)))
            for nr in n_roots
            if abs(mp.mpf(str(sp.im(nr)))) < mp_frac(1, 10**45)
        ]

        phys_candidates = []
        for rr in r_roots:
            u_mp = sp_to_mp(rr)
            if u_mp > 0:
                lam_mp = (mp.mpf(1) - u_mp) / mp.mpf(2)
                g_mp = (
                    -mp.mpf(12)
                    * mp.pi
                    * u_mp**2
                    / (mp.mpf(mg_val - 14) * u_mp**2 + mp.mpf(15) * u_mp - mp.mpf(24))
                )
                if g_mp > 0:
                    phys_candidates.append((u_mp, g_mp, lam_mp))

        if len(phys_candidates) != 1:
            all_unique_phys = False
            raise RuntimeError(f"Expected 1 physical gravity FP for {key}, found {len(phys_candidates)}")

        u_star, g_star, lam_star = phys_candidates[0]
        # Cross-check against nroots
        nroot_diff = min(abs(u_star - nr) for nr in real_nroots)
        if nroot_diff >= mp_frac(1, 10**50):
            all_nroots_agree = False

        # Direct evaluation of original beta_g, beta_lam at (g_star, lam_star)
        u_eval = mp.mpf(1) - mp.mpf(2) * lam_star
        b1_val = (mp.mpf(1) / (mp.mpf(6) * mp.pi)) * (
            mp.mpf(10) / u_eval - mp.mpf(18) / u_eval**2 - mp.mpf(14) + mp.mpf(mg_val)
        )
        b2_val = (mp.mpf(1) / (mp.mpf(6) * mp.pi)) * (
            -mp_frac(5, 2) / u_eval + mp.mpf(3) / u_eval**2
        )
        eta_val = g_star * b1_val / (mp.mpf(1) - g_star * b2_val)
        bg_res = (mp.mpf(2) + eta_val) * g_star
        ml_mp = mp_frac(n_s - 2 * n_w + 2 * n_v, 2)
        bl_res = (eta_val - mp.mpf(2)) * lam_star + (g_star / (mp.mpf(2) * mp.pi)) * (
            mp.mpf(5) * (mp.mpf(1) - eta_val / mp.mpf(6)) / u_eval - mp.mpf(4) + ml_mp
        )
        max_res = max(abs(bg_res), abs(bl_res))
        if max_res >= mp_frac(1, 10**50):
            all_residuals_ok = False

        # Evaluate f_lam^(dD), f_lam^(LDW), f_xi^(bg) directly from symbolically derived forms
        f_dD_val = mp.mpf(20) * g_star / (mp.mpf(3) * mp.pi * u_eval**2)
        f_LDW_val = (
            mp.mpf(10) * g_star / (mp.mpf(3) * mp.pi * u_eval**2)
            + mp.mpf(4) * g_star / (mp.pi * (mp.mpf(3) - mp.mpf(4) * lam_star) ** 2)
        )
        f_xi_bg_val = (
            -g_star * lam_star * (mp.mpf(11) + mp.mpf(10) * lam_star)
            / (mp.pi * u_eval**3)
        )

        # Also cross-check f_dD_val, f_LDW_val, f_xi_bg_val directly via sympy subs
        subs_pt = {
            g: sp.Float(mp.nstr(g_star, 60), 60),
            lam: sp.Float(mp.nstr(lam_star, 60), 60),
        }
        f_dD_sp = sp_to_mp(f_dD_eta2.subs(subs_pt))
        f_LDW_sp = sp_to_mp(f_LDW_eta2.subs(subs_pt))
        f_xi_sp = sp_to_mp(f_xi_bg_expr.subs(subs_pt))
        sym_eval_diff = max(
            abs(f_dD_val - f_dD_sp),
            abs(f_LDW_val - f_LDW_sp),
            abs(f_xi_bg_val - f_xi_sp),
        )
        if sym_eval_diff >= mp_frac(1, 10**50):
            all_residuals_ok = False

        if not (f_dD_val > 0 and f_LDW_val > 0):
            all_f_lam_pos = False

        entry: Dict[str, Any] = {
            "label": label,
            "N_S": n_s,
            "N_W": n_w,
            "N_V": n_v,
            "f_W": f_w,
            "M_g": mg_val,
            "M_l": str(ml_rat),
            "num_physical_fps": len(phys_candidates),
            "u_star": to_pair(u_star),
            "g_star": to_pair(g_star),
            "lam_star": to_pair(lam_star),
            "eta_N_at_fp": to_pair(eta_val),
            "max_beta_residual": to_pair(max_res),
            "real_roots_vs_nroots_diff": to_pair(nroot_diff),
            "f_lam_dD": to_pair(f_dD_val),
            "f_lam_LDW": to_pair(f_LDW_val),
            "f_xi_bg": to_pair(f_xi_bg_val),
            "f_lam_both_positive": bool(f_dD_val > 0 and f_LDW_val > 0),
        }

        # For Pure Gravity T2: compute Litim (2004) complex critical exponents via symbolic Jacobian
        if key == "pure_gravity_T2":
            J_pg = J_grav_sym.subs({M_g: mg_val, M_l: ml_rat}).subs(subs_pt)
            J_pg_mp = mp.matrix([
                [sp_to_mp(J_pg[0, 0]), sp_to_mp(J_pg[0, 1])],
                [sp_to_mp(J_pg[1, 0]), sp_to_mp(J_pg[1, 1])],
            ])
            eigs_pg = mp.eig(J_pg_mp, left=False, right=False)
            thetas_pg = [-ev for ev in eigs_pg]
            re_theta = mp.re(thetas_pg[0])
            im_theta = abs(mp.im(thetas_pg[0]))
            litim_bench_passed = bool(
                abs(g_star - mp_frac(70732, 10**5)) < mp_frac(1, 10**5)
                and abs(lam_star - mp_frac(19320, 10**5)) < mp_frac(1, 10**5)
                and abs(re_theta - mp_frac(14753, 10**4)) < mp_frac(1, 10**4)
                and abs(im_theta - mp_frac(30432, 10**4)) < mp_frac(1, 10**4)
                and max_res < mp_frac(1, 10**30)
            )
            entry["litim_2004_benchmark"] = {
                "Re_theta": to_pair(re_theta),
                "Im_theta": to_pair(im_theta),
                "passed": litim_bench_passed,
            }

        fps_out[key] = entry
        fps_mp[key] = {
            "u": u_star,
            "g": g_star,
            "lam": lam_star,
            "f_dD": f_dD_val,
            "f_LDW": f_LDW_val,
            "f_xi_bg": f_xi_bg_val,
        }

    litim_summary = {
        "I_litim_symbolic_exact": I_litim_exact_zero,
        "I_litim_expr": str(sp.simplify(I_litim_derived)),
        "f_lam_dD_symbolic_exact": f_dD_symbolic_match,
        "f_lam_dD_at_eta_minus2_expr": str(f_dD_eta2),
        "f_lam_LDW_symbolic_exact": f_LDW_symbolic_match,
        "f_lam_LDW_at_eta_minus2_expr": str(f_LDW_eta2),
        "g_fp_symbolic_exact": g_fp_symbolic_match,
        "cubic_symbolic_exact": cubic_symbolic_match,
        "all_5_unique_physical_fps": all_unique_phys,
        "all_5_real_roots_agree_nroots": all_nroots_agree,
        "all_5_beta_residuals_lt_1e_50": all_residuals_ok,
        "all_5_f_lam_dD_and_LDW_strictly_positive": all_f_lam_pos,
        "pure_gravity_litim_2004_passed": fps_out["pure_gravity_T2"]["litim_2004_benchmark"]["passed"],
        "gravity_fixed_points": fps_out,
        "passed": bool(
            I_litim_exact_zero
            and f_dD_symbolic_match
            and f_LDW_symbolic_match
            and g_fp_symbolic_match
            and cubic_symbolic_match
            and all_unique_phys
            and all_nroots_agree
            and all_residuals_ok
            and all_f_lam_pos
            and fps_out["pure_gravity_T2"]["litim_2004_benchmark"]["passed"]
        ),
    }

    # Task OW13-B.2 payload (built directly from the same exact symbolic derivation)
    s10_fxi = fps_mp["spin10_real10_T2"]["f_xi_bg"]
    ps_fxi = fps_mp["ps_412_T2"]["f_xi_bg"]
    gsm_fxi = fps_mp["gsm_2h_T2"]["f_xi_bg"]
    all_nonzero_fxi = all(
        abs(fps_mp[k]["f_xi_bg"]) > mp_frac(1, 10**10) for k in fps_mp
    )
    spin10_fxi_bracket = bool(-mp_frac(8, 100) < s10_fxi < -mp_frac(7, 100))
    # Erratum 1 exact bracket for PS(4,1,2) T2: +16/1000 < f_xi^{bg} < +17/1000
    ps412_fxi_bracket_erratum1 = bool(mp_frac(16, 1000) < ps_fxi < mp_frac(17, 1000))
    ps412_g_bracket_erratum1 = bool(
        mp_frac(119, 100) < fps_mp["ps_412_T2"]["g"] < mp_frac(120, 100)
    )
    ps412_lam_bracket_erratum1 = bool(
        -mp_frac(99, 100) < fps_mp["ps_412_T2"]["lam"] < -mp_frac(98, 100)
    )
    gsm_fxi_bracket = bool(-mp_frac(22, 100) < gsm_fxi < -mp_frac(21, 100))

    grav_bg_xi_out = {
        "beta_xi_grav_bg_symbolic_exact": beta_xi_bg_symbolic_match,
        "beta_xi_grav_bg_expr": str(beta_xi_bg_derived),
        "f_xi_bg_at_lam_zero_is_zero": f_xi_bg_at_zero_is_zero,
        "all_5_nonzero_lam_have_nonzero_f_xi_bg": all_nonzero_fxi,
        "spin10_T2_f_xi_bg": to_pair(s10_fxi),
        "spin10_T2_bracket_minus8pct_to_minus7pct": spin10_fxi_bracket,
        "ps_412_T2_f_xi_bg": to_pair(ps_fxi),
        "ps_412_T2_g_star_erratum1_bracket": ps412_g_bracket_erratum1,
        "ps_412_T2_lam_star_erratum1_bracket": ps412_lam_bracket_erratum1,
        "ps_412_T2_bracket_erratum1_16_to_17_permille": ps412_fxi_bracket_erratum1,
        "gsm_2h_T2_f_xi_bg": to_pair(gsm_fxi),
        "gsm_2h_T2_bracket_minus22pct_to_minus21pct": gsm_fxi_bracket,
        "all_5_f_xi_bg": {k: to_pair(fps_mp[k]["f_xi_bg"]) for k in fps_mp},
        "passed": bool(
            beta_xi_bg_symbolic_match
            and f_xi_bg_at_zero_is_zero
            and all_nonzero_fxi
            and spin10_fxi_bracket
            and ps412_fxi_bracket_erratum1
            and ps412_g_bracket_erratum1
            and ps412_lam_bracket_erratum1
            and gsm_fxi_bracket
        ),
    }

    return litim_summary, fps_mp, grav_bg_xi_out


# =============================================================================
# 2H Type-II Symbolic Quartic System (Derived from 8x8 Hessian Tr(H^2))
# =============================================================================
def build_2hdm_symbolic_system() -> Dict[str, Any]:
    """
    Derive the pure-scalar U(1)_PQ-symmetric (lam_5=0) 2HDM quartic beta functions
    from first principles via the 8x8 Hessian matrix H = d^2 V / (d phi_a d phi_b)
    and Tr(H^2), then construct the full 4-coupling beta functions and symbolic 4x4
    Jacobian.
    """
    a1, b1, c1, d1, a2, b2, c2, d2 = sp.symbols("a1 b1 c1 d1 a2 b2 c2 d2", real=True)
    h1, h2 = sp.symbols("h1 h2", real=True)
    l1, l2, l3, l4 = sp.symbols("l1 l2 l3 l4", real=True)
    g2, gp, yt, yb, ytau, f_lam, box_sign = sp.symbols(
        "g2 gp yt yb ytau f_lam box_sign", real=True
    )

    fields = [a1, b1, c1, d1, a2, b2, c2, d2]
    p1p1 = (a1**2 + b1**2 + c1**2 + d1**2) / 2
    p2p2 = (a2**2 + b2**2 + c2**2 + d2**2) / 2
    re12 = (a1 * a2 + b1 * b2 + c1 * c2 + d1 * d2) / 2
    im12 = (a1 * b2 - b1 * a2 + c1 * d2 - d1 * c2) / 2
    p1p2_sq = re12**2 + im12**2

    V_pot = (
        sp.Rational(1, 2) * l1 * p1p1**2
        + sp.Rational(1, 2) * l2 * p2p2**2
        + l3 * p1p1 * p2p2
        + l4 * p1p2_sq
    )
    H_mat = sp.hessian(V_pot, fields)

    # Extract 16 pi^2 beta_{lam_i}^{scalar} from 16 pi^2 dV/dt = (1/2) Tr(H^2)
    H_s1 = H_mat.subs({a1: 0, b1: 0, c1: h1, d1: 0, a2: 0, b2: 0, c2: 0, d2: 0})
    b1_sc = sp.expand(sp.simplify(4 * (H_s1**2).trace() / h1**4))

    H_s2 = H_mat.subs({a1: 0, b1: 0, c1: 0, d1: 0, a2: 0, b2: 0, c2: h2, d2: 0})
    b2_sc = sp.expand(sp.simplify(4 * (H_s2**2).trace() / h2**4))

    H_s3 = H_mat.subs({a1: 0, b1: 0, c1: h1, d1: 0, a2: h2, b2: 0, c2: 0, d2: 0})
    tr_s3 = sp.expand((H_s3**2).trace())
    b3_sc = sp.expand(2 * tr_s3.coeff(h1**2 * h2**2))

    H_s4 = H_mat.subs({a1: 0, b1: 0, c1: h1, d1: 0, a2: 0, b2: 0, c2: h2, d2: 0})
    tr_s4 = sp.expand((H_s4**2).trace())
    b34_sc = sp.expand(2 * tr_s4.coeff(h1**2 * h2**2))
    b4_sc = sp.expand(b34_sc - b3_sc)

    # Verify sum-of-squares positivity of the cross-coupling contribution to beta_{lam_1}
    cross_sos_identity = bool(
        sp.simplify((b1_sc - 12 * l1**2) - (2 * l3**2 + 2 * (l3 + l4) ** 2)) == 0
    )

    # Verify canonical 2HDM scalar formulas match Hessian derivation identically
    hessian_matches_canonical = bool(
        sp.simplify(b1_sc - (12 * l1**2 + 4 * l3**2 + 4 * l3 * l4 + 2 * l4**2)) == 0
        and sp.simplify(b2_sc - (12 * l2**2 + 4 * l3**2 + 4 * l3 * l4 + 2 * l4**2)) == 0
        and sp.simplify(
            b3_sc - ((l1 + l2) * (6 * l3 + 2 * l4) + 4 * l3**2 + 2 * l4**2)
        )
        == 0
        and sp.simplify(b4_sc - (2 * (l1 + l2) * l4 + 8 * l3 * l4 + 4 * l4**2)) == 0
    )

    inv16 = 1 / (16 * sp.pi**2)
    b1_mat = inv16 * (
        b1_sc
        + l1 * (12 * yb**2 + 4 * ytau**2 - 9 * g2**2 - 3 * gp**2)
        - 12 * yb**4
        - 4 * ytau**4
        + box_sign * sp.Rational(3, 4) * (3 * g2**4 + 2 * g2**2 * gp**2 + gp**4)
    )
    b2_mat = inv16 * (
        b2_sc
        + l2 * (12 * yt**2 - 9 * g2**2 - 3 * gp**2)
        - 12 * yt**4
        + sp.Rational(3, 4) * (3 * g2**4 + 2 * g2**2 * gp**2 + gp**4)
    )
    b3_mat = inv16 * (
        b3_sc
        + l3 * (6 * yt**2 + 6 * yb**2 + 2 * ytau**2 - 9 * g2**2 - 3 * gp**2)
        - 12 * yt**2 * yb**2
        + sp.Rational(3, 4) * (3 * g2**4 - 2 * g2**2 * gp**2 + gp**4)
    )
    b4_mat = inv16 * (
        b4_sc
        + l4 * (6 * yt**2 + 6 * yb**2 + 2 * ytau**2 - 9 * g2**2 - 3 * gp**2)
        + 12 * yt**2 * yb**2
        + 3 * g2**2 * gp**2
    )

    B_full = sp.Matrix([
        b1_mat + f_lam * l1,
        b2_mat + f_lam * l2,
        b3_mat + f_lam * l3,
        b4_mat + f_lam * l4,
    ])
    J_full = B_full.jacobian([l1, l2, l3, l4])

    args = (l1, l2, l3, l4, g2, gp, yt, yb, ytau, f_lam, box_sign)
    B_fn = sp.lambdify(args, B_full, modules="mpmath")
    J_fn = sp.lambdify(args, J_full, modules="mpmath")

    return {
        "symbols": {
            "l1": l1,
            "l2": l2,
            "l3": l3,
            "l4": l4,
            "g2": g2,
            "gp": gp,
            "yt": yt,
            "yb": yb,
            "ytau": ytau,
            "f_lam": f_lam,
            "box_sign": box_sign,
        },
        "b1_mat": b1_mat,
        "B_full": B_full,
        "J_full": J_full,
        "B_fn": B_fn,
        "J_fn": J_fn,
        "hessian_matches_canonical": hessian_matches_canonical,
        "cross_sos_identity": cross_sos_identity,
    }


def solve_4d_quartic_fp(
    sys2h: Dict[str, Any],
    f_lam_val: mp.mpf,
    g_uv: mp.mpf,
    yt_val: mp.mpf,
    yb_val: mp.mpf,
    ytau_val: mp.mpf,
    box_sign_val: int = 1,
) -> Dict[str, Any]:
    """
    Solve the full 4-coupling coupled nonlinear system beta_{lam_i} = 0 using
    sympy symbolic Jacobian + damped Newton in 60-digit mpmath.
    """
    g2_val = g_uv
    gp_val = mp.sqrt(mp_frac(3, 5)) * g_uv
    B_fn = sys2h["B_fn"]
    J_fn = sys2h["J_fn"]
    bs = mp.mpf(box_sign_val)

    x = [mp.mpf(0), mp.mpf(0), mp.mpf(0), mp.mpf(0)]
    converged = False
    iters = 0
    for it in range(1, 81):
        iters = it
        Fv = mp.matrix(B_fn(x[0], x[1], x[2], x[3], g2_val, gp_val, yt_val, yb_val, ytau_val, f_lam_val, bs))
        res = max(abs(Fv[i]) for i in range(4))
        if res < mp_frac(1, 10**52):
            converged = True
            break
        Jv = mp.matrix(J_fn(x[0], x[1], x[2], x[3], g2_val, gp_val, yt_val, yb_val, ytau_val, f_lam_val, bs))
        dx = mp.lu_solve(Jv, -Fv)
        # Backtracking line-search damping for robustness
        alpha = mp.mpf(1)
        for _ in range(12):
            x_try = [x[i] + alpha * dx[i] for i in range(4)]
            F_try = mp.matrix(
                B_fn(x_try[0], x_try[1], x_try[2], x_try[3], g2_val, gp_val, yt_val, yb_val, ytau_val, f_lam_val, bs)
            )
            res_try = max(abs(F_try[i]) for i in range(4))
            if res_try < res or alpha < mp_frac(1, 1000):
                x = x_try
                break
            alpha = alpha * mp_frac(1, 2)

    Fv_fin = mp.matrix(B_fn(x[0], x[1], x[2], x[3], g2_val, gp_val, yt_val, yb_val, ytau_val, f_lam_val, bs))
    residual = max(abs(Fv_fin[i]) for i in range(4))
    Jv_fin = mp.matrix(J_fn(x[0], x[1], x[2], x[3], g2_val, gp_val, yt_val, yb_val, ytau_val, f_lam_val, bs))
    eigs = mp.eig(Jv_fin, left=False, right=False)
    thetas = sorted([-mp.re(ev) for ev in eigs])
    max_imag_eig = max(abs(mp.im(ev)) for ev in eigs)
    max_abs_lam = max(abs(v) for v in x)

    # Tree-level BFB checks
    bfb_1 = x[0] > 0
    bfb_2 = x[1] > 0
    if bfb_1 and bfb_2:
        sq12 = mp.sqrt(x[0] * x[1])
        bfb_3_val = x[2] + sq12
        bfb_4_val = x[2] + x[3] + sq12
        bfb_all = bool(bfb_1 and bfb_2 and (bfb_3_val > 0) and (bfb_4_val > 0))
    else:
        bfb_3_val = None
        bfb_4_val = None
        bfb_all = False

    return {
        "converged": bool(converged and residual < mp_frac(1, 10**40)),
        "iterations": iters,
        "lam_star_mp": x,
        "lam_star": [to_pair(v) for v in x],
        "residual": to_pair(residual),
        "thetas": [to_pair(t) for t in thetas],
        "thetas_mp": thetas,
        "max_imag_eig": to_pair(max_imag_eig),
        "all_thetas_negative": bool(all(t < 0 for t in thetas)),
        "all_thetas_positive": bool(all(t > 0 for t in thetas)),
        "max_abs_lam": to_pair(max_abs_lam),
        "all_abs_lam_lt_3pct": bool(max_abs_lam < mp_frac(3, 100)),
        "bfb": {
            "lam_1_pos": bool(bfb_1),
            "lam_2_pos": bool(bfb_2),
            "lam_3_plus_sqrt_l1l2": to_pair(bfb_3_val) if bfb_3_val is not None else None,
            "lam_3_plus_lam_4_plus_sqrt_l1l2": to_pair(bfb_4_val) if bfb_4_val is not None else None,
            "all_4_bfb_positive": bfb_all,
        },
    }


def run_quartic_fps_and_collision(
    sys2h: Dict[str, Any],
    fps_mp: Dict[str, Dict[str, mp.mpf]],
) -> Tuple[Dict[str, Any], Dict[str, List[mp.mpf]]]:
    """
    Verify analytic f_crit collision wall, G_SM 2H complex root collision,
    and full 4-coupling UV fixed points across Spin(10) T2/T1 and PS(4,1,2) T2.
    """
    s = sys2h["symbols"]
    g_uv_sym = sp.Symbol("g_UV", positive=True)
    f_sym = sp.Symbol("f_lam", real=True)
    l1_sym = s["l1"]

    # 1. Exact symbolic derivation of f_crit(g_UV) at y_b = y_tau = 0, l3 = l4 = 0
    b1_dec = sp.expand(
        16
        * sp.pi**2
        * sys2h["B_full"][0].subs({
            s["l3"]: 0,
            s["l4"]: 0,
            s["yb"]: 0,
            s["ytau"]: 0,
            s["g2"]: g_uv_sym,
            s["gp"]: sp.sqrt(sp.Rational(3, 5)) * g_uv_sym,
            s["f_lam"]: f_sym,
            s["box_sign"]: 1,
        })
    )
    disc_sym = sp.discriminant(sp.Poly(b1_dec, l1_sym))
    f_crit_sols = sp.solve(sp.Eq(disc_sym, 0), f_sym)
    pos_sols = [
        sol
        for sol in f_crit_sols
        if sp.im(sp.N(sol.subs(g_uv_sym, 1))) == 0
        and sp.re(sp.N(sol.subs(g_uv_sym, 1))) > 0
    ]
    f_crit_derived = sp.simplify(pos_sols[0])
    f_crit_target = (54 + 6 * sp.sqrt(114)) * g_uv_sym**2 / (80 * sp.pi**2)
    f_crit_symbolic_match = bool(sp.simplify(f_crit_derived - f_crit_target) == 0)

    g_uv = mp_frac(13, 25)
    yt_uv = mp_frac(11, 20)
    yb_low = mp_frac(1, 100)
    yb_high = mp_frac(9, 20)

    f_crit_val = sp_to_mp(f_crit_derived.subs(g_uv_sym, sp.Rational(13, 25)))
    f_crit_bracket = bool(mp_frac(4, 100) < f_crit_val < mp_frac(41, 1000))
    yb_crit_val = (mp_frac(171, 600) ** mp_frac(1, 4)) * g_uv
    yb_regime_check = bool(yb_low < yb_crit_val < yb_high)

    # 2. G_SM 2H T2 collision wall check at y_b = 1/100 in BOTH dD and LDW
    gsm_dD = fps_mp["gsm_2h_T2"]["f_dD"]
    gsm_LDW = fps_mp["gsm_2h_T2"]["f_LDW"]
    gsm_dD_below = bool(gsm_dD < mp_frac(34, 1000) < f_crit_val)
    gsm_LDW_below = bool(gsm_LDW < mp_frac(22, 1000) < f_crit_val)

    b1_sym_dec = sp.expand(
        16 * sp.pi**2 * sys2h["B_full"][0].subs({s["l3"]: 0, s["l4"]: 0})
    )
    disc_b1_exact_sym = sp.expand(sp.discriminant(sp.Poly(b1_sym_dec, l1_sym)))

    gsm_collision_details: Dict[str, Any] = {}
    for gname, f_val in [("dD", gsm_dD), ("LDW", gsm_LDW)]:
        subs_gsm = {
            s["yb"]: sp.Rational(1, 100),
            s["ytau"]: sp.Rational(1, 100),
            s["g2"]: sp.Rational(13, 25),
            s["gp"]: sp.sqrt(sp.Rational(3, 5)) * sp.Rational(13, 25),
            s["f_lam"]: sp.Float(mp.nstr(f_val, 60), 60),
            s["box_sign"]: 1,
        }
        l1_c = sp.Symbol("l1_c")
        disc_gsm = sp_to_mp(disc_b1_exact_sym.subs(subs_gsm))
        b1_gsm_num = sp.N(b1_sym_dec.subs(subs_gsm).subs(l1_sym, l1_c), 65)
        roots_gsm = sp.solve(sp.Eq(b1_gsm_num, 0), l1_c)
        re_root = sp_to_mp(sp.re(roots_gsm[0]))
        im_root = abs(sp_to_mp(sp.im(roots_gsm[0])))
        gsm_collision_details[gname] = {
            "f_lam": to_pair(f_val),
            "f_lam_lt_f_crit": bool(f_val < f_crit_val),
            "discriminant_lam1_y_b_1pct": to_pair(disc_gsm),
            "discriminant_strictly_negative": bool(disc_gsm < 0),
            "complex_root_Re": to_pair(re_root),
            "complex_root_abs_Im": to_pair(im_root),
            "complex_pair_confirmed": bool(disc_gsm < 0 and im_root > mp_frac(1, 1000)),
        }

    # 3. Verify Spin(10) T2, Spin(10) T1, PS(4,1,2) T2 all lie strictly above f_crit in BOTH gauges
    above_fcrit_spectra = ["spin10_real10_T2", "spin10_real10_T1", "ps_412_T2"]
    all_above_fcrit = all(
        fps_mp[k]["f_dD"] > f_crit_val and fps_mp[k]["f_LDW"] > f_crit_val
        for k in above_fcrit_spectra
    )
    spin10_dD_gt_67pct = bool(fps_mp["spin10_real10_T2"]["f_dD"] > mp_frac(67, 100))
    spin10_LDW_gt_37pct = bool(fps_mp["spin10_real10_T2"]["f_LDW"] > mp_frac(37, 100))

    # 4. Solve full 4-coupling system across all 12 combinations
    solutions_out: Dict[str, Any] = {}
    saved_lams_mp: Dict[str, List[mp.mpf]] = {}
    all_12_converged = True
    all_12_thetas_neg = True

    for skey in above_fcrit_spectra:
        for gname, fkey in [("dD", "f_dD"), ("LDW", "f_LDW")]:
            for yname, yb_v in [("low_yb", yb_low), ("high_yb", yb_high)]:
                tag = f"{skey}_{gname}_{yname}"
                res = solve_4d_quartic_fp(sys2h, fps_mp[skey][fkey], g_uv, yt_uv, yb_v, yb_v)
                saved_lams_mp[tag] = res["lam_star_mp"]
                if not res["converged"]:
                    all_12_converged = False
                if not res["all_thetas_negative"]:
                    all_12_thetas_neg = False
                solutions_out[tag] = {
                    k: v for k, v in res.items() if k not in ("lam_star_mp", "thetas_mp")
                }

    # Card line 40 checks:
    # Spin(10) T2 (both dD and LDW, both y_b = 1/100 and y_b = 9/20) AND PS(4,1,2) T2 (dD canonical gauge)
    # Note: we also report PS(4,1,2) T2 LDW high_yb honestly (max|lam| ~ 0.03061 > 0.03)!
    card_line40_keys = [
        "spin10_real10_T2_dD_low_yb",
        "spin10_real10_T2_dD_high_yb",
        "spin10_real10_T2_LDW_low_yb",
        "spin10_real10_T2_LDW_high_yb",
        "ps_412_T2_dD_low_yb",
        "ps_412_T2_dD_high_yb",
    ]
    card_line40_all_thetas_neg = all(solutions_out[k]["all_thetas_negative"] for k in card_line40_keys)
    card_line40_all_lam_lt_3pct = all(solutions_out[k]["all_abs_lam_lt_3pct"] for k in card_line40_keys)

    # Card line 41 check: Spin(10) T2 with y_b = 9/20 satisfies ALL 4 BFB conditions
    spin10_T2_dD_high_bfb = solutions_out["spin10_real10_T2_dD_high_yb"]["bfb"]["all_4_bfb_positive"]
    spin10_T2_LDW_high_bfb = solutions_out["spin10_real10_T2_LDW_high_yb"]["bfb"]["all_4_bfb_positive"]

    passed = bool(
        sys2h["hessian_matches_canonical"]
        and sys2h["cross_sos_identity"]
        and f_crit_symbolic_match
        and f_crit_bracket
        and yb_regime_check
        and gsm_dD_below
        and gsm_LDW_below
        and gsm_collision_details["dD"]["complex_pair_confirmed"]
        and gsm_collision_details["LDW"]["complex_pair_confirmed"]
        and all_above_fcrit
        and spin10_dD_gt_67pct
        and spin10_LDW_gt_37pct
        and all_12_converged
        and all_12_thetas_neg
        and card_line40_all_thetas_neg
        and card_line40_all_lam_lt_3pct
        and spin10_T2_dD_high_bfb
        and spin10_T2_LDW_high_bfb
    )

    out = {
        "hessian_derivation_matches_canonical": sys2h["hessian_matches_canonical"],
        "cross_term_sum_of_squares_positive_identity": sys2h["cross_sos_identity"],
        "f_crit_symbolic_exact": f_crit_symbolic_match,
        "f_crit_expr": str(f_crit_derived),
        "f_crit_at_g_UV": to_pair(f_crit_val),
        "f_crit_in_4pct_to_41permille": f_crit_bracket,
        "y_b_crit": to_pair(yb_crit_val),
        "y_b_regimes_bracket_y_b_crit": yb_regime_check,
        "gsm_2h_dD_lt_34permille_lt_f_crit": gsm_dD_below,
        "gsm_2h_LDW_lt_22permille_lt_f_crit": gsm_LDW_below,
        "gsm_2h_collision_wall": gsm_collision_details,
        "all_3_gut_ps_spectra_above_f_crit_both_gauges": all_above_fcrit,
        "spin10_T2_f_dD_gt_67pct": spin10_dD_gt_67pct,
        "spin10_T2_f_LDW_gt_37pct": spin10_LDW_gt_37pct,
        "all_12_4d_fps_converged_lt_1e_40": all_12_converged,
        "all_12_4d_fps_all_thetas_negative": all_12_thetas_neg,
        "card_line40_all_thetas_negative": card_line40_all_thetas_neg,
        "card_line40_all_abs_lam_lt_3pct": card_line40_all_lam_lt_3pct,
        "ps_412_T2_LDW_high_yb_abs_lam_lt_3pct_diagnostic": solutions_out["ps_412_T2_LDW_high_yb"]["all_abs_lam_lt_3pct"],
        "spin10_T2_dD_high_yb_all_4_bfb_positive": spin10_T2_dD_high_bfb,
        "spin10_T2_LDW_high_yb_all_4_bfb_positive": spin10_T2_LDW_high_bfb,
        "fixed_points_4d": solutions_out,
        "passed": passed,
    }
    return out, saved_lams_mp


# =============================================================================
# TASK OW13-A.3: Downward 1-Loop 2H Type-II RGE (t = 0 -> -38)
# =============================================================================
def run_downward_2h_rge(
    saved_lams_mp: Dict[str, List[mp.mpf]],
) -> Tuple[Dict[str, Any], Dict[str, List[mp.mpf]]]:
    """
    Integrate the full 10-coupling 2H Type-II RGE downward from t = 0 to t = -38
    via BOTH pure mpmath RK4+Richardson AND scipy Radau.
    """
    g_uv = mp_frac(13, 25)
    gp_uv = mp.sqrt(mp_frac(3, 5)) * g_uv
    yt_uv = mp_frac(11, 20)
    yb_high = mp_frac(9, 20)
    yb_low = mp_frac(1, 100)
    t_ir = mp.mpf(-38)

    inv16 = mp.mpf(1) / (mp.mpf(16) * mp.pi**2)
    c9_2 = mp_frac(9, 2)
    c1_2 = mp_frac(1, 2)
    c9_4 = mp_frac(9, 4)
    c17_12 = mp_frac(17, 12)
    c5_12 = mp_frac(5, 12)
    c5_2 = mp_frac(5, 2)
    c15_4 = mp_frac(15, 4)
    c3_4 = mp_frac(3, 4)

    def rhs_2h_mp(_t: mp.mpf, y: List[mp.mpf]) -> List[mp.mpf]:
        g3, g2, gp, yt, yb, ytau, l1, l2, l3, l4 = y
        dg3 = inv16 * (-mp.mpf(7) * g3**3)
        dg2 = inv16 * (-mp.mpf(3) * g2**3)
        dgp = inv16 * (mp.mpf(7) * gp**3)
        dyt = inv16 * yt * (
            c9_2 * yt**2 + c1_2 * yb**2 - mp.mpf(8) * g3**2 - c9_4 * g2**2 - c17_12 * gp**2
        )
        dyb = inv16 * yb * (
            c9_2 * yb**2 + c1_2 * yt**2 + ytau**2 - mp.mpf(8) * g3**2 - c9_4 * g2**2 - c5_12 * gp**2
        )
        dytau = inv16 * ytau * (
            c5_2 * ytau**2 + mp.mpf(3) * yb**2 - c9_4 * g2**2 - c15_4 * gp**2
        )
        dl1 = inv16 * (
            mp.mpf(12) * l1**2
            + mp.mpf(4) * l3**2
            + mp.mpf(4) * l3 * l4
            + mp.mpf(2) * l4**2
            + l1 * (mp.mpf(12) * yb**2 + mp.mpf(4) * ytau**2 - mp.mpf(9) * g2**2 - mp.mpf(3) * gp**2)
            - mp.mpf(12) * yb**4
            - mp.mpf(4) * ytau**4
            + c3_4 * (mp.mpf(3) * g2**4 + mp.mpf(2) * g2**2 * gp**2 + gp**4)
        )
        dl2 = inv16 * (
            mp.mpf(12) * l2**2
            + mp.mpf(4) * l3**2
            + mp.mpf(4) * l3 * l4
            + mp.mpf(2) * l4**2
            + l2 * (mp.mpf(12) * yt**2 - mp.mpf(9) * g2**2 - mp.mpf(3) * gp**2)
            - mp.mpf(12) * yt**4
            + c3_4 * (mp.mpf(3) * g2**4 + mp.mpf(2) * g2**2 * gp**2 + gp**4)
        )
        dl3 = inv16 * (
            (l1 + l2) * (mp.mpf(6) * l3 + mp.mpf(2) * l4)
            + mp.mpf(4) * l3**2
            + mp.mpf(2) * l4**2
            + l3 * (
                mp.mpf(6) * yt**2
                + mp.mpf(6) * yb**2
                + mp.mpf(2) * ytau**2
                - mp.mpf(9) * g2**2
                - mp.mpf(3) * gp**2
            )
            - mp.mpf(12) * yt**2 * yb**2
            + c3_4 * (mp.mpf(3) * g2**4 - mp.mpf(2) * g2**2 * gp**2 + gp**4)
        )
        dl4 = inv16 * (
            mp.mpf(2) * (l1 + l2) * l4
            + mp.mpf(8) * l3 * l4
            + mp.mpf(4) * l4**2
            + l4 * (
                mp.mpf(6) * yt**2
                + mp.mpf(6) * yb**2
                + mp.mpf(2) * ytau**2
                - mp.mpf(9) * g2**2
                - mp.mpf(3) * gp**2
            )
            + mp.mpf(12) * yt**2 * yb**2
            + mp.mpf(3) * g2**2 * gp**2
        )
        return [dg3, dg2, dgp, dyt, dyb, dytau, dl1, dl2, dl3, dl4]

    inv16_f = float(inv16)
    c9_2_f = float(Fraction(9, 2))
    c1_2_f = float(Fraction(1, 2))
    c9_4_f = float(Fraction(9, 4))
    c17_12_f = float(Fraction(17, 12))
    c5_12_f = float(Fraction(5, 12))
    c5_2_f = float(Fraction(5, 2))
    c15_4_f = float(Fraction(15, 4))
    c3_4_f = float(Fraction(3, 4))

    def rhs_2h_f(_t: float, y: List[float]) -> List[float]:
        g3, g2, gp, yt, yb, ytau, l1, l2, l3, l4 = y
        dg3 = inv16_f * (-7 * g3**3)
        dg2 = inv16_f * (-3 * g2**3)
        dgp = inv16_f * (7 * gp**3)
        dyt = inv16_f * yt * (c9_2_f * yt**2 + c1_2_f * yb**2 - 8 * g3**2 - c9_4_f * g2**2 - c17_12_f * gp**2)
        dyb = inv16_f * yb * (c9_2_f * yb**2 + c1_2_f * yt**2 + ytau**2 - 8 * g3**2 - c9_4_f * g2**2 - c5_12_f * gp**2)
        dytau = inv16_f * ytau * (c5_2_f * ytau**2 + 3 * yb**2 - c9_4_f * g2**2 - c15_4_f * gp**2)
        dl1 = inv16_f * (
            12 * l1**2 + 4 * l3**2 + 4 * l3 * l4 + 2 * l4**2
            + l1 * (12 * yb**2 + 4 * ytau**2 - 9 * g2**2 - 3 * gp**2)
            - 12 * yb**4 - 4 * ytau**4
            + c3_4_f * (3 * g2**4 + 2 * g2**2 * gp**2 + gp**4)
        )
        dl2 = inv16_f * (
            12 * l2**2 + 4 * l3**2 + 4 * l3 * l4 + 2 * l4**2
            + l2 * (12 * yt**2 - 9 * g2**2 - 3 * gp**2)
            - 12 * yt**4
            + c3_4_f * (3 * g2**4 + 2 * g2**2 * gp**2 + gp**4)
        )
        dl3 = inv16_f * (
            (l1 + l2) * (6 * l3 + 2 * l4) + 4 * l3**2 + 2 * l4**2
            + l3 * (6 * yt**2 + 6 * yb**2 + 2 * ytau**2 - 9 * g2**2 - 3 * gp**2)
            - 12 * yt**2 * yb**2
            + c3_4_f * (3 * g2**4 - 2 * g2**2 * gp**2 + gp**4)
        )
        dl4 = inv16_f * (
            2 * (l1 + l2) * l4 + 8 * l3 * l4 + 4 * l4**2
            + l4 * (6 * yt**2 + 6 * yb**2 + 2 * ytau**2 - 9 * g2**2 - 3 * gp**2)
            + 12 * yt**2 * yb**2 + 3 * g2**2 * gp**2
        )
        return [dg3, dg2, dgp, dyt, dyb, dytau, dl1, dl2, dl3, dl4]

    # Exact 1-loop analytic gauge couplings at t = -38 for ODE verification
    g3_ir_exact = (g_uv ** (-2) - mp.mpf(2) * (-mp.mpf(7)) * t_ir * inv16) ** (-c1_2)
    g2_ir_exact = (g_uv ** (-2) - mp.mpf(2) * (-mp.mpf(3)) * t_ir * inv16) ** (-c1_2)
    gp_ir_exact = (gp_uv ** (-2) - mp.mpf(2) * mp.mpf(7) * t_ir * inv16) ** (-c1_2)

    scenarios = [
        ("high_yb_spin10_T2_dD", yb_high, saved_lams_mp["spin10_real10_T2_dD_high_yb"]),
        ("high_yb_exact_zero", yb_high, [mp.mpf(0), mp.mpf(0), mp.mpf(0), mp.mpf(0)]),
        ("low_yb_spin10_T2_dD", yb_low, saved_lams_mp["spin10_real10_T2_dD_low_yb"]),
        ("low_yb_exact_zero", yb_low, [mp.mpf(0), mp.mpf(0), mp.mpf(0), mp.mpf(0)]),
    ]

    names_10 = ["g_3", "g_2", "g_p", "y_t", "y_b", "y_tau", "lam_1", "lam_2", "lam_3", "lam_4"]
    trajs_out: Dict[str, Any] = {}
    ir_states_mp: Dict[str, List[mp.mpf]] = {}
    all_integrators_agree = True
    all_gauge_exact_ok = True

    for sc_name, yb_v, lams_uv in scenarios:
        y0 = [g_uv, g_uv, gp_uv, yt_uv, yb_v, yb_v] + list(lams_uv)
        _, _, yf_rich, diff_rk4 = rk4_mp_step_halving(rhs_2h_mp, mp.mpf(0), t_ir, y0, 400)
        sol_rad = solve_ivp(
            rhs_2h_f,
            [0, -38],
            [float(v) for v in y0],
            method="Radau",
            rtol=float(Fraction(1, 10**13)),
            atol=float(Fraction(1, 10**15)),
        )
        yf_rad = [mp.mpf(float(sol_rad.y[i, -1])) for i in range(10)]
        max_rk4_vs_rad = max(abs(yf_rich[i] - yf_rad[i]) for i in range(10))
        if (not sol_rad.success) or max_rk4_vs_rad >= mp_frac(1, 10**10):
            all_integrators_agree = False

        gauge_err = max(
            abs(yf_rich[0] - g3_ir_exact),
            abs(yf_rich[1] - g2_ir_exact),
            abs(yf_rich[2] - gp_ir_exact),
        )
        if gauge_err >= mp_frac(1, 10**12):
            all_gauge_exact_ok = False

        l1_ir, l2_ir, l3_ir, l4_ir = yf_rich[6], yf_rich[7], yf_rich[8], yf_rich[9]
        if l1_ir > 0 and l2_ir > 0:
            sq = mp.sqrt(l1_ir * l2_ir)
            bfb3 = l3_ir + sq
            bfb4 = l3_ir + l4_ir + sq
            bfb_ok = bool(l1_ir > 0 and l2_ir > 0 and bfb3 > 0 and bfb4 > 0)
        else:
            bfb3 = None
            bfb4 = None
            bfb_ok = False

        ir_states_mp[sc_name] = yf_rich
        trajs_out[sc_name] = {
            "couplings_IR": {names_10[i]: to_pair(yf_rich[i]) for i in range(10)},
            "rk4_step_halving_diff": to_pair(diff_rk4),
            "max_rk4_vs_radau_diff": to_pair(max_rk4_vs_rad),
            "max_gauge_analytic_err": to_pair(gauge_err),
            "bfb_IR": {
                "lam_1_pos": bool(l1_ir > 0),
                "lam_2_pos": bool(l2_ir > 0),
                "lam_3_plus_sqrt_l1l2": to_pair(bfb3) if bfb3 is not None else None,
                "lam_3_plus_lam_4_plus_sqrt_l1l2": to_pair(bfb4) if bfb4 is not None else None,
                "all_4_bfb_positive": bfb_ok,
            },
        }

    # Card line 45: high_yb grav vs exact-zero UV comparison
    hg = ir_states_mp["high_yb_spin10_T2_dD"]
    hz = ir_states_mp["high_yb_exact_zero"]
    max_ir_quartic_diff_high = max(abs(hg[i] - hz[i]) for i in range(6, 10))
    high_bfb_grav = trajs_out["high_yb_spin10_T2_dD"]["bfb_IR"]["all_4_bfb_positive"]
    high_bfb_zero = trajs_out["high_yb_exact_zero"]["bfb_IR"]["all_4_bfb_positive"]
    high_diff_lt_5permille = bool(max_ir_quartic_diff_high < mp_frac(5, 1000))

    # Card line 46: low_yb radiative destabilization of H_d (lam_1 < -1/10, lam_2 > 7/10)
    lg = ir_states_mp["low_yb_spin10_T2_dD"]
    lz = ir_states_mp["low_yb_exact_zero"]
    low_grav_destab = bool(lg[6] < -mp_frac(1, 10) and lg[7] > mp_frac(7, 10))
    low_zero_destab = bool(lz[6] < -mp_frac(1, 10) and lz[7] > mp_frac(7, 10))

    passed = bool(
        all_integrators_agree
        and all_gauge_exact_ok
        and high_bfb_grav
        and high_bfb_zero
        and high_diff_lt_5permille
        and low_grav_destab
        and low_zero_destab
    )

    out = {
        "methods": ["mpmath_RK4_Richardson_400_800", "scipy_Radau"],
        "t_UV": 0,
        "t_IR": -38,
        "all_integrators_agree_lt_1e_10": all_integrators_agree,
        "all_gauge_couplings_match_analytic_lt_1e_12": all_gauge_exact_ok,
        "high_yb_grav_vs_zero_max_IR_quartic_diff": to_pair(max_ir_quartic_diff_high),
        "high_yb_max_IR_quartic_diff_lt_5permille": high_diff_lt_5permille,
        "high_yb_all_4_bfb_positive_grav": high_bfb_grav,
        "high_yb_all_4_bfb_positive_zero": high_bfb_zero,
        "low_yb_grav_lam1_lt_minus10pct_and_lam2_gt_70pct": low_grav_destab,
        "low_yb_zero_lam1_lt_minus10pct_and_lam2_gt_70pct": low_zero_destab,
        "trajectories": trajs_out,
        "passed": passed,
    }
    return out, ir_states_mp


# =============================================================================
# TASK OW13-A.4: Exact f_g > 0 Structural Theorem (Spin(10) vs U(1)_Y)
# =============================================================================
def run_fg_structural_theorem() -> Dict[str, Any]:
    """
    Exact Dynkin-index 1-loop gauge beta coefficients and symbolic fixed-point
    stability proof for beta_g = -f_g g + b g^3 / (16 pi^2) with arbitrary f_g > 0.
    """
    t_adj = sp.Integer(8)
    t_16 = sp.Integer(2)
    t_vec10 = sp.Integer(1)
    n_gen = sp.Integer(3)

    b_spin10_real10 = (
        -sp.Rational(11, 3) * t_adj
        + sp.Rational(2, 3) * (n_gen * t_16)
        + sp.Rational(1, 6) * t_vec10
    )
    b_spin10_complex10 = (
        -sp.Rational(11, 3) * t_adj
        + sp.Rational(2, 3) * (n_gen * t_16)
        + sp.Rational(1, 6) * (2 * t_vec10)
    )
    # 2H U(1)_Y: b_{g'} = (4/3)*n_gen*(5/3) + (1/6)*2 = 20/3 + 1/3 = 7; GUT-normalized b_1 = (3/5)*b_{g'}
    b_gp_2h = sp.Rational(4, 3) * n_gen * sp.Rational(5, 3) + sp.Rational(1, 6) * 2
    b_1_2h = sp.Rational(3, 5) * b_gp_2h

    g_s = sp.Symbol("g", real=True)
    f_g_s = sp.Symbol("f_g", positive=True)
    b_pos = sp.Symbol("b_pos", positive=True)
    b_neg = sp.Symbol("b_neg", negative=True)

    # Case 1: b < 0 (Spin(10))
    beta_neg = -f_g_s * g_s + b_neg * g_s**3 / (16 * sp.pi**2)
    sols_neg = sp.solve(sp.Eq(beta_neg, 0), g_s)
    real_sols_neg = [s for s in sols_neg if s.is_real]
    theta_neg_gauss = sp.simplify(-sp.diff(beta_neg, g_s).subs(g_s, 0))
    spin10_only_gaussian = bool(real_sols_neg == [0] and sp.simplify(theta_neg_gauss - f_g_s) == 0)

    # Case 2: b > 0 (U(1)_Y Harst-Reuter)
    beta_pos = -f_g_s * g_s + b_pos * g_s**3 / (16 * sp.pi**2)
    sols_pos = sp.solve(sp.Eq(beta_pos, 0), g_s)
    pos_interactive_sols = [s for s in sols_pos if s.is_positive]
    g1_star = sp.simplify(pos_interactive_sols[0])
    g1_star_sq_target = 16 * sp.pi**2 * f_g_s / b_pos
    theta_pos_hr = sp.simplify(-sp.diff(beta_pos, g_s).subs(g_s, g1_star))
    u1y_unique_hr = bool(
        len(pos_interactive_sols) == 1
        and sp.simplify(g1_star**2 - g1_star_sq_target) == 0
        and sp.simplify(theta_pos_hr - (-2 * f_g_s)) == 0
    )

    coeffs_exact = bool(
        b_spin10_real10 == sp.Rational(-151, 6)
        and b_spin10_complex10 == sp.Integer(-25)
        and b_gp_2h == sp.Integer(7)
        and b_1_2h == sp.Rational(21, 5)
    )

    return {
        "b_spin10_real10": str(b_spin10_real10),
        "b_spin10_complex10": str(b_spin10_complex10),
        "b_gp_2h": str(b_gp_2h),
        "b_1_u1y_2h": str(b_1_2h),
        "exact_rational_coefficients_match": coeffs_exact,
        "spin10_real_fixed_points": [str(s) for s in real_sols_neg],
        "spin10_gaussian_theta_g": str(theta_neg_gauss),
        "spin10_only_gaussian_uv_relevant": spin10_only_gaussian,
        "u1y_interactive_g1_star": str(g1_star),
        "u1y_interactive_theta_g": str(theta_pos_hr),
        "u1y_unique_harst_reuter_uv_irrelevant": u1y_unique_hr,
        "passed": bool(coeffs_exact and spin10_only_gaussian and u1y_unique_hr),
    }


# =============================================================================
# TASK OW13-B.1: 1-Loop 2H Curved-Space (beta_{xi_d}, beta_{xi_u}) & M_xi
# =============================================================================
def run_curved_space_xi_1loop(
    saved_lams_mp: Dict[str, List[mp.mpf]],
    ir_states_mp: Dict[str, List[mp.mpf]],
) -> Dict[str, Any]:
    """
    Symbolically verify vanishing of 1-loop (beta_{xi_d}, beta_{xi_u}) at (1/6, 1/6)
    and compute exact eigenvalues of the 2x2 stability matrix M_xi.
    """
    xi_d, xi_u = sp.symbols("xi_d xi_u", real=True)
    l1, l2, l3, l4, g2, gp, yt, yb, ytau = sp.symbols("l1 l2 l3 l4 g2 gp yt yb ytau", real=True)

    b_xid_16 = (xi_d - sp.Rational(1, 6)) * (
        6 * l1 + 6 * yb**2 + 2 * ytau**2 - sp.Rational(9, 2) * g2**2 - sp.Rational(3, 2) * gp**2
    ) + (xi_u - sp.Rational(1, 6)) * (4 * l3 + 2 * l4)
    b_xiu_16 = (xi_u - sp.Rational(1, 6)) * (
        6 * l2 + 6 * yt**2 - sp.Rational(9, 2) * g2**2 - sp.Rational(3, 2) * gp**2
    ) + (xi_d - sp.Rational(1, 6)) * (4 * l3 + 2 * l4)

    vanish_sym = bool(
        sp.simplify(b_xid_16.subs({xi_d: sp.Rational(1, 6), xi_u: sp.Rational(1, 6)})) == 0
        and sp.simplify(b_xiu_16.subs({xi_d: sp.Rational(1, 6), xi_u: sp.Rational(1, 6)})) == 0
    )

    M_xi_sym = sp.Matrix([b_xid_16, b_xiu_16]).jacobian([xi_d, xi_u])
    M_fn = sp.lambdify((l1, l2, l3, l4, g2, gp, yt, yb, ytau), M_xi_sym, modules="mpmath")
    b_fn = sp.lambdify((xi_d, xi_u, l1, l2, l3, l4, g2, gp, yt, yb, ytau), [b_xid_16, b_xiu_16], modules="mpmath")

    g_uv = mp_frac(13, 25)
    gp_uv = mp.sqrt(mp_frac(3, 5)) * g_uv
    yt_uv = mp_frac(11, 20)
    yb_low = mp_frac(1, 100)
    yb_high = mp_frac(9, 20)
    inv16 = mp.mpf(1) / (mp.mpf(16) * mp.pi**2)
    conformal = mp_frac(1, 6)

    def eval_point(
        g2_v: mp.mpf,
        gp_v: mp.mpf,
        yt_v: mp.mpf,
        yb_v: mp.mpf,
        ytau_v: mp.mpf,
        lams: List[mp.mpf],
    ) -> Dict[str, Any]:
        b_conf = b_fn(conformal, conformal, lams[0], lams[1], lams[2], lams[3], g2_v, gp_v, yt_v, yb_v, ytau_v)
        res_conf = max(abs(b_conf[0] * inv16), abs(b_conf[1] * inv16))
        M_mat = mp.matrix(M_fn(lams[0], lams[1], lams[2], lams[3], g2_v, gp_v, yt_v, yb_v, ytau_v))
        # Exact symmetric 2x2 eigenvalues + cross-check with mp.eig
        a_m, b_m, c_m, d_m = M_mat[0, 0], M_mat[0, 1], M_mat[1, 0], M_mat[1, 1]
        tr_m = a_m + d_m
        disc_m = mp.sqrt((a_m - d_m) ** 2 + mp.mpf(4) * b_m * c_m)
        e1 = (tr_m - disc_m) / mp.mpf(2)
        e2 = (tr_m + disc_m) / mp.mpf(2)
        eigs_num = sorted([mp.re(ev) for ev in mp.eig(M_mat, left=False, right=False)])
        eig_cross_diff = max(abs(e1 - eigs_num[0]), abs(e2 - eigs_num[1]))
        return {
            "conformal_beta_residual": to_pair(res_conf),
            "M_xi": [
                [to_pair(a_m), to_pair(b_m)],
                [to_pair(c_m), to_pair(d_m)],
            ],
            "eig_1": to_pair(e1),
            "eig_2": to_pair(e2),
            "eig_1_mp": e1,
            "eig_2_mp": e2,
            "eig_formula_vs_mp_eig_diff": to_pair(eig_cross_diff),
            "is_saddle": bool(e1 < 0 < e2),
            "is_double_ir_attractive": bool(0 < e1 < e2),
        }

    ir_hg = ir_states_mp["high_yb_spin10_T2_dD"]
    ir_hz = ir_states_mp["high_yb_exact_zero"]

    pt_uv_low = eval_point(g_uv, gp_uv, yt_uv, yb_low, yb_low, saved_lams_mp["spin10_real10_T2_dD_low_yb"])
    pt_uv_high = eval_point(g_uv, gp_uv, yt_uv, yb_high, yb_high, saved_lams_mp["spin10_real10_T2_dD_high_yb"])
    pt_uv_low_ldw = eval_point(g_uv, gp_uv, yt_uv, yb_low, yb_low, saved_lams_mp["spin10_real10_T2_LDW_low_yb"])
    pt_uv_high_ldw = eval_point(g_uv, gp_uv, yt_uv, yb_high, yb_high, saved_lams_mp["spin10_real10_T2_LDW_high_yb"])
    pt_ir_hg = eval_point(ir_hg[1], ir_hg[2], ir_hg[3], ir_hg[4], ir_hg[5], ir_hg[6:10])
    pt_ir_hz = eval_point(ir_hz[1], ir_hz[2], ir_hz[3], ir_hz[4], ir_hz[5], ir_hz[6:10])

    all_pts = [pt_uv_low, pt_uv_high, pt_uv_low_ldw, pt_uv_high_ldw, pt_ir_hg, pt_ir_hz]
    all_conf_res_ok = all(
        mp.mpf(p["conformal_beta_residual"]["mp_str"]) < mp_frac(1, 10**45) for p in all_pts
    )
    ir_bounds_ok = bool(pt_ir_hg["eig_1_mp"] > mp.mpf(9) and pt_ir_hg["eig_2_mp"] > mp.mpf(13))
    ir_zero_bounds_ok = bool(pt_ir_hz["eig_1_mp"] > mp.mpf(9) and pt_ir_hz["eig_2_mp"] > mp.mpf(13))

    def strip_mp(d: Dict[str, Any]) -> Dict[str, Any]:
        return {k: v for k, v in d.items() if k not in ("eig_1_mp", "eig_2_mp")}

    return {
        "conformal_fixed_point_symbolic_vanishing": vanish_sym,
        "all_conformal_residuals_lt_1e_45": all_conf_res_ok,
        "uv_spin10_T2_dD_low_yb": strip_mp(pt_uv_low),
        "uv_spin10_T2_dD_high_yb": strip_mp(pt_uv_high),
        "uv_spin10_T2_LDW_low_yb": strip_mp(pt_uv_low_ldw),
        "uv_spin10_T2_LDW_high_yb": strip_mp(pt_uv_high_ldw),
        "ir_t_minus38_high_yb_grav": strip_mp(pt_ir_hg),
        "ir_t_minus38_high_yb_zero": strip_mp(pt_ir_hz),
        "ir_grav_eig1_gt_9_and_eig2_gt_13": ir_bounds_ok,
        "ir_zero_eig1_gt_9_and_eig2_gt_13": ir_zero_bounds_ok,
        "passed": bool(
            vanish_sym
            and all_conf_res_ok
            and pt_uv_low["is_saddle"]
            and pt_uv_high["is_double_ir_attractive"]
            and pt_ir_hg["is_double_ir_attractive"]
            and ir_bounds_ok
            and ir_zero_bounds_ok
        ),
    }


# =============================================================================
# TASK OW13-B.3: Exact 1-Loop Quadratic Gravity (C^2 + R^2) + Conformal Matter
# =============================================================================
def run_quadratic_gravity_c2_r2() -> Dict[str, Any]:
    """
    Isolated Guardrail 4 Pure Gravity Avramidi-Barvinsky (1985) / Codello-Percacci (2006)
    benchmark + exact sympy.solve analysis of all 4 open-weave matter spectra and
    non-conformal |xi - 1/6|_crit bounds.
    """
    omega, xi = sp.symbols("omega xi", real=True)
    a_C_pure = sp.Rational(133, 10)
    b_lin_pure = 5 + a_C_pure  # 183/10
    c_const_pure = sp.Rational(5, 12)
    a_quad = sp.Rational(10, 3)

    # 1. Isolated Guardrail 4 Pure Gravity Benchmark (N_S = N_W = N_V = 0)
    poly_pure = a_quad * omega**2 + b_lin_pure * omega + c_const_pure
    disc_pure_sym = sp.discriminant(sp.Poly(poly_pure, omega))
    disc_pure_mp = sp_to_mp(disc_pure_sym)
    roots_pure = sorted([sp_to_mp(r) for r in sp.solve(sp.Eq(poly_pure, 0), omega)])
    omega_minus_pure, omega_plus_pure = roots_pure[0], roots_pure[1]
    # Stability: 16 pi^2 beta_omega = -lam_C * poly(omega), so d(16 pi^2 beta_omega)/d(omega) / lam_C = -poly'(omega)
    deriv_pure_expr = -sp.diff(poly_pure, omega)
    stab_plus_pure = sp_to_mp(deriv_pure_expr.subs(omega, sp.Float(mp.nstr(omega_plus_pure, 60), 60)))
    stab_minus_pure = sp_to_mp(deriv_pure_expr.subs(omega, sp.Float(mp.nstr(omega_minus_pure, 60), 60)))

    pure_bench_ok = bool(
        (-mp_frac(23, 1000) < omega_plus_pure < -mp_frac(22, 1000))
        and (-mp_frac(55, 10) < omega_minus_pure < -mp_frac(54, 10))
        and (stab_plus_pure < 0)
        and (stab_minus_pure > 0)
    )

    # 2. All 4 open-weave matter spectra
    matter_specs = [
        ("gsm_2h", "G_SM 2H", 8, 48, 12, sp.Rational(37, 15), mp_frac(19, 10)),
        ("ps_412", "PS(4,1,2)", 16, 48, 21, sp.Rational(103, 30), mp_frac(15, 10)),
        ("spin10_real10", "Spin(10) real-10", 10, 48, 45, sp.Rational(347, 60), mp_frac(22, 10)),
        ("spin10_complex10", "Spin(10) complex-10", 20, 48, 45, sp.Rational(88, 15), mp_frac(15, 10)),
    ]

    spectra_out: Dict[str, Any] = {}
    all_spectra_ok = True

    for key, label, n_s, n_w, n_v, expected_c_mat, crit_upper_bound in matter_specs:
        c_mat = sp.Rational(n_s + 3 * n_w + 12 * n_v, 120)
        c_mat_exact = bool(c_mat == expected_c_mat)
        b_R_mat = sp.Rational(3, 2) * n_s * (xi - sp.Rational(1, 6)) ** 2
        b_R_at_conformal_zero = bool(sp.simplify(b_R_mat.subs(xi, sp.Rational(1, 6))) == 0)

        a_C_tot = a_C_pure + 2 * c_mat
        b_lin_tot = 5 + a_C_tot
        poly_mat_xi = a_quad * omega**2 + b_lin_tot * omega + (c_const_pure + b_R_mat)
        poly_mat_conf = poly_mat_xi.subs(xi, sp.Rational(1, 6))

        disc_mat_conf_sym = sp.discriminant(sp.Poly(poly_mat_conf, omega))
        disc_mat_conf_mp = sp_to_mp(disc_mat_conf_sym)
        roots_mat = sorted([sp_to_mp(r) for r in sp.solve(sp.Eq(poly_mat_conf, 0), omega)])
        om_minus, om_plus = roots_mat[0], roots_mat[1]

        deriv_mat_expr = -sp.diff(poly_mat_conf, omega)
        stab_plus = sp_to_mp(deriv_mat_expr.subs(omega, sp.Float(mp.nstr(om_plus, 60), 60)))
        stab_minus = sp_to_mp(deriv_mat_expr.subs(omega, sp.Float(mp.nstr(om_minus, 60), 60)))

        # Solve exact |xi - 1/6|_crit via sympy.solve on discriminant(xi) == 0
        disc_xi_expr = sp.discriminant(sp.Poly(poly_mat_xi, omega))
        xi_crit_sols = sp.solve(sp.Eq(disc_xi_expr, 0), xi)
        deltas_crit = [abs(sp_to_mp(sol) - mp_frac(1, 6)) for sol in xi_crit_sols]
        xi_crit_delta = deltas_crit[0]
        sym_deltas_agree = bool(abs(deltas_crit[0] - deltas_crit[1]) < mp_frac(1, 10**50))

        spec_ok = bool(
            c_mat_exact
            and b_R_at_conformal_zero
            and (a_C_tot > a_C_pure)
            and (om_minus < om_plus < 0)
            and (stab_plus < 0)
            and (stab_minus > 0)
            and (disc_mat_conf_mp > disc_pure_mp)
            and sym_deltas_agree
            and (xi_crit_delta < crit_upper_bound)
        )
        if not spec_ok:
            all_spectra_ok = False

        spectra_out[key] = {
            "label": label,
            "spectrum": [n_s, n_w, n_v],
            "c_mat": str(c_mat),
            "c_mat_matches_exact": c_mat_exact,
            "a_C_tot": str(a_C_tot),
            "c2_asymptotic_freedom_strengthened": bool(a_C_tot > a_C_pure),
            "b_R_mat_at_conformal_is_zero": b_R_at_conformal_zero,
            "discriminant_at_conformal": to_pair(disc_mat_conf_mp),
            "discriminant_gt_pure_gravity": bool(disc_mat_conf_mp > disc_pure_mp),
            "omega_plus_uv_attractive": to_pair(om_plus),
            "omega_minus_uv_repulsive": to_pair(om_minus),
            "stab_deriv_omega_plus": to_pair(stab_plus),
            "stab_deriv_omega_minus": to_pair(stab_minus),
            "abs_xi_minus_1_6_crit": to_pair(xi_crit_delta),
            "crit_bound_passed": bool(xi_crit_delta < crit_upper_bound),
            "passed": spec_ok,
        }

    return {
        "pure_gravity_benchmark": {
            "a_C_pure": str(a_C_pure),
            "b_lin_pure": str(b_lin_pure),
            "c_const_pure": str(c_const_pure),
            "discriminant": to_pair(disc_pure_mp),
            "omega_plus_uv_attractive": to_pair(omega_plus_pure),
            "omega_minus_uv_repulsive": to_pair(omega_minus_pure),
            "stab_deriv_omega_plus": to_pair(stab_plus_pure),
            "stab_deriv_omega_minus": to_pair(stab_minus_pure),
            "passed": pure_bench_ok,
        },
        "matter_spectra": spectra_out,
        "all_4_spectra_passed": all_spectra_ok,
        "passed": bool(pure_bench_ok and all_spectra_ok),
    }


# =============================================================================
# TASK OW13-C: Exact 2H Gildener-Weinberg Scalon Spectrum & Collider Sum Rule
# =============================================================================
def run_task_ow13_c(
    sys2h: Dict[str, Any],
    ir_states_mp: Dict[str, List[mp.mpf]],
) -> Dict[str, Any]:
    """
    Symbolically prove 8 B_GW - (1/2) beta_{lam_1}(0) == 0, certify 1H SM top-tachyon
    no-go threshold y_t^{crit}, 2H pure-gauge Weinberg-Linde floor, and collider sum
    rule for m_h / v = 1/2.
    """
    s = sys2h["symbols"]
    v_ew = sp.Symbol("v", positive=True)
    l3, l4, g2, gp, yb, ytau, yt = (
        s["l3"],
        s["l4"],
        s["g2"],
        s["gp"],
        s["yb"],
        s["ytau"],
        s["yt"],
    )

    # 1. Exact 1-loop 2H GW identity along H_d flat direction (H_u = 0, lam_1 = 0)
    m_Hpm_sq = sp.Rational(1, 2) * l3 * v_ew**2
    m_H_sq = sp.Rational(1, 2) * (l3 + l4) * v_ew**2
    m_A_sq = sp.Rational(1, 2) * (l3 + l4) * v_ew**2
    m_W_sq = sp.Rational(1, 4) * g2**2 * v_ew**2
    m_Z_sq = sp.Rational(1, 4) * (g2**2 + gp**2) * v_ew**2
    m_b_sq = sp.Rational(1, 2) * yb**2 * v_ew**2
    m_tau_sq = sp.Rational(1, 2) * ytau**2 * v_ew**2

    B_GW_2h = (1 / (64 * sp.pi**2 * v_ew**4)) * (
        m_H_sq**2
        + m_A_sq**2
        + 2 * m_Hpm_sq**2
        + 6 * m_W_sq**2
        + 3 * m_Z_sq**2
        - 12 * m_b_sq**2
        - 4 * m_tau_sq**2
    )
    beta_lam1_at_0 = sys2h["b1_mat"].subs({s["l1"]: 0, s["box_sign"]: 1})
    gw_diff_sym = sp.simplify(8 * B_GW_2h - sp.Rational(1, 2) * beta_lam1_at_0)
    gw_identity_symbolic_zero = bool(gw_diff_sym == 0)

    # Numerical check at representative non-trivial rational point (< 1/10^45)
    num_pt = {
        g2: sp.Rational(13, 20),
        gp: sp.Rational(9, 25),
        l3: sp.Rational(7, 10),
        l4: sp.Rational(-3, 10),
        yb: sp.Rational(1, 100),
        ytau: sp.Rational(1, 100),
    }
    lhs_num = sp_to_mp((8 * B_GW_2h).subs(num_pt))
    rhs_num = sp_to_mp((sp.Rational(1, 2) * beta_lam1_at_0).subs(num_pt))
    gw_identity_num_diff = abs(lhs_num - rhs_num)

    # 2. 1H SM top-tachyon no-go threshold via sympy.solve
    yt_pos = sp.Symbol("yt_pos", positive=True)
    m_t_sq = sp.Rational(1, 2) * yt_pos**2 * v_ew**2
    B_1H = (1 / (64 * sp.pi**2 * v_ew**4)) * (6 * m_W_sq**2 + 3 * m_Z_sq**2 - 12 * m_t_sq**2)
    yt_sols = sp.solve(sp.Eq(B_1H, 0), yt_pos)
    yt_crit_expr = yt_sols[0]
    yt_crit_target = ((3 * g2**4 + 2 * g2**2 * gp**2 + gp**4) / 16) ** sp.Rational(1, 4)
    yt_crit_symbolic_match = bool(
        len(yt_sols) == 1 and sp.simplify(yt_crit_expr**4 - yt_crit_target**4) == 0
    )

    ew_g2 = mp_frac(13, 20)
    ew_gp = mp_frac(9, 25)
    gut_g2 = mp_frac(13, 25)
    gut_gp = mp.sqrt(mp_frac(3, 5)) * gut_g2

    def eval_yt_crit(g2_v: mp.mpf, gp_v: mp.mpf) -> mp.mpf:
        return ((mp.mpf(3) * g2_v**4 + mp.mpf(2) * g2_v**2 * gp_v**2 + gp_v**4) / mp.mpf(16)) ** mp_frac(1, 4)

    def eval_B_gauge(g2_v: mp.mpf, gp_v: mp.mpf) -> mp.mpf:
        return (mp.mpf(3) / (mp.mpf(1024) * mp.pi**2)) * (
            mp.mpf(3) * g2_v**4 + mp.mpf(2) * g2_v**2 * gp_v**2 + gp_v**4
        )

    yt_crit_ew = eval_yt_crit(ew_g2, ew_gp)
    yt_crit_gut = eval_yt_crit(gut_g2, gut_gp)
    b1h_ew_yt1 = eval_B_gauge(ew_g2, ew_gp) - (mp.mpf(3) / (mp.mpf(64) * mp.pi**2)) * mp.mpf(1) ** 4
    b1h_gut_yt1 = eval_B_gauge(gut_g2, gut_gp) - (mp.mpf(3) / (mp.mpf(64) * mp.pi**2)) * mp.mpf(1) ** 4

    yt_crit_ew_ok = bool(mp_frac(45, 100) < yt_crit_ew < mp_frac(46, 100))
    yt_crit_gut_ok = bool(mp_frac(37, 100) < yt_crit_gut < mp_frac(38, 100))

    # 3. Pure-gauge Weinberg-Linde 2H GW floor along H_d (top decoupled)
    B_2h_gauge_ew = eval_B_gauge(ew_g2, ew_gp)
    B_2h_gauge_gut = eval_B_gauge(gut_g2, gut_gp)
    mh_over_v_floor_ew = mp.sqrt(mp.mpf(8) * B_2h_gauge_ew)
    mh_over_v_floor_gut = mp.sqrt(mp.mpf(8) * B_2h_gauge_gut)
    floor_ew_ok = bool(mp_frac(39, 1000) < mh_over_v_floor_ew < mp_frac(40, 1000))
    floor_gut_ok = bool(mp_frac(28, 1000) < mh_over_v_floor_gut < mp_frac(29, 1000))

    # 4. Collider sum rule for m_h / v = 1/2 at EW benchmark
    # m_h^2 / v^2 = 8 B_GW = (1 / (8 pi^2)) * (m_H^4 + m_A^4 + 2 m_{H+-}^4) / v^4 + 8 B_gauge
    target_mh_over_v = mp_frac(1, 2)
    scalar_quartic_sum_over_v4 = mp.mpf(8) * mp.pi**2 * (target_mh_over_v**2 - mp.mpf(8) * B_2h_gauge_ew)
    sum_rule_inv = scalar_quartic_sum_over_v4 ** mp_frac(1, 4)
    M_heavy_over_v = (scalar_quartic_sum_over_v4 / mp.mpf(4)) ** mp_frac(1, 4)
    lam_eff_required = mp.mpf(2) * M_heavy_over_v**2

    # Compare against max |lam_{3,4}| from OW13-A downward RGE
    max_abs_lam34_ir = max(
        max(abs(ir_states_mp[k][8]), abs(ir_states_mp[k][9])) for k in ir_states_mp
    )

    sum_rule_inv_ok = bool(mp_frac(210, 100) < sum_rule_inv < mp_frac(211, 100))
    m_heavy_ok = bool(mp_frac(148, 100) < M_heavy_over_v < mp_frac(150, 100))
    lam_eff_ok = bool(lam_eff_required > mp_frac(44, 10))
    perturbative_gap_confirmed = bool(max_abs_lam34_ir < mp.mpf(1) < lam_eff_required)

    passed = bool(
        gw_identity_symbolic_zero
        and (gw_identity_num_diff < mp_frac(1, 10**45))
        and yt_crit_symbolic_match
        and yt_crit_ew_ok
        and yt_crit_gut_ok
        and (b1h_ew_yt1 < 0)
        and (b1h_gut_yt1 < 0)
        and (B_2h_gauge_ew > 0)
        and (B_2h_gauge_gut > 0)
        and floor_ew_ok
        and floor_gut_ok
        and sum_rule_inv_ok
        and m_heavy_ok
        and lam_eff_ok
        and perturbative_gap_confirmed
    )

    return {
        "gw_identity_symbolic_zero": gw_identity_symbolic_zero,
        "gw_identity_num_diff": to_pair(gw_identity_num_diff),
        "yt_crit_symbolic_match": yt_crit_symbolic_match,
        "yt_crit_ew": to_pair(yt_crit_ew),
        "yt_crit_ew_in_45_to_46_pct": yt_crit_ew_ok,
        "yt_crit_gut": to_pair(yt_crit_gut),
        "yt_crit_gut_in_37_to_38_pct": yt_crit_gut_ok,
        "B_1H_at_yt_1_ew": to_pair(b1h_ew_yt1),
        "B_1H_at_yt_1_gut": to_pair(b1h_gut_yt1),
        "B_2H_gauge_ew": to_pair(B_2h_gauge_ew),
        "B_2H_gauge_gut": to_pair(B_2h_gauge_gut),
        "mh_over_v_pure_gauge_floor_ew": to_pair(mh_over_v_floor_ew),
        "mh_over_v_floor_ew_in_39_to_40_permille": floor_ew_ok,
        "mh_over_v_pure_gauge_floor_gut": to_pair(mh_over_v_floor_gut),
        "mh_over_v_floor_gut_in_28_to_29_permille": floor_gut_ok,
        "collider_sum_rule_for_mh_over_v_half": {
            "M_heavy_over_v": to_pair(M_heavy_over_v),
            "M_heavy_over_v_in_148_to_150_pct": m_heavy_ok,
            "sum_rule_invariant_over_v": to_pair(sum_rule_inv),
            "sum_rule_invariant_in_210_to_211_pct": sum_rule_inv_ok,
            "lam_eff_required": to_pair(lam_eff_required),
            "lam_eff_gt_44_tenths": lam_eff_ok,
            "max_abs_lam34_downward_rge_IR": to_pair(max_abs_lam34_ir),
            "perturbative_gap_exposed": perturbative_gap_confirmed,
        },
        "passed": passed,
    }


# =============================================================================
# TASK OW13-D: 4 / 4 Planted Fault Controls (PF-OW13-1..4)
# =============================================================================
def run_planted_faults(
    sys2h: Dict[str, Any],
    fps_mp: Dict[str, Dict[str, mp.mpf]],
) -> Dict[str, Any]:
    """
    Execute all 4 planted fault controls PF-OW13-1..4 and verify each is caught
    by direct recomputation without hardcoded flags.
    """
    g_uv = mp_frac(13, 25)
    yt_uv = mp_frac(11, 20)
    yb_high = mp_frac(9, 20)
    yb_low = mp_frac(1, 100)

    # PF-OW13-1: Flip f_lam -> -f_lam at Spin(10) T2 (dD)
    f_dD_s10 = fps_mp["spin10_real10_T2"]["f_dD"]
    pf1_high = solve_4d_quartic_fp(sys2h, -f_dD_s10, g_uv, yt_uv, yb_high, yb_high)
    pf1_low = solve_4d_quartic_fp(sys2h, -f_dD_s10, g_uv, yt_uv, yb_low, yb_low)
    pf1_caught = bool(
        pf1_high["converged"]
        and pf1_high["all_thetas_positive"]
        and pf1_low["converged"]
        and pf1_low["all_thetas_positive"]
    )

    # PF-OW13-2: Flip sign of 1-loop gauge box in beta_{lam_1} -> G_SM 2H at y_b = 1/100 falsely gains real lam_1 root
    s = sys2h["symbols"]
    l1_sym = s["l1"]
    b1_sym_dec_pf2 = sp.expand(
        16 * sp.pi**2 * sys2h["B_full"][0].subs({s["l3"]: 0, s["l4"]: 0})
    )
    disc_b1_pf2_sym = sp.expand(sp.discriminant(sp.Poly(b1_sym_dec_pf2, l1_sym)))
    pf2_details: Dict[str, Any] = {}
    pf2_both_real = True
    for gname, fkey in [("dD", "f_dD"), ("LDW", "f_LDW")]:
        f_gsm = fps_mp["gsm_2h_T2"][fkey]
        subs_pf2 = {
            s["yb"]: sp.Rational(1, 100),
            s["ytau"]: sp.Rational(1, 100),
            s["g2"]: sp.Rational(13, 25),
            s["gp"]: sp.sqrt(sp.Rational(3, 5)) * sp.Rational(13, 25),
            s["f_lam"]: sp.Float(mp.nstr(f_gsm, 60), 60),
            s["box_sign"]: -1,
        }
        l1_c = sp.Symbol("l1_c")
        disc_f = sp_to_mp(disc_b1_pf2_sym.subs(subs_pf2))
        b1_flipped_num = sp.N(b1_sym_dec_pf2.subs(subs_pf2).subs(l1_sym, l1_c), 65)
        roots_f = sp.solve(sp.Eq(b1_flipped_num, 0), l1_c)
        max_im_f = max(abs(sp_to_mp(sp.im(r))) for r in roots_f)
        real_roots_f = sorted([sp_to_mp(sp.re(r)) for r in roots_f])
        # Also record full 4D coupled solver result informatively
        sol4_pf2 = solve_4d_quartic_fp(sys2h, f_gsm, g_uv, yt_uv, yb_low, yb_low, box_sign_val=-1)
        g_caught = bool(
            disc_f > 0
            and max_im_f < mp_frac(1, 10**45)
        )
        if not g_caught:
            pf2_both_real = False
        pf2_details[gname] = {
            "discriminant_flipped": to_pair(disc_f),
            "real_lam1_roots": [to_pair(r) for r in real_roots_f],
            "max_imag_part": to_pair(max_im_f),
            "full_4d_real_fp_converged": sol4_pf2["converged"],
            "full_4d_lam_star": sol4_pf2["lam_star"],
            "caught": g_caught,
        }
    pf2_caught = pf2_both_real

    # PF-OW13-3: Set non-conformal xi = 5 in C^2 + R^2 quadratic gravity for Spin(10) real-10
    omega_c = sp.Symbol("omega_c")
    n_s_s10, n_w_s10, n_v_s10 = 10, 48, 45
    c_mat_s10 = sp.Rational(n_s_s10 + 3 * n_w_s10 + 12 * n_v_s10, 120)
    b_lin_s10 = 5 + sp.Rational(133, 10) + 2 * c_mat_s10
    xi_fault = sp.Integer(5)
    c_const_fault = sp.Rational(5, 12) + sp.Rational(3, 2) * n_s_s10 * (xi_fault - sp.Rational(1, 6)) ** 2
    poly_pf3 = sp.Rational(10, 3) * omega_c**2 + b_lin_s10 * omega_c + c_const_fault
    disc_pf3 = sp_to_mp(sp.discriminant(sp.Poly(poly_pf3, omega_c)))
    roots_pf3 = sp.solve(sp.Eq(poly_pf3, 0), omega_c)
    im_pf3 = abs(sp_to_mp(sp.im(roots_pf3[0])))
    pf3_caught = bool(disc_pf3 < 0 and im_pf3 > mp_frac(1, 10))

    # PF-OW13-4: Couple top quark y_t = 94/100 to H_d GW flat direction at EW benchmark
    ew_g2 = mp_frac(13, 20)
    ew_gp = mp_frac(9, 25)
    yt_fault = mp_frac(94, 100)
    B_gauge_ew = (mp.mpf(3) / (mp.mpf(1024) * mp.pi**2)) * (
        mp.mpf(3) * ew_g2**4 + mp.mpf(2) * ew_g2**2 * ew_gp**2 + ew_gp**4
    )
    B_gw_fault = B_gauge_ew - (mp.mpf(3) / (mp.mpf(64) * mp.pi**2)) * yt_fault**4
    mh2_over_v2_fault = mp.mpf(8) * B_gw_fault
    pf4_caught = bool(B_gw_fault < 0 and mh2_over_v2_fault < 0)

    faults_detected = sum([int(pf1_caught), int(pf2_caught), int(pf3_caught), int(pf4_caught)])
    return {
        "PF_OW13_1_flip_f_lam_sign": {
            "spin10_T2_dD_high_yb_thetas": pf1_high["thetas"],
            "spin10_T2_dD_low_yb_thetas": pf1_low["thetas"],
            "all_thetas_flipped_positive_high_yb": pf1_high["all_thetas_positive"],
            "all_thetas_flipped_positive_low_yb": pf1_low["all_thetas_positive"],
            "caught": pf1_caught,
        },
        "PF_OW13_2_flip_gauge_box_sign": {
            "gauges": pf2_details,
            "caught": pf2_caught,
        },
        "PF_OW13_3_nonconformal_xi_5": {
            "xi_fault": 5,
            "discriminant_omega": to_pair(disc_pf3),
            "complex_root_abs_Im": to_pair(im_pf3),
            "caught": pf3_caught,
        },
        "PF_OW13_4_couple_top_to_Hd_GW": {
            "y_t_fault": to_pair(yt_fault),
            "B_GW_fault": to_pair(B_gw_fault),
            "mh2_over_v2_fault": to_pair(mh2_over_v2_fault),
            "caught": pf4_caught,
        },
        "planted_faults_detected": faults_detected,
        "planted_faults_total": 4,
        "passed": bool(faults_detected == 4),
    }


def main() -> None:
    buttazzo = run_guardrail4_buttazzo_sm()
    litim_grav, fps_mp, grav_bg_xi = derive_litim_and_solve_gravity_fps()
    sys2h = build_2hdm_symbolic_system()
    quartic_fps, saved_lams_mp = run_quartic_fps_and_collision(sys2h, fps_mp)
    downward_rge, ir_states_mp = run_downward_2h_rge(saved_lams_mp)
    fg_theorem = run_fg_structural_theorem()
    curved_xi = run_curved_space_xi_1loop(saved_lams_mp, ir_states_mp)
    quad_grav = run_quadratic_gravity_c2_r2()
    ow13_c = run_task_ow13_c(sys2h, ir_states_mp)
    ow13_d = run_planted_faults(sys2h, fps_mp)

    ow13_a_passed = bool(
        buttazzo["passed"]
        and litim_grav["passed"]
        and quartic_fps["passed"]
        and downward_rge["passed"]
        and fg_theorem["passed"]
    )
    ow13_b_passed = bool(
        curved_xi["passed"]
        and grav_bg_xi["passed"]
        and quad_grav["passed"]
    )
    ow13_c_passed = bool(ow13_c["passed"])
    ow13_d_passed = bool(ow13_d["passed"])
    all_gates_passed = bool(ow13_a_passed and ow13_b_passed and ow13_c_passed and ow13_d_passed)

    results = {
        "card_id": "A2-OW13",
        "erratum_applied": "AGY-002_A2-OW13-ERRATUM-1",
        "role": "Independent Cold-Room Zero-Trust Referee",
        "mpmath_dps": int(mp.mp.dps),
        "empirical_inputs_count": 0,
        "disjoint_methods": {
            "litim_and_beta_xi_bg": "sympy.integrate + sympy.diff symbolic differentiation",
            "gravity_cubic_roots": "sympy.real_roots + sympy.Poly.nroots cross-check",
            "quartic_2hdm_system": "8x8 sympy.hessian Tr(H^2) derivation + sympy.Matrix.jacobian + mpmath damped Newton",
            "ode_integrators": "pure mpmath RK4 with step-halving Richardson extrapolation + scipy Radau cross-check",
            "algebraic_theorems": "sympy.solve + sympy.discriminant + sympy.simplify",
        },
        "OW13_A": {
            "guardrail4_buttazzo_sm": buttazzo,
            "litim_symbolic_and_gravity_fps": litim_grav,
            "quartic_fps_and_collision_wall": quartic_fps,
            "downward_2h_rge": downward_rge,
            "fg_structural_theorem": fg_theorem,
            "passed": ow13_a_passed,
        },
        "OW13_B": {
            "curved_space_xi_1loop": curved_xi,
            "grav_bg_beta_xi": grav_bg_xi,
            "quadratic_gravity_c2_r2": quad_grav,
            "passed": ow13_b_passed,
        },
        "OW13_C": ow13_c,
        "OW13_D": ow13_d,
        "summary": {
            "ow13_a": ow13_a_passed,
            "ow13_b": ow13_b_passed,
            "ow13_c": ow13_c_passed,
            "ow13_d": ow13_d_passed,
            "planted_faults_detected": ow13_d["planted_faults_detected"],
            "all_gates_passed": all_gates_passed,
        },
    }

    out_path = Path(__file__).resolve().parent / "a2_ow13_referee_results.json"
    with out_path.open("w", encoding="utf-8") as fh:
        json.dump(results, fh, indent=2, sort_keys=False)
        fh.write("\n")


if __name__ == "__main__":
    main()
