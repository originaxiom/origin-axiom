"""B8081 — ρ built, not cited.

Reads `results.json` (computed) and never prose. The targets are the paper's own numbers,
so a drift in either the construction or the paper breaks these.
"""
import json
import os

import pytest

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "..", "frontier", "B8081_rho_rebuilt", "results.json")


@pytest.fixture(scope="module")
def r():
    with open(RES) as fh:
        return json.load(fh)


def test_ord_T_is_15(r):
    """Prop (2880) names ord T = 15. Here it is derived from h = (a²+b²+ab+3a+3b)/15
    and c/24 = 2/15, not assumed."""
    from math import gcd
    from functools import reduce
    assert r["ord_T"] == 15
    assert gcd(reduce(gcd, r["T_exponents_over_15"]), 15) == 1


def test_the_six_primaries_are_the_level_two_weights(r):
    prim = [tuple(x) for x in r["primaries"]]
    assert len(prim) == 6
    assert all(a + b <= 2 for a, b in prim)
    assert sorted(prim) == sorted({(a, b) for a in range(3) for b in range(3)
                                   if a + b <= 2})


def test_the_image_has_order_2880_at_every_prime(r):
    """Proposition (2880), from a built ρ rather than a cited one."""
    assert r["image_order"] == 2880 == 24 * 120
    assert set(r["image_order_by_prime"].values()) == {2880}
    assert len(r["primes"]) >= 2, "the paper's own method is enumeration at two primes"


def test_theta_blocks_are_two_and_four(r):
    """The coupling law's θ is charge conjugation, and its eigenspaces must be 2 and 4."""
    assert sorted(r["theta_block_dims"]) == [2, 4]


def test_the_odd_block_is_360_not_2880(r):
    """Scope (2880) exists to keep these apart: the θ-odd block is 2I×ℤ/3 of order 360,
    the six-dimensional stage is 2880, of index 8."""
    assert r["odd_block_image_order"] == 360
    assert r["image_order"] // r["odd_block_image_order"] == 8


def test_the_63_class_match_holds(r):
    """63 = 7×9, and (size, χ(A)trV₂(B), trV₂(A)trV₂(B)) agrees class by class against an
    independently built quaternion model. This is the coupling law."""
    assert r["n_classes"] == 63 == 7 * 9
    assert r["class_match"] is True


def test_the_primes_admit_zeta_60(r):
    """ℚ(ζ₆₀) is the field the paper's proof names; p ≡ 1 mod 60 puts it in 𝔽ₚ."""
    for p in r["primes"]:
        assert p % 60 == 1
