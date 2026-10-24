#!/usr/bin/env python3
"""W153 — the ladder: is the prime 5 forced? (the rule: W153_RULE.md, committed and pushed before this script).

  L1  Klein's ladder: |Delta(2, 3, N)| by coset enumeration for N = 2..5, against |PSL(2, Z/N)|; N = 6 infinite by an
      affine representation with a nonzero translation, N = 7 by an SL(2, R) representation with |tr| > 2
  L2  McKay: the binary groups <a, b> in SU(2) (orders 12, 24, 48, 120); Burnside's character table; the McKay graph
      against the affine T(2, 3, N); SL(2, Z/N) against the binary group by element-order counts
  L3  det C(T(2, 3, N)) = 6 - N for N = 2..8; 6N(1/2 + 1/3 + 1/N - 1) = 6 - N; SL(2, Z)'s torsion and abelianization
  L4  the chain in W135's icosian E8: E7 = the roots orthogonal to 1 (126, Gram determinant 2), fixed by conjugation,
      holding W135's 10 E6 frames; the D5 sets inside one E6 frame (40 roots each, determinant 4) and their orbits
      under the frame's stabilizer
  L5  the record's forced levels: rho'(T) (W134's rho_exact, twist k = 21), the theta qubit's g_T (W152), W28's lift,
      chi_eta(T), and B1601's primes read from W16's JSON
  R   the rules R1, R2, R3 and the rung each gives (no prediction)

    python3 -B the_ladder.py      # writes the_ladder.json beside itself
"""
import collections
import contextlib
import io
import itertools
import json
import sys
from pathlib import Path

import mpmath as mp
import networkx as nx
import numpy as np
import sympy as sp
from sympy.combinatorics.fp_groups import FpGroup
from sympy.combinatorics.free_groups import free_group
from sympy.matrices.normalforms import smith_normal_form

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_joint_computation as JC  # noqa: E402  (W135: B1270's icosians, frame, gram_det_basis; JC.W134 = W134)
    import the_higgs_as_a_qubit as HQ  # noqa: E402  (W152: G_T, mul)

BR = JC.W134
OUT = HERE / "the_ladder.json"
mp.mp.dps = 60
RUNG = {2: "D5", 3: "E6", 4: "E7", 5: "E8"}


# ------------------------------------------------------------------ helpers
def tree_edges(arms):
    """the tree with one centre (node 0) and arms of the given numbers of nodes"""
    edges, nxt = [], 1
    for a in arms:
        prev = 0
        for _ in range(a):
            edges.append((prev, nxt))
            prev, nxt = nxt, nxt + 1
    return edges, nxt


def T_graph(N):
    edges, n = tree_edges((1, 2, N - 1))
    G = nx.Graph()
    G.add_nodes_from(range(n))
    G.add_edges_from(edges)
    return G


AFFINE = {2: [(0, 2), (1, 2), (2, 3), (3, 4), (3, 5)],          # D5~: two branch nodes
          3: tree_edges((2, 2, 2))[0],                           # E6~ = T(3, 3, 3)
          4: tree_edges((1, 3, 3))[0],                           # E7~ = T(2, 4, 4)
          5: tree_edges((1, 2, 5))[0]}                           # E8~ = T(2, 3, 6)


def sl2_elements(N):
    return [m for m in itertools.product(range(N), repeat=4) if (m[0] * m[3] - m[1] * m[2]) % N == 1]


def sl2_order(m, N):
    a, b, c, d = m
    x, n = (a, b, c, d), 1
    while x != (1, 0, 0, 1):
        x = ((x[0] * a + x[1] * c) % N, (x[0] * b + x[1] * d) % N, (x[2] * a + x[3] * c) % N,
             (x[2] * b + x[3] * d) % N)
        n += 1
    return n


def psl_order(N):
    return len({min(m, tuple(-x % N for x in m)) for m in sl2_elements(N)})


