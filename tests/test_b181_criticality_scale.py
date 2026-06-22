"""B181 -- the criticality scale-door (V175). Fast locks (shorter transfer products).

The decisive contrast: the Aubry-Andre (smooth cosine) operator HAS a metal-insulator transition
(Lyapunov 0 -> ln(lam/2) across lam=2), while the metallic Fibonacci/Sturmian operator is PERMANENTLY
CRITICAL (Lyapunov ~ 0 on the spectrum at all coupling) -- so criticality is the metallic object's
scale-freeness, not a scale source. Full averaged version in criticality_scale.py.
"""
import numpy as np
from scipy.linalg import eigvalsh_tridiagonal

phi = (1 + 5**0.5) / 2
alpha = 1 / phi


def _sturm(N, lam, th):
    n = np.arange(1, N + 1); return lam * (((n * alpha + th) % 1.0) >= 1.0 - alpha).astype(float)


def _cos(N, lam, th):
    n = np.arange(1, N + 1); return lam * np.cos(2 * np.pi * (alpha * n + th))


def _in_spectrum(Vfun, lam, th, Ns=1200, k=6):
    V = Vfun(Ns, lam, th); e = np.sort(eigvalsh_tridiagonal(V, np.ones(Ns - 1)))
    return e[np.linspace(int(Ns * 0.3), int(Ns * 0.7), k).astype(int)]


def _lyap(Vfun, lam, th, E, Nl=12000):
    V = Vfun(Nl, lam, th); v = np.array([1.0, 0.0]); s = 0.0
    for n in range(Nl):
        v = np.array([(E - V[n]) * v[0] - v[1], v[0]]); nr = np.linalg.norm(v); s += np.log(nr); v /= nr
    return s / Nl


def _avg(Vfun, lam, th=0.137):
    return float(np.mean([_lyap(Vfun, lam, th, E) for E in _in_spectrum(Vfun, lam, th)]))


def test_aubry_andre_has_transition():
    assert _avg(_cos, 1.0) < 0.06              # extended below lam=2
    assert abs(_avg(_cos, 3.0) - np.log(1.5)) < 0.08   # localized above: gamma = ln(lam/2)


def test_metallic_is_permanently_critical():
    gF3 = _avg(_sturm, 3.0)
    assert _avg(_sturm, 1.0) < 0.06            # critical at weak coupling
    assert gF3 < 0.12                          # STILL critical at strong coupling (no transition)
    assert gF3 < 0.3 * np.log(1.5)             # << the AA localized value -> does not localize
