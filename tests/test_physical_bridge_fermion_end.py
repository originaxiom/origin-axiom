"""R61 local mathematical controls with explicit false-admission comparators."""
import importlib.util
from pathlib import Path
import pytest
import sympy as s

spec = importlib.util.spec_from_file_location('fermion_end', Path(__file__).resolve().parents[1]/
                                            'reports/physical_bridge_2026_09_05/fermion_end.py')
F = importlib.util.module_from_spec(spec)
spec.loader.exec_module(F)


def test_full_clifford_and_hodge_transport():
    assert all(F.clifford().values())


def test_combined_reality_not_separate_real_conditions():
    for kind in ('square', 'hexagonal'):
        r = F.boundary(kind)['checks']
        assert r['combined_reality'] and r['combined_reality_involution']
        assert r['bare_star_fails'] and r['bare_conjugation_fails']
        assert r['real_line_control'] and r['helicity_line_is_not_real']


def test_hermitian_green_current_and_wrong_complement():
    for kind in ('square', 'hexagonal'):
        r = F.boundary(kind)['checks']
        assert r['maximal_current_cancellation'] and r['conjugate_line_current_cancellation']
        assert r['wrong_complement_rejected']


def test_rotations_and_two_distinct_reflection_operations():
    for kind in ('square', 'hexagonal'):
        r = F.boundary(kind)['checks']
        assert r['metric_and_rotation'] and r['rotation_preserves_complex_domain']
        assert r['reflection_exchanges_domains'] and r['anti_reflection_model_preserves_domain']


def test_extreme_domains_fail_the_actual_combined_test():
    for kind in ('square', 'hexagonal'):
        r = F.boundary(kind)['checks']
        assert r['extremes_still_cancel_current'] and r['extremes_fail_reality']


def test_multiplet_constraint_does_not_erase_gauge_or_susy_derivatives():
    r = F.boundary('hexagonal')
    P, w = r['projector'], r['line']
    assert F.zero((s.eye(2)-P)*w)
    assert F.zero((s.eye(2)-P)*s.zeros(2, 1))
    assert not F.zero(r['real_gauge_derivative_residual'])
    assert r['checks']['coefficient_multiplet_constraint']
    assert r['checks']['susy_derivative_countercontrol']


def test_boundary_wedge_distinguishes_same_and_opposite_lines():
    for kind in ('square', 'hexagonal'):
        r = F.boundary(kind)
        assert r['checks']['common_line_boundary_variation_zero']
        assert not F.zero(r['opposite_wedge'])


def test_scope_and_input_rejection():
    with pytest.raises(ValueError):
        F.boundary('cusp')
    data = F.run()
    assert data['all_checks_pass'] and len(data['checks']) == 50
