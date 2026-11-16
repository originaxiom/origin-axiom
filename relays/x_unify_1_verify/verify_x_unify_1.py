#!/usr/bin/env python3
"""
Standalone Zero-Import Verifier for Card X-UNIFY-1:
  Part 1A: CRT Gauge x Family Tensor Unification (W_15 ~= W_5^{gauge} (x) W_3^{family}),
           Anomaly-Forced Hypercharge (3a + 2b = 0 => k_2/k_1 = 3/5), Cusp Spin Registration,
           and Classical Generator Trace-Norm c_H = kappa(H^2) Restoration.
  Part 1B: First-Ever Independent Zero-Import Scientific Execution & Countercheck of All 12
           Mathematical Methods Sealed in physical's P-C3 Package (ca02b5d8d).

Empirical Firewall: 0 of 19 (zero Standard Model empirical values read, imported, or compared;
zero float literals in the entire script; zero repository imports).
"""

from __future__ import annotations

import ast
from fractions import Fraction
import hashlib
from itertools import product
import json
import math
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple

import mpmath as mp
import sympy as sp


# ============================================================================
# SECTION 0: AST SOURCE AUDIT (ZERO IMPORTS & ZERO FLOAT LITERALS MODULE-WIDE)
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


def verify_ast_unify1() -> Dict[str, Any]:
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
    passed = len(disallowed) == 0 and float_literals == 0 and complex_literals == 0
    return {
        "Gate_AST_Stage1_Unify_Passed": passed,
        "imported_top_modules": sorted(mods),
        "disallowed_imports_count": len(disallowed),
        "float_literals_module_wide": float_literals,
        "complex_literals_module_wide": complex_literals,
        "zero_imports_from_repo_or_reports": len(disallowed) == 0,
    }


# ============================================================================
# SECTION 1: PART 1A — CRT W_15 ~= W_5 (x) W_3, ANOMALY HYPERCHARGE LOCK,
#                      CUSP SPIN REGISTRATION, & c_H TYPE RESTORATION
# ============================================================================

def build_weil_generators_mp(n_dim: int, mult_r: int) -> Tuple[Any, Any]:
    """Finite Weil generators T_N^{(r)} and S_N^{(r)} on l^2(Z/NZ) in mpmath."""
    t_mat = mp.zeros(n_dim, n_dim)
    s_mat = mp.zeros(n_dim, n_dim)
    inv_sqrt = mp.mpf(1) / mp.sqrt(mp.mpf(n_dim))
    two_pi_i = mp.mpc(0, 2) * mp.pi
    for x in range(n_dim):
        t_mat[x, x] = mp.exp(two_pi_i * mp.mpf((mult_r * x * x) % n_dim) / mp.mpf(n_dim))
        for y in range(n_dim):
            s_mat[x, y] = inv_sqrt * mp.exp(-two_pi_i * mp.mpf((mult_r * x * y) % n_dim) / mp.mpf(n_dim))
    return t_mat, s_mat


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


