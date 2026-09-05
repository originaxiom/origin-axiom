"""Equation-level controls for the explicitly post-R1/R2 mass extension."""
from fractions import Fraction as F
import json
import math

import numpy as np
import pytest

from reports.physical_bridge_2026_09_05.gauge_running import SM_B, evolve
from reports.physical_bridge_2026_09_05.mass_match import (
    alpha_integrals, casimirs, common_uv_upper_bound, log_mass_enhancement,
    mass_block_check)
from reports.physical_bridge_2026_09_05.spectrum import D_PAIR, L_PAIR, matter_beta


def test_singlet_and_split_mass_spaces_are_computed():
    result = mass_block_check()
    assert result["SU5_commutant_dimension"] == 1
    assert result["SM_commutant_dimension"] == 2
    assert result["split_mass_control_rejected_by_SU5"]


def test_mass_beta_uses_casimirs_not_spectator_weighted_indices():
    assert casimirs(D_PAIR[0]) == (F(1,15), 0, F(4,3))
    assert casimirs(L_PAIR[0]) == (F(3,20), F(3,4), 0)
    # The familiar color-fundamental gauge coefficient is 6 C_F = 8.
    assert 6*casimirs(D_PAIR[0])[2] == 8


def test_integrals_include_zero_beta_control_and_correct_direction():
    x, start, end = np.array([60.,30.,10.]), 2., 12.
    analytical, numerical = alpha_integrals(x, end, [], start=start, baseline=[0.,0.,0.])
    assert analytical == pytest.approx((end-start)/x, abs=1e-12)
    assert numerical == pytest.approx(analytical, abs=1e-12)
    expected = 6*sum(float(c)/xx for c,xx in zip(casimirs(D_PAIR[0]),x))*(end-start)/(4*math.pi)
    assert log_mass_enhancement(analytical,D_PAIR[0]) == pytest.approx(expected, abs=1e-12)
    assert expected > 0  # A gauge-only mass increases when evolved down.


@pytest.mark.parametrize("start", [0.,3.,9.,20.])
def test_piecewise_integrals_agree_with_independent_quadrature(start):
    d, l = np.array(matter_beta(D_PAIR),float), np.array(matter_beta(L_PAIR),float)
    for thresholds in ([], [(3.,d),(9.,l)], [(3.,d),(3.,l)], [(0.,d),(20.,l)]):
        analytical, numerical = alpha_integrals([60.,30.,10.], 20., thresholds, start=start)
        assert analytical == pytest.approx(numerical, abs=2e-11)
        assert (analytical >= 0).all()


def test_uniform_bound_covers_extreme_thresholds_with_a_nonvacuous_control():
    x, t = np.array([60.,30.,10.]), 25.
    d, l = np.array(matter_beta(D_PAIR),float), np.array(matter_beta(L_PAIR),float)
    for n in (1,2,3):
        upper = common_uv_upper_bound(x,t,n)["per_pair_log_MD_over_ML_upper_bound"]
        for td,tl in ((0.,0.),(0.,t),(t,0.),(.3*t,.7*t),(t,t)):
            thresholds = [(td,n*d),(tl,n*l)]
            ad,_ = alpha_integrals(x,t,thresholds,start=td)
            al,_ = alpha_integrals(x,t,thresholds,start=tl)
            generated = log_mass_enhancement(ad,D_PAIR[0])-log_mass_enhancement(al,L_PAIR[0])
            assert generated <= upper+1e-12
        # A weak target is NOT excluded by this bound; it is not an always-fail rule.
        assert 0 < upper/2 < upper
    assert common_uv_upper_bound([1.,30.,10.],100.,3) is None
    with pytest.raises(ValueError):
        common_uv_upper_bound(x,t,4)


def test_single_interval_integral_has_independent_closed_form():
    x, t = np.array([60.,30.,10.]), 25.
    got,_ = alpha_integrals(x,t,[])
    endpoint = evolve(x,0,t,loops=1)
    expected = -2*math.pi/SM_B*np.log(endpoint/x)
    assert got == pytest.approx(expected,abs=1e-12)


def test_bound_and_its_decision_are_json_serializable():
    upper = common_uv_upper_bound(np.array([60.,30.,10.]),25.,3)
    report = {"bound":upper, "excluded":upper["sum_log_MD_over_ML_upper_bound"] < 40.}
    restored = json.loads(json.dumps(report,allow_nan=False))
    assert restored == report and restored["excluded"] is True
