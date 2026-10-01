#!/usr/bin/env python3
"""control: classes pulled back to the double cover give twice the value.  Run on M2's firing modules (m206), which
are not generation-shaped backgrounds (M2 has none): no prediction of the census is touched."""
import sys
from interaction_census import *
eps, word, k = 1, "LR", 2
o, bgs, I, chars, N, rels, tau = level_census(eps, word, k)
assert len(bgs) == 0
B1 = Bundle(Phi_of(eps, word, k)); C1, z1, _ = B1.fundamental()
B2 = Bundle(Phi_of(eps, word, 2 * k)); C2, z2, _ = B2.fundamental()
p = o["primes"][0]; zeta = pow(cc.primroot(p), (p - 1) // N, p)
add = lambda x, y: tuple((a + b) % N for a, b in zip(x, y)); neg = lambda x: tuple((-a) % N for a in x)
def up_module(V):                                           # restriction to the index-2 subgroup <x, y, t^2>
    return Module(B2, V.M[X], V.M[Y], mmul(V.Mt, V.Mt, V.p), V.p)
def up_cocycle(c, V2):                                      # f(t^2) = f(t) + t f(t)
    return Cocycle(V2, c.v[X], c.v[Y], [(a + b) % c.V.p for a, b in zip(c.vt, mvec(c.V.Mt, c.vt, c.V.p))])
firing = sorted(I.items()); print("M2 firing modules:", len(firing))
by_locus = defaultdict(list)
for (lc, al), i in firing: by_locus[lc].append((al, i))
n = ok = nz = 0
for lc, lst in by_locus.items():
    h1, ct = cc.cocycle(lc, rels, 3, N, zeta, p)
    for (alA, iA), (alB, iB) in itertools.combinations_with_replacement(lst, 2):
        if iA != iB: continue
        VA = my_module(B1, lc, alA, ct, N, zeta, p, dual=(iA < 0)); VB = my_module(B1, lc, alB, ct, N, zeta, p, dual=(iA < 0))
        ra, rb = classes(VA), classes(VB)
        if len(ra) != 1 or len(rb) != 1: continue
        a, b = ra[0], rb[0]; e = relative_lift(a)
        if e is None or relative_lift(b) is None: continue
        eta = add(add(alA, alB), neg(lc)); eta = neg(eta) if iA > 0 else eta
        Vh = char_module(B1, eta, N, zeta, p); rh = classes(Vh)
        if len(rh) != 1: continue
        h = rh[0]
        y1 = Yval(B1, C1, z1, Evaluator(VA, a), Evaluator(VB, b), Evaluator(Vh, h), e, p)
        VA2, VB2, Vh2 = up_module(VA), up_module(VB), up_module(Vh)
        a2, b2, h2 = up_cocycle(a, VA2), up_cocycle(b, VB2), up_cocycle(h, Vh2)
        e2 = relative_lift(a2); assert e2 is not None
        y2 = Yval(B2, C2, z2, Evaluator(VA2, a2), Evaluator(VB2, b2), Evaluator(Vh2, h2), e2, p)
        # coboundary invariance on the twisted module
        a3 = a.plus_coboundary([3, 7]); y3 = Yval(B1, C1, z1, Evaluator(VA, a3), Evaluator(VB, b.plus_coboundary([11, 5])), Evaluator(Vh, h.plus_coboundary([9])), relative_lift(a3), p)
        n += 1; ok += (y2 == 2 * y1 % p and y3 == y1); nz += (y1 != 0)
        print("locus", lc, "pair", alA, alB, "sign", iA, "eta", eta, "Y", y1, "Y(cover)", y2, "2Y", 2 * y1 % p, "cob", y3 == y1)
print("pullback law and coboundary invariance:", ok, "of", n, "; non-zero:", nz)
assert ok == n and n > 0
