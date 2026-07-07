"""Locks for B446 (Thermodynamic Campaign D1) — the fixed-cofactor tower moment law.

Fast levels only (N <= 405); the full battery incl. N=1215/2003/3645 is pipeline.py.
"""
import os
import sys

import numpy as np

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B446_thermo_d1_tower_moments")
sys.path.insert(0, HERE)
import pipeline as P  # noqa: E402


def _basis(A, N, n=4, tw=1):
    U = _u_tw(A % N, N, tw)
    H, _ = P.hecke_units(A, N, n)
    HQ = [_u_tw(M, N, tw) for M in H]
    V, resid, mult = P.joint_eigenbasis([U] + HQ + [P.parity(N).astype(complex)], N)
    assert resid < 1e-8
    return V, mult


def _u_tw(B, N, tw=1):
    a, b, d = int(B[0, 0]), int(B[0, 1]), int(B[1, 1])
    ib2 = pow((2 * b) % N, -1, N)
    j = np.arange(N).reshape(-1, 1)
    k = np.arange(N).reshape(1, -1)
    return np.exp(2j * np.pi * ((tw * ib2 * (a * k * k - 2 * j * k + d * j * j)) % N) / N) / np.sqrt(N)


def _xv(V, N, u=1):
    fd = np.cos(2 * np.pi * u * np.arange(N) / N)
    return np.einsum('jn,j,jn->n', V.conj(), fd, V).real


def test_kr_prime_gate_small():
    # prime N=241: KR arithmetically-enhanced constant ~1 (not the RMT 1/2), kurtosis ~2
    r, _ = P.run_level(P.A_GOLD, 241)
    assert abs(r['NVar'] - 1.0) < 0.02
    assert abs(r['kurtosis'] - 2.0) < 0.12
    assert r['unitarity_err'] < 1e-12 and r['commutator_err'] < 1e-12


def test_five_factor_exact_golden():
    # the golden 5-factor multiset is EXACTLY {+-1/2, 0, 0, 0} for every unit u
    vals, resid, _ = P.five_factor_exact()
    assert resid < 1e-10
    for u, d in vals.items():
        X = np.sort(np.round(d['X'], 9))
        assert list(X) == [-0.5, 0.0, 0.0, 0.0, 0.5]
        assert abs(d['S5'] - 0.5) < 1e-9
        assert abs(d['K5'] - 2.5) < 1e-9


def test_tower_variance_law_golden():
    # N*Var = S5*C3 = 3/8 exactly along the tower (lock at 15, 45, 135)
    for N in (15, 45, 135):
        r, _ = P.run_level(P.A_GOLD, N)
        assert abs(r['NVar'] - 0.375) < 1e-6, (N, r['NVar'])


def test_pure3_constant():
    r, _ = P.run_level(P.A_GOLD, 243)
    assert abs(r['NVar'] - 0.75) < 1e-6


def test_silver_control_product_law():
    # silver: same law FORM, own constant 5/8 (5 inert in Q(sqrt2) -> generic 5-multiset)
    r, _ = P.run_level(P.A_SILV, 45)
    assert abs(r['NVar'] - 0.625) < 1e-6
    r2, _ = P.run_level(P.A_SILV, 243)
    assert abs(r2['NVar'] - 0.75) < 1e-6      # C3 shared with golden


def test_twisted_factor_multiset_and_kurtosis_at_135():
    # the exact lemma: X_135 = {Y5_i * Y27_j} with CHARACTER-TWISTED factor bases,
    # and kurt(135) = K5 * K27(psi) to 6 digits
    N1, N2 = 5, 27
    u1, u2 = pow(N2, -1, N1), pow(N1, -1, N2)
    V5, _ = _basis(P.A_GOLD, 5, 3, tw=u1)
    Y5 = _xv(V5, 5, u1)
    V27, _ = _basis(P.A_GOLD, 27, 3, tw=u2)
    Y27 = _xv(V27, 27, u2)
    V135, _ = _basis(P.A_GOLD, 135, 4, tw=1)
    X135 = _xv(V135, 135, 1)
    prod = np.sort(np.outer(Y5, Y27).flatten())
    assert np.allclose(prod, np.sort(X135), atol=1e-9)
    k_pred = (np.mean(Y5**4) / np.mean(Y5**2)**2) * (np.mean(Y27**4) / np.mean(Y27**2)**2)
    k_meas = np.mean(X135**4) / np.mean(X135**2)**2
    assert abs(k_pred - k_meas) < 1e-6
    assert abs(k_meas - 4.904533) < 1e-4       # the drifting non-KR value


def test_sff_pisano_launder():
    # untwisted SFF full revival at t = ord(A mod N) = pi(N)/2 (the P59 law); twisted kills it
    r, _ = P.run_level(P.A_GOLD, 45, want_sff=True)
    assert r['ord_A_mod_N'] == 60
    i = r['sff_t'].index(60)
    assert abs(r['sff_untwisted'][i] - 45.0) < 1e-6      # full revival = N
    assert r['sff_twisted'][i] < 0.1                     # parity annihilates it (|tr P|^2/N)
