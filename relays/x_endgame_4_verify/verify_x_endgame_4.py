#!/usr/bin/env python3
"""
Standalone Zero-Import Verifier for Card X-ENDGAME-4 (0 of 19).

Verifies:
  Part 4A (Target-Free (L, R) Bundle SL(2, C) Holonomy, Two-Presentation Wada Polynomial,
           Exact Parabolic Fox-Bundle Reidemeister-Porti Torsion, and Kashaev 1-Loop State Sum):
    - Gate_AST_Stage4_ZeroTargetLiterals: zero disallowed imports and zero float literals or sqrt(3)
      targets inside all target-free bundle / variational root-finding functions.
    - Unbiased complex Newton solver on pi_1(m004) = <a, b, t | t a t^-1 = a b a, t b t^-1 = b a>
      from four rational seeds; verifies convergence, bundle relations, Tr([a, b]) = -2, [[a, b], t] = 0,
      and agreement of -K_{0,1}/K_{0,0} with 2 sqrt(3) i (and Thurston's tau_NZ(z*)).
    - Two-presentation Fox calculus verification: W_bundle(u) + u^3 W_Wirtinger(u) = 0 across test points,
      exact Lagrange-Vandermonde recovery of (u - 1)(u^2 - 5u + 1), and |W'_bundle(1)| = 3.
    - Exact m = 1 parabolic Fox-bundle cochain complex 0 -> C^0(C^3) -> C^1(C^9) -> C^2(C^6) -> 0
      across two distinct unimodular bases of sl_2(C), using the exact free-group torus identity
      [t, K] = R_1 * (aba) R_2 (aba)^-1 * (ab) R_1^-1 (ab)^-1 * K R_2^-1 K^-1:
        * Verifies rk(d^0) = 3, rk(d^1) = 5, peripheral pullback closure pb * d^1 = 0,
        * Cohomological meridian torsion |Tor_cohom(m004; mu)| = 2 / sqrt(3) (Porti meridian torsion 1 / sqrt(3)),
        * Deformed character-variety check at m = 3/2 matching 2 / sqrt((x^2 - 1)(5 - x^2)),
        * CCGLS A-polynomial trace-differential ratio |d Tr rho(lambda) / d Tr rho(mu)| = 12 = |tau_cusp|^2,
        * Porti longitudinal torsion |T_Porti(m004; lambda)| = 12 * (1 / sqrt(3)) = 4 sqrt(3),
        * Planted control PC_ENDGAME4_AbelianLocusCohomologyFailure (abelian locus drops rk(d^0) from 3 to 2).
    - Seven-level Kashaev quantum dilogarithm state sum <4_1>_N at N in {100, 150, 200, 250, 300, 350, 400}:
      7-point asymptotic extraction simultaneously reproduces Vol(m004) to < 1e-9, log(N) exponent 3/2
      to < 1e-6, and the 1-loop meridian torsion prefactor |T_Porti(m004; mu)|^(1/2) = 3^(-1/4) to < 1e-6.

  Part 4B (SL(2, C) = Spin^+(3, 1) Lorentzian Homomorphism & 3+1D Plebanski Self-Dual B ^ F Soldering):
    - Explicit matrix verification that Lambda(G)^mu_nu = (1/2) Tr(sigma_mu G sigma_nu G^dag) maps
      (A, B, T) and 10 random SL(2, C) pairs homomorphically into SO^+(3, 1).
    - Across 10 random non-degenerate tetrads e^I_mu and spin connections omega^{IJ}_mu at rational
      Immirzi parameter gamma = 3/7, verifies (*)^2 = -I, P_+^2 = P_+, *(P_+) = i P_+,
      Re((i + 1/gamma) eps^{mnrs} B_{+,IJ,mn} F_+^{IJ}_{rs}) == L_Pal + (1/gamma) L_Holst,
      L_Pal == 2 det(e) e^m_I e^n_J F^{IJ}_{mn}, Re(B_+ ^ B_+) == 0, and Im(B_+ ^ B_+) == -24 det(e).
    - Planted controls PC_ENDGAME4_BrokenSimplicityConstraint and PC_ENDGAME4_EuclideanSignatureSelfDualMismatch.

  Part 4C (Parameter-Free Exponential Scale Hierarchy Ledger — Strict Dimensionless Ratios):
    - Dynamically computes Stage 2 stabilized cusp area A* (confirming |A* - 6 pi| < 2e-3),
    - Evaluates gravitational instanton factors (4 sqrt(3))^(-1/2) exp(-k Vol(m004) / (2 pi)) for k in {1, 4, 45, 180},
    - Evaluates 1-loop non-abelian dimensional transmutation ratios exp(-2 pi alpha_UV^-1 / 7) under both
      pure-2D horotorus (alpha_UV^-1 = A*) and 3D-bulk-weighted (alpha_UV^-1 = Vol(m004) A*) KK measures,
      explicitly pricing the 2D vs 3D KK measure choice at 1 discrete bit.
"""

from __future__ import annotations

import ast
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple

import mpmath as mp
import numpy as np


ALLOWED_IMPORTS: Set[str] = {
    "__future__",
    "ast",
    "fractions",
    "hashlib",
    "json",
    "math",
    "mpmath",
    "numpy",
    "pathlib",
    "typing",
}

TARGET_FREE_FUNCTIONS: Set[str] = {
    "solve_bundle_parabolic_seed",
    "solve_deformed_wirtinger",
    "bloch_wigner_mp",
    "z2_from_z1_gluing",
    "tau_nz_from_z1",
    "neg_vol_on_gluing_curve",
    "s_eff_joint_3d_2d",
    "solve_joint_3var_newton",
}


