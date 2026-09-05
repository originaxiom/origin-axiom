"""Post-result controls; original R6 science and tests remain byte-identical."""
import importlib.util
from pathlib import Path

import numpy as np
import pytest

from reports.physical_bridge_2026_09_05 import quantum_shift as s
from reports.physical_bridge_2026_09_05 import quantum_vacuum as q


def original_derivative_test():
    path = Path(__file__).with_name("test_physical_bridge_quantum_shift.py")
    spec = importlib.util.spec_from_file_location("r6_sealed_derivative_test", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.test_vector_and_complex_Weyl_mass_derivatives


def test_original_derivative_assertion_rejects_broken_vector_linearity(monkeypatch):
    check = original_derivative_test()
    check()
    original = s.orbit
    extra = np.zeros((186, 78))
    extra[0, 0] = .1
    monkeypatch.setattr(s, "orbit", lambda z: original(z)+extra)
    with pytest.raises(AssertionError):
        check()


def test_original_derivative_assertion_rejects_broken_Weyl_linearity(monkeypatch):
    check = original_derivative_test()
    check()
    original = s.fermion_mass
    monkeypatch.setattr(s, "fermion_mass", lambda z, y: original(z, y)+.1*np.eye(27))
    with pytest.raises(AssertionError):
        check()


def test_scalar_gradient_by_all_explicit_full_Hessian_derivatives():
    geo = q.geometry()
    z = s.vacuum_coordinates()
    parts, h0 = s.one_loop_gradient()
    spectral = s.fprime_matrix(geo["si"]@h0@geo["si"], 1.5, 1.)
    direct = []
    for direction in np.eye(186):
        derivative = geo["si"]@s.tree_hessian_derivative(z, direction, .2)@geo["si"]
        direct.append(np.trace(spectral@derivative).real/(64*np.pi**2))
    assert len(direct) == 186
    np.testing.assert_allclose(direct, parts[0], atol=2e-11, rtol=1e-10)


def test_reduced_nine_mode_singlet_solve_recovers_full_displacement():
    b = s.sm_singlet_basis()
    parts, h0 = s.one_loop_gradient()
    force = parts.sum(axis=0)
    ev, u = np.linalg.eigh(b.T@h0@b)
    positive = ev > 1e-9
    assert np.count_nonzero(positive) == 9
    reduced = -u[:, positive]@((u[:, positive].T@b.T@force)/ev[positive])
    shift = b@reduced
    np.testing.assert_allclose(h0@shift+force, 0, atol=1e-10)
    np.testing.assert_allclose(shift, s.solve_shift()["coordinate_displacement"], atol=1e-10)
