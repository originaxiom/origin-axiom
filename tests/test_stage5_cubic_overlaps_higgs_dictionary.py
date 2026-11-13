"""Zero-trust pytest counterchecks & AST locks for Stage 5 (B1861 WP-1.7, WP-3.4, WP-2.5):
Quantum-Number Dictionary, Curved Trilinear Gauge-Yukawa Overlaps vs Four-Channel Value Frame,
Stationary Source & Relative Lepton-to-Quark Normalization Factor c.

Enforces Guardrails 1-6 and Anti-Shortcut Locks F1-F6:
- Strict 0-of-19 empirical data firewall & Guardrail-2 AST locks on both producer and test suite.
- Guardrail 6 zero-trust independence: constructs independent Pauli-Kronecker Cl(10)xCl(6) Lie
  centralizers, Z_4 glue kernel, full SU(2)_L eps_{ab} doublet contractions, 16D gauge-allowed
  Haar U(3)_C x U(2)_L scrambling, independent 35-digit mpmath Weierstrass-Jacobi & curved
  hyperbolic cusp integrals at a second modulus tau_alt (both off-diagonal and diagonal spin-slot
  parity reversal), explicit Cl(10) 5-form 126bar_s Georgi-Jarlskog operator, independent Q(zeta_24)
  commutants for 3_sp(96) & 3_dp(288), and independent 128D S_16^+ quartic D-term dichotomy.
"""
from __future__ import annotations

from itertools import combinations, product
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
    assert audit_source_zero_empirical_constants(STAGE5_SRC) is True
    assert audit_source_zero_empirical_constants(TEST5_SRC) is True
    assert check_guardrail2_ast_no_literal_bool_verdicts(STAGE5_SRC.read_text(encoding="utf-8")) is True
    assert check_guardrail2_ast_no_literal_bool_verdicts(TEST5_SRC.read_text(encoding="utf-8")) is True
    assert stage5_results["zero_sm_empirical_constants_ast_verified"] is True
    assert stage5_results["guardrail2_ast_no_literal_bool_verdicts_verified"] is True
    assert stage5_results["all_verifications_passed"] is True


