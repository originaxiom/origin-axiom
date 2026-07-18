"""Lock: the divided-power law at sampled n + the banked witnesses."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..",
                                "frontier", "B674_generation_leg"))
from divided_power_law import series, v5den, s5  # noqa: E402


def test_divided_power_law_sampled():
    ser = series()
    for n in (1, 7, 10, 25, 40, 63, 80, 100, 119):
        assert v5den(ser[n]) == n + (n - s5(n)) // 4
    assert v5den(ser[10]) == 12 and v5den(ser[40]) == 49
    assert v5den(ser[119]) == 146
    assert all(ser[n].denominator % 3 != 0 for n in range(121))
