#!/usr/bin/env python3
"""SM-R581 (register row P-581, FL-26, Q-STRUCT): the structural package's rate in one comparison class.

Card: relays/cards/SM_R581_one-class-for-the-structural-grades.md (sealed before any run on the class).

Rule K (the one rule): the comparison class is every orientable one-cusped hyperbolic 3-manifold of the census with
at most 6 ideal tetrahedra, in census order, and the construction applied to each is F-MC's, unchanged: a surjection
pi_1 -> 2T (McKay: E6), then the fused cascade (B861), the global form (B862) and the hypercharge direction (B1160)
inside SU(5), and sin^2 theta_W at the SU(5) normalisation.

Per object it counts surjections pi_1 -> G up to Aut(G), by exhaustive enumeration over generator images with the
relators checked in G's multiplication table (the first image fixed to a conjugacy-class representative and weighted
by the class size), for G = 2T = SL(2,3) (E6), 2O (E7), 2I = SL(2,5) (E8), and two plants: Z/3 (every object has it,
rate must be 1; its count must equal 3^d - 1, d the F_3-rank of H_1 from the relator matrix) and (Z/2)^3 (no
two-generator group has it, rate must be 0 there). The steps after E6 take no object as input; they are computed
once, exactly, and enter every object's package with the same value.

  python3 run.py MAIN_CHECKOUT PRESENTATIONS.json OUT_DIR [--smoke]

Depends on the standard library, numpy and sympy, plus main's B862 module (frontier/B862_global_form/global_form.py)
and main's B993 output (sl23_baserate.json) as a per-object control. Data-free: no measured value is read.
"""
import hashlib
import importlib.util
import itertools
import json
import os
import sys
import time
from fractions import Fraction as Fr

import numpy as np
import sympy as sp


# ---------------------------------------------------------------------------------------------------- finite groups
class Group:
    def __init__(self, name, elements, mul, identity):
        self.name = name
        self.els = list(elements)
        self.n = len(self.els)
        idx = {e: i for i, e in enumerate(self.els)}
        self.MT = np.array([[idx[mul(x, y)] for y in self.els] for x in self.els], dtype=np.int64)
        self.ID = idx[identity]
        self.INV = np.array([int(np.where(self.MT[i] == self.ID)[0][0]) for i in range(self.n)], dtype=np.int64)
        assert all(sorted(row) == list(range(self.n)) for row in self.MT.tolist())        # a Latin square
        self._classes()
        self.aut_order = self._aut_order()

    def generated(self, gens):
        S = {self.ID}
        frontier = [self.ID]
        while frontier:
            nxt = []
            for s in frontier:
                for g in gens:
                    t = int(self.MT[s, g])
                    if t not in S:
                        S.add(t)
                        nxt.append(t)
            frontier = nxt
        return S

    def _classes(self):
        seen, reps, sizes = set(), [], []
        for x in range(self.n):
            if x in seen:
                continue
            cl = {int(self.MT[self.MT[g, x], self.INV[g]]) for g in range(self.n)}
            seen |= cl
            reps.append(x)
            sizes.append(len(cl))
        self.class_reps, self.class_sizes = reps, sizes

    def _aut_order(self):
        """|Aut(G)|: the image tuples of a minimal generating tuple that extend to an automorphism."""
        for r in (1, 2, 3):
            gt = next((t for t in itertools.product(range(self.n), repeat=r) if len(self.generated(list(t))) == self.n),
                      None)
            if gt is not None:
                break
        words = {self.ID: []}
        frontier = [self.ID]
        while frontier:
            nxt = []
            for s in frontier:
                for k, g in enumerate(gt):
                    t = int(self.MT[s, g])
                    if t not in words:
                        words[t] = words[s] + [k]
                        nxt.append(t)
            frontier = nxt
        order = lambda x: next(m for m in range(1, self.n + 1) if self._pow(x, m) == self.ID)
        ords = [order(g) for g in gt]
        cands = [[h for h in range(self.n) if order(h) == o] for o in ords]
        count = 0
        for imgs in itertools.product(*cands):
            m = np.empty(self.n, dtype=np.int64)
            for e, w in words.items():
                v = self.ID
                for k in w:
                    v = int(self.MT[v, imgs[k]])
                m[e] = v
            if len(set(m.tolist())) != self.n:
                continue
            if np.array_equal(m[self.MT], self.MT[m[:, None], m[None, :]]):
                count += 1
        return count

    def _pow(self, x, m):
        v = self.ID
        for _ in range(m):
            v = int(self.MT[v, x])
        return v


