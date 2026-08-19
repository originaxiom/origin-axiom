"""B1084 lock: the flat G2 cone's census and stabilizers (float pipeline, fast)."""
import numpy as np
import itertools
import pytest

TOL = 1e-9

def _qmul(p, q):
    a1, b1, c1, d1 = p; a2, b2, c2, d2 = q
    return np.array([a1*a2 - b1*b2 - c1*c2 - d1*d2,
                     a1*b2 + b1*a2 + c1*d2 - d1*c2,
                     a1*c2 - b1*d2 + c1*a2 + d1*b2,
                     a1*d2 + b1*c2 - c1*b2 + d1*a2])

_E4 = [np.eye(4)[i] for i in range(4)]

def _lmat(q): return np.array([_qmul(q, e) for e in _E4]).T
def _rmat(p): return np.array([_qmul(e, p) for e in _E4]).T

def _bd(A, B):
    n = A.shape[0] + B.shape[0]
    M = np.zeros((n, n)); M[:A.shape[0], :A.shape[0]] = A; M[A.shape[0]:, A.shape[0]:] = B
    return M

@pytest.fixture(scope="module")
def group():
    twoT = []
    for idx in range(4):
        for s in (1, -1):
            v = np.zeros(4); v[idx] = s; twoT.append(v)
    for signs in itertools.product((1, -1), repeat=4):
        twoT.append(np.array(signs) * 0.5)
    i_q = np.array([0., 1, 0, 0]); k_q = np.array([0., 0, 0, 1])
    w_q = np.array([1, 1, 0, 0]) / np.sqrt(2)
    g_tau = _bd(np.diag([1., -1, -1]), _rmat(i_q))
    g_sigma = _bd(np.diag([-1., -1, 1]), _lmat(w_q) @ _rmat(k_q))
    gens = [_bd(np.eye(3), _lmat(q)) for q in twoT] + [g_tau, g_sigma]
    key = lambda M: tuple(np.round(M.flatten(), 7))
    seen = {key(np.eye(7)): np.eye(7)}
    frontier = [np.eye(7)]
    while frontier:
        nxt = []
        for M in frontier:
            for g in gens:
                P = M @ g; k = key(P)
                if k not in seen:
                    seen[k] = P; nxt.append(P)
        frontier = nxt
    return list(seen.values())

def test_order_96(group):
    assert len(group) == 96

def test_census_53_42_no_isolated(group):
    census = {}
    for M in group:
        d = 7 - np.linalg.matrix_rank(M - np.eye(7), tol=TOL)
        if d == 7: continue
        census[d] = census.get(d, 0) + 1
    assert census == {3: 53, 1: 42}   # NO 0-dim fixed set: the AW isolation failure

def test_r3_stabilizer_is_2T(group):
    stab = [M for M in group if np.allclose(M[:3, :3], np.eye(3), atol=TOL)]
    assert len(stab) == 24

def test_axis_stabilizers_48(group):
    for idx in range(3):
        v = np.zeros(7); v[idx] = 1
        assert sum(1 for M in group if np.allclose(M @ v, v, atol=TOL)) == 48
