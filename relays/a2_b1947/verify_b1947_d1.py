#!/usr/bin/env python3
"""Standalone 55-digit mpmath second computation of B1947's C2 (tau -> tau + 1 covariance) negative (M40, A2-B1947).

Strictly blind prior to opening frontier/B1947_frame_d1s_coupling/FINDINGS.md or its verification scripts/outputs.
Strict compliance with M40:
  - Zero shared code with frontier/ or other seats;
  - Zero measured numbers touched anywhere;
  - COMPUTES NO MIXING (no U_u^H U_d or |V| computed anywhere);
  - Physical singular-value ratios stored strictly in verify_b1947_d1.json ONLY;
  - Evaluates C0 (q_H = 0 match to Frame C B1691 q-series), C1 (q_H = -3 vs +3 component phase identity),
    exact T-transport component phases on DR, and C2 (tau -> tau + 1 covariance at (tau + 1, T*w) vs (tau, w))
    across BOTH conventions:
      * D1  (original card): Higgs characteristic shift (q_H a, 2 q_H b)
      * D1' (Amendment A1):  Higgs characteristic shift (q_H a,   q_H b)
    and BOTH theta_4 representatives:
      * Rep + (declared): theta_4 = theta[delta_alpha, +1/2 + delta_beta]
      * Rep - (other):    theta_4 = theta[delta_alpha, -1/2 + delta_beta]
    across all 24 order-5 points, 3 bulk moduli, and all 3 fermion sectors (up +3, down -3, leptons -3),
    plus untwisted Frame C control (q_H = 0), a = 0 stratum control, and Guardrail 3 Haar SU(3) scrambling.

0 of 19.
"""

from __future__ import annotations

import fractions
import json
import math
import random
import sys
import time
from pathlib import Path

import mpmath as mp
import numpy as np

mp.mp.dps = 55

HERE = Path(__file__).resolve().parent
RELAYS = HERE.parent
sys.path.insert(0, str(RELAYS / "a2_canon"))
import verify_a2_canon as a2c  # agy-002's own standalone canonical L2 interpolant


# ---------------------------------------------------------------------------
# 1. Standalone Quaternion Contraction Tensor (COUP["S"], no reading choice)
# ---------------------------------------------------------------------------

def build_frame_c_s_couplings() -> tuple[list, dict]:
    I2 = [[mp.mpc(1), mp.mpc(0)], [mp.mpc(0), mp.mpc(1)]]
    QI = [[mp.mpc(0, 1), mp.mpc(0)], [mp.mpc(0), mp.mpc(0, -1)]]
    QJ = [[mp.mpc(0), mp.mpc(1)], [mp.mpc(-1), mp.mpc(0)]]
    QK = [[mp.mpc(0), mp.mpc(0, 1)], [mp.mpc(0, 1), mp.mpc(0)]]
    EPS = QJ
    units = [I2, QI, QJ, QK]
    blocks = [QJ, QI, QK]
    q_S = [QI, QJ, QK]

    def mat_mul(A, B):
        return [
            [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]],
        ]

    def mat_T(A):
        return [[A[0][0], A[1][0]], [A[0][1], A[1][1]]]

    def had(A, B):
        return A[0][0] * B[0][0] + A[0][1] * B[0][1] + A[1][0] * B[1][0] + A[1][1] * B[1][1]

    ec_list = [mat_mul(EPS, U) for U in units]
    G = mp.matrix(4, 4)
    for t in range(4):
        for s in range(4):
            G[t, s] = had(ec_list[t], units[s])
    Ginv = G ** (-1)
    edual = []
    for a in range(4):
        M = [[mp.mpc(0), mp.mpc(0)], [mp.mpc(0), mp.mpc(0)]]
        for b in range(4):
            for r in range(2):
                for c in range(2):
                    M[r][c] += Ginv[b, a] * units[b][r][c]
        edual.append(M)

    coup_s = {}
    for qi in range(3):
        for si in range(4):
            for a in range(3):
                for b in range(3):
                    prod = mat_mul(mat_mul(mat_mul(mat_T(blocks[a]), EPS), q_S[qi]), blocks[b])
                    coup_s[(qi, si, a, b)] = had(prod, edual[si])
    return ec_list, coup_s


CHAR_SHIFTS = [
    (fractions.Fraction(0, 1), fractions.Fraction(0, 1)),
    (fractions.Fraction(0, 1), fractions.Fraction(-1, 2)),
    (fractions.Fraction(-1, 2), fractions.Fraction(0, 1)),
    (fractions.Fraction(-1, 2), fractions.Fraction(-1, 2)),
]

ORDER5_24_POINTS: list[tuple[fractions.Fraction, fractions.Fraction]] = [
    (fractions.Fraction(a, 5), fractions.Fraction(b, 5))
    for a in range(5)
    for b in range(5)
    if (a, b) != (0, 0)
]

