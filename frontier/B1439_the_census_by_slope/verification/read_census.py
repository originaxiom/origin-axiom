#!/usr/bin/env python3
"""Reads census_by_slope_*.json and decides E1-E8 as sealed.  Computes nothing.  Sealed with the instrument."""
import json, glob, sys, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent
def block_state(pat, name):
    d = dict(json.loads(pat)); return d.get(name)            # "Y", "0", "Y0" or None
def read(d):
    old = {(o["state"], o["k"]) for o in json.load(open(HERE.parents[1] / "B1434_the_architecture_census" / "verification" / "architecture_census.json")) if "candidates" in o}
    rows = []
    for f in sorted(glob.glob(str(pathlib.Path(d) / "census_by_slope_*.json"))): rows += json.load(open(f))
    new = [r for r in rows if (r["state"], r["k"]) not in old]
    own = [r for r in new if r["k"] == 1]; firing_own = [r for r in own if r["generation_backgrounds"]]
    E = {}
    E["E1"] = any(r["state"][0] == "+" for r in firing_own)
    E["E2"] = len(firing_own) >= 37
    E["E3"] = all(block_state(p, "ten.ten") == "Y" for r in firing_own for p in r["patterns"])
    E["E4"] = all(block_state(p, "ten.five") == "0" for r in firing_own for p in r["patterns"])
    E["E5"] = any(json.loads(y) == [True, True, True, True] for r in firing_own for y in r["yukawa_type"])
    E["E6"] = all(r["torsion"] % 3 == 0 for r in firing_own)
    three = [r for r in new if r["k"] == 3 and r["generation_backgrounds"]]
    E["E7"] = all(set(r["backgrounds_by_orbit_size"]) == {"3"} for r in three)
    E["E8"] = any(block_state(p, "ten.five") in ("Y", "Y0") and block_state(p, "ten.ten") == "0" for r in new for p in r["patterns"])
    return dict(levels=len(rows), control_levels=len(rows) - len(new), new_levels=len(new), new_own_levels=len(own),
                new_own_levels_firing=len(firing_own), firing_own_states=[(r["state"], r["torsion"], r["generation_backgrounds"], r["lifted"]) for r in firing_own],
                new_three_fold_levels=len([r for r in new if r["k"] == 3]), new_three_fold_levels_firing=len(three),
                backgrounds_total=sum(r["generation_backgrounds"] for r in rows), backgrounds_new=sum(r["generation_backgrounds"] for r in new),
                slope_coincidences_at_one_prime_only=sum((r["slope_coincidences_at_one_prime_only"] or 0) for r in rows),
                predictions=E)
if __name__ == "__main__":
    r = read(sys.argv[1] if len(sys.argv) > 1 else str(HERE)); json.dump(r, open(HERE / "census_by_slope_summary.json", "w"), indent=1)
    print(json.dumps({k: v for k, v in r.items() if k != "firing_own_states"}, indent=1)); print(len(r["firing_own_states"]), "own-level firing states")
