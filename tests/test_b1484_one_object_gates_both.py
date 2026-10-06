"""B1484 -- the unification ratio by field content and the triplet's weights: recomputed live."""
import json, os, subprocess, sys
from fractions import Fraction as F
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = os.path.join(ROOT, "frontier", "B1484_one_object_gates_both_nearest_approaches", "verification")


def test_the_coefficients_come_from_the_field_content_and_the_ratios_follow():
    out = subprocess.run([sys.executable, os.path.join(V, "unification_ratio.py")], capture_output=True, text=True); assert out.returncode == 0, out.stderr[-400:]
    d = json.load(open(os.path.join(V, "unification_ratio.json"))); s = d["spectra"]
    assert s["the Standard Model, a desert (B915)"]["b"] == ["41/10", "-19/6", "-7"] and s["the Standard Model, a desert (B915)"]["B"] == "115/218"
    k = "supersymmetric; Higgs doublets light, colour triplets heavy"; assert s[k]["b"] == ["33/5", "1", "-3"] and s[k]["B"] == "5/7"
    assert s["supersymmetric; three complete 27s light"]["B"] == "1/2" and s["supersymmetric; one light Higgs pair AND one light colour-triplet pair (one complete 5 + 5bar)"]["B"] == "1/2"
    assert abs(d["measured"]["B"] - 0.7172) < 5e-4 and abs(s[k]["alpha_s_implied"] - 0.1168) < 5e-4
    assert d["complete_multiplets"]["equal"] and d["weights"]["w_D_is_minus_two_w_Q"] and d["weights"]["H_u_and_D_differ_only_in_Y"]


def test_the_ratio_can_tell_spectra_apart():
    r = lambda b: (b[1] - b[2]) / (b[0] - b[1])
    assert r((F(41, 10), F(-19, 6), F(-7))) != r((F(33, 5), F(1), F(-3))) and abs(float(r((F(33, 5), F(1), F(-3)))) - 0.7172) < 0.004 < abs(float(r((F(7), F(1), F(-2)))) - 0.7172)
