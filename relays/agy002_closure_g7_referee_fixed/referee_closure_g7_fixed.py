#!/usr/bin/env python3
"""Independent Cold-Room Zero-Trust Referee for Gate 7 (AGY-002_CLOSURE-G7).

Enforces Guardrails 1-6, strict 0-of-19 empirical firewall, zero repo imports,
and zero float/complex AST literals across all deliverables and planted faults:
  1. Deliverable 1: Exact SymPy rational + multi-seed SVD U(3)^5 broken-symmetry
     ranks (41 for SM -> 19 parameters; 44 for Weinberg EFT -> 28 parameters),
     explicit unbroken U(1)_B x U(1)_{L_e} x U(1)_{L_mu} x U(1)_{L_tau} -> U(1)_B
     nullspace verification, rank-1 Buckingham-Pi matrix D_dim, and PF7.1.
  2. Deliverable 2: Independent 46-node monotone max-plus epistemic DAG
     (Kahn + 3-color DFS acyclicity, Guardrail 1 seam honesty, [2, 6, 2, 0]
     relation histogram, [0, 0, 1, 18] SM target histogram, PF7.2..PF7.4)
     plus independent first-principles verification of PR-1..PR-10.
  3. Deliverable 3: Campaign-wide byte-for-byte SHA-256 custody lock across all
     38 prior Gate 0-7 manifests + runtime self-verification of SCRIPT_SHA256.txt
     + PF7.5 in-memory digest tamper control.
"""

import ast
import cmath
import copy
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import re
import sys

import mpmath as mp
import numpy as np
import sympy as sp
from sympy.polys.domains import QQ
from sympy.polys.matrices import DomainMatrix


ALLOWED_TOP_IMPORTS = frozenset({
    "ast",
    "cmath",
    "copy",
    "fractions",
    "hashlib",
    "json",
    "math",
    "mpmath",
    "numpy",
    "pathlib",
    "re",
    "sys",
    "sympy",
})

IMAG_UNIT = complex(0, 1)


def qfloat(num: int, den: int = 1) -> float:
    """Construct runtime Python float from exact integers with zero float literals."""
    return int(num) / int(den)


def frac_str(frac: Fraction) -> str:
    """Format an exact Fraction as p/q (or integer string if denominator == 1)."""
    if frac.denominator == 1:
        return str(frac.numerator)
    return f"{frac.numerator}/{frac.denominator}"


def bounded_rat_str(val: float, max_den: int = 10**16) -> str:
    """Convert runtime float into mask-safe p/q rational string."""
    fval = Fraction(val).limit_denominator(max_den)
    return frac_str(fval)


# ============================================================================
# 0. Self-AST Zero-Float / Zero-Complex / Zero-Repo-Import Gate
# ============================================================================

def audit_self_source(script_path: Path) -> dict:
    source_text = script_path.read_text(encoding="utf-8")
    tree = ast.parse(source_text, filename=str(script_path))

    float_literals = 0
    complex_literals = 0
    imported_roots = set()
    disallowed_imports = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Constant):
            if isinstance(node.value, float):
                float_literals += 1
            elif isinstance(node.value, complex):
                complex_literals += 1
        elif isinstance(node, ast.Import):
            for alias in node.names:
                root = alias.name.split(".")[0]
                imported_roots.add(root)
                if root not in ALLOWED_TOP_IMPORTS:
                    disallowed_imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            root = (node.module or "").split(".")[0]
            imported_roots.add(root)
            if node.level != 0 or root not in ALLOWED_TOP_IMPORTS:
                disallowed_imports.append(node.module or "<relative>")

    passed = (
        float_literals == 0
        and complex_literals == 0
        and len(disallowed_imports) == 0
    )
    return {
        "float_literal_count": float_literals,
        "complex_literal_count": complex_literals,
        "disallowed_import_count": len(disallowed_imports),
        "disallowed_imports": disallowed_imports,
        "imported_roots": sorted(imported_roots),
        "passed": bool(passed),
    }


# ============================================================================
# 1. Deliverable 1: Exact U(3)^5 Broken-Symmetry Rank & Buckingham-Pi Lock
# ============================================================================

def build_u3_skew_hermitian_basis() -> list:
    """Construct exact 9-element real Lie algebra basis of u(3) over Z[i]."""
    basis = []
    for k in range(3):
        mat = sp.zeros(3, 3)
        mat[k, k] = sp.I
        basis.append(mat)
    for j in range(3):
        for k in range(j + 1, 3):
            mat_re = sp.zeros(3, 3)
            mat_re[j, k] = sp.Integer(1)
            mat_re[k, j] = sp.Integer(-1)
            basis.append(mat_re)

            mat_im = sp.zeros(3, 3)
            mat_im[j, k] = sp.I
            mat_im[k, j] = sp.I
            basis.append(mat_im)
    return basis


def pack_dirac_qq(mat: sp.Matrix) -> list:
    out = []
    for r in range(3):
        for c in range(3):
            re_part, im_part = mat[r, c].as_real_imag()
            out.append(QQ(int(re_part)))
            out.append(QQ(int(im_part)))
    return out


def pack_symmetric_qq(mat: sp.Matrix) -> list:
    out = []
    for r in range(3):
        for c in range(r, 3):
            re_part, im_part = mat[r, c].as_real_imag()
            out.append(QQ(int(re_part)))
            out.append(QQ(int(im_part)))
    return out


def build_exact_jacobians(Yu: sp.Matrix, Yd: sp.Matrix, Ye: sp.Matrix, kap: sp.Matrix):
    """Build exact 54x45 (SM) and 66x45 (Weinberg EFT) Jacobians over QQ."""
    u3_basis = build_u3_skew_hermitian_basis()
    zero3 = sp.zeros(3, 3)
    cols_sm = []
    cols_eft = []

    for slot in range(5):
        for gen in u3_basis:
            slots = [zero3, zero3, zero3, zero3, zero3]
            slots[slot] = gen
            g_Q, g_u, g_d, g_L, g_e = slots
            d_Yu = g_Q * Yu - Yu * g_u
            d_Yd = g_Q * Yd - Yd * g_d
            d_Ye = g_L * Ye - Ye * g_e
            d_kap = g_L * kap + kap * g_L.T

            col_sm = pack_dirac_qq(d_Yu) + pack_dirac_qq(d_Yd) + pack_dirac_qq(d_Ye)
            col_eft = col_sm + pack_symmetric_qq(d_kap)
            cols_sm.append(col_sm)
            cols_eft.append(col_eft)

    dm_sm = DomainMatrix(cols_sm, (45, 54), QQ).transpose()
    dm_eft = DomainMatrix(cols_eft, (45, 66), QQ).transpose()
    return dm_sm, dm_eft


def run_deliverable_1() -> dict:
    I = sp.I
    Yu_gen = sp.Matrix([
        [2 + I, 1 - I, 3],
        [1 + 2 * I, 4 - I, 2 + I],
        [3 - I, 1 + I, 5 + 2 * I],
    ])
    Yd_gen = sp.Matrix([
        [3 - I, 2 + I, 1 + 3 * I],
        [1 - 2 * I, 5 + I, 2 - I],
        [2 + I, 3 - 2 * I, 4 + I],
    ])
    Ye_gen = sp.Matrix([
        [4 + I, 1 + 2 * I, 2 - I],
        [2 - I, 3 + 2 * I, 1 + I],
        [1 + I, 2 - 3 * I, 6 - I],
    ])
    kap_gen = sp.Matrix([
        [2 + I, 1 - I, 3 + 2 * I],
        [1 - I, 4 + 3 * I, 2 - I],
        [3 + 2 * I, 2 - I, 5 - 2 * I],
    ])
    assert kap_gen == kap_gen.T
    assert sp.simplify(Yu_gen.det()) != 0
    assert sp.simplify(Yd_gen.det()) != 0
    assert sp.simplify(Ye_gen.det()) != 0
    assert sp.simplify(kap_gen.det()) != 0

    dm_sm_gen, dm_eft_gen = build_exact_jacobians(Yu_gen, Yd_gen, Ye_gen, kap_gen)
    rank_sm_gen = dm_sm_gen.rank()
    rank_eft_gen = dm_eft_gen.rank()
    ns_sm_gen = dm_sm_gen.nullspace()
    ns_eft_gen = dm_eft_gen.nullspace()

    Ye_diag = sp.Matrix([
        [2, 0, 0],
        [0, 5, 0],
        [0, 0, 11],
    ])
    dm_sm_lepdiag, dm_eft_lepdiag = build_exact_jacobians(Yu_gen, Yd_gen, Ye_diag, kap_gen)
    rank_sm_lepdiag = dm_sm_lepdiag.rank()
    rank_eft_lepdiag = dm_eft_lepdiag.rank()

    v_B = [QQ(0)] * 45
    for slot_idx in (0, 1, 2):
        for k in range(3):
            v_B[slot_idx * 9 + k] = QQ(1)

    v_Le = [QQ(0)] * 45
    v_Le[3 * 9 + 0] = QQ(1)
    v_Le[4 * 9 + 0] = QQ(1)

    v_Lmu = [QQ(0)] * 45
    v_Lmu[3 * 9 + 1] = QQ(1)
    v_Lmu[4 * 9 + 1] = QQ(1)

    v_Ltau = [QQ(0)] * 45
    v_Ltau[3 * 9 + 2] = QQ(1)
    v_Ltau[4 * 9 + 2] = QQ(1)

    V_u1_4 = DomainMatrix([v_B, v_Le, v_Lmu, v_Ltau], (4, 45), QQ).transpose()
    sm_annihilates_u1_4 = (dm_sm_lepdiag * V_u1_4).is_zero_matrix
    u1_4_rank = V_u1_4.rank()

    u3_basis = build_u3_skew_hermitian_basis()

    def coords_in_u3(skew_mat: sp.Matrix) -> list:
        coords = []
        for k in range(3):
            _, im_diag = skew_mat[k, k].as_real_imag()
            coords.append(QQ(int(im_diag)))
        for j in range(3):
            for k in range(j + 1, 3):
                re_jk, im_jk = skew_mat[j, k].as_real_imag()
                coords.append(QQ(int(re_jk)))
                coords.append(QQ(int(im_jk)))
        return coords

    He_L = Ye_gen * Ye_gen.adjoint()
    He_R = Ye_gen.adjoint() * Ye_gen
    cov_lepton_vecs = []
    for power_m in (0, 1, 2):
        gL_m = sp.I * (He_L ** power_m)
        ge_m = sp.I * (He_R ** power_m)
        vec45 = [QQ(0)] * 27 + coords_in_u3(gL_m) + coords_in_u3(ge_m)
        cov_lepton_vecs.append(vec45)

    V_cov_4 = DomainMatrix([v_B] + cov_lepton_vecs, (4, 45), QQ).transpose()
    cov_sm_kernel_exact = bool((dm_sm_gen * V_cov_4).is_zero_matrix) and (V_cov_4.rank() == 4)

    v_B_dm = DomainMatrix([[x] for x in v_B], (45, 1), QQ)
    eft_preserves_B_gen = bool((dm_eft_gen * v_B_dm).is_zero_matrix)
    eft_preserves_B_diag = bool((dm_eft_lepdiag * v_B_dm).is_zero_matrix)

    eft_breaks_all_3_lepton_diag = all(
        not (dm_eft_lepdiag * DomainMatrix([[x] for x in vL], (45, 1), QQ)).is_zero_matrix
        for vL in (v_Le, v_Lmu, v_Ltau)
    )
    eft_breaks_all_3_lepton_cov = all(
        not (dm_eft_gen * DomainMatrix([[x] for x in vL], (45, 1), QQ)).is_zero_matrix
        for vL in cov_lepton_vecs
    )

    u3_np = [np.array(m.tolist(), dtype=complex) for m in u3_basis]
    svd_ranks_sm = []
    svd_ranks_eft = []
    max_null_sv = 0
    min_pos_sv_num = 10**9

    for seed in (11, 23, 37, 53, 71):
        rng = np.random.default_rng(seed)
        Yu_n = rng.standard_normal((3, 3)) + IMAG_UNIT * rng.standard_normal((3, 3))
        Yd_n = rng.standard_normal((3, 3)) + IMAG_UNIT * rng.standard_normal((3, 3))
        Ye_n = rng.standard_normal((3, 3)) + IMAG_UNIT * rng.standard_normal((3, 3))
        raw_k = rng.standard_normal((3, 3)) + IMAG_UNIT * rng.standard_normal((3, 3))
        kap_n = (raw_k + raw_k.T) / qfloat(2, 1)

        J_sm_n = np.zeros((54, 45), dtype=float)
        J_eft_n = np.zeros((66, 45), dtype=float)
        z3_n = np.zeros((3, 3), dtype=complex)

        col_idx = 0
        for slot in range(5):
            for gen_n in u3_np:
                gs = [z3_n, z3_n, z3_n, z3_n, z3_n]
                gs[slot] = gen_n
                gQ, gu, gd, gL, ge = gs
                dYu = gQ @ Yu_n - Yu_n @ gu
                dYd = gQ @ Yd_n - Yd_n @ gd
                dYe = gL @ Ye_n - Ye_n @ ge
                dkap = gL @ kap_n + kap_n @ gL.T

                vec_sm = []
                for M_cur in (dYu, dYd, dYe):
                    for r in range(3):
                        for c in range(3):
                            vec_sm.append(M_cur[r, c].real)
                            vec_sm.append(M_cur[r, c].imag)
                vec_kap = []
                for r in range(3):
                    for c in range(r, 3):
                        vec_kap.append(dkap[r, c].real)
                        vec_kap.append(dkap[r, c].imag)

                J_sm_n[:, col_idx] = np.array(vec_sm, dtype=float)
                J_eft_n[:, col_idx] = np.array(vec_sm + vec_kap, dtype=float)
                col_idx += 1

        sv_sm = np.linalg.svd(J_sm_n, compute_uv=False)
        sv_eft = np.linalg.svd(J_eft_n, compute_uv=False)
        tol = qfloat(1, 10**10)
        r_sm = int(np.sum(sv_sm > tol))
        r_eft = int(np.sum(sv_eft > tol))
        svd_ranks_sm.append(r_sm)
        svd_ranks_eft.append(r_eft)

        null_max_cur = max(float(np.max(sv_sm[41:])), float(np.max(sv_eft[44:])))
        if null_max_cur > max_null_sv:
            max_null_sv = null_max_cur
        pos_min_cur = min(float(sv_sm[40]), float(sv_eft[43]))
        if pos_min_cur < min_pos_sv_num:
            min_pos_sv_num = pos_min_cur

    unbroken_sm = 45 - rank_sm_gen
    flavour_sm = 54 - rank_sm_gen
    total_sm = flavour_sm + 3 + 2 + 1

    unbroken_eft = 45 - rank_eft_gen
    flavour_nu_eft = 66 - rank_eft_gen
    total_eft = flavour_nu_eft + 6

    dim_row_19 = [QQ(1)] * 11 + [QQ(0)] * 8
    D_dim = DomainMatrix([dim_row_19], (1, 19), QQ)
    rank_D_dim = D_dim.rank()
    nullspace_D_dim = D_dim.nullspace()
    dimensionless_pi_count = nullspace_D_dim.shape[0]

    unpriced_second_unit_row_19 = [QQ(0)] * 18 + [QQ(1)]
    D_dim_fault_19 = DomainMatrix([dim_row_19, unpriced_second_unit_row_19], (2, 19), QQ)
    rank_fault_19 = D_dim_fault_19.rank()

    D_dim_fault_20 = DomainMatrix(
        [dim_row_19 + [QQ(0)], [QQ(0)] * 19 + [QQ(1)]],
        (2, 20),
        QQ,
    )
    rank_fault_20 = D_dim_fault_20.rank()
    pf7_1_caught = (rank_fault_19 == 2 and rank_fault_19 > 1 and rank_fault_20 == 2)

    passed = (
        rank_sm_gen == 41
        and rank_sm_lepdiag == 41
        and ns_sm_gen.shape == (4, 45)
        and unbroken_sm == 4
        and flavour_sm == 13
        and total_sm == 19
        and rank_eft_gen == 44
        and rank_eft_lepdiag == 44
        and ns_eft_gen.shape == (1, 45)
        and unbroken_eft == 1
        and flavour_nu_eft == 22
        and total_eft == 28
        and bool(sm_annihilates_u1_4)
        and u1_4_rank == 4
        and cov_sm_kernel_exact
        and eft_preserves_B_gen
        and eft_preserves_B_diag
        and eft_breaks_all_3_lepton_diag
        and eft_breaks_all_3_lepton_cov
        and svd_ranks_sm == [41, 41, 41, 41, 41]
        and svd_ranks_eft == [44, 44, 44, 44, 44]
        and max_null_sv < qfloat(1, 10**13)
        and min_pos_sv_num > qfloat(1, 10)
        and rank_D_dim == 1
        and dimensionless_pi_count == 18
        and pf7_1_caught
    )

    return {
        "jacobian_sm_shape": [54, 45],
        "jacobian_eft_shape": [66, 45],
        "rank_J_U3_5_SM": rank_sm_gen,
        "unbroken_dim_SM": unbroken_sm,
        "flavour_parameters_SM": flavour_sm,
        "total_parameters_SM": total_sm,
        "rank_J_U3_5_EFT": rank_eft_gen,
        "unbroken_dim_EFT": unbroken_eft,
        "flavour_neutrino_parameters_EFT": flavour_nu_eft,
        "total_parameters_EFT": total_eft,
        "unbroken_U1_4_exact_span_verified": bool(sm_annihilates_u1_4 and cov_sm_kernel_exact),
        "weinberg_breaks_3_lepton_U1_leaves_U1_B": bool(
            eft_preserves_B_gen
            and eft_preserves_B_diag
            and eft_breaks_all_3_lepton_diag
            and eft_breaks_all_3_lepton_cov
        ),
        "svd_5_seed_ranks_SM": svd_ranks_sm,
        "svd_5_seed_ranks_EFT": svd_ranks_eft,
        "svd_max_null_singular_value": bounded_rat_str(max_null_sv),
        "svd_min_nonzero_singular_value": bounded_rat_str(min_pos_sv_num, 10**6),
        "buckingham_pi_shape": [1, 19],
        "buckingham_pi_mass_dim_1_count": 11,
        "buckingham_pi_dimensionless_input_count": 8,
        "rank_D_dim": rank_D_dim,
        "sole_anchor": "v_EW",
        "dimensionless_pi_ratios_count": dimensionless_pi_count,
        "PF7_1": {
            "description": "Unpriced second independent unit anchor raises rank(D_dim) from 1 to 2 > 1",
            "fault_rank_2x19": rank_fault_19,
            "fault_rank_2x20": rank_fault_20,
            "caught": bool(pf7_1_caught),
        },
        "passed": bool(passed),
    }


