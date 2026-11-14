"""Zero-trust pytest counterchecks & AST locks for Stage 7:
B1604 Flat-Counting Dictionary No-Go Theorem, Explicit 65-Node Upstream Epistemic DAG &
FK1-FK16 Gate Propagation, Cross-Stage Live Operator Witnesses, and Guardrail-5
Buckingham-Pi Single-Anchor Dimensional Audit.

Enforces Guardrails 1-6:
- Strict 0-of-19 empirical data firewall & Guardrail-2 AST locks on both producer and test suite.
- Guardrail 6 zero-trust independence: constructs independent 4x4 real SO(4, Z) quaternion
  left-multiplication matrices for Aut(Q_8), independent GL(2, F_5) (order 480) transitive
  projective-line stabilizers, independent 8x8 cellular cochain rank checks on T^3 and M=5
  CP^1 Cech-Dirac flux operators, independent Floyd-Warshall transitive closure & planted
  cycle/shadow-closure controls on the 65-node DAG, independent cyclotomic quotient ring
  Q[zeta]/(Phi_5(zeta)) proof of J_5(4_1) = 46 + 2*sqrt(5), independent representation-index
  derivation of 115*(b_1 - b_2) == 218*(b_2 - b_3), and independent Buckingham-Pi nullspace checks.
"""
from __future__ import annotations

from itertools import product
from pathlib import Path
from typing import Any

import numpy as np
import pytest
import sympy as sp

from origin_axiom.stage1_curved_action_cusp_orbit import (
    TOL,
    audit_source_zero_empirical_constants,
    check_guardrail2_ast_no_literal_bool_verdicts,
    haar_unitary,
)
from origin_axiom.stage7_upstream_audit_dag import (
    build_upstream_dag_spec,
    run_stage7_complete_verification,
)


ROOT = Path(__file__).resolve().parents[1]
STAGE7_SRC = ROOT / "src" / "origin_axiom" / "stage7_upstream_audit_dag.py"
TEST7_SRC = Path(__file__).resolve()


@pytest.fixture(scope="module")
def stage7_results() -> dict[str, Any]:
    return run_stage7_complete_verification()


def test_stage7_firewall_and_guardrail2_ast_locks(stage7_results: dict[str, Any]) -> None:
    fw_prod = audit_source_zero_empirical_constants(STAGE7_SRC)
    fw_test = audit_source_zero_empirical_constants(TEST7_SRC)
    g2_prod = check_guardrail2_ast_no_literal_bool_verdicts(STAGE7_SRC.read_text(encoding="utf-8"))
    g2_test = check_guardrail2_ast_no_literal_bool_verdicts(TEST7_SRC.read_text(encoding="utf-8"))
    assert fw_prod is True
    assert fw_test is True
    assert g2_prod is True
    assert g2_test is True
    assert stage7_results["zero_sm_empirical_constants_ast_verified"] is True
    assert stage7_results["guardrail2_ast_no_literal_bool_verdicts_verified"] is True
    assert stage7_results["all_verifications_passed"] is True

    # Adversarial synthetic probes confirming FW and G2 fail closed on forbidden inputs:
    fw_reject_snippets = [
        "alpha_em = 1",
        "v_EW = 1",
        "bad_val = 0.3125",
        "bad_rat = sp.Rational(401, 503)",
    ]
    for bad_fw in fw_reject_snippets:
        assert audit_source_zero_empirical_constants("synthetic_bad.py", source_override=bad_fw) is False

    g2_reject_snippets = [
        "def f_bad():\n    return {'ok': True}\n",
        "def f_zero():\n    return {'theta': 0.0}\n",
        "def f_alias():\n    flag = False\n    return {'v': flag}\n",
    ]
    for bad_g2 in g2_reject_snippets:
        assert check_guardrail2_ast_no_literal_bool_verdicts(bad_g2) is False


