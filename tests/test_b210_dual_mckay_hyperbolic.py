"""B210 -- golden's dual McKay (E8 monodromy / E6 hyperbolic); WRT image != 2I. Nothing to CLAIMS.md.
The hyperbolic trace fields are recorded from sage-python (SnapPy invariant_trace_field_gens); the
McKay-structure + WRT-image parts are pyenv-verifiable."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "frontier", "B210_dual_mckay_hyperbolic"))
from dual_mckay import sl2_order, wrt_image_order_su2_3, HYP_TRACE_FIELDS, mckay_at_prime  # noqa: E402


def test_dual_mckay_exceptional_primes():
    # SL(2,F3)=2T=E6 (24), SL(2,F5)=2I=E8 (120); E7=2O (48) is not an SL(2,Fp) order
    assert sl2_order(3) == 24 and sl2_order(5) == 120
    assert 48 not in [sl2_order(p) for p in range(2, 300)]
    assert mckay_at_prime(3) == "2T=E6" and mckay_at_prime(5) == "2I=E8"


def test_golden_hyperbolic_field_is_eisenstein():
    # golden = figure-eight = m004, invariant trace field x^2-x+1 = Q(sqrt-3), ramified at 3
    assert HYP_TRACE_FIELDS[1] == ("m004", "x^2-x+1", 2, "Q(sqrt-3)")
    # silver = m136 = Q(i), ramified at 2 (degenerate)
    assert HYP_TRACE_FIELDS[2] == ("m136", "x^2+1", 2, "Q(i)")


def test_figure_eight_surjects_onto_2T_E6_mod3():
    # VERIFIED (not asserted): figure-eight holonomy mod (sqrt-3) = SL(2,F3) = 2T = E6 (order 24)
    from dual_mckay import figure_eight_mod3_image
    assert figure_eight_mod3_image() == 24


def test_wrt_image_is_not_2I():
    # the WRT modular-rep image at the golden level is NOT 2I (order 2880, SL(2,Z/20)-related)
    o = wrt_image_order_su2_3()
    assert o == 2880 and o != 120


if __name__ == "__main__":
    test_dual_mckay_exceptional_primes()
    test_golden_hyperbolic_field_is_eisenstein()
    test_wrt_image_is_not_2I()
    print("ALL CHECKS PASS")
