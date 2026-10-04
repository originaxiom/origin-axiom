#!/usr/bin/env python3
"""B1536 control K5 (population structure only, no cohomology): the covers and their cusps, two ways.
  - the number of covers of each degree <= 12 by low_index on sm:B1527's presentation and on SnapPy's presentation;
  - the multiset of (degree, number of cusps) through degree 8: cover_lib's orbits of <l, t'> against SnapPy's own covers of
    its own triangulation (M.covers(d), num_cusps).

    python3 control_k5.py [--record]   ->  k5.json"""
import json
import sys
import time
import warnings
from collections import Counter
from pathlib import Path

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import cover_lib as CL  # noqa: E402


def main():
    import low_index
    import snappy
    t0 = time.time()
    out = {}
    for name in ("m004", "m003"):
        st = CL.state(name)
        fam = CL.low_index_covers(st["G"], 12)
        by_fam = Counter(len(p["a"]) for p in fam)
        M = snappy.Manifold(name)
        G = M.fundamental_group()
        by_snap = Counter(len(h[0]) for h in low_index.permutation_reps(len(G.generators()), list(G.relators()), [], 12))
        mine = Counter((len(p["a"]), len(CL.cusps(st["G"], p))) for p in fam if len(p["a"]) <= 8)
        theirs = Counter()
        for d in range(1, 9):
            for Nc in M.covers(d):
                theirs[(d, Nc.num_cusps())] += 1
        out[name] = {"covers by degree (family presentation)": dict(sorted(by_fam.items())),
                     "covers by degree (SnapPy presentation)": dict(sorted(by_snap.items())),
                     "counts agree": by_fam == by_snap,
                     "(degree, cusps) through degree 8": {str(k): v for k, v in sorted(mine.items())},
                     "cusps agree with SnapPy's covers": mine == theirs}
    out["holds"] = all(v["counts agree"] and v["cusps agree with SnapPy's covers"] for v in out.values()
                       if isinstance(v, dict))
    out["seconds"] = round(time.time() - t0)
    print(json.dumps(out, indent=1))
    if "--record" in sys.argv:
        (HERE / "k5.json").write_text(json.dumps(out, indent=1) + "\n")
    return out


if __name__ == "__main__":
    main()
