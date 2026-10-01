#!/usr/bin/env python3
"""THE INTERACTION CENSUS: the relative triple product a u b u h on the generation-shaped backgrounds of a level.

A background (B1432/B1434) has six doublet sectors s with modules V_s = R (x) beta_s, R = [[l, ct],[0,1]] (l the extension
character).  If its count is +1 the zero mode of sector s is the interior class of H^1(M; V_s); if -1, of H^1(M; V_s*).
E6's invariant tensors restricted to two doublet sectors A, B and a spin-0 sector are the SL(2)_beta invariant
    T(a, b, w) = (a_1 b_2 - a_2 b_1) w,
and the spin-0 sector's character is then forced:  eta = (alpha_A beta_B)^(-sign).  The Higgs-type mode is the class of
H^1(M; eta).  Y(A, B) = <(a, e) u b u h, [M, dM]> by relcup.py.  Each class is a line, so a single Y is defined up to a
non-zero scale: its vanishing is an invariant, its value is not.
"""
import sys, json, time, pathlib, itertools
from collections import Counter, defaultdict
HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "frontier/B1434_the_architecture_census/verification"))
import architecture_census as ac
cc = ac.cc
from myindex import rank_and_null
from relcup import *

SECT = ["Q", "uc", "ec", "dc", "L", "nuc"]
CH = dict(Q=(1, 3), uc=(-4, 3), ec=(6, 3), dc=(2, 1), L=(-3, 1), nuc=(0, -5))
# spin-0 sectors of 78 + 27 + 27bar, charges (6Y, 3 gamma): the partner of a pair must have minus the pair's charge
SPIN0 = {(1, -2): "27:Q'", (-4, -2): "27:u'", (6, -2): "27:e'", (-2, 4): "27:D", (3, 4): "27:Hu",
         (-1, 2): "27b:Q'b", (4, 2): "27b:u'b", (-6, 2): "27b:e'b", (2, -4): "27b:Db", (-3, -4): "27b:Hd",
         (0, 0): "78:adj", (-5, 0): "78:X", (5, 0): "78:Xb", (-2, -6): "78:D", (3, -6): "78:Hu", (2, 6): "78:Db", (-3, 6): "78:Hd"}
def partner(A, B):
    c = (-(CH[A][0] + CH[B][0]), -(CH[A][1] + CH[B][1]))
    return SPIN0.get(c)

def Phi_of(eps, word, k):
    phi = ac.monodromy(eps, word); P = ac.IDENT
    for _ in range(k): P = ac.compose(phi, P)
    return {X: tuple(P[ac.X]), Y: tuple(P[ac.Y])}

def level_census(eps, word, k, pstart=3000):
    ng, rels, mu, lam, tau, A, tors = ac.level(eps, word, k)
    N = max(1, ac.torsion_exponent(A))
    saved = cc.cover; cc.cover = lambda _n: (ng, rels, mu, lam, tau)
    try: o, bgs, I, chars, _ = cc.census(k, N, pstart, nprimes=3, verbose=False)
    finally: cc.cover = saved
    return o, bgs, I, chars, N, rels, tau

class Plan:
    """one prefix tree for all the free-group words of a level's chain, and the index arrays of its cells"""
    def __init__(self, B, C, z):
        import numpy as np
        self.B = B; els = set()
        for cell in C:
            els.update(cell); els.add(B.mul(cell[0], cell[1]))
        for cell in z: els.update(cell)
        self.els = sorted(els, key=lambda g: (-len(g[0]), g)); self.idx = {g: i for i, g in enumerate(self.els)}
        node = {(): 0}; self.parent = [-1]; self.letter = [0]
        for f, n in self.els:                                # longest first: every prefix becomes a node once
            if f in node: continue
            for i in range(1, len(f) + 1):
                pf = f[:i]
                if pf not in node:
                    node[pf] = len(self.parent); self.parent.append(node[f[:i - 1]]); self.letter.append(f[i - 1])
        self.node_of = [node[f] for f, n in self.els]; self.tpow = [n for f, n in self.els]
        order = sorted(range(len(self.parent)), key=lambda j: j)          # parents are created before children
        self.order = order
        cells = list(C.items())
        self.i1 = np.array([self.idx[c[0]] for c, k in cells]); self.i2 = np.array([self.idx[c[1]] for c, k in cells])
        self.i3 = np.array([self.idx[c[2]] for c, k in cells]); self.i12 = np.array([self.idx[B.mul(c[0], c[1])] for c, k in cells])
        self.kC = np.array([k for c, k in cells], dtype=np.int64)
        zc = list(z.items())
        self.j1 = np.array([self.idx[c[0]] for c, k in zc]); self.j2 = np.array([self.idx[c[1]] for c, k in zc])
        self.kz = np.array([k for c, k in zc], dtype=np.int64)

