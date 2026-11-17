"""B1949's lock: R1 (exact proportional-charge identity), R2 (exponents, a sample of slopes), R3 (levels 10 and 15), and
R4's committed limits (order 10's reciprocal pair, order 5's copy)."""
import sys, json, pathlib
from fractions import Fraction as Fr
from math import gcd
from collections import Counter
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1945_*")) / "verification"))
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1788_*")) / "verification"))
import determinant_law as DL
import tropical as T


def test_r1_the_leptons_at_w_are_the_doublet_negated_down_at_3w():
    DL.B.SIXY["X"] = -1; DL.B.SECTORS["dneg"] = ("X", "d")
    a, b = Fr(1, 10), Fr(3, 10)
    _, _, Yl, *_ = DL.parts("0.13", 1.7, a, b, "lep"); _, _, Yx, *_ = DL.parts("0.13", 1.7, 3 * a, 3 * b, "dneg")
    _, _, Yd, *_ = DL.parts("0.13", 1.7, 3 * a, 3 * b, "down")
    assert max(abs(Yl["S"][i, j] - Yx["S"][i, j]) for i in range(3) for j in range(3)) < 1e-25
    assert max(abs(Yl["S"][i, j] - Yd["S"][i, j]) for i in range(3) for j in range(3)) > 1e-3     # the down sector itself differs


def test_r2_and_r3_on_the_closed_form():
    P = {rd: T.polys(rd) for rd in ("S", "St")}
    ex = lambda ql, qr, a, rd: T.predict(P[rd], T.E(ql * a, qr * a))
    for den in (7, 10, 12, 15, 30):
        for num in range(den):
            a = Fr(num, den)
            for rd in ("S", "St"):
                assert ex(-3, 6, a, rd) == ex(1, 2, 3 * a, rd)
    pts = lambda N: [Fr(i, N) for i in range(N) for j in range(N) if N // gcd(gcd(i, j), N) == N]
    for rd in ("S", "St"):
        assert Counter(ex(-3, 6, a, rd) for a in pts(10)) == Counter(ex(1, 2, a, rd) for a in pts(10))
        assert Counter(ex(-3, 6, a, rd) for a in pts(15)) != Counter(ex(1, 2, a, rd) for a in pts(15))


def test_r4_committed_limits():
    d = json.loads((HERE / "r4_gj_factor.json").read_text())
    assert abs(d["5|S|28.0"]["ratio"][0] - 1) < 1e-12 and abs(d["5|St|28.0"]["ratio"][1] - 1) < 1e-12
    s, t = d["10|S|28.0"]["ratio"][0], d["10|St|28.0"]["ratio"][0]
    assert abs(s * t - 1) < 1e-4 and abs(s - 0.634644) < 1e-5
    assert abs(d["10|S|22.0"]["ratio"][0] - s) < 1e-5          # free of the height
    assert d["15|S|28.0"]["ratio"][0] < 0.1 * d["15|S|16.0"]["ratio"][0]   # order 15 has no constant


def test_r5_at_order_10_the_leptons_take_the_down_ratios_of_the_other_reading_in_the_cusp():
    d = json.loads((HERE / "r4_gj_factor.json").read_text())
    a, b = d["10|S|28.0"], d["10|St|28.0"]
    assert abs(a["lep"][0] / b["down"][0] - 1) < 1e-5 and abs(b["lep"][0] / a["down"][0] - 1) < 1e-5
    assert abs(a["lep"][0] / a["down"][0] - 1) > 0.3          # and not the same reading's
