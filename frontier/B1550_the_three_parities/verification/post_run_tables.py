#!/usr/bin/env python3
"""sm:B1550 -- the post-run table, written after the read-out and named as such (it seals nothing): the parity label of
every generation-shaped member of the root's tetrahedral cover. A sign member's label is its edge (the read-out's label);
an order-4 member's is the parity p of the translation t_p that fixes it (its stabilizer in V4), so it descends to the
double cover N/<t_p> of the third level. For each kind: the members per label, and the golden map on the labels.

    python3 post_run_tables.py   ->  post_run_tables.json beside this file"""
import gzip
import json
from collections import Counter

import tetra_lib as L

T = L.T
HERE = L.HERE


def main():
    ro = json.loads((HERE / "read_out.json").read_text())
    pop = json.loads((HERE / "population.json").read_text())
    wl, C = L.tetra_cover("+LR")
    gs = [(sw, tuple(ch), g, lab, order) for sw, ch, g, lab, order in ro["generation-shaped members"]]
    orbit_of = {}
    for o in pop["member orbits"]:
        for ch in o["orbit"]:
            orbit_of[(o["state"], tuple(ch))] = o

    def label(ch, order):
        if order == 2:
            return tuple(orbit_of[("+LR", ch)]["members"][json.dumps(list(ch))]["label"])
        ez, es = tuple(ch[:-1]), ch[-1]
        dk = T.deck_action(C, ez, es, 4)
        st = [C.vecs[x] for x in range(C.d) if dk[x] == (ez, es) and C.vecs[x] != (0, 0)]
        assert len(st) == 1, (ch, st)
        return tuple(st[0])
    out = {}
    for order in (2, 4):
        mem = [ch for sw, ch, g, lab, o in gs if sw == "+LR" and o == order]
        labs = {ch: label(ch, order) for ch in mem}
        gmap = {}
        for ch in mem:
            img = tuple(orbit_of[("+LR", ch)]["golden"][json.dumps(list(ch))])
            gmap.setdefault(labs[ch], set()).add(labs[img])
        out[f"order {order}"] = {"generation-shaped members": len(mem),
                                 "per label": {str(list(k)): v for k, v in sorted(Counter(labs.values()).items())},
                                 "the golden map on the labels": {str(list(k)): [list(x) for x in sorted(v)]
                                                                  for k, v in sorted(gmap.items())},
                                 "counts": sorted({str(g) for sw, ch, g, lab, o in gs if sw == "+LR" and o == order})}
    allabs = Counter()
    for order in (2, 4):
        for k, v in out[f"order {order}"]["per label"].items():
            allabs[k] += v
    out["all generation-shaped members of the root's cover, per label"] = dict(sorted(allabs.items()))
    (HERE / "post_run_tables.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
