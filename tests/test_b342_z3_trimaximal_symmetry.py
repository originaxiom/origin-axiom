"""B342 -- abstract Z/3 = trimaximal symmetry + honest data comparison (physics firewalled to S048). numpy."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B342_z3_trimaximal_symmetry'))
from z3_trimaximal_symmetry import (z3_dft_is_democratic, magic_column_is_z3_invariant,
                                    theta12_from, data_favours_tm1)


def test_z3_is_the_trimaximal_symmetry():
    assert z3_dft_is_democratic()               # |entry|^2 = 1/3
    assert magic_column_is_z3_invariant()        # (1,1,1)/sqrt3 = Z/3-invariant = TBM middle column


def test_honest_data_comparison_favours_tm1():
    # the check Chat-2 skipped: current data favours TM1 over the object's would-be TM2
    fav, tm1, tm2 = data_favours_tm1()
    assert fav                                   # |TM1 - obs| < |TM2 - obs|
    assert abs(theta12_from('TM2') - 35.72) < 0.1 and abs(theta12_from('TM1') - 34.34) < 0.1
