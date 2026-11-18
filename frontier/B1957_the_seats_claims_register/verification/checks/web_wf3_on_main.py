"""B1957: the web seat's foundations card W-F3 (the cone-point loophole), on main's own code.  Data-free; exact over F_p.
G_n = <a, b, t | t x t^-1 = sigma^n(x)>, sigma: a -> ab, b -> a (the tick), levels n = 2 to 6; G_(n,k) adds
lambda^k = 1, lambda = [a, b] (the fibre's puncture replaced by a cone point of order k).  w(t) = (-1)^n.
Modules, as the seat's sealed script defines them (read as text):
 (a) every character chi with chi o sigma^n = chi on the fibre and chi(t) any 2e-th root of unity (e the fibre
     torsion's exponent);
 (b) for every non-trivial fibre-torsion character l with l(mu) = 1 that has a class c of H^1(G; l) which is not a
     coboundary, the modules [[alpha, c beta], [0, beta]], alpha and beta = alpha/l fibre-torsion characters with
     value 1 on mu, beta non-trivial.
The gap of V: h^1(V) - h^1(V* (x) w).
 K1  at k = 2 to 6: whether any class has c(lambda) != 0, and how many non-split modules exist.
 K2/K3  the number of modules with a non-zero gap, at every k and at k = infinity.
 Q1  at finite k, for every character: gap = h^0(V) - h^0(V* (x) w).
 Q2  which characters keep a gap at finite k.
Main's code: the words and the conjugator are B1926's; the cohomology of a matrix module by Fox calculus is written here.
Two primes, both different from the seat's."""
import sys, pathlib, functools, itertools
from math import gcd
print = functools.partial(print, flush=True)
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1926_*")) / "verification")); import odd_ticks_no_modules as B
A_, B_, T_ = B.A, B.B, B.T; LAM = B.LAM


class Rep:
    def __init__(self, mats, p):
        self.p, self.d = p, len(mats[1]); self.m = {}
        for g, M in mats.items(): self.m[g] = [[x % p for x in r] for r in M]; self.m[-g] = self.inverse(self.m[g])
    def inverse(self, M):
        p, d = self.p, len(M); Aug = [list(r) + [int(i == j) for j in range(d)] for i, r in enumerate(M)]
        for c in range(d):
            k = next(i for i in range(c, d) if Aug[i][c] % p); Aug[c], Aug[k] = Aug[k], Aug[c]; iv = pow(Aug[c][c], p - 2, p); Aug[c] = [x * iv % p for x in Aug[c]]
            for i in range(d):
                if i != c and Aug[i][c] % p: f = Aug[i][c]; Aug[i] = [(x - f * y) % p for x, y in zip(Aug[i], Aug[c])]
        return [r[d:] for r in Aug]
    def mul(self, X, Y): return [[sum(X[i][k] * Y[k][j] for k in range(self.d)) % self.p for j in range(self.d)] for i in range(self.d)]
    def fox(self, w, gen):
        """the matrix of d w / d gen in this module: c(w) = sum over generators of fox(w, g) c(g), with c(xy) = c(x) + x c(y)"""
        d, p = self.d, self.p; S = [[0] * d for _ in range(d)]; pre = [[int(i == j) for j in range(d)] for i in range(d)]
        for g in w:
            if g == gen: S = [[(S[i][j] + pre[i][j]) % p for j in range(d)] for i in range(d)]
            elif g == -gen:
                X = self.mul(pre, self.m[-gen]); S = [[(S[i][j] - X[i][j]) % p for j in range(d)] for i in range(d)]
            pre = self.mul(pre, self.m[g])
        return S


def rank(M, p):
    M = [list(r) for r in M]; r = 0
    for c in range(len(M[0]) if M else 0):
        k = next((i for i in range(r, len(M)) if M[i][c] % p), None)
        if k is None: continue
        M[r], M[k] = M[k], M[r]; iv = pow(M[r][c], p - 2, p); M[r] = [x * iv % p for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] % p: f = M[i][c]; M[i] = [(x - f * y) % p for x, y in zip(M[i], M[r])]
        r += 1
    return r


def cohom(V, rels):
    d, p = V.d, V.p
    inv_rows = [[(V.m[g][i][j] - int(i == j)) % p for j in range(d)] for g in (1, 2, 3) for i in range(d)]; h0 = d - rank(inv_rows, p)
    rows = []
    for r in rels:
        F = [V.fox(r, g) for g in (1, 2, 3)]
        for i in range(d): rows.append([F[g][i][j] for g in range(3) for j in range(d)])
    z1 = 3 * d - rank(rows, p)
    return h0, z1 - (d - h0)


def dual_w(V, w):
    tr = lambda M: [list(r) for r in zip(*M)]
    return Rep({1: tr(V.m[-1]), 2: tr(V.m[-2]), 3: [[x * w % V.p for x in r] for r in tr(V.m[-3])]}, V.p)


