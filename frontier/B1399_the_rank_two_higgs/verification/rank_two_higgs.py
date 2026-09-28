#!/usr/bin/env python3
"""B1399 -- THE RANK-TWO HIGGS, run as sealed (PREREGISTRATION.md; sha256 in docs/SEAL_LEDGER.md).

The question: is there a census member M and cuspidal classes w1, w2 on it with C(a_k w1 + b_k w2) = t_k on B1398's six direction
classes, stably, at g = 3?  C(v) = -sum_c chi(d+_c(v)) read from v's leading Fourier shell at each cusp (B1387's chi_plus).

The instrument, as sealed:
- the harmonic forms: B1387's Hejhal solve, generalised to a basis of the cuspidal space V with one right-hand side per basis class
  (the rows depend only on the geometry; the class enters linearly through the walk's accumulation and the charts' gamma values, so the
  class is carried as a vector);  ladder (K_n, tau) = (10, 0.10), (14, 0.10), (14, 0.08); chart seed 1; sample seeds 1 and 2;
  acceptance: full rank, every basis class 0 on every parabolic, fit rms < 1e-3, test rms at 0.06 and 0.09 < 1e-2, tau below the lowest
  pulled-back normalised height, and the two seeds agreeing;
- the solved basis: the rational null space (sympy) of the relators and peripheral words of the unsimplified presentation, each vector
  scaled to largest entry +1 (B1387's normalisation);
- the leading shells, decided on V: a shell is killed when its coefficient map V -> C^m has norm below 1e-2 of the largest among the
  cusp's first six shells; a ratio in [1e-3, 1e-1) at a shell up to and including the leading one makes the member unresolved;
- C on a circle: per cusp with a leading shell of >= 3 directions, the breakpoints psi(x) +- pi/2 at the critical points of the angle
  map (damped Newton on g1 grad g2 - g2 grad g1 from 64, 128, 256 seeds per side, complete when the indices sum to zero), merged below
  1e-6; chi_c by B1387's Morse count at the midpoint of each of the cusp's arcs; every change of chi_c between neighbouring arcs must
  equal the predicted jump; a leading shell of 1 or 2 directions gives chi_c = 0; a leading shell whose map on the circle has real rank
  one (sigma2/sigma1 < 1e-3; [1e-3, 1e-1) unresolved) flips at the two directions where the map vanishes;
- the cross-check: 720 equally spaced directions (V's circle in dimension 2; the three coordinate planes in dimension 3), every
  direction farther than 1e-3 from a breakpoint showing its arc's value, by a full Morse count;
- realisability: L in GL(2, R) with L p_k in an open arc of value t_k -- one exact linear program per assignment (arcs < pi; longer arcs
  covered by overlapping shorter ones; margin 1), searched depth-first with feasibility pruning; a positive re-verified with the L that
  maximises the smallest margin (|L_ij| <= 1), C evaluated directly at the six image directions from both seeds' forms, each image
  farther than 1e-3 from every breakpoint;
- dimension 3: the three coordinate planes of the solved basis and 200 planes with normals default_rng(1399).normal(size=(200, 3)).
Usage: python3 rank_two_higgs.py identity | census [workers] | member <isometry signature>"""
import importlib.util
import json
import math
import random
import sys
import time
import warnings
from bisect import bisect_right
from collections import deque
from pathlib import Path

warnings.filterwarnings("ignore")
import numpy as np
import sympy
from scipy.optimize import linprog
import snappy

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


HF = _load("b1387_harmonic_cusp_form", ROOT / "frontier" / "B1387_the_index_computed" / "verification" / "harmonic_cusp_form.py")
BC = _load("b1399_breakpoint_check", HERE / "breakpoint_check.py")

CLASSES = [(1, -4), (1, 0), (1, 1), (1, 6), (3, -2), (3, 8)]
PATTERN = [1, 0, -1, 0, 1, -2]
LADDER = [(10.0, 0.10), (14.0, 0.10), (14.0, 0.08)]
CHART_SEED, SAMPLE_SEEDS, TEST_TAUS = 1, (1, 2), (0.06, 0.09)
FIT_MAX, TEST_MAX, PARABOLIC_MAX = 1e-3, 1e-2, 1e-8
KILL, AMB_LO, AMB_HI = 1e-2, 1e-3, 1e-1
MERGE, MATCH, AWAY, NGRID = 1e-6, 1e-3, 1e-3, 720
NPLANES, PLANE_SEED = 200, 1399
SNAPPY_SEED = 1399          # SnapPy's generator choice is random; seeded before every manifold is built, so the solved basis is reproducible
TWO_PI = 2 * math.pi