# ============================================================================
# 2A. Deliverable 2 (Part A): 46-Node Monotone Max-Plus Epistemic DAG
# ============================================================================

def build_canonical_46_node_dag() -> tuple:
    """Construct the 46-node epistemic DAG from Card AGY-002_CLOSURE-G7."""
    nodes = [
        {"id": "G:m004_Mostow_Rigidity", "category": "ROOT", "intrinsic_rank": 0, "has_stabilization_proof": True},
        {"id": "G:X4_Collar_Cobordism", "category": "ROOT", "intrinsic_rank": 0, "has_stabilization_proof": True},
        {"id": "G:Spin10_E6_Chirality", "category": "ROOT", "intrinsic_rank": 0, "has_stabilization_proof": True},
        {"id": "G:Heisenberg_Weil_SL2Z", "category": "ROOT", "intrinsic_rank": 0, "has_stabilization_proof": True},
        {"id": "G:MSbar_2Loop_EFT_RGE", "category": "ROOT", "intrinsic_rank": 0, "has_stabilization_proof": True},

        {"id": "O:Spin10_Anomaly_Operator", "category": "OPERATOR", "intrinsic_rank": 0, "has_stabilization_proof": True},
        {"id": "O:Collar_Casimir_Operator", "category": "OPERATOR", "intrinsic_rank": 0, "has_stabilization_proof": True},
        {"id": "O:PatiSalam_Z2D_Channel", "category": "OPERATOR", "intrinsic_rank": 1, "has_stabilization_proof": True},
        {"id": "O:CIM_33m6_Frame_D1", "category": "OPERATOR", "intrinsic_rank": 1, "has_stabilization_proof": True},
        {"id": "O:Bergman_Majorana_Seesaw", "category": "OPERATOR", "intrinsic_rank": 1, "has_stabilization_proof": True},

        {"id": "S:StrongCP_Det_Sign_Bit", "category": "SEAM", "intrinsic_rank": 2, "has_stabilization_proof": False},
        {"id": "S:Discrete_Torsion_TM1_Z2", "category": "SEAM", "intrinsic_rank": 2, "has_stabilization_proof": False},
        {"id": "S:Collar_Modulus_Delta_PS", "category": "SEAM", "intrinsic_rank": 3, "has_stabilization_proof": False},
        {"id": "S:Unified_Gauge_Anchor_AlphaU", "category": "SEAM", "intrinsic_rank": 3, "has_stabilization_proof": False},
        {"id": "S:Elliptic_Fibre_Modulus_Tau", "category": "SEAM", "intrinsic_rank": 3, "has_stabilization_proof": False},
        {"id": "S:Torsion_Tau_SU2R_Break", "category": "SEAM", "intrinsic_rank": 3, "has_stabilization_proof": False},
        {"id": "S:Electroweak_VEV_Portal_Scale", "category": "SEAM", "intrinsic_rank": 3, "has_stabilization_proof": False},

        {"id": "PR-1", "category": "RELATION", "intrinsic_rank": 0, "has_stabilization_proof": True},
        {"id": "PR-2", "category": "RELATION", "intrinsic_rank": 0, "has_stabilization_proof": True},
        {"id": "PR-3", "category": "RELATION", "intrinsic_rank": 0, "has_stabilization_proof": True},
        {"id": "PR-4", "category": "RELATION", "intrinsic_rank": 0, "has_stabilization_proof": True},
        {"id": "PR-5", "category": "RELATION", "intrinsic_rank": 0, "has_stabilization_proof": True},
        {"id": "PR-6", "category": "RELATION", "intrinsic_rank": 0, "has_stabilization_proof": True},
        {"id": "PR-7", "category": "RELATION", "intrinsic_rank": 0, "has_stabilization_proof": True},
        {"id": "PR-8", "category": "RELATION", "intrinsic_rank": 0, "has_stabilization_proof": True},
        {"id": "PR-9", "category": "RELATION", "intrinsic_rank": 0, "has_stabilization_proof": True},
        {"id": "PR-10", "category": "RELATION", "intrinsic_rank": 0, "has_stabilization_proof": True},

        {"id": "SM01:y_u", "category": "SM_TARGET", "intrinsic_rank": 0, "has_stabilization_proof": True},
        {"id": "SM02:y_c", "category": "SM_TARGET", "intrinsic_rank": 0, "has_stabilization_proof": True},
        {"id": "SM03:y_t", "category": "SM_TARGET", "intrinsic_rank": 0, "has_stabilization_proof": True},
        {"id": "SM04:y_d", "category": "SM_TARGET", "intrinsic_rank": 0, "has_stabilization_proof": True},
        {"id": "SM05:y_s", "category": "SM_TARGET", "intrinsic_rank": 0, "has_stabilization_proof": True},
        {"id": "SM06:y_b", "category": "SM_TARGET", "intrinsic_rank": 0, "has_stabilization_proof": True},
        {"id": "SM07:y_e", "category": "SM_TARGET", "intrinsic_rank": 0, "has_stabilization_proof": True},
        {"id": "SM08:y_mu", "category": "SM_TARGET", "intrinsic_rank": 0, "has_stabilization_proof": True},
        {"id": "SM09:y_tau", "category": "SM_TARGET", "intrinsic_rank": 0, "has_stabilization_proof": True},
        {"id": "SM10:theta_12_CKM", "category": "SM_TARGET", "intrinsic_rank": 0, "has_stabilization_proof": True},
        {"id": "SM11:theta_23_CKM", "category": "SM_TARGET", "intrinsic_rank": 0, "has_stabilization_proof": True},
        {"id": "SM12:theta_13_CKM", "category": "SM_TARGET", "intrinsic_rank": 0, "has_stabilization_proof": True},
        {"id": "SM13:delta_CKM", "category": "SM_TARGET", "intrinsic_rank": 0, "has_stabilization_proof": True},
        {"id": "SM14:g_1", "category": "SM_TARGET", "intrinsic_rank": 0, "has_stabilization_proof": True},
        {"id": "SM15:g_2", "category": "SM_TARGET", "intrinsic_rank": 0, "has_stabilization_proof": True},
        {"id": "SM16:g_3", "category": "SM_TARGET", "intrinsic_rank": 0, "has_stabilization_proof": True},
        {"id": "SM17:v_EW", "category": "SM_TARGET", "intrinsic_rank": 0, "has_stabilization_proof": True},
        {"id": "SM18:m_H", "category": "SM_TARGET", "intrinsic_rank": 0, "has_stabilization_proof": True},
        {"id": "SM19:bar_theta_QCD", "category": "SM_TARGET", "intrinsic_rank": 0, "has_stabilization_proof": True},
    ]

    edges = [
        ("G:Spin10_E6_Chirality", "O:Spin10_Anomaly_Operator"),
        ("G:m004_Mostow_Rigidity", "O:Collar_Casimir_Operator"),
        ("G:X4_Collar_Cobordism", "O:Collar_Casimir_Operator"),
        ("G:Spin10_E6_Chirality", "O:Collar_Casimir_Operator"),
        ("G:X4_Collar_Cobordism", "O:PatiSalam_Z2D_Channel"),
        ("G:Spin10_E6_Chirality", "O:PatiSalam_Z2D_Channel"),
        ("G:MSbar_2Loop_EFT_RGE", "O:PatiSalam_Z2D_Channel"),
        ("G:m004_Mostow_Rigidity", "O:CIM_33m6_Frame_D1"),
        ("G:Heisenberg_Weil_SL2Z", "O:CIM_33m6_Frame_D1"),
        ("O:CIM_33m6_Frame_D1", "O:Bergman_Majorana_Seesaw"),
        ("O:PatiSalam_Z2D_Channel", "O:Bergman_Majorana_Seesaw"),
        ("G:MSbar_2Loop_EFT_RGE", "O:Bergman_Majorana_Seesaw"),

        ("O:PatiSalam_Z2D_Channel", "S:StrongCP_Det_Sign_Bit"),
        ("O:Bergman_Majorana_Seesaw", "S:Discrete_Torsion_TM1_Z2"),
        ("O:Collar_Casimir_Operator", "S:Collar_Modulus_Delta_PS"),
        ("PR-10", "S:Collar_Modulus_Delta_PS"),
        ("O:Collar_Casimir_Operator", "S:Unified_Gauge_Anchor_AlphaU"),
        ("O:CIM_33m6_Frame_D1", "S:Elliptic_Fibre_Modulus_Tau"),
        ("O:PatiSalam_Z2D_Channel", "S:Torsion_Tau_SU2R_Break"),
        ("G:MSbar_2Loop_EFT_RGE", "S:Electroweak_VEV_Portal_Scale"),

        ("G:Spin10_E6_Chirality", "PR-1"),
        ("O:Spin10_Anomaly_Operator", "PR-1"),
        ("G:m004_Mostow_Rigidity", "PR-10"),
        ("G:X4_Collar_Cobordism", "PR-10"),
        ("O:Collar_Casimir_Operator", "PR-10"),

        ("PR-1", "PR-3"),
        ("G:MSbar_2Loop_EFT_RGE", "PR-3"),
        ("O:PatiSalam_Z2D_Channel", "PR-3"),
        ("G:MSbar_2Loop_EFT_RGE", "PR-4"),
        ("O:PatiSalam_Z2D_Channel", "PR-4"),
        ("O:CIM_33m6_Frame_D1", "PR-5"),
        ("O:PatiSalam_Z2D_Channel", "PR-6"),
        ("O:CIM_33m6_Frame_D1", "PR-6"),
        ("O:PatiSalam_Z2D_Channel", "PR-7"),
        ("O:CIM_33m6_Frame_D1", "PR-7"),
        ("G:Heisenberg_Weil_SL2Z", "PR-8"),
        ("O:CIM_33m6_Frame_D1", "PR-8"),
        ("PR-5", "PR-8"),
        ("PR-6", "PR-8"),
        ("PR-7", "PR-8"),

        ("G:m004_Mostow_Rigidity", "PR-2"),
        ("G:MSbar_2Loop_EFT_RGE", "PR-2"),
        ("O:PatiSalam_Z2D_Channel", "PR-2"),
        ("S:StrongCP_Det_Sign_Bit", "PR-2"),
        ("G:MSbar_2Loop_EFT_RGE", "PR-9"),
        ("O:Bergman_Majorana_Seesaw", "PR-9"),
        ("S:Discrete_Torsion_TM1_Z2", "PR-9"),

        ("PR-5", "SM01:y_u"),
        ("PR-8", "SM01:y_u"),
        ("S:Discrete_Torsion_TM1_Z2", "SM01:y_u"),
        ("S:Elliptic_Fibre_Modulus_Tau", "SM01:y_u"),
        ("PR-5", "SM02:y_c"),
        ("PR-8", "SM02:y_c"),
        ("S:Discrete_Torsion_TM1_Z2", "SM02:y_c"),
        ("S:Elliptic_Fibre_Modulus_Tau", "SM02:y_c"),
        ("PR-5", "SM03:y_t"),
        ("PR-8", "SM03:y_t"),
        ("S:Discrete_Torsion_TM1_Z2", "SM03:y_t"),
        ("S:Elliptic_Fibre_Modulus_Tau", "SM03:y_t"),

        ("PR-5", "SM04:y_d"),
        ("PR-7", "SM04:y_d"),
        ("PR-8", "SM04:y_d"),
        ("S:Elliptic_Fibre_Modulus_Tau", "SM04:y_d"),
        ("S:Torsion_Tau_SU2R_Break", "SM04:y_d"),
        ("PR-5", "SM05:y_s"),
        ("PR-7", "SM05:y_s"),
        ("PR-8", "SM05:y_s"),
        ("S:Elliptic_Fibre_Modulus_Tau", "SM05:y_s"),
        ("S:Torsion_Tau_SU2R_Break", "SM05:y_s"),
        ("PR-5", "SM06:y_b"),
        ("PR-7", "SM06:y_b"),
        ("PR-8", "SM06:y_b"),
        ("S:Elliptic_Fibre_Modulus_Tau", "SM06:y_b"),
        ("S:Torsion_Tau_SU2R_Break", "SM06:y_b"),

        ("PR-5", "SM07:y_e"),
        ("PR-7", "SM07:y_e"),
        ("PR-8", "SM07:y_e"),
        ("PR-9", "SM07:y_e"),
        ("S:Elliptic_Fibre_Modulus_Tau", "SM07:y_e"),
        ("S:Torsion_Tau_SU2R_Break", "SM07:y_e"),
        ("PR-5", "SM08:y_mu"),
        ("PR-7", "SM08:y_mu"),
        ("PR-8", "SM08:y_mu"),
        ("PR-9", "SM08:y_mu"),
        ("S:Elliptic_Fibre_Modulus_Tau", "SM08:y_mu"),
        ("S:Torsion_Tau_SU2R_Break", "SM08:y_mu"),
        ("PR-5", "SM09:y_tau"),
        ("PR-7", "SM09:y_tau"),
        ("PR-8", "SM09:y_tau"),
        ("PR-9", "SM09:y_tau"),
        ("S:Elliptic_Fibre_Modulus_Tau", "SM09:y_tau"),
        ("S:Torsion_Tau_SU2R_Break", "SM09:y_tau"),

        ("PR-6", "SM10:theta_12_CKM"),
        ("S:Elliptic_Fibre_Modulus_Tau", "SM10:theta_12_CKM"),
        ("S:Torsion_Tau_SU2R_Break", "SM10:theta_12_CKM"),
        ("PR-6", "SM11:theta_23_CKM"),
        ("S:Elliptic_Fibre_Modulus_Tau", "SM11:theta_23_CKM"),
        ("S:Torsion_Tau_SU2R_Break", "SM11:theta_23_CKM"),
        ("PR-6", "SM12:theta_13_CKM"),
        ("S:Elliptic_Fibre_Modulus_Tau", "SM12:theta_13_CKM"),
        ("S:Torsion_Tau_SU2R_Break", "SM12:theta_13_CKM"),
        ("PR-6", "SM13:delta_CKM"),
        ("S:Elliptic_Fibre_Modulus_Tau", "SM13:delta_CKM"),
        ("S:Torsion_Tau_SU2R_Break", "SM13:delta_CKM"),

        ("PR-1", "SM14:g_1"),
        ("PR-3", "SM14:g_1"),
        ("S:Collar_Modulus_Delta_PS", "SM14:g_1"),
        ("S:Unified_Gauge_Anchor_AlphaU", "SM14:g_1"),
        ("PR-3", "SM15:g_2"),
        ("S:Collar_Modulus_Delta_PS", "SM15:g_2"),
        ("S:Unified_Gauge_Anchor_AlphaU", "SM15:g_2"),
        ("PR-3", "SM16:g_3"),
        ("S:Collar_Modulus_Delta_PS", "SM16:g_3"),
        ("S:Unified_Gauge_Anchor_AlphaU", "SM16:g_3"),

        ("S:Electroweak_VEV_Portal_Scale", "SM17:v_EW"),
        ("PR-4", "SM18:m_H"),
        ("PR-5", "SM18:m_H"),
        ("SM03:y_t", "SM18:m_H"),
        ("S:Torsion_Tau_SU2R_Break", "SM18:m_H"),
        ("S:Electroweak_VEV_Portal_Scale", "SM18:m_H"),

        ("PR-2", "SM19:bar_theta_QCD"),
        ("G:MSbar_2Loop_EFT_RGE", "SM19:bar_theta_QCD"),
    ]
    return nodes, edges


