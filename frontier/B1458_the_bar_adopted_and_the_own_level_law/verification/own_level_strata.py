#!/usr/bin/env python3
"""B1458 -- the own-level law on main's census, by manifold and by the fibre torsion's group structure.

The SM seat's sm:B1518 (its relay of 2026-10-02): "no criterion in the fibre torsion with the monodromy's action exists on
your census: twenty-two (G, sign) strata each hold a firing and a silent manifold; the smallest pair is m369 = -LLRLR and
o9_00001 = -LLLLLLLLR".  Re-derived here from main's own census files (B1439), with the unit of B1456 (a word and its
reverse are one manifold) and G = coker(eps w - I) by Smith normal form.

    python3 own_level_strata.py      # prints, writes own_level_strata.json
"""
import glob, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "frontier", "B1454_genesis_v1_verified_and_adopted", "verification"))
sys.path.insert(0, os.path.join(ROOT, "frontier", "B1456_genesis_v1_2_verified_and_the_seats_reconciled", "verification"))
import genesis_own as G
sys.argv = [sys.argv[0], "--quick"]; import v1_2_own as V

rows = []
for f in sorted(glob.glob(os.path.join(ROOT, "frontier", "B1439_the_census_by_slope", "verification", "census_by_slope_*.json"))): rows += json.load(open(f))
own = {r["state"]: r for r in rows if r["k"] == 1}
assert len(own) == 758
# one row per manifold: the canonical representative under rotation, swap and reversal
man = {}
for st, r in own.items():
    key = st[0] + V.canon(st[1:], True); man.setdefault(key, []).append(r)
assert len(man) == 536
def smith_of(st):
    B = G.word(st[1:]) if st[0] == "+" else G.neg(G.word(st[1:]))
    return G.smith(G.minus_identity(B))
strata = {}; both_agree = True; fired = 0
for key, rs in man.items():
    fires = {r["generation_backgrounds"] > 0 for r in rs}
    if len(fires) > 1: both_agree = False
    fire = rs[0]["generation_backgrounds"] > 0; fired += fire
    g = smith_of(rs[0]["state"]); s = (g, key[0]); strata.setdefault(s, [set(), set()])[0 if fire else 1].add(key)
mixed = {k: v for k, v in strata.items() if v[0] and v[1]}
smallest = min(((len(k[0]) and k[0][1]), k, sorted(v[0], key=len)[0], sorted(v[1], key=len)[0]) for k, v in mixed.items())
out = dict(manifolds=len(man), firing_manifolds=fired, pairs_agree=both_agree, strata=len(strata), mixed_strata=len(mixed),
           mixed_list=sorted((str(k), len(v[0]), len(v[1])) for k, v in mixed.items()),
           smallest_mixed=dict(stratum=str(smallest[1]), firing=smallest[2], silent=smallest[3]),
           m369=dict(G=str(smith_of("-LLRLR")), backgrounds=own["-LLRLR"]["generation_backgrounds"]),
           o9_00001=dict(G=str(smith_of("-LLLLLLLLR")), backgrounds=own["-LLLLLLLLR"]["generation_backgrounds"]))
for k, v in out.items(): print(k, v if k != "mixed_list" else v[:8])
json.dump(out, open(os.path.join(HERE, "own_level_strata.json"), "w"), indent=1)
ok = len(man) == 536 and fired == 87 and both_agree and len(mixed) >= 1 and out["m369"]["G"] == out["o9_00001"]["G"] and out["o9_00001"]["backgrounds"] == 0
print("VERDICT own-level-strata: %s" % ("PASS" if ok else "FAIL")); sys.exit(0 if ok else 1)
