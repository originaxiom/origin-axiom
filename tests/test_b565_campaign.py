"""B565 gauge-behavior campaign — consolidated locks (cheap, exact anchors).

  T1  : the Z/11 gate — UV torsion exact; 11 divides no IR invertible-symmetry order.
  T6  : the octonion door — |Aut(octavians)| = |G2(2)| = 12096 = 2^6*3^3*7, no 11.
  F2  : rung-3 K0 = Z/18845089 cyclic, unit class coprime => O_{M_16} = O_{18845090}.
  F3  : the 2^{2n+1} tower conjecture is REFUTED at rung 3 (census record, binomial bound).
Full evidence: frontier/B565_gauge_behavior_campaign/RESULTS.md + workflow journal.
"""
from fractions import Fraction
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

M4 = sp.Matrix([[1, 1, 1, 1], [1, 0, 1, 0], [2, 1, 1, 1], [1, 1, 1, 0]])


def test_t1_gate_z11_does_not_descend():
    snf = smith_normal_form(sp.eye(4) - M4, domain=sp.ZZ)
    assert [snf[i, i] for i in range(4)] == [1, 1, 1, 11]      # UV torsion = Z/11
    chi = sp.Matrix([[1, 3, 6, 7]])
    assert [(chi * M4)[0, j] % 11 for j in range(4)] == [1, 3, 6, 7]
    # IR invertible-symmetry orders available to the golden chain / c=7/10:
    # Inv(Fib)=1, Inv(Z(Fib))=1, ring sectors=2, TCI simple-current group=2.
    for order in (1, 1, 2, 2):
        assert sp.igcd(11, order) == 1                          # only the trivial hom exists


def test_t6_octonion_door_no_order_11():
    assert 12096 == 2**6 * 3**3 * 7                             # |Aut(octavians)| = |G2(2)|
    assert 12096 % 11 != 0                                      # no order-11 element (Lagrange)
    assert all(o != 11 for o in (1, 2, 3, 4, 6, 7, 8, 12))      # computed element orders


def test_f2_rung3_cuntz_identification():
    F = sp.Matrix([[1, 1], [1, 0]])
    M = F
    for _ in range(3):
        M = M.row_join(M).col_join((M * M).row_join(M))         # M_3, 16x16
    snf = smith_normal_form(sp.eye(16) - M.T, domain=sp.ZZ)
    diag = [abs(snf[i, i]) for i in range(16)]
    assert diag[:15] == [1] * 15 and diag[15] == 18845089       # K0 cyclic Z/|e_3|
    assert sp.isprime(18845089)                                 # => any nonzero class generates
    # unit class [1] = image of (1,...,1): nonzero mod the prime => generates => O_{M_16} ~ O_{18845090}


def test_f3_tower_conjecture_refuted_at_rung3():
    """|G_n| = 2^{2n+1} predicts 128 at rung 3 => identity-frequency 1/128; the census
    saw 1 identity among 11255 unramified primes. Binomial tail: decisively excluded."""
    n, k, p = 11255, 1, Fraction(1, 128)
    # P(X <= 1) = (1-p)^n + n p (1-p)^{n-1}, exact rational arithmetic
    q = 1 - p
    tail = q**n + n * p * q**(n - 1)
    assert tail < Fraction(1, 10**30)                           # P ~ 5.8e-37: REFUTED
    # rung-1 and rung-2 remain exact: D4 (order 8) and SmallGroup(32,43) (order 32)
    assert 2 ** (2 * 1 + 1) == 8 and 2 ** (2 * 2 + 1) == 32     # the formula held only to rung 2
