#!/usr/bin/env python3
"""The sealed reader: answers C1-C7 of the preregistration from the complete_*.json records of a directory."""
import sys, json, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent
src = HERE / (sys.argv[1] if len(sys.argv) > 1 else "run")
recs = [json.load(open(f)) for f in sorted(src.glob("complete_*.json"))]
r6 = lambda s: round(abs(complex(s.replace(" ", ""))), 6) if s else None
tot = collections.Counter(); c5_fail = []; split = {}; updown = {}; half = []
for d in recs:
    nm = "%s %d" % (d["state"], d["k"]); pts = d["points"]
    kinds = collections.Counter(v.get("kind", "not reached") for v in pts.values()); tot.update(kinds)
    print("%-12s exponent %3d, %4d backgrounds; kappa = -2 points: %s" % (nm, d["exponent"], d["backgrounds"], dict(kinds)))
    pats = collections.Counter(); ok5 = True; differs = False; nbg = 0
    for row in d["sectors"]:
        if row["kind"] != "parabolic": continue
        t = {k: r6(v) for k, v in row["torsion"].items()}
        if None in t.values(): continue
        nbg += 1; ten = {t["Q"], t["uc"], t["ec"]}; five = {t["dc"], t["L"]}
        if len(ten) > 1 or len(five) > 1: ok5 = False
        if ten != five: differs = True
        pats[(row["slope"][:9], t["Q"], t["uc"], t["ec"], t["dc"], t["L"], t["nuc"])] += 1
    if nbg:
        split[nm] = differs
        if not ok5: c5_fail.append(nm)
        print("     sectors at the background's own point (|slope|; Q uc ec | dc L | nuc) x backgrounds:")
        for k, v in sorted(pats.items()): print("       %3d x  %s ; %s %s %s | %s %s | %s" % ((v,) + k))
    by = collections.defaultdict(list); nz = []; idx = collections.Counter()
    for c in d["couplings"]:
        if c.get("higgs_point") == "parabolic" and "abs_end_cusp" in c:
            a = round(float(c["abs_end_cusp"]), 6); nz.append(a)
            for typ in c["types"]: by[typ].append(a)
        if c.get("higgs_point") == "parabolic" and c.get("extension_point") == "parabolic" and "cusp_cusp" in c: idx[c["cusp_cusp"]["index"]] += 1
    if nz:
        print("     couplings, Higgs at its point, extension at its end: |torsion| by type:")
        for typ in ("up", "down", "lepton", "neutrino"):
            if by[typ]: print("       %-8s %s" % (typ, dict(sorted(collections.Counter(by[typ]).items()))))
        if by["up"] and by["down"]:
            updown[nm] = sorted(set(by["up"])) != sorted(set(by["down"]))
            if all(abs(2 * u - w) < 1e-5 for u in by["up"] for w in by["down"]): half.append(nm)
    tot["zero torsion"] += sum(1 for a in nz if a < 1e-9); tot["couplings with a value"] += len(nz)
    for k, v in idx.items(): tot[("index", k)] += v
    if idx: print("     class index at the doubly parabolic points: %s" % dict(idx))
print()
ind = {k[1]: v for k, v in tot.items() if isinstance(k, tuple)}
print("C1  class index at doubly parabolic points: %s  -> %s" % (ind, "all zero" if set(ind) <= {0} and ind else ("NOT all zero" if ind else "none computed")))
print("C2  couplings with a value: %d, of which torsion zero: %d" % (tot["couplings with a value"], tot["zero torsion"]))
print("C3  levels where the up-type and down-type moduli differ: %d of %d %s" % (sum(updown.values()), len(updown), sorted(k for k, v in updown.items() if v)))
print("C4  levels where every up-type modulus is half of every down-type modulus: %s" % half)
print("C5  levels where the ten's three sectors or the five-bar's two do not share a torsion: %s (of %d levels with a table)" % (c5_fail, len(split)))
print("C6  levels where the ten and the five-bar differ on some background: %d of %d %s" % (sum(split.values()), len(split), sorted(k for k, v in split.items() if v)))
reach = tot["parabolic"]; al = tot["parabolic"] + tot["elliptic"] + tot["not reached"]
print("C7  characters attempted: %d; parabolic point %d, elliptic %d, not reached %d" % (al, reach, tot["elliptic"], tot["not reached"]))
