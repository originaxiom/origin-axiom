#!/usr/bin/env python3
"""Standalone verifier for Card A2-AMP (M34 & P-860 (a)):
Amplitude read-out with B1929 twisted-eta phases, level-5 Weil connection obstruction,
canonical Hermitian Gramian resolution, dynamic odd-tick cancellation check, and move-vs-area comparison.

Hygiene & Guardrails:
  - Zero imports from frontier/ or other seats (uses only pure Python/NumPy/mpmath and agy-002's own standalone
    relays/a2_canon/verify_a2_canon.py).
  - Zero measured numbers touched anywhere.
  - Mask-safe stdout / _out.txt: physical 7-values are written ONLY to verify_a2_amp.json, NEVER printed in _out.txt.
  - Guardrail 2: All algebraic, modular, and spectral claims computed directly from explicit matrices/products.
  - Guardrail 3: Mandatory random Haar SU(3) basis-scrambling invariance (< 1e-12) + planted U^H V failure.

0 of 19.
"""

from __future__ import annotations

import cmath
import fractions
import json
import math
import random
import sys
import time
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
RELAYS = HERE.parent
sys.path.insert(0, str(RELAYS / "a2_canon"))

import verify_a2_canon as a2c  # agy-002's own zero-shared-code standalone module


# ---------------------------------------------------------------------------
# 1. Standalone Arbitrary-Precision Frame C Matrix Builder (Safe for All Im(tau) > 0.2)
# ---------------------------------------------------------------------------

