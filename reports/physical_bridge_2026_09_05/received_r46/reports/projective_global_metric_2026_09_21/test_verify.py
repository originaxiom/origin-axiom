"""F12 preregistered finite tests; the analytic proof has separate status."""
from pathlib import Path
import importlib.util
import sympy as s
import pytest

spec=importlib.util.spec_from_file_location('f12_global',Path(__file__).with_name('verify.py'))
v=importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)
q,z,L,beta,k=v.q,v.z,v.L,v.beta,v.k
p=q*q-14*q+1


def test_scalar_control():
    assert len(v.algebra_words((s.eye(4),s.eye(4)),p)[0])==1


def test_full_matrix_control():
    cycle=s.zeros(4)
    for i in range(4):
        cycle[(i+1)%4,i]=1
    assert len(v.algebra_words((s.diag(1,2,3,4),cycle),p)[0])==16


def test_triangular_control_and_scalar_commutant_trap():
    a=s.diag(2,s.Rational(1,2))
    b=s.Matrix([[1,1],[0,1]])
    assert len(v.algebra_words((a,b),p)[0])==3
    xs=s.symbols('x:4')
    x=s.Matrix(2,2,xs)
    comm=s.linear_eq_to_matrix(list(a*x-x*a)+list(b*x-x*b),xs)[0]
    assert len(comm.nullspace())==1  # NOT an irreducibility certificate.


@pytest.mark.parametrize('middle',(14,34))
def test_exceptional_full_algebra(middle):
    result=v.certificate(middle)
    assert result['dimension']==16
    assert result['determinant_mod_p']!=0
    assert result['word_reconstruction']
    poly=s.Poly(q*q-middle*q+1,q,extension=s.I)
    assert poly.is_irreducible
    assert s.Poly(poly.as_expr(),q,domain=s.QQ).count_roots(0,s.oo)==2


@pytest.mark.parametrize('middle',(14,34))
def test_determinant_certificate_survives_both_roots(middle):
    data=v.certificate(middle)
    det=data['determinant_mod_p']
    assert det is not None
    num,den=s.fraction(s.cancel(det))
    poly=q*q-middle*q+1
    assert s.gcd(s.Poly(num,q),s.Poly(poly,q)).degree()==0
    assert s.gcd(s.Poly(den,q),s.Poly(poly,q)).degree()==0
    assert s.rem(s.cancel(poly.subs(q,1/q)*q*q-poly),poly,q)==0


def test_tracefree_sharp_floor():
    proj=v.tracefree_projector()
    assert s.trace(proj)==0
    assert s.trace(proj*proj)==s.Rational(3,4)
    assert 9/s.trace(proj*proj)==12
    _,_,d,_=v.f10.cusp_generators()
    assert s.trace(d*d)==12
    # The q^-3 eigenline, coordinate 1, attains the trace-free bound.
    p1=s.diag(0,1,0,0)-s.eye(4)/4
    assert d==-4*p1


def test_actual_reference_density_and_tail_primitive():
    density,residual,tail=v.energy_data()
    assert s.simplify(density-12*k*k/(L*z)-residual)==0
    assert s.simplify(s.diff(tail,z)+residual)==0


def test_exact_large_height_limits():
    _,residual,tail=v.energy_data()
    assert s.limit(z**3*residual,z,s.oo)==6*L
    assert s.limit(z**2*tail,z,s.oo)==3*L


def test_excess_positive_and_integrable_upper_bound():
    _,residual,_=v.energy_data()
    w=s.symbols('w',nonnegative=True)
    # Write z^2=2c+w: every coefficient in numerator/denominator is nonnegative.
    c=4*beta**2/L**2
    scaled=s.factor((24*L/z**3-residual)*z**3*(z*z-c)**2/L)
    assert s.expand(scaled.subs(z*z,2*c+w))==4*c*c+26*c*w+18*w*w


def test_weaker_floor_cannot_bound_excess():
    density,_,_=v.energy_data()
    assert s.limit(z*(density-9*k*k/(L*z)),z,s.oo)==3*k*k/L


def test_matrix_unit_condition_number_identity():
    # Exact non-diagonal positive Hermitian control for the general trace formula.
    a=s.Matrix([[1,s.I,0,0],[0,1,1,0],[0,0,1,1],[0,0,0,1]])
    h=a.conjugate().T*a
    inv=h.inv()
    total=0
    for i in range(4):
        for j in range(4):
            unit=s.zeros(4)
            unit[i,j]=1
            norm=s.trace(inv*unit.T*h*unit)
            assert norm==h[i,i]*inv[j,j]
            total+=norm
    assert total==s.trace(h)*s.trace(inv)


def test_tracefree_diagonal_end_saturates_floor():
    _,_,d,_=v.f10.cusp_generators()
    assert s.trace((-k*d)**2)/L==12*k*k/L


def test_distance_to_norm_bound_convention():
    a=s.symbols('a',nonnegative=True)
    # If d_X(I,H)=1/2 ||log H||_F <= C, each |log lambda_i|<=2C.
    logs=s.Matrix([a,-a,0,0])
    assert (logs.dot(logs))/4==a*a/2
    assert s.simplify(4*(logs.dot(logs)/4)-a*a)==a*a
