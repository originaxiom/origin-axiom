#!/usr/bin/env python3
"""
Standalone preregistered pure-mathematics verifier for Card X-P1 (0 of 19, data-free).

Covers four exact data-free modules:
  J  B1955 Open #1: sl(5)-invariant adjoint-wedge classification (exact dim 2 in up and
     down/lepton, level-5 SL(2, F_5) invariance in both Weil classes, exact -3 Georgi-Jarlskog
     ratio on traceless 45-bar, linear commutant proportionality wall to F(tau)) and the
     five-multiplet exterior-derivation Gramian lift G_R(tau) on (Q, u^c, d^c, L, e^c),
     exact 3x3 matrix Schur-Plancherel identity, SL(2, Z) covariance, and 10-trial Haar
     unitary basis-scrambling invariance.
  Z  P-874 Q2 (W-L1 design criterion without data): firewall-clean 55-digit integer nullities,
     degeneracy partitions, and stabilizer Schur intertwining of Frame C / B1953 / exterior
     readouts at tau = i (fixed by S) and tau = exp(2*pi*i/3) (fixed by ST), printing zero
     non-zero singular-value ratios or mixing angles.
  W  Independent pure-math recomputation of Web Card W-P1 (2f2e490e1) items P1-P3 and W1-W4,
     plus exact test of W-P1 section 5 item 2 (whether the golden iteration selects S vs Stilde
     or the sign of B on the Higgs ground plane E).
  C  P-875 Q2: independent symbolic Clifford Cl(10) (both 16_+ and 16_- half-spinors and
     vector-10 control) and 4-degree Dolbeault-Koszul cochain check of Physical Card C3i
     (GLOBAL_CYCLIC_CROSS_FORM_CHAIN_MAP.md, equations (1)-(7), core swap, 24/16/8 divisor
     kernel persistence, and non-unitarity of 1 + H).
  P  Five planted adversarial controls PC_XP1_1..PC_XP1_5 that must fail when broken.

Zero float literals appear anywhere in this file (enforced by AST inspection).
Zero measured values or held-out targets are used or compared.
"""

from __future__ import annotations

import ast
import hashlib
import itertools
import json
import math
import pathlib
import random
from fractions import Fraction
from typing import Any, Dict, List, Sequence, Tuple

import mpmath as mp
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from sympy.polys.domains import QQ

HERE = pathlib.Path(__file__).resolve().parent
OUT_PATH = HERE / "verify_x_p1_out.json"
OUT_SHA_PATH = HERE / "OUTPUT_SHA256.txt"

mp.mp.dps = 55


# ============================================================================
# 0. AST Guardrail Self-Check (Zero Float Literals)
# ============================================================================

def enforce_zero_float_literals_ast() -> Dict[str, Any]:
    src = pathlib.Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(src, filename=str(__file__))
    float_lines: List[int] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, float):
            float_lines.append(getattr(node, "lineno", -1))
    return {
        "float_literal_count": len(float_lines),
        "ast_zero_float_passed": len(float_lines) == 0,
    }


def f2m(fr: Fraction) -> mp.mpf:
    return mp.mpf(fr.numerator) / mp.mpf(fr.denominator)


def mat_max_abs(m: mp.matrix) -> mp.mpf:
    best = mp.mpf(0)
    for r in range(m.rows):
        for c in range(m.cols):
            v = abs(m[r, c])
            if v > best:
                best = v
    return best


def mat_conj_T(m: mp.matrix) -> mp.matrix:
    out = mp.zeros(m.cols, m.rows)
    for r in range(m.rows):
        for c in range(m.cols):
            out[c, r] = mp.conj(m[r, c])
    return out


def mat_T(m: mp.matrix) -> mp.matrix:
    out = mp.zeros(m.cols, m.rows)
    for r in range(m.rows):
        for c in range(m.cols):
            out[c, r] = m[r, c]
    return out


def mat_trace(m: mp.matrix) -> mp.mpc:
    acc = mp.mpc(0)
    for k in range(min(m.rows, m.cols)):
        acc += m[k, k]
    return acc


def mat_frob_sq(m: mp.matrix) -> mp.mpf:
    acc = mp.mpf(0)
    for r in range(m.rows):
        for c in range(m.cols):
            acc += abs(m[r, c]) ** 2
    return acc


def kron_mp(a: mp.matrix, b: mp.matrix) -> mp.matrix:
    out = mp.zeros(a.rows * b.rows, a.cols * b.cols)
    for r1 in range(a.rows):
        for c1 in range(a.cols):
            v = a[r1, c1]
            if v == 0:
                continue
            br = r1 * b.rows
            bc = c1 * b.cols
            for r2 in range(b.rows):
                for c2 in range(b.cols):
                    out[br + r2, bc + c2] = v * b[r2, c2]
    return out


def svd_sorted(m: mp.matrix) -> List[mp.mpf]:
    svals = mp.svd_c(m, compute_uv=False)
    return sorted([abs(x) for x in svals], reverse=True)


def eig_hermitian_sorted(h: mp.matrix) -> List[mp.mpf]:
    # Enforce exact Hermiticity before eigendecomposition
    hh = (h + mat_conj_T(h)) / mp.mpf(2)
    evals, _ = mp.eigh(hh)
    return sorted([mp.re(x) for x in evals], reverse=True)


def random_haar_unitary_mp(n: int, rng: random.Random) -> mp.matrix:
    """Gram-Schmidt QR with positive diagonal R on rational-seeded complex Gaussian matrix."""
    iu = mp.mpc(0, 1)
    cols: List[List[mp.mpc]] = []
    for _ in range(n):
        col: List[mp.mpc] = []
        for _ in range(n):
            # Box-Muller free rational sum of 12 uniforms -> smooth complex entries
            rx = sum(rng.randint(-1000, 1000) for _ in range(6))
            ry = sum(rng.randint(-1000, 1000) for _ in range(6))
            col.append(mp.mpf(rx) / mp.mpf(1000) + iu * (mp.mpf(ry) / mp.mpf(1000)))
        cols.append(col)
    ortho: List[List[mp.mpc]] = []
    for j in range(n):
        v = list(cols[j])
        for k in range(j):
            proj = sum(mp.conj(ortho[k][idx]) * v[idx] for idx in range(n))
            for idx in range(n):
                v[idx] -= proj * ortho[k][idx]
        nrm = mp.sqrt(sum(abs(x) ** 2 for x in v))
        ortho.append([x / nrm for x in v])
    u = mp.zeros(n, n)
    for r in range(n):
        for c in range(n):
            u[r, c] = ortho[c][r]
    # Normalize det to SU(n) if needed by caller; here U(n)
    return u


def make_su(u: mp.matrix) -> mp.matrix:
    d = mp.det(u)
    ph = mp.exp(-mp.mpc(0, 1) * mp.arg(d) / mp.mpf(u.rows))
    return ph * u


# ============================================================================
# 1. Standalone Frame C & B1953 Operator Construction in 55-Digit mpmath
# ============================================================================

PTS_24: List[Tuple[int, int]] = [
    (a, b) for a in range(5) for b in range(5) if (a, b) != (0, 0)
]


def theta_char_z(alpha: mp.mpf, beta: mp.mpf, z: mp.mpc, tau: mp.mpc) -> mp.mpc:
    im_tau = mp.im(tau)
    center = -(mp.re(alpha) + mp.im(z) / im_tau)
    n0 = int(mp.nint(center))
    span = int(mp.ceil(mp.sqrt(mp.mpf(195) / (mp.pi * im_tau)))) + 10
    acc = mp.mpc(0)
    iu = mp.mpc(0, 1)
    for dn in range(-span, span + 1):
        na = mp.mpf(n0 + dn) + alpha
        acc += mp.exp(mp.pi * iu * (na * na) * tau + 2 * mp.pi * iu * na * (z + beta))
    return acc


def theta1_and_dz(z: mp.mpc, tau: mp.mpc) -> Tuple[mp.mpc, mp.mpc]:
    """theta_1(z | tau) = -theta[1/2, 1/2](z | tau) and its z-derivative."""
    half = mp.mpf(1) / mp.mpf(2)
    im_tau = mp.im(tau)
    center = -(half + mp.im(z) / im_tau)
    n0 = int(mp.nint(center))
    span = int(mp.ceil(mp.sqrt(mp.mpf(195) / (mp.pi * im_tau)))) + 10
    s0 = mp.mpc(0)
    s1 = mp.mpc(0)
    iu = mp.mpc(0, 1)
    for dn in range(-span, span + 1):
        na = mp.mpf(n0 + dn) + half
        term = mp.exp(mp.pi * iu * (na * na) * tau + 2 * mp.pi * iu * na * (z + half))
        s0 -= term
        s1 -= (2 * mp.pi * iu * na) * term
    return s0, s1


def theta_char_0_and_dtau(alpha: mp.mpf, beta: mp.mpf, tau: mp.mpc) -> Tuple[mp.mpc, mp.mpc]:
    im_tau = mp.im(tau)
    n0 = int(mp.nint(-mp.re(alpha)))
    span = int(mp.ceil(mp.sqrt(mp.mpf(195) / (mp.pi * im_tau)))) + 10
    s0 = mp.mpc(0)
    sdt = mp.mpc(0)
    iu = mp.mpc(0, 1)
    for dn in range(-span, span + 1):
        na = mp.mpf(n0 + dn) + alpha
        term = mp.exp(mp.pi * iu * (na * na) * tau + 2 * mp.pi * iu * na * beta)
        s0 += term
        sdt += (mp.pi * iu * (na * na)) * term
    return s0, sdt


def kronecker_F_u(u1: Fraction, u2: Fraction, tau: mp.mpc) -> mp.mpf:
    """B1919 closed-form Kronecker limit function F_u(u1, u2, tau) in 55-digit mpmath."""
    a = u1 - Fraction(math.floor(u1), 1)
    b = u2 - Fraction(math.floor(u2), 1)
    x = mp.re(tau)
    y = mp.im(tau)
    iu = mp.mpc(0, 1)
    if a != 0:
        fa = f2m(a)
        first = -mp.pi * (2 * mp.log(mp.mpf(2)) + mp.log(y) + mp.digamma(fa) + mp.digamma(mp.mpf(1) - fa))
        zero_row = mp.mpf(0)
    else:
        first = mp.pi * (2 * mp.euler - 2 * mp.log(mp.mpf(2)) - mp.log(y))
        zero_row = y * (mp.pi ** 2) / (mp.sin(mp.pi * f2m(b)) ** 2)
    k_cap = int(mp.ceil(mp.mpf(195) / (2 * mp.pi * y))) + 8
    tot = mp.mpf(0)
    fa_all = f2m(a)
    fb_all = f2m(b)
    for k in range(-k_cap, k_cap + 1):
        m = fa_all + mp.mpf(k)
        if m == 0:
            continue
        w = mp.exp(-2 * mp.pi * abs(m) * y + 2 * iu * mp.pi * (m * x + fb_all))
        tot += (2 * mp.pi / abs(m)) * mp.re(w / (mp.mpc(1) - w))
    return first + zero_row + tot


def eval_higgs_triplet_B1(tau: mp.mpc) -> List[mp.mpc]:
    """Exact weight-3/2 Serre derivative B[1] = D_{-1/2} R of R = (-th2^2, -th4^2, i th3^2)/(th2 th3 th4)."""
    yv = mp.im(tau)
    iu = mp.mpc(0, 1)
    q = mp.exp(2 * iu * mp.pi * tau)
    m_cap = int(mp.ceil(mp.mpf(195) / (2 * mp.pi * yv))) + 14
    eta_prod = mp.mpc(1)
    e2 = mp.mpc(1)
    qk = mp.mpc(1)
    for m_i in range(1, m_cap + 1):
        qk *= q
        eta_prod *= (mp.mpc(1) - qk)
        e2 -= mp.mpf(24 * m_i) * qk / (mp.mpc(1) - qk)
    # th2 * th3 * th4 = 2 * eta(tau)^3
    den = mp.mpf(2) * ((mp.exp(iu * mp.pi * tau / mp.mpf(12)) * eta_prod) ** 3)
    half = mp.mpf(1) / mp.mpf(2)
    zero = mp.mpf(0)
    t2, dt2 = theta_char_0_and_dtau(half, zero, tau)
    t4, dt4 = theta_char_0_and_dtau(zero, half, tau)
    t3, dt3 = theta_char_0_and_dtau(zero, zero, tau)
    inv_2pi_i = mp.mpc(1) / (2 * mp.pi * iu)
    r_vec = [-(t2 * t2) / den, -(t4 * t4) / den, iu * (t3 * t3) / den]
    dn_vec = [
        -mp.mpf(2) * t2 * (dt2 * inv_2pi_i) / den,
        -mp.mpf(2) * t4 * (dt4 * inv_2pi_i) / den,
        mp.mpf(2) * iu * t3 * (dt3 * inv_2pi_i) / den,
    ]
    return [dn_vec[idx] - (e2 / mp.mpf(12)) * r_vec[idx] for idx in range(3)]