def test_wp17_zero_trust_spin10_centralizers_z4_glue_and_up_conjugate(stage5_results: dict[str, Any]) -> None:
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

    prod_g10 = sp.eye(32)
    for g_m in gammas_10:
        prod_g10 = (prod_g10 * g_m).applyfunc(sp.expand)
    chir10_unit = (-sp.I * prod_g10).applyfunc(sp.expand)
    idx_16p = [r_i for r_i in range(32) if chir10_unit[r_i, r_i] == 1]
    assert len(idx_16p) == 16

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
    assert stage5_results["wp17_dictionary"]["so10_centralizer_dim"] == len(z_so10_ns)
    assert stage5_results["wp17_dictionary"]["u5_centralizer_dim"] == len(z_u5_ns)

    z_so10_mats = [so10_from_col(v_z) for v_z in z_so10_ns]
    assert sp.Matrix([coords45(z_so10_mats[p_i] * z_so10_mats[q_i] - z_so10_mats[q_i] * z_so10_mats[p_i]) for p_i, q_i in combinations(range(4), 2)]).rank() == 3

    # 2. Independent hypercharge dichotomy, w_{SU(2)_R}, Z_4 glue kernel, and full SU(2)_L doublet conjugation:
    h_cartan = [(-sp.I * sp.Rational(1, 2) * gammas_10[2 * a_i] * gammas_10[2 * a_i + 1]).extract(idx_16p, idx_16p) for a_i in range(5)]
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
    assert stage5_results["wp17_dictionary"]["hypercharge_solutions_count"] == len(found_ab)
    assert stage5_results["wp17_dictionary"]["z4_glue_kernel_order"] == 4
    assert stage5_results["wp17_dictionary"]["shared_16_4_sector_carrier_derived"] is True

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
        return sp.expand(p6 * c10_vecs[6][u_a, u_b] + p7 * c10_vecs[7][u_a, u_b] + p8 * c10_vecs[8][u_a, u_b] + p9 * c10_vecs[9][u_a, u_b])

    y_uu = c10_ew(u_qu, u_uc)
    y_du = c10_ew(u_qd, u_uc)
    y_ud = c10_ew(u_qu, u_dc)
    y_dd = c10_ew(u_qd, u_dc)
    # Full SU(2)_L eps_{ab} conjugate doublet check across all 4 real EW parameters:
    r_00 = sp.simplify(y_dd / sp.conjugate(y_uu))
    r_01 = sp.simplify(y_ud / sp.conjugate(y_du))
    assert sp.simplify(r_00 * sp.conjugate(r_00) - 1) == 0
    assert sp.simplify(r_01 + r_00) == 0

    # Independent 16D gauge-allowed SU(3)_C x SU(2)_L x U(1)_Y Haar basis scrambling (< 1e-12):
    sm16_indep = []
    for g_sm in (su3_10 + su2_10):
        acc_g16 = sp.zeros(16, 16)
        for a_i in range(10):
            for b_i in range(a_i + 1, 10):
                c_ab = sp.Rational(g_sm[a_i, b_i])
                if c_ab != 0:
                    gen_ab = (sp.Rational(1, 2) * gammas_10[a_i] * gammas_10[b_i]).extract(idx_16p, idx_16p)
                    acc_g16 = acc_g16 + c_ab * gen_ab
        sm16_indep.append(np.array(acc_g16.applyfunc(sp.expand).tolist(), dtype=complex))
    rng_17 = np.random.default_rng(37)
    k16_np = np.array(c10_vecs[6].tolist(), dtype=complex)
    sv0_16 = np.sort(np.linalg.svd(k16_np, compute_uv=False))
    for _ in range(8):
        th_v = rng_17.normal(size=len(sm16_indep))
        ah_m = sum(th_v[i_g] * sm16_indep[i_g] for i_g in range(len(sm16_indep)))
        ev_a, vc_a = np.linalg.eigh(-1.0j * ah_m)
        u_g = vc_a @ np.diag(np.exp(1.0j * ev_a)) @ vc_a.conj().T
        sv_scr = np.sort(np.linalg.svd(u_g @ k16_np @ u_g.T, compute_uv=False))
        assert float(np.max(np.abs(sv_scr - sv0_16))) < TOL


