"""chat1, 2026-10-28: post hoc read-out (labelled), written after riddles_checks.py's run and committed before its own.
On B1667's 48 grid points, the exact channel norm at the maximal horoball, N_max, against the small-cut asymptotic form
evaluated there from the length-2 horocycle, N_2 + 2 pi (L_max - L_2), as a relative gap, by height. It uses only
B1667's committed json and no frame computation or data.
Run:  python3 -B riddles_posthoc.py <main_checkout>"""
import sys, json, math, pathlib
ROOT = pathlib.Path(sys.argv[1]).resolve()
d = json.loads((ROOT / "frontier" / "B1667_the_canonical_cusp" / "verification" / "the_canonical_cusp.json").read_text())
grid = [p for p in d["points"] if p["where"] == "grid"]
for lo in (0.0, 2.0, 3.0):
    rel = [(p["N_max"][r] - (p["N_2"][r] + 2 * math.pi * (p["L_max"] - p["L_2"]))) / (p["N_2"][r] + 2 * math.pi * (p["L_max"] - p["L_2"]))
           for p in grid if p["tau"][1] >= lo for r in p["N_max"]]
    n = sum(1 for p in grid if p["tau"][1] >= lo)
    print("Im tau >= %.1f: %d grid points, %d channel norms; exact N_max relative to the asymptotic form: %.3f to %.3f" % (lo, n, len(rel), min(rel), max(rel)))
print("riddles_posthoc exit 0")
