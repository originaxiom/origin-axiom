"""P-294 (data-free): is the frame's own R2 = (m2/m3)_lep/(m2/m3)_down near 3 on the slope 1/10 structural or a height
coincidence?  (a) B1786's census rows of slope 1/10 binned by Im tau; (b) the frame recomputed on (1/10, b) lines at Im tau
2, 3, 4, 6, 8 (B1726's compute, L clamped as in B1785), reading S for both sectors; B1788's closed form gives the two
sectors the same m2/m3 exponent 1/5 on 1/10, so R2 is a prefactor ratio and should tend to a constant if structural."""
import json, math, pathlib, statistics, sys, importlib.util, contextlib, io
from fractions import Fraction as Fr
from collections import defaultdict
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
by = defaultdict(list)
with open(ROOT / "frontier/B1786_the_slope_principle_out_of_sample/verification/census.jsonl", encoding="utf-8") as fh:
    for l in fh:
        r = json.loads(l)
        if r["alpha"] != "1/10": continue
        for h in ("L_max", "L_2"):
            d2 = r["down|%s|S" % h][0]; e2 = r["lep|%s|S" % h][0]
            by[(round(r["Im_tau"], 1), h)].append(e2 / d2)
print("(a) B1786 census, slope 1/10: median R2 by Im tau (rounded) and horocycle")
for k in sorted(by): print("   Im tau %.1f %-5s n %3d  median R2 %.3f  [%.3f, %.3f]" % (k[0], k[1], len(by[k]), statistics.median(by[k]), min(by[k]), max(by[k])))
spec = importlib.util.spec_from_file_location("c26", ROOT / "frontier/B1726_the_two_ingredients_replicated/verification/census.py")
C = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(C)
print("(b) recomputed, reading S, L_max (clamped beyond the column as in B1785): R2 on (1/10, b)")
out = {}
for b in (Fr(1, 30), Fr(1, 6), Fr(7, 30), Fr(1, 2)):
    row = []
    for y in (2.0, 3.0, 4.0, 6.0, 8.0):
        r = C.compute(1.0 / 3.0, y, Fr(1, 10), b)
        d2, d1 = r["down|L_max|S"]; e2, e1 = r["lep|L_max|S"]
        row.append((y, e2 / d2, d1 / e1))
    out[str(b)] = row
    print("   b %-5s" % b, "  ".join("Im %.0f: R2 %.3f R1 %.2e" % t for t in row))
json.dump({"census": {"%s %s" % k: statistics.median(v) for k, v in by.items()}, "recomputed": out}, open(pathlib.Path(__file__).resolve().parent / "r2_tenth.json", "w"), indent=1)