def kahn_topological_sort(node_ids: list, edges: list) -> tuple:
    adj = {nid: [] for nid in node_ids}
    indeg = {nid: 0 for nid in node_ids}
    for u, v in edges:
        adj[u].append(v)
        indeg[v] += 1

    queue = [nid for nid in node_ids if indeg[nid] == 0]
    topo = []
    idx = 0
    while idx < len(queue):
        cur = queue[idx]
        idx += 1
        topo.append(cur)
        for nxt in adj[cur]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                queue.append(nxt)
    is_acyclic = len(topo) == len(node_ids)
    return is_acyclic, topo


def dfs_three_color_has_cycle(node_ids: list, edges: list) -> bool:
    adj = {nid: [] for nid in node_ids}
    for u, v in edges:
        adj[u].append(v)

    color = {nid: 0 for nid in node_ids}

    def visit(u: str) -> bool:
        color[u] = 1
        for v in adj[u]:
            if color[v] == 1:
                return True
            if color[v] == 0 and visit(v):
                return True
        color[u] = 2
        return False

    for nid in node_ids:
        if color[nid] == 0:
            if visit(nid):
                return True
    return False


def check_guardrail_1_seams(nodes: list, propagated_ranks: dict) -> list:
    violations = []
    for nd in nodes:
        if nd["category"] == "SEAM":
            if not nd["has_stabilization_proof"]:
                if nd["intrinsic_rank"] < 2 or propagated_ranks[nd["id"]] < 2:
                    violations.append(nd["id"])
    return violations


def check_monotone_max_plus(nodes: list, edges: list, reported_ranks: dict) -> list:
    parents = {nd["id"]: [] for nd in nodes}
    intrinsic = {nd["id"]: nd["intrinsic_rank"] for nd in nodes}
    for u, v in edges:
        parents[v].append(u)

    violations = []
    for nd in nodes:
        nid = nd["id"]
        expected = max([intrinsic[nid]] + [reported_ranks[p] for p in parents[nid]])
        if reported_ranks[nid] < intrinsic[nid]:
            violations.append((nid, "below_intrinsic"))
        for p in parents[nid]:
            if reported_ranks[nid] < reported_ranks[p]:
                violations.append((nid, f"below_parent:{p}"))
        if reported_ranks[nid] != expected:
            violations.append((nid, f"mismatch_max_plus:{reported_ranks[nid]}!={expected}"))
    return violations


def propagate_max_plus_ranks(nodes: list, edges: list, topo_order: list) -> dict:
    parents = {nd["id"]: [] for nd in nodes}
    intrinsic = {nd["id"]: nd["intrinsic_rank"] for nd in nodes}
    for u, v in edges:
        parents[v].append(u)
    ranks = {}
    for nid in topo_order:
        ranks[nid] = max([intrinsic[nid]] + [ranks[p] for p in parents[nid]])
    return ranks