class Unresolved(Exception):
    pass


# ------------------------------------------------------------------------------------------------ the solved basis of V
def cuspidal_basis(M):
    G = M.fundamental_group(simplify_presentation=False)
    n = G.num_generators()

    def vec(word):
        x = [0] * n
        for g in word:
            x[abs(g) - 1] += 1 if g > 0 else -1
        return x
    rows = [vec(r) for r in G.relators(as_int_list=True)] + [vec(w) for pair in G.peripheral_curves(as_int_list=True) for w in pair]
    null = sympy.Matrix(rows).nullspace()
    B = []
    for col in null:
        x = np.array([float(e) for e in col])
        B.append(x / x[np.argmax(np.abs(x))])
    B = np.array(B).reshape(len(B), n)
    v = {}
    for g in range(n):
        v[g + 1], v[-(g + 1)] = B[:, g].copy(), -B[:, g].copy()
    return v, B, G


# ------------------------------------------------------------------------------------------------ B1387's charts and solve, class as a vector
class VCharts(HF.Charts):
    def __init__(self, P, v, d):                                    # B1387's Charts.__init__, the class carried as a d-vector
        self.P = P
        edges = []
        for i in range(P.ntet):
            for F in HF.FACES:
                g = P.info[i][F]
                if g:
                    _, s, _, perm = P.pairing[(i, F)]
                    for vv in HF.FACE_VERTS[F]:
                        edges.append((P.vclass[s][perm.image(vv)], P.vclass[i][vv], g))
        self.cusp_of_vertex, pos, count = {}, {}, {}
        for i in range(P.ntet):
            for vv in HF.V:
                u = P.vclass[i][vv]
                self.cusp_of_vertex[u], pos[u] = P.cusp_of[i][vv], P.verts[i][vv]
                count[u] = count.get(u, 0) + 1
        adj = {}
        for uS, uT, g in edges:
            adj.setdefault(uS, []).append((uT, g, +1))
            adj.setdefault(uT, []).append((uS, g, -1))
        self.gamma, self.vgam, self.base, self.A, self.Ainv, self.lat, self.parabolic_v = {}, {}, {}, {}, {}, {}, {}
        for c in range(P.M.num_cusps()):
            u0 = max((u for u, cc in self.cusp_of_vertex.items() if cc == c), key=lambda u: count[u])
            self.base[c] = u0
            A = np.array([[pos[u0], -1], [1, 0]], dtype=complex)
            self.A[c], self.Ainv[c] = A, np.linalg.inv(A)
            self.gamma[u0], self.vgam[u0] = np.eye(2, dtype=complex), np.zeros(d)
            lam, pv = [], []
            queue = deque([u0])
            while queue:
                u = queue.popleft()
                for w, g, sgn in adj.get(u, []):
                    if sgn == +1:
                        gw, vw = self.gamma[u] @ P.geninv[g], self.vgam[u] - v[g]
                    else:
                        gw, vw = self.gamma[u] @ P.gen[g], self.vgam[u] + v[g]
                    if w not in self.gamma:
                        self.gamma[w], self.vgam[w] = gw, vw
                        queue.append(w)
                    else:
                        p = gw @ np.linalg.inv(self.gamma[w])
                        if min(np.abs(p - np.eye(2)).max(), np.abs(p + np.eye(2)).max()) > 1e-8:
                            q = self.Ainv[c] @ p @ A
                            q = q / q[1, 1]
                            assert abs(q[1, 0]) < 1e-6 and abs(q[0, 0] - 1) < 1e-6, "a loop at the cusp is not a translation"
                            lam.append(q[0, 1])
                            pv.append(float(np.max(np.abs(vw - self.vgam[w]))))
            self.lat[c] = HF._lattice_basis(lam)
            self.parabolic_v[c] = max(pv) if pv else 0.0