class Evaluator:
    """the matrices and the cocycle values of one module on every element of the plan, as arrays"""
    def __init__(self, V, co, plan=None):
        self.V, self.co, self.r, self.c = V, co, {}, {}
        if plan is not None: self.tabulate(plan)
    def rho(self, g):
        if g not in self.r: self.r[g] = self.V.rho(g)
        return self.r[g]
    def val(self, g):
        if g not in self.c: self.c[g] = self.co(g)
        return self.c[g]
    def tabulate(self, plan):
        import numpy as np
        V, co = self.V, self.co; p = V.p; d = V.d; nn = len(plan.parent)
        R = [None] * nn; F = [None] * nn; R[0] = eye(d); F[0] = [0] * d
        for j in range(1, nn):
            g = plan.letter[j]; Rp = R[plan.parent[j]]; Fp = F[plan.parent[j]]
            if g > 0:
                F[j] = [(x + y) % p for x, y in zip(Fp, mvec(Rp, co.v[g], p))]; R[j] = mmul(Rp, V.M[g], p)
            else:
                R[j] = mmul(Rp, V.M[g], p); F[j] = [(x - y) % p for x, y in zip(Fp, mvec(R[j], co.v[-g], p))]
        rho = []; val = []
        for nd, n in zip(plan.node_of, plan.tpow):
            Rg, Fg = R[nd], F[nd]
            for _ in range(n):
                Fg = [(x + y) % p for x, y in zip(Fg, mvec(Rg, co.vt, p))]; Rg = mmul(Rg, V.Mt, p)
            rho.append(Rg); val.append(Fg)
        self.RHO = np.array(rho, dtype=np.int64); self.VAL = np.array(val, dtype=np.int64)

def z1_basis(V):
    d = V.d; n = 3 * d; p = V.p
    def resid(vec):
        c = Cocycle(V, vec[:d], vec[d:2 * d], vec[2 * d:], check=False); out = []
        for g in (X, Y):
            lhs = [(a + b - q) % p for a, b, q in zip(c.vt, mvec(V.Mt, c.v[g], p), mvec(V.rhoF(V.B.Phi[g]), c.vt, p))]
            out += [(l - r) % p for l, r in zip(lhs, c.onF(V.B.Phi[g]))]
        return out
    cols = [resid([int(i == j) for j in range(n)]) for i in range(n)]
    rk, NS = rank_and_null([list(r) for r in zip(*cols)], n, p, want_null=True)
    return NS
def b1_basis(V):
    d = V.d; p = V.p; I = eye(d); out = []
    for i in range(d):
        v = [int(i == j) for j in range(d)]
        dv = lambda M: [(a - b) % p for a, b in zip(mvec(M, v, p), v)]
        out.append(dv(V.M[X]) + dv(V.M[Y]) + dv(V.Mt))
    return out
def classes(V):
    """representatives of a basis of H^1(G; V)"""
    Z = z1_basis(V); Bb = [b for b in b1_basis(V) if any(b)]; n = 3 * V.d; p = V.p
    cur = list(Bb); rk = rank_and_null(cur, n, p)[0] if cur else 0; reps = []
    for zc in Z:
        r2 = rank_and_null(cur + [zc], n, p)[0]
        if r2 > rk: cur.append(zc); rk = r2; reps.append(Cocycle(V, zc[:V.d], zc[V.d:2 * V.d], zc[2 * V.d:]))
    return reps

def my_module(B, lc, al, ct, N, zeta, p, dual):
    M = cc.module(lc, al, ct, 3, N, zeta, p)
    V = Module(B, M.M['a'], M.M['b'], M.M['c'], p)
    return V.dual() if dual else V
def char_module(B, ex, N, zeta, p):
    return Module(B, [[pow(zeta, ex[0] % N, p)]], [[pow(zeta, ex[1] % N, p)]], [[pow(zeta, ex[2] % N, p)]], p)

