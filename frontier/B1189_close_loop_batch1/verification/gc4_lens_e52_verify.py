#!/usr/bin/env python3
"""E52 lens on GC-4: attack the instrument.
(1) headline reproduction: r, d_MM, N, E, level sizes.
(2) BITE control on null B (leave-one-out; the cell only controlled null A).
(3) MCMC mixing check: null B at sweeps=20 vs sweeps=200 (chains start at Omega;
    under-mixing would bias the null toward Omega and/or shrink sd).
(4) independent re-derivation of gc4_locality_out.txt (no script was archived):
    edge |dabc| means vs random-pair means at L8->L9, L9->L10; Spearman(|dabc|,
    L10-cone Jaccard) at L7 and L8.
"""
import csv, math, ast, collections
import numpy as np
from scipy import stats as sps

BASE = str(__import__("pathlib").Path(__file__).resolve().parents[3] / "frontier/B159_omega_class_dag/")

def mm_fraction(d):
    return math.gamma(d+1)*math.gamma(d/2)/(4*math.gamma(3*d/2))

def d_from_r(r, lo=1.5, hi=8.0):
    if r >= mm_fraction(lo): return lo
    if r <= mm_fraction(hi): return hi
    for _ in range(60):
        m = (lo+hi)/2
        lo, hi = (m, hi) if mm_fraction(m) > r else (lo, m)
    return (lo+hi)/2

ids, level, abc = [], [], []
idx = {}
with open(BASE+"omega_strict_full_class_nodes_L4_L10.csv") as fh:
    for row in csv.DictReader(fh):
        idx[row["id"]] = len(ids); ids.append(row["id"])
        level.append(int(row["level"])); abc.append(ast.literal_eval(row["abc"]))
N = len(ids); level = np.array(level); abc = np.array(abc)
edges = []
with open(BASE+"omega_strict_full_class_edges_L4_L10.csv") as fh:
    for row in csv.DictReader(fh):
        edges.append((idx[row["source"]], idx[row["target"]]))
LEVELS = sorted(set(level.tolist()))
by_level = {L: np.where(level == L)[0].tolist() for L in LEVELS}
print("(1) N =", N, " E =", len(edges), " level sizes:", [len(by_level[L]) for L in LEVELS])
assert all(level[v] == level[u]+1 for u, v in edges), "non-consecutive edge found"

epair = collections.defaultdict(list)
for u, v in edges: epair[(level[u], level[u]+1)].append((u, v))
ORDER_DESC = sorted(range(N), key=lambda u: -level[u])

def reach(adj):
    R = [0]*N
    for u in ORDER_DESC:
        s = 0
        for v in adj[u]: s |= (1 << v) | R[v]
        R[u] = s
    return R

def d_of(adj):
    R = reach(adj)
    tot = sum(bin(x).count("1") for x in R)
    return tot/(N*(N-1)), d_from_r(tot/(N*(N-1))), R

def adj_from(elist):
    adj = [[] for _ in range(N)]
    for u, v in elist: adj[u].append(v)
    return adj

r_om, d_om, R_om = d_of(adj_from(edges))
print(f"    Omega r={r_om:.5f} d_MM={d_om:.4f}  (quoted 0.05276 / 3.936)")

def null_B(rng, sweeps=20):
    elist = []
    for (La, Lb), es in epair.items():
        cur = list(es); eset = set(cur); m = len(cur)
        for _ in range(sweeps*m):
            i, j = rng.integers(0, m, size=2)
            if i == j: continue
            (u1, v1), (u2, v2) = cur[i], cur[j]
            if v1 == v2 or u1 == u2: continue
            if (u1, v2) in eset or (u2, v1) in eset: continue
            eset.discard((u1, v1)); eset.discard((u2, v2))
            eset.add((u1, v2)); eset.add((u2, v1))
            cur[i], cur[j] = (u1, v2), (u2, v1)
        elist.extend(cur)
    # verify degree preservation
    return adj_from(elist)

def degs(adj):
    outd = tuple(len(a) for a in adj)
    ind = collections.Counter()
    for a in adj:
        for v in a: ind[v] += 1
    return outd, tuple(ind[u] for u in range(N))

d_ref = degs(adj_from(edges))

# (2)+(3): null B at 20 sweeps (same seeds as the cell: 2000+s) and at 200 sweeps
res20, res200 = [], []
for s in range(40):
    aB = null_B(np.random.default_rng(2000+s), sweeps=20)
    assert degs(aB) == d_ref, "degree not preserved!"
    res20.append(d_of(aB)[1])
for s in range(15):
    aB = null_B(np.random.default_rng(9000+s), sweeps=200)
    res200.append(d_of(aB)[1])
res20 = np.array(res20); res200 = np.array(res200)
print(f"\n(2) null B sweeps=20, 40 seeds (cell's seed line): {res20.mean():.4f} +- {res20.std():.4f}  (cell quoted 3.6351 +- 0.0055 at 100 seeds)")
z0 = (res20[0] - res20[1:].mean())/res20[1:].std()
print(f"    BITE control: null-B draw #0 vs null-B ensemble z = {z0:+.2f} (|z|<2 required)")
print(f"(3) null B sweeps=200, 15 seeds: {res200.mean():.4f} +- {res200.std():.4f}")
print(f"    mixing shift (200 vs 20 sweeps) = {res200.mean()-res20.mean():+.4f} "
      f"({abs(res200.mean()-res20.mean())/res20.std():.1f} x sd20)")
zB20 = (d_om - res20.mean())/res20.std(); zB200 = (d_om - res200.mean())/res200.std()
print(f"    z(Omega) vs sweeps=20: {zB20:.1f}   vs sweeps=200: {zB200:.1f}")

# (4) locality re-derivation (independent of the missing script)
def l1(u, v): return int(np.abs(abc[u]-abc[v]).sum())
for (a, b) in [(8, 9), (9, 10)]:
    es = epair[(a, b)]
    em = np.mean([l1(u, v) for u, v in es])
    rng = np.random.default_rng(0)
    src, tgt = by_level[a], by_level[b]
    rp = np.mean([l1(src[i], tgt[j]) for i in rng.integers(0, len(src), 20000)
                  for j in [rng.integers(0, len(tgt))]])
    print(f"\n(4) edge L{a}->L{b}: mean|dabc|={em:.2f} (n={len(es)})  all-random-pair mean={rp:.2f}"
          f"  (quoted {8.24 if a==8 else 10.62} vs {17.35 if a==8 else 25.94})")
m10 = sum(1 << u for u in by_level[10])
for L in (7, 8):
    nodes = by_level[L]
    dj, jc = [], []
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            a_, b_ = R_om[nodes[i]] & m10, R_om[nodes[j]] & m10
            un = bin(a_ | b_).count("1")
            dj.append(l1(nodes[i], nodes[j]))
            jc.append(bin(a_ & b_).count("1")/un if un else np.nan)
    rho, p = sps.spearmanr(dj, jc)
    print(f"    L{L}: Spearman(|dabc|, L10-cone Jaccard) = {rho:.3f} (p={p:.2e}, n={len(dj)} pairs)"
          f"  (quoted {-0.612 if L==7 else -0.619})")
