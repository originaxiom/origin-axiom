"""B339 / H107 -- CS(1,n) sub-leading = rational 1/24, no sqrt(-3). Recorded values; numpy-only."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B339_cs_flow_subleading'))
from cs_flow_subleading import (leading_law_holds, even_coefficients_vanish,
                               c3_is_rational_1_over_2h, C3, TAU_SQ)


def test_leading_and_even_vanish():
    assert leading_law_holds()                # CS(1,n)*n -> -1/2
    assert even_coefficients_vanish()          # c_even = 0 (amphichirality: CS(1,-n) = -CS(1,n))


def test_c3_is_rational_no_sqrt3():
    assert c3_is_rational_1_over_2h()          # c3 = 1/24 = 1/(2 h(E6)); rational -> no sqrt(-3)
    assert TAU_SQ == 12 and C3 == 1.0 / 24     # |tau|^2 = h(E6) = 12
