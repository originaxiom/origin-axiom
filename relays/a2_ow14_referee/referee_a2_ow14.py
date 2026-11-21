#!/usr/bin/env python3
"""
Independent Cold-Room Zero-Trust Referee for AGY-002 Card A2-OW14.

Disjoint verification methods (zero producer / frontier imports, zero float/complex AST literals,
zero empirical PDG inputs, zero hardcoded proof flags):
  - OW14-A.1: General D = d + n two-step Weyl conformal transformation formula AND (1+6) ADM
              extrinsic curvature K_{ij} K^{ij} - K^2 (no 7^3 Christoffel loop).
  - OW14-A.2: Exact Heaviside partial fractions + sympy.integrate + 70-dps Gauss-Legendre and
              tanh-sinh quadrature + scipy Radau 1D autonomous dx/dN ODE + scipy Radau 4D
              cosmic-time Friedmann-radion ODE with exact analytic Jacobian (no DOP853).
  - OW14-A.3: Manual exact-QQ (Fraction) Euclidean GCD + Sturm sequence (no sympy.real_roots),
              70-dps bisection + Halley root finding, symbolic AdS elimination & Minkowski lift.
  - OW14-B.1: General 10-parameter non-diagonal symmetric 4x4 metric g = L D L^T (trace-free
              decoupling via g^{ab} g_{ab} = 4) + curved unimodular 4D Klein-Gordon preservation.
  - OW14-B.2: Exact unimodular FRG (cap=23 full & cap=22 traceless), sympy.combinatorics
              PermutationGroup / Schreier-Sims coset action enumeration for Delta(2,3,N),
              Spin(10) Type-II/I checks, and A2-OW13 bridges at lam = 0.
  - OW14-B.3: Direct variational Kaloper-Padilla global vacuum sequestering (abstract + scalar).
  - OW14-C:   Independent verification of all 4/4 planted fault controls (PF-OW14-1..4).
"""

from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any, Dict, List, Sequence, Tuple

import mpmath as mp
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from sympy.combinatorics import Permutation, PermutationGroup

# High-precision mpmath working precision (70 decimal digits, strictly >= 60 dps).
MP_DPS = 70
mp.mp.dps = MP_DPS


# ---------------------------------------------------------------------------
# Exact rational / mpmath helpers (zero float/complex AST literals)
# ---------------------------------------------------------------------------

def rat_float(num: int, den: int = 1) -> float:
    return float(Fraction(num, den))


def rat_mp(num: int, den: int = 1) -> mp.mpf:
    return mp.mpf(num) / mp.mpf(den)


def mp_str(val: mp.mpf, digits: int = 55) -> str:
    return mp.nstr(val, digits)


