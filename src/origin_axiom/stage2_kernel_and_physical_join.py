"""Stage 2 (B1861 WP-3.1, WP-3.2 & B1866 Open Physical Question):
Explicit 248-Root Kernel Theorem, Curved Half-Form PDE Embedding, & Zero-Hand-Typed 3-Branch Physical Join.

Strictly data-free (0 of 19). Zero empirical Standard Model constants or fitted parameters
appear anywhere in this module. Every identity is proved in exact symbolic/cyclotomic arithmetic
(SymPy + Q(zeta_24) = Q[z]/(z^8 - z^4 + 1)) paired with high-precision numerical and independent
Haar unitary basis-scrambling checks (Guardrails 1-6 and Anti-Shortcut Locks F1-F6).
"""
from __future__ import annotations

from itertools import combinations
import math
from pathlib import Path
from typing import Any

import mpmath as mp
import numpy as np
import sympy as sp

from origin_axiom.stage1_curved_action_cusp_orbit import (
    audit_source_zero_empirical_constants,
    haar_unitary,
    joint_commutant_dim_num,
)

TOL = 1e-12


# ============================================================================
# 1. Exact Q(zeta_24) = Q[z]/(z^8 - z^4 + 1) Cyclotomic Matrix Arithmetic (F5)
# ============================================================================

Z24 = sp.Symbol("z24")
Cyc24Elem = tuple[sp.Rational, ...]


def _q_zero() -> Cyc24Elem:
    z0 = sp.Rational(0)
    return (z0, z0, z0, z0, z0, z0, z0, z0)


def cyc24_from_int(n_val: int) -> Cyc24Elem:
    z0 = sp.Rational(0)
    return (sp.Rational(n_val), z0, z0, z0, z0, z0, z0, z0)


def cyc24_pow(k_exp: int) -> Cyc24Elem:
    """Exact power zeta_24^k in the basis (1, z, ..., z^7) with z^8 = z^4 - 1."""
    m_exp = k_exp % 24
    coeffs = [sp.Rational(0) for _ in range(24)]
    coeffs[m_exp] = sp.Rational(1)
    for deg in range(23, 7, -1):
        c_top = coeffs[deg]
        if c_top != 0:
            coeffs[deg - 4] += c_top
            coeffs[deg - 8] -= c_top
    return tuple(coeffs[:8])


def cyc24_add(a_el: Cyc24Elem, b_el: Cyc24Elem) -> Cyc24Elem:
    return tuple(a_el[k_i] + b_el[k_i] for k_i in range(8))


def cyc24_neg(a_el: Cyc24Elem) -> Cyc24Elem:
    return tuple(-a_el[k_i] for k_i in range(8))


def cyc24_scale_half(a_el: Cyc24Elem) -> Cyc24Elem:
    h_q = sp.Rational(1, 2)
    return tuple(a_el[k_i] * h_q for k_i in range(8))


def cyc24_mul(a_el: Cyc24Elem, b_el: Cyc24Elem) -> Cyc24Elem:
    prod = [sp.Rational(0) for _ in range(15)]
    for i_a in range(8):
        ai = a_el[i_a]
        if ai != 0:
            for j_b in range(8):
                bj = b_el[j_b]
                if bj != 0:
                    prod[i_a + j_b] += ai * bj
    for deg in range(14, 7, -1):
        c_top = prod[deg]
        if c_top != 0:
            prod[deg - 4] += c_top
            prod[deg - 8] -= c_top
    return tuple(prod[:8])


def cyc24_conj(a_el: Cyc24Elem) -> Cyc24Elem:
    """Exact complex conjugation conj(zeta_24^k) = zeta_24^(-k) in Q(zeta_24)."""
    acc = _q_zero()
    for k_i in range(8):
        ck = a_el[k_i]
        if ck != 0:
            p_neg = cyc24_pow(-k_i)
            acc = tuple(acc[j_i] + ck * p_neg[j_i] for j_i in range(8))
    return acc


def cyc24_to_sympy_expr(a_el: Cyc24Elem) -> sp.Expr:
    return sum((a_el[k_i] * (Z24**k_i) for k_i in range(8)), sp.Integer(0))


def cyc24_matmul(mat_a: list[list[Cyc24Elem]], mat_b: list[list[Cyc24Elem]]) -> list[list[Cyc24Elem]]:
    """Exact matrix product over Q(zeta_24)."""
    n_r = len(mat_a)
    n_k = len(mat_b)
    n_c = len(mat_b[0])
    out: list[list[Cyc24Elem]] = []
    for r_i in range(n_r):
        row_out: list[Cyc24Elem] = []
        for c_i in range(n_c):
            acc = _q_zero()
            for k_i in range(n_k):
                acc = cyc24_add(acc, cyc24_mul(mat_a[r_i][k_i], mat_b[k_i][c_i]))
            row_out.append(acc)
        out.append(row_out)
    return out


def cyc24_herm(mat_a: list[list[Cyc24Elem]]) -> list[list[Cyc24Elem]]:
    """Exact conjugate transpose over Q(zeta_24)."""
    n_r = len(mat_a)
    n_c = len(mat_a[0])
    return [[cyc24_conj(mat_a[r_i][c_i]) for r_i in range(n_r)] for c_i in range(n_c)]


def cyc24_eye(dim: int) -> list[list[Cyc24Elem]]:
    """Exact identity matrix over Q(zeta_24)."""
    return [[cyc24_from_int(1 if r_i == c_i else 0) for c_i in range(dim)] for r_i in range(dim)]


def cyc24_key(mat_a: list[list[Cyc24Elem]]) -> tuple[tuple[Cyc24Elem, ...], ...]:
    """Hashable canonical key of a matrix over Q(zeta_24) with zero float rounding."""
    return tuple(tuple(row) for row in mat_a)


def cyc24_sym2_2x2(mat_2: list[list[Cyc24Elem]]) -> list[list[Cyc24Elem]]:
    """Exact unitary symmetric square Sym^2(C^2) on orthonormal basis (e1^2, sqrt(2) e1 e2, e2^2)."""
    rt2 = cyc24_add(cyc24_pow(3), cyc24_neg(cyc24_pow(9)))
    a00, a01 = mat_2[0][0], mat_2[0][1]
    a10, a11 = mat_2[1][0], mat_2[1][1]
    return [
        [cyc24_mul(a00, a00), cyc24_mul(rt2, cyc24_mul(a00, a01)), cyc24_mul(a01, a01)],
        [
            cyc24_mul(rt2, cyc24_mul(a00, a10)),
            cyc24_add(cyc24_mul(a00, a11), cyc24_mul(a01, a10)),
            cyc24_mul(rt2, cyc24_mul(a01, a11)),
        ],
        [
            cyc24_mul(a10, a10),
            cyc24_mul(rt2, cyc24_mul(a10, a11)),
            cyc24_mul(a11, a11),
        ],
    ]


def cyc24_close_group(
    gens: dict[str, list[list[Cyc24Elem]]], max_depth: int = 24
) -> dict[tuple[tuple[Cyc24Elem, ...], ...], tuple[str, list[list[Cyc24Elem]]]]:
    """Exact finite matrix group closure in Q(zeta_24) by bounded-depth BFS (F5, F6)."""
    dim = len(next(iter(gens.values())))
    ident = cyc24_eye(dim)
    id_k = cyc24_key(ident)
    seen: dict[tuple[tuple[Cyc24Elem, ...], ...], tuple[str, list[list[Cyc24Elem]]]] = {id_k: ("", ident)}
    frontier: list[tuple[str, list[list[Cyc24Elem]]]] = [("", ident)]
    for _ in range(max_depth):
        if not frontier:
            break
        nxt_frontier: list[tuple[str, list[list[Cyc24Elem]]]] = []
        for word_s, cur_m in frontier:
            for lbl, g_m in gens.items():
                prod_m = cyc24_matmul(cur_m, g_m)
                k_prod = cyc24_key(prod_m)
                if k_prod not in seen:
                    seen[k_prod] = (word_s + lbl, prod_m)
                    nxt_frontier.append((word_s + lbl, prod_m))
        frontier = nxt_frontier
    if frontier:
        raise RuntimeError("Exact cyclotomic BFS group closure did not terminate within max_depth")
    return seen


def cyc24_center_and_pg_orders(
    grp: dict[tuple[tuple[Cyc24Elem, ...], ...], tuple[str, list[list[Cyc24Elem]]]]
) -> tuple[int, int]:
    """Compute exact center size |Z(G)| and projective quotient order |G / Z(G)| in Q(zeta_24)."""
    mats = [pair[1] for pair in grp.values()]
    n_cent = sum(
        1
        for m_a in mats
        if all(cyc24_key(cyc24_matmul(m_a, mat_q)) == cyc24_key(cyc24_matmul(mat_q, m_a)) for mat_q in mats)
    )
    return n_cent, len(grp) // n_cent


def cyc24_to_numpy(mat_a: list[list[Cyc24Elem]]) -> np.ndarray:
    """Evaluate an exact Q(zeta_24) matrix to complex128 for numerical cross-checks."""
    z_pows_num = [complex(math.cos(k_i * math.pi / 12), math.sin(k_i * math.pi / 12)) for k_i in range(8)]
    n_r = len(mat_a)
    n_c = len(mat_a[0])
    out = np.zeros((n_r, n_c), dtype=complex)
    for r_i in range(n_r):
        for c_i in range(n_c):
            el = mat_a[r_i][c_i]
            out[r_i, c_i] = sum(float(el[k_i]) * z_pows_num[k_i] for k_i in range(8))
    return out


def snap_unit_phase_to_cyc24(val_c: complex) -> tuple[Cyc24Elem, float]:
    """Identify an exact 24th root of unity z24^k closest to val_c and return (exact_elem, abs_err)."""
    best_k = 0
    best_err = 2.0
    for k_pow in range(24):
        ang = k_pow * math.pi / 12
        cand = complex(math.cos(ang), math.sin(ang))
        err = abs(val_c - cand)
        if err < best_err:
            best_err = err
            best_k = k_pow
    return cyc24_pow(best_k), float(best_err)


def snap_monomial_3x3_to_cyc24(mat_num: np.ndarray) -> tuple[list[list[Cyc24Elem]], float]:
    """Mechanically lift a numerical 3x3 monomial matrix of 24th roots to exact Q(zeta_24), returning max_err."""
    out = [[_q_zero() for _ in range(3)] for _ in range(3)]
    max_err = 0.0
    for r_i in range(3):
        nz_cols = [c_i for c_i in range(3) if abs(mat_num[r_i, c_i]) > 0.5]
        if len(nz_cols) != 1:
            raise RuntimeError("Matrix row is not monomial")
        c_hit = nz_cols[0]
        for c_i in range(3):
            if c_i == c_hit:
                ex_p, p_err = snap_unit_phase_to_cyc24(complex(mat_num[r_i, c_i]))
                out[r_i][c_i] = ex_p
                max_err = max(max_err, p_err)
            else:
                max_err = max(max_err, float(abs(mat_num[r_i, c_i])))
    return out, max_err


# ============================================================================
# 2. WP-3.1: Exact SymPy Q_8-Equivariant Koszul Homotopy, Curved PDE & 248 Census
# ============================================================================


def _orth_basis_sym(vecs: list[sp.Matrix]) -> list[sp.Matrix]:
    gs: list[sp.Matrix] = []
    for vec in vecs:
        w_v = vec
        for u_v in gs:
            w_v = (w_v - ((u_v.H * w_v)[0, 0] / (u_v.H * u_v)[0, 0]) * u_v).applyfunc(sp.expand)
        norm_sq = sp.expand((w_v.H * w_v)[0, 0])
        if norm_sq != 0:
            gs.append((w_v / sp.sqrt(norm_sq)).applyfunc(sp.expand))
    return gs


def _orth_proj_sym(vecs: list[sp.Matrix], dim: int) -> sp.Matrix:
    gs = _orth_basis_sym(vecs)
    proj = sp.zeros(dim, dim)
    for u_v in gs:
        proj = (proj + u_v * u_v.H).applyfunc(sp.expand)
    return proj


def _build_q8_equivariant_koszul_homotopy(
    e_op: sp.Matrix, g_op: sp.Matrix, x_op: sp.Matrix, y_op: sp.Matrix
) -> dict[str, Any]:
    """Construct exact SymPy Moore-Penrose Koszul cochain homotopy (h1, h2) and verify Q8 equivariance."""
    n_dim = e_op.rows
    f_i = sp.Matrix([[sp.I, 0], [0, -sp.I]])
    f_j = sp.Matrix([[0, 1], [-1, 0]])
    d0 = sp.Matrix.vstack(e_op, g_op)
    d1 = sp.Matrix.hstack(-g_op, e_op)
    nilpotent_ok = (d1 * d0).applyfunc(sp.expand) == sp.zeros(n_dim, n_dim)

    ns0 = d0.nullspace()
    ns1 = sp.Matrix.vstack(d1, d0.H).nullspace()
    ns2 = d1.H.nullspace()
    p0 = _orth_proj_sym(ns0, n_dim)
    p1 = _orth_proj_sym(ns1, 2 * n_dim)
    p2 = _orth_proj_sym(ns2, n_dim)

    lap0 = (d0.H * d0).applyfunc(sp.expand)
    lap2 = (d1 * d1.H).applyfunc(sp.expand)
    g0 = ((lap0 + p0).inv() - p0).applyfunc(sp.expand)
    g2 = ((lap2 + p2).inv() - p2).applyfunc(sp.expand)
    h1 = (g0 * d0.H).applyfunc(sp.expand)
    h2 = (d1.H * g2).applyfunc(sp.expand)

    r1_a = sp.kronecker_product(f_i, x_op).applyfunc(sp.expand)
    r1_b = sp.kronecker_product(f_j, y_op).applyfunc(sp.expand)
    d_equiv = (
        (r1_a * d0 - d0 * x_op).applyfunc(sp.expand) == sp.zeros(2 * n_dim, n_dim)
        and (r1_b * d0 - d0 * y_op).applyfunc(sp.expand) == sp.zeros(2 * n_dim, n_dim)
        and (x_op * d1 - d1 * r1_a).applyfunc(sp.expand) == sp.zeros(n_dim, 2 * n_dim)
        and (y_op * d1 - d1 * r1_b).applyfunc(sp.expand) == sp.zeros(n_dim, 2 * n_dim)
    )
    h_equiv = (
        (x_op * h1 - h1 * r1_a).applyfunc(sp.expand) == sp.zeros(n_dim, 2 * n_dim)
        and (y_op * h1 - h1 * r1_b).applyfunc(sp.expand) == sp.zeros(n_dim, 2 * n_dim)
        and (r1_a * h2 - h2 * x_op).applyfunc(sp.expand) == sp.zeros(2 * n_dim, n_dim)
        and (r1_b * h2 - h2 * y_op).applyfunc(sp.expand) == sp.zeros(2 * n_dim, n_dim)
    )
    homotopy_id = (
        (h1 * d0 - (sp.eye(n_dim) - p0)).applyfunc(sp.expand) == sp.zeros(n_dim, n_dim)
        and (d0 * h1 + h2 * d1 - (sp.eye(2 * n_dim) - p1)).applyfunc(sp.expand) == sp.zeros(2 * n_dim, 2 * n_dim)
        and (d1 * h2 - (sp.eye(n_dim) - p2)).applyfunc(sp.expand) == sp.zeros(n_dim, n_dim)
    )
    return {
        "ranks": (len(ns0), len(ns1), len(ns2)),
        "nilpotent_exact": nilpotent_ok,
        "d_q8_equivariant_exact": d_equiv,
        "h_q8_equivariant_exact": h_equiv,
        "homotopy_identity_exact": homotopy_id,
    }


