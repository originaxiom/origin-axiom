"""F19 exact identities AND excluded-point-aware specialization certificates."""
from pathlib import Path
import importlib.util
import pytest
import sympy as s

spec=importlib.util.spec_from_file_location('f19_test_producer',Path(__file__).with_name('verify.py'))
a=importlib.util.module_from_spec(spec); spec.loader.exec_module(a)
p,v,q,K=a.p,a.v,a.q,a.K


def test_literal_family_not_projective_rescaling():
    rho=a.generators(); one=v.eye(4,K)
    assert all(g.det()==K.one for g in rho)
    assert (p.word(p.REL,rho)-one).is_zero_matrix
    for g in rho:
        b=g-one
        assert (b*b*b*b).is_zero_matrix
    lam=p.word(p.LONG,rho)
    diff=s.trace(lam.to_Matrix())-s.trace(lam.inv().to_Matrix())
    assert s.cancel(diff+(q-1/q)**3)==0
    assert a.domain_certificate(diff)['valid']


@pytest.mark.parametrize('name',['theta','thetaT'])
def test_generic_primitive_witness_and_every_positive_specialization(name):
    c=a.intertwiner(name)
    assert c['dimension']==1 and c['equations'].rank()==15
    assert all(r.is_zero_matrix for r in c['residuals'])
    assert all(s.Poly(x,q,domain=s.QQ) is not None for x in c['matrix'])
    assert c['domain']['valid']
    for middle in (14,34):
        for embedding in (-1,1):
            jj=a.specialize(c['matrix'],middle,embedding); k=jj.domain
            old=p.base_intertwiner(middle,name,embedding)[0]
            scalar=jj.inv()*old; first=scalar.to_list()[0][0]
            assert first!=k.zero
            assert (scalar-v.eye(4,k).scalarmul(first)).is_zero_matrix


def test_full_algebra_determinant_has_no_hidden_positive_exception():
    c=a.word_algebra()
    assert c['column'].shape==(16,16) and c['domain']['valid']
    for value in (s.Rational(1,2),s.Rational(3,2),s.Integer(2)):
        rho=v.f10.generators(value); columns=[]
        for w in p.BASIS_WORDS:
            g=s.eye(4)
            for letter in w: g=g*rho['mn'.index(letter)]
            columns.append(g.reshape(16,1))
        independent=s.Matrix.hstack(*columns)
        assert independent.det()==s.cancel(c['determinant'].subs(q,value))!=0
        independent[:,15]=independent[:,0]
        assert independent.det()==0
    for middle in (14,34):
        for embedding in (-1,1):
            k,value,_,_=v.context(middle,embedding)
            expected=k.from_sympy(c['determinant'].subs(q,value))
            assert expected==p.matrix_algebra_determinant(middle,embedding)!=k.zero


def test_peripheral_frame_at_every_allowed_parameter():
    c=a.peripheral()
    assert c['domain']['valid'] and c['finite']['valid']
    assert all(r.is_zero_matrix for r in c['residues'])
    assert a.domain_certificate(6/(q-1/q))['denominator']['excluded_multiplicities']['1']==1


def test_root_and_pole_detector_rejects_counterexamples():
    assert a.domain_certificate((q-1)**2/q)['valid']
    assert a.domain_certificate(q*q+q+1)['valid']
    assert not a.domain_certificate((q-2)/(q+1))['valid']
    assert a.domain_certificate((q-2)/(q+1))['numerator']['positive_roots']==1
    assert not a.domain_certificate(1/(q-2))['valid']
    assert a.domain_certificate(1/(q-2))['denominator']['positive_roots']==1
    assert not a.domain_certificate(0)['valid']
    with pytest.raises(ValueError): a.stripped_roots(0)
    hole=s.diag(1/(q-2),q-2,1,1)
    assert a.domain_certificate(hole.det())['valid']
    assert not a.matrix_pole_certificate(hole)['valid']  # A finite determinant is insufficient.


def test_wrong_map_constant_witness_and_twist_phase_fail():
    rho=a.generators(); jj=a.intertwiner('theta')['J']
    assert any(not (g.inv().transpose()*jj-jj*g).is_zero_matrix for g in rho)
    fixed=v.dm(a.intertwiner('theta')['matrix'].subs(q,2),K)
    assert any(not (g.inv().transpose()*fixed-fixed*g.inv()).is_zero_matrix for g in rho)
    field=s.QQ_I.frac_field(q); j=v.dm(a.intertwiner('thetaT')['matrix'],field)
    rr=tuple(v.dm(g.to_Matrix(),field) for g in rho)
    ii=field.from_sympy(s.I)
    left=tuple(g.inv().transpose().scalarmul(-ii) for g in rr)
    images=(rr[1].inv(),rr[0].inv())
    assert all((x*j-j*y.scalarmul(-ii)).is_zero_matrix for x,y in zip(left,images))
    assert any(not (x*j-j*y.scalarmul(ii)).is_zero_matrix for x,y in zip(left,images))