# ------------------------------------------------------------------ L1
def L1():
    F, s, u = free_group("s u")
    orders = {N: int(FpGroup(F, [s ** 2, u ** 3, (s * u) ** N]).order()) for N in (2, 3, 4, 5)}
    psl = {N: psl_order(N) for N in range(2, 8)}
    polyhedra = {2: 6, 3: 12, 4: 24, 5: 60}                      # dihedron D3, tetrahedron, octahedron, icosahedron
    # N = 6: z -> a z + b, composed as maps; S a half turn about 0, U a third of a turn about 1
    w = sp.Rational(-1, 2) + sp.sqrt(3) * sp.I / 2

    def comp(f, g):                                              # f after g
        return (sp.expand(f[0] * g[0]), sp.expand(f[0] * g[1] + f[1]))

    def power(f, n):
        r = (sp.Integer(1), sp.Integer(0))
        for _ in range(n):
            r = comp(f, r)
        return r

    def is_id(f):
        return sp.simplify(f[0] - 1) == 0 and sp.simplify(f[1]) == 0

    Sa, Ua = (sp.Integer(-1), sp.Integer(0)), (w, 1 - w)
    Ui = (sp.expand(1 / w), sp.expand(-(1 - w) / w))
    rel6 = is_id(power(Sa, 2)) and is_id(power(Ua, 3)) and is_id(power(comp(Sa, Ua), 6)) and is_id(comp(Ua, Ui))
    X = comp(Sa, comp(Ua, comp(Sa, Ui)))
    translation = sp.simplify(X[0] - 1) == 0 and sp.simplify(X[1]) != 0
    # N = 7: SL(2, R) with A^2 = B^3 = (AB)^7 = -1
    c = 2 * mp.cos(mp.pi / 7)
    r = mp.sqrt(c ** 2 - 3)
    A = mp.matrix([[0, -1], [1, 0]])
    Bm = mp.matrix([[mp.mpf(1) / 2, (c + r) / 2], [(-c + r) / 2, mp.mpf(1) / 2]])
    I2 = mp.eye(2)
    res7 = max(mp.mnorm(A ** 2 + I2, 1), mp.mnorm(Bm ** 3 + I2, 1), mp.mnorm((A * Bm) ** 7 + I2, 1))
    letters = {"A": A, "B": Bm, "b": Bm ** -1}
    best = None
    for n in range(2, 7):
        for word in itertools.product("ABb", repeat=n):
            M = I2
            for ch in word:
                M = M * letters[ch]
            t = abs(M[0, 0] + M[1, 1])
            if t > 2 + mp.mpf(10) ** -30 and best is None:
                best = ("".join(word), t)
        if best:
            break
    ch = {"|Delta(2, 3, N)| = 6, 12, 24, 60 for N = 2..5": orders == {2: 6, 3: 12, 4: 24, 5: 60},
          "equal to |PSL(2, Z/N)| and the polyhedral rotation groups": all(orders[N] == psl[N] == polyhedra[N]
                                                                           for N in orders),
          "N = 6: the affine representation satisfies the relations exactly": bool(rel6),
          "N = 6: S U S U^-1 is a nonzero translation (infinite order)": bool(translation),
          "N = 7: the SL(2, R) representation satisfies the relations to 1e-40": bool(res7 < mp.mpf(10) ** -40),
          "N = 7: an element with |tr| > 2 (infinite order)": best is not None}
    return {"checks": ch, "orders": orders, "|PSL(2, Z/N)|": psl,
            "N = 6 translation": str(sp.nsimplify(sp.simplify(X[1]))),
            "N = 7 relation residual": mp.nstr(res7, 5),
            "N = 7 word with |tr| > 2": [best[0], mp.nstr(best[1], 20)] if best else None}, all(ch.values())


# ------------------------------------------------------------------ L2
def qm(w, x, y, z):
    return np.array([[w + 1j * x, y + 1j * z], [-y + 1j * z, w - 1j * x]])