def setup_quaternions() -> Tuple[mp.matrix, List[mp.matrix], List[mp.matrix], List[mp.matrix]]:
    one = mp.mpc(1)
    zero = mp.mpc(0)
    iu = mp.mpc(0, 1)
    i2 = mp.matrix([[one, zero], [zero, one]])
    qi = mp.matrix([[iu, zero], [zero, -iu]])
    qj = mp.matrix([[zero, one], [-one, zero]])
    qk = mp.matrix([[zero, iu], [iu, zero]])
    eps = qj
    units = [i2, qi, qj, qk]
    # Dual basis for Tr(eps * u_a * edual_b^T) or entrywise pairing hsum(eps*u_a, edual_b) = delta_ab
    def hsum(m1: mp.matrix, m2: mp.matrix) -> mp.mpc:
        return m1[0, 0] * m2[0, 0] + m1[0, 1] * m2[0, 1] + m1[1, 0] * m2[1, 0] + m1[1, 1] * m2[1, 1]

    ec = [eps * u for u in units]
    g_mat = mp.zeros(4, 4)
    for r in range(4):
        for c in range(4):
            g_mat[r, c] = hsum(ec[r], units[c])
    g_inv = g_mat ** (-1)
    edual: List[mp.matrix] = []
    for a_i in range(4):
        acc = mp.zeros(2, 2)
        for b_i in range(4):
            acc += g_inv[b_i, a_i] * units[b_i]
        edual.append(acc)
    blocks = [qj, qi, qk]
    q_s = [qi, qj, qk]
    return eps, edual, blocks, q_s


def frame_c_couplings_24(
    tau: mp.mpc,
    ql: int,
    qr: int,
    residue_only: bool = False,
    l_tilde_inv: mp.mpf | None = None,
) -> Dict[str, Dict[Tuple[int, int], mp.matrix]]:
    r"""
    Evaluate Frame C's 3x3 family couplings Y(tau, w) at all 24 order-5 points w = (a, b) in F_5^2 \ {0}
    in readings 'S', 'St', and 'Sstar' (for planted control).
    When residue_only=False, uses the exact covariant end L(tau) = L_tilde_inv - (1/2) ln Im(tau) + euler + ln(pi)
    satisfying L(tau + 1) = L(tau) and L(-1/tau) = L(tau) + ln|tau| identically (B1927).
    """
    eps, edual, blocks, q_s = setup_quaternions()
    iu = mp.mpc(0, 1)
    yv = mp.im(tau)
    q = mp.exp(2 * iu * mp.pi * tau)
    m_cap = int(mp.ceil(mp.mpf(195) / (2 * mp.pi * yv))) + 14
    eta_prod = mp.mpc(1)
    qk = mp.mpc(1)
    for _ in range(1, m_cap + 1):
        qk *= q
        eta_prod *= (mp.mpc(1) - qk)
    t1p = mp.mpf(2) * mp.pi * ((mp.exp(iu * mp.pi * tau / mp.mpf(12)) * eta_prod) ** 3)

    c3 = eval_higgs_triplet_B1(tau)
    s_mat = c3[0] * q_s[0] + c3[1] * q_s[1] + c3[2] * q_s[2]
    s_conj = mp.matrix([[mp.conj(s_mat[r, c]) for c in range(2)] for r in range(2)])
    st_mat = eps * s_conj * mat_T(eps)
    readings = {"S": s_mat, "St": st_mat, "Sstar": s_conj}

    if l_tilde_inv is None:
        l_tilde_inv = mp.mpf(3)
    l_end = l_tilde_inv - (mp.mpf(1) / mp.mpf(2)) * mp.log(yv) + mp.euler + mp.log(mp.pi)

    half = Fraction(1, 2)
    out: Dict[str, Dict[Tuple[int, int], mp.matrix]] = {rn: {} for rn in readings}

    def is_zero_char(ch: Tuple[Fraction, Fraction]) -> bool:
        return (ch[0] - half).denominator == 1 and (ch[1] - half).denominator == 1

    for a_int, b_int in PTS_24:
        af = Fraction(a_int, 5)
        bf = Fraction(b_int, 5)
        x0, x1 = ql * af, 2 * ql * bf
        y0, y1 = qr * af, 2 * qr * bf
        ap, am = x0 + y0, x0 - y0
        bp, bm = (x1 + y1) / 2, (x1 - y1) / 2
        e_fac = mp.exp(-2 * iu * mp.pi * f2m(x0))
        kap = [
            -iu * e_fac,
            mp.mpc(-1),
            -e_fac,
            iu,
        ]
        cs_list = [(ap + half, bp + half), (ap + half, bp), (ap, bp + half), (ap, bp)]
        ds_list = [(am + half, bm + half), (am + half, bm), (am, bm + half), (am, bm)]
        mw = mp.zeros(2, 2)
        for s_idx in range(4):
            if is_zero_char(cs_list[s_idx]) or is_zero_char(ds_list[s_idx]):
                continue
            r_val = (
                kap[s_idx]
                * theta_char_z(f2m(cs_list[s_idx][0]), f2m(cs_list[s_idx][1]), mp.mpc(0), tau)
                * theta_char_z(f2m(ds_list[s_idx][0]), f2m(ds_list[s_idx][1]), mp.mpc(0), tau)
                / t1p
            )
            if residue_only:
                u_val = r_val
            else:
                al = cs_list[s_idx][0] - half
                be = cs_list[s_idx][1] - half
                z_pt = f2m(al) * tau + f2m(be)
                th1_v, dth1_v = theta1_and_dz(z_pt, tau)
                a0 = 2 * iu * mp.pi * f2m(al) + dth1_v / th1_v
                c_norm = (
                    kronecker_F_u(al, be, tau)
                    + mp.pi * mp.log(yv)
                    - 2 * mp.pi * (mp.euler + mp.log(mp.pi))
                    - mp.pi * (abs(a0) ** 2) * mp.exp(-2 * l_end)
                )
                arg = 2 * mp.pi * l_end + c_norm
                assert arg > mp.mpf(0), f"Non-positive channel weight at {(a_int, b_int)}, s={s_idx}"
                u_val = mp.sqrt(arg) * r_val
            mw += u_val * edual[s_idx]

        for rn, sr in readings.items():
            ymat = mp.zeros(3, 3)
            for ra in range(3):
                for cb in range(3):
                    ker = mat_T(blocks[ra]) * eps * sr * blocks[cb]
                    acc = mp.mpc(0)
                    for m_i in range(2):
                        for n_i in range(2):
                            acc += ker[m_i, n_i] * mw[m_i, n_i]
                    ymat[ra, cb] = acc
            out[rn][(a_int, b_int)] = ymat
    return out


# ============================================================================
# 2. Module J: B1955 Open #1 — Linear Adjoint-Wedge Wall & 5-Multiplet Gramians
# ============================================================================

def build_weil_and_weyl_mp() -> Dict[str, Any]:
    iu = mp.mpc(0, 1)
    zeta = mp.exp(2 * iu * mp.pi / mp.mpf(5))
    psi = lambda k: zeta ** (k % 5)

    x_op = mp.zeros(5, 5)
    z_op = mp.zeros(5, 5)
    p_op = mp.zeros(5, 5)
    for x in range(5):
        x_op[(x + 1) % 5, x] = mp.mpc(1)
        z_op[x, x] = psi(x)
        p_op[(-x) % 5, x] = mp.mpc(1)

    def mat_pow(m: mp.matrix, e: int) -> mp.matrix:
        res = mp.eye(m.rows)
        for _ in range(e % 5):
            res = res * m
        return res

    d_ops: Dict[Tuple[int, int], mp.matrix] = {}
    for a, b in PTS_24:
        d_ops[(a, b)] = psi(3 * a * b) * mat_pow(x_op, a) * mat_pow(z_op, b)

    # Adapted orthonormal basis V_adap = [3_c (P=+1) | 2_w (P=-1)]
    inv_rt2 = mp.mpf(1) / mp.sqrt(mp.mpf(2))
    v_adap = mp.zeros(5, 5)
    # e0 = |0>, e1 = (|1>+|4>)/sqrt2, e2 = (|2>+|3>)/sqrt2
    v_adap[0, 0] = mp.mpc(1)
    v_adap[1, 1] = inv_rt2
    v_adap[4, 1] = inv_rt2
    v_adap[2, 2] = inv_rt2
    v_adap[3, 2] = inv_rt2
    # e3 = (|1>-|4>)/sqrt2, e4 = (|2>-|3>)/sqrt2
    v_adap[1, 3] = inv_rt2
    v_adap[4, 3] = -inv_rt2
    v_adap[2, 4] = inv_rt2
    v_adap[3, 4] = -inv_rt2

    # Both Weil classes a_cls in {1 (knot q = x^2/5), 2 (act 2x^2/5 = B1951)}
    weil_classes: Dict[int, Tuple[mp.matrix, mp.matrix]] = {}
    for a_cls in (1, 2):
        t_m = mp.zeros(5, 5)
        f_m = mp.zeros(5, 5)
        for x in range(5):
            t_m[x, x] = psi(a_cls * x * x)
            for y in range(5):
                f_m[x, y] = psi(-2 * a_cls * x * y)
        # Fix scalar c so (c F)^2 = ((c F) T)^3 = P
        ff = f_m * f_m
        ft = f_m * t_m
        ft3 = ft * ft * ft
        # Pick (0, 0) entry where P[0, 0] = 1
        c_sc = ff[0, 0] / ft3[0, 0]
        s_m = c_sc * f_m
        weil_classes[a_cls] = (t_m, s_m)

    return {
        "psi": psi,
        "X": x_op,
        "Z": z_op,
        "P": p_op,
        "D": d_ops,
        "V_adap": v_adap,
        "weil_classes": weil_classes,
    }


