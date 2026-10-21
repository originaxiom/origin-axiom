"""B1653's own functions (main's code), copied verbatim for P-169's exploration."""

import itertools, json, pathlib
import mpmath as mp
import numpy as np

I = mp.mpc(0, 1)
mp.mp.dps = 40
QI = mp.matrix([[I, 0], [0, -I]]); QJ = mp.matrix([[0, 1], [-1, 0]]); QK = QI * QJ; ONE = mp.eye(2); EPS = QJ
BLOCKS = [QJ, QI, QK]
SIXY = {'Q': 1, 'u': -4, 'd': 2, 'L': -3, 'e': 6, 'H': 3}
SECTORS = {'up': ('Q', 'u'), 'down': ('Q', 'd'), 'lep': ('L', 'e')}
# ---------------------------------------------------------------- thetas (period-1), by jtheta
def th(n, u, t):
    q = mp.exp(I * mp.pi * t); x = mp.pi * u
    if n == 3: return mp.jtheta(3, x, q)
    if n == 4: return mp.jtheta(4, x, q)
    q4 = mp.exp(I * mp.pi * t / 4); s = x + mp.pi * t / 2
    if n == 2: return q4 * mp.exp(I * x) * mp.jtheta(3, s, q)
    return -I * q4 * mp.exp(I * x) * mp.jtheta(4, s, q)


def thc(a, b, u, T):
    return mp.exp(I * mp.pi * a * a * T + 2 * I * mp.pi * a * (u + b)) * th(3, u + a * T + b, T)


def th_series(n, u, t, N=30):
    e = lambda x: mp.exp(I * mp.pi * x); K = range(-N, N + 1); h = mp.mpf(1) / 2
    if n == 1: return -I * mp.fsum((-1) ** k * e(t * (k + h) ** 2 + (2 * k + 1) * u) for k in K)
    if n == 2: return mp.fsum(e(t * (k + h) ** 2 + (2 * k + 1) * u) for k in K)
    if n == 3: return mp.fsum(e(t * k * k + 2 * k * u) for k in K)
    return mp.fsum((-1) ** k * e(t * k * k + 2 * k * u) for k in K)


def eta(t): return mp.exp(I * mp.pi * t / 12) * mp.qp(mp.exp(2 * I * mp.pi * t))
def d1(t): return mp.diff(lambda u: th(1, u, t), 0)


# ---------------------------------------------------------------- bilinears, pairings, couplings
def bil(x, y, u, t, frame="record"):
    (ax, bx), (ay, by) = x, y
    T = 2 * t; t1 = th(1, u, t)
    den = I * mp.exp(-I * mp.pi * t / 2) * mp.exp(-I * mp.pi * u) * t1
    X0, X1 = thc(ax, bx, u, T), thc(ax, bx, u + t, T)
    Y0, Y1 = thc(ay, by, u, T), thc(ay, by, u + t, T)
    if frame == "record":
        p01, p10 = mp.exp(I * mp.pi * by), mp.exp(I * mp.pi * bx)
    else:                                                    # the control: the symmetric phase on both off-diagonals
        p01 = p10 = mp.exp(I * mp.pi * (bx + by) / 2)
    p11 = mp.exp(I * mp.pi * (bx + by))
    return mp.matrix([[X0 * Y0 / t1, p01 * X0 * Y1 / den], [p10 * X1 * Y0 / den, p11 * X1 * Y1 / th(1, u + t, t)]])


def pair_from(M, C):
    K = EPS * C
    return sum(K[m, n] * M[m, n] for m in range(2) for n in range(2))


def res_bil(x, y, t, rad=mp.mpf("0.02"), N=96):
    acc = mp.matrix(2, 2)
    for m in range(N):
        u = rad * mp.exp(2 * I * mp.pi * m / N); acc += bil(x, y, u, t) * u
    return acc / N


def coupling(S, M):
    Y = mp.matrix(3, 3)
    for a, Ca in enumerate(BLOCKS):
        for b, Cb in enumerate(BLOCKS):
            K = Ca.T * EPS * S * Cb
            Y[a, b] = sum(K[m, n] * M[m, n] for m in range(2) for n in range(2))
    return Y


def sv(Y):
    return sorted([abs(s) for s in mp.svd_c(Y, compute_uv=False)], reverse=True)


def left_null(Y):
    U, S, V = mp.svd_c(Y)
    k = min(range(3), key=lambda i: abs(S[i]))
    v = [U[r, k] for r in range(3)]; n = mp.sqrt(sum(abs(z) ** 2 for z in v))
    return [z / n for z in v], [abs(S[i]) for i in range(3)], U


def det2(M): return M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]
def mx(M): return max(abs(M[m, n]) for m in range(M.rows) for n in range(M.cols))
def wpt(x, t): return x[0] * t + x[1] / 2
def twist_of(w, t):
    a = mp.im(w) / mp.im(t); return (a, 2 * (mp.re(w) - a * mp.re(t)))


def line_w(psi1, psi2, t): return psi1 * t - psi2             # W59's holonomy phases (the reviewer's finding 4)


def field(wline, f, t): return twist_of(SIXY[f] * wline, t)


