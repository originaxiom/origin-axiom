#!/usr/bin/env python3
"""GC-4: the reach-deficit law (L190) with richer nulls.

(1) reproduce the L10 z with an own null (level sizes + consecutive-level distinct-edge
    counts matched, 100 seeds);
(2) richer null: degree-preserving rewiring (exact in/out degrees per node, simple graph,
    swap-MCMC within each adjacent level pair; 100 seeds) -- does the deficit survive?
(3) localize: per-level-pair comparable-pair counts C(a,b) Omega vs both nulls;
(4) law candidate: pair-overlap (Jaccard) distribution of descendant sets of same-level
    nodes vs nulls + sibling child-overlap.

Conventions: d_from_r / mm_fraction from B189 (omega_causal_dimension.py lines 43-51);
r = sum_u |R(u)| / (N(N-1)) on the transitive closure (directed-pair convention).
"""
import csv, math, os, collections
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

# ---- load ----
ids, level = [], []
idx = {}
with open(BASE+"omega_strict_full_class_nodes_L4_L10.csv") as fh:
    for row in csv.DictReader(fh):
        idx[row["id"]] = len(ids); ids.append(row["id"]); level.append(int(row["level"]))
N = len(ids)
level = np.array(level)
edges = []
with open(BASE+"omega_strict_full_class_edges_L4_L10.csv") as fh:
    for row in csv.DictReader(fh):
        edges.append((idx[row["source"]], idx[row["target"]]))
LEVELS = sorted(set(level.tolist()))
by_level = {L: np.where(level == L)[0].tolist() for L in LEVELS}
sizes = {L: len(by_level[L]) for L in LEVELS}
# edges grouped by level pair
epair = collections.defaultdict(list)
for u, v in edges:
    epair[(level[u], level[u]+1)].append((u, v))

def reach_bitsets(adj, N, order_desc):
    """adj: list of lists; order_desc: nodes in descending level order. Returns list of ints (bitsets)."""
    R = [0]*N
    for u in order_desc:
        s = 0
        for v in adj[u]:
            s |= (1 << v) | R[v]
        R[u] = s
    return R

ORDER_DESC = sorted(range(N), key=lambda u: -level[u])

def analyze(adj, Lmax=10):
    """Return (r, d_MM, C) where C[(a,b)] = # comparable ordered pairs u in L_a, v in L_b."""
    R = reach_bitsets(adj, N, ORDER_DESC)
    keep = [u for u in range(N) if level[u] <= Lmax]
    if Lmax < 10:
        mask = 0
        for u in keep: mask |= (1 << u)
        tot = sum(bin(R[u] & mask).count("1") for u in keep)
        n = len(keep)
        return tot/(n*(n-1)), d_from_r(tot/(n*(n-1))), None, R
    C = collections.Counter()
    lvl_mask = {L: sum(1 << u for u in by_level[L]) for L in LEVELS}
    tot = 0
    for u in range(N):
        a = level[u]
        for b in LEVELS:
            if b <= a: continue
            c = bin(R[u] & lvl_mask[b]).count("1")
            if c: C[(a, b)] += c; tot += c
    return tot/(N*(N-1)), d_from_r(tot/(N*(N-1))), C, R

def adj_from_edges(elist):
    adj = [[] for _ in range(N)]
    for u, v in elist: adj[u].append(v)
    return adj