class VSolver(HF.Solver):
    def equations(self, c, tau, Q, rng):                            # B1387's equations, the right-hand side a d-vector
        b1, b2 = self.C.lat[c]
        i0 = next(i for i in range(self.P.ntet) for vv in HF.V if self.P.vclass[i][vv] == self.C.base[c])
        rows, rhs, taus = [], [], []
        for a in range(Q):
            for b in range(Q):
                y = (((a + 0.5 + rng.uniform(-0.3, 0.3)) / Q) * b1 + ((b + 0.5 + rng.uniform(-0.3, 0.3)) / Q) * b2, tau * self.s[c])
                i, Ps, acc, _ = self.P.walk(i0, HF.act(self.C.A[c], y), self.v)
                tb, cb, ub, yb = self.best_chart(i, Ps)
                r = self.row(c, y)
                self.row(cb, yb, -1.0, r)
                val = np.zeros(self.d) + acc - self.C.vgam[ub]
                if np.abs(r).max() < 1e-12 and np.all(np.abs(val) < 1e-12):
                    continue
                rows.append(r)
                rhs.append(val)
                taus.append(tb)
        return rows, rhs, taus


def solve_basis(M, v, d, Kn, tau, chart_seed, sample_seed):
    t0 = time.time()
    P = HF.Polyhedron(M, seed=chart_seed)
    C = VCharts(P, v, d)
    S = VSolver(P, C, v, Kn)
    S.d = d
    rng = random.Random(sample_seed)
    rows, rhs, taus = [], [], []
    for c in range(S.nc):
        Q = int(math.ceil(math.sqrt(1.6 * 2 * len(S.modes[c][0])))) + 2
        r, b, t = S.equations(c, tau, Q, rng)
        rows += r
        rhs += b
        taus += t
    A, Bm = np.array(rows), np.array(rhs)
    X, _, rank, sv = np.linalg.lstsq(A, Bm, rcond=None)
    res = A @ X - Bm
    test = []
    for c in range(S.nc):
        for tt in TEST_TAUS:
            r, bb, _ = S.equations(c, tt, 12, random.Random(1000 + 17 * c))
            test.append(np.array(r) @ X - np.array(bb))
    test = np.vstack(test)
    stats = {"Kn": Kn, "tau": tau, "sample seed": sample_seed, "unknowns": S.ncol, "equations": len(Bm), "full rank": bool(rank == S.ncol),
             "condition": float(sv[0] / sv[-1]), "fit residual rms": float(np.sqrt(np.mean(res ** 2, axis=0)).max()),
             "test residual rms": float(np.sqrt(np.mean(test ** 2, axis=0)).max()), "lowest pulled-back height": float(min(taus)),
             "parabolic max": float(max(C.parabolic_v.values())), "seconds": round(time.time() - t0, 1)}
    return S, X, stats


def accepted(st):
    return (st["full rank"] and st["parabolic max"] < PARABOLIC_MAX and st["fit residual rms"] < FIT_MAX
            and st["test residual rms"] < TEST_MAX and st["tau"] < st["lowest pulled-back height"])


# ------------------------------------------------------------------------------------------------ the shells, decided on V
def shell_data(S, X, nshell=6):
    out = {}
    for c in range(S.nc):
        per = [S.shells(X[:, i], c, nshell) for i in range(X.shape[1])]
        shells = []
        for j in range(len(per[0])):
            ks = [k for k, _ in per[0][j][1]]
            for i in range(1, len(per)):
                assert [k for k, _ in per[i][j][1]] == ks
            Mj = np.array([[z for _, z in per[i][j][1]] for i in range(len(per))], dtype=complex).T      # m x d
            shells.append((float(per[0][j][0]), ks, Mj))
        out[c] = shells
    return out


def real_map(Mj):
    return np.vstack([Mj.real, Mj.imag])


def leading(shells):
    norms = [float(np.linalg.svd(real_map(Mj), compute_uv=False)[0]) for _, _, Mj in shells]
    top = max(norms)
    for j, nj in enumerate(norms):
        r = nj / top
        if r < AMB_LO:
            continue
        if r >= AMB_HI:
            return j, [n / top for n in norms]
        raise Unresolved("shell %d at ratio %.2e: ambiguous kill" % (j, r))
    raise Unresolved("every shell killed")


# ------------------------------------------------------------------------------------------------ C on a circle
def adist(a, b):
    return abs((a - b + math.pi) % TWO_PI - math.pi)


def chi_at(ks, a, b, th):
    """B1387's Morse count for the leading shell of cos(th) w1 + sin(th) w2 (a, b: its coefficient vectors for w1, w2)"""
    z = math.cos(th) * a + math.sin(th) * b
    try:
        return HF.chi_plus(list(zip([tuple(k) for k in ks], z)))[0]
    except AssertionError:
        raise Unresolved("Morse count incomplete")