def gkey(g):
    v = np.round(np.concatenate([g.real.ravel(), g.imag.ravel()]), 9) + 0.0
    return tuple(v.tolist())


def binary_group(N):
    ct = -np.cos(np.pi / N) / np.sin(np.pi / 3)
    st = np.sqrt(1 - ct ** 2)
    a = qm(0, 1, 0, 0)
    b = qm(np.cos(np.pi / 3), np.sin(np.pi / 3) * ct, np.sin(np.pi / 3) * st, 0)
    elems = {gkey(np.eye(2)): np.eye(2, dtype=complex)}
    frontier = list(elems.values())
    while frontier:
        new = []
        for g in frontier:
            for h in (a, b):
                k = g @ h
                kk = gkey(k)
                if kk not in elems:
                    elems[kk] = k
                    new.append(k)
        frontier = new
    return list(elems.values()), a, b


def elem_order(g):
    x, n = g.copy(), 1
    while np.abs(x - np.eye(2)).max() > 1e-8:
        x = x @ g
        n += 1
    return n


def character_table(G, seed=153):
    n = len(G)
    idx = {gkey(g): i for i, g in enumerate(G)}
    inv = [idx[gkey(g.conj().T)] for g in G]
    table = [[idx[gkey(G[i] @ G[j])] for j in range(n)] for i in range(n)]
    cls_of, classes = [-1] * n, []
    for i in range(n):
        if cls_of[i] >= 0:
            continue
        orb = sorted({table[table[h][i]][inv[h]] for h in range(n)})
        for e in orb:
            cls_of[e] = len(classes)
        classes.append(orb)
    r = len(classes)
    reps = [cl[0] for cl in classes]
    C = np.zeros((r, r, r))
    for i, Ki in enumerate(classes):
        for k, z in enumerate(reps):
            for x in Ki:
                C[i, cls_of[table[inv[x]][z]], k] += 1
    rng = np.random.default_rng(seed)
    for _ in range(20):
        M = sum(rng.normal() * C[i] for i in range(r))
        vals, vecs = np.linalg.eig(M)
        gap = min(abs(vals[p] - vals[q]) for p in range(r) for q in range(p + 1, r)) if r > 1 else 1.0
        if gap > 1e-6:
            break
    e = cls_of[idx[gkey(np.eye(2))]]
    sizes = np.array([len(cl) for cl in classes])
    chars = []
    for j in range(r):
        wv = vecs[:, j] / vecs[e, j]
        d = np.sqrt(n / np.sum(np.abs(wv) ** 2 / sizes))
        chars.append(d * wv / sizes)
    X = np.array(chars)
    return X, classes, sizes, reps, e, gap


