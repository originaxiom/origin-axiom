#!/usr/bin/env python3
"""
Standalone blind-sealed verifier for Card X-L5 (0 of 19, data-free).

Tests main's level-5 point-phase law (P-871 / B1945 Section 6, asked in M37 & M38)
from its prose statement alone, with zero reading of main's check script, zero
imports from main or peer branches, and zero float literals anywhere in this module.
"""

from __future__ import annotations

import ast
import hashlib
import json
import pathlib
from fractions import Fraction
from typing import Any, Dict, List, Tuple

import mpmath as mp

HERE = pathlib.Path(__file__).resolve().parent
OUT_PATH = HERE / "verify_x_l5_out.json"
OUT_SHA_PATH = HERE / "OUTPUT_SHA256.txt"

SECTORS: Dict[str, Tuple[int, int]] = {
    "sec_1": (1, -4),   # q_H = +3
    "sec_2": (1, 2),    # q_H = -3
    "sec_3": (-3, 6),   # q_H = -3
}

C_PLACEMENTS: List[int] = [0, 1, -1, 2, -2, 5, 7]

PTS_CANON_24: List[Tuple[Fraction, Fraction]] = [
    (Fraction(ia, 5), Fraction(ib, 5))
    for ia in range(5)
    for ib in range(5)
    if (ia, ib) != (0, 0)
]

PTS_CENTERED_24: List[Tuple[Fraction, Fraction]] = [
    (Fraction(ia, 5), Fraction(ib, 5))
    for ia in (-2, -1, 0, 1, 2)
    for ib in (-2, -1, 0, 1, 2)
    if (ia, ib) != (0, 0)
]


def f2m(fr: Fraction) -> mp.mpf:
    return mp.mpf(fr.numerator) / mp.mpf(fr.denominator)


def m2dec(val: mp.mpf) -> str:
    return mp.nstr(val, 18)


def eta_cubed_2pi(tau: mp.mpc) -> mp.mpc:
    """2 * pi * eta(tau)^3 = theta_1'(0 | tau)."""
    yv = mp.im(tau)
    q = mp.exp(2 * mp.mpc(0, 1) * mp.pi * tau)
    m_cap = int(mp.ceil(mp.mpf(175) / (2 * mp.pi * yv))) + 14
    prod = mp.mpc(1)
    qk = mp.mpc(1)
    for _ in range(1, m_cap + 1):
        qk *= q
        prod *= (mp.mpc(1) - qk)
    eta = mp.exp(mp.mpc(0, 1) * mp.pi * tau / mp.mpf(12)) * prod
    return 2 * mp.pi * (eta ** 3)


def theta_char_z(alpha: mp.mpf, beta: mp.mpf, z: mp.mpc, tau_arg: mp.mpc) -> mp.mpc:
    """
    Jacobi theta[alpha, beta](z | tau_arg) centered at the Gaussian saddle
    n_0 = -round(Re(alpha) + Im(z) / Im(tau_arg)) for uniform 55-digit accuracy
    even at large shifts |c| = 7.
    """
    im_tau = mp.im(tau_arg)
    center = -(mp.re(alpha) + mp.im(z) / im_tau)
    n0 = int(mp.nint(center))
    span = int(mp.ceil(mp.sqrt(mp.mpf(185) / (mp.pi * im_tau)))) + 10
    acc = mp.mpc(0)
    iu = mp.mpc(0, 1)
    for dn in range(-span, span + 1):
        na = mp.mpf(n0 + dn) + alpha
        acc += mp.exp(mp.pi * iu * (na * na) * tau_arg + 2 * mp.pi * iu * na * (z + beta))
    return acc


def theta_char_0_and_dtau(alpha: mp.mpf, beta: mp.mpf, tau: mp.mpc) -> Tuple[mp.mpc, mp.mpc]:
    """theta[alpha, beta](0 | tau) and d/d(tau) theta[alpha, beta](0 | tau) / (2*pi*i) * (2*pi*i)."""
    im_tau = mp.im(tau)
    n0 = int(mp.nint(-mp.re(alpha)))
    span = int(mp.ceil(mp.sqrt(mp.mpf(185) / (mp.pi * im_tau)))) + 10
    s0 = mp.mpc(0)
    s_dt = mp.mpc(0)
    iu = mp.mpc(0, 1)
    for dn in range(-span, span + 1):
        na = mp.mpf(n0 + dn) + alpha
        term = mp.exp(mp.pi * iu * (na * na) * tau + 2 * mp.pi * iu * na * beta)
        s0 += term
        s_dt += (mp.pi * iu * (na * na)) * term
    return s0, s_dt