BULK_MODULI: list[tuple[str, mp.mpc]] = [
    ("0.13+1.45i", mp.mpc("0.13", "1.45")),
    ("-0.29+1.18i", mp.mpc("-0.29", "1.18")),
    ("0.37+2.35i", mp.mpc("0.37", "2.35")),
]

SECTORS: dict[str, tuple[int, int, int]] = {
    "up": (1, -4, +3),
    "down": (1, 2, -3),
    "leptons": (-3, 6, -3),
}


# ---------------------------------------------------------------------------
# 2. Jacobi Theta with Characteristics, Twisted Higgs Serre Derivative DR,
#    and Frame D1 / D1' Yukawa Matrix Builder (Strictly NO Mixing!)
# ---------------------------------------------------------------------------

def theta_char_and_qderiv(alpha: mp.mpf, beta: mp.mpf, tau: mp.mpc, n_th: int) -> tuple[mp.mpc, mp.mpc]:
    """Evaluate (theta[alpha, beta](tau), q * d/dq theta[alpha, beta](tau)) centered at k0 = round(-alpha)."""
    k0 = round(-float(alpha))
    pi = mp.pi
    s0 = mp.mpc(0)
    s1 = mp.mpc(0)
    for k in range(-n_th, n_th + 1):
        na = mp.mpf(k + k0) + alpha
        tm = mp.exp(1j * pi * tau * (na * na) + 2j * pi * na * beta)
        s0 += tm
        s1 += mp.mpf("0.5") * (na * na) * tm
    return s0, s1


def eisenstein_e2_and_eta3(tau: mp.mpc, m_max: int) -> tuple[mp.mpc, mp.mpc]:
    """Evaluate (E_2(tau), eta(tau)^3) with full q^(1/8) = exp(i pi tau / 4) factor on eta(tau)^3."""
    pi = mp.pi
    q = mp.exp(2j * pi * tau)
    eta_prod = mp.mpc(1)
    e2 = mp.mpc(1)
    qp = mp.mpc(1)
    for m in range(1, m_max + 3):
        qp *= q
        eta_prod *= 1 - qp
        e2 -= 24 * m * qp / (1 - qp)
    eta3 = mp.exp(1j * pi * tau / 4) * (eta_prod ** 3)
    return e2, eta3


def eval_twisted_higgs_dr(
    tau: mp.mpc,
    da: fractions.Fraction,
    db: fractions.Fraction,
    rep: str,
) -> list[mp.mpc]:
    """Evaluate the 3-component Serre derivative DR = q dR/dq + (1/24) E_2 R of
    R = (-theta_2/(theta_3 theta_4), -theta_4/(theta_2 theta_3), i theta_3/(theta_2 theta_4))
    with characteristics shifted by (da, db) and theta_4 representative rep in ('+', '-')."""
    y_f = float(mp.im(tau))
    m_max = max(12, int(math.ceil(mp.mp.dps * math.log(10) / (2.0 * math.pi * max(y_f, 0.8)) + 5)))
    n_th = max(12, int(math.ceil(math.sqrt(mp.mp.dps * math.log(10) / (math.pi * max(y_f, 0.8))) + 5)))

    da_m = mp.mpf(da.numerator) / mp.mpf(da.denominator)
    db_m = mp.mpf(db.numerator) / mp.mpf(db.denominator)
    half = mp.mpf(1) / mp.mpf(2)
    b4_shift = +half if rep == "+" else -half

    t2, dt2 = theta_char_and_qderiv(half + da_m, db_m, tau, n_th)
    t3, dt3 = theta_char_and_qderiv(da_m, db_m, tau, n_th)
    t4, dt4 = theta_char_and_qderiv(da_m, b4_shift + db_m, tau, n_th)
    e2, _ = eisenstein_e2_and_eta3(tau, m_max)

    r0 = -t2 / (t3 * t4)
    r1 = -t4 / (t2 * t3)
    r2 = 1j * t3 / (t2 * t4)

    lt2 = dt2 / t2
    lt3 = dt3 / t3
    lt4 = dt4 / t4

    dr0 = r0 * (lt2 - lt3 - lt4) + (e2 / 24) * r0
    dr1 = r1 * (lt4 - lt2 - lt3) + (e2 / 24) * r1
    dr2 = r2 * (lt3 - lt2 - lt4) + (e2 / 24) * r2
    return [dr0, dr1, dr2]


def eval_frame_c_untwisted_b1(tau: mp.mpc) -> list[mp.mpc]:
    """Frame C's untwisted B1691 B[1] q-series components via N = (-theta_2^2, -theta_4^2, i theta_3^2) / (2 eta^3)."""
    y_f = float(mp.im(tau))
    m_max = max(12, int(math.ceil(mp.mp.dps * math.log(10) / (2.0 * math.pi * max(y_f, 0.8)) + 5)))
    n_th = max(12, int(math.ceil(math.sqrt(mp.mp.dps * math.log(10) / (math.pi * max(y_f, 0.8))) + 5)))
    half = mp.mpf(1) / mp.mpf(2)
    t2, dt2 = theta_char_and_qderiv(half, mp.mpf(0), tau, n_th)
    t3, dt3 = theta_char_and_qderiv(mp.mpf(0), mp.mpf(0), tau, n_th)
    t4, dt4 = theta_char_and_qderiv(mp.mpf(0), half, tau, n_th)
    e2, eta3 = eisenstein_e2_and_eta3(tau, m_max)
    den = 2 * eta3
    r_h = [-(t2 * t2) / den, -(t4 * t4) / den, 1j * (t3 * t3) / den]
    dn_h = [-2 * t2 * dt2 / den, -2 * t4 * dt4 / den, 2j * t3 * dt3 / den]
    return [dn_h[i] - (e2 / 12) * r_h[i] for i in range(3)]


