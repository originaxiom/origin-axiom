#!/usr/bin/env python3
"""B1546 -- controls K1-K7, before the seal.  No count is read here except at classes whose counts are banked (sm:B1541's
generic classes of N45's interior and of tau's eigenspaces' interior parts, sm:B1544's three-cusp strata of K0).

  K1  structure, in both routes: Proposition L (prop_l.check: L0-L3), the dimensions (V_j^int, (K_-j)^int, Kc0, the image),
      the ten eigen-lines (one class each; cup ranks 1 for u_j, 2 for w_j, v_a, v_b; the entries of F they fill), the ten
      three-cusp strata K0(S) (one class each, support S), the cusp labels and the deck group on them.  The routes must agree
      and the values must be the sealed ones (STRUCTURE below, run.SUBSPACES).
  K2  the cochain formula for the cup map against the long exact sequence, h1(V) + h1(L) - h1(W) - 1, at a class of each kind
      (Z1, Z2, X:S=0,1,2, u1, w1, va) in both routes.
  K3  the positive controls, in both routes: a generic interior class (4, -10), a generic class of tau's zeta^0 interior part
      (-1, -10) and of its zeta^1 interior part (3, -10) (sm:B1541), and a generic class of K0({0, 1, 2}) (0, 0) (sm:B1544).
  K4  the read-out on synthetic rows (read_out.selftest).
  K5  the cusps: route F's and route R's coincide as point sets and their deck transformations are the same permutation.
  K6  Lemma F's ingredients at a generic class of H^1(N; rho), which reads the banked (5, -5), in both routes.
  K7  the draws: in each route, at three random vectors v of the image, the solution space of delta1_W(c) = v (x) phi is one
      class, of cup rank 1 and empty support; the sum of two has cup rank 2; a square plus a class of K0({0, 1, 2}) has cup
      rank 1 and support {0, 1, 2}.  (Structure only: no count.)

    python3 controls.py [--record]   ->  controls.json"""
import importlib.util
import json
import random
import sys
import time
import zlib
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load(name, path):
    """a module of this arc, by path under its own name (E12)"""
    if name not in sys.modules:
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[name] = mod
        spec.loader.exec_module(mod)
    return sys.modules[name]


LR = load("b1546_lowrank_lib", HERE / "lowrank_lib.py")
PL = load("b1546_prop_l", HERE / "prop_l.py")
RUN = load("b1546_run", HERE / "run.py")
FL = LR.FL
STRUCTURE = {
    "dim V_j^int": [2, 4, 4, 4, 4], "dim (K_-j)^int": [3, 3, 3, 3], "dim Kc0": 10, "Kc0 meets K0 in": 0, "image on Kc0": 4,
    "eigen-lines (classes, cup rank)": {**{f"u{j}": [1, 1] for j in range(1, 5)}, **{f"w{j}": [1, 2] for j in range(1, 5)},
                                        "va": [1, 2], "vb": [1, 2]},
    "entries of F filled by each eigen-line": {"va": [[1, 1], [4, 4]], "vb": [[2, 2], [3, 3]], "u1": [[3, 2]],
                                               "w1": [[2, 1], [4, 3]], "u2": [[1, 4]], "w2": [[3, 1], [4, 2]],
                                               "u3": [[4, 1]], "w3": [[1, 3], [2, 4]], "u4": [[2, 3]],
                                               "w4": [[1, 2], [3, 4]]},
    "K0(S) for the ten three-cusp sets (classes, support = S)": [1, True],
    "cusp labels": list(RUN.CUSPS), "tau on the cusps": dict(RUN.TAU),
    "Lemma M's input: the cup rank on the line's interior classes (n(1), at v_a, v_b, u_j, w_j and a generic class of "
    "V_0^int)": {"n(1)": 4, **{f"u{j}": 1 for j in range(1, 5)}, **{f"w{j}": 2 for j in range(1, 5)}, "va": 2, "vb": 2,
                 "generic V_0^int": 4},
}
BANKED = {"interior": [4, -10], "zeta^0 interior": [-1, -10], "zeta^1 interior": [3, -10], "K0(S=0,1,2)": [0, 0],
          "generic": [5, -5]}