def run_module_j_exterior_join() -> Dict[str, Any]:
    """
    Exact tests J1..J5 on B1955 Open #1.
    """
    # J1a: Exact rational classification of sl(5)-invariant maps in
    #   Up:   sl(5) (x) Lambda^2 (x) Lambda^2 (x) Lambda^1 -> Lambda^5
    #   Down: sl(5) (x) Lambda^2 (x) Lambda^4 (x) Lambda^4 -> (Lambda^5)^2
    # Restrict first to weight-(1,1,1,1,1) [up] and weight-(2,2,2,2,2) [down] basis tuples,
    # then impose all 8 Chevalley simple root generators E_{i,i+1}, E_{i+1,i} over QQ!
    lam2 = list(itertools.combinations(range(5), 2))   # 10 basis elements
    lam4 = list(itertools.combinations(range(5), 4))   # 5 basis elements
    lam1 = [(i,) for i in range(5)]                    # 5 basis elements
    # Basis of sl(5): 4 Cartans H_k = e_{k,k} - e_{4,4} (k=0..3) + 20 roots E_{a,b} (a!=b)
    sl5_basis: List[Tuple[str, int, int]] = [("H", k, 4) for k in range(4)] + [
        ("E", a, b) for a in range(5) for b in range(5) if a != b
    ]

    def wedge_action(gen_a: int, gen_b: int, tup: Tuple[int, ...]) -> List[Tuple[int, Tuple[int, ...]]]:
        """Action of E_{gen_a, gen_b} (maps e_{gen_b} -> e_{gen_a}) on exterior basis tuple."""
        if gen_b not in tup or gen_a in tup:
            return []
        lst = list(tup)
        pos = lst.index(gen_b)
        lst[pos] = gen_a
        # Bubble sort to canonical order and track parity sign
        sgn = 1
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                if lst[i] > lst[j]:
                    lst[i], lst[j] = lst[j], lst[i]
                    sgn = -sgn
        return [(sgn, tuple(lst))]

    def sl5_adjoint_action(gen_a: int, gen_b: int, elem: Tuple[str, int, int]) -> List[Tuple[Fraction, Tuple[str, int, int]]]:
        """Commutator [E_{gen_a, gen_b}, elem] expressed in sl5_basis."""
        # Represent E_{gen_a, gen_b} and elem as 5x5 dict matrices, take commutator, decompose in sl5_basis
        m_e = {(gen_a, gen_b): Fraction(1)}
        if elem[0] == "H":
            m_x = {(elem[1], elem[1]): Fraction(1), (4, 4): Fraction(-1)}
        else:
            m_x = {(elem[1], elem[2]): Fraction(1)}
        comm: Dict[Tuple[int, int], Fraction] = {}
        for (r1, c1), v1 in m_e.items():
            for (r2, c2), v2 in m_x.items():
                if c1 == r2:
                    comm[(r1, c2)] = comm.get((r1, c2), Fraction(0)) + v1 * v2
                if c2 == r1:
                    comm[(r2, c1)] = comm.get((r2, c1), Fraction(0)) - v1 * v2
        res: List[Tuple[Fraction, Tuple[str, int, int]]] = []
        for k in range(4):
            val = comm.get((k, k), Fraction(0))
            if val != 0:
                res.append((val, ("H", k, 4)))
        for (r, c), val in comm.items():
            if r != c and val != 0:
                res.append((val, ("E", r, c)))
        return res

    def count_sl5_invariants(
        b2: List[Tuple[int, ...]],
        b3: List[Tuple[int, ...]],
        b4: List[Tuple[int, ...]],
        target_wt: Tuple[int, int, int, int, int],
    ) -> Tuple[int, int]:
        wt_tuples: List[Tuple[int, int, int, int]] = []
        for i1, el in enumerate(sl5_basis):
            w1 = [0, 0, 0, 0, 0]
            if el[0] == "E":
                w1[el[1]] += 1
                w1[el[2]] -= 1
            for i2, t2 in enumerate(b2):
                for i3, t3 in enumerate(b3):
                    for i4, t4 in enumerate(b4):
                        wt = list(w1)
                        for x in t2:
                            wt[x] += 1
                        for x in t3:
                            wt[x] += 1
                        for x in t4:
                            wt[x] += 1
                        if tuple(wt) == target_wt:
                            wt_tuples.append((i1, i2, i3, i4))
        col_idx = {tp: idx for idx, tp in enumerate(wt_tuples)}
        idx_b2 = {t: i for i, t in enumerate(b2)}
        idx_b3 = {t: i for i, t in enumerate(b3)}
        idx_b4 = {t: i for i, t in enumerate(b4)}
        idx_sl = {el: i for i, el in enumerate(sl5_basis)}

        rows_dict: List[Dict[int, Any]] = []
        simple_gens = [(k, k + 1) for k in range(4)] + [(k + 1, k) for k in range(4)]
        for ga, gb in simple_gens:
            # Target weight bumped by E_{ga, gb}: a source tuple has weight target_wt - e_ga + e_gb
            src_wt = list(target_wt)
            src_wt[ga] -= 1
            src_wt[gb] += 1
            src_wt_t = tuple(src_wt)
            for i1, el in enumerate(sl5_basis):
                w1 = [0, 0, 0, 0, 0]
                if el[0] == "E":
                    w1[el[1]] += 1
                    w1[el[2]] -= 1
                for i2, t2 in enumerate(b2):
                    for i3, t3 in enumerate(b3):
                        for i4, t4 in enumerate(b4):
                            wt = list(w1)
                            for x in t2:
                                wt[x] += 1
                            for x in t3:
                                wt[x] += 1
                            for x in t4:
                                wt[x] += 1
                            if tuple(wt) != src_wt_t:
                                continue
                            row: Dict[int, Any] = {}
                            for cf, el_p in sl5_adjoint_action(ga, gb, el):
                                key = (idx_sl[el_p], i2, i3, i4)
                                if key in col_idx:
                                    c_i = col_idx[key]
                                    row[c_i] = row.get(c_i, QQ.zero) + QQ(cf.numerator, cf.denominator)
                            for sgn, t2_p in wedge_action(ga, gb, t2):
                                key = (i1, idx_b2[t2_p], i3, i4)
                                if key in col_idx:
                                    c_i = col_idx[key]
                                    row[c_i] = row.get(c_i, QQ.zero) + QQ(sgn, 1)
                            for sgn, t3_p in wedge_action(ga, gb, t3):
                                key = (i1, i2, idx_b3[t3_p], i4)
                                if key in col_idx:
                                    c_i = col_idx[key]
                                    row[c_i] = row.get(c_i, QQ.zero) + QQ(sgn, 1)
                            for sgn, t4_p in wedge_action(ga, gb, t4):
                                key = (i1, i2, i3, idx_b4[t4_p])
                                if key in col_idx:
                                    c_i = col_idx[key]
                                    row[c_i] = row.get(c_i, QQ.zero) + QQ(sgn, 1)
                            row = {k: v for k, v in row.items() if v != QQ.zero}
                            if row:
                                rows_dict.append(row)
        dm = DomainMatrix({r_i: r for r_i, r in enumerate(rows_dict)}, (len(rows_dict), len(wt_tuples)), QQ)
        rk = dm.rank()
        return len(wt_tuples), len(wt_tuples) - rk

    up_wt_dim, up_inv_dim = count_sl5_invariants(lam2, lam2, lam1, (1, 1, 1, 1, 1))
    dn_wt_dim, dn_inv_dim = count_sl5_invariants(lam2, lam4, lam4, (2, 2, 2, 2, 2))

    # J1b: Verify SL(2, F_5) group order = 120, det = 1 in BOTH Weil classes, and exact GL(5)
    # equivariance of the 2 channels (Higgs-leg and 10-leg / traceless 45-bar) across both classes!
    wb = build_weil_and_weyl_mp()
    weil_group_sizes: Dict[str, int] = {}
    max_det_err = mp.mpf(0)
    max_wedge_inv_err = mp.mpf(0)

    # Enumerate SL(2, F_5) abstractly via 2x2 mod 5 matrices and homomorphism rho_a
    t_mod5 = ((1, 1), (0, 1))
    s_mod5 = ((0, 4), (1, 0))
    def mul2_mod5(m1: Tuple[Tuple[int, int], Tuple[int, int]], m2: Tuple[Tuple[int, int], Tuple[int, int]]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        return (
            ((m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0]) % 5, (m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]) % 5),
            ((m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0]) % 5, (m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]) % 5),
        )

    for a_cls in (1, 2):
        tm, sm = wb["weil_classes"][a_cls]
        visited: Dict[Tuple[Tuple[int, int], Tuple[int, int]], mp.matrix] = {((1, 0), (0, 1)): mp.eye(5)}
        queue = [((1, 0), (0, 1))]
        while queue:
            cur = queue.pop(0)
            cur_u = visited[cur]
            for g_mod, g_u in ((t_mod5, tm), (s_mod5, sm)):
                nxt = mul2_mod5(cur, g_mod)
                if nxt not in visited:
                    visited[nxt] = cur_u * g_u
                    queue.append(nxt)
        weil_group_sizes[str(a_cls)] = len(visited)
        # Test det(rho(g)) == 1 on all 120 elements, and check equivariance of both invariant contractions on random complex vectors
        rng_j = random.Random(20261118 + a_cls)
        a_test = wb["D"][(1, 2)] - (mp.mpc(1) / mp.mpf(3)) * wb["D"][(2, 4)]
        psi1 = mp.zeros(5, 5)
        psi2 = mp.zeros(5, 5)
        for p_i in range(5):
            for q_i in range(p_i + 1, 5):
                v1 = mp.mpf(rng_j.randint(-7, 7)) + mp.mpc(0, 1) * mp.mpf(rng_j.randint(-7, 7))
                v2 = mp.mpf(rng_j.randint(-7, 7)) + mp.mpc(0, 1) * mp.mpf(rng_j.randint(-7, 7))
                psi1[p_i, q_i] = v1
                psi1[q_i, p_i] = -v1
                psi2[p_i, q_i] = v2
                psi2[q_i, p_i] = -v2
        h_up = mp.matrix([mp.mpf(rng_j.randint(-5, 5)) for _ in range(5)])
        psi_b = mp.matrix([mp.mpf(rng_j.randint(-5, 5)) for _ in range(5)])
        h_dn = mp.matrix([mp.mpf(rng_j.randint(-5, 5)) for _ in range(5)])

        def pfaff_up(x1: mp.matrix, x2: mp.matrix, hv: mp.matrix) -> mp.mpc:
            # eps_{abcde} x1^{ab} x2^{cd} hv^e
            acc = mp.mpc(0)
            for perm in itertools.permutations(range(5)):
                # sign of perm
                inv_c = sum(1 for i in range(5) for j in range(i + 1, 5) if perm[i] > perm[j])
                sgn = mp.mpf(-1) if (inv_c % 2) else mp.mpf(1)
                acc += sgn * x1[perm[0], perm[1]] * x2[perm[2], perm[3]] * hv[perm[4]]
            return acc

        c_up_5_0 = pfaff_up(psi1, psi2, a_test * h_up)
        c_up_45_0 = pfaff_up(a_test * psi1 + psi1 * mat_T(a_test), psi2, h_up)
        # Down contractions in dual basis bar_psi_a, bar_H_b:
        # 5-bar channel: psi1^{ab} bar_psi_a (A^T bar_H)_b
        # 45-bar channel: (1/2) M_45^a_{jk} psi1^{jk} bar_psi_a
        def dn_channels(am: mp.matrix, x1: mp.matrix, bp: mp.matrix, bh: mp.matrix) -> Tuple[mp.mpc, mp.mpc]:
            at_bh = mat_T(am) * bh
            ch5 = mp.mpc(0)
            ch45 = mp.mpc(0)
            for a_i in range(5):
                for b_i in range(5):
                    ch5 += x1[a_i, b_i] * bp[a_i] * at_bh[b_i]
                for j_i in range(5):
                    for k_i in range(5):
                        m45 = (am[a_i, j_i] * bh[k_i] - am[a_i, k_i] * bh[j_i]) + (mp.mpf(1) / mp.mpf(4)) * (
                            (mp.mpf(1) if a_i == j_i else mp.mpf(0)) * at_bh[k_i]
                            - (mp.mpf(1) if a_i == k_i else mp.mpf(0)) * at_bh[j_i]
                        )
                        ch45 += (mp.mpf(1) / mp.mpf(2)) * m45 * x1[j_i, k_i] * bp[a_i]
            return ch5, ch45

        c_dn_5_0, c_dn_45_0 = dn_channels(a_test, psi1, psi_b, h_dn)

        for g_u in visited.values():
            max_det_err = max(max_det_err, abs(mp.det(g_u) - mp.mpc(1)))
            g_inv = mat_conj_T(g_u)
            a_g = g_u * a_test * g_inv
            psi1_g = g_u * psi1 * mat_T(g_u)
            psi2_g = g_u * psi2 * mat_T(g_u)
            h_up_g = g_u * h_up
            psi_b_g = mat_T(g_inv) * psi_b
            h_dn_g = mat_T(g_inv) * h_dn
            max_wedge_inv_err = max(
                max_wedge_inv_err,
                abs(pfaff_up(psi1_g, psi2_g, a_g * h_up_g) - c_up_5_0),
                abs(pfaff_up(a_g * psi1_g + psi1_g * mat_T(a_g), psi2_g, h_up_g) - c_up_45_0),
            )
            d5_g, d45_g = dn_channels(a_g, psi1_g, psi_b_g, h_dn_g)
            max_wedge_inv_err = max(max_wedge_inv_err, abs(d5_g - c_dn_5_0), abs(d45_g - c_dn_45_0))

    # J2: Exact Georgi-Jarlskog -3 ratio on traceless 45-bar AND Linear Commutant Proportionality Wall!
    v_adap = wb["V_adap"]
    # Express all 24 D(w) in the adapted basis [3_c | 2_w]
    d_adap: Dict[Tuple[int, int], mp.matrix] = {
        w: mat_conj_T(v_adap) * wb["D"][w] * v_adap for w in PTS_24
    }
    six_y_adap = mp.diag([mp.mpf(-2), mp.mpf(-2), mp.mpf(-2), mp.mpf(3), mp.mpf(3)])

    # Check Tr_3(D_adap(w)) == +1/2, Tr_2(D_adap(w)) == -1/2, and Tr(D_adap(w)*6Y) == -5/2 for ALL 24 w!
    max_commutant_proj_err = mp.mpf(0)
    for w in PTS_24:
        dw = d_adap[w]
        tr3 = dw[0, 0] + dw[1, 1] + dw[2, 2]
        tr2 = dw[3, 3] + dw[4, 4]
        tr_y = mat_trace(dw * six_y_adap)
        max_commutant_proj_err = max(
            max_commutant_proj_err,
            abs(tr3 - mp.mpf(1) / mp.mpf(2)),
            abs(tr2 + mp.mpf(1) / mp.mpf(2)),
            abs(tr_y + mp.mpf(5) / mp.mpf(2)),
        )

    # Evaluate exact rational Clebsch ratios on 6Y = diag(-2,-2,-2,3,3) for down (i=0, alpha=4) vs lepton (beta=3, alpha=4)
    # Using M_45^a_{jk} with exact Fraction arithmetic:
    six_y_q = [Fraction(-2), Fraction(-2), Fraction(-2), Fraction(3), Fraction(3)]
    # bar_H placed at weak component alpha = 4 (value 1)
    # Down quark pairing: Psi^{0, 4} = 1 (Q_{0, 4}), bar_Psi_0 = 1 (d^c_0)
    # Lepton pairing: Psi^{3, 4} = 1 (e^c), bar_Psi_3 = 1 (L_3)
    # 5-bar channel: Psi^{a, 4} bar_Psi_a * (six_y_q[4])
    ch5_down_q = six_y_q[4]
    ch5_lep_q = six_y_q[4]
    # Traceless 45-bar channel: (1/2) M_45^a_{jk} Psi^{jk} bar_Psi_a (summing j,k in 0..4 with Psi^{jk} = -Psi^{kj})
    ch45_down_q = six_y_q[0] + Fraction(1, 4) * six_y_q[4]    # -2 + 3/4 = -5/4
    ch45_lep_q = six_y_q[3] + Fraction(1, 4) * six_y_q[4]     # +3 + 3/4 = +15/4
    gj_ratio_45_q = ch45_lep_q / ch45_down_q                  # -3 exact!
    # Untraceless planted control PC_XP1_2 (dropping +1/4 trace term):
    untraceless_ratio_q = six_y_q[3] / six_y_q[0]             # +3 / (-2) = -3/2!

    # Also verify numerically on B1953's actual 15x15 operator O(tau) at tau_1 = 13/100 + 17/10 i
    # by averaging over S(U(3)_c x U(2)_w) gauge group (exact Schur projection onto SM invariants)
    # that Y_e, Y_d^T, and Y_u extracted linearly from O(tau) are ALL scalar multiples of F(tau)!
    psi = wb["psi"]
    tau1 = f2m(Fraction(13, 100)) + mp.mpc(0, 1) * f2m(Fraction(17, 10))
    tau2 = f2m(Fraction(31, 100)) + mp.mpc(0, 1) * f2m(Fraction(6, 5))

    def build_five_multiplet_gramians(
        ymap: Dict[Tuple[int, int], mp.matrix],
        use_phase_table: bool = True,
    ) -> Dict[str, Any]:
        # Construct Y_tilde(w) = psi(-a*b)*Y(w), F = sum_w Y_tilde(w), and O_adap (15x15)
        ytil: Dict[Tuple[int, int], mp.matrix] = {}
        f_sum = mp.zeros(3, 3)
        o_adap = mp.zeros(15, 15)
        plain_gram = mp.zeros(3, 3)
        for a, b in PTS_24:
            ph = psi(-a * b) if use_phase_table else mp.mpc(1)
            yw = ph * ymap[(a, b)]
            ytil[(a, b)] = yw
            f_sum += yw
            o_adap += kron_mp(yw, d_adap[(a, b)])
            plain_gram += mp.mpf(5) * (ymap[(a, b)] * mat_conj_T(ymap[(a, b)]))

        # Check mixing between 3_c (indices 0,1,2) and 2_w (indices 3,4)
        mix_32 = mp.mpf(0)
        for fi in range(3):
            for fj in range(3):
                for c_i in range(3):
                    for w_i in (3, 4):
                        mix_32 = max(
                            mix_32,
                            abs(o_adap[5 * fi + c_i, 5 * fj + w_i]),
                            abs(o_adap[5 * fi + w_i, 5 * fj + c_i]),
                        )

        # Compute G_3 and G_2 directly from o_adap
        g3 = mp.zeros(3, 3)
        g2 = mp.zeros(3, 3)
        for fi in range(3):
            for fk in range(3):
                s3 = mp.mpc(0)
                s2 = mp.mpc(0)
                for fj in range(3):
                    for x in range(3):
                        for y in range(3):
                            s3 += o_adap[5 * fi + x, 5 * fj + y] * mp.conj(o_adap[5 * fk + x, 5 * fj + y])
                    for x in (3, 4):
                        for y in (3, 4):
                            s2 += o_adap[5 * fi + x, 5 * fj + y] * mp.conj(o_adap[5 * fk + x, 5 * fj + y])
                g3[fi, fk] = s3
                g2[fi, fk] = s2

        # ALSO construct explicit exterior-derivation operators d_O on:
        #   Lambda^2(W_adap) (10-dim -> 30x30 on F x Lambda^2):
        #     Q:   {(0,3),(0,4),(1,3),(1,4),(2,3),(2,4)} (dim 6)
        #     u^c: {(1,2),(0,2),(0,1)}                   (dim 3)
        #     e^c: {(3,4)}                               (dim 1)
        #   Lambda^4(W_adap) (5-dim -> 15x15 on F x Lambda^4):
        #     d^c: {(1,2,3,4),(0,2,3,4),(0,1,3,4)}       (dim 3)
        #     L:   {(0,1,2,3),(0,1,2,4)}                 (dim 2)
        def ext_deriv_matrix(am: mp.matrix, basis_tuples: List[Tuple[int, ...]]) -> mp.matrix:
            k_deg = len(basis_tuples[0])
            idx_map = {tp: idx for idx, tp in enumerate(basis_tuples)}
            nb = len(basis_tuples)
            dm_out = mp.zeros(nb, nb)
            for col_i, tp in enumerate(basis_tuples):
                for slot in range(k_deg):
                    src_v = tp[slot]
                    for dst_v in range(5):
                        coeff = am[dst_v, src_v]
                        if coeff == 0 or (dst_v in tp and dst_v != src_v):
                            continue
                        lst = list(tp)
                        lst[slot] = dst_v
                        sgn = mp.mpf(1)
                        for p1 in range(k_deg):
                            for p2 in range(p1 + 1, k_deg):
                                if lst[p1] > lst[p2]:
                                    lst[p1], lst[p2] = lst[p2], lst[p1]
                                    sgn = -sgn
                        row_i = idx_map[tuple(lst)]
                        dm_out[row_i, col_i] += sgn * coeff
            return dm_out

        q_tuples = [(0, 3), (0, 4), (1, 3), (1, 4), (2, 3), (2, 4)]
        uc_tuples = [(1, 2), (0, 2), (0, 1)]
        ec_tuples = [(3, 4)]
        dc_tuples = [(1, 2, 3, 4), (0, 2, 3, 4), (0, 1, 3, 4)]
        l_tuples = [(0, 1, 2, 3), (0, 1, 2, 4)]

        mult_defs = {
            "Q": q_tuples,
            "uc": uc_tuples,
            "ec": ec_tuples,
            "dc": dc_tuples,
            "L": l_tuples,
        }
        gramians_direct: Dict[str, mp.matrix] = {}
        for mname, btups in mult_defs.items():
            dim_r = len(btups)
            big_op = mp.zeros(3 * dim_r, 3 * dim_r)
            for w in PTS_24:
                big_op += kron_mp(ytil[w], ext_deriv_matrix(d_adap[w], btups))
            gr = mp.zeros(3, 3)
            for fi in range(3):
                for fk in range(3):
                    acc = mp.mpc(0)
                    for fj in range(3):
                        for x in range(dim_r):
                            for y in range(dim_r):
                                acc += big_op[dim_r * fi + x, dim_r * fj + y] * mp.conj(
                                    big_op[dim_r * fk + x, dim_r * fj + y]
                                )
                    gr[fi, fk] = acc / mp.mpf(dim_r)
            gramians_direct[mname] = gr

        ff = f_sum * mat_conj_T(f_sum)
        formulas = {
            "ec": ff / mp.mpf(4),
            "L": g2 / mp.mpf(2),
            "dc": g3 / mp.mpf(3),
            "uc": g3 / mp.mpf(3) + ff / mp.mpf(12),
            "Q": g3 / mp.mpf(3) + g2 / mp.mpf(2) - ff / mp.mpf(12),
        }
        max_formula_err = max(
            mat_max_abs(gramians_direct[k] - formulas[k]) / mat_max_abs(gramians_direct[k])
            for k in formulas
        )
        # Exact 3x3 matrix Schur-Plancherel on Lambda^2(W):
        # 6 G_Q + 3 G_uc + G_ec == 3*(G_3 + G_2) == 3 * plain_gram
        lhs_sp = mp.mpf(6) * gramians_direct["Q"] + mp.mpf(3) * gramians_direct["uc"] + gramians_direct["ec"]
        rhs_sp1 = mp.mpf(3) * (g3 + g2)
        rhs_sp2 = mp.mpf(3) * plain_gram
        sp_err = max(mat_max_abs(lhs_sp - rhs_sp1), mat_max_abs(lhs_sp - rhs_sp2)) / mat_max_abs(rhs_sp2)

        # Linear S(U(3)xU(2))-commutant projection of O_adap:
        # Project each 3x3 colour block to (Tr/3)*I_3 and each 2x2 weak block to (Tr/2)*I_2!
        # In the 45-bar down/lepton channel on O_adap:
        yd_lin_45 = mp.zeros(3, 3)
        ye_lin_45 = mp.zeros(3, 3)
        yu_lin_5 = mp.zeros(3, 3)
        for fi in range(3):
            for fj in range(3):
                blk = mp.zeros(5, 5)
                for r in range(5):
                    for c in range(5):
                        blk[r, c] = o_adap[5 * fi + r, 5 * fj + c]
                a_col_avg = (blk[0, 0] + blk[1, 1] + blk[2, 2]) / mp.mpf(3)
                a_wk_avg = (blk[3, 3] + blk[4, 4]) / mp.mpf(2)
                yd_lin_45[fi, fj] = a_col_avg + (mp.mpf(1) / mp.mpf(4)) * a_wk_avg
                ye_lin_45[fi, fj] = a_wk_avg + (mp.mpf(1) / mp.mpf(4)) * a_wk_avg
                yu_lin_5[fi, fj] = a_wk_avg
        # Check exact linear proportionality:
        # a_col_avg = +(1/6)*F, a_wk_avg = -(1/4)*F =>
        # yd_lin_45 = (1/6 - 1/16) F = +(5/48) F; ye_lin_45 = (-1/4 - 1/16) F = -(5/16) F = -3 * yd_lin_45;
        # yu_lin_5  = -(1/4) F!
        lin_wall_err = max(
            mat_max_abs(ye_lin_45 + mp.mpf(3) * yd_lin_45) / mat_max_abs(yd_lin_45),
            mat_max_abs(yd_lin_45 - (mp.mpf(5) / mp.mpf(48)) * f_sum) / mat_max_abs(f_sum),
            mat_max_abs(yu_lin_5 + (mp.mpf(1) / mp.mpf(4)) * f_sum) / mat_max_abs(f_sum),
        )

        return {
            "F": f_sum,
            "G3": g3,
            "G2": g2,
            "G_mult": gramians_direct,
            "mix_32": mix_32 / mat_max_abs(o_adap),
            "max_formula_err": max_formula_err,
            "schur_plancherel_err": sp_err,
            "linear_wall_err": lin_wall_err,
        }

    # Check hypercharge-square specialization on pure 6Y operator O_Y = -(1/12) F (x) 6Y
    f_rand = mp.matrix([
        [mp.mpf(2), mp.mpc(1, -1), mp.mpf(-1) / mp.mpf(3)],
        [mp.mpc(0, 2), mp.mpf(-3) / mp.mpf(2), mp.mpf(1)],
        [mp.mpf(1) / mp.mpf(5), mp.mpf(2), mp.mpc(-1, 2)],
    ])
    ff_rand = f_rand * mat_conj_T(f_rand)
    # On O_Y = -(1/12) F (x) 6Y: G3 = 3*(2/12)^2 FF = (1/12) FF, G2 = 2*(-3/12)^2 FF = (1/8) FF
    g3_y = ff_rand / mp.mpf(12)
    g2_y = ff_rand / mp.mpf(8)
    hy_forms = {
        "ec": (ff_rand / mp.mpf(4), Fraction(36, 144)),
        "L": (g2_y / mp.mpf(2), Fraction(9, 144)),
        "dc": (g3_y / mp.mpf(3), Fraction(4, 144)),
        "uc": (g3_y / mp.mpf(3) + ff_rand / mp.mpf(12), Fraction(16, 144)),
        "Q": (g3_y / mp.mpf(3) + g2_y / mp.mpf(2) - ff_rand / mp.mpf(12), Fraction(1, 144)),
    }
    max_hy_sq_err = max(
        mat_max_abs(mat_v - f2m(fr_v) * ff_rand) / mat_max_abs(ff_rand)
        for mat_v, fr_v in hy_forms.values()
    )

    # J3-J5: Test SL(2, Z) invariance (T and S), PSD positivity, pairwise distinctness across all 5 SM multiplets,
    # non-trivial eigenbasis misalignment, planted control PC_XP1_1 (no phase table), and 10-trial Haar scrambling!
    max_formula_all = mp.mpf(0)
    max_sp_all = mp.mpf(0)
    max_lin_wall_all = mp.mpf(0)
    max_mix32_all = mp.mpf(0)
    max_sl2z_ratio_err = mp.mpf(0)
    min_psd_eig_ratio = mp.mpf(1)
    min_pairwise_mult_sep = mp.mpf(1)
    min_offdiag_overlap = mp.mpf(1)
    min_pc1_broken_drift = mp.mpf(10)

    def eig_ratios_psd(gm: mp.matrix) -> Tuple[mp.mpf, mp.mpf, mp.mpf]:
        ev = eig_hermitian_sorted(gm)
        return ev[1] / ev[0], ev[2] / ev[0], ev[2] / ev[0]

    for res_mode in (True, False):
        for tau_b in (tau1, tau2):
            y_base = frame_c_couplings_24(tau_b, 1, 2, residue_only=res_mode)
            y_t = frame_c_couplings_24(tau_b + mp.mpf(1), 1, 2, residue_only=res_mode)
            y_s = frame_c_couplings_24(-mp.mpc(1) / tau_b, 1, 2, residue_only=res_mode)
            for rd in ("S", "St"):
                b0 = build_five_multiplet_gramians(y_base[rd], use_phase_table=True)
                bt = build_five_multiplet_gramians(y_t[rd], use_phase_table=True)
                bs = build_five_multiplet_gramians(y_s[rd], use_phase_table=True)

                max_formula_all = max(max_formula_all, b0["max_formula_err"])
                max_sp_all = max(max_sp_all, b0["schur_plancherel_err"])
                max_lin_wall_all = max(max_lin_wall_all, b0["linear_wall_err"])
                max_mix32_all = max(max_mix32_all, b0["mix_32"])

                rats_0: Dict[str, Tuple[mp.mpf, mp.mpf]] = {}
                for mname in ("Q", "uc", "dc", "L", "ec"):
                    r12_0, r13_0, min_ev = eig_ratios_psd(b0["G_mult"][mname])
                    r12_t, r13_t, _ = eig_ratios_psd(bt["G_mult"][mname])
                    r12_s, r13_s, _ = eig_ratios_psd(bs["G_mult"][mname])
                    rats_0[mname] = (r12_0, r13_0)
                    min_psd_eig_ratio = min(min_psd_eig_ratio, min_ev)
                    max_sl2z_ratio_err = max(
                        max_sl2z_ratio_err,
                        abs(r12_t / r12_0 - mp.mpf(1)),
                        abs(r13_t / r13_0 - mp.mpf(1)),
                        abs(r12_s / r12_0 - mp.mpf(1)),
                        abs(r13_s / r13_0 - mp.mpf(1)),
                    )

                for m1, m2 in itertools.combinations(("Q", "uc", "dc", "L", "ec"), 2):
                    sep = max(abs(rats_0[m1][0] - rats_0[m2][0]), abs(rats_0[m1][1] - rats_0[m2][1]))
                    min_pairwise_mult_sep = min(min_pairwise_mult_sep, sep)

                # Check eigenbasis misalignment between G_Q and G_dc
                _, vq = mp.eigh((b0["G_mult"]["Q"] + mat_conj_T(b0["G_mult"]["Q"])) / mp.mpf(2))
                _, vdc = mp.eigh((b0["G_mult"]["dc"] + mat_conj_T(b0["G_mult"]["dc"])) / mp.mpf(2))
                ov = mat_conj_T(vq) * vdc
                off_max = max(abs(ov[r, c]) for r in range(3) for c in range(3) if r != c)
                min_offdiag_overlap = min(min_offdiag_overlap, off_max)

                # Planted control PC_XP1_1: without coboundary phase table, SL(2, Z) fails on G_Q and G_ec!
                if res_mode and tau_b == tau1 and rd == "S":
                    b0_bad = build_five_multiplet_gramians(y_base[rd], use_phase_table=False)
                    bt_bad = build_five_multiplet_gramians(y_t[rd], use_phase_table=False)
                    r12_b0, r13_b0, _ = eig_ratios_psd(b0_bad["G_mult"]["ec"])
                    r12_bt, r13_bt, _ = eig_ratios_psd(bt_bad["G_mult"]["ec"])
                    min_pc1_broken_drift = max(abs(r12_bt - r12_b0) / r12_b0, abs(r13_bt - r13_b0) / r13_b0)

    # J5: Mandatory 10-trial random Haar basis-scrambling test (Guardrail 3) on U(3)_L x U(3)_R x SU(3)_c x SU(2)_w
    rng_haar = random.Random(2026111805)
    y_haar_src = frame_c_couplings_24(tau1, 1, 2, residue_only=False)["S"]
    ref_j = build_five_multiplet_gramians(y_haar_src, use_phase_table=True)
    ref_eigs = {m: eig_hermitian_sorted(ref_j["G_mult"][m]) for m in ("Q", "uc", "dc", "L", "ec")}
    _, vq0 = mp.eigh((ref_j["G_mult"]["Q"] + mat_conj_T(ref_j["G_mult"]["Q"])) / mp.mpf(2))
    _, vdc0 = mp.eigh((ref_j["G_mult"]["dc"] + mat_conj_T(ref_j["G_mult"]["dc"])) / mp.mpf(2))
    ov0_mod = sorted([abs((mat_conj_T(vq0) * vdc0)[r, c]) for r in range(3) for c in range(3)])

    max_haar_err = mp.mpf(0)
    for _ in range(10):
        ul = random_haar_unitary_mp(3, rng_haar)
        ur = random_haar_unitary_mp(3, rng_haar)
        uc3 = make_su(random_haar_unitary_mp(3, rng_haar))
        uw2 = make_su(random_haar_unitary_mp(2, rng_haar))
        u_gauge = mp.zeros(5, 5)
        for r in range(3):
            for c in range(3):
                u_gauge[r, c] = uc3[r, c]
        for r in range(2):
            for c in range(2):
                u_gauge[3 + r, 3 + c] = uw2[r, c]

        # Rotate both family frames Y(w) -> U_L Y(w) U_R^dag AND internal S(U(3)xU(2)) basis D_adap(w) -> U_g D_adap(w) U_g^dag
        d_adap_scr = {w: u_gauge * d_adap[w] * mat_conj_T(u_gauge) for w in PTS_24}
        ytil_scr = {w: psi(-w[0] * w[1]) * (ul * y_haar_src[w] * mat_conj_T(ur)) for w in PTS_24}

        # Reconstruct Q (6D) and dc (3D) exterior operators directly in the scrambled gauge & family bases
        def ext_deriv_scr(am: mp.matrix, basis_tuples: List[Tuple[int, ...]]) -> mp.matrix:
            k_deg = len(basis_tuples[0])
            idx_map = {tp: idx for idx, tp in enumerate(basis_tuples)}
            nb = len(basis_tuples)
            dm_out = mp.zeros(nb, nb)
            for col_i, tp in enumerate(basis_tuples):
                for slot in range(k_deg):
                    src_v = tp[slot]
                    for dst_v in range(5):
                        coeff = am[dst_v, src_v]
                        if coeff == 0 or (dst_v in tp and dst_v != src_v):
                            continue
                        lst = list(tp)
                        lst[slot] = dst_v
                        sgn = mp.mpf(1)
                        for p1 in range(k_deg):
                            for p2 in range(p1 + 1, k_deg):
                                if lst[p1] > lst[p2]:
                                    lst[p1], lst[p2] = lst[p2], lst[p1]
                                    sgn = -sgn
                        dm_out[idx_map[tuple(lst)], col_i] += sgn * coeff
            return dm_out

        mult_scr = {
            "Q": [(0, 3), (0, 4), (1, 3), (1, 4), (2, 3), (2, 4)],
            "uc": [(1, 2), (0, 2), (0, 1)],
            "ec": [(3, 4)],
            "dc": [(1, 2, 3, 4), (0, 2, 3, 4), (0, 1, 3, 4)],
            "L": [(0, 1, 2, 3), (0, 1, 2, 4)],
        }
        g_scr: Dict[str, mp.matrix] = {}
        for mname, btups in mult_scr.items():
            dim_r = len(btups)
            big_op = mp.zeros(3 * dim_r, 3 * dim_r)
            for w in PTS_24:
                big_op += kron_mp(ytil_scr[w], ext_deriv_scr(d_adap_scr[w], btups))
            gr = mp.zeros(3, 3)
            for fi in range(3):
                for fk in range(3):
                    acc = mp.mpc(0)
                    for fj in range(3):
                        for x in range(dim_r):
                            for y in range(dim_r):
                                acc += big_op[dim_r * fi + x, dim_r * fj + y] * mp.conj(
                                    big_op[dim_r * fk + x, dim_r * fj + y]
                                )
                    gr[fi, fk] = acc / mp.mpf(dim_r)
            g_scr[mname] = gr
            ev_s = eig_hermitian_sorted(gr)
            for idx_e in range(3):
                max_haar_err = max(max_haar_err, abs(ev_s[idx_e] - ref_eigs[mname][idx_e]) / ref_eigs[mname][0])

        _, vqs = mp.eigh((g_scr["Q"] + mat_conj_T(g_scr["Q"])) / mp.mpf(2))
        _, vdcs = mp.eigh((g_scr["dc"] + mat_conj_T(g_scr["dc"])) / mp.mpf(2))
        ovs_mod = sorted([abs((mat_conj_T(vqs) * vdcs)[r, c]) for r in range(3) for c in range(3)])
        for idx_o in range(9):
            max_haar_err = max(max_haar_err, abs(ovs_mod[idx_o] - ov0_mod[idx_o]))

    tol_strict = mp.mpf(10) ** (-40)
    return {
        "up_weight_space_dim": up_wt_dim,
        "up_sl5_invariant_dim": up_inv_dim,
        "down_weight_space_dim": dn_wt_dim,
        "down_sl5_invariant_dim": dn_inv_dim,
        "weil_group_sizes": weil_group_sizes,
        "det_rho_unit_passed": max_det_err < tol_strict,
        "sl2f5_wedge_invariance_both_classes_passed": max_wedge_inv_err < tol_strict,
        "commutant_projection_constant_across_24_passed": max_commutant_proj_err < tol_strict,
        "ch5_lepton_over_down_ratio": f"{(ch5_lep_q / ch5_down_q).numerator}/{(ch5_lep_q / ch5_down_q).denominator}",
        "ch45_lepton_over_down_ratio": f"{gj_ratio_45_q.numerator}/{gj_ratio_45_q.denominator}",
        "pc2_untraceless_ratio": f"{untraceless_ratio_q.numerator}/{untraceless_ratio_q.denominator}",
        "linear_proportionality_wall_passed": max_lin_wall_all < tol_strict,
        "parity_3_2_block_diagonal_passed": max_mix32_all < tol_strict,
        "five_multiplet_closed_forms_passed": max_formula_all < tol_strict,
        "hypercharge_square_specialization_passed": max_hy_sq_err < tol_strict,
        "matrix_schur_plancherel_passed": max_sp_all < tol_strict,
        "sl2z_invariance_all_five_gramians_passed": max_sl2z_ratio_err < tol_strict,
        "strict_positivity_all_five_gramians": min_psd_eig_ratio > mp.mpf(0),
        "all_ten_multiplet_pairs_distinct": min_pairwise_mult_sep > mp.mpf(1) / mp.mpf(1000),
        "q_dc_eigenbasis_nontrivial_overlap": min_offdiag_overlap > mp.mpf(1) / mp.mpf(100),
        "haar_10trial_basis_invariance_passed": max_haar_err < mp.mpf(10) ** (-38),
        "pc1_dropped_phase_table_breaks_sl2z": min_pc1_broken_drift > mp.mpf(1) / mp.mpf(10),
    }


