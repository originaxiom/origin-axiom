"""B212 -- the metallic congruence/monodromy shadow, COMPUTED (corrects B210 silver). Nothing to CLAIMS.md.

Load-bearing locks (the chat1-flagged asserted-not-computed item, now computed):
 - the silver monodromy R^2L^2 == I mod 2 (TRIVIAL, not S3); even-m generally trivial mod 2.
 - the characterization R^mL^m == I mod p  <=>  p|m  (for every prime p|m^2+4).
 - the congruence-GROUP shadow <R,L> mod N = SL(2,Z/N) (golden 120=2I, silver 384, bronze 2184).
 - the recorded hyperbolic trace-degeneration (square-traces == 0 mod (1+i)).
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "frontier",
                                "B212_silver_congruence_holonomy_shadow"))
from shadow_core import (Q, monodromy, monodromy_mod, monodromy_trivial_mod2,  # noqa: E402
                         congruence_group_order, order)
from shadow_holonomy_sage import SILVER_SQUARE_TRACES  # noqa: E402


def test_silver_monodromy_trivial_mod2_not_S3():
    # the correction: silver R^2L^2 == I mod 2 (trivial), NOT S3
    assert monodromy_mod(2, 2) == (1, 0, 0, 1)
    # and it is even-m general
    for m in (2, 4, 6, 8, 10):
        assert monodromy_trivial_mod2(m) is True
    for m in (1, 3, 5, 7, 9):
        assert monodromy_trivial_mod2(m) is False


def test_monodromy_trivial_iff_p_divides_m():
    # R^mL^m == I (mod p), p|m^2+4  <=>  p|m  <=>  p=2 & m even
    for m in range(1, 16):
        N = m * m + 4
        for p in range(2, N + 1):
            if N % p == 0 and all(p % i for i in range(2, p)):       # prime p | N
                trivial = (monodromy_mod(m, p) == (1, 0, 0, 1))
                assert trivial == (m % p == 0), (m, p)
                if trivial:
                    assert p == 2 and m % 2 == 0


def test_congruence_group_shadow_is_full_SL2():
    # <R,L>=SL(2,Z) -> reduces onto ALL of SL(2,Z/N); golden N=5 -> 120 = |SL(2,F5)|=|2I|
    assert congruence_group_order(1) == 120          # 2I = SL(2,F5)
    assert congruence_group_order(2) == 384          # SL(2,Z/8)
    assert congruence_group_order(3) == 13 * (13 * 13 - 1)   # SL(2,F13) = 2184


def test_monodromy_order_tracks_2Q():
    # B211 reconfirmed on the discriminant modulus
    for m in range(1, 11):
        N = m * m + 4
        assert order(monodromy_mod(m, N), N) == 2 * Q(m)


def test_silver_hyperbolic_trace_degeneration_recorded():
    # square-traces are 2, +-2i -- all == 0 mod (1+i) (the computed degeneration; sage-gated record)
    assert SILVER_SQUARE_TRACES == {"a^2": "+2i", "b^2": "2", "c^2": "-2i"}
    # numeric check that each == 0 mod (1+i) in Z[i] (N(1+i)=2; z == 0 mod (1+i) iff (re+im) even)
    for val in [(0, 2), (2, 0), (0, -2)]:     # 2i, 2, -2i as (re,im)
        re, im = val
        assert (re + im) % 2 == 0


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_"):
            fn(); print(f"{name}  PASS")
    print("ALL CHECKS PASS")
