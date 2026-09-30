"""R64 finite locks; the authored local existence argument needs separate review."""
import importlib.util
from pathlib import Path
import pytest
import sympy as s

spec = importlib.util.spec_from_file_location('cone_gauge', Path(__file__).resolve().parents[1]/
                                            'reports/physical_bridge_2026_09_05/cone_gauge.py')
C = importlib.util.module_from_spec(spec)
spec.loader.exec_module(C)


def test_nonlinear_operator_uses_the_actual_cone_metric():
    for kind in ('square', 'hexagonal'):
        d = C.metric_controls(kind)['checks']
        assert d['full_curvature_zero'] and d['moment_from_metric']
        assert d['radial_equation_annuls_moment'] and d['root_inclusion']


def test_compact_and_positive_transformations_are_not_identified():
    for kind in ('square', 'hexagonal'):
        d = C.metric_controls(kind)['checks']
        assert d['compact_unitary'] and d['compact_full_residual_zero']
        assert d['compact_radial_Higgs_zero'] and d['positive_not_unitary']
        assert d['positive_radial_detector']


def test_radial_and_moment_countercontrols_can_fail():
    for kind in ('square', 'hexagonal'):
        d = C.metric_controls(kind)['checks']
        assert d['wrong_radial_omission_rejected'] and d['wrong_product_metric_rejected']
        assert d['wrong_nonlinear_sign_rejected'] and d['quadratic_source_nonzero']


def test_paired_primitives_and_stabilizer_are_both_retained():
    d = C.pair_controls()
    assert d['checks']['both_roots_are_R63_modes']
    assert d['checks']['opposite_sign_is_same_stabilizer_orbit']
    assert all(d['checks'].values())
    for kind in ('square', 'hexagonal'):
        assert C.metric_controls(kind)['checks']['tangent_is_negative_covariant_primitive']


def test_volterra_inverse_cubic_and_strict_contraction():
    d = C.volterra_controls()
    assert d['cubic_coefficient'] == 4*(C.eta+1)/(3*(4*C.eta+1))
    assert d['correction_bound'] == s.Rational(1, 12)
    assert d['lipschitz_bound'] == s.Rational(1, 8)
    assert all(d['checks'].values())


def test_full_residual_zero_is_not_separate_graph_admission():
    for kind in ('square', 'hexagonal'):
        d = C.metric_controls(kind)['checks']
        for key in ('background_adjoint', 'shell_adjoint_cubic', 'compact_gauge_component_zero',
                    'exact_flatness_retains_quadratic_source', 'pairing_density',
                    'bracket_density', 'pairing_leading_coefficient', 'bracket_leading_coefficient'):
            assert d[key]


def test_improper_integrals_include_both_logarithmic_thresholds():
    d = C.threshold_controls()
    assert d['L4_integrals'][:2] == [s.oo, s.oo]
    assert d['moment_integrals'][:2] == [s.oo, s.oo]
    assert all(d['checks'].values())


def test_outer_boundary_flux_cannot_be_discarded():
    d = C.boundary_controls()
    assert d['energy'] == d['outer_flux']
    assert d['energy'] != 0
    assert all(d['checks'].values())


def test_all_groups_and_invalid_link_scope():
    with pytest.raises(ValueError):
        C.geometry('complete hyperbolic cusp')
    d = C.run()
    assert set(d['groups']) == {'square', 'hexagonal', 'pair', 'volterra', 'thresholds', 'boundary'}
    assert len(d['checks']) == 95
    assert d['all_checks_pass']
