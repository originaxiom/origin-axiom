"""Locks for B436 -- the child's identity card (C1)."""
import json, os
import sympy as sp

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B436_child_identity")
R = json.load(open(os.path.join(HERE, "identity.json")))
x = sp.Symbol('x')

def test_field_facts():
    P = x**4 - x - 1
    assert sp.discriminant(P, x) == -283
    # signature (2,1): 2 real roots, one complex pair
    rr = sp.Poly(P, x).count_roots()      # real roots
    assert rr == 2

def test_borel_identity_banked():
    assert float(R["borel_ratio_minus_12_abs"].replace("e-64", "")) < 10
    assert "4.52e-64" == R["borel_ratio_minus_12_abs"]        # exact-to-63-digits record
    assert R["child_field"].startswith("x^4 - x - 1")

def test_registered_outcomes_honest():
    assert "not identified" in R["cs_small_rational"]         # CS: no forcing
    assert "degree 14" in R["sibling_7_field_degree"]         # control: sibling generic