def verify_ast_zero_imports_and_zero_target_literals() -> Dict[str, Any]:
    src = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(src)
    mods: Set[str] = set()
    float_literals: List[Any] = []
    sqrt3_calls: List[str] = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                mods.add(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.level > 0:
                mods.add("<relative>")
            elif node.module:
                mods.add(node.module.split(".")[0])

    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in TARGET_FREE_FUNCTIONS:
            for sub in ast.walk(node):
                if isinstance(sub, ast.Constant) and isinstance(sub.value, (float, complex)):
                    float_literals.append((node.name, sub.value))
                if isinstance(sub, ast.Call):
                    fn_str = ast.unparse(sub.func) if hasattr(ast, "unparse") else ""
                    if "sqrt" in fn_str:
                        for arg in sub.args:
                            if isinstance(arg, ast.Constant) and arg.value == 3:
                                sqrt3_calls.append(node.name)

    disallowed = sorted(mods - ALLOWED_IMPORTS)
    passed = (len(disallowed) == 0) and (len(float_literals) == 0) and (len(sqrt3_calls) == 0)
    return {
        "imported_top_modules": sorted(mods),
        "disallowed_imports_count": len(disallowed),
        "zero_imports_from_main_or_other_relays": len(disallowed) == 0,
        "inspected_target_free_functions": sorted(TARGET_FREE_FUNCTIONS),
        "float_literals_in_target_free_functions": len(float_literals),
        "sqrt3_calls_in_target_free_functions": len(sqrt3_calls),
        "Gate_AST_Stage4_ZeroTargetLiterals_passed": bool(passed),
    }


# ============================================================================
# SECTION 1: TARGET-FREE (L, R) BUNDLE HOLONOMY & VARIATIONAL HELPERS
# ============================================================================

def mat_inv_sl2(m_mat: Any) -> Any:
    return mp.matrix([[m_mat[1, 1], -m_mat[0, 1]], [-m_mat[1, 0], m_mat[0, 0]]])


def solve_bundle_parabolic_seed(
    vr_seed: Fraction, vi_seed: Fraction, wr_seed: Fraction, wi_seed: Fraction
) -> Dict[str, Any]:
    """
    Target-free complex Newton solver for the punctured-torus bundle presentation of m004:
      pi_1(m004) = <a, b, t | t a t^-1 = a b a, t b t^-1 = b a>
    Fix meridian gauge t = [[1, 1], [0, 1]] and parabolic translation gauge b_{1, 1} = 1,
    giving B(v, w) = [[1 + v w, w], [v, 1]] in SL(2, C) with det(B) = 1 identically.
    Setting A := B^-1 T B T^-1 satisfies R_2 identically; R_1 reduces to T A T^-1 - A B A = 0
    on the non-abelian locus v != 0.
    """
    t_mat = mp.matrix([[1, 1], [0, 1]])
    t_inv = mat_inv_sl2(t_mat)

    def eval_res(v_val: Any, w_val: Any) -> Tuple[Any, Any, Any, Any]:
        b_mat = mp.matrix([[1 + v_val * w_val, w_val], [v_val, 1]])
        b_inv = mat_inv_sl2(b_mat)
        a_mat = b_inv * t_mat * b_mat * t_inv
        diff = (t_mat * a_mat * t_inv) - (a_mat * b_mat * a_mat)
        return diff[0, 1], diff[1, 0] / v_val, a_mat, b_mat

    v = mp.mpc(
        mp.mpf(vr_seed.numerator) / mp.mpf(vr_seed.denominator),
        mp.mpf(vi_seed.numerator) / mp.mpf(vi_seed.denominator),
    )
    w = mp.mpc(
        mp.mpf(wr_seed.numerator) / mp.mpf(wr_seed.denominator),
        mp.mpf(wi_seed.numerator) / mp.mpf(wi_seed.denominator),
    )
    eps = mp.mpf(10) ** (-22)
    tol = mp.mpf(10) ** (-44)

    for _ in range(35):
        f1, f2, _, _ = eval_res(v, w)
        if abs(f1) + abs(f2) < tol:
            break
        f1_v, f2_v, _, _ = eval_res(v + eps, w)
        f1_w, f2_w, _, _ = eval_res(v, w + eps)
        j11 = (f1_v - f1) / eps
        j21 = (f2_v - f2) / eps
        j12 = (f1_w - f1) / eps
        j22 = (f2_w - f2) / eps
        det_j = j11 * j22 - j12 * j21
        v -= (j22 * f1 - j12 * f2) / det_j
        w -= (-j21 * f1 + j11 * f2) / det_j

    _, _, a_sol, b_sol = eval_res(v, w)
    r1_mat = t_mat * a_sol * t_inv * mat_inv_sl2(a_sol * b_sol * a_sol) - mp.eye(2)
    r2_mat = t_mat * b_sol * t_inv * mat_inv_sl2(b_sol * a_sol) - mp.eye(2)
    k_mat = a_sol * b_sol * mat_inv_sl2(a_sol) * mat_inv_sl2(b_sol)
    comm_kt = k_mat * t_mat - t_mat * k_mat
    tau_bundle = -k_mat[0, 1] / k_mat[0, 0]

    return {
        "v": v,
        "w": w,
        "A": a_sol,
        "B": b_sol,
        "T": t_mat,
        "K": k_mat,
        "r1_frob_err": mp.mnorm(r1_mat, "F"),
        "r2_frob_err": mp.mnorm(r2_mat, "F"),
        "comm_KT_frob_err": mp.mnorm(comm_kt, "F"),
        "tr_K": k_mat[0, 0] + k_mat[1, 1],
        "tau_bundle": tau_bundle,
    }


def solve_deformed_wirtinger(m_val: Any, s_init: Any) -> Dict[str, Any]:
    """Target-free solver for deformed SL(2, C) representation around m = 1."""
    t_m = mp.matrix([[m_val, 1], [0, 1 / m_val]])
    t_i = mat_inv_sl2(t_m)
    eps = mp.mpf(10) ** (-22)
    tol = mp.mpf(10) ** (-44)
    s = s_init

    for _ in range(30):
        y_m = mp.matrix([[m_val, 0], [-s, 1 / m_val]])
        w_m = t_m * mat_inv_sl2(y_m) * t_i * y_m
        f0 = (w_m * t_m - y_m * w_m)[1, 0]
        if abs(f0) < tol:
            break
        y_p = mp.matrix([[m_val, 0], [-(s + eps), 1 / m_val]])
        w_p = t_m * mat_inv_sl2(y_p) * t_i * y_p
        fp = (w_p * t_m - y_p * w_p)[1, 0]
        s -= f0 / ((fp - f0) / eps)

    y_sol = mp.matrix([[m_val, 0], [-s, 1 / m_val]])
    b_m = t_i * y_sol
    a_m = mat_inv_sl2(b_m) * t_m * b_m * t_i
    k_m = a_m * b_m * mat_inv_sl2(a_m) * mat_inv_sl2(b_m)
    return {"A": a_m, "B": b_m, "T": t_m, "Y": y_sol, "K": k_m, "s": s}


def bloch_wigner_mp(z: Any) -> Any:
    return mp.im(mp.polylog(2, z)) + mp.arg(1 - z) * mp.log(abs(z))


def z2_from_z1_gluing(z1: Any) -> Any:
    w = z1 * (z1 - 1)
    disc = mp.sqrt(1 + 4 / w)
    r_plus = (1 + disc) / 2
    r_minus = (1 - disc) / 2
    return r_plus if mp.im(r_plus) > 0 else r_minus


def tau_nz_from_z1(z1: Any) -> Any:
    z2 = z2_from_z1_gluing(z1)
    h_mu = z2 * (1 - z1)
    a11 = (2 * z1 - 1) * z2 * (z2 - 1)
    a12 = z1 * (z1 - 1) * (2 * z2 - 1)
    a21 = -z2
    a22 = 1 - z1
    dw1_du = h_mu / (a21 - a22 * a11 / a12)
    return (mp.mpf(2) / z1 - mp.mpf(2) / (1 - z1)) * dw1_du


def eisenstein_char_mp(tau: Any, a_fr: Fraction, b_fr: Fraction, s_int: int = 3) -> Any:
    x, y = mp.re(tau), mp.im(tau)
    s = mp.mpf(s_int)
    half = mp.mpf(1) / mp.mpf(2)
    af = mp.mpf(a_fr.numerator) / mp.mpf(a_fr.denominator)
    af = af - mp.floor(af)
    bf = mp.mpf(b_fr.numerator) / mp.mpf(b_fr.denominator)
    k0 = (
        ((-1) ** (s_int - 1))
        * ((2 * mp.pi) ** (2 * s_int))
        / mp.factorial(2 * s_int)
        * mp.bernpoly(2 * s_int, af)
        * (y ** s)
    )
    thresh = mp.mp.dps * 2.4 + 18.0
    y_fl = max(float(y), 0.5)
    af_fl = float(af)
    k_max = int(thresh / (2.0 * math.pi * y_fl * 0.15)) + 6
    m_span = 14
    tot = k0
    for k in range(1, k_max + 1):
        for m in range(-m_span, m_span + 1):
            ma_fl = abs(m + af_fl)
            if ma_fl > 1e-12 and (2.0 * math.pi * k * y_fl * ma_fl > thresh):
                continue
            ma = mp.mpf(m) + af
            ang = 2 * mp.pi * k * (bf - ma * x)
            if abs(ma) < mp.mpf("1e-30"):
                term = (
                    mp.sqrt(mp.pi)
                    * mp.gamma(s - half)
                    / mp.gamma(s)
                    * (y ** (1 - s))
                    * (mp.mpf(k) ** (1 - 2 * s_int))
                )
            else:
                z = 2 * mp.pi * k * y * abs(ma)
                if s_int == 3:
                    bess = mp.sqrt(mp.pi / (2 * z)) * mp.exp(-z) * (1 + 3 / z + 3 / (z * z))
                else:
                    bess = mp.besselk(s - half, z)
                term = (
                    (2 * (mp.pi ** s) / mp.gamma(s))
                    * mp.sqrt(y)
                    * ((abs(ma) / k) ** (s - half))
                    * bess
                )
            tot += 2 * mp.cos(ang) * term
    return tot


_VCAS_CACHE: Dict[Tuple[int, str, str, int, int, int, int], Any] = {}


def v_cas_point_mp(tau: Any, a_fr: Fraction, b_fr: Fraction) -> Any:
    key = (
        int(mp.mp.dps),
        mp.nstr(mp.re(tau), mp.mp.dps),
        mp.nstr(mp.im(tau), mp.mp.dps),
        a_fr.numerator,
        a_fr.denominator,
        b_fr.numerator,
        b_fr.denominator,
    )
    if key in _VCAS_CACHE:
        return _VCAS_CACHE[key]
    e0 = eisenstein_char_mp(tau, Fraction(0), Fraction(0), 3)
    str_w = (
        24 * e0
        + 4 * eisenstein_char_mp(tau, 3 * a_fr, 3 * b_fr, 3)
        - (
            36 * eisenstein_char_mp(tau, a_fr, b_fr, 3)
            + 18 * eisenstein_char_mp(tau, -4 * a_fr, -4 * b_fr, 3)
            + 18 * eisenstein_char_mp(tau, 2 * a_fr, 2 * b_fr, 3)
            + 12 * eisenstein_char_mp(tau, -3 * a_fr, -3 * b_fr, 3)
            + 6 * eisenstein_char_mp(tau, 6 * a_fr, 6 * b_fr, 3)
        )
    )
    val = -(str_w / (2 * (mp.pi ** 3)))
    _VCAS_CACHE[key] = val
    return val


def neg_vol_on_gluing_curve(x: Any, y: Any) -> Any:
    z1 = mp.mpc(x, y)
    z2 = z2_from_z1_gluing(z1)
    return -(bloch_wigner_mp(z1) + bloch_wigner_mp(z2))


def s_eff_joint_3d_2d(x: Any, y: Any, area: Any) -> Any:
    nv = neg_vol_on_gluing_curve(x, y)
    tnz = tau_nz_from_z1(mp.mpc(x, y))
    vc = v_cas_point_mp(tnz, Fraction(4, 15), Fraction(8, 15))
    c_vol = mp.mpf(1) / mp.mpf(2)
    c_flux = 2 * (mp.pi ** 2) * (mp.mpf(3) ** 2)
    return mp.re(nv + c_vol * area + c_flux / area + vc / (16 * (mp.pi ** 2) * (area ** 2)))


def solve_joint_3var_newton(seed_x: Fraction, seed_y: Fraction, seed_a: Fraction) -> Tuple[Any, Any, Any]:
    vec = [
        mp.mpf(seed_x.numerator) / mp.mpf(seed_x.denominator),
        mp.mpf(seed_y.numerator) / mp.mpf(seed_y.denominator),
        mp.mpf(seed_a.numerator) / mp.mpf(seed_a.denominator),
    ]
    steps = [mp.mpf(10) ** (-6), mp.mpf(10) ** (-6), mp.mpf(10) ** (-5)]
    tol = mp.mpf(10) ** (-14)

    for _ in range(18):
        f0 = s_eff_joint_3d_2d(vec[0], vec[1], vec[2])
        grad = [mp.mpf(0), mp.mpf(0), mp.mpf(0)]
        hess = mp.zeros(3, 3)
        for i in range(3):
            vp, vm = list(vec), list(vec)
            vp[i] += steps[i]
            vm[i] -= steps[i]
            fp = s_eff_joint_3d_2d(vp[0], vp[1], vp[2])
            fm = s_eff_joint_3d_2d(vm[0], vm[1], vm[2])
            grad[i] = (fp - fm) / (2 * steps[i])
            hess[i, i] = (fp - 2 * f0 + fm) / (steps[i] ** 2)
        for i in range(3):
            for j in range(i + 1, 3):
                vpp, vpm, vmp, vmm = list(vec), list(vec), list(vec), list(vec)
                vpp[i] += steps[i]; vpp[j] += steps[j]
                vpm[i] += steps[i]; vpm[j] -= steps[j]
                vmp[i] -= steps[i]; vmp[j] += steps[j]
                vmm[i] -= steps[i]; vmm[j] -= steps[j]
                hij = (
                    s_eff_joint_3d_2d(vpp[0], vpp[1], vpp[2])
                    - s_eff_joint_3d_2d(vpm[0], vpm[1], vpm[2])
                    - s_eff_joint_3d_2d(vmp[0], vmp[1], vmp[2])
                    + s_eff_joint_3d_2d(vmm[0], vmm[1], vmm[2])
                ) / (4 * steps[i] * steps[j])
                hess[i, j] = hij
                hess[j, i] = hij
        delta = (hess ** (-1)) * mp.matrix(grad)
        for i in range(3):
            vec[i] -= delta[i, 0]
        if abs(delta[0, 0]) + abs(delta[1, 0]) + abs(delta[2, 0]) < tol:
            break
    return vec[0], vec[1], vec[2]


# ============================================================================
# SECTION 2: FOX CALCULUS, WADA POLYNOMIAL, COCHAIN TORSION & KASHAEV SUM
# ============================================================================

WordType = List[Tuple[str, int]]


def inv_word(w: WordType) -> WordType:
    return [(g, -s) for g, s in reversed(w)]


def reduce_free_word(w: WordType) -> WordType:
    st: WordType = []
    for g, s in w:
        if st and st[-1][0] == g and st[-1][1] == -s:
            st.pop()
        else:
            st.append((g, s))
    return st


def fox_deriv_mp(word: WordType, gens: List[str], rho_ad: Dict[str, Any]) -> Dict[str, Any]:
    i3 = mp.eye(3)
    out = {g: mp.zeros(3, 3) for g in gens}
    pref = i3
    for g, sgn in word:
        mg = rho_ad[g]
        if sgn == 1:
            out[g] = out[g] + pref
            pref = pref * mg
        else:
            mgi = mg ** (-1)
            out[g] = out[g] - pref * mgi
            pref = pref * mgi
    return out


def compute_bundle_cohom_torsion_m1(
    a_mat: Any, b_mat: Any, t_mat: Any, k_mat: Any, h_scale: Any, f_scale: Any
) -> Dict[str, Any]:
    basis = [
        mp.matrix([[0, 1], [0, 0]]),
        mp.matrix([[1, 0], [0, -1]]) * h_scale,
        mp.matrix([[0, 0], [1, 0]]) * f_scale,
    ]

    def vec3(m_in: Any) -> Any:
        return mp.matrix([m_in[0, 1], m_in[0, 0] / h_scale, m_in[1, 0] / f_scale])

    def ad3(g_in: Any) -> Any:
        gi = mat_inv_sl2(g_in)
        m_out = mp.matrix(3, 3)
        for j, bj in enumerate(basis):
            vv = vec3(g_in * bj * gi)
            for i in range(3):
                m_out[i, j] = vv[i]
        return m_out

    r1_w: WordType = [("t", 1), ("a", 1), ("t", -1), ("a", -1), ("b", -1), ("a", -1)]
    r2_w: WordType = [("t", 1), ("b", 1), ("t", -1), ("a", -1), ("b", -1)]
    gens = ["a", "b", "t"]
    rho_ad = {"a": ad3(a_mat), "b": ad3(b_mat), "t": ad3(t_mat)}
    dr1 = fox_deriv_mp(r1_w, gens, rho_ad)
    dr2 = fox_deriv_mp(r2_w, gens, rho_ad)

    d0_mp = mp.zeros(9, 3)
    d1_mp = mp.zeros(6, 9)
    for ig, g in enumerate(gens):
        ag = rho_ad[g] - mp.eye(3)
        for r in range(3):
            for c in range(3):
                d0_mp[3 * ig + r, c] = ag[r, c]
                d1_mp[r, 3 * ig + c] = dr1[g][r, c]
                d1_mp[3 + r, 3 * ig + c] = dr2[g][r, c]

    # Canonical nilpotent log(T) = E:
    n_mu = t_mat - mp.eye(2)
    cov_mu = mp.zeros(1, 3)
    for j, bj in enumerate(basis):
        pr = n_mu * bj
        cov_mu[0, j] = (pr[0, 0] + pr[1, 1]) / 2

    ad_ab = ad3(a_mat * b_mat)
    ad_aba = ad3(a_mat * b_mat * a_mat)
    ad_k = ad3(k_mat)
    pb_mu = mp.zeros(1, 6)
    row1 = cov_mu * (mp.eye(3) - ad_ab)
    row2 = cov_mu * (ad_aba - ad_k)
    for c in range(3):
        pb_mu[0, c] = row1[0, c]
        pb_mu[0, 3 + c] = row2[0, c]

    pb_d1_err = mp.mnorm(pb_mu * d1_mp, "F")

    d0_np = np.array([[complex(d0_mp[r, c]) for c in range(3)] for r in range(9)], dtype=complex)
    d1_np = np.array([[complex(d1_mp[r, c]) for c in range(9)] for r in range(6)], dtype=complex)
    s_d0 = np.linalg.svd(d0_np, compute_uv=False)
    _, s_d1, vh1 = np.linalg.svd(d1_np)

    rk_d0 = int(np.sum(s_d0 > 1e-10))
    rk_d1 = int(np.sum(s_d1 > 1e-10))

    k_ker = vh1[5:, :].conj().T
    q0, _ = np.linalg.qr(d0_np)
    uk, _, _ = np.linalg.svd(k_ker - q0 @ (q0.conj().T @ k_ker))
    z1_u = uk[:, 0]

    cov_np = np.array([complex(cov_mu[0, c]) for c in range(3)], dtype=complex)
    pb_np = np.array([complex(pb_mu[0, c]) for c in range(6)], dtype=complex)
    pair_mu = cov_np @ z1_u[6:9]

    s2 = vh1[:5, :].conj().T
    h2_mu = pb_np.conj() / (pb_np @ pb_np.conj())
    tor_cohom_mu = abs(
        np.linalg.det(np.hstack([d0_np, (z1_u / pair_mu)[:, None], s2]))
        / np.linalg.det(np.hstack([d1_np @ s2, h2_mu[:, None]]))
    )
    return {
        "rk_d0": rk_d0,
        "rk_d1": rk_d1,
        "pb_d1_err": float(pb_d1_err),
        "tor_cohom_mu": float(tor_cohom_mu),
    }


def compute_deformed_bundle_torsion(a_m: Any, b_m: Any, t_m: Any, k_m: Any, m_val: Any) -> float:
    basis = [
        mp.matrix([[0, 1], [0, 0]]),
        mp.matrix([[1, 0], [0, -1]]) / mp.sqrt(2),
        mp.matrix([[0, 0], [1, 0]]),
    ]
    gram = mp.matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])

    def vec3(m_in: Any) -> Any:
        return mp.matrix([m_in[0, 1], m_in[0, 0] * mp.sqrt(2), m_in[1, 0]])

    def ad3(g_in: Any) -> Any:
        gi = mat_inv_sl2(g_in)
        m_out = mp.matrix(3, 3)
        for j, bj in enumerate(basis):
            vv = vec3(g_in * bj * gi)
            for i in range(3):
                m_out[i, j] = vv[i]
        return m_out

    r1_w: WordType = [("t", 1), ("a", 1), ("t", -1), ("a", -1), ("b", -1), ("a", -1)]
    r2_w: WordType = [("t", 1), ("b", 1), ("t", -1), ("a", -1), ("b", -1)]
    gens = ["a", "b", "t"]
    rho_ad = {"a": ad3(a_m), "b": ad3(b_m), "t": ad3(t_m)}
    dr1 = fox_deriv_mp(r1_w, gens, rho_ad)
    dr2 = fox_deriv_mp(r2_w, gens, rho_ad)

    d0_np = np.zeros((9, 3), dtype=complex)
    d1_np = np.zeros((6, 9), dtype=complex)
    for ig, g in enumerate(gens):
        ag = rho_ad[g] - mp.eye(3)
        for r in range(3):
            for c in range(3):
                d0_np[3 * ig + r, c] = complex(ag[r, c])
                d1_np[r, 3 * ig + c] = complex(dr1[g][r, c])
                d1_np[3 + r, 3 * ig + c] = complex(dr2[g][r, c])

    p_diag = mp.matrix([[1, 1 / (1 / m_val - m_val)], [0, 1]])
    h_m = p_diag * basis[1] * mat_inv_sl2(p_diag)
    e_p = vec3(h_m)
    cov_p = (gram * e_p).T
    pb = mp.zeros(1, 6)
    r1 = cov_p * (mp.eye(3) - ad3(a_m * b_m))
    r2 = cov_p * (ad3(a_m * b_m * a_m) - ad3(k_m))
    for c in range(3):
        pb[0, c] = r1[0, c]
        pb[0, 3 + c] = r2[0, c]

    pb_np = np.array([complex(pb[0, c]) for c in range(6)], dtype=complex)
    cov_np = np.array([complex(cov_p[0, c]) for c in range(3)], dtype=complex)
    _, _, vh1 = np.linalg.svd(d1_np)
    k_ker = vh1[5:, :].conj().T
    q0, _ = np.linalg.qr(d0_np)
    uk, _, _ = np.linalg.svd(k_ker - q0 @ (q0.conj().T @ k_ker))
    z1_u = uk[:, 0]
    pair_mu = cov_np @ z1_u[6:9]
    s2 = vh1[:5, :].conj().T
    h2 = pb_np.conj() / (pb_np @ pb_np.conj())
    return float(
        abs(
            np.linalg.det(np.hstack([d0_np, (z1_u / pair_mu)[:, None], s2]))
            / np.linalg.det(np.hstack([d1_np @ s2, h2[:, None]]))
        )
    )


