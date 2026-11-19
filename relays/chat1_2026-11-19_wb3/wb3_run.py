#!/usr/bin/env python3
"""W-B3 (M78): frame D1 at the norms, and its cusp mixing on this seat's code. Data-free: frame outputs are computed and
printed under the author's ruling of 2026-11-15; no data is opened and nothing is set beside a measured number.

    python3 -I -u wb3_run.py <a checkout of main>    # main's checkout: read for B1927's and B1667's end tables only

Card: relays/cards/CHAT1_W-B3_frame_d1_at_the_norms_and_its_mixing.md (647429f10, rewrapped at e3be7373e), committed
before this script. Every definition, check and expectation is the card's; the labels below are its labels.

THE BUILD (extended precision, 30 + 2 Im tau digits):
  thetas      theta[al, be](u, T) = sum_n exp(i pi T (n + al)^2 + 2 pi i (n + al)(u + be)), summed over a window about
              the largest term, with the u-derivative term by term; theta_1 = -theta[1/2, 1/2].
  v           v(u) = (theta[al, be](u, 2 tau), -i theta[al + 1/2, be](u, 2 tau)), the characteristic of charge q at the
              point (a, b) being (q a, 2 q b).
  channels    n_s(u) = sum_mn (eps C_s)_mn v_x,m(u) v_y,n(u), C_s in (1, i, j, k) (W-F22's).
  D1          h = c q_H w, w = a tau + b; the pole at u = -h; R_s = n_s(-h) / theta_1'(0); zero if |n_s(-h)| is below
              10^(-dps/2) times the largest |v_x,m v_y,n|; a0 = n_s'(-h) / n_s(-h) - lambda (covariant), lambda =
              2 pi i c q_H a; the plain a0 (no connection) is the fork's variant.
  c_s         B1919's closed form (re-typed from B1940's frame_mp.F_u) at frame C''s channel characteristic,
              (ap, bp), (ap, bp - 1/2), (ap - 1/2, bp), (ap - 1/2, bp - 1/2) for 1, i, j, k, with ap = x'_0 + y'_0,
              bp = (x'_1 + y'_1) / 2 at q' = q - c q_H / 2; plus pi log y - 2 pi (euler + log pi).
  the end     this seat's W-F24 interpolation of B1927's grid and B1667's points, at (0.13, min(y, 6)).
  weight      u_s = sqrt(2 pi L + c_s - pi |a0_s|^2 exp(-2 L)) R_s, zero if the channel is zero or the argument <= 0.
  triplet     W-F22's thetanull form, R = (-t2 / (t3 t4), -t4 / (t2 t3), i t3 / (t2 t4)), with the tau-derivative term
              by term; av = R' / (2 pi i) + E2 R / 24. S = av_1 QI + av_2 QJ + av_3 QK; St = eps conj(S) eps^T.
  coupling    W-F22's contraction, blocks (QJ, QI, QK); U = left singular vectors, columns by ascending singular value;
              V = U_up^H U_down.
"""
import json
import math
import pathlib
import random
import sys
import time
from fractions import Fraction as Fr

import mpmath as mp
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
RELAYS = HERE.parent
MAIN = sys.argv[1] if len(sys.argv) > 1 else None
sys.path.insert(0, str(RELAYS / "chat1_2026-11-15_wb2"))
import wb2_stage4 as W4  # noqa: E402  (stage 4's double-precision D1 and the transcription; computes nothing on import)

W3, K = W4.W3, W4.K
NSD = K.NS
T0 = time.time()
H = Fr(1, 2)
SIXY = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6}
SECT = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}
QH = {s: -(SIXY[l] + SIXY[r]) for s, (l, r) in SECT.items()}
POINTS = [(Fr(i, 5), Fr(j, 5)) for i in range(5) for j in range(5) if (i, j) != (0, 0)]
UN = ("1", "i", "j", "k")
PAIRS = (("S", "S"), ("St", "St"), ("St", "S"), ("S", "St"))
X_RE = Fr(13, 100)


def say(*a):
    print(*a, flush=True)


def f2m(q):
    return mp.mpf(q.numerator) / q.denominator