def eval_serre_triplet(tau: mp.mpc, tilde_reading: bool = False) -> List[mp.mpc]:
    """Untwisted weight-3/2 Serre derivative Higgs triplet S(tau) (or conjugate tilde_S(tau))."""
    yv = mp.im(tau)
    q = mp.exp(2 * mp.mpc(0, 1) * mp.pi * tau)
    m_cap = int(mp.ceil(mp.mpf(175) / (2 * mp.pi * yv))) + 14
    eta_prod = mp.mpc(1)
    e2 = mp.mpc(1)
    qk = mp.mpc(1)
    for m_i in range(1, m_cap + 1):
        qk *= q
        eta_prod *= (mp.mpc(1) - qk)
        e2 -= mp.mpf(24 * m_i) * qk / (mp.mpc(1) - qk)
    iu = mp.mpc(0, 1)
    den = 2 * mp.pi * ((mp.exp(iu * mp.pi * tau / mp.mpf(12)) * eta_prod) ** 3)
    half = mp.mpf(1) / mp.mpf(2)
    zero = mp.mpf(0)

    t2, dt2 = theta_char_0_and_dtau(half, zero, tau)
    t4, dt4 = theta_char_0_and_dtau(zero, half, tau)
    t3, dt3 = theta_char_0_and_dtau(zero, zero, tau)

    # Note dt_k is d/d(tau) theta_k; normalized q*d/dq = (1/(2*pi*i)) d/d(tau):
    inv_2pi_i = mp.mpc(1) / (2 * mp.pi * iu)
    r_vec = [-(t2 * t2) / den, -(t4 * t4) / den, iu * (t3 * t3) / den]
    dn_vec = [
        -2 * t2 * (dt2 * inv_2pi_i) / den,
        -2 * t4 * (dt4 * inv_2pi_i) / den,
        2 * iu * t3 * (dt3 * inv_2pi_i) / den,
    ]
    # Serre derivative of weight-1/2 triplet R: q dR/dq - (1/24) E_2 * R_hat (with x-dependent vs holomorphic hat cancels in ratio;
    # use holistic holomorphic den = 2*pi*eta(tau)^3 so R has modular weight +1/2: D_{1/2} R = q dR/dq - (1/24) E_2 R!
    # Wait: check d/dtau(eta^3) = (2*pi*i)*(3/24)*E_2*eta^3 = (2*pi*i)*(1/8)*E_2*eta^3, while dn_vec differentiated numerator only!
    # Differentiating R = num / eta^3 gives q dR/dq = dn_vec - (1/8)*E_2*R, so D_{1/2} R = q dR/dq - (1/24)*E_2*R = dn_vec - (1/6)*E_2*R?
    # Wait: R = -theta_2^2 / (2*pi*eta^3) has weight 2*(1/2) - 3*(1/2) = -1/2!!
    # Weight k = -1/2 has Serre derivative D_{-1/2} R = q dR/dq - (-1/2)/12 * E_2 R = (dn_vec - (3/24) E_2 R) + (1/24) E_2 R = dn_vec - (1/12) E_2 R!
    s_vec = [dn_vec[idx] - (e2 / mp.mpf(12)) * r_vec[idx] for idx in range(3)]
    if tilde_reading:
        return [mp.conj(z) for z in s_vec]
    return s_vec


def build_quaternion_contraction() -> Tuple[List[mp.matrix], List[mp.matrix], Dict[str, List[Tuple[int, int, int, int, mp.mpc]]]]:
    """Standalone quaternion algebra and Frame C / D1 contraction tensor."""
    one = mp.mpc(1)
    zero = mp.mpc(0)
    iu = mp.mpc(0, 1)
    i2 = mp.matrix([[one, zero], [zero, one]])
    qi = mp.matrix([[iu, zero], [zero, -iu]])
    qj = mp.matrix([[zero, one], [-one, zero]])
    qk = mp.matrix([[zero, iu], [iu, zero]])
    eps = qj
    units = [i2, qi, qj, qk]
    ec = [eps * u for u in units]

    def hsum(m1: mp.matrix, m2: mp.matrix) -> mp.mpc:
        return m1[0, 0] * m2[0, 0] + m1[0, 1] * m2[0, 1] + m1[1, 0] * m2[1, 0] + m1[1, 1] * m2[1, 1]

    g_mat = mp.matrix(4, 4)
    for r_i in range(4):
        for c_i in range(4):
            g_mat[r_i, c_i] = hsum(ec[r_i], units[c_i])
    g_inv = g_mat ** (-1)
    edual: List[mp.matrix] = []
    for a_i in range(4):
        acc_m = mp.zeros(2, 2)
        for b_i in range(4):
            acc_m += g_inv[b_i, a_i] * units[b_i]
        edual.append(acc_m)

    blocks = [qj, qi, qk]
    q_s = [qi, qj, qk]
    q_st = [eps * mp.matrix([[mp.conj(q[0, 0]), mp.conj(q[0, 1])], [mp.conj(q[1, 0]), mp.conj(q[1, 1])]]) * eps.T for q in q_s]

    tensors: Dict[str, List[Tuple[int, int, int, int, mp.mpc]]] = {"S": [], "tilde_S": []}
    for rname, qlist in (("S", q_s), ("tilde_S", q_st)):
        for qi_idx in range(3):
            for si_idx in range(4):
                for ra in range(3):
                    for cb in range(3):
                        prod = blocks[ra].T * eps * qlist[qi_idx] * blocks[cb]
                        val = hsum(prod, edual[si_idx])
                        if abs(val) > mp.mpf(10) ** (-40):
                            tensors[rname].append((qi_idx, si_idx, ra, cb, val))
    return ec, edual, tensors


def frame_d1_residue_2x2(tau: mp.mpc, a: Fraction, b: Fraction, ql: int, qr: int, c_place: int) -> mp.matrix:
    """
    Frame D1 2x2 residue at the Higgs zero h = c_place * q_H * w (pole u_0 = -h):
      B_D1(tau, w; c) = v_{q_L w}(-h | 2*tau) * v_{q_R w}(-h | 2*tau)^T / theta_1'(0 | tau),
    with v_{q w}(u | 2*tau) = (theta[q*a, 2*q*b](u | 2*tau), -i * theta[q*a + 1/2, 2*q*b](u | 2*tau)).
    """
    qh = -(ql + qr)
    w = f2m(a) * tau + f2m(b)
    u0 = -mp.mpf(c_place * qh) * w
    two_tau = 2 * tau
    half = Fraction(1, 2)
    iu = mp.mpc(0, 1)

    vl0 = theta_char_z(f2m(ql * a), f2m(2 * ql * b), u0, two_tau)
    vl1 = -iu * theta_char_z(f2m(ql * a + half), f2m(2 * ql * b), u0, two_tau)
    vr0 = theta_char_z(f2m(qr * a), f2m(2 * qr * b), u0, two_tau)
    vr1 = -iu * theta_char_z(f2m(qr * a + half), f2m(2 * qr * b), u0, two_tau)

    t1p = eta_cubed_2pi(tau)
    b_mat = mp.zeros(2, 2)
    b_mat[0, 0] = (vl0 * vr0) / t1p
    b_mat[0, 1] = (vl0 * vr1) / t1p
    b_mat[1, 0] = (vl1 * vr0) / t1p
    b_mat[1, 1] = (vl1 * vr1) / t1p
    return b_mat


