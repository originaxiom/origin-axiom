"""Main's check of the seat's shifted Hecke formula (its cal17), cited in B1919 and not yet recomputed by main:

    integral over one period of E^(u)(z, s) ds  =  H(s) * sum over v in (u + Z^2)/<M> of |Q(v)|^(-s),

E^(u)(z, s) = sum over (m, n) in u + Z^2 of y^s |m z + n|^(-2s). At s = 2 both sides converge absolutely. The shift u must
be fixed by M modulo Z^2 (M u = u mod Z^2, columns) for the orbit sum to make sense; u is taken among the points of
order N that M fixes. Left: the lattice sum along one period of the geodesic of gamma = M^T. Right: orbit
representatives of u + Z^2 in the fundamental strip. Main's code, from hecke_s2.py's pieces."""
import math, sys, io, contextlib, itertools
import numpy as np
import hecke_s2 as H


def lhs_shift(M, u, s=2.0, nodes=96, Mmax=200, Nmax=3000):
    beta, betap, ell, _ = H.geodesic(M)
    x, w = np.polynomial.legendre.leggauss(nodes)
    t = ell / 2 * x
    z = (beta * 1j * np.exp(t) + betap) / (1j * np.exp(t) + 1)
    y = z.imag
    total = np.zeros(len(t))
    n = np.arange(-Nmax, Nmax + 1) + u[1]
    for k in range(-Mmax, Mmax + 1):
        m = k + u[0]
        lat = m * z[:, None] + n[None, :]
        a = np.abs(lat)
        term = np.where(a > 1e-14, a ** (-2 * s), 0.0)
        total += term.sum(1)
    return ell / 2 * np.sum(w * (y ** s) * total)


def rhs_shift(M, u, s=2.0, X=8000.0):
    Mf = np.array([[float(M[0][0]), float(M[0][1])], [float(M[1][0]), float(M[1][1])]])
    ev, R = np.linalg.eig(Mf)
    halve = ev.real.min() < 0
    G = Mf @ Mf if halve else Mf
    ev, R = np.linalg.eig(G); order = np.argsort(-np.abs(ev.real)); ev = ev.real[order]; R = R[:, order].real
    lam = ev[0]
    a, b, cc, d = (int(x) for x in (M[0][0], M[0][1], M[1][0], M[1][1]))
    D = (a + d) ** 2 - 4
    Q = lambda v0, v1: (b * v1 ** 2 + (a - d) * v0 * v1 - cc * v0 ** 2) / math.sqrt(D)
    Rinv = np.linalg.inv(R)
    q12 = (Q(*(R[:, 0] + R[:, 1])) - Q(*R[:, 0]) - Q(*R[:, 1]))
    A = math.sqrt(X / abs(q12)) * lam * 1.05; Bm = math.sqrt(X / abs(q12)) * 1.05
    corners = np.array([[sa * A, sb * Bm] for sa in (1, -1) for sb in (1, -1)]) @ R.T
    lo = np.floor(corners.min(0)).astype(int) - 2; hi = np.ceil(corners.max(0)).astype(int) + 2
    tot = 0.0
    for k0 in range(lo[0], hi[0] + 1):
        v0 = k0 + u[0]
        v1 = np.arange(lo[1], hi[1] + 1) + u[1]
        V = np.vstack([np.full(len(v1), v0), v1])
        al, be = Rinv @ V
        ok = (np.abs(al) > 1e-12) & (np.abs(be) > 1e-12)
        tt = np.where(ok, np.log(np.abs(al) / np.where(ok, np.abs(be), 1)), -1)
        q = q12 * al * be
        sel = ok & (tt >= 0) & (tt < 2 * math.log(lam)) & (np.abs(q) <= X)
        tot += float(np.sum(np.abs(q[sel]) ** (-s)))
    return tot / 2 if halve else tot


def fixed_shifts(M, N):
    a, b, c, d = (int(x) for x in (M[0][0], M[0][1], M[1][0], M[1][1]))
    out = []
    for i, j in itertools.product(range(N), repeat=2):
        if (i, j) == (0, 0):
            continue
        if ((a * i + b * j - i) % N == 0) and ((c * i + d * j - j) % N == 0):
            out.append((i / N, j / N))
    return out


if __name__ == "__main__":
    SL = H.B._sl()
    for st, k in [("+LR", 2), ("+LR", 3)]:
        eps = 1 if st[0] == "+" else -1
        with contextlib.redirect_stdout(io.StringIO()):
            N, F, S = SL.exact_slopes(eps, st[1:], k)
        M = H.B.abel_M(SL, eps, st[1:], k)
        us = fixed_shifts(M, N)[:4]
        for u in us:
            L = lhs_shift(M, u); R2 = rhs_shift(M, u, X=8000.0); R1 = rhs_shift(M, u, X=2000.0)
            print(st, k, "u", u, "lhs %.8f" % L, "H*sum %.8f" % (H.H(2) * R2), "rel %.1e" % (abs(L - H.H(2) * R2) / abs(L)),
                  "tail %.1e" % (abs(R2 - R1) / abs(R2)), flush=True)
