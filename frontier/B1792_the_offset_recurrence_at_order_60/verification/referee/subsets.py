"""specificity read-out reproduced (own draws reimplementing B1741's generator; seeds 4501-4540) + the random-subset control"""
import json, math, random, itertools, pickle
from fractions import Fraction as Fr
import numpy as np
R = str(next(q for q in __import__("pathlib").Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())) + "/"
P = pickle.load(open(str(__import__("pathlib").Path(__file__).resolve().parent) + "/slope25.pkl", "rb")); rows = P["rows"]; T = np.array(P["T"]); S = np.array(P["S"])
M = pickle.load(open(str(__import__("pathlib").Path(__file__).resolve().parent) + "/lmin.pkl", "rb"))
L60 = sorted({k[0] for k in rows if M["order"][k[0]] == 60}, key=Fr)
L3 = math.log(3)
X = {}
for b in L60:
    v = []
    for k, rec in rows.items():
        if k[0] != b: continue
        for h in ("L_max", "L_2"):
            for u, dn, l in (("St", "S", "S"), ("St", "St", "St")):
                m = rec[h]["up" + u] + rec[h]["down" + dn] + rec[h]["lep" + l]
                for c in (0.0, L3): v.append(m[:4] + [m[4] + c, m[5] - c])
    X[b] = np.array(v) / S
    assert len(v) == 125 * 2 * 2 * 2
obs = {b: float((((X[b] - T / S) ** 2).sum(1)).min()) for b in L60}
def draws(seed, N=4000):
    rng = random.Random(seed); out = []
    for _ in range(N):
        tg = []
        for _s in range(3):
            while True:
                r2 = 10 ** rng.uniform(-3, -1); r1 = 10 ** rng.uniform(-6, -2.5)
                if r1 < r2: break
            tg += [r2, r1]
        out.append(np.log(np.array(tg)))
    return np.array(out)
seeds = list(range(4501, 4541))
D = np.concatenate([draws(s) for s in seeds]) / S          # 160 000 x 6
Mx = np.empty((len(D), len(L60)))
for j, b in enumerate(L60):
    x2 = (X[b] ** 2).sum(1)
    for s0 in range(0, len(D), 20000):
        t = D[s0:s0 + 20000]
        Mx[s0:s0 + 20000, j] = (x2[:, None] - 2 * X[b] @ t.T + (t ** 2).sum(1)[None, :]).min(0)
np.save(str(__import__("pathlib").Path(__file__).resolve().parent) + "/random_line_min.npy", Mx)
PRED = {"1/60", "7/60", "29/60", "7/12", "41/60", "47/60", "49/60", "11/12"}
def frac(sub):
    idx = [L60.index(b) for b in sub]; o = min(obs[b] for b in sub)
    hit = Mx[:, idx].min(1) <= o + 1e-9
    return o, hit.mean(), int(hit.sum())
for name, sub in (("predicted", PRED), ("other", set(L60) - PRED), ("all", set(L60))):
    o, f, n = frac(sub); print("%-9s min %.4f  random as low %.5f  hits %d" % (name, o, f, n))
mir = lambda b: str((Fr(3, 5) - Fr(b)) % 1)
pairs = sorted({tuple(sorted((b, mir(b)), key=Fr)) for b in L60}, key=lambda p: Fr(p[0]))
assert len(pairs) == 10
res = []
for comb in itertools.combinations(pairs, 4):
    sub = {b for p in comb for b in p}; o, f, n = frac(sub); res.append((f, o, sorted(sub, key=Fr)))
res.sort()
fp = frac(PRED)[1]
print("random-subset control over all 210 mirror-respecting 4-pair classes: %d have random-as-low <= predicted's %.5f; %d at or below 0.1%%; %d at or below 1%%" % (sum(1 for r in res if r[0] <= fp + 1e-12), fp, sum(1 for r in res if r[0] <= 0.001), sum(1 for r in res if r[0] <= 0.01)))
print("classes containing 47/60-49/60:", sum(1 for r in res if "47/60" in r[2]), "; their fractions range %.5f-%.5f" % (min(r[0] for r in res if "47/60" in r[2]), max(r[0] for r in res if "47/60" in r[2])))
for r in res[:5]: print("  best classes", "%.5f" % r[0], "%.2f" % r[1], r[2])
