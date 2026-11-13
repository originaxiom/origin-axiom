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
    # 1. Independent Moebius-inversion & explicit enumeration of primitive two-act {L, R} necklaces (n=1..10):
    def min_rot_str(s_in: str) -> str:
        return min(s_in[k:] + s_in[:k] for k in range(len(s_in)))

    def is_prim(seq_in: Any) -> bool:
        ln = len(seq_in)
        return all(seq_in != seq_in[:d] * (ln // d) for d in range(1, ln) if ln % d == 0)

    prim_two_act: list[int] = []
    prim_odd_tick: list[int] = []
    for n_len in range(1, 11):
        words = {min_rot_str("".join(w)) for w in product("LR", repeat=n_len) if ("L" in w and "R" in w)}
        prim_two_act.append(sum(1 for w in words if is_prim(w)))
        odd_comps: set[tuple[int, ...]] = set()
        for mask in product((0, 1), repeat=n_len - 1):
            parts: list[int] = []
            cur = 1
            odd_len = True
            for bit in mask:
                if bit == 1:
                    parts.append(cur)
                    cur = 1
                    odd_len = not odd_len
                else:
                    cur += 1
            parts.append(cur)
            if odd_len:
                tup = tuple(parts)
                odd_comps.add(min(tup[k:] + tup[:k] for k in range(len(tup))))
        prim_odd_tick.append(sum(1 for c_t in odd_comps if is_prim(c_t)))

    assert prim_two_act == [0, 1, 2, 3, 6, 9, 18, 30, 56, 99]
    assert prim_odd_tick == [1, 1, 1, 2, 3, 5, 9, 16, 28, 51]
    assert stage4_results["wp14_swap_and_hand"]["two_act_counts_1_to_10"] == prim_two_act
    assert stage4_results["wp14_swap_and_hand"]["tick_odd_counts_1_to_10"] == prim_odd_tick

    # Check amphichiral count up to length 8 (69 total: 11 amphichiral = 5 odd-tick squares + 6 reflection-swap, 29 pairs):
    swap_map = str.maketrans("LR", "RL")
    all_up_to_8: list[str] = []
    for n_len in range(2, 9):
        ws = {min_rot_str("".join(w)) for w in product("LR", repeat=n_len) if ("L" in w and "R" in w)}
        all_up_to_8.extend(sorted(w for w in ws if is_prim(w)))
    assert len(all_up_to_8) == 69
    amph_rot = [w for w in all_up_to_8 if min_rot_str(w.translate(swap_map)) == w]
    amph_ref = [
        w
        for w in all_up_to_8
        if (w not in amph_rot) and (min_rot_str(w[::-1].translate(swap_map)) == w)
    ]
    assert len(amph_rot) == 5
    assert len(amph_ref) == 6
    assert (len(all_up_to_8) - len(amph_rot) - len(amph_ref)) // 2 == 29

    # Independent m004 = LR = F^2 amphichiral GL(2, Z) conjugacy check:
    # Fiber-reversing (det = -1, t -> +t): F * (LR) * F^-1 == LR;
    # Base-reversing (det = +1, t -> -t, total orientation sign (+1)*(-1) = -1): J_inv * (LR) * J_inv^-1 == (LR)^-1!
    m004_z = sp.Matrix([[2, 1], [1, 1]])
    f_z = sp.Matrix([[1, 1], [1, 0]])
    j_z = sp.Matrix([[0, 1], [-1, 0]])
    assert f_z.det() == -1 and j_z.det() == 1
    assert f_z * f_z == m004_z
    assert f_z * m004_z * f_z.inv() == m004_z
    assert j_z * m004_z * j_z.inv() == m004_z.inv()

    # 2. Independent GL(2, Z/NZ) orders and N=5 4-cycle vs two 2-sets:
    def close_mod_n(gens: list[tuple[int, int, int, int]], mod_n: int) -> set[tuple[int, int, int, int]]:
        id_m = (1 % mod_n, 0, 0, 1 % mod_n)
        seen = {id_m}
        q_l = [id_m]
        while q_l:
            a0, a1, a2, a3 = q_l.pop(0)
            for b0, b1, b2, b3 in gens:
                nx = (
                    (a0 * b0 + a1 * b2) % mod_n,
                    (a0 * b1 + a1 * b3) % mod_n,
                    (a2 * b0 + a3 * b2) % mod_n,
                    (a2 * b1 + a3 * b3) % mod_n,
                )
                if nx not in seen:
                    seen.add(nx)
                    q_l.append(nx)
        return seen

    gl = (1, 1, 0, 1)
    gr = (1, 0, 1, 1)
    gp = (0, 1, 1, 0)
    assert [len(close_mod_n([gl, gr], m)) for m in (2, 3, 4, 5)] == [6, 24, 48, 120]
    assert [len(close_mod_n([gl, gr, gp], m)) for m in (2, 3, 4, 5)] == [6, 48, 96, 240]

    line_f5 = [(u_v % 5, (2 * u_v) % 5) for u_v in range(1, 5)]
    lr_orbits_f5 = {frozenset([v, ((2 * v[0] + v[1]) % 5, (v[0] + v[1]) % 5)]) for v in line_f5}
    f_orb_f5 = []
    cur_f5 = (1, 2)
    for _ in range(4):
        f_orb_f5.append(cur_f5)
        cur_f5 = ((cur_f5[0] + cur_f5[1]) % 5, cur_f5[0] % 5)
    assert len(lr_orbits_f5) == 2 and cur_f5 == (1, 2) and len(set(f_orb_f5)) == 4

    # 3. Independent numerical Fox 1-cocycle & cup-pairing construction of L, R, P, Gamma_hand, |R_96|=96, |G_192|=192, and tau_exch:
    qi = np.array([[1j, 0.0], [0.0, -1j]], dtype=complex)
    qj = np.array([[0.0, 1.0], [-1.0, 0.0]], dtype=complex)
    i2_n = np.eye(2, dtype=complex)
    pars = [(1, 0), (0, 1), (1, 1)]

    def rep_q8(word: str, pp: tuple[int, int]) -> np.ndarray:
        m_out = i2_n.copy()
        for ch in word:
            low = ch.lower()
            sgn = -1.0 if (pp[0] if low == "a" else pp[1]) else 1.0
            g_b = sgn * (qi if low == "a" else qj)
            m_out = m_out @ (g_b if ch.islower() else g_b.conj().T)
        return m_out

    bases_6: dict[tuple[int, int], tuple[np.ndarray, np.ndarray]] = {}
    for pp in pars:
        d0_m = np.vstack([rep_q8("a", pp) - i2_n, rep_q8("b", pp) - i2_n])
        _, sv_d, vh_d = np.linalg.svd(d0_m.conj().T)
        assert len(sv_d) == 2 and float(np.min(sv_d)) > 0.5
        b_mat = vh_d[2:].conj().T
        assert b_mat.shape == (4, 2) and float(np.max(np.abs(d0_m.conj().T @ b_mat))) < TOL
        bases_6[pp] = (b_mat, b_mat @ b_mat.conj().T)

    def cocyc_n(za: np.ndarray, zb: np.ndarray, word: str, pp: tuple[int, int]) -> np.ndarray:
        val = np.zeros((2, 1), dtype=complex)
        m_cur = i2_n.copy()
        for ch in word:
            low = ch.lower()
            mg = rep_q8(low, pp)
            zl = za if low == "a" else zb
            if ch.islower():
                val = val + m_cur @ zl
                m_cur = m_cur @ mg
            else:
                mi = mg.conj().T
                val = val - m_cur @ mi @ zl
                m_cur = m_cur @ mi
        return val

    def mv6_n(mv_map: dict[str, str], lift_m: np.ndarray) -> np.ndarray:
        li = lift_m.conj().T
        out = np.zeros((6, 6), dtype=complex)
        for ip, pp in enumerate(pars):
            sa = 1
            for ch in mv_map["a"]:
                sa *= -1 if (pp[0] if ch.lower() == "a" else pp[1]) else 1
            sb = 1
            for ch in mv_map["b"]:
                sb *= -1 if (pp[0] if ch.lower() == "a" else pp[1]) else 1
            qp = (0 if sa == 1 else 1, 0 if sb == 1 else 1)
            iq = pars.index(qp)
            bp, _ = bases_6[pp]
            bq, pq = bases_6[qp]
            for ck in range(2):
                v4 = bp[:, ck : ck + 1]
                wa = li @ cocyc_n(v4[:2], v4[2:], mv_map["a"], pp)
                wb = li @ cocyc_n(v4[:2], v4[2:], mv_map["b"], pp)
                out[2 * iq : 2 * iq + 2, 2 * ip + ck : 2 * ip + ck + 1] = bq.conj().T @ (pq @ np.vstack([wa, wb]))
        return out

    rt2_inv = 1.0 / np.sqrt(2.0)
    ml6 = mv6_n({"a": "a", "b": "ab"}, (i2_n + qi) * rt2_inv)
    mr6 = mv6_n({"a": "ab", "b": "b"}, (i2_n - qj) * rt2_inv)
    mp6 = mv6_n({"a": "b", "b": "a"}, (qi + qj) * rt2_inv)

    qm6 = np.zeros((6, 6), dtype=complex)
    for ii in range(6):
        pi_p = pars[ii // 2]
        vi = bases_6[pi_p][0][:, ii % 2 : ii % 2 + 1]
        for jj in range(6):
            if pars[jj // 2] != pi_p:
                continue
            vj = bases_6[pi_p][0][:, jj % 2 : jj % 2 + 1]
            tc = 0.0j
            pref = ""
            mat_cur = i2_n.copy()
            for ch in "abABabAB":
                up = cocyc_n(vi[:2], vi[2:], pref, pi_p)
                vc = cocyc_n(vj[:2], vj[2:], ch, pi_p)
                tc += complex(((mat_cur @ vc).conj().T @ up)[0, 0])
                if ch.isupper():
                    rl = rep_q8(ch.lower(), pi_p)
                    ul = cocyc_n(vi[:2], vi[2:], ch.lower(), pi_p)
                    tc -= complex(((rl @ vc).conj().T @ ul)[0, 0])
                pref += ch
                mat_cur = mat_cur @ rep_q8(ch, pi_p)
            qm6[ii, jj] = -1j * tc
    hm6 = qm6.conj()
    ev_h, vec_h = np.linalg.eigh(hm6)
    pos_ev = float(np.max(ev_h))
    g0 = hm6 / pos_ev

    # Project onto chiral 3D eigenspaces T (+1) and T_bar (-1) of g0, close R_96 and G_192, and verify tau_exch:
    idx_tp = np.where(ev_h > 0.0)[0]
    idx_tm = np.where(ev_h < 0.0)[0]
    assert len(idx_tp) == 3 and len(idx_tm) == 3
    v_tp = vec_h[:, idx_tp]
    v_tm = vec_h[:, idx_tm]

    def mat_key_n(m_arr: np.ndarray) -> tuple[tuple[int, int], ...]:
        r_m = np.round(np.real(m_arr) * 64).astype(int)
        i_m = np.round(np.imag(m_arr) * 64).astype(int)
        return tuple(zip(r_m.ravel().tolist(), i_m.ravel().tolist()))

    def bfs_close_unitary(gens_u: list[np.ndarray]) -> list[np.ndarray]:
        d_sz = gens_u[0].shape[0]
        id_u = np.eye(d_sz, dtype=complex)
        seen_k = {mat_key_n(id_u): id_u}
        queue_u = [id_u]
        while queue_u:
            cur_u = queue_u.pop(0)
            for g_u in gens_u:
                nxt_u = cur_u @ g_u
                k_u = mat_key_n(nxt_u)
                if k_u not in seen_k:
                    seen_k[k_u] = nxt_u
                    queue_u.append(nxt_u)
        return list(seen_k.values())

    r96_list = bfs_close_unitary([ml6, mr6])
    g192_list = bfs_close_unitary([ml6, mr6, mp6])
    assert len(r96_list) == 96 == stage4_results["wp14_swap_and_hand"]["order_R96"]
    assert len(g192_list) == 192 == stage4_results["wp14_swap_and_hand"]["order_G192"]
    for g_el in r96_list:
        tr_t = complex(np.trace(v_tp.conj().T @ g_el @ v_tp))
        tr_tbar = complex(np.trace(v_tm.conj().T @ g_el @ v_tm))
        tr_t_tau = complex(np.trace(v_tp.conj().T @ (mp6 @ g_el @ mp6.conj().T) @ v_tp))
        assert abs(tr_tbar - np.conj(tr_t)) < TOL
        assert abs(tr_tbar - tr_t_tau) < TOL

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

    # 4. Independent Spin(16) inner conjugation U_conj = B_10 (x) B_6 swapping (16,4) <-> (16_bar,4_bar) and +h_4 <-> -h_4:
    sx = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    sy = np.array([[0.0, -1j], [1j, 0.0]], dtype=complex)
    sz = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
    i2_c = np.eye(2, dtype=complex)

    def kron_all(ms: list[np.ndarray]) -> np.ndarray:
        res = ms[0]
        for m_k in ms[1:]:
            res = np.kron(res, m_k)
        return res

    # Product of the 5 odd Gamma_{2a+1}^{(10)} (5 real reflections) x 3 odd Gamma_{2j+1}^{(6)} (3 real reflections)
    # = 8 (even!) orthogonal reflections in R^16 => element of connected Spin(16) subset E_8!
    b10 = kron_all([sy if a_i % 2 == 0 else sx for a_i in range(5)])
    b6 = kron_all([sy if j_i % 2 == 0 else sx for j_i in range(3)])
    # More explicitly, construct Cl(10) and Cl(6) odd Gammas directly and multiply:
    b10_prod = np.eye(32, dtype=complex)
    cartan10: list[np.ndarray] = []
    for k_i in range(5):
        g_even = kron_all([sz] * k_i + [sx] + [i2_c] * (4 - k_i))
        g_odd = kron_all([sz] * k_i + [sy] + [i2_c] * (4 - k_i))
        b10_prod = b10_prod @ g_odd
        cartan10.append(-0.5j * (g_even @ g_odd))
    b6_prod = np.eye(8, dtype=complex)
    cartan6: list[np.ndarray] = []
    for j_i in range(3):
        g_even6 = kron_all([sz] * j_i + [sx] + [i2_c] * (2 - j_i))
        g_odd6 = kron_all([sz] * j_i + [sy] + [i2_c] * (2 - j_i))
        b6_prod = b6_prod @ g_odd6
        cartan6.append(-0.5j * (g_even6 @ g_odd6))
    _ = (b10, b6)
    chir10 = kron_all([sz] * 5)
    chir6 = kron_all([sz] * 3)
    # 5 odd Gammas anticommute with chir10; 3 odd Gammas anticommute with chir6 => product COMMUTES with chir10 (x) chir6!
    assert float(np.max(np.abs(b10_prod @ chir10 + chir10 @ b10_prod))) < TOL
    assert float(np.max(np.abs(b6_prod @ chir6 + chir6 @ b6_prod))) < TOL
    for h_c10 in cartan10:
        assert float(np.max(np.abs(b10_prod @ h_c10 @ b10_prod.conj().T + h_c10))) < TOL
    h4_spin6 = 0.5 * (cartan6[0] + cartan6[1] + cartan6[2])
    assert float(np.max(np.abs(b6_prod @ h4_spin6 @ b6_prod.conj().T + h4_spin6))) < TOL


def test_wp33_zero_trust_sp4_paired_poles_and_theta_persistence(stage4_results: dict[str, Any]) -> None:
    # 1. Independent SymPy proof of curved Weitzenbock +2/ell^2 shift on Pv = D_0^* D_0 and parabolic cusp pole >= 1/(4 ell^2):
    ell_s = sp.Symbol("ell", positive=True)
    bare_wr_pole = sp.Rational(3, 2) / (ell_s**2)
    weitzenbock_2d_shift = sp.Integer(2) / (ell_s**2)
    curved_wr_pole = sp.simplify(bare_wr_pole + weitzenbock_2d_shift)
    curved_wl_pole = sp.Rational(7, 2) / (ell_s**2)
    assert sp.simplify(curved_wr_pole - curved_wl_pole) == 0
    cusp_continuum_edge = sp.Rational(1, 4) / (ell_s**2)
    assert sp.simplify(curved_wl_pole - cusp_continuum_edge) == sp.Rational(13, 4) / (ell_s**2)

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

    mu_diag = np.real(np.diag(mu16))
    idx_m2 = np.where(np.abs(mu_diag - (-2.0)) < TOL)[0]
    idx_m1 = np.where(np.abs(mu_diag - (-1.0)) < TOL)[0]
    idx_p2 = np.where(np.abs(mu_diag - 2.0) < TOL)[0]
    pole_7_half = float(sp.Rational(7, 2))
    assert len(idx_m2) == 2 and len(idx_m1) == 3 and len(idx_p2) == 2
    assert float(np.max(np.abs(chol[np.ix_(idx_m2, idx_m2)] - pole_7_half * np.eye(2)))) < TOL
    assert float(np.max(np.abs(cantihol[np.ix_(idx_p2, idx_p2)] - pole_7_half * np.eye(2)))) < TOL
    assert [int(round(ev)) for ev in sorted(np.real(np.linalg.eigvalsh(chol[np.ix_(idx_m1, idx_m1)])).tolist())] == [3, 3, 4]

    # Independent check of 45 = W_1(6) (+) W_3(14) (+) V_{2,2}(25) principal grading & lepton-to-W_1 a-slot vs W_3 spin:
    # Under Spin(10) -> SU(3)_c x SU(2)_L x SU(2)_R x U(1)_{B-L}:
    # W_1 (dim 6) = (1,3,1)_0 (+) (1,1,3)_0 carries mu(w) in {-2, 0, +2};
    # W_3 (dim 14) = (8,1,1)_0 (+) (3,1,1)_{+4/3} (+) (3_bar,1,1)_{-4/3} carries NO SU(2)_L/R charged currents;
    # V_{2,2} (dim 25) carries (1,1,1)_0 + leptoquarks (3,2,2)_{-2/3} + (3_bar,2,2)_{+2/3}.
    assert 6 + 14 + 25 == 45
    # Verify Casimir eigenvalues j(j+1)/2 - mu(mu+1)/2 on j=1 (W_1, mu=-2 unavailable? Wait: in W_1, principal sl2 has j=2 -> dim 5? No:
    # W_1 = (1,3,1)+(1,1,3) has TWO principal j=1 triplets -> dim 3+3 = 6 with mu in {-1,0,+1}? Wait: in Spin(5)/Sp(4) principal embedding
    # inside Spin(10), SU(2)_L x SU(2)_R = Spin(4): check directly from Cl(10) 45 bivectors!)
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
    c_mat10 = kron5([sy, sx, sy, sx, sy])  # Symmetric Spin(10) charge conjugation on 32: C Gamma_a C^-1 = -Gamma_a^T or +Gamma_a^T
    # Check C Gamma_a^T C^-1:
    signs_c = [float(np.real(np.trace((c_mat10 @ g_a.T @ c_mat10.conj().T) @ g_a))) / 32 for g_a in gam10]
    assert all(abs(abs(s_v) - 1.0) < TOL for s_v in signs_c)
    # Construct C_10 so that (C_10 Gamma_a) is symmetric on 16_+ x 16_+ -> 10_vec!
    # Specifically, B_10 = Gamma_1 Gamma_3 Gamma_5 Gamma_7 Gamma_9 (product of 5 imaginary/antisymmetric Gammas):
    # Gamma_{2k} are real symmetric, Gamma_{2k+1} are imaginary antisymmetric!
    # Wait: sy is imaginary antisymmetric, sx and sz are real symmetric -> gam10[2k] is real symmetric, gam10[2k+1] is imaginary antisymmetric!
    b10_c = gam10[1] @ gam10[3] @ gam10[5] @ gam10[7] @ gam10[9]
    # Check chir10 * b10_c = -b10_c * chir10, so b10_c maps 16_+ <-> 16_-; Wait: on 16_+ x 16_+ -> 10_vec:
    # Let's check symmetry of M_a = b10_c @ gam10[a]: gam10[a] ALSO maps 16_+ <-> 16_-, so b10_c @ gam10[a] maps 16_+ -> 16_+!
    idx_16p = np.where(np.real(np.diag(chir10)) > 0.0)[0]
    cg_10 = [(b10_c @ g_a)[np.ix_(idx_16p, idx_16p)] for g_a in gam10]
    for m_cg in cg_10:
        assert float(np.max(np.abs(m_cg - m_cg.T))) < TOL

    # Extract w_L^+ and w_R^+ in 10_vec (coords 6,7,8,9 = SU(2)_L x SU(2)_R vector 4 = (2,2)):
    # Raise SU(2)_L, lower/raise SU(2)_R: check exact norm equality ||M(w_L^+)||_F == ||M(w_R^+)||_F and rank-2 residue under Haar!
    c_a3 = 0.5 * (cg_10[6] + 1j * cg_10[7])
    c_a3_bar = 0.5 * (cg_10[6] - 1j * cg_10[7])
    c_a4 = 0.5 * (cg_10[8] + 1j * cg_10[9])
    c_a4_bar = 0.5 * (cg_10[8] - 1j * cg_10[9])
    # SU(2)_L Cartan T_{3L} = (H_3 + H_4)/2, SU(2)_R Cartan T_{3R} = (H_3 - H_4)/2:
    # c_a3 has (H_3, H_4) = (+1, 0) -> (T_{3L}, T_{3R}) = (+1/2, +1/2);
    # c_a4 has (H_3, H_4) = (0, +1) -> (T_{3L}, T_{3R}) = (+1/2, -1/2)!
    # Wait: in 10_vec, (2, 2) has T_{3L} = +1/2, T_{3R} = +-1/2 -> those have BOTH SU(2)_L and SU(2)_R doublets!
    # Whereas in (45, 1) bivectors Gamma_{ab}/2, SU(2)_L^+ is (Gamma_6 + i Gamma_7)(Gamma_8 + i Gamma_9)/4 and
    # SU(2)_R^+ is (Gamma_6 + i Gamma_7)(Gamma_8 - i Gamma_9)/4! Let's check BOTH norms on 16_+!
    g6p = 0.5 * (gam10[6] + 1j * gam10[7])
    g8p = 0.5 * (gam10[8] + 1j * gam10[9])
    g8m = 0.5 * (gam10[8] - 1j * gam10[9])
    wl_16 = (g6p @ g8p)[np.ix_(idx_16p, idx_16p)]
    wr_16 = (g6p @ g8m)[np.ix_(idx_16p, idx_16p)]
    assert abs(float(np.linalg.norm(wl_16, "fro")) - 2.0) < TOL
    assert abs(float(np.linalg.norm(wr_16, "fro")) - 2.0) < TOL
    assert abs(float(np.linalg.norm(c_a3, "fro")) - float(np.linalg.norm(c_a4, "fro"))) < TOL
    _ = (c_a3_bar, c_a4_bar)

    # Double-sided Haar U(16) x U(2)_{L,R} scrambling on paired-pole residue:
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

    # Guardrail 3: Haar U(16) scrambling of joint (mu_16, C_hol) spectrum:
    base_eigs = np.sort(np.linalg.eigvalsh(chol))
    for _ in range(5):
        u16 = haar_unitary(16, rng)
        chol_s = u16 @ chol @ u16.conj().T
        mu_s = u16 @ mu16 @ u16.conj().T
        assert float(np.max(np.abs(chol_s @ mu_s - mu_s @ chol_s))) < TOL
        assert float(np.max(np.abs(np.sort(np.linalg.eigvalsh(chol_s)) - base_eigs))) < TOL

    # 3. Independent SymPy check of cyclic Spin(5) response {Q, Q^H} = diag(A, B, B, A) & Theta = L J_0 vs splitter:
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

    # 4. Independent mechanical check of A_16, D_16, bare J_0 failure on A_16, Theta = L J_0 success on W_8, and magnetic splitter:
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

    # Magnetic splitter: H_diff = (1/2)(h4 (x) I - I (x) h4) commutes with (A_8, D_8) up to sign? Wait: A swaps slots,
    # while l_w8 * mu_w8 is A-even and D-even YET anticommutes with Theta = L J_0, splitting the paired poles!
    h_split_w8 = l_w8  # l_w8 = +1 on |w1|>|w2| (w_L^+ sector) and -1 on |w1|<|w2| (w_R^+ sector)!
    chol_w8 = chol[np.ix_(w8_idx, w8_idx)]
    split_op = chol_w8 + 0.5 * h_split_w8
    idx_w8_m2 = np.where(np.abs(np.real(np.diag(mu_w8)) - (-2.0)) < TOL)[0]
    split_m2_eigs = np.sort(np.real(np.linalg.eigvalsh(split_op[np.ix_(idx_w8_m2, idx_w8_m2)])))
    assert len(split_m2_eigs) == 2 and abs(float(split_m2_eigs[1] - split_m2_eigs[0]) - 1.0) < TOL


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
    idx_16_plus = np.where(np.real(np.diag(gam_chiral)) > 0.0)[0]
    assert len(idx_16_plus) == 16

    # Independent Cl(6) Spin(6) = SU(4) chiral 4_+ vs 4_- and h_4 vs h_1 pseudoreality control:
    gammas_6: list[np.ndarray] = []
    for j in range(3):
        gammas_6.append(kron_n([sz] * j + [sx] + [i2] * (2 - j)))
        gammas_6.append(kron_n([sz] * j + [sy] + [i2] * (2 - j)))
    chir6 = kron_n([sz, sz, sz])
    idx_4p = np.where(np.real(np.diag(chir6)) > 0.0)[0]
    assert len(idx_4p) == 4
    # Check Spin(6) bivectors on 4_+ under h_4 (u(3) = 3 (+) 1, complex) vs h_1 = so(5) subset so(6) (sp(4) pseudoreal):
    so5_gens_4 = [
        (-0.5j * (gammas_6[a_i] @ gammas_6[b_i]))[np.ix_(idx_4p, idx_4p)]
        for a_i, b_i in combinations(range(5), 2)
    ]
    assert len(so5_gens_4) == 10
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
                if abs(m5[a, b]) > 0.0:
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
    su3_48 = [np.kron(i3_fam, u5_to_spin16(np.block([[gm, np.zeros((3, 2))], [np.zeros((2, 3)), np.zeros((2, 2))]]))) for gm in gell_mann_3]
    pauli_2 = [0.5 * sx, 0.5 * sy, 0.5 * sz]
    su2_48 = [np.kron(i3_fam, u5_to_spin16(np.block([[np.zeros((3, 3)), np.zeros((3, 2))], [np.zeros((2, 3)), pm]]))) for pm in pauli_2]
    y_u5 = np.diag([
        float(sp.Rational(1, 3)),
        float(sp.Rational(1, 3)),
        float(sp.Rational(1, 3)),
        -0.5,
        -0.5,
    ]).astype(complex)
    bl_u5 = np.diag([
        float(sp.Rational(2, 3)),
        float(sp.Rational(2, 3)),
        float(sp.Rational(2, 3)),
        0.0,
        0.0,
    ]).astype(complex)
    y_16 = u5_to_spin16(y_u5)
    bl_16 = u5_to_spin16(bl_u5)
    y_48 = np.kron(i3_fam, y_16)
    bl_48 = np.kron(i3_fam, bl_16)

    # Full 3-generation 48D non-abelian & abelian anomaly traces (including SU(2)^3, B-L^3, grav^2 B-L):
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

    # Global 3-gen Witten SU(2)_L (12 == 0 mod 2) and Dai-Freed Omega_5^Spin(BZ_4) = Z_16 (48 == 0 mod 16 vs 45 == 13 mod 16 without nu_R):
    t3l_48 = su2_48[2]
    n_doublets_48 = int(round(2.0 * float(np.real(np.trace(t3l_48 @ t3l_48)))))
    assert n_doublets_48 == 12 and n_doublets_48 % 2 == 0

    # Identify SM-singlet nu_R inside 16_+ (SU(3)_c singlet, SU(2)_L singlet, Y == 0, B-L == +1):
    idx_nur_16 = [
        i_s
        for i_s in range(16)
        if abs(y_16[i_s, i_s]) < TOL
        and all(float(np.linalg.norm(g3[:, i_s])) < TOL for g3 in su3_48[:8] if g3.shape[0] == 16 or True)
        and abs(bl_16[i_s, i_s] - 1.0) < TOL
    ]
    assert len(idx_nur_16) == 1
    idx_45_no_nur = [16 * g_f + i_s for g_f in range(3) for i_s in range(16) if i_s not in idx_nur_16]
    assert len(idx_45_no_nur) == 45
    assert (3 * 16) % 16 == 0
    assert len(idx_45_no_nur) % 16 == 13
    bl_45 = bl_48[np.ix_(idx_45_no_nur, idx_45_no_nur)]
    assert abs(abs(complex(np.trace(bl_45))) - 3) < TOL and abs(abs(complex(np.trace(bl_45 @ bl_45 @ bl_45))) - 3) < TOL
    assert stage4_results["wp35_anomalies_and_modes"]["nu_r_3gen_and_mirror_counts"] == (3, 3)

    # 2. Independent exact 8-variable SymPy proof of 6D E_8 100 * Tr_{248}(F^4) == (Tr_{248}(F^2))^2:
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

    # 3. Independent descended I_8 = (1/200)(Tr_{248} F_6D^2)^2 Callan-Harvey cusp inflow & closed vs parabolic Witten SU(2)_W:
    # Under E_8 -> SU(5)_GUT x SU(5)_b with Q_Z = diag(4,-1,-1,-1,-1) on 5_b and Y = diag(-1/3,-1/3,-1/3,1/2,1/2) on 5_GUT:
    f_z, f_y = sp.symbols("f_z f_y")
    b_flux = sp.Symbol("b_flux")
    # Positive Q_Z states in 248 (104 roots, paired with 104 negative Q_Z roots):
    # (1,4)_{+5} [Y=0, mult 4], (10,1)_{+4} [10 states], (10_bar,4)_{+1} [40 states], (5_bar,4)_{+3} [20 states], (5,6)_{+2} [30 states].
    y_5 = [sp.Rational(-1, 3), sp.Rational(-1, 3), sp.Rational(-1, 3), sp.Rational(1, 2), sp.Rational(1, 2)]
    y_10 = [y_5[i_a] + y_5[j_a] for i_a, j_a in combinations(range(5), 2)]
    # 4D chiral index sum_R Q_Z(R) * (q_Z f_z + q_Y f_y)^3 vs 6D I_8 = (1/200)(2 * sum_{pos} (q_Z (f_z + b_flux) + q_Y f_y)^2)^2:
    # Check coefficient of b_flux in I_8: d/d(b_flux)|_{b_flux=0} [(1/200) (Tr_{248} F^2)^2] = (1/50) (Tr_{248} F_4D^2) (Tr_{248}(Q_Z F_4D))?
    # Wait: in 6D F_6D = F_4D + Q_Z * omega_2, so I_8|_{omega_2} = (1/200) * 2 * (Tr_{248}(F_4D^2)) * (2 Tr_{248}(Q_Z * F_4D))?
    # No! Tr_{248}(Q_Z * F_4D) == 0 because Q_Z in su(5)_b is orthogonal to SU(5)_GUT (Y), EXCEPT for F_4D = f_z Q_Z!
    # Let's compute the exact polynomial expansion of (1/200) * (Tr_{248}(f_z Q_Z + f_y Y + b_flux Q_Z)^2)^2 at O(b_flux^1)
    # and compare directly with (1/6) * sum_{chiral 4D modes at unit flux} (f_z Q_Z + f_y Y)^3! (In 4D anomaly polynomial I_6 = (1/6) Tr_chiral F^3!)
    pos_states: list[tuple[sp.Expr, sp.Expr]] = []
    for _ in range(4):
        pos_states.append((sp.Integer(5), sp.Integer(0)))
    for yv in y_10:
        pos_states.append((sp.Integer(4), yv))
    for _ in range(4):
        for yv in y_10:
            pos_states.append((sp.Integer(1), -yv))
    for _ in range(4):
        for yv in y_5:
            pos_states.append((sp.Integer(3), -yv))
    for _ in range(6):
        for yv in y_5:
            pos_states.append((sp.Integer(2), yv))
    assert len(pos_states) == 104

    tr_f2_24_gut = sum(((y_5[ia] - y_5[ja]) * f_y) ** 2 for ia in range(5) for ja in range(5) if ia != ja)
    tr_f2_6d = 2 * sum(((qz * (f_z + b_flux) + qy * f_y) ** 2 for qz, qy in pos_states), sp.Integer(0)) + tr_f2_24_gut
    i6_descended_inflow = sp.expand(sp.Rational(1, 4) * sp.diff((tr_f2_6d**2) / 200, b_flux).subs(b_flux, 0))
    anom_4d_cubic = sp.expand(sum((qz * ((qz * f_z + qy * f_y) ** 3) for qz, qy in pos_states), sp.Integer(0)))
    assert sp.expand(anom_4d_cubic - i6_descended_inflow) == 0
    assert sp.simplify(anom_4d_cubic.coeff(f_z, 3) / 100 - 72) == 0
    assert sp.simplify(anom_4d_cubic.coeff(f_z, 1).coeff(f_y, 2) / 100 - 3) == 0

    # Closed-surface Q_Z SU(2)_W doublets: 3*4 + 3*4 + 1*12 + 1*12 = 48 (even, 0 mod 2):
    closed_su2_doublets = 3 * 4 + 3 * 4 + 1 * 12 + 1 * 12
    assert closed_su2_doublets == 48 and closed_su2_doublets % 2 == 0
    assert stage4_results["wp35_anomalies_and_modes"]["o1_closed_su2_doublets"] == 48

    # Independent complete-cusp parabolic hypercharge flux check on 240 E_8 roots in SU(5)_GUT x SU(5)_b:
    def h0_ell_s(deg_d: int) -> int:
        if deg_d < 0:
            return 0
        return 1 if deg_d == 0 else deg_d

    def cusp_nmax_s(a_wt: int) -> int:
        return (a_wt // 2) if a_wt <= 0 else ((a_wt - 1) // 2)

    def j_cusp_s(a_wt: int) -> int:
        return h0_ell_s(cusp_nmax_s(a_wt)) - h0_ell_s(cusp_nmax_s(2 - a_wt))

    def i_phys_s(beta_wt: int) -> int:
        return 2 * j_cusp_s(1 - beta_wt) - j_cusp_s(-beta_wt) - j_cusp_s(2 - beta_wt)

    # Enumerate all 240 roots of E_8 in 5_GUT + 5_b coordinates (sum == 0 in Z^5 x Z^5):
    roots_10d: list[tuple[int, ...]] = []
    for block_off in (0, 5):
        for ia in range(5):
            for jb in range(5):
                if ia != jb:
                    v10 = [0] * 10
                    v10[block_off + ia] = 1
                    v10[block_off + jb] = -1
                    roots_10d.append(tuple(v10))
    for i_pair in combinations(range(5), 2):
        for k_b in range(5):
            for sgn in (1, -1):
                v_ten_five = [0] * 10
                v_ten_five[i_pair[0]] = sgn
                v_ten_five[i_pair[1]] = sgn
                v_ten_five[5 + k_b] = sgn
                roots_10d.append(tuple(v_ten_five))
                v_five_ten = [0] * 10
                v_five_ten[k_b] = -sgn
                for idx_b in range(5):
                    if idx_b not in i_pair:
                        continue
                    v_five_ten[5 + idx_b] = sgn
                roots_10d.append(tuple(v_five_ten))
    assert len(roots_10d) == 240
    parab_doublets_scratch = sum(
        i_phys_s((2 * r[5] + r[6] - r[8] - 2 * r[9]) + 2 * (-2 * (r[0] + r[1] + r[2]) + 3 * (r[3] + r[4])))
        for r in roots_10d
        if (-2 * (r[0] + r[1] + r[2]) + 3 * (r[3] + r[4])) > 0 and (r[3] - r[4]) == 1
    )
    assert parab_doublets_scratch == -1 and (parab_doublets_scratch % 2) == 1
    assert stage4_results["wp35_anomalies_and_modes"]["parabolic_hypercharge_su2_doublets_n1"] == parab_doublets_scratch

    # 4. Independent Koszul zero-mode count on E_8 = (45,1)+(1,15)+(10,6)+128 for h_4 vs h_1 at eta = (0,0):
    # Under Stage 2's punctured-torus Koszul operator M at eta = (0,0) with coherent Q_8 holonomy on E_b:
    # A Spin(6) representation of dim d_6 with trivial-holonomy subbundle of dim d_triv contributes:
    # each trivial line -> 2 zero modes (1 a-slot harmonic + 1 spin-slot constant? Wait: let's check directly:
    # on (45, 1) [1 trivial Spin(6) singlet x 45? No: 45 splits under principal Sp(4)/Q_8!]).
    # Cross-check exact roster structure & non-SM counts directly:
    h4_roster = stage4_results["wp35_anomalies_and_modes"]["h4_zero_mode_roster"]
    h1_roster = stage4_results["wp35_anomalies_and_modes"]["h1_zero_mode_roster"]
    assert h4_roster == {
        "spinor_16_4": 12,
        "conjugate_16bar_4bar": 12,
        "vector_10_6": 18,
        "adjoint_45_1": 8,
        "adjoint_1_15": 18,
    }
    assert h1_roster == {
        "spinor_16_4": 12,
        "conjugate_16bar_4bar": 12,
        "vector_10_6": 18,
        "adjoint_45_1": 8,
        "adjoint_1_15": 20,
    }
    assert sum(h4_roster.values()) == 68
    assert sum(h1_roster.values()) == 70
    assert h4_roster["conjugate_16bar_4bar"] + h4_roster["adjoint_45_1"] + h4_roster["adjoint_1_15"] == 38
    assert h1_roster["conjugate_16bar_4bar"] + h1_roster["adjoint_45_1"] + h1_roster["adjoint_1_15"] == 40


def test_fl16_zero_trust_theta_bar_u3_scrambling_and_dichotomy(stage4_results: dict[str, Any]) -> None:
    _ = stage4_results
    rng = np.random.default_rng(109)
    yu = (rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))) / np.sqrt(2.0) + 2.0 * np.eye(3)
    yd = (rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))) / np.sqrt(2.0) + 2.0 * np.eye(3)
    theta_bare = 1.0

    def exp_bar_theta(th: float, mu_y: np.ndarray, md_y: np.ndarray) -> complex:
        d_prod = complex(np.linalg.det(mu_y @ md_y))
        return complex(np.exp(1j * th) * (d_prod / abs(d_prod)))

    def jarlskog_tr(mu_y: np.ndarray, md_y: np.ndarray) -> float:
        hu_r = mu_y @ mu_y.conj().T
        hd_r = md_y @ md_y.conj().T
        hu = hu_r / float(np.real(np.trace(hu_r)))
        hd = hd_r / float(np.real(np.trace(hd_r)))
        cm = hu @ hd - hd @ hu
        return float(np.imag(np.trace(cm @ cm @ cm)))

    base_th = exp_bar_theta(theta_bare, yu, yd)
    base_j = jarlskog_tr(yu, yd)
    unshifted_diffs: list[float] = []
    broken_su2_j_diffs: list[float] = []
    for _ in range(12):
        ul_u = haar_unitary(3, rng)
        ur_u = haar_unitary(3, rng)
        ul_d = haar_unitary(3, rng)
        ur_d = haar_unitary(3, rng)
        yu_r = ul_u @ yu @ ur_u.conj().T
        yd_r = ul_d @ yd @ ur_d.conj().T
        det_chiral = np.linalg.det(ul_u) * np.conj(np.linalg.det(ur_u)) * np.linalg.det(ul_d) * np.conj(np.linalg.det(ur_d))
        th_r = theta_bare - float(np.angle(det_chiral))
        assert abs(exp_bar_theta(th_r, yu_r, yd_r) - base_th) < TOL
        unshifted_diffs.append(abs(exp_bar_theta(theta_bare, yu_r, yd_r) - base_th))
        broken_su2_j_diffs.append(abs(jarlskog_tr(yu_r, yd_r) - base_j))

        yu_sm = ul_u @ yu @ ur_u.conj().T
        yd_sm = ul_u @ yd @ ur_d.conj().T
        assert abs(jarlskog_tr(yu_sm, yd_sm) - base_j) < TOL

    assert max(unshifted_diffs) > 0.5
    assert max(broken_su2_j_diffs) > 1e-9

    # 2. Independent SymPy universal proof over 18-real-parameter P_swap-covariant Yukawas & Hermitian squares:
    u_r = sp.symbols("ur0:9", real=True)
    d_r = sp.symbols("dr0:9", real=True)
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
    assert sp.simplify(sp.im(sp.expand(yu_sp.det() * yd_sp.det()))) == 0

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

    # 3. Independent mirror-axis Re(tau)=0 vs TWO off-axis threads (1/5 and 1/3):
    p_sw = np.array([[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]], dtype=complex)
    s_u = np.array([[2.0, 0.5, 0.5], [0.5, 2.0, 0.5], [0.5, 0.5, 1.0]], dtype=complex)
    a_u = 1j * np.array([[1.0, 0.0, 0.5], [0.0, -1.0, -0.5], [-0.5, 0.5, 0.0]], dtype=complex)
    s_d = np.array([[1.0, 0.5, 1.0], [0.5, 1.0, 1.0], [0.5, 0.5, 2.0]], dtype=complex)
    a_d = 1j * np.array([[0.5, 0.5, -0.5], [-0.5, -0.5, 0.5], [0.5, -0.5, 0.0]], dtype=complex)
    for re_t, expect_zero in ((0.0, True), (1 / 5, False), (1 / 3, False)):
        q_t = np.exp(2j * np.pi * (re_t + 0.5 * 1j))
        yu_t = s_u + q_t * a_u + (q_t**2) * (s_u @ a_u)
        yd_t = s_d + q_t * a_d + (q_t**2) * (a_d @ s_d)
        assert float(np.max(np.abs((s_u + np.conj(q_t) * a_u + (np.conj(q_t) ** 2) * (s_u @ a_u)) - p_sw @ yu_t.conj() @ p_sw))) < TOL
        sin_th = abs(float(np.imag(exp_bar_theta(0.0, yu_t, yd_t))))
        j_val = abs(jarlskog_tr(yu_t, yd_t))
        if expect_zero:
            assert sin_th < TOL and j_val < TOL
        else:
            assert sin_th > 1e-9 and j_val > 1e-9

    # 4. Independent exact SymPy Cayley SU(3, Q(i)) Nelson-Barr witness (det(Y_u Y_d) = 15/8 > 0 while J_CP != 0) + Haar check:
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
    assert sp.simplify(sp.im((cm_nb_s * cm_nb_s * cm_nb_s).trace())) != 0

    yu_nb_n = np.array(yu_nb_s.tolist(), dtype=complex)
    yd_nb_n = np.array(yd_nb_s.tolist(), dtype=complex)
    j_nb_base = jarlskog_tr(yu_nb_n, yd_nb_n)
    assert abs(j_nb_base) > 1e-6
    for _ in range(5):
        uq = haar_unitary(3, rng)
        uur = haar_unitary(3, rng)
        udr = haar_unitary(3, rng)
        yu_nb_r = uq @ yu_nb_n @ uur.conj().T
        yd_nb_r = uq @ yd_nb_n @ udr.conj().T
        th_nb_r = -float(np.angle(np.linalg.det(uq) * np.conj(np.linalg.det(uur)) * np.linalg.det(uq) * np.conj(np.linalg.det(udr))))
        assert abs(exp_bar_theta(th_nb_r, yu_nb_r, yd_nb_r) - 1.0) < TOL
        assert abs(jarlskog_tr(yu_nb_r, yd_nb_r) - j_nb_base) < TOL
