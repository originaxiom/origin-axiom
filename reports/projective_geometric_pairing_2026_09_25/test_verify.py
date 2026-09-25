"""F14 preregistered exact candidate tests and analytic-input controls."""
from pathlib import Path
import importlib.util
import sympy as s
import pytest

spec=importlib.util.spec_from_file_location('f14_geometric',Path(__file__).with_name('verify.py'))
v=importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)
q,z,L,beta,k=v.q,v.z,v.L,v.beta,v.k


@pytest.mark.parametrize('name',tuple(v.CANDIDATES))
def test_candidate_isometry_exact_generator_action_and_surjectivity(name):
    cert=v.geometric_certificate(name)
    assert cert['generator_actions'],cert
    assert cert['power_in_Gamma'],cert
    assert cert['orientation']==v.CANDIDATES[name][3]


def test_geometric_relator_and_wrong_map_control():
    rho,_=v.geometry()
    assert v.psl_equal(v.word(v.f11.RELATOR,rho,True),s.eye(2))
    assert not v.psl_equal(rho[0],rho[0].inv())
    assert v.substitute(v.LONGITUDE,('M','N'))==v.inverse_word(v.LONGITUDE)


@pytest.mark.parametrize('middle',(14,34))
def test_theta_restores_geometric_duality_prior(middle):
    cert=v.candidate_certificate(middle,'theta')
    assert cert['dimension']==1,cert
    assert cert['determinant']!=0,cert
    assert cert['entrywise']


@pytest.mark.parametrize('middle',(14,34))
@pytest.mark.parametrize('name',tuple(v.CANDIDATES))
def test_entire_candidate_table_witnesses_or_full_rank(middle,name):
    cert=v.candidate_certificate(middle,name)
    assert cert['dimension'] in (0,1)
    if cert['dimension']:
        assert cert['entrywise'] and cert['determinant']!=0
        p=q*q-middle*q+1
        assert s.gcd(s.Poly(cert['determinant'],q),s.Poly(p,q)).degree()==0
    else:
        assert cert['rank']==16


def test_generic_theta_and_exceptional_specializations():
    matrices=v.generic_inversion()
    assert len(matrices)==1
    matrix=matrices[0]
    assert s.factor(matrix.det())!=0
    for a in v.f10.generators():
        assert v.clean(a.T*matrix-matrix*a)==s.zeros(4)
    for middle in (14,34):
        p=q*q-middle*q+1
        assert v.field.reduce_scalar(matrix.det(),p)!=0
        actual=v.candidate_certificate(middle,'theta')['matrix']
        vec=matrix.reshape(16,1)
        assert v.field.rank(vec.row_join(actual.reshape(16,1)),p)==1


def test_phase_factors_for_linear_and_antilinear_maps():
    for name in v.CANDIDATES:
        eps=v.CANDIDATES[name][2]
        for phase in (s.I,-s.I,-s.Integer(1)):
            linear=v.phase_factor(phase,name)
            anti=v.phase_factor(phase,name,True)
            assert linear==s.simplify(phase**eps/(phase**-1))
            assert anti==s.simplify(s.conjugate(phase**eps)/(phase**-1))
            if phase==-1:
                assert linear==anti==1
        assert v.phase_factor(s.I,name)==(1 if eps==-1 else -1)
        assert v.phase_factor(s.I,name,True)==(1 if eps==1 else -1)
    assert v.phase_factor(s.I,'theta')==1


@pytest.mark.parametrize('middle',(14,34))
def test_mismatched_phase_sylvester_control(middle):
    p=q*q-middle*q+1
    m,n=v.f10.generators()
    for source in (m,n,m.inv(),n.inv()):
        # One generator alone has disjoint spectra (+1 versus -1).
        eq=v.intertwiner_equations((m.inv().T,),(-source,))
        assert v.field.rank(eq,p)==16


def test_intertwiner_instrument_positive_and_negative_controls():
    p=q*q-14*q+1
    full=v.intertwiner_equations((s.eye(2),),(s.eye(2),))
    none=v.intertwiner_equations((s.eye(2),),(-s.eye(2),))
    assert v.field.kernel(full,p).cols==4
    assert v.field.kernel(none,p).cols==0
    # Row-major equation construction is checked on an arbitrary actual matrix.
    x=s.Matrix([[1,2],[3,4]])
    a=s.Matrix([[1,1],[0,1]])
    b=s.Matrix([[1,0],[2,1]])
    assert v.intertwiner_equations((b,),(a,))*x.reshape(4,1)==(b*x-x*a).reshape(4,1)


