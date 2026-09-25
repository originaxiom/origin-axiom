"""F13 pre-execution controls, including the fallible mediator-gap prior."""
from pathlib import Path
import importlib.util
import sympy as s
import pytest

spec=importlib.util.spec_from_file_location('f13_fluctuations',Path(__file__).with_name('verify.py'))
v=importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)
q,z,L,beta,k,omega=v.q,v.z,v.L,v.beta,v.k,v.omega


@pytest.mark.parametrize('middle,sign',v.ACTUAL)
def test_actual_six_has_no_massless_one_form_prior(middle,sign):
    data=v.six_certificate(middle,sign)
    assert data['H0']==0
    assert data['H1']==0, data
    assert data['B']['rank']==data['J']['rank']==6


@pytest.mark.parametrize('middle,sign',((14,-1),(14,1),(34,-1),(34,1)))
def test_field_certificates_and_independent_affine_composition(middle,sign):
    data=v.six_certificate(middle,sign)
    assert data['relation'] and data['fox_equals_affine'] and data['J_B_zero']
    p=q*q-middle*q+1
    for key in ('B','J'):
        minor=data[key]['minor']
        assert minor!=0
        assert s.gcd(s.Poly(minor,q),s.Poly(p,q)).degree()==0
    assert s.Poly(p,q,extension=s.I).is_irreducible
    assert s.Poly(p,q).count_roots(0,s.oo)==2


def test_trivial_coefficient_recovers_nonzero_H1_control():
    rho={'m':s.eye(1),'n':s.eye(1)}
    b=s.zeros(2,1)
    j=v.f11.fox(v.f11.RELATOR,rho)
    assert j==s.Matrix([[1,-1]])
    assert 2-b.rank()-j.rank()==1
    relation,affine=v.field_affine(v.f11.RELATOR,rho,q*q-14*q+1)
    assert relation==s.eye(1) and affine==j


def test_exterior_functor_and_actual_central_twist():
    m,n=v.f10.generators()
    ext=v.f05.exterior_group
    assert v.clean(ext(m*n)-ext(m)*ext(n))==s.zeros(6)
    for phase in (1,-1,s.I,-s.I):
        assert v.clean(ext(phase*m)-phase**2*ext(m))==s.zeros(6)
    t=s.symbols('t')
    x=v.f10.cusp_generators()[0]
    assert ext(s.eye(4)+t*x).diff(t).subs(t,0)==v.f05.exterior_lie(x)


def test_six_longitude_boundary_acyclicity():
    # Conjugation-invariant spectrum, using F10's already checked normal form.
    _,ell=v.f10.normal_form()
    six=v.f05.exterior_group(ell)
    x=s.symbols('x')
    assert s.factor(six.charpoly(x).as_expr())==s.factor((x-q*q)**3*(x-q**-2)**3)
    assert s.factor((six-s.eye(6)).det())==s.factor((q*q-1)**3*(q**-2-1)**3)


def test_exterior_cusp_weight_and_nilpotent_norm():
    _,p,d,_=v.f10.cusp_generators()
    pp,dd=v.f05.exterior_lie(p),v.f05.exterior_lie(d)
    assert dd.eigenvals()=={-2:3,2:3}
    assert pp*pp==s.zeros(6) and v.comm(dd,pp)==s.zeros(6)
    assert (pp.T*pp).eigenvals()=={0:4,1:2}


def test_exact_all_frequency_inverse_and_radial_connection():
    cx,cy,cz=v.six_cusp()
    inverse=v.six_longitude_inverse()
    t=s.I*omega*s.eye(6)+cy
    assert v.clean(t*inverse-s.eye(6))==s.zeros(6)
    assert v.clean(inverse*t-s.eye(6))==s.zeros(6)
    assert v.clean(v.comm(cx,inverse))==s.zeros(6)
    assert v.clean(inverse.diff(z)+v.comm(cz,inverse))==s.zeros(6)
    # Dropping the z derivative loses the full Cartan homotopy.
    assert v.clean(v.comm(cz,inverse))!=s.zeros(6)


def test_six_inherits_actual_flatness_and_moment():
    c=v.six_cusp()
    out=[]
    for i in range(3):
        for j in range(i+1,3):
            derivative=-c[i].diff(z) if j==2 else s.zeros(6)
            out.append(v.clean(derivative+v.comm(c[i],c[j])))
    assert all(a==s.zeros(6) for a in out)
    moment=z**3*((c[2]+c[2].T)/z).diff(z)
    moment+=z*z*sum((w*v.comm(a,a.T) for w,a in zip((1,L**-2,1),c)),s.zeros(6))
    assert v.clean(moment)==s.zeros(6)


