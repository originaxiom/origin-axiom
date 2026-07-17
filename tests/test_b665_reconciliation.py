"""B665 locks — the shadow-class law's decisive witnesses."""
import importlib.util
import os

import numpy as np

_ROOT = os.path.join(os.path.dirname(__file__), "..")
_spec = importlib.util.spec_from_file_location(
    "b238r", os.path.join(_ROOT, "frontier", "B238_su32_levelrank",
                          "su32_wrt.py"))
b238 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b238)


def _stage():
    w, S, T, c = b238.su3_data(2)
    X = np.linalg.inv(S) @ np.linalg.inv(T) @ S
    prs = [(i, w.index((wt[1], wt[0]))) for i, wt in enumerate(w)
           if (wt[1], wt[0]) > wt]
    odd = np.zeros((len(w), len(prs)))
    for j, (a, b) in enumerate(prs):
        odd[a, j], odd[b, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)
    return T, X, odd


def _trodd(word):
    T, X, odd = _stage()
    M = np.eye(T.shape[0], dtype=complex)
    for ch in word:
        M = M @ (T if ch == 'R' else X)
    return np.trace(odd.T @ M @ odd)


def test_trace_does_not_determine_hearing():
    phi = (1 + 5**0.5) / 2
    t1 = _trodd("RLRL")      # trace 7, class of (RL)^2 mod 5
    t2 = _trodd("RRRRRL")    # trace 7, class of L mod 5
    assert abs(abs(t1) - phi) < 1e-9        # a tone OUTSIDE the family's three
    assert abs(t1.imag) < 1e-9              # and REAL
    assert abs(abs(t2) - 1 / phi) < 1e-9    # same trace, different tone
    assert abs(t2.imag) > 1e-3              # and complex


def test_general_word_reality_counterexamples():
    for word in ("RRLL", "RRRLLL"):
        t = _trodd(word)
        assert abs(t - 1.0) < 1e-9          # tr_odd = 1 exactly, REAL