def test_wp34_zero_trust_parabolic_selection_curved_cusp_weierstrass_and_q24_q5(
    stage5_results: dict[str, Any],
) -> None:
    wp34 = stage5_results["wp34_cubic_overlaps"]
    assert wp34["fock_16p_odd_bitsum_verified"] is True
    assert wp34["mechanical_h4_4p_split_exact"] is True
    assert wp34["all_three_parabolic_harmonic_yukawas_vanish"] is True
    assert wp34["parabolic_spin_mu_neg1_couples_to_v10_aslot"] is True
    assert wp34["parabolic_aslot_mu_neg1_couples_to_v10_h1"] is True
    assert wp34["aslot_vtop_holonomy_singlet_vs_triplet"] == ((-1, -1), (1, 1))
    assert wp34["parabolic_spin_slot_h0_singlet_by_eta"] == {(0, 0): 1, (1, 1): 1, (1, 0): 0, (0, 1): 0}
    assert wp34["parabolic_spin_slot_h0_triplet_line_by_eta"] == {(0, 0): 1, (1, 1): 1, (1, 0): 0, (0, 1): 0}
    assert wp34["parabolic_s16p_128_census_h4"] == {(0, 0): (24, 24), (1, 1): (24, 24), (1, 0): (16, 16), (0, 1): (16, 16)}
    assert wp34["parabolic_s16p_128_census_h1"] == {(0, 0): (24, 24), (1, 1): (24, 24), (1, 0): (16, 16), (0, 1): (16, 16)}
    assert wp34["singlet_singlet_wedge_dim_b1866"] == 0
    assert wp34["singlet_triplet_wedge_dim_b1866"] == 3

    # Independent non-commuting reflection counterexample for joint_fixed_subspace_dim_num:
    # T_a = diag(1, -1), T_b = (1/13)[[5, 12], [12, -5]] (Pythagorean 5^2 + 12^2 = 13^2):
    # True joint fixed dim == 0, while Tr((I+T_a)(I+T_b)/4) = 9/13 > 1/2 rounds to 1!
    ta_nc_sp = sp.Matrix([[1, 0], [0, -1]])
    tb_nc_sp = sp.Matrix([[sp.Rational(5, 13), sp.Rational(12, 13)], [sp.Rational(12, 13), sp.Rational(-5, 13)]])
    ta_nc = np.array(ta_nc_sp.tolist(), dtype=complex)
    tb_nc = np.array(tb_nc_sp.tolist(), dtype=complex)
    assert joint_fixed_subspace_dim_num(ta_nc, tb_nc, tol=1e-9) == 0
    assert sp.Rational(((sp.eye(2) + ta_nc_sp) * (sp.eye(2) + tb_nc_sp)).trace(), 4) == sp.Rational(9, 13)

    # Independent 35-digit mpmath verification at second modulus tau_alt = 1/4 + i*19/12:
    #   - Weierstrass-Jacobi identities d_z S_k + S_i S_j == 0 and d_z S_k S_i S_j + (wp-e_i)(wp-e_j) == 0,
    #   - Curved hyperbolic cusp measures Omega_metric^{-3/2} d^2z and Omega_metric^{-5/4} d^2z,
    #   - Off-diagonal parity selection (|I_sp| < 1e-20, |I_dp| > 1.0) vs diagonal spin-slot H^0 parity
    #     reversal (|I_sp^diag| > 1.0, |I_dp^diag| < 1e-20) + planted parity-breaking shift control!
    with mp.workdps(35):
        re_alt = mp.mpf(1) / mp.mpf(4)
        im_alt = mp.mpf(19) / mp.mpf(12)
        tau_alt = mp.mpc(re_alt, im_alt)
        q_alt = mp.exp(1j * mp.pi * tau_alt)

        def s_kern(nu_i: int, z_v: mp.mpc) -> mp.mpc:
            return (mp.pi * mp.jtheta(1, 0, q_alt, 1) * mp.jtheta(nu_i, mp.pi * z_v, q_alt)) / (
                mp.jtheta(nu_i, 0, q_alt) * mp.jtheta(1, mp.pi * z_v, q_alt)
            )

        def ds_kern(nu_i: int, z_v: mp.mpc) -> mp.mpc:
            c_p = mp.pi * mp.jtheta(1, 0, q_alt, 1) / mp.jtheta(nu_i, 0, q_alt)
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

        e_alt = {
            2: f_wp(mp.mpc(mp.mpf(1) / mp.mpf(2))),
            3: f_wp((mp.mpc(1) + tau_alt) / mp.mpf(2)),
            4: f_wp(tau_alt / mp.mpf(2)),
        }
        z_test = mp.mpc(mp.mpf(3) / mp.mpf(11), mp.mpf(5) / mp.mpf(13))
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

        n_pts = 12
        th1p_sq = abs(mp.pi * mp.jtheta(1, 0, q_alt, 1)) ** 2
        cell_p = mp.fdiv(im_alt, n_pts * n_pts)
        for k_h, i_f, j_f in [(2, 3, 4), (3, 4, 2), (4, 2, 3)]:
            sp_int = mp.mpc(0)
            dp_int = mp.mpc(0)
            sp_diag = mp.mpc(0)
            dp_diag = mp.mpc(0)
            planted_bad_int = mp.mpc(0)
            for ku_p in range(n_pts):
                u_p = mp.fdiv(2 * ku_p - n_pts + 1, 2 * n_pts)
                for kv_p in range(n_pts):
                    v_p = mp.fdiv(2 * kv_p - n_pts + 1, 2 * n_pts)
                    z_p = mp.mpc(u_p) + mp.mpc(v_p) * tau_alt
                    r2_p = (abs(mp.jtheta(1, mp.pi * z_p, q_alt)) ** 2 / th1p_sq) * mp.exp(-2 * mp.pi * (v_p**2) * im_alt)
                    om_p = mp.mpf(1) / (r2_p * (mp.log(r2_p / mp.mpf(16)) ** 2))
                    om_inv_half = abs(mp.sqrt(mp.mpf(1) / om_p))
                    om_inv_qtr = abs(mp.sqrt(om_inv_half))
                    w_s3 = (om_inv_half**3) * cell_p
                    w_mx = (om_inv_qtr**5) * cell_p
                    sk = s_kern(k_h, z_p)
                    dsk = ds_kern(k_h, z_p)
                    si = s_kern(i_f, z_p)
                    sj = s_kern(j_f, z_p)
                    sp_int += w_s3 * sk * si * mp.conj(sj)
                    dp_int += w_s3 * dsk * si * mp.conj(sj)
                    sp_diag += w_mx * sk * mp.conj(sk)
                    dp_diag += w_mx * dsk * mp.conj(sk)
                    planted_bad_int += w_s3 * s_kern(k_h, z_p + mp.mpf(1) / mp.mpf(6)) * si * mp.conj(sj)
            assert float(abs(sp_int)) < 1e-18
            assert float(abs(dp_int)) > 1.0
            assert float(abs(sp_diag)) > 1.0
            assert float(abs(dp_diag)) < 1e-18
            assert float(abs(planted_bad_int)) > 1e-6

    x_pol = sp.Symbol("x_pol")
    assert sp.degree(sp.cyclotomic_poly(24, x_pol), x_pol) == 8
    assert sp.degree(sp.cyclotomic_poly(5, x_pol), x_pol) == 4
    assert sp.degree(sp.cyclotomic_poly(120, x_pol), x_pol) == 32
    assert wp34["cyclotomic_q24_q5_disjoint_slope_2_5_unforced"] is True


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

    # Independent Pauli Cl(10) symmetric 5-form Georgi-Jarlskog operator in 126bar_s:
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
    for q_w, d_w in [
        ((-1, 1, 1, -1, 1), (1, -1, -1, -1, -1)),
        ((1, -1, 1, -1, 1), (-1, 1, -1, -1, -1)),
        ((1, 1, -1, -1, 1), (-1, -1, 1, -1, -1)),
    ]:
        qd_val = m_gj[weights16.index(q_w), weights16.index(d_w)]
        assert int(abs(sp.simplify(le_val / qd_val))) == 3
    assert wp25["gj_126bar_5form_lepton_to_quark_abs_ratios"] == [3, 3, 3]
    assert wp25["gj_126bar_absent_in_e8_248"] is True

    # Independent 2D Weil Sym^2 construction of BOTH 3_sp (order 96) and 3_dp (order 288 = 12*24):
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
    assert joint_commutant_dim_num([tl_sp, tr_sp], tol=1e-10) == 1
    assert joint_commutant_dim_num([tl_dp, tr_dp], tol=1e-10) == 1
    assert joint_commutant_dim_num([np.block([[tl_sp, z3], [z3, tl_dp]]), np.block([[tr_sp, z3], [z3, tr_dp]])], tol=1e-10) == 2
    assert joint_commutant_dim_num([tl_sp, tr_sp @ tr_sp], tol=1e-10) == 2
    assert wp25["weave_g96_gen_metric_commutant_dim"] == 1
    assert wp25["weave_3dp_gen_metric_commutant_dim"] == 1
    assert wp25["weave_hom_3sp_to_3dp_dim"] == 0
    assert wp25["weave_6d_sp_plus_dp_commutant_dim"] == 2
    assert wp25["weave_3dp_center_and_pg"] == (12, 24)

    # Independent 128D S_16^+ quartic D-term dichotomy check:
    f6_t = [
        kron_l([sx, i2, i2]),
        kron_l([sy, i2, i2]),
        kron_l([sz, sx, i2]),
        kron_l([sz, sy, i2]),
        kron_l([sz, sz, sx]),
        kron_l([sz, sz, sy]),
    ]
    chir6_t = -sp.I * (f6_t[0] * f6_t[1] * f6_t[2] * f6_t[3] * f6_t[4] * f6_t[5])
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
        assert sp.simplify(tr_val / 64 - expected_poly) == 0

    assert wp25["d_term_real_slice_coeff_per_64"] == 8
    assert wp25["d_term_same_h4_posdef_coeff_per_64"] == 16
    assert wp25["d_term_dichotomy_and_real_valley_verified"] is True