def L2():
    rows, ok_all = {}, True
    for N in (2, 3, 4, 5):
        G, a, b = binary_group(N)
        n = len(G)
        X, classes, sizes, reps, e, gap = character_table(G)
        r = len(classes)
        row_orth = np.abs((X * sizes) @ X.conj().T - n * np.eye(r)).max()
        col_orth = np.abs(X.T @ X.conj() - np.diag(n / sizes)).max()
        dims = np.real(X[:, e])
        chiV = np.array([np.trace(G[k]) for k in reps])
        A = (X * sizes * chiV) @ X.conj().T / n
        Ai = np.rint(np.real(A)).astype(int)
        adj_dev = np.abs(A - Ai).max()
        Gm = nx.from_numpy_array(Ai)
        aff = nx.Graph(AFFINE[N])
        triv = [i for i in range(r) if np.abs(X[i] - 1).max() < 1e-8]
        H = Gm.copy()
        H.remove_node(triv[0])
        dvec = np.rint(dims).astype(int)
        null = np.abs((2 * np.eye(r) - Ai) @ dvec).max()
        sl = collections.Counter(sl2_order(m, N) for m in sl2_elements(N))
        bi = collections.Counter(elem_order(g) for g in G)
        c = {"order": n == {2: 12, 3: 24, 4: 48, 5: 120}[N],
             "a has order 4, b order 6, ab order 2N": (elem_order(a), elem_order(b),
                                                        elem_order(a @ b)) == (4, 6, 2 * N),
             "both orthogonality relations to 1e-9": bool(row_orth < 1e-9 and col_orth < 1e-9),
             "dimensions are positive integers": bool(np.abs(dims - np.rint(dims)).max() < 1e-9 and min(dims) > 0.5),
             "McKay matrix integral, symmetric, loop-free": bool(adj_dev < 1e-9 and (Ai == Ai.T).all()
                                                                and not np.diag(Ai).any()),
             "McKay graph isomorphic to the affine T(2, 3, N)": nx.is_isomorphic(Gm, aff),
             "the trivial representation is a leaf": len(triv) == 1 and Gm.degree(triv[0]) == 1,
             "removing it leaves T(2, 3, N)": nx.is_isomorphic(H, T_graph(N)),
             "dimensions are the affine null vector, sum d^2 = |G|": bool(null == 0 and int((dvec ** 2).sum()) == n)}
        same = sl == bi
        c["SL(2, Z/N) has the binary group's element-order counts exactly when N = 3, 5"] = same == (N in (3, 5))
        ok_all &= all(c.values())
        rows[str(N)] = {"checks": c, "classes": r, "dimensions": sorted(dvec.tolist()), "eigenvalue gap": float(gap),
                        "orthogonality residuals": [float(row_orth), float(col_orth)],
                        "McKay degrees": sorted(d for _, d in Gm.degree()),
                        "SL(2, Z/N) order counts": dict(sorted(sl.items())),
                        "binary group order counts": dict(sorted(bi.items())),
                        "rung": RUNG[N]}
    return {"rows": rows}, ok_all


# ------------------------------------------------------------------ L3
def cartan_det(N):
    edges, n = tree_edges((1, 2, N - 1))
    C = sp.eye(n) * 2
    for i, j in edges:
        C[i, j] = C[j, i] = -1
    return C.det()


def L3():
    dets = {N: int(cartan_det(N)) for N in range(2, 9)}
    Ns = sp.Symbol("N", positive=True)
    ident = sp.simplify(6 * Ns * (sp.Rational(1, 2) + sp.Rational(1, 3) + 1 / Ns - 1) - (6 - Ns)) == 0
    finite = [N for N in range(2, 30) if sp.Rational(1, 2) + sp.Rational(1, 3) + sp.Rational(1, N) > 1]
    S = sp.Matrix([[0, -1], [1, 0]])
    T = sp.Matrix([[1, 1], [0, 1]])

    def morder(M):
        P, n = M, 1
        while P != sp.eye(2):
            P, n = P * M, n + 1
        return n

    snf = smith_normal_form(sp.Matrix([[4, 0], [0, 6], [2, -3]]), domain=sp.ZZ)
    inv = sorted(abs(int(snf[i, i])) for i in range(2))
    ch = {"det C(T(2, 3, N)) = 6 - N for N = 2..8": all(dets[N] == 6 - N for N in dets),
          "6N(1/2 + 1/3 + 1/N - 1) = 6 - N identically": bool(ident),
          "finite exactly for N < 6 = 2*3": finite == [2, 3, 4, 5],
          "the last finite rung N = 5 is the only unimodular one": [N for N in range(2, 6) if dets[N] == 1] == [5],
          "S has order 4 and ST order 6 in SL(2, Z)": (morder(S), morder(S * T)) == (4, 6),
          "SL(2, Z)'s abelianization is Z/12": inv == [1, 12]}
    return {"checks": ch, "determinants": dets, "finite N": finite, "abelianization invariants": inv}, all(ch.values())


