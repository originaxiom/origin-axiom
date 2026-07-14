"""B595 — the dictionary bridge (locks). See frontier/B595_dictionary/FINDINGS.md."""
import importlib.util
import math
import os

import numpy as np

_ROOT = os.path.join(os.path.dirname(__file__), "..")
_spec = importlib.util.spec_from_file_location(
    "b238m7", os.path.join(_ROOT, "frontier", "B238_su32_levelrank", "su32_wrt.py"))
b238 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b238)

PHI = (1 + 5 ** 0.5) / 2


def _odd_block(k):
    w, S, T, c = b238.su3_data(k)
    n = len(w)
    Si, Ti = np.linalg.inv(S), np.linalg.inv(T)
    M = T @ (Si @ Ti @ S)
    prs = [(i, w.index((wt[1], wt[0]))) for i, wt in enumerate(w)
           if (wt[1], wt[0]) > wt]
    odd = np.zeros((n, len(prs)))
    for j, (a, b) in enumerate(prs):
        odd[a, j], odd[b, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)
    return odd.T @ M @ odd


def test_spectral_bridge_phi_squared():
    B = _odd_block(2)
    assert abs(np.linalg.det(np.eye(2) - B) - PHI ** 2) < 1e-9   # = lambda(A1)


def test_golden_powers_on_5divides():
    assert abs(np.linalg.det(np.eye(16) - _odd_block(7)) - PHI ** 4) < 1e-7
    assert abs(np.linalg.det(np.eye(42) - _odd_block(12)) - PHI ** 4) < 1e-6


def test_dimension_constraint():
    # SU(2)_k: no odd space; SU(3)_2: dim 2 = the dial; E6_2: dim 3 != 2
    assert _odd_block(2).shape == (2, 2)


def test_e6_fixed_ear_achiral():
    spec = importlib.util.spec_from_file_location(
        "c3mod4", os.path.join(_ROOT, "frontier", "B570_allowed_plays",
                               "c3_e6_level2_monodromy.py"))
    c3 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(c3)
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
    T6 = np.diag([np.exp(2j * np.pi * (h - (2 * 78 / c3.KH) / 24)) for h in hs])
    rho6 = T6 @ T6 @ S @ T6
    C6m = (S @ S).real
    U6 = np.zeros((9, 3))
    for j, (a, b) in enumerate([(1, 2), (3, 4), (7, 8)]):
        U6[a, j], U6[b, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)
    B6 = U6.T @ rho6 @ U6
    assert abs(np.linalg.det(np.eye(3) - B6)) < 1e-10        # fixed direction exists
    ev, evec = np.linalg.eig(B6)
    u = evec[:, int(np.argmin(np.abs(ev - 1)))]
    u = u / np.linalg.norm(u)
    v = U6 @ u
    coeff = np.conj(v) @ (C6m @ rho6) @ v
    assert abs(coeff + 1) < 1e-9                              # exactly -1: achiral
