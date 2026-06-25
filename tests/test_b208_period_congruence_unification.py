"""B208 -- WRT period (B204) and congruence shadow (B206) are the same arithmetic (det(gamma+I)=m^2+4).
The field radicand squarefree(m^2+4) always divides the period; at golden it is 5 = the McKay prime."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "frontier", "B208_period_congruence_unification"))
from period_congruence import wrt_period, det_gamma_plus_I, radicand  # noqa: E402


def test_radicand_divides_period():
    assert all(wrt_period(m) % radicand(m) == 0 for m in range(1, 300))


def test_golden_collapse():
    # period = det(gamma+I) = field discriminant = McKay prime = 5 at m=1
    assert wrt_period(1) == 5
    assert det_gamma_plus_I(1) == 5
    assert radicand(1) == 5


def test_det_gamma_plus_I_is_m2_plus_4():
    assert all(det_gamma_plus_I(m) == m * m + 4 for m in range(1, 50))


if __name__ == "__main__":
    test_radicand_divides_period()
    test_golden_collapse()
    test_det_gamma_plus_I_is_m2_plus_4()
    print("ALL CHECKS PASS")