def run_part_1a_crt_gauge_family_and_anomaly() -> Dict[str, Any]:
    # 1. Exact Smith invariants of M^4 - I_2 on m004's 4-fold punctured cover:
    m_mon = sp.Matrix([[2, 1], [1, 1]])
    m4_minus_i = m_mon ** 4 - sp.eye(2)
    det_m4 = int(m4_minus_i.det())
    g1 = math.gcd(
        math.gcd(abs(int(m4_minus_i[0, 0])), abs(int(m4_minus_i[0, 1]))),
        math.gcd(abs(int(m4_minus_i[1, 0])), abs(int(m4_minus_i[1, 1]))),
    )
    smith_invariants = [g1, abs(det_m4) // g1]

    # 2. 55-digit CRT Weil tensor factorization W_15 ~= W_5^{(3)} (x) W_3^{(2)}:
    with mp.workdps(55):
        t15, s15 = build_weil_generators_mp(15, 1)
        t5_3, s5_3 = build_weil_generators_mp(5, 3)
        t3_2, s3_2 = build_weil_generators_mp(3, 2)

        # Unitary CRT permutation P_CRT |3u + 5v mod 15> = |u>_5 (x) |v>_3:
        p_crt = mp.zeros(15, 15)
        for u in range(5):
            for v in range(3):
                x15 = (3 * u + 5 * v) % 15
                row_idx = 3 * u + v
                p_crt[row_idx, x15] = mp.mpf(1)

        unit_crt_err = mp.mnorm(p_crt * p_crt.transpose_conj() - mp.eye(15), "F")
        t_prod = kron_mp(t5_3, t3_2)
        s_prod = kron_mp(s5_3, s3_2)
        t_crt_err = mp.mnorm(p_crt * t15 * p_crt.transpose_conj() - t_prod, "F")
        s_crt_err = mp.mnorm(p_crt * s15 * p_crt.transpose_conj() - s_prod, "F")

        # Planted control PC_U1_NonCoprimeLevel9Failure: N = 9 = 3 x 3 (gcd(3, 3) = 3 != 1)
        # No tensor product A_3 (x) B_3 of diagonal unitary 3x3 matrices can equal T_9^{(1)} under x = u + 3v!
        t9, _ = build_weil_generators_mp(9, 1)
        # Under reshape D_{u, v} = T_9[u + 3v, u + 3v], tensor factorization requires rank-1 3x3 matrix D_{u,v}:
        d9_uv = mp.zeros(3, 3)
        for u in range(3):
            for v in range(3):
                x9 = (u + 3 * v) % 9
                d9_uv[u, v] = t9[x9, x9]
        # Wait: for x = u + 3v, x^2 = u^2 + 6 u v + 9 v^2 == u^2 + 6 u v mod 9!
        # Let's compute singular values of D_{u,v}: rank-1 tensor product would have sv_0 = sv_1 = 0!
        sv_d9 = sorted([mp.re(val) for val in mp.svd_c(d9_uv, compute_uv=False)])
        pc_level9_nonfactor_err = float(mp.sqrt(sv_d9[0] ** 2 + sv_d9[1] ** 2))

        # Parity C_5 = (S_5^{(3)})^2 on W_5 splits W_5 = 3_c (+) 2_w:
        c5 = s5_3 * s5_3
        proj_plus = (mp.eye(5) + c5) / mp.mpf(2)
        proj_minus = (mp.eye(5) - c5) / mp.mpf(2)
        dim_3c = int(mp.nint(mp.re(sum(proj_plus[k, k] for k in range(5)))))
        dim_2w = int(mp.nint(mp.re(sum(proj_minus[k, k] for k in range(5)))))

    # Exact symbolic commutator check between End(W_5) (x) I_3 (gauge) and I_5 (x) End(W_3) (family):
    # Verify across a complete basis of sl_5 (x) I_3 and Heisenberg H_3 generators X_3, Z_3 on W_3:
    omega3 = sp.exp(2 * sp.pi * sp.I / 3)
    z3_fam = sp.diag(1, omega3, omega3 ** 2)
    x3_fam = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    c5_sym = sp.Matrix([
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0],
    ])
    # Orthonormal basis U_5 diagonalizing C_5 into (+1, +1, +1, -1, -1):
    is2 = 1 / sp.sqrt(2)
    u5_split = sp.Matrix([
        [1, 0, 0, 0, 0],
        [0, is2, 0, 0, is2],
        [0, 0, is2, is2, 0],
        [0, is2, 0, 0, -is2],
        [0, 0, is2, -is2, 0],
    ])
    c5_diag = sp.simplify(u5_split * c5_sym * u5_split.H)
    h_hyper_diag = sp.diag(-2, -2, -2, 3, 3)
    h_hyper_w5 = sp.simplify(u5_split.H * h_hyper_diag * u5_split)
    gauge_gen_15 = sp.kronecker_product(h_hyper_w5, sp.eye(3))
    fam_x_15 = sp.kronecker_product(sp.eye(5), x3_fam)
    fam_z_15 = sp.kronecker_product(sp.eye(5), z3_fam)
    comm_x_zero = sp.simplify(gauge_gen_15 * fam_x_15 - fam_x_15 * gauge_gen_15) == sp.zeros(15, 15)
    comm_z_zero = sp.simplify(gauge_gen_15 * fam_z_15 - fam_z_15 * gauge_gen_15) == sp.zeros(15, 15)

    # Even exterior algebra dimension sum_{k in {0, 2, 4}} C(5, k) = 1 + 10 + 5 = 16, times 3 families = 48:
    even_ext_dims = [math.comb(5, 0), math.comb(5, 2), math.comb(5, 4)]
    dim_one_gen = sum(even_ext_dims)
    dim_three_fam = 3 * dim_one_gen

    # 3. Exact 4-anomaly hypercharge polynomial factorization on Lambda^{even}(W_5):
    a_sym, b_sym = sp.symbols("a b", real=True)
    # Multiplets of Lambda^{even}(3_a (+) 2_b):
    # deg 0: (1, 1)_0 [mult 1]
    # deg 2: (3bar, 1)_{2a} [mult 3], (3, 2)_{a+b} [mult 6], (1, 1)_{2b} [mult 1]
    # deg 4: (1, 2)_{3a+b} [mult 2], (3bar, 1)_{2a+2b} [mult 3]
    a_su3_sq_u1 = sp.expand(sp.Rational(1, 2) * (2 * (a_sym + b_sym) + 2 * a_sym + (2 * a_sym + 2 * b_sym)))
    a_su2_sq_u1 = sp.expand(sp.Rational(1, 2) * (3 * (a_sym + b_sym) + (3 * a_sym + b_sym)))
    a_grav_sq_u1 = sp.expand(6 * (a_sym + b_sym) + 3 * (2 * a_sym) + (2 * b_sym) + 3 * (2 * a_sym + 2 * b_sym) + 2 * (3 * a_sym + b_sym))
    a_u1_cubed = sp.expand(
        6 * (a_sym + b_sym) ** 3
        + 3 * (2 * a_sym) ** 3
        + (2 * b_sym) ** 3
        + 3 * (2 * a_sym + 2 * b_sym) ** 3
        + 2 * (3 * a_sym + b_sym) ** 3
    )
    a_u1_cubed_expected = sp.expand(4 * (3 * a_sym + 2 * b_sym) * ((3 * a_sym + b_sym) ** 2 + 4 * b_sym ** 2))
    cubic_factorization_exact = (sp.simplify(a_u1_cubed - a_u1_cubed_expected) == 0)

    # Evaluate at primitive integral solution (a, b) = (-2, 3) => Y = Q / 6:
    sol_sub = {a_sym: -2, b_sym: 3}
    anom_at_sm = [
        int(a_su3_sq_u1.subs(sol_sub)),
        int(a_su2_sq_u1.subs(sol_sub)),
        int(a_grav_sq_u1.subs(sol_sub)),
        int(a_u1_cubed.subs(sol_sub)),
    ]
    # Dynkin ratio Tr_{16}(Y^2) / Tr_{16}(T_{3L}^2) at Y = Q / 6:
    q_mults = [
        (6, Fraction(1, 6)),      # (3, 2)_{+1/6}
        (3, Fraction(-4, 6)),     # (3bar, 1)_{-2/3}
        (1, Fraction(6, 6)),      # (1, 1)_{+1}
        (3, Fraction(2, 6)),      # (3bar, 1)_{+1/3}
        (2, Fraction(-3, 6)),     # (1, 2)_{-1/2}
        (1, Fraction(0, 6)),      # (1, 1)_0
    ]
    tr_y2 = sum(mult * (yv * yv) for mult, yv in q_mults)
    # T_{3L} = diag(+1/2, -1/2) on 3 colour + 1 uncoloured = 4 weak doublets => Tr(T_{3L}^2) = 4 * (1/4 + 1/4) = 2:
    tr_t3l_sq = Fraction(4, 1) * (Fraction(1, 4) + Fraction(1, 4))
    k2_over_k1 = tr_t3l_sq / tr_y2

    # Planted control PC_U1_UnbalancedHyperchargeAnomaly at (a, b) = (-1, 1):
    bad_sub = {a_sym: -1, b_sym: 1}
    pc_unbalanced_cubic = abs(int(a_u1_cubed.subs(bad_sub)))

    # 4. Codex X_BRIDGE_INTAKE Point 1: Classical trace-norm c_H = kappa(H^2) vs seam stiffness kappa_seam:
    p_seam, r_maxw, n_flux = sp.symbols("p_seam r_maxw n_flux", positive=True)
    # Finite-cell Schur complement E(n) = (r p / (r + p)) * (2 pi n)^2 / 2; stiff-seam limit p_seam -> oo gives r * (2 pi n)^2 / 2
    # where r = c_H / (G Area) depends ONLY on classical c_H = Tr(H^2), with d/d(p_seam) lim_{p->oo} = 0!
    e_schur = sp.Rational(1, 2) * (r_maxw * p_seam / (r_maxw + p_seam)) * (2 * sp.pi * n_flux) ** 2
    e_stiff_limit = sp.limit(e_schur, p_seam, sp.oo)
    seam_indep_in_limit = (sp.diff(e_stiff_limit, p_seam) == 0) and (
        sp.simplify(e_stiff_limit - 2 * sp.pi ** 2 * r_maxw * n_flux ** 2) == 0
    )
    c_h_6y_trace_norm = int((h_hyper_diag * h_hyper_diag).trace())  # Tr((6Y)^2) = 3*4 + 2*9 = 30; Tr(Y^2) = 30/36 = 5/6

    # 5. Untwisted integer registration m in Z vs half-integral antiperiodic spin registration q = r - 1/2:
    untwisted_vals = {m: Fraction(m * m, 1) for m in range(-2, 3)}
    half_spin_vals = {f"{r}-1/2": (Fraction(r, 1) - Fraction(1, 2)) ** 2 for r in range(-2, 4)}
    min_untwisted = min(untwisted_vals.values())
    min_half_spin = min(half_spin_vals.values())
    half_spin_minima_count = sum(1 for v in half_spin_vals.values() if v == min_half_spin)

    e1_passed = bool(
        smith_invariants == [3, 15]
        and float(unit_crt_err) < float(Fraction(1, 10 ** 45))
        and float(t_crt_err) < float(Fraction(1, 10 ** 45))
        and float(s_crt_err) < float(Fraction(1, 10 ** 45))
        and pc_level9_nonfactor_err > 1
        and dim_3c == 3
        and dim_2w == 2
        and c5_diag == sp.diag(1, 1, 1, -1, -1)
        and comm_x_zero
        and comm_z_zero
        and dim_one_gen == 16
        and dim_three_fam == 48
        and cubic_factorization_exact
        and anom_at_sm == [0, 0, 0, 0]
        and k2_over_k1 == Fraction(3, 5)
        and pc_unbalanced_cubic >= 32
        and seam_indep_in_limit
        and c_h_6y_trace_norm == 30
        and min_untwisted == Fraction(0, 1)
        and min_half_spin == Fraction(1, 4)
        and half_spin_minima_count == 2
    )

    return {
        "E1_CRT_GaugeFamily_and_Anomaly_Gate_passed": e1_passed,
        "smith_invariants_4fold_punctured_cover": smith_invariants,
        "crt_weil_tensor_factorization_55dps": {
            "unitarity_err": float(unit_crt_err),
            "T15_vs_T5_kron_T3_frob_err": float(t_crt_err),
            "S15_vs_S5_kron_S3_frob_err": float(s_crt_err),
            "PC_U1_NonCoprimeLevel9Failure_non_rank1_sv_norm": pc_level9_nonfactor_err,
            "W5_parity_split_dims": [dim_3c, dim_2w],
            "even_exterior_dims_deg_0_2_4": even_ext_dims,
            "one_generation_weyl_dim": dim_one_gen,
            "three_commuting_family_weyl_dim": dim_three_fam,
            "gauge_commutes_with_H3_family_exact": bool(comm_x_zero and comm_z_zero),
        },
        "anomaly_forced_hypercharge": {
            "A_SU3_sq_U1_formula": str(a_su3_sq_u1),
            "A_SU2_sq_U1_formula": str(a_su2_sq_u1),
            "A_grav_sq_U1_formula": str(a_grav_sq_u1),
            "A_U1_cubed_factored": "4*(3*a + 2*b)*((3*a + b)**2 + 4*b**2)",
            "cubic_factorization_exact": cubic_factorization_exact,
            "anomalies_at_a_neg2_b_3": anom_at_sm,
            "derived_k2_over_k1": str(k2_over_k1),
            "PC_U1_UnbalancedHyperchargeAnomaly_abs_cubic_at_neg1_1": pc_unbalanced_cubic,
        },
        "c_H_and_spin_registration_audit": {
            "c_H_classical_6Y_trace_norm": c_h_6y_trace_norm,
            "c_H_normalized_Y_trace_norm": "5/6",
            "stiff_seam_limit_independent_of_kappa_seam": seam_indep_in_limit,
            "untwisted_integer_min_energy_unit_sq": str(min_untwisted),
            "antiperiodic_half_spin_min_energy_unit_sq": str(min_half_spin),
            "antiperiodic_half_spin_degenerate_minima_count": half_spin_minima_count,
            "honest_scope_note": (
                "c_H = kappa(H^2) is the classical Lie-algebra generator trace norm in Gamma = c_H Phi^2 / (2 G Area), "
                "distinct from seam-phase stiffness kappa_seam; untwisted integer m in Z attains minimum at m = 0 "
                "(requiring a nontrivial registration premise to select |m| = 1), whereas half-integral antiperiodic "
                "spin shift q in Z - 1/2 excludes 0 automatically with twin minima +-1/2 (1 orientation bit), "
                "while mapping half-unit spin shift vs integer divisor m = +-1 to 3 chiral families remains the slotwise domain duty."
            ),
        },
    }


