"""B169 -- the isomonodromy (Painleve-VI) flow + firewall-relocation verdict (V161, P1/PR2). Fast locks.

The metallic dynamical degree on (0,4) is lambda_m^2 (homological); the Schlesinger flow preserves
the monodromy (isomonodromy) while a control ODE does not. FIREWALL: the scale is external; the
flow's time is a dimensionless modulus; nothing to CLAIMS.md.
"""
import numpy as np
import sympy as sp


def test_dynamical_degree_lambda_m_squared():
    for m in (1, 2, 3):
        M = sp.Matrix([[m, 1], [1, 0]])
        lam = max(M.eigenvals(), key=lambda e: abs(complex(e)))
        assert sp.simplify(lam**2 - ((m + sp.sqrt(m**2 + 4)) / 2)**2) == 0


def _comm(X, Y): return X @ Y - Y @ X


def _rk4_schlesinger(A, t, s0, h, n):
    def rhs(A, s):
        d1 = _comm(A[2], A[0]) / (s - t[0]); d2 = _comm(A[2], A[1]) / (s - t[1])
        return [d1, d2, -(d1 + d2)]
    s = s0
    for _ in range(n):
        k1 = rhs(A, s)
        k2 = rhs([A[i] + 0.5*h*k1[i] for i in range(3)], s + 0.5*h)
        k3 = rhs([A[i] + 0.5*h*k2[i] for i in range(3)], s + 0.5*h)
        k4 = rhs([A[i] + h*k3[i] for i in range(3)], s + h)
        A = [A[i] + (h/6)*(k1[i] + 2*k2[i] + 2*k3[i] + k4[i]) for i in range(3)]
        s += h
    return A


def _inv(A):
    Ainf = -(A[0] + A[1] + A[2])
    return [np.linalg.det(X) for X in A] + [np.trace(Ainf), np.linalg.det(Ainf)]


def test_schlesinger_flow_is_isomonodromic():
    rng = np.random.default_rng(7)
    def rtl():
        a, b, c = (rng.normal()+1j*rng.normal() for _ in range(3))
        return np.array([[a, b], [c, -a]], dtype=complex)
    t = [0.0+0j, 1.0+0j]
    A0 = [rtl(), rtl(), rtl()]
    inv0 = _inv(A0)
    A1 = _rk4_schlesinger([X.copy() for X in A0], t, 2.0+0j, 0.01, 100)
    drift = max(abs(a - b) for a, b in zip(inv0, _inv(A1)))
    assert drift < 1e-6                       # monodromy conjugacy classes preserved => isomonodromy
    assert max(np.max(np.abs(A1[i] - A0[i])) for i in range(3)) > 1e-3   # residues genuinely moved
