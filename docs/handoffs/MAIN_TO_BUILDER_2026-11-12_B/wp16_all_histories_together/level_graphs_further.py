#!/usr/bin/env python3
"""WP-1.6: does the three-valent graph of the moves obey Ramanujan's bound at every level?  Levels 14 to 32.

By Z4 of the_weaves_zeta.py an even sector cancels at exactly 1/sqrt 2 when the level's graph has no eigenvalue beyond
2 sqrt 2 in that sector, and slower when it has one.  To level 13 it has none; at 13 the largest is 2.8256, against
2.8284.  This run goes on.  What would be found if the bound fails: a level, an eigenvalue above 2 sqrt 2, and so an even
sector that outlasts the bulk.  Double precision; the graph is checked three-valent and symmetric at every level.
level_graph() below is the function of the_weaves_zeta.py, copied whole (a test in the lock compares the two)."""
import json, math, pathlib, sys, time
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
def mm(A, B): return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))) for i in range(len(A)))
def neg(A): return tuple(tuple(-x for x in r) for r in A)
def eye(n): return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))
L, R = ((1, 1), (0, 1)), ((1, 0), (1, 1))
S, U = ((0, -1), (1, 0)), ((0, 1), (-1, -1))
Ui = mm(U, U)


def level_graph(N, move_edge=False):
    """the three-valent graph of level N: vertices are the cosets g<U> of PSL(2, Z/N); g<U> is joined to g U^k S <U>, k = 0, 1, 2"""
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
    if move_edge and len(V) > 3:
        a, b = np.argwhere(Adj > 0)[0]; Adj[a, b] -= 1; Adj[b, a] -= 1; c = (b + 1) % len(V); Adj[a, c] += 1; Adj[c, a] += 1
    return len(G), Adj


if __name__ == "__main__":
    bound = 2 * math.sqrt(2); out = {}
    for N in [int(a) for a in sys.argv[1:]] or range(14, 33):
        t0 = time.time(); order, Adj = level_graph(N)
        assert np.allclose(Adj, Adj.T) and np.allclose(Adj.sum(1), 3)
        ev = np.sort(np.linalg.eigvalsh(Adj))[::-1]; non = [x for x in ev if abs(abs(x) - 3) > 1e-7]
        lam = max(abs(x) for x in non); beyond = sorted({round(float(abs(x)), 6) for x in non if abs(x) > bound + 1e-9}, reverse=True)
        out[N] = {"vertices": int(Adj.shape[0]), "largest eigenvalue in modulus below 3": round(float(lam), 6), "within 2 sqrt 2": bool(lam <= bound + 1e-9), "eigenvalues beyond the bound": beyond[:8],
                  "how many beyond, with multiplicity": int(sum(1 for x in non if abs(x) > bound + 1e-9)), "two-coloured": bool(abs(ev[-1] + 3) < 1e-7)}
        print("level %2d: %5d vertices; largest below 3: %.6f  %s  %s  (%.0fs)" % (N, Adj.shape[0], lam, "within" if lam <= bound + 1e-9 else "BEYOND 2 sqrt 2 = 2.828427", beyond[:4] if beyond else "", time.time() - t0), flush=True)
        json.dump(out, open(HERE / "level_graphs_further.json", "w"), indent=1)
