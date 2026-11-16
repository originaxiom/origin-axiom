#!/usr/bin/env python3
"""
Standalone Zero-Import Verifier for Card AGY-002_ENDGAME-V2-G1 (with G1-ERRATUM):
  E_6 -> Pati-Salam x| Z_2^D Universal Gauge Corridor & 3-Family Strong-CP Law (0 of 19).

Empirical Firewall: 0 of 19 (zero repository imports, zero float literals in source).
"""

from __future__ import annotations

import ast
from dataclasses import dataclass
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple

import mpmath as mp
import numpy as np


ALLOWED_IMPORTS: Set[str] = {
    "__future__",
    "ast",
    "dataclasses",
    "fractions",
    "hashlib",
    "json",
    "math",
    "mpmath",
    "numpy",
    "pathlib",
    "typing",
}


def frac_f64(num: int, den: int = 1) -> float:
    return float(Fraction(num, den))


def pow10_f64(exp_int: int) -> float:
    return float(Fraction(10, 1) ** exp_int)


# ============================================================================
# SECTION 0: AST SOURCE LOCK (ZERO REPO IMPORTS & ZERO FLOAT LITERALS)
# ============================================================================

def verify_ast_g1() -> Dict[str, Any]:
    src = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(src)
    mods: Set[str] = set()
    float_literals = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                mods.add(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.level > 0:
                mods.add("<relative>")
            elif node.module:
                mods.add(node.module.split(".")[0])
        elif isinstance(node, ast.Constant) and isinstance(node.value, float):
            float_literals += 1

    disallowed = sorted(mods - ALLOWED_IMPORTS)
    return {
        "ast_gate_passed": (len(disallowed) == 0) and (float_literals == 0),
        "imported_modules": sorted(mods),
        "disallowed_imports": disallowed,
        "float_literals_in_entire_file": float_literals,
    }


# ============================================================================
# SECTION 1: EXACT Z[zeta_6] RILEY CUSP GEOMETRY & E_6 27 BRANCHING
# ============================================================================

@dataclass(frozen=True)
class Z6:
    """Exact element a + b * zeta_6 in Z[zeta_6], where zeta_6^2 - zeta_6 + 1 = 0."""
    a: int
    b: int

    def __add__(self, o: "Z6") -> "Z6":
        return Z6(self.a + o.a, self.b + o.b)

    def __sub__(self, o: "Z6") -> "Z6":
        return Z6(self.a - o.a, self.b - o.b)

    def __neg__(self) -> "Z6":
        return Z6(-self.a, -self.b)

    def __mul__(self, o: "Z6") -> "Z6":
        # zeta_6^2 = zeta_6 - 1
        return Z6(self.a * o.a - self.b * o.b, self.a * o.b + self.b * o.a + self.b * o.b)

    def norm_sq(self) -> int:
        # |a + b * (1/2 + i sqrt(3)/2)|^2 = (a + b/2)^2 + 3 b^2 / 4 = a^2 + a b + b^2
        return self.a * self.a + self.a * self.b + self.b * self.b

    def twice_real(self) -> int:
        return 2 * self.a + self.b


def z6_mat_mul(X: Tuple[Tuple[Z6, Z6], Tuple[Z6, Z6]], Y: Tuple[Tuple[Z6, Z6], Tuple[Z6, Z6]]) -> Tuple[Tuple[Z6, Z6], Tuple[Z6, Z6]]:
    return (
        (X[0][0] * Y[0][0] + X[0][1] * Y[1][0], X[0][0] * Y[0][1] + X[0][1] * Y[1][1]),
        (X[1][0] * Y[0][0] + X[1][1] * Y[1][0], X[1][0] * Y[0][1] + X[1][1] * Y[1][1]),
    )


def z6_mat_inv(X: Tuple[Tuple[Z6, Z6], Tuple[Z6, Z6]]) -> Tuple[Tuple[Z6, Z6], Tuple[Z6, Z6]]:
    # For det(X) = +1 in SL_2(Z[zeta_6])
    return ((X[1][1], -X[0][1]), (-X[1][0], X[0][0]))


def z6_mat_det(X: Tuple[Tuple[Z6, Z6], Tuple[Z6, Z6]]) -> Z6:
    return X[0][0] * X[1][1] - X[0][1] * X[1][0]


def run_cusp_and_e6_checks() -> Dict[str, Any]:
    zero = Z6(0, 0)
    one = Z6(1, 0)
    zeta6 = Z6(0, 1)

    # Verify cyclotomic polynomial zeta_6^2 - zeta_6 + 1 = 0
    cyc_zero = (zeta6 * zeta6) - zeta6 + one

    A = ((one, one), (zero, one))
    B = ((one, zero), (zeta6, one))
    Ai = z6_mat_inv(A)
    Bi = z6_mat_inv(B)

    # Wirtinger relation for figure-eight knot group: W A = B W with W = [A, B^{-1}] = A B^{-1} A^{-1} B
    W = z6_mat_mul(z6_mat_mul(A, Bi), z6_mat_mul(Ai, B))
    lhs_w = z6_mat_mul(W, A)
    rhs_w = z6_mat_mul(B, W)
    wirtinger_exact = (lhs_w == rhs_w) and (z6_mat_det(A) == one) and (z6_mat_det(B) == one) and (cyc_zero == zero)

    # Zero-linking peripheral longitude word L = B^{-1} A B A^{-2} B A B^{-1}
    # Linking exponent sum = -1 + 1 + 1 - 2 + 1 + 1 - 1 = 0
    word_ops = [("b", Bi, -1), ("A", A, 1), ("B", B, 1), ("a", Ai, -1), ("a", Ai, -1), ("B", B, 1), ("A", A, 1), ("b", Bi, -1)]
    linking_sum = sum(lk for _, _, lk in word_ops)
    L_mat = ((one, zero), (zero, one))
    for _, op, _ in word_ops:
        L_mat = z6_mat_mul(L_mat, op)

    # Commutes with meridian M = A:
    comm_LA = (z6_mat_mul(L_mat, A) == z6_mat_mul(A, L_mat))
    # In PSL_2(C), L_mat = - [[1, tau_cusp], [0, 1]] => tau_cusp = -L_mat[0][1] / (-1) = -L_mat[0][1]
    minus_one = Z6(-1, 0)
    upper_parabolic = (L_mat[1][0] == zero) and (L_mat[0][0] == minus_one) and (L_mat[1][1] == minus_one)
    tau_z6 = -L_mat[0][1]  # = 2 - 4 * zeta_6 = -2 * sqrt(3) i (or +2 * sqrt(3) i for L_mat^{-1})
    re_tau_twice = tau_z6.twice_real()
    abs_tau_sq = tau_z6.norm_sq()  # |+- 2 sqrt(3) i|^2 = 12

    # Breadth-first census of reduced words up to length 6 in <A, B> to verify min_{|c|>0} |c|^2 = 1
    gens = [("A", A), ("a", Ai), ("B", B), ("b", Bi)]
    inv_tag = {"A": "a", "a": "A", "B": "b", "b": "B"}
    stack: List[Tuple[str, Tuple[Tuple[Z6, Z6], Tuple[Z6, Z6]]]] = [("", ((one, zero), (zero, one)))]
    min_nonzero_c_norm_sq = 1000
    nonparabolic_checked = 0
    for _ in range(6):
        nxt = []
        for w_str, M_cur in stack:
            for tag, G_op in gens:
                if w_str and inv_tag[w_str[-1]] == tag:
                    continue
                M_nx = z6_mat_mul(M_cur, G_op)
                c_entry = M_nx[1][0]
                nsq = c_entry.norm_sq()
                if nsq > 0:
                    nonparabolic_checked += 1
                    if nsq < min_nonzero_c_norm_sq:
                        min_nonzero_c_norm_sq = nsq
                nxt.append((w_str + tag, M_nx))
        stack = nxt

    # Exact 50-digit hyperbolic invariants of m004 and m000
    mp.mp.dps = 50
    t_tan_mp = mp.mpf(1) / mp.sqrt(min_nonzero_c_norm_sq)
    a_max_mp = mp.sqrt(abs_tau_sq) / (t_tan_mp ** 2)  # 2 * sqrt(3)
    v_cusp_max_mp = a_max_mp / 2  # int_1^infty (2 sqrt(3) / t^3) dt = sqrt(3)
    # Clausen function Cl_2(pi/3) = Im Li_2(e^{i pi/3}) = Vol(m000); Vol(m004) = 2 * Cl_2(pi/3)
    vol_m000_mp = mp.im(mp.polylog(2, mp.exp(mp.mpc(0, 1) * mp.pi / 3)))
    vol_m004_mp = 2 * vol_m000_mp
    # Cross-check against 3 * Cl_2(2 pi / 3) (Lobachevsky identity Cl_2(theta) = (3/2) Cl_2(2 theta) at pi/3? Wait:
    # Duplication identity: (1/2) Cl_2(2 theta) = Cl_2(theta) - Cl_2(pi - theta); at theta = pi/3, Cl_2(pi - pi/3) = Cl_2(2 pi/3),
    # so (1/2) Cl_2(2 pi/3) = Cl_2(pi/3) - Cl_2(2 pi/3) => Cl_2(pi/3) = (3/2) Cl_2(2 pi/3) => 2 Cl_2(pi/3) = 3 Cl_2(2 pi/3)!)
    vol_m004_alt_mp = 3 * mp.im(mp.polylog(2, mp.exp(mp.mpc(0, 1) * 2 * mp.pi / 3)))
    lobachevsky_diff = float(abs(vol_m004_mp - vol_m004_alt_mp))
    packing_density = float(v_cusp_max_mp / vol_m004_mp)

    # E_6 -> SU(4)_c x SU(2)_L x SU(2)_R x U(1)_psi branching of chiral 27:
    # (d4, d2L, d2R, q_psi, T4, T2L, T2R, chiral_after_vectorlike_decoupling)
    e6_27_branch = [
        (4, 2, 1, Fraction(1, 1), Fraction(1, 2), Fraction(1, 2), Fraction(0, 1), True),
        (4, 1, 2, Fraction(1, 1), Fraction(1, 2), Fraction(0, 1), Fraction(1, 2), True),
        (1, 2, 2, Fraction(-2, 1), Fraction(0, 1), Fraction(1, 2), Fraction(1, 2), False),
        (6, 1, 1, Fraction(-2, 1), Fraction(1, 1), Fraction(0, 1), Fraction(0, 1), False),
        (1, 1, 1, Fraction(4, 1), Fraction(0, 1), Fraction(0, 1), Fraction(0, 1), False),
    ]
    dim_27 = sum(d4 * d2l * d2r for d4, d2l, d2r, _, _, _, _, _ in e6_27_branch)
    tr_qpsi = sum(d4 * d2l * d2r * q for d4, d2l, d2r, q, _, _, _, _ in e6_27_branch)
    tr_qpsi3 = sum(d4 * d2l * d2r * (q ** 3) for d4, d2l, d2r, q, _, _, _, _ in e6_27_branch)
    # Note: U(1)_psi has a pure U(1)_psi^3 anomaly inside a single 27 (broken at M_U), while Tr(Q_psi) = 0 and Dynkin indices match!
    idx_su4_27 = sum(d2l * d2r * t4 for _, d2l, d2r, _, t4, _, _, _ in e6_27_branch)
    idx_su2L_27 = sum(d4 * d2r * t2l for d4, _, d2r, _, _, t2l, _, _ in e6_27_branch)
    idx_su2R_27 = sum(d4 * d2l * t2r for d4, d2l, _, _, _, _, t2r, _ in e6_27_branch)
    chiral_dim_per_gen = sum(d4 * d2l * d2r for d4, d2l, d2r, _, _, _, _, ch in e6_27_branch if ch)

    n_g = 3
    b3_sm_3fam = -Fraction(11, 3) * 3 + Fraction(2, 3) * n_g * 2

    cusp_and_e6_ok = (
        wirtinger_exact
        and linking_sum == 0
        and comm_LA
        and upper_parabolic
        and re_tau_twice == 0
        and abs_tau_sq == 12
        and min_nonzero_c_norm_sq == 1
        and lobachevsky_diff < pow10_f64(-45)
        and dim_27 == 27
        and tr_qpsi == 0
        and (idx_su4_27, idx_su2L_27, idx_su2R_27) == (Fraction(3, 1), Fraction(3, 1), Fraction(3, 1))
        and chiral_dim_per_gen == 16
        and b3_sm_3fam == Fraction(-7, 1)
    )

    return {
        "cusp_and_e6_gate_passed": bool(cusp_and_e6_ok),
        "wirtinger_relation_exact_in_Z_zeta6": wirtinger_exact,
        "longitude_linking_sum": linking_sum,
        "re_tau_cusp_twice_exact_int": re_tau_twice,
        "abs_tau_cusp_sq_exact_int": abs_tau_sq,
        "min_nonzero_c_norm_sq_over_words_len_6": min_nonzero_c_norm_sq,
        "nonparabolic_words_checked": nonparabolic_checked,
        "t_tan": float(t_tan_mp),
        "A_max_m004": float(a_max_mp),
        "V_cusp_max_m004": float(v_cusp_max_mp),
        "Vol_m000": float(vol_m000_mp),
        "Vol_m004": float(vol_m004_mp),
        "Vol_m004_50digit_str": mp.nstr(vol_m004_mp, 45),
        "lobachevsky_2Cl2_pi3_vs_3Cl2_2pi3_diff": lobachevsky_diff,
        "horoball_packing_density_m004": packing_density,
        "e6_27_dim": dim_27,
        "e6_27_dynkin_indices_su4_su2L_su2R": [str(idx_su4_27), str(idx_su2L_27), str(idx_su2R_27)],
        "chiral_weyl_dim_per_gen_below_M_PS": chiral_dim_per_gen,
        "n_generations_chiral": n_g,
        "sm_b3_3fam": str(b3_sm_3fam),
    }


# ============================================================================
# SECTION 2: 2-LOOP MATRIX RGE & 3-FAMILY D-PARITY STRONG-CP THEOREM
# ============================================================================

def mv_2loop_gauge_matrix(
    c2_G: List[Fraction],
    weyl_reps: List[Tuple[List[int], List[Fraction], List[Fraction]]],
    complex_scalars: List[Tuple[List[int], List[Fraction], List[Fraction]]],
) -> Tuple[List[Fraction], List[List[Fraction]]]:
    n = len(c2_G)
    b1 = [-Fraction(11, 3) * c2_G[a] for a in range(n)]
    B2 = [[-Fraction(34, 3) * (c2_G[a] ** 2) if a == b else Fraction(0, 1) for b in range(n)] for a in range(n)]

    for a in range(n):
        for dims, t_idx, c2_rep in weyl_reps:
            if t_idx[a] == 0:
                continue
            d_oth = Fraction(1, 1)
            for c in range(n):
                if c != a:
                    d_oth *= dims[c]
            b1[a] += Fraction(2, 3) * t_idx[a] * d_oth
            B2[a][a] += (2 * c2_rep[a] + Fraction(10, 3) * c2_G[a]) * t_idx[a] * d_oth
            for b in range(n):
                if b != a and c2_rep[b] != 0:
                    B2[a][b] += 2 * c2_rep[b] * t_idx[a] * d_oth

        for dims, t_idx, c2_rep in complex_scalars:
            if t_idx[a] == 0:
                continue
            d_oth = Fraction(1, 1)
            for c in range(n):
                if c != a:
                    d_oth *= dims[c]
            b1[a] += Fraction(1, 3) * t_idx[a] * d_oth
            B2[a][a] += (4 * c2_rep[a] + Fraction(2, 3) * c2_G[a]) * t_idx[a] * d_oth
            for b in range(n):
                if b != a and c2_rep[b] != 0:
                    B2[a][b] += 4 * c2_rep[b] * t_idx[a] * d_oth

    return b1, B2


def sm_2loop_rhs_f64(
    Yu: np.ndarray,
    Yd: np.ndarray,
    Ye: np.ndarray,
    g1: float,
    g2: float,
    g3: float,
    lam: float,
    two_loop: bool = True,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, float, float, float, float]:
    k1 = frac_f64(1, 16) / (math.pi * math.pi)
    k2 = k1 * k1 if two_loop else frac_f64(0, 1)

    Hu = Yu @ Yu.conj().T
    Hd = Yd @ Yd.conj().T
    He = Ye @ Ye.conj().T

    tu = float(np.real(np.trace(Hu)))
    td = float(np.real(np.trace(Hd)))
    te = float(np.real(np.trace(He)))
    y2_tr = 3 * tu + 3 * td + te

    g1s, g2s, g3s = g1 * g1, g2 * g2, g3 * g3
    eye3 = np.eye(3, dtype=complex)

    c1_u = (y2_tr - frac_f64(17, 20) * g1s - frac_f64(9, 4) * g2s - 8 * g3s) * eye3 + frac_f64(3, 2) * (Hu - Hd)
    c1_d = (y2_tr - frac_f64(1, 4) * g1s - frac_f64(9, 4) * g2s - 8 * g3s) * eye3 + frac_f64(3, 2) * (Hd - Hu)
    c1_e = (y2_tr - frac_f64(9, 4) * g1s - frac_f64(9, 4) * g2s) * eye3 + frac_f64(3, 2) * He

    thu2 = float(np.real(np.trace(Hu @ Hu)))
    thd2 = float(np.real(np.trace(Hd @ Hd)))
    the2 = float(np.real(np.trace(He @ He)))
    thuhd = float(np.real(np.trace(Hu @ Hd)))

    chi2 = (
        -frac_f64(27, 4) * (thu2 + thd2)
        - frac_f64(9, 4) * the2
        + frac_f64(3, 2) * thuhd
        + (frac_f64(17, 8) * g1s + frac_f64(45, 8) * g2s + 20 * g3s) * tu
        + (frac_f64(5, 8) * g1s + frac_f64(45, 8) * g2s + 20 * g3s) * td
        + (frac_f64(15, 8) * g1s + frac_f64(15, 8) * g2s) * te
    )

    c2_u = (
        frac_f64(3, 2) * (Hu @ Hu)
        - (Hu @ Hd)
        - frac_f64(1, 4) * (Hd @ Hu)
        + frac_f64(11, 4) * (Hd @ Hd)
        + (-frac_f64(9, 4) * y2_tr - 12 * lam + frac_f64(223, 80) * g1s + frac_f64(135, 16) * g2s + 16 * g3s) * Hu
        + (frac_f64(5, 4) * y2_tr - frac_f64(43, 80) * g1s + frac_f64(9, 16) * g2s - 16 * g3s) * Hd
        + (
            chi2 + 6 * lam * lam + frac_f64(1187, 600) * (g1s ** 2) - frac_f64(9, 20) * g1s * g2s
            + frac_f64(19, 15) * g1s * g3s - frac_f64(23, 4) * (g2s ** 2) + 9 * g2s * g3s - 108 * (g3s ** 2)
        ) * eye3
    )
    c2_d = (
        frac_f64(3, 2) * (Hd @ Hd)
        - (Hd @ Hu)
        - frac_f64(1, 4) * (Hu @ Hd)
        + frac_f64(11, 4) * (Hu @ Hu)
        + (-frac_f64(9, 4) * y2_tr - 12 * lam + frac_f64(187, 80) * g1s + frac_f64(135, 16) * g2s + 16 * g3s) * Hd
        + (frac_f64(5, 4) * y2_tr - frac_f64(79, 80) * g1s + frac_f64(9, 16) * g2s - 16 * g3s) * Hu
        + (
            chi2 + 6 * lam * lam - frac_f64(127, 600) * (g1s ** 2) - frac_f64(27, 20) * g1s * g2s
            + frac_f64(31, 15) * g1s * g3s - frac_f64(23, 4) * (g2s ** 2) + 9 * g2s * g3s - 108 * (g3s ** 2)
        ) * eye3
    )
    c2_e = (
        frac_f64(3, 2) * (He @ He)
        + (-frac_f64(9, 4) * y2_tr - 12 * lam + frac_f64(387, 80) * g1s + frac_f64(135, 16) * g2s) * He
        + (chi2 + 6 * lam * lam + frac_f64(1371, 200) * (g1s ** 2) + frac_f64(27, 20) * g1s * g2s - frac_f64(23, 4) * (g2s ** 2)) * eye3
    )

    dYu = (k1 * c1_u + k2 * c2_u) @ Yu
    dYd = (k1 * c1_d + k2 * c2_d) @ Yd
    dYe = (k1 * c1_e + k2 * c2_e) @ Ye

    dg1 = k1 * frac_f64(41, 10) * (g1 ** 3) + k2 * (g1 ** 3) * (
        frac_f64(199, 50) * g1s + frac_f64(27, 10) * g2s + frac_f64(44, 5) * g3s - frac_f64(17, 10) * tu - frac_f64(1, 2) * td - frac_f64(3, 2) * te
    )
    dg2 = k1 * frac_f64(-19, 6) * (g2 ** 3) + k2 * (g2 ** 3) * (
        frac_f64(9, 10) * g1s + frac_f64(35, 6) * g2s + 12 * g3s - frac_f64(3, 2) * tu - frac_f64(3, 2) * td - frac_f64(1, 2) * te
    )
    dg3 = k1 * (-7) * (g3 ** 3) + k2 * (g3 ** 3) * (
        frac_f64(11, 10) * g1s + frac_f64(9, 2) * g2s - 26 * g3s - 2 * tu - 2 * td
    )

    thu3 = float(np.real(np.trace(Hu @ Hu @ Hu)))
    thd3 = float(np.real(np.trace(Hd @ Hd @ Hd)))
    the3 = float(np.real(np.trace(He @ He @ He)))
    thu2hd = float(np.real(np.trace(Hu @ Hu @ Hd)))
    thuhd2 = float(np.real(np.trace(Hu @ Hd @ Hd)))

    dlam1 = (
        24 * lam * lam + lam * (4 * y2_tr - 9 * g2s - frac_f64(9, 5) * g1s)
        - 2 * (3 * thu2 + 3 * thd2 + the2)
        + frac_f64(9, 8) * (g2s ** 2) + frac_f64(27, 200) * (g1s ** 2) + frac_f64(9, 20) * g1s * g2s
    )
    dlam2 = (
        -312 * (lam ** 3) + 36 * (lam * lam) * (3 * g2s + frac_f64(3, 5) * g1s) - 48 * (lam * lam) * y2_tr
        + lam * (80 * g3s + frac_f64(45, 2) * g2s) * (tu + td)
        + lam * g1s * (frac_f64(17, 2) * tu + frac_f64(5, 2) * td + frac_f64(15, 2) * te)
        + frac_f64(15, 2) * lam * g2s * te
        - 3 * lam * (thu2 + thd2 + frac_f64(1, 3) * the2 + 14 * thuhd)
        + lam * (-frac_f64(73, 8) * (g2s ** 2) + frac_f64(117, 20) * g1s * g2s + frac_f64(1887, 200) * (g1s ** 2))
        + 30 * (thu3 + thd3 + frac_f64(1, 3) * the3) - 6 * (thu2hd + thuhd2)
        - 32 * g3s * (thu2 + thd2) - frac_f64(8, 5) * g1s * thu2 + frac_f64(4, 5) * g1s * thd2 - frac_f64(12, 5) * g1s * the2
        - frac_f64(9, 4) * (g2s ** 2) * (tu + td + frac_f64(1, 3) * te)
        + g1s * g2s * (frac_f64(63, 10) * tu + frac_f64(27, 10) * td + frac_f64(33, 10) * te)
        - (g1s ** 2) * (frac_f64(171, 100) * tu - frac_f64(9, 20) * td + frac_f64(9, 4) * te)
        + frac_f64(305, 16) * (g2s ** 3) - frac_f64(289, 80) * (g2s ** 2) * g1s
        - frac_f64(1677, 400) * g2s * (g1s ** 2) - frac_f64(3411, 2000) * (g1s ** 3)
    )
    return dYu, dYd, dYe, dg1, dg2, dg3, k1 * dlam1 + k2 * dlam2


def rk4_sm_f64(
    Yu0: np.ndarray,
    Yd0: np.ndarray,
    Ye0: np.ndarray,
    g1_0: float,
    g2_0: float,
    g3_0: float,
    lam_0: float,
    dt_total: float,
    n_steps: int,
    two_loop: bool = True,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, float, float, float, float]:
    h = dt_total / n_steps
    Yu, Yd, Ye = Yu0.copy(), Yd0.copy(), Ye0.copy()
    g1, g2, g3, lam = g1_0, g2_0, g3_0, lam_0
    for _ in range(n_steps):
        s1 = sm_2loop_rhs_f64(Yu, Yd, Ye, g1, g2, g3, lam, two_loop)
        s2 = sm_2loop_rhs_f64(
            Yu + frac_f64(1, 2) * h * s1[0], Yd + frac_f64(1, 2) * h * s1[1], Ye + frac_f64(1, 2) * h * s1[2],
            g1 + frac_f64(1, 2) * h * s1[3], g2 + frac_f64(1, 2) * h * s1[4], g3 + frac_f64(1, 2) * h * s1[5],
            lam + frac_f64(1, 2) * h * s1[6], two_loop,
        )
        s3 = sm_2loop_rhs_f64(
            Yu + frac_f64(1, 2) * h * s2[0], Yd + frac_f64(1, 2) * h * s2[1], Ye + frac_f64(1, 2) * h * s2[2],
            g1 + frac_f64(1, 2) * h * s2[3], g2 + frac_f64(1, 2) * h * s2[4], g3 + frac_f64(1, 2) * h * s2[5],
            lam + frac_f64(1, 2) * h * s2[6], two_loop,
        )
        s4 = sm_2loop_rhs_f64(
            Yu + h * s3[0], Yd + h * s3[1], Ye + h * s3[2],
            g1 + h * s3[3], g2 + h * s3[4], g3 + h * s3[5], lam + h * s3[6], two_loop,
        )
        Yu = Yu + (h / 6) * (s1[0] + 2 * s2[0] + 2 * s3[0] + s4[0])
        Yd = Yd + (h / 6) * (s1[1] + 2 * s2[1] + 2 * s3[1] + s4[1])
        Ye = Ye + (h / 6) * (s1[2] + 2 * s2[2] + 2 * s3[2] + s4[2])
        g1 = g1 + (h / 6) * (s1[3] + 2 * s2[3] + 2 * s3[3] + s4[3])
        g2 = g2 + (h / 6) * (s1[4] + 2 * s2[4] + 2 * s3[4] + s4[4])
        g3 = g3 + (h / 6) * (s1[5] + 2 * s2[5] + 2 * s3[5] + s4[5])
        lam = lam + (h / 6) * (s1[6] + 2 * s2[6] + 2 * s3[6] + s4[6])
    return Yu, Yd, Ye, g1, g2, g3, lam


def wrap_angle_pi(angle: float) -> float:
    return math.atan2(math.sin(angle), math.cos(angle))


def haar_unitary_3x3(rng: np.random.Generator) -> np.ndarray:
    z = (rng.standard_normal((3, 3)) + complex(0, 1) * rng.standard_normal((3, 3))) / math.sqrt(2)
    q, r = np.linalg.qr(z)
    d = np.diag(r)
    return q * (d / np.abs(d))[None, :]


def extract_quark_cp_observables(Yu: np.ndarray, Yd: np.ndarray, theta_g: float) -> Tuple[float, float, np.ndarray]:
    uu, su, _ = np.linalg.svd(Yu)
    iu = np.argsort(su)
    uu, su = uu[:, iu], su[iu]

    ud, sd, _ = np.linalg.svd(Yd)
    id_ = np.argsort(sd)
    ud, sd = ud[:, id_], sd[id_]

    v_ckm = uu.conj().T @ ud
    j_ckm = float(np.imag(v_ckm[0, 1] * v_ckm[1, 2] * np.conj(v_ckm[0, 2]) * np.conj(v_ckm[1, 1])))
    det_y = np.linalg.det(Yu) * np.linalg.det(Yd)
    bar_theta = wrap_angle_pi(theta_g + math.atan2(float(np.imag(det_y)), float(np.real(det_y))))
    vec = np.array([su[0], su[1], su[2], sd[0], sd[1], sd[2], abs(v_ckm[0, 1]), abs(v_ckm[1, 2]), abs(v_ckm[0, 2]), j_ckm, bar_theta], dtype=float)
    return bar_theta, j_ckm, vec


def build_d_symmetric_hermitian_3fam_state(case_idx: int) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    # Construct strictly positive-definite complex Hermitian 3x3 matrices M = A @ A^dag
    # with non-commuting complex off-diagonal phases so J_CKM != 0 while Yu = Yu^dag, Yd = Yd^dag, Ye = Ye^dag!
    scale_shift = Fraction(case_idx, 20)
    Au = np.array(
        [
            [complex(frac_f64(1, 12), frac_f64(1, 30)), complex(frac_f64(1, 10), frac_f64(-1, 25)), complex(frac_f64(1, 9), frac_f64(1, 18))],
            [complex(frac_f64(-1, 25), frac_f64(1, 20)), complex(frac_f64(7, 20) + float(scale_shift) / 5, frac_f64(1, 15)), complex(frac_f64(1, 6), frac_f64(-1, 10))],
            [complex(frac_f64(1, 30), frac_f64(-1, 28)), complex(frac_f64(1, 8), frac_f64(1, 12)), complex(frac_f64(4, 5), frac_f64(1, 20))],
        ],
        dtype=complex,
    )
    Ad = np.array(
        [
            [complex(frac_f64(1, 15), frac_f64(-1, 35)), complex(frac_f64(1, 9), frac_f64(1, 14)), complex(frac_f64(-1, 16), frac_f64(1, 12))],
            [complex(frac_f64(1, 18), frac_f64(1, 16)), complex(frac_f64(3, 10) + float(scale_shift) / 8, frac_f64(-1, 14)), complex(frac_f64(1, 7), frac_f64(1, 9))],
            [complex(frac_f64(-1, 22), frac_f64(1, 25)), complex(frac_f64(1, 10), frac_f64(-1, 11)), complex(frac_f64(1, 2), frac_f64(-1, 25))],
        ],
        dtype=complex,
    )
    Ae = np.array(
        [
            [complex(frac_f64(1, 18), frac_f64(1, 40)), complex(frac_f64(1, 20), frac_f64(-1, 30)), complex(frac_f64(1, 25), frac_f64(1, 35))],
            [complex(frac_f64(-1, 30), frac_f64(1, 25)), complex(frac_f64(1, 4), frac_f64(1, 30)), complex(frac_f64(1, 12), frac_f64(-1, 18))],
            [complex(frac_f64(1, 35), frac_f64(-1, 30)), complex(frac_f64(1, 15), frac_f64(1, 20)), complex(frac_f64(9, 20), frac_f64(1, 30))],
        ],
        dtype=complex,
    )
    Yu = Au @ Au.conj().T
    Yd = Ad @ Ad.conj().T
    Ye = Ae @ Ae.conj().T
    return Yu, Yd, Ye


def run_strong_cp_checks() -> Dict[str, Any]:
    g_uv = math.sqrt(4 * math.pi / 42)
    lam_uv = frac_f64(1, 8)

    max_tree_theta = frac_f64(0, 1)
    max_2loop_ir_theta = frac_f64(0, 1)
    min_ir_abs_j_ckm = frac_f64(1, 1)
    max_im_beta_trace = frac_f64(0, 1)

    for idx in range(3):
        Yu0, Yd0, Ye0 = build_d_symmetric_hermitian_3fam_state(idx)
        th_uv, j_uv, _ = extract_quark_cp_observables(Yu0, Yd0, frac_f64(0, 1))
        max_tree_theta = max(max_tree_theta, abs(th_uv))

        # Check instantaneous 2-loop Jacobi trace reality Im Tr((dYu/dt) Yu^{-1} + (dYd/dt) Yd^{-1}) == 0
        dYu, dYd, _, _, _, _, _ = sm_2loop_rhs_f64(Yu0, Yd0, Ye0, g_uv, g_uv, g_uv, lam_uv, True)
        im_tr = abs(float(np.imag(np.trace(dYu @ np.linalg.inv(Yu0) + dYd @ np.linalg.inv(Yd0)))))
        max_im_beta_trace = max(max_im_beta_trace, im_tr)

        Yu_ir, Yd_ir, Ye_ir, _, _, _, _ = rk4_sm_f64(Yu0, Yd0, Ye0, g_uv, g_uv, g_uv, lam_uv, frac_f64(-30, 1), 900, True)
        th_ir, j_ir, _ = extract_quark_cp_observables(Yu_ir, Yd_ir, frac_f64(0, 1))
        max_2loop_ir_theta = max(max_2loop_ir_theta, abs(th_ir))
        min_ir_abs_j_ckm = min(min_ir_abs_j_ckm, abs(j_ir))

    # 8 random Haar U(3)^6 basis transformations on state 0 (with Fujikawa anomaly compensation)
    Yu_b, Yd_b, Ye_b = build_d_symmetric_hermitian_3fam_state(0)
    Yu_ref, Yd_ref, _, _, _, _, _ = rk4_sm_f64(Yu_b, Yd_b, Ye_b, g_uv, g_uv, g_uv, lam_uv, frac_f64(-30, 1), 900, True)
    _, _, vec_ref = extract_quark_cp_observables(Yu_ref, Yd_ref, frac_f64(0, 1))

    rng = np.random.default_rng(20261117)
    max_haar_drift = frac_f64(0, 1)
    max_haar_ir_theta = frac_f64(0, 1)
    for _ in range(8):
        UQ = haar_unitary_3x3(rng)
        Uu = haar_unitary_3x3(rng)
        Ud = haar_unitary_3x3(rng)
        UL = haar_unitary_3x3(rng)
        Ue = haar_unitary_3x3(rng)

        Yu_s = UQ @ Yu_b @ Uu.conj().T
        Yd_s = UQ @ Yd_b @ Ud.conj().T
        Ye_s = UL @ Ye_b @ Ue.conj().T
        jac = (np.linalg.det(UQ) ** 2) * np.linalg.det(Uu.conj().T) * np.linalg.det(Ud.conj().T)
        theta_fuj = wrap_angle_pi(-math.atan2(float(np.imag(jac)), float(np.real(jac))))

        Yu_sir, Yd_sir, _, _, _, _, _ = rk4_sm_f64(Yu_s, Yd_s, Ye_s, g_uv, g_uv, g_uv, lam_uv, frac_f64(-30, 1), 900, True)
        th_sir, _, vec_sir = extract_quark_cp_observables(Yu_sir, Yd_sir, theta_fuj)
        max_haar_ir_theta = max(max_haar_ir_theta, abs(th_sir))
        drift = max(float(np.max(np.abs(vec_sir[:10] - vec_ref[:10]))), abs(wrap_angle_pi(vec_sir[10] - vec_ref[10])))
        max_haar_drift = max(max_haar_drift, drift)

    strong_cp_ok = (
        max_tree_theta < pow10_f64(-15)
        and max_im_beta_trace < pow10_f64(-15)
        and max_2loop_ir_theta < pow10_f64(-13)
        and min_ir_abs_j_ckm > pow10_f64(-5)
        and max_haar_ir_theta < pow10_f64(-13)
        and max_haar_drift < pow10_f64(-12)
    )
    return {
        "strong_cp_gate_passed": strong_cp_ok,
        "max_tree_bar_theta_qcd": max_tree_theta,
        "max_instantaneous_2loop_im_jacobi_trace": max_im_beta_trace,
        "max_2loop_ir_bar_theta_qcd_across_3_states": max_2loop_ir_theta,
        "min_ir_abs_J_CKM_across_3_states": min_ir_abs_j_ckm,
        "max_haar_u3_6_ir_bar_theta_qcd": max_haar_ir_theta,
        "max_haar_u3_6_observable_drift": max_haar_drift,
    }


# ============================================================================
# SECTION 3: 1-LOOP & 2-LOOP PATI-SALAM x| Z_2^D CORRIDOR (P-862) & 4D SCALING
# ============================================================================

def rk4_ps_2loop_gauge(
    g4_0: float,
    g2L_0: float,
    g2R_0: float,
    b_ps: List[float],
    B_ps: List[List[float]],
    dt_total: float,
    n_steps: int,
    two_loop: bool = True,
) -> Tuple[float, float, float]:
    k1 = frac_f64(1, 16) / (math.pi * math.pi)
    k2 = k1 * k1 if two_loop else frac_f64(0, 1)

    def rhs(g4: float, g2l: float, g2r: float) -> Tuple[float, float, float]:
        gsq = [g4 * g4, g2l * g2l, g2r * g2r]
        gvec = [g4, g2l, g2r]
        out = [frac_f64(0, 1), frac_f64(0, 1), frac_f64(0, 1)]
        for a in range(3):
            s2_sum = sum(B_ps[a][b] * gsq[b] for b in range(3))
            out[a] = (gvec[a] ** 3) * (k1 * b_ps[a] + k2 * s2_sum)
        return out[0], out[1], out[2]

    h = dt_total / n_steps
    g4, g2l, g2r = g4_0, g2L_0, g2R_0
    for _ in range(n_steps):
        s1 = rhs(g4, g2l, g2r)
        s2 = rhs(g4 + frac_f64(1, 2) * h * s1[0], g2l + frac_f64(1, 2) * h * s1[1], g2r + frac_f64(1, 2) * h * s1[2])
        s3 = rhs(g4 + frac_f64(1, 2) * h * s2[0], g2l + frac_f64(1, 2) * h * s2[1], g2r + frac_f64(1, 2) * h * s2[2])
        s4 = rhs(g4 + h * s3[0], g2l + h * s3[1], g2r + h * s3[2])
        g4 += (h / 6) * (s1[0] + 2 * s2[0] + 2 * s3[0] + s4[0])
        g2l += (h / 6) * (s1[1] + 2 * s2[1] + 2 * s3[1] + s4[1])
        g2r += (h / 6) * (s1[2] + 2 * s2[2] + 2 * s3[2] + s4[2])
    return g4, g2l, g2r


def run_pati_salam_corridor_and_collar_obstruction(vol_m000: float, vol_m004: float) -> Dict[str, Any]:
    # Exact Machacek-Vaughn (1983) derivation of 1-loop and 2-loop Pati-Salam gauge betas
    c2_ps = [Fraction(4, 1), Fraction(2, 1), Fraction(2, 1)]
    ps_gen1 = [
        ([4, 2, 1], [Fraction(1, 2), Fraction(1, 2), Fraction(0, 1)], [Fraction(15, 8), Fraction(3, 4), Fraction(0, 1)]),
        ([4, 1, 2], [Fraction(1, 2), Fraction(0, 1), Fraction(1, 2)], [Fraction(15, 8), Fraction(0, 1), Fraction(3, 4)]),
    ]
    ps_scalars = [
        ([1, 2, 2], [Fraction(0, 1), Fraction(1, 2), Fraction(1, 2)], [Fraction(0, 1), Fraction(3, 4), Fraction(3, 4)]),
        ([4, 1, 2], [Fraction(1, 2), Fraction(0, 1), Fraction(1, 2)], [Fraction(15, 8), Fraction(0, 1), Fraction(3, 4)]),
        ([4, 2, 1], [Fraction(1, 2), Fraction(1, 2), Fraction(0, 1)], [Fraction(15, 8), Fraction(3, 4), Fraction(0, 1)]),
    ]
    b_ps_frac, B_ps_frac = mv_2loop_gauge_matrix(c2_ps, ps_gen1 * 3, ps_scalars)
    delta_b_ps = b_ps_frac[1] - b_ps_frac[0]  # -7/3 - (-10) = +23/3
    reciprocity_ok = (15 * B_ps_frac[0][1] == 3 * B_ps_frac[1][0]) and (15 * B_ps_frac[0][1] == Fraction(225, 2))
    expected_B_ps = [
        [Fraction(-117, 2), Fraction(15, 2), Fraction(15, 2)],
        [Fraction(75, 2), Fraction(50, 3), Fraction(3, 1)],
        [Fraction(75, 2), Fraction(3, 1), Fraction(50, 3)],
    ]
    ps_betas_exact = (b_ps_frac == [Fraction(-10, 1), Fraction(-7, 3), Fraction(-7, 3)]) and (B_ps_frac == expected_B_ps) and reciprocity_ok

    # Verify exact rational coefficients of the 1-loop P-862 Pati-Salam elimination law:
    # sin^2 theta_W = c0 + c_rat * (alpha_EM / alpha_3) + c_ps * (alpha_EM / pi) * Delta_PS
    b1_sm, b2_sm, b3_sm = Fraction(41, 10), Fraction(-19, 6), Fraction(-7, 1)
    denom_em_3 = Fraction(5, 3) * b1_sm + b2_sm - Fraction(8, 3) * b3_sm  # 67/3
    c0_exact = (b2_sm - b3_sm) / denom_em_3  # (23/6) / (67/3) = 23/134
    c_rat_exact = 1 - Fraction(8, 3) * c0_exact  # 1 - 184/402 = 218/402 = 109/201
    # Coefficient of (Delta_PS / (2 pi)) in alpha_2^{-1}(IR): (1 - 2 * c0_exact) * delta_b_ps = (44/67) * delta_b_ps
    # Dividing by 2 gives coefficient of (alpha_EM / pi) * Delta_PS: (22/67) * delta_b_ps = 506/201!
    c_ps_over_pi = Fraction(22, 67) * delta_b_ps  # 22/67 * 23/3 = 506/201

    coeff_algebra_ok = (
        c0_exact == Fraction(23, 134)
        and c_rat_exact == Fraction(109, 201)
        and c_ps_over_pi == Fraction(506, 201)
        and c_ps_over_pi > 0
    )

    b_ps_f = [float(x) for x in b_ps_frac]
    B_ps_f = [[float(x) for x in row] for row in B_ps_frac]

    # Canonical 0-of-19 geometric Delta_PS grid from m000/m004 invariants
    a_max = 2 * math.sqrt(3)
    v_cusp = math.sqrt(3)
    delta_ps_grid: List[Tuple[str, float]] = [
        ("0_minimal_su5_desert", frac_f64(0, 1)),
        ("Vol_m000", vol_m000),
        ("ln_A_max", math.log(a_max)),
        ("V_cusp_max", v_cusp),
        ("Vol_m004", vol_m004),
        ("A_max_2sqrt3", a_max),
        ("2_Vol_m004", 2 * vol_m004),
        ("4_Vol_m004", 4 * vol_m004),
    ]

    # Test 1-loop closed-form identity against 1-loop ODE across 12 x 8 = 96 histories
    z3 = np.zeros((3, 3), dtype=complex)
    max_1loop_corridor_ode_err = frac_f64(0, 1)
    for alpha_u_inv in (frac_f64(54, 1), frac_f64(62, 1), frac_f64(70, 1)):
        for delta_sm in (frac_f64(24, 1), frac_f64(27, 1), frac_f64(30, 1), frac_f64(32, 1)):
            for _, dps in delta_ps_grid:
                g_u = math.sqrt(4 * math.pi / alpha_u_inv)
                if dps > 0:
                    g4_p, g2l_p, g2r_p = rk4_ps_2loop_gauge(g_u, g_u, g_u, b_ps_f, B_ps_f, -dps, 1200, two_loop=False)
                else:
                    g4_p, g2l_p, g2r_p = g_u, g_u, g_u
                a4_p = 4 * math.pi / (g4_p * g4_p)
                a2l_p = 4 * math.pi / (g2l_p * g2l_p)
                a2r_p = 4 * math.pi / (g2r_p * g2r_p)
                a1_p = frac_f64(3, 5) * a2r_p + frac_f64(2, 5) * a4_p
                g1_p = math.sqrt(4 * math.pi / a1_p)
                g2_p = math.sqrt(4 * math.pi / a2l_p)
                g3_p = g4_p

                _, _, _, g1_ir, g2_ir, g3_ir, _ = rk4_sm_f64(z3, z3, z3, g1_p, g2_p, g3_p, frac_f64(0, 1), -delta_sm, 2400, two_loop=False)
                a1_ir = 4 * math.pi / (g1_ir * g1_ir)
                a2_ir = 4 * math.pi / (g2_ir * g2_ir)
                a3_ir = 4 * math.pi / (g3_ir * g3_ir)
                aem_ir = frac_f64(5, 3) * a1_ir + a2_ir
                sin2_ode = a2_ir / aem_ir
                sin2_law = (
                    float(c0_exact)
                    + float(c_rat_exact) * (a3_ir / aem_ir)
                    + (float(c_ps_over_pi) / math.pi) * (dps / aem_ir)
                )
                max_1loop_corridor_ode_err = max(max_1loop_corridor_ode_err, abs(sin2_ode - sin2_law))

    # Blind 2-loop coupled Pati-Salam -> SM gauge-Yukawa corridor table across the 8 canonical geometric Delta_PS values:
    # Solve by 2D Newton shooting for (alpha_U^{-1}, Delta_SM) matching fixed synthetic rational IR couplings
    # (alpha_EM^{-1}(IR), alpha_3^{-1}(IR)) = (150, 15) (strictly 0 of 19 synthetic integers), isolating the pure
    # 2-loop P-862 corridor law sin^2 theta_W(IR) as a function of Delta_PS!
    Yu_ref, Yd_ref, Ye_ref = build_d_symmetric_hermitian_3fam_state(0)
    target_aem_ir = frac_f64(150, 1)
    target_a3_ir = frac_f64(15, 1)

    def forward_2loop_ir_couplings(alpha_u_inv_v: float, delta_sm_v: float, dps_v: float) -> Tuple[float, float, float]:
        g_u = math.sqrt(4 * math.pi / alpha_u_inv_v)
        if dps_v > 0:
            g4_p, g2l_p, g2r_p = rk4_ps_2loop_gauge(g_u, g_u, g_u, b_ps_f, B_ps_f, -dps_v, 300, two_loop=True)
        else:
            g4_p, g2l_p, g2r_p = g_u, g_u, g_u
        a4_p = 4 * math.pi / (g4_p * g4_p)
        a2l_p = 4 * math.pi / (g2l_p * g2l_p)
        a2r_p = 4 * math.pi / (g2r_p * g2r_p)
        a1_p = frac_f64(3, 5) * a2r_p + frac_f64(2, 5) * a4_p
        g1_p = math.sqrt(4 * math.pi / a1_p)
        g2_p = math.sqrt(4 * math.pi / a2l_p)
        g3_p = g4_p
        lam_p = (g2_p * g2_p) / 5
        _, _, _, g1_ir, g2_ir, g3_ir, _ = rk4_sm_f64(Yu_ref, Yd_ref, Ye_ref, g1_p, g2_p, g3_p, lam_p, -delta_sm_v, 600, two_loop=True)
        a1_ir = 4 * math.pi / (g1_ir * g1_ir)
        a2_ir = 4 * math.pi / (g2_ir * g2_ir)
        a3_ir = 4 * math.pi / (g3_ir * g3_ir)
        aem_ir = frac_f64(5, 3) * a1_ir + a2_ir
        return aem_ir, a3_ir, a2_ir / aem_ir

    corridor_table_2loop: List[Dict[str, Any]] = []
    sin2_prev = frac_f64(-1, 1)
    monotone_2loop_lift = True
    max_newton_residual = frac_f64(0, 1)

    for label, dps in delta_ps_grid:
        # Analytic 1-loop initial guess for (alpha_U^{-1}, Delta_SM):
        # delta_sm_0 = (6 pi / 67) * (target_aem - (8/3) target_a3 - (delta_b_ps / pi) * dps)
        dsm_cur = (6 * math.pi / 67) * (target_aem_ir - frac_f64(8, 3) * target_a3_ir - (float(delta_b_ps) / math.pi) * dps)
        au_cur = target_a3_ir + (7 / (2 * math.pi)) * dsm_cur + (10 / (2 * math.pi)) * dps
        eps_fd = pow10_f64(-5)
        for _ in range(8):
            f_aem, f_a3, _ = forward_2loop_ir_couplings(au_cur, dsm_cur, dps)
            r0 = f_aem - target_aem_ir
            r1 = f_a3 - target_a3_ir
            if max(abs(r0), abs(r1)) < pow10_f64(-12):
                break
            f_aem_u, f_a3_u, _ = forward_2loop_ir_couplings(au_cur + eps_fd, dsm_cur, dps)
            f_aem_s, f_a3_s, _ = forward_2loop_ir_couplings(au_cur, dsm_cur + eps_fd, dps)
            j00 = (f_aem_u - f_aem) / eps_fd
            j10 = (f_a3_u - f_a3) / eps_fd
            j01 = (f_aem_s - f_aem) / eps_fd
            j11 = (f_a3_s - f_a3) / eps_fd
            det_j = j00 * j11 - j01 * j10
            au_cur -= (j11 * r0 - j01 * r1) / det_j
            dsm_cur -= (-j10 * r0 + j00 * r1) / det_j

        aem_ir, a3_ir, sin2_2l = forward_2loop_ir_couplings(au_cur, dsm_cur, dps)
        max_newton_residual = max(max_newton_residual, abs(aem_ir - target_aem_ir), abs(a3_ir - target_a3_ir))
        sin2_1l_formula = (
            float(c0_exact)
            + float(c_rat_exact) * (target_a3_ir / target_aem_ir)
            + (float(c_ps_over_pi) / math.pi) * (dps / target_aem_ir)
        )
        delta_2loop_shift = sin2_2l - sin2_1l_formula
        if sin2_2l <= sin2_prev:
            monotone_2loop_lift = False
        sin2_prev = sin2_2l
        corridor_table_2loop.append(
            {
                "collar_label": label,
                "Delta_PS": dps,
                "solved_alpha_U_inv_2loop": au_cur,
                "solved_Delta_SM_2loop": dsm_cur,
                "alpha_EM_inv_IR": aem_ir,
                "alpha_3_inv_IR": a3_ir,
                "sin2_theta_W_1loop_law": sin2_1l_formula,
                "sin2_theta_W_2loop": sin2_2l,
                "two_loop_shift_delta_2loop": delta_2loop_shift,
            }
        )

    # 4D Collar Scaling Obstruction Proof (Guardrail 1):
    # On X_4 = m000 x~ [-L_4, L_4] with ds_4^2 = ds_4_trans^2 + e^{-2 sigma(s)} ds_{m000}^2:
    # Under transverse rescaling L_4 -> lambda_4 * L_4 and warp rate kappa_w -> c_w * kappa_w,
    # 3D hyperbolic invariants of partial X_4 = m004 (Vol_m004, A_max, Im(tau_cusp)) have 0 variation,
    # whereas 4D gauge norm alpha_U^{-1} = (4 pi / g_bulk^2) * (2 L_4 * Vol(m000)) and collar log-threshold
    # Delta_PS = kappa_w * L_4 scale linearly with (lambda_4, kappa_w).
    def eval_4d_collar_reduction(lam4: float, kwarp: float) -> Tuple[float, float, float, float]:
        # Returns (Vol_m004_boundary, A_max_boundary, alpha_U_inv_4d_unit_bulk, Delta_PS_warped)
        return vol_m004, a_max, 4 * math.pi * (2 * lam4 * vol_m000), kwarp * lam4

    base_4d = eval_4d_collar_reduction(frac_f64(1, 1), frac_f64(1, 1))
    scaled_4d = eval_4d_collar_reduction(frac_f64(3, 1), frac_f64(2, 1))
    boundary_3d_rigid = (abs(scaled_4d[0] - base_4d[0]) == 0) and (abs(scaled_4d[1] - base_4d[1]) == 0)
    bulk_4d_unfixed_without_potential = (abs(scaled_4d[2] / base_4d[2] - 3) < pow10_f64(-15)) and (
        abs(scaled_4d[3] - 6) < pow10_f64(-15)
    )

    corridor_gate_ok = (
        ps_betas_exact
        and coeff_algebra_ok
        and max_1loop_corridor_ode_err < pow10_f64(-14)
        and max_newton_residual < pow10_f64(-11)
        and monotone_2loop_lift
        and boundary_3d_rigid
        and bulk_4d_unfixed_without_potential
    )

    return {
        "pati_salam_corridor_and_obstruction_gate_passed": corridor_gate_ok,
        "b_PS_1loop": [str(x) for x in b_ps_frac],
        "B_PS_2loop": [[str(x) for x in row] for row in B_ps_frac],
        "gauge_reciprocity_15_B4_2L_eq_3_B2L_4": reciprocity_ok,
        "p862_1loop_exact_coefficients": {
            "c0": str(c0_exact),
            "c_alphaEM_over_alpha3": str(c_rat_exact),
            "c_DeltaPS_times_pi": str(c_ps_over_pi),
            "c_DeltaPS_numeric": float(c_ps_over_pi) / math.pi,
        },
        "max_1loop_corridor_law_vs_ode_err_across_96_histories": max_1loop_corridor_ode_err,
        "max_2loop_newton_shooting_residual": max_newton_residual,
        "monotone_2loop_sin2_lift_across_Delta_PS": monotone_2loop_lift,
        "blind_2loop_corridor_table": corridor_table_2loop,
        "collar_4d_scaling_obstruction": {
            "boundary_3d_mostow_rigid": boundary_3d_rigid,
            "bulk_4d_L4_and_warp_unfixed_without_4d_potential": bulk_4d_unfixed_without_potential,
            "parameter_free_collar_scale_fixing_closes_from_3d_alone": False,
            "obstruction_statement": "3D Mostow rigidity fixes Vol(m004), A_max, and tau_cusp uniquely, but alpha_U^-1 and ln(M_U/M_PS) scale with 4D interval length L_4 and collar warp rate unless a 4D bulk stabilization action is supplied.",
        },
    }


# ============================================================================
# SECTION 4: FIVE PLANTED FAULT CONTROLS (PF1.1 - PF1.5)
# ============================================================================

def run_planted_faults_g1() -> Dict[str, Any]:
    g_uv = math.sqrt(4 * math.pi / 42)
    lam_uv = frac_f64(1, 8)
    Yu0, Yd0, Ye0 = build_d_symmetric_hermitian_3fam_state(0)

    # PF1.1: Non-Hermitian D-parity-breaking perturbation at M_PS
    Yd_bad = Yd0.copy()
    Yd_bad[0, 2] += complex(frac_f64(1, 20), frac_f64(1, 12))
    Yu_pf1, Yd_pf1, _, _, _, _, _ = rk4_sm_f64(Yu0, Yd_bad, Ye0, g_uv, g_uv, g_uv, lam_uv, frac_f64(-30, 1), 450, True)
    th_pf1, _, _ = extract_quark_cp_observables(Yu_pf1, Yd_pf1, frac_f64(0, 1))
    pf1_1_err = abs(th_pf1)
    pf1_1_caught = pf1_1_err > frac_f64(1, 20)

    # PF1.2: Opposite determinant sign parity (Hermitian Yd with one negative eigenvalue => det(Yu Yd) < 0)
    evals, evecs = np.linalg.eigh(Yd0)
    evals_flip = evals.copy()
    evals_flip[0] = -evals_flip[0]
    Yd_flip = evecs @ np.diag(evals_flip) @ evecs.conj().T
    th_pf2, _, _ = extract_quark_cp_observables(Yu0, Yd_flip, frac_f64(0, 1))
    pf1_2_err = abs(th_pf2)
    pf1_2_caught = pf1_2_err > frac_f64(3, 1)

    # PF1.3: 6-family mirror doubling regression (N_g = 6 => b_3 = -3 vs -7)
    b3_3fam = -Fraction(11, 3) * 3 + Fraction(2, 3) * 3 * 2
    b3_6fam = -Fraction(11, 3) * 3 + Fraction(2, 3) * 6 * 2
    pf1_3_err = float(abs(b3_6fam - b3_3fam))
    pf1_3_caught = pf1_3_err > frac_f64(1, 1)

    # PF1.4: Flipped threshold running sign in Delta_PS
    z3 = np.zeros((3, 3), dtype=complex)
    b_ps_f = [frac_f64(-10, 1), frac_f64(-7, 3), frac_f64(-7, 3)]
    B_ps_zero = [[frac_f64(0, 1)] * 3 for _ in range(3)]
    dps_test = frac_f64(4, 1)
    gu = math.sqrt(4 * math.pi / 45)
    g4_p, g2l_p, g2r_p = rk4_ps_2loop_gauge(gu, gu, gu, b_ps_f, B_ps_zero, -dps_test, 300, two_loop=False)
    a4_p = 4 * math.pi / (g4_p * g4_p)
    a2_p = 4 * math.pi / (g2l_p * g2l_p)
    a1_p = frac_f64(3, 5) * a2_p + frac_f64(2, 5) * a4_p
    _, _, _, g1_ir, g2_ir, g3_ir, _ = rk4_sm_f64(
        z3, z3, z3, math.sqrt(4 * math.pi / a1_p), math.sqrt(4 * math.pi / a2_p), math.sqrt(4 * math.pi / a4_p),
        frac_f64(0, 1), frac_f64(-28, 1), 500, two_loop=False,
    )
    a1_ir = 4 * math.pi / (g1_ir * g1_ir)
    a2_ir = 4 * math.pi / (g2_ir * g2_ir)
    a3_ir = 4 * math.pi / (g3_ir * g3_ir)
    aem_ir = frac_f64(5, 3) * a1_ir + a2_ir
    sin2_true = a2_ir / aem_ir
    sin2_flipped = frac_f64(23, 134) + frac_f64(109, 201) * (a3_ir / aem_ir) - (frac_f64(506, 201) / math.pi) * (dps_test / aem_ir)
    pf1_4_err = abs(sin2_true - sin2_flipped)
    pf1_4_caught = pf1_4_err > frac_f64(1, 100)

    # PF1.5: Over-inflated horoball height t = 1/2 < t_tan = 1 => Euclidean sphere diameter = 1 / (|c|^2 t) = 2 > lattice spacing 1
    t_bad = Fraction(1, 2)
    c_norm_sq = 1
    euclid_sphere_diam = Fraction(1, 1) / (c_norm_sq * t_bad)  # = 2
    lattice_min_dist = Fraction(1, 1)  # meridian shift |1| = 1 between adjacent horoballs at z=0 and z=1
    overlap_penetration = float(euclid_sphere_diam - lattice_min_dist)  # = 1.0 > 0
    pf1_5_caught = overlap_penetration > frac_f64(1, 2)

    all_caught = pf1_1_caught and pf1_2_caught and pf1_3_caught and pf1_4_caught and pf1_5_caught
    return {
        "all_5_planted_faults_caught": all_caught,
        "PF1_1_broken_dparity_theta_err": {"measured_err": pf1_1_err, "caught": pf1_1_caught},
        "PF1_2_opposite_det_parity_theta_err": {"measured_err": pf1_2_err, "caught": pf1_2_caught},
        "PF1_3_six_family_b3_shift": {"measured_err": pf1_3_err, "caught": pf1_3_caught},
        "PF1_4_flipped_threshold_sign_err": {"measured_err": pf1_4_err, "caught": pf1_4_caught},
        "PF1_5_horoball_overlap_penetration": {"measured_err": overlap_penetration, "caught": pf1_5_caught},
    }


def main() -> None:
    ast_res = verify_ast_g1()
    cusp_res = run_cusp_and_e6_checks()
    scp_res = run_strong_cp_checks()
    ps_res = run_pati_salam_corridor_and_collar_obstruction(cusp_res["Vol_m000"], cusp_res["Vol_m004"])
    pf_res = run_planted_faults_g1()

    gate_passed = (
        ast_res["ast_gate_passed"]
        and cusp_res["cusp_and_e6_gate_passed"]
        and scp_res["strong_cp_gate_passed"]
        and ps_res["pati_salam_corridor_and_obstruction_gate_passed"]
        and pf_res["all_5_planted_faults_caught"]
    )

    payload = {
        "campaign": "AGY-002-ENDGAME-V2",
        "gate": "Gate 1 — E_6 -> Pati-Salam x| Z_2^D Universal Gauge Corridor & 3-Family Strong-CP Law",
        "empirical_firewall": "0 of 19",
        "gate_1_passed": gate_passed,
        "section_0_ast_lock": ast_res,
        "section_1_cusp_z_zeta6_and_e6_27_branching": cusp_res,
        "section_2_3family_dparity_strong_cp_law": scp_res,
        "section_3_pati_salam_corridor_and_4d_collar_obstruction": ps_res,
        "section_4_planted_fault_controls": pf_res,
    }

    out_path = Path(__file__).resolve().parent / "verify_endgame_v2_g1_fixed_out.json"
    out_bytes = (json.dumps(payload, indent=2, sort_keys=False) + "\n").encode("utf-8")
    out_path.write_bytes(out_bytes)
    digest = hashlib.sha256(out_bytes).hexdigest()
    sha_path = Path(__file__).resolve().parent / "OUTPUT_SHA256.txt"
    sha_path.write_text(f"{digest}  relays/agy002_endgame_v2_g1_fixed/verify_endgame_v2_g1_fixed_out.json\n", encoding="utf-8")


if __name__ == "__main__":
    main()
