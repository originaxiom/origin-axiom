"""B180 -- the two-faces dictionary (V174). Fast locks.

The hinge: kappa = tr[A,B] is conserved by the Dehn-twist trace maps (so it is the SAME number on the
character-variety boundary and the spectral trace-map side); and its value sets the spectral type
(coupling 0 / periodic -> full band, no gaps; coupling > 0 / kappa>2 -> Cantor, gaps). The fence (two
distinct interaction operations) lives in two_faces.py.
"""
import sympy as sp
import numpy as np
from scipy.linalg import eigvalsh_tridiagonal


def test_dehn_twists_conserve_kappa():
    x, y, z = sp.symbols('x y z')
    kappa = x**2 + y**2 + z**2 - x*y*z - 2
    Ta = {x: x, y: z, z: x*z - y}
    Tb = {x: z, y: y, z: y*z - x}
    assert sp.simplify(kappa.subs(Ta, simultaneous=True) - kappa) == 0
    assert sp.simplify(kappa.subs(Tb, simultaneous=True) - kappa) == 0


def test_kappa_sets_spectral_type():
    phi = (1 + 5**0.5) / 2; alpha = 1 / phi; N = 4000

    def n_gaps(lam, th=0.137, thresh=0.05):
        n = np.arange(1, N + 1)
        V = lam * (((n * alpha + th) % 1.0) >= 1.0 - alpha).astype(float)
        e = np.sort(eigvalsh_tridiagonal(V, np.ones(N - 1)))
        return int((np.diff(e) > thresh).sum())

    assert n_gaps(0.0) == 0        # periodic value -> full band (no gaps)
    assert n_gaps(1.5) >= 5        # kappa > 2 -> Cantor (gaps)
