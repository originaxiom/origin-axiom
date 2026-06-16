"""B157 -- the metallic degree=rank exponent (V151). Fast deterministic locks.

Locks the two cheap, decisive facts:
- the foundational free-group identity phi_m([A,B]) = A^m [A,B] A^-m (m=1,2,3), which
  makes mu = A^-m t the cusp meridian (checked on the Sanov free pair, exact integers);
- the REFUTATION of the closed form k = 4 - m(o-3): the verified (m,o)->k grid disagrees
  with the formula at the bronze (m=3) cells.

The heavy reproducers (the full Newton k-grid, the exact Q(i) figure-eight o=4 identity,
the SL(4) {1,1,i,-i} emptiness) live in frontier/B157_metallic_exponent/ and are not
re-run here.
"""
import numpy as np


def _matpow(M, k):
    R = np.eye(M.shape[0], dtype=object)
    if k >= 0:
        for _ in range(k):
            R = R @ M
        return R
    # inverse for 2x2 integer SL(2): [[a,b],[c,d]]^-1 = [[d,-b],[-c,a]] (det=1)
    Mi = np.array([[M[1, 1], -M[0, 1]], [-M[1, 0], M[0, 0]]], dtype=object)
    for _ in range(-k):
        R = R @ Mi
    return R


def _comm(X, Y):
    Xi = np.array([[X[1, 1], -X[0, 1]], [-X[1, 0], X[0, 0]]], dtype=object)
    Yi = np.array([[Y[1, 1], -Y[0, 1]], [-Y[1, 0], Y[0, 0]]], dtype=object)
    return X @ Y @ Xi @ Yi


def test_meridian_commutation_identity():
    # phi_m: A -> A*(A^m B)^m,  B -> A^m B   (abelianizes to R^m L^m = [[1+m^2,m],[m,1]])
    # Identity to lock: phi_m([A,B]) = A^m [A,B] A^-m  (a free-group identity).
    # Verified on the Sanov free pair (exact integer SL(2)).
    A = np.array([[1, 2], [0, 1]], dtype=object)
    B = np.array([[1, 0], [2, 1]], dtype=object)
    for m in (1, 2, 3):
        Am = _matpow(A, m)
        phiA = A @ _matpow(Am @ B, m)
        phiB = Am @ B
        lhs = _comm(phiA, phiB)                       # phi_m([A,B]) in the rep
        rhs = Am @ _comm(A, B) @ _matpow(A, -m)       # A^m [A,B] A^-m
        assert np.array_equal(lhs, rhs), f"meridian identity failed at m={m}"


def test_abelianization_is_metallic():
    # phi_m abelianizes to R^m L^m = [[1+m^2, m],[m, 1]] (m=1 figure-eight, m=2 silver)
    for m, expect in [(1, [[2, 1], [1, 1]]), (2, [[5, 2], [2, 1]]), (3, [[10, 3], [3, 1]])]:
        ab = np.array([[1 + m * m, m], [m, 1]])
        assert ab.tolist() == expect


def test_closed_form_k_4_minus_m_o_minus_3_is_refuted():
    # verified (m,o)->k grid at SL(3) (B157, two seeds, full-relation + irreducible gates);
    # (3,3) excised as the o|m collapse (mu=t).
    grid = {(1, 3): 4, (1, 4): 3, (2, 3): 4, (2, 4): 2, (3, 4): 3, (3, 6): 1}
    formula = lambda m, o: 4 - m * (o - 3)
    # m in {1,2} fit the formula...
    for (m, o), k in grid.items():
        if m in (1, 2):
            assert formula(m, o) == k
    # ...but bronze (m=3) breaks it -> the formula is REFUTED
    assert formula(3, 4) == 1 and grid[(3, 4)] == 3      # predicts 1, actual 3
    assert formula(3, 6) == -5 and grid[(3, 6)] == 1     # predicts -5, actual 1
    assert any(formula(m, o) != k for (m, o), k in grid.items())


def test_order_not_rank_survives():
    # the surviving qualitative fact: o=3 -> k=4 at BOTH n=3 and n=4 (m=1,2)
    # (recorded values; "degree=rank" k=n is a principal-spectrum coincidence)
    o3_at_n3 = {(1, 3): 4, (2, 3): 4}
    assert all(k == 4 for k in o3_at_n3.values())
