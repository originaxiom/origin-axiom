#!/usr/bin/env python3
"""
Standalone zero-import verifier for Card X-FUNNEL-1 (0 of 19, data-free).

Part 1A:
  - Cross-family statement-only recomputation of B1947 (C0, C1, C2 on both D1 and D1'
    and across both characteristic representatives) without reading d1_coupling.py.
  - Verification of P-861's owed question on W-B2 Stage Three: whether shifting the
    kernel's Szego zero alone by h = c * q_H * w at c in {-2, +2} extends identity E
    (q' = q - c * q_H / 2) from the residues R_s to the full Theorem-90 channel-weighted
    matrices Y_f.

Part 1B:
  - First-principles construction and 3-route mpmath verification (2D spectral quadrature
    on E_tau, direct unfolded Gaussian lattice sum, and fast Poisson-erfc sum) of the
    punctured-torus magnetized (p, q)-bigraded triple overlap on (E_tau^x, spin (1/2, 1/2))
    with I_L = +3, I_R = -3, I_H = 0, and q_L + q_R + q_H = 0.
  - Verification of Haar gauge-basis scrambling invariance (Gate_Haar), planted controls
    (PC_FUNNEL1_Spin, PC_FUNNEL1_ChargeBreak, PC_Haar_DistinctUL), SL(2, Z) covariance
    (T and S), torsion-lattice gauge invariance (a -> a+1, b -> b+1), deep-cusp alignment
    across all 24 order-5 points at heights 6 and 30, bulk mixing hierarchy, and B1934's
    order-5 transposition identity between the second and third charged sectors.
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
OUT_PATH = HERE / "verify_x_funnel_1_out.json"
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
    (Fraction(3, 5), Fraction(1, 5)),
    (Fraction(4, 5), Fraction(3, 5)),
]

CHARGES_CHARGED: Dict[str, Tuple[int, int]] = {
    "sec_1": (1, -4),   # Q_6 = (+1, -4), q_H = +3
    "sec_2": (1, 2),    # Q_6 = (+1, +2), q_H = -3
    "sec_3": (-3, 6),   # Q_6 = (-3, +6), q_H = -3
}


# ============================================================================
# SECTION 1: ZERO-IMPORT QUATERNION CONTRACTION, SERRE Q-SERIES & FRAME C ENGINE
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


def f2m(q: Fraction) -> mp.mpf:
    return mp.mpf(q.numerator) / q.denominator


def th_char_val_and_dtau(al: mp.mpf, be: mp.mpf, tau: mp.mpc, k_span: int = 30) -> Tuple[mp.mpc, mp.mpc]:
    """Exact theta[al, be](0, tau) and d/dtau theta[al, be](0, tau) without integer-shift phase loss."""
    k0 = int(round(-float(al)))
    s = mp.mpc(0)
    ds = mp.mpc(0)
    for dk in range(-k_span, k_span + 1):
        m = mp.mpf(k0 + dk) + al
        t = mp.exp(mp.pi * 1j * tau * (m * m) + 2j * mp.pi * m * be)
        s += t
        ds += (mp.pi * 1j * (m * m)) * t
    return s, ds


def e2_mp(tau: mp.mpc) -> mp.mpc:
    q = mp.exp(2j * mp.pi * tau)
    s = mp.mpc(1)
    cutoff = mp.mpf(10) ** (-(mp.mp.dps + 6))
    for n in range(1, 200):
        qn = q ** n
        if abs(qn) < cutoff:
            break
        s -= 24 * n * qn / (1 - qn)
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
                c_mp = mp.mpc(f2m(fr), f2m(fi))
                c3[col_j] += pw * c_mp
    return c3


def eval_s_d1_vec(tau: mp.mpc, sa: mp.mpf, sb: mp.mpf, rep_sign: int = 1) -> List[mp.mpc]:
    """Twisted Higgs Serre derivative S_D1 from B1947 CARD.md statement alone."""
    half = mp.mpf(1) / 2
    y_f = max(float(mp.im(tau)), 0.4)
    k_span = max(24, int(math.ceil(math.sqrt((mp.mp.dps * math.log(10.0) + 20.0) / (math.pi * y_f)))) + 4)
    t2, dt2 = th_char_val_and_dtau(half + sa, sb, tau, k_span)
    t3, dt3 = th_char_val_and_dtau(sa, sb, tau, k_span)
    t4, dt4 = th_char_val_and_dtau(sa, rep_sign * half + sb, tau, k_span)
    e2_v = e2_mp(tau)
    r0 = -t2 / (t3 * t4)
    dr0 = r0 * (dt2 / t2 - dt3 / t3 - dt4 / t4) / (2j * mp.pi) + e2_v * r0 / 24
    r1 = -t4 / (t2 * t3)
    dr1 = r1 * (dt4 / t4 - dt2 / t2 - dt3 / t3) / (2j * mp.pi) + e2_v * r1 / 24
    r2 = 1j * t3 / (t2 * t4)
    dr2 = r2 * (dt3 / t3 - dt2 / t2 - dt4 / t4) / (2j * mp.pi) + e2_v * r2 / 24
    return [dr0, dr1, dr2]


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


def is_zero_char(c: Tuple[Fraction, Fraction]) -> bool:
    half = Fraction(1, 2)
    return ((c[0] - half) % 1 == 0) and ((c[1] - half) % 1 == 0)


def a0_from_char(al_fr: Fraction, be_fr: Fraction, tau: mp.mpc) -> mp.mpc:
    """Constant term a_0 = 2 pi i alpha + theta_1'(alpha tau + beta | tau) / theta_1(alpha tau + beta | tau)."""
    # Exact identity: for [al + 1/2, be + 1/2], d/dz ln theta[al+1/2, be+1/2](0, tau) = a_0!
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


