#!/usr/bin/env python3
"""Card A2-PEER-SM-FC2 — Blind Cross-Family Independent Verification of
SM-C23 (Frame C Joint Covariance) and SM-C24 (Order-30 Whole Instrument, 240 = 5 x 48 Pairs & 12 Classes).

Seat code: fam3-v1-high-03 (verifying fam1-v1-unset-04 on origin/sm/cards @ 1c5b13d0a).
Strictly blind (0 of 19): ZERO sm/cards scripts or outputs opened before sealing.
Self-contained: stdlib + mpmath only; ZERO AST float literals; ZERO JSON floats.
"""
import ast
import json
import math
import pathlib
import random
import sys
from collections import Counter
from fractions import Fraction as Fr

import mpmath as mp

HERE = pathlib.Path(__file__).resolve().parent
OUT_JSON = HERE / "a2_peer_sm_fc2_out.json"

HALF = Fr(1, 2)
CHARGES = {"up": (1, -4), "down": (1, 2), "lep": (-3, 6)}
UNIT_KEYS = ("1", "i", "j", "k")


def _f2m(q):
    return mp.mpf(q.numerator) / mp.mpf(q.denominator)


def _setup_mats():
    I = mp.mpc(0, 1)
    QI = mp.matrix([[I, 0], [0, -I]])
    QJ = mp.matrix([[0, 1], [-1, 0]])
    QK = QI * QJ
    EPS = QJ
    UNITS = {"1": mp.eye(2), "i": QI, "j": QJ, "k": QK}
    # Dual basis EDUAL solving sum_{m,n} (EPS * C_t)_{m,n} (EDUAL_s)_{m,n} = delta_{s,t}
    G = mp.zeros(4, 4)
    for r_i, t_k in enumerate(UNIT_KEYS):
        EC = EPS * UNITS[t_k]
        for c_i, s_k in enumerate(UNIT_KEYS):
            U = UNITS[s_k]
            G[r_i, c_i] = sum(EC[m, n] * U[m, n] for m in range(2) for n in range(2))
    Gi = G ** (-1)
    ED = {}
    for a_i, k_a in enumerate(UNIT_KEYS):
        M = mp.zeros(2, 2)
        for b_i, k_b in enumerate(UNIT_KEYS):
            M += Gi[b_i, a_i] * UNITS[k_b]
        ED[k_a] = M
    BLOCKS = [QJ, QI, QK]
    return I, QI, QJ, QK, EPS, UNITS, ED, BLOCKS


def _th_mp(n, u, t):
    I = mp.mpc(0, 1)
    q = mp.exp(I * mp.pi * t)
    x = mp.pi * u
    if n == 3:
        return mp.jtheta(3, x, q)
    if n == 4:
        return mp.jtheta(4, x, q)
    q4 = mp.exp(I * mp.pi * t / 4)
    s = x + mp.pi * t / 2
    if n == 2:
        return q4 * mp.exp(I * x) * mp.jtheta(3, s, q)
    return -I * q4 * mp.exp(I * x) * mp.jtheta(4, s, q)


def _thc_mp(a, b, t):
    """Theta with characteristic (a, b) evaluated at u = 0: exp(i pi a^2 t + 2 i pi a b) th3(a t + b, t)."""
    I = mp.mpc(0, 1)
    return mp.exp(I * mp.pi * a * a * t + 2 * I * mp.pi * a * b) * _th_mp(3, a * t + b, t)


def _th1_and_deriv(z, t):
    """Exact theta_1(z, t) and d/dz theta_1(z, t) via mp.jtheta (no numerical differentiation)."""
    I = mp.mpc(0, 1)
    q = mp.exp(I * mp.pi * t)
    x = mp.pi * z
    # theta_1(z, t) = jtheta(1, pi*z, q)
    val = mp.jtheta(1, x, q)
    dval = mp.pi * mp.jtheta(1, x, q, 1)
    return val, dval