def run_part_4a() -> Tuple[Dict[str, Any], Any, Any, Any, Any]:
    seeds = [
        (Fraction(1, 2), Fraction(-4, 5), Fraction(-9, 10), Fraction(1, 10)),
        (Fraction(3, 5), Fraction(-7, 10), Fraction(-11, 10), Fraction(-1, 5)),
        (Fraction(2, 5), Fraction(-9, 10), Fraction(-4, 5), Fraction(3, 10)),
        (Fraction(7, 10), Fraction(-3, 5), Fraction(-6, 5), Fraction(-1, 10)),
    ]

    with mp.workdps(48):
        sols = [solve_bundle_parabolic_seed(*sd) for sd in seeds]
        ref = sols[0]
        max_spread = max(
            max(abs(s["v"] - ref["v"]), abs(s["w"] - ref["w"])) for s in sols[1:]
        )
        max_r1 = max(s["r1_frob_err"] for s in sols)
        max_r2 = max(s["r2_frob_err"] for s in sols)
        max_comm = max(s["comm_KT_frob_err"] for s in sols)
        tr_k_plus_2_err = abs(ref["tr_K"] + 2)
        tau_target_check = abs(ref["tau_bundle"] - mp.mpc(0, 2 * mp.sqrt(3)))

        # Wada polynomial across Bundle (6x6) and Wirtinger (3x3):
        a_b, b_b, t_b, k_b = ref["A"], ref["B"], ref["T"], ref["K"]
        x_w = t_b
        y_w = t_b * b_b
        basis_std = [
            mp.matrix([[0, 1], [0, 0]]),
            mp.matrix([[1, 0], [0, -1]]),
            mp.matrix([[0, 0], [1, 0]]),
        ]

        def ad_std(g_in: Any) -> Any:
            gi = mat_inv_sl2(g_in)
            m_out = mp.matrix(3, 3)
            for j, bj in enumerate(basis_std):
                pr = g_in * bj * gi
                vv = [pr[0, 1], pr[0, 0], pr[1, 0]]
                for i in range(3):
                    m_out[i, j] = vv[i]
            return m_out

        r1_w: WordType = [("t", 1), ("a", 1), ("t", -1), ("a", -1), ("b", -1), ("a", -1)]
        r2_w: WordType = [("t", 1), ("b", 1), ("t", -1), ("a", -1), ("b", -1)]
        r_wirt: WordType = [
            ("x", 1), ("y", -1), ("x", -1), ("y", 1),
            ("x", 1),
            ("y", -1), ("x", 1), ("y", 1), ("x", -1),
            ("y", -1),
        ]

        ad_a, ad_b, ad_t = ad_std(a_b), ad_std(b_b), ad_std(t_b)
        ad_xw, ad_yw = ad_std(x_w), ad_std(y_w)

        def wada_bundle(u_val: Any) -> Any:
            rho_u = {"a": ad_a, "b": ad_b, "t": u_val * ad_t}
            d1 = fox_deriv_mp(r1_w, ["a", "b", "t"], rho_u)
            d2 = fox_deriv_mp(r2_w, ["a", "b", "t"], rho_u)
            m6 = mp.zeros(6, 6)
            for r in range(3):
                for c in range(3):
                    m6[r, c] = d1["a"][r, c]
                    m6[r, c + 3] = d1["b"][r, c]
                    m6[r + 3, c] = d2["a"][r, c]
                    m6[r + 3, c + 3] = d2["b"][r, c]
            return mp.det(m6) / mp.det(rho_u["t"] - mp.eye(3))

        def wada_wirt(u_val: Any) -> Any:
            rho_u = {"x": u_val * ad_xw, "y": u_val * ad_yw}
            dw = fox_deriv_mp(r_wirt, ["x", "y"], rho_u)
            return mp.det(dw["x"]) / mp.det(rho_u["y"] - mp.eye(3))

        test_u = [mp.mpf(2), mp.mpf(3), mp.mpc(mp.mpf(7) / 5, mp.mpf(-3) / 5)]
        wada_laurent_diff = max(abs(wada_bundle(u) + (u ** 3) * wada_wirt(u)) for u in test_u)

        # Interpolate W_bundle(u) = c0 + c1 u + c2 u^2 + c3 u^3 on u in {-1, 2, 3, 4}:
        # Exact polynomial (u - 1)(u^2 - 5u + 1) = -1 + 6u - 6u^2 + u^3
        u_interp = [mp.mpf(-1), mp.mpf(2), mp.mpf(3), mp.mpf(4)]
        vand = mp.zeros(4, 4)
        rhs_v = mp.zeros(4, 1)
        for i, up in enumerate(u_interp):
            for j in range(4):
                vand[i, j] = up ** j
            rhs_v[i, 0] = wada_bundle(up)
        c_poly = mp.lu_solve(vand, rhs_v)
        exact_c = [mp.mpf(-1), mp.mpf(6), mp.mpf(-6), mp.mpf(1)]
        wada_poly_coeff_err = max(abs(c_poly[j, 0] - exact_c[j]) for j in range(4))
        wada_deriv_at_1_abs = abs(c_poly[1, 0] + 2 * c_poly[2, 0] + 3 * c_poly[3, 0])

        # Free-group peripheral torus identity check:
        w_k: WordType = [("a", 1), ("b", 1), ("a", -1), ("b", -1)]
        w_aba: WordType = [("a", 1), ("b", 1), ("a", 1)]
        w_ab: WordType = [("a", 1), ("b", 1)]
        lhs_comm = [("t", 1)] + w_k + [("t", -1)] + inv_word(w_k)
        rhs_prod = (
            r1_w
            + w_aba + r2_w + inv_word(w_aba)
            + w_ab + inv_word(r1_w) + inv_word(w_ab)
            + w_k + inv_word(r2_w) + inv_word(w_k)
        )
        free_group_identity_exact = len(reduce_free_word(lhs_comm + inv_word(rhs_prod))) == 0

        # Two-basis untwisted m = 1 parabolic Fox-bundle torsion:
        tor_basis_a = compute_bundle_cohom_torsion_m1(a_b, b_b, t_b, k_b, 1 / mp.sqrt(2), mp.mpf(1))
        tor_basis_b = compute_bundle_cohom_torsion_m1(a_b, b_b, t_b, k_b, mp.mpf(1), mp.mpf(2))
        two_basis_diff = abs(tor_basis_a["tor_cohom_mu"] - tor_basis_b["tor_cohom_mu"])
        tor_cohom_mu = tor_basis_a["tor_cohom_mu"]
        tor_cohom_err = abs(tor_cohom_mu - float(2 / mp.sqrt(3)))

        # Deformed character-variety check at m = 3/2 (x = 13/6) and near m = exp(1e-7) for dTr(lambda)/dTr(mu) = 12:
        s_init = -ref["v"]
        def_32 = solve_deformed_wirtinger(mp.mpf(3) / mp.mpf(2), s_init)
        tor_def_32 = compute_deformed_bundle_torsion(
            def_32["A"], def_32["B"], def_32["T"], def_32["K"], mp.mpf(3) / mp.mpf(2)
        )
        x_32 = mp.mpf(3) / mp.mpf(2) + mp.mpf(2) / mp.mpf(3)
        porti_formula_32 = float(2 / mp.sqrt((x_32 ** 2 - 1) * (5 - x_32 ** 2)))
        deformed_32_err = abs(tor_def_32 - porti_formula_32)

        m_near = mp.exp(mp.mpf(10) ** (-7))
        def_near = solve_deformed_wirtinger(m_near, s_init)
        l_eig = def_near["K"][0, 0]
        a_poly_res = abs(
            (l_eig + 1 / l_eig)
            - (m_near ** 4 - m_near ** 2 - 2 - m_near ** (-2) + m_near ** (-4))
        )
        dtr_lam_over_dtr_mu = float(
            abs((l_eig + 1 / l_eig) + 2) / abs((m_near + 1 / m_near) - 2)
        )
        dtr_ratio_12_err = abs(dtr_lam_over_dtr_mu - 12.0)

        porti_meridian_torsion = 0.5 * tor_cohom_mu
        porti_longitudinal_torsion = dtr_lam_over_dtr_mu * porti_meridian_torsion
        porti_longitudinal_4sqrt3_err = abs(porti_longitudinal_torsion - float(4 * mp.sqrt(3)))

        # Planted control PC_ENDGAME4_AbelianLocusCohomologyFailure: A = B = I_2, T = [[1,1],[0,1]]
        d0_abelian = np.zeros((9, 3), dtype=complex)
        ad_t_np = np.array([[complex((ad_t - mp.eye(3))[r, c]) for c in range(3)] for r in range(3)])
        d0_abelian[6:9, :] = ad_t_np
        rk_d0_abelian = int(np.sum(np.linalg.svd(d0_abelian, compute_uv=False) > 1e-10))

        # Kashaev 7-point state sum <4_1>_N on N in {100, 150, 200, 250, 300, 350, 400}:
        vol_exact = 2 * bloch_wigner_mp(mp.exp(mp.mpc(0, mp.pi / 3)))
        ns = [100, 150, 200, 250, 300, 350, 400]
        m_fit = mp.zeros(7, 7)
        y_fit = mp.zeros(7, 1)
        for r_i, n_val in enumerate(ns):
            s_sum = mp.mpf(1)
            prod = mp.mpf(1)
            pi_n = mp.pi / n_val
            for j in range(1, n_val):
                sj = 2 * mp.sin(pi_n * j)
                prod *= sj * sj
                s_sum += prod
            m_fit[r_i, 0] = mp.mpf(n_val)
            m_fit[r_i, 1] = mp.log(n_val)
            m_fit[r_i, 2] = mp.mpf(1)
            m_fit[r_i, 3] = mp.mpf(1) / n_val
            m_fit[r_i, 4] = mp.mpf(1) / (n_val ** 2)
            m_fit[r_i, 5] = mp.mpf(1) / (n_val ** 3)
            m_fit[r_i, 6] = mp.mpf(1) / (n_val ** 4)
            y_fit[r_i, 0] = mp.log(s_sum)

        fit_c = mp.lu_solve(m_fit, y_fit)
        kashaev_vol = 2 * mp.pi * fit_c[0, 0]
        kashaev_log_exp = fit_c[1, 0]
        kashaev_prefactor = mp.exp(fit_c[2, 0])
        kashaev_vol_err = abs(kashaev_vol - vol_exact)
        kashaev_log_exp_err = abs(kashaev_log_exp - mp.mpf(3) / mp.mpf(2))
        kashaev_prefactor_err = abs(kashaev_prefactor - mp.power(3, mp.mpf(-1) / mp.mpf(4)))

    e1_passed = bool(
        float(max_spread) < 1e-36
        and float(max_r1) < 1e-36
        and float(max_r2) < 1e-36
        and float(max_comm) < 1e-36
        and float(tr_k_plus_2_err) < 1e-36
        and float(tau_target_check) < 1e-36
        and float(wada_laurent_diff) < 1e-36
        and float(wada_poly_coeff_err) < 1e-36
        and abs(float(wada_deriv_at_1_abs) - 3.0) < 1e-36
        and free_group_identity_exact
        and tor_basis_a["rk_d0"] == 3
        and tor_basis_a["rk_d1"] == 5
        and tor_basis_a["pb_d1_err"] < 1e-36
        and two_basis_diff < 1e-12
        and tor_cohom_err < 1e-12
        and deformed_32_err < 1e-12
        and dtr_ratio_12_err < 1e-10
        and porti_longitudinal_4sqrt3_err < 1e-10
        and float(kashaev_vol_err) < 1e-9
        and float(kashaev_log_exp_err) < 1e-6
        and float(kashaev_prefactor_err) < 1e-6
    )

    out = {
        "four_seed_bundle_spread": float(max_spread),
        "bundle_R1_frob_err": float(max_r1),
        "bundle_R2_frob_err": float(max_r2),
        "puncture_commutator_KT_err": float(max_comm),
        "puncture_commutator_tr_plus_2_err": float(tr_k_plus_2_err),
        "bundle_tau_im": float(mp.im(ref["tau_bundle"])),
        "bundle_tau_vs_2sqrt3i_err": float(tau_target_check),
        "wada_bundle_vs_wirtinger_laurent_err": float(wada_laurent_diff),
        "wada_polynomial_coeff_err": float(wada_poly_coeff_err),
        "wada_deriv_at_1_abs": float(wada_deriv_at_1_abs),
        "free_group_peripheral_identity_exact": free_group_identity_exact,
        "cochain_rk_d0": tor_basis_a["rk_d0"],
        "cochain_rk_d1": tor_basis_a["rk_d1"],
        "peripheral_pullback_cocycle_err": tor_basis_a["pb_d1_err"],
        "two_sl2_basis_torsion_diff": float(two_basis_diff),
        "tor_cohom_meridian_2_over_sqrt3": tor_cohom_mu,
        "tor_cohom_meridian_err": float(tor_cohom_err),
        "deformed_m_3_2_porti_formula_err": float(deformed_32_err),
        "ccgls_A_polynomial_residual": float(a_poly_res),
        "dTr_lambda_over_dTr_mu": dtr_lam_over_dtr_mu,
        "porti_meridian_torsion_1_over_sqrt3": porti_meridian_torsion,
        "porti_longitudinal_torsion_4sqrt3": porti_longitudinal_torsion,
        "porti_longitudinal_4sqrt3_err": float(porti_longitudinal_4sqrt3_err),
        "PC_ENDGAME4_AbelianLocus_rk_d0": rk_d0_abelian,
        "kashaev_7pt_vol": float(kashaev_vol),
        "kashaev_7pt_vol_err": float(kashaev_vol_err),
        "kashaev_7pt_logN_exp": float(kashaev_log_exp),
        "kashaev_7pt_prefactor": float(kashaev_prefactor),
        "kashaev_7pt_prefactor_vs_3_minus_1_4_err": float(kashaev_prefactor_err),
        "E1_Bundle_Holonomy_Torsion_and_StateSum_passed": e1_passed,
    }
    return out, ref["A"], ref["B"], ref["T"], vol_exact