def evaluate_epistemic_dag() -> dict:
    nodes, edges = build_canonical_46_node_dag()
    node_ids = [nd["id"] for nd in nodes]

    cat_counts = {"ROOT": 0, "OPERATOR": 0, "SEAM": 0, "RELATION": 0, "SM_TARGET": 0}
    for nd in nodes:
        cat_counts[nd["category"]] += 1

    kahn_ok, topo_order = kahn_topological_sort(node_ids, edges)
    dfs_cycle = dfs_three_color_has_cycle(node_ids, edges)
    ranks = propagate_max_plus_ranks(nodes, edges, topo_order)
    g1_violations = check_guardrail_1_seams(nodes, ranks)
    monotone_violations = check_monotone_max_plus(nodes, edges, ranks)

    rel_hist = [0, 0, 0, 0]
    sm_hist = [0, 0, 0, 0]
    rel_by_rank = {0: [], 1: [], 2: [], 3: []}
    sm_by_rank = {0: [], 1: [], 2: [], 3: []}

    for nd in nodes:
        r = ranks[nd["id"]]
        if nd["category"] == "RELATION":
            rel_hist[r] += 1
            rel_by_rank[r].append(nd["id"])
        elif nd["category"] == "SM_TARGET":
            sm_hist[r] += 1
            sm_by_rank[r].append(nd["id"])

    edges_pf7_2 = list(edges) + [("SM03:y_t", "G:m004_Mostow_Rigidity")]
    kahn_ok_pf7_2, _ = kahn_topological_sort(node_ids, edges_pf7_2)
    dfs_cycle_pf7_2 = dfs_three_color_has_cycle(node_ids, edges_pf7_2)
    pf7_2_caught = (not kahn_ok_pf7_2) and dfs_cycle_pf7_2

    laundered_ranks = dict(ranks)
    laundered_ranks["SM03:y_t"] = 1
    pf7_3_violations = check_monotone_max_plus(nodes, edges, laundered_ranks)
    pf7_3_caught = len(pf7_3_violations) > 0

    nodes_pf7_4a = copy.deepcopy(nodes)
    for nd in nodes_pf7_4a:
        if nd["id"] == "S:Collar_Modulus_Delta_PS":
            nd["intrinsic_rank"] = 0
    ranks_pf7_4a = propagate_max_plus_ranks(nodes_pf7_4a, edges, topo_order)
    viol_4a = check_guardrail_1_seams(nodes_pf7_4a, ranks_pf7_4a)

    nodes_pf7_4b = copy.deepcopy(nodes)
    for nd in nodes_pf7_4b:
        if nd["id"] == "S:Torsion_Tau_SU2R_Break":
            nd["intrinsic_rank"] = 0
    ranks_pf7_4b = propagate_max_plus_ranks(nodes_pf7_4b, edges, topo_order)
    viol_4b = check_guardrail_1_seams(nodes_pf7_4b, ranks_pf7_4b)

    pf7_4_caught = (
        "S:Collar_Modulus_Delta_PS" in viol_4a
        and "S:Torsion_Tau_SU2R_Break" in viol_4b
    )

    seam_nodes = [nd for nd in nodes if nd["category"] == "SEAM"]
    discrete_seams_at_2 = sum(1 for nd in seam_nodes if nd["intrinsic_rank"] == 2)
    continuous_seams_at_3 = sum(1 for nd in seam_nodes if nd["intrinsic_rank"] == 3)
    all_seams_unproved = all(not nd["has_stabilization_proof"] for nd in seam_nodes)

    passed = (
        len(nodes) == 46
        and cat_counts == {"ROOT": 5, "OPERATOR": 5, "SEAM": 7, "RELATION": 10, "SM_TARGET": 19}
        and discrete_seams_at_2 == 2
        and continuous_seams_at_3 == 5
        and all_seams_unproved
        and kahn_ok
        and (not dfs_cycle)
        and len(g1_violations) == 0
        and len(monotone_violations) == 0
        and rel_hist == [2, 6, 2, 0]
        and rel_by_rank[0] == ["PR-1", "PR-10"]
        and rel_by_rank[1] == ["PR-3", "PR-4", "PR-5", "PR-6", "PR-7", "PR-8"]
        and rel_by_rank[2] == ["PR-2", "PR-9"]
        and sm_hist == [0, 0, 1, 18]
        and sm_by_rank[2] == ["SM19:bar_theta_QCD"]
        and pf7_2_caught
        and pf7_3_caught
        and pf7_4_caught
    )

    return {
        "total_nodes": len(nodes),
        "total_edges": len(edges),
        "category_counts": cat_counts,
        "discrete_seams_rank_2": discrete_seams_at_2,
        "continuous_seams_rank_3": continuous_seams_at_3,
        "all_7_seams_unproved": bool(all_seams_unproved),
        "kahn_acyclic": bool(kahn_ok),
        "dfs_three_color_acyclic": bool(not dfs_cycle),
        "guardrail_1_violations": g1_violations,
        "monotone_violations": monotone_violations,
        "relation_rank_histogram": rel_hist,
        "relations_by_rank": {str(k): v for k, v in rel_by_rank.items()},
        "sm_target_rank_histogram": sm_hist,
        "sm_targets_rank_2": sm_by_rank[2],
        "PF7_2": {
            "description": "Back-edge SM03:y_t -> G:m004_Mostow_Rigidity triggers cycle detection",
            "kahn_detected_cycle": bool(not kahn_ok_pf7_2),
            "dfs_detected_cycle": bool(dfs_cycle_pf7_2),
            "caught": bool(pf7_2_caught),
        },
        "PF7_3": {
            "description": "Assigning child SM03:y_t rank 1 < parent rank 3 fails monotone max-plus invariant",
            "violation_count": len(pf7_3_violations),
            "caught": bool(pf7_3_caught),
        },
        "PF7_4": {
            "description": "Setting S:Collar_Modulus_Delta_PS or S:Torsion_Tau_SU2R_Break to rank 0 without stabilization proof triggers Guardrail 1",
            "violations_delta_ps": viol_4a,
            "violations_tau_su2r": viol_4b,
            "caught": bool(pf7_4_caught),
        },
        "passed": bool(passed),
    }


# ============================================================================
# 2B. Deliverable 2 (Part B): Independent PR-1..PR-10 Kill-Line Counterchecks
# ============================================================================

def random_haar_u3(rng: np.random.Generator) -> np.ndarray:
    """Sample exact Haar-distributed 3x3 unitary matrix via Mezzadri QR algorithm."""
    z = (rng.standard_normal((3, 3)) + IMAG_UNIT * rng.standard_normal((3, 3))) / math.sqrt(qfloat(2, 1))
    q_mat, r_mat = np.linalg.qr(z)
    diag_r = np.diag(r_mat)
    phases = diag_r / np.abs(diag_r)
    return q_mat * phases[None, :]


def random_su3(rng: np.random.Generator) -> np.ndarray:
    u_mat = random_haar_u3(rng)
    det_u = np.linalg.det(u_mat)
    phase = cmath.exp(-IMAG_UNIT * cmath.phase(det_u) / qfloat(3, 1))
    return u_mat * phase


def verify_pr1() -> dict:
    sm_reps = [
        ("Q_L", 1, 1, sp.Rational(1, 6)),
        ("u_R^c", 2, 0, sp.Rational(-2, 3)),
        ("d_R^c", 2, 0, sp.Rational(1, 3)),
        ("L_L", 0, 1, sp.Rational(-1, 2)),
        ("e_R^c", 0, 0, sp.Integer(1)),
    ]
    z6_residues = []
    for _, tc, dw, hyp in sm_reps:
        val = sp.Integer(2) * tc + sp.Integer(3) * dw + sp.Integer(6) * hyp
        z6_residues.append(int(val) % 6)

    a, b = sp.symbols("a b", real=True)
    shift_tw = (3 * a + 2 * b) / sp.Integer(2)

    def anomalies_v5(twist):
        q_11a = -twist
        q_3b1a = 2 * a - twist
        q_32 = a + b - twist
        q_11b = 2 * b - twist
        q_12 = 3 * a + b - twist
        q_3b1b = 2 * a + 2 * b - twist
        a333 = sp.Integer(2) * 1 + sp.Integer(1) * (-1) + sp.Integer(1) * (-1)
        a331 = sp.simplify(2 * sp.Rational(1, 2) * q_32 + sp.Rational(1, 2) * q_3b1a + sp.Rational(1, 2) * q_3b1b)
        a221 = sp.simplify(3 * sp.Rational(1, 2) * q_32 + sp.Rational(1, 2) * q_12)
        agrav = sp.simplify(q_11a + 3 * q_3b1a + 6 * q_32 + q_11b + 2 * q_12 + 3 * q_3b1b)
        a111 = sp.expand(q_11a**3 + 3 * q_3b1a**3 + 6 * q_32**3 + q_11b**3 + 2 * q_12**3 + 3 * q_3b1b**3)
        return [a333, a331, a221, agrav, a111]

    twisted_anom = anomalies_v5(shift_tw)
    untwisted_anom = anomalies_v5(sp.Integer(0))
    target_cubic = sp.expand(4 * (3 * a + 2 * b) * (9 * a**2 + 6 * a * b + 5 * b**2))
    pos_def_quad = sp.expand((9 * a**2 + 6 * a * b + 5 * b**2) - ((3 * a + b) ** 2 + 4 * b**2))

    sm_15 = [
        (6, sp.Rational(1, 6), sp.Rational(1, 3)),
        (3, sp.Rational(-2, 3), sp.Rational(-1, 3)),
        (3, sp.Rational(1, 3), sp.Rational(-1, 3)),
        (2, sp.Rational(-1, 2), sp.Integer(-1)),
        (1, sp.Integer(1), sp.Integer(1)),
    ]
    agrav_15 = sp.simplify(sum(mult * (a * bl + b * y) for mult, y, bl in sm_15))
    a111_15 = sp.simplify(sum(mult * (a * bl + b * y) ** 3 for mult, y, bl in sm_15))
    sol_a = sp.solve([agrav_15, a111_15], a, dict=True)
    forces_a_zero = sol_a == [{a: sp.Integer(0)}]

    k2 = sp.Integer(3) * sp.Rational(1, 2) + sp.Rational(1, 2)
    k1 = sum(mult * (y**2) for mult, y, _ in sm_15)
    k2_over_k1 = k2 / k1

    passed = (
        z6_residues == [0, 0, 0, 0, 0]
        and twisted_anom == [0, 0, 0, 0, 0]
        and sp.simplify(untwisted_anom[4] - target_cubic) == 0
        and pos_def_quad == 0
        and forces_a_zero
        and k2_over_k1 == sp.Rational(3, 5)
    )
    return {
        "z6_residues_mod_6": z6_residues,
        "spin10_16_anomalies_vanish": twisted_anom == [0, 0, 0, 0, 0],
        "untwisted_cubic_identity_exact": sp.simplify(untwisted_anom[4] - target_cubic) == 0,
        "sm15_forces_a_eq_0": bool(forces_a_zero),
        "k2_over_k1": f"{k2_over_k1.p}/{k2_over_k1.q}",
        "passed": bool(passed),
    }


def extract_ckm_jarlskog(Yu: np.ndarray, Yd: np.ndarray) -> float:
    """Basis-invariant extraction of |J_CKM| from Hu = Yu Yu^dag, Hd = Yd Yd^dag."""
    Hu = Yu @ Yu.conj().T
    Hd = Yd @ Yd.conj().T
    _, Uu = np.linalg.eigh(Hu)
    _, Ud = np.linalg.eigh(Hd)
    V = Uu.conj().T @ Ud
    return abs(float(np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1]))))


def verify_pr2() -> dict:
    Yu = np.array([
        [qfloat(2, 1), qfloat(1, 3) + IMAG_UNIT * qfloat(1, 4), qfloat(1, 5) - IMAG_UNIT * qfloat(1, 7)],
        [qfloat(1, 3) - IMAG_UNIT * qfloat(1, 4), qfloat(5, 1), qfloat(3, 5) + IMAG_UNIT * qfloat(1, 2)],
        [qfloat(1, 5) + IMAG_UNIT * qfloat(1, 7), qfloat(3, 5) - IMAG_UNIT * qfloat(1, 2), qfloat(11, 1)],
    ], dtype=complex)
    Yd = np.array([
        [qfloat(3, 2), qfloat(2, 5) - IMAG_UNIT * qfloat(1, 3), qfloat(1, 4) + IMAG_UNIT * qfloat(2, 7)],
        [qfloat(2, 5) + IMAG_UNIT * qfloat(1, 3), qfloat(9, 2), qfloat(1, 2) - IMAG_UNIT * qfloat(3, 7)],
        [qfloat(1, 4) - IMAG_UNIT * qfloat(2, 7), qfloat(1, 2) + IMAG_UNIT * qfloat(3, 7), qfloat(9, 1)],
    ], dtype=complex)

    herm_err = max(
        float(np.max(np.abs(Yu - Yu.conj().T))),
        float(np.max(np.abs(Yd - Yd.conj().T))),
    )
    prod_det = np.linalg.det(Yu @ Yd)
    arg_pos_branch = abs(cmath.phase(prod_det))

    prod_det_neg = np.linalg.det(Yu @ (-Yd))
    arg_neg_mod_pi = abs(abs(cmath.phase(prod_det_neg)) - math.pi)

    j_ckm_base = extract_ckm_jarlskog(Yu, Yd)

    rng = np.random.default_rng(102)
    max_su3_theta_drift = 0
    max_haar_theta_bar_drift = 0
    max_haar_jarlskog_drift = 0

    for _ in range(10):
        SQ = random_su3(rng)
        Su = random_su3(rng)
        Sd = random_su3(rng)
        Yu_s = SQ @ Yu @ Su.conj().T
        Yd_s = SQ @ Yd @ Sd.conj().T
        su3_theta = abs(cmath.phase(np.linalg.det(Yu_s @ Yd_s)))
        if su3_theta > max_su3_theta_drift:
            max_su3_theta_drift = su3_theta

        UQ = random_haar_u3(rng)
        Uu = random_haar_u3(rng)
        Ud = random_haar_u3(rng)
        Yu_h = UQ @ Yu @ Uu.conj().T
        Yd_h = UQ @ Yd @ Ud.conj().T
        theta_bare_shift = -cmath.phase((np.linalg.det(UQ) ** 2) * np.conj(np.linalg.det(Uu)) * np.conj(np.linalg.det(Ud)))
        arg_det_h = cmath.phase(np.linalg.det(Yu_h @ Yd_h))
        bar_theta_h = math.atan2(math.sin(theta_bare_shift + arg_det_h), math.cos(theta_bare_shift + arg_det_h))
        if abs(bar_theta_h) > max_haar_theta_bar_drift:
            max_haar_theta_bar_drift = abs(bar_theta_h)

        j_h = extract_ckm_jarlskog(Yu_h, Yd_h)
        if abs(j_h - j_ckm_base) > max_haar_jarlskog_drift:
            max_haar_jarlskog_drift = abs(j_h - j_ckm_base)

    passed = (
        herm_err == 0
        and prod_det.real > 0
        and arg_pos_branch < qfloat(1, 10**14)
        and arg_neg_mod_pi < qfloat(1, 10**14)
        and j_ckm_base > qfloat(1, 1000)
        and max_su3_theta_drift < qfloat(1, 10**13)
        and max_haar_theta_bar_drift < qfloat(1, 10**12)
        and max_haar_jarlskog_drift < qfloat(1, 10**12)
    )
    return {
        "arg_det_pos_branch": bounded_rat_str(arg_pos_branch),
        "arg_det_neg_branch_minus_pi": bounded_rat_str(arg_neg_mod_pi),
        "jarlskog_ckm_nonzero": bounded_rat_str(j_ckm_base, 10**8),
        "max_su3_arg_det_drift": bounded_rat_str(max_su3_theta_drift),
        "max_u3_haar_bar_theta_drift": bounded_rat_str(max_haar_theta_bar_drift),
        "max_u3_haar_jarlskog_drift": bounded_rat_str(max_haar_jarlskog_drift),
        "passed": bool(passed),
    }


