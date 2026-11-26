"""B2015, R1 and R2 (main, 2026-11-26; data-free): the six-move sum W (L, R, their inverses, X and X^-1; e_v -> e_m(v))
on the largest orbit over the common point (B1996's orbits_over_common_point, from its committed script).
R1: the largest eigenvalue below 6 (double, eigvalsh; W is symmetric) against 2 sqrt(5 + 4 cos(pi/M)); exactly: the factor
of F(x) = Res_t(m_c(t), x^2 - 20 - 16 t) vanishing at the value (m_c the minimal polynomial of cos(pi/M)) divides charpoly(W)
over Z (orbits up to 1176 points) or modulo three 62-bit primes (3000 points).
R2: mod 243; an orthonormal basis of the complement of the functions pulled back from mod 81 (scipy null_space); W's
eigenvalues there and on the whole orbit.
    python3 -B rate_law.py > rate_law_run.txt"""
import pathlib, time
import numpy as np, sympy as sp, flint, mpmath as mp
from scipy.linalg import null_space, eigh
ROOT = pathlib.Path(__file__).resolve().parents[3]
src = next(ROOT.glob("frontier/B1996_*/verification/tower_decay.py")).read_text().split("t0 = time.time()")[0]
ns = {}; exec(src, ns); orbits = ns["orbits_over_common_point"]
t0 = time.time()
log = lambda s: print(s + "  [%.0f s]" % (time.time() - t0), flush=True)
mp.mp.dps = 50
t = sp.Symbol("t"); x = sp.Symbol("x")


def largest_points(p, k):
    N, n, Lm, Rm, roots = orbits(p, k)
    r, c = np.unique(roots, return_counts=True); big = r[np.argmax(c)]; mem = np.nonzero(roots == big)[0]
    vals = np.arange(0, N, p)
    X, Y, Z = np.meshgrid(vals, vals, vals, indexing="ij"); on = (X * X + Y * Y + Z * Z - X * Y * Z) % N == 0
    pts = list(zip(X[on].ravel().tolist(), Y[on].ravel().tolist(), Z[on].ravel().tolist()))
    return N, [pts[i] for i in mem]


def six(N, pts):
    idx = {v: i for i, v in enumerate(pts)}; n = len(pts)
    mv = [lambda v: (v[0], v[2], (v[0] * v[2] - v[1]) % N), lambda v: (v[2], v[1], (v[1] * v[2] - v[0]) % N),
          lambda v: (v[0], (v[0] * v[1] - v[2]) % N, v[1]), lambda v: ((v[0] * v[1] - v[2]) % N, v[1], v[0]),
          lambda v: (v[1], (v[1] * v[2] - v[0]) % N, v[2]), lambda v: ((v[0] * v[2] - v[1]) % N, v[0], v[2])]
    W = np.zeros((n, n), dtype=np.int64)
    for i, v in enumerate(pts):
        for m in mv:
            W[idx[m(v)], i] += 1
    return W, idx


def val(M):
    return 2 * mp.sqrt(5 + 4 * mp.cos(mp.pi / M))


for p, k, M in ((3, 3, 3), (3, 4, 9), (5, 3, 5), (7, 3, 7), (5, 4, 25)):
    N, pts = largest_points(p, k)
    W, _ = six(N, pts)
    sym = (W == W.T).all()
    ev = np.linalg.eigvalsh(W.astype(float))
    below = max(e for e in ev if e < 6 - 1e-9)
    v = val(M)
    log("R1 mod %d (M = %d): %d points, W symmetric: %s; largest eigenvalue below 6 (double) %.15f; 2 sqrt(5 + 4 cos(pi/M)) = %s; difference %.1e" % (
        N, M, len(pts), sym, below, mp.nstr(v, 18), abs(below - float(v))))
    mc = sp.minimal_polynomial(sp.cos(sp.pi / M), t)
    F = sp.Poly(sp.resultant(sp.Poly(mc, t).as_expr(), x ** 2 - 20 - 16 * t, t), x)
    Fz = flint.fmpz_poly([int(c) for c in reversed(F.all_coeffs())])
    f = [g for g, e in Fz.factor()[1] if abs(mp.polyval(list(reversed([mp.mpf(int(c)) for c in g.coeffs()])), v)) < mp.mpf(10) ** -30][0]
    if len(pts) <= 1176:
        cp = flint.fmpz_mat(W.tolist()).charpoly(); mult = 0
        while True:
            q, r = divmod(cp, f)
            if r != 0:
                break
            cp = q; mult += 1
        log("    the factor of degree %d vanishing at the value divides charpoly(W) over Z with multiplicity %d" % (f.degree(), mult))
    else:
        oks = []; pr = int(sp.nextprime(1 << 61))
        for _ in range(3):
            oks.append(flint.nmod_mat(W.tolist(), pr).charpoly() % flint.nmod_poly([int(c) % pr for c in f.coeffs()], pr) == 0)
            pr = int(sp.nextprime(pr + 1000003))
        log("    the factor of degree %d vanishing at the value divides charpoly(W) modulo three 62-bit primes: %s" % (f.degree(), oks))

# R2
N, pts = largest_points(3, 5)
W, idx = six(N, pts)
n = len(pts)
lower = sorted({(a % 81, b % 81, c % 81) for a, b, c in pts}); li = {v: i for i, v in enumerate(lower)}
Q = np.zeros((n, len(lower)))
for i, (a, b, c) in enumerate(pts):
    Q[i, li[(a % 81, b % 81, c % 81)]] = 1.0
Q /= np.sqrt(Q.sum(axis=0))
B = null_space(Q.T)
Wf = W.astype(float)
evn = eigh(B.T @ Wf @ B, eigvals_only=True)
eva = eigh(Wf, eigvals_only=True)
v9 = float(val(9))
log("R2 mod 243: %d points, %d pulled back from mod 81, new fibre of dimension %d; the new fibre's largest eigenvalue %.15f (its smallest %.6f); the whole orbit's largest below 6: %.15f; 2 sqrt(5 + 4 cos(pi/9)) = %.15f; its multiplicity on the whole orbit (to 1e-8): %d, on the new fibre: %d" % (
    n, len(lower), B.shape[1], evn.max(), evn.min(), max(e for e in eva if e < 6 - 1e-9), v9, int((abs(eva - v9) < 1e-8).sum()), int((abs(evn - v9) < 1e-8).sum())))
