"""B585 — the listener's law (locks).

N1: the C-twist = the other SL(2,Z) lift (tr(C rho W) = -tr rho(S^2 W); the
theta-odd channel = the lift-symmetrization). LAW-O: on SU(3)_k the figure-eight
chiral channel is the additive two-tone law tr_odd = [4|kap] - [5|kap]/phi,
including the kap=20 collision (= 1/phi^2). M1 refutation: silver RRLL fires at
kap=10 although 8 does not divide 10 — the field-containment mechanism is dead.

See frontier/B585_listener_law/FINDINGS.md.
"""
import importlib.util
import os

import numpy as np
import pytest

_ROOT = os.path.join(os.path.dirname(__file__), "..")
_spec = importlib.util.spec_from_file_location(
    "b238m2", os.path.join(_ROOT, "frontier", "B238_su32_levelrank", "su32_wrt.py"))
b238 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b238)

PHI = (1 + 5 ** 0.5) / 2


def _stage(k):
    w, S, T, c = b238.su3_data(k)
    n = len(w)
    C = np.zeros((n, n))
    for i, wt in enumerate(w):
        C[w.index((wt[1], wt[0])), i] = 1.0
    return w, S, T, C


def _rho(S, T, word):
    Si, Ti = np.linalg.inv(S), np.linalg.inv(T)
    R, L = T, Si @ Ti @ S
    M = np.eye(S.shape[0], dtype=complex)
    for ch in word:
        M = M @ (R if ch == 'R' else L)
    return M


def _tr_odd(k, word):
    w, S, T, C = _stage(k)
    M = _rho(S, T, word)
    return np.trace(M @ (np.eye(len(w)) - C) / 2)


def test_n1_naming_theorem_lift_identities():
    w, S, T, C = _stage(2)
    n = len(w)
    S2 = S @ S
    assert np.allclose(S2, -C, atol=1e-9)               # S^2 = -C on this stage
    for word in ("RL", "RRLL", "RRRLLL", "RRL"):
        M = _rho(S, T, word)
        Z, ZC, Zlift = np.trace(M), np.trace(C @ M), np.trace(S2 @ M)
        assert abs(ZC + Zlift) < 1e-9                   # C-twist = the -M lift
        assert abs(np.trace(M @ (np.eye(n) - C) / 2) - (Z + Zlift) / 2) < 1e-9
        assert abs(np.trace(M @ (np.eye(n) + C) / 2) - (Z - Zlift) / 2) < 1e-9


@pytest.mark.parametrize("k,expected", [
    (1, 1.0),                    # kap=4:  the unit 4-tone
    (2, -1 / PHI),               # kap=5:  the golden 5-tone alone (B584)
    (3, 0.0),                    # kap=6:  silent
    (7, -1 / PHI),               # kap=10: golden again
    (13, 1.0),                   # kap=16: 4-tone (held-out level)
])
def test_law_o_two_tones(k, expected):
    assert abs(_tr_odd(k, "RL") - expected) < 1e-7


def test_law_o_collision_kap20_additive():
    # first 4|kap AND 5|kap: the tones ADD: 1 - 1/phi = 1/phi^2
    assert abs(_tr_odd(17, "RL") - (1 - 1 / PHI)) < 1e-7
    assert abs((1 - 1 / PHI) - 1 / PHI ** 2) < 1e-12


def test_m1_field_containment_refuted():
    # silver RRLL (trace field Q(sqrt2), sqrt2 in Q(zeta_kap) iff 8|kap) fires
    # at kap=10 where 8 does NOT divide 10 -> the mechanism as stated is dead
    v = _tr_odd(7, "RRLL")
    assert abs(v - 1.0) < 1e-7
    # and bronze is SILENT at kap=10 despite firing at kap=5,15 (interference)
    assert abs(_tr_odd(7, "RRRLLL")) < 1e-7


def test_clock_orders_sample():
    # the clock table's anchor rows: kap=5 -> 10 (B584), kap=10 -> 60 (L77's 60)
    for k, expected in ((2, 10), (7, 60)):
        w, S, T, C = _stage(k)
        M = _rho(S, T, "RL")
        n = len(w)
        pairs = [(i, w.index((wt[1], wt[0]))) for i, wt in enumerate(w)
                 if (wt[1], wt[0]) > wt]
        odd = np.zeros((n, len(pairs)))
        for j, (i, ib) in enumerate(pairs):
            odd[i, j], odd[ib, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)
        B = odd.T @ M @ odd
        P = np.eye(len(pairs), dtype=complex)
        order = None
        for m in range(1, 121):
            P = P @ B
            if np.allclose(P, np.eye(len(pairs)), atol=1e-8):
                order = m
                break
        assert order == expected