def lemma_f_ok(x):
    lf, k = x["lemma F"], len(x["support"])
    m = lf["m"]
    return (lf["h0(dN;W*)"] == 2 * m and lf["h1(dN;W)"] == 4 * m - k and lf["r1(W)"] <= 3 * m - k
            and x["count"][0] == -1 + lf["h0(dN;W*)"] - lf["r1(W)"] and x["count"][0] >= k - m - 1)


def lemma_m_input(G):
    """the line's interior classes, and the rank of c u . on them at the eigen-lines and a generic class of V_0^int (the
    cup rank of each, if Lemma M's input holds)"""
    X = G.line_interior()
    nm = G.named()
    rng = random.Random(zlib.crc32(b"B1546|lemma M input"))
    c0 = G.combine(G.vint(0), [rng.randrange(1, G.p) for _ in range(G.n(G.vint(0)))])
    out = {"n(1)": G.n(X)}
    for x, v in nm.items():
        out[x] = G.rank(G.cupmat(G.col(v, 0), X))
    out["generic V_0^int"] = G.rank(G.cupmat(c0, X))
    return out


def structure(G):
    Cv = G.Cv
    res = PL.check(G, LR)
    nm = G.named()
    K = G.kappa0()
    sets = []
    for S in RUN.THREE_SETS:
        kap = G.reduce(Cv.stratum(set(S), G.K0))
        sets.append([G.n(kap), G.n(kap) == 1 and Cv.support(G.col(kap, 0)) == S])
    s = {"Proposition L holds": PL.holds(res),
         "dim V_j^int": res["dim V_j^int"], "dim (K_-j)^int": res["dim (K_-j)^int"],
         "dim Kc0": G.dim_mod(K), "Kc0 meets K0 in": G.meet(K, G.K0), "image on Kc0": int(G.image4().shape[1]),
         "eigen-lines (classes, cup rank)": {x: [G.n(v), G.cup_rank(G.col(v, 0))] for x, v in nm.items()},
         "entries of F filled by each eigen-line": {x: [list(e) for e in v] for x, v in res["L3: supports"].items()},
         "K0(S) for the ten three-cusp sets (classes, support = S)": [1, True] if all(a == 1 and b for a, b in sets) else sets,
         "Lemma M's input: the cup rank on the line's interior classes (n(1), at v_a, v_b, u_j, w_j and a generic class of "
         "V_0^int)": lemma_m_input(G),
         "cusp labels": sorted(Cv.labels), "tau on the cusps": {int(a): int(b) for a, b in FL.tau_on_cusps(Cv).items()}}
    return s, res


