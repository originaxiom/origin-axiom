import importlib.util
from pathlib import Path

import sympy as s

spec=importlib.util.spec_from_file_location('silver_cusp_polarization',Path(__file__).with_name('verify.py'))
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_boundary_controls_include_unequal_dual_invariants():
    result=m.comparators()
    assert result['status']=='PASS'
    assert result['field_conversion_comparators']==84


def test_all_actual_members_in_both_conjugate_structures():
    rows=m.actual_members()
    assert len(rows)==4
    for r in rows:
        assert [x['difference'] for x in r['W']['rows']]==[-1,-1]
        assert [x['difference'] for x in r['wedge2W']['rows']]==[0,0]
        assert r['W']['profile']['E']['h1_interior']-r['W']['profile']['dual']['h1_interior']==-1
        assert r['wedge2W']['profile']['E']['h1_interior']-r['wedge2W']['profile']['dual']['h1_interior']==-1


def test_arbitrary_changed_domain_is_not_a_universal_no_go():
    for r in m.actual_members():
        for row in r['wedge2W']['rows']:
            changed=row['supplied_codimension_one_control']
            assert changed['difference']==-1
            assert changed['dimensions'][0]==row['polar_dimensions'][0]-1
            assert changed['dimensions'][1]==row['polar_dimensions'][1]+1


def test_split_and_global_gauge_controls():
    rows=m.actual_members()
    for r in rows:
        for key in ('splitW','split_wedge2W'):
            assert all(x['difference']==0 for x in r[key]['rows'])
    assert 'gauge_controls' in rows[0]


def test_zero_classes_are_quotiented_not_counted_as_representatives():
    X=s.Matrix([[0,1,0],[0,0,1],[0,0,0]])
    U=s.eye(3)+X+X**2/2
    b=m.Boundary(U,U)
    # tau=1 makes every vector a closed representative, but two are exact.
    assert m.kernel(b.Y-b.X).cols==3
    assert b.pure(1).cols==1


def test_direct_field_and_dual_conventions():
    A=s.Matrix([[1,s.sqrt(2)+s.I],[0,1]])
    assert m.zero(m.mul(A,m.inverse(A))-s.eye(2))
    assert m.zero(m.dual(m.dual({'a':A}))['a']-A)
    assert not m.zero(m.dual({'a':A})['a']-m.inverse(A).conjugate().T)
