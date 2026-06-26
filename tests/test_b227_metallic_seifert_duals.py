"""B227 / L45 -- the metallic SUSY chains have explicit Seifert 3-manifold duals. Nothing to CLAIMS.md.

Load-bearing locks (exact):
  - the metallic chain m -> M(m^2+4, m^2+3); the Gang-Kang-Kim recipe with (R,S)=(1,1) (PS-QR=1) gives
    the Seifert space; m=1 reproduces the paper's TCI Seifert (|H_1|=83).
  - cone orders = (m^2+4, m^2+3, 3); the largest = the metallic discriminant m^2+4.
  - |H_1| = 4m^4 + 28m^2 + 51 = (2m^2+7)^2 + 2.
"""
import os
import sys
from fractions import Fraction as Fr

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "frontier", "B227_metallic_seifert_duals"))
from metallic_seifert import (  # noqa: E402
    metallic_minimal_model, seifert_data, h1_order, euler_number, cone_orders,
)


def test_metallic_model_and_sl2z_condition():
    assert metallic_minimal_model(1) == (5, 4)         # golden = TCI M(4,5) (P>Q convention)
    for m in range(1, 12):
        P, Q = metallic_minimal_model(m)
        assert (P, Q) == (m * m + 4, m * m + 3)
        # the recipe's SL(2,Z) condition P*S - Q*R = 1 with (R,S)=(1,1)
        assert P * 1 - Q * 1 == 1


def test_m1_reproduces_paper_tci():
    # m=1 Seifert vs the paper's TCI S^2((5,-1),(4,5),(3,1)) -- same 3-manifold (|H_1| invariant)
    assert h1_order(seifert_data(1)[0], 0) == 83
    assert h1_order([(5, -1), (4, 5), (3, 1)], 0) == 83


def test_cone_orders_largest_is_metallic_discriminant():
    for m in range(1, 12):
        c = cone_orders(m)
        assert c == (m * m + 4, m * m + 3, 3)
        assert max(c) == m * m + 4                      # the metallic discriminant


def test_h1_quartic_and_euler_consistency():
    for m in range(1, 12):
        fib, b = seifert_data(m)
        h1 = h1_order(fib, b)
        assert h1 == 4 * m**4 + 28 * m**2 + 51 == (2 * m**2 + 7)**2 + 2
        # |H_1| = alpha1*alpha2*alpha3 * |e|  (e != 0 -> finite H_1)
        P, Q = metallic_minimal_model(m)
        assert euler_number(fib, b) == Fr(-h1, 3 * P * Q)


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_"):
            fn(); print(f"{name}  PASS")
    print("ALL CHECKS PASS")