def frame_c_matter_u(
    tau: mp.mpc,
    a: Fraction,
    b: Fraction,
    ql: Fraction,
    qr: Fraction,
    L2_val: mp.mpf,
) -> Tuple[List[mp.mpc], List[mp.mpc]]:
    """
    Computes Frame C's exact channel residues [R_1, R_i, R_j, R_k] and
    Theorem-90 weighted channel amplitudes [u_1, u_i, u_j, u_k] for rational charges (ql, qr).
    """
    yv = mp.im(tau)
    q_mp = mp.exp(2j * mp.pi * tau)
    eta = mp.exp(1j * mp.pi * tau / 12) * mp.qp(q_mp)
    t1p = 2 * mp.pi * (eta ** 3)
    half = Fraction(1, 2)
    x = (ql * a, 2 * ql * b)
    yy = (qr * a, 2 * qr * b)
    ap, am = x[0] + yy[0], x[0] - yy[0]
    bp, bm = (x[1] + yy[1]) / 2, (x[1] - yy[1]) / 2
    e_ph = mp.exp(-2j * mp.pi * f2m(x[0]))
    kap = [-1j * e_ph, mp.mpc(-1), -e_ph, mp.mpc(0, 1)]
    cs = [
        (ap + half, bp + half),
        (ap + half, bp),
        (ap, bp + half),
        (ap, bp),
    ]
    ds = [
        (am + half, bm + half),
        (am + half, bm),
        (am, bm + half),
        (am, bm),
    ]
    y_f = max(float(yv), 0.4)
    k_span = max(24, int(math.ceil(math.sqrt((mp.mp.dps * math.log(10.0) + 20.0) / (math.pi * y_f)))) + 4)
    r_list: List[mp.mpc] = []
    u_list: List[mp.mpc] = []
    for idx in range(4):
        if is_zero_char(cs[idx]) or is_zero_char(ds[idx]):
            r_list.append(mp.mpc(0))
            u_list.append(mp.mpc(0))
            continue
        tc, _ = th_char_val_and_dtau(f2m(cs[idx][0]), f2m(cs[idx][1]), tau, k_span)
        td, _ = th_char_val_and_dtau(f2m(ds[idx][0]), f2m(ds[idx][1]), tau, k_span)
        r_val = kap[idx] * tc * td / t1p
        al_fr = cs[idx][0] - half
        be_fr = cs[idx][1] - half
        a0_v = a0_from_char(al_fr, be_fr, tau)
        c_val = (
            F_kron_mp(al_fr, be_fr, tau)
            + mp.pi * mp.log(yv)
            - 2 * mp.pi * (mp.euler + mp.log(mp.pi))
            - mp.pi * (abs(a0_v) ** 2) * mp.exp(-2 * L2_val)
        )
        arg = 2 * mp.pi * L2_val + c_val
        u_val = mp.sqrt(arg) * r_val if arg > 0 else mp.mpc(0)
        r_list.append(r_val)
        u_list.append(u_val)
    return r_list, u_list


def contract_frame_c_Y(c_vec: List[mp.mpc], u_vec: List[mp.mpc]) -> mp.matrix:
    y_mat = mp.zeros(3, 3)
    half = mp.mpf(1) / 2
    for al_i, s_i, ra, cb, tr2, ti2 in T_COUP_NZ:
        y_mat[ra, cb] += c_vec[al_i] * u_vec[s_i] * mp.mpc(tr2, ti2) * half
    return y_mat


def svd_ascending(y_mat: mp.matrix) -> Tuple[mp.matrix, List[mp.mpf]]:
    u_desc, sv_desc, _ = mp.svd_c(y_mat)
    order = sorted(range(3), key=lambda idx: sv_desc[idx])
    u_asc = mp.matrix([[u_desc[r, order[c]] for c in range(3)] for r in range(3)])
    sv_asc = [sv_desc[order[c]] for c in range(3)]
    return u_asc, sv_asc


def overlap_moduli(u1: mp.matrix, u2: mp.matrix) -> List[List[mp.mpf]]:
    v = mp.matrix([[mp.conj(u1[k, r]) for k in range(3)] for r in range(3)]) * u2
    return [[abs(v[r, c]) for c in range(3)] for r in range(3)]


