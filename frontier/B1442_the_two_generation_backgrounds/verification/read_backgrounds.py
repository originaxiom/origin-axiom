#!/usr/bin/env python3
"""Reads backgrounds_<slice>.json (digits only) and decides G1-G5 as sealed.  Computes nothing; writes its summary to
the arc's root, outside its input pattern; may be run any number of times."""
import json, glob, sys, pathlib, re
HERE = pathlib.Path(__file__).resolve().parent
def read(d):
    rows = []
    for f in sorted(glob.glob(str(pathlib.Path(d) / "backgrounds_*.json"))):
        if re.fullmatch(r"backgrounds_\d+\.json", pathlib.Path(f).name): rows += json.load(open(f))
    def has(r, pred, key="by_count"): return any(pred(int(k)) and v for k, v in r[key].items())
    G = {}
    G["G1"] = any(has(r, lambda g: abs(g) == 2) for r in rows)
    G["G2"] = all(has(r, lambda g: abs(g) == 1) for r in rows)
    G["G3"] = any(v and abs(int(k.split(",")[0])) == 2 and int(k.split(",")[1]) == int(k.split(",")[0]) for r in rows for k, v in r["by_count_and_singlet"].items())
    G["G4"] = any(has(r, lambda g: abs(g) == 2, "by_count_generic_class_only") for r in rows)
    G["G5"] = all(not has(r, lambda g: abs(g) > 2) for r in rows)
    return dict(carriers=len(rows), backgrounds=sum(r["backgrounds"] for r in rows),
                by_count={str(g): sum(r["by_count"].get(str(g), 0) for r in rows) for g in (-3, -2, -1, 1, 2, 3)},
                carriers_with_count_two=[r["tag"] for r in rows if has(r, lambda g: abs(g) == 2)],
                per_carrier=[(r["tag"], r["cusps"], r["characters"], r["backgrounds"], r["by_count"], r["by_count_generic_class_only"]) for r in rows],
                predictions=G)
if __name__ == "__main__":
    r = read(sys.argv[1] if len(sys.argv) > 1 else str(HERE)); json.dump(r, open(HERE.parent / "backgrounds_summary.json", "w"), indent=1)
    print(json.dumps({k: r[k] for k in ("carriers", "backgrounds", "by_count", "carriers_with_count_two", "predictions")}, indent=1))
