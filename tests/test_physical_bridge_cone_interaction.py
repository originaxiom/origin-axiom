"""R62 finite controls for the separately written all-dimension argument."""
import importlib.util
from pathlib import Path
import pytest
import sympy as s

spec = importlib.util.spec_from_file_location('cone_interaction', Path(__file__).resolve().parents[1]/
                                            'reports/physical_bridge_2026_09_05/cone_interaction.py')
C = importlib.util.module_from_spec(spec)
spec.loader.exec_module(C)


def test_metric_residuals_are_not_assumed_from_the_leading_formula():
    for kind in ('square', 'hexagonal'):
        for row in C.fixtures(kind)['rows'].values():
            assert all(row['checks'].values())


def test_symbolic_trace_identity_includes_the_curvature_term():
    data = C.symbolic_trace()
    assert data['identity'] == 0
    assert data['wrong_factor_nonzero'] and data['radial_cyclic_trace']


def test_flat_nilpotent_trace_has_positive_moment_energy():
    for kind in ('square', 'hexagonal'):
        r = C.fixtures(kind)['rows']['nilpotent_no_radial']
        assert C.zero(r['F']) and not C.zero(r['M']) and r['K'] > 0


def test_cancelling_moment_map_with_radial_field_costs_curvature():
    for kind in ('square', 'hexagonal'):
        r = C.fixtures(kind)['rows']['moment_only_cancel']
        assert C.zero(r['M']) and not C.zero(r['F']) and r['K'] > 0


def test_radial_self_commutator_cannot_be_dropped():
    for kind in ('square', 'hexagonal'):
        assert C.fixtures(kind)['checks']['nonnormal_radial_term_needed']


def test_nonzero_commuting_boundary_data_survive():
    for kind in ('square', 'hexagonal'):
        r = C.fixtures(kind)['rows']['normal_positive']
        assert C.zero(r['F']) and C.zero(r['M']) and r['K'] == 0
        assert r['pairing'] > 0


def test_unitary_and_actual_parent_root_controls():
    for kind in ('square', 'hexagonal'):
        r = C.fixtures(kind)['checks']
        assert r['unitary_comparator'] and r['unitary_residual_covariance']
        assert r['actual_su5_root_inclusion'] and r['wrong_metric_sign_rejected']


def test_asymptotic_threshold_includes_the_logarithmic_boundary():
    r = C.convergence()
    assert all(r['checks'].values())
    assert [x['limit'] for x in r['controls'][:2]] == [s.oo, s.oo]
    assert all(x['limit'] > 0 for x in r['controls'][2:])


def test_normality_is_nonlinear_and_linearization_can_miss_it():
    assert all(C.normality()['checks'].values())


def test_input_scope_and_complete_native_controls():
    with pytest.raises(ValueError):
        C.link('complete cusp')
    with pytest.raises(ValueError):
        C.residuals(s.zeros(2), s.zeros(3), 1)
    data = C.run()
    assert data['all_checks_pass'] and len(data['checks']) == 70
