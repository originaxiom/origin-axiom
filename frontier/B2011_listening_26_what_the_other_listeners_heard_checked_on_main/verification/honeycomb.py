"""B2011, B1 and B3 (main, 2026-11-26; data-free): agy-exp's honeycomb claims rebuilt on main's own code.
B1: on the largest orbit over the common point mod p^k (B1996's orbits_over_common_point, imported from its committed
script), W+ = P_L + P_R. (a) Double precision: the slowest decay (largest eigenvalue modulus below 2) over 2, against
Lambda(M)/2 = sqrt(w + sqrt(w^2 - 4))/2, w = (1 + 4 cos(pi/M))/2. (b) Exactly: F(x) = Res_t(m_c(t), x^4 - (1 + 4t) x^2 + 4),
m_c the minimal polynomial of cos(pi/M); its irreducible factor f vanishing at Lambda(M) (mpmath, 50 digits) tested for
division of W+'s characteristic polynomial: over Z (FLINT) for orbits up to 1176 points, modulo three 62-bit primes above.
B3: mod 81, the 648-point orbit against {0,1} x (Z/18)^2 with the card's L and R, by simultaneous breadth-first search from
every base point; L^2 and R^2 as permutations: commuting, their orders, the order of the group they generate.
    python3 -B honeycomb.py > honeycomb_run.txt"""
import pathlib, time
import numpy as np, sympy as sp, flint, mpmath as mp
ROOT = pathlib.Path(__file__).resolve().parents[3]
src = next(ROOT.glob("frontier/B1996_*/verification/tower_decay.py")).read_text().split("t0 = time.time()")[0]
ns = {}; exec(src, ns); orbits = ns["orbits_over_common_point"]
t0 = time.time()
log = lambda s: print(s + "  [%.0f s]" % (time.time() - t0), flush=True)
mp.mp.dps = 50
t = sp.Symbol("t"); x = sp.Symbol("x")


def largest(p, k):
    N, n, Lm, Rm, roots = orbits(p, k)
    r, c = np.unique(roots, return_counts=True); big = r[np.argmax(c)]; mem = np.nonzero(roots == big)[0]; m = len(mem)
    loc = -np.ones(n, dtype=int); loc[mem] = np.arange(m)
    return N, m, loc[Lm[mem]], loc[Rm[mem]], mem


def lam(M):
    w = (1 + 4 * mp.cos(mp.pi / M)) / 2
    return mp.sqrt(w + mp.sqrt(w * w - 4))


for p, k, M in ((3, 3, 3), (3, 4, 9), (5, 3, 5), (7, 3, 7), (5, 4, 25)):
    N, m, Li, Ri, mem = largest(p, k)
    W = np.zeros((m, m), dtype=np.int64)
    np.add.at(W, (Li, np.arange(m)), 1); np.add.at(W, (Ri, np.arange(m)), 1)
    ev = np.linalg.eigvals(W.astype(float))
    mods = np.abs(ev)
    slow = max(v for v in mods if v < 2 - 1e-6)
    L = lam(M)
    # fixed after a first run stopped here before printing (B2011 disclosure): at M = 3, w < 2 and Lambda is complex; its modulus is compared
    log("B1 mod %d (p = %d, M = %d): largest orbit %d; slowest decay (double) %.15f; |Lambda(M)|/2 = %s; difference %.2e" % (N, p, M, m, slow / 2, mp.nstr(abs(L) / 2, 18), abs(slow / 2 - float(abs(L) / 2))))
    mc = sp.minimal_polynomial(sp.cos(sp.pi / M), t)
    F = sp.Poly(sp.resultant(sp.Poly(mc, t).as_expr(), x ** 4 - (1 + 4 * t) * x ** 2 + 4, t), x)
    Fz = flint.fmpz_poly([int(c) for c in reversed(F.all_coeffs())])
    _, facs = Fz.factor()
    f = None
    for g, e in facs:
        cs = [int(c) for c in g.coeffs()]
        if abs(mp.polyval(list(reversed([mp.mpf(c) for c in cs])), L)) < mp.mpf(10) ** -30:
            f = g
    log("    the factor of F vanishing at Lambda(M): degree %d, coefficients (constant first) %s" % (f.degree(), [int(c) for c in f.coeffs()]))
    if m <= 1176:
        cp = flint.fmpz_mat(W.tolist()).charpoly()
        mult = 0; q = cp
        while True:
            qq, rr = divmod(q, f)
            if rr != 0:
                break
            q = qq; mult += 1
        log("    over Z: f divides W+'s characteristic polynomial with multiplicity %d" % mult)
    else:
        oks = []
        pr = int(sp.nextprime(1 << 61))
        for _ in range(3):
            A = flint.nmod_mat(W.tolist(), pr)
            cpm = A.charpoly()
            fm = flint.nmod_poly([int(c) % pr for c in f.coeffs()], pr)
            oks.append((pr, cpm % fm == 0))
            pr = int(sp.nextprime(pr + 1000003))
        log("    modulo three 62-bit primes: f divides W+'s characteristic polynomial: %s" % [o for _, o in oks])