def canonicalize_log_expr(expr: sp.Expr) -> sp.Expr:
    """
    Canonicalize linear combinations of logs of real algebraic numbers without
    raising arguments to irrational powers: clean/rationalize each log argument,
    extract branch cut I*pi for negative arguments, and combine terms sharing the
    same irrational basis coefficient via exact integer powers.
    """
    def _clean_log(arg: sp.Expr) -> sp.Expr:
        sarg = sp.radsimp(sp.together(sp.expand(arg)))
        if sarg.is_negative:
            return sp.log(sp.simplify(-sarg)) + sp.I * sp.pi
        return sp.log(sp.simplify(sarg))

    rw = expr.replace(
        lambda e: isinstance(e, sp.log),
        lambda e: _clean_log(e.args[0]),
    )
    ex = sp.expand_log(sp.expand(rw), force=True)
    terms = sp.Add.make_args(sp.expand(ex))
    const_part = sp.Integer(0)
    # Group (rational_coeff, arg) by irrational basis key:
    groups: Dict[sp.Expr, List[Tuple[sp.Rational, sp.Expr]]] = {}
    for term in terms:
        logs = [f for f in sp.Mul.make_args(term) if isinstance(f, sp.log)]
        if len(logs) == 1:
            lg = logs[0]
            coeff = sp.simplify(term / lg)
            r_part, ir_part = coeff.as_coeff_Mul(rational=True)
            if isinstance(r_part, sp.Rational):
                key = sp.simplify(ir_part)
                groups.setdefault(key, []).append((r_part, lg.args[0]))
            else:
                const_part += term
        else:
            const_part += term

    out = sp.simplify(const_part)
    for key, items in groups.items():
        lcm_den = 1
        for r_val, _ in items:
            lcm_den = math.lcm(lcm_den, int(r_val.q))
        arg_prod = sp.Integer(1)
        for r_val, arg in items:
            exp_int = int(r_val.p) * (lcm_den // int(r_val.q))
            arg_prod = sp.radsimp(sp.together(arg_prod * (arg ** exp_int)))
        arg_clean = sp.simplify(sp.radsimp(sp.together(arg_prod)))
        if arg_clean != 1:
            out += (key / lcm_den) * sp.log(arg_clean)
    return sp.simplify(out)


# ---------------------------------------------------------------------------
# Manual exact-QQ polynomial arithmetic & Sturm sequence (disjoint from sympy.real_roots)
# ---------------------------------------------------------------------------

PolyQQ = List[Fraction]  # ascending powers: c[0] + c[1]*x + ... + c[d]*x^d


def poly_trim(p: Sequence[Fraction]) -> PolyQQ:
    out = [Fraction(c) for c in p]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out if out else [Fraction(0)]


def poly_deg(p: PolyQQ) -> int:
    t = poly_trim(p)
    if len(t) == 1 and t[0] == 0:
        return -1
    return len(t) - 1


def poly_deriv(p: PolyQQ) -> PolyQQ:
    t = poly_trim(p)
    if len(t) <= 1:
        return [Fraction(0)]
    return poly_trim([t[k] * k for k in range(1, len(t))])


def poly_divmod(a: PolyQQ, b: PolyQQ) -> Tuple[PolyQQ, PolyQQ]:
    rem = poly_trim(a)
    div = poly_trim(b)
    db = poly_deg(div)
    if db < 0:
        raise ZeroDivisionError("Polynomial division by zero")
    da = poly_deg(rem)
    if da < db:
        return [Fraction(0)], rem
    q = [Fraction(0)] * (da - db + 1)
    lc_b = div[db]
    for k in range(da - db, -1, -1):
        coeff = rem[k + db] / lc_b
        q[k] = coeff
        if coeff != 0:
            for j in range(db + 1):
                rem[k + j] -= coeff * div[j]
    return poly_trim(q), poly_trim(rem)


def poly_monic(p: PolyQQ) -> PolyQQ:
    t = poly_trim(p)
    d = poly_deg(t)
    if d < 0:
        return [Fraction(0)]
    lc = t[d]
    return [c / lc for c in t]


def poly_gcd(a: PolyQQ, b: PolyQQ) -> PolyQQ:
    x = poly_trim(a)
    y = poly_trim(b)
    while poly_deg(y) >= 0:
        _, r = poly_divmod(x, y)
        x, y = y, r
    return poly_monic(x)


def poly_eval_qq(p: PolyQQ, x: Fraction) -> Fraction:
    acc = Fraction(0)
    for c in reversed(p):
        acc = acc * x + c
    return acc


def poly_eval_mp(p: PolyQQ, x: mp.mpf) -> mp.mpf:
    acc = mp.mpf(0)
    for c in reversed(p):
        acc = acc * x + rat_mp(c.numerator, c.denominator)
    return acc


def _sign_qq(val: Fraction) -> int:
    if val > 0:
        return 1
    if val < 0:
        return -1
    return 0


def _sign_variations(signs: Sequence[int]) -> int:
    nz = [s for s in signs if s != 0]
    return sum(1 for i in range(len(nz) - 1) if nz[i] * nz[i + 1] < 0)


def sturm_chain_qq(p: PolyQQ) -> Tuple[List[PolyQQ], int]:
    """Build exact-QQ Sturm chain for square-free part of p; returns (chain, gcd_degree)."""
    p0 = poly_trim(p)
    dp = poly_deriv(p0)
    g = poly_gcd(p0, dp)
    g_deg = poly_deg(g)
    if g_deg > 0:
        p0, rem_chk = poly_divmod(p0, g)
        if poly_deg(rem_chk) >= 0:
            raise ValueError("Square-free division left nonzero remainder")
    p1 = poly_deriv(p0)
    chain: List[PolyQQ] = [p0, p1]
    while poly_deg(chain[-1]) > 0:
        _, r = poly_divmod(chain[-2], chain[-1])
        if poly_deg(r) < 0:
            break
        neg_r = [-c for c in r]
        # Scale by positive |lc|^-1 to keep rational heights small while preserving all signs.
        scale = abs(neg_r[-1])
        chain.append(poly_trim([c / scale for c in neg_r]))
    return chain, g_deg


def sturm_root_count_pos_inf(p: PolyQQ) -> Dict[str, Any]:
    """Count distinct real roots in (0, +inf) via exact-QQ Sturm theorem (assuming p(0) != 0)."""
    chain, g_deg = sturm_chain_qq(p)
    p0_at_0 = poly_eval_qq(chain[0], Fraction(0))
    if p0_at_0 == 0:
        raise ValueError("Boundary x=0 is a root; factor out x first")
    signs_zero = [_sign_qq(poly_eval_qq(q, Fraction(0))) for q in chain]
    signs_pos_inf = [_sign_qq(q[-1]) for q in chain]
    signs_neg_inf = [
        _sign_qq(q[-1] * (-1 if (poly_deg(q) % 2 == 1) else 1))
        for q in chain
    ]
    v_zero = _sign_variations(signs_zero)
    v_pos_inf = _sign_variations(signs_pos_inf)
    v_neg_inf = _sign_variations(signs_neg_inf)
    return {
        "sturm_chain_length": len(chain),
        "gcd_degree": g_deg,
        "v_zero": v_zero,
        "v_pos_inf": v_pos_inf,
        "v_neg_inf": v_neg_inf,
        "positive_real_roots": v_zero - v_pos_inf,
        "negative_real_roots": v_neg_inf - v_zero,
        "total_real_roots": v_neg_inf - v_pos_inf,
    }


def descartes_sign_changes(p: PolyQQ) -> int:
    signs = [_sign_qq(c) for c in reversed(poly_trim(p)) if c != 0]
    return _sign_variations(signs)


# ---------------------------------------------------------------------------
# Task OW14-A.1: 7D -> 4D Einstein-Frame Radion via Two-Step Weyl + (1+6) ADM
# ---------------------------------------------------------------------------

def run_ow14_a1() -> Dict[str, Any]:
    d_sym, n_sym = sp.symbols("d n", integer=True, positive=True)
    D_sym = d_sym + n_sym
    a_sym, b_sym = sp.symbols("a b", real=True)
    t_sym = sp.Symbol("t", real=True)
    sig = sp.Function("sig")(t_sym)
    sig_p = sp.diff(sig, t_sym)
    sig_pp = sp.diff(sig, t_sym, 2)

    # --- Disjoint Method 1: General D = d + n Two-Step Weyl Conformal Transformation ---
    # Metric: ds_D^2 = e^{2 a sig} g~_{mu nu}(x) dx^mu dx^nu + e^{2 b sig} g^_{mn}(y) dy^m dy^n
    # Step 1: Factor overall e^{2 omega_D} with omega_D = b * sig:
    #         g_D = e^{2 omega_D} g_ring_D, where g_ring_D is the EXACT direct product
    #         (e^{2 omega_d} g~_d) x g^_n with omega_d = (a - b) * sig.
    # Step 2: Apply R(e^{2 omega} g_bar) = e^{-2 omega}[R_bar - 2(D-1) Box_bar omega - (D-1)(D-2) (nabla_bar omega)^2]
    #         first in D dimensions (g_ring_D -> g_D), then in d dimensions (g~_d -> g_ring_d),
    #         using Box_ring(omega_D) = e^{-2 omega_d}[Box~ omega_D + (d-2) (nabla~ omega_d).(nabla~ omega_D)].
    w_D_coeff = b_sym
    w_d_coeff = a_sym - b_sym

    # Coefficients inside R_D(g_D) = e^{-2 a sig}[ R_d(g~) + C_box * Box~ sig + C_grad2 * (nabla~ sig)^2 ] + e^{-2 b sig} R_n(g^)
    C_box_gen = sp.simplify(
        -2 * (d_sym - 1) * w_d_coeff - 2 * (D_sym - 1) * w_D_coeff
    )
    C_grad2_gen = sp.simplify(
        -(d_sym - 1) * (d_sym - 2) * w_d_coeff**2
        - 2 * (D_sym - 1) * (d_sym - 2) * w_d_coeff * w_D_coeff
        - (D_sym - 1) * (D_sym - 2) * w_D_coeff**2
    )

    # Volume measure factor in (1/2) sqrt(-g_D) R_D:
    # sqrt(-g_D) * e^{-2 a sig} = e^{E_gen * sig} sqrt(-g~) sqrt(g^), with E_gen = (d-2)*a + n*b.
    E_gen = (d_sym - 2) * a_sym + n_sym * b_sym

    # Integration by parts on e^{E sig} Box~ sig = div(e^{E sig} nabla~ sig) - E e^{E sig} (nabla~ sig)^2:
    C_kin_cov_gen = sp.simplify(C_grad2_gen - E_gen * C_box_gen)

    # Specialize to d = 4, n = 3 (D = 7), flat 4D metric eta = diag(-1,1,1,1) and sig = sig(t):
    # Here Box~ sig = -sig'', (nabla~ sig)^2 = -(sig')^2.
    subs_7d = {d_sym: 4, n_sym: 3}
    E_7d = sp.simplify(E_gen.subs(subs_7d))  # 2*a + 3*b
    C_box_7d = sp.simplify(C_box_gen.subs(subs_7d))  # -6*a - 6*b
    C_grad2_7d = sp.simplify(C_grad2_gen.subs(subs_7d))  # -6*a^2 - 12*a*b - 12*b^2
    C_kin_cov_7d = sp.simplify(C_kin_cov_gen.subs(subs_7d))

    L_eff_weyl = sp.expand(
        sp.Rational(1, 2) * sp.exp(E_7d * sig) * (C_box_7d * (-sig_pp) + C_grad2_7d * (-sig_p**2))
    )
    # Total time derivative to subtract: d/dt(c_pp * e^{E sig} * sig')
    c_pp_weyl = sp.simplify(-sp.Rational(1, 2) * C_box_7d)  # 3*(a + b)
    total_deriv_weyl = sp.diff(c_pp_weyl * sp.exp(E_7d * sig) * sig_p, t_sym)
    L_kin_weyl_general = sp.simplify(L_eff_weyl - total_deriv_weyl)

    # --- Disjoint Method 2: (1+6) ADM Extrinsic Curvature K_{ij} K^{ij} - K^2 ---
    # Metric: ds_7^2 = -N(t)^2 dt^2 + sum_{i=1}^3 A(t)^2 (dx^i)^2 + sum_{m=4}^6 B(t)^2 (dy^m)^2
    # with N = A = e^{a sig(t)}, B = e^{b sig(t)}, spatial slices flat (R^{(6)} = 0).
    N_adm = sp.exp(a_sym * sig)
    A_adm = sp.exp(a_sym * sig)
    B_adm = sp.exp(b_sym * sig)
    sqrt_gamma = A_adm**3 * B_adm**3
    K_ext = (sp.diff(A_adm, t_sym) / (N_adm * A_adm))
    K_int = (sp.diff(B_adm, t_sym) / (N_adm * B_adm))
    K_trace = sp.simplify(3 * K_ext + 3 * K_int)
    K_ij_K_ij = sp.simplify(3 * K_ext**2 + 3 * K_int**2)
    L_kin_adm_general = sp.simplify(sp.Rational(1, 2) * N_adm * sqrt_gamma * (K_ij_K_ij - K_trace**2))
    boundary_deriv_adm = sp.diff(sqrt_gamma * K_trace, t_sym)
    L_eff_adm = sp.simplify(L_kin_adm_general + boundary_deriv_adm)

    # Cross-check Method 1 (Weyl) vs Method 2 (ADM) identically for arbitrary (a, b):
    weyl_vs_adm_leff_diff = sp.simplify(L_eff_weyl - L_eff_adm)
    weyl_vs_adm_lkin_diff = sp.simplify(L_kin_weyl_general - L_kin_adm_general)

    # Enforce 4D Einstein frame: E_7d = 2*a + 3*b = 0 => a = -(3/2)*b
    a_einstein_expr = sp.solve(E_7d, a_sym)[0]
    L_kin_einstein = sp.simplify(L_kin_weyl_general.subs(a_sym, a_einstein_expr))
    kin_prefactor_b2 = sp.simplify(L_kin_einstein / sig_p**2)  # (15/4)*b^2

    # Solve L_kin = (1/2)*(sig')^2 for positive canonical b:
    b_solutions = sp.solve(sp.Eq(kin_prefactor_b2, sp.Rational(1, 2)), b_sym)
    b_canon = [s for s in b_solutions if s.is_positive][0]
    a_canon = sp.simplify(a_einstein_expr.subs(b_sym, b_canon))

    # General d = 4, arbitrary internal dimension n canonical formula from Method 1:
    a_gen_d4 = sp.solve(E_gen.subs(d_sym, 4), a_sym)[0]
    kin_coeff_d4_n = sp.simplify(-sp.Rational(1, 2) * C_kin_cov_gen.subs({d_sym: 4, a_sym: a_gen_d4}))
    # Check kin_coeff_d4_n == n*(n+2)/4 * b^2:
    kin_coeff_d4_n_diff = sp.simplify(kin_coeff_d4_n - n_sym * (n_sym + 2) * b_sym**2 / 4)

    # Potential exponents for L = e^{b * phi} (with phi = canonical radion):
    # sqrt(-g_7) = e^{(4a + 3b) phi} sqrt(-g~) sqrt(g^) = L^{-3} sqrt(-g~) sqrt(g^)
    # 1. Bulk Lambda_7: -Lambda_7 * sqrt(-g_7) -> L^{-3}
    # 2. Hyperbolic curvature R(H^3) = -6/L^2: -(1/2) sqrt(-g_7) R(H^3) -> L^{-3} * L^{-2} = L^{-5}
    # 3. 7D CS 3-form flux F_{mnp} F^{mnp} ~ L^{-6}: sqrt(-g_7) F^2 -> L^{-3} * L^{-6} = L^{-9}
    # 4. 1-loop Casimir rho_7 ~ L^{-7} (or 4D KK mass^4 = (e^{a phi}/L)^4 = L^{-10}): sqrt(-g_7) L^{-7} -> L^{-10}
    vol_exp_L = sp.simplify((4 * a_einstein_expr + 3 * b_sym) / b_sym)  # -3
    pot_specs = [
        ("bulk_Lambda7", int(-vol_exp_L), sp.sqrt(sp.Rational(6, 5)), sp.Rational(3, 5), sp.Rational(-3, 5)),
        ("hyperbolic_curvature", int(-vol_exp_L + 2), sp.sqrt(sp.Rational(10, 3)), sp.Rational(5, 3), sp.Rational(1, 9)),
        ("cs_3form_flux", int(-vol_exp_L + 6), 3 * sp.sqrt(sp.Rational(6, 5)), sp.Rational(27, 5), sp.Rational(13, 5)),
        ("casimir_1loop", int(-vol_exp_L + 7), 2 * sp.sqrt(sp.Rational(10, 3)), sp.Rational(20, 3), sp.Rational(31, 9)),
    ]

    slopes: Dict[str, Any] = {}
    slopes_exact_ok = True
    single_term_nogo_ok = True
    for name, p_power, gamma_expected, eps_expected, w_expected in pot_specs:
        gamma_val = sp.simplify(p_power * b_canon)
        eps_V = sp.simplify(gamma_val**2 / 2)
        w_attr = sp.simplify(gamma_val**2 / 3 - 1)
        g_ok = sp.simplify(gamma_val - gamma_expected) == 0
        e_ok = sp.simplify(eps_V - eps_expected) == 0
        w_ok = sp.simplify(w_attr - w_expected) == 0
        slopes_exact_ok = slopes_exact_ok and g_ok and e_ok and w_ok
        accelerating = bool(sp.simplify(gamma_val**2 - 2) < 0)
        if name != "bulk_Lambda7":
            single_term_nogo_ok = single_term_nogo_ok and (not accelerating) and bool(eps_V > 1) and bool(w_attr > sp.Rational(-1, 3))
        else:
            single_term_nogo_ok = single_term_nogo_ok and accelerating and bool(w_attr < sp.Rational(-1, 3))
        slopes[name] = {
            "L_exponent": -p_power,
            "gamma_exact": str(gamma_val),
            "gamma_squared": str(sp.simplify(gamma_val**2)),
            "gamma_float": float(sp.N(gamma_val, 30)),
            "eps_V": str(eps_V),
            "w_attr": str(w_attr),
            "accelerating": accelerating,
            "matches_expected": bool(g_ok and e_ok and w_ok),
        }

    # Verify canonical values match Townsend-Wohlfarth n=3 benchmark:
    b_match = sp.simplify(b_canon - sp.sqrt(sp.Rational(2, 15))) == 0
    a_match = sp.simplify(a_canon - (-sp.sqrt(sp.Rational(3, 10)))) == 0
    lkin_match = sp.simplify(kin_prefactor_b2 - sp.Rational(15, 4) * b_sym**2) == 0

    passed = bool(
        (weyl_vs_adm_leff_diff == 0)
        and (weyl_vs_adm_lkin_diff == 0)
        and (kin_coeff_d4_n_diff == 0)
        and b_match
        and a_match
        and lkin_match
        and slopes_exact_ok
        and single_term_nogo_ok
    )

    return {
        "methods": ["general_D_two_step_Weyl_conformal", "1plus6_ADM_extrinsic_curvature"],
        "weyl_C_box_general": str(C_box_gen),
        "weyl_C_grad2_general": str(C_grad2_gen),
        "weyl_vs_adm_Leff_diff": str(weyl_vs_adm_leff_diff),
        "weyl_vs_adm_Lkin_diff": str(weyl_vs_adm_lkin_diff),
        "general_d4_n_kin_coeff_diff": str(kin_coeff_d4_n_diff),
        "einstein_frame_condition": str(E_7d),
        "a_in_terms_of_b": str(a_einstein_expr),
        "c_pp_total_derivative_coeff": str(c_pp_weyl),
        "L_kin_einstein_prefactor": str(kin_prefactor_b2),
        "b_canonical": str(b_canon),
        "b_canonical_55dps": mp_str(mp.sqrt(rat_mp(2, 15))),
        "a_canonical": str(a_canon),
        "a_canonical_55dps": mp_str(-mp.sqrt(rat_mp(3, 10))),
        "slopes": slopes,
        "single_term_slow_roll_nogo_verified": single_term_nogo_ok,
        "passed": passed,
    }


# ---------------------------------------------------------------------------
# Task OW14-A.2: Townsend-Wohlfarth Hyperbolic Transient Acceleration
# ---------------------------------------------------------------------------

def _exact_N_accel_max_Hn(n_int: int) -> Tuple[sp.Expr, sp.Expr, sp.Expr, bool]:
    """
    Derive N_accel_max(H^n) from 1D autonomous ODE dx/dN = (1 - x^2)(c - 3*x)
    where c = sqrt(3/2)*gamma_curv(H^n) = sqrt(3*(n+2)/n), via:
      (1) exact Heaviside partial fractions + termwise sympy.integrate
      (2) direct sympy.integrate
      (3) closed-form logarithmic identity
    """
    x = sp.Symbol("x", real=True)
    gamma_n = sp.sqrt(sp.Rational(2 * (n_int + 2), n_int))
    c_n = sp.simplify(sp.sqrt(sp.Rational(3, 2)) * gamma_n)  # sqrt(3*(n+2)/n)
    integrand = 1 / ((1 - x**2) * (c_n - 3 * x))

    # Heaviside cover-up partial fractions: A/(1-x) + B/(1+x) + C/(c - 3x)
    A = sp.simplify(sp.limit((1 - x) * integrand, x, 1))
    B = sp.simplify(sp.limit((1 + x) * integrand, x, -1))
    C = sp.simplify(sp.limit((c_n - 3 * x) * integrand, x, c_n / 3))
    pf_expr = A / (1 - x) + B / (1 + x) + C / (c_n - 3 * x)
    pf_identity_ok = sp.simplify(pf_expr - integrand) == 0

    lim_lo = -1 / sp.sqrt(3)
    lim_hi = 1 / sp.sqrt(3)

    # Termwise sympy.integrate on partial fractions:
    int_A = sp.integrate(A / (1 - x), (x, lim_lo, lim_hi))
    int_B = sp.integrate(B / (1 + x), (x, lim_lo, lim_hi))
    int_C = sp.integrate(C / (c_n - 3 * x), (x, lim_lo, lim_hi))
    N_from_pf = sp.simplify(int_A + int_B + int_C)

    # Closed form: (3/(9 - c^2)) ln((c + sqrt(3))/(c - sqrt(3))) - (c/(9 - c^2)) ln((sqrt(3)+1)/(sqrt(3)-1))
    denom = sp.simplify(9 - c_n**2)
    N_closed = (
        sp.Rational(3, 1) / denom * sp.log((c_n + sp.sqrt(3)) / (c_n - sp.sqrt(3)))
        - c_n / denom * sp.log((sp.sqrt(3) + 1) / (sp.sqrt(3) - 1))
    )

    pf_matches_closed = canonicalize_log_expr(N_from_pf - N_closed) == 0
    return gamma_n, c_n, N_closed, bool(pf_identity_ok and pf_matches_closed)


def run_ow14_a2() -> Dict[str, Any]:
    # 1. Exact symbolic partial fractions + sympy.integrate for H^3 (and H^2, H^4, H^6):
    gamma_h3, c_h3, N_closed_h3, sym_pf_ok_h3 = _exact_N_accel_max_Hn(3)
    x_sym = sp.Symbol("x", real=True)
    direct_sym_int = sp.integrate(
        1 / ((1 - x_sym**2) * (sp.sqrt(5) - 3 * x_sym)),
        (x_sym, -1 / sp.sqrt(3), 1 / sp.sqrt(3)),
    )
    direct_sym_matches_closed = canonicalize_log_expr(direct_sym_int - N_closed_h3) == 0

    # Verify explicit card formula:
    card_N_formula = (
        sp.Rational(3, 4) * sp.log((sp.sqrt(5) + sp.sqrt(3)) / (sp.sqrt(5) - sp.sqrt(3)))
        - sp.sqrt(5) / 4 * sp.log((sp.sqrt(3) + 1) / (sp.sqrt(3) - 1))
    )
    card_formula_exact_match = canonicalize_log_expr(N_closed_h3 - card_N_formula) == 0

    # High-precision mpmath evaluation of exact closed form (70 dps):
    s5 = mp.sqrt(mp.mpf(5))
    s3 = mp.sqrt(mp.mpf(3))
    N_exact_mp = (
        rat_mp(3, 4) * mp.log((s5 + s3) / (s5 - s3))
        - (s5 / mp.mpf(4)) * mp.log((s3 + mp.mpf(1)) / (s3 - mp.mpf(1)))
    )

    # 2. Disjoint 70-dps quadrature: BOTH Gauss-Legendre AND tanh-sinh
    def _integrand_h3_mp(xv: mp.mpf) -> mp.mpf:
        return mp.mpf(1) / ((mp.mpf(1) - xv * xv) * (s5 - mp.mpf(3) * xv))

    lo_mp = -mp.mpf(1) / s3
    hi_mp = mp.mpf(1) / s3
    N_quad_gl = mp.quad(_integrand_h3_mp, [lo_mp, hi_mp], method="gauss-legendre")
    N_quad_ts = mp.quad(_integrand_h3_mp, [lo_mp, hi_mp], method="tanh-sinh")
    err_quad_gl = abs(N_quad_gl - N_exact_mp)
    err_quad_ts = abs(N_quad_ts - N_exact_mp)
    tol_quad = rat_mp(1, 10**45)

    # 3. Disjoint 1D autonomous ODE dx/dN = (1 - x^2)(sqrt(5) - 3x) via scipy Radau:
    s5_f = math.sqrt(5)
    inv_s3_f = 1 / math.sqrt(3)
    x0_f = rat_float(-999, 1000)
    rtol_ode = rat_float(1, 10**13)
    atol_ode = rat_float(1, 10**14)

    def rhs_1d(_N: float, y: np.ndarray) -> List[float]:
        xv = float(y[0])
        return [(1 - xv * xv) * (s5_f - 3 * xv)]

    def jac_1d(_N: float, y: np.ndarray) -> np.ndarray:
        xv = float(y[0])
        return np.array([[9 * xv * xv - 2 * s5_f * xv - 3]])

    def ev_1d_entry(_N: float, y: np.ndarray) -> float:
        return float(y[0]) + inv_s3_f

    ev_1d_entry.terminal = False
    ev_1d_entry.direction = 1

    def ev_1d_bounce(_N: float, y: np.ndarray) -> float:
        return float(y[0])

    ev_1d_bounce.terminal = False
    ev_1d_bounce.direction = 1

    def ev_1d_exit(_N: float, y: np.ndarray) -> float:
        return float(y[0]) - inv_s3_f

    ev_1d_exit.terminal = False
    ev_1d_exit.direction = 1

    sol_1d = solve_ivp(
        rhs_1d,
        (0, 12),
        [x0_f],
        method="Radau",
        jac=jac_1d,
        events=[ev_1d_entry, ev_1d_bounce, ev_1d_exit],
        rtol=rtol_ode,
        atol=atol_ode,
    )
    events_1d_ok = bool(
        sol_1d.success
        and len(sol_1d.t_events[0]) == 1
        and len(sol_1d.t_events[1]) == 1
        and len(sol_1d.t_events[2]) == 1
    )
    N_accel_1d_ode = float(sol_1d.t_events[2][0] - sol_1d.t_events[0][0]) if events_1d_ok else rat_float(-1, 1)
    err_1d_ode = abs(mp.mpf(str(N_accel_1d_ode)) - N_exact_mp)
    x_1d_end = float(sol_1d.y[0, -1])
    w_1d_end = 2 * x_1d_end * x_1d_end - 1

    # 4. Disjoint 4D cosmic-time Friedmann + radion ODE via scipy Radau + exact Jacobian:
    #    3 H^2 = (1/2) phidot^2 + e^{-gamma phi},  phiddot + 3 H phidot - gamma e^{-gamma phi} = 0
    #    State y = [N, phi, v] with v = phidot, phi_0 = 0, x_0 = -999/1000.
    gamma_f = math.sqrt(rat_float(10, 3))
    H0_f = 1 / math.sqrt(3 * (1 - x0_f * x0_f))
    v0_f = math.sqrt(6) * H0_f * x0_f

    def rhs_4d(_t: float, y: np.ndarray) -> List[float]:
        phi_v = float(y[1])
        v_v = float(y[2])
        V_v = math.exp(-gamma_f * phi_v)
        H_v = math.sqrt((v_v * v_v / 2 + V_v) / 3)
        return [H_v, v_v, -3 * H_v * v_v + gamma_f * V_v]

    def jac_4d(_t: float, y: np.ndarray) -> np.ndarray:
        phi_v = float(y[1])
        v_v = float(y[2])
        V_v = math.exp(-gamma_f * phi_v)
        H_v = math.sqrt((v_v * v_v / 2 + V_v) / 3)
        dH_dphi = -gamma_f * V_v / (6 * H_v)
        dH_dv = v_v / (6 * H_v)
        df2_dphi = gamma_f * v_v * V_v / (2 * H_v) - gamma_f * gamma_f * V_v
        df2_dv = -3 * H_v - v_v * v_v / (2 * H_v)
        z0 = rat_float(0)
        one = rat_float(1)
        return np.array([
            [z0, dH_dphi, dH_dv],
            [z0, z0, one],
            [z0, df2_dphi, df2_dv],
        ], dtype=float)

    def ev_4d_entry(_t: float, y: np.ndarray) -> float:
        return 3 * float(y[2]) ** 2 - 2 * math.exp(-gamma_f * float(y[1]))

    ev_4d_entry.terminal = False
    ev_4d_entry.direction = -1

    def ev_4d_bounce(_t: float, y: np.ndarray) -> float:
        return float(y[2])

    ev_4d_bounce.terminal = False
    ev_4d_bounce.direction = 1

    def ev_4d_exit(_t: float, y: np.ndarray) -> float:
        return 3 * float(y[2]) ** 2 - 2 * math.exp(-gamma_f * float(y[1]))

    ev_4d_exit.terminal = False
    ev_4d_exit.direction = 1

    sol_4d = solve_ivp(
        rhs_4d,
        (rat_float(0), rat_float(200)),
        [rat_float(0), rat_float(0), v0_f],
        method="Radau",
        jac=jac_4d,
        events=[ev_4d_entry, ev_4d_bounce, ev_4d_exit],
        rtol=rtol_ode,
        atol=atol_ode,
    )
    events_4d_ok = bool(
        sol_4d.success
        and len(sol_4d.t_events[0]) == 1
        and len(sol_4d.t_events[1]) == 1
        and len(sol_4d.t_events[2]) == 1
    )
    if events_4d_ok:
        N_accel_4d_ode = float(sol_4d.y_events[2][0][0] - sol_4d.y_events[0][0][0])
        t_entry_4d = float(sol_4d.t_events[0][0])
        t_bounce_4d = float(sol_4d.t_events[1][0])
        t_exit_4d = float(sol_4d.t_events[2][0])
        vb = float(sol_4d.y_events[1][0][2])
        Vb = math.exp(-gamma_f * float(sol_4d.y_events[1][0][1]))
        w_min_bounce = (vb * vb / 2 - Vb) / (vb * vb / 2 + Vb)
    else:
        N_accel_4d_ode = rat_float(-1, 1)
        t_entry_4d = t_bounce_4d = t_exit_4d = rat_float(-1, 1)
        w_min_bounce = rat_float(0, 1)

    v_t200 = float(sol_4d.y[2, -1])
    V_t200 = math.exp(-gamma_f * float(sol_4d.y[1, -1]))
    w_t200 = (v_t200 * v_t200 / 2 - V_t200) / (v_t200 * v_t200 / 2 + V_t200)
    err_4d_ode = abs(mp.mpf(str(N_accel_4d_ode)) - N_exact_mp)
    err_w_min = abs(mp.mpf(str(w_min_bounce)) + mp.mpf(1))
    err_w_t200 = abs(mp.mpf(str(w_t200)) - rat_mp(1, 9))

    # 5. Dimension hierarchy H^2, H^3, H^4, H^6:
    hierarchy: Dict[str, Any] = {}
    hier_vals: List[mp.mpf] = []
    hier_sym_ok = True
    for n_val in (2, 3, 4, 6):
        g_n, c_n, N_cl_n, ok_n = _exact_N_accel_max_Hn(n_val)
        c_mp = mp.sqrt(rat_mp(3 * (n_val + 2), n_val))
        denom_mp = mp.mpf(9) - c_mp * c_mp
        N_n_mp = (
            (mp.mpf(3) / denom_mp) * mp.log((c_mp + s3) / (c_mp - s3))
            - (c_mp / denom_mp) * mp.log((s3 + mp.mpf(1)) / (s3 - mp.mpf(1)))
        )
        N_n_quad = mp.quad(
            lambda xv, cm=c_mp: mp.mpf(1) / ((mp.mpf(1) - xv * xv) * (cm - mp.mpf(3) * xv)),
            [lo_mp, hi_mp],
            method="gauss-legendre",
        )
        q_err = abs(N_n_quad - N_n_mp)
        hier_sym_ok = hier_sym_ok and ok_n and bool(q_err < tol_quad)
        hier_vals.append(N_n_mp)
        hierarchy[f"H^{n_val}"] = {
            "n": n_val,
            "gamma_curv": str(g_n),
            "c_eff": str(c_n),
            "N_accel_max_closed": str(N_cl_n),
            "N_accel_max_55dps": mp_str(N_n_mp),
            "quad_abs_err": mp_str(q_err, 12),
            "symbolic_pf_verified": ok_n,
        }

    ordering_ok = bool(
        hier_vals[0] < hier_vals[1] < hier_vals[2] < hier_vals[3] < mp.mpf(2)
    )
    band_ok = bool(rat_mp(81, 100) < N_exact_mp < rat_mp(82, 100))
    nogo_60_ok = bool(N_exact_mp < mp.mpf(1) and N_exact_mp < mp.mpf(60))

    passed = bool(
        sym_pf_ok_h3
        and direct_sym_matches_closed
        and card_formula_exact_match
        and band_ok
        and nogo_60_ok
        and bool(err_quad_gl < tol_quad)
        and bool(err_quad_ts < tol_quad)
        and events_1d_ok
        and bool(err_1d_ode < rat_mp(1, 10**11))
        and events_4d_ok
        and bool(err_4d_ode < rat_mp(1, 10**11))
        and bool(err_w_min < rat_mp(1, 10**12))
        and bool(err_w_t200 < rat_mp(2, 1000))
        and hier_sym_ok
        and ordering_ok
    )

    return {
        "methods": [
            "Heaviside_partial_fractions_sympy_integrate",
            "mpmath_70dps_gauss_legendre",
            "mpmath_70dps_tanh_sinh",
            "scipy_Radau_1D_autonomous_dx_dN",
            "scipy_Radau_4D_cosmic_time_Friedmann_exact_jac",
        ],
        "N_accel_max_H3_closed": str(N_closed_h3),
        "N_accel_max_H3_55dps": mp_str(N_exact_mp),
        "symbolic_pf_matches_closed": sym_pf_ok_h3,
        "direct_sympy_integrate_matches_closed": direct_sym_matches_closed,
        "matches_card_closed_form": card_formula_exact_match,
        "in_81_to_82_hundredths_band": band_ok,
        "single_radion_60_efold_nogo": nogo_60_ok,
        "quad_gauss_legendre_55dps": mp_str(N_quad_gl),
        "quad_gauss_legendre_abs_err": mp_str(err_quad_gl, 12),
        "quad_tanh_sinh_55dps": mp_str(N_quad_ts),
        "quad_tanh_sinh_abs_err": mp_str(err_quad_ts, 12),
        "ode_1d_radau": {
            "events_found": events_1d_ok,
            "N_accel_1d": N_accel_1d_ode,
            "abs_err_vs_exact": mp_str(err_1d_ode, 12),
            "x_at_N12": x_1d_end,
            "w_at_N12": w_1d_end,
        },
        "ode_4d_radau": {
            "events_found": events_4d_ok,
            "t_entry": t_entry_4d,
            "t_bounce": t_bounce_4d,
            "t_exit": t_exit_4d,
            "N_accel_4d": N_accel_4d_ode,
            "abs_err_vs_exact": mp_str(err_4d_ode, 12),
            "w_min_bounce": w_min_bounce,
            "w_min_plus_1_abs_err": mp_str(err_w_min, 12),
            "w_at_t200": w_t200,
            "w_at_t200_minus_1_9_abs_err": mp_str(err_w_t200, 12),
        },
        "dimension_hierarchy": hierarchy,
        "hierarchy_strict_ordering_lt_2": ordering_ok,
        "passed": passed,
    }


# ---------------------------------------------------------------------------
# Task OW14-A.3: 7D Hyperbolic Volume Stabilization (Manual QQ Sturm + Halley)
# ---------------------------------------------------------------------------

def _locate_unique_root_bisection_and_halley(
    poly: PolyQQ, lo_q: Fraction, hi_q: Fraction
) -> Dict[str, Any]:
    """
    Independently locate unique root in (lo_q, hi_q) via:
      (1) 235-step exact bracketed bisection at 70 dps
      (2) Halley's cubically convergent method starting from coarse midpoint
    """
    dpoly = poly_deriv(poly)
    ddpoly = poly_deriv(dpoly)

    a_mp = rat_mp(lo_q.numerator, lo_q.denominator)
    b_mp = rat_mp(hi_q.numerator, hi_q.denominator)
    fa = poly_eval_mp(poly, a_mp)
    fb = poly_eval_mp(poly, b_mp)
    if fa * fb >= 0:
        raise ValueError("Bracket endpoints do not straddle a root")

    # (1) Pure bisection to < 10^-65:
    lo_b, hi_b = a_mp, b_mp
    flo_b = fa
    for _ in range(235):
        mid = (lo_b + hi_b) / mp.mpf(2)
        fmid = poly_eval_mp(poly, mid)
        if flo_b * fmid <= 0:
            hi_b = mid
        else:
            lo_b = mid
            flo_b = fmid
    root_bisect = (lo_b + hi_b) / mp.mpf(2)

    # (2) Halley's method from initial midpoint (independent of bisection result):
    x_h = (a_mp + b_mp) / mp.mpf(2)
    for _ in range(25):
        fx = poly_eval_mp(poly, x_h)
        dfx = poly_eval_mp(dpoly, x_h)
        ddfx = poly_eval_mp(ddpoly, x_h)
        denom = mp.mpf(2) * dfx * dfx - fx * ddfx
        step = (mp.mpf(2) * fx * dfx) / denom
        x_h = x_h - step
        if abs(step) < rat_mp(1, 10**65):
            break
    root_halley = x_h

    return {
        "root_bisection": root_bisect,
        "root_halley": root_halley,
        "bisect_vs_halley_diff": abs(root_bisect - root_halley),
        "poly_residual_halley": abs(poly_eval_mp(poly, root_halley)),
    }


def run_ow14_a3() -> Dict[str, Any]:
    L = sp.Symbol("L", positive=True)
    a3, c5, c6, c9, c10 = sp.symbols("a3 c5 c6 c9 c10", positive=True)
    L_star_sym = sp.Symbol("L_star", positive=True)

    # Potential V(L) = -a3 L^-3 + c5 L^-5 + c9 L^-9 + c10 L^-10 (AdS bulk c3 = -a3 < 0)
    V_ads = -a3 * L**(-3) + c5 * L**(-5) + c9 * L**(-9) + c10 * L**(-10)
    dV_ads = sp.diff(V_ads, L)
    d2V_ads = sp.diff(V_ads, L, 2)

    # Symbolic elimination of a3 = |c3| from V'(L_*) = 0 (Guardrail 1: zero pinning of L_*):
    a3_from_stat = sp.solve(sp.Eq(dV_ads.subs(L, L_star_sym), 0), a3)[0]
    V_at_Lstar_sym = sp.factor(sp.together(V_ads.subs({L: L_star_sym, a3: a3_from_stat})))
    d2V_at_Lstar_sym = sp.factor(sp.together(d2V_ads.subs({L: L_star_sym, a3: a3_from_stat})))

    V_expected_sym = -(2 * c5 * L_star_sym**5 + 6 * c9 * L_star_sym + 7 * c10) / (3 * L_star_sym**10)
    d2V_expected_sym = 2 * (5 * c5 * L_star_sym**5 + 27 * c9 * L_star_sym + 35 * c10) / (L_star_sym**12)
    ads_V_match = sp.simplify(V_at_Lstar_sym - V_expected_sym) == 0
    ads_d2V_match = sp.simplify(d2V_at_Lstar_sym - d2V_expected_sym) == 0

    # Check strictly negative V(L_*) and strictly positive V''(L_*) for all positive c5, c9, c10, L_*:
    ads_V_strictly_neg = bool(sp.simplify(-V_at_Lstar_sym).is_positive)
    ads_d2V_strictly_pos = bool(sp.simplify(d2V_at_Lstar_sym).is_positive)

    # Manual exact-QQ Sturm root counts on V'(L) = -P(L) / L^11 => Q(L) = 3 c3 L^7 + 5 c5 L^5 + 9 c9 L + 10 c10
    # 1. Zero bulk (c3=0, c5=c9=c10=1): P(L) = 5 L^5 + 9 L + 10
    poly_zero_bulk: PolyQQ = [Fraction(10), Fraction(9), Fraction(0), Fraction(0), Fraction(0), Fraction(5)]
    sturm_zero = sturm_root_count_pos_inf(poly_zero_bulk)
    descartes_zero = descartes_sign_changes(poly_zero_bulk)

    # 2. dS bulk (c3=+1, c5=c9=c10=1): P(L) = 3 L^7 + 5 L^5 + 9 L + 10
    poly_ds_bulk: PolyQQ = [
        Fraction(10), Fraction(9), Fraction(0), Fraction(0),
        Fraction(0), Fraction(5), Fraction(0), Fraction(3),
    ]
    sturm_ds = sturm_root_count_pos_inf(poly_ds_bulk)
    descartes_ds = descartes_sign_changes(poly_ds_bulk)

    # 3. AdS bulk benchmark (c3=-1, c5=c9=c10=1): Q(L) = 3 L^7 - 5 L^5 - 9 L - 10
    poly_ads_bench: PolyQQ = [
        Fraction(-10), Fraction(-9), Fraction(0), Fraction(0),
        Fraction(0), Fraction(-5), Fraction(0), Fraction(3),
    ]
    sturm_ads = sturm_root_count_pos_inf(poly_ads_bench)
    descartes_ads = descartes_sign_changes(poly_ads_bench)

    # Locate unique L_* for benchmark (1, 1, 1, 1) at 70 dps via bisection + Halley:
    loc = _locate_unique_root_bisection_and_halley(poly_ads_bench, Fraction(1), Fraction(2))
    Lstar_mp = loc["root_halley"]
    V_bench_mp = -Lstar_mp**(-3) + Lstar_mp**(-5) + Lstar_mp**(-9) + Lstar_mp**(-10)
    dV_bench_mp = mp.mpf(3) * Lstar_mp**(-4) - mp.mpf(5) * Lstar_mp**(-6) - mp.mpf(9) * Lstar_mp**(-10) - mp.mpf(10) * Lstar_mp**(-11)
    d2V_bench_mp = -mp.mpf(12) * Lstar_mp**(-5) + mp.mpf(30) * Lstar_mp**(-7) + mp.mpf(90) * Lstar_mp**(-11) + mp.mpf(110) * Lstar_mp**(-12)

    V_elim_mp = -(mp.mpf(2) * Lstar_mp**5 + mp.mpf(6) * Lstar_mp + mp.mpf(7)) / (mp.mpf(3) * Lstar_mp**10)
    d2V_elim_mp = mp.mpf(2) * (mp.mpf(5) * Lstar_mp**5 + mp.mpf(27) * Lstar_mp + mp.mpf(35)) / (Lstar_mp**12)
    V_elim_err = abs(V_bench_mp - V_elim_mp)
    d2V_elim_err = abs(d2V_bench_mp - d2V_elim_mp)
    tol_60 = rat_mp(1, 10**60)

    # Minkowski lift: V_mink = c5 L^-5 - c6 L^-6 + c9 L^-9, solve V(L_*) = 0 and V'(L_*) = 0
    V_mink = c5 * L**(-5) - c6 * L**(-6) + c9 * L**(-9)
    dV_mink = sp.diff(V_mink, L)
    d2V_mink = sp.diff(V_mink, L, 2)
    mink_sol = sp.solve(
        [sp.Eq(V_mink.subs(L, L_star_sym), 0), sp.Eq(dV_mink.subs(L, L_star_sym), 0)],
        [c6, c9],
        dict=True,
    )[0]
    c6_mink = sp.simplify(mink_sol[c6])
    c9_mink = sp.simplify(mink_sol[c9])
    d2V_mink_at_Lstar = sp.simplify(d2V_mink.subs({L: L_star_sym, c6: c6_mink, c9: c9_mink}))

    mink_c6_ok = sp.simplify(c6_mink - sp.Rational(4, 3) * c5 * L_star_sym) == 0
    mink_c9_ok = sp.simplify(c9_mink - sp.Rational(1, 3) * c5 * L_star_sym**4) == 0
    mink_d2V_ok = sp.simplify(d2V_mink_at_Lstar - 4 * c5 / L_star_sym**7) == 0
    mink_d2V_pos = bool(d2V_mink_at_Lstar.is_positive)

    # Bonus Sturm check on Minkowski lift derivative at c5=1, L_*=1:
    # V'_mink = (-5 L^4 + 8 L^3 - 3) / L^10; numerator P_mink'(L) = -5 L^4 + 8 L^3 - 3 = -(L - 1)(5 L^3 - 3 L^2 - 3 L - 3)
    poly_mink_dV: PolyQQ = [Fraction(-3), Fraction(0), Fraction(0), Fraction(8), Fraction(-5)]
    sturm_mink_dV = sturm_root_count_pos_inf(poly_mink_dV)
    # Check V_mink(L) numerator 3 L^4 - 4 L^3 + 1 = (L-1)^2 (3 L^2 + 2 L + 1) has gcd degree 1 (double root at L=1) and unique positive root:
    poly_mink_V: PolyQQ = [Fraction(1), Fraction(0), Fraction(0), Fraction(-4), Fraction(3)]
    sturm_mink_V = sturm_root_count_pos_inf(poly_mink_V)

    passed = bool(
        (sturm_zero["positive_real_roots"] == 0)
        and (descartes_zero == 0)
        and (sturm_ds["positive_real_roots"] == 0)
        and (descartes_ds == 0)
        and (sturm_ads["positive_real_roots"] == 1)
        and (descartes_ads == 1)
        and bool(loc["bisect_vs_halley_diff"] < tol_60)
        and bool(loc["poly_residual_halley"] < tol_60)
        and bool(abs(dV_bench_mp) < tol_60)
        and bool(V_bench_mp < 0)
        and bool(d2V_bench_mp > 0)
        and bool(V_elim_err < tol_60)
        and bool(d2V_elim_err < tol_60)
        and ads_V_match
        and ads_d2V_match
        and ads_V_strictly_neg
        and ads_d2V_strictly_pos
        and mink_c6_ok
        and mink_c9_ok
        and mink_d2V_ok
        and mink_d2V_pos
        and (sturm_mink_V["positive_real_roots"] == 1)
        and (sturm_mink_V["gcd_degree"] == 1)
    )

    return {
        "methods": [
            "manual_exact_QQ_Sturm_sequence",
            "Descartes_sign_rule",
            "mpmath_70dps_bisection_and_Halley",
            "symbolic_a3_elimination",
        ],
        "zero_bulk_sturm": sturm_zero,
        "zero_bulk_descartes": descartes_zero,
        "ds_bulk_sturm": sturm_ds,
        "ds_bulk_descartes": descartes_ds,
        "ads_benchmark_sturm": sturm_ads,
        "ads_benchmark_descartes": descartes_ads,
        "ads_benchmark_L_star_55dps": mp_str(Lstar_mp),
        "ads_benchmark_bisect_vs_halley_diff": mp_str(loc["bisect_vs_halley_diff"], 12),
        "ads_benchmark_dV_residual": mp_str(abs(dV_bench_mp), 12),
        "ads_benchmark_V_L_star_55dps": mp_str(V_bench_mp),
        "ads_benchmark_d2V_L_star_55dps": mp_str(d2V_bench_mp),
        "ads_benchmark_V_elim_diff": mp_str(V_elim_err, 12),
        "ads_benchmark_d2V_elim_diff": mp_str(d2V_elim_err, 12),
        "ads_symbolic_a3_eliminated": str(a3_from_stat),
        "ads_symbolic_V_L_star": str(V_at_Lstar_sym),
        "ads_symbolic_d2V_L_star": str(d2V_at_Lstar_sym),
        "ads_symbolic_V_matches": ads_V_match,
        "ads_symbolic_d2V_matches": ads_d2V_match,
        "ads_symbolic_strictly_AdS_and_stable": bool(ads_V_strictly_neg and ads_d2V_strictly_pos),
        "minkowski_lift": {
            "c6_exact": str(c6_mink),
            "c9_exact": str(c9_mink),
            "d2V_L_star_exact": str(d2V_mink_at_Lstar),
            "matches_expected": bool(mink_c6_ok and mink_c9_ok and mink_d2V_ok),
            "stable_positive_mass_sq": mink_d2V_pos,
            "sturm_mink_V_unit_benchmark": sturm_mink_V,
            "sturm_mink_dV_unit_benchmark": sturm_mink_dV,
        },
        "passed": passed,
    }


# ---------------------------------------------------------------------------
# Task OW14-B.1: Unimodular Trace-Free Decoupling & Klein-Gordon Preservation
# ---------------------------------------------------------------------------

def run_ow14_b1(V_Lstar_mp: mp.mpf) -> Dict[str, Any]:
    # 1. General 10-parameter non-diagonal symmetric 4x4 Lorentzian metric via g = L D L^T
    #    with unimodular constraint det(g) = -1 <=> d0 = 1 / (d1*d2*d3).
    d1, d2, d3 = sp.symbols("d1 d2 d3", positive=True)
    d0 = 1 / (d1 * d2 * d3)
    l10, l20, l21, l30, l31, l32 = sp.symbols("l10 l20 l21 l30 l31 l32", real=True)
    L_mat = sp.Matrix([
        [1, 0, 0, 0],
        [l10, 1, 0, 0],
        [l20, l21, 1, 0],
        [l30, l31, l32, 1],
    ])
    D_mat = sp.diag(-d0, d1, d2, d3)
    g_mat = sp.expand(L_mat * D_mat * L_mat.T)
    L_inv = L_mat.inv()
    D_inv = sp.diag(-1 / d0, 1 / d1, 1 / d2, 1 / d3)
    g_inv = sp.expand(L_inv.T * D_inv * L_inv)

    # Verify g is symmetric, non-diagonal, unimodular (det g == -1), g * g_inv == I_4, g^{ab} g_{ab} == 4:
    is_symmetric = all(sp.expand(g_mat[a, b] - g_mat[b, a]) == 0 for a in range(4) for b in range(4))
    offdiag_nonzero_count = sum(1 for a in range(4) for b in range(4) if a != b and g_mat[a, b] != 0)
    det_g = sp.expand(g_mat.det(method="berkowitz"))
    inv_prod = g_mat * g_inv - sp.eye(4)
    inv_exact_ok = all(sp.expand(inv_prod[a, b]) == 0 for a in range(4) for b in range(4))
    trace_g_contraction = sp.expand(sum(g_inv[a, b] * g_mat[a, b] for a in range(4) for b in range(4)))

    # Arbitrary symmetric 4x4 stress-energy tensor T_{ab} (10 independent symbols) + symbolic rho_vac shift:
    t_syms = {}
    for a in range(4):
        for b in range(a, 4):
            t_syms[(a, b)] = sp.Symbol(f"T_{a}{b}", real=True)
            t_syms[(b, a)] = t_syms[(a, b)]
    T_mat = sp.Matrix(4, 4, lambda a, b: t_syms[(a, b)])
    rho_vac = sp.Symbol("rho_vac", real=True)
    T_shifted = T_mat - rho_vac * g_mat

    T_trace = sp.expand(sum(g_inv[a, b] * T_mat[a, b] for a in range(4) for b in range(4)))
    T_hat = T_mat - sp.Rational(1, 4) * g_mat * T_trace

    T_sh_trace = sp.expand(sum(g_inv[a, b] * T_shifted[a, b] for a in range(4) for b in range(4)))
    T_sh_hat = T_shifted - sp.Rational(1, 4) * g_mat * T_sh_trace

    # Verify trace-freeness of T_hat and 16/16 exact vanishing of T_sh_hat - T_hat:
    trace_That = sp.expand(sum(g_inv[a, b] * T_hat[a, b] for a in range(4) for b in range(4)))
    diff_That_zero_entries = 0
    for a in range(4):
        for b in range(4):
            if sp.expand(T_sh_hat[a, b] - T_hat[a, b]) == 0:
                diff_That_zero_entries += 1

    # Also verify trace-free Ricci tensor R_{ab} - (1/4) g_{ab} R invariant under R_{ab} -> R_{ab} + Lam * g_{ab}:
    Lam_sym = sp.Symbol("Lam_shift", real=True)
    R_hat_diff_zero_entries = 0
    R_shifted = T_mat + Lam_sym * g_mat  # reuse arbitrary symmetric 10-param tensor
    R_sh_trace = sp.expand(sum(g_inv[a, b] * R_shifted[a, b] for a in range(4) for b in range(4)))
    R_sh_hat = R_shifted - sp.Rational(1, 4) * g_mat * R_sh_trace
    for a in range(4):
        for b in range(4):
            if sp.expand(R_sh_hat[a, b] - T_hat[a, b]) == 0:
                R_hat_diff_zero_entries += 1

    # Explicit decoupling test on concrete vacuum shifts a_0 = -64, 6D bulk {-6, -2, -1}, and V(L_*) < 0:
    concrete_shifts_ok = True
    for shift_val in (sp.Integer(-64), sp.Integer(-6), sp.Integer(-2), sp.Integer(-1), sp.Rational(int(mp.floor(V_Lstar_mp * 10**12)), 10**12)):
        for a in range(4):
            for b in range(4):
                if sp.expand((T_sh_hat[a, b] - T_hat[a, b]).subs(rho_vac, shift_val)) != 0:
                    concrete_shifts_ok = False

    # 2. Exact Klein-Gordon preservation on curved 4D unimodular metric (det g = -1):
    #    g_{mu nu} = diag(-a(t)^-6, a(t)^2, a(t)^2, a(t)^2), phi = phi(t, x), arbitrary V(phi) + const rho_vac.
    t_c, x_c, y_c, z_c = sp.symbols("t x y z", real=True)
    coords = (t_c, x_c, y_c, z_c)
    a_f = sp.Function("a")(t_c)
    phi_f = sp.Function("phi")(t_c, x_c)
    V_f = sp.Function("V")
    V_expr = V_f(phi_f)
    V_prime_expr = sp.diff(V_expr, phi_f)

    g_uni = sp.diag(-a_f**(-6), a_f**2, a_f**2, a_f**2)
    g_uni_inv = sp.diag(-a_f**6, a_f**(-2), a_f**(-2), a_f**(-2))
    det_g_uni = sp.simplify(g_uni.det())  # -1 identically => sqrt(-g) = 1

    dphi = [sp.diff(phi_f, c) for c in coords]
    grad_phi_sq = sum(g_uni_inv[mu, nu] * dphi[mu] * dphi[nu] for mu in range(4) for nu in range(4))
    T_phi = sp.Matrix(
        4,
        4,
        lambda mu, nu: dphi[mu] * dphi[nu] - g_uni[mu, nu] * (sp.Rational(1, 2) * grad_phi_sq + V_expr + rho_vac),
    )
    T_up_dn = g_uni_inv * T_phi
    T_up_up = g_uni_inv * T_phi * g_uni_inv

    # Exact Box phi = (1/sqrt(-g)) d_mu(sqrt(-g) g^{mu nu} d_nu phi) with sqrt(-g) = 1:
    box_phi = sum(
        sp.diff(g_uni_inv[mu, nu] * dphi[nu], coords[mu])
        for mu in range(4)
        for nu in range(4)
    )

    # Exact covariant divergence nabla_mu T^mu_nu = d_mu(T^mu_nu) - (1/2) (d_nu g_{ab}) T^{ab} (since sqrt(-g) = 1):
    kg_components_ok = 0
    rho_vac_indep_ok = 0
    for nu in range(4):
        div_nu = sum(sp.diff(T_up_dn[mu, nu], coords[mu]) for mu in range(4)) - sp.Rational(1, 2) * sum(
            sp.diff(g_uni[a, b], coords[nu]) * T_up_up[a, b]
            for a in range(4)
            for b in range(4)
        )
        resid_nu = sp.simplify(div_nu - (box_phi - V_prime_expr) * dphi[nu])
        if resid_nu == 0:
            kg_components_ok += 1
        if sp.simplify(sp.diff(div_nu, rho_vac)) == 0:
            rho_vac_indep_ok += 1

    passed = bool(
        is_symmetric
        and (offdiag_nonzero_count == 12)
        and (det_g == -1)
        and inv_exact_ok
        and (trace_g_contraction == 4)
        and (trace_That == 0)
        and (diff_That_zero_entries == 16)
        and (R_hat_diff_zero_entries == 16)
        and concrete_shifts_ok
        and (det_g_uni == -1)
        and (kg_components_ok == 4)
        and (rho_vac_indep_ok == 4)
    )

    return {
        "metric_type": "general_10_param_nondiagonal_unimodular_LDLT",
        "is_symmetric": is_symmetric,
        "offdiagonal_nonzero_entries": offdiag_nonzero_count,
        "det_g_general": str(det_g),
        "g_times_ginv_equals_I4": inv_exact_ok,
        "g_up_ab_g_dn_ab": str(trace_g_contraction),
        "trace_of_tracefree_T": str(trace_That),
        "tracefree_T_shift_zero_entries": diff_That_zero_entries,
        "tracefree_R_shift_zero_entries": R_hat_diff_zero_entries,
        "concrete_vacuum_shifts_decoupled": concrete_shifts_ok,
        "unimodular_FLRW_det_g": str(det_g_uni),
        "klein_gordon_exact_components_verified": kg_components_ok,
        "div_T_rho_vac_independent_components": rho_vac_indep_ok,
        "passed": passed,
    }


# ---------------------------------------------------------------------------
# Task OW14-B.2: Unimodular FRG, Delta(2,3,N) PermutationGroup Enum, A2-OW13 Bridges
# ---------------------------------------------------------------------------

def _enumerate_delta_23N_coset_actions(include_N1: bool = False) -> Dict[str, Any]:
    """
    Enumerate faithful transitive coset actions of Delta(2,3,N) directly via
    sympy.combinatorics.Permutation / PermutationGroup (Schreier-Sims order verification).
    """
    specs: List[Tuple[int, str, int, List[Permutation]]] = []
    if include_N1:
        specs.append((1, "C1", 1, [Permutation([0])]))
    specs.extend([
        (2, "S3", 6, [Permutation([[0, 1]], size=3), Permutation([[0, 1, 2]], size=3)]),
        (3, "A4", 12, [Permutation([[0, 1], [2, 3]], size=4), Permutation([[0, 1, 2]], size=4)]),
        (4, "S4", 24, [Permutation([[0, 1]], size=4), Permutation([[1, 2, 3]], size=4)]),
        (5, "A5", 60, [Permutation([[0, 1], [2, 3]], size=5), Permutation([[0, 2, 4]], size=5)]),
    ])

    all_faithful: List[Dict[str, Any]] = []
    per_N_summary: Dict[str, Any] = {}
    all_relations_ok = True
    all_orbit_stab_ok = True
    all_schreier_faithful_ok = True

    for N_val, gname, expected_order, gens in specs:
        G = PermutationGroup(*gens)
        order_ss = int(G.order())
        if N_val >= 2:
            S_gen, T_gen = gens[0], gens[1]
            rel_ok = bool(
                (S_gen.order() == 2)
                and (T_gen.order() == 3)
                and ((S_gen * T_gen).order() == N_val)
                and (order_ss == expected_order)
            )
        else:
            S_gen = T_gen = gens[0]
            rel_ok = bool(order_ss == expected_order)
        all_relations_ok = all_relations_ok and rel_ok

        elems = list(G.generate())
        n = len(elems)
        idx = {e: i for i, e in enumerate(elems)}
        id_i = idx[G.identity]
        mul = [[idx[elems[i] * elems[j]] for j in range(n)] for i in range(n)]
        inv = [idx[~elems[i]] for i in range(n)]

        # Enumerate complete subgroup lattice via iterative single-generator closure:
        subgroups = {frozenset([id_i])}
        queue = [frozenset([id_i])]
        while queue:
            H = queue.pop()
            for g in range(n):
                if g not in H:
                    H2 = set(H)
                    frontier = {g}
                    while frontier:
                        H2 |= frontier
                        nxt = set()
                        for a in list(H2):
                            for b in frontier:
                                ab = mul[a][b]
                                if ab not in H2:
                                    nxt.add(ab)
                                ba = mul[b][a]
                                if ba not in H2:
                                    nxt.add(ba)
                        frontier = nxt
                    fH2 = frozenset(H2)
                    if fH2 not in subgroups:
                        subgroups.add(fH2)
                        queue.append(fH2)

        # Partition subgroups into conjugacy classes & check core-freeness:
        rem = set(subgroups)
        total_classes = 0
        sum_class_sizes = 0
        faithful_for_N: List[Dict[str, Any]] = []

        while rem:
            H = next(iter(rem))
            conj_class = {
                frozenset(mul[mul[g][h]][inv[g]] for h in H)
                for g in range(n)
            }
            rem -= conj_class
            total_classes += 1
            sum_class_sizes += len(conj_class)

            core = set(range(n))
            for C in conj_class:
                core &= C
            is_core_free = (len(core) == 1) and (id_i in core)
            if not is_core_free:
                continue

            # Build explicit left cosets G/H and verify faithfulness via SymPy PermutationGroup order:
            cosets: List[frozenset] = []
            seen = set()
            for g in range(n):
                if g not in seen:
                    c = frozenset(mul[g][h] for h in H)
                    cosets.append(c)
                    seen |= c
            d = len(cosets)
            cidx = {c: i for i, c in enumerate(cosets)}

            def _coset_perm(gen_elem: Permutation) -> Permutation:
                gi = idx[gen_elem]
                arr = [cidx[frozenset(mul[gi][x] for x in c)] for c in cosets]
                return Permutation(arr)

            rho_S = _coset_perm(S_gen)
            rho_T = _coset_perm(T_gen)
            img_group = PermutationGroup(rho_S, rho_T)
            img_order = int(img_group.order())
            schreier_faithful = (img_order == n)
            all_schreier_faithful_ok = all_schreier_faithful_ok and schreier_faithful

            # Commutator subgroup [H, H] -> abelianization order |H/[H,H]| = number of 1D irreps of H:
            comm = {id_i}
            for a in H:
                for b in H:
                    comm.add(mul[mul[a][b]][mul[inv[a]][inv[b]]])
            changed = True
            while changed:
                changed = False
                add = set()
                for a in comm:
                    for b in comm:
                        ab = mul[a][b]
                        if ab not in comm:
                            add.add(ab)
                if add:
                    comm |= add
                    changed = True
            ab_order = len(H) // len(comm)

            # Cycle counts of S, T, ST on G/H:
            def _cycle_count(perm_p: Permutation) -> int:
                return perm_p.cycles

            # Spin(2d) chirality & anomaly-freedom + M_g prescriptions:
            # - Half-spinor 2^{d-1} of Spin(2d) is complex (chiral) iff d is odd.
            # - Spin(2d) is gauge anomaly-free iff d not in {1, 3} (Spin(2)=U(1), Spin(6)=SU(4) have cubic anomalies).
            chiral = (d % 2 == 1)
            anomaly_free = (d not in (1, 3))

            # Three independent physically principled M_g formulas for degree-d models:
            # (a) Broken SM-like SU(d-2) x SU(2) x U(1) + 2H (d >= 3) with N_gen = 3 spinors 2^{d-1}:
            if d >= 3:
                nv_broken = ((d - 2) ** 2 - 1) + 3 + 1
                mg_broken_3gen = 8 + 3 * (2 ** (d - 1)) - 4 * nv_broken
            else:
                mg_broken_3gen = 8 + 3 * (2 ** (d - 1)) - 4 * 1
            # (b) G_SM + 2H with N_gen = |H/[H,H]| (stabilizer abelianization):
            mg_gsm_hab = 16 * ab_order - 40
            # (c) G_SM + 2H with N_gen = c(T) (order-3 generator orbits):
            cT = _cycle_count(rho_T)
            mg_gsm_cT = 16 * cT - 40

            entry = {
                "N": N_val,
                "group": gname,
                "order_G": n,
                "order_H": len(H),
                "degree_d": d,
                "conj_class_size": len(conj_class),
                "H_abelianization_order": ab_order,
                "cycles_S": _cycle_count(rho_S),
                "cycles_T": cT,
                "cycles_ST": _cycle_count(_coset_perm(S_gen * T_gen)),
                "schreier_sims_faithful": schreier_faithful,
                "chiral": chiral,
                "anomaly_free": anomaly_free,
                "M_g_broken_3gen": mg_broken_3gen,
                "M_g_gsm_Hab": mg_gsm_hab,
                "M_g_gsm_cT": mg_gsm_cT,
                "survives_cap23_broken_3gen": bool(chiral and anomaly_free and (0 < mg_broken_3gen < 23)),
                "survives_cap22_broken_3gen": bool(chiral and anomaly_free and (0 < mg_broken_3gen < 22)),
                "survives_cap23_gsm_Hab": bool(chiral and anomaly_free and (0 < mg_gsm_hab < 23)),
                "survives_cap22_gsm_Hab": bool(chiral and anomaly_free and (0 < mg_gsm_hab < 22)),
                "survives_cap23_gsm_cT": bool(chiral and anomaly_free and (0 < mg_gsm_cT < 23)),
                "survives_cap22_gsm_cT": bool(chiral and anomaly_free and (0 < mg_gsm_cT < 22)),
            }
            faithful_for_N.append(entry)

        faithful_for_N.sort(key=lambda r: (r["degree_d"], r["conj_class_size"], r["cycles_S"]))
        all_orbit_stab_ok = all_orbit_stab_ok and (sum_class_sizes == len(subgroups))
        all_faithful.extend(faithful_for_N)
        per_N_summary[f"N={N_val}"] = {
            "group": gname,
            "order_G": n,
            "relations_verified": rel_ok,
            "total_subgroups": len(subgroups),
            "total_conjugacy_classes": total_classes,
            "faithful_coset_actions": len(faithful_for_N),
            "faithful_degrees": [r["degree_d"] for r in faithful_for_N],
        }

    def _survivors(key: str) -> List[Tuple[int, int]]:
        return [(r["N"], r["degree_d"]) for r in all_faithful if r[key]]

    surv_23_a = _survivors("survives_cap23_broken_3gen")
    surv_22_a = _survivors("survives_cap22_broken_3gen")
    surv_23_b = _survivors("survives_cap23_gsm_Hab")
    surv_22_b = _survivors("survives_cap22_gsm_Hab")
    surv_23_c = _survivors("survives_cap23_gsm_cT")
    surv_22_c = _survivors("survives_cap22_gsm_cT")

    unique_N5_d5_all = bool(
        surv_23_a == [(5, 5)]
        and surv_22_a == [(5, 5)]
        and surv_23_b == [(5, 5)]
        and surv_22_b == [(5, 5)]
        and surv_23_c == [(5, 5)]
        and surv_22_c == [(5, 5)]
    )

    return {
        "include_N1": include_N1,
        "total_faithful_actions": len(all_faithful),
        "per_N_summary": per_N_summary,
        "all_triangle_relations_verified": all_relations_ok,
        "orbit_stabilizer_subgroup_sum_verified": all_orbit_stab_ok,
        "all_schreier_sims_faithful_verified": all_schreier_faithful_ok,
        "survivors_cap23_broken_3gen": surv_23_a,
        "survivors_cap22_broken_3gen": surv_22_a,
        "survivors_cap23_gsm_Hab": surv_23_b,
        "survivors_cap22_gsm_Hab": surv_22_b,
        "survivors_cap23_gsm_cT": surv_23_c,
        "survivors_cap22_gsm_cT": surv_22_c,
        "unique_N5_d5_survivor_all_prescriptions_and_caps": unique_N5_d5_all,
        "actions": all_faithful,
    }


def run_ow14_b2() -> Dict[str, Any]:
    g_sym, M_sym, cap_sym = sp.symbols("g M_g cap", real=True)
    # General unimodular Litim Type-II FRG at lam = 0:
    # B_1(0) = (M_g - (cap - 1)) / (6 pi),  B_2(0) = 1 / (12 pi)
    # eta_N(g) = g B_1 / (1 - g B_2),  beta_g(g) = (2 + eta_N(g)) * g
    B1_gen = (M_sym - (cap_sym - 1)) / (6 * sp.pi)
    B2_gen = 1 / (12 * sp.pi)
    eta_N_gen = g_sym * B1_gen / (1 - g_sym * B2_gen)
    beta_g_gen = sp.simplify((2 + eta_N_gen) * g_sym)

    # Solve beta_g(g) = 0 for non-Gaussian fixed point g_* != 0:
    fp_sols = sp.solve(sp.Eq(beta_g_gen, 0), g_sym)
    g_star_gen = [s for s in fp_sols if s != 0][0]
    g_star_expected = 12 * sp.pi / (cap_sym - M_sym)
    g_star_closed_ok = sp.simplify(g_star_gen - g_star_expected) == 0

    # Critical exponent theta_g = -d(beta_g)/dg |_{g = g_*}:
    theta_g_gen = sp.simplify(-sp.diff(beta_g_gen, g_sym).subs(g_sym, g_star_gen))
    theta_g_expected = 2 * (cap_sym - M_sym) / (cap_sym - 1 - M_sym)
    theta_g_closed_ok = sp.simplify(theta_g_gen - theta_g_expected) == 0

    # Verify theta_g - 2 = 2 / (cap - 1 - M_g) > 0 for all M_g < cap - 1:
    theta_minus_2 = sp.simplify(theta_g_gen - 2)
    theta_gt2_ok = sp.simplify(theta_minus_2 - 2 / (cap_sym - 1 - M_sym)) == 0

    # Double Pincer 0 < M_g < cap for G_SM + 2H:
    # First-principles matter counting: N_S = 8 (2 complex doublets), N_W = 16 * N_gen (16 Weyl per gen), N_V = 12 (8+3+1)
    N_gen_sym = sp.Symbol("N_gen", real=True)
    M_g_SM = 8 + 16 * N_gen_sym - 4 * 12  # 16*N_gen - 40
    M_g_SM_ok = sp.simplify(M_g_SM - (16 * N_gen_sym - 40)) == 0

    pincer_results: Dict[str, Any] = {}
    for label, cap_val in (("full_cap23", 23), ("traceless_cap22", 22)):
        lo_bound = sp.solve(sp.Eq(M_g_SM, 0), N_gen_sym)[0]
        hi_bound = sp.solve(sp.Eq(M_g_SM, cap_val), N_gen_sym)[0]
        allowed_ints = [
            k for k in range(0, 10)
            if (0 < int(M_g_SM.subs(N_gen_sym, k)) < cap_val)
        ]
        M_g_3 = int(M_g_SM.subs(N_gen_sym, 3))
        M_g_4 = int(M_g_SM.subs(N_gen_sym, 4))
        g_star_3 = sp.simplify(g_star_gen.subs({cap_sym: cap_val, M_sym: M_g_3}))
        theta_3 = sp.simplify(theta_g_gen.subs({cap_sym: cap_val, M_sym: M_g_3}))
        g_star_4 = sp.simplify(g_star_gen.subs({cap_sym: cap_val, M_sym: M_g_4}))
        pincer_results[label] = {
            "cap": cap_val,
            "N_gen_lower_bound": str(lo_bound),
            "N_gen_upper_bound": str(hi_bound),
            "allowed_integer_N_gen": allowed_ints,
            "unique_N_gen_3": bool(allowed_ints == [3]),
            "N_gen_3_M_g": M_g_3,
            "N_gen_3_g_star": str(g_star_3),
            "N_gen_3_g_star_float": float(sp.N(g_star_3, 30)),
            "N_gen_3_theta_g": str(theta_3),
            "N_gen_3_theta_g_gt_2": bool(theta_3 > 2),
            "N_gen_4_M_g": M_g_4,
            "N_gen_4_g_star": str(g_star_4),
            "N_gen_4_excluded_neg_g_star": bool(sp.simplify(g_star_4 / sp.pi) < 0),
        }

    # Explicitly flag the arithmetic check on traceless cap=22 theta_g = 28/13 vs card prose "14/6 = 7/3":
    theta_cap23_exact = sp.Rational(pincer_results["full_cap23"]["N_gen_3_theta_g"])
    theta_cap22_exact = sp.Rational(pincer_results["traceless_cap22"]["N_gen_3_theta_g"])
    cap23_exact_ok = bool(
        (sp.simplify(sp.sympify(pincer_results["full_cap23"]["N_gen_3_g_star"]) - 4 * sp.pi / 5) == 0)
        and (theta_cap23_exact == sp.Rational(15, 7))
    )
    cap22_exact_ok = bool(
        (sp.simplify(sp.sympify(pincer_results["traceless_cap22"]["N_gen_3_g_star"]) - 6 * sp.pi / 7) == 0)
        and (theta_cap22_exact == sp.Rational(28, 13))
    )
    card_line58_prose_discrepancy = {
        "computed_theta_g_cap22": str(theta_cap22_exact),
        "card_line55_formula_at_cap22_Mg8": str(sp.simplify(theta_g_expected.subs({cap_sym: 22, M_sym: 8}))),
        "card_line58_prose_value": "7/3",
        "exact_diff_computed_minus_card_prose": str(theta_cap22_exact - sp.Rational(7, 3)),
        "note": "Exact beta_g'(g_*) and Card line 55 formula 2*(cap - M_g)/(cap - 1 - M_g) both give 2*(22-8)/(21-8) = 28/13; Card line 58 prose '14/6 = 7/3' has 21-8 miscomputed as 12.",
    }

    # Enumerate Delta(2,3,N) faithful coset actions for N=2..5 (exact count = 20) and N=1..5 (count = 21):
    delta_N2_to_5 = _enumerate_delta_23N_coset_actions(include_N1=False)
    delta_N1_to_5 = _enumerate_delta_23N_coset_actions(include_N1=True)

    # UV Spin(10) real-10: N_S = 10, N_W = 3 * 16 = 48, N_V = 10*9/2 = 45
    M_g_so10_II = 10 + 48 - 4 * 45  # -122
    M_g_so10_I = 10 + 2 * 48 - 4 * 45  # -74
    spin10_checks: Dict[str, Any] = {}
    spin10_all_ok = True
    for rtype, mg_val, exp_full, exp_tr in (
        ("Type_II", M_g_so10_II, 12 * sp.pi / 145, sp.pi / 12),
        ("Type_I", M_g_so10_I, 12 * sp.pi / 97, sp.pi / 8),
    ):
        g_full = sp.simplify(g_star_gen.subs({cap_sym: 23, M_sym: mg_val}))
        th_full = sp.simplify(theta_g_gen.subs({cap_sym: 23, M_sym: mg_val}))
        g_tr = sp.simplify(g_star_gen.subs({cap_sym: 22, M_sym: mg_val}))
        th_tr = sp.simplify(theta_g_gen.subs({cap_sym: 22, M_sym: mg_val}))
        ok_r = bool(
            (sp.simplify(g_full - exp_full) == 0)
            and (sp.simplify(g_tr - exp_tr) == 0)
            and (sp.simplify(g_full / sp.pi) > 0)
            and (sp.simplify(g_tr / sp.pi) > 0)
            and (th_full > 2)
            and (th_tr > 2)
        )
        spin10_all_ok = spin10_all_ok and ok_r
        spin10_checks[rtype] = {
            "M_g": mg_val,
            "full_cap23_g_star": str(g_full),
            "full_cap23_theta_g": str(th_full),
            "traceless_cap22_g_star": str(g_tr),
            "traceless_cap22_theta_g": str(th_tr),
            "survives_both_caps": ok_r,
        }

    # A2-OW13 Bridges at lam = 0:
    # (i) Background-field f_xi^{bg}(lam) derived directly from F_k(phi) = k^2/(16 pi g) - (1/2) xi phi^2
    #     with lam_eff(phi) = lam / (1 - 8 pi g xi phi_tilde^2):
    lam_sym, xi_sym, phi_t2, eta_sym = sp.symbols("lam xi phi_tilde_sq eta_N", real=True)
    B1_fn = sp.Function("B1")
    B2_fn = sp.Function("B2")
    lam_eff = lam_sym / (1 - 8 * sp.pi * g_sym * xi_sym * phi_t2)
    # partial_t F_k(phi) / k^2 = -(1/(16 pi)) * [B1(lam_eff) + eta_N * B2(lam_eff)]
    # beta_xi^{bg} = -2 * d/d(phi_tilde^2) [partial_t F_k / k^2] |_{phi=0} = f_xi^{bg}(lam) * xi
    dt_F_dimless = -(1 / (16 * sp.pi)) * (B1_fn(lam_eff) + eta_sym * B2_fn(lam_eff))
    beta_xi_bg = sp.simplify(-2 * sp.diff(dt_F_dimless, phi_t2).subs(phi_t2, 0))
    f_xi_bg_lam = sp.simplify(beta_xi_bg / xi_sym)
    f_xi_bg_at_0 = sp.simplify(f_xi_bg_lam.subs(lam_sym, 0))

    # Concrete Litim B1(lam), B2(lam) check (smooth rational at lam=0, poles at lam=1/2):
    B1_litim = (M_sym - 22) / (6 * sp.pi * (1 - 2 * lam_sym)**2)
    B2_litim = 1 / (12 * sp.pi * (1 - 2 * lam_sym)**2)
    f_xi_bg_litim = sp.simplify(
        g_sym * lam_sym * (sp.diff(B1_litim, lam_sym) + eta_sym * sp.diff(B2_litim, lam_sym))
    )
    f_xi_bg_litim_at_0 = sp.simplify(f_xi_bg_litim.subs(lam_sym, 0))

    # (ii) De Donder 10-mode Wetterich trace derivation of f_lam^{(dD)}(lam):
    #      partial_t u_grav(u) = (10 / (32 pi^2)) * (1 - eta_N/6) / (1 - 2 lam - 16 pi g u)
    #      f_lam^{(dD)}(lam) = d(partial_t u_grav)/du |_{u=0}
    u_sym = sp.Symbol("u", real=True)
    y_int = sp.Symbol("y", positive=True)
    # Direct Litim momentum integral: int_0^1 y * (2 - eta_N*(1 - y)) dy = 1 - eta_N/6
    litim_thresh = sp.integrate(y_int * (2 - eta_sym * (1 - y_int)), (y_int, 0, 1))
    dt_u_grav = sp.Rational(10, 32) / sp.pi**2 * litim_thresh / (1 - 2 * lam_sym - 16 * sp.pi * g_sym * u_sym)
    f_lam_dD = sp.simplify(sp.diff(dt_u_grav, u_sym).subs(u_sym, 0))
    f_lam_dD_fp_lam0 = sp.simplify(f_lam_dD.subs({eta_sym: -2, lam_sym: 0}))
    f_lam_dD_formula_ok = sp.simplify(f_lam_dD_fp_lam0 - 20 * g_sym / (3 * sp.pi)) == 0

    g_star_gsm_full = sp.simplify(g_star_gen.subs({cap_sym: 23, M_sym: 8}))
    f_lam_gsm_full = sp.simplify(f_lam_dD_fp_lam0.subs(g_sym, g_star_gsm_full))
    f_crit = sp.Rational(404, 10000)
    f_lam_ratio = sp.simplify(f_lam_gsm_full / f_crit)
    f_lam_cures_wall = bool(
        (f_lam_gsm_full == sp.Rational(16, 3))
        and (f_lam_gsm_full > 5)
        and (f_lam_gsm_full > f_crit)
    )

    passed = bool(
        g_star_closed_ok
        and theta_g_closed_ok
        and theta_gt2_ok
        and M_g_SM_ok
        and pincer_results["full_cap23"]["unique_N_gen_3"]
        and pincer_results["full_cap23"]["N_gen_4_excluded_neg_g_star"]
        and pincer_results["traceless_cap22"]["unique_N_gen_3"]
        and pincer_results["traceless_cap22"]["N_gen_4_excluded_neg_g_star"]
        and cap23_exact_ok
        and cap22_exact_ok
        and delta_N2_to_5["all_triangle_relations_verified"]
        and delta_N2_to_5["orbit_stabilizer_subgroup_sum_verified"]
        and delta_N2_to_5["all_schreier_sims_faithful_verified"]
        and delta_N2_to_5["unique_N5_d5_survivor_all_prescriptions_and_caps"]
        and delta_N1_to_5["unique_N5_d5_survivor_all_prescriptions_and_caps"]
        and (delta_N2_to_5["total_faithful_actions"] == 20)
        and (delta_N1_to_5["total_faithful_actions"] == 21)
        and spin10_all_ok
        and (f_xi_bg_at_0 == 0)
        and (f_xi_bg_litim_at_0 == 0)
        and f_lam_dD_formula_ok
        and f_lam_cures_wall
    )

    return {
        "g_star_closed_form": str(g_star_gen),
        "theta_g_closed_form": str(theta_g_gen),
        "theta_g_minus_2": str(theta_minus_2),
        "M_g_GSM_2H": str(M_g_SM),
        "pincer": pincer_results,
        "card_line58_prose_discrepancy": card_line58_prose_discrepancy,
        "delta_23N_N2_to_5": delta_N2_to_5,
        "delta_23N_N1_to_5": {
            "total_faithful_actions": delta_N1_to_5["total_faithful_actions"],
            "unique_N5_d5_survivor_all_prescriptions_and_caps": delta_N1_to_5["unique_N5_d5_survivor_all_prescriptions_and_caps"],
            "note": "Exact faithful transitive coset action counts for Delta(2,3,N): N=2(2), N=3(3), N=4(7), N=5(8) => 20 for N=2..5; including trivial N=1(1) gives 21 for N=1..5.",
        },
        "spin10_real10": spin10_checks,
        "a2_ow13_bridges": {
            "f_xi_bg_general": str(f_xi_bg_lam),
            "f_xi_bg_at_lam0": str(f_xi_bg_at_0),
            "f_xi_bg_litim_at_lam0": str(f_xi_bg_litim_at_0),
            "conformal_xi_1_6_protected": bool(f_xi_bg_at_0 == 0 and f_xi_bg_litim_at_0 == 0),
            "litim_threshold_integral": str(litim_thresh),
            "f_lam_dD_general": str(f_lam_dD),
            "f_lam_dD_at_etaN_m2_lam0": str(f_lam_dD_fp_lam0),
            "f_lam_dD_GSM_full": str(f_lam_gsm_full),
            "f_crit": str(f_crit),
            "f_lam_over_f_crit": str(f_lam_ratio),
            "cures_lam1_collision_wall": f_lam_cures_wall,
        },
        "passed": passed,
    }


# ---------------------------------------------------------------------------
# Task OW14-B.3: Kaloper-Padilla (arXiv:1309-6562) Global Vacuum Sequestering
# ---------------------------------------------------------------------------

def _replace_sigma_deriv(expr: sp.Expr, sigma_fn: sp.FunctionClass, sym: sp.Symbol) -> sp.Expr:
    return expr.replace(
        lambda ex: isinstance(ex, sp.Subs) and ex.expr.has(sigma_fn),
        lambda _ex: sym,
    )


def run_ow14_b3(V_Lstar_mp: mp.mpf) -> Dict[str, Any]:
    V4, Lam_bare, lam_s, mu, rho_vac = sp.symbols("V_4 Lam_bare lam_s mu rho_vac", positive=True)
    K_sym = sp.Symbol("K_sym", real=True)
    L0_fn = sp.Function("L_0")(lam_s)
    sigma_fn = sp.Function("sigma")

    # 1. Abstract matter Lagrangian L_0(lam_s) with dL_0/dlam_s = -(2/lam_s) * K_sym:
    z = Lam_bare / (lam_s**4 * mu**4)
    S_abs = V4 * (-Lam_bare + lam_s**4 * (L0_fn - rho_vac)) + sigma_fn(z)

    eq_Lam = sp.diff(S_abs, Lam_bare)
    eq_lams = sp.diff(S_abs, lam_s).subs(sp.diff(L0_fn, lam_s), -2 * K_sym / lam_s)

    sigma_p_sym = sp.Symbol("sigma_p", nonzero=True)
    eq_Lam_sub = sp.simplify(_replace_sigma_deriv(eq_Lam, sigma_fn, sigma_p_sym))
    eq_lams_sub = sp.simplify(_replace_sigma_deriv(eq_lams, sigma_fn, sigma_p_sym))

    sol_kp = sp.solve([sp.Eq(eq_Lam_sub, 0), sp.Eq(eq_lams_sub, 0)], [sigma_p_sym, Lam_bare], dict=True)[0]
    Lam_bare_sol = sp.simplify(sol_kp[Lam_bare])
    sigma_p_sol = sp.simplify(sol_kp[sigma_p_sym])

    T_phys_expr = lam_s**4 * (4 * (L0_fn - rho_vac) - 2 * K_sym)
    T_mat_expr = lam_s**4 * (4 * L0_fn - 2 * K_sym)
    Lam_res_expr = sp.simplify(Lam_bare_sol + lam_s**4 * rho_vac)
    dLam_res_drho = sp.simplify(sp.diff(Lam_res_expr, rho_vac))

    lam_bare_matches_Tphys = sp.simplify(Lam_bare_sol - sp.Rational(1, 4) * T_phys_expr) == 0
    lam_res_matches_Tmat = sp.simplify(Lam_res_expr - sp.Rational(1, 4) * T_mat_expr) == 0
    sequester_exact_zero = (dLam_res_drho == 0)

    # 2. Concrete dynamical scalar field test: L_0(lam_s) = -(1/2) lam_s^-2 X - U (no chain-rule substitution!)
    X_kin, U_pot = sp.symbols("X_kin U_pot", real=True)
    L0_scalar = -sp.Rational(1, 2) * lam_s**(-2) * X_kin - U_pot
    S_scalar = V4 * (-Lam_bare + lam_s**4 * (L0_scalar - rho_vac)) + sigma_fn(z)
    eq1_sc = sp.simplify(_replace_sigma_deriv(sp.diff(S_scalar, Lam_bare), sigma_fn, sigma_p_sym))
    eq2_sc = sp.simplify(_replace_sigma_deriv(sp.diff(S_scalar, lam_s), sigma_fn, sigma_p_sym))
    sol_sc = sp.solve([sp.Eq(eq1_sc, 0), sp.Eq(eq2_sc, 0)], [sigma_p_sym, Lam_bare], dict=True)[0]
    Lam_bare_sc = sp.simplify(sol_sc[Lam_bare])
    Lam_res_sc = sp.simplify(Lam_bare_sc + lam_s**4 * rho_vac)
    dLam_res_sc_drho = sp.simplify(sp.diff(Lam_res_sc, rho_vac))
    # Expected trace of scalar T_mat = lam_s^4 * (-lam_s^-2 X_kin - 4 U_pot):
    T_mat_sc_expected = lam_s**4 * (-lam_s**(-2) * X_kin - 4 * U_pot)
    scalar_matches = sp.simplify(Lam_res_sc - sp.Rational(1, 4) * T_mat_sc_expected) == 0

    # Explicit invariance of Lam_res under shifts of rho_vac by a_0=-64, 6D {-6,-2,-1}, and V(L_*):
    shift_vals = (
        sp.Integer(-64),
        sp.Integer(-6),
        sp.Integer(-2),
        sp.Integer(-1),
        sp.Rational(int(mp.floor(V_Lstar_mp * 10**12)), 10**12),
    )
    shift_invariance_ok = all(
        sp.simplify(Lam_res_expr.subs(rho_vac, rho_vac + dv) - Lam_res_expr) == 0
        for dv in shift_vals
    )

    passed = bool(
        lam_bare_matches_Tphys
        and lam_res_matches_Tmat
        and sequester_exact_zero
        and scalar_matches
        and (dLam_res_sc_drho == 0)
        and shift_invariance_ok
    )

    return {
        "sigma_prime_solution": str(sigma_p_sol),
        "Lam_bare_solution": str(Lam_bare_sol),
        "Lam_bare_equals_quarter_Tphys": lam_bare_matches_Tphys,
        "Lam_res_solution": str(Lam_res_expr),
        "Lam_res_equals_quarter_Tmat": lam_res_matches_Tmat,
        "d_Lam_res_d_rho_vac": str(dLam_res_drho),
        "concrete_scalar_Lam_res": str(Lam_res_sc),
        "concrete_scalar_matches_quarter_Tmat": scalar_matches,
        "concrete_scalar_d_Lam_res_d_rho_vac": str(dLam_res_sc_drho),
        "vacuum_shift_invariance_verified": shift_invariance_ok,
        "passed": passed,
    }


# ---------------------------------------------------------------------------
# Task OW14-C: 4 / 4 Planted Fault Controls (PF-OW14-1..4)
# ---------------------------------------------------------------------------

def run_ow14_c() -> Dict[str, Any]:
    # PF-OW14-1: Corrupt Einstein-frame a = -(3/2)*b to a = -b
    a_sym, b_sym = sp.symbols("a b", real=True, positive=True)
    # From ADM/Weyl general 7D formula: E = 2a + 3b, L_kin_coeff = -3a^2 - 9ab - 3b^2
    E_7d = 2 * a_sym + 3 * b_sym
    kin_coeff = -3 * a_sym**2 - 9 * a_sym * b_sym - 3 * b_sym**2
    E_corrupt = sp.simplify(E_7d.subs(a_sym, -b_sym))  # +b != 0
    kin_corrupt = sp.simplify(kin_coeff.subs(a_sym, -b_sym))  # +3 b^2
    b_corrupt = sp.solve(sp.Eq(kin_corrupt, sp.Rational(1, 2)), b_sym)[0]  # 1/sqrt(6)
    b_exact = sp.sqrt(sp.Rational(2, 15))
    pf1_detected = bool((E_corrupt != 0) and (sp.simplify(b_corrupt - b_exact) != 0))

    # PF-OW14-2: Flip AdS bulk sign -|c_3| -> +|c_3| (c_3 = +1) in V(L) -> 0 positive extrema via manual QQ Sturm
    poly_ads: PolyQQ = [
        Fraction(-10), Fraction(-9), Fraction(0), Fraction(0),
        Fraction(0), Fraction(-5), Fraction(0), Fraction(3),
    ]
    poly_flipped: PolyQQ = [
        Fraction(10), Fraction(9), Fraction(0), Fraction(0),
        Fraction(0), Fraction(5), Fraction(0), Fraction(3),
    ]
    sturm_ads_cnt = sturm_root_count_pos_inf(poly_ads)["positive_real_roots"]
    sturm_flip_cnt = sturm_root_count_pos_inf(poly_flipped)["positive_real_roots"]
    pf2_detected = bool((sturm_ads_cnt == 1) and (sturm_flip_cnt == 0))

    # PF-OW14-3: N_gen = 4 (M_g = 24) in unimodular FRG (cap = 23 and cap = 22) -> g_* < 0
    g_sym = sp.Symbol("g", real=True)
    M_g_4 = 16 * 4 - 40
    g_star_4_cap23 = [
        s for s in sp.solve(
            sp.Eq((2 + g_sym * (M_g_4 - 22) / (6 * sp.pi) / (1 - g_sym / (12 * sp.pi))) * g_sym, 0),
            g_sym,
        )
        if s != 0
    ][0]
    g_star_4_cap22 = [
        s for s in sp.solve(
            sp.Eq((2 + g_sym * (M_g_4 - 21) / (6 * sp.pi) / (1 - g_sym / (12 * sp.pi))) * g_sym, 0),
            g_sym,
        )
        if s != 0
    ][0]
    pf3_detected = bool(
        (M_g_4 == 24)
        and (sp.simplify(g_star_4_cap23 / sp.pi) < 0)
        and (sp.simplify(g_star_4_cap22 / sp.pi) < 0)
    )

    # PF-OW14-4: Omit lam_s^4 metric rescaling (fixed lam_s = 1, varying only Lam_bare; AND unscaled rho_vac)
    V4, Lam_bare, lam_s, mu, rho_vac, L0_c, K_c = sp.symbols(
        "V_4 Lam_bare lam_s mu rho_vac L_0 K_c", positive=True
    )
    # Version A: fixed lam_s = 1, explicit smooth sigma(z) = (1/2) z^2, vary only Lam_bare
    S_fault_fixed = V4 * (-Lam_bare + L0_c - rho_vac) + sp.Rational(1, 2) * (Lam_bare / mu**4) ** 2
    Lam_bare_fault_A = sp.solve(sp.Eq(sp.diff(S_fault_fixed, Lam_bare), 0), Lam_bare)[0]
    Lam_res_fault_A = sp.simplify(Lam_bare_fault_A + rho_vac)
    dLam_drho_A = sp.simplify(sp.diff(Lam_res_fault_A, rho_vac))

    # Version B: vary (Lam_bare, lam_s) with unscaled -rho_vac (no lam_s^4 factor on rho_vac)
    sigma_fn = sp.Function("sigma")
    z_f = Lam_bare / (lam_s**4 * mu**4)
    L0_f = sp.Function("L_0")(lam_s)
    S_fault_unscaled = V4 * (-Lam_bare + lam_s**4 * L0_f - rho_vac) + sigma_fn(z_f)
    sp_sym = sp.Symbol("sigma_p", nonzero=True)
    eq1_f = sp.simplify(_replace_sigma_deriv(sp.diff(S_fault_unscaled, Lam_bare), sigma_fn, sp_sym))
    eq2_f = sp.simplify(
        _replace_sigma_deriv(
            sp.diff(S_fault_unscaled, lam_s).subs(sp.diff(L0_f, lam_s), -2 * K_c / lam_s),
            sigma_fn,
            sp_sym,
        )
    )
    sol_fB = sp.solve([sp.Eq(eq1_f, 0), sp.Eq(eq2_f, 0)], [sp_sym, Lam_bare], dict=True)[0]
    Lam_res_fault_B = sp.simplify(sol_fB[Lam_bare] + rho_vac)
    dLam_drho_B = sp.simplify(sp.diff(Lam_res_fault_B, rho_vac))

    pf4_detected = bool(
        (dLam_drho_A == 1)
        and (dLam_drho_B == 1)
    )

    detected_count = sum(int(x) for x in (pf1_detected, pf2_detected, pf3_detected, pf4_detected))
    return {
        "PF-OW14-1": {
            "E_corrupt": str(E_corrupt),
            "L_kin_corrupt": str(kin_corrupt),
            "b_corrupt": str(b_corrupt),
            "b_exact": str(b_exact),
            "detected": pf1_detected,
        },
        "PF-OW14-2": {
            "ads_positive_roots": sturm_ads_cnt,
            "flipped_c3_plus1_positive_roots": sturm_flip_cnt,
            "detected": pf2_detected,
        },
        "PF-OW14-3": {
            "N_gen": 4,
            "M_g": M_g_4,
            "g_star_cap23": str(g_star_4_cap23),
            "g_star_cap22": str(g_star_4_cap22),
            "detected": pf3_detected,
        },
        "PF-OW14-4": {
            "fixed_lams_Lam_bare": str(Lam_bare_fault_A),
            "fixed_lams_dLam_res_drho": str(dLam_drho_A),
            "unscaled_rhovac_Lam_res": str(Lam_res_fault_B),
            "unscaled_rhovac_dLam_res_drho": str(dLam_drho_B),
            "detected": pf4_detected,
        },
        "planted_faults_detected": detected_count,
        "planted_faults_total": 4,
        "passed": bool(detected_count == 4),
    }


def main() -> None:
    empirical_inputs_list: List[str] = []
    ow14_a1 = run_ow14_a1()
    ow14_a2 = run_ow14_a2()
    ow14_a3 = run_ow14_a3()
    V_Lstar_mp = mp.mpf(ow14_a3["ads_benchmark_V_L_star_55dps"])
    ow14_b1 = run_ow14_b1(V_Lstar_mp)
    ow14_b2 = run_ow14_b2()
    ow14_b3 = run_ow14_b3(V_Lstar_mp)
    ow14_c = run_ow14_c()

    subtask_gates = {
        "OW14-A.1": ow14_a1["passed"],
        "OW14-A.2": ow14_a2["passed"],
        "OW14-A.3": ow14_a3["passed"],
        "OW14-B.1": ow14_b1["passed"],
        "OW14-B.2": ow14_b2["passed"],
        "OW14-B.3": ow14_b3["passed"],
        "OW14-C": ow14_c["passed"],
    }
    all_gates_passed = bool(all(subtask_gates.values()))

    results = {
        "card_id": "A2-OW14",
        "role": "independent_cold_room_zero_trust_referee",
        "empirical_inputs_used": len(empirical_inputs_list),
        "empirical_inputs_budget": 19,
        "mpmath_dps": MP_DPS,
        "subtask_gates": subtask_gates,
        "planted_faults_detected": f"{ow14_c['planted_faults_detected']}/{ow14_c['planted_faults_total']}",
        "all_gates_passed": all_gates_passed,
        "OW14-A.1": ow14_a1,
        "OW14-A.2": ow14_a2,
        "OW14-A.3": ow14_a3,
        "OW14-B.1": ow14_b1,
        "OW14-B.2": ow14_b2,
        "OW14-B.3": ow14_b3,
        "OW14-C": ow14_c,
    }

    out_path = Path(__file__).resolve().parent / "a2_ow14_referee_results.json"
    out_path.write_text(json.dumps(results, indent=2, sort_keys=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
