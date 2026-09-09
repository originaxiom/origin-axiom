"""Exact R24 connection locks, retaining the original raw-comparison failure."""
import importlib.util
from pathlib import Path

import sympy as sp

SPEC = importlib.util.spec_from_file_location('r24_control_test', Path(__file__).resolve().parents[1]/
                                            'reports/physical_bridge_2026_09_05/global_mass_flux_control.py')
m = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(m)


def test_actual_connection_has_zero_exact_polynomial_residual():
    r = m.connection_control()
    assert r['exact_residual'] == sp.zeros(4)
    assert r['raw_comparison_disagrees']
    assert r['original_structural_boolean'] is False


def test_independent_exterior_action_agrees_without_a_new_intertwiner():
    r = m.connection_control()
    assert r['independent_residual'] == sp.zeros(4)
    assert len(r['basis_residuals']) == 3
    assert all(A == sp.zeros(4) for A in r['basis_residuals'])


def test_missing_factor_reversed_sign_and_wrong_axis_each_fail():
    r = m.connection_control()
    assert len(r['mutant_residuals']) == 3
    assert all(A != sp.zeros(4) for A in r['mutant_residuals'])


def test_connection_rotates_the_actual_arbitrary_mass_vector():
    assert m.connection_control()['mass_rotation_residual'] == sp.zeros(2)
