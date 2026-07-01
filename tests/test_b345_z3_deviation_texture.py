"""B345 -- the Z/3-graded deviation texture (forced charge-conservation selection rule). sympy-only."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B345_z3_deviation_texture'))
from z3_deviation_texture import deviation_charges, selection_rule, exponent_split_aligns_with_charge


def test_deviation_carries_z3_charges():
    assert deviation_charges() == {0, 1, 2}             # modes {1, omega, omega^2}


def test_charge_conservation_texture():
    allowed, forbidden = selection_rule()
    assert allowed == [(0, 0), (1, 2), (2, 1)]          # anti-diagonal = omega-circulant (B324)
    assert (1, 1) in forbidden and (0, 1) in forbidden


def test_z3_independent_of_e6_exponent_split():
    assert exponent_split_aligns_with_charge() is False  # B265 split not separated by Z/3 charge -> independent
