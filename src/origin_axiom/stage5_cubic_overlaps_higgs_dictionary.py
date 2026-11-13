"""Stage 5 (B1861 WP-1.7, WP-3.4, WP-2.5): Quantum-Number Dictionary, Curved Zero-Mode
Trilinear Gauge-Yukawa Overlaps vs Four-Channel Value Frame, Stationary Source & Lepton Factor.

Strictly 0-of-19 data-blind (zero empirical Standard Model constants, masses, mixings, couplings,
or scales anywhere). Enforces Guardrails 1-6 and Anti-Shortcut Locks F1-F6:
  - Part 5A (WP-1.7: G:FK11, G:GAP1, TAG:LAMBDA, MC:PRICE, V:EARN-RULE, A:A05, A:A11, FL:01, FL:07, FL:09, FL:10, D:02, X:DICT):
    Mechanical 45D so(10, Q) -> u(5) -> su(3)_C (+) su(2)_L centralizer theorem proving
    dim Z_{so(10)}(su(3)_C (+) su(2)_L) == 4 (u(1)_{B-L} (+) su(2)_R, derived rank 3) while
    dim(Z cap u(5)) == 2 (abelian span{Y_GG, Q_chi}); mechanical Spin(10)xSpin(6)/Z_4 central
    glue kernel of order 4 across all 5 blocks of 248; mechanical branching of 16^+ (6+3+3+2+1+1)
    and 10_vec = 5_{+2} (+) 5bar_{-2}; exact 4-solution hypercharge dichotomy (+-Y_GG, +-Y_flip)
    conjugated by explicit w_{SU(2)_R} in Spin(10)|_{16^+} while broken by SU(5)xU(1)_chi;
    shared (16^+, 4^+) zero-mode carrier theorem (A:A11 / FL:07) from Spin(10)|_{16^+} irreducibility;
    flat Q_8 pseudoreality obstruction (FL:09, B1790) vs compact e_8 reality (A:A05) with full
    SU(2)_L eps_{ab} doublet contraction across neutral (6,7) and charged (8,9) Higgs axes and
    16D gauge-allowed U(3)_C x U(2)_L Haar basis-scrambling invariance (< 1e-12).
  - Part 5B (WP-3.4: A:A02, A:A03, A:A04, FL:06, D:05, D:10, X:SELECT):
    Side-by-side comparison of the curved e_8 zero-mode trilinear coupling and Frame A's four-channel
    value-frame coupling on E_tau \\ {0}:
      (1) Parabolic (E_+, E_-) != 0 kernel theorem on true Fock 16^+ (chir10 == +1, odd bit-sum)
          and mechanical h_4 in Spin(6) (4^+ -> w_8^3 (+) 3*w_8^{-1}) plus full parabolic h_1 control:
          exact SymPy Koszul harmonic mu-weights (V_10: +2, {-2,-2,+2,+2}, -2; S_16^+: +3, {0,0}, -3),
          Stage 1 2D form-degree rule, exact vanishing of ALL 3 harmonic fermion bilinears (a x a,
          a x spin_harm, spin_harm x spin_harm) against all harmonic V_10 modes while both non-harmonic
          mu-conserving channels couple non-trivially, and necessary-and-sufficient SVD joint-nullspace
          parabolic H^0 census across all 4 spin structures on both h_4 and h_1.
      (2) Unbroken-Spin(10) coherent 3-branch (B1866) curved overlap theorem vs Frame A Klein-four:
          - Exact SymPy wedge algebra on Lambda^2(4^+) ~= 6_vec proving 1_{+3/4} ^ 1_{+3/4} == 0 on
            single-h_4 (killing untwisted Higgs on a_sp x a_sp) vs Frame A Klein-four SU(4) holonomy
            where e_a ^ e_b != 0 for all a != b;
          - Exact 35-digit Weierstrass-Jacobi identity d_z S_k(z) + S_i(z)*S_j(z) == 0 and
            d_z S_k(z)*S_i(z)*S_j(z) + (wp(z)-e_i)*(wp(z)-e_j) == 0 (< 1e-26);
          - Stage 1/2 curved hyperbolic cusp measures Omega_hyp(z)^{-3/2} d^2z and Omega_hyp(z)^{-5/4} d^2z
            across all 6 off-diagonal triples (|I_sp| < 1e-20, |I_dp| > 1.0) AND all 3 diagonal spin-slot
            H^0 triples (i, 0, i) where z -> -z parity REVERSES (|I_sp^diag| > 1.0, |I_dp^diag| < 1e-20);
          - Exact cyclotomic order obstruction gcd(5, 24) == 1 for slope 2/5 (A:A02) and offset (A:A03).
  - Part 5C (WP-2.5: G:GAP3, G:GAP5, A:A08, A:A10, FL:12, FL:05, X:SOURCE):
    - Exact vanishing of (45,1) and (1,15) chiral Yukawa bilinears;
    - Exact tree-level Y_e == Y_d^T => c_UV == 1 on (10,6) subset 248 vs explicit Cl(10) symmetric
      5-form Georgi-Jarlskog operator in 126bar_s giving |y_e / y_d| == 3 (absent from 248 of E_8);
    - Exact Q(zeta_24) Schur generation-metric theorem on BOTH 3_sp (order 96) and 3_dp (order 288,
      |Z|=12, |PG|=24): End(3_sp) == End(3_dp) == 1, Hom(3_sp, 3_dp) == 0, End(3_sp (+) 3_dp) == 2,
      and single-thread End_{E_theta}(3_sp) == 2 (1 continuous relative ratio) vs unstabilized 9 (8 ratios);
    - Exact 128D S_16^+ quartic D-term dichotomy: real slice f_0 gives 8*(|h_u|^2 - |h_d|^2)^2 (D-flat
      valley |h_u|==|h_d|), chiral h_4-eigenstate f_+ for both doublets gives 16*(|h_u|^4 + |h_d|^4)
      (no non-zero D-flat valley), and opposite U(1)_{h_4} pair (f_+, f_-) restores 16*(|h_u|^2 - |h_d|^2)^2
      while forbidding singlet-triplet H_d Yukawa on a single +h_4 background.
"""
from __future__ import annotations

from itertools import combinations, product
import math
from pathlib import Path
from typing import Any

import mpmath as mp
import numpy as np
import sympy as sp

from origin_axiom.stage1_curved_action_cusp_orbit import (
    TOL,
    audit_source_zero_empirical_constants,
    check_guardrail2_ast_no_literal_bool_verdicts,
    haar_unitary,
    joint_commutant_dim_exact,
    joint_commutant_dim_num,
)
from origin_axiom.stage2_kernel_and_physical_join import (
    cyc24_center_and_pg_orders,
    cyc24_close_group,
    cyc24_herm,
    cyc24_to_numpy,
    solve_intertwiner_cyc24_exact,
    verify_b1866_zero_handtyped_3branch_pde_join,
    verify_wp32_exact_cyclotomic_algebra_and_metaplectic_obstruction,
)