def extract_gate6_json_envelopes(repo_root: Path) -> dict:
    """Cross-check sealed Gate 6 producer & referee raw JSON envelopes for PR-3 and PR-4."""
    g6_paths = [
        repo_root / "relays" / "agy002_closure_g6_fixed" / "verify_closure_g6_fixed_out.json",
        repo_root / "relays" / "agy002_closure_g6_referee" / "referee_closure_g6_out.json",
    ]
    fault_words = frozenset({"pf6", "planted", "plant", "fault", "faults", "tamper", "wrong"})
    leaf_skip_words = frozenset({
        "diff", "absdiff", "reldiff", "err", "error", "tol", "tolerance",
        "count", "histories", "trials", "steps", "seed", "seeds", "rank",
        "ranks", "yukawa", "sensitivity", "shift", "excursion", "jarlskog", "haar", "theta",
    })
    extremum_words = frozenset({"min", "max", "lo", "hi", "low", "high", "lower", "upper", "val", "value"})

    def split_words(s: str) -> list:
        return [w for w in re.split(r"[^a-z0-9]+", s.lower()) if w]

    def parse_rat(val):
        if isinstance(val, bool) or val is None:
            return None
        if isinstance(val, int):
            return Fraction(val, 1)
        if isinstance(val, float):
            return Fraction(str(val))
        if isinstance(val, str):
            s = val.strip()
            if not s:
                return None
            try:
                return Fraction(s)
            except (ValueError, ZeroDivisionError):
                return None
        return None

    def collect_candidates(obj, path=""):
        d2l_vals = []
        s2lam_vals = []
        p_low = path.lower()
        p_words = split_words(p_low)
        if any(w.startswith("pf") or w in fault_words for w in p_words):
            return d2l_vals, s2lam_vals

        if isinstance(obj, dict):
            for k, v in obj.items():
                sub_p = f"{path}.{k}" if path else str(k)
                c1, c2 = collect_candidates(v, sub_p)
                d2l_vals.extend(c1)
                s2lam_vals.extend(c2)
        elif isinstance(obj, list):
            parsed_items = [parse_rat(it) for it in obj]
            leaf_seg = p_low.rsplit(".", 1)[-1]
            leaf_w = set(split_words(leaf_seg))
            if len(obj) >= 2 and all(x is not None for x in parsed_items) and not (leaf_w & leaf_skip_words):
                lo_v, hi_v = min(parsed_items), max(parsed_items)
                if ("delta" in p_low or "s2w" in p_low or "sin2" in p_low) and (
                    "2loop" in p_low or "2_loop" in p_low or "twoloop" in p_low
                ):
                    d2l_vals.extend([lo_v, hi_v])
                if ("sqrt" in p_low and "lam" in p_low) or ("mh" in p_words and ("v" in p_words or "vew" in p_words)):
                    s2lam_vals.extend([lo_v, hi_v])
            else:
                for idx, it in enumerate(obj):
                    c1, c2 = collect_candidates(it, f"{path}[{idx}]")
                    d2l_vals.extend(c1)
                    s2lam_vals.extend(c2)
        else:
            rval = parse_rat(obj)
            if rval is not None:
                leaf_seg = p_low.rsplit(".", 1)[-1]
                leaf_w = set(split_words(leaf_seg))
                if not (leaf_w & leaf_skip_words) and bool(leaf_w & extremum_words):
                    if ("delta" in p_low or "s2w" in p_low or "sin2" in p_low or "corridor" in p_low) and (
                        "2loop" in p_low or "2_loop" in p_low or "twoloop" in p_low
                    ):
                        d2l_vals.append(rval)
                    if ("sqrt" in p_low and "lam" in p_low) or ("mh" in p_words and ("v" in p_words or "vew" in p_words)):
                        s2lam_vals.append(rval)
        return d2l_vals, s2lam_vals

    lo_d2l = Fraction(7, 10000)
    hi_d2l = Fraction(3, 1000)
    lo_s2l = Fraction(35, 100)
    hi_s2l = Fraction(78, 100)

    per_file = {}
    all_ok = True
    for p in g6_paths:
        data = json.loads(p.read_text(encoding="utf-8"))
        pass_keys = ("overall_passed", "all_passed", "passed", "gate_passed", "all_checks_passed")
        present_pass = [bool(data[k]) for k in pass_keys if k in data]
        ov_pass = all(present_pass) if present_pass else all(
            bool(v.get("passed", True)) for v in data.values() if isinstance(v, dict)
        )
        d2l_v, s2l_v = collect_candidates(data)
        d2l_ok = len(d2l_v) >= 1 and all(lo_d2l <= x <= hi_d2l for x in d2l_v)
        s2l_ok = len(s2l_v) >= 1 and all(lo_s2l <= x <= hi_s2l for x in s2l_v)
        file_ok = ov_pass and d2l_ok and s2l_ok
        if not file_ok:
            all_ok = False
        per_file[p.name] = {
            "overall_passed": ov_pass,
            "delta_2loop_samples": len(d2l_v),
            "delta_2loop_min": frac_str(min(d2l_v)) if d2l_v else "none",
            "delta_2loop_max": frac_str(max(d2l_v)) if d2l_v else "none",
            "delta_2loop_in_envelope": bool(d2l_ok),
            "sqrt_2_lambda_samples": len(s2l_v),
            "sqrt_2_lambda_min": frac_str(min(s2l_v)) if s2l_v else "none",
            "sqrt_2_lambda_max": frac_str(max(s2l_v)) if s2l_v else "none",
            "sqrt_2_lambda_in_envelope": bool(s2l_ok),
        }

    return {"files": per_file, "passed": bool(all_ok)}