def sl2(p):
    els = [t for t in itertools.product(range(p), repeat=4) if (t[0] * t[3] - t[1] * t[2]) % p == 1]
    mul = lambda x, y: ((x[0] * y[0] + x[1] * y[2]) % p, (x[0] * y[1] + x[1] * y[3]) % p,
                        (x[2] * y[0] + x[3] * y[2]) % p, (x[2] * y[1] + x[3] * y[3]) % p)
    return els, mul, (1, 0, 0, 1)


def binary_octahedral():
    """2O as unit quaternions with coefficients in Q(sqrt 2), each a pair (a, b) = a + b sqrt 2, exact."""
    def fm(x, y):
        return (x[0] * y[0] + 2 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])

    def fa(*xs):
        return (sum(x[0] for x in xs), sum(x[1] for x in xs))

    def fn(x):
        return (-x[0], -x[1])

    def qm(p, q):
        a1, b1, c1, d1 = p
        a2, b2, c2, d2 = q
        return (fa(fm(a1, a2), fn(fm(b1, b2)), fn(fm(c1, c2)), fn(fm(d1, d2))),
                fa(fm(a1, b2), fm(b1, a2), fm(c1, d2), fn(fm(d1, c2))),
                fa(fm(a1, c2), fn(fm(b1, d2)), fm(c1, a2), fm(d1, b2)),
                fa(fm(a1, d2), fm(b1, c2), fn(fm(c1, b2)), fm(d1, a2)))
    z, o, h, r = (Fr(0), Fr(0)), (Fr(1), Fr(0)), (Fr(1, 2), Fr(0)), (Fr(0), Fr(1, 2))
    one = (o, z, z, z)
    gens = [(z, o, z, z), (h, h, h, h), (r, r, z, z)]          # i, (1+i+j+k)/2, (1+i)/sqrt 2
    S, frontier = {one}, [one]
    while frontier:
        nxt = []
        for s in frontier:
            for g in gens:
                t = qm(s, g)
                if t not in S:
                    S.add(t)
                    nxt.append(t)
        frontier = nxt
    return sorted(S), qm, one


def cyclic_power(p, r):
    els = list(itertools.product(range(p), repeat=r))
    return els, (lambda x, y: tuple((a + b) % p for a, b in zip(x, y))), tuple([0] * r)


def build_groups():
    G = {}
    G["2T"] = Group("2T = SL(2,3)", *sl2(3))
    G["2O"] = Group("2O", *binary_octahedral())
    G["2I"] = Group("2I = SL(2,5)", *sl2(5))
    G["Z3"] = Group("Z/3 (plant, rate 1)", *cyclic_power(3, 1))
    G["Z2^3"] = Group("(Z/2)^3 (plant, rate 0 on two generators)", *cyclic_power(2, 3))
    expect = {"2T": (24, 24), "2O": (48, 48), "2I": (120, 120), "Z3": (3, 2), "Z2^3": (8, 168)}
    for k, (n, a) in expect.items():                       # group orders and |Aut|: standard facts, checked here
        assert (G[k].n, G[k].aut_order) == (n, a), (k, G[k].n, G[k].aut_order)
    assert len(G["2O"].class_reps) == 8 and len(G["2I"].class_reps) == 9 and len(G["2T"].class_reps) == 7
    return G


# ------------------------------------------------------------------------------------------ homomorphism counting
def count_surjections(G, gens, rels):
    """(number of surjections pi_1 -> G, number up to Aut(G)) for the presentation <gens | rels>."""
    k = len(gens)
    gi = {g: i for i, g in enumerate(gens)}
    rest = np.array(list(itertools.product(range(G.n), repeat=k - 1)), dtype=np.int64).reshape(-1, k - 1)
    total = 0
    for rep, size in zip(G.class_reps, G.class_sizes):
        imgs = np.concatenate([np.full((rest.shape[0], 1), rep, dtype=np.int64), rest], axis=1)
        ok = np.ones(imgs.shape[0], dtype=bool)
        for w in rels:
            v = np.full(imgs.shape[0], G.ID, dtype=np.int64)
            for ch in w:
                col = imgs[:, gi[ch.lower()]]
                v = G.MT[v, col if ch.islower() else G.INV[col]]
            ok &= v == G.ID
        for row in imgs[ok]:
            if len(G.generated([int(x) for x in row])) == G.n:
                total += size
    assert total % G.aut_order == 0, (G.name, total)          # Aut(G) acts freely on surjections
    return total, total // G.aut_order


