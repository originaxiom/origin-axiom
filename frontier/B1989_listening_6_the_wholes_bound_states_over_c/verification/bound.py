"""B1989 (main, 2026-11-25; data-free): the whole's bound states over C. For each finite subgroup G of SU(2) (Q8, 2T, 2O, 2I)
built exactly over a cyclotomic field, every pair (a, b) in G gives a reading (tr a, tr b, tr ab); the moves L, R permute the
readings of pairs (L: b -> ab, i.e. (x, y, z) -> (x, z, xz - y); R the mirror); their orbits, sizes and kappa. Exact (sympy).
    python3 -B bound.py > bound_run.txt"""
import sympy as sp
from itertools import product
I = sp.I
def close(gens):
    G = {}; fr = []
    def key(M): return tuple(sp.nsimplify(sp.expand(e)) for e in M)
    E = sp.eye(2)
    G[key(E)] = E; fr = [E]
    while fr:
        A = fr.pop()
        for g in gens:
            C = (g * A).applyfunc(lambda e: sp.radsimp(sp.expand(e)))
            k = key(C)
            if k not in G: G[k] = C; fr.append(C)
    return list(G.values())
q = lambda a, b, c, d: sp.Matrix([[a + b * I, c + d * I], [-c + d * I, a - b * I]])
i_, j_ = q(0, 1, 0, 0), q(0, 0, 1, 0)
h = sp.Rational(1, 2); w = q(-h, h, h, h)                           # an order-6 unit (1 + i + j + k)/2 up to sign
s2 = sp.sqrt(2) / 2; o = q(s2, s2, 0, 0)                            # (1 + i)/sqrt2, order 8
phi = (1 + sp.sqrt(5)) / 2; ic = q(phi / 2, (phi - 1) / 2, h, 0)    # an order-10 icosian
groups = {"Q8": [i_, j_], "2T": [i_, j_, w], "2O": [i_, j_, w, o], "2I": [i_, j_, w, ic]}
def rd(e): return sp.nsimplify(sp.radsimp(sp.expand(e)))
for name, gens in groups.items():
    G = close(gens)
    tr = {}
    for A in G: tr[id(A)] = rd(A.trace())
    reads = set()
    for A, B in product(G, G):
        reads.add((tr[id(A)], tr[id(B)], rd((A * B).trace())))
    L = lambda v: (v[0], v[2], rd(v[0] * v[2] - v[1])); R = lambda v: (v[2], v[1], rd(v[1] * v[2] - v[0]))
    seen, orbs = set(), []
    for v in reads:
        if v in seen: continue
        o_, st = {v}, [v]
        while st:
            u = st.pop()
            for f in (L, R):
                x = f(u)
                if x not in o_: o_.add(x); st.append(x)
        assert o_ <= reads
        seen |= o_; orbs.append(o_)
    kap = lambda v: rd(v[0] ** 2 + v[1] ** 2 + v[2] ** 2 - v[0] * v[1] * v[2] - 2)
    rows = sorted(((kap(next(iter(o))), len(o)) for o in orbs), key=lambda t: (float(t[0]), t[1]))
    print("%s: order %d; %d distinct readings of pairs; %d orbits of the moves; (kappa, size): %s" % (name, len(G), len(reads), len(orbs), rows), flush=True)
    print("   kappa values carrying a bound state: %s" % sorted({r[0] for r in rows}, key=float), flush=True)
    print("   the common point (0, 0, 0) among the readings: %s" % ((0, 0, 0) in reads), flush=True)