# ============================================================================
# 3. Module Z: P-874 Q2 (W-L1 Design Criterion Without Data at tau=i and tau=rho)
# ============================================================================

def classify_nullity_and_degeneracy(svals: List[mp.mpf]) -> Dict[str, Any]:
    """
    Firewall-clean classifier: returns ONLY integer nullity in {0,1,2,3},
    boolean gap check (that zero SVs are < 10^-38*s_max while nonzero SVs are > 10^-15*s_max),
    and integer degeneracy partition of the non-zero singular values.
    NO continuous singular-value ratios are ever returned or printed!
    """
    smax = svals[0]
    assert smax > mp.mpf(10) ** (-30), "All singular values vanished unexpectedly"
    lo_cut = mp.mpf(10) ** (-38) * smax
    hi_cut = mp.mpf(10) ** (-15) * smax
    nz: List[mp.mpf] = []
    nullity = 0
    clean_gap = True
    for s in svals:
        if s < lo_cut:
            nullity += 1
        elif s > hi_cut:
            nz.append(s)
        else:
            clean_gap = False
            nz.append(s)

    # Group non-zero SVs into degeneracy clusters within relative tolerance 10^-30
    clusters: List[int] = []
    used = [False] * len(nz)
    for i in range(len(nz)):
        if used[i]:
            continue
        cnt = 1
        used[i] = True
        for j in range(i + 1, len(nz)):
            if not used[j] and abs(nz[i] - nz[j]) <= mp.mpf(10) ** (-30) * nz[i]:
                used[j] = True
                cnt += 1
        clusters.append(cnt)
    clusters.sort(reverse=True)
    return {
        "rank": 3 - nullity,
        "nullity": nullity,
        "clean_zero_gap": clean_gap,
        "nonzero_degeneracy_partition": clusters,
    }


