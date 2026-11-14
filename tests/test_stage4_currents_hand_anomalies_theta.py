"""Zero-trust pytest counterchecks & AST locks for Stage 4 (B1861 WP-1.4, WP-3.3, WP-3.5, FL:16):
Weak Currents & Paired-Pole Theorem (P-749), Swap/Orientation/Hand Exhaustion (B1871/B1879/B1886),
6D/4D Perturbative + Global Anomalies & Cusp Inflow + Mode Fate, and Strong-CP bar_theta Theorem.

Strictly enforces 0-of-19 empirical data blindness, Guardrails 1-6, and Anti-Shortcut Locks F1-F6.
Zero producer-dictionary boolean echoing in theorem countercheck tests (Guardrail 6).
"""
from __future__ import annotations

from itertools import combinations, product
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
    joint_commutant_dim_num,
)
from origin_axiom.stage4_currents_hand_anomalies_theta import (
    run_stage4_complete_verification,
)


ROOT = Path(__file__).resolve().parents[1]
STAGE4_SRC = ROOT / "src" / "origin_axiom" / "stage4_currents_hand_anomalies_theta.py"
TEST_SRC = Path(__file__).resolve()


@pytest.fixture(scope="module")
def stage4_results() -> dict[str, Any]:
    return run_stage4_complete_verification()


def test_stage4_firewall_and_guardrail2_ast_locks(stage4_results: dict[str, Any]) -> None:
    assert audit_source_zero_empirical_constants(STAGE4_SRC) is True
    assert audit_source_zero_empirical_constants(TEST_SRC) is True
    assert check_guardrail2_ast_no_literal_bool_verdicts(STAGE4_SRC.read_text(encoding="utf-8")) is True
    assert check_guardrail2_ast_no_literal_bool_verdicts(TEST_SRC.read_text(encoding="utf-8")) is True
    assert stage4_results["zero_sm_empirical_constants_ast_verified"] is True
    assert stage4_results["guardrail2_ast_no_literal_bool_verdicts_verified"] is True
    assert stage4_results["all_verifications_passed"] is True


