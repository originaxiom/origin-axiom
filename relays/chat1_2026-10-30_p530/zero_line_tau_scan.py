# Referee 2 check (read-only on the record): on the zero line, does the S / S~ split (and so the
# reading's split of up from down) hold at every tau, or does it vanish on mirror lines (Re tau = 0, 1/2)?
# Uses B1726's committed compute(); both horocycles.
import sys, importlib.util, pathlib
from fractions import Fraction as Fr
ROOT = pathlib.Path(sys.argv[1])
spec = importlib.util.spec_from_file_location("census", ROOT / "frontier/B1726_the_two_ingredients_replicated/verification/census.py")
c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
def rel(a, b): return max(abs(x - y) / max(abs(x), abs(y)) for x, y in zip(a, b))
for (re_t, im_t) in [(0.0, 2.75), (0.5, 2.75), (0.25, 2.75), (0.35, 2.75), (0.05, 3.05), (0.45, 3.05), (0.5, 3.05), (0.0, 3.05), (1.0, 2.75), (0.75, 2.75)]:
    r = c.compute(re_t, im_t, Fr(0), Fr(0))
    for h in ("L_max", "L_2"):
        S, St = r["up|%s|S" % h], r["up|%s|St" % h]
        same_sectors = max(rel(r["%s|%s|%s" % (s, h, rn)], r["up|%s|%s" % (h, rn)]) for s in ("down", "lep") for rn in ("S", "St"))
        print("tau %.2f+%.2fi %-5s  S %-32s St %-32s  rel(S,St) %.3e  sectors-identical-dev %.1e" % (re_t, im_t, h, [round(x, 8) for x in S], [round(x, 8) for x in St], rel(S, St), same_sectors))