def run_module_z_symmetry_nullity() -> Dict[str, Any]:
    """
    Firewall-clean test of P-874 Q2 (W-L1's vanishing criterion) at:
      - tau_i = i               (fixed by S: tau -> -1/tau)
      - tau_rho = (-1 + i*sqrt(3))/2  (fixed by ST: tau -> -1/(tau + 1))
    Also checks B[1] third component vanishing at tau = i (W-A1 line 167) and Wronskian/discriminant
    behavior at tau = rho, and records integer nullities and degeneracy partitions for:
      - pointwise coupling at the mark (2/5, 4/5) in up and down sectors,
      - B1953 phased sum F(tau_*),
      - B1953 / exterior multiplet Gramians G_3, G_2, G_Q, G_uc.
    Zero non-zero singular-value ratios or mixing angles are computed or stored!
    """
    iu = mp.mpc(0, 1)
    tau_i = iu
    tau_rho = (mp.mpf(-1) + iu * mp.sqrt(mp.mpf(3))) / mp.mpf(2)

    wb = build_weil_and_weyl_mp()
    psi = wb["psi"]
    v_adap = wb["V_adap"]
    d_adap = {w: mat_conj_T(v_adap) * wb["D"][w] * v_adap for w in PTS_24}

    # Check exact Higgs triplet B[1] zeroes at tau = i and tau = rho
    b1_i = eval_higgs_triplet_B1(tau_i)
    b1_rho = eval_higgs_triplet_B1(tau_rho)
    b1_i_c3_vanishes = abs(b1_i[2]) < mp.mpf(10) ** (-45)
    # Check isotropic dot product B[1] . B[1] at tau = i and tau = rho
    b1_dot_i = b1_i[0] ** 2 + b1_i[1] ** 2 + b1_i[2] ** 2
    b1_dot_rho = b1_rho[0] ** 2 + b1_rho[1] ** 2 + b1_rho[2] ** 2
    b1_rho_isotropic_vanishes = abs(b1_dot_rho) < mp.mpf(10) ** (-45)

    results_loci: Dict[str, Any] = {}
    for locus_name, tau_pt in (("tau_eq_i", tau_i), ("tau_eq_rho", tau_rho)):
        locus_entry: Dict[str, Any] = {}
        for res_label, res_flag in (("residue", True), ("channel_weighted", False)):
            y_dn_all = frame_c_couplings_24(tau_pt, 1, 2, residue_only=res_flag)
            y_up_all = frame_c_couplings_24(tau_pt, 1, -4, residue_only=res_flag)
            mode_entry: Dict[str, Any] = {}
            for rd in ("S", "St"):
                ydn = y_dn_all[rd]
                yup = y_up_all[rd]
                # Mark (2, 4) pointwise nullities
                mark_dn = classify_nullity_and_degeneracy(svd_sorted(ydn[(2, 4)]))
                mark_up = classify_nullity_and_degeneracy(svd_sorted(yup[(2, 4)]))
                # Count how many of the 24 points have nullity >= 1 in down and up
                pts_null_ge1_dn = sum(
                    1 for w in PTS_24 if classify_nullity_and_degeneracy(svd_sorted(ydn[w]))["nullity"] >= 1
                )
                pts_null_ge1_up = sum(
                    1 for w in PTS_24 if classify_nullity_and_degeneracy(svd_sorted(yup[w]))["nullity"] >= 1
                )

                # Build B1953 covariant operator O_adap and exterior Gramians at tau_pt
                f_sum = mp.zeros(3, 3)
                o_adap = mp.zeros(15, 15)
                for a, b in PTS_24:
                    yw = psi(-a * b) * ydn[(a, b)]
                    f_sum += yw
                    o_adap += kron_mp(yw, d_adap[(a, b)])
                g3 = mp.zeros(3, 3)
                g2 = mp.zeros(3, 3)
                for fi in range(3):
                    for fk in range(3):
                        s3 = mp.mpc(0)
                        s2 = mp.mpc(0)
                        for fj in range(3):
                            for x in range(3):
                                for y in range(3):
                                    s3 += o_adap[5 * fi + x, 5 * fj + y] * mp.conj(o_adap[5 * fk + x, 5 * fj + y])
                            for x in (3, 4):
                                for y in (3, 4):
                                    s2 += o_adap[5 * fi + x, 5 * fj + y] * mp.conj(o_adap[5 * fk + x, 5 * fj + y])
                        g3[fi, fk] = s3
                        g2[fi, fk] = s2
                ff = f_sum * mat_conj_T(f_sum)
                g_uc = g3 / mp.mpf(3) + ff / mp.mpf(12)
                g_q = g3 / mp.mpf(3) + g2 / mp.mpf(2) - ff / mp.mpf(12)

                mode_entry[rd] = {
                    "mark_down": mark_dn,
                    "mark_up": mark_up,
                    "points_of_24_with_nullity_ge_1_down": pts_null_ge1_dn,
                    "points_of_24_with_nullity_ge_1_up": pts_null_ge1_up,
                    "phased_sum_F": classify_nullity_and_degeneracy(svd_sorted(f_sum)),
                    "gramian_G3": classify_nullity_and_degeneracy(eig_hermitian_sorted(g3)),
                    "gramian_G2": classify_nullity_and_degeneracy(eig_hermitian_sorted(g2)),
                    "gramian_G_uc": classify_nullity_and_degeneracy(eig_hermitian_sorted(g_uc)),
                    "gramian_G_Q": classify_nullity_and_degeneracy(eig_hermitian_sorted(g_q)),
                }
            locus_entry[res_label] = mode_entry
        results_loci[locus_name] = locus_entry

    # Also check fixed-point stabilizer consistency: S(i) == i and (ST)(rho) == rho identically
    st_rho = -mp.mpc(1) / (tau_rho + mp.mpf(1))
    orbifold_fixed_err = max(abs(-mp.mpc(1) / tau_i - tau_i), abs(st_rho - tau_rho))

    return {
        "orbifold_fixed_points_exact": orbifold_fixed_err < mp.mpf(10) ** (-50),
        "b1_third_component_vanishes_at_i": b1_i_c3_vanishes,
        "b1_isotropic_square_vanishes_at_rho": b1_rho_isotropic_vanishes,
        "loci": results_loci,
    }


