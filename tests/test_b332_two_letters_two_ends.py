"""B332 -- the two ends are the product and ratio of the founding letters (Chat-1 handoff). sympy-only."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B332_two_letters_two_ends'))
import sympy as sp
from two_letters_two_ends import (identity_g_is_signed_ratio, product_and_ratio_ends,
                                  g_commensurates_not_normalizes, L)


def test_founding_identity_g_is_signed_ratio():
    i1, i2 = identity_g_is_signed_ratio()
    assert i1 and i2                       # g = -R L^-1 ; g^-1 a = -L, exact


def test_product_is_sqrt5_ratio_is_sqrt_minus3():
    ends = product_and_ratio_ends()
    assert ends["product RL"] == (3, 5)            # golden -> E8
    assert ends["ratio g=-RL^-1"] == (-1, -3)      # Eisenstein -> E6  (corrects Chat-1's labeling)


def test_g_commensurates_not_normalizes():
    assert g_commensurates_not_normalizes() == L.inv()   # gag^-1 = L^-1 (real; index=3 NOT claimed)
