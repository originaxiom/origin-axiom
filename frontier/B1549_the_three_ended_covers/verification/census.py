#!/usr/bin/env python3
"""sm:B1549 -- the design-time structure census (no count): on every three-ended cover of the 27 states (three_lib's
three_covers: 13 covers of 10 states), every deck orbit of characters of order dividing 4, read in both routes at 50 digits:
h0, h1, r1, n of nu (x) rho with the gaps; the order, m_A (ends where nu is trivial), the orbit. At every orbit with an
interior class in either route, the flavor group of Ind chi (exact). One JSON line per orbit.

    python3 census.py PART NPARTS   ->  census_PART.jsonl beside this file
    python3 census.py collect NPARTS -> population.json (the members, by cover, in the run's order; it reads the banked
                                        census_PART.jsonl.gz when the raw records are absent)"""
import json
import sys
import time

import three_lib as T

HERE = T.HERE
M_ORDER = 4


def run_part(part, nparts):
    covers = T.three_covers()
    out = open(HERE / f"census_{part}.jsonl", "w")
    for k, (sw, d, lat, wl) in enumerate(covers):
        if k % nparts != part:
            continue
        C = T.PC.Cover(T.PC.State(sw), lat, wl)
        for orb in T.orbits(C, M_ORDER):
            t0 = time.time()
            c = orb[0]
            P = T.read_P(sw, C, c[0], c[1], M_ORDER)["structure"]
            S = T.read_S(sw, C, c[0], c[1], M_ORDER)["structure"]
            row = {"state": sw, "ends of companion": d, "lattice": list(lat), "wbar": wl,
                   "orbit": [list(o[0]) + [o[1]] for o in orb], "size": len(orb), "order": T.char_order(c, M_ORDER),
                   "m_A": len(C.trivial_cusps(c[0], c[1], M_ORDER)), "P": P, "S": S}
            if P["n"] > 0 or S["n"] > 0:
                row["flavor group"] = T.flavor_group(C, c[0], c[1], M_ORDER) if len(orb) == C.d else None
            row["s"] = round(time.time() - t0, 1)
            out.write(json.dumps(row) + "\n")
            out.flush()


def _lines(path):
    """a record's lines, from the file or from its banked .gz"""
    import gzip
    if path.exists():
        return path.read_text().splitlines()
    return gzip.open(str(path) + ".gz", "rt").read().splitlines()


def collect(nparts):
    rows = [json.loads(x) for p in range(nparts) for x in _lines(HERE / f"census_{p}.jsonl") if x.strip()]
    covers = T.three_covers()
    key = {(sw, tuple(lat), wl): i for i, (sw, d, lat, wl) in enumerate(covers)}
    rows.sort(key=lambda r: (key[(r["state"], tuple(r["lattice"]), r["wbar"])], r["orbit"]))
    members = [r for r in rows if r["P"]["n"] > 0 or r["S"]["n"] > 0]
    agree = all((r["P"]["h1"], r["P"]["r1"], r["P"]["n"]) == (r["S"]["h1"], r["S"]["r1"], r["S"]["n"]) for r in rows)
    out = {"covers": [{"state": sw, "ends of companion": d, "lattice": list(lat), "wbar": wl} for sw, d, lat, wl in covers],
           "orbits read": len(rows), "routes agree on every orbit": agree,
           "member orbits": [{k: r[k] for k in ("state", "lattice", "wbar", "orbit", "size", "order", "m_A", "P", "S",
                                                "flavor group")} for r in members],
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
