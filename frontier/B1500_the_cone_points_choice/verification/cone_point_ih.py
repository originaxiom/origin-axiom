#!/usr/bin/env python3
"""B1500 -- THE CONE POINT'S CHOICE: intersection homology of the one-point compactification Q^ of a cusped hyperbolic
3-manifold, by allowable simplicial chains on the barycentric subdivision of SnapPy's ideal triangulation.  The ideal vertices
are the cusp points; each has the cusp torus T as its link, and H_1(T) != 0, so the points are not Witt.

What is computed, over F_p (p = 2^31 - 1):
- K' = the first barycentric subdivision of the ideal triangulation (a simplex is a chain of faces inside one tetrahedron,
  identified across the face gluings); K'' = the barycentric subdivision of K' (used on m004 and m003 as a cross-check).
- For a choice at every cusp point -- lower middle perversity (a simplex through the point is allowable only in degree 3), upper
  middle perversity (degree >= 2), or a Lagrangian line L in H_1(T) (degree >= 2, and a 2-chain through the point must meet the
  link in a cycle whose class lies in L: Cheeger's ideal boundary condition, Banagl's Lagrangian structure) -- the groups
  IH_i = ker(d on IC_i) / d(IC_{i+1}), IC_i = {allowable i-chains with allowable boundary}.
- Twisted by the rank-one local system t^omega of a cuspidal class omega (a class of H^1(Q^), i.e. of H^1(Q) vanishing on every
  cusp torus -- the frame's Higgs classes), with t random in F_p^*: the Higgs deformation d + s*omega at any coupling.
- The isolated-singularity formula it must match: lower -- IH_1 = H_1(Q), IH_2 = im(H_2(Q) -> H_2(Q^)); upper -- IH_1 =
  im(H_1(Q) -> H_1(Q^)), IH_2 = H_2(Q^); so chi = -k (lower), +k (upper).
Usage: python3 cone_point_ih.py [quick]   (writes cone_point_ih.json next to this file)"""
import itertools
import json
import random
import sys
import time
import warnings
from fractions import Fraction
from pathlib import Path

warnings.filterwarnings("ignore")
import snappy
import sympy

HERE = Path(__file__).resolve().parent
P = 2147483647                                                            # 2^31 - 1
SNAPPY_SEED = 1500


# ------------------------------------------------------------------------------------------------ sparse linear algebra over F_p
def rank_of_rows(rows):
    """rank over F_p of a list of sparse rows {column: value}; incremental echelon form keyed by leading column"""
    pivots = {}
    r = 0
    for row in rows:
        v = {c: x % P for c, x in row.items() if x % P}
        while v:
            lead = min(v)
            if lead in pivots:
                prow = pivots[lead]
                f = v[lead]                                                  # pivot rows are normalised to lead 1
                for c, x in prow.items():
                    y = (v.get(c, 0) - f * x) % P
                    if y:
                        v[c] = y
                    else:
                        v.pop(c, None)
            else:
                inv = pow(v[lead], P - 2, P)
                pivots[lead] = {c: (x * inv) % P for c, x in v.items()}
                r += 1
                break
    return r


def columns_to_rows(cols, keep_rows=None):
    """transpose a list of sparse columns {row: value} into sparse rows {col: value}, optionally keeping only some rows"""
    rows = {}
    for j, col in enumerate(cols):
        for i, x in col.items():
            if keep_rows is not None and i not in keep_rows:
                continue
            rows.setdefault(i, {})[j] = x
    return list(rows.values())


def rank_of_columns(cols, keep_rows=None, extra_rows=()):
    """rank of the matrix whose columns are the sparse dicts `cols` (rows restricted to keep_rows), with extra dense-ish rows appended"""
    rows = columns_to_rows(cols, keep_rows) + [dict(r) for r in extra_rows]
    return rank_of_rows(rows)


