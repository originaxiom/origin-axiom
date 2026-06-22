"""B189 -- Omega causal-set dimension (V184), FIREWALLED. Fast locks.

The Myrheim-Meyer ordering-fraction estimator (calibrated on Minkowski sprinklings) gives the Omega class poset
d_MM ~ 4 -- but this is a generic graded-DAG / truncation artifact: it DRIFTS upward with the number of layers
(no convergence) and is matched by a random graded-DAG null control (matched sizes + edge counts). So d~4 is
combinatorial, NOT a spacetime dimension; the firewall holds by computation. Full version in omega_causal_dimension.py.
"""
import numpy as np, csv, math, os, sys

BASE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B159_omega_class_dag")


def _mm(d): return math.gamma(d+1)*math.gamma(d/2)/(4*math.gamma(3*d/2))
def _d_from_r(r, lo=1.5, hi=8.0):
    if r >= _mm(lo): return lo
    if r <= _mm(hi): return hi
    for _ in range(50):
        m = (lo+hi)/2; lo, hi = (m, hi) if _mm(m) > r else (lo, m)
    return (lo+hi)/2


def _load():
    nodes = []; idx = {}; level = {}
    with open(os.path.join(BASE, "omega_strict_full_class_nodes_L4_L10.csv")) as fh:
        for row in csv.DictReader(fh):
            idx[row["id"]] = len(nodes); level[len(nodes)] = int(row["level"]); nodes.append(row["id"])
    N = len(nodes); succ = [set() for _ in range(N)]
    with open(os.path.join(BASE, "omega_strict_full_class_edges_L4_L10.csv")) as fh:
        for row in csv.DictReader(fh):
            if row["source"] in idx and row["target"] in idx: succ[idx[row["source"]]].add(idx[row["target"]])
    return N, succ, level


def _ordering_fraction(N, succ, level, keepmax):
    sys.setrecursionlimit(20000)
    keep = [u for u in range(N) if level[u] <= keepmax]; ks = set(keep); reach = {}
    def R(u):
        if u in reach: return reach[u]
        s = set()
        for v in succ[u]:
            if v in ks: s.add(v); s |= R(v)
        reach[u] = s; return s
    rel = sum(len(R(u)) for u in keep); n = len(keep)
    return rel/(n*(n-1))


def test_calibration_matches_meyer():
    rng = np.random.default_rng(0)
    for d in (2, 4):
        N = 150; pts = []
        while len(pts) < N:
            t = rng.random(); x = (rng.random(d-1)-0.5)*2; rx = float(np.linalg.norm(x))
            if rx < t and rx < 1.0 - t: pts.append((t, x))
        rel = sum(1 for i in range(N) for j in range(N)
                  if i != j and pts[j][0] > pts[i][0] and (pts[j][0]-pts[i][0])**2 > np.sum((pts[j][1]-pts[i][1])**2))
        assert abs(rel/(N*(N-1)) - _mm(d)) < 0.04          # estimator correct on ground truth


def test_omega_dimension_drifts_and_same_order_as_null():
    N, succ, level = _load()
    d6 = _d_from_r(_ordering_fraction(N, succ, level, 6))
    d10 = _d_from_r(_ordering_fraction(N, succ, level, 10))
    assert d6 < d10                                         # drifts up with truncation -> not a stable dimension
    assert 3.5 < d10 < 4.3                                  # ~4 (the over-readable number)
    # null control: random graded DAG, matched level sizes + consecutive-level edge counts
    sizes = {}; edgecount = {}
    for u in range(N): sizes[level[u]] = sizes.get(level[u], 0) + 1
    for u in range(N):
        for v in succ[u]:
            if level[v] == level[u]+1: edgecount[(level[u], level[v])] = edgecount.get((level[u], level[v]), 0)+1
    levels = sorted(sizes); g = np.random.default_rng(2)
    nb = [(L, i) for L in levels for i in range(sizes[L])]; ix = {nd: k for k, nd in enumerate(nb)}; Nn = len(nb)
    out = [set() for _ in range(Nn)]
    for (La, Lb), m in edgecount.items():
        srcs = [ix[(La, i)] for i in range(sizes[La])]; tgts = [ix[(Lb, j)] for j in range(sizes[Lb])]
        for _ in range(m): out[g.choice(srcs)].add(int(g.choice(tgts)))
    reach = {}
    def R(u):
        if u in reach: return reach[u]
        s = set()
        for v in out[u]: s.add(v); s |= R(v)
        reach[u] = s; return s
    rel = sum(len(R(u)) for u in range(Nn)); d_ctrl = _d_from_r(rel/(Nn*(Nn-1)))
    assert 3.4 < d_ctrl < 4.2                               # null is the SAME ORDER (~4): both graded-DAG artifacts
    assert d10 >= d_ctrl                                    # Omega sits AT/ABOVE the null (sparser/more tree-like)