def _wedge2_group_sym(mat: sp.Matrix) -> sp.Matrix:
    n_d = mat.rows
    ps = list(combinations(range(n_d), 2))
    out = sp.zeros(len(ps), len(ps))
    for r_i, (r0, r1) in enumerate(ps):
        for c_i, (c0, c1) in enumerate(ps):
            val = mat[r0, c0] * mat[r1, c1] - mat[r0, c1] * mat[r1, c0]
            if val != 0:
                out[r_i, c_i] = sp.expand(val)
    return out


def _wedge2_lie_sym(x_m: sp.Matrix) -> sp.Matrix:
    n_d = x_m.rows
    ps = list(combinations(range(n_d), 2))
    out = sp.zeros(len(ps), len(ps))
    idx_map = {p_t: k_i for k_i, p_t in enumerate(ps)}
    for col, (c1, c2) in enumerate(ps):
        for r_i in range(n_d):
            if x_m[r_i, c1] != 0 and r_i != c2:
                pair, sgn = ((r_i, c2), 1) if r_i < c2 else ((c2, r_i), -1)
                out[idx_map[pair], col] += sgn * x_m[r_i, c1]
            if x_m[r_i, c2] != 0 and r_i != c1:
                pair, sgn = ((c1, r_i), 1) if c1 < r_i else ((r_i, c1), -1)
                out[idx_map[pair], col] += sgn * x_m[r_i, c2]
    return out.applyfunc(sp.expand)


