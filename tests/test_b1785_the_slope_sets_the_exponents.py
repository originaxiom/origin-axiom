"""B1785 -- the slope sets the exponents.  The committed census: 662 lines; the exponents on alpha = 2/5 are (up, down) =
(3/10, 1/5) to 0.02 at every offset; the offset moves the up m2/m3 exponent by at most 0.06 except at the tie alpha = 1/4."""
import json, pathlib, statistics
from fractions import Fraction as Fr
from collections import defaultdict
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1785_the_slope_sets_the_exponents" / "verification"


def test_the_census():
    d = json.loads((A / "exponents.json").read_text(encoding="utf-8"))
    assert len(d) == 662
    by = defaultdict(list)
    for r in d: by[Fr(r["alpha"])].append(r)
    for r in by[Fr(2, 5)]:
        assert abs(r["up|L_max|St|m2/m3"]["exponent"] - 0.3) < 0.02 and abs(r["down|L_max|S|m2/m3"]["exponent"] - 0.2) < 0.01
    for a, rs in by.items():
        if a == Fr(1, 4): continue
        e = [r["up|L_max|St|m2/m3"]["exponent"] for r in rs]
        assert max(e) - min(e) < 0.06, a
