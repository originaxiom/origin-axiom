"""B1957: the web seat's foundations card W-F4 (the non-orientable closing; the odd tick's matter as its double cover's),
on main's own code.  Data-free; exact ranks over two prime fields (neither the seat's).
Definitions as the seat's sealed script states them (read as text):
  the metallic tick tau_m: a -> a^m b, b -> a (m = 1 golden, 3 bronze); G_n = <a, b, t | t x t^-1 = tau_m^n(x)>; odd n is
  non-orientable, w(t) = (-1)^n; lambda = [a, b]; g_1 = a^m, g_(k+1) = tau_m(g_k) a^m, mu_n = g_n^-1 t; the double cover of
  an odd level n is level 2n = <a, b, T = t^2>, with mu_2n = mu_n^2; characters: on the fibre torsion, chi(t) any 2e-th
  root of unity; Ind psi: a -> diag(psi(a), psi(tau^n a)), b likewise, t -> [[0, psi(T)], [1, 0]]; closed objects add
  lambda^k = 1, k = 1 to 6; U the unipotent extension by the tick's class.
 N1  transfer: h^i(G_2n; pi* chi) = h^i(G_n; chi) + h^i(G_n; chi w), i = 0, 1, and the interior classes, every character.
 N2  the fibre-non-trivial chi with chi(mu_n) = -1: their number; each pulls back to a character trivial on mu_2n that
     carries a class with c(lambda) != 0; and h^1 = 0 for every fibre-non-trivial chi with chi(mu_n) = +1.
 N3  the record's data at level 2n; the deck-invariant ones; the deck pairs; and Ind psi for every fibre-non-trivial psi
     that is not deck-invariant: a module of G_n with h^0, h^1 and the interior classes of psi on the double cover.
 N4  closed objects at odd levels, k = 1 to 6: h^1 is 1 for the trivial character and 0 for every other.
 N5  there: characters, the doublets alpha (x) U and the induced modules have untwisted gap 0 and twisted gap
     h^0(V) - h^0(V* w); and h^1(G_n,k; Ind psi) = h^1(G_2n,k; psi).
 N6  the control on N_3 x S^1 with the seat's alpha, beta, omega and cocycle: (h^0, h^1) of V, V*, V* omega, V omega."""
import functools, itertools, sys
from math import gcd
print = functools.partial(print, flush=True)
A, B, T = 1, 2, 3


def red(w):
    out = []
    for g in w:
        if out and out[-1] == -g: out.pop()
        else: out.append(g)
    return tuple(out)
inv = lambda w: tuple(-g for g in reversed(w))
def tau(w, m):
    out = []
    for g in w: out.extend(((A,) * m + (B,) if abs(g) == A else (A,)) if g > 0 else inv((A,) * m + (B,) if abs(g) == A else (A,)))
    return red(out)
def tau_n(w, m, n):
    for _ in range(n): w = tau(w, m)
    return w
LAM = (A, B, -A, -B)
def conjugator(m, n):
    g = (A,) * m
    for _ in range(n - 1): g = red(tau(g, m) + (A,) * m)
    return g
abel = lambda w: [sum((1 if g > 0 else -1) for g in w if abs(g) == x) for x in (A, B)]


class Rep:
    def __init__(self, mats, p):
        self.p = p; self.d = len(next(iter(mats.values()))); self.gens = sorted(mats); self.m = {}
        for g, M in mats.items(): self.m[g] = [[x % p for x in r] for r in M]; self.m[-g] = self.inverse(self.m[g])
    def inverse(self, M):
        p, d = self.p, len(M); Aug = [list(r) + [int(i == j) for j in range(d)] for i, r in enumerate(M)]
        for c in range(d):
            k = next(i for i in range(c, d) if Aug[i][c] % p); Aug[c], Aug[k] = Aug[k], Aug[c]; iv = pow(Aug[c][c], p - 2, p); Aug[c] = [x * iv % p for x in Aug[c]]
            for i in range(d):
                if i != c and Aug[i][c] % p: f = Aug[i][c]; Aug[i] = [(x - f * y) % p for x, y in zip(Aug[i], Aug[c])]
        return [r[d:] for r in Aug]
    def mul(self, X, Y): return [[sum(X[i][k] * Y[k][j] for k in range(self.d)) % self.p for j in range(self.d)] for i in range(self.d)]
    def word(self, w): return functools.reduce(self.mul, [self.m[g] for g in w], [[int(i == j) for j in range(self.d)] for i in range(self.d)])
    def fox(self, w, gen):
        d, p = self.d, self.p; S = [[0] * d for _ in range(d)]; pre = [[int(i == j) for j in range(d)] for i in range(d)]
        for g in w:
            if g == gen: S = [[(S[i][j] + pre[i][j]) % p for j in range(d)] for i in range(d)]
            elif g == -gen:
                X = self.mul(pre, self.m[-gen]); S = [[(S[i][j] - X[i][j]) % p for j in range(d)] for i in range(d)]
            pre = self.mul(pre, self.m[g])
        return S
    def is_module(self, rels): return all(self.word(r) == [[int(i == j) for j in range(self.d)] for i in range(self.d)] for r in rels)
    def dual(self, w=None):
        tr = lambda M: [list(r) for r in zip(*M)]; return Rep({g: [[x * (w[g] if w else 1) % self.p for x in r] for r in tr(self.m[-g])] for g in self.gens}, self.p)


