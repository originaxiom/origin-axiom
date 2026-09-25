"""Exact finite certificates; convergence is proved in PROOF, not by jets."""
from pathlib import Path
import importlib.util
import pytest
import sympy as s

spec=importlib.util.spec_from_file_location('f16_test_producer',Path(__file__).with_name('verify.py'))
p=importlib.util.module_from_spec(spec); spec.loader.exec_module(p)
v=p.v
CASES=[(14,1),(14,-1),(34,1),(34,-1)]


def test_actual_group_automorphism_not_transpose_alone():
    r=v.REL
    assert p.reduce_word(r.swapcase())==p.reduce_word('N'+p.inverse_word(r)+'n')
    for w in ('mn',r,'nMNmmNMn','MNmnnMN'):
        assert w.swapcase().swapcase()==w
    assert 'mn'.swapcase()!=p.inverse_word('mn')


@pytest.mark.parametrize('middle,embedding',CASES)
def test_full_gauge_and_odd_implicit_certificates(middle,embedding):
    c=p.slice_certificate(middle,embedding); a=c['a']; k=a['K']
    assert a['B'].rank()==15
    assert [c['ambient'][sgn].shape[1] for sgn in (1,-1)]==[18,12]
    assert [c['W'][sgn].shape[1] for sgn in (1,-1)]==[12,3]
    total=c['total']; ti=total.inv()
    assert c['total_det']!=k.zero
    assert (total*ti-v.eye(30,k)).is_zero_matrix
    assert (ti*total-v.eye(30,k)).is_zero_matrix
    for sign in (1,-1):
        assert ((a['T']-v.eye(30,k).scalarmul(k(sign)))*c['W'][sign]).is_zero_matrix
        assert v.cat(a['Bs'][sign],c['W'][sign]).rank()==c['ambient'][sign].shape[1]
    assert c['odd'].rank()==3 and c['minor_det']!=k.zero
    assert (c['minor']*c['minor'].inv()-v.eye(3,k)).is_zero_matrix
    w=v.cat(c['W'][1],c['W'][-1]); z=v.kernel(a['R']*w)
    assert z.shape==(15,3)
    assert z.extract(range(12,15),range(3)).is_zero_matrix


@pytest.mark.parametrize('middle,embedding',CASES)
def test_exact_chart_jet_and_gauge_action_sign(middle,embedding):
    c=p.slice_certificate(middle,embedding); a=c['a']; k=a['K']
    u=v.dm(s.Matrix([(-1)**i*(i+1) for i in range(30)]),k)
    assert all(x.is_zero_matrix for x in p.chart_jet_residuals(a,u))
    # Deliberately omit Ad(rho): the wrong left-log derivative must fail.
    c0=a['C']; wrong=v.stack(v.cat(c0,v.zero(15,15,k)),v.cat(v.zero(15,15,k),c0))
    assert not ((a['T']-wrong)*u).is_zero_matrix
    assert (a['T']*a['B']+a['B']*c0).is_zero_matrix
    x=v.uncoords(v.dm(s.Matrix(range(1,16)),k)); j=a['J']; ji=j.inv()
    # sigma(exp(tX))=exp(-t C(X)), coefficients, with the inverse-transpose sign.
    for lhs,rhs in zip(p.exp_jet(-x),p.exp_jet(-ji*x.transpose()*j)):
        assert (ji*lhs.transpose()*j-rhs).is_zero_matrix


def test_variable_intertwiner_family_and_wrong_maps():
    a=p.conjugated_family(); k=a['k']; rho=a['rho']; j=a['Ja']
    assert a['g'].det()==k.one and j.det()==a['J'].det()
    assert (j-j.transpose()).is_zero_matrix
    assert all((r.transpose()*j-j*r).is_zero_matrix for r in rho)
    assert (p.word(v.REL,rho)-v.eye(4,k)).is_zero_matrix
    assert any(not (r.transpose()*a['fixed_J']-a['fixed_J']*r).is_zero_matrix for r in rho)
    for w in ('mn','mnMNm','nMNmmNMn'):
        lhs=p.word(w,rho).inv().transpose()*j
        assert (lhs-j*p.word(w.swapcase(),rho)).is_zero_matrix
    prod=p.word('mn',rho)
    assert not (prod.transpose()*j-j*prod).is_zero_matrix
    assert (prod.transpose()*j-j*p.word('nm',rho)).is_zero_matrix


def test_invariant_singular_locus_with_hidden_second_order_curve():
    x,y,t=s.symbols('x y t')
    f=y*y-x**4
    assert f.subs(y,-y)==f
    assert f.subs({x:t,y:t*t})==0
    assert s.diff(t*t,t).subs(t,0)==0 and t*t!=-t*t
    # FULL defining-equation tangent detects the odd direction despite that curve.
    jac=s.Matrix([f]).jacobian((x,y)).subs({x:0,y:0})
    assert jac.rank()==0 and jac[:,1].rank()==0
    good=s.Matrix([y,x*x]).jacobian((x,y)).subs({x:0,y:0})
    assert good[:,1].rank()==1  # Odd variable eliminated even at a singular germ.
    nonfinite=x+x*x
    assert s.diff(nonfinite,x).subs(x,0)==1
    assert s.expand(nonfinite.subs(x,nonfinite)-x)!=0


def test_trivial_representation_cannot_use_injective_gauge_chart():
    k=s.QQ; a=v.tangent_data((v.eye(4,k),v.eye(4,k)),v.eye(4,k))
    assert a['B'].rank()==0 and a['Hs'][-1].shape[1]==6
    assert a['B'].shape==(30,15)  # Dimension alone is not an injectivity certificate.
