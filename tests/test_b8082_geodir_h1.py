"""B8082 — the geodir H¹ count, and the adjective it does not cover.

Reads `results.json` (computed) and never prose.
"""
import json
import os

import pytest

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "..", "frontier", "B8082_geodir_h1", "results.json")
EXPS = ["1", "4", "5", "7", "8", "11"]


@pytest.fixture(scope="module")
def r():
    with open(RES) as fh:
        return json.load(fh)


def test_H1_is_six_dimensional(r):
    """Prop (geodir)'s dimension count, which its scope says the paper does not compute."""
    assert r["total_H1"] == 6
    assert sum(r["H1_by_exponent"][m] for m in EXPS) == 6


def test_the_split_is_one_plus_five(r):
    assert r["split"] == [1, 5]
    assert r["H1_by_exponent"]["1"] == 1
    assert sum(r["H1_by_exponent"][m] for m in EXPS[1:]) == 5


def test_the_exponent_one_block_is_the_embedded_sl2(r):
    """Sym²(V₂) is the adjoint of sl₂ — dimension 3."""
    assert r["block_dims"]["1"] == 3


def test_the_blocks_account_for_e6(r):
    assert r["sum_block_dims"] == 78
    assert sorted(int(x) for x in r["block_dims"].values()) == [3, 9, 11, 15, 17, 23]


def test_H0_vanishes_so_the_count_is_clean(r):
    """H⁰ = 0 makes B¹ full; if it were non-zero the count would need care."""
    assert all(r["H0_by_exponent"][m] == 0 for m in EXPS)


def test_the_six_is_the_exponent_count_not_a_fact_about_which_exponents(r):
    """m = 2, 3, 6 are not E₆ exponents and give 1 as well. So dim H¹ = rank(E₆), and
    the '1+5 split by exponent' is a way of counting — not a discovery about E₆."""
    assert all(v == 1 for v in r["non_exponents_also_one"].values())
    assert set(r["non_exponents_also_one"]) == {"2", "3", "6"}
    assert r["total_H1"] == len(EXPS)


def test_unobstructedness_is_not_claimed(r):
    """The proposition says 'unobstructed'. This arc computes H¹ only, and dim H² = 6,
    so the obstruction space is non-zero and no dimension count settles it."""
    assert r["unobstructedness_computed"] is False
    assert r["dim_H2_by_euler_characteristic"] == 6
    assert "owed" in r["scope"] and "fully priced choice" in r["scope"]


def test_the_trace_field_control(r):
    """t² − t + 1 = 0 puts the trace field at ℚ(√−3) — the figure-eight's. This is what
    identifies the solution as the geometric representation."""
    assert r["trace_field_poly"] == "t^2 - t + 1"
    assert all(p % 6 == 1 for p in r["primes"])