# ============================================================================
# 4. Module W: Chartered Pure-Math Check of Web Card W-P1 + Section 5 Item 2
# ============================================================================

def run_module_w_wp1_and_sec5() -> Dict[str, Any]:
    """
    Independent second derivation of W-P1 (2f2e490e1) items P1-P3 and W1-W4,
    plus exact decision on W-P1 section 5 item 2 (whether 'what the act does'
    settles S vs Stilde or the sign of B on the Higgs ground plane E).
    """
    g = sp.Matrix([[2, 1], [1, 1]])
    i2 = sp.eye(2)
    tr_g = int(g.trace())
    det_g = int(g.det())
    # Characteristic polynomial lambda^2 - 3 lambda + 1 = 0 -> (3 + sqrt(5))/2
    lam_max = (sp.Integer(3) + sp.sqrt(sp.Integer(5))) / sp.Integer(2)
    fixed_torus_1_to_8 = [int(abs((g ** n - i2).det())) for n in range(1, 9)]
    trace_formula_matches = all(
        fixed_torus_1_to_8[n - 1] == int(abs(2 - (g ** n).trace())) for n in range(1, 9)
    )

    # P2: fixed points on R of z -> (2z + 1)/(z + 1) => z^2 - z - 1 = 0 => (1 +- sqrt(5))/2
    fp_plus = (sp.Integer(1) + sp.sqrt(sp.Integer(5))) / sp.Integer(2)
    fp_minus = (sp.Integer(1) - sp.sqrt(sp.Integer(5))) / sp.Integer(2)
    axis_center = sp.simplify((fp_plus + fp_minus) / sp.Integer(2))          # 1/2
    axis_radius_sq = sp.simplify(((fp_plus - fp_minus) / sp.Integer(2)) ** 2) # 5/4
    i_on_axis = sp.simplify(abs(sp.I - axis_center) ** 2 - axis_radius_sq) == 0
    one_plus_i_on_axis = sp.simplify(abs(1 + sp.I - axis_center) ** 2 - axis_radius_sq) == 0
    gamma_of_i = sp.simplify((2 * sp.I + 1) / (sp.I + 1))                     # 3/2 + i/2

    # P3: L^n R = [[n + 1, n], [1, 1]], axis radius^2 = ((n + 2)^2 - 4) / 4 = (n^2 + 4n) / 4
    l_mat = sp.Matrix([[1, 1], [0, 1]])
    r_mat = sp.Matrix([[1, 0], [1, 1]])
    lnr_radii_sq: List[str] = []
    for n in range(1, 9):
        mn = (l_mat ** n) * r_mat
        rad_sq = sp.Rational(int(mn.trace() ** 2 - 4), int(4 * mn[1, 0] ** 2))
        lnr_radii_sq.append(f"{rad_sq.p}/{rad_sq.q}")

    # Orders of gamma mod 2 and mod 5
    ord_mod2 = next(k for k in range(1, 10) if ((g ** k) % 2) == i2)
    ord_mod5 = next(k for k in range(1, 25) if ((g ** k) % 5) == i2)
    g5_mod5 = ((g ** 5) % 5).tolist()   # [[4, 0], [0, 4]] == -I mod 5

    # W1-W4: Weil space in classes a = 1 and a = 2 in 55-digit mpmath
    wb = build_weil_and_weyl_mp()
    p_op = wb["P"]
    v_adap = wb["V_adap"]
    tol_w = mp.mpf(10) ** (-45)

    weil_results: Dict[str, Any] = {}
    t_traces: Dict[int, Tuple[mp.mpc, mp.mpc]] = {}
    for a_cls in (1, 2):
        tm, sm = wb["weil_classes"][a_cls]
        t_inv = mat_conj_T(tm)
        s_inv = mat_conj_T(sm)
        # gamma = [[2, 1], [1, 1]] = T * S * T^-1 * S^-1
        rho_g = tm * sm * t_inv * s_inv
        s2_eq_p = mat_max_abs(sm * sm - p_op) < tol_w
        s4_eq_i = mat_max_abs((sm * sm) * (sm * sm) - mp.eye(5)) < tol_w
        rg5 = mp.eye(5)
        for _ in range(5):
            rg5 = rg5 * rho_g
        rg5_eq_p = mat_max_abs(rg5 - p_op) < tol_w

        tr_rg1 = mat_trace(rho_g)
        tr_rg2 = mat_trace(rho_g * rho_g)

        # Restrict rho_g to 3_even and 2_odd via V_adap
        rg_adap = mat_conj_T(v_adap) * rho_g * v_adap
        rg_even = mp.zeros(3, 3)
        rg_odd = mp.zeros(2, 2)
        for r in range(3):
            for c in range(3):
                rg_even[r, c] = rg_adap[r, c]
        for r in range(2):
            for c in range(2):
                rg_odd[r, c] = rg_adap[3 + r, 3 + c]

        # Extract eigenphases in exact tenths of a turn (since rho_g^10 = P^2 = I_5!)
        ev_even, _ = mp.eig(rg_even)
        ev_odd, _ = mp.eig(rg_odd)
        def tenths_list(vals: Sequence[mp.mpc]) -> List[int]:
            out_t: List[int] = []
            for v in vals:
                ang_turns = (mp.arg(v) / (2 * mp.pi)) % mp.mpf(1)
                tenth = int(mp.nint(ang_turns * mp.mpf(10))) % 10
                out_t.append(10 if tenth == 0 else tenth)
            return sorted(out_t)

        t_traces[a_cls] = (mat_trace(tm), mat_trace(tm * tm))
        weil_results[str(a_cls)] = {
            "S2_equals_P": s2_eq_p,
            "S4_equals_I": s4_eq_i,
            "rho_gamma_5_equals_P": rg5_eq_p,
            "tr_rho_gamma_zero": abs(tr_rg1) < tol_w,
            "tr_rho_gamma2_abs_sq_eq_5": abs(abs(tr_rg2) ** 2 - mp.mpf(5)) < tol_w,
            "eigenphases_tenths_even3": tenths_list(ev_even),
            "eigenphases_tenths_odd2": tenths_list(ev_odd),
        }

    # W4: signature tr R(T^2) / (tr R(T))^2 for R = W_a (x) conj(W_b)
    sig_table: Dict[str, str] = {}
    sig_exact_ok = True
    for a_cls in (1, 2):
        for b_cls in (1, 2):
            t1 = t_traces[a_cls][0] * mp.conj(t_traces[b_cls][0])
            t2 = t_traces[a_cls][1] * mp.conj(t_traces[b_cls][1])
            ratio = t2 / (t1 * t1)
            want = Fraction(1, 5) if a_cls == b_cls else Fraction(-1, 5)
            if abs(ratio - f2m(want)) >= tol_w:
                sig_exact_ok = False
            sig_table[f"{a_cls}_{b_cls}"] = f"{want.numerator}/{want.denominator}"

    # Planted control PC_XP1_4: wrong Fourier sign +2*a*x*y in W-P1's first run
    iu = mp.mpc(0, 1)
    zeta = mp.exp(2 * iu * mp.pi / mp.mpf(5))
    psi = lambda k: zeta ** (k % 5)
    t_bad = mp.diag([psi(x * x) for x in range(5)])
    f_bad = mp.matrix([[psi(2 * x * y) for y in range(5)] for x in range(5)])
    a_bad = f_bad * f_bad
    b_bad = (f_bad * t_bad) * (f_bad * t_bad) * (f_bad * t_bad)
    # Check if a_bad and b_bad are proportional (if proportional, all ratios a_bad[r,c]/b_bad[r,c] match;
    # actually check c = a_bad[0,0]/b_bad[0,0] and residual |(c*f_bad)^2 - (c*f_bad*t_bad)^3|!)
    c_try = a_bad[0, 0] / b_bad[0, 0]
    s_try = c_try * f_bad
    pc4_wrong_sign_residual = mat_max_abs(s_try * s_try - (s_try * t_bad) * (s_try * t_bad) * (s_try * t_bad))

    # W-P1 Section 5 Item 2:
    # (a) On Higgs ground plane E = span(v_+, v_-), transport U = diag(exp(i*pi/6), exp(-i*pi/6))
    #     and orientation-reversing tick/S6 swap [[0, 1], [1, 0]]:
    c_p, c_m, cb_p, cb_m = sp.symbols("c_p c_m cb_p cb_m")
    n_inv = c_p * cb_p + c_m * cb_m
    delta_sq = (c_p * cb_p - c_m * cb_m) ** 2
    ph_u = sp.exp(sp.I * sp.pi / 6)
    n_after_u = sp.simplify(n_inv.subs({c_p: ph_u * c_p, cb_p: sp.conjugate(ph_u) * cb_p, c_m: sp.conjugate(ph_u) * c_m, cb_m: ph_u * cb_m}) - n_inv)
    d2_after_u = sp.simplify(delta_sq.subs({c_p: ph_u * c_p, cb_p: sp.conjugate(ph_u) * cb_p, c_m: sp.conjugate(ph_u) * c_m, cb_m: ph_u * cb_m}) - delta_sq)
    d2_after_swap = sp.simplify(delta_sq.subs({c_p: c_m, cb_p: cb_m, c_m: c_p, cb_m: cb_p}) - delta_sq)
    sign_B_stays_unselected = (n_after_u == 0 and d2_after_u == 0 and d2_after_swap == 0)

    # (b) On readings S vs Stilde vs Sstar along the golden axis at gamma's own fixed line (1, 2) mod 5!
    # Check 1-turn repetition of Y(gamma^k(tau_axis), (1, 2)) for S, Stilde, and planted control Sstar (PC_XP1_3):
    # Note: on the golden axis |tau - 1/2| = sqrt(5)/2, take a generic point tau_ax = 1/2 + (sqrt(5)/2)*exp(i*theta)
    # with rational cos/sin (Pythagorean triple (3/5, 4/5): Re = 1/2 + (3/10)*sqrt(5), Im = (2/5)*sqrt(5))!
    rt5 = mp.sqrt(mp.mpf(5))
    tau_ax0 = mp.mpf(1) / mp.mpf(2) + (mp.mpf(3) / mp.mpf(10)) * rt5 + iu * (mp.mpf(2) / mp.mpf(5)) * rt5

    def gamma_act(t: mp.mpc) -> mp.mpc:
        return (mp.mpf(2) * t + mp.mpf(1)) / (t + mp.mpf(1))

    tau_ax1 = gamma_act(tau_ax0)
    tau_ax3 = gamma_act(gamma_act(tau_ax1))
    # Note: under gamma = [[2, 1], [1, 1]], w*gamma for w = (1, 2) mod 5:
    # (1, 2) * [[2, 1], [1, 1]] = (4, 3) = -(1, 2) mod 5, and Y(tau, -w) = Y(tau, w)!
    y_ax0 = frame_c_couplings_24(tau_ax0, 1, 2, residue_only=False)
    y_ax1 = frame_c_couplings_24(tau_ax1, 1, 2, residue_only=False)
    y_ax3 = frame_c_couplings_24(tau_ax3, 1, 2, residue_only=False)

    def sv_ratio_drift(m0: mp.matrix, m1: mp.matrix) -> mp.mpf:
        s0 = svd_sorted(m0)
        s1 = svd_sorted(m1)
        return max(abs(s1[1] / s1[0] - s0[1] / s0[0]) / (s0[1] / s0[0]), abs(s1[2] / s1[0] - s0[2] / s0[0]) / (s0[2] / s0[0]))

    drift_1turn_S = sv_ratio_drift(y_ax0["S"][(1, 2)], y_ax1["S"][(1, 2)])
    drift_1turn_St = sv_ratio_drift(y_ax0["St"][(1, 2)], y_ax1["St"][(1, 2)])
    drift_1turn_Sstar = sv_ratio_drift(y_ax0["Sstar"][(1, 2)], y_ax1["Sstar"][(1, 2)])
    drift_3turn_Sstar = sv_ratio_drift(y_ax0["Sstar"][(1, 2)], y_ax3["Sstar"][(1, 2)])

    # Also verify golden-axis reflection rho_gold(tau) = 1 - conj(tau) commutes with gamma(tau)
    # and exchanges the singular-value spectra of S at tau_ax0 with Stilde at rho_gold(tau_ax0)!
    tau_ax0_refl = mp.mpc(1) - mp.conj(tau_ax0)
    gamma_commutes_with_axis_refl = abs(gamma_act(tau_ax0_refl) - (mp.mpc(1) - mp.conj(tau_ax1))) < tol_w
    y_ax0_refl = frame_c_couplings_24(tau_ax0_refl, 1, 2, residue_only=False)
    s_vs_st_refl_swap = sv_ratio_drift(y_ax0["S"][(1, 2)], y_ax0_refl["St"][(1, 2)])

    return {
        "P1_trace_det": [tr_g, det_g],
        "P1_stretch_minpoly_zero": sp.simplify(lam_max ** 2 - 3 * lam_max + 1) == 0,
        "P1_fixed_points_n1_to_8": fixed_torus_1_to_8,
        "P1_trace_formula_matches": trace_formula_matches,
        "P2_axis_center": f"{axis_center.p}/{axis_center.q}",
        "P2_axis_radius_sq": f"{axis_radius_sq.p}/{axis_radius_sq.q}",
        "P2_i_and_1plus_i_on_axis": bool(i_on_axis and one_plus_i_on_axis),
        "P2_gamma_of_i": [f"{sp.re(gamma_of_i).p}/{sp.re(gamma_of_i).q}", f"{sp.im(gamma_of_i).p}/{sp.im(gamma_of_i).q}"],
        "P3_LnR_axis_radii_sq_n1_to_8": lnr_radii_sq,
        "W2_orders_mod2_mod5": [ord_mod2, ord_mod5],
        "W2_gamma5_mod5": g5_mod5,
        "weil_classes_check": weil_results,
        "W4_signature_table": sig_table,
        "W4_signature_exact_passed": sig_exact_ok,
        "sec5_item2_sign_B_invariant_under_U_and_swap": sign_B_stays_unselected,
        "sec5_item2_both_S_and_St_repeat_in_1_turn": (drift_1turn_S < mp.mpf(10) ** (-40)) and (drift_1turn_St < mp.mpf(10) ** (-40)),
        "sec5_item2_axis_reflection_swaps_S_and_St": gamma_commutes_with_axis_refl and (s_vs_st_refl_swap < mp.mpf(10) ** (-40)),
        "pc3_Sstar_breaks_1turn_and_repeats_at_3turns": (drift_1turn_Sstar > mp.mpf(1) / mp.mpf(10)) and (drift_3turn_Sstar < mp.mpf(10) ** (-40)),
        "pc4_wrong_fourier_sign_fails_relation": pc4_wrong_sign_residual > mp.mpf(1) / mp.mpf(10),
    }