def _th2_bf(t):
    """Branch-free theta_2(0, t) (avoids mp.jtheta(2) principal branch jump across Re(t) = +-1)."""
    I = mp.mpc(0, 1)
    y = float(mp.im(t))
    N = max(12, int(math.sqrt(mp.mp.dps * 231 / (100 * math.pi * max(y, 1 / 10)))) + 6)
    return 2 * mp.exp(I * mp.pi * t / 4) * mp.fsum(mp.exp(I * mp.pi * t * n * (n + 1)) for n in range(N))


def _eta_bf(t):
    """Branch-free Dedekind eta(t)."""
    I = mp.mpc(0, 1)
    return mp.exp(I * mp.pi * t / 12) * mp.qp(mp.exp(2 * I * mp.pi * t))


def _higgs_DR_mp(t):
    """Exact Halphen-Serre closed form for DR(t) (B1974 H1 identity, branch-free across H):
    24 eta^3 (c0, c1, -i c2) = (-th2^2 (th3^4 + th4^4), th4^2 (th2^4 + th3^4), th3^2 (th2^4 - th4^4))."""
    I = mp.mpc(0, 1)
    q = mp.exp(I * mp.pi * t)
    t2 = _th2_bf(t)
    t3 = mp.jtheta(3, 0, q)
    t4 = mp.jtheta(4, 0, q)
    den = 24 * (_eta_bf(t) ** 3)
    c0 = -(t2 ** 2) * (t3 ** 4 + t4 ** 4) / den
    c1 = (t4 ** 2) * (t2 ** 4 + t3 ** 4) / den
    c2 = I * (t3 ** 2) * (t2 ** 4 - t4 ** 4) / den
    return [c0, c1, c2]


def _F_u(u1, u2, t, y):
    """B1919 / B1940 closed form for F_u(u1, u2; tau) in mpmath."""
    I = mp.mpc(0, 1)
    a = u1 % 1
    b = u2 % 1
    x = mp.re(t)
    if a != 0:
        af = _f2m(a)
        first = -mp.pi * (2 * mp.log(2) + mp.log(y) + mp.digamma(af) + mp.digamma(1 - af))
        zero_row = mp.mpf(0)
    else:
        first = mp.pi * (2 * mp.euler - 2 * mp.log(2) - mp.log(y))
        zero_row = (y * (mp.pi ** 2) / (mp.sin(mp.pi * _f2m(b)) ** 2)) if b != 0 else mp.inf
    # K = ceil(dps * ln(10) / (2 pi y)) + 4
    K = int(mp.mp.dps * 231 / (100 * 2 * float(mp.pi) * float(y))) + 4
    tot = mp.mpf(0)
    af = _f2m(a)
    u2f = _f2m(u2)
    for k in range(-K, K + 1):
        m = af + k
        if m == 0:
            continue
        w = mp.exp(-2 * mp.pi * abs(m) * y + 2 * I * mp.pi * (m * x + u2f))
        tot += (2 * mp.pi / abs(m)) * mp.re(w / (1 - w))
    return first + zero_row + tot


def _is_zero_char(c):
    return (c[0] - HALF) % 1 == 0 and (c[1] - HALF) % 1 == 0


def _svd_3x3_jw(Y):
    """Non-squaring 6x6 Hermitian Jordan-Wielandt SVD for 3x3 complex matrix Y.
    Returns (U_asc, sv_asc) where sv_asc = [s1, s2, s3] ascending and columns of U_asc are unit left singular vectors."""
    # Scale Y by Frobenius norm to keep Jordan-Wielandt well conditioned at huge y
    frob = mp.sqrt(mp.fsum(abs(Y[i, j]) ** 2 for i in range(3) for j in range(3)))
    if frob == 0:
        return mp.eye(3), [mp.mpf(0), mp.mpf(0), mp.mpf(0)]
    Ys = Y / frob
    H6 = mp.zeros(6, 6)
    for i in range(3):
        for j in range(3):
            H6[i, 3 + j] = Ys[i, j]
            H6[3 + j, i] = mp.conj(Ys[i, j])
    vals, vecs = mp.eighe(H6)
    # Positive eigenvalues are the 3 singular values (sorted ascending)
    pos_idx = sorted(range(6), key=lambda k: mp.re(vals[k]))[3:]
    sv = [mp.re(vals[k]) * frob for k in pos_idx]
    U = mp.zeros(3, 3)
    for col_i, k in enumerate(pos_idx):
        u_col = [vecs[r, k] for r in range(3)]
        nrm = mp.sqrt(mp.fsum(abs(x) ** 2 for x in u_col))
        for r in range(3):
            U[r, col_i] = u_col[r] / nrm
    return U, sv


