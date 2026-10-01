#!/usr/bin/env python3
"""The class index of a module of a level given numerically (mpmath, 60 digits): ranks by singular values.
Module: matrices h[1], h[2] for x, y and T for the meridian, with T h[g] T^-1 = h(Phi(g)).
  Z^1 = cocycles (z_x, z_y, z_t);  B^1 = coboundaries;  h^1 = dim Z^1 - dim B^1;
  interior classes n(V): cocycles whose restriction to the peripheral group <t, [x,y]> is a coboundary there, modulo B^1.
  I(V) = n(V) - n(V*)."""
import curve_engine as ce
from mpmath import mp, mpf, mpc, matrix, zeros, eye, inverse, svd_c, nstr
TOL = mpf(10) ** (-25)
def nullity(M):
    if M.rows == 0: return M.cols, None
    if M.rows < M.cols:
        P = zeros(M.cols, M.cols)
        for i in range(M.rows):
            for j in range(M.cols): P[i, j] = M[i, j]
        M = P
    S = svd_c(M, compute_uv=False); sv = sorted([abs(S[i]) for i in range(len(S))]); top = sv[-1] if sv else mpf(1)
    small = [s for s in sv if s < TOL * max(top, 1)]; gap = (min([s for s in sv if s >= TOL * max(top, 1)] or [mpf(0)]), max(small or [mpf(0)]))
    return len(small), gap
def block(rows):
    """rows: list of lists of matrices (same row heights) -> one matrix"""
    R = sum(r[0].rows for r in rows); C = sum(m.cols for m in rows[0]); M = zeros(R, C); i0 = 0
    for r in rows:
        j0 = 0
        for m in r:
            for i in range(m.rows):
                for j in range(m.cols): M[i0 + i, j0 + j] = m[i, j]
            j0 += m.cols
        i0 += r[0].rows
    return M
def data(Phi, h, T):
    n = T.rows; I = eye(n); O = zeros(n)
    X, Y = h[1], h[2]; Xi, Yi = inverse(X), inverse(Y)
    xx, xy, PX = ce.fox(Phi[1], h); yx, yy, PY = ce.fox(Phi[2], h)
    for (g, P) in ((X, PX), (Y, PY)):
        e = T * g * inverse(T) - P; assert max(abs(e[a, b]) for a in range(n) for b in range(n)) < mpf(10) ** (-25), "not a module"
    lam = X * Y * Xi * Yi
    coc = block([[T - xx, -xy, I - PX], [-yx, T - yy, I - PY]])                         # unknowns (z_x, z_y, z_t)
    lamrow = [I - X * Y * Xi, X - lam, O]                                               # z(lambda)
    h0 = nullity(block([[X - I], [Y - I], [T - I]]))[0]
    t0 = nullity(block([[T - I], [lam - I]]))[0]
    dimZ, gapZ = nullity(coc)
    big = block([[T - xx, -xy, I - PX, O], [-yx, T - yy, I - PY, O], [O, O, I, -(T - I)], lamrow + [-(lam - I)]])     # unknowns (z, v)
    D, gapD = nullity(big)
    h1 = dimZ - (n - h0); nint = D - t0 - (n - h0)
    return dict(n=n, h0=h0, t0=t0, h1=h1, interior=nint, gaps=(gapZ, gapD))
def dual(h, T):
    return {1: inverse(h[1]).T, 2: inverse(h[2]).T}, inverse(T).T
def index(Phi, h, T):
    a = data(Phi, h, T); hd, Td = dual(h, T); b = data(Phi, hd, Td)
    return a["interior"] - b["interior"], a, b
