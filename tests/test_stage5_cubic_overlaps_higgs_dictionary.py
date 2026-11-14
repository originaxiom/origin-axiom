"""Zero-trust pytest counterchecks & AST locks for Stage 5 (B1861 WP-1.7, WP-3.4, WP-2.5):
Quantum-Number Dictionary, Curved Trilinear Gauge-Yukawa Overlaps vs Four-Channel Value Frame,
Stationary Source & Relative Lepton-to-Quark Normalization Factor c.

Enforces Guardrails 1-6 and Anti-Shortcut Locks F1-F6:
- Strict 0-of-19 empirical data firewall & Guardrail-2 AST locks on both producer and test suite.
- Guardrail 6 zero-trust independence: constructs independent Pauli-Kronecker Cl(10)xCl(6) Lie
  centralizers, mechanical Clifford Z_4 glue kernel across all 5 blocks of 248, explicit w_{SU(2)_R},
  45-generator Spin(10)|_{16^+} & full SM joint commutants (6 with Y_GG, 10 without), full SU(2)_L
  eps_{ab} doublet contractions, independent parabolic Koszul harmonic mu-weights & harmonic bilinear
  vanishing & 128D parabolic cohomology census on h_4 and h_1, independent 35-digit mpmath curved
  cusp overlaps at second modulus tau_alt with |eta(tau)|^4, true orthonormal exponents, SL(2, Z)
  T & S invariance, analytical Riemann theta triple-product agreement, independent (10,6) Yukawa
  canonical normalization Y_phys = (G_L^{-1/2})^T Y G_R^{-1/2} with pre-normalization Haar U(3)^6
  scrambling invariance + wrong-transpose negative control, Cl(10) 5-form 126bar_s Georgi-Jarlskog
  operator, Weil Sym^2 commutants for 3_sp(96) & 3_dp(288), and 128D S_16^+ quartic D-term dichotomy.
"""
from __future__ import annotations

from itertools import combinations
import math
from pathlib import Path
from typing import Any

import mpmath as mp
import numpy as np
import pytest
import sympy as sp

from origin_axiom.stage1_curved_action_cusp_orbit import (
    TOL,
    audit_source_zero_empirical_constants,
    check_guardrail2_ast_no_literal_bool_verdicts,
    haar_unitary,
    joint_commutant_dim_num,
)
from origin_axiom.stage5_cubic_overlaps_higgs_dictionary import (
    joint_fixed_subspace_dim_num,
    run_stage5_complete_verification,
)


ROOT = Path(__file__).resolve().parents[1]
STAGE5_SRC = ROOT / "src" / "origin_axiom" / "stage5_cubic_overlaps_higgs_dictionary.py"
TEST5_SRC = Path(__file__).resolve()


@pytest.fixture(scope="module")
def stage5_results() -> dict[str, Any]:
    return run_stage5_complete_verification()


def test_stage5_firewall_and_guardrail2_ast_locks(stage5_results: dict[str, Any]) -> None:
    indep_fw_prod = audit_source_zero_empirical_constants(STAGE5_SRC)
    indep_fw_test = audit_source_zero_empirical_constants(TEST5_SRC)
    indep_g2_prod = check_guardrail2_ast_no_literal_bool_verdicts(STAGE5_SRC.read_text(encoding="utf-8"))
    indep_g2_test = check_guardrail2_ast_no_literal_bool_verdicts(TEST5_SRC.read_text(encoding="utf-8"))
    assert indep_fw_prod and indep_fw_test and indep_g2_prod and indep_g2_test
    assert stage5_results["zero_sm_empirical_constants_ast_verified"] == indep_fw_prod
    assert stage5_results["guardrail2_ast_no_literal_bool_verdicts_verified"] == indep_g2_prod
    assert stage5_results["all_verifications_passed"] == (indep_fw_prod and indep_g2_prod)


