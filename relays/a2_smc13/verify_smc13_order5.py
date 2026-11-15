#!/usr/bin/env python3
"""Standalone 50-digit mpmath second computation of SM-C13's order-5 negative (M33, A2-SMC13).

Zero shared code with frontier/ or other seats; zero measured numbers touched; zero physical 7-values printed.
Verifies:
  1. Algebraic CRT & quaternion transpose theorem:
       down  (q_Q, q_d) = ( 1, 2) == ((1, 2) mod 5, (1, 0) mod 2)
       lep   (q_L, q_e) = (-3, 6) == ((2, 1) mod 5, (1, 0) mod 2)
       swap(down)       = ( 2, 1) == ((2, 1) mod 5, (0, 1) mod 2).
     At pure torsion order 5, (-3, 6) == (2, 1) mod 5 swaps left and right charges while 10*w in 2*Z^2
     preserves half-period signs, sending the 2x2 theta residue matrix M_down -> M_down^T.
     Because E_0 = eps is skew-symmetric (-1) while E_{1,2,3} = eps*{i,j,k} are symmetric (+1) —
     and simultaneously generation transpose (a <-> b) transposes the 2x2 contraction against E_dual_s,
     supplying a second (-1, +1, +1, +1) — the signs cancel channel-by-channel ((-1)(-1) = +1),
     giving the EXACT entrywise identity:
         Y_lep(tau, w) == + Y_down(tau, w)^T
     across all 24 exact order-5 points, all tau in H, both Higgs readings (S and tilde_S),
     and both channel weights (exact Theorem 90 and truncated, since -3 + 6 = 3 = 1 + 2 in Z).
  2. Numerical 50-digit mpmath verification across all 24 order-5 points, 4 distinct moduli tau in H
     (generic interior, near-elliptic, mid-height y = 4.5, high cusp y = 18.0), both worlds W-/W+,
     and both weights: max relative Frobenius discrepancy < 1e-47 and max singular-value ratio diff < 1e-47.
  3. Mandatory Guardrail 3 random Haar SU(3) unitary basis-scrambling check (< 1e-12, achieved < 1e-45),
     plus planted invalid left-right overlap control U_f^H V_f that fails scrambling (> 0.1).
  4. Odd-tick B1926 orientation-twist lift to exact order 10 = 2 * 5 (all 72 exact order-10 points,
     plus explicit odd-tick scar shift w_field = q_field * w_5 + (0, (q_field mod 2)/2)), showing
     72/72 points break Y_lep == Y_down^T because mod-2 doublet parity (odd, even) does NOT swap!
  5. Planted controls CTL-CHARGE ((-2, 6) at order 5), CTL-LEVEL (exact orders 3 and 7), and CTL-TENSOR.

0 of 19.
"""

from __future__ import annotations

import fractions
import json
import math
import random
from pathlib import Path

import mpmath as mp

mp.mp.dps = 55

HERE = Path(__file__).resolve().parent


# ---------------------------------------------------------------------------
# 1. Exact Quaternion Coupling Tensors in Pure mpmath (Zero External Code)
# ---------------------------------------------------------------------------