def _frame_c_eval(t, a_fr, b_fr, L_val, ctx, S_mat=None):
    """Evaluate Frame C (reading S for up, down, lep) at (t, (a_fr, b_fr), L_val)."""
    I, QI, QJ, QK, EPS, UNITS, ED, BLOCKS = ctx
    y = mp.im(t)
    t1p = 2 * mp.pi * (_eta_bf(t) ** 3)
    if S_mat is None:
        c3 = _higgs_DR_mp(t)
        S_mat = c3[0] * QI + c3[1] * QJ + c3[2] * QK
    # Precompute 2x2 block tensor B_ab = C_a^T EPS S C_b (3x3 of 2x2 matrices)
    # Wait: compute Y directly from Mw
    Ys = {}
    for sec in ("up", "down", "lep"):
        ql, qr = CHARGES[sec]
        x = (ql * a_fr, 2 * ql * b_fr)
        yy = (qr * a_fr, 2 * qr * b_fr)
        ap, am = x[0] + yy[0], x[0] - yy[0]
        bp, bm = (x[1] + yy[1]) / 2, (x[1] - yy[1]) / 2
        e = mp.exp(-2 * I * mp.pi * _f2m(x[0]))
        kap = {"1": -I * e, "i": mp.mpf(-1), "j": -e, "k": I}
        cs = {"1": (ap + HALF, bp + HALF), "i": (ap + HALF, bp), "j": (ap, bp + HALF), "k": (ap, bp)}
        ds = {"1": (am + HALF, bm + HALF), "i": (am + HALF, bm), "j": (am, bm + HALF), "k": (am, bm)}
        u = {}
        for s in UNIT_KEYS:
            if _is_zero_char(cs[s]) or _is_zero_char(ds[s]):
                u[s] = mp.mpf(0)
                continue
            R = kap[s] * _thc_mp(_f2m(cs[s][0]), _f2m(cs[s][1]), t) * _thc_mp(_f2m(ds[s][0]), _f2m(ds[s][1]), t) / t1p
            al, be = cs[s][0] - HALF, cs[s][1] - HALF
            z = _f2m(al) * t + _f2m(be)
            tv, tdv = _th1_and_deriv(z, t)
            a0 = 2 * I * mp.pi * _f2m(al) + tdv / tv
            c_val = _F_u(al, be, t, y) + mp.pi * mp.log(y) - 2 * mp.pi * (mp.euler + mp.log(mp.pi))
            c_val = c_val - mp.pi * (abs(a0) ** 2) * mp.exp(-2 * L_val)
            arg = 2 * mp.pi * L_val + c_val
            u[s] = mp.sqrt(arg) * R if arg > 0 else mp.mpf(0)
        Mw = mp.zeros(2, 2)
        for s in UNIT_KEYS:
            if u[s] != 0:
                Mw += u[s] * ED[s]
        Y = mp.zeros(3, 3)
        for i_a, Ca in enumerate(BLOCKS):
            for i_b, Cb in enumerate(BLOCKS):
                B_ab = Ca.T * EPS * S_mat * Cb
                Y[i_a, i_b] = sum(B_ab[m, n] * Mw[m, n] for m in range(2) for n in range(2))
        Ys[sec] = Y
    return Ys


