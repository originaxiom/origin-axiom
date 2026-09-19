"""R34 rational normal form with a separately tested physical domain."""
import importlib.util
from pathlib import Path

import pytest
import sympy as sp

PATH = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/mirror_quartic_normal_form_control.py'
SPEC = importlib.util.spec_from_file_location('physical_bridge_mirror_quartic_control', PATH)
nf = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(nf)


def test_all_channels_and_mirror_limit_as_exact_rational_identities():
    row = nf.check()
    assert row['original_structural_equality'] is False
    assert row['exact_mirror_residual'] == row['full_numerator_residual'] == 0
    assert row['zero_kappa_residual'] == row['zero_Phi_residual'] == 0
    assert row['changed_coefficient_rejected']


def test_normal_form_instrument_can_pass_and_fail():
    x = sp.Symbol('x')
    assert nf.residual((x*x-1)/(x-1), x+1) == 0
    assert nf.residual((x*x-1)/(x-1), x+2) == -1
    with pytest.raises(ValueError):
        nf.residual(sp.Float(1), sp.Integer(1))


@pytest.mark.parametrize('r,k,phi,want', ((3, 1, 1, sp.Rational(1, 5)),
                                       (5, 2, (3+4*sp.I)/5, sp.Rational(1, 9)),
                                       (1, 0, 1, 1)))
def test_stable_scalar_inputs(r, k, phi, want):
    assert nf.stable_inverse(r, k, phi) == want


@pytest.mark.parametrize('r,k,phi', ((2, 1, 1), (1, 1, 1), (-3, 1, 1)))
def test_pole_and_unstable_scalar_inputs_are_not_rescued_by_cancellation(r, k, phi):
    with pytest.raises(ValueError):
        nf.stable_inverse(r, k, phi)


def test_symbolic_and_complex_stability_inputs_fail_closed():
    with pytest.raises(ValueError):
        nf.stable_inverse(sp.Symbol('r'), 1, 1)
    with pytest.raises(ValueError):
        nf.stable_inverse(sp.I, 1, 1)
