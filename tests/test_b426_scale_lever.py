"""Locks for B426 -- the scale-lever closed form + the Galois-orbit contraction theorem."""
import json, os, sys
from fractions import Fraction as F
import sympy as sp

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B426_scale_lever_closed_form")
sys.path.insert(0, HERE)
import closed_form as CF

R = json.load(open(os.path.join(HERE, "closed_form.json")))


def test_sector_coefficients_match_banked_sweep():
    # the (4,8) sqrt-15 sector from the banked B372 exact JSON
    assert CF.sector_48() == (F(1, 96), F(-1, 160), F(1, 480))


def test_exhaustive_max_at_4_8_embedding_2():
    v, cell, emb = CF.exhaustive_max()
    assert cell == "4,8" and emb == 2
    assert abs(abs(v) - 0.0253546762728196) < 1e-15


def test_closed_form_and_minpoly():
    r, resid, mp_r = CF.ratio_closed_form()
    assert resid == 0                                   # ratio == (3A^2+4A-1)/10 exactly
    x = sp.Symbol('x')
    assert sp.expand(mp_r - (1000*x**3 - 1500*x**2 + 360*x - 19)) == 0


def test_galois_orbit_contraction():
    inv = CF.galois_orbit_invariants()
    assert inv["mean"] == sp.Rational(1, 2)
    assert sp.simplify(inv["rms"] - sp.sqrt(51)/10) == 0
    assert inv["all_below_one"] is True                 # every invariant functional contracts


def test_sqrt5_free_field():
    # the ratio's field is the cyclic cubic Q(zeta9)+ (disc 3^4) -- no sqrt5
    A = sp.Symbol('A')
    d = sp.factorint(sp.discriminant(A**3 - 3*A + 1, A))
    assert d == {3: 4}