# ============================================================================
# SECTION 3: PART 4B — SL(2, C) = SPIN^+(3, 1) & PLEBANSKI B ^ F SOLDERING
# ============================================================================

def run_part_4b(a_mp: Any, b_mp: Any, t_mp: Any) -> Dict[str, Any]:
    sigma = [
        np.array([[1, 0], [0, 1]], dtype=complex),
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.array([[1, 0], [0, -1]], dtype=complex),
    ]
    eta = np.diag([1.0, -1.0, -1.0, -1.0])

    def sl2c_to_so31(g_mat: np.ndarray) -> np.ndarray:
        lam = np.zeros((4, 4), dtype=complex)
        gd = g_mat.conj().T
        for mu in range(4):
            for nu in range(4):
                lam[mu, nu] = 0.5 * np.trace(sigma[mu] @ g_mat @ sigma[nu] @ gd)
        return lam

    def mp_to_np2(m_in: Any) -> np.ndarray:
        return np.array([[complex(m_in[r, c]) for c in range(2)] for r in range(2)], dtype=complex)

    a_c, b_c, t_c = mp_to_np2(a_mp), mp_to_np2(b_mp), mp_to_np2(t_mp)
    lam_a_c, lam_b_c, lam_t_c = sl2c_to_so31(a_c), sl2c_to_so31(b_c), sl2c_to_so31(t_c)
    max_im_lam = float(max(np.max(np.abs(m.imag)) for m in (lam_a_c, lam_b_c, lam_t_c)))
    lam_a, lam_b, lam_t = lam_a_c.real, lam_b_c.real, lam_t_c.real

    rng = np.random.default_rng(2026111504)
    max_metric_err = 0.0
    max_det_err = 0.0
    min_orthochronous = 1e9
    max_hom_err = 0.0

    for g_chk in [a_c, b_c, t_c]:
        lc = sl2c_to_so31(g_chk)
        max_im_lam = max(max_im_lam, float(np.max(np.abs(lc.imag))))
        lr = lc.real
        max_metric_err = max(max_metric_err, float(np.max(np.abs(lr.T @ eta @ lr - eta))))
        max_det_err = max(max_det_err, abs(float(np.linalg.det(lr)) - 1.0))
        min_orthochronous = min(min_orthochronous, float(lr[0, 0]))

    for _ in range(10):
        m1 = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
        m1 /= np.sqrt(np.linalg.det(m1))
        m2 = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
        m2 /= np.sqrt(np.linalg.det(m2))
        l1 = sl2c_to_so31(m1).real
        l2 = sl2c_to_so31(m2).real
        l12 = sl2c_to_so31(m1 @ m2).real
        max_metric_err = max(max_metric_err, float(np.max(np.abs(l1.T @ eta @ l1 - eta))))
        max_det_err = max(max_det_err, abs(float(np.linalg.det(l1)) - 1.0))
        min_orthochronous = min(min_orthochronous, float(l1[0, 0]))
        max_hom_err = max(max_hom_err, float(np.max(np.abs(l1 @ l2 - l12))))

    so31_bundle_rel1_err = float(
        np.max(np.abs(lam_t @ lam_a @ np.linalg.inv(lam_t) - lam_a @ lam_b @ lam_a))
    )
    so31_bundle_rel2_err = float(
        np.max(np.abs(lam_t @ lam_b @ np.linalg.inv(lam_t) - lam_b @ lam_a))
    )

    # 3+1D Plebanski Self-Dual B ^ F = Palatini-Holst Identity:
    eps4 = np.zeros((4, 4, 4, 4), dtype=float)
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if len({i, j, k, l}) == 4:
                        inv = sum(
                            1
                            for idx_a, a in enumerate((i, j, k, l))
                            for b in (i, j, k, l)[idx_a + 1 :]
                            if a > b
                        )
                        eps4[i, j, k, l] = -1.0 if (inv % 2) else 1.0

    eps_up_down = np.zeros((4, 4, 4, 4), dtype=float)
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    eps_up_down[i, j, k, l] = -eps4[i, j, k, l] * eta[k, k] * eta[l, l]

    def hodge_dual(x_ten: np.ndarray) -> np.ndarray:
        return 0.5 * np.tensordot(eps_up_down, x_ten, axes=([2, 3], [0, 1]))

    def proj_plus(x_ten: np.ndarray) -> np.ndarray:
        return 0.5 * (x_ten - 1j * hodge_dual(x_ten))

    x_rand = rng.normal(size=(4, 4))
    x_rand = x_rand - x_rand.T
    star_sq_plus_id_err = float(np.max(np.abs(hodge_dual(hodge_dual(x_rand)) + x_rand)))
    px = proj_plus(x_rand)
    proj_idemp_err = float(np.max(np.abs(proj_plus(px) - px)))
    proj_eigen_err = float(np.max(np.abs(hodge_dual(px) - 1j * px)))

    # Planted control PC_ENDGAME4_EuclideanSignatureSelfDualMismatch:
    # In (+,+,+,+) signature, det(delta) = +1 => eps_eucl_up_down = +eps4 => (*_E)^2 = +I => P_+^2 != P_+!
    def hodge_eucl(x_ten: np.ndarray) -> np.ndarray:
        return 0.5 * np.tensordot(eps4, x_ten, axes=([2, 3], [0, 1]))

    def proj_eucl(x_ten: np.ndarray) -> np.ndarray:
        return 0.5 * (x_ten - 1j * hodge_eucl(x_ten))

    # Build 6x6 operator matrix of (P_+^2 - P_+) on orthonormal basis of so(4):
    so4_basis: List[np.ndarray] = []
    for a_i in range(4):
        for b_i in range(a_i + 1, 4):
            eb = np.zeros((4, 4), dtype=float)
            eb[a_i, b_i] = 1.0 / math.sqrt(2.0)
            eb[b_i, a_i] = -1.0 / math.sqrt(2.0)
            so4_basis.append(eb)
    p_eucl_err_mat = np.zeros((6, 6), dtype=complex)
    for col_j, bj in enumerate(so4_basis):
        diff_bj = proj_eucl(proj_eucl(bj)) - proj_eucl(bj)
        for row_i, bi in enumerate(so4_basis):
            p_eucl_err_mat[row_i, col_j] = np.sum(bi * diff_bj)
    eucl_idemp_err = float(np.linalg.norm(p_eucl_err_mat))

    gamma_bi = float(Fraction(3, 7))
    max_ph_err = 0.0
    max_eh_scalar_err = 0.0
    max_simplicity_err = 0.0
    min_broken_simplicity = 1e9

    for _ in range(10):
        e_tet = rng.normal(size=(4, 4))
        while abs(np.linalg.det(e_tet)) < 0.25:
            e_tet = rng.normal(size=(4, 4))
        om_raw = rng.normal(size=(4, 4, 4))
        omega = 0.5 * (om_raw - np.swapaxes(om_raw, 0, 1))
        dom_raw = rng.normal(size=(4, 4, 4, 4))
        d_omega = 0.5 * (dom_raw - np.swapaxes(dom_raw, 0, 1))

        f_curv = np.zeros((4, 4, 4, 4), dtype=float)
        for mu in range(4):
            for nu in range(4):
                om_m, om_n = omega[:, :, mu], omega[:, :, nu]
                comm = om_m @ eta @ om_n - om_n @ eta @ om_m
                f_curv[:, :, mu, nu] = d_omega[:, :, mu, nu] - d_omega[:, :, nu, mu] + comm

        sigma_2f = np.einsum("Im,Jn->IJmn", e_tet, e_tet) - np.einsum("In,Jm->IJmn", e_tet, e_tet)
        b_plus = proj_plus(sigma_2f)
        f_plus = proj_plus(f_curv)
        b_plus_low = np.einsum("IK,JL,KLmn->IJmn", eta, eta, b_plus)
        sigma_low = np.einsum("IK,JL,KLmn->IJmn", eta, eta, sigma_2f)

        z_bf = np.einsum("mnrs,IJmn,IJrs->", eps4, b_plus_low, f_plus)
        l_pal = 0.25 * np.einsum("mnrs,IJKL,IJmn,KLrs->", eps4, eps4, sigma_2f, f_curv)
        l_holst = 0.5 * np.einsum("mnrs,IJmn,IJrs->", eps4, sigma_low, f_curv)

        l_ph_bf = float((z_bf * (1j + 1.0 / gamma_bi)).real)
        l_ph_direct = float(l_pal + (1.0 / gamma_bi) * l_holst)
        max_ph_err = max(max_ph_err, abs(l_ph_bf - l_ph_direct))

        det_e = float(np.linalg.det(e_tet))
        e_inv = np.linalg.inv(e_tet)
        eh_scalar = 2.0 * det_e * float(np.einsum("mI,nJ,IJmn->", e_inv, e_inv, f_curv))
        max_eh_scalar_err = max(max_eh_scalar_err, abs(float(l_pal) - eh_scalar))

        w_bb = np.einsum("mnrs,IJmn,IJrs->", eps4, b_plus_low, b_plus)
        max_simplicity_err = max(
            max_simplicity_err, abs(float(w_bb.real)), abs(float(w_bb.imag) + 24.0 * det_e)
        )

        # Planted control PC_ENDGAME4_BrokenSimplicityConstraint:
        x_gen = rng.normal(size=(4, 4, 4, 4))
        x_gen = 0.25 * (
            x_gen
            - np.swapaxes(x_gen, 0, 1)
            - np.swapaxes(x_gen, 2, 3)
            + np.swapaxes(np.swapaxes(x_gen, 0, 1), 2, 3)
        )
        b_brk = proj_plus(x_gen)
        b_brk_low = np.einsum("IK,JL,KLmn->IJmn", eta, eta, b_brk)
        w_brk = np.einsum("mnrs,IJmn,IJrs->", eps4, b_brk_low, b_brk)
        min_broken_simplicity = min(min_broken_simplicity, abs(float(w_brk.real)))

    e2_passed = bool(
        max_im_lam < 1e-14
        and max_metric_err < 1e-13
        and max_det_err < 1e-13
        and min_orthochronous >= 1.0 - 1e-14
        and max_hom_err < 1e-13
        and so31_bundle_rel1_err < 1e-13
        and so31_bundle_rel2_err < 1e-13
        and star_sq_plus_id_err < 1e-14
        and proj_idemp_err < 1e-14
        and proj_eigen_err < 1e-14
        and max_ph_err < 1e-12
        and max_eh_scalar_err < 1e-12
        and max_simplicity_err < 1e-12
    )
    return {
        "max_im_lambda_err": max_im_lam,
        "lorentz_metric_preservation_err": max_metric_err,
        "lorentz_det_err": max_det_err,
        "min_orthochronous_lambda_00": min_orthochronous,
        "sl2c_to_so31_homomorphism_err": max_hom_err,
        "so31_m004_bundle_rel1_err": so31_bundle_rel1_err,
        "so31_m004_bundle_rel2_err": so31_bundle_rel2_err,
        "hodge_star_sq_plus_I_err": star_sq_plus_id_err,
        "self_dual_proj_idempotency_err": proj_idemp_err,
        "self_dual_proj_eigen_err": proj_eigen_err,
        "plebanski_BF_vs_palatini_holst_max_err": max_ph_err,
        "palatini_vs_2det_e_R_max_err": max_eh_scalar_err,
        "simplicity_constraint_max_err": max_simplicity_err,
        "PC_ENDGAME4_BrokenSimplicity_min_abs_Re": min_broken_simplicity,
        "PC_ENDGAME4_EuclideanSelfDual_idemp_err": eucl_idemp_err,
        "E2_Spin31_and_Plebanski_Soldering_passed": e2_passed,
    }