def Yval(B, C, z, Ea, Eb, Eh, e, p):
    """reference implementation, cell by cell (used by the controls and cross-checked against Yfast)"""
    tot = 0
    for (g1, g2, g3), k in C.items():
        a = Ea.val(g1); b = mvec(Eb.rho(g1), Eb.val(g2), p); w = Eh.rho(B.mul(g1, g2))[0][0] * Eh.val(g3)[0] % p
        tot += k * (a[0] * b[1] - a[1] * b[0]) * w
    for (g1, g2), k in z.items():
        b = Eb.val(g1); w = Eh.rho(g1)[0][0] * Eh.val(g2)[0] % p
        tot -= k * (e[0] * b[1] - e[1] * b[0]) * w
    return tot % p

def Yfast(plan, Ea, Eb, Eh, e, p):
    import numpy as np
    a = Ea.VAL[plan.i1]; Rb = Eb.RHO[plan.i1]; bv = Eb.VAL[plan.i2]
    b0 = (Rb[:, 0, 0] * bv[:, 0] + Rb[:, 0, 1] * bv[:, 1]) % p; b1 = (Rb[:, 1, 0] * bv[:, 0] + Rb[:, 1, 1] * bv[:, 1]) % p
    w = Eh.RHO[plan.i12, 0, 0] * Eh.VAL[plan.i3, 0] % p
    tot = int(((((a[:, 0] * b1 - a[:, 1] * b0) % p) * w % p) * plan.kC).sum() % p)
    bz = Eb.VAL[plan.j1]; wz = Eh.RHO[plan.j1, 0, 0] * Eh.VAL[plan.j2, 0] % p
    tot -= int(((((e[0] * bz[:, 1] - e[1] * bz[:, 0]) % p) * wz % p) * plan.kz).sum() % p)
    return tot % p

def background_couplings(B, C, z, key, cnt, rels, N, zeta, p, plan=None, cache=None):
    """all pair couplings of one background at one prime: {(A,B): dict(Y, eta, h1, h_t, allowed)}"""
    if plan is None: plan = Plan(B, C, z)
    if cache is None: cache = {}
    lc = key[0]; al = dict(zip(SECT, key[1:])); sg = cnt[0]
    if ("ct", lc) not in cache:
        h1, ct = cc.cocycle(lc, rels, 3, N, zeta, p); assert ct is not None; cache[("ct", lc)] = ct
    ct = cache[("ct", lc)]
    add = lambda x, y: tuple((a + b) % N for a, b in zip(x, y)); neg = lambda x: tuple((-a) % N for a in x)
    E = {}; lifts = {}
    for s, c in zip(SECT, cnt):
        if c != sg: continue
        ck = ("V", lc, al[s], sg)
        if ck not in cache:
            V = my_module(B, lc, al[s], ct, N, zeta, p, dual=(sg < 0))
            reps = classes(V); assert len(reps) == 1, (s, len(reps))
            e = relative_lift(reps[0]); assert e is not None, ("the firing class is not interior", s)
            cache[ck] = (Evaluator(V, reps[0], plan), e)
        E[s], lifts[s] = cache[ck]
    out = {}
    for A, Bs in itertools.combinations_with_replacement([s for s in SECT if s in E], 2):
        eta = add(add(al[A], al[Bs]), neg(lc))               # alpha_A beta_B
        if sg > 0: eta = neg(eta)
        if ("H", eta) not in cache:
            Vh = char_module(B, eta, N, zeta, p); reps = classes(Vh)
            cache[("H", eta)] = (Vh, reps, Evaluator(Vh, reps[0], plan) if len(reps) == 1 else None)
        Vh, reps, Eh = cache[("H", eta)]
        rec = dict(eta=list(eta), eta_trivial_on_fibre=(eta[0] == 0 and eta[1] == 0), h1=len(reps), allowed=partner(A, Bs))
        if Eh is not None:
            rec["h_t"] = reps[0].vt[0] % p
            rec["Y"] = Yfast(plan, E[A], E[Bs], Eh, lifts[A], p)
            if A != Bs: rec["Y_swapped"] = Yfast(plan, E[Bs], E[A], Eh, lifts[Bs], p)
        out[(A, Bs)] = rec
    return out

