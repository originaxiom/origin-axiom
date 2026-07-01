"""B330 / S032-A -- the no-forced-choice capstone via Galois symmetrization. sympy-only."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..',
                                'frontier', 'B330_s032a_galois_symmetrization'))
import sympy as sp
from s032a_galois import (golden_orbit_symmetrizable, eisenstein_cp_orbit_symmetrizable,
                          torsion_no_forced_choice, kappa_is_continuous)


def test_golden_orbit_symmetrizable():
    s, p, ok = golden_orbit_symmetrizable()
    assert s == 1 and p == -1 and ok            # symmetric fns rational -> canonical


def test_eisenstein_cp_orbit_symmetrizable():
    s, p, ok = eisenstein_cp_orbit_symmetrizable()
    assert s == sp.sqrt(3) and p == 1 and ok    # CP-sign pair -> real symmetric data


def test_cover_torsion_no_forced_choice():
    det_C_minus_I, fixed = torsion_no_forced_choice()
    assert sp.gcd(det_C_minus_I, 4) == 1        # (C-I) invertible mod 4
    assert fixed == [(0, 0)]                     # only the zero fixed vector -> no distinguished sub-object


def test_kappa_continuous_fails_multivalued_clause():
    assert kappa_is_continuous()                 # kappa varies continuously -> not discretely multivalued