def rank_mod_p(rows, p):
    A = [[x % p for x in r] for r in rows]
    rank, ncol = 0, len(A[0]) if A else 0
    for c in range(ncol):
        piv = next((i for i in range(rank, len(A)) if A[i][c]), None)
        if piv is None:
            continue
        A[rank], A[piv] = A[piv], A[rank]
        inv = pow(A[rank][c], p - 2, p)
        A[rank] = [x * inv % p for x in A[rank]]
        for i in range(len(A)):
            if i != rank and A[i][c]:
                f = A[i][c]
                A[i] = [(x - f * y) % p for x, y in zip(A[i], A[rank])]
        rank += 1
    return rank


def h1_rank_mod_p(gens, rels, p):
    rows = [[w.count(g) - w.count(g.upper()) for g in gens] for w in rels]
    return len(gens) - (rank_mod_p(rows, p) if rows else 0)


# ------------------------------------------------------------- the steps after E6, which take no object as input
def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def object_independent_steps(main):
    """Computed once. Returns the three structural properties after E6 and the values they take."""
    b862 = load_module(os.path.join(main, "frontier", "B862_global_form", "global_form.py"), "b862_global_form")
    ker = b862.kernel_exact(6)
    assert len(b862.kernel_exact(72)) == len(ker)
    z6 = len(ker) == 6 and max(b862._order(g) for g in ker) == 6
    # the hypercharge direction: the traceless commutant of su(3)+su(2) (block-diagonal in 5 = 3 + 2) inside su(5)
    X = sp.Matrix(5, 5, lambda i, j: sp.Symbol("x%d%d" % (i, j)))
    gens = []
    for (a, b) in [(0, 1), (1, 2), (3, 4)]:
        for kind in (0, 1):
            E = sp.zeros(5, 5)
            if kind == 0:
                E[a, b], E[b, a] = 1, 1
            else:
                E[a, b], E[b, a] = sp.I, -sp.I
            gens.append(E)
    gens += [sp.diag(1, -1, 0, 0, 0), sp.diag(0, 1, -1, 0, 0), sp.diag(0, 0, 0, 1, -1)]
    eqs = [e for E in gens for e in (X * E - E * X)] + [X.trace()]
    sol = sp.solve(eqs, list(X), dict=True)[0]
    Y = X.subs(sol)
    free = sorted(Y.free_symbols, key=str)
    hyper_dim = len(free)
    Yv = Y.subs({free[0]: 1}) if free else Y
    diag = [Yv[i, i] for i in range(5)]
    off = all(Yv[i, j] == 0 for i in range(5) for j in range(5) if i != j)
    ratio = [sp.nsimplify(d / diag[0] * 2) for d in diag]               # scaled so the first entry is 2
    hyper_ok = hyper_dim == 1 and off and ratio == [2, 2, 2, -3, -3]
    # sin^2 theta_W at the SU(5) normalisation: Tr(T3^2) / Tr(Q^2) on the 5, Q = T3 + Y, Y the direction above
    T3 = [Fr(0), Fr(0), Fr(0), Fr(1, 2), Fr(-1, 2)]
    if not hyper_ok:
        return dict(Z6=bool(z6), hypercharge=False, hypercharge_commutant_dim=hyper_dim, sin2_SU5=None,
                    sin2_is_3_8=False)
    yv = [Fr(-int(x), 6) for x in ratio]                 # the computed direction, at the normalisation of the 5
    Q = [t + y for t, y in zip(T3, yv)]
    s2 = sum(t * t for t in T3) / sum(q * q for q in Q)
    return dict(Z6=bool(z6), hypercharge=bool(hyper_ok), hypercharge_commutant_dim=hyper_dim,
                sin2_SU5=str(s2), sin2_is_3_8=(s2 == Fr(3, 8)))


