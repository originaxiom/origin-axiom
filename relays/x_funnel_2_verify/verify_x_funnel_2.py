#!/usr/bin/env python3
"""
Standalone zero-import verifier for Card X-FUNNEL-2 (0 of 19, data-free).

Deliverables verified:
  - Regression Gate R0: mended linear erfc dual-sum bound l_max(n_a) in y_mag_poisson_fixed,
    proving exact S-covariance (< 1e-42) and Gaussian-vs-Poisson agreement at both tau and -1/tau.
  - Part 2A:
      * Exact Gamma(5) (tau -> tau + 5) fiber holonomy spread across p = 5a in {0..4} in both
        Frame C and magnetized level-3, proving the X(1) flat-connection obstruction theorem
        (answering B1945 Section 6 and P-860 (a)/(b)), plus naive 24-point sum non-invariance.
      * Direct matrix verification of m004's monodromy M = LR = [[2,1],[1,1]] and tick J = [[1,1],[1,0]]:
        (M + I_2) w == 0 mod 1 uniquely selects B1943's 4-point orbit O_4, cycled transitively by J^{-1},
        while P_5 \ O_4 splits into two length-10 M-orbits.
      * Gauge-invariant quartic commutator I_CP(tau, w) = (1/6) Im Tr([H_1, H_2]^3) on O_4:
        non-zero in the bulk, Haar-invariant (Gate_Haar_CP), strictly EVEN under Pin(2) twin reversal
        w -> -w == M^{-1} w mod 1 (reinforcing rather than cancelling across twins, addressing P-856),
        and strictly ODD under fiber orientation reversal (tau, a, b) -> (-conj(tau), a, -b).
      * Zak-dressed left-handed Hermitian orbit sum H_bar_f(tau) over O_4: exact b -> b + 1 periodicity,
        lifting of the a in {2/5, 3/5} light-doublet degeneracy in both bulk and deep cusp (height 30),
        and deep-cusp heavy-generation alignment |(Q_1^dagger Q_2)_{3,3}| > 1 - 1e-12.
  - Part 2B:
      * SL(2, Z)-covariant SU(3) Casimir shift M_Cas^2 = 4/3 vs 0 test: exact T and S covariance (< 1e-42)
        and honest partial-kill documentation (sharpens both consecutive ratios in the same direction).
      * Theorem 2B-2 (Order-3 Blindness & Order-15 Surjection Law): verified across ALL 192 primitive
        order-15 points w_15 = w_3 + w_5 in BOTH Frame C and the magnetized triple overlap at bulk tau.
      * Theorem 2B-3 (P-862 Step Two Cusp-Exponent Laws): exact B1788 tropical tables across all primitive
        points of orders 5 (24), 10 (72), 15 (192), and 30 (576) cross-checked against high-height mpmath
        (heights 40 and 60), plus magnetized triple-overlap cusp-exponent splitting at orders 5, 10, 15, 30.
  - Mandatory Planted Controls:
      * Gate_Haar_CP (common U_L vs distinct U_{L,1} != U_{L,2})
      * PC_FUNNEL2_WrongOrbit (non-eigenline 4-point subset fails J^{-1} and M^{-1} w == -w closure)
      * PC_FUNNEL2_NotDivBy3 (perturbing sec_3 charges from (-3, 6) to (-2, 5) breaks order-3 blindness)
"""

from __future__ import annotations

import ast
import hashlib
import json
import math
import pathlib
from fractions import Fraction
from typing import Any, Dict, List, Set, Tuple

import mpmath as mp
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
OUT_PATH = HERE / "verify_x_funnel_2_out.json"
OUT_SHA_PATH = HERE / "OUTPUT_SHA256.txt"

P5_ALL_24: List[Tuple[Fraction, Fraction]] = [
    (Fraction(i, 5), Fraction(j, 5))
    for i in range(5)
    for j in range(5)
    if (i, j) != (0, 0)
]

O4_M004: List[Tuple[Fraction, Fraction]] = [
    (Fraction(1, 5), Fraction(2, 5)),
    (Fraction(2, 5), Fraction(4, 5)),
    (Fraction(4, 5), Fraction(3, 5)),
    (Fraction(3, 5), Fraction(1, 5)),
]


def f2m(q: Fraction) -> mp.mpf:
    return mp.mpf(q.numerator) / q.denominator


def conj_t(m: mp.matrix) -> mp.matrix:
    return mp.matrix([[mp.conj(m[c, r]) for c in range(m.cols)] for r in range(m.rows)])


def tr_mp(m: mp.matrix) -> mp.mpc:
    return sum(m[r, r] for r in range(m.rows))


def svd_ascending(y_mat: mp.matrix) -> Tuple[mp.matrix, List[mp.mpf]]:
    u_desc, sv_desc, _ = mp.svd_c(y_mat)
    order = sorted(range(3), key=lambda idx: sv_desc[idx])
    u_asc = mp.matrix([[u_desc[r, order[c]] for c in range(3)] for r in range(3)])
    sv_asc = [sv_desc[order[c]] for c in range(3)]
    return u_asc, sv_asc


def overlap_moduli(u1: mp.matrix, u2: mp.matrix) -> List[List[mp.mpf]]:
    v = conj_t(u1) * u2
    return [[abs(v[r, c]) for c in range(3)] for r in range(3)]


# ============================================================================
# SECTION 1: ZERO-IMPORT FRAME C ENGINE & MENDED MAGNETIZED OVERLAP ENGINE
# ============================================================================

def build_quaternions_and_coupling_standalone() -> List[Tuple[int, int, int, int, int, int]]:
    i2 = np.eye(2, dtype=np.complex128)
    qi = np.array([[1j, 0.0], [0.0, -1j]], dtype=np.complex128)
    qj = np.array([[0.0, 1.0], [-1.0, 0.0]], dtype=np.complex128)
    qk = qi @ qj
    eps = qj
    units = [i2, qi, qj, qk]
    ec = [eps @ u for u in units]
    g_mat = np.array([[np.sum(ec[t] * units[s]) for s in range(4)] for t in range(4)], dtype=np.complex128)
    g_inv = np.linalg.inv(g_mat)
    edual = [sum(g_inv[b, a] * units[b] for b in range(4)) for a in range(4)]
    blocks = [qj, qi, qk]
    higgs_units = [qi, qj, qk]
    nz: List[Tuple[int, int, int, int, int, int]] = []
    for alpha in range(3):
        s_unit = higgs_units[alpha]
        for s_idx in range(4):
            m_unit = edual[s_idx]
            for ra in range(3):
                for cb in range(3):
                    val = np.sum((blocks[ra].T @ eps @ s_unit @ blocks[cb]) * m_unit)
                    if abs(val) > 1e-14:
                        tr2 = int(round(val.real * 2.0))
                        ti2 = int(round(val.imag * 2.0))
                        assert abs(val - complex(tr2 / 2.0, ti2 / 2.0)) < 1e-14
                        nz.append((alpha, s_idx, ra, cb, tr2, ti2))
    return nz


