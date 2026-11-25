"""B2001, listening card 16 (main, 2026-11-25; data-free): the charge sectors of the whole's covariant unfolding on the cusp's leaf.
W6 = sum_k C^k (P_L + P_R) C^-k and W12 = the same with the inverse moves, on functions on the orbit; decomposed into the
eigenspaces of the cyclic exchange C (x,y,z) -> (y,z,x); per sector: dimension, top modulus, slowest decay below the top.
    python3 -B sectors.py > sectors_run.txt"""
import time
import numpy as np
from scipy.sparse import csr_matrix
t0 = time.time()
def leaf(N, start):
    L = lambda v: (v[0], v[2], (v[0] * v[2] - v[1]) % N); R = lambda v: (v[2], v[1], (v[1] * v[2] - v[0]) % N)
    Li = lambda v: (v[0], (v[0] * v[1] - v[2]) % N, v[1]); Ri = lambda v: ((v[0] * v[1] - v[2]) % N, v[1], v[0])
    if start is None:
        pts = [(x, y, z) for x in range(N) for y in range(N) for z in range(N) if (x*x + y*y + z*z - x*y*z) % N == 0 and (x, y, z) != (0, 0, 0)]
    else:
        seen, todo = {start}, [start]
        while todo:
            v = todo.pop()
            for g in (L, R, Li, Ri):
                u = g(v)
                if u not in seen: seen.add(u); todo.append(u)
        pts = sorted(seen)
    idx = {v: i for i, v in enumerate(pts)}
    perm = lambda g: np.array([idx[g(v)] for v in pts])
    return pts, idx, {"L": perm(L), "R": perm(R), "Li": perm(Li), "Ri": perm(Ri), "C": perm(lambda v: (v[1], v[2], v[0]))}
def P(p):
    n = len(p); return csr_matrix((np.ones(n), (p, np.arange(n))), shape=(n, n))
w = np.exp(2j * np.pi / 3)
def run(N, start, label):
    pts, idx, pm = leaf(N, start); n = len(pts)
    PC = P(pm["C"]); PCi = PC.T
    W2 = P(pm["L"]) + P(pm["R"]); W4 = W2 + P(pm["Li"]) + P(pm["Ri"])
    W6 = W2 + PC @ W2 @ PCi + PCi @ W2 @ PC; W12 = W4 + PC @ W4 @ PCi + PCi @ W4 @ PC
    comm = max(abs(W6 @ PC - PC @ W6).max(), abs(W12 @ PC - PC @ W12).max())
    # sector bases
    seen, cyc, fixed = set(), [], []
    for i in range(n):
        if i in seen: continue
        j, k = pm["C"][i], pm["C"][pm["C"][i]]
        if j == i: fixed.append(i); seen.add(i)
        else: cyc.append((i, j, k)); seen.update((i, j, k))
    out = {}
    for name, W in (("W6", W6), ("W12", W12)):
        Wd = W.toarray(); top = 6 if name == "W6" else 12; specs = {}
        for q in range(3):
            cols = []
            for (i, j, k) in cyc:
                b = np.zeros(n, complex); b[i], b[j], b[k] = 1, w ** (-q), w ** (-2 * q); cols.append(b / np.sqrt(3))
            if q == 0:
                for i in fixed:
                    b = np.zeros(n, complex); b[i] = 1; cols.append(b)
            B = np.array(cols).T
            M = B.conj().T @ Wd @ B
            ev = np.linalg.eigvals(M); specs[q] = ev
            mods = np.sort(np.abs(ev))[::-1]
            slow = max([m for m in mods if m < top - 1e-9], default=0.0)
            out[(name, q)] = (B.shape[1], mods[0] / top, slow / top)
        pair = np.max(np.abs(np.sort_complex(specs[1]) - np.sort_complex(np.conj(specs[2])))) if len(specs[1]) else 0.0
        out[(name, "pair")] = pair
    print("%s: orbit %d points (C-fixed %d, C-cycles %d); [W, C] = %s" % (label, n, len(fixed), len(cyc), comm))
    for name in ("W6", "W12"):
        row = "; ".join("q=%d: dim %d, top %.6f, slowest decay %.6f" % (q, *out[(name, q)]) for q in range(3))
        print("    %s: %s; charged pair spectra differ by %.1e" % (name, row, out[(name, "pair")]))
    print("    [%.0f s]" % (time.time() - t0), flush=True)
    return out
res = {}
for p in (5, 7, 11, 13):
    res[("p", p)] = run(p, None, "mod %d, the cusp's leaf minus the common point" % p)
for k in (3, 4, 5):
    res[("3", k)] = run(3 ** k, (3, 3, 3), "mod %d, the orbit of (3,3,3)" % 3 ** k)
for name in ("W6", "W12"):
    g3 = all(abs(r[(name, 0)][2] - r[(name, 1)][2]) > 1e-6 for r in res.values())
    print("SUMMARY G3 (%s): the neutral sector's slowest decay differs from the charged pair's at every level run: %s" % (name, g3))
    t = [res[("3", k)][(name, q)][2] for k in (4, 5) for q in range(3)]
    print("SUMMARY G4 (%s): per-sector slowest decays at mod 81 and mod 243 (q = 0, 1, 2): %s" % (name, [round(x, 6) for x in t]))