def nullspace_vectors(rows, ncols):
    """a basis of {x : row . x = 0 for every row} over F_p (rows sparse dicts), as sparse dicts"""
    pivots = {}                                                              # lead column -> fully reduced row
    for row in rows:
        v = {c: x % P for c, x in row.items() if x % P}
        for lead, prow in pivots.items():
            if lead in v:
                f = v[lead]
                for c, x in prow.items():
                    y = (v.get(c, 0) - f * x) % P
                    if y:
                        v[c] = y
                    else:
                        v.pop(c, None)
        if not v:
            continue
        lead = min(v)
        inv = pow(v[lead], P - 2, P)
        v = {c: (x * inv) % P for c, x in v.items()}
        for l2, prow in pivots.items():                                      # keep the echelon form fully reduced
            if lead in prow:
                f = prow[lead]
                for c, x in v.items():
                    y = (prow.get(c, 0) - f * x) % P
                    if y:
                        prow[c] = y
                    else:
                        prow.pop(c, None)
        pivots[lead] = v
    free = [c for c in range(ncols) if c not in pivots]
    basis = []
    for fcol in free:
        x = {fcol: 1}
        for lead, prow in pivots.items():
            if fcol in prow:
                x[lead] = (-prow[fcol]) % P
        basis.append(x)
    return basis


def dot(u, v):
    if len(u) > len(v):
        u, v = v, u
    return sum(x * v.get(c, 0) for c, x in u.items()) % P


# ------------------------------------------------------------------------------------------------ the triangulation and K'
def all_chains():
    """all strictly increasing chains of nonempty subsets of {0,1,2,3} (bitmasks)"""
    out = []

    def extend(chain):
        out.append(tuple(chain))
        for m in range(1, 16):
            if m != chain[-1] and (m & chain[-1]) == chain[-1]:
                extend(chain + [m])
    for m in range(1, 16):
        extend([m])
    return out


CHAINS = all_chains()
CHAIN_INDEX = {c: i for i, c in enumerate(CHAINS)}
NCH = len(CHAINS)
assert NCH == 15 + 50 + 60 + 24


def map_mask(m, perm):
    return sum(1 << perm[j] for j in range(4) if m >> j & 1)


class UF:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, a):
        while self.p[a] != a:
            self.p[a] = self.p[self.p[a]]
            a = self.p[a]
        return a

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            self.p[max(a, b)] = min(a, b)


class Complex:
    """a Delta-complex of dimension 3 with canonically ordered simplices: verts[d][s] (vertex ids), faces[d][s] (face i drops vertex i);
    singular: vertex id -> cusp label; edge_of[d][s] = the edge (vertex 0, vertex 1) of simplex s (for the twisted boundary)"""

    def __init__(self):
        self.verts = [[] for _ in range(4)]
        self.faces = [[] for _ in range(4)]
        self.singular = {}
        self.edge_of = [[] for _ in range(4)]
        self.omega = None                                                    # integer cocycle on edges, for twisting

    def n(self, d):
        return len(self.verts[d])


def build_first_subdivision(M):
    data = M._get_tetrahedra_gluing_data()
    n = len(data)
    uf = UF(n * NCH)
    for t, (nbrs, perms) in enumerate(data):
        for f in range(4):
            F = 15 ^ (1 << f)
            t2, perm = nbrs[f], perms[f]
            for ch in CHAINS:
                if (ch[-1] & F) == ch[-1]:
                    image = tuple(map_mask(m, perm) for m in ch)
                    uf.union(t * NCH + CHAIN_INDEX[ch], t2 * NCH + CHAIN_INDEX[image])
    cls = {}
    rep = {}
    for t in range(n):
        for ch in CHAINS:
            r = uf.find(t * NCH + CHAIN_INDEX[ch])
            if r not in rep:
                rep[r] = (t, ch)
    by_dim = [[] for _ in range(4)]
    for r, (t, ch) in sorted(rep.items()):
        by_dim[len(ch) - 1].append(r)
    ids = [{r: i for i, r in enumerate(by_dim[d])} for d in range(4)]
    K = Complex()

    def cid(t, ch):
        r = uf.find(t * NCH + CHAIN_INDEX[ch])
        return ids[len(ch) - 1][r]
    for d in range(4):
        for r in by_dim[d]:
            t, ch = rep[r]
            K.verts[d].append(tuple(cid(t, (m,)) for m in ch))
            K.faces[d].append(tuple(cid(t, ch[:i] + ch[i + 1:]) for i in range(len(ch))) if d > 0 else ())
            K.edge_of[d].append(cid(t, ch[:2]) if d >= 1 else None)
    # the cusp points: classes of single ideal vertices, labelled by union-find over (t, vertex)
    vuf = UF(4 * n)
    for t, (nbrs, perms) in enumerate(data):
        for f in range(4):
            for j in range(4):
                if j != f:
                    vuf.union(4 * t + j, 4 * nbrs[f] + perms[f][j])
    labels = {}
    for t in range(n):
        for v in range(4):
            c = vuf.find(4 * t + v)
            labels.setdefault(c, len(labels))
            K.singular[cid(t, (1 << v,))] = labels[c]
    K.k = len(labels)
    K.data = data
    K.ntet = n
    K._cid = cid
    return K


