"""P-294 (data-free): the frame's own R2, R1 on slope-2/5 lines of orders 10-30 as Im tau grows (reading S, L_max, B1726's
compute; L clamped as in B1785): do they tend to 1 (lepton = down at leading order) or to a constant?"""
import json, pathlib, importlib.util, contextlib, io
from fractions import Fraction as Fr
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
spec = importlib.util.spec_from_file_location("c26", ROOT / "frontier/B1726_the_two_ingredients_replicated/verification/census.py")
C = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(C)
out = {}
for b in (Fr(1, 10), Fr(3, 10), Fr(2, 15), Fr(4, 25), Fr(23, 30), Fr(1, 6)):
    row = []
    for y in (3.0, 4.0, 6.0, 8.0):
        r = C.compute(1.0 / 3.0, y, Fr(2, 5), b)
        d2, d1 = r["down|L_max|S"]; e2, e1 = r["lep|L_max|S"]
        row.append((y, e2 / d2, d1 / e1))
    out[str(b)] = row
    print("b %-5s" % b, "  ".join("Im %.0f: R2 %.4f R1 %.4f" % t for t in row))
json.dump(out, open(pathlib.Path(__file__).resolve().parent / "r_twofifths.json", "w"), indent=1)