# ============================================================================
# SECTION 2: PART 1B — INDEPENDENT ZERO-IMPORT VERIFICATION OF ALL 12 CODEX
#                      P-C3 MATHEMATICAL METHODS (ca02b5d8d)
# ============================================================================

def quat_basis_sp() -> Tuple[sp.Matrix, sp.Matrix, sp.Matrix, Tuple[sp.Matrix, sp.Matrix, sp.Matrix]]:
    qi = sp.diag(sp.I, -sp.I)
    qj = sp.Matrix([[0, 1], [-1, 0]])
    qk = qi * qj
    return qi, qj, qk, (qj, qi, qk)


def so3_adjoint_sp(g_mat: sp.Matrix, blocks: Tuple[sp.Matrix, sp.Matrix, sp.Matrix]) -> sp.Matrix:
    g_inv = g_mat.inv()
    out = sp.zeros(3, 3)
    for r in range(3):
        for c in range(3):
            out[r, c] = sp.simplify(-sp.trace(blocks[r] * g_mat * blocks[c] * g_inv) / 2)
    return out


def quat_contraction_sp(s_mat: sp.Matrix, m_pair: sp.Matrix, blocks: Tuple[sp.Matrix, sp.Matrix, sp.Matrix]) -> sp.Matrix:
    eps = sp.Matrix([[0, 1], [-1, 0]])
    out = sp.zeros(3, 3)
    for a in range(3):
        for b in range(3):
            c_mat = blocks[a].T * eps * s_mat * blocks[b]
            val = sum(c_mat[r, col] * m_pair[r, col] for r in range(2) for col in range(2))
            out[a, b] = sp.simplify(val)
    return out


