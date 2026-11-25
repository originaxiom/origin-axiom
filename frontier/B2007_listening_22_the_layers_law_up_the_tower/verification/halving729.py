"""B2007, L3: at mod 729 (the orbit of (3,3,3), 52,488 points) the leading 30 eigenvalues of the six-move unfolding in the
neutral sector and in a charged sector (sparse eigsh), and whether the charged ones are half the neutral ones below the top.
    python3 -B halving729.py > halving729_run.txt"""
import json, pathlib, time
import numpy as np
from scipy.sparse import csr_matrix, coo_matrix
from scipy.sparse.linalg import eigsh
HERE = pathlib.Path(__file__).resolve().parent
d = json.loads((HERE / "orbits.json").read_text())["6"]; n = d["n"]; pC = np.array(d["C"]); pS = np.array(d["S"])
t0 = time.time()
P = lambda p: csr_matrix((np.ones(n), (p, np.arange(n))), shape=(n, n))
PC, PS = P(pC), P(pS); PCi = PC.T.tocsr()
# the six moves: R = sigma C, R^-1 = C^-1 sigma, L = sigma C^2, L^-1 = C sigma, X = C sigma C, X^-1 = C^-1 sigma C^-1 (B2004)
W = PS @ PC + PCi @ PS + PS @ PC @ PC + PC @ PS + PC @ PS @ PC + PCi @ PS @ PCi
assert abs(W - W.T).max() == 0
seen, cyc, fx = set(), [], []
for i in range(n):
    if i in seen: continue
    j, k = pC[i], pC[pC[i]]
    if j == i: fx.append(i); seen.add(i)
    else: cyc.append((i, j, k)); seen.update((i, j, k))
w = np.exp(2j * np.pi / 3); res = {}
for q in (0, 1):
    rows, cols, vals = [], [], []
    for c, (i, j, k) in enumerate(cyc):
        for t, idx in enumerate((i, j, k)): rows.append(idx); cols.append(c); vals.append(w ** (-q * t) / np.sqrt(3))
    m = len(cyc)
    if q == 0:
        for c, i in enumerate(fx): rows.append(i); cols.append(m + c); vals.append(1.0)
        m += len(fx)
    B = coo_matrix((np.array(vals, complex), (rows, cols)), shape=(n, m)).tocsr()
    M = (B.conj().T @ (W @ B)).tocsr(); M = (M + M.conj().T) / 2
    ev = eigsh(M, k=32, which="LA", return_eigenvectors=False, tol=1e-12, maxiter=500000)
    res[q] = np.sort(ev.real)[::-1]
    print("sector q = %d (dimension %d): leading eigenvalues %s  [%.0f s]" % (q, m, np.round(res[q][:8], 9).tolist(), time.time() - t0), flush=True)
neu = [x for x in res[0] if abs(x - 6) > 1e-8][:30]; ch = list(res[1][:30])
dev = max(abs(a / 2 - b) for a, b in zip(neu, ch))
print("L3: the leading 30 charged eigenvalues against half the leading neutral ones below the top: largest difference %.2e; equal to 1e-8: %s" % (dev, dev < 1e-8))