def main():
    t0 = time.time()
    rep = {}
    pF = FL.F().primes(1)[0]
    rep["prime (route F)"] = pF
    G = {"F": LR.Graded(FL.FCover("N45", pF)), "R": LR.Graded(FL.RCover("N45"))}
    rep["prime (route R)"] = G["R"].p
    # K1
    k1 = {}
    for route in ("F", "R"):
        s, res = structure(G[route])
        k1[route] = {"structure": s, "Proposition L (the checks)": res}
    exp = dict(STRUCTURE, **{"Proposition L holds": True})
    sF, sR = k1["F"]["structure"], k1["R"]["structure"]
    k1["holds"] = sF == sR == exp
    rep["K1"] = k1
    print("K1", k1["holds"], round(time.time() - t0, 1), "s", flush=True)
    # K2 and K7 (structure only)
    k2, k7 = {}, {}
    for route in ("F", "R"):
        g = G[route]
        rng = random.Random(zlib.crc32(f"B1546|K2|{route}".encode()))
        rows = []
        for sub in ("Z1", "Z2", "X:S=0,1,2", "u1", "w1", "va"):
            c = RUN.draw(g, sub, rng)
            rows.append([sub, g.Cv.rk_cup(c), g.Cv.rk_les(c)])
        k2[route] = rows
        rng = random.Random(zlib.crc32(f"B1546|K7|{route}".encode()))
        sq = [g.rank1(g.draw_v(rng)) for _ in range(3)]
        one = lambda c: c.reshape(-1, 1) if g.F else c.reshape(1, -1)  # noqa: E731
        kap = g.reduce(g.Cv.stratum({0, 1, 2}, g.K0))
        k7[route] = {"squares (cup rank, support)": [[g.cup_rank(c), g.Cv.support(c)] for c in sq],
                     "a sum of two (cup rank)": g.cup_rank(g.combine(g.stack(one(sq[0]), one(sq[1])), [1, 1])),
                     "a square plus K0(S=0,1,2) (cup rank, support)":
                         [g.cup_rank(g.combine(g.stack(one(sq[2]), kap), [1, 1])),
                          g.Cv.support(g.combine(g.stack(one(sq[2]), kap), [1, 1]))]}
    want2 = {"Z1": 1, "Z2": 2, "X:S=0,1,2": 1, "u1": 1, "w1": 2, "va": 2}
    rep["K2"] = {"readings (subspace, cochain rank, LES rank)": k2,
                 "holds": all(r[1] == r[2] == want2[r[0]] for rows in k2.values() for r in rows)}
    rep["K7"] = dict(k7, holds=all(v["squares (cup rank, support)"] == [[1, []]] * 3 and v["a sum of two (cup rank)"] == 2
                                   and v["a square plus K0(S=0,1,2) (cup rank, support)"] == [1, [0, 1, 2]]
                                   for v in k7.values()))
    print("K2", rep["K2"]["holds"], "K7", rep["K7"]["holds"], round(time.time() - t0, 1), "s", flush=True)
    # K3 and K6 (banked counts)
    k3, k6 = {}, {}
    for route in ("F", "R"):
        g = G[route]
        Cv = g.Cv
        rng = random.Random(zlib.crc32(f"B1546|K3|{route}".encode()))
        got = {}
        got["interior"] = Cv.reading(Cv.draw(Cv.Cint, rng))["count"]
        got["zeta^0 interior"] = Cv.reading(Cv.draw(g.vint(0), rng))["count"]
        got["zeta^1 interior"] = Cv.reading(Cv.draw(g.vint(1), rng))["count"]
        got["K0(S=0,1,2)"] = Cv.reading(Cv.draw(Cv.stratum({0, 1, 2}, g.K0), rng))["count"]
        k3[route] = got
        rng = random.Random(zlib.crc32(f"B1546|K6|{route}".encode()))
        x = Cv.reading(Cv.draw(Cv.Call if g.F else Cv.Cs, rng))
        k6[route] = {"count": x["count"], "support": x["support"], "lemma F": x["lemma F"],
                     "holds": lemma_f_ok(x) and x["support"] == sorted(Cv.labels) and x["count"] == BANKED["generic"]}
        print("K3/K6", route, got, k6[route]["holds"], round(time.time() - t0, 1), "s", flush=True)
    rep["K3"] = dict(k3, banked={k: v for k, v in BANKED.items() if k != "generic"},
                     holds=all(k3[r][k] == BANKED[k] for r in ("F", "R") for k in k3[r]))
    rep["K6"] = dict(k6, holds=all(v["holds"] for v in k6.values()))
    RO = load("b1546_read_out", HERE / "read_out.py")
    rep["K4"] = RO.selftest()
    fo = sorted(sorted(T["orbit"]) for T in G["F"].Cv.cov.cusps)
    ro = sorted(sorted(T["orbit"]) for T in G["R"].Cv.cov.cusp_list)
    rep["K5"] = {"cusps (orbit sizes)": sorted(len(o) for o in fo),
                 "holds": fo == ro and list(G["F"].Cv.tau) == list(G["R"].Cv.tau)}
    rep["all hold"] = all(rep[k]["holds"] for k in ("K1", "K2", "K3", "K4", "K5", "K6", "K7"))
    rep["seconds"] = round(time.time() - t0, 1)
    print(json.dumps({k: (v["holds"] if isinstance(v, dict) and "holds" in v else v) for k, v in rep.items()}), flush=True)
    if "--record" in sys.argv:
        (HERE / "controls.json").write_text(json.dumps(rep, indent=1, default=str) + "\n")
    return rep


if __name__ == "__main__":
    sys.exit(0 if main()["all hold"] else 1)
