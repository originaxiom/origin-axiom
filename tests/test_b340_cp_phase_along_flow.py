"""B340 / H108 -- the CP phase kappa along the flow, extremal at the amphichiral point. Recorded; numpy."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B340_cp_phase_along_flow'))
from cp_phase_along_flow import (cusp_is_extremal_cp_phase, chirality_lowers_the_phase,
                                deviation_is_second_order)


def test_cusp_is_extremal_cp_phase():
    assert cusp_is_extremal_cp_phase()          # arg=pi/6, |kappa|=sqrt3, CS=0 at the cusp (B285)


def test_chirality_deforms_the_phase_at_second_order():
    assert chirality_lowers_the_phase()          # arg(kappa) down, |kappa| up as |CS| grows
    assert deviation_is_second_order()           # (pi/6 - arg kappa) ~ CS^2