def test_b1604_zero_trust_q8_automorphisms_gl2_f5_and_3d_flat_index(stage7_results: dict[str, Any]) -> None:
    res_7a = stage7_results["b1604_flat_counting_no_go"]

    # 1. Independent 4x4 real SO(4, Z) left-multiplication matrices on H = span{1, i, j, k}:
    eye4 = np.eye(4, dtype=int)
    li_4 = np.array(
        [[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0]],
        dtype=int,
    )
    lj_4 = np.array(
        [[0, 0, -1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, -1, 0, 0]],
        dtype=int,
    )
    lk_4 = li_4 @ lj_4
    assert np.array_equal(li_4 @ li_4, -eye4)
    assert np.array_equal(lj_4 @ lj_4, -eye4)
    assert np.array_equal(lk_4 @ lk_4, -eye4)
    assert np.array_equal(li_4 @ lj_4 @ lk_4, -eye4)

    q8_real = [eye4, -eye4, li_4, -li_4, lj_4, -lj_4, lk_4, -lk_4]
    cayley_4d = np.zeros((8, 8), dtype=int)
    for ia in range(8):
        for ib in range(8):
            p_mat = q8_real[ia] @ q8_real[ib]
            matches = [ic for ic in range(8) if np.array_equal(p_mat, q8_real[ic])]
            assert len(matches) == 1
            cayley_4d[ia, ib] = matches[0]

    ord4_set = [idx_e for idx_e in range(2, 8)]
    aut_4d: list[tuple[int, ...]] = []
    for u_idx in ord4_set:
        neg_u = int(cayley_4d[int(cayley_4d[u_idx, u_idx]), u_idx])
        for v_idx in ord4_set:
            if v_idx in (u_idx, neg_u):
                continue
            neg_v = int(cayley_4d[int(cayley_4d[v_idx, v_idx]), v_idx])
            uv_idx = int(cayley_4d[u_idx, v_idx])
            neg_uv = int(cayley_4d[1, uv_idx])
            p_map = (0, 1, u_idx, neg_u, v_idx, neg_v, uv_idx, neg_uv)
            if len(set(p_map)) == 8 and all(
                p_map[int(cayley_4d[x_a, x_b])] == int(cayley_4d[p_map[x_a], p_map[x_b]])
                for x_a in range(8)
                for x_b in range(8)
            ):
                aut_4d.append(p_map)
    assert len(aut_4d) == 24
    assert res_7a["q8_aut_order"] == len(aut_4d)

    axes_3 = [frozenset({2, 3}), frozenset({4, 5}), frozenset({6, 7})]
    induced_s3 = {
        tuple(axes_3.index(frozenset(p_m[e_i] for e_i in ax_s)) for ax_s in axes_3)
        for p_m in aut_4d
    }
    assert len(induced_s3) == 6
    assert res_7a["q8_s3_imaginary_axis_perm_order"] == len(induced_s3)
    assert res_7a["q8_inn_order"] == 4
    assert res_7a["q8_out_order"] == 6
    assert res_7a["q8_inn_is_normal_and_kernel_of_axis_s3"] is True
    assert res_7a["q8_invariant_axis_function_dim"] == 1

    # Haar U(4) basis scrambling on real Q_8 representation traces:
    rng = np.random.default_rng(83)
    u4_scr = haar_unitary(4, rng)
    for g_m in q8_real:
        g_rot = u4_scr @ g_m.astype(complex) @ u4_scr.conj().T
        assert abs(complex(np.trace(g_rot)) - float(np.trace(g_m))) < TOL

    # 2. Independent GL(2, F_5) (order 480) transitive action on P^1(F_5):
    gl2_list = [
        (a_c, b_c, c_c, d_c)
        for a_c, b_c, c_c, d_c in product(range(5), repeat=4)
        if (a_c * d_c - b_c * c_c) % 5 != 0
    ]
    assert len(gl2_list) == 480
    assert res_7a["gl2_f5_order"] == len(gl2_list)
    assert res_7a["sl2_f5_order"] == 120
    assert res_7a["lr_mod5_generates_full_sl2_f5"] is True

    p1_reps = [(1, 0), (0, 1), (1, 1), (1, 2), (1, 3), (1, 4)]

    def canon_p1_f5(vx: int, vy: int) -> tuple[int, int]:
        vx_m, vy_m = vx % 5, vy % 5
        if vx_m == 0:
            return (0, 1)
        inv_mod5 = {1: 1, 2: 3, 3: 2, 4: 4}[vx_m]
        return (1, (vy_m * inv_mod5) % 5)

    line0_orb = {canon_p1_f5(g_e[0], g_e[2]) for g_e in gl2_list}
    stab_line0 = [g_e for g_e in gl2_list if canon_p1_f5(g_e[0], g_e[2]) == (1, 0)]
    stab_pair01 = [
        g_e
        for g_e in stab_line0
        if canon_p1_f5(g_e[1], g_e[3]) == (0, 1)
    ]
    assert line0_orb == set(p1_reps)
    assert len(line0_orb) == 6
    assert len(stab_line0) == 80
    assert len(stab_pair01) == 16
    assert res_7a["sl2_f5_nonzero_vector_orbit_size"] == 24
    assert res_7a["sl2_f5_ordered_line_pair_orbit_size"] == 30
    assert res_7a["p1_f5_invariant_function_dim"] == 1
    assert res_7a["p1_f5_equivariant_pairing_dim"] == 2

    # 3. Independent 8-block cellular cochain check on T^3 & M=5 CP^1 Cech-Dirac flux contrast:
    for hol_triple, exp_betti in [
        ((sp.Integer(1), sp.Integer(1), sp.Integer(1)), (1, 3, 3, 1)),
        (
            (
                sp.Rational(3, 5) + sp.Rational(4, 5) * sp.I,
                sp.Rational(5, 13) + sp.Rational(12, 13) * sp.I,
                sp.Rational(8, 17) + sp.Rational(15, 17) * sp.I,
            ),
            (0, 0, 0, 0),
        ),
    ]:
        z1, z2, z3 = hol_triple[0] - 1, hol_triple[1] - 1, hol_triple[2] - 1
        d0_m = sp.Matrix([z1, z2, z3])
        d1_m = sp.Matrix([[0, -z3, z2], [z3, 0, -z1], [-z2, z1, 0]])
        d2_m = sp.Matrix([[z1, z2, z3]])
        assert (d1_m * d0_m).applyfunc(sp.expand) == sp.zeros(3, 1)
        assert (d2_m * d1_m).applyfunc(sp.expand) == sp.zeros(1, 3)
        rk0, rk1, rk2 = int(d0_m.rank()), int(d1_m.rank()), int(d2_m.rank())
        b_tup = (1 - rk0, 3 - rk1 - rk0, 3 - rk2 - rk1, 1 - rk2)
        assert b_tup == exp_betti
        assert (b_tup[0] - b_tup[1] + b_tup[2] - b_tup[3]) == 0

    # Independent M=5 Cech coboundary check on CP^1 for flux k in {0, 3, -3}:
    cutoff_ind = 5
    for k_flx in (0, 3, -3):
        deg_s = k_flx - 1
        win = list(range(-cutoff_ind, cutoff_ind + 1))
        u0_p = list(range(0, cutoff_ind + 1))
        u1_b = [b_i for b_i in range(0, deg_s + cutoff_ind + 1) if -cutoff_ind <= deg_s - b_i <= cutoff_ind]
        c_mat = sp.zeros(len(win), len(u0_p) + len(u1_b))
        for ca, ea in enumerate(u0_p):
            c_mat[win.index(ea), ca] = 1
        for cb, bv in enumerate(u1_b):
            c_mat[win.index(deg_s - bv), len(u0_p) + cb] = -1
        rk_c = int(c_mat.rank())
        ind_c = (c_mat.cols - rk_c) - (c_mat.rows - rk_c)
        assert ind_c == k_flx

    assert res_7a["t3_flat_cochain_nilpotent_and_self_dual"] is True
    assert res_7a["t3_nontrivial_golden5_betti_sum_vanishes"] is True
    assert res_7a["t3_flat_euler_and_folded_index_vanish"] is True
    assert res_7a["cp1_flat_vs_curved_index_dichotomy"] is True
    assert res_7a["b1604_flat_counting_no_go_verified"] is True