_UCH_CACHE: dict[tuple, list[mp.mpc]] = {}


def eval_matter_uch_cached(
    tau: mp.mpc,
    l2: mp.mpf,
    w: tuple[fractions.Fraction, fractions.Fraction],
    q_L: int,
    q_R: int,
    ec_list: list,
    reduce_matter_mod1: bool = True,
) -> list[mp.mpc]:
    key = (str(tau), str(l2), w[0], w[1], q_L, q_R, reduce_matter_mod1)
    if key in _UCH_CACHE:
        return _UCH_CACHE[key]

    x_r, y_r = mp.re(tau), mp.im(tau)
    pi = mp.pi
    eg = mp.euler
    q = mp.exp(2j * pi * tau)
    y_f = float(y_r)
    m_max = max(12, int(math.ceil(mp.mp.dps * math.log(10) / (2.0 * math.pi * max(y_f, 0.8)) + 5)))
    n_th = max(12, int(math.ceil(math.sqrt(mp.mp.dps * math.log(10) / (math.pi * max(y_f, 0.8))) + 5)))

    a, b = w
    _, eta3 = eisenstein_e2_and_eta3(tau, m_max)
    denom_matter = 2 * pi * eta3

    w_L = ((q_L * a) % 1, (q_L * b) % 1) if reduce_matter_mod1 else (q_L * a, q_L * b)
    w_R = ((q_R * a) % 1, (q_R * b) % 1) if reduce_matter_mod1 else (q_R * a, q_R * b)

    def thc01(aa: mp.mpf, bb: mp.mpf):
        k0 = round(-float(aa))
        k1 = round(-float(aa) - 0.5)
        X0 = mp.mpc(0)
        X1 = mp.mpc(0)
        for k in range(-n_th, n_th + 1):
            n0 = mp.mpf(k + k0) + aa
            X0 += mp.exp(2j * pi * tau * n0 * n0 + 2j * pi * n0 * bb)
            n1 = mp.mpf(k + k1) + aa
            X1 += mp.exp(2j * pi * tau * ((n1 + mp.mpf("0.5")) ** 2) + 2j * pi * n1 * bb)
        return X0, X1

    ax = mp.mpf(w_L[0].numerator) / mp.mpf(w_L[0].denominator)
    bx = 2 * mp.mpf(w_L[1].numerator) / mp.mpf(w_L[1].denominator)
    ay = mp.mpf(w_R[0].numerator) / mp.mpf(w_R[0].denominator)
    by = 2 * mp.mpf(w_R[1].numerator) / mp.mpf(w_R[1].denominator)
    X0, X1 = thc01(ax, bx)
    Y0, Y1 = thc01(ay, by)
    Mm = [
        [X0 * Y0 / denom_matter, mp.exp(1j * pi * by) * X0 * Y1 / (1j * denom_matter)],
        [mp.exp(1j * pi * bx) * X1 * Y0 / (1j * denom_matter), -mp.exp(1j * pi * (bx + by)) * X1 * Y1 / denom_matter],
    ]
    R_ch = [sum(ec_list[si][r][c] * Mm[r][c] for r in range(2) for c in range(2)) for si in range(4)]

    shift_old = 2 * pi * (l2 + mp.mpf("0.5") * mp.log(y_r) - eg - mp.log(pi))
    em2l2 = mp.exp(-2 * l2)
    u_sum_a = w_L[0] + w_R[0]
    u_sum_b = w_L[1] + w_R[1]
    u_ch = []
    for si, (ds1, ds2) in enumerate(CHAR_SHIFTS):
        ua = (u_sum_a + ds1) % 1
        ub = (u_sum_b + ds2) % 1
        if ua == 0 and ub == 0:
            u_ch.append(mp.mpc(0))
            continue
        a_m = mp.mpf(ua.numerator) / mp.mpf(ua.denominator)
        b_m = mp.mpf(ub.numerator) / mp.mpf(ub.denominator)
        if ua == 0:
            fu = pi * (2 * eg - 2 * mp.log(2) - mp.log(y_r)) + (pi ** 2) * y_r / (mp.sin(pi * b_m) ** 2)
            for m in range(1, m_max + 2):
                for ms in (mp.mpf(m), mp.mpf(-m)):
                    wm = mp.exp(2j * pi * (ms * x_r + b_m) - 2 * pi * abs(ms) * y_r)
                    fu += (2 * pi / abs(ms)) * mp.re(wm / (1 - wm))
        else:
            fu = -pi * (mp.digamma(a_m) + mp.digamma(1 - a_m) + 2 * mp.log(2) + mp.log(y_r))
            for k in range(-m_max - 1, m_max + 2):
                ms = mp.mpf(k) + a_m
                wm = mp.exp(2j * pi * (ms * x_r + b_m) - 2 * pi * abs(ms) * y_r)
                fu += (2 * pi / abs(ms)) * mp.re(wm / (1 - wm))
        nu_f = ua if ua <= fractions.Fraction(1, 2) else ua - 1
        nu = mp.mpf(nu_f.numerator) / mp.mpf(nu_f.denominator)
        bm_neg = (-ub) % 1
        Bm = mp.mpf(bm_neg.numerator) / mp.mpf(bm_neg.denominator)
        w_z = nu * tau - Bm
        ser = mp.mpc(0)
        for m in range(1, m_max + 2):
            qm = q ** m
            ser += (mp.exp(2j * pi * m * (tau + w_z)) - mp.exp(2j * pi * m * (tau - w_z))) / (2j * (1 - qm))
        a0 = pi * mp.cot(pi * w_z) + 4 * pi * ser + 2j * pi * nu
        val = shift_old + fu - pi * (abs(a0) ** 2) * em2l2
        u_ch.append(mp.sqrt(val) * R_ch[si])

    _UCH_CACHE[key] = u_ch
    return u_ch


