"""F10 exact controls; analytic/global scope is not replaced by finite tests."""
import importlib.util
from pathlib import Path
import sympy as s
import pytest

spec=importlib.util.spec_from_file_location('f10_verify',Path(__file__).with_name('verify.py'))
v=importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


def zero(m):
    return m.applyfunc(s.simplify)==s.zeros(*m.shape)


def test_actual_knot_relation_and_determinants():
    m,n=v.generators()
    w=v.word('nMNm',(m,n))
    assert m.det()==n.det()==1
    assert zero(m*w-w*n)
    assert (m-s.eye(4))**3==s.zeros(4)
    assert (n-s.eye(4))**3==s.zeros(4)


def test_longitude_word_and_peripheral_commutation():
    m,n=v.generators()
    w=v.word('nMNm',(m,n))
    rev=v.word('mNMn',(m,n))
    ell=v.longitude()
    assert zero(ell-w*rev)
    assert zero(m*ell-ell*m)
    assert s.factor(ell.det())==1
    word='nMNmmNMn'
    assert sum(1 if c.islower() else -1 for c in word)==0


def test_full_longitude_characteristic_and_pairing_witness():
    x=s.symbols('X')
    ell=v.longitude()
    expected=(x-v.q)**3*(x-v.q**-3)
    assert s.factor(ell.charpoly(x).as_expr()-expected)==0
    assert s.factor(s.trace(ell)-s.trace(ell.inv())+(v.q-v.q**-1)**3)==0
    assert s.factor((ell-s.eye(4)).det()-(v.q-1)**3*(v.q**-3-1))==0


def test_projective_rescaling_is_not_same_linear_bundle():
    ell=v.longitude()
    scaled=ell/v.q
    assert s.factor(scaled.det())==v.q**-4
    assert s.factor((scaled-s.eye(4)).det())==0
    assert s.factor((ell-s.eye(4)).det())!=0


def test_geometric_point_is_actual_balanced_coefficient():
    m,n=v.generators(s.Integer(1))
    a,b=v.center_balanced()
    candidates=v.intertwiner((m,n),(a,b))
    assert len(candidates)==1
    p=candidates[0]
    assert s.simplify(p.det())!=0
    assert zero(m*p-p*a) and zero(n*p-p*b)
    ell=v.longitude(s.Integer(1))
    assert (ell-s.eye(4))**3==s.zeros(4)


def test_general_cusp_conjugacy():
    p=v.cusp_conjugator()
    m,_=v.generators()
    m0,l0=v.normal_form()
    assert s.factor(p.det())!=0
    assert zero(m*p-p*m0)
    assert zero(v.longitude()*p-p*l0)


@pytest.mark.parametrize('q',[s.Rational(1,2),s.Rational(3,2),s.Integer(2)])
def test_cusp_conjugator_invertible_both_sides(q):
    p=v.cusp_conjugator().subs(v.q,q)
    assert p.det()!=0
    ell=v.longitude(q)
    assert s.trace(ell)!=s.trace(ell.inv())
    # Since these matrices are real, this also refutes an invertible
    # flat antilinear map to the dual, not just a bilinear J trial.
    assert ell.conjugate()==ell


def test_finite_cover_power_character():
    n,p,d,h=v.cusp_generators()
    m,l=v.normal_form()
    for power in (2,3,5):
        lp=l**power
        expected=-(v.q**power-v.q**(-power))**3
        assert s.factor(s.trace(lp)-s.trace(lp.inv())-expected)==0
        assert s.factor((lp-s.eye(4)).det())!=0


def test_local_full_flatness_and_moment():
    c=v.local_connection()
    assert all(zero(r) for r in v.local_flat(c))
    assert zero(v.local_moment(c))
    assert all(s.simplify(s.trace(x))==0 for x in c)


def test_local_connection_has_the_claimed_cusp_holonomy():
    n,p,d,h=v.cusp_generators()
    u=v.z**2/4-v.beta**2/v.length**2
    f=s.sqrt(u)
    frame=s.diag(f,1,1,1/f)
    c=v.local_connection()
    assert zero(c[0]-frame.inv()*(-n)*frame)
    assert zero(c[1]-frame.inv()*(-v.kappa*d-v.beta*p)*frame)
    assert zero(c[2]-frame.inv()*frame.diff(v.z))
    assert zero(n*p-p*n) and zero(d*p-p*d) and zero(d*n-n*d)
    # exp(N)=I+N+N^2/2, exp(beta P)=I+beta P exactly.
    assert n**3==s.zeros(4) and p**2==s.zeros(4)


def test_norm_density_and_asymptotic_divergence():
    c=v.local_connection()
    u=v.z**2/4-v.beta**2/v.length**2
    fp_over_f=s.diff(u,v.z)/(2*u)
    expected=(v.length/(v.z*u)+12*v.kappa**2/(v.length*v.z)
              +v.beta**2/(2*v.length*v.z*u*u)+2*v.length*fp_over_f**2/v.z)
    actual=v.local_norm_density(c)
    assert s.factor(actual-expected)==0
    assert s.limit(v.z*actual,v.z,s.oo)==12*v.kappa**2/v.length
    remainder=s.factor(actual-12*v.kappa**2/(v.length*v.z))
    assert s.limit(v.z**3*remainder,v.z,s.oo)==6*v.length


def test_wrong_radial_profile_is_not_harmonic():
    c=v.local_connection(wrong_radial=True)
    assert all(zero(r) for r in v.local_flat(c))
    residual=v.local_moment(c)
    assert not zero(residual)
    assert zero(residual.subs(v.beta,0))


def test_diagonal_zero_residual_infinite_norm_comparator():
    _,_,d,_=v.cusp_generators()
    c=(s.zeros(4),-v.kappa*d,s.zeros(4))
    assert all(zero(r) for r in v.local_flat(c))
    assert zero(v.local_moment(c))
    assert v.local_norm_density(c)==12*v.kappa**2/(v.length*v.z)


@pytest.mark.parametrize('q',[s.Rational(1,2),s.Rational(3,2),s.Integer(2)])
def test_boundary_chain_contraction(q):
    m,_=v.generators(q)
    ell=v.longitude(q)
    d0,d1=v.torus_complex(m,ell)
    h1,h2=v.torus_homotopy(ell)
    assert d1*d0==s.zeros(4)
    assert h1*d0==s.eye(4)
    assert d0*h1+h2*d1==s.eye(8)
    assert d1*h2==s.eye(4)


def test_one_off_unit_eigenvalue_is_not_acyclic():
    m=s.eye(4)
    ell=s.diag(2,s.Rational(1,2),1,1)
    d0,d1=v.torus_complex(m,ell)
    assert ell.det()==1
    assert 4-d0.rank()==2
    assert 8-d1.rank()-d0.rank()==4
    assert 4-d1.rank()==2


def test_flat_torus_energy_evaluation_inequality_identity():
    a,b,c=s.symbols('a b c',real=True)
    x,y=s.symbols('x y',real=True)
    delta=a*c-b*b
    inverse=s.Matrix([[c,-b],[-b,a]])/delta
    energy=(s.Matrix([[x,y]])*inverse*s.Matrix([x,y]))[0]
    assert s.factor(energy-x*x/a-(a*y-b*x)**2/(a*delta))==0
