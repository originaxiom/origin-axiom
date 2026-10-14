#!/usr/bin/env python3
"""B1548 -- the structure census before the seal (PREREGISTRATION.md section 5).  Route R, at every member of the circle
through chi0: its order and key, n(nu^4), the structure (h1(nu^5 rho), n(nu^5 rho), h1(L), n(L), dim K0^nu, its interior
part), the sixteen strata's dimensions, the distinct strata, and the support of a generic class of each distinct stratum
(seed crc32 of "B1548|census|m|key|U").  Structure only: no reading, no count, is taken at any member.

    python3 census.py [--record]   ->  census.json"""
import importlib.util
import json
import random
import sys
import time
import zlib
from collections import Counter
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


def main():
    t0 = time.time()
    RUN = load("b1548_run_census", HERE / "run.py")
    C = RUN.setup("R")
    CL, ML, cv, CH = C["CL"], C["ML"], C["cover"], C["chars"]
    rows = []
    for i, (m, key, e) in enumerate(C["members"]):
        ks = RUN.key_str(key)
        M = CL.member(cv, "R", e, m)
        st = ML.strata(M)
        dims = {U: d for U, (d, _) in st.items()}
        dist = ML.distinct_strata(dims)
        supp = {}
        for U in dist:
            rng = random.Random(zlib.crc32(f"B1548|census|{m}|{ks}|{U}".encode()))
            supp[U] = [int(x) for x in M.support(M.draw(st[U][1], rng))]
        rows.append({"index": i, "order": m, "key": ks, "galois rep": RUN.key_str(RUN.galois_rep(key, m)),
                     "n(nu^4)": CL.line_n(CH, cv, "R", (4 * e) % m, m), "structure": M.structure(), "strata": dims,
                     "distinct": dist, "generic supports": supp})
        print(f"{i + 1}/{len(C['members'])}: order {m}", flush=True)
    s = lambda r: r["structure"]                                                    # noqa: E731
    table = Counter(json.dumps([r["order"], s(r)["h1(nu^5 rho)"], s(r)["n(nu^5 rho)"], s(r)["h1(L)"], s(r)["n(L)"],
                                s(r)["dim K0"], s(r)["dim K0 interior"], sorted(r["distinct"], key=lambda U: (len(U), U))])
                    for r in rows)
    gal = {}
    for r in rows:
        gal.setdefault((r["order"], r["galois rep"]), set()).add(json.dumps(
            [r["n(nu^4)"], r["structure"], r["strata"], r["distinct"]], sort_keys=True))
    out = {"route": "R", "members": len(rows), "chi0": RUN.key_str(C["chi0"]), "direction": list(C["direction"]),
           "by (order, h1(nu^5 rho), n(nu^5 rho), h1(L), n(L), dim K0, its interior part, distinct strata)":
               dict(sorted(table.items())),
           "Galois classes": len(gal), "Galois classes alike in structure": all(len(v) == 1 for v in gal.values()),
           "n(nu^4) = 3 at every member": all(r["n(nu^4)"] == 3 for r in rows),
           "distinct strata in all": sum(len(r["distinct"]) for r in rows),
           "distinct strata by |U|": dict(Counter(len(U.split(",")) if U else 0 for r in rows for U in r["distinct"])),
           "every generic support is U": all(r["generic supports"][U] == ([int(x) for x in U.split(",")] if U else [])
                                             for r in rows for U in r["distinct"]),
           "K0^nu not zero at": sum(1 for r in rows if s(r)["dim K0"] > 0),
           "rows": rows, "seconds": round(time.time() - t0, 1)}
    print(json.dumps({k: v for k, v in out.items() if k != "rows"}, indent=1), flush=True)
    if "--record" in sys.argv:
        (HERE / "census.json").write_text(json.dumps(out, indent=1) + "\n")
    return out


if __name__ == "__main__":
    main()
