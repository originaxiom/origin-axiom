#!/usr/bin/env python3
"""
Standalone Zero-Import Verifier for Card AGY-002_FOUND-G8:
  Complete Resolution of P-863 (B1951): CAR/Clifford Derivation of Postulate D,
  Continuous-Colour Commutant Dichotomy, Metallic Rivals, and Prime-3 / Prime-5
  Orthogonality in E_8 (0 of 19).

Empirical Firewall: 0 of 19 (zero repository imports, zero float/complex literals in source).
"""

from __future__ import annotations

import ast
import cmath
from collections import Counter
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple

import numpy as np


ALLOWED_IMPORTS: Set[str] = {
    "__future__",
    "ast",
    "cmath",
    "collections",
    "fractions",
    "hashlib",
    "json",
    "math",
    "numpy",
    "pathlib",
    "typing",
}


def frac_f64(num: int, den: int = 1) -> float:
    return float(Fraction(num, den))


def pow10_f64(exp_int: int) -> float:
    return float(Fraction(10, 1) ** exp_int)


# ============================================================================
# SECTION 0: AST SOURCE LOCK (ZERO REPO IMPORTS & ZERO FLOAT/COMPLEX LITERALS)
# ============================================================================

def verify_ast_g8() -> Dict[str, Any]:
    src = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(src)
    mods: Set[str] = set()
    float_literals = 0
    complex_literals = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                mods.add(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.level > 0:
                mods.add("<relative>")
            elif node.module:
                mods.add(node.module.split(".")[0])
        elif isinstance(node, ast.Constant):
            if isinstance(node.value, float):
                float_literals += 1
            elif isinstance(node.value, complex):
                complex_literals += 1

    disallowed = sorted(mods - ALLOWED_IMPORTS)
    passed = (len(disallowed) == 0) and (float_literals == 0) and (complex_literals == 0)
    return {
        "ast_gate_passed": passed,
        "imported_modules": sorted(mods),
        "disallowed_imports": disallowed,
        "float_literals_in_entire_file": float_literals,
        "complex_literals_in_entire_file": complex_literals,
    }


# ============================================================================
# SECTION 1: CAR / CL(10) FOCK DERIVATION OF POSTULATE D (P-863(a))
# ============================================================================

def build_level5_weil() -> Tuple[np.ndarray, np.ndarray, np.ndarray, List[np.ndarray]]:
    # B1951 convention: psi(u) = exp(4 pi i u / 5), rho(T) = diag(psi(2 x^2)) = diag(z5^{4 x^2}),
    # rho(S)_{xy} = -(1/sqrt(5)) z5^{-2 x y} = -(1/sqrt(5)) z5^{3 x y}: (ST)^3 == S^2 == P5
    z5 = cmath.exp(2 * complex(0, 1) * math.pi / 5)
    T5 = np.diag([z5 ** ((4 * x * x) % 5) for x in range(5)])
    S5 = np.array(
        [[-frac_f64(1, 1) * (z5 ** ((3 * x * y) % 5)) / math.sqrt(5) for y in range(5)] for x in range(5)],
        dtype=complex,
    )
    P5 = np.zeros((5, 5), dtype=complex)
    for x in range(5):
        P5[x, (-x) % 5] = frac_f64(1, 1)

    grp: List[np.ndarray] = [np.eye(5, dtype=complex)]
    for M in grp:
        for G in (T5, S5):
            cand = M @ G
            if not any(np.linalg.norm(cand - H) < pow10_f64(-10) for H in grp):
                grp.append(cand)
    return T5, S5, P5, grp


def run_section_1_car_fock_postulate_d(T5: np.ndarray, S5: np.ndarray, P5: np.ndarray, grp: List[np.ndarray]) -> Dict[str, Any]:
    s2_err = float(np.linalg.norm(S5 @ S5 - P5))
    st3_err = float(np.linalg.norm(np.linalg.matrix_power(S5 @ T5, 3) - P5))

    # Build 32 x 32 CAR creation/annihilation operators on Fock(W_5) = Lambda^*(W_5)
    c_ops: List[np.ndarray] = []
    for a in range(5):
        mat = np.zeros((32, 32), dtype=complex)
        for mask in range(32):
            if (mask >> a) & 1:
                below = bin(mask & ((1 << a) - 1)).count("1")
                sgn = frac_f64(-1, 1) if (below % 2 == 1) else frac_f64(1, 1)
                mat[mask ^ (1 << a), mask] = sgn
        c_ops.append(mat)
    cdag_ops = [m.conj().T for m in c_ops]

    # Verify CAR {c_a, c_b^dag} = delta_{ab} I_32 and {c_a, c_b} = 0
    max_car_err = frac_f64(0, 1)
    i32 = np.eye(32, dtype=complex)
    for a in range(5):
        for b in range(5):
            anti_ab = c_ops[a] @ cdag_ops[b] + cdag_ops[b] @ c_ops[a]
            target = i32 if a == b else np.zeros((32, 32), dtype=complex)
            max_car_err = max(max_car_err, float(np.linalg.norm(anti_ab - target)))
            max_car_err = max(max_car_err, float(np.linalg.norm(c_ops[a] @ c_ops[b] + c_ops[b] @ c_ops[a])))

    # Build 10 Hermitian Clifford Cl(10) gamma matrices and prove 1024 subset products are orthonormal (span == 1024)
    gammas: List[np.ndarray] = []
    for a in range(5):
        gammas.append(c_ops[a] + cdag_ops[a])
        gammas.append(-complex(0, 1) * (c_ops[a] - cdag_ops[a]))

    nonempty_max_trace = frac_f64(0, 1)
    unitarity_max_err = frac_f64(0, 1)
    prod_count = 0
    for mask_g in range(1024):
        prod_m = np.eye(32, dtype=complex)
        for bit_i in range(10):
            if (mask_g >> bit_i) & 1:
                prod_m = prod_m @ gammas[bit_i]
        prod_count += 1
        unitarity_max_err = max(unitarity_max_err, float(np.linalg.norm(prod_m.conj().T @ prod_m - i32)))
        if mask_g != 0:
            nonempty_max_trace = max(nonempty_max_trace, float(abs(np.trace(prod_m))) / 32)
    cl10_span_dim = prod_count if (nonempty_max_trace < pow10_f64(-13) and unitarity_max_err < pow10_f64(-13)) else 0

    # Second-quantized 6Y on Fock(W_5): zero normal-ordering ambiguity because Tr(6Y) == 0
    Y6_single = frac_f64(1, 2) * (np.eye(5, dtype=complex) - frac_f64(5, 1) * P5)
    tr_y6 = float(abs(np.trace(Y6_single)))
    Y6_fock_normal = sum(Y6_single[a, b] * (cdag_ops[a] @ c_ops[b]) for a in range(5) for b in range(5))
    Y6_fock_weyl = sum(
        Y6_single[a, b] * (cdag_ops[a] @ c_ops[b] - (frac_f64(1, 2) if a == b else frac_f64(0, 1)) * i32)
        for a in range(5) for b in range(5)
    )
    normal_vs_weyl_diff = float(np.linalg.norm(Y6_fock_normal - Y6_fock_weyl))

    even_idx = [m for m in range(32) if bin(m).count("1") % 2 == 0]
    odd_idx = [m for m in range(32) if bin(m).count("1") % 2 == 1]
    one_idx = [1 << a for a in range(5)]

    ev_even_16 = sorted(int(round(v)) for v in np.linalg.eigvalsh(Y6_fock_normal[np.ix_(even_idx, even_idx)]).real)
    ev_odd_16 = sorted(int(round(v)) for v in np.linalg.eigvalsh(Y6_fock_normal[np.ix_(odd_idx, odd_idx)]).real)
    ev_one_5 = sorted(int(round(v)) for v in np.linalg.eigvalsh(Y6_fock_normal[np.ix_(one_idx, one_idx)]).real)

    expected_even_16 = sorted([-4] * 3 + [-3] * 2 + [0] * 1 + [1] * 6 + [2] * 3 + [6] * 1)
    sum_6y_even = sum(ev_even_16)
    sum_6y_cubed_even = sum(q * q * q for q in ev_even_16)

    # Planted PF8.1: wrong-chirality odd projection flips signs (gives -6 instead of +6)
    pf8_1_caught = (ev_odd_16 != expected_even_16) and (-6 in ev_odd_16) and (6 not in ev_odd_16)

    passed = (
        len(grp) == 120
        and s2_err < pow10_f64(-13)
        and st3_err < pow10_f64(-13)
        and max_car_err < pow10_f64(-14)
        and cl10_span_dim == 1024
        and tr_y6 < pow10_f64(-14)
        and normal_vs_weyl_diff < pow10_f64(-14)
        and ev_even_16 == expected_even_16
        and sum_6y_even == 0
        and sum_6y_cubed_even == 0
        and ev_one_5 == [-2, -2, -2, 3, 3]
        and pf8_1_caught
    )
    return {
        "section_1_passed": passed,
        "sl2_f5_group_order": len(grp),
        "weil_S2_minus_P_err": s2_err,
        "weil_ST3_minus_P_err": st3_err,
        "car_anticommutator_max_err": max_car_err,
        "cl10_operator_span_dim": cl10_span_dim,
        "normal_vs_weyl_ordering_diff": normal_vs_weyl_diff,
        "even_fock_16_6Y_charges": ev_even_16,
        "even_fock_sum_6Y": sum_6y_even,
        "even_fock_sum_6Y_cubed": sum_6y_cubed_even,
        "one_particle_5_6Y_charges": ev_one_5,
        "PF8_1_odd_projection_charges": ev_odd_16,
        "PF8_1_caught": pf8_1_caught,
    }


# ============================================================================
# SECTION 2: CONTINUOUS-COLOUR COMMUTANT DICHOTOMY & FROBENIUS-SCHUR (P-863(c))
# ============================================================================

def run_section_2_commutant_dichotomy(T5: np.ndarray, S5: np.ndarray, P5: np.ndarray, grp: List[np.ndarray]) -> Dict[str, Any]:
    evals_P, U_P = np.linalg.eigh(P5)
    idx_desc = np.argsort(-evals_P)
    U_P = U_P[:, idx_desc]

    # Exact Frobenius-Schur indicators (1/|G|) sum_{g in G} chi(g^2) on 3_+ and 2_-
    fs_3_raw = sum(float(np.trace(U_P[:, :3].conj().T @ (G @ G) @ U_P[:, :3]).real) for G in grp) / 120
    fs_2_raw = sum(float(np.trace(U_P[:, 3:].conj().T @ (G @ G) @ U_P[:, 3:]).real) for G in grp) / 120
    fs_3_int = int(round(fs_3_raw))
    fs_2_int = int(round(fs_2_raw))
    fs_err = max(abs(fs_3_raw - 1), abs(fs_2_raw - (-1)))

    # 24-dim real basis of anti-Hermitian traceless su(5)
    su5_basis: List[np.ndarray] = []
    for i in range(5):
        for j in range(i + 1, 5):
            m1 = np.zeros((5, 5), dtype=complex)
            m1[i, j] = frac_f64(1, 1)
            m1[j, i] = frac_f64(-1, 1)
            m2 = np.zeros((5, 5), dtype=complex)
            m2[i, j] = complex(0, 1)
            m2[j, i] = complex(0, 1)
            su5_basis.extend([m1, m2])
    for k in range(1, 5):
        d = np.zeros((5, 5), dtype=complex)
        for r in range(k):
            d[r, r] = complex(0, 1)
        d[k, k] = -complex(0, k)
        su5_basis.append(d)

    cols_full: List[np.ndarray] = []
    cols_centre: List[np.ndarray] = []
    for B in su5_basis:
        c1 = B @ T5 - T5 @ B
        c2 = B @ S5 - S5 @ B
        cols_full.append(np.concatenate([c1.real.ravel(), c1.imag.ravel(), c2.real.ravel(), c2.imag.ravel()]))
        cc = B @ P5 - P5 @ B
        cols_centre.append(np.concatenate([cc.real.ravel(), cc.imag.ravel()]))

    comm_full_dim = 24 - int(np.linalg.matrix_rank(np.column_stack(cols_full), tol=pow10_f64(-10)))
    comm_centre_dim = 24 - int(np.linalg.matrix_rank(np.column_stack(cols_centre), tol=pow10_f64(-10)))

    # Planted PF8.2: non-abelian SU(3)_c generator inside 3_+ commutes with P5, but NOT with S5!
    G_su3_block = np.zeros((5, 5), dtype=complex)
    G_su3_block[0, 1] = frac_f64(1, 1)
    G_su3_block[1, 0] = frac_f64(-1, 1)
    G_su3 = U_P @ G_su3_block @ U_P.conj().T
    comm_P_norm = float(np.linalg.norm(G_su3 @ P5 - P5 @ G_su3))
    comm_S_norm = float(np.linalg.norm(G_su3 @ S5 - S5 @ G_su3))
    pf8_2_caught = (comm_P_norm < pow10_f64(-13)) and (comm_S_norm > frac_f64(1, 2))

    passed = (
        fs_3_int == 1
        and fs_2_int == -1
        and fs_err < pow10_f64(-12)
        and comm_full_dim == 1
        and comm_centre_dim == 12
        and pf8_2_caught
    )
    return {
        "section_2_passed": passed,
        "frobenius_schur_3_plus": fs_3_int,
        "frobenius_schur_2_minus": fs_2_int,
        "frobenius_schur_max_err": fs_err,
        "commutant_dim_full_sl2_f5_in_su5": comm_full_dim,
        "commutant_dim_centre_P_in_su5": comm_centre_dim,
        "PF8_2_su3_comm_with_P_norm": comm_P_norm,
        "PF8_2_su3_comm_with_S_norm": comm_S_norm,
        "PF8_2_caught": pf8_2_caught,
    }


# ============================================================================
# SECTION 3: METALLIC-MEAN FUNDAMENTAL DISCRIMINANTS & RIVAL PRIMES (P-863(d))
# ============================================================================

def squarefree_core(n: int) -> int:
    res = 1
    d = 2
    rem = n
    while d * d <= rem:
        cnt = 0
        while rem % d == 0:
            rem //= d
            cnt += 1
        if cnt % 2 == 1:
            res *= d
        d += 1
    if rem > 1:
        res *= rem
    return res


def fundamental_discriminant(n: int) -> int:
    sf = squarefree_core(n)
    return sf if (sf % 4 == 1) else (4 * sf)


def weil_parity_split(p_odd: int) -> Tuple[int, int]:
    P_p = np.zeros((p_odd, p_odd), dtype=float)
    for x in range(p_odd):
        P_p[x, (-x) % p_odd] = frac_f64(1, 1)
    evs = np.linalg.eigvalsh(P_p)
    n_plus = sum(1 for v in evs if v > 0)
    n_minus = sum(1 for v in evs if v < 0)
    return (n_plus, n_minus)


def run_section_3_metallic_rivals() -> Dict[str, Any]:
    # Metallic polynomial x^2 - k x - 1 = 0 -> raw D_k = k^2 + 4, fundamental field discriminant Delta_K
    metallic_table: List[Dict[str, Any]] = []
    unique_prime_disc_3_2_fields: Set[int] = set()
    for k in range(1, 13):
        raw_d = k * k + 4
        f_disc = fundamental_discriminant(raw_d)
        entry: Dict[str, Any] = {"k": k, "raw_D": raw_d, "fundamental_discriminant": f_disc}
        # Check if f_disc is an odd prime
        is_odd_p = (f_disc > 2) and (f_disc % 2 == 1) and all(f_disc % d != 0 for d in range(3, int(math.isqrt(f_disc)) + 1, 2))
        if is_odd_p:
            sp_pair = weil_parity_split(f_disc)
            entry["weil_split"] = list(sp_pair)
            if sp_pair == (3, 2):
                unique_prime_disc_3_2_fields.add(f_disc)
        metallic_table.append(entry)

    prime_splits = {str(p): list(weil_parity_split(p)) for p in (3, 5, 7, 11, 13, 29)}
    # Note k=4 gives raw_D = 20 = 4 * 5 -> same Golden field Q(sqrt(5)), Delta_K = 5!
    k4_same_golden_field = metallic_table[3]["fundamental_discriminant"] == 5

    # Planted PF8.3: Bronze-mean prime p = 13 (k = 3) gives (7, 6) != (3, 2)
    bronze_split = tuple(prime_splits["13"])
    pf8_3_caught = (bronze_split == (7, 6)) and (bronze_split != (3, 2))

    passed = (
        unique_prime_disc_3_2_fields == {5}
        and k4_same_golden_field
        and prime_splits["5"] == [3, 2]
        and pf8_3_caught
    )
    return {
        "section_3_passed": passed,
        "unique_odd_prime_discriminant_giving_3_2": sorted(unique_prime_disc_3_2_fields),
        "k4_phi_cubed_shares_golden_field_disc_5": k4_same_golden_field,
        "rival_prime_splits": prime_splits,
        "metallic_discriminant_table_k1_to_12": metallic_table,
        "PF8_3_bronze_p13_split": list(bronze_split),
        "PF8_3_caught": pf8_3_caught,
    }


# ============================================================================
# SECTION 4: PRIME-3 FAMILY VS PRIME-5 GAUGE ORTHOGONALITY IN 248D E_8 (P-863(b))
# ============================================================================

def run_section_4_e8_prime3_prime5_orthogonality() -> Dict[str, Any]:
    roots: List[Tuple[int, ...]] = []
    for i in range(8):
        for j in range(i + 1, 8):
            for s1 in (-2, 2):
                for s2 in (-2, 2):
                    v = [0] * 8
                    v[i] = s1
                    v[j] = s2
                    roots.append(tuple(v))
    for mask in range(256):
        signs = [1 if ((mask >> b) & 1) else -1 for b in range(8)]
        if sum(1 for s in signs if s < 0) % 2 == 0:
            roots.append(tuple(signs))

    def dot8(u: Tuple[int, ...], v: Tuple[int, ...]) -> int:
        return sum(a * b for a, b in zip(u, v))

    # A_2^{fam} on coords (0, 1, 2) with sum 0; A_2^{(c)} on coords (3, 4, 5) with sum 0
    a2_fam_simple = [(2, -2, 0, 0, 0, 0, 0, 0), (0, 2, -2, 0, 0, 0, 0, 0)]
    a2_col_simple = [(0, 0, 0, 2, -2, 0, 0, 0), (0, 0, 0, 0, 2, -2, 0, 0)]

    e6_gut_roots = {r for r in roots if dot8(r, a2_fam_simple[0]) == 0 and dot8(r, a2_fam_simple[1]) == 0}
    e6_cent_roots = {r for r in roots if dot8(r, a2_col_simple[0]) == 0 and dot8(r, a2_col_simple[1]) == 0}
    a2_fam_roots = {r for r in roots if r[3:] == (0, 0, 0, 0, 0) and (r[0] + r[1] + r[2] == 0)}
    a2_col_roots = {r for r in roots if r[:3] == (0, 0, 0) and r[6:] == (0, 0) and (r[3] + r[4] + r[5] == 0)}

    inter_e6_roots = e6_gut_roots & e6_cent_roots
    # Cartan dim orthogonal to both 2D A_2 subspaces inside R^8 is 8 - 4 = 4 -> 12 + 4 = 16D (su(3)_L (+) su(3)_R)
    inter_e6_lie_dim = len(inter_e6_roots) + 4

    # G_422 inside E_6^{GUT}: SU(4)_c on coords (3, 4, 5, 6, 7)? Check: D_3 = A_3 on coords (3, 4, 5, 6) + D_2 = SU(2)_L x SU(2)_R!
    # Specifically, inside D_5 subset E_6^{GUT} (integer roots on coords 3..7), G_422 = D_3 (coords 3,4,5 +1? Wait: D_3 has 12 roots ±2 at i,j in {3,4,5} — no, {3,4,5} has 3*2*4/2 = 12 roots, plus {6,7} has 4 roots = D_2 = SU(2)_L x SU(2)_R!)
    # Let's check! Integer roots on {3, 4, 5}: C(3,2)*4 = 12 = dim(SU(4)) - 3! Integer roots on {6, 7}: C(2,2)*4 = 4 = dim(SU(2)_L x SU(2)_R) - 2!
    # Total G_422 roots = 12 + 4 = 16, + 5 Cartans = 21 = 15 + 3 + 3 = dim(SU(4)_c x SU(2)_L x SU(2)_R)!
    g422_roots = {
        r for r in e6_gut_roots
        if (r[:3] == (0, 0, 0) and r[6:] == (0, 0)) or (r[:6] == (0, 0, 0, 0, 0, 0))
    }
    inter_cent_g422_roots = e6_cent_roots & g422_roots
    # Cartans in G_422 (coords 3..7, dim 5) orthogonal to A_2^{(c)} (2 constraints r3-r4=0, r4-r5=0) have dim 5 - 2 = 3 -> 4 + 3 = 7D!
    inter_cent_g422_lie_dim = len(inter_cent_g422_roots) + 3

    # 4-reflection W_swap in W(E_8) cap SO(8): exact order check (order == 4, NOT 2!)
    refl_roots = [
        (2, 0, 0, -2, 0, 0, 0, 0),
        (0, 2, 0, 0, -2, 0, 0, 0),
        (0, 0, 2, 0, 0, -2, 0, 0),
        (0, 0, 0, 0, 0, 0, 2, -2),
    ]
    W_mat = np.eye(8, dtype=int)
    for rr in refl_roots:
        rv = np.array(rr, dtype=int)
        # Reflection I - 2 (r r^T) / (r.r); since r.r = 8, 2/8 = 1/4, and all entries of r are even (+-2, 0), r/2 is integer!
        u_half = rv // 2  # norm^2 = 2, so I - u_half u_half^T is an exact integer matrix!
        R_i = np.eye(8, dtype=int) - np.outer(u_half, u_half)
        W_mat = R_i @ W_mat

    det_w = int(round(float(np.linalg.det(W_mat))))
    w2_is_id = bool(np.array_equal(W_mat @ W_mat, np.eye(8, dtype=int)))
    w4_is_id = bool(np.array_equal(np.linalg.matrix_power(W_mat, 4), np.eye(8, dtype=int)))
    mapped_cent_eq_gut = {tuple((W_mat @ np.array(r, dtype=int)).tolist()) for r in e6_cent_roots} == e6_gut_roots

    # Planted PF8.4: asserting W_swap is an order-2 involution fails (W_swap^2 != I_8)
    pf8_4_caught = (not w2_is_id) and w4_is_id

    # Verify [A_2^{fam}, E_6^{GUT}] == 0 (every root r_f + r_g for r_f in A_2^{fam}, r_g in E_6^{GUT} has norm^2 = 16 > 8, NOT a root!)
    root_set = set(roots)
    comm_fam_gut_nonzero = sum(
        1 for rf in a2_fam_roots for rg in e6_gut_roots
        if tuple(rf[k] + rg[k] for k in range(8)) in root_set
    )
    # Count (3_{fam}, 27_{GUT}) + (3bar_{fam}, 27bar_{GUT}): 162 = 81 + 81 -> 3 generations x 27!
    bifund_count = len(root_set - e6_gut_roots - a2_fam_roots)

    # CRT bijection Z_15 <-> Z_3^{fam} x Z_5^{gauge}
    crt_pairs = {(k % 3, k % 5) for k in range(15)}
    crt_bijection_ok = len(crt_pairs) == 15

    # Planted PF8.5: conflating family A_2 with colour A_2^{(c)} inside E_6^{GUT} gives non-zero root commutators!
    bad_comm_col_col = sum(
        1 for r1 in a2_col_roots for r2 in a2_col_roots
        if tuple(r1[k] + r2[k] for k in range(8)) in root_set
    )
    pf8_5_caught = (comm_fam_gut_nonzero == 0) and (bad_comm_col_col > 0)

    self_dir = Path(__file__).resolve().parent
    repo_root = self_dir.parent.parent
    self_mf = self_dir / "SCRIPT_SHA256.txt"
    self_sha_ok = False
    if self_mf.exists():
        sp = self_mf.read_text(encoding="utf-8").strip().split()
        self_sha_ok = hashlib.sha256((repo_root / sp[1]).read_bytes()).hexdigest() == sp[0]

    passed = (
        len(roots) == 240
        and inter_e6_lie_dim == 16
        and inter_cent_g422_lie_dim == 7
        and det_w == 1
        and mapped_cent_eq_gut
        and pf8_4_caught
        and comm_fam_gut_nonzero == 0
        and bifund_count == 162
        and crt_bijection_ok
        and pf8_5_caught
        and self_sha_ok
    )
    return {
        "section_4_passed": passed,
        "e6_cent_cap_e6_gut_lie_dim": inter_e6_lie_dim,
        "e6_cent_cap_g422_lie_dim": inter_cent_g422_lie_dim,
        "w_swap_det": det_w,
        "w_swap_maps_cent_to_gut": mapped_cent_eq_gut,
        "w_swap_order": 4 if (w4_is_id and not w2_is_id) else 0,
        "PF8_4_involution_claim_caught": pf8_4_caught,
        "comm_a2_fam_with_e6_gut_root_pairs": comm_fam_gut_nonzero,
        "bifundamental_3fam_x_27_plus_conj_count": bifund_count,
        "crt_z15_eq_z3_x_z5_bijection": crt_bijection_ok,
        "PF8_5_conflated_colour_comm_pairs": bad_comm_col_col,
        "PF8_5_caught": pf8_5_caught,
        "self_script_sha256_matched": self_sha_ok,
    }


def main() -> None:
    ast_res = verify_ast_g8()
    T5, S5, P5, grp = build_level5_weil()
    sec1_res = run_section_1_car_fock_postulate_d(T5, S5, P5, grp)
    sec2_res = run_section_2_commutant_dichotomy(T5, S5, P5, grp)
    sec3_res = run_section_3_metallic_rivals()
    sec4_res = run_section_4_e8_prime3_prime5_orthogonality()

    all_planted = (
        sec1_res["PF8_1_caught"]
        and sec2_res["PF8_2_caught"]
        and sec3_res["PF8_3_caught"]
        and sec4_res["PF8_4_involution_claim_caught"]
        and sec4_res["PF8_5_caught"]
    )
    gate_passed = (
        ast_res["ast_gate_passed"]
        and sec1_res["section_1_passed"]
        and sec2_res["section_2_passed"]
        and sec3_res["section_3_passed"]
        and sec4_res["section_4_passed"]
        and all_planted
    )

    out: Dict[str, Any] = {
        "card": "AGY-002_FOUND-G8",
        "empirical_firewall": "0 of 19",
        "gate_8_passed": gate_passed,
        "all_5_planted_faults_caught": all_planted,
        "section_0_ast": ast_res,
        "section_1_car_fock_postulate_d": sec1_res,
        "section_2_commutant_dichotomy": sec2_res,
        "section_3_metallic_rivals": sec3_res,
        "section_4_e8_prime3_prime5_orthogonality": sec4_res,
    }

    out_path = Path(__file__).with_name("verify_found_g8_out.json")
    out_path.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
