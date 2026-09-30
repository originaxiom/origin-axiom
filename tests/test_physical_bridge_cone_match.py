"""R65 exact necessary admission tests; no independent global PDE certificate."""
import importlib.util
from pathlib import Path

import pytest
import sympy as s

PATH = Path(__file__).resolve().parents[1] / 'reports/physical_bridge_2026_09_05/cone_match.py'
SPEC = importlib.util.spec_from_file_location('physical_bridge_cone_match', PATH)
probe = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(probe)


def assert_group(group):
    assert group['checks']
    assert all(group['checks'].values()), group['checks']


def test_actual_words_and_cover_inclusion():
    assert_group(probe.source_controls())
    assert probe.word((1, -1), [((1, 0), (2, -2))]) == probe.one(2)
    assert probe.word((1, 1), [((1, 0), (2, -2))]) == probe.one(2)


@pytest.mark.parametrize('number', [0, 1])
def test_both_monomial_families_on_both_covers(number):
    group = probe.monomial_controls(number)
    assert_group(group)
    for row in group['peripheral'].values():
        assert row['meridian'][1] == row['longitude'][1] == (0,)*5
        assert all(n is not None and n >= 1 for n in row['orders'])


def test_two_period_map_and_all_log_branches():
    for kind in ('square', 'hexagonal'):
        group = probe.period_controls(kind)
        assert_group(group)
        assert group['real_modulus_matrix'].rank() == 2


def test_literal_projective_meridian_and_arbitrary_powers():
    group = probe.projective_controls()
    assert_group(group)
    assert (group['meridian']-s.eye(4)).rank() == 2


def test_bounded_transport_and_singular_countercontrols():
    assert_group(probe.transport_controls())


def test_positive_global_abelian_control_and_charged_window():
    for kind in ('square', 'hexagonal'):
        group = probe.abelian_controls(kind)
        assert_group(group)
        assert group['longitude'] == s.eye(5)
        assert group['zero_root_lower_bound'] > s.Rational(3, 4)


def test_all_groups_and_declared_link_scope():
    answer = probe.run()
    assert answer['all_checks_pass']
    assert all(answer['checks'].values())
    with pytest.raises(ValueError):
        probe.period_controls('unspecified')