def level(n, p, gen):
    M = [[1, 0], [0, 1]]
    for _ in range(n): M = [[M[0][0] + M[0][1], M[0][0]], [M[1][0] + M[1][1], M[1][0]]]        # columns: a -> a + b, b -> a
    tor = abs((M[0][0] - 1) * (M[1][1] - 1) - M[0][1] * M[1][0]); g1 = gcd(gcd(M[0][0] - 1, M[0][1]), gcd(M[1][0], M[1][1] - 1)); e = max(tor // g1, 1)
    g, s = B.find_g(n); w = p - 1 if n % 2 else 1; z = pow(gen, (p - 1) // (2 * e), p)
    fib = [(a1, a2) for a1 in range(e) for a2 in range(e) if (a1 * M[0][0] + a2 * M[1][0] - a1) % e == 0 and (a1 * M[0][1] + a2 * M[1][1] - a2) % e == 0]
    chars = [(pow(z, 2 * a1, p), pow(z, 2 * a2, p), pow(z, j, p)) for a1, a2 in fib for j in range(2 * e)]
    ga, gb = B.abel(g)[0], B.abel(g)[1]
    tors = [(pow(z, 2 * a1, p), pow(z, 2 * a2, p), pow(z, 2 * ((a1 * ga + a2 * gb) % e), p)) for a1, a2 in fib if (a1, a2) != (0, 0)]
    base = [B.red((T_, A_, -T_) + B.inv(B.sigma_n((A_,), n))), B.red((T_, B_, -T_) + B.inv(B.sigma_n((B_,), n)))]
    return e, w, chars, tors, base


def table(p):
    gen = next(x for x in range(2, p) if all(pow(x, (p - 1) // q, p) != 1 for q in set(f for f in range(2, p) if (p - 1) % f == 0 and all(f % r for r in range(2, int(f ** 0.5) + 1)))))
    out = {}; q1 = True; keepers = set()
    for n in range(2, 7):
        e, w, chars, tors, base = level(n, p, gen)
        for k in (2, 3, 4, 5, 6, None):
            rels = base + ([B.red(LAM * k)] if k else []); nz = 0; sector = False; nb = 0
            def gap(mats):
                V = Rep(mats, p); return cohom(V, rels)[1] - cohom(dual_w(V, w), rels)[1]
            for ch in chars:
                V = Rep({1: [[ch[0]]], 2: [[ch[1]]], 3: [[ch[2]]]}, p); (h0, h1), (g0, g1) = cohom(V, rels), cohom(dual_w(V, w), rels); gp = h1 - g1; nz += gp != 0
                if k:
                    q1 &= gp == h0 - g0
                    if gp: keepers.add((n % 2, "trivial" if ch == (1, 1, 1) else ("w" if ch == (1, 1, w) else "other"), gp))
            for l in tors:
                r1 = Rep({1: [[l[0]]], 2: [[l[1]]], 3: [[l[2]]]}, p); F = [[r1.fox(r, g)[0][0] for g in (1, 2, 3)] for r in rels]; Z = B.nullspace(F, p, 3); cob = [(l[i] - 1) % p for i in range(3)]
                c = next((zb for zb in Z if any((zb[i] * cob[j] - zb[j] * cob[i]) % p for i in range(3) for j in range(3))), None)
                if c is None: continue
                if sum(r1.fox(LAM, g)[0][0] * c[g - 1] for g in (1, 2, 3)) % p: sector = True
                for al in tors:
                    be = tuple(al[i] * pow(l[i], p - 2, p) % p for i in range(3))
                    if be[:2] == (1, 1): continue
                    nz += gap({g: [[al[g - 1], c[g - 1] * be[g - 1] % p], [0, be[g - 1]]] for g in (1, 2, 3)}) != 0; nb += 1
            out[(n, k)] = (len(chars), nb, sector, nz)
    return out, q1, keepers


if __name__ == "__main__":
    res = {}
    for p in (881, 1321):
        out, q1, keepers = table(p); res[p] = out
        print("prime %d:" % p)
        for n in range(2, 7):
            print("  level %d: characters %d; at k = 2 to 6: non-split modules %s, a class with c(lambda) != 0: %s, modules with a non-zero gap %s; at the puncture: non-split modules %d, a class with c(lambda) != 0: %s, modules with a non-zero gap %d" % (
                n, out[(n, None)][0], sorted({out[(n, k)][1] for k in range(2, 7)}), sorted({out[(n, k)][2] for k in range(2, 7)}), sorted({out[(n, k)][3] for k in range(2, 7)}), out[(n, None)][1], out[(n, None)][2], out[(n, None)][3]))
        print("  Q1: at k = 2 to 6, every level, every character: gap = h^0(V) - h^0(V* (x) w): %s; Q2: the characters that keep a gap there (level's parity, which, gap): %s" % (q1, sorted(keepers)))
    print("the two primes give the same table: %s" % (res[881] == res[1321]))