# B3: the honeycomb torus at mod 81
N, m, Li, Ri, mem = largest(3, 4)
_, n, Lm, Rm, roots = orbits(3, 4)
vals = np.arange(0, N, 3)
Xg, Yg, Zg = np.meshgrid(vals, vals, vals, indexing="ij"); on = (Xg * Xg + Yg * Yg + Zg * Zg - Xg * Yg * Zg) % N == 0
pts = list(zip(Xg[on].ravel().tolist(), Yg[on].ravel().tolist(), Zg[on].ravel().tolist()))
log("B3 mod 81: the largest orbit over the common point has %d points; it contains (3,3,3): %s" % (m, any(pts[i] == (3, 3, 3) for i in mem)))
model = [(s, a, b) for s in (0, 1) for a in range(18) for b in range(18)]
mid = {v: i for i, v in enumerate(model)}
mL = [mid[(1, (a + b) % 18, (-b) % 18)] if s == 0 else mid[(0, (a + b + 1) % 18, (-b) % 18)] for s, a, b in model]
mR = [mid[(1, (-a) % 18, (a + b) % 18)] if s == 0 else mid[(0, (-a) % 18, (a + b + 1) % 18)] for s, a, b in model]


def try_base(x0):
    phi = {x0: 0}; todo = [x0]
    while todo:
        u = todo.pop()
        for A, B in ((Li, mL), (Ri, mR)):
            v = int(A[u]); w = B[phi[u]]
            if v in phi:
                if phi[v] != w:
                    return False
            else:
                phi[v] = w; todo.append(v)
    return len(phi) == m and len(set(phi.values())) == m


good = [x0 for x0 in range(m) if try_base(x0)]
log("    base points of the orbit from which the map onto {0,1} x (Z/18)^2 is an isomorphism with L and R: %d of %d" % (len(good), m))
L2 = [int(Li[int(Li[i])]) for i in range(m)]; R2 = [int(Ri[int(Ri[i])]) for i in range(m)]
comp = lambda a, b: tuple(a[b[i]] for i in range(m))
log("    L^2 and R^2 commute: %s" % (comp(L2, R2) == comp(R2, L2)))
ident = tuple(range(m))
def order(pm):
    q = tuple(pm); o = 1
    while q != ident:
        q = comp(pm, q); o += 1
    return o
G = {ident}; frontier = [ident]
while frontier:
    nxt = []
    for g in frontier:
        for h in (tuple(L2), tuple(R2)):
            e = comp(h, g)
            if e not in G:
                G.add(e); nxt.append(e)
    frontier = nxt
log("    orders of L^2, R^2: %d, %d; the group they generate has order %d" % (order(L2), order(R2), len(G)))
