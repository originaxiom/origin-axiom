#!/usr/bin/env python3
"""plumbing control: background_couplings on a synthetic 'background' made of ONE firing module of M2 repeated in all
six sectors.  M2 has no generation-shaped background; this exercises the code path, not the population."""
from interaction_census import *
eps, word, k = 1, "LR", 2
o, bgs, I, chars, N, rels, tau = level_census(eps, word, k); assert len(bgs) == 0
B = Bundle(Phi_of(eps, word, k)); C, z, _ = B.fundamental()
P = o["primes"]; zeta = {p: pow(cc.primroot(p), (p - 1) // N, p) for p in P}
for (lc, al), i in sorted(I.items())[:4]:
    key = (lc,) + (al,) * 6; cnt = (i,) * 6
    per = [background_couplings(B, C, z, key, cnt, rels, N, zeta[p], p) for p in P]
    nz = [[bool(pp[pair]["Y"]) for pp in per] for pair in per[0]]
    sym = all(pp[pair].get("Y_swapped", pp[pair]["Y"]) == pp[pair]["Y"] for pp in per for pair in pp)
    assert all(len(set(v)) == 1 for v in nz) and sym
    # the vectorised sum against the cell-by-cell reference, every pair, first prime
    p0 = P[0]; ct = cc.cocycle(lc, rels, 3, N, zeta[p0], p0)[1]
    V = my_module(B, lc, al, ct, N, zeta[p0], p0, dual=(i < 0)); a = classes(V)[0]; e = relative_lift(a)
    eta = tuple((2 * x - y) % N for x, y in zip(al, lc)); eta = tuple((-x) % N for x in eta) if i > 0 else eta
    Vh = char_module(B, eta, N, zeta[p0], p0); h = classes(Vh)[0]
    ref = Yval(B, C, z, Evaluator(V, a), Evaluator(V, a), Evaluator(Vh, h), e, p0)
    assert ref == per[0][("Q", "Q")]["Y"], (ref, per[0][("Q", "Q")]["Y"])
    print("module", lc, al, "sign", i, "pairs", len(per[0]), "non-zero at all three primes:", sum(v[0] for v in nz), "symmetric:", sym)
print("PLUMBING OK")