# ---------------- algebra in mp
def setup():
    I = mp.mpc(0, 1)
    QI = mp.matrix([[I, 0], [0, -I]])
    QJ = mp.matrix([[0, 1], [-1, 0]])
    QK = QI * QJ
    U = {"1": mp.eye(2), "i": QI, "j": QJ, "k": QK}
    EPS = QJ
    EC = {s: EPS * U[s] for s in UN}
    G = mp.matrix(4, 4)
    for r, t in enumerate(UN):
        for c, s in enumerate(UN):
            G[r, c] = sum(EC[t][m, n] * U[s][m, n] for m in range(2) for n in range(2))
    Gi = G ** -1
    ED = {UN[a]: sum((Gi[b, a] * U[UN[b]] for b in range(4)), mp.zeros(2, 2)) for a in range(4)}
    return I, QI, QJ, QK, EPS, U, EC, ED, [QJ, QI, QK]


def theta(al, be, u, T):
    """theta[al, be](u, T) and its u-derivative; al, be mp numbers"""
    yT = mp.im(T)
    W = int(mp.sqrt(mp.mp.dps * 2.31 / (mp.pi * yT))) + 3
    n0 = int(mp.nint(-mp.im(u) / yT - al))
    s = d = mp.mpc(0)
    for n in range(n0 - W, n0 + W + 1):
        k = n + al
        e = mp.exp(1j * mp.pi * T * k * k + 2j * mp.pi * k * (u + be))
        s += e
        d += 2j * mp.pi * k * e
    return s, d


def th1(u, t):
    s, d = theta(mp.mpf(0.5), mp.mpf(0.5), u, t)
    return -s, -d


def vvec(ch, u, t):
    al, be = f2m(ch[0]), f2m(ch[1])
    T = 2 * t
    a0, a1 = theta(al, be, u, T)
    b0, b1 = theta(al + mp.mpf(0.5), be, u, T)
    return [a0, -1j * b0], [a1, -1j * b1]


def chars(q, a, b):
    return (q * a, 2 * q * b)


def channels(x, y, u, t, EC):
    vx, dvx = vvec(x, u, t)
    vy, dvy = vvec(y, u, t)
    n = {s: sum(EC[s][m, k] * vx[m] * vy[k] for m in range(2) for k in range(2)) for s in UN}
    dn = {s: sum(EC[s][m, k] * (dvx[m] * vy[k] + vx[m] * dvy[k]) for m in range(2) for k in range(2)) for s in UN}
    scale = max(abs(vx[m] * vy[k]) for m in range(2) for k in range(2))
    return n, dn, scale


def F_u(u1, u2, t, y):
    """B1919's closed form, re-typed (u1, u2 exact rationals)"""
    a = u1 % 1
    b = u2 % 1
    x = mp.re(t)
    if a != 0:
        first = -mp.pi * (2 * mp.log(2) + mp.log(y) + mp.digamma(f2m(a)) + mp.digamma(1 - f2m(a)))
        zero_row = 0
    else:
        first = mp.pi * (2 * mp.euler - 2 * mp.log(2) - mp.log(y))
        zero_row = y * mp.pi ** 2 / mp.sin(mp.pi * f2m(b)) ** 2 if b != 0 else mp.inf
    Kt = int(mp.mp.dps * 2.31 / (2 * mp.pi * y)) + 4
    tot = 0
    for k in range(-Kt, Kt + 1):
        m = f2m(a) + k
        if m == 0:
            continue
        w = mp.exp(-2 * mp.pi * abs(m) * y + 2j * mp.pi * (m * x + f2m(u2)))
        tot += (2 * mp.pi / abs(m)) * mp.re(w / (1 - w))
    return first + zero_row + tot


def char_of(qL, qR, a, b):
    """frame C's channel characteristics (u1, u2) for c_s, and the pairs (cs, ds) of the theta-constant rule"""
    x, y = chars(qL, a, b), chars(qR, a, b)
    ap, am = x[0] + y[0], x[0] - y[0]
    bp, bm = (x[1] + y[1]) / 2, (x[1] - y[1]) / 2
    cs = {"1": (ap + H, bp + H), "i": (ap + H, bp), "j": (ap, bp + H), "k": (ap, bp)}
    ds = {"1": (am + H, bm + H), "i": (am + H, bm), "j": (am, bm + H), "k": (am, bm)}
    return cs, ds


