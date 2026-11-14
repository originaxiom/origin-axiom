#!/usr/bin/env python3
"""The principle note's falsifier W1, read from committed outputs only (relays/SM_PRINCIPLE_NOTE_EXPECTATIONS.md,
pushed before this was run): does every recorded +- binary of the chain have equal multiplicities?  Not blind: most of
these censuses were seen in their own runs.  It gathers them in one place, with the test applied the same way to each.
    python3 w1_pairs.py MAIN_CHECKOUT [out.json]"""
import sys, json, pathlib
from collections import Counter
R = pathlib.Path(__file__).resolve().parents[1]
MAIN = pathlib.Path(sys.argv[1]).resolve()


def sym(c):
    """c: {value: count}; symmetric when count(v) == count(-v) for every v"""
    c = {int(k): v for k, v in c.items()}
    return all(c.get(-k, 0) == v for k, v in c.items())


def main():
    out = {}
    # E1: (n, n*) census, (1,0) against (0,1), per level
    e1 = json.load(open(R / "sm_c6" / "e1_results.json"))
    out["E1_(1,0)_vs_(0,1)"] = [sum(c["census"].get("10", 0) == c["census"].get("01", 0) for c in e1["census"]), len(e1["census"])]
    # B1441: I histograms per entry (main's committed slices)
    hist = []
    for f in sorted((MAIN / "frontier" / "B1441_the_several_cusped_levels" / "verification").glob("several_cusps_*.json")):
        for e in json.load(open(f)):
            if e.get("I_hist"): hist.append(e["I_hist"])
    out["B1441_I_histograms"] = [sum(sym(h) for h in hist), len(hist)]
    # SM-C8: D_ord per entry
    c8 = json.load(open(R / "sm_c8" / "c8_results.json"))
    E = [e for e in c8["entries"] if "modules" in e and e["D_ord"]]
    out["SM-C8_D_ord"] = [sum(sym(e["D_ord"]) for e in E), len(E)]
    out["SM-C8_index_I"] = [sum(sym(e["I_hist"]) for e in E), len(E)]
    # SM-C10: twisted and untwisted gaps per level (sealed run) and post hoc ones
    c10 = json.load(open(R / "sm_c10" / "c10_results.json"))
    L = [v["summary"] for v in c10["levels"].values() if v["summary"]["modules"]]
    out["SM-C10_g_w"] = [sum(sym(s["census_g_w"]) for s in L), len(L)]
    out["SM-C10_g_0"] = [sum(sym(s["census_g_0"]) for s in L), len(L)]
    un = json.load(open(R / "sm_c10" / "c10_posthoc_unipotent.json"))
    out["SM-C10_unipotent_g_w"] = [int(sym(un["g_w_census"])), 1]
    # SM-C9: rho(M^-1) = -rho(M) (T3), and the sign census of rho per level
    c9 = json.load(open(R / "sm_c9" / "c9_results.json"))
    out["SM-C9_rho_flips_with_orientation"] = [c9["transcription"]["T3"], c9["transcription"]["n"]]
    by = {}
    for r in c9["rows"]:
        by.setdefault(json.dumps(r["level"]), Counter())[(r["rho_f"] > 1e-12) - (r["rho_f"] < -1e-12)] += 1
    out["SM-C9_rho_sign_census_per_level (information)"] = {k: dict(v) for k, v in by.items()}
    tests = {k: v for k, v in out.items() if isinstance(v, list)}
    out["W1_happens"] = any(v[0] != v[1] for v in tests.values())
    json.dump(out, open(sys.argv[2] if len(sys.argv) > 2 else pathlib.Path(__file__).parent / "w1_pairs.json", "w"), indent=1)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
