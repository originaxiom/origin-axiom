"""Audit check of M4: how much of each normalised weight sits at the truncation lengths 17-18, and how the band
fractions move when the cut is lowered (length <= 14, 16, 18). Reads t_root_threads.json (path in argv[1])."""
import json, math, sys
import numpy as np
thr = json.loads(open(sys.argv[1]).read())
words = list(thr)
def runs(w):
    k = 0
    while w[k] == w[k - 1]: k += 1
    u = w[k:] + w[:k]; rl, cur, n = [], u[0], 0
    for ch in u:
        if ch == cur: n += 1
        else: rl.append(n); cur, n = ch, 1
    rl.append(n); return rl
def cf(seq):
    x = 0.0
    for a in reversed(seq[1:]): x = 1.0 / (a + x)
    return seq[0] + x
def lagrange(w):
    a = runs(w); n = len(a); rep = 60 // n + 4
    return max(cf([a[(i + j) % n] for j in range(n * rep)]) + 1.0 / cf([a[(i - 1 - j) % n] for j in range(n * rep)]) for i in range(n))
lag = np.array([lagrange(w) for w in words]); vol = np.array([thr[w][0] for w in words]); n_arr = np.array([len(w) for w in words])
L_of_n = {}
for w in words: L_of_n[len(w)] = L_of_n.get(len(w), 0) + 1
for cut in (12, 14, 16, 18):
    sel = n_arr <= cut
    logw = {"A": -n_arr * math.log(2), "B": -n_arr * math.log(3),
            "C": np.array([-math.log(len(w) * (len(w) - 1) * L_of_n[len(w)]) for w in words])}
    for key in ("A", "B", "C"):
        for c in (6, 24):
            e = logw[key] - c * vol / (6 * math.pi); e = np.where(sel, e, -np.inf); q = np.exp(e - e[sel].max()); q /= q.sum()
            b = [q[lag < 3 - 1e-9].sum(), q[(lag >= 3 - 1e-9) & (lag < 3.6)].sum(), q[lag >= 3.6].sum()]
            per = [q[n_arr == k].sum() for k in range(2, cut + 1)]
            print(f"cut {cut:2d} ({key}) c={c:2d}: bands <3 {b[0]:.3f} 3-3.6 {b[1]:.3f} >3.6 {b[2]:.3f} | weight at last two lengths {per[-2]:.4f}, {per[-1]:.4f}; ratio last/prev {per[-1]/per[-2]:.3f}")