def run_part_1a() -> Dict[str, Any]:
    """
    Part 1A:
      - B1947 C0, C1, C2 from CARD.md statement alone.
      - P-861's owed question on W-B2 Stage 3: Szego-zero shift h = c * q_H * w at c = -2, +2
        and extension of identity E from residues R_s to Theorem-90 channel norms.
    """
    with mp.workdps(55):
        moduli = [
            mp.mpc("0.13", "1.7"),
            mp.mpc("-0.31", "2.4"),
            mp.mpc("0.27", "1.35"),
        ]
        # C0: q_H = 0 matches untwisted Serre q-series
        c0_max_diff = mp.mpf(0)
        for tau in moduli:
            s_ref = eval_serre_qseries_mp(tau)
            s_zero = eval_s_d1_vec(tau, mp.mpf(0), mp.mpf(0), rep_sign=1)
            for idx in range(3):
                c0_max_diff = max(c0_max_diff, abs(s_ref[idx] - s_zero[idx]))

        # C1: S_D1(-3) vs S_D1(+3) component-dependent phase phi = 2*pi*3*a
        c1_max_diff = mp.mpf(0)
        c1_non_scalar_spread = mp.mpf(0)
        for tau in moduli:
            for a_fr, b_fr in [(Fraction(1, 5), Fraction(2, 5)), (Fraction(2, 5), Fraction(1, 5))]:
                a_m, b_m = f2m(a_fr), f2m(b_fr)
                sp = eval_s_d1_vec(tau, 3 * a_m, 6 * b_m, rep_sign=1)
                sm = eval_s_d1_vec(tau, -3 * a_m, -6 * b_m, rep_sign=1)
                phi = 6 * mp.pi * a_m
                expected = [mp.exp(1j * phi), mp.exp(-1j * phi), mp.exp(1j * phi)]
                for idx in range(3):
                    c1_max_diff = max(c1_max_diff, abs(sm[idx] / sp[idx] - expected[idx]))
                c1_non_scalar_spread = max(c1_non_scalar_spread, abs(sm[1] / sp[1] - sm[0] / sp[0]))

        # C2: tau -> tau + 1 covariance test on ratios and |V| at (tau, w) vs (tau + 1, (a, b - a))
        # Test untwisted Frame C control, B1947 D1 (qH*a, 2*qH*b), and B1947 D1' (qH*a, qH*b), both reps (+1, -1).
        L2_test = f2m(Fraction(9, 10))
        ctrl_frame_c_max_diff = mp.mpf(0)
        c2_diffs: Dict[str, mp.mpf] = {
            "D1_rep_plus": mp.mpf(0),
            "D1_rep_minus": mp.mpf(0),
            "D1prime_rep_plus": mp.mpf(0),
            "D1prime_rep_minus": mp.mpf(0),
        }
        test_pts = [(Fraction(1, 5), Fraction(2, 5)), (Fraction(2, 5), Fraction(4, 5)), (Fraction(1, 5), Fraction(0, 5))]
        for tau in moduli:
            tau_T = tau + 1
            s_untw_0 = eval_serre_qseries_mp(tau)
            s_untw_T = eval_serre_qseries_mp(tau_T)
            st_untw_0 = [mp.conj(z) for z in s_untw_0]
            st_untw_T = [mp.conj(z) for z in s_untw_T]
            for a_fr, b_fr in test_pts:
                bT_fr = b_fr - a_fr
                _, uu0 = frame_c_matter_u(tau, a_fr, b_fr, Fraction(1), Fraction(-4), L2_test)
                _, ud0 = frame_c_matter_u(tau, a_fr, b_fr, Fraction(1), Fraction(2), L2_test)
                _, uuT = frame_c_matter_u(tau_T, a_fr, bT_fr, Fraction(1), Fraction(-4), L2_test)
                _, udT = frame_c_matter_u(tau_T, a_fr, bT_fr, Fraction(1), Fraction(2), L2_test)

                # Untwisted Frame C control (W_- = St in sec_1, S in sec_2)
                Uu0, su0 = svd_ascending(contract_frame_c_Y(st_untw_0, uu0))
                Ud0, sd0 = svd_ascending(contract_frame_c_Y(s_untw_0, ud0))
                UuT, suT = svd_ascending(contract_frame_c_Y(st_untw_T, uuT))
                UdT, sdT = svd_ascending(contract_frame_c_Y(s_untw_T, udT))
                V0 = overlap_moduli(Uu0, Ud0)
                VT = overlap_moduli(UuT, UdT)
                ctrl_frame_c_max_diff = max(
                    ctrl_frame_c_max_diff,
                    abs(su0[1] / su0[2] - suT[1] / suT[2]),
                    abs(su0[0] / su0[2] - suT[0] / suT[2]),
                    abs(sd0[1] / sd0[2] - sdT[1] / sdT[2]),
                    abs(sd0[0] / sd0[2] - sdT[0] / sdT[2]),
                    max(abs(V0[r][c] - VT[r][c]) for r in range(3) for c in range(3)),
                )

                # Twisted variants
                for mode_name, b_mult in (("D1", 2), ("D1prime", 1)):
                    for rep_label, rep_sgn in (("rep_plus", 1), ("rep_minus", -1)):
                        key = f"{mode_name}_{rep_label}"
                        a_m, b_m, bT_m = f2m(a_fr), f2m(b_fr), f2m(bT_fr)
                        su_h0 = eval_s_d1_vec(tau, 3 * a_m, b_mult * 3 * b_m, rep_sgn)
                        sd_h0 = eval_s_d1_vec(tau, -3 * a_m, b_mult * (-3) * b_m, rep_sgn)
                        su_hT = eval_s_d1_vec(tau_T, 3 * a_m, b_mult * 3 * bT_m, rep_sgn)
                        sd_hT = eval_s_d1_vec(tau_T, -3 * a_m, b_mult * (-3) * bT_m, rep_sgn)

                        U_u0, s_u0 = svd_ascending(contract_frame_c_Y(su_h0, uu0))
                        U_d0, s_d0 = svd_ascending(contract_frame_c_Y(sd_h0, ud0))
                        U_uT, s_uT = svd_ascending(contract_frame_c_Y(su_hT, uuT))
                        U_dT, s_dT = svd_ascending(contract_frame_c_Y(sd_hT, udT))
                        V_0 = overlap_moduli(U_u0, U_d0)
                        V_T = overlap_moduli(U_uT, U_dT)
                        # Compare relative log-ratios and |V| differences
                        d_val = max(
                            abs(mp.log((s_u0[1] / s_u0[2]) / (s_uT[1] / s_uT[2]))),
                            abs(mp.log((s_u0[0] / s_u0[2]) / (s_uT[0] / s_uT[2]))),
                            abs(mp.log((s_d0[1] / s_d0[2]) / (s_dT[1] / s_dT[2]))),
                            abs(mp.log((s_d0[0] / s_d0[2]) / (s_dT[0] / s_dT[2]))),
                            max(abs(V_0[r][c] - V_T[r][c]) for r in range(3) for c in range(3)),
                        )
                        c2_diffs[key] = max(c2_diffs[key], d_val)

        # P-861 owed check on W-B2 Stage 3: Szego-zero shift h = c * q_H * w at c in {-2, +2}
        # Evaluating Frame C's Szego pole at u = -h (h = c * q_H * w) shifts matter's level-2 theta
        # characteristics from (ql*a, 2*ql*b) and (qr*a, 2*qr*b) to q' = q - c * q_H / 2!
        # Specifically, for c = -2: q' = q + q_H = q - (ql + qr), so (ql', qr') = (-qr, -ql)!
        # Let's check BOTH directly:
        #   (i) At c = -2, compare Frame C at shifted charges (ql', qr') = (-qr, -ql) vs unshifted Frame C (ql, qr)
        #       on BOTH residues R_s and full Theorem-90 channel norms u_s and outputs (ratios, |V|)!
        #   (ii) Verify why: in cs[s], ap' = ql'*a + qr'*a = -(ql + qr)*a = -ap, bp' = -bp, am' = (ql' - qr')*a = (ql - qr)*a = +am!
        #        Wait: check F_kron(-al, -be) == F_kron(al, be) and |a0(-al, -be)|^2 == |a0(al, be)|^2!
        wb2_c_minus2_norm_ratio_diff = mp.mpf(0)
        wb2_c_minus2_a0_antisym_diff = mp.mpf(0)
        wb2_c_minus2_fkron_even_diff = mp.mpf(0)
        wb2_c_minus2_output_diff = mp.mpf(0)
        wb2_c_plus2_cov_T_diff = mp.mpf(0)
        wb2_c_plus2_lep_down_copy_diff = mp.mpf(0)

        tau_w = moduli[0]
        s_vec_w = eval_serre_qseries_mp(tau_w)
        s_vec_wT = eval_serre_qseries_mp(tau_w + 1)
        half_fr = Fraction(1, 2)
        hs_spins = [(Fraction(0), Fraction(0)), (Fraction(0), half_fr), (half_fr, Fraction(0)), (half_fr, half_fr)]
        for a_fr, b_fr in P5_ALL_24:
            for sec_name, (ql_i, qr_i) in CHARGES_CHARGED.items():
                ql, qr = Fraction(ql_i), Fraction(qr_i)
                qH = -(ql + qr)
                for A_sp, B_sp in hs_spins:
                    al_s = ((ql + qr) * a_fr - A_sp) % 1
                    be_s = ((ql + qr) * b_fr - B_sp) % 1
                    if al_s == 0 and be_s == 0:
                        continue
                    al_neg = (-al_s) % 1
                    be_neg = (-be_s) % 1
                    wb2_c_minus2_fkron_even_diff = max(
                        wb2_c_minus2_fkron_even_diff,
                        abs(F_kron_mp(al_s, be_s, tau_w) - F_kron_mp(al_neg, be_neg, tau_w)),
                    )
                    wb2_c_minus2_a0_antisym_diff = max(
                        wb2_c_minus2_a0_antisym_diff,
                        abs(abs(a0_from_char(al_s, be_s, tau_w)) - abs(a0_from_char(al_neg, be_neg, tau_w))),
                    )
                # c = -2 -> q' = q + qH = (-qr, -ql)
                ql_m2, qr_m2 = ql + qH, qr + qH
                r_orig, u_orig = frame_c_matter_u(tau_w, a_fr, b_fr, ql, qr, L2_test)
                r_m2, u_m2 = frame_c_matter_u(tau_w, a_fr, b_fr, ql_m2, qr_m2, L2_test)
                for idx in range(4):
                    if abs(r_orig[idx]) > mp.mpf("1e-35"):
                        n_orig = u_orig[idx] / r_orig[idx]
                        n_m2 = u_m2[idx] / r_m2[idx]
                        wb2_c_minus2_norm_ratio_diff = max(wb2_c_minus2_norm_ratio_diff, abs(n_orig - n_m2))
                _, sv_o = svd_ascending(contract_frame_c_Y(s_vec_w, u_orig))
                _, sv_m = svd_ascending(contract_frame_c_Y(s_vec_w, u_m2))
                wb2_c_minus2_output_diff = max(
                    wb2_c_minus2_output_diff,
                    abs(sv_o[1] / sv_o[2] - sv_m[1] / sv_m[2]),
                    abs(sv_o[0] / sv_o[2] - sv_m[0] / sv_m[2]),
                )

            # c = +2 -> q' = q - qH: sec_1 (-2, -7), sec_2 (4, 5), sec_3 (0, 9)
            _, u_d_p2 = frame_c_matter_u(tau_w, a_fr, b_fr, Fraction(4), Fraction(5), L2_test)
            _, u_e_p2 = frame_c_matter_u(tau_w, a_fr, b_fr, Fraction(0), Fraction(9), L2_test)
            _, sv_d_p2 = svd_ascending(contract_frame_c_Y(s_vec_w, u_d_p2))
            _, sv_e_p2 = svd_ascending(contract_frame_c_Y(s_vec_w, u_e_p2))
            wb2_c_plus2_lep_down_copy_diff = max(
                wb2_c_plus2_lep_down_copy_diff,
                abs(sv_d_p2[1] / sv_d_p2[2] - sv_e_p2[1] / sv_e_p2[2]),
                abs(sv_d_p2[0] / sv_d_p2[2] - sv_e_p2[0] / sv_e_p2[2]),
            )
            # Also check T-covariance of c = +2 with Theorem-90 norms:
            _, u_u_p2 = frame_c_matter_u(tau_w, a_fr, b_fr, Fraction(-2), Fraction(-7), L2_test)
            _, u_u_p2_T = frame_c_matter_u(tau_w + 1, a_fr, b_fr - a_fr, Fraction(-2), Fraction(-7), L2_test)
            _, sv_u_p2 = svd_ascending(contract_frame_c_Y(s_vec_w, u_u_p2))
            _, sv_u_p2_T = svd_ascending(contract_frame_c_Y(s_vec_wT, u_u_p2_T))
            wb2_c_plus2_cov_T_diff = max(
                wb2_c_plus2_cov_T_diff,
                abs(sv_u_p2[1] / sv_u_p2[2] - sv_u_p2_T[1] / sv_u_p2_T[2]),
                abs(sv_u_p2[0] / sv_u_p2[2] - sv_u_p2_T[0] / sv_u_p2_T[2]),
            )

        tol_strict = mp.mpf("1e-35")
        e1_passed = bool(
            c0_max_diff < tol_strict
            and c1_max_diff < tol_strict
            and c1_non_scalar_spread > mp.mpf("0.5")
            and ctrl_frame_c_max_diff < tol_strict
            and min(c2_diffs.values()) > mp.mpf("0.1")
            and wb2_c_minus2_fkron_even_diff < tol_strict
            and wb2_c_minus2_a0_antisym_diff < tol_strict
            and wb2_c_minus2_norm_ratio_diff < tol_strict
            and wb2_c_minus2_output_diff < tol_strict
            and wb2_c_plus2_cov_T_diff < tol_strict
            and wb2_c_plus2_lep_down_copy_diff < tol_strict
        )

        return {
            "c0_max_diff": float(c0_max_diff),
            "c1_max_diff": float(c1_max_diff),
            "c1_non_scalar_spread": float(c1_non_scalar_spread),
            "ctrl_frame_c_T_max_diff": float(ctrl_frame_c_max_diff),
            "c2_T_max_diffs": {k: float(v) for k, v in c2_diffs.items()},
            "p861_wb2_c_minus2_fkron_even_diff": float(wb2_c_minus2_fkron_even_diff),
            "p861_wb2_c_minus2_a0_mod_diff": float(wb2_c_minus2_a0_antisym_diff),
            "p861_wb2_c_minus2_channel_norm_diff": float(wb2_c_minus2_norm_ratio_diff),
            "p861_wb2_c_minus2_output_diff": float(wb2_c_minus2_output_diff),
            "p861_wb2_c_plus2_T_cov_diff": float(wb2_c_plus2_cov_T_diff),
            "p861_wb2_c_plus2_sec2_sec3_copy_diff": float(wb2_c_plus2_lep_down_copy_diff),
            "E1_B1947_and_P861_passed": e1_passed,
        }


