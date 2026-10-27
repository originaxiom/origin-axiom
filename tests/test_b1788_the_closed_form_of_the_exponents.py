"""B1788 -- the closed form of the exponents.  The closed form e(m2/m3) = 1/2 - (||2 q_L a|| + ||2 q_R a||)/2 equals the
tropical minimum of Y's 2x2 minors over B1785's slopes and gives (3/10, 1/5, 1/5) on alpha = 2/5 and 1/10; the committed
census comparison (7 206 of 7 812 within 0.05) and W160's check (zero law 0 mismatches, the identity to 1e-10) as stated."""
import json, pathlib, sys
from fractions import Fraction as Fr
ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1788_the_closed_form_of_the_exponents" / "verification"
SIXY = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6}
SECTORS = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}


def nd(x):
    x = x % 1; return min(x, 1 - x)


def closed(sector, a):
    ql, qr = (SIXY[f] for f in SECTORS[sector]); return Fr(1, 2) - (nd(2 * ql * a) + nd(2 * qr * a)) / 2


def test_the_closed_form_values():
    for a in (Fr(2, 5), Fr(1, 10)):
        assert (closed("up", a), closed("down", a), closed("lep", a)) == (Fr(3, 10), Fr(1, 5), Fr(1, 5))
    # on 5 alpha in Z the up exponent is 1/2 - ||3 alpha|| (W160's branch)
    for k in range(5):
        a = Fr(k, 5); assert closed("up", a) == Fr(1, 2) - nd(3 * a)


def test_the_tropical_prediction_is_the_closed_form():
    sys.path.insert(0, str(V))
    import tropical as T
    P = {rd: T.polys(rd) for rd in ("S", "St")}
    for a in (Fr(2, 5), Fr(1, 10), Fr(1, 7), Fr(2, 11), Fr(1, 3)):
        for sec, (l, r) in SECTORS.items():
            mu = T.E(SIXY[l] * a, SIXY[r] * a)
            for rd in ("S", "St"):
                assert T.predict(P[rd], mu)[0] == closed(sec, a), (a, sec, rd)
    dm = json.loads((V / "domain.json").read_text(encoding="utf-8"))
    assert dm["tropical_vs_closed_mismatches"] == 0 and dm["tropical_vs_closed_cases"] == 3972
    assert dm["pair_3_10_1_5_alphas"] == ["1/10", "2/5"] and dm["excluded_outside_degeneracy"] == 16
    assert (dm["failing_m2m3_classes"], dm["failing_m2m3_cases"]) == (32, 474)


def test_the_blocks_and_the_channel_map():
    b = json.loads((V / "blocks.json").read_text(encoding="utf-8"))
    assert b["channel_map_line_sectors"] == 360 and max(b["channel_map_worst"].values()) < 1e-9
    assert b["off_by_more_than_0_02"] == 0 and b["blocks_fitted"] == 5724 and len(b["flagged"]) == 36


def test_the_40_digit_convergence():
    rows = json.loads((V / "highprec" / "compare_closed.json").read_text(encoding="utf-8"))
    for r in rows:
        if r["ratio"] == "m2/m3":
            assert -0.025 < r["diff"] <= 0.001, r
        elif r["line"] != ["2/11", "1/11"]:             # its last pair is below 40 digits (sigma3/sigma1 ~ e^-107)
            assert abs(r["diff"]) < 0.006, r


def test_the_closed_form_is_the_tropical_minimum():
    sys.path.insert(0, str(V))
    import tropical as T
    a_list = sorted({Fr(r["alpha"]) for r in json.loads((ROOT / "frontier" / "B1785_the_slope_sets_the_exponents" / "verification" / "exponents.json").read_text(encoding="utf-8"))})
    for a in a_list:
        for sec, (l, r) in SECTORS.items():
            mu = T.E(SIXY[l] * a, SIXY[r] * a)
            assert min(Fr(1, 2), (mu[0] + mu[3]) - 2 * min(mu)) == closed(sec, a), (a, sec)


def test_the_committed_comparisons():
    lines = (V / "classify_run.txt").read_text(encoding="utf-8").splitlines()
    tally = {l.rsplit(None, 1)[0].strip(): int(l.rsplit(None, 1)[1]) for l in lines[:5]}
    assert tally["CF ok"] + tally["DEG ok"] == 7206
    assert sum(tally.values()) - tally["DEG m1=0 (not compared)"] == 7812
    w = json.loads((V / "w160_check.json").read_text(encoding="utf-8"))
    assert w["zero_law"]["mismatches"] == {"up": 0, "down": 0}
    assert w["identity_worst_rel"] < 1e-10 and w["general_form_reduces_to_W160_on_5a_in_Z"] is True