def rref(M, p):
    M = [list(r) for r in M]; r = 0; piv = []
    for c in range(len(M[0]) if M else 0):
        k = next((i for i in range(r, len(M)) if M[i][c] % p), None)
        if k is None: continue
        M[r], M[k] = M[k], M[r]; iv = pow(M[r][c], p - 2, p); M[r] = [x * iv % p for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] % p: f = M[i][c]; M[i] = [(x - f * y) % p for x, y in zip(M[i], M[r])]
        piv.append(c); r += 1
    return M[:r], piv
rank = lambda M, p: len(rref(M, p)[1]) if M else 0
def nullspace(M, p, n):
    R, piv = rref(M, p) if M else ([], []); free = [c for c in range(n) if c not in piv]; out = []
    for f in free:
        v = [0] * n; v[f] = 1
        for i, c in enumerate(piv): v[c] = (-R[i][f]) % p
        out.append(v)
    return out


def cohom(V, rels, cusp=None):
    """(h^0, h^1) and, with cusp = a list of words generating the cusp group, the number of interior classes"""
    d, p, G = V.d, V.p, V.gens
    h0 = d - rank([[(V.m[g][i][j] - int(i == j)) % p for j in range(d)] for g in G for i in range(d)], p)
    rows = []
    for r in rels:
        F = [V.fox(r, g) for g in G]
        for i in range(d): rows.append([F[k][i][j] for k in range(len(G)) for j in range(d)])
    Z = nullspace(rows, p, len(G) * d); h1 = len(Z) - (d - h0)
    if cusp is None: return h0, h1
    def value(c, w):                                                   # c(w) = sum_g fox(w, g) c(g)
        out = [0] * d
        for k, g in enumerate(G):
            F = V.fox(w, g)
            for i in range(d): out[i] = (out[i] + sum(F[i][j] * c[k * d + j] for j in range(d))) % p
        return out
    Rm = [sum((value(c, w) for w in cusp), []) for c in Z]            # each cocycle restricted to the cusp's generators
    Wm = [V.word(w) for w in cusp]; Cb = [sum(([(Wm[q][i][j] - int(i == j)) % p for i in range(d)] for q in range(len(cusp))), []) for j in range(d)]   # coboundaries on the cusp
    interior_cocycles = len(Z) - (rank(Rm + Cb, p) - rank(Cb, p))
    return h0, h1, interior_cocycles - (d - h0)