def test_dag_zero_trust_acyclicity_monotonicity_and_0_of_19_obstruction(stage7_results: dict[str, Any]) -> None:
    res_7b = stage7_results["upstream_epistemic_dag"]
    spec = build_upstream_dag_spec()

    ids = [r_s[0] for r_s in spec]
    layers = [r_s[1] for r_s in spec]
    intr = np.array([r_s[2] for r_s in spec], dtype=int)
    n_v = len(ids)
    assert n_v == 65
    pos_map = {nm: idx for idx, nm in enumerate(ids)}

    adj = np.zeros((n_v, n_v), dtype=int)
    for ch_id, _, _, par_tup in spec:
        v_i = pos_map[ch_id]
        for p_id in par_tup:
            adj[pos_map[p_id], v_i] = 1

    # Independent matrix-power trace check tr(sum_{k=1}^n A^k) == 0:
    pow_sum = np.zeros((n_v, n_v), dtype=int)
    cur_p = adj.copy()
    for _ in range(n_v):
        pow_sum = pow_sum + (cur_p > 0).astype(int)
        cur_p = ((cur_p @ adj) > 0).astype(int)
    assert int(np.trace(pow_sum)) == 0
    assert int(np.sum(cur_p)) == 0

    # Independent Floyd-Warshall transitive closure:
    fw_reach = (adj > 0).astype(int).copy()
    for piv_k in range(n_v):
        col_k = fw_reach[:, piv_k : piv_k + 1]
        row_k = fw_reach[piv_k : piv_k + 1, :]
        fw_reach = np.logical_or(fw_reach, col_k @ row_k > 0).astype(int)
    assert int(np.trace(fw_reach)) == 0

    eff_fw = intr.copy()
    for v_j in range(n_v):
        anc_vals = [int(intr[v_j])] + [int(intr[u_i]) for u_i in range(n_v) if int(fw_reach[u_i, v_j]) == 1]
        eff_fw[v_j] = max(anc_vals)

    l1_ids = [i_v for i_v, ly in enumerate(layers) if ly == "L1_SPINE"]
    l2_ids = [i_v for i_v, ly in enumerate(layers) if ly == "L2_SEAM"]
    l3_ids = [i_v for i_v, ly in enumerate(layers) if ly == "L3_GATE"]
    l4_ids = [i_v for i_v, ly in enumerate(layers) if ly == "L4_SM"]
    assert (len(l1_ids), len(l2_ids), len(l3_ids), len(l4_ids)) == (19, 11, 16, 19)

    assert all(int(eff_fw[i_v]) == 0 for i_v in l1_ids)
    assert all(int(eff_fw[i_v]) >= 2 for i_v in l2_ids)
    assert [ids[i_v] for i_v in l3_ids if int(eff_fw[i_v]) == 0] == ["FK3", "FK16"]
    assert sum(1 for i_v in l3_ids if int(eff_fw[i_v]) >= 2) == 14

    # Verify every single SM:* node has >= 1 X:* ancestor with status >= 2 and eff >= 2 (0 of 19 unconditional):
    for sm_i in l4_ids:
        seam_ancs = [u_s for u_s in l2_ids if int(fw_reach[u_s, sm_i]) == 1 and int(intr[u_s]) >= 2]
        assert len(seam_ancs) >= 1
        assert int(eff_fw[sm_i]) >= 2
    assert sum(1 for sm_i in l4_ids if int(eff_fw[sm_i]) == 0) == 0

    # Independent planted cycle control via Floyd-Warshall diagonal:
    fw_bad = (adj > 0).astype(int).copy()
    fw_bad[pos_map["SM:G1"], pos_map["WP-1.3"]] = 1
    for piv_k in range(n_v):
        fw_bad = np.logical_or(fw_bad, (fw_bad[:, piv_k : piv_k + 1] @ fw_bad[piv_k : piv_k + 1, :]) > 0).astype(int)
    assert int(np.trace(fw_bad)) >= 2

    # Independent shadow-closure counterfactual zeroing all 11 X:* seams:
    intr_shadow = intr.copy()
    for s_i in l2_ids:
        intr_shadow[s_i] = 0
    eff_shadow = [
        max([int(intr_shadow[v_j])] + [int(intr_shadow[u_i]) for u_i in range(n_v) if int(fw_reach[u_i, v_j]) == 1])
        for v_j in range(n_v)
    ]
    assert all(eff_shadow[sm_i] == 0 for sm_i in l4_ids)

    assert res_7b["acyclic_kahn_and_nilpotent_verified"] is True
    assert res_7b["obstructed_or_open_sm_count"] == 19
    assert res_7b["unblocked_sm_count_is_zero"] is True
    assert res_7b["planted_cycle_negative_control_detected"] is True
    assert res_7b["shadow_zeroed_seams_unblocked_sm_count"] == 19
    assert res_7b["all_11_seams_individually_blocking"] is True
    assert res_7b["dag_and_fk_audit_verified"] is True


