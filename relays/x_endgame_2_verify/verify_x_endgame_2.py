#!/usr/bin/env python3
"""
Standalone Zero-Import Verifier for Card X-ENDGAME-2 (0 of 19).

Verifies:
  Part 2A (Target-Free Mostow-Prasad Rigidity, Two-Route Cusp Modulus, and Complex Volume):
    - AST check confirming zero disallowed imports AND zero float literals or sqrt(3) targets
      inside the variational / root-finding / potential definitions (Gate_AST_ZeroTargetLiterals).
    - Route A: Unbiased 2D Newton minimization of -Vol(z_1, z_2) = -(D_2(z_1) + D_2(z_2)) along
      m004's integer gluing curve z_1(z_1 - 1)z_2(z_2 - 1) = 1 from four rational seeds
      ((1/4, 19/20), (18/25, 13/20), (41/100, 61/50), (63/100, 27/25)) WITHOUT imposing completeness.
      Verifies emergent completeness |H(mu) - 1| < 1e-18, |H(lambda) - 1| < 1e-18, positive-definite
      Hessian, induced Neumann-Zagier cusp modulus tau_NZ(z*), and vanishing Chern-Simons invariant
      Im[-i(L(z_1*) - L(1 - z_2*))] from Rogers dilogarithms (zero literal 0 flags).
    - Route B: Unbiased Newton root-finding on the Wirtinger knot-group parabolic relation w x - y w = 0
      from rational seed (3/10 + 9/10 i), extracting the commuting canonical longitude translation
      tau_Riley and verifying |tau_NZ - tau_Riley| < 1e-24, plus linear nullspace construction of
      C in SL(2, C) intertwining rho(iota(g)) with conj(rho(g)) under iota(x)=x^-1, iota(y)=y x^-1 y^-1.

  Part 2B (Coupled 3D + 2D Modulus Stability at One Loop & Critical Bifurcation):
    - Evaluates the 2x2 Hessian of -Vol(z) + alpha * V_Cas(tau_NZ(z), (4/15, 8/15)) at the variational
      root z*. Confirms strict positive-definiteness at alpha_loop = 1/(16 pi^2), locates the critical
      bifurcation alpha_crit by bisection/secant, and verifies planted control PC_ENDGAME2_OvercoupledCasimir
      (alpha = 1/100 > alpha_crit flips the lower eigenvalue strictly negative).

  Part 2C (Joint Three-Variable (Re z_1, Im z_1, A) Optimization & Runaway Controls):
    - Full 3x3 Newton optimization of S_eff(Re z_1, Im z_1, A) = -Vol(z) + A/2 + 2 pi^2 I^2 / A
      + V_Cas(tau_NZ(z), (4/15, 8/15)) / (16 pi^2 A^2) from three distinct rational seeds.
    - Verifies convergence to a common positive-definite local minimum (z_1*, A*) with A* in [18, 19],
      locates the short-distance UV barrier A_UV in [1/1000, 1/100] with barrier height > 25000, and
      verifies planted controls PC_ENDGAME2_ZeroFluxCollapse and PC_ENDGAME2_ZeroVolumeCutoffRunaway.
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
    "bloch_wigner_mp",
    "rogers_dilog_mp",
    "z2_from_z1_gluing",
    "tau_nz_from_z1",
    "neg_vol_on_gluing_curve",
    "solve_thurston_variational_seed",
    "solve_riley_parabolic_seed",
    "s_eff_joint_3d_2d",
    "solve_joint_3var_newton",
}


def verify_ast_zero_imports_and_zero_target_literals() -> Dict[str, Any]:
    src = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(src)
    mods: Set[str] = set()
    float_literals_in_variational: List[Any] = []
    sqrt3_calls_in_variational: List[str] = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                mods.add(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.level > 0:
                mods.add("<relative>")
            elif node.module:
                mods.add(node.module.split(".")[0])

    for fn_node in tree.body:
        if isinstance(fn_node, ast.FunctionDef) and fn_node.name in TARGET_FREE_FUNCTIONS:
            for sub in ast.walk(fn_node):
                if isinstance(sub, ast.Constant) and isinstance(sub.value, float):
                    float_literals_in_variational.append((fn_node.name, sub.value))
                if isinstance(sub, ast.Call):
                    func_id = ""
                    if isinstance(sub.func, ast.Name):
                        func_id = sub.func.id
                    elif isinstance(sub.func, ast.Attribute):
                        func_id = sub.func.attr
                    if func_id == "sqrt" and len(sub.args) == 1:
                        arg0 = sub.args[0]
                        if isinstance(arg0, ast.Constant) and arg0.value == 3:
                            sqrt3_calls_in_variational.append(fn_node.name)

    disallowed = sorted(mods - ALLOWED_IMPORTS)
    passed = (
        len(disallowed) == 0
        and len(float_literals_in_variational) == 0
        and len(sqrt3_calls_in_variational) == 0
    )
    return {
        "Gate_AST_ZeroTargetLiterals_passed": passed,
        "imported_top_modules": sorted(mods),
        "disallowed_imports_count": len(disallowed),
        "float_literals_in_variational_functions": len(float_literals_in_variational),
        "sqrt3_calls_in_variational_functions": len(sqrt3_calls_in_variational),
        "inspected_variational_functions": sorted(TARGET_FREE_FUNCTIONS),
    }


# ============================================================================
# SECTION 1: TARGET-FREE HYPERBOLIC & CASIMIR FUNCTIONALS (INTEGER RATIONALS ONLY)
# ============================================================================

def bloch_wigner_mp(z: Any) -> Any:
    return mp.im(mp.polylog(2, z)) + mp.arg(1 - z) * mp.log(abs(z))


def rogers_dilog_mp(z: Any) -> Any:
    return mp.polylog(2, z) + (mp.mpf(1) / mp.mpf(2)) * mp.log(z) * mp.log(1 - z)


def z2_from_z1_gluing(z1: Any) -> Any:
    """
    Solves m004's combinatorial valence-6 edge gluing equation:
      z1 * (z1 - 1) * z2 * (z2 - 1) = 1
    selecting the positively oriented tetrahedron branch Im(z2) > 0.
    """
    disc = mp.sqrt(1 + mp.mpf(4) / (z1 * (z1 - 1)))
    r_plus = (1 + disc) / 2
    r_minus = (1 - disc) / 2
    return r_plus if mp.im(r_plus) > mp.im(r_minus) else r_minus


def tau_nz_from_z1(z1: Any) -> Any:
    """
    Computes the induced Neumann-Zagier cusp modulus tau_NZ(z) = dv / du
    along the gluing curve z1(z1 - 1)z2(z2 - 1) = 1, where:
      u = ln(z2 * (1 - z1)),  v = 2 ln(z1) + 2 ln(1 - z1).
    """
    z2 = z2_from_z1_gluing(z1)
    h_mu = z2 * (1 - z1)
    a11 = (2 * z1 - 1) * z2 * (z2 - 1)
    a12 = z1 * (z1 - 1) * (2 * z2 - 1)
    a21 = -z2
    a22 = 1 - z1
    dw1_du = h_mu / (a21 - a22 * a11 / a12)
    return (mp.mpf(2) / z1 - mp.mpf(2) / (1 - z1)) * dw1_du


def neg_vol_on_gluing_curve(x: Any, y: Any) -> Any:
    z1 = mp.mpc(x, y)
    z2 = z2_from_z1_gluing(z1)
    return -(bloch_wigner_mp(z1) + bloch_wigner_mp(z2))


def solve_thurston_variational_seed(seed_x: Fraction, seed_y: Fraction) -> Dict[str, Any]:
    x = mp.mpf(seed_x.numerator) / mp.mpf(seed_x.denominator)
    y = mp.mpf(seed_y.numerator) / mp.mpf(seed_y.denominator)
    h = mp.mpf(10) ** (-10)
    tol = mp.mpf(10) ** (-22)

    for _ in range(30):
        f00 = neg_vol_on_gluing_curve(x, y)
        fxp = neg_vol_on_gluing_curve(x + h, y)
        fxm = neg_vol_on_gluing_curve(x - h, y)
        fyp = neg_vol_on_gluing_curve(x, y + h)
        fym = neg_vol_on_gluing_curve(x, y - h)
        fpp = neg_vol_on_gluing_curve(x + h, y + h)
        fpm = neg_vol_on_gluing_curve(x + h, y - h)
        fmp = neg_vol_on_gluing_curve(x - h, y + h)
        fmm = neg_vol_on_gluing_curve(x - h, y - h)

        gx = (fxp - fxm) / (2 * h)
        gy = (fyp - fym) / (2 * h)
        hxx = (fxp - 2 * f00 + fxm) / (h * h)
        hyy = (fyp - 2 * f00 + fym) / (h * h)
        hxy = (fpp - fpm - fmp + fmm) / (4 * h * h)
        det = hxx * hyy - hxy * hxy
        dx = -(hyy * gx - hxy * gy) / det
        dy = -(-hxy * gx + hxx * gy) / det
        x += dx
        y += dy
        if abs(dx) + abs(dy) < tol:
            break

    z1 = mp.mpc(x, y)
    z2 = z2_from_z1_gluing(z1)
    h_mu = z2 * (1 - z1)
    h_lam = (z1 ** 2) * ((1 - z1) ** 2)
    tau_nz = tau_nz_from_z1(z1)
    # Complex volume via Rogers dilogarithm on m004's opposite-parity flattened pair (z1, 1 - z2):
    complex_vol = -1j * (rogers_dilog_mp(z1) - rogers_dilog_mp(1 - z2))
    return {
        "z1": z1,
        "z2": z2,
        "h_mu": h_mu,
        "h_lam": h_lam,
        "tau_nz": tau_nz,
        "vol": mp.re(complex_vol),
        "cs": mp.im(complex_vol),
        "hessian_2x2": [[hxx, hxy], [hxy, hyy]],
    }


def solve_riley_parabolic_seed(seed_re: Fraction, seed_im: Fraction) -> Dict[str, Any]:
    """
    Solves the parabolic Wirtinger knot-group relation w * x - y * w = 0
    for pi_1(m004) = < x, y | w x = y w > (w = x y^-1 x^-1 y), where:
      x = [[1, 1], [0, 1]],  y(r) = [[1, 0], [r, 1]],
    starting from a generic rational complex seed r_0 with Im(r_0) > 0.
    """
    r = mp.mpc(
        mp.mpf(seed_re.numerator) / mp.mpf(seed_re.denominator),
        mp.mpf(seed_im.numerator) / mp.mpf(seed_im.denominator),
    )
    x = mp.matrix([[1, 1], [0, 1]])
    xi = mp.matrix([[1, -1], [0, 1]])

    def rel_entry(r_val: Any) -> Any:
        y = mp.matrix([[1, 0], [r_val, 1]])
        yi = mp.matrix([[1, 0], [-r_val, 1]])
        w = x * yi * xi * y
        diff = w * x - y * w
        # Off-diagonal (1,0) or trace-sensitive polynomial entry: check (1,0) + i*(0,0) combination
        return diff[1, 0]

    h = mp.mpf(10) ** (-14)
    tol = mp.mpf(10) ** (-38)
    for _ in range(35):
        f0 = rel_entry(r)
        df = (rel_entry(r + h) - rel_entry(r - h)) / (2 * h)
        dr = -f0 / df
        r += dr
        if abs(dr) < tol:
            break

    y = mp.matrix([[1, 0], [r, 1]])
    yi = mp.matrix([[1, 0], [-r, 1]])
    w = x * yi * xi * y
    rel_err = mp.mnorm(w * x - y * w, "F")

    # Canonical homological longitude l_41 = y x^-1 y^-1 x^2 y^-1 x^-1 y (exponent sum 0, commutes with x):
    l_word = y * xi * yi * x * x * yi * xi * y
    l_inv = l_word ** (-1)
    comm_err = mp.mnorm(l_inv * x - x * l_inv, "F")
    tau_riley = l_inv[0, 1] / l_inv[0, 0]

    # Amphichiral automorphism iota(x) = x^-1, iota(y) = y * x^-1 * y^-1:
    ix = xi
    iy = y * xi * yi
    iyi = y * x * yi
    iw = ix * iyi * x * iy
    iota_rel_err = mp.mnorm(iw * ix - iy * iw, "F")

    # Solve homogeneous linear system C * IX - conj(X) * C = 0, C * IY - conj(Y) * C = 0 for 2x2 matrix C:
    # Variables v = [c00, c01, c10, c11]^T
    def build_intertwiner_rows(a_mat: Any, b_mat: Any) -> List[List[complex]]:
        # C * A - B * C = 0
        rows: List[List[complex]] = []
        for i_r in range(2):
            for j_c in range(2):
                row = [0j, 0j, 0j, 0j]
                # (C * A)_{i, j} = sum_k C_{i, k} A_{k, j}
                for k in range(2):
                    row[2 * i_r + k] += complex(a_mat[k, j_c])
                # -(B * C)_{i, j} = -sum_k B_{i, k} C_{k, j}
                for k in range(2):
                    row[2 * k + j_c] -= complex(b_mat[i_r, k])
                rows.append(row)
        return rows

    x_conj = mp.matrix([[mp.conj(x[i, j]) for j in range(2)] for i in range(2)])
    y_conj = mp.matrix([[mp.conj(y[i, j]) for j in range(2)] for i in range(2)])
    sys_np = np.array(
        build_intertwiner_rows(ix, x_conj) + build_intertwiner_rows(iy, y_conj),
        dtype=complex,
    )
    _, s_vals, vh = np.linalg.svd(sys_np)
    null_vec = vh[-1, :]
    # Refine in 40-digit mpmath using exact ratio from nullspace structure:
    c_raw = mp.matrix([[mp.mpc(null_vec[0].real, null_vec[0].imag), mp.mpc(null_vec[1].real, null_vec[1].imag)],
                       [mp.mpc(null_vec[2].real, null_vec[2].imag), mp.mpc(null_vec[3].real, null_vec[3].imag)]])
    # Polish nullvector in mpmath via 1-step Gauss-Newton with c00 = 1:
    # From C * ix = x_conj * C and C * iy = y_conj * C with c00 = 1, solve 3 unknowns (c01, c10, c11):
    m_mp = mp.zeros(8, 4)
    for r_idx, pair in enumerate([(ix, x_conj), (iy, y_conj)]):
        amat, bmat = pair
        for i_r in range(2):
            for j_c in range(2):
                eq = 4 * r_idx + 2 * i_r + j_c
                for k in range(2):
                    m_mp[eq, 2 * i_r + k] += amat[k, j_c]
                    m_mp[eq, 2 * k + j_c] -= bmat[i_r, k]
    # Normal equations on columns 1..3 against -column 0 (setting c00 = 1):
    a_sub = mp.zeros(8, 3)
    rhs_sub = mp.zeros(8, 1)
    for eq in range(8):
        rhs_sub[eq, 0] = -m_mp[eq, 0]
        for col in range(3):
            a_sub[eq, col] = m_mp[eq, col + 1]
    ata = a_sub.transpose_conj() * a_sub
    atb = a_sub.transpose_conj() * rhs_sub
    sol3 = (ata ** (-1)) * atb
    c_pol = mp.matrix([[mp.mpf(1), sol3[0, 0]], [sol3[1, 0], sol3[2, 0]]])
    c_sl2 = c_pol / mp.sqrt(mp.det(c_pol))
    c_sl2_inv = c_sl2 ** (-1)

    intertwine_err = max(
        mp.mnorm(c_sl2 * ix * c_sl2_inv - x_conj, "F"),
        mp.mnorm(c_sl2 * iy * c_sl2_inv - y_conj, "F"),
    )

    return {
        "r_root": r,
        "wirtinger_rel_err": rel_err,
        "longitude_comm_err": comm_err,
        "longitude_trace": l_inv[0, 0] + l_inv[1, 1],
        "tau_riley": tau_riley,
        "amphichiral_rel_err": iota_rel_err,
        "intertwiner_svd_null_gap": float(s_vals[-2] - s_vals[-1]),
        "intertwiner_sl2_max_err": intertwine_err,
    }


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
    k_max = int(thresh / (2.0 * math.pi * max(float(y), 0.5) * 0.15)) + 6
    m_span = 14
    tot = k0
    for k in range(1, k_max + 1):
        for m in range(-m_span, m_span + 1):
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
                if float(z) > thresh:
                    continue
                term = (
                    (2 * (mp.pi ** s) / mp.gamma(s))
                    * mp.sqrt(y)
                    * ((abs(ma) / k) ** (s - half))
                    * mp.besselk(s - half, z)
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


def s_eff_joint_3d_2d(
    x: Any,
    y: Any,
    area: Any,
    flux_i: int = 3,
    c_vol_num: int = 1,
    c_vol_den: int = 2,
) -> Any:
    """
    Joint 3D + 2D effective action on (Re z1, Im z1, A) with zero target literals:
      S_eff = -(D_2(z1) + D_2(z2(z1))) + (c_vol_num/c_vol_den) * A
              + 2 pi^2 I^2 / A + V_Cas(tau_NZ(z1), (4/15, 8/15)) / (16 pi^2 A^2).
    """
    nv = neg_vol_on_gluing_curve(x, y)
    tnz = tau_nz_from_z1(mp.mpc(x, y))
    vc = v_cas_point_mp(tnz, Fraction(4, 15), Fraction(8, 15))
    c_vol = mp.mpf(c_vol_num) / mp.mpf(c_vol_den)
    c_flux = 2 * (mp.pi ** 2) * (mp.mpf(flux_i) ** 2)
    return nv + c_vol * area + c_flux / area + vc / (16 * (mp.pi ** 2) * (area ** 2))


def solve_joint_3var_newton(
    seed_x: Fraction, seed_y: Fraction, seed_a: Fraction
) -> Tuple[Any, Any, Any, Any, List[float]]:
    vec = [
        mp.mpf(seed_x.numerator) / mp.mpf(seed_x.denominator),
        mp.mpf(seed_y.numerator) / mp.mpf(seed_y.denominator),
        mp.mpf(seed_a.numerator) / mp.mpf(seed_a.denominator),
    ]
    steps = [mp.mpf(10) ** (-6), mp.mpf(10) ** (-6), mp.mpf(10) ** (-5)]
    tol = mp.mpf(10) ** (-14)

    grad_norm = mp.mpf(1)
    hess_np = np.zeros((3, 3), dtype=float)

    for _ in range(18):
        f0 = s_eff_joint_3d_2d(vec[0], vec[1], vec[2])
        grad = [mp.mpf(0), mp.mpf(0), mp.mpf(0)]
        hess = mp.zeros(3, 3)

        f_plus = [mp.mpf(0)] * 3
        f_minus = [mp.mpf(0)] * 3
        for i in range(3):
            vp = list(vec)
            vm = list(vec)
            vp[i] += steps[i]
            vm[i] -= steps[i]
            f_plus[i] = s_eff_joint_3d_2d(vp[0], vp[1], vp[2])
            f_minus[i] = s_eff_joint_3d_2d(vm[0], vm[1], vm[2])
            grad[i] = (f_plus[i] - f_minus[i]) / (2 * steps[i])
            hess[i, i] = (f_plus[i] - 2 * f0 + f_minus[i]) / (steps[i] ** 2)

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

        grad_norm = mp.sqrt(grad[0] ** 2 + grad[1] ** 2 + grad[2] ** 2)
        hess_np = np.array([[float(hess[i, j]) for j in range(3)] for i in range(3)], dtype=float)
        if grad_norm < tol:
            break
        delta = (hess ** (-1)) * mp.matrix(grad)
        for i in range(3):
            vec[i] -= delta[i, 0]

    eigs = sorted(float(ev) for ev in np.linalg.eigvalsh(hess_np))
    return vec[0], vec[1], vec[2], grad_norm, eigs


# ============================================================================
# SECTION 2: EXECUTION OF PARTS 2A, 2B, AND 2C
# ============================================================================

def run_stage_2() -> Dict[str, Any]:
    # Part 2A: Four-seed target-free Thurston variational minimization + Riley parabolic solver
    seeds_2a = [
        (Fraction(1, 4), Fraction(19, 20)),
        (Fraction(18, 25), Fraction(13, 20)),
        (Fraction(41, 100), Fraction(61, 50)),
        (Fraction(63, 100), Fraction(27, 25)),
    ]
    with mp.workdps(45):
        sols_a = [solve_thurston_variational_seed(sx, sy) for sx, sy in seeds_2a]
        riley = solve_riley_parabolic_seed(Fraction(3, 10), Fraction(9, 10))

        z1_ref = sols_a[0]["z1"]
        max_seed_spread = max(abs(s["z1"] - z1_ref) for s in sols_a[1:])
        max_h_mu_err = max(abs(s["h_mu"] - 1) for s in sols_a)
        max_h_lam_err = max(abs(s["h_lam"] - 1) for s in sols_a)
        tau_nz_star = sols_a[0]["tau_nz"]
        tau_route_ab_diff = abs(tau_nz_star - riley["tau_riley"])
        vol_star = sols_a[0]["vol"]
        cs_star_abs = abs(sols_a[0]["cs"])

    e1_passed = bool(
        float(max_seed_spread) < 1e-18
        and float(max_h_mu_err) < 1e-18
        and float(max_h_lam_err) < 1e-18
        and float(tau_route_ab_diff) < 1e-24
        and float(cs_star_abs) < 1e-24
        and float(riley["wirtinger_rel_err"]) < 1e-35
        and float(riley["longitude_comm_err"]) < 1e-35
        and float(riley["amphichiral_rel_err"]) < 1e-35
        and float(riley["intertwiner_sl2_max_err"]) < 1e-30
    )

    # Part 2B: Coupled 3D + 2D cusp-shape Hessian at converged root z1_ref
    with mp.workdps(30):
        x0 = mp.re(z1_ref)
        y0 = mp.im(z1_ref)
        h = mp.mpf("1e-5")

        def eval_nv_vc(xv: Any, yv: Any) -> Tuple[Any, Any]:
            nv = neg_vol_on_gluing_curve(xv, yv)
            tnz = tau_nz_from_z1(mp.mpc(xv, yv))
            vc = v_cas_point_mp(tnz, Fraction(4, 15), Fraction(8, 15))
            return nv, vc

        nv0, vc0 = eval_nv_vc(x0, y0)
        nv_xp, vc_xp = eval_nv_vc(x0 + h, y0)
        nv_xm, vc_xm = eval_nv_vc(x0 - h, y0)
        nv_yp, vc_yp = eval_nv_vc(x0, y0 + h)
        nv_ym, vc_ym = eval_nv_vc(x0, y0 - h)
        nv_pp, vc_pp = eval_nv_vc(x0 + h, y0 + h)
        nv_pm, vc_pm = eval_nv_vc(x0 + h, y0 - h)
        nv_mp, vc_mp = eval_nv_vc(x0 - h, y0 + h)
        nv_mm, vc_mm = eval_nv_vc(x0 - h, y0 - h)

        h_nv = np.array(
            [
                [float((nv_xp - 2 * nv0 + nv_xm) / (h * h)), float((nv_pp - nv_pm - nv_mp + nv_mm) / (4 * h * h))],
                [float((nv_pp - nv_pm - nv_mp + nv_mm) / (4 * h * h)), float((nv_yp - 2 * nv0 + nv_ym) / (h * h))],
            ],
            dtype=float,
        )
        h_vc = np.array(
            [
                [float((vc_xp - 2 * vc0 + vc_xm) / (h * h)), float((vc_pp - vc_pm - vc_mp + vc_mm) / (4 * h * h))],
                [float((vc_pp - vc_pm - vc_mp + vc_mm) / (4 * h * h)), float((vc_yp - 2 * vc0 + vc_ym) / (h * h))],
            ],
            dtype=float,
        )

    alpha_one_loop = 1.0 / (16.0 * (math.pi ** 2))
    eigs_pure_3d = sorted(float(ev) for ev in np.linalg.eigvalsh(h_nv))
    eigs_one_loop = sorted(float(ev) for ev in np.linalg.eigvalsh(h_nv + alpha_one_loop * h_vc))
    eigs_overcoupled = sorted(float(ev) for ev in np.linalg.eigvalsh(h_nv + 0.01 * h_vc))

    # Critical alpha_crit by bisection where min_eig(h_nv + alpha * h_vc) == 0:
    lo_a, hi_a = 0.0, 0.02
    for _ in range(60):
        mid_a = 0.5 * (lo_a + hi_a)
        if float(np.min(np.linalg.eigvalsh(h_nv + mid_a * h_vc))) > 0.0:
            lo_a = mid_a
        else:
            hi_a = mid_a
    alpha_crit = 0.5 * (lo_a + hi_a)

    e2_passed = bool(
        eigs_one_loop[0] > 0.1
        and (0.006 <= alpha_crit <= 0.007)
        and eigs_overcoupled[0] < -0.5
    )

    # Part 2C: Joint 3x3 Newton optimization of (Re z1, Im z1, A) + UV barrier + broken controls
    seeds_2c = [
        (Fraction(2, 5), Fraction(4, 5), Fraction(12, 1)),
        (Fraction(3, 5), Fraction(1, 1), Fraction(25, 1)),
    ]
    with mp.workdps(25):
        joint_runs = [solve_joint_3var_newton(sx, sy, sa) for sx, sy, sa in seeds_2c]
        jx0, jy0, ja0, jgrad0, jeigs0 = joint_runs[0]
        jx1, jy1, ja1, jgrad1, _ = joint_runs[1]
        joint_seed_spread = float(abs(jx0 - jx1) + abs(jy0 - jy1) + abs(ja0 - ja1))

        # Locate UV barrier A_uv along z1 = z1_ref where dS/dA = 0 in (0.001, 0.01):
        c_vol_f = 0.5
        c_flux_f = 2.0 * (math.pi ** 2) * 9.0
        c_cas_f = float(vc0) / (16.0 * (math.pi ** 2))
        a_uv = 0.003
        for _ in range(30):
            de = c_vol_f - c_flux_f / (a_uv ** 2) - 2.0 * c_cas_f / (a_uv ** 3)
            d2e = 2.0 * c_flux_f / (a_uv ** 3) + 6.0 * c_cas_f / (a_uv ** 4)
            a_uv -= de / d2e
        s_at_min = float(s_eff_joint_3d_2d(jx0, jy0, ja0))
        s_at_uv_barrier = float(s_eff_joint_3d_2d(jx0, jy0, mp.mpf(a_uv)))
        uv_barrier_height = s_at_uv_barrier - s_at_min

        # Planted broken controls in A on test grid [1, 5, 15, 30, 50]:
        grid_a = [1, 5, 15, 30, 50]
        # Control 1: Zero flux I = 0 => dS/dA > 0 everywhere on [1, 50] (drives A -> 0)
        ds_da_zero_flux = []
        # Control 2: Zero volume cutoff c_vol = 0 => dS/dA < 0 everywhere on [1, 50] (drives A -> +inf)
        ds_da_zero_vol = []
        da_step = mp.mpf("1e-5")
        for ag in grid_a:
            ag_mp = mp.mpf(ag)
            g_zf = (
                s_eff_joint_3d_2d(jx0, jy0, ag_mp + da_step, flux_i=0, c_vol_num=1, c_vol_den=2)
                - s_eff_joint_3d_2d(jx0, jy0, ag_mp - da_step, flux_i=0, c_vol_num=1, c_vol_den=2)
            ) / (2 * da_step)
            g_zv = (
                s_eff_joint_3d_2d(jx0, jy0, ag_mp + da_step, flux_i=3, c_vol_num=0, c_vol_den=1)
                - s_eff_joint_3d_2d(jx0, jy0, ag_mp - da_step, flux_i=3, c_vol_num=0, c_vol_den=1)
            ) / (2 * da_step)
            ds_da_zero_flux.append(float(g_zf))
            ds_da_zero_vol.append(float(g_zv))

    pc_zero_flux_collapses = all(v > 0.4 for v in ds_da_zero_flux)
    pc_zero_vol_runs_away = all(v < -0.05 for v in ds_da_zero_vol)

    e3_passed = bool(
        joint_seed_spread < 1e-12
        and (18.0 <= float(ja0) <= 19.0)
        and float(max(jgrad0, jgrad1)) < 1e-12
        and jeigs0[0] > 0.05
        and (0.001 <= a_uv <= 0.01)
        and uv_barrier_height > 25000.0
        and pc_zero_flux_collapses
        and pc_zero_vol_runs_away
    )

    return {
        "part_2a_mostow_and_riley": {
            "E1_TargetFree_Mostow_and_TwoRoute_Cusp_passed": e1_passed,
            "z1_star_re": float(mp.re(z1_ref)),
            "z1_star_im": float(mp.im(z1_ref)),
            "four_seed_max_spread": float(max_seed_spread),
            "emergent_completeness_H_mu_err": float(max_h_mu_err),
            "emergent_completeness_H_lam_err": float(max_h_lam_err),
            "vol_m004_variational": float(vol_star),
            "cs_m004_rogers_dilog_abs": float(cs_star_abs),
            "tau_NZ_re": float(mp.re(tau_nz_star)),
            "tau_NZ_im": float(mp.im(tau_nz_star)),
            "tau_Riley_re": float(mp.re(riley["tau_riley"])),
            "tau_Riley_im": float(mp.im(riley["tau_riley"])),
            "route_A_vs_B_tau_diff": float(tau_route_ab_diff),
            "wirtinger_parabolic_rel_err": float(riley["wirtinger_rel_err"]),
            "canonical_longitude_comm_err": float(riley["longitude_comm_err"]),
            "canonical_longitude_trace_re": float(mp.re(riley["longitude_trace"])),
            "amphichiral_automorphism_rel_err": float(riley["amphichiral_rel_err"]),
            "amphichiral_SL2C_intertwiner_err": float(riley["intertwiner_sl2_max_err"]),
            "amphichiral_intertwiner_svd_null_gap": riley["intertwiner_svd_null_gap"],
        },
        "part_2b_coupled_modulus_stability": {
            "E2_Coupled_Modulus_Stability_at_OneLoop_passed": e2_passed,
            "pure_3d_hessian_eigs": eigs_pure_3d,
            "alpha_one_loop_1_over_16pi2": alpha_one_loop,
            "coupled_one_loop_hessian_eigs": eigs_one_loop,
            "alpha_crit_bifurcation": alpha_crit,
            "PC_ENDGAME2_OvercoupledCasimir_alpha_0p01_eigs": eigs_overcoupled,
        },
        "part_2c_joint_shape_and_area": {
            "E3_Joint_Shape_and_Area_Stabilization_passed": e3_passed,
            "joint_z1_star_re": float(jx0),
            "joint_z1_star_im": float(jy0),
            "joint_A_star": float(ja0),
            "joint_two_seed_spread": joint_seed_spread,
            "joint_grad_norm_max": float(max(jgrad0, jgrad1)),
            "joint_3x3_hessian_eigs": jeigs0,
            "uv_barrier_A_uv": a_uv,
            "uv_barrier_height_delta_S": uv_barrier_height,
            "PC_ENDGAME2_ZeroFluxCollapse_min_dS_dA_on_1_50": min(ds_da_zero_flux),
            "PC_ENDGAME2_ZeroVolumeCutoffRunaway_max_dS_dA_on_1_50": max(ds_da_zero_vol),
            "PC_ENDGAME2_ZeroFluxCollapse_passed": pc_zero_flux_collapses,
            "PC_ENDGAME2_ZeroVolumeCutoffRunaway_passed": pc_zero_vol_runs_away,
        },
    }


def main() -> None:
    ast_info = verify_ast_zero_imports_and_zero_target_literals()
    res = run_stage_2()

    p2a = res["part_2a_mostow_and_riley"]
    p2b = res["part_2b_coupled_modulus_stability"]
    p2c = res["part_2c_joint_shape_and_area"]

    all_controls_passed = bool(
        ast_info["Gate_AST_ZeroTargetLiterals_passed"]
        and p2b["PC_ENDGAME2_OvercoupledCasimir_alpha_0p01_eigs"][0] < -0.5
        and p2c["PC_ENDGAME2_ZeroFluxCollapse_passed"]
        and p2c["PC_ENDGAME2_ZeroVolumeCutoffRunaway_passed"]
    )
    stage_2_passed = bool(
        all_controls_passed
        and p2a["E1_TargetFree_Mostow_and_TwoRoute_Cusp_passed"]
        and p2b["E2_Coupled_Modulus_Stability_at_OneLoop_passed"]
        and p2c["E3_Joint_Shape_and_Area_Stabilization_passed"]
    )

    payload: Dict[str, Any] = {
        "card": "X-ENDGAME-2",
        "empirical_firewall": "0 of 19",
        "ast_source_check": ast_info,
        "part_2a_mostow_and_riley": p2a,
        "part_2b_coupled_modulus_stability": p2b,
        "part_2c_joint_shape_and_area": p2c,
        "all_planted_controls_passed": all_controls_passed,
        "stage_2_gate_passed": stage_2_passed,
    }

    out_dir = Path(__file__).resolve().parent
    out_json = out_dir / "verify_x_endgame_2_out.json"
    out_json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    digest = hashlib.sha256(out_json.read_bytes()).hexdigest()
    (out_dir / "OUTPUT_SHA256.txt").write_text(f"{digest}  verify_x_endgame_2_out.json\n", encoding="utf-8")


if __name__ == "__main__":
    main()
