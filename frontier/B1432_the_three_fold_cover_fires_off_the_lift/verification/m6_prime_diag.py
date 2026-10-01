#!/usr/bin/env python3
"""Which prime disagrees on M6, on which modules, and why."""
import sys, json
from collections import Counter
import cover_census as cc
from myindex import index
n, N = 6, 40
ng, rels, mu, lam, tau = cc.cover(n)
Lr = [cc.letters(r) for r in rels]; Lm = cc.letters(mu); Ll = cc.letters(lam)
chars = cc.characters(rels, mu, ng, N)
P = [1481, 1601, 1721, 2081, 2161, 2281]
assert all(cc.is_prime(p) and p % N == 1 for p in P)
zeta = {p: pow(cc.primroot(p), (p - 1) // N, p) for p in P}
coc = {p: {c: cc.cocycle(c, rels, ng, N, zeta[p], p) for c in chars} for p in P}
h1bad = {p: [c for c in chars if coc[p][c][0] != 1] for p in P}
print("loci with h1 != 1 per prime:", {p: len(v) for p, v in h1bad.items()}, flush=True)
tab = {}
for p in P:
    T = {}
    for lc in chars:
        ct = coc[p][lc][1]
        for al in chars:
            i, dV, dVs = index(cc.module(lc, al, ct, ng, N, zeta[p], p), Lr, Lm, Ll)
            if i: T[(lc, al)] = (i, dV, dVs)
    tab[p] = T
    print(p, "firing", len(T), flush=True)
ref = None
keys = set().union(*[set(t) for t in tab.values()])
maj = {}
for k in keys:
    vals = Counter(tab[p].get(k, (0,))[0] for p in P)
    maj[k] = vals.most_common(1)[0]
out = {}
for p in P:
    bad = [k for k in keys if tab[p].get(k, (0,))[0] != maj[k][0]]
    out[p] = dict(firing=len(tab[p]), disagree_with_majority=len(bad),
                  examples=[dict(lam=k[0], alpha=k[1], here=tab[p].get(k, (0,)), majority=maj[k][0]) for k in bad[:4]],
                  signatures_of_disagreeing=dict(Counter(str(tab[p].get(k, (0, None, None))[1:]) for k in bad)))
    print(p, json.dumps(out[p])[:900], flush=True)
print("majority firing count:", sum(1 for k in keys if maj[k][0] != 0), "| weakest majority:", min(v[1] for v in maj.values()), "of", len(P))
json.dump({str(p): v for p, v in out.items()}, open("m6_prime_diag.json", "w"), indent=1)
