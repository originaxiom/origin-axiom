"""Actual period/operator controls. No global PDE or full SM acceptance."""
from collections import Counter
import importlib.util
from pathlib import Path
import pytest
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
PACKET=ROOT/'reports/physical_bridge_2026_09_05/silver_gauge_end_transport_2026_10_12'
def load(name):
    spec=importlib.util.spec_from_file_location('gauge_end_'+name,PACKET/(name+'.py'))
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module

@pytest.fixture(scope='module')
def modules():return load('probe'),load('reference')
@pytest.fixture(scope='module')
def results(modules):return modules[0].run(),modules[1].run()

def test_actual_presented_period_space_and_not_two_free_boundary_periods(results):
    native,_=results
    R=s.Matrix(native['period_relation_matrix']);P=s.Matrix(native['peripheral_map'])
    assert R.rank()==2 and R.nullspace()==[s.Matrix([0,0,1])]
    assert P*R.nullspace()[0]==s.Matrix([0,1])
    assert P*s.Matrix([1,0,1])!=s.Matrix([0,1])

def test_actual_gauge10_holonomy_and_special_fixed_spaces(results):
    n,_=results;weights=[int(k) for k,v in n['gauge10_weights'].items() for _ in range(v)]
    assert Counter(weights)=={4:3,-1:6,-6:1}
    z=s.symbols('z',nonzero=True);mat=s.diag(*(z**w-1 for w in weights))
    assert mat.rank()==10 and mat.subs(z,1).rank()==0 and mat.subs(z,-1).rank()==6

def test_two_methods_agree_on_entire_operator_not_only_counts(results):
    n,r=results
    A=s.Matrix(n['full_potential_matrix']);B=s.Matrix(r['full_potential_matrix'])
    assert A.shape==(8,8) and all(s.simplify(v)==0 for v in A-B)
    assert A[1,2]!=0 and A[1,4]!=0

def test_missing_weight_mutation_breaks_the_actual_complex(modules):
    p,_=modules;r,ell,mu,kx,ky=s.symbols('r ell mu kx ky',real=True)
    d,_,_,_=p.full_operator(r,ell,mu,kx,ky)
    bad,_,_,_=p.full_operator(r,ell,mu,kx,ky,omit_weight=True)
    assert all(p.mz(x) for x in p.compose(d,d,r))
    assert not all(p.mz(x) for x in p.compose(bad,bad,r))

def test_false_zero_mixing_is_rejected_by_nonzero_actual_block(results):
    n,_=results;V=s.Matrix(n['full_potential_matrix'])
    actual=V.extract([1,2,4],[1,2,4]);mutated=s.diag(*actual.diagonal())
    assert actual!=mutated and actual[0,1]!=0 and actual[0,2]!=0

def test_actual_static_angular_response_not_old_zero_partner_product(results):
    _,ref=results;vals=ref['static_nonzero_angular_response']
    assert s.Float(vals['plus'])>0 and s.Float(vals['minus'])>0
    assert s.Float(vals['product'])>s.Float('1e-10')
    assert s.Float(vals['product'])!=0

def test_all_degrees_and_opposite_charge_are_retained(results):
    native,_=results;V=s.Matrix(native['full_potential_matrix'])
    assert Counter(i.bit_count() for i in range(8))=={0:1,1:3,2:3,3:1}
    assert V[0,0]==V[7,7]
    mu=next(v for v in V.free_symbols if v.name=='mu')
    assert all(s.simplify(V[i,i]-V[j,j].subs(mu,-mu))==0 for i,j in ((3,4),(5,2),(6,1)))

def test_controls_do_not_claim_global_particles_or_selected_SM(results):
    n,r=results
    assert all(n['checks'].values()) and all(r['exact_checks'].values())
    assert not n['global_core_match'] and not n['generated_SM_selection']
    assert not n['global_particles_or_family_count'] and not r['full_goal_achieved']
