"""B162 -- the kappa-sweep: kappa=2 is the unique cancellation<->non-cancellation wall (V156).

Fast locks: the kappa=2 full-band vs kappa>2 fracture (small chain), and the kappa=-2
parabolic-cusp endpoint (symbolic). The heavy 987-dim complex-spectrum sweep + V1-V4
self-validation live in frontier/B162_kappa_sweep/kappa_sweep.py.
"""
import numpy as np
import sympy as sp


def _band_measure(word, lm, NE=60000):
    Es = np.linspace(-(2+lm)-.05, (2+lm)+.05, NE)
    a = np.ones(NE); b = np.zeros(NE); c = np.zeros(NE); d = np.ones(NE)
    with np.errstate(over='ignore', invalid='ignore'):
        for ch in word:
            V = lm*(1.0 if ch == 'a' else 0.0)
            na = (Es-V)*a - c; nb = (Es-V)*b - d; a, b, c, d = na, nb, a.copy(), b.copy()
        return float(np.mean(np.abs(a+d) <= 2.0)*(Es[-1]-Es[0]))


def _word(n):
    w = {1: "a", 2: "ab"}
    for j in range(3, n+1): w[j] = w[j-1] + w[j-2]
    return w[n]


def test_kappa2_full_band_is_the_wall():
    W = _word(11)
    assert abs(_band_measure(W, 0.0) - 4.0) < 0.05    # kappa=2: full band (the unique positive-measure fiber)
    assert _band_measure(W, 1.0) < 3.5                  # kappa>2: fractured (Cantor, zero-measure)


def test_kappa_minus_two_parabolic_cusp():
    E, lam = sp.symbols('E lambda'); I2 = sp.eye(2)
    A = sp.Matrix([[E-lam, -1], [1, 0]]); B = sp.Matrix([[E, -1], [1, 0]])
    assert sp.simplify(2 + (2*sp.I)**2 - (-2)) == 0          # kappa=2+lambda^2=-2 <=> lambda=2i
    C = sp.simplify((A*B*A.inv()*B.inv()).subs(lam, 2*sp.I).subs(E, sp.Rational(1, 2)))
    assert sp.simplify(sp.trace(C) + 2) == 0                  # trace -2
    assert sp.simplify((C + I2)**2) == sp.zeros(2)            # single Jordan block => parabolic
    assert sp.simplify(C - (-I2)) != sp.zeros(2)             # not central -I (genuine cusp)


def test_chiral_symmetry_small_chain():
    # open-BC chiral symmetry E <-> -conj(E) on a small non-Hermitian Fibonacci chain
    word = _word(9); L = len(word); mu = 2.0
    V = np.array([1j*mu if ch == "a" else 0.0 for ch in word], dtype=complex)
    H = np.diag(V).astype(complex)
    i = np.arange(L-1); H[i, i+1] = 1.0; H[i+1, i] = 1.0
    ev = np.linalg.eigvals(H)
    assert np.max(np.abs(np.sort_complex(ev) - np.sort_complex(-np.conj(ev)))) < 1e-7
