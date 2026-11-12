#!/usr/bin/env python3
"""WP-1.6: which sector carries the eigenvalue beyond Ramanujan's bound at level 15?

The level's three-valent graph has an eigenvalue 2.90628 > 2 sqrt 2.  Its eigenspace is carried to itself by the group
acting on the cosets.  SL(2, Z/15) = SL(2, Z/3) x SL(2, Z/5); its centre has four elements, +-1 and +-4, and 4 is +1
modulo 3 and -1 modulo 5.  So the trace of the central element 4 on the eigenspace says whether the sector is odd at
level 5 (and then, being even as a whole, odd at level 3 too): a JOIN OF TWO ODD SECTORS, or even at both.
Also computed: the eigenvalue's multiplicity, the traces of an element of level 3 only and of level 5 only, and the same
at level 29 and 30.  Double precision."""
import json, math, pathlib, sys
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from level_graphs_further import mm, neg, eye, L, R, S, U, Ui

def graph(N):
    red = lambda g: tuple(tuple(x % N for x in r) for r in g)
    canon = lambda g: min(red(g), red(neg(g)))
    one = canon(eye(2)); G = {one}; fr = [one]
    while fr:
        nxt = []
        for g in fr:
            for h in (L, R):
                x = canon(mm(g, h))
                if x not in G: G.add(x); nxt.append(x)
        fr = nxt
    coset = lambda g: min(canon(g), canon(mm(g, U)), canon(mm(g, Ui)))
    V = sorted({coset(g) for g in G}); ix = {v: i for i, v in enumerate(V)}
    Adj = np.zeros((len(V), len(V)))
    for v in V:
        for k in range(3):
            g = v
            for _ in range(k): g = mm(g, U)
            Adj[ix[v], ix[coset(mm(g, S))]] += 1
    def perm(z):                                   # the action of a group element on the cosets, from the left
        P = np.zeros((len(V), len(V)))
        for v in V: P[ix[coset(mm(z, v))], ix[v]] = 1
        return P
    return V, Adj, perm

out = {}
for N, facs in ((15, (3, 5)), (30, (2, 3, 5)), (29, (29,))):
    V, Adj, perm = graph(N); w, X = np.linalg.eigh(Adj)
    lam = max((x for x in w if abs(abs(x) - 3) > 1e-7), key=abs)           # the eigenvalue of largest modulus below 3, with its sign
    sel = np.abs(w - lam) < 1e-7; E = X[:, sel]; m = int(sel.sum()); neg_too = int((np.abs(w + lam) < 1e-7).sum())
    row = {"vertices": len(V), "the eigenvalue": round(float(lam), 9), "its multiplicity": m, "multiplicity of its negative": neg_too,
           "rate of the sector it gives": round(float((abs(lam) + math.sqrt(lam * lam - 8)) / 4), 9), "sqrt 3 / 2": round(math.sqrt(3) / 2, 9)}
    # candidates for a closed form
    row["lam^2"] = round(float(lam * lam), 9)
    if N % 15 == 0:
        z = None
        for a in range(2, N):
            if (a * a) % N == 1 and a % 3 == 1 and a % 5 == 4: z = a; break
        Pz = perm(((z, 0), (0, z))); row["the central element that is +1 mod 3 and -1 mod 5"] = z
        row["its trace on the eigenspace"] = round(float(np.trace(E.T @ Pz @ E)), 6)
        row["so the sector is"] = "odd at level 3 and odd at level 5: a join of two odd sectors" if abs(np.trace(E.T @ Pz @ E) + m) < 1e-6 else ("even at both" if abs(np.trace(E.T @ Pz @ E) - m) < 1e-6 else "mixed")
    out[N] = row; print(N, row, flush=True)
json.dump(out, open(HERE / "the_sector_at_15.json", "w"), indent=1)
