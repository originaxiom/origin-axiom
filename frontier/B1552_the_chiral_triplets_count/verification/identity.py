#!/usr/bin/env python3
"""sm:B1552 -- the banked identity, run after the seal and before the run.

  I1  sm:B1549's count path (three_lib.read_P with a generic interior class), at 50 digits, reproduces sm:B1530's banked
      count (-1, -1) at m135's two members, the fibre characters (0, 1/2) and (1/2, 0) at kappa = 6/12 in the library's
      convention.
  I2  the two routes give the same structure (h1, n), as a multiset over parities and kappa in mu_8, for module (a) on
      the first lift of two states of the population (+LR and -LR): structure only, no count.
  I3  the two routes give the same counts on the pre-seal controls (+LLRR at tick 1, both modules): outside the
      population.

    python3 identity.py   ->  identity.json beside this file
"""
import json
import random
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import chiral_lib as L  # noqa: E402

T, PC = L.T, L.PC


def i1():
    C = PC.Cover(PC.State("-LLRR"), (1, 0, 1), 0)
    out = []
    for ez in ((0, 6), (6, 0)):
        r = T.read_P("-LLRR", C, ez, 6, 12, rngs=[random.Random(1530)])
        out.append(list(r["draws"][0]["count"]))
    return {"counts": out, "held": out == [[-1, -1], [-1, -1]]}


def multiset(route, sw, k=3, variant="a"):
    m = Counter()
    if route == 1:
        st = L.route1_setup(sw, k)
        g = st["lifts"][0]
        for p in L.PARITIES:
            for e in range(L.M8):
                s = L.route1_structure(st, L.route1_module(st["Pr"], p, e, g, variant))
                if s["h1"]:
                    m[(s["h1"], s["n"])] += 1
    else:
        st = L.route2_setup(sw, k)
        g = st["lifts"][0]
        for p in L.PARITIES:
            for e in range(L.M8):
                s = L.route2_cohom(st, L.route2_module(p, e, g, variant))
                if s["h1"]:
                    m[(s["h1"], s["n"])] += 1
    return m


def i2():
    out = {}
    for sw in ("+LR", "-LR"):
        a, b = multiset(1, sw), multiset(2, sw)
        out[sw] = {"route 1": {str(k): v for k, v in a.items()}, "route 2": {str(k): v for k, v in b.items()},
                   "held": a == b}
    return out


def i3():
    out = {}
    s1, s2 = L.route1_setup("+LLRR", 1), L.route2_setup("+LLRR", 1)
    for variant in ("a", "b"):
        c1, c2 = [], []
        for p in L.PARITIES:
            for e in range(L.M8):
                A = L.route1_module(s1["Pr"], p, e, s1["lifts"][0], variant)
                if L.route1_structure(s1, A)["n"]:
                    c1.append(tuple(L.route1_count(s1, A, 1552)["count"]))
                mats = L.route2_module(p, e, s2["lifts"][0], variant)
                if L.route2_cohom(s2, mats)["n"]:
                    c2.append(tuple(L.route2_count(s2, mats, 1552)["count"]))
        out[variant] = {"route 1": sorted(c1), "route 2": sorted(c2), "held": sorted(c1) == sorted(c2)}
    return out


if __name__ == "__main__":
    res = {"I1": i1(), "I2": i2(), "I3": i3()}
    res["all held"] = bool(res["I1"]["held"] and all(v["held"] for v in res["I2"].values())
                           and all(v["held"] for v in res["I3"].values()))
    with open(HERE / "identity.json", "w") as f:
        json.dump(res, f, indent=1)
    print(json.dumps(res))