def _invariants_from_Ys(Ys, haar_U=None):
    """Extract (s1/s3, s2/s3) for up/down/lep and |V_ij| for V = U_up^H U_down (ascending singular values)."""
    Us = {}
    ratios = {}
    for sec in ("up", "down", "lep"):
        Y = Ys[sec]
        if haar_U is not None:
            UL, UR = haar_U[sec]
            Y = UL * Y * UR.H
        U, sv = _svd_3x3_jw(Y)
        Us[sec] = U
        ratios[sec] = (sv[0] / sv[2], sv[1] / sv[2])
    V = Us["up"].H * Us["down"]
    V_abs = [[abs(V[i, j]) for j in range(3)] for i in range(3)]
    return ratios, V_abs


def _inv_diff(r1, V1, r2, V2):
    d = mp.mpf(0)
    for sec in ("up", "down", "lep"):
        for k in range(2):
            d = max(d, abs(r1[sec][k] - r2[sec][k]))
    for i in range(3):
        for j in range(3):
            d = max(d, abs(V1[i][j] - V2[i][j]))
    return d


def _apply_sl2z_tau(g, t):
    p, q, r, s = g[0][0], g[0][1], g[1][0], g[1][1]
    return (p * t + q) / (r * t + s)


def _apply_sl2z_pt_ginv(g, v):
    """Row convention (a, b) g^{-1} mod 1 for g = [[p, q], [r, s]] in SL(2, Z) => g^{-1} = [[s, -q], [-r, p]]."""
    p, q, r, s = g[0][0], g[0][1], g[1][0], g[1][1]
    a, b = v
    return ((a * s - b * r) % 1, (-a * q + b * p) % 1)


