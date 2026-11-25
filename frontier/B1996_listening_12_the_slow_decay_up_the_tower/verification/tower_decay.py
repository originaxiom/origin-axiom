"""B1996 (main, 2026-11-25; data-free): the slowest decay of the unfolding on the largest orbit over the common point, mod 3^k
(k = 3, 4, 5) and 5^k (k = 3, 4): W+ = P_L + P_R by sparse Arnoldi (largest moduli), W+- = W+ + W+^T by eigsh (largest).
    python3 -B tower_decay.py > tower_decay_run.txt"""
import numpy as np, time
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import eigs, eigsh
def orbits_over_common_point(p, k):
    N = p ** k
    vals = np.arange(0, N, p)
    X, Y, Z = np.meshgrid(vals, vals, vals, indexing="ij")
    X, Y, Z = X.ravel(), Y.ravel(), Z.ravel()
    on = (X * X + Y * Y + Z * Z - X * Y * Z) % N == 0
    pts = list(zip(X[on].tolist(), Y[on].tolist(), Z[on].tolist()))
    idx = {v: i for i, v in enumerate(pts)}
    L = lambda v: (v[0], v[2], (v[0] * v[2] - v[1]) % N); R = lambda v: (v[2], v[1], (v[1] * v[2] - v[0]) % N)
    Lm = np.array([idx[L(v)] for v in pts]); Rm = np.array([idx[R(v)] for v in pts])
    n = len(pts); parent = list(range(n))
    def find(a):
        while parent[a] != a: parent[a] = parent[parent[a]]; a = parent[a]
        return a
    for i in range(n):
        for j in (Lm[i], Rm[i]):
            ri, rj = find(i), find(int(j))
            if ri != rj: parent[ri] = rj
    roots = np.array([find(i) for i in range(n)])
    return N, n, Lm, Rm, roots
t0 = time.time()
for p, ks in ((3, (3, 4, 5)), (5, (3, 4))):
    for k in ks:
        N, n, Lm, Rm, roots = orbits_over_common_point(p, k)
        r, counts = np.unique(roots, return_counts=True)
        big = r[np.argmax(counts)]; members = np.nonzero(roots == big)[0]; m = len(members)
        loc = -np.ones(n, dtype=int); loc[members] = np.arange(m)
        rows = np.concatenate([loc[Lm[members]], loc[Rm[members]]]); cols = np.concatenate([np.arange(m), np.arange(m)])
        W = csr_matrix((np.ones(2 * m), (rows, cols)), shape=(m, m))
        kk = min(8, m - 2)
        ev = eigs(W, k=kk, which="LM", return_eigenvectors=False, tol=1e-10, maxiter=100000)
        mods = sorted(np.abs(ev), reverse=True)
        slow = max([x for x in mods if x < 2 - 1e-6], default=0.0)
        S = W + W.T
        es = np.sort(eigsh(S, k=min(4, m - 2), which="LA", return_eigenvectors=False, tol=1e-10, maxiter=100000))[::-1]
        gap = es[0] - next((e for e in es[1:] if e < es[0] - 1e-8), es[0])
        print("mod %4d (p = %d, k = %d): %6d points over the common point; largest orbit %6d; W+ largest moduli %s; slowest decay ratio %.4f; W+- top %.4f, gap below it %.4f  [%.0f s]" % (
            N, p, k, n, m, [round(x, 4) for x in mods[:5]], slow / 2, es[0], gap, time.time() - t0), flush=True)