def crit_breakpoints(K, ga, gb):
    """the breakpoints psi(x) +- pi/2 with their jumps, from the zeros of g1 grad g2 - g2 grad g1 (B1399 design-time machinery)"""
    complete = False
    for seeds in (64, 128, 256):
        P = BC.zeros_of_h(K, ga, gb, seeds)
        h, Dh, g1, g2 = BC.h_and_Dh(K, ga, gb, P)
        rho = np.hypot(g1, g2)
        rmax = np.max(np.hypot(*BC.h_and_Dh(K, ga, gb, np.random.default_rng(1).random((4000, 2)))[2:]))
        idx = np.sign(np.linalg.det(Dh)) if len(P) else np.array([])
        common = rho < 1e-7 * rmax
        if idx.sum() == 0 and np.all(idx[common] == 1):
            complete = True
            break
    if not complete:
        raise Unresolved("critical points of the angle map incomplete at 256 seeds")
    out = []
    for r, dd, G1, G2 in zip(rho, idx, g1, g2):
        if r < 1e-7 * rmax:
            continue
        psi = math.atan2(G2, G1)
        saddle = dd < 0
        out.append(((psi + math.pi / 2) % TWO_PI, +1 if saddle else -1))
        out.append(((psi - math.pi / 2) % TWO_PI, -1 if saddle else +1))
    return out


def merge(bps):
    """merge breakpoints closer than MERGE (cyclically), adding their jumps"""
    bps = sorted(bps)
    if not bps:
        return []
    groups = [[bps[0]]]
    for th, j in bps[1:]:
        if th - groups[-1][-1][0] < MERGE:
            groups[-1].append((th, j))
        else:
            groups.append([(th, j)])
    if len(groups) > 1 and (groups[0][0][0] + TWO_PI) - groups[-1][-1][0] < MERGE:
        groups[0] = groups.pop() + groups[0]
    out = []
    for gp in groups:
        ths = [t for t, _ in gp]
        ref = ths[0]
        mean = (ref + np.mean([((t - ref + math.pi) % TWO_PI) - math.pi for t in ths])) % TWO_PI
        out.append((float(mean), sum(j for _, j in gp)))
    return sorted(out)


def arcs_of(bps):
    """the arcs between consecutive breakpoints: (start, length); one full arc if there are none"""
    if not bps:
        return [(0.0, TWO_PI)]
    ths = [t for t, _ in bps]
    return [(ths[i], (ths[(i + 1) % len(ths)] - ths[i]) % TWO_PI or TWO_PI) for i in range(len(ths))]


def value_on(bps, vals, th):
    """the value of a piecewise-constant function (arcs_of(bps), vals) at the angle th"""
    if not bps:
        return vals[0]
    ths = [t for t, _ in bps]
    i = bisect_right(ths, th % TWO_PI) - 1
    return vals[i % len(ths)]


def cusp_on_circle(ks, Mj, W):
    a, b = Mj @ W[0], Mj @ W[1]
    if len(ks) <= 2:
        return dict(kind="bands", bps=[], vals=[0], a=a, b=b, ks=ks)
    R = np.column_stack([np.concatenate([a.real, a.imag]), np.concatenate([b.real, b.imag])])
    s, vt = np.linalg.svd(R, full_matrices=False)[1:]
    r = s[1] / s[0]
    if AMB_LO <= r < AMB_HI:
        raise Unresolved("the leading shell's rank on the circle is ambiguous (%.2e)" % r)
    if r < AMB_LO:                                                   # real rank one: +- one function
        kern = math.atan2(vt[1][1], vt[1][0]) % TWO_PI
        bps = [(kern, 0), ((kern + math.pi) % TWO_PI, 0)]
        kind = "rank one"
    else:
        K = np.array([list(k) for k in ks], dtype=float)
        bps = crit_breakpoints(K, -a, -b)                            # g = -(shell): d+ = {g > 0}
        kind = "generic"
    bps = merge(bps)
    arcs = arcs_of(bps)
    vals = [chi_at(ks, a, b, st + ln / 2) for st, ln in arcs]
    if kind == "generic":
        for i, (th, jump) in enumerate(bps):
            if vals[i] - vals[i - 1] != jump:
                raise Unresolved("jump accounting fails at %.6f: %d vs predicted %d" % (th, vals[i] - vals[i - 1], jump))
    else:
        if vals[0] != -vals[1]:
            raise Unresolved("rank-one shell is not odd on the circle")
        bps = [(t, vals[i] - vals[i - 1]) for i, (t, _) in enumerate(bps)]
    return dict(kind=kind, bps=bps, vals=vals, a=a, b=b, ks=ks)