def test_wp17_zero_trust_spin10_centralizers_z4_glue_and_up_conjugate(stage5_results: dict[str, Any]) -> None:
    wp17 = stage5_results["wp17_dictionary"]
    i2 = sp.eye(2)
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])

    def kron_list(mats: list[sp.Matrix]) -> sp.Matrix:
        acc = mats[0]
        for m_k in mats[1:]:
            acc = sp.kronecker_product(acc, m_k)
        return acc

    gammas_10: list[sp.Matrix] = []
    for k_ax in range(5):
        prefix = [sz] * k_ax
        suffix = [i2] * (4 - k_ax)
        gammas_10.append(kron_list(prefix + [sx] + suffix))
        gammas_10.append(kron_list(prefix + [sy] + suffix))

    gammas_6: list[sp.Matrix] = []
    for k_ax in range(3):
        prefix6 = [sz] * k_ax
        suffix6 = [i2] * (2 - k_ax)
        gammas_6.append(kron_list(prefix6 + [sx] + suffix6))
        gammas_6.append(kron_list(prefix6 + [sy] + suffix6))

    om10_ind = sp.eye(32)
    for g_m in gammas_10:
        om10_ind = (om10_ind * g_m).applyfunc(sp.expand)
    chir10_unit = (-sp.I * om10_ind).applyfunc(sp.expand)
    idx_16p = [r_i for r_i in range(32) if chir10_unit[r_i, r_i] == 1]
    idx_16m = [r_i for r_i in range(32) if chir10_unit[r_i, r_i] == -1]
    assert len(idx_16p) == 16 and len(idx_16m) == 16

    om6_ind = sp.eye(8)
    for f_m in gammas_6:
        om6_ind = (om6_ind * f_m).applyfunc(sp.expand)
    chir6_unit = (sp.I * om6_ind).applyfunc(sp.expand)
    idx_4p = [r_i for r_i in range(8) if chir6_unit[r_i, r_i] == 1]
    idx_4m = [r_i for r_i in range(8) if chir6_unit[r_i, r_i] == -1]
    assert len(idx_4p) == 4 and len(idx_4m) == 4

    # 1. Independent 45D so(10, Q) centralizer verification:
    def e10_ab(a_i: int, b_i: int) -> sp.Matrix:
        mat_el = sp.zeros(10, 10)
        mat_el[a_i, b_i] = 1
        mat_el[b_i, a_i] = -1
        return mat_el

    def coords45(m10: sp.Matrix) -> list[sp.Rational]:
        out_c: list[sp.Rational] = []
        for a_i in range(10):
            for b_i in range(a_i + 1, 10):
                out_c.append(sp.Rational(m10[a_i, b_i]))
        return out_c

    def so10_from_col(col_v: sp.Matrix) -> sp.Matrix:
        acc_m = sp.zeros(10, 10)
        idx_p = 0
        for a_i in range(10):
            for b_i in range(a_i + 1, 10):
                c_val = col_v[idx_p, 0]
                if c_val != 0:
                    acc_m = acc_m + c_val * e10_ab(a_i, b_i)
                idx_p = idx_p + 1
        return acc_m

    def lin_comb_col(col_v: sp.Matrix, mats: list[sp.Matrix], dim_n: int) -> sp.Matrix:
        acc_m = sp.zeros(dim_n, dim_n)
        for idx_m, m_cur in enumerate(mats):
            c_val = col_v[idx_m, 0]
            if c_val != 0:
                acc_m = acc_m + c_val * m_cur
        return acc_m

    j10 = sp.zeros(10, 10)
    for ax in range(5):
        j10[2 * ax, 2 * ax + 1] = -1
        j10[2 * ax + 1, 2 * ax] = 1
    u5_cols = []
    for a_i in range(10):
        for b_i in range(a_i + 1, 10):
            x_m = e10_ab(a_i, b_i)
            u5_cols.append(coords45(x_m * j10 - j10 * x_m))
    u5_rows = sp.Matrix(u5_cols).T
    u5_ns = u5_rows.nullspace()
    assert len(u5_ns) == 25
    u5_mats = [so10_from_col(v_u) for v_u in u5_ns]

    c_off = []
    w_off = []
    for a_i in range(10):
        for b_i in range(a_i + 1, 10):
            row_ab = [u_m[a_i, b_i] for u_m in u5_mats]
            if a_i >= 6 or b_i >= 6:
                c_off.append(row_ab)
            if a_i < 6 or b_i < 6:
                w_off.append(row_ab)
    tr_r = [int((j10 * u_m).trace()) for u_m in u5_mats]
    su3_10 = [lin_comb_col(v_s, u5_mats, 10) for v_s in sp.Matrix(c_off + [tr_r]).nullspace()]
    su2_10 = [lin_comb_col(v_s, u5_mats, 10) for v_s in sp.Matrix(w_off + [tr_r]).nullspace()]
    assert len(su3_10) == 8 and len(su2_10) == 3

    z_eqs = []
    for g_sm in (su3_10 + su2_10):
        ad_cols = []
        for a_i in range(10):
            for b_i in range(a_i + 1, 10):
                x_m = e10_ab(a_i, b_i)
                ad_cols.append(coords45(x_m * g_sm - g_sm * x_m))
        z_eqs.extend(list(sp.Matrix(ad_cols).T.tolist()))
    z_so10_ns = sp.Matrix(z_eqs).nullspace()
    z_u5_ns = sp.Matrix(z_eqs + list(u5_rows.tolist())).nullspace()
    assert len(z_so10_ns) == 4 and len(z_u5_ns) == 2
    assert wp17["so10_centralizer_dim"] == len(z_so10_ns)
    assert wp17["u5_centralizer_dim"] == len(z_u5_ns)

    z_so10_mats = [so10_from_col(v_z) for v_z in z_so10_ns]
    indep_z_derived = int(
        sp.Matrix(
            [
                coords45(z_so10_mats[p_i] * z_so10_mats[q_i] - z_so10_mats[q_i] * z_so10_mats[p_i])
                for p_i, q_i in combinations(range(4), 2)
            ]
        ).rank()
    )
    assert indep_z_derived == 3
    assert wp17["so10_centralizer_derived_dim"] == indep_z_derived

    # 2. Independent Pauli-Kronecker hypercharge dichotomy, explicit w_{SU(2)_R}, mechanical Z_4 glue
    #    kernel across ALL 5 blocks of 248, 45-generator Spin(10)|_{16^+} commutant, and full SM commutants:
    def spin16_ind(m10: sp.Matrix) -> sp.Matrix:
        acc_s = sp.zeros(16, 16)
        for a_i in range(10):
            for b_i in range(a_i + 1, 10):
                c_ab = sp.Rational(m10[a_i, b_i])
                if c_ab != 0:
                    gen_ab = (sp.Rational(1, 2) * gammas_10[a_i] * gammas_10[b_i]).extract(idx_16p, idx_16p)
                    acc_s = acc_s + c_ab * gen_ab
        return acc_s.applyfunc(sp.expand)

    h_cartan = [
        (-sp.I * sp.Rational(1, 2) * gammas_10[2 * a_i] * gammas_10[2 * a_i + 1]).extract(idx_16p, idx_16p)
        for a_i in range(5)
    ]
    weights_16 = [tuple(int(2 * h_cartan[a_i][u_i, u_i]) for a_i in range(5)) for u_i in range(16)]
    assert all(w[0] * w[1] * w[2] * w[3] * w[4] == 1 for w in weights_16)

    found_ab: list[tuple[sp.Rational, sp.Rational]] = []
    for alpha_v in (sp.Rational(1, 6), sp.Rational(-1, 6)):
        for which_zero in (1, -1):
            beta_v = sp.Rational(-3, 2) * alpha_v * which_zero
            spec = sorted(abs(alpha_v * (w[0] + w[1] + w[2]) + beta_v * (w[3] + w[4])) for w in weights_16)
            expected_spec = sorted(
                [sp.Integer(0), sp.Integer(1)]
                + [sp.Rational(1, 2)] * 2
                + [sp.Rational(1, 3)] * 3
                + [sp.Rational(2, 3)] * 3
                + [sp.Rational(1, 6)] * 6
            )
            if spec == expected_spec:
                found_ab.append((alpha_v, beta_v))
    assert len(found_ab) == 4
    assert wp17["hypercharge_solutions_count"] == len(found_ab)

    # Independent explicit w_{SU(2)_R} in Pauli-Kronecker Cl(10)|_{16^+}:
    su3_16_sp = [spin16_ind(g_m) for g_m in su3_10]
    su2_16_sp = [spin16_ind(g_m) for g_m in su2_10]
    q_chi_ind = (-2 * (h_cartan[0] + h_cartan[1] + h_cartan[2] + h_cartan[3] + h_cartan[4])).applyfunc(sp.expand)
    y_gg_ind = (
        -sp.Rational(1, 3) * (h_cartan[0] + h_cartan[1] + h_cartan[2])
        + sp.Rational(1, 2) * (h_cartan[3] + h_cartan[4])
    ).applyfunc(sp.expand)
    y_flip_ind = (-sp.Rational(1, 5) * y_gg_ind + sp.Rational(1, 5) * q_chi_ind).applyfunc(sp.expand)

    tp_su2r_ind = (
        (gammas_10[6] - sp.I * gammas_10[7]) * (gammas_10[8] - sp.I * gammas_10[9]) / 4
    ).extract(idx_16p, idx_16p)
    gen_su2r_ind = (tp_su2r_ind - tp_su2r_ind.H).applyfunc(sp.expand)
    w_su2r_ind = (sp.eye(16) + gen_su2r_ind + gen_su2r_ind * gen_su2r_ind).applyfunc(sp.expand)
    indep_weyl_conj = (
        (w_su2r_ind * w_su2r_ind.H - sp.eye(16)).applyfunc(sp.expand) == sp.zeros(16, 16)
        and sp.simplify(w_su2r_ind.det()) == 1
        and all(
            (w_su2r_ind * g_m - g_m * w_su2r_ind).applyfunc(sp.expand) == sp.zeros(16, 16)
            for g_m in (su3_16_sp + su2_16_sp)
        )
        and (w_su2r_ind * y_gg_ind * w_su2r_ind.H - y_flip_ind).applyfunc(sp.expand) == sp.zeros(16, 16)
    )
    indep_su5_breaks = (w_su2r_ind * q_chi_ind - q_chi_ind * w_su2r_ind).applyfunc(sp.expand) != sp.zeros(16, 16)
    assert indep_weyl_conj and indep_su5_breaks
    assert wp17["weyl_su2r_conjugates_gg_and_flipped"] == indep_weyl_conj
    assert wp17["su5_u1_breaks_gg_flipped_equivalence"] == indep_su5_breaks

    # Independent mechanical Clifford Z_4 glue kernel across ALL 5 blocks of 248:
    z10_pows = [(om10_ind**k10).applyfunc(sp.expand) for k10 in range(4)]
    z6_pows = [(om6_ind**k6).applyfunc(sp.expand) for k6 in range(4)]
    g10_pconj = [
        [(z10_pows[k10] * gammas_10[a_i] * z10_pows[k10].H).applyfunc(sp.expand) for a_i in range(10)]
        for k10 in range(4)
    ]
    f6_pconj = [
        [(z6_pows[k6] * gammas_6[p_i] * z6_pows[k6].H).applyfunc(sp.expand) for p_i in range(6)]
        for k6 in range(4)
    ]
    adj45_ok = [
        all(
            (z10_pows[k10] * gammas_10[a_i] * gammas_10[b_i] * z10_pows[k10].H - gammas_10[a_i] * gammas_10[b_i]).applyfunc(sp.expand)
            == sp.zeros(32, 32)
            for a_i, b_i in combinations(range(10), 2)
        )
        for k10 in range(4)
    ]
    adj15_ok = [
        all(
            (z6_pows[k6] * gammas_6[p_i] * gammas_6[q_i] * z6_pows[k6].H - gammas_6[p_i] * gammas_6[q_i]).applyfunc(sp.expand)
            == sp.zeros(8, 8)
            for p_i, q_i in combinations(range(6), 2)
        )
        for k6 in range(4)
    ]
    indep_z4_kernel: list[tuple[int, int]] = []
    for k10 in range(4):
        z10_16p = z10_pows[k10].extract(idx_16p, idx_16p)
        z10_16m = z10_pows[k10].extract(idx_16m, idx_16m)
        for k6 in range(4):
            z6_4p = z6_pows[k6].extract(idx_4p, idx_4p)
            z6_4m = z6_pows[k6].extract(idx_4m, idx_4m)
            ok_sp_p = sp.kronecker_product(z10_16p, z6_4p).applyfunc(sp.expand) == sp.eye(64)
            ok_sp_m = sp.kronecker_product(z10_16m, z6_4m).applyfunc(sp.expand) == sp.eye(64)
            ok_v_10_6 = all(
                (f6_pconj[k6][p_i][r6, c6] * g10_pconj[k10][a_i]).applyfunc(sp.expand)
                == (gammas_6[p_i][r6, c6] * gammas_10[a_i]).applyfunc(sp.expand)
                for a_i in range(10)
                for p_i in range(6)
                for r6 in range(8)
                for c6 in range(8)
                if f6_pconj[k6][p_i][r6, c6] != 0 or gammas_6[p_i][r6, c6] != 0
            )
            if ok_sp_p and ok_sp_m and ok_v_10_6 and adj45_ok[k10] and adj15_ok[k6]:
                indep_z4_kernel.append((k10, k6))
    assert indep_z4_kernel == [(0, 0), (1, 1), (2, 2), (3, 3)]
    assert wp17["z4_glue_kernel_order"] == len(indep_z4_kernel)

    # Independent 45-generator Spin(10)|_{16^+} commutant (== 1) and SM joint commutants (6 vs 10):
    spin10_45_ind = [
        np.array(((sp.Rational(1, 2) * gammas_10[a_i] * gammas_10[b_i]).extract(idx_16p, idx_16p)).tolist(), dtype=complex)
        for a_i, b_i in combinations(range(10), 2)
    ]
    sm16_indep = [np.array(g_m.tolist(), dtype=complex) for g_m in (su3_16_sp + su2_16_sp)]
    y_gg_np = np.array(y_gg_ind.tolist(), dtype=complex)
    indep_spin10_comm = joint_commutant_dim_num(spin10_45_ind, tol=1e-10)
    indep_sm_nonab_comm = joint_commutant_dim_num(sm16_indep, tol=1e-10)
    indep_sm_full_comm = joint_commutant_dim_num(sm16_indep + [y_gg_np], tol=1e-10)
    assert indep_spin10_comm == 1
    assert indep_sm_nonab_comm == 10
    assert indep_sm_full_comm == 6
    assert wp17["spin10_16p_commutant_dim"] == indep_spin10_comm
    assert wp17["sm_nonabelian_commutant_dim_16"] == indep_sm_nonab_comm
    assert wp17["sm_full_commutant_dim_16"] == indep_sm_full_comm
    assert wp17["shared_16_4_sector_carrier_derived"] == (indep_spin10_comm == 1 and indep_sm_full_comm == 6)

    b10 = kron_list([sy, sx, sy, sx, sy])
    c10_vecs = [(b10 * g_m * chir10_unit).extract(idx_16p, idx_16p).applyfunc(sp.expand) for g_m in gammas_10]
    for m_v in c10_vecs:
        assert (m_v - m_v.T).applyfunc(sp.expand) == sp.zeros(16, 16)

    u_qu = weights_16.index((1, 1, -1, 1, -1))
    u_qd = weights_16.index((1, 1, -1, -1, 1))
    u_uc = weights_16.index((-1, -1, 1, 1, 1))
    u_dc = weights_16.index((-1, -1, 1, -1, -1))
    p6, p7, p8, p9 = sp.symbols("p6 p7 p8 p9", real=True)

    def c10_ew(u_a: int, u_b: int) -> sp.Expr:
        return sp.expand(
            p6 * c10_vecs[6][u_a, u_b]
            + p7 * c10_vecs[7][u_a, u_b]
            + p8 * c10_vecs[8][u_a, u_b]
            + p9 * c10_vecs[9][u_a, u_b]
        )

    y_uu = c10_ew(u_qu, u_uc)
    y_du = c10_ew(u_qd, u_uc)
    y_ud = c10_ew(u_qu, u_dc)
    y_dd = c10_ew(u_qd, u_dc)
    r_00 = sp.simplify(y_dd / sp.conjugate(y_uu))
    r_01 = sp.simplify(y_ud / sp.conjugate(y_du))
    assert sp.simplify(r_00 * sp.conjugate(r_00) - 1) == 0
    assert sp.simplify(r_01 + r_00) == 0

    # Independent 16D gauge-allowed SU(3)_C x SU(2)_L x U(1)_Y Haar basis scrambling (< 1e-12):
    sm16_full_gens = sm16_indep + [1.0j * y_gg_np]
    rng_17 = np.random.default_rng(37)
    k16_np = np.array(c10_vecs[6].tolist(), dtype=complex)
    sv0_16 = np.sort(np.linalg.svd(k16_np, compute_uv=False))
    for _ in range(8):
        th_v = rng_17.normal(size=len(sm16_full_gens))
        ah_m = sum(th_v[i_g] * sm16_full_gens[i_g] for i_g in range(len(sm16_full_gens)))
        ev_a, vc_a = np.linalg.eigh(-1.0j * ah_m)
        u_g = vc_a @ np.diag(np.exp(1.0j * ev_a)) @ vc_a.conj().T
        sv_scr = np.sort(np.linalg.svd(u_g @ k16_np @ u_g.T, compute_uv=False))
        assert float(np.max(np.abs(sv_scr - sv0_16))) < TOL


