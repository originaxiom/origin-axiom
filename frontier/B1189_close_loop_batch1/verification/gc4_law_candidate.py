#!/usr/bin/env python3
"""GC-4 follow-up: (a) replicate B189's exact null variant (with-replacement edge draws
collapsed into sets, 100 seeds) to tie back to the quoted 11 sigma; (b) sharpen the law
candidate: cone segregation -- same-level pairs' L10-cone overlap distribution + sibling
(shared-parent) cone overlap, Omega vs degree-preserving null (30 seeds)."""
import csv, math, collections
import numpy as np

BASE = "/Users/dri/origin-axiom/frontier/B159_omega_class_dag/"

def mm_fraction(d):
    return math.gamma(d+1)*math.gamma(d/2)/(4*math.gamma(3*d/2))

def d_from_r(r, lo=1.5, hi=8.0):
    if r >= mm_fraction(lo): return lo
    if r <= mm_fraction(hi): return hi
    for _ in range(60):
        m = (lo+hi)/2
        lo, hi = (m, hi) if mm_fraction(m) > r else (lo, m)
    return (lo+hi)/2

ids, level = [], []
idx = {}
with open(BASE+"omega_strict_full_class_nodes_L4_L10.csv") as fh:
    for row in csv.DictReader(fh):
        idx[row["id"]] = len(ids); ids.append(row["id"]); level.append(int(row["level"]))
N = len(ids); level = np.array(level)
edges = []
with open(BASE+"omega_strict_full_class_edges_L4_L10.csv") as fh:
    for row in csv.DictReader(fh):
        edges.append((idx[row["source"]], idx[row["target"]]))
LEVELS = sorted(set(level.tolist()))
by_level = {L: np.where(level == L)[0].tolist() for L in LEVELS}
sizes = {L: len(by_level[L]) for L in LEVELS}
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
    return d_from_r(tot/(N*(N-1))), R

def adj_from(elist):
    adj = [[] for _ in range(N)]
    for u, v in elist: adj[u].append(v)
    return adj

# ---- (a) B189's exact null: with-replacement draws into a set (duplicates collapse) ----
def null_b189(rng):
    adj = [set() for _ in range(N)]
    for (La, Lb), es in epair.items():
        srcs = by_level[La]; tgts = by_level[Lb]
        for _ in range(len(es)):
            adj[srcs[rng.integers(len(srcs))]].add(tgts[rng.integers(len(tgts))])
    return [list(s) for s in adj]

d_om, R_om = d_of(adj_from(edges))
ds = [d_of(null_b189(np.random.default_rng(5000+s)))[0] for s in range(100)]
ds = np.array(ds)
print(f"(a) B189-variant null (100 seeds): d_MM = {ds.mean():.4f} +- {ds.std():.4f} -> z(Omega {d_om:.3f}) = {(d_om-ds.mean())/ds.std():.1f}")
print(f"    (B189 quoted 3.782 +- 0.014, z ~ 11, 30 seeds)")

# ---- (b) law candidate: cone segregation into L10 ----
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
    return adj_from(elist)

m10 = sum(1 << u for u in by_level[10])

def cone_stats(R):
    """per level: (mean pairwise Jaccard of L10-cones over ALL same-level pairs,
                   disjoint-pair fraction, mean pairwise Jaccard over SIBLING pairs)"""
    out = {}
    # sibling pairs: children of the same parent (distinct)
    for L in LEVELS[1:-1]:  # levels 5..9 as child levels? we want pairs AT level L sharing a parent at L-1
        nodesL = by_level[L]
        cones = {u: R[u] & m10 for u in nodesL}
        js, disj = [], 0; npairs = 0
        for i in range(len(nodesL)):
            for j in range(i+1, len(nodesL)):
                a, b = cones[nodesL[i]], cones[nodesL[j]]
                un = bin(a | b).count("1"); it = bin(a & b).count("1")
                npairs += 1
                if it == 0: disj += 1
                if un: js.append(it/un)
        out[L] = [float(np.mean(js)) if js else np.nan, disj/npairs if npairs else np.nan]
    return out

def sibling_stats(adj, R):
    """mean Jaccard of full descendant cones over sibling pairs (same parent), per child level."""
    out = collections.defaultdict(list)
    for u in range(N):
        ch = adj[u]
        for i in range(len(ch)):
            for j in range(i+1, len(ch)):
                a, b = R[ch[i]], R[ch[j]]
                un = bin(a | b).count("1")
                if un: out[level[u]+1].append(bin(a & b).count("1")/un)
    return {L: float(np.mean(v)) for L, v in out.items()}

st_om = cone_stats(R_om)
sib_om = sibling_stats(adj_from(edges), R_om)
stB = collections.defaultdict(lambda: [[], []]); sibB = collections.defaultdict(list)
NS = 30
for s in range(NS):
    aB = null_B(np.random.default_rng(7000+s))
    dB, RB = d_of(aB)
    st = cone_stats(RB)
    for L in st:
        stB[L][0].append(st[L][0]); stB[L][1].append(st[L][1])
    sb = sibling_stats(aB, RB)
    for L in sb: sibB[L].append(sb[L])

print(f"\n(b) L10-cone segregation, Omega vs degree-preserving null ({NS} seeds):")
print(f"{'L':>3} | {'J_all Om':>8} {'J_all B':>14} {'z':>7} | {'disj Om':>8} {'disj B':>14} {'z':>7} | {'J_sib Om':>8} {'J_sib B':>14} {'z':>7}")
for L in LEVELS[1:-1]:
    jA = np.array(stB[L][0]); dA = np.array(stB[L][1]); sA = np.array(sibB.get(L, [np.nan]))
    zj = (st_om[L][0]-jA.mean())/jA.std() if jA.std() > 0 else np.nan
    zd = (st_om[L][1]-dA.mean())/dA.std() if dA.std() > 0 else np.nan
    zs = (sib_om.get(L, np.nan)-sA.mean())/sA.std() if sA.std() > 0 else np.nan
    print(f"{L:3d} | {st_om[L][0]:8.3f} {jA.mean():7.3f}+-{jA.std():5.3f} {zj:+7.1f} | {st_om[L][1]:8.3f} {dA.mean():7.3f}+-{dA.std():5.3f} {zd:+7.1f} | {sib_om.get(L, np.nan):8.3f} {sA.mean():7.3f}+-{sA.std():5.3f} {zs:+7.1f}")

# exact sharp statement: per-node L10-cone size distribution at L7/L8
print("\nper-node |cone ∩ L10| at L7 and L8 (Omega vs nullB mean):")
for L in (7, 8):
    om = sorted(bin(R_om[u] & m10).count("1") for u in by_level[L])
    print(f"  L{L} Omega: min={om[0]} med={om[len(om)//2]} max={om[-1]} mean={np.mean(om):.1f} (n={len(om)})")
