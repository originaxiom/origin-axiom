"""B218 -- metallic multiplicity selects golden as the unique anyon theory (Jones-index). Nothing to CLAIMS.md.

Load-bearing lock: the selection is EXACT -- lambda_m < 2 (anyon-realizable) iff m=1, and lambda_1=2cos(pi/5).
(The chain-level CFT c=7/10 is CITED, not tested -- the in-sandbox ED was inconclusive; see FINDINGS.)
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "frontier", "B218_metallic_anyon_selection"))
from jones_selection import lam, realizable, is_fibonacci_golden  # noqa: E402


def test_golden_unique_anyon_realizable():
    # exact Jones-index selection: only m=1 has lambda_m < 2 (a quantized unitary anyon dimension)
    assert realizable(1) is True
    assert all(realizable(m) is False for m in range(2, 60))
    assert [m for m in range(1, 200) if realizable(m)] == [1]


def test_golden_is_the_fibonacci_anyon():
    # lambda_1 = 2cos(pi/5) = phi exactly (the Fibonacci anyon, SU(2)_3, the dual-McKay E8 point)
    assert is_fibonacci_golden()
    phi = (1 + 5 ** 0.5) / 2
    assert abs(lam(1) - phi) < 1e-12


def test_metallic_means_above_the_wall():
    # m>=2 are above the Jones index-4 wall: lambda_m >= 1+sqrt2 > 2, index lambda_m^2 > 4
    for m in range(2, 12):
        assert lam(m) > 2 and lam(m) ** 2 > 4


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_"):
            fn(); print(f"{name}  PASS")
    print("ALL CHECKS PASS")
