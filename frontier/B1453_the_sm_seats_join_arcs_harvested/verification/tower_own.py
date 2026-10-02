#!/usr/bin/env python3
"""sm:B1511 recomputed with main's own index code: on the n-fold cyclic cover of the figure-eight complement, the
background nu (x) rho_q (nu a character of the level, lambda its value on the level's meridian), the cocycles of the
level by linear algebra on the fibred presentation, the extension W1 = [[A, c], [0, 1]] and its class index."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import join_own as jo
ix = jo.ix
from mpmath import mp, mpf, mpc, matrix, eye, zeros, inverse, sqrt, svd_c, nstr, exp, pi
mp.dps = 60
def red(w):
    out = []
    for c in w:
        if out and out[-1] == -c: out.pop()
        else: out.append(c)
    return out
def compose(P, n):
    cur = {1: [1], 2: [2]}
    for _ in range(n):
        cur = {g: red(sum(((P[c] if c > 0 else [-d for d in reversed(P[-c])]) for c in cur[g]), [])) for g in (1, 2)}
    return cur
def wordm(w, h):
    r = eye(h[1].rows); hi = {1: inverse(h[1]), 2: inverse(h[2])}
    for c in w: r = r * (h[c] if c > 0 else hi[-c])
    return r
def level(q, n, nu, lam):
    """fibre matrices and meridian of nu (x) rho_q on the n-fold cover; nu = (nu(u0), nu(u1))"""
    g = jo.ballas(q, mpc(1)); h1, T1 = jo.fibred(g)
    Phi = compose(jo.PHI, n); h = {1: nu[0] * h1[1], 2: nu[1] * h1[2]}; T = lam * T1 ** n
    for gg in (1, 2):
        d = T * h[gg] * inverse(T) - wordm(Phi[gg], h)
        assert max(abs(d[i, j]) for i in range(4) for j in range(4)) < mpf(10) ** (-35), "nu is not a character of the level"
    return Phi, h, T
def cocycles(Phi, h, T):
    """classes of H^1(level; A): unknowns (c_x, c_y, c_t), the two relations t g t^-1 = Phi(g) on 5 x 5 extensions"""
    def ext(c):
        out = []
        for k, M in enumerate((h[1], h[2], T)):
            W = zeros(5, 5)
            for i in range(4):
                for j in range(4): W[i, j] = M[i, j]
                W[i, 4] = c[4 * k + i]
            W[4, 4] = 1; out.append(W)
        return {1: out[0], 2: out[1]}, out[2]
    M = matrix(8, 12)
    for j in range(12):
        c = [mpc(0)] * 12; c[j] = mpc(1); hh, TT = ext(c)
        for gi, gg in enumerate((1, 2)):
            D = TT * hh[gg] * inverse(TT) - wordm(Phi[gg], hh)
            for i in range(4): M[4 * gi + i, j] = D[i, 4]
    Z, rk, S = jo.null(M)
    Bm = matrix(12, 4)
    for j in range(4):
        v = zeros(4, 1); v[j] = 1
        for k, Mx in enumerate((h[1], h[2], T)):
            b = (Mx - eye(4)) * v
            for i in range(4): Bm[4 * k + i, j] = b[i]
    Ub, Sb, Vb = svd_c(Bm); rb = sum(1 for i in range(len(Sb)) if abs(Sb[i]) > mpf(10) ** (-30)); reps = []
    for zv in Z:
        Tm = matrix(12, 4 + len(reps) + 1)
        for i in range(12):
            for j in range(4): Tm[i, j] = Bm[i, j]
            for j, r in enumerate(reps): Tm[i, 4 + j] = r[i]
            Tm[i, 4 + len(reps)] = zv[i]
        U2, S2, V2 = svd_c(Tm)
        if sum(1 for i in range(len(S2)) if abs(S2[i]) > mpf(10) ** (-30)) > rb + len(reps): reps.append(zv)
    return reps, ext
def dual(Phi, h, T): return Phi, {1: inverse(h[1]).T, 2: inverse(h[2]).T}, inverse(T).T
def count(q, n, nu, lam, label):
    Phi, h, T = level(q, n, nu, lam); out = []
    for name, (P, hh, TT) in (("W1", (Phi, h, T)), ("W1[A*]", dual(Phi, h, T))):
        reps, ext = cocycles(P, hh, TT)
        if not reps: out.append("%s: h1(A) = 0" % name); continue
        hw, Tw = ext([reps[0][i] for i in range(12)]); I, a, b = ix.index(P, hw, Tw)
        out.append("%s: h1(A) = %d, index %+d (h1 %d/%d, interior %d/%d, kept %s dropped %s)" % (name, len(reps), I, a["h1"], b["h1"], a["interior"], b["interior"], nstr(a["gaps"][1][0], 2), nstr(a["gaps"][1][1], 2)))
    print("%-58s %s" % (label, " | ".join(out)), flush=True)
if __name__ == "__main__":
    s2 = sqrt(mpf(2)); q1 = 17 + 12 * s2; phi = (1 + sqrt(mpf(5))) / 2; w = exp(2j * pi / 3)
    count(q1, 1, (1, 1), mpc(-1), "level 1, q = 17+12 sqrt 2, lambda -1 (B1509)")
    count(q1, 3, (1, 1), mpc(-1), "level 3, the pullback, q = 17+12 sqrt 2, lambda -1")
    for q3 in (q1, 17 - 12 * s2):
        qq = q3 ** (mpf(1) / 3)
        for nu in ((-1, 1), (1, -1), (-1, -1)): count(qq, 3, nu, mpc(-1), "level 3, nu = %s, q^3 = %s, lambda -1" % (nu, nstr(q3, 8)))
    count(q1 ** (mpf(1) / 3), 3, (-1, 1), mpc(1), "level 3, nu = (-1, 1), same q, lambda +1 (control)")
    count(mpf(2), 3, (-1, 1), mpc(-1), "level 3, nu = (-1, 1), q = 2, lambda -1 (control)")
    for nu in ((w, 1), (1, w), (w, w), (w, w ** 2)): count(phi ** 4, 4, nu, mpc(1), "level 4, 3-torsion nu, q = phi^4, lambda +1")
