"""B219 -- L39 resolved: the class-field period law is P=lcm(t-2,t+2)/content (form content),
fully elementary, NOT genus-theoretic (overturns B216). Nothing to CLAIMS.md.

Fast locks: the content law + the high-content (small-period) WRT period checks that pin the
mechanism (A==5I mod 8 -> content 8; f=16 -> 9I mod 16 -> content 16). The exhaustive f=8 sweep
(all genera, period 80) lives in the reproducer (slower).
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "frontier", "B219_period_content_law"))
from period_content import (  # noqa: E402
    content, law, conductor, scalar_depth_pm, scalar_depth_any, minimal_period, lcm,
    trace_classes, GAMMA_A, GAMMA_B,
)


def test_b216_obstruction_is_content():
    # A == 5I mod 8 (5^2==1 mod 8, a non-+-1 root) -> content 8; B content 4. The +-I test misses A.
    assert content(GAMMA_A) == 8 and content(GAMMA_B) == 4
    assert scalar_depth_pm(GAMMA_A, 8) == 4 and scalar_depth_pm(GAMMA_B, 8) == 4   # OLD: both 4 (wrong)
    assert scalar_depth_any(GAMMA_A, 8) == 8 and scalar_depth_any(GAMMA_B, 8) == 4  # content: 8 vs 4


def test_content_equals_any_scalar_depth_and_divides_f():
    for t in range(3, 21):
        f = conductor(t)
        for M in trace_classes(t):
            assert content(M) == scalar_depth_any(M, f)
            assert f % content(M) == 0


def test_extra_sqrt_of_unity_is_2adic():
    # the +-I criterion fails exactly when 8|f: (Z/2^k)^x has 4 square-roots of 1 for k>=3
    assert sorted(s for s in range(8) if s * s % 8 == 1) == [1, 3, 5, 7]
    assert sorted(s for s in range(16) if s * s % 16 == 1) == [1, 7, 9, 15]
    # mod 4 and odd primes: only +-1 (so content==+-I-depth there, why B215 worked for f<=4)
    assert sorted(s for s in range(4) if s * s % 4 == 1) == [1, 3]
    assert sorted(s for s in range(9) if s * s % 9 == 1) == [1, 8]


def test_period_equals_law_high_content_f8():
    # high-content => small period (fast): the decisive content-8/4/2 classes at f=8 (t=18)
    for M in trace_classes(18):
        ct = content(M)
        if ct >= 2:  # periods 40,20,10 -- fast
            pred = 80 // ct
            assert minimal_period(M, cap=pred + 4) == pred == law(M)


def test_period_generalizes_f16():
    # f=16: content-16 rep == 9I mod 16, period 68 = 1088/16
    M = [[41, -64], [-16, 25]]
    assert content(M) == 16
    assert minimal_period(M, cap=lcm(64, 68) // 16 + 4) == 68 == law(M)


def test_reproduces_b204_block_word():
    from math import gcd
    for a in range(1, 6):
        for b in range(1, 6):
            M = [[1 + a * b, a], [b, 1]]
            b204 = lcm(a, b) * (a * b + 4) // gcd(a * b + 4, 4)
            assert law(M) == b204 and content(M) == gcd(a, b)


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_"):
            fn(); print(f"{name}  PASS")
    print("ALL CHECKS PASS")
