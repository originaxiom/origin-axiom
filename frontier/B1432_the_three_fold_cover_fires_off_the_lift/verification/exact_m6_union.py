#!/usr/bin/env python3
"""Exact index over Q(zeta_40) of every M_6 module that fires at ANY of the primes 1481, 1721 (1721 is the bad prime:
its firing set contains the 960 spurious ones). Stage 1 builds the union; stage 2 (slice k of K) evaluates exactly."""
import os, sys, json, time
os.environ['OA_CYC'] = '40'
import cover_census as cc
from myindex import index as pindex
n, N = 6, 40
ng, rels, mu, lam, tau = cc.cover(n); chars = cc.characters(rels, mu, ng, N)
Lr = [cc.letters(r) for r in rels]; Lm = cc.letters(mu); Ll = cc.letters(lam)
if sys.argv[1] == "union":
    tab = {}
    for p in (1481, 1721):
        z = pow(cc.primroot(p), (p - 1) // N, p)
        for lc in chars:
            h1, ct = cc.cocycle(lc, rels, ng, N, z, p)
            for al in chars:
                i, _, _ = pindex(cc.module(lc, al, ct, ng, N, z, p), Lr, Lm, Ll)
                if i: tab.setdefault((lc, al), {})[p] = i
        print(p, "done", flush=True)
    json.dump([[list(k[0]), list(k[1]), v.get(1481, 0), v.get(1721, 0)] for k, v in sorted(tab.items())], open("m6_union.json", "w"))
    print("union size", len(tab))
else:
    k, K = int(sys.argv[1]), int(sys.argv[2])
    import exact_lib as E
    U = json.load(open("m6_union.json")); out = []; t0 = time.time()
    for idx in range(k, len(U), K):
        lc, al, i1481, i1721 = U[idx]
        out.append([lc, al, i1481, i1721, E.exact_index(n, N, tuple(lc), tuple(al))])
        if len(out) % 100 == 0:
            json.dump(out, open("m6_exact_slice_%02d.json" % k, "w")); print(k, len(out), round(time.time() - t0), flush=True)
    json.dump(out, open("m6_exact_slice_%02d.json" % k, "w")); print(k, "DONE", len(out), round(time.time() - t0), flush=True)
