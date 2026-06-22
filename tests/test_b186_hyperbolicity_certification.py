"""B186 -- off-axis hyperbolicity certification (V180). Fast locks.

The escape rate gamma of the Fricke trace map's trapping region is a hyperbolicity signature (exponential
escape <=> hyperbolic repeller): it is >0 on the DG-proven kappa>2 case AND off-axis kappa<2, but ~0 on the
kappa=2 band -- validated on ground truth, fixing B165's escape-contaminated ratio. Box-counting dimension is
a 2nd, independent Cantor diagnostic (off-axis < band). Full version in trace_map_hyperbolicity.py.
"""
import numpy as np
np.seterr(over="ignore", invalid="ignore")


def _T(p):
    x, y, z = p; return np.array([2*x*y - z, x, y])


def _survival(lmb, Egrid, Kmax=26, R=20.0):
    P = np.array([[(E - lmb)/2, E/2, 1.0] for E in Egrid], dtype=complex)
    alive = np.ones(len(P), bool); f = []
    for _ in range(Kmax):
        nrm = np.linalg.norm(P, axis=1); alive &= np.isfinite(nrm) & (nrm < R)
        f.append(alive.mean()); P[~alive] = 0.0; P = np.array([_T(p) for p in P])
    return np.array(f)


def _escape_rate(f):
    K = np.arange(len(f)); m = (f > 1e-3) & (f < 0.5)
    if m.sum() < 3: return 0.0
    return float(-np.polyfit(K[m], np.log(f[m]), 1)[0])


def _word(n, m=1):
    sub = "a"*m + "b"; s = {-1: "b", 0: "a"}
    for k in range(1, n+1): s[k] = "".join(sub if c == "a" else "a" for c in s[k-1])
    return s[n]


def _spectrum(word, lmb):
    L = len(word); V = np.array([lmb if c == "a" else 0.0 for c in word], dtype=complex)
    H = np.zeros((L, L), dtype=complex); np.fill_diagonal(H, V); i = np.arange(L-1)
    H[i, i+1] = 1; H[i+1, i] = 1; H[0, L-1] = 1; H[L-1, 0] = 1
    return np.linalg.eigvals(H)


def _box_dim(ev, scales=2.0**np.arange(-2, -8, -1)):
    P = np.c_[ev.real, ev.imag]; rng = np.ptp(P, axis=0); rng[rng == 0] = 1
    P = (P - P.min(0))/rng
    Ns = [len({(int(a//s), int(b//s)) for a, b in P}) for s in scales]
    return float(np.polyfit(np.log(1/scales), np.log(np.array(Ns, float)), 1)[0])


def test_escape_rate_separates_hyperbolic_from_band():
    reg = np.linspace(-4, 4, 240) + 0j
    cstrip = np.array([r + 1j*im for r in np.linspace(-4, 4, 50) for im in np.linspace(-3, 3, 9)])
    g_gt = _escape_rate(_survival(3.0, reg))      # DG-proven hyperbolic
    g_band = _escape_rate(_survival(0.0, reg))    # band
    g_off = _escape_rate(_survival(2.0j, cstrip)) # off-axis kappa=-2
    assert g_gt > 0.2          # ground truth: exponential escape
    assert g_band < 0.05       # band: no escape
    assert g_off > 0.1         # off-axis: same horseshoe signature


def test_box_dim_off_axis_below_band():
    for m, depth in [(1, 12), (2, 6)]:
        d_band = _box_dim(_spectrum(_word(depth, m), 0.0))
        d_off = _box_dim(_spectrum(_word(depth, m), 2.0j))
        assert d_off < 1.0
        assert d_off < d_band - 0.04
