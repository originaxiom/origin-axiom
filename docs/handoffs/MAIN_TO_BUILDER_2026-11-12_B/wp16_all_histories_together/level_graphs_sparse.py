#!/usr/bin/env python3
"""WP-1.6: the three-valent graph of the moves at higher levels, by a sparse method.

For each level N: the graph (vertices the cosets g<U> of SL(2, Z/N) modulo its sign, each joined to g U^k S <U> for
k = 0, 1, 2), built by walking it from the identity; its extreme eigenvalues by Lanczos' method (ARPACK), sixteen from
each end; the largest in modulus below 3, and whether it is beyond Ramanujan's bound 2 sqrt 2.  An eigenvalue of level
d is an eigenvalue of every multiple of d, so what is NEW at a level is told apart from what its divisors already hold.
Controls: the graph is three-valent and symmetric; the number of vertices is |SL(2, Z/N)| / 6 (N > 2); at levels 14 to
32 the answer must be the dense computation's (level_graphs_further.json).  Double precision.  No measured number."""
import json, math, pathlib, sys, time
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh
HERE = pathlib.Path(__file__).resolve().parent
BOUND = 2 * math.sqrt(2)


def order_sl2(N):
    n, out, p = N, N ** 3, 2
    while p * p <= n:
        if n % p == 0:
            out = out // (p * p) * (p * p - 1)
            while n % p == 0: n //= p
        p += 1
    if n > 1: out = out // (n * n) * (n * n - 1)
    return out


def graph(N):
    def canon(a, b, c, d):
        x = (a % N, b % N, c % N, d % N); y = ((-a) % N, (-b) % N, (-c) % N, (-d) % N)
        return x if x <= y else y
    def coset(a, b, c, d):
        return min(canon(a, b, c, d), canon(-b, a - b, -d, c - d), canon(b - a, -a, d - c, -c))          # g, gU, gU^2
    start = coset(1, 0, 0, 1); ix = {start: 0}; todo = [start]; rows, cols = [], []
    while todo:
        nxt = []
        for g in todo:
            a, b, c, d = g; i = ix[g]
            for (p, q, r, s) in ((a, b, c, d), (-b, a - b, -d, c - d), (b - a, -a, d - c, -c)):         # g U^k
                h = coset(q, -p, s, -r)                                                               # (g U^k) S
                j = ix.get(h)
                if j is None:
                    j = ix[h] = len(ix); nxt.append(h)
                rows.append(i); cols.append(j)
        todo = nxt
    n = len(ix); A = sp.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(n, n))
    assert abs(A - A.T).sum() == 0 and np.allclose(np.asarray(A.sum(1)).ravel(), 3), "not three-valent and symmetric"
    return A


if __name__ == "__main__":
    levels = [int(a) for a in sys.argv[1:]] or list(range(14, 101))
    dense = json.loads((HERE / "level_graphs_further.json").read_text()) if (HERE / "level_graphs_further.json").exists() else {}
    out = {}
    if (HERE / "level_graphs_sparse.json").exists(): out = {int(k): v for k, v in json.loads((HERE / "level_graphs_sparse.json").read_text()).items()}
    for N in levels:
        if N in out: continue
        t0 = time.time(); A = graph(N); n = A.shape[0]
        assert N <= 2 or n == order_sl2(N) // 6, ("the number of vertices is not |SL(2, Z/N)| / 6", N, n)
        k = min(32, n - 2)
        w = eigsh(A, k=k, which="BE", return_eigenvectors=False, tol=1e-10, maxiter=20000)
        w = np.sort(w); non = [x for x in w if abs(abs(x) - 3) > 1e-6]
        lam = max(non, key=abs)
        beyond = sorted({round(float(x), 6) for x in non if abs(x) > BOUND + 1e-8}, key=abs, reverse=True)
        row = {"vertices": n, "largest in modulus below 3": round(float(lam), 6), "within 2 sqrt 2": bool(abs(lam) <= BOUND + 1e-8), "beyond the bound": beyond,
               "seconds": round(time.time() - t0, 1)}
        if str(N) in dense: row["the dense computation agrees"] = bool(abs(abs(lam) - dense[str(N)]["largest eigenvalue in modulus below 3"]) < 1e-5)
        out[N] = row
        print("level %3d: %6d vertices; largest below 3: %+.6f  %-7s %s%s  (%.0fs)" % (N, n, lam, "within" if row["within 2 sqrt 2"] else "BEYOND", beyond if beyond else "",
              "" if "the dense computation agrees" not in row else "  [dense agrees: %s]" % row["the dense computation agrees"], time.time() - t0), flush=True)
        json.dump(out, open(HERE / "level_graphs_sparse.json", "w"), indent=1)
