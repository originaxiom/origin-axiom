#!/usr/bin/env python3
"""SM-R581, stage 1: freeze the fundamental-group presentations of the comparison class (card SM_R581, rule K).

The only step that needs the census package. It writes the presentations (generators, relators as words) to a JSON
file, so the decisive script (run.py) needs only the standard library, numpy, sympy and main's own
modules, and can run sandboxed.

  python3 extract_presentations.py population OUT.json   # rule K: orientable, one cusp, at most 6 ideal tetrahedra
  python3 extract_presentations.py smoke OUT.json        # outside K: 7 tetrahedra, four with 2 generators, four with 3

A presentation is a topological datum of the census triangulation; no measured value is read.
"""
import json
import sys


def main():
    mode, out = sys.argv[1], sys.argv[2]
    import snappy
    rows = []
    if mode not in ("population", "smoke"):
        raise SystemExit("mode is population or smoke")
    tets_list = range(1, 7) if mode == "population" else [7]
    taken = {2: 0, 3: 0}
    for k in tets_list:
        for M in snappy.OrientableCuspedCensus(cusps=1, tets=k):
            G = M.fundamental_group()
            ng = len(G.generators())
            if mode == "smoke":                     # four of each generator count, then stop
                if taken.get(ng, 4) >= 4:
                    if all(v >= 4 for v in taken.values()):
                        break
                    continue
                taken[ng] += 1
            rows.append(dict(name=M.name(), tets=int(M.num_tetrahedra()), cusps=int(M.num_cusps()),
                             gens=list(G.generators()), rels=list(G.relators())))
    meta = dict(mode=mode, rule="orientable, one cusp, ideal tetrahedra <= 6, census order" if mode == "population"
                else "smoke: outside the rule (7 tetrahedra)", census_package_version=snappy.__version__, n=len(rows))
    with open(out, "w") as f:
        json.dump(dict(meta=meta, rows=rows), f, indent=0, sort_keys=True)
    print("wrote %d presentations (%s)" % (len(rows), mode))


if __name__ == "__main__":
    main()
