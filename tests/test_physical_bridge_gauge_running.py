"""Equation-level controls for the 2026-09-05 conditional physical bridge."""
from fractions import Fraction as F
import math

import numpy as np
import pytest

from reports.physical_bridge_2026_09_05.gauge_running import (
    SM_B, boundary_down, boundary_up, evolve, inverse_couplings,
    InvalidTrajectory, piecewise_one_loop)
from reports.physical_bridge_2026_09_05.spectrum import (
    ONE_FAMILY, HIGGS, D_PAIR, L_PAIR, SINGLET, Field, anomalies, beta,
    matter_beta, threshold_requirement)


def test_representation_content_and_standard_beta_control():
    assert sum(f.color_dim*f.weak for f in ONE_FAMILY) == 16
    assert sum(f.color_dim*f.weak for f in ONE_FAMILY+D_PAIR+L_PAIR+(SINGLET,)) == 27
    assert beta(ONE_FAMILY*3+(HIGGS,)) == (F(41,10), F(-19,6), F(-7))
    assert beta(()) == (0, F(-22,3), -11)
    # Independent known Dynkin indices, including representations outside the fit.
    assert Field("adjoint", (1,1), 1, 0).color_index == 3
    assert Field("sextet", (2,0), 1, 0).color_index == F(5,2)
    assert Field("spin1", (0,0), 3, 0).weak_index == 2


def test_anomaly_positive_and_negative_controls():
    assert all(v == 0 for v in anomalies(ONE_FAMILY).values())
    assert all(v == 0 for v in anomalies(D_PAIR+L_PAIR).values())
    assert anomalies(ONE_FAMILY[1:])["SU3_cubic"] == -2
    assert anomalies((ONE_FAMILY[3],))["SU2_global_mod2"] == 1
    # Scalars contribute to running, not to these fermion anomalies.
    assert anomalies((HIGGS,)) == anomalies(())


def test_hypercharge_conventions_have_the_expected_scaling():
    fields = ONE_FAMILY[:3]
    factor = F(7,3)
    rescaled = tuple(Field(f.name, f.color, f.weak, f.y*factor) for f in fields)
    before, after = anomalies(fields), anomalies(rescaled)
    for channel in ("SU3_squared_Y", "SU2_squared_Y", "gravity_Y"):
        assert after[channel] == before[channel]*factor
    assert after["Y_cubic"] == before["Y_cubic"]*factor**3
    assert matter_beta(rescaled, F(5,3)*factor**2) == matter_beta(fields)


def test_complete_multiplet_and_statistics_controls():
    assert matter_beta(D_PAIR) == (F(4,15), 0, F(2,3))
    assert matter_beta(L_PAIR) == (F(2,5), F(2,3), 0)
    assert matter_beta(D_PAIR+L_PAIR) == (F(2,3),)*3
    f = D_PAIR[0]
    scalar = Field(f.name, f.color, f.weak, f.y, "complex_scalar")
    assert matter_beta((f,)) == tuple(2*v for v in matter_beta((scalar,)))


@pytest.mark.parametrize("t", [0., 5., 20., 30.])
def test_one_loop_forward_boundary_has_closed_form(t):
    inv = 128.  # synthetic normalization, not a comparison datum
    p = boundary_down(t, inv, 1)
    # 5*x1/3+x2 = inv, x1-x2 = (b1-b2)t/(2pi).
    expected_x2 = 3/8*inv - 5/8*(SM_B[0]-SM_B[1])*t/(2*math.pi)
    expected_s = expected_x2/inv
    assert p.sin2theta == pytest.approx(expected_s, abs=1e-13)
    assert p.inv_alpha_em == pytest.approx(inv, abs=1e-11)
    assert max(abs(np.diff(evolve(p.inverse_ir, 0, t, loops=1)))) < 1e-11


@pytest.mark.parametrize("t", [20., 25., 30.])
def test_two_loop_boundary_satisfies_both_equations_and_reverse_solve(t):
    p = boundary_down(t, 128., 2)
    assert abs(p.inv_alpha_em-128.) < 1e-8
    end = evolve(p.inverse_ir, 0, t)
    assert max(abs(np.diff(end))) < 1e-7
    assert max(abs(end-p.inverse_uv)) < 1e-7
    for guess_as in (.07, .15):
        up = boundary_up(t, 128., guess=(p.sin2theta, guess_as))
        assert max(abs(up-p.observables)) < 1e-8


def test_nonmeeting_and_pole_controls_do_not_pass_as_solutions():
    p = boundary_down(25., 128., 2)
    wrong = list(p.inverse_ir)
    wrong[2] += 1
    assert max(abs(np.diff(evolve(wrong, 0, 25.)))) > .1
    with pytest.raises(InvalidTrajectory):
        evolve([1., 1., 1.], 0, 100, loops=1, b=[1., 1., 1.])
    with pytest.raises(InvalidTrajectory):
        evolve([float("nan"), 1., 1.], 0, 1)
    with pytest.raises(ValueError):
        boundary_down(1., 128., loops=3)


def test_piecewise_running_including_coincident_thresholds():
    x = np.array([60., 30., 9.])
    d, l = np.array(matter_beta(D_PAIR), float), np.array(matter_beta(L_PAIR), float)
    for td, tl in ((3.,3.), (3.,7.), (0.,12.), (12.,0.)):
        numerical = piecewise_one_loop(x, 12., [(td,d), (tl,l)])
        exact = x-(SM_B*12+d*(12-td)+l*(12-tl))/(2*math.pi)
        assert max(abs(numerical-exact)) < 1e-12
    for tm in (0.,4.,12.):
        with_multiplet = piecewise_one_loop(x, 12., [(tm,d), (tm,l)])
        without = evolve(x, 0, 12., loops=1)
        assert max(abs(np.diff(with_multiplet)-np.diff(without))) < 1e-12
    with pytest.raises(ValueError):
        piecewise_one_loop(x, 12., [(-1.,d)])


def test_threshold_inverse_recovers_a_planted_positive_with_independent_formula():
    # Plant a genuinely unified model, then infer its two difference parameters.
    t, td, tl, n, uv = 25., 15., 5., 2, 40.
    d, l = np.array(matter_beta(D_PAIR), float), np.array(matter_beta(L_PAIR), float)
    ir = np.repeat(uv,3)+(SM_B*t+n*d*(t-td)+n*l*(t-tl))/(2*math.pi)
    got_t, got_r = threshold_requirement(ir, SM_B, d)
    assert got_t == pytest.approx(t, abs=1e-12)
    assert got_r == pytest.approx(n*(tl-td), abs=1e-11)
    # Same target cannot be met by one copy with thresholds in [0,t] if |r|>t.
    impossible_ir = np.repeat(uv,3)+(SM_B*t+d*(-2*t))/(2*math.pi)
    other_t, other_r = threshold_requirement(impossible_ir, SM_B, d)
    assert abs(other_r) > other_t
