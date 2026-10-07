#!/usr/bin/env python3
"""sm:B1552 -- the sealed run. One line per reading, written as it is computed; nothing is read back here.

    python3 run.py ROUTE STATE ...   ->  appends JSON lines to run_ROUTE.jsonl beside this file

A reading is (state, module, lift index, parity, kappa in mu_8 where the module's n > 0, draw seed). Route 1 is the
tick's route-P presentation with sm:B1549's banked cohomology at 50 digits; route 2 is the deck-compatible presentation
with this arc's numpy Fox calculus (chiral_lib.py)."""
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import chiral_lib as L  # noqa: E402

SEEDS = (1552, 2552)
MODULES = ("a", "b")


def readings(route, sw):
    if route == "1":
        st = L.route1_setup(sw)
        lifts = st["lifts"]
        for li, g in enumerate(lifts):
            for mod in MODULES:
                for p in L.PARITIES:
                    for e in range(L.M8):
                        A = L.route1_module(st["Pr"], p, e, g, mod)
                        s = L.route1_structure(st, A)
                        if s["n"] == 0:
                            continue
                        for seed in SEEDS:
                            t0 = time.time()
                            c = L.route1_count(st, A, seed)
                            yield {"route": 1, "state": sw, "module": mod, "lift": li, "parity": L.NAMES[p],
                                   "kappa (eighths)": e, "structure": s, "seed": seed, "count": c["count"],
                                   "reads": c["reads"], "s": round(time.time() - t0, 1)}
    else:
        st = L.route2_setup(sw)
        for li, g in enumerate(st["lifts"]):
            for mod in MODULES:
                for p in L.PARITIES:
                    for e in range(L.M8):
                        mats = L.route2_module(p, e, g, mod)
                        s = L.route2_cohom(st, mats)
                        if s["n"] == 0:
                            continue
                        for seed in SEEDS:
                            t0 = time.time()
                            c = L.route2_count(st, mats, seed)
                            yield {"route": 2, "state": sw, "module": mod, "lift": li, "parity": L.NAMES[p],
                                   "kappa (eighths)": e,
                                   "structure": {k: s[k] for k in ("h0", "h1", "r1", "n")},
                                   "seed": seed, "count": c["count"], "reads": c["reads"],
                                   "worst gap": c["worst gap"], "s": round(time.time() - t0, 1)}


if __name__ == "__main__":
    route, states = sys.argv[1], sys.argv[2:]
    out = HERE / f"run_{route}.jsonl"
    with open(out, "a") as f:
        for sw in states:
            for r in readings(route, sw):
                f.write(json.dumps(r) + "\n")
                f.flush()
            f.write(json.dumps({"route": int(route), "state": sw, "done": True}) + "\n")
            f.flush()