# ============================================================================
# SECTION 2: PUNCTURED-TORUS MAGNETIZED (p, q)-BIGRADED TRIPLE OVERLAP (3 ROUTES)
# ============================================================================

def cim_landau_mode(
    x: mp.mpf,
    y: mp.mpf,
    tau: mp.mpc,
    gen_idx: int,
    i_flux: int,
    alpha: mp.mpf,
    beta: mp.mpf,
    spin_half: bool = True,
) -> mp.mpc:
    """
    Orthonormal zero mode on E_tau for flux i_flux > 0, flat U(1) holonomy (alpha, beta),
    and spin structure (1/2, 1/2) (spin_half=True) or (0, 0) (spin_half=False, planted control).
    """
    tau2 = mp.im(tau)
    norm = (2 * tau2 * i_flux) ** mp.mpf("0.25")
    sp_a = mp.mpf(1) / 2 if spin_half else mp.mpf(0)
    sp_b = mp.mpf(i_flux) / 2 if spin_half else mp.mpf(0)
    c_a = (mp.mpf(gen_idx) + sp_a + alpha) / i_flux
    b_tot = sp_b + beta
    m0 = int(round(-float(x + c_a)))
    s = mp.mpc(0)
    for dm in range(-22, 23):
        u = mp.mpf(m0 + dm) + c_a
        s += mp.exp(mp.pi * 1j * i_flux * tau * ((x + u) ** 2) + 2j * mp.pi * (i_flux * y + b_tot) * u)
    return norm * s


