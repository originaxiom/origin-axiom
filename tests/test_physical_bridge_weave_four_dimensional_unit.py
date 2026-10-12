"""Total metric/source controls; no inferred physical generation spectrum."""
import importlib.util
from pathlib import Path
import pytest
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
PACKET=ROOT/'reports/physical_bridge_2026_09_05/weave_four_dimensional_unit_2026_10_12'
def load(name):
    spec=importlib.util.spec_from_file_location('unit_lift_'+name,PACKET/(name+'.py'))
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module
@pytest.fixture(scope='module')
def modules():return load('probe'),load('reference')
@pytest.fixture(scope='module')
def results(modules):return modules[0].run(),modules[1].run()

def test_actual_metric_and_orthonormal_coframe_agree(results):
    native,reference=results;A=s.Matrix(native['metric']);B=s.Matrix(reference['metric'])
    assert A.shape==B.shape==(4,4) and all(s.simplify(v)==0 for v in A-B)
    assert A[2,3]!=0

def test_full_Hodge_response_and_square_not_base_only(modules):
    p,_=modules;G=p.metric(s.Rational(1,3),s.Integer(2),s.Integer(3),s.Integer(5))
    F=p.twoform(0,1,-s.I*3/2);vol=s.Rational(45,4)
    star=p.hodge(G,vol,F)
    assert star==p.twoform(2,3,-s.I*10/3)
    assert p.hodge(G,vol,star)==F
    assert p.hodge(G,vol/5,F)!=star

def test_actual_S_and_T_metric_descent_and_holomorphic_coordinates(results):
    native,_=results
    for name in ('actual_full_metric_S_automorphy','actual_full_metric_T_automorphy',
                 'actual_curvature_S_automorphy','actual_curvature_T_automorphy',
                 'actual_holomorphic_coordinates_not_only_J_square','actual_closed_Kahler_form'):
        assert native['checks'][name]
    p=load('probe');G=p.metric(s.Integer(1),s.Integer(2),s.Integer(3),s.Integer(5))
    bad=s.diag(1,1,2,1)
    assert bad.T*G*bad!=G

def test_varying_fibre_area_really_changes_YM_equation(modules):
    p,_=modules;y=s.symbols('y',positive=True);x=s.symbols('x',real=True)
    G=p.metric(x,y,s.Integer(2),1+y);F=p.twoform(0,1,-6*s.I/y**2)
    response=p.hodge(G,4*(1+y)/y**2,F)
    assert s.diff(response[2,3],y)==-s.Rational(3,2)*s.I
    zero=p.hodge(G,4*(1+y)/y**2,s.zeros(4))
    assert zero==s.zeros(4)

def test_total_stack_action_keeps_central_involution_and_finite_tail(results):
    native,reference=results;En=s.sympify(native['total_action']);Er=s.sympify(reference['total_action'])
    assert s.simplify(En-Er)==0
    names={str(v):v for v in En.free_symbols};ell,A,g,n=[names[k] for k in ('ell','A','g','n')]
    assert s.simplify(En-3*s.pi*A*n*n/(g*g*ell*ell))==0
    assert En.subs(n,0)==0 and En.subs(n,1)!=2*En.subs(n,1)
    tail=s.sympify(native['tail_action']);Y=next(v for v in tail.free_symbols if str(v)=='Y')
    assert s.limit(tail,Y,s.oo)==0

def test_pure_base_degree_four_detector_recovers_mixed_curvature(modules):
    p,r=modules;F=p.twoform(0,1,-6*s.I)
    assert p.wedge_square(F)==0
    mixed=F+p.twoform(2,3,s.I)
    assert p.wedge_square(mixed)==12
    assert r.wedge({3:-6*s.I,12:s.I},{3:-6*s.I,12:s.I})=={15:12}

def test_nonzero_flux_is_not_zero_moment_or_a_selected_unit(results):
    native,_=results;moment=s.sympify(native['kahler_moment']);n=next(v for v in moment.free_symbols if str(v)=='n')
    assert moment.subs(n,0)==0 and moment.subs(n,1)!=0 and moment.subs(n,-1)==-moment.subs(n,1)
    assert native['checks']['zero_flux_not_excluded'] and native['checks']['opposite_sign_not_selected']

def test_metric_lift_does_not_claim_a_complete_physical_three_family_operator(results):
    native,reference=results
    assert all(native['checks'].values()) and all(reference['exact_checks'].values())
    assert not native['fibre_complete'] and not native['physical_Dirac_index_computed']
    assert not native['unit_selected'] and not native['three_physical_generations_derived']
    assert not reference['three_physical_generations_derived']
