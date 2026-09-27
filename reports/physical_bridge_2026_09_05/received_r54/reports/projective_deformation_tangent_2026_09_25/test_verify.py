"""F15: tests do not prescribe the scientific sign/dimension verdict."""
from pathlib import Path
import importlib.util
import pytest
import sympy as s

spec=importlib.util.spec_from_file_location('f15_test_producer',Path(__file__).with_name('verify.py'))
v=importlib.util.module_from_spec(spec); spec.loader.exec_module(v)
CASES=[(14,1),(14,-1),(34,1),(34,-1)]


def test_field_and_linear_algebra_controls():
    k=s.QQ.algebraic_field(s.sqrt(3),s.I)
    a=v.dm([[1,s.sqrt(3)],[0,0]],k); z=v.kernel(a)
    assert a.rank()==1 and z.shape==(2,1) and (a*z).is_zero_matrix
    assert v.zero(2,2,k).rank()==0 and v.eye(2,k).rank()==2
    assert (v.dm([[s.sqrt(3)]],k)**2-v.dm([[3]],k)).is_zero_matrix
    for b in v.basis(k): assert (v.uncoords(v.coords(b))-b).is_zero_matrix
    with pytest.raises(ValueError): v.coords(v.eye(4,k))
    # One-dimensional complex d(t)=t: alpha=1 obstructs; d(t)=0 does not.
    left=v.eye(1,k); alpha=v.eye(1,k)
    assert (left*v.eye(1,k)*alpha).rank()==1
    assert (left*v.zero(1,1,k)*alpha).rank()==0


def test_trivial_representation_two_sided_grading_control():
    k=s.QQ; rho=(v.eye(4,k),v.eye(4,k))
    a=v.tangent_data(rho,v.eye(4,k))
    assert a['B'].rank()==0 and a['R'].rank()==15
    assert a['Hs'][1].shape[1]==9 and a['Hs'][-1].shape[1]==6
    assert (a['R']-v.direct_differential(rho)).is_zero_matrix


@pytest.mark.parametrize('middle,embedding',CASES)
def test_representation_and_independent_differential(middle,embedding):
    a=v.actual(middle,embedding); k=a['K']; rho=a['rho']
    assert s.simplify(a['q']**2-middle*a['q']+1)==0
    assert all(x.det()==k.one for x in rho)
    assert all((x.transpose()*a['J']-a['J']*x).is_zero_matrix for x in rho)
    value,_=v.word_jet(rho,(v.zero(4,4,k),v.zero(4,4,k)))
    assert (value-v.eye(4,k)).is_zero_matrix
    assert (a['R']-v.direct_differential(rho)).is_zero_matrix
    assert a['R'].rank()>0  # Non-cocycles really are rejected.
    assert (a['R']*a['B']).is_zero_matrix


@pytest.mark.parametrize('middle,embedding',CASES)
def test_involution_and_complete_quotient(middle,embedding):
    a=v.actual(middle,embedding); k=a['K']; t,b,r=a['T'],a['B'],a['R']
    assert (t*t-v.eye(30,k)).is_zero_matrix
    assert (t*b+b*a['C']).is_zero_matrix
    z=v.kernel(r)
    assert (r*t*z).is_zero_matrix
    for sign in (1,-1):
        zz,bb,hh=a['Z'][sign],a['Bs'][sign],a['Hs'][sign]
        assert (r*zz).is_zero_matrix and (r*bb).is_zero_matrix
        assert ((t-v.eye(30,k).scalarmul(k(sign)))*zz).is_zero_matrix
        assert ((t-v.eye(30,k).scalarmul(k(sign)))*bb).is_zero_matrix
        assert hh.shape[1]==zz.shape[1]-bb.rank()
        assert v.cat(bb,hh).rank()==zz.shape[1]
    assert a['H'].shape[1]==30-r.rank()-b.rank()
    assert v.cat(b,a['H']).rank()==30-r.rank()
    assert (r*a['qt']).is_zero_matrix
    assert v.cat(b,(t-v.eye(30,k))*a['qt']).rank()==b.rank()


@pytest.mark.parametrize('middle,embedding',CASES)
def test_matter_obstructions_descend_to_quotient(middle,embedding):
    a=v.actual(middle,embedding); k=a['K']; phase=s.I if middle==14 else -s.Integer(1)
    data=v.matter_data(middle,embedding)
    for dual,row in zip((False,True),data['rows']):
        m=v.matter_complex(a['rho'],phase,dual)
        assert m['B'].rank()==4 and m['R'].rank()==3
        assert (m['R']*m['B']).is_zero_matrix
        assert m['H'].shape==(8,1) and v.cat(m['B'],m['H']).rank()==5
        assert v.obstruction_row(a['rho'],phase,dual,a['B']).is_zero_matrix
        # Change every quotient representative by an explicit gauge direction.
        change=a['B'].extract(range(30),range(a['H'].shape[1]))
        shifted=v.obstruction_row(a['rho'],phase,dual,a['H']+change)
        assert (shifted-row).is_zero_matrix
        # Changing a matter representative by a boundary changes no class.
        for i in range(a['H'].shape[1]):
            dj=v.matter_derivative(a['rho'],phase,dual,v.col(a['H'],i))
            assert (m['left']*dj*m['B']).is_zero_matrix
    assert data['joint'].rank()<=2
    assert data['odd'].rank()<=a['Hs'][-1].shape[1]
