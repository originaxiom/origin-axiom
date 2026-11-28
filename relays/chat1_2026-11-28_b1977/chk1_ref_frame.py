#!/usr/bin/env python3
"""W-D2's referee's independent frame code (2026-11-19), copied unchanged except for MAIN, now read from argv.
Imports from main's frame_mp only: F_u (B1919 closed form), CR (canonical end table), te (triplet q-series),
B.SIXY / B.SECTORS (charges). Own: theta constants by direct sum, theta1 log-derivative by direct sum, eta by product,
ED hard-coded, the coupling, the SVD via the Hermitian eigenproblem of Y Y^H at higher precision, |V|, J, ratios."""
import sys, glob, math, json
from fractions import Fraction as Fr
import mpmath as mp

MAIN = __file__.rsplit("/", 1)[0] + "/main_tree"  # [copy: loader replaced, see MANIFEST.md]
pass  # [copy: loader replaced, see MANIFEST.md]
_a = sys.argv; sys.argv = ["x"]
import frame_mp as FM
sys.argv = _a
F_u, CR, te, B = FM.F_u, FM.CR, FM.te, FM.B
HALF = Fr(1, 2)


def q2m(q):
    return mp.mpf(q.numerator) / q.denominator


def theta_char(a, b, t):
    """theta[a,b](0,t) = sum_n exp(pi i (n+a)^2 t + 2 pi i (n+a) b), a, b exact rationals"""
    y = mp.im(t)
    N = int(math.sqrt(mp.mp.dps * 2.31 / (math.pi * float(y)))) + 4 + int(abs(a)) + 1
    A, Bb = q2m(a), q2m(b)
    tot = mp.mpc(0)
    for n in range(-N, N + 1):
        m = n + A
        tot += mp.exp(mp.pi * 1j * m * m * t + 2j * mp.pi * m * Bb)
    return tot


def th1_logder(z, t):
    """d/dz log theta[1/2,1/2](z,t) by direct sums"""
    y = mp.im(t)
    shift = int(abs(mp.im(z) / y)) + 2
    N = int(math.sqrt(mp.mp.dps * 2.31 / (math.pi * float(y)))) + 4 + shift
    num = mp.mpc(0); den = mp.mpc(0)
    for n in range(-N, N + 1):
        m = n + mp.mpf(1) / 2
        term = mp.exp(mp.pi * 1j * m * m * t + 2j * mp.pi * m * (z + mp.mpf(1) / 2))
        den += term
        num += 2j * mp.pi * m * term
    return num / den


def eta(t):
    q = mp.exp(2j * mp.pi * t)
    p = mp.mpc(1); qn = q
    while abs(qn) > mp.mpf(10) ** (-mp.mp.dps - 5):
        p *= (1 - qn); qn *= q
    return mp.exp(1j * mp.pi * t / 12) * p


I = mp.mpc(0, 1)
def M(rows):
    return mp.matrix(rows)


def basics():
    QI = M([[I, 0], [0, -I]]); QJ = M([[0, 1], [-1, 0]]); QK = QI * QJ
    ED = {"1": M([[0, 0.5], [-0.5, 0]]), "i": M([[0, 0.5j], [0.5j, 0]]), "j": M([[-0.5, 0], [0, -0.5]]),
          "k": M([[-0.5j, 0], [0, 0.5j]])}
    return QI, QJ, QK, ED


def check_ED():
    for s in ("1", "i", "j", "k"):
        for i in range(2):
            for j in range(2):
                assert complex(B.EDUAL[s][i][j]) == complex(basics()[3][s][i, j]), s


def point_setup(tx, ty, dps):
    mp.mp.dps = dps
    QI, QJ, QK, ED = basics()
    t = mp.mpc(q2m(tx), mp.mpf(ty))
    xr = ((float(tx) + 0.5) % 1.0) - 0.5
    L = mp.mpf(CR.canon(complex(xr, float(ty)))["L_2"])
    c3 = [te.ev(cc, t) for cc in te.B[1]]
    S = c3[0] * QI + c3[1] * QJ + c3[2] * QK
    St = c3[0].conjugate() * QI + c3[1].conjugate() * QJ + c3[2].conjugate() * QK   # B1964 L4: conj of coefficients
    St2 = QJ * mp.matrix([[mp.conj(S[i, j]) for j in range(2)] for i in range(2)]) * QJ.T
    assert mp.mnorm(St - St2, 1) < mp.mpf(10) ** (-dps + 8) * mp.mnorm(S, 1)
    return dict(t=t, y=mp.mpf(ty), L=L, c3=c3, S=S, St=St, QI=QI, QJ=QJ, QK=QK, ED=ED, t1p=2 * mp.pi * eta(t) ** 3)