def mat_eq_sp(a_m: sp.Matrix, b_m: sp.Matrix) -> bool:
    diff = (a_m - b_m).applyfunc(sp.simplify)
    return diff == sp.zeros(a_m.rows, a_m.cols)


def e_unit_sp(sz: int, r: int, c: int) -> sp.Matrix:
    m = sp.zeros(sz, sz)
    m[r, c] = 1
    return m


def run_part_1b_independent_pc3_twelve_methods() -> Dict[str, Any]:
    qi, qj, qk, blocks = quat_basis_sp()
    i2 = sp.eye(2)
    i3 = sp.eye(3)

    # --- Method 1: Quaternion relations, SO(3) conjugation, and quarter-turn unsigned det = -1 ---
    q_rel_ok = (
        qi ** 2 == -i2 and qj ** 2 == -i2 and qk ** 2 == -i2
        and qi * qj == qk and qj * qi == -qk and qj * qi != qk
    )
    q_turn = (i2 + qi) / sp.sqrt(2)
    gens_m1 = (qi, qj, q_turn)
    hom_ok = True
    for g1, g2 in product(gens_m1, repeat=2):
        o1 = so3_adjoint_sp(g1, blocks)
        o2 = so3_adjoint_sp(g2, blocks)
        o12 = so3_adjoint_sp(g1 * g2, blocks)
        if not (mat_eq_sp(o12, o1 * o2) and mat_eq_sp(o1.T * o1, i3) and sp.simplify(o1.det() - 1) == 0):
            hom_ok = False
        if not mat_eq_sp(o12.applyfunc(abs), o1.applyfunc(abs) * o2.applyfunc(abs)):
            hom_ok = False
    o_qt = so3_adjoint_sp(q_turn, blocks)
    u_qt = o_qt.applyfunc(abs)
    vx, vy = sp.Matrix([1, 0, 0]), sp.Matrix([0, 1, 0])
    qt_unsigned_det = int(sp.simplify(u_qt.det()))
    cross_signed_ok = mat_eq_sp((o_qt * vx).cross(o_qt * vy), o_qt * vx.cross(vy))
    cross_unsigned_fails = not mat_eq_sp((u_qt * vx).cross(u_qt * vy), u_qt * vx.cross(vy))
    m01_ok = bool(q_rel_ok and hom_ok and qt_unsigned_det == -1 and cross_signed_ok and cross_unsigned_fails)

    # --- Method 2: Full and traceless M_3(C) coupling span ---
    m_units = [e_unit_sp(2, r, c) for r, c in product(range(2), repeat=2)]
    s_traceless = [sp.diag(1, -1), m_units[1], m_units[2]]
    cols_full = [sp.Matrix(list(quat_contraction_sp(s, m, blocks))) for s, m in product(m_units, m_units)]
    cols_tr0 = [sp.Matrix(list(quat_contraction_sp(s, m, blocks))) for s, m in product(s_traceless, m_units)]
    rank_full = int(sp.Matrix.hstack(*cols_full).rank())
    rank_traceless = int(sp.Matrix.hstack(*cols_tr0).rank())
    single_rank = int(quat_contraction_sp(s_traceless[0], m_units[1], blocks).rank())
    m02_ok = bool(rank_full == 9 and rank_traceless == 9 and single_rank < 3)

    # --- Method 3: SL(2, C) covariance (including unipotent & hyperbolic) + traceless-S unsigned counterexample ---
    gens_m3 = (qi, qj, q_turn, sp.Matrix([[1, 1], [0, 1]]), sp.Matrix([[2, 1], [1, 1]]))
    cov_ok = True
    for g_m, s_m, mp_m in product(gens_m3, s_traceless, m_units):
        og = so3_adjoint_sp(g_m, blocks)
        c_new = quat_contraction_sp(g_m * s_m * g_m.inv(), g_m * mp_m * g_m.T, blocks)
        c_old = quat_contraction_sp(s_m, mp_m, blocks)
        if not mat_eq_sp(c_new, og * c_old * og.T):
            cov_ok = False
    s_wit = sp.diag(1, -1)
    m_wit = sp.Matrix([[0, -1], [0, 0]])
    c_wit = quat_contraction_sp(s_wit, m_wit, blocks)
    c_wit_exp = sp.Matrix([[-1, 0, -sp.I], [0, 1, 0], [sp.I, 0, -1]])
    c_wit_j = quat_contraction_sp(qj * s_wit * qj.inv(), qj * m_wit * qj.T, blocks)
    oj = so3_adjoint_sp(qj, blocks)
    uj = oj.applyfunc(abs)
    unsigned_wit_fails = not mat_eq_sp(uj.T * c_wit_j * uj, c_wit)
    signed_wit_passes = mat_eq_sp(oj.T * c_wit_j * oj, c_wit) and mat_eq_sp(c_wit, c_wit_exp)
    m03_ok = bool(cov_ok and unsigned_wit_fails and signed_wit_passes)

    # --- Method 4: Q_8 inner residual after deck cancellation & vertical spin sheet ---
    q8 = (i2, -i2, qi, -qi, qj, -qj, qk, -qk)
    q8_res_ok = True
    for h_el in q8:
        oh = so3_adjoint_sp(h_el, blocks)
        res = sp.kronecker_product(oh, h_el) * sp.kronecker_product(i3, h_el).inv()
        if not mat_eq_sp(res, sp.kronecker_product(oh, i2)):
            q8_res_ok = False
        for k_el in q8:
            lhs = sp.kronecker_product(oh, h_el) * sp.kronecker_product(i3, h_el.inv() * k_el)
            rhs = sp.kronecker_product(oh, k_el)
            if not mat_eq_sp(lhs, rhs):
                q8_res_ok = False
    lift_qi = sp.kronecker_product(so3_adjoint_sp(qi, blocks), qi)
    wrong_side_fails = not mat_eq_sp(
        lift_qi * sp.kronecker_product(i3, qj * qi.inv()),
        lift_qi * sp.kronecker_product(i3, qi.inv() * qj),
    )
    missing_deck_fails = not mat_eq_sp(lift_qi, lift_qi * sp.kronecker_product(i3, qi).inv())
    k_eps, j_eps = -1, -1
    unspun = i3 / k_eps
    spun = j_eps * unspun
    spin_sheet_ok = (unspun == -i3) and (spun == i3) and (unspun != spun) and (so3_adjoint_sp(-i2, blocks) == i3)
    m04_ok = bool(q8_res_ok and wrong_side_fails and missing_deck_fails and spin_sheet_ok)

    # --- Method 5: Constant left/right stabilizers on full M_3(C) and 5-slot singular family ---
    vars18 = sp.symbols("l0:9 b0:9")
    l_var = sp.Matrix(3, 3, vars18[:9])
    b_var = sp.Matrix(3, 3, vars18[9:])
    full_fam = [e_unit_sp(3, r, c) for r, c in product(range(3), repeat=2)]
    slot5_fam = [e_unit_sp(3, r, c) for r, c in ((0, 2), (1, 2), (2, 0), (2, 1), (2, 2))]
    sys_full, _ = sp.linear_eq_to_matrix([e for y in full_fam for e in (l_var.T * y - y * b_var)], vars18)
    sys_slot5, _ = sp.linear_eq_to_matrix([e for y in slot5_fam for e in (l_var.T * y - y * b_var)], vars18)
    sys_one, _ = sp.linear_eq_to_matrix(list(l_var.T * slot5_fam[-1] - slot5_fam[-1] * b_var), vars18)
    rk_full_stab = int(sys_full.rank())
    rk_slot5_stab = int(sys_slot5.rank())
    rk_one_stab = int(sys_one.rank())
    m05_ok = bool(rk_full_stab == 17 and rk_slot5_stab == 17 and len(sys_slot5.nullspace()) == 1 and rk_one_stab < 17)

    # --- Method 6: Antisymmetric source cubic & noncommuting polarization ---
    h5 = sp.diag(-2, -2, -2, 3, 3)
    ep = e_unit_sp(5, 3, 0)
    em = e_unit_sp(5, 0, 3)

    def w3_src(ca: sp.Matrix, u_m: sp.Matrix, v_m: sp.Matrix) -> Any:
        return -sp.I * sp.trace(u_m * (ca * v_m - v_m * ca) - v_m * (ca * u_m - u_m * ca)) / 2

    t1, t2, t3 = sp.symbols("t1 t2 t3")
    triples = ((h5, ep, em), (2 * h5, 3 * ep, 5 * em), (7 * h5, 11 * ep, 13 * em))
    comb_slots = [sum((t_s * trp[idx] for t_s, trp in zip((t1, t2, t3), triples)), sp.zeros(5, 5)) for idx in range(3)]
    poly_coeff = sp.expand(w3_src(*comb_slots)).coeff(t1).coeff(t2).coeff(t3)
    expected_pol = sp.I * sum(
        sp.trace(x[0] * ((y[1] * z[2] - z[2] * y[1]) + (z[1] * y[2] - y[2] * z[1])))
        for x, y, z in ((triples[0], triples[1], triples[2]), (triples[1], triples[2], triples[0]), (triples[2], triples[0], triples[1]))
    )
    m06_ok = bool(
        sp.simplify(poly_coeff - expected_pol) == 0
        and poly_coeff != 0
        and sp.simplify(w3_src(h5, ep, em) - sp.I * sp.trace(h5 * (ep * em - em * ep))) == 0
        and w3_src(h5, h5, h5) == 0
    )

    # --- Method 7: SU(5) root bracket & physical mass-operator derivative ---
    t_par = sp.Symbol("t_par", real=True)
    omega_den = sp.Rational(3, 2)
    p1_op = -sp.I * ((t_par * h5) * ep - ep * (t_par * h5))
    row_deriv = (-p1_op / omega_den).diff(t_par)
    proj_val = sp.simplify(omega_den * sp.trace(em * row_deriv))
    unweighted_val = sp.simplify(sp.trace(em * row_deriv))
    m07_ok = bool(
        (h5 * ep - ep * h5) == 5 * ep
        and (h5 * em - em * h5) == -5 * em
        and int(sp.trace(h5 * h5)) == 30
        and int(sp.trace(ep * em)) == 1
        and proj_val == 5 * sp.I
        and proj_val == w3_src(h5, ep, em)
        and unweighted_val != proj_val
    )

    # --- Method 8: Normalized |y|^2 / e_H^2 = 2 A_omega A_g / I_omega^2 & rescaling invariance ---
    qs, ks, hs, gs, ao, ag, io, cp = sp.symbols("qs ks hs gs ao ag io cp", positive=True)

    def norm_pair(q_v: Any, k_v: Any, h_v: Any, g_v: Any, a_om: Any, a_gm: Any, i_om: Any, c_p: Any, c_m: Any, wt_a: Any = sp.Rational(1, 2)) -> Tuple[Any, Any]:
        z_a = wt_a * h_v * a_om / g_v
        z_u = k_v * c_p * i_om / g_v
        z_v = k_v * c_m * i_om / g_v
        z_h = h_v * a_gm / g_v
        y2_raw = (q_v ** 2) * (k_v ** 2) * (a_om ** 2) / (g_v ** 2)
        return sp.cancel(y2_raw / (z_a * z_u * z_v)), sp.cancel((q_v ** 2) / z_h)

    y2_sym, eh2_sym = norm_pair(qs, ks, hs, gs, ao, ag, io, cp, 1 / cp)
    y2_bad_wt, _ = norm_pair(qs, ks, hs, gs, ao, ag, io, cp, 1 / cp, wt_a=1)
    ratio_exact = sp.cancel(y2_sym / eh2_sym - 2 * ao * ag / (io ** 2)) == 0
    bad_wt_ratio = sp.cancel(y2_bad_wt / eh2_sym)  # equals ao * ag / io^2 (factor 1 instead of 2!)
    lam_c, p_c = 3 + 4 * sp.I, 1 + sp.I
    frame_f = (sp.conjugate(lam_c), p_c, lam_c / p_c)
    frame_inv = sp.simplify(sp.prod(frame_f) * sp.conjugate(sp.prod(frame_f)) / sp.prod(x * sp.conjugate(x) for x in frame_f)) == 1
    m08_ok = bool(ratio_exact and sp.cancel(bad_wt_ratio - ao * ag / (io ** 2)) == 0 and frame_inv)

    # --- Method 9: Cauchy-Schwarz shape inequality on flat, periodic, AND hyperbolic-cusp collar metrics ---
    x_coord = sp.Symbol("x_coord", real=True)
    # Flat Omega = 2 on [0, 1] with |omega_z| = 1:
    ag_flat = sp.integrate(sp.Integer(2) ** 2, (x_coord, 0, 1))
    io_flat = sp.integrate(sp.Integer(2), (x_coord, 0, 1))
    r_flat = sp.cancel(2 * ag_flat / (io_flat ** 2))
    # Periodic Omega = 2 + cos(2 pi x) on [0, 1]:
    om_per = 2 + sp.cos(2 * sp.pi * x_coord)
    ag_per = sp.integrate(om_per ** 2, (x_coord, 0, 1))
    io_per = sp.integrate(om_per, (x_coord, 0, 1))
    r_per = sp.cancel(2 * ag_per / (io_per ** 2))
    # Independent hyperbolic cusp collar Omega(y) = 1/y on [1, e^2] with |omega_z| = 1:
    y_coord = sp.Symbol("y_coord", positive=True)
    ao_hyp = sp.integrate(1, (y_coord, 1, sp.E ** 2))
    ag_hyp = sp.integrate(1 / (y_coord ** 2), (y_coord, 1, sp.E ** 2))
    io_hyp = sp.integrate(1 / y_coord, (y_coord, 1, sp.E ** 2))
    r_hyp = sp.simplify(2 * ao_hyp * ag_hyp / (io_hyp ** 2))  # = 2*(e^2 - 1)*(1 - e^{-2}) / 4 = (e - e^{-1})^2 / 2 = 2 sinh^2(1) > 2!
    with mp.workdps(80):
        r_hyp_mp = 2 * (mp.sinh(1) ** 2)
        r_hyp_diff = abs(mp.mpf(str(sp.N(r_hyp, 85))) - r_hyp_mp)
    m09_ok = bool(r_flat == 2 and r_per == sp.Rational(9, 4) and bool(r_hyp > 2) and float(r_hyp_diff) < float(Fraction(1, 10 ** 75)))

    # --- Method 10: Pure-slot rank <= 2 rule & illicit form-form entry ---
    u1, u2, u3, v1, v2, v3 = sp.symbols("u1 u2 u3 v1 v2 v3")
    pure_slot_mat = sp.Matrix([
        [0, 0, u1 * v3],
        [0, 0, u2 * v3],
        [u3 * v1, u3 * v2, u3 * v3],
    ])
    lead_2 = e_unit_sp(3, 0, 2) + e_unit_sp(3, 2, 0)
    m10_ok = bool(
        sp.simplify(pure_slot_mat.det()) == 0
        and int(pure_slot_mat.rank()) == 2
        and int(lead_2.rank()) == 2
        and int((lead_2 + e_unit_sp(3, 1, 1)).rank()) == 3
        and lead_2 * sp.Matrix([0, 1, 0]) == sp.zeros(3, 1)
    )

    # --- Method 11: Full-complement second-order response V_2 - b c / d & characteristic polynomial ---
    t_s = sp.Symbol("t_s", real=True)
    v2_mat = 4 * e_unit_sp(3, 1, 1)
    b_col = sp.Matrix([0, 2, 0])
    c_row = sp.Matrix([[0, 5, 0]])
    d_heavy = 3 + 7 * t_s
    full_4x4 = (t_s * lead_2 + (t_s ** 2) * v2_mat).row_join(t_s * b_col).col_join((t_s * c_row).row_join(sp.Matrix([[d_heavy]])))
    red_3x3 = t_s * lead_2 + (t_s ** 2) * v2_mat - (t_s ** 2) * b_col * c_row / d_heavy
    c2_coeff = (red_3x3.diff(t_s, 2).subs(t_s, 0) / 2).applyfunc(sp.simplify)
    ker_vec = sp.Matrix([0, 1, 0])
    m2_val = (ker_vec.T * c2_coeff * ker_vec)[0]
    blk_2x2 = full_4x4.extract([1, 3], [1, 3])
    lam_sym = sp.Symbol("lam_sym")
    cpoly_t4 = sp.expand((blk_2x2.T * blk_2x2).charpoly(lam_sym).as_expr().subs(lam_sym, (m2_val ** 2) * (t_s ** 4))).coeff(t_s, 4)
    wrong_cpoly_t4 = sp.expand((blk_2x2.T * blk_2x2).charpoly(lam_sym).as_expr().subs(lam_sym, 16 * (t_s ** 4))).coeff(t_s, 4)
    m11_ok = bool(
        mat_eq_sp(c2_coeff, v2_mat - b_col * c_row / 3)
        and m2_val == sp.Rational(2, 3)
        and cpoly_t4 == 0
        and wrong_cpoly_t4 != 0
    )

    # --- Method 12: Complex-bilinear Gram S_L^{-T} Y S_R^{-1} vs wrong S_L^{-H} & Hermitian current ---
    sl = sp.Matrix([[2, sp.I], [-sp.I, 2]])
    sr = sp.Matrix([[3, 1 + sp.I], [1 - sp.I, 3]])
    gl, gr = sl ** 2, sr ** 2
    y_raw = sp.Matrix([[1, sp.I], [2, 3 - sp.I]])
    y_can = sl.inv().T * y_raw * sr.inv() / 3
    y_wrong_herm = sl.inv().H * y_raw * sr.inv() / 3
    zl = sp.Matrix([1 + sp.I, 2 - sp.I])
    zr = sp.Matrix([2 + sp.I, 1 - 2 * sp.I])
    bilin_id = sp.simplify((zl.T * y_can * zr)[0] - ((sl.inv() * zl).T * y_raw * (sr.inv() * zr))[0] / 3) == 0
    wrong_herm_differs = not mat_eq_sp(y_wrong_herm, y_can)
    q_diag = sp.diag(2, -1)
    rho_rep = sl.inv() * q_diag * sl
    j_cur = gl * rho_rep
    cur_ok = mat_eq_sp(j_cur, j_cur.H) and mat_eq_sp(sl.inv() * j_cur * sl.inv(), q_diag) and (not mat_eq_sp(j_cur, rho_rep))
    b_g, u_f, ub_f, du_f, dub_f = sp.symbols("b_g u_f ub_f du_f dub_f")
    kin_exp = sp.expand(sp.Rational(11, 7) * (dub_f + sp.I * 5 * b_g * ub_f) * (du_f - sp.I * 5 * b_g * u_f))
    kin_b1 = sp.expand(kin_exp.coeff(b_g, 1) - sp.I * 5 * sp.Rational(11, 7) * (ub_f * du_f - dub_f * u_f)) == 0
    m12_ok = bool(bilin_id and wrong_herm_differs and cur_ok and kin_b1)

    methods_status = {
        "M01_quaternion_relations_and_conjugation_generators": m01_ok,
        "M02_coupling_span_full_and_traceless": m02_ok,
        "M03_coupling_covariance_and_unsigned_counterexample": m03_ok,
        "M04_inner_residual_and_vertical_spin_sheet": m04_ok,
        "M05_full_and_slot_family_constant_stabilizers": m05_ok,
        "M06_source_cubic_and_polarization": m06_ok,
        "M07_root_vertex_and_physical_mass_derivative": m07_ok,
        "M08_normalized_vertex_current_and_rescalings": m08_ok,
        "M09_shape_inequality_exact_metric_controls_plus_hyperbolic_collar": m09_ok,
        "M10_slot_rank_and_illicit_form_entry": m10_ok,
        "M11_full_complement_response_and_backreaction": m11_ok,
        "M12_complex_bilinear_gram_and_current_transport": m12_ok,
    }
    e2_passed = all(methods_status.values())

    return {
        "E2_PC3_TwelveMethod_Independent_Gate_passed": e2_passed,
        "methods_passed_count": sum(1 for v in methods_status.values() if v),
        "methods_total_count": len(methods_status),
        "comparison_verdict_vs_physical_ca02b5d8d": "SAME_ACROSS_ALL_12_METHODS" if e2_passed else "DIFFERENT",
        "method_results": methods_status,
        "witness_values": {
            "M01_quarter_turn_unsigned_det": qt_unsigned_det,
            "M02_ranks_full_and_traceless": [rank_full, rank_traceless],
            "M05_stabilizer_ranks_full_slot5_single": [rk_full_stab, rk_slot5_stab, rk_one_stab],
            "M07_projected_mass_derivative": str(proj_val),
            "M09_ratios_flat_periodic_hyperbolic_e2": [str(r_flat), str(r_per), float(r_hyp_mp)],
            "M11_second_order_light_mass_coeff": str(m2_val),
        },
        "planted_controls": {
            "PC_U1_UnsignedLiftAndWrongSideDeck_caught": bool(qt_unsigned_det == -1 and unsigned_wit_fails and wrong_side_fails),
            "PC_U1_WrongHermitianVsTransposeGramAndConnectionWeight_caught": bool(
                wrong_herm_differs and sp.cancel(bad_wt_ratio - ao * ag / (io ** 2)) == 0
            ),
        },
    }