def is_half(c):
    return (c[0] - H) % 1 == 0 and (c[1] - H) % 1 == 0


def kron_a0(al, be, t):
    z = f2m(al) * t + f2m(be)
    s, d = th1(z, t)
    return 2j * mp.pi * f2m(al) + d / s


# ---------------- the triplet
def triplet(t):
    y = mp.im(t)
    N = int(mp.sqrt(mp.mp.dps * 2.31 / (mp.pi * y))) + 3
    t2 = d2 = t3 = d3 = t4 = d4 = mp.mpc(0)
    for n in range(-N, N + 1):
        e3 = mp.exp(1j * mp.pi * t * n * n)
        t3 += e3
        d3 += 1j * mp.pi * n * n * e3
        t4 += (-1) ** abs(n) * e3
        d4 += (-1) ** abs(n) * 1j * mp.pi * n * n * e3
        k = n + mp.mpf(0.5)
        e2 = mp.exp(1j * mp.pi * t * k * k)
        t2 += e2
        d2 += 1j * mp.pi * k * k * e2
    L2, L3, L4 = d2 / t2, d3 / t3, d4 / t4
    R = [-t2 / (t3 * t4), -t4 / (t2 * t3), 1j * t3 / (t2 * t4)]
    dR = [R[0] * (L2 - L3 - L4), R[1] * (L4 - L2 - L3), R[2] * (L3 - L2 - L4)]
    Q = mp.exp(2j * mp.pi * t)
    nmax = int(mp.mp.dps * 2.31 / (2 * mp.pi * y)) + 6
    E2 = 1 - 24 * mp.fsum(mp.fsum(dd for dd in range(1, n + 1) if n % dd == 0) * Q ** n for n in range(1, nmax))
    return [dr / (2j * mp.pi) + E2 * r / 24 for dr, r in zip(dR, R)]


# ---------------- the end (this seat's W-F24 construction)
def end_value(y):
    sys.path.insert(0, str(RELAYS / "chat1_2026-11-15_wf24"))
    src = (RELAYS / "chat1_2026-11-15_wf24" / "wf24_run.py").read_text()
    ns = {"__file__": str(RELAYS / "chat1_2026-11-15_wf24" / "wf24_run.py")}
    i0, i1 = src.index("def end_tables"), src.index("MAIN = os.environ")
    exec("import json, os\nimport numpy as np\n" + src[i0:i1], ns)
    lin, near, ymax = ns["end_tables"](MAIN)
    v = float(lin(float(X_RE), min(y, ymax)))
    return (v if np.isfinite(v) else float(near(float(X_RE), min(y, ymax)))), ymax


# ---------------- one sector at one point
def sector(t, y, a, b, sec, c, L, ALG, a0_mode="cov"):
    I, QI, QJ, QK, EPS, U, EC, ED, BL = ALG
    lf, rf = SECT[sec]
    qL, qR = SIXY[lf], SIXY[rf]
    w = f2m(a) * t + f2m(b)
    h = c * QH[sec] * w
    lam = 2j * mp.pi * c * QH[sec] * f2m(a)
    x, yy = chars(Fr(qL), a, b), chars(Fr(qR), a, b)
    n, dn, scale = channels(x, yy, -h, t, EC)
    _, t1p = th1(mp.mpc(0), t)
    qLp, qRp = Fr(qL) - Fr(c * QH[sec], 2), Fr(qR) - Fr(c * QH[sec], 2)
    cs, ds = char_of(qLp, qRp, a, b)
    tol = mp.mpf(10) ** (-mp.mp.dps / 2) * scale
    u, info = {}, {}
    for s in UN:
        zero = abs(n[s]) < tol
        info[s] = {"zero": zero, "rule_zero": is_half(cs[s]) or is_half(ds[s])}
        if zero:
            u[s] = 0
            continue
        R = n[s] / t1p
        a0 = dn[s] / n[s] - (lam if a0_mode == "cov" else 0)
        cn = F_u(cs[s][0] - H, cs[s][1] - H, t, y) + mp.pi * mp.log(y) - 2 * mp.pi * (mp.euler + mp.log(mp.pi))
        arg = 2 * mp.pi * L + cn - mp.pi * abs(a0) ** 2 * mp.exp(-2 * L)
        u[s] = mp.sqrt(arg) * R if arg > 0 else 0
    Mw = sum((u[s] * ED[s] for s in UN), mp.zeros(2, 2))
    return Mw, info


