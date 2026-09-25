"""R45 finite mathematical controls, not a certificate of the global proof."""
import importlib.util
from pathlib import Path

import pytest
import sympy as s

spec = importlib.util.spec_from_file_location('r45_test',Path(__file__).parents[1]
    /'reports/physical_bridge_2026_09_05/parent_cusp.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_complete_actual_parent_weights_and_wrong_bar_control():
    b = m.pb.branching()
    assert b['actual'] == b['expected'] != b['wrong']
    expected = {-4:3,-3:16,-2:30,-1:48,0:54,1:48,2:30,3:16,4:3}
    assert m.full_weights() == m.direct_root_weights() == expected
    assert sum(expected.values()) == 248 and b['trace_ratio'] == 60


@pytest.mark.parametrize('kind',m.KINDS)
def test_actual_lie_invariants_not_dimension_matching(kind):
    assert m.lie_invariants()[kind] == 0
    d = m.operators(kind)[0].rows
    assert len(m.pb.common_kernel((s.zeros(d),))) == d


@pytest.mark.parametrize('q',(s.S(2),s.Rational(1,2)))
def test_literal_generator_common_invariants(q):
    assert m.literal_invariants(q) == dict.fromkeys(m.KINDS,0)


def test_different_geometric_fours_are_not_identified():
    e,f,h = m.pb.generators()
    assert len(m.pb.common_kernel(tuple(m.pb.exterior_action(x) for x in (e,f,h)))) == 1
    actual,_ = m.cc.prior.generators(s.S(1))
    nil = actual-s.eye(4)
    assert nil**3 == s.zeros(4) and nil**2 != s.zeros(4)
    assert e**4 == s.zeros(4) and e**3 != s.zeros(4)


@pytest.mark.parametrize('kind',m.KINDS)
def test_entire_radial_connection_and_two_sided_inverse(kind):
    assert all(x == s.zeros(x.rows) for x in m.flat_residuals(kind))
    t,ti = m.inverse(kind)
    assert m.cc.clean(t*ti-s.eye(t.rows)) == s.zeros(t.rows)
    assert m.cc.clean(ti*t-s.eye(t.rows)) == s.zeros(t.rows)
    d,n,p,j = m.operators(kind)
    assert n != s.zeros(n.rows)
    omitted = (n/s.sqrt(m.cc.R)).diff(m.cc.R)
    assert omitted != s.zeros(n.rows)


def test_zero_weight_cannot_use_the_defining_inverse():
    with pytest.raises(ValueError,match='zero longitudinal weight'):
        m.inverse('15',include_zero=True)
    z = m.zero_sector()
    assert z['dimension'] == 9 and z['longitude_rank'] == 4
    assert z['longitude_nilpotent']


def test_zero_sector_log_and_actual_holonomy_complexes():
    z = m.zero_sector()
    for key in ('log','exp'):
        assert z[key]['ranks'] == (6,6) and z[key]['dims'] == (3,6,3)
        assert z[key]['chain']
    assert z['invariants_rank'] == 3 and z['invariants_killed']
    assert [a+45*b for a,b in zip(z['log']['dims'],(1,2,1))] == [48,96,48]
    trivial = m.koszul(s.zeros(9),s.zeros(9))
    assert trivial['dims'] == (9,18,9) != z['log']['dims']


def test_peripheral_invariants_are_radially_parallel_and_L2_on_tail():
    residuals,powers = m.parallel_controls()
    assert all(x == s.zeros(4) for row in residuals for x in row)
    assert powers == [-s.Rational(3,2),-s.Rational(5,2),-s.Rational(7,2)]
    assert all(a < -1 for a in powers)
    assert m.cc.comm(m.cc.J,m.cc.N0) != s.zeros(4)


def test_trivial_longitude_and_meridian_have_different_norm_integrals():
    r = s.symbols('r',positive=True)
    longitude = s.integrate(r**(-s.Rational(3,2)),(r,1,s.oo))
    meridian = s.integrate(r**(-s.Rational(1,2)),(r,1,s.oo))
    assert longitude == 2 and meridian == s.oo


@pytest.mark.parametrize('chi',(s.S(1),s.S(-1),s.I,-s.I))
def test_only_declared_central_characters_are_admitted(chi):
    actual,_ = m.cc.prior.generators(s.S(2))
    assert s.simplify((chi*actual).det()) == 1
    assert m.group_action('15',chi*actual) == m.group_action('15',actual)
    assert m.cc.clean(m.group_action('6',chi*actual)-chi**2*m.group_action('6',actual)) == s.zeros(6)
    assert s.simplify((s.exp(s.I*s.pi/3)*actual).det()-1) != 0
