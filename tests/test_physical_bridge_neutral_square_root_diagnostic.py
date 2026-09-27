"""Supplementary noncommuting fixture, not an edit to the failed original."""
import importlib.util
from pathlib import Path

PATH = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/neutral_square_root_diagnostic.py'
SPEC = importlib.util.spec_from_file_location('r52_square_diagnostic', PATH)
r = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(r)


def test_old_fixture_defect_remains_a_visible_result():
    c = r.controls()
    assert c['original_fixture_is_polynomial_in_S']
    assert c['original_fixture_commutes'] and c['original_failures_preserved']


def test_new_fixture_rejects_both_incorrect_derivative_shortcuts():
    c = r.controls()
    assert c['replacement_commutator_explicit'] and c['first_solution_noncommuting']
    assert c['second_solution_noncommuting']
    assert c['commuting_shortcut_rejected'] and c['second_product_omission_rejected']


def test_symbolic_sylvester_control_and_positive_spectrum():
    c = r.controls()
    assert c['fully_symbolic_symmetric_tangent'] and c['positive_sylvester_spectrum']


def test_all_supplementary_predicates():
    c = r.controls()
    assert len(c) == 13 and all(bool(x) for x in c.values())