def couplings(Mw, S3, ALG):
    I, QI, QJ, QK, EPS, U, EC, ED, BL = ALG
    S = S3[0] * QI + S3[1] * QJ + S3[2] * QK
    conj = lambda A: mp.matrix([[mp.conj(A[i, j]) for j in range(2)] for i in range(2)])
    RD = {"S": S, "St": EPS * conj(S) * EPS.T}
    out = {}
    for rn, Sr in RD.items():
        out[rn] = mp.matrix([[sum(((Ca.T * EPS * Sr * Cb)[m, k] * Mw[m, k] for m in range(2) for k in range(2)),
                                  mp.mpc(0)) for Cb in BL] for Ca in BL])
    return out


def U_of(Y):
    Uu, Sv, Vv = mp.svd_c(Y)
    order = sorted(range(3), key=lambda i: -Sv[i])
    return mp.matrix([[Uu[r, order[2 - c]] for c in range(3)] for r in range(3)])


def point_table(t, y, a, b, c, L, S3, ALG, a0_mode="cov"):
    Y, zinfo = {}, {}
    for sec in SECT:
        Mw, info = sector(t, y, a, b, sec, c, L, ALG, a0_mode)
        Y[sec] = couplings(Mw, S3, ALG)
        zinfo[sec] = info
    Uo = {(sec, r): U_of(Y[sec][r]) for sec in SECT for r in ("S", "St")}
    res = {}
    for ru, rd in PAIRS:
        V = Uo[("up", ru)].H * Uo[("down", rd)]
        A = [[float(abs(V[i, j])) for j in range(3)] for i in range(3)]
        res[(ru, rd)] = (min(A[k][k] for k in range(3)), max(A[i][j] for i in range(3) for j in range(3) if i != j), A)
    lep = {}
    pat = lambda W: max(min(abs(float(abs(W[i, j])) - 1), float(abs(W[i, j]))) for i in range(3) for j in range(3))
    sv = lambda M: sorted(float(v) for v in mp.svd_c(M, compute_uv=False))
    for r in ("S", "St"):
        plain = pat(Uo[("lep", r)].H * Uo[("down", r)])
        trans = pat(Uo[("lep", r)].H * U_of(Y["down"][r].T))
        sl, sd = sv(Y["lep"][r]), sv(Y["down"][r])
        lep[r] = (plain, trans, max(abs(sl[k] / sl[2] - sd[k] / sd[2]) for k in range(3)))
    return res, lep, zinfo


def classify(mins):
    lo = min(mins)
    return "ALIGNED" if lo >= 0.9 else ("DERANGED" if lo < 0.1 else "PARTIAL")


