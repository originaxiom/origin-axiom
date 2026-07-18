"""B681 lock — the pre-test decomposition (denominator-level necessary cond)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..",
                                "frontier", "B681_habiro_pretest"))
from pretest import v5_factorial, v5_int, divided_power_v5  # noqa


def test_decomposition_exact():
    for n, tgt in {1: 1, 10: 12, 40: 49, 80: 99, 119: 146}.items():
        assert v5_factorial(n) == v5_int(math.factorial(n))
        assert divided_power_v5(n) == n + v5_factorial(n) == tgt