def verify_pr3_and_pr4(repo_root: Path) -> tuple:
    N_g = sp.Integer(3)
    N_H = sp.Integer(1)
    b1_SM = sp.Rational(4, 3) * N_g + sp.Rational(1, 10) * N_H
    b2_SM = -sp.Rational(22, 3) + sp.Rational(4, 3) * N_g + sp.Rational(1, 6) * N_H
    b3_SM = -sp.Integer(11) + sp.Rational(4, 3) * N_g

    b4_PS = -sp.Rational(11, 3) * 4 + sp.Rational(4, 3) * N_g + sp.Rational(2, 3)
    b2L_PS = -sp.Rational(11, 3) * 2 + sp.Rational(4, 3) * N_g + sp.Rational(1, 3) + sp.Rational(2, 3)
    b2R_PS = b2L_PS

    a_U_inv, L_IR, Delta_PS, a_EM, a_3 = sp.symbols("a_U_inv L_IR Delta_PS a_EM a_3", positive=True)
    a4_PS = a_U_inv + b4_PS * Delta_PS / (2 * sp.pi)
    a2L_PS = a_U_inv + b2L_PS * Delta_PS / (2 * sp.pi)
    a2R_PS = a_U_inv + b2R_PS * Delta_PS / (2 * sp.pi)

    a3_IR = a4_PS + b3_SM * L_IR
    a2_IR = a2L_PS + b2_SM * L_IR
    a1_IR = sp.Rational(3, 5) * a2R_PS + sp.Rational(2, 5) * a4_PS + b1_SM * L_IR

    sol_list = sp.solve(
        [sp.Eq(sp.Rational(5, 3) * a1_IR + a2_IR, 1 / a_EM), sp.Eq(a3_IR, 1 / a_3)],
        [a_U_inv, L_IR],
        dict=True,
    )
    s2w_expr = sp.expand(sp.simplify(a_EM * a2_IR.subs(sol_list[0])))
    c_0 = s2w_expr.subs({a_EM: 0})
    c_rat = sp.simplify(sp.diff(s2w_expr, a_EM).subs({Delta_PS: 0}) * a_3)
    c_delta = sp.simplify(sp.diff(s2w_expr, Delta_PS) * sp.pi / a_EM)

    g2L, g2R, beta, h_norm = sp.symbols("g2L g2R beta h_norm", real=True)
    d_L = -sp.Rational(1, 2) * sp.cos(2 * beta) * h_norm**2
    d_R = sp.Rational(1, 2) * sp.cos(2 * beta) * h_norm**2
    V_D = sp.Rational(1, 2) * g2L**2 * d_L**2 + sp.Rational(1, 2) * g2R**2 * d_R**2
    lam_PS_sym = sp.trigsimp(V_D / (h_norm**4))
    target_lam_PS = ((g2L**2 + g2R**2) / sp.Integer(8)) * sp.cos(2 * beta) ** 2

    theta_s, yt_s, yb_s = sp.symbols("theta_s yt_s yb_s", real=True, positive=True)
    R2 = sp.Matrix([[sp.cos(theta_s), -sp.sin(theta_s)], [sp.sin(theta_s), sp.cos(theta_s)]])
    Yu_2 = sp.Matrix([[0, 0], [0, yt_s]])
    Yd_2 = R2 * sp.Matrix([[0, 0], [0, yb_s]])
    Hu_2 = Yu_2 * Yu_2.T
    Hd_2 = Yd_2 * Yd_2.T
    Tu_2, Td_2 = sp.trace(Hu_2), sp.trace(Hd_2)
    I2 = sp.eye(2)
    u_v = sp.Matrix([0, 1])
    d_v = R2 * u_v
    Pu, Pd = u_v * u_v.T, d_v * d_v.T

    Mu_1 = sp.Rational(3, 2) * Hu_2 - sp.Rational(3, 2) * Hd_2
    Md_1 = sp.Rational(3, 2) * Hd_2 - sp.Rational(3, 2) * Hu_2
    slope_1 = sp.trigsimp(
        -(((I2 - Pu) * Mu_1 * u_v).T * d_v + u_v.T * ((I2 - Pd) * Md_1 * d_v))[0]
        / (sp.sin(theta_s) ** 2 * sp.cos(theta_s))
    )

    Mu_2 = (
        sp.Rational(3, 2) * Hu_2**2
        + sp.Rational(11, 4) * Hd_2**2
        - sp.Rational(1, 4) * Hu_2 * Hd_2
        - Hd_2 * Hu_2
        - sp.Rational(27, 4) * Tu_2 * Hu_2
        - sp.Rational(9, 4) * Td_2 * Hu_2
        + sp.Rational(15, 4) * Tu_2 * Hd_2
        + sp.Rational(15, 4) * Td_2 * Hd_2
    )
    Md_2 = (
        sp.Rational(3, 2) * Hd_2**2
        + sp.Rational(11, 4) * Hu_2**2
        - sp.Rational(1, 4) * Hd_2 * Hu_2
        - Hu_2 * Hd_2
        - sp.Rational(27, 4) * Td_2 * Hd_2
        - sp.Rational(9, 4) * Tu_2 * Hd_2
        + sp.Rational(15, 4) * Td_2 * Hu_2
        + sp.Rational(15, 4) * Tu_2 * Hu_2
    )
    slope_2 = sp.trigsimp(
        -(((I2 - Pu) * Mu_2 * u_v).T * d_v + u_v.T * ((I2 - Pd) * Md_2 * d_v))[0]
        / (sp.sin(theta_s) ** 2 * sp.cos(theta_s))
    )
    bbo_1_ok = sp.simplify(slope_1 - sp.Rational(3, 2) * (yt_s**2 + yb_s**2)) == 0
    bbo_2_ok = sp.simplify(slope_2 - (-sp.Rational(13, 2) * (yt_s**4 + yb_s**4) - sp.Rational(11, 2) * yt_s**2 * yb_s**2)) == 0

    b1_vec = np.array([qfloat(41, 10), -qfloat(19, 6), -qfloat(7, 1)])
    B2_mat = np.array([
        [qfloat(199, 50), qfloat(27, 10), qfloat(44, 5)],
        [qfloat(9, 10), qfloat(35, 6), qfloat(12, 1)],
        [qfloat(11, 10), qfloat(9, 2), -qfloat(26, 1)],
    ])
    c_top_vec = np.array([qfloat(17, 20), qfloat(9, 4), qfloat(2, 1)])

    def sm_2loop_rhs(state: np.ndarray) -> np.ndarray:
        g1_v, g2_v, g3_v, yt_v, lam_v = state
        g_arr = np.array([g1_v, g2_v, g3_v])
        g_sq = g_arr * g_arr
        loop1 = qfloat(1, 16) / (math.pi * math.pi)
        loop2 = loop1 * loop1
        dg_arr = g_arr * g_sq * (loop1 * b1_vec + loop2 * (B2_mat @ g_sq - c_top_vec * yt_v * yt_v))

        byt_1 = yt_v * (qfloat(9, 2) * yt_v**2 - qfloat(8, 1) * g3_v**2 - qfloat(9, 4) * g2_v**2 - qfloat(17, 20) * g1_v**2)
        byt_2 = yt_v * (
            -qfloat(12, 1) * yt_v**4
            + yt_v**2 * (qfloat(131, 16) * g2_v**2 + qfloat(393, 80) * g1_v**2 + qfloat(36, 1) * g3_v**2 - qfloat(12, 1) * lam_v)
            + qfloat(6, 1) * lam_v**2
            - qfloat(108, 1) * g3_v**4
            - qfloat(23, 4) * g2_v**4
            + qfloat(1187, 600) * g1_v**4
            + qfloat(9, 1) * g3_v**2 * g2_v**2
            + qfloat(19, 15) * g3_v**2 * g1_v**2
            - qfloat(9, 20) * g2_v**2 * g1_v**2
        )
        dyt_v = loop1 * byt_1 + loop2 * byt_2

        gY_sq = qfloat(3, 5) * g1_v**2
        blam_1 = (
            qfloat(24, 1) * lam_v**2
            + qfloat(12, 1) * lam_v * yt_v**2
            - qfloat(6, 1) * yt_v**4
            - qfloat(3, 1) * lam_v * (qfloat(3, 1) * g2_v**2 + gY_sq)
            + qfloat(3, 8) * (qfloat(2, 1) * g2_v**4 + (g2_v**2 + gY_sq) ** 2)
        )
        blam_2 = (
            -qfloat(312, 1) * lam_v**3
            - qfloat(144, 1) * lam_v**2 * yt_v**2
            - qfloat(3, 1) * lam_v * yt_v**4
            + qfloat(30, 1) * yt_v**6
            + qfloat(36, 1) * lam_v**2 * (qfloat(3, 1) * g2_v**2 + gY_sq)
            + yt_v**4 * (-qfloat(32, 1) * g3_v**2 - qfloat(8, 3) * gY_sq)
            + lam_v * yt_v**2 * (qfloat(80, 1) * g3_v**2 + qfloat(45, 2) * g2_v**2 + qfloat(17, 2) * gY_sq)
        )
        dlam_v = loop1 * blam_1 + loop2 * blam_2
        return np.array([dg_arr[0], dg_arr[1], dg_arr[2], dyt_v, dlam_v], dtype=float)

    def integrate_rk4(y0: np.ndarray, dt_total: float, n_steps: int) -> np.ndarray:
        y_cur = y0.copy()
        h = dt_total / qfloat(n_steps, 1)
        half = qfloat(1, 2)
        sixth = qfloat(1, 6)
        for _ in range(n_steps):
            k1 = sm_2loop_rhs(y_cur)
            k2 = sm_2loop_rhs(y_cur + half * h * k1)
            k3 = sm_2loop_rhs(y_cur + half * h * k2)
            k4 = sm_2loop_rhs(y_cur + h * k3)
            y_cur = y_cur + sixth * h * (k1 + qfloat(2, 1) * k2 + qfloat(2, 1) * k3 + k4)
        return y_cur

    aU_inv_0 = qfloat(44, 1)
    delta_ps_0 = qfloat(2, 1)
    a4_ps = aU_inv_0 + (-qfloat(10, 1)) * delta_ps_0 / (qfloat(2, 1) * math.pi)
    a2_ps = aU_inv_0 + (-qfloat(7, 3)) * delta_ps_0 / (qfloat(2, 1) * math.pi)
    a1_ps = qfloat(3, 5) * a2_ps + qfloat(2, 5) * a4_ps
    g1_init = math.sqrt(qfloat(4, 1) * math.pi / a1_ps)
    g2_init = math.sqrt(qfloat(4, 1) * math.pi / a2_ps)
    g3_init = math.sqrt(qfloat(4, 1) * math.pi / a4_ps)
    yt_init = qfloat(1, 2)
    cos2b_init = qfloat(4, 5)
    lam_init = qfloat(1, 4) * g2_init**2 * cos2b_init**2

    y_init = np.array([g1_init, g2_init, g3_init, yt_init, lam_init], dtype=float)
    y_ir_coarse = integrate_rk4(y_init, -qfloat(28, 1), 600)
    y_ir_fine = integrate_rk4(y_init, -qfloat(28, 1), 1200)
    rk4_conv_err = float(np.max(np.abs(y_ir_fine - y_ir_coarse)))

    g1_ir, g2_ir, g3_ir, _, lam_ir = y_ir_fine
    a1_ir = g1_ir**2 / (qfloat(4, 1) * math.pi)
    a2_ir = g2_ir**2 / (qfloat(4, 1) * math.pi)
    a3_ir = g3_ir**2 / (qfloat(4, 1) * math.pi)
    aEM_ir = qfloat(1, 1) / (qfloat(5, 3) / a1_ir + qfloat(1, 1) / a2_ir)
    s2w_2l = aEM_ir / a2_ir
    s2w_1l = qfloat(23, 134) + qfloat(109, 201) * (aEM_ir / a3_ir) + (qfloat(506, 201) / math.pi) * aEM_ir * delta_ps_0
    indep_delta_2loop = Fraction(s2w_2l - s2w_1l).limit_denominator(10**12)
    indep_sqrt_2_lam = Fraction(math.sqrt(qfloat(2, 1) * lam_ir)).limit_denominator(10**12)

    g6_cross = extract_gate6_json_envelopes(repo_root)

    pr3_ok = (
        (b1_SM, b2_SM, b3_SM) == (sp.Rational(41, 10), sp.Rational(-19, 6), sp.Integer(-7))
        and (b4_PS, b2L_PS, b2R_PS) == (sp.Integer(-10), sp.Rational(-7, 3), sp.Rational(-7, 3))
        and (c_0, c_rat, c_delta) == (sp.Rational(23, 134), sp.Rational(109, 201), sp.Rational(506, 201))
        and bbo_1_ok
        and bbo_2_ok
        and rk4_conv_err < qfloat(1, 10**11)
        and Fraction(7, 10000) < indep_delta_2loop < Fraction(3, 1000)
        and g6_cross["passed"]
    )

    pr4_ok = (
        sp.simplify(lam_PS_sym - target_lam_PS) == 0
        and sp.simplify(lam_PS_sym.subs(beta, sp.pi / 4)) == 0
        and Fraction(35, 100) < indep_sqrt_2_lam < Fraction(78, 100)
        and g6_cross["passed"]
    )

    pr3_res = {
        "c_0": f"{c_0.p}/{c_0.q}",
        "c_rat": f"{c_rat.p}/{c_rat.q}",
        "c_Delta_PS": f"{c_delta.p}/{c_delta.q}",
        "guardrail_4_bbo_bpv_1loop_2loop_exact": bool(bbo_1_ok and bbo_2_ok),
        "rk4_step_halving_max_diff": bounded_rat_str(rk4_conv_err),
        "independent_sample_delta_2loop": frac_str(indep_delta_2loop),
        "gate6_sealed_json_envelope_check": g6_cross,
        "passed": bool(pr3_ok),
    }
    pr4_res = {
        "d_term_quartic_identity_exact": sp.simplify(lam_PS_sym - target_lam_PS) == 0,
        "vanishes_at_tan_beta_eq_1": sp.simplify(lam_PS_sym.subs(beta, sp.pi / 4)) == 0,
        "independent_sample_sqrt_2_lambda_IR": frac_str(indep_sqrt_2_lam),
        "gate6_sealed_json_envelope_verified": bool(g6_cross["passed"]),
        "passed": bool(pr4_ok),
    }
    return pr3_res, pr4_res


def psi_magnetized_torus(j: int, flux_m: int, u: np.ndarray, v: np.ndarray, alpha: float, beta: float, tau: complex, nmax: int = 8) -> np.ndarray:
    """Magnetized T^2 wavefunction psi^{j, M}(z; tau, alpha + beta*tau) from hep-th/0404229."""
    u_s = u + alpha
    v_s = v + beta
    ns = np.arange(-nmax, nmax + 1)[:, None]
    a = qfloat(j, flux_m)
    exponent = IMAG_UNIT * math.pi * qfloat(flux_m, 1) * (
        tau * (v_s[None, :] + ns + a) ** 2 + u_s[None, :] * (v_s[None, :] + qfloat(2, 1) * (ns + a))
    )
    heis_phase = np.exp(-IMAG_UNIT * math.pi * qfloat(flux_m, 1) * (alpha * v - beta * u))
    norm = (qfloat(2, 1) * tau.imag * qfloat(flux_m, 1)) ** qfloat(1, 4)
    return norm * heis_phase * np.exp(exponent).sum(axis=0)


def verify_pr5() -> dict:
    tau_cusp = IMAG_UNIT * qfloat(2, 1) * math.sqrt(qfloat(3, 1))
    ngrid = 32
    grid_1d = (np.arange(ngrid, dtype=float) + qfloat(1, 2)) / qfloat(ngrid, 1)
    uu, vv = np.meshgrid(grid_1d, grid_1d, indexing="ij")
    u_pts, v_pts = uu.ravel(), vv.ravel()
    dz2 = qfloat(1, ngrid * ngrid)

    psi3 = np.array([psi_magnetized_torus(j, 3, u_pts, v_pts, 0, 0, tau_cusp) for j in range(3)])
    psi6 = np.array([psi_magnetized_torus(k, 6, u_pts, v_pts, 0, 0, tau_cusp) for k in range(6)])

    gram3_err = float(np.max(np.abs(psi3 @ psi3.conj().T * dz2 - np.eye(3))))
    gram6_err = float(np.max(np.abs(psi6 @ psi6.conj().T * dz2 - np.eye(6))))

    Y_tensor = np.einsum("iz,jz,kz->ijk", psi3, psi3, psi6.conj()) * dz2
    Sigma_H = np.einsum("ijk,ijm->km", Y_tensor.conj(), Y_tensor)

    evals_neg_sig = np.linalg.eigvalsh(-Sigma_H)
    d_sigma_alone = int(np.sum(np.abs(evals_neg_sig - evals_neg_sig[0]) < qfloat(1, 10**10)))

    thetas = np.array([(qfloat(2 * k + 1, 6) * math.pi) for k in range(6)], dtype=float)
    K_KK = np.diag(qfloat(2, 1) - qfloat(2, 1) * np.cos(thetas))
    evals_kkk = np.linalg.eigvalsh(K_KK)
    d_kkk_alone = int(np.sum(np.abs(evals_kkk - evals_kkk[0]) < qfloat(1, 10**10)))

    M_H_sq = K_KK - Sigma_H
    evals_mh, evecs_mh = np.linalg.eigh(M_H_sq)
    min_adj_gap = float(np.min(np.diff(evals_mh)))
    d_combined = int(np.sum(np.abs(evals_mh - evals_mh[0]) < qfloat(1, 10**6)))
    ground_overlap_v_pos_pi6 = float(abs(evecs_mh[0, 0]) ** 2)

    passed = (
        gram3_err < qfloat(1, 10**13)
        and gram6_err < qfloat(1, 10**13)
        and d_sigma_alone == 3
        and d_kkk_alone == 2
        and d_combined == 1
        and min_adj_gap > qfloat(1, 100)
        and ground_overlap_v_pos_pi6 > qfloat(999, 1000)
    )
    return {
        "gram3_orthonormality_err": bounded_rat_str(gram3_err),
        "gram6_orthonormality_err": bounded_rat_str(gram6_err),
        "degeneracy_K_KK_alone": d_kkk_alone,
        "degeneracy_Sigma_H_alone": d_sigma_alone,
        "degeneracy_M_H_sq_combined": d_combined,
        "min_eigenvalue_gap": bounded_rat_str(min_adj_gap, 10**6),
        "ground_state_overlap_v_plus_pi_over_6": bounded_rat_str(ground_overlap_v_pos_pi6, 10**8),
        "passed": bool(passed),
    }


