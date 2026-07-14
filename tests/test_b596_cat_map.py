"""B596 — the clock is not the naive cat-map period (locks).

The null-with-structure: the registered candidate laws fail on the sweep;
the specific counterexample rows are locked. See
frontier/B596_cat_map/FINDINGS.md.
"""
import importlib.util
import os

import numpy as np

_ROOT = os.path.join(os.path.dirname(__file__), "..")
_spec = importlib.util.spec_from_file_location(
    "b238m8", os.path.join(_ROOT, "frontier", "B238_su32_levelrank", "su32_wrt.py"))
b238 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b238)


def _clock(k, cap=200):
    w, S, T, c = b238.su3_data(k)
    n = len(w)
    Si, Ti = np.linalg.inv(S), np.linalg.inv(T)
    M = T @ (Si @ Ti @ S)
    prs = [(i, w.index((wt[1], wt[0]))) for i, wt in enumerate(w)
           if (wt[1], wt[0]) > wt]
    odd = np.zeros((n, len(prs)))
    for j, (a, b) in enumerate(prs):
        odd[a, j], odd[b, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)
    B = odd.T @ M @ odd
    P = np.eye(len(prs), dtype=complex)
    for m in range(1, cap + 1):
        P = P @ B
        if np.allclose(P, np.eye(len(prs)), atol=1e-8):
            return m
    return None


def _ord_mod(m, cap=10000):
    A = np.array([[2, 1], [1, 1]], dtype=object)
    I = np.eye(2, dtype=object)
    P = I.copy()
    for k in range(1, cap + 1):
        P = (P @ A) % m
        if np.array_equal(P, I % m):
            return k
    return None


def test_counterexample_rows():
    # kappa = 4: clock SHORTER than the classical order (kills divisibility)
    assert _clock(1) == 1 and _ord_mod(4) == 3
    # kappa = 9: clock 36 vs ord 12 (factor 3 — not metaplectic x2)
    assert _clock(6) == 36 and _ord_mod(9) == 12
    # kappa = 11: clock 20 vs ord 5
    assert _clock(8) == 20 and _ord_mod(11) == 5


def test_lucky_rows_still_hold():
    # the prereg's hand-checks were true but not a law
    assert _clock(2) == 10 and _ord_mod(5) == 10
    assert _clock(3) == 12 and _ord_mod(6) == 12
    assert _clock(4) == 8 and _ord_mod(7) == 8
