#!/usr/bin/env python3
"""B1542's audit -- the data route F reads (sm:B1541's route_f.py checks every item itself before using it): m003's
presentation and cusp words, the exact holonomy (coefficients on 1, zeta, ..., zeta^7, zeta = e^(2 pi i / 24)), and for each of
the four degree-60 covers its permutation action, its deck permutation tau (order 6), and its cusps in sm:B1536's order (so that
a stratum S names the same cusps in both).  This script uses the instrument (ncyc.py and the sm:B1536 modules it loads); route F
does not.

    python3 export_f.py      ->  route_f_input_degree60.json"""
import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    spec = importlib.util.spec_from_file_location("b1542_ncyc_export", HERE / "ncyc.py")
    L = importlib.util.module_from_spec(spec)
    sys.modules["b1542_ncyc_export"] = L
    spec.loader.exec_module(L)
    spec = importlib.util.spec_from_file_location("b1542_run_export", HERE / "run.py")
    RUN = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(RUN)
    out = {"state": "m003", "k": RUN.K, "covers": {}}
    for cid in RUN.COVERS:
        st, perms, pts, tau = L.build("m003", cid, RUN.PSI[0], RUN.PSI[1], RUN.K)
        G = st["G"]
        if "gens" not in out:
            out.update(gens=list(G.gens), rels=list(G.rels), cusp=list(G.cusp),
                       holonomy={g: [[[str(Fraction(c, x.d)) for c in x.c] for x in row] for row in st["g2"][g]]
                                 for g in "abt"})
        out["covers"][cid] = {"perms": {g: list(perms[g]) for g in G.gens}, "tau": list(tau),
                              "cusps (sm:B1536's order)": [c["orbit"] for c in L.CL.cusps(G, perms)]}
    (HERE / "route_f_input_degree60.json").write_text(json.dumps(out) + "\n")
    print({cid: len(v["cusps (sm:B1536's order)"]) for cid, v in out["covers"].items()})


if __name__ == "__main__":
    main()
