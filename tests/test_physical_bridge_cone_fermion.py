"""R68 finite controls supporting the separately stated local domain argument."""
import importlib.util
from pathlib import Path
import sympy as s

spec = importlib.util.spec_from_file_location('r68_cone_fermion', Path(__file__).resolve().parents[1]/
        'reports/physical_bridge_2026_09_05/cone_fermion.py')
C = importlib.util.module_from_spec(spec)
spec.loader.exec_module(C)


def test_actual_full_operator_from_coordinate_metric():
    result = C.metric_controls()
    assert result['components'] == 32 and result['coefficient_dimension'] == 4
    assert all(result['checks'].values())


def test_variable_flatness_requires_radial_transport():
    assert all(C.flat_controls()['checks'].values())


def test_exact_reducing_coefficient_not_holonomy_centralizer():
    result = C.reducing_controls()
    assert result['reducing_dimension'] == 1 and result['holonomy_dimension'] == 3
    assert all(result['checks'].values())


def test_actual_neutral_traces_have_nondegenerate_Green_form():
    result = C.trace_controls()
    assert result['local_apex_trace_dimension_lower_bound'] == 4
    assert result['Green'].det() == 1
    assert all(result['checks'].values())


def test_kinetic_admission_does_not_imply_L4_or_minimal_trace():
    result = C.trace_controls()
    assert result['kinetic_density'] == 12*C.alpha
    assert result['checks']['critical_L4_diverges']
    assert result['checks']['cutoff_capacity_nonzero']


def test_reality_compatible_linear_domains_and_supercharge_pair():
    result = C.domain_controls()
    assert not C.domain_source.same(result['plus_domain'], result['minus_domain'])
    assert all(result['checks'].values())


def test_complementary_brackets_and_zero_action_holonomy_control():
    result = C.nonlinear_controls()
    assert result['sourced_projection'] == C.Z/3
    assert all(result['checks'].values())


def test_scope_and_all_frozen_groups():
    result = C.run()
    assert set(result['groups']) == {'metric', 'flat', 'reducing', 'trace', 'domain', 'nonlinear'}
    assert result['all_checks_pass']
    assert 'not a full physical end law' in result['scope']