def test_fiberwise_pairing_and_geometric_pairing_are_different():
    m,n=v.f10.generators(s.Integer(1))
    assert len(v.f10.intertwiner((m.inv().T,n.inv().T),(m,n)))>=1
    ell=v.f10.longitude()
    difference=s.factor(s.trace(ell)-s.trace(ell.inv()))
    assert s.factor(difference+(q-q**-1)**3)==0
    for middle in (14,34):
        assert v.field.reduce_scalar(difference,q*q-middle*q+1)!=0
        assert v.candidate_certificate(middle,'id')['dimension']==0


def test_full_local_cusp_pairing_and_radial_sign_control():
    r=v.cusp_reflector()
    c=v.f10.local_connection()
    signs=(-1,-1,1)
    assert r.T*r==s.eye(4)
    for sign,a in zip(signs,c):
        assert v.clean(r*(sign*a)*r.T+a.T)==s.zeros(4)
    assert v.clean(r*c[2]*r.T-c[2].T)!=s.zeros(4)


def test_full_centralizer_and_its_bounded_inverse():
    (n,p,d,h,pi),(a,b,c,e,u),zmat,inv,scale=v.cusp_centralizer()
    eq=v.intertwiner_equations((n,d),(n,d))
    assert 16-eq.rank()==4
    basis=s.Matrix.hstack(*(x.reshape(16,1) for x in (s.eye(4),n,p,pi)))
    assert basis.rank()==4 and eq*basis==s.zeros(32,4)
    assert s.factor(zmat.det())==a**3*(a+e)
    assert v.clean(zmat*inv-s.eye(4))==s.zeros(4)
    assert v.clean(inv*zmat-s.eye(4))==s.zeros(4)
    expected=a*s.eye(4)+b*n/s.sqrt(u)+c*p/u+e*pi
    r=v.cusp_reflector()
    assert v.clean(scale.T*r*zmat*scale-r*expected)==s.zeros(4)
    assert expected.applyfunc(lambda x:s.limit(x,u,s.oo))==a*s.eye(4)+e*pi
    scaled_inverse=v.clean(scale.inv()*inv*scale)
    limit=scaled_inverse.applyfunc(lambda x:s.limit(x,u,s.oo))
    assert v.clean(limit*(a*s.eye(4)+e*pi)-s.eye(4))==s.zeros(4)


def test_actual_generic_map_lands_in_the_full_cusp_centralizer():
    matrix=v.generic_inversion()[0]
    basis=v.f10.cusp_conjugator()
    cusp=v.clean(basis.T*matrix*basis)
    central=v.clean(v.cusp_reflector().T*cusp)
    n,_,d,_=v.f10.cusp_generators()
    assert v.clean(central*n-n*central)==s.zeros(4)
    assert v.clean(central*d-d*central)==s.zeros(4)


def test_volume_pairing_tracks_the_actual_determinant():
    j=v.generic_inversion()[0]
    jj=v.f05.exterior_group(j)
    kk=v.volume_pairing()
    assert v.clean(jj.T*kk*jj-j.det()*kk)==s.zeros(6)
    # Dropping the determinant for a non-volume-normalized map is wrong.
    arbitrary=2*s.eye(4)
    ext=v.f05.exterior_group(arbitrary)
    assert ext.T*kk*ext==16*kk
    assert ext.T*kk*ext!=kk


def test_parent_map_is_an_actual_E8_Weyl_element():
    w,roots=v.parent_weyl()
    roster=v.f05.e8_roots()
    assert all(tuple(r) in roster and r.dot(r)==2 for r in roots)
    assert w==s.diag(-1,1,1,1,1,-1,-1,-1)
    assert w.T*w==s.eye(8) and w*w==s.eye(8)
    assert {tuple(w*s.Matrix(r)) for r in roster}==roster
    assert w[5:,5:]==-s.eye(3)
    # Half roots encode both chiral D5 spinors and the A3 four/dual-four.
    half=[r for r in roster if all(abs(x)==s.Rational(1,2) for x in r)]
    assert len(half)==128
    for r in half:
        image=w*s.Matrix(r)
        assert s.prod(image[:5])==-s.prod(r[:5])
        assert s.prod(image[5:])==-s.prod(r[5:])