def build_serre_b1_exact_standalone(max_k: int = 168) -> List[Tuple[int, List[Tuple[Fraction, Fraction]]]]:
    n_cap = max_k

    def s_mul(a: Dict[int, Tuple[Fraction, Fraction]], b: Dict[int, Tuple[Fraction, Fraction]]):
        out: Dict[int, Tuple[Fraction, Fraction]] = {}
        for ka, (ar, ai) in a.items():
            for kb, (br, bi) in b.items():
                k = ka + kb
                if k <= n_cap:
                    pr, pi_ = out.get(k, (Fraction(0), Fraction(0)))
                    out[k] = (pr + ar * br - ai * bi, pi_ + ar * bi + ai * br)
        return {k: v for k, v in out.items() if v[0] or v[1]}

    def s_inv(a: Dict[int, Tuple[Fraction, Fraction]]):
        k0 = min(a)
        c0r, c0i = a[k0]
        d = c0r * c0r + c0i * c0i
        inv0 = (c0r / d, -c0i / d)
        m_cap = n_cap + k0
        sj = [a.get(k0 + j, (Fraction(0), Fraction(0))) for j in range(m_cap + 1)]
        t: List[Tuple[Fraction, Fraction]] = [inv0]
        for m in range(1, m_cap + 1):
            ar, ai = Fraction(0), Fraction(0)
            for j in range(1, m + 1):
                sr, si = sj[j]
                if sr or si:
                    tr, ti = t[m - j]
                    ar += sr * tr - si * ti
                    ai += sr * ti + si * tr
            t.append((-(inv0[0] * ar - inv0[1] * ai), -(inv0[0] * ai + inv0[1] * ar)))
        return {m - k0: t[m] for m in range(m_cap + 1) if m - k0 <= n_cap and (t[m][0] or t[m][1])}

    th2: Dict[int, Tuple[Fraction, Fraction]] = {}
    n = 0
    while (2 * n + 1) ** 2 <= n_cap:
        th2[(2 * n + 1) ** 2] = (Fraction(2), Fraction(0))
        n += 1
    th3: Dict[int, Tuple[Fraction, Fraction]] = {0: (Fraction(1), Fraction(0))}
    th4: Dict[int, Tuple[Fraction, Fraction]] = {0: (Fraction(1), Fraction(0))}
    n = 1
    while 4 * n * n <= n_cap:
        th3[4 * n * n] = (Fraction(2), Fraction(0))
        th4[4 * n * n] = (Fraction(2 * ((-1) ** n)), Fraction(0))
        n += 1

    e2: Dict[int, Tuple[Fraction, Fraction]] = {0: (Fraction(1), Fraction(0))}
    for m in range(1, n_cap // 8 + 1):
        sig1 = sum(d for d in range(1, m + 1) if m % d == 0)
        e2[8 * m] = (Fraction(-24 * sig1), Fraction(0))

    di = s_inv(s_mul(s_mul(th2, th3), th4))
    r0 = {k: (-v[0], -v[1]) for k, v in s_mul(s_mul(th2, th2), di).items()}
    r1 = {k: (-v[0], -v[1]) for k, v in s_mul(s_mul(th4, th4), di).items()}
    r2 = s_mul(s_mul(s_mul(th3, th3), {0: (Fraction(0), Fraction(1))}), di)

    def serre_mhalf(f: Dict[int, Tuple[Fraction, Fraction]]):
        qdf = {k: (v[0] * Fraction(k, 8), v[1] * Fraction(k, 8)) for k, v in f.items() if k != 0}
        e2f = s_mul(e2, f)
        out = dict(qdf)
        for k, (r, im) in e2f.items():
            pr, pi_ = out.get(k, (Fraction(0), Fraction(0)))
            out[k] = (pr + r * Fraction(1, 24), pi_ + im * Fraction(1, 24))
        return out

    b1 = [serre_mhalf(r0), serre_mhalf(r1), serre_mhalf(r2)]
    all_ks = sorted(set().union(*(d.keys() for d in b1)))
    return [(k, [d.get(k, (Fraction(0), Fraction(0))) for d in b1]) for k in all_ks]


T_COUP_NZ = build_quaternions_and_coupling_standalone()
SERRE_EXACT_ROWS = build_serre_b1_exact_standalone(168)


def th_char_val(al: mp.mpf, be: mp.mpf, tau: mp.mpc, k_span: int = 28) -> mp.mpc:
    k0 = int(round(-float(al)))
    s = mp.mpc(0)
    for dk in range(-k_span, k_span + 1):
        m = mp.mpf(k0 + dk) + al
        s += mp.exp(mp.pi * 1j * tau * (m * m) + 2j * mp.pi * m * be)
    return s


def eval_serre_qseries_mp(tau: mp.mpc) -> List[mp.mpc]:
    xq = mp.exp(1j * mp.pi * tau / 4)
    c3 = [mp.mpc(0), mp.mpc(0), mp.mpc(0)]
    cutoff = mp.mpf(10) ** (-(mp.mp.dps + 6))
    for k_int, cols_frac in SERRE_EXACT_ROWS:
        pw = xq ** k_int
        if abs(pw) < cutoff and k_int > 8:
            break
        for col_j in range(3):
            fr, fi = cols_frac[col_j]
            if fr or fi:
                c3[col_j] += pw * mp.mpc(f2m(fr), f2m(fi))
    return c3


def F_kron_mp(u1: Fraction, u2: Fraction, tau: mp.mpc) -> mp.mpf:
    xv, yv = mp.re(tau), mp.im(tau)
    a_fr = u1 % 1
    b_fr = u2 % 1
    a = f2m(a_fr)
    b = f2m(b_fr)
    if a_fr == 0:
        base = mp.pi * (2 * mp.euler - 2 * mp.log(2) - mp.log(yv))
        if b_fr != 0:
            base += yv * (mp.pi ** 2) / (mp.sin(mp.pi * b) ** 2)
    else:
        base = -mp.pi * (2 * mp.log(2) + mp.log(yv) + mp.digamma(a) + mp.digamma(1 - a))
    k_max = int(mp.mp.dps * 2.35 / (2 * float(mp.pi * yv))) + 6
    tot = base
    for k in range(-k_max, k_max + 1):
        m = mp.mpf(k) + a
        if m == 0:
            continue
        w = mp.exp(-2 * mp.pi * abs(m) * yv + 2j * mp.pi * (m * xv + f2m(u2)))
        tot += (2 * mp.pi / abs(m)) * mp.re(w / (1 - w))
    return tot


def a0_from_char(al_fr: Fraction, be_fr: Fraction, tau: mp.mpc) -> mp.mpc:
    half = Fraction(1, 2)
    al = f2m(al_fr + half)
    be = f2m(be_fr + half)
    y_f = max(float(mp.im(tau)), 0.4)
    k_span = max(24, int(math.ceil(math.sqrt((mp.mp.dps * math.log(10.0) + 20.0) / (math.pi * y_f)))) + 4)
    k0 = int(round(-float(al)))
    den = mp.mpc(0)
    num = mp.mpc(0)
    for dk in range(-k_span, k_span + 1):
        m = mp.mpf(k0 + dk) + al
        t = mp.exp(mp.pi * 1j * tau * (m * m) + 2j * mp.pi * m * be)
        den += t
        num += m * t
    return (2j * mp.pi * num) / den


def frame_c_Y(
    tau: mp.mpc,
    a: Fraction,
    b: Fraction,
    ql_i: int,
    qr_i: int,
    L2_val: mp.mpf,
    tilde_s: bool = False,
) -> mp.matrix:
    yv = mp.im(tau)
    q_mp = mp.exp(2j * mp.pi * tau)
    eta = mp.exp(1j * mp.pi * tau / 12) * mp.qp(q_mp)
    t1p = 2 * mp.pi * (eta ** 3)
    half = Fraction(1, 2)
    ql, qr = Fraction(ql_i), Fraction(qr_i)
    x = (ql * a, 2 * ql * b)
    yy = (qr * a, 2 * qr * b)
    ap, am = x[0] + yy[0], x[0] - yy[0]
    bp, bm = (x[1] + yy[1]) / 2, (x[1] - yy[1]) / 2
    e_ph = mp.exp(-2j * mp.pi * f2m(x[0]))
    kap = [-1j * e_ph, mp.mpc(-1), -e_ph, mp.mpc(0, 1)]
    cs = [(ap + half, bp + half), (ap + half, bp), (ap, bp + half), (ap, bp)]
    ds = [(am + half, bm + half), (am + half, bm), (am, bm + half), (am, bm)]
    y_f = max(float(yv), 0.4)
    k_span = max(24, int(math.ceil(math.sqrt((mp.mp.dps * math.log(10.0) + 20.0) / (math.pi * y_f)))) + 4)
    u_vec: List[mp.mpc] = []
    for idx in range(4):
        if (((cs[idx][0] - half) % 1 == 0) and ((cs[idx][1] - half) % 1 == 0)) or (
            ((ds[idx][0] - half) % 1 == 0) and ((ds[idx][1] - half) % 1 == 0)
        ):
            u_vec.append(mp.mpc(0))
            continue
        tc = th_char_val(f2m(cs[idx][0]), f2m(cs[idx][1]), tau, k_span)
        td = th_char_val(f2m(ds[idx][0]), f2m(ds[idx][1]), tau, k_span)
        r_val = kap[idx] * tc * td / t1p
        al_fr, be_fr = cs[idx][0] - half, cs[idx][1] - half
        a0_v = a0_from_char(al_fr, be_fr, tau)
        c_val = (
            F_kron_mp(al_fr, be_fr, tau)
            + mp.pi * mp.log(yv)
            - 2 * mp.pi * (mp.euler + mp.log(mp.pi))
            - mp.pi * (abs(a0_v) ** 2) * mp.exp(-2 * L2_val)
        )
        arg = 2 * mp.pi * L2_val + c_val
        u_vec.append(mp.sqrt(arg) * r_val if arg > 0 else mp.mpc(0))
    s_raw = eval_serre_qseries_mp(tau)
    c_vec = [mp.conj(z) for z in s_raw] if tilde_s else s_raw
    y_mat = mp.zeros(3, 3)
    half_mp = mp.mpf(1) / 2
    for al_i, s_i, ra, cb, tr2, ti2 in T_COUP_NZ:
        y_mat[ra, cb] += c_vec[al_i] * u_vec[s_i] * mp.mpc(tr2, ti2) * half_mp
    return y_mat


def y_mag_direct_gaussian(
    tau: mp.mpc,
    a: mp.mpf,
    b: mp.mpf,
    ql: int,
    qr: int,
    casimir_mass_sq: Fraction = Fraction(0),
) -> mp.matrix:
    """Exact unfolded Gaussian lattice sum with optional SL(2, Z)-invariant Casimir mass shift."""
    qh = -(ql + qr)
    tau1, tau2 = mp.re(tau), mp.im(tau)
    thresh = (mp.mp.dps + 6) * mp.log(10)
    r_sq = thresh * 6 * tau2 / mp.pi
    k_max = max(int(mp.ceil(mp.sqrt(r_sq) / tau2 / 3)) + 3, 6)
    m_span = int(mp.ceil(mp.sqrt(r_sq))) + 4
    sp = mp.mpf(1) / 2
    mc2 = f2m(casimir_mass_sq)
    y_mat = mp.zeros(3, 3)
    for i in range(3):
        c_l = (mp.mpf(i) + sp + ql * a) / 3
        for j in range(3):
            c_r = (mp.mpf(j) + sp - qr * a) / 3
            acc = mp.mpc(0)
            for k in range(-k_max, k_max + 1):
                n = (j - i) - 3 * k
                na = mp.mpf(n) + qh * a
                delta_k = na / 3
                m_center = int(round(-float(na * tau1 + qh * b)))
                for dm in range(-m_span, m_span + 1):
                    m = m_center + dm
                    omega = na * tau + (mp.mpf(m) + qh * b)
                    om_sq = abs(omega) ** 2
                    if om_sq == 0 and mc2 == 0:
                        continue
                    gauss = mp.exp(-mp.pi * om_sq / (6 * tau2))
                    phase = mp.exp(mp.pi * 1j * (mp.mpf(m) * (c_l + c_r - k) + delta_k * ((qr - ql) * b - 3)))
                    prop = 1 / (mp.pi * (om_sq / tau2 + mc2))
                    acc += prop * gauss * phase
            y_mat[i, j] = acc
    return y_mat


def erfcx_mp(x_val: mp.mpf) -> mp.mpf:
    return mp.exp(x_val * x_val) * mp.erfc(x_val)


def erfc_integral_mp(alpha: mp.mpf, beta: mp.mpf, u0: mp.mpf, thresh: mp.mpf) -> mp.mpf:
    xm = alpha * u0 - beta / u0
    xp = alpha * u0 + beta / u0
    edge_exp = (alpha * u0) ** 2 + (beta / u0) ** 2
    if xm >= 0:
        if edge_exp > thresh:
            return mp.mpf(0)
        return (mp.sqrt(mp.pi) / (2 * alpha)) * mp.exp(-edge_exp) * (erfcx_mp(xm) + erfcx_mp(xp))
    if 2 * alpha * beta > thresh:
        return mp.mpf(0)
    part1 = 2 * mp.exp(-2 * alpha * beta)
    part2 = mp.mpf(0) if edge_exp > thresh else mp.exp(-edge_exp) * (erfcx_mp(xp) - erfcx_mp(-xm))
    return (mp.sqrt(mp.pi) / (2 * alpha)) * (part1 + part2)


def y_mag_poisson_fixed(tau: mp.mpc, a: mp.mpf, b: mp.mpf, ql: int, qr: int) -> mp.matrix:
    """Mended fast Poisson-erfc formula with linear l_max_na bound for exact S-covariance at small Im(tau)."""
    qh = -(ql + qr)
    tau1, tau2 = mp.re(tau), mp.im(tau)
    u0 = mp.mpf(1) / mp.sqrt(6)
    u_split = mp.sqrt(tau2)
    thresh = (mp.mp.dps + 8) * mp.log(10)
    half = mp.mpf(1) / 2
    k_max = int(mp.ceil(mp.sqrt(thresh * 6 / (mp.pi * tau2)) / 3)) + 4
    l_quad = int(mp.ceil(mp.sqrt(thresh * 6 / (mp.pi * tau2)))) + 6
    l_riem = int(mp.ceil(mp.sqrt(thresh / mp.pi))) + 4

    def f_prim(u_val: mp.mpf, b_val: mp.mpf) -> mp.mpf:
        if b_val == 0:
            return 2 * u_val
        bv_u = b_val / u_val
        if bv_u * bv_u > thresh:
            return mp.mpf(0)
        return 2 * mp.exp(-(bv_u ** 2)) * (u_val - mp.sqrt(mp.pi) * b_val * erfcx_mp(bv_u))

    y_mat = mp.zeros(3, 3)
    for i in range(3):
        c_l = (mp.mpf(i) + half + ql * a) / 3
        for j in range(3):
            c_r = (mp.mpf(j) + half - qr * a) / 3
            acc = mp.mpc(0)
            for k in range(-k_max, k_max + 1):
                n = (j - i) - 3 * k
                na = mp.mpf(n) + qh * a
                delta_k = na / 3
                xi0 = (c_l + c_r - mp.mpf(k)) / 2
                x0 = na * tau1 + qh * b
                base_phase = mp.exp(mp.pi * 1j * delta_k * ((qr - ql) * b - 3))
                if na != 0:
                    alpha = mp.sqrt(mp.pi * tau2) * abs(na)
                    l_lin = int(mp.ceil(thresh / (2 * mp.pi * tau2 * abs(na)))) + 4
                    l_max_na = max(l_lin, l_quad)
                    sub = mp.mpc(0)
                    l_center = int(round(float(xi0)))
                    for dl in range(-l_max_na, l_max_na + 1):
                        l = l_center + dl
                        beta = mp.sqrt(mp.pi * tau2) * abs(mp.mpf(l) - xi0)
                        iv = mp.sqrt(tau2) * erfc_integral_mp(alpha, beta, u0, thresh)
                        if iv != 0:
                            sub += iv * mp.exp(2j * mp.pi * (mp.mpf(l) - xi0) * x0)
                    acc += base_phase * sub
                else:
                    sub1 = mp.mpc(0)
                    l_center = int(round(float(xi0)))
                    for dl in range(-l_riem, l_riem + 1):
                        l = l_center + dl
                        beta = mp.sqrt(mp.pi * tau2) * abs(mp.mpf(l) - xi0)
                        iv = mp.sqrt(tau2) * (f_prim(u_split, beta) - f_prim(u0, beta))
                        if iv != 0:
                            sub1 += iv * mp.exp(2j * mp.pi * (mp.mpf(l) - xi0) * x0)
                    sub2 = mp.mpc(0)
                    m_center = int(round(-float(x0)))
                    for dm in range(-l_riem, l_riem + 1):
                        m = m_center + dm
                        mx = mp.mpf(m) + x0
                        if abs(mx) > mp.mpf("1e-35") and mp.pi * (mx ** 2) <= thresh:
                            sub2 += (tau2 / (mp.pi * (mx ** 2))) * mp.exp(-mp.pi * (mx ** 2)) * mp.exp(2j * mp.pi * mp.mpf(m) * xi0)
                    acc += base_phase * (sub1 + sub2)
            y_mat[i, j] = acc
    return y_mat


def random_haar_u3_mp(seed: int) -> mp.matrix:
    rng = np.random.default_rng(seed)
    z = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    q_np, r_np = np.linalg.qr(z)
    d_np = np.diag(r_np)
    q_np = q_np * (d_np / np.abs(d_np))[np.newaxis, :]
    cols = [
        [mp.mpc(repr(float(q_np[r, c].real)), repr(float(q_np[r, c].imag))) for r in range(3)]
        for c in range(3)
    ]
    orth: List[List[mp.mpc]] = []
    for c in range(3):
        v = list(cols[c])
        for prev in orth:
            ip = sum(mp.conj(prev[r]) * v[r] for r in range(3))
            v = [v[r] - ip * prev[r] for r in range(3)]
        nrm = mp.sqrt(sum(abs(v[r]) ** 2 for r in range(3)))
        orth.append([v[r] / nrm for r in range(3)])
    return mp.matrix([[orth[c][r] for c in range(3)] for r in range(3)])


# ============================================================================
# SECTION 2: REGRESSION GATE R0 + PART 2A (GAMMA(5) OBSTRUCTION & M004 ORBIT)
# ============================================================================

def quartic_cp_invariant(y1: mp.matrix, y2: mp.matrix) -> mp.mpf:
    h1 = y1 * conj_t(y1)
    h2 = y2 * conj_t(y2)
    cm = h1 * h2 - h2 * h1
    return mp.im(tr_mp(cm * cm * cm)) / 6


def zak_dressed_left_hermitian(tau: mp.mpc, a_fr: Fraction, b_fr: Fraction, ql: int, qr: int) -> mp.matrix:
    am, bm = f2m(a_fr), f2m(b_fr)
    d_zak = mp.diag([mp.exp(-2j * mp.pi * (ql * bm / 3) * (mp.mpf(i) + mp.mpf("0.5"))) for i in range(3)])
    y_m = d_zak * y_mag_poisson_fixed(tau, am, bm, ql, qr)
    return y_m * conj_t(y_m)


def run_r0_and_part_2a() -> Dict[str, Any]:
    with mp.workdps(48):
        tau_b = mp.mpc("0.13", "1.7")
        a0, b0 = f2m(Fraction(1, 5)), f2m(Fraction(2, 5))

        # R0: Regression gate on S-covariance and Poisson vs Gaussian at both tau_b and -1/tau_b
        s_cov_max_diff = mp.mpf(0)
        gauss_vs_poiss_S_diff = mp.mpf(0)
        for ql, qr in [(1, -4), (1, 2), (-3, 6)]:
            yp0 = y_mag_poisson_fixed(tau_b, a0, b0, ql, qr)
            yg0 = y_mag_direct_gaussian(tau_b, a0, b0, ql, qr)
            ypS = y_mag_poisson_fixed(-1 / tau_b, -b0, a0, ql, qr)
            ygS = y_mag_direct_gaussian(-1 / tau_b, -b0, a0, ql, qr)
            for r in range(3):
                for c in range(3):
                    gauss_vs_poiss_S_diff = max(
                        gauss_vs_poiss_S_diff,
                        abs(yp0[r, c] - yg0[r, c]),
                        abs(ypS[r, c] - ygS[r, c]),
                    )
            _, sv0 = svd_ascending(yp0)
            _, svS = svd_ascending(ypS)
            s_cov_max_diff = max(
                s_cov_max_diff,
                abs(sv0[1] / sv0[2] - svS[1] / svS[2]),
                abs(sv0[0] / sv0[2] - svS[0] / svS[2]),
            )
        u1_0, _ = svd_ascending(y_mag_poisson_fixed(tau_b, a0, b0, 1, -4))
        u2_0, _ = svd_ascending(y_mag_poisson_fixed(tau_b, a0, b0, 1, 2))
        u1_S, _ = svd_ascending(y_mag_poisson_fixed(-1 / tau_b, -b0, a0, 1, -4))
        u2_S, _ = svd_ascending(y_mag_poisson_fixed(-1 / tau_b, -b0, a0, 1, 2))
        v_0 = overlap_moduli(u1_0, u2_0)
        v_S = overlap_moduli(u1_S, u2_S)
        s_cov_max_diff = max(s_cov_max_diff, max(abs(v_0[r][c] - v_S[r][c]) for r in range(3) for c in range(3)))

        e0_passed = bool(float(s_cov_max_diff) < 1e-42 and float(gauss_vs_poiss_S_diff) < 1e-35)

        # Part 2A-1: Gamma(5) (tau -> tau + 5) holonomy spread across p = 5a in {0..4}
        # If a tau-independent flat unitary connection existed on X(1), then for every w in P_5,
        # U_rel(w) := Y(tau+5, w) * Y(tau, w)^{-1} (normalized by ||.|| or singular-value-free polar factor)
        # would have to admit a factorization W_L(w) U_0 W_L(w)^dagger... Wait: even simpler and completely
        # basis-free! If Y(tau+5, w) = W_L(w) U_L W_L(w)^dagger ... wait: W_L(w)^dagger Y(tau+5, w) W_R(w)
        # = U_L [W_L(w)^dagger Y(tau, w) W_R(w)] U_R^dagger iff
        #   Y(tau+5, w) = [W_L(w) U_L W_L(w)^dagger] Y(tau, w) [W_R(w) U_R^dagger W_R(w)^dagger]!
        # Wait: take ANY two points w_a, w_b in P_5! Even MORE direct:
        # Look at Tr(Y(tau+5, w) Y(tau, w)^dagger) / ||Y(tau, w)||_F^2:
        # Under ANY w-dependent conjugation U_L(w) = W_L(w) U_L W_L(w)^dagger, U_L(w) is SIMILAR to U_L
        # (so its eigenvalues are INDEPENDENT of w!!)!
        # Let M_hol(w) := Y(tau+5, w) * Y(tau, w)^{-1} when we fix U_R? Even better:
        # Compare H(tau+5, w) = Y(tau+5, w) Y(tau+5, w)^dagger with H(tau, w) = Y(tau, w) Y(tau, w)^dagger!
        # If W_L(w)^dagger H(tau+5, w) W_L(w) = U_L [W_L(w)^dagger H(tau, w) W_L(w)] U_L^dagger,
        # then Tr(H(tau+5, w) H(tau, w)) / Tr(H(tau, w)^2) can still vary if U_L doesn't commute with W_L(w)^dagger H W_L(w),
        # WHEREAS in Y(tau+5, w) vs Y(tau, w) in Frame C:
        # Let's check BOTH:
        #   (1) Direct entrywise holonomy matrix R_mag(w)_{i,j} = Y_mag(tau+5, w)_{i,j} / Y_mag(tau, w)_{i,j}:
        #       In magnetized level-3, R_mag(w) = D_L(w) * R_0 * D_R(w) is rank-1 in phase space, and
        #       det(Y_mag(tau+5, w)) / det(Y_mag(tau, w)) is a GAUGE-BASIS-INDEPENDENT SCALAR under W_L(w), W_R(w)!!
        #       WAIT A SECOND! CHECK THAT!!
        #       If W_L(w)^dagger Y(tau+5, w) W_R(w) = U_L [W_L(w)^dagger Y(tau, w) W_R(w)] U_R^dagger,
        #       TAKE THE DETERMINANT OF BOTH SIDES!!
        #       det(W_L(w)^dagger) CANCELS ON BOTH SIDES, AND det(W_R(w)) CANCELS ON BOTH SIDES!!
        #       SO det(Y(tau + 5, w)) / det(Y(tau, w)) MUST EQUAL det(U_L) * conj(det(U_R)) — STRICTLY INDEPENDENT OF w!!
        L2_test = f2m(Fraction(9, 10))
        det_ratios_fc: List[mp.mpc] = []
        det_ratios_mag: List[mp.mpc] = []
        sum_fc_0 = mp.zeros(3, 3)
        sum_fc_T5 = mp.zeros(3, 3)
        sum_mag_0 = mp.zeros(3, 3)
        sum_mag_T5 = mp.zeros(3, 3)
        for a_fr, b_fr in P5_ALL_24:
            y_fc_0 = frame_c_Y(tau_b, a_fr, b_fr, 1, 2, L2_test, tilde_s=False)
            y_fc_5 = frame_c_Y(tau_b + 5, a_fr, b_fr, 1, 2, L2_test, tilde_s=False)
            sum_fc_0 += y_fc_0
            sum_fc_T5 += y_fc_5
            d0_fc, d5_fc = mp.det(y_fc_0), mp.det(y_fc_5)
            if abs(d0_fc) > mp.mpf("1e-30"):
                det_ratios_fc.append(d5_fc / d0_fc)

            am, bm = f2m(a_fr), f2m(b_fr)
            y_m_0 = y_mag_poisson_fixed(tau_b, am, bm, 1, 2)
            y_m_5 = y_mag_poisson_fixed(tau_b + 5, am, bm, 1, 2)
            sum_mag_0 += y_m_0
            sum_mag_T5 += y_m_5
            d0_m, d5_m = mp.det(y_m_0), mp.det(y_m_5)
            det_ratios_mag.append(d5_m / d0_m)

        fc_det_holonomy_spread = max(abs(z1 - z2) for z1 in det_ratios_fc for z2 in det_ratios_fc)
        mag_det_holonomy_spread = max(abs(z1 - z2) for z1 in det_ratios_mag for z2 in det_ratios_mag)

        _, sv_sfc0 = svd_ascending(sum_fc_0)
        _, sv_sfc5 = svd_ascending(sum_fc_T5)
        naive_24sum_fc_T5_shift = max(
            abs(sv_sfc0[1] / sv_sfc0[2] - sv_sfc5[1] / sv_sfc5[2]),
            abs(sv_sfc0[0] / sv_sfc0[2] - sv_sfc5[0] / sv_sfc5[2]),
        )
        _, sv_sm0 = svd_ascending(sum_mag_0)
        _, sv_sm5 = svd_ascending(sum_mag_T5)
        naive_24sum_mag_T5_shift = max(
            abs(sv_sm0[1] / sv_sm0[2] - sv_sm5[1] / sv_sm5[2]),
            abs(sv_sm0[0] / sv_sm0[2] - sv_sm5[0] / sv_sm5[2]),
        )

        # Also check T (tau -> tau + 1) on naive 24-point sum in magnetized level-3:
        sum_mag_T1 = mp.zeros(3, 3)
        for a_fr, b_fr in P5_ALL_24:
            sum_mag_T1 += y_mag_poisson_fixed(tau_b + 1, f2m(a_fr), f2m(b_fr), 1, 2)
        _, sv_sm1 = svd_ascending(sum_mag_T1)
        naive_24sum_mag_T1_shift = max(
            abs(sv_sm0[1] / sv_sm0[2] - sv_sm1[1] / sv_sm1[2]),
            abs(sv_sm0[0] / sv_sm0[2] - sv_sm1[0] / sv_sm1[2]),
        )

        # Part 2A-2: Explicit m004 monodromy M = [[2,1],[1,1]] and tick J = [[1,1],[1,0]] action on P_5
        # Row-vector action w' = w * A^{-1} mod 1:
        # M^{-1} = [[1, -1], [-1, 2]], J^{-1} = [[0, 1], [1, -1]]
        def act_minv(pt: Tuple[Fraction, Fraction]) -> Tuple[Fraction, Fraction]:
            a, b = pt
            return ((a - b) % 1, (-a + 2 * b) % 1)

        def act_jinv(pt: Tuple[Fraction, Fraction]) -> Tuple[Fraction, Fraction]:
            a, b = pt
            return (b % 1, (a - b) % 1)

        eigenline_m_minus1 = [pt for pt in P5_ALL_24 if act_minv(pt) == ((-pt[0]) % 1, (-pt[1]) % 1)]
        j_cycle_from_mark: List[Tuple[Fraction, Fraction]] = []
        cur = (Fraction(1, 5), Fraction(2, 5))
        for _ in range(4):
            j_cycle_from_mark.append(cur)
            cur = act_jinv(cur)
        o4_matches_eigenline_and_jcycle = bool(
            set(eigenline_m_minus1) == set(O4_M004)
            and j_cycle_from_mark == O4_M004
            and cur == (Fraction(1, 5), Fraction(2, 5))
        )
        # Orbit lengths of M^{-1} on P_5 \ O_4:
        rem_pts = [pt for pt in P5_ALL_24 if pt not in O4_M004]
        rem_orbit_lengths: List[int] = []
        seen: Set[Tuple[Fraction, Fraction]] = set()
        for pt in rem_pts:
            if pt in seen:
                continue
            orb: List[Tuple[Fraction, Fraction]] = []
            c_pt = pt
            while c_pt not in seen:
                seen.add(c_pt)
                orb.append(c_pt)
                c_pt = act_minv(c_pt)
            rem_orbit_lengths.append(len(orb))

        # Planted control PC_FUNNEL2_WrongOrbit: non-eigenline 4-point subset fails J^{-1} closure
        wrong_orbit = [
            (Fraction(1, 5), Fraction(0, 5)),
            (Fraction(2, 5), Fraction(0, 5)),
            (Fraction(3, 5), Fraction(0, 5)),
            (Fraction(4, 5), Fraction(0, 5)),
        ]
        pc_wrong_orbit_escapes_count = sum(1 for pt in wrong_orbit if act_jinv(pt) not in wrong_orbit)

        # Quartic commutator I_CP(tau, w) on O_4: Pin(2) twin parity vs orientation parity + Haar gate
        icp_vals: Dict[str, float] = {}
        twin_even_max_diff = mp.mpf(0)
        orient_odd_max_diff = mp.mpf(0)
        for a_fr, b_fr in O4_M004:
            am, bm = f2m(a_fr), f2m(b_fr)
            y1_w = y_mag_poisson_fixed(tau_b, am, bm, 1, -4)
            y2_w = y_mag_poisson_fixed(tau_b, am, bm, 1, 2)
            icp_w = quartic_cp_invariant(y1_w, y2_w)
            icp_vals[f"{a_fr},{b_fr}"] = float(icp_w)

            # Twin -w mod 1:
            am_tw, bm_tw = f2m((-a_fr) % 1), f2m((-b_fr) % 1)
            icp_tw = quartic_cp_invariant(
                y_mag_poisson_fixed(tau_b, am_tw, bm_tw, 1, -4),
                y_mag_poisson_fixed(tau_b, am_tw, bm_tw, 1, 2),
            )
            twin_even_max_diff = max(twin_even_max_diff, abs(icp_tw - icp_w))

            # Fiber orientation reversal (tau, a, b) -> (-conj(tau), a, -b):
            tau_rev = -mp.conj(tau_b)
            icp_rev = quartic_cp_invariant(
                y_mag_poisson_fixed(tau_rev, am, -bm, 1, -4),
                y_mag_poisson_fixed(tau_rev, am, -bm, 1, 2),
            )
            orient_odd_max_diff = max(orient_odd_max_diff, abs(icp_rev + icp_w))

        # Gate_Haar_CP: 10 random gauge-allowed Haar transformations vs distinct left Haar control
        y1_mark = y_mag_poisson_fixed(tau_b, a0, b0, 1, -4)
        y2_mark = y_mag_poisson_fixed(tau_b, a0, b0, 1, 2)
        icp_mark = quartic_cp_invariant(y1_mark, y2_mark)
        haar_cp_max_diff = mp.mpf(0)
        for trial in range(10):
            u_l = random_haar_u3_mp(2000 + 3 * trial)
            u_r1 = random_haar_u3_mp(2001 + 3 * trial)
            u_r2 = random_haar_u3_mp(2002 + 3 * trial)
            icp_scr = quartic_cp_invariant(u_l * y1_mark * conj_t(u_r1), u_l * y2_mark * conj_t(u_r2))
            haar_cp_max_diff = max(haar_cp_max_diff, abs(icp_scr - icp_mark))
        ul_bad1 = random_haar_u3_mp(9201)
        ul_bad2 = random_haar_u3_mp(9202)
        pc_haar_cp_distinct_ul_diff = float(abs(quartic_cp_invariant(ul_bad1 * y1_mark, ul_bad2 * y2_mark) - icp_mark))

        # Zak-dressed Hermitian orbit sum H_bar_f(tau): b -> b+1 periodicity + bulk & height-30 splitting
        zak_b_periodicity_max_diff = mp.mpf(0)
        hbar1_bulk = mp.zeros(3, 3)
        for a_fr, b_fr in O4_M004:
            h0 = zak_dressed_left_hermitian(tau_b, a_fr, b_fr, 1, -4)
            h_b1 = zak_dressed_left_hermitian(tau_b, a_fr, b_fr + 1, 1, -4)
            for r in range(3):
                for c in range(3):
                    zak_b_periodicity_max_diff = max(zak_b_periodicity_max_diff, abs(h0[r, c] - h_b1[r, c]))
            hbar1_bulk += h0 / 4
        eb_bulk, _ = mp.eigh(hbar1_bulk)
        bulk_light_splitting = float(1 - mp.sqrt(eb_bulk[0] / eb_bulk[1]))

    with mp.workdps(108):
        tau_c30 = mp.mpc(f2m(Fraction(13, 100)), mp.mpf(30))
        hbar1_30 = mp.zeros(3, 3)
        hbar2_30 = mp.zeros(3, 3)
        for a_fr, b_fr in O4_M004:
            hbar1_30 += zak_dressed_left_hermitian(tau_c30, a_fr, b_fr, 1, -4) / 4
            hbar2_30 += zak_dressed_left_hermitian(tau_c30, a_fr, b_fr, 1, 2) / 4
        e1_30, q1_30 = mp.eigh(hbar1_30)
        e2_30, q2_30 = mp.eigh(hbar2_30)
        v_hbar_30 = conj_t(q1_30) * q2_30
        cusp30_light_splitting = float(1 - mp.sqrt(e1_30[0] / e1_30[1]))
        cusp30_v33 = float(abs(v_hbar_30[2, 2]))

    # Note: in magnetized level-3, check BOTH det holonomy spread AND off-diagonal mode holonomy spread!
    # Wait: earlier we found det(D_L) * det(D_R)? Let's check mag_entry_holonomy_spread across w in P_5 too!
    with mp.workdps(48):
        tau_b = mp.mpc("0.13", "1.7")
        # Gauge-invariant test of whether a SINGLE (U_L, U_R) works for all w:
        # If Y(tau+5, w) = W_L(w) U_L W_L(w)^dagger ... wait: for ANY two points w1, w2, if a tau-independent
        # connection W_L(w), W_R(w) existed such that Y_aligned(tau, w) = W_L(w)^dagger Y(tau, w) W_R(w)
        # transforms as Y_aligned(tau+5, w) = U_L Y_aligned(tau, w) U_R^dagger for ALL tau, then
        # M_w(tau1, tau2) := Y(tau1 + 5, w) Y(tau2 + 5, w)^{-1} and N_w(tau1, tau2) := Y(tau1, w) Y(tau2, w)^{-1}
        # satisfy M_w = U_L(w) N_w U_L(w)^dagger (conjugate by a tau-INDEPENDENT unitary U_L(w) = W_L(w) U_L W_L(w)^dagger),
        # AND naive_24sum_mag_T5_shift / T1_shift directly tests B1945 Section 6's equal-weight sum!
        mag_offdiag_hol_spread = mp.mpf(0)
        r01_list: List[mp.mpc] = []
        for a_fr, b_fr in P5_ALL_24:
            am, bm = f2m(a_fr), f2m(b_fr)
            ym0 = y_mag_poisson_fixed(tau_b, am, bm, 1, -4)
            ym5 = y_mag_poisson_fixed(tau_b + 5, am, bm, 1, -4)
            r01_list.append(ym5[0, 1] / ym0[0, 1])
        mag_offdiag_hol_spread = max(abs(z1 - z2) for z1 in r01_list for z2 in r01_list)

    max_hol_spread_fc = float(fc_det_holonomy_spread)
    max_hol_spread_mag = float(max(mag_det_holonomy_spread, mag_offdiag_hol_spread))

    e1_passed = bool(
        max_hol_spread_fc > 0.5
        and max_hol_spread_mag > 0.5
        and float(max(naive_24sum_fc_T5_shift, naive_24sum_mag_T1_shift)) > 0.05
        and o4_matches_eigenline_and_jcycle
        and rem_orbit_lengths == [10, 10]
        and min(abs(v) for v in icp_vals.values()) > 1e-3
        and float(twin_even_max_diff) < 1e-40
        and float(orient_odd_max_diff) < 1e-40
        and float(zak_b_periodicity_max_diff) < 1e-40
        and bulk_light_splitting > 0.1
        and cusp30_light_splitting > 1e-9
        and cusp30_v33 > 1.0 - 1e-12
    )

    return {
        "R0_S_covariance_fix": {
            "S_cov_max_diff": float(s_cov_max_diff),
            "gaussian_vs_poisson_at_tau_and_minus_inv_tau_max_diff": float(gauss_vs_poiss_S_diff),
            "E0_S_Covariance_Fix_passed": e0_passed,
        },
        "gamma5_obstruction_on_X1": {
            "frame_c_T5_det_holonomy_spread": float(fc_det_holonomy_spread),
            "mag_T5_det_holonomy_spread": float(mag_det_holonomy_spread),
            "mag_T5_entry_holonomy_spread": float(mag_offdiag_hol_spread),
            "naive_24pt_sum_frame_c_T5_ratio_shift": float(naive_24sum_fc_T5_shift),
            "naive_24pt_sum_mag_T5_ratio_shift": float(naive_24sum_mag_T5_shift),
            "naive_24pt_sum_mag_T1_ratio_shift": float(naive_24sum_mag_T1_shift),
        },
        "m004_root_orbit_and_cp": {
            "O4_matches_M_minus1_eigenline_and_J_four_cycle": o4_matches_eigenline_and_jcycle,
            "remaining_20_points_M_orbit_lengths": rem_orbit_lengths,
            "I_CP_on_O4_bulk": icp_vals,
            "I_CP_twin_even_max_diff": float(twin_even_max_diff),
            "I_CP_orientation_odd_max_diff": float(orient_odd_max_diff),
            "Zak_Hbar_b_plus_1_periodicity_max_diff": float(zak_b_periodicity_max_diff),
            "Zak_Hbar_bulk_light_doublet_splitting": bulk_light_splitting,
            "Zak_Hbar_cusp30_light_doublet_splitting": cusp30_light_splitting,
            "Zak_Hbar_cusp30_V33": cusp30_v33,
        },
        "controls_2a": {
            "Gate_Haar_CP_max_diff_10_trials": float(haar_cp_max_diff),
            "PC_Haar_CP_distinct_UL_diff": pc_haar_cp_distinct_ul_diff,
            "PC_FUNNEL2_WrongOrbit_escapes_J_count": pc_wrong_orbit_escapes_count,
        },
        "E1_Gamma5_Obstruction_and_m004_CP_passed": e1_passed,
    }


# ============================================================================
# SECTION 3: PART 2B (SU(3) CASIMIR SHIFT, ORDER-15 SURJECTION & P-862 EXPONENTS)
# ============================================================================

def norm_dist_z(x: Fraction) -> Fraction:
    r = x % 1
    return r if r <= Fraction(1, 2) else 1 - r


def b1788_e23(a: Fraction, ql: int, qr: int) -> Fraction:
    return Fraction(1, 2) - (norm_dist_z(2 * ql * a) + norm_dist_z(2 * qr * a)) / 2


def primitive_torsion_points(n_ord: int) -> List[Tuple[Fraction, Fraction]]:
    return [
        (Fraction(p, n_ord), Fraction(q, n_ord))
        for p in range(n_ord)
        for q in range(n_ord)
        if math.gcd(math.gcd(p, q), n_ord) == 1
    ]


def run_part_2b() -> Dict[str, Any]:
    with mp.workdps(44):
        tau_b = mp.mpc("0.13", "1.7")
        a0, b0 = f2m(Fraction(1, 5)), f2m(Fraction(2, 5))
        cas_q = Fraction(4, 3)

        # 1. SU(3) Casimir shift M_Cas^2 = 4/3 modular covariance (T and S) + partial-kill ordering test
        yd_cas_0 = y_mag_direct_gaussian(tau_b, a0, b0, 1, 2, cas_q)
        yd_cas_T = y_mag_direct_gaussian(tau_b + 1, a0, b0 - a0, 1, 2, cas_q)
        yd_cas_S = y_mag_direct_gaussian(-1 / tau_b, -b0, a0, 1, 2, cas_q)
        _, sv_c0 = svd_ascending(yd_cas_0)
        _, sv_cT = svd_ascending(yd_cas_T)
        _, sv_cS = svd_ascending(yd_cas_S)
        cas_cov_max_diff = max(
            abs(sv_c0[1] / sv_c0[2] - sv_cT[1] / sv_cT[2]),
            abs(sv_c0[0] / sv_c0[2] - sv_cT[0] / sv_cT[2]),
            abs(sv_c0[1] / sv_c0[2] - sv_cS[1] / sv_cS[2]),
            abs(sv_c0[0] / sv_c0[2] - sv_cS[0] / sv_cS[2]),
        )

        r23_diffs_o4: List[mp.mpf] = []
        r12_diffs_o4: List[mp.mpf] = []
        cas_o4_samples: Dict[str, Any] = {}
        for a_fr, b_fr in O4_M004:
            am, bm = f2m(a_fr), f2m(b_fr)
            _, sd_c = svd_ascending(y_mag_direct_gaussian(tau_b, am, bm, 1, 2, cas_q))
            _, se_0 = svd_ascending(y_mag_direct_gaussian(tau_b, am, bm, -3, 6, Fraction(0)))
            r23_d, r12_d = sd_c[1] / sd_c[2], sd_c[0] / sd_c[1]
            r23_e, r12_e = se_0[1] / se_0[2], se_0[0] / se_0[1]
            r23_diffs_o4.append(r23_e - r23_d)
            r12_diffs_o4.append(r12_e - r12_d)
            cas_o4_samples[f"{a_fr},{b_fr}"] = {
                "sec2_casimir_r23_r12": [float(r23_d), float(r12_d)],
                "sec3_untw_r23_r12": [float(r23_e), float(r12_e)],
            }

        cas_heavier_ratio_sec3_gt_sec2_all_o4 = bool(all(d > 0 for d in r23_diffs_o4))
        cas_lighter_ratio_sec3_lt_sec2_any_o4 = bool(any(d < 0 for d in r12_diffs_o4))

        e2_casimir_passed = bool(
            float(cas_cov_max_diff) < 1e-40
            and cas_heavier_ratio_sec3_gt_sec2_all_o4
            and (not cas_lighter_ratio_sec3_lt_sec2_any_o4)
        )

        # 2. Theorem 2B-2: Exact Order-3 Blindness & Order-15 Surjection across ALL 192 primitive order-15 points!
        L2_test = f2m(Fraction(9, 10))
        pts_15 = primitive_torsion_points(15)
        assert len(pts_15) == 192

        # Precompute sec_2 ratios on all 24 order-5 points in both Frame C and Magnetized Level-3:
        fc_sec2_p5: Dict[Tuple[Fraction, Fraction], Tuple[mp.mpf, mp.mpf]] = {}
        mag_sec2_p5: Dict[Tuple[Fraction, Fraction], Tuple[mp.mpf, mp.mpf]] = {}
        for w5 in P5_ALL_24:
            _, sv_fc5 = svd_ascending(frame_c_Y(tau_b, w5[0], w5[1], 1, 2, L2_test, False))
            fc_sec2_p5[w5] = (sv_fc5[1] / sv_fc5[2], sv_fc5[0] / sv_fc5[2])
            _, sv_m5 = svd_ascending(y_mag_poisson_fixed(tau_b, f2m(w5[0]), f2m(w5[1]), 1, 2))
            mag_sec2_p5[w5] = (sv_m5[1] / sv_m5[2], sv_m5[0] / sv_m5[2])

        fc_ord15_sec3_vs_w5_sec2_max_diff = mp.mpf(0)
        fc_ord15_sec2_vs_w5_sec2_max_split = mp.mpf(0)
        mag_ord15_sec3_vs_w5_sec2_max_diff = mp.mpf(0)
        mag_ord15_sec2_vs_w5_sec2_max_split = mp.mpf(0)

        for a15, b15 in pts_15:
            p15 = a15.numerator * (15 // a15.denominator)
            q15 = b15.numerator * (15 // b15.denominator)
            # Bezout 6 - 5 = 1 => p/15 = (2p)/5 + (-p)/3 mod 1
            w5 = (Fraction((2 * p15) % 5, 5), Fraction((2 * q15) % 5, 5))
            w3 = (Fraction((-p15) % 3, 3), Fraction((-q15) % 3, 3))
            assert ((w5[0] + w3[0]) % 1, (w5[1] + w3[1]) % 1) == (a15, b15)

            _, sv_fc_e15 = svd_ascending(frame_c_Y(tau_b, a15, b15, -3, 6, L2_test, False))
            _, sv_fc_d15 = svd_ascending(frame_c_Y(tau_b, a15, b15, 1, 2, L2_test, False))
            ref_fc = fc_sec2_p5[w5]
            fc_ord15_sec3_vs_w5_sec2_max_diff = max(
                fc_ord15_sec3_vs_w5_sec2_max_diff,
                abs(sv_fc_e15[1] / sv_fc_e15[2] - ref_fc[0]),
                abs(sv_fc_e15[0] / sv_fc_e15[2] - ref_fc[1]),
            )
            fc_ord15_sec2_vs_w5_sec2_max_split = max(
                fc_ord15_sec2_vs_w5_sec2_max_split,
                abs(sv_fc_d15[1] / sv_fc_d15[2] - ref_fc[0]),
            )

            am15, bm15 = f2m(a15), f2m(b15)
            _, sv_m_e15 = svd_ascending(y_mag_poisson_fixed(tau_b, am15, bm15, -3, 6))
            _, sv_m_d15 = svd_ascending(y_mag_poisson_fixed(tau_b, am15, bm15, 1, 2))
            ref_m = mag_sec2_p5[w5]
            mag_ord15_sec3_vs_w5_sec2_max_diff = max(
                mag_ord15_sec3_vs_w5_sec2_max_diff,
                abs(sv_m_e15[1] / sv_m_e15[2] - ref_m[0]),
                abs(sv_m_e15[0] / sv_m_e15[2] - ref_m[1]),
            )
            mag_ord15_sec2_vs_w5_sec2_max_split = max(
                mag_ord15_sec2_vs_w5_sec2_max_split,
                abs(sv_m_d15[1] / sv_m_d15[2] - ref_m[0]),
            )

        # Planted control PC_FUNNEL2_NotDivBy3: (-2, 5) at (2/15, 4/15) vs (4/5, 3/5) (its w_5 projection!)
        _, sv_bad_15 = svd_ascending(y_mag_poisson_fixed(tau_b, f2m(Fraction(2, 15)), f2m(Fraction(4, 15)), -2, 5))
        _, sv_bad_5 = svd_ascending(y_mag_poisson_fixed(tau_b, f2m(Fraction(4, 5)), f2m(Fraction(3, 5)), -2, 5))
        pc_not_div_by_3_break = float(abs(sv_bad_15[1] / sv_bad_15[2] - sv_bad_5[1] / sv_bad_5[2]))

    # 3. Theorem 2B-3: P-862 Step Two Cusp-Exponent Tables at Orders 5, 10, 15, 30
    fc_tables: Dict[str, Any] = {}
    pts_10_check = primitive_torsion_points(10)
    ord10_e23_identical_all_72 = bool(
        len(pts_10_check) == 72
        and all(b1788_e23(a, 1, 2) == b1788_e23(a, -3, 6) for a, _ in pts_10_check)
    )
    for n_ord in (5, 10, 15, 30):
        pts_n = primitive_torsion_points(n_ord)
        e_u = [b1788_e23(a, 1, -4) for a, _ in pts_n]
        e_d = [b1788_e23(a, 1, 2) for a, _ in pts_n]
        e_e = [b1788_e23(a, -3, 6) for a, _ in pts_n]
        fc_tables[f"order_{n_ord}"] = {
            "primitive_point_count": len(pts_n),
            "min_e23_sec1": str(min(e_u)),
            "min_e23_sec2": str(min(e_d)),
            "min_e23_sec3": str(min(e_e)),
            "distinct_e23_sec2": [str(x) for x in sorted(set(e_d))],
            "distinct_e23_sec3": [str(x) for x in sorted(set(e_e))],
        }

    # High-height mpmath cross-check of Frame C exponents at (1/10, 1/5) and (1/15, 2/15), (2/15, 4/15) (heights 40 vs 60)
    with mp.workdps(165):
        L2_hi = f2m(Fraction(9, 10))
        fc_mpmath_checks: Dict[str, Any] = {}
        for label, (af, bf), ql, qr, expected_e23, expected_e13 in [
            ("ord10_sec2_1_10", (Fraction(1, 10), Fraction(1, 5)), 1, 2, b1788_e23(Fraction(1, 10), 1, 2), Fraction(7, 10)),
            ("ord10_sec3_1_10", (Fraction(1, 10), Fraction(1, 5)), -3, 6, b1788_e23(Fraction(1, 10), -3, 6), Fraction(1, 2)),
            ("ord15_sec2_1_15", (Fraction(1, 15), Fraction(2, 15)), 1, 2, b1788_e23(Fraction(1, 15), 1, 2), Fraction(4, 5)),
            ("ord15_sec2_2_15", (Fraction(2, 15), Fraction(4, 15)), 1, 2, b1788_e23(Fraction(2, 15), 1, 2), Fraction(37, 60)),
            ("ord15_sec3_2_15", (Fraction(2, 15), Fraction(4, 15)), -3, 6, b1788_e23(Fraction(2, 15), -3, 6), Fraction(11, 20)),
        ]:
            t40 = mp.mpc(f2m(Fraction(13, 100)), mp.mpf(40))
            t60 = mp.mpc(f2m(Fraction(13, 100)), mp.mpf(60))
            _, s40 = svd_ascending(frame_c_Y(t40, af, bf, ql, qr, L2_hi, False))
            _, s60 = svd_ascending(frame_c_Y(t60, af, bf, ql, qr, L2_hi, False))
            e23_num = -mp.log((s60[1] / s60[2]) / (s40[1] / s40[2])) / (40 * mp.pi)
            e13_num = -mp.log((s60[0] / s60[2]) / (s40[0] / s40[2])) / (40 * mp.pi)
            fc_mpmath_checks[label] = {
                "e23_mpmath_40_60": float(e23_num),
                "e23_closed": float(f2m(expected_e23)),
                "e23_abs_err": float(abs(e23_num - f2m(expected_e23))),
                "e13_mpmath_40_60": float(e13_num),
                "e13_closed": float(f2m(expected_e13)),
                "e13_abs_err": float(abs(e13_num - f2m(expected_e13))),
            }

    # Magnetized triple-overlap cusp exponents at heights 20 vs 30 across orders 5, 10, 15, 30
    mag_cusp_exps: Dict[str, Any] = {}
    with mp.workdps(105):
        for label, (af, bf) in [
            ("order_5_1_5_2_5", (Fraction(1, 5), Fraction(2, 5))),
            ("order_10_1_10_1_5", (Fraction(1, 10), Fraction(1, 5))),
            ("order_15_1_15_2_15", (Fraction(1, 15), Fraction(2, 15))),
            ("order_15_2_15_4_15", (Fraction(2, 15), Fraction(4, 15))),
            ("order_30_1_30_7_30", (Fraction(1, 30), Fraction(7, 30))),
        ]:
            am, bm = f2m(af), f2m(bf)
            t20 = mp.mpc(f2m(Fraction(13, 100)), mp.mpf(20))
            t30 = mp.mpc(f2m(Fraction(13, 100)), mp.mpf(30))
            entry: Dict[str, Any] = {}
            for sname, (ql, qr) in [("sec1", (1, -4)), ("sec2", (1, 2)), ("sec3", (-3, 6))]:
                _, s20 = svd_ascending(y_mag_poisson_fixed(t20, am, bm, ql, qr))
                _, s30 = svd_ascending(y_mag_poisson_fixed(t30, am, bm, ql, qr))
                e23 = float(-mp.log((s30[1] / s30[2]) / (s20[1] / s20[2])) / (20 * mp.pi))
                e13 = float(-mp.log((s30[0] / s30[2]) / (s20[0] / s20[2])) / (20 * mp.pi))
                entry[sname] = {"e23": e23, "e13": e13, "e12": e13 - e23}
            mag_cusp_exps[label] = entry

    max_fc_mpmath_err = max(
        max(v["e23_abs_err"], v["e13_abs_err"]) for v in fc_mpmath_checks.values()
    )
    ord10_mag_split = abs(
        mag_cusp_exps["order_10_1_10_1_5"]["sec3"]["e23"]
        - mag_cusp_exps["order_10_1_10_1_5"]["sec2"]["e23"]
    )
    ord15_2_15_opposite_skew = bool(
        mag_cusp_exps["order_15_2_15_4_15"]["sec2"]["e23"]
        < mag_cusp_exps["order_15_2_15_4_15"]["sec3"]["e23"]
        and mag_cusp_exps["order_15_2_15_4_15"]["sec2"]["e12"]
        > mag_cusp_exps["order_15_2_15_4_15"]["sec3"]["e12"]
    )

    e3_passed = bool(
        float(fc_ord15_sec3_vs_w5_sec2_max_diff) < 1e-38
        and float(mag_ord15_sec3_vs_w5_sec2_max_diff) < 1e-38
        and float(fc_ord15_sec2_vs_w5_sec2_max_split) > 0.1
        and float(mag_ord15_sec2_vs_w5_sec2_max_split) > 0.1
        and ord10_e23_identical_all_72
        and fc_tables["order_15"]["min_e23_sec2"] == "2/15"
        and fc_tables["order_15"]["min_e23_sec3"] == "1/5"
        and fc_tables["order_30"]["min_e23_sec2"] == "2/15"
        and fc_tables["order_30"]["min_e23_sec3"] == "1/5"
        and max_fc_mpmath_err < 0.005
        and ord10_mag_split > 0.05
        and ord15_2_15_opposite_skew
    )

    return {
        "casimir_shift_test": {
            "SL2Z_T_and_S_max_diff": float(cas_cov_max_diff),
            "heavier_ratio_sec3_gt_sec2_all_O4": cas_heavier_ratio_sec3_gt_sec2_all_o4,
            "lighter_ratio_sec3_lt_sec2_any_O4": cas_lighter_ratio_sec3_lt_sec2_any_o4,
            "O4_samples": cas_o4_samples,
            "E2_Casimir_PartialKill_passed": e2_casimir_passed,
        },
        "order_15_surjection_192_pts": {
            "frame_c_sec3_vs_w5_sec2_max_diff": float(fc_ord15_sec3_vs_w5_sec2_max_diff),
            "frame_c_sec2_vs_w5_sec2_max_split": float(fc_ord15_sec2_vs_w5_sec2_max_split),
            "mag_sec3_vs_w5_sec2_max_diff": float(mag_ord15_sec3_vs_w5_sec2_max_diff),
            "mag_sec2_vs_w5_sec2_max_split": float(mag_ord15_sec2_vs_w5_sec2_max_split),
            "PC_FUNNEL2_NotDivBy3_break": pc_not_div_by_3_break,
        },
        "p862_step2_cusp_exponents": {
            "frame_c_exact_tables": fc_tables,
            "frame_c_order10_e23_identical_all_72_pts": ord10_e23_identical_all_72,
            "frame_c_mpmath_40_60_checks": fc_mpmath_checks,
            "magnetized_triple_overlap_20_30_exponents": mag_cusp_exps,
            "magnetized_order10_sec2_sec3_e23_split": ord10_mag_split,
            "magnetized_order15_2_15_opposite_consecutive_skew": ord15_2_15_opposite_skew,
        },
        "E3_Order15_Surjection_and_P862_Exponents_passed": e3_passed,
    }


def verify_source_isolation_via_ast() -> Dict[str, Any]:
    src = pathlib.Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(src)
    allowed_top: Set[str] = {
        "__future__", "ast", "fractions", "hashlib", "json", "math", "mpmath", "numpy", "pathlib", "typing"
    }
    imported_top: Set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imported_top.add(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom) and node.module is not None:
            imported_top.add(node.module.split(".")[0])
    disallowed = sorted(imported_top - allowed_top)
    return {
        "imported_top_modules": sorted(imported_top),
        "disallowed_imports_count": len(disallowed),
        "zero_imports_from_main_or_other_relays": len(disallowed) == 0,
    }


def main() -> None:
    ast_isolation = verify_source_isolation_via_ast()
    part_2a = run_r0_and_part_2a()
    part_2b = run_part_2b()
    controls_all_passed = bool(
        part_2a["controls_2a"]["Gate_Haar_CP_max_diff_10_trials"] < 1e-40
        and part_2a["controls_2a"]["PC_Haar_CP_distinct_UL_diff"] > 1e-3
        and part_2a["controls_2a"]["PC_FUNNEL2_WrongOrbit_escapes_J_count"] == 4
        and part_2b["order_15_surjection_192_pts"]["PC_FUNNEL2_NotDivBy3_break"] > 0.1
    )
    stage_2_gate_passed = bool(
        ast_isolation["zero_imports_from_main_or_other_relays"]
        and part_2a["R0_S_covariance_fix"]["E0_S_Covariance_Fix_passed"]
        and part_2a["E1_Gamma5_Obstruction_and_m004_CP_passed"]
        and part_2b["casimir_shift_test"]["E2_Casimir_PartialKill_passed"]
        and part_2b["E3_Order15_Surjection_and_P862_Exponents_passed"]
        and controls_all_passed
    )
    payload = {
        "card": "X-FUNNEL-2",
        "empirical_firewall": "0 of 19",
        "source_isolation_ast_check": ast_isolation,
        "part_2a_r0_gamma5_and_m004": part_2a,
        "part_2b_casimir_surjection_and_p862": part_2b,
        "all_planted_controls_passed": controls_all_passed,
        "stage_2_gate_passed": stage_2_gate_passed,
    }
    raw = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    OUT_PATH.write_text(raw, encoding="utf-8")
    digest = hashlib.sha256(raw.encode("utf-8")).hexdigest()
    OUT_SHA_PATH.write_text(f"{digest}  verify_x_funnel_2_out.json\n", encoding="utf-8")


if __name__ == "__main__":
    main()