# ---------------------------------------------------------------------------------------------------------- main
def sha16(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()[:16]


def main():
    main_co, pres_path, out_dir = sys.argv[1], sys.argv[2], sys.argv[3]
    smoke = "--smoke" in sys.argv
    t0 = time.time()
    data = json.load(open(pres_path))
    G = build_groups()
    steps = object_independent_steps(main_co)
    rows = []
    for r in data["rows"]:
        gens, rels = r["gens"], r["rels"]
        row = dict(name=r["name"], tets=r["tets"], ngens=len(gens))
        for key in ("2T", "2O", "2I", "Z3", "Z2^3"):
            row[key] = count_surjections(G[key], gens, rels)[1]
        row["Z3_surjections_expected"] = 3 ** h1_rank_mod_p(gens, rels, 3) - 1
        row["Z3_surjections"] = row["Z3"] * G["Z3"].aut_order
        rows.append(row)
    # plants, on every input
    plant_rate1 = all(x["Z3"] >= 1 for x in rows)
    plant_h1 = all(x["Z3_surjections"] == x["Z3_surjections_expected"] for x in rows)
    two_gen = [x for x in rows if x["ngens"] == 2]
    plant_rate0 = all(x["Z2^3"] == 0 for x in two_gen)
    assert plant_rate1 and plant_h1 and plant_rate0, "a plant failed"
    if smoke:
        print("smoke ok: %d presentations outside the class; plants pass; %.1f s; no rate printed"
              % (len(rows), time.time() - t0))
        return 0
    N = len(rows)
    after_e6 = steps["Z6"] and steps["hypercharge"] and steps["sin2_is_3_8"]
    for x in rows:
        x["E6_route"] = x["2T"] >= 1
        x["package"] = x["E6_route"] and after_e6
    rate = lambda f, rs: (sum(1 for x in rs if f(x)), len(rs))
    props = {
        "E6 route (2T classes >= 1)": lambda x: x["2T"] >= 1,
        "exactly the root's count (2T classes == 2)": lambda x: x["2T"] == 2,
        "Z6 global form": lambda x: x["E6_route"] and steps["Z6"],
        "hypercharge direction": lambda x: x["E6_route"] and steps["hypercharge"],
        "sin^2 = 3/8 at SU(5)": lambda x: x["E6_route"] and steps["sin2_is_3_8"],
        "the package (all four)": lambda x: x["package"],
        "E7 label (2O classes >= 1)": lambda x: x["2O"] >= 1,
        "E8 label (2I classes >= 1)": lambda x: x["2I"] >= 1,
        "any exceptional label": lambda x: x["2T"] + x["2O"] + x["2I"] >= 1,
        "plant Z/3 (must be 1)": lambda x: x["Z3"] >= 1,
    }
    table = {k: rate(f, rows) for k, f in props.items()}
    by_tets = {t: rate(props["the package (all four)"], [x for x in rows if x["tets"] == t])
               for t in sorted({x["tets"] for x in rows})}
    root = next(x for x in rows if x["name"] == "m004")
    # control: per-object agreement with main's B993 output on the overlap (first 400 in census order)
    b993 = json.load(open(os.path.join(main_co, "frontier", "B993_cornerstone_verified", "verification",
                                       "sl23_baserate.json")))
    b993_rows = {x["name"]: x["classes"] for x in b993["rows"]}
    overlap = [x for x in rows if x["name"] in b993_rows]
    agree = sum(1 for x in overlap if x["2T"] == b993_rows[x["name"]])
    out = dict(rule="K: orientable, one cusp, ideal tetrahedra <= 6, census order; F-MC's construction unchanged",
               N=N, presentations_sha16=sha16(pres_path), presentations_meta=data["meta"],
               object_independent_steps=steps, rates={k: [a, b, a / b] for k, (a, b) in table.items()},
               package_rate_by_tetrahedra={t: [a, b] for t, (a, b) in by_tets.items()},
               root_m004=dict((k, root[k]) for k in ("2T", "2O", "2I", "Z3")),
               control_b993=dict(overlap=len(overlap), agree=agree),
               plants=dict(Z3_rate_1=plant_rate1, Z3_count_equals_3_to_d_minus_1=plant_h1,
                           Z2cubed_zero_on_two_generators=plant_rate0, two_generator_n=len(two_gen)),
               seconds=round(time.time() - t0, 1), rows=rows)
    os.makedirs(out_dir, exist_ok=True)
    jp = os.path.join(out_dir, "r581_results.json")
    with open(jp, "w") as f:
        json.dump(out, f, indent=1, sort_keys=True)
    lines = ["SM-R581: rule K, N = %d, presentations %s" % (N, out["presentations_sha16"]),
             "steps after E6 (object-independent): %s" % json.dumps(steps, sort_keys=True)]
    for k, (a, b) in table.items():
        lines.append("  %-44s %5d / %5d = %.4f" % (k, a, b, a / b))
    lines.append("package rate by tetrahedra: %s" % ", ".join("%d: %d/%d" % (t, a, b) for t, (a, b) in by_tets.items()))
    lines.append("root m004: %s" % json.dumps(out["root_m004"], sort_keys=True))
    lines.append("control B993 per object: %d of %d agree" % (agree, len(overlap)))
    lines.append("plants: %s" % json.dumps(out["plants"], sort_keys=True))
    txt = "\n".join(lines) + "\n"
    with open(os.path.join(out_dir, "r581_run.txt"), "w") as f:
        f.write(txt)
    print(txt, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