# ------------------------------------------------------------------ L4
def L4():
    key, bil, qmul, qinv, ONE = JC.key, JC.bil, JC.qmul, JC.qinv, JC.ONE
    units = JC.B.unit_icosians()
    roots = JC.B.e8_roots(units)
    E7 = [r for r in roots if bil(r, ONE) == 0]
    k7 = {key(r) for r in E7}
    n7, d7 = JC.gram_det_basis(E7)
    conj = lambda v, r: qmul(qmul(v, r), qinv(v))
    fixed = all({key(conj(v, r)) for r in E7} == k7 for v in units)
    order3 = [u for u in units if JC.order(u) == 3]
    subgroups = {frozenset({key(u), key(qmul(u, u))}) for u in order3}
    holds = True
    for sg in subgroups:
        w = next(u for u in order3 if key(u) in sg)
        perp, _, _ = JC.frame(w, roots)
        holds &= {key(r) for r in perp} <= k7
    w = order3[0]
    perp, rest, cls = JC.frame(w, roots)
    kp = {key(r) for r in perp}
    sets, sizes = {}, collections.Counter()
    for r in rest:
        D = [a for a in perp if bil(a, r) == 0]
        sizes[len(D)] += 1
        sets.setdefault(frozenset(key(a) for a in D), D)
    dets5 = collections.Counter(JC.gram_det_basis(D) for D in sets.values())
    stab = [v for v in units if {key(conj(v, r)) for r in perp} == kp]
    perms = {tuple(sorted((key(r), key(conj(v, r))) for r in perp)) for v in stab}
    labels = list(sets)
    parent = list(range(len(labels)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    where = {s: i for i, s in enumerate(labels)}
    closed = True
    for v in stab:
        for i, s in enumerate(labels):
            img = frozenset(key(conj(v, a)) for a in sets[s])
            if img not in where:
                closed = False
                continue
            parent[find(i)] = find(where[img])
    orbits = collections.Counter(find(i) for i in range(len(labels)))
    ch = {"126 roots orthogonal to 1, rank 7, Gram determinant 2 (E7)": len(E7) == 126 and (n7, d7) == (7, 2),
          "conjugation by every unit icosian fixes the E7 set": bool(fixed),
          "it contains each of W135's 10 E6 frames": len(subgroups) == 10 and bool(holds),
          "each of the 162 roots cuts exactly 40 frame roots (D5)": dict(sizes) == {40: 162},
          "27 distinct D5 sets in one E6 frame": len(sets) == 27,
          "each D5 set has rank 5 and Gram determinant 4": set(dets5) == {(5, 4)},
          "the frame's stabilizer acts as a group of order 6": len(perms) == 6,
          "the stabilizer permutes the 27 D5 sets": bool(closed),
          "the 27 D5 sets are not one orbit": len(orbits) > 1}
    return {"checks": ch, "E7 roots": len(E7), "E7 rank and determinant": [n7, str(d7)],
            "D5 cut sizes": dict(sizes), "D5 sets": len(sets), "D5 rank and determinant": [list(map(str, k))
                                                                                         for k in dets5],
            "stabilizer units": len(stab), "stabilizer permutations": len(perms),
            "D5 orbit sizes": sorted(orbits.values())}, all(ch.values())


# ------------------------------------------------------------------ L5
def L5():
    rS, rT = BR.rho_exact()
    cS, cT = BR.chi(21)
    Tp = (cT * rT).applyfunc(lambda x: sp.nsimplify(sp.simplify(sp.expand_complex(x))))

    def sorder(M, cap=96):
        P = M
        for n in range(1, cap + 1):
            if (P - sp.eye(M.shape[0])).applyfunc(lambda x: sp.simplify(sp.expand_complex(x))) == sp.zeros(*M.shape):
                return n
            P = P * M
        return None

    def projective_order_mp(g, cap=96):
        P = g
        for n in range(1, cap + 1):
            off = max(abs(P[0][1]), abs(P[1][0]))
            if off < mp.mpf(10) ** -40 and abs(P[0][0] - P[1][1]) < mp.mpf(10) ** -40:
                return n
            P = HQ.mul(P, g)
        return None

    gT = projective_order_mp(HQ.G_T)
    lift = sp.diag(sp.exp(sp.I * sp.pi / 4), sp.exp(-sp.I * sp.pi / 4))
    lift_order = sorder(lift)
    lift_proj = next(n for n in range(1, 17) if sp.simplify(sp.expand_complex((lift ** n)[0, 0]
                                                                               - (lift ** n)[1, 1])) == 0
                     and (lift ** n)[0, 1] == 0)
    eta = BR.chi(1)[1]
    eta_order = next(n for n in range(1, 97) if sp.simplify(sp.expand_complex(eta ** n - 1)) == 0)
    rho_order = sorder(Tp)
    cp = json.loads((HERE / "the_common_point_mod_3.json").read_text(encoding="utf-8"))
    odd = {f["p"] for row in cp["rows"] if row["odd trace"] for f in row["prime factors"]}
    even = {f["p"] for row in cp["rows"] if not row["odd trace"] for f in row["prime factors"]}
    odd_norm = {row["norm of (x, y, z)"] for row in cp["rows"] if row["odd trace"]}
    orders = {"rho'(T), twist 21 (W136)": rho_order, "the theta qubit's g_T, projective (W152)": gT,
              "W28's lift e^{i pi Z/4}": lift_order, "W28's lift, projective": lift_proj,
              "chi_eta(T)": eta_order}
    primes = set()
    for v in orders.values():
        primes |= set(sp.factorint(v)) if v else {None}
    primes |= odd | even
    ch = {"rho'(T) has order 4": rho_order == 4,
          "g_T has projective order 4": gT == 4,
          "W28's lift has order 8 and projective order 4": (lift_order, lift_proj) == (8, 4),
          "chi_eta(T) has order 24": eta_order == 24,
          "B1601: odd trace over one prime of norm 3, even trace over 2": odd == {3} and odd_norm == {3}
                                                                          and even == {2},
          "every prime is 2 or 3; 5 occurs nowhere": primes <= {2, 3}}
    levels = sorted({v for v in (rho_order, gT, lift_proj) if v and v <= 5} | (odd | even))
    return {"checks": ch, "orders": orders, "common point primes": {"odd trace": sorted(odd),
                                                                    "even trace": sorted(even)},
            "primes": sorted(p for p in primes if p), "ladder levels in use": levels}, all(ch.values())


# ------------------------------------------------------------------ R
def R(l5):
    used = l5["ladder levels in use"]
    return {"R1, every finite rung at once": {"rungs": [2, 3, 4, 5], "top": RUNG[5]},
            "R2, invariance under every move": {"unimodular rungs": [5], "top": RUNG[5],
                                                "needs": "a lattice partition function in the joint action"},
            "R3, only the levels the forced structures use": {"rungs": used, "top": RUNG[max(used)]},
            "under every rule": "the step from the algebra to the loop's fields stays GENESIS FK11's"}


def main():
    out, ok = {}, {}
    for name, f in (("L1", L1), ("L2", L2), ("L3", L3), ("L4", L4), ("L5", L5)):
        out[name], ok[name] = f()
        print(name, "holds" if ok[name] else "FAILS")
        for k, v in out[name].get("checks", {}).items():
            print("   ", "ok  " if v else "FAIL", k)
        for N, row in out[name].get("rows", {}).items():
            for k, v in row["checks"].items():
                print("   ", "ok  " if v else "FAIL", f"N = {N}:", k)
    out["R"] = R(out["L5"])
    out["cells holding"] = ok
    out["verdict"] = ("every cell as predicted" if all(ok.values())
                      else "cells failed: " + ", ".join(k for k, v in ok.items() if not v))
    print("R:", json.dumps(out["R"], ensure_ascii=False))
    print("verdict:", out["verdict"])
    OUT.write_text(json.dumps(out, indent=1, ensure_ascii=False, default=str) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