# ---------------- Q1's checks in extended precision
def q1_checks(y, ALG, rng):
    mp.mp.dps = int(30 + 2 * y)
    t = mp.mpc(f2m(X_RE), y)
    I, QI, QJ, QK, EPS, U, EC, ED, BL = ALG
    e1 = e2 = e3 = 0.0
    zero_mismatch = 0
    for sec in SECT:
        lf, rf = SECT[sec]
        for c in (2, -2):
            for a, b in POINTS:
                w = f2m(a) * t + f2m(b)
                h = c * QH[sec] * w
                lam = 2j * mp.pi * c * QH[sec] * f2m(a)
                qL, qR = Fr(SIXY[lf]), Fr(SIXY[rf])
                qLp, qRp = qL - Fr(c * QH[sec], 2), qR - Fr(c * QH[sec], 2)
                x, yy = chars(qL, a, b), chars(qR, a, b)
                xp, yp = chars(qLp, a, b), chars(qRp, a, b)
                # E1: K_D1(z - h) e^(-lam z) / K_C'(z), one constant over the entries and five z
                ref = None
                for _ in range(5):
                    z = mp.mpf(rng.uniform(-0.45, 0.45)) + mp.mpf(rng.uniform(-0.45, 0.45)) * t
                    vx, _ = vvec(x, z - h, t)
                    vy, _ = vvec(yy, z - h, t)
                    wx, _ = vvec(xp, z, t)
                    wy, _ = vvec(yp, z, t)
                    for m in range(2):
                        for k in range(2):
                            r = vx[m] * vy[k] * mp.exp(-lam * z) / (wx[m] * wy[k])
                            ref = r if ref is None else ref
                            e1 = max(e1, float(abs(r / ref - 1)))
                # E2, E3
                n1, dn1, sc1 = channels(x, yy, -h, t, EC)
                n2, dn2, sc2 = channels(xp, yp, mp.mpc(0), t, EC)
                tol1, tol2 = mp.mpf(10) ** (-mp.mp.dps / 2) * sc1, mp.mpf(10) ** (-mp.mp.dps / 2) * sc2
                rref = None
                for s in UN:
                    z1, z2 = abs(n1[s]) < tol1, abs(n2[s]) < tol2
                    if z1 != z2:
                        zero_mismatch += 1
                        continue
                    if z1:
                        continue
                    rr = n1[s] / n2[s]
                    rref = rr if rref is None else rref
                    e2 = max(e2, float(abs(rr / rref - 1)))
                    a0d, a0c = dn1[s] / n1[s] - lam, dn2[s] / n2[s]
                    e3 = max(e3, float(abs(a0d - a0c) / max(1, abs(a0c))))
    return e1, e2, e3, zero_mismatch


# ---------------- E4 in double precision (this seat's quadrature)
def cA_metric(x, y, t, R, h, a0cov, eps=1e-5, nth=96, ns_=64):
    from numpy.polynomial.legendre import leggauss
    br = NSD["vangles"](t)
    xg, wg = leggauss(nth)
    xs, ws = leggauss(ns_)
    tot = {s: 0.0 for s in NSD["UNITS"]}
    for a_, b_ in zip(br[:-1], br[1:]):
        th = 0.5 * (b_ - a_) * xg + 0.5 * (b_ + a_)
        wt = 0.5 * (b_ - a_) * wg
        hi = np.log(NSD["rmax_np"](th, t))
        lo = math.log(eps)
        sg = 0.5 * (hi - lo)[:, None] * xs[None, :] + 0.5 * (hi + lo)[:, None]
        w2 = 0.5 * (hi - lo)[:, None] * ws[None, :]
        rr = np.exp(sg)
        zz = rr * np.exp(1j * th)[:, None]
        P = W4.chan(x, y, -h + zz, t, h)
        m = np.exp(4 * np.pi * h.imag * zz.imag / t.imag)
        for s in NSD["UNITS"]:
            if abs(R[s]) > 1e-12:
                tot[s] += np.sum(wt[:, None] * w2 * np.abs(P[s] / R[s]) ** 2 * m * rr ** 2)
    return {s: (float(tot[s] - 2 * np.pi * math.log(1 / eps) + np.pi * eps ** 2 * abs(a0cov[s]) ** 2)
                if abs(R[s]) > 1e-12 and a0cov[s] is not None else None) for s in NSD["UNITS"]}


