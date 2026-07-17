"""B661 — the wave-1 identification lock (qdims from the banked stage)."""
import importlib.util
import os

import numpy as np

_ROOT = os.path.join(os.path.dirname(__file__), "..")
_spec = importlib.util.spec_from_file_location(
    "b238w1", os.path.join(_ROOT, "frontier", "B238_su32_levelrank",
                           "su32_wrt.py"))
b238 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b238)


def test_wave1_moduli_are_su32_quantum_dimensions():
    w, S, T, c = b238.su3_data(2)
    phi = (1 + 5**0.5) / 2
    D = (3 + 3 * phi**2)**0.5
    assert set(np.round(np.abs(S[0]), 6)) == {round(1 / D, 6),
                                              round(phi / D, 6)}
    assert np.allclose(np.abs(np.diag(S)), 1 / D, atol=1e-9)


def test_r2l_eigenvalue_correction():
    import sympy as sp
    m = sp.Matrix([[1, 1], [0, 1]])**2 * sp.Matrix([[1, 0], [1, 1]])
    assert m.trace() == 4
    assert sp.simplify(max(m.eigenvals()) - (2 + sp.sqrt(3))) == 0
