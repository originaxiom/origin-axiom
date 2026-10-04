#!/usr/bin/env python3
"""B1474 post-processing: close the found generators of K under products, recompute the coset eta_0 K and the verdict
(GENUINE SWAP iff 1 not in eta_0 K), and the agreement with the torsion route. Writes table.json."""
import json, pathlib, itertools
HERE = pathlib.Path(__file__).resolve().parent
pc = json.load(open(HERE / "preserving_characters.json")); sw = json.load(open(HERE / "spin_swap.json"))
def close(gens_):
    G = {tuple(g) for g in gens_}; n = len(next(iter(G))); G.add(tuple([1] * n))
    while True:
        new = {tuple(a * b for a, b in zip(x, y)) for x in G for y in G} | G
        if new == G: return G
        G = new
table = {}
for nm, r in pc.items():
    K = close(r["K"]); n = len(r["gens"]); one = tuple([1] * n)
    etas = {tuple(e) for e in r["reversing_etas"]}; e0 = next(iter(etas)); coset = {tuple(a * b for a, b in zip(e0, k)) for k in K}
    genuine = one not in coset
    table[nm] = dict(h1=sw[nm]["h1"], gens=r["gens"], K_closed=sorted(K), K_order=len(K), reversing_etas=sorted(etas), coset=sorted(coset),
                     etas_in_coset=etas <= coset, verdict="GENUINE SWAP" if genuine else "FIX", torsion_odd_real=r["torsion_route_odd_real"],
                     agree=(r["torsion_route_odd_real"] == (not genuine)))
for nm, v in sw.items():
    if "error" in v or not v.get("amphichiral_snappy") or nm in table: continue
    table[nm] = dict(h1=v["h1"], verdict="UNDETERMINED (no mirror word found; L up to %s)" % v["L"], torsion_odd_real=None, agree=None)
summary = dict(members=len(table), genuine_swap=sorted(k for k, v in table.items() if v["verdict"] == "GENUINE SWAP"),
               fix=sorted(k for k, v in table.items() if v["verdict"] == "FIX"), undetermined=sorted(k for k, v in table.items() if v["verdict"].startswith("UNDETERMINED")),
               all_decided_agree=all(v["agree"] for v in table.values() if v["agree"] is not None), etas_all_in_cosets=all(v.get("etas_in_coset", True) for v in table.values()),
               chiral_none=sum(1 for v in sw.values() if "error" not in v and not v["amphichiral_snappy"] and v["verdict"].startswith("NONE")),
               chiral_total=sum(1 for v in sw.values() if "error" not in v and not v["amphichiral_snappy"]))
json.dump(dict(summary=summary, table=table), open(HERE / "table.json", "w"), indent=1)
print(json.dumps(summary, indent=1))
for nm, v in table.items(): print("%-11s %-16s K=%s etas=%s -> %s | torsion odd-real %s agree %s" % (nm, v["h1"], v.get("K_order"), v.get("reversing_etas"), v["verdict"], v["torsion_odd_real"], v["agree"]))
