#!/usr/bin/env python3
"""SM-C10, post hoc, written after the sealed run (relays/sm_c10/RUN.txt) and labelled as such.  The sealed population
(non-split abelian modules of character order <= 6) is empty on m000, m004 and m407.  Two extensions, same checks:
  PH1  m407 (n = 5) with characters of order dividing 22 (its H1 = Z/11 + Z).
  PH2  the common point's representation on every M_n: x -> i, y -> j (Q8 in SU(2)), t -> c g^n, g in SU(2) with
       g i g^-1 = rho(phi(x)) = ji and g j g^-1 = rho(phi(y)) = i; c a root of unity of order dividing 12.
       It is irreducible and unitary, so V* = V-bar; the untwisted gap compares V with V*, the twisted with V* (x) w.
    python3 posthoc_c10.py [out.json]"""
import sys, json, itertools, pathlib, math
from collections import Counter
from fractions import Fraction as Fr
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import run_c10 as C


def gaps_rows(G, n, mods, G2=None):
    w = {1: 1.0, 2: 1.0, 3: (-1.0 if n % 2 else 1.0)}
    rows = []
    for tag, V in mods:
        Vs = C.dual(V); Vsw = C.twist(Vs, w); Vw = C.twist(V, w)
        cV, cVs, cVsw, cVw = C.coh(G, V), C.coh(G, Vs), C.coh(G, Vsw), C.coh(G, Vw)
        k1, k2 = C.k12(cV, cVsw); p1 = C.k12(cV, cVs)
        r = {"module": tag, "h1": [cV["h1"], cVs["h1"], cVsw["h1"], cVw["h1"]], "h0b": cV["h0b"], "h1b": cV["h1b"],
             "A": [cV["A"], cVs["A"], cVsw["A"]], "K1": k1, "K2": k2, "P1_fails": not (p1[0] and p1[1]),
             "g_w": cVsw["h1"] - cV["h1"], "g_0": cVs["h1"] - cV["h1"]}
        if G2 is not None:
            V2 = {1: V[1], 2: V[2], 3: V[3] @ V[3]}
            r["K4"] = cV["h1"] + cVw["h1"] == C.coh(G2, V2)["h1"]
        rows.append(r)
    return rows


def summary(rows):
    return {"modules": len(rows), "K1": [sum(r["K1"] for r in rows), len(rows)], "K2": [sum(r["K2"] for r in rows), len(rows)],
            "K4": [sum(r.get("K4", False) for r in rows), sum("K4" in r for r in rows)],
            "P1_fails_on": [sum(r["P1_fails"] for r in rows), len(rows)],
            "g_w_ne_g_0": [sum(r["g_w"] != r["g_0"] for r in rows), len(rows)],
            "census_(g_0,g_w)": {str(k): v for k, v in Counter((r["g_0"], r["g_w"]) for r in rows).items()}}


def ph1():
    G = C.Group(5); G2 = C.Group(10)
    chars = set()
    for N in (11, 22):
        for th in itertools.product(range(N), repeat=3):
            if all(sum(int(G.E[i, k]) * th[k] for k in range(3)) % N == 0 for i in range(len(G.rels))):
                chars.add(tuple(Fr(a, N) for a in th))
    chars = sorted(chars); mods = []
    for a, b in itertools.permutations(chars, 2):
        V = C.module(G, a, b)
        if V is not None: mods.append(([str(x) for x in a] + ["|"] + [str(x) for x in b], V))
    return summary(gaps_rows(G, 5, mods, G2)), len(chars)


def common_point_g():
    I = np.array([[1j, 0], [0, -1j]]); J = np.array([[0, 1], [-1, 0]], dtype=complex)
    tgt = {1: J @ I, 2: I}                                   # rho(phi(x)) = rho(y) rho(x) = j i ; rho(phi(y)) = i
    src = {1: I, 2: J}
    # g src = tgt g  for both: linear in the 4 entries of g
    rows = []
    for k in (1, 2):
        for (p, q) in itertools.product(range(2), repeat=2):
            row = np.zeros(4, dtype=complex)
            for m in range(2):
                row[2 * p + m] += src[k][m, q]               # (g src)_{pq} = sum_m g_{pm} src_{mq}
                row[2 * m + q] -= tgt[k][p, m]               # (tgt g)_{pq} = sum_m tgt_{pm} g_{mq}
            rows.append(row)
    ns = C.null(np.array(rows))
    assert ns.shape[1] == 1, "g unique up to scale"
    g = ns[:, 0].reshape(2, 2); g = g / np.sqrt(np.linalg.det(g))
    return {1: I, 2: J}, g


def ph2():
    base, g = common_point_g()
    out = {}
    for n in range(1, 7):
        G = C.Group(n); G2 = C.Group(2 * n) if n % 2 else None
        gn = np.linalg.matrix_power(g, n); mods = []
        for N in range(1, 13):
            for e in range(N):
                if math.gcd(e, N) != 1 and not (N == 1 and e == 0): continue
                c = np.exp(2j * math.pi * e / N)
                V = {1: base[1], 2: base[2], 3: c * gn}
                ok = all(np.allclose(C.mat_of(V, r), np.eye(2), atol=1e-9) for r in G.rels)
                if ok: mods.append(("c = exp(2 pi i %d/%d)" % (e, N), V))
        out[n] = summary(gaps_rows(G, n, mods, G2))
    return out


def main():
    out_path = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "c10_posthoc.json"
    s1, nch = ph1()
    res = {"PH1_m407_orders_11_22": dict(s1, characters=nch), "PH2_common_point": ph2()}
    json.dump(res, open(out_path, "w"), indent=1)
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
