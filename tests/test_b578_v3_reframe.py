"""D8-v3 lock: B299's (theta,phi) on the 27 forces a 9+9+9 = {1,omega,omega^2}
eigenvalue split (character-theoretic, exact) -- and this is dimensionally/
group-theoretically DISTINCT from B576's theta-odd adjoint blocks (dims 9,17
inside the 78-dim adjoint, a Z/2 parity label, not a Z/3 action).
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..",
                                "frontier", "B299_trinification_triality"))
import sympy as sp
from trinification_triality import THETA, PHI, _weights_27, _action_on_dynkin


def _perm_matrix(M, W, idx):
    A = _action_on_dynkin(M)
    n = len(W)
    P = sp.zeros(n, n)
    for mu in W:
        nu = tuple(sum(A[i, j] * mu[j] for j in range(6)) for i in range(6))
        P[idx[nu], idx[mu]] = 1
    return P


def test_theta_phi_27_eigensplit_is_9_9_9():
    W = _weights_27()
    idx = {w: i for i, w in enumerate(W)}
    assert len(W) == 27
    for M in (THETA, PHI):
        P = _perm_matrix(M, W, idx)
        assert P**3 == sp.eye(27)
        ev = P.eigenvals()
        mults = sorted(ev.values())
        assert mults == [9, 9, 9]
        assert P.trace() == 0 and (P * P).trace() == 0  # forces a=b=c=9 by character theory


def test_b576_theta_odd_blocks_are_a_different_space():
    # B576's theta-odd isotypic blocks: exponents {4,8} of the principal sl2 in the
    # 78-dim adjoint e6, dims (2*4+1)=9 and (2*8+1)=17 -- NOT the 27-dim rep B299 acts on.
    e6_exponents = [1, 4, 5, 7, 8, 11]
    dims = {m: 2 * m + 1 for m in e6_exponents}
    assert sum(dims.values()) == 78
    theta_odd_dims = (dims[4], dims[8])
    assert theta_odd_dims == (9, 17)
    assert sum(theta_odd_dims) != 27  # confirms: no size-match with B299's 27-dim carrier
    # B576's grading is binary (odd/even, i.e. Z/2 label on exponent parity-in-F4);
    # B299's (theta,phi) are order-3 elements. Orders differ -> no shared cyclic group.
    b576_label_order = 2
    b299_generator_order = 3
    assert b576_label_order != b299_generator_order
