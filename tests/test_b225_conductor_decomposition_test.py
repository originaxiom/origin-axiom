"""B225 -- conductor-decomposition test: 5=golden filling holds; 2=octahedral parent REFUTED. Nothing to CLAIMS.md.

Load-bearing locks:
  - pipeline validation: the figure-eight character variety reproduces B211's Phi and bad primes {2,5}=40a1.
  - SOLID: the figure-eight branch locus is (x^2-1)(x^2-5); the x^2=5 branch = the golden monodromy disc (t^2-4=5).
  - REFUTED (2=parent): prime 2 appears in NON-twist 2-bridge knots (6_2, 6_3) too -- it is universal, not the
    octahedral-parent signature.
"""
import os
import sys

import sympy as sp

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "frontier", "B225_conductor_decomposition_test"))
from conductor_test import char_variety, bad_primes, branch_locus  # noqa: E402

x, z = sp.symbols('x z')


def test_pipeline_validates_against_40a1():
    Phi = char_variety(5, 3)                       # figure-eight b(5,3)
    assert sp.expand(Phi - (z**2 - (x**2 + 1) * z + (2 * x**2 - 1))) == 0   # = B211
    assert bad_primes(Phi) == [2, 5]              # = conductor of 40a1


def test_five_is_the_golden_filling():
    # figure-eight branch locus (x^2-1)(x^2-5): the x^2=5 branch = golden monodromy disc t^2-4=5 (trace 3)
    Phi = char_variety(5, 3)
    Dr = sp.Poly(sp.expand(branch_locus(Phi)), x)
    assert sp.rem(Dr, sp.Poly(x**2 - 5, x)) == 0   # (x^2 - 5) divides the branch locus


def test_two_is_universal_not_octahedral_parent():
    # the twist knots (Whitehead fillings) AND non-twist 2-bridge knots all have prime 2 -> 2 is NOT
    # the octahedral-parent signature (it does not discriminate Whitehead fillings).
    for p, q in [(5, 2), (7, 3)]:                  # twist / Whitehead fillings
        assert 2 in bad_primes(char_variety(p, q))
    for p, q in [(11, 3), (13, 5)]:               # 6_2, 6_3 -- NON-twist, NOT Whitehead fillings
        assert 2 in bad_primes(char_variety(p, q))


def test_simplest_knots_are_two_and_determinant():
    assert bad_primes(char_variety(5, 3)) == [2, 5]    # 4_1: {2, det=5}
    bp52 = bad_primes(char_variety(7, 3))              # 5_2: {2, det=7}
    assert 2 in bp52 and 7 in bp52


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_"):
            fn(); print(f"{name}  PASS")
    print("ALL CHECKS PASS")
