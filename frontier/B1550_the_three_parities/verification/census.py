#!/usr/bin/env python3
"""sm:B1550 -- the design-time structure census (no count): on the tetrahedral cover N of every state of the selection
(tetra_lib.STATES), every A4 orbit of characters of order dividing 4, its representative read in both routes at 50
digits (sm:B1549's read_P on N's presentation, read_S by Shapiro on M_3): h0, h1, r1, n of nu (x) rho with the gaps; the
order, m_A, the puncture pattern and label of every member of the orbit, the V4 orbits, the stabilizer. One JSON line per
orbit.

    python3 census.py PART NPARTS   ->  census_PART.jsonl beside this file
    python3 census.py collect NPARTS -> population.json (the member orbits, in the run's order; it reads the banked
                                        census_PART.jsonl.gz when the raw records are absent)"""
import json
import sys
import time

import tetra_lib as L

T = L.T
HERE = L.HERE
M_ORDER = L.M_ORDER


def orbit_rows(sw, take=lambda k: True):
    wl, C = L.tetra_cover(sw)
    s3 = L.level3(sw)
    for k, o in enumerate(L.a4_orbits(sw, C, M_ORDER)):
        if not take(k):
            continue
        t0 = time.time()
        orb = o["orbit"]
        c = orb[0]
        P = T.read_P(s3, C, c[0], c[1], M_ORDER)["structure"]
        S = T.read_S(s3, C, c[0], c[1], M_ORDER)["structure"]
        pats = {}
        for x in orb:
            pv, sup, lab = L.pattern(C, x[0], M_ORDER)
            pats[json.dumps(L.char_list(x))] = {"puncture values": pv, "support": len(sup),
                                                "label": list(lab) if lab else None,
                                                "m_A": len(C.trivial_cusps(x[0], x[1], M_ORDER))}
        row = {"state": sw, "level 3": s3, "wbar": wl, "orbit": [L.char_list(x) for x in orb], "size": len(orb),
               "stabilizer": 12 // len(orb), "golden-fixed": (12 // len(orb)) % 3 == 0,
               "v4 orbits": [[L.char_list(x) for x in v] for v in o["v4 orbits"]],
               "golden": {json.dumps(L.char_list(x)): L.char_list(y) for x, y in o["gold"].items()},
               "order": T.char_order(c, M_ORDER), "members": pats, "P": P, "S": S, "s": round(time.time() - t0, 1)}
        yield row


def run_part(part, nparts):
    out = open(HERE / f"census_{part}.jsonl", "w")
    for i, sw in enumerate(L.STATES):
        for row in orbit_rows(sw, lambda k: (k + i) % nparts == part):
            out.write(json.dumps(row) + "\n")
            out.flush()


def _lines(path):
    import gzip
    if path.exists():
        return path.read_text().splitlines()
    return gzip.open(str(path) + ".gz", "rt").read().splitlines()


def collect(nparts):
    rows = [json.loads(x) for p in range(nparts) for x in _lines(HERE / f"census_{p}.jsonl") if x.strip()]
    order = {sw: i for i, sw in enumerate(L.STATES)}
    rows.sort(key=lambda r: (order[r["state"]], r["orbit"]))
    struct = lambda r, k: (r[k]["h1"], r[k]["r1"], r[k]["n"])
    members = [r for r in rows if r["P"]["n"] > 0 or r["S"]["n"] > 0]
    out = {"states": [{"state": sw, "level 3": L.level3(sw), "wbar": L.tetra_cover(sw)[0]} for sw in L.STATES],
           "orbits read": len(rows), "routes agree on every orbit": all(struct(r, "P") == struct(r, "S") for r in rows),
           "member orbits": [{k: r[k] for k in ("state", "level 3", "wbar", "orbit", "size", "stabilizer", "golden-fixed",
                                                "v4 orbits", "golden", "order", "members", "P", "S")} for r in members],
           "members": sum(r["size"] for r in members)}
    (HERE / "population.json").write_text(json.dumps(out, indent=1) + "\n")
    return out


if __name__ == "__main__":
    if sys.argv[1] == "collect":
        o = collect(int(sys.argv[2]))
        print("orbits", o["orbits read"], "member orbits", len(o["member orbits"]), "members", o["members"],
              "routes agree", o["routes agree on every orbit"])
    else:
        run_part(int(sys.argv[1]), int(sys.argv[2]))
