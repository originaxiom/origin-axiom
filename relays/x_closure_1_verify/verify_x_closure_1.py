#!/usr/bin/env python3
"""
Standalone Zero-Import Verifier for Card X-CLOSURE-1:
  Part 1A: Repaired 2^{-1} mod N Metaplectic Weil Generators ((ST)^3 = S^2, Zero Defect),
           Unit-Shear Heisenberg Conjugation, Gauss-Sum CRT Factorization, & Anomaly Lock.
  Part 1B: True Goerner-Zickert-Neumann Flattened Extended Rogers Dilogarithm Complex
           Chern-Simons Engine (m004 = 0 vs Chiral Sister m003 = 1/4 & Chiral 5_2 Knot
           m015 = -0.15320413...) + Explicit Tier-II Scoping of Bare 4D Parity Theta.

Empirical Firewall: 0 of 19 (zero Standard Model empirical targets read, imported, or compared;
the published SnapPy m015 pure-topology Chern-Simons benchmark float is strictly AST-isolated
inside check_m015_published_snappy_benchmark).
"""

from __future__ import annotations

import ast
from fractions import Fraction
import hashlib
import itertools
import json
import math
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

import mpmath as mp
import sympy as sp


# ============================================================================
# SECTION 0: AST SOURCE AUDIT (ZERO IMPORTS & MODEL ZERO-FLOAT ISOLATION)
# ============================================================================

ALLOWED_IMPORTS: Set[str] = {
    "__future__",
    "ast",
    "fractions",
    "hashlib",
    "itertools",
    "json",
    "math",
    "mpmath",
    "pathlib",
    "sympy",
    "typing",
}

BENCHMARK_ONLY_FUNCTIONS: Set[str] = {
    "check_m015_published_snappy_benchmark",
}


