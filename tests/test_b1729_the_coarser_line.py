"""B1729 -- the coarser line (P-305), NEGATIVE. Live: the lepton charges are 3 x (-1, 2) and the quarks' are not; one
order-5 point recomputed (R2 = R1 = 1). Stored: the census's medians against the criteria written before the read."""
import json, math, pathlib, sys
from fractions import Fraction as Fr
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1729_the_coarser_line"
ROOT = A.parents[1]


def test_the_charges():
    six_y = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6}
    assert six_y["L"] == 3 * -1 and six_y["e"] == 3 * 2
    assert all(six_y[f] % 3 for f in ("Q", "u", "d"))


def test_the_census_stored():
    d = json.loads((A / "verification" / "frame_r2r1.json").read_text(encoding="utf-8"))["by_order"]
    assert d["5"]["max_abs_log_order5_check"] < 1e-9 and sum(v["masked"] for v in d.values()) == 0
    assert sum(v["n"] for v in d.values()) == 7344 * 4                   # 2 horocycles x 2 readings per point
    three = [d[str(N)]["logR2_q"][2] for N in (15, 18, 21, 24, 27, 30)]
    rest = [d[str(N)]["logR2_q"][2] for N in range(13, 30) if N % 3]
    r1three = [d[str(N)]["logR1_q"][2] for N in (15, 18, 21, 24, 27, 30)]
    r1rest = [d[str(N)]["logR1_q"][2] for N in range(13, 30) if N % 3]
    m = lambda x: sum(x) / len(x)
    assert abs(m(three) - 0.174) < 0.01 and abs(m(rest) - 0.025) < 0.01
    assert m(three) - m(rest) < 0.2 < math.log(3)                         # far short of Georgi-Jarlskog's log 3
    assert abs(m(r1three) - m(r1rest)) < 0.05                               # R1 does not move
    assert min(three) < 0                                                   # not systematic (order 27)


def test_an_order5_point_live():
    sys.path.insert(0, str(ROOT / "frontier" / "B1726_the_two_ingredients_replicated" / "verification"))
    import census as K
    r = K.compute(0.55, 3.05, Fr(1, 5), Fr(2, 5))
    for h in ("L_max", "L_2"):
        for rd in ("S", "St"):
            dn, lp = r["down|%s|%s" % (h, rd)], r["lep|%s|%s" % (h, rd)]
            assert max(abs(math.log(x / y)) for x, y in zip(dn, lp)) < 1e-8