def b2x2_to_channel_residues(b_mat: mp.matrix, edual: List[mp.matrix]) -> List[mp.mpc]:
    """Maps B_D1 to Frame C's 4 channel residues R_s via M_ec = 2 * eps * B_D1^T * eps^T."""
    m_ec = mp.matrix([
        [2 * b_mat[1, 1], -2 * b_mat[0, 1]],
        [-2 * b_mat[1, 0], 2 * b_mat[0, 0]],
    ])
    out: List[mp.mpc] = []
    for s_i in range(4):
        ed = edual[s_i]
        out.append(m_ec[0, 0] * ed[0, 0] + m_ec[0, 1] * ed[0, 1] + m_ec[1, 0] * ed[1, 0] + m_ec[1, 1] * ed[1, 1])
    return out


def frame_c_direct_channel_residues(tau: mp.mpc, a: Fraction, b: Fraction, ql: int, qr: int) -> List[mp.mpc]:
    """Standalone level-1 Riemann-product Frame C channel residues [R_0, R_1, R_2, R_3] (for Gate_U0)."""
    t1p = eta_cubed_2pi(tau)
    half = Fraction(1, 2)
    iu = mp.mpc(0, 1)
    ap = (ql + qr) * a
    am = (ql - qr) * a
    bp = (ql + qr) * b
    bm = (ql - qr) * b
    e_ph = mp.exp(-2 * mp.pi * iu * f2m(ql * a))
    kap = [-iu * e_ph, mp.mpc(-1), -e_ph, iu]
    cs = [(ap + half, bp + half), (ap + half, bp), (ap, bp + half), (ap, bp)]
    ds = [(am + half, bm + half), (am + half, bm), (am, bm + half), (am, bm)]

    res: List[mp.mpc] = []
    for idx in range(4):
        c_a, c_b = cs[idx]
        d_a, d_b = ds[idx]
        if ((c_a - half) % 1 == 0 and (c_b - half) % 1 == 0) or ((d_a - half) % 1 == 0 and (d_b - half) % 1 == 0):
            res.append(mp.mpc(0))
            continue
        tc, _ = theta_char_0_and_dtau(f2m(c_a), f2m(c_b), tau)
        td, _ = theta_char_0_and_dtau(f2m(d_a), f2m(d_b), tau)
        res.append(kap[idx] * tc * td / t1p)
    return res


def contract_yukawa_3x3(s_vec: List[mp.mpc], r_vec: List[mp.mpc], tensor_entries: List[Tuple[int, int, int, int, mp.mpc]]) -> mp.matrix:
    y_mat = mp.zeros(3, 3)
    for qi_i, si_i, ra, cb, coeff in tensor_entries:
        y_mat[ra, cb] += s_vec[qi_i] * r_vec[si_i] * coeff
    return y_mat


def frob_norm_sq(m: mp.matrix) -> mp.mpf:
    acc = mp.mpf(0)
    for r_i in range(m.rows):
        for c_i in range(m.cols):
            acc += abs(m[r_i, c_i]) ** 2
    return acc


def frob_inner(m1: mp.matrix, m2: mp.matrix) -> mp.mpc:
    """Tr(m1^dagger * m2)."""
    acc = mp.mpc(0)
    for r_i in range(m1.rows):
        for c_i in range(m1.cols):
            acc += mp.conj(m1[r_i, c_i]) * m2[r_i, c_i]
    return acc


def fit_global_signed_perm_unitaries(y0: mp.matrix, y_sh: mp.matrix) -> Tuple[mp.matrix, mp.matrix, mp.mpf]:
    """
    Finds the w-independent 3x3 unitaries (U_L, U_R) from the 4 exact signed permutations
    generated by R_+ = [[0,0,1],[0,1,0],[-1,0,0]] and R_- = R_+^T at the reference point w_0 = (0, 1/5).
    """
    one = mp.mpc(1)
    zero = mp.mpc(0)
    i3 = mp.matrix([[one, zero, zero], [zero, one, zero], [zero, zero, one]])
    r_plus = mp.matrix([[zero, zero, one], [zero, one, zero], [-one, zero, zero]])
    r_minus = r_plus.T
    cands = [i3, r_plus, r_minus, r_plus * r_plus]

    best_err = mp.mpf(10) ** 10
    best_ul = i3
    best_ur = i3
    n_sq = frob_norm_sq(y0)
    for ol in cands:
        for or_m in cands:
            base = ol * y0 * or_m.T
            eta = frob_inner(base, y_sh) / n_sq
            if abs(eta) > mp.mpf(1) / mp.mpf(10):
                eta_unit = eta / abs(eta)
                diff = y_sh - eta_unit * base
                rel = mp.sqrt(frob_norm_sq(diff) / n_sq)
                if rel < best_err:
                    best_err = rel
                    best_ul = eta_unit * ol
                    best_ur = or_m
    return best_ul, best_ur, best_err


