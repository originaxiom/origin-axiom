#!/usr/bin/env python3
"""sm:B1551 -- the controls, run before the seal (and again, in part, by identity.py).

  K1  a third presentation: SnapPy's own spin cover (the unique degree-8 cover of s961 = M_3 with four cusps and H1 = Z^8),
      its presentation and polished holonomy (220 bits); the structure (h1, r1, n) of nu (x) rho at all 256 sign
      characters (sm:B1549's cohomology code at 50 digits) must have the same distribution as route P~'s census, and the
      line at the trivial character must read n = 4.
  K2  the routes on a cover whose answers are banked: the tetrahedral cover N rebuilt as the double cover of the
      fibre-direction double cover N_p (lattice (1, 0, 2)) of the third level cut out by its lattice parity. Its 64 sign
      characters in route P~ must have sm:B1550's census distribution, and a sign member must read sm:B1550's banked
      (-1, -1) in both routes, one draw.
  K3  the deck group of S over m004 on S's characters: order 24 with SL(2, F_3)'s element orders {1: 1, 2: 1, 3: 8,
      4: 6, 6: 8}.
  K4  the read-out on synthetic rows.
  K5  the room, exact: n(1) on S by sm:B1538's reader at the trivial character, two primes: (h1, r1, n) = (8, 4, 4);
      and n_N(1) + n_N(eps) = 0 + 4 on N (Shapiro).
  K6  Shapiro at every member orbit pulled back from N: (h1, r1, n) on S equals the sum of N's at nu and nu eps (sm:B1550's
      census), for the orbit's representative.

    python3 controls.py   ->  controls.json beside this file"""
import gzip
import json
import random
import time
from collections import Counter

import mpmath as mp

import read_out as RO
import spin_lib as S

T, PC, L = S.T, S.PC, S.L
HERE = S.HERE
B1550V = S.B1550V


def _b1550_census():
    rows = [json.loads(x) for p in range(3) for x in gzip.open(B1550V / f"census_{p}.jsonl.gz", "rt") if x.strip()]
    out = {}
    for r in rows:
        if r["state"] == "+LR":
            for ch in r["orbit"]:
                out[tuple(ch)] = (r["P"]["h1"], r["P"]["r1"], r["P"]["n"])
    return out


# ------------------------------------------------------------------------------------------------ K1: SnapPy's cover
def K1():
    import itertools
    import snappy
    M = snappy.Manifold("s961")
    hits = [X for X in M.covers(8) if X.num_cusps() == 4 and X.homology().betti_number() == 8]
    C = hits[0]
    G = C.fundamental_group()
    gens = G.generators()
    idx = {g: i for i, g in enumerate(gens)}

    def conv(w):
        return [(idx[c.lower()], 1 if c.islower() else -1) for c in w]
    P = T.Pres(len(gens), [conv(r) for r in G.relators()], [[conv(m), conv(l)] for (m, l) in G.peripheral_curves()])
    H = C.polished_holonomy(bits_prec=220)
    mp.mp.dps = 60

    def tompc(z):
        return mp.mpc(mp.mpf(str(z.real())), mp.mpf(str(z.imag())))
    four = []
    for g in gens:
        X = H.SL2C(g)
        four.append(T.to_list(T.four_mp(mp.matrix([[tompc(X[0, 0]), tompc(X[0, 1])], [tompc(X[1, 0]), tompc(X[1, 1])]]))))
    mp.mp.dps = T.DPS
    tab = Counter()
    for chi in itertools.product(range(2), repeat=len(gens)):
        A = [[[T.root(chi[j], 2) * x for x in row] for row in four[j]] for j in range(len(gens))]
        s = T.cohom(T.Mod(A), P)
        tab[str([s["h1"], s["r1"], s["n"]])] += 1
    line = T.cohom(T.Mod([[[mp.mpc(1)]] for _ in gens]), P)
    pop_tab = Counter()
    for x in (HERE / "census.jsonl").read_text().splitlines() if (HERE / "census.jsonl").exists() else \
            gzip.open(str(HERE / "census.jsonl") + ".gz", "rt").read().splitlines():
        if not x.strip():
            continue
        r = json.loads(x)
        if r["order"] <= 2:
            pop_tab[str([r["P"]["h1"], r["P"]["r1"], r["P"]["n"]])] += r["size"]
    holds = dict(tab) == dict(pop_tab) and line["n"] == 4 and sum(tab.values()) == 256
    return {"snappy cover": {"cusps": C.num_cusps(), "H1": str(C.homology()), "generators": len(gens),
                             "relators": len(G.relators())},
            "route X sign characters": dict(sorted(tab.items())), "route P~ census sign characters": dict(sorted(pop_tab.items())),
            "route X line at 1": [line["h1"], line["r1"], line["n"]], "holds": holds}


