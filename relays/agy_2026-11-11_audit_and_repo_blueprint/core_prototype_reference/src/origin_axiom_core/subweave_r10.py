"""Whole-Subweave Operators on +-Gamma_1(N) and Holomorphic Ray-Singer Analytic Torsion (B1879).

Provides strictly data-free (`0 of 19`) operators on the allowed level-N marked-line
subweave `Omega_1(N) = PSL_2(Z) / +-Gamma_1(N)`:
  1. Infinite-`PSL_2(Z)` Schreier transversal and BFS word factorization of `+-Gamma_1(5)`
     from the four positive charge-invisible words `w_1..w_4` (`B1872`).
  2. `R10-A`: Coset-coupled Gauss-Mayer-Selberg transfer operator `M_{1, Omega_1(N)}`
     on the zero-sum subweave space `C_0[Omega_1(N)]`, uniquely selecting `N = 5` across
     `N = 2..11` by maximizing `rho_0` and minimizing `det(I - M_1|_{C_0})`.
  3. `R10-B/C1/C2`: Holomorphic fractional-nome Siegel modular units (`exp(2*pi*i*a_1*tau)`,
     branch-cut-free across all `tau in H`), Kronecker-Siegel factorization, and the
     Ray-Singer analytic torsion potentials `V_{X_1(N)}^{(kappa)}(tau)` for `kappa = 1`
     (`O (+) L_{1/N}`) and `kappa = 2` twin-symmetric (`O (+) L_{1/N} (+) L_{-1/N}`),
     whose cusp-coercivity slope satisfies `1/3 + 4*B_2(a_1) == (2*a_1 - 1)^2`.
"""

from __future__ import annotations

from collections import deque
import math
from typing import Any, Dict, List, Tuple

import mpmath as mp
import numpy as np
from scipy.special import zeta as hurwitz_zeta

from .guardrail_dsl import producer


def build_marked_lines(n_level: int) -> List[Tuple[int, int]]:
    """Canonical representatives (a, b) of +-v for primitive order-N vectors in (Z/NZ)^2."""
    reps = set()
    for a in range(n_level):
        for b in range(n_level):
            if math.gcd(math.gcd(a, b), n_level) == 1:
                reps.add(min((a, b), ((-a) % n_level, (-b) % n_level)))
    return sorted(reps)


def act_marked_line(mat: Tuple[int, int, int, int], line: Tuple[int, int], n_level: int) -> Tuple[int, int]:
    a, b, c, d = mat
    x, y = line
    nx = (a * x + b * y) % n_level
    ny = (c * x + d * y) % n_level
    return min((nx, ny), ((-nx) % n_level, (-ny) % n_level))


def _psl_key(m: np.ndarray) -> Tuple[int, int, int, int]:
    t1 = (int(m[0, 0]), int(m[0, 1]), int(m[1, 0]), int(m[1, 1]))
    t2 = (-t1[0], -t1[1], -t1[2], -t1[3])
    return min(t1, t2)


def _mat_inv_sl2(m: np.ndarray) -> np.ndarray:
    return np.array([[m[1, 1], -m[0, 1]], [-m[1, 0], m[0, 0]]], dtype=np.int64)