def y_mag_unfolded_mp(tau: mp.mpc, a: Fraction, b: Fraction, ql: int, qr: int) -> mp.matrix:
    """
    Exact unfolded 2D Gaussian lattice sum for X-FOUNDATION-4's magnetized (3, 3, -6)
    triple overlap with q_H = -(q_L + q_R) on spin structure (1/2, 1/2).
    """
    qh = -(ql + qr)
    tau1, tau2 = mp.re(tau), mp.im(tau)
    a_m, b_m = f2m(a), f2m(b)
    thresh = mp.mpf(mp.mp.dps + 8) * mp.log(mp.mpf(10))
    r_sq = thresh * mp.mpf(6) * tau2 / mp.pi
    k_max = max(int(mp.ceil(mp.sqrt(r_sq) / tau2 / mp.mpf(3))) + 3, 6)
    m_span = int(mp.ceil(mp.sqrt(r_sq))) + 5
    half = mp.mpf(1) / mp.mpf(2)
    iu = mp.mpc(0, 1)

    y_mat = mp.zeros(3, 3)
    for i_idx in range(3):
        cl = (mp.mpf(i_idx) + half + mp.mpf(ql) * a_m) / mp.mpf(3)
        zak_ph = mp.exp(-2 * mp.pi * iu * (mp.mpf(ql) * b_m / mp.mpf(3)) * (mp.mpf(i_idx) + half))
        for j_idx in range(3):
            cr = (mp.mpf(j_idx) + half - mp.mpf(qr) * a_m) / mp.mpf(3)
            acc = mp.mpc(0)
            for k_i in range(-k_max, k_max + 1):
                n_int = (j_idx - i_idx) - 3 * k_i
                na = mp.mpf(n_int) + mp.mpf(qh) * a_m
                dk = na / mp.mpf(3)
                m_center = int(mp.nint(-(na * tau1 + mp.mpf(qh) * b_m)))
                for dm in range(-m_span, m_span + 1):
                    m_i = m_center + dm
                    omega = na * tau + (mp.mpf(m_i) + mp.mpf(qh) * b_m)
                    om_sq = abs(omega) ** 2
                    if om_sq == 0:
                        continue
                    gauss = mp.exp(-mp.pi * om_sq / (mp.mpf(6) * tau2))
                    ph = mp.exp(mp.pi * iu * (mp.mpf(m_i) * (cl + cr - mp.mpf(k_i)) + dk * (mp.mpf(qr - ql) * b_m - mp.mpf(3))))
                    prop = tau2 / (mp.pi * om_sq)
                    acc += prop * gauss * ph
            y_mat[i_idx, j_idx] = zak_ph * acc
    return y_mat


def det_3x3(m: mp.matrix) -> mp.mpc:
    return (
        m[0, 0] * (m[1, 1] * m[2, 2] - m[1, 2] * m[2, 1])
        - m[0, 1] * (m[1, 0] * m[2, 2] - m[1, 2] * m[2, 0])
        + m[0, 2] * (m[1, 0] * m[2, 1] - m[1, 1] * m[2, 0])
    )


def run_ast_self_audit() -> Dict[str, Any]:
    src = pathlib.Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(src)
    float_literals = 0
    complex_literals = 0
    forbidden_imports: List[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant):
            if isinstance(node.value, float):
                float_literals += 1
            elif isinstance(node.value, complex):
                complex_literals += 1
        elif isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.startswith("frontier") or alias.name.startswith("verification"):
                    forbidden_imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            mod = node.module or ""
            if mod.startswith("frontier") or mod.startswith("verification"):
                forbidden_imports.append(mod)
    passed = (float_literals == 0) and (complex_literals == 0) and (len(forbidden_imports) == 0)
    return {
        "float_literal_count": float_literals,
        "complex_literal_count": complex_literals,
        "forbidden_imports": forbidden_imports,
        "Gate_AST_ZeroFloatLiterals_Passed": passed,
    }