def e4_case(t, a, b, sec, cc):
    w = a * t + b
    lf, rf = K.SECT[sec]
    S3 = K.comps(t, 0.0, 0.0)
    S = S3[0] * K.QI + S3[1] * K.QJ + S3[2] * K.QK
    h = cc * K.QH[sec] * w
    lam = 2j * np.pi * cc * K.QH[sec] * a
    x, yy = K.twist_of(K.SIXY[lf] * w, t), K.twist_of(K.SIXY[rf] * w, t)
    R = W3.res_alt(x, yy, t, h)
    a0p = W4.a0_alt(x, yy, t, R, h)
    a0c = {s: (v - lam if v is not None else None) for s, v in a0p.items()}
    cm = cA_metric(x, yy, t, R, h, a0c)
    uDc = W4.weights(R, cm, a0c)
    uDp = W4.weights(R, cm, a0p)
    qs = (K.SIXY[lf] - cc * K.QH[sec] / 2, K.SIXY[rf] - cc * K.QH[sec] / 2)
    x2, y2 = K.twist_of(qs[0] * w, t), K.twist_of(qs[1] * w, t)
    R2 = NSD["residues"](x2, y2, t)
    uC = W4.weights(R2, NSD["cA"](x2, y2, t, R2), NSD["a0_of"](x2, y2, t, R2))
    with np.errstate(all="ignore"):
        rC = W4.ratios(NSD["coupling"](S, NSD["weighted_M"](uC)))
        dc = float(np.max(np.abs(W4.ratios(NSD["coupling"](S, NSD["weighted_M"](uDc))) / rC - 1)))
        dp = float(np.max(np.abs(W4.ratios(NSD["coupling"](S, NSD["weighted_M"](uDp))) / rC - 1)))
        dn = W4.both(t, a, b, sec, cc, True)
    # a coupling that vanishes (every weight's argument not positive) gives no ratio: counted, never dropped
    return [v if math.isfinite(v) else math.inf for v in (dc, dp, dn)]