def eval_d1_yukawa_mp(
    tau: mp.mpc,
    l2: mp.mpf,
    w: tuple[fractions.Fraction, fractions.Fraction],
    q_L: int,
    q_R: int,
    q_H: int,
    convention: str,
    rep: str,
    ec_list: list,
    coup_s: dict,
    reduce_matter_mod1: bool = True,
) -> mp.matrix:
    """Evaluate 3x3 Yukawa matrix in Frame D1 / D1' (or untwisted Frame C when q_H = 0).
    Matter residues and exact_T90 channel weights follow Frame C identically; Higgs triplet uses DR(tau; da, db; rep)."""
    a, b = w
    if convention == "untwisted":
        da, db = fractions.Fraction(0, 1), fractions.Fraction(0, 1)
    elif convention == "D1":
        da, db = q_H * a, 2 * q_H * b
    elif convention == "D1_prime":
        da, db = q_H * a, q_H * b
    else:
        raise ValueError(f"Unknown convention: {convention}")

    c3 = eval_twisted_higgs_dr(tau, da, db, rep)
    u_ch = eval_matter_uch_cached(tau, l2, w, q_L, q_R, ec_list, reduce_matter_mod1)

    Ym = mp.matrix(3, 3)
    for a_i in range(3):
        for b_i in range(3):
            s_val = mp.mpc(0)
            for qi in range(3):
                for si in range(4):
                    cc = coup_s[(qi, si, a_i, b_i)]
                    if cc != 0:
                        s_val += c3[qi] * u_ch[si] * cc
            Ym[a_i, b_i] = s_val
    return Ym


def sv_mass_ratios_no_mixing(Y: mp.matrix) -> tuple[mp.mpf, mp.mpf]:
    """Extract strictly basis-invariant singular-value mass ratios (sigma_2 / sigma_3, sigma_1 / sigma_3) in (0, 1].
    Computes NO mixing matrices or cross-sector overlaps."""
    H = Y * Y.H
    for r in range(3):
        H[r, r] = mp.re(H[r, r])
        for c in range(r + 1, 3):
            avg = mp.mpf("0.5") * (H[r, c] + mp.conj(H[c, r]))
            H[r, c] = avg
            H[c, r] = mp.conj(avg)
    evals, _ = mp.eighe(H)
    sigs = sorted([mp.sqrt(max(mp.mpf(0), mp.re(ev))) for ev in evals])
    return sigs[1] / sigs[2], sigs[0] / sigs[2]


def random_su3_mp(rng: random.Random) -> mp.matrix:
    M = mp.matrix(3, 3)
    for r in range(3):
        for c in range(3):
            M[r, c] = mp.mpc(rng.gauss(0.0, 1.0), rng.gauss(0.0, 1.0))
    Q, R = mp.qr(M)
    for i in range(3):
        ph = R[i, i] / abs(R[i, i])
        for r in range(3):
            Q[r, i] *= ph
    det_q = (
        Q[0, 0] * (Q[1, 1] * Q[2, 2] - Q[1, 2] * Q[2, 1])
        - Q[0, 1] * (Q[1, 0] * Q[2, 2] - Q[1, 2] * Q[2, 0])
        + Q[0, 2] * (Q[1, 0] * Q[2, 1] - Q[1, 1] * Q[2, 0])
    )
    ph_det = mp.exp(-1j * mp.arg(det_q) / 3)
    return Q * ph_det


