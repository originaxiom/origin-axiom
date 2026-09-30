"""R60 explicit countercontrols; no physical chirality is asserted."""
import importlib.util
from pathlib import Path

import pytest
import sympy as s

P=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/end_law.py'
spec=importlib.util.spec_from_file_location('end_law',P)
E=importlib.util.module_from_spec(spec)
spec.loader.exec_module(E)


def test_all_subsets_lattice_lemma():
    rows=E.lattice()
    assert len(rows)==26
    assert sum(r['rotation'] for r in rows)==7
    assert all(r['rotation'] != r['has_line'] for r in rows)
    assert {r['ambient'] for r in rows}=={'D4','D6'}


def test_projective_orbit_does_not_require_shortest_lines():
    checks,orbit=E.marking_and_slopes()
    assert checks['root_orbit'] and checks['nonroot_orbit'] and checks['nonroot_length']
    assert set(orbit)=={(1,3),(3,2),(2,-1)}
    with pytest.raises(ValueError):
        E.line((0,0))


def test_marked_equivariance_is_not_unmarked_invariance():
    checks,_=E.marking_and_slopes()
    assert checks['oriented_conjugacy'] and checks['marking_equivariance']
    assert checks['marking_changes_line']


def test_self_adjoint_green_condition_is_not_poincare_self_duality():
    rows,bad,invariant=E.domains()
    assert invariant and bad
    assert [r['dim_W'] for r in rows]==[0,2,1]
    assert all(r['boundary_dim']==2 and r['isotropic'] for r in rows)
    assert all(r['rotation_invariant'] for r in rows[:2])
    assert not any(r['poincare_self_dual'] for r in rows[:2])
    assert rows[2]['poincare_self_dual'] and not rows[2]['rotation_invariant']


def test_metric_change_changes_end_norms():
    assert all(E.metric().values())


def test_actual_nonabelian_variation_has_boundary_and_cubic():
    checks,detail=E.action()
    assert all(checks.values())
    assert s.sympify(detail['boundary_derivative'])!=0
    assert s.sympify(detail['cubic'])!=0


def test_wedge_and_exterior_signs_independently():
    x,y,z=s.symbols('x y z')
    assert E.wedge({(0,):1},{(1,):1})=={(0,1):1}
    assert E.wedge({(1,):1},{(0,):1})=={(0,1):-1}
    assert E.wedge({(0,):1},{(0,):1})=={}
    derivative=E.exterior({(0,):y*z,(1,):x*z},(x,y,z))
    assert all(s.expand(v)==0 for v in E.exterior(derivative,(x,y,z)).values())


def test_native_summary_keeps_physical_scope():
    data=E.run()
    assert data['all_checks_pass'] and all(data['checks'].values())
    assert len(data['checks'])>=25