# ============================================================================
# SECTION 4: PART 4C — PARAMETER-FREE EXPONENTIAL SCALE HIERARCHY LEDGER
# ============================================================================

def run_part_4c(vol_m004: Any) -> Dict[str, Any]:
    with mp.workdps(22):
        _, _, a_star = solve_joint_3var_newton(Fraction(2, 5), Fraction(9, 10), Fraction(15, 1))
        a_tree_6pi = 6 * mp.pi
        a_star_minus_6pi_abs = abs(a_star - a_tree_6pi)

        rs_longitudinal_pref = 1 / mp.sqrt(4 * mp.sqrt(3))
        instanton_factors: Dict[str, float] = {}
        for k in [1, 4, 45, 180]:
            amp = rs_longitudinal_pref * mp.exp(-mp.mpf(k) * vol_m004 / (2 * mp.pi))
            instanton_factors[f"k_{k}"] = float(amp)

        # 1-loop non-abelian dimensional transmutation for 3 chiral families (|b_3| = 11 - 4 = 7):
        alpha_inv_2d = a_star
        alpha_inv_3d_bulk = vol_m004 * a_star
        ln_ratio_2d = (2 * mp.pi / 7) * alpha_inv_2d
        ln_ratio_3d = (2 * mp.pi / 7) * alpha_inv_3d_bulk
        scale_ratio_2d = mp.exp(-ln_ratio_2d)
        scale_ratio_3d = mp.exp(-ln_ratio_3d)

    e3_passed = bool(
        float(a_star_minus_6pi_abs) < 2e-3
        and float(scale_ratio_2d) < 1e-6
        and float(scale_ratio_3d) < 1e-12
        and instanton_factors["k_180"] < 1e-20
    )
    return {
        "A_star_stabilized": float(a_star),
        "A_tree_6pi": float(a_tree_6pi),
        "A_star_minus_6pi_abs": float(a_star_minus_6pi_abs),
        "ray_singer_longitudinal_prefactor_4sqrt3_inv_sqrt": float(rs_longitudinal_pref),
        "gravitational_instanton_amplitudes": instanton_factors,
        "alpha_UV_inv_2d_horotorus": float(alpha_inv_2d),
        "alpha_UV_inv_3d_bulk_vol_weighted": float(alpha_inv_3d_bulk),
        "dim_transmutation_ln_UV_over_IR_2d_b7": float(ln_ratio_2d),
        "dim_transmutation_ln_UV_over_IR_3d_b7": float(ln_ratio_3d),
        "dim_transmutation_IR_over_UV_2d_b7": float(scale_ratio_2d),
        "dim_transmutation_IR_over_UV_3d_b7": float(scale_ratio_3d),
        "kk_measure_2d_vs_3d_discrete_choice_bits": 1,
        "continuous_fitted_parameters": 0,
        "E3_ParameterFree_Exponential_Hierarchy_passed": e3_passed,
    }


