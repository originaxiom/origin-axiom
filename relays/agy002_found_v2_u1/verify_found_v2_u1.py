#!/usr/bin/env python3
"""Standalone producer script for Gate F-U1 (AGY-002_FOUND-V2-U1):
Dihedral cover 8^3_4 uniqueness, Riley SL_2(Z[zeta_6]) longitude triviality,
Weyl-hypercharge identity q_{W5} = -(1/2) sum D(v), Berezin-CAR Fock algebra on C^32,
4D collar APS chirality projection, Kawamura SU(5) -> G_SM / Z_6 gauge commutant &
doublet-triplet splitting, and planted fault controls PFU1-1..PFU1-5.

Strict hygiene:
- Zero float or complex AST literals across 100% of module AST.
- Zero repository imports (stdlib + sympy + mpmath + numpy only).
- Zero measured / experimental comparisons (0 of 19).
- Zero Guardrail 2 literal boolean/zero claims: every property computed explicitly.
"""

from __future__ import annotations

import ast
import hashlib
import itertools
import json
import math
import pathlib
import time
from collections import Counter
from typing import Dict, List, Tuple

import mpmath as mp
import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[1]


def mp_rat(num: int, den: int = 1):
    return mp.mpf(int(num)) / mp.mpf(int(den))


def mp_pow10(exp_int: int):
    if exp_int >= 0:
        return mp.mpf(10 ** int(exp_int))
    return mp.mpf(1) / mp.mpf(10 ** int(-exp_int))


def pow10_f(exp_int: int) -> float:
    if exp_int >= 0:
        return int(10 ** int(exp_int)) / int(1)
    return int(1) / int(10 ** int(-exp_int))


# ---------------------------------------------------------------------------
# SECTION 0: Whole-Module AST Zero-Float/Complex Scan & Import/SHA Custody
# ---------------------------------------------------------------------------

