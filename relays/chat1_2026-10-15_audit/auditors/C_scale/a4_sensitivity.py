import json, math, sys
import numpy as np
d = json.load(open(sys.argv[1]))
def lr(w): return min(w[i:] + w[:i] for i in range(len(w)))
words = list(d)
Ln = {}
for w in words: Ln[len(w)] = Ln.get(len(w), 0) + 1
n = np.array([len(w) for w in words], float); vol = np.array([d[w][0] for w in words])
iroot = words.index("LR")
logw = {"A": -n*math.log(2), "B": -n*math.log(3), "C": np.array([-math.log(len(w)*(len(w)-1)*Ln[len(w)]) for w in words])}
def dist(c, k, mask=None):
    e = logw[k] - c*vol/(6*math.pi)
    if mask is not None: e = np.where(mask, e, -np.inf)
    q = np.exp(e - e[np.isfinite(e)].max()); q = q/q.sum(); return q
def neff(q):
    q = q[q > 0]; return math.exp(-(q*np.log(q)).sum())
# (a) action vs word weight: N_eff and KL(c=6 || c=0)
for k in "ABC":
    q0, q6 = dist(0.0, k), dist(6, k)
    kl = float((q6[q6>0]*np.log(q6[q6>0]/q0[q6>0])).sum())
    print(f"{k}: N_eff c=0 {neff(q0):8.2f} -> c=6 {neff(q6):6.2f};  p_root {q0[iroot]:.3f} -> {q6[iroot]:.3f};  KL(c6||c0) = {kl:.3f} nats")
# (b) merge reversal pairs (one oriented manifold): keep one representative per {W, lr(rev W)}
keep = np.array([w <= lr(w[::-1]) for w in words])
print("reversal classes:", int(keep.sum()), "of", len(words), "words;", int((~keep).sum()), "words are the reverse-duplicate of another")
for k in "ABC":
    q = dist(6, k, keep)
    print(f"{k}: per-oriented-manifold counting, c=6: p_root = {q[iroot]:.4f}, N_eff = {neff(q):.2f}")
# (c) c-window where the root holds < 1/2 and N_eff > 3, per weight
for k in "ABC":
    rows = []
    for c in [6, 12, 16, 20, 24, 32, 48, 64]:
        q = dist(c, k); rows.append((c, round(float(q[iroot]), 3), round(neff(q), 1)))
    print(k, "(c, p_root, N_eff):", rows)