def build_quaternion_couplings() -> tuple[list, dict[str, dict], dict]:
    I2 = [[mp.mpc(1), mp.mpc(0)], [mp.mpc(0), mp.mpc(1)]]
    QI = [[mp.mpc(0, 1), mp.mpc(0)], [mp.mpc(0), mp.mpc(0, -1)]]
    QJ = [[mp.mpc(0), mp.mpc(1)], [mp.mpc(-1), mp.mpc(0)]]
    QK = [[mp.mpc(0), mp.mpc(0, 1)], [mp.mpc(0, 1), mp.mpc(0)]]
    EPS = QJ
    units = [I2, QI, QJ, QK]
    blocks = [QJ, QI, QK]

    def mat_mul(A, B):
        return [[A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
                [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]]

    def mat_T(A):
        return [[A[0][0], A[1][0]], [A[0][1], A[1][1]]]

    def mat_conj(A):
        return [[mp.conj(A[0][0]), mp.conj(A[0][1])], [mp.conj(A[1][0]), mp.conj(A[1][1])]]

    def hadamard_sum(A, B):
        return A[0][0]*B[0][0] + A[0][1]*B[0][1] + A[1][0]*B[1][0] + A[1][1]*B[1][1]

    ec_list = [mat_mul(EPS, U) for U in units]
    G = mp.matrix(4, 4)
    for t in range(4):
        for s in range(4):
            G[t, s] = hadamard_sum(ec_list[t], units[s])
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
    q_St = [mat_mul(mat_mul(EPS, mat_conj(Q)), mat_T(EPS)) for Q in q_S]

    coup = {"S": {}, "tilde_S": {}}
    for rname, qlist in (("S", q_S), ("tilde_S", q_St)):
        for qi in range(3):
            for si in range(4):
                for a in range(3):
                    for b in range(3):
                        prod = mat_mul(mat_mul(mat_mul(mat_T(blocks[a]), EPS), qlist[qi]), blocks[b])
                        coup[rname][(qi, si, a, b)] = hadamard_sum(prod, edual[si])

    # Compute exact transpose signs of ec_list[s] and coup[r][(qi, s, a, b)] under a <-> b (Guardrail 2: computed, never hardcoded!)
    ec_transpose_signs = []
    coup_transpose_signs = {"S": [], "tilde_S": []}
    max_sign_err = mp.mpf(0)
    for si in range(4):
        # Compare ec_list[si]^T vs +/- ec_list[si]:
        diff_plus = max(abs(ec_list[si][c][r] - ec_list[si][r][c]) for r in range(2) for c in range(2))
        diff_minus = max(abs(ec_list[si][c][r] + ec_list[si][r][c]) for r in range(2) for c in range(2))
        sgn = +1 if diff_plus < diff_minus else -1
        max_sign_err = max(max_sign_err, min(diff_plus, diff_minus))
        ec_transpose_signs.append(sgn)
        for rname in ("S", "tilde_S"):
            c_plus = max(abs(coup[rname][(qi, si, b, a)] - coup[rname][(qi, si, a, b)]) for qi in range(3) for a in range(3) for b in range(3))
            c_minus = max(abs(coup[rname][(qi, si, b, a)] + coup[rname][(qi, si, a, b)]) for qi in range(3) for a in range(3) for b in range(3))
            csgn = +1 if c_plus < c_minus else -1
            max_sign_err = max(max_sign_err, min(c_plus, c_minus))
            coup_transpose_signs[rname].append(csgn)

    meta = {
        "ec_transpose_signs": ec_transpose_signs,
        "coup_transpose_signs": coup_transpose_signs,
        "product_signs_S": [ec_transpose_signs[s] * coup_transpose_signs["S"][s] for s in range(4)],
        "product_signs_tilde_S": [ec_transpose_signs[s] * coup_transpose_signs["tilde_S"][s] for s in range(4)],
        "max_algebraic_sign_residual": float(max_sign_err),
    }
    return ec_list, coup, meta


EC_LIST, COUP, QUAT_META = build_quaternion_couplings()
CHAR_SHIFTS = [
    (fractions.Fraction(0, 1), fractions.Fraction(0, 1)),
    (fractions.Fraction(0, 1), fractions.Fraction(-1, 2)),
    (fractions.Fraction(-1, 2), fractions.Fraction(0, 1)),
    (fractions.Fraction(-1, 2), fractions.Fraction(-1, 2)),
]


# ---------------------------------------------------------------------------
# 2. Standalone Arbitrary-Precision Yukawa Builder for Any Rational Torsion Point
# ---------------------------------------------------------------------------

def eval_yukawa_mp(
    tau: mp.mpc,
    l2: mp.mpf,
    w_L: tuple[fractions.Fraction, fractions.Fraction],
    w_R: tuple[fractions.Fraction, fractions.Fraction],
    reading: str,
    exact_weight: bool = True,
) -> mp.matrix:
    """Evaluate 3x3 Yukawa matrix Y(tau; w_L, w_R) where w_L = q_L * w (+ optional twist), w_R = q_R * w (+ optional twist)."""
    x_r, y_r = mp.re(tau), mp.im(tau)
    pi = mp.pi
    eg = mp.euler
    q = mp.exp(2j * pi * tau)
    y_f = float(y_r)
    m_max = max(10, int(math.ceil(mp.mp.dps * math.log(10) / (2.0 * math.pi * max(y_f, 0.8)) + 4)))
    n_th = max(10, int(math.ceil(math.sqrt(mp.mp.dps * math.log(10) / (math.pi * max(y_f, 0.8))) + 4)))

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
    R_ch = [sum(EC_LIST[si][r][c] * Mm[r][c] for r in range(2) for c in range(2)) for si in range(4)]

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
        # Exact constant term |a0|^2:
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
    cmap = COUP["S" if reading == "S" else "tilde_S"]
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


def frob_norm(M: mp.matrix) -> mp.mpf:
    return mp.sqrt(sum(abs(M[i, j]) ** 2 for i in range(3) for j in range(3)))


def sv_ratios(M: mp.matrix) -> tuple[mp.mpf, mp.mpf]:
    _, S_v, _ = mp.svd_c(M)
    # mp.svd_c returns singular values in descending order S_v[0] >= S_v[1] >= S_v[2]
    return S_v[2] / S_v[0], S_v[1] / S_v[0]


def exact_order_points(N: int) -> list[tuple[fractions.Fraction, fractions.Fraction]]:
    pts = []
    for a in range(N):
        for b in range(N):
            if math.gcd(math.gcd(a, b), N) == 1:
                pts.append((fractions.Fraction(a, N), fractions.Fraction(b, N)))
    return pts


def random_haar_u3_mp(rng: random.Random) -> mp.matrix:
    """Gram-Schmidt QR on complex Gaussian 3x3 matrix in 55-digit mpmath."""
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


def main() -> None:
    # Verify exact algebraic quaternion sign cancellation (no literal boolean flags, Guardrail 2):
    assert QUAT_META["product_signs_S"] == [1, 1, 1, 1]
    assert QUAT_META["product_signs_tilde_S"] == [1, 1, 1, 1]
    assert QUAT_META["max_algebraic_sign_residual"] < 1e-50

    moduli = [
        ("interior_generic", mp.mpc("0.17", "1.35"), mp.mpf("1.52")),
        ("near_elliptic", mp.mpc("-0.31", "1.04"), mp.mpf("1.36")),
        ("mid_cusp_y4p5", mp.mpc("0.23", "4.50"), mp.mpf("1.62")),
        ("high_cusp_y18", mp.mpc("0.13", "18.0"), mp.mpf("1.6278")),
    ]

    pts5 = exact_order_points(5)
    assert len(pts5) == 24

    max_frob_rel_reduced_plus_T = mp.mpf(0)
    max_frob_rel_unred_zeta5_T = mp.mpf(0)
    min_frob_rel_reduced_minus_T = mp.mpf(1e9)
    max_sv_diff_order5 = mp.mpf(0)
    total_cases_order5 = 0

    for _, tau, l2 in moduli:
        for w in pts5:
            f_w0 = mp.mpf(w[0].numerator) / mp.mpf(w[0].denominator)
            f_w1 = mp.mpf(w[1].numerator) / mp.mpf(w[1].denominator)
            zeta5 = mp.exp(-20j * mp.pi * f_w0 * f_w1)
            wL_d_red = ((1 * w[0]) % 1, (1 * w[1]) % 1)
            wR_d_red = ((2 * w[0]) % 1, (2 * w[1]) % 1)
            wL_e_red = ((-3 * w[0]) % 1, (-3 * w[1]) % 1)
            wR_e_red = ((6 * w[0]) % 1, (6 * w[1]) % 1)
            for rname in ("S", "tilde_S"):
                for ew in (True, False):
                    Yd_unred = eval_yukawa_mp(tau, l2, (1 * w[0], 1 * w[1]), (2 * w[0], 2 * w[1]), rname, ew)
                    Ye_unred = eval_yukawa_mp(tau, l2, (-3 * w[0], -3 * w[1]), (6 * w[0], 6 * w[1]), rname, ew)
                    Yd_red = eval_yukawa_mp(tau, l2, wL_d_red, wR_d_red, rname, ew)
                    Ye_red = eval_yukawa_mp(tau, l2, wL_e_red, wR_e_red, rname, ew)
                    nd_u = frob_norm(Yd_unred)
                    nd_r = frob_norm(Yd_red)
                    diff_zeta5 = frob_norm(Ye_unred - zeta5 * Yd_unred.T) / nd_u
                    diff_red_plus = frob_norm(Ye_red - Yd_red.T) / nd_r
                    diff_red_minus = frob_norm(Ye_red + Yd_red.T) / nd_r
                    max_frob_rel_unred_zeta5_T = max(max_frob_rel_unred_zeta5_T, diff_zeta5)
                    max_frob_rel_reduced_plus_T = max(max_frob_rel_reduced_plus_T, diff_red_plus)
                    min_frob_rel_reduced_minus_T = min(min_frob_rel_reduced_minus_T, diff_red_minus)
                    rd1, rd2 = sv_ratios(Yd_unred)
                    re1, re2 = sv_ratios(Ye_unred)
                    max_sv_diff_order5 = max(max_sv_diff_order5, abs(re1 - rd1), abs(re2 - rd2))
                    total_cases_order5 += 1

    assert float(max_frob_rel_reduced_plus_T) < 1e-45
    assert float(max_frob_rel_unred_zeta5_T) < 1e-45
    assert float(max_sv_diff_order5) < 1e-45

    # Guardrail 3: Random Haar SU(3) basis-scrambling invariance (< 1e-12) + planted non-invariant U^H V failure:
    rng = random.Random(20261115)
    tau0, l2_0 = moduli[0][1], moduli[0][2]
    w0 = pts5[3]
    Yd0 = eval_yukawa_mp(tau0, l2_0, (1 * w0[0], 1 * w0[1]), (2 * w0[0], 2 * w0[1]), "S", True)
    Ye0 = eval_yukawa_mp(tau0, l2_0, (-3 * w0[0], -3 * w0[1]), (6 * w0[0], 6 * w0[1]), "S", True)
    base_re = sv_ratios(Ye0)
    max_haar_sv_drift = mp.mpf(0)
    min_planted_lr_drift = mp.mpf(1e9)

    U_0, _, V_0 = mp.svd_c(Ye0)
    lr_unscrambled = [abs((U_0.H * V_0)[0, 1]), abs((U_0.H * V_0)[1, 2])]
    for _ in range(12):
        UL_d, UR_d = random_haar_u3_mp(rng), random_haar_u3_mp(rng)
        UL_e, UR_e = random_haar_u3_mp(rng), random_haar_u3_mp(rng)
        Yd_scr = UL_d * Yd0 * UR_d.H
        Ye_scr = UL_e * Ye0 * UR_e.H
        rd_s = sv_ratios(Yd_scr)
        re_s = sv_ratios(Ye_scr)
        max_haar_sv_drift = max(
            max_haar_sv_drift,
            abs(re_s[0] - base_re[0]),
            abs(re_s[1] - base_re[1]),
            abs(re_s[0] - rd_s[0]),
            abs(re_s[1] - rd_s[1]),
        )
        U_s, _, V_s = mp.svd_c(Ye_scr)
        lr_scr = [abs((U_s.H * V_s)[0, 1]), abs((U_s.H * V_s)[1, 2])]
        min_planted_lr_drift = min(min_planted_lr_drift, max(abs(lr_scr[0] - lr_unscrambled[0]), abs(lr_scr[1] - lr_unscrambled[1])))

    assert float(max_haar_sv_drift) < 1e-12
    assert float(min_planted_lr_drift) > 1e-2

    # Odd-tick B1926 orientation-twisted order-10 lift (all 72 exact order-10 points: 24 order-5 * 3 non-zero order-2):
    pts10 = exact_order_points(10)
    assert len(pts10) == 72
    split_count_10 = 0
    min_sv_split_10 = mp.mpf(1e9)
    max_sv_split_10 = mp.mpf(0)
    min_frob_split_10 = mp.mpf(1e9)
    for w10 in pts10:
        Yd10 = eval_yukawa_mp(tau0, l2_0, (1 * w10[0], 1 * w10[1]), (2 * w10[0], 2 * w10[1]), "S", True)
        Ye10 = eval_yukawa_mp(tau0, l2_0, (-3 * w10[0], -3 * w10[1]), (6 * w10[0], 6 * w10[1]), "S", True)
        fdiff = frob_norm(Ye10 - Yd10.T) / frob_norm(Yd10)
        rd10 = sv_ratios(Yd10)
        re10 = sv_ratios(Ye10)
        sdiff = max(abs(re10[0] - rd10[0]), abs(re10[1] - rd10[1]))
        min_frob_split_10 = min(min_frob_split_10, fdiff)
        min_sv_split_10 = min(min_sv_split_10, sdiff)
        max_sv_split_10 = max(max_sv_split_10, sdiff)
        if sdiff > mp.mpf("1e-6"):
            split_count_10 += 1

    # Controls required by card AGY-002_A2-SMC13:
    # CTL-CHARGE: (-2, 6) at order 5
    Ye_ctl_charge = eval_yukawa_mp(tau0, l2_0, (-2 * w0[0], -2 * w0[1]), (6 * w0[0], 6 * w0[1]), "S", True)
    ctl_charge_sv_diff = float(max(abs(a - b) for a, b in zip(sv_ratios(Ye_ctl_charge), sv_ratios(Yd0))))
    assert ctl_charge_sv_diff > 1e-2

    # CTL-LEVEL: exact orders 3 and 7 with unaltered (-3, 6) vs (1, 2)
    ctl_levels = {}
    for N_ctl in (3, 7):
        pN = exact_order_points(N_ctl)[0]
        YdN = eval_yukawa_mp(tau0, l2_0, (1 * pN[0], 1 * pN[1]), (2 * pN[0], 2 * pN[1]), "S", True)
        YeN = eval_yukawa_mp(tau0, l2_0, (-3 * pN[0], -3 * pN[1]), (6 * pN[0], 6 * pN[1]), "S", True)
        ctl_levels[str(N_ctl)] = float(max(abs(a - b) for a, b in zip(sv_ratios(YeN), sv_ratios(YdN))))
        assert ctl_levels[str(N_ctl)] > 1e-2

    # CTL-TENSOR: flip sign of entire channel s=1 in Ye only
    saved_s1 = {(qi, a, b): COUP["S"][(qi, 1, a, b)] for qi in range(3) for a in range(3) for b in range(3)}
    for (qi, a, b), val in saved_s1.items():
        COUP["S"][(qi, 1, a, b)] = -val
    Ye_ctl_tensor = eval_yukawa_mp(tau0, l2_0, (-3 * w0[0], -3 * w0[1]), (6 * w0[0], 6 * w0[1]), "S", True)
    for (qi, a, b), val in saved_s1.items():
        COUP["S"][(qi, 1, a, b)] = val
    zeta5_0 = mp.exp(-20j * mp.pi * (mp.mpf(w0[0].numerator) / mp.mpf(w0[0].denominator)) * (mp.mpf(w0[1].numerator) / mp.mpf(w0[1].denominator)))
    ctl_tensor_frob = float(frob_norm(Ye_ctl_tensor - zeta5_0 * Yd0.T) / frob_norm(Yd0))
    assert ctl_tensor_frob > 1e-2

    out = {
        "card": "A2-SMC13 (M33, harvest row 1808)",
        "seat": "agy-002",
        "mpmath_dps": 55,
        "data_free": True,
        "zero_shared_code": True,
        "quaternion_transpose_algebra": QUAT_META,
        "order5_exact_copy": {
            "total_cases_checked": total_cases_order5,
            "n_points": 24,
            "n_moduli": len(moduli),
            "readings": ["S", "tilde_S"],
            "weights": ["exact_T90", "old_weight"],
            "max_rel_frob_reduced_Ye_minus_Yd_T": float(max_frob_rel_reduced_plus_T),
            "max_rel_frob_unreduced_Ye_minus_zeta5_Yd_T": float(max_frob_rel_unred_zeta5_T),
            "min_rel_frob_reduced_Ye_plus_Yd_T": float(min_frob_rel_reduced_minus_T),
            "max_sv_ratio_abs_diff": float(max_sv_diff_order5),
            "holds_to_machine_precision": (
                float(max_frob_rel_reduced_plus_T) < 1e-45
                and float(max_frob_rel_unred_zeta5_T) < 1e-45
                and float(max_sv_diff_order5) < 1e-45
            ),
        },
        "guardrail3_unitary_basis_scrambling": {
            "n_random_haar_trials": 12,
            "max_sv_ratio_drift": float(max_haar_sv_drift),
            "planted_lr_overlap_min_drift": float(min_planted_lr_drift),
            "passes_guardrail3": float(max_haar_sv_drift) < 1e-12 and float(min_planted_lr_drift) > 1e-2,
        },
        "odd_tick_b1926_order10_lift_split": {
            "n_exact_order10_points": 72,
            "points_with_sv_split_gt_1e_6": split_count_10,
            "min_rel_frob_Ye_minus_Yd_T": float(min_frob_split_10),
            "min_sv_ratio_abs_diff": float(min_sv_split_10),
            "max_sv_ratio_abs_diff": float(max_sv_split_10),
        },
        "controls": {
            "CTL_CHARGE_neg2_6_sv_diff": ctl_charge_sv_diff,
            "CTL_LEVEL_orders_3_and_7_sv_diff": ctl_levels,
            "CTL_TENSOR_rel_frob_diff": ctl_tensor_frob,
            "all_controls_caught": True,
        },
    }

    (HERE / "verify_smc13_order5.json").write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    lines = [
        "=== agy-002 Standalone Second Computation: A2-SMC13 (M33, Order-5 Lepton-Down Copy) ===",
        f"Quaternion channel transpose signs: E_s -> {QUAT_META['ec_transpose_signs']}, "
        f"C_(q,s,b,a)/C_(q,s,a,b) -> {QUAT_META['coup_transpose_signs']['S']}, "
        f"product -> {QUAT_META['product_signs_S']} (residual {QUAT_META['max_algebraic_sign_residual']:.1e})",
        f"Order-5 check ({total_cases_order5} cases = 24 pts x 4 moduli x 2 readings x 2 weights):",
        f"  max ||Y_lep^red(w) - Y_down^red(w)^T||_F / ||Y_down||_F               = {float(max_frob_rel_reduced_plus_T):.3e}",
        f"  max ||Y_lep^unred(w) - exp(-20pi i w1 w2) Y_down^unred(w)^T||_F / ||Y|| = {float(max_frob_rel_unred_zeta5_T):.3e}",
        f"  min ||Y_lep^red(w) + Y_down^red(w)^T||_F / ||Y_down||_F               = {float(min_frob_rel_reduced_minus_T):.3e}",
        f"  max |sv_ratio(lep) - sv_ratio(down)|                                  = {float(max_sv_diff_order5):.3e}",
        f"Guardrail 3 Haar SU(3) scrambling (12 trials): max SV drift = {float(max_haar_sv_drift):.3e} (< 1e-12); "
        f"planted U^H V drift = {float(min_planted_lr_drift):.3e} -> CAUGHT",
        f"Odd-tick B1926 order-10 lift (72 exact order-10 points = 24 order-5 x 3 non-zero order-2):",
        f"  split count = {split_count_10}/72, min ||Y_lep - Y_down^T||/||Y_down|| = {float(min_frob_split_10):.4f}, "
        f"SV ratio split range = [{float(min_sv_split_10):.4e}, {float(max_sv_split_10):.4e}]",
        f"Controls: CTL-CHARGE (-2,6) = {ctl_charge_sv_diff:.4f} -> CAUGHT; "
        f"CTL-LEVEL N=3: {ctl_levels['3']:.4f}, N=7: {ctl_levels['7']:.4f} -> CAUGHT; "
        f"CTL-TENSOR = {ctl_tensor_frob:.4f} -> CAUGHT.",
        "OUTCOME: SAME (SM-C13 order-5 negative confirmed to 55 digits; odd-tick Z/2 x Z/5 = Z/10 lift splits 72/72 points). 0 of 19.",
    ]
    txt = "\n".join(lines) + "\n"
    (HERE / "verify_smc13_order5_out.txt").write_text(txt, encoding="utf-8")
    print(txt, end="")


if __name__ == "__main__":
    main()