def main() -> None:
    ast_res = run_ast_self_audit()

    with mp.workdps(55):
        iu = mp.mpc(0, 1)
        zeta5 = mp.exp(2 * mp.pi * iu / mp.mpf(5))
        moduli = [
            f2m(Fraction(13, 100)) + iu * f2m(Fraction(17, 10)),
            f2m(Fraction(-31, 100)) + iu * f2m(Fraction(12, 5)),
            f2m(Fraction(27, 100)) + iu * f2m(Fraction(27, 20)),
        ]
        _, edual, tensors = build_quaternion_contraction()

        # =====================================================================
        # PART A: Gate_U0 — c = 0 match between B_D1 2x2 residue and Frame C
        # =====================================================================
        u0_max_rel_err = mp.mpf(0)
        for tau in moduli:
            for sec_name, (ql, qr) in SECTORS.items():
                for a_fr, b_fr in PTS_CANON_24:
                    b_d1 = frame_d1_residue_2x2(tau, a_fr, b_fr, ql, qr, 0)
                    r_from_b = b2x2_to_channel_residues(b_d1, edual)
                    r_direct = frame_c_direct_channel_residues(tau, a_fr, b_fr, ql, qr)
                    norm_r = mp.sqrt(sum(abs(x) ** 2 for x in r_direct))
                    diff_r = mp.sqrt(sum(abs(r_from_b[k] - r_direct[k]) ** 2 for k in range(4)))
                    u0_max_rel_err = max(u0_max_rel_err, diff_r / norm_r)

        gate_u0_passed = bool(u0_max_rel_err < mp.mpf(10) ** (-42))

        # =====================================================================
        # PART B: Main's Level-5 Law (P-871) Across c in {0, 1, -1, 2, -2, 5, 7}
        # =====================================================================
        c1_diag_t5_max_err = mp.mpf(0)
        c1_diag_t25_max_err = mp.mpf(0)
        c1_even_offdiag_t5_max_err = mp.mpf(0)
        c1_even_3x3_S_t5_max_err = mp.mpf(0)
        c1_even_3x3_tildeS_t5_max_err = mp.mpf(0)
        c1_even_3x3_t25_max_err = mp.mpf(0)
        c2_odd_offdiag_t5_max_err = mp.mpf(0)
        c2_odd_offdiag_t25_max_err = mp.mpf(0)
        c2_odd_3x3_nonscalar_min_defect = mp.mpf(10) ** 10

        # Planted control accumulators
        pc1_wrong_quad_c_min_err = mp.mpf(10) ** 10
        pc2_omitted_odd_sign_min_err = mp.mpf(10) ** 10
        pc4_plain_sum_obstructed_min_drift = mp.mpf(10) ** 10

        per_c_sector_table: Dict[str, Dict[str, Any]] = {}
        ref_pt = (Fraction(0, 5), Fraction(1, 5))

        for c_val in C_PLACEMENTS:
            c_key = f"c_{c_val:+d}"
            per_c_sector_table[c_key] = {}
            is_odd_c = (c_val % 2 != 0)

            for sec_name, (ql, qr) in SECTORS.items():
                qh = -(ql + qr)
                e_mod5 = (ql * ql + qr * qr + c_val * qh * qh) % 5
                sec_diag_t5_err = mp.mpf(0)
                sec_off_t5_err = mp.mpf(0)
                sec_off_t25_err = mp.mpf(0)
                sec_3x3_t5_err = mp.mpf(0)

                for rep_name, pt_list in (("canon_0_to_4", PTS_CANON_24), ("centered_m2_to_p2", PTS_CENTERED_24)):
                    for tau in moduli:
                        tau5 = tau + mp.mpf(5)
                        tau25 = tau + mp.mpf(25)

                        # Reference w-independent global T^5 and T^25 entrywise factors at ref_pt = (0, 1/5)
                        b_ref0 = frame_d1_residue_2x2(tau, ref_pt[0], ref_pt[1], ql, qr, c_val)
                        b_ref5 = frame_d1_residue_2x2(tau5, ref_pt[0], ref_pt[1], ql, qr, c_val)
                        b_ref25 = frame_d1_residue_2x2(tau25, ref_pt[0], ref_pt[1], ql, qr, c_val)

                        g5 = mp.zeros(2, 2)
                        g25 = mp.zeros(2, 2)
                        for ri in range(2):
                            for ci in range(2):
                                g5[ri, ci] = b_ref5[ri, ci] / b_ref0[ri, ci]
                                g25[ri, ci] = b_ref25[ri, ci] / b_ref0[ri, ci]

                        # Precompute Serre vectors & global 3x3 unitaries from ref_pt for S and tilde_S
                        s0_S = eval_serre_triplet(tau, False)
                        s5_S = eval_serre_triplet(tau5, False)
                        s25_S = eval_serre_triplet(tau25, False)
                        s0_St = eval_serre_triplet(tau, True)
                        s5_St = eval_serre_triplet(tau5, True)

                        y_ref0_S = contract_yukawa_3x3(s0_S, b2x2_to_channel_residues(b_ref0, edual), tensors["S"])
                        y_ref5_S = contract_yukawa_3x3(s5_S, b2x2_to_channel_residues(b_ref5, edual), tensors["S"])
                        y_ref25_S = contract_yukawa_3x3(s25_S, b2x2_to_channel_residues(b_ref25, edual), tensors["S"])
                        ul5_S, ur5_S, fit_err5_S = fit_global_signed_perm_unitaries(y_ref0_S, y_ref5_S)
                        ul25_S, ur25_S, fit_err25_S = fit_global_signed_perm_unitaries(y_ref0_S, y_ref25_S)

                        y_ref0_St = contract_yukawa_3x3(s0_St, b2x2_to_channel_residues(b_ref0, edual), tensors["tilde_S"])
                        y_ref5_St = contract_yukawa_3x3(s5_St, b2x2_to_channel_residues(b_ref5, edual), tensors["tilde_S"])
                        ul5_St, ur5_St, fit_err5_St = fit_global_signed_perm_unitaries(y_ref0_St, y_ref5_St)

                        if not is_odd_c:
                            c1_even_3x3_S_t5_max_err = max(c1_even_3x3_S_t5_max_err, fit_err5_S)
                            c1_even_3x3_tildeS_t5_max_err = max(c1_even_3x3_tildeS_t5_max_err, fit_err5_St)
                            c1_even_3x3_t25_max_err = max(c1_even_3x3_t25_max_err, fit_err25_S)

                        sum_y0 = mp.zeros(3, 3)
                        sum_y5 = mp.zeros(3, 3)

                        for a_fr, b_fr in pt_list:
                            five_a = int(a_fr * 5)
                            ph_law = zeta5 ** ((e_mod5 * five_a * five_a) % 5)
                            odd_sgn = mp.mpf(-1) if (is_odd_c and (five_a % 2 != 0)) else mp.mpf(1)

                            b0 = frame_d1_residue_2x2(tau, a_fr, b_fr, ql, qr, c_val)
                            b5 = frame_d1_residue_2x2(tau5, a_fr, b_fr, ql, qr, c_val)
                            b25 = frame_d1_residue_2x2(tau25, a_fr, b_fr, ql, qr, c_val)

                            # Diagonal entries (0,0) and (1,1)
                            for di in (0, 1):
                                rat5 = b5[di, di] / (g5[di, di] * b0[di, di])
                                rat25 = b25[di, di] / (g25[di, di] * b0[di, di])
                                err5 = abs(rat5 - ph_law)
                                err25 = abs(rat25 - mp.mpc(1))
                                c1_diag_t5_max_err = max(c1_diag_t5_max_err, err5)
                                c1_diag_t25_max_err = max(c1_diag_t25_max_err, err25)
                                sec_diag_t5_err = max(sec_diag_t5_err, err5)

                                # Planted control 1: wrong quadratic c law E_wrong = q_L^2 + q_R^2 + (c + 4*c^2) q_H^2 mod 5 at c = +2 (5a = 1)
                                if c_val == 2 and abs(five_a) == 1:
                                    # 1/4 mod 5 == 4, so c + c^2/4 mod 5 at c=2 is 2 + 4*4 = 18 == 3 != 2 mod 5
                                    e_wrong = (ql * ql + qr * qr + 3 * qh * qh) % 5
                                    ph_wrong = zeta5 ** ((e_wrong * five_a * five_a) % 5)
                                    pc1_wrong_quad_c_min_err = min(pc1_wrong_quad_c_min_err, abs(rat5 - ph_wrong))

                            # Off-diagonal entries (0,1) and (1,0)
                            for ri, ci in ((0, 1), (1, 0)):
                                rat5_off = b5[ri, ci] / (g5[ri, ci] * b0[ri, ci])
                                rat25_off = b25[ri, ci] / (g25[ri, ci] * b0[ri, ci])
                                err5_off = abs(rat5_off - ph_law * odd_sgn)
                                err25_off = abs(rat25_off - odd_sgn)
                                sec_off_t5_err = max(sec_off_t5_err, err5_off)
                                sec_off_t25_err = max(sec_off_t25_err, err25_off)
                                if is_odd_c:
                                    c2_odd_offdiag_t5_max_err = max(c2_odd_offdiag_t5_max_err, err5_off)
                                    c2_odd_offdiag_t25_max_err = max(c2_odd_offdiag_t25_max_err, err25_off)
                                    if five_a % 2 != 0:
                                        pc2_omitted_odd_sign_min_err = min(
                                            pc2_omitted_odd_sign_min_err,
                                            abs(rat5_off - ph_law),
                                            abs(rat25_off - mp.mpc(1)),
                                        )
                                else:
                                    c1_even_offdiag_t5_max_err = max(c1_even_offdiag_t5_max_err, err5_off)

                            # Contracted 3x3 Yukawa coupling check
                            r0_ch = b2x2_to_channel_residues(b0, edual)
                            r5_ch = b2x2_to_channel_residues(b5, edual)
                            r25_ch = b2x2_to_channel_residues(b25, edual)

                            y0_S = contract_yukawa_3x3(s0_S, r0_ch, tensors["S"])
                            y5_S = contract_yukawa_3x3(s5_S, r5_ch, tensors["S"])
                            y25_S = contract_yukawa_3x3(s25_S, r25_ch, tensors["S"])
                            sum_y0 += y0_S
                            sum_y5 += y5_S

                            y0_St = contract_yukawa_3x3(s0_St, r0_ch, tensors["tilde_S"])
                            y5_St = contract_yukawa_3x3(s5_St, r5_ch, tensors["tilde_S"])

                            n_y0_S = mp.sqrt(frob_norm_sq(y0_S))
                            n_y0_St = mp.sqrt(frob_norm_sq(y0_St))
                            if not is_odd_c:
                                err_y5_S = mp.sqrt(frob_norm_sq(y5_S - ph_law * (ul5_S * y0_S * ur5_S.T))) / n_y0_S
                                err_y5_St = mp.sqrt(frob_norm_sq(y5_St - ph_law * (ul5_St * y0_St * ur5_St.T))) / n_y0_St
                                err_y25_S = mp.sqrt(frob_norm_sq(y25_S - (ul25_S * y0_S * ur25_S.T))) / n_y0_S
                                c1_even_3x3_S_t5_max_err = max(c1_even_3x3_S_t5_max_err, err_y5_S)
                                c1_even_3x3_tildeS_t5_max_err = max(c1_even_3x3_tildeS_t5_max_err, err_y5_St)
                                c1_even_3x3_t25_max_err = max(c1_even_3x3_t25_max_err, err_y25_S)
                                sec_3x3_t5_err = max(sec_3x3_t5_err, err_y5_S, err_y5_St)
                            else:
                                if five_a % 2 != 0:
                                    # Odd c + odd 5a breaks scalar proportionality to U_L Y0 U_R^dagger!
                                    proj_target = ul5_S * y0_S * ur5_S.T
                                    best_sc = frob_inner(proj_target, y5_S) / frob_norm_sq(proj_target)
                                    def_val = mp.sqrt(frob_norm_sq(y5_S - best_sc * proj_target)) / n_y0_S
                                    c2_odd_3x3_nonscalar_min_defect = min(c2_odd_3x3_nonscalar_min_defect, def_val)

                        # Plain sum singular-value ratio check when E != 0 mod 5 at even c (PC_XL5_4)
                        if (not is_odd_c) and (e_mod5 != 0) and rep_name == "canon_0_to_4":
                            _, sv0, _ = mp.svd_c(sum_y0)
                            _, sv5, _ = mp.svd_c(sum_y5)
                            drift = abs((sv5[1] / sv5[0]) - (sv0[1] / sv0[0]))
                            pc4_plain_sum_obstructed_min_drift = min(pc4_plain_sum_obstructed_min_drift, drift)

                per_c_sector_table[c_key][sec_name] = {
                    "E_mod_5": e_mod5,
                    "closes_at_level_5": bool((not is_odd_c) and (e_mod5 == 0)),
                    "diag_t5_max_err": m2dec(sec_diag_t5_err),
                    "offdiag_t5_max_err": m2dec(sec_off_t5_err),
                    "offdiag_t25_max_err": m2dec(sec_off_t25_err),
                    "even_c_3x3_t5_max_err": m2dec(sec_3x3_t5_err) if not is_odd_c else "N/A_odd_c_sign",
                }

        # C3: Exhaustive check over Z / 5Z (and all integers mod 10 considering odd-c sign) that no c closes both sec_1 and sec_2
        simultaneous_closure_c_values: List[int] = []
        mod5_closure_map: Dict[str, List[int]] = {"sec_1": [], "sec_2": [], "sec_3": []}
        for c_mod5 in range(5):
            e1 = (1 + 16 + c_mod5 * 9) % 5
            e2 = (1 + 4 + c_mod5 * 9) % 5
            e3 = (9 + 36 + c_mod5 * 9) % 5
            if e1 == 0:
                mod5_closure_map["sec_1"].append(c_mod5)
            if e2 == 0:
                mod5_closure_map["sec_2"].append(c_mod5)
            if e3 == 0:
                mod5_closure_map["sec_3"].append(c_mod5)
            if e1 == 0 and e2 == 0:
                simultaneous_closure_c_values.append(c_mod5)

        gate_c1_c2_c3_passed = bool(
            c1_diag_t5_max_err < mp.mpf(10) ** (-42)
            and c1_diag_t25_max_err < mp.mpf(10) ** (-42)
            and c1_even_offdiag_t5_max_err < mp.mpf(10) ** (-42)
            and c1_even_3x3_S_t5_max_err < mp.mpf(10) ** (-40)
            and c1_even_3x3_tildeS_t5_max_err < mp.mpf(10) ** (-40)
            and c1_even_3x3_t25_max_err < mp.mpf(10) ** (-40)
            and c2_odd_offdiag_t5_max_err < mp.mpf(10) ** (-42)
            and c2_odd_offdiag_t25_max_err < mp.mpf(10) ** (-42)
            and c2_odd_3x3_nonscalar_min_defect > mp.mpf(1) / mp.mpf(20)
            and mod5_closure_map["sec_1"] == [2]
            and mod5_closure_map["sec_2"] == [0]
            and mod5_closure_map["sec_3"] == [0]
            and len(simultaneous_closure_c_values) == 0
        )

        # =====================================================================
        # PART C: Audit of X-FOUNDATION-4's "Shifted" Convention vs c = 2
        # =====================================================================
        with mp.workdps(35):
            iu35 = mp.mpc(0, 1)
            zeta5_35 = mp.exp(2 * mp.pi * iu35 / mp.mpf(5))
            tau_mag = f2m(Fraction(13, 100)) + iu35 * f2m(Fraction(17, 10))
            tau_mag5 = tau_mag + mp.mpf(5)
            tau_mag25 = tau_mag + mp.mpf(25)

            mag_audit: Dict[str, Any] = {}
            c4_all_det_errs = mp.mpf(0)
            two_sin_pi_over_5 = 2 * mp.sin(mp.pi / mp.mpf(5))
            two_sin_2pi_over_5 = 2 * mp.sin(2 * mp.pi / mp.mpf(5))

            for sec_name, (ql, qr) in SECTORS.items():
                # Expected E_mag = (q_L^2 - q_R^2) mod 5; 3x3 determinant multiplies exponent by 3 mod 5
                e_mag_mod5 = (ql * ql - qr * qr) % 5
                det_exp_mod5 = (3 * e_mag_mod5) % 5
                e_d1_c2_mod5 = (ql * ql + qr * qr + 2 * (ql + qr) * (ql + qr)) % 5
                det_d1_c2_mod5 = (3 * e_d1_c2_mod5) % 5

                # Reference a = 0 point (0, 1/5)
                y_m_ref0 = y_mag_unfolded_mp(tau_mag, ref_pt[0], ref_pt[1], ql, qr)
                y_m_ref5 = y_mag_unfolded_mp(tau_mag5, ref_pt[0], ref_pt[1], ql, qr)
                y_m_ref25 = y_mag_unfolded_mp(tau_mag25, ref_pt[0], ref_pt[1], ql, qr)
                det_ref_rat5 = det_3x3(y_m_ref5) / det_3x3(y_m_ref0)
                det_ref_rat5 /= abs(det_ref_rat5)
                det_ref_rat25 = det_3x3(y_m_ref25) / det_3x3(y_m_ref0)
                det_ref_rat25 /= abs(det_ref_rat25)

                det_phases_t5: List[mp.mpc] = []
                det_phases_t25: List[mp.mpc] = []
                sec_det_law_err = mp.mpf(0)
                sec_t25_det_err = mp.mpf(0)
                # Also test whether U_L, U_R in magnetized 3-bundle depend on 5a mod 3
                max_const_unitary_defect = mp.mpf(0)
                max_mod3_twisted_unitary_err = mp.mpf(0)

                for a_fr, b_fr in PTS_CANON_24:
                    five_a = int(a_fr * 5)
                    ym0 = y_mag_unfolded_mp(tau_mag, a_fr, b_fr, ql, qr)
                    ym5 = y_mag_unfolded_mp(tau_mag5, a_fr, b_fr, ql, qr)
                    ym25 = y_mag_unfolded_mp(tau_mag25, a_fr, b_fr, ql, qr)

                    dr5 = (det_3x3(ym5) / det_3x3(ym0)) / det_ref_rat5
                    dr5 /= abs(dr5)
                    dr25 = (det_3x3(ym25) / det_3x3(ym0)) / det_ref_rat25
                    dr25 /= abs(dr25)
                    det_phases_t5.append(dr5)
                    det_phases_t25.append(dr25)

                    pred_det_ph = zeta5_35 ** ((det_exp_mod5 * five_a * five_a) % 5)
                    sec_det_law_err = max(sec_det_law_err, abs(dr5 - pred_det_ph))
                    sec_t25_det_err = max(sec_t25_det_err, abs(dr25 - mp.mpc(1)))

                    # Matrix-level exact law for y_mag_unfolded_mp:
                    # Y_mag(tau+5, w) = zeta5^(E_mag*(5a)^2) * D_L(5a) * Y_mag(tau, w) * D_R(5a)
                    # where D_L[i,i] = exp(+2*pi*i * ql * (5a) * i / 3), D_R[j,j] = exp(+2*pi*i * qr * (5a) * j / 3)!
                    ph_entry_5 = zeta5_35 ** ((e_mag_mod5 * five_a * five_a) % 5)
                    ym5_pred = mp.zeros(3, 3)
                    for ii in range(3):
                        dl_i = mp.exp(2 * mp.pi * iu35 * mp.mpf(ql * five_a * ii) / mp.mpf(3))
                        for jj in range(3):
                            dr_j = mp.exp(2 * mp.pi * iu35 * mp.mpf(qr * five_a * jj) / mp.mpf(3))
                            ym5_pred[ii, jj] = ph_entry_5 * dl_i * ym0[ii, jj] * dr_j
                    rel_mod3_err = mp.sqrt(frob_norm_sq(ym5 - ym5_pred) / frob_norm_sq(ym0))
                    max_mod3_twisted_unitary_err = max(max_mod3_twisted_unitary_err, rel_mod3_err)

                    # Constant-unitary (D_L = D_R = I_3) residual at 5a = 1:
                    best_const_sc = frob_inner(ym0, ym5) / frob_norm_sq(ym0)
                    const_def = mp.sqrt(frob_norm_sq(ym5 - best_const_sc * ym0) / frob_norm_sq(ym0))
                    max_const_unitary_defect = max(max_const_unitary_defect, const_def)

                c4_all_det_errs = max(c4_all_det_errs, sec_det_law_err, sec_t25_det_err, max_mod3_twisted_unitary_err)

                # Spread from first point (0, 1/5) vs pairwise diameter across all 24 points
                spread_from_p0 = max(abs(p - det_phases_t5[0]) for p in det_phases_t5)
                pairwise_diam = max(abs(p1 - p2) for p1 in det_phases_t5 for p2 in det_phases_t5)
                distinct_5th_roots = len({(int(mp.nint(mp.re(p) * 10000)), int(mp.nint(mp.im(p) * 10000))) for p in det_phases_t5})

                mag_audit[sec_name] = {
                    "E_mag_coupling_mod5": e_mag_mod5,
                    "det3x3_exponent_mod5": det_exp_mod5,
                    "Frame_D1_c2_E_mod5": e_d1_c2_mod5,
                    "Frame_D1_c2_det3x3_exponent_mod5": det_d1_c2_mod5,
                    "distinct_T5_det_phases": distinct_5th_roots,
                    "spread_from_ref_a0": m2dec(spread_from_p0),
                    "spread_matches_2sin_pi_over_5_err": m2dec(abs(spread_from_p0 - two_sin_pi_over_5)) if distinct_5th_roots > 1 else "zero_spread",
                    "pairwise_diameter": m2dec(pairwise_diam),
                    "pairwise_matches_2sin_2pi_over_5_err": m2dec(abs(pairwise_diam - two_sin_2pi_over_5)) if distinct_5th_roots > 1 else "zero_spread",
                    "det_T5_law_max_err": m2dec(sec_det_law_err),
                    "det_T25_closure_max_err": m2dec(sec_t25_det_err),
                    "matrix_mod3_heisenberg_law_max_err": m2dec(max_mod3_twisted_unitary_err),
                    "w_independent_unitary_defect": m2dec(max_const_unitary_defect),
                }

            gate_c4_passed = bool(
                c4_all_det_errs < mp.mpf(10) ** (-24)
                and mag_audit["sec_1"]["distinct_T5_det_phases"] == 1
                and mag_audit["sec_2"]["distinct_T5_det_phases"] == 3
                and mag_audit["sec_3"]["distinct_T5_det_phases"] == 3
                and abs(mp.mpf(mag_audit["sec_2"]["spread_matches_2sin_pi_over_5_err"])) < mp.mpf(10) ** (-15)
            )

        gate_pc_passed = bool(
            ast_res["Gate_AST_ZeroFloatLiterals_Passed"]
            and pc1_wrong_quad_c_min_err > mp.mpf(1)
            and pc2_omitted_odd_sign_min_err > mp.mpf(19) / mp.mpf(10)
            and len(simultaneous_closure_c_values) == 0
            and pc4_plain_sum_obstructed_min_drift > mp.mpf(1) / mp.mpf(20)
        )

        overall_passed = bool(gate_u0_passed and gate_c1_c2_c3_passed and gate_c4_passed and gate_pc_passed)

        result_payload: Dict[str, Any] = {
            "card": "X-L5",
            "protocol": "blind_statement_only_zero_main_script_read",
            "zero_of_19": True,
            "overall_x_l5_gate_passed": overall_passed,
            "gates": {
                "Gate_AST_ZeroFloatLiterals_Passed": ast_res["Gate_AST_ZeroFloatLiterals_Passed"],
                "Gate_U0_Level2Factorization_Passed": gate_u0_passed,
                "Gate_C1_C2_C3_Level5Law_and_OddCSign_Passed": gate_c1_c2_c3_passed,
                "Gate_C4_XFoundation4_ShiftedAudit_Passed": gate_c4_passed,
                "Gate_PC_AllPlantedControls_Passed": gate_pc_passed,
            },
            "summary_metrics": {
                "u0_c0_channel_residue_max_rel_err": m2dec(u0_max_rel_err),
                "c1_diag_t5_max_err": m2dec(c1_diag_t5_max_err),
                "c1_diag_t25_max_err": m2dec(c1_diag_t25_max_err),
                "c1_even_offdiag_t5_max_err": m2dec(c1_even_offdiag_t5_max_err),
                "c1_even_3x3_S_t5_max_err": m2dec(c1_even_3x3_S_t5_max_err),
                "c1_even_3x3_tildeS_t5_max_err": m2dec(c1_even_3x3_tildeS_t5_max_err),
                "c1_even_3x3_t25_max_err": m2dec(c1_even_3x3_t25_max_err),
                "c2_odd_offdiag_t5_max_err": m2dec(c2_odd_offdiag_t5_max_err),
                "c2_odd_offdiag_t25_max_err": m2dec(c2_odd_offdiag_t25_max_err),
                "c2_odd_3x3_nonscalar_min_defect": m2dec(c2_odd_3x3_nonscalar_min_defect),
                "mod5_closure_map": mod5_closure_map,
                "simultaneous_closure_c_values": simultaneous_closure_c_values,
            },
            "planted_controls": {
                "PC_XL5_1_WrongQuadraticC_min_err": m2dec(pc1_wrong_quad_c_min_err),
                "PC_XL5_2_OmittedOddCSign_min_err": m2dec(pc2_omitted_odd_sign_min_err),
                "PC_XL5_3_SimultaneousLevel5Closure_count": len(simultaneous_closure_c_values),
                "PC_XL5_4_PlainSumT5Invariance_min_drift": m2dec(pc4_plain_sum_obstructed_min_drift),
            },
            "ast_self_audit": ast_res,
            "per_c_and_sector_table": per_c_sector_table,
            "x_foundation_4_shifted_comparison": mag_audit,
        }

    out_bytes = (json.dumps(result_payload, indent=2, sort_keys=True) + "\n").encode("utf-8")
    OUT_PATH.write_bytes(out_bytes)
    sha_hex = hashlib.sha256(out_bytes).hexdigest()
    OUT_SHA_PATH.write_text(f"{sha_hex}  {OUT_PATH.name}\n", encoding="utf-8")


if __name__ == "__main__":
    main()
