#!/usr/bin/env python3
"""WP-1.6: the eigenvalues beyond the bound at levels 40 and 48: their values to ten digits and the parity of their
sectors at each prime power of the level.

At level 40 the level-15 value is found again though 15 does not divide 40.  At level 48 the largest eigenvalue found to
level 100 stands.  For each: the eigenvalue by Lanczos' method at a tight tolerance; its eigenspace; the trace on it of
the central elements that are -1 modulo one prime power of the level and +1 modulo the other (the trace is minus the
dimension when the sector is odd there)."""
import json, math, pathlib, sys
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh
HERE = pathlib.Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))

def graph_with_action(N):
    def canon(a, b, c, d):
        x = (a % N, b % N, c % N, d % N); y = ((-a) % N, (-b) % N, (-c) % N, (-d) % N)
        return x if x <= y else y
    def coset(a, b, c, d): return min(canon(a, b, c, d), canon(-b, a - b, -d, c - d), canon(b - a, -a, d - c, -c))
    start = coset(1, 0, 0, 1); ix = {start: 0}; todo = [start]; rows, cols = [], []
    while todo:
        nxt = []
        for g in todo:
            a, b, c, d = g; i = ix[g]
            for (p, q, r, s) in ((a, b, c, d), (-b, a - b, -d, c - d), (b - a, -a, d - c, -c)):
                h = coset(q, -p, s, -r); j = ix.get(h)
                if j is None: j = ix[h] = len(ix); nxt.append(h)
                rows.append(i); cols.append(j)
        todo = nxt
    n = len(ix); A = sp.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(n, n))
    def central(z):                                    # the scalar matrix z acts on the cosets
        perm = np.empty(n, dtype=np.int64)
        for g, i in ix.items(): perm[i] = ix[coset(z * g[0], z * g[1], z * g[2], z * g[3])]
        return perm
    return A, central

out = {}
for N, parts in ((40, (5, 8)), (48, (3, 16)), (15, (3, 5))):
    A, central = graph_with_action(N)
    w, X = eigsh(A, k=24, which="BE", tol=1e-13, maxiter=100000)
    non = [(abs(x), x) for x in w if abs(abs(x) - 3) > 1e-6]; lam = max(non)[1]
    sel = np.abs(w - lam) < 1e-7; E = X[:, sel]; E, _ = np.linalg.qr(E); m = int(sel.sum())
    row = {"vertices": A.shape[0], "the eigenvalue": float(lam), "its multiplicity among those found": m}
    for p, other in (parts, parts[::-1]):
        z = next(a for a in range(1, N) if a % p == p - 1 and a % other == 1)
        perm = central(z); tr = float(np.trace(E.T @ E[perm, :]))
        row["central element %d (-1 mod %d, +1 mod %d): trace" % (z, p, other)] = round(tr, 6)
    out[N] = row; print(N, row, flush=True)
s15 = (math.sqrt(5) - 1) / 2 + math.sqrt(2) * (1 + math.sqrt(5)) / 2
print("level 40 against 1/phi + sqrt2 phi = %.12f: differ by %.2e" % (s15, abs(abs(out[40]["the eigenvalue"]) - s15)))
print("level 48 against 1 + 2 cos 15 degrees = %.12f: differ by %.2e" % (1 + 2 * math.cos(math.pi / 12), abs(abs(out[48]["the eigenvalue"]) - (1 + 2 * math.cos(math.pi / 12)))))
json.dump(out, open(HERE / "the_sectors_at_40_and_48.json", "w"), indent=1)
