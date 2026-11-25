"""B2007, POST HOC (labelled; written after halving729_run.txt showed L3 failing as worded, with the solver visibly imprecise:
6.000000215 for the exact top 6). The same sectors at mod 729, solved with shift-invert near each sector's top and tol = 0, 60
eigenvalues each; then a set-wise check: is every charged eigenvalue c within 1e-6 of half of some neutral eigenvalue below the
top, and every neutral one within 1e-6 of twice a charged one, counting multiplicities greedily?
    python3 -B halving729_posthoc.py > halving729_posthoc_run.txt"""
import json, pathlib, time
import numpy as np
from scipy.sparse import csr_matrix, coo_matrix
from scipy.sparse.linalg import eigsh
HERE = pathlib.Path(__file__).resolve().parent
d = json.loads((HERE / "orbits.json").read_text())["6"]; n = d["n"]; pC = np.array(d["C"]); pS = np.array(d["S"])
t0 = time.time()
P = lambda p: csr_matrix((np.ones(n), (p, np.arange(n))), shape=(n, n))
PC, PS = P(pC), P(pS); PCi = PC.T.tocsr()
W = PS @ PC + PCi @ PS + PS @ PC @ PC + PC @ PS + PC @ PS @ PC + PCi @ PS @ PCi
seen, cyc, fx = set(), [], []
for i in range(n):
    if i in seen: continue
    j, k = pC[i], pC[pC[i]]
    if j == i: fx.append(i); seen.add(i)
    else: cyc.append((i, j, k)); seen.update((i, j, k))
w = np.exp(2j * np.pi / 3); res = {}
for q, sigma in ((0, 5.95), (1, 2.975)):
    rows, cols, vals = [], [], []
    for c, (i, j, k) in enumerate(cyc):
        for t, idx in enumerate((i, j, k)): rows.append(idx); cols.append(c); vals.append(w ** (-q * t) / np.sqrt(3))
    m = len(cyc)
    if q == 0:
        for c, i in enumerate(fx): rows.append(i); cols.append(m + c); vals.append(1.0)
        m += len(fx)
    B = coo_matrix((np.array(vals, complex), (rows, cols)), shape=(n, m)).tocsc()
    M = (B.conj().T @ (W @ B)).tocsc(); M = (M + M.conj().T) / 2
    ev = eigsh(M, k=60, sigma=sigma, which="LM", return_eigenvectors=False, tol=0)
    res[q] = np.sort(ev.real)[::-1]
    print("sector q = %d: 60 eigenvalues nearest %.3f, from %.9f to %.9f  [%.0f s]" % (q, sigma, res[q][0], res[q][-1], time.time() - t0), flush=True)
neu = [x for x in res[0] if abs(x - 6) > 1e-6]; ch = list(res[1])
lo = max(min(neu) / 2, min(ch)); hi = min(max(neu) / 2, max(ch))
A = sorted(x / 2 for x in neu if lo - 1e-6 <= x / 2 <= hi + 1e-6); Bc = sorted(c for c in ch if lo - 1e-6 <= c <= hi + 1e-6)   # edge tolerance 1e-6 (first run: 1e-9, which cut the top pair; disclosed in FINDINGS)
i = j = matched = 0; worst = 0.0
while i < len(A) and j < len(Bc):
    if abs(A[i] - Bc[j]) < 1e-6: matched += 1; worst = max(worst, abs(A[i] - Bc[j])); i += 1; j += 1
    elif A[i] < Bc[j]: i += 1
    else: j += 1
print("top of the neutral sector: %.12f" % res[0][0])
np.save(HERE / "halving729_eigs_q0.npy", res[0]); np.save(HERE / "halving729_eigs_q1.npy", res[1])
print("over the common window [%.6f, %.6f]: half-neutral values %d, charged values %d, matched within 1e-6: %d (largest matched difference %.1e)" % (lo, hi, len(A), len(Bc), matched, worst))