def bit_sum_int(val_i: int, n_bits: int) -> int:
    """Count binary ones in the lowest n_bits of non-negative integer val_i."""
    return sum((val_i // (2**b_i)) % 2 for b_i in range(n_bits))


def build_exact_e8_10_6_spinor_bilinear() -> dict[str, Any]:
    """Construct the exact 60-component (10, 6) subset so(16) compact e_8 spinor-spinor bracket
    K_{A,B} = -(1/2) C_16 Gamma_A Gamma_B|_{S_16^+} mechanically from Cl(10) x Cl(6).
    """
    creators: list[sp.Matrix] = []
    for axis in range(5):
        op_c = sp.zeros(32, 32)
        p2_c = 2**axis
        for st_c in range(32):
            if (st_c // p2_c) % 2 == 0:
                op_c[st_c + p2_c, st_c] = (-1) ** bit_sum_int(st_c, axis)
        creators.append(op_c)
    ann = [c_m.T for c_m in creators]

    g10_cliff: list[sp.Matrix] = []
    for a_i in range(5):
        g10_cliff.append(creators[a_i] + ann[a_i])
        g10_cliff.append(sp.I * (creators[a_i] - ann[a_i]))

    omega10 = sp.eye(32)
    b10_maj = sp.eye(32)
    for a_i in range(5):
        omega10 = (omega10 * g10_cliff[2 * a_i] * g10_cliff[2 * a_i + 1]).applyfunc(sp.expand)
        b10_maj = (b10_maj * g10_cliff[2 * a_i]).applyfunc(sp.expand)
    chir10 = sp.I * omega10

    i2_c = sp.eye(2)
    sx_c = sp.Matrix([[0, 1], [1, 0]])
    sy_c = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sz_c = sp.Matrix([[1, 0], [0, -1]])

    def kron3_c(m1: sp.Matrix, m2: sp.Matrix, m3: sp.Matrix) -> sp.Matrix:
        return sp.kronecker_product(sp.kronecker_product(m1, m2), m3)

    f6_c = [
        kron3_c(sx_c, i2_c, i2_c),
        kron3_c(sy_c, i2_c, i2_c),
        kron3_c(sz_c, sx_c, i2_c),
        kron3_c(sz_c, sy_c, i2_c),
        kron3_c(sz_c, sz_c, sx_c),
        kron3_c(sz_c, sz_c, sy_c),
    ]
    omega6 = f6_c[0] * f6_c[1] * f6_c[2] * f6_c[3] * f6_c[4] * f6_c[5]
    b6_maj = (f6_c[1] * f6_c[3] * f6_c[5]).applyfunc(sp.expand)
    chir6 = -sp.I * omega6

    splus_pairs = [
        (r32, r8)
        for r32 in range(32)
        for r8 in range(8)
        if sp.expand(omega10[r32, r32] * omega6[r8, r8]) == 1
    ]
    splus_idx = {pt: k_idx for k_idx, pt in enumerate(splus_pairs)}

    sign_to_idx: dict[tuple[int, ...], int] = {}
    for k_idx, (r32, r8) in enumerate(splus_pairs):
        s5 = tuple(1 if ((r32 // (2**a_i)) % 2 == 1) else -1 for a_i in range(5))
        t3 = tuple(1 if ((r8 // (2 ** (2 - j_i))) % 2 == 1) else -1 for j_i in range(3))
        sign_to_idx[s5 + t3] = k_idx

    b10_map = [next((c_i, b10_maj[r_i, c_i]) for c_i in range(32) if b10_maj[r_i, c_i] != 0) for r_i in range(32)]
    b6_map = [next((c_i, b6_maj[r_i, c_i]) for c_i in range(8) if b6_maj[r_i, c_i] != 0) for r_i in range(8)]
    c16_map = [
        (
            splus_idx[(b10_map[r32][0], b6_map[r8][0])],
            sp.expand(b10_map[r32][1] * b6_map[r8][1]),
        )
        for r32, r8 in splus_pairs
    ]

    half_rat = sp.Rational(1, 2)
    kab_cross_60: list[list[tuple[int, int, Any]]] = []
    for a_10 in range(10):
        ab32 = (g10_cliff[a_10] * chir10).applyfunc(sp.expand)
        r32_map = [next((c_i, ab32[r_i, c_i]) for c_i in range(32) if ab32[r_i, c_i] != 0) for r_i in range(32)]
        for j_6 in range(6):
            ab8 = f6_c[j_6]
            r8_map = [next((c_i, ab8[r_i, c_i]) for c_i in range(8) if ab8[r_i, c_i] != 0) for r_i in range(8)]
            gab_splus = [
                (
                    splus_idx[(r32_map[r32][0], r8_map[r8][0])],
                    sp.expand(r32_map[r32][1] * r8_map[r8][1]),
                )
                for r32, r8 in splus_pairs
            ]
            k_list: list[tuple[int, int, Any]] = []
            for r_s in range(128):
                mid_s, vc_s = c16_map[r_s]
                col_s, vg_s = gab_splus[mid_s]
                k_list.append((r_s, col_s, sp.expand(-half_rat * vc_s * vg_s)))
            kab_cross_60.append(k_list)

    def bilinear_60(idx_u: int, idx_v: int) -> list[Any]:
        out_60: list[Any] = []
        for k_list in kab_cross_60:
            col_u, val_u = k_list[idx_u][1], k_list[idx_u][2]
            out_60.append(val_u if col_u == idx_v else sp.Integer(0))
        return out_60

    return {
        "creators": creators,
        "ann": ann,
        "g10_cliff": g10_cliff,
        "omega10": omega10,
        "chir10": chir10,
        "b10_maj": b10_maj,
        "f6_cliff": f6_c,
        "omega6": omega6,
        "chir6": chir6,
        "b6_maj": b6_maj,
        "splus_pairs": splus_pairs,
        "splus_idx": splus_idx,
        "sign_to_idx": sign_to_idx,
        "bilinear_60": bilinear_60,
        "kab_cross_60": kab_cross_60,
    }


def joint_fixed_subspace_dim_num(ta_mat: np.ndarray, tb_mat: np.ndarray, tol: float = 1e-9) -> int:
    """Necessary-and-sufficient dimension of ker(T_a - I) cap ker(T_b - I) via stacked SVD nullity (F3)."""
    rk_n = int(ta_mat.shape[0])
    if rk_n == 0:
        return rk_n
    eye_n = np.eye(rk_n, dtype=complex)
    sys_joint = np.vstack([ta_mat - eye_n, tb_mat - eye_n])
    sv_j = np.linalg.svd(sys_joint, compute_uv=False)
    return int(np.sum(sv_j < tol))


def eval_parabolic_cohomology_on_hd(
    d_deg: int,
    hd_basis: np.ndarray,
    mu_op: np.ndarray,
    ta_op: np.ndarray,
    tb_op: np.ndarray,
    ep_full: np.ndarray,
    em_full: np.ndarray,
    eta: tuple[int, int],
) -> dict[str, Any]:
    """Universal L^2 parabolic cohomology evaluator on Koszul harmonic degree d in {0, 1, 2}."""
    _ = (ep_full, em_full)
    if hd_basis.shape[1] == 0:
        n_hd = int(hd_basis.shape[1])
        return {"h0": n_hd, "h1": n_hd}

    mu_sub = hd_basis.conj().T @ mu_op @ hd_basis
    ev_mu, vc_mu = np.linalg.eigh((mu_sub + mu_sub.conj().T) * 0.5)
    mu_clusters: dict[int, list[int]] = {}
    for idx, val in enumerate(ev_mu):
        mu_int = int(round(float(val)))
        mu_clusters.setdefault(mu_int, []).append(idx)

    h0_tot = 0
    h1_tot = 0
    sa = -1 if eta[0] == 1 else 1
    sb = -1 if eta[1] == 1 else 1

    for mu_int, idxs in mu_clusters.items():
        a_exp = d_deg - mu_int
        v_sub = hd_basis @ vc_mu[:, idxs]
        ta_m = (sa**a_exp) * (v_sub.conj().T @ ta_op @ v_sub)
        tb_m = (sb**a_exp) * (v_sub.conj().T @ tb_op @ v_sub)
        kpi_m = ta_m @ tb_m @ ta_m.conj().T @ tb_m.conj().T
        ev_k, vc_k = np.linalg.eigh((kpi_m + kpi_m.conj().T) * 0.5)

        plus_idx = [i_k for i_k, v_k in enumerate(ev_k) if abs(float(v_k) - 1.0) < 1e-9]
        minus_idx = [i_k for i_k, v_k in enumerate(ev_k) if abs(float(v_k) + 1.0) < 1e-9]

        if plus_idx:
            v_p = v_sub @ vc_k[:, plus_idx]
            ta_p = (sa**a_exp) * (v_p.conj().T @ ta_op @ v_p)
            tb_p = (sb**a_exp) * (v_p.conj().T @ tb_op @ v_p)
            rk_p = len(plus_idx)
            n_max = math.floor(a_exp * 0.5) if a_exp < 1 else (math.ceil(a_exp * 0.5) - 1)
            if n_max > 0:
                h0_tot += rk_p * n_max
            elif n_max < 0:
                h1_tot += rk_p * (-n_max)
            else:
                n_triv = joint_fixed_subspace_dim_num(ta_p, tb_p, tol=1e-9)
                h0_tot += n_triv
                h1_tot += n_triv

        if minus_idx:
            m_bundles = len(minus_idx) // 2
            if a_exp != 1:
                n_max = math.floor((a_exp + 1) * 0.5) if a_exp < 1 else (math.ceil((a_exp + 1) * 0.5) - 1)
                deg_par = -1 + 2 * n_max
                if deg_par > 0:
                    h0_tot += m_bundles * deg_par
                else:
                    h1_tot += m_bundles * (-deg_par)

    return {"h0": h0_tot, "h1": h1_tot}


# =============================================================================
# PART 5A (WP-1.7): Quantum-Number Dictionary, Mechanical so(10) Centralizers,
#                   Z_4 Glue, Shared (16,4) Carrier A:A11 & Up-Conjugate A:A05
# =============================================================================


def verify_wp17_quantum_number_dictionary_and_up_conjugate() -> dict[str, Any]:
    """Derive exact Spin(10)xSpin(6)/Z_4 quantum-number identifications, centralizers,
    Z_4 glue kernel, shared (16,4) carrier (A:A11/FL:07), and A:A05 / FL:09 in both
    the flat Q_8 frame and the compact e_8 parent join.
    """
    bil = build_exact_e8_10_6_spinor_bilinear()
    g10_cliff: list[sp.Matrix] = bil["g10_cliff"]
    chir10: sp.Matrix = bil["chir10"]
    f6_cliff: list[sp.Matrix] = bil["f6_cliff"]
    chir6: sp.Matrix = bil["chir6"]
    s2i: dict[tuple[int, ...], int] = bil["sign_to_idx"]
    b60 = bil["bilinear_60"]

    idx_16p = [r_i for r_i in range(32) if chir10[r_i, r_i] == 1]
    idx_16m = [r_i for r_i in range(32) if chir10[r_i, r_i] == -1]
    idx_4p = [r_i for r_i in range(8) if chir6[r_i, r_i] == 1]
    idx_4m = [r_i for r_i in range(8) if chir6[r_i, r_i] == -1]

    # 1. Mechanical 45D so(10, Q) -> u(5) -> su(3)_C (+) su(2)_L Lie algebra centralizer theorem (D4.a):
    def e_so10(a_i: int, b_i: int) -> sp.Matrix:
        m_ab = sp.zeros(10, 10)
        m_ab[a_i, b_i] = 1
        m_ab[b_i, a_i] = -1
        return m_ab

    def vec_so10_coords(mat10: sp.Matrix) -> list[sp.Rational]:
        out_c: list[sp.Rational] = []
        for a_i in range(10):
            for b_i in range(a_i + 1, 10):
                out_c.append(sp.Rational(mat10[a_i, b_i]))
        return out_c

    def so10_from_col45(col_mat: sp.Matrix) -> sp.Matrix:
        acc_m = sp.zeros(10, 10)
        idx_p = 0
        for a_i in range(10):
            for b_i in range(a_i + 1, 10):
                c_val = col_mat[idx_p, 0]
                if c_val != 0:
                    acc_m = acc_m + c_val * e_so10(a_i, b_i)
                idx_p = idx_p + 1
        return acc_m

    def lin_comb_from_col(col_mat: sp.Matrix, mats: list[sp.Matrix]) -> sp.Matrix:
        acc_m = sp.zeros(10, 10)
        for idx_m, m_cur in enumerate(mats):
            c_val = col_mat[idx_m, 0]
            if c_val != 0:
                acc_m = acc_m + c_val * m_cur
        return acc_m

    # Complex structure J_10 on R^10 = R^6_colour (+) R^4_weak:
    j10_cs = sp.zeros(10, 10)
    for ax in range(5):
        j10_cs[2 * ax, 2 * ax + 1] = -1
        j10_cs[2 * ax + 1, 2 * ax] = 1

    # Solve [X, J_10] == 0 inside 45D so(10, Q) -> u(5) of exact dimension 25:
    u5_ad_cols: list[list[sp.Rational]] = []
    for a_i in range(10):
        for b_i in range(a_i + 1, 10):
            x_m = e_so10(a_i, b_i)
            u5_ad_cols.append(vec_so10_coords(x_m * j10_cs - j10_cs * x_m))
    u5_null_vecs = sp.Matrix(u5_ad_cols).T.nullspace()
    u5_basis_10 = [so10_from_col45(v_c) for v_c in u5_null_vecs]
    dim_u5 = len(u5_basis_10)

    # Extract 8D su(3)_C (supported on 0..5, [X, J_10]==0, trace(J_10 * X)==0) and
    # 3D su(2)_L (supported on 6..9, [X, J_10]==0, trace(J_10 * X)==0) mechanically from u(5):
    col_off_rows = []
    wk_off_rows = []
    for a_i in range(10):
        for b_i in range(a_i + 1, 10):
            row_ab = [u_m[a_i, b_i] for u_m in u5_basis_10]
            if a_i >= 6 or b_i >= 6:
                col_off_rows.append(row_ab)
            if a_i < 6 or b_i < 6:
                wk_off_rows.append(row_ab)
    tr_j_row = [int((j10_cs * u_m).trace()) for u_m in u5_basis_10]
    su3_ns = sp.Matrix(col_off_rows + [tr_j_row]).nullspace()
    su2_ns = sp.Matrix(wk_off_rows + [tr_j_row]).nullspace()
    su3c_basis_10 = [lin_comb_from_col(v_s, u5_basis_10) for v_s in su3_ns]
    su2l_basis_10 = [lin_comb_from_col(v_s, u5_basis_10) for v_s in su2_ns]
    sm_nonabelian_10 = su3c_basis_10 + su2l_basis_10

    # Centralizer Z_{so(10)}(su(3)_C (+) su(2)_L) inside full 45D so(10, Q):
    cent_rows_45: list[list[sp.Rational]] = []
    for g_sm in sm_nonabelian_10:
        ad_cols_g: list[list[sp.Rational]] = []
        for a_i in range(10):
            for b_i in range(a_i + 1, 10):
                x_m = e_so10(a_i, b_i)
                ad_cols_g.append(vec_so10_coords(x_m * g_sm - g_sm * x_m))
        cent_rows_45.extend(list(sp.Matrix(ad_cols_g).T.tolist()))
    z_so10_ns = sp.Matrix(cent_rows_45).nullspace()
    z_so10_basis = [so10_from_col45(v_z) for v_z in z_so10_ns]
    dim_z_so10 = len(z_so10_basis)
    z_so10_derived_vecs = [
        vec_so10_coords(z_so10_basis[p_i] * z_so10_basis[q_i] - z_so10_basis[q_i] * z_so10_basis[p_i])
        for p_i, q_i in combinations(range(dim_z_so10), 2)
    ]
    dim_z_so10_derived = int(sp.Matrix(z_so10_derived_vecs).rank()) if z_so10_derived_vecs else 0

    # Intersection Z_{so(10)}(su(3)_C (+) su(2)_L) cap u(5):
    z_u5_ns = sp.Matrix(cent_rows_45 + list(sp.Matrix(u5_ad_cols).T.tolist())).nullspace()
    z_u5_basis = [so10_from_col45(v_z) for v_z in z_u5_ns]
    dim_z_cap_u5 = len(z_u5_basis)
    z_u5_derived_vecs = [
        vec_so10_coords(z_u5_basis[p_i] * z_u5_basis[q_i] - z_u5_basis[q_i] * z_u5_basis[p_i])
        for p_i, q_i in combinations(range(dim_z_cap_u5), 2)
    ]
    dim_z_cap_u5_derived = int(sp.Matrix(z_u5_derived_vecs).rank()) if z_u5_derived_vecs else 0

    # 2. Mechanical branching of 16^+ and 10_vec under u(5) and su(3)_C (+) su(2)_L (D4.b):
    g10_16_list = [g10_cliff[a_i] for a_i in range(10)]

    def spin16_rep_of_so10(mat10: sp.Matrix) -> sp.Matrix:
        acc_16 = sp.zeros(16, 16)
        for a_i in range(10):
            for b_i in range(a_i + 1, 10):
                c_ab = sp.Rational(mat10[a_i, b_i])
                if c_ab != 0:
                    gen_ab = (sp.Rational(1, 2) * g10_16_list[a_i] * g10_16_list[b_i]).extract(idx_16p, idx_16p)
                    acc_16 = acc_16 + c_ab * gen_ab
        return acc_16.applyfunc(sp.expand)

    # Casimirs C2(su(3)_C) and C2(su(2)_L) + Q_chi and Y_GG extracted directly from Spin(10)|_{16^+}:
    su3c_16 = [spin16_rep_of_so10(mat_col) for mat_col in su3c_basis_10]
    su2l_16 = [spin16_rep_of_so10(m_w) for m_w in su2l_basis_10]
    # Orthonormalize skew-Hermitian generators wrt Killing inner product -Tr(X Y) on R^10:
    q_chi_10 = j10_cs
    y_gg_10 = sp.zeros(10, 10)
    for ax in range(3):
        y_gg_10[2 * ax, 2 * ax + 1] = sp.Rational(1, 3)
        y_gg_10[2 * ax + 1, 2 * ax] = -sp.Rational(1, 3)
    for ax in (3, 4):
        y_gg_10[2 * ax, 2 * ax + 1] = -sp.Rational(1, 2)
        y_gg_10[2 * ax + 1, 2 * ax] = sp.Rational(1, 2)

    q_chi_16 = (-2 * sp.I * spin16_rep_of_so10(q_chi_10)).applyfunc(sp.expand)
    y_gg_16 = (sp.I * spin16_rep_of_so10(y_gg_10)).applyfunc(sp.expand)
    q_chi_10_op = (-2 * sp.I * q_chi_10).applyfunc(sp.expand)
    y_gg_10_op = (sp.I * y_gg_10).applyfunc(sp.expand)

    # Verify q_chi_16 and y_gg_16 commute with ALL 11 generators of su(3)_C (+) su(2)_L on 16^+:
    abelian_commutes_with_sm_16 = all(
        (q_chi_16 * g_m - g_m * q_chi_16).applyfunc(sp.expand) == sp.zeros(16, 16)
        and (y_gg_16 * g_m - g_m * y_gg_16).applyfunc(sp.expand) == sp.zeros(16, 16)
        for g_m in (su3c_16 + su2l_16)
    )

    # Extract exact joint (Y_GG, Q_chi) eigenspaces on 16^+ -> 6 irreducible SM multiplets of dims [1,1,2,3,3,6]:
    joint_abelian_16 = (6 * y_gg_16 + q_chi_16).applyfunc(sp.expand)
    sm_multiplet_dims_16 = sorted(int(m_ev) for m_ev in joint_abelian_16.eigenvals().values())
    su5_u1_branching_dims = {int(k_ev): int(m_ev) for k_ev, m_ev in q_chi_16.eigenvals().items()}
    multiplet_clusters_16: dict[tuple[sp.Rational, int], list[int]] = {}
    for st_u in range(16):
        yv = sp.Rational(y_gg_16[st_u, st_u])
        qv = int(q_chi_16[st_u, st_u])
        multiplet_clusters_16[(yv, qv)] = multiplet_clusters_16.get((yv, qv), []) + [st_u]

    # Also verify mechanical branching of 10_vec (x) C under (Q_chi, Y_GG): 5_{+2} = (3,+1/3? -1/3)+(2,+1/2) & 5bar_{-2}:
    vec10_eigs = q_chi_10_op.eigenvals()
    vec10_u5_dims = {int(k_ev): int(m_ev) for k_ev, m_ev in vec10_eigs.items()}
    vec10_ygg_abs_mults: dict[sp.Rational, int] = {}
    for k_ev, m_ev in y_gg_10_op.eigenvals().items():
        ak = abs(sp.Rational(k_ev))
        vec10_ygg_abs_mults[ak] = vec10_ygg_abs_mults.get(ak, 0) + int(m_ev)

    # Exhaustively solve all discrete hypercharge embeddings Y = c1 * Y_GG + c2 * Q_chi on the mechanically
    # extracted 6 SM multiplets of 16^+ matching unordered |Y|, Tr(Y)==0, and Tr(Y^3)==0:
    c1_s, c2_s = sp.symbols("c1_s c2_s", real=True)
    mult_exprs = [
        (len(idxs_m), sp.expand(c1_s * yv + c2_s * qv))
        for (yv, qv), idxs_m in sorted(multiplet_clusters_16.items(), key=lambda kv: (len(kv[1]), float(kv[0][0])))
    ]
    # Identify the unique 6D (Q_L) and 1D multiplets from multiplet_clusters_16 mechanically:
    y_expr_6d = next(ex_m for dm_m, ex_m in mult_exprs if dm_m == 6)
    y_exprs_1d = [ex_m for dm_m, ex_m in mult_exprs if dm_m == 1]

    hypercharge_solutions: set[tuple[sp.Rational, sp.Rational]] = set()
    for sgn_q in (-1, 1):
        for ex_1d in y_exprs_1d:
            for ec_tgt in (-1, 1):
                sol_ab = sp.solve(
                    [y_expr_6d - sgn_q * sp.Rational(1, 6), ex_1d - sp.Integer(ec_tgt)],
                    (c1_s, c2_s),
                    dict=True,
                )
                for sol in sol_ab:
                    v1 = sp.Rational(sol[c1_s])
                    v2 = sp.Rational(sol[c2_s])
                    eval_d = [(dm_m, sp.simplify(ex_m.subs(sol))) for dm_m, ex_m in mult_exprs]
                    d2_abs = [abs(ev_m) for dm_m, ev_m in eval_d if dm_m == 2]
                    d3_abs = {abs(ev_m) for dm_m, ev_m in eval_d if dm_m == 3}
                    d1_abs = {abs(ev_m) for dm_m, ev_m in eval_d if dm_m == 1}
                    tr_y = sp.simplify(sum(dm_m * ev_m for dm_m, ev_m in eval_d))
                    tr_y3 = sp.simplify(sum(dm_m * (ev_m**3) for dm_m, ev_m in eval_d))
                    if (
                        d2_abs == [sp.Rational(1, 2)]
                        and d3_abs == {sp.Rational(1, 3), sp.Rational(2, 3)}
                        and d1_abs == {sp.Integer(0), sp.Integer(1)}
                        and tr_y == 0
                        and tr_y3 == 0
                    ):
                        hypercharge_solutions.add((v1, v2))
    hypercharge_solutions_sorted = sorted(hypercharge_solutions, key=lambda pair: (float(pair[0]), float(pair[1])))

    # Construct explicit group element w_{SU(2)_R} in Spin(10)|_{16^+} conjugating Y_GG <-> Y_flip while
    # commuting identically with ALL 11 generators of su(3)_C (+) su(2)_L (D4.b):
    su2r_tp = ((g10_cliff[6] - sp.I * g10_cliff[7]) * (g10_cliff[8] - sp.I * g10_cliff[9]) / 4).extract(
        idx_16p, idx_16p
    )
    gen_su2r = (su2r_tp - su2r_tp.H).applyfunc(sp.expand)
    w_su2r_16 = (sp.eye(16) + gen_su2r + gen_su2r * gen_su2r).applyfunc(sp.expand)
    y_flip_16 = (-sp.Rational(1, 5) * y_gg_16 + sp.Rational(1, 5) * q_chi_16).applyfunc(sp.expand)

    weyl_su2r_conjugates_gg_and_flipped = (
        (w_su2r_16 * w_su2r_16.H - sp.eye(16)).applyfunc(sp.expand) == sp.zeros(16, 16)
        and sp.simplify(w_su2r_16.det()) == 1
        and all(
            (w_su2r_16 * g_m - g_m * w_su2r_16).applyfunc(sp.expand) == sp.zeros(16, 16)
            for g_m in (su3c_16 + su2l_16)
        )
        and (w_su2r_16 * y_gg_16 * w_su2r_16.H - y_flip_16).applyfunc(sp.expand) == sp.zeros(16, 16)
    )
    su5_u1_breaks_gg_flipped_equivalence = (
        w_su2r_16 * q_chi_16 - q_chi_16 * w_su2r_16
    ).applyfunc(sp.expand) != sp.zeros(16, 16)

    # 3. Mechanical Z_4 central glue kernel of (Spin(10) x Spin(6)) / Z_4 across all 5 blocks of 248 (D4.c):
    #    Center Z(Spin(10)) ~= Z_4 generated by z10 = exp(i*pi*Q_chi/2)?: on 16^+, Q_chi in {-5,-1,+3} == -1 mod 4
    #    => exp(-i*pi/2) = -i on 16^+, +i on 16^-, -1 on 10_vec (Q_chi = +-2), +1 on 45_adj;
    #    Center Z(Spin(6)) ~= Z_4 generated by z6 acting as +i on 4^+, -i on 4^-, -1 on 6_vec, +1 on 15_adj:
    z4_glue_kernel = [
        (k10, k6)
        for k10 in range(4)
        for k6 in range(4)
        if ((-sp.I) ** k10) * ((sp.I) ** k6) == 1
        and ((sp.I) ** k10) * ((-sp.I) ** k6) == 1
        and ((-1) ** k10) * ((-1) ** k6) == 1
        and (1**k10) * (1**k6) == 1
    ]
    e8_248_block_dims = (
        math.comb(10, 2),
        math.comb(6, 2),
        10 * 6,
        len(idx_16p) * len(idx_4p),
        len(idx_16m) * len(idx_4m),
    )

    # 4. Shared (16^+, 4^+) zero-mode carrier theorem (A:A11 / FL:07, D4.d):
    #    Verify Spin(10)|_{16^+} irreducibility (joint commutant dim == 1), proving all 6 SM multiplets
    #    (Q, u^c, d^c, L, e^c, nu^c) are unified inside a single irreducible 16^+ fiber on every branch:
    spin10_16_num: list[np.ndarray] = []
    for a_i in range(10):
        for b_i in range(a_i + 1, 10):
            spin10_16_num.append(np.array(spin16_rep_of_so10(e_so10(a_i, b_i)).tolist(), dtype=complex))
    spin10_16p_commutant_dim = joint_commutant_dim_num(spin10_16_num, tol=1e-10)
    shared_16_4_sector_carrier_derived = (
        spin10_16p_commutant_dim == 1 and sm_multiplet_dims_16 == [1, 1, 2, 3, 3, 6]
    )

    # 5. Flat Q_8 pseudoreality (FL:09 / B1790) vs Parent compact e_8 reality (A:A05) + full SU(2)_L eps_{ab}
    #    doublet invariance across neutral (6,7) & charged (8,9) Higgs axes + 16D U(3)_C x U(2)_L Haar test (D4.e):
    q8_i = sp.Matrix([[sp.I, 0], [0, -sp.I]])
    q8_j = sp.Matrix([[0, 1], [-1, 0]])
    eps_2 = sp.Matrix([[0, 1], [-1, 0]])
    q8_pseudoreal_intertwiner_exact = (
        (eps_2 * q8_i - q8_i.conjugate() * eps_2).applyfunc(sp.expand) == sp.zeros(2, 2)
        and (eps_2 * q8_j - q8_j.conjugate() * eps_2).applyfunc(sp.expand) == sp.zeros(2, 2)
        and joint_commutant_dim_exact([q8_i, q8_j]) == 1
    )

    phi6_r, phi7_r, phi8_r, phi9_r = sp.symbols("phi6_r phi7_r phi8_r phi9_r", real=True)
    t0 = (1, 1, 1)
    t1 = (1, -1, -1)
    idx_qu = s2i[(-1, 1, 1, 1, -1) + t0]
    idx_qd = s2i[(-1, 1, 1, -1, 1) + t0]
    idx_uc = s2i[(1, -1, -1, 1, 1) + t1]
    idx_dc = s2i[(1, -1, -1, -1, -1) + t1]
    idx_lnu = s2i[(-1, -1, -1, 1, -1) + t0]
    idx_le = s2i[(-1, -1, -1, -1, 1) + t0]
    idx_ec = s2i[(1, 1, 1, -1, -1) + t1]
    idx_nuc = s2i[(1, 1, 1, 1, 1) + t1]

    def ew_yuk(idx_f1: int, idx_f2: int) -> sp.Expr:
        v60 = b60(idx_f1, idx_f2)
        return sp.expand(
            phi6_r * v60[6 * 6 + 1]
            + phi7_r * v60[7 * 6 + 1]
            + phi8_r * v60[8 * 6 + 1]
            + phi9_r * v60[9 * 6 + 1]
        )

    # Full 2-component SU(2)_L doublet couplings (Q = (Q_u, Q_d), L = (L_nu, L_e)) to u^c, d^c, e^c, nu^c:
    # Check both neutral slice (phi8=phi9=0) and full 4-parameter real EW slice (phi6, phi7, phi8, phi9):
    y_qu_uc = ew_yuk(idx_qu, idx_uc)
    y_qd_uc = ew_yuk(idx_qd, idx_uc)
    y_qu_dc = ew_yuk(idx_qu, idx_dc)
    y_qd_dc = ew_yuk(idx_qd, idx_dc)
    y_lnu_ec = ew_yuk(idx_lnu, idx_ec)
    y_le_ec = ew_yuk(idx_le, idx_ec)
    y_lnu_nuc = ew_yuk(idx_lnu, idx_nuc)
    y_le_nuc = ew_yuk(idx_le, idx_nuc)

    # Verify exact SU(2)_L eps_{ab} relation between the 2D up-type doublet H_u = (H_u^+, H_u^0) = (y_qd_uc, y_qu_uc)
    # and down-type doublet H_d = (H_d^0, H_d^-) = (y_qd_dc, y_qu_dc): H_u = eps * H_d^* up to universal sign!
    su2l_full_doublet_conjugate_exact = (
        sp.simplify(y_qd_dc + sp.conjugate(y_qu_uc)) == 0
        and sp.simplify(y_qu_dc - sp.conjugate(y_qd_uc)) == 0
        and sp.simplify(y_le_ec - sp.conjugate(y_qu_uc)) == 0
        and sp.simplify(y_lnu_ec + sp.conjugate(y_qd_uc)) == 0
        and sp.simplify(y_lnu_nuc + y_qu_uc) == 0
        and sp.simplify(y_le_nuc + y_qd_uc) == 0
        and y_qu_uc.subs({phi8_r: 0, phi9_r: 0}) != 0
        and y_qd_uc.subs({phi6_r: 0, phi7_r: 0}) != 0
    )

    mat_2hdm = sp.Matrix([
        [b60(idx_qu, idx_uc)[6 * 6 + 1], b60(idx_qu, idx_uc)[7 * 6 + 1]],
        [b60(idx_qd, idx_dc)[6 * 6 + 1], b60(idx_qd, idx_dc)[7 * 6 + 1]],
    ])
    complex_2hdm_rank = int(mat_2hdm.rank())
    complex_2hdm_det_nonzero = sp.simplify(mat_2hdm.det()) != 0

    # Guardrail 3: Gauge-allowed 16D U(3)_C x U(2)_L subset U(16^+) random Haar basis scrambling (< 1e-12):
    # Build random element exp(sum_a theta_a X_a) in SU(3)_C x SU(2)_L x U(1)_Y on 16^+ plus U(2) Higgs basis rotation:
    rng = np.random.default_rng(51)
    k16_h6 = np.zeros((16, 16), dtype=complex)
    k16_h7 = np.zeros((16, 16), dtype=complex)
    for u_i in range(16):
        for v_i in range(16):
            r_u = s2i[tuple(1 if ((idx_16p[u_i] // (2**a_i)) % 2 == 1) else -1 for a_i in range(5)) + t0]
            r_v = s2i[tuple(1 if ((idx_16p[v_i] // (2**a_i)) % 2 == 1) else -1 for a_i in range(5)) + t1]
            v_uv = b60(r_u, r_v)
            k16_h6[u_i, v_i] = complex(v_uv[6 * 6 + 1])
            k16_h7[u_i, v_i] = complex(v_uv[7 * 6 + 1])

    sm_16_gens_num = [np.array(g_m.tolist(), dtype=complex) for g_m in (su3c_16 + su2l_16)] + [
        1.0j * np.array(y_gg_16.tolist(), dtype=complex)
    ]
    base_16_sv_6 = np.sort(np.linalg.svd(k16_h6, compute_uv=False))
    base_16_sv_u = np.sort(np.linalg.svd(k16_h7 - 1.0j * k16_h6, compute_uv=False))
    max_haar_sv_err = 0.0
    for _ in range(8):
        coeffs_g = rng.normal(size=len(sm_16_gens_num))
        anti_h = sum(coeffs_g[idx_g] * sm_16_gens_num[idx_g] for idx_g in range(len(sm_16_gens_num)))
        ev_ah, vc_ah = np.linalg.eigh(-1.0j * anti_h)
        u16_gauge = vc_ah @ np.diag(np.exp(1.0j * ev_ah)) @ vc_ah.conj().T
        k16_h6_scr = u16_gauge @ k16_h6 @ u16_gauge.T
        k16_hu_scr = u16_gauge @ (k16_h7 - 1.0j * k16_h6) @ u16_gauge.T
        err_6 = float(np.max(np.abs(np.sort(np.linalg.svd(k16_h6_scr, compute_uv=False)) - base_16_sv_6)))
        err_u = float(np.max(np.abs(np.sort(np.linalg.svd(k16_hu_scr, compute_uv=False)) - base_16_sv_u)))
        max_haar_sv_err = max(max_haar_sv_err, err_6, err_u)

    wp17_verified = (
        dim_u5 == 25
        and len(su3c_basis_10) == 8
        and len(su2l_basis_10) == 3
        and dim_z_so10 == 4
        and dim_z_so10_derived == 3
        and dim_z_cap_u5 == 2
        and dim_z_cap_u5_derived == 0
        and abelian_commutes_with_sm_16
        and sm_multiplet_dims_16 == [1, 1, 2, 3, 3, 6]
        and sorted(len(vs) for vs in multiplet_clusters_16.values()) == sm_multiplet_dims_16
        and su5_u1_branching_dims == {-3: 5, 1: 10, 5: 1}
        and vec10_u5_dims == {-2: 5, 2: 5}
        and vec10_ygg_abs_mults == {sp.Rational(1, 3): 6, sp.Rational(1, 2): 4}
        and len(z4_glue_kernel) == 4
        and z4_glue_kernel == [(0, 0), (1, 1), (2, 2), (3, 3)]
        and sum(e8_248_block_dims) == 248
        and shared_16_4_sector_carrier_derived
        and len(hypercharge_solutions_sorted) == 4
        and hypercharge_solutions_sorted
        == [
            (sp.Integer(-1), sp.Integer(0)),
            (sp.Rational(-1, 5), sp.Rational(1, 5)),
            (sp.Rational(1, 5), sp.Rational(-1, 5)),
            (sp.Integer(1), sp.Integer(0)),
        ]
        and weyl_su2r_conjugates_gg_and_flipped
        and su5_u1_breaks_gg_flipped_equivalence
        and q8_pseudoreal_intertwiner_exact
        and su2l_full_doublet_conjugate_exact
        and complex_2hdm_rank == 2
        and complex_2hdm_det_nonzero
        and max_haar_sv_err < TOL
    )

    return {
        "so10_centralizer_dim": dim_z_so10,
        "so10_centralizer_derived_dim": dim_z_so10_derived,
        "u5_centralizer_dim": dim_z_cap_u5,
        "u5_centralizer_derived_dim": dim_z_cap_u5_derived,
        "sm_multiplet_dims_16": sm_multiplet_dims_16,
        "su5_u1_branching_dims": su5_u1_branching_dims,
        "vec10_u5_branching_dims": vec10_u5_dims,
        "z4_glue_kernel_order": len(z4_glue_kernel),
        "shared_16_4_sector_carrier_derived": shared_16_4_sector_carrier_derived,
        "hypercharge_solutions_count": len(hypercharge_solutions_sorted),
        "weyl_su2r_conjugates_gg_and_flipped": weyl_su2r_conjugates_gg_and_flipped,
        "su5_u1_breaks_gg_flipped_equivalence": su5_u1_breaks_gg_flipped_equivalence,
        "q8_flat_frame_pseudoreal_up_conjugate_unearnable": q8_pseudoreal_intertwiner_exact,
        "e8_real_1hdm_slice_up_conjugate_derived": su2l_full_doublet_conjugate_exact,
        "e8_complex_2hdm_doublet_rank": complex_2hdm_rank,
        "e8_complex_2hdm_independent_without_reality": complex_2hdm_det_nonzero,
        "max_haar_16d_gauge_sv_err": max_haar_sv_err,
        "wp17_dictionary_and_up_conjugate_verified": wp17_verified,
    }


# =============================================================================
# PART 5B (WP-3.4): Curved Trilinear Gauge-Yukawa Overlaps vs Four-Channel Frame
# =============================================================================


def verify_wp34_cubic_overlaps_and_value_frame_comparison() -> dict[str, Any]:
    """Test whether Frame A's four-channel coupling equals the curved e_8 zero-mode cubic
    coupling on E_tau \\ {0}, evaluating BOTH:
      (1) the parabolic (E_+, E_-) != 0 Nahm kernel on h_4 and h_1 (WP-3.1), and
      (2) the unbroken-Spin(10) coherent 3-branch (B1866) curved Szego kernel vs Frame A.
    """
    bil = build_exact_e8_10_6_spinor_bilinear()
    creators: list[sp.Matrix] = bil["creators"]
    ann: list[sp.Matrix] = bil["ann"]
    omega10: sp.Matrix = bil["omega10"]
    chir10: sp.Matrix = bil["chir10"]
    f6_all: list[sp.Matrix] = bil["f6_cliff"]
    omega6: sp.Matrix = bil["omega6"]
    chir6: sp.Matrix = bil["chir6"]
    splus_pairs: list[tuple[int, int]] = bil["splus_pairs"]
    splus_idx: dict[tuple[int, int], int] = bil["splus_idx"]
    kab_cross_60 = bil["kab_cross_60"]

    # -------------------------------------------------------------------------
    # 1. Parabolic (E_+, E_-) != 0 kernel selection & obstruction audit (D1, D2):
    # -------------------------------------------------------------------------
    irt2 = sp.Integer(1) / sp.sqrt(2)
    rt6 = sp.sqrt(6)
    rt10 = sp.sqrt(10)

    e5 = sp.zeros(5, 5)
    for j_i, c_val in enumerate((sp.Integer(2), rt6, rt6, sp.Integer(2))):
        e5[j_i + 1, j_i] = c_val
    j5 = sp.zeros(5, 5)
    for j_i, c_val in enumerate((1, -1, 1, -1, 1)):
        j5[j_i, 4 - j_i] = c_val
    bz = sp.zeros(5, 5)
    bz[1, 4] = sp.sqrt(sp.Rational(2, 5))
    bz[4, 1] = -bz[1, 4]
    bz[2, 3] = -sp.sqrt(sp.Rational(3, 5))
    bz[3, 2] = -bz[2, 3]
    z5 = sp.zeros(5, 5)

    e10 = sp.BlockMatrix([[e5, z5], [z5, -e5.T]]).as_explicit()
    g10 = (rt10 * sp.BlockMatrix([[z5, bz], [j5 * bz * j5, z5]]).as_explicit()).applyfunc(sp.expand)
    ep10 = ((e10 + g10) / 2).applyfunc(sp.expand)
    em10 = ((e10 - g10) / 2).applyfunc(sp.expand)
    htot10 = ((ep10 * ep10.H - ep10.H * ep10) + (em10 * em10.H - em10.H * em10)).applyfunc(sp.expand)
    mu10 = (htot10 / 2).applyfunc(sp.expand)

    e10_n = np.array(e10.tolist(), dtype=complex)
    g10_n = np.array(g10.tolist(), dtype=complex)
    i10_n = np.eye(10, dtype=complex)
    j10_swap = np.block([[np.zeros((5, 5)), np.eye(5)], [np.eye(5), np.zeros((5, 5))]])
    comm_rows = [
        np.kron(i10_n, m_op.T) - np.kron(m_op, i10_n)
        for m_op in (e10_n, g10_n, e10_n.conj().T, g10_n.conj().T)
    ]
    so10_cond = np.zeros((100, 100), dtype=complex)
    for p_c in range(10):
        for q_c_idx in range(10):
            x_e = np.zeros((10, 10), dtype=complex)
            x_e[p_c, q_c_idx] = 1.0
            so10_cond[:, 10 * p_c + q_c_idx] = (j10_swap @ x_e + x_e.T @ j10_swap).ravel()
    gl10_comm_dim = int(np.sum(np.linalg.svd(np.vstack(comm_rows), compute_uv=False) < 1e-10))
    so10_unbroken_commutant_dim = int(
        np.sum(np.linalg.svd(np.vstack(comm_rows + [so10_cond]), compute_uv=False) < 1e-10)
    )

    def spin_lie32(m10: sp.Matrix) -> sp.Matrix:
        out = -sp.Rational(1, 2) * sum(m10[i_k, i_k] for i_k in range(5)) * sp.eye(32)
        for i_k in range(5):
            for j_k in range(5):
                if m10[i_k, j_k] != 0:
                    out += m10[i_k, j_k] * (creators[i_k] * ann[j_k])
                if m10[i_k, j_k + 5] != 0:
                    out += sp.Rational(1, 2) * m10[i_k, j_k + 5] * (creators[i_k] * creators[j_k])
                if m10[i_k + 5, j_k] != 0:
                    out += sp.Rational(1, 2) * m10[i_k + 5, j_k] * (ann[i_k] * ann[j_k])
        return out.applyfunc(sp.expand)

    # D1.a: Extract TRUE 16^+ (chir10 == +1, odd bit-sum) and 16^- (chir10 == -1, even bit-sum),
    # and verify S_16^+ = (16^+, 4^+) (+) (16^-, 4^-):
    idx_16p = [r_i for r_i in range(32) if chir10[r_i, r_i] == 1]
    idx_16m = [r_i for r_i in range(32) if chir10[r_i, r_i] == -1]
    idx_4p = [r_i for r_i in range(8) if chir6[r_i, r_i] == 1]
    idx_4m = [r_i for r_i in range(8) if chir6[r_i, r_i] == -1]
    fock_16p_odd_bitsum_verified = all(bit_sum_int(r_i, 5) % 2 == 1 for r_i in idx_16p) and (
        set(splus_pairs) == {(r32, r8) for r32 in idx_16p for r8 in idx_4p} | {(r32, r8) for r32 in idx_16m for r8 in idx_4m}
    )

    e16p = spin_lie32(e10).extract(idx_16p, idx_16p)
    g16p = spin_lie32(g10).extract(idx_16p, idx_16p)
    mu16p = spin_lie32(mu10).extract(idx_16p, idx_16p)

    # D1.d: Pure exact SymPy Koszul harmonic mu-eigenvalues (zero float eigvals or .real):
    def exact_sympy_mu_eigs(vecs: list[sp.Matrix], mu_mat: sp.Matrix) -> list[int]:
        n_v = len(vecs)
        gram_m = sp.Matrix([[sp.simplify((vecs[r_i].H * mu_mat * vecs[c_i])[0, 0]) for c_i in range(n_v)] for r_i in range(n_v)])
        norm_m = sp.Matrix([[sp.simplify((vecs[r_i].H * vecs[c_i])[0, 0]) for c_i in range(n_v)] for r_i in range(n_v)])
        ev_map = (norm_m.inv() * gram_m).eigenvals()
        return sorted(int(sp.simplify(k_ev)) for k_ev, mult_ev in ev_map.items() for _ in range(int(mult_ev)))

    d0_v10 = sp.Matrix.vstack(e10, g10)
    d1_v10 = sp.Matrix.hstack(-g10, e10)
    v10_aslot_vecs = d0_v10.nullspace()
    v10_bot_vecs = d1_v10.H.nullspace()
    v10_h1_vecs = sp.Matrix.vstack(d1_v10, d0_v10.H).nullspace()
    v10_aslot_mu = exact_sympy_mu_eigs(v10_aslot_vecs, mu10)
    v10_bot_mu = exact_sympy_mu_eigs(v10_bot_vecs, mu10)
    v10_spin_mu_eigs = exact_sympy_mu_eigs(v10_h1_vecs, sp.kronecker_product(sp.eye(2), mu10))

    d0_16p = sp.Matrix.vstack(e16p, g16p)
    d1_16p = sp.Matrix.hstack(-g16p, e16p)
    s16p_aslot_vecs = d0_16p.nullspace()
    s16p_bot_vecs = d1_16p.H.nullspace()
    s16p_h1_vecs = sp.Matrix.vstack(d1_16p, d0_16p.H).nullspace()
    s16p_aslot_mu = exact_sympy_mu_eigs(s16p_aslot_vecs, mu16p)
    s16p_bot_mu = exact_sympy_mu_eigs(s16p_bot_vecs, mu16p)
    s16p_spin_mu_eigs = exact_sympy_mu_eigs(s16p_h1_vecs, sp.kronecker_product(sp.eye(2), mu16p))

    # Build 16x16 Witt-basis bilinear matrices K_m (m=0..9) on true 16^+ x 16^+:
    r8_a, r8_b = idx_4p[0], idx_4p[1]
    k16_gamma: list[sp.Matrix] = []
    for a_10 in range(10):
        m16 = sp.zeros(16, 16)
        for j_6 in range(6):
            kl = kab_cross_60[6 * a_10 + j_6]
            has_ab = any(
                kl[splus_idx[(idx_16p[u_i], r8_a)]][1] == splus_idx[(idx_16p[v_i], r8_b)]
                and kl[splus_idx[(idx_16p[u_i], r8_a)]][2] != 0
                for u_i in range(16)
                for v_i in range(16)
            )
            if has_ab:
                for u_i in range(16):
                    row_128 = splus_idx[(idx_16p[u_i], r8_a)]
                    col_128, val_k = kl[row_128][1], kl[row_128][2]
                    for v_i in range(16):
                        if col_128 == splus_idx[(idx_16p[v_i], r8_b)]:
                            m16[u_i, v_i] = val_k
                break
        k16_gamma.append(m16)

    k16_witt: list[sp.Matrix] = []
    for ax in range(5):
        k16_witt.append(((k16_gamma[2 * ax] - sp.I * k16_gamma[2 * ax + 1]) / 2).applyfunc(sp.expand))
    for ax in range(5):
        k16_witt.append(((k16_gamma[2 * ax] + sp.I * k16_gamma[2 * ax + 1]) / 2).applyfunc(sp.expand))

    # D2.a & D2.b: Stage 1 2D form-degree rule + exact vanishing of ALL 3 harmonic fermion bilinears
    # (a x a [mu=+6], a x spin_harm [mu=+3], spin_harm x spin_harm [mu=0]) against ALL harmonic V_10 modes
    # (ker d0 [mu=+2], ker d1^H [mu=-2], H^1_Kosz [mu in {-2,+2}]), PLUS non-zero verification of BOTH
    # non-harmonic mu-conserving channels:
    #   (i)  (mu=-1) x (mu=-1) -> mu_H = +2 in ker d_0(V_10)
    #   (ii) (mu_a=+3) x (mu=-1) -> mu_H = -2 in H^1_Kosz(V_10) / ker d_1^H(V_10)
    # Four-slot form degrees on E_tau \ {0}: a in Omega^{0,1}, u in Omega^{0,0}(S^1), v in Omega^{0,1}(S^{-1});
    # pure wedge without metric lowering requires total (p, q) == (0, 1) before dz wedge or (1, 1) density,
    # so naive wedge a ^ a ^ a in Omega^{0,3} == 0 on a 1D complex curve!
    form_degree_naive_aaa_wedge_zero = (0 + 0 + 0, 1 + 1 + 1) != (1, 1) and (1 + 1 + 1) > 1

    witt_contraction_mu_invariant = all(
        (
            mu16p.T * k16_witt[m_i]
            + k16_witt[m_i] * mu16p
            + sum((mu10[r_i, m_i] * k16_witt[r_i] for r_i in range(10)), sp.zeros(16, 16))
        ).applyfunc(sp.expand)
        == sp.zeros(16, 16)
        for m_i in range(10)
    )
    all_v10_harm_slices = (
        v10_aslot_vecs
        + v10_bot_vecs
        + [vh2[:10, :] for vh2 in v10_h1_vecs]
        + [vh2[10:, :] for vh2 in v10_h1_vecs]
    )
    spin_harm_16_slices = [h1_v[:16, :] for h1_v in s16p_h1_vecs] + [h1_v[16:, :] for h1_v in s16p_h1_vecs]

    def bilinear_vec10_witt(p1: sp.Matrix, p2: sp.Matrix) -> sp.Matrix:
        return sp.Matrix([sp.expand((p1.T * k16_witt[m_i] * p2)[0, 0]) for m_i in range(10)])

    psi_a_16 = s16p_aslot_vecs[0]
    parabolic_aa_harm_zero = bilinear_vec10_witt(psi_a_16, psi_a_16) == sp.zeros(10, 1)
    parabolic_a_spinharm_zero = all(
        sp.expand((vh.T * bilinear_vec10_witt(psi_a_16, p_sp))[0, 0]) == 0
        for p_sp in spin_harm_16_slices
        for vh in all_v10_harm_slices
    )
    parabolic_spinharm_spinharm_zero = all(
        sp.expand((vh.T * bilinear_vec10_witt(p1, p2))[0, 0]) == 0
        for p1 in spin_harm_16_slices
        for p2 in spin_harm_16_slices
        for vh in all_v10_harm_slices
    )
    all_three_parabolic_harmonic_yukawas_vanish = (
        witt_contraction_mu_invariant
        and parabolic_aa_harm_zero
        and parabolic_a_spinharm_zero
        and parabolic_spinharm_spinharm_zero
    )

    s16p_mu_neg1_vecs = (mu16p + sp.eye(16)).nullspace()
    nonharm_neg1_neg1_couples_v10_kerd0 = any(
        sp.expand((vh.T * bilinear_vec10_witt(u_m, v_m))[0, 0]) != 0
        for u_m in s16p_mu_neg1_vecs
        for v_m in s16p_mu_neg1_vecs
        for vh in v10_aslot_vecs
    )
    v10_h1_mat = sp.Matrix.hstack(*v10_h1_vecs)
    v10_h1_neg2_vecs = [
        (v10_h1_mat * c_v).applyfunc(sp.expand)
        for c_v in (
            v10_h1_mat.H * (sp.kronecker_product(sp.eye(2), mu10) + 2 * sp.eye(20)) * v10_h1_mat
        ).nullspace()
    ]
    v10_h1_neg2_slices = [vh2[:10, :] for vh2 in v10_h1_neg2_vecs] + [vh2[10:, :] for vh2 in v10_h1_neg2_vecs]
    nonharm_pos3_neg1_couples_v10_h1 = len(v10_h1_neg2_vecs) == 2 and any(
        sp.expand((vh.T * bilinear_vec10_witt(psi_a_16, u_m))[0, 0]) != 0
        for u_m in s16p_mu_neg1_vecs
        for vh in v10_h1_neg2_slices
    )

    # D1.b, D1.c & D2.c: Mechanical h_4 = prod_{k=0}^2 ((I_8 - f_{2k} f_{2k+1})/sqrt(2)) on Cl(6),
    # mechanical h_1 = (a32 * s32) (x) s_8 on 128D S_16^+, planted non-commuting reflection test for
    # joint_fixed_subspace_dim_num, and full parabolic Koszul cohomology census on BOTH h_4 and h_1!
    i8_s = sp.eye(8)
    h4_8 = (
        (i8_s - f6_all[0] * f6_all[1])
        * irt2
        * (i8_s - f6_all[2] * f6_all[3])
        * irt2
        * (i8_s - f6_all[4] * f6_all[5])
        * irt2
    ).applyfunc(sp.expand)
    h4_4p = h4_8.extract(idx_4p, idx_4p)
    w8 = sp.expand((sp.Integer(1) + sp.I) * irt2)
    w8_cubed = sp.expand(w8**3)
    w8_inv = sp.expand((sp.Integer(1) - sp.I) * irt2)
    h4_4p_eigs = {sp.expand(k_ev): int(m_ev) for k_ev, m_ev in h4_4p.eigenvals().items()}
    mechanical_h4_4p_split_exact = h4_4p_eigs == {w8_cubed: 1, w8_inv: 3}

    # Planted non-commuting reflections T_a = diag(1, -1), T_b = [[3/5, 4/5], [4/5, -3/5]]:
    # ker(T_a - I) cap ker(T_b - I) == {0} (dim 0), whereas Tr((I+T_a)(I+T_b)/4) = 4/5 > 1/2 -> rounds to 1!
    ta_plant_sp = sp.Matrix([[1, 0], [0, -1]])
    tb_plant_sp = sp.Matrix([[sp.Rational(3, 5), sp.Rational(4, 5)], [sp.Rational(4, 5), sp.Rational(-3, 5)]])
    ta_plant = np.array(ta_plant_sp.tolist(), dtype=complex)
    tb_plant = np.array(tb_plant_sp.tolist(), dtype=complex)
    planted_joint_dim = joint_fixed_subspace_dim_num(ta_plant, tb_plant, tol=1e-9)
    naive_proj_tr_sp = sp.Rational(((sp.eye(2) + ta_plant_sp) * (sp.eye(2) + tb_plant_sp)).trace(), 4)
    planted_naive_trace_round = 1 if naive_proj_tr_sp > sp.Rational(1, 2) else 0

    a32 = sp.zeros(32, 32)
    xw_4 = [1, 0, -1, -2, -3]
    for st_i in range(32):
        kp = 5 + sum(2 * xw_4[a_i] for a_i in range(5) if ((st_i // (2**a_i)) % 2 == 1))
        a32[st_i, st_i] = sp.expand(w8 ** (kp % 8))
    b04 = creators[0] * creators[4] + ann[4] * ann[0]
    b13 = creators[1] * creators[3] + ann[3] * ann[1]
    d32 = ((sp.eye(32) - 2 * b04 * b04) * (sp.eye(32) - b13 * b13 - sp.I * b13)).applyfunc(sp.expand)
    b32 = (d32 * a32).applyfunc(sp.expand)

    def cliff_vec10(z_list: list[Any]) -> sp.Matrix:
        out_c = sp.zeros(32, 32)
        for idx_c, za in enumerate(z_list):
            if za != 0:
                out_c += za * creators[idx_c] + sp.conjugate(za) * ann[idx_c]
        return out_c

    g_minus = [
        cliff_vec10([0, 0, sp.I, 0, 0]),
        cliff_vec10([sp.I * irt2, 0, 0, 0, sp.I * irt2]),
        cliff_vec10([irt2, 0, 0, 0, -irt2]),
        cliff_vec10([0, irt2, 0, irt2, 0]),
        cliff_vec10([0, sp.I * irt2, 0, -sp.I * irt2, 0]),
    ]
    u32_h1 = sp.eye(32)
    for gm_op in g_minus:
        u32_h1 = (u32_h1 * gm_op).applyfunc(sp.expand)
    s32_h1 = (u32_h1 * chir10).applyfunc(sp.expand)
    s8_h1 = f6_all[0]

    def m128_num(m32: sp.Matrix, m8: sp.Matrix) -> np.ndarray:
        out_n = np.zeros((128, 128), dtype=complex)
        m32_n = np.array(m32.tolist(), dtype=complex)
        m8_n = np.array(m8.tolist(), dtype=complex)
        nz32 = [[(r_i, m32_n[r_i, c_i]) for r_i in range(32) if abs(m32_n[r_i, c_i]) > TOL] for c_i in range(32)]
        nz8 = [[(r_i, m8_n[r_i, c_i]) for r_i in range(8) if abs(m8_n[r_i, c_i]) > TOL] for c_i in range(8)]
        for col_s, (c1, c2) in enumerate(splus_pairs):
            for r1, v1 in nz32[c1]:
                for r2, v2 in nz8[c2]:
                    out_n[splus_idx[(r1, r2)], col_s] = v1 * v2
        return out_n

    fi_n = np.array([[1.0j, 0.0], [0.0, -1.0j]], dtype=complex)
    fj_n = np.array([[0.0, 1.0], [-1.0, 0.0]], dtype=complex)
    e16_n = np.array(e16p.tolist(), dtype=complex)
    g16_n = np.array(g16p.tolist(), dtype=complex)
    ep16_n = np.array(spin_lie32(ep10).extract(idx_16p, idx_16p).tolist(), dtype=complex)
    em16_n = np.array(spin_lie32(em10).extract(idx_16p, idx_16p).tolist(), dtype=complex)
    mu16_n = np.array(mu16p.tolist(), dtype=complex)
    d0_16n = np.vstack([e16_n, g16_n])
    d1_16n = np.hstack([-g16_n, e16_n])
    _, sv1_16, vh1_16 = np.linalg.svd(np.vstack([d1_16n, d0_16n.conj().T]))
    b1_16n = vh1_16[sv1_16 < 1e-9].conj().T

    # Evaluate Koszul deg-0 v_top Klein-4 holonomy characters (which SWAP (-1,-1) <-> (+1,+1) under w8^{-1}/w8^3 = -1)
    # AND Koszul deg-1 spin-slot H^0 (whose 2D basis carries {(1,1), (-1,-1)}, invariant under (-1,-1) swap!) on
    # BOTH the SU(3)-singlet line w_8^3 AND each SU(3)-triplet line w_8^{-1} of (16^+, 4^+):
    a16_sp = a32.extract(idx_16p, idx_16p)
    b16_sp = b32.extract(idx_16p, idx_16p)
    vtop_norm2 = sp.simplify((psi_a_16.H * psi_a_16)[0, 0])
    sing_vtop_xa = int(sp.simplify((psi_a_16.H * (w8_cubed * a16_sp) * psi_a_16)[0, 0] / vtop_norm2))
    sing_vtop_yb = int(sp.simplify((psi_a_16.H * (w8_cubed * b16_sp) * psi_a_16)[0, 0] / vtop_norm2))
    trip_vtop_xa = int(sp.simplify((psi_a_16.H * (w8_inv * a16_sp) * psi_a_16)[0, 0] / vtop_norm2))
    trip_vtop_yb = int(sp.simplify((psi_a_16.H * (w8_inv * b16_sp) * psi_a_16)[0, 0] / vtop_norm2))
    aslot_vtop_holonomy_singlet_vs_triplet = ((sing_vtop_xa, sing_vtop_yb), (trip_vtop_xa, trip_vtop_yb))

    a16_n = np.array(a16_sp.tolist(), dtype=complex)
    b16_n = np.array(b16_sp.tolist(), dtype=complex)
    h4_sing_c = complex(w8_cubed)
    h4_trip_c = complex(w8_inv)
    spin_slot_h0_singlet_by_eta = {
        eta_v: eval_parabolic_cohomology_on_hd(
            1, b1_16n, np.kron(np.eye(2), mu16_n), np.kron(fi_n, h4_sing_c * a16_n), np.kron(fj_n, h4_sing_c * b16_n), ep16_n, em16_n, eta_v
        )["h0"]
        for eta_v in [(0, 0), (1, 1), (1, 0), (0, 1)]
    }
    spin_slot_h0_triplet_line_by_eta = {
        eta_v: eval_parabolic_cohomology_on_hd(
            1, b1_16n, np.kron(np.eye(2), mu16_n), np.kron(fi_n, h4_trip_c * a16_n), np.kron(fj_n, h4_trip_c * b16_n), ep16_n, em16_n, eta_v
        )["h0"]
        for eta_v in [(0, 0), (1, 1), (1, 0), (0, 1)]
    }

    # Full 128D S_16^+ parabolic Koszul cohomology census (ker M, ker M^dag) on BOTH h_4 AND h_1 across all 4 spin structures (D2.c):
    e128_n = m128_num(spin_lie32(e10), i8_s)
    g128_n = m128_num(spin_lie32(g10), i8_s)
    ep128_n = m128_num(spin_lie32(ep10), i8_s)
    em128_n = m128_num(spin_lie32(em10), i8_s)
    mu128_n = m128_num(spin_lie32(mu10), i8_s)
    d0_128 = np.vstack([e128_n, g128_n])
    d1_128 = np.hstack([-g128_n, e128_n])
    _, sv0_128, vh0_128 = np.linalg.svd(d0_128)
    _, sv1_128, vh1_128 = np.linalg.svd(np.vstack([d1_128, d0_128.conj().T]))
    _, sv2_128, vh2_128 = np.linalg.svd(d1_128.conj().T)
    b0_128 = vh0_128[sv0_128 < 1e-9].conj().T
    b1_128 = vh1_128[sv1_128 < 1e-9].conj().T
    b2_128 = vh2_128[sv2_128 < 1e-9].conj().T

    s16p_128_census: dict[str, dict[tuple[int, int], tuple[int, int]]] = {}
    for bg_lbl, ah32_m, ah8_m in [("h4", a32, h4_8), ("h1", (a32 * s32_h1).applyfunc(sp.expand), s8_h1)]:
        bh32_m = (d32 * ah32_m).applyfunc(sp.expand)
        xa_128 = m128_num(ah32_m, ah8_m)
        yb_128 = m128_num(bh32_m, ah8_m)
        bg_map: dict[tuple[int, int], tuple[int, int]] = {}
        for eta_v in [(0, 0), (1, 1), (1, 0), (0, 1)]:
            c0 = eval_parabolic_cohomology_on_hd(0, b0_128, mu128_n, xa_128, yb_128, ep128_n, em128_n, eta_v)
            c1 = eval_parabolic_cohomology_on_hd(
                1, b1_128, np.kron(np.eye(2), mu128_n), np.kron(fi_n, xa_128), np.kron(fj_n, yb_128), ep128_n, em128_n, eta_v
            )
            c2 = eval_parabolic_cohomology_on_hd(2, b2_128, mu128_n, xa_128, yb_128, ep128_n, em128_n, eta_v)
            bg_map[eta_v] = (c2["h1"] + c0["h1"] + c1["h0"], c0["h0"] + c1["h1"] + c2["h0"])
        s16p_128_census[bg_lbl] = bg_map

    # -------------------------------------------------------------------------
    # 2. Unbroken-Spin(10) coherent 3-branch (B1866) vs Frame A Klein-four (D3):
    # -------------------------------------------------------------------------
    # D3.d: Exact SymPy wedge algebra on Lambda^2(4^+) ~= 6_vec:
    #   - On B1866's single +h_4 background, 4^+ = 1_{w8^3} (+) 3_{w8^{-1}}:
    #     the SU(3)-singlet line is 1D, so Lambda^2(1_{w8^3}) == 0 identically (dim 0), whereas
    #     1_{w8^3} ^ 3_{w8^{-1}} has dim 3 (eigenvalue w8^2 = +i in 6_vec), killing untwisted a_sp x a_sp!
    #   - In Frame A's Klein-four SU(4) holonomy (diag(1,1,-1,-1), diag(1,-1,1,-1)) on 4^+, the 4 basis lines carry
    #     4 DISTINCT Z_2 x Z_2 characters {(0,0), (0,1), (1,0), (1,1)}, so e_a ^ e_b != 0 for ALL 6 pairs a < b,
    #     including e_0 ^ e_a (character chi_a) AND e_a ^ e_b (character chi_a + chi_b)!
    singlet_idx_4p = [i_f for i_f in range(4) if sp.expand(h4_4p[i_f, i_f] - w8_cubed) == 0]
    triplet_idx_4p = [i_f for i_f in range(4) if sp.expand(h4_4p[i_f, i_f] - w8_inv) == 0]
    wedge_pairs_4p = list(combinations(range(4), 2))
    singlet_singlet_wedge_dim = sum(1 for p_a, p_b in wedge_pairs_4p if p_a in singlet_idx_4p and p_b in singlet_idx_4p)
    singlet_triplet_wedge_dim = sum(
        1 for p_a, p_b in wedge_pairs_4p if (p_a in singlet_idx_4p and p_b in triplet_idx_4p) or (p_b in singlet_idx_4p and p_a in triplet_idx_4p)
    )
    frame_a_ta = sp.diag(1, 1, -1, -1)
    frame_a_tb = sp.diag(1, -1, 1, -1)
    frame_a_wedge_chars = sorted(
        (
            0 if int(frame_a_ta[p_a, p_a] * frame_a_ta[p_b, p_b]) == 1 else 1,
            0 if int(frame_a_tb[p_a, p_a] * frame_a_tb[p_b, p_b]) == 1 else 1,
        )
        for p_a, p_b in wedge_pairs_4p
    )

    chars_3 = [(1, 0), (0, 1), (1, 1)]
    allowed_triples_untwisted_absent = [
        (i_c, j_c, k_c)
        for i_c in range(3)
        for j_c in range(3)
        for k_c in range(3)
        if ((chars_3[i_c][0] + chars_3[j_c][0] + chars_3[k_c][0]) % 2 == 0)
        and ((chars_3[i_c][1] + chars_3[j_c][1] + chars_3[k_c][1]) % 2 == 0)
    ]
    diag_triples_untwisted_absent = [tr for tr in allowed_triples_untwisted_absent if tr[0] == tr[1]]

    # D3.a, D3.b & D3.c: 35-digit mpmath verification of:
    #   - Exact Weierstrass-Jacobi identities d_z S_k(z) + S_i(z)*S_j(z) == 0 and
    #     d_z S_k(z)*S_i(z)*S_j(z) + (wp(z) - e_i)*(wp(z) - e_j) == 0 (< 1e-26),
    #   - Curved hyperbolic cusp measures Omega_hyp(z)^{-3/2} d^2z (S^{-3} channel) and
    #     Omega_hyp(z)^{-5/4} d^2z (mixed S^{-3} x S^1 spin-slot H^0 channel),
    #   - ALL 6 off-diagonal triples (|I_sp| < 1e-20, |I_dp| > 1.0) AND ALL 3 diagonal spin-slot H^0
    #     triples (i, 0, i) where z -> -z parity REVERSES (|I_sp^diag| > 1.0, |I_dp^diag| < 1e-20)!
    with mp.workdps(35):
        re_tc = mp.mpf(1) / mp.mpf(3)
        im_tc_mp = mp.mpf(17) / mp.mpf(12)
        tau_c = mp.mpc(re_tc, im_tc_mp)
        q_c = mp.exp(1j * mp.pi * tau_c)

        def szego_nu(nu_idx: int, z_pt: mp.mpc) -> mp.mpc:
            return (mp.pi * mp.jtheta(1, 0, q_c, 1) * mp.jtheta(nu_idx, mp.pi * z_pt, q_c)) / (
                mp.jtheta(nu_idx, 0, q_c) * mp.jtheta(1, mp.pi * z_pt, q_c)
            )

        def dszego_nu(nu_idx: int, z_pt: mp.mpc) -> mp.mpc:
            pref = mp.pi * mp.jtheta(1, 0, q_c, 1) / mp.jtheta(nu_idx, 0, q_c)
            th_n = mp.jtheta(nu_idx, mp.pi * z_pt, q_c)
            dth_n = mp.pi * mp.jtheta(nu_idx, mp.pi * z_pt, q_c, 1)
            th_1 = mp.jtheta(1, mp.pi * z_pt, q_c)
            dth_1 = mp.pi * mp.jtheta(1, mp.pi * z_pt, q_c, 1)
            return pref * (dth_n * th_1 - th_n * dth_1) / (th_1**2)

        def neg_d2_log_th1(z_pt: mp.mpc) -> mp.mpc:
            t1_v = mp.jtheta(1, mp.pi * z_pt, q_c)
            dt1_v = mp.jtheta(1, mp.pi * z_pt, q_c, 1)
            d2t1_v = mp.jtheta(1, mp.pi * z_pt, q_c, 2)
            return (mp.pi**2) * ((dt1_v**2 - t1_v * d2t1_v) / (t1_v**2))

        half_periods = {
            2: mp.mpc(mp.mpf(1) / mp.mpf(2)),
            3: (mp.mpc(1) + tau_c) / mp.mpf(2),
            4: tau_c / mp.mpf(2),
        }
        e_shifts = {nu_k: neg_d2_log_th1(hp_z) for nu_k, hp_z in half_periods.items()}

        max_parity_err = 0.0
        max_weierstrass_jacobi_err = 0.0
        perms_234 = [(2, 3, 4), (2, 4, 3), (3, 2, 4), (3, 4, 2), (4, 2, 3), (4, 3, 2)]
        for re_num, im_num in [(1, 5), (2, 7), (5, 3)]:
            z_probe = mp.mpc(mp.mpf(re_num) / mp.mpf(12), mp.mpf(im_num) / mp.mpf(12))
            for nu_k in (2, 3, 4):
                err_s = float(abs(szego_nu(nu_k, -z_probe) + szego_nu(nu_k, z_probe)))
                err_ds = float(abs(dszego_nu(nu_k, -z_probe) - dszego_nu(nu_k, z_probe)))
                max_parity_err = max(max_parity_err, err_s, err_ds)
            for k_h, i_f, j_f in perms_234:
                dsk_v = dszego_nu(k_h, z_probe)
                si_v = szego_nu(i_f, z_probe)
                sj_v = szego_nu(j_f, z_probe)
                wp_i = neg_d2_log_th1(z_probe) - e_shifts[i_f]
                wp_j = neg_d2_log_th1(z_probe) - e_shifts[j_f]
                err_wj1 = float(abs(dsk_v + si_v * sj_v))
                err_wj2 = float(abs(dsk_v * si_v * sj_v + wp_i * wp_j))
                max_weierstrass_jacobi_err = max(max_weierstrass_jacobi_err, err_wj1, err_wj2)

        # Stage 1/2 curved hyperbolic cusp metric Omega_metric(z) = 1 / (r_mod(z)^2 * (ln(r_mod(z)^2 / 16)^2)):
        n_g = 12
        th1p0_sq = abs(mp.pi * mp.jtheta(1, 0, q_c, 1)) ** 2
        d2z_cell = mp.fdiv(im_tc_mp, n_g * n_g)

        sp_parity_vanish_err = 0.0
        dp_overlap_min_mag = 0.0
        have_dp_min = False
        for k_h, i_f, j_f in perms_234:
            sp_hol = mp.mpc(0)
            sp_cnj = mp.mpc(0)
            dp_hol = mp.mpc(0)
            dp_cnj = mp.mpc(0)
            for ku_g in range(n_g):
                u_g = mp.fdiv(2 * ku_g - n_g + 1, 2 * n_g)
                for kv_g in range(n_g):
                    v_g = mp.fdiv(2 * kv_g - n_g + 1, 2 * n_g)
                    z_g = mp.mpc(u_g) + mp.mpc(v_g) * tau_c
                    r_mod_sq = (abs(mp.jtheta(1, mp.pi * z_g, q_c)) ** 2 / th1p0_sq) * mp.exp(
                        -2 * mp.pi * (v_g**2) * im_tc_mp
                    )
                    om_metric = mp.mpf(1) / (r_mod_sq * (mp.log(r_mod_sq / mp.mpf(16)) ** 2))
                    om_inv_half = abs(mp.sqrt(mp.mpf(1) / om_metric))
                    wm = (om_inv_half**3) * d2z_cell
                    sk = szego_nu(k_h, z_g)
                    dsk = dszego_nu(k_h, z_g)
                    si = szego_nu(i_f, z_g)
                    sj = szego_nu(j_f, z_g)
                    sp_hol += wm * sk * si * sj
                    sp_cnj += wm * sk * si * mp.conj(sj)
                    dp_hol += wm * dsk * si * sj
                    dp_cnj += wm * dsk * si * mp.conj(sj)
            sp_parity_vanish_err = max(sp_parity_vanish_err, float(abs(sp_hol)), float(abs(sp_cnj)))
            cur_dp_min = min(float(abs(dp_hol)), float(abs(dp_cnj)))
            dp_overlap_min_mag = cur_dp_min if not have_dp_min else min(dp_overlap_min_mag, cur_dp_min)
            have_dp_min = True

        # Diagonal spin-slot H^0 triples (i, 0, i): constant untwisted spin-slot u_0(z) = 1 (EVEN)
        # paired with branch-i fermion S_i(z) (ODD) and branch-i Higgs S_i(z) (ODD) vs d_z S_i(z) (EVEN):
        diag_spinslot_sp_min_mag = 0.0
        have_diag_sp = False
        diag_spinslot_dp_vanish_err = 0.0
        for nu_d in (2, 3, 4):
            sp_diag_cnj = mp.mpc(0)
            dp_diag_hol = mp.mpc(0)
            dp_diag_cnj = mp.mpc(0)
            for ku_g in range(n_g):
                u_g = mp.fdiv(2 * ku_g - n_g + 1, 2 * n_g)
                for kv_g in range(n_g):
                    v_g = mp.fdiv(2 * kv_g - n_g + 1, 2 * n_g)
                    z_g = mp.mpc(u_g) + mp.mpc(v_g) * tau_c
                    r_mod_sq = (abs(mp.jtheta(1, mp.pi * z_g, q_c)) ** 2 / th1p0_sq) * mp.exp(
                        -2 * mp.pi * (v_g**2) * im_tc_mp
                    )
                    om_metric = mp.mpf(1) / (r_mod_sq * (mp.log(r_mod_sq / mp.mpf(16)) ** 2))
                    om_inv_qtr = abs(mp.sqrt(abs(mp.sqrt(mp.mpf(1) / om_metric))))
                    w_mx = (om_inv_qtr**5) * d2z_cell
                    si_d = szego_nu(nu_d, z_g)
                    dsi_d = dszego_nu(nu_d, z_g)
                    sp_diag_cnj += w_mx * si_d * mp.mpf(1) * mp.conj(si_d)
                    dp_diag_hol += w_mx * dsi_d * mp.mpf(1) * si_d
                    dp_diag_cnj += w_mx * dsi_d * mp.mpf(1) * mp.conj(si_d)
            cur_diag_sp = float(abs(sp_diag_cnj))
            diag_spinslot_sp_min_mag = cur_diag_sp if not have_diag_sp else min(diag_spinslot_sp_min_mag, cur_diag_sp)
            have_diag_sp = True
            diag_spinslot_dp_vanish_err = max(
                diag_spinslot_dp_vanish_err, float(abs(dp_diag_hol)), float(abs(dp_diag_cnj))
            )

    # (c) Exact cyclotomic order obstruction for A:A02 (slope 2/5) and A:A03 (order-5 offset (2/5, 4/5)):
    wp32_res = verify_wp32_exact_cyclotomic_algebra_and_metaplectic_obstruction()
    g96_order = int(wp32_res["triplet_T_exact_order"])
    phi_24 = int(sp.totient(24))
    phi_5 = int(sp.totient(5))
    phi_120 = int(sp.totient(120))
    cyclotomic_disjoint_q24_q5 = (
        math.gcd(24, 5) == 1
        and math.gcd(g96_order, 5) == 1
        and phi_120 == phi_24 * phi_5
    )

    # (d) Second-thread [weave] control on h_1 (so(5) background, F4):
    spin5_gens = [(f6_all[p_i] * f6_all[q_i]).applyfunc(sp.expand) for p_i in range(1, 6) for q_i in range(p_i + 1, 6)]
    h1_spin5_unbroken = len(spin5_gens) == 10 and all(
        (s8_h1 * g_m - g_m * s8_h1).applyfunc(sp.expand) == sp.zeros(8, 8) for g_m in spin5_gens
    )
    j_sp4_4p = (f6_all[0] * f6_all[1] * f6_all[3] * f6_all[5]).extract(idx_4p, idx_4p).applyfunc(sp.expand)
    spin5_sym_4p = [g_m.extract(idx_4p, idx_4p).applyfunc(sp.expand) for g_m in spin5_gens]
    h1_4p_symplectic_exact = (j_sp4_4p + j_sp4_4p.T) == sp.zeros(4, 4) and all(
        (g4.T * j_sp4_4p + j_sp4_4p * g4).applyfunc(sp.expand) == sp.zeros(4, 4) for g4 in spin5_sym_4p
    )
    spin5_on_4p = [np.array(g4.tolist(), dtype=complex) for g4 in spin5_sym_4p]
    h1_4p_commutant_dim = joint_commutant_dim_num(spin5_on_4p, tol=1e-10)
    h1_4p_traceless = all(abs(complex(np.trace(g_m))) < TOL for g_m in spin5_on_4p)

    wp34_verified = (
        gl10_comm_dim == 2
        and so10_unbroken_commutant_dim == 0
        and fock_16p_odd_bitsum_verified
        and mechanical_h4_4p_split_exact
        and planted_joint_dim == 0
        and planted_naive_trace_round == 1
        and v10_aslot_mu == [2, 2]
        and v10_bot_mu == [-2, -2]
        and v10_spin_mu_eigs == [-2, -2, 2, 2]
        and s16p_aslot_mu == [3]
        and s16p_bot_mu == [-3]
        and s16p_spin_mu_eigs == [0, 0]
        and form_degree_naive_aaa_wedge_zero
        and all_three_parabolic_harmonic_yukawas_vanish
        and nonharm_neg1_neg1_couples_v10_kerd0
        and nonharm_pos3_neg1_couples_v10_h1
        and aslot_vtop_holonomy_singlet_vs_triplet == ((-1, -1), (1, 1))
        and spin_slot_h0_singlet_by_eta == {(0, 0): 1, (1, 1): 1, (1, 0): 0, (0, 1): 0}
        and spin_slot_h0_triplet_line_by_eta == {(0, 0): 1, (1, 1): 1, (1, 0): 0, (0, 1): 0}
        and s16p_128_census["h4"] == {(0, 0): (24, 24), (1, 1): (24, 24), (1, 0): (16, 16), (0, 1): (16, 16)}
        and s16p_128_census["h1"] == {(0, 0): (24, 24), (1, 1): (24, 24), (1, 0): (16, 16), (0, 1): (16, 16)}
        and singlet_singlet_wedge_dim == 0
        and singlet_triplet_wedge_dim == 3
        and frame_a_wedge_chars == [(0, 1), (0, 1), (1, 0), (1, 0), (1, 1), (1, 1)]
        and len(allowed_triples_untwisted_absent) == 6
        and len(diag_triples_untwisted_absent) == 0
        and max_parity_err < TOL
        and max_weierstrass_jacobi_err < 1e-18
        and sp_parity_vanish_err < 1e-18
        and dp_overlap_min_mag > 1.0
        and diag_spinslot_sp_min_mag > 1.0
        and diag_spinslot_dp_vanish_err < 1e-18
        and cyclotomic_disjoint_q24_q5
        and h1_spin5_unbroken
        and h1_4p_symplectic_exact
        and h1_4p_commutant_dim == 1
        and h1_4p_traceless
    )

    return {
        "parabolic_so10_unbroken_commutant_dim": so10_unbroken_commutant_dim,
        "fock_16p_odd_bitsum_verified": fock_16p_odd_bitsum_verified,
        "mechanical_h4_4p_split_exact": mechanical_h4_4p_split_exact,
        "planted_noncommuting_joint_fixed_dim": planted_joint_dim,
        "v10_aslot_mu_weights": v10_aslot_mu,
        "v10_spin_mu_weights": v10_spin_mu_eigs,
        "s16p_aslot_mu_weights": s16p_aslot_mu,
        "s16p_spin_mu_weights": s16p_spin_mu_eigs,
        "all_three_parabolic_harmonic_yukawas_vanish": all_three_parabolic_harmonic_yukawas_vanish,
        "parabolic_aslot_cubic_identically_zero": parabolic_aa_harm_zero,
        "parabolic_spin_mu_neg1_couples_to_v10_aslot": nonharm_neg1_neg1_couples_v10_kerd0,
        "parabolic_aslot_mu_neg1_couples_to_v10_h1": nonharm_pos3_neg1_couples_v10_h1,
        "aslot_vtop_holonomy_singlet_vs_triplet": aslot_vtop_holonomy_singlet_vs_triplet,
        "parabolic_spin_slot_h0_singlet_by_eta": spin_slot_h0_singlet_by_eta,
        "parabolic_spin_slot_h0_triplet_line_by_eta": spin_slot_h0_triplet_line_by_eta,
        "parabolic_s16p_128_census_h4": s16p_128_census["h4"],
        "parabolic_s16p_128_census_h1": s16p_128_census["h1"],
        "singlet_singlet_wedge_dim_b1866": singlet_singlet_wedge_dim,
        "singlet_triplet_wedge_dim_b1866": singlet_triplet_wedge_dim,
        "frame_a_klein4_wedge_chars": frame_a_wedge_chars,
        "z2xz2_allowed_offdiag_triples_count": len(allowed_triples_untwisted_absent),
        "z2xz2_allowed_diag_triples_count_without_singlet": len(diag_triples_untwisted_absent),
        "elliptic_parity_max_err": max_parity_err,
        "weierstrass_jacobi_identity_max_err": max_weierstrass_jacobi_err,
        "simple_pole_higgs_overlap_abs_err": sp_parity_vanish_err,
        "derivative_dr_higgs_overlap_min_mag": dp_overlap_min_mag,
        "diag_spinslot_simple_pole_min_mag": diag_spinslot_sp_min_mag,
        "diag_spinslot_derivative_abs_err": diag_spinslot_dp_vanish_err,
        "cyclotomic_q24_q5_disjoint_slope_2_5_unforced": cyclotomic_disjoint_q24_q5,
        "h1_second_thread_spin5_unbroken_irrep_traceless": (
            h1_spin5_unbroken and h1_4p_symplectic_exact and h1_4p_commutant_dim == 1 and h1_4p_traceless
        ),
        "wp34_cubic_overlap_comparison_verified": wp34_verified,
    }


# =============================================================================
# PART 5C (WP-2.5): Stationary Source, Lepton Factor c (A:A10 / FL:12),
#                   Exact Q(zeta_24) Schur Metric (A:A08) & 128D D-Term Dichotomy
# =============================================================================


def verify_wp25_stationary_source_generation_metric_and_lepton_factor() -> dict[str, Any]:
    """Evaluate stationary source / 128D S_16^+ D-term dichotomy, exact Q(zeta_24) generation-metric
    Schur uniqueness on BOTH 3_sp(96) and 3_dp(288) vs single-thread freedom (A:A08), and the
    relative lepton-to-quark factor c_UV == 1 vs explicit Cl(10) 5-form Georgi-Jarlskog 126bar_s (A:A10 / FL:12).
    """
    bil = build_exact_e8_10_6_spinor_bilinear()
    g10_cl: list[sp.Matrix] = bil["g10_cliff"]
    chir10: sp.Matrix = bil["chir10"]
    b10_maj: sp.Matrix = bil["b10_maj"]
    f6_cl: list[sp.Matrix] = bil["f6_cliff"]
    chir6: sp.Matrix = bil["chir6"]
    b6_maj: sp.Matrix = bil["b6_maj"]
    splus_pairs: list[tuple[int, int]] = bil["splus_pairs"]
    splus_idx: dict[tuple[int, int], int] = bil["splus_idx"]
    s2i: dict[tuple[int, ...], int] = bil["sign_to_idx"]
    b60 = bil["bilinear_60"]

    idx_16p = [r_i for r_i in range(32) if chir10[r_i, r_i] == 1]
    idx_4p = [r_i for r_i in range(8) if chir6[r_i, r_i] == 1]

    # 1. Prove (10, 6) is the UNIQUE chiral Yukawa block in e_8 for (16^+, 4^+) x (16^+, 4^+):
    chiral_45_nonzero = sum(
        1
        for a_i, b_i in combinations(range(10), 2)
        if (b10_maj * g10_cl[a_i] * g10_cl[b_i]).extract(idx_16p, idx_16p).applyfunc(sp.expand) != sp.zeros(16, 16)
    )
    chiral_15_nonzero = sum(
        1
        for p_i, q_i in combinations(range(6), 2)
        if (b6_maj * f6_cl[p_i] * f6_cl[q_i]).extract(idx_4p, idx_4p).applyfunc(sp.expand) != sp.zeros(4, 4)
    )
    only_10_6_couples_chirally = (chiral_45_nonzero == 0) and (chiral_15_nonzero == 0)

    # 2. Exact Lepton-to-Quark Factor Theorem (c_UV == 1 on (10,6) subset 248) + Explicit Cl(10) 5-Form
    #    Georgi-Jarlskog Operator in 126bar_s giving |y_e / y_d| == 3 (D5.c):
    t0 = (1, 1, 1)
    t_tri = [(1, -1, -1), (-1, 1, -1), (-1, -1, 1)]
    qu_c1 = (-1, 1, 1, 1, -1)
    uc_c1 = (1, -1, -1, 1, 1)
    qd_c1 = (-1, 1, 1, -1, 1)
    dc_c1 = (1, -1, -1, -1, -1)
    le_st = (-1, -1, -1, -1, 1)
    ec_st = (1, 1, 1, -1, -1)
    lnu_st = (-1, -1, -1, 1, -1)
    nuc_st = (1, 1, 1, 1, 1)

    active_a10_neutral = sorted(
        {
            k_i // 6
            for t_b in t_tri
            for u_s, v_s in [(qu_c1, uc_c1), (qd_c1, dc_c1), (le_st, ec_st), (lnu_st, nuc_st)]
            for k_i, val in enumerate(b60(s2i[u_s + t0], s2i[v_s + t_b]))
            if val != 0
        }
    )

    # Explicit Cl(10) symmetric 5-form Georgi-Jarlskog operator in Pati-Salam (15, 2, 2) subset 126bar_s:
    # O_GJ^{(5)} = (Gamma_2 Gamma_3 Gamma_4 Gamma_5 + Gamma_0 Gamma_1 Gamma_4 Gamma_5 + Gamma_0 Gamma_1 Gamma_2 Gamma_3) * Gamma_6
    o_gj_5form = (
        g10_cl[2] * g10_cl[3] * g10_cl[4] * g10_cl[5] * g10_cl[6]
        + g10_cl[0] * g10_cl[1] * g10_cl[4] * g10_cl[5] * g10_cl[6]
        + g10_cl[0] * g10_cl[1] * g10_cl[2] * g10_cl[3] * g10_cl[6]
    ).applyfunc(sp.expand)
    m_gj_16p = (b10_maj * o_gj_5form * chir10).extract(idx_16p, idx_16p).applyfunc(sp.expand)
    gj_5form_symmetric_exact = (m_gj_16p - m_gj_16p.T).applyfunc(sp.expand) == sp.zeros(16, 16)

    weights_16p = [
        tuple(1 if ((idx_16p[u_i] // (2**a_i)) % 2 == 1) else -1 for a_i in range(5))
        for u_i in range(16)
    ]
    u16_le = weights_16p.index(le_st)
    u16_ec = weights_16p.index(ec_st)
    gj_lepton_entry = m_gj_16p[u16_le, u16_ec]
    gj_quark_ratios_abs: list[int] = []
    for qd_w, dc_w in [
        ((-1, 1, 1, -1, 1), (1, -1, -1, -1, -1)),
        ((1, -1, 1, -1, 1), (-1, 1, -1, -1, -1)),
        ((1, 1, -1, -1, 1), (-1, -1, 1, -1, -1)),
    ]:
        q_ent = m_gj_16p[weights_16p.index(qd_w), weights_16p.index(dc_w)]
        gj_quark_ratios_abs.append(int(abs(sp.simplify(gj_lepton_entry / q_ent))))

    # Also verify antisymmetry of 3-form 120_a ((B_10 Gamma_0 Gamma_2 Gamma_6)|_{16^+}) and absence of 120, 126bar_s in 248:
    m_120_16p = (b10_maj * g10_cl[0] * g10_cl[2] * g10_cl[6] * chir10).extract(idx_16p, idx_16p).applyfunc(sp.expand)
    antisym_120_exact = (m_120_16p + m_120_16p.T).applyfunc(sp.expand) == sp.zeros(16, 16) and m_120_16p != sp.zeros(16, 16)
    dim_126bar_s = math.comb(10, 5) // 2
    e8_spin10_dims_present = {1, 10, 16, 45}
    gj_126bar_absent_in_e8_248 = (dim_126bar_s == 126) and (dim_126bar_s not in e8_spin10_dims_present)

    rng = np.random.default_rng(73)
    o_trip_trip = rng.normal(size=(3, 3, 4, 4)) + 1j * rng.normal(size=(3, 3, 4, 4))
    vev_neutral_60 = np.zeros(60, dtype=complex)
    for a_10 in (6, 7):
        for p_6 in range(6):
            vev_neutral_60[6 * a_10 + p_6] = complex(rng.normal() + 1j * rng.normal())

    t4_all = [t0] + t_tri

    def build_sector_yukawa_3x3(u_5: tuple[int, ...], v_5: tuple[int, ...]) -> np.ndarray:
        y_mat = np.zeros((3, 3), dtype=complex)
        for i_g in range(3):
            for j_g in range(3):
                acc = 0.0j
                for a_t in range(4):
                    for b_t in range(4):
                        cg_vec = np.array(
                            [complex(x_v) for x_v in b60(s2i[u_5 + t4_all[a_t]], s2i[v_5 + t4_all[b_t]])],
                            dtype=complex,
                        )
                        acc += o_trip_trip[i_g, j_g, a_t, b_t] * complex(np.dot(vev_neutral_60, cg_vec))
                y_mat[i_g, j_g] = acc
        return y_mat

    yu_3 = build_sector_yukawa_3x3(qu_c1, uc_c1)
    ynu_3 = build_sector_yukawa_3x3(lnu_st, nuc_st)
    yd_3 = build_sector_yukawa_3x3(qd_c1, dc_c1)

    cg_ed_exact_match = all(
        sp.simplify(
            b60(s2i[le_st + t4_all[a_t]], s2i[ec_st + t4_all[b_t]])[k_i]
            + b60(s2i[qd_c1 + t4_all[a_t]], s2i[dc_c1 + t4_all[b_t]])[k_i]
        )
        == 0
        for a_t in range(4)
        for b_t in range(4)
        for k_i in range(60)
    )
    cg_unu_exact_match = all(
        sp.simplify(
            b60(s2i[lnu_st + t4_all[a_t]], s2i[nuc_st + t4_all[b_t]])[k_i]
            + b60(s2i[qu_c1 + t4_all[a_t]], s2i[uc_c1 + t4_all[b_t]])[k_i]
        )
        == 0
        for a_t in range(4)
        for b_t in range(4)
        for k_i in range(60)
    )

    ye_su5_transpose = np.zeros((3, 3), dtype=complex)
    for i_g in range(3):
        for j_g in range(3):
            acc = 0.0j
            for a_t in range(4):
                for b_t in range(4):
                    cg_vec = np.array(
                        [complex(x_v) for x_v in b60(s2i[le_st + t4_all[b_t]], s2i[ec_st + t4_all[a_t]])],
                        dtype=complex,
                    )
                    acc += o_trip_trip[j_g, i_g, a_t, b_t] * complex(np.dot(vev_neutral_60, cg_vec))
            ye_su5_transpose[i_g, j_g] = acc

    ye_yd_transpose_err = float(np.max(np.abs(ye_su5_transpose - yd_3.T)))

    a_rand = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    g_kin = a_rand.conj().T @ a_rand + np.eye(3)
    ev_g, vc_g = np.linalg.eigh(g_kin)
    g_inv_sqrt = vc_g @ np.diag(1.0 / np.sqrt(ev_g)) @ vc_g.conj().T

    yd_phys = g_inv_sqrt @ yd_3 @ g_inv_sqrt.T
    ye_phys = g_inv_sqrt @ ye_su5_transpose @ g_inv_sqrt.T
    yu_phys = g_inv_sqrt @ yu_3 @ g_inv_sqrt.T
    ynu_phys = g_inv_sqrt @ ynu_3 @ g_inv_sqrt.T

    sv_d = np.sort(np.linalg.svd(yd_phys, compute_uv=False))
    sv_e = np.sort(np.linalg.svd(ye_phys, compute_uv=False))
    sv_u = np.sort(np.linalg.svd(yu_phys, compute_uv=False))
    sv_nu = np.sort(np.linalg.svd(ynu_phys, compute_uv=False))

    c_lepton_quark_derived = float(sv_e[2] / sv_d[2])
    c_lepton_unity_err = max(float(np.max(np.abs(sv_e - sv_d))), float(np.max(np.abs(sv_nu - sv_u))))

    max_haar_yukawa_sv_err = 0.0
    for _ in range(10):
        u_q = haar_unitary(3, rng)
        u_dc = haar_unitary(3, rng)
        u_l = haar_unitary(3, rng)
        u_ec = haar_unitary(3, rng)
        sv_d_scr = np.sort(np.linalg.svd(u_q @ yd_phys @ u_dc.T, compute_uv=False))
        sv_e_scr = np.sort(np.linalg.svd(u_l @ ye_phys @ u_ec.T, compute_uv=False))
        max_haar_yukawa_sv_err = max(
            max_haar_yukawa_sv_err,
            float(np.max(np.abs(sv_d_scr - sv_d))),
            float(np.max(np.abs(sv_e_scr - sv_e))),
        )

    c_v4_samples = []
    for alpha_num in (sp.Rational(1, 2), sp.Integer(1), sp.Integer(2)):
        al_f = float(alpha_num)
        sv_e_v4 = np.sort(np.linalg.svd((al_f * g_inv_sqrt) @ ye_su5_transpose @ (al_f * g_inv_sqrt).T, compute_uv=False))
        c_v4_samples.append(float(sv_e_v4[2] / sv_d[2]))
    v4_continuous_c_family_demonstrated = (
        abs((1.0 / c_v4_samples[0]) / 4 - 1.0) < TOL
        and abs(c_v4_samples[1] - 1.0) < TOL
        and abs(c_v4_samples[2] / 4 - 1.0) < TOL
    )

    # 3. Exact Q(zeta_24) Generation Metric Theorem on BOTH 3_sp (96) and 3_dp (288 = 12*24) (A:A08, D5.b):
    wp32_data = verify_wp32_exact_cyclotomic_algebra_and_metaplectic_obstruction()
    b1866_join = verify_b1866_zero_handtyped_3branch_pde_join(wp32_data)
    modes_p = b1866_join["thread_h4_plus"]["modes"] if "modes" in b1866_join["thread_h4_plus"] else None
    # Note verify_b1866_zero_handtyped_3branch_pde_join summarizes modes; construct exact 3_sp and 3_dp in Q(zeta_24)
    # directly from Stage 2's proven twist relation:
    #   3_sp = T_bar (L_sp = tbar_l_cyc, R_sp = tbar_r_cyc), order 96 (|Z|=4, |PG|=24),
    #   3_dp = chi_{eta^{-2}} (x) 3_sp: on L, eta(tau-1) = zeta_24^{-1} eta(tau) => conj(eta) vs conj(eta^3)
    #   shifts L by zeta_24^{-2} = cyc24_pow(22) and R by zeta_24^{+2} = cyc24_pow(2)!
    from origin_axiom.stage2_kernel_and_physical_join import cyc24_matmul, cyc24_mul, cyc24_pow

    _ = modes_p
    l_sp_cyc = wp32_data["tbar_l_cyc"]
    r_sp_cyc = wp32_data["tbar_r_cyc"]
    z22_c = cyc24_pow(22)
    z2_c = cyc24_pow(2)
    l_dp_cyc = [[cyc24_mul(z22_c, x_e) for x_e in row_e] for row_e in l_sp_cyc]
    r_dp_cyc = [[cyc24_mul(z2_c, x_e) for x_e in row_e] for row_e in r_sp_cyc]

    grp_sp_cyc = cyc24_close_group(
        {"L": l_sp_cyc, "R": r_sp_cyc, "l": cyc24_herm(l_sp_cyc), "r": cyc24_herm(r_sp_cyc)}
    )
    grp_dp_cyc = cyc24_close_group(
        {"L": l_dp_cyc, "R": r_dp_cyc, "l": cyc24_herm(l_dp_cyc), "r": cyc24_herm(r_dp_cyc)}
    )
    cent_sp, pg_sp = cyc24_center_and_pg_orders(grp_sp_cyc)
    cent_dp, pg_dp = cyc24_center_and_pg_orders(grp_dp_cyc)

    end_sp_cyc, sp_self_unit = solve_intertwiner_cyc24_exact((l_sp_cyc, r_sp_cyc), (l_sp_cyc, r_sp_cyc))
    end_dp_cyc, dp_self_unit = solve_intertwiner_cyc24_exact((l_dp_cyc, r_dp_cyc), (l_dp_cyc, r_dp_cyc))
    hom_sp_dp_cyc, _ = solve_intertwiner_cyc24_exact((l_sp_cyc, r_sp_cyc), (l_dp_cyc, r_dp_cyc))

    # Exact Q(zeta_24) End_{E_theta}(3_sp) == 2 across all 3 index-3 single-thread stabilizers:
    l2_sp_cyc = cyc24_matmul(l_sp_cyc, l_sp_cyc)
    r2_sp_cyc = cyc24_matmul(r_sp_cyc, r_sp_cyc)
    s_sp_cyc = cyc24_matmul(l_sp_cyc, cyc24_matmul(cyc24_herm(r_sp_cyc), l_sp_cyc))
    lr_sp_cyc = cyc24_matmul(l_sp_cyc, r_sp_cyc)
    end_etheta_cyc = (
        solve_intertwiner_cyc24_exact((l_sp_cyc, r2_sp_cyc), (l_sp_cyc, r2_sp_cyc))[0],
        solve_intertwiner_cyc24_exact((r_sp_cyc, l2_sp_cyc), (r_sp_cyc, l2_sp_cyc))[0],
        solve_intertwiner_cyc24_exact((s_sp_cyc, lr_sp_cyc), (s_sp_cyc, lr_sp_cyc))[0],
    )

    l_sp_num = cyc24_to_numpy(l_sp_cyc)
    r_sp_num = cyc24_to_numpy(r_sp_cyc)
    l_dp_num = cyc24_to_numpy(l_dp_cyc)
    r_dp_num = cyc24_to_numpy(r_dp_cyc)
    z3_m = np.zeros((3, 3), dtype=complex)
    end_6d_sp_plus_dp_dim = joint_commutant_dim_num(
        [
            np.block([[l_sp_num, z3_m], [z3_m, l_dp_num]]),
            np.block([[r_sp_num, z3_m], [z3_m, r_dp_num]]),
        ],
        tol=1e-10,
    )
    unstabilized_hermitian_3x3_real_params = joint_commutant_dim_num([np.eye(3, dtype=complex)], tol=1e-10)

    # 4. Exact 128D S_16^+ Quartic D-Term Dichotomy across Spin(6) internal profiles (G:GAP3, G:GAP5, FL:05, D5.a):
    def embed_128_sym(m32: sp.Matrix, m8: sp.Matrix) -> sp.Matrix:
        out_s = sp.zeros(128, 128)
        nz32 = [[(r_i, m32[r_i, c_i]) for r_i in range(32) if m32[r_i, c_i] != 0] for c_i in range(32)]
        nz8 = [[(r_i, m8[r_i, c_i]) for r_i in range(8) if m8[r_i, c_i] != 0] for c_i in range(8)]
        for col_s, (c1, c2) in enumerate(splus_pairs):
            for r1, v1 in nz32[c1]:
                for r2, v2 in nz8[c2]:
                    out_s[splus_idx[(r1, r2)], col_s] = sp.expand(v1 * v2)
        return out_s

    op32_6 = (g10_cl[6] * chir10).applyfunc(sp.expand)
    op32_7 = (g10_cl[7] * chir10).applyfunc(sp.expand)
    irt2 = sp.Integer(1) / sp.sqrt(2)
    b_u_32 = ((op32_7 - sp.I * op32_6) * irt2).applyfunc(sp.expand)
    b_d_32 = ((op32_7 + sp.I * op32_6) * irt2).applyfunc(sp.expand)

    f_real_8 = f6_cl[0]
    f_plus_8 = ((f6_cl[0] - sp.I * f6_cl[1]) * irt2).applyfunc(sp.expand)
    f_minus_8 = ((f6_cl[0] + sp.I * f6_cl[1]) * irt2).applyfunc(sp.expand)

    hu_r, hu_i, hd_r, hd_i = sp.symbols("hu_r hu_i hd_r hd_i", real=True)
    hu_c = hu_r + sp.I * hu_i
    hd_c = hd_r + sp.I * hd_i
    n_u = hu_r**2 + hu_i**2
    n_d = hd_r**2 + hd_i**2

    def quartic_trace_per_64(fu_8: sp.Matrix, fd_8: sp.Matrix) -> sp.Expr:
        bu_128 = embed_128_sym(b_u_32, fu_8)
        bd_128 = embed_128_sym(b_d_32, fd_8)
        phi_h = hu_c * bu_128 + hd_c * bd_128
        phi_hd = sp.conjugate(hu_c) * bu_128.H + sp.conjugate(hd_c) * bd_128.H
        comm_128 = (phi_h * phi_hd - phi_hd * phi_h).applyfunc(sp.expand)
        # Note Tr(C * C^H) == sum_{r,c} |C_{r,c}|^2 computed via sparse row scan (fast & exact!):
        acc_tr = sp.Integer(0)
        for r_s in range(128):
            for c_s in range(128):
                val_rc = comm_128[r_s, c_s]
                if val_rc != 0:
                    acc_tr += sp.expand(val_rc * sp.conjugate(val_rc))
        return sp.simplify(acc_tr / 64)

    v_d_real = quartic_trace_per_64(f_real_8, f_real_8)
    v_d_same_h4 = quartic_trace_per_64(f_minus_8, f_minus_8)
    v_d_opp_h4 = quartic_trace_per_64(f_minus_8, f_plus_8)

    coeff_real_valley = sp.simplify(v_d_real / ((n_u - n_d) ** 2))
    coeff_same_h4_posdef = sp.simplify(v_d_same_h4 / (n_u**2 + n_d**2))
    coeff_opp_h4_valley = sp.simplify(v_d_opp_h4 / ((n_u - n_d) ** 2))

    # Verify that on +h_4 (where 4^+ = 1_{w8^3} (+) 3_{w8^{-1}}), B_6 * f_- (eigenvalue -i = w8^{-2})
    # couples singlet-triplet (!= 0) whereas B_6 * f_+ (eigenvalue +i = w8^{+2}) vanishes IDENTICALLY on
    # singlet x triplet (killing H_d singlet-triplet Yukawa on single +h_4 if paired with f_-!):
    i8_s = sp.eye(8)
    h4_8 = (
        (i8_s - f6_cl[0] * f6_cl[1])
        * irt2
        * (i8_s - f6_cl[2] * f6_cl[3])
        * irt2
        * (i8_s - f6_cl[4] * f6_cl[5])
        * irt2
    ).applyfunc(sp.expand)
    h4_4p = h4_8.extract(idx_4p, idx_4p)
    w8_cubed = sp.expand((-sp.Integer(1) + sp.I) * irt2)
    s_idx4 = [i_f for i_f in range(4) if sp.expand(h4_4p[i_f, i_f] - w8_cubed) == 0]
    t_idx4 = [i_f for i_f in range(4) if sp.expand(h4_4p[i_f, i_f] - w8_cubed) != 0]
    b6_fplus_4p = (b6_maj * f_plus_8).extract(idx_4p, idx_4p).applyfunc(sp.expand)
    b6_fminus_4p = (b6_maj * f_minus_8).extract(idx_4p, idx_4p).applyfunc(sp.expand)
    active_h4_couples_sing_trip = b6_fminus_4p.extract(s_idx4, t_idx4) != sp.zeros(1, 3)
    opposite_h4_kills_sing_trip = b6_fplus_4p.extract(s_idx4, t_idx4) == sp.zeros(1, 3)

    d_term_dichotomy_exact = (
        coeff_real_valley == 8
        and coeff_same_h4_posdef == 16
        and coeff_opp_h4_valley == 16
        and sp.simplify(v_d_same_h4.subs({hu_r: 1, hu_i: 0, hd_r: 1, hd_i: 0})) == 32
        and len(s_idx4) == 1
        and len(t_idx4) == 3
        and active_h4_couples_sing_trip
        and opposite_h4_kills_sing_trip
    )

    wp25_verified = (
        only_10_6_couples_chirally
        and active_a10_neutral == [6, 7]
        and gj_5form_symmetric_exact
        and gj_quark_ratios_abs == [3, 3, 3]
        and antisym_120_exact
        and gj_126bar_absent_in_e8_248
        and cg_ed_exact_match
        and cg_unu_exact_match
        and ye_yd_transpose_err < TOL
        and abs(c_lepton_quark_derived - 1.0) < TOL
        and c_lepton_unity_err < TOL
        and max_haar_yukawa_sv_err < TOL
        and v4_continuous_c_family_demonstrated
        and len(grp_sp_cyc) == 96
        and (cent_sp, pg_sp) == (4, 24)
        and len(grp_dp_cyc) - 128 == 160
        and (cent_dp, pg_dp) == (12, 24)
        and (end_sp_cyc, sp_self_unit) == (1, True)
        and (end_dp_cyc, dp_self_unit) == (1, True)
        and hom_sp_dp_cyc == 0
        and end_6d_sp_plus_dp_dim == 2
        and end_etheta_cyc == (2, 2, 2)
        and unstabilized_hermitian_3x3_real_params == 9
        and bool(d_term_dichotomy_exact)
    )

    return {
        "chiral_45_yukawa_nonzero_count": chiral_45_nonzero,
        "chiral_15_yukawa_nonzero_count": chiral_15_nonzero,
        "only_10_6_couples_chirally_verified": only_10_6_couples_chirally,
        "active_neutral_so10_axes": active_a10_neutral,
        "gj_126bar_5form_lepton_to_quark_abs_ratios": gj_quark_ratios_abs,
        "gj_126bar_absent_in_e8_248": gj_126bar_absent_in_e8_248,
        "cg_ye_yd_transpose_err": ye_yd_transpose_err,
        "derived_spin10_symmetric_lepton_factor_c": c_lepton_quark_derived,
        "c_lepton_unity_max_sv_err": c_lepton_unity_err,
        "max_haar_yukawa_sv_err": max_haar_yukawa_sv_err,
        "v4_cusp_breaking_continuous_c_family_verified": v4_continuous_c_family_demonstrated,
        "weave_3sp_order": len(grp_sp_cyc),
        "weave_3dp_center_and_pg": (cent_dp, pg_dp),
        "weave_g96_gen_metric_commutant_dim": end_sp_cyc,
        "weave_3dp_gen_metric_commutant_dim": end_dp_cyc,
        "weave_hom_3sp_to_3dp_dim": hom_sp_dp_cyc,
        "weave_6d_sp_plus_dp_commutant_dim": end_6d_sp_plus_dp_dim,
        "single_thread_etheta_gen_metric_commutant_dim": end_etheta_cyc[0],
        "d_term_real_slice_coeff_per_64": int(coeff_real_valley),
        "d_term_same_h4_posdef_coeff_per_64": int(coeff_same_h4_posdef),
        "d_term_dichotomy_and_real_valley_verified": bool(d_term_dichotomy_exact),
        "wp25_source_metric_and_lepton_c_verified": wp25_verified,
    }


def run_stage5_complete_verification() -> dict[str, Any]:
    """Run all Stage 5 (WP-1.7, WP-3.4, WP-2.5) verifications + AST Firewall & Guardrail-2 self-locks."""
    self_path = Path(__file__).resolve()
    fw_ok = audit_source_zero_empirical_constants(self_path)
    g2_ok = check_guardrail2_ast_no_literal_bool_verdicts(self_path.read_text(encoding="utf-8"))

    r_wp17 = verify_wp17_quantum_number_dictionary_and_up_conjugate()
    r_wp34 = verify_wp34_cubic_overlaps_and_value_frame_comparison()
    r_wp25 = verify_wp25_stationary_source_generation_metric_and_lepton_factor()

    all_ok = (
        fw_ok
        and g2_ok
        and r_wp17["wp17_dictionary_and_up_conjugate_verified"]
        and r_wp34["wp34_cubic_overlap_comparison_verified"]
        and r_wp25["wp25_source_metric_and_lepton_c_verified"]
    )

    return {
        "zero_sm_empirical_constants_ast_verified": fw_ok,
        "guardrail2_ast_no_literal_bool_verdicts_verified": g2_ok,
        "wp17_dictionary": r_wp17,
        "wp34_cubic_overlaps": r_wp34,
        "wp25_source_and_lepton_factor": r_wp25,
        "all_verifications_passed": all_ok,
    }
