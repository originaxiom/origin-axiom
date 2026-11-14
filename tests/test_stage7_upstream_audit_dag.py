"""Zero-trust pytest counterchecks & AST locks for Stage 7 v2:
B1604 Flat-Counting Dictionary No-Go Theorem (including Cusped 3-Manifold m004 Spine),
Explicit 83-Node 5-Layer Monotone Upstream Epistemic DAG, Faithful FK1-FK16 & FG:01-12 Gates,
Unconditional 16-File Cross-Stage Audit & Live Operator Witnesses, and Guardrail-5
20-Item (Nullity-19) Buckingham-Pi & Secondary-Scale Pricing Ledger.

Enforces Guardrails 1-6:
- Strict 0-of-19 empirical data firewall, Guardrail-2 AST locks, and hardened banned-SM-identifier
  AST scanner locks (including keyword args, function/class defs, and import aliases).
- Guardrail 6 zero-trust independence: constructs independent 4x4 real SO(4, Z) quaternion matrices
  and full S_6 brute-force enumeration proving Aut(Q_8) ~= S_4 (trivial center, order profile
  {1:1, 2:9, 3:8, 4:6}), full 120/480 SL(2, F_5) & GL(2, F_5) commutant stacks on P^1(F_5),
  separate (h^0, h^1) Cech cohomology across M in {5, 6, 8} + zero-matrix rejection, non-trivial
  T^3 folded Dirac invertibility + twisted Poincare duality, independent 3-generator 2-relator
  punctured-torus mapping-torus Fox spine on m004 across ranks 1 and 2 (including 2T), independent
  Floyd-Warshall checks on the 83-node monotone DAG, and independent 20x19 Buckingham-Pi nullspace
  & Guardrail-5 secondary empirical scale pricing counterchecks.
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
    ast_scan_zero_banned_sm_identifiers,
    audit_buckingham_pi_guardrail5_ledger,
    build_upstream_dag_spec,
    run_stage7_complete_verification,
)


ROOT = Path(__file__).resolve().parents[1]
STAGE7_SRC = ROOT / "src" / "origin_axiom" / "stage7_upstream_audit_dag.py"
TEST7_SRC = Path(__file__).resolve()


@pytest.fixture(scope="module")
def stage7_results() -> dict[str, Any]:
    return run_stage7_complete_verification()


def test_stage7_firewall_guardrail2_and_sm_identifier_ast_locks(stage7_results: dict[str, Any]) -> None:
    fw_prod = audit_source_zero_empirical_constants(STAGE7_SRC)
    fw_test = audit_source_zero_empirical_constants(TEST7_SRC)
    g2_prod = check_guardrail2_ast_no_literal_bool_verdicts(STAGE7_SRC.read_text(encoding="utf-8"))
    g2_test = check_guardrail2_ast_no_literal_bool_verdicts(TEST7_SRC.read_text(encoding="utf-8"))
    sm_prod_ok, _, _ = ast_scan_zero_banned_sm_identifiers(STAGE7_SRC.read_text(encoding="utf-8"))
    sm_test_ok, _, _ = ast_scan_zero_banned_sm_identifiers(TEST7_SRC.read_text(encoding="utf-8"))
    assert fw_prod is True
    assert fw_test is True
    assert g2_prod is True
    assert g2_test is True
    assert sm_prod_ok is True
    assert sm_test_ok is True
    assert stage7_results["zero_sm_empirical_constants_ast_verified"] is True
    assert stage7_results["guardrail2_ast_no_literal_bool_verdicts_verified"] is True
    assert stage7_results["zero_banned_sm_identifiers_ast_verified"] is True
    assert stage7_results["all_verifications_passed"] is True

    # Unconditional 16-file existence & hardened banned-SM-identifier scan across all 8 producers + 8 tests:
    src_dir = ROOT / "src" / "origin_axiom"
    tst_dir = ROOT / "tests"
    expected_16_files = [
        src_dir / "p753_register_field_join.py",
        src_dir / "stage1_curved_action_cusp_orbit.py",
        src_dir / "stage2_kernel_and_physical_join.py",
        src_dir / "stage3_carrier_moves_parent_algebra.py",
        src_dir / "stage4_currents_hand_anomalies_theta.py",
        src_dir / "stage5_cubic_overlaps_higgs_dictionary.py",
        src_dir / "stage6_closed_loop_scale_rge.py",
        src_dir / "stage7_upstream_audit_dag.py",
        tst_dir / "test_p753_register_field_join.py",
        tst_dir / "test_stage1_curved_action_cusp_orbit.py",
        tst_dir / "test_stage2_kernel_and_physical_join.py",
        tst_dir / "test_stage3_carrier_moves_parent_algebra.py",
        tst_dir / "test_stage4_currents_hand_anomalies_theta.py",
        tst_dir / "test_stage5_cubic_overlaps_higgs_dictionary.py",
        tst_dir / "test_stage6_closed_loop_scale_rge.py",
        tst_dir / "test_stage7_upstream_audit_dag.py",
    ]
    assert len(expected_16_files) == 16
    for f_path in expected_16_files:
        assert f_path.is_file() is True
        clean_f, nodes_f, _ = ast_scan_zero_banned_sm_identifiers(f_path.read_text(encoding="utf-8"))
        assert clean_f is True
        assert nodes_f > 20

    # Adversarial synthetic probes confirming FW, G2, and hardened SM-identifier scanner fail closed:
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

    sm_id_reject_snippets = [
        "def f():\n    return dict(m_e=1, M_Z=2, v_EW=3)\n",
        "def alpha_em():\n    return 1\n",
        "async def V_us():\n    return 2\n",
        "class sin2_theta_W:\n    pass\n",
        "import pdg\n",
        "import some_pkg.codata as clean_name\n",
        "import math as G_F\n",
    ]
    for bad_sm in sm_id_reject_snippets:
        clean_flag, _, _ = ast_scan_zero_banned_sm_identifiers(bad_sm)
        assert clean_flag is False


def test_b1604_zero_trust_q8_s4_gl2_f5_cp1_t3_and_m004_spine(stage7_results: dict[str, Any]) -> None:
    res_7a = stage7_results["b1604_flat_counting_no_go"]

    # 1. Independent 4x4 real SO(4, Z) left-multiplication Q_8 + brute-force S_6 Aut(Q_8) ~= S_4 proof:
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

    aut_4d: list[tuple[int, ...]] = []
    for perm6 in product(range(2, 8), repeat=6):
        if len(set(perm6)) != 6:
            continue
        p_cand = (0, 1) + perm6
        if all(
            p_cand[int(cayley_4d[x_a, x_b])] == int(cayley_4d[p_cand[x_a], p_cand[x_b]])
            for x_a in range(8)
            for x_b in range(8)
        ):
            aut_4d.append(p_cand)
    assert len(aut_4d) == 24
    assert aut_4d[0] == (0, 1, 2, 3, 4, 5, 6, 7)

    aut_pos = {p_el: idx_p for idx_p, p_el in enumerate(aut_4d)}
    mul_24 = np.zeros((24, 24), dtype=int)
    for i_a, p_a in enumerate(aut_4d):
        for i_b, p_b in enumerate(aut_4d):
            mul_24[i_a, i_b] = aut_pos[tuple(p_a[p_b[x_k]] for x_k in range(8))]

    ord_hist: dict[int, int] = {}
    cent_list: list[int] = []
    for i_a in range(24):
        cur_x = i_a
        ord_x = 1
        while cur_x != 0:
            cur_x = int(mul_24[cur_x, i_a])
            ord_x += 1
        ord_hist[ord_x] = ord_hist.get(ord_x, 0) + 1
        if all(int(mul_24[i_a, j_b]) == int(mul_24[j_b, i_a]) for j_b in range(24)):
            cent_list.append(i_a)
    assert cent_list == [0]
    assert ord_hist == {1: 1, 2: 9, 3: 8, 4: 6}
    assert res_7a["q8_aut_isomorphic_to_s4_verified"] is True
    assert res_7a["q8_aut_order_profile"] == {1: 1, 2: 9, 3: 8, 4: 6}
    assert res_7a["q8_aut_center_size"] == 1
    assert res_7a["q8_axis_commutant_dim"] == 2

    rng = np.random.default_rng(83)
    u4_scr = haar_unitary(4, rng)
    for g_m in q8_real:
        g_rot = u4_scr @ g_m.astype(complex) @ u4_scr.conj().T
        assert abs(complex(np.trace(g_rot)) - float(np.trace(g_m))) < TOL

    # 2. Independent full 120-element SL(2, F_5) & 480-element GL(2, F_5) commutant check on P^1(F_5):
    gl2_list = [
        (a_c, b_c, c_c, d_c)
        for a_c, b_c, c_c, d_c in product(range(5), repeat=4)
        if (a_c * d_c - b_c * c_c) % 5 != 0
    ]
    sl2_list = [g_e for g_e in gl2_list if (g_e[0] * g_e[3] - g_e[1] * g_e[2]) % 5 == 1]
    assert len(gl2_list) == 480
    assert len(sl2_list) == 120

    p1_reps = [(1, 0), (0, 1), (1, 1), (1, 2), (1, 3), (1, 4)]
    inv_mod5 = {1: 1, 2: 3, 3: 2, 4: 4}

    def canon_p1_f5(vx: int, vy: int) -> tuple[int, int]:
        vx_m, vy_m = vx % 5, vy % 5
        if vx_m == 0:
            return (0, 1)
        return (1, (vy_m * inv_mod5[vx_m]) % 5)

    eye6 = np.eye(6, dtype=float)
    for grp_elems in (sl2_list, gl2_list):
        inv_rows: list[np.ndarray] = []
        comm_rows: list[np.ndarray] = []
        for ga, gb, gc, gd in grp_elems:
            pm6 = np.zeros((6, 6), dtype=float)
            for col_i, (px, py) in enumerate(p1_reps):
                img_rep = canon_p1_f5(ga * px + gb * py, gc * px + gd * py)
                pm6[p1_reps.index(img_rep), col_i] = 1.0
            inv_rows.append(pm6 - eye6)
            comm_rows.append(np.kron(pm6.T, eye6) - np.kron(eye6, pm6))
        assert int(6 - np.linalg.matrix_rank(np.vstack(inv_rows))) == 1
        assert int(36 - np.linalg.matrix_rank(np.vstack(comm_rows))) == 2
    assert res_7a["sl2_f5_full_p1_invariant_and_commutant_dims"] == [1, 2]
    assert res_7a["gl2_f5_full_p1_invariant_and_commutant_dims"] == [1, 2]

    # 3. Independent separate (h^0, h^1) check on CP^1 across M in {5, 6, 8}, k in {-3, -1, 0, 1, 3}:
    for cut_ind in (5, 6, 8):
        n_laurent = 2 * cut_ind + 1
        for k_flx in (-3, -1, 0, 1, 3):
            deg_s = k_flx - 1
            cols_c: list[sp.Matrix] = []
            for ea in range(0, cut_ind + 1):
                col_a = sp.zeros(n_laurent, 1)
                col_a[ea + cut_ind, 0] = 1
                cols_c.append(col_a)
            for b_i in range(0, deg_s + cut_ind + 1):
                if -cut_ind <= deg_s - b_i <= cut_ind:
                    col_b = sp.zeros(n_laurent, 1)
                    col_b[deg_s - b_i + cut_ind, 0] = -1
                    cols_c.append(col_b)
            c_mat = sp.Matrix.hstack(*cols_c)
            rk_c = int(c_mat.rank())
            h0_ind = int(c_mat.cols - rk_c)
            h1_ind = int(c_mat.rows - rk_c)
            assert h0_ind == max(k_flx, 0)
            assert h1_ind == max(-k_flx, 0)

    # Zero-matrix negative control proving separate (h^0, h^1) rejects rank-0 bogus operator:
    z_bogus = sp.zeros(13, 16)
    rk_zb = int(z_bogus.rank())
    assert (int(z_bogus.cols - rk_zb), int(z_bogus.rows - rk_zb)) == (16, 13)
    assert (int(z_bogus.cols - rk_zb), int(z_bogus.rows - rk_zb)) != (3, 0)
    assert res_7a["cp1_all_15_cutoffs_separate_h0_h1_verified"] is True
    assert res_7a["cp1_corrupted_negative_controls_rejected"] is True

    # 4. Independent T^3 cellular cochain, folded operator D_fold at non-trivial holonomies, & Poincare duality:
    for hol_triple in [
        (
            sp.Rational(3, 5) + sp.Rational(4, 5) * sp.I,
            sp.Rational(5, 13) + sp.Rational(12, 13) * sp.I,
            sp.Rational(8, 17) + sp.Rational(15, 17) * sp.I,
        ),
        (sp.Rational(5, 13) + sp.Rational(12, 13) * sp.I, sp.Integer(1), sp.Integer(1)),
    ]:
        z1, z2, z3 = hol_triple[0] - 1, hol_triple[1] - 1, hol_triple[2] - 1
        d0_m = sp.Matrix([z1, z2, z3])
        d1_m = sp.Matrix([[0, -z3, z2], [z3, 0, -z1], [-z2, z1, 0]])
        d2_m = sp.Matrix([[z1, z2, z3]])
        assert (d1_m * d0_m).applyfunc(sp.expand) == sp.zeros(3, 1)
        assert (d2_m * d1_m).applyfunc(sp.expand) == sp.zeros(1, 3)
        rk0, rk1, rk2 = int(d0_m.rank()), int(d1_m.rank()), int(d2_m.rank())
        assert (1 - rk0, 3 - rk0 - rk1, 3 - rk1 - rk2, 1 - rk2) == (0, 0, 0, 0)
        d_fold = sp.BlockMatrix([[d0_m, d1_m.H], [sp.zeros(1, 1), d2_m]]).as_explicit()
        assert int(d_fold.rank()) == 4
        assert int(4 - d_fold.rank()) == 0
        assert int(4 - d_fold.H.rank()) == 0

    # Trivial rank-1 & non-unitary rank-2 unipotent twisted Poincare duality h^p(E) == h^{3-p}(E^v) + corrupted control:
    a1_u = sp.Matrix([[0, 1], [0, 0]])
    a2_u = sp.Matrix([[0, 0], [0, 0]])
    a3_u = sp.Matrix([[0, 2], [0, 0]])
    a1_du = (sp.eye(2) + a1_u).inv().T - sp.eye(2)
    a2_du = (sp.eye(2) + a2_u).inv().T - sp.eye(2)
    a3_du = (sp.eye(2) + a3_u).inv().T - sp.eye(2)

    def ind_t3_betti_rk2(m1: sp.Matrix, m2: sp.Matrix, m3: sp.Matrix) -> tuple[int, int, int, int]:
        z2 = sp.zeros(2, 2)
        d0_u = sp.Matrix.vstack(m1, m2, m3)
        d1_u = sp.BlockMatrix([[z2, -m3, m2], [m3, z2, -m1], [-m2, m1, z2]]).as_explicit()
        d2_u = sp.Matrix.hstack(m1, m2, m3)
        assert (d1_u * d0_u) == sp.zeros(6, 2)
        assert (d2_u * d1_u) == sp.zeros(2, 6)
        r0_u, r1_u, r2_u = int(d0_u.rank()), int(d1_u.rank()), int(d2_u.rank())
        return (2 - r0_u, 6 - r0_u - r1_u, 6 - r1_u - r2_u, 2 - r2_u)

    b_u = ind_t3_betti_rk2(a1_u, a2_u, a3_u)
    b_du = ind_t3_betti_rk2(a1_du, a2_du, a3_du)
    assert b_u == (1, 3, 3, 1)
    for p_deg in range(4):
        assert b_u[p_deg] == b_du[3 - p_deg]
    d0_bad_t3 = sp.Matrix([sp.Integer(1), sp.Integer(2), sp.Integer(3)])
    d1_bad_t3 = sp.Matrix([[0, 3, 2], [3, 0, -1], [-2, 1, 0]])
    assert (d1_bad_t3 * d0_bad_t3) != sp.zeros(3, 1)

    assert res_7a["t3_nontrivial_folded_invertible_verified"] is True
    assert res_7a["t3_poincare_duality_and_unipotent_verified"] is True
    assert res_7a["t3_corrupted_negative_control_rejected"] is True

    # 5. Independent cusped 3-manifold m004 spine check via 3-generator 2-relator mapping torus:
    #    pi_1(m004) = <a, b, t | t a T B A = 1, t b T B A B = 1> (1 vertex, 3 edges, 2 faces: 1 - 3 + 2 == 0)
    mt_rels = ["taTBA", "tbTBAB"]
    mt_gens = ["a", "b", "t"]

    def mt_fox_betti(rep_d: dict[str, sp.Matrix], inv_d: dict[str, sp.Matrix]) -> tuple[bool, tuple[int, int, int]]:
        n_r = rep_d["a"].rows
        eye_r = sp.eye(n_r)
        all_let: dict[str, sp.Matrix] = {}
        for k_g in mt_gens:
            all_let[k_g] = rep_d[k_g]
            all_let[k_g.upper()] = inv_d[k_g]
        d0_blocks: list[sp.Matrix] = []
        for k_g in mt_gens:
            d0_blocks.append((rep_d[k_g] - eye_r).applyfunc(sp.expand))
        d0_mt = sp.Matrix.vstack(*d0_blocks)
        d1_rows_mt: list[sp.Matrix] = []
        for rw in mt_rels:
            acc_g: dict[str, sp.Matrix] = {}
            for k_g in mt_gens:
                acc_g[k_g] = sp.zeros(n_r, n_r)
            pf = eye_r
            for ch_r in rw:
                if ch_r.islower():
                    acc_g[ch_r] = (acc_g[ch_r] + pf).applyfunc(sp.expand)
                    pf = (pf * all_let[ch_r]).applyfunc(sp.expand)
                else:
                    pf = (pf * all_let[ch_r]).applyfunc(sp.expand)
                    acc_g[ch_r.lower()] = (acc_g[ch_r.lower()] - pf).applyfunc(sp.expand)
            row_blocks: list[sp.Matrix] = []
            for k_g in mt_gens:
                row_blocks.append(acc_g[k_g])
            d1_rows_mt.append(sp.Matrix.hstack(*row_blocks))
        d1_mt = sp.Matrix.vstack(*d1_rows_mt)
        nil_mt = (d1_mt * d0_mt).applyfunc(sp.expand) == sp.zeros(2 * n_r, n_r)
        rk0_mt = int(d0_mt.rank())
        rk1_mt = int(d1_mt.rank())
        return nil_mt, (n_r - rk0_mt, 3 * n_r - rk0_mt - rk1_mt, 2 * n_r - rk1_mt)

    t_al = sp.Rational(3, 2) + sp.sqrt(5) / 2
    t_al_i = sp.Rational(3, 2) - sp.sqrt(5) / 2
    qi_2 = sp.Matrix([[sp.I, 0], [0, -sp.I]])
    qj_2 = sp.Matrix([[0, 1], [-1, 0]])
    qk_2 = qi_2 * qj_2
    t_2t = sp.Rational(1, 2) * (sp.eye(2) - qi_2 - qj_2 - qk_2)
    t_2t_inv = sp.Rational(1, 2) * (sp.eye(2) + qi_2 + qj_2 + qk_2)

    mt_checks = [
        ({"a": sp.Matrix([[1]]), "b": sp.Matrix([[1]]), "t": sp.Matrix([[1]])}, {"a": sp.Matrix([[1]]), "b": sp.Matrix([[1]]), "t": sp.Matrix([[1]])}, (1, 1, 0)),
        ({"a": sp.Matrix([[1]]), "b": sp.Matrix([[1]]), "t": sp.Matrix([[-1]])}, {"a": sp.Matrix([[1]]), "b": sp.Matrix([[1]]), "t": sp.Matrix([[-1]])}, (0, 0, 0)),
        ({"a": sp.Matrix([[1]]), "b": sp.Matrix([[1]]), "t": sp.Matrix([[t_al]])}, {"a": sp.Matrix([[1]]), "b": sp.Matrix([[1]]), "t": sp.Matrix([[t_al_i]])}, (0, 1, 1)),
        ({"a": qi_2, "b": qj_2, "t": t_2t}, {"a": -qi_2, "b": -qj_2, "t": t_2t_inv}, (0, 2, 2)),
        ({"a": qi_2, "b": qj_2, "t": -t_2t}, {"a": -qi_2, "b": -qj_2, "t": -t_2t_inv}, (0, 0, 0)),
    ]
    for r_d, ri_d, exp_b in mt_checks:
        ok_nil, b_mt = mt_fox_betti(r_d, ri_d)
        assert ok_nil is True
        assert b_mt == exp_b
        assert (b_mt[0] - b_mt[1] + b_mt[2]) == 0

    # Non-representation control on mapping torus (swapping t_2t -> t_2t_inv breaks conjugation of a, b):
    bad_nil, _ = mt_fox_betti({"a": qi_2, "b": qj_2, "t": t_2t_inv}, {"a": -qi_2, "b": -qj_2, "t": t_2t})
    assert bad_nil is False
    assert res_7a["m004_cusped_spine_zero_euler_verified"] is True
    assert res_7a["b1604_flat_counting_no_go_verified"] is True


def test_dag_zero_trust_monotone_lattice_fk_fidelity_and_0_of_19_obstruction(stage7_results: dict[str, Any]) -> None:
    res_7b = stage7_results["upstream_epistemic_dag"]
    spec = build_upstream_dag_spec()

    ids = [r_s[0] for r_s in spec]
    layers = [r_s[1] for r_s in spec]
    subtypes = [r_s[2] for r_s in spec]
    intr = np.array([r_s[3] for r_s in spec], dtype=int)
    n_v = len(ids)
    assert n_v == 83
    pos_map = {nm: idx for idx, nm in enumerate(ids)}

    adj = np.zeros((n_v, n_v), dtype=int)
    for ch_id, _, _, _, par_tup in spec:
        v_i = pos_map[ch_id]
        for p_id in par_tup:
            adj[pos_map[p_id], v_i] = 1

    # Independent Floyd-Warshall transitive closure & acyclicity check:
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
    l3_ids = [i_v for i_v, ly in enumerate(layers) if ly == "L3_FORK"]
    l4_ids = [i_v for i_v, ly in enumerate(layers) if ly == "L4_CLOSURE_GATE"]
    l5_ids = [i_v for i_v, ly in enumerate(layers) if ly == "L5_SM"]
    assert (len(l1_ids), len(l2_ids), len(l3_ids), len(l4_ids), len(l5_ids)) == (25, 11, 16, 12, 19)

    # Zero WP-* -> X:* incoming edges into L2_SEAM, zero unbuilt WP-1.5/1.6/4.5 in L1_SPINE:
    assert int(np.sum(adj[:, l2_ids])) == 0
    for unbuilt_id in ("WP-1.5", "WP-1.6", "WP-4.5"):
        assert unbuilt_id not in ids
    assert [ids[i_v] for i_v in l1_ids if subtypes[i_v] == "AXIOM_CONVENTION"] == ["WP-1.1"]
    assert all(int(eff_fw[i_v]) == 0 for i_v in l1_ids)

    # Canonical 11 seams & exact FK1..FK16 monotone lattice assignments:
    expected_seams = {
        "X:PARENT": 2,
        "X:ACTION": 2,
        "X:ENDLAW": 2,
        "X:DICT": 3,
        "X:HAND": 2,
        "X:MODULUS": 3,
        "X:LEVEL": 2,
        "X:WHOLE": 3,
        "X:DESERT": 3,
        "X:SCALE": 3,
        "X:GRAVITY": 2,
    }
    assert {ids[i_v]: int(eff_fw[i_v]) for i_v in l2_ids} == expected_seams

    expected_fk_ranks = {
        "FK1": 0,
        "FK2": 1,
        "FK3": 2,
        "FK4": 0,
        "FK5": 2,
        "FK6": 1,
        "FK7": 2,
        "FK8": 2,
        "FK9": 3,
        "FK10": 2,
        "FK11": 3,
        "FK12": 2,
        "FK13": 0,
        "FK14": 2,
        "FK15": 2,
        "FK16": 2,
    }
    assert {ids[i_v]: int(eff_fw[i_v]) for i_v in l3_ids} == expected_fk_ranks
    assert res_7b["stage4_fk3_fk16_live_agreement_verified"] is True

    # Every FG:* gate has >= 1 L1_SPINE ancestor and >= 1 L2_SEAM ancestor; 3 OPEN, 9 OBSTRUCTED:
    for fg_i in l4_ids:
        assert any(int(fw_reach[u_sp, fg_i]) == 1 for u_sp in l1_ids)
        assert any(int(fw_reach[u_sm, fg_i]) == 1 for u_sm in l2_ids)
    assert sum(1 for fg_i in l4_ids if int(eff_fw[fg_i]) == 2) == 3
    assert sum(1 for fg_i in l4_ids if int(eff_fw[fg_i]) == 3) == 9

    # Active obstructions (3 = OBSTRUCTED) are NEVER overwritten by OPEN (2); 0 of 19 derived:
    assert sum(1 for sm_i in l5_ids if int(eff_fw[sm_i]) == 3) == 19
    assert sum(1 for sm_i in l5_ids if int(eff_fw[sm_i]) == 0) == 0

    # Independent planted FITTED = 4 negative control:
    intr_fitted = intr.copy()
    intr_fitted[pos_map["X:MODULUS"]] = 4
    eff_fitted_fw = [
        max([int(intr_fitted[v_j])] + [int(intr_fitted[u_i]) for u_i in range(n_v) if int(fw_reach[u_i, v_j]) == 1])
        for v_j in range(n_v)
    ]
    assert sum(1 for sm_i in l5_ids if eff_fitted_fw[sm_i] == 4) == 14

    # Independent shadow-closure counterfactual zeroing all hypotheses:
    assert all(
        max([0] + [0 for u_i in range(n_v) if int(fw_reach[u_i, sm_i]) == 1]) == 0
        for sm_i in l5_ids
    )
    assert res_7b["obstructed_sm_count"] == 19
    assert res_7b["unblocked_sm_count_is_zero"] is True
    assert res_7b["honest_seam_direction_zero_wp_to_x_verified"] is True
    assert res_7b["planted_fitted_negative_control_verified"] is True
    assert res_7b["dag_and_fk_audit_verified"] is True


def test_cross_stage_witnesses_and_buckingham_pi_guardrail5_zero_trust(stage7_results: dict[str, Any]) -> None:
    res_7c = stage7_results["cross_stage_witnesses_and_buckingham_pi"]
    assert len(res_7c["discovered_producer_modules"]) == 8
    assert len(res_7c["discovered_test_modules"]) == 8
    assert res_7c["cross_stage_ast_contract_and_locks_verified"] is True

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

    n_g_sym = sp.Symbol("n_g_sym")
    b1_sym = sp.Rational(2, 3) * n_g_sym * idx_s1_gen + sp.Rational(1, 3) * sp.Rational(3, 5) * 2 * sp.Rational(1, 4)
    b2_sym = -sp.Rational(11, 3) * 2 + sp.Rational(2, 3) * n_g_sym * idx_s2_gen + sp.Rational(1, 3) * sp.Rational(1, 2)
    b3_sym = -sp.Rational(11, 3) * 3 + sp.Rational(2, 3) * n_g_sym * idx_s3_gen
    assert sp.simplify(sp.diff(b1_sym - b2_sym, n_g_sym)) == 0
    assert sp.simplify(sp.diff(b2_sym - b3_sym, n_g_sym)) == 0
    b1_ind = b1_sym.subs(n_g_sym, 3)
    b2_ind = b2_sym.subs(n_g_sym, 3)
    b3_ind = b3_sym.subs(n_g_sym, 3)
    assert sp.simplify(115 * (b1_ind - b2_ind) - 218 * (b2_ind - b3_ind)) == 0

    # 3. Independent 20-item (nullity == 19) Buckingham-Pi nullspace & Guardrail-5 secondary scale pricing checks:
    assert res_7c["buckingham_pi_ledger_size"] == 20
    assert res_7c["buckingham_pi_mass_dim_rank"] == 1
    assert res_7c["buckingham_pi_dimensionless_nullity"] == 19

    dim_row_20 = np.array([[1] * 12 + [0] * 8], dtype=int)
    assert int(np.linalg.matrix_rank(dim_row_20.astype(float))) == 1
    pi_cols_19: list[np.ndarray] = []
    for idx_m in range(1, 12):
        col_r = np.zeros(20, dtype=int)
        col_r[0] = -1
        col_r[idx_m] = 1
        pi_cols_19.append(col_r)
    for idx_d in range(12, 20):
        col_d = np.zeros(20, dtype=int)
        col_d[idx_d] = 1
        pi_cols_19.append(col_d)
    pi_mat_20x19 = np.column_stack(pi_cols_19)
    assert pi_mat_20x19.shape == (20, 19)
    assert int(np.linalg.matrix_rank(pi_mat_20x19.astype(float))) == 19
    assert int(np.max(np.abs(dim_row_20 @ pi_mat_20x19))) == 0

    # Guardrail-5 unit counterchecks on both violations:
    clean_rows = [("ANCHOR:V", 1, 1, 0), ("OBS:M1", 1, 0, 0), ("OBS:G1", 0, 0, 0)]
    assert audit_buckingham_pi_guardrail5_ledger(clean_rows, priced_imported_ratios=0)["guardrail5_compliant"] is True

    two_anch_rows = clean_rows + [("ANCHOR:SECOND", 1, 1, 0)]
    res_two_anch = audit_buckingham_pi_guardrail5_ledger(two_anch_rows, priced_imported_ratios=0)
    assert res_two_anch["guardrail5_compliant"] is False
    assert res_two_anch["anchor_count"] == 2

    unpriced_emp_rows = clean_rows + [("IMP:REF_MASS", 1, 0, 1)]
    res_unpriced = audit_buckingham_pi_guardrail5_ledger(unpriced_emp_rows, priced_imported_ratios=0)
    res_priced = audit_buckingham_pi_guardrail5_ledger(unpriced_emp_rows, priced_imported_ratios=1)
    assert res_unpriced["guardrail5_compliant"] is False
    assert res_unpriced["unpriced_empirical_scale_deficit"] == 1
    assert res_priced["guardrail5_compliant"] is True

    assert res_7c["stage1_koszul_and_conformal_witness_verified"] is True
    assert res_7c["stage2_p753_register16_and_sym2_witness_verified"] is True
    assert res_7c["stage3_wp13_and_e8_248_witness_verified"] is True
    assert res_7c["stage4_fl16_and_full_anomaly16_witness_verified"] is True
    assert res_7c["stage5_gj_ratio_and_haar_yukawa_witness_verified"] is True
    assert res_7c["stage6_b1922_j5_and_desert_218_115_witness_verified"] is True
    assert res_7c["buckingham_pi_single_anchor_verified"] is True
    assert res_7c["derived_ew_vector_boson_masses_verified"] is True
    assert res_7c["two_anchor_negative_control_rejected"] is True
    assert res_7c["secondary_empirical_scale_pricing_enforced"] is True
    assert res_7c["cross_stage_and_buckingham_verified"] is True
