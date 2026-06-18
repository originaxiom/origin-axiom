"""B163 -- the kappa-sweep resolved (V157). Fast locks on small chains.

(3a) the largest-gap diagnostic separates band (gap->0) from Cantor (gap->const): the band
control (lambda=0) gap shrinks with size and is tiny, while the kappa=-2 (lambda=2i) gap is
large and persistent (Cantor-like). (3b) coarse smoothness through kappa=-2. The full
F=1597 sweep + null-test live in frontier/B163_kappa_sweep_resolved/kappa_resolved.py.
"""
import numpy as np


def _word(n):
    w = {1: "a", 2: "ab"}
    for j in range(3, n+1): w[j] = w[j-1] + w[j-2]
    return w[n]


def _eig(word, lam):
    L = len(word); V = np.array([lam if c == "a" else 0.0 for c in word], dtype=complex)
    H = np.diag(V).astype(complex)
    i = np.arange(L-1); H[i, i+1] = 1.0; H[i+1, i] = 1.0
    return np.linalg.eigvals(H)


def _max_gap_over_diam(pts):
    P = np.c_[pts.real, pts.imag]; n = len(P)
    in_tree = np.zeros(n, bool); mind = np.full(n, np.inf); mind[0] = 0.0; edges = np.empty(n)
    for t in range(n):
        u = int(np.argmin(np.where(in_tree, np.inf, mind)))
        edges[t] = mind[u]; in_tree[u] = True
        d = np.sqrt(((P - P[u])**2).sum(1)); upd = (~in_tree) & (d < mind); mind[upd] = d[upd]
    diam = np.hypot(pts.real.max()-pts.real.min(), pts.imag.max()-pts.imag.min())
    return float(edges[1:].max())/float(diam)


def test_3a_band_gap_shrinks_cantor_gap_persists():
    # band control lambda=0: gap/diam shrinks with size and is tiny (connected band)
    g_band_144 = _max_gap_over_diam(_eig(_word(11), 0.0+0j))
    g_band_377 = _max_gap_over_diam(_eig(_word(13), 0.0+0j))
    assert g_band_377 < g_band_144 and g_band_377 < 0.02
    # kappa=-2 (lambda=2i): gap large and persistent (Cantor-like) -- NOT shrinking to 0
    g_fig_144 = _max_gap_over_diam(_eig(_word(11), 2.0j))
    g_fig_377 = _max_gap_over_diam(_eig(_word(13), 2.0j))
    assert g_fig_377 > 0.1 and g_fig_377 > 0.5*g_fig_144
    # decisive separation: the kappa<2 gap dwarfs the band gap
    assert g_fig_377 > 10*g_band_377


def test_3b_smooth_through_kappa_minus_two():
    # max|Im E| is smooth (no kink) across kappa=-1.8,-2.0,-2.2 (coarse 2nd-difference)
    def mim(kap):
        mu = (2.0 - kap)**0.5
        return float(np.max(np.abs(_eig(_word(13), mu*1j).imag)))
    v = [mim(-1.8), mim(-2.0), mim(-2.2)]
    d2 = abs(v[0] - 2*v[1] + v[2])
    assert d2 < 0.05           # smooth through kappa=-2 (no spectral signature of the cusp-opening)