@producer
def schreier_closure_pm_gamma1_5() -> Dict[str, Any]:
    """Constructively factors all non-trivial Schreier generators of +-Gamma_1(5) in infinite PSL_2(Z)."""
    Ls = np.array([[1, 0], [1, 1]], dtype=np.int64)
    Rs = np.array([[1, 1], [0, 1]], dtype=np.int64)
    LR = Ls @ Rs
    w1 = np.linalg.matrix_power(Ls, 6) @ Rs @ LR
    w2 = np.linalg.matrix_power(Ls, 6) @ Rs @ LR @ LR
    w3 = Ls @ np.linalg.matrix_power(Rs, 6) @ LR
    w4 = Ls @ np.linalg.matrix_power(Rs, 6) @ LR @ LR

    S_mat = np.array([[0, -1], [1, 0]], dtype=np.int64)
    T_mat = Rs.copy()
    T_inv = _mat_inv_sl2(T_mat)
    base_mark = (1, 3)

    transversal: Dict[Tuple[int, int], np.ndarray] = {base_mark: np.eye(2, dtype=np.int64)}
    q_cos = deque([base_mark])
    while q_cos:
        mk = q_cos.popleft()
        rep = transversal[mk]
        for gen in (S_mat, T_mat, T_inv):
            prod = gen @ rep
            tup = (int(prod[0, 0]), int(prod[0, 1]), int(prod[1, 0]), int(prod[1, 1]))
            nxt_mk = act_marked_line(tup, base_mark, 5)
            if nxt_mk not in transversal:
                transversal[nxt_mk] = prod
                q_cos.append(nxt_mk)

    schreier_gens: Dict[Tuple[int, int, int, int], np.ndarray] = {}
    id_key = _psl_key(np.eye(2, dtype=np.int64))
    for rep in transversal.values():
        for gen in (S_mat, T_mat):
            prod = gen @ rep
            tup = (int(prod[0, 0]), int(prod[0, 1]), int(prod[1, 0]), int(prod[1, 1]))
            nxt_mk = act_marked_line(tup, base_mark, 5)
            sch = _mat_inv_sl2(transversal[nxt_mk]) @ prod
            k_sch = _psl_key(sch)
            if k_sch != id_key:
                schreier_gens[k_sch] = sch

    g1 = _mat_inv_sl2(w1) @ w2
    g2 = w2 @ _mat_inv_sl2(w1) @ _mat_inv_sl2(w1)
    g3 = (w3 @ _mat_inv_sl2(w1)) @ g2
    sub_gens = [
        w1, _mat_inv_sl2(w1), w2, _mat_inv_sl2(w2),
        w3, _mat_inv_sl2(w3), w4, _mat_inv_sl2(w4),
        g1, _mat_inv_sl2(g1), g2, _mat_inv_sl2(g2), g3, _mat_inv_sl2(g3),
    ]

    remaining = set(schreier_gens.keys())
    visited = {id_key}
    bfs_q = deque([(np.eye(2, dtype=np.int64), 0)])
    max_depth = 0
    while bfs_q and remaining:
        cur_m, d = bfs_q.popleft()
        if d >= 7:
            continue
        for sg in sub_gens:
            nxt_m = cur_m @ sg
            if int(np.max(np.abs(nxt_m))) > 50000:
                continue
            nk = _psl_key(nxt_m)
            if nk not in visited:
                visited.add(nk)
                if nk in remaining:
                    remaining.remove(nk)
                    max_depth = max(max_depth, d + 1)
                bfs_q.append((nxt_m, d + 1))

    return {
        "index_in_psl2z": len(transversal),
        "schreier_generator_count": len(schreier_gens),
        "unfactored_count": len(remaining),
        "max_word_depth": max_depth,
    }


def _chebyshev_basis_matrix(xs: np.ndarray, k_nodes: int) -> np.ndarray:
    u = 2.0 * xs - 1.0
    v_mat = np.zeros((len(xs), k_nodes), dtype=np.float64)
    v_mat[:, 0] = 1.0
    if k_nodes > 1:
        v_mat[:, 1] = u
    for k in range(2, k_nodes):
        v_mat[:, k] = 2.0 * u * v_mat[:, k - 1] - v_mat[:, k - 2]
    return v_mat


def _chebyshev_u_monomial_coeffs(k_nodes: int) -> np.ndarray:
    coeffs = np.zeros((k_nodes, k_nodes), dtype=np.float64)
    coeffs[0, 0] = 1.0
    if k_nodes > 1:
        coeffs[1, 0] = -1.0
        coeffs[1, 1] = 2.0
    for k in range(2, k_nodes):
        coeffs[k, :] = -2.0 * coeffs[k - 1, :] - coeffs[k - 2, :]
        coeffs[k, 1:] += 4.0 * coeffs[k - 1, :-1]
    return coeffs


