"""Live R92 affine mathematics, including two opposite erroneous-verdict controls."""
import importlib.util
import sys
from pathlib import Path

path = Path(__file__).resolve().parents[1] / 'reports/physical_bridge_2026_09_05/affine_spin.py'
spec = importlib.util.spec_from_file_location('pb_r92', path)
M = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = M
spec.loader.exec_module(M)


def test_actual_orbit_is_not_its_additive_span():
    group = M.closure(M.fixtures()['tetrahedral'])
    data = M.orbit_data(group)
    assert len(group) == 24 and len(data['preserving']) == 4
    assert len(data['additive_span']) == 8
    assert (1, 1, 0) not in data['preserving']


def test_complete_group_can_still_get_false_fix_from_ordinary_closure():
    data = M.orbit_data(M.closure(M.fixtures()['tetrahedral']))
    assert not data['true_fix'] and data['shortcut_fix']


def test_linear_transport_in_the_defect_product_is_essential():
    p, q, _ = M.fixtures()['tetrahedral']
    assert M.compose(p, q).b == (0, 1, 0)
    assert M.add(p.b, q.b) == (1, 0, 0)
    assert M.compose(p, q).b == M.add(p.b, M.mv(p.a, q.b))


def test_fixed_equation_and_exhaustive_action_agree():
    for fixture in M.fixtures().values():
        for g in M.closure(fixture):
            assert M.fixed_equation(g) == {x for x in M.points(3) if g(x) == x}


def test_false_fix_survives_all_origin_changes():
    group = M.closure(M.fixtures()['tetrahedral'])
    for u in M.points(3):
        data = M.orbit_data({M.rebase(g, u) for g in group})
        assert not data['true_fix'] and data['shortcut_fix']


def test_translation_coset_rule_has_both_correct_outcomes():
    for name, fix in [('translation_swap', False), ('translation_fix', True)]:
        data = M.orbit_data(M.closure(M.fixtures()[name]))
        assert data['preserving'] == data['additive_span']
        assert data['true_fix'] == data['shortcut_fix'] == fix


def test_nontrivial_linear_action_does_not_by_itself_kill_the_coset():
    group = M.closure(M.fixtures()['nontrivial_subgroup_orbit'])
    data = M.orbit_data(group)
    assert any(g.a != M.identity(3) for g in group if not g.reverse)
    assert data['preserving'] == data['additive_span']
    assert not data['true_fix'] and not data['shortcut_fix']


def test_incomplete_sample_can_get_opposite_false_swap():
    fixture = M.fixtures()['translation_fix']
    unit = M.Affine(M.identity(3), (0, 0, 0))
    assert not M.orbit_data({unit, fixture[-1]})['shortcut_fix']
    assert M.orbit_data(M.closure(fixture))['true_fix']


def test_order_two_parent_lift_obstruction_and_odd_order_control():
    checks = M.evaluate()['checks']
    assert checks['no_section_on_order_two_subgroup']
    assert checks['both_order_two_lifts_have_order_four']
    assert checks['order_three_has_homomorphic_lift']


def test_all_live_checks_and_scope():
    result = M.evaluate()
    assert all(result['checks'].values())
    for name in ('actual_manifold_table_recomputed', 'physical_chirality_derived',
                 'generated_spin_selection_derived', 'physical_goal_achieved', 'non_author_acceptance'):
        assert result[name] is False