def test_wp34_zero_trust_parabolic_selection_curved_cusp_weierstrass_and_q24_q5(
    stage5_results: dict[str, Any],
) -> None:
    wp34 = stage5_results["wp34_cubic_overlaps"]

    # 1. Independent Pauli-Kronecker Cl(10) x Cl(6) construction of parabolic Koszul harmonic mu-weights,
    #    harmonic Yukawa vanishing, h_4 1 (+) 3 split, wedge dims 0 vs 3, and 128D parabolic census:
    i2 = sp.eye(2)
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])

    def kron_pk(ms: list[sp.Matrix]) -> sp.Matrix:
        out_m = ms[0]
        for nxt_m in ms[1:]:
            out_m = sp.kronecker_product(out_m, nxt_m)
        return out_m

    gammas_10 = []
    for k_i in range(5):
        gammas_10.append(kron_pk([sz] * k_i + [sx] + [i2] * (4 - k_i)))
        gammas_10.append(kron_pk([sz] * k_i + [sy] + [i2] * (4 - k_i)))
    cr_pk = [((gammas_10[2 * k_i] - sp.I * gammas_10[2 * k_i + 1]) / 2).applyfunc(sp.expand) for k_i in range(5)]
    an_pk = [((gammas_10[2 * k_i] + sp.I * gammas_10[2 * k_i + 1]) / 2).applyfunc(sp.expand) for k_i in range(5)]

    om10_pk = sp.eye(32)
    b10_pk = sp.eye(32)
    for k_i in range(5):
        om10_pk = (om10_pk * gammas_10[2 * k_i] * gammas_10[2 * k_i + 1]).applyfunc(sp.expand)
        b10_pk = (b10_pk * gammas_10[2 * k_i]).applyfunc(sp.expand)
    chir10_pk = (sp.I * om10_pk).applyfunc(sp.expand)
    idx16p = [r_i for r_i in range(32) if chir10_pk[r_i, r_i] == 1]
    idx16m = [r_i for r_i in range(32) if chir10_pk[r_i, r_i] == -1]

    f6_pk = []
    for k_i in range(3):
        f6_pk.append(kron_pk([sz] * k_i + [sx] + [i2] * (2 - k_i)))
        f6_pk.append(kron_pk([sz] * k_i + [sy] + [i2] * (2 - k_i)))
    om6_pk = f6_pk[0] * f6_pk[1] * f6_pk[2] * f6_pk[3] * f6_pk[4] * f6_pk[5]
    chir6_pk = (-sp.I * om6_pk).applyfunc(sp.expand)
    idx4p = [r_i for r_i in range(8) if chir6_pk[r_i, r_i] == 1]
    idx4m = [r_i for r_i in range(8) if chir6_pk[r_i, r_i] == -1]
    splus_pk = [(r10, r6) for r10 in range(32) for r6 in range(8) if sp.expand(om10_pk[r10, r10] * om6_pk[r6, r6]) == 1]
    splus_pk_idx = {pt: idx_s for idx_s, pt in enumerate(splus_pk)}

    indep_odd_bitsum = all(sum((r_i // (2**b_i)) % 2 for b_i in range(5)) % 2 == 1 for r_i in idx16p) and (
        set(splus_pk) == {(r10, r6) for r10 in idx16p for r6 in idx4p} | {(r10, r6) for r10 in idx16m for r6 in idx4m}
    )
    assert indep_odd_bitsum
    assert wp34["fock_16p_odd_bitsum_verified"] == indep_odd_bitsum

    irt2 = sp.Integer(1) / sp.sqrt(2)
    rt6 = sp.sqrt(6)
    rt10 = sp.sqrt(10)
    e5 = sp.zeros(5, 5)
    for j_i, c_v in enumerate((sp.Integer(2), rt6, rt6, sp.Integer(2))):
        e5[j_i + 1, j_i] = c_v
    j5 = sp.zeros(5, 5)
    for j_i, c_v in enumerate((1, -1, 1, -1, 1)):
        j5[j_i, 4 - j_i] = c_v
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
    mu10 = (((ep10 * ep10.H - ep10.H * ep10) + (em10 * em10.H - em10.H * em10)) / 2).applyfunc(sp.expand)

    def spin32_pk(m10: sp.Matrix) -> sp.Matrix:
        out_s = -sp.Rational(1, 2) * sum(m10[i_k, i_k] for i_k in range(5)) * sp.eye(32)
        for i_k in range(5):
            for j_k in range(5):
                if m10[i_k, j_k] != 0:
                    out_s += m10[i_k, j_k] * (cr_pk[i_k] * an_pk[j_k])
                if m10[i_k, j_k + 5] != 0:
                    out_s += sp.Rational(1, 2) * m10[i_k, j_k + 5] * (cr_pk[i_k] * cr_pk[j_k])
                if m10[i_k + 5, j_k] != 0:
                    out_s += sp.Rational(1, 2) * m10[i_k + 5, j_k] * (an_pk[i_k] * an_pk[j_k])
        return out_s.applyfunc(sp.expand)

    e16 = spin32_pk(e10).extract(idx16p, idx16p)
    g16 = spin32_pk(g10).extract(idx16p, idx16p)
    mu16 = spin32_pk(mu10).extract(idx16p, idx16p)

    def indep_mu_eigs(vecs: list[sp.Matrix], mu_m: sp.Matrix) -> list[int]:
        n_v = len(vecs)
        g_mat = sp.Matrix([[sp.simplify((vecs[r_i].H * mu_m * vecs[c_i])[0, 0]) for c_i in range(n_v)] for r_i in range(n_v)])
        n_mat = sp.Matrix([[sp.simplify((vecs[r_i].H * vecs[c_i])[0, 0]) for c_i in range(n_v)] for r_i in range(n_v)])
        return sorted(int(sp.simplify(kv)) for kv, mv in (n_mat.inv() * g_mat).eigenvals().items() for _ in range(int(mv)))

    d0_v10 = sp.Matrix.vstack(e10, g10)
    d1_v10 = sp.Matrix.hstack(-g10, e10)
    v10_a_vecs = d0_v10.nullspace()
    v10_b_vecs = d1_v10.H.nullspace()
    v10_h1_vecs = sp.Matrix.vstack(d1_v10, d0_v10.H).nullspace()
    indep_v10_a_mu = indep_mu_eigs(v10_a_vecs, mu10)
    indep_v10_h1_mu = indep_mu_eigs(v10_h1_vecs, sp.kronecker_product(sp.eye(2), mu10))
    assert indep_v10_a_mu == [2, 2] and indep_v10_h1_mu == [-2, -2, 2, 2]
    assert wp34["v10_aslot_mu_weights"] == indep_v10_a_mu
    assert wp34["v10_spin_mu_weights"] == indep_v10_h1_mu

    d0_16 = sp.Matrix.vstack(e16, g16)
    d1_16 = sp.Matrix.hstack(-g16, e16)
    s16_a_vecs = d0_16.nullspace()
    s16_h1_vecs = sp.Matrix.vstack(d1_16, d0_16.H).nullspace()
    indep_s16_a_mu = indep_mu_eigs(s16_a_vecs, mu16)
    indep_s16_h1_mu = indep_mu_eigs(s16_h1_vecs, sp.kronecker_product(sp.eye(2), mu16))
    assert indep_s16_a_mu == [3] and indep_s16_h1_mu == [0, 0]
    assert wp34["s16p_aslot_mu_weights"] == indep_s16_a_mu
    assert wp34["s16p_spin_mu_weights"] == indep_s16_h1_mu

    c10_gam = [(b10_pk * gammas_10[a_i] * chir10_pk).extract(idx16p, idx16p).applyfunc(sp.expand) for a_i in range(10)]
    c10_witt = [((c10_gam[2 * k_i] - sp.I * c10_gam[2 * k_i + 1]) / 2).applyfunc(sp.expand) for k_i in range(5)] + [
        ((c10_gam[2 * k_i] + sp.I * c10_gam[2 * k_i + 1]) / 2).applyfunc(sp.expand) for k_i in range(5)
    ]

    def witt_bil_ind(p_u: sp.Matrix, p_v: sp.Matrix) -> sp.Matrix:
        return sp.Matrix([sp.expand((p_u.T * c10_witt[m_i] * p_v)[0, 0]) for m_i in range(10)])

    v10_harm_slices = v10_a_vecs + v10_b_vecs + [vh[:10, :] for vh in v10_h1_vecs] + [vh[10:, :] for vh in v10_h1_vecs]
    s16_harm_slices = [sh[:16, :] for sh in s16_h1_vecs] + [sh[16:, :] for sh in s16_h1_vecs]
    psi_a_ind = s16_a_vecs[0]
    indep_harm_zero = (
        witt_bil_ind(psi_a_ind, psi_a_ind) == sp.zeros(10, 1)
        and all(sp.expand((vh.T * witt_bil_ind(psi_a_ind, sh))[0, 0]) == 0 for sh in s16_harm_slices for vh in v10_harm_slices)
        and all(sp.expand((vh.T * witt_bil_ind(s1, s2))[0, 0]) == 0 for s1 in s16_harm_slices for s2 in s16_harm_slices for vh in v10_harm_slices)
    )
    s16_neg1 = (mu16 + sp.eye(16)).nullspace()
    indep_nh_neg1 = any(
        sp.expand((vh.T * witt_bil_ind(u_v, v_v))[0, 0]) != 0 for u_v in s16_neg1 for v_v in s16_neg1 for vh in v10_a_vecs
    )
    v10_h1_m = sp.Matrix.hstack(*v10_h1_vecs)
    v10_h1_n2 = [
        (v10_h1_m * cv).applyfunc(sp.expand)
        for cv in (v10_h1_m.H * (sp.kronecker_product(sp.eye(2), mu10) + 2 * sp.eye(20)) * v10_h1_m).nullspace()
    ]
    v10_h1_n2_sl = [vh[:10, :] for vh in v10_h1_n2] + [vh[10:, :] for vh in v10_h1_n2]
    indep_nh_pos3 = any(sp.expand((vh.T * witt_bil_ind(psi_a_ind, u_v))[0, 0]) != 0 for u_v in s16_neg1 for vh in v10_h1_n2_sl)
    assert indep_harm_zero and indep_nh_neg1 and indep_nh_pos3
    assert wp34["all_three_parabolic_harmonic_yukawas_vanish"] == indep_harm_zero
    assert wp34["parabolic_spin_mu_neg1_couples_to_v10_aslot"] == indep_nh_neg1
    assert wp34["parabolic_aslot_mu_neg1_couples_to_v10_h1"] == indep_nh_pos3

    i8_pk = sp.eye(8)
    h4_8_pk = (
        (i8_pk - f6_pk[0] * f6_pk[1]) * irt2 * (i8_pk - f6_pk[2] * f6_pk[3]) * irt2 * (i8_pk - f6_pk[4] * f6_pk[5]) * irt2
    ).applyfunc(sp.expand)
    h4_4p_pk = h4_8_pk.extract(idx4p, idx4p)
    w8 = sp.expand((sp.Integer(1) + sp.I) * irt2)
    w8_c = sp.expand(w8**3)
    w8_i = sp.expand((sp.Integer(1) - sp.I) * irt2)
    indep_h4_split = {sp.expand(kv): int(mv) for kv, mv in h4_4p_pk.eigenvals().items()} == {w8_c: 1, w8_i: 3}
    assert indep_h4_split
    assert wp34["mechanical_h4_4p_split_exact"] == indep_h4_split

    s_idx_4p = [i_f for i_f in range(4) if sp.expand(h4_4p_pk[i_f, i_f] - w8_c) == 0]
    t_idx_4p = [i_f for i_f in range(4) if sp.expand(h4_4p_pk[i_f, i_f] - w8_i) == 0]
    indep_ss_wedge = sum(1 for pa, pb in combinations(range(4), 2) if pa in s_idx_4p and pb in s_idx_4p)
    indep_st_wedge = sum(
        1 for pa, pb in combinations(range(4), 2) if (pa in s_idx_4p and pb in t_idx_4p) or (pb in s_idx_4p and pa in t_idx_4p)
    )
    assert indep_ss_wedge == 0 and indep_st_wedge == 3
    assert wp34["singlet_singlet_wedge_dim_b1866"] == indep_ss_wedge
    assert wp34["singlet_triplet_wedge_dim_b1866"] == indep_st_wedge

    a32_pk = sp.zeros(32, 32)
    xw_4 = [1, 0, -1, -2, -3]
    for st_i in range(32):
        kp_v = 5 + sum(2 * xw_4[a_i] for a_i in range(5) if ((st_i // (2 ** (4 - a_i))) % 2 == 1))
        a32_pk[st_i, st_i] = sp.expand(w8 ** (kp_v % 8))
    b04_pk = cr_pk[0] * cr_pk[4] + an_pk[4] * an_pk[0]
    b13_pk = cr_pk[1] * cr_pk[3] + an_pk[3] * an_pk[1]
    d32_pk = ((sp.eye(32) - 2 * b04_pk * b04_pk) * (sp.eye(32) - b13_pk * b13_pk - sp.I * b13_pk)).applyfunc(sp.expand)
    b32_pk = (d32_pk * a32_pk).applyfunc(sp.expand)
    a16_pk = a32_pk.extract(idx16p, idx16p)
    b16_pk = b32_pk.extract(idx16p, idx16p)
    vn2_pk = sp.simplify((psi_a_ind.H * psi_a_ind)[0, 0])
    indep_vtop_hol = (
        (
            int(sp.simplify((psi_a_ind.H * (w8_c * a16_pk) * psi_a_ind)[0, 0] / vn2_pk)),
            int(sp.simplify((psi_a_ind.H * (w8_c * b16_pk) * psi_a_ind)[0, 0] / vn2_pk)),
        ),
        (
            int(sp.simplify((psi_a_ind.H * (w8_i * a16_pk) * psi_a_ind)[0, 0] / vn2_pk)),
            int(sp.simplify((psi_a_ind.H * (w8_i * b16_pk) * psi_a_ind)[0, 0] / vn2_pk)),
        ),
    )
    assert indep_vtop_hol == ((-1, -1), (1, 1))
    assert wp34["aslot_vtop_holonomy_singlet_vs_triplet"] == indep_vtop_hol

    # Independent parabolic cohomology evaluator (never calling producer's eval_parabolic_cohomology_on_hd):
    def indep_parabolic_cohom(
        deg_d: int, basis_hd: np.ndarray, mu_m: np.ndarray, ta_m: np.ndarray, tb_m: np.ndarray, eta_ab: tuple[int, int]
    ) -> tuple[int, int]:
        if basis_hd.shape[1] == 0:
            z_d = int(basis_hd.shape[1])
            return (z_d, z_d)
        mu_s = basis_hd.conj().T @ mu_m @ basis_hd
        ev_m, vc_m = np.linalg.eigh((mu_s + mu_s.conj().T) * 0.5)
        clusters: dict[int, list[int]] = {}
        for idx_e, val_e in enumerate(ev_m):
            clusters.setdefault(int(round(float(val_e))), []).append(idx_e)
        h0_c = 0
        h1_c = 0
        s_a = -1 if eta_ab[0] == 1 else 1
        s_b = -1 if eta_ab[1] == 1 else 1
        for mu_val, idxs_c in clusters.items():
            a_p = deg_d - mu_val
            v_s = basis_hd @ vc_m[:, idxs_c]
            ta_s = (s_a**a_p) * (v_s.conj().T @ ta_m @ v_s)
            tb_s = (s_b**a_p) * (v_s.conj().T @ tb_m @ v_s)
            comm_ab = ta_s @ tb_s @ ta_s.conj().T @ tb_s.conj().T
            ev_k, vc_k = np.linalg.eigh((comm_ab + comm_ab.conj().T) * 0.5)
            p_ids = [i_k for i_k, v_k in enumerate(ev_k) if abs(float(v_k) - 1.0) < 1e-9]
            m_ids = [i_k for i_k, v_k in enumerate(ev_k) if abs(float(v_k) + 1.0) < 1e-9]
            if p_ids:
                vp = v_s @ vc_k[:, p_ids]
                tap = (s_a**a_p) * (vp.conj().T @ ta_m @ vp)
                tbp = (s_b**a_p) * (vp.conj().T @ tb_m @ vp)
                n_mx = math.floor(a_p * 0.5) if a_p < 1 else (math.ceil(a_p * 0.5) - 1)
                if n_mx > 0:
                    h0_c += len(p_ids) * n_mx
                elif n_mx < 0:
                    h1_c += len(p_ids) * (-n_mx)
                else:
                    ey = np.eye(len(p_ids), dtype=complex)
                    sv_f = np.linalg.svd(np.vstack([tap - ey, tbp - ey]), compute_uv=False)
                    n_fx = int(np.sum(sv_f < 1e-9))
                    h0_c += n_fx
                    h1_c += n_fx
            if m_ids and a_p != 1:
                mb = len(m_ids) // 2
                n_mx = math.floor((a_p + 1) * 0.5) if a_p < 1 else (math.ceil((a_p + 1) * 0.5) - 1)
                d_par = -1 + 2 * n_mx
                if d_par > 0:
                    h0_c += mb * d_par
                else:
                    h1_c += mb * (-d_par)
        return (h0_c, h1_c)

    def cliff_v10_pk(z_l: list[Any]) -> sp.Matrix:
        acc_c = sp.zeros(32, 32)
        for idx_c, z_v in enumerate(z_l):
            if z_v != 0:
                acc_c += z_v * cr_pk[idx_c] + sp.conjugate(z_v) * an_pk[idx_c]
        return acc_c

    u32_h1_pk = sp.eye(32)
    for gm_v in [
        cliff_v10_pk([0, 0, sp.I, 0, 0]),
        cliff_v10_pk([sp.I * irt2, 0, 0, 0, sp.I * irt2]),
        cliff_v10_pk([irt2, 0, 0, 0, -irt2]),
        cliff_v10_pk([0, irt2, 0, irt2, 0]),
        cliff_v10_pk([0, sp.I * irt2, 0, -sp.I * irt2, 0]),
    ]:
        u32_h1_pk = (u32_h1_pk * gm_v).applyfunc(sp.expand)
    s32_h1_pk = (u32_h1_pk * chir10_pk).applyfunc(sp.expand)

    def lift128_pk_np(m32: sp.Matrix, m8: sp.Matrix) -> np.ndarray:
        out_n = np.zeros((128, 128), dtype=complex)
        m32_n = np.array(m32.tolist(), dtype=complex)
        m8_n = np.array(m8.tolist(), dtype=complex)
        nz32 = [[(r_i, m32_n[r_i, c_i]) for r_i in range(32) if abs(m32_n[r_i, c_i]) > TOL] for c_i in range(32)]
        nz8 = [[(r_i, m8_n[r_i, c_i]) for r_i in range(8) if abs(m8_n[r_i, c_i]) > TOL] for c_i in range(8)]
        for col_s, (c1, c2) in enumerate(splus_pk):
            for r1, v1 in nz32[c1]:
                for r2, v2 in nz8[c2]:
                    out_n[splus_pk_idx[(r1, r2)], col_s] = v1 * v2
        return out_n

    fi_np = np.array([[1.0j, 0.0], [0.0, -1.0j]], dtype=complex)
    fj_np = np.array([[0.0, 1.0], [-1.0, 0.0]], dtype=complex)
    e16_np = np.array(e16.tolist(), dtype=complex)
    g16_np = np.array(g16.tolist(), dtype=complex)
    mu16_np = np.array(mu16.tolist(), dtype=complex)
    a16_np = np.array(a16_pk.tolist(), dtype=complex)
    b16_np = np.array(b16_pk.tolist(), dtype=complex)
    _, sv1_16, vh1_16 = np.linalg.svd(np.vstack([np.hstack([-g16_np, e16_np]), np.vstack([e16_np, g16_np]).conj().T]))
    b1_16_np = vh1_16[sv1_16 < 1e-9].conj().T

    etas_all = [(0, 0), (1, 1), (1, 0), (0, 1)]
    indep_spin_h0_sing = {
        eta_v: indep_parabolic_cohom(
            1, b1_16_np, np.kron(np.eye(2), mu16_np), np.kron(fi_np, complex(w8_c) * a16_np), np.kron(fj_np, complex(w8_c) * b16_np), eta_v
        )[0]
        for eta_v in etas_all
    }
    indep_spin_h0_trip = {
        eta_v: indep_parabolic_cohom(
            1, b1_16_np, np.kron(np.eye(2), mu16_np), np.kron(fi_np, complex(w8_i) * a16_np), np.kron(fj_np, complex(w8_i) * b16_np), eta_v
        )[0]
        for eta_v in etas_all
    }
    assert indep_spin_h0_sing == {(0, 0): 1, (1, 1): 1, (1, 0): 0, (0, 1): 0}
    assert indep_spin_h0_trip == {(0, 0): 1, (1, 1): 1, (1, 0): 0, (0, 1): 0}
    assert wp34["parabolic_spin_slot_h0_singlet_by_eta"] == indep_spin_h0_sing
    assert wp34["parabolic_spin_slot_h0_triplet_line_by_eta"] == indep_spin_h0_trip

    e128_pk = lift128_pk_np(spin32_pk(e10), i8_pk)
    g128_pk = lift128_pk_np(spin32_pk(g10), i8_pk)
    mu128_pk = lift128_pk_np(spin32_pk(mu10), i8_pk)
    d0_128_pk = np.vstack([e128_pk, g128_pk])
    d1_128_pk = np.hstack([-g128_pk, e128_pk])
    _, sv0_p, vh0_p = np.linalg.svd(d0_128_pk)
    _, sv1_p, vh1_p = np.linalg.svd(np.vstack([d1_128_pk, d0_128_pk.conj().T]))
    _, sv2_p, vh2_p = np.linalg.svd(d1_128_pk.conj().T)
    b0_p = vh0_p[sv0_p < 1e-9].conj().T
    b1_p = vh1_p[sv1_p < 1e-9].conj().T
    b2_p = vh2_p[sv2_p < 1e-9].conj().T

    for key_c, ah32_c, ah8_c in [
        ("parabolic_s16p_128_census_h4", a32_pk, h4_8_pk),
        ("parabolic_s16p_128_census_h1", (a32_pk * s32_h1_pk).applyfunc(sp.expand), f6_pk[0]),
    ]:
        xa_c = lift128_pk_np(ah32_c, ah8_c)
        yb_c = lift128_pk_np((d32_pk * ah32_c).applyfunc(sp.expand), ah8_c)
        indep_census: dict[tuple[int, int], tuple[int, int]] = {}
        for eta_v in etas_all:
            h0_0, h1_0 = indep_parabolic_cohom(0, b0_p, mu128_pk, xa_c, yb_c, eta_v)
            h0_1, h1_1 = indep_parabolic_cohom(
                1, b1_p, np.kron(np.eye(2), mu128_pk), np.kron(fi_np, xa_c), np.kron(fj_np, yb_c), eta_v
            )
            h0_2, h1_2 = indep_parabolic_cohom(2, b2_p, mu128_pk, xa_c, yb_c, eta_v)
            indep_census[eta_v] = (h1_2 + h1_0 + h0_1, h0_0 + h1_1 + h0_2)
        assert indep_census == {(0, 0): (24, 24), (1, 1): (24, 24), (1, 0): (16, 16), (0, 1): (16, 16)}
        assert wp34[key_c] == indep_census

    # Independent non-commuting reflection counterexample for joint_fixed_subspace_dim_num:
    ta_nc_sp = sp.Matrix([[1, 0], [0, -1]])
    tb_nc_sp = sp.Matrix([[sp.Rational(5, 13), sp.Rational(12, 13)], [sp.Rational(12, 13), sp.Rational(-5, 13)]])
    ta_nc = np.array(ta_nc_sp.tolist(), dtype=complex)
    tb_nc = np.array(tb_nc_sp.tolist(), dtype=complex)
    assert joint_fixed_subspace_dim_num(ta_nc, tb_nc, tol=1e-9) == 0
    assert sp.Rational(((sp.eye(2) + ta_nc_sp) * (sp.eye(2) + tb_nc_sp)).trace(), 4) == sp.Rational(9, 13)

    # 2. Independent 35-digit mpmath verification at second modulus tau_alt = 1/4 + i*19/12:
    #    - |eta(tau)|^4 = |theta_1'(0|tau)/(2*pi)|^{4/3} inside Omega_coord(z|tau) (S-covariant to < 1e-30),
    #    - True orthonormal exponents (-13/4, -11/4, -7/4, -9/4) on n_pts = 20,
    #    - Exact SL(2, Z) T and S invariance (< 1e-12) + no-|eta|^4 negative control,
    #    - Exact analytical Riemann theta triple-product overlap agreement (< 1e-30)!
    with mp.workdps(35):
        re_alt = mp.fdiv(1, 4)
        im_alt = mp.fdiv(19, 12)
        tau_alt = mp.mpc(re_alt, im_alt)
        q_alt = mp.exp(1j * mp.pi * tau_alt)
        th1p_alt = mp.pi * mp.jtheta(1, 0, q_alt, 1)

        def s_kern(nu_i: int, z_v: mp.mpc) -> mp.mpc:
            return (th1p_alt * mp.jtheta(nu_i, mp.pi * z_v, q_alt)) / (
                mp.jtheta(nu_i, 0, q_alt) * mp.jtheta(1, mp.pi * z_v, q_alt)
            )

        def ds_kern(nu_i: int, z_v: mp.mpc) -> mp.mpc:
            c_p = th1p_alt / mp.jtheta(nu_i, 0, q_alt)
            tn = mp.jtheta(nu_i, mp.pi * z_v, q_alt)
            dtn = mp.pi * mp.jtheta(nu_i, mp.pi * z_v, q_alt, 1)
            t1 = mp.jtheta(1, mp.pi * z_v, q_alt)
            dt1 = mp.pi * mp.jtheta(1, mp.pi * z_v, q_alt, 1)
            return c_p * (dtn * t1 - tn * dt1) / (t1**2)

        def f_wp(z_v: mp.mpc) -> mp.mpc:
            t1 = mp.jtheta(1, mp.pi * z_v, q_alt)
            dt1 = mp.jtheta(1, mp.pi * z_v, q_alt, 1)
            d2t1 = mp.jtheta(1, mp.pi * z_v, q_alt, 2)
            return (mp.pi**2) * ((dt1**2 - t1 * d2t1) / (t1**2))

        def om_coord_alt(z_v: mp.mpc, t_m: mp.mpc) -> mp.mpf:
            q_m = mp.exp(1j * mp.pi * t_m)
            th1p_m = mp.pi * mp.jtheta(1, 0, q_m, 1)
            eta4_m = abs(th1p_m / (2 * mp.pi)) ** (mp.mpf(4) / mp.mpf(3))
            v_m = mp.fdiv(mp.im(z_v), mp.im(t_m))
            r2_m = (abs(mp.jtheta(1, mp.pi * z_v, q_m)) ** 2 / (abs(th1p_m) ** 2)) * mp.exp(
                -2 * mp.pi * (v_m**2) * mp.im(t_m)
            )
            return mp.mpf(1) / (r2_m * (mp.log((eta4_m * r2_m) / mp.mpf(16)) ** 2))

        e_alt = {
            2: f_wp(mp.mpc(mp.mpf(1) / mp.mpf(2))),
            3: f_wp((mp.mpc(1) + tau_alt) / mp.mpf(2)),
            4: f_wp(tau_alt / mp.mpf(2)),
        }
        z_test = mp.mpc(mp.fdiv(3, 11), mp.fdiv(5, 13))
        assert (
            float(
                abs(
                    om_coord_alt(mp.fdiv(-z_test, tau_alt), mp.fdiv(-1, tau_alt))
                    - mp.re(tau_alt * mp.conj(tau_alt)) * om_coord_alt(z_test, tau_alt)
                )
            )
            < 1e-30
        )
        assert float(abs(om_coord_alt(z_test, tau_alt + 1) - om_coord_alt(z_test, tau_alt))) < 1e-30
        for k_h, i_f, j_f in [(2, 3, 4), (3, 4, 2), (4, 2, 3)]:
            assert float(abs(ds_kern(k_h, z_test) + s_kern(i_f, z_test) * s_kern(j_f, z_test))) < 1e-24
            assert (
                float(
                    abs(
                        ds_kern(k_h, z_test) * s_kern(i_f, z_test) * s_kern(j_f, z_test)
                        + (f_wp(z_test) - e_alt[i_f]) * (f_wp(z_test) - e_alt[j_f])
                    )
                )
                < 1e-24
            )

        perms_all = [(2, 3, 4), (2, 4, 3), (3, 2, 4), (3, 4, 2), (4, 2, 3), (4, 3, 2)]
        n_pts = 20

        def eval_alt_overlaps(t_m: mp.mpc, use_eta4: bool = True) -> dict[str, Any]:
            q_m = mp.exp(1j * mp.pi * t_m)
            im_m = mp.im(t_m)
            th1p_m = mp.pi * mp.jtheta(1, 0, q_m, 1)
            eta4_m = (abs(th1p_m / (2 * mp.pi)) ** (mp.mpf(4) / mp.mpf(3))) if use_eta4 else mp.mpf(1)
            th1p_sq = abs(th1p_m) ** 2
            th0_m = {nu_i: mp.jtheta(nu_i, 0, q_m) for nu_i in (2, 3, 4)}
            cell_p = mp.fdiv(mp.fdiv(im_m, n_pts), n_pts)

            nrm_s = {2: mp.mpf(0), 3: mp.mpf(0), 4: mp.mpf(0)}
            nrm_ds = {2: mp.mpf(0), 3: mp.mpf(0), 4: mp.mpf(0)}
            nrm_u0 = mp.mpf(0)
            sp_map = {tr: mp.mpc(0) for tr in perms_all}
            dp_map = {tr: mp.mpc(0) for tr in perms_all}
            sp_dg = {nu_i: mp.mpc(0) for nu_i in (2, 3, 4)}
            dp_dg = {nu_i: mp.mpc(0) for nu_i in (2, 3, 4)}
            planted_bad = mp.mpc(0)

            for ku_p in range(n_pts):
                u_raw = ku_p - n_pts if 2 * ku_p > n_pts else ku_p
                u_p = mp.fdiv(u_raw, n_pts)
                for kv_p in range(n_pts):
                    if ku_p == 0 and kv_p == 0:
                        continue
                    v_raw = kv_p - n_pts if 2 * kv_p > n_pts else kv_p
                    v_p = mp.fdiv(v_raw, n_pts)
                    z_p = mp.mpc(u_p) + mp.mpc(v_p) * t_m
                    pz_p = mp.pi * z_p
                    t1_p = mp.jtheta(1, pz_p, q_m)
                    dt1_p = mp.pi * mp.jtheta(1, pz_p, q_m, 1)
                    r2_p = (abs(t1_p) ** 2 / th1p_sq) * mp.exp(-2 * mp.pi * (v_p**2) * im_m)
                    om_p = mp.mpf(1) / (r2_p * (mp.log((eta4_m * r2_p) / mp.mpf(16)) ** 2))
                    om_inv_qtr = abs(mp.sqrt(abs(mp.sqrt(mp.mpf(1) / om_p))))
                    om_qtr = mp.mpf(1) / om_inv_qtr

                    sv_m: dict[int, mp.mpc] = {}
                    dsv_m: dict[int, mp.mpc] = {}
                    t1_sq = t1_p**2
                    for nu_i in (2, 3, 4):
                        tn_p = mp.jtheta(nu_i, pz_p, q_m)
                        dtn_p = mp.pi * mp.jtheta(nu_i, pz_p, q_m, 1)
                        pr_i = th1p_m / th0_m[nu_i]
                        sv_m[nu_i] = (pr_i * tn_p) / t1_p
                        dsv_m[nu_i] = pr_i * (dtn_p * t1_p - tn_p * dt1_p) / t1_sq

                    nrm_u0 += (om_qtr**2) * cell_p
                    for nu_i in (2, 3, 4):
                        nrm_s[nu_i] += (om_inv_qtr**6) * cell_p * (abs(sv_m[nu_i]) ** 2)
                        nrm_ds[nu_i] += (om_inv_qtr**10) * cell_p * (abs(dsv_m[nu_i]) ** 2)
                        sp_dg[nu_i] += (om_inv_qtr**7) * cell_p * sv_m[nu_i] * mp.conj(sv_m[nu_i])
                        dp_dg[nu_i] += (om_inv_qtr**9) * cell_p * dsv_m[nu_i] * mp.conj(sv_m[nu_i])
                    for k_h, i_f, j_f in perms_all:
                        sp_map[(k_h, i_f, j_f)] += (om_inv_qtr**11) * cell_p * sv_m[k_h] * sv_m[i_f] * mp.conj(sv_m[j_f])
                        dp_map[(k_h, i_f, j_f)] += (om_inv_qtr**13) * cell_p * dsv_m[k_h] * sv_m[i_f] * mp.conj(sv_m[j_f])
                    z_shift = z_p + mp.mpf(1) / mp.mpf(6)
                    s2_sh = (th1p_m * mp.jtheta(2, mp.pi * z_shift, q_m)) / (
                        th0_m[2] * mp.jtheta(1, mp.pi * z_shift, q_m)
                    )
                    planted_bad += (om_inv_qtr**11) * cell_p * s2_sh * sv_m[3] * mp.conj(sv_m[4])

            mags_dp = sorted(
                float(abs(dp_map[(k_h, i_f, j_f)]) / mp.sqrt(nrm_ds[k_h] * nrm_s[i_f] * nrm_s[j_f]))
                for k_h, i_f, j_f in perms_all
            )
            mags_diag_sp = sorted(
                float(abs(sp_dg[nu_i]) / mp.sqrt(nrm_s[nu_i] * nrm_u0 * nrm_s[nu_i]))
                for nu_i in (2, 3, 4)
            )
            return {
                "mags_dp": mags_dp,
                "mags_diag_sp": mags_diag_sp,
                "sp_err": max(float(abs(v_p)) for v_p in sp_map.values()),
                "dp_raw_min": min(float(abs(v_p)) for v_p in dp_map.values()),
                "diag_sp_raw_min": min(float(abs(v_p)) for v_p in sp_dg.values()),
                "diag_dp_err": max(float(abs(v_p)) for v_p in dp_dg.values()),
                "planted_bad_mag": float(abs(planted_bad)),
            }

        res_alt = eval_alt_overlaps(tau_alt, use_eta4=True)
        res_alt_t = eval_alt_overlaps(tau_alt + 1, use_eta4=True)
        res_alt_s = eval_alt_overlaps(mp.fdiv(-1, tau_alt), use_eta4=True)
        res_no_eta = eval_alt_overlaps(tau_alt, use_eta4=False)
        res_s_no_eta = eval_alt_overlaps(mp.fdiv(-1, tau_alt), use_eta4=False)

        assert res_alt["sp_err"] < 1e-24
        assert res_alt["dp_raw_min"] > 1.0
        assert 4 * res_alt["mags_dp"][0] > 1.0
        assert res_alt["diag_sp_raw_min"] > 1.0
        assert res_alt["mags_diag_sp"][0] > 1.0
        assert res_alt["diag_dp_err"] < 1e-24
        assert res_alt["planted_bad_mag"] > 1e-6

        err_t_alt = max(abs(a_v - b_v) for a_v, b_v in zip(res_alt["mags_dp"], res_alt_t["mags_dp"]))
        err_s_alt = max(abs(a_v - b_v) for a_v, b_v in zip(res_alt["mags_dp"], res_alt_s["mags_dp"]))
        err_s_broken_alt = max(abs(a_v - b_v) for a_v, b_v in zip(res_no_eta["mags_dp"], res_s_no_eta["mags_dp"]))
        assert err_t_alt < TOL
        assert err_s_alt < TOL
        assert 10 * err_s_broken_alt > 1.0
        assert wp34["omega_coord_modular_max_err"] < 1e-30
        assert wp34["modular_t_yukawa_max_err"] < TOL
        assert wp34["modular_s_yukawa_max_err"] < TOL

        # Analytical Riemann theta triple-product agreement at tau_alt (< 1e-30):
        q_2alt = mp.exp(2 * 1j * mp.pi * tau_alt)
        i0_ex_alt = mp.sqrt(mp.sqrt(im_alt)) * mp.jtheta(3, 0, q_2alt)
        i1_ex_alt = mp.sqrt(mp.sqrt(im_alt)) * mp.jtheta(2, 0, q_2alt)
        n_q_alt = 28
        u_q_pts = [mp.fdiv(ku_q, n_q_alt) for ku_q in range(n_q_alt)]
        v_q_pts = [mp.fdiv(kv_q, n_q_alt) for kv_q in range(n_q_alt)]

        def theta_grid_alt(j_i: int, m_l: int) -> list[list[mp.mpc]]:
            pr_m = mp.sqrt(mp.sqrt(2 * m_l * im_alt))
            xs_l = [mp.mpf(n_i) + mp.fdiv(j_i, m_l) for n_i in range(-7, 8)]
            eu_l = [[mp.exp(2 * 1j * mp.pi * m_l * x_i * u_i) for x_i in xs_l] for u_i in u_q_pts]
            ev_l = [
                [mp.exp(1j * mp.pi * tau_alt * m_l * (x_i**2) + 2 * 1j * mp.pi * m_l * x_i * v_i * tau_alt) for x_i in xs_l]
                for v_i in v_q_pts
            ]
            return [
                [pr_m * sum((eu_l[ku_q][ix] * ev_l[kv_q][ix] for ix in range(len(xs_l))), mp.mpc(0)) for kv_q in range(n_q_alt)]
                for ku_q in range(n_q_alt)
            ]

        f01_a = theta_grid_alt(0, 1)
        f02_a = theta_grid_alt(0, 2)
        f12_a = theta_grid_alt(1, 2)
        du_dv_a = mp.fdiv(mp.fdiv(1, n_q_alt), n_q_alt)
        i0_q_alt = mp.mpc(0)
        i1_q_alt = mp.mpc(0)
        for ku_q in range(n_q_alt):
            for kv_q in range(n_q_alt):
                vq = v_q_pts[kv_q]
                wh = mp.exp(-4 * mp.pi * (vq**2) * im_alt) * du_dv_a
                f_sq = f01_a[ku_q][kv_q] ** 2
                i0_q_alt += wh * f_sq * mp.conj(f02_a[ku_q][kv_q])
                i1_q_alt += wh * f_sq * mp.conj(f12_a[ku_q][kv_q])
        assert float(abs(i0_ex_alt - i0_q_alt)) < 1e-30
        assert float(abs(i1_ex_alt - i1_q_alt)) < 1e-30
        assert wp34["theta_triple_product_exact_vs_quad_err"] < 1e-30

    x_pol = sp.Symbol("x_pol")
    deg_24 = int(sp.degree(sp.cyclotomic_poly(24, x_pol), x_pol))
    deg_5 = int(sp.degree(sp.cyclotomic_poly(5, x_pol), x_pol))
    deg_120 = int(sp.degree(sp.cyclotomic_poly(120, x_pol), x_pol))
    indep_q24_q5_disjoint = (deg_24 == 8) and (deg_5 == 4) and (deg_120 == deg_24 * deg_5)
    assert indep_q24_q5_disjoint
    assert wp34["cyclotomic_q24_q5_disjoint_slope_2_5_unforced"] == indep_q24_q5_disjoint


def test_wp25_zero_trust_lepton_c_gj_126bar_cyc24_schur_and_128d_dterm(
    stage5_results: dict[str, Any],
) -> None:
    wp25 = stage5_results["wp25_source_and_lepton_factor"]
    i2 = sp.eye(2)
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])

    def kron_l(ms: list[sp.Matrix]) -> sp.Matrix:
        res_m = ms[0]
        for nxt_m in ms[1:]:
            res_m = sp.kronecker_product(res_m, nxt_m)
        return res_m

    g10 = []
    for k_i in range(5):
        g10.append(kron_l([sz] * k_i + [sx] + [i2] * (4 - k_i)))
        g10.append(kron_l([sz] * k_i + [sy] + [i2] * (4 - k_i)))
    chir10 = kron_l([sz, sz, sz, sz, sz])
    b10 = kron_l([sy, sx, sy, sx, sy])
    idx16 = [r_i for r_i in range(32) if chir10[r_i, r_i] == 1]

    for a_i, b_i in combinations(range(10), 2):
        assert (b10 * g10[a_i] * g10[b_i]).extract(idx16, idx16).applyfunc(sp.expand) == sp.zeros(16, 16)

    # 1. Independent Pauli Cl(10) symmetric 5-form Georgi-Jarlskog operator in 126bar_s:
    weights16 = [
        tuple(int((-sp.I * g10[2 * a_i] * g10[2 * a_i + 1])[idx16[u_i], idx16[u_i]]) for a_i in range(5))
        for u_i in range(16)
    ]
    o_gj5 = (
        g10[2] * g10[3] * g10[4] * g10[5] * g10[6]
        + g10[0] * g10[1] * g10[4] * g10[5] * g10[6]
        + g10[0] * g10[1] * g10[2] * g10[3] * g10[6]
    ).applyfunc(sp.expand)
    m_gj = (b10 * o_gj5 * chir10).extract(idx16, idx16).applyfunc(sp.expand)
    assert (m_gj - m_gj.T).applyfunc(sp.expand) == sp.zeros(16, 16)
    le_val = m_gj[weights16.index((-1, -1, -1, -1, 1)), weights16.index((1, 1, 1, -1, -1))]
    indep_gj_ratios: list[int] = []
    for q_w, d_w in [
        ((-1, 1, 1, -1, 1), (1, -1, -1, -1, -1)),
        ((1, -1, 1, -1, 1), (-1, 1, -1, -1, -1)),
        ((1, 1, -1, -1, 1), (-1, -1, 1, -1, -1)),
    ]:
        qd_val = m_gj[weights16.index(q_w), weights16.index(d_w)]
        indep_gj_ratios.append(int(abs(sp.simplify(le_val / qd_val))))
    indep_gj_absent = (math.comb(10, 5) // 2) not in {1, 10, 16, 45}
    assert indep_gj_ratios == [3, 3, 3] and indep_gj_absent
    assert wp25["gj_126bar_5form_lepton_to_quark_abs_ratios"] == indep_gj_ratios
    assert wp25["gj_126bar_absent_in_e8_248"] == indep_gj_absent

    # 2. Independent Pauli-Kronecker (10, 6) Yukawa matrices Y_e, Y_d, Y_u, Y_nu, canonical normalization
    #    Y_phys = (G_L^{-1/2})^T Y G_R^{-1/2}, pre-normalization Haar U(3)^6 invariance (< 1e-12),
    #    and wrong-transpose G^{-1/2} Y (G^{-1/2})^T negative control (> 1e-2):
    f6_t = [
        kron_l([sx, i2, i2]),
        kron_l([sy, i2, i2]),
        kron_l([sz, sx, i2]),
        kron_l([sz, sy, i2]),
        kron_l([sz, sz, sx]),
        kron_l([sz, sz, sy]),
    ]
    chir6_t = -sp.I * (f6_t[0] * f6_t[1] * f6_t[2] * f6_t[3] * f6_t[4] * f6_t[5])
    b6_t = (f6_t[1] * f6_t[3] * f6_t[5]).applyfunc(sp.expand)
    idx4 = [r_i for r_i in range(8) if chir6_t[r_i, r_i] == 1]

    c10_16 = [np.array(((b10 * g10[a_i] * chir10).extract(idx16, idx16)).tolist(), dtype=complex) for a_i in range(10)]
    c6_4 = [np.array(((b6_t * f6_t[p_i]).extract(idx4, idx4)).tolist(), dtype=complex) for p_i in range(6)]
    for m6 in c6_4:
        assert float(np.max(np.abs(m6 + m6.T))) < TOL

    rng_25 = np.random.default_rng(61)
    ov_gen_4 = 0.5 * (rng_25.normal(size=(3, 3, 4, 4)) + 1j * rng_25.normal(size=(3, 3, 4, 4)))
    vev_ew = np.zeros((10, 6), dtype=complex)
    for a_ew in (6, 7):
        for p_ew in range(6):
            vev_ew[a_ew, p_ew] = 0.5 * complex(rng_25.normal() + 1j * rng_25.normal())

    def indep_yuk_3x3(w_l: tuple[int, ...], w_r: tuple[int, ...], transpose_6: bool = False) -> np.ndarray:
        u_idx = weights16.index(w_l)
        v_idx = weights16.index(w_r)
        y_out = np.zeros((3, 3), dtype=complex)
        for i_g in range(3):
            for j_g in range(3):
                acc_y = 0.0j
                for a_t in range(4):
                    for b_t in range(4):
                        cg_ab = 0.0j
                        for a_ew in (6, 7):
                            for p_ew in range(6):
                                r_a, r_b = (b_t, a_t) if transpose_6 else (a_t, b_t)
                                cg_ab += -0.5 * vev_ew[a_ew, p_ew] * c10_16[a_ew][u_idx, v_idx] * c6_4[p_ew][r_a, r_b]
                        i_use, j_use = (j_g, i_g) if transpose_6 else (i_g, j_g)
                        acc_y += ov_gen_4[i_use, j_use, a_t, b_t] * cg_ab
                y_out[i_g, j_g] = acc_y
        return y_out

    yu_raw = indep_yuk_3x3((-1, 1, 1, 1, -1), (1, -1, -1, 1, 1))
    ynu_raw = indep_yuk_3x3((-1, -1, -1, 1, -1), (1, 1, 1, 1, 1))
    yd_raw = indep_yuk_3x3((-1, 1, 1, -1, 1), (1, -1, -1, -1, -1))
    ye_raw = indep_yuk_3x3((-1, -1, -1, -1, 1), (1, 1, 1, -1, -1), transpose_6=True)
    # Note in Pauli-Kronecker B_10 = sy(x)sx(x)sy(x)sx(x)sy, Check exact sign of Y_e vs Y_d^T:
    assert min(float(np.max(np.abs(ye_raw - yd_raw.T))), float(np.max(np.abs(ye_raw + yd_raw.T)))) < TOL
    assert min(float(np.max(np.abs(ynu_raw - yu_raw))), float(np.max(np.abs(ynu_raw + yu_raw)))) < TOL

    def inv_sqrt_3(g_m: np.ndarray) -> np.ndarray:
        ev_g, vc_g = np.linalg.eigh((g_m + g_m.conj().T) * 0.5)
        return vc_g @ np.diag(1.0 / np.sqrt(ev_g)) @ vc_g.conj().T

    def ckm_and_j_ind(yu_m: np.ndarray, yd_m: np.ndarray) -> tuple[np.ndarray, float]:
        hu_m = yu_m.conj() @ yu_m.T
        hd_m = yd_m.conj() @ yd_m.T
        _, vu_m = np.linalg.eigh((hu_m + hu_m.conj().T) * 0.5)
        _, vd_m = np.linalg.eigh((hd_m + hd_m.conj().T) * 0.5)
        cm_ud = hu_m @ hd_m - hd_m @ hu_m
        return np.abs(vu_m.conj().T @ vd_m), float(np.imag(np.trace(cm_ud @ cm_ud @ cm_ud)))

    a_kin = rng_25.normal(size=(3, 3)) + 1j * rng_25.normal(size=(3, 3))
    g_kin_0 = a_kin.conj().T @ a_kin + np.eye(3)
    e_kin_0 = inv_sqrt_3(g_kin_0)

    yu_phys_0 = e_kin_0.T @ yu_raw @ e_kin_0
    yd_phys_0 = e_kin_0.T @ yd_raw @ e_kin_0
    ye_phys_0 = e_kin_0.T @ ye_raw @ e_kin_0
    ynu_phys_0 = e_kin_0.T @ ynu_raw @ e_kin_0

    sv_u_0 = np.sort(np.linalg.svd(yu_phys_0, compute_uv=False))
    sv_d_0 = np.sort(np.linalg.svd(yd_phys_0, compute_uv=False))
    sv_e_0 = np.sort(np.linalg.svd(ye_phys_0, compute_uv=False))
    sv_nu_0 = np.sort(np.linalg.svd(ynu_phys_0, compute_uv=False))
    c_uv_0 = float(sv_e_0[2] / sv_d_0[2])
    ckm_0, jtr_0 = ckm_and_j_ind(yu_phys_0, yd_phys_0)
    assert abs(c_uv_0 - 1.0) < TOL
    assert abs(wp25["derived_spin10_symmetric_lepton_factor_c"] - c_uv_0) < TOL
    assert abs(jtr_0) > 1e-6

    # Negative-control base (WRONG transpose E @ Y @ E.T):
    sv_wrong_0 = np.sort(np.linalg.svd(e_kin_0 @ yd_raw @ e_kin_0.T, compute_uv=False))
    max_true_prenorm_err = 0.0
    max_wrong_prenorm_err = 0.0
    for _ in range(10):
        w_q = haar_unitary(3, rng_25)
        w_uc = haar_unitary(3, rng_25)
        w_dc = haar_unitary(3, rng_25)
        w_l = haar_unitary(3, rng_25)
        w_ec = haar_unitary(3, rng_25)
        w_nuc = haar_unitary(3, rng_25)

        e_q = inv_sqrt_3(w_q.conj().T @ g_kin_0 @ w_q)
        e_uc = inv_sqrt_3(w_uc.conj().T @ g_kin_0 @ w_uc)
        e_dc = inv_sqrt_3(w_dc.conj().T @ g_kin_0 @ w_dc)
        e_l = inv_sqrt_3(w_l.conj().T @ g_kin_0 @ w_l)
        e_ec = inv_sqrt_3(w_ec.conj().T @ g_kin_0 @ w_ec)
        e_nuc = inv_sqrt_3(w_nuc.conj().T @ g_kin_0 @ w_nuc)

        yu_s = e_q.T @ (w_q.T @ yu_raw @ w_uc) @ e_uc
        yd_s = e_q.T @ (w_q.T @ yd_raw @ w_dc) @ e_dc
        ye_s = e_l.T @ (w_l.T @ ye_raw @ w_ec) @ e_ec
        ynu_s = e_l.T @ (w_l.T @ ynu_raw @ w_nuc) @ e_nuc

        sv_us = np.sort(np.linalg.svd(yu_s, compute_uv=False))
        sv_ds = np.sort(np.linalg.svd(yd_s, compute_uv=False))
        sv_es = np.sort(np.linalg.svd(ye_s, compute_uv=False))
        sv_nus = np.sort(np.linalg.svd(ynu_s, compute_uv=False))
        ckm_s, jtr_s = ckm_and_j_ind(yu_s, yd_s)
        max_true_prenorm_err = max(
            max_true_prenorm_err,
            float(np.max(np.abs(sv_us - sv_u_0))),
            float(np.max(np.abs(sv_ds - sv_d_0))),
            float(np.max(np.abs(sv_es - sv_e_0))),
            float(np.max(np.abs(sv_nus - sv_nu_0))),
            abs(float(sv_es[2] / sv_ds[2]) - 1.0),
            float(np.max(np.abs(ckm_s - ckm_0))),
            abs(jtr_s - jtr_0),
        )

        yd_wrong_s = e_q @ (w_q.T @ yd_raw @ w_dc) @ e_dc.T
        sv_wrong_s = np.sort(np.linalg.svd(yd_wrong_s, compute_uv=False))
        max_wrong_prenorm_err = max(max_wrong_prenorm_err, float(np.max(np.abs(sv_wrong_s - sv_wrong_0))))

    assert max_true_prenorm_err < TOL
    assert 100 * max_wrong_prenorm_err > 1.0
    assert wp25["max_prenorm_haar_observables_err"] < TOL

    # 3. Independent 2D Weil Sym^2 construction of BOTH 3_sp (order 96) and 3_dp (order 288 = 12*24):
    t_weil = np.diag([1.0 + 0.0j, 1.0j])
    s_weil = (np.exp(-1j * math.pi / 4) / math.sqrt(2.0)) * np.array([[1.0, 1.0], [1.0, -1.0]], dtype=complex)
    r_weil = np.linalg.inv(s_weil) @ np.linalg.inv(t_weil) @ s_weil
    p_sym2 = np.zeros((4, 3), dtype=complex)
    p_sym2[0, 0] = 1.0
    p_sym2[1, 1] = 1.0 / math.sqrt(2.0)
    p_sym2[2, 1] = 1.0 / math.sqrt(2.0)
    p_sym2[3, 2] = 1.0

    tl_sp = (np.exp(-1j * math.pi / 4) * (p_sym2.conj().T @ np.kron(t_weil, t_weil) @ p_sym2)).conj()
    tr_sp = (np.exp(1j * math.pi / 4) * (p_sym2.conj().T @ np.kron(r_weil, r_weil) @ p_sym2)).conj()
    tl_dp = np.exp(-1j * math.pi / 6) * tl_sp
    tr_dp = np.exp(1j * math.pi / 6) * tr_sp
    z3 = np.zeros((3, 3), dtype=complex)
    indep_end_sp = joint_commutant_dim_num([tl_sp, tr_sp], tol=1e-10)
    indep_end_dp = joint_commutant_dim_num([tl_dp, tr_dp], tol=1e-10)
    indep_end_6d = joint_commutant_dim_num(
        [np.block([[tl_sp, z3], [z3, tl_dp]]), np.block([[tr_sp, z3], [z3, tr_dp]])], tol=1e-10
    )
    indep_hom_sp_dp = (indep_end_6d - indep_end_sp - indep_end_dp) // 2
    assert indep_end_sp == 1 and indep_end_dp == 1 and indep_end_6d == 2 and indep_hom_sp_dp == 0
    assert joint_commutant_dim_num([tl_sp, tr_sp @ tr_sp], tol=1e-10) == 2
    assert wp25["weave_g96_gen_metric_commutant_dim"] == indep_end_sp
    assert wp25["weave_3dp_gen_metric_commutant_dim"] == indep_end_dp
    assert wp25["weave_hom_3sp_to_3dp_dim"] == indep_hom_sp_dp
    assert wp25["weave_6d_sp_plus_dp_commutant_dim"] == indep_end_6d

    # Independent closure of 3_dp group (order 288 -> len - 128 == 160, center 12, PG 24):
    grp_dp_np: list[np.ndarray] = [np.eye(3, dtype=complex)]
    gens_dp_np = [tl_dp, tr_dp, tl_dp.conj().T, tr_dp.conj().T]
    q_idx = 0
    while q_idx < len(grp_dp_np):
        cur_g = grp_dp_np[q_idx]
        q_idx += 1
        for gen_m in gens_dp_np:
            cand_m = cur_g @ gen_m
            if not any(float(np.max(np.abs(cand_m - ex_m))) < 1e-8 for ex_m in grp_dp_np):
                grp_dp_np.append(cand_m)
    assert len(grp_dp_np) - 128 == 160
    i3_np = np.eye(3, dtype=complex)
    indep_cent_dp = sum(
        1
        for g_m in grp_dp_np
        if float(np.max(np.abs(g_m - (np.trace(g_m) / 3) * i3_np))) < 1e-8
    )
    indep_pg_dp = len(grp_dp_np) // indep_cent_dp
    assert (indep_cent_dp, indep_pg_dp) == (12, 24)
    assert wp25["weave_3dp_center_and_pg"] == (indep_cent_dp, indep_pg_dp)

    # 4. Independent 128D S_16^+ quartic D-term dichotomy check:
    splus = [(r10, r6) for r10 in range(32) for r6 in range(8) if sp.expand(chir10[r10, r10] * chir6_t[r6, r6]) == 1]
    assert len(splus) == 128
    s_map = {pt: idx_s for idx_s, pt in enumerate(splus)}

    def lift128(m32: sp.Matrix, m8: sp.Matrix) -> sp.Matrix:
        out_m = sp.zeros(128, 128)
        nz32 = [[(r_i, m32[r_i, c_i]) for r_i in range(32) if m32[r_i, c_i] != 0] for c_i in range(32)]
        nz8 = [[(r_i, m8[r_i, c_i]) for r_i in range(8) if m8[r_i, c_i] != 0] for c_i in range(8)]
        for col_i, (c10, c6) in enumerate(splus):
            for r10, v10 in nz32[c10]:
                for r6, v6 in nz8[c6]:
                    out_m[s_map[(r10, r6)], col_i] = sp.expand(v10 * v6)
        return out_m

    irt2 = sp.Integer(1) / sp.sqrt(2)
    bu32 = ((g10[7] - sp.I * g10[6]) * chir10 * irt2).applyfunc(sp.expand)
    bd32 = ((g10[7] + sp.I * g10[6]) * chir10 * irt2).applyfunc(sp.expand)
    fp8 = ((f6_t[0] - sp.I * f6_t[1]) * irt2).applyfunc(sp.expand)
    fm8 = ((f6_t[0] + sp.I * f6_t[1]) * irt2).applyfunc(sp.expand)
    r_u, r_d = sp.symbols("r_u r_d", real=True)

    dterm_polys: list[sp.Expr] = []
    for fu8, fd8, expected_poly in [
        (f6_t[0], f6_t[0], 8 * (r_u**2 - r_d**2) ** 2),
        (fm8, fm8, 16 * (r_u**4 + r_d**4)),
        (fm8, fp8, 16 * (r_u**2 - r_d**2) ** 2),
    ]:
        bu128 = lift128(bu32, fu8)
        bd128 = lift128(bd32, fd8)
        ph = r_u * bu128 + r_d * bd128
        phd = r_u * bu128.H + r_d * bd128.H
        cm = (ph * phd - phd * ph).applyfunc(sp.expand)
        tr_val = sp.Integer(0)
        for r_s in range(128):
            for c_s in range(128):
                if cm[r_s, c_s] != 0:
                    tr_val += sp.expand(cm[r_s, c_s] * sp.conjugate(cm[r_s, c_s]))
        poly_64 = sp.simplify(tr_val / 64)
        assert sp.simplify(poly_64 - expected_poly) == 0
        dterm_polys.append(poly_64)

    indep_c_real = int(sp.simplify(dterm_polys[0] / ((r_u**2 - r_d**2) ** 2)))
    indep_c_same = int(sp.simplify(dterm_polys[1] / (r_u**4 + r_d**4)))
    indep_dterm_ok = (indep_c_real == 8) and (indep_c_same == 16)
    assert indep_dterm_ok
    assert wp25["d_term_real_slice_coeff_per_64"] == indep_c_real
    assert wp25["d_term_same_h4_posdef_coeff_per_64"] == indep_c_same
    assert wp25["d_term_dichotomy_and_real_valley_verified"] == indep_dterm_ok
