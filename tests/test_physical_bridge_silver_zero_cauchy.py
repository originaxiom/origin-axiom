"""Actual kernel/current/field controls, not a global particle certificate."""
import importlib.util
from pathlib import Path
import mpmath as mp
import pytest
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
PACKET=ROOT/'reports/physical_bridge_2026_09_05/silver_zero_cauchy_2026_10_12'
def load(name):
    spec=importlib.util.spec_from_file_location('zero_cauchy_'+name,PACKET/(name+'.py'))
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module

@pytest.fixture(scope='module')
def modules():return load('probe'),load('reference')
@pytest.fixture(scope='module')
def results(modules):return modules[0].run(),modules[1].run()

def reduced_residual(p,B,r,ell,mu,K):
    q=p.arithmetic().full_operator(r,ell,mu,K,0)[2]
    phi=s.Function('phi',real=True)(r)
    pot=mu**2*s.exp(4*r/ell)+ell**-2+(K/ell)**2*s.exp(2*r/ell)
    return (q[0]*B.diff(r)+q[1]*B).applyfunc(
        lambda v:s.simplify(s.expand(v).subs(s.diff(phi,r,2),pot*phi)))

def test_complete_columns_solve_actual_full_operator_both_charge_signs(modules):
    p,_=modules;r=s.symbols('r',real=True);ell=s.Integer(2);K=s.Rational(2,7)
    phi=s.Function('phi',real=True)(r);L=K/ell*s.exp(r/ell)
    for mu in (s.Rational(1,3),-s.Rational(1,3)):
        B=p.columns(phi,s.diff(phi,r),mu*s.exp(2*r/ell),L,ell)
        assert p.arithmetic().mz(reduced_residual(p,B,r,ell,mu,K))

def test_omitted_mixed_component_fails_same_equation(modules):
    p,_=modules;r=s.symbols('r',real=True);ell=s.Integer(1);K=s.Rational(3,5);mu=s.Rational(2,5)
    phi=s.Function('phi',real=True)(r)
    B=p.columns(phi,s.diff(phi,r),mu*s.exp(2*r),K*s.exp(r),ell)
    B[3,0]=0
    assert not p.arithmetic().mz(reduced_residual(p,B,r,ell,mu,K)[:,0])

def test_actual_trace_is_rank_four_maximal_null_and_wrong_current_fails(modules):
    p,_=modules;F=s.symbols('F',positive=True);G,W=s.symbols('G W',real=True)
    B=p.columns(F,G,W,s.Rational(3,5),s.Integer(2))
    e=p.arithmetic().exterior(0);C=e-e.T
    assert B.rank()==4 and p.arithmetic().mz(B.H*C*B)
    B[1,0]=s.I*F
    assert not p.arithmetic().mz(B.H*C*B)

def test_actual_Weyl_field_map_and_parity_not_eight_particles(modules):
    p,_=modules;F=s.symbols('F',positive=True);G,W=s.symbols('G W',real=True)
    ell=s.Integer(2);L=s.Rational(3,5);B=p.columns(F,G,W,L,ell)
    So,Se=p.physical_maps();odd=So.T*B[:,[1,3]];even=Se.T*B[:,[0,2]]
    assert So.T*So==Se.T*Se==s.eye(4) and So.T*Se==s.zeros(4)
    assert odd==s.Matrix([[0,F],[G+(W+1/ell)*F,0],[s.I*L*F,0],[0,s.I*(-G+(W-1/ell)*F)/L]])
    assert odd.rank()==even.rank()==2 and So*odd+Se*even!=s.zeros(8,2)

def test_angular_zero_profiles_are_four_with_two_each_parity(modules):
    p,_=modules;r=s.symbols('r',real=True);ell=s.Integer(2);beta=s.Rational(2,5)
    phase=beta*ell/2*(s.exp(2*r/ell)-1)
    for sign,supports,offsets in ((1,[0,2,6,4],[-1,0,1,0]),(-1,[3,1,5,7],[0,1,0,-1])):
        Z=s.zeros(8,4)
        for j,(ix,g) in enumerate(zip(supports,offsets)):Z[ix,j]=s.exp(g*r/ell-phase)
        q=p.arithmetic().full_operator(r,ell,sign*beta,0,0)[2]
        assert Z.rank()==4 and p.arithmetic().mz(q[0]*Z.diff(r)+q[1]*Z)
        assert sum(ix.bit_count()%2==0 for ix in supports)==2

def test_neutral_joint_corner_keeps_two_L2_and_four_threshold_resonances(modules):
    p,_=modules;r=s.symbols('r',real=True);ell=s.Integer(2)
    q=p.arithmetic().full_operator(r,ell,0,0,0)[2]
    N=s.zeros(8,2);N[0,0]=N[7,1]=s.exp(-r/ell)
    C=s.zeros(8,4)
    for j,ix in enumerate((2,3,4,5)):C[ix,j]=1
    assert p.arithmetic().mz(q[0]*N.diff(r)+q[1]*N) and p.arithmetic().mz(q[1]*C)
    assert N.rank()==2 and C.rank()==4
    assert s.integrate(s.exp(-2*r/ell),(r,0,s.oo))==ell/2
    assert s.integrate(s.Integer(1),(r,0,s.oo))==s.oo

def test_Whittaker_and_Euler_projectors_agree_not_just_dimensions(results):
    native,reference=results
    with mp.workdps(50):
        lookup={(row['sign'],row['K']):row for row in native['numeric_projectors']}
        for row in reference['numeric_projectors']:
            other=lookup[(row['sign'],row['K'])]
            assert abs(mp.mpf(row['scalar_log_derivative'])-mp.mpf(other['scalar_log_derivative']))<mp.mpf('1e-20')
            a=mp.matrix([[mp.mpc(v['re'],v['im']) for v in line] for line in row['projector']])
            b=mp.matrix([[mp.mpc(v['re'],v['im']) for v in line] for line in other['projector']])
            assert max(abs(v) for v in a-b)<mp.mpf('1e-20')
            assert abs(sum(a[i,i] for i in range(8))-4)<mp.mpf('1e-20')

def test_numerical_grades_limits_and_zero_wall_scalar_control_are_separate(results):
    native,reference=results
    for result,key in ((native,'checks'),(reference,'exact_checks')):
        assert result[key] and all(type(v) is bool and v for v in result[key].values())
        for value in result['numerical_checks'].values():
            assert value['passed'] and mp.mpf(value['residual'])<mp.mpf(value['tolerance'])
            assert value['grade'] in ('precision','finite_limit')
        assert any(v['grade']=='finite_limit' for v in result['numerical_checks'].values())
    assert native['complete_end_dimension']==4 and native['neutral_corner_L2_dimension']==2
    assert native['odd_even_dimensions']==[2,2]
    assert not native['core_join_solved'] and not native['global_particles_or_chirality']
    assert not native['SM_selection_derived'] and not reference['SM_selection_derived']
