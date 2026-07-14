"""B586 — the Round-3 handoff processed (locks).

E6 level 2: the entire amplitude is theta-odd (Z = +1, Z_C = -1, tr_even = 0,
tr_odd = +1) — the B584 pattern holds on the E6 stage too; the three per-pair
chirality amplitudes are fixed complex numbers summing to 1 (C3's trace); the
blind -1/phi check is empty (the golden voice is stage arithmetic, not
object-universal); S^2 = +C on E6_2 (vs -C in B238's SU(3)_2 normalization) and
the lift identity holds with the matching sign.

See frontier/B586_round3_handoff/FINDINGS.md.
"""
import importlib.util
import os

import numpy as np
import pytest

_spec = importlib.util.spec_from_file_location(
    "c3mod2", os.path.join(os.path.dirname(__file__), "..",
                           "frontier", "B570_allowed_plays", "c3_e6_level2_monodromy.py"))
c3 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(c3)

PHI = (1 + 5 ** 0.5) / 2

PAIR_AMPS = {                       # the banked blind numbers (pair basis diagonals)
    "27": 0.13151189 + 0.57619122j,
    "351p": 0.20449548 - 0.25642922j,
    "351": 0.66399264 - 0.31976200j,
}


@pytest.fixture(scope="module")
def stage():
    W, eps = c3.weyl_group()
    assert len(W) == 51840
    rho_w = c3.root_coords([1] * 6)
    shifted = [c3.root_coords(p) + rho_w for p in c3.PRIM]
    S = np.zeros((9, 9), dtype=complex)
    Wl = np.einsum('wij,lj->wli', W.astype(float), np.array(shifted))
    for a in range(9):
        for b in range(a, 9):
            ips = Wl[:, a, :] @ (c3.C @ shifted[b])
            S[a, b] = S[b, a] = np.sum(eps * np.exp(-2j * np.pi * ips / c3.KH))
    S /= np.sqrt((S @ S.conj().T)[0, 0].real)
    if S[0, 0].real < 0:
        S = -S
    ip = lambda x, y: float(x @ (c3.C @ y))
    cc = 2 * 78 / c3.KH
    hs = [ip(c3.root_coords(p), c3.root_coords(p) + 2 * rho_w) / (2 * c3.KH)
          for p in c3.PRIM]
    T = np.diag([np.exp(2j * np.pi * (h - cc / 24)) for h in hs])
    rho = T @ T @ S @ T
    Cmat = (S @ S).real
    return S, T, rho, Cmat


def test_sign_convention_s2_plus_c(stage):
    S, T, rho, Cmat = stage
    expect = np.zeros((9, 9))
    for i, p in enumerate(c3.PRIM):
        expect[c3.PRIM.index(c3.theta(p)), i] = 1
    assert np.allclose(S @ S, expect, atol=1e-9)          # +C, unlike B238's -C
    assert np.allclose(Cmat @ rho, rho @ Cmat, atol=1e-9)


def test_e6_hears_everything(stage):
    S, T, rho, Cmat = stage
    Z = np.trace(rho)
    ZC = np.trace(Cmat @ rho)
    tr_odd = np.trace(rho @ (np.eye(9) - Cmat) / 2)
    assert abs(Z - 1) < 1e-8
    assert abs(ZC + 1) < 1e-8
    assert abs(tr_odd - 1) < 1e-8                          # ALL of Z is theta-odd
    assert abs((Z - tr_odd)) < 1e-8                        # tr_even = 0 exactly
    assert abs(tr_odd - (Z - ZC) / 2) < 1e-10              # the B584 identity
    assert abs(ZC - np.trace(S @ S @ rho)) < 1e-9          # lift identity, + sign


def test_per_pair_amplitudes_and_no_golden(stage):
    S, T, rho, Cmat = stage
    pairs = [(1, 2, "27"), (3, 4, "351p"), (7, 8, "351")]
    odd = np.zeros((9, 3))
    for j, (a, b, _) in enumerate(pairs):
        odd[a, j], odd[b, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)
    B = odd.T @ rho @ odd
    for j, (a, b, nm) in enumerate(pairs):
        assert abs(B[j, j] - PAIR_AMPS[nm]) < 1e-7
    assert abs(np.trace(B) - 1) < 1e-8                     # C3 gate
    assert np.linalg.norm(np.linalg.matrix_power(B, 4) - np.eye(3)) < 1e-7
    # the blind -1/phi check is EMPTY: no amplitude, trace, or ratio is golden
    vals = [B[j, j] for j in range(3)]
    assert all(abs(abs(v) - 1 / PHI) > 1e-4 for v in vals)
    for i in range(3):
        for j in range(3):
            if i != j:
                r = abs(B[i, i] / B[j, j])
                assert abs(r - 1 / PHI) > 1e-4 and abs(r - PHI) > 1e-4