# ------------------------------------------------------------------------------------------------ K2: the rebuilt N
def K2():
    st3 = PC.State("+LRLRLR")
    Np = PC.Cover(st3, (1, 0, 2), 0)
    DC = S.DoubleCover(Np, "+LRLRLR", S.lattice_parity_character(Np))
    tab = Counter()
    members = []
    for c in DC.characters(2):
        s = T.read_P("+LRLRLR", DC, c, 0, 2)["structure"]
        tab[str([s["h1"], s["r1"], s["n"]])] += 1
        if s["n"] > 0:
            members.append(c)
    cen = _b1550_census()
    want = Counter(str(list(v)) for k, v in cen.items() if all(x % 2 == 0 for x in k))
    c = members[0]
    got = {}
    for route in ("P", "S"):
        rng = random.Random(f"B1551|K2|{route}")
        r = T.read_P("+LRLRLR", DC, c, 0, 2, [rng]) if route == "P" else S.read_SN(DC, c, 2, [rng])
        got[route] = r["draws"][0]["count"]
    holds = dict(tab) == dict(want) and got["P"] == got["S"] == [-1, -1] and len(DC.cusps) == 4
    return {"cusps": len(DC.cusps), "sign characters": dict(sorted(tab.items())), "sm:B1550's census": dict(sorted(want.items())),
            "a sign member's count": got, "holds": holds}


# ------------------------------------------------------------------------------------------------ K3: the deck group
def K3():
    import numpy as np
    SC = S.SpinCover()
    Pr, P = S.presentation_S(SC)
    chars = SC.characters(4)
    K = np.array([S.key(SC, Pr, c, 4) for c in chars], dtype=np.int64)
    idx = {tuple(r): i for i, r in enumerate(K)}
    perms = [tuple(idx[tuple(r)] for r in (K @ np.array(M, dtype=np.int64).T) % 4) for M in S.action_matrices(SC, Pr)]
    n = len(chars)
    ident = tuple(range(n))
    G, fr = {ident}, [ident]
    comp = lambda p, q: tuple(q[p[i]] for i in range(n))
    while fr:
        nx = []
        for g in fr:
            for h in perms:
                k = comp(g, h)
                if k not in G:
                    G.add(k)
                    nx.append(k)
        fr = nx

    def order(g):
        k, x = 1, g
        while x != ident:
            x = comp(x, g)
            k += 1
        return k
    prof = dict(sorted(Counter(order(g) for g in G).items()))
    return {"group order": len(G), "element orders": {str(k): v for k, v in prof.items()},
            "holds": len(G) == 24 and prof == {1: 1, 2: 1, 3: 8, 4: 6, 6: 8}}


# ------------------------------------------------------------------------------------------------ K4: the read-out
def K4():
    pop = {"member orbits": [
        {"orbit": [[1] * 24, [2] * 24], "size": 2, "order": 2, "m_A": 0, "pulled back": True,
         "P": {"h1": 2, "r1": 0, "n": 2}, "S": {"h1": 2, "r1": 0, "n": 2}},
        {"orbit": [[3] * 24], "size": 1, "order": 4, "m_A": 2, "pulled back": True,
         "P": {"h1": 3, "r1": 2, "n": 1}, "S": {"h1": 3, "r1": 2, "n": 1}},
        {"orbit": [[5] * 24], "size": 1, "order": 4, "m_A": 0, "pulled back": True,
         "P": {"h1": 4, "r1": 0, "n": 4}, "S": {"h1": 4, "r1": 0, "n": 4}}]}
    gap = [[0.01, 1e-50]] * 4

    def rows(fused=(-1, -1), o4=(-2, -1), o44=(1, 0)):
        out = []
        for orb, cnt in zip(pop["member orbits"], (fused, o4, o44)):
            nd = 3 if orb["P"]["n"] >= 2 else 1
            for ch in orb["orbit"]:
                for route in ("P", "S"):
                    reads = {k: {"h0": 0, "h1": 1, "r1": 0, "n": 1, "gaps": gap} for k in ("W1", "W1*", "L2", "L2*")}
                    out.append({"route": route, "character": ch, "m_A (this character)": orb["m_A"],
                                "structure": {"h0": 0, "h1": orb["P"]["h1"], "r1": orb["P"]["r1"], "n": orb["P"]["n"],
                                              "gaps": gap}, "interior dimension": orb["P"]["n"],
                                "draws": [{"count": list(cnt), "reads": reads} for _ in range(nd)]})
        return out
    ctl = {"all hold": True}
    cases = {}
    o, _ = RO.evaluate(rows(), pop, ctl, True)
    cases["the selection: PROVED, P6-P9 hold"] = o["verdict"] == "PROVED" and o["P9"]
    o, _ = RO.evaluate(rows(fused=(-2, -2)), pop, ctl, True)
    cases["two at a member trivial on no end breaks Lemma F': P4 false, OPEN"] = o["P4"] is False and o["verdict"] == "OPEN"
    o, _ = RO.evaluate(rows(o4=(-1, -1)), pop, ctl, True)
    cases["the order-4 type survives: P7, P9 false, NEGATIVE"] = (o["P7"] is False and o["P9"] is False and
                                                                  o["verdict"] == "NEGATIVE")
    o, _ = RO.evaluate(rows(fused=(-1, -2)), pop, ctl, True)
    cases["the fused type not shaped: P8, P9 false, NEGATIVE"] = (o["P8"] is False and o["verdict"] == "NEGATIVE")
    r = rows()
    r[0]["draws"][1]["count"] = [-2, -2]
    o, _ = RO.evaluate(r, pop, ctl, True)
    cases["draws disagree: P5 false, OPEN"] = o["P5"] is False and o["verdict"] == "OPEN"
    o, _ = RO.evaluate(rows()[:-1], pop, ctl, True)
    cases["a missing task: OPEN"] = o["complete"] is False and o["verdict"] == "OPEN"
    r = rows()
    r.append(dict(r[0]))
    o, _ = RO.evaluate(r, pop, ctl, True)
    cases["a duplicated task: OPEN"] = o["complete"] is False and o["verdict"] == "OPEN"
    r = rows()
    r[1]["draws"] = [{"count": [-2, -2], "reads": r[1]["draws"][0]["reads"]} for _ in range(3)]
    o, _ = RO.evaluate(r, pop, ctl, True)
    cases["routes disagree: P2 false, OPEN"] = o["P2"] is False and o["verdict"] == "OPEN"
    r = rows()
    for d in r[0]["draws"]:
        d["count"] = [-6, -1]
    o, _ = RO.evaluate(r, pop, ctl, True)
    cases["below the room's cap: P4 false, OPEN"] = o["P4"] is False and o["verdict"] == "OPEN"
    o, _ = RO.evaluate(rows(), pop, {"all hold": False}, True)
    cases["a control failed: P1 false, OPEN"] = o["P1"] is False and o["verdict"] == "OPEN"
    r = rows()
    r[0]["structure"]["gaps"] = [[1e-28, 1e-40]]
    o, _ = RO.evaluate(r, pop, ctl, True)
    cases["a murky gap: P4 false, OPEN"] = o["P4"] is False and o["verdict"] == "OPEN"
    return {"cases": cases, "holds": all(cases.values())}