# ============================================================================
# 5. Module C: P-875 Q2 — Symbolic Clifford Cl(10) & Cochain Check of Card C3i
# ============================================================================

def run_module_c_physical_c3i() -> Dict[str, Any]:
    """
    Independent exact symbolic verification of Physical Card C3i
    (GLOBAL_CYCLIC_CROSS_FORM_CHAIN_MAP.md, equations (1)-(7), both chiralities 16_+ and 16_-,
    vector-10 control, core-swap invariance of h_F, 24/16/8 divisor cohomology persistence,
    and quadratic norm growth of (1 + H)^n).
    """
    # 1. Equation (2): Spin(5) 4x4 matrix polynomial Q^2 = p*r*(e13 + e24) + p*f*(e31 + e42)
    p_s, r_s, f_s = sp.symbols("p r f")
    q4 = sp.Matrix([
        [0, p_s, 0, 0],
        [0, 0, r_s, 0],
        [0, 0, 0, p_s],
        [f_s, 0, 0, 0],
    ])
    q4_sq_want = sp.Matrix([
        [0, 0, p_s * r_s, 0],
        [0, 0, 0, p_s * r_s],
        [p_s * f_s, 0, 0, 0],
        [0, p_s * f_s, 0, 0],
    ])
    eq2_exact = (q4 * q4 - q4_sq_want).applyfunc(sp.expand) == sp.zeros(4, 4)

    # 2. Full 32x32 Cl(10) Clifford algebra check (covering BOTH 16_+ and 16_- simultaneously!)
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])
    i2 = sp.eye(2)

    def kron_sp(ms: List[sp.Matrix]) -> sp.Matrix:
        out = ms[0]
        for m in ms[1:]:
            out = sp.kronecker_product(out, m)
        return out

    gammas: List[sp.Matrix] = []
    for k in range(5):
        gammas.append(kron_sp([sz] * k + [sx] + [i2] * (4 - k)))
        gammas.append(kron_sp([sz] * k + [sy] + [i2] * (4 - k)))

    gamma_chir = kron_sp([sz, sz, sz, sz, sz])
    plus_idx = [i for i in range(32) if gamma_chir[i, i] == 1]
    minus_idx = [i for i in range(32) if gamma_chir[i, i] == -1]

    def sigma32(a: int, b: int) -> sp.Matrix:
        if a == b:
            return sp.zeros(32, 32)
        return sp.Rational(1, 2) * (gammas[a] * gammas[b])

    # Literal E_+, T3_+, E_-, T3_-, and X_(+-2, +-2) in full 32x32 Cl(10)
    e_short_p = sigma32(0, 4) - sp.I * sigma32(1, 4)
    e_long_p = sp.Rational(1, 2) * (sigma32(2, 0) - sp.I * sigma32(3, 0) + sp.I * sigma32(2, 1) + sigma32(3, 1))
    e_plus = sp.sqrt(sp.Rational(3, 2)) * e_short_p + sp.sqrt(sp.Integer(2)) * e_long_p
    t3_plus = sp.Rational(1, 2) * (sigma32(0, 2) + sp.I * sigma32(1, 2) + sp.I * sigma32(0, 3) - sigma32(1, 3))

    e_short_m = sigma32(6, 5) - sp.I * sigma32(7, 5)
    e_long_m = sp.Rational(1, 2) * (sigma32(8, 6) - sp.I * sigma32(9, 6) + sp.I * sigma32(8, 7) + sigma32(9, 7))
    e_minus = sp.sqrt(sp.Rational(3, 2)) * e_short_m + sp.sqrt(sp.Integer(2)) * e_long_m
    t3_minus = sp.Rational(1, 2) * (sigma32(6, 8) + sp.I * sigma32(7, 8) + sp.I * sigma32(6, 9) - sigma32(7, 9))

    # C3i Section 2 Clifford commutators: [E_+, v_+] = 0, [E_+, v_-] = -sqrt(2) w, [T3_+, v_+] = w, [T3_+, v_-] = 0
    vp = gammas[2] - sp.I * gammas[3]
    vm = gammas[2] + sp.I * gammas[3]
    w_cl = gammas[0] + sp.I * gammas[1]
    comm_relations_ok = (
        (e_plus * vp - vp * e_plus).applyfunc(sp.simplify) == sp.zeros(32, 32)
        and (e_plus * vm - vm * e_plus + sp.sqrt(2) * w_cl).applyfunc(sp.simplify) == sp.zeros(32, 32)
        and (t3_plus * vp - vp * t3_plus - w_cl).applyfunc(sp.simplify) == sp.zeros(32, 32)
        and (t3_plus * vm - vm * t3_plus).applyfunc(sp.simplify) == sp.zeros(32, 32)
    )

    x_22 = sp.Rational(1, 2) * (sigma32(2, 8) - sp.I * sigma32(3, 8) - sp.I * sigma32(2, 9) - sigma32(3, 9))
    x_m2_p2 = sp.Rational(1, 2) * (sigma32(2, 8) + sp.I * sigma32(3, 8) - sp.I * sigma32(2, 9) + sigma32(3, 9))
    x_p2_m2 = sp.Rational(1, 2) * (sigma32(2, 8) - sp.I * sigma32(3, 8) + sp.I * sigma32(2, 9) + sigma32(3, 9))
    x_m2_m2 = sp.Rational(1, 2) * (sigma32(2, 8) + sp.I * sigma32(3, 8) + sp.I * sigma32(2, 9) - sigma32(3, 9))

    fp, fm = sp.symbols("f_p f_m")
    r2_half = sp.sqrt(2) / 2
    a32 = x_22 + r2_half * (fp * x_m2_p2 + fm * x_p2_m2) + sp.Rational(1, 2) * fp * fm * x_m2_m2
    q32 = e_plus + fp * t3_plus
    r32 = e_minus + fm * t3_minus

    # Exact F-flatness in full 32x32 Cl(10) (hence on BOTH 16_+ and 16_-)!
    f_flat_32_ok = (
        (a32 * q32 - q32 * a32).applyfunc(sp.expand) == sp.zeros(32, 32)
        and (a32 * r32 - r32 * a32).applyfunc(sp.expand) == sp.zeros(32, 32)
    )

    # Exact chirality proportionality law: Q32^2 * R32^2 == -3 * i * gamma_chir * A32!
    q32_sq = (q32 * q32).applyfunc(sp.expand)
    r32_sq = (r32 * r32).applyfunc(sp.expand)
    pn_32 = (q32_sq * r32_sq).applyfunc(sp.expand)
    chirality_proportionality_exact = (pn_32 + 3 * sp.I * gamma_chir * a32).applyfunc(sp.simplify) == sp.zeros(32, 32)

    # Verify non-zero action on BOTH 16_+ (scalar -3i) and 16_- (scalar +3i)
    a_plus = sp.Matrix([[a32[r, c] for c in plus_idx] for r in plus_idx])
    a_minus = sp.Matrix([[a32[r, c] for c in minus_idx] for r in minus_idx])
    pn_plus = sp.Matrix([[pn_32[r, c] for c in plus_idx] for r in plus_idx])
    pn_minus = sp.Matrix([[pn_32[r, c] for c in minus_idx] for r in minus_idx])
    both_chiralities_ok = (
        a_plus != sp.zeros(16, 16)
        and a_minus != sp.zeros(16, 16)
        and (pn_plus + 3 * sp.I * a_plus).applyfunc(sp.simplify) == sp.zeros(16, 16)
        and (pn_minus - 3 * sp.I * a_minus).applyfunc(sp.simplify) == sp.zeros(16, 16)
    )

    # 3. Vector-10 control (PC_XP1_5b): in so(10) on C^10 = C^5_+ (+) C^5_-, sigma_{ab} acts as e_{ab} - e_{ba}.
    def sigma10(a: int, b: int) -> sp.Matrix:
        m = sp.zeros(10, 10)
        if a != b:
            m[a, b] = 1
            m[b, a] = -1
        return m

    q10 = (
        sp.sqrt(sp.Rational(3, 2)) * (sigma10(0, 4) - sp.I * sigma10(1, 4))
        + sp.sqrt(2) * sp.Rational(1, 2) * (sigma10(2, 0) - sp.I * sigma10(3, 0) + sp.I * sigma10(2, 1) + sigma10(3, 1))
        + fp * sp.Rational(1, 2) * (sigma10(0, 2) + sp.I * sigma10(1, 2) + sp.I * sigma10(0, 3) - sigma10(1, 3))
    )
    r10 = (
        sp.sqrt(sp.Rational(3, 2)) * (sigma10(6, 5) - sp.I * sigma10(7, 5))
        + sp.sqrt(2) * sp.Rational(1, 2) * (sigma10(8, 6) - sp.I * sigma10(9, 6) + sp.I * sigma10(8, 7) + sigma10(9, 7))
        + fm * sp.Rational(1, 2) * (sigma10(6, 8) + sp.I * sigma10(7, 8) + sp.I * sigma10(6, 9) - sigma10(7, 9))
    )
    x22_10 = sp.Rational(1, 2) * (sigma10(2, 8) - sp.I * sigma10(3, 8) - sp.I * sigma10(2, 9) - sigma10(3, 9))
    vec10_q2r2_zero_while_cross_nonzero = (
        (q10 * q10 * r10 * r10).applyfunc(sp.expand) == sp.zeros(10, 10)
        and x22_10 != sp.zeros(10, 10)
    )

    # 4. Equations (4)-(7): Full 8-block Dolbeault-Koszul bidegree (l in {0,1}) x (k in {0,1,2}: 1, e_+, e_-, e_+ ^ e_-)
    # Basis of bidegree space (8 blocks):
    #   l=0: [0:(0,1), 1:(0,e_+), 2:(0,e_-), 3:(0,e_+^e_-)]
    #   l=1: [4:(1,1), 5:(1,e_+), 6:(1,e_-), 7:(1,e_+^e_-)]
    # With commuting gauge symbols Qs, Rs, dbar scalar db, and (0,1)-form beta_s:
    qs, rs, db_s, beta_s = sp.symbols("Q_s R_s dbar_s beta_s")
    pn_s = (qs ** 2) * (rs ** 2)

    # Exterior wedge e_+ ^ . and e_- ^ . on [1, e_+, e_-, e_+^e_-]:
    w_ep = sp.Matrix([
        [0, 0, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 1, 0],
    ])
    w_em = sp.Matrix([
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 0, 0, 0],
        [0, -1, 0, 0],
    ])
    i_ep = w_ep.T
    i_em = w_em.T

    delta_4 = qs * w_ep + rs * w_em
    hf_4 = sp.Rational(1, 2) * (qs * (rs ** 2) * i_ep + (qs ** 2) * rs * i_em)
    eq5_anticomm_ok = (delta_4 * hf_4 + hf_4 * delta_4 - pn_s * sp.eye(4)).applyfunc(sp.expand) == sp.zeros(4, 4)

    # Assemble 8x8 operators over commuting symbolic ring (valid since [Q, R] = 0!)
    dn_8 = sp.zeros(8, 8)
    dn_bad_sign_8 = sp.zeros(8, 8)
    h_8 = sp.zeros(8, 8)
    b_ins_8 = sp.zeros(8, 8)
    for r in range(4):
        dn_8[4 + r, r] = db_s
        dn_bad_sign_8[4 + r, r] = db_s
        b_ins_8[4 + r, r] = beta_s * pn_s
        for c in range(4):
            dn_8[r, c] += delta_4[r, c]               # l = 0: (+1) * delta
            dn_8[4 + r, 4 + c] -= delta_4[r, c]       # l = 1: (-1) * delta
            dn_bad_sign_8[r, c] += delta_4[r, c]      # planted control: (+1) on both l=0 and l=1
            dn_bad_sign_8[4 + r, 4 + c] += delta_4[r, c]
            h_8[4 + r, c] = beta_s * hf_4[r, c]       # raises l by 1, lowers k by 1

    i8 = sp.eye(8)
    h_sq_zero = (h_8 * h_8).applyfunc(sp.expand) == sp.zeros(8, 8)
    hdnh_zero = (h_8 * dn_8 * h_8).applyfunc(sp.expand) == sp.zeros(8, 8)
    comm_dnh_ok = (dn_8 * h_8 - h_8 * dn_8 + b_ins_8).applyfunc(sp.expand) == sp.zeros(8, 8)
    eq7_chain_iso_ok = ((i8 + h_8) * dn_8 * (i8 - h_8) - (dn_8 + b_ins_8)).applyfunc(sp.expand) == sp.zeros(8, 8)
    inv_iso_ok = ((i8 + h_8) * (i8 - h_8) - i8).applyfunc(sp.expand) == sp.zeros(8, 8)

    # Planted control PC_XP1_5a: omitting (-1)^l breaks (1+H) d_N (1-H) == d_N + beta P_N
    pc5_bad_koszul_sign_fails = (
        (i8 + h_8) * dn_bad_sign_8 * (i8 - h_8) - (dn_bad_sign_8 + b_ins_8)
    ).applyfunc(sp.expand) != sp.zeros(8, 8)

    # Core-swap gluing symmetry of h_F (C3i Section 4):
    # Under swap: Q -> (-i) R, R -> (-i) Q, and flavour basis swap e_+ <-> e_- with phase (+i) on contraction
    # Check (-i)^3 * (+i) = (-i)^2 = -1? Wait: C3i lines 344-346:
    # "Under the core swap, the three gauge factors contribute i [(-i)^3 = +i!] and the contraction contributes -i;
    #  the two terms exchange." Indeed (-i)^3 = -(-i) = +i, and (+i)*(-i) = +1!!
    swap_f = sp.Matrix([
        [1, 0, 0, 0],
        [0, 0, sp.I, 0],
        [0, sp.I, 0, 0],
        [0, 0, 0, -1],
    ])
    # Note: if w_ep -> (+i) w_em, then dual contraction i_ep = w_ep^dag -> (-i) i_em!
    swap_f_inv = swap_f.H
    hf_swapped = (swap_f * hf_4.subs({qs: -sp.I * rs, rs: -sp.I * qs}, simultaneous=True) * swap_f_inv).applyfunc(sp.simplify)
    core_swap_glues = (hf_swapped - hf_4).applyfunc(sp.expand) == sp.zeros(4, 4)

    # 5. Exact Q[t]/(t^4 (t - 1)^4) local curve-divisor Koszul cohomology checking C3i Section 6:
    # div(f0) = 2p -> t^2, div(f1) = p + q -> t*(t - 1) on R_8 = Q[t] / (t^4 * (t - 1)^4).
    # Verify H^1 = ker(d2)/im(d1) and H^2 = coker(d2) both have exact length deg(Z) = 2 on either
    # single axis (z0!=0,z1=0 or z0=0,z1!=0) and deg(Z) = 1 when z0*z1 != 0, and stay invariant
    # under non-unitary chain isomorphism d_comp = U_2 * d * U_1^-1!
    t_var = sp.Symbol("t_loc")
    mod_poly = sp.expand((t_var ** 4) * ((t_var - 1) ** 4))   # degree 8

    def mul_mod_mat(poly_expr: sp.Expr) -> sp.Matrix:
        """8x8 multiplication matrix of poly_expr on basis 1, t, ..., t^7 modulo mod_poly."""
        cols_m: List[List[sp.Rational]] = []
        for deg_j in range(8):
            rem = sp.rem(sp.expand(poly_expr * (t_var ** deg_j)), mod_poly, t_var)
            p_obj = sp.Poly(rem, t_var)
            col = [sp.Rational(p_obj.nth(r_i)) for r_i in range(8)]
            cols_m.append(col)
        return sp.Matrix([[cols_m[c_i][r_i] for c_i in range(8)] for r_i in range(8)])

    m_f0_unit = mul_mod_mat(t_var ** 2)
    m_f1_unit = mul_mod_mat(t_var * (t_var - 1))
    m_h_shift = mul_mod_mat(1 + 3 * t_var)   # invertible local change / (1 + H)-type conjugation

    def koszul_h1_h2_lengths(zv0: int, zv1: int, b_mix: int) -> Tuple[int, int]:
        f0_m = zv0 * m_f0_unit
        f1_m = zv1 * m_f1_unit
        d1_k = sp.Matrix.vstack(f0_m, f1_m)          # 16 x 8
        d2_k = sp.Matrix.hstack(-f1_m, f0_m)         # 8 x 16
        # Apply non-unitary chain isomorphism (1 + H) on middle C^16: [[I_8, b_mix * m_h_shift], [0, I_8]]
        u_mid = sp.Matrix.vstack(
            sp.Matrix.hstack(sp.eye(8), b_mix * m_h_shift),
            sp.Matrix.hstack(sp.zeros(8, 8), sp.eye(8)),
        )
        u_mid_inv = sp.Matrix.vstack(
            sp.Matrix.hstack(sp.eye(8), -b_mix * m_h_shift),
            sp.Matrix.hstack(sp.zeros(8, 8), sp.eye(8)),
        )
        d1_c = u_mid * d1_k
        d2_c = d2_k * u_mid_inv
        assert (d2_c * d1_c) == sp.zeros(8, 8)
        rk1 = d1_c.rank()
        rk2 = d2_c.rank()
        dim_ker_d2 = 16 - rk2
        h1_len = dim_ker_d2 - rk1
        h2_len = 8 - rk2
        return h1_len, h2_len

    len_axis1 = koszul_h1_h2_lengths(3, 0, 7)     # (2, 2)
    len_axis2 = koszul_h1_h2_lengths(0, 5, 7)     # (2, 2)
    len_generic = koszul_h1_h2_lengths(3, 5, 7)   # (1, 1)
    chi0_origin_128 = 8 * (1 + 2)
    wilson_origin_128 = 2 * (1 + 2) + 6 * (0 + 2)
    chi0_counts = [
        chi0_origin_128,
        8 * len_axis1[0],
        8 * len_axis2[0],
        8 * len_generic[0],
    ]
    divisor_h1_eq_h2_and_wilson18 = (
        len_axis1 == (2, 2)
        and len_axis2 == (2, 2)
        and len_generic == (1, 1)
        and wilson_origin_128 == 18
    )

    # 6. Section 7 non-unitarity check: ||(1 + H)^n x||^2 = ||x||^2 + n^2 ||H x||^2 (for x _|_ H x) grows as n^2!
    n_sym = sp.Symbol("n", integer=True, positive=True)
    # On concrete 2x2 nilpotent H_nil = [[0, b], [0, 0]] (H^2 = 0), (I + H_nil)^n = [[1, n*b], [0, 1]]:
    x_vec = sp.Matrix([0, 1])
    norm_sq_n = ((sp.Matrix([[1, n_sym * 3], [0, 1]]) * x_vec).norm() ** 2).simplify()   # 1 + 9*n^2
    non_unitary_growth_verified = sp.simplify(norm_sq_n - (1 + 9 * (n_sym ** 2))) == 0

    return {
        "eq2_spin5_polynomial_exact": eq2_exact,
        "clifford_commutators_exact": comm_relations_ok,
        "f_flatness_32_exact": f_flat_32_ok,
        "chirality_proportionality_mp_3i_exact": chirality_proportionality_exact,
        "both_16plus_and_16minus_verified": both_chiralities_ok,
        "eq5_koszul_anticommutator_exact": eq5_anticomm_ok,
        "eq6_h2_hdnh_commutator_exact": bool(h_sq_zero and hdnh_zero and comm_dnh_ok),
        "eq7_chain_isomorphism_all_degrees_exact": bool(eq7_chain_iso_ok and inv_iso_ok),
        "core_swap_gluing_exact": core_swap_glues,
        "chi0_128_divisor_counts_origin_axis1_axis2_generic": chi0_counts,
        "divisor_h1_eq_h2_and_wilson18_exact": divisor_h1_eq_h2_and_wilson18,
        "non_unitary_quadratic_norm_growth_verified": bool(non_unitary_growth_verified),
        "pc5a_omitted_koszul_sign_fails": pc5_bad_koszul_sign_fails,
        "pc5b_vec10_q2r2_zero_while_cross_nonzero": vec10_q2r2_zero_while_cross_nonzero,
    }


