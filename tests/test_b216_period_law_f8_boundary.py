"""B216 -- the f>=8 boundary of the class-field period law (L39). Nothing to CLAIMS.md.

Load-bearing locks:
 - the general WRT factorization is CORRECT (validated vs the block-word Z of B204/B214).
 - the obstruction: two non-conjugate trace-18 classes with IDENTICAL elementary invariants
   (scalar-depth 4, order-profile (1,1,2,4)) have DIFFERENT d (8 vs 4) -> the f>=8 split is a finer
   form-class/genus invariant (NEEDS-SPECIALIST), not a scalar-depth/order criterion.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "frontier", "B216_period_law_f8_boundary"))
from general_wrt import (Zabs, Zabs_block, gmat, period, scalar_depth, order_profile,  # noqa: E402
                         conjugate, GAMMA_A, GAMMA_B)


def test_general_wrt_factorization_validated():
    # the tool must reproduce the validated block-word WRT for arbitrary gamma
    for bl in [[(1, 1)], [(2, 3)], [(1, 2), (2, 1)], [(5, 1)], [(4, 4)], [(1, 2), (1, 3)], [(2, 1), (3, 1)]]:
        g = gmat(bl)
        for k in [4, 7, 11, 16]:
            assert abs(Zabs(g, k) - Zabs_block(bl, k)) < 1e-7, (bl, k)


def test_f8_obstruction_d_not_elementary():
    # THE load-bearing obstruction: same elementary invariants, different d
    pA, pB = period(GAMMA_A, maxk=40), period(GAMMA_B, maxk=40)
    assert pA == 10 and pB == 20                       # d = 80/period = 8 and 4
    assert 80 // pA == 8 and 80 // pB == 4
    assert scalar_depth(GAMMA_A) == scalar_depth(GAMMA_B) == 4          # identical scalar-depth
    assert order_profile(GAMMA_A) == order_profile(GAMMA_B) == (1, 1, 2, 4)   # identical order-profile
    assert conjugate(GAMMA_A, GAMMA_B) is False         # yet non-conjugate (different class)
    # => d is NOT a function of scalar-depth or order-mod-2^k : the f>=8 split is finer (genus-level)


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_"):
            fn(); print(f"{name}  PASS")
    print("ALL CHECKS PASS")
