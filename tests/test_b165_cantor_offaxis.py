"""B165 -- toward the off-axis (kappa<2) Cantor theorem (V162, P2a). Fast locks.

D0 [exact]: the trace map conserves I. D1 [num, small]: the MST max-gap separates the kappa=-2
Cantor spectrum (persistent gap) from the kappa=2 band (gap -> small), on a small golden chain.
The seed-robust extension + the conditional reduction live in cantor_offaxis.py / FINDINGS.
"""
import numpy as np
import sympy as sp


def test_trace_map_conserves_invariant():
    x, y, z = sp.symbols('x y z')
    T = (2*x*y - z, x, y)
    I = lambda a, b, c: a**2 + b**2 + c**2 - 2*a*b*c - 1
    assert sp.expand(I(*T) - I(x, y, z)) == 0


def _word(n):                       # golden Fibonacci word
    w = {1: "a", 2: "ab"}
    for j in range(3, n+1): w[j] = w[j-1] + w[j-2]
    return w[n]


def _eig(word, lam):
    L = len(word); V = np.array([lam if c == "a" else 0.0 for c in word], dtype=complex)
    H = np.diag(V).astype(complex)
    i = np.arange(L-1); H[i, i+1] = 1.0; H[i+1, i] = 1.0
    H[0, L-1] = 1.0; H[L-1, 0] = 1.0
    return np.linalg.eigvals(H)


def _max_gap_over_diam(ev):
    P = np.c_[ev.real, ev.imag]; n = len(P)
    intree = np.zeros(n, bool); mind = np.full(n, np.inf); mind[0] = 0.0; edges = np.empty(n)
    for t in range(n):
        u = int(np.argmin(np.where(intree, np.inf, mind))); edges[t] = mind[u]; intree[u] = True
        d = np.sqrt(((P - P[u])**2).sum(1)); upd = (~intree) & (d < mind); mind[upd] = d[upd]
    diam = np.hypot(ev.real.max()-ev.real.min(), ev.imag.max()-ev.imag.min())
    return float(edges[1:].max())/float(diam)


def test_kappa_minus2_cantor_vs_band_small():
    w = _word(13)                                       # F=377, fast
    gap_cantor = _max_gap_over_diam(_eig(w, 2.0j))      # kappa=-2 (non-Hermitian)
    gap_band = _max_gap_over_diam(_eig(w, 0.0+0j))      # kappa=2 (band)
    assert gap_cantor > 0.08                            # persistent gap (Cantor-like)
    assert gap_cantor > 5 * gap_band                    # dwarfs the band control (-> 0)
