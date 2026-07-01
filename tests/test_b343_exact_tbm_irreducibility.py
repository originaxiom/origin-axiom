"""B343 -- the object forces EXACT TBM (not TM2), irreducibility is why (Chat-2, verified). sympy/numpy."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B343_exact_tbm_irreducibility'))
from exact_tbm_irreducibility import (two_torsion_is_klein, deck_z3_cycles_the_three_z2s,
                                      T_does_not_normalize_neutrino_klein, full_klein_gives_exact_tbm)


def test_klein_and_irreducible_z3_action():
    assert two_torsion_is_klein()                       # 2-torsion of (Z/4)^2 = Klein Z2xZ2
    assert deck_z3_cycles_the_three_z2s()               # Z/3 3-cycles them, fixes none (Phi_3 mod 2 irred)


def test_charged_lepton_z3_does_not_select_a_column():
    assert T_does_not_normalize_neutrino_klein()        # T does not fix a neutrino Z2 (B342 conflation fixed)


def test_full_klein_gives_exact_tbm_theta13_zero():
    t13_zero, s12_third = full_klein_gives_exact_tbm()
    assert t13_zero and s12_third                        # exact TBM, theta13=0 (excluded), sin^2 th12=1/3