def subdivide(K):
    """the barycentric subdivision of a Delta-complex whose simplices have distinct, canonically ordered vertices"""
    memo = {}

    def subface(d, s, positions):
        """the face of simplex (d, s) spanned by the given sorted vertex positions"""
        key = (d, s, positions)
        if key in memo:
            return memo[key]
        full = tuple(range(d + 1))
        if positions == full:
            memo[key] = (d, s)
            return (d, s)
        drop = max(set(full) - set(positions))
        fs = K.faces[d][s][drop]
        newpos = tuple(p if p < drop else p - 1 for p in positions)
        out = subface(d - 1, fs, newpos)
        memo[key] = out
        return out
    # vertices of K'' = simplices of K
    vid = {}
    for d in range(4):
        for s in range(K.n(d)):
            vid[(d, s)] = len(vid)
    L = Complex()
    simp_id = [{} for _ in range(4)]
    items = [[] for _ in range(4)]
    for d in range(4):
        full = (1 << (d + 1)) - 1
        for s in range(K.n(d)):
            # flags of nonempty subsets of the d+1 positions ending at the full set
            chains = [(full,)]
            frontier = [(full,)]
            while frontier:
                new = []
                for ch in frontier:
                    for m in range(1, full + 1):
                        if m != ch[0] and (m & ch[0]) == m:
                            c2 = (m,) + ch
                            chains.append(c2)
                            new.append(c2)
                frontier = new
            for ch in chains:
                j = len(ch) - 1
                key = (d, s, ch)
                simp_id[j][key] = len(items[j])
                items[j].append(key)

    def positions(m):
        return tuple(i for i in range(4) if m >> i & 1)

    def key_of(d, s, ch):
        """canonical key of the K'' simplex given by chain ch (masks over the positions of K-simplex (d, s)) whose top may be smaller"""
        top = positions(ch[-1])
        d2, s2 = subface(d, s, top)
        remap = {p: i for i, p in enumerate(top)}
        ch2 = tuple(sum(1 << remap[p] for p in positions(m)) for m in ch)
        return (d2, s2, ch2)
    for j in range(4):
        for (d, s, ch) in items[j]:
            L.verts[j].append(tuple(vid[subface(d, s, positions(m))] for m in ch))
            if j > 0:
                L.faces[j].append(tuple(simp_id[j - 1][key_of(d, s, ch[:i] + ch[i + 1:])] for i in range(j + 1)))
            else:
                L.faces[j].append(())
            L.edge_of[j].append(simp_id[1][key_of(d, s, ch[:2])] if j >= 1 else None)
    for v, c in K.singular.items():
        L.singular[vid[(0, v)]] = c
    L.k = K.k
    return L


# ------------------------------------------------------------------------------------------------ cuspidal classes and the twist
def cuspidal_cocycles(K):
    """integer 1-cocycles on the ideal triangulation's edges representing a basis of H^1(Q^; Q) (the cuspidal classes)"""
    data, n, cid = K.data, K.ntet, K._cid
    edges = {}                                                               # K' vertex id of an edge barycentre -> column
    ends = {}

    def emask(a, b):
        return (1 << a) | (1 << b)
    for t in range(n):
        for a, b in itertools.combinations(range(4), 2):
            e = cid(t, (emask(a, b),))
            edges.setdefault(e, len(edges))
            ends.setdefault(e, set()).add(cid(t, (1 << a, emask(a, b))))
            ends[e].add(cid(t, (1 << b, emask(a, b))))
    assert all(len(v) == 2 for v in ends.values()) and len(edges) == n
    X = {e: min(v) for e, v in ends.items()}

    def sign(t, a, b):                                                       # tet orientation a -> b (a < b) against the edge's X -> Y
        e = cid(t, (emask(a, b),))
        return edges[e], (1 if cid(t, (1 << a, emask(a, b))) == X[e] else -1)
    rows = []
    for t in range(n):
        for tri in itertools.combinations(range(4), 3):
            a, b, c = tri
            row = [0] * n
            for (x, y), s in (((a, b), 1), ((b, c), 1), ((a, c), -1)):
                col, sg = sign(t, x, y)
                row[col] += s * sg
            rows.append(row)
    Z = sympy.Matrix(rows).nullspace()
    # coboundaries of functions on the cusp points
    cob = []
    endcusp = {}
    for e, col in edges.items():
        xe = X[e]
        ye = [h for h in ends[e] if h != xe][0]
        endcusp[col] = (K.singular[K.verts[1][xe][0]], K.singular[K.verts[1][ye][0]])
    for c in range(K.k):
        v = [0] * n
        for col, (cx, cy) in endcusp.items():
            v[col] += (1 if cy == c else 0) - (1 if cx == c else 0)
        cob.append(sympy.Matrix(v))
    base = sympy.Matrix.hstack(*cob) if cob else sympy.zeros(n, 0)
    r0 = base.rank()
    basis = []
    cur = base
    for z in Z:
        trial = sympy.Matrix.hstack(cur, z)
        if trial.rank() > cur.rank():
            cur = trial
            basis.append(z)
    out = []
    for z in basis:
        den = sympy.ilcm(*[sympy.fraction(x)[1] for x in z])
        out.append([int(x * den) for x in z])
    return out, edges, sign, r0