@producer
def mayer_selberg_subweave_spectrum(n_level: int, k_nodes: int = 16, q_direct_blocks: int = 40) -> Dict[str, Any]:
    """Evaluates R10-A Mayer-Selberg transfer operator spectrum on C_0[Omega_1(N)] via Chebyshev collocation."""
    cosets = build_marked_lines(n_level)
    d_cos = len(cosets)
    cos_to_idx = {c: i for i, c in enumerate(cosets)}

    idx_k = np.arange(k_nodes, dtype=np.float64)
    xs = 0.5 * (1.0 + np.cos(np.pi * (2.0 * idx_k + 1.0) / (2.0 * k_nodes)))
    v_inv = np.linalg.inv(_chebyshev_basis_matrix(xs, k_nodes))
    c_mono = _chebyshev_u_monomial_coeffs(k_nodes)
    j_arr = np.arange(k_nodes, dtype=np.float64)

    residue_blocks: List[np.ndarray] = []
    for r in range(1, n_level + 1):
        ns = (np.arange(q_direct_blocks, dtype=np.float64) * n_level + r)[:, None]
        den = ns + xs[None, :]
        u_vals = 1.0 / den
        weights = den ** (-2.0)
        t_eval = _chebyshev_basis_matrix(u_vals.ravel(), k_nodes).reshape(q_direct_blocks, k_nodes, k_nodes)
        modal_direct = np.einsum("qi,qik->ik", weights, t_eval)

        a_shift = q_direct_blocks + (r + xs) / float(n_level)
        s_vec = (2.0 + j_arr)[None, :]
        zeta_mat = (float(n_level) ** (-s_vec)) * hurwitz_zeta(s_vec, a_shift[:, None])
        modal_tail = zeta_mat @ c_mono.T
        residue_blocks.append((modal_direct + modal_tail) @ v_inv)

    g_full = np.zeros((k_nodes * d_cos, k_nodes * d_cos), dtype=np.float64)
    for r_idx, r in enumerate(range(1, n_level + 1)):
        gn_mat = (0, 1 % n_level, 1 % n_level, r % n_level)
        b_r = residue_blocks[r_idx]
        for c_i, c_val in enumerate(cosets):
            c_j = cos_to_idx[act_marked_line(gn_mat, c_val, n_level)]
            g_full[c_i * k_nodes : (c_i + 1) * k_nodes, c_j * k_nodes : (c_j + 1) * k_nodes] += b_r

    m_op = g_full @ g_full
    ones = np.ones((d_cos, 1), dtype=np.float64) / math.sqrt(d_cos)
    q_mat, _ = np.linalg.qr(np.hstack([ones, np.eye(d_cos, d_cos - 1)]), mode="complete")
    p_triv = np.kron(ones, np.eye(k_nodes))
    p_sub = np.kron(q_mat[:, 1:], np.eye(k_nodes))

    m_triv = p_triv.T @ m_op @ p_triv
    m_sub = p_sub.T @ m_op @ p_sub
    ev_triv = np.sort(np.abs(np.linalg.eigvals(m_triv)))[::-1]
    ev_sub = np.sort(np.abs(np.linalg.eigvals(m_sub)))[::-1]
    det_sub = float(np.linalg.det(np.eye(m_sub.shape[0]) - m_sub))

    return {
        "N": n_level,
        "index_d": d_cos,
        "trivial_lambda1": float(ev_triv[0]),
        "trivial_lambda2_wirsing_sq": float(ev_triv[1]),
        "subweave_mayer_rho0": float(ev_sub[0]),
        "subweave_fredholm_det": det_sub,
    }


@producer
def ray_singer_x1_sheet_potential_mp(
    tau0: complex | mp.mpc, r1: int, r2: int, n_level: int, kappa: int = 1, n_terms: int = 50
) -> mp.mpf:
    """Evaluates holomorphic fractional-nome Ray-Singer torsion potential V_{X_1(N)}^{(kappa)} on sheet (r1, r2)."""
    t = mp.mpc(tau0)
    q2 = mp.exp(2j * mp.pi * t)
    et_prod = mp.mpc(1, 0)
    qm = q2
    for _ in range(n_terms):
        et_prod *= 1 - qm
        qm *= q2
    eta_val = mp.exp(1j * mp.pi * t / 12) * et_prod

    a1_int = r1 % n_level
    a1 = mp.mpf(a1_int) / mp.mpf(n_level)
    a2 = mp.mpf(r2 % n_level) / mp.mpf(n_level)
    b2 = a1 * a1 - a1 + mp.mpf(1) / 6
    z = mp.exp(2j * mp.pi * a2)

    s_prod = mp.mpc(1, 0)
    if a1_int == 0:
        s_prod *= 1 - z
        qm = q2
        for _ in range(1, n_terms + 1):
            s_prod *= (1 - qm * z) * (1 - qm / z)
            qm *= q2
    else:
        qm = mp.mpc(1, 0)
        qa = mp.exp(2j * mp.pi * a1 * t)
        qb = mp.exp(2j * mp.pi * (1 - a1) * t)
        for _ in range(0, n_terms + 1):
            s_prod *= (1 - qm * qa * z) * (1 - qm * qb / z)
            qm *= q2

    su_abs = abs(mp.exp(2j * mp.pi * t * (mp.mpf("0.5") * b2)) * mp.exp(1j * mp.pi * a2 * (a1 - 1)) * s_prod)
    return -mp.log(mp.im(t) * (abs(eta_val) ** 4) * (su_abs ** (2 * kappa)))
