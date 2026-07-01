"""B346 -- the cross-structure map: symplectic = Z/3 conjugation (linked); E6-exponent independent. sympy-only."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B346_cross_structure_map'))
from cross_structure_map import symplectic_equals_charge_conjugation, e6_exponent_independent_of_charge


def test_symplectic_equals_z3_charge_conjugation():
    assert symplectic_equals_charge_conjugation()       # lambda->1/lambda == charge c->-c mod 3 (links B344, B345)


def test_e6_exponent_is_an_independent_grading():
    assert e6_exponent_independent_of_charge()           # B265 split not graded by Z/3 -> third independent structure