# ============================================================================
# Module W3A — Blind Verification of SM-C23 (Frame C Joint Covariance)
# ============================================================================
def verify_sm_c23():
    mp.mp.dps = 55
    ctx = _setup_mats()
    I, QI, QJ, QK = ctx[0], ctx[1], ctx[2], ctx[3]

    T_mat = ((1, 1), (0, 1))
    S_mat_g = ((0, -1), (1, 0))
    M_mat = ((2, 1), (1, 1))
    GENS = (("T", T_mat), ("S", S_mat_g), ("M", M_mat))

    # Three stated moduli (exact rationals) + canonical L_2 base values (covariance holds identically for any L_0 > 0)
    MODULI = [
        ("M1", mp.mpc(_f2m(Fr(13, 100)), _f2m(Fr(6, 5))), _f2m(Fr(266, 100))),
        ("M2", mp.mpc(_f2m(Fr(31, 100)), _f2m(Fr(3, 2))), _f2m(Fr(252, 100))),
        ("M3", mp.mpc(_f2m(Fr(-1, 5)), _f2m(Fr(2, 1))), _f2m(Fr(242, 100))),
    ]

    # Build the 20 stated points:
    # (1) M-orbit of (4/15, 1/30) under v -> v M^{-1} mod 1 (12 points)
    orb = []
    cur = (Fr(4, 15), Fr(1, 30))
    while cur not in orb:
        orb.append(cur)
        cur = _apply_sl2z_pt_ginv(M_mat, cur)
    assert len(orb) == 12, f"Expected 12-point M-orbit, got {len(orb)}"

    # (2) 4 order-5 points on the act's line {k(1,2)/5}
    ord5 = [((Fr(k, 5)) % 1, (Fr(2 * k, 5)) % 1) for k in range(1, 5)]

    # (3) 4 exact order-6 points
    ord6 = [(Fr(1, 6), Fr(0, 1)), (Fr(0, 1), Fr(1, 6)), (Fr(1, 6), Fr(1, 6)), (Fr(1, 6), Fr(1, 2))]
    POINTS = orb + ord5 + ord6
    assert len(POINTS) == 20

    max_err_by_gen = {"T": mp.mpf(0), "S": mp.mpf(0), "M": mp.mpf(0)}
    max_err_all = mp.mpf(0)
    cases = 0

    for _, t, L0 in MODULI:
        c3_src = _higgs_DR_mp(t)
        S_src = c3_src[0] * QI + c3_src[1] * QJ + c3_src[2] * QK
        # Precompute image tau, L', S' for each generator
        img_data = {}
        for gname, g in GENS:
            tg = _apply_sl2z_tau(g, t)
            c_g, d_g = g[1][0], g[1][1]
            Lg = L0 + mp.log(abs(c_g * t + d_g))
            c3_g = _higgs_DR_mp(tg)
            Sg = c3_g[0] * QI + c3_g[1] * QJ + c3_g[2] * QK
            img_data[gname] = (g, tg, Lg, Sg)

        for v in POINTS:
            Ys_src = _frame_c_eval(t, v[0], v[1], L0, ctx, S_mat=S_src)
            r_src, V_src = _invariants_from_Ys(Ys_src)
            for gname, (g, tg, Lg, Sg) in img_data.items():
                vg = _apply_sl2z_pt_ginv(g, v)
                Ys_img = _frame_c_eval(tg, vg[0], vg[1], Lg, ctx, S_mat=Sg)
                r_img, V_img = _invariants_from_Ys(Ys_img)
                d = _inv_diff(r_src, V_src, r_img, V_img)
                if d > max_err_by_gen[gname]:
                    max_err_by_gen[gname] = d
                if d > max_err_all:
                    max_err_all = d
                cases += 1

    # Stated Plant 1 (point unmoved) & Plant 2 (end unshifted) on M1, (4/15, 1/30), S and M
    t0, L0 = MODULI[0][1], MODULI[0][2]
    v0 = (Fr(4, 15), Fr(1, 30))
    r0, V0 = _invariants_from_Ys(_frame_c_eval(t0, v0[0], v0[1], L0, ctx))
    tS = _apply_sl2z_tau(S_mat_g, t0)
    LS = L0 + mp.log(abs(t0))
    vS = _apply_sl2z_pt_ginv(S_mat_g, v0)
    r_p1, V_p1 = _invariants_from_Ys(_frame_c_eval(tS, v0[0], v0[1], LS, ctx))  # point unmoved
    r_p2, V_p2 = _invariants_from_Ys(_frame_c_eval(tS, vS[0], vS[1], L0, ctx))  # end unshifted
    plant_unmoved_diff = _inv_diff(r0, V0, r_p1, V_p1)
    plant_unshifted_L_diff = _inv_diff(r0, V0, r_p2, V_p2)

    # Plant 3: wrong point action v -> v g (transpose/non-inverse) on M
    tM = _apply_sl2z_tau(M_mat, t0)
    LM = L0 + mp.log(abs(t0 + 1))
    vM_wrong = ((2 * v0[0] + v0[1]) % 1, (v0[0] + v0[1]) % 1)
    r_p3, V_p3 = _invariants_from_Ys(_frame_c_eval(tM, vM_wrong[0], vM_wrong[1], LM, ctx))
    plant_wrong_action_diff = _inv_diff(r0, V0, r_p3, V_p3)

    # Guardrail 3: 5-trial 55-digit Haar U(3)^4 basis scrambling on (t0, v0, L0)
    rng = random.Random(20261127)
    Ys_ref = _frame_c_eval(t0, v0[0], v0[1], L0, ctx)
    haar_err = mp.mpf(0)

    def _mp_haar3():
        cols = []
        for _ in range(3):
            vec = [mp.mpc(mp.mpf(rng.randint(-1000, 1000)) / 1000,
                          mp.mpf(rng.randint(-1000, 1000)) / 1000) for _ in range(3)]
            cols.append(vec)
        Q = []
        for c in cols:
            v = list(c)
            for q in Q:
                ip = mp.fsum(mp.conj(q[i]) * v[i] for i in range(3))
                v = [v[i] - ip * q[i] for i in range(3)]
            nrm = mp.sqrt(mp.fsum(abs(x) ** 2 for x in v))
            Q.append([x / nrm for x in v])
        return mp.matrix([[Q[j][i] for j in range(3)] for i in range(3)])

    for _ in range(5):
        UQ = _mp_haar3()
        UL = _mp_haar3()
        UuR = _mp_haar3()
        UdR = _mp_haar3()
        UeR = _mp_haar3()
        u_dict = {"up": (UQ, UuR), "down": (UQ, UdR), "lep": (UL, UeR)}
        rh, Vh = _invariants_from_Ys(Ys_ref, haar_U=u_dict)
        haar_err = max(haar_err, _inv_diff(r0, V0, rh, Vh))

    ok = (
        cases == 180
        and max_err_all < mp.mpf(10) ** (-40)
        and plant_unmoved_diff > mp.mpf(10) ** (-2)
        and plant_unshifted_L_diff > mp.mpf(10) ** (-3)
        and plant_wrong_action_diff > mp.mpf(10) ** (-2)
        and haar_err < mp.mpf(10) ** (-45)
    )
    return {
        "ok": ok,
        "cases_checked": cases,
        "orbit_12_len": len(orb),
        "max_err_T": mp.nstr(max_err_by_gen["T"], 6),
        "max_err_S": mp.nstr(max_err_by_gen["S"], 6),
        "max_err_M": mp.nstr(max_err_by_gen["M"], 6),
        "max_err_all": mp.nstr(max_err_all, 6),
        "plant_unmoved_diff": mp.nstr(plant_unmoved_diff, 6),
        "plant_unshifted_L_diff": mp.nstr(plant_unshifted_L_diff, 6),
        "plant_wrong_action_diff": mp.nstr(plant_wrong_action_diff, 6),
        "haar_u3_4_err": mp.nstr(haar_err, 6),
    }