def y_mag_direct_gaussian(
    tau: mp.mpc,
    a: mp.mpf,
    b: mp.mpf,
    ql: int,
    qr: int,
    spin_half: bool = True,
    qh_override: int | None = None,
) -> mp.matrix:
    """Route 2: Exact unfolded Gaussian lattice sum on E_tau^x."""
    qh = -(ql + qr) if qh_override is None else qh_override
    tau1, tau2 = mp.re(tau), mp.im(tau)
    thresh = (mp.mp.dps + 6) * mp.log(10)
    r_sq = thresh * 6 * tau2 / mp.pi
    k_max = max(int(mp.ceil(mp.sqrt(r_sq) / tau2 / 3)) + 3, 6)
    m_span = int(mp.ceil(mp.sqrt(r_sq))) + 4
    sp = mp.mpf(1) / 2 if spin_half else mp.mpf(0)
    sp_phase = mp.mpf(3) if spin_half else mp.mpf(0)
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
                    if om_sq == 0:
                        continue
                    gauss = mp.exp(-mp.pi * om_sq / (6 * tau2))
                    phase = mp.exp(mp.pi * 1j * (mp.mpf(m) * (c_l + c_r - k) + delta_k * ((qr - ql) * b - sp_phase)))
                    prop = tau2 / (mp.pi * om_sq)
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