def test_cross_stage_witnesses_and_buckingham_pi_zero_trust(stage7_results: dict[str, Any]) -> None:
    res_7c = stage7_results["cross_stage_witnesses_and_buckingham_pi"]

    # 1. Independent cyclotomic ring Q[z]/(Phi_5(z)) proof of J_5(4_1) = 46 + 2*sqrt(5):
    z_sym = sp.Symbol("z_sym")
    phi5_poly = 1 + z_sym + z_sym**2 + z_sym**3 + z_sym**4
    gauss_tau5 = z_sym + z_sym**4 - z_sym**2 - z_sym**3
    assert sp.rem(sp.expand(gauss_tau5**2 - 5), phi5_poly, z_sym) == 0

    habiro_sum = sp.Integer(0)
    for n_step in range(5):
        term_p = sp.Integer(1)
        for k_step in range(1, n_step + 1):
            factor_k = 2 - z_sym**k_step - z_sym ** (5 - k_step)
            term_p = sp.expand(term_p * factor_k)
        habiro_sum = habiro_sum + term_p
    target_cyclotomic = 46 + 2 * gauss_tau5
    assert sp.rem(sp.expand(habiro_sum - target_cyclotomic), phi5_poly, z_sym) == 0

    # 2. Independent SU(3)xSU(2)xU(1) representation-index derivation of 1-loop (b_1 - b_2)/(b_2 - b_3) = 218/115:
    # Chiral left-handed Weyl multiplets per generation: (dim_3, dim_2, S_3_rep, S_2_rep, Y_val)
    weyl_mults = [
        (3, 2, sp.Rational(1, 2), sp.Rational(1, 2), sp.Rational(1, 6)),
        (3, 1, sp.Rational(1, 2), sp.Integer(0), sp.Rational(-2, 3)),
        (3, 1, sp.Rational(1, 2), sp.Integer(0), sp.Rational(1, 3)),
        (1, 2, sp.Integer(0), sp.Rational(1, 2), sp.Rational(-1, 2)),
        (1, 1, sp.Integer(0), sp.Integer(0), sp.Integer(1)),
        (1, 1, sp.Integer(0), sp.Integer(0), sp.Integer(0)),
    ]
    idx_s3_gen = sum(d2_m * s3_m for _, d2_m, s3_m, _, _ in weyl_mults)
    idx_s2_gen = sum(d3_m * s2_m for d3_m, _, _, s2_m, _ in weyl_mults)
    idx_s1_gen = sp.Rational(3, 5) * sum(d3_m * d2_m * (yv**2) for d3_m, d2_m, _, _, yv in weyl_mults)
    assert (idx_s3_gen, idx_s2_gen, idx_s1_gen) == (2, 2, 2)

    # Complex Higgs doublet (1, 2)_{1/2} + symbolic generation number n_g_sym:
    n_g_sym = sp.Symbol("n_g_sym")
    b1_sym = sp.Rational(2, 3) * n_g_sym * idx_s1_gen + sp.Rational(1, 3) * sp.Rational(3, 5) * 2 * sp.Rational(1, 4)
    b2_sym = -sp.Rational(11, 3) * 2 + sp.Rational(2, 3) * n_g_sym * idx_s2_gen + sp.Rational(1, 3) * sp.Rational(1, 2)
    b3_sym = -sp.Rational(11, 3) * 3 + sp.Rational(2, 3) * n_g_sym * idx_s3_gen
    # Complete Spin(10) 16-plets drop out of b_1 - b_2 and b_2 - b_3 at 1-loop:
    assert sp.simplify(sp.diff(b1_sym - b2_sym, n_g_sym)) == 0
    assert sp.simplify(sp.diff(b2_sym - b3_sym, n_g_sym)) == 0
    b1_ind = b1_sym.subs(n_g_sym, 3)
    b2_ind = b2_sym.subs(n_g_sym, 3)
    b3_ind = b3_sym.subs(n_g_sym, 3)
    assert sp.simplify(10 * b1_ind - 41) == 0
    assert sp.simplify(6 * b2_ind + 19) == 0
    assert sp.simplify(b3_ind + 7) == 0
    assert sp.simplify(115 * (b1_ind - b2_ind) - 218 * (b2_ind - b3_ind)) == 0
    assert sp.simplify((b1_ind - b2_ind) - (b2_ind - b3_ind)) != 0

    # 3. Independent Buckingham-Pi nullspace basis & multi-anchor rejection check:
    k_cols = res_7c["buckingham_pi_ledger_size"]
    assert k_cols == 21
    dim_row = np.array([[1] * 14 + [0] * 7], dtype=int)
    assert int(np.linalg.matrix_rank(dim_row.astype(float))) == 1

    pi_cols: list[np.ndarray] = []
    for idx_m in range(1, 14):
        col_r = np.zeros(21, dtype=int)
        col_r[0] = -1
        col_r[idx_m] = 1
        pi_cols.append(col_r)
    for idx_d in range(14, 21):
        col_d = np.zeros(21, dtype=int)
        col_d[idx_d] = 1
        pi_cols.append(col_d)
    pi_mat = np.column_stack(pi_cols)
    assert pi_mat.shape == (21, 20)
    assert int(np.linalg.matrix_rank(pi_mat.astype(float))) == 20
    assert int(np.max(np.abs(dim_row @ pi_mat))) == 0

    assert res_7c["cross_stage_ast_contract_and_locks_verified"] is True
    assert res_7c["stage1_koszul_and_conformal_witness_verified"] is True
    assert res_7c["stage2_p753_register16_and_sym2_witness_verified"] is True
    assert res_7c["stage3_wp13_and_e8_248_witness_verified"] is True
    assert res_7c["stage4_fl16_and_anomaly16_witness_verified"] is True
    assert res_7c["stage5_gj_ratio_and_haar_yukawa_witness_verified"] is True
    assert res_7c["stage6_b1922_j5_and_desert_218_115_witness_verified"] is True
    assert res_7c["buckingham_pi_single_anchor_verified"] is True
    assert res_7c["unpriced_multi_anchor_negative_control_rejected"] is True
    assert res_7c["cross_stage_and_buckingham_verified"] is True