def circle(shells, lead, W):
    cusps = {c: cusp_on_circle(shells[c][lead[c]][1], shells[c][lead[c]][2], W) for c in shells}
    union = merge([(t, 0) for cu in cusps.values() for t, _ in cu["bps"]])
    arcs = arcs_of(union)
    vals = []
    for st, ln in arcs:
        mid = (st + ln / 2) % TWO_PI
        vals.append(-sum(value_on(cu["bps"], cu["vals"], mid) for cu in cusps.values()))
    bps = [(t, vals[i] - vals[i - 1]) for i, (t, _) in enumerate(union)] if union else []
    return dict(cusps=cusps, bps=bps, arcs=arcs, vals=vals, W=W)


def C_direct(circ, th):
    return -sum(0 if cu["kind"] == "bands" else chi_at(cu["ks"], cu["a"], cu["b"], th) for cu in circ["cusps"].values())


def cross_check(circ):
    bad = 0
    for j in range(NGRID):
        th = TWO_PI * j / NGRID
        if any(adist(th, t) < AWAY for t, _ in circ["bps"]):
            continue
        if C_direct(circ, th) != value_on(circ["bps"], circ["vals"], th):
            bad += 1
    if bad:
        raise Unresolved("cross-check: %d of %d directions disagree with their arcs" % (bad, NGRID))


def agree(c1, c2):
    b1, b2 = [t for t, _ in c1["bps"]], [t for t, _ in c2["bps"]]
    if len(b1) != len(b2):
        raise Unresolved("the seeds disagree on the number of breakpoints (%d, %d)" % (len(b1), len(b2)))
    if not b1:
        if c1["vals"] != c2["vals"]:
            raise Unresolved("the seeds disagree on C")
        return
    n = len(b1)
    best = min(range(n), key=lambda s: max(adist(b1[i], b2[(i + s) % n]) for i in range(n)))
    if max(adist(b1[i], b2[(i + best) % n]) for i in range(n)) >= MATCH:
        raise Unresolved("the seeds' breakpoints differ by more than 1e-3")
    if any(c1["vals"][i] != c2["vals"][(i + best) % n] for i in range(n)):
        raise Unresolved("the seeds disagree on C on an arc")


# ------------------------------------------------------------------------------------------------ realisability
def unit(th):
    return math.cos(th), math.sin(th)


def arcs_for_value(circ, t):
    out = []
    for (st, ln), val in zip(circ["arcs"], circ["vals"]):
        if val != t:
            continue
        n = max(1, math.ceil(ln / 3.0))
        piece = ln / n
        for i in range(n):
            lo = st + i * piece - (1e-4 if i else 0)
            hi = st + (i + 1) * piece + (1e-4 if i < n - 1 else 0)
            assert hi - lo < math.pi
            out.append((lo % TWO_PI, (hi - lo)))
    return out


def rows_for(p, arc):
    (st, ln), (pa, pb) = arc, p
    ux, uy = unit(st)
    wx, wy = unit(st + ln)
    r1 = [-uy * pa, -uy * pb, ux * pa, ux * pb]                     # det(u, Lp) >= 1
    r2 = [wy * pa, wy * pb, -wx * pa, -wx * pb]                     # det(Lp, u') >= 1
    return [r1, r2]


def feasible(rows):
    A = -np.array(rows, dtype=float)
    res = linprog(np.zeros(4), A_ub=A, b_ub=-np.ones(len(rows)), bounds=[(None, None)] * 4, method="highs")
    return res.status == 0


def assignments(circ, g):
    targets = [g * t for t in PATTERN]
    cand = [arcs_for_value(circ, t) for t in targets]
    if any(not c for c in cand):
        return
    order = sorted(range(6), key=lambda k: len(cand[k]))

    def dfs(i, rows, assign):
        if i == 6:
            yield list(assign)
            return
        k = order[i]
        for arc in cand[k]:
            r = rows + rows_for(CLASSES[k], arc)
            if feasible(r):
                yield from dfs(i + 1, r, assign + [(k, arc)])
    yield from dfs(0, [], [])