# ------------------------------------------------------------------------------------------------ K5: the room
def K5():
    SC = S.SpinCover()
    Pr = T.RP.Presentation(SC)
    ez = tuple([0] * len(SC.edges))
    reads = [T.RP.read(Pr, ez, 0, 2, p) for p in (1000003, 998244353)]
    wl, N = L.tetra_cover("+LR")
    PrN = T.RP.Presentation(N)
    n1 = T.RP.read(PrN, tuple([0] * N.n), 0, 2, 1000003)
    neps = T.RP.read(PrN, S.EPS[:-1], S.EPS[-1], 2, 1000003)
    holds = reads[0] == reads[1] and (reads[0]["h1"], reads[0]["r1"], reads[0]["n"]) == (8, 4, 4) and \
        n1["n"] == 0 and neps["n"] == 4
    return {"S: (h1, r1, n) at 1": [reads[0]["h1"], reads[0]["r1"], reads[0]["n"]], "primes agree": reads[0] == reads[1],
            "N: n(1), n(eps)": [n1["n"], neps["n"]], "holds": holds}


# ------------------------------------------------------------------------------------------------ K6: Shapiro
def K6():
    SC = S.SpinCover()
    Pr, P = S.presentation_S(SC)
    pop = json.loads((HERE / "population.json").read_text())
    cen = _b1550_census()
    wl, N = L.tetra_cover("+LR")
    pull = {}
    for nu in cen:
        pull.setdefault(S.key(SC, Pr, SC.pullback((nu[:-1], nu[-1]), 4), 4), []).append(nu)
    rows, ok = [], True
    for orb in pop["member orbits"]:
        if not orb["pulled back"]:
            continue
        rep = tuple(orb["orbit"][0])
        pre = pull.get(S.key(SC, Pr, rep, 4))
        if not pre:
            rows.append({"rep": list(rep), "found": False})
            ok = False
            continue
        nu = pre[0]
        nue = tuple((a + b) % 4 for a, b in zip(nu, tuple(2 * x for x in S.EPS)))
        want = [x + y for x, y in zip(cen[nu], cen[nue])]
        got = [orb["P"]["h1"], orb["P"]["r1"], orb["P"]["n"]]
        rows.append({"rep": list(rep), "nu on N": list(nu), "nu eps": list(nue), "want": want, "got": got})
        ok = ok and want == got
    return {"orbits": rows, "holds": ok}


def main():
    t0 = time.time()
    out = {"K1": K1(), "K2": K2(), "K3": K3(), "K4": K4(), "K5": K5(), "K6": K6()}
    out["all hold"] = all(out[k]["holds"] for k in ("K1", "K2", "K3", "K4", "K5", "K6"))
    out["seconds"] = round(time.time() - t0, 1)
    (HERE / "controls.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps({k: (out[k]["holds"] if isinstance(out[k], dict) else out[k]) for k in out}, indent=1))


if __name__ == "__main__":
    main()