def twist_cocycle(K, K_cols, sign, omega_edges):
    """the cocycle omega on K' edges, 12 * (potential difference) inside each tetrahedron, checked consistent across representatives"""
    n, cid = K.ntet, K._cid
    val = {}
    for t in range(n):
        phi = [Fraction(0)] * 4
        for j in range(1, 4):
            col, sg = sign(t, 0, j)
            phi[j] = Fraction(sg * omega_edges[col])
        for a, b in itertools.combinations(range(4), 2):
            col, sg = sign(t, a, b)
            assert phi[b] - phi[a] == sg * omega_edges[col], "not a cocycle inside a tetrahedron"

        def pot(m):
            bits = [j for j in range(4) if m >> j & 1]
            return sum(phi[j] for j in bits) / len(bits)
        for ch in CHAINS:
            if len(ch) == 2:
                e = cid(t, ch)
                w = 12 * (pot(ch[1]) - pot(ch[0]))
                assert w.denominator == 1
                if e in val:
                    assert val[e] == int(w), "twist cocycle inconsistent across representatives"
                val[e] = int(w)
    return [val[e] for e in range(K.n(1))]


# ------------------------------------------------------------------------------------------------ the chain complex and IH
def boundary_columns(K, d, tw=None):
    """sparse columns of the boundary C_d -> C_{d-1}; tw = (t, omega) twists face 0 by t^omega(v0 v1)"""
    cols = []
    for s in range(K.n(d)):
        col = {}
        for i, f in enumerate(K.faces[d][s]):
            x = 1 if i % 2 == 0 else P - 1
            if i == 0 and tw is not None:
                t, om = tw
                x = pow(t, om[K.edge_of[d][s]] % (P - 1), P)
            col[f] = (col.get(f, 0) + x) % P
        cols.append({k: v for k, v in col.items() if v})
    return cols


def through(K, d, s):
    """the cusp whose point is vertex 0 of simplex (d, s), or None"""
    return K.singular.get(K.verts[d][s][0])


