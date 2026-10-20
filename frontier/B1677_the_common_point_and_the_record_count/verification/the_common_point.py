#!/usr/bin/env python3
"""THE COMMON POINT AND THE COUNT OF RECORDS (P-201, P-205). Does a weave of n records have an SU(2) common point
only at n = 2?

A common point of the weave of n records: a character of the free group F_n in SU(2), with finite non-abelian image,
fixed by every move a_i -> a_i a_j and a_i -> a_j a_i (i != j). These transvections generate SAut(F_n), so such a
character is fixed by the whole special automorphism group.

The census. For each finite non-abelian subgroup G of SU(2) (binary dihedral Dic_m for m = 2..15, 2T, 2O, 2I), as unit
quaternions: every n-tuple generating G that passes the exact necessary filter (all tr a_i equal, all tr a_i a_j equal
to it; derived from the moves a_i -> a_i a_j) is tested against every move by comparing characters through the trace
coordinates of all words of length <= 3 in the generators (Fricke-Vogt: these determine an SL(2, C) character of F_n).
Every generator runs over every element of G with the common trace (no reduction by conjugation, which may leave G).

Cells (sealed): C0 (n = 2) the quaternion character is a common point, and every common point found is listed;
C1 (n = 3) and C2 (n = 4) no common point for any G; the bite: if any is found, its G, generators and traces are printed.
Writes the_common_point.json."""
import itertools, json, pathlib, sys, time
import numpy as np

def qmul(p, q):
    a1, b1, c1, d1 = p; a2, b2, c2, d2 = q
    return (a1*a2 - b1*b2 - c1*c2 - d1*d2, a1*b2 + b1*a2 + c1*d2 - d1*c2,
            a1*c2 - b1*d2 + c1*a2 + d1*b2, a1*d2 + b1*c2 - c1*b2 + d1*a2)

def key(q, nd=9): return tuple(round(x + 0.0, nd) + 0.0 for x in q)

def close(gens, cap=500):
    G = {key((1.0, 0.0, 0.0, 0.0)): (1.0, 0.0, 0.0, 0.0)}; frontier = [(1.0, 0.0, 0.0, 0.0)]
    while frontier and len(G) <= cap:
        x = frontier.pop()
        for g in gens:
            y = qmul(x, g); k = key(y)
            if k not in G: G[k] = y; frontier.append(y)
    return list(G.values())

def groups():
    out = {}
    for m in range(2, 16):                                                   # Dic_m: <e^{i pi/m}, j>, order 4m
        out[f"Dic{m}"] = close([(np.cos(np.pi / m), np.sin(np.pi / m), 0.0, 0.0), (0.0, 0.0, 1.0, 0.0)])
    h = 0.5
    T = close([(h, h, h, h), (0.0, 1.0, 0.0, 0.0)]); out["2T"] = T
    s = 1 / np.sqrt(2); out["2O"] = close([(h, h, h, h), (s, s, 0.0, 0.0)])
    ph = (1 + 5 ** 0.5) / 2; out["2I"] = close([(h, h, h, h), (0.0, 0.5, ph / 2, 1 / (2 * ph))])
    return out

ORDERS = {**{f"Dic{m}": 4 * m for m in range(2, 16)}, "2T": 24, "2O": 48, "2I": 120}

def tr(q): return 2 * q[0]

def words(n):                                                                 # index tuples of length 1..3, increasing
    W = [(i,) for i in range(n)] + [(i, j) for i in range(n) for j in range(i + 1, n)]
    W += [(i, j, k) for i in range(n) for j in range(i + 1, n) for k in range(j + 1, n)]
    return W

def signature(tup, W):
    out = []
    for w in W:
        x = (1.0, 0.0, 0.0, 0.0)
        for i in w: x = qmul(x, tup[i])
        out.append(round(tr(x), 7) + 0.0)
    return tuple(out)

def moves(n):
    for i in range(n):
        for j in range(n):
            if i != j: yield ("R", i, j); yield ("L", i, j)

def apply(tup, mv):
    side, i, j = mv; t = list(tup)
    t[i] = qmul(tup[i], tup[j]) if side == "R" else qmul(tup[j], tup[i])
    return tuple(t)

def common_points(G, n):
    W = words(n); found = []; tested = 0; seen = set()
    traces = sorted({round(tr(g), 7) for g in G})
    for t0 in traces:
        if abs(abs(t0) - 2) < 1e-9: continue                                  # +-1: central, abelian
        cands = [g for g in G if abs(tr(g) - t0) < 1e-7]
        for a1, *rest in itertools.product(cands, repeat=n):                  # every first generator (no reduction:
            rest = tuple(rest)                                                # conjugation may leave G)
            tup = (a1,) + rest
            if any(abs(tr(qmul(tup[i], tup[j])) - t0) > 1e-7 for i in range(n) for j in range(i + 1, n)): continue
            if len(close(list(tup), cap=ORDERS_CUR[0] + 1)) != ORDERS_CUR[0]: continue   # must generate G
            tested += 1
            sig = signature(tup, W)
            if all(signature(apply(tup, mv), W) == sig for mv in moves(n)):
                if sig not in seen:
                    seen.add(sig)
                    found.append({"traces": [float(x) for x in sig], "generators": [[round(float(x), 6) for x in q] for q in tup],
                                  "generating tuples with this character": 0})
                next(f for f in found if tuple(f["traces"]) == tuple(float(x) for x in sig))["generating tuples with this character"] += 1
    return found, tested

ORDERS_CUR = [0]
def main():
    t0 = time.time(); out = {"groups": {}, "cells": {}}
    G = groups()
    assert all(len(G[k]) == ORDERS[k] for k in G), {k: len(G[k]) for k in G}
    for n in (2, 3, 4):
        for name, grp in G.items():
            ORDERS_CUR[0] = ORDERS[name]
            found, tested = common_points(grp, n)
            out["groups"][f"n={n} {name}"] = {"tuples passing the filter and generating": tested, "common points": found}
            print(f"n={n} {name:6s} order {ORDERS[name]:3d}: filtered generating tuples {tested:7d}; distinct common characters {len(found)}", flush=True)
    q8 = [v for k, v in out["groups"].items() if k == "n=2 Dic2"][0]["common points"]
    out["cells"]["C0 the quaternion character is a common point at n = 2"] = any(all(abs(x) < 1e-6 for x in cp["traces"]) for cp in q8)
    out["cells"]["C1 no common point at n = 3"] = all(not v["common points"] for k, v in out["groups"].items() if k.startswith("n=3"))
    out["cells"]["C2 no common point at n = 4"] = all(not v["common points"] for k, v in out["groups"].items() if k.startswith("n=4"))
    out["seconds"] = round(time.time() - t0, 1)
    json.dump(out, open(pathlib.Path(__file__).with_name("the_common_point.json"), "w"), indent=1)
    print("cells:", out["cells"])

if __name__ == "__main__":
    main()