def verify_ast_closure1() -> Dict[str, Any]:
    src = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(src)
    mods: Set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                mods.add(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.level > 0:
                mods.add("<relative>")
            elif node.module:
                mods.add(node.module.split(".")[0])

    disallowed = sorted(mods - ALLOWED_IMPORTS)
    non_benchmark_float_literals = 0
    non_benchmark_complex_literals = 0

    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in BENCHMARK_ONLY_FUNCTIONS:
            continue
        for sub in ast.walk(node):
            if isinstance(sub, ast.Constant):
                if isinstance(sub.value, float):
                    non_benchmark_float_literals += 1
                elif isinstance(sub.value, complex):
                    non_benchmark_complex_literals += 1

    passed = (
        len(disallowed) == 0
        and non_benchmark_float_literals == 0
        and non_benchmark_complex_literals == 0
    )
    return {
        "Gate_AST_Stage1_Closure_Passed": passed,
        "imported_top_modules": sorted(mods),
        "disallowed_imports_count": len(disallowed),
        "non_benchmark_float_literals": non_benchmark_float_literals,
        "non_benchmark_complex_literals": non_benchmark_complex_literals,
        "zero_imports_from_repo_or_reports": len(disallowed) == 0,
    }


# ============================================================================
# SECTION 1: PART 1A — REPAIRED 2^{-1} MOD N WEIL METAPLECTIC GENERATORS & CRT
# ============================================================================

def build_repaired_weil_generators_mp(n_dim: int, mult_r: int) -> Tuple[Any, Any, Any]:
    """
    Standard metaplectic Weil generators on l^2(Z/NZ) for odd N and gcd(r, N) = 1:
      r_2 := (r * 2^{-1}) mod N
      T_N^{(r)}[x, x] = exp(2 pi i r_2 x^2 / N)
      gamma_N(r)      = N^{-1/2} sum_{z=0}^{N-1} exp(2 pi i r_2 z^2 / N)
      S_N^{(r)}[x, y] = (gamma_N(r) sqrt(N))^{-1} exp(-2 pi i r x y / N)
    Satisfies exact non-projective (S_N T_N)^3 = S_N^2 and unit Heisenberg shear.
    """
    assert n_dim % 2 == 1 and math.gcd(mult_r, n_dim) == 1
    inv2 = pow(2, -1, n_dim)
    r2 = (mult_r * inv2) % n_dim
    inv_sqrt = mp.mpf(1) / mp.sqrt(mp.mpf(n_dim))
    two_pi_i = mp.mpc(0, 2) * mp.pi

    gauss_sum = mp.mpc(0)
    for z in range(n_dim):
        gauss_sum += mp.exp(two_pi_i * mp.mpf((r2 * z * z) % n_dim) / mp.mpf(n_dim))
    gamma_n = inv_sqrt * gauss_sum

    t_mat = mp.zeros(n_dim, n_dim)
    s_mat = mp.zeros(n_dim, n_dim)
    s_pref = inv_sqrt / gamma_n
    for x in range(n_dim):
        t_mat[x, x] = mp.exp(two_pi_i * mp.mpf((r2 * x * x) % n_dim) / mp.mpf(n_dim))
        for y in range(n_dim):
            s_mat[x, y] = s_pref * mp.exp(-two_pi_i * mp.mpf((mult_r * x * y) % n_dim) / mp.mpf(n_dim))
    return t_mat, s_mat, gamma_n


def build_heisenberg_xz_mp(n_dim: int, mult_r: int) -> Tuple[Any, Any]:
    """Heisenberg clock/shift operators X|x> = |x + 1 mod N>, Z|x> = exp(2 pi i r x / N)|x>."""
    x_op = mp.zeros(n_dim, n_dim)
    z_op = mp.zeros(n_dim, n_dim)
    two_pi_i = mp.mpc(0, 2) * mp.pi
    for x in range(n_dim):
        x_op[(x + 1) % n_dim, x] = mp.mpf(1)
        z_op[x, x] = mp.exp(two_pi_i * mp.mpf((mult_r * x) % n_dim) / mp.mpf(n_dim))
    return x_op, z_op


def kron_mp(a_mat: Any, b_mat: Any) -> Any:
    ra, ca = a_mat.rows, a_mat.cols
    rb, cb = b_mat.rows, b_mat.cols
    out = mp.zeros(ra * rb, ca * cb)
    for r1 in range(ra):
        for c1 in range(ca):
            v = a_mat[r1, c1]
            if v != 0:
                for r2 in range(rb):
                    for c2 in range(cb):
                        out[r1 * rb + r2, c1 * cb + c2] = v * b_mat[r2, c2]
    return out


def run_part_1a_repaired_weil_and_crt() -> Dict[str, Any]:
    with mp.workdps(65):
        t15, s15, g15 = build_repaired_weil_generators_mp(15, 1)
        t5, s5, g5 = build_repaired_weil_generators_mp(5, 3)
        t3, s3, g3 = build_repaired_weil_generators_mp(3, 2)

        # 1. Non-projective metaplectic relation (S_N T_N)^3 == S_N^2 and unitarity across N in {15, 5, 3}:
        modular_rel_errs: Dict[str, float] = {}
        heisenberg_errs: Dict[str, float] = {}
        for lbl, n_d, r_m, tm, sm in [
            ("N15_r1", 15, 1, t15, s15),
            ("N5_r3", 5, 3, t5, s5),
            ("N3_r2", 3, 2, t3, s3),
        ]:
            st = sm * tm
            st3 = st * st * st
            s2 = sm * sm
            u_err = mp.mnorm(tm * tm.transpose_conj() - mp.eye(n_d), "F") + mp.mnorm(sm * sm.transpose_conj() - mp.eye(n_d), "F")
            m_err = mp.mnorm(st3 - s2, "F")
            # Check S^4 == I_N (since gamma_N^4 == 1 for all odd N and C_N^2 == I_N):
            s4_err = mp.mnorm(s2 * s2 - mp.eye(n_d), "F")
            modular_rel_errs[lbl] = float(u_err + m_err + s4_err)

            # Check unit-shear Heisenberg conjugation:
            #   S X S^-1 == Z^-1,  S Z S^-1 == X
            #   T X T^-1 == exp(2 pi i r_2 / N) * X * Z,  T Z T^-1 == Z
            x_op, z_op = build_heisenberg_xz_mp(n_d, r_m)
            r2 = (r_m * pow(2, -1, n_d)) % n_d
            zeta = mp.exp(mp.mpc(0, 2) * mp.pi * mp.mpf(r2) / mp.mpf(n_d))
            s_inv = sm.transpose_conj()
            t_inv = tm.transpose_conj()
            z_inv = z_op.transpose_conj()
            h_err = (
                mp.mnorm(sm * x_op * s_inv - z_inv, "F")
                + mp.mnorm(sm * z_op * s_inv - x_op, "F")
                + mp.mnorm(tm * x_op * t_inv - zeta * (x_op * z_op), "F")
                + mp.mnorm(tm * z_op * t_inv - z_op, "F")
            )
            heisenberg_errs[lbl] = float(h_err)

        # 2. Gauss-sum reciprocity & exact CRT Weil tensor factorization W_15^{(1)} ~= W_5^{(3)} (x) W_3^{(2)}:
        gauss_crt_err = float(abs(g15 - g5 * g3))
        p_crt = mp.zeros(15, 15)
        for u in range(5):
            for v in range(3):
                p_crt[3 * u + v, (3 * u + 5 * v) % 15] = mp.mpf(1)
        p_unit_err = float(mp.mnorm(p_crt * p_crt.transpose_conj() - mp.eye(15), "F"))
        crt_t_err = float(mp.mnorm(p_crt * t15 * p_crt.transpose_conj() - kron_mp(t5, t3), "F"))
        crt_s_err = float(mp.mnorm(p_crt * s15 * p_crt.transpose_conj() - kron_mp(s5, s3), "F"))

        # Check W_5 = 3_c (+) 2_w under parity C_5 = (S_5^{(3)})^2 (note g5 = +1 so S_5^2 == +C_5!):
        c5_op = s5 * s5
        c5_inv_err = float(mp.mnorm(c5_op * c5_op - mp.eye(5), "F"))
        proj_plus = (mp.eye(5) + c5_op) / mp.mpf(2)
        proj_minus = (mp.eye(5) - c5_op) / mp.mpf(2)
        dim_3c = int(mp.nint(mp.re(sum(proj_plus[i, i] for i in range(5)))))
        dim_2w = int(mp.nint(mp.re(sum(proj_minus[i, i] for i in range(5)))))

        # 3. Planted Control PC_CL1_DoubledShearHeisenbergDefect (Codex Item A control):
        # Un-halved T_old[x, x] = exp(2 pi i r x^2 / N) induces T0_bad = [[1, 0], [2, 1]] and (S0 T0_bad)^3 = [[4, 3], [-3, -2]] != S0^2!
        n_c, r_c = 5, 3
        t_old5 = mp.zeros(n_c, n_c)
        s_old5 = mp.zeros(n_c, n_c)
        two_pi_i = mp.mpc(0, 2) * mp.pi
        for x in range(n_c):
            t_old5[x, x] = mp.exp(two_pi_i * mp.mpf((r_c * x * x) % n_c) / mp.mpf(n_c))
            for y in range(n_c):
                s_old5[x, y] = (mp.mpf(1) / mp.sqrt(mp.mpf(n_c))) * mp.exp(-two_pi_i * mp.mpf((r_c * x * y) % n_c) / mp.mpf(n_c))
        x5, z5 = build_heisenberg_xz_mp(n_c, r_c)
        st_old3 = (s_old5 * t_old5) ** 3
        s_old2 = s_old5 * s_old5
        # Non-central Heisenberg action mismatch || (S_old T_old)^3 X (S_old T_old)^-3 - S_old^2 X S_old^-2 ||_F:
        # Note any projective scalar cancels identically in conjugation M -> U M U^-1!
        conj_st3_x = st_old3 * x5 * st_old3.transpose_conj()
        conj_s2_x = s_old2 * x5 * s_old2.transpose_conj()
        pc_doubled_shear_heis_defect = float(mp.mnorm(conj_st3_x - conj_s2_x, "F"))

    # Exact integer matrix check on Sp(2, Z):
    s0_mat = sp.Matrix([[0, 1], [-1, 0]])
    t0_good = sp.Matrix([[1, 0], [1, 1]])
    t0_bad = sp.Matrix([[1, 0], [2, 1]])
    good_sp2_zero = (s0_mat * t0_good) ** 3 - (s0_mat ** 2) == sp.zeros(2, 2)
    bad_sp2_mat = (s0_mat * t0_bad) ** 3  # == [[4, 3], [-3, -2]]

    bad_sp2_list = [[int(v) for v in row] for row in bad_sp2_mat.tolist()]

    # Exact SymPy anomaly factorization on Lambda^{even}(3_a (+) 2_b):
    a_sym, b_sym = sp.symbols("a b", real=True)
    a_u1_cubed = sp.expand(
        6 * (a_sym + b_sym) ** 3
        + 3 * (2 * a_sym) ** 3
        + (2 * b_sym) ** 3
        + 3 * (2 * a_sym + 2 * b_sym) ** 3
        + 2 * (3 * a_sym + b_sym) ** 3
    )
    factored_target = sp.expand(4 * (3 * a_sym + 2 * b_sym) * ((3 * a_sym + b_sym) ** 2 + 4 * b_sym ** 2))
    anom_factor_exact = (a_u1_cubed - factored_target) == 0
    tr_t3_sq = 6 * Fraction(1, 4) + 2 * Fraction(1, 4)
    tr_y_sq = (
        6 * Fraction(1, 36)
        + 3 * Fraction(16, 36)
        + Fraction(36, 36)
        + 3 * Fraction(4, 36)
        + 2 * Fraction(9, 36)
    )
    k2_over_k1 = tr_t3_sq / tr_y_sq

    max_mod_err = max(modular_rel_errs.values())
    max_heis_err = max(heisenberg_errs.values())
    e1_passed = bool(
        max_mod_err < 10 ** (-54)
        and max_heis_err < 10 ** (-54)
        and gauss_crt_err < 10 ** (-54)
        and p_unit_err == 0
        and crt_t_err < 10 ** (-54)
        and crt_s_err < 10 ** (-54)
        and c5_inv_err < 10 ** (-54)
        and dim_3c == 3
        and dim_2w == 2
        and good_sp2_zero
        and bad_sp2_list == [[4, 3], [-3, -2]]
        and pc_doubled_shear_heis_defect > 2
        and anom_factor_exact
        and k2_over_k1 == Fraction(3, 5)
    )

    return {
        "E1_RepairedWeilMetaplectic_and_CRT_Gate_passed": e1_passed,
        "nonprojective_modular_relation_frob_errs_65dps": modular_rel_errs,
        "unit_shear_heisenberg_conjugation_frob_errs_65dps": heisenberg_errs,
        "gauss_sum_crt_reciprocity_err_65dps": gauss_crt_err,
        "gauss_sums_re_im": {
            "gamma_15_1": [float(mp.re(g15)), float(mp.im(g15))],
            "gamma_5_3": [float(mp.re(g5)), float(mp.im(g5))],
            "gamma_3_2": [float(mp.re(g3)), float(mp.im(g3))],
        },
        "crt_T15_tensor_frob_err_65dps": crt_t_err,
        "crt_S15_tensor_frob_err_65dps": crt_s_err,
        "w5_parity_split_dims": {"dim_3c": dim_3c, "dim_2w": dim_2w, "c5_involution_err": c5_inv_err},
        "anomaly_factorization_verified": anom_factor_exact,
        "k2_over_k1_exact": str(k2_over_k1),
        "PC_CL1_DoubledShearHeisenbergDefect": {
            "noncentral_heisenberg_conjugation_frob_defect": pc_doubled_shear_heis_defect,
            "sp2_bad_st_cubed_matrix": bad_sp2_list,
        },
    }


# ============================================================================
# SECTION 2: PART 1B — GOERNER-ZICKERT-NEUMANN FLATTENED ROGERS DILOGARITHM CS
# ============================================================================

EDGES_TET: List[Tuple[int, int]] = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
FACE_VERTS: Dict[int, Tuple[int, int, int]] = {
    0: (1, 2, 3),
    1: (0, 2, 3),
    2: (0, 1, 3),
    3: (0, 1, 2),
}


def mat_inv_sl2(m_mat: Any) -> Any:
    return mp.matrix([[m_mat[1, 1], -m_mat[0, 1]], [-m_mat[1, 0], m_mat[0, 0]]])


def det2_spinors(u_vec: Any, w_vec: Any) -> Any:
    return u_vec[0, 0] * w_vec[1, 0] - u_vec[1, 0] * w_vec[0, 0]


def zickert_extended_rogers_mp(c01: Any, c02: Any, c03: Any, c12: Any, c13: Any, c23: Any) -> Tuple[Any, int, int, Any]:
    """
    Evaluates Zickert's (Duke Math. J. 150:489-532, 2009) / Neumann's (GT 8:413-474, 2004)
    flattened extended Rogers dilogarithm R(z; p, q) directly from Plucker-compatible edge coordinates
    c_{03} c_{12} + c_{01} c_{23} = c_{02} c_{13}, with ZERO hand-chosen flattening integers.
    Returns (z, p, q, R_val) where Im(sum eps_k R_k) = Vol(M) and Re(sum eps_k R_k)/(2 pi^2) = CS(M) mod 1/2.
    """
    plucker_err = abs(c03 * c12 + c01 * c23 - c02 * c13)
    assert plucker_err < mp.mpf(10) ** (-42), f"Plucker violation: {plucker_err}"
    z = (c03 * c12) / (c02 * c13)
    omz = (c01 * c23) / (c02 * c13)
    l01, l02, l03 = mp.log(c01), mp.log(c02), mp.log(c03)
    l12, l13, l23 = mp.log(c12), mp.log(c13), mp.log(c23)
    lz, lomz = mp.log(z), mp.log(omz)

    p_complex = (l03 + l12 - l02 - l13 - lz) / (mp.pi * mp.mpc(0, 1))
    q_complex = (l02 + l13 - l01 - l23 + lomz) / (mp.pi * mp.mpc(0, 1))
    p_int = int(mp.nint(mp.re(p_complex)))
    q_int = int(mp.nint(mp.re(q_complex)))
    assert abs(p_complex - p_int) < mp.mpf(10) ** (-40)
    assert abs(q_complex - q_int) < mp.mpf(10) ** (-40)

    r_val = (
        mp.polylog(2, z)
        + (mp.mpf(1) / mp.mpf(2)) * lz * lomz
        + (mp.pi * mp.mpc(0, 1) / mp.mpf(2)) * (q_int * lz + p_int * lomz)
        - (mp.pi ** 2) / mp.mpf(6)
    )
    return z, p_int, q_int, r_val


def goerner_canonical_lift(s0: int, s1: int, s2: int, s3: int) -> Dict[Tuple[int, int], int]:
    """Goerner (GT 19:245-286, 2015, Def. 2.7) canonical PSL(2,C)->SL(2,C) obstruction lift on a 3-simplex."""
    assert s0 * s1 * s2 * s3 == 1
    return {(0, 1): 1, (0, 2): 1, (0, 3): 1, (1, 2): s3, (1, 3): s2, (2, 3): s1}


def wrap_half_mp(val: Any) -> Any:
    half = mp.mpf(1) / mp.mpf(2)
    return val - mp.nint(val / half) * half


def bloch_wigner_conj_tautology_diff(z_val: Any) -> Any:
    """Demonstrates Codex Item B finding: D(z) + D(conj(z)) == 0 identically for ANY z in C!"""
    def d_bw(w: Any) -> Any:
        return mp.im(mp.polylog(2, w)) + mp.arg(1 - w) * mp.log(abs(w))
    return abs(d_bw(z_val) + d_bw(mp.conj(z_val)))


def solve_bundle_parabolic_seed_mp(vr: Fraction, vi: Fraction, wr: Fraction, wi: Fraction) -> Dict[str, Any]:
    t_mat = mp.matrix([[1, 1], [0, 1]])
    t_inv = mat_inv_sl2(t_mat)

    def eval_res(v_val: Any, w_val: Any) -> Tuple[Any, Any, Any, Any]:
        b_mat = mp.matrix([[1 + v_val * w_val, w_val], [v_val, 1]])
        b_inv = mat_inv_sl2(b_mat)
        a_mat = b_inv * t_mat * b_mat * t_inv
        diff = (t_mat * a_mat * t_inv) - (a_mat * b_mat * a_mat)
        return diff[0, 1], diff[1, 0] / v_val, a_mat, b_mat

    v = mp.mpc(mp.mpf(vr.numerator) / mp.mpf(vr.denominator), mp.mpf(vi.numerator) / mp.mpf(vi.denominator))
    w = mp.mpc(mp.mpf(wr.numerator) / mp.mpf(wr.denominator), mp.mpf(wi.numerator) / mp.mpf(wi.denominator))
    eps = mp.mpf(10) ** (-24)
    tol = mp.mpf(10) ** (-50)
    for _ in range(40):
        f1, f2, _, _ = eval_res(v, w)
        if abs(f1) + abs(f2) < tol:
            break
        f1_v, f2_v, _, _ = eval_res(v + eps, w)
        f1_w, f2_w, _, _ = eval_res(v, w + eps)
        j11, j21 = (f1_v - f1) / eps, (f2_v - f2) / eps
        j12, j22 = (f1_w - f1) / eps, (f2_w - f2) / eps
        det_j = j11 * j22 - j12 * j21
        v -= (j22 * f1 - j12 * f2) / det_j
        w -= (-j21 * f1 + j11 * f2) / det_j
    _, _, a_sol, b_sol = eval_res(v, w)
    k_mat = a_sol * b_sol * mat_inv_sl2(a_sol) * mat_inv_sl2(b_sol)
    return {"A": a_sol, "B": b_sol, "T_plus": t_mat, "K": k_mat}


def eval_punctured_torus_word_zickert(a_mat: Any, b_mat: Any, moves: List[str]) -> Tuple[Any, Any, Any, List[Any]]:
    """
    Evaluates Zickert's extended Rogers dilogarithm on the canonical layered ideal triangulation
    of a once-punctured torus bundle given by an elementary Nielsen word in {R, Ri, L, Li}.
    """
    v_inf = mp.matrix([[1], [0]])
    x, y = a_mat, b_mat
    tot = mp.mpc(0)
    shapes: List[Any] = []
    for mv in moves:
        if mv == "R":
            tri = (x, x * y, x * y * x)
            sgn = 1
            x, y = x, y * x
        elif mv == "Ri":
            yn = y * mat_inv_sl2(x)
            tri = (x, x * yn, x * yn * x)
            sgn = -1
            x, y = x, yn
        elif mv == "L":
            tri = (y, y * x, y * x * y)
            sgn = -1
            x, y = x * y, y
        elif mv == "Li":
            xn = x * mat_inv_sl2(y)
            tri = (y, y * xn, y * xn * y)
            sgn = 1
            x, y = xn, y
        else:
            raise ValueError(mv)
        u0 = v_inf
        u1, u2, u3 = tri[0] * v_inf, tri[1] * v_inf, tri[2] * v_inf
        c01, c02, c03 = det2_spinors(u0, u1), det2_spinors(u0, u2), det2_spinors(u0, u3)
        c12, c13, c23 = det2_spinors(u1, u2), det2_spinors(u1, u3), det2_spinors(u2, u3)
        z_t, _, _, r_val = zickert_extended_rogers_mp(c01, c02, c03, c12, c13, c23)
        shapes.append(z_t)
        tot += sgn * r_val
    return x, y, tot, shapes


def eval_ordered_ptolemy_triangulation_mp(
    n_tet: int,
    eps_signs: Tuple[int, ...],
    face_pairs: List[Tuple[Tuple[int, int], Tuple[int, int]]],
    face_cocycle: Tuple[int, ...],
    seeds_rat: List[Tuple[Fraction, Fraction]],
) -> Dict[str, Any]:
    """
    Solves the Goerner-Zickert Ptolemy variety on an ordered ideal triangulation from rational seeds
    (ZERO float literals) and returns Vol(M), CS(M) mod 1/2, and cellular H_1(M_hat; Z) torsion check.
    """
    items = [(t, e) for t in range(n_tet) for e in EDGES_TET]
    parent = {it: it for it in items}

    def find(it: Tuple[int, Tuple[int, int]]) -> Tuple[int, Tuple[int, int]]:
        while parent[it] != it:
            parent[it] = parent[parent[it]]
            it = parent[it]
        return it

    fpid: Dict[Tuple[int, int], int] = {}
    for pid, (f1, f2) in enumerate(face_pairs):
        fpid[f1] = pid
        fpid[f2] = pid
        fv1, fv2 = FACE_VERTS[f1[1]], FACE_VERTS[f2[1]]
        for a, b in ((0, 1), (0, 2), (1, 2)):
            r1 = find((f1[0], (fv1[a], fv1[b])))
            r2 = find((f2[0], (fv2[a], fv2[b])))
            if r1 != r2:
                parent[r1] = r2

    roots = sorted(set(find(it) for it in items))
    assert len(roots) == n_tet
    rmap = {r: idx for idx, r in enumerate(roots)}

    u_tet = {
        t: goerner_canonical_lift(*(face_cocycle[fpid[(t, k)]] for k in range(4)))
        for t in range(n_tet)
    }

    def eval_ptol(free_vars: List[Any]) -> List[Any]:
        vals = [mp.mpc(1)] + list(free_vars)
        out = []
        for t in range(n_tet):
            ut = u_tet[t]
            cs = [ut[e] * vals[rmap[find((t, e))]] for e in EDGES_TET]
            out.append(cs[2] * cs[3] + cs[0] * cs[5] - cs[1] * cs[4])
        return out

    vec = [
        mp.mpc(mp.mpf(sr.numerator) / mp.mpf(sr.denominator), mp.mpf(si.numerator) / mp.mpf(si.denominator))
        for sr, si in seeds_rat
    ]
    n_var = len(vec)
    h_step = mp.mpf(10) ** (-24)
    tol = mp.mpf(10) ** (-48)
    for _ in range(40):
        f0 = eval_ptol(vec)
        if sum(abs(f0[i]) for i in range(n_var)) < tol:
            break
        jac = mp.zeros(n_var, n_var)
        for j in range(n_var):
            vp = list(vec)
            vp[j] += h_step
            fp = eval_ptol(vp)
            for i in range(n_var):
                jac[i, j] = (fp[i] - f0[i]) / h_step
        delta = (jac ** (-1)) * mp.matrix([f0[i] for i in range(n_var)])
        for j in range(n_var):
            vec[j] -= delta[j, 0]

    res_all = eval_ptol(vec)
    max_ptol_err = max(abs(v) for v in res_all)
    vals_sol = [mp.mpc(1)] + vec
    tot = mp.mpc(0)
    shapes: List[Any] = []
    for t in range(n_tet):
        ut = u_tet[t]
        cs = [ut[e] * vals_sol[rmap[find((t, e))]] for e in EDGES_TET]
        z_t, _, _, rv = zickert_extended_rogers_mp(*cs)
        shapes.append(z_t)
        tot += eps_signs[t] * rv

    vol_mp = mp.im(tot)
    cs_raw_mp = mp.re(tot) / (2 * (mp.pi ** 2))
    cs_mod_half_mp = wrap_half_mp(cs_raw_mp)
    return {
        "vol_mp": vol_mp,
        "cs_mod_half_mp": cs_mod_half_mp,
        "max_ptolemy_residual": float(max_ptol_err),
        "shapes": shapes,
    }


def check_m015_published_snappy_benchmark(cs_m015_mp: Any) -> Dict[str, Any]:
    """
    AST-isolated topology benchmark check against Marc Culler & Nathan Dunfield's published
    SnapPy documentation value Manifold('m015').chern_simons() == -0.15320413 (8 significant figures).
    """
    snappy_published_m015_cs = -0.15320413
    abs_err = float(abs(cs_m015_mp - mp.mpf(str(snappy_published_m015_cs))))
    return {
        "published_snappy_m015_cs": snappy_published_m015_cs,
        "computed_zickert_m015_cs": float(cs_m015_mp),
        "abs_diff_vs_published_8fig": abs_err,
        "benchmark_8fig_passed": abs_err < 5.0e-9,
    }


def run_part_1b_zickert_rogers_cs_and_theta_scoping() -> Dict[str, Any]:
    with mp.workdps(60):
        # 1. Punctured-torus bundle Zickert spinor evaluation on m004 (+LR) vs chiral sister m003 (-LR):
        sol = solve_bundle_parabolic_seed_mp(Fraction(1, 2), Fraction(4, 5), Fraction(-1, 1), Fraction(4, 5))
        a_mat, b_mat, t_plus = sol["A"], sol["B"], sol["T_plus"]

        # Topological H_1 torsion orders |det(M - I_2)| = 1 (m004) vs |det(-M - I_2)| = 5 (m003):
        m_plus = sp.Matrix([[2, 1], [1, 1]])
        m_minus = -m_plus
        h1_tor_m004 = abs(int((m_plus - sp.eye(2)).det()))
        h1_tor_m003 = abs(int((m_minus - sp.eye(2)).det()))

        x4, y4, tot_m004_bundle, shapes_m004 = eval_punctured_torus_word_zickert(a_mat, b_mat, ["R", "L"])
        x3, y3, tot_m003_bundle, shapes_m003 = eval_punctured_torus_word_zickert(
            a_mat, b_mat, ["L", "Ri", "L", "Ri", "L", "L"]
        )
        mu_3 = (x3[0, 0] - a_mat[0, 0]) / a_mat[1, 0]
        t_minus = mp.matrix([[1, mu_3], [0, 1]])
        m004_conj_err = float(
            mp.mnorm(t_plus * a_mat * mat_inv_sl2(t_plus) - x4, "F")
            + mp.mnorm(t_plus * b_mat * mat_inv_sl2(t_plus) - y4, "F")
        )
        m003_conj_err = float(
            mp.mnorm(t_minus * a_mat * mat_inv_sl2(t_minus) - x3, "F")
            + mp.mnorm(t_minus * b_mat * mat_inv_sl2(t_minus) - y3, "F")
        )

        vol_m004_b = mp.im(tot_m004_b := tot_m004_bundle)
        cs_m004_b = wrap_half_mp(mp.re(tot_m004_b) / (2 * (mp.pi ** 2)))
        vol_m003_b = mp.im(tot_m003_b := tot_m003_bundle)
        cs_m003_b = wrap_half_mp(mp.re(tot_m003_b) / (2 * (mp.pi ** 2)))

        # 2. Independent ordered Goerner-Zickert Ptolemy triangulation of m004 (checking both coboundary-equivalent cocycles!):
        pairs_m004 = [((0, 0), (1, 2)), ((0, 2), (1, 0)), ((1, 1), (0, 3)), ((1, 3), (0, 1))]
        ptol_m004_a = eval_ordered_ptolemy_triangulation_mp(
            2, (1, -1), pairs_m004, (1, -1, -1, 1), [(Fraction(1, 2), Fraction(4, 5))]
        )
        ptol_m004_b = eval_ordered_ptolemy_triangulation_mp(
            2, (1, -1), pairs_m004, (-1, 1, 1, -1), [(Fraction(-1, 2), Fraction(4, 5))]
        )
        coboundary_inv_m004 = float(abs(ptol_m004_a["cs_mod_half_mp"] - ptol_m004_b["cs_mod_half_mp"]))

        # 3. Ordered 3-tetrahedron Goerner-Zickert Ptolemy triangulation of chiral 5_2 knot complement m015:
        pairs_m015 = [
            ((0, 0), (1, 1)),
            ((0, 2), (2, 1)),
            ((1, 0), (2, 3)),
            ((1, 2), (0, 1)),
            ((2, 0), (0, 3)),
            ((2, 2), (1, 3)),
        ]
        ptol_m015 = eval_ordered_ptolemy_triangulation_mp(
            3,
            (1, 1, 1),
            pairs_m015,
            (-1, 1, 1, -1, 1, 1),
            [(Fraction(2, 3), Fraction(3, 5)), (Fraction(1, 8), Fraction(3, 4))],
        )
        bench_m015 = check_m015_published_snappy_benchmark(ptol_m015["cs_mod_half_mp"])
        twelfth = mp.mpf(1) / mp.mpf(12)
        m015_dist_from_rational_twelfths = float(
            abs(ptol_m015["cs_mod_half_mp"] - mp.nint(ptol_m015["cs_mod_half_mp"] / twelfth) * twelfth)
        )

        # 4. Planted Control PC_CL1_BlochWignerConjugateTautologyControl:
        # Show D(z) + D(conj(z)) == 0 vanishes even on chiral m003 and chiral m015 shapes!
        bw_tautology_on_m003 = float(sum(bloch_wigner_conj_tautology_diff(z) for z in shapes_m003))
        bw_tautology_on_m015 = float(sum(bloch_wigner_conj_tautology_diff(z) for z in ptol_m015["shapes"]))

        # 5. Explicit Tier-II Scoping of 7D -> 4D Physical YM Theta (Item B):
        # Geometric KK Chern-Simons shift Delta_theta_CS = 2 * pi * CS(m004) vanishes to 55+ digits,
        # while bare parity-allowed 4D/7D discrete branch theta_bare in {0, pi} is NOT erased without
        # a parent-action exclusion of the bare pi branch!
        delta_theta_cs_m004 = 2 * mp.pi * ptol_m004_a["cs_mod_half_mp"]
        pc_bare_pi_branch_theta_rad = float(abs(mp.pi + delta_theta_cs_m004))

        vol_diff_m004_m003 = float(abs(vol_m004_b - vol_m003_b))
        vol_diff_bundle_vs_ptol_m004 = float(abs(vol_m004_b - ptol_m004_a["vol_mp"]))
        cs_m004_abs = float(max(abs(cs_m004_b), abs(ptol_m004_a["cs_mod_half_mp"])))
        cs_m003_quarter_err = float(abs(abs(cs_m003_b) - mp.mpf(1) / mp.mpf(4)))

    e2_passed = bool(
        h1_tor_m004 == 1
        and h1_tor_m003 == 5
        and m004_conj_err < 10 ** (-54)
        and m003_conj_err < 10 ** (-54)
        and vol_diff_m004_m003 < 10 ** (-54)
        and vol_diff_bundle_vs_ptol_m004 < 10 ** (-54)
        and cs_m004_abs < 10 ** (-54)
        and coboundary_inv_m004 < 10 ** (-54)
        and cs_m003_quarter_err < 10 ** (-54)
        and bench_m015["benchmark_8fig_passed"]
        and m015_dist_from_rational_twelfths > Fraction(1, 100)
        and bw_tautology_on_m003 < 10 ** (-54)
        and bw_tautology_on_m015 < 10 ** (-54)
        and pc_bare_pi_branch_theta_rad > 3
    )

    return {
        "E2_ZickertRogersCS_and_ThetaScoping_Gate_passed": e2_passed,
        "amphichiral_m004_zickert_audit": {
            "h1_torsion_order": h1_tor_m004,
            "monodromy_conjugation_err_60dps": m004_conj_err,
            "vol_m004": float(vol_m004_b),
            "bundle_vs_ordered_ptolemy_vol_diff": vol_diff_bundle_vs_ptol_m004,
            "cs_mod_half_max_abs_60dps": cs_m004_abs,
            "goerner_coboundary_invariance_err_60dps": coboundary_inv_m004,
        },
        "chiral_sister_m003_equal_volume_control": {
            "h1_torsion_order": h1_tor_m003,
            "monodromy_conjugation_err_60dps": m003_conj_err,
            "vol_m003": float(vol_m003_b),
            "vol_m004_minus_vol_m003_abs_60dps": vol_diff_m004_m003,
            "cs_m003_mod_half": float(cs_m003_b),
            "abs_cs_minus_one_quarter_err_60dps": cs_m003_quarter_err,
        },
        "chiral_5_2_knot_m015_irrational_control": {
            "vol_m015": float(ptol_m015["vol_mp"]),
            "max_ptolemy_residual": ptol_m015["max_ptolemy_residual"],
            "snappy_benchmark_audit": bench_m015,
            "min_distance_to_any_twelfth_lattice": m015_dist_from_rational_twelfths,
        },
        "PC_CL1_BlochWignerConjugateTautologyControl": {
            "tautological_D_plus_Dconj_on_chiral_m003": bw_tautology_on_m003,
            "tautological_D_plus_Dconj_on_chiral_m015": bw_tautology_on_m015,
        },
        "explicit_tier_II_theta_branch_scoping": {
            "geometric_kk_delta_theta_cs_m004_rad": float(abs(delta_theta_cs_m004)),
            "PC_CL1_BareParityPiBranchUnselectedWithoutParentMap_rad": pc_bare_pi_branch_theta_rad,
            "scoped_statement": (
                "Zickert-Rogers flattened dilogarithm proves CS(m004) = 0 mod 1/2 (unlike chiral m003 = 1/4 and m015 = -0.15320413...), "
                "vanishing the geometric 3D CS shift Delta_theta_CS = 0; exclusion of an independent bare parity-allowed theta_bare = pi "
                "branch remains an explicit Tier-II parent-action premise rather than an unconditional assignment."
            ),
        },
    }


def main() -> None:
    ast_check = verify_ast_closure1()
    part_1a = run_part_1a_repaired_weil_and_crt()
    part_1b = run_part_1b_zickert_rogers_cs_and_theta_scoping()

    controls_passed = bool(
        ast_check["Gate_AST_Stage1_Closure_Passed"]
        and part_1a["PC_CL1_DoubledShearHeisenbergDefect"]["noncentral_heisenberg_conjugation_frob_defect"] > 2
        and part_1b["chiral_sister_m003_equal_volume_control"]["abs_cs_minus_one_quarter_err_60dps"] < 10 ** (-54)
        and part_1b["chiral_5_2_knot_m015_irrational_control"]["min_distance_to_any_twelfth_lattice"] > Fraction(1, 100)
        and part_1b["PC_CL1_BlochWignerConjugateTautologyControl"]["tautological_D_plus_Dconj_on_chiral_m003"] < 10 ** (-54)
        and part_1b["explicit_tier_II_theta_branch_scoping"]["PC_CL1_BareParityPiBranchUnselectedWithoutParentMap_rad"] > 3
    )

    stage_1_passed = bool(
        controls_passed
        and part_1a["E1_RepairedWeilMetaplectic_and_CRT_Gate_passed"]
        and part_1b["E2_ZickertRogersCS_and_ThetaScoping_Gate_passed"]
    )

    out_payload: Dict[str, Any] = {
        "card": "X-CLOSURE-1",
        "empirical_firewall": "0 of 19",
        "ast_source_check": ast_check,
        "part_1a_repaired_weil_metaplectic_and_crt": part_1a,
        "part_1b_zickert_rogers_cs_and_theta_scoping": part_1b,
        "all_planted_controls_passed": controls_passed,
        "stage_1_gate_passed": stage_1_passed,
    }

    out_dir = Path(__file__).resolve().parent
    out_json = out_dir / "verify_x_closure_1_out.json"
    out_json.write_text(json.dumps(out_payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    sha = hashlib.sha256(out_json.read_bytes()).hexdigest()
    (out_dir / "OUTPUT_SHA256.txt").write_text(f"{sha}  verify_x_closure_1_out.json\n", encoding="utf-8")


if __name__ == "__main__":
    main()