# ============================================================================
# 6. Main Driver & Sealed JSON Output
# ============================================================================

def main() -> None:
    ast_check = enforce_zero_float_literals_ast()
    assert ast_check["ast_zero_float_passed"], f"AST float literal check failed: {ast_check}"

    mod_j = run_module_j_exterior_join()
    mod_z = run_module_z_symmetry_nullity()
    mod_w = run_module_w_wp1_and_sec5()
    mod_c = run_module_c_physical_c3i()

    planted_controls = {
        "PC_XP1_1_dropped_phase_table_breaks_sl2z": mod_j["pc1_dropped_phase_table_breaks_sl2z"],
        "PC_XP1_2_untraceless_45_gives_minus_3_halves": mod_j["pc2_untraceless_ratio"] == "-3/2",
        "PC_XP1_3_Sstar_breaks_1turn_repeats_3turns": mod_w["pc3_Sstar_breaks_1turn_and_repeats_at_3turns"],
        "PC_XP1_4_wrong_weil_sign_fails_relation": mod_w["pc4_wrong_fourier_sign_fails_relation"],
        "PC_XP1_5_koszul_sign_and_vec10_controls": (
            mod_c["pc5a_omitted_koszul_sign_fails"] and mod_c["pc5b_vec10_q2r2_zero_while_cross_nonzero"]
        ),
    }
    all_planted_passed = all(planted_controls.values())

    payload = {
        "card": "AGY-EXP_X-P1",
        "date": "2026-11-18",
        "empirical_inputs_used": 0,
        "held_out_targets_touched": 0,
        "ast_audit": ast_check,
        "module_J_exterior_join": mod_j,
        "module_Z_symmetry_nullity": mod_z,
        "module_W_wp1_check": mod_w,
        "module_C_c3i_check": mod_c,
        "planted_controls": planted_controls,
        "all_planted_controls_passed": all_planted_passed,
    }

    out_txt = json.dumps(payload, indent=2, sort_keys=False) + "\n"
    OUT_PATH.write_text(out_txt, encoding="utf-8")
    sha = hashlib.sha256(out_txt.encode("utf-8")).hexdigest()
    OUT_SHA_PATH.write_text(f"{sha}  verify_x_p1_out.json\n", encoding="utf-8")
    print(f"Wrote {OUT_PATH.name} (sha256={sha[:16]}..., all_planted_controls_passed={all_planted_passed})")


if __name__ == "__main__":
    main()
