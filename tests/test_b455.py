"""Locks for B455 — Ethogram E3: the engine structure + the homeostasis retirement."""
import os
import sys

import numpy as np

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B455_ethogram_e3_response")
sys.path.insert(0, HERE)


def test_sl2_triple_exact_and_S_conditioned():
    import integrate as I
    assert np.linalg.norm(I.adH @ I.adE - I.adE @ I.adH - 2 * I.adE) == 0.0
    assert np.linalg.norm(I.adE @ I.adF - I.adF @ I.adE - I.adH) == 0.0
    assert np.linalg.cond(I.S) < 1e6


def test_blockwise_engine_correct_low_m():
    """per-block expm reproduces tr Sym^{2m}(holonomy) — the engine is structurally sound."""
    from scipy.linalg import expm, logm
    import integrate as I
    import snappy
    M = snappy.ManifoldHP('4_1')
    G = M.fundamental_group()
    A = G.SL2C('a')
    a = np.array([[complex(float(A[i, j].real()), float(A[i, j].imag()))
                   for j in range(2)] for i in range(2)])
    xi = logm(a)
    adxi = xi[0, 1] * I.adE + xi[0, 0] * I.adH + xi[1, 0] * I.adF
    adxi_b = I.Sinv @ adxi @ I.S
    j = 0
    for m in I.EXPONENTS:
        d = 2 * m + 1
        if m <= 8:
            t1 = np.trace(expm(adxi_b[j:j + d, j:j + d]))
            t2 = np.trace(I.sym_power(a, 2 * m))
            assert abs(t1 - t2) < 1e-5 * max(1, abs(t2)), m
        j += d


def test_homeostasis_retired_kappa_conserved_exactly():
    from fractions import Fraction as F

    def T1(v):
        x, y, z = v
        return (z, x, x * z - y)

    def kappa(v):
        x, y, z = v
        return x * x + y * y + z * z - x * y * z - 2

    v = (F(31, 10), F(3), F(3))          # perturbed off kappa=-2
    k0 = kappa(v)
    assert k0 != -2
    for _ in range(12):
        v = T1(v)
        assert kappa(v) == k0             # exactly conserved: no return, ever
