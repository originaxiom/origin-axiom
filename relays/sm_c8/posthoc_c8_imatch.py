#!/usr/bin/env python3
"""SM-C8, post hoc and labelled: the sealed control "the record's index against B1441's I histogram" compared module
sets that differ where H^1(M; l) has dimension > 1 (B1441 takes its basis and random combinations mod p).  Here: for
every entry, the largest dim H^1(M; l), and whether the histograms agree on the entries where every H^1(M; l) is a line.
    python3 posthoc_c8_imatch.py MAIN_CHECKOUT [out.json]"""
import sys, json, math, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.argv = [sys.argv[0], sys.argv[1]] + sys.argv[2:]
import run_c8 as R
SC = R.SC


def main():
    res = json.load(open(HERE / "c8_results.json")); rows = []
    by = {e["tag"]: e for e in res["entries"] if "modules" in e}
    for tag, nm, d, i, N in SC.population():
        if N is not None or tag not in by: continue
        C = SC.get(nm, d, i); G = R.GroupC(C); b1, tors, Nt = SC.homology(G.gens, G.rels); Nn = max(Nt, 2)
        chars = SC.characters(G.gens, G.rels, Nn); triv = tuple([0] * G.n)
        dims = [R.h1_basis(G, [complex(np.exp(2j * math.pi * e / Nn)) for e in c]).shape[1] for c in chars if c != triv]
        e = by[tag]
        rows.append({"tag": tag, "max_dim_H1_l": max(dims or [0]), "I_matches": e["I_matches_B1441"]})
    lines = [r for r in rows if r["max_dim_H1_l"] <= 1]
    out = {"entries": len(rows), "entries_all_lines": len(lines), "match_on_all_lines": sum(bool(r["I_matches"]) for r in lines),
           "entries_with_a_plane_or_more": len(rows) - len(lines),
           "match_where_some_dim_gt_1": sum(bool(r["I_matches"]) for r in rows if r["max_dim_H1_l"] > 1), "rows": rows}
    json.dump(out, open(sys.argv[2] if len(sys.argv) > 2 else HERE / "c8_posthoc_imatch.json", "w"), indent=1)
    print(json.dumps({k: v for k, v in out.items() if k != "rows"}, indent=1))


if __name__ == "__main__":
    main()
