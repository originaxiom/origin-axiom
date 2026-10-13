"""Live flag, chain-map, dual and full-degree controls, not a PDE certificate."""
import importlib.util
from pathlib import Path
import pytest
import sympy as s

BASE = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/silver_complete_flag_2026_10_13'


@pytest.fixture(scope='module')
def native():
    spec = importlib.util.spec_from_file_location('flag_live_test', BASE/'probe.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_live_complete_counts_all_degrees(native):
    out = native.run()
    assert len(out['records']) == 16
    for row in out['records'].values():
        assert len(row['H']) == 4 and min(row['H']) >= 0
        assert row['J'] == row['H'][1]+row['H'][3]-row['H'][0]-row['H'][2] == 0
        assert row['H'][0]+row['cone_ranks'][0] == row['dimensions'][0]
        assert row['H'][3]+row['cone_ranks'][2] == row['dimensions'][3]


def test_full_dual_not_naive_same_flag(native):
    rows = native.run()['records']
    for amplitude in (0, 1):
        for slot in ('W', 'F'):
            for sign in (1, -1):
                a, b = rows[f'{amplitude}:{slot}:{sign}'], rows[f'{amplitude}:{slot}dual:{sign}']
                assert a['H'] == b['H'][::-1]
                assert a['positive_rank']+b['positive_rank'] == (5 if slot == 'W' else 10)


def test_induced_flags_not_a_fifth_line_copy(native):
    rows = native.run()['records']
    assert rows['1:W:1']['positive_indices'] == [0, 1, 2, 3]
    assert rows['1:F:1']['positive_indices'] == [0, 1, 2, 4, 5, 7]
    assert rows['1:F:1']['positive_rank'] == 6
    assert rows['1:Fdual:1']['positive_rank'] == 4


def test_actual_peripheral_not_global_split(native):
    out = native.run()['checks']
    assert out['core_flag_not_global_split_1']
    assert out['core_flag_not_global_split_0']
    assert out['noninvariant_cusp_selection_rejected']
    assert out['1_W_False_whole_frame_transport']
    assert out['1_F_True_whole_frame_transport']


def test_wrong_degree_two_sign_is_live_failure(native):
    import json
    data = json.loads((BASE.parent/'silver_operator_gate_2026_10_05/candidate.json').read_text())
    v = native.seed.four(data)
    c = s.Matrix([s.Rational(x)+s.sqrt(2)*s.Rational(y) for x, y in data['cocycle_Qsqrt2_pairs']])
    cell = native.Cell(native.seed.extension(v, c), data)
    projection, inclusion = native.selector(5, [0, 1, 2, 3])
    _, (_, _, _, r1, r2, _, gt) = native.cone(cell, projection, inclusion)
    assert not native.zero(native.mm(gt, r1))
    assert not native.zero(native.mm(-r2, cell.F)-native.mm(gt, r1))


def test_real_wall_controls_and_neutral_limit(native):
    out = native.run()['checks']
    assert all(out['wall_anticommutes_principal_'+str(j)] for j in range(3))
    assert all(out['positive_tail_derivative_'+str(j)] and out['negative_tail_derivative_'+str(j)] for j in range(3))
    assert out['radial_wall_square'] and out['neutral_wall_control']


def test_scope_does_not_complete_or_kill_goal(native):
    out = native.run()
    assert out['passed'] == len(out['checks']) and all(out['checks'].values())
    assert out['analytic_proof_machine_certified'] is False
    assert out['neutral_spectrum_computed'] is False
    assert out['physical_end_or_parent_selected'] is False
    assert out['physical_goal_achieved'] is False
    assert out['compact_three_family_result_retracted'] is False
