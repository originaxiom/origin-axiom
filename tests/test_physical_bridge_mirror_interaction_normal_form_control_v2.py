"""Exact residual successor; no weakening or hiding the original R33 failures."""
import importlib.util
from pathlib import Path

import pytest
import sympy as sp

PATH = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/mirror_interaction_normal_form_control_v2.py'
SPEC = importlib.util.spec_from_file_location('physical_bridge_mirror_normal_form_control_v2', PATH)
control = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(control)


@pytest.mark.parametrize('sign', (1, -1))
def test_original_collinear_complex_example_has_exact_zero_residual(sign):
    r = control.check(sign)
    assert sp.expand(r['raw_norm']-10) == 0
    assert r['expanded_norm'] == 10 and r['exact_residual_zero'] and r['rank'] == 16
    assert r['changed_mass_rejected']


@pytest.mark.parametrize('sign', (1, -1))
def test_symbolic_complex_multiple_of_real_vector_not_only_one_point(sign):
    assert control.check(sign)['symbolic_collinear']


@pytest.mark.parametrize('sign', (1, -1))
def test_normalization_does_not_make_a_wrong_complex_gap_claim_pass(sign):
    assert control.check(sign)['noncollinear_counterexample']