def link_lagrangian_functional(K, c, rng):
    """a 1-cocycle phi on the link of cusp point c (indexed by the 2-simplices through c) whose kernel on H_1(link) is a random line L"""
    idx = [{} for _ in range(4)]
    for d in (1, 2, 3):
        for s in range(K.n(d)):
            if through(K, d, s) == c:
                idx[d][s] = len(idx[d])
    # link boundary: link simplex of (d, s) has faces = faces i >= 1 of (d, s), with sign (-1)^(i-1)
    def lcols(d):
        cols = []
        for s in idx[d]:
            col = {}
            for i, f in enumerate(K.faces[d][s]):
                if i == 0:
                    continue
                col[idx[d - 1][f]] = (col.get(idx[d - 1][f], 0) + (1 if (i - 1) % 2 == 0 else P - 1)) % P
            cols.append(col)
        return cols
    b2 = lcols(2)                                                            # link C_1 -> C_0
    b3 = lcols(3)                                                            # link C_2 -> C_1
    n0, n1, n2 = len(idx[1]), len(idx[2]), len(idx[3])
    # link homology H_1: cycles modulo boundaries
    Z1 = nullspace_vectors(columns_to_rows(b2), n1)
    B1_rows = [dict(col) for col in b3]                                      # the boundaries, as vectors in C_1
    rB = rank_of_rows([dict(r) for r in B1_rows])
    h = [z for z in Z1]
    # choose two cycles independent modulo boundaries
    reps = []
    cur = list(B1_rows)
    r = rB
    for z in h:
        r2 = rank_of_rows([dict(x) for x in cur] + [dict(z)])
        if r2 > r:
            cur.append(z)
            r = r2
            reps.append(z)
        if len(reps) == 2:
            break
    b0 = n0 - rank_of_columns(b2)
    assert len(reps) == 2, "the link does not have H_1 of rank 2"
    a, b = rng.randrange(1, P), rng.randrange(1, P)
    zL = {k: (a * reps[0].get(k, 0) + b * reps[1].get(k, 0)) % P for k in set(reps[0]) | set(reps[1])}
    zO = reps[1] if b % P else reps[0]
    # cocycles: phi with phi . boundary = 0 for every link 2-simplex boundary
    cocycles = nullspace_vectors([dict(col) for col in b3], n1)
    # find phi in span(cocycles) with phi(zL) = 0 and phi(zO) != 0
    vals = [(dot(ph, zL), dot(ph, zO)) for ph in cocycles]
    phi = None
    for i, (x1, y1) in enumerate(vals):
        for j, (x2, y2) in enumerate(vals):
            if j <= i:
                continue
            # combination u*ph_i + v*ph_j with u*x1 + v*x2 = 0
            u, v = x2 % P, (-x1) % P
            if (u or v) and (u * y1 + v * y2) % P:
                phi = {k: (u * cocycles[i].get(k, 0) + v * cocycles[j].get(k, 0)) % P for k in set(cocycles[i]) | set(cocycles[j])}
                break
        if phi is not None:
            break
    if phi is None:
        for i, (x1, y1) in enumerate(vals):
            if x1 == 0 and y1:
                phi = cocycles[i]
                break
    assert phi is not None
    inv = {j: s for s, j in idx[2].items()}
    return {inv[j]: x for j, x in phi.items() if x}, dict(link_h0=b0, link_simplices=(n0, n1, n2))


def ih(K, choice, tw=None, lag=None):
    """IH_0..IH_3 for choice: cusp -> 'lower' | 'upper' | 'lag'; lag: cusp -> functional on 2-simplices through that cusp"""
    p_of = {"lower": 0, "upper": 1, "lag": 1}
    allow = []
    for d in range(4):
        a = []
        for s in range(K.n(d)):
            c = through(K, d, s)
            a.append(c is None or d >= 3 - p_of[choice[c]])
        allow.append(a)
    cols = [None] + [boundary_columns(K, d, tw) for d in (1, 2, 3)]
    m = [sum(allow[d]) for d in range(4)]
    acol = [None]
    for d in (1, 2, 3):
        acol.append([cols[d][s] for s in range(K.n(d)) if allow[d][s]])
    amap = [{s: i for i, s in enumerate([s for s in range(K.n(d)) if allow[d][s]])} for d in range(4)]
    phi_rows = {1: [], 2: [], 3: []}
    if lag:
        for c, phi in lag.items():
            if choice[c] == "lag":
                phi_rows[2].append({amap[2][s]: x for s, x in phi.items() if s in amap[2]})
    nonallowed = [None] + [set(s for s in range(K.n(d - 1)) if not allow[d - 1][s]) for d in (1, 2, 3)]
    rk_full = [0, 0, 0, 0, 0]
    rk_cons = [0, 0, 0, 0, 0]
    for d in (1, 2, 3):
        rk_full[d] = rank_of_columns(acol[d], None, phi_rows[d])
        rk_cons[d] = rank_of_columns(acol[d], nonallowed[d], phi_rows[d])
    out = []
    for d in range(4):
        dimIC = m[d] - rk_cons[d]
        rank_d = rk_full[d] - rk_cons[d]
        rank_next = (rk_full[d + 1] - rk_cons[d + 1]) if d < 3 else 0
        out.append(dimIC - rank_d - rank_next)
    return out


def plain_homology(K, tw=None):
    cols = [None] + [boundary_columns(K, d, tw) for d in (1, 2, 3)]
    r = [0] + [rank_of_columns(cols[d]) for d in (1, 2, 3)] + [0]
    return [K.n(d) - r[d] - r[d + 1] for d in range(4)]


