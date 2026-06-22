"""B183 -- the open/driven collective arrow door (V177). Fast locks (small N).

The discriminating probe is Hatano-Nelson (imaginary gauge field g, PBC): the real spectrum becomes
complex (irreversible / non-unitary = an arrow) at g_c = min Lyapunov over the spectrum = inverse
localization length. The metallic object is PERMANENTLY CRITICAL (B181, min Lyap ~ 0) => g_c ~ 0:
thresholdless arrow (the INVERSION -- criticality = maximal fragility). A localized control (AA, V=8cos,
off-metallic) is protected up to the exact finite g_c = ln(4). The naive staggered-PT probe is a
chiral-symmetry artifact (g_c ~ 0 for any V != 0). Full version in open_collective.py.
"""
import numpy as np
from numpy.linalg import eigvals, eigvalsh

phi = (1 + 5**0.5) / 2
alpha = 1 / phi


def _V(model, N, seed=1):
    n = np.arange(1, N + 1)
    if model == "metallic":     return 1.0 * (((n * alpha) % 1.0) >= 1.0 - alpha).astype(float)
    if model == "AA_localized": return 8.0 * np.cos(2 * np.pi * alpha * n)
    if model == "periodic":     return np.zeros(N)
    raise ValueError(model)


def _hn_maximag(N, V, g):                       # Hatano-Nelson PBC
    H = np.diag(V).astype(complex); f, b = np.exp(g), np.exp(-g)
    i = np.arange(N - 1); H[i, i + 1] = f; H[i + 1, i] = b; H[N - 1, 0] = f; H[0, N - 1] = b
    return float(np.max(np.abs(eigvals(H).imag)))


def _gc(N, V, tol=1e-6, gmax=2.5, steps=16):
    if _hn_maximag(N, V, 1e-4) > tol: return 0.0
    if _hn_maximag(N, V, gmax) < tol: return float("inf")
    lo, hi = 0.0, gmax
    for _ in range(steps):
        mid = (lo + hi) / 2
        if _hn_maximag(N, V, mid) > tol: hi = mid
        else: lo = mid
    return hi


def _staggered_gc(N, V, tol=1e-6, gmax=1.0, steps=14):
    n = np.arange(N)
    def mi(g):
        H = np.diag(V + 1j * g * ((-1.0) ** n)).astype(complex)
        o = np.ones(N - 1); H += np.diag(o, 1) + np.diag(o, -1)
        return float(np.max(np.abs(eigvals(H).imag)))
    if mi(1e-4) > tol: return 0.0
    lo, hi = 0.0, gmax
    for _ in range(steps):
        mid = (lo + hi) / 2
        if mi(mid) > tol: hi = mid
        else: lo = mid
    return hi


def test_metallic_collective_is_thresholdless():
    # critical (B181) => g_c ~ 0: irreversible spectrum under the slightest open-system drive
    assert _gc(160, _V("metallic", 160)) < 0.05
    assert _gc(160, _V("periodic", 160)) < 0.05          # extended also thresholdless


def test_localized_control_is_protected_at_ln4():
    # off-metallic localized chain keeps a REAL spectrum up to the EXACT finite g_c = ln(4)
    gc = _gc(200, _V("AA_localized", 200))
    assert abs(gc - np.log(4.0)) < 0.18 * np.log(4.0)
    assert gc > 10 * max(_gc(160, _V("metallic", 160)), 1e-4)   # >> the metallic ~0


def test_staggered_pt_is_a_chiral_artifact():
    # the naive PT probe does NOT see localization: g_c ~ 0 for the metallic AND the (V!=0) localized chain
    assert _staggered_gc(160, _V("metallic", 160)) < 0.03
    assert _staggered_gc(160, _V("AA_localized", 160)) < 0.03