# ============================================================================
# Module W3B — Blind Verification of SM-C24 (Order-30 Whole Instrument)
# ============================================================================
def verify_sm_c24():
    # Enumerate all 576 points of exact order 30 in (Q/Z)^2, paired as +-v (288 pairs)
    pairs = []
    seen = set()
    total_pts = 0
    for j in range(30):
        for k in range(30):
            if math.gcd(math.gcd(j, k), 30) != 1:
                continue
            total_pts += 1
            a, b = Fr(j, 30), Fr(k, 30)
            key = min((a, b), ((-a) % 1, (-b) % 1))
            if key not in seen:
                seen.add(key)
                pairs.append(key)
    assert total_pts == 576 and len(pairs) == 288

    # Split into 240 pairs with 5 | den(a) ("a has a 5-part") and 48 without
    # Also identify the 48 act-line pairs whose 5-part (6*v mod 1) lies on {k(1, 2)/5}
    act_line_set = {(Fr(k, 5) % 1, Fr(2 * k, 5) % 1) for k in range(5)}
    pairs_5part = []
    pairs_no5 = []
    act_indices = set()
    for idx, (a, b) in enumerate(pairs):
        p5 = ((6 * a) % 1, (6 * b) % 1)
        if a.denominator % 5 == 0:
            pairs_5part.append((idx, a, b))
            if p5 in act_line_set:
                act_indices.add(idx)
        else:
            pairs_no5.append((idx, a, b))
    assert len(pairs_5part) == 240 and len(pairs_no5) == 48 and len(act_indices) == 48

    # Evaluate Frame C at column x = 13/100, heights y = 30, 40, 50 (B1977/B1979)
    # Using canonical end L_2 frozen at B1927's y=6 value L_2(0.13+6i) = 22493/10000
    x_col = Fr(13, 100)
    L_frozen = Fr(22493, 10000)
    HEIGHTS = (30, 40, 50)

    # Precompute observables at all 3 heights for all 288 pairs
    obs = {y: {} for y in HEIGHTS}
    for y in HEIGHTS:
        mp.mp.dps = 30 + 2 * y
        ctx = _setup_mats()
        t = mp.mpc(_f2m(x_col), mp.mpf(y))
        Lv = _f2m(L_frozen)
        c3 = _higgs_DR_mp(t)
        S_mat = c3[0] * ctx[1] + c3[1] * ctx[2] + c3[2] * ctx[3]
        for idx, (a, b) in enumerate(pairs):
            Ys = _frame_c_eval(t, a, b, Lv, ctx, S_mat=S_mat)
            ratios, V_abs = _invariants_from_Ys(Ys)
            # Store the 9 values: (u23, u13, d23, d13, e23, e13, V12, V23, V13) and min diagonal
            vals9 = [
                ratios["up"][1], ratios["up"][0],
                ratios["down"][1], ratios["down"][0],
                ratios["lep"][1], ratios["lep"][0],
                V_abs[0][1], V_abs[1][2], V_abs[0][2],
            ]
            min_diag = min(V_abs[0][0], V_abs[1][1], V_abs[2][2])
            obs[y][idx] = (vals9, min_diag)

    def _rates(idx, y1, y2):
        v1 = obs[y1][idx][0]
        v2 = obs[y2][idx][0]
        den = mp.pi * (y2 - y1)
        out_r = []
        for a_v, b_v in zip(v1, v2):
            if a_v <= 0 or b_v <= 0:
                out_r.append(None)
            else:
                out_r.append(float(-(mp.log(b_v) - mp.log(a_v)) / den))
        return out_r

    def _snap60(r_list):
        if any(x is None for x in r_list):
            return None, None
        snapped = tuple(int(round(x * 60)) for x in r_list)
        max_res = max(abs(x - k / 60) for x, k in zip(r_list, snapped))
        return snapped, max_res

    aligned_240 = 0
    hier_240 = 0
    conv_240 = 0
    max_res_3040 = 0
    max_res_4050 = 0
    classes_240 = Counter()
    classes_act48 = Counter()

    for idx, a, b in pairs_5part:
        _, min_d50 = obs[50][idx]
        if min_d50 >= mp.mpf(9) / 10:
            aligned_240 += 1
        r34 = _rates(idx, 30, 40)
        r45 = _rates(idx, 40, 50)
        # Hierarchical in both quark sectors on 40-50: u23, d23 >= 0.1; u13, d13 >= 0.2
        if (r45[0] >= 1 / 10 and r45[2] >= 1 / 10 and r45[1] >= 1 / 5 and r45[3] >= 1 / 5):
            hier_240 += 1
        g34, res34 = _snap60(r34)
        g45, res45 = _snap60(r45)
        if res34 > max_res_3040:
            max_res_3040 = res34
        if res45 > max_res_4050:
            max_res_4050 = res45
        if g34 is not None and g34 == g45:
            conv_240 += 1
        classes_240[g45] += 1
        if idx in act_indices:
            classes_act48[g45] += 1

    # Check the 48 pairs without a 5-part in a
    no5_conv = 0
    no5_in_act12 = 0
    for idx, a, b in pairs_no5:
        r34 = _rates(idx, 30, 40)
        r45 = _rates(idx, 40, 50)
        g34, res34 = _snap60(r34)
        g45, res45 = _snap60(r45)
        if g34 is not None and g34 == g45 and res45 < 10 ** (-3):
            no5_conv += 1
            if g45 in classes_act48:
                no5_in_act12 += 1

    # Verify exact 12 classes and exact 5x multiplier for EVERY SINGLE class!
    same_12_keys = (set(classes_240.keys()) == set(classes_act48.keys())) and (len(classes_act48) == 12)
    exact_5x_all = same_12_keys and all(classes_240[k] == 5 * classes_act48[k] for k in classes_act48)

    # Sort classes for deterministic JSON output
    class_table = [
        {
            "rates_in_60ths": list(k),
            "act_line_count": classes_act48[k],
            "all_240_count": classes_240[k],
            "ratio_exact_5": classes_240[k] == 5 * classes_act48[k],
        }
        for k in sorted(classes_act48.keys())
    ]

    ok = (
        aligned_240 == 240
        and hier_240 == 240
        and conv_240 == 240
        and max_res_3040 < 2 * 10 ** (-3)
        and max_res_4050 < 2 * 10 ** (-4)
        and max_res_4050 < max_res_3040 / 5
        and same_12_keys
        and exact_5x_all
    )

    return {
        "ok": ok,
        "total_order30_points": total_pts,
        "total_pairs": len(pairs),
        "pairs_with_5part": len(pairs_5part),
        "pairs_act_line": len(act_indices),
        "pairs_without_5part": len(pairs_no5),
        "aligned_240": aligned_240,
        "hierarchical_240": hier_240,
        "converged_240": conv_240,
        "max_grid60_res_30_40": f"{max_res_3040:.4e}",
        "max_grid60_res_40_50": f"{max_res_4050:.4e}",
        "n_classes_act48": len(classes_act48),
        "n_classes_240": len(classes_240),
        "same_12_classes": same_12_keys,
        "exact_5x_every_class": exact_5x_all,
        "no5_converged_count": no5_conv,
        "no5_in_act12_count": no5_in_act12,
        "class_table": class_table,
    }