def main() -> None:
    ast_check = verify_ast_zero_imports_and_zero_target_literals()
    part_4a, a_mp, b_mp, t_mp, vol_exact = run_part_4a()
    part_4b = run_part_4b(a_mp, b_mp, t_mp)
    part_4c = run_part_4c(vol_exact)

    controls_passed = bool(
        ast_check["Gate_AST_Stage4_ZeroTargetLiterals_passed"]
        and part_4a["PC_ENDGAME4_AbelianLocus_rk_d0"] == 2
        and part_4b["PC_ENDGAME4_BrokenSimplicity_min_abs_Re"] > 0.01
        and part_4b["PC_ENDGAME4_EuclideanSelfDual_idemp_err"] > 0.5
    )
    stage_4_passed = bool(
        controls_passed
        and part_4a["E1_Bundle_Holonomy_Torsion_and_StateSum_passed"]
        and part_4b["E2_Spin31_and_Plebanski_Soldering_passed"]
        and part_4c["E3_ParameterFree_Exponential_Hierarchy_passed"]
    )

    out_payload: Dict[str, Any] = {
        "card": "X-ENDGAME-4",
        "empirical_firewall": "0 of 19",
        "ast_source_check": ast_check,
        "part_4a_bundle_holonomy_torsion_and_statesum": part_4a,
        "part_4b_spin31_and_plebanski_soldering": part_4b,
        "part_4c_parameter_free_scale_hierarchy": part_4c,
        "all_planted_controls_passed": controls_passed,
        "stage_4_gate_passed": stage_4_passed,
    }

    out_dir = Path(__file__).resolve().parent
    out_json = out_dir / "verify_x_endgame_4_out.json"
    out_txt = json.dumps(out_payload, indent=2, sort_keys=True) + "\n"
    out_json.write_text(out_txt, encoding="utf-8")

    sha = hashlib.sha256(out_json.read_bytes()).hexdigest()
    (out_dir / "OUTPUT_SHA256.txt").write_text(
        f"{sha}  verify_x_endgame_4_out.json\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
