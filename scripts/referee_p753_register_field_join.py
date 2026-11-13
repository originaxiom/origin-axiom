#!/usr/bin/env python3
r"""Independent Zero-Trust Referee Countercheck for P-753 / R77-2 (WP-2.2 & WP-3.2).

Guardrail 6 & F1-F6 enforcement:
- Zero imports from src/origin_axiom/*.
- Independently constructs:
  (1) All 240 explicit E8 root vectors in exact rational Fraction^8 + 8 Cartan generators to prove
      the exact E8 coroot identity (1,1,1,1,1,1,1,1) in Q^v(E8) => -h4 == zeta_Spin(10) * (+h4)
      across all 248 dims.
  (2) Explicit 5-fold Pauli Clifford algebra Cl(10) (32x32) and Spin(10) Pin/Spin lifts under
      adversarial Haar unitary basis rotations + standalone exact Q(zeta_24) = Q[z]/(z^8 - z^4 + 1)
      cyclotomic group closures to prove |2O| = 48, |St| = 16 ([2O : St] = 3), all E_theta
      compensators (< 1e-12), and the Klein-4 spectrum (112; 37, 33, 33, 33).
  (3) Adversarial Haar-scrambled quaternion F2 1-cocycle + independent q-series leading-power
      & Cauchy contour quadrature of V(tau) = (theta_2^2, theta_3^2, theta_4^2) / eta^3 + standalone
      exact Q(zeta_24) group closures proving |Weil_2| = 96, |Sym^2(Weil_2)| = 48, even Z_24 twist
      orders [24, 48, 72, 144] (excluding 96), and odd m = 3, 15 order 96.
  (4) Independent Cauchy contour Laurent quadrature around |z| = eps on E_tau \ {0} constructing
      the full 2x2 physical S^{-3} half-form representation matrices of BOTH generators (L^2, S_theta)
      of E_theta (including 64D E_8 gauge compensators, never zero-initializing off-diagonal blocks!)
      on BOTH 128's chi_(1,1) {a_sp, a_dp} and chi_(0,0) {a_hol, a_wp} 2-mode a-slots, proving
      off-diagonal shear < 1e-12, joint_commutant_dim == 2, and distinct L^2 eigenvalues (1 + 1),
      versus irreducible (2) (joint_commutant_dim == 1) on (10,6)'s (S_2, S_4) doublet.
  (5) Exact rational Fraction^8 E8 Z_4 global kernel proof ((Spin(10) x Spin(6)) / Z_4, order 4),
      disconnected so(5) holonomy comparison (dim 10 vs u(3) dim 9), and Cauchy-contour + exact
      Q(zeta_24) 3-branch half-form coset transport (zero hand-typed 3x3 matrices) proving proxy
      order 24 vs physical S^5/S^{-3}/S^1 orders (96, 96, 288, 72) + SHA256 pins.

Strictly data-free (0 of 19). Writes tracked receipts to relays/p753_verification/.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
import hashlib
from itertools import combinations, product
import json
import math
from pathlib import Path
import platform
import sys
from typing import Any

import mpmath as mp
import numpy as np


TOL = 1e-12

Cyc24Elem = tuple[Fraction, Fraction, Fraction, Fraction, Fraction, Fraction, Fraction, Fraction]
Cyc24Mat = tuple[tuple[Cyc24Elem, ...], ...]

_CYC24_ZERO: Cyc24Elem = (
    Fraction(0),
    Fraction(0),
    Fraction(0),
    Fraction(0),
    Fraction(0),
    Fraction(0),
    Fraction(0),
    Fraction(0),
)


def _cyc24_int(n: int) -> Cyc24Elem:
    return (
        Fraction(n),
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(0),
    )


def _cyc24_frac(p: int, q: int = 1) -> Cyc24Elem:
    return (
        Fraction(p, q),
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(0),
    )


def _cyc24_add(a: Cyc24Elem, b: Cyc24Elem) -> Cyc24Elem:
    return (
        a[0] + b[0],
        a[1] + b[1],
        a[2] + b[2],
        a[3] + b[3],
        a[4] + b[4],
        a[5] + b[5],
        a[6] + b[6],
        a[7] + b[7],
    )


def _cyc24_neg(a: Cyc24Elem) -> Cyc24Elem:
    return (-a[0], -a[1], -a[2], -a[3], -a[4], -a[5], -a[6], -a[7])


def _cyc24_mul(a: Cyc24Elem, b: Cyc24Elem) -> Cyc24Elem:
    # Modulo Phi_24(z) = z^8 - z^4 + 1 => z^8 = z^4 - 1
    buf = [Fraction(0) for _ in range(15)]
    for i in range(8):
        ai = a[i]
        if ai != 0:
            for j in range(8):
                bj = b[j]
                if bj != 0:
                    buf[i + j] += ai * bj
    for deg in range(14, 7, -1):
        c = buf[deg]
        if c != 0:
            buf[deg - 4] += c
            buf[deg - 8] -= c
    return (buf[0], buf[1], buf[2], buf[3], buf[4], buf[5], buf[6], buf[7])


def _cyc24_pow_zeta(k: int) -> Cyc24Elem:
    m = k % 24
    base: Cyc24Elem = (
        Fraction(0),
        Fraction(1),
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(0),
    )
    acc = _cyc24_int(1)
    for _ in range(m):
        acc = _cyc24_mul(acc, base)
    return acc


def _cyc24_conj(a: Cyc24Elem) -> Cyc24Elem:
    acc = _CYC24_ZERO
    for idx in range(8):
        if a[idx] != 0:
            acc = _cyc24_add(acc, _cyc24_mul(_cyc24_frac(a[idx].numerator, a[idx].denominator), _cyc24_pow_zeta(-idx)))
    return acc


def _cyc24_sqrt2_inv() -> Cyc24Elem:
    # zeta_24^3 + zeta_24^{-3} = exp(i pi/4) + exp(-i pi/4) = sqrt(2) => 1/sqrt(2) = (zeta^3 + zeta^{-3})/2
    s2 = _cyc24_add(_cyc24_pow_zeta(3), _cyc24_pow_zeta(-3))
    return _cyc24_mul(_cyc24_frac(1, 2), s2)


def _cyc24_to_complex(a: Cyc24Elem) -> complex:
    tot = 0.0 + 0.0j
    for idx in range(8):
        if a[idx] != 0:
            ang = math.pi * idx / 12
            tot += float(a[idx]) * complex(math.cos(ang), math.sin(ang))
    return tot


def _cyc24_eye(dim: int) -> Cyc24Mat:
    one = _cyc24_int(1)
    return tuple(tuple(one if r == c else _CYC24_ZERO for c in range(dim)) for r in range(dim))


def _cyc24_matmul(a: Cyc24Mat, b: Cyc24Mat) -> Cyc24Mat:
    d_r = len(a)
    d_m = len(b)
    d_c = len(b[0])
    rows = []
    for r in range(d_r):
        row = []
        for c in range(d_c):
            acc = _CYC24_ZERO
            for k in range(d_m):
                if a[r][k] != _CYC24_ZERO and b[k][c] != _CYC24_ZERO:
                    acc = _cyc24_add(acc, _cyc24_mul(a[r][k], b[k][c]))
            row.append(acc)
        rows.append(tuple(row))
    return tuple(rows)


def _cyc24_mat_dag(a: Cyc24Mat) -> Cyc24Mat:
    d_r = len(a)
    d_c = len(a[0])
    return tuple(tuple(_cyc24_conj(a[r][c]) for r in range(d_r)) for c in range(d_c))


def _cyc24_mat_scale(sc: Cyc24Elem, a: Cyc24Mat) -> Cyc24Mat:
    return tuple(tuple(_cyc24_mul(sc, x) for x in row) for row in a)


def _bfs_group_cyc24(gens: dict[str, Cyc24Mat], cap_steps: int = 16) -> dict[Cyc24Mat, str]:
    dim = len(next(iter(gens.values())))
    id_m = _cyc24_eye(dim)
    seen: dict[Cyc24Mat, str] = {id_m: ""}
    frontier: list[tuple[str, Cyc24Mat]] = [("", id_m)]
    max_sz = 2 ** (cap_steps - 4)
    while frontier:
        w, cur = frontier.pop(0)
        for lbl, g_m in gens.items():
            nxt = _cyc24_matmul(cur, g_m)
            if nxt not in seen:
                seen[nxt] = w + lbl
                frontier.append((w + lbl, nxt))
                if len(seen) > max_sz:
                    raise RuntimeError("Exact cyclotomic group exceeded bound")
    return seen


# Lookup table of exact unit-circle/sqrt(2) elements in Q(zeta_24) for verified exact snapping (< 1e-12):
_CYC24_ATOMS: list[tuple[complex, Cyc24Elem]] = [(_cyc24_to_complex(_CYC24_ZERO), _CYC24_ZERO)] + [
    (_cyc24_to_complex(el_v), el_v)
    for _k_z in range(24)
    for el_v in (_cyc24_pow_zeta(_k_z), _cyc24_mul(_cyc24_sqrt2_inv(), _cyc24_pow_zeta(_k_z)))
]


def _solve_intertwiner_cyc24_fraction(
    pair_src: tuple[Cyc24Mat, Cyc24Mat],
    pair_dst: tuple[Cyc24Mat, Cyc24Mat],
) -> tuple[int, bool]:
    """Exact Q(zeta_24) Fraction RREF solver for U L_src - L_dst U = 0, U R_src - R_dst U = 0 (zero floats)."""
    l_src, r_src = pair_src
    l_dst, r_dst = pair_dst
    z_pows = [_cyc24_pow_zeta(b_k) for b_k in range(8)]
    rows_q = [[Fraction(0) for _ in range(72)] for _ in range(144)]
    for r_i in range(3):
        for c_i in range(3):
            for b_k in range(8):
                col_idx = 24 * r_i + 8 * c_i + b_k
                zb = z_pows[b_k]
                e_mat: Cyc24Mat = tuple(
                    tuple(zb if (rr == r_i and cc == c_i) else _CYC24_ZERO for cc in range(3))
                    for rr in range(3)
                )
                dl_m = _cyc24_matmul(e_mat, l_src)
                dl_r = _cyc24_matmul(l_dst, e_mat)
                dr_m = _cyc24_matmul(e_mat, r_src)
                dr_r = _cyc24_matmul(r_dst, e_mat)
                for p_i in range(3):
                    for q_i in range(3):
                        base_l = 8 * (3 * p_i + q_i)
                        base_r = 72 + base_l
                        el_l = _cyc24_add(dl_m[p_i][q_i], _cyc24_neg(dl_r[p_i][q_i]))
                        el_r = _cyc24_add(dr_m[p_i][q_i], _cyc24_neg(dr_r[p_i][q_i]))
                        for idx_b in range(8):
                            rows_q[base_l + idx_b][col_idx] = el_l[idx_b]
                            rows_q[base_r + idx_b][col_idx] = el_r[idx_b]

    piv_cnt = 0
    is_piv = [False for _ in range(72)]
    piv_col_at = [-1 for _ in range(72)]
    for col_j in range(72):
        piv_r = -1
        for r_scan in range(piv_cnt, 144):
            if rows_q[r_scan][col_j] != 0:
                piv_r = r_scan
                break
        if piv_r < 0:
            continue
        cur_p = piv_cnt
        if piv_r != cur_p:
            rows_q[cur_p], rows_q[piv_r] = rows_q[piv_r], rows_q[cur_p]
        pv = rows_q[cur_p][col_j]
        rows_q[cur_p] = [x_v / pv for x_v in rows_q[cur_p]]
        for r_elim in range(144):
            if r_elim != cur_p and rows_q[r_elim][col_j] != 0:
                fac = rows_q[r_elim][col_j]
                rows_q[r_elim] = [rows_q[r_elim][k_c] - fac * rows_q[cur_p][k_c] for k_c in range(72)]
        is_piv[col_j] = True
        piv_col_at[cur_p] = col_j
        piv_cnt = piv_cnt + 1

    hom_dim = next((d_h for d_h in range(10) if piv_cnt == 72 - 8 * d_h), -1)
    if hom_dim < 0:
        raise RuntimeError("Expected Q-rank congruent to 0 mod 8")
    if hom_dim != 1:
        return hom_dim, False

    free_col = next(c_j for c_j in range(72) if not is_piv[c_j])
    vec_q = [Fraction(0) for _ in range(72)]
    vec_q[free_col] = Fraction(1)
    for p_idx in range(piv_cnt):
        p_col = piv_col_at[p_idx]
        vec_q[p_col] = -rows_q[p_idx][free_col]

    u_raw: Cyc24Mat = tuple(
        tuple(
            tuple(vec_q[24 * r_i + 8 * c_i + b_k] for b_k in range(8))
            for c_i in range(3)
        )
        for r_i in range(3)
    )
    uu_dag = _cyc24_matmul(u_raw, _cyc24_mat_dag(u_raw))
    c_q = uu_dag[0][0][0]
    if any(uu_dag[0][0][b_k] != 0 for b_k in range(1, 8)) or c_q <= 0:
        return hom_dim, False

    def is_rat_sq(fr: Fraction) -> Fraction | None:
        sn = math.isqrt(fr.numerator)
        sd = math.isqrt(fr.denominator)
        if sn * sn == fr.numerator and sd * sd == fr.denominator:
            return Fraction(sn, sd)
        return None

    r1 = is_rat_sq(c_q)
    r2 = is_rat_sq(c_q / 2)
    r3 = is_rat_sq(c_q / 3)
    if r1 is not None:
        scale_el = _cyc24_frac(r1.denominator, r1.numerator)
    elif r2 is not None:
        scale_el = _cyc24_mul(_cyc24_frac(r2.denominator, r2.numerator), _cyc24_sqrt2_inv())
    elif r3 is not None:
        rt3_el = _cyc24_add(_cyc24_pow_zeta(2), _cyc24_pow_zeta(-2))
        scale_el = _cyc24_mul(_cyc24_frac(r3.denominator, 3 * r3.numerator), rt3_el)
    else:
        return hom_dim, False

    u_unit = _cyc24_mat_scale(scale_el, u_raw)
    u_dag = _cyc24_mat_dag(u_unit)
    equiv_ok = (
        _cyc24_matmul(u_unit, u_dag) == _cyc24_eye(3)
        and _cyc24_matmul(_cyc24_matmul(u_unit, l_src), u_dag) == l_dst
        and _cyc24_matmul(_cyc24_matmul(u_unit, r_src), u_dag) == r_dst
    )
    return hom_dim, equiv_ok


def _snap_mat_to_cyc24(mat: np.ndarray) -> tuple[Cyc24Mat, float]:
    max_err = 0.0
    rows = []
    for r in range(mat.shape[0]):
        row = []
        for c in range(mat.shape[1]):
            val = complex(mat[r, c])
            best_c, best_el = min(_CYC24_ATOMS, key=lambda pr: abs(val - pr[0]))
            err = abs(val - best_c)
            if err > 1e-9:
                raise RuntimeError(f"Matrix entry {val} does not lie in Q(zeta_24) atom table (err={err})")
            max_err = max(max_err, err)
            row.append(best_el)
        rows.append(tuple(row))
    return tuple(rows), max_err


def _mat_sig(mat: np.ndarray, digits: int = 6) -> bytes:
    arr = np.asarray(mat, dtype=complex)
    return (np.round(arr.real, digits) + 0.0).tobytes() + (np.round(arr.imag, digits) + 0.0).tobytes()


def _bfs_group(gens: dict[str, np.ndarray]) -> list[tuple[str, np.ndarray]]:
    dim = next(iter(gens.values())).shape[0]
    eye = np.eye(dim, dtype=complex)
    seen: dict[bytes, tuple[str, np.ndarray]] = {_mat_sig(eye): ("", eye)}
    q: list[tuple[str, np.ndarray]] = [("", eye)]
    bound = 64 * dim * dim
    while q:
        w, cur = q.pop(0)
        for lbl, g in gens.items():
            nxt = cur @ g
            s = _mat_sig(nxt)
            if s not in seen:
                seen[s] = (w + lbl, nxt)
                q.append((w + lbl, nxt))
                if len(seen) > bound:
                    raise RuntimeError("Group order exceeded bound")
    return list(seen.values())


def _joint_commutant_dim(mats: list[np.ndarray]) -> int:
    dim = mats[0].shape[0]
    id_d = np.eye(dim, dtype=complex)
    stk = np.vstack([np.kron(id_d, m) - np.kron(m.T, id_d) for m in mats])
    svals = np.linalg.svd(stk, compute_uv=False)
    return int(np.sum(svals < 1e-9))


def _haar(dim: int, rng: np.random.Generator) -> np.ndarray:
    z = (rng.normal(size=(dim, dim)) + 1j * rng.normal(size=(dim, dim))) / math.sqrt(2.0)
    q, r = np.linalg.qr(z)
    d = np.diag(r)
    ph = np.where(np.abs(d) > 0.0, d / np.abs(d), 1.0 + 0.0j)
    return q * ph


# ---------------------------------------------------------------------------
# Check 1: Explicit E8 Root Lattice in Exact Rational Fraction^8 (240 + 8 = 248)
# ---------------------------------------------------------------------------
def check_e8_root_lattice_coroot_identity() -> dict[str, Any]:
    int_roots = [
        (
            i,
            j,
            tuple(Fraction(si if k_r == i else (sj if k_r == j else 0)) for k_r in range(8)),
        )
        for i, j in combinations(range(8), 2)
        for si, sj in product((-1, 1), repeat=2)
    ]
    roots_d5_adj = [vt for _, j, vt in int_roots if j < 5]
    roots_d3_adj = [vt for i, _, vt in int_roots if i >= 5]
    roots_10_6 = [vt for i, j, vt in int_roots if i < 5 <= j]
    spin_even = [signs for signs in product((-1, 1), repeat=8) if signs.count(-1) % 2 == 0]
    roots_16_4 = [tuple(Fraction(s_i, 2) for s_i in signs) for signs in spin_even if signs[:5].count(-1) % 2 == 1]
    roots_bar16_bar4 = [tuple(Fraction(s_i, 2) for s_i in signs) for signs in spin_even if signs[:5].count(-1) % 2 == 0]

    delta_d3 = (Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(1), Fraction(1), Fraction(1))
    delta_d5 = (Fraction(1), Fraction(1), Fraction(1), Fraction(1), Fraction(1), Fraction(0), Fraction(0), Fraction(0))

    all_roots = roots_d5_adj + roots_d3_adj + roots_10_6 + roots_16_4 + roots_bar16_bar4
    n_roots = len(all_roots)
    total_dim = n_roots + len(delta_d3)

    norms_exact_2 = all(sum(c * c for c in r) == Fraction(2) for r in all_roots)
    inner_prods_integral = all(
        sum(r1[k] * r2[k] for k in range(8)).denominator == 1
        for r1 in all_roots[:16]
        for r2 in all_roots
    )

    max_phase_diff = 0.0
    coroot_diff_nonint = 0
    integer_root_flips = 0
    spinor_root_flips = 0
    for r in all_roots:
        dot_d3 = sum(r[k] * delta_d3[k] for k in range(8))
        dot_d5 = sum(r[k] * delta_d5[k] for k in range(8))
        if (dot_d3 - dot_d5).denominator != 1:
            coroot_diff_nonint += 1
        ph_d3 = np.exp(2j * math.pi * float(dot_d3))
        ph_d5 = np.exp(2j * math.pi * float(dot_d5))
        max_phase_diff = max(max_phase_diff, abs(ph_d3 - ph_d5))
        if r[0].denominator == 1:
            if (dot_d3 % 1) != 0:
                integer_root_flips += 1
        else:
            if (dot_d3 - Fraction(1, 2)).denominator == 1:
                spinor_root_flips += 1

    theta_plus_h4 = (
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(-1, 4),
        Fraction(-1, 4),
        Fraction(-1, 4),
    )
    theta_minus_h4 = tuple(theta_plus_h4[k] + delta_d3[k] for k in range(8))
    w_sing = (Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(-1, 2), Fraction(-1, 2), Fraction(-1, 2))
    w_trip = (Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(-1, 2), Fraction(1, 2), Fraction(1, 2))
    ratios = set()
    for theta in (theta_plus_h4, theta_minus_h4):
        lam_s = np.exp(2j * math.pi * float(sum(w_sing[k] * theta[k] for k in range(8))))
        lam_t = np.exp(2j * math.pi * float(sum(w_trip[k] * theta[k] for k in range(8))))
        ratios.add(round(float((lam_s / lam_t).real), 9))

    d3_plus_minus: Counter[int] = Counter()
    for r in roots_d3_adj:
        val = int(round(float(np.exp(2j * math.pi * float(sum(r[k] * theta_plus_h4[k] for k in range(8)))).real)))
        d3_plus_minus[val] += 1
    d3_plus_minus[1] += 3

    return {
        "n_roots": n_roots,
        "total_e8_dim": total_dim,
        "branching_dims": {
            "(45,1)": len(roots_d5_adj) + 5,
            "(1,15)": len(roots_d3_adj) + 3,
            "(10,6)": len(roots_10_6),
            "(16,4)": len(roots_16_4),
            "(bar16,bar4)": len(roots_bar16_bar4),
        },
        "all_roots_norm_sq_2": norms_exact_2 and inner_prods_integral and (coroot_diff_nonint == 0),
        "coroot_phase_equivalence_max_err": float(max_phase_diff),
        "integer_root_flips": integer_root_flips,
        "spinor_root_flips": spinor_root_flips,
        "singlet_over_triplet_h4_ratio_set": sorted(ratios),
        "a3_adjoint_15_parity_split": {str(k): v for k, v in d3_plus_minus.items()},
    }


# ---------------------------------------------------------------------------
# Check 2: Independent Pauli-Clifford Cl(10) Construction & Exact Q(zeta_24) 2O/St
# ---------------------------------------------------------------------------
def check_pauli_clifford_spin10_and_e_theta(seed: int = 29) -> dict[str, Any]:
    rng = np.random.default_rng(seed)
    sx = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    sy = np.array([[0.0, -1j], [1j, 0.0]], dtype=complex)
    sz = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
    i2 = np.eye(2, dtype=complex)

    def kron5(ops: list[np.ndarray]) -> np.ndarray:
        out = ops[0]
        for op in ops[1:]:
            out = np.kron(out, op)
        return out

    gammas_eucl: list[np.ndarray] = []
    for k in range(5):
        pref = [sz] * k
        suff = [i2] * (4 - k)
        gammas_eucl.append(kron5(pref + [sx] + suff))
        gammas_eucl.append(kron5(pref + [sy] + suff))

    chirality = kron5([sz] * 5)
    psis = [(gammas_eucl[2 * k] + 1j * gammas_eucl[2 * k + 1]) / 2.0 for k in range(5)]
    psidags = [p.conj().T for p in psis]

    e5 = np.zeros((5, 5), dtype=complex)
    for j, c in enumerate([2.0, math.sqrt(6), math.sqrt(6), 2.0]):
        e5[j + 1, j] = c
    h5 = np.diag([-4, -2, 0, 2, 4]).astype(complex)
    j5 = np.diag([1.0, -1.0, 1.0, -1.0, 1.0])[:, ::-1].astype(complex)
    bz = np.zeros((5, 5), dtype=complex)
    bz[1, 4] = math.sqrt(2 / 5)
    bz[4, 1] = -bz[1, 4]
    bz[2, 3] = -math.sqrt(3 / 5)
    bz[3, 2] = -bz[2, 3]
    z5 = np.zeros((5, 5), dtype=complex)

    e10 = np.block([[e5, z5], [z5, -e5.T]])
    g10 = math.sqrt(10) * np.block([[z5, bz], [j5 @ bz @ j5, z5]])
    h10 = np.block([[h5, z5], [z5, -h5.T]])
    n10 = np.block([[np.eye(5), z5], [z5, -np.eye(5)]]).astype(complex)
    ep10, em10 = (e10 + g10) / 2.0, (e10 - g10) / 2.0
    hp10 = ep10 @ ep10.conj().T - ep10.conj().T @ ep10
    hm10 = em10 @ em10.conj().T - em10.conj().T @ em10

    def cliff_lie(m10: np.ndarray) -> np.ndarray:
        out = -0.5 * np.trace(m10[:5, :5]) * np.eye(32, dtype=complex)
        for a in range(5):
            for b in range(5):
                out += m10[a, b] * (psis[a] @ psidags[b])
                out += 0.5 * m10[a, b + 5] * (psis[a] @ psis[b])
                out += 0.5 * m10[a + 5, b] * (psidags[a] @ psidags[b])
        return out

    a_vec = -1j * n10 @ np.diag(np.exp(-1j * math.pi * np.diag(h10) / 4))
    psi_vec = psis + psidags
    rows = []
    for m_idx in range(10):
        target_op = sum(a_vec[n_idx, m_idx] * psi_vec[n_idx] for n_idx in range(10))
        rows.append(np.kron(psi_vec[m_idx].T, np.eye(32)) - np.kron(np.eye(32), target_op))
    _, svals_a, vh_a = np.linalg.svd(np.vstack(rows), full_matrices=False)
    if float(svals_a[-1]) > 1e-10:
        raise RuntimeError("Failed to find Clifford Spin(10) lift of A_vec")
    raw_a = vh_a[-1].conj().reshape((32, 32), order="F")
    ua_pol, _, vha_pol = np.linalg.svd(raw_a)
    a_spin_raw = ua_pol @ vha_pol
    top_phase_target = np.exp(1j * math.pi * sum([1, 0, -1, -2, -3]) / 4)
    a_spin = a_spin_raw * (top_phase_target / a_spin_raw[0, 0])

    vals_hd, vecs_hd = np.linalg.eigh(cliff_lie(hp10 - hm10))
    d_spin = (vecs_hd * np.exp(-1j * math.pi * vals_hd / 4)) @ vecs_hd.conj().T
    dh_spin = (vecs_hd * np.exp(+1j * math.pi * vals_hd / 8)) @ vecs_hd.conj().T

    vals_v, vecs_v = np.linalg.eigh(hp10 - hm10)
    d_vec = (vecs_v * np.exp(-1j * math.pi * vals_v / 4)) @ vecs_v.conj().T

    ev_ch = np.real(np.diag(chirality))
    idx_ch_plus = [i for i in range(32) if ev_ch[i] > 0.0]
    idx_ch_minus = [i for i in range(32) if ev_ch[i] < 0.0]
    h4 = np.diag([np.exp(1j * (3 * math.pi / 4))] + [np.exp(-1j * (math.pi / 4))] * 3)

    u16_a = _haar(16, rng)
    u16_b = _haar(16, rng)
    u4_adv = _haar(4, rng)

    x_16_4 = u16_a @ a_spin[np.ix_(idx_ch_plus, idx_ch_plus)] @ u16_a.conj().T
    d_16_4 = u16_a @ d_spin[np.ix_(idx_ch_plus, idx_ch_plus)] @ u16_a.conj().T
    dh_16_4 = u16_a @ dh_spin[np.ix_(idx_ch_plus, idx_ch_plus)] @ u16_a.conj().T
    e_16_4 = u16_a @ cliff_lie(e10)[np.ix_(idx_ch_plus, idx_ch_plus)] @ u16_a.conj().T
    g_16_4 = u16_a @ cliff_lie(g10)[np.ix_(idx_ch_plus, idx_ch_plus)] @ u16_a.conj().T
    h4_s = u4_adv @ h4 @ u4_adv.conj().T

    x_64a = np.kron(x_16_4, h4_s)
    y_64a = np.kron(d_16_4 @ x_16_4, h4_s)
    dh_64a = np.kron(dh_16_4, np.eye(4, dtype=complex))
    e_64a = np.kron(e_16_4, np.eye(4, dtype=complex))
    g_64a = np.kron(g_16_4, np.eye(4, dtype=complex))

    x_b16 = u16_b @ a_spin[np.ix_(idx_ch_minus, idx_ch_minus)] @ u16_b.conj().T
    d_b16 = u16_b @ d_spin[np.ix_(idx_ch_minus, idx_ch_minus)] @ u16_b.conj().T
    x_64b = np.kron(x_b16, u4_adv @ h4.conj() @ u4_adv.conj().T)
    y_64b = np.kron(d_b16 @ x_b16, u4_adv @ h4.conj() @ u4_adv.conj().T)

    fi = np.diag([1j, -1j])
    fj = np.array([[0.0, 1.0], [-1.0, 0.0]], dtype=complex)
    fk = fi @ fj
    gs = (np.eye(2) - fk) / math.sqrt(2.0)
    gl = (np.eye(2) + fi) / math.sqrt(2.0)
    gr = (np.eye(2) - fj) / math.sqrt(2.0)

    phi_s0 = gs[0, 0] * e_64a + gs[0, 1] * g_64a
    phi_s1 = gs[1, 0] * e_64a + gs[1, 1] * g_64a
    err_s_scrambled = max(
        float(np.max(np.abs(dh_64a @ y_64a @ dh_64a.conj().T - x_64a))),
        float(np.max(np.abs(dh_64a @ x_64a.conj().T @ dh_64a.conj().T - y_64a))),
        float(np.max(np.abs(dh_64a @ phi_s0 @ dh_64a.conj().T - e_64a))),
        float(np.max(np.abs(dh_64a @ phi_s1 @ dh_64a.conj().T - g_64a))),
    )

    def ext2(m: np.ndarray) -> np.ndarray:
        ps = list(combinations(range(m.shape[0]), 2))
        out = np.zeros((len(ps), len(ps)), dtype=complex)
        for i, (r0, r1) in enumerate(ps):
            for j, (c0, c1) in enumerate(ps):
                out[i, j] = m[r0, c0] * m[r1, c1] - m[r0, c1] * m[r1, c0]
        return out

    x_4x4b = np.kron(h4, h4.conj())
    v_tr = np.zeros(16, dtype=complex)
    for i in range(4):
        v_tr[5 * i] = 0.5
    p_15 = np.eye(16, dtype=complex) - np.outer(v_tr, v_tr.conj())
    u_15, sv_15, _ = np.linalg.svd(p_15)
    b_15 = u_15[:, sv_15 > 0.5]
    x_15 = b_15.conj().T @ x_4x4b @ b_15

    blocks_xy = [
        (ext2(a_vec), ext2(d_vec @ a_vec)),
        (x_15, x_15),
        (np.kron(a_vec, ext2(h4)), np.kron(d_vec @ a_vec, ext2(h4))),
        (x_64a, y_64a),
        (x_64b, y_64b),
    ]
    kpi_minus = 0
    k4_counts: Counter[str] = Counter()
    for xm, ym in blocks_xy:
        kpi = xm @ ym @ xm.conj().T @ ym.conj().T
        ev, vc = np.linalg.eigh((kpi + kpi.conj().T) / 2.0)
        kpi_minus += int(np.sum(np.abs(ev + 1.0) < 1e-8))
        vp = vc[:, np.abs(ev - 1.0) < 1e-8]
        xp = vp.conj().T @ xm @ vp
        yp = vp.conj().T @ ym @ vp
        id_p = np.eye(vp.shape[1], dtype=complex)
        for p1, p2 in product((0, 1), repeat=2):
            proj = (1 / 4) * (id_p + ((-1) ** p1) * xp) @ (id_p + ((-1) ** p2) * yp)
            k4_counts[f"{p1}{p2}"] += int(round(float(np.real(np.trace(proj)))))

    # Exact Q(zeta_24) closure of 2O (order 48) and St (order 16, index 3) (S2-D3 fix):
    irt2_c = _cyc24_sqrt2_inv()
    one_c = _cyc24_int(1)
    i_c = _cyc24_pow_zeta(6)
    gl_c: Cyc24Mat = (
        (_cyc24_mul(irt2_c, _cyc24_add(one_c, i_c)), _CYC24_ZERO),
        (_CYC24_ZERO, _cyc24_mul(irt2_c, _cyc24_add(one_c, _cyc24_neg(i_c)))),
    )
    gr_c: Cyc24Mat = (
        (irt2_c, _cyc24_neg(irt2_c)),
        (irt2_c, irt2_c),
    )
    g_2o_cyc = _bfs_group_cyc24({"L": gl_c, "R": gr_c, "l": _cyc24_mat_dag(gl_c), "r": _cyc24_mat_dag(gr_c)})
    sx_c: Cyc24Mat = ((_CYC24_ZERO, one_c), (one_c, _CYC24_ZERO))
    neg_sx_c: Cyc24Mat = ((_CYC24_ZERO, _cyc24_neg(one_c)), (_cyc24_neg(one_c), _CYC24_ZERO))
    st_cyc = [
        mat_g
        for mat_g in g_2o_cyc
        if _cyc24_matmul(
            _cyc24_matmul(tuple(tuple(_cyc24_conj(mat_g[r_i][c_i]) for c_i in range(2)) for r_i in range(2)), sx_c),
            tuple(tuple(mat_g[c_i][r_i] for c_i in range(2)) for r_i in range(2)),
        )
        in (sx_c, neg_sx_c)
    ]

    g_2o = _bfs_group({"L": gl, "R": gr, "l": gl.conj().T, "r": gr.conj().T})
    st = [
        m
        for _, m in g_2o
        if np.max(np.abs(m.conj() @ sx @ m.T - sx)) < 1e-9 or np.max(np.abs(m.conj() @ sx @ m.T + sx)) < 1e-9
    ]

    st_left_cosets = {
        frozenset(_cyc24_matmul(g_m, s_m) for s_m in st_cyc)
        for g_m in g_2o_cyc
    }

    return {
        "order_2O": len(g_2o_cyc),
        "order_St": len(st_cyc),
        "order_2O_float_matches_exact": len(g_2o) == len(g_2o_cyc) and len(st) == len(st_cyc),
        "index_2O_St": len(st_left_cosets),
        "pauli_clifford_scrambled_S_theta_err": err_s_scrambled,
        "kpi_minus_total": kpi_minus,
        "klein4_totals": dict(k4_counts),
    }


# ---------------------------------------------------------------------------
# Check 3: q-Series Leading Powers + Scrambled F2 Cocycle + Exact Q(zeta_24) Sym^2
# ---------------------------------------------------------------------------
def check_qseries_and_scrambled_weave_triplet(seed: int = 31) -> dict[str, Any]:
    rng = np.random.default_rng(seed)

    def eval_v(tau: complex) -> np.ndarray:
        with mp.workdps(40):
            t = mp.mpc(tau)
            q2 = mp.exp(2j * mp.pi * t)
            q1 = mp.exp(1j * mp.pi * t)
            t2 = 2 * mp.exp(1j * (mp.pi * t / 4)) * sum(q2 ** (n * (n + 1) // 2) for n in range(36))
            t3 = mp.jtheta(3, 0, q1)
            t4 = mp.jtheta(4, 0, q1)
            eta3 = mp.exp(1j * mp.pi * t / 4) * mp.fprod([(1 - q2**n) ** 3 for n in range(1, 60)])
            return np.array([complex(t2**2 / eta3), complex(t3**2 / eta3), complex(t4**2 / eta3)], dtype=complex)

    y0 = 8 / 5
    n_quad = 64
    xs = np.linspace(0.0, 2.0, n_quad, endpoint=False)
    c0_lead = 0.0 + 0.0j
    c1_lead = 0.0 + 0.0j
    c2_lead = 0.0 + 0.0j
    for x in xs:
        tau = complex(float(x), y0)
        q2_eighth = np.exp(2j * math.pi * tau / 8)
        vv = eval_v(tau)
        c0_lead += vv[0] / q2_eighth
        c1_lead += vv[1] * q2_eighth
        c2_lead += vv[2] * q2_eighth
    c0_lead /= n_quad
    c1_lead /= n_quad
    c2_lead /= n_quad
    qseries_leading_coeff_err = max(abs(c0_lead - 4), abs(c1_lead - 1.0), abs(c2_lead - 1.0))

    u2 = _haar(2, rng)
    qi = u2 @ np.diag([1j, -1j]) @ u2.conj().T
    qj = u2 @ np.array([[0.0, 1.0], [-1.0, 0.0]], dtype=complex) @ u2.conj().T
    gl = (np.eye(2) + qi) / math.sqrt(2.0)
    gr = (np.eye(2) - qj) / math.sqrt(2.0)
    rho = {"a": qi, "b": qj}
    pars = [(1, 0), (0, 1), (1, 1)]

    def chi(p: tuple[int, int], ch: str) -> int:
        return -1 if (p[0] if ch == "a" else p[1]) else 1

    def rep_w(w: str, p: tuple[int, int]) -> np.ndarray:
        m = np.eye(2, dtype=complex)
        for c in w:
            g = rho[c.lower()] * chi(p, c.lower())
            m = m @ (g if c.islower() else g.conj().T)
        return m

    def cocyc(z: dict[str, np.ndarray], w: str, p: tuple[int, int]) -> np.ndarray:
        val = np.zeros(2, dtype=complex)
        m = np.eye(2, dtype=complex)
        for c in w:
            mg = rep_w(c.lower(), p)
            if c.islower():
                val = val + m @ z[c.lower()]
                m = m @ mg
            else:
                mi = mg.conj().T
                val = val - m @ (mi @ z[c.lower()])
                m = m @ mi
        return val

    bases = {}
    for p in pars:
        cob = np.zeros((4, 2), dtype=complex)
        for k in range(2):
            ek = np.zeros(2, dtype=complex)
            ek[k] = 1.0
            cob[:2, k] = rep_w("a", p) @ ek - ek
            cob[2:, k] = rep_w("b", p) @ ek - ek
        qc, _ = np.linalg.qr(cob)
        pr = np.eye(4, dtype=complex) - qc @ qc.conj().T
        us, _, _ = np.linalg.svd(pr)
        bases[p] = (us[:, :2], pr)

    def act_p(mv: dict[str, str], p: tuple[int, int]) -> tuple[int, int]:
        sa = math.prod(chi(p, c.lower()) for c in mv["a"])
        sb = math.prod(chi(p, c.lower()) for c in mv["b"])
        return (0 if sa == 1 else 1, 0 if sb == 1 else 1)

    def build_mv(mv: dict[str, str], lift: np.ndarray) -> np.ndarray:
        li = lift.conj().T
        out = np.zeros((6, 6), dtype=complex)
        for ip, p in enumerate(pars):
            q = act_p(mv, p)
            iq = pars.index(q)
            bp, _ = bases[p]
            bq, pq = bases[q]
            for k in range(2):
                v = bp[:, k]
                z = {"a": v[:2], "b": v[2:]}
                w = pq @ np.concatenate([li @ cocyc(z, mv["a"], p), li @ cocyc(z, mv["b"], p)])
                out[2 * iq : 2 * iq + 2, 2 * ip + k] = bq.conj().T @ w
        return out

    ml6 = build_mv({"a": "a", "b": "ab"}, gl)
    mr6 = build_mv({"a": "ab", "b": "b"}, gr)
    gv = _bfs_group({"L": ml6, "R": mr6})

    cstack = np.vstack([np.kron(np.eye(6), m) - np.kron(m.T, np.eye(6)) for _, m in gv])
    _, _, vhc = np.linalg.svd(cstack)
    xc = next(
        r.reshape((6, 6), order="F")
        for r in vhc[-2:].conj()
        if np.linalg.norm(r.reshape((6, 6), order="F") - (np.trace(r.reshape((6, 6), order="F")) / 6) * np.eye(6)) > 1e-6
    )
    evx, vxx = np.linalg.eig(xc)
    cl: dict[tuple[float, float], list[int]] = {}
    for idx, val in enumerate(evx):
        cl.setdefault((round(float(val.real), 4), round(float(val.imag), 4)), []).append(idx)
    tl_cand = tr_cand = None
    w8b = np.exp(-1j * math.pi / 4)
    for idxs in cl.values():
        qp, _ = np.linalg.qr(vxx[:, idxs])
        tl_try = qp.conj().T @ ml6 @ qp
        tr_try = qp.conj().T @ mr6 @ qp
        if abs(np.trace(tl_try) - w8b) < 1e-7:
            tl_cand, tr_cand = tl_try, tr_try
    if tl_cand is None or tr_cand is None:
        raise RuntimeError("Failed to isolate T in scrambled quaternion basis")

    gt = _bfs_group({"L": tl_cand, "R": tr_cand})
    zt = [w for w, m in gt if all(np.max(np.abs(m @ n - n @ m)) < 1e-7 for _, n in gt)]
    st_mat = tl_cand @ np.linalg.inv(tr_cand) @ tl_cand
    st4_plus_i_err = float(np.max(np.abs(np.linalg.matrix_power(st_mat, 4) + np.eye(3))))

    # Exact Q(zeta_24) Weil_2 and Sym^2(Weil_2) group closures across all twists (S2-D3 fix):
    one_c = _cyc24_int(1)
    i_c = _cyc24_pow_zeta(6)
    irt2_c = _cyc24_sqrt2_inv()
    s2_c = _cyc24_add(_cyc24_pow_zeta(3), _cyc24_pow_zeta(-3))  # sqrt(2)
    l2_c: Cyc24Mat = ((one_c, _CYC24_ZERO), (_CYC24_ZERO, i_c))
    l2_inv_c: Cyc24Mat = ((one_c, _CYC24_ZERO), (_CYC24_ZERO, _cyc24_neg(i_c)))
    s0_c: Cyc24Mat = ((irt2_c, irt2_c), (irt2_c, _cyc24_neg(irt2_c)))
    r2_c = _cyc24_matmul(_cyc24_matmul(s0_c, l2_inv_c), s0_c)
    weil2_cyc = _bfs_group_cyc24({"L": l2_c, "R": r2_c})

    def sym2_cyc(u: Cyc24Mat) -> Cyc24Mat:
        a, b, c, d = u[0][0], u[0][1], u[1][0], u[1][1]
        return (
            (_cyc24_mul(a, a), _cyc24_mul(s2_c, _cyc24_mul(a, b)), _cyc24_mul(b, b)),
            (
                _cyc24_mul(s2_c, _cyc24_mul(a, c)),
                _cyc24_add(_cyc24_mul(a, d), _cyc24_mul(b, c)),
                _cyc24_mul(s2_c, _cyc24_mul(b, d)),
            ),
            (_cyc24_mul(c, c), _cyc24_mul(s2_c, _cyc24_mul(c, d)), _cyc24_mul(d, d)),
        )

    sym2_l_c = sym2_cyc(l2_c)
    sym2_r_c = sym2_cyc(r2_c)
    untwisted_order = len(_bfs_group_cyc24({"L": sym2_l_c, "R": sym2_r_c}))
    even_orders = sorted(
        {
            len(
                _bfs_group_cyc24(
                    {
                        "L": _cyc24_mat_scale(_cyc24_pow_zeta(m), sym2_l_c),
                        "R": _cyc24_mat_scale(_cyc24_pow_zeta(-m), sym2_r_c),
                    }
                )
            )
            for m in range(0, 24, 2)
        }
    )
    l2_bar_c = tuple(tuple(_cyc24_conj(l2_c[r_i][c_i]) for c_i in range(2)) for r_i in range(2))
    r2_bar_c = tuple(tuple(_cyc24_conj(r2_c[r_i][c_i]) for c_i in range(2)) for r_i in range(2))
    odd_m3_bar_l_c = _cyc24_mat_scale(_cyc24_pow_zeta(3), sym2_cyc(l2_bar_c))
    odd_m3_bar_r_c = _cyc24_mat_scale(_cyc24_pow_zeta(-3), sym2_cyc(r2_bar_c))
    odd_m3_grp_c = _bfs_group_cyc24({"L": odd_m3_bar_l_c, "R": odd_m3_bar_r_c})
    odd_m3_center_c = [
        m_g
        for m_g in odd_m3_grp_c
        if all(_cyc24_matmul(m_g, n_g) == _cyc24_matmul(n_g, m_g) for n_g in odd_m3_grp_c)
    ]

    odd_m3_bar_l = np.array([[_cyc24_to_complex(x) for x in row] for row in odd_m3_bar_l_c], dtype=complex)
    odd_m3_bar_r = np.array([[_cyc24_to_complex(x) for x in row] for row in odd_m3_bar_r_c], dtype=complex)
    sys_int = np.vstack(
        [
            np.kron(tl_cand.T, np.eye(3)) - np.kron(np.eye(3), odd_m3_bar_l),
            np.kron(tr_cand.T, np.eye(3)) - np.kron(np.eye(3), odd_m3_bar_r),
        ]
    )
    _, _, vh_int = np.linalg.svd(sys_int)
    u_raw = vh_int[-1].conj().reshape((3, 3), order="F")
    up, _, vhp = np.linalg.svd(u_raw)
    u_int = up @ vhp
    intertwine_err = max(
        float(np.max(np.abs(u_int @ tl_cand @ u_int.conj().T - odd_m3_bar_l))),
        float(np.max(np.abs(u_int @ tr_cand @ u_int.conj().T - odd_m3_bar_r))),
    )

    return {
        "qseries_leading_coeff_quadrature_err": float(qseries_leading_coeff_err),
        "exact_weil2_order_cyc24": len(weil2_cyc),
        "exact_odd_m3_order_cyc24": len(odd_m3_grp_c),
        "exact_odd_m3_center_order_cyc24": len(odd_m3_center_c),
        "scrambled_order_G_V": len(gv),
        "scrambled_order_G_T": len(gt),
        "scrambled_center_order": len(zt),
        "scrambled_S_T_fourth_plus_I_err": st4_plus_i_err,
        "untwisted_Sym2_Weil2_order": untwisted_order,
        "even_Z24_twist_orders": even_orders,
        "odd_m3_Sym2_Weil2_bar_intertwiner_err": intertwine_err,
    }


# ---------------------------------------------------------------------------
# Check 4: Cauchy Contour Physical S^{-3} 2-Mode E_theta Splitting on E_tau \ {0}
# ---------------------------------------------------------------------------
def check_elliptic_contour_pole_filtration() -> dict[str, Any]:
    r"""Use direct Cauchy contour Laurent integration around |z| = eps on E_tau \ {0} AND explicit
    64D (16,4) E_8 gauge compensators (X_64, D_half^-1) to construct the full 2x2 physical S^{-3}
    representation matrices of BOTH generators (L^2, S_theta) of E_theta on:
      (a) chi_(1,1) 2-mode a-slot {v_sing * conj(eta^3 S_3), v_sing * conj(eta d_z S_3)}
      (b) chi_(0,0) 2-mode a-slot {v_trip * conj(eta^5), v_trip * conj(eta wp)}
    (using exact Jacobi identity wp = (S_2^2 + S_3^2 + S_4^2)/3, never zero-initializing off-diagonals!),
    proving off-diagonal shear < 1e-12, joint_commutant_dim == 2, and distinct L^2 eigenvalues (1 + 1),
    plus irreducible (2) (joint_commutant_dim == 1) on (10,6)'s (S_2, S_4) doublet.
    """
    # Build independent 64D (16,4) compensators X_64 (for L^2) and Dh_64 (for S_theta) + harmonic fibers:
    sx = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    sy = np.array([[0.0, -1j], [1j, 0.0]], dtype=complex)
    sz = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
    i2 = np.eye(2, dtype=complex)

    def kron5(ops: list[np.ndarray]) -> np.ndarray:
        out = ops[0]
        for op in ops[1:]:
            out = np.kron(out, op)
        return out

    gam_e = []
    for k in range(5):
        gam_e.append(kron5([sz] * k + [sx] + [i2] * (4 - k)))
        gam_e.append(kron5([sz] * k + [sy] + [i2] * (4 - k)))
    chir5 = kron5([sz] * 5)
    psis = [(gam_e[2 * k] + 1j * gam_e[2 * k + 1]) / 2.0 for k in range(5)]
    psidags = [p.conj().T for p in psis]

    e5 = np.zeros((5, 5), dtype=complex)
    for j, c in enumerate([2.0, math.sqrt(6), math.sqrt(6), 2.0]):
        e5[j + 1, j] = c
    h5 = np.diag([-4, -2, 0, 2, 4]).astype(complex)
    j5 = np.diag([1.0, -1.0, 1.0, -1.0, 1.0])[:, ::-1].astype(complex)
    bz = np.zeros((5, 5), dtype=complex)
    bz[1, 4] = math.sqrt(2 / 5)
    bz[4, 1] = -bz[1, 4]
    bz[2, 3] = -math.sqrt(3 / 5)
    bz[3, 2] = -bz[2, 3]
    z5 = np.zeros((5, 5), dtype=complex)
    e10 = np.block([[e5, z5], [z5, -e5.T]])
    g10 = math.sqrt(10) * np.block([[z5, bz], [j5 @ bz @ j5, z5]])
    h10 = np.block([[h5, z5], [z5, -h5.T]])
    n10 = np.block([[np.eye(5), z5], [z5, -np.eye(5)]]).astype(complex)
    ep10, em10 = (e10 + g10) / 2.0, (e10 - g10) / 2.0
    hp10 = ep10 @ ep10.conj().T - ep10.conj().T @ ep10
    hm10 = em10 @ em10.conj().T - em10.conj().T @ em10

    def cliff_lie(m10: np.ndarray) -> np.ndarray:
        out = -0.5 * np.trace(m10[:5, :5]) * np.eye(32, dtype=complex)
        for a in range(5):
            for b in range(5):
                out += m10[a, b] * (psis[a] @ psidags[b])
                out += 0.5 * m10[a, b + 5] * (psis[a] @ psis[b])
                out += 0.5 * m10[a + 5, b] * (psidags[a] @ psidags[b])
        return out

    a_vec = -1j * n10 @ np.diag(np.exp(-1j * math.pi * np.diag(h10) / 4))
    psi_vec = psis + psidags
    rows_a = [
        np.kron(psi_vec[m_idx].T, np.eye(32))
        - np.kron(np.eye(32), sum(a_vec[n_idx, m_idx] * psi_vec[n_idx] for n_idx in range(10)))
        for m_idx in range(10)
    ]
    _, _, vh_a = np.linalg.svd(np.vstack(rows_a), full_matrices=False)
    ua_p, _, vha_p = np.linalg.svd(vh_a[-1].conj().reshape((32, 32), order="F"))
    a_spin_raw = ua_p @ vha_p
    top_ph = np.exp(1j * math.pi * sum([1, 0, -1, -2, -3]) / 4)
    a_spin = a_spin_raw * (top_ph / a_spin_raw[0, 0])

    vals_s, vecs_s = np.linalg.eigh(cliff_lie(hp10 - hm10))
    dh_spin = (vecs_s * np.exp(+1j * math.pi * vals_s / 8)) @ vecs_s.conj().T
    idx_p = [i for i in range(32) if float(np.real(chir5[i, i])) > 0.0]
    h4 = np.diag([np.exp(1j * (3 * math.pi / 4))] + [np.exp(-1j * (math.pi / 4))] * 3)
    x_64 = np.kron(a_spin[np.ix_(idx_p, idx_p)], h4)
    dh_64 = np.kron(dh_spin[np.ix_(idx_p, idx_p)], np.eye(4, dtype=complex))
    e_16 = cliff_lie(e10)[np.ix_(idx_p, idx_p)]
    g_16 = cliff_lie(g10)[np.ix_(idx_p, idx_p)]
    _, _, vh_top = np.linalg.svd(np.vstack([e_16, g_16]))
    v16_top = vh_top[-1].conj()
    v16_top /= np.linalg.norm(v16_top)
    v_sing = np.zeros(64, dtype=complex)
    v_trip = np.zeros(64, dtype=complex)
    for r_i in range(16):
        v_sing[4 * r_i] = v16_top[r_i]
        v_trip[4 * r_i + 1] = v16_top[r_i]

    with mp.workdps(40):
        tau = mp.mpc(mp.mpf(3) / mp.mpf(16), mp.mpf(19) / mp.mpf(15))
        eps = mp.mpf(1) / mp.mpf(25)
        n_pts = 64

        def eta_mp(t: mp.mpc) -> mp.mpc:
            q2 = mp.exp(2j * mp.pi * t)
            return mp.exp(1j * mp.pi * t / 12) * mp.fprod([1 - q2**n for n in range(1, 70)])

        def szego(idx_th: int, z: mp.mpc, t: mp.mpc) -> mp.mpc:
            q = mp.exp(1j * mp.pi * t)
            return (mp.pi * mp.jtheta(1, 0, q, 1) * mp.jtheta(idx_th, mp.pi * z, q)) / (
                mp.jtheta(idx_th, 0, q) * mp.jtheta(1, mp.pi * z, q)
            )

        def dszego(idx_th: int, z: mp.mpc, t: mp.mpc) -> mp.mpc:
            q = mp.exp(1j * mp.pi * t)
            c0 = mp.pi * mp.jtheta(1, 0, q, 1) / mp.jtheta(idx_th, 0, q)
            tb = mp.jtheta(idx_th, mp.pi * z, q)
            dtb = mp.pi * mp.jtheta(idx_th, mp.pi * z, q, 1)
            t1 = mp.jtheta(1, mp.pi * z, q)
            dt1 = mp.pi * mp.jtheta(1, mp.pi * z, q, 1)
            return c0 * (dtb * t1 - tb * dt1) / (t1**2)

        def weierstrass_p(z: mp.mpc, t: mp.mpc) -> mp.mpc:
            # Exact Jacobi identity: wp(z|tau) = (S_2(z|tau)^2 + S_3(z|tau)^2 + S_4(z|tau)^2) / 3
            return (szego(2, z, t) ** 2 + szego(3, z, t) ** 2 + szego(4, z, t) ** 2) / 3

        def contour_laurent(fn, power_z: int) -> complex:
            acc = mp.mpc(0)
            for k in range(n_pts):
                ang = 2 * mp.pi * k / n_pts
                z = eps * mp.exp(1j * ang)
                acc += (z**power_z) * fn(z) * (1j * z)
            return complex((acc / 1j) / n_pts)

        c_minus2_hol_after_s = contour_laurent(lambda z: (-1 / tau), 1)
        c_minus2_wp_base = contour_laurent(lambda z: weierstrass_p(z, tau), 1)
        c_minus2_wp_after_s = contour_laurent(lambda z: (-1 / tau) * weierstrass_p(-z / tau, -1 / tau), 1)
        triv_filtration_err = max(
            abs(c_minus2_hol_after_s),
            abs(c_minus2_wp_base - 1.0),
            abs(c_minus2_wp_after_s + complex(tau)),
        )

        z_probe = mp.mpc(mp.mpf(3) / mp.mpf(17), mp.mpf(4) / mp.mpf(13))
        odd_parity_err = max(abs(complex(szego(b_i, -z_probe, tau) + szego(b_i, z_probe, tau))) for b_i in (2, 3, 4))
        c_minus1_s3_base = contour_laurent(lambda z: szego(3, z, tau), 0)
        c_minus2_s3_after_s = contour_laurent(lambda z: (-1 / tau) * szego(3, -z / tau, -1 / tau), 1)
        c_minus1_s3_after_s = contour_laurent(lambda z: (-1 / tau) * szego(3, -z / tau, -1 / tau), 0)
        c_minus2_s3p_base = contour_laurent(lambda z: dszego(3, z, tau), 1)
        chi11_filtration_err = max(
            odd_parity_err,
            abs(c_minus1_s3_base - 1.0),
            abs(c_minus2_s3_after_s),
            abs(c_minus1_s3_after_s - 1.0),
            abs(c_minus2_s3p_base + 1.0),
        )

        swap_err = max(
            abs(complex((-1 / tau) * szego(2, -z_probe / tau, -1 / tau) - szego(4, z_probe, tau))),
            abs(complex((-1 / tau) * szego(4, -z_probe / tau, -1 / tau) - szego(2, z_probe, tau))),
        )

        # Full 2x2 physical S^{-3} E_theta matrices via Cauchy Laurent functionals + 64D compensators (S2-D4 fix):
        def contour_2mode_etheta_mats(
            v_fib: np.ndarray,
            hol_f0,
            hol_f1,
            pwr0: int,
            pwr1: int,
        ) -> tuple[np.ndarray, np.ndarray]:
            c_base = np.array(
                [
                    [contour_laurent(lambda z: hol_f0(z, tau), pwr0), contour_laurent(lambda z: hol_f1(z, tau), pwr0)],
                    [contour_laurent(lambda z: hol_f0(z, tau), pwr1), contour_laurent(lambda z: hol_f1(z, tau), pwr1)],
                ],
                dtype=complex,
            ).conj()
            c_inv = np.linalg.inv(c_base)
            mats_out: list[np.ndarray] = []
            for u64_g, is_s in [(x_64, False), (dh_64, True)]:
                fib_amp = complex(np.vdot(v_fib, u64_g @ v_fib))
                if not is_s:
                    t_old = tau - 2
                    eg5 = mp.mpc(1)
                    c_push_hol = np.array(
                        [
                            [
                                contour_laurent(lambda z: hol_f0(z, t_old) * eg5, pwr0),
                                contour_laurent(lambda z: hol_f1(z, t_old) * eg5, pwr0),
                            ],
                            [
                                contour_laurent(lambda z: hol_f0(z, t_old) * eg5, pwr1),
                                contour_laurent(lambda z: hol_f1(z, t_old) * eg5, pwr1),
                            ],
                        ],
                        dtype=complex,
                    )
                else:
                    t_old = -1 / tau
                    eg5 = mp.sqrt(-1 / tau) ** 5
                    c_push_hol = np.array(
                        [
                            [
                                contour_laurent(lambda z: hol_f0(-z / tau, t_old) * eg5, pwr0),
                                contour_laurent(lambda z: hol_f1(-z / tau, t_old) * eg5, pwr0),
                            ],
                            [
                                contour_laurent(lambda z: hol_f0(-z / tau, t_old) * eg5, pwr1),
                                contour_laurent(lambda z: hol_f1(-z / tau, t_old) * eg5, pwr1),
                            ],
                        ],
                        dtype=complex,
                    )
                mats_out.append(fib_amp * (c_inv @ c_push_hol.conj()))
            return mats_out[0], mats_out[1]

        l2_chi11, s_chi11 = contour_2mode_etheta_mats(
            v_sing,
            lambda z, t: (eta_mp(t) ** 3) * szego(3, z, t),
            lambda z, t: eta_mp(t) * dszego(3, z, t),
            0,
            1,
        )
        l2_chi00, s_chi00 = contour_2mode_etheta_mats(
            v_trip,
            lambda z, t: eta_mp(t) ** 5,
            lambda z, t: eta_mp(t) * weierstrass_p(z, t),
            -1,
            1,
        )

    shear_err = max(
        abs(complex(l2_chi11[0, 1])),
        abs(complex(l2_chi11[1, 0])),
        abs(complex(s_chi11[0, 1])),
        abs(complex(s_chi11[1, 0])),
        abs(complex(l2_chi00[0, 1])),
        abs(complex(l2_chi00[1, 0])),
        abs(complex(s_chi00[0, 1])),
        abs(complex(s_chi00[1, 0])),
    )
    comm_chi11 = _joint_commutant_dim([l2_chi11, s_chi11])
    comm_chi00 = _joint_commutant_dim([l2_chi00, s_chi00])
    # Distinct L^2 eigenvalues rule out a 2x2 non-split Jordan block (which also has commutant dim 2 under 1 gen):
    chi11_l2_distinct = abs(complex(l2_chi11[0, 0] - l2_chi11[1, 1])) > (1 / 10)
    chi00_l2_distinct = abs(complex(l2_chi00[0, 0] - l2_chi00[1, 1])) > (1 / 10)
    chi11_l2_eig_err = max(
        abs(complex(l2_chi11[0, 0]) - (-1j)),
        abs(complex(l2_chi11[1, 1]) - complex(np.exp(-1j * (5 * math.pi / 6)))),
    )
    chi00_l2_eig_err = max(
        abs(complex(l2_chi00[0, 0]) - complex(np.exp(1j * (5 * math.pi / 6)))),
        abs(complex(l2_chi00[1, 1]) - complex(np.exp(1j * (math.pi / 6)))),
    )
    # Contrast with (10,6) a-slot doublet (S_2, S_4): X = diag(-1, +1) + swap => joint commutant dim = 1!
    comm_vec6 = _joint_commutant_dim([np.diag([-1.0 + 0j, 1.0 + 0j]), sx])

    all_ok = (
        max(
            odd_parity_err,
            triv_filtration_err,
            chi11_filtration_err,
            swap_err,
            shear_err,
            chi11_l2_eig_err,
            chi00_l2_eig_err,
        )
        < TOL
        and comm_chi11 == 2
        and comm_chi00 == 2
        and comm_vec6 == 1
        and chi11_l2_distinct
        and chi00_l2_distinct
    )

    return {
        "szego_odd_parity_err": float(odd_parity_err),
        "trivial_O2p_pole_filtration_err": float(triv_filtration_err),
        "chi11_2p_pole_filtration_err": float(chi11_filtration_err),
        "vector_six_S2_S4_swap_err": float(swap_err),
        "physical_s_minus3_offdiag_shear_err": float(shear_err),
        "chi11_aslot_joint_commutant_dim": comm_chi11,
        "chi00_aslot_joint_commutant_dim": comm_chi00,
        "vector_six_aslot_joint_commutant_dim": comm_vec6,
        "chi11_l2_eig_err": float(chi11_l2_eig_err),
        "chi00_l2_eig_err": float(chi00_l2_eig_err),
        "filtration_and_swap_verified": all_ok,
    }


# ---------------------------------------------------------------------------
# Check 5: Exact Rational Z_4 Global Kernel in E8, Disconnected so(5) Control,
#          and Cauchy-Contour + Exact Q(zeta_24) 3-Branch Half-Form Transport
# ---------------------------------------------------------------------------
def check_z4_kernel_so5_and_3branch_half_form_orders() -> dict[str, Any]:
    # 1. Exact rational Fraction^8 test of all 16 central pairs (k10, k6) in Z_4 x Z_4 across all 240 E8 roots (S2-D3 fix):
    roots_240: list[tuple[Fraction, ...]] = []
    for i, j in combinations(range(8), 2):
        for si, sj in product((-1, 1), repeat=2):
            v = [Fraction(0) for _ in range(8)]
            v[i], v[j] = Fraction(si), Fraction(sj)
            roots_240.append(tuple(v))
    for signs in product((-1, 1), repeat=8):
        if signs.count(-1) % 2 == 0:
            roots_240.append(tuple(Fraction(s_i, 2) for s_i in signs))

    th10 = (Fraction(1, 2), Fraction(1, 2), Fraction(1, 2), Fraction(1, 2), Fraction(1, 2), Fraction(0), Fraction(0), Fraction(0))
    th6 = (Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(1, 2), Fraction(1, 2), Fraction(1, 2))
    z4_kernel_pairs: list[list[int]] = []
    for k10 in range(4):
        for k6 in range(4):
            shift = tuple(k10 * th10[c] + k6 * th6[c] for c in range(8))
            if all(sum(r[c] * shift[c] for c in range(8)).denominator == 1 for r in roots_240):
                z4_kernel_pairs.append([k10, k6])

    # 2. Disconnected Pin_-(6) / O(6) coherent holonomy h_1 = diag(-1, 1, 1, 1, 1, 1) centralizer in so(6):
    h1_mat = np.diag([-1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
    so6_gens = []
    for a_i, b_i in combinations(range(6), 2):
        g_m = np.zeros((6, 6), dtype=float)
        g_m[a_i, b_i] = 1.0
        g_m[b_i, a_i] = -1.0
        so6_gens.append(g_m)
    unbroken_so5_dim = sum(1 for g_m in so6_gens if float(np.max(np.abs(h1_mat @ g_m @ h1_mat.T - g_m))) < TOL)

    # 3. Independent Pauli-Clifford 124D = (10, 6) (+) (16, 4) faithful carrier + Cauchy contour 3-branch transport:
    sx = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    sy = np.array([[0.0, -1j], [1j, 0.0]], dtype=complex)
    sz = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
    i2 = np.eye(2, dtype=complex)

    def kron5(ops: list[np.ndarray]) -> np.ndarray:
        out = ops[0]
        for op in ops[1:]:
            out = np.kron(out, op)
        return out

    gammas_e = []
    for k in range(5):
        gammas_e.append(kron5([sz] * k + [sx] + [i2] * (4 - k)))
        gammas_e.append(kron5([sz] * k + [sy] + [i2] * (4 - k)))
    chir = kron5([sz] * 5)
    psis = [(gammas_e[2 * k] + 1j * gammas_e[2 * k + 1]) / 2.0 for k in range(5)]
    psidags = [p.conj().T for p in psis]

    e5 = np.zeros((5, 5), dtype=complex)
    for j, c in enumerate([2.0, math.sqrt(6), math.sqrt(6), 2.0]):
        e5[j + 1, j] = c
    h5 = np.diag([-4, -2, 0, 2, 4]).astype(complex)
    j5 = np.diag([1.0, -1.0, 1.0, -1.0, 1.0])[:, ::-1].astype(complex)
    bz = np.zeros((5, 5), dtype=complex)
    bz[1, 4] = math.sqrt(2 / 5)
    bz[4, 1] = -bz[1, 4]
    bz[2, 3] = -math.sqrt(3 / 5)
    bz[3, 2] = -bz[2, 3]
    z5 = np.zeros((5, 5), dtype=complex)
    e10 = np.block([[e5, z5], [z5, -e5.T]])
    g10 = math.sqrt(10) * np.block([[z5, bz], [j5 @ bz @ j5, z5]])
    h10 = np.block([[h5, z5], [z5, -h5.T]])
    n10 = np.block([[np.eye(5), z5], [z5, -np.eye(5)]]).astype(complex)
    ep10, em10 = (e10 + g10) / 2.0, (e10 - g10) / 2.0
    hp10 = ep10 @ ep10.conj().T - ep10.conj().T @ ep10
    hm10 = em10 @ em10.conj().T - em10.conj().T @ em10

    def cliff_lie(m10: np.ndarray) -> np.ndarray:
        out = -0.5 * np.trace(m10[:5, :5]) * np.eye(32, dtype=complex)
        for a in range(5):
            for b in range(5):
                out += m10[a, b] * (psis[a] @ psidags[b])
                out += 0.5 * m10[a, b + 5] * (psis[a] @ psis[b])
                out += 0.5 * m10[a + 5, b] * (psidags[a] @ psidags[b])
        return out

    a_vec = -1j * n10 @ np.diag(np.exp(-1j * math.pi * np.diag(h10) / 4))
    psi_vec = psis + psidags
    rows_a = [
        np.kron(psi_vec[m_idx].T, np.eye(32))
        - np.kron(np.eye(32), sum(a_vec[n_idx, m_idx] * psi_vec[n_idx] for n_idx in range(10)))
        for m_idx in range(10)
    ]
    _, _, vh_a = np.linalg.svd(np.vstack(rows_a), full_matrices=False)
    ua_p, _, vha_p = np.linalg.svd(vh_a[-1].conj().reshape((32, 32), order="F"))
    a_spin_raw = ua_p @ vha_p
    top_ph = np.exp(1j * math.pi * sum([1, 0, -1, -2, -3]) / 4)
    a_spin = a_spin_raw * (top_ph / a_spin_raw[0, 0])

    vals_s, vecs_s = np.linalg.eigh(cliff_lie(hp10 - hm10))
    d_spin = (vecs_s * np.exp(-1j * math.pi * vals_s / 4)) @ vecs_s.conj().T
    dh_spin = (vecs_s * np.exp(+1j * math.pi * vals_s / 8)) @ vecs_s.conj().T
    vals_v, vecs_v = np.linalg.eigh(hp10 - hm10)
    d_vec = (vecs_v * np.exp(-1j * math.pi * vals_v / 4)) @ vecs_v.conj().T
    dh_vec = (vecs_v * np.exp(+1j * math.pi * vals_v / 8)) @ vecs_v.conj().T

    idx_p = [i for i in range(32) if float(np.real(chir[i, i])) > 0.0]
    h4 = np.diag([np.exp(1j * (3 * math.pi / 4))] + [np.exp(-1j * (math.pi / 4))] * 3)
    ps6 = list(combinations(range(4), 2))
    h4_6 = np.zeros((6, 6), dtype=complex)
    for r_i, (r0, r1) in enumerate(ps6):
        for c_i, (c0, c1) in enumerate(ps6):
            h4_6[r_i, c_i] = h4[r0, c0] * h4[r1, c1] - h4[r0, c1] * h4[r1, c0]

    def blk124(m60: np.ndarray, m64: np.ndarray) -> np.ndarray:
        z_a = np.zeros((60, 64), dtype=complex)
        z_b = np.zeros((64, 60), dtype=complex)
        return np.block([[m60, z_a], [z_b, m64]])

    x_124 = blk124(np.kron(a_vec, h4_6), np.kron(a_spin[np.ix_(idx_p, idx_p)], h4))
    y_124 = blk124(np.kron(d_vec @ a_vec, h4_6), np.kron((d_spin @ a_spin)[np.ix_(idx_p, idx_p)], h4))
    dh_124 = blk124(np.kron(dh_vec, np.eye(6, dtype=complex)), np.kron(dh_spin[np.ix_(idx_p, idx_p)], np.eye(4, dtype=complex)))
    e_124 = blk124(np.kron(e10, np.eye(6, dtype=complex)), np.kron(cliff_lie(e10)[np.ix_(idx_p, idx_p)], np.eye(4, dtype=complex)))
    g_124 = blk124(np.kron(g10, np.eye(6, dtype=complex)), np.kron(cliff_lie(g10)[np.ix_(idx_p, idx_p)], np.eye(4, dtype=complex)))

    comp_grp = _bfs_group({"X": x_124, "Y": y_124, "D": dh_124, "x": x_124.conj().T, "y": y_124.conj().T, "d": dh_124.conj().T})

    fi = np.diag([1j, -1j])
    fj = np.array([[0.0, 1.0], [-1.0, 0.0]], dtype=complex)
    gl = (np.eye(2) + fi) / math.sqrt(2.0)
    gr = (np.eye(2) - fj) / math.sqrt(2.0)
    gens_f2 = {"L": ("a", "Ab", gl), "R": ("aB", "b", gr)}

    def eval_w(ha: np.ndarray, hb: np.ndarray, w: str) -> np.ndarray:
        cur = np.eye(ha.shape[0], dtype=complex)
        for ch in w:
            cur = cur @ (ha if ch == "a" else ha.conj().T if ch == "A" else hb if ch == "b" else hb.conj().T)
        return cur

    def push_bg(gk: str, bg: tuple[np.ndarray, ...]) -> tuple[np.ndarray, ...]:
        wa, wb, u2 = gens_f2[gk]
        ha, hb, p1, p2 = bg
        return (eval_w(ha, hb, wa), eval_w(ha, hb, wb), u2[0, 0] * p1 + u2[0, 1] * p2, u2[1, 0] * p1 + u2[1, 1] * p2)

    b3 = (x_124, y_124, e_124, g_124)
    b2 = push_bg("R", b3)
    b4 = push_bg("L", b3)
    bgs = {2: b2, 3: b3, 4: b4}
    u2_br = {2: gr, 3: np.eye(2, dtype=complex), 4: gl}
    br_ord = [2, 3, 4]

    sel_sing = [60 + 4 * r_i for r_i in range(16)]
    e_sg = e_124[np.ix_(sel_sing, sel_sing)]
    g_sg = g_124[np.ix_(sel_sing, sel_sing)]
    _, _, vh0 = np.linalg.svd(np.vstack([e_sg, g_sg]))
    v_top = np.zeros(124, dtype=complex)
    v_top[sel_sing] = vh0[-1].conj()
    v_top /= np.linalg.norm(v_top)

    _, sv1, vh1 = np.linalg.svd(np.vstack([np.hstack([e_sg.conj().T, g_sg.conj().T]), np.hstack([-g_sg, e_sg])]))
    h1_16 = vh1[sv1 < 1e-9].conj().T
    x_sg = x_124[np.ix_(sel_sing, sel_sing)]
    y_sg = y_124[np.ix_(sel_sing, sel_sing)]
    ha1 = h1_16.conj().T @ np.kron(fi, x_sg) @ h1_16
    hb1 = h1_16.conj().T @ np.kron(fj, y_sg) @ h1_16
    up1, _, _ = np.linalg.svd((1 / 4) * (np.eye(2) + ha1) @ (np.eye(2) + hb1))
    w32 = h1_16 @ up1[:, 0]
    w_ref = np.zeros((2, 124), dtype=complex)
    w_ref[0, sel_sing] = w32[:16]
    w_ref[1, sel_sing] = w32[16:]
    w_ref /= np.linalg.norm(w_ref)
    w_spin_br = {b_i: u2_br[b_i] @ w_ref for b_i in br_ord}

    with mp.workdps(40):
        tau_c = mp.mpc(mp.mpf(5) / mp.mpf(22), mp.mpf(18) / mp.mpf(13))
        eps_c = mp.mpf(1) / mp.mpf(28)
        n_c = 48

        def eta_f(tv: mp.mpc) -> mp.mpc:
            q2 = mp.exp(2j * mp.pi * tv)
            return mp.exp(1j * mp.pi * tv / 12) * mp.fprod([1 - q2**n for n in range(1, 70)])

        def sz_f(bi: int, zv: mp.mpc, tv: mp.mpc) -> mp.mpc:
            qv = mp.exp(1j * mp.pi * tv)
            return (mp.pi * mp.jtheta(1, 0, qv, 1) * mp.jtheta(bi, mp.pi * zv, qv)) / (
                mp.jtheta(bi, 0, qv) * mp.jtheta(1, mp.pi * zv, qv)
            )

        def dsz_f(bi: int, zv: mp.mpc, tv: mp.mpc) -> mp.mpc:
            qv = mp.exp(1j * mp.pi * tv)
            c0 = mp.pi * mp.jtheta(1, 0, qv, 1) / mp.jtheta(bi, 0, qv)
            tb = mp.jtheta(bi, mp.pi * zv, qv)
            dtb = mp.pi * mp.jtheta(bi, mp.pi * zv, qv, 1)
            t1 = mp.jtheta(1, mp.pi * zv, qv)
            dt1 = mp.pi * mp.jtheta(1, mp.pi * zv, qv, 1)
            return c0 * (dtb * t1 - tb * dt1) / (t1**2)

        def laurent_c(fn, pwr: int) -> mp.mpc:
            acc = mp.mpc(0)
            for k_c in range(n_c):
                ang = 2 * mp.pi * k_c / n_c
                zv = eps_c * mp.exp(1j * ang)
                acc += (zv**pwr) * fn(zv) * (1j * zv)
            return (acc / 1j) / n_c

        def inv_act(gk: str, zv: mp.mpc, tv: mp.mpc) -> tuple[mp.mpc, mp.mpc, mp.mpc]:
            if gk == "L":
                return zv, tv - 1, mp.mpc(1)
            t_old = tv / (1 - tv)
            eg = mp.sqrt(t_old + 1)
            return (eg**2) * zv, t_old, eg

        def contour_3branch(kind: str) -> dict[str, np.ndarray]:
            out_m: dict[str, np.ndarray] = {}
            for gk in ("L", "R"):
                m3 = np.zeros((3, 3), dtype=complex)
                for col_i, b_src in enumerate(br_ord):
                    bg_p = push_bg(gk, bgs[b_src])
                    hits = [
                        (b_cand, uc)
                        for b_cand in br_ord
                        for _, uc in comp_grp
                        if max(float(np.max(np.abs(uc @ bg_p[k_i] @ uc.conj().T - bgs[b_cand][k_i]))) for k_i in range(4)) < 1e-9
                    ]
                    if len(hits) != 1:
                        raise RuntimeError(f"Expected unique compensator on 124D carrier, got {len(hits)}")
                    b_dst, u_comp = hits[0]
                    row_i = br_ord.index(b_dst)

                    if kind == "proxy_1form":
                        fib = complex(np.vdot(v_top.conj(), u_comp.conj() @ v_top.conj()))
                        num_c = laurent_c(
                            lambda z: sz_f(b_src, inv_act(gk, z, tau_c)[0], inv_act(gk, z, tau_c)[1])
                            * (inv_act(gk, z, tau_c)[2] ** 2),
                            0,
                        )
                        den_c = laurent_c(lambda z: sz_f(b_dst, z, tau_c), 0)
                        m3[row_i, col_i] = fib * complex(num_c / den_c)
                    elif kind == "phi_sp_S5":
                        fib = complex(np.vdot(v_top.conj(), u_comp.conj() @ v_top.conj()))
                        num_c = laurent_c(
                            lambda z: (eta_f(inv_act(gk, z, tau_c)[1]) ** 3)
                            * sz_f(b_src, inv_act(gk, z, tau_c)[0], inv_act(gk, z, tau_c)[1])
                            * (inv_act(gk, z, tau_c)[2] ** 5),
                            0,
                        )
                        den_c = laurent_c(lambda z: (eta_f(tau_c) ** 3) * sz_f(b_dst, z, tau_c), 0)
                        m3[row_i, col_i] = fib * complex(num_c / den_c)
                    elif kind == "a_sp_S_minus3":
                        fib = complex(np.vdot(v_top, u_comp @ v_top))
                        num_c = mp.conj(
                            laurent_c(
                                lambda z: (eta_f(inv_act(gk, z, tau_c)[1]) ** 3)
                                * sz_f(b_src, inv_act(gk, z, tau_c)[0], inv_act(gk, z, tau_c)[1])
                                * (inv_act(gk, z, tau_c)[2] ** 5),
                                0,
                            )
                        )
                        den_c = mp.conj(laurent_c(lambda z: (eta_f(tau_c) ** 3) * sz_f(b_dst, z, tau_c), 0))
                        m3[row_i, col_i] = fib * complex(num_c / den_c)
                    elif kind == "a_dp_S_minus3":
                        fib = complex(np.vdot(v_top, u_comp @ v_top))
                        num_c = mp.conj(
                            laurent_c(
                                lambda z: eta_f(inv_act(gk, z, tau_c)[1])
                                * dsz_f(b_src, inv_act(gk, z, tau_c)[0], inv_act(gk, z, tau_c)[1])
                                * (inv_act(gk, z, tau_c)[2] ** 5),
                                1,
                            )
                        )
                        den_c = mp.conj(laurent_c(lambda z: eta_f(tau_c) * dsz_f(b_dst, z, tau_c), 1))
                        m3[row_i, col_i] = fib * complex(num_c / den_c)
                    elif kind == "psi_spin_S1":
                        ug = gens_f2[gk][2]
                        wp = ug @ (w_spin_br[b_src] @ u_comp.T)
                        fib = complex(np.vdot(w_spin_br[b_dst].reshape(-1), wp.reshape(-1)))
                        _, t_old, eg = inv_act(gk, mp.mpc(0), tau_c)
                        m3[row_i, col_i] = fib * complex(eta_f(t_old) * eg / eta_f(tau_c))
                out_m[gk] = m3
            return out_m

    orders_by_mode: dict[str, int] = {}
    s4_signs_by_mode: dict[str, int] = {}
    mats_by_mode: dict[str, dict[str, np.ndarray]] = {}
    cyc_mats_by_mode: dict[str, tuple[Cyc24Mat, Cyc24Mat]] = {}
    proxy_b3_l2_s: list[int] = []
    max_cyc24_snap_err = 0.0
    float_vs_cyc24_mismatches = 0
    id3_cyc = _cyc24_eye(3)
    neg_id3_cyc = _cyc24_mat_scale(_cyc24_int(-1), id3_cyc)
    for mk in ("proxy_1form", "phi_sp_S5", "a_sp_S_minus3", "a_dp_S_minus3", "psi_spin_S1"):
        gm = contour_3branch(mk)
        mats_by_mode[mk] = gm
        grp_float = _bfs_group(gm)
        l_cyc, err_l = _snap_mat_to_cyc24(gm["L"])
        r_cyc, err_r = _snap_mat_to_cyc24(gm["R"])
        cyc_mats_by_mode[mk] = (l_cyc, r_cyc)
        max_cyc24_snap_err = max(max_cyc24_snap_err, err_l, err_r)
        grp_cyc = _bfs_group_cyc24({"L": l_cyc, "R": r_cyc, "l": _cyc24_mat_dag(l_cyc), "r": _cyc24_mat_dag(r_cyc)})
        if len(grp_float) != len(grp_cyc):
            float_vs_cyc24_mismatches += 1
        orders_by_mode[mk] = len(grp_cyc)
        s_cyc = _cyc24_matmul(_cyc24_matmul(l_cyc, _cyc24_mat_dag(r_cyc)), l_cyc)
        s2_cyc = _cyc24_matmul(s_cyc, s_cyc)
        s4_cyc = _cyc24_matmul(s2_cyc, s2_cyc)
        s4_signs_by_mode[mk] = -1 if s4_cyc == neg_id3_cyc else (1 if s4_cyc == id3_cyc else 0)
        if mk == "proxy_1form":
            l2_cyc = _cyc24_matmul(l_cyc, l_cyc)
            proxy_b3_l2_s = [
                int(round(_cyc24_to_complex(l2_cyc[1][1]).real)),
                int(round(_cyc24_to_complex(s_cyc[1][1]).real)),
            ]

    # D2 fix (F3 + F5 + G6): Exact Q(zeta_24) Hom & unitary intertwiner checks against canonical T_weave and T_weave^*:
    w8_c = _cyc24_pow_zeta(3)
    w8b_c = _cyc24_pow_zeta(21)
    t_weave_l_c: Cyc24Mat = ((w8b_c, _CYC24_ZERO, _CYC24_ZERO), (_CYC24_ZERO, _CYC24_ZERO, w8_c), (_CYC24_ZERO, w8_c, _CYC24_ZERO))
    t_weave_r_c: Cyc24Mat = ((_CYC24_ZERO, w8b_c, _CYC24_ZERO), (w8b_c, _CYC24_ZERO, _CYC24_ZERO), (_CYC24_ZERO, _CYC24_ZERO, w8_c))
    t_weave_bar_l_c: Cyc24Mat = tuple(tuple(_cyc24_conj(x_c) for x_c in row_c) for row_c in t_weave_l_c)
    t_weave_bar_r_c: Cyc24Mat = tuple(tuple(_cyc24_conj(x_c) for x_c in row_c) for row_c in t_weave_r_c)

    hom_weave_to_a_sp, cyc_weave_to_a_sp = _solve_intertwiner_cyc24_fraction(
        (t_weave_l_c, t_weave_r_c), cyc_mats_by_mode["a_sp_S_minus3"]
    )
    hom_weave_conj_to_a_sp, cyc_weave_conj_to_a_sp = _solve_intertwiner_cyc24_fraction(
        (t_weave_bar_l_c, t_weave_bar_r_c), cyc_mats_by_mode["a_sp_S_minus3"]
    )
    hom_weave_to_phi_sp, cyc_weave_to_phi_sp = _solve_intertwiner_cyc24_fraction(
        (t_weave_l_c, t_weave_r_c), cyc_mats_by_mode["phi_sp_S5"]
    )
    hom_phi_sp_to_a_sp, _ = _solve_intertwiner_cyc24_fraction(
        cyc_mats_by_mode["phi_sp_S5"], cyc_mats_by_mode["a_sp_S_minus3"]
    )

    def hom_dim_pair(ma: dict[str, np.ndarray], mb: dict[str, np.ndarray]) -> int:
        id3 = np.eye(3, dtype=complex)
        sys_h = np.vstack(
            [
                np.kron(ma["L"].T, id3) - np.kron(id3, mb["L"]),
                np.kron(ma["R"].T, id3) - np.kron(id3, mb["R"]),
            ]
        )
        sv_h = np.linalg.svd(sys_h, compute_uv=False)
        return int(np.sum(sv_h < 1e-9))

    pairwise_hom_dims = {
        "a_sp_vs_a_dp": hom_dim_pair(mats_by_mode["a_sp_S_minus3"], mats_by_mode["a_dp_S_minus3"]),
        "a_sp_vs_psi_spin": hom_dim_pair(mats_by_mode["a_sp_S_minus3"], mats_by_mode["psi_spin_S1"]),
        "a_dp_vs_psi_spin": hom_dim_pair(mats_by_mode["a_dp_S_minus3"], mats_by_mode["psi_spin_S1"]),
    }
    mode_commutant_dims = {
        mk_c: _joint_commutant_dim([mats_by_mode[mk_c]["L"], mats_by_mode[mk_c]["R"]])
        for mk_c in ("a_sp_S_minus3", "a_dp_S_minus3", "psi_spin_S1")
    }
    z3_m = np.zeros((3, 3), dtype=complex)
    l_9d_m = np.block([
        [mats_by_mode["a_sp_S_minus3"]["L"], z3_m, z3_m],
        [z3_m, mats_by_mode["a_dp_S_minus3"]["L"], z3_m],
        [z3_m, z3_m, mats_by_mode["psi_spin_S1"]["L"]],
    ])
    r_9d_m = np.block([
        [mats_by_mode["a_sp_S_minus3"]["R"], z3_m, z3_m],
        [z3_m, mats_by_mode["a_dp_S_minus3"]["R"], z3_m],
        [z3_m, z3_m, mats_by_mode["psi_spin_S1"]["R"]],
    ])
    end_9d_commutant_dim = _joint_commutant_dim([l_9d_m, r_9d_m])

    return {
        "z4_kernel_pairs": z4_kernel_pairs,
        "z4_kernel_order": len(z4_kernel_pairs),
        "unbroken_so5_dim_h1": unbroken_so5_dim,
        "comp_group_124d_order": len(comp_grp),
        "proxy_b3_stabilizer_L2_S": proxy_b3_l2_s,
        "orders_3branch_by_mode": orders_by_mode,
        "s4_signs_by_mode": s4_signs_by_mode,
        "hom_weave_to_a_sp": hom_weave_to_a_sp,
        "hom_weave_conj_to_a_sp": hom_weave_conj_to_a_sp,
        "hom_weave_to_phi_sp": hom_weave_to_phi_sp,
        "hom_phi_sp_to_a_sp": hom_phi_sp_to_a_sp,
        "exact_cyc24_intertwiners_verified": (
            (hom_weave_to_a_sp, cyc_weave_to_a_sp) == (0, False)
            and (hom_weave_conj_to_a_sp, cyc_weave_conj_to_a_sp) == (1, True)
            and (hom_weave_to_phi_sp, cyc_weave_to_phi_sp) == (1, True)
            and hom_phi_sp_to_a_sp == 0
        ),
        "mode_commutant_dims": mode_commutant_dims,
        "pairwise_hom_dims": pairwise_hom_dims,
        "end_9d_commutant_dim": end_9d_commutant_dim,
        "max_cyc24_snap_err": float(max_cyc24_snap_err),
        "exact_cyc24_orders_match_float": float_vs_cyc24_mismatches == 0 and max_cyc24_snap_err < TOL,
    }


def run_independent_referee_suite() -> dict[str, Any]:
    if "origin_axiom.p753_register_field_join" in sys.modules:
        raise RuntimeError("Guardrail 6 violation: producer module must not be imported in referee script!")
    repo_root = Path(__file__).resolve().parents[1]
    producer_file = repo_root / "src" / "origin_axiom" / "p753_register_field_join.py"
    referee_file = Path(__file__).resolve()

    c1 = check_e8_root_lattice_coroot_identity()
    c2 = check_pauli_clifford_spin10_and_e_theta()
    c3 = check_qseries_and_scrambled_weave_triplet()
    c4 = check_elliptic_contour_pole_filtration()
    c5 = check_z4_kernel_so5_and_3branch_half_form_orders()

    all_pass = (
        c1["n_roots"] == 240
        and c1["total_e8_dim"] == 248
        and c1["all_roots_norm_sq_2"]
        and c1["coroot_phase_equivalence_max_err"] < TOL
        and c1["integer_root_flips"] == 0
        and c1["spinor_root_flips"] == 128
        and c1["singlet_over_triplet_h4_ratio_set"] == [-1.0]
        and c1["a3_adjoint_15_parity_split"] == {"1": 9, "-1": 6}
        and c2["order_2O"] == 48
        and c2["order_St"] == 16
        and c2["order_2O_float_matches_exact"]
        and c2["index_2O_St"] == 3
        and c2["pauli_clifford_scrambled_S_theta_err"] < TOL
        and c2["kpi_minus_total"] == 112
        and c2["klein4_totals"] == {"00": 37, "10": 33, "01": 33, "11": 33}
        and c3["qseries_leading_coeff_quadrature_err"] < TOL
        and c3["exact_weil2_order_cyc24"] == 96
        and c3["exact_odd_m3_order_cyc24"] == 96
        and c3["exact_odd_m3_center_order_cyc24"] == 4
        and c3["scrambled_order_G_V"] == 96
        and c3["scrambled_order_G_T"] == 96
        and c3["scrambled_center_order"] == 4
        and c3["scrambled_S_T_fourth_plus_I_err"] < TOL
        and c3["untwisted_Sym2_Weil2_order"] == 48
        and c3["even_Z24_twist_orders"] == [24, 48, 72, 144]
        and (96 not in c3["even_Z24_twist_orders"])
        and c3["odd_m3_Sym2_Weil2_bar_intertwiner_err"] < TOL
        and c4["filtration_and_swap_verified"]
        and c5["z4_kernel_order"] == 4
        and c5["z4_kernel_pairs"] == [[0, 0], [1, 1], [2, 2], [3, 3]]
        and c5["unbroken_so5_dim_h1"] == 10
        and c5["comp_group_124d_order"] == 16
        and c5["proxy_b3_stabilizer_L2_S"] == [-1, -1]
        and c5["exact_cyc24_orders_match_float"]
        and set(c5["orders_3branch_by_mode"]) == {
            "proxy_1form",
            "phi_sp_S5",
            "a_sp_S_minus3",
            "a_dp_S_minus3",
            "psi_spin_S1",
        }
        and c5["orders_3branch_by_mode"]["proxy_1form"] == 24
        and c5["orders_3branch_by_mode"]["phi_sp_S5"] == 96
        and c5["orders_3branch_by_mode"]["a_sp_S_minus3"] == 96
        and c5["orders_3branch_by_mode"]["a_dp_S_minus3"] - 128 == 160
        and c5["orders_3branch_by_mode"]["psi_spin_S1"] == 72
        and c5["s4_signs_by_mode"] == {
            "proxy_1form": 1,
            "phi_sp_S5": -1,
            "a_sp_S_minus3": -1,
            "a_dp_S_minus3": -1,
            "psi_spin_S1": -1,
        }
        and c5["hom_weave_to_a_sp"] == 0
        and c5["hom_weave_conj_to_a_sp"] == 1
        and c5["hom_weave_to_phi_sp"] == 1
        and c5["hom_phi_sp_to_a_sp"] == 0
        and c5["exact_cyc24_intertwiners_verified"]
        and c5["mode_commutant_dims"] == {
            "a_sp_S_minus3": 1,
            "a_dp_S_minus3": 1,
            "psi_spin_S1": 2,
        }
        and c5["pairwise_hom_dims"] == {
            "a_sp_vs_a_dp": 0,
            "a_sp_vs_psi_spin": 0,
            "a_dp_vs_psi_spin": 0,
        }
        and c5["end_9d_commutant_dim"] == 4
    )

    return {
        "zero_producer_imports": "origin_axiom.p753_register_field_join" not in sys.modules,
        "all_independent_checks_pass": all_pass,
        "metadata": {
            "producer_sha256": hashlib.sha256(producer_file.read_bytes()).hexdigest(),
            "referee_sha256": hashlib.sha256(referee_file.read_bytes()).hexdigest(),
            "python_version": platform.python_version(),
            "platform": f"{platform.system()}-{platform.machine()}",
        },
        "check1_e8_root_lattice_coroot": c1,
        "check2_pauli_clifford_scrambled_e_theta": c2,
        "check3_qseries_and_scrambled_cocycle": c3,
        "check4_cauchy_contour_pole_filtration": c4,
        "check5_z4_so5_and_3branch_half_form_orders": c5,
    }


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    out_dir = repo_root / "relays" / "p753_verification"
    out_dir.mkdir(parents=True, exist_ok=True)

    receipt = run_independent_referee_suite()
    json_path = out_dir / "p753_referee_receipt.json"
    txt_path = out_dir / "p753_referee_run.txt"

    json_text = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    json_path.write_text(json_text, encoding="utf-8")

    summary_lines = [
        "P-753 / R77-2 (WP-2.2 & WP-3.2) Independent Zero-Trust Referee Run",
        "===================================================================",
        f"Zero producer imports (Guardrail 6): {receipt['zero_producer_imports']}",
        f"All independent checks PASS:         {receipt['all_independent_checks_pass']}",
        f"Producer SHA256:                     {receipt['metadata']['producer_sha256']}",
        f"Referee SHA256:                      {receipt['metadata']['referee_sha256']}",
        f"Python / Platform:                   {receipt['metadata']['python_version']} ({receipt['metadata']['platform']})",
        f"E8 root lattice dim (240 + 8):       {receipt['check1_e8_root_lattice_coroot']['total_e8_dim']}",
        f"E8 (Spin10 x Spin6)/Z_4 kernel ord:  {receipt['check5_z4_so5_and_3branch_half_form_orders']['z4_kernel_order']} ({receipt['check5_z4_so5_and_3branch_half_form_orders']['z4_kernel_pairs']})",
        f"Disconnected h1 so(5) centralizer:   {receipt['check5_z4_so5_and_3branch_half_form_orders']['unbroken_so5_dim_h1']} vs u(3)=9",
        f"Coroot -h4 == zeta_Spin10*(+h4) err: {receipt['check1_e8_root_lattice_coroot']['coroot_phase_equivalence_max_err']:.3e}",
        f"Singlet/triplet h4 ratio (+-h4):     {receipt['check1_e8_root_lattice_coroot']['singlet_over_triplet_h4_ratio_set']}",
        f"Pauli Cl(10) scrambled S_theta err:  {receipt['check2_pauli_clifford_scrambled_e_theta']['pauli_clifford_scrambled_S_theta_err']:.3e}",
        f"248D Klein-4 totals (112; 136):      kpi_minus={receipt['check2_pauli_clifford_scrambled_e_theta']['kpi_minus_total']}, k4={receipt['check2_pauli_clifford_scrambled_e_theta']['klein4_totals']}",
        f"q-series leading coeff quadrature:   {receipt['check3_qseries_and_scrambled_cocycle']['qseries_leading_coeff_quadrature_err']:.3e}",
        f"Scrambled |G_T| / untwisted Sym^2:   {receipt['check3_qseries_and_scrambled_cocycle']['scrambled_order_G_T']} vs {receipt['check3_qseries_and_scrambled_cocycle']['untwisted_Sym2_Weil2_order']}",
        f"Even Z_24 twist orders:              {receipt['check3_qseries_and_scrambled_cocycle']['even_Z24_twist_orders']}",
        f"Odd m=3 Sym^2(Weil_2^*) intertwiner: {receipt['check3_qseries_and_scrambled_cocycle']['odd_m3_Sym2_Weil2_bar_intertwiner_err']:.3e}",
        f"Contour S^-3 shear & comm(11,00,v6): {receipt['check4_cauchy_contour_pole_filtration']['physical_s_minus3_offdiag_shear_err']:.3e}, ({receipt['check4_cauchy_contour_pole_filtration']['chi11_aslot_joint_commutant_dim']}, {receipt['check4_cauchy_contour_pole_filtration']['chi00_aslot_joint_commutant_dim']}, {receipt['check4_cauchy_contour_pole_filtration']['vector_six_aslot_joint_commutant_dim']})",
        f"3-branch orders (proxy; S5,S-3,S1):  {receipt['check5_z4_so5_and_3branch_half_form_orders']['orders_3branch_by_mode']}",
        "0 of 19.",
    ]
    txt_out = "\n".join(summary_lines) + "\n"
    txt_path.write_text(txt_out, encoding="utf-8")
    print(txt_out, end="")
    if not receipt["all_independent_checks_pass"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
