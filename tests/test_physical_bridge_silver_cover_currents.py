"""Live exact operator/action controls, not transcript or completion tests."""
import importlib.util
from functools import lru_cache
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/silver_cover_currents_2026_10_12'


@lru_cache(None)
def result(name):
    spec = importlib.util.spec_from_file_location('cover_current_test_'+name, BASE/(name+'.py'))
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    return module.run()


def test_both_live_algorithms_and_actual_weighted_kernels():
    a, b = result('probe'), result('reference')
    assert a['blocks'] == b['blocks']
    for key in ('facts', 'checks'):
        assert all((a if key == 'facts' else b)[key].values())
    assert len(a['blocks']) == 10
    assert all(row['primitive_dimension'] == row['trace_rank'] for row in a['blocks'].values())


def test_three_from_kernel_not_from_replication():
    rows = result('probe')['blocks']
    for key in ('Q', 'uc', 'ec', 'dc', 'L'):
        assert rows[key+'_plus']['primitive_dimension'] == 1
        assert rows[key+'_minus']['primitive_dimension'] == 2
        assert rows[key+'_plus']['H_weight'] != 0


def test_every_explicit_gauge_intertwiner_and_faithfulness():
    for name, field in (('probe', 'facts'), ('reference', 'checks')):
        out = result(name); values = [v for k, v in out[field].items() if 'intertwiner' in k]
        assert len(values) == 12 and all(values)
        assert out['generator_faithfulness_rank'] == 12


def test_actual_charge_assignment_and_wrong_dual_control():
    a, b = result('probe'), result('reference')
    assert a['hypercharges'] == b['hypercharges'] == {'Q': '1/6', 'uc': '-2/3', 'ec': '1', 'dc': '1/3', 'L': '-1/2'}
    assert a['facts']['actual_hypercharge_and_wrong_dual_rejected']
    assert b['checks']['hypercharges_and_wrong_fundamental_control']


def test_kernel_equivariance_under_all_generators():
    values = [v for k, v in result('probe')['facts'].items() if 'kernel_equivariance' in k]
    assert len(values) == 120 and all(values)


def test_positive_nonorthogonal_normalization_and_rejecting_control():
    a = result('probe')['facts']; b = result('reference')['checks']
    assert a['nonorthogonal_fixture_positive_and_deck_compatible']
    assert a['actual_canonical_Gram_congruence'] and a['missing_kinetic_Gram_rejected']
    assert b['nonorthogonal_positive_fixture'] and b['omitted_Gram_fails']
    assert len([v for k, v in a.items() if k.endswith('_normalized_current') and v]) == 60


def test_classical_Ward_identity_with_nonzero_derivative_control():
    a = result('probe')['facts']; b = result('reference')['checks']
    assert len([v for k, v in a.items() if k.endswith('_classical_Ward_first_jet') and v]) == 12
    assert len([v for k, v in b.items() if k.endswith('_first_jet_Ward') and v]) == 12
    assert len([v for k, v in a.items() if k.endswith('_omitted_gauge_derivative_rejected') and v]) == 12


def test_trace_and_volume_normalizations_remain_conditional():
    a, b = result('probe'), result('reference')
    assert a['conditional_gY_squared_over_g5_squared'] == b['conditional_gY_squared_over_g5_squared'] == '3/5'
    assert a['facts']['cover_volume_and_wrong_single_sheet_rejected']
    assert b['checks']['n_points_false_null_n_plus_one_rejects']


def test_current_is_nonzero_but_not_a_three_selector():
    a, b = result('probe'), result('reference')
    assert a['current_support'] == b['current_support']
    assert all(a['current_support'].values())
    assert a['facts']['current_normalization_does_not_select_three']
    assert b['checks']['current_does_not_select_family_number']


def test_scope_flags_after_live_mathematics():
    for name in ('probe', 'reference'):
        out = result(name)
        assert out['actual_gauge_current_map_conditional'] is True
        for key in ('global_profile_Gram_computed', 'Yukawas_computed', 'odd_neutral_interactions_computed',
                    'generated_boundary', 'global_quantum_anomaly', 'outside_review', 'full_goal_achieved'):
            assert out[key] is False
