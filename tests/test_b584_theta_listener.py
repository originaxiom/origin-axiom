"""B584 — Round 3 of the chord program: THE LISTENER (locks).

The theta-odd listener on the golden stage SU(3)_2:
  * the operational identity tr_odd rho = (Z - Z_C)/2 (Z_C = tr(C rho));
  * BLIND result: tr_even = 0 and tr_odd = -1/phi — the ENTIRE banked golden
    value Z = -1/phi (B238) is theta-odd; the odd block is the order-10 golden
    rotation with eigenvalues e^(+-3 pi i/5), trace 2cos(3pi/5) = -1/phi;
  * the even block is the silent order-20 clock (eigenvalues cancel in pairs);
  * bare knots are deaf sources: J_3(4_1) = J_3bar(4_1) (dual color = same
    invariant), so bare knot states have zero theta-odd component.

See frontier/B584_theta_listener/FINDINGS.md.
"""
import cmath
import importlib.util
import os

import numpy as np
import pytest

_ROOT = os.path.join(os.path.dirname(__file__), "..")


def _load(rel, name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(_ROOT, rel))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


b238 = _load(os.path.join("frontier", "B238_su32_levelrank", "su32_wrt.py"), "b238m")
b245 = _load(os.path.join("frontier", "B245_higher_color_levelrank",
                          "higher_color_levelrank.py"), "b245m")

PHI = (1 + 5 ** 0.5) / 2


@pytest.fixture(scope="module")
def stage():
    w, S, T, c = b238.su3_data(2)
    n = len(w)
    C = np.zeros((n, n))
    for i, wt in enumerate(w):
        C[w.index((wt[1], wt[0])), i] = 1.0
    Si, Ti = np.linalg.inv(S), np.linalg.inv(T)
    M = T @ (Si @ Ti @ S)
    return w, S, T, C, M


def test_charge_conjugation_gates(stage):
    w, S, T, C, M = stage
    n = len(w)
    assert np.allclose(C @ C, np.eye(n))
    assert np.allclose(C @ S, S @ C, atol=1e-10)
    assert np.allclose(C @ T, T @ C, atol=1e-10)
    # B238's normalization carries a global sign: the permutation pattern is C
    assert np.allclose(np.abs(S @ S), C, atol=1e-9)


def test_operational_identity_and_blind_result(stage):
    w, S, T, C, M = stage
    n = len(w)
    Z = np.trace(M)
    ZC = np.trace(C @ M)
    tr_odd = np.trace(M @ (np.eye(n) - C) / 2)
    tr_even = np.trace(M @ (np.eye(n) + C) / 2)
    assert abs(Z - (-1 / PHI)) < 1e-9                       # banked B238 gate
    assert abs(tr_odd - (Z - ZC) / 2) < 1e-12               # the identity
    assert abs(tr_even) < 1e-10                             # BLIND: even silent
    assert abs(tr_odd - (-1 / PHI)) < 1e-9                  # BLIND: all of Z is odd
    assert abs(ZC - (1 / PHI)) < 1e-9                       # mirror-twisted = +1/phi


def test_odd_block_order10_golden_rotation(stage):
    w, S, T, C, M = stage
    n = len(w)
    pairs = [(i, w.index((wt[1], wt[0]))) for i, wt in enumerate(w)
             if (wt[1], wt[0]) > wt]
    assert len(pairs) == 2
    odd = np.zeros((n, 2))
    for j, (i, ib) in enumerate(pairs):
        odd[i, j], odd[ib, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)
    B = odd.T @ M @ odd
    ev = sorted(np.linalg.eigvals(B), key=lambda e: e.imag)
    for e, sgn in zip(ev, (-1, 1)):
        assert abs(e - cmath.exp(sgn * 3j * np.pi / 5)) < 1e-9
    assert abs(np.trace(B) - 2 * np.cos(3 * np.pi / 5)) < 1e-9
    P = np.eye(2, dtype=complex)
    orders = []
    for k in range(1, 21):
        P = P @ B
        if np.allclose(P, np.eye(2), atol=1e-9):
            orders.append(k)
    assert orders and orders[0] == 10


def test_even_block_silent_order20(stage):
    w, S, T, C, M = stage
    n = len(w)
    pairs = [(i, w.index((wt[1], wt[0]))) for i, wt in enumerate(w)
             if (wt[1], wt[0]) > wt]
    fixed = [i for i, wt in enumerate(w) if wt == (wt[1], wt[0])]
    even = np.zeros((n, 4))
    for j, (i, ib) in enumerate(pairs):
        even[i, j], even[ib, j] = 1 / np.sqrt(2), 1 / np.sqrt(2)
    for j, i in enumerate(fixed):
        even[i, 2 + j] = 1.0
    B = even.T @ M @ even
    assert abs(np.trace(B)) < 1e-10
    args = sorted(round(cmath.phase(e) / np.pi, 6) for e in np.linalg.eigvals(B))
    assert args == [-0.9, -0.1, 0.1, 0.9]                    # 20th roots, cancelling


def test_bare_knots_are_deaf_sources():
    for t in (0.29, 0.73, 1.31):
        q = cmath.exp(1j * t)
        assert abs(b245.H_sym(1, q ** 3, q) - b245.H_antisym(2, q ** 3, q)) < 1e-9
