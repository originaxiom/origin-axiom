#!/usr/bin/env python3
"""B1541's audit -- the data route F reads (route_f.py checks every item itself before using it): m003's presentation and cusp
words, the exact holonomy (coefficients on 1, zeta, ..., zeta^7, zeta = e^(2 pi i / 24)), N_45's permutation action and deck
permutation, and the cusps in sm:B1536's order (so that a stratum S names the same cusps in both).  This script uses the
instrument (n45.py and the sm:B1536 modules it loads); route F does not.

    python3 export_f.py      ->  route_f_input_n45.json"""
import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    spec = importlib.util.spec_from_file_location("b1541_n45_export", HERE / "n45.py")
    L = importlib.util.module_from_spec(spec)
    sys.modules["b1541_n45_export"] = L
    spec.loader.exec_module(L)
    st, perms, pts, tau = L.build()
    G = st["G"]
    hol = {g: [[[str(Fraction(c, x.d)) for c in x.c] for x in row] for row in st["g2"][g]] for g in "abt"}
    out = {"state": "m003", "gens": list(G.gens), "rels": list(G.rels), "cusp": list(G.cusp), "holonomy": hol,
           "cover": "N_45", "perms": {g: list(perms[g]) for g in G.gens}, "tau": list(tau), "k": 5,
           "cusps (sm:B1536's order)": [c["orbit"] for c in L.CL.cusps(G, perms)]}
    (HERE / "route_f_input_n45.json").write_text(json.dumps(out) + "\n")
    print({k: (v if k in ("state", "gens", "rels", "cusp", "cover", "k") else "...") for k, v in out.items()})


if __name__ == "__main__":
    main()
