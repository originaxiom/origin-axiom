#!/usr/bin/env python3
"""POST HOC (after E1's run, disclosed): P2 redone with words that are neither the reverse nor the mirror of each other.
    python3 posthoc_p2.py MAIN_CHECKOUT"""
import sys, json, pathlib
sys.argv = [sys.argv[0], sys.argv[1]]
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import run_e1 as E
def mirror(w): return E.rot_class(w.translate(str.maketrans("LR", "RL"))[::-1])
out = []
for a, b in [("LLRLRR", "LLLRLR"), ("LLRLRR", "LLRLLR"), ("LLLRLRR", "LLLLRLR"), ("LLRLRRR", "LLLRLLR")]:
    assert E.rot_class(b) not in (E.rot_class(a), E.rot_class(a[::-1]), mirror(a)), (a, b)
    for eps in (1, -1):
        Na, Sa, _ = E.level(eps, a, 1); Nb, Sb, _ = E.level(eps, b, 1)
        ca, cb = E.census(E.based(Sa, Na)), E.census(E.based(Sb, Nb))
        sa = sorted(str(v.c) for k, v in Sa.items() if k != (0, 0, 0)); sb = sorted(str(v.c) for k, v in Sb.items() if k != (0, 0, 0))
        out.append({"a": a, "b": b, "sign": eps, "N": [Na, Nb], "census_a": ca, "census_b": cb, "census_differs": ca != cb,
                    "slope_sets_differ": sa != sb})
        print(eps, a, b, "N", Na, Nb, "census differs", ca != cb, "slope sets differ", sa != sb)
json.dump(out, open(HERE / "posthoc_p2.json", "w"), indent=1)
