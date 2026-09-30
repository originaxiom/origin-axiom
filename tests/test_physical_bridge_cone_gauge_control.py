"""Separately sealed sign certificate; no original test is rewritten."""
import importlib.util
from pathlib import Path
import sympy as s

spec = importlib.util.spec_from_file_location('cone_gauge_control', Path(__file__).resolve().parents[1]/
                                            'reports/physical_bridge_2026_09_05/cone_gauge_control.py')
C = importlib.util.module_from_spec(spec)
spec.loader.exec_module(C)


def test_original_failure_and_effective_population_remain_visible():
    d = C.run()
    assert len(d['original_checks']) == 95
    assert [k for k, v in d['original_checks'].items() if not v] == ['volterra_kernel_positive_control']
    assert not d['original_all_checks_pass']
    assert len(d['effective_checks']) == 99 and d['all_effective_checks_pass']


def test_unchanged_expression_has_positive_base_and_derivative():
    d = C.repair()
    eta = C.C.eta
    assert d['value_at_zero'] == 1
    assert d['derivative'].is_positive is True
    assert C.C.zero(d['expression']-(2**(2*eta+1)-1))
    assert d['checks']['wrong_sign_rejected']


def test_unknown_inference_and_domain_countercontrols_are_not_erased():
    d = C.repair()
    assert d['original_sign_inference'] is None
    assert d['expression'].subs(C.C.eta, -s.Rational(1, 2)) == 0
    assert d['expression'].subs(C.C.eta, -1) == -s.Rational(1, 2)
    assert len(d['checks']) == 5 and all(d['checks'].values())