def max_margin(assign):
    rows = []
    for k, arc in assign:
        rows += rows_for(CLASSES[k], arc)
    A = np.array([r + [-1.0] for r in rows])                        # -(row . l) + s <= 0
    res = linprog(np.array([0, 0, 0, 0, -1.0]), A_ub=-A, b_ub=np.zeros(len(rows)) * 0,
                  bounds=[(-1, 1)] * 4 + [(0, 10)], method="highs")
    assert res.status == 0
    l = res.x[:4]
    return np.array([[l[0], l[1]], [l[2], l[3]]]), float(res.x[4])


def verify(L, circs, g):
    """C at the six image directions, directly from each seed's forms, and their distance from every breakpoint"""
    targets = [g * t for t in PATTERN]
    rows = []
    for k, (pa, pb) in enumerate(CLASSES):
        x, y = L @ np.array([pa, pb], dtype=float)
        th = math.atan2(y, x) % TWO_PI
        vals = [C_direct(c, th) for c in circs]
        far = min(adist(th, t) for c in circs for t, _ in c["bps"]) if any(c["bps"] for c in circs) else math.pi
        rows.append(dict(cls=CLASSES[k], target=targets[k], angle=th, C=vals, away=far))
    ok = all(all(v == r["target"] for v in r["C"]) and r["away"] > AWAY for r in rows)
    return ok, rows


def realise(circs, g, cap=200):
    """the first assignment whose max-margin L passes the direct re-verification with both seeds; tried assignments counted"""
    tried = 0
    for assign in assignments(circs[0], g):
        tried += 1
        L, s = max_margin(assign)
        ok, rows = verify(L, circs, g)
        if ok:
            return dict(L=L.tolist(), margin=s, rows=rows, assign=[(k, list(a)) for k, a in assign], tried=tried)
        if tried >= cap:
            break
    return dict(L=None, tried=tried)


def total_variation(circ):
    return sum(abs(j) for _, j in circ["bps"])


# ------------------------------------------------------------------------------------------------ one member
def planes(d):
    if d == 2:
        return [("V", np.eye(2))], {"V"}
    W = [("coord12", np.eye(3)[[0, 1]]), ("coord13", np.eye(3)[[0, 2]]), ("coord23", np.eye(3)[[1, 2]])]
    rng = np.random.default_rng(PLANE_SEED)
    normals = rng.normal(size=(NPLANES, 3))
    for i, nrm in enumerate(normals):
        nrm = nrm / np.linalg.norm(nrm)
        e = np.eye(3)[int(np.argmin(np.abs(nrm)))]
        w1 = np.cross(nrm, e)
        w1 /= np.linalg.norm(w1)
        w2 = np.cross(nrm, w1)
        W.append(("plane%03d" % i, np.array([w1, w2])))
    return W, {"coord12", "coord13", "coord23"}


def manifold(sig):
    snappy.set_rand_seed(SNAPPY_SEED)
    return snappy.Manifold(sig)


