"""Exploratory (main, 2026-11-19; data-free): with B1736's coupling Y(h; u, w) = u h^T + h u^T - (u.h) 1 + w [h]_x and the
charge rule (up: conj(h) with channels (u_u, w_u); down: h with (u_d, w_d)), are there channels, free in C^4 per sector,
that give an aligned mixing (smallest diagonal |U_up^H U_down| >= 0.9) with both m2/m3 <= 1e-2, at a Higgs of reality r?
Objective: log10(max m2/m3) + 20 max(0, 0.9 - diag) + 20 max(0, -6 - log10(min m2/m3)) + 20 max(0, log10(max m1/m2) - log10(0.5)):
a set of channels with a value below -2 has diag >= 0.9 - 0.1 ... so the run reports the actual diag and ratios, and a
COUNTEREXAMPLE is a result with diag >= 0.9, both m2/m3 in [1e-6, 1e-2] and both m1/m2 <= 0.5 (three distinct non-zero masses)."""
import numpy as np
from scipy.optimize import minimize
def cross(v): return np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
def Y(h, u, w): return np.outer(u, h) + np.outer(h, u) - (u @ h) * np.eye(3) + w * cross(h)
def U(M):
    Uu, s, Vh = np.linalg.svd(M); o = np.argsort(s); return Uu[:, o], s[o]
def h_of(r):
    th = 0.5 * np.arccos(r); return np.array([np.cos(th), 1j * np.sin(th), 0])      # h.h = cos 2 th = r, |h| = 1
def obj(p, h):
    uu = p[0:3] + 1j * p[3:6]; wu = p[6] + 1j * p[7]; ud = p[8:11] + 1j * p[11:14]; wd = p[14] + 1j * p[15]
    Uu, su = U(Y(np.conj(h), uu, wu)); Ud, sd = U(Y(h, ud, wd))
    V = Uu.conj().T @ Ud; diag = min(abs(V[k, k]) for k in range(3))
    r2 = max(su[1] / su[2], sd[1] / sd[2]); r2min = min(su[1] / su[2], sd[1] / sd[2]); r1 = max(su[0] / max(su[1], 1e-300), sd[0] / max(sd[1], 1e-300))
    f = np.log10(max(r2, 1e-300)) + 20 * max(0.0, 0.9 - diag) + 20 * max(0.0, -6 - np.log10(max(r2min, 1e-300))) + 20 * max(0.0, np.log10(max(r1, 1e-300)) - np.log10(0.5))
    return f, diag, su[1] / su[2], sd[1] / sd[2], r1
rng = np.random.default_rng(11)
for r in (0.003, 0.01, 0.03):
    h = h_of(r); best = None
    for s in range(40):
        res = minimize(lambda p: obj(p, h)[0], rng.normal(size=16), method="Nelder-Mead", options={"maxiter": 6000, "maxfev": 6000, "xatol": 1e-8, "fatol": 1e-10})
        f, d, a, b, c1 = obj(res.x, h)
        if best is None or f < best[0]: best = (f, d, a, b, c1)
    f, d, a, b, c1 = best; ce = d >= 0.9 and 1e-6 <= a <= 1e-2 and 1e-6 <= b <= 1e-2 and c1 <= 0.5
    print("r %.2f: best objective %.3f: smallest diagonal %.3f, up m2/m3 %.1e, down m2/m3 %.1e, max m1/m2 %.2f -> %s" % (r, f, d, a, b, c1, "COUNTEREXAMPLE" if ce else "none"), flush=True)