# ---------------------------------------------------------------------------
# 3. Main Execution: C0, C1, Component T-Transport Theorem, C2, and Controls
# ---------------------------------------------------------------------------

def main() -> None:
    t0 = time.time()
    mp.mp.dps = 55
    ec_list, coup_s = build_frame_c_s_couplings()
    l2_interp = a2c.CanonicalL2Interpolant()

    # Canonical L2 at the 3 bulk moduli (note tau and tau+1 share the exact same FD pullback):
    tau_l2: dict[str, mp.mpf] = {}
    for label, tau in BULK_MODULI:
        tc = complex(float(mp.re(tau)), float(mp.im(tau)))
        t_fd, _, _ = a2c.pullback_b1724(np.array([tc], dtype=np.complex128), 0.0, 0.2)
        t_fd1, _, _ = a2c.pullback_b1724(np.array([tc + 1.0], dtype=np.complex128), 0.0, 0.2)
        assert abs(t_fd[0] - t_fd1[0]) < 1e-14
        l2_v = float(l2_interp.eval_fd(t_fd)[0])
        tau_l2[label] = mp.mpf(repr(l2_v))

    # --- Check C0: q_H = 0 match to Frame C's untwisted B1691 B[1] q-series & finite-diff derivative check ---
    max_c0_rel_err = 0.0
    max_fd_deriv_err = 0.0
    eps_fd = mp.mpf("1e-18")
    for label, tau in BULK_MODULI:
        b1_ref = eval_frame_c_untwisted_b1(tau)
        for rep in ("+", "-"):
            dr_0 = eval_twisted_higgs_dr(tau, fractions.Fraction(0, 1), fractions.Fraction(0, 1), rep)
            num = mp.sqrt(sum(abs(dr_0[k] - b1_ref[k]) ** 2 for k in range(3)))
            den = mp.sqrt(sum(abs(b1_ref[k]) ** 2 for k in range(3)))
            max_c0_rel_err = max(max_c0_rel_err, float(num / den))

        # Independent central-difference verification of q dR/dq = (1 / (2 pi i)) dR/dtau at twisted (3/5, 4/5):
        da_t, db_t = fractions.Fraction(3, 5), fractions.Fraction(4, 5)
        e2_t, _ = eisenstein_e2_and_eta3(tau, 30)
        dr_exact = eval_twisted_higgs_dr(tau, da_t, db_t, "+")

        def eval_R_only(z: mp.mpc):
            half = mp.mpf(1) / 2
            t2, _ = theta_char_and_qderiv(half + mp.mpf(3) / 5, mp.mpf(4) / 5, z, 28)
            t3, _ = theta_char_and_qderiv(mp.mpf(3) / 5, mp.mpf(4) / 5, z, 28)
            t4, _ = theta_char_and_qderiv(mp.mpf(3) / 5, half + mp.mpf(4) / 5, z, 28)
            return [-t2 / (t3 * t4), -t4 / (t2 * t3), 1j * t3 / (t2 * t4)]

        r_here = eval_R_only(tau)
        r_plus = eval_R_only(tau + eps_fd)
        r_minus = eval_R_only(tau - eps_fd)
        dr_fd = [
            ((r_plus[k] - r_minus[k]) / (2 * eps_fd)) / (2j * mp.pi) + (e2_t / 24) * r_here[k]
            for k in range(3)
        ]
        fd_err = float(max(abs(dr_exact[k] - dr_fd[k]) / abs(dr_exact[k]) for k in range(3)))
        max_fd_deriv_err = max(max_fd_deriv_err, fd_err)

    assert max_c0_rel_err < 1e-48, f"C0 failed: {max_c0_rel_err}"
    assert max_fd_deriv_err < 1e-32, f"Derivative check failed: {max_fd_deriv_err}"

    # --- Check C1: Exact component-phase relation DR(-3) vs DR(+3) across both conventions & both reps ---
    c1_max_rel_err = {"D1_+": 0.0, "D1_-": 0.0, "D1_prime_+": 0.0, "D1_prime_-": 0.0}
    for _, tau in BULK_MODULI:
        for a, b in ORDER5_24_POINTS:
            phi = 2 * mp.pi * (3 * mp.mpf(a.numerator) / mp.mpf(a.denominator))
            for conv, b_mult in (("D1", 2), ("D1_prime", 1)):
                for rep, sgn in (("+", +1), ("-", -1)):
                    dr_p3 = eval_twisted_higgs_dr(tau, +3 * a, +3 * b_mult * b, rep)
                    dr_m3 = eval_twisted_higgs_dr(tau, -3 * a, -3 * b_mult * b, rep)
                    pred = [
                        mp.exp(1j * sgn * phi) * dr_p3[0],
                        mp.exp(-1j * sgn * phi) * dr_p3[1],
                        mp.exp(1j * sgn * phi) * dr_p3[2],
                    ]
                    err = mp.sqrt(sum(abs(dr_m3[k] - pred[k]) ** 2 for k in range(3))) / mp.sqrt(
                        sum(abs(dr_p3[k]) ** 2 for k in range(3))
                    )
                    c1_max_rel_err[f"{conv}_{rep}"] = max(c1_max_rel_err[f"{conv}_{rep}"], float(err))
    for k, v in c1_max_rel_err.items():
        assert v < 1e-48, f"C1 phase relation failed on {k}: {v}"

    # --- Exact Algebraic Component-Transport Theorem Check for D1' under (tau, w) -> (tau + 1, (a, b - a)) ---
    d1p_transport_law_err = {"+": 0.0, "-": 0.0}
    for _, tau in BULK_MODULI:
        for a, b in ORDER5_24_POINTS:
            for q_H in (+3, -3):
                da = q_H * a
                da_m = mp.mpf(da.numerator) / mp.mpf(da.denominator)
                overall = mp.exp(1j * mp.pi / 4 + 1j * mp.pi * (da_m ** 2))
                rel_ph = mp.exp(2j * mp.pi * da_m)
                for rep in ("+", "-"):
                    dr_0 = eval_twisted_higgs_dr(tau, da, q_H * b, rep)
                    dr_1 = eval_twisted_higgs_dr(tau + 1, da, q_H * (b - a), rep)
                    if rep == "+":
                        pred = [overall * dr_0[0], overall * rel_ph * dr_0[2], -overall * (1 / rel_ph) * dr_0[1]]
                    else:
                        pred = [overall * dr_0[0], overall * (1 / rel_ph) * dr_0[2], -overall * rel_ph * dr_0[1]]
                    err = mp.sqrt(sum(abs(dr_1[k] - pred[k]) ** 2 for k in range(3))) / mp.sqrt(
                        sum(abs(dr_0[k]) ** 2 for k in range(3))
                    )
                    d1p_transport_law_err[rep] = max(d1p_transport_law_err[rep], float(err))
    assert d1p_transport_law_err["+"] < 1e-48 and d1p_transport_law_err["-"] < 1e-48

    # --- Check C2: tau -> tau + 1 Covariance of Mass Ratios (sigma_2/sigma_3, sigma_1/sigma_3), NO MIXING ---
    # Test all 4 combinations (D1/D1', +/-) + untwisted Frame C control across 3 moduli x 24 points x 3 sectors,
    # for BOTH reduced T*w = (a, (b - a) mod 1) and unreduced T*w = (a, b - a):
    c2_summary: dict[str, dict] = {}
    sample_ratios_json_only: dict[str, dict] = {}

    configs = [
        ("CTL_untwisted_Frame_C", "untwisted", "+"),
        ("D1_rep_plus", "D1", "+"),
        ("D1_rep_minus", "D1", "-"),
        ("D1_prime_rep_plus", "D1_prime", "+"),
        ("D1_prime_rep_minus", "D1_prime", "-"),
    ]

    for tag, conv, rep in configs:
        max_abs_diff_all = 0.0
        max_dln_all = 0.0
        max_dln_unreduced_Tw = 0.0
        max_dln_a0_stratum = 0.0
        min_dln_a_nonzero_worst_sector = {}
        by_sector: dict[str, dict] = {}
        sample_ratios_json_only[tag] = {}

        for sec_name, (q_L, q_R, q_H_sec) in SECTORS.items():
            q_H_use = 0 if conv == "untwisted" else q_H_sec
            sec_max_abs = 0.0
            sec_max_dln = 0.0
            sec_max_dln_unred = 0.0
            sec_max_dln_a0 = 0.0
            sec_a_nonzero_point_dlns = []

            for m_idx, (m_label, tau) in enumerate(BULK_MODULI):
                l2_v = tau_l2[m_label]
                for w_idx, (a, b) in enumerate(ORDER5_24_POINTS):
                    w_T_red = (a, (b - a) % 1)
                    w_T_unred = (a, b - a)

                    Y0 = eval_d1_yukawa_mp(tau, l2_v, (a, b), q_L, q_R, q_H_use, conv, rep, ec_list, coup_s)
                    Y1_red = eval_d1_yukawa_mp(tau + 1, l2_v, w_T_red, q_L, q_R, q_H_use, conv, rep, ec_list, coup_s)
                    Y1_unred = eval_d1_yukawa_mp(tau + 1, l2_v, w_T_unred, q_L, q_R, q_H_use, conv, rep, ec_list, coup_s)

                    r2_0, r1_0 = sv_mass_ratios_no_mixing(Y0)
                    r2_1, r1_1 = sv_mass_ratios_no_mixing(Y1_red)
                    r2_u, r1_u = sv_mass_ratios_no_mixing(Y1_unred)

                    abs_d = float(max(abs(r2_1 - r2_0), abs(r1_1 - r1_0)))
                    dln_d = float(max(abs(mp.log(r2_1 / r2_0)), abs(mp.log(r1_1 / r1_0))))
                    dln_u = float(max(abs(mp.log(r2_u / r2_0)), abs(mp.log(r1_u / r1_0))))

                    sec_max_abs = max(sec_max_abs, abs_d)
                    sec_max_dln = max(sec_max_dln, dln_d)
                    sec_max_dln_unred = max(sec_max_dln_unred, dln_u)

                    if a == 0:
                        sec_max_dln_a0 = max(sec_max_dln_a0, dln_d)
                    else:
                        sec_a_nonzero_point_dlns.append(dln_d)

                    if m_idx == 0 and w_idx == 6:  # representative (1/5, 2/5) stored in JSON only
                        sample_ratios_json_only[tag][sec_name] = {
                            "tau": m_label,
                            "w": [float(a), float(b)],
                            "at_tau_w_r2_r1": [float(r2_0), float(r1_0)],
                            "at_tau_plus_1_Tw_r2_r1": [float(r2_1), float(r1_1)],
                        }

            max_abs_diff_all = max(max_abs_diff_all, sec_max_abs)
            max_dln_all = max(max_dln_all, sec_max_dln)
            max_dln_unreduced_Tw = max(max_dln_unreduced_Tw, sec_max_dln_unred)
            max_dln_a0_stratum = max(max_dln_a0_stratum, sec_max_dln_a0)
            min_dln_a_nonzero_worst_sector[sec_name] = float(min(sec_a_nonzero_point_dlns))
            by_sector[sec_name] = {
                "max_abs_ratio_diff_reduced_Tw": sec_max_abs,
                "max_abs_dln_ratio_reduced_Tw": sec_max_dln,
                "max_abs_dln_ratio_unreduced_Tw": sec_max_dln_unred,
                "max_abs_dln_on_a_eq_0_stratum": sec_max_dln_a0,
                "n_failing_a_nonzero_cases_gt_1e_6": sum(1 for x in sec_a_nonzero_point_dlns if x > 1e-6),
                "total_a_nonzero_cases": len(sec_a_nonzero_point_dlns),
            }

        c2_summary[tag] = {
            "convention": conv,
            "theta4_rep": rep,
            "passes_C2": max_dln_all < 1e-12,
            "max_abs_ratio_diff_all_sectors": max_abs_diff_all,
            "max_abs_dln_ratio_reduced_Tw_all_sectors": max_dln_all,
            "max_abs_dln_ratio_unreduced_Tw_all_sectors": max_dln_unreduced_Tw,
            "max_abs_dln_on_a_eq_0_stratum_4pts": max_dln_a0_stratum,
            "by_sector": by_sector,
        }

    # Assertions on C2 and controls:
    assert c2_summary["CTL_untwisted_Frame_C"]["max_abs_dln_ratio_reduced_Tw_all_sectors"] < 1e-45
    assert c2_summary["CTL_untwisted_Frame_C"]["passes_C2"] is True
    for bad_tag in ("D1_rep_plus", "D1_rep_minus", "D1_prime_rep_plus", "D1_prime_rep_minus"):
        assert c2_summary[bad_tag]["passes_C2"] is False
        assert c2_summary[bad_tag]["max_abs_dln_ratio_reduced_Tw_all_sectors"] > 0.5
        assert c2_summary[bad_tag]["max_abs_dln_on_a_eq_0_stratum_4pts"] < 1e-45
        for sec_name in ("up", "down", "leptons"):
            st = c2_summary[bad_tag]["by_sector"][sec_name]
            assert st["n_failing_a_nonzero_cases_gt_1e_6"] == st["total_a_nonzero_cases"] == 60

    # --- Mandatory Guardrail 3: Random Haar SU(3)_L x SU(3)_R Basis Scrambling Test ---
    rng = random.Random(2026111540)
    tau_g, l2_g = BULK_MODULI[0][1], tau_l2[BULK_MODULI[0][0]]
    Y_test = eval_d1_yukawa_mp(
        tau_g, l2_g, (fractions.Fraction(1, 5), fractions.Fraction(2, 5)),
        1, -4, +3, "D1_prime", "+", ec_list, coup_s
    )
    r2_base, r1_base = sv_mass_ratios_no_mixing(Y_test)
    U0_lr, _, Vh0_lr = mp.svd_c(Y_test)
    ov_base = U0_lr.H * Vh0_lr.H

    max_haar_ratio_drift = 0.0
    min_planted_lr_drift = 1e9
    for _ in range(8):
        UL = random_su3_mp(rng)
        UR = random_su3_mp(rng)
        Y_scr = UL * Y_test * UR.H
        r2_s, r1_s = sv_mass_ratios_no_mixing(Y_scr)
        max_haar_ratio_drift = max(max_haar_ratio_drift, float(max(abs(r2_s - r2_base), abs(r1_s - r1_base))))
        Us_lr, _, Vhs_lr = mp.svd_c(Y_scr)
        ov_scr = Us_lr.H * Vhs_lr.H
        mat_drift = max(float(abs(abs(ov_scr[r, c]) - abs(ov_base[r, c]))) for r in range(3) for c in range(3))
        min_planted_lr_drift = min(min_planted_lr_drift, mat_drift)

    assert max_haar_ratio_drift < 1e-45
    assert min_planted_lr_drift > 1e-2

    elapsed = time.time() - t0
    out = {
        "card": "A2-B1947 (M40)",
        "seat": "agy-002",
        "date": "2026-11-15",
        "blind_before_opening_b1947_findings_or_code": True,
        "data_free": True,
        "mixing_computed": False,
        "working_precision_dps": 55,
        "elapsed_seconds": round(elapsed, 2),
        "C0_untwisted_match_to_B1691_B1": {
            "max_rel_l2_err_across_3_moduli_both_reps": max_c0_rel_err,
            "central_difference_q_deriv_cross_check_err": max_fd_deriv_err,
        },
        "C1_sign_flip_phase_identity_rel_err": c1_max_rel_err,
        "D1_prime_exact_T_transport_component_phase_law_rel_err": d1p_transport_law_err,
        "C2_tau_plus_1_mass_ratio_covariance": c2_summary,
        "CTL_B1947_HAAR_guardrail3": {
            "max_haar_su3_ratio_drift": max_haar_ratio_drift,
            "planted_lr_overlap_min_drift": min_planted_lr_drift,
            "caught": min_planted_lr_drift > 1e-2,
        },
        "sample_mass_ratios_json_only": sample_ratios_json_only,
    }
    (HERE / "verify_b1947_d1.json").write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")

    # Mask-safe summary text (ZERO physical ratio values printed; only covariance drifts and residuals):
    lines = [
        "=== agy-002 Standalone Verifier: Card A2-B1947 (M40 — Frame D1 / D1' C2 Covariance) ===",
        f"Elapsed: {elapsed:.2f}s | 55-dps mpmath | Mixing computed: False | Blind: True",
        "",
        "--- Check C0 & C1 & Algebraic T-Transport Law ---",
        f"  C0 (q_H = 0 vs Frame C B1691 B[1], 3 moduli, +/- reps): max rel err = {max_c0_rel_err:.3e}",
        f"  Central-diff cross-check of Serre derivative q dR/dq:   max rel err = {max_fd_deriv_err:.3e}",
        f"  C1 (DR(-3) vs DR(+3) with phi = 2*pi*3a, 72 cases):     D1(+) = {c1_max_rel_err['D1_+']:.3e}, D1(-) = {c1_max_rel_err['D1_-']:.3e}, D1'(+) = {c1_max_rel_err['D1_prime_+']:.3e}, D1'(-) = {c1_max_rel_err['D1_prime_-']:.3e}",
        f"  Exact D1' T-transport component phase law (144 cases):  Rep(+) err = {d1p_transport_law_err['+']:.3e}, Rep(-) err = {d1p_transport_law_err['-']:.3e}",
        "",
        "--- Check C2: tau -> tau + 1 Mass-Ratio Covariance (3 bulk moduli x 24 pts x 3 sectors, NO MIXING) ---",
    ]
    for tag, _, _ in configs:
        st = c2_summary[tag]
        u_dln = st["by_sector"]["up"]["max_abs_dln_ratio_reduced_Tw"]
        d_dln = st["by_sector"]["down"]["max_abs_dln_ratio_reduced_Tw"]
        l_dln = st["by_sector"]["leptons"]["max_abs_dln_ratio_reduced_Tw"]
        a0_dln = st["max_abs_dln_on_a_eq_0_stratum_4pts"]
        lines.append(
            f"  {tag:24s}: passes_C2 = {str(st['passes_C2']):5s} | max |d ln(sigma_i/sigma_3)| = {st['max_abs_dln_ratio_reduced_Tw_all_sectors']:.4e} "
            f"(up {u_dln:.4f}, down {d_dln:.4f}, lep {l_dln:.4f}; max |d ratio| = {st['max_abs_ratio_diff_all_sectors']:.4f}; a=0 4-pt stratum = {a0_dln:.3e})"
        )
    lines += [
        "",
        "--- Mandatory Controls ---",
        f"  CTL-B1947-UNTWISTED (q_H = 0): max |d ln| = {c2_summary['CTL_untwisted_Frame_C']['max_abs_dln_ratio_reduced_Tw_all_sectors']:.3e} (PASS)",
        "  CTL-B1947-A0-STRATUM:          4/24 points with a=0 give < 1e-45, while 60/60 cases (20 a!=0 pts x 3 moduli) fail > 1e-6 in EVERY sector and EVERY (D1/D1', +/-) variant!",
        f"  CTL-B1947-HAAR (Guardrail 3):  max SU(3)^2 drift = {max_haar_ratio_drift:.3e}, planted U^H V drift = {min_planted_lr_drift:.3e} -> CAUGHT",
        "",
        "OUTCOME: NEGATIVE CONFIRMED ON ALL FOUR COMBINATIONS (D1/D1' x Rep+/Rep-). 0 of 19.",
    ]
    txt = "\n".join(lines) + "\n"
    (HERE / "verify_b1947_d1_out.txt").write_text(txt, encoding="utf-8")
    print(txt, end="")


if __name__ == "__main__":
    main()
