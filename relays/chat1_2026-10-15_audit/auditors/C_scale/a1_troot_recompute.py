"""Audit A1: recompute T-ROOT's c = 6 numbers from the saved (Vol, CS) data with independent code, and tabulate
what 'selects' would mean under alternative definitions (mode, majority, 90%, 99%).  Also separate the word weight's
contribution from the action's (root share as c -> 0)."""
import json, math, sys
import numpy as np

DATA = sys.argv[1]
d = json.load(open(DATA))
words = list(d)
n = np.array([len(w) for w in words], float)
vol = np.array([d[w][0] for w in words])
cs = np.array([d[w][1] for w in words])

# independent Lyndon count by Moebius formula
def mobius(k):
    res, p, m = 1, 2, k
    while p * p <= m:
        if m % p == 0:
            m //= p
            if m % p == 0:
                return 0
            res = -res
        p += 1
    if m > 1:
        res = -res
    return res
Ln = {m: sum(mobius(e) * 2 ** (m // e) for e in range(1, m + 1) if m % e == 0) // m for m in range(2, 19)}
print("Lyndon counts by formula:", Ln, "total", sum(Ln.values()), "data:", len(words))
from collections import Counter
cnt = Counter(len(w) for w in words)
assert all(cnt[m] == Ln[m] for m in Ln), "count mismatch"

# all words Lyndon?
def is_lyndon(w): return all(w < w[i:] + w[:i] for i in range(1, len(w)))
assert all(is_lyndon(w) for w in words)
iroot = words.index("LR")
print("root Vol, CS:", vol[iroot], cs[iroot], " argmin vol:", words[int(np.argmin(vol))])
srt = np.argsort(vol)[:6]
print("6 smallest volumes:", [(words[i], round(vol[i], 6)) for i in srt])

logw = {"A": -n * math.log(2), "B": -n * math.log(3),
        "C": np.array([-math.log(len(w) * (len(w) - 1) * Ln[len(w)]) for w in words])}

def dist(c, k):
    e = logw[k] - c * vol / (6 * math.pi)
    q = np.exp(e - e.max())
    return q / q.sum()

chiral = np.abs(cs) > 1e-6
print("\n== c = 6 ==")
for k in "ABC":
    q = dist(6, k)
    order = np.argsort(-q)
    neff = math.exp(-(q[q > 0] * np.log(q[q > 0])).sum())
    top = [(words[i], round(q[i], 4)) for i in order[:4]]
    print(f"{k}: p_root={q[iroot]:.4f}  f_chiral={q[chiral].sum():.4f}  N_eff={neff:.2f}  mode={words[order[0]]}  "
          f"root/second={q[order[0]]/q[order[1]]:.2f}  top4={top}")

print("\n== is the root the modal thread at every c?  (grid 0..1000) ==")
for k in "ABC":
    ok = all(int(np.argmax(dist(c, k))) == iroot for c in [0.0, 0.01, 0.1, 0.5, 1, 2, 4, 6, 8, 16, 64, 256, 1000])
    print(k, "root is the mode at every c on the grid:", ok)

print("\n== the word weight's own root share (c = 0, truncated at n<=18) vs c = 6 ==")
for k in "ABC":
    print(k, f"p_root(c=0)={dist(0.0, k)[iroot]:.4f}  p_root(c=6)={dist(6, k)[iroot]:.4f}")

print("\n== thresholds for 'select' = share >= level ==")
def thr(level, k):
    lo, hi = 1e-6, 5000.0
    if dist(lo, k)[iroot] >= level: return 0.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if dist(mid, k)[iroot] >= level: hi = mid
        else: lo = mid
    return hi
for k in "ABC":
    print(k, {lv: round(thr(lv, k), 2) for lv in (0.5, 0.9, 0.99)})

print("\n== level footprint at c = 6 under (A): 1 - Re Z(k)/Z(0), phase exp(2 pi i k CS/pi^2) ==")
q = dist(6, "A")
PI2 = math.pi ** 2
print({kk: round(float(1 - (q * np.cos(2 * math.pi * kk * cs / PI2)).sum()), 4) for kk in range(1, 7)})
print("imag part of Z(k)/Z(0) (should be ~0 by mirror pairing):",
      max(abs(float((q * np.sin(2 * math.pi * kk * cs / PI2)).sum())) for kk in range(1, 13)))
