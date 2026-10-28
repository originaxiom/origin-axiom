"""Referee B1802, r2: the order-2 torsion of Q = m004(p,q) (p even) without the Alexander polynomial or the arc's r-formula
(SnapPy's own words, Fox calculus, Turaev gluing), and |H1| of the 2-fold cyclic cover by own Reidemeister-Schreier
(Smith normal form over Z) vs SnapPy vs 5p/2.  Also: Smith counts; p odd controls; and H1(Q;Z/2) for p = 2 mod 4 vs 0 mod 4."""
import itertools, math, cmath
import sympy as sp
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form
import snappy
t = sp.symbols("t")
def abel_exp(word, ph): return sum((1 if ch.islower() else -1) * ph[ch.lower()] for ch in word)
def fox_abel(word, gen, phi):
    total = 0; prefix = 0
    for ch in word:
        e = 1 if ch.islower() else -1; g = ch.lower()
        if g == gen: total += t**prefix if e == 1 else -t**(prefix - phi[g])
        prefix += e * phi[g]
    return sp.expand(total)
G = snappy.Manifold("m004").fundamental_group(); gens = G.generators(); rel = G.relators()[0]
phi = None
for i in range(-3, 4):
    for j in range(-3, 4):
        if (i, j) != (0, 0) and math.gcd(i, j) == 1 and abel_exp(rel, {gens[0]: i, gens[1]: j}) == 0 and phi is None:
            phi = {gens[0]: i, gens[1]: j}
mer, lon = G.peripheral_curves()[0]
if abel_exp(mer, phi) < 0: phi = {k: -v for k, v in phi.items()}
assert abel_exp(mer, phi) == 1 and abel_exp(lon, phi) == 0
gi = gens[0] if phi[gens[0]] != 0 else gens[1]; gj = gens[1] if gi == gens[0] else gens[0]
Dj = fox_abel(rel, gj, phi)
print("exterior torsion (SnapPy words):", sp.factor(sp.simplify(Dj / (t**phi[gi] - 1))))
def tau_Q(p, q, k):
    z = cmath.exp(2j * math.pi * k / p)
    tauX = complex(sp.N(Dj.subs(t, z))) / (z**phi[gi] - 1)
    r = next(rr for rr in range(-200, 201) if (1 + q * rr) % p == 0)
    return abs(tauX / (z**r - 1))
def fox_group_ring(word, gen, ph, n):
    v = [0] * n; prefix = 0
    for ch in word:
        e = 1 if ch.islower() else -1; g = ch.lower()
        if g == gen:
            if e == 1: v[prefix % n] += 1
            else: v[(prefix - ph[g]) % n] -= 1
        prefix += e * ph[g]
    return v
def cover_H1_own(p, q, n=2):
    M = snappy.Manifold("m004"); M.dehn_fill((p, q))
    GQ = M.fundamental_group(); gq = GQ.generators(); rels = GQ.relators()
    sol = None
    for vals in itertools.product(range(p), repeat=len(gq)):
        ph = dict(zip(gq, vals))
        if all(abel_exp(r, ph) % p == 0 for r in rels) and math.gcd(*vals, p) == 1: sol = ph; break
    phn = {g: v % n for g, v in sol.items()}
    rows = []
    for r in rels:
        for s in range(n):
            row = []
            for g in gq:
                v = fox_group_ring(r, g, phn, n); row += [v[(j - s) % n] for j in range(n)]
            rows.append(row)
    D2 = Matrix(rows)
    cols = []
    for g in gq:
        for j in range(n):
            c = [0] * n; c[(j + phn[g]) % n] += 1; c[j] -= 1; cols.append(c)
    D1 = Matrix(cols)
    snf = smith_normal_form(D2, domain=ZZ)
    diag = [abs(snf[i, i]) for i in range(min(snf.shape)) if snf[i, i] != 0]
    free = (len(gq) * n - D1.rank()) - len(diag)
    return free, math.prod(d for d in diag if d != 1)
print("filling     |tau(chi_2)| own   2-fold cover |H1|: own RS   SnapPy   5p/2   | sum dim H_*(Q;Z/2)")
bad = 0
for (p, q) in [(6, 1), (8, 1), (2, 3), (4, 3), (10, 3), (2, 5), (12, 5), (14, 3), (16, 7), (20, 9), (4, 7), (6, -1), (8, -3)]:
    tv = tau_Q(p, q, p // 2)
    free, order = cover_H1_own(p, q)
    M = snappy.Manifold("m004"); M.dehn_fill((p, q))
    sn = [str(C.homology()) for C in M.covers(2, cover_type="cyclic")]
    ed = M.homology().elementary_divisors(); z2 = sum(1 for x in ed if x % 2 == 0)
    ok = abs(tv - 1.25) < 1e-9 and free == 0 and order == 5 * p // 2
    bad += not ok
    print("m004(%3d,%3d)  %.12f        free %d order %4d   %s   %4d   | %d  %s" % (p, q, tv, free, order, sn, 5 * p // 2, 2 + 2 * z2, "ok" if ok else "MISMATCH"))
print("mismatches:", bad)
# p odd: no order-2 character, Z/2 homology total 2
for (p, q) in [(5, 1), (3, 2), (7, 2), (9, 4)]:
    M = snappy.Manifold("m004"); M.dehn_fill((p, q)); ed = M.homology().elementary_divisors()
    print("control m004(%d,%d): H1 %s, sum dim H_*(Q;Z/2) = %d" % (p, q, M.homology(), 2 + 2 * sum(1 for x in ed if x % 2 == 0)))
print("r2 exit 0")