def Mw(P, a, b, sec):
    t, y, L = P["t"], P["y"], P["L"]
    ql, qr = B.SIXY[B.SECTORS[sec][0]], B.SIXY[B.SECTORS[sec][1]]
    x0, x1 = ql * a, 2 * ql * b
    y0, y1 = qr * a, 2 * qr * b
    ap, am, bp, bm = x0 + y0, x0 - y0, (x1 + y1) / 2, (x1 - y1) / 2
    e = mp.exp(-2 * I * mp.pi * q2m(x0))
    kap = {"1": -I * e, "i": mp.mpc(-1), "j": -e, "k": I}
    cs = {"1": (ap + HALF, bp + HALF), "i": (ap + HALF, bp), "j": (ap, bp + HALF), "k": (ap, bp)}
    ds = {"1": (am + HALF, bm + HALF), "i": (am + HALF, bm), "j": (am, bm + HALF), "k": (am, bm)}
    out = mp.zeros(2, 2)
    for s in ("1", "i", "j", "k"):
        zc = (cs[s][0] - HALF) % 1 == 0 and (cs[s][1] - HALF) % 1 == 0
        zd = (ds[s][0] - HALF) % 1 == 0 and (ds[s][1] - HALF) % 1 == 0
        if zc or zd:
            continue
        R = kap[s] * theta_char(cs[s][0], cs[s][1], t) * theta_char(ds[s][0], ds[s][1], t) / P["t1p"]
        al, be = cs[s][0] - HALF, cs[s][1] - HALF
        z = q2m(al) * t + q2m(be)
        a0 = 2 * I * mp.pi * q2m(al) + th1_logder(z, t)
        c = F_u(al, be, t, y) + mp.pi * mp.log(y) - 2 * mp.pi * (mp.euler + mp.log(mp.pi)) - mp.pi * abs(a0) ** 2 * mp.exp(-2 * L)
        arg = 2 * mp.pi * L + c
        if arg > 0:
            out += mp.sqrt(arg) * R * P["ED"][s]
    return out


def Ycoup(P, H, W):
    EPS = P["QJ"]; blocks = [P["QJ"], P["QI"], P["QK"]]
    Y = mp.zeros(3, 3)
    for ia, Ca in enumerate(blocks):
        for ib, Cb in enumerate(blocks):
            K = Ca.T * EPS * H * Cb
            Y[ia, ib] = sum((K[m, n] * W[m, n] for m in range(2) for n in range(2)), mp.mpc(0))
    return Y


def left_sv(Y):
    """eigen of Y Y^H (Hermitian), ascending: light to heavy; returns masses and U"""
    G = Y * Y.H
    G = (G + G.H) / 2
    E, Q = mp.eighe(G)
    idx = sorted(range(3), key=lambda i: mp.re(E[i]))
    m = [mp.sqrt(max(mp.re(E[i]), 0)) for i in idx]
    U = mp.matrix(3, 3)
    for c, i in enumerate(idx):
        for r in range(3):
            U[r, c] = Q[r, i]
    return m, U


def analyse(P, Ws, Hm):
    res = {}; Us = {}
    for sec in ("up", "down", "lep"):
        m, U = left_sv(Ycoup(P, Hm[sec], Ws[sec]))
        Us[sec] = U
        res[sec] = (m[1] / m[2], m[0] / m[2])
    V = Us["up"].H * Us["down"]
    A = [[abs(V[i, j]) for j in range(3)] for i in range(3)]
    dmin = min(A[i][i] for i in range(3)); dmax = max(A[i][i] for i in range(3))
    cls = "aligned" if dmin >= 0.9 else ("deranged" if dmax <= 0.1 else "partial")
    J = mp.im(V[0, 1] * V[1, 2] * mp.conj(V[0, 2]) * mp.conj(V[1, 1]))
    lnD2 = abs(mp.log(res["lep"][0] / res["down"][0])); lnD1 = abs(mp.log(res["lep"][1] / res["down"][1]))
    return dict(r=res, A=A, cls=cls, dmin=dmin, J=J, lnD2=lnD2, lnD1=lnD1, hp=max(res["up"][0], res["down"][0]))


POINTS = {"mark": (Fr(2, 5), Fr(4, 5)), "twin": (Fr(1, 5), Fr(2, 5))}