def check_dd(K, tw=None):
    for d in (2, 3):
        hi, lo = boundary_columns(K, d, tw), boundary_columns(K, d - 1, tw)
        for col in hi:
            acc = {}
            for f, x in col.items():
                for g, y in lo[f].items():
                    acc[g] = (acc.get(g, 0) + x * y) % P
            assert not any(acc.values()), "d^2 != 0"
    return True


# ------------------------------------------------------------------------------------------------ one manifold
def manifold(sig):
    snappy.set_rand_seed(SNAPPY_SEED)
    if sig == "cube~3.24":                                                  # B1386's member, built as B1387 builds it
        import importlib.util
        spec = importlib.util.spec_from_file_location("b1387_harmonic_cusp_form", HERE.parents[1] / "B1387_the_index_computed" /
                                                      "verification" / "harmonic_cusp_form.py")
        HF = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(HF)
        return HF.member()
    return snappy.Manifold(sig)


def formula(M, K):
    """the isolated-singularity formula from SnapPy's homology: b1 of the core, k; lower IH = (1, b1, b1 - k, 1), upper = (1, u1, b1, 1)"""
    b1 = M.homology().betti_number()
    k = M.num_cusps()
    return b1, k


def run_manifold(sig, label, second=False, twists=2, patterns=None, rng=None, lag_lines=2):
    t0 = time.time()
    rng = rng or random.Random(1500)
    M = manifold(sig)
    K = build_first_subdivision(M)
    assert K.k == M.num_cusps()
    b1, k = formula(M, K)
    rep = dict(label=label, tets=M.num_tetrahedra(), cusps=k, b1=b1, simplices=[K.n(d) for d in range(4)])
    check_dd(K)
    H = plain_homology(K)
    rep["H(Q^)"] = H
    assert H[0] == 1 and H[3] == 1 and sum((-1) ** d * H[d] for d in range(4)) == k
    # cuspidal classes
    cocs, ecols, sign, rcob = cuspidal_cocycles(K)
    rep["cuspidal dimension (H^1(Q^))"] = len(cocs)
    assert len(cocs) == H[1], (len(cocs), H[1])
    cusps = list(range(k))
    res = {}
    lower = ih(K, {c: "lower" for c in cusps})
    upper = ih(K, {c: "upper" for c in cusps})
    res["lower"] = lower
    res["upper"] = upper
    # the formula: lower (1, b1, b1 - k, 1), upper (1, rank im(H1(Q) -> H1(Q^)), b1, 1)
    assert lower == [1, b1, b1 - k, 1], (lower, b1, k)
    assert upper == [1, b1 - k, b1, 1], (upper, b1, k)
    # mixed choices
    pats = patterns if patterns is not None else list(itertools.product(("lower", "upper"), repeat=k)) if k <= 3 else \
        [tuple("lower" if (i + j) % 2 else "upper" for i in range(k)) for j in range(2)] + [tuple(["lower"] + ["upper"] * (k - 1))]
    mixed = []
    for pat in pats:
        g = ih(K, dict(zip(cusps, pat)))
        chi = g[0] - g[1] + g[2] - g[3]
        want = sum(-1 if x == "lower" else 1 for x in pat)
        mixed.append(dict(pattern=list(pat), IH=g, chi=chi, predicted=want))
        assert chi == want, (pat, g)
    res["mixed"] = mixed
    # Lagrangian lines at every cusp point, and Lagrangian at one point with lower/upper elsewhere
    lagrep = []
    for trial in range(lag_lines):
        lag = {}
        for c in cusps:
            phi, info = link_lagrangian_functional(K, c, rng)
            lag[c] = phi
        g = ih(K, {c: "lag" for c in cusps}, lag=lag)
        chi = g[0] - g[1] + g[2] - g[3]
        lagrep.append(dict(choice="Lagrangian at every point", IH=g, chi=chi, predicted=0))
        assert chi == 0, g
        if k >= 2:
            ch = {c: ("lag" if c == 0 else ("lower" if c % 2 else "upper")) for c in cusps}
            g = ih(K, ch, lag=lag)
            chi = g[0] - g[1] + g[2] - g[3]
            want = sum(0 if v == "lag" else (-1 if v == "lower" else 1) for v in ch.values())
            lagrep.append(dict(choice=[ch[c] for c in cusps], IH=g, chi=chi, predicted=want))
            assert chi == want, (ch, g)
    res["lagrangian"] = lagrep
    # twisted by cuspidal classes
    tw_rep = []
    for trial in range(twists if cocs else 0):
        coef = [rng.randrange(-3, 4) for _ in cocs]
        if not any(coef):
            coef[0] = 1
        omega_edges = [sum(a * z[i] for a, z in zip(coef, cocs)) for i in range(K.ntet)]
        om = twist_cocycle(K, None, sign, omega_edges)
        t = rng.randrange(2, P - 1)
        check_dd(K, (t, om))
        Ht = plain_homology(K, (t, om))
        gl = ih(K, {c: "lower" for c in cusps}, tw=(t, om))
        gu = ih(K, {c: "upper" for c in cusps}, tw=(t, om))
        row = dict(coefficients=coef, H_twisted=Ht, IH_lower=gl, IH_upper=gu,
                   chi=(sum((-1) ** d * Ht[d] for d in range(4)), sum((-1) ** d * gl[d] for d in range(4)), sum((-1) ** d * gu[d] for d in range(4))))
        assert row["chi"] == (k, -k, k), row
        if k >= 2:
            pat = {c: ("lower" if c % 2 == 0 else "upper") for c in cusps}
            gm = ih(K, pat, tw=(t, om))
            row["IH_mixed"] = gm
            want = sum(-1 if v == "lower" else 1 for v in pat.values())
            assert sum((-1) ** d * gm[d] for d in range(4)) == want
        tw_rep.append(row)
    res["twisted"] = tw_rep
    if second:
        L = subdivide(K)
        check_dd(L)
        HL = plain_homology(L)
        lowL = ih(L, {c: "lower" for c in cusps})
        upL = ih(L, {c: "upper" for c in cusps})
        res["second subdivision"] = dict(simplices=[L.n(d) for d in range(4)], H=HL, lower=lowL, upper=upL,
                                          agrees=(HL == H and lowL == lower and upL == upper))
        assert HL == H and lowL == lower and upL == upper
    rep["results"] = res
    rep["seconds"] = round(time.time() - t0, 1)
    return rep


