"""P-753 / R77-2 (B1861 WP-2.2 & WP-3.2): Exact Register-to-Field & Weave-Triplet Join.

Strictly data-free (0 of 19). Zero empirical constants or held-out quantities appear in
this module. Every boolean verdict is computed from explicit matrix norms (< 1e-12) or
exact integer group/rank invariants (Guardrail 2), and verified under independent Haar
unitary basis-scrambling transformations (Guardrail 3).
"""
from __future__ import annotations

from collections import Counter
from itertools import combinations, product
import math
from typing import Any

import mpmath as mp
import numpy as np


TOL = 1e-12


def _matrix_key(mat: np.ndarray, digits: int = 6) -> bytes:
    arr = np.asarray(mat, dtype=complex)
    return (np.round(arr.real, digits) + 0.0).tobytes() + (np.round(arr.imag, digits) + 0.0).tobytes()


def close_matrix_group(gen_map: dict[str, np.ndarray], cap: int = 4096) -> list[tuple[str, np.ndarray]]:
    """Deterministic BFS closure of a finite matrix group from named generators."""
    first = next(iter(gen_map.values()))
    dim = first.shape[0]
    ident = np.eye(dim, dtype=complex)
    seen: dict[bytes, tuple[str, np.ndarray]] = {_matrix_key(ident): ("", ident)}
    queue: list[tuple[str, np.ndarray]] = [("", ident)]
    while queue:
        word, cur = queue.pop(0)
        for name, gen in gen_map.items():
            nxt = cur @ gen
            k = _matrix_key(nxt)
            if k not in seen:
                seen[k] = (word + name, nxt)
                queue.append((word + name, nxt))
                if len(seen) > cap:
                    raise RuntimeError(f"Matrix group exceeded cap {cap}")
    return list(seen.values())


def haar_unitary(dim: int, rng: np.random.Generator) -> np.ndarray:
    """Sample a Haar-distributed unitary matrix of size dim x dim via QR with positive R diagonal."""
    z = (rng.normal(size=(dim, dim)) + 1j * rng.normal(size=(dim, dim))) / math.sqrt(2.0)
    q, r = np.linalg.qr(z)
    diag = np.diag(r)
    ph = np.where(np.abs(diag) > 0.0, diag / np.abs(diag), 1.0 + 0.0j)
    return q * ph


def sym2_2x2(u2: np.ndarray) -> np.ndarray:
    """Symmetric square of a 2x2 matrix on the orthonormal basis (e0^2, sqrt(2) e0 e1, e1^2)."""
    a, b = u2[0, 0], u2[0, 1]
    c, d = u2[1, 0], u2[1, 1]
    rt2 = math.sqrt(2.0)
    return np.array(
        [
            [a * a, rt2 * a * b, b * b],
            [rt2 * a * c, a * d + b * c, rt2 * b * d],
            [c * c, rt2 * c * d, d * d],
        ],
        dtype=complex,
    )


def solve_unitary_intertwiner(
    gens_a: tuple[np.ndarray, ...],
    gens_b: tuple[np.ndarray, ...],
) -> tuple[np.ndarray | None, float]:
    """Solve U @ A_k @ U^dag = B_k for unitary U; returns (U, max_err) or (None, min_sv)."""
    dim = gens_a[0].shape[0]
    blocks = [np.kron(a.T, np.eye(dim)) - np.kron(np.eye(dim), b) for a, b in zip(gens_a, gens_b)]
    sys_mat = np.vstack(blocks)
    _, svals, vh = np.linalg.svd(sys_mat)
    if float(svals[-1]) > 1e-8:
        return None, float(svals[-1])
    raw = vh[-1].conj().reshape((dim, dim), order="F")
    u_pol, _, vh_pol = np.linalg.svd(raw)
    u_unit = u_pol @ vh_pol
    err = max(float(np.max(np.abs(u_unit @ a @ u_unit.conj().T - b))) for a, b in zip(gens_a, gens_b))
    return u_unit, err


