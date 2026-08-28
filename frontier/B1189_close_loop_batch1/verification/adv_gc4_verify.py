#!/usr/bin/env python3
"""ADVERSARIAL re-derivation of GC-4 (independent code).

Independent choices vs the cell under review:
- degree-preserving null sampled by CURVEBALL trades (not swap-MCMC), different seeds;
- own bitset transitive closure; own bisection for d(r);
- checks: basic stats, r, d_MM, null means/sds/z, C(a,b) localization + 81% figure,
  reach-into-L10 fractions, two-sided control.
"""
import csv, math, collections
import numpy as np

BASE = "/Users/dri/origin-axiom/frontier/B159_omega_class_dag/"

# ---------- MM estimator (own implementation) ----------
def mm(d):  # Myrheim-Meyer expected ordering fraction, directed-pair convention (B189)
    return math.gamma(d + 1) * math.gamma(d / 2) / (4 * math.gamma(1.5 * d))

def d_of_r(r):
    lo, hi = 1.5, 8.0
    if r >= mm(lo): return lo
    if r <= mm(hi): return hi
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if mm(mid) > r: lo = mid
        else: hi = mid
    return 0.5 * (lo + hi)

# sanity of my own mm(): mm(4) should be ~ 0.04938 (=1/2 * known 2-sided value)
# known: Meyer d=4 ordering fraction (unordered convention) = 0.0988 -> directed = same number over N(N-1)... just print
print(f"[cal] mm(2)={mm(2):.6f} mm(4)={mm(4):.6f}")

# ---------- load ----------
nodes = []; lev = {}; abc = {}
with open(BASE + "omega_strict_full_class_nodes_L4_L10.csv") as fh:
    for row in csv.DictReader(fh):
        i = len(nodes); nodes.append(row["id"]); lev[i] = int(row["level"])
        abc[i] = tuple(int(x) for x in row["abc"].strip("[]").split(","))
idx = {nid: i for i, nid in enumerate(nodes)}
N = len(nodes)
E = []
with open(BASE + "omega_strict_full_class_edges_L4_L10.csv") as fh:
    for row in csv.DictReader(fh):
        E.append((idx[row["source"]], idx[row["target"]]))
LV = sorted(set(lev.values()))
byL = {L: [u for u in range(N) if lev[u] == L] for L in LV}
print(f"[data] N={N} E={len(E)} sizes={[len(byL[L]) for L in LV]} "
      f"all_consecutive={all(lev[v]==lev[u]+1 for u,v in E)} "
      f"dup_edges={len(E)-len(set(E))}")

epair = collections.defaultdict(list)
for u, v in E: epair[(lev[u], lev[v])].append((u, v))

DESC = sorted(range(N), key=lambda u: -lev[u])
Lmask = {L: sum(1 << u for u in byL[L]) for L in LV}

def closure(adj):
    R = [0] * N
    for u in DESC:
        s = 0
        for v in adj[u]: s |= (1 << v) | R[v]
        R[u] = s
    return R

def to_adj(elist):
    adj = [[] for _ in range(N)]
    for u, v in elist: adj[u].append(v)
    return adj

def stats(R):
    tot = 0; C = collections.Counter()
    for u in range(N):
        for L in LV:
            if L <= lev[u]: continue
            c = bin(R[u] & Lmask[L]).count("1")
            if c: C[(lev[u], L)] += c; tot += c
    r = tot / (N * (N - 1))
    return r, d_of_r(r), C

adjO = to_adj(E)
RO = closure(adjO)
rO, dO, CO = stats(RO)
print(f"[Omega] r={rO:.5f} d_MM={dO:.4f} total_comparable={sum(CO.values())}")

# ---------- null 1: B189 exact variant (with-replacement, collapsed) ----------
def null_rep(rng):
    adj = [set() for _ in range(N)]
    for (a, b), es in epair.items():
        S, T = byL[a], byL[b]
        for _ in range(len(es)):
            adj[S[rng.integers(len(S))]].add(T[rng.integers(len(T))])
    return [list(s) for s in adj]

