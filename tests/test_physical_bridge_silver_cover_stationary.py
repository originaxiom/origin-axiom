"""Live equation and opposing controls, not assertions of an analytic verdict."""
import importlib.util
from functools import lru_cache
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/silver_cover_stationary_2026_10_13'


@lru_cache(None)
def both():
    out = []
    for name in ('probe', 'reference'):
        spec = importlib.util.spec_from_file_location('stationary_test_'+name, BASE/(name+'.py'))
        module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
        out.append(module.run())
    return out


def test_full_independent_moment_jets_and_energy_agree():
    a, b = both()
    assert a['records'] == b['records']
    assert a['checks']['second_moment_coefficient_retained']
    assert b['checks']['separate_second_moment_not_deleted']


def test_complex_transform_sign_and_actual_curvature():
    a, b = both()
    for k in ('actual_first_complex_transform_sign', 'actual_second_complex_transform_coefficient',
              'curvature_covariance_with_full_derivative_jets', 'wrong_derivative_sign_rejected'):
        assert a['checks'][k]
    assert b['checks']['separate_covariance_full_jets'] and b['checks']['separate_wrong_sign_fails']


def test_real_moment_derivative_includes_connection_jets():
    a, b = both()
    assert a['checks']['full_real_moment_derivative_minus_P']
    assert a['checks']['frozen_connection_derivatives_rejected']
    assert b['checks']['separate_real_moment_derivative'] and b['checks']['separate_frozen_jets_fail']


def test_both_boundary_frames_and_free_normal_jets():
    a, b = both()
    assert a['checks']['both_boundary_values_fixed'] and a['checks']['normal_derivatives_not_frozen']
    assert a['checks']['Dirichlet_positive_frame_identity']
    assert b['checks']['separate_tangential_boundary_fixed'] and b['checks']['separate_normal_jets_free']


def test_Dirichlet_positive_form_not_unrestricted_inverse():
    a, b = both()
    assert a['checks']['actual_Dirichlet_form_positive_no_surface']
    assert a['checks']['unrestricted_parallel_kernel_not_Dirichlet']
    assert a['checks']['wrong_Higgs_sign_rejected']
    assert b['checks']['separate_Dirichlet_energy_positive_exact'] and b['checks']['separate_wrong_Higgs_sign_fails']


def test_complex_configuration_not_quotiented_as_real_gauge():
    a, b = both()
    assert a['checks']['positive_Hermitian_not_unitary']
    assert a['checks']['complex_transform_keeps_flat_not_moment']
    assert b['checks']['separate_complex_is_not_real_gauge']


def test_whole_kernel_when_deck_parity_fails():
    a, b = both()
    assert a['checks']['whole_graded_complex_invertible_change']
    assert a['checks']['whole_three_kernel_not_sector_copy']
    assert a['checks']['deck_parity_fails_at_nonzero_parameter']
    assert a['checks']['old_adjoint_cannot_be_frozen']
    assert b['checks']['fraction_mixed_zero_not_deck_invariant']


def test_index_requires_missing_partner_gap():
    a, b = both()
    assert a['records']['toy_gap_closed'] == b['records']['toy_gap_closed'] == [1, 4, 0]
    assert a['records']['toy_start'] == [0, 3, 0]
    assert a['checks']['index_alone_allows_extra_endpoint_pair'] and b['checks']['fraction_index_not_endpoint_gap']