def run_section_0_ast_and_custody(self_path: pathlib.Path) -> Dict[str, object]:
    src = self_path.read_text(encoding="utf-8")
    tree = ast.parse(src, filename=str(self_path))
    bad_lits = []
    imported_roots = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, (float, complex)):
            bad_lits.append((node.lineno, repr(node.value)))
        elif isinstance(node, ast.Import):
            for alias in node.names:
                imported_roots.append(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imported_roots.append(node.module.split(".")[0])

    allowed = {
        "__future__", "ast", "hashlib", "itertools", "json", "math",
        "pathlib", "time", "collections", "typing", "mpmath", "sympy", "numpy",
    }
    bad_imports = sorted(set(imported_roots) - allowed)
    rel_self = self_path.relative_to(REPO_ROOT).as_posix()
    actual_sha = hashlib.sha256(self_path.read_bytes()).hexdigest()

    sha_file = HERE / "SCRIPT_SHA256.txt"
    sha_matched = False
    if sha_file.is_file():
        tokens = sha_file.read_text(encoding="utf-8").strip().split()
        if len(tokens) >= 2 and tokens[0] == actual_sha and tokens[1] == rel_self:
            sha_matched = True

    ok = len(bad_lits) == 0 and len(bad_imports) == 0 and sha_matched
    return {
        "section_0_passed": ok,
        "float_literal_count": sum(1 for _, v in bad_lits if "j" not in v),
        "complex_literal_count": sum(1 for _, v in bad_lits if "j" in v),
        "bad_imports": bad_imports,
        "script_sha256_matched": sha_matched,
        "script_sha256": actual_sha,
    }


# ---------------------------------------------------------------------------
# SECTION 1: Dihedral Cover 8^3_4 Uniqueness, Riley SL_2(Z[zeta_6]), & Weyl-6Y
# ---------------------------------------------------------------------------

def _dn_mul(g1: Tuple[int, int], g2: Tuple[int, int], n: int) -> Tuple[int, int]:
    return ((g1[0] + g1[1] * g2[0]) % n, g1[1] * g2[1])


def _dn_inv(g: Tuple[int, int], n: int) -> Tuple[int, int]:
    return ((-g[1] * g[0]) % n, g[1])


def _compose_perm(p1: Tuple[int, ...], p2: Tuple[int, ...]) -> Tuple[int, ...]:
    return tuple(p1[i] for i in p2)


def run_section_1_dihedral_cover_and_weyl() -> Dict[str, object]:
    # 1.1: Enumerate all homomorphisms pi_1(m004) = <x, y | w x = y w>, w = x^-1 y x y^-1 -> D_n
    odd_ns = list(range(3, 33, 2))
    surj_counts = {}
    x_map = (0, -1)
    for n in odd_ns:
        valid_surj = []
        for k in range(n):
            y_map = (k, -1)
            w_map = _dn_mul(_dn_mul(_dn_inv(x_map, n), y_map, n), _dn_mul(x_map, _dn_inv(y_map, n), n), n)
            if _dn_mul(w_map, x_map, n) == _dn_mul(y_map, w_map, n):
                if math.gcd(k, n) == 1:
                    valid_surj.append(k)
        surj_counts[str(n)] = len(valid_surj)

    unique_n5 = (
        surj_counts["5"] == 4
        and all(surj_counts[str(n)] == 0 for n in odd_ns if n != 5)
    )

    # 1.2: Exact Riley SL_2(Z[zeta_6]) verification of relation and canonical longitude
    u_r = sp.Rational(1, 2) + sp.I * sp.sqrt(3) / 2
    X_r = sp.Matrix([[1, 1], [0, 1]])
    Y_r = sp.Matrix([[1, 0], [u_r, 1]])
    W_r = X_r.inv() * Y_r * X_r * Y_r.inv()
    riley_rel_zero = sp.simplify(W_r * X_r - Y_r * W_r) == sp.zeros(2, 2)

    lam_word = [1, -1, -1, 1, 1, -1, -1, 1]  # y x^-1 y^-1 x^2 y^-1 x^-1 y
    exp_sum_lam = sum(lam_word)
    lam_r = Y_r * X_r.inv() * Y_r.inv() * (X_r ** 2) * Y_r.inv() * X_r.inv() * Y_r
    lam_r = sp.simplify(lam_r)
    lam_commutes_riley = sp.simplify(lam_r * X_r - X_r * lam_r) == sp.zeros(2, 2)
    lam_expected = sp.Matrix([[-1, 2 * sp.sqrt(3) * sp.I], [0, -1]])
    lam_riley_exact = sp.simplify(lam_r - lam_expected) == sp.zeros(2, 2)

    # 1.3: Action on 5 sheets (k = 1 in D_5): meridian x5 = (0, -1), y5 = (1, -1)
    x5 = (0, -1)
    y5 = (1, -1)
    act5 = lambda g, j: (g[0] + g[1] * j) % 5
    P_perm = tuple(act5(x5, j) for j in range(5))
    lam_d5 = (0, 1)
    for g5 in [y5, _dn_inv(x5, 5), _dn_inv(y5, 5), x5, x5, _dn_inv(y5, 5), _dn_inv(x5, 5), y5]:
        lam_d5 = _dn_mul(lam_d5, g5, 5)
    lam_perm = tuple(act5(lam_d5, j) for j in range(5))

    # Peripheral <x, lambda>-orbits on {0,1,2,3,4}
    visited = set()
    orbit_sizes = []
    for j in range(5):
        if j in visited:
            continue
        comp = set([j])
        stack = [j]
        while stack:
            cur = stack.pop()
            for nxt in (P_perm[cur], lam_perm[cur]):
                if nxt not in comp:
                    comp.add(nxt)
                    stack.append(nxt)
        visited |= comp
        orbit_sizes.append(len(comp))
    orbit_sizes.sort()

    # S_5 centralizers of full D_5 and index-2 rotation subgroup Z_5
    s5 = list(itertools.permutations(range(5)))
    gen_x_perm = tuple((0 - j) % 5 for j in range(5))
    gen_r_perm = tuple((j + 1) % 5 for j in range(5))
    cent_d5 = [
        p for p in s5
        if _compose_perm(p, gen_x_perm) == _compose_perm(gen_x_perm, p)
        and _compose_perm(p, gen_r_perm) == _compose_perm(gen_r_perm, p)
    ]
    cent_z5 = [p for p in s5 if _compose_perm(p, gen_r_perm) == _compose_perm(gen_r_perm, p)]

    # 1.4: Explicit SymPy Weyl algebra and Hypercharge Identity q_{W5} = -(1/2) sum D(v)
    zeta5 = sp.exp(2 * sp.pi * sp.I / 5)
    X5 = sp.zeros(5, 5)
    Z5 = sp.zeros(5, 5)
    P5 = sp.zeros(5, 5)
    for j in range(5):
        X5[(j + 1) % 5, j] = sp.Integer(1)
        Z5[j, j] = zeta5 ** j
        P5[(-j) % 5, j] = sp.Integer(1)

    weyl_comm_zero = sp.simplify(X5 * Z5 - (zeta5 ** -1) * Z5 * X5) == sp.zeros(5, 5)

    def D5_sym(a: int, b: int):
        return (zeta5 ** ((3 * a * b) % 5)) * (X5 ** (a % 5)) * (Z5 ** (b % 5))

    pts_24 = [(a, b) for a in range(5) for b in range(5) if (a, b) != (0, 0)]
    D_list = [D5_sym(a, b) for a, b in pts_24]
    max_ortho_err = 0
    # Verify numerically at 50 digits AND symbolically on P-eigenbasis B_5 = [B_3 | B_2]
    mp.mp.dps = 50
    iu = mp.mpc(0, 1)
    z5_mp = mp.exp(2 * iu * mp.pi / 5)
    X5_mp = mp.zeros(5, 5)
    Z5_mp = mp.zeros(5, 5)
    P5_mp = mp.zeros(5, 5)
    for j in range(5):
        X5_mp[(j + 1) % 5, j] = mp.mpf(1)
        Z5_mp[j, j] = z5_mp ** j
        P5_mp[(-j) % 5, j] = mp.mpf(1)

    def mat_pow_mp(M, k: int):
        R = mp.eye(M.rows)
        for _ in range(k % 5):
            R = R * M
        return R

    D_mp = [
        (z5_mp ** ((3 * a * b) % 5)) * mat_pow_mp(X5_mp, a) * mat_pow_mp(Z5_mp, b)
        for a, b in pts_24
    ]
    ortho_err_mp = mp.mpf(0)
    tr_dp_err_mp = mp.mpf(0)
    sum_D_mp = mp.zeros(5, 5)
    for idx_i, Di in enumerate(D_mp):
        sum_D_mp += Di
        tr_p = sum((Di * P5_mp)[r, r] for r in range(5))
        tr_dp_err_mp = max(tr_dp_err_mp, abs(tr_p - mp.mpf(1)))
        for idx_j, Dj in enumerate(D_mp):
            ip = sum((Di.T.conjugate() * Dj)[r, r] for r in range(5)) / mp.mpf(5)
            target = mp.mpf(1) if idx_i == idx_j else mp.mpf(0)
            ortho_err_mp = max(ortho_err_mp, abs(ip - target))

    # P-eigenbasis B_5 = [B_3^+ | B_2^-]
    inv_r2 = mp.mpf(1) / mp.sqrt(mp.mpf(2))
    B5_mp = mp.matrix([
        [1, 0, 0, 0, 0],
        [0, inv_r2, 0, inv_r2, 0],
        [0, 0, inv_r2, 0, inv_r2],
        [0, 0, inv_r2, 0, -inv_r2],
        [0, inv_r2, 0, -inv_r2, 0],
    ])
    B5_unitary_err = max(
        abs((B5_mp.T.conjugate() * B5_mp - mp.eye(5))[r, c])
        for r in range(5) for c in range(5)
    )
    P_diag_mp = B5_mp.T.conjugate() * P5_mp * B5_mp
    P_target_mp = mp.diag([mp.mpf(1), mp.mpf(1), mp.mpf(1), mp.mpf(-1), mp.mpf(-1)])
    P_diag_err = max(abs((P_diag_mp - P_target_mp)[r, c]) for r in range(5) for c in range(5))

    qW5_eigbasis_mp = mp_rat(-1, 2) * (B5_mp.T.conjugate() * sum_D_mp * B5_mp)
    qW5_target_mp = mp.diag([mp.mpf(-2), mp.mpf(-2), mp.mpf(-2), mp.mpf(3), mp.mpf(3)])
    qW5_ident_err = max(abs((qW5_eigbasis_mp - qW5_target_mp)[r, c]) for r in range(5) for c in range(5))

    # Exact SymPy verification of -(1/2) sum_{v!=0} D(v) = (5 I_5 - 5 P5?) Wait: check 5/2 * (-P5?) ->
    # On (+1, +1, +1, -1, -1), -2 = (1/2) - (5/2)*(+1), +3 = (1/2) - (5/2)*(-1)!
    # That is: -(1/2) sum D(v) = (1/2) I_5 - (5/2) P5! Let's check symbolically in SymPy!
    sum_D_sym = sum(D_list, sp.zeros(5, 5))
    qW5_formula_exact = sp.simplify(sp.Rational(-1, 2) * sum_D_sym - (sp.Rational(1, 2) * sp.eye(5) - sp.Rational(5, 2) * P5)) == sp.zeros(5, 5)
    inv_r2_s = 1 / sp.sqrt(2)
    B5_sym = sp.Matrix([
        [1, 0, 0, 0, 0],
        [0, inv_r2_s, 0, inv_r2_s, 0],
        [0, 0, inv_r2_s, 0, inv_r2_s],
        [0, 0, inv_r2_s, 0, -inv_r2_s],
        [0, inv_r2_s, 0, -inv_r2_s, 0],
    ])
    qW5_diag_exact = sp.simplify(
        sp.Rational(-1, 2) * (B5_sym.H * sum_D_sym * B5_sym)
        - sp.diag(-2, -2, -2, 3, 3)
    ) == sp.zeros(5, 5)

    tol35 = mp_pow10(-35)
    sec1_passed = (
        unique_n5
        and riley_rel_zero
        and exp_sum_lam == 0
        and lam_commutes_riley
        and lam_riley_exact
        and lam_perm == (0, 1, 2, 3, 4)
        and orbit_sizes == [1, 2, 2]
        and len(cent_d5) == 1
        and len(cent_z5) == 5
        and weyl_comm_zero
        and ortho_err_mp < tol35
        and tr_dp_err_mp < tol35
        and B5_unitary_err < tol35
        and P_diag_err < tol35
        and qW5_ident_err < tol35
        and qW5_formula_exact
        and qW5_diag_exact
    )
    return {
        "section_1_passed": bool(sec1_passed),
        "surjective_Dn_counts_odd_3_to_31": surj_counts,
        "riley_rel_zero": bool(riley_rel_zero),
        "longitude_exp_sum": int(exp_sum_lam),
        "longitude_riley_exact": bool(lam_riley_exact and lam_commutes_riley),
        "longitude_perm_on_5_sheets": list(lam_perm),
        "meridian_perm_on_5_sheets": list(P_perm),
        "peripheral_orbit_sizes": orbit_sizes,
        "centralizer_D5_in_S5_order": len(cent_d5),
        "centralizer_Z5_in_S5_order": len(cent_z5),
        "weyl_XZ_relation_exact": bool(weyl_comm_zero),
        "weyl_orthonormality_err_mp50": str(ortho_err_mp),
        "tr_D_P_equals_1_err_mp50": str(tr_dp_err_mp),
        "qW5_closed_form_half_I_minus_5half_P_exact": bool(qW5_formula_exact),
        "qW5_eigenbasis_diag_m2m2m2p3p3_exact": bool(qW5_diag_exact),
        "qW5_eigenbasis_err_mp50": str(qW5_ident_err),
    }


# ---------------------------------------------------------------------------
# SECTION 2: Berezin-CAR Fock Algebra, APS Chirality, su(5)^P, & Doublet-Triplet
# ---------------------------------------------------------------------------

def _build_fock_operators(n_modes: int):
    """Explicit Jordan-Wigner operators c_a, c_a^dag on C^(2^n_modes)."""
    dim = 1 << n_modes
    c_ops = []
    cdag_ops = []
    for a in range(n_modes):
        c_a = sp.zeros(dim, dim)
        for state in range(dim):
            if (state >> a) & 1:
                parity_below = sum((state >> k) & 1 for k in range(a))
                sgn = 1 if (parity_below % 2 == 0) else -1
                c_a[state ^ (1 << a), state] = sp.Integer(sgn)
        c_ops.append(c_a)
        cdag_ops.append(c_a.T)
    return c_ops, cdag_ops


def _matrix_perm_det_sympy(M: sp.Matrix):
    """Exact Berezin Grassmann Gaussian integral sum_{sigma in S_n} sgn(sigma) prod_i M[i, sigma(i)]."""
    n = M.rows
    total = sp.Integer(0)
    for perm in itertools.permutations(range(n)):
        inv_cnt = sum(1 for i in range(n) for j in range(i + 1, n) if perm[i] > perm[j])
        sgn = 1 if (inv_cnt % 2 == 0) else -1
        prod = sp.Integer(1)
        for i in range(n):
            prod *= M[i, perm[i]]
        total += sgn * prod
    return sp.simplify(total)


def _commutant_basis_and_split(n: int, k_plus: int):
    """Construct explicit hermitian basis of su(n) and compute C_{su(n)}(P) for P=(+1^k_plus, -1^(n-k_plus))."""
    P_diag = sp.diag(*([1] * k_plus + [-1] * (n - k_plus)))
    # Explicit orthonormal hermitian basis of su(n)
    su_gens = []
    for i in range(n):
        for j in range(i + 1, n):
            M_re = sp.zeros(n, n)
            M_re[i, j] = sp.Integer(1)
            M_re[j, i] = sp.Integer(1)
            M_im = sp.zeros(n, n)
            M_im[i, j] = -sp.I
            M_im[j, i] = sp.I
            su_gens.extend([M_re, M_im])
    for m in range(1, n):
        D_m = sp.zeros(n, n)
        for r in range(m):
            D_m[r, r] = sp.Integer(1)
        D_m[m, m] = sp.Integer(-m)
        su_gens.append(D_m)

    dim_su = len(su_gens)
    # Linear map ad_P on coordinates of su_gens: P G - G P == 0 iff commutes with P
    comm_vecs = []
    cols = []
    for G in su_gens:
        C = sp.simplify(P_diag * G - G * P_diag)
        flat = [C[r, c] for r in range(n) for c in range(n)]
        cols.append(flat)
    A_mat = sp.Matrix(cols).T
    ker = A_mat.nullspace()
    dim_comm = len(ker)
    comm_mats = []
    for kv in ker:
        M = sum((kv[i] * su_gens[i] for i in range(dim_su)), sp.zeros(n, n))
        comm_mats.append(sp.simplify(M))
    return dim_su, dim_comm, comm_mats, P_diag


def run_section_2_berezin_aps_kawamura() -> Dict[str, object]:
    # 2.1: Jordan-Wigner CAR on Lambda^*(W_5) = C^32
    c_ops, cdag_ops = _build_fock_operators(5)
    I32 = sp.eye(32)
    car_errs = 0
    for a in range(5):
        for b in range(5):
            ac1 = c_ops[a] * cdag_ops[b] + cdag_ops[b] * c_ops[a]
            if ac1 != (I32 if a == b else sp.zeros(32, 32)):
                car_errs += 1
            if c_ops[a] * c_ops[b] + c_ops[b] * c_ops[a] != sp.zeros(32, 32):
                car_errs += 1
            if cdag_ops[a] * cdag_ops[b] + cdag_ops[b] * cdag_ops[a] != sp.zeros(32, 32):
                car_errs += 1

    # 2.2: Exact Berezin Gaussian integral vs Matrix determinant
    M1 = sp.Matrix([
        [2, 1, 0, -1, 3],
        [0, -1, 2, 1, 0],
        [1, 3, -2, 0, 1],
        [-2, 0, 1, 4, -1],
        [1, -1, 2, 1, 2],
    ])
    M2 = sp.Matrix([
        [1, 2, -1, 0, 1],
        [-1, 3, 1, 2, 0],
        [0, 1, -1, 3, -2],
        [2, 0, 1, -1, 4],
        [-1, 1, 0, 2, 1],
    ])
    ber_M1 = _matrix_perm_det_sympy(M1)
    ber_M2 = _matrix_perm_det_sympy(M2)
    ber_prod = _matrix_perm_det_sympy(M1 * M2)
    berezin_exact_ok = (ber_M1 == M1.det()) and (ber_M2 == M2.det()) and (ber_prod == ber_M1 * ber_M2)

    # 2.3: 4D Collar APS parity operator (-1)^F & chiral correlation gamma_5 (-1)^F = +1
    F_parity = I32
    for a in range(5):
        F_parity = F_parity * (I32 - 2 * cdag_ops[a] * c_ops[a])
    even_indices = [s for s in range(32) if bin(s).count("1") % 2 == 0]
    odd_indices = [s for s in range(32) if bin(s).count("1") % 2 == 1]
    parity_split_ok = (
        len(even_indices) == 16
        and len(odd_indices) == 16
        and all(F_parity[s, s] == 1 for s in even_indices)
        and all(F_parity[s, s] == -1 for s in odd_indices)
        and all(F_parity[r, c] == 0 for r in range(32) for c in range(32) if r != c)
    )

    # 2.4: Kawamura gauge commutant C_{su(5)}(P) and global kernel Z_6
    dim_su5, dim_comm, comm_mats, P5_eig = _commutant_basis_and_split(5, 3)
    # Verify non-abelian block commutators preserve 3x3 and 2x2 separation and center has dim 1
    # Check global kernel in SU(3) x SU(2) x U(1): elements (z3*I3, z2*I2, u) with z3^3=1, z2^2=1, |u|=1
    # mapping to diag(z3*u^-2 * I3, z2*u^3 * I2) = I_5: z3*u^-2 = 1 and z2*u^3 = 1 -> u^6 = 1!
    kernel_elems = []
    for m_exp in range(60):
        u = sp.exp(sp.I * sp.pi * m_exp / 30)  # dense 60th roots check; wait let's check exact 6k roots:
        pass
    # Solve symbolically over z3 = w^a (a=0..2), z2 = (-1)^b (b=0,1), u = exp(2 pi i k / 6):
    # Note u = exp(i pi m / 3), 0<=m<6 -> z3 = u^2, z2 = u^-3 gives z3^3=u^6=1, z2^2=u^-6=1!
    kernel_z6 = []
    for k3 in range(3):
        for k2 in range(2):
            for k6 in range(12):  # test 12th roots; only 6th roots survive!
                z3 = sp.exp(2 * sp.pi * sp.I * k3 / 3)
                z2 = (-1) ** k2
                u = sp.exp(2 * sp.pi * sp.I * k6 / 6)
                if sp.simplify(z3 * (u ** -2) - 1) == 0 and sp.simplify(z2 * (u ** 3) - 1) == 0:
                    kernel_z6.append((k3, k2, k6 % 6))
    kernel_z6 = sorted(set(kernel_z6))
    kernel_order_6 = len(kernel_z6) == 6

    # 2.5: 6Y operator Q_{6Y} on Lambda^{even}(W_5) & SM anomaly cancellation
    qW5_weights = [-2, -2, -2, 3, 3]
    Q_6Y_32 = sp.zeros(32, 32)
    for a in range(5):
        Q_6Y_32 += sp.Integer(qW5_weights[a]) * (cdag_ops[a] * c_ops[a])

    # Extract exact 6Y spectrum on Lambda^{even}(W_5)
    spec_even_6Y = sorted(int(Q_6Y_32[s, s]) for s in even_indices)
    spec_odd_6Y = sorted(int(Q_6Y_32[s, s]) for s in odd_indices)
    expected_even_6Y = sorted([-4, -4, -4, -3, -3, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 6])

    # Verify all 4 SM anomaly traces in units of 6Y
    tr_Y = sum(spec_even_6Y)
    tr_Y3 = sum(y ** 3 for y in spec_even_6Y)
    # Count exact SU(3)_c and SU(2)_L representation quantum numbers per basis state in even_indices
    # Modes 0,1,2 carry 3_c; modes 3,4 carry 2_L. An SU(3) generator T^8 = diag(1, 1, -2) on modes 0,1,2:
    # An SU(2) generator T^3 = diag(1, -1) on modes 3,4:
    T3c_sq = sp.zeros(32, 32)  # use diag(1, -1, 0) on color modes (Tr = 2 = 2 T(fund))
    T3c = sp.Integer(1) * (cdag_ops[0] * c_ops[0]) - sp.Integer(1) * (cdag_ops[1] * c_ops[1])
    T2L = sp.Integer(1) * (cdag_ops[3] * c_ops[3]) - sp.Integer(1) * (cdag_ops[4] * c_ops[4])
    tr_su3_sq_Y = int(sum((T3c * T3c * Q_6Y_32)[s, s] for s in even_indices))
    tr_su2_sq_Y = int(sum((T2L * T2L * Q_6Y_32)[s, s] for s in even_indices))
    tr_su3_sq_check = int(sum((T3c * T3c)[s, s] for s in even_indices))
    tr_su2_sq_check = int(sum((T2L * T2L)[s, s] for s in even_indices))

    # 2.6: Kawamura Doublet-Triplet Splitting on collar-odd scalar Phi_s(-s) = -P Phi_s(s)
    # Zero mode condition: P v = -v => ker(P + I_5) intersected with W_3^+ and W_2^-
    P_plus_I = P5_eig + sp.eye(5)
    Proj_3c = sp.diag(1, 1, 1, 0, 0)
    Proj_2L = sp.diag(0, 0, 0, 1, 1)
    ker_scalar_odd = P_plus_I.nullspace()
    weak_doublet_zero_modes = sum(1 for v in ker_scalar_odd if Proj_2L * v == v)
    color_triplet_zero_modes = sum(1 for v in ker_scalar_odd if Proj_3c * v != sp.zeros(5, 1))

    # Verify weak doublet has 6Y == +3 and antiparticle in W_2^- has +3
    # Wait: in W_5 = 3_{-2} (+) 2_{+3}, W_2^- has 6Y = +3, i.e., Y = +1/2 SM Higgs doublet!
    doublet_6Y_values = [int((sp.diag(*qW5_weights) * v)[3]) if v[3] != 0 else int((sp.diag(*qW5_weights) * v)[4]) for v in ker_scalar_odd]

    sec2_passed = (
        car_errs == 0
        and berezin_exact_ok
        and parity_split_ok
        and dim_su5 == 24
        and dim_comm == 12
        and kernel_order_6
        and spec_even_6Y == expected_even_6Y
        and tr_Y == 0
        and tr_Y3 == 0
        and tr_su3_sq_Y == 0
        and tr_su2_sq_Y == 0
        and tr_su3_sq_check > 0
        and tr_su2_sq_check > 0
        and len(ker_scalar_odd) == 2
        and weak_doublet_zero_modes == 2
        and color_triplet_zero_modes == 0
        and doublet_6Y_values == [3, 3]
    )
    return {
        "section_2_passed": bool(sec2_passed),
        "car_anticommutator_errors": car_errs,
        "berezin_det_exact": bool(berezin_exact_ok),
        "aps_parity_16_16_split_ok": bool(parity_split_ok),
        "dim_su5": dim_su5,
        "dim_commutant_P": dim_comm,
        "global_kernel_Z6_order": len(kernel_z6),
        "spec_even_6Y": spec_even_6Y,
        "anomaly_tr_Y": tr_Y,
        "anomaly_tr_Y3": tr_Y3,
        "anomaly_tr_SU3sq_Y": tr_su3_sq_Y,
        "anomaly_tr_SU2sq_Y": tr_su2_sq_Y,
        "kawamura_weak_doublet_zero_modes": weak_doublet_zero_modes,
        "kawamura_color_triplet_zero_modes": color_triplet_zero_modes,
        "higgs_doublet_6Y_weights": doublet_6Y_values,
    }


# ---------------------------------------------------------------------------
# SECTION 3: Five Non-Vacuous Planted Fault Controls (PFU1-1..PFU1-5)
# ---------------------------------------------------------------------------

def run_section_3_planted_faults() -> Dict[str, object]:
    # PFU1-1: Trefoil 3_1 (<x, y | x y x = y x y> -> D_3, P_3 = (+1^2, -1^1)) with traceless q_{W3} = diag(-1, -1, +2)
    def trefoil_surj_d3():
        cnt = 0
        x = (0, -1)
        for k in range(1, 3):
            y = (k, -1)
            lhs = _dn_mul(_dn_mul(x, y, 3), x, 3)
            rhs = _dn_mul(_dn_mul(y, x, 3), y, 3)
            if lhs == rhs:
                cnt += 1
        return cnt

    trefoil_d3_count = trefoil_surj_d3()
    c3, cdag3 = _build_fock_operators(3)
    even3 = [s for s in range(8) if bin(s).count("1") % 2 == 0]
    qW3_weights = [-1, -1, 2]
    Q3 = sum((sp.Integer(qW3_weights[a]) * (cdag3[a] * c3[a]) for a in range(3)), sp.zeros(8, 8))
    spec_trefoil_even = [int(Q3[s, s]) for s in even3]
    tr3_cubed = sum(y ** 3 for y in spec_trefoil_even)
    pfu1_1_caught = trefoil_d3_count == 2 and tr3_cubed == -6 and tr3_cubed != 0

    # PFU1-2: Bronze rival p = 13 (P_13 = (+1^7, -1^6)) -> dim C_{su(13)}(P) = 84 != 12
    # Wait: computing nullspace of 169x168 symbolic matrix can take ~2s; compute exact block dimensions directly
    # on hermitian 13x13 commutator [P, G] == 0 using explicit off-diagonal/diagonal generators!
    # Wait: let's actually loop over all 13^2 - 1 = 168 explicit generators!
    P13 = sp.diag(*([1] * 7 + [-1] * 6))
    comm13_count = 0
    for i in range(13):
        for j in range(i + 1, 13):
            # M_re and M_im commute with P13 iff P13[i,i] == P13[j,j]
            G_re = sp.zeros(13, 13)
            G_re[i, j] = 1
            G_re[j, i] = 1
            if P13 * G_re - G_re * P13 == sp.zeros(13, 13):
                comm13_count += 2
    for m in range(1, 13):
        G_d = sp.zeros(13, 13)
        for r in range(m):
            G_d[r, r] = 1
        G_d[m, m] = -m
        if P13 * G_d - G_d * P13 == sp.zeros(13, 13):
            comm13_count += 1
    pfu1_2_caught = comm13_count == 84 and comm13_count != 12

    # PFU1-3: Level-25 dihedral cover pi_1(m004) ->> D_25 has 0 surjective maps
    x25 = (0, -1)
    d25_surj = 0
    for k in range(25):
        y25 = (k, -1)
        w25 = _dn_mul(_dn_mul(_dn_inv(x25, 25), y25, 25), _dn_mul(x25, _dn_inv(y25, 25), 25), 25)
        if _dn_mul(w25, x25, 25) == _dn_mul(y25, w25, 25) and math.gcd(k, 25) == 1:
            d25_surj += 1
    pfu1_3_caught = d25_surj == 0

    # PFU1-4: Collar-even scalar parity P Phi_s = +Phi_s leaves 3 colour triplets and 0 weak doublets
    P5_eig = sp.diag(1, 1, 1, -1, -1)
    ker_scalar_even = (P5_eig - sp.eye(5)).nullspace()
    Proj_3c = sp.diag(1, 1, 1, 0, 0)
    Proj_2L = sp.diag(0, 0, 0, 1, 1)
    wrong_color = sum(1 for v in ker_scalar_even if Proj_3c * v == v)
    wrong_doublet = sum(1 for v in ker_scalar_even if Proj_2L * v != sp.zeros(5, 1))
    pfu1_4_caught = wrong_color == 3 and wrong_doublet == 0

    # PFU1-5: Dropping (-1)^F = +1 (keeping full 32D Lambda^*(W_5)) gives vector-like Y <-> -Y symmetry
    c5, cdag5 = _build_fock_operators(5)
    qW5_weights = [-2, -2, -2, 3, 3]
    Q_6Y_32 = sum((sp.Integer(qW5_weights[a]) * (cdag5[a] * c5[a]) for a in range(5)), sp.zeros(32, 32))
    full_32_spec = Counter(int(Q_6Y_32[s, s]) for s in range(32))
    even_spec = Counter(int(Q_6Y_32[s, s]) for s in range(32) if bin(s).count("1") % 2 == 0)
    full_is_vectorlike = all(full_32_spec[y] == full_32_spec[-y] for y in full_32_spec)
    even_is_chiral = not all(even_spec[y] == even_spec[-y] for y in even_spec)
    pfu1_5_caught = full_is_vectorlike and even_is_chiral

    all_5_caught = pfu1_1_caught and pfu1_2_caught and pfu1_3_caught and pfu1_4_caught and pfu1_5_caught
    return {
        "all_5_planted_faults_caught": bool(all_5_caught),
        "PFU1_1_trefoil_surj_D3": trefoil_d3_count,
        "PFU1_1_trefoil_even_6Y": spec_trefoil_even,
        "PFU1_1_trefoil_tr_Y3": tr3_cubed,
        "PFU1_1_caught": bool(pfu1_1_caught),
        "PFU1_2_p13_commutant_dim": comm13_count,
        "PFU1_2_caught": bool(pfu1_2_caught),
        "PFU1_3_d25_surj_count": d25_surj,
        "PFU1_3_caught": bool(pfu1_3_caught),
        "PFU1_4_even_scalar_color_modes": wrong_color,
        "PFU1_4_even_scalar_doublet_modes": wrong_doublet,
        "PFU1_4_caught": bool(pfu1_4_caught),
        "PFU1_5_full32_vectorlike": bool(full_is_vectorlike),
        "PFU1_5_even16_chiral": bool(even_is_chiral),
        "PFU1_5_caught": bool(pfu1_5_caught),
    }


def main() -> None:
    t0 = time.time()
    self_path = pathlib.Path(__file__).resolve()
    s0 = run_section_0_ast_and_custody(self_path)
    assert s0["section_0_passed"], f"Section 0 failed: {s0}"
    s1 = run_section_1_dihedral_cover_and_weyl()
    s2 = run_section_2_berezin_aps_kawamura()
    s3 = run_section_3_planted_faults()
    gate_passed = (
        s0["section_0_passed"]
        and s1["section_1_passed"]
        and s2["section_2_passed"]
        and s3["all_5_planted_faults_caught"]
    )
    payload = {
        "card": "AGY-002_FOUND-V2-U1",
        "empirical_firewall": "0 of 19",
        "gate_f_u1_passed": bool(gate_passed),
        "runtime_seconds_int": int(round(time.time() - t0)),
        "section_0_ast_and_custody": s0,
        "section_1_dihedral_cover_and_weyl": s1,
        "section_2_berezin_aps_kawamura": s2,
        "section_3_planted_faults": s3,
    }
    out_path = HERE / "verify_found_v2_u1_out.json"
    out_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
