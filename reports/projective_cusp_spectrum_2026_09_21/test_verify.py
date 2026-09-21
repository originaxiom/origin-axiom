"""F11 falsifiable exact controls; no finite test replaces the end proof."""
import importlib.util
from pathlib import Path
import sympy as s
import pytest

spec=importlib.util.spec_from_file_location('f11_verify',Path(__file__).with_name('verify.py'))
v=importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


def zero(m):
    return m.applyfunc(s.simplify)==s.zeros(*m.shape)


@pytest.mark.parametrize('dual',[False,True])
def test_all_frequency_longitudinal_inverse(dual):
    c=v.connection(dual)
    t=s.I*v.omega*s.eye(4)+c[1]
    h=v.inverse_longitude(dual)
    assert zero(t*h-s.eye(4)) and zero(h*t-s.eye(4))
    assert zero(c[2]*h-h*c[2]+h.diff(v.z))
    assert zero(c[0]*h-h*c[0])


@pytest.mark.parametrize('dual',[False,True])
def test_full_cusp_cartan_homotopy(dual):
    assert all(zero(r) for r in v.cartan_residual(dual))
    h=v.homotopy(dual)
    assert zero(h*h)


def test_actual_form_metric_contraction_scale():
    g=v.form_metric()
    contraction=v.wedge(1).T
    adj=g.inv()*contraction.T*g
    assert zero(adj*contraction+contraction*adj-v.L**2/v.z**2*s.eye(8))


def test_cutoff_retraction_is_a_chain_map():
    a,b=v.differential_parts()
    h=v.homotopy()
    chi=s.Function('chi')(v.z)
    r=(1-chi)*s.eye(32)-s.diff(chi,v.z)*b*h
    assert zero(a*r-r*a+b*r.diff(v.z))
    assert zero(b*r-r*b)


def test_nonflat_radial_family_rejects_total_homotopy():
    # d=d_z+z dy is nonflat although its longitudinal coefficient is invertible.
    ey,ez=v.wedge(1),v.wedge(2)
    h=ey.T/v.z
    residual=v.z*ey*h+h*v.z*ey+ez*h.diff(v.z)-s.eye(8)
    assert not zero(residual)
    assert zero(residual+ez*ey.T/v.z**2)


def test_zero_real_part_control_is_singular():
    c=v.connection()
    t=c[1].subs(v.k,0)
    assert s.factor(t.det())==0
    assert t.rank()==1


@pytest.mark.parametrize('dual',[False,True])
@pytest.mark.parametrize('frequency',[0,2,7])
def test_inverse_norm_bound_exact_controls(dual,frequency):
    values={v.k:s.Integer(1),v.beta:s.Integer(2),v.L:s.Integer(3),
            v.z:s.Integer(10),v.omega:s.Integer(frequency)}
    a=v.inverse_longitude(dual).subs(values)
    u=s.Rational(100,4)-s.Rational(4,9)
    bound=1+2/u
    positive=bound**2*s.eye(4)-a.H*a
    # All principal minors, not just leading ones, certify semidefiniteness.
    from itertools import combinations
    for size in range(1,5):
        for indices in combinations(range(4),size):
            assert s.simplify(positive.extract(indices,indices).det())>=0


def test_inverse_real_part_bound_and_tail_decay():
    k,w=s.symbols('k w',real=True)
    for weight in (1,-3):
        assert s.expand((s.I*w-k*weight)*(-s.I*w-k*weight)-k*k*weight**2)==w*w
    kp,bp=s.symbols('kp bp',positive=True)
    u=v.z*v.z/4-bp*bp/v.L**2
    bound=v.L/v.z*(1/kp+bp/(u*kp*kp))
    assert s.limit(bound,v.z,s.oo)==0
    assert s.limit((1/(2*bound**2))/v.z**2,v.z,s.oo)==kp**2/(2*v.L**2)


@pytest.mark.parametrize('phase',v.PHASES)
def test_actual_twisted_relation_and_complex(phase):
    rho=v.representation(phase=phase)
    b,j=v.complex_matrices(phase=phase)
    assert zero(v.word(v.RELATOR,rho)-s.eye(4))
    assert zero(j*b)


def test_fox_agrees_with_affine_construction():
    rho=v.representation()
    assert zero(v.fox(v.RELATOR,rho)-v.affine_cocycle(v.RELATOR,rho))
    for phase in v.PHASES:
        rho=v.representation(s.Rational(3,2),phase,dual=True)
        assert zero(v.fox(v.RELATOR,rho)-v.affine_cocycle(v.RELATOR,rho))


@pytest.mark.parametrize('phase',v.PHASES)
def test_every_positive_rank_exception_is_geometric(phase):
    b,j=v.certificates(phase)
    assert b['minors']==j['minors']==70
    assert b['q_only_denominators'] and j['q_only_denominators']
    assert b['positive_roots']==0
    assert j['positive_roots'] in (0,1)
    if j['positive_roots']==1:
        assert s.simplify(j['gcd'].subs(v.q,1))==0


def test_geometric_ordinary_h1_control():
    assert v.dimensions(1)==(0,1)
    # The changed-end L2 proof explicitly excludes this parameter.


@pytest.mark.parametrize('parameter',[s.Rational(1,2),s.Rational(3,2),s.Integer(2)])
def test_member_and_dual_ordinary_counts(parameter):
    for phase in v.PHASES:
        assert v.dimensions(parameter,phase)==(0,0)
        assert v.dimensions(parameter,phase,dual=True)==(0,0)


def test_trivial_coefficient_positive_control():
    rho={'m':s.eye(4),'n':s.eye(4)}
    b=s.zeros(8,4)
    j=v.fox(v.RELATOR,rho)
    assert zero(j-s.eye(4).row_join(-s.eye(4)))
    assert 8-b.rank()-j.rank()==4


def test_modulus_projection_and_gauge_independence():
    _,p,d,_=v.f10.cusp_generators()
    c=v.connection()[1]
    psi=(c+c.T)/2
    assert zero(d*psi-psi*d)
    variation=psi.diff(v.k)+s.symbols('beta_prime',real=True)*psi.diff(v.beta)
    assert s.simplify(s.trace(d*variation))==-12
    xs=s.symbols('e0:16')
    epsilon=s.Matrix(4,4,xs)
    assert s.simplify(s.trace(d*(psi*epsilon-epsilon*psi)))==0
    density=12/(v.L*v.z)
    assert s.integrate(density,(v.z,1,s.oo))==s.oo