def run_level(eps, word, k, pstart=3000, verbose=True, limit=None):
    t0 = time.time()
    o, bgs, I, chars, N, rels, tau = level_census(eps, word, k, pstart)
    B = Bundle(Phi_of(eps, word, k)); C, z, _ = B.fundamental()
    P = o["primes"]; zeta = {p: pow(cc.primroot(p), (p - 1) // N, p) for p in P}
    res = []; plan = Plan(B, C, z); caches = {p: {} for p in P}; last_lc = None
    for n, (key, cnt) in enumerate(sorted(bgs.items())):
        if limit and n >= limit: break
        if n and key[0] != last_lc:                          # the matter modules of a locus are not needed again
            for p in P:
                for ck in [ck for ck in caches[p] if ck[0] != "H"]: del caches[p][ck]
        last_lc = key[0]
        per = [background_couplings(B, C, z, key, cnt, rels, N, zeta[p], p, plan, caches[p]) for p in P]
        row = dict(key=[list(c) for c in key], counts=list(cnt), pairs={})
        for pair in per[0]:
            recs = [pp[pair] for pp in per]
            nz = [bool(r.get("Y")) for r in recs]; hz = [bool(r.get("h_t")) for r in recs]
            sym = [("Y_swapped" not in r) or (r["Y"] == r["Y_swapped"]) for r in recs]
            row["pairs"]["%s.%s" % pair] = dict(eta=recs[0]["eta"], fibre_trivial=recs[0]["eta_trivial_on_fibre"], h1=[r["h1"] for r in recs],
                                               allowed=recs[0]["allowed"], nonzero=nz, h_t_nonzero=hz, symmetric=sym)
        res.append(row)
    if verbose: print("level", eps, word, k, "backgrounds", len(res), "cells", len(C), "seconds", round(time.time() - t0, 1), flush=True)
    return dict(state=("+" if eps > 0 else "-") + word, k=k, N=N, primes=P, cells=len(C), backgrounds=res)

def summarize(lv):
    pat = Counter(); bad = 0
    for row in lv["backgrounds"]:
        sig = []
        for name, r in sorted(row["pairs"].items()):
            if len(set(r["nonzero"])) != 1 or len(set(r["h1"])) != 1: bad += 1
            if r["allowed"]: sig.append((name, r["allowed"], r["h1"][0], r["nonzero"][0], r["h_t_nonzero"][0], r["fibre_trivial"]))
        pat[(row["counts"][0] > 0, tuple(sig))] += 1
    return pat, bad

def compact(lv):
    """per background: key, counts and, per pair, [allowed, h1, fibre_trivial, nonzero, h_t_nonzero] (primes agreeing) or the raw triple lists"""
    out = dict(state=lv["state"], k=lv["k"], N=lv["N"], primes=lv["primes"], cells=lv["cells"], backgrounds=[])
    for row in lv["backgrounds"]:
        pr = {}
        for name, r in row["pairs"].items():
            agree = len(set(r["nonzero"])) == 1 and len(set(r["h1"])) == 1 and len(set(r["h_t_nonzero"])) == 1 and all(r["symmetric"])
            pr[name] = [r["allowed"], r["h1"][0], r["fibre_trivial"], r["nonzero"][0], r["h_t_nonzero"][0]] if agree else dict(DISAGREE=r)
        out["backgrounds"].append(dict(key=row["key"], counts=row["counts"], pairs=pr))
    return out

def population():
    r = json.load(open(REPO / "frontier/B1434_the_architecture_census/verification/architecture_census.json"))
    return [(o["state"], o["k"], o["generation_backgrounds"]) for o in r if o.get("generation_backgrounds")]

if __name__ == "__main__":
    if sys.argv[1] == "all":                                  # all <slice> <nslices> <outdir>
        sl, ns, outdir = int(sys.argv[2]), int(sys.argv[3]), pathlib.Path(sys.argv[4])
        pop = sorted(population(), key=lambda t: t[2])
        for i, (st, k, nb) in enumerate(pop):
            if i % ns != sl: continue
            eps = 1 if st[0] == "+" else -1
            lv = run_level(eps, st[1:], k)
            assert len(lv["backgrounds"]) == nb, ("background count differs from B1434", st, k, len(lv["backgrounds"]), nb)
            pat, bad = summarize(lv)
            print(st, k, "backgrounds", nb, "prime disagreements", bad, "patterns", len(pat), flush=True)
            json.dump(compact(lv), open(outdir / ("couplings_%s_%d.json" % (st.replace("+", "p").replace("-", "m"), k)), "w"))
    else:
        eps = 1 if sys.argv[1][0] == "+" else -1; word = sys.argv[1][1:]; k = int(sys.argv[2])
        lv = run_level(eps, word, k)
        pat, bad = summarize(lv)
        print("prime disagreements:", bad)
        for (sgn, sig), n in sorted(pat.items(), key=lambda kv: -kv[1]):
            print(n, "backgrounds, sign", "+" if sgn else "-")
            for q in sig: print("   ", q)
        if len(sys.argv) > 3: json.dump(compact(lv), open(sys.argv[3], "w"))
