"""R77 report repair: false/unknown controls, native failure retained."""
import importlib.util
from pathlib import Path
import pytest
import sympy as s


P = Path(__file__).resolve().parents[1] / 'reports/physical_bridge_2026_09_05/source_core_report_control.py'
SPEC = importlib.util.spec_from_file_location('r77_report', P)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def test_ground_symbolic_flags_and_false_outcome_retained():
    answer = M.normalize({'control': {'checks': {'good': s.true, 'bad': s.false}}})
    assert answer['passed'] == 1 and answer['total'] == 2
    assert answer['all_checks_pass'] is False
    assert answer['groups']['control']['checks']['bad'] is False


def test_unknown_and_numeric_flags_rejected():
    for value in (s.Symbol('undecided'), s.Symbol('x') > 0, 1):
        with pytest.raises(TypeError, match='non-ground/non-boolean'):
            M.normalize({'control': {'checks': {'not_a_ground_boolean': value}}})


def test_native_original_collector_failure_still_reproducible():
    with pytest.raises(TypeError, match='BooleanAtom'):
        M.native().run()


def test_corrected_collector_keeps_all_mathematical_groups():
    result = M.run()
    assert set(result['groups']) == {'image', 'action', 'localization', 'profiles', 'duality'}
    assert result['all_checks_pass']
    assert result['passed'] == result['total']
    assert result['groups']['profiles']['checks']['same_hessian_detects_gradient']