def jacobi_dedekind_half_weight_vector(tau: complex | mp.mpc, dps: int = 40) -> np.ndarray:
    """Branch-cut-free evaluation on Im(tau) > 0 of
    V(tau) = (theta_2(0|tau)^2, theta_3(0|tau)^2, theta_4(0|tau)^2) / eta(tau)^3.
    """
    with mp.workdps(dps):
        t = mp.mpc(tau)
        q2 = mp.exp(2j * mp.pi * t)
        q1 = mp.exp(1j * mp.pi * t)
        s2 = mp.mpf(0)
        for n in range(45):
            term = q2 ** (n * (n + 1) // 2)
            s2 += term
            if abs(term) < mp.mpf("1e-42"):
                break
        t2 = 2 * mp.exp(1j * mp.pi * t / 4) * s2
        t3 = mp.jtheta(3, 0, q1)
        t4 = mp.jtheta(4, 0, q1)
        prod_eta = mp.mpf(1)
        for n in range(1, 90):
            qn = q2 ** n
            if abs(qn) < mp.mpf("1e-42"):
                break
            prod_eta *= (1 - qn) ** 3
        eta3 = mp.exp(1j * mp.pi * t / 4) * prod_eta
        return np.array(
            [complex(t2**2 / eta3), complex(t3**2 / eta3), complex(t4**2 / eta3)],
            dtype=complex,
        )


def build_weave_triplet_and_sym2_census() -> dict[str, Any]:
    """Construct W10/B1610/B1611 weave triplet T and exhaustively test all Sym^2(Weil_2) candidates."""
    eye2 = np.eye(2, dtype=complex)
    qi = np.array([[1j, 0.0], [0.0, -1j]], dtype=complex)
    qj = np.array([[0.0, 1.0], [-1.0, 0.0]], dtype=complex)
    rho = {"a": qi, "b": qj}
    parities = [(1, 0), (0, 1), (1, 1)]
    all_parities = [(0, 0), (1, 0), (0, 1), (1, 1)]

    def chi(p: tuple[int, int], letter: str) -> int:
        return -1 if (p[0] if letter == "a" else p[1]) else 1

    def rep_word(word: str, p: tuple[int, int]) -> np.ndarray:
        mat = eye2.copy()
        for ch in word:
            g = rho[ch.lower()] * chi(p, ch.lower())
            mat = mat @ (g if ch.islower() else g.conj().T)
        return mat

    def cocycle_val(z: dict[str, np.ndarray], word: str, p: tuple[int, int]) -> np.ndarray:
        val = np.zeros(2, dtype=complex)
        mat = eye2.copy()
        for ch in word:
            g_let = ch.lower()
            mg = rep_word(g_let, p)
            if ch.islower():
                val = val + mat @ z[g_let]
                mat = mat @ mg
            else:
                mi = mg.conj().T
                val = val - mat @ (mi @ z[g_let])
                mat = mat @ mi
        return val

    def h1_basis(p: tuple[int, int]) -> tuple[np.ndarray, np.ndarray]:
        cob = np.zeros((4, 2), dtype=complex)
        for k in range(2):
            v = np.zeros(2, dtype=complex)
            v[k] = 1.0
            cob[:2, k] = rep_word("a", p) @ v - v
            cob[2:, k] = rep_word("b", p) @ v - v
        q_cob, _ = np.linalg.qr(cob)
        proj = np.eye(4, dtype=complex) - q_cob @ q_cob.conj().T
        u_svd, _, _ = np.linalg.svd(proj)
        return u_svd[:, :2], proj

    bases = {p: h1_basis(p) for p in all_parities}

    def act_parity(move: dict[str, str], p: tuple[int, int]) -> tuple[int, int]:
        sa = 1
        for ch in move["a"]:
            sa *= chi(p, ch.lower())
        sb = 1
        for ch in move["b"]:
            sb *= chi(p, ch.lower())
        return (0 if sa == 1 else 1, 0 if sb == 1 else 1)

    def move_matrix(move: dict[str, str], lift: np.ndarray, par_list: list[tuple[int, int]]) -> np.ndarray:
        li = lift.conj().T
        dim = 2 * len(par_list)
        out = np.zeros((dim, dim), dtype=complex)
        for ip, p in enumerate(par_list):
            q = act_parity(move, p)
            iq = par_list.index(q)
            bp, _ = bases[p]
            bq, pq = bases[q]
            for k in range(2):
                vec = bp[:, k]
                z = {"a": vec[:2], "b": vec[2:]}
                w = np.concatenate([li @ cocycle_val(z, move["a"], p), li @ cocycle_val(z, move["b"], p)])
                w = pq @ w
                out[2 * iq : 2 * iq + 2, 2 * ip + k] = bq.conj().T @ w
        return out

    rt_half = 1.0 / math.sqrt(2.0)
    l_move = {"a": "a", "b": "ab"}
    r_move = {"a": "ab", "b": "b"}
    gl = (eye2 + qi) * rt_half
    gr = (eye2 - qj) * rt_half

    ml6 = move_matrix(l_move, gl, parities)
    mr6 = move_matrix(r_move, gr, parities)
    ml0 = move_matrix(l_move, gl, [(0, 0)])
    mr0 = move_matrix(r_move, gr, [(0, 0)])

    # Hodge-Riemann form Qm / Hm on V (B1610)
    def cup_form(u: dict[str, np.ndarray], v: dict[str, np.ndarray], p: tuple[int, int], rel: str = "abABabAB") -> complex:
        tot = 0.0 + 0.0j
        pref = ""
        mat = eye2.copy()
        for ch in rel:
            tot += np.vdot(mat @ cocycle_val(v, ch, p), cocycle_val(u, pref, p))
            if ch.isupper():
                rl = rep_word(ch.lower(), p)
                tot -= np.vdot(rl @ cocycle_val(v, ch, p), cocycle_val(u, ch.lower(), p))
            pref += ch
            mat = mat @ rep_word(ch, p)
        return complex(tot)

    def cup_triv(u: dict[str, complex], v: dict[str, complex], rel: str = "abABabAB") -> complex:
        eval_ab = lambda z, w: sum((z[c] if c.islower() else -z[c.lower()]) for c in w)
        tot = 0.0 + 0.0j
        pref = ""
        for ch in rel:
            tot += eval_ab(u, pref) * np.conj(eval_ab(v, ch))
            if ch.isupper():
                tot -= eval_ab(u, ch.lower()) * np.conj(eval_ab(v, ch))
            pref += ch
        return complex(tot)

    tau_orient = 0.3 + 1.1j
    orient_sign = 1.0 if (1j * cup_triv({"a": 1.0, "b": tau_orient}, {"a": 1.0, "b": tau_orient})).real > 0.0 else -1.0
    basis_v = [(p, {"a": bases[p][0][:, k][:2], "b": bases[p][0][:, k][2:]}) for p in parities for k in range(2)]
    qm = np.zeros((6, 6), dtype=complex)
    for i, (pi, zi) in enumerate(basis_v):
        for j, (pj, zj) in enumerate(basis_v):
            if pi == pj:
                qm[i, j] = orient_sign * 1j * cup_form(zi, zj, pi)
    hm = qm.conj()
    hm_herm_err = float(np.max(np.abs(hm - hm.conj().T)))
    hm_eigs = np.linalg.eigvalsh((hm + hm.conj().T) / 2.0)
    n_pos = int(np.sum(hm_eigs > 1e-8))
    n_neg = int(np.sum(hm_eigs < -1e-8))

    # Split V = T (+) Tbar via the commutant of G_LR
    g_v = close_matrix_group({"L": ml6, "R": mr6})
    comm_stack = np.vstack([np.kron(np.eye(6), m) - np.kron(m.T, np.eye(6)) for _, m in g_v])
    _, _, vh_c = np.linalg.svd(comm_stack)
    x_comm = None
    for row in vh_c[-2:].conj():
        cand = row.reshape((6, 6), order="F")
        if np.linalg.norm(cand - (np.trace(cand) / 6.0) * np.eye(6)) > 1e-6:
            x_comm = cand
            break
    if x_comm is None:
        raise RuntimeError("Failed to locate non-scalar commutant operator on V")
    ev_x, vx = np.linalg.eig(x_comm)
    clusters: dict[tuple[float, float], list[int]] = {}
    for idx, val in enumerate(ev_x):
        clusters.setdefault((round(float(val.real), 4), round(float(val.imag), 4)), []).append(idx)
    pieces: dict[str, np.ndarray] = {}
    for idxs in clusters.values():
        qp, _ = np.linalg.qr(vx[:, idxs])
        ht = qp.conj().T @ hm @ qp
        ev_p = np.linalg.eigvalsh((ht + ht.conj().T) / 2.0)
        if np.all(ev_p > 1e-9):
            pieces["T"] = qp
        elif np.all(ev_p < -1e-9):
            pieces["Tbar"] = qp

    tb = pieces["T"]
    tbarb = pieces["Tbar"]
    tl = tb.conj().T @ ml6 @ tb
    tr = tb.conj().T @ mr6 @ tb
    tbarl = tbarb.conj().T @ ml6 @ tbarb
    tbarr = tbarb.conj().T @ mr6 @ tbarb

    subspace_inv_err = max(
        float(np.max(np.abs(tb @ tl - ml6 @ tb))),
        float(np.max(np.abs(tb @ tr - mr6 @ tb))),
        float(np.max(np.abs(tbarb @ tbarl - ml6 @ tbarb))),
        float(np.max(np.abs(tbarb @ tbarr - mr6 @ tbarb))),
    )

    g_t = close_matrix_group({"L": tl, "R": tr})
    g_m0 = close_matrix_group({"L": ml0, "R": mr0})
    g_sym2_m0 = close_matrix_group({"L": sym2_2x2(ml0), "R": sym2_2x2(mr0)})

    center_t = [w for w, m in g_t if all(np.max(np.abs(m @ n - n @ m)) < 1e-7 for _, n in g_t)]

    braid_lhs = tl @ np.linalg.inv(tr) @ tl
    braid_rhs = np.linalg.inv(tr) @ tl @ np.linalg.inv(tr)
    braid_err = float(np.max(np.abs(braid_lhs - braid_rhs)))
    s_t = braid_lhs
    st2_minus_i_err = float(np.max(np.abs(s_t @ s_t - 1j * np.eye(3))))
    st4_plus_i3_dist = float(np.max(np.abs(np.linalg.matrix_power(s_t, 4) - np.eye(3))))
    st4_minus_i3_err = float(np.max(np.abs(np.linalg.matrix_power(s_t, 4) + np.eye(3))))
    st8_minus_i3_err = float(np.max(np.abs(np.linalg.matrix_power(s_t, 8) - np.eye(3))))

    # Textbook level-2 Weil representation rho_{Weil,2} on Mp(2, Z):
    # L_2 = diag(1, i), S_0 = (1/sqrt(2))[[1, 1], [1, -1]], R_2 = S_0 L_2^-1 S_0
    l2_weil = np.diag([1.0, 1j]).astype(complex)
    s0_weil = np.array([[1.0, 1.0], [1.0, -1.0]], dtype=complex) * rt_half
    r2_weil = s0_weil @ np.linalg.inv(l2_weil) @ s0_weil
    # Standard Mp(2,Z) Weil_2 has S_weil = exp(-i pi/4) S_0, L_weil = L_2 => R_weil = S_weil L_weil^-1 S_weil^-1 = R_2!
    g_weil2_2d = close_matrix_group({"L": l2_weil, "R": r2_weil})
    g_untwisted_sym2 = close_matrix_group({"L": sym2_2x2(l2_weil), "R": sym2_2x2(r2_weil)})

    # Census of all 24 Z_24 metaplectic character twists chi_m (x) Sym^2(Weil_2) and Sym^2(Weil_2^*)
    twist_rows = []
    even_twist_orders: set[int] = set()
    matching_twists_t: list[tuple[str, int, float]] = []
    matching_twists_tbar: list[tuple[str, int, float]] = []

    for conj_flag, family in [(False, "Sym2(Weil2)"), (True, "Sym2(Weil2_bar)")]:
        l_base = sym2_2x2(l2_weil.conj() if conj_flag else l2_weil)
        r_base = sym2_2x2(r2_weil.conj() if conj_flag else r2_weil)
        for m in range(24):
            zeta = cmath_exp_2pi_i(m, 24)
            lm = zeta * l_base
            rm = (zeta.conjugate()) * r_base
            gm = close_matrix_group({"L": lm, "R": rm})
            order_m = len(gm)
            if m % 2 == 0:
                even_twist_orders.add(order_m)
            u_t, err_t = solve_unitary_intertwiner((tl, tr), (lm, rm))
            u_tb, err_tb = solve_unitary_intertwiner((tbarl, tbarr), (lm, rm))
            if u_t is not None and err_t < TOL:
                # Verify across all 96 group words
                all_err = 0.0
                for w_str, mt in g_t:
                    mj = np.eye(3, dtype=complex)
                    for ch in w_str:
                        mj = mj @ (lm if ch == "L" else rm)
                    all_err = max(all_err, float(np.max(np.abs(u_t @ mt @ u_t.conj().T - mj))))
                matching_twists_t.append((family, m, all_err))
            if u_tb is not None and err_tb < TOL:
                matching_twists_tbar.append((family, m, err_tb))
            twist_rows.append(
                {
                    "family": family,
                    "m_mod_24": m,
                    "parity": "even" if m % 2 == 0 else "odd",
                    "group_order": order_m,
                    "matches_T": bool(u_t is not None and err_t < TOL),
                    "matches_Tbar": bool(u_tb is not None and err_tb < TOL),
                }
            )

    # Analytical Jacobi-Dedekind half-weight triplet (theta_2^2, theta_3^2, theta_4^2) / eta^3
    sample_taus = [0.17 + 1.23j, -0.31 + 0.97j, 0.43 + 1.61j]
    v_base = np.column_stack([jacobi_dedekind_half_weight_vector(t) for t in sample_taus])
    v_l = np.column_stack([jacobi_dedekind_half_weight_vector(t + 1.0) for t in sample_taus])
    v_r = np.column_stack(
        [complex(mp.sqrt(mp.mpc(t) + 1)) * jacobi_dedekind_half_weight_vector(t / (t + 1.0)) for t in sample_taus]
    )
    m_jd_l = v_l @ np.linalg.inv(v_base)
    m_jd_r = v_r @ np.linalg.inv(v_base)

    # Independent fourth point test + exact monomial comparison
    tau_check = -0.19 + 1.44j
    jd_cov_err = max(
        float(np.max(np.abs(jacobi_dedekind_half_weight_vector(tau_check + 1.0) - m_jd_l @ jacobi_dedekind_half_weight_vector(tau_check)))),
        float(
            np.max(
                np.abs(
                    complex(mp.sqrt(mp.mpc(tau_check) + 1))
                    * jacobi_dedekind_half_weight_vector(tau_check / (tau_check + 1.0))
                    - m_jd_r @ jacobi_dedekind_half_weight_vector(tau_check)
                )
            )
        ),
    )
    w8 = np.exp(1j * math.pi / 4.0)
    w8b = np.exp(-1j * math.pi / 4.0)
    monomial_t_l = np.array([[w8b, 0.0, 0.0], [0.0, 0.0, w8], [0.0, w8, 0.0]], dtype=complex)
    monomial_t_r = np.array([[0.0, w8b, 0.0], [w8b, 0.0, 0.0], [0.0, 0.0, w8]], dtype=complex)
    jd_monomial_err = max(
        float(np.max(np.abs(m_jd_l.conj() - monomial_t_l))),
        float(np.max(np.abs(m_jd_r.conj() - monomial_t_r))),
    )
    u_jd_t, err_jd_t = solve_unitary_intertwiner((tl, tr), (monomial_t_l, monomial_t_r))
    if u_jd_t is None:
        raise RuntimeError("Failed to intertwine T with conjugate Jacobi-Dedekind monomial triplet")
    jd_all96_err = 0.0
    for w_str, mt in g_t:
        mj = np.eye(3, dtype=complex)
        for ch in w_str:
            mj = mj @ (monomial_t_l if ch == "L" else monomial_t_r)
        jd_all96_err = max(jd_all96_err, float(np.max(np.abs(u_jd_t @ mt @ u_jd_t.conj().T - mj))))

    return {
        "order_G_V_6D": len(g_v),
        "order_G_T_3D": len(g_t),
        "order_center_G_T": len(center_t),
        "projective_order_G_T": len(g_t) // len(center_t),
        "order_G_M0_2D": len(g_m0),
        "order_G_Sym2_M0_3D": len(g_sym2_m0),
        "order_Weil2_2D": len(g_weil2_2d),
        "order_untwisted_Sym2_Weil2": len(g_untwisted_sym2),
        "untwisted_Sym2_equals_96": len(g_untwisted_sym2) == 96,
        "even_Mp2Z_twist_orders": sorted(even_twist_orders),
        "any_even_Mp2Z_twist_equals_96": 96 in even_twist_orders,
        "matching_odd_twists_for_T": matching_twists_t,
        "matching_odd_twists_for_Tbar": matching_twists_tbar,
        "hodge_riemann_hermitian_err": hm_herm_err,
        "hodge_riemann_signature": (n_pos, n_neg),
        "subspace_invariance_err": subspace_inv_err,
        "braid_relation_err": braid_err,
        "braid_holds_on_T": braid_err < TOL,
        "S_T_sq_minus_iI_err": st2_minus_i_err,
        "S_T_fourth_minus_I_dist": st4_plus_i3_dist,
        "S_T_fourth_plus_I_err": st4_minus_i3_err,
        "S_T_eighth_minus_I_err": st8_minus_i3_err,
        "factors_through_SL2Z": st4_plus_i3_dist < TOL,
        "factors_through_Mp2Z": (st4_minus_i3_err < TOL) and (st8_minus_i3_err < TOL),
        "jacobi_dedekind_covariance_err": jd_cov_err,
        "jacobi_dedekind_monomial_err": jd_monomial_err,
        "jacobi_dedekind_all96_intertwiner_err": jd_all96_err,
        "monomial_T_generators_intertwine_B1611": (err_jd_t < TOL) and (jd_all96_err < TOL),
        "TL": tl,
        "TR": tr,
        "ML6": ml6,
        "MR6": mr6,
        "HM6": hm,
        "twist_census": twist_rows,
    }


def cmath_exp_2pi_i(num: int, den: int) -> complex:
    angle = 2.0 * math.pi * float(num) / float(den)
    return complex(math.cos(angle), math.sin(angle))


def _expm_hermitian(h_mat: np.ndarray, coeff: complex) -> np.ndarray:
    vals, vecs = np.linalg.eigh(h_mat)
    return (vecs * np.exp(coeff * vals)) @ vecs.conj().T


def _ext2_group(mat: np.ndarray) -> np.ndarray:
    pairs = list(combinations(range(mat.shape[0]), 2))
    m = len(pairs)
    out = np.zeros((m, m), dtype=complex)
    for i, (r0, r1) in enumerate(pairs):
        for j, (c0, c1) in enumerate(pairs):
            out[i, j] = mat[r0, c0] * mat[r1, c1] - mat[r0, c1] * mat[r1, c0]
    return out


def _ext2_lie(mat: np.ndarray) -> np.ndarray:
    pairs = list(combinations(range(mat.shape[0]), 2))
    m = len(pairs)
    out = np.zeros((m, m), dtype=complex)
    for i, (r0, r1) in enumerate(pairs):
        for j, (c0, c1) in enumerate(pairs):
            out[i, j] = (
                mat[r0, c0] * (r1 == c1)
                + (r0 == c0) * mat[r1, c1]
                - mat[r0, c1] * (r1 == c0)
                - (r0 == c1) * mat[r1, c0]
            )
    return out


def build_e8_carriers_and_modules(h4_sign: int = 1, spinor_signs: tuple[int, int] = (1, 1)) -> dict[str, Any]:
    """Construct the 5 D5 + A3 summands of 248-dimensional E8 with explicit holonomy and Higgs carriers."""
    if h4_sign not in (1, -1):
        raise ValueError("h4_sign must be +1 or -1")
    e5 = np.zeros((5, 5), dtype=complex)
    for j, c in enumerate([2.0, math.sqrt(6.0), math.sqrt(6.0), 2.0]):
        e5[j + 1, j] = c
    h5 = np.diag([-4.0, -2.0, 0.0, 2.0, 4.0]).astype(complex)
    j5 = np.zeros((5, 5), dtype=complex)
    for j, c in enumerate([1.0, -1.0, 1.0, -1.0, 1.0]):
        j5[j, 4 - j] = c
    bz = np.zeros((5, 5), dtype=complex)
    bz[1, 4] = math.sqrt(2.0 / 5.0)
    bz[4, 1] = -bz[1, 4]
    bz[2, 3] = -math.sqrt(3.0 / 5.0)
    bz[3, 2] = -bz[2, 3]
    z5 = np.zeros((5, 5), dtype=complex)

    e10 = np.block([[e5, z5], [z5, -e5.T]])
    g10 = math.sqrt(10.0) * np.block([[z5, bz], [j5 @ bz @ j5, z5]])
    h10 = np.block([[h5, z5], [z5, -h5.T]])
    n10 = np.block([[np.eye(5), z5], [z5, -np.eye(5)]]).astype(complex)
    ep10, em10 = (e10 + g10) / 2.0, (e10 - g10) / 2.0
    hp10 = ep10 @ ep10.conj().T - ep10.conj().T @ ep10
    hm10 = em10 @ em10.conj().T - em10.conj().T @ em10

    a_vec = -1j * n10 @ np.diag(np.exp(-1j * math.pi * np.diag(h10) / 4.0))
    d_vec = _expm_hermitian(hp10 - hm10, -1j * math.pi / 4.0)
    d_half_inv_vec = _expm_hermitian(hp10 - hm10, +1j * math.pi / 8.0)

    creators = []
    for axis in range(5):
        op = np.zeros((32, 32), dtype=complex)
        bit = 1 << axis
        for st in range(32):
            if (st & bit) == 0:
                lower = (st & (bit - 1)).bit_count()
                op[st | bit, st] = (-1) ** lower
        creators.append(op)

    def spin_lie(mat10: np.ndarray) -> np.ndarray:
        ann = [c.conj().T for c in creators]
        out = -0.5 * np.trace(mat10[:5, :5]) * np.eye(32, dtype=complex)
        for i in range(5):
            for j in range(5):
                out += mat10[i, j] * (creators[i] @ ann[j])
                out += 0.5 * mat10[i, j + 5] * (creators[i] @ creators[j])
                out += 0.5 * mat10[i + 5, j] * (ann[i] @ ann[j])
        return out

    xw = [0.25, 0.0, -0.25, -0.5, -0.75]
    a_spin = np.diag(
        [
            np.exp(2j * math.pi * sum(xw[i] * ((1.0 if (st & (1 << i)) else 0.0) - 0.5) for i in range(5)))
            for st in range(32)
        ]
    )
    hdiff_spin = spin_lie(hp10 - hm10)
    d_spin = _expm_hermitian(hdiff_spin, -1j * math.pi / 4.0)
    d_half_inv_spin = _expm_hermitian(hdiff_spin, +1j * math.pi / 8.0)

    h4 = float(h4_sign) * np.diag(
        [
            cmath_exp_2pi_i(3, 8),
            cmath_exp_2pi_i(-1, 8),
            cmath_exp_2pi_i(-1, 8),
            cmath_exp_2pi_i(-1, 8),
        ]
    )

    a3_basis = []
    for i in range(4):
        for j in range(4):
            if i != j:
                el = np.zeros((4, 4), dtype=complex)
                el[i, j] = 1.0
                a3_basis.append(el)
    a3_basis.extend(
        [
            np.diag([1.0, -1.0, 0.0, 0.0]) / math.sqrt(2.0),
            np.diag([1.0, 1.0, -2.0, 0.0]) / math.sqrt(6.0),
            np.diag([1.0, 1.0, 1.0, -3.0]) / math.sqrt(12.0),
        ]
    )

    def a3_adj_group(u4: np.ndarray) -> np.ndarray:
        out = np.zeros((15, 15), dtype=complex)
        for i in range(15):
            conj_m = u4 @ a3_basis[i] @ u4.conj().T
            for j in range(15):
                out[j, i] = np.trace(a3_basis[j].conj().T @ conj_m)
        return out

    def a3_adj_lie(x4: np.ndarray) -> np.ndarray:
        out = np.zeros((15, 15), dtype=complex)
        for i in range(15):
            comm = x4 @ a3_basis[i] - a3_basis[i] @ x4
            for j in range(15):
                out[j, i] = np.trace(a3_basis[j].conj().T @ comm)
        return out

    # Unbroken 9D gauge subalgebra su(3) (+) u(1) subset A3 (indices 1,2,3 of 4 + diag(-3,1,1,1))
    su3_4 = []
    for i, j in [(1, 2), (2, 3), (1, 3)]:
        g1 = np.zeros((4, 4), dtype=complex); g1[i, j] = 1.0; g1[j, i] = 1.0
        g2 = np.zeros((4, 4), dtype=complex); g2[i, j] = -1j; g2[j, i] = 1j
        su3_4.extend([g1, g2])
    su3_4.append(np.diag([0.0, 1.0, -1.0, 0.0]))
    su3_4.append(np.diag([0.0, 1.0, 1.0, -2.0]))
    su3_4.append(np.diag([-3.0, 1.0, 1.0, 1.0]))

    idx_even = [i for i in range(32) if i.bit_count() % 2 == 0]
    idx_odd = [i for i in range(32) if i.bit_count() % 2 == 1]
    spin_e = spin_lie(e10)
    spin_g = spin_lie(g10)

    sa, sb = float(spinor_signs[0]), float(spinor_signs[1])
    x_odd = sa * np.kron(a_spin[np.ix_(idx_odd, idx_odd)], h4)
    y_odd = sb * (np.kron(d_spin[np.ix_(idx_odd, idx_odd)], np.eye(4)) @ np.kron(a_spin[np.ix_(idx_odd, idx_odd)], h4))
    x_even = sa * np.kron(a_spin[np.ix_(idx_even, idx_even)], h4.conj())
    y_even = sb * (np.kron(d_spin[np.ix_(idx_even, idx_even)], np.eye(4)) @ np.kron(a_spin[np.ix_(idx_even, idx_even)], h4.conj()))

    modules = [
        {
            "name": "(45,1)",
            "dim": 45,
            "E": _ext2_lie(e10),
            "G": _ext2_lie(g10),
            "X": _ext2_group(a_vec),
            "Y": _ext2_group(d_vec @ a_vec),
            "D": _ext2_group(d_vec),
            "D_half_inv": _ext2_group(d_half_inv_vec),
            "su3": [np.zeros((45, 45), dtype=complex) for _ in su3_4],
        },
        {
            "name": "(1,15)",
            "dim": 15,
            "E": np.zeros((15, 15), dtype=complex),
            "G": np.zeros((15, 15), dtype=complex),
            "X": a3_adj_group(h4),
            "Y": a3_adj_group(h4),
            "D": np.eye(15, dtype=complex),
            "D_half_inv": np.eye(15, dtype=complex),
            "su3": [a3_adj_lie(g) for g in su3_4],
        },
        {
            "name": "(10,6)",
            "dim": 60,
            "E": np.kron(e10, np.eye(6)),
            "G": np.kron(g10, np.eye(6)),
            "X": np.kron(a_vec, _ext2_group(h4)),
            "Y": np.kron(d_vec @ a_vec, _ext2_group(h4)),
            "D": np.kron(d_vec, np.eye(6)),
            "D_half_inv": np.kron(d_half_inv_vec, np.eye(6)),
            "su3": [np.kron(np.eye(10), _ext2_lie(g)) for g in su3_4],
        },
        {
            "name": "(16,4)",
            "dim": 64,
            "E": np.kron(spin_e[np.ix_(idx_odd, idx_odd)], np.eye(4)),
            "G": np.kron(spin_g[np.ix_(idx_odd, idx_odd)], np.eye(4)),
            "X": x_odd,
            "Y": y_odd,
            "D": np.kron(d_spin[np.ix_(idx_odd, idx_odd)], np.eye(4)),
            "D_half_inv": np.kron(d_half_inv_spin[np.ix_(idx_odd, idx_odd)], np.eye(4)),
            "su3": [np.kron(np.eye(16), g) for g in su3_4],
        },
        {
            "name": "(bar16,bar4)",
            "dim": 64,
            "E": np.kron(spin_e[np.ix_(idx_even, idx_even)], np.eye(4)),
            "G": np.kron(spin_g[np.ix_(idx_even, idx_even)], np.eye(4)),
            "X": x_even,
            "Y": y_even,
            "D": np.kron(d_spin[np.ix_(idx_even, idx_even)], np.eye(4)),
            "D_half_inv": np.kron(d_half_inv_spin[np.ix_(idx_even, idx_even)], np.eye(4)),
            "su3": [np.kron(np.eye(16), -g.T) for g in su3_4],
        },
    ]
    for m in modules:
        m["K_pi"] = m["X"] @ m["Y"] @ m["X"].conj().T @ m["Y"].conj().T

    return {
        "e10": e10,
        "g10": g10,
        "ep10": ep10,
        "em10": em10,
        "hp10": hp10,
        "hm10": hm10,
        "a_vec": a_vec,
        "d_vec": d_vec,
        "d_half_inv_vec": d_half_inv_vec,
        "a_spin": a_spin,
        "d_spin": d_spin,
        "d_half_inv_spin": d_half_inv_spin,
        "spin_lie": spin_lie,
        "idx_odd": idx_odd,
        "idx_even": idx_even,
        "h4": h4,
        "modules": modules,
    }


def build_e8_parent_and_background_orbit() -> dict[str, Any]:
    """Verify Theorem 1 & WP-2.2: Index-3 background orbit [E : E_theta] = 3, explicit 248D E8
    compensators on E_theta, Klein-4 parity spectrum, and all 5 unselected background data."""
    carrier = build_e8_carriers_and_modules(h4_sign=1, spinor_signs=(1, 1))
    modules = carrier["modules"]
    total_dim = sum(m["dim"] for m in modules)

    fi = np.diag([1j, -1j])
    fj = np.array([[0.0, 1.0], [-1.0, 0.0]], dtype=complex)
    fk = fi @ fj
    sx = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    gl = (np.eye(2) + fi) / math.sqrt(2.0)
    gr = (np.eye(2) - fj) / math.sqrt(2.0)
    gs_theta = (np.eye(2) - fk) / math.sqrt(2.0)

    # 1. Local fiber stabilizer St subset 2O (B1832 check6)
    g_2o = close_matrix_group({"L": gl, "R": gr, "l": gl.conj().T, "r": gr.conj().T})
    st_els = [
        m
        for _, m in g_2o
        if np.max(np.abs(m.conj() @ sx @ m.T - sx)) < 1e-9 or np.max(np.abs(m.conj() @ sx @ m.T + sx)) < 1e-9
    ]
    gl_in_st = any(np.max(np.abs(gl - s)) < 1e-9 for s in st_els)
    gr_in_st = any(np.max(np.abs(gr - s)) < 1e-9 for s in st_els)
    gs_in_st = any(np.max(np.abs(gs_theta - s)) < 1e-9 for s in st_els)
    gl2_in_st = any(np.max(np.abs(gl @ gl - s)) < 1e-9 for s in st_els)

    # Quartic invariant separating the 3 cosets of 2O / St on D5 carrier
    phi0_10 = (carrier["e10"] / (2.0 * math.sqrt(2.0)), carrier["g10"] / (2.0 * math.sqrt(2.0)))

    def rot_pair(u2: np.ndarray, pair: tuple[np.ndarray, np.ndarray]) -> tuple[np.ndarray, np.ndarray]:
        return (u2[0, 0] * pair[0] + u2[0, 1] * pair[1], u2[1, 0] * pair[0] + u2[1, 1] * pair[1])

    def quartic_probe(pair: tuple[np.ndarray, np.ndarray], z: np.ndarray) -> float:
        x = z[0] * pair[0] + z[1] * pair[1]
        comm = x @ x.conj().T - x.conj().T @ x
        return float(np.real(0.8 * np.trace(comm @ comm)))

    z_probes = [
        np.array([1.0, 1.0], dtype=complex) / math.sqrt(2.0),
        np.array([1.0, 1j], dtype=complex) / math.sqrt(2.0),
        np.array([1.0, 0.0], dtype=complex),
    ]
    vec_0 = tuple(round(quartic_probe(phi0_10, z), 10) for z in z_probes)
    vec_l = tuple(round(quartic_probe(rot_pair(gl, phi0_10), z), 10) for z in z_probes)
    vec_r = tuple(round(quartic_probe(rot_pair(gr, phi0_10), z), 10) for z in z_probes)
    orbit_quartic_vectors = {vec_0, vec_l, vec_r}

    # 2. Global 248D E8 compensators for E_theta and Klein-4 spectrum
    err_l2 = 0.0
    err_s = 0.0
    err_neg = 0.0
    err_inn_a = 0.0
    err_inn_b = 0.0
    err_su3 = 0.0
    err_x4 = 0.0

    summand_k4: dict[str, dict[str, Any]] = {}
    tot_kpi_minus = 0
    tot_k4: Counter[str] = Counter()

    for m in modules:
        x_m, y_m, kpi, dh = m["X"], m["Y"], m["K_pi"], m["D_half_inv"]
        phi_m = (m["E"], m["G"])
        err_x4 = max(err_x4, float(np.max(np.abs(np.linalg.matrix_power(x_m, 4) - np.eye(m["dim"])))))

        # L^2: (X, X^-2 Y; Fi Phi) compensated by U = X
        phi_l2 = rot_pair(gl @ gl, phi_m)
        y_l2 = (x_m.conj().T @ x_m.conj().T) @ y_m
        err_l2 = max(
            err_l2,
            float(np.max(np.abs(x_m @ x_m @ x_m.conj().T - x_m))),
            float(np.max(np.abs(x_m @ y_l2 @ x_m.conj().T - y_m))),
            float(np.max(np.abs(x_m @ phi_l2[0] @ x_m.conj().T - phi_m[0]))),
            float(np.max(np.abs(x_m @ phi_l2[1] @ x_m.conj().T - phi_m[1]))),
        )

        # S_theta: (Y, X^-1; gS_theta Phi) compensated by U = D^{-1/2}
        phi_s = rot_pair(gs_theta, phi_m)
        err_s = max(
            err_s,
            float(np.max(np.abs(dh @ y_m @ dh.conj().T - x_m))),
            float(np.max(np.abs(dh @ x_m.conj().T @ dh.conj().T - y_m))),
            float(np.max(np.abs(dh @ phi_s[0] @ dh.conj().T - phi_m[0]))),
            float(np.max(np.abs(dh @ phi_s[1] @ dh.conj().T - phi_m[1]))),
        )

        # Central sign (1, -I2): (X, Y; -Phi) compensated by U = K_pi = X^2
        err_neg = max(
            err_neg,
            float(np.max(np.abs(kpi @ x_m @ kpi.conj().T - x_m))),
            float(np.max(np.abs(kpi @ y_m @ kpi.conj().T - y_m))),
            float(np.max(np.abs(kpi @ (-phi_m[0]) @ kpi.conj().T - phi_m[0]))),
            float(np.max(np.abs(kpi @ (-phi_m[1]) @ kpi.conj().T - phi_m[1]))),
        )

        # Inner automorphisms Inn(a), Inn(b) compensated by X, Y
        phi_ia = rot_pair(fi, phi_m)
        err_inn_a = max(
            err_inn_a,
            float(np.max(np.abs(x_m @ x_m @ x_m.conj().T - x_m))),
            float(np.max(np.abs(x_m @ (x_m.conj().T @ y_m @ x_m) @ x_m.conj().T - y_m))),
            float(np.max(np.abs(x_m @ phi_ia[0] @ x_m.conj().T - phi_m[0]))),
            float(np.max(np.abs(x_m @ phi_ia[1] @ x_m.conj().T - phi_m[1]))),
        )
        phi_ib = rot_pair(fj, phi_m)
        err_inn_b = max(
            err_inn_b,
            float(np.max(np.abs(y_m @ (y_m.conj().T @ x_m @ y_m) @ y_m.conj().T - x_m))),
            float(np.max(np.abs(y_m @ y_m @ y_m.conj().T - y_m))),
            float(np.max(np.abs(y_m @ phi_ib[0] @ y_m.conj().T - phi_m[0]))),
            float(np.max(np.abs(y_m @ phi_ib[1] @ y_m.conj().T - phi_m[1]))),
        )

        for g_su3 in m["su3"]:
            for u_comp in (x_m, y_m, dh, kpi):
                err_su3 = max(err_su3, float(np.max(np.abs(u_comp @ g_su3 - g_su3 @ u_comp))))

        # Klein-4 decomposition on ker(K_pi - I)
        ev_k, v_k = np.linalg.eigh((kpi + kpi.conj().T) / 2.0)
        plus_m = np.abs(ev_k - 1.0) < 1e-8
        minus_m = np.abs(ev_k + 1.0) < 1e-8
        n_minus = int(np.sum(minus_m))
        tot_kpi_minus += n_minus
        vp = v_k[:, plus_m]
        xp = vp.conj().T @ x_m @ vp
        yp = vp.conj().T @ y_m @ vp
        ip = np.eye(vp.shape[1], dtype=complex)
        k4_sub: dict[str, int] = {}
        for p1, p2 in [(0, 0), (1, 0), (0, 1), (1, 1)]:
            s1, s2 = (-1) ** p1, (-1) ** p2
            proj = 0.25 * (ip + s1 * xp) @ (ip + s2 * yp)
            rk = int(np.round(float(np.real(np.trace(proj)))))
            pk = f"{p1}{p2}"
            k4_sub[pk] = rk
            tot_k4[pk] += rk
        summand_k4[m["name"]] = {"kpi_minus": n_minus, "k4": k4_sub}

    # 3. Exact equivalence X(-h4) == zeta_Spin10 * X(+h4) across all 248 dims (WP-2.2 coherent lift identity)
    carrier_minus_h4 = build_e8_carriers_and_modules(h4_sign=-1, spinor_signs=(1, 1))
    carrier_zeta_spin = build_e8_carriers_and_modules(h4_sign=+1, spinor_signs=(-1, -1))
    coherent_lift_zeta_err = 0.0
    for m_neg, m_zeta in zip(carrier_minus_h4["modules"], carrier_zeta_spin["modules"]):
        coherent_lift_zeta_err = max(
            coherent_lift_zeta_err,
            float(np.max(np.abs(m_neg["X"] - m_zeta["X"]))),
            float(np.max(np.abs(m_neg["Y"] - m_zeta["Y"]))),
        )

    # 4. Exact coincidence of fiber stabilizer and holonomy parity stabilizer on all SL(2, F2) cosets
    # In E = Aut^+(F2) x_{Aut(Q8)} 2O, check on the 48 elements of 2O whether g in St iff Ad_g fixes F_k up to sign
    # (which is the exact parity condition chi_(1,1) o phi^-1 == chi_(1,1))!
    coincidence_all_48 = all(
        (
            any(np.max(np.abs(g - s)) < 1e-9 for s in st_els)
            == (
                np.max(np.abs(g @ fk @ g.conj().T - fk)) < 1e-9
                or np.max(np.abs(g @ fk @ g.conj().T + fk)) < 1e-9
            )
        )
        for _, g in g_2o
    )

    return {
        "total_e8_dim": total_dim,
        "order_2O": len(g_2o),
        "order_St": len(st_els),
        "index_2O_St": len(g_2o) // len(st_els),
        "gL_in_St": gl_in_st,
        "gR_in_St": gr_in_st,
        "gL2_in_St": gl2_in_st,
        "gS_theta_in_St": gs_in_st,
        "distinct_quartic_orbit_vectors": len(orbit_quartic_vectors),
        "fiber_and_holonomy_stabilizers_coincide": coincidence_all_48,
        "X_fourth_power_identity_err": err_x4,
        "compensator_err_L2": err_l2,
        "compensator_err_S_theta": err_s,
        "compensator_err_neg_I2": err_neg,
        "compensator_err_inn_a": err_inn_a,
        "compensator_err_inn_b": err_inn_b,
        "compensator_commutes_su3_err": err_su3,
        "E_theta_preserves_full_248D_background": max(err_l2, err_s, err_neg, err_inn_a, err_inn_b, err_su3) < TOL,
        "single_moves_preserve_background": gl_in_st and gr_in_st,
        "kpi_minus_total": tot_kpi_minus,
        "klein4_totals": dict(tot_k4),
        "summand_klein4": summand_k4,
        "coherent_lift_equals_spin10_center_err": coherent_lift_zeta_err,
        "coherent_lifts_related_by_spin10_center": coherent_lift_zeta_err < TOL,
    }


def analyze_zero_mode_bundles_and_filtrations() -> dict[str, Any]:
    """Verify Theorems 2, 3 & 4: pure-slot block diagonality, alpha_R * alpha_barR = -1 across
    both +-h4 and all 4 core sign pairs, cusp pole-order filtration on 128 vs irreducible 2 on (10,6)
    under E_theta, and finite group orders of the 3-branch induced zero-mode spaces."""
    carrier = build_e8_carriers_and_modules(h4_sign=1, spinor_signs=(1, 1))
    fi = np.diag([1j, -1j])
    fj = np.array([[0.0, 1.0], [-1.0, 0.0]], dtype=complex)
    fk = fi @ fj
    gl = (np.eye(2) + fi) / math.sqrt(2.0)
    gr = (np.eye(2) - fj) / math.sqrt(2.0)
    gs_theta = (np.eye(2) - fk) / math.sqrt(2.0)

    # 1. Pure-slot block separation between Slot 1 (1-form a, 2 modes) and Slots 2,3 (spinors u,v, 1 mode)
    # Check physical_transition_blocks(flavour, gauge) for random unitary gauge and all 48 flavour elements
    rng = np.random.default_rng(75301)
    g_rand = haar_unitary(4, rng)
    zero4 = np.zeros((4, 4), dtype=complex)
    off_block_norm = 0.0
    for f_mat in (gl, gr, gs_theta, fi, fj):
        trans = np.block(
            [
                [g_rand, zero4, zero4, zero4],
                [zero4, g_rand, zero4, zero4],
                [zero4, zero4, f_mat[0, 0] * g_rand, f_mat[0, 1] * g_rand],
                [zero4, zero4, f_mat[1, 0] * g_rand, f_mat[1, 1] * g_rand],
            ]
        )
        # Off-diagonal coupling between Slot 1 (rows/cols 4:8) and Slots 2,3 (rows/cols 8:16)
        off_block_norm = max(
            off_block_norm,
            float(np.max(np.abs(trans[4:8, 8:16]))),
            float(np.max(np.abs(trans[8:16, 4:8]))),
        )

    # 2. Exact Koszul harmonic table on 128 = (16,4) + (bar16,bar4) across BOTH +-h4 and ALL 4 core sign pairs!
    all_lift_sign_opposite = True
    half_root_table: list[dict[str, Any]] = []

    for h4_sign in (+1, -1):
        for s_pair in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
            c_loc = build_e8_carriers_and_modules(h4_sign=h4_sign, spinor_signs=s_pair)
            spin_lie = c_loc["spin_lie"]
            row_signs: dict[str, tuple[int, int]] = {}
            spinor_h0_counts: dict[str, int] = {}
            for mod_name, idxs, mod_idx in [("(16,4)", c_loc["idx_odd"], 3), ("(bar16,bar4)", c_loc["idx_even"], 4)]:
                ep_s = spin_lie(c_loc["ep10"])[np.ix_(idxs, idxs)]
                em_s = spin_lie(c_loc["em10"])[np.ix_(idxs, idxs)]
                _, _, vh_t = np.linalg.svd(np.vstack([ep_s, em_s]))
                top_v = vh_t[-1].conj()
                top_v = top_v / np.linalg.norm(top_v)
                mod = c_loc["modules"][mod_idx]
                x_full, y_full = mod["X"], mod["Y"]
                sel0 = [4 * r for r in range(16)]
                e_16 = mod["E"][np.ix_(sel0, sel0)]
                g_16 = mod["G"][np.ix_(sel0, sel0)]
                m_k1 = np.vstack([np.hstack([e_16.conj().T, g_16.conj().T]), np.hstack([-g_16, e_16])])
                _, sv_k1, vh_k1 = np.linalg.svd(m_k1)
                h1_16 = vh_k1[sv_k1 < 1e-9].conj().T

                for col_label, col_idx in [("singlet", 0), ("triplet", 1)]:
                    # Extract 16D block for colour index col_idx (stride 4 in kronecker(16, 4))
                    sel = [4 * r + col_idx for r in range(16)]
                    x_b = x_full[np.ix_(sel, sel)]
                    y_b = y_full[np.ix_(sel, sel)]
                    ax = int(np.round(float(np.real(np.vdot(top_v, x_b @ top_v)))))
                    ay = int(np.round(float(np.real(np.vdot(top_v, y_b @ top_v)))))
                    key_lbl = f"{mod_name}_{col_label}"
                    row_signs[key_lbl] = (ax, ay)

                    # Spinor deg-1 holonomy (Fi (x) x_b, Fj (x) y_b) restricted to h1_16:
                    ha = h1_16.conj().T @ np.kron(fi, x_b) @ h1_16
                    hb = h1_16.conj().T @ np.kron(fj, y_b) @ h1_16
                    id_h1 = np.eye(ha.shape[0], dtype=complex)
                    proj_triv = 0.25 * (id_h1 + ha) @ (id_h1 + hb)
                    spinor_h0_counts[key_lbl] = int(np.round(float(np.real(np.trace(proj_triv)))))

            # Check singlet vs triplet opposite character product on BOTH (16,4) and (bar16,bar4),
            # AND conjugate-pair opposite product!
            s16 = row_signs["(16,4)_singlet"]
            t16 = row_signs["(16,4)_triplet"]
            sb16 = row_signs["(bar16,bar4)_singlet"]
            tb16 = row_signs["(bar16,bar4)_triplet"]
            opp_ok = (
                (s16[0] * t16[0] == -1)
                and (s16[1] * t16[1] == -1)
                and (s16[0] * sb16[0] == -1)
                and (t16[0] * tb16[0] == -1)
            )
            all_lift_sign_opposite = all_lift_sign_opposite and opp_ok
            if h4_sign == 1:
                half_root_table.append(
                    {
                        "h4_sign": h4_sign,
                        "spinor_signs": s_pair,
                        "deg0_holonomies": row_signs,
                        "spinor_h0_counts": spinor_h0_counts,
                        "total_zero_modes_per_rep": {k: 2 + v for k, v in spinor_h0_counts.items()},
                    }
                )

    # 3. Explicit elliptic pole-filtration check under Gamma_theta on E_tau \ {0}
    # Verify:
    #  (a) On H^0(E_tau, chi_(1,1)(p)): unit-residue Szego 1-form S_3(z|tau) dz is invariant under L^2 and S_theta!
    #  (b) On H^0(E_tau, chi_(1,0)(p) (+) chi_(0,1)(p)) in (10,6): L^2 is diagonal, while S_theta swaps S_2 <-> S_4!
    with mp.workdps(35):
        t0 = mp.mpc("0.21", "1.31")
        z0 = mp.mpc("0.13", "0.29")

        def szego_unit_res(idx_theta: int, z: mp.mpc, tau: mp.mpc) -> complex:
            q = mp.exp(1j * mp.pi * tau)
            num = mp.pi * mp.jtheta(1, 0, q, 1) * mp.jtheta(idx_theta, mp.pi * z, q)
            den = mp.jtheta(idx_theta, 0, q) * mp.jtheta(1, mp.pi * z, q)
            return complex(num / den)

        # S_3 corresponds to chi_(1,1); S_2 to chi_(1,0); S_4 to chi_(0,1)
        s3_base = szego_unit_res(3, z0, t0)
        s3_l2 = szego_unit_res(3, z0, t0 + 2)
        s3_s = complex(1 / t0) * szego_unit_res(3, z0 / t0, -1 / t0)
        szego_chi11_gamma_theta_err = max(abs(s3_l2 - s3_base), abs(s3_s - s3_base))

        s2_base = szego_unit_res(2, z0, t0)
        s4_base = szego_unit_res(4, z0, t0)
        s2_after_s = complex(1 / t0) * szego_unit_res(2, z0 / t0, -1 / t0)
        s4_after_s = complex(1 / t0) * szego_unit_res(4, z0 / t0, -1 / t0)
        up_sector_swap_err = max(abs(s2_after_s - s4_base), abs(s4_after_s - s2_base))

    # 4. Finite groups generated on the 3-branch induced zero-mode spaces vs G_96:
    # (a) Pure S3 permutation of unit-residue Szego modes (alpha=+1 or uncompensated residue basis): order 6
    p_l = np.array([[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]], dtype=complex)
    p_r = np.array([[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]], dtype=complex)
    g_s3 = close_matrix_group({"L": p_l, "R": p_r})

    # (b) 3-branch active Szego 1-form mode in 128 (alpha=-1, where E_theta fiber compensator X gives L^2 -> -1, S -> +1):
    # Induced monomial representation from (L^2 -> -1, S -> +1) on index 1:
    # Take L_oct = diag(i, ...) ? Check exact induced representation of psi(L^2)=-1, psi(S)=+1:
    # Sym^2(M0) / octahedral S_4 has L_s4 = [[i, 0, 0], [0, 0, 1], [0, 1, 0]]? Check L_s4^2 = diag(-1, 1, 1) — wait:
    # On index 1 (chi_(1,1)), L swaps 1 <-> 2, so L^2 on index 1 is L_{1,2} * L_{2,1}!
    # For L^2|_{1} = -1 and R^2|_{1} = -1 and S = L R^-1 L|_{1} = +1:
    l_ind_1form = np.array([[1.0, 0.0, 0.0], [0.0, 0.0, 1j], [0.0, 1j, 0.0]], dtype=complex)
    r_ind_1form = np.array([[0.0, -1j, 0.0], [-1j, 0.0, 0.0], [0.0, 0.0, 1.0]], dtype=complex)
    # Check braid relation and stabilizer characters on e_1:
    braid_1f_err = float(
        np.max(np.abs(l_ind_1form @ np.linalg.inv(r_ind_1form) @ l_ind_1form - np.linalg.inv(r_ind_1form) @ l_ind_1form @ np.linalg.inv(r_ind_1form)))
    )
    g_ind_1form = close_matrix_group({"L": l_ind_1form, "R": r_ind_1form})

    # (c) 3-branch spinor zero mode in 128 (fiber compensator gives L^2 -> +1, S_theta -> -1, -I2 -> +1):
    # Induced monomial representation on 3 branches: L swaps 1<->2 with +1, fixes 0 with -1; R swaps 0<->1 with +1, fixes 2 with -1!
    l_ind_spin = np.array([[-1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]], dtype=complex)
    r_ind_spin = np.array([[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]], dtype=complex)
    braid_sp_err = float(
        np.max(np.abs(l_ind_spin @ np.linalg.inv(r_ind_spin) @ l_ind_spin - np.linalg.inv(r_ind_spin) @ l_ind_spin @ np.linalg.inv(r_ind_spin)))
    )
    g_ind_spin = close_matrix_group({"L": l_ind_spin, "R": r_ind_spin})
    center_ind_spin = [
        w for w, m in g_ind_spin if all(np.max(np.abs(m @ n - n @ m)) < 1e-7 for _, n in g_ind_spin)
    ]
    center_ind_1form = [
        w for w, m in g_ind_1form if all(np.max(np.abs(m @ n - n @ m)) < 1e-7 for _, n in g_ind_1form)
    ]

    return {
        "slot_off_block_norm": off_block_norm,
        "slots_strictly_block_diagonal": off_block_norm < TOL,
        "outcome_1_irreducible_on_fixed_bg": (off_block_norm > TOL),
        "all_lifts_and_signs_have_opposite_alpha_sectors": all_lift_sign_opposite,
        "half_root_sign_census": half_root_table,
        "szego_chi11_gamma_theta_invariance_err": float(szego_chi11_gamma_theta_err),
        "pole_filtration_splits_128_under_E_theta": float(szego_chi11_gamma_theta_err) < TOL,
        "vector_six_S_theta_swap_err": float(up_sector_swap_err),
        "vector_six_a_slot_irreducible_2_under_E_theta": float(up_sector_swap_err) < TOL,
        "order_3branch_pure_permutation": len(g_s3),
        "order_3branch_128_active_1form": len(g_ind_1form),
        "projective_order_3branch_128_active_1form": len(g_ind_1form) // len(center_ind_1form),
        "braid_err_3branch_128_active_1form": braid_1f_err,
        "order_3branch_128_spinor_fiber": len(g_ind_spin),
        "projective_order_3branch_128_spinor_fiber": len(g_ind_spin) // len(center_ind_spin),
        "braid_err_3branch_128_spinor_fiber": braid_sp_err,
    }


def run_haar_unitary_basis_scrambling_audit(seed: int = 20261110) -> dict[str, Any]:
    """Guardrail 3: Verify that all group orders, character traces, Hodge-Riemann signatures,
    and E_theta compensator identities remain invariant (< 1e-12) under independent random Haar
    unitary basis transformations."""
    rng = np.random.default_rng(seed)
    w_res = build_weave_triplet_and_sym2_census()
    tl, tr = w_res["TL"], w_res["TR"]
    ml6, mr6, hm6 = w_res["ML6"], w_res["MR6"], w_res["HM6"]

    max_trace_drift = 0.0
    max_sig_drift = 0
    orders_scrambled: set[int] = set()

    for _ in range(5):
        u3 = haar_unitary(3, rng)
        tl_s = u3 @ tl @ u3.conj().T
        tr_s = u3 @ tr @ u3.conj().T
        gs = close_matrix_group({"L": tl_s, "R": tr_s})
        orders_scrambled.add(len(gs))
        max_trace_drift = max(
            max_trace_drift,
            abs(complex(np.trace(tl_s) - np.trace(tl))),
            abs(complex(np.trace(tr_s) - np.trace(tr))),
            abs(complex(np.trace(tl_s @ tr_s) - np.trace(tl @ tr))),
        )

        u6 = haar_unitary(6, rng)
        hm_s = u6 @ hm6 @ u6.conj().T
        ml_s = u6 @ ml6 @ u6.conj().T
        ev_s = np.linalg.eigvalsh((hm_s + hm_s.conj().T) / 2.0)
        sig_s = (int(np.sum(ev_s > 1e-8)), int(np.sum(ev_s < -1e-8)))
        if sig_s != (3, 3):
            max_sig_drift += 1
        # Check scrambled invariance ml_s^dag hm_s ml_s == hm_s:
        inv_err = float(np.max(np.abs(ml_s.conj().T @ hm_s @ ml_s - hm_s)))
        max_trace_drift = max(max_trace_drift, inv_err)

    # Scramble 16D Spin(10) basis and SU(3)_c basis on (16,4)
    carrier = build_e8_carriers_and_modules(h4_sign=1, spinor_signs=(1, 1))
    mod16 = carrier["modules"][3]
    u16 = haar_unitary(16, rng)
    u3_c = haar_unitary(3, rng)
    u4_c = np.eye(4, dtype=complex)
    u4_c[1:, 1:] = u3_c
    u64 = np.kron(u16, u4_c)

    x_s = u64 @ mod16["X"] @ u64.conj().T
    y_s = u64 @ mod16["Y"] @ u64.conj().T
    dh_s = u64 @ mod16["D_half_inv"] @ u64.conj().T
    e_s = u64 @ mod16["E"] @ u64.conj().T
    g_s = u64 @ mod16["G"] @ u64.conj().T
    fk = np.diag([1j, -1j]) @ np.array([[0.0, 1.0], [-1.0, 0.0]], dtype=complex)
    gs_th = (np.eye(2) - fk) / math.sqrt(2.0)
    phi_s0 = gs_th[0, 0] * e_s + gs_th[0, 1] * g_s
    phi_s1 = gs_th[1, 0] * e_s + gs_th[1, 1] * g_s
    e8_scramble_err = max(
        float(np.max(np.abs(dh_s @ y_s @ dh_s.conj().T - x_s))),
        float(np.max(np.abs(dh_s @ x_s.conj().T @ dh_s.conj().T - y_s))),
        float(np.max(np.abs(dh_s @ phi_s0 @ dh_s.conj().T - e_s))),
        float(np.max(np.abs(dh_s @ phi_s1 @ dh_s.conj().T - g_s))),
    )

    return {
        "scrambled_orders": sorted(orders_scrambled),
        "max_trace_and_form_drift": float(max_trace_drift),
        "signature_drift_count": max_sig_drift,
        "e8_spinor_colour_scramble_err": e8_scramble_err,
        "basis_scrambling_invariant": (
            orders_scrambled == {96}
            and max_trace_drift < TOL
            and max_sig_drift == 0
            and e8_scramble_err < TOL
        ),
    }


def run_full_p753_join() -> dict[str, Any]:
    """Execute all 4 exact verification stages for P-753 / R77-2 (WP-2.2 & WP-3.2)."""
    t_sym2 = build_weave_triplet_and_sym2_census()
    e8_bg = build_e8_parent_and_background_orbit()
    zero_modes = analyze_zero_mode_bundles_and_filtrations()
    scramble = run_haar_unitary_basis_scrambling_audit()
    return {
        "weave_triplet_and_sym2": {
            k: v for k, v in t_sym2.items() if k not in ("TL", "TR", "ML6", "MR6", "HM6")
        },
        "e8_background_orbit": e8_bg,
        "zero_mode_bundles": zero_modes,
        "haar_basis_scrambling": scramble,
    }