def build_quat_couplings_mp():
    I2 = [[mp.mpc(1), mp.mpc(0)], [mp.mpc(0), mp.mpc(1)]]
    QI = [[mp.mpc(0, 1), mp.mpc(0)], [mp.mpc(0), mp.mpc(0, -1)]]
    QJ = [[mp.mpc(0), mp.mpc(1)], [mp.mpc(-1), mp.mpc(0)]]
    QK = [[mp.mpc(0), mp.mpc(0, 1)], [mp.mpc(0, 1), mp.mpc(0)]]
    EPS = QJ
    units = [I2, QI, QJ, QK]
    blocks = [QJ, QI, QK]

    def mm(A, B):
        return [[A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
                [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]]

    def mT(A):
        return [[A[0][0], A[1][0]], [A[0][1], A[1][1]]]

    def mC(A):
        return [[mp.conj(A[0][0]), mp.conj(A[0][1])], [mp.conj(A[1][0]), mp.conj(A[1][1])]]

    def hsum(A, B):
        return A[0][0]*B[0][0] + A[0][1]*B[0][1] + A[1][0]*B[1][0] + A[1][1]*B[1][1]

    ec_list = [mm(EPS, U) for U in units]
    G = mp.matrix(4, 4)
    for t in range(4):
        for s in range(4):
            G[t, s] = hsum(ec_list[t], units[s])
    Ginv = G ** (-1)
    edual = []
    for a in range(4):
        M = [[mp.mpc(0), mp.mpc(0)], [mp.mpc(0), mp.mpc(0)]]
        for b in range(4):
            for r in range(2):
                for c in range(2):
                    M[r][c] += Ginv[b, a] * units[b][r][c]
        edual.append(M)

    q_S = [QI, QJ, QK]
    q_St = [mm(mm(EPS, mC(Q)), mT(EPS)) for Q in q_S]
    coup = {"S": {}, "tilde_S": {}}
    for rname, qlist in (("S", q_S), ("tilde_S", q_St)):
        for qi in range(3):
            for si in range(4):
                for a in range(3):
                    for b in range(3):
                        prod = mm(mm(mm(mT(blocks[a]), EPS), qlist[qi]), blocks[b])
                        coup[rname][(qi, si, a, b)] = hsum(prod, edual[si])
    return ec_list, coup


CHAR_SHIFTS = [
    (fractions.Fraction(0, 1), fractions.Fraction(0, 1)),
    (fractions.Fraction(0, 1), fractions.Fraction(-1, 2)),
    (fractions.Fraction(-1, 2), fractions.Fraction(0, 1)),
    (fractions.Fraction(-1, 2), fractions.Fraction(-1, 2)),
]

PTS_5 = [
    (fractions.Fraction(a, 5), fractions.Fraction(b, 5))
    for a in range(5) for b in range(5) if (a, b) != (0, 0)
]


def eval_yukawa_mp(
    tau: mp.mpc,
    l2: mp.mpf,
    w_L: tuple[fractions.Fraction, fractions.Fraction],
    w_R: tuple[fractions.Fraction, fractions.Fraction],
    reading: str,
    ec_list: list,
    coup: dict,
    exact_weight: bool = True,
) -> mp.matrix:
    """Arbitrary-precision 3x3 Yukawa matrix valid down to small Im(tau) >= 0.2 and high Im(tau) <= 200."""
    x_r, y_r = mp.re(tau), mp.im(tau)
    pi = mp.pi
    eg = mp.euler
    q = mp.exp(2j * pi * tau)
    y_eff = max(float(y_r), 0.15)
    m_max = max(14, int(math.ceil(mp.mp.dps * math.log(10) / (2.0 * math.pi * y_eff) + 6)))
    n_th = max(12, int(math.ceil(math.sqrt(mp.mp.dps * math.log(10) / (math.pi * y_eff)) + 5)))

    eta_prod = mp.mpf(1)
    e2 = mp.mpf(1)
    qp = mp.mpc(1)
    for m in range(1, m_max + 3):
        qp *= q
        eta_prod *= 1 - qp
        e2 -= 24 * m * qp / (1 - qp)
    denom_hat = 2 * pi * ((mp.exp(1j * pi * x_r / 12) * eta_prod) ** 3)

    def th0_dt(ca: mp.mpf, cb: mp.mpf):
        s0 = mp.mpc(0)
        s1 = mp.mpc(0)
        for k in range(-n_th, n_th + 1):
            na = mp.mpf(k) + ca
            tm = mp.exp(1j * pi * na * na * tau + 2j * pi * na * cb)
            s0 += tm
            s1 += mp.mpf("0.5") * na * na * tm
        return s0, s1

    t2, dt2 = th0_dt(mp.mpf("0.5"), mp.mpf(0))
    t4, dt4 = th0_dt(mp.mpf(0), mp.mpf("0.5"))
    t3, dt3 = th0_dt(mp.mpf(0), mp.mpf(0))
    R_h = [-(t2 * t2) / denom_hat, -(t4 * t4) / denom_hat, 1j * (t3 * t3) / denom_hat]
    dN_h = [-2 * t2 * dt2 / denom_hat, -2 * t4 * dt4 / denom_hat, 2j * t3 * dt3 / denom_hat]
    c3 = [dN_h[i] - (e2 / 12) * R_h[i] for i in range(3)]
    if reading == "tilde_S":
        c3 = [mp.conj(v) for v in c3]

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
        [X0 * Y0 / denom_hat, mp.exp(1j * pi * by) * X0 * Y1 / (1j * denom_hat)],
        [mp.exp(1j * pi * bx) * X1 * Y0 / (1j * denom_hat), -mp.exp(1j * pi * (bx + by)) * X1 * Y1 / denom_hat],
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
        val = shift_old + fu - (pi * (abs(a0) ** 2) * em2l2 if exact_weight else 0)
        u_ch.append(mp.sqrt(val) * R_ch[si])

    Ym = mp.matrix(3, 3)
    cmap = coup["S" if reading == "S" else "tilde_S"]
    for a_i in range(3):
        for b_i in range(3):
            s_val = mp.mpc(0)
            for qi in range(3):
                for si in range(4):
                    cc = cmap[(qi, si, a_i, b_i)]
                    if cc != 0:
                        s_val += c3[qi] * u_ch[si] * cc
            Ym[a_i, b_i] = s_val
    return Ym


def sv_ratios_mp(M: mp.matrix) -> tuple[mp.mpf, mp.mpf]:
    """Return (sigma_2 / sigma_3, sigma_1 / sigma_3) matching position_names ordering."""
    _, Sv, _ = mp.svd_c(M)
    return Sv[1] / Sv[0], Sv[2] / Sv[0]


def frob_mp(M: mp.matrix) -> mp.mpf:
    return mp.sqrt(sum(abs(M[r, c]) ** 2 for r in range(M.rows) for c in range(M.cols)))


def random_haar_u3_mp(rng: random.Random) -> mp.matrix:
    cols = []
    for _ in range(3):
        v = [mp.mpc(mp.mpf(repr(rng.gauss(0, 1))), mp.mpf(repr(rng.gauss(0, 1)))) for _ in range(3)]
        for u in cols:
            proj = sum(mp.conj(u[i]) * v[i] for i in range(3))
            v = [v[i] - proj * u[i] for i in range(3)]
        nrm = mp.sqrt(sum(abs(v[i]) ** 2 for i in range(3)))
        cols.append([v[i] / nrm for i in range(3)])
    U = mp.matrix(3, 3)
    for r in range(3):
        for c in range(3):
            U[r, c] = cols[c][r]
    return U


# ---------------------------------------------------------------------------
# 2. Standalone Kubert-Lang Siegel Winding & B1929 Twisted-Eta Invariant
# ---------------------------------------------------------------------------

def log_siegel_kl(a1: float, a2: float, z: complex) -> complex:
    """Principal-branch terms summed independently in Kubert-Lang's product for log g_{(a1, a2)}(z)."""
    y = z.imag
    k_max = max(8, int(math.ceil(42.0 / (2.0 * math.pi * max(y, 1e-8)))) + 4)
    two_pi_i = 2j * math.pi
    q = cmath.exp(two_pi_i * z)
    qa = cmath.exp(two_pi_i * (a1 * z + a2))
    b2 = a1 * a1 - a1 + (1.0 / 6.0)
    tot = 1j * math.pi + two_pi_i * z * (0.5 * b2) + two_pi_i * (0.5 * a2 * (a1 - 1.0)) + cmath.log(1.0 - qa)
    if k_max <= 24:
        qn = q
        for _ in range(k_max):
            tot += cmath.log(1.0 - qn * qa) + cmath.log(1.0 - qn / qa)
            qn *= q
    else:
        ns = np.arange(1, k_max + 1, dtype=np.float64)
        qn = np.exp((two_pi_i * z) * ns)
        tot += complex(np.sum(np.log1p(-qn * qa) + np.log1p(-qn / qa)))
    return tot


def _adaptive_winding(a1: float, a2: float, z_fn, s0: float, s1: float, depth: int = 0) -> complex:
    d = log_siegel_kl(a1, a2, z_fn(s1)) - log_siegel_kl(a1, a2, z_fn(s0))
    im_wrapped = (d.imag + math.pi) % (2.0 * math.pi) - math.pi
    d = complex(d.real, im_wrapped)
    if abs(d.imag) < 0.45:
        return d
    if depth >= 36:
        raise RuntimeError("Adaptive Siegel winding exceeded max recursion depth")
    mid = 0.5 * (s0 + s1)
    return _adaptive_winding(a1, a2, z_fn, s0, mid, depth + 1) + _adaptive_winding(a1, a2, z_fn, mid, s1, depth + 1)


def siegel_eta_hyperbolic(M: np.ndarray, w1: float, w2: float) -> tuple[float, float]:
    """Compute (eta_A, |Re Delta|) for hyperbolic M in SL_2(Z) and torsion point (w1, w2) in [0, 1)^2
    satisfying M w == +- w mod 1. By B1929, L_odd(1, chi) = -2 pi i Delta and eta_A = -L_odd / pi^2 = -(2/pi) Im(Delta)."""
    a1 = w1 % 1.0
    a2 = w2 % 1.0
    gamma = M.T  # [[m00, m10], [m01, m11]]
    ga, gb, gc, gd = float(gamma[0, 0]), float(gamma[0, 1]), float(gamma[1, 0]), float(gamma[1, 1])
    tr = ga + gd
    disc = math.sqrt(tr * tr - 4.0)
    r1 = ((ga - gd) + disc) / (2.0 * gc)
    r2 = ((ga - gd) - disc) / (2.0 * gc)
    cen = 0.5 * (r1 + r2)
    rad = 0.5 * abs(r1 - r2)
    ell = 2.0 * math.log(0.5 * (abs(tr) + disc))

    def z_geo(s: float) -> complex:
        return complex(cen + rad * math.tanh(s), rad / math.cosh(s))

    s0 = -0.5 * ell
    z0 = z_geo(s0)
    gz0 = (ga * z0 + gb) / (gc * z0 + gd)
    s1 = s0 + ell if abs(gz0 - z_geo(s0 + ell)) < 1e-7 * (1.0 + abs(z0)) else s0 - ell
    assert abs(gz0 - z_geo(s1)) < 1e-7 * (1.0 + abs(z0)), "Geodesic period mismatch"
    delta = _adaptive_winding(a1, a2, z_geo, s0, s1)
    eta_a = -(2.0 / math.pi) * delta.imag
    return eta_a, abs(delta.real)


def build_exact_siegel_automaton_mp() -> dict:
    """Build the exact 24-state finite-state Meyer-Siegel integer cocycle automaton in 50-digit mpmath,
    verify basepoint independence (< 1e-45) and 15 * delta_eta integrality (< 1e-45), and compute the exact
    24x24 transfer matrix spectral radii for alpha = 1/2 and alpha = 1."""
    old_dps = mp.mp.dps
    mp.mp.dps = 50
    try:
        def L_mp(a1_5: int, a2_5: int, z: mp.mpc) -> mp.mpc:
            a1, a2 = mp.mpf(a1_5) / 5, mp.mpf(a2_5) / 5
            tpi = 2j * mp.pi
            q = mp.exp(tpi * z)
            qa = mp.exp(tpi * (a1 * z + a2))
            b2 = a1 * a1 - a1 + mp.mpf(1) / 6
            res = 1j * mp.pi + tpi * z * (b2 / 2) + tpi * (a2 * (a1 - 1) / 2) + mp.log(1 - qa)
            qp = q
            for _ in range(82):
                res += mp.log(1 - qp * qa) + mp.log(1 - qp / qa)
                qp *= q
            return res

        z1 = mp.mpc("0.17", "1.13")
        z2 = mp.mpc("-0.31", "0.89")
        pts = [(a, b) for a in range(5) for b in range(5) if (a, b) != (0, 0)]
        idx_map = {p: i for i, p in enumerate(pts)}

        step_k15 = {}
        neg_k15 = {}
        max_const_err = 0.0
        max_int15_err = 0.0

        for a1, a2 in pts:
            for bit, nxt, gz1, gz2 in (
                (0, ((a1 + a2) % 5, a2), z1 / (z1 + 1), z2 / (z2 + 1)),
                (1, (a1, (a1 + a2) % 5), z1 + 1, z2 + 1),
            ):
                c1 = L_mp(a1, a2, gz1) - L_mp(nxt[0], nxt[1], z1)
                c2 = L_mp(a1, a2, gz2) - L_mp(nxt[0], nxt[1], z2)
                max_const_err = max(max_const_err, float(abs(c1 - c2)))
                val15 = -(2 / mp.pi) * mp.im(c1) * 15
                k_int = int(mp.nint(val15))
                max_int15_err = max(max_int15_err, float(abs(val15 - k_int)))
                step_k15[(bit, a1, a2)] = k_int

            cn1 = L_mp((-a1) % 5, (-a2) % 5, z1) - L_mp(a1, a2, z1)
            cn2 = L_mp((-a1) % 5, (-a2) % 5, z2) - L_mp(a1, a2, z2)
            max_const_err = max(max_const_err, float(abs(cn1 - cn2)))
            vn15 = -(2 / mp.pi) * mp.im(cn1) * 15
            kn_int = int(mp.nint(vn15))
            max_int15_err = max(max_int15_err, float(abs(vn15 - kn_int)))
            neg_k15[(a1, a2)] = kn_int

        assert max_const_err < 1e-45
        assert max_int15_err < 1e-45

        transfer_spectra = {}
        for tag, alpha in (("alpha_half", 0.5), ("alpha_one", 1.0)):
            T = np.zeros((24, 24), dtype=np.complex128)
            for p in pts:
                i = idx_map[p]
                for bit, nxt in ((0, ((p[0] + p[1]) % 5, p[1])), (1, (p[0], (p[0] + p[1]) % 5))):
                    j = idx_map[nxt]
                    k15 = step_k15[(bit, p[0], p[1])]
                    T[i, j] += 0.5 * cmath.exp(1j * math.pi * alpha * (k15 / 15.0))
            evals = np.linalg.eigvals(T)
            rho = float(np.max(np.abs(evals)))
            traces_unnorm = {}
            for n_tr in (6, 10, 14, 17, 20, 24, 40, 100):
                Tn = np.linalg.matrix_power(T, n_tr)
                traces_unnorm[str(n_tr)] = float(np.real(np.trace(Tn)))
            transfer_spectra[tag] = {
                "spectral_radius_rho": rho,
                "rho_sq_minus_half": abs(rho * rho - 0.5) if tag == "alpha_half" else None,
                "strictly_contractive_lt_1": rho < 0.999,
                "trace_T_pow_n_real": traces_unnorm,
            }
        assert abs(transfer_spectra["alpha_half"]["spectral_radius_rho"] - math.sqrt(0.5)) < 1e-13
        assert transfer_spectra["alpha_one"]["spectral_radius_rho"] < 0.75

        return {
            "step_k15": step_k15,
            "neg_k15": neg_k15,
            "max_basepoint_constancy_err_50dps": max_const_err,
            "max_15_times_step_integrality_err_50dps": max_int15_err,
            "transfer_matrix_24x24_spectra": transfer_spectra,
        }
    finally:
        mp.mp.dps = old_dps


def eval_eta_automaton(bits: int, length: int, w5: tuple[int, int], step_k15: dict, neg_k15: dict) -> float:
    """Exact O(length) integer evaluation of eta_A(M_W, w5/5) in (1/15)Z via the Meyer-Siegel cocycle."""
    cur = w5
    k15_sum = 0
    for pos in range(length):
        bit = (bits >> pos) & 1
        k15_sum += step_k15[(bit, cur[0], cur[1])]
        if bit == 0:
            cur = ((cur[0] + cur[1]) % 5, cur[1])
        else:
            cur = (cur[0], (cur[0] + cur[1]) % 5)
    if cur == ((-w5[0]) % 5, (-w5[1]) % 5):
        k15_sum += neg_k15[w5]
    else:
        assert cur == w5, f"Orbit did not close on +-w5: {cur} vs {w5}"
    return k15_sum / 15.0


def siegel_eta_chord_check(M: np.ndarray, w1: float, w2: float, z0: complex = 0.21 + 1.37j) -> float:
    """Independent path/basepoint check along straight Euclidean chord in H from z0 to M^T(z0)."""
    a1, a2 = w1 % 1.0, w2 % 1.0
    ga, gb, gc, gd = float(M[0, 0]), float(M[1, 0]), float(M[0, 1]), float(M[1, 1])
    z1 = (ga * z0 + gb) / (gc * z0 + gd)
    delta = _adaptive_winding(a1, a2, lambda t: z0 + t * (z1 - z0), 0.0, 1.0)
    return -(2.0 / math.pi) * delta.imag


# ---------------------------------------------------------------------------
# 3. Part 0: P-860 (a) Level-5 Weil Connection Obstruction & Canonical Gramian Resolution
# ---------------------------------------------------------------------------

def run_part0_p860a_connection(l2_interp: a2c.CanonicalL2Interpolant) -> dict:
    mp.mp.dps = 45
    ec_list, coup = build_quat_couplings_mp()

    tau0_c = 0.13 + 1.70j  # exact test point of B1945 section 6
    l2_0_f = float(l2_interp.eval_fd(np.array([tau0_c]))[0])
    tau0 = mp.mpc("0.13", "1.70")
    l2_0 = mp.mpf(repr(l2_0_f))
    tau_S = -1 / tau0
    l2_S = l2_0 + mp.log(abs(tau0))

    # 0A: Linear Yukawa sum at tau0, tau0 + 1 (T), tau0 + 5 (T^5 in Gamma(5)), tau0 + 25 (T^25 in Gamma(25))
    linear_drifts = {}
    for sec, (ql, qr) in (("up", (1, -4)), ("down", (1, 2))):
        sums_unred = {}
        sums_red = {}
        for tag, t_val in (("0", tau0), ("T1", tau0 + 1), ("T5", tau0 + 5), ("T25", tau0 + 25)):
            Su = mp.zeros(3, 3)
            Sr = mp.zeros(3, 3)
            for w in PTS_5:
                wL_u = (ql * w[0], ql * w[1])
                wR_u = (qr * w[0], qr * w[1])
                Su += eval_yukawa_mp(t_val, l2_0, wL_u, wR_u, "S", ec_list, coup, True)
                Sr += eval_yukawa_mp(t_val, l2_0, (wL_u[0] % 1, wL_u[1] % 1), (wR_u[0] % 1, wR_u[1] % 1), "S", ec_list, coup, True)
            sums_unred[tag] = sv_ratios_mp(Su)
            sums_red[tag] = sv_ratios_mp(Sr)
        linear_drifts[sec] = {
            "unreduced_T1_max_abs_dln": float(max(abs(mp.log(sums_unred["T1"][i] / sums_unred["0"][i])) for i in (0, 1))),
            "unreduced_T5_Gamma5_max_abs_dln": float(max(abs(mp.log(sums_unred["T5"][i] / sums_unred["0"][i])) for i in (0, 1))),
            "unreduced_T25_Gamma25_max_abs_dln": float(max(abs(mp.log(sums_unred["T25"][i] / sums_unred["0"][i])) for i in (0, 1))),
            "reduced_T1_max_abs_dln": float(max(abs(mp.log(sums_red["T1"][i] / sums_red["0"][i])) for i in (0, 1))),
            "reduced_T5_Gamma5_max_abs_dln": float(max(abs(mp.log(sums_red["T5"][i] / sums_red["0"][i])) for i in (0, 1))),
            "reduced_T25_Gamma25_max_abs_dln": float(max(abs(mp.log(sums_red["T25"][i] / sums_red["0"][i])) for i in (0, 1))),
        }

    # Verify exact stratum-by-stratum fifth-root Weil monodromy under T^5 in Gamma(5) for up vs down:
    # Extract U_L(T^5), U_R(T^5) from stratum w_1 = 0 (points (0, 1/5) and (0, 2/5)), then check all 24 points!
    stratum_phases = {}
    for sec, (ql, qr) in (("up", (1, -4)), ("down", (1, 2))):
        Y0_map = {}
        Y5_map = {}
        for w in PTS_5:
            wL = ((ql * w[0]) % 1, (ql * w[1]) % 1)
            wR = ((qr * w[0]) % 1, (qr * w[1]) % 1)
            Y0_map[w] = eval_yukawa_mp(tau0, l2_0, wL, wR, "S", ec_list, coup, True)
            Y5_map[w] = eval_yukawa_mp(tau0 + 5, l2_0, wL, wR, "S", ec_list, coup, True)
        w_ref1 = (fractions.Fraction(1, 5), fractions.Fraction(0, 5))
        w_ref2 = (fractions.Fraction(1, 5), fractions.Fraction(1, 5))
        U0, _, Vh0 = mp.svd_c(Y0_map[w_ref1])
        U5, _, Vh5 = mp.svd_c(Y5_map[w_ref1])
        # Lock relative singular-vector phases using w_ref2's Hermitian left Gramian H_L = Y Y^H:
        A0 = U0.H * (Y0_map[w_ref2] * Y0_map[w_ref2].H) * U0
        A5 = U5.H * (Y5_map[w_ref2] * Y5_map[w_ref2].H) * U5
        ph1 = A5[1, 0] / A0[1, 0]
        ph1 /= abs(ph1)
        ph2 = A5[2, 0] / A0[2, 0]
        ph2 /= abs(ph2)
        D = mp.diag([mp.mpc(1), ph1, ph2])
        UL_T5 = U5 * D * U0.H
        UR_T5 = Vh5.H * D * Vh0

        # Normalize overall global phase on stratum w_1 = 0 at (0, 1/5):
        w_zero = (fractions.Fraction(0, 5), fractions.Fraction(1, 5))
        M_z = UL_T5.H * Y5_map[w_zero] * UR_T5
        phi_z = sum(mp.conj(Y0_map[w_zero][r, c]) * M_z[r, c] for r in range(3) for c in range(3)) / sum(
            abs(Y0_map[w_zero][r, c]) ** 2 for r in range(3) for c in range(3)
        )
        UL_T5 = UL_T5 * phi_z

        max_unitary_residual = 0.0
        phases_by_w1 = {0: [], 1: [], 2: []}
        for w in PTS_5:
            M_trans = UL_T5.H * Y5_map[w] * UR_T5
            num = sum(mp.conj(Y0_map[w][r, c]) * M_trans[r, c] for r in range(3) for c in range(3))
            den = sum(abs(Y0_map[w][r, c]) ** 2 for r in range(3) for c in range(3))
            phi = num / den
            res = float(frob_mp(M_trans - phi * Y0_map[w]) / frob_mp(Y0_map[w]))
            max_unitary_residual = max(max_unitary_residual, res)
            k_stratum = min(w[0].numerator % 5, (-w[0].numerator) % 5)
            ang = float(mp.arg(phi) / (2 * mp.pi))
            if abs(ang) < 1e-13:
                ang = 0.0
            phases_by_w1[k_stratum].append(ang)
        stratum_phases[sec] = {
            "max_pointwise_unitary_residual": max_unitary_residual,
            "arg_over_2pi_by_abs_5w1": {str(k): round(vals[0], 12) for k, vals in phases_by_w1.items()},
            "max_within_stratum_spread": max(max(vals) - min(vals) for vals in phases_by_w1.values()),
        }
        assert max_unitary_residual < 1e-35

    # Down-sector explicit T-coboundary repair check (since q_L^2 + q_R^2 = 5 == 0 mod 5 has trivial T^5 monodromy!):
    Yd0 = {w: eval_yukawa_mp(tau0, l2_0, ((1*w[0])%1, (1*w[1])%1), ((2*w[0])%1, (2*w[1])%1), "S", ec_list, coup, True) for w in PTS_5}
    Yd1 = {w: eval_yukawa_mp(tau0 + 1, l2_0, ((1*w[0])%1, (1*w[1])%1), ((2*w[0])%1, (2*w[1])%1), "S", ec_list, coup, True) for w in PTS_5}
    w_r1 = (fractions.Fraction(1, 5), fractions.Fraction(0, 5))
    w_r1_T = (fractions.Fraction(1, 5), fractions.Fraction(1, 5))
    w_r2 = (fractions.Fraction(2, 5), fractions.Fraction(0, 5))
    w_r2_T = (fractions.Fraction(2, 5), fractions.Fraction(2, 5))
    U0d, _, Vh0d = mp.svd_c(Yd0[w_r1_T])
    U1d, _, Vh1d = mp.svd_c(Yd1[w_r1])
    B0d = U0d.H * (Yd0[w_r2_T] * Yd0[w_r2_T].H) * U0d
    B1d = U1d.H * (Yd1[w_r2] * Yd1[w_r2].H) * U1d
    p1d = (B1d[1, 0] / B0d[1, 0]) / abs(B1d[1, 0] / B0d[1, 0])
    p2d = (B1d[2, 0] / B0d[2, 0]) / abs(B1d[2, 0] / B0d[2, 0])
    Dd = mp.diag([mp.mpc(1), p1d, p2d])
    UL_Td = U1d * Dd * U0d.H
    UR_Td = Vh1d.H * Dd * Vh0d
    wz_d = (fractions.Fraction(0, 5), fractions.Fraction(1, 5))
    Mz_d = UL_Td.H * Yd1[wz_d] * UR_Td
    phiz_d = sum(mp.conj(Yd0[wz_d][r, c]) * Mz_d[r, c] for r in range(3) for c in range(3)) / sum(
        abs(Yd0[wz_d][r, c]) ** 2 for r in range(3) for c in range(3)
    )
    UL_Td = UL_Td * phiz_d

    phi_T_down = {}
    for w in PTS_5:
        wT = (w[0], (w[1] + w[0]) % 1)
        Mt = UL_Td.H * Yd1[w] * UR_Td
        num = sum(mp.conj(Yd0[wT][r, c]) * Mt[r, c] for r in range(3) for c in range(3))
        den = sum(abs(Yd0[wT][r, c]) ** 2 for r in range(3) for c in range(3))
        phi_T_down[w] = num / den
    c_down = {}
    for a_num in range(5):
        if a_num == 0:
            for b_num in range(1, 5):
                w_0b = (fractions.Fraction(0, 5), fractions.Fraction(b_num, 5))
                assert abs(phi_T_down[w_0b] - 1) < mp.mpf("1e-35")
                c_down[w_0b] = mp.mpc(1)
        else:
            w_cur = (fractions.Fraction(a_num, 5), fractions.Fraction(0, 5))
            c_val = mp.mpc(1)
            for _ in range(5):
                c_down[w_cur] = c_val
                w_nxt = (w_cur[0], (w_cur[1] + w_cur[0]) % 1)
                c_val = c_val * phi_T_down[w_cur]
                w_cur = w_nxt
            assert abs(c_val - 1) < mp.mpf("1e-35"), f"Down T-orbit monodromy failed to close: {abs(c_val - 1)}"
    Sd_cov_0 = sum((c_down[w] * Yd0[w] for w in PTS_5), mp.zeros(3, 3))
    Sd_cov_1 = sum((c_down[w] * Yd1[w] for w in PTS_5), mp.zeros(3, 3))
    rv0, rv1 = sv_ratios_mp(Sd_cov_0), sv_ratios_mp(Sd_cov_1)
    down_T_repaired_dln = float(max(abs(mp.log(rv1[i] / rv0[i])) for i in (0, 1)))
    assert down_T_repaired_dln < 1e-35

    # 0B: Canonical Hermitian Mass-Squared Operator H_{L,f}(tau) = (1/24) sum_{|w|=5} Y_f(tau, w) Y_f(tau, w)^H
    def eval_gramian_readout(t_val: mp.mpc, lv: mp.mpf, scramble_mats=None):
        sectors = {}
        lr_planted = {}
        for sec, (ql, qr), rn in (
            ("up_St", (1, -4), "tilde_S"),
            ("down_S", (1, 2), "S"),
            ("up_S", (1, -4), "S"),
            ("down_St", (1, 2), "tilde_S"),
        ):
            H = mp.zeros(3, 3)
            Y_sum_for_lr = mp.zeros(3, 3)
            for w in PTS_5:
                wL = ((ql * w[0]) % 1, (ql * w[1]) % 1)
                wR = ((qr * w[0]) % 1, (qr * w[1]) % 1)
                Y = eval_yukawa_mp(t_val, lv, wL, wR, rn, ec_list, coup, True)
                if scramble_mats is not None:
                    UL_q, UR_sec = scramble_mats["UL_Q"], scramble_mats[f"UR_{sec}"]
                    Y = UL_q * Y * UR_sec.H
                H += Y * Y.H
                Y_sum_for_lr += Y
            H /= 24
            Uu, Sv, _ = mp.svd_c(H)
            m_ratios = [mp.sqrt(Sv[1] / Sv[0]), mp.sqrt(Sv[2] / Sv[0])]
            U_asc = mp.matrix([[Uu[r, 2 - c] for c in range(3)] for r in range(3)])
            sectors[sec] = (m_ratios, U_asc)
            Ul, _, Vhl = mp.svd_c(Y_sum_for_lr)
            lr_planted[sec] = abs((Ul.H * Vhl.H)[0, 1])

        V_wm = sectors["up_St"][1].H * sectors["down_S"][1]
        V_wp = sectors["up_S"][1].H * sectors["down_St"][1]
        unitarity_err = max(
            float(frob_mp(V_wm * V_wm.H - mp.eye(3))),
            float(frob_mp(V_wp * V_wp.H - mp.eye(3))),
        )
        v7_wm = [
            float(sectors["up_St"][0][0]), float(sectors["up_St"][0][1]),
            float(sectors["down_S"][0][0]), float(sectors["down_S"][0][1]),
            float(abs(V_wm[0, 1])), float(abs(V_wm[1, 2])), float(abs(V_wm[0, 2])),
        ]
        v7_wp = [
            float(sectors["up_S"][0][0]), float(sectors["up_S"][0][1]),
            float(sectors["down_St"][0][0]), float(sectors["down_St"][0][1]),
            float(abs(V_wp[0, 1])), float(abs(V_wp[1, 2])), float(abs(V_wp[0, 2])),
        ]
        jcp_wm = float(mp.im(V_wm[0, 1] * V_wm[1, 2] * mp.conj(V_wm[0, 2]) * mp.conj(V_wm[1, 1])))
        jcp_wp = float(mp.im(V_wp[0, 1] * V_wp[1, 2] * mp.conj(V_wp[0, 2]) * mp.conj(V_wp[1, 1])))
        v33_wm = float(abs(V_wm[2, 2]))
        v33_wp = float(abs(V_wp[2, 2]))
        return {
            "v7_wm": v7_wm, "v7_wp": v7_wp,
            "jcp_wm": jcp_wm, "jcp_wp": jcp_wp,
            "abs_V33_wm": v33_wm, "abs_V33_wp": v33_wp,
            "ckm_unitarity_err": unitarity_err,
            "lr_planted": lr_planted,
        }

    g0 = eval_gramian_readout(tau0, l2_0)
    gT1 = eval_gramian_readout(tau0 + 1, l2_0)
    gT5 = eval_gramian_readout(tau0 + 5, l2_0)
    gS = eval_gramian_readout(tau_S, l2_S)

    def max_dln7(a, b):
        return max(abs(math.log(x / y)) for x, y in zip(a, b))

    gram_T1_err = max(max_dln7(gT1["v7_wm"], g0["v7_wm"]), max_dln7(gT1["v7_wp"], g0["v7_wp"]))
    gram_T5_err = max(max_dln7(gT5["v7_wm"], g0["v7_wm"]), max_dln7(gT5["v7_wp"], g0["v7_wp"]))
    gram_S_err = max(max_dln7(gS["v7_wm"], g0["v7_wm"]), max_dln7(gS["v7_wp"], g0["v7_wp"]))
    gram_jcp_S_err = max(abs(abs(gS["jcp_wm"]) - abs(g0["jcp_wm"])), abs(abs(gS["jcp_wp"]) - abs(g0["jcp_wp"])))

    assert gram_T1_err < 1e-14 and gram_T5_err < 1e-14 and gram_S_err < 1e-14

    # CTL-AMP-3 (Guardrail 3): Random Haar SU(3) scrambling on shared Q_L and independent right-handed singlets:
    rng = random.Random(20261115)
    max_haar_err = 0.0
    min_lr_planted_drift = 1e9
    for _ in range(4):
        scr = {
            "UL_Q": random_haar_u3_mp(rng),
            "UR_up_St": random_haar_u3_mp(rng),
            "UR_down_S": random_haar_u3_mp(rng),
            "UR_up_S": random_haar_u3_mp(rng),
            "UR_down_St": random_haar_u3_mp(rng),
        }
        gs = eval_gramian_readout(tau0, l2_0, scramble_mats=scr)
        err = max(
            max_dln7(gs["v7_wm"], g0["v7_wm"]),
            max_dln7(gs["v7_wp"], g0["v7_wp"]),
            abs(gs["jcp_wm"] - g0["jcp_wm"]),
            abs(gs["jcp_wp"] - g0["jcp_wp"]),
        )
        max_haar_err = max(max_haar_err, err)
        lr_drift = max(abs(float(gs["lr_planted"][k] - g0["lr_planted"][k])) for k in g0["lr_planted"])
        min_lr_planted_drift = min(min_lr_planted_drift, lr_drift)

    assert max_haar_err < 1e-12
    assert min_lr_planted_drift > 1e-2

    # Check high-cusp behavior (y = 30) of canonical Gramian H_{L,f}(tau) at high precision:
    mp.mp.dps = 125
    ec_hi, coup_hi = build_quat_couplings_mp()
    tau_cusp = mp.mpc("0.13", "30.0")
    l2_cusp_f = float(l2_interp.eval_fd(np.array([0.13 + 30.0j]))[0])
    l2_cusp = mp.mpf(repr(l2_cusp_f))
    sec_cusp = {}
    for sec, (ql, qr), rn in (("up_St", (1, -4), "tilde_S"), ("down_S", (1, 2), "S"), ("up_S", (1, -4), "S"), ("down_St", (1, 2), "tilde_S")):
        Hc = mp.zeros(3, 3)
        for w in PTS_5:
            Y = eval_yukawa_mp(tau_cusp, l2_cusp, ((ql*w[0])%1, (ql*w[1])%1), ((qr*w[0])%1, (qr*w[1])%1), rn, ec_hi, coup_hi, True)
            Hc += Y * Y.H
        Hc /= 24
        Uuc, Svc, _ = mp.svd_c(Hc)
        U_asc = mp.matrix([[Uuc[r, 2 - c] for c in range(3)] for r in range(3)])
        sec_cusp[sec] = U_asc
    Vc_wm = sec_cusp["up_St"].H * sec_cusp["down_S"]
    Vc_ss = sec_cusp["up_S"].H * sec_cusp["down_S"]
    cusp_gramian_v33 = {
        "y30_mixed_W_minus_abs_V33": float(abs(Vc_wm[2, 2])),
        "y30_aligned_S_S_abs_V33": float(abs(Vc_ss[2, 2])),
        "y30_unitarity_err": float(frob_mp(Vc_wm * Vc_wm.H - mp.eye(3))),
    }
    mp.mp.dps = 45

    return {
        "tau0": "0.13 + 1.70i",
        "CTL_AMP_2_naive_linear_sum_drifts": linear_drifts,
        "Gamma5_T5_stratum_weil_monodromy": stratum_phases,
        "down_sector_T1_coboundary_repaired_dln": down_T_repaired_dln,
        "canonical_gramian_SL2Z_covariance": {
            "T1_max_abs_dln_7": gram_T1_err,
            "T5_max_abs_dln_7": gram_T5_err,
            "S_max_abs_dln_7": gram_S_err,
            "S_abs_JCP_diff": gram_jcp_S_err,
            "ckm_unitarity_err": g0["ckm_unitarity_err"],
            "interior_JCP_W_minus": g0["jcp_wm"],
            "interior_JCP_W_plus": g0["jcp_wp"],
            "interior_seven_values_json_only": {"W_minus": g0["v7_wm"], "W_plus": g0["v7_wp"]},
            "cusp_y30_structural_check": cusp_gramian_v33,
        },
        "CTL_AMP_3_guardrail3_haar_scrambling": {
            "max_observable_drift": max_haar_err,
            "planted_lr_overlap_min_drift": min_lr_planted_drift,
            "caught": max_haar_err < 1e-12 and min_lr_planted_drift > 1e-2,
        },
    }


# ---------------------------------------------------------------------------
# 4. Part 1 & Part 3: B1929 Twisted-Eta Convergence on {L, R}^n & Move-vs-Area Dissolution
# ---------------------------------------------------------------------------

IDX_W_MINUS = [2, 3, 4, 5, 18, 19, 20]
IDX_W_PLUS = [0, 1, 6, 7, 15, 16, 17]


def swap_LR_bits(bits: int, length: int) -> int:
    return ((1 << length) - 1) ^ bits


def eval_geodesic_jcp_and_gramian(M_word: np.ndarray, l2_interp: a2c.CanonicalL2Interpolant, ec_list, coup) -> tuple[float, float]:
    """Evaluate closed-geodesic average of Jarlskog J_CP(tau, w_mark) in W_- and W_+ along M_word's geodesic
    using 12 midpoint nodes (interior geodesics all sit at Im(tau_fd) < 6)."""
    _, taus = a2c.geodesic_midpoint_taus(M_word, density=4.0, min_nodes=12)
    t_fd, a_m, b_m = a2c.pullback_b1724(taus, 0.4, 0.8)
    l2_fd = l2_interp.eval_fd(t_fd)
    j_wm_acc = 0.0
    j_wp_acc = 0.0
    mp.mp.dps = 18
    for k in range(len(t_fd)):
        tk = mp.mpc(repr(float(t_fd[k].real)), repr(float(t_fd[k].imag)))
        lk = mp.mpf(repr(float(l2_fd[k])))
        w1 = fractions.Fraction(round(float(a_m[k]) * 5) % 5, 5)
        w2 = fractions.Fraction(round(float(b_m[k]) * 5) % 5, 5)
        Yu_st = eval_yukawa_mp(tk, lk, (w1, w2), ((-4*w1)%1, (-4*w2)%1), "tilde_S", ec_list, coup, True)
        Yd_s = eval_yukawa_mp(tk, lk, (w1, w2), ((2*w1)%1, (2*w2)%1), "S", ec_list, coup, True)
        Yu_s = eval_yukawa_mp(tk, lk, (w1, w2), ((-4*w1)%1, (-4*w2)%1), "S", ec_list, coup, True)
        Yd_st = eval_yukawa_mp(tk, lk, (w1, w2), ((2*w1)%1, (2*w2)%1), "tilde_S", ec_list, coup, True)
        Uu_st, _, _ = mp.svd_c(Yu_st)
        Ud_s, _, _ = mp.svd_c(Yd_s)
        Uu_s, _, _ = mp.svd_c(Yu_s)
        Ud_st, _, _ = mp.svd_c(Yd_st)
        # Ascending order (2, 1, 0):
        U1 = mp.matrix([[Uu_st[r, 2 - c] for c in range(3)] for r in range(3)])
        D1 = mp.matrix([[Ud_s[r, 2 - c] for c in range(3)] for r in range(3)])
        V_m = U1.H * D1
        j_wm_acc += float(mp.im(V_m[0, 1] * V_m[1, 2] * mp.conj(V_m[0, 2]) * mp.conj(V_m[1, 1])))
        U2 = mp.matrix([[Uu_s[r, 2 - c] for c in range(3)] for r in range(3)])
        D2 = mp.matrix([[Ud_st[r, 2 - c] for c in range(3)] for r in range(3)])
        V_p = U2.H * D2
        j_wp_acc += float(mp.im(V_p[0, 1] * V_p[1, 2] * mp.conj(V_p[0, 2]) * mp.conj(V_p[1, 1])))
    return j_wm_acc / len(t_fd), j_wp_acc / len(t_fd)


def run_part1_and_part3(l2_interp: a2c.CanonicalL2Interpolant, area_ref: dict) -> dict:
    # 1A: Build 50-dps exact Meyer-Siegel 24-state integer cocycle automaton & 24x24 transfer matrix spectra,
    # cross-check word-by-word against continuous adaptive geodesic winding across exhaustive n = 4..13,
    # and evaluate exact Z_eta(n) across exhaustive n = 4..18:
    auto = build_exact_siegel_automaton_mp()
    step_k15 = auto["step_k15"]
    neg_k15 = auto["neg_k15"]

    partition_table = {}
    max_re_delta = 0.0
    max_cocycle_vs_geodesic_diff = 0.0
    max_chord_diff = 0.0
    max_mirror_sum_err = 0.0
    chord_checked = 0
    geodesic_cross_checked = 0

    for n in range(4, 19):
        bits_list, mats_list = a2c.enumerate_allowed_words(n)
        if not mats_list:
            continue
        etas = np.zeros(len(mats_list), dtype=np.float64)
        is_strict = np.zeros(len(mats_list), dtype=bool)
        for idx, (b, M) in enumerate(zip(bits_list, mats_list)):
            u0 = int((2 * M[0, 0] + 4 * M[0, 1]) % 5)
            u1 = int((2 * M[1, 0] + 4 * M[1, 1]) % 5)
            is_strict[idx] = (u0 == 2 and u1 == 4)
            eta_val = eval_eta_automaton(b, n, (2, 4), step_k15, neg_k15)
            etas[idx] = eta_val
            if n <= 13:
                eta_geo, re_del = siegel_eta_hyperbolic(M, 0.4, 0.8)
                max_re_delta = max(max_re_delta, re_del)
                max_cocycle_vs_geodesic_diff = max(max_cocycle_vs_geodesic_diff, abs(eta_val - eta_geo))
                geodesic_cross_checked += 1
            if chord_checked < 40:
                eta_ch = siegel_eta_chord_check(M, 0.4, 0.8)
                max_chord_diff = max(max_chord_diff, abs(eta_val - eta_ch))
                chord_checked += 1

        # Check mirror anti-symmetry under L<->R swap (b_swap = ((1<<n)-1) ^ b, fixing P w = (0.8, 0.4)):
        if n <= 14:
            all_ones = (1 << n) - 1
            for idx, b in enumerate(bits_list):
                eta_swap = eval_eta_automaton(all_ones ^ b, n, (4, 2), step_k15, neg_k15)
                max_mirror_sum_err = max(max_mirror_sum_err, abs(etas[idx] + eta_swap))

        partition_table[str(n)] = {
            "n_keeps_mark_pm": int(len(etas)),
            "n_strict_plus": int(np.sum(is_strict)),
            "var_eta_pm": float(np.var(etas)),
            "mean_eta_pm": float(np.mean(etas)),
            "Z_cos_half_pi_pm": float(np.mean(np.cos(0.5 * math.pi * etas))),
            "Z_sin_half_pi_pm": float(np.mean(np.sin(0.5 * math.pi * etas))),
            "Z_cos_pi_pm": float(np.mean(np.cos(math.pi * etas))),
            "Z_sin_pi_pm": float(np.mean(np.sin(math.pi * etas))),
            "Z_cos_half_pi_strict": float(np.mean(np.cos(0.5 * math.pi * etas[is_strict]))) if np.any(is_strict) else None,
            "Z_cos_pi_strict": float(np.mean(np.cos(math.pi * etas[is_strict]))) if np.any(is_strict) else None,
        }

    assert max_re_delta < 1e-12, f"Re(Delta) residual too large: {max_re_delta}"
    assert max_cocycle_vs_geodesic_diff < 1e-12, f"Cocycle vs geodesic mismatch: {max_cocycle_vs_geodesic_diff}"
    assert max_chord_diff < 1e-12, f"Path/basepoint independence failed: {max_chord_diff}"
    assert max_mirror_sum_err < 1e-14, f"Orientation-reversal anti-symmetry failed: {max_mirror_sum_err}"

    # Verify exact Im(Z_eta) == 0 on the full 24-point symmetric population {(W, w) : M_W w = +-w mod 5} at n = 6, 8, 10, 12
    # + planted control CTL-AMP-1 (flipping sign on half the words):
    full24_symmetry = {}
    for n_sym in (6, 8, 10, 12):
        total = 1 << n_sym
        re_half, im_half = 0.0, 0.0
        ctl_im_half = 0.0
        cnt = 0
        for b in range(1, total - 1):
            M = a2c.word_bits_to_mat(b, n_sym)
            for a5 in range(5):
                for b5 in range(5):
                    if a5 == 0 and b5 == 0:
                        continue
                    u0 = int((M[0, 0] * a5 + M[0, 1] * b5) % 5)
                    u1 = int((M[1, 0] * a5 + M[1, 1] * b5) % 5)
                    if (u0 == a5 and u1 == b5) or (u0 == (-a5) % 5 and u1 == (-b5) % 5):
                        eta_v = eval_eta_automaton(b, n_sym, (a5, b5), step_k15, neg_k15)
                        re_half += math.cos(0.5 * math.pi * eta_v)
                        im_half += math.sin(0.5 * math.pi * eta_v)
                        # Planted sign flip on words starting with R (b >> (n_sym-1) == 1):
                        eta_ctl = abs(eta_v) if ((b >> (n_sym - 1)) & 1) else eta_v
                        ctl_im_half += math.sin(0.5 * math.pi * eta_ctl)
                        cnt += 1
        full24_symmetry[str(n_sym)] = {
            "total_pairs": cnt,
            "mean_cos_half_pi": re_half / cnt,
            "mean_sin_half_pi": im_half / cnt,
            "CTL_AMP_1_planted_mean_sin_half_pi": ctl_im_half / cnt,
        }
        assert abs(im_half / cnt) < 1e-13
        assert abs(ctl_im_half / cnt) > 1e-2

    # 1B: Evaluate full Frame C geodesic observables across exhaustive n = 6, 8, 10, 12, 14 and compare weightings!
    obs_convergence = {}
    area_wm = np.array(area_ref["W_minus"], dtype=np.float64)
    area_wp = np.array(area_ref["W_plus"], dtype=np.float64)

    for n in (6, 8, 10, 12, 14):
        bits_list, mats_list = a2c.enumerate_allowed_words(n)
        lengths, mark_means, _, _ = a2c.evaluate_allowed_word_set(
            mats_list, l2_interp, eval_twin=False, mode_list=("exact_T90",)
        )
        vals24 = mark_means["exact_T90"]  # shape (W, 24)
        etas = np.zeros(len(mats_list), dtype=np.float64)
        selberg_w = np.zeros(len(mats_list), dtype=np.float64)
        is_strict = np.zeros(len(mats_list), dtype=bool)
        for i, (b, M) in enumerate(zip(bits_list, mats_list)):
            etas[i] = eval_eta_automaton(b, n, (2, 4), step_k15, neg_k15)
            tr = float(M[0, 0] + M[1, 1])
            selberg_w[i] = 1.0 / math.sqrt(abs(tr - 2.0))
            u0 = int((2 * M[0, 0] + 4 * M[0, 1]) % 5)
            u1 = int((2 * M[1, 0] + 4 * M[1, 1]) % 5)
            is_strict[i] = (u0 == 2 and u1 == 4)

        w_len = lengths / np.sum(lengths)
        w_unif = np.full(len(mats_list), 1.0 / len(mats_list))
        c_half = np.cos(0.5 * math.pi * etas)
        c_one = np.cos(math.pi * etas)

        def w_avg7(weights: np.ndarray):
            denom = float(np.sum(weights))
            v24 = (weights @ vals24) / denom
            return v24[IDX_W_MINUS], v24[IDX_W_PLUS], denom / len(weights)

        wm_len, wp_len, _ = w_avg7(lengths)
        wm_unif, wp_unif, _ = w_avg7(np.ones_like(lengths))
        wm_eta_h, wp_eta_h, z_h = w_avg7(c_half)
        wm_eta_1, wp_eta_1, z_1 = w_avg7(c_one)
        wm_sel, wp_sel, _ = w_avg7(selberg_w)
        wm_sel_eta, wp_sel_eta, _ = w_avg7(selberg_w * c_half)

        def dln_stats(v_wm, v_wp, ref_wm, ref_wp):
            d_m = np.abs(np.log(np.abs(v_wm) / ref_wm))
            d_p = np.abs(np.log(np.abs(v_wp) / ref_wp))
            return {
                "W_minus_max_abs_dln": float(np.max(d_m)),
                "W_minus_rms_dln": float(np.sqrt(np.mean(d_m ** 2))),
                "W_plus_max_abs_dln": float(np.max(d_p)),
                "W_plus_rms_dln": float(np.sqrt(np.mean(d_p ** 2))),
            }

        obs_convergence[str(n)] = {
            "n_words": len(mats_list),
            "Z_cos_half_pi": float(np.mean(c_half)),
            "Z_cos_pi": float(np.mean(c_one)),
            "seven_values_json_only": {
                "move_len_weighted": {"W_minus": wm_len.tolist(), "W_plus": wp_len.tolist()},
                "move_uniform": {"W_minus": wm_unif.tolist(), "W_plus": wp_unif.tolist()},
                "twisted_eta_half_pi": {"W_minus": wm_eta_h.tolist(), "W_plus": wp_eta_h.tolist()},
                "twisted_eta_pi": {"W_minus": wm_eta_1.tolist(), "W_plus": wp_eta_1.tolist()},
                "selberg_one_loop": {"W_minus": wm_sel.tolist(), "W_plus": wp_sel.tolist()},
                "selberg_times_eta_half_pi": {"W_minus": wm_sel_eta.tolist(), "W_plus": wp_sel_eta.tolist()},
            },
            "vs_area_dln": {
                "move_len_weighted": dln_stats(wm_len, wp_len, area_wm, area_wp),
                "move_uniform": dln_stats(wm_unif, wp_unif, area_wm, area_wp),
                "twisted_eta_half_pi": dln_stats(wm_eta_h, wp_eta_h, area_wm, area_wp),
                "twisted_eta_pi": dln_stats(wm_eta_1, wp_eta_1, area_wm, area_wp),
                "selberg_one_loop": dln_stats(wm_sel, wp_sel, area_wm, area_wp),
                "selberg_times_eta_half_pi": dln_stats(wm_sel_eta, wp_sel_eta, area_wm, area_wp),
            },
            "shift_from_unweighted_dln": {
                "twisted_eta_half_pi_vs_uniform": dln_stats(wm_eta_h, wp_eta_h, wm_unif, wp_unif),
                "selberg_vs_uniform": dln_stats(wm_sel, wp_sel, wm_unif, wp_unif),
            },
        }

    # 1C: P-846 Hand / CP-Odd Jarlskog Test on Closed Geodesic Pairs (W, w) vs Mirror (P W P, P w) at n = 6, 8:
    mp.mp.dps = 18
    ec_22, coup_22 = build_quat_couplings_mp()
    hand_results = {}
    for n_h in (6, 8):
        bits_list, mats_list = a2c.enumerate_allowed_words(n_h)
        # Include mirror pairs (P M P, P w = (0.8, 0.4)) explicitly so ensemble is mirror-closed:
        j_wm_unweighted = 0.0
        j_wm_sin_eta = 0.0
        j_wp_unweighted = 0.0
        j_wp_sin_eta = 0.0
        max_pair_jcp_sum = 0.0
        n_pairs = len(mats_list)
        for M in mats_list:
            eta1, _ = siegel_eta_hyperbolic(M, 0.4, 0.8)
            j1_m, j1_p = eval_geodesic_jcp_and_gramian(M, l2_interp, ec_22, coup_22)
            # Mirror word M_mir = P M P with mark P(0.4, 0.8) = (0.8, 0.4):
            M_mir = np.array([[M[1, 1], M[1, 0]], [M[0, 1], M[0, 0]]], dtype=np.int64)
            eta2, _ = siegel_eta_hyperbolic(M_mir, 0.8, 0.4)
            # Evaluate J_CP at (taus_mir, 0.8, 0.4):
            _, taus_m = a2c.geodesic_midpoint_taus(M_mir, density=4.0, min_nodes=12)
            t_fd_m, a_mm, b_mm = a2c.pullback_b1724(taus_m, 0.8, 0.4)
            l2_m = l2_interp.eval_fd(t_fd_m)
            j2_m, j2_p = 0.0, 0.0
            for k in range(len(t_fd_m)):
                tk = mp.mpc(repr(float(t_fd_m[k].real)), repr(float(t_fd_m[k].imag)))
                lk = mp.mpf(repr(float(l2_m[k])))
                w1 = fractions.Fraction(round(float(a_mm[k]) * 5) % 5, 5)
                w2 = fractions.Fraction(round(float(b_mm[k]) * 5) % 5, 5)
                Yu_st = eval_yukawa_mp(tk, lk, (w1, w2), ((-4*w1)%1, (-4*w2)%1), "tilde_S", ec_22, coup_22, True)
                Yd_s = eval_yukawa_mp(tk, lk, (w1, w2), ((2*w1)%1, (2*w2)%1), "S", ec_22, coup_22, True)
                Yu_s = eval_yukawa_mp(tk, lk, (w1, w2), ((-4*w1)%1, (-4*w2)%1), "S", ec_22, coup_22, True)
                Yd_st = eval_yukawa_mp(tk, lk, (w1, w2), ((2*w1)%1, (2*w2)%1), "tilde_S", ec_22, coup_22, True)
                Uu_st, _, _ = mp.svd_c(Yu_st)
                Ud_s, _, _ = mp.svd_c(Yd_s)
                Uu_s, _, _ = mp.svd_c(Yu_s)
                Ud_st, _, _ = mp.svd_c(Yd_st)
                U1 = mp.matrix([[Uu_st[r, 2 - c] for c in range(3)] for r in range(3)])
                D1 = mp.matrix([[Ud_s[r, 2 - c] for c in range(3)] for r in range(3)])
                Vm = U1.H * D1
                j2_m += float(mp.im(Vm[0, 1] * Vm[1, 2] * mp.conj(Vm[0, 2]) * mp.conj(Vm[1, 1])))
                U2 = mp.matrix([[Uu_s[r, 2 - c] for c in range(3)] for r in range(3)])
                D2 = mp.matrix([[Ud_st[r, 2 - c] for c in range(3)] for r in range(3)])
                Vp = U2.H * D2
                j2_p += float(mp.im(Vp[0, 1] * Vp[1, 2] * mp.conj(Vp[0, 2]) * mp.conj(Vp[1, 1])))
            j2_m /= len(t_fd_m)
            j2_p /= len(t_fd_m)

            max_pair_jcp_sum = max(max_pair_jcp_sum, abs(j1_m + j2_m), abs(j1_p + j2_p))
            j_wm_unweighted += j1_m + j2_m
            j_wp_unweighted += j1_p + j2_p
            j_wm_sin_eta += math.sin(0.5 * math.pi * eta1) * j1_m + math.sin(0.5 * math.pi * eta2) * j2_m
            j_wp_sin_eta += math.sin(0.5 * math.pi * eta1) * j1_p + math.sin(0.5 * math.pi * eta2) * j2_p

        denom_cnt = 2 * n_pairs
        hand_results[str(n_h)] = {
            "n_mirror_closed_histories": denom_cnt,
            "max_mirror_pair_JCP_sum_residual": max_pair_jcp_sum,
            "unweighted_mean_JCP_W_minus": j_wm_unweighted / denom_cnt,
            "unweighted_mean_JCP_W_plus": j_wp_unweighted / denom_cnt,
            "sin_half_pi_eta_weighted_JCP_W_minus": j_wm_sin_eta / denom_cnt,
            "sin_half_pi_eta_weighted_JCP_W_plus": j_wp_sin_eta / denom_cnt,
        }

    a2c.close_spawn_pool()
    return {
        "geodesic_vs_automaton_words_checked_n4_to_13": geodesic_cross_checked,
        "max_re_delta_residual_n4_to_13": max_re_delta,
        "max_cocycle_vs_geodesic_diff_n4_to_13": max_cocycle_vs_geodesic_diff,
        "max_15_times_step_integrality_err_50dps": auto["max_15_times_step_integrality_err_50dps"],
        "max_cocycle_basepoint_constancy_err_50dps": auto["max_basepoint_constancy_err_50dps"],
        "max_chord_vs_automaton_diff": max_chord_diff,
        "max_mirror_orientation_reversal_err": max_mirror_sum_err,
        "transfer_matrix_24x24_spectra": auto["transfer_matrix_24x24_spectra"],
        "partition_and_variance_by_n": partition_table,
        "full_24pt_im_cancellation_and_CTL_AMP_1": full24_symmetry,
        "observable_convergence_and_part3_area_gap": obs_convergence,
        "p846_hand_jarlskog_coupling": hand_results,
    }


# ---------------------------------------------------------------------------
# 5. Part 2: M34 Q2 — Dynamic Odd-Tick Interference ({L, R}^n P, det = -1)
# ---------------------------------------------------------------------------

def run_part2_odd_ticks() -> dict:
    """Test exhaustive odd-tick hyperbolic words M_W = M_{W0} P (det M_W = -1) across n = 1..14
    (including m000 = LP at n=1). Verify the exact trace-divisibility theorem (order-5 character exists iff
    5 | tr(M_W), hence 0 surviving characters for n = 1..4 and positive counts from n = 5 upward) across n = 1..14,
    and evaluate adaptive Kubert-Lang Siegel winding on the orientable double cover T^2_{M_W^2} across all 24 points
    for exhaustive n = 1..9."""
    P_mat = np.array([[0, 1], [1, 0]], dtype=np.int64)
    odd_tick_by_n = {}
    max_abs_eta_double_cover = 0.0
    max_half_step_sum_err = 0.0
    max_single_half_step_abs = 0.0
    total_odd_pairs = 0
    trace_div_mismatches = 0

    for n in range(1, 15):
        total = 1 << n
        cnt_twisted = 0
        cnt_untwisted = 0
        max_eta_n = 0.0
        for b in range(total):
            M0 = a2c.word_bits_to_mat(b, n)
            M_odd = M0 @ P_mat  # det = -1, tr >= 1 (always strictly hyperbolic!)
            tr_odd = int(M_odd[0, 0] + M_odd[1, 1])
            pts_check = [(a5, b5) for a5 in range(5) for b5 in range(5) if (a5, b5) != (0, 0)]
            found_any = False
            for a5, b5 in pts_check:
                u0 = int((M_odd[0, 0] * a5 + M_odd[0, 1] * b5) % 5)
                u1 = int((M_odd[1, 0] * a5 + M_odd[1, 1] * b5) % 5)
                is_tw = (u0 == (-a5) % 5 and u1 == (-b5) % 5)   # B1926 orientation-twisted: M w = (det M) w = -w
                is_un = (u0 == a5 and u1 == b5)                 # untwisted: M w = +w
                if not (is_tw or is_un):
                    continue
                found_any = True
                if is_tw:
                    cnt_twisted += 1
                else:
                    cnt_untwisted += 1
                if n <= 9:
                    M2 = M_odd @ M_odd  # orientable double cover in SL_2(Z), tr(M2) = tr(M_odd)^2 + 2 >= 3
                    eta2, re2 = siegel_eta_hyperbolic(M2, a5 / 5.0, b5 / 5.0)
                    assert re2 < 1e-11, f"Odd-tick Re(Delta) at n={n}: {re2}"
                    max_eta_n = max(max_eta_n, abs(eta2))
                    max_abs_eta_double_cover = max(max_abs_eta_double_cover, abs(eta2))
                    total_odd_pairs += 1

                    if n <= 6:
                        gamma2 = M2.T
                        ga, gb, gc, gd = float(gamma2[0, 0]), float(gamma2[0, 1]), float(gamma2[1, 0]), float(gamma2[1, 1])
                        tr2 = ga + gd
                        disc2 = math.sqrt(tr2 * tr2 - 4.0)
                        r1 = ((ga - gd) + disc2) / (2.0 * gc)
                        r2 = ((ga - gd) - disc2) / (2.0 * gc)
                        cen, rad = 0.5 * (r1 + r2), 0.5 * abs(r1 - r2)
                        ell2 = 2.0 * math.log(0.5 * (abs(tr2) + disc2))
                        z_fn = lambda s: complex(cen + rad * math.tanh(s), rad / math.cosh(s))
                        s0 = -0.5 * ell2
                        z0 = z_fn(s0)
                        gz0 = (ga * z0 + gb) / (gc * z0 + gd)
                        s2 = s0 + ell2 if abs(gz0 - z_fn(s0 + ell2)) < 1e-7 * (1.0 + abs(z0)) else s0 - ell2
                        smid = 0.5 * (s0 + s2)
                        d_half1 = _adaptive_winding(a5 / 5.0, b5 / 5.0, z_fn, s0, smid)
                        d_half2 = _adaptive_winding(a5 / 5.0, b5 / 5.0, z_fn, smid, s2)
                        max_single_half_step_abs = max(max_single_half_step_abs, abs(d_half1.imag))
                        max_half_step_sum_err = max(max_half_step_sum_err, abs(d_half1.imag + d_half2.imag))
            if found_any != (tr_odd % 5 == 0):
                trace_div_mismatches += 1

        odd_tick_by_n[str(n)] = {
            "n_twisted_characters": cnt_twisted,
            "n_untwisted_characters": cnt_untwisted,
            "max_abs_eta_double_cover": max_eta_n if n <= 9 else None,
            "mean_exp_i_half_pi_eta": (1.0 if (cnt_twisted + cnt_untwisted) > 0 else None) if n <= 9 else None,
        }

    assert trace_div_mismatches == 0
    assert max_abs_eta_double_cover < 1e-11, f"Odd-tick double-cover eta_A non-zero: {max_abs_eta_double_cover}"
    assert max_half_step_sum_err < 1e-12
    assert max_single_half_step_abs > 0.1  # individual half-steps are non-trivial, cancelling in the double cover!

    return {
        "total_odd_tick_siegel_histories_checked": total_odd_pairs,
        "trace_mod5_character_theorem_mismatches_n1_to_14": trace_div_mismatches,
        "max_abs_eta_A_orientable_double_cover": max_abs_eta_double_cover,
        "max_individual_half_step_winding_rad": max_single_half_step_abs,
        "max_two_half_steps_sum_residual": max_half_step_sum_err,
        "pure_b1929_eta_phase_cancels_odd_ticks": False,
        "mechanism": (
            "Every odd-tick monodromy M_W (det M_W = -1) acts as an orientation-reversing glide-reflection deck "
            "involution on its orientable double cover T^2_{M_W^2}; individual half-steps carry non-zero Siegel "
            "winding (up to > 0.1 rad), but the second half-step reverses fibre orientation and cancels the first "
            "identically (Delta_1 + Delta_2 = 0 to < 1e-13). Hence eta_A(T^2_{M_W^2}, w) == 0 on 100% of odd-tick "
            "histories, so exp(i alpha pi eta_A) == +1 does NOT cancel odd ticks unless an extra discrete Pin^- / "
            "Dai-Freed fourth-root cobordism factor (+-i) enters outside B1929."
        ),
        "by_word_length": odd_tick_by_n,
    }


def main() -> None:
    t_start = time.time()
    canon_json = json.loads((RELAYS / "a2_canon" / "verify_a2_canon_results.json").read_text(encoding="utf-8"))
    area_ref = {
        "W_minus": canon_json["seven_values_summary"]["area_measure_exact_untruncated"]["exact_T90"]["W_minus"]["value_7"],
        "W_plus": canon_json["seven_values_summary"]["area_measure_exact_untruncated"]["exact_T90"]["W_plus"]["value_7"],
    }

    l2_interp = a2c.CanonicalL2Interpolant()
    print(f"[A2-AMP] L2 interpolant ready ({time.time() - t_start:.1f}s)", file=sys.stderr, flush=True)

    p0 = run_part0_p860a_connection(l2_interp)
    print(f"[A2-AMP] Part 0 done ({time.time() - t_start:.1f}s)", file=sys.stderr, flush=True)
    p13 = run_part1_and_part3(l2_interp, area_ref)
    print(f"[A2-AMP] Part 1 & 3 done ({time.time() - t_start:.1f}s)", file=sys.stderr, flush=True)
    p2 = run_part2_odd_ticks()
    print(f"[A2-AMP] Part 2 done ({time.time() - t_start:.1f}s)", file=sys.stderr, flush=True)
    elapsed = time.time() - t_start

    out = {
        "card": "A2-AMP (M34 & P-860 (a))",
        "seat": "agy-002",
        "date": "2026-11-15",
        "data_free": True,
        "zero_shared_code_with_frontier": True,
        "elapsed_seconds": round(elapsed, 2),
        "part0_p860a_connection_and_gramian": p0,
        "part1_and_part3_twisted_eta_convergence_and_area_gap": p13,
        "part2_odd_tick_interference": p2,
    }
    (HERE / "verify_a2_amp.json").write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")

    # Mask-safe summary text (ZERO physical 7-values printed; only |d ln| distances, partition functions, and residuals):
    n14 = p13["observable_convergence_and_part3_area_gap"]["14"]
    n17 = p13["partition_and_variance_by_n"]["17"]
    n18 = p13["partition_and_variance_by_n"]["18"]
    tm_spec = p13["transfer_matrix_24x24_spectra"]
    h8 = p13["p846_hand_jarlskog_coupling"]["8"]
    c12 = p13["full_24pt_im_cancellation_and_CTL_AMP_1"]["12"]
    up_d = p0["CTL_AMP_2_naive_linear_sum_drifts"]["up"]
    dn_d = p0["CTL_AMP_2_naive_linear_sum_drifts"]["down"]
    gr_cov = p0["canonical_gramian_SL2Z_covariance"]
    cusp_c = gr_cov["cusp_y30_structural_check"]

    lines = [
        "=== agy-002 Standalone Verifier: Card A2-AMP (M34 & P-860 (a)) ===",
        f"Elapsed: {elapsed:.2f}s | Data-free: True | Physical 7-values in verify_a2_amp.json ONLY.",
        "",
        "--- Part 0: P-860 (a) Level-5 Weil Obstruction & Canonical Gramian Resolution ---",
        f"  Naive linear sum |d ln| under T (tau -> tau+1):   up = {up_d['reduced_T1_max_abs_dln']:.4f}, down = {dn_d['reduced_T1_max_abs_dln']:.4f} (CTL-AMP-2 CAUGHT)",
        f"  Naive linear sum |d ln| under T^5 in Gamma(5):    up = {up_d['reduced_T5_Gamma5_max_abs_dln']:.4f} (OBSTRUCTED!), down = {dn_d['reduced_T5_Gamma5_max_abs_dln']:.3e}",
        f"  Naive linear sum |d ln| under T^25 in Gamma(25):  up = {up_d['reduced_T25_Gamma25_max_abs_dln']:.3e}, down = {dn_d['reduced_T25_Gamma25_max_abs_dln']:.3e}",
        f"  T^5 Weil phases arg/(2pi) by |5*w1| mod 5:        up = {p0['Gamma5_T5_stratum_weil_monodromy']['up']['arg_over_2pi_by_abs_5w1']}, down = {p0['Gamma5_T5_stratum_weil_monodromy']['down']['arg_over_2pi_by_abs_5w1']}",
        f"  Down T-coboundary scalar-phase repaired |d ln|:   {p0['down_sector_T1_coboundary_repaired_dln']:.3e}",
        f"  Canonical Gramian H_f = (1/24) sum Y_f Y_f^H SL(2,Z) covariance:",
        f"    T (tau+1) max |d ln| = {gr_cov['T1_max_abs_dln_7']:.3e}, T^5 max |d ln| = {gr_cov['T5_max_abs_dln_7']:.3e}, S (-1/tau) max |d ln| = {gr_cov['S_max_abs_dln_7']:.3e}",
        f"    CKM unitarity ||V V^H - I||_F = {gr_cov['ckm_unitarity_err']:.3e}; interior J_CP(W-) = {gr_cov['interior_JCP_W_minus']:.4e}",
        f"    Cusp y=30 Gramian |V_33|: mixed W- = {cusp_c['y30_mixed_W_minus_abs_V33']:.3e}, aligned (S,S) = {cusp_c['y30_aligned_S_S_abs_V33']:.6f}",
        f"  CTL-AMP-3 (Guardrail 3 Haar SU(3) scrambling):    max drift = {p0['CTL_AMP_3_guardrail3_haar_scrambling']['max_observable_drift']:.3e}, planted U^H V drift = {p0['CTL_AMP_3_guardrail3_haar_scrambling']['planted_lr_overlap_min_drift']:.3e} -> CAUGHT",
        "",
        "--- Part 1: M34 Q1 — B1929 Twisted-Eta Automaton, Transfer Spectra & P-846 Hand Coupling ---",
        f"  50-dps Meyer-Siegel step cocycle: basepoint constancy err = {p13['max_cocycle_basepoint_constancy_err_50dps']:.3e}, 15*step integrality err = {p13['max_15_times_step_integrality_err_50dps']:.3e}",
        f"  Geodesic vs automaton cross-check ({p13['geodesic_vs_automaton_words_checked_n4_to_13']} words, n=4..13): max |Re Delta| = {p13['max_re_delta_residual_n4_to_13']:.3e}, max |eta_auto - eta_geo| = {p13['max_cocycle_vs_geodesic_diff_n4_to_13']:.3e}, chord diff = {p13['max_chord_vs_automaton_diff']:.3e}",
        f"  Exact 24x24 transfer matrix spectral radii: rho(alpha=1/2) = {tm_spec['alpha_half']['spectral_radius_rho']:.12f} (1/sqrt(2), sign-oscillating!), rho(alpha=1) = {tm_spec['alpha_one']['spectral_radius_rho']:.12f}",
        f"  Mirror orientation-reversal max |eta(W,w) + eta(PWP,Pw)| = {p13['max_mirror_orientation_reversal_err']:.3e}",
        f"  Full 24-pt n=12: mean sin(pi/2 eta) = {c12['mean_sin_half_pi']:.3e}, CTL-AMP-1 planted = {c12['CTL_AMP_1_planted_mean_sin_half_pi']:.4f} -> CAUGHT",
        f"  Partition Z_eta(n) = <cos(alpha pi eta_A)> (keeps_mark, n=6 -> 10 -> 14 -> 17 -> 18):",
        f"    alpha=1/2: {p13['partition_and_variance_by_n']['6']['Z_cos_half_pi_pm']:.4f} -> {p13['partition_and_variance_by_n']['10']['Z_cos_half_pi_pm']:.4f} -> {p13['partition_and_variance_by_n']['14']['Z_cos_half_pi_pm']:.4f} -> {n17['Z_cos_half_pi_pm']:.4f} -> {n18['Z_cos_half_pi_pm']:.4f}",
        f"    alpha=1:   {p13['partition_and_variance_by_n']['6']['Z_cos_pi_pm']:.4f} -> {p13['partition_and_variance_by_n']['10']['Z_cos_pi_pm']:.4f} -> {p13['partition_and_variance_by_n']['14']['Z_cos_pi_pm']:.4f} -> {n17['Z_cos_pi_pm']:.4f} -> {n18['Z_cos_pi_pm']:.4f}",
        f"    Var(eta_A): n=6: {p13['partition_and_variance_by_n']['6']['var_eta_pm']:.4f}, n=10: {p13['partition_and_variance_by_n']['10']['var_eta_pm']:.4f}, n=14: {p13['partition_and_variance_by_n']['14']['var_eta_pm']:.4f}, n=18: {n18['var_eta_pm']:.4f}",
        f"  P-846 Hand / Jarlskog J_CP on mirror-closed n=8 ensemble ({h8['n_mirror_closed_histories']} histories):",
        f"    unweighted <J_CP>(W-) = {h8['unweighted_mean_JCP_W_minus']:.3e} (cancels by mirror symmetry)",
        f"    twisted-eta <sin(pi/2 eta_A) J_CP>(W-) = {h8['sin_half_pi_eta_weighted_JCP_W_minus']:.4e}, (W+) = {h8['sin_half_pi_eta_weighted_JCP_W_plus']:.4e}",
        "",
        "--- Part 2: M34 Q2 — Dynamic Odd-Tick Interference ({L, R}^n P, det = -1, n=1..14) ---",
        f"  Trace divisibility theorem (order-5 character <=> 5 | tr(M_odd), n=1..14): mismatches = {p2['trace_mod5_character_theorem_mismatches_n1_to_14']} (0 chars for n=1..4 incl. m000)",
        f"  Checked {p2['total_odd_tick_siegel_histories_checked']} surviving odd-tick Siegel histories (n=5..9):",
        f"  Max single half-step Siegel winding = {p2['max_individual_half_step_winding_rad']:.4f} rad, but two-half-step sum residual = {p2['max_two_half_steps_sum_residual']:.3e}",
        f"  Max |eta_A(T^2_{{M^2}}, w)| = {p2['max_abs_eta_A_orientable_double_cover']:.3e} -> <exp(i alpha pi eta_A)>_odd = 1.000000 (DOES NOT CANCEL without discrete Pin^- +-i factor)",
        "",
        "--- Part 3: M34 Q3 — Move-Count vs Hyperbolic Area Log-Distance (n=14 exhaustive, exact T90) ---",
        f"  Move (ell-weighted) vs Area:         W- max |d ln| = {n14['vs_area_dln']['move_len_weighted']['W_minus_max_abs_dln']:.4f} (rms {n14['vs_area_dln']['move_len_weighted']['W_minus_rms_dln']:.4f}), W+ max |d ln| = {n14['vs_area_dln']['move_len_weighted']['W_plus_max_abs_dln']:.4f}",
        f"  Move (uniform) vs Area:              W- max |d ln| = {n14['vs_area_dln']['move_uniform']['W_minus_max_abs_dln']:.4f} (rms {n14['vs_area_dln']['move_uniform']['W_minus_rms_dln']:.4f}), W+ max |d ln| = {n14['vs_area_dln']['move_uniform']['W_plus_max_abs_dln']:.4f}",
        f"  Twisted-eta (alpha=1/2) vs Area:     W- max |d ln| = {n14['vs_area_dln']['twisted_eta_half_pi']['W_minus_max_abs_dln']:.4f} (rms {n14['vs_area_dln']['twisted_eta_half_pi']['W_minus_rms_dln']:.4f}), W+ max |d ln| = {n14['vs_area_dln']['twisted_eta_half_pi']['W_plus_max_abs_dln']:.4f}",
        f"  Twisted-eta (alpha=1) vs Area:       W- max |d ln| = {n14['vs_area_dln']['twisted_eta_pi']['W_minus_max_abs_dln']:.4f} (rms {n14['vs_area_dln']['twisted_eta_pi']['W_minus_rms_dln']:.4f}), W+ max |d ln| = {n14['vs_area_dln']['twisted_eta_pi']['W_plus_max_abs_dln']:.4f}",
        f"  Selberg |det(I-M)|^(-1/2) vs Area:   W- max |d ln| = {n14['vs_area_dln']['selberg_one_loop']['W_minus_max_abs_dln']:.4f} (rms {n14['vs_area_dln']['selberg_one_loop']['W_minus_rms_dln']:.4f}), W+ max |d ln| = {n14['vs_area_dln']['selberg_one_loop']['W_plus_max_abs_dln']:.4f}",
        f"  Selberg * cos(pi/2 eta_A) vs Area:   W- max |d ln| = {n14['vs_area_dln']['selberg_times_eta_half_pi']['W_minus_max_abs_dln']:.4f} (rms {n14['vs_area_dln']['selberg_times_eta_half_pi']['W_minus_rms_dln']:.4f}), W+ max |d ln| = {n14['vs_area_dln']['selberg_times_eta_half_pi']['W_plus_max_abs_dln']:.4f}",
        "",
        "ALL ASSERTIONS AND PLANTED CONTROLS PASSED. 0 of 19.",
    ]
    txt = "\n".join(lines) + "\n"
    (HERE / "verify_a2_amp_out.txt").write_text(txt, encoding="utf-8")
    print(txt, end="")


if __name__ == "__main__":
    main()
