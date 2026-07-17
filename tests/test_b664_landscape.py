"""B664 locks — the metallic hearing landscape theorem."""
import importlib.util
import os

import numpy as np
import sympy as sp

_ROOT = os.path.join(os.path.dirname(__file__), "..")
_spec = importlib.util.spec_from_file_location(
    "b238l", os.path.join(_ROOT, "frontier", "B238_su32_levelrank",
                          "su32_wrt.py"))
b238 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b238)


def _landscape():
    w, S, T, c = b238.su3_data(2)
    X = np.linalg.inv(S) @ np.linalg.inv(T) @ S
    prs = [(i, w.index((wt[1], wt[0]))) for i, wt in enumerate(w)
           if (wt[1], wt[0]) > wt]
    odd = np.zeros((len(w), len(prs)))
    for j, (a, b) in enumerate(prs):
        odd[a, j], odd[b, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)
    return T, X, odd


def test_golden_trig_identities_exact():
    PHI = (1 + sp.sqrt(5)) / 2
    D2 = 3 * PHI * sp.sqrt(5)
    assert sp.simplify(sp.sin(sp.rad(72))**2 - D2 / 12) == 0
    assert sp.simplify(sp.sin(sp.rad(36))**2 - D2 / (12 * PHI**2)) == 0


def test_closed_form_and_three_values():
    T, X, odd = _landscape()
    phi = (1 + 5**0.5) / 2
    D = (3 * phi * 5**0.5)**0.5
    for n in range(3, 26):
        tr = np.trace(odd.T @ (np.linalg.matrix_power(T, n - 2) @ X) @ odd)
        closed = (2 * np.sqrt(3) / D) * abs(np.cos(np.pi * (4 * n - 5) / 10))
        assert abs(abs(tr) - closed) < 1e-9
        assert min(abs(abs(tr)), abs(abs(tr) - 1 / phi),
                   abs(abs(tr) - 1)) < 1e-9


def test_fact2_refutation_quiet_real_not_unique():
    T, X, odd = _landscape()
    phi = (1 + 5**0.5) / 2
    for n in (12, 18):    # quiet AND real, but not the golden
        tr = np.trace(odd.T @ (np.linalg.matrix_power(T, n - 2) @ X) @ odd)
        assert abs(abs(tr) - 1 / phi) < 1e-9
        assert abs(tr.imag) < 1e-9


def test_t_phases_exact_fifth_root_ratio():
    T, X, odd = _landscape()
    ph = np.angle(np.diag(odd.T @ T @ odd)) / (2 * np.pi) % 1
    assert abs(ph[0] - 2 / 15) < 1e-9 and abs(ph[1] - 8 / 15) < 1e-9