def y_mag_poisson_fast(tau: mp.mpc, a: mp.mpf, b: mp.mpf, ql: int, qr: int) -> mp.matrix:
    """Route 3: Fast Poisson-resummed erfc + Riemann-split formula valid to arbitrary height Im(tau)."""
    qh = -(ql + qr)
    tau1, tau2 = mp.re(tau), mp.im(tau)
    u0 = mp.mpf(1) / mp.sqrt(6)
    u_split = mp.sqrt(tau2)
    thresh = (mp.mp.dps + 8) * mp.log(10)
    half = mp.mpf(1) / 2
    k_max = int(mp.ceil(mp.sqrt(thresh * 6 / (mp.pi * tau2)) / 3)) + 4
    l_max = int(mp.ceil(mp.sqrt(thresh * 6 / (mp.pi * tau2)))) + 6
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
                    sub = mp.mpc(0)
                    l_center = int(round(float(xi0)))
                    for dl in range(-l_max, l_max + 1):
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
    ph = d_np / np.abs(d_np)
    q_np = q_np * ph[np.newaxis, :]
    # Polish to 50-digit exact unitarity in mpmath via Gram-Schmidt!
    cols: List[List[mp.mpc]] = [
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


def conj_transpose(m: mp.matrix) -> mp.matrix:
    return mp.matrix([[mp.conj(m[c, r]) for c in range(m.cols)] for r in range(m.rows)])


def run_part_1b_and_controls() -> Dict[str, Any]:
    with mp.workdps(48):
        tau_bulk = mp.mpc("0.13", "1.7")
        a0, b0 = f2m(Fraction(1, 5)), f2m(Fraction(2, 5))

        # 1. Three-route cross-check:
        #    (a) Route 1 (2D spectral trapezoidal quadrature on [0,1]^2 for mode window |m|, |n| <= 6)
        #        vs Route 2 (direct unfolded Gaussian lattice sum restricted to |m|, |n| <= 6) across all 9 entries!
        n_grid = 26
        tau2 = mp.im(tau_bulk)
        ql, qr, qh = 1, -4, 3
        y_quad_win = mp.zeros(3, 3)
        # Precompute Landau zero modes and truncated Higgs Green's function on 26 x 26 grid
        psi_l_grid = [[[cim_landau_mode(mp.mpf(ix) / n_grid, mp.mpf(iy) / n_grid, tau_bulk, i, 3, ql * a0, ql * b0, True)
                        for iy in range(n_grid)] for ix in range(n_grid)] for i in range(3)]
        psi_r_grid = [[[mp.conj(cim_landau_mode(mp.mpf(ix) / n_grid, mp.mpf(iy) / n_grid, tau_bulk, j, 3, -qr * a0, -qr * b0, True))
                        for iy in range(n_grid)] for ix in range(n_grid)] for j in range(3)]
        h_grid = [[mp.mpc(0) for _ in range(n_grid)] for _ in range(n_grid)]
        for ix in range(n_grid):
            x = mp.mpf(ix) / n_grid
            for iy in range(n_grid):
                y = mp.mpf(iy) / n_grid
                hv = mp.mpc(0)
                for n in range(-6, 7):
                    na = mp.mpf(n) + qh * a0
                    for m in range(-6, 7):
                        omega = na * tau_bulk + (mp.mpf(m) + qh * b0)
                        hv += (tau2 / (mp.pi * (abs(omega) ** 2))) * mp.exp(2j * mp.pi * (na * y - (mp.mpf(m) + qh * b0) * x))
                h_grid[ix][iy] = hv

        for i in range(3):
            for j in range(3):
                acc_q = mp.mpc(0)
                for ix in range(n_grid):
                    for iy in range(n_grid):
                        acc_q += psi_l_grid[i][ix][iy] * psi_r_grid[j][ix][iy] * h_grid[ix][iy]
                y_quad_win[i, j] = acc_q / (n_grid * n_grid)

        # Analytical formula restricted to |m| <= 6, |n| <= 6
        half = mp.mpf(1) / 2
        y_cf_win = mp.zeros(3, 3)
        for i in range(3):
            c_l = (mp.mpf(i) + half + ql * a0) / 3
            for j in range(3):
                c_r = (mp.mpf(j) + half - qr * a0) / 3
                acc_c = mp.mpc(0)
                for k in range(-5, 6):
                    n = (j - i) - 3 * k
                    if abs(n) > 6:
                        continue
                    na = mp.mpf(n) + qh * a0
                    delta_k = na / 3
                    for m in range(-6, 7):
                        omega = na * tau_bulk + (mp.mpf(m) + qh * b0)
                        acc_c += (
                            (tau2 / (mp.pi * (abs(omega) ** 2)))
                            * mp.exp(-mp.pi * (abs(omega) ** 2) / (6 * tau2))
                            * mp.exp(mp.pi * 1j * (mp.mpf(m) * (c_l + c_r - k) + delta_k * ((qr - ql) * b0 - 3)))
                        )
                y_cf_win[i, j] = acc_c

        quad_vs_gaussian_max_diff = max(abs(y_quad_win[r, c] - y_cf_win[r, c]) for r in range(3) for c in range(3))

        #    (b) Route 2 (full direct Gaussian sum) vs Route 3 (fast Poisson-erfc sum) at both a != 0 and a == 0!
        gaussian_vs_poisson_max_diff = mp.mpf(0)
        for a_fr, b_fr in [(Fraction(1, 5), Fraction(2, 5)), (Fraction(0, 5), Fraction(2, 5))]:
            am, bm = f2m(a_fr), f2m(b_fr)
            for ql_t, qr_t in CHARGES_CHARGED.values():
                yd = y_mag_direct_gaussian(tau_bulk, am, bm, ql_t, qr_t)
                yp = y_mag_poisson_fast(tau_bulk, am, bm, ql_t, qr_t)
                for r in range(3):
                    for c in range(3):
                        gaussian_vs_poisson_max_diff = max(gaussian_vs_poisson_max_diff, abs(yd[r, c] - yp[r, c]))

        # 2. Full SL(2, Z) modular covariance (T and S) and torsion-lattice gauge invariance (a -> a+1, b -> b+1)
        def eval_all_obs(t_v: mp.mpc, a_v: mp.mpf, b_v: mp.mpf):
            y1 = y_mag_poisson_fast(t_v, a_v, b_v, 1, -4)
            y2 = y_mag_poisson_fast(t_v, a_v, b_v, 1, 2)
            y3 = y_mag_poisson_fast(t_v, a_v, b_v, -3, 6)
            u1, s1 = svd_ascending(y1)
            u2, s2 = svd_ascending(y2)
            _, s3 = svd_ascending(y3)
            v_mod = overlap_moduli(u1, u2)
            return y1, y2, y3, [s1[1] / s1[2], s1[0] / s1[2]], [s2[1] / s2[2], s2[0] / s2[2]], [s3[1] / s3[2], s3[0] / s3[2]], v_mod

        y1_0, y2_0, _, r1_0, r2_0, r3_0, v_0 = eval_all_obs(tau_bulk, a0, b0)
        cov_diffs: Dict[str, float] = {}
        for name, (tv, av, bv) in [
            ("T_cov", (tau_bulk + 1, a0, b0 - a0)),
            ("S_cov", (-1 / tau_bulk, -b0, a0)),
            ("shift_a_plus_1", (tau_bulk, a0 + 1, b0)),
            ("shift_b_plus_1", (tau_bulk, a0, b0 + 1)),
        ]:
            _, _, _, r1_t, r2_t, r3_t, v_t = eval_all_obs(tv, av, bv)
            d = max(
                max(abs(r1_0[k] - r1_t[k]) for k in range(2)),
                max(abs(r2_0[k] - r2_t[k]) for k in range(2)),
                max(abs(r3_0[k] - r3_t[k]) for k in range(2)),
                max(abs(v_0[r][c] - v_t[r][c]) for r in range(3) for c in range(3)),
            )
            cov_diffs[name] = float(d)

        # Bulk hierarchy check at tau_bulk, w = (1/5, 2/5): 1 > |V_12| > |V_23| > |V_13| > 0
        v12_b, v23_b, v13_b = float(v_0[0][1]), float(v_0[1][2]), float(v_0[0][2])
        bulk_hierarchy_holds = bool(1.0 > v12_b > v23_b > v13_b > 0.0)

        # 3. Gate_Haar (Guardrail 3): 10 random gauge-allowed Haar unitary basis transformations
        #    Y_1 -> U_L Y_1 U_{R,1}^dagger, Y_2 -> U_L Y_2 U_{R,2}^dagger
        haar_max_diff = mp.mpf(0)
        for trial in range(10):
            u_l = random_haar_u3_mp(1000 + 3 * trial)
            u_r1 = random_haar_u3_mp(1001 + 3 * trial)
            u_r2 = random_haar_u3_mp(1002 + 3 * trial)
            # Verify unitarity of u_l explicitly (Guardrail 2: no literal flag!)
            unit_check = u_l * conj_transpose(u_l) - mp.eye(3)
            for r in range(3):
                for c in range(3):
                    haar_max_diff = max(haar_max_diff, abs(unit_check[r, c]))
            y1_scr = u_l * y1_0 * conj_transpose(u_r1)
            y2_scr = u_l * y2_0 * conj_transpose(u_r2)
            u1_s, s1_s = svd_ascending(y1_scr)
            u2_s, s2_s = svd_ascending(y2_scr)
            v_scr = overlap_moduli(u1_s, u2_s)
            haar_max_diff = max(
                haar_max_diff,
                abs(s1_s[1] / s1_s[2] - r1_0[0]),
                abs(s1_s[0] / s1_s[2] - r1_0[1]),
                abs(s2_s[1] / s2_s[2] - r2_0[0]),
                abs(s2_s[0] / s2_s[2] - r2_0[1]),
                max(abs(v_scr[r][c] - v_0[r][c]) for r in range(3) for c in range(3)),
            )

        # Planted gauge-breaking Haar control: distinct U_{L,1} != U_{L,2} MUST scramble |V|!
        u_l1_bad = random_haar_u3_mp(9001)
        u_l2_bad = random_haar_u3_mp(9002)
        u1_bad, _ = svd_ascending(u_l1_bad * y1_0)
        u2_bad, _ = svd_ascending(u_l2_bad * y2_0)
        v_bad = overlap_moduli(u1_bad, u2_bad)
        pc_haar_distinct_ul_scramble = float(max(abs(v_bad[r][c] - v_0[r][c]) for r in range(3) for c in range(3)))

        # 4. Planted Control PC_FUNNEL1_Spin: wrong spin structure (0, 0) breaks T covariance!
        y_sp0_0 = y_mag_direct_gaussian(tau_bulk, a0, b0, 1, -4, spin_half=False)
        y_sp0_T = y_mag_direct_gaussian(tau_bulk + 1, a0, b0 - a0, 1, -4, spin_half=False)
        _, sv_sp0_0 = svd_ascending(y_sp0_0)
        _, sv_sp0_T = svd_ascending(y_sp0_T)
        pc_spin_00_T_break = float(max(
            abs(sv_sp0_0[1] / sv_sp0_0[2] - sv_sp0_T[1] / sv_sp0_T[2]),
            abs(sv_sp0_0[0] / sv_sp0_0[2] - sv_sp0_T[0] / sv_sp0_T[2]),
        ))

        # 5. Planted Control PC_FUNNEL1_ChargeBreak: q_H = -(q_L + q_R) + 1 breaks double periodicity on E_tau!
        x_pt, y_pt = mp.mpf("0.37"), mp.mpf("0.29")
        qh_good = -(ql + qr)
        qh_bad = qh_good + 1
        f_matter_0 = cim_landau_mode(x_pt, y_pt, tau_bulk, 1, 3, ql * a0, ql * b0, True) * mp.conj(
            cim_landau_mode(x_pt, y_pt, tau_bulk, 2, 3, -qr * a0, -qr * b0, True)
        )
        f_matter_y1 = cim_landau_mode(x_pt, y_pt + 1, tau_bulk, 1, 3, ql * a0, ql * b0, True) * mp.conj(
            cim_landau_mode(x_pt, y_pt + 1, tau_bulk, 2, 3, -qr * a0, -qr * b0, True)
        )
        p_good_diff = float(abs(
            f_matter_y1 * mp.exp(2j * mp.pi * (qh_good * a0 * (y_pt + 1) - qh_good * b0 * x_pt))
            - f_matter_0 * mp.exp(2j * mp.pi * (qh_good * a0 * y_pt - qh_good * b0 * x_pt))
        ))
        p_bad_diff = float(abs(
            f_matter_y1 * mp.exp(2j * mp.pi * (qh_bad * a0 * (y_pt + 1) - qh_bad * b0 * x_pt))
            - f_matter_0 * mp.exp(2j * mp.pi * (qh_bad * a0 * y_pt - qh_bad * b0 * x_pt))
        ))
        y_cb_0 = y_mag_direct_gaussian(tau_bulk, a0, b0, 1, -4, spin_half=True, qh_override=qh_bad)
        y_cb_a1 = y_mag_direct_gaussian(tau_bulk, a0 + 1, b0, 1, -4, spin_half=True, qh_override=qh_bad)
        _, sv_cb_0 = svd_ascending(y_cb_0)
        _, sv_cb_a1 = svd_ascending(y_cb_a1)
        pc_chargebreak_shift_a1_diff = float(max(
            abs(sv_cb_0[1] / sv_cb_0[2] - sv_cb_a1[1] / sv_cb_a1[2]),
            abs(sv_cb_0[0] / sv_cb_0[2] - sv_cb_a1[0] / sv_cb_a1[2]),
        ))

        # 6. Order-5 transposition identity check across all 24 points (sec_2 vs sec_3) at tau_bulk:
        order5_sec2_sec3_max_diff = mp.mpf(0)
        for a_fr, b_fr in P5_ALL_24:
            am, bm = f2m(a_fr), f2m(b_fr)
            _, s_d = svd_ascending(y_mag_poisson_fast(tau_bulk, am, bm, 1, 2))
            _, s_e = svd_ascending(y_mag_poisson_fast(tau_bulk, am, bm, -3, 6))
            order5_sec2_sec3_max_diff = max(
                order5_sec2_sec3_max_diff,
                abs(s_d[1] / s_d[2] - s_e[1] / s_e[2]),
                abs(s_d[0] / s_d[2] - s_e[0] / s_e[2]),
            )

    # 7. Deep-cusp alignment scan across ALL 24 points of P_5 at heights y = 6 and y = 30!
    cusp_summary: Dict[str, Any] = {}
    for y_int in (6, 30):
        with mp.workdps(48 + 2 * y_int):
            tau_c = mp.mpc(f2m(Fraction(13, 100)), mp.mpf(y_int))
            min_v33_all24 = mp.mpf(1)
            min_v33_anz20 = mp.mpf(1)
            min_v33_o4 = mp.mpf(1)
            min_diag_a15 = mp.mpf(1)
            per_a_min_v33: Dict[str, float] = {}
            for a_fr, b_fr in P5_ALL_24:
                am, bm = f2m(a_fr), f2m(b_fr)
                u1_c, _ = svd_ascending(y_mag_poisson_fast(tau_c, am, bm, 1, -4))
                u2_c, _ = svd_ascending(y_mag_poisson_fast(tau_c, am, bm, 1, 2))
                vm = overlap_moduli(u1_c, u2_c)
                v33 = vm[2][2]
                min_v33_all24 = min(min_v33_all24, v33)
                if a_fr != 0:
                    min_v33_anz20 = min(min_v33_anz20, v33)
                if (a_fr, b_fr) in O4_M004:
                    min_v33_o4 = min(min_v33_o4, v33)
                if a_fr in (Fraction(1, 5), Fraction(4, 5)):
                    min_diag_a15 = min(min_diag_a15, vm[0][0], vm[1][1], vm[2][2])
                ak = str(a_fr)
                per_a_min_v33[ak] = min(per_a_min_v33.get(ak, 1.0), float(v33))
            cusp_summary[f"height_{y_int}"] = {
                "min_V33_all_24": float(min_v33_all24),
                "min_V33_a_nonzero_20": float(min_v33_anz20),
                "min_V33_m004_orbit_4": float(min_v33_o4),
                "min_all3_diags_a_1_5_and_4_5": float(min_diag_a15),
                "per_a_min_V33": per_a_min_v33,
            }

    tol_12 = 1e-12
    tol_30 = 1e-30
    e2_passed = bool(
        float(quad_vs_gaussian_max_diff) < tol_30
        and float(gaussian_vs_poisson_max_diff) < tol_30
        and max(cov_diffs.values()) < tol_30
    )
    e3_passed = bool(
        cusp_summary["height_30"]["min_V33_all_24"] > 0.98
        and cusp_summary["height_30"]["min_V33_a_nonzero_20"] > 0.9999
        and cusp_summary["height_30"]["min_V33_m004_orbit_4"] > 0.9999
        and cusp_summary["height_30"]["min_all3_diags_a_1_5_and_4_5"] > 0.9999
        and bulk_hierarchy_holds
        and float(order5_sec2_sec3_max_diff) < tol_30
    )
    controls_passed = bool(
        float(haar_max_diff) < tol_12
        and pc_haar_distinct_ul_scramble > 0.05
        and pc_spin_00_T_break > 0.01
        and p_good_diff < tol_30
        and p_bad_diff > 0.1
        and pc_chargebreak_shift_a1_diff > 0.01
    )

    return {
        "three_route_agreement": {
            "quadrature_vs_gaussian_window_max_diff": float(quad_vs_gaussian_max_diff),
            "gaussian_vs_poisson_full_max_diff": float(gaussian_vs_poisson_max_diff),
        },
        "modular_and_lattice_covariance": cov_diffs,
        "bulk_sample_tau_0p13_1p7i_w_1_5_2_5": {
            "sec1_ratios": [float(x) for x in r1_0],
            "sec2_ratios": [float(x) for x in r2_0],
            "sec3_ratios": [float(x) for x in r3_0],
            "overlap_moduli": [[float(v_0[r][c]) for c in range(3)] for r in range(3)],
            "off_diag_strict_hierarchy_1_gt_V12_gt_V23_gt_V13_gt_0": bulk_hierarchy_holds,
        },
        "order5_sec2_sec3_copy_max_diff_24pts": float(order5_sec2_sec3_max_diff),
        "cusp_alignment_scan": cusp_summary,
        "controls": {
            "Gate_Haar_max_diff_10_trials": float(haar_max_diff),
            "PC_Haar_distinct_UL_scramble": pc_haar_distinct_ul_scramble,
            "PC_FUNNEL1_Spin_00_T_break": pc_spin_00_T_break,
            "double_periodicity_conserved_qH_diff": p_good_diff,
            "PC_FUNNEL1_ChargeBreak_periodicity_diff": p_bad_diff,
            "PC_FUNNEL1_ChargeBreak_shift_a_plus_1_diff": pc_chargebreak_shift_a1_diff,
            "all_controls_passed": controls_passed,
        },
        "E2_Covariance_and_Quadrature_passed": e2_passed,
        "E3_Cusp_Alignment_and_Order5_Law_passed": e3_passed,
    }


def verify_source_isolation_via_ast() -> Dict[str, Any]:
    src = pathlib.Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(src)
    allowed_top_modules: Set[str] = {
        "__future__", "ast", "fractions", "hashlib", "json", "math", "mpmath", "numpy", "pathlib", "typing"
    }
    imported_top: Set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imported_top.add(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom) and node.module is not None:
            imported_top.add(node.module.split(".")[0])
    disallowed = sorted(imported_top - allowed_top_modules)
    return {
        "imported_top_modules": sorted(imported_top),
        "disallowed_imports_count": len(disallowed),
        "zero_imports_from_main_or_other_relays": len(disallowed) == 0,
    }


def main() -> None:
    ast_isolation = verify_source_isolation_via_ast()
    part_1a = run_part_1a()
    part_1b = run_part_1b_and_controls()
    stage_1_gate_passed = bool(
        ast_isolation["zero_imports_from_main_or_other_relays"]
        and part_1a["E1_B1947_and_P861_passed"]
        and part_1b["E2_Covariance_and_Quadrature_passed"]
        and part_1b["E3_Cusp_Alignment_and_Order5_Law_passed"]
        and part_1b["controls"]["all_controls_passed"]
    )
    payload = {
        "card": "X-FUNNEL-1",
        "empirical_firewall": "0 of 19",
        "source_isolation_ast_check": ast_isolation,
        "part_1a_b1947_and_p861": part_1a,
        "part_1b_magnetized_triple_overlap": part_1b,
        "stage_1_gate_passed": stage_1_gate_passed,
    }
    raw = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    OUT_PATH.write_text(raw, encoding="utf-8")
    digest = hashlib.sha256(raw.encode("utf-8")).hexdigest()
    OUT_SHA_PATH.write_text(f"{digest}  verify_x_funnel_1_out.json\n", encoding="utf-8")


if __name__ == "__main__":
    main()
