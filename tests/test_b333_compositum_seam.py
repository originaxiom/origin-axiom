"""B333 -- the compositum seam probe (Chat-1 handoff). Firewall holds at Q(sqrt-15). sympy-only."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B333_compositum_seam'))
from compositum_seam import sqrt5_times_sqrtm3_is_sqrtm15, class_number, null_test


def test_sqrt_product_is_sqrt_minus15():
    assert sqrt5_times_sqrtm3_is_sqrtm15()


def test_class_number_minus15_is_two():
    assert class_number(-15) == 2                 # Chat-1's claim, verified


def test_null_test_field_is_generic():
    h15, same, total, generic = null_test()
    assert h15 == 2
    assert generic and same > 1                   # h=2 shared by many -> Q(sqrt-15) generic -> firewall holds
    # sanity: class_number of a well-known h=1 field
    assert class_number(-163) == 1