def setup(m, n, p, gen):
    f = {A: tau_n((A,), m, n), B: tau_n((B,), m, n)}; M = [[abel(f[A])[0], abel(f[B])[0]], [abel(f[A])[1], abel(f[B])[1]]]
    tor = abs((M[0][0] - 1) * (M[1][1] - 1) - M[0][1] * M[1][0]); g1 = gcd(gcd(M[0][0] - 1, M[0][1]), gcd(M[1][0], M[1][1] - 1)); e = max(tor // g1, 1)
    z = pow(gen, (p - 1) // (2 * e), p); g = conjugator(m, n); mu = red(inv(g) + (T,))
    fib = [(a1, a2) for a1 in range(e) for a2 in range(e) if (a1 * M[0][0] + a2 * M[1][0] - a1) % e == 0 and (a1 * M[0][1] + a2 * M[1][1] - a2) % e == 0]
    chars = [(pow(z, 2 * a1, p), pow(z, 2 * a2, p), pow(z, j, p)) for a1, a2 in fib for j in range(2 * e)]
    rels = [red((T, A, -T) + inv(f[A])), red((T, B, -T) + inv(f[B]))]
    return dict(f=f, e=e, z=z, mu=mu, chars=chars, rels=rels, tor=tor)
ch1 = lambda ch, p: Rep({A: [[ch[0]]], B: [[ch[1]]], T: [[ch[2]]]}, p)
val = lambda ch, w, p: functools.reduce(lambda v, g: v * (ch[abs(g) - 1] if g > 0 else pow(ch[abs(g) - 1], p - 2, p)) % p, w, 1)


def run(p):
    gen = next(x for x in range(2, p) if all(pow(x, (p - 1) // q, p) != 1 for q in {f for f in range(2, 2000) if (p - 1) % f == 0 and all(f % r for r in range(2, int(f ** 0.5) + 1))} | {q for q in [(p - 1) // 264 // (2 ** k) for k in range(8)] if q > 1 and (p - 1) % q == 0 and all(q % r for r in range(2, int(q ** 0.5) + 1))}))
    out = {}
    for m, n in ((1, 1), (1, 3), (1, 5), (3, 1)):
        lo, hi = setup(m, n, p, gen), setup(m, 2 * n, p, gen); w = {A: 1, B: 1, T: p - 1}; one = (1, 1, 1); res = {}
        cusp_lo, cusp_hi = [lo["mu"], LAM], [hi["mu"], LAM]
        # N1
        ok = True
        for ch in lo["chars"]:
            a = cohom(ch1(ch, p), lo["rels"], cusp_lo); b = cohom(ch1((ch[0], ch[1], ch[2] * (p - 1) % p), p), lo["rels"], cusp_lo); c = cohom(ch1((ch[0], ch[1], ch[2] * ch[2] % p), p), hi["rels"], cusp_hi)
            ok &= all(c[i] == a[i] + b[i] for i in range(3))
        res["N1"] = (len(lo["chars"]), ok)
        # N2
        fibnt = [ch for ch in lo["chars"] if ch[:2] != (1, 1)]; minus = [ch for ch in fibnt if val(ch, lo["mu"], p) == p - 1]; plus = [ch for ch in fibnt if val(ch, lo["mu"], p) == 1]
        def has_sector(ch, S):
            V = ch1(ch, p); F = [[V.fox(r, g)[0][0] for g in (A, B, T)] for r in S["rels"]]; Z = nullspace(F, p, 3)
            return any(sum(V.fox(LAM, g)[0][0] * c[k] for k, g in enumerate((A, B, T))) % p for c in Z)
        pulled = [(ch[0], ch[1], ch[2] * ch[2] % p) for ch in minus]
        res["N2"] = (len(minus), all(val(q, hi["mu"], p) == 1 and has_sector(q, hi) for q in pulled), len(plus), all(cohom(ch1(ch, p), lo["rels"])[1] == 0 for ch in plus))
        # N3
        data = [ch for ch in hi["chars"] if ch[:2] != (1, 1) and val(ch, hi["mu"], p) == 1 and has_sector(ch, hi)]
        deck = lambda ch: (val(ch, lo["f"][A], p), val(ch, lo["f"][B], p), ch[2]); inv_data = [ch for ch in data if deck(ch) == ch]
        res["N3count"] = (len(data), len(inv_data), set(inv_data) == set(pulled), (len(data) - len(inv_data)) // 2, all(deck(ch) in data for ch in data))
        psis = [ch for ch in hi["chars"] if ch[:2] != (1, 1) and deck(ch) != ch]; okI = True; classes = set()
        def ind(ch): return Rep({A: [[ch[0], 0], [0, val(ch, lo["f"][A], p)]], B: [[ch[1], 0], [0, val(ch, lo["f"][B], p)]], T: [[0, ch[2]], [1, 0]]}, p)
        for ch in psis:
            V = ind(ch); okI &= V.is_module(lo["rels"]) and cohom(V, lo["rels"], cusp_lo) == cohom(ch1(ch, p), hi["rels"], cusp_hi); classes.add(frozenset((ch, deck(ch))))
        res["N3ind"] = (len(psis), len(classes), okI)
        # N4, N5 on the closed objects
        n4 = True; n5c = n5u = n5i = True; ni = 0
        for k in range(1, 7):
            rl, rh = lo["rels"] + [red(LAM * k)], hi["rels"] + [red(LAM * k)]
            for ch in lo["chars"]:
                V = ch1(ch, p); h0, h1 = cohom(V, rl); n4 &= h1 == (1 if ch == one else 0)
                d0, d1 = cohom(V.dual(), rl); t0, t1 = cohom(V.dual(w), rl); n5c &= (h1 - d1 == 0) and (h1 - t1 == h0 - t0)
                U = Rep({A: [[ch[0], 0], [0, ch[0]]], B: [[ch[1], 0], [0, ch[1]]], T: [[ch[2], ch[2]], [0, ch[2]]]}, p); u0, u1 = cohom(U, rl); ud0, ud1 = cohom(U.dual(), rl); ut0, ut1 = cohom(U.dual(w), rl)
                n5u &= U.is_module(rl) and (u1 - ud1 == 0) and (u1 - ut1 == u0 - ut0)
            for ch in psis:
                V = ind(ch); h0, h1 = cohom(V, rl); d0, d1 = cohom(V.dual(), rl); t0, t1 = cohom(V.dual(w), rl); ni += 1
                n5i &= (h1 - d1 == 0) and (h1 - t1 == h0 - t0) and h1 == cohom(ch1(ch, p), rh)[1]
        res["N4"] = n4; res["N5"] = (n5c, n5u, n5i, ni // 6)
        out[(m, n)] = res
    # N6: N_3 x S^1
    z3 = pow(gen, (p - 1) // 3, p); rels6 = [(1, 1, 2, 2, 3, 3)] + [red((4, i, -4, -i)) for i in (1, 2, 3)]; om = {1: p - 1, 2: p - 1, 3: p - 1, 4: 1}
    al, be, u = (z3, z3 * z3 % p, 1, 1), (p - 1, p - 1, p - 1, 1), (0, 0, 1, 0)
    V = Rep({g: [[al[g - 1], u[g - 1] * be[g - 1] % p], [0, be[g - 1]]] for g in (1, 2, 3, 4)}, p)
    out["N6"] = (V.is_module(rels6), cohom(V, rels6), cohom(V.dual(), rels6), cohom(V.dual(om), rels6), cohom(Rep({g: [[x * om[g] % p for x in r] for r in V.m[g]] for g in (1, 2, 3, 4)}, p), rels6))
    return out


if __name__ == "__main__":
    primes = []; q = 1000000 - (1000000 % 264) + 1
    while len(primes) < 2:
        q += 264
        if all(q % r for r in range(2, int(q ** 0.5) + 1)): primes.append(q)
    res = {p: run(p) for p in primes}; r = res[primes[0]]
    print("primes %s (both 1 mod 264; the seat's were 10561849 and 10563433); the two give the same results: %s" % (primes, res[primes[0]] == res[primes[1]]))
    for (m, n), name in (((1, 1), "golden n = 1"), ((1, 3), "golden n = 3"), ((1, 5), "golden n = 5"), ((3, 1), "bronze n = 1")):
        x = r[(m, n)]
        print("%s: N1 transfer with the interior classes on all %d characters: %s | N2: %d fibre-non-trivial characters with chi(mu) = -1, each pulling back to a character trivial on mu_2n with c(lambda) != 0: %s; the %d with chi(mu) = +1 all have h^1 = 0: %s" % (name, x["N1"][0], x["N1"][1], x["N2"][0], x["N2"][1], x["N2"][2], x["N2"][3]))
        print("    N3: the record's data at level %d: %d; deck-invariant %d, and they are exactly the pull-backs: %s; deck pairs %d (the data closed under the deck: %s); Ind psi on %d characters psi (%d modules up to the deck): a module with h^0, h^1 and interior classes equal to psi's: %s" % (2 * n, x["N3count"][0], x["N3count"][1], x["N3count"][2], x["N3count"][3], x["N3count"][4], x["N3ind"][0], x["N3ind"][1], x["N3ind"][2]))
        print("    N4: closed objects k = 1 to 6: h^1 = 1 for the trivial character and 0 for every other: %s | N5: untwisted gap 0 and twisted gap = h^0(V) - h^0(V* w) on every character: %s, every doublet alpha (x) U: %s, every induced module (%d per k) with h^1 equal to psi's on the double cover: %s" % (x["N4"], x["N5"][0], x["N5"][1], x["N5"][3], x["N5"][2]))
    print("N6: N_3 x S^1 with the seat's alpha, beta, cocycle: a module: %s; (h^0, h^1) of V %s, V* %s, V* omega %s, V omega %s (agy-exp's: (0, 3), (0, 2), (1, 4); the seat adds V omega (0, 2))" % r["N6"])
