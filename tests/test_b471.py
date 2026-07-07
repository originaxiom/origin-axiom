"""B471 — locks: the uniqueness theorem, the Cohn identities, the chain laws."""
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "frontier", "B471_chain_verification"))

from chain_verify import Am


def test_uniqueness_theorem_closed_form():
    m, n = sp.symbols('m n', positive=True, integer=True)
    x = m*m + 2
    y = n*n + 2
    z = (m*n + 1)**2 + m*m + n*n + 1
    assert sp.expand(x**2 + y**2 + z**2 - x*y*z - 2) == sp.expand(2 - (m*n*(n - m))**2)
    assert 2 - (1*2*1)**2 == -2                      # (1,2) closes the cusp
    assert [2-(1*3*2)**2, 2-(1*4*3)**2, 2-(2*4*2)**2] == [-34, -142, -254]


def test_cohn_identities():
    A1, A2 = Am(1), Am(2)
    g1 = sp.Matrix([[2, 1], [1, 1]])
    g2 = sp.Matrix([[1, 1], [1, 2]])
    assert A1 == g1
    assert sp.simplify(A1 * A2.inv() * A1 - g2) == sp.zeros(2, 2)
    assert sp.simplify(g1 * g2.inv() * g1 - A2) == sp.zeros(2, 2)


def test_chain_markov_conservation_and_parabolicity():
    Sm = {0: Am(2), 1: Am(1)}
    for k in range(2, 10):
        Sm[k] = Sm[k-1] * Sm[k-2]
    u = {k: int(sp.trace(Sm[k])) for k in Sm}
    assert [u[1], u[0], u[2], u[3]] == [3, 6, 15, 39]
    for k in range(0, 8):
        assert u[k]**2 + u[k+1]**2 + u[k+2]**2 == u[k]*u[k+1]*u[k+2]
    for k in range(0, 8):
        assert int(sp.trace(Sm[k]*Sm[k+1]*Sm[k].inv()*Sm[k+1].inv())) == -2


def test_half_chain_twisted_fricke():
    X = {0: sp.Matrix([[2, 1], [1, 0]]), 1: sp.Matrix([[1, 1], [1, 0]])}
    for k in range(2, 10):
        X[k] = X[k-1] * X[k-2]
    v = {k: int(sp.trace(X[k])) for k in X}
    d = {k: int(X[k].det()) for k in X}
    for k in range(2, 9):
        assert v[k+1] == v[k]*v[k-1] - d[k-1]*v[k-2]
