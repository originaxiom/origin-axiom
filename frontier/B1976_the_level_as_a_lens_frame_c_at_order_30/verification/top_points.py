"""B1976 follow-up, labelled post hoc (written after reading level30_run.json, 2026-11-24): the five order-30 points with the
largest off-diagonal mixing at height 30 -- their |V| at heights 20 and 30 and the rates (eps units), plus 1 - least diagonal
at the order-6 controls."""
import sys, pathlib, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import level30 as L
from fractions import Fraction as Fr
mp = L.mp
R = json.load(open(pathlib.Path(__file__).with_name("level30_run.json")))
print("order-6 controls: 1 - least diagonal from %.1e to %.1e" % (min(1 - r["diag"] for r in R["P6"]), max(1 - r["diag"] for r in R["P6"])))
top = sorted(R["P30"], key=lambda r: -r["off"])[:5]
for r in top:
    a, b = Fr(r["a"]), Fr(r["b"]); vs = {}
    for y in (20.0, 30.0):
        out = L.at(a, b, y); V = L.CM.U_of(out["up"]["Y"]).H * L.CM.U_of(out["down"]["Y"]); vs[y] = V
    rate = lambda i, j: float(-(mp.log(abs(vs[30.0][i, j])) - mp.log(abs(vs[20.0][i, j]))) / (mp.pi * 10))
    print("(%s, %s): |V| at 30 = %s ; rates V12 %.3f V23 %.3f V13 %.3f" % (a, b, [[round(float(abs(vs[30.0][i, j])), 4) for j in range(3)] for i in range(3)], rate(0, 1), rate(1, 2), rate(0, 2)), flush=True)
