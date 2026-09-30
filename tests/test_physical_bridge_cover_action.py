"""Finite algebra/domain comparators; global proof remains authored analysis."""
import importlib.util
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / 'reports/physical_bridge_2026_09_05/cover_action.py'
SPEC = importlib.util.spec_from_file_location('pb_cover_action', PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def test_products_brackets_and_proper_algebra():
    assert all(M.algebra_checks().values())


def test_metric_derivative_and_variation_transport():
    assert all(M.kinetic_checks().values())


def test_monomial_transport_does_not_drop_the_metric():
    assert all(M.monodromy_checks().values())


def test_quartic_tensor_is_not_replaced_by_a_norm():
    assert all(M.quartic_checks().values())


def test_symmetry_does_not_choose_one_boundary_domain():
    assert all(M.boundary_checks().values())


def test_two_sided_controls_are_nonvacuous():
    s = M.s
    a,b = s.zeros(6),s.zeros(6)
    a[0,2]=1; b[2,0]=1
    assert M.diagonal_part(M.bracket(a,b)) != M.bracket(M.diagonal_part(a),M.diagonal_part(b))
    assert M.diagonal_part(s.eye(6)) == s.eye(6)
    assert M.equal(s.Matrix([[1]]),s.Matrix([[1]]))
    assert not M.equal(s.Matrix([[1]]),s.Matrix([[2]]))


def test_scope_and_full_finite_population():
    d = M.run()
    assert d['all_checks_pass'] and d['total'] == d['passed'] == 28
    assert not any(d[k] for k in ('actual_m6_index_recomputed','physical_action_selected',
        'physical_end_law_derived','physical_chirality_derived','global_analysis_independently_reviewed'))