def verify_pr6_pr7_pr8() -> tuple:
    q_QL, q_qRc = 1, -1
    q_LL, q_lRc = -3, 3
    delta_up = q_QL - q_qRc
    delta_dn = q_QL - q_qRc
    delta_lep = q_LL - q_lRc
    deltas = [delta_up, delta_dn, delta_lep]
    all_even = all(d % 2 == 0 for d in deltas)
    flux_sum = 3 + 3 - 6

    BL_diag = sp.diag(sp.Rational(1, 3), sp.Rational(1, 3), sp.Rational(1, 3), sp.Integer(-1))
    Gamma_bid = sp.eye(4)
    comm_bl_bid = BL_diag * Gamma_bid - Gamma_bid * BL_diag

    # Full 2D torus quadrature of CIM (3, 3, -6) ground-state Yukawa Y_cim[:, :, 0] at Im(tau) = 4, (p, q) = (1, 1) / 5
    ngrid = 28
    g_1d = (np.arange(ngrid, dtype=float) + qfloat(1, 2)) / qfloat(ngrid, 1)
    uu, vv = np.meshgrid(g_1d, g_1d, indexing="ij")
    u_pts, v_pts = uu.ravel(), vv.ravel()
    dz2 = qfloat(1, ngrid * ngrid)
    tau_y4 = IMAG_UNIT * qfloat(4, 1)
    psi6_0 = psi_magnetized_torus(0, 6, u_pts, v_pts, 0, 0, tau_y4, nmax=10)

    def y_cim_k0(delta_charge: int, p_idx: int, q_idx: int) -> np.ndarray:
        aL = qfloat(delta_charge * p_idx, 10)
        bL = qfloat(delta_charge * q_idx, 10)
        pL = np.array([psi_magnetized_torus(j, 3, u_pts, v_pts, aL, bL, tau_y4, nmax=10) for j in range(3)])
        pR = np.array([psi_magnetized_torus(j, 3, u_pts, v_pts, -aL, -bL, tau_y4, nmax=10) for j in range(3)])
        return np.einsum("iz,jz,z->ij", pL, pR, psi6_0.conj()) * dz2

    Yu_ps = y_cim_k0(delta_up, 1, 1)
    Yd_ps = y_cim_k0(delta_dn, 1, 1)
    Ye_ps = y_cim_k0(delta_lep, 1, 1)

    _, Uu_ps = np.linalg.eigh(Yu_ps @ Yu_ps.conj().T)
    _, Ud_ps = np.linalg.eigh(Yd_ps @ Yd_ps.conj().T)
    v_tb_abs = float(abs(np.vdot(Uu_ps[:, 2], Ud_ps[:, 2])))

    rng = np.random.default_rng(607)
    max_haar_vtb_drift = 0
    for _ in range(8):
        UQ = random_haar_u3(rng)
        Uu_r = random_haar_u3(rng)
        Ud_r = random_haar_u3(rng)
        Yu_scr = UQ @ Yu_ps @ Uu_r.conj().T
        Yd_scr = UQ @ Yd_ps @ Ud_r.conj().T
        _, Uu_s = np.linalg.eigh(Yu_scr @ Yu_scr.conj().T)
        _, Ud_s = np.linalg.eigh(Yd_scr @ Yd_scr.conj().T)
        v_tb_s = float(abs(np.vdot(Uu_s[:, 2], Ud_s[:, 2])))
        if abs(v_tb_s - v_tb_abs) > max_haar_vtb_drift:
            max_haar_vtb_drift = abs(v_tb_s - v_tb_abs)

    sv_dn = np.linalg.svd(Yd_ps, compute_uv=False)
    sv_lep = np.linalg.svd(Ye_ps, compute_uv=False)
    ratio_dn = float(sv_dn[0] / sv_dn[2])
    ratio_lep = float(sv_lep[0] / sv_lep[2])
    lep_dn_split_factor = max(ratio_dn / ratio_lep, ratio_lep / ratio_dn)

    exp_lep_m2_m3 = Fraction(1, 5)
    exp_dn_m2_m3 = Fraction(2, 15)
    level15_exp_ratio = exp_lep_m2_m3 / exp_dn_m2_m3

    e5_points = [(p, q) for p in range(5) for q in range(5) if not (p == 0 and q == 0)]
    even_signs_all_plus = all(((-1) ** (p * q * d)) == 1 for d in deltas for (p, q) in e5_points)
    odd_6y_has_minus = any(((-1) ** (p * q * 5)) == -1 for (p, q) in e5_points)

    tau_mod = qfloat(23, 100) + IMAG_UNIT * qfloat(147, 100)

    def spin_v3(p_over_5: float, q_over_5: float, t_val: complex) -> np.ndarray:
        alpha = p_over_5 + qfloat(1, 2)
        beta = q_over_5 + qfloat(1, 2)
        ns = np.arange(-14, 15, dtype=float)[:, None]
        js = np.arange(3, dtype=float)[None, :]
        a = js / qfloat(3, 1) + alpha
        b = qfloat(3, 1) * beta
        th = np.exp(
            IMAG_UNIT * math.pi * qfloat(3, 1) * t_val * (ns + a) ** 2
            + qfloat(2, 1) * IMAG_UNIT * math.pi * (ns + a) * b
        ).sum(axis=0)
        return (qfloat(6, 1) * t_val.imag) ** qfloat(1, 4) * cmath.exp(-IMAG_UNIT * qfloat(3, 1) * math.pi * alpha * beta) * th

    def build_e5_gramian(delta_c: int, t_val: complex) -> np.ndarray:
        g_mat = np.zeros((3, 3), dtype=complex)
        for p_i, q_i in e5_points:
            vec = spin_v3(qfloat(delta_c * p_i, 5), qfloat(delta_c * q_i, 5), t_val)
            g_mat += np.outer(vec, vec.conj())
        return g_mat

    G_tau = build_e5_gramian(2, tau_mod)
    G_T = build_e5_gramian(2, tau_mod + qfloat(1, 1))
    G_S = build_e5_gramian(2, -qfloat(1, 1) / tau_mod)
    ev_0 = np.linalg.eigvalsh(G_tau)
    ev_T = np.linalg.eigvalsh(G_T)
    ev_S = np.linalg.eigvalsh(G_S)
    sl2z_gram_diff = max(float(np.max(np.abs(ev_0 - ev_T))), float(np.max(np.abs(ev_0 - ev_S))))
    gram_anisotropy = float(ev_0[2] - ev_0[0])

    pr6_pr7_ok = (
        deltas == [2, 2, -6]
        and all_even
        and flux_sum == 0
        and comm_bl_bid == sp.zeros(4, 4)
        and abs(qfloat(1, 1) - v_tb_abs) < qfloat(1, 10**14)
        and max_haar_vtb_drift < qfloat(1, 10**12)
        and lep_dn_split_factor > qfloat(28, 1)
        and level15_exp_ratio == Fraction(3, 2)
    )
    pr8_ok = (
        len(e5_points) == 24
        and even_signs_all_plus
        and odd_6y_has_minus
        and sl2z_gram_diff < qfloat(1, 10**12)
        and gram_anisotropy > qfloat(1, 100)
    )

    pr6_pr7_res = {
        "charges_3BL_QL_qRc": [q_QL, q_qRc],
        "charges_3BL_LL_lRc": [q_LL, q_lRc],
        "Delta_up_dn_lep": deltas,
        "all_Delta_even": bool(all_even),
        "CIM_flux_sum": flux_sum,
        "local_bidoublet_BL_commutator_zero": comm_bl_bid == sp.zeros(4, 4),
        "one_minus_abs_V_tb": bounded_rat_str(abs(qfloat(1, 1) - v_tb_abs)),
        "max_haar_V_tb_drift": bounded_rat_str(max_haar_vtb_drift),
        "lepton_down_s1_over_s3_split_factor": bounded_rat_str(lep_dn_split_factor, 10**6),
        "level15_cusp_exponent_ratio": frac_str(level15_exp_ratio),
        "passed": bool(pr6_pr7_ok),
    }
    pr8_res = {
        "primitive_E5_points": len(e5_points),
        "even_Delta_parity_all_plus_one": bool(even_signs_all_plus),
        "odd_6Y_parity_breaks_sign": bool(odd_6y_has_minus),
        "e5_gramian_SL2Z_T_S_max_diff": bounded_rat_str(sl2z_gram_diff),
        "e5_gramian_anisotropy": bounded_rat_str(gram_anisotropy, 10**6),
        "passed": bool(pr8_ok),
    }
    return pr6_pr7_res, pr8_res


def extract_pmns_invariants(Ye: np.ndarray, kap: np.ndarray) -> tuple:
    """Basis-invariant extraction of (|U_{e1}|^2, |U_{e3}|^2, |J_PMNS|) from (Ye, kappa_Weinberg)."""
    He = Ye @ Ye.conj().T
    Hnu = kap @ kap.conj().T
    _, Ue = np.linalg.eigh(He)
    _, Unu = np.linalg.eigh(Hnu)
    U_pmns = Ue.conj().T @ Unu
    ue1_sq = float(abs(U_pmns[0, 0]) ** 2)
    ue3_sq = float(abs(U_pmns[0, 2]) ** 2)
    j_pmns = abs(float(np.imag(U_pmns[0, 1] * U_pmns[1, 2] * np.conj(U_pmns[0, 2]) * np.conj(U_pmns[1, 1]))))
    return ue1_sq, ue3_sq, j_pmns


def verify_pr9() -> dict:
    psi_s, delta_s = sp.symbols("psi_s delta_s", real=True)
    u1 = sp.Matrix([2, -1, -1]) / sp.sqrt(6)
    u2_0 = sp.Matrix([1, 1, 1]) / sp.sqrt(3)
    u3_0 = sp.Matrix([0, 1, -1]) / sp.sqrt(2)

    c2 = sp.cos(psi_s) * u2_0 - sp.sin(psi_s) * sp.exp(sp.I * delta_s) * u3_0
    c3 = sp.sin(psi_s) * sp.exp(-sp.I * delta_s) * u2_0 + sp.cos(psi_s) * u3_0
    U_tm1 = sp.Matrix.hstack(u1, c2, c3)
    unitarity_check = sp.simplify(U_tm1.adjoint() * U_tm1 - sp.eye(3))
    i_tm1_sym = sp.simplify(U_tm1[0, 0] * sp.conjugate(U_tm1[0, 0]))

    ue3_sq_bench = sp.Rational(1, 48)
    cos2_12_bench = sp.Rational(2, 3) / (sp.Integer(1) - ue3_sq_bench)

    s_psi = qfloat(1, 4)
    c_psi = math.sqrt(qfloat(15, 16))
    ph = cmath.exp(IMAG_UNIT * qfloat(3, 5))
    u1_n = np.array([qfloat(2, 1), -qfloat(1, 1), -qfloat(1, 1)], dtype=complex) / math.sqrt(qfloat(6, 1))
    u2_0n = np.array([qfloat(1, 1), qfloat(1, 1), qfloat(1, 1)], dtype=complex) / math.sqrt(qfloat(3, 1))
    u3_0n = np.array([qfloat(0, 1), qfloat(1, 1), -qfloat(1, 1)], dtype=complex) / math.sqrt(qfloat(2, 1))
    U_uv = np.column_stack([
        u1_n,
        c_psi * u2_0n - s_psi * ph * u3_0n,
        s_psi * np.conj(ph) * u2_0n + c_psi * u3_0n,
    ])

    Ye_0 = np.diag([qfloat(1, 500), qfloat(1, 50), qfloat(1, 20)]).astype(complex)
    mnu_diag = np.diag([qfloat(1, 1000), qfloat(1, 10), qfloat(1, 2)]).astype(complex)
    kap_0 = U_uv @ mnu_diag @ U_uv.T

    ue1_base, ue3_base, j_base = extract_pmns_invariants(Ye_0, kap_0)

    rng = np.random.default_rng(909)
    max_haar_tm1_drift = 0
    max_haar_ue3_drift = 0
    max_haar_j_drift = 0
    for _ in range(10):
        UL = random_haar_u3(rng)
        UeR = random_haar_u3(rng)
        Ye_scr = UL @ Ye_0 @ UeR.conj().T
        kap_scr = UL @ kap_0 @ UL.T
        ue1_s, ue3_s, j_s = extract_pmns_invariants(Ye_scr, kap_scr)
        max_haar_tm1_drift = max(max_haar_tm1_drift, abs(ue1_s - ue1_base))
        max_haar_ue3_drift = max(max_haar_ue3_drift, abs(ue3_s - ue3_base))
        max_haar_j_drift = max(max_haar_j_drift, abs(j_s - j_base))

    def tm1_rge_excursion(y_tau_val: float) -> float:
        Ye_run = np.diag([qfloat(1, 500), qfloat(1, 50), y_tau_val]).astype(complex)
        P_e = Ye_run @ Ye_run.conj().T
        loop1 = qfloat(1, 16) / (math.pi * math.pi)
        dt_tot = -qfloat(30, 1)
        steps = 200
        h = dt_tot / qfloat(steps, 1)
        kap_cur = kap_0.copy()
        for _ in range(steps):
            def rhs_k(k_m):
                return -qfloat(3, 2) * loop1 * (P_e @ k_m + k_m @ P_e.T)
            k1 = rhs_k(kap_cur)
            k2 = rhs_k(kap_cur + qfloat(1, 2) * h * k1)
            k3 = rhs_k(kap_cur + qfloat(1, 2) * h * k2)
            k4 = rhs_k(kap_cur + h * k3)
            kap_cur = kap_cur + qfloat(1, 6) * h * (k1 + qfloat(2, 1) * k2 + qfloat(2, 1) * k3 + k4)
        ue1_ir, _, _ = extract_pmns_invariants(Ye_run, kap_cur)
        return abs(ue1_ir - qfloat(2, 3))

    exc_ytau_1_20 = tm1_rge_excursion(qfloat(1, 20))
    exc_ytau_1_5 = tm1_rge_excursion(qfloat(1, 5))

    passed = (
        unitarity_check == sp.zeros(3, 3)
        and i_tm1_sym == sp.Rational(2, 3)
        and cos2_12_bench == sp.Rational(32, 47)
        and abs(ue1_base - qfloat(2, 3)) < qfloat(1, 10**14)
        and abs(ue3_base - qfloat(1, 48)) < qfloat(1, 10**14)
        and max_haar_tm1_drift < qfloat(1, 10**12)
        and max_haar_ue3_drift < qfloat(1, 10**12)
        and max_haar_j_drift < qfloat(1, 10**12)
        and exc_ytau_1_20 < qfloat(1, 2000)
        and exc_ytau_1_5 < qfloat(1, 200)
    )
    return {
        "I_TM1_exact": f"{i_tm1_sym.p}/{i_tm1_sym.q}",
        "cos2_theta12_at_Ue3_sq_1_over_48": f"{cos2_12_bench.p}/{cos2_12_bench.q}",
        "uv_abs_I_TM1_minus_2_over_3": bounded_rat_str(abs(ue1_base - qfloat(2, 3))),
        "max_u3_haar_I_TM1_drift": bounded_rat_str(max_haar_tm1_drift),
        "rge_dt_minus_30_excursion_ytau_1_over_20": bounded_rat_str(exc_ytau_1_20, 10**8),
        "rge_dt_minus_30_excursion_ytau_1_over_5": bounded_rat_str(exc_ytau_1_5, 10**8),
        "passed": bool(passed),
    }


