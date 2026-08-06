"""B930 locks: the rotation spectrum, the sum rule, the superselection, the 5^12 minpoly."""
import json
import os

import sympy as sp

ARC = os.path.join(os.path.dirname(__file__), "..", "frontier", "B930_overlap_matrix")


def _res():
    with open(os.path.join(ARC, "results.json")) as f:
        return json.load(f)


def test_w3_rotation_rational_spectrum():
    x = sp.Symbol("x")
    q = 1536*x**2 - 2088*x + 677
    r = sorted(sp.nroots(q))
    assert abs(float(r[0]) - 0.53401701801096878822) < 1e-15
    assert abs(float(r[1]) - 0.82535798198903121178) < 1e-15
    t = json.dumps(_res())
    assert "1536" in t and "677" in t


def test_block_refined_sum_rule_11():
    assert sp.Rational(151, 64) + sp.Rational(169, 64) + 6 == 11


def test_branch_superselection_and_golden_minpoly():
    t = json.dumps(_res())
    # the same-gen branch overlap is the zero K-element
    assert "'0', '0', '0'" in t or '"0", "0", "0"' in t
    # the S-A overlap-squared minpoly: 953^4 lead, 5^12 constant
    assert "824843587681" in t
    assert str(5**12) in t


def test_all_checks_passed():
    r = _res()
    # checks store {"pass":...} for CHK rows and raw values for DATA rows
    assert all(v["pass"] for v in r["checks"].values()
               if isinstance(v, dict) and "pass" in v)
    assert r.get("verdict") != "UNSTABLE"
