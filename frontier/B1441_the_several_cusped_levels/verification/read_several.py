#!/usr/bin/env python3
"""Reads several_cusps_<slice>.json (digits only in the slice) and decides M1-M7 as sealed.  Computes nothing.
Its own output is written to the arc's root, outside its input pattern, and it may be run any number of times."""
import json, glob, sys, pathlib, re
HERE = pathlib.Path(__file__).resolve().parent
def read(d):
    rows = []
    for f in sorted(glob.glob(str(pathlib.Path(d) / "several_cusps_*.json"))):
        if re.fullmatch(r"several_cusps_\d+\.json", pathlib.Path(f).name): rows += json.load(open(f))
    run = [r for r in rows if "skipped" not in r]
    covers = [r for r in run if r["degree"] is not None]
    def named(nm): return [r for r in run if r["root"] == nm and r["degree"] is None]
    mx = max([r["max_abs_I"] for r in run] or [0])
    M = {}
    M["M1"] = any(r["max_abs_I"] >= 2 for r in run)
    M["M2"] = any(r["max_abs_I"] >= 3 for r in run)
    M["M3"] = all(r["max_abs_I"] <= r["cusps"] for r in run)
    M["M4"] = all(any(r["max_abs_I"] >= 1 for r in named(nm)) for nm in ("m202", "s959"))
    M["M5"] = any(r["max_abs_I"] >= 2 for nm in ("m202", "s959") for r in named(nm))
    def live2(key):                                          # "|I|=k live (..) dual (..)"
        m = re.match(r"\|I\|=(\d+) live \((.*?)\) dual \((.*?)\)", key)
        k = int(m.group(1)); a = [int(x) for x in m.group(2).replace(",", " ").split()]; b = [int(x) for x in m.group(3).replace(",", " ").split()]
        return k, max(sum(1 for x in a if x), sum(1 for x in b if x))
    M["M6"] = all(live2(key)[1] >= 2 for r in run for key in r["firing_by_live_cusps"] if live2(key)[0] >= 2)
    cmx = max([r["max_abs_I"] for r in covers] or [0])
    M["M7"] = cmx > 0 and any(r["max_abs_I"] == cmx and r["cusps"] >= 3 for r in covers)
    return dict(entries=len(rows), run=len(run), skipped=[r["tag"] for r in rows if "skipped" in r], modules=sum(r["modules"] for r in run),
                max_abs_I=mx, max_abs_I_on_covers=cmx, rechecks_differing=sum(r["rechecks_differing"] for r in run),
                by_cusps={str(c): dict(manifolds=sum(1 for r in run if r["cusps"] == c), max_abs_I=max([r["max_abs_I"] for r in run if r["cusps"] == c] or [0]),
                                       with_abs_I_ge_2=sum(1 for r in run if r["cusps"] == c and r["max_abs_I"] >= 2)) for c in sorted({r["cusps"] for r in run})},
                carriers=[(r["tag"], r["cusps"], r["max_abs_I"], r["witnesses_abs_I_ge_2"]) for r in run if r["max_abs_I"] >= 2],
                named={nm: [(r["tag"], r["N"], r["modules"], r["I_hist"]) for r in named(nm)] for nm in ("m202", "s959", "o10_150726", "m129", "m125")},
                predictions=M)
if __name__ == "__main__":
    r = read(sys.argv[1] if len(sys.argv) > 1 else str(HERE)); json.dump(r, open(HERE.parent / "several_cusps_summary.json", "w"), indent=1)
    print(json.dumps({k: r[k] for k in ("entries", "run", "skipped", "modules", "max_abs_I", "rechecks_differing", "by_cusps", "predictions")}, indent=1))
