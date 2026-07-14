"""B599 — the theta-parity selection rule (stage face locks).

See frontier/B599_selection_rule/FINDINGS.md.
"""
import importlib.util
import os

import numpy as np

_ROOT = os.path.join(os.path.dirname(__file__), "..")
_spec = importlib.util.spec_from_file_location(
    "b238m9", os.path.join(_ROOT, "frontier", "B238_su32_levelrank", "su32_wrt.py"))
b238 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b238)


def _setup():
    w, S, T, c = b238.su3_data(2)
    n = len(w)
    C = np.zeros((n, n))
    for i, wt in enumerate(w):
        C[w.index((wt[1], wt[0])), i] = 1.0
    return n, S, T, C


def test_ingredients():
    n, S, T, C = _setup()
    assert np.allclose(C @ C, np.eye(n))
    assert np.allclose(C @ S, S @ C, atol=1e-9)
    assert np.allclose(C @ T, T @ C, atol=1e-9)


def test_selection_rule_random_configurations():
    n, S, T, C = _setup()
    Pp, Pm = (np.eye(n) + C) / 2, (np.eye(n) - C) / 2
    rng = np.random.default_rng(7)

    def hvec(par):
        v = rng.normal(size=n) + 1j * rng.normal(size=n)
        return (Pp if par == 0 else Pm) @ v

    def hop(par):
        W = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
        return (Pp @ W @ Pp + Pm @ W @ Pm) if par == 0 else (Pp @ W @ Pm + Pm @ W @ Pp)

    evens = 0
    for _ in range(120):
        kins = rng.integers(0, 4)
        pars = [int(rng.integers(0, 2)) for _ in range(2 + kins)]
        bra, ket = hvec(pars[0]), hvec(pars[1])
        M = np.eye(n, dtype=complex)
        for p in pars[2:]:
            M = M @ hop(p)
        A = np.conj(bra) @ M @ ket
        if sum(pars) % 2 == 1:
            assert abs(A) < 1e-10          # forced zero
        else:
            evens += 1
    assert evens > 20                       # the even side is generic (non-vacuous)
