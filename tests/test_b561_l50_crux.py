"""B561 — the L50 CRUX computed: no Eisenstein Z/3 selects SU(3)^2 in F4.

The proposed E6 ->[theta] F4 ->[Z/3?] SU(3)^2 chain: Step 1 is forced (B353), and
group theory says an order-3 element of F4 has centralizer A2 x A2~ = SU(3)xSU(3).
BUT the figure-eight provides no order-3 automorphism at its hyperbolic point:
  - the theta-even F4 exponents {1,5,7,11} = (Z/12)* = Klein four (Z/2 x Z/2), NO order-3;
  - the figure-eight isometry group is D4 (order 8): element orders 1,2,4 only;
  - the trace field Q(sqrt-3) has Galois group Z/2, not Z/3 (omega is a field element);
  - (B257) the order-3 Eisenstein rotation lives at the collapsed Euclidean point x=1.
See frontier/B561_l50_crux/FINDINGS.md.
"""
from math import gcd


def test_theta_grading_gives_F4_exponents():
    E6 = [1, 4, 5, 7, 8, 11]
    even = [m for m in E6 if (-1) ** (m + 1) == 1]
    odd = [m for m in E6 if (-1) ** (m + 1) == -1]
    assert even == [1, 5, 7, 11]        # F4 exponents (theta-even = F4 sector)
    assert odd == [4, 8]                # the 26 complement


def test_F4_exponent_group_is_klein_four_no_order3():
    units12 = [m for m in range(1, 12) if gcd(m, 12) == 1]
    assert units12 == [1, 5, 7, 11]     # F4 exponents ARE (Z/12)*

    def order_mod(a, n):
        x, k = a % n, 1
        while x != 1:
            x = (x * a) % n
            k += 1
        return k
    orders = {m: order_mod(m, 12) for m in units12}
    assert set(orders.values()) == {1, 2}          # Klein four: no order-3 element
    assert 3 not in orders.values()


def test_figure_eight_has_no_order3_symmetry():
    import pytest
    snappy = pytest.importorskip("snappy")
    G = snappy.Manifold("4_1").symmetry_group()
    assert G.order() == 8               # D4 -> element orders divide 8 -> {1,2,4}, no order-3
    assert 8 % 3 != 0                   # Lagrange: no order-3 element in a group of order 8