def members(quick=False):
    out = [("m004", "m004", True), ("m003", "m003", True)]
    census = json.load(open(HERE.parents[1] / "B1399_the_rank_two_higgs" / "verification" / "census.json"))["members"]
    picks = []
    seen = set()
    for want in [(2, 1), (2, 2), (2, 3), (3, 1), (2, 5), (3, 3)]:
        for m in census:
            if m["status"] == "resolved" and (m["dim"], m["cusps"]) == want and m["label"] not in seen:
                picks.append((m["label"], "%s cover (dim %d, %d cusps)" % (m["parent"], m["dim"], m["cusps"]), False))
                seen.add(m["label"])
                break
    for m in census:
        if m["status"] != "resolved" and m["cusps"] == 4:
            picks.append((m["label"], "%s cover (hexagonal, 4 cusps, unresolved in B1399)" % m["parent"], False))
            break
    out += picks if not quick else picks[:2]
    if not quick:
        out.append(("cube~3.24", "cube~3.24 (B1386's member; its cuspidal line is B1387's v+)", False))
    return out


def main(quick=False):
    rng = random.Random(1500)
    reps = []
    for sig, label, second in members(quick):
        r = run_manifold(sig, label, second=second, rng=rng)
        reps.append(r)
        res = r["results"]
        print("%-58s tets %3d  k %d  b1 %d  H(Q^) %s  cuspidal %d | lower %s  upper %s | mixed %d/%d | Lagrangian %d/%d | twisted %d%s  (%ss)"
              % (label[:58], r["tets"], r["cusps"], r["b1"], r["H(Q^)"], r["cuspidal dimension (H^1(Q^))"], res["lower"], res["upper"],
                 sum(x["chi"] == x["predicted"] for x in res["mixed"]), len(res["mixed"]),
                 sum(x["chi"] == x["predicted"] for x in res["lagrangian"]), len(res["lagrangian"]), len(res["twisted"]),
                 " | K'' agrees" if res.get("second subdivision", {}).get("agrees") else "", r["seconds"]), flush=True)
    json.dump(reps, open(HERE / "cone_point_ih.json", "w"), indent=1)
    return reps


if __name__ == "__main__":
    main(quick="quick" in sys.argv)
    print("ALL CHECKS PASS")