def main():
    if MAIN is None:
        sys.exit("give a checkout of main (for B1927's and B1667's end tables)")
    out = {}
    say("W-B3: frame D1 at the norms, and its cusp mixing on this seat's code. Data-free.")
    rng = random.Random(20261119)

    # C2: the triplet
    mp.mp.dps = 33
    tq = mp.mpc(0.13, 1.7)
    S_new = triplet(tq)
    S_old = NSD["av"](tq)
    c2 = max(float(abs(p / q - 1)) for p, q in zip(S_new, S_old))
    say("C2 holds:", c2 < 1e-8, "| term-by-term triplet against W-F22's finite difference at 0.13 + 1.7i: %.2e" % c2)

    # C1 and C3: the closed form against the quadrature; Kronecker's a0; the zero channels
    ALG = None
    c1n = c1a = 0.0
    c3 = 0
    ncase = 0
    for y in (1.7, 2.9):
        mp.mp.dps = int(30 + 2 * y)
        ALG = setup()
        EC = ALG[6]
        t = mp.mpc(f2m(X_RE), y)
        tc = complex(float(X_RE), y)
        for sec in SECT:
            lf, rf = SECT[sec]
            for a, b in POINTS:
                x, yy = chars(Fr(SIXY[lf]), a, b), chars(Fr(SIXY[rf]), a, b)
                n, dn, sc = channels(x, yy, mp.mpc(0), t, EC)
                cs, ds = char_of(Fr(SIXY[lf]), Fr(SIXY[rf]), a, b)
                xd, yd = (float(x[0]), float(x[1])), (float(yy[0]), float(yy[1]))
                Rq = NSD["residues"](xd, yd, tc)
                cq = NSD["cA"](xd, yd, tc, Rq)
                tol = mp.mpf(10) ** (-mp.mp.dps / 2) * sc
                for s in UN:
                    z = abs(n[s]) < tol
                    rule = is_half(cs[s]) or is_half(ds[s])
                    c3 += z != rule
                    if z:
                        continue
                    cn = F_u(cs[s][0] - H, cs[s][1] - H, t, mp.mpf(y)) + mp.pi * mp.log(y) \
                        - 2 * mp.pi * (mp.euler + mp.log(mp.pi))
                    if cq[s] is not None:
                        c1n = max(c1n, abs(float(cn) - cq[s]))
                    c1a = max(c1a, float(abs(dn[s] / n[s] - kron_a0(cs[s][0] - H, cs[s][1] - H, t))))
                    ncase += 1
    say("C1 holds:", c1n < 1e-6 and c1a < 1e-20,
        "| closed form against the quadrature: %.2e; Laurent a0 against Kronecker's form: %.2e (%d channels)"
        % (c1n, c1a, ncase))
    say("C3 holds:", c3 == 0, "| numerical zeros against the theta-constant rule: %d mismatches" % c3)
    out["controls"] = {"C1_norm": c1n, "C1_a0": c1a, "C2": c2, "C3": c3}

    # Q1: E1 to E3
    q1 = {}
    for y in (1.7, 6.0, 30.0):
        mp.mp.dps = int(30 + 2 * y)
        ALG = setup()
        e1, e2, e3, zm = q1_checks(y, ALG, rng)
        q1[y] = (e1, e2, e3, zm)
        say("Q1 at height %4.1f (dps %d): E1 %.2e, E2 %.2e, E3 %.2e, zero channels that differ %d  [%.0f s]"
            % (y, mp.mp.dps, e1, e2, e3, zm, time.time() - T0))
    x1 = all(v[0] < 1e-20 and v[1] < 1e-20 and v[2] < 1e-20 and v[3] == 0 for v in q1.values())
    say("X1 holds:", x1)
    out["Q1"] = {str(k): v for k, v in q1.items()}

    # E4
    taus = [complex(0.13, 1.7), complex(-0.31, 1.25), complex(0.4, 1.2)]
    pts = [(0.4, 0.8), (0.2, 0.4)]
    e4 = {"cov": 0.0, "plain": 0.0, "neither": 0.0}
    e4_void = {"cov": 0, "plain": 0, "neither": 0}
    for cc in (2, -2):
        for sec in ("up", "down", "lep"):
            for a, b in pts:
                for t in taus:
                    dc, dp, dn = e4_case(t, a, b, sec, cc)
                    for key, val in (("cov", dc), ("plain", dp), ("neither", dn)):
                        if val == math.inf:
                            e4_void[key] += 1
                        else:
                            e4[key] = max(e4[key], val)
    x2 = e4["cov"] < 1e-6 and e4_void["cov"] == 0 and (e4["plain"] > 1e-3 or e4_void["plain"] > 0) \
        and e4["neither"] > 1e-2
    say("E4: D1 against frame C' (largest relative difference of s2/s1, s3/s1): metric and covariant a0 %.2e;"
        " metric and plain a0 %.2e; neither (stage 4) %.2e  [%.0f s]"
        % (e4["cov"], e4["plain"], e4["neither"], time.time() - T0))
    say("  cases whose coupling vanishes (no ratio), of 36: covariant %d, plain %d, neither %d"
        % (e4_void["cov"], e4_void["plain"], e4_void["neither"]))
    say("X2 holds:", x2)
    out["E4"] = {"largest": e4, "vanishing": e4_void}

    # Q2
    L, ymax = end_value(6.0)
    say("the end L at (0.13, %.1f): %.6f (the tables' top %.1f)" % (min(6.0, ymax), L, ymax))
    tables = {}
    for a0_mode in ("cov", "plain"):
        for c in (0, -2, 2):
            if a0_mode == "plain" and c == 0:
                continue
            for y in (6.0, 30.0):
                mp.mp.dps = int(30 + 2 * y)
                ALG = setup()
                t = mp.mpc(f2m(X_RE), y)
                S3 = triplet(t)
                Lm = mp.mpf(L)
                acc = {k: [] for k in PAIRS}
                lep = {"S": [], "St": []}
                zmis = nzero = 0
                for a, b in POINTS:
                    res, lp, zi = point_table(t, mp.mpf(y), a, b, c, Lm, S3, ALG, a0_mode)
                    for sec in zi:
                        for s in zi[sec]:
                            zmis += zi[sec][s]["zero"] != zi[sec][s]["rule_zero"]
                            nzero += zi[sec][s]["zero"]
                    for k in PAIRS:
                        acc[k].append(res[k][:2])
                    for r in lp:
                        lep[r].append(lp[r])
                tables[(a0_mode, c, y)] = (acc, lep)
                for k in PAIRS:
                    mins = [v[0] for v in acc[k]]
                    say("%-5s c = %+d  height %4.1f  up %-2s down %-2s: smallest diagonal |V| %.4e,"
                        " largest off-diagonal %.4e  %s"
                        % (a0_mode, c, y, k[0], k[1], min(mins), max(v[1] for v in acc[k]), classify(mins)))
                for r in ("S", "St"):
                    v = lep[r]
                    say("%-5s c = %+d  height %4.1f  leptons against down, reading %-2s: plain %.3e, transposed %.3e,"
                        " spectra %.3e" % (a0_mode, c, y, r, max(q[0] for q in v), max(q[1] for q in v),
                                           max(q[2] for q in v)))
                say("  zero channels %d; against the theta-constant rule at q': %d mismatches  [%.0f s]"
                    % (nzero, zmis, time.time() - T0))

    # C0, C4
    c0 = tables[("cov", 0, 6.0)][0]
    got = [(min(v[0] for v in c0[k]), max(v[1] for v in c0[k])) for k in (("S", "S"), ("St", "St"))]
    want = [(0.9932, 0.1161), (0.9752, 0.2215)]
    c0ok = all(float("%.4g" % g[i]) == w[i] for g, w in zip(got, want) for i in range(2))
    say("C0 holds:", c0ok, "| frame C at height 6: (S, S) %.4e %.4e; (St, St) %.4e %.4e" % (*got[0], *got[1]))
    worst4 = 0.0
    for a, b in POINTS[:2]:
        A = {}
        for extra in (0, 20):
            mp.mp.dps = int(30 + 2 * 30) + extra
            ALG = setup()
            t = mp.mpc(f2m(X_RE), 30)
            res, _, _ = point_table(t, mp.mpf(30), a, b, 2, mp.mpf(L), triplet(t), ALG, "cov")
            A[extra] = res
        for k in PAIRS:
            worst4 = max(worst4, max(abs(A[0][k][2][i][j] - A[20][k][2][i][j]) for i in range(3) for j in range(3)))
    say("C4 holds:", worst4 < 1e-15, "| |V| at 20 more digits, two points at height 30, c = +2: %.2e" % worst4)

    # X3, X4
    cls = {(c, y, k): classify([v[0] for v in tables[("cov", c, y)][0][k]]) for c in (2, -2) for y in (6.0, 30.0)
           for k in PAIRS}
    x3a = all(cls[(c, 30.0, k)] != "ALIGNED" and min(v[0] for v in tables[("cov", c, 30.0)][0][k]) < 1e-3
              for c in (2, -2) for k in PAIRS)
    x3b = all(sum(cls[(c, 6.0, k)] == "DERANGED" for k in PAIRS) == 3 and cls[(c, 6.0, ("St", "St"))] == "PARTIAL"
              for c in (2, -2))
    x3c = all(cls[(2, y, k)] == cls[(-2, y, k)] for y in (6.0, 30.0) for k in PAIRS)
    sst = {c: min(v[0] for v in tables[("cov", c, 6.0)][0][("St", "St")]) for c in (-2, 2)}
    x3d = float("%.3g" % sst[-2]) == 0.125 and float("%.3g" % sst[2]) == 0.126
    say("X3 holds:", x3a and x3b and x3c and x3d, "| height 30 none aligned, all below 1e-3: %s;"
        " height 6 three deranged and (St, St) partial: %s; signs agree: %s; (St, St) at 6: %.4f (c = -2),"
        " %.4f (c = +2): %s" % (x3a, x3b, x3c, sst[-2], sst[2], x3d))
    x4 = all(max(q[1] for q in tables[("cov", c, y)][1][r]) < 1e-10
             for c in (2, -2) for y in (6.0, 30.0) for r in ("S", "St"))
    say("X4 holds:", x4)
    out["tables"] = {"%s|%+d|%g" % key: {"%s,%s" % k: v for k, v in val[0].items()} for key, val in tables.items()}
    out["leptons"] = {"%s|%+d|%g" % key: val[1] for key, val in tables.items()}
    out["verdicts"] = {"C0": c0ok, "C1": c1n < 1e-6 and c1a < 1e-20, "C2": c2 < 1e-8, "C3": c3 == 0,
                       "C4": worst4 < 1e-15, "X1": x1, "X2": x2, "X3": x3a and x3b and x3c and x3d, "X4": x4}
    json.dump(out, open(HERE / "wb3_summary.json", "w"), indent=1, default=float)
    say("done  [%.0f s]" % (time.time() - T0))


if __name__ == "__main__":
    main()