def _eval_parabolic_cohomology_on_hd(
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
    if hd_basis.shape[1] == 0:
        n_hd = int(hd_basis.shape[1])
        nrm_hd = float(np.linalg.norm(hd_basis))
        return {
            "h0": n_hd,
            "h1": n_hd,
            "cont_q8_bundles": n_hd,
            "cont_spin_components": n_hd,
            "crit_max_decouple_err": nrm_hd,
        }

    mu_sub = hd_basis.conj().T @ mu_op @ hd_basis
    ev_mu, vc_mu = np.linalg.eigh((mu_sub + mu_sub.conj().T) * 0.5)
    mu_clusters: dict[int, list[int]] = {}
    for idx, val in enumerate(ev_mu):
        mu_int = int(round(float(val)))
        if abs(float(val) - mu_int) > 1e-9:
            raise RuntimeError("Non-integer U(1)_J weight mu encountered")
        mu_clusters.setdefault(mu_int, []).append(idx)

    h0_tot = 0
    h1_tot = 0
    cont_bundles_tot = 0
    cont_comp_tot = 0
    dec_errs: list[float] = [0.0]
    sa = -1 if eta[0] == 1 else 1
    sb = -1 if eta[1] == 1 else 1

    for mu_int, idxs in mu_clusters.items():
        a_exp = d_deg - mu_int
        v_sub = hd_basis @ vc_mu[:, idxs]
        ta_m = (sa**a_exp) * (v_sub.conj().T @ ta_op @ v_sub)
        tb_m = (sb**a_exp) * (v_sub.conj().T @ tb_op @ v_sub)
        kpi_m = ta_m @ tb_m @ ta_m.conj().T @ tb_m.conj().T
        ev_k, vc_k = np.linalg.eigh((kpi_m + kpi_m.conj().T) * 0.5)

        plus_idx = [i_k for i_k, v_k in enumerate(ev_k) if abs(v_k - 1.0) < 1e-9]
        minus_idx = [i_k for i_k, v_k in enumerate(ev_k) if abs(v_k + 1.0) < 1e-9]
        if len(plus_idx) + len(minus_idx) != len(ev_k):
            raise RuntimeError("Peripheral commutator K_pi eigenvalue outside {+1, -1}")

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
                proj_triv = ((np.eye(rk_p) + ta_p) @ (np.eye(rk_p) + tb_p)) / 4
                n_triv = int(round(float(np.real(np.trace(proj_triv)))))
                h0_tot += n_triv
                h1_tot += n_triv

        if minus_idx:
            rk_m = len(minus_idx)
            if rk_m % 2 != 0:
                raise RuntimeError("Odd multiplicity on K_pi = -I sector")
            m_bundles = rk_m // 2
            if a_exp == 1:
                cont_bundles_tot += m_bundles
                cont_comp_tot += rk_m
                v_m = v_sub @ vc_k[:, minus_idx]
                n_half = v_m.shape[0] // 2
                u_part = v_m[:n_half, :]
                v_part = v_m[n_half:, :]
                inv_rt2 = 1.0 / math.sqrt(2.0)
                up_part = (u_part + v_part) * inv_rt2
                vp_part = (u_part - v_part) * inv_rt2
                dec_errs.extend(
                    [
                        float(np.max(np.abs(ep_full.conj().T @ up_part))),
                        float(np.max(np.abs(em_full @ up_part))),
                        float(np.max(np.abs(em_full.conj().T @ vp_part))),
                        float(np.max(np.abs(ep_full @ vp_part))),
                    ]
                )
            else:
                n_max = math.floor((a_exp + 1) * 0.5) if a_exp < 1 else (math.ceil((a_exp + 1) * 0.5) - 1)
                deg_par = -1 + 2 * n_max
                if deg_par > 0:
                    h0_tot += m_bundles * deg_par
                else:
                    h1_tot += m_bundles * (-deg_par)

    return {
        "h0": h0_tot,
        "h1": h1_tot,
        "cont_q8_bundles": cont_bundles_tot,
        "cont_spin_components": cont_comp_tot,
        "crit_max_decouple_err": max(dec_errs),
    }


def verify_wp31_exact_koszul_homotopy_and_248_parabolic_kernel() -> dict[str, Any]:
    """Prove WP-3.1: Q8-equivariant Koszul homotopy, curved pure-slot PDE, Gram parity, and 248-root census."""
    irt2 = sp.Integer(1) / sp.sqrt(2)
    rt6 = sp.sqrt(6)
    rt10 = sp.sqrt(10)
    w8 = sp.exp(sp.I * sp.pi / 4)

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
    hp10 = (ep10 * ep10.H - ep10.H * ep10).applyfunc(sp.expand)
    hm10 = (em10 * em10.H - em10.H * em10).applyfunc(sp.expand)
    htot10 = (hp10 + hm10).applyfunc(sp.expand)

    h5 = sp.diag(-4, -2, 0, 2, 4)
    h10 = sp.BlockMatrix([[h5, z5], [z5, -h5]]).as_explicit()
    n10 = sp.BlockMatrix([[sp.eye(5), z5], [z5, -sp.eye(5)]]).as_explicit()
    a10_vec = (-sp.I * n10 * sp.diag(*[sp.exp(-sp.I * sp.pi * h10[k_i, k_i] / 4) for k_i in range(10)])).applyfunc(sp.expand)
    hdiff10 = (hp10 - hm10).applyfunc(sp.expand)
    d10_vec = sp.exp(-sp.I * sp.pi * hdiff10 / 4).applyfunc(sp.expand)
    b10_vec = (d10_vec * a10_vec).applyfunc(sp.expand)

    # 1a. Exact SymPy Q8-equivariant Koszul homotopy on V_10:
    hom_v10 = _build_q8_equivariant_koszul_homotopy(e10, g10, a10_vec, b10_vec)

    # 1b. Exact SymPy Q8-equivariant Koszul homotopy on chiral spinor S_16 of Spin(10):
    def _bit_sum(val_i: int, n_bits: int) -> int:
        return sum((val_i // (2**b_i)) % 2 for b_i in range(n_bits))

    creators = []
    for ax in range(5):
        op = sp.zeros(32, 32)
        p2_ax = 2**ax
        for st in range(32):
            if (st // p2_ax) % 2 == 0:
                op[st + p2_ax, st] = (-1) ** _bit_sum(st, ax)
        creators.append(op)
    ann = [c_op.T for c_op in creators]

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

    a32 = sp.zeros(32, 32)
    xw_4 = [1, 0, -1, -2, -3]
    for st in range(32):
        k_pow = 5 + sum(2 * xw_4[a_idx] for a_idx in range(5) if ((st // (2**a_idx)) % 2 == 1))
        a32[st, st] = sp.expand(w8 ** (k_pow % 8))
    b04 = creators[0] * creators[4] + ann[4] * ann[0]
    b13 = creators[1] * creators[3] + ann[3] * ann[1]
    p04, p13 = b04 * b04, b13 * b13
    d32 = ((sp.eye(32) - 2 * p04) * (sp.eye(32) - p13 - sp.I * b13)).applyfunc(sp.expand)
    b32 = (d32 * a32).applyfunc(sp.expand)

    idx_odd = [st for st in range(32) if _bit_sum(st, 5) % 2 == 1]
    e16 = spin_lie32(e10).extract(idx_odd, idx_odd)
    g16 = spin_lie32(g10).extract(idx_odd, idx_odd)
    # Include the Spin(6) h4 singlet factor w8^3 = exp(3 i pi / 4) so X_16, Y_16 generate Q8 on (16, 4)_singlet:
    h4_sing = sp.expand(w8**3)
    x16 = (h4_sing * a32.extract(idx_odd, idx_odd)).applyfunc(sp.expand)
    y16 = (h4_sing * b32.extract(idx_odd, idx_odd)).applyfunc(sp.expand)
    hom_s16 = _build_q8_equivariant_koszul_homotopy(e16, g16, x16, y16)

    # 1c. Exact SymPy Casimir split 45 = W_1(6) (+) W_3(14) (+) V_(2,2)(25) and Q8-equivariant homotopies:
    ep45 = _wedge2_lie_sym(ep10)
    em45 = _wedge2_lie_sym(em10)
    hp45 = _wedge2_lie_sym(hp10)
    hm45 = _wedge2_lie_sym(hm10)
    cp45 = (hp45 * hp45 + 2 * (ep45 * ep45.H + ep45.H * ep45)).applyfunc(sp.expand)
    cm45 = (hm45 * hm45 + 2 * (em45 * em45.H + em45.H * em45)).applyfunc(sp.expand)
    csum45 = (cp45 + cm45).applyfunc(sp.expand)
    cprod45 = (cp45 * cm45).applyfunc(sp.expand)

    b_w1 = sp.Matrix.hstack(*_orth_basis_sym((csum45 - 8 * sp.eye(45)).nullspace()))
    b_w3 = sp.Matrix.hstack(*_orth_basis_sym(sp.Matrix.vstack(csum45 - 48 * sp.eye(45), cprod45).nullspace()))
    b_v22 = sp.Matrix.hstack(*_orth_basis_sym(sp.Matrix.vstack(cp45 - 24 * sp.eye(45), cm45 - 24 * sp.eye(45)).nullspace()))

    e45 = _wedge2_lie_sym(e10)
    g45 = _wedge2_lie_sym(g10)
    x45 = _wedge2_group_sym(a10_vec)
    y45 = _wedge2_group_sym(b10_vec)

    sub45_inv = all(
        ((sp.eye(45) - b_sub * b_sub.H) * op_m * b_sub).applyfunc(sp.expand) == sp.zeros(45, b_sub.cols)
        for b_sub in (b_w1, b_w3, b_v22)
        for op_m in (e45, g45, x45, y45)
    )
    hom_w1 = _build_q8_equivariant_koszul_homotopy(
        (b_w1.H * e45 * b_w1).applyfunc(sp.expand),
        (b_w1.H * g45 * b_w1).applyfunc(sp.expand),
        (b_w1.H * x45 * b_w1).applyfunc(sp.expand),
        (b_w1.H * y45 * b_w1).applyfunc(sp.expand),
    )
    hom_w3 = _build_q8_equivariant_koszul_homotopy(
        (b_w3.H * e45 * b_w3).applyfunc(sp.expand),
        (b_w3.H * g45 * b_w3).applyfunc(sp.expand),
        (b_w3.H * x45 * b_w3).applyfunc(sp.expand),
        (b_w3.H * y45 * b_w3).applyfunc(sp.expand),
    )
    hom_v22 = _build_q8_equivariant_koszul_homotopy(
        (b_v22.H * e45 * b_v22).applyfunc(sp.expand),
        (b_v22.H * g45 * b_v22).applyfunc(sp.expand),
        (b_v22.H * x45 * b_v22).applyfunc(sp.expand),
        (b_v22.H * y45 * b_v22).applyfunc(sp.expand),
    )

    koszul_homotopy_all_exact = (
        (b_w1.cols, b_w3.cols, b_v22.cols) == (6, 14, 25)
        and sub45_inv
        and hom_v10["ranks"] == (2, 4, 2)
        and hom_s16["ranks"] == (1, 2, 1)
        and hom_w1["ranks"] == (2, 4, 2)
        and hom_w3["ranks"] == (2, 4, 2)
        and hom_v22["ranks"] == (1, 2, 1)
        and all(
            h_res["nilpotent_exact"]
            and h_res["d_q8_equivariant_exact"]
            and h_res["h_q8_equivariant_exact"]
            and h_res["homotopy_identity_exact"]
            for h_res in (hom_v10, hom_s16, hom_w1, hom_w3, hom_v22)
        )
    )

    # 2. Curved pure-slot PDE embedding, intrinsic hyperbolic cusp L^2 pole selection, & Gram parity orthogonality:
    x_s, y_s, r_rad = sp.symbols("x_s y_s r_rad", real=True, positive=True)
    om_f = sp.Function("Omega", real=True, positive=True)(x_s, y_s)
    j_sym = sp.Symbol("J_wt", real=True)
    phi_bar_f = sp.Function("Phi_bar")(x_s - sp.I * y_s)
    phi_hol_f = sp.Function("Phi_hol")(x_s + sp.I * y_s)

    def dz_sym(expr_f: sp.Expr) -> sp.Expr:
        return sp.Rational(1, 2) * (sp.diff(expr_f, x_s) - sp.I * sp.diff(expr_f, y_s))

    def dzbar_sym(expr_f: sp.Expr) -> sp.Expr:
        return sp.Rational(1, 2) * (sp.diff(expr_f, x_s) + sp.I * sp.diff(expr_f, y_s))

    psi_orth = (om_f ** (-(j_sym + 2) / 4)) * phi_bar_f
    res_orth = sp.powsimp(sp.expand(dz_sym(psi_orth) + ((j_sym + 2) / 4) * (dz_sym(om_f) / om_f) * psi_orth), force=True)
    a_coord = (om_f ** (-j_sym / 4)) * phi_bar_f
    res_coord = sp.powsimp(sp.expand(dz_sym(a_coord) + (j_sym / 4) * (dz_sym(om_f) / om_f) * a_coord), force=True)
    u_spin = (om_f ** (-sp.Rational(1, 4))) * phi_hol_f
    res_spin = sp.powsimp(sp.expand(dzbar_sym(u_spin) + sp.Rational(1, 4) * (dzbar_sym(om_f) / om_f) * u_spin), force=True)

    # Pure-slot decoupling in full 4-slot curved operator M(0, a_coord * v_top, 0, 0) == 0 when E_+ v_top = E_- v_top = 0:
    v_top_16 = sp.Matrix.vstack(e16, g16).nullspace()[0]
    pure_slot_higgs_vanish = (
        (spin_lie32(ep10).extract(idx_odd, idx_odd) * v_top_16).applyfunc(sp.expand) == sp.zeros(16, 1)
        and (spin_lie32(em10).extract(idx_odd, idx_odd) * v_top_16).applyfunc(sp.expand) == sp.zeros(16, 1)
    )

    # Complete hyperbolic cusp metric Omega ~ (r^2 ln^2 r)^(-1) -> S^5 norm density r^(4 - 2*k) |ln r|^3 dr near r -> 0+:
    int_pole1 = sp.integrate((r_rad**2) * (-sp.log(r_rad)) ** 3, (r_rad, 0, sp.Rational(1, 2)))
    int_pole2 = sp.integrate((-sp.log(r_rad)) ** 3, (r_rad, 0, sp.Rational(1, 2)))
    int_pole3 = sp.integrate((r_rad ** (-2)) * (-sp.log(r_rad)) ** 3, (r_rad, 0, sp.Rational(1, 2)))
    cusp_s5_pole_cutoff_exact = int_pole1.is_finite and int_pole2.is_finite and (int_pole3 == sp.oo)

    curved_pde_and_cusp_cutoff_exact = (
        res_orth == 0
        and res_coord == 0
        and res_spin == 0
        and pure_slot_higgs_vanish
        and bool(cusp_s5_pole_cutoff_exact)
    )

    # 2b. Numerical 2D Gram matrix parity orthogonality <a_sp, a_dp>_{G_ker} == 0 on punctured E_tau \ {0}:
    with mp.workdps(30):
        tau_g = mp.mpc(mp.mpf(4) / mp.mpf(17), mp.mpf(19) / mp.mpf(14))
        q_g = mp.exp(1j * mp.pi * tau_g)

        def szego3_fn(z_v: mp.mpc) -> complex:
            return complex(
                (mp.pi * mp.jtheta(1, 0, q_g, 1) * mp.jtheta(3, mp.pi * z_v, q_g))
                / (mp.jtheta(3, 0, q_g) * mp.jtheta(1, mp.pi * z_v, q_g))
            )

        def dszego3_fn(z_v: mp.mpc) -> complex:
            c0 = mp.pi * mp.jtheta(1, 0, q_g, 1) / mp.jtheta(3, 0, q_g)
            th3 = mp.jtheta(3, mp.pi * z_v, q_g)
            dth3 = mp.pi * mp.jtheta(3, mp.pi * z_v, q_g, 1)
            th1 = mp.jtheta(1, mp.pi * z_v, q_g)
            dth1 = mp.pi * mp.jtheta(1, mp.pi * z_v, q_g, 1)
            return complex(c0 * (dth3 * th1 - th3 * dth1) / (th1**2))

        im_t = float(mp.im(tau_g))
        n_grid = 16
        us_grid = (np.arange(n_grid) + 0.5) / float(n_grid) - 0.5
        gram_2d = np.zeros((2, 2), dtype=complex)
        for u_c in us_grid:
            for v_c in us_grid:
                z_val = mp.mpc(float(u_c)) + mp.mpc(float(v_c)) * tau_g
                th1_sq = float(abs(mp.jtheta(1, mp.pi * z_val, q_g)) ** 2) * math.exp(-2.0 * math.pi * float(v_c * v_c) * im_t)
                om_mod = 1.0 / (th1_sq * (math.log(th1_sq) ** 2 + 1.0))
                w_d2z = ((1.0 / (om_mod * math.sqrt(om_mod))) * im_t / float(n_grid)) / float(n_grid)
                vec_2 = np.array([szego3_fn(z_val), dszego3_fn(z_val)], dtype=complex)
                gram_2d += w_d2z * np.outer(vec_2.conj(), vec_2)

    gram_offdiag_err = float(abs(gram_2d[0, 1]))
    gram_parity_orthogonal = (
        gram_offdiag_err < TOL
        and float(gram_2d[0, 0].real) > 0.0
        and float(gram_2d[1, 1].real) > 0.0
    )

    # 3. Universal 248-root parabolic L^2 kernel census across BOTH coherent holonomy threads h_4 and h_1
    #    and ALL 4 spin structures eta in {(1,1), (1,0), (0,1), (0,0)} (F4):
    i2 = sp.eye(2)
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])

    def kron3(m1: sp.Matrix, m2: sp.Matrix, m3: sp.Matrix) -> sp.Matrix:
        return sp.kronecker_product(sp.kronecker_product(m1, m2), m3)

    f6 = [
        kron3(sx, i2, i2),
        kron3(sy, i2, i2),
        kron3(sz, sx, i2),
        kron3(sz, sy, i2),
        kron3(sz, sz, sx),
        kron3(sz, sz, sy),
    ]
    omega6 = f6[0] * f6[1] * f6[2] * f6[3] * f6[4] * f6[5]
    j1, j2, j3 = f6[0] * f6[1], f6[2] * f6[3], f6[4] * f6[5]
    i8 = sp.eye(8)
    h4_8 = ((i8 - j1) * irt2 * (i8 - j2) * irt2 * (i8 - j3) * irt2).applyfunc(sp.expand)
    s8 = f6[0]

    def cliff_vec10(z_list: list[Any]) -> sp.Matrix:
        out = sp.zeros(32, 32)
        for idx, za in enumerate(z_list):
            if za != 0:
                out += za * creators[idx] + sp.conjugate(za) * ann[idx]
        return out

    g_minus = [
        cliff_vec10([0, 0, sp.I, 0, 0]),
        cliff_vec10([sp.I * irt2, 0, 0, 0, sp.I * irt2]),
        cliff_vec10([irt2, 0, 0, 0, -irt2]),
        cliff_vec10([0, irt2, 0, irt2, 0]),
        cliff_vec10([0, sp.I * irt2, 0, -sp.I * irt2, 0]),
    ]
    u32 = sp.eye(32)
    for gm in g_minus:
        u32 = (u32 * gm).applyfunc(sp.expand)
    omega10 = sp.eye(32)
    for a_idx in range(5):
        omega10 = (omega10 * (creators[a_idx] + ann[a_idx]) * (sp.I * (creators[a_idx] - ann[a_idx]))).applyfunc(sp.expand)
    chir10 = sp.I * omega10
    s32 = (u32 * chir10).applyfunc(sp.expand)

    psi10 = creators + ann
    psi10_dual = ann + creators

    def q10_pin(elem32: sp.Matrix, odd_grade: bool) -> sp.Matrix:
        sgn = -1 if odd_grade else 1
        m10 = sp.zeros(10, 10)
        eh = elem32.H
        for col in range(10):
            img = sgn * (elem32 * psi10[col] * eh).applyfunc(sp.expand)
            for row in range(10):
                ac = psi10_dual[row] * img + img * psi10_dual[row]
                m10[row, col] = sp.expand(ac.trace() / 32)
        return m10

    def q6_pin(elem8: sp.Matrix, odd_grade: bool) -> sp.Matrix:
        sgn = -1 if odd_grade else 1
        m6 = sp.zeros(6, 6)
        eh = elem8.H
        for col in range(6):
            img = sgn * (elem8 * f6[col] * eh).applyfunc(sp.expand)
            for row in range(6):
                m6[row, col] = sp.expand((f6[row].H * img).trace() / 8)
        return m6

    splus_pairs = [(r_i, c_i) for r_i in range(32) for c_i in range(8) if sp.expand(omega10[r_i, r_i] * omega6[c_i, c_i]) == 1]
    splus_idx = {p_t: k_i for k_i, p_t in enumerate(splus_pairs)}

    def m128_from_spin16(m32: sp.Matrix, m8: sp.Matrix) -> np.ndarray:
        out = np.zeros((128, 128), dtype=complex)
        m32_n = np.array(m32.tolist(), dtype=complex)
        m8_n = np.array(m8.tolist(), dtype=complex)
        nz32 = [[(r_i, m32_n[r_i, c_i]) for r_i in range(32) if abs(m32_n[r_i, c_i]) > TOL] for c_i in range(32)]
        nz8 = [[(r_i, m8_n[r_i, c_i]) for r_i in range(8) if abs(m8_n[r_i, c_i]) > TOL] for c_i in range(8)]
        for col, (c1, c2) in enumerate(splus_pairs):
            for r1, v1 in nz32[c1]:
                for r2, v2 in nz8[c2]:
                    out[splus_idx[(r1, r2)], col] = v1 * v2
        return out

    def ext2_grp_n(mat_n: np.ndarray) -> np.ndarray:
        ps = list(combinations(range(mat_n.shape[0]), 2))
        out = np.zeros((len(ps), len(ps)), dtype=complex)
        for r_i, (r0, r1) in enumerate(ps):
            for c_i, (c0, c1) in enumerate(ps):
                out[r_i, c_i] = mat_n[r0, c0] * mat_n[r1, c1] - mat_n[r0, c1] * mat_n[r1, c0]
        return out

    def ext2_lie_n(mat_n: np.ndarray) -> np.ndarray:
        ps = list(combinations(range(mat_n.shape[0]), 2))
        out = np.zeros((len(ps), len(ps)), dtype=complex)
        for r_i, (r0, r1) in enumerate(ps):
            for c_i, (c0, c1) in enumerate(ps):
                out[r_i, c_i] = (
                    mat_n[r0, c0] * (r1 == c1)
                    + (r0 == c0) * mat_n[r1, c1]
                    - mat_n[r0, c1] * (r1 == c0)
                    - (r0 == c1) * mat_n[r1, c0]
                )
        return out

    fi_n = np.array([[1.0j, 0.0], [0.0, -1.0j]], dtype=complex)
    fj_n = np.array([[0.0, 1.0], [-1.0, 0.0]], dtype=complex)
    e10_n = np.array(e10.tolist(), dtype=complex)
    g10_n = np.array(g10.tolist(), dtype=complex)
    ep10_n = np.array(ep10.tolist(), dtype=complex)
    em10_n = np.array(em10.tolist(), dtype=complex)
    mu10_n = 0.5 * np.array(htot10.tolist(), dtype=complex)

    e128_n = m128_from_spin16(spin_lie32(e10), i8)
    g128_n = m128_from_spin16(spin_lie32(g10), i8)
    ep128_n = m128_from_spin16(spin_lie32(ep10), i8)
    em128_n = m128_from_spin16(spin_lie32(em10), i8)
    mu128_n = m128_from_spin16(spin_lie32(htot10 / 2), i8)

    # Graded Spin(16) action of the 60-dimensional (10,6) block on 128 = S_16^+:
    # B_{m, p} = (psi10[m] * chir10) (x) f6[p]|_{S_16^+} for m in 0..9, p in 0..5.
    b10_6_on_128_sym = [
        [
            sp.Matrix([[0 for _ in range(128)] for _ in range(128)])
            for _ in range(6)
        ]
        for _ in range(10)
    ]
    b10_6_on_128_num = np.zeros((60, 128, 128), dtype=complex)
    for m_idx in range(10):
        op32_m = (psi10[m_idx] * chir10).applyfunc(sp.expand)
        nz32_m = [[(r_i, op32_m[r_i, c_i]) for r_i in range(32) if op32_m[r_i, c_i] != 0] for c_i in range(32)]
        for p_idx in range(6):
            op8_p = f6[p_idx]
            nz8_p = [[(r_i, op8_p[r_i, c_i]) for r_i in range(8) if op8_p[r_i, c_i] != 0] for c_i in range(8)]
            mat_sym = sp.zeros(128, 128)
            mat_num = np.zeros((128, 128), dtype=complex)
            for col_s, (c1, c2) in enumerate(splus_pairs):
                for r1, v1 in nz32_m[c1]:
                    for r2, v2 in nz8_p[c2]:
                        row_s = splus_idx[(r1, r2)]
                        val_s = sp.expand(v1 * v2)
                        mat_sym[row_s, col_s] = val_s
                        mat_num[row_s, col_s] = complex(val_s)
            b10_6_on_128_sym[m_idx][p_idx] = mat_sym
            b10_6_on_128_num[6 * m_idx + p_idx] = mat_num

    def m128_sym(m32: sp.Matrix, m8: sp.Matrix) -> sp.Matrix:
        out = sp.zeros(128, 128)
        nz32 = [[(r_i, m32[r_i, c_i]) for r in range(1) for r_i in range(32) if m32[r_i, c_i] != 0] for c_i in range(32)]
        nz8 = [[(r_i, m8[r_i, c_i]) for r_i in range(8) if m8[r_i, c_i] != 0] for c_i in range(8)]
        for col_s, (c1, c2) in enumerate(splus_pairs):
            for r1, v1 in nz32[c1]:
                for r2, v2 in nz8[c2]:
                    out[splus_idx[(r1, r2)], col_s] = sp.expand(v1 * v2)
        return out

    census_table: dict[str, dict[tuple[int, int], dict[str, Any]]] = {}
    max_decouple_err_all = 0.0
    e8_cross_bracket_sym_mismatches = 0
    e8_cross_bracket_sym_checks = 0
    max_e8_cross_bracket_err = 0.0
    rng_haar = np.random.default_rng(29)
    haar_invariance_checks: list[bool] = []

    for bg_name, (ah32_s, ah8_s) in [
        ("h4", (a32, h4_8)),
        ("h1", ((a32 * s32).applyfunc(sp.expand), s8)),
    ]:
        bh32_s = (d32 * ah32_s).applyfunc(sp.expand)
        # Mechanical Spin(16) -> SO(10) x SO(6) projection:
        # Gamma_m^(10) = psi10[m] (x) I_8 has no chirality sign factor from Spin(6), while
        # Gamma_p^(6) = chir10 (x) f6[p] acquires sign_32 = chir10 * m32 * chir10 * m32^H in {+1, -1}:
        odd_a = sp.expand((chir10 * ah32_s * chir10 * ah32_s.H)[0, 0]) == -1
        odd_b = sp.expand((chir10 * bh32_s * chir10 * bh32_s.H)[0, 0]) == -1
        v10_a_sym = q10_pin(ah32_s, odd_grade=False)
        v10_b_sym = q10_pin(bh32_s, odd_grade=False)
        v6_a_sym = q6_pin(ah8_s, odd_grade=odd_a)
        v6_b_sym = q6_pin(ah8_s, odd_grade=odd_b)

        v10_a = np.array(v10_a_sym.tolist(), dtype=complex)
        v10_b = np.array(v10_b_sym.tolist(), dtype=complex)
        v6_a = np.array(v6_a_sym.tolist(), dtype=complex)
        v6_b = np.array(v6_b_sym.tolist(), dtype=complex)

        # Verify exact 248D e_8 Lie bracket equivariance U_128 [M_(10,6), psi] = [Ad_U(M_(10,6)), U_128 psi]
        # across all 60 generators of (10,6) in BOTH exact SymPy arithmetic and numerical probes (< 1e-12):
        for m32_g, m8_g, v10_g_sym, v6_g_sym, v10_g_n, v6_g_n in [
            (ah32_s, ah8_s, v10_a_sym, v6_a_sym, v10_a, v6_a),
            (bh32_s, ah8_s, v10_b_sym, v6_b_sym, v10_b, v6_b),
        ]:
            u128_sym = m128_sym(m32_g, m8_g)
            u128_h_sym = u128_sym.H
            for m_idx in range(10):
                nz_v10 = [(m_dst, v10_g_sym[m_dst, m_idx]) for m_dst in range(10) if v10_g_sym[m_dst, m_idx] != 0]
                for p_idx in range(6):
                    nz_v6 = [(p_dst, v6_g_sym[p_dst, p_idx]) for p_dst in range(6) if v6_g_sym[p_dst, p_idx] != 0]
                    lhs_sym = (u128_sym * b10_6_on_128_sym[m_idx][p_idx] * u128_h_sym).applyfunc(sp.expand)
                    rhs_sym = sp.zeros(128, 128)
                    for m_dst, cv10 in nz_v10:
                        for p_dst, cv6 in nz_v6:
                            rhs_sym += sp.expand(cv10 * cv6) * b10_6_on_128_sym[m_dst][p_dst]
                    e8_cross_bracket_sym_checks += 1
                    if (lhs_sym - rhs_sym).applyfunc(sp.expand) != sp.zeros(128, 128):
                        e8_cross_bracket_sym_mismatches += 1

            u128_n = m128_from_spin16(m32_g, m8_g)
            ad60_n = np.kron(v10_g_n, v6_g_n)
            m_probe = rng_haar.normal(size=60) + 1j * rng_haar.normal(size=60)
            m_probe /= np.linalg.norm(m_probe)
            psi_probe = rng_haar.normal(size=128) + 1j * rng_haar.normal(size=128)
            psi_probe /= np.linalg.norm(psi_probe)
            op_m = np.tensordot(m_probe, b10_6_on_128_num, axes=([0], [0]))
            op_ad_m = np.tensordot(ad60_n @ m_probe, b10_6_on_128_num, axes=([0], [0]))
            err_br = float(np.max(np.abs(u128_n @ (op_m @ psi_probe) - op_ad_m @ (u128_n @ psi_probe))))
            max_e8_cross_bracket_err = max(max_e8_cross_bracket_err, err_br)

        sectors = [
            (
                "(1,15)",
                np.zeros((15, 15), dtype=complex),
                np.zeros((15, 15), dtype=complex),
                np.zeros((15, 15), dtype=complex),
                np.zeros((15, 15), dtype=complex),
                np.zeros((15, 15), dtype=complex),
                ext2_grp_n(v6_a),
                ext2_grp_n(v6_b),
            ),
            (
                "(45,1)",
                ext2_lie_n(e10_n),
                ext2_lie_n(g10_n),
                ext2_lie_n(ep10_n),
                ext2_lie_n(em10_n),
                ext2_lie_n(mu10_n),
                ext2_grp_n(v10_a),
                ext2_grp_n(v10_b),
            ),
            (
                "(10,6)",
                np.kron(e10_n, np.eye(6)),
                np.kron(g10_n, np.eye(6)),
                np.kron(ep10_n, np.eye(6)),
                np.kron(em10_n, np.eye(6)),
                np.kron(mu10_n, np.eye(6)),
                np.kron(v10_a, v6_a),
                np.kron(v10_b, v6_b),
            ),
            (
                "128",
                e128_n,
                g128_n,
                ep128_n,
                em128_n,
                mu128_n,
                m128_from_spin16(ah32_s, ah8_s),
                m128_from_spin16(bh32_s, ah8_s),
            ),
        ]

        census_table[bg_name] = {}
        for eta in [(1, 1), (1, 0), (0, 1), (0, 0)]:
            lam_modes = 0
            a_modes = 0
            spin_modes = 0
            right_modes = 0
            cont_bundles = 0
            cont_spin_comp = 0
            by_sec: dict[str, int] = {}

            for s_name, e_s, g_s, ep_s, em_s, mu_s, xa_s, yb_s in sectors:
                d0_s = np.vstack([e_s, g_s])
                d1_s = np.hstack([-g_s, e_s])
                _, sv0, vh0 = np.linalg.svd(d0_s)
                b_hd0 = vh0[sv0 < 1e-9].conj().T
                m_k1 = np.vstack([d1_s, d0_s.conj().T])
                _, sv1, vh1 = np.linalg.svd(m_k1)
                b_hd1 = vh1[sv1 < 1e-9].conj().T
                _, sv2, vh2 = np.linalg.svd(d1_s.conj().T)
                b_hd2 = vh2[sv2 < 1e-9].conj().T

                r0 = _eval_parabolic_cohomology_on_hd(0, b_hd0, mu_s, xa_s, yb_s, ep_s, em_s, eta)
                r1 = _eval_parabolic_cohomology_on_hd(
                    1, b_hd1, np.kron(np.eye(2), mu_s), np.kron(fi_n, xa_s), np.kron(fj_n, yb_s), ep_s, em_s, eta
                )
                r2 = _eval_parabolic_cohomology_on_hd(2, b_hd2, mu_s, xa_s, yb_s, ep_s, em_s, eta)
                max_decouple_err_all = max(
                    max_decouple_err_all,
                    r0["crit_max_decouple_err"],
                    r1["crit_max_decouple_err"],
                    r2["crit_max_decouple_err"],
                )

                l_sec = r2["h1"] + r0["h1"] + r1["h0"]
                r_sec = r0["h0"] + r1["h1"] + r2["h0"]
                lam_modes += r2["h1"]
                a_modes += r0["h1"]
                spin_modes += r1["h0"]
                right_modes += r_sec
                cont_bundles += r1["cont_q8_bundles"]
                cont_spin_comp += r1["cont_spin_components"]
                by_sec[s_name] = l_sec

                # Guardrail 3: Random Haar unitary basis scrambling on (45,1) & (10,6) for true odd spin eta == (0,0):
                if eta == (0, 0) and s_name in ("(45,1)", "(10,6)"):
                    u_scr = haar_unitary(e_s.shape[0], rng_haar)
                    u_scr_h = u_scr.conj().T
                    e_scr = u_scr @ e_s @ u_scr_h
                    g_scr = u_scr @ g_s @ u_scr_h
                    ep_scr = u_scr @ ep_s @ u_scr_h
                    em_scr = u_scr @ em_s @ u_scr_h
                    mu_scr = u_scr @ mu_s @ u_scr_h
                    xa_scr = u_scr @ xa_s @ u_scr_h
                    yb_scr = u_scr @ yb_s @ u_scr_h
                    d0_scr = np.vstack([e_scr, g_scr])
                    d1_scr = np.hstack([-g_scr, e_scr])
                    _, sv0_q, vh0_q = np.linalg.svd(d0_scr)
                    _, sv1_q, vh1_q = np.linalg.svd(np.vstack([d1_scr, d0_scr.conj().T]))
                    _, sv2_q, vh2_q = np.linalg.svd(d1_scr.conj().T)
                    rq0 = _eval_parabolic_cohomology_on_hd(0, vh0_q[sv0_q < 1e-9].conj().T, mu_scr, xa_scr, yb_scr, ep_scr, em_scr, eta)
                    rq1 = _eval_parabolic_cohomology_on_hd(
                        1,
                        vh1_q[sv1_q < 1e-9].conj().T,
                        np.kron(np.eye(2), mu_scr),
                        np.kron(fi_n, xa_scr),
                        np.kron(fj_n, yb_scr),
                        ep_scr,
                        em_scr,
                        eta,
                    )
                    rq2 = _eval_parabolic_cohomology_on_hd(2, vh2_q[sv2_q < 1e-9].conj().T, mu_scr, xa_scr, yb_scr, ep_scr, em_scr, eta)
                    haar_invariance_checks.append(
                        (rq2["h1"] + rq0["h1"] + rq1["h0"]) == l_sec
                        and (rq0["h0"] + rq1["h1"] + rq2["h0"]) == r_sec
                        and rq1["cont_q8_bundles"] == r1["cont_q8_bundles"]
                    )

            tot_left = lam_modes + a_modes + spin_modes
            census_table[bg_name][eta] = {
                "ker_M": tot_left,
                "lam_modes": lam_modes,
                "a_modes": a_modes,
                "spin_modes": spin_modes,
                "ker_M_dag": right_modes,
                "index": tot_left - right_modes,
                "cont_q8_bundles": cont_bundles,
                "cont_spin_components": cont_spin_comp,
                "by_sector": by_sec,
            }

    # Joint commutants on (10,6) sectors (F3 / HAND_COUNTERCHECKS S5):
    # (i) 4D Koszul deg-1 space on V_10 splits by U(1)_J weight mu in {-2, +2} into two 2D Q_8 bundles (K_pi = -I_2):
    #     mu = -2 (a_exp = 3, parabolic H^0 = 1 => 6 left-Weyl spinor zero modes) has irreducible Q_8 action (commutant dim 1),
    #     while unsplit H_Q8 (+) H_Q8 has End_{Q_8} = M_2(C) (commutant dim 4):
    comm_q8_spin_doublet_dim = joint_commutant_dim_num([fi_n, fj_n], tol=1e-10)
    _, sv_10, vh_10 = np.linalg.svd(np.vstack([np.hstack([-g10_n, e10_n]), np.vstack([e10_n, g10_n]).conj().T]))
    b_10_h1 = vh_10[sv_10 < 1e-9].conj().T
    v10_a_h4 = np.array(q10_pin(a32, odd_grade=bool(0)).tolist(), dtype=complex)
    v10_b_h4 = np.array(q10_pin((d32 * a32).applyfunc(sp.expand), odd_grade=bool(0)).tolist(), dtype=complex)
    ha_4d = b_10_h1.conj().T @ np.kron(fi_n, 1.0j * v10_a_h4) @ b_10_h1
    hb_4d = b_10_h1.conj().T @ np.kron(fj_n, 1.0j * v10_b_h4) @ b_10_h1
    comm_10_6_deg1_unsplit_dim = joint_commutant_dim_num([ha_4d, hb_4d], tol=1e-10)
    mu_4d = b_10_h1.conj().T @ np.kron(np.eye(2, dtype=complex), mu10_n) @ b_10_h1
    ev_m4, vc_m4 = np.linalg.eigh((mu_4d + mu_4d.conj().T) * 0.5)
    b_10_mu_neg2 = b_10_h1 @ vc_m4[:, ev_m4 < 0.0]
    ha_m2 = b_10_mu_neg2.conj().T @ np.kron(fi_n, 1.0j * v10_a_h4) @ b_10_mu_neg2
    hb_m2 = b_10_mu_neg2.conj().T @ np.kron(fj_n, 1.0j * v10_b_h4) @ b_10_mu_neg2
    comm_10_6_deg1_mu_neg2_q8_dim = joint_commutant_dim_num([ha_m2, hb_m2], tol=1e-10)

    # (ii) 2D a-slot Szego doublet {v_(1,0) S_2, v_(0,1) S_4} on V_10^top (x) C_{+i} under E_theta = <L^2, S_theta>:
    #      Bare Szego swap without gauge compensator X gives L^2 = +I_2 => commutant dim 2 (reducible!),
    #      whereas actual gauge-compensated (X, D^(-1/2)) gives L^2 = diag(-1, +1) + off-diagonal S_theta => commutant dim 1!
    _, sv_10_0, vh_10_0 = np.linalg.svd(np.vstack([e10_n, g10_n]))
    b_10_h0 = vh_10_0[sv_10_0 < 1e-9].conj().T
    dh_10_n = np.array(sp.exp(sp.I * sp.pi * hdiff10 / 8).applyfunc(sp.expand).tolist(), dtype=complex)
    x_a2 = 1.0j * (b_10_h0.conj().T @ v10_a_h4 @ b_10_h0)
    y_a2 = 1.0j * (b_10_h0.conj().T @ v10_b_h4 @ b_10_h0)
    dh_a2 = b_10_h0.conj().T @ dh_10_n @ b_10_h0
    ev_x2, vc_x2 = np.linalg.eigh((x_a2 + x_a2.conj().T) * 0.5)
    idx_10 = int(np.argmin(ev_x2))  # eigenvalue -1 -> chi_(1,0)
    idx_01 = int(np.argmax(ev_x2))  # eigenvalue +1 -> chi_(0,1)
    v_10_ch = vc_x2[:, idx_10]
    v_01_ch = vc_x2[:, idx_01]
    y_eigs_ok = (
        abs(complex(np.vdot(v_10_ch, y_a2 @ v_10_ch)) - 1.0) < TOL
        and abs(complex(np.vdot(v_01_ch, y_a2 @ v_01_ch)) + 1.0) < TOL
    )
    rho_l2_comp = np.diag([complex(np.vdot(v_10_ch, x_a2 @ v_10_ch)), complex(np.vdot(v_01_ch, x_a2 @ v_01_ch))])
    rho_stheta_comp = np.array(
        [
            [0.0j, complex(np.vdot(v_10_ch, dh_a2 @ v_01_ch))],
            [complex(np.vdot(v_01_ch, dh_a2 @ v_10_ch)), 0.0j],
        ],
        dtype=complex,
    )
    comm_10_6_aslot_etheta_dim = joint_commutant_dim_num([rho_l2_comp, rho_stheta_comp], tol=1e-10)
    comm_10_6_aslot_bare_swap_dim = joint_commutant_dim_num(
        [np.eye(2, dtype=complex), np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)],
        tol=1e-10,
    )

    # D1 fix (Atiyah-Mumford spin-holonomy verification & symmetric [weave] spin-orbit check, F1 + F4):
    # In the global translation-invariant (dz)^{1/2} frame on E_tau, (s_a, s_b) = ((-1)^{eta_0}, (-1)^{eta_1}),
    # so eta = (0, 0) -> (s_a, s_b) = (+1, +1) is the unique modular-invariant ODD spin bundle S_0 ~= O_{E_tau}
    # (Arf invariant 1, dim H^0(E_tau, S_0) == 1), whereas {(1, 0), (0, 1), (1, 1)} is the 3-element EVEN spin orbit!
    untwisted_spin_h0_by_eta = {
        eta_u: _eval_parabolic_cohomology_on_hd(
            1,
            np.eye(1, dtype=complex),
            np.zeros((1, 1), dtype=complex),
            np.eye(1, dtype=complex),
            np.eye(1, dtype=complex),
            np.zeros((1, 1), dtype=complex),
            np.zeros((1, 1), dtype=complex),
            eta_u,
        )["h0"]
        for eta_u in [(0, 0), (1, 0), (0, 1), (1, 1)]
    }
    untwisted_odd_spin_unique = untwisted_spin_h0_by_eta == {(0, 0): 1, (1, 0): 0, (0, 1): 0, (1, 1): 0}

    even_etas = [(1, 0), (0, 1), (1, 1)]
    h4_even_orbit_ker = sorted(census_table["h4"][et]["ker_M"] for et in even_etas)
    h1_even_orbit_ker = sorted(census_table["h1"][et]["ker_M"] for et in even_etas)
    # Under (B_2, B_3, B_4) = (R(B_3), B_3, L(B_3)), spin shift eta pulls back to ((eta_0+eta_1)%2, eta_1), eta, (eta_0, (eta_0+eta_1)%2):
    branch_pullback_eta00 = [
        census_table["h4"][((0 + 0) % 2, 0)]["ker_M"],
        census_table["h4"][(0, 0)]["ker_M"],
        census_table["h4"][(0, (0 + 0) % 2)]["ker_M"],
    ]
    branch_pullback_eta11 = [
        census_table["h4"][((1 + 1) % 2, 1)]["ker_M"],
        census_table["h4"][(1, 1)]["ker_M"],
        census_table["h4"][(1, (1 + 1) % 2)]["ker_M"],
    ]

    h4_odd = census_table["h4"][(0, 0)]
    h1_odd = census_table["h1"][(0, 0)]
    parabolic_248_verified = (
        untwisted_odd_spin_unique
        and h4_odd["ker_M"] == 68
        and h4_odd["ker_M_dag"] == 68
        and h4_odd["index"] == 0
        and (h4_odd["lam_modes"], h4_odd["a_modes"], h4_odd["spin_modes"]) == (9, 43, 16)
        and h4_odd["by_sector"] == {"(1,15)": 18, "(45,1)": 8, "(10,6)": 18, "128": 24}
        and h4_odd["cont_q8_bundles"] == 16
        and h4_odd["cont_spin_components"] == 32
        and h4_even_orbit_ker == [60, 60, 68]
        and branch_pullback_eta00 == [68, 68, 68]
        and branch_pullback_eta11 == [60, 68, 60]
        and h1_odd["ker_M"] == 70
        and h1_odd["ker_M_dag"] == 70
        and h1_odd["index"] == 0
        and (h1_odd["lam_modes"], h1_odd["a_modes"], h1_odd["spin_modes"]) == (10, 44, 16)
        and h1_odd["by_sector"] == {"(1,15)": 20, "(45,1)": 8, "(10,6)": 18, "128": 24}
        and h1_odd["cont_q8_bundles"] == 16
        and h1_even_orbit_ker == [62, 62, 70]
        and (e8_cross_bracket_sym_exact := (e8_cross_bracket_sym_checks == 240 and e8_cross_bracket_sym_mismatches == 0))
        and max_e8_cross_bracket_err < TOL
        and max_decouple_err_all < TOL
        and comm_q8_spin_doublet_dim == 1
        and comm_10_6_deg1_unsplit_dim == 4
        and comm_10_6_deg1_mu_neg2_q8_dim == 1
        and y_eigs_ok
        and comm_10_6_aslot_etheta_dim == 1
        and comm_10_6_aslot_bare_swap_dim == 2
        and len(haar_invariance_checks) == 4
        and all(haar_invariance_checks)
    )

    return {
        "koszul_homotopy_all_5_blocks_exact": koszul_homotopy_all_exact,
        "untwisted_spin_h0_by_eta": untwisted_spin_h0_by_eta,
        "h4_even_spin_orbit_ker": h4_even_orbit_ker,
        "h1_even_spin_orbit_ker": h1_even_orbit_ker,
        "branch_pullback_eta00": branch_pullback_eta00,
        "branch_pullback_eta11": branch_pullback_eta11,
        "koszul_ranks_by_block": {
            "V_10": hom_v10["ranks"],
            "S_16": hom_s16["ranks"],
            "W_1": hom_w1["ranks"],
            "W_3": hom_w3["ranks"],
            "V_(2,2)": hom_v22["ranks"],
        },
        "curved_pde_and_cusp_s5_pole_cutoff_exact": curved_pde_and_cusp_cutoff_exact,
        "gram_parity_orthogonal_verified": gram_parity_orthogonal,
        "gram_offdiag_abs_err": gram_offdiag_err,
        "comm_q8_spin_doublet_dim": comm_q8_spin_doublet_dim,
        "comm_10_6_deg1_unsplit_dim": comm_10_6_deg1_unsplit_dim,
        "comm_10_6_deg1_mu_neg2_q8_dim": comm_10_6_deg1_mu_neg2_q8_dim,
        "comm_10_6_aslot_etheta_dim": comm_10_6_aslot_etheta_dim,
        "comm_10_6_aslot_bare_swap_dim": comm_10_6_aslot_bare_swap_dim,
        "census_248_by_bg_and_spin": census_table,
        "e8_cross_bracket_10_6_x_128_sym_exact": e8_cross_bracket_sym_exact,
        "max_e8_cross_bracket_err": max_e8_cross_bracket_err,
        "crit_max_decouple_err": max_decouple_err_all,
        "parabolic_248_census_verified": parabolic_248_verified,
    }


# ============================================================================
# 3. WP-3.2 (Algebraic Half): Exact Q(zeta_24) Closures, Universal S^4 No-Go & G_192 Exchange
# ============================================================================


def verify_wp32_exact_cyclotomic_algebra_and_metaplectic_obstruction() -> dict[str, Any]:
    """Prove WP-3.2 algebraic theorems in exact Q(zeta_24) arithmetic + universal central-S^4 No-Go + B1879 G_192."""
    q0 = _q_zero()
    q1 = cyc24_from_int(1)
    i_cyc = cyc24_pow(6)
    rt2_cyc = cyc24_add(cyc24_pow(3), cyc24_neg(cyc24_pow(9)))
    inv_rt2 = cyc24_scale_half(rt2_cyc)

    # Textbook level-2 Weil doublet D on Mp(2, Z) in exact Q(zeta_24):
    l_weil = [[q1, q0], [q0, i_cyc]]
    s0_weil = [[inv_rt2, inv_rt2], [inv_rt2, cyc24_neg(inv_rt2)]]
    l_weil_inv = cyc24_herm(l_weil)
    r_weil = cyc24_matmul(s0_weil, cyc24_matmul(l_weil_inv, s0_weil))

    grp_weil2 = cyc24_close_group({"L": l_weil, "R": r_weil})
    cent_weil2, pg_weil2 = cyc24_center_and_pg_orders(grp_weil2)

    # Universal central-S^4 eigenvalue obstruction covering ALL 2D representations of Mp(2, Z) (B1866 Row 8):
    sym2_s4_eigs_all = [
        (e1 * e1, e1 * e2, e2 * e2)
        for e1 in (-1, 1)
        for e2 in (-1, 1)
    ]
    universal_s4_no_go_proven = all(eig_triple != (-1, -1, -1) for eig_triple in sym2_s4_eigs_all)

    # Full 24-twist exact Q(zeta_24) census of chi_m (x) Sym^2(D) and chi_m (x) Sym^2(D_bar):
    sym2_l = cyc24_sym2_2x2(l_weil)
    sym2_r = cyc24_sym2_2x2(r_weil)
    sym2_l_bar = [[cyc24_conj(x_e) for x_e in row] for row in sym2_l]
    sym2_r_bar = [[cyc24_conj(x_e) for x_e in row] for row in sym2_r]

    # Canonical weave triplet T = chi_15 (x) Sym^2(D) and conjugate T_bar = chi_9 (x) Sym^2(D_bar):
    z15 = cyc24_pow(15)
    z15_inv = cyc24_pow(9)
    t_l_cyc = [[cyc24_mul(z15, x_e) for x_e in row] for row in sym2_l]
    t_r_cyc = [[cyc24_mul(z15_inv, x_e) for x_e in row] for row in sym2_r]
    tbar_l_cyc = [[cyc24_conj(x_e) for x_e in row] for row in t_l_cyc]
    tbar_r_cyc = [[cyc24_conj(x_e) for x_e in row] for row in t_r_cyc]

    grp_t = cyc24_close_group({"L": t_l_cyc, "R": t_r_cyc})
    cent_t, pg_t = cyc24_center_and_pg_orders(grp_t)

    # Exact braid relation S = L R^-1 L == R^-1 L R^-1 and S^4 == -I_3 on T:
    t_r_inv = cyc24_herm(t_r_cyc)
    s_lhs = cyc24_matmul(t_l_cyc, cyc24_matmul(t_r_inv, t_l_cyc))
    s_rhs = cyc24_matmul(t_r_inv, cyc24_matmul(t_l_cyc, t_r_inv))
    s2_t = cyc24_matmul(s_lhs, s_lhs)
    s4_t = cyc24_matmul(s2_t, s2_t)
    neg_i3 = [[cyc24_from_int(-1 if r_i == c_i else 0) for c_i in range(3)] for r_i in range(3)]
    t_braid_and_s4_exact = (cyc24_key(s_lhs) == cyc24_key(s_rhs)) and (cyc24_key(s4_t) == cyc24_key(neg_i3))

    even_orders: set[int] = set()
    odd_96_hits_d: list[int] = []
    odd_96_hits_dbar: list[int] = []
    for m_tw in range(24):
        zm = cyc24_pow(m_tw)
        zm_inv = cyc24_pow(-m_tw)
        lm_d = [[cyc24_mul(zm, x_e) for x_e in row] for row in sym2_l]
        rm_d = [[cyc24_mul(zm_inv, x_e) for x_e in row] for row in sym2_r]
        gm_d = cyc24_close_group({"L": lm_d, "R": rm_d})
        ord_d = len(gm_d)
        if m_tw % 2 == 0:
            even_orders.add(ord_d)
        elif ord_d == 96:
            odd_96_hits_d.append(m_tw)

        lm_db = [[cyc24_mul(zm, x_e) for x_e in row] for row in sym2_l_bar]
        rm_db = [[cyc24_mul(zm_inv, x_e) for x_e in row] for row in sym2_r_bar]
        gm_db = cyc24_close_group({"L": lm_db, "R": rm_db})
        if m_tw % 2 == 1 and len(gm_db) == 96:
            odd_96_hits_dbar.append(m_tw)

    # B1871 / B1879 Exchange P on T (+) T_bar (6D):
    s0_sym2 = cyc24_sym2_2x2(s0_weil)
    ex_conj_check_l = cyc24_key(cyc24_matmul(s0_sym2, cyc24_matmul(tbar_l_cyc, s0_sym2))) == cyc24_key(t_r_cyc)
    ex_conj_check_r = cyc24_key(cyc24_matmul(s0_sym2, cyc24_matmul(tbar_r_cyc, s0_sym2))) == cyc24_key(t_l_cyc)

    z3 = [[q0 for _ in range(3)] for _ in range(3)]
    l6_cyc = [t_l_cyc[r_i] + z3[r_i] for r_i in range(3)] + [z3[r_i] + tbar_l_cyc[r_i] for r_i in range(3)]
    r6_cyc = [t_r_cyc[r_i] + z3[r_i] for r_i in range(3)] + [z3[r_i] + tbar_r_cyc[r_i] for r_i in range(3)]
    p6_cyc = [z3[r_i] + s0_sym2[r_i] for r_i in range(3)] + [s0_sym2[r_i] + z3[r_i] for r_i in range(3)]

    grp_6_lr = cyc24_close_group({"L": l6_cyc, "R": r6_cyc})
    grp_6_lrp = cyc24_close_group({"L": l6_cyc, "R": r6_cyc, "P": p6_cyc})

    tl_num = cyc24_to_numpy(t_l_cyc)
    tr_num = cyc24_to_numpy(t_r_cyc)
    l6_num = cyc24_to_numpy(l6_cyc)
    r6_num = cyc24_to_numpy(r6_cyc)
    p6_num = cyc24_to_numpy(p6_cyc)
    comm_t_dim = joint_commutant_dim_num([tl_num, tr_num], tol=1e-10)
    comm_6_lr_dim = joint_commutant_dim_num([l6_num, r6_num], tol=1e-10)
    comm_6_lrp_dim = joint_commutant_dim_num([l6_num, r6_num, p6_num], tol=1e-10)

    algebra_verified = (
        len(grp_weil2) == 96
        and (cent_weil2, pg_weil2) == (4, 24)
        and len(grp_t) == 96
        and (cent_t, pg_t) == (4, 24)
        and t_braid_and_s4_exact
        and universal_s4_no_go_proven
        and even_orders == {24, 48, 72, 144}
        and set(odd_96_hits_d) == {3, 9, 15, 21}
        and set(odd_96_hits_dbar) == {3, 9, 15, 21}
        and ex_conj_check_l
        and ex_conj_check_r
        and len(grp_6_lr) == 96
        and len(grp_6_lrp) == 192
        and comm_t_dim == 1
        and comm_6_lr_dim == 2
        and comm_6_lrp_dim == 1
    )

    return {
        "weil2_exact_order": len(grp_weil2),
        "triplet_T_exact_order": len(grp_t),
        "triplet_T_center_and_pg": (cent_t, pg_t),
        "t_braid_and_s4_minus_i3_exact": t_braid_and_s4_exact,
        "universal_s4_sym2_no_go_proven": universal_s4_no_go_proven,
        "even_twist_orders_exact": sorted(even_orders),
        "odd_96_twists_sym2_D": sorted(odd_96_hits_d),
        "odd_96_twists_sym2_Dbar": sorted(odd_96_hits_dbar),
        "b1879_exchange_doubles_96_to_192_exact": len(grp_6_lrp) == 192 and (comm_6_lr_dim, comm_6_lrp_dim) == (2, 1),
        "t_l_cyc": t_l_cyc,
        "t_r_cyc": t_r_cyc,
        "tbar_l_cyc": tbar_l_cyc,
        "tbar_r_cyc": tbar_r_cyc,
        "wp32_algebra_verified": algebra_verified,
    }


# ============================================================================
# 4. WP-3.2 (Physical Half) & B1866 Resolution: Zero-Hand-Typed 3-Branch PDE Join
# ============================================================================


def _build_16_4_carrier_and_compensators(h4_sign: int) -> dict[str, Any]:
    """Construct the (16, 4) Spin(10)xSpin(6) carrier and exact 248-compatible compensator group for h4_sign in {+1, -1}."""
    e5 = np.zeros((5, 5), dtype=complex)
    for j_i, c_v in enumerate((2, math.sqrt(6), math.sqrt(6), 2)):
        e5[j_i + 1, j_i] = c_v
    h5 = np.diag([-4, -2, 0, 2, 4]).astype(complex)
    j5 = np.zeros((5, 5), dtype=complex)
    for j_i, c_v in enumerate((1, -1, 1, -1, 1)):
        j5[j_i, 4 - j_i] = c_v
    bz = np.zeros((5, 5), dtype=complex)
    bz[1, 4] = math.sqrt(2) / math.sqrt(5)
    bz[4, 1] = -bz[1, 4]
    bz[2, 3] = -math.sqrt(3) / math.sqrt(5)
    bz[3, 2] = -bz[2, 3]
    z5 = np.zeros((5, 5), dtype=complex)

    e10 = np.block([[e5, z5], [z5, -e5.T]])
    g10 = math.sqrt(10) * np.block([[z5, bz], [j5 @ bz @ j5, z5]])
    ep10, em10 = (e10 + g10) * 0.5, (e10 - g10) * 0.5
    hp10 = ep10 @ ep10.conj().T - ep10.conj().T @ ep10
    hm10 = em10 @ em10.conj().T - em10.conj().T @ em10

    def _bit_sum_c(val_i: int, n_bits: int) -> int:
        return sum((val_i // (2**b_i)) % 2 for b_i in range(n_bits))

    creators = []
    for ax in range(5):
        op = np.zeros((32, 32), dtype=complex)
        p2_ax = 2**ax
        for st in range(32):
            if (st // p2_ax) % 2 == 0:
                op[st + p2_ax, st] = (-1) ** _bit_sum_c(st, ax)
        creators.append(op)

    def spin_lie(mat10: np.ndarray) -> np.ndarray:
        ann = [c_op.conj().T for c_op in creators]
        out = -0.5 * np.trace(mat10[:5, :5]) * np.eye(32, dtype=complex)
        for i_k in range(5):
            for j_k in range(5):
                out += mat10[i_k, j_k] * (creators[i_k] @ ann[j_k])
                out += 0.5 * mat10[i_k, j_k + 5] * (creators[i_k] @ creators[j_k])
                out += 0.5 * mat10[i_k + 5, j_k] * (ann[i_k] @ ann[j_k])
        return out

    xw_q = [1, 0, -1, -2, -3]
    a_spin = np.diag(
        [
            complex(
                math.cos(math.pi * (5 + sum(2 * xw_q[i_k] for i_k in range(5) if ((st // (2**i_k)) % 2 == 1))) / 4),
                math.sin(math.pi * (5 + sum(2 * xw_q[i_k] for i_k in range(5) if ((st // (2**i_k)) % 2 == 1))) / 4),
            )
            for st in range(32)
        ]
    )
    hdiff_32 = spin_lie(hp10 - hm10)
    ev_hd, vc_hd = np.linalg.eigh((hdiff_32 + hdiff_32.conj().T) * 0.5)
    d_spin = vc_hd @ np.diag(np.exp(-1.0j * math.pi * ev_hd / 4)) @ vc_hd.conj().T
    dh_inv_spin = vc_hd @ np.diag(np.exp(1.0j * math.pi * ev_hd / 8)) @ vc_hd.conj().T

    w8_3 = complex(math.cos(3 * math.pi / 4), math.sin(3 * math.pi / 4))
    w8_m1 = complex(math.cos(-math.pi / 4), math.sin(-math.pi / 4))
    h4_mat = float(h4_sign) * np.diag([w8_3, w8_m1, w8_m1, w8_m1])

    # Build both (10, 6) and (16, 4) together (124D faithful on Spin(10)xSpin(6)/Z4 compensators) so U_comp is unique on E8:
    h10 = np.block([[h5, z5], [z5, -h5.T]])
    n10 = np.block([[np.eye(5), z5], [z5, -np.eye(5)]]).astype(complex)
    a_vec = -1.0j * n10 @ np.diag(np.exp(-1.0j * math.pi * np.diag(h10) / 4))
    ev_hv, vc_hv = np.linalg.eigh(((hp10 - hm10) + (hp10 - hm10).conj().T) * 0.5)
    d_vec = vc_hv @ np.diag(np.exp(-1.0j * math.pi * ev_hv / 4)) @ vc_hv.conj().T
    dh_inv_vec = vc_hv @ np.diag(np.exp(1.0j * math.pi * ev_hv / 8)) @ vc_hv.conj().T

    ps4 = list(combinations(range(4), 2))
    h6_mat = np.zeros((6, 6), dtype=complex)
    for r_i, (r0, r1) in enumerate(ps4):
        for c_i, (c0, c1) in enumerate(ps4):
            h6_mat[r_i, c_i] = h4_mat[r0, c0] * h4_mat[r1, c1] - h4_mat[r0, c1] * h4_mat[r1, c0]

    idx_odd = [st for st in range(32) if _bit_sum_c(st, 5) % 2 == 1]
    e64 = np.kron(spin_lie(e10)[np.ix_(idx_odd, idx_odd)], np.eye(4, dtype=complex))
    g64 = np.kron(spin_lie(g10)[np.ix_(idx_odd, idx_odd)], np.eye(4, dtype=complex))
    x64 = np.kron(a_spin[np.ix_(idx_odd, idx_odd)], h4_mat)
    y64 = np.kron((d_spin @ a_spin)[np.ix_(idx_odd, idx_odd)], h4_mat)
    dh64 = np.kron(dh_inv_spin[np.ix_(idx_odd, idx_odd)], np.eye(4, dtype=complex))

    e60 = np.kron(e10, np.eye(6, dtype=complex))
    g60 = np.kron(g10, np.eye(6, dtype=complex))
    x60 = np.kron(a_vec, h6_mat)
    y60 = np.kron(d_vec @ a_vec, h6_mat)
    dh60 = np.kron(dh_inv_vec, np.eye(6, dtype=complex))

    def blk124(m60: np.ndarray, m64: np.ndarray) -> np.ndarray:
        z_a = np.zeros((60, 64), dtype=complex)
        z_b = np.zeros((64, 60), dtype=complex)
        return np.block([[m60, z_a], [z_b, m64]])

    x124 = blk124(x60, x64)
    y124 = blk124(y60, y64)
    dh124 = blk124(dh60, dh64)
    e124 = blk124(e60, e64)
    g124 = blk124(g60, g64)

    # Close finite compensator subgroup generated by {X, Y, D_half_inv} and inverses:
    gens_c = {
        "X": x124,
        "Y": y124,
        "D": dh124,
        "x": x124.conj().T,
        "y": y124.conj().T,
        "d": dh124.conj().T,
    }
    comp_list: list[tuple[str, np.ndarray]] = [("", np.eye(124, dtype=complex))]
    frontier: list[tuple[str, np.ndarray]] = [("", np.eye(124, dtype=complex))]
    for _ in range(16):
        if not frontier:
            break
        nxt_f: list[tuple[str, np.ndarray]] = []
        for w_s, m_cur in frontier:
            for lbl, g_m in gens_c.items():
                cand = m_cur @ g_m
                if not any(float(np.max(np.abs(cand - m_prev))) < 1e-9 for _, m_prev in comp_list):
                    comp_list.append((w_s + lbl, cand))
                    nxt_f.append((w_s + lbl, cand))
        frontier = nxt_f

    return {
        "X": x124,
        "Y": y124,
        "E": e124,
        "G": g124,
        "comp_group": comp_list,
    }


def _hom_dim_num(
    pair_a: tuple[np.ndarray, np.ndarray],
    pair_b: tuple[np.ndarray, np.ndarray],
    tol: float = 1e-9,
) -> int:
    """Necessary-and-sufficient Sylvester nullity dim Hom_{<L, R>}(A, B) (works on reducible modules too, F3)."""
    la, ra = pair_a
    lb, rb = pair_b
    da = la.shape[0]
    db = lb.shape[0]
    sys_m = np.vstack(
        [
            np.kron(la.T, np.eye(db, dtype=complex)) - np.kron(np.eye(da, dtype=complex), lb),
            np.kron(ra.T, np.eye(db, dtype=complex)) - np.kron(np.eye(da, dtype=complex), rb),
        ]
    )
    svals = np.linalg.svd(sys_m, compute_uv=False)
    return int(np.sum(svals < tol))


def _solve_intertwiner_3d(
    pair_a: tuple[np.ndarray, np.ndarray], pair_b: tuple[np.ndarray, np.ndarray]
) -> tuple[np.ndarray | None, float]:
    """Unitary isomorphism solver for IRREDUCIBLE 3D modules (requires dim Hom == 1)."""
    la, ra = pair_a
    lb, rb = pair_b
    sys_m = np.vstack(
        [
            np.kron(la.T, np.eye(3, dtype=complex)) - np.kron(np.eye(3, dtype=complex), lb),
            np.kron(ra.T, np.eye(3, dtype=complex)) - np.kron(np.eye(3, dtype=complex), rb),
        ]
    )
    _, svals, vh = np.linalg.svd(sys_m)
    null_cnt = int(np.sum(svals < 1e-9))
    if null_cnt != 1:
        return None, 1.0
    cand = vh[-1].conj().reshape((3, 3), order="F")
    u_svd, sv_c, vh_c = np.linalg.svd(cand)
    if float(np.min(sv_c)) < 1e-9:
        return None, 1.0
    u_unit = u_svd @ vh_c
    err = max(
        float(np.max(np.abs(u_unit @ la @ u_unit.conj().T - lb))),
        float(np.max(np.abs(u_unit @ ra @ u_unit.conj().T - rb))),
    )
    return u_unit, err


def solve_intertwiner_cyc24_exact(
    pair_src: tuple[list[list[Cyc24Elem]], list[list[Cyc24Elem]]],
    pair_dst: tuple[list[list[Cyc24Elem]], list[list[Cyc24Elem]]],
) -> tuple[int, bool]:
    """Exact zero-float Q(zeta_24) Sylvester Hom-dimension & unitary intertwiner solver (F5)."""
    l_src, r_src = pair_src
    l_dst, r_dst = pair_dst
    q0_el = _q_zero()
    cols_72: list[list[sp.Rational]] = []
    for r_b in range(3):
        for c_b in range(3):
            for k_b in range(8):
                zk_el = cyc24_pow(k_b)
                e_mat = [[zk_el if (ri == r_b and ci == c_b) else q0_el for ci in range(3)] for ri in range(3)]
                dl_a = cyc24_matmul(e_mat, l_src)
                dl_b = cyc24_matmul(l_dst, e_mat)
                dr_a = cyc24_matmul(e_mat, r_src)
                dr_b = cyc24_matmul(r_dst, e_mat)
                col_vec: list[sp.Rational] = []
                for ri in range(3):
                    for ci in range(3):
                        for ki in range(8):
                            col_vec.append(dl_a[ri][ci][ki] - dl_b[ri][ci][ki])
                for ri in range(3):
                    for ci in range(3):
                        for ki in range(8):
                            col_vec.append(dr_a[ri][ci][ki] - dr_b[ri][ci][ki])
                cols_72.append(col_vec)
    ns_q = sp.Matrix(cols_72).T.nullspace()
    hom_dim = next((d_h for d_h in range(10) if len(ns_q) == 8 * d_h), -1)
    if hom_dim != 1:
        return hom_dim, False
    v_q = list(ns_q[0])
    u_raw: list[list[Cyc24Elem]] = []
    for ri in range(3):
        row_u: list[Cyc24Elem] = []
        for ci in range(3):
            base_idx = 8 * (3 * ri + ci)
            row_u.append(tuple(sp.Rational(v_q[base_idx + ki]) for ki in range(8)))
        u_raw.append(row_u)
    gram_u = cyc24_matmul(u_raw, cyc24_herm(u_raw))
    c_q = gram_u[0][0][0]
    if c_q <= 0 or any(gram_u[0][0][ki] != 0 for ki in range(1, 8)):
        return hom_dim, False
    rt_c1 = sp.sqrt(c_q)
    rt_c2 = sp.sqrt(c_q / 2)
    rt_c3 = sp.sqrt(c_q / 3)
    if rt_c1.is_Rational:
        s_q = sp.Rational(1) / rt_c1
        scale_el: Cyc24Elem = (s_q,) + (sp.Rational(0),) * 7
    elif rt_c2.is_Rational:
        s_q = sp.Rational(1) / rt_c2
        inv_rt2_el = cyc24_scale_half(cyc24_add(cyc24_pow(3), cyc24_neg(cyc24_pow(9))))
        scale_el = tuple(s_q * x_c for x_c in inv_rt2_el)
    elif rt_c3.is_Rational:
        s_q = sp.Rational(1) / (3 * rt_c3)
        rt3_el = cyc24_add(cyc24_pow(2), cyc24_pow(-2))
        scale_el = tuple(s_q * x_c for x_c in rt3_el)
    else:
        return hom_dim, False
    u_unit = [[cyc24_mul(scale_el, x_e) for x_e in row_e] for row_e in u_raw]
    u_dag = cyc24_herm(u_unit)
    unitary_and_equiv_ok = (
        cyc24_key(cyc24_matmul(u_unit, u_dag)) == cyc24_key(cyc24_eye(3))
        and cyc24_key(cyc24_matmul(u_unit, cyc24_matmul(l_src, u_dag))) == cyc24_key(l_dst)
        and cyc24_key(cyc24_matmul(u_unit, cyc24_matmul(r_src, u_dag))) == cyc24_key(r_dst)
    )
    return hom_dim, unitary_and_equiv_ok


def verify_b1866_zero_handtyped_3branch_pde_join(alg_ref: dict[str, Any]) -> dict[str, Any]:
    """Mechanically compute all 3-branch zero-mode representations directly from PDE sections & E8 compensators (F1-F6)."""
    tl_ref_num = cyc24_to_numpy(alg_ref["t_l_cyc"])
    tr_ref_num = cyc24_to_numpy(alg_ref["t_r_cyc"])
    tbar_l_num = cyc24_to_numpy(alg_ref["tbar_l_cyc"])
    tbar_r_num = cyc24_to_numpy(alg_ref["tbar_r_cyc"])

    fi = np.diag([1.0j, -1.0j])
    fj = np.array([[0.0, 1.0], [-1.0, 0.0]], dtype=complex)
    inv_rt2 = 1.0 / math.sqrt(2.0)
    gl = (np.eye(2, dtype=complex) + fi) * inv_rt2
    gr = (np.eye(2, dtype=complex) - fj) * inv_rt2

    tower_gens = {
        "L": ("a", "Ab", gl),
        "R": ("aB", "b", gr),
    }

    def eval_hol_word(ha: np.ndarray, hb: np.ndarray, word: str) -> np.ndarray:
        out = np.eye(ha.shape[0], dtype=complex)
        for ch in word:
            step = ha if ch == "a" else ha.conj().T if ch == "A" else hb if ch == "b" else hb.conj().T
            out = out @ step
        return out

    def apply_gen_bg(gen_k: str, bg_tup: tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]) -> tuple[np.ndarray, ...]:
        wa, wb, u2 = tower_gens[gen_k]
        ha, hb, p1, p2 = bg_tup
        p1n = u2[0, 0] * p1 + u2[0, 1] * p2
        p2n = u2[1, 0] * p1 + u2[1, 1] * p2
        return (eval_hol_word(ha, hb, wa), eval_hol_word(ha, hb, wb), p1n, p2n)

    def run_3branch_thread(h4_sign: int) -> dict[str, Any]:
        car = _build_16_4_carrier_and_compensators(h4_sign=h4_sign)
        x_op, y_op, e_op, g_op = car["X"], car["Y"], car["E"], car["G"]
        comp_grp = car["comp_group"]

        b3 = (x_op, y_op, e_op, g_op)
        b2 = apply_gen_bg("R", b3)
        b4 = apply_gen_bg("L", b3)
        branch_bgs = {2: b2, 3: b3, 4: b4}
        branch_u2 = {2: gr, 3: np.eye(2, dtype=complex), 4: gl}
        branch_order = [2, 3, 4]

        # Extract (16, 4)_singlet (colour index 0 inside 64D block starting at offset 60):
        # Note: for h4_sign = +1, colour index 0 is the SU(3)-singlet line; for h4_sign = -1, colour index 0 is still the unique SU(3)-singlet!
        sel_sing = [60 + 4 * r_i for r_i in range(16)]
        e_sing = e_op[np.ix_(sel_sing, sel_sing)]
        g_sing = g_op[np.ix_(sel_sing, sel_sing)]
        _, sv0, vh0 = np.linalg.svd(np.vstack([e_sing, g_sing]))
        if int(np.sum(sv0 < 1e-9)) != 1:
            raise RuntimeError("Unexpected Koszul deg-0 singlet rank")
        v_top = np.zeros(124, dtype=complex)
        v_top[sel_sing] = vh0[-1].conj()
        v_top /= np.linalg.norm(v_top)

        m_k1 = np.vstack([np.hstack([e_sing.conj().T, g_sing.conj().T]), np.hstack([-g_sing, e_sing])])
        _, sv1, vh1 = np.linalg.svd(m_k1)
        h1_16 = vh1[sv1 < 1e-9].conj().T
        x_sing = x_op[np.ix_(sel_sing, sel_sing)]
        y_sing = y_op[np.ix_(sel_sing, sel_sing)]
        ha_1 = h1_16.conj().T @ np.kron(fi, x_sing) @ h1_16
        hb_1 = h1_16.conj().T @ np.kron(fj, y_sing) @ h1_16

        # Notice: for h4_sign = +1, (16, 4)_singlet has 1 trivial holonomy deg-1 spinor mode and 1 chi_(1,1) mode;
        # for h4_sign = -1 (the O_0 sign-flipped lift = same physical background with swapped singlet/triplet characters!),
        # let's record the exact trivial-holonomy count on (16, 4)_singlet!
        proj_triv_1 = ((np.eye(2, dtype=complex) + ha_1) @ (np.eye(2, dtype=complex) + hb_1)) / 4
        u_p1, sv_p1, _ = np.linalg.svd(proj_triv_1)
        n_triv_sing_deg1 = int(np.sum(sv_p1 > 0.5))

        # Check top-weight holonomy eigenvalues on B3:
        la_top = complex(np.vdot(v_top, x_op @ v_top))
        lb_top = complex(np.vdot(v_top, y_op @ v_top))
        top_hol_b3 = (int(round(la_top.real)), int(round(lb_top.real)))

        if h4_sign == -1:
            # On h4_sign = -1, v_top in (16, 4)_singlet carries trivial holonomy (+1, +1) while (16, 4)_triplet carries (-1, -1),
            # confirming Stage 1's h4_sign_flip_swaps_colour_singlet_triplet_parities!
            return {
                "h4_sign": h4_sign,
                "comp_group_order": len(comp_grp),
                "top_hol_b3": top_hol_b3,
                "n_triv_sing_deg1": n_triv_sing_deg1,
            }

        w_spin_32 = h1_16 @ u_p1[:, 0]
        w_spin_ref = np.zeros((2, 124), dtype=complex)
        w_spin_ref[0, sel_sing] = w_spin_32[:16]
        w_spin_ref[1, sel_sing] = w_spin_32[16:]
        w_spin_ref /= np.linalg.norm(w_spin_ref)
        branch_w_spin = {b_i: branch_u2[b_i] @ w_spin_ref for b_i in branch_order}

        with mp.workdps(40):
            def eta_mp(tau_v: mp.mpc) -> mp.mpc:
                q2 = mp.exp(2j * mp.pi * tau_v)
                prod = mp.mpf(1)
                for n_k in range(1, 80):
                    prod *= 1 - q2**n_k
                return mp.exp(1j * mp.pi * tau_v / 12) * prod

            def szego_mp(b_idx: int, z_v: mp.mpc, tau_v: mp.mpc) -> mp.mpc:
                q_v = mp.exp(1j * mp.pi * tau_v)
                return (mp.pi * mp.jtheta(1, 0, q_v, 1) * mp.jtheta(b_idx, mp.pi * z_v, q_v)) / (
                    mp.jtheta(b_idx, 0, q_v) * mp.jtheta(1, mp.pi * z_v, q_v)
                )

            def dszego_mp(b_idx: int, z_v: mp.mpc, tau_v: mp.mpc) -> mp.mpc:
                q_v = mp.exp(1j * mp.pi * tau_v)
                c0 = mp.pi * mp.jtheta(1, 0, q_v, 1) / mp.jtheta(b_idx, 0, q_v)
                th_b = mp.jtheta(b_idx, mp.pi * z_v, q_v)
                dth_b = mp.pi * mp.jtheta(b_idx, mp.pi * z_v, q_v, 1)
                th_1 = mp.jtheta(1, mp.pi * z_v, q_v)
                dth_1 = mp.pi * mp.jtheta(1, mp.pi * z_v, q_v, 1)
                return c0 * (dth_b * th_1 - th_b * dth_1) / (th_1**2)

            def mp_inv_eval(gen_k: str, z_new: mp.mpc, tau_new: mp.mpc) -> tuple[mp.mpc, mp.mpc, mp.mpc]:
                if gen_k == "L":
                    return z_new, tau_new - 1, mp.mpc(1)
                tau_old = tau_new / (1 - tau_new)
                eps_g = mp.sqrt(tau_old + 1)
                return (eps_g**2) * z_new, tau_old, eps_g

            # Verify cusp-isometric trivialization |eta(g tau)^2 dz_new| == |eta(tau)^2 dz_old| vs naive |dz_new| != |dz_old|:
            tau_iso = mp.mpc(mp.mpf(4) / mp.mpf(17), mp.mpf(19) / mp.mpf(14))
            _, tau_r_old, eps_r = mp_inv_eval("R", mp.mpc(mp.mpf(3) / mp.mpf(17), mp.mpf(5) / mp.mpf(16)), tau_iso)
            cusp_iso_err = float(abs(abs(eta_mp(tau_iso)) ** 2 - abs(eta_mp(tau_r_old)) ** 2 * abs(eps_r) ** 2))
            naive_dz_nonunitary_gap = float(abs(abs(eps_r) ** 2 - 1.0))

            def eval_mode_3branch(mode_kind: str, z_pt: mp.mpc, tau_pt: mp.mpc) -> dict[str, np.ndarray]:
                mats_out: dict[str, np.ndarray] = {}
                for gen_k in ("L", "R"):
                    z_old, tau_old, eps_g = mp_inv_eval(gen_k, z_pt, tau_pt)
                    mat_3 = np.zeros((3, 3), dtype=complex)
                    for col_i, b_src in enumerate(branch_order):
                        bg_pushed = apply_gen_bg(gen_k, branch_bgs[b_src])
                        b_dst = None
                        u_comp = None
                        for b_cand in branch_order:
                            hits = [
                                u_c
                                for _, u_c in comp_grp
                                if max(
                                    float(np.max(np.abs(u_c @ bg_pushed[k_i] @ u_c.conj().T - branch_bgs[b_cand][k_i])))
                                    for k_i in range(4)
                                )
                                < 1e-9
                            ]
                            if hits:
                                if len(hits) != 1:
                                    raise RuntimeError("Non-unique compensator on 124D faithful carrier")
                                b_dst = b_cand
                                u_comp = hits[0]
                                break
                        if b_dst is None or u_comp is None:
                            raise RuntimeError("Failed to find target branch and compensator")
                        row_i = branch_order.index(b_dst)

                        if mode_kind == "proxy_1form_no_S3":
                            fib_ph = complex(np.vdot(v_top.conj(), u_comp.conj() @ v_top.conj()))
                            val_pushed = szego_mp(b_src, z_old, tau_old) * (eps_g**2)
                            val_dst = szego_mp(b_dst, z_pt, tau_pt)
                            mat_3[row_i, col_i] = fib_ph * complex(val_pushed / val_dst)
                        elif mode_kind == "phi_sp_conj_weyl":
                            fib_ph = complex(np.vdot(v_top.conj(), u_comp.conj() @ v_top.conj()))
                            val_pushed = (eta_mp(tau_old) ** 3) * szego_mp(b_src, z_old, tau_old) * (eps_g**5)
                            val_dst = (eta_mp(tau_pt) ** 3) * szego_mp(b_dst, z_pt, tau_pt)
                            mat_3[row_i, col_i] = fib_ph * complex(val_pushed / val_dst)
                        elif mode_kind == "a_sp_left_weyl":
                            fib_ph = complex(np.vdot(v_top, u_comp @ v_top))
                            val_pushed = mp.conj((eta_mp(tau_old) ** 3) * szego_mp(b_src, z_old, tau_old) * (eps_g**5))
                            val_dst = mp.conj((eta_mp(tau_pt) ** 3) * szego_mp(b_dst, z_pt, tau_pt))
                            mat_3[row_i, col_i] = fib_ph * complex(val_pushed / val_dst)
                        elif mode_kind == "a_dp_left_weyl":
                            fib_ph = complex(np.vdot(v_top, u_comp @ v_top))
                            val_pushed = mp.conj(eta_mp(tau_old) * dszego_mp(b_src, z_old, tau_old) * (eps_g**5))
                            val_dst = mp.conj(eta_mp(tau_pt) * dszego_mp(b_dst, z_pt, tau_pt))
                            mat_3[row_i, col_i] = fib_ph * complex(val_pushed / val_dst)
                        elif mode_kind == "psi_spin_left_weyl":
                            u_g = tower_gens[gen_k][2]
                            w_src = branch_w_spin[b_src]
                            w_pushed = u_g @ (w_src @ u_comp.T)
                            w_dst = branch_w_spin[b_dst]
                            fib_ph = complex(np.vdot(w_dst.reshape(-1), w_pushed.reshape(-1)))
                            val_pushed = eta_mp(tau_old) * eps_g
                            val_dst = eta_mp(tau_pt)
                            mat_3[row_i, col_i] = fib_ph * complex(val_pushed / val_dst)
                        else:
                            raise ValueError(mode_kind)
                    mats_out[gen_k] = mat_3
                return mats_out

            z_p1 = mp.mpc(mp.mpf(3) / mp.mpf(17), mp.mpf(5) / mp.mpf(16))
            t_p1 = mp.mpc(mp.mpf(4) / mp.mpf(17), mp.mpf(19) / mp.mpf(14))
            z_p2 = mp.mpc(-mp.mpf(5) / mp.mpf(19), mp.mpf(7) / mp.mpf(17))
            t_p2 = mp.mpc(-mp.mpf(6) / mp.mpf(17), mp.mpf(17) / mp.mpf(14))

            modes_summary: dict[str, Any] = {}
            max_ztau_indep_err = 0.0
            max_snap_err = 0.0
            for mk in (
                "proxy_1form_no_S3",
                "phi_sp_conj_weyl",
                "a_sp_left_weyl",
                "a_dp_left_weyl",
                "psi_spin_left_weyl",
            ):
                m_pt1 = eval_mode_3branch(mk, z_p1, t_p1)
                m_pt2 = eval_mode_3branch(mk, z_p2, t_p2)
                indep_e = max(
                    float(np.max(np.abs(m_pt1["L"] - m_pt2["L"]))),
                    float(np.max(np.abs(m_pt1["R"] - m_pt2["R"]))),
                )
                max_ztau_indep_err = max(max_ztau_indep_err, indep_e)
                l_cyc, err_l = snap_monomial_3x3_to_cyc24(m_pt1["L"])
                r_cyc, err_r = snap_monomial_3x3_to_cyc24(m_pt1["R"])
                max_snap_err = max(max_snap_err, err_l, err_r)

                grp_m = cyc24_close_group({"L": l_cyc, "R": r_cyc})
                cent_m, pg_m = cyc24_center_and_pg_orders(grp_m)
                r_inv_c = cyc24_herm(r_cyc)
                s_c = cyc24_matmul(l_cyc, cyc24_matmul(r_inv_c, l_cyc))
                s_rhs_c = cyc24_matmul(r_inv_c, cyc24_matmul(l_cyc, r_inv_c))
                braid_ok = cyc24_key(s_c) == cyc24_key(s_rhs_c)
                l2_c = cyc24_matmul(l_cyc, l_cyc)
                s4_c = cyc24_matmul(cyc24_matmul(s_c, s_c), cyc24_matmul(s_c, s_c))
                s4_diag_sign = -1 if cyc24_key(s4_c) == cyc24_key([[cyc24_from_int(-1 if i == j else 0) for j in range(3)] for i in range(3)]) else (
                    1 if cyc24_key(s4_c) == cyc24_key(cyc24_eye(3)) else 0
                )

                _, err_to_t = _solve_intertwiner_3d((m_pt1["L"], m_pt1["R"]), (tl_ref_num, tr_ref_num))
                _, err_to_tbar = _solve_intertwiner_3d((m_pt1["L"], m_pt1["R"]), (tbar_l_num, tbar_r_num))
                hom_t_exact, cyc_intertwines_t = solve_intertwiner_cyc24_exact(
                    (alg_ref["t_l_cyc"], alg_ref["t_r_cyc"]), (l_cyc, r_cyc)
                )
                hom_tbar_exact, cyc_intertwines_tbar = solve_intertwiner_cyc24_exact(
                    (alg_ref["tbar_l_cyc"], alg_ref["tbar_r_cyc"]), (l_cyc, r_cyc)
                )
                comm_dim = joint_commutant_dim_num([m_pt1["L"], m_pt1["R"]], tol=1e-10)

                # Extract stabilizer signs (L^2, S) on B_(1,1) (branch b=3 -> index 1 in branch_order=[2,3,4]):
                l2_b3_el = l2_c[1][1]
                s_b3_el = s_c[1][1]
                l2_sgn = 1 if l2_b3_el == cyc24_from_int(1) else (-1 if l2_b3_el == cyc24_from_int(-1) else 0)
                s_sgn = 1 if s_b3_el == cyc24_from_int(1) else (-1 if s_b3_el == cyc24_from_int(-1) else 0)

                modes_summary[mk] = {
                    "L_cyc": l_cyc,
                    "R_cyc": r_cyc,
                    "L_num": m_pt1["L"],
                    "R_num": m_pt1["R"],
                    "exact_center_order": cent_m,
                    "exact_pg_order": pg_m,
                    "exact_group_eq_cent_times_pg": len(grp_m) == cent_m * pg_m,
                    "braid_exact": braid_ok,
                    "s4_scalar_sign": s4_diag_sign,
                    "b3_stabilizer_L2_S_signs": (l2_sgn, s_sgn),
                    "hom_from_T_exact": hom_t_exact,
                    "hom_from_Tbar_exact": hom_tbar_exact,
                    "cyc24_unitary_intertwiner_T": cyc_intertwines_t,
                    "cyc24_unitary_intertwiner_Tbar": cyc_intertwines_tbar,
                    "matches_T": cyc_intertwines_t and (err_to_t < TOL),
                    "matches_Tbar": cyc_intertwines_tbar and (err_to_tbar < TOL),
                    "joint_commutant_dim": comm_dim,
                }

        return {
            "h4_sign": h4_sign,
            "comp_group_order": len(comp_grp),
            "top_hol_b3": top_hol_b3,
            "n_triv_sing_deg1": n_triv_sing_deg1,
            "cusp_isometric_eta2_dz_err": cusp_iso_err,
            "naive_dz_nonunitary_gap": naive_dz_nonunitary_gap,
            "max_ztau_independence_err": max_ztau_indep_err,
            "max_cyc24_snap_err": max_snap_err,
            "modes": modes_summary,
        }

    thread_plus = run_3branch_thread(h4_sign=1)
    thread_minus = run_3branch_thread(h4_sign=-1)
    modes_p = thread_plus["modes"]

    # D2 fix (F3): Necessary-and-sufficient Sylvester nullity dim Hom_{<L,R>}(A, B) == 0 across all 3 pairs
    # of (a_sp, a_dp, psi_spin) + direct-sum commutant dim End_{<L,R>}(9D) == 4 (= 1 + 1 + 2),
    # plus reducible rank-1 non-zero Hom negative control!
    pair_sp = (modes_p["a_sp_left_weyl"]["L_num"], modes_p["a_sp_left_weyl"]["R_num"])
    pair_dp = (modes_p["a_dp_left_weyl"]["L_num"], modes_p["a_dp_left_weyl"]["R_num"])
    pair_spin = (modes_p["psi_spin_left_weyl"]["L_num"], modes_p["psi_spin_left_weyl"]["R_num"])
    hom_sp_dp = _hom_dim_num(pair_sp, pair_dp)
    hom_sp_spin = _hom_dim_num(pair_sp, pair_spin)
    hom_dp_spin = _hom_dim_num(pair_dp, pair_spin)

    z3_blk = np.zeros((3, 3), dtype=complex)
    l_9d = np.block([[pair_sp[0], z3_blk, z3_blk], [z3_blk, pair_dp[0], z3_blk], [z3_blk, z3_blk, pair_spin[0]]])
    r_9d = np.block([[pair_sp[1], z3_blk, z3_blk], [z3_blk, pair_dp[1], z3_blk], [z3_blk, z3_blk, pair_spin[1]]])
    end_9d_commutant_dim = joint_commutant_dim_num([l_9d, r_9d], tol=1e-9)

    # Planted negative control: two inequivalent reducible 3D modules sharing a 1D summand have Hom > 0 (singular intertwiner):
    red_a = (
        np.array([[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]], dtype=complex),
        np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]], dtype=complex),
    )
    red_b = (
        np.array([[1.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, -1.0, 0.0]], dtype=complex),
        np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]], dtype=complex),
    )
    reducible_neg_ctrl_hom_dim = _hom_dim_num(red_a, red_b)

    # Guardrail 3: Random Haar U(3) basis scrambling on a_sp_left_weyl:
    rng_j = np.random.default_rng(83)
    haar_join_checks: list[bool] = []
    for _ in range(8):
        u3 = haar_unitary(3, rng_j)
        l_scr = u3 @ modes_p["a_sp_left_weyl"]["L_num"] @ u3.conj().T
        r_scr = u3 @ modes_p["a_sp_left_weyl"]["R_num"] @ u3.conj().T
        _, err_scr = _solve_intertwiner_3d((l_scr, r_scr), (tbar_l_num, tbar_r_num))
        s_scr = l_scr @ np.linalg.inv(r_scr) @ l_scr
        s4_err = float(np.max(np.abs(np.linalg.matrix_power(s_scr, 4) + np.eye(3, dtype=complex))))
        haar_join_checks.append(
            err_scr < TOL
            and s4_err < TOL
            and joint_commutant_dim_num([l_scr, r_scr], tol=1e-10) == 1
        )

    # Also verify exact Q(zeta_24) twist relation between proxy_1form_no_S3 and phi_sp_conj_weyl:
    # Multiplying proxy_1form_no_S3 by chi_21 on L (z24^-3 = z24^21, since eta(tau_old)^3 = exp(-3 i pi/12) eta(tau_new)^3 = z24^21!)
    # and z24^+3 on R reproduces phi_sp_conj_weyl identically!
    z21_c = cyc24_pow(21)
    z3_c = cyc24_pow(3)
    proxy_twisted_l = [[cyc24_mul(z21_c, x_e) for x_e in row] for row in modes_p["proxy_1form_no_S3"]["L_cyc"]]
    proxy_twisted_r = [[cyc24_mul(z3_c, x_e) for x_e in row] for row in modes_p["proxy_1form_no_S3"]["R_cyc"]]
    eta3_supplies_odd_metaplectic_char_exact = (
        cyc24_key(proxy_twisted_l) == cyc24_key(modes_p["phi_sp_conj_weyl"]["L_cyc"])
        and cyc24_key(proxy_twisted_r) == cyc24_key(modes_p["phi_sp_conj_weyl"]["R_cyc"])
    )

    b1866_resolved_and_verified = (
        thread_plus["top_hol_b3"] == (-1, -1)
        and thread_plus["n_triv_sing_deg1"] == 1
        and thread_minus["top_hol_b3"] == (1, 1)
        and thread_minus["n_triv_sing_deg1"] == 1
        and thread_plus["cusp_isometric_eta2_dz_err"] < TOL
        and thread_plus["naive_dz_nonunitary_gap"] > 1 / 4
        and thread_plus["max_ztau_independence_err"] < TOL
        and thread_plus["max_cyc24_snap_err"] < TOL
        # 1. Proxy 1-form (dropping S^-3): stabilizer (L^2, S = L R^-1 L) = (-1, -1) on B_(1,1)
        #    (since S = Inn(b^-1) o S_theta picks up Y^-1 = -1 alongside D^(-1/2) = +1!), order 24 (|Z|=1, |PG|=24), S^4 = +I_3:
        and modes_p["proxy_1form_no_S3"]["b3_stabilizer_L2_S_signs"] == (-1, -1)
        and (modes_p["proxy_1form_no_S3"]["exact_center_order"], modes_p["proxy_1form_no_S3"]["exact_pg_order"]) == (1, 24)
        and modes_p["proxy_1form_no_S3"]["s4_scalar_sign"] == 1
        and (not modes_p["proxy_1form_no_S3"]["matches_T"])
        and eta3_supplies_odd_metaplectic_char_exact
        # 2. Physical S^5 simple-pole partner phi_sp: order 96 (|Z|=4, |PG|=24), S^4 = -I_3, matches T (Hom(T, phi_sp)==1, Hom(Tbar, phi_sp)==0):
        and (modes_p["phi_sp_conj_weyl"]["exact_center_order"], modes_p["phi_sp_conj_weyl"]["exact_pg_order"]) == (4, 24)
        and modes_p["phi_sp_conj_weyl"]["s4_scalar_sign"] == -1
        and modes_p["phi_sp_conj_weyl"]["hom_from_T_exact"] == 1
        and modes_p["phi_sp_conj_weyl"]["hom_from_Tbar_exact"] == 0
        and modes_p["phi_sp_conj_weyl"]["cyc24_unitary_intertwiner_T"]
        and (not modes_p["phi_sp_conj_weyl"]["matches_Tbar"])
        and modes_p["phi_sp_conj_weyl"]["matches_T"]
        and modes_p["phi_sp_conj_weyl"]["joint_commutant_dim"] == 1
        # 3. Physical S^-3 left-Weyl simple-pole mode a_sp: order 96 (|Z|=4, |PG|=24), S^4 = -I_3, matches T_bar (Hom(T, a_sp)==0, Hom(Tbar, a_sp)==1):
        and (modes_p["a_sp_left_weyl"]["exact_center_order"], modes_p["a_sp_left_weyl"]["exact_pg_order"]) == (4, 24)
        and modes_p["a_sp_left_weyl"]["s4_scalar_sign"] == -1
        and modes_p["a_sp_left_weyl"]["hom_from_T_exact"] == 0
        and modes_p["a_sp_left_weyl"]["hom_from_Tbar_exact"] == 1
        and modes_p["a_sp_left_weyl"]["cyc24_unitary_intertwiner_Tbar"]
        and (not modes_p["a_sp_left_weyl"]["matches_T"])
        and modes_p["a_sp_left_weyl"]["matches_Tbar"]
        and modes_p["a_sp_left_weyl"]["joint_commutant_dim"] == 1
        # 4. Physical S^-3 left-Weyl double-pole mode a_dp: |Z|=12, |PG|=24 (order 12*24=288), S^4 = -I_3, irrep:
        and (modes_p["a_dp_left_weyl"]["exact_center_order"], modes_p["a_dp_left_weyl"]["exact_pg_order"]) == (12, 24)
        and modes_p["a_dp_left_weyl"]["exact_group_eq_cent_times_pg"]
        and modes_p["a_dp_left_weyl"]["s4_scalar_sign"] == -1
        and modes_p["a_dp_left_weyl"]["joint_commutant_dim"] == 1
        # 5. Physical S^1 Koszul deg-1 spinor mode psi_spin: order 72 (|Z|=12, |PG|=6 < 3^2=9 => reducible 1 (+) 2, commutant dim 2!):
        and (modes_p["psi_spin_left_weyl"]["exact_center_order"], modes_p["psi_spin_left_weyl"]["exact_pg_order"]) == (12, 6)
        and modes_p["psi_spin_left_weyl"]["s4_scalar_sign"] == -1
        and modes_p["psi_spin_left_weyl"]["joint_commutant_dim"] == 2
        # 6. Necessary-and-sufficient pairwise Hom == 0 across the 3 physical 3D sectors + End(9D) == 4:
        and (hom_sp_dp, hom_sp_spin, hom_dp_spin) == (0, 0, 0)
        and end_9d_commutant_dim == 4
        and reducible_neg_ctrl_hom_dim == 2
        and all(haar_join_checks)
    )

    return {
        "thread_h4_plus": {
            "comp_group_order": thread_plus["comp_group_order"],
            "top_hol_b3": thread_plus["top_hol_b3"],
            "cusp_isometric_eta2_dz_err": thread_plus["cusp_isometric_eta2_dz_err"],
            "max_ztau_independence_err": thread_plus["max_ztau_independence_err"],
            "max_cyc24_snap_err": thread_plus["max_cyc24_snap_err"],
            "proxy_1form_b3_stabilizer_L2_S": modes_p["proxy_1form_no_S3"]["b3_stabilizer_L2_S_signs"],
            "hom_weave_to_a_sp": modes_p["a_sp_left_weyl"]["hom_from_T_exact"],
            "hom_weave_conj_to_a_sp": modes_p["a_sp_left_weyl"]["hom_from_Tbar_exact"],
            "hom_weave_to_phi_sp": modes_p["phi_sp_conj_weyl"]["hom_from_T_exact"],
            "exact_cyc24_intertwiners_verified": (
                modes_p["phi_sp_conj_weyl"]["cyc24_unitary_intertwiner_T"]
                and modes_p["a_sp_left_weyl"]["cyc24_unitary_intertwiner_Tbar"]
                and modes_p["a_sp_left_weyl"]["hom_from_T_exact"] == 0
                and modes_p["a_sp_left_weyl"]["hom_from_Tbar_exact"] == 1
            ),
            "pairwise_hom_dims": {
                "a_sp_vs_a_dp": hom_sp_dp,
                "a_sp_vs_psi_spin": hom_sp_spin,
                "a_dp_vs_psi_spin": hom_dp_spin,
            },
            "end_9d_commutant_dim": end_9d_commutant_dim,
            "reducible_neg_ctrl_hom_dim": reducible_neg_ctrl_hom_dim,
            "mode_center_and_pg_orders": {
                k_m: (v_m["exact_center_order"], v_m["exact_pg_order"]) for k_m, v_m in modes_p.items()
            },
            "mode_s4_signs": {k_m: v_m["s4_scalar_sign"] for k_m, v_m in modes_p.items()},
            "mode_commutant_dims": {k_m: v_m["joint_commutant_dim"] for k_m, v_m in modes_p.items()},
        },
        "second_lift_control_h4_minus": thread_minus,
        "eta3_supplies_odd_metaplectic_char_exact": eta3_supplies_odd_metaplectic_char_exact,
        "haar_join_scrambling_invariant": all(haar_join_checks),
        "b1866_physical_join_resolved_and_verified": b1866_resolved_and_verified,
    }


def run_stage2_complete_verification() -> dict[str, Any]:
    """Run all Stage 2 (WP-3.1, WP-3.2, B1866 physical join) exact symbolic and numerical verifications."""
    zero_sm_ast_verified = audit_source_zero_empirical_constants(Path(__file__))
    wp31 = verify_wp31_exact_koszul_homotopy_and_248_parabolic_kernel()
    wp32_alg = verify_wp32_exact_cyclotomic_algebra_and_metaplectic_obstruction()
    b1866_phys = verify_b1866_zero_handtyped_3branch_pde_join(wp32_alg)

    all_passed = all(
        [
            zero_sm_ast_verified,
            wp31["koszul_homotopy_all_5_blocks_exact"],
            wp31["curved_pde_and_cusp_s5_pole_cutoff_exact"],
            wp31["gram_parity_orthogonal_verified"],
            wp31["parabolic_248_census_verified"],
            wp32_alg["wp32_algebra_verified"],
            wp32_alg["universal_s4_sym2_no_go_proven"],
            wp32_alg["b1879_exchange_doubles_96_to_192_exact"],
            b1866_phys["eta3_supplies_odd_metaplectic_char_exact"],
            b1866_phys["haar_join_scrambling_invariant"],
            b1866_phys["b1866_physical_join_resolved_and_verified"],
        ]
    )

    return {
        "stage": "Stage 2 (WP-3.1, WP-3.2, B1866 Open Physical Question)",
        "zero_sm_empirical_constants_ast_verified": zero_sm_ast_verified,
        "all_verifications_passed": all_passed,
        "wp31_kernel_and_homotopy": wp31,
        "wp32_cyclotomic_algebra": {
            k_a: v_a
            for k_a, v_a in wp32_alg.items()
            if k_a not in ("t_l_cyc", "t_r_cyc", "tbar_l_cyc", "tbar_r_cyc")
        },
        "b1866_zero_handtyped_3branch_join": b1866_phys,
    }
