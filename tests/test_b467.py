"""B467 — locks: the parity table, the H112 identity + refutation, the corrected
ratios, and the oriented wall-merge fact."""
import os
import sys
from math import sqrt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "frontier", "B467_family_residue_wall"))

from f2_parity import perm_sign_of_map, linmap, mm, N
from itertools import product


def test_parity_only_odd_bit_is_the_half_monodromy():
    dom = list(product(range(N), repeat=2))
    A1 = [[2, 1], [1, 1]]
    A2 = [[5, 2], [2, 1]]
    NEG = [[N - 1, 0], [0, N - 1]]
    assert perm_sign_of_map(linmap(A1), dom) == 1
    assert perm_sign_of_map(linmap(A2), dom) == 1
    assert perm_sign_of_map(linmap(mm(NEG, mm(A1, A2))), dom) == 1
    assert perm_sign_of_map(linmap([[1, 1], [1, 0]]), dom) == -1   # sigma, det -1


def test_h112_identity_and_refutation():
    def Amat(m):
        return [[m * m + 1, m], [m, 1]]
    def tr_prod(m, n):
        A, B = Amat(m), Amat(n)
        return A[0][0]*B[0][0] + A[0][1]*B[1][0] + A[1][0]*B[0][1] + A[1][1]*B[1][1]
    for m in range(1, 7):
        for n in range(m, 7):
            assert tr_prod(m, n) == (m*n + 1)**2 + m*m + n*n + 1
    assert tr_prod(1, 2) == 15          # the seam-level coincidence
    assert tr_prod(1, 3) == 27 != 65    # the naive conductor law dies here


def test_corrected_ratios():
    a = lambda m: (m + sqrt(m*m + 4)) / 2
    assert abs(a(1)/a(2) - 0.670212) < 1e-6      # not Chat-1's 0.6686
    assert abs(a(2)/a(3) - 0.730965) < 1e-6      # not Chat-1's 0.7346


def test_wall_merge_oriented():
    import snappy
    A = snappy.Manifold('4_1')
    A.chern_simons()
    A.dehn_fill((-5, 1))
    B = snappy.Manifold('5_2')
    B.chern_simons()
    B.dehn_fill((5, 1))
    assert abs(float(A.volume()) - 0.9813688289) < 1e-8
    assert abs(float(A.chern_simons()) - float(B.chern_simons())) < 1e-9
    assert A.is_isometric_to(B)     # oriented: 5_2(5,1) = 4_1(-5,1)