def main() -> None:
    ast_check = verify_ast_unify1()
    part_1a = run_part_1a_crt_gauge_family_and_anomaly()
    part_1b = run_part_1b_independent_pc3_twelve_methods()

    controls_passed = bool(
        ast_check["Gate_AST_Stage1_Unify_Passed"]
        and part_1a["crt_weil_tensor_factorization_55dps"]["PC_U1_NonCoprimeLevel9Failure_non_rank1_sv_norm"] > 1
        and part_1a["anomaly_forced_hypercharge"]["PC_U1_UnbalancedHyperchargeAnomaly_abs_cubic_at_neg1_1"] >= 32
        and part_1b["planted_controls"]["PC_U1_UnsignedLiftAndWrongSideDeck_caught"]
        and part_1b["planted_controls"]["PC_U1_WrongHermitianVsTransposeGramAndConnectionWeight_caught"]
    )

    stage_1_passed = bool(
        controls_passed
        and part_1a["E1_CRT_GaugeFamily_and_Anomaly_Gate_passed"]
        and part_1b["E2_PC3_TwelveMethod_Independent_Gate_passed"]
    )

    out_payload: Dict[str, Any] = {
        "card": "X-UNIFY-1",
        "empirical_firewall": "0 of 19",
        "ast_source_check": ast_check,
        "part_1a_crt_gauge_family_and_anomaly": part_1a,
        "part_1b_independent_pc3_twelve_methods": part_1b,
        "all_planted_controls_passed": controls_passed,
        "stage_1_gate_passed": stage_1_passed,
    }

    out_dir = Path(__file__).resolve().parent
    out_json = out_dir / "verify_x_unify_1_out.json"
    out_json.write_text(json.dumps(out_payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    sha = hashlib.sha256(out_json.read_bytes()).hexdigest()
    (out_dir / "OUTPUT_SHA256.txt").write_text(f"{sha}  verify_x_unify_1_out.json\n", encoding="utf-8")


if __name__ == "__main__":
    main()
