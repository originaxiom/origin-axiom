"""B588 — the sector-exchange theorem (locks). See frontier/B588_sector_exchange/FINDINGS.md."""
import importlib.util
import os

import numpy as np
import pytest

_ROOT = os.path.join(os.path.dirname(__file__), "..")
_spec = importlib.util.spec_from_file_location(
    "b238m4", os.path.join(_ROOT, "frontier", "B238_su32_levelrank", "su32_wrt.py"))
b238 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b238)

PHI = (1 + 5 ** 0.5) / 2


def _a1_weil(kapp):
    n = 2 * kapp
    mu = np.arange(n)
    T = np.exp(1j * np.pi * mu * mu / (2.0 * kapp))
    S = np.exp(-1j * np.pi * np.outer(mu, mu) / kapp) / np.sqrt(n)
    P = np.zeros((n, n))
    for i in range(n):
        P[(-i) % n, i] = 1.0
    return T, S, P


def _rho(word, T, S):
    Rop = np.diag(T)
    Lop = S.conj().T @ np.diag(T).conj() @ S
    M = np.eye(S.shape[0], dtype=complex)
    for ch in word:
        M = M @ (Rop if ch == 'R' else Lop)
    return M


@pytest.mark.parametrize("kapp", [3, 5, 7, 10, 12])
def test_rank1_decomposition_identity(kapp):
    S2, T2, c2 = b238.su2_data(kapp - 2)
    T, S, P = _a1_weil(kapp)
    assert np.allclose(S @ S, P, atol=1e-8)                  # S^2 = parity
    for word in ("RL", "RRLL", "RRRLLL"):
        M = _rho(word, T, S)
        zW = (np.trace(M) - np.trace(M @ P)) / 2.0
        assert abs(zW - b238.wrt_trace(S2, T2, word)) < 1e-7


def test_membership_minus_one():
    # -1 in W(A1): the reflection. -1 not in W(A2): check all six elements.
    S1 = np.array([[-1, 0], [1, 1]])
    S2m = np.array([[1, 1], [0, -1]])
    elems = []
    for word in ((), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)):
        M = np.eye(2, dtype=int)
        for g in word:
            M = (S1 if g == 0 else S2m) @ M
        elems.append(M)
    assert not any(np.array_equal(w, -np.eye(2, dtype=int)) for w in elems)


def test_ingredient_identity_at_five():
    T, S, P = _a1_weil(5)
    M = _rho("RL", T, S)
    tp, tm = np.trace(M), np.trace(M @ P)
    assert abs(tp - 1) < 1e-8                                # unit conductor
    assert abs(tm - np.sqrt(5)) < 1e-8                       # the sqrt5 family
    lhs = (tp - tm) / 2
    rhs = ((1 + 5) - 6 * np.sqrt(5)) / 12                    # the A2 assembly (B587)
    assert abs(lhs - rhs) < 1e-9 and abs(lhs - (-1 / PHI)) < 1e-9


def test_legendre_oscillation_off_locus():
    # t_- = Legendre(kap'/5)-pattern off the 5-locus: +1 at 4,6; -1 at 7,8
    for kapp, expect in ((4, 1), (6, 1), (7, -1), (8, -1)):
        T, S, P = _a1_weil(kapp)
        M = _rho("RL", T, S)
        assert abs(np.trace(M @ P) - expect) < 1e-7
