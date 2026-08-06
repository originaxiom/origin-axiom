"""B922 locks: the received value's arithmetic + the clean spot axis."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..",
                                "frontier", "B922_lambda2_receipt"))
import spot_checks  # noqa: E402
import mpmath as mp  # noqa: E402


def test_lambda_equals_one_plus_r_squared():
    lam = spot_checks.arithmetic_identity()
    assert mp.nstr(lam, 12) == "25.0108366633"


def test_h4_axis_clean():
    assert spot_checks.spot_pslq() == []
