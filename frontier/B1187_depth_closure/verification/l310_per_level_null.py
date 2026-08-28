#!/usr/bin/env python3
"""B1187 / TOMB-L310: per-level matched-null genericity (replaces the 5-point
convergence inference). At EVERY truncation level, Omega's d_MM is compared to a
100-seed matched null (same level sizes + consecutive-level edge counts). The
verdict-bearing claim of the kill is GENERICITY (Omega ~ null, drift and all),
not convergence of d_MM -- B189's C2 already typed d_MM as a drift."""
import csv, math, sys, json
import numpy as np

base = "/Users/dri/origin-axiom/frontier/B159_omega_class_dag"
nodes, level_of = [], {}
with open(f"{base}/omega_strict_full_class_nodes_L4_L10.csv") as fh:
    for row in csv.DictReader(fh):
        level_of[row[[k for k in row if 'id' in k.lower()][0]]] = int(row.get('level', row.get('L')))
idx = {nid: i for i, nid in enumerate(level_of)}
N = len(idx)
level = [0]*N
for nid, i in idx.items(): level[i] = level_of[nid]
succ = [set() for _ in range(N)]
with open(f"{base}/omega_strict_full_class_edges_L4_L10.csv") as fh:
    for row in csv.DictReader(fh):
        if row["source"] in idx and row["target"] in idx:
            succ[idx[row["source"]]].add(idx[row["target"]])

def mm_fraction(d):
    return math.gamma(d+1)*math.gamma(d/2)/(4*math.gamma(3*d/2))
def d_from_r(r, lo=1.5, hi=8.0):
    if r >= mm_fraction(lo): return lo
    if r <= mm_fraction(hi): return hi
    for _ in range(60):
        m = (lo+hi)/2
        lo, hi = (m, hi) if mm_fraction(m) > r else (lo, m)
    return (lo+hi)/2

def omega_d(keepmax):
    keep = [u for u in range(N) if level[u] <= keepmax]; ks = set(keep); reach = {}
    def R(u):
        if u in reach: return reach[u]
        s = set()
        for v in succ[u]:
            if v in ks: s.add(v); s |= R(v)
        reach[u] = s; return s
    rel = sum(len(R(u)) for u in keep); n = len(keep)
    return d_from_r(rel/(n*(n-1))), n

sizes_all, edgecount_all = {}, {}
for u in range(N): sizes_all[level[u]] = sizes_all.get(level[u], 0) + 1
for u in range(N):
    for v in succ[u]:
        if level[v] == level[u] + 1:
            edgecount_all[(level[u], level[v])] = edgecount_all.get((level[u], level[v]), 0) + 1

def null_d(keepmax, seed):
    g = np.random.default_rng(seed)
    sizes = {L: c for L, c in sizes_all.items() if L <= keepmax}
    ec = {k: m for k, m in edgecount_all.items() if k[1] <= keepmax}
    nb = [(L, i) for L in sorted(sizes) for i in range(sizes[L])]
    ix = {nd: k for k, nd in enumerate(nb)}; Nn = len(nb)
    out = [set() for _ in range(Nn)]
    for (La, Lb), m in ec.items():
        srcs = [ix[(La, i)] for i in range(sizes[La])]
        tgts = [ix[(Lb, j)] for j in range(sizes[Lb])]
        for _ in range(m): out[g.choice(srcs)].add(int(g.choice(tgts)))
    reach = {}
    def R(u):
        if u in reach: return reach[u]
        s = set()
        for v in out[u]: s.add(v); s |= R(v)
        reach[u] = s; return s
    rel = sum(len(R(u)) for u in range(Nn))
    return d_from_r(rel/(Nn*(Nn-1)))

import sys as _s; _s.setrecursionlimit(20000)
res = {"per_level": []}
print(f"{'L':>4} {'N':>4} {'Omega':>7} {'null mean':>10} {'null std':>9} {'z':>6}")
for Lmax in (6, 7, 8, 9, 10):
    dO, n = omega_d(Lmax)
    nulls = [null_d(Lmax, s) for s in range(100)]
    mu, sd = float(np.mean(nulls)), float(np.std(nulls))
    z = (dO - mu)/sd if sd > 0 else 0.0
    res["per_level"].append({"L": Lmax, "N": n, "omega": round(dO,3),
                             "null_mean": round(mu,3), "null_std": round(sd,3),
                             "z": round(z,2)})
    print(f"{Lmax:>4} {n:>4} {dO:>7.3f} {mu:>10.3f} {sd:>9.3f} {z:>6.2f}")
zmax = max(abs(r["z"]) for r in res["per_level"])
res["verdict"] = {"max_abs_z": round(zmax, 2), "generic_at_every_level": bool(zmax < 4)}
print(f"max |z| across levels = {zmax:.2f} -> genericity {'HOLDS' if zmax < 4 else 'FAILS'} at every measured level")
json.dump(res, open("l310_per_level_null.json", "w"), indent=1)
print("DONE")
