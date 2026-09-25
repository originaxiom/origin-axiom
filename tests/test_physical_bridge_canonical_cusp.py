"""R44 failable finite controls; not a certification of the analytic theorem."""
import importlib.util
from pathlib import Path

import pytest
import sympy as s

PATH=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/canonical_cusp.py'
spec=importlib.util.spec_from_file_location('r44_cusp',PATH)
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_literal_peripheral_conjugacy_and_projector():
    d=m.peripheral()
    assert d['meridian'] == m.I4+m.N0+m.P/2
    assert m.clean(d['longitude']-d['expected_longitude']) == s.zeros(4)
    assert d['pi_residual'] == s.zeros(4)
    assert d['det'] != 0
    num,den=s.fraction(d['det'])
    # Every positive exceptional root has q!=1; inspect all possible zeros/poles.
    assert set(s.solve(num,m.Q)) <= {0,1,-1}
    assert set(s.solve(den,m.Q)) <= {0,1,-1}


@pytest.mark.parametrize('q',[s.Rational(2),s.Rational(1,2),s.Rational(3),s.Rational(1,3)])
def test_exact_reciprocal_samples(q):
    d=m.peripheral(q)
    assert d['det'] != 0
    assert d['meridian'] == m.I4+m.N0+m.P/2
    assert d['longitude'] == d['expected_longitude']
    assert d['beta']/s.log(q)>0


def test_both_radial_transformations_and_wrong_sign():
    assert m.radial_changes() == (0,0)
    assert m.radial_changes(True)[0] == 0
    assert m.radial_changes(True)[1] != 0


def test_actual_SL_rescaling_and_generator_rates():
    a=m.rescaling()
    assert m.clean(a.det()) == 1
    assert m.clean(a*m.N0*a.inv()-m.N0/s.sqrt(m.R)) == s.zeros(4)
    assert m.clean(a*m.P*a.inv()-m.P/m.R) == s.zeros(4)
    assert m.clean(a*m.D*a.inv()-m.D) == s.zeros(4)
    assert m.clean(a*a.inv().diff(m.R)-m.J/m.R) == s.zeros(4)


@pytest.mark.parametrize('dual',[False,True])
def test_full_radial_flatness(dual):
    assert all(a == s.zeros(4) for a in m.connection(dual=dual)[3])
    assert any(a != s.zeros(4) for a in m.connection(omit_radial=True,dual=dual)[3])


def test_product_affine_sphere_MA_and_positivity():
    d=m.product_metric()
    assert d['ma_powers'] == (0,0)
    assert d['density_constant'] == s.Rational(27,2048)
    assert d['density_constant']*s.Rational(2048,27) == 1
    expected=s.Matrix([[s.Rational(15,64),-s.Rational(3,32),0],
                       [-s.Rational(3,32),s.Rational(3,16),0],
                       [0,0,s.Rational(3,8)]])
    assert d['point'] == expected
    assert all(d['point'][:j,:j].det()>0 for j in range(1,4))


def test_wrong_radial_exponent_fails_same_MA_equation():
    d=m.product_metric(s.Rational(1,2),s.Rational(1,4))
    assert d['ma_powers'] != (0,0)
    assert d['point'].det()>0  # Positivity alone is not the affine-sphere equation.


def test_base_scales_volume_and_nonshrinking_longitude():
    h=m.product_metric()['point']
    vectors=s.Matrix([[1/m.R,0,m.BETA/m.R],[0,0,-4*m.K],[0,1/s.sqrt(m.R),0]])
    pulled=m.clean(vectors.T*h*vectors)
    assert m.clean(pulled.det()*m.R**3-16*m.K**2*h.det()) == 0
    assert s.limit(pulled[2,2],m.R,s.oo) == 3*m.K**2
    assert s.integrate(m.R**(-s.Rational(3,2)),(m.R,1,s.oo)) == 2
    assert s.integrate(1/m.R,(m.R,1,s.oo)) == s.oo
    # Wrong shrink-all ansatz disagrees with the actual longitudinal limit.
    assert s.limit(1/m.R,m.R,s.oo) == 0


@pytest.mark.parametrize('dual',[False,True])
def test_fourier_inverse_both_sides_and_radial_commutator(dual):
    t,inv=m.fourier_inverse(dual)
    bx,bt,br,_=m.connection(dual=dual)
    assert m.clean(t*inv-m.I4) == s.zeros(4)
    assert m.clean(inv*t-m.I4) == s.zeros(4)
    assert m.clean(inv.diff(m.R)+m.comm(br,inv)) == s.zeros(4)
    assert m.clean(m.comm(bx,inv)) == s.zeros(4)


def test_q_one_and_zero_weight_controls_are_singular():
    t,_=m.fourier_inverse()
    assert t.subs({m.K:0,m.W:0}).det() == 0
    zero_weight=s.diag(0,-3,1,1)
    assert (m.K*zero_weight+m.BETA*m.P/m.R).det() == 0
    assert m.clean((m.K*m.D).det()) == -3*m.K**4


def test_unitary_frequency_does_not_close_semisimple_gap():
    for weight in (1,-3):
        squared=s.expand((s.I*m.W+m.K*weight)*(-s.I*m.W+m.K*weight))
        assert squared == m.W**2+(m.K*weight)**2
    for phase in (0,s.Rational(1,4),s.Rational(1,2),s.Rational(3,4)):
        t,_=m.fourier_inverse()
        assert t.subs({m.W:2*s.pi*phase,m.K:1,m.R:2,m.BETA:3}).det() != 0


def test_whole_exterior_cartan_not_torus_only():
    wedge,contract=m.exterior_operators()
    for a in range(3):
        for b in range(3):
            assert wedge[a]*contract[b]+contract[b]*wedge[a] == (s.eye(8) if a==b else s.zeros(8))
    assert wedge[0]*contract[2]+contract[2]*wedge[0] == s.zeros(8)
    assert contract[2].rank() == 4