def test_wp14_zero_trust_histories_amphichirality_mod_n_and_hand(stage4_results: dict[str, Any]) -> None:
    # 1. Independent Moebius-necklace & odd-tick composition enumeration (n=1..10) + 3D bracelets & Rademacher framing:
    def min_rot_str(s_in: str) -> str:
        return min(s_in[k:] + s_in[:k] for k in range(len(s_in)))

    def min_brac_str(s_in: str) -> str:
        return min(min_rot_str(s_in), min_rot_str(s_in[::-1]))

    def is_prim(seq_in: Any) -> bool:
        ln = len(seq_in)
        return all(seq_in != seq_in[:d] * (ln // d) for d in range(1, ln) if ln % d == 0)

    def build_comp_from_mask(mask_bits: tuple[int, ...]) -> tuple[int, ...]:
        parts_l: list[int] = []
        cur_l = 1
        for b_v in mask_bits:
            if b_v == 1:
                parts_l.append(cur_l)
                cur_l = 1
            else:
                cur_l += 1
        parts_l.append(cur_l)
        return tuple(parts_l)

    prim_two_act: list[int] = []
    prim_odd_tick: list[int] = []
    for n_len in range(1, 11):
        words = {min_rot_str("".join(w)) for w in product("LR", repeat=n_len) if ("L" in w and "R" in w)}
        prim_two_act.append(sum(1 for w in words if is_prim(w)))
        comps_all = [build_comp_from_mask(msk) for msk in product((0, 1), repeat=n_len - 1)]
        odd_comps = {
            min(tp[k:] + tp[:k] for k in range(len(tp)))
            for tp in comps_all
            if len(tp) % 2 == 1
        }
        prim_odd_tick.append(sum(1 for c_t in odd_comps if is_prim(c_t)))

    assert prim_two_act == [0, 1, 2, 3, 6, 9, 18, 30, 56, 99]
    assert prim_odd_tick == [1, 1, 1, 2, 3, 5, 9, 16, 28, 51]
    assert stage4_results["wp14_swap_and_hand"]["two_act_counts_1_to_10"] == prim_two_act
    assert stage4_results["wp14_swap_and_hand"]["tick_odd_counts_1_to_10"] == prim_odd_tick

    # Check 69 cyclic necklaces (11 = 5 + 6 amphichiral, 29 pairs) AND 60 oriented 3-manifold bracelets (8 + 2*26):
    swap_map = str.maketrans("LR", "RL")
    all_up_to_8: list[str] = []
    for n_len in range(2, 9):
        ws = {min_rot_str("".join(w)) for w in product("LR", repeat=n_len) if ("L" in w and "R" in w)}
        all_up_to_8.extend(sorted(w for w in ws if is_prim(w)))
    assert len(all_up_to_8) == 69
    amph_rot = [w for w in all_up_to_8 if min_rot_str(w.translate(swap_map)) == w]
    amph_ref = [w for w in all_up_to_8 if (w not in amph_rot) and (min_rot_str(w[::-1].translate(swap_map)) == w)]
    assert (len(amph_rot), len(amph_ref), (len(all_up_to_8) - len(amph_rot) - len(amph_ref)) // 2) == (5, 6, 29)

    bracelets_60 = sorted({min_brac_str(w) for w in all_up_to_8})
    brac_amph_8 = [b_w for b_w in bracelets_60 if min_brac_str(b_w.translate(swap_map)) == b_w]
    brac_chiral = [b_w for b_w in bracelets_60 if b_w not in brac_amph_8]
    assert (len(bracelets_60), len(brac_amph_8), len(brac_chiral) // 2) == (60, 8, 26)
    # Rademacher / adiabatic Chern-Simons framing defect Psi(W) = #L(W) - #R(W):
    for b_a in brac_amph_8:
        assert sum(1 if ch == "L" else -1 for ch in b_a) == 0
    assert any(sum(1 if ch == "L" else -1 for ch in b_c) != 0 for b_c in brac_chiral)
    assert sum(sum(1 if ch == "L" else -1 for ch in b_w) for b_w in bracelets_60) == 0

    # Independent 3D orientation Jacobian & monodromy conjugacy check on M_LR = m004:
    l_z = sp.Matrix([[1, 1], [0, 1]])
    r_z = sp.Matrix([[1, 0], [1, 1]])
    m004_z = l_z * r_z
    f_z = sp.Matrix([[1, 1], [1, 0]])
    j_inv_z = sp.Matrix([[0, 1], [-1, 0]])
    j_refl_z = sp.Matrix([[1, 0], [0, -1]])
    # 3x3 tangent differentials on (x1, x2, t):
    #   Phi_F(x, t) = (F x, t) and Phi_Jinv(x, t) = (J_inv x, -t) both have det = -1 (orientation-reversing),
    #   while Phi_Jrefl(x, t) = (J_refl x, -t) has det = +1 (orientation-preserving word reversal):
    d_phi_f = sp.BlockMatrix([[f_z, sp.zeros(2, 1)], [sp.zeros(1, 2), sp.Matrix([[1]])]]).as_explicit()
    d_phi_jinv = sp.BlockMatrix([[j_inv_z, sp.zeros(2, 1)], [sp.zeros(1, 2), sp.Matrix([[-1]])]]).as_explicit()
    d_phi_jrefl = sp.BlockMatrix([[j_refl_z, sp.zeros(2, 1)], [sp.zeros(1, 2), sp.Matrix([[-1]])]]).as_explicit()
    assert d_phi_f.det() == -1 and d_phi_jinv.det() == -1 and d_phi_jrefl.det() == 1
    assert f_z * f_z == m004_z
    assert f_z * m004_z * f_z.inv() == m004_z
    assert j_inv_z * m004_z * j_inv_z.inv() == m004_z.inv()
    assert j_refl_z * m004_z * j_refl_z.inv() == (r_z * l_z).inv()
    for w_str in all_up_to_8:
        mw = sp.eye(2)
        mw_rev = sp.eye(2)
        mw_swap_rev = sp.eye(2)
        for ch in w_str:
            mw = mw * (l_z if ch == "L" else r_z)
        for ch in w_str[::-1]:
            mw_rev = mw_rev * (l_z if ch == "L" else r_z)
            mw_swap_rev = mw_swap_rev * (r_z if ch == "L" else l_z)
        assert j_refl_z * mw * j_refl_z.inv() == mw_rev.inv()
        assert j_inv_z * mw * j_inv_z.inv() == mw_swap_rev.inv()

    # 2. Independent GL(2, Z/NZ) orders across N in {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13}:
    def close_mod_n(gens: list[np.ndarray], mod_n: int) -> int:
        id_m = np.eye(2, dtype=int) % mod_n
        id_key = (int(id_m[0, 0]), int(id_m[0, 1]), int(id_m[1, 0]), int(id_m[1, 1]))
        seen_d = {id_key: id_m}
        frontier = [id_m]
        while frontier:
            nxt_front: list[np.ndarray] = []
            for a_m in frontier:
                for b_m in gens:
                    nx_m = (a_m @ b_m) % mod_n
                    nx_k = (int(nx_m[0, 0]), int(nx_m[0, 1]), int(nx_m[1, 0]), int(nx_m[1, 1]))
                    if nx_k not in seen_d:
                        seen_d[nx_k] = nx_m
                        nxt_front.append(nx_m)
            frontier = nxt_front
        return len(seen_d)

    gl = np.array([[1, 1], [0, 1]], dtype=int)
    gr = np.array([[1, 0], [1, 1]], dtype=int)
    gp = np.array([[0, 1], [1, 0]], dtype=int)
    assert [close_mod_n([gl, gr], m) for m in (2, 3, 4, 5)] == [6, 24, 48, 120]
    assert [close_mod_n([gl, gr, gp], m) for m in (2, 3, 4, 5)] == [6, 48, 96, 240]
    for m_n in (6, 7, 8, 9, 10, 11, 13):
        sz_lr = close_mod_n([gl, gr], m_n)
        sz_lrp = close_mod_n([gl, gr, gp], m_n)
        assert sz_lrp == 2 * sz_lr

    # 3. Independent exact SymPy Fox 1-cocycle & cup-pairing closure of R_96 (40+28+28), G_192, and tau_exch:
    qi_s = sp.Matrix([[sp.I, 0], [0, -sp.I]])
    qj_s = sp.Matrix([[0, 1], [-1, 0]])
    i2_s = sp.eye(2)
    pars = [(1, 0), (0, 1), (1, 1)]

    def rep_q8_s(word: str, pp: tuple[int, int]) -> sp.Matrix:
        m_out = sp.eye(2)
        for ch in word:
            low = ch.lower()
            sgn = -1 if (pp[0] if low == "a" else pp[1]) else 1
            g_b = sgn * (qi_s if low == "a" else qj_s)
            m_out = m_out * (g_b if ch.islower() else g_b.H)
        return m_out

    bases_s: dict[tuple[int, int], tuple[sp.Matrix, sp.Matrix]] = {}
    for pp in pars:
        d0_s = sp.Matrix.vstack(rep_q8_s("a", pp) - i2_s, rep_q8_s("b", pp) - i2_s)
        ns_vecs = d0_s.H.nullspace()
        assert len(ns_vecs) == 2
        v0 = ns_vecs[0] / sp.sqrt((ns_vecs[0].H * ns_vecs[0])[0, 0])
        v1_raw = ns_vecs[1] - v0 * (v0.H * ns_vecs[1])[0, 0]
        v1 = v1_raw / sp.sqrt((v1_raw.H * v1_raw)[0, 0])
        b_sp = sp.Matrix.hstack(v0, v1).applyfunc(sp.simplify)
        bases_s[pp] = (b_sp, (b_sp * b_sp.H).applyfunc(sp.simplify))

    def cocyc_s(za: sp.Matrix, zb: sp.Matrix, word: str, pp: tuple[int, int]) -> sp.Matrix:
        val = sp.zeros(2, 1)
        m_cur = sp.eye(2)
        for ch in word:
            low = ch.lower()
            mg = rep_q8_s(low, pp)
            zl = za if low == "a" else zb
            if ch.islower():
                val = val + m_cur * zl
                m_cur = m_cur * mg
            else:
                mi = mg.H
                val = val - m_cur * mi * zl
                m_cur = m_cur * mi
        return val.applyfunc(sp.expand)

    def mv6_s(mv_map: dict[str, str], lift_m: sp.Matrix) -> sp.Matrix:
        li = lift_m.H
        out = sp.zeros(6, 6)
        for ip, pp in enumerate(pars):
            sa = 1
            for ch in mv_map["a"]:
                sa *= -1 if (pp[0] if ch.lower() == "a" else pp[1]) else 1
            sb = 1
            for ch in mv_map["b"]:
                sb *= -1 if (pp[0] if ch.lower() == "a" else pp[1]) else 1
            qp = (0 if sa == 1 else 1, 0 if sb == 1 else 1)
            iq = pars.index(qp)
            bp, p_unused = bases_s[pp]
            assert p_unused.rows == 4
            bq, pq = bases_s[qp]
            for ck in range(2):
                v4 = bp[:, ck]
                wa = li * cocyc_s(v4[:2, :], v4[2:, :], mv_map["a"], pp)
                wb = li * cocyc_s(v4[:2, :], v4[2:, :], mv_map["b"], pp)
                col_proj = bq.H * (pq * sp.Matrix.vstack(wa, wb))
                out[2 * iq : 2 * iq + 2, 2 * ip + ck] = col_proj.applyfunc(sp.simplify)
        return out

    irt2_s = sp.Integer(1) / sp.sqrt(2)
    ml6_s = mv6_s({"a": "a", "b": "ab"}, (i2_s + qi_s) * irt2_s)
    mr6_s = mv6_s({"a": "ab", "b": "b"}, (i2_s - qj_s) * irt2_s)
    mp6_s = mv6_s({"a": "b", "b": "a"}, (qi_s + qj_s) * irt2_s)

    qm6_s = sp.zeros(6, 6)
    for ii in range(6):
        pi_p = pars[ii // 2]
        vi = bases_s[pi_p][0][:, ii % 2]
        for jj in range(6):
            if pars[jj // 2] != pi_p:
                continue
            vj = bases_s[pi_p][0][:, jj % 2]
            tc_s = sp.Integer(0)
            pref = ""
            mat_cur = sp.eye(2)
            for ch in "abABabAB":
                up = cocyc_s(vi[:2, :], vi[2:, :], pref, pi_p)
                vc = cocyc_s(vj[:2, :], vj[2:, :], ch, pi_p)
                tc_s = tc_s + ((mat_cur * vc).H * up)[0, 0]
                if ch.isupper():
                    rl = rep_q8_s(ch.lower(), pi_p)
                    ul = cocyc_s(vi[:2, :], vi[2:, :], ch.lower(), pi_p)
                    tc_s = tc_s - ((rl * vc).H * ul)[0, 0]
                pref += ch
                mat_cur = mat_cur * rep_q8_s(ch, pi_p)
            qm6_s[ii, jj] = sp.simplify(-sp.I * tc_s)
    g0_s = (qm6_s.conjugate() / 4).applyfunc(sp.simplify)
    assert (g0_s * g0_s - sp.eye(6)).applyfunc(sp.simplify) == sp.zeros(6, 6)
    assert sp.simplify(g0_s.trace()) == 0
    assert (ml6_s * g0_s - g0_s * ml6_s).applyfunc(sp.simplify) == sp.zeros(6, 6)
    assert (mr6_s * g0_s - g0_s * mr6_s).applyfunc(sp.simplify) == sp.zeros(6, 6)
    assert (mp6_s * g0_s + g0_s * mp6_s).applyfunc(sp.simplify) == sp.zeros(6, 6)

    # Exact Q(zeta_24) / cyclotomic BFS closure via exact Gaussian-scaled integer key on numerical unitary matrices
    # AND exact trace partition 96 = 40 (real) + 28 (Im > 0) + 28 (Im < 0):
    ml6 = np.array(ml6_s.tolist(), dtype=complex)
    mr6 = np.array(mr6_s.tolist(), dtype=complex)
    mp6 = np.array(mp6_s.tolist(), dtype=complex)
    g0 = np.array(g0_s.tolist(), dtype=complex)
    tp_vecs = (sp.eye(6) + g0_s).columnspace()
    tm_vecs = (sp.eye(6) - g0_s).columnspace()
    assert len(tp_vecs) == 3 and len(tm_vecs) == 3

    def gs_orthonorm_3(vecs_l: list[sp.Matrix]) -> sp.Matrix:
        on_l: list[sp.Matrix] = []
        for v_c in vecs_l:
            w_c = v_c
            for u_p in on_l:
                w_c = w_c - u_p * (u_p.H * w_c)[0, 0]
            w_c = (w_c / sp.sqrt((w_c.H * w_c)[0, 0])).applyfunc(sp.simplify)
            on_l.append(w_c)
        return sp.Matrix.hstack(*on_l)

    v_tp_s = gs_orthonorm_3(tp_vecs)
    v_tm_s = gs_orthonorm_3(tm_vecs)
    v_tp = np.array(v_tp_s.tolist(), dtype=complex)
    v_tm = np.array(v_tm_s.tolist(), dtype=complex)

    def bfs_close_tol(gens_u: list[np.ndarray]) -> list[np.ndarray]:
        d_sz = gens_u[0].shape[0]
        seen_u = [np.eye(d_sz, dtype=complex)]
        q_i = 0
        while q_i < len(seen_u):
            cur_u = seen_u[q_i]
            q_i += 1
            for g_u in gens_u:
                nxt_u = cur_u @ g_u
                if not any(float(np.max(np.abs(nxt_u - ex_u))) < 1e-9 for ex_u in seen_u):
                    seen_u.append(nxt_u)
        return seen_u

    r96_list = bfs_close_tol([ml6, mr6])
    g192_list = bfs_close_tol([ml6, mr6, mp6])
    assert len(r96_list) == 96 == stage4_results["wp14_swap_and_hand"]["order_R96"]
    assert len(g192_list) == 192 == stage4_results["wp14_swap_and_hand"]["order_G192"]
    im_z, im_p, im_m = 0, 0, 0
    for g_el in r96_list:
        tr_t = complex(np.trace(v_tp.conj().T @ g_el @ v_tp))
        tr_tbar = complex(np.trace(v_tm.conj().T @ g_el @ v_tm))
        tr_t_tau = complex(np.trace(v_tp.conj().T @ (mp6 @ g_el @ mp6.conj().T) @ v_tp))
        assert abs(tr_tbar - np.conj(tr_t)) < TOL
        assert abs(tr_tbar - tr_t_tau) < TOL
        two_im = complex(-1j * (tr_t - np.conj(tr_t)))
        two_im_r = abs(two_im)
        if two_im_r < 1e-9:
            im_z += 1
        elif abs((tr_t - np.conj(tr_t)) - 1j * two_im_r) < 1e-9:
            im_p += 1
        else:
            im_m += 1
    assert (im_z, im_p, im_m) == (40, 28, 28)

    rng = np.random.default_rng(71)
    for _ in range(5):
        u6 = haar_unitary(6, rng)
        g_s = u6 @ g0 @ u6.conj().T
        l_s = u6 @ ml6 @ u6.conj().T
        r_s = u6 @ mr6 @ u6.conj().T
        p_s = u6 @ mp6 @ u6.conj().T
        assert float(np.max(np.abs(g_s @ g_s - np.eye(6)))) < TOL
        assert float(np.max(np.abs(l_s @ g_s - g_s @ l_s))) < TOL
        assert float(np.max(np.abs(r_s @ g_s - g_s @ r_s))) < TOL
        assert float(np.max(np.abs(p_s @ g_s + g_s @ p_s))) < TOL
        assert abs(complex(np.trace(g_s))) < TOL
        assert joint_commutant_dim_num([l_s, r_s], tol=1e-9) == 2
        assert joint_commutant_dim_num([l_s, r_s, p_s], tol=1e-9) == 1

    # 4. Independent Z_2-graded Cl(16) = Cl(10) hat(x) Cl(6) inner Spin(16) conjugation U_tilde = (B_10 chi_10) (x) B_6
    #    and 120-generator e_8 spinor-spinor bilinear Lie-bracket automorphism check (D1):
    sx = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    sy = np.array([[0.0, -1j], [1j, 0.0]], dtype=complex)
    sz = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
    i2_c = np.eye(2, dtype=complex)

    def kron_all(ms: list[np.ndarray]) -> np.ndarray:
        res = ms[0]
        for m_k in ms[1:]:
            res = np.kron(res, m_k)
        return res

    g10_l: list[np.ndarray] = []
    for k_i in range(5):
        g10_l.append(kron_all([sz] * k_i + [sx] + [i2_c] * (4 - k_i)))
        g10_l.append(kron_all([sz] * k_i + [sy] + [i2_c] * (4 - k_i)))
    chir10 = kron_all([sz] * 5)
    g6_l: list[np.ndarray] = []
    for j_i in range(3):
        g6_l.append(kron_all([sz] * j_i + [sx] + [i2_c] * (2 - j_i)))
        g6_l.append(kron_all([sz] * j_i + [sy] + [i2_c] * (2 - j_i)))
    chir6 = kron_all([sz] * 3)

    i8_c = np.eye(8, dtype=complex)
    gtilde_16 = [np.kron(g_a, i8_c) for g_a in g10_l] + [np.kron(chir10, f_j) for f_j in g6_l]
    assert len(gtilde_16) == 16
    chir16 = np.kron(chir10, chir6)
    idx_splus = [k_s for k_s in range(256) if abs(chir16[k_s, k_s] - 1.0) < TOL]
    assert len(idx_splus) == 128

    c16_256 = np.eye(256, dtype=complex)
    for ax_o in (1, 3, 5, 7, 9, 11, 13, 15):
        c16_256 = c16_256 @ gtilde_16[ax_o]
    uconj_256 = np.eye(256, dtype=complex)
    for ax_c in (0, 2, 4, 6, 8, 11, 13, 15):
        uconj_256 = uconj_256 @ gtilde_16[ax_c]

    c16_s = c16_256[np.ix_(idx_splus, idx_splus)]
    uconj_s = uconj_256[np.ix_(idx_splus, idx_splus)]
    assert float(np.max(np.abs(c16_s - c16_s.T))) < TOL
    assert float(np.max(np.abs(c16_s @ c16_s - np.eye(128)))) < TOL
    assert float(np.max(np.abs(uconj_s @ uconj_s - np.eye(128)))) < TOL
    assert abs(complex(np.linalg.det(uconj_s)) - 1.0) < TOL
    assert float(np.max(np.abs(uconj_s.T @ c16_s @ uconj_s - c16_s))) < TOL

    vec_s16: list[int] = []
    for m_i in range(16):
        cg_m = uconj_256 @ gtilde_16[m_i] @ uconj_256
        if float(np.max(np.abs(cg_m - gtilde_16[m_i]))) < TOL:
            vec_s16.append(1)
        else:
            assert float(np.max(np.abs(cg_m + gtilde_16[m_i]))) < TOL
            vec_s16.append(-1)
    assert sum(1 for sv in vec_s16 if sv == -1) == 8

    # Check ALL 120 = C(16, 2) e_8 spinor-spinor bilinear generators K_{M,N} = -(1/2) C_16 (Gamma_M Gamma_N)|_{S_16^+}:
    cnt_120 = 0
    for m_i in range(16):
        for n_i in range(m_i + 1, 16):
            cnt_120 += 1
            gmn_s = (gtilde_16[m_i] @ gtilde_16[n_i])[np.ix_(idx_splus, idx_splus)]
            k_mn = -0.5 * (c16_s @ gmn_s)
            assert float(np.max(np.abs(uconj_s.T @ k_mn @ uconj_s - (vec_s16[m_i] * vec_s16[n_i]) * k_mn))) < TOL
    assert cnt_120 == 120


def test_wp33_zero_trust_sp4_paired_poles_and_theta_persistence(stage4_results: dict[str, Any]) -> None:
    _ = stage4_results
    # 1. Independent SymPy differential-operator derivation of curved Weitzenbock +2/ell^2 shift on Sigma_cusp:
    # For conformal metric ds^2 = Omega(y)^2 (dx^2 + dy^2) with Omega(y) = ell / y (Gaussian curvature K = -1/ell^2),
    # the covariant lowering/raising operators on weight-k_w spin/form densities along x-homogeneous modes (d/dx = 0) are
    # L_- f = (1/Omega) (f'(y) - k_w (Omega'/Omega) f(y)),  L_-^+ f = (1/Omega) (-f'(y) - (1 + k_w) (Omega'/Omega) f(y)).
    y_c = sp.Symbol("y_c", positive=True)
    ell_s = sp.Symbol("ell", positive=True)
    kw_s = sp.Symbol("kw_s", real=True)
    f_fn = sp.Function("f_fn")(y_c)
    om_y = ell_s / y_c
    om_ratio = sp.diff(om_y, y_c) / om_y
    l_minus_f = sp.simplify((sp.diff(f_fn, y_c) - kw_s * om_ratio * f_fn) / om_y)
    l_dag_l_minus = sp.simplify((-sp.diff(l_minus_f, y_c) - (1 + kw_s) * om_ratio * l_minus_f) / om_y)
    l_dag_f = sp.simplify((-sp.diff(f_fn, y_c) - kw_s * om_ratio * f_fn) / om_y)
    l_minus_l_dag = sp.simplify((sp.diff(l_dag_f, y_c) - (kw_s - 1) * om_ratio * l_dag_f) / om_y)
    weitzenbock_comm = sp.simplify(l_dag_l_minus - l_minus_l_dag)
    assert sp.simplify(weitzenbock_comm - (2 * kw_s / (ell_s**2)) * f_fn) == 0
    # On anti-holomorphic 1-form a-slots (kw_s = +1), [L_-^+, L_-] = +2/ell^2 shifts bare 3/(2 ell^2) to 7/(2 ell^2) matching w_L^+!
    assert sp.simplify((weitzenbock_comm.subs(kw_s, 1) / f_fn) + sp.Rational(3, 2) / (ell_s**2) - sp.Rational(7, 2) / (ell_s**2)) == 0
    # On 0-form cusp continuum f(y) = y^(1/2) * y^(i s_p), L_-^+ L_- = (s_p^2 + 1/4)/ell^2 >= 1/(4 ell^2):
    sp_k = sp.Symbol("sp_k", real=True)
    psi_cont = y_c ** (sp.Rational(1, 2) + sp.I * sp_k)
    cont_lap = sp.simplify(l_dag_l_minus.subs({kw_s: 0, f_fn: psi_cont}).doit() / psi_cont)
    assert sp.simplify(cont_lap - (sp_k**2 + sp.Rational(1, 4)) / (ell_s**2)) == 0

    # 2. Independent numerical + Haar U(16) check of principal Casimir on V_{3/2} (x) V_{3/2}:
    rt3 = np.sqrt(3)
    ep = np.array([[0.0, rt3, 0.0, 0.0], [0.0, 0.0, 2.0, 0.0], [0.0, 0.0, 0.0, rt3], [0.0, 0.0, 0.0, 0.0]], dtype=complex)
    em = ep.conj().T
    h4 = ep @ em - em @ ep
    i4 = np.eye(4, dtype=complex)
    ep1 = np.kron(ep, i4)
    ep2 = np.kron(i4, ep)
    em1 = ep1.conj().T
    em2 = ep2.conj().T
    mu16 = 0.5 * (np.kron(h4, i4) + np.kron(i4, h4))
    chol = 0.5 * (em1 @ ep1 + em2 @ ep2)
    cantihol = 0.5 * (ep1 @ em1 + ep2 @ em2)

    mu_diag_c = np.diag(mu16)
    idx_m2 = [k_d for k_d in range(16) if abs(mu_diag_c[k_d] - (-2.0)) < TOL]
    idx_m1 = [k_d for k_d in range(16) if abs(mu_diag_c[k_d] - (-1.0)) < TOL]
    idx_p2 = [k_d for k_d in range(16) if abs(mu_diag_c[k_d] - 2.0) < TOL]
    assert len(idx_m2) == 2 and len(idx_m1) == 3 and len(idx_p2) == 2
    assert float(np.max(np.abs(2.0 * chol[np.ix_(idx_m2, idx_m2)] - 7 * np.eye(2)))) < TOL
    assert float(np.max(np.abs(2.0 * cantihol[np.ix_(idx_p2, idx_p2)] - 7 * np.eye(2)))) < TOL
    eigs_m1 = sorted(float(ev) for ev in np.linalg.eigvalsh(chol[np.ix_(idx_m1, idx_m1)]).tolist())
    assert [int(round(ev)) for ev in eigs_m1] == [3, 3, 4]

    # Independent Cl(10) spinor-to-10 & spinor-to-45 current norms + Haar U(32) & U(16) basis scrambling:
    sx = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    sy = np.array([[0.0, -1j], [1j, 0.0]], dtype=complex)
    sz = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
    i2 = np.eye(2, dtype=complex)

    def kron5(ms: list[np.ndarray]) -> np.ndarray:
        res = ms[0]
        for m_k in ms[1:]:
            res = np.kron(res, m_k)
        return res

    gam10 = []
    for k_i in range(5):
        gam10.append(kron5([sz] * k_i + [sx] + [i2] * (4 - k_i)))
        gam10.append(kron5([sz] * k_i + [sy] + [i2] * (4 - k_i)))
    chir10 = kron5([sz] * 5)
    b10_c = gam10[1] @ gam10[3] @ gam10[5] @ gam10[7] @ gam10[9]
    idx_16p = [k_d for k_d in range(32) if abs(chir10[k_d, k_d] - 1.0) < TOL]
    cg_10 = [(b10_c @ g_a)[np.ix_(idx_16p, idx_16p)] for g_a in gam10]
    for m_cg in cg_10:
        assert float(np.max(np.abs(m_cg - m_cg.T))) < TOL

    c_a3 = 0.5 * (cg_10[6] + 1j * cg_10[7])
    c_a4 = 0.5 * (cg_10[8] + 1j * cg_10[9])
    g6p = 0.5 * (gam10[6] + 1j * gam10[7])
    g8p = 0.5 * (gam10[8] + 1j * gam10[9])
    g8m = 0.5 * (gam10[8] - 1j * gam10[9])
    wl_16 = (g6p @ g8p)[np.ix_(idx_16p, idx_16p)]
    wr_16 = (g6p @ g8m)[np.ix_(idx_16p, idx_16p)]
    assert abs(float(np.linalg.norm(wl_16, "fro")) - 2.0) < TOL
    assert abs(float(np.linalg.norm(wr_16, "fro")) - 2.0) < TOL
    assert abs(float(np.linalg.norm(c_a3, "fro")) - float(np.linalg.norm(c_a4, "fro"))) < TOL

    rng = np.random.default_rng(83)
    res_pair = np.block([[wl_16, np.zeros((16, 16))], [np.zeros((16, 16)), wr_16]])
    assert np.linalg.matrix_rank(wl_16, tol=1e-9) == 4
    assert np.linalg.matrix_rank(wr_16, tol=1e-9) == 4
    base_sv = np.linalg.svd(res_pair, compute_uv=False)
    for _ in range(5):
        u_l = haar_unitary(32, rng)
        u_r = haar_unitary(32, rng)
        sv_s = np.linalg.svd(u_l @ res_pair @ u_r.conj().T, compute_uv=False)
        assert float(np.max(np.abs(sv_s - base_sv))) < TOL

    base_eigs = np.sort(np.linalg.eigvalsh(chol))
    for _ in range(5):
        u16 = haar_unitary(16, rng)
        chol_s = u16 @ chol @ u16.conj().T
        mu_s = u16 @ mu16 @ u16.conj().T
        assert float(np.max(np.abs(chol_s @ mu_s - mu_s @ chol_s))) < TOL
        assert float(np.max(np.abs(np.sort(np.linalg.eigvalsh(chol_s)) - base_eigs))) < TOL

    # 3. Independent SymPy cyclic Spin(5) response {Q, Q^H} = diag(A, B, B, A):
    p_s, r_s, f_s = sp.symbols("p_s r_s f_s")
    pc_s, rc_s, fc_s = sp.symbols("pc_s rc_s fc_s")
    x_r, y_r = sp.symbols("x_r y_r", real=True)
    q_m = sp.Matrix([
        [0, p_s * sp.exp(x_r - y_r), 0, 0],
        [0, 0, r_s * sp.exp(2 * y_r), 0],
        [0, 0, 0, p_s * sp.exp(x_r - y_r)],
        [f_s * sp.exp(-2 * x_r), 0, 0, 0],
    ])
    qh_m = sp.Matrix([
        [0, 0, 0, fc_s * sp.exp(-2 * x_r)],
        [pc_s * sp.exp(x_r - y_r), 0, 0, 0],
        [0, rc_s * sp.exp(2 * y_r), 0, 0],
        [0, 0, pc_s * sp.exp(x_r - y_r), 0],
    ])
    anti = (q_m * qh_m + qh_m * q_m).applyfunc(sp.expand)
    comm = (q_m * qh_m - qh_m * q_m).applyfunc(sp.expand)
    assert sp.simplify(anti[0, 0] - anti[3, 3]) == 0
    assert sp.simplify(anti[1, 1] - anti[2, 2]) == 0
    assert sp.simplify(comm[0, 0] + comm[3, 3]) == 0
    assert sp.simplify(comm[1, 1] + comm[2, 2]) == 0

    # 4. Independent mechanical check of A_16, D_16, Theta = L J_0 on W_8, AND holonomy-commuting magnetic splitter (D4):
    hw16 = np.zeros((16, 1), dtype=complex)
    hw16[0, 0] = 1.0
    a16_n = np.zeros((16, 16), dtype=complex)
    d16_n = np.zeros((16, 16), dtype=complex)
    j0_n = np.zeros((16, 16), dtype=complex)
    w_twice = [3, 1, -1, -3]
    for ia in range(4):
        for ib in range(4):
            rv = np.linalg.matrix_power(em1, ia) @ np.linalg.matrix_power(em2, ib) @ hw16
            nv = float(np.linalg.norm(rv))
            a16_n[:, 4 * ia + ib : 4 * ia + ib + 1] = (
                np.linalg.matrix_power(1j * em2, ia) @ np.linalg.matrix_power(1j * em1, ib) @ hw16
            ) / nv
            d16_n[:, 4 * ia + ib : 4 * ia + ib + 1] = (
                np.linalg.matrix_power(-1j * em1, ia) @ np.linalg.matrix_power(1j * em2, ib) @ hw16
            ) / nv
            mu_i = (w_twice[ia] + w_twice[ib]) // 2
            j0_n[4 * (3 - ia) + (3 - ib), 4 * ia + ib] = float((-1) ** (3 - mu_i))
    assert float(np.max(np.abs(j0_n @ a16_n.conj() + a16_n @ j0_n))) < TOL
    w8_idx = [4 * ia + ib for ia in range(4) for ib in range(4) if abs(w_twice[ia]) != abs(w_twice[ib])]
    l_w8 = np.diag([1.0 if abs(w_twice[k // 4]) > abs(w_twice[k % 4]) else -1.0 for k in w8_idx])
    th_w8 = l_w8 @ j0_n[np.ix_(w8_idx, w8_idx)]
    aw8 = a16_n[np.ix_(w8_idx, w8_idx)]
    dw8 = d16_n[np.ix_(w8_idx, w8_idx)]
    mu_w8 = mu16[np.ix_(w8_idx, w8_idx)]
    assert float(np.max(np.abs(th_w8 @ th_w8.conj() - np.eye(8)))) < TOL
    assert float(np.max(np.abs(th_w8 @ aw8.conj() - aw8 @ th_w8))) < TOL
    assert float(np.max(np.abs(th_w8 @ dw8.conj() - dw8 @ th_w8))) < TOL
    assert float(np.max(np.abs(th_w8 @ mu_w8.conj() + mu_w8 @ th_w8))) < TOL

    # Genuine holonomy-equivariant Theta-odd splitter B_split = b_h * mu_w8 (commutes with BOTH A_W8 and D_W8,
    # anticommutes with Theta = L J_0, and splits holomorphic mu=-2 vs antiholomorphic mu=+2 poles by 4*b_h!):
    b_split_op = 0.5 * mu_w8
    assert float(np.max(np.abs(b_split_op @ aw8 - aw8 @ b_split_op))) < TOL
    assert float(np.max(np.abs(b_split_op @ dw8 - dw8 @ b_split_op))) < TOL
    assert float(np.max(np.abs(th_w8 @ b_split_op.conj() + b_split_op @ th_w8))) < TOL
    chol_w8 = chol[np.ix_(w8_idx, w8_idx)]
    cantihol_w8 = cantihol[np.ix_(w8_idx, w8_idx)]
    idx_w8_m2 = [k_d for k_d in range(8) if abs(mu_w8[k_d, k_d] - (-2.0)) < TOL]
    idx_w8_p2 = [k_d for k_d in range(8) if abs(mu_w8[k_d, k_d] - 2.0) < TOL]
    hol_shifted = (chol_w8 + b_split_op)[np.ix_(idx_w8_m2, idx_w8_m2)]
    antihol_shifted = (cantihol_w8 + b_split_op)[np.ix_(idx_w8_p2, idx_w8_p2)]
    assert float(np.max(np.abs(2.0 * hol_shifted - 5 * np.eye(2)))) < TOL
    assert float(np.max(np.abs(2.0 * antihol_shifted - 9 * np.eye(2)))) < TOL


def test_wp35_zero_trust_cl10_matrix_anomalies_6d_gs_and_inflow(stage4_results: dict[str, Any]) -> None:
    # 1. Independent 3-generation 48x48 Cl(10) x Cl(6) construction of FULL non-abelian SU(3)_c x SU(2)_L x U(1)_Y x U(1)_{B-L}:
    sx = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    sy = np.array([[0.0, -1j], [1j, 0.0]], dtype=complex)
    sz = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
    i2 = np.eye(2, dtype=complex)

    def kron_n(mats: list[np.ndarray]) -> np.ndarray:
        out = mats[0]
        for m in mats[1:]:
            out = np.kron(out, m)
        return out

    gammas_10: list[np.ndarray] = []
    for k in range(5):
        prefix = [sz] * k
        suffix = [i2] * (4 - k)
        gammas_10.append(kron_n(prefix + [sx] + suffix))
        gammas_10.append(kron_n(prefix + [sy] + suffix))

    gam_chiral = kron_n([sz, sz, sz, sz, sz])
    idx_16_plus = [k_d for k_d in range(32) if abs(gam_chiral[k_d, k_d] - 1.0) < TOL]
    assert len(idx_16_plus) == 16

    gammas_6: list[np.ndarray] = []
    for j in range(3):
        gammas_6.append(kron_n([sz] * j + [sx] + [i2] * (2 - j)))
        gammas_6.append(kron_n([sz] * j + [sy] + [i2] * (2 - j)))
    chir6 = kron_n([sz, sz, sz])
    idx_4p = [k_d for k_d in range(8) if abs(chir6[k_d, k_d] - 1.0) < TOL]
    assert len(idx_4p) == 4
    so5_gens_4 = [
        (-0.5j * (gammas_6[a_i] @ gammas_6[b_i]))[np.ix_(idx_4p, idx_4p)]
        for a_i, b_i in combinations(range(5), 2)
    ]
    j_sp4 = (gammas_6[1] @ gammas_6[3])[np.ix_(idx_4p, idx_4p)]
    assert float(np.max(np.abs(j_sp4 + j_sp4.T))) < TOL
    assert float(np.max(np.abs(j_sp4 @ j_sp4.conj().T - np.eye(4)))) < TOL
    for g_so5 in so5_gens_4:
        assert float(np.max(np.abs(j_sp4 @ g_so5 + g_so5.T @ j_sp4))) < TOL

    c_ann = [0.5 * (gammas_10[2 * a] - 1j * gammas_10[2 * a + 1]) for a in range(5)]
    c_cre = [m.conj().T for m in c_ann]

    def u5_to_spin16(m5: np.ndarray) -> np.ndarray:
        op32 = np.zeros((32, 32), dtype=complex)
        for a in range(5):
            for b in range(5):
                if abs(m5[a, b]) > TOL:
                    term = c_cre[a] @ c_ann[b]
                    if a == b:
                        term = term - 0.5 * np.eye(32, dtype=complex)
                    op32 = op32 + m5[a, b] * term
        return op32[np.ix_(idx_16_plus, idx_16_plus)]

    gell_mann_3 = [
        np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex) * 0.5,
        np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex) * 0.5,
        np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex) * 0.5,
        np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex) * 0.5,
        np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex) * 0.5,
        np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex) * 0.5,
        np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex) * 0.5,
        np.diag([1.0, 1.0, -2.0]).astype(complex) / (2.0 * np.sqrt(3)),
    ]
    i3_fam = np.eye(3, dtype=complex)
    su3_16 = [u5_to_spin16(np.block([[gm, np.zeros((3, 2))], [np.zeros((2, 3)), np.zeros((2, 2))]])) for gm in gell_mann_3]
    su3_48 = [np.kron(i3_fam, g16) for g16 in su3_16]
    pauli_2 = [0.5 * sx, 0.5 * sy, 0.5 * sz]
    su2_16 = [u5_to_spin16(np.block([[np.zeros((3, 3)), np.zeros((3, 2))], [np.zeros((2, 3)), pm]])) for pm in pauli_2]
    su2_48 = [np.kron(i3_fam, w16) for w16 in su2_16]
    y_u5_sp = sp.diag(sp.Rational(1, 3), sp.Rational(1, 3), sp.Rational(1, 3), -sp.Rational(1, 2), -sp.Rational(1, 2))
    bl_u5_sp = sp.diag(sp.Rational(2, 3), sp.Rational(2, 3), sp.Rational(2, 3), 0, 0)
    y_16 = u5_to_spin16(np.array(y_u5_sp.tolist(), dtype=complex))
    bl_16 = u5_to_spin16(np.array(bl_u5_sp.tolist(), dtype=complex))
    y_48 = np.kron(i3_fam, y_16)
    bl_48 = np.kron(i3_fam, bl_16)

    max_333 = max(abs(complex(np.trace(ta @ (tb @ tc + tc @ tb)))) for ta in su3_48 for tb in su3_48 for tc in su3_48)
    max_222 = max(abs(complex(np.trace(wa @ (wb @ wc + wc @ wb)))) for wa in su2_48 for wb in su2_48 for wc in su2_48)
    max_33y = max(abs(complex(np.trace(ta @ (tb @ y_48 + y_48 @ tb)))) for ta in su3_48 for tb in su3_48)
    max_22y = max(abs(complex(np.trace(wa @ (wb @ y_48 + y_48 @ wb)))) for wa in su2_48 for wb in su2_48)
    max_33bl = max(abs(complex(np.trace(ta @ (tb @ bl_48 + bl_48 @ tb)))) for ta in su3_48 for tb in su3_48)
    max_22bl = max(abs(complex(np.trace(wa @ (wb @ bl_48 + bl_48 @ wb)))) for wa in su2_48 for wb in su2_48)
    yyy_48 = abs(complex(np.trace(y_48 @ y_48 @ y_48)))
    gravy_48 = abs(complex(np.trace(y_48)))
    bl3_48 = abs(complex(np.trace(bl_48 @ bl_48 @ bl_48)))
    gravbl_48 = abs(complex(np.trace(bl_48)))
    y2bl_48 = abs(complex(np.trace(y_48 @ y_48 @ bl_48)))
    ybl2_48 = abs(complex(np.trace(y_48 @ bl_48 @ bl_48)))
    assert max(max_333, max_222, max_33y, max_22y, max_33bl, max_22bl, yyy_48, gravy_48, bl3_48, gravbl_48, y2bl_48, ybl2_48) < TOL

    t3l_48 = su2_48[2]
    n_doublets_48 = int(round(2.0 * abs(complex(np.trace(t3l_48 @ t3l_48)))))
    assert n_doublets_48 == 12 and n_doublets_48 % 2 == 0

    idx_nur_16 = [
        i_s
        for i_s in range(16)
        if abs(y_16[i_s, i_s]) < TOL
        and all(float(np.linalg.norm(g3[:, i_s])) < TOL for g3 in su3_16)
        and all(float(np.linalg.norm(w2[:, i_s])) < TOL for w2 in su2_16)
        and abs(bl_16[i_s, i_s] - 1.0) < TOL
    ]
    assert len(idx_nur_16) == 1 == stage4_results["wp35_anomalies_and_modes"]["nu_r_static_3gen_multiplicity"] // 3
    idx_45_no_nur = [16 * g_f + i_s for g_f in range(3) for i_s in range(16) if i_s not in idx_nur_16]
    assert len(idx_45_no_nur) == 45 and len(idx_45_no_nur) % 16 == 13
    bl_45 = bl_48[np.ix_(idx_45_no_nur, idx_45_no_nur)]
    assert abs(abs(complex(np.trace(bl_45))) - 3) < TOL and abs(abs(complex(np.trace(bl_45 @ bl_45 @ bl_45))) - 3) < TOL

    # 2. Independent 8-variable SymPy proof of 6D E_8 100 * Tr_{248}(F^4) == (Tr_{248}(F^2))^2:
    f_vars = sp.symbols("f0:8")
    e8_roots_sp: list[tuple[sp.Expr, ...]] = []
    for i_c, j_c in combinations(range(8), 2):
        for si in (-1, 1):
            for sj in (-1, 1):
                rv_l = [sp.Integer(0)] * 8
                rv_l[i_c] = sp.Integer(si)
                rv_l[j_c] = sp.Integer(sj)
                e8_roots_sp.append(tuple(rv_l))
    half_q = sp.Rational(1, 2)
    for bits in product((-1, 1), repeat=8):
        if sum(1 for b_v in bits if b_v < 0) in (0, 2, 4, 6, 8):
            e8_roots_sp.append(tuple(b_v * half_q for b_v in bits))
    assert len(e8_roots_sp) == 240
    tr2_sp = sum((sum(r_v[k_i] * f_vars[k_i] for k_i in range(8)) ** 2 for r_v in e8_roots_sp), sp.Integer(0))
    tr4_sp = sum((sum(r_v[k_i] * f_vars[k_i] for k_i in range(8)) ** 4 for r_v in e8_roots_sp), sp.Integer(0))
    assert sp.expand(100 * tr4_sp - tr2_sp**2) == 0

    # 3. Independent exterior-algebra DGA two-step Stora-Zumino descent & Bardeen counterterm B_4 (D5):
    lam_z_s, lam_y_s, fz_s, fy_s = sp.symbols("lam_z_s lam_y_s fz_s fy_s")
    w_ops: list[sp.Matrix] = []
    for g_ax in range(4):
        w_m = sp.zeros(16, 16)
        b_st = 2**g_ax
        for m_k in range(16):
            if (m_k // b_st) % 2 == 0:
                p_b = sum((m_k // (2**j_b)) % 2 for j_b in range(g_ax))
                w_m[m_k + b_st, m_k] = (-1) ** p_b
        w_ops.append(w_m)
    i_ops = [w_m.T for w_m in w_ops]

    def sc_vec(ex: sp.Expr | int) -> sp.Matrix:
        v_o = sp.zeros(16, 1)
        v_o[0, 0] = sp.expand(ex)
        return v_o

    def wedge_16(va: sp.Matrix, vb: sp.Matrix) -> sp.Matrix:
        out_v = sp.zeros(16, 1)
        for m_a in range(16):
            if va[m_a, 0] != 0:
                op_m = sp.eye(16)
                for g_ax in range(4):
                    if (m_a // (2**g_ax)) % 2 == 1:
                        op_m = op_m * w_ops[g_ax]
                out_v = out_v + va[m_a, 0] * (op_m * vb)
        return out_v.applyfunc(sp.expand)

    def d_16(va: sp.Matrix) -> sp.Matrix:
        dl = w_ops[0] * va.applyfunc(lambda ex: sp.diff(ex, lam_z_s)) + w_ops[1] * va.applyfunc(lambda ex: sp.diff(ex, lam_y_s))
        dc = fz_s * (i_ops[2] * va) + fy_s * (i_ops[3] * va)
        return (dl + dc).applyfunc(sp.expand)

    def delta_16(va: sp.Matrix, uz: bool = True, uy: bool = True) -> sp.Matrix:
        od = sp.zeros(16, 1)
        if uz:
            od = od + w_ops[0] * (i_ops[2] * va)
        if uy:
            od = od + w_ops[1] * (i_ops[3] * va)
        return od.applyfunc(sp.expand)

    y_5 = [sp.Rational(-1, 3), sp.Rational(-1, 3), sp.Rational(-1, 3), sp.Rational(1, 2), sp.Rational(1, 2)]
    y_10 = [y_5[i_a] + y_5[j_a] for i_a, j_a in combinations(range(5), 2)]
    pos_states: list[tuple[sp.Expr, sp.Expr]] = (
        [(sp.Integer(5), sp.Integer(0))] * 4
        + [(sp.Integer(4), yv) for yv in y_10]
        + [(sp.Integer(1), -yv) for _ in range(4) for yv in y_10]
        + [(sp.Integer(3), -yv) for _ in range(4) for yv in y_5]
        + [(sp.Integer(2), yv) for _ in range(6) for yv in y_5]
    )
    assert len(pos_states) == 104

    az_v = w_ops[2] * sc_vec(1)
    ay_v = w_ops[3] * sc_vec(1)
    fz_v = sc_vec(fz_s)
    fy_v = sc_vec(fy_s)
    lz_v = sc_vec(lam_z_s)
    ly_v = sc_vec(lam_y_s)
    z16 = sp.zeros(16, 1)

    i6_v = (72 * wedge_16(fz_v, wedge_16(fz_v, fz_v)) + 3 * wedge_16(fz_v, wedge_16(fy_v, fy_v))).applyfunc(sp.expand)
    i5_sym_v = (
        72 * wedge_16(az_v, wedge_16(fz_v, fz_v))
        + wedge_16(az_v, wedge_16(fy_v, fy_v))
        + 2 * wedge_16(ay_v, wedge_16(fz_v, fy_v))
    ).applyfunc(sp.expand)
    a4_cons_100 = sp.zeros(16, 1)
    for qz_s, qy_s in pos_states:
        lm_v = qz_s * lz_v + qy_s * ly_v
        fm_v = qz_s * fz_v + qy_s * fy_v
        a4_cons_100 = (a4_cons_100 + qz_s * wedge_16(lm_v, wedge_16(fm_v, fm_v))).applyfunc(sp.expand)
    assert (d_16(i5_sym_v) - i6_v).applyfunc(sp.expand) == z16
    assert (100 * delta_16(i5_sym_v, uz=True, uy=True) - d_16(a4_cons_100)).applyfunc(sp.expand) == z16
    b4_v = (2 * wedge_16(az_v, wedge_16(ay_v, fy_v))).applyfunc(sp.expand)
    i5_cov_v = (i5_sym_v - d_16(b4_v)).applyfunc(sp.expand)
    i4_cov_v = (72 * wedge_16(lz_v, wedge_16(fz_v, fz_v)) + 3 * wedge_16(lz_v, wedge_16(fy_v, fy_v))).applyfunc(sp.expand)
    assert (d_16(i5_cov_v) - i6_v).applyfunc(sp.expand) == z16
    assert delta_16(i5_cov_v, uz=False, uy=True) == z16
    assert (delta_16(i5_cov_v, uz=True, uy=True) - d_16(i4_cov_v)).applyfunc(sp.expand) == z16

    # 4. Independent live 128D parabolic Koszul subspace check on h_4 (9+3+9+3=24 & live nu_R weights) vs h_1 (0 chiral, 24 vectorlike) (D2):
    irt2_k = 1.0 / np.sqrt(2.0)
    rt6_k = np.sqrt(6)
    rt10_k = np.sqrt(10)
    w8_k = np.exp(1j * np.pi / 4)
    e5_k = np.zeros((5, 5), dtype=complex)
    for j_k, cv_k in enumerate((2.0, rt6_k, rt6_k, 2.0)):
        e5_k[j_k + 1, j_k] = cv_k
    j5_k = np.zeros((5, 5), dtype=complex)
    for j_k, cv_k in enumerate((1.0, -1.0, 1.0, -1.0, 1.0)):
        j5_k[j_k, 4 - j_k] = cv_k
    bz_sp = sp.zeros(5, 5)
    bz_sp[1, 4] = sp.sqrt(sp.Rational(2, 5))
    bz_sp[4, 1] = -bz_sp[1, 4]
    bz_sp[2, 3] = -sp.sqrt(sp.Rational(3, 5))
    bz_sp[3, 2] = -bz_sp[2, 3]
    bz_k = np.array(bz_sp.tolist(), dtype=complex)
    z5_k = np.zeros((5, 5), dtype=complex)
    e10_k = np.block([[e5_k, z5_k], [z5_k, -e5_k.T]])
    g10_k = rt10_k * np.block([[z5_k, bz_k], [j5_k @ bz_k @ j5_k, z5_k]])
    ep10_k = 0.5 * (e10_k + g10_k)
    em10_k = 0.5 * (e10_k - g10_k)
    htot10_k = (ep10_k @ ep10_k.conj().T - ep10_k.conj().T @ ep10_k) + (em10_k @ em10_k.conj().T - em10_k.conj().T @ em10_k)

    cre32: list[np.ndarray] = []
    for ax_k in range(5):
        op_m = np.zeros((32, 32), dtype=complex)
        p2_k = 2**ax_k
        for st_k in range(32):
            if (st_k // p2_k) % 2 == 0:
                op_m[st_k + p2_k, st_k] = float((-1) ** sum((st_k // (2**b_i)) % 2 for b_i in range(ax_k)))
        cre32.append(op_m)
    ann32 = [cm.T for cm in cre32]

    def lie32_n(m10_n: np.ndarray) -> np.ndarray:
        out_n = -0.5 * sum(m10_n[i_a, i_a] for i_a in range(5)) * np.eye(32, dtype=complex)
        for i_a in range(5):
            for j_a in range(5):
                if abs(m10_n[i_a, j_a]) > TOL:
                    out_n = out_n + m10_n[i_a, j_a] * (cre32[i_a] @ ann32[j_a])
                if abs(m10_n[i_a, j_a + 5]) > TOL:
                    out_n = out_n + 0.5 * m10_n[i_a, j_a + 5] * (cre32[i_a] @ cre32[j_a])
                if abs(m10_n[i_a + 5, j_a]) > TOL:
                    out_n = out_n + 0.5 * m10_n[i_a + 5, j_a] * (ann32[i_a] @ ann32[j_a])
        return out_n

    a32_n = np.diag([w8_k ** ((5 + sum(2 * [1, 0, -1, -2, -3][ax_k] for ax_k in range(5) if ((st_k // (2**ax_k)) % 2 == 1))) % 8) for st_k in range(32)])
    b04_n = cre32[0] @ cre32[4] + ann32[4] @ ann32[0]
    b13_n = cre32[1] @ cre32[3] + ann32[3] @ ann32[1]
    d32_n = (np.eye(32) - 2.0 * (b04_n @ b04_n)) @ (np.eye(32) - (b13_n @ b13_n) - 1j * b13_n)

    def clv_n(z_l: list[complex]) -> np.ndarray:
        out_c = np.zeros((32, 32), dtype=complex)
        for ix_c, zv in enumerate(z_l):
            if abs(zv) > TOL:
                out_c = out_c + zv * cre32[ix_c] + np.conj(zv) * ann32[ix_c]
        return out_c

    u32_n = np.eye(32, dtype=complex)
    for gv in (
        clv_n([0j, 0j, 1j, 0j, 0j]),
        clv_n([1j * irt2_k, 0j, 0j, 0j, 1j * irt2_k]),
        clv_n([irt2_k, 0j, 0j, 0j, -irt2_k]),
        clv_n([0j, irt2_k, 0j, irt2_k, 0j]),
        clv_n([0j, 1j * irt2_k, 0j, -1j * irt2_k, 0j]),
    ):
        u32_n = u32_n @ gv
    om10_n = np.eye(32, dtype=complex)
    for ax_k in range(5):
        om10_n = om10_n @ (cre32[ax_k] + ann32[ax_k]) @ (1j * (cre32[ax_k] - ann32[ax_k]))
    s32_n = u32_n @ (1j * om10_n)
    om6_n = gammas_6[0] @ gammas_6[1] @ gammas_6[2] @ gammas_6[3] @ gammas_6[4] @ gammas_6[5]
    j1_n, j2_n, j3_n = gammas_6[0] @ gammas_6[1], gammas_6[2] @ gammas_6[3], gammas_6[4] @ gammas_6[5]
    i8_n = np.eye(8, dtype=complex)
    h4_grp8_n = (i8_n - j1_n) * irt2_k @ ((i8_n - j2_n) * irt2_k) @ ((i8_n - j3_n) * irt2_k)
    h4_lie8_n = 0.5j * (j1_n + j2_n + j3_n)

    sp_pairs = [(r1, r2) for r1 in range(32) for r2 in range(8) if abs(om10_n[r1, r1] * om6_n[r2, r2] - 1.0) < TOL]
    assert len(sp_pairs) == 128
    sp_map = {pt: ix for ix, pt in enumerate(sp_pairs)}

    def to128(m32_i: np.ndarray, m8_i: np.ndarray) -> np.ndarray:
        return np.kron(m32_i, m8_i)[np.ix_([8 * r1 + r2 for r1, r2 in sp_pairs], [8 * r1 + r2 for r1, r2 in sp_pairs])]

    e128 = to128(lie32_n(e10_k), i8_n)
    g128 = to128(lie32_n(g10_k), i8_n)
    mu128 = to128(lie32_n(0.5 * htot10_k), i8_n)
    xa128_h4 = to128(a32_n, h4_grp8_n)
    yb128_h4 = to128(d32_n @ a32_n, h4_grp8_n)
    ah32_h1 = a32_n @ s32_n
    xa128_h1 = to128(ah32_h1, gammas_6[0])
    yb128_h1 = to128(d32_n @ ah32_h1, gammas_6[0])
    fi2 = np.array([[1j, 0.0], [0.0, -1j]], dtype=complex)
    fj2 = np.array([[0.0, 1.0], [-1.0, 0.0]], dtype=complex)

    def parab_modes(
        es: np.ndarray, gs: np.ndarray, mus: np.ndarray, xas: np.ndarray, ybs: np.ndarray
    ) -> tuple[int, int, int, np.ndarray, np.ndarray]:
        d0s = np.vstack([es, gs])
        d1s = np.hstack([-gs, es])
        sv0_u, sv0, vh0 = np.linalg.svd(d0s)
        assert sv0_u.shape[0] > 0
        b0 = vh0[sv0 < 1e-9].conj().T
        sv1_u, sv1, vh1 = np.linalg.svd(np.vstack([d1s, d0s.conj().T]))
        assert sv1_u.shape[0] > 0
        b1 = vh1[sv1 < 1e-9].conj().T
        sv2_u, sv2, vh2 = np.linalg.svd(d1s.conj().T)
        assert sv2_u.shape[0] > 0
        b2 = vh2[sv2 < 1e-9].conj().T

        def cnt_deg(dp: int, bh: np.ndarray, xh: np.ndarray, yh: np.ndarray, mh: np.ndarray) -> tuple[int, int, np.ndarray]:
            n_rows = xh.shape[0]
            if bh.shape[1] == 0:
                return 0, 0, np.zeros((n_rows, 0), dtype=complex)
            muh = bh.conj().T @ mh @ bh
            ev_m, vc_m = np.linalg.eigh(0.5 * (muh + muh.conj().T))
            clusters: dict[int, list[int]] = {}
            for ix_e, vl_e in enumerate(ev_m):
                clusters.setdefault(int(round(float(vl_e))), []).append(ix_e)
            h0_tot = 0
            h1_tot = 0
            cols_v: list[np.ndarray] = []
            for m_int, id_l in clusters.items():
                a_ex = dp - m_int
                v_s = bh @ vc_m[:, id_l]
                ta_s = v_s.conj().T @ xh @ v_s
                tb_s = v_s.conj().T @ yh @ v_s
                kp_s = ta_s @ tb_s @ ta_s.conj().T @ tb_s.conj().T
                ev_k, vc_k = np.linalg.eigh(0.5 * (kp_s + kp_s.conj().T))
                p_ix = [i_x for i_x, v_x in enumerate(ev_k) if abs(v_x - 1.0) < 1e-9]
                m_ix = [i_x for i_x, v_x in enumerate(ev_k) if abs(v_x + 1.0) < 1e-9]
                if p_ix:
                    v_p = v_s @ vc_k[:, p_ix]
                    rk_p = len(p_ix)
                    n_mx = (a_ex // 2) if a_ex < 1 else ((a_ex - 1) // 2)
                    if n_mx > 0:
                        h0_tot += rk_p * n_mx
                        if dp == 1:
                            for _ in range(n_mx):
                                cols_v.append(v_p)
                    elif n_mx < 0:
                        h1_tot += rk_p * (-n_mx)
                        if dp in (0, 2):
                            for _ in range(-n_mx):
                                cols_v.append(v_p)
                    else:
                        ta_p = v_p.conj().T @ xh @ v_p
                        tb_p = v_p.conj().T @ yh @ v_p
                        k_u, k_s, k_vh = np.linalg.svd(np.vstack([ta_p - np.eye(rk_p), tb_p - np.eye(rk_p)]))
                        assert k_u.shape[0] > 0
                        v_tr = v_p @ k_vh[k_s < 1e-9].conj().T
                        n_tr = int(v_tr.shape[1])
                        h0_tot += n_tr
                        h1_tot += n_tr
                        if n_tr > 0:
                            cols_v.append(v_tr)
                if m_ix and a_ex != 1:
                    m_bd = len(m_ix) // 2
                    n_mx_m = ((a_ex + 1) // 2) if a_ex < 1 else (a_ex // 2)
                    dg_p = -1 + 2 * n_mx_m
                    v_m = v_s @ vc_k[:, m_ix]
                    if dg_p > 0:
                        h0_tot += m_bd * dg_p
                        if dp == 1:
                            cols_v.append(v_m)
                    else:
                        h1_tot += m_bd * (-dg_p)
                        if dp in (0, 2):
                            cols_v.append(v_m)
            return h0_tot, h1_tot, (np.hstack(cols_v) if cols_v else np.zeros((n_rows, 0), dtype=complex))

        i2_b = np.eye(2, dtype=complex)
        _, ca, va = cnt_deg(0, b0, xas, ybs, mus)
        cs0, _, vs0 = cnt_deg(1, b1, np.kron(fi2, xas), np.kron(fj2, ybs), np.kron(i2_b, mus))
        _, cs2, _ = cnt_deg(2, b2, xas, ybs, mus)
        return ca, cs0, cs2, va, vs0

    idx_16_3 = [sp_map[(r1, r2)] for r1, r2 in sp_pairs if abs(om10_n[r1, r1] + 1j) < TOL and abs(h4_lie8_n[r2, r2] + 0.5) < TOL]
    idx_16_1 = [sp_map[(r1, r2)] for r1, r2 in sp_pairs if abs(om10_n[r1, r1] + 1j) < TOL and abs(2.0 * h4_lie8_n[r2, r2] - 3) < TOL]
    idx_16b_3b = [sp_map[(r1, r2)] for r1, r2 in sp_pairs if abs(om10_n[r1, r1] - 1j) < TOL and abs(h4_lie8_n[r2, r2] - 0.5) < TOL]
    idx_16b_1 = [sp_map[(r1, r2)] for r1, r2 in sp_pairs if abs(om10_n[r1, r1] - 1j) < TOL and abs(2.0 * h4_lie8_n[r2, r2] + 3) < TOL]
    assert (len(idx_16_3), len(idx_16_1), len(idx_16b_3b), len(idx_16b_1)) == (48, 16, 48, 16)

    for sub_i, exp_tup in ((idx_16_3, (6, 3, 0)), (idx_16_1, (2, 1, 0)), (idx_16b_3b, (6, 3, 0)), (idx_16b_1, (2, 1, 0))):
        ca_s, cs0_s, cs2_s, va_s, vs0_s = parab_modes(
            e128[np.ix_(sub_i, sub_i)],
            g128[np.ix_(sub_i, sub_i)],
            mu128[np.ix_(sub_i, sub_i)],
            xa128_h4[np.ix_(sub_i, sub_i)],
            yb128_h4[np.ix_(sub_i, sub_i)],
        )
        assert (ca_s, cs0_s, cs2_s) == exp_tup
        if sub_i is idx_16_3:
            # Verify live nu_R (r1 == 31, 5-fermion SU(5)-singlet state of 16) carries nonvanishing weight 3/4 on H^0 spin modes!
            nur_loc = [ix_l for ix_l, g_id in enumerate(idx_16_3) if sp_pairs[g_id][0] == 31]
            assert len(nur_loc) == 3
            assert float(np.sum(np.abs(va_s[nur_loc, :]) ** 2)) < TOL
            nur_spin_rows = nur_loc + [len(idx_16_3) + ix_l for ix_l in nur_loc]
            q_on, _ = np.linalg.qr(vs0_s)
            nur_spin_wt = float(np.sum(np.abs(q_on[nur_spin_rows, :]) ** 2))
            assert abs(4 * nur_spin_wt - 3) < TOL

    # On h_1, Pin-odd S_32 (x) f_0 swaps 16 <-> 16_bar with ZERO block-diagonal part and 24 50/50 vectorlike modes:
    idx_c64 = idx_16_3 + idx_16_1
    idx_cb64 = idx_16b_3b + idx_16b_1
    assert float(np.linalg.norm(xa128_h1[np.ix_(idx_c64, idx_c64)])) < TOL
    assert float(np.linalg.norm(yb128_h1[np.ix_(idx_c64, idx_c64)])) < TOL
    ca_h1, cs0_h1, cs2_h1, va_h1, vs0_h1 = parab_modes(e128, g128, mu128, xa128_h1, yb128_h1)
    assert ca_h1 + cs0_h1 + cs2_h1 == 24
    idx_c64_spin = idx_c64 + [128 + ix_c for ix_c in idx_c64]
    idx_cb64_spin = idx_cb64 + [128 + ix_c for ix_c in idx_cb64]
    assert abs(float(np.sum(np.abs(va_h1[idx_c64, :]) ** 2)) - float(np.sum(np.abs(va_h1[idx_cb64, :]) ** 2))) < TOL
    assert abs(float(np.sum(np.abs(vs0_h1[idx_c64_spin, :]) ** 2)) - float(np.sum(np.abs(vs0_h1[idx_cb64_spin, :]) ** 2))) < TOL
    assert stage4_results["wp35_anomalies_and_modes"]["h4_zero_mode_roster"] == {
        "chiral_family_triplet_16_3": 9,
        "family_singlet_exotic_16_1": 3,
        "conjugate_mirror_16bar_3bar": 9,
        "conjugate_singlet_mirror_16bar_1": 3,
        "vector_10_6": 18,
        "adjoint_45_1": 8,
        "adjoint_1_15": 18,
    }
    assert stage4_results["wp35_anomalies_and_modes"]["h1_zero_mode_roster"] == {
        "chiral_16_4_subspace": 0,
        "vectorlike_pin_entangled_128": 24,
        "vector_10_6": 18,
        "adjoint_45_1": 8,
        "adjoint_1_15": 20,
    }


def test_fl16_zero_trust_theta_bar_u3_scrambling_and_dichotomy(stage4_results: dict[str, Any]) -> None:
    _ = stage4_results
    rng = np.random.default_rng(109)
    yu = (rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))) / np.sqrt(2.0) + 2.0 * np.eye(3)
    yd = (rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))) / np.sqrt(2.0) + 2.0 * np.eye(3)
    ye = (rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))) / np.sqrt(2.0) + 2.0 * np.eye(3)
    u_bare_0 = complex(np.exp(1.0j))

    def unit_ph(z_v: complex) -> complex:
        return complex(z_v) / abs(z_v)

    def exp_bar_theta(u_b: complex, mu_y: np.ndarray, md_y: np.ndarray) -> complex:
        return complex(u_b) * unit_ph(complex(np.linalg.det(mu_y @ md_y)))

    def jarlskog_c3(mu_y: np.ndarray, md_y: np.ndarray) -> complex:
        hu_r = mu_y @ mu_y.conj().T
        hd_r = md_y @ md_y.conj().T
        hu = hu_r / (float(np.linalg.norm(mu_y)) ** 2)
        hd = hd_r / (float(np.linalg.norm(md_y)) ** 2)
        cm = hu @ hd - hd @ hu
        return complex(np.trace(cm @ cm @ cm))

    base_th = exp_bar_theta(u_bare_0, yu, yd)
    base_j = jarlskog_c3(yu, yd)
    base_ye_tr = complex(np.trace(ye @ ye.conj().T))

    # 1. Topological QCD instanton shift invariance theta_0 -> theta_0 + 2 * pi * nu_inst (D6):
    for nu_i in (-3, -1, 1, 2, 5):
        u_inst = complex(np.exp(1.0j + 2j * np.pi * nu_i))
        assert abs(exp_bar_theta(u_inst, yu, yd) - base_th) < TOL

    # 2. Full U(3)^4 quark chiral + 5-factor SM U(3)_Q x U(3)_{uR} x U(3)_{dR} x U(3)_L x U(3)_{eR} invariance (D6):
    unshifted_diffs: list[float] = []
    broken_su2_j_diffs: list[float] = []
    for _ in range(12):
        ul_u = haar_unitary(3, rng)
        ur_u = haar_unitary(3, rng)
        ul_d = haar_unitary(3, rng)
        ur_d = haar_unitary(3, rng)
        ul_l = haar_unitary(3, rng)
        ur_e = haar_unitary(3, rng)

        yu_r = ul_u @ yu @ ur_u.conj().T
        yd_r = ul_d @ yd @ ur_d.conj().T
        det_chiral = np.linalg.det(ul_u) * np.conj(np.linalg.det(ur_u)) * np.linalg.det(ul_d) * np.conj(np.linalg.det(ur_d))
        u_sh = u_bare_0 * np.conj(unit_ph(complex(det_chiral)))
        assert abs(exp_bar_theta(u_sh, yu_r, yd_r) - base_th) < TOL
        unshifted_diffs.append(abs(exp_bar_theta(u_bare_0, yu_r, yd_r) - base_th))
        broken_su2_j_diffs.append(abs(jarlskog_c3(yu_r, yd_r) - base_j))

        # Full 5-factor SM flavour rotation (lepton U_L, U_eR carry zero QCD color ABJ anomaly!):
        yu_sm = ul_u @ yu @ ur_u.conj().T
        yd_sm = ul_u @ yd @ ur_d.conj().T
        ye_sm = ul_l @ ye @ ur_e.conj().T
        det_sm5 = (np.linalg.det(ul_u) ** 2) * np.conj(np.linalg.det(ur_u)) * np.conj(np.linalg.det(ur_d))
        u_sm5 = u_bare_0 * np.conj(unit_ph(complex(det_sm5)))
        assert abs(exp_bar_theta(u_sm5, yu_sm, yd_sm) - base_th) < TOL
        assert abs(jarlskog_c3(yu_sm, yd_sm) - base_j) < TOL
        assert abs(complex(np.trace(ye_sm @ ye_sm.conj().T)) - base_ye_tr) < TOL

    assert max(unshifted_diffs) > 0.5
    assert max(broken_su2_j_diffs) > 1e-9

    # 3. Independent SymPy universal proof on BOTH strict mirror-real locus (Y_f = Y_f^*) AND P_swap-covariant locus (D6):
    u_r = sp.symbols("ur0:9", real=True)
    d_r = sp.symbols("dr0:9", real=True)
    yu_real = sp.Matrix([[u_r[0], u_r[1], u_r[2]], [u_r[3], u_r[4], u_r[5]], [u_r[6], u_r[7], u_r[8]]])
    yd_real = sp.Matrix([[d_r[0], d_r[1], d_r[2]], [d_r[3], d_r[4], d_r[5]], [d_r[6], d_r[7], d_r[8]]])
    det_real_p = sp.expand(yu_real.det() * yd_real.det())
    assert sp.expand(det_real_p - sp.conjugate(det_real_p)) == 0
    s_r = sp.symbols("sr0:6", real=True)
    t_r = sp.symbols("tr0:6", real=True)
    hu_rs = sp.Matrix([[s_r[0], s_r[1], s_r[2]], [s_r[1], s_r[3], s_r[4]], [s_r[2], s_r[4], s_r[5]]])
    hd_rs = sp.Matrix([[t_r[0], t_r[1], t_r[2]], [t_r[1], t_r[3], t_r[4]], [t_r[2], t_r[4], t_r[5]]])
    cm_rs = (hu_rs * hd_rs - hd_rs * hu_rs).applyfunc(sp.expand)
    assert sp.expand((cm_rs * cm_rs * cm_rs).trace()) == 0

    p_sw_sp = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    yu_sp = sp.Matrix([
        [u_r[0] + sp.I * u_r[1], u_r[2] + sp.I * u_r[3], u_r[4] + sp.I * u_r[5]],
        [u_r[2] - sp.I * u_r[3], u_r[0] - sp.I * u_r[1], u_r[4] - sp.I * u_r[5]],
        [u_r[6] + sp.I * u_r[7], u_r[6] - sp.I * u_r[7], u_r[8]],
    ])
    yd_sp = sp.Matrix([
        [d_r[0] + sp.I * d_r[1], d_r[2] + sp.I * d_r[3], d_r[4] + sp.I * d_r[5]],
        [d_r[2] - sp.I * d_r[3], d_r[0] - sp.I * d_r[1], d_r[4] - sp.I * d_r[5]],
        [d_r[6] + sp.I * d_r[7], d_r[6] - sp.I * d_r[7], d_r[8]],
    ])
    assert (p_sw_sp * yu_sp.conjugate() * p_sw_sp - yu_sp).applyfunc(sp.expand) == sp.zeros(3, 3)
    det_psw = sp.expand(yu_sp.det() * yd_sp.det())
    assert sp.expand(det_psw - sp.conjugate(det_psw)) == 0

    ha_s = sp.symbols("has0:5", real=True)
    hb_s = sp.symbols("hbs0:5", real=True)
    hu_g = sp.Matrix([
        [ha_s[0], ha_s[1], ha_s[2] + sp.I * ha_s[3]],
        [ha_s[1], ha_s[0], ha_s[2] - sp.I * ha_s[3]],
        [ha_s[2] - sp.I * ha_s[3], ha_s[2] + sp.I * ha_s[3], ha_s[4]],
    ])
    hd_g = sp.Matrix([
        [hb_s[0], hb_s[1], hb_s[2] + sp.I * hb_s[3]],
        [hb_s[1], hb_s[0], hb_s[2] - sp.I * hb_s[3]],
        [hb_s[2] - sp.I * hb_s[3], hb_s[2] + sp.I * hb_s[3], hb_s[4]],
    ])
    cm_g = (hu_g * hd_g - hd_g * hu_g).applyfunc(sp.expand)
    assert sp.expand((cm_g * cm_g * cm_g).trace()) == 0

    # 4. Independent mirror-axis Re(tau)=0 vs TWO off-axis threads (1/5 and 1/3):
    p_sw = np.array([[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]], dtype=complex)
    s_u = np.array([[2.0, 0.5, 0.5], [0.5, 2.0, 0.5], [0.5, 0.5, 1.0]], dtype=complex)
    a_u = 1j * np.array([[1.0, 0.0, 0.5], [0.0, -1.0, -0.5], [-0.5, 0.5, 0.0]], dtype=complex)
    s_d = np.array([[1.0, 0.5, 1.0], [0.5, 1.0, 1.0], [0.5, 0.5, 2.0]], dtype=complex)
    a_d = 1j * np.array([[0.5, 0.5, -0.5], [-0.5, -0.5, 0.5], [0.5, -0.5, 0.0]], dtype=complex)
    u_id = complex(1.0)
    for re_t, expect_zero in ((0.0, True), (1 / 5, False), (1 / 3, False)):
        q_t = np.exp(2j * np.pi * (re_t + 0.5 * 1j))
        yu_t = s_u + q_t * a_u + (q_t**2) * (s_u @ a_u)
        yd_t = s_d + q_t * a_d + (q_t**2) * (a_d @ s_d)
        assert float(np.max(np.abs((s_u + np.conj(q_t) * a_u + (np.conj(q_t) ** 2) * (s_u @ a_u)) - p_sw @ yu_t.conj() @ p_sw))) < TOL
        w_th = exp_bar_theta(u_id, yu_t, yd_t)
        sin_th = 0.5 * abs(w_th - np.conj(w_th))
        j_val = abs(jarlskog_c3(yu_t, yd_t))
        if expect_zero:
            assert sin_th < TOL and j_val < TOL
        else:
            assert sin_th > 1e-9 and j_val > 1e-9

    # 5. Independent exact SymPy Cayley SU(3, Q(i)) Nelson-Barr witness (det(Y_u Y_d) = 15/8 > 0 while J_CP != 0) + Haar check:
    def cayley_2(h2_s: sp.Matrix) -> sp.Matrix:
        i2_s = sp.eye(2)
        return ((i2_s + sp.I * h2_s) * (i2_s - sp.I * h2_s).inv()).applyfunc(sp.simplify)

    q_half = sp.Rational(1, 2)
    c_r = cayley_2(sp.Matrix([[0, q_half], [q_half, 0]]))
    c_i = cayley_2(sp.Matrix([[0, (1 + sp.I) * q_half], [(1 - sp.I) * q_half, 0]]))
    u12 = sp.Matrix([[c_r[0, 0], c_r[0, 1], 0], [c_r[1, 0], c_r[1, 1], 0], [0, 0, 1]])
    u13 = sp.Matrix([[c_i[0, 0], 0, c_i[0, 1]], [0, 1, 0], [c_i[1, 0], 0, c_i[1, 1]]])
    u23 = sp.Matrix([[1, 0, 0], [0, c_r[0, 0], c_r[0, 1]], [0, c_r[1, 0], c_r[1, 1]]])
    u_nb = (u23 * u13 * u12).applyfunc(sp.simplify)
    assert (u_nb * u_nb.H - sp.eye(3)).applyfunc(sp.simplify) == sp.zeros(3, 3)
    assert sp.simplify(u_nb.det() - 1) == 0
    yu_nb_s = sp.diag(q_half, 1, 2)
    yd_nb_s = (u_nb * sp.diag(q_half, sp.Rational(3, 2), sp.Rational(5, 2))).applyfunc(sp.simplify)
    assert sp.simplify((yu_nb_s * yd_nb_s).det()) == sp.Rational(15, 8)
    hu_nb_s = yu_nb_s * yu_nb_s.H
    hd_nb_s = (yd_nb_s * yd_nb_s.H).applyfunc(sp.simplify)
    cm_nb_s = (hu_nb_s * hd_nb_s - hd_nb_s * hu_nb_s).applyfunc(sp.simplify)
    tr_nb_s = sp.expand((cm_nb_s * cm_nb_s * cm_nb_s).trace())
    assert sp.simplify(tr_nb_s - sp.conjugate(tr_nb_s)) != 0

    yu_nb_n = np.array(yu_nb_s.tolist(), dtype=complex)
    yd_nb_n = np.array(yd_nb_s.tolist(), dtype=complex)
    j_nb_base = jarlskog_c3(yu_nb_n, yd_nb_n)
    assert abs(j_nb_base) > 1e-6
    for _ in range(5):
        uq = haar_unitary(3, rng)
        uur = haar_unitary(3, rng)
        udr = haar_unitary(3, rng)
        yu_nb_r = uq @ yu_nb_n @ uur.conj().T
        yd_nb_r = uq @ yd_nb_n @ udr.conj().T
        det_nb_c = (np.linalg.det(uq) ** 2) * np.conj(np.linalg.det(uur)) * np.conj(np.linalg.det(udr))
        u_nb_r = np.conj(unit_ph(complex(det_nb_c)))
        assert abs(exp_bar_theta(u_nb_r, yu_nb_r, yd_nb_r) - 1.0) < TOL
        assert abs(jarlskog_c3(yu_nb_r, yd_nb_r) - j_nb_base) < TOL