# ---------- null 2: distinct-edge-count matched ----------
def null_dist(rng):
    el = []
    for (a, b), es in epair.items():
        S, T = byL[a], byL[b]
        pick = rng.choice(len(S) * len(T), size=len(es), replace=False)
        el += [(S[p // len(T)], T[p % len(T)]) for p in pick]
    return to_adj(el)

# ---------- null 3: degree-preserving via CURVEBALL trades ----------
def null_cb(rng, rounds=60):
    el = []
    for (a, b), es in epair.items():
        S = byL[a]
        nb = {u: set() for u in S}
        for u, v in es: nb[u].add(v)
        ns = len(S)
        if ns >= 2:
            for _ in range(rounds * ns):
                i, j = rng.integers(0, ns, size=2)
                if i == j: continue
                u1, u2 = S[i], S[j]
                inter = nb[u1] & nb[u2]
                A = nb[u1] - inter; B = nb[u2] - inter
                if not A or not B: continue
                pool = list(A) + list(B)
                perm = rng.permutation(len(pool))
                new1 = set(pool[k] for k in perm[:len(A)])
                new2 = set(pool[k] for k in perm[len(A):])
                nb[u1] = inter | new1
                nb[u2] = inter | new2
        for u in S:
            for v in nb[u]: el.append((u, v))
    return to_adj(el)

def ens(fn, nseed, seed0, collectC=False):
    ds, Cs = [], collections.defaultdict(list)
    for s in range(nseed):
        adj = fn(np.random.default_rng(seed0 + s))
        r, d, C = stats(closure(adj))
        ds.append(d)
        if collectC:
            for k in [(a, b) for a in LV for b in LV if b > a]:
                Cs[k].append(C.get(k, 0))
    return np.array(ds), Cs

d1, _ = ens(null_rep, 60, 11000)
print(f"[null rep] d={d1.mean():.4f}+-{d1.std():.4f} z={(dO-d1.mean())/d1.std():.1f}  (claim 3.7837+-0.0148 z=10.3)")
d2, _ = ens(null_dist, 60, 12000)
print(f"[null dist] d={d2.mean():.4f}+-{d2.std():.4f} z={(dO-d2.mean())/d2.std():.1f}  (claim 3.7324+-0.0132 z=15.4)")
# two-sided control on my own ensemble
z0 = (d2[0] - d2[1:].mean()) / d2[1:].std()
print(f"[control] null-dist draw#0 vs rest: z={z0:+.2f} (must be |z|<2)")

d3, C3 = ens(null_cb, 100, 13000, collectC=True)
print(f"[null CB deg-preserving] d={d3.mean():.4f}+-{d3.std():.4f} z={(dO-d3.mean())/d3.std():.1f}  (claim 3.6351+-0.0055 z=55.1)")

# mixing check: fewer rounds
d3b, _ = ens(lambda g: null_cb(g, rounds=15), 30, 14000)
print(f"[mixing check rounds=15] d={d3b.mean():.4f}+-{d3b.std():.4f} (should match rounds=60 if mixed)")

# ---------- localization vs CB null ----------
print("\n[localization vs degree-preserving null]")
tot_def = 0.0; defs = {}
for k in sorted(C3):
    om = CO.get(k, 0); arr = np.array(C3[k])
    dfc = om - arr.mean(); tot_def += dfc
    z = (om - arr.mean()) / arr.std() if arr.std() > 0 else float("nan")
    defs[k] = dfc
    print(f"  L{k[0]}->L{k[1]}: Om={om} null={arr.mean():.1f}+-{arr.std():.1f} z={z:+.1f} deficit={dfc:+.1f}")
d710 = defs.get((7, 10), 0); d810 = defs.get((8, 10), 0)
print(f"  TOTAL deficit={tot_def:.1f}  (claim -3384.9);  (L7->L10 + L8->L10)/total = {(d710+d810)/tot_def:.3f} (claim 0.81)")

# adjacent pairs zero-variance check
adj_fixed = all(np.array(C3[(a, a + 1)]).std() == 0 for a in LV[:-1])
adj_match = all(CO[(a, a + 1)] == len(set(epair[(a, a + 1)])) for a in LV[:-1])
print(f"  adjacent C(a,a+1): zero-variance in null={adj_fixed}, equals distinct edge count in Omega={adj_match}")

# ---------- per-node reach-into-L10 fraction ----------
m10 = Lmask[10]; n10 = len(byL[10])
frO = {L: np.mean([bin(RO[u] & m10).count('1') for u in byL[L]]) / n10 for L in (7, 8)}
frN = {7: [], 8: []}
for s in range(10):
    Rb = closure(null_cb(np.random.default_rng(15000 + s)))
    for L in (7, 8):
        frN[L].append(np.mean([bin(Rb[u] & m10).count('1') for u in byL[L]]) / n10)
for L in (7, 8):
    print(f"[reach L{L}->L10 frac] Omega={frO[L]:.3f} null={np.mean(frN[L]):.3f}+-{np.std(frN[L]):.3f} "
          f"(claim: L7 0.576 vs 0.867+-0.011, L8 0.210 vs 0.303+-0.002)")
