"""W108: the binary icosahedral case of the record count, blind (main's P-205, relay of 2026-10-20; the owner's word,
2026-10-20). The rule, W108_RULE.md, was committed before this script (a67995a9b). One run.

Does a weave of three records have an SU(2) common point with image the binary icosahedral group 2I? For G = 2I and
the positive control Q8, at n = 2 and n = 3:
  - Epi(F_n, G), by the maximal subgroups, and |Epi| again by Hall's formula on the subgroup lattice;
  - the classes Epi/Aut(G) (K) and the characters, the trace functions through G in SU(2) (X);
  - the classes and characters fixed by every move, for main's full moves (the elementary Nielsen moves, the
    inversions, the transpositions), for the transvections alone, and at n = 2 for the record's <L, R>;
  - the orbits of the moves on the classes.

Run: python3 the_icosahedral_common_point.py -> the_icosahedral_common_point.json and _run.txt beside it.
"""
import itertools
import json
from pathlib import Path

import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components

HERE = Path(__file__).resolve().parent
OUT = HERE / "the_icosahedral_common_point.json"
RUN = HERE / "the_icosahedral_common_point_run.txt"
PHI = (1 + 5 ** 0.5) / 2
LINES = []


def say(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LINES.append(s)


def qmul(p, q):
    a1, b1, c1, d1 = p
    a2, b2, c2, d2 = q
    return (a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2, a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
            a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2, a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2)


def key(q):
    return tuple(round(x, 9) + 0.0 for x in q)


def quat_closure(gens, cap=1000):
    one = (1.0, 0.0, 0.0, 0.0)
    el = {key(one): one}
    fr = [one]
    while fr:
        nx = []
        for x in fr:
            for g in gens:
                y = qmul(x, g)
                k = key(y)
                if k not in el:
                    el[k] = y
                    nx.append(y)
        fr = nx
        if len(el) > cap:
            break
    return list(el.values())


class Group:
    def __init__(self, elems, name):
        self.name = name
        self.q = [tuple(x) for x in elems]
        self.N = N = len(elems)
        idx = {key(x): i for i, x in enumerate(self.q)}
        self.mul = np.array([[idx[key(qmul(self.q[i], self.q[j]))] for j in range(N)] for i in range(N)], dtype=np.int64)
        self.inv = np.array([idx[key((x[0], -x[1], -x[2], -x[3]))] for x in self.q], dtype=np.int64)
        self.e = idx[key((1.0, 0.0, 0.0, 0.0))]
        self.m1 = idx[key((-1.0, 0.0, 0.0, 0.0))]
        self.tr = np.array([2 * x[0] for x in self.q])
        self.order = np.array([self._order(i) for i in range(N)])

    def _order(self, i):
        k, x = 1, i
        while x != self.e:
            x = self.mul[x, i]
            k += 1
        return k

    def gen(self, gens):
        s = {self.e}
        fr = [self.e]
        while fr:
            nx = []
            for x in fr:
                for g in gens:
                    y = int(self.mul[x, g])
                    if y not in s:
                        s.add(y)
                        nx.append(y)
            fr = nx
        return frozenset(s)


def subgroups(G):
    subs = {frozenset([G.e])}
    for i in range(G.N):
        for j in range(i, G.N):
            subs.add(G.gen([i, j]))
    return sorted(subs, key=len)


def mobius(G, subs):
    full = frozenset(range(G.N))
    mu = {full: 1}
    for H in sorted(subs, key=len, reverse=True):
        if H == full:
            continue
        mu[H] = -sum(mu[K] for K in mu if len(K) > len(H) and H < K)
    return mu


def automorphisms(G, s, t):
    """every automorphism, as the map of the generating pair (s, t) to pairs with the same orders of s, t and st that
    generate G; each map is checked to be a homomorphism"""
    os_, ot, ost = G.order[s], G.order[t], G.order[G.mul[s, t]]
    maps = []
    for s2 in np.where(G.order == os_)[0]:
        for t2 in np.where(G.order == ot)[0]:
            if G.order[G.mul[s2, t2]] != ost or len(G.gen([s2, t2])) != G.N:
                continue
            m = -np.ones(G.N, dtype=np.int64)
            m[G.e] = G.e
            fr = [G.e]
            ok = True
            while fr and ok:
                nx = []
                for x in fr:
                    for g, g2 in ((s, s2), (t, t2)):
                        y, y2 = G.mul[x, g], G.mul[m[x], g2]
                        if m[y] < 0:
                            m[y] = y2
                            nx.append(y)
                        elif m[y] != y2:
                            ok = False
                fr = nx
            if ok and (m >= 0).all() and (m[G.mul] == G.mul[m[:, None], m[None, :]]).all():
                maps.append(m)
    return np.array(maps)


def inner(G):
    maps = {tuple(G.mul[G.mul[g, :], G.inv[g]]) for g in range(G.N)}
    return np.array(sorted(maps))


def epis(G, maxsubs, n):
    mask = np.zeros(G.N, dtype=np.int64)
    for b, M in enumerate(maxsubs):
        for x in M:
            mask[x] |= 1 << b
    if n == 2:
        a, b = np.nonzero((mask[:, None] & mask[None, :]) == 0)
        return np.stack([a, b], axis=1)
    out = []
    for g1 in range(G.N):
        b, c = np.nonzero((mask[g1] & mask[:, None] & mask[None, :]) == 0)
        out.append(np.stack([np.full(len(b), g1), b, c], axis=1))
    return np.concatenate(out)


def encode(G, T):
    code = np.zeros(len(T), dtype=np.int64)
    for k in range(T.shape[1]):
        code = code * G.N + T[:, k]
    return code


def decode(G, codes, n):
    T = np.zeros((len(codes), n), dtype=np.int64)
    c = codes.copy()
    for k in range(n - 1, -1, -1):
        T[:, k] = c % G.N
        c //= G.N
    return T


def canon(G, T, maps):
    best = None
    for m in maps:
        c = encode(G, m[T])
        best = c if best is None else np.minimum(best, c)
    return best


def moves(G, n, kind):
    """the move set as functions on tuple arrays"""
    out = []
    pairs = [(i, j) for i in range(n) for j in range(n) if i != j]
    for i, j in pairs:
        for e in (1, -1):
            def right(T, i=i, j=j, e=e):
                U = T.copy()
                U[:, i] = G.mul[T[:, i], T[:, j] if e == 1 else G.inv[T[:, j]]]
                return U

            def left(T, i=i, j=j, e=e):
                U = T.copy()
                U[:, i] = G.mul[T[:, j] if e == 1 else G.inv[T[:, j]], T[:, i]]
                return U
            out += [(f"a{i}->a{i}a{j}^{e}", right), (f"a{i}->a{j}^{e}a{i}", left)]
    if kind == "full":
        for i in range(n):
            def invert(T, i=i):
                U = T.copy()
                U[:, i] = G.inv[T[:, i]]
                return U
            out.append((f"a{i}->a{i}^-1", invert))
        for i, j in itertools.combinations(range(n), 2):
            def swap(T, i=i, j=j):
                U = T.copy()
                U[:, [i, j]] = T[:, [j, i]]
                return U
            out.append((f"swap a{i} a{j}", swap))
    if kind == "LR":
        def L(T):
            U = T.copy()
            U[:, 1] = G.mul[T[:, 0], T[:, 1]]
            return U

        def R(T):
            U = T.copy()
            U[:, 0] = G.mul[T[:, 0], T[:, 1]]
            return U
        out = [("L", L), ("R", R)]
    return out


def traces(G, T):
    n = T.shape[1]
    words = [(k,) for k in range(n)] + [c for r in range(2, n + 1) for c in itertools.combinations(range(n), r)]
    cols = []
    for w in words:
        x = T[:, w[0]]
        for k in w[1:]:
            x = G.mul[x, T[:, k]]
        cols.append(G.tr[x])
    return np.round(np.stack(cols, axis=1), 7)


def study(G, maxsubs, mu, auts, inns, n, kinds):
    E = epis(G, maxsubs, n)
    hall = int(round(sum(m * len(H) ** n for H, m in mu.items())))
    cK = canon(G, E, auts)
    repsK = np.unique(cK)
    free_aut = len(repsK) * len(auts) == len(E)
    cX = canon(G, E, inns)
    repsX = np.unique(cX)
    free_inn = len(repsX) * len(inns) == len(E)
    TX = decode(G, repsX, n)
    trX = traces(G, TX)
    chars_distinct = len(np.unique(trX, axis=0))
    res = {"|Epi|": int(len(E)), "Hall's formula": hall, "classes (K)": int(len(repsK)),
           "Aut acts freely": bool(free_aut), "Inn classes": int(len(repsX)), "Inn acts freely": bool(free_inn),
           "distinct characters (X)": int(chars_distinct)}
    TK = decode(G, repsK, n)
    for kind in kinds:
        mv = moves(G, n, kind)
        fixedK = np.ones(len(repsK), dtype=bool)
        rows, cols = [], []
        for name, f in mv:
            img = canon(G, f(TK), auts)
            pos = np.searchsorted(repsK, img)
            fixedK &= pos == np.arange(len(repsK))
            rows.append(np.arange(len(repsK)))
            cols.append(pos)
        A = coo_matrix((np.ones(sum(len(r) for r in rows)), (np.concatenate(rows), np.concatenate(cols))),
                       shape=(len(repsK), len(repsK)))
        ncomp, lab = connected_components(A, directed=True, connection="weak")
        sizes = sorted(np.bincount(lab).tolist(), reverse=True)
        fixedX = np.ones(len(repsX), dtype=bool)
        for name, f in mv:
            fixedX &= np.all(np.abs(traces(G, f(TX)) - trX) < 1e-6, axis=1)
        res[kind] = {"moves": len(mv), "classes fixed by every move (K)": int(fixedK.sum()),
                     "characters fixed by every move (X)": int(fixedX.sum()),
                     "orbits on the classes": int(ncomp), "orbit sizes (largest ten)": sizes[:10],
                     "fixed classes": [TK[i].tolist() for i in np.where(fixedK)[0][:5]],
                     "fixed characters' traces": [trX[i].tolist() for i in np.where(fixedX)[0][:5]]}
    return res


def main():
    out = {"status": "one run", "rule": "W108_RULE.md (a67995a9b)", "cells": {}}
    i_, w_ = (0.0, 1.0, 0.0, 0.0), (0.5, 0.5, 0.5, 0.5)
    u_ = (PHI / 2, 1 / (2 * PHI), 0.5, 0.0)
    elems = quat_closure([i_, w_, u_])
    if len(elems) != 120:
        out["A0"] = {"2I closure size": len(elems)}
        out["cells"]["A0"] = False
        say("A0 failed: the closure has", len(elems), "elements; the arc stops at A0")
        OUT.write_text(json.dumps(out, indent=1, default=str), encoding="utf-8")
        RUN.write_text("\n".join(LINES) + "\n", encoding="utf-8")
        return
    G = Group(elems, "2I")
    Q = Group(quat_closure([i_, (0.0, 0.0, 1.0, 0.0)]), "Q8")
    a0 = {}
    for H in (G, Q):
        subs = subgroups(H)
        full = frozenset(range(H.N))
        proper = [S for S in subs if S != full]
        maxs = [S for S in proper if not any(S < K for K in proper)]
        mu = mobius(H, subs)
        want = (4, 6, 10) if H.name == "2I" else (4, 4, 4)
        s, t = next((x, y) for x in range(H.N) for y in range(H.N)
                    if (H.order[x], H.order[y], H.order[H.mul[x, y]]) == want and len(H.gen([x, y])) == H.N)
        auts, inns = automorphisms(H, s, t), inner(H)
        centre = [x for x in range(H.N) if all(H.mul[x, y] == H.mul[y, x] for y in range(H.N))]
        a0[H.name] = {"order": H.N, "centre": len(centre), "subgroups": len(subs),
                      "maximal subgroups by order": sorted(len(S) for S in maxs), "|Aut|": len(auts),
                      "|Inn|": len(inns)}
        H.maxs, H.mu, H.auts, H.inns = maxs, mu, auts, inns
    say("A0", json.dumps(a0))
    ok2I = (a0["2I"]["order"] == 120 and a0["2I"]["centre"] == 2 and a0["2I"]["|Aut|"] == 120
            and a0["2I"]["|Inn|"] == 60 and a0["2I"]["maximal subgroups by order"] == [12] * 10 + [20] * 6 + [24] * 5)
    okQ = a0["Q8"]["order"] == 8 and a0["Q8"]["|Aut|"] == 24
    out["A0"] = a0
    res = {}
    for H in (Q, G):
        for n in (2, 3):
            kinds = ("full", "trans", "LR") if n == 2 else ("full", "trans")
            res[f"{H.name}, n = {n}"] = r = study(H, H.maxs, H.mu, H.auts, H.inns, n, kinds)
            say(f"{H.name}, n = {n}", json.dumps(r))
    out["results"] = res
    q2, q3 = res["Q8, n = 2"], res["Q8, n = 3"]
    i2, i3 = res["2I, n = 2"], res["2I, n = 3"]
    free = all(r["Aut acts freely"] and r["Inn acts freely"] for r in res.values())
    out["cells"]["A0"] = bool(ok2I and okQ and free and q2["|Epi|"] == 24 and q2["classes (K)"] == 1
                              and q3["|Epi|"] == 336 and q3["classes (K)"] == 14)
    out["cells"]["H"] = all(r["|Epi|"] == r["Hall's formula"] for r in res.values())
    out["cells"]["P"] = all(q2[k]["classes fixed by every move (K)"] == 1 and q2[k]["characters fixed by every move (X)"] >= 1
                            for k in ("full", "LR"))
    out["cells"]["N2"] = all(i2[k]["classes fixed by every move (K)"] == 0 and i2[k]["characters fixed by every move (X)"] == 0
                             for k in ("full", "LR"))
    out["cells"]["C1-K"] = i3["full"]["classes fixed by every move (K)"] == 0
    out["cells"]["C1-X"] = i3["full"]["characters fixed by every move (X)"] == 0
    out["cells"]["C1-T"] = (i3["trans"]["classes fixed by every move (K)"] == 0
                            and i3["trans"]["characters fixed by every move (X)"] == 0)
    out["cells"]["C1-Q"] = q3["full"]["classes fixed by every move (K)"] == 0
    out["cells"]["O-full"] = i3["full"]["orbits on the classes"] == 1
    out["cells"]["O-T"] = i3["trans"]["orbits on the classes"] == 1
    say("cells", json.dumps(out["cells"]))
    OUT.write_text(json.dumps(out, indent=1, default=str), encoding="utf-8")
    RUN.write_text("\n".join(LINES) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
