"""B8080 — the assembly classification refuted.

Reads `results.json` (computed) and never prose. These pin the refutation so it cannot
quietly revert: if a later edit restores "only A₄ and 2T" without changing the definition,
these fail.
"""
import json
import os

import pytest

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "..", "frontier", "B8080_assembly_classification", "results.json")
SIX = ["2I", "2O", "2T", "A4", "A5", "S4"]


@pytest.fixture(scope="module")
def r():
    with open(RES) as fh:
        return json.load(fh)


def test_all_six_admit_an_assembly_so_the_theorem_is_false_as_stated(r):
    assert r["_summary"]["all_six_admit"] is True
    assert sorted(r["_summary"]["survivors"]) == SIX
    assert r["_summary"]["theorem_as_stated"] == "FALSE"


def test_the_two_exclusions_that_matter_are_binary(r):
    """2O and 2I survive and are binary, so Cor (onlybinary) cannot absorb the failure —
    this is what makes the refutation load-bearing rather than cosmetic."""
    for g in ("2O", "2I"):
        assert r[g]["assembly_exists"] is True


def test_the_papers_positive_half_still_stands(r):
    """2T does admit an assembly. The refutation is of uniqueness, not of 2T."""
    assert r["2T"]["assembly_exists"] is True
    assert r["A4"]["assembly_exists"] is True


def test_every_witness_is_valid(r):
    """Each witness must total 27 and use only degrees that carry an invariant cubic.
    Tests the property, not the search order — a different but equally valid witness
    must still pass."""
    for g in SIX:
        w = r[g]["witness"]
        assert w, g
        assert sum(d * m for d, m in w) == 27, g
        ok = {d for d, _ in r[g]["irreps_with_invariant_cubic"]}
        assert all(d in ok for d, _ in w), (g, w, ok)


def test_the_failure_mode_is_multiplicity_not_triviality(r):
    """Every witness is many copies of ONE OR TWO small irreducibles — and for A₄ and 2T
    it is 27 copies of a non-trivial LINEAR character, which is the original refuted
    construction (27 copies of the trivial) barely disguised. Excluding trivial summands
    did not touch the actual defect."""
    for g in SIX:
        assert len(r[g]["witness"]) <= 2, g
    for g in ("A4", "2T"):
        assert r[g]["witness"] == [[1, 27]], g


def test_character_degrees_are_the_real_ones(r):
    """Computed, not transcribed — but they must still come out right."""
    assert sorted(r["A4"]["degrees"]) == [1, 1, 1, 3]
    assert sorted(r["S4"]["degrees"]) == [1, 1, 2, 3, 3]
    assert sorted(r["A5"]["degrees"]) == [1, 3, 3, 4, 5]
    assert sorted(r["2T"]["degrees"]) == [1, 1, 1, 2, 2, 2, 3]
    assert sorted(r["2O"]["degrees"]) == [1, 1, 2, 2, 2, 3, 3, 4]
    assert sorted(r["2I"]["degrees"]) == [1, 2, 2, 3, 3, 4, 4, 5, 6]
    for g in SIX:
        assert sum(d * d for d in r[g]["degrees"]) in (12, 24, 48, 60, 120)


def test_the_icosahedral_threes_carry_no_invariant_cubic(r):
    """Classical: the icosahedral invariant degrees are 2, 6, 10 — no cubic. A control
    this arc did not choose, and the computation must reproduce it."""
    for g in ("A5", "2I"):
        assert all(d != 3 for d, _ in r[g]["irreps_with_invariant_cubic"])


def test_the_prime_puts_every_character_value_in_the_field(r):
    """p ≡ 1 mod 120 = lcm of the six exponents, and p > C(29,3) = 3654 so every
    multiplicity is recovered unambiguously."""
    p = r["_summary"]["prime"]
    assert p % 120 == 1 and p > 3654
