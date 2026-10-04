#!/usr/bin/env python3
"""Lists for B1476 P7/P8: amphichiral cusped census manifolds (first 3000) with their CS class, and the amphichiral closed
census manifolds (B1239's 37) -- names only; no spin computation here."""
import json, warnings, pathlib; warnings.filterwarnings("ignore")
import snappy
def fold(x, mod):
    x = float(x) % mod; return min(x, mod - x)
def cls(c, mod=0.5):
    f0 = fold(c, mod); f4 = fold(c - 0.25, mod); return "zero" if f0 < 1e-9 else ("quarter" if f4 < 1e-9 else "other")
fam = {r["name"] for r in json.load(open(pathlib.Path(__file__).resolve().parents[2] / "B1235_two_seat_harvest" / "verification" / "chirality_112.json"))}
out = dict(cusped=[], closed=[])
for i, M in enumerate(snappy.OrientableCuspedCensus[:3000]):
    try:
        if not M.symmetry_group().is_amphicheiral(): continue
        c = float(M.chern_simons())
    except Exception: continue
    out["cusped"].append(dict(name=M.name(), cusps=M.num_cusps(), h1=str(M.homology()), cs=c, cls=cls(c), in_family=M.name() in fam))
print("cusped amphichiral:", len(out["cusped"]), {k: sum(1 for r in out["cusped"] if r["cls"] == k) for k in ("zero", "quarter", "other")}, "outside family:", sum(1 for r in out["cusped"] if not r["in_family"]), flush=True)
def closed_cs(M):
    P = M.copy(); fill = [tuple(c["filling"]) for c in P.cusp_info()]
    P.dehn_fill([(0, 0)] * P.num_cusps()); P.chern_simons(); P.dehn_fill(fill); return float(P.chern_simons())
for M in snappy.OrientableClosedCensus:
    try:
        if not M.symmetry_group().is_amphicheiral(): continue
        c = closed_cs(M)
    except Exception: continue
    out["closed"].append(dict(name=M.name(), h1=str(M.homology()), cs=c, cls=cls(c, 1.0)))
print("closed amphichiral:", len(out["closed"]), {k: sum(1 for r in out["closed"] if r["cls"] == k) for k in ("zero", "quarter", "other")}, flush=True)
json.dump(out, open("census_lists.json", "w"), indent=1)