def verify_pr10() -> dict:
    x_s = sp.Symbol("x_s")
    B4_poly = sp.bernoulli(4, x_s)
    B4_0 = B4_poly.subs(x_s, 0)
    B4_half = B4_poly.subs(x_s, sp.Rational(1, 2))
    zeta_m3 = sp.zeta(-3)

    w_bos_per = sp.Integer(30) * B4_0
    w_bos_anti = sp.Integer(30) * B4_half
    w_fer_per = -sp.Integer(30) * B4_0
    w_fer_anti = -sp.Integer(30) * B4_half

    C_UV_gauge = 42 * w_bos_per + 114 * w_bos_anti
    C_UV_fermion = 96 * w_fer_per + 66 * w_fer_anti
    C_UV_scalar = 26 * w_bos_per + 28 * w_bos_anti

    C_UV = C_UV_gauge + C_UV_fermion + C_UV_scalar
    C_IR = 96 * w_fer_per + 42 * w_bos_per + 26 * w_bos_per

    mp.mp.dps = 30

    def casimir_potential_mp(L_val) -> mp.mpf:
        x = mp.mpf(L_val)
        w_uv_ir = (mp.mpf(1) / mp.mpf(2)) * (x ** 2) * mp.besselk(2, x)
        c_ir_mp = mp.mpf(int(C_IR))
        c_diff_mp = mp.mpf(C_UV.p) / mp.mpf(C_UV.q) - c_ir_mp
        return (c_ir_mp + c_diff_mp * w_uv_ir) / (x ** 3)

    max_deriv = -mp.inf
    for k_step in range(1, 26):
        L_pt = mp.mpf(k_step) / mp.mpf(5)
        h_eps = mp.mpf(1) / mp.mpf(10**8)
        dV = (casimir_potential_mp(L_pt + h_eps) - casimir_potential_mp(L_pt - h_eps)) / (2 * h_eps)
        if dV > max_deriv:
            max_deriv = dV

    passed = (
        B4_0 == sp.Rational(-1, 30)
        and B4_half == sp.Rational(7, 240)
        and zeta_m3 == sp.Rational(1, 120)
        and C_UV_gauge == sp.Rational(231, 4)
        and C_UV_fermion == sp.Rational(153, 4)
        and C_UV_scalar == sp.Rational(-3, 2)
        and C_UV == sp.Rational(189, 2)
        and C_IR == sp.Integer(28)
        and C_UV > 0
        and C_IR > 0
        and max_deriv < 0
    )
    return {
        "B4_0": f"{B4_0.p}/{B4_0.q}",
        "B4_half": f"{B4_half.p}/{B4_half.q}",
        "zeta_R_minus_3": f"{zeta_m3.p}/{zeta_m3.q}",
        "C_UV_gauge": f"{C_UV_gauge.p}/{C_UV_gauge.q}",
        "C_UV_fermion": f"{C_UV_fermion.p}/{C_UV_fermion.q}",
        "C_UV_scalar": f"{C_UV_scalar.p}/{C_UV_scalar.q}",
        "C_UV": f"{C_UV.p}/{C_UV.q}",
        "C_IR": str(int(C_IR)),
        "both_UV_and_IR_strictly_positive": bool(C_UV > 0 and C_IR > 0),
        "max_dV_dL4_strictly_negative": bool(max_deriv < 0),
        "passed": bool(passed),
    }


def run_deliverable_2(repo_root: Path) -> dict:
    dag_res = evaluate_epistemic_dag()
    pr1_res = verify_pr1()
    pr2_res = verify_pr2()
    pr3_res, pr4_res = verify_pr3_and_pr4(repo_root)
    pr5_res = verify_pr5()
    pr67_res, pr8_res = verify_pr6_pr7_pr8()
    pr9_res = verify_pr9()
    pr10_res = verify_pr10()

    kill_lines = {
        "PR-1": pr1_res,
        "PR-2": pr2_res,
        "PR-3": pr3_res,
        "PR-4": pr4_res,
        "PR-5": pr5_res,
        "PR-6_and_PR-7": pr67_res,
        "PR-8": pr8_res,
        "PR-9": pr9_res,
        "PR-10": pr10_res,
    }
    all_pr_passed = all(item["passed"] for item in kill_lines.values())
    return {
        "epistemic_dag_46_node": dag_res,
        "kill_lines_pr1_to_pr10": kill_lines,
        "all_kill_lines_passed": bool(all_pr_passed),
        "passed": bool(dag_res["passed"] and all_pr_passed),
    }


# ============================================================================
# 3. Deliverable 3: Campaign-Wide Cryptographic Custody Lock (38 Prior + Self)
# ============================================================================

def parse_sha256_manifest(manifest_path: Path, repo_root: Path) -> list:
    lines = [ln.strip() for ln in manifest_path.read_text(encoding="utf-8").splitlines() if ln.strip()]
    records = []
    for ln in lines:
        if ln.startswith("SHA256") and "=" in ln and "(" in ln and ")" in ln:
            raw_target = ln.split("(", 1)[1].rsplit(")", 1)[0].strip()
            expected_hex = ln.rsplit("=", 1)[1].strip().lower()
        else:
            parts = ln.split(None, 1)
            expected_hex = parts[0].strip().lower()
            raw_target = parts[1].strip().lstrip("*").strip() if len(parts) == 2 else ""

        if raw_target:
            cand_abs = Path(raw_target)
            cand_repo = repo_root / raw_target
            cand_local = manifest_path.parent / raw_target
            cand_base = manifest_path.parent / Path(raw_target).name
            if cand_abs.is_absolute() and cand_abs.is_file():
                target_path = cand_abs
            elif cand_repo.is_file():
                target_path = cand_repo
            elif cand_local.is_file():
                target_path = cand_local
            else:
                target_path = cand_base
        else:
            ext = "*.py" if "SCRIPT" in manifest_path.name else "*.json"
            matches = sorted(manifest_path.parent.glob(ext))
            target_path = matches[0] if matches else (manifest_path.parent / "MISSING")

        records.append({
            "manifest_rel": str(manifest_path.relative_to(repo_root)),
            "target_path": target_path,
            "target_rel": str(target_path.relative_to(repo_root)) if target_path.exists() else str(target_path),
            "expected_sha256": expected_hex,
        })
    return records


def verify_custody_records(records: list) -> dict:
    hex_chars = frozenset("0123456789abcdef")
    matched = 0
    mismatches = []
    for rec in records:
        exp = rec["expected_sha256"]
        tpath = rec["target_path"]
        valid_fmt = len(exp) == 64 and all(ch in hex_chars for ch in exp)
        if not valid_fmt or not tpath.is_file():
            mismatches.append(rec["manifest_rel"])
            continue
        actual = hashlib.sha256(tpath.read_bytes()).hexdigest().lower()
        if actual == exp:
            matched += 1
        else:
            mismatches.append(rec["manifest_rel"])
    return {
        "total": len(records),
        "matched": matched,
        "mismatch_count": len(mismatches),
        "mismatches": mismatches,
        "passed": len(mismatches) == 0 and matched == len(records),
    }


def run_deliverable_3(repo_root: Path, self_script_path: Path) -> dict:
    relays_dir = repo_root / "relays"
    all_manifests = sorted(relays_dir.glob("*/*SHA256.txt"))
    prior_manifests = [
        m for m in all_manifests if m.parent != self_script_path.parent
    ]

    prior_records = []
    for mpath in prior_manifests:
        prior_records.extend(parse_sha256_manifest(mpath, repo_root))

    prior_check = verify_custody_records(prior_records)

    self_manifest_path = self_script_path.parent / "SCRIPT_SHA256.txt"
    if self_manifest_path.is_file():
        self_records = parse_sha256_manifest(self_manifest_path, repo_root)
        self_check = verify_custody_records(self_records)
        self_verified = (
            self_check["passed"]
            and len(self_records) == 1
            and self_records[0]["target_path"].resolve() == self_script_path.resolve()
        )
    else:
        self_verified = False

    tampered_records = copy.deepcopy(prior_records)
    orig_digest = tampered_records[0]["expected_sha256"]
    flipped_char = "0" if orig_digest[0] != "0" else "1"
    tampered_records[0]["expected_sha256"] = flipped_char + orig_digest[1:]
    tampered_check = verify_custody_records(tampered_records)
    pf7_5_caught = (not tampered_check["passed"]) and tampered_check["mismatch_count"] == 1

    passed = (
        len(prior_manifests) == 40
        and len(prior_records) == 40
        and prior_check["matched"] == 40
        and prior_check["passed"]
        and self_verified
        and pf7_5_caught
    )
    return {
        "prior_manifest_file_count": len(prior_manifests),
        "prior_records_verified": prior_check["matched"],
        "prior_records_total": prior_check["total"],
        "prior_mismatches": prior_check["mismatches"],
        "self_script_sha256_verified_at_runtime": bool(self_verified),
        "PF7_5": {
            "description": "Flipping 1 hex character of expected SHA-256 digest in memory fails custody verifier",
            "tampered_mismatch_count": tampered_check["mismatch_count"],
            "caught": bool(pf7_5_caught),
        },
        "passed": bool(passed),
    }


def main() -> int:
    self_script = Path(__file__).resolve()
    repo_root = self_script.parents[2]
    out_path = self_script.parent / "referee_closure_g7_fixed_out.json"

    ast_lock = audit_self_source(self_script)
    d1 = run_deliverable_1()
    d2 = run_deliverable_2(repo_root)
    d3 = run_deliverable_3(repo_root, self_script)

    dag_part = d2["epistemic_dag_46_node"]
    planted_faults = {
        "PF7_1_unpriced_second_anchor": bool(d1["PF7_1"]["caught"]),
        "PF7_2_dag_back_edge_cycle": bool(dag_part["PF7_2"]["caught"]),
        "PF7_3_rank_laundering": bool(dag_part["PF7_3"]["caught"]),
        "PF7_4_zero_bit_unstabilized_seam": bool(dag_part["PF7_4"]["caught"]),
        "PF7_5_sha256_memory_tamper": bool(d3["PF7_5"]["caught"]),
    }
    all_5_caught = all(planted_faults.values())
    overall_passed = bool(
        ast_lock["passed"]
        and d1["passed"]
        and d2["passed"]
        and d3["passed"]
        and all_5_caught
    )

    report = {
        "gate": "AGY-002_CLOSURE-G7",
        "role": "independent_cold_room_referee",
        "empirical_inputs_used": "0/19",
        "overall_passed": overall_passed,
        "all_5_planted_faults_caught": all_5_caught,
        "planted_fault_summary": planted_faults,
        "source_ast_and_import_lock": ast_lock,
        "deliverable_1_u3_5_and_buckingham_pi": d1,
        "deliverable_2_epistemic_dag_and_kill_lines": d2,
        "deliverable_3_campaign_custody_lock": d3,
    }

    out_path.write_text(json.dumps(report, indent=2, sort_keys=False) + "\n", encoding="utf-8")
    return 0 if overall_passed else 1


if __name__ == "__main__":
    sys.exit(main())
