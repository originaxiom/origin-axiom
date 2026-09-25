"""R47 pre-execution finite controls with a nonzero/zero detector split."""
from pathlib import Path
import importlib.util

import sympy as s

path = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/neutral_tangent.py'
spec = importlib.util.spec_from_file_location('r47_neutral',path)
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)
q,R = v.q,v.R


def test_global_relator_and_composed_adjoint_tangent():
    hol,tangent = v.word_cocycle(v.RELATOR)
    assert hol == s.eye(4) and tangent == s.zeros(4)
    for word in ('mnM',v.LONGITUDE):
        hol,tangent = v.word_cocycle(word)
        direct = v.cc.prior.word(word,v.cc.prior.generators(q))
        assert v.cc.clean(hol-direct) == s.zeros(4)
        assert v.cc.clean(tangent-v.dot(direct)*direct.inv()) == s.zeros(4)


def test_trace_free_global_tangent():
    for a in v.cc.prior.generators(q):
        assert v.cc.clean(s.trace(v.dot(a)*a.inv())) == 0
    assert s.trace(v.tail_tangent()) == 0
    assert v.cc.clean(v.DOT_BETA+6*q*(q*q+1)/((q-1)**2*(q+1)**2)) == 0


def test_covariantly_closed_tail_and_radial_omission():
    assert all(a == s.zeros(4) for a in v.closure_residuals())
    assert v.closure_residuals(True)[1] != s.zeros(4)


def test_actual_longitude_detector_not_just_normal_form():
    data = v.literal_longitude_detector()
    assert data['parallel'] == s.zeros(4)
    assert data['pairing'] == 12
    assert v.cc.clean(data['trace_derivative']-3*(q-q**-3)) == 0
    assert s.factor(data['trace_derivative']) != 0
    # q=1 is the excluded normal-frame degeneration, not a uniform-q limit.
    assert s.factor(data['trace_derivative']).subs(q,1) == 0


def test_compact_dual_detector_and_covariant_closure():
    d = v.cc.D
    bx,bt,br,_ = v.cc.connection()
    assert all(v.cc.comm(a,d) == s.zeros(4) for a in (bx,bt,br))
    f = v.compact_profile()
    assert s.integrate(f,(R,1,2)) == 1
    for end in (1,2):
        assert f.subs(R,end) == 0 and s.diff(f,R).subs(R,end) == 0
    assert v.cc.clean(s.trace(v.tail_tangent()*d)) == 12
    assert s.trace(v.cc.P*d) == 0
    assert s.trace(s.zeros(4)*d) == 0


def test_pure_gauge_detector_and_nonperiodic_primitive_control():
    t = s.symbols('t',real=True)
    x = s.Matrix(4,4,s.symbols('x:16'))
    bt = v.cc.K*v.cc.D+v.cc.BETA*v.cc.P/R
    gauge_part = v.cc.comm(bt,x)
    assert v.cc.clean(s.trace(v.cc.D*gauge_part)) == 0
    periodic = s.sin(2*s.pi*t)
    assert s.integrate(s.diff(periodic,t),(t,0,1)) == 0
    forbidden = t*v.cc.D
    assert forbidden.subs(t,1)-forbidden.subs(t,0) == v.cc.D
    assert s.integrate(s.trace(v.cc.D*forbidden.diff(t)),(t,0,1)) == 12


def test_canonical_integrals_and_different_old_metric():
    b,r0,l2,l4,old = v.reference_integrals()
    assert v.cc.clean(l2-24/s.sqrt(r0)-2*b*b/(5*r0**s.Rational(5,2))) == 0
    assert v.cc.clean(l4-288/s.sqrt(r0)-48*b*b/(5*r0**s.Rational(5,2))
                      -2*b**4/(9*r0**s.Rational(9,2))) == 0
    assert l2.subs({b:1,r0:1}) > 0 and l4.subs({b:1,r0:1}) > 0
    assert old == s.oo


def test_projection_detector_model_in_both_directions():
    d0 = s.Matrix([[1],[0],[0]])
    d1 = s.Matrix([[0,0,1]])
    harmonic = s.Matrix([0,1,0])
    detector = 12*harmonic
    assert d1*d0 == s.zeros(1)
    assert d1*harmonic == s.zeros(1) and d0.T*harmonic == s.zeros(1)
    assert d0.T*detector == s.zeros(1)
    exact_projection = d0*(d0.T*d0).inv()*d0.T
    c = s.Matrix([3,1,0])
    alpha = (s.eye(3)-exact_projection)*c
    assert alpha == harmonic and detector.dot(alpha) == detector.dot(c) == 12
    assert (s.eye(3)-exact_projection)*d0 == s.zeros(3,1)


def test_received_generic_pairing_and_dual_inverse_identity():
    witness = v.pairing_witness()
    det = -q*(q*q+q+1)**3/(16*(q+1)**4)
    assert v.cc.clean(witness.det()-det) == 0
    for a in v.cc.prior.generators(q):
        assert v.cc.clean(a.T*witness-witness*a) == s.zeros(4)
        assert v.cc.clean(a.inv().T*witness-witness*a.inv()) == s.zeros(4)
        for phase in (1,-1,s.I,-s.I):
            twisted = phase*a
            assert v.cc.clean(twisted.inv().T*witness-witness*twisted.inv()) == s.zeros(4)
    for value in (s.Rational(1,2),s.Integer(2)):
        assert det.subs(q,value) < 0


def test_differentiated_pairing_requires_the_compensator():
    assert all(a == s.zeros(4) for a in v.pairing_residuals())
    assert any(a != s.zeros(4) for a in v.pairing_residuals(True))


def test_native_controls():
    result = v.run()
    assert result['all_checks_pass']
    assert not result['nonlinear_modulus_derived']
    assert not result['canonical_geometric_pairing_derived']