def run_member(M, expect_dim=None, label=""):
    t0 = time.time()
    out = dict(label=label, cusps=M.num_cusps(), tets=M.num_tetrahedra())
    v, B, G = cuspidal_basis(M)
    d = B.shape[0]
    out["dim"] = d
    if expect_dim is not None and d != expect_dim:
        out.update(status="unresolved", reason="cuspidal dimension %d, census says %d" % (d, expect_dim))
        return out
    rungs = []
    Ws, xcheck = planes(d)
    try:
        for Kn, tau in LADDER:
            trial = []
            for ss in SAMPLE_SEEDS:
                try:
                    S, X, st = solve_basis(M, v, d, Kn, tau, CHART_SEED, ss)
                except Exception as e:                               # a failed walk or chart: this rung fails for this seed
                    S, X, st = None, None, {"Kn": Kn, "tau": tau, "sample seed": ss, "error": repr(e)[:200]}
                trial.append((S, X, st))
            rungs.append(dict(stats=[t[2] for t in trial]))
            if not all(X is not None and accepted(st) for S, X, st in trial):
                rungs[-1]["accepted"] = "residuals"
                continue
            shells = [shell_data(S, X) for S, X, _ in trial]
            leads = [{c: leading(sh[c])[0] for c in sh} for sh in shells]
            if leads[0] != leads[1]:
                rungs[-1]["accepted"] = "leading shells differ between the seeds"
                continue
            lead = leads[0]
            circles_by_plane, disagree = [], None
            for name, W in Ws:
                circs = [circle(sh, lead, W) for sh in shells]
                try:
                    agree(circs[0], circs[1])
                except Unresolved as e:
                    disagree = "%s: %s" % (name, e)
                    break
                circles_by_plane.append((name, circs))
            if disagree:
                rungs[-1]["accepted"] = "seeds disagree on " + disagree
                continue
            rungs[-1]["accepted"] = True
            break
        else:
            out.update(rungs=rungs, status="unresolved", reason="no rung passes acceptance with both seeds", seconds=round(time.time() - t0))
            return out
        out["rungs"] = rungs
        out["leading"] = {str(c): dict(index=lead[c], vectors=len(shells[0][c][lead[c]][1]),
                                       kn=shells[0][c][lead[c]][0]) for c in shells[0]}
        maxC, gs, per = 0, set(), []
        positive = {}
        for name, circs in circles_by_plane:
            if name in xcheck:
                for cc in circs:
                    cross_check(cc)
            mc = max(abs(x) for x in circs[0]["vals"])
            tv = total_variation(circs[0])
            row = dict(plane=name, breakpoints=len(circs[0]["bps"]), total_variation=tv, maxC=mc, g=[])
            for g in range(1, mc // 2 + 1):
                if tv < 12 * g:
                    continue
                res = realise(circs, g)
                if res["L"] is not None:
                    row["g"].append(g)
                    gs.add(g)
                    positive.setdefault(g, dict(plane=name, **res))
            maxC = max(maxC, mc)
            per.append(row)
            if name == "V":
                out["V_circle"] = dict(bps=[[round(t, 6), j] for t, j in circs[0]["bps"]], vals=circs[0]["vals"])
        out.update(status="resolved", maxC=maxC, achievable_g=sorted(gs), g3=3 in gs, circles=per,
                   positive={str(k): val for k, val in positive.items()})
    except Unresolved as e:
        out.update(rungs=rungs, status="unresolved", reason=str(e))
    out["seconds"] = round(time.time() - t0)
    return out


# ------------------------------------------------------------------------------------------------ the banked identity
def banked_identity():
    rep = {}
    # (1) cube~3.24 reproduces B1387
    snappy.set_rand_seed(SNAPPY_SEED)
    M = HF.member()
    vB, _, dimB = HF.cuspidal_class(M)
    v, B, G = cuspidal_basis(M)
    assert dimB == 1 and B.shape[0] == 1
    n = B.shape[1]
    vp = np.array([vB[g + 1] for g in range(n)])
    lam = float(vp @ B[0] / (B[0] @ B[0]))
    assert np.abs(vp - lam * B[0]).max() < 1e-12
    rows = []
    for ss in SAMPLE_SEEDS:
        S, X, st = solve_basis(M, v, 1, 10.0, 0.10, CHART_SEED, ss)
        assert accepted(st), st
        sh = shell_data(S, X)
        lead = {c: leading(sh[c])[0] for c in sh}
        info = {c: (lead[c], len(sh[c][lead[c]][1]), sh[c][lead[c]][0] / sh[c][0][0]) for c in sh}
        # the direction v+ = sign(lam) e1: C = -sum chi
        s = 1.0 if lam > 0 else -1.0
        Cp = -sum(0 if len(sh[c][lead[c]][1]) <= 2 else HF.chi_plus(list(zip(sh[c][lead[c]][1], s * sh[c][lead[c]][2][:, 0])))[0] for c in sh)
        Cm = -sum(0 if len(sh[c][lead[c]][1]) <= 2 else HF.chi_plus(list(zip(sh[c][lead[c]][1], -s * sh[c][lead[c]][2][:, 0])))[0] for c in sh)
        ok_shells = (info[0][0] == 0 and info[0][1] == 3 and info[3][0] == 0 and info[3][1] == 3 and info[1][1] == 1 and info[1][0] >= 1
                     and info[2][0] >= 1 and info[2][1] == 3 and abs(info[2][2] - math.sqrt(3)) < 1e-6)
        rows.append(dict(seed=ss, stats=st, leading=info, C_vplus=Cp, C_minus=Cm, shells_as_B1387=ok_shells))
        assert Cp == 2 and Cm == -2 and ok_shells, rows[-1]
    rep["cube~3.24"] = rows
    # (2) the breakpoint machinery on the design-time synthetic shells
    rep["breakpoint machinery failures"] = BC.main(720)
    assert rep["breakpoint machinery failures"] == 0
    # (3) the linear-feasibility machinery on synthetic count functions
    rays = []
    for (pa, pb), t in zip(CLASSES, PATTERN):
        th = math.atan2(pb, pa) % TWO_PI
        rays += [(th, 3 * t), ((th + math.pi) % TWO_PI, -3 * t)]
    rays.sort()
    mids = [((rays[i][0] + ((rays[(i + 1) % 12][0] - rays[i][0]) % TWO_PI) / 2) % TWO_PI) for i in range(12)]

    def synthetic(values_by_ray):
        bps = sorted((m, 0) for m in mids)
        # arc i (starting at the sorted midpoint i) contains the ray following it
        vals = []
        for st, ln in arcs_of(bps):
            ray = min(rays, key=lambda r: adist(r[0], (st + ln / 2) % TWO_PI))
            vals.append(values_by_ray[ray[0]])
        bps = [(t, vals[i] - vals[i - 1]) for i, (t, _) in enumerate(bps)]
        return dict(cusps={}, bps=bps, arcs=arcs_of(bps), vals=vals)
    good = synthetic({th: val for th, val in rays})
    assign = next(assignments(good, 3), None)
    assert assign is not None
    L, s = max_margin(assign)
    imgs = [math.atan2(*(L @ np.array(p, dtype=float))[::-1]) % TWO_PI for p in CLASSES]
    assert all(value_on(good["bps"], good["vals"], th) == 3 * t for th, t in zip(imgs, PATTERN)) and s > 0
    # remove the jump between (3,-2) [3] and (1,0) [0]: both arcs carry 3 (and antipodally -3)
    th32, th10 = math.atan2(-2, 3) % TWO_PI, 0.0
    bad_vals = {th: val for th, val in rays}
    bad_vals[th10] = 3
    bad_vals[math.pi] = -3
    bad = synthetic(bad_vals)
    assert next(assignments(bad, 3), None) is None
    rep["linear feasibility"] = dict(realisable_found=True, max_margin=s, jump_removed_infeasible=True)
    # (4) B1398's target pattern, recomputed from the record's vectors
    FV = _load("b1398_frame_verdict", ROOT / "frontier" / "B1398_the_frame_verdict_on_three" / "verification" / "frame_verdict.py")
    got = FV.main()["V5 the anomaly-free family at g = 3: N per class"]
    want = {str(cls): 3 * t for cls, t in zip(CLASSES, PATTERN)}
    assert got == want, (got, want)
    rep["B1398 pattern"] = got
    return rep


# ------------------------------------------------------------------------------------------------ the census
def census_entry(entry):
    M = manifold(entry["isometry_signature"])
    r = run_member(M, expect_dim=entry["cuspidal_dim"], label=entry["isometry_signature"])
    r.update(parent=entry["parent"], degree=entry["degree"], index=entry["index"])
    return r


def census(workers=4, partial=HERE / "census_partial.jsonl"):
    from multiprocessing import Pool
    entries = json.load(open(HERE / "census_list.json"))["census"]
    done = set()
    if partial.exists():
        for line in open(partial):
            done.add(json.loads(line)["label"])
    todo = [e for e in entries if e["isometry_signature"] not in done]
    todo.sort(key=lambda e: (e["cuspidal_dim"], e["tets"]))
    with Pool(workers) as pool:
        for r in pool.imap_unordered(census_entry, todo):
            with open(partial, "a") as f:
                f.write(json.dumps(r, default=float) + "\n")
            print("%s dim %d cusps %d: %s %s maxC %s g %s (%ss)" % (r["label"][:24], r.get("dim", -1), r["cusps"], r["status"],
                  r.get("reason", ""), r.get("maxC"), r.get("achievable_g"), r.get("seconds")), flush=True)
    rows = [json.loads(line) for line in open(partial)]
    return rows


if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else "identity"
    if what == "identity":
        rep = banked_identity()
        print(json.dumps(rep, indent=1, default=str))
        print("BANKED IDENTITY: PASS")
    elif what == "member":
        M = manifold(sys.argv[2])
        print(json.dumps(run_member(M, label=sys.argv[2]), indent=1, default=str))
    elif what == "census":
        rows = census(int(sys.argv[2]) if len(sys.argv) > 2 else 4)
        print("DONE", len(rows))