def test_scalar_freedom_removed_only_after_irreducibility():
    # Full matrix algebra: only the scalar commutes; trace-free kills it.
    xs=s.symbols('x:16')
    x=s.Matrix(4,4,xs)
    diagonal=s.diag(1,2,3,4)
    cycle=s.zeros(4)
    for i in range(4):
        cycle[(i+1)%4,i]=1
    equations=list(v.comm(x,diagonal))+list(v.comm(x,cycle))+[s.trace(x)]
    coeff=s.linear_eq_to_matrix(equations,xs)[0]
    assert coeff.rank()==16
    # Trivial flat connection: distinct constant det-one metrics both solve mu=0.
    h=s.diag(2,s.Rational(1,2),1,1)
    assert h.det()==1 and h!=s.eye(4)
    assert all(e>0 for e in h.diagonal())


def test_parent_adjoint_split_and_wrong_sign_control():
    adj,gauge,moment,wrong=v.linearized_split()
    assert v.clean(adj-gauge-moment)==s.zeros(2)
    assert v.clean(gauge.H+gauge)==s.zeros(2)
    assert v.clean(moment.H-moment)==s.zeros(2)
    assert v.clean((adj+adj.H)/2-moment)==s.zeros(2)
    assert v.clean((adj-adj.H)/2-gauge)==s.zeros(2)
    assert v.clean(moment-wrong)!=s.zeros(2)
    # Orthogonality is real, not necessarily the complex trace itself being zero.
    assert s.simplify(s.re(s.trace(gauge.H*moment)))==0


def test_nonlinear_parent_moment_expansion():
    t,diff,first,second=v.nonlinear_moment_coefficients()
    assert v.clean(diff-t*first-t*t*second)==s.zeros(2)
    assert second!=s.zeros(2)


def test_compact_gauge_moment_cancellation_with_first_jets():
    e=s.I*v.pauli_hermitian('eps_')
    psi=v.pauli_hermitian('psi_')
    de=s.I*v.pauli_hermitian('deps_')
    mu=v.pauli_hermitian('mu_')
    # delta_A[Psi,eps]=[delta_A Psi,eps]-[Psi,d_A eps].
    delta_of_variation=v.comm(mu,e)-v.comm(psi,de)
    linear_moment=delta_of_variation+v.comm(psi,de)
    assert v.clean(linear_moment-v.comm(mu,e))==s.zeros(2)
    assert v.clean(linear_moment.subs({x:0 for x in mu.free_symbols}))==s.zeros(2)
    assert v.clean(delta_of_variation.subs({x:0 for x in mu.free_symbols}))!=s.zeros(2)


def test_parent_relative_normalization_from_components():
    f01,f02,f12,mu,gauge=s.symbols('f01 f02 f12 mu gauge',real=True)
    f=s.Matrix([[0,f01,f02],[-f01,0,f12],[-f02,-f12,0]])
    form_norm=f01*f01+f02*f02+f12*f12
    component_norm=sum(a*a for a in f)
    potential=component_norm+s.Rational(1,2)*(-2*mu)**2
    assert s.expand(potential-2*(form_norm+mu*mu))==0
    assert s.expand(potential+2*gauge*gauge-2*(form_norm+mu*mu+gauge*gauge))==0
    assert s.expand(potential-(form_norm+mu*mu))!=0


def test_Clifford_IMS_principal_symbol_and_cutoff_cancellation():
    cs=tuple(v.f11.wedge(i)-v.f11.wedge(i).T for i in range(3))
    xs=s.symbols('x:3',real=True)
    c=sum((x*a for x,a in zip(xs,cs)),s.zeros(8))
    assert v.clean(c.T*c-sum(x*x for x in xs)*s.eye(8))==s.zeros(8)
    t=s.symbols('t',real=True)
    pair=(s.cos(t),s.sin(t))
    assert s.simplify(sum(a*a for a in pair))==1
    assert s.simplify(sum(a*s.diff(a,t) for a in pair))==0


def test_L2_is_not_L4_on_the_actual_cusp_control():
    a=s.Rational(3,4)
    assert s.integrate(z**(2*a-3),(z,1,s.oo))==2
    assert s.integrate(z**(4*a-3),(z,1,s.oo))==s.oo
    eps=s.symbols('eps',positive=True)
    assert s.limit(z**s.Rational(3,2)*s.exp(-eps*z),z,s.oo)==0


def test_Agmon_weight_hyperbolic_gradient_and_absorption():
    eps,A=s.symbols('eps A',positive=True)
    f=s.exp(eps*z)
    assert s.simplify(z*z*s.diff(f,z)**2-eps*eps*z*z*f*f)==0
    assert s.simplify((2*A*eps*eps).subs(eps,1/(2*s.sqrt(A))))==s.Rational(1,2)


def test_rank_one_profile_control_does_not_force_nonzero_vertex():
    # Nonzero, decomposable bundle-valued one-form has zero self source.
    spatial=s.Matrix([1,2,3])
    coeff=s.Matrix([1,s.I,2,0])
    u=coeff*spatial.T
    assert u!=s.zeros(4,3)
    for i in range(3):
        for j in range(3):
            assert u[:,i]*u[:,j].T-u[:,j]*u[:,i].T==s.zeros(4)