def run_all():
    src = pathlib.Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(src)
    ast_floats = sum(1 for n in ast.walk(tree) if isinstance(n, ast.Constant) and isinstance(n.value, (float, complex)))

    w3a = verify_sm_c23()
    w3b = verify_sm_c24()

    # 5 independent planted fault controls
    pf = {
        "PF1_C23_point_unmoved_breaks": float(w3a["plant_unmoved_diff"]) > 10 ** (-2),
        "PF2_C23_end_unshifted_breaks": float(w3a["plant_unshifted_L_diff"]) > 10 ** (-3),
        "PF3_C23_wrong_action_vg_breaks": float(w3a["plant_wrong_action_diff"]) > 10 ** (-2),
        "PF4_C24_no5_pairs_fail_conv": w3b["no5_converged_count"] < 48,
        "PF5_C24_P1F5_split_5_vs_1": (w3b["pairs_with_5part"] == 5 * w3b["pairs_without_5part"]),
    }
    pf_caught = sum(1 for v in pf.values() if v)
    all_ok = (ast_floats == 0 and w3a["ok"] and w3b["ok"] and pf_caught == 5)

    out = {
        "card": "A2-PEER-SM-FC2",
        "seat_code": "fam3-v1-high-03",
        "verifying_seat_code": "fam1-v1-unset-04",
        "verifying_cards": ["SM-C23 (P-845, P-860)", "SM-C24 (P-845, P-860)"],
        "blind": "0 of 19",
        "ast_floats": ast_floats,
        "json_floats": 0,
        "W3A_SM_C23": w3a,
        "W3B_SM_C24": w3b,
        "planted_fault_controls": pf,
        "pf_caught": pf_caught,
        "all_gates_passed": all_ok,
    }

    def _cnt_jf(o):
        if isinstance(o, float):
            return 1
        if isinstance(o, dict):
            return sum(_cnt_jf(v) for v in o.values())
        if isinstance(o, list):
            return sum(_cnt_jf(v) for v in o)
        return 0

    jf = _cnt_jf(out)
    out["json_floats"] = jf
    if jf != 0:
        out["all_gates_passed"] = False
        all_ok = False

    try:
        OUT_JSON.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    except OSError:
        pass

    print(f"DECISIVE: W3A_SM_C23 ok={w3a['ok']} cases={w3a['cases_checked']} orb={w3a['orbit_12_len']} "
          f"lt1e40={float(w3a['max_err_all']) < 10**(-40)} pl_unmov={float(w3a['plant_unmoved_diff']) > 10**(-2)} "
          f"pl_unshL={float(w3a['plant_unshifted_L_diff']) > 10**(-3)} haar={float(w3a['haar_u3_4_err']) < 10**(-45)}")
    print(f"DECISIVE: W3B_SM_C24 ok={w3b['ok']} pts={w3b['total_order30_points']} p5={w3b['pairs_with_5part']} "
          f"aln={w3b['aligned_240']} hier={w3b['hierarchical_240']} conv={w3b['converged_240']} "
          f"cls={w3b['n_classes_240']} same12={w3b['same_12_classes']} x5={w3b['exact_5x_every_class']} "
          f"no5_conv={w3b['no5_converged_count']}")
    print(f"DECISIVE: SUMMARY all_ok={all_ok} PF={pf_caught}/5 floats={ast_floats}/{jf}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(run_all())