# ---- null A: level sizes + consecutive-level distinct-edge counts matched ----
def null_A(rng):
    elist = []
    for (La, Lb), es in epair.items():
        m = len(es)
        src, tgt = by_level[La], by_level[Lb]
        npairs = len(src)*len(tgt)
        pick = rng.choice(npairs, size=m, replace=False)
        for p in pick:
            elist.append((src[p // len(tgt)], tgt[p % len(tgt)]))
    return adj_from_edges(elist)

# ---- null B: degree-preserving swap-MCMC within each level pair (exact degrees, simple) ----
def null_B(rng, sweeps=20):
    elist = []
    for (La, Lb), es in epair.items():
        cur = list(es)
        eset = set(cur)
        m = len(cur)
        if m >= 2:
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
    return adj_from_edges(elist)

adj_omega = adj_from_edges(edges)
r_om, d_om, C_om, R_om = analyze(adj_omega)
print(f"Omega: r={r_om:.5f} d_MM={d_om:.3f}")

NSEED = 100
resA, resB = [], []
CA = collections.defaultdict(list); CB = collections.defaultdict(list)
truncA = collections.defaultdict(list)  # Lmax -> list of d
adjsA, adjsB = [], []
for s in range(NSEED):
    rngA = np.random.default_rng(1000+s); rngB = np.random.default_rng(2000+s)
    aA = null_A(rngA); aB = null_B(rngB)
    rA, dA, cA, _ = analyze(aA); rB, dB, cB, _ = analyze(aB)
    resA.append(dA); resB.append(dB)
    for k in cA: CA[k].append(cA[k])
    for k in cB: CB[k].append(cB[k])
    for Lmax in (6, 7, 8, 9):
        truncA[Lmax].append(analyze(aA, Lmax)[1])
    if s < 10: adjsA.append(aA); adjsB.append(aB)

resA = np.array(resA); resB = np.array(resB)
zA = (d_om - resA.mean())/resA.std()
zB = (d_om - resB.mean())/resB.std()
print(f"\n(1) null A (edge-count-matched, {NSEED} seeds): d_MM = {resA.mean():.4f} +- {resA.std():.4f}  -> z(Omega) = {zA:.1f}")
print(f"(2) null B (degree-preserving, {NSEED} seeds):  d_MM = {resB.mean():.4f} +- {resB.std():.4f}  -> z(Omega) = {zB:.1f}")

# two-sided control: a null-A draw scored against the remaining null-A ensemble must NOT fire
d0 = resA[0]; rest = resA[1:]
z0 = (d0 - rest.mean())/rest.std()
print(f"    control (deliberately-absent target): null-A draw #0 vs null-A ensemble z = {z0:+.2f} (|z|<2 required)")

# per-truncation-level z trend vs null A (reproduce the -2.2,-2.8,-2.3,+0.6,+11.2 structure)
print("\nper-truncation z-trend vs null A:")
ztrend = []
for Lmax in (6, 7, 8, 9):
    dOm = analyze(adj_omega, Lmax)[1]
    arr = np.array(truncA[Lmax])
    z = (dOm - arr.mean())/arr.std()
    ztrend.append(z)
    print(f"  L<= {Lmax}: Omega d={dOm:.3f} null {arr.mean():.3f}+-{arr.std():.3f} z={z:+.1f}")
ztrend.append(zA)
print(f"  L<=10: z={zA:+.1f}")
print("  trend:", ", ".join(f"{z:+.1f}" for z in ztrend))

# ---- (3) localization: per-level-pair comparable-pair counts ----
print("\n(3) localization: comparable pairs C(a,b) Omega vs nulls (z = (Omega-null)/sd; negative = deficit)")
print(f"{'pair':>9} {'Omega':>7} {'nullA mean+-sd':>18} {'zA':>7} {'nullB mean+-sd':>18} {'zB':>7} {'fracOm':>7}")
pairs = [(a, b) for a in LEVELS for b in LEVELS if b > a]
deficits = []
for (a, b) in pairs:
    om = C_om.get((a, b), 0)
    A = np.array(CA[(a, b)]); B = np.array(CB[(a, b)])
    za = (om - A.mean())/A.std() if A.std() > 0 else float('nan')
    zb = (om - B.mean())/B.std() if B.std() > 0 else float('nan')
    frac = om/(sizes[a]*sizes[b])
    deficits.append(((a, b), om, A.mean(), za, B.mean(), zb, om - B.mean()))
    print(f"  L{a}->L{b} {om:7d} {A.mean():10.1f}+-{A.std():6.1f} {za:+7.1f} {B.mean():10.1f}+-{B.std():6.1f} {zb:+7.1f} {frac:7.3f}")
totdefB = sum(d[6] for d in deficits)
print(f"  total comparable-pair deficit vs null B: {totdefB:+.1f} (Omega {sum(C_om.values())} vs nullB {sum(C_om.values())-totdefB:.1f})")

# ---- (4) law candidate: same-level descendant-set pair overlap ----
def overlap_stats(adjR, R=None):
    """mean Jaccard of descendant sets over same-level pairs, per level; and mean |R| per level."""
    if R is None: R = reach_bitsets(adjR, N, ORDER_DESC)
    J = {}; meanR = {}
    for L in LEVELS:
        nodes_L = by_level[L]
        meanR[L] = np.mean([bin(R[u]).count("1") for u in nodes_L]) if nodes_L else 0
        js = []
        for i in range(len(nodes_L)):
            for j in range(i+1, len(nodes_L)):
                a, b = R[nodes_L[i]], R[nodes_L[j]]
                un = bin(a | b).count("1")
                if un: js.append(bin(a & b).count("1")/un)
        J[L] = float(np.mean(js)) if js else float('nan')
    return J, meanR

J_om, mR_om = overlap_stats(None, R_om)
JA = collections.defaultdict(list); JB = collections.defaultdict(list)
mRA = collections.defaultdict(list); mRB = collections.defaultdict(list)
for aA, aB in zip(adjsA, adjsB):
    j, m = overlap_stats(aA)
    for L in LEVELS: JA[L].append(j[L]); mRA[L].append(m[L])
    j, m = overlap_stats(aB)
    for L in LEVELS: JB[L].append(j[L]); mRB[L].append(m[L])
print("\n(4) same-level descendant-set Jaccard overlap (10 null seeds) + mean reach |R|:")
print(f"{'L':>3} {'J_Omega':>8} {'J_nullA':>8} {'J_nullB':>8} {'|R|_Om':>8} {'|R|_A':>8} {'|R|_B':>8}")
for L in LEVELS[:-1]:
    print(f"{L:3d} {J_om[L]:8.3f} {np.mean(JA[L]):8.3f} {np.mean(JB[L]):8.3f} {mR_om[L]:8.1f} {np.mean(mRA[L]):8.1f} {np.mean(mRB[L]):8.1f}")

# sharpest law: reach-into-L10 fraction per source level, Omega vs null B
print("\nreach-into-L10 fraction per source level (Omega vs nullB):")
m10 = sum(1 << u for u in by_level[10])
for L in LEVELS[:-1]:
    fr_om = np.mean([bin(R_om[u] & m10).count("1") for u in by_level[L]])/sizes[10]
    frB = []
    for aB in adjsB:
        Rb = reach_bitsets(aB, N, ORDER_DESC)
        frB.append(np.mean([bin(Rb[u] & m10).count("1") for u in by_level[L]])/sizes[10])
    print(f"  L{L}: Omega {fr_om:.3f}  nullB {np.mean(frB):.3f}+-{np.std(frB):.3f}")
