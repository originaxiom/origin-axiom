"""LIVE locks for one frozen compact coefficient; no physical bank certificate."""
import importlib.util
import json
from pathlib import Path

import pytest
import sympy as s

BASE = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/silver_operator_gate_2026_10_05'


def load(name):
    spec = importlib.util.spec_from_file_location('silver_gate_'+name,BASE/(name+'.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope='module')
def native():
    return load('probe')


@pytest.fixture(scope='module')
def reading(native):
    return native.run()


def test_literal_marking_and_actual_cocycle(native):
    data = json.loads((BASE/'candidate.json').read_text())
    assert native.marked_relators()==data['relators']==['taTbba','tbTbbabbab']
    v = native.four(data)
    cx = native.Complex({g:native.restrict(m) for g,m in v.items()},data)
    c = s.Matrix([s.Rational(a)+s.sqrt(2)*s.Rational(b) for a,b in data['cocycle_Qsqrt2_pairs']])
    cr = s.Matrix([x for entry in c for x in native.pairs(entry)])
    assert cx.F*cr==s.zeros(16,1) and cx.R*cr==s.zeros(16,1)
    assert native.rank(cx.B.row_join(cr))==native.rank(cx.B)+1
    wrong = cr.copy(); wrong[0] += 1
    assert cx.F*wrong!=s.zeros(16,1)


def test_full_counts_keep_all_three_frames(reading):
    a,b = reading['profiles']['W'],reading['profiles']['wedge2W']
    assert a['difference']=={'h1_absolute':-1,'h1_relative':0,'h1_interior':-1}
    assert b['difference']=={'h1_absolute':1,'h1_relative':-1,'h1_interior':-1}
    assert reading['V']['h1_interior']==1
    assert a['dual']['h0_absolute']==1 and a['E']['h0_absolute']==0


def test_actual_endpoint_modes_complete_the_graded_kernels(reading):
    a = reading['profiles']['W']
    assert a['E']['absolute_betti']==[0,2,2,0]
    assert a['dual']['absolute_betti']==[1,3,2,0]
    assert a['E']['relative_betti']==[0,2,3,1]
    assert a['dual']['relative_betti']==[0,2,2,0]
    b = reading['profiles']['wedge2W']
    assert b['E']['absolute_betti']==[0,4,4,0]
    assert b['dual']['absolute_betti']==[0,3,3,0]
    assert b['E']['relative_betti']==[0,3,3,0]
    assert b['dual']['relative_betti']==[0,4,4,0]
    for pair in reading['profiles'].values():
        for branch in ('E','dual'):
            for frame in ('absolute','relative'):
                odd,even = pair[branch][frame+'_odd_even']
                assert odd==even
    # Dropping H3 would produce a false -1 in this relative W control.
    assert a['E']['relative_betti'][1]-a['E']['relative_betti'][2]==-1
    assert a['E']['relative_odd_even']==[3,3]


def test_split_and_coboundary_controls(reading):
    assert reading['checks']['coboundary_gauge_invariance']
    assert reading['checks']['literal_dual_invariant_line']
    for label in ('splitW','split_wedge2W'):
        assert all(v==0 for v in reading['profiles'][label]['difference'].values())
    assert reading['profiles']['splitW']['E']['h0_absolute']==1
    assert reading['profiles']['W']['E']['h0_absolute']==0


def test_field_dual_and_exterior_order_are_real_constraints(native):
    q = s.Matrix([[1,s.sqrt(2)],[0,2]])
    correct = native.restrict(q.inv().T)
    assert native.dual({'a':native.restrict(q)})['a']==correct
    assert native.inverse(native.restrict(q)).T!=correct
    m = s.eye(5); m[0,1] = s.sqrt(2)
    assert native.restrict(native.wedge(m)).shape==(20,20)
    assert native.wedge(native.restrict(m)).shape==(45,45)
    with pytest.raises(ValueError,match='outside'):
        native.pairs(s.sqrt(3))


def test_green_current_and_combined_reality_not_separate_factors(native):
    g,a,r,j,p = native.boundary_matrices()
    assert a.rank()==r.rank()==4 and g.det()==1
    assert a*g*a==r*g*r==s.zeros(8)
    assert j*j==s.eye(8) and j*a*j==r
    assert j*a!=a*j
    # An unrestricted trace has a nonzero current; half dimension matters.
    assert g!=s.zeros(8)
    assert a*p==p*a and r*p==p*r


def test_scalar_boundary_flux_cannot_be_dropped(native):
    assert native.boundary_control()['twisted_energy']==0
    k = s.symbols('k',real=True,nonzero=True)
    L = s.symbols('L',positive=True)
    r = s.symbols('r',real=True)
    u = s.exp(-k*r)
    energy = s.integrate(s.diff(u,r)**2+k**2*u**2,(r,-L,L))
    flux = k*(u.subs(r,L)**2-u.subs(r,-L)**2)
    assert s.simplify(energy+flux)==0
    assert s.simplify(energy-flux-4*k*s.sinh(2*k*L))==0
    assert energy.subs({k:1,L:1})>0
    assert s.diff(u,r).subs({r:L,k:1})!=0
    assert s.diff(u,r)+k*u==0


def test_direct_field_reference_and_full_semantic_tables(reading):
    ref = load('reference')
    rr = ref.run()
    assert reading['profiles']==rr['profiles'] and reading['V']==rr['V']
    assert reading['boundary_control']==rr['boundary_control']
    assert ref.K(1,1)*ref.K(-1,1)==1
    assert ref.inverse([[ref.K(1),ref.K(0,1)],[ref.K(0),ref.K(2)]])==[
        [ref.K(1),ref.K(0,'-1/2')],[ref.K(0),ref.K('1/2')]]
    assert not reading['physical_goal_achieved'] and not rr['physical_goal_achieved']
