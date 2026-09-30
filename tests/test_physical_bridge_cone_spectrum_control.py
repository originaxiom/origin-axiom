"""R63 comparison repair without modifying or rebinding the frozen tests."""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location('r63_control', Path(__file__).resolve().parents[1]/
                                            'reports/physical_bridge_2026_09_05/cone_spectrum_control.py')
C = importlib.util.module_from_spec(spec)
spec.loader.exec_module(C)


def test_generic_formula_and_original_polynomial_are_unchanged():
    c = C.polynomial_controls()['checks']
    assert c['characteristic_polynomial'] and c['original_polynomial_unchanged']


def test_both_wrong_polynomials_still_fail_after_generator_repair():
    c = C.polynomial_controls()['checks']
    assert c['wrong_density_shift_rejected'] and c['wrong_coefficient_rejected']


def test_same_printed_symbol_is_not_the_same_variable():
    c = C.polynomial_controls()['checks']
    assert c['diagnostic_mismatch_reproduced'] and c['diagnostic_generator_equality']


def test_effective_controls_pass_and_the_first_failure_remains():
    data = C.run()
    assert not data['original_all_checks_pass']
    assert {k for k, v in data['original_checks'].items() if not v}=={'spectrum_characteristic_polynomial'}
    assert len(data['effective_checks'])==73 and all(data['effective_checks'].values())
    assert data['all_effective_checks_pass'] and all(data['repair']['checks'].values())
