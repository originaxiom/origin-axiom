#!/usr/bin/env python3
"""W6 of the weave (docs/THE_WEAVE.md): Theorem G (the lines carry alike), checked on every thread with members.

The weave's A4 = V4 x| <g> on an odd-trace thread's forced cover N (W3). A member's line is the non-zero parity p of the
edge it is supported on (a sign member), or of the one translation t_p that fixes it. The theorem: the line is constant
on V4 orbits; g carries line p to line g(p), a 3-cycle; so an orbit of members with lines has |O|/3 on each line, and on
the third level M_3 = N/V4 it gives one local system per line, cycled by the weave, each with the member's count.
For every member orbit of the census (the_lines_census.py's record) this checks the lines, their constancy on V4 orbits,
the golden map on the lines, and the members per line. Orbits fixed by all of V4 (orbit size 3) have no single line.

    python3 the_lines.py CENSUS.json   ->  the_lines.json beside this file"""
import json
import sys
from collections import Counter
from pathlib import Path

import the_lines_census as LC

L, T = LC.L, LC.T
HERE = Path(__file__).resolve().parent


def line_of(C, x, m):
    pv, sup, lab = L.pattern(C, x[0], m)
    if lab:
        return "edge", tuple(lab)
    dk = T.deck_action(C, x[0], x[1], m)
    st = [tuple(C.vecs[k]) for k in range(C.d) if dk[k] == x and tuple(C.vecs[k]) != (0, 0)]
    if len(st) == 1:
        return "fixed by", st[0]
    return "fixed by all of V4" if len(st) == 3 else "none", None


def check(sw, reps, m=4):
    wl, C = L.tetra_cover(sw)
    want = {tuple(r) for r in reps}
    out = []
    for o in L.a4_orbits(sw, C, m):
        if not want & {tuple(L.char_list(x)) for x in o["orbit"]}:
            continue
        lines = {x: line_of(C, x, m) for x in o["orbit"]}
        kinds = sorted({k for k, _ in lines.values()})
        row = {"size": len(o["orbit"]), "kind": kinds}
        if all(p is not None for _, p in lines.values()):
            gmap = {}
            for x in o["orbit"]:
                gmap.setdefault(lines[x][1], set()).add(lines[o["gold"][x]][1])
            row.update({
                "members per line": {str(list(k)): v for k, v in sorted(Counter(p for _, p in lines.values()).items())},
                "constant on V4 orbits": all(len({lines[x][1] for x in v}) == 1 for v in o["v4 orbits"]),
                "the golden map on lines": {str(list(k)): str([list(y) for y in sorted(v)]) for k, v in sorted(gmap.items())},
                "a well-defined 3-cycle": len(gmap) == 3 and all(len(v) == 1 and next(iter(v)) != k
                                                                  for k, v in gmap.items())})
        out.append(row)
    return out


def main(path):
    rows = [json.loads(x) for x in open(path) if x.strip()]
    res = {}
    for r in rows:
        reps = [mo["rep"] for mo in r["member orbits"]]
        tr = r.get("trace", (1 if r["state"][0] == "+" else -1) * LC.trace(r["state"][1:]))
        res[r["state"]] = {"trace": tr, "members": r["members"],
                           "member orbits": check(r["state"], reps) if reps else []}
    (HERE / "the_lines.json").write_text(json.dumps(res, indent=1) + "\n")
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main(sys.argv[1])
