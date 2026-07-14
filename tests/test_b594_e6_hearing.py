"""B594 — the E6_2 hearing law (locks). See frontier/B594_e6_hearing/FINDINGS.md."""
import cmath
import importlib.util
import math
import os

import numpy as np
import pytest

_spec = importlib.util.spec_from_file_location(
    "c3mod3", os.path.join(os.path.dirname(__file__), "..",
                           "frontier", "B570_allowed_plays", "c3_e6_level2_monodromy.py"))
c3 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(c3)


@pytest.fixture(scope="module")
def stage():
    W, eps_signs = c3.weyl_group()
    rho_w = c3.root_coords([1] * 6)
    shifted = [c3.root_coords(p) + rho_w for p in c3.PRIM]
    S = np.zeros((9, 9), dtype=complex)
    Wl = np.einsum('wij,lj->wli', W.astype(float), np.array(shifted))
    for a in range(9):
        for b in range(a, 9):
            ips = Wl[:, a, :] @ (c3.C @ shifted[b])
            S[a, b] = S[b, a] = np.sum(eps_signs * np.exp(-2j * np.pi * ips / c3.KH))
    S /= np.sqrt((S @ S.conj().T)[0, 0].real)
    if S[0, 0].real < 0:
        S = -S
    ipf = lambda x, y: float(x @ (c3.C @ y))
    hs = [ipf(c3.root_coords(p), c3.root_coords(p) + 2 * rho_w) / (2 * c3.KH)
          for p in c3.PRIM]
    T = np.diag([np.exp(2j * np.pi * (h - (2 * 78 / c3.KH) / 24)) for h in hs])
    rho = T @ T @ S @ T
    Cm = (S @ S).real
    conj_idx = [c3.PRIM.index(c3.theta(p)) for p in c3.PRIM]
    U = np.zeros((9, 3))
    for j, (a, b) in enumerate([(1, 2), (3, 4), (7, 8)]):
        U[a, j], U[b, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)
    return rho, Cm, conj_idx, U


def test_law_state_independent(stage):
    rho, Cm, conj_idx, U = stage
    rng = np.random.default_rng(7)
    for Wm in (Cm @ rho, rho, Cm):
        z = rng.normal(size=9) + 1j * rng.normal(size=9)
        psi = np.array([(z[i] + z[conj_idx[i]]) / 2 for i in range(9)])
        A0 = sum(np.conj(psi[conj_idx[i]]) * (Wm @ psi)[i] for i in range(9))
        for j in range(3):
            u = U[:, j].astype(complex)
            quad = np.conj(u) @ Wm @ u
            for e in (0.07, 0.31):
                pe = psi + e * u
                Ae = sum(np.conj(pe[conj_idx[i]]) * (Wm @ pe)[i] for i in range(9))
                assert abs(Ae - (A0 - e * e * quad)) < 1e-10


def test_coefficients_are_banked_amplitudes(stage):
    rho, Cm, conj_idx, U = stage
    banked = [(1, 3), (3, -2), (2, -1)]
    Wt = Cm @ rho
    for j, (jp, k) in enumerate(banked):
        u = U[:, j].astype(complex)
        coeff = np.conj(u) @ Wt @ u
        p = (2 / math.sqrt(7)) * math.sin(2 * math.pi * jp / 7) \
            * cmath.exp(2j * math.pi * k / 14)
        assert abs(coeff + p) < 1e-7
        assert abs(coeff.imag) > 1e-3


def test_trace_and_order(stage):
    rho, Cm, conj_idx, U = stage
    B = U.T @ (Cm @ rho) @ U
    assert abs(np.trace(B) + 1) < 1e-8
    P4 = np.linalg.matrix_power(U.T @ rho @ U, 4)
    assert np.allclose(P4, np.eye(3), atol=1e-7)
