"""B1998, listening card 14 (main, 2026-11-25; data-free): the slowest decay of the unfolding on the largest orbit over the common point
on the cusp's leaf mod 2^k, k = 3..8; and, where it settles, the exact factor (FLINT) of the characteristic polynomial carrying it.
    python3 -B two_tower.py > two_tower_run.txt"""
import numpy as np, time, flint
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import eigs, eigsh
def orbits(p, k):
    N = p ** k; vals = np.arange(0, N, p)
    X, Y, Z = np.meshgrid(vals, vals, vals, indexing="ij"); X, Y, Z = X.ravel(), Y.ravel(), Z.ravel()
    on = (X * X + Y * Y + Z * Z - X * Y * Z) % N == 0
    pts = list(zip(X[on].tolist(), Y[on].tolist(), Z[on].tolist())); idx = {v: i for i, v in enumerate(pts)}
    Lm = np.array([idx[(v[0], v[2], (v[0] * v[2] - v[1]) % N)] for v in pts]); Rm = np.array([idx[(v[2], v[1], (v[1] * v[2] - v[0]) % N)] for v in pts])
    n = len(pts); parent = list(range(n))
    def find(a):
        while parent[a] != a: parent[a] = parent[parent[a]]; a = parent[a]
        return a
    for i in range(n):
        for j in (Lm[i], Rm[i]):
            ri, rj = find(i), find(int(j))
            if ri != rj: parent[ri] = rj
    return N, n, Lm, Rm, np.array([find(i) for i in range(n)])
def largest(N, n, Lm, Rm, roots):
    r, c = np.unique(roots, return_counts=True); big = r[np.argmax(c)]; mem = np.nonzero(roots == big)[0]; m = len(mem)
    loc = -np.ones(n, dtype=int); loc[mem] = np.arange(m)
    return m, mem, loc
t0 = time.time(); rows = []
for k in range(3, 9):
    N, n, Lm, Rm, roots = orbits(2, k); m, mem, loc = largest(N, n, Lm, Rm, roots)
    W = csr_matrix((np.ones(2 * m), (np.concatenate([loc[Lm[mem]], loc[Rm[mem]]]), np.concatenate([np.arange(m), np.arange(m)]))), shape=(m, m))
    if m <= 400:
        ev = np.linalg.eigvals(W.toarray())
    else:
        ev = eigs(W, k=min(10, m - 2), which="LM", return_eigenvectors=False, tol=1e-10, maxiter=200000)
    mods = sorted(np.abs(ev), reverse=True); slow = max([x for x in mods if x < 2 - 1e-6], default=0.0)
    S = (W + W.T)
    es = np.sort(np.linalg.eigvalsh(S.toarray()))[::-1] if m <= 400 else np.sort(eigsh(S, k=min(4, m - 2), which="LA", return_eigenvectors=False, tol=1e-10, maxiter=200000))[::-1]
    gap = es[0] - next((e for e in es[1:] if e < es[0] - 1e-8), es[0])
    rows.append((k, N, n, m, slow))
    print("mod %3d (k = %d): %6d points over the common point; largest orbit %6d; W+ largest moduli %s; slowest decay ratio %.6f; W+- gap %.4f  [%.0f s]" % (
        N, k, n, m, [round(float(x), 4) for x in mods[:6]], slow / 2, gap, time.time() - t0), flush=True)
settled = [rows[i] for i in range(len(rows) - 2) if abs(rows[i][4] - rows[i + 1][4]) < 1e-6 and abs(rows[i][4] - rows[i + 2][4]) < 1e-6]
print("SUMMARY T1: settled at three consecutive levels: %s" % (["mod %d: %.6f" % (r[1], r[4] / 2) for r in settled] or "no"))
if settled:
    k = settled[0][0]; N, n, Lm, Rm, roots = orbits(2, k); m, mem, loc = largest(N, n, Lm, Rm, roots)
    if m <= 2000:
        Wl = [[0] * m for _ in range(m)]
        for j, i in enumerate(mem): Wl[loc[Lm[i]]][j] += 1; Wl[loc[Rm[i]]][j] += 1
        cp = flint.fmpz_mat(Wl).charpoly(); content, facs = cp.factor()
        target = settled[0][4]
        for f, e in facs:
            rts = np.roots([int(x) for x in reversed(f.coeffs())]) if f.degree() > 0 else []
            if any(abs(abs(z) - target) < 1e-6 for z in rts):
                print("T2: at mod %d (orbit %d) the settled modulus %.9f is carried by the irreducible factor of degree %d (multiplicity %d), coefficients (constant first) %s" % (
                    N, m, target, f.degree(), e, [int(x) for x in f.coeffs()]))
    else:
        print("T2: the smallest settled level's orbit (%d) is beyond this run's exact step" % m)
