"""R46 pre-execution discriminating controls; no global-proof test claim."""
import importlib.util
from pathlib import Path

import pytest
import sympy as s

path = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/canonical_interaction.py'
spec = importlib.util.spec_from_file_location('r46_interaction',path)
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)
R = v.R


@pytest.mark.parametrize('kind',v.KINDS)
def test_two_sided_meridian_inverse_and_full_radial_covariance(kind):
    t,ti = v.meridian_inverse(kind)
    assert v.cc.clean(t*ti-s.eye(t.rows)) == s.zeros(t.rows)
    assert v.cc.clean(ti*t-s.eye(t.rows)) == s.zeros(t.rows)
    assert all(a == s.zeros(t.rows) for a in v.covariance(kind))
    j = v.pc.operators(kind)[3]
    assert v.cc.clean(v.cc.comm(j/R,ti)) != s.zeros(t.rows)


@pytest.mark.parametrize('kind',v.KINDS)
def test_zero_frequency_is_a_real_failure_not_a_small_gap(kind):
    n = v.pc.operators(kind)[1]
    assert n.det() == 0 and n**3 == s.zeros(n.rows)
    with pytest.raises(ValueError):
        v.meridian_inverse(kind,0)
    with pytest.raises(ValueError):
        v.bound(kind,0)


def test_complete_exterior_Cartan_identity_and_missing_derivative_control():
    assert v.full_cartan() == s.zeros(32)
    assert v.full_cartan(omit_derivative=True) != s.zeros(32)
    wedge,interior = v.cc.exterior_operators()
    for i in range(3):
        assert wedge[i]*interior[1]+interior[1]*wedge[i] == (s.eye(8) if i==1 else s.zeros(8))


def test_frequency_gap_and_actual_exterior_square_character():
    assert [v.frequency_gap(a) for a in range(4)] == [0,s.pi/2,s.pi,s.pi/2]
    assert v.frequency_gap(-1) == v.frequency_gap(1)
    assert v.frequency_gap(4) == 0
    m,_ = v.cc.prior.generators(s.S(2))
    for phase in (1,-1,s.I,-s.I):
        assert v.pc.group_action('6',phase*m) == phase**2*v.pc.group_action('6',m)
    assert s.I**2 == -1 and (-1)**2 == 1


@pytest.mark.parametrize('kind',v.KINDS)
def test_meridian_decay_does_not_upgrade_untwisted_longitude(kind):
    for exponent in (1,2,3):
        assert s.limit(v.bound(kind,exponent),R,s.oo) == 0
        assert s.limit(s.sqrt(R)*v.bound(kind,exponent),R,s.oo) == 1/v.frequency_gap(exponent)
    assert v.comparison_metric()[2,2] == 1


def test_canonical_volume_gradient_and_L2_not_L4():
    metric = v.comparison_metric()
    assert s.sqrt(metric.det()) == R**(-s.Rational(3,2))
    assert s.integrate(s.sqrt(metric.det()),(R,1,s.oo)) == 2
    power = s.Rational(3,16)
    assert s.integrate(R**(2*power-s.Rational(3,2)),(R,1,s.oo)) == 8
    assert s.integrate(R**(4*power-s.Rational(3,2)),(R,1,s.oo)) == s.oo
    eps,A = s.symbols('eps A',positive=True)
    f = s.exp(eps*s.sqrt(R))
    assert s.simplify(metric.inv()[0,0]*s.diff(f,R)**2/f**2) == eps**2*R/4
    assert s.simplify((2*A*eps**2).subs(eps,1/(2*s.sqrt(A)))) == s.Rational(1,2)
    assert s.limit(R**s.Rational(3,4)*s.exp(-eps*s.sqrt(R)),R,s.oo) == 0


def test_Clifford_IMS_controls_on_all_degrees():
    wedge,interior = v.cc.exterior_operators()
    x = s.symbols('x:3',real=True)
    c = sum((a*(w-i) for a,w,i in zip(x,wedge,interior)),s.zeros(8))
    assert v.cc.clean(c.T*c-sum(a*a for a in x)*s.eye(8)) == s.zeros(8)
    t = s.symbols('t',real=True)
    pair = (s.cos(t),s.sin(t))
    assert s.simplify(sum(a*a for a in pair)) == 1
    assert s.simplify(sum(a*s.diff(a,t) for a in pair)) == 0


def test_nonzero_profile_need_not_generate_source():
    profile,sources = v.rank_one_sources()
    assert profile != s.zeros(4,3)
    assert all(a == s.zeros(4) for a in sources)


def test_native_controls():
    assert v.run()['all_checks_pass']
